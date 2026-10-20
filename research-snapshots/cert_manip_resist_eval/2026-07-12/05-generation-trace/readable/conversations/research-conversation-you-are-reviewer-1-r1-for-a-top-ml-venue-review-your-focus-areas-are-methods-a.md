# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus areas are **Methods** and **Experiments**. Use a 6-point s

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a1dc3465676d872cd.jsonl`
- **Structured JSON:** [`c61dd306e2c718121d2f.json`](../../sessions/c6/c61dd306e2c718121d2f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-20T19:38:27.298Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus areas are **Methods** and **Experiments**. Use a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target acceptance rate ~25%.

## Paper Summary

**Title**: "Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR"

The paper studies cross-lingual correctness probe transfer for calibration across 20 languages and 3 architectures (Qwen3-235B-A22B MoE 94L, Llama 4 Scout MoE 48L, Gemma 4 31B Dense 60L). Four claims:

1. **Pareto Frontier Discovery**: Deeper layers yield better EN calibration but degrade cross-lingual zero-shot transfer. Optimal transfer depth ~58-60% of model depth. Spearman ρ=0.82-0.88.
2. **Decomposition**: Correctness signal decomposes into difficulty-shared (68% var, language-agnostic, transfers well) and capability-specific (32% var, language-dependent, drives 87% of transfer degradation).
3. **CaCLR**: A training objective (L_BCE + α·L_SB-ECE + β·L_consistency) that shifts the Pareto frontier outward. +5.2pp AUROC over zero-shot, ~40% ECE reduction vs temp scaling, no target-language labels needed.
4. **Orthogonality**: Correctness-confidence orthogonality (cosine<0.1) persists across all 20 languages, with resource-tier gradient (ρ=-0.68).

## Methods Details

- **Probes**: Logistic regression (primary) and 2-layer MLP (comparison), trained on EN correctness labels from GlobalMMLU.
- **Transfer conditions**: Zero-shot, mean-shift, linear projection, few-shot (25/100), CaCLR.
- **CaCLR loss**: L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency. α=0.15, β=0.08. L_consistency penalizes divergence between EN and non-EN probe outputs on parallel activations. L_SB-ECE is soft-binned ECE loss.
- **Pareto frontier**: EN AUROC vs ZS mean AUROC (19 langs) at each probed layer.
- **Decomposition**: IRT difficulty probes (Ridge regression, R²=0.72), project out difficulty direction, retrain on residuals.
- **Orthogonality**: Cosine similarity between correctness direction (from probes) and verbalized confidence direction (from prompted confidence scores).
- **Activations**: Every 4th layer. Llama 4 Scout uses INT8 quantization (validated in Table 16).

## Experimental Results

**Table 1**: Qwen3-235B Pareto Frontier — 24 layers probed, EN AUROC peaks at L72 (0.843), best ZS transfer at L56 (0.762). 6 Pareto-optimal layers (L40-L60). ρ=0.88.

**Table 2**: Transfer conditions at L56 (Qwen3): ZS 0.762/0.098 ECE, mean-shift 0.758/0.101 (degrades!), linear proj 0.781/0.082, few-shot-25 0.748/0.089, few-shot-100 0.771/0.079, CaCLR **0.814/0.058** (40.8% ECE reduction).

**Table 3**: Llama 4 Scout — 12 layers probed, EN AUROC peaks L36 (0.821), best ZS transfer L28 (0.741). 4 Pareto layers (L20-L32). ρ=0.82.

**Table 4**: Cross-architecture agreement — best transfer depth 60% vs 58% (within 2pp), Pareto zone 43-64% vs 42-67%, both convex monotonic.

**Table 5**: Decomposition — difficulty-shared 68.4% var, 0.738 transfer AUROC, 1.1pp drop (13% of total). Capability-specific 31.6% var, 0.614 transfer, 14.2pp drop (87% of total).

**Table 6**: Capability transfer drop by depth — 0.8pp (0-30%), 3.4pp (30-60%), 9.7pp (60-90%). Ratio grows from 2.7× to 6.1×.

**Table 7**: CaCLR vs baselines (averaged both architectures): CaCLR 0.804 AUROC, 0.061 ECE, no target labels, ~1% overhead. Best baseline: few-shot-100 at 0.762/0.079.

**Table 8**: CaCLR ablation — L_BCE only: 0.752, +L_SB-ECE: 0.768, +L_consistency: 0.793, full: 0.804. Both components contribute; synergistic.

**Table 9**: CaCLR Pareto shift on Qwen3 — shifted frontier extends from L48 to L68 (vs L40-L60 for ZS). At L64: ZS 0.741 → CaCLR 0.814 (+7.3pp).

**Table 10-11**: Orthogonality — mean cosine 0.052, range 0.018-0.094, 39/40 below 0.1 (Yoruba on Llama4 = 0.099). Resource-tier ρ=-0.68.

**Table 12**: Probe complexity — logreg 0.843 EN / 0.762 ZS (8.1pp drop), MLP 0.856 EN / 0.733 ZS (12.4pp drop). Linear probes transfer better.

**Table 13**: Cross-benchmark — CaCLR gain 5.1-5.2pp AUROC, 33-40% ECE reduction across GlobalMMLU, Belebele, MMLU-ProX. CV=0.08.

**Table 14**: Three-architecture — Qwen3 (MoE, 94L, 0.843/0.762, 60%, ρ=0.88), Llama4 Scout (MoE, 48L, 0.821/0.741, 58%, ρ=0.82), Gemma4 31B Dense (Dense, 60L, 0.812/0.734, 60%, ρ=0.86).

**Table 15**: 52-language extension — high (12 langs, ZS 0.782, CaCLR 0.812), mid (25, 0.738, 0.784), low (10, 0.661, 0.712), very-low (4, 0.582, 0.638).

**Table 16**: INT8 vs FP16 — max AUROC diff 0.3pp, rank correlation 0.997.

## Experiment Design Coverage

The paper's review_context.yaml lists 10 planned experiments (plan_001 through plan_010). All 10 are covered in the paper:
- plan_001 (Qwen3 Pareto): Tables 1-2 ✓
- plan_002 (Llama4 Pareto): Tables 3-4 ✓
- plan_003 (CaCLR): Tables 7-9 ✓
- plan_004 (Difficulty decomposition): Tables 5-6 ✓
- plan_005 (Orthogonality): Tables 10-11 ✓
- plan_006 (Probe complexity): Table 12 ✓
- plan_007 (Cross-benchmark): Table 13 ✓
- plan_008 (Gemma 4 31B): Table 14 ✓
- plan_009 (Extended languages): Table 15 ✓
- plan_010 (INT8 validation): Table 16 ✓

## Your Task

Produce a structured review focusing on Methods and Experiments. Your review must include:

1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, specific)
3. **Weaknesses** (bulleted, specific, with severity: minor/moderate/major)
4. **Questions for Authors** (numbered)
5. **Missing Experiments or Analyses** (if any)
6. **Preliminary Score** (1-6 with justification)
7. **Confidence** (1-5)

Be rigorous. Flag any methodological concerns, missing controls, unfair comparisons, or statistical issues. Consider whether the experimental evidence fully supports each of the 4 claims. Note the paper is a "dream" paper (simulated results), so assess the experimental design quality and internal consistency rather than questioning whether experiments were actually run.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "bb5af5ae-0ef2-4d29-8f3f-b58276a3e403",
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

_source line 2 · 2026-05-20T19:38:27.303Z_

```json
{
  "parentUuid": "bb5af5ae-0ef2-4d29-8f3f-b58276a3e403",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
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
  "uuid": "b1859197-5b8f-43c2-ace4-53ae744c3194",
  "timestamp": "2026-05-20T19:38:27.303Z",
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

_source line 3 · 2026-05-20T19:38:30.141Z_



I'll review the paper systematically. Let me first load the project files to understand the full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1859197-5b8f-43c2-ace4-53ae744c3194",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPMa8TxLpXj2fKHvFux",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbd2b6bc-58cc-4dc0-9cdd-9071d51ba743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sszCCiFqbq6YXwmixBnAV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16560,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16560,
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

_source line 4 · 2026-05-20T19:38:31.124Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011LkPhDBuFBKmgiqQgCrpsM`</summary>

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
  "parentUuid": "cbd2b6bc-58cc-4dc0-9cdd-9071d51ba743",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPMa8TxLpXj2fKHvFux",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6aa5010-dadb-400d-816a-e8741fde8ad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sszCCiFqbq6YXwmixBnAV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16560,
      "cache_read_input_tokens": 0,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16560
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 144,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16560,
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

_source line 5 · 2026-05-20T19:38:31.127Z_

<details><summary>↩ Tool result · `toolu_011LkPhDBuFBKmgiqQgCrpsM`</summary>

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
  "parentUuid": "a6aa5010-dadb-400d-816a-e8741fde8ad0",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "63c88192-596b-4c63-86fb-db8bdb4da6e6",
  "sourceToolAssistantUUID": "a6aa5010-dadb-400d-816a-e8741fde8ad0",
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

_source line 6 · 2026-05-20T19:38:33.884Z_



Let me read the paper report and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63c88192-596b-4c63-86fb-db8bdb4da6e6",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPMrhcm6hiCGN4UkLds",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b0d0415-54ff-47f2-b531-ae930b3019a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5NBHvH4sqsJ8dyo1oQrBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 16560,
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

_source line 7 · 2026-05-20T19:38:34.775Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RzERdZe3u5rikJ69q3AoXn`</summary>

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
  "parentUuid": "7b0d0415-54ff-47f2-b531-ae930b3019a1",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPMrhcm6hiCGN4UkLds",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e421e8ce-19ba-4f0f-a904-0430705cdc48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5NBHvH4sqsJ8dyo1oQrBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 16560,
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

_source line 8 · 2026-05-20T19:38:34.790Z_

<details><summary>↩ Tool result · `toolu_01RzERdZe3u5rikJ69q3AoXn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp_003 | Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_002** (failed): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\\n\\n## 趋势\\n成功 1 / 负向 0 / 失败 1 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-13176: 无 GPU 信息\\n\\n## 告警\\n- mvp_002: 训练失败 — unknown\\n\", \"total_chars\": 1092, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e421e8ce-19ba-4f0f-a904-0430705cdc48",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "f09bcaa3-4a34-467f-8ed8-d437776829bd",
  "sourceToolAssistantUUID": "e421e8ce-19ba-4f0f-a904-0430705cdc48",
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

_source line 9 · 2026-05-20T19:38:35.749Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JerDxDvynWLSUDi4jysF15`</summary>

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
  "parentUuid": "f09bcaa3-4a34-467f-8ed8-d437776829bd",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPMrhcm6hiCGN4UkLds",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7d07afe-01ae-410c-a089-336b4a178e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5NBHvH4sqsJ8dyo1oQrBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 16560,
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

_source line 10 · 2026-05-20T19:38:35.760Z_

<details><summary>↩ Tool result · `toolu_01JerDxDvynWLSUDi4jysF15`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-20 19:00 UTC | 更新原因: Reviewer 修正 mean-shift 叙事 + 标注覆盖度风险 + temp scaling 待确认\\n\\n## 核心方向\\n通过中间层 correctness direction 将英语校准迁移到非英语语言。发现 depth-transferability Pareto frontier，提出 CaCLR 方法联合优化 correctness + 跨语言一致性。详见 paper_framing.md。\\n\\n## 当前进展\\n- 阶段：**Research**（MVP 已通过，D004）\\n- 服务器：westd-13176（4× RTX 6000 PRO 96GB）\\n- MVP 结论：核心假设获强支持（EN AUROC=0.754, 4/5 语言迁移成功, layer-depth 14.3pp, Pareto tradeoff 直接观测）\\n- Mean-shift 不可靠/不一致（部分语言微改善、部分恶化，无系统性）→ motivate CaCLR\\n- paper_framing.md ✅ | experiment_plan.yaml ✅ | Dream 模拟进行中（dream_20260520T185641）\\n- ⚠️ P1 ECE pass 依赖 post-hoc temp scaling (T=6.21)，需确认是否在 held-out set 上调\\n\\n## 实验计划（详见 experiment_plan.yaml）\\n- **P0**：plan_001(Qwen3-235B) + plan_002(Llama4 Scout) + plan_003(CaCLR) + plan_004(difficulty ablation)\\n- **P1**：plan_005(orthogonality) + plan_006(probe complexity) + plan_007(Belebele/MMLU-ProX) + plan_010(INT8 ablation)\\n- **P2**：plan_008(Gemma4) + plan_009(50+ languages)\\n- **MVP**：mvp_001 ✅ | mvp_002 bug 修复中 | mvp_003 RUNNING (Llama-3.1-8B, cuda:2)\\n- **覆盖风险**：Claims 2/3/4 各仅 1 个实验，需 Dream 反馈后评估是否加备份\\n\\n## 近期任务\\n- [ ] 等待 Dream 回调，按结果调整 framing/plan\\n- [ ] Agent 修复 --layers 默认值 bug（M004）+ mvp_002 重跑\\n- [ ] Agent 确认 temp scaling 是否在 held-out set 上调\\n- [ ] 确认 IRT difficulty scores 数据可获取性（plan_004 硬依赖）\\n- [ ] mvp_003 结果（cross-architecture 验证）\\n- [ ] Dream 通过后批准 P0 实验\\n\\n## GPU 预算\\n**已分配**：westd-13176 4× RTX 6000 PRO 96GB\\n**当前使用**：cuda:0 空闲 | cuda:1 空闲(mvp_002完成) | cuda:2 mvp_003 | cuda:3 空闲\\n**Critical path**：plan_001(Qwen3-235B INT8 ~235GB) 需 3-4 卡，是全计划瓶颈\\n**Fallback**：CaCLR 效果不显著 → paper 退化为 systematic characterization，仍可投但 significance 降级\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\n| D002 | 2026-05-20 | MVP 模型固定为 Qwen2.5-7B-Instruct | — |\\n| D001 | 2026-05-20 | MVP 用 7-8B 模型验证核心假设，不直接上 235B | — |\\n\\n\\n\\n\", \"total_chars\": 1996, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7d07afe-01ae-410c-a089-336b4a178e63",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "95e6ae5e-eb42-4c3a-aaa5-bf64644e87d7",
  "sourceToolAssistantUUID": "f7d07afe-01ae-410c-a089-336b4a178e63",
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

_source line 11 · 2026-05-20T19:38:35.949Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013vM29SuA1vKLPdpKgYFyhp`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95e6ae5e-eb42-4c3a-aaa5-bf64644e87d7",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPMrhcm6hiCGN4UkLds",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22d8fe6a-314e-4e6d-828d-eda0cf3cedb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5NBHvH4sqsJ8dyo1oQrBY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2063,
      "cache_read_input_tokens": 16560,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2063
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 16560,
          "cache_creation_input_tokens": 2063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2063,
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

_source line 12 · 2026-05-20T19:38:35.961Z_

<details><summary>↩ Tool result · `toolu_013vM29SuA1vKLPdpKgYFyhp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml\", \"content\": \"_next_id: 5\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 13:49 UTC\\n  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B\\n  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &\\n    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B\\n    的大资源。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 13:53 UTC\\n  summary: MVP 模型固定为 Qwen2.5-7B-Instruct\\n  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为\\n    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-20 18:25 UTC\\n  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言\\n  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用\\n    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: trigger\\n    result: P4 ΔAUROC=0 暴露标准设计缺陷\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-20 18:52 UTC\\n  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'\\n  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth\\n    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift\\n    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift\\n    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: primary\\n    result: P1✅P2✅P3✅P4❌, core hypothesis supported\\n  depends_on: []\\n\", \"total_chars\": 1523, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22d8fe6a-314e-4e6d-828d-eda0cf3cedb4",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "267f7f8d-a2e0-4039-9197-18be4eda421a",
  "sourceToolAssistantUUID": "22d8fe6a-314e-4e6d-828d-eda0cf3cedb4",
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

_source line 13 · 2026-05-20T19:38:38.798Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019haxYmmoG64QtgvprFGF2b`</summary>

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
  "parentUuid": "267f7f8d-a2e0-4039-9197-18be4eda421a",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPNDP5AmNpW9pwwWgS9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eefae54e-2581-4357-a556-553003d3c297",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VDGBaPYdzKx1mYDySJpSLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3551,
      "cache_read_input_tokens": 18623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3551,
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

_source line 14 · 2026-05-20T19:38:38.813Z_

<details><summary>↩ Tool result · `toolu_019haxYmmoG64QtgvprFGF2b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 2 models × 20 languages × all contributions\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.\\n- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.\\n- **Headline template**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak\\\"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 6025, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eefae54e-2581-4357-a556-553003d3c297",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "262dfd72-03e9-4e35-bf49-14a6789ace41",
  "sourceToolAssistantUUID": "eefae54e-2581-4357-a556-553003d3c297",
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

_source line 15 · 2026-05-20T19:38:39.757Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NQk2MV9US5fN16RFnLFAPd`</summary>

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
  "parentUuid": "262dfd72-03e9-4e35-bf49-14a6789ace41",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPNDP5AmNpW9pwwWgS9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56b2f12a-64d0-4690-b660-cdb65c55384c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VDGBaPYdzKx1mYDySJpSLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3551,
      "cache_read_input_tokens": 18623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3551,
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

_source line 16 · 2026-05-20T19:38:39.765Z_

<details><summary>↩ Tool result · `toolu_01NQk2MV9US5fN16RFnLFAPd`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56b2f12a-64d0-4690-b660-cdb65c55384c",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "8d6a43bd-4c8b-4e47-83b9-1b28d4b5a2e1",
  "sourceToolAssistantUUID": "56b2f12a-64d0-4690-b660-cdb65c55384c",
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

_source line 17 · 2026-05-20T19:38:40.219Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U3iuVf9FEpcyw3o4Bad59z`</summary>

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
  "parentUuid": "8d6a43bd-4c8b-4e47-83b9-1b28d4b5a2e1",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPNDP5AmNpW9pwwWgS9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed6683e9-c518-4216-9315-c0ada76c0902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VDGBaPYdzKx1mYDySJpSLJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3551,
      "cache_read_input_tokens": 18623,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3551
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 18623,
          "cache_creation_input_tokens": 3551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3551,
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

_source line 18 · 2026-05-20T19:38:40.228Z_

<details><summary>↩ Tool result · `toolu_01U3iuVf9FEpcyw3o4Bad59z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/memory.md\", \"content\": \"# Memory — xling_calib_direction\\n\\n## 环境配置\\n- **服务器**: westd-13176, 4× RTX 6000 PRO 96GB\\n- **环境**: conda base (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)\\n- **模型路径**: `/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct`（symlink `/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct`）\\n- **代码路径**: `/root/xling_calib_direction/`\\n- **Qwen2.5-7B-Instruct**: 28 layers (index 0-27), hidden_dim=3584\\n- **网络**: 不要用 `source /etc/network_turbo`（会破坏 HF SSL），用 `HF_ENDPOINT=https://hf-mirror.com`\\n- **模型下载**: 用 ModelScope（AutoDL 上 HF 代理太慢）\\n\\n## 数据集字段差异\\n- cais/mmlu: `choices` (list), `answer` (int 0-3)\\n- CohereForAI/Global-MMLU: `option_a/b/c/d` (str), `answer` (letter \\\"A\\\"-\\\"D\\\")\\n- `normalize_row()` 已处理两种格式\\n\\n## 激活提取速度\\n- Qwen2.5-7B-Instruct, BF16, RTX 6000 PRO 96GB: ~1 sample/s (MMLU 5-shot)\\n- 14K samples × 7 layers × 6 语言 ≈ 2h per GPU\\n\\n## MVP 实验关键发现 (2026-05-20)\\n\\n### Mean-shift alignment 完全无效（方法论发现）\\nMean-shift 对所有样本加同一常数向量 `(mean_en - mean_tgt)`。\\n- **不能改变 AUROC**: 经线性 probe 后等价于 logit 加常数，AUROC（rank-based）不变。\\n- **不能改善 calibration**: ΔECE 测试结果 0/5 语言达标。zh/ar 仅 marginal（<0.4pp），hi/sw 反而大幅恶化（+2.2pp/+6.4pp）。\\n- **结论**: 简单常数平移不足以 align 跨语言 representation。需要非常数方法（CDA/CORAL/Procrustes）。这是论文贡献空间。\\n\\n### Temperature scaling 有效修复 ECE\\n- Layer 24: T=5.36, ECE 0.1982→0.0888\\n- Layer 27: T=6.21, ECE 0.1951→0.0744\\n- T>1 说明 LogisticRegression 过于自信（overconfident），需要 softening\\n\\n### Layer 27 vs Layer 24: 最后一层更 language-specific\\n- EN AUROC: L27=0.7541 > L24=0.7486（最后一层英语 probe 最强）\\n- 但跨语言迁移: L24 全面优于 L27（zh 0.686 vs 0.661, ar 0.651 vs 0.635, hi 0.652 vs 0.626, ko 0.648 vs 0.607）\\n- **解读**: 最后一层 representation 更 language-specific，对 zero-shot transfer 不利。Optimal transfer layer ≠ optimal source-language layer。这是论文可讨论的有趣发现。\\n\\n### Swahili 始终最差\\n- Best zero-shot AUROC: sw=0.560 (L27) / 0.544 (L20)，均 < 0.58 阈值\\n- 与 low-resource 假设一致，论文中作为 expected limitation\\n\\n### 最终 Gate Check (2026-05-20)\\n- P1 ✅ PASS (AUROC=0.7541, ECE=0.0744 with temp scaling)\\n- P2 ✅ PASS (4/5 langs)\\n- P3 ✅ PASS (14.28pp)\\n- P4 ❌ FAIL (mean-shift 无效，0/5)\\n- 无 hard fail\\n- Overall: PARTIAL 3/4, 核心假设获强支持\\n\", \"total_chars\": 2071, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed6683e9-c518-4216-9315-c0ada76c0902",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "ebc38fd5-6bec-4d26-b668-66d48381b361",
  "sourceToolAssistantUUID": "ed6683e9-c518-4216-9315-c0ada76c0902",
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

_source line 19 · 2026-05-20T19:38:42.832Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Wo25oz9rcksLTg3fH1EWdN`</summary>

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
  "parentUuid": "ebc38fd5-6bec-4d26-b668-66d48381b361",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPNXZxhWhakcWknfZhk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c21f0a5-ee3f-4344-a743-f593ec538802",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJt1suyx4jq6xNBvmoWiDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 22174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 20 · 2026-05-20T19:38:42.841Z_

<details><summary>↩ Tool result · `toolu_01Wo25oz9rcksLTg3fH1EWdN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c21f0a5-ee3f-4344-a743-f593ec538802",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "ff675679-9c13-42ad-91cd-303cd26cc0dc",
  "sourceToolAssistantUUID": "0c21f0a5-ee3f-4344-a743-f593ec538802",
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

_source line 21 · 2026-05-20T19:38:43.756Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FJGGspbbMhMafoxCF2rHHo`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff675679-9c13-42ad-91cd-303cd26cc0dc",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPNXZxhWhakcWknfZhk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61aab8b1-4946-48ef-b362-0c3da0d989cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJt1suyx4jq6xNBvmoWiDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 22174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3528,
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

_source line 22 · 2026-05-20T19:38:43.764Z_

<details><summary>↩ Tool result · `toolu_01FJGGspbbMhMafoxCF2rHHo`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61aab8b1-4946-48ef-b362-0c3da0d989cb",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "6af66bb8-210e-4fae-a8e0-7e6392b8cfc6",
  "sourceToolAssistantUUID": "61aab8b1-4946-48ef-b362-0c3da0d989cb",
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

_source line 23 · 2026-05-20T19:38:44.333Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018ouiZ7jNcb5XwoYnZzUJaM`</summary>

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
  "parentUuid": "6af66bb8-210e-4fae-a8e0-7e6392b8cfc6",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPNXZxhWhakcWknfZhk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e1681f3-d515-4ea2-bb10-dbba00a011aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJt1suyx4jq6xNBvmoWiDo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3528,
      "cache_read_input_tokens": 22174,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3528
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 22174,
          "cache_creation_input_tokens": 3528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3528,
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

_source line 24 · 2026-05-20T19:38:44.343Z_

<details><summary>↩ Tool result · `toolu_018ouiZ7jNcb5XwoYnZzUJaM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\", \"content\": \"papers:\\n  miao2026closing:\\n    title: \\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\"\\n    authors: [\\\"Ruoxi Miao\\\", \\\"Lyle Ungar\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.25052\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  xiao2025knowledge:\\n    title: \\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\"\\n    authors: [\\\"Zheng Xiao\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2504.13816\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  civelli2026shared:\\n    title: \\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\"\\n    authors: [\\\"Andrea Civelli\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2601.12731\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  zhou2025lace:\\n    title: \\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\"\\n    authors: [\\\"Zhou\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03136\\\"\\n    category: \\\"multilingual_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ravisankar2026dali:\\n    title: \\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\"\\n    authors: [\\\"Ravisankar\\\"]\\n    year: 2026\\n    venue: \\\"EACL 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2504.09378\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  miao2026coral:\\n    title: \\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\"\\n    authors: [\\\"Ruoxi Miao\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.06022\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  joshi2025calibration:\\n    title: \\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\"\\n    authors: [\\\"Joshi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  confidence_manifold2026:\\n    title: \\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08159\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  karandikar2021sbece:\\n    title: \\\"Soft Calibration Objectives for Neural Networks\\\"\\n    authors: [\\\"Karandikar\\\"]\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"\\\"\\n    category: \\\"calibration_methods\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  khanmohammadi2025ccps:\\n    title: \\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\"\\n    authors: [\\\"Khanmohammadi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.21772\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  liu2025middle:\\n    title: \\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\"\\n    authors: [\\\"Liu\\\", \\\"Niehues\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ji2025calibrating:\\n    title: \\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\"\\n    authors: [\\\"Ji\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Verbal uncertainty governed by single linear direction in representation space.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\ncategories:\\n  mechanistic_calibration: \\\"Probing/steering calibration signals in LLM internal representations\\\"\\n  cross_lingual_probing: \\\"Cross-lingual transfer of probes/directions in multilingual models\\\"\\n  cross_lingual_alignment: \\\"Language alignment and shared representations in multilingual LLMs\\\"\\n  multilingual_calibration: \\\"Calibration methods for multilingual LLMs\\\"\\n  calibration_methods: \\\"General calibration objectives and techniques\\\"\\n\\nmeta:\\n  created_at: \\\"2026-05-20\\\"\\n  last_updated: \\\"2026-05-20\\\"\\n  total_papers: 12\\n\", \"total_chars\": 6989, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e1681f3-d515-4ea2-bb10-dbba00a011aa",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "d6f6ede7-94b9-42a6-8883-34c349876e6f",
  "sourceToolAssistantUUID": "5e1681f3-d515-4ea2-bb10-dbba00a011aa",
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

_source line 25 · 2026-05-20T19:38:46.905Z_

Now let me look at the experiment plan and any review context files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6f6ede7-94b9-42a6-8883-34c349876e6f",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPNqF5xjMu6YRhu2F2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00c482c6-8c70-4096-9b14-f92270213dae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rQ3x9jgQByj4m2qpxB12n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3352,
      "cache_read_input_tokens": 25702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3352,
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

_source line 26 · 2026-05-20T19:38:47.339Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011R4MrAcFfYg7zwKtcFruTM`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00c482c6-8c70-4096-9b14-f92270213dae",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPNqF5xjMu6YRhu2F2t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d089aef7-4592-4cb8-881e-8a5d30f6069c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rQ3x9jgQByj4m2qpxB12n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3352,
      "cache_read_input_tokens": 25702,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3352
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 25702,
          "cache_creation_input_tokens": 3352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3352,
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

_source line 27 · 2026-05-20T19:38:47.359Z_

<details><summary>↩ Tool result · `toolu_011R4MrAcFfYg7zwKtcFruTM`</summary>

```text
literature_map.yaml
distill_tmp/karandikar2021sbece.yaml
distill_tmp/miao2026closing.yaml
distill_tmp/civelli2026shared.yaml
distill_tmp/confidence_manifold2026.yaml
distill_tmp/xiao2025knowledge.yaml
distill_tmp/joshi2025calibration.yaml
distill_tmp/khanmohammadi2025ccps.yaml
distill_tmp/liu2025middle.yaml
distill_tmp/ji2025calibrating.yaml
distill_tmp/ravisankar2026dali.yaml
distill_tmp/zhou2025lace.yaml
distill_tmp/miao2026coral.yaml
decisions.yaml
experiment_plan.yaml
mistakes.yaml
artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml
registry.yaml
artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d089aef7-4592-4cb8-881e-8a5d30f6069c",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "5ed67616-7fa9-47dc-97f9-6e2c83da616e",
  "sourceToolAssistantUUID": "d089aef7-4592-4cb8-881e-8a5d30f6069c",
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

_source line 28 · 2026-05-20T19:38:50.073Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EhgkxAM4NRp4MBJjKB2vyP`</summary>

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
  "parentUuid": "5ed67616-7fa9-47dc-97f9-6e2c83da616e",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPP46FVUqopjudztLqw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5271f67c-7939-4891-b900-1212e0540a19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126Y1bHpuMaLh36s4jUXagG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 29054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 418,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
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

_source line 29 · 2026-05-20T19:38:50.078Z_

<details><summary>↩ Tool result · `toolu_01EhgkxAM4NRp4MBJjKB2vyP`</summary>

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
  "parentUuid": "5271f67c-7939-4891-b900-1212e0540a19",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "2a657c47-6e9b-4d82-8d5b-b5e181c9d7ee",
  "sourceToolAssistantUUID": "5271f67c-7939-4891-b900-1212e0540a19",
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

_source line 30 · 2026-05-20T19:38:50.406Z_

<details open><summary>🔧 Tool call — Read · `toolu_012oQx9QnHk964EAEXfbN5Zv`</summary>

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
  "parentUuid": "2a657c47-6e9b-4d82-8d5b-b5e181c9d7ee",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPP46FVUqopjudztLqw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eab69240-d79c-4828-be93-a1c66dffcc97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126Y1bHpuMaLh36s4jUXagG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 29054,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 418
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 29054,
          "cache_creation_input_tokens": 418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 418,
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

_source line 31 · 2026-05-20T19:38:51.094Z_

<details><summary>↩ Tool result · `toolu_012oQx9QnHk964EAEXfbN5Zv`</summary>

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
  "parentUuid": "eab69240-d79c-4828-be93-a1c66dffcc97",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "7b2d5625-60d3-4f2f-9afd-30118c84041e",
  "sourceToolAssistantUUID": "eab69240-d79c-4828-be93-a1c66dffcc97",
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

_source line 32 · 2026-05-20T19:38:54.089Z_

Now let me check for the dream registry and any other review-relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b2d5625-60d3-4f2f-9afd-30118c84041e",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPPL2CgwBQzZRAQ3qJ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc87bce6-f402-4c45-adc7-eff36fe1aed2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQrU2uHFbtuBM8p2jzZqRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19224,
      "cache_read_input_tokens": 29472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19224,
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

_source line 33 · 2026-05-20T19:38:55.971Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WKY5nFwXggbgiirie7vnjn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/dream_registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc87bce6-f402-4c45-adc7-eff36fe1aed2",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPPL2CgwBQzZRAQ3qJ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51978dc5-9860-4c90-b614-adfb6854b9a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQrU2uHFbtuBM8p2jzZqRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19224,
      "cache_read_input_tokens": 29472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19224,
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

_source line 34 · 2026-05-20T19:38:55.976Z_

<details><summary>↩ Tool result · `toolu_01WKY5nFwXggbgiirie7vnjn`</summary>

```text
1	dreams:
2	  dream_20260520T185641:
3	    dream_id: dream_20260520T185641
4	    project: xling_calib_direction
5	    status: reviewing
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
  "parentUuid": "51978dc5-9860-4c90-b614-adfb6854b9a7",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "1f7295ad-4a4e-45da-a68b-3890fa8b5c98",
  "sourceToolAssistantUUID": "51978dc5-9860-4c90-b614-adfb6854b9a7",
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

_source line 35 · 2026-05-20T19:38:56.416Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YUggwmh9RTxqFDTZQ7AVoG`</summary>

```json
{
  "pattern": "**/dream_reports/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f7295ad-4a4e-45da-a68b-3890fa8b5c98",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPPL2CgwBQzZRAQ3qJ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9d0ce74-5d99-4541-be93-38ed99b70cd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQrU2uHFbtuBM8p2jzZqRw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19224,
      "cache_read_input_tokens": 29472,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 29472,
          "cache_creation_input_tokens": 19224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19224,
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

_source line 36 · 2026-05-20T19:38:56.425Z_

<details><summary>↩ Tool result · `toolu_01YUggwmh9RTxqFDTZQ7AVoG`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9d0ce74-5d99-4541-be93-38ed99b70cd6",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "aea87127-0354-4b56-9069-ef123ff8b9d2",
  "sourceToolAssistantUUID": "a9d0ce74-5d99-4541-be93-38ed99b70cd6",
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

_source line 37 · 2026-05-20T19:38:59.486Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EYbaJueXN8VbTGZDpkQMSb`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260520T185641/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aea87127-0354-4b56-9069-ef123ff8b9d2",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPPihTiAL2C454EkNkx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d339980a-4761-4d47-be4f-42c3b8cb0063",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJgrMp98RUGde9XneNCyrJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 761,
      "cache_read_input_tokens": 48696,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 761
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 48696,
          "cache_creation_input_tokens": 761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 761,
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

_source line 38 · 2026-05-20T19:38:59.499Z_

<details><summary>↩ Tool result · `toolu_01EYbaJueXN8VbTGZDpkQMSb`</summary>

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
  "parentUuid": "d339980a-4761-4d47-be4f-42c3b8cb0063",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "4457a583-1918-4b37-ace3-16250a914e19",
  "sourceToolAssistantUUID": "d339980a-4761-4d47-be4f-42c3b8cb0063",
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

_source line 39 · 2026-05-20T19:39:03.101Z_

Let me read the best-tier paper to review the actual methods and experiments sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4457a583-1918-4b37-ace3-16250a914e19",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPPwzfgmhCSVahecpZ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "508b8f60-b5a1-4b47-9ab3-5d518589792e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVSEqJU29VLzqDR69cckpT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 49457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 966,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 40 · 2026-05-20T19:39:03.965Z_

<details open><summary>🔧 Tool call — Read · `toolu_016L7gkJvRTU95LFipqEVYYW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "508b8f60-b5a1-4b47-9ab3-5d518589792e",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPPwzfgmhCSVahecpZ1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0219af67-c473-41b2-b79a-2029a04661e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVSEqJU29VLzqDR69cckpT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 49457,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 966
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 49457,
          "cache_creation_input_tokens": 966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 966,
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

_source line 41 · 2026-05-20T19:39:04.353Z_

<details><summary>↩ Tool result · `toolu_016L7gkJvRTU95LFipqEVYYW`</summary>

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
11	\usepackage{url}
12	\usepackage{hyperref}
13	\usepackage{microtype}
14	\usepackage{array}
15	\usepackage{natbib}
16	
17	\newcommand{\caclr}{\textsc{CaCLR}}
18	\newcommand{\ece}{\text{ECE}}
19	\newcommand{\auroc}{\text{AUROC}}
20	
21	\title{Shifting the Cross-Lingual Calibration Pareto Frontier:\\Probe-Based Calibration Transfer via CaCLR}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\begin{abstract}
29	Non-English languages suffer substantially worse calibration in multilingual LLMs, yet existing probe-based calibration methods operate exclusively in English.
30	We present the first systematic study of cross-lingual correctness probe transfer for calibration across 20 languages and three architectures (Qwen3-235B-A22B, Llama~4~Scout, Gemma~4~31B Dense).
31	We discover a \emph{depth-transferability Pareto frontier}: deeper layers yield better English calibration but degrade cross-lingual zero-shot transfer, with the optimal transfer depth converging to $\sim$58--60\% of model depth across architectures.
32	We decompose correctness probe signal into a \emph{difficulty-shared} component (68\% of variance, language-agnostic, transfers at all depths) and a \emph{capability-specific} component (32\%, language-dependent, drives 87\% of transfer degradation).
33	We propose \caclr{} (\textbf{Ca}libration-aware \textbf{C}ross-\textbf{L}ingual \textbf{R}egularization), a training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without target-language labels.
34	\caclr{} shifts the Pareto frontier outward: averaged across architectures, it improves non-English AUROC by 5.2pp over zero-shot transfer and reduces ECE by $\sim$40\% relative to temperature scaling, with zero target-language correctness labels.
35	We further show that correctness--confidence orthogonality (cosine $<0.1$) persists across all 20 languages in both architectures, establishing output-based calibration as structurally limited regardless of language.
36	Results generalize to 52 languages and two additional benchmarks (Belebele, MMLU-ProX).
37	\end{abstract}
38	
39	%------------------------------------------------------------------
40	\section{Introduction}
41	\label{sec:intro}
42	%------------------------------------------------------------------
43	
44	Calibration---the alignment between a model's expressed confidence and its actual accuracy---is critical for safe deployment of large language models (LLMs). While recent work has made substantial progress on English calibration through internal representation probing \cite{burns2023discovering,marks2024geometry,miao2026coral}, non-English languages remain poorly served: they suffer up to 5$\times$ worse expected calibration error (ECE) under standard output-based methods.
45	
46	This gap is not merely quantitative. Miao \& Ungar (2026) demonstrated that the correctness direction in LLM activation space is \emph{orthogonal} to the verbalized confidence direction, implying that output-based calibration methods are structurally limited. However, their analysis---and indeed all probe-based calibration work---is restricted to English. Whether this entire research line extends to multilingual settings is an open question with field-level implications.
47	
48	We address this question systematically. Our investigation reveals four findings that form an unbroken causal chain:
49	
50	\paragraph{Claim 1: Pareto Frontier (Discovery).}
51	Cross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth converges to $\sim$58--60\% of model depth across three architectures (Qwen3-235B-A22B, Llama~4~Scout, Gemma~4~31B Dense), with Spearman rank correlations between depth and transfer degradation of $\rho=0.82$--$0.88$ ($p<0.001$).
52	
53	\paragraph{Claim 2: Decomposition (Analysis).}
54	Cross-lingual transfer decomposes into a \emph{difficulty-shared} component (68\% of correctness variance; language-agnostic; transfers at all depths) and a \emph{capability-specific} component (32\%; language-dependent; accounts for 87\% of transfer degradation). This decomposition is prescriptive: it predicts with 81\% accuracy when alignment intervention is needed.
55	
56	\paragraph{Claim 3: CaCLR (Method).}
57	We propose \caclr{}, a probe training objective ($\mathcal{L}_\text{BCE} + \alpha \cdot \mathcal{L}_\text{SB-ECE} + \beta \cdot \mathcal{L}_\text{consistency}$) that shifts the Pareto frontier outward by jointly optimizing calibration and cross-lingual invariance. Averaged across both architectures, \caclr{} improves non-English AUROC by 5.2pp over zero-shot transfer and reduces ECE by $\sim$40\% relative to temperature scaling, requiring zero target-language correctness labels.
58	
59	\paragraph{Claim 4: Cross-Lingual Orthogonality (Mechanistic).}
60	The correctness--confidence orthogonality persists across all 20 languages (mean cosine similarity = 0.052, all $<$ 0.1), with a resource-tier gradient ($\rho=-0.68$): better-resourced languages show stronger orthogonality. This establishes output-based calibration as fundamentally limited regardless of language.
61	
62	Together, these claims position \caclr{} as the first method to provide effective probe-based cross-lingual calibration without target-language labels, shifting the Pareto frontier that constrains all prior approaches.
63	
64	%------------------------------------------------------------------
65	\section{Related Work}
66	\label{sec:related}
67	%------------------------------------------------------------------
68	
69	\paragraph{Probe-Based Calibration.}
70	Burns et al.\ (2023) and Marks et al.\ (2024) showed that linear probes on intermediate activations can recover correctness signals. Miao et al.\ (2026a; CORAL) demonstrated cross-task transfer of such probes. Miao \& Ungar (2026b) established the orthogonality of correctness and verbalized confidence directions. All of this work is English-only.
71	
72	\paragraph{Cross-Lingual Representation Transfer.}
73	Xiao et al.\ (ACL 2025) transferred \emph{knowledge-boundary} probes (input-level answerability, not output-dependent correctness) across 8 languages, measuring probing accuracy rather than calibration. Civelli et al.\ transferred difficulty probes cross-lingually, finding language-agnostic difficulty encoding---a result we leverage as a control in our decomposition (Claim~2).
74	
75	\paragraph{Multilingual Calibration.}
76	LACE (Zhou et al.) uses per-language layer ensembles but requires target-language labels. MKA employs multi-key attention at 5$\times$ inference cost. Temperature scaling is the standard output-based baseline. None addresses representation-level cross-lingual calibration transfer.
77	
78	%------------------------------------------------------------------
79	\section{Method}
80	\label{sec:method}
81	%------------------------------------------------------------------
82	
83	\subsection{Correctness Probing and Transfer}
84	\label{sec:probing}
85	
86	Given a multilingual LLM with $L$ layers, we extract activations $\mathbf{h}_l^{(i)}$ at layer $l$ for input $i$. A logistic regression probe $f_l(\mathbf{h}) = \sigma(\mathbf{w}_l^\top \mathbf{h} + b_l)$ is trained on English correctness labels (binary: correct/incorrect on GlobalMMLU). We evaluate five cross-lingual transfer conditions:
87	
88	\begin{enumerate}
89	\item \textbf{Zero-shot}: Apply the English-trained probe directly to non-English activations.
90	\item \textbf{Mean-shift}: Subtract the English activation mean and add the target-language mean before applying the probe.
91	\item \textbf{Linear projection}: Learn a linear map $\mathbf{A}$ between English and target-language activation distributions from parallel data.
92	\item \textbf{Few-shot} (25/100): Fine-tune the probe with 25 or 100 target-language labeled examples.
93	\item \textbf{CaCLR}: Our proposed method (Section~\ref{sec:caclr}).
94	\end{enumerate}
95	
96	\subsection{Pareto Frontier Analysis}
97	\label{sec:pareto}
98	
99	For each probed layer $l$, we measure English probe AUROC and mean cross-lingual transfer AUROC across 19 non-English languages. Plotting these defines a \emph{depth-transferability Pareto frontier}: the set of layers where no other layer simultaneously achieves higher English and higher transfer performance. We characterize this frontier across multiple architectures to assess universality.
100	
101	\subsection{Difficulty--Capability Decomposition}
102	\label{sec:decomp}
103	
104	To explain \emph{why} transfer degrades at deeper layers, we decompose the correctness signal. Using IRT (Item Response Theory) difficulty parameters as supervision, we train Ridge regression probes to extract a \emph{difficulty direction} from activations. We project out this direction and retrain correctness probes on the residual activations. The residual captures \emph{capability-specific} signal---language-dependent competence differences that drive transfer degradation.
105	
106	\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}
107	\label{sec:caclr}
108	
109	\caclr{} optimizes a multi-objective loss:
110	\begin{equation}
111	\mathcal{L}_\text{CaCLR} = \mathcal{L}_\text{BCE} + \alpha \cdot \mathcal{L}_\text{SB-ECE} + \beta \cdot \mathcal{L}_\text{consistency}
112	\label{eq:caclr}
113	\end{equation}
114	
115	\noindent where:
116	\begin{itemize}
117	\item $\mathcal{L}_\text{BCE}$ is binary cross-entropy on English correctness labels.
118	\item $\mathcal{L}_\text{SB-ECE}$ is a soft-binned ECE loss that directly penalizes calibration error during training (as opposed to post-hoc temperature scaling).
119	\item $\mathcal{L}_\text{consistency}$ penalizes divergence between probe outputs on English and non-English parallel activations, forcing the probe to learn language-invariant features without requiring target-language correctness labels.
120	\end{itemize}
121	
122	The key insight is that $\mathcal{L}_\text{consistency}$ shapes the probe during training to exploit language-invariant features, which is strictly more powerful than post-hoc alignment (mean-shift or linear projection) that corrects distributional mismatch after the probe has already been fit. Hyperparameters $\alpha$ and $\beta$ are tuned on a validation set; optimal values are $\alpha=0.15$ and $\beta=0.08$.
123	
124	\subsection{Orthogonality Analysis}
125	\label{sec:ortho}
126	
127	Following Miao \& Ungar (2026), we extract the \emph{verbalized confidence direction} by prompting models for explicit confidence scores and regressing activations on these scores. We compute cosine similarity between the correctness direction (from probes) and the confidence direction across all 20 languages to test whether the orthogonality finding generalizes beyond English.
128	
129	%------------------------------------------------------------------
130	\section{Experimental Setup}
131	\label{sec:setup}
132	%------------------------------------------------------------------
133	
134	\paragraph{Models.} We evaluate three architectures: \textbf{Qwen3-235B-A22B} (94 layers, MoE, $\sim$22B active parameters), \textbf{Llama~4~Scout} (48 layers, MoE, $\sim$17B active, INT8 quantization), and \textbf{Gemma~4~31B Dense} (60 layers, dense). Activations are extracted at every 4th layer.
135	
136	\paragraph{Benchmarks.} Primary evaluation uses \textbf{GlobalMMLU} (20 languages covering high-, mid-, and low-resource tiers). Generalization is tested on \textbf{Belebele} (reading comprehension) and \textbf{MMLU-ProX} (harder MCQA).
137	
138	\paragraph{Languages.} Core set: en, zh, de, fr, es, ja, ru, pt, it, ar, hi, ko, vi, th, bn, tr, nl, sw, yo, ig. Extended set: 52 languages covering Austronesian, Dravidian, Niger-Congo~B, Uralic, and Kartvelian families.
139	
140	\paragraph{Probes.} Logistic regression (primary) and 2-layer MLP (comparison). Trained on English correctness labels from GlobalMMLU.
141	
142	\paragraph{Metrics.} AUROC for discrimination, ECE for calibration quality (lower is better). ECE reduction is reported relative to temperature scaling (optimized $T$; $T=4.87$ for Qwen3, $T=5.34$ for Llama~4).
143	
144	%------------------------------------------------------------------
145	\section{Results}
146	\label{sec:results}
147	%------------------------------------------------------------------
148	
149	\subsection{Pareto Frontier Discovery (Claim 1)}
150	\label{sec:res_pareto}
151	
152	\paragraph{Qwen3-235B-A22B.}
153	Table~\ref{tab:pareto_qwen3} presents the full depth profile. English AUROC peaks at layer 72 (0.843) while best cross-lingual transfer occurs at layer 56 (0.762 mean across 19 languages). Six layers (L40--L60) form the Pareto frontier, with a Spearman rank correlation of $\rho=0.88$ between depth and transfer degradation. The 16-layer gap between best-English and best-transfer layers confirms that the depth--transferability tradeoff is substantial at scale.
154	
155	The resource-tier gradient is consistent: high-resource languages achieve 0.791 mean AUROC at the best-transfer layer, mid-resource 0.754, and low-resource 0.683. All low-resource languages (sw, yo, ig) exceed 0.65 AUROC.
156	
157	\begin{table}[t]
158	\centering
159	\small
160	\caption{Qwen3-235B Pareto Frontier: English AUROC vs.\ zero-shot transfer AUROC by layer. Pareto-optimal layers are marked ($\bullet$).}
161	\label{tab:pareto_qwen3}
162	\begin{tabular}{rrrrrr}
163	\toprule
164	Layer & Depth\% & EN & ZS-19 & Drop & Pareto \\
165	\midrule
166	4 & 4 & .621 & .608 & 1.3 & \\
167	8 & 9 & .648 & .637 & 1.1 & \\
168	12 & 13 & .689 & .671 & 1.8 & \\
169	16 & 17 & .712 & .698 & 1.4 & \\
170	20 & 21 & .738 & .724 & 1.4 & \\
171	24 & 26 & .756 & .742 & 1.4 & \\
172	28 & 30 & .771 & .755 & 1.6 & \\
173	32 & 34 & .784 & .764 & 2.0 & \\
174	36 & 38 & .795 & .771 & 2.4 & \\
175	40 & 43 & .803 & .776 & 2.7 & $\bullet$ \\
176	44 & 47 & .810 & .774 & 3.6 & $\bullet$ \\
177	48 & 51 & .816 & .770 & 4.6 & $\bullet$ \\
178	52 & 55 & .822 & .765 & 5.7 & $\bullet$ \\
179	56 & 60 & .827 & .762 & 6.5 & $\bullet$ \\
180	60 & 64 & .831 & .753 & 7.8 & $\bullet$ \\
181	64 & 68 & .835 & .741 & 9.4 & \\
182	68 & 72 & .839 & .728 & 11.1 & \\
183	72 & 77 & .843 & .712 & 13.1 & \\
184	76 & 81 & .841 & .694 & 14.7 & \\
185	80 & 85 & .838 & .671 & 16.7 & \\
186	84 & 89 & .832 & .643 & 18.9 & \\
187	88 & 94 & .819 & .611 & 20.8 & \\
188	92 & 98 & .791 & .574 & 21.7 & \\
189	94 & 100 & .762 & .541 & 22.1 & \\
190	\bottomrule
191	\end{tabular}
192	\end{table}
193	
194	\paragraph{Transfer Conditions at Best-Transfer Layer.}
195	Table~\ref{tab:transfer_conditions} compares all five transfer conditions at layer 56. Mean-shift \emph{degrades} performance ($-3.1$\% ECE reduction vs.\ temperature scaling), confirming that correctness directions require rotation, not translation. Linear projection provides moderate improvement (16.3\% ECE reduction). Few-shot transfer with 100 labeled examples achieves 19.4\% ECE reduction. \caclr{} dominates all conditions: 40.8\% ECE reduction with AUROC of 0.814, requiring no target-language labels.
196	
197	\begin{table}[t]
198	\centering
199	\small
200	\caption{Transfer condition comparison at best-transfer layer (L56, Qwen3-235B). ECE reduction is relative to temperature scaling.}
201	\label{tab:transfer_conditions}
202	\begin{tabular}{lccc}
203	\toprule
204	Condition & AUROC & ECE & ECE Red.\% \\
205	\midrule
206	Zero-shot & .762 & .098 & 0.0 \\
207	Mean-shift & .758 & .101 & $-3.1$ \\
208	Linear proj. & .781 & .082 & 16.3 \\
209	Few-shot (25) & .748 & .089 & 9.2 \\
210	Few-shot (100) & .771 & .079 & 19.4 \\
211	\caclr{} & \textbf{.814} & \textbf{.058} & \textbf{40.8} \\
212	\bottomrule
213	\end{tabular}
214	\end{table}
215	
216	\paragraph{Llama 4 Scout.}
217	Table~\ref{tab:pareto_llama4} shows the Pareto frontier for Llama~4~Scout (48 layers, INT8). English AUROC peaks at layer 36 (0.821); best transfer is at layer 28 (0.741). Four layers (L20--L32) form the frontier, with $\rho=0.82$. The best-transfer depth is 58\%, remarkably close to Qwen3's 60\%.
218	
219	\begin{table}[t]
220	\centering
221	\small
222	\caption{Llama~4~Scout Pareto Frontier. Pareto-optimal layers marked ($\bullet$).}
223	\label{tab:pareto_llama4}
224	\begin{tabular}{rrrrrr}
225	\toprule
226	Layer & Depth\% & EN & ZS-19 & Drop & Pareto \\
227	\midrule
228	4 & 8 & .634 & .624 & 1.0 & \\
229	8 & 17 & .672 & .659 & 1.3 & \\
230	12 & 25 & .714 & .699 & 1.5 & \\
231	16 & 33 & .745 & .729 & 1.6 & \\
232	20 & 42 & .768 & .748 & 2.0 & $\bullet$ \\
233	24 & 50 & .786 & .745 & 4.1 & $\bullet$ \\
234	28 & 58 & .798 & .741 & 5.7 & $\bullet$ \\
235	32 & 67 & .810 & .732 & 7.8 & $\bullet$ \\
236	36 & 75 & .821 & .714 & 10.7 & \\
237	40 & 83 & .818 & .689 & 12.9 & \\
238	44 & 92 & .804 & .651 & 15.3 & \\
239	48 & 100 & .771 & .608 & 16.3 & \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	\paragraph{Cross-Architecture Agreement.}
245	Table~\ref{tab:cross_arch} quantifies cross-architecture agreement. Best-transfer depth, Pareto zone, rank correlation, and frontier shape all agree within tight tolerances across the two MoE architectures. This establishes the depth-transferability tradeoff as an architecture-general property of transformer depth.
246	
247	\begin{table}[t]
248	\centering
249	\small
250	\caption{Cross-architecture Pareto frontier agreement.}
251	\label{tab:cross_arch}
252	\begin{tabular}{lccc}
253	\toprule
254	Metric & Qwen3 & Llama4 & Agreement \\
255	\midrule
256	Best EN depth\% & 77 & 75 & within 2pp \\
257	Best transfer depth\% & 60 & 58 & within 2pp \\
258	Pareto zone\% & 43--64 & 42--67 & overlapping \\
259	Rank corr.\ $\rho$ & 0.88 & 0.82 & both $>$0.75 \\
260	Frontier shape & convex & convex & consistent \\
261	\bottomrule
262	\end{tabular}
263	\end{table}
264	
265	%------------------------------------------------------------------
266	\subsection{Difficulty--Capability Decomposition (Claim 2)}
267	\label{sec:res_decomp}
268	%------------------------------------------------------------------
269	
270	Table~\ref{tab:decomp} presents the decomposition results. IRT difficulty probes achieve $R^2=0.72$, explaining 68.4\% of correctness variance. This \emph{difficulty-shared} component transfers near-perfectly across languages (only 1.1pp drop from English, accounting for 13\% of total transfer degradation). The \emph{capability-specific} residual (31.6\% of variance) drives nearly all transfer degradation: 14.2pp drop, accounting for 87\% of total degradation.
271	
272	\begin{table}[t]
273	\centering
274	\small
275	\caption{Decomposition: difficulty-shared vs.\ capability-specific components.}
276	\label{tab:decomp}
277	\begin{tabular}{lcccc}
278	\toprule
279	Component & Var\% & Transfer & Drop & Share\% \\
280	\midrule
281	Full correctness & 100 & .752 & 8.1 & 100 \\
282	Difficulty (shared) & 68.4 & .738 & 1.1 & 13 \\
283	Capability (specific) & 31.6 & .614 & 14.2 & 87 \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	The depth interaction is the mechanistic key (Table~\ref{tab:decomp_depth}). Capability-specific transfer degradation accelerates with depth: 0.8pp at shallow layers ($<$30\%), 3.4pp at mid-depth (30--60\%), and 9.7pp at deep layers (60--90\%). The ratio of capability to difficulty degradation grows from 2.7$\times$ to 6.1$\times$. This explains the Pareto frontier: deeper layers encode stronger capability-specific signals that improve English calibration but are language-dependent and thus impede transfer.
289	
290	\begin{table}[t]
291	\centering
292	\small
293	\caption{Capability-specific transfer degradation by depth band.}
294	\label{tab:decomp_depth}
295	\begin{tabular}{lccr}
296	\toprule
297	Depth Band & Diff.\ Drop & Cap.\ Drop & Ratio \\
298	\midrule
299	0--30\% & 0.3pp & 0.8pp & 2.7$\times$ \\
300	30--60\% & 0.8pp & 3.4pp & 4.3$\times$ \\
301	60--90\% & 1.6pp & 9.7pp & 6.1$\times$ \\
302	\bottomrule
303	\end{tabular}
304	\end{table}
305	
306	The decomposition achieves 81\% prescriptive accuracy: when difficulty explains most of a language-layer combination's correctness variance, zero-shot transfer suffices; when the capability residual is large, \caclr{} is needed.
307	
308	%------------------------------------------------------------------
309	\subsection{CaCLR Evaluation (Claim 3)}
310	\label{sec:res_caclr}
311	%------------------------------------------------------------------
312	
313	\paragraph{Full Comparison.}
314	Table~\ref{tab:caclr_full} compares \caclr{} against all baselines, averaged across both architectures and 19 non-English languages. \caclr{} achieves the highest AUROC (0.804) and lowest ECE (0.061) while requiring no target-language labels. It outperforms linear projection by 3.4pp AUROC and few-shot (100 labeled examples) by 4.2pp AUROC. The parameter overhead is minimal ($\sim$1\% additional probe parameters).
315	
316	\begin{table}[t]
317	\centering
318	\small
319	\caption{\caclr{} vs.\ baselines (averaged across both architectures).}
320	\label{tab:caclr_full}
321	\begin{tabular}{lcccc}
322	\toprule
323	Method & AUROC & ECE & Labels? & Overhead \\
324	\midrule
325	Zero-shot & .752 & .098 & no & 0 \\
326	Mean-shift & .747 & .102 & no & 0 \\
327	Linear proj. & .770 & .082 & no & $d{\times}d$ \\
328	Few-shot (25) & .738 & .089 & yes (25) & 0 \\
329	Few-shot (100) & .762 & .079 & yes (100) & 0 \\
330	\caclr{} & \textbf{.804} & \textbf{.061} & \textbf{no} & $\sim$1\% \\
331	\bottomrule
332	\end{tabular}
333	\end{table}
334	
335	\paragraph{Ablation.}
336	Table~\ref{tab:ablation} shows the contribution of each \caclr{} loss component. $\mathcal{L}_\text{consistency}$ provides the bulk of AUROC improvement (+4.1pp alone), while $\mathcal{L}_\text{SB\text{-}ECE}$ contributes calibration refinement (ECE drops from 0.078 to 0.061 when added). The full objective achieves synergistic gains: 0.804 AUROC and 0.061 ECE, better than either auxiliary term alone.
337	
338	\begin{table}[t]
339	\centering
340	\small
341	\caption{Ablation of \caclr{} loss components.}
342	\label{tab:ablation}
343	\begin{tabular}{lccc}
344	\toprule
345	Configuration & AUROC & ECE & $\Delta$AUROC \\
346	\midrule
347	$\mathcal{L}_\text{BCE}$ only & .752 & .098 & $-5.2$ \\
348	$+ \mathcal{L}_\text{SB-ECE}$ & .768 & .072 & $-3.6$ \\
349	$+ \mathcal{L}_\text{consistency}$ & .793 & .078 & $-1.1$ \\
350	Full \caclr{} & \textbf{.804} & \textbf{.061} & 0.0 \\
351	\bottomrule
352	\end{tabular}
353	\end{table}
354	
355	\paragraph{Pareto Frontier Shift.}
356	Table~\ref{tab:pareto_shift} demonstrates the headline result: \caclr{} shifts the Pareto frontier outward on Qwen3-235B. At layer 64, zero-shot transfer achieves 0.741 AUROC; \caclr{} achieves 0.814---a 7.3pp improvement. The practical implication: \caclr{} enables operating at deeper, better-calibrated layers without sacrificing cross-lingual transfer. The shifted Pareto frontier extends from L48 to L68, 2 layers deeper than the original frontier (L40--L60).
357	
358	\begin{table}[t]
359	\centering
360	\small
361	\caption{\caclr{} Pareto frontier shift (Qwen3-235B). Shifted Pareto layers marked ($\bullet$).}
362	\label{tab:pareto_shift}
363	\begin{tabular}{rcccc}
364	\toprule
365	Layer & ZS & \caclr{} & $\Delta$pp & Shifted \\
366	\midrule
367	40 & .776 & .798 & 2.2 & \\
368	44 & .774 & .800 & 2.6 & \\
369	48 & .770 & .803 & 3.3 & $\bullet$ \\
370	52 & .765 & .806 & 4.1 & $\bullet$ \\
371	56 & .762 & .810 & 4.8 & $\bullet$ \\
372	60 & .753 & .814 & 6.1 & $\bullet$ \\
373	64 & .741 & .814 & 7.3 & $\bullet$ \\
374	68 & .728 & .808 & 8.0 & $\bullet$ \\
375	72 & .712 & .796 & 8.4 & \\
376	\bottomrule
377	\end{tabular}
378	\end{table}
379	
380	The improvement pass rate across model--language pairs is 92\% (35/38). The 3 non-improving pairs are high-resource languages on Llama~4~Scout where zero-shot transfer is already excellent and the consistency loss has minimal signal to exploit.
381	
382	\paragraph{Low-Resource Performance.}
383	\caclr{} is especially effective for low-resource languages. On Qwen3: Swahili 0.731, Yoruba 0.709, Igbo 0.718 (vs.\ zero-shot: 0.695, 0.672, 0.681). On Llama~4: Swahili 0.712, Yoruba 0.681, Igbo 0.698. All low-resource languages pass the 0.60 AUROC threshold for usable calibration.
384	
385	%------------------------------------------------------------------
386	\subsection{Cross-Lingual Orthogonality (Claim 4)}
387	\label{sec:res_ortho}
388	%------------------------------------------------------------------
389	
390	Table~\ref{tab:ortho} presents the correctness--confidence cosine similarity across all 20 languages and both architectures. The mean cosine is 0.052 (range: 0.018--0.094), well within the near-orthogonal regime ($<0.1$). Across all 40 language--architecture pairs, 39/40 fall below 0.1 (Yoruba on Llama~4 reaches 0.099).
391	
392	\begin{table}[t]
393	\centering
394	\small
395	\caption{Correctness--confidence cosine similarity by language. All values $<0.1$.}
396	\label{tab:ortho}
397	\begin{tabular}{llccc}
398	\toprule
399	Language & Tier & Qwen3 & Llama4 & Mean \\
400	\midrule
401	en & high & .031 & .037 & .034 \\
402	zh & high & .035 & .041 & .038 \\
403	de & high & .033 & .039 & .036 \\
404	fr & high & .036 & .042 & .039 \\
405	es & high & .038 & .044 & .041 \\
406	ja & high & .041 & .047 & .044 \\
407	ru & high & .040 & .046 & .043 \\
408	pt & high & .037 & .043 & .040 \\
409	it & high & .039 & .045 & .042 \\
410	nl & high & .034 & .040 & .037 \\
411	\midrule
412	ar & mid & .047 & .055 & .051 \\
413	hi & mid & .051 & .059 & .055 \\
414	ko & mid & .045 & .053 & .049 \\
415	vi & mid & .054 & .062 & .058 \\
416	th & mid & .057 & .065 & .061 \\
417	bn & mid & .052 & .060 & .056 \\
418	tr & mid & .048 & .056 & .052 \\
419	\midrule
420	sw & low & .073 & .083 & .078 \\
421	yo & low & .089 & .099 & .094 \\
422	ig & low & .077 & .087 & .082 \\
423	\bottomrule
424	\end{tabular}
425	\end{table}
426	
427	The resource-tier gradient is notable: high-resource languages have mean cosine 0.041, mid-resource 0.054, and low-resource 0.074 (Spearman $\rho=-0.68$ between resource tier and cosine). This suggests that output-based calibration methods are not just structurally limited but are \emph{more} limited for well-resourced languages where the orthogonality is strongest. The cross-architecture consistency (Qwen3: 0.048, Llama~4: 0.057) confirms this is not architecture-specific (Table~\ref{tab:ortho_summary}).
428	
429	\begin{table}[t]
430	\centering
431	\small
432	\caption{Orthogonality summary statistics.}
433	\label{tab:ortho_summary}
434	\begin{tabular}{lccc}
435	\toprule
436	Statistic & Qwen3 & Llama4 & Both \\
437	\midrule
438	Mean & 0.048 & 0.057 & 0.052 \\
439	Std & 0.015 & 0.017 & 0.016 \\
440	Max & 0.089 & 0.099 & 0.094 \\
441	Min & 0.031 & 0.037 & 0.018 \\
442	All $<0.1$ & 20/20 & 19/20 & 39/40 \\
443	Tier corr.\ $\rho$ & $-0.71$ & $-0.65$ & $-0.68$ \\
444	\bottomrule
445	\end{tabular}
446	\end{table}
447	
448	%------------------------------------------------------------------
449	\subsection{Probe Complexity Analysis}
450	\label{sec:res_probe}
451	%------------------------------------------------------------------
452	
453	Table~\ref{tab:probe_complexity} compares logistic regression vs.\ 2-layer MLP probes. MLPs gain 1.3pp English AUROC but lose 4.3pp in cross-lingual transfer. The transfer advantage of linear probes grows with depth: 2.1pp at shallow layers vs.\ 6.8pp at deep layers. This confirms that deep-layer transfer degradation is driven by nonlinear, language-specific features that MLPs exploit but linear probes ignore. Linear probes are thus the correct choice for cross-lingual calibration transfer.
454	
455	\begin{table}[t]
456	\centering
457	\small
458	\caption{Probe complexity comparison (Qwen3-235B).}
459	\label{tab:probe_complexity}
460	\begin{tabular}{lcccc}
461	\toprule
462	Probe & EN Best & ZS-19 & Drop & ECE \\
463	\midrule
464	Logistic regression & .843 & .762 & 8.1pp & .054 \\
465	2-layer MLP & .856 & .733 & 12.4pp & .068 \\
466	\bottomrule
467	\end{tabular}
468	\end{table}
469	
470	%------------------------------------------------------------------
471	\subsection{Cross-Benchmark Generalization}
472	\label{sec:res_benchmark}
473	%------------------------------------------------------------------
474	
475	Table~\ref{tab:cross_bench} shows that \caclr{} generalizes cleanly across benchmarks. The improvement magnitude is remarkably stable: 5.1--5.2pp AUROC gain and 33--40\% ECE reduction across GlobalMMLU, Belebele (reading comprehension), and MMLU-ProX (harder MCQA). The cross-benchmark coefficient of variation for \caclr{} improvement is 0.08, indicating the method addresses a fundamental representation alignment issue rather than overfitting to benchmark-specific patterns.
476	
477	\begin{table}[t]
478	\centering
479	\small
480	\caption{Cross-benchmark generalization of \caclr{}.}
481	\label{tab:cross_bench}
482	\begin{tabular}{lcccc}
483	\toprule
484	Benchmark & ZS & \caclr{} & $\Delta$pp & ECE Red.\% \\
485	\midrule
486	GlobalMMLU & .752 & .804 & 5.2 & 39.7 \\
487	Belebele & .738 & .789 & 5.1 & 36.2 \\
488	MMLU-ProX & .722 & .774 & 5.2 & 33.8 \\
489	\bottomrule
490	\end{tabular}
491	\end{table}
492	
493	%------------------------------------------------------------------
494	\subsection{Three-Architecture Validation}
495	\label{sec:res_three_arch}
496	%------------------------------------------------------------------
497	
498	Table~\ref{tab:three_arch} summarizes results across all three architectures, including Gemma~4~31B Dense. The best-transfer depth converges to 58--60\% across dense and MoE architectures with 48--94 layers. \caclr{} provides consistent 2.9--3.3pp improvement. The Pareto rank correlation is 0.82--0.88 in all cases. Dense vs.\ MoE architecture makes minimal difference---the phenomenon is a property of transformer depth, not routing architecture.
499	
500	\begin{table}[t]
501	\centering
502	\small
503	\caption{Three-architecture summary. Transfer depth\% = best cross-lingual transfer layer as percentage of total depth.}
504	\label{tab:three_arch}
505	\begin{tabular}{lcccccc}
506	\toprule
507	Model & Type & $L$ & EN & ZS-19 & Depth\% & $\rho$ \\
508	\midrule
509	Qwen3-235B & MoE & 94 & .843 & .762 & 60 & .88 \\
510	Llama 4 Scout & MoE & 48 & .821 & .741 & 58 & .82 \\
511	Gemma 4 31B & Dense & 60 & .812 & .734 & 60 & .86 \\
512	\bottomrule
513	\end{tabular}
514	\end{table}
515	
516	%------------------------------------------------------------------
517	\subsection{Extended Language Coverage}
518	\label{sec:res_extended}
519	%------------------------------------------------------------------
520	
521	Table~\ref{tab:extended_langs} summarizes the extension to 52 languages. The resource-tier gradient is smooth: \caclr{} gain increases from 3.0pp (high-resource) to 5.6pp (very-low-resource), confirming that the consistency loss provides most value where representation misalignment is worst. Zero-shot \caclr{} transfer achieves $>$0.60 AUROC for 48/51 non-English languages, establishing practical usability across the vast majority of languages without any target-language labels.
522	
523	\begin{table}[t]
524	\centering
525	\small
526	\caption{Extended coverage (52 languages) by resource tier.}
527	\label{tab:extended_langs}
528	\begin{tabular}{lccccc}
529	\toprule
530	Tier & $n$ & ZS & \caclr{} & $\Delta$pp & $>$0.60 \\
531	\midrule
532	High & 12 & .782 & .812 & 3.0 & 100\% \\
533	Mid & 25 & .738 & .784 & 4.6 & 100\% \\
534	Low & 10 & .661 & .712 & 5.1 & 90\% \\
535	Very low & 4 & .582 & .638 & 5.6 & 50\% \\
536	\bottomrule
537	\end{tabular}
538	\end{table}
539	
540	%------------------------------------------------------------------
541	\subsection{INT8 Quantization Validation}
542	\label{sec:res_int8}
543	%------------------------------------------------------------------
544	
545	Table~\ref{tab:int8} validates that INT8 weight quantization (used for Llama~4~Scout) introduces negligible distortion. The maximum AUROC difference is 0.3pp, and the rank correlation between INT8 and FP16 layer rankings is 0.997. The Pareto frontier shape and ordering are perfectly preserved, confirming that our quantized results are reliable.
546	
547	\begin{table}[t]
548	\centering
549	\small
550	\caption{INT8 vs.\ FP16 validation (Llama~4~Scout, 5\% subset).}
551	\label{tab:int8}
552	\begin{tabular}{rcccccc}
553	\toprule
554	Layer & FP16 & INT8 & $\Delta$ & FP16-ZS & INT8-ZS & $\Delta$-ZS \\
555	\midrule
556	8 & .674 & .672 & .2 & .661 & .658 & .3 \\
557	16 & .747 & .745 & .2 & .731 & .728 & .3 \\
558	24 & .788 & .786 & .2 & .747 & .744 & .3 \\
559	32 & .812 & .810 & .2 & .734 & .731 & .3 \\
560	40 & .820 & .817 & .3 & .691 & .687 & .4 \\
561	\bottomrule
562	\end{tabular}
563	\end{table}
564	
565	%------------------------------------------------------------------
566	\section{Discussion}
567	\label{sec:discussion}
568	%------------------------------------------------------------------
569	
570	\paragraph{Why CaCLR Works.}
571	The decomposition analysis (Section~\ref{sec:res_decomp}) provides a mechanistic explanation. The consistency loss ($\mathcal{L}_\text{consistency}$) specifically targets the capability-specific component---the 32\% of correctness variance that is language-dependent and drives 87\% of transfer degradation. By forcing alignment of probe outputs across languages during training, \caclr{} learns to extract language-invariant correctness features. This is strictly more powerful than post-hoc alignment (linear projection corrects first-order distributional mismatch but not nonlinear feature interactions).
572	
573	\paragraph{Why Output-Based Methods Cannot Suffice.}
574	The orthogonality results (Section~\ref{sec:res_ortho}) establish a structural limitation. With correctness and verbalized confidence directions nearly orthogonal across all 20 languages (mean cosine = 0.052), output-based methods---which operate on the confidence direction---cannot access correctness information regardless of language. The resource-tier gradient (stronger orthogonality for high-resource languages) further implies that improved multilingual training actually \emph{widens} this structural gap.
575	
576	\paragraph{Limitations.}
577	Our evaluation is restricted to MCQA benchmarks where correctness is cleanly defined. Extension to open-ended generation requires different correctness labeling strategies. The consistency loss requires parallel or comparable cross-lingual activations, which limits applicability to settings where such data exists. We evaluate only logistic regression probes; nonlinear probes may yield different tradeoff curves.
578	
579	%------------------------------------------------------------------
580	\section{Conclusion}
581	\label{sec:conclusion}
582	%------------------------------------------------------------------
583	
584	We presented the first systematic study of cross-lingual probe-based calibration, testing whether the emerging research line on representation-level calibration extends beyond English. Our four findings form a causal chain: (1)~a depth-transferability Pareto frontier constrains all probe-based calibration transfer, converging to $\sim$60\% depth across three architectures; (2)~this frontier arises because capability-specific (not difficulty-shared) signals drive transfer degradation, especially at depth; (3)~\caclr{} shifts this frontier outward, achieving $\sim$40\% ECE reduction over temperature scaling with zero target-language labels; and (4)~correctness--confidence orthogonality persists across all 20 languages, establishing output-based calibration as structurally limited regardless of language. Results extend to 52 languages and three benchmarks, confirming the generality of both the problem and our proposed solution.
585	
586	%------------------------------------------------------------------
587	% References
588	%------------------------------------------------------------------
589	%\bibliography{references}
590	%\bibliographystyle{acl_natbib}
591	
592	\begin{thebibliography}{20}
593	
594	\bibitem[\protect\citeauthoryear{Burns et al.}{2023}]{burns2023discovering}
595	Collin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt.
596	\newblock Discovering latent knowledge in language models without supervision.
597	\newblock In \emph{ICLR}, 2023.
598	
599	\bibitem[\protect\citeauthoryear{Marks et al.}{2024}]{marks2024geometry}
600	Samuel Marks, Max Tegmark, et al.
601	\newblock The geometry of truth: Emergent linear structure in large language model representations of true/false datasets.
602	\newblock In \emph{COLM}, 2024.
603	
604	\bibitem[\protect\citeauthoryear{Miao et al.}{2026a}]{miao2026coral}
605	Shuo Miao et al.
606	\newblock {CORAL}: Cross-task correctness probes for LLM calibration.
607	\newblock 2026.
608	
609	\bibitem[\protect\citeauthoryear{Miao and Ungar}{2026b}]{miao2026ortho}
610	Shuo Miao and Lyle Ungar.
611	\newblock Orthogonality of correctness and confidence directions in LLM representations.
612	\newblock 2026.
613	
614	\bibitem[\protect\citeauthoryear{Xiao et al.}{2025}]{xiao2025knowledge}
615	Zhihao Xiao et al.
616	\newblock Cross-lingual knowledge boundary probe transfer.
617	\newblock In \emph{ACL}, 2025.
618	
619	\bibitem[\protect\citeauthoryear{Civelli et al.}{2025}]{civelli2025difficulty}
620	Andrea Civelli et al.
621	\newblock Cross-lingual difficulty probe transfer in multilingual LLMs.
622	\newblock 2025.
623	
624	\bibitem[\protect\citeauthoryear{Zhou et al.}{2024}]{zhou2024lace}
625	Xin Zhou et al.
626	\newblock {LACE}: Layer-adaptive calibration ensembles for multilingual LLMs.
627	\newblock 2024.
628	
629	\bibitem[\protect\citeauthoryear{Gao et al.}{2024}]{gao2024quantization}
630	Leo Gao et al.
631	\newblock Quantization effects on probing and representation analysis.
632	\newblock 2024.
633	
634	\end{thebibliography}
635	
636	\end{document}
637	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0219af67-c473-41b2-b79a-2029a04661e1",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "657b409c-48fb-41df-870e-c816f58d3040",
  "sourceToolAssistantUUID": "0219af67-c473-41b2-b79a-2029a04661e1",
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

_source line 42 · 2026-05-20T19:39:07.722Z_

Now I have a comprehensive understanding of the paper. Let me also check the experiment data JSON for any inconsistencies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "657b409c-48fb-41df-870e-c816f58d3040",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPQJYvwdraY34EraGdN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f5ffd2b-9f0c-40cb-9ef9-1c1c0291541a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017z9tZwbfXb7XBXZjoZjBvD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13444,
      "cache_read_input_tokens": 50423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13444,
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

_source line 43 · 2026-05-20T19:39:10.102Z_

<details open><summary>🔧 Tool call — Read · `toolu_014fy8wzhFRzhsQmqbaeiKDM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f5ffd2b-9f0c-40cb-9ef9-1c1c0291541a",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPQJYvwdraY34EraGdN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "723ec184-c9ba-402b-8670-c910d1600032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017z9tZwbfXb7XBXZjoZjBvD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13444,
      "cache_read_input_tokens": 50423,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13444
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 50423,
          "cache_creation_input_tokens": 13444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13444,
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

_source line 44 · 2026-05-20T19:39:10.123Z_

<details><summary>↩ Tool result · `toolu_014fy8wzhFRzhsQmqbaeiKDM`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B",
4	    "description": "Extract activations at every 4th layer (24 probed layers out of 94), 20 languages, train English correctness probes (logistic regression + 2-layer MLP), evaluate 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\n",
5	    "results": {
6	      "en_auroc_best_layer": 0.843,
7	      "en_best_layer_idx": 72,
8	      "en_auroc_range": [
9	        0.621,
10	        0.843
11	      ],
12	      "en_ece_raw_best": 0.162,
13	      "en_ece_tempcal_best": 0.054,
14	      "temp_scaling_T": 4.87,
15	      "zs_transfer_auroc_mean_19lang_best_transfer_layer": 0.762,
16	      "zs_best_transfer_layer_idx": 56,
17	      "zs_transfer_drop_from_en_mean_pp": 8.1,
18	      "zs_auroc_by_tier": {
19	        "high_resource_mean": 0.791,
20	        "mid_resource_mean": 0.754,
21	        "low_resource_mean": 0.683
22	      },
23	      "zs_auroc_by_lang": {
24	        "en": 0.843,
25	        "zh": 0.802,
26	        "de": 0.796,
27	        "fr": 0.793,
28	        "es": 0.789,
29	        "ja": 0.785,
30	        "ru": 0.782,
31	        "pt": 0.788,
32	        "it": 0.786,
33	        "ar": 0.768,
34	        "hi": 0.761,
35	        "ko": 0.755,
36	        "vi": 0.749,
37	        "th": 0.743,
38	        "bn": 0.738,
39	        "tr": 0.756,
40	        "nl": 0.79,
41	        "sw": 0.695,
42	        "yo": 0.672,
43	        "ig": 0.681
44	      },
45	      "mean_shift_improvement_count": 2,
46	      "mean_shift_delta_ece_mean": 1.41,
47	      "linproj_auroc_mean_19lang": 0.724,
48	      "fewshot_25_auroc_mean_19lang": 0.748,
49	      "fewshot_100_auroc_mean_19lang": 0.771,
50	      "pareto_depth_transfer_rank_corr": 0.88,
51	      "pareto_frontier_layers": [
52	        40,
53	        44,
54	        48,
55	        52,
56	        56,
57	        60
58	      ],
59	      "layers_above_0p5_auroc_count": 22
60	    },
61	    "tables": [
62	      {
63	        "name": "Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by Layer",
64	        "columns": [
65	          "layer_idx",
66	          "layer_depth_pct",
67	          "en_auroc",
68	          "zs_mean_auroc_19",
69	          "zs_drop_pp",
70	          "on_pareto"
71	        ],
72	        "rows": [
73	          [
74	            4,
75	            4,
76	            0.621,
77	            0.608,
78	            1.3,
79	            false
80	          ],
81	          [
82	            8,
83	            9,
84	            0.648,
85	            0.637,
86	            1.1,
87	            false
88	          ],
89	          [
90	            12,
91	            13,
92	            0.689,
93	            0.671,
94	            1.8,
95	            false
96	          ],
97	          [
98	            16,
99	            17,
100	            0.712,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "723ec184-c9ba-402b-8670-c910d1600032",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "f6220c7c-e01b-4d92-91e0-6dc13f540c29",
  "sourceToolAssistantUUID": "723ec184-c9ba-402b-8670-c910d1600032",
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

_source line 45 · 2026-05-20T19:39:12.867Z_

I have sufficient information to produce a thorough review. Let me now also check for internal consistency issues by verifying some numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6220c7c-e01b-4d92-91e0-6dc13f540c29",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPQjZ5xK1ZNzY18P78Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ace44998-f6f3-4837-a3b3-44e651ae0ca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsqFq7M3py31CAZFVExvhV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1337,
      "cache_read_input_tokens": 63867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1337,
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

_source line 46 · 2026-05-20T19:39:13.437Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XXjSfHusy1vXfppLbavv4W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ace44998-f6f3-4837-a3b3-44e651ae0ca3",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPQjZ5xK1ZNzY18P78Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd5cfb18-3abc-490b-9830-080decabecfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsqFq7M3py31CAZFVExvhV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1337,
      "cache_read_input_tokens": 63867,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1337
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 63867,
          "cache_creation_input_tokens": 1337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1337,
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

_source line 47 · 2026-05-20T19:39:13.443Z_

<details><summary>↩ Tool result · `toolu_01XXjSfHusy1vXfppLbavv4W`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.
15	- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.
16	- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency) shifts the Pareto frontier by jointly optimizing calibration and cross-lingual invariance, enabling effective probe transfer at deeper, better-calibrated layers without target-language correctness labels.
24	- MVP evidence: Mean-shift fails entirely (0/5 languages improved) — motivates principled approach.
25	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier.
26	
27	### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
28	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
29	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
30	
31	## Story Spine
32	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
33	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
34	- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, and propose CaCLR to shift the frontier. This is both a field-level viability test and a practical method contribution.
35	- **Headline template**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
36	
37	## Field-Level Significance
38	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
39	
40	## Anticipated Reviewer Concerns & Responses
41	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier.
42	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
43	3. **"Mean-shift too weak"** → 5 transfer conditions tested. Mean-shift failure (MVP-confirmed) motivates CaCLR. Mean-shift works for Xiao et al.'s knowledge boundary but fails for correctness — important finding.
44	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
45	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
46	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
47	
48	## Differentiation from Closest Prior Work
49	| Paper | Their Focus | Our Difference |
50	|-------|-------------|----------------|
51	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier |
52	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
53	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
54	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
55	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd5cfb18-3abc-490b-9830-080decabecfb",
  "isSidechain": true,
  "promptId": "366ca7f9-8c87-45af-a404-203dffcdc31f",
  "agentId": "a1dc3465676d872cd",
  "type": "user",
  "uuid": "111ca3be-2b83-486c-8c55-2fbab2f98cff",
  "sourceToolAssistantUUID": "cd5cfb18-3abc-490b-9830-080decabecfb",
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

_source line 48 · 2026-05-20T19:40:28.291Z_

I now have a thorough understanding of the paper. Let me compile my review.

---

## Reviewer 1 (R1) Review: Methods and Experiments

### 1. Summary

This paper presents the first systematic study of cross-lingual correctness probe transfer for calibration, testing 20 languages across 3 architectures. It identifies a depth-transferability Pareto frontier, decomposes the correctness signal into difficulty-shared and capability-specific components, proposes CaCLR (a multi-objective probe training loss), and extends Miao & Ungar's orthogonality finding to multilingual settings. The experimental breadth is impressive (16 tables, 10 experiments, 3 architectures, 52 languages), and the four claims form a coherent causal chain.

### 2. Strengths

- **Comprehensive experimental design.** 10 experiments covering all 4 claims with systematic ablations, cross-architecture validation, cross-benchmark generalization, quantization validation, and extended language coverage. The experiment plan is well-prioritized (P0/P1/P2) and the coverage is thorough.

- **Strong baseline coverage.** Five transfer conditions (zero-shot, mean-shift, linear projection, few-shot-25, few-shot-100, CaCLR) provide a fair comparison space. The inclusion of mean-shift as a negative baseline is well-motivated by MVP findings.

- **Clean causal chain across claims.** The Pareto frontier (Claim 1) motivates the decomposition (Claim 2), which explains why CaCLR works (Claim 3), while orthogonality (Claim 4) establishes the structural limitation of output-based alternatives. Each claim has dedicated experiments.

- **CaCLR ablation is well-designed.** The additive ablation (BCE only, +SB-ECE, +consistency, full) cleanly isolates each component's contribution. The synergistic interaction between L_SB-ECE and L_consistency is a genuine finding.

- **Pareto frontier shift is a compelling visualization of CaCLR's value.** Table 9/7 (shifted frontier) is the paper's most impactful result -- showing that CaCLR doesn't just improve a single operating point but shifts the entire efficiency frontier.

- **INT8 validation ablation** preempts a legitimate concern. Rank correlation of 0.997 is convincing.

- **Three-architecture validation** with both MoE and dense models, converging to 58-60% optimal transfer depth, is strong evidence for generality.

### 3. Weaknesses

- **(Major) CaCLR's L_consistency requires parallel/comparable cross-lingual activations, but the paper does not specify how these are obtained.** The method section says L_consistency "penalizes divergence between EN and non-EN probe outputs on parallel activations." GlobalMMLU provides parallel questions, but: (a) are activations extracted from the exact same questions in different languages? (b) if so, this is a strong requirement not available for most practical deployment scenarios. The paper claims "no target-language labels" but does require target-language *activations* on parallel inputs, which is a non-trivial requirement that is underspecified and under-discussed.

- **(Major) The "best-transfer layer" (L56 for Qwen3) is not clearly the same layer where CaCLR is evaluated in Tables 2 vs 7.** Table 2 evaluates all conditions at L56. Table 7 (CaCLR full comparison, averaged across architectures) reports CaCLR AUROC of 0.804, but Table 9 (Pareto shift) shows CaCLR at L56 achieves 0.810, and the best CaCLR point is L60/L64 at 0.814. The headline "5.2pp improvement" appears to compare different operating points across methods, which is methodologically misleading. A fair comparison should fix the layer or explicitly optimize over layers for each method independently.

- **(Major) No confidence intervals, standard deviations, or significance tests on any result.** With 19 languages and 3 architectures, there is ample opportunity to report variance. The Spearman correlations (0.82-0.88) are reported with p-values, but AUROC and ECE differences lack any uncertainty quantification. A 5.2pp improvement could be within noise for some language subsets.

- **(Moderate) The decomposition methodology (Claim 2) has a circularity risk.** IRT difficulty is extracted from human performance data, but the probe is trained on model correctness. If model errors correlate with human difficulty (which they do -- that's the whole point), projecting out difficulty and calling the residual "capability-specific" is tautological unless the decomposition is validated on held-out data. The 81% "prescriptive accuracy" is mentioned but not defined: prescriptive of what, evaluated on what held-out set, with what baseline?

- **(Moderate) The Pareto frontier definition is non-standard and potentially misleading.** In Table 1, L60 (EN 0.831, ZS 0.753) is marked Pareto-optimal, but L40 (0.803, 0.776) strictly dominates L44 (0.810, 0.774) on the ZS axis -- L44's ZS of 0.774 is lower than L40's 0.776 while EN is higher, so L44 *is* Pareto-optimal. But L48 (0.816, 0.770) has lower ZS than L40 (0.776). In a true Pareto set, any layer not dominated should be included. The marking appears correct on inspection, but the "6 Pareto layers" claim should be verified: L32 (0.784, 0.764) is not dominated by any listed layer, yet is not marked Pareto-optimal. Why?

- **(Moderate) Linear projection baseline underperforms expectations and is not well-specified.** Table 2 shows linear projection AUROC of 0.781, but the experiment_data JSON shows linproj_auroc_mean_19lang of 0.724 for the Qwen3 full experiment. These numbers disagree (0.781 at L56 vs 0.724 across layers). The method for computing the linear projection (Procrustes? least squares? what parallel data?) is not described.

- **(Moderate) Temperature scaling baseline is applied inconsistently.** The paper reports ECE reduction "relative to temperature scaling," but temperature scaling is a post-hoc method applied to any probe's output. The fair comparison is CaCLR + temp scaling vs. zero-shot + temp scaling, not CaCLR vs. temp scaling applied to raw logits. Table 2's "ECE reduction vs tempcal" column header is ambiguous.

- **(Minor) Few-shot-25 underperforms zero-shot (0.748 vs 0.762 AUROC in Table 2).** This is counter-intuitive and not discussed. With 25 target-language examples, fine-tuning should not degrade performance unless there is catastrophic forgetting. This deserves explanation.

- **(Minor) The orthogonality cosines show suspiciously uniform Llama4-Qwen3 offset.** Every single language has Llama4 cosine exactly 0.006-0.010 higher than Qwen3 (Table 10). This uniformity across 20 typologically diverse languages is unusual and suggests a systematic bias rather than genuine architectural difference.

- **(Minor) Probe complexity comparison (Table 12) is shown only for Qwen3-235B.** The claim is about transfer properties of linear vs. nonlinear probes, but this should be validated across architectures.

### 4. Questions for Authors

1. How exactly are "parallel activations" obtained for L_consistency? Are these activations from the same GlobalMMLU questions translated into different languages? If so, does CaCLR require parallel evaluation data at training time, and how does this affect the "no target-language labels" claim?

2. What is the exact definition of "prescriptive accuracy" for the decomposition (81%)? What is the prediction target, what is the held-out evaluation set, and what is the majority-class baseline?

3. Why does few-shot-25 underperform zero-shot transfer (Table 2)? Is this due to catastrophic forgetting during fine-tuning, or label noise in 25 examples? What learning rate / regularization was used?

4. At what layer is the CaCLR headline number (0.804 AUROC, Table 7) computed? Is this the best CaCLR layer per architecture, or a fixed layer? If methods are compared at their respective best layers, this inflates CaCLR's advantage since its optimal layer differs from zero-shot's.

5. The paper claims the Pareto frontier is "convex monotonic" for both architectures (Table 4). But looking at Table 1, ZS AUROC does not monotonically decrease -- L8 (0.637) to L12 (0.671) to L16 (0.698) shows ZS increasing with depth in shallow layers. The frontier is only monotonically decreasing in the Pareto zone. Can you clarify what "convex monotonic" refers to precisely?

6. How sensitive is CaCLR to the choice of alpha and beta? The paper reports optimal values (0.15, 0.08) but no sensitivity analysis. If the optimal hyperparameters differ substantially across architectures, this undermines generalizability.

7. For the orthogonality analysis, at which layer(s) are the correctness and confidence directions extracted? If these are layer-dependent, the choice of layer could affect the cosine similarity.

### 5. Missing Experiments or Analyses

- **Per-language CaCLR results on the 20-language core set.** The paper reports resource-tier averages but never shows per-language CaCLR AUROC for all 20 languages. Some languages may show no improvement or degradation, which would be masked by tier averages.

- **CaCLR hyperparameter sensitivity analysis.** Alpha and beta are tuned on a held-out set, but no sensitivity curve is provided. Given that CaCLR is the core method contribution, this is a notable gap.

- **Statistical significance testing.** At minimum, paired bootstrap tests or Wilcoxon signed-rank tests across languages should accompany the headline CaCLR vs. baseline comparisons.

- **Computational cost comparison.** The paper mentions "~1% overhead" for CaCLR but does not report actual training time, inference time, or memory overhead relative to baselines. Linear projection requires a d-by-d matrix; how does CaCLR's cost compare in practice?

- **CaCLR on Llama 4 Scout Pareto shift.** The Pareto shift is only shown for Qwen3 (Table 9). Showing it for Llama 4 would strengthen the universality claim.

- **Cross-validated probe training.** No mention of cross-validation or train/test splits for the probes. With logistic regression on potentially high-dimensional activations, overfitting is a risk, especially for the English probe that underpins all transfer experiments.

### 6. Preliminary Score: 4 (Weak Accept)

**Justification:** The paper addresses a genuinely important and timely question -- whether probe-based calibration extends to multilingual settings. The experimental design is ambitious and the four-claim causal chain is intellectually compelling. The Pareto frontier discovery and CaCLR's ability to shift it are strong contributions. However, several methodological concerns prevent a higher score: (1) the CaCLR method's reliance on parallel activations is underspecified and the "no target-language labels" framing is potentially misleading; (2) the absence of uncertainty quantification across all results is a significant gap for a paper making quantitative claims at the 0.1-5pp level; (3) the decomposition's prescriptive accuracy claim lacks methodological detail; (4) the comparison across methods at different optimal layers inflates CaCLR's advantage. The experimental breadth is clearly above average, but the depth of methodological rigor needs strengthening. If the authors can address questions 1, 2, and 4 satisfactorily, this would be a solid accept.

### 7. Confidence: 4/5

I have high confidence in the methodological assessment. I am familiar with the probe-based calibration and cross-lingual representation transfer literatures. The internal consistency issues I flagged (linear projection numbers, Pareto definition, few-shot degradation) are based on careful reading of the tables and are unlikely to be resolved without additional data. My uncertainty comes from not having access to the actual code/data to verify the imagined numbers, and from the possibility that some of my concerns (e.g., parallel activations) may be addressed in supplementary material not included in the review copy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "111ca3be-2b83-486c-8c55-2fbab2f98cff",
  "isSidechain": true,
  "agentId": "a1dc3465676d872cd",
  "requestId": "req_011CbEPQybS8maXY9ikhg5y6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd1f8e54-4470-4244-81eb-9941700fd16a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d09a0a85-eeda-4d6e-b19c-3b10fe8c8caf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yLLds7Aeu96AdKUgyT5bz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 65204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1824,
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
