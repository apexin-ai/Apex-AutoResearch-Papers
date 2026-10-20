# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus: **methodology soundness and experimental rigor**. ## Pape

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a63f8037928e359aa.jsonl`
- **Structured JSON:** [`5935a63f408a28f1fe6f.json`](../../sessions/59/5935a63f408a28f1fe6f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

57 recorded events

### User

_source line 1 · 2026-05-20T21:12:38.127Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus: **methodology soundness and experimental rigor**.

## Paper Summary
"Does Probe-Based Calibration Work Beyond English?" — A systematic investigation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), up to 52 languages, 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot, CaCLR).

Key claims:
1. Mean-shift rank-invariance theorem: under StandardScaler + logistic regression, mean-shift produces ΔAUROC ≡ 0
2. Resource-tier taxonomy: high-resource transfers (7–8pp drop), mid marginal (10–12pp), low fails (13–20pp)
3. Practical recommendation: few-shot (25–100 labels) is the only viable path for low-resource
4. CaCLR fails (consistency loss inert, p=0.71 vs zero-shot)
5. Pareto frontier is architecture-dependent (ρ = −0.44 dense, −0.38 MoE-large, −0.18 MoE-small)
6. CKA provides suggestive but not convincing mechanistic explanation (r = 0.32)
7. Decomposition is inconclusive (difficulty removal neither helps nor hurts systematically)
8. Orthogonality persists cross-lingually but with outliers (cosine up to 0.172 for Yoruba)

## Experimental Setup
- Models: Qwen3-235B-A22B (94 layers, MoE, INT8), Llama 4 Scout (48 layers, MoE, INT8), Gemma 4 31B Dense (60 layers, FP16)
- Benchmarks: GlobalMMLU (primary), Belebele, MMLU-ProX
- Languages: Core 20 (12 families, 3 tiers), Extended 52 (15 families, 4 tiers)
- Probes: logistic regression (default) + 2-layer MLP (512 hidden, ReLU), StandardScaler-normalized
- Layers: every 4th layer per model
- Stats: Bootstrap CIs (1000 resamples), paired permutation tests, Cohen's d

## Key Tables from Paper
- Table 1: English probe AUROC by layer across 3 architectures. Best: Qwen3 L72 = 0.776, Llama4 L36 = 0.749, Gemma4 L45 = 0.761
- Table 2: Zero-shot transfer by resource tier. High: Q3=.663, L4=.648; Mid: Q3=.615, L4=.582; Low: Q3=.548, L4=.522
- Table 3: 52-language extended results. Overall mean 0.581, 24% pass rate. Very-low (n=10): 0.518, 0% pass
- Table 4: Per-language zero-shot on Qwen3. Best layer shifts shallower for low-resource (L52→L24 from zh→yo). Spearman ρ ranges from −0.55 (zh) to +0.31 (yo)
- Table 5: Three-architecture comparison. Pareto ρ: Qwen3 −0.38, Llama4 −0.18, Gemma4 −0.44. Sign consistency: 0.63, 0.53, 0.68
- Table 6: Transfer methods (19-lang mean). Zero-shot=.618/.588, Mean-shift=.618/.588 (d=0.00), CaCLR=.623/.594 (d=0.04), LinProj=.636/.608 (d=0.24), Few-shot-25=.644/.617 (d=0.35), Few-shot-100=.662/.641 (d=0.58)
- Table 7: CaCLR ablation. Full CaCLR=.621, BCE+SB-ECE (no consistency)=.627, BCE+Consistency=.611, BCE only=.618, LinProj ref=.636. Removing consistency IMPROVES by 0.6pp
- Table 8: CaCLR β sensitivity. β from 0 to 1.0, AUROC monotonically decreases from .627 to .618
- Table 9: Decomposition ablation. Residual (diff out): Q3=.613 (−0.5pp), L4=.583 (−0.5pp). Random direction control: −0.3pp
- Table 10: Orthogonality cosine. High=0.052, Mid=0.073, Low=0.108, All=0.074
- Table 11: CKA correlation. Qwen3 r=0.38, Llama4 r=0.24, Combined r=0.32
- Table 12: Linear projection by n pairs. 10→.608(−1.0pp), 50→.636(+1.8pp), 200→.647(+2.9pp)
- Table 13: Control task selectivity. High=17.2pp, Mid=13.8pp, Low=8.4pp (min 4.8pp)

## Experiment Design Reference (what was planned)
12 experiments were planned. The paper covers all major ones:
- Plan 001: Qwen3 Pareto frontier (covered in Tables 1-4)
- Plan 002: Llama4 Pareto frontier (covered in Table 5, cross-arch comparison)
- Plan 003: CaCLR (covered in Tables 6-8)
- Plan 004: Difficulty decomposition (covered in Table 9)
- Plan 005: Orthogonality (covered in Table 10)
- Plan 006: Probe complexity (mentioned: MLP +1.0pp EN, −0.3pp transfer, d=0.15, p=0.34)
- Plan 007: Additional benchmarks (covered in §5.12)
- Plan 008: Gemma 4 (covered in Table 5)
- Plan 009: Extended 52 languages (covered in Table 3)
- Plan 010: INT8 validation (covered in §5.11)
- Plan 011: CKA analysis (covered in Table 11, §5.8)
- Plan 012: Linear projection sensitivity (covered in Table 12)
- Plan 013: Control tasks (covered in Table 13)

## Your Review Task
Evaluate ONLY methodology and experiments. Produce a structured review with:

1. **Methodology Assessment** (soundness of the approach, statistical rigor, controls)
2. **Experimental Coverage** (completeness, missing experiments, coverage of planned experiments)
3. **Strengths** (3-5 bullet points)
4. **Weaknesses** (3-5 bullet points with severity: minor/moderate/major)
5. **Questions for Authors** (2-3 specific methodological questions)
6. **Score** (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)
7. **Confidence** (1-5: 1=low, 5=expert)

Be rigorous. This is a top ML venue with ~25% acceptance rate.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "093bf73e-1f63-4a86-b386-245cfd15ebf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T21:12:38.132Z_

```json
{
  "parentUuid": "093bf73e-1f63-4a86-b386-245cfd15ebf5",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
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
  "uuid": "cc99831b-5073-4593-9f8e-36915fdb96e2",
  "timestamp": "2026-05-20T21:12:38.132Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T21:12:41.106Z_



I'll start by loading the project files to understand the full paper and experimental details before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc99831b-5073-4593-9f8e-36915fdb96e2",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWY7v1Ke52NnU75KUKR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55606ad6-99fe-4a1a-a72a-5cbcf7015de3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNyNGAmq3WRRH2BUUofm2w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7900,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7900,
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

_source line 4 · 2026-05-20T21:12:42.033Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Bv4B2Vg44S7UNmJsc6VQyU`</summary>

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
  "parentUuid": "55606ad6-99fe-4a1a-a72a-5cbcf7015de3",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWY7v1Ke52NnU75KUKR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e416791a-4281-4924-85b0-c41912776c38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YNyNGAmq3WRRH2BUUofm2w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7900,
      "cache_read_input_tokens": 8251,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 127,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7900,
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

_source line 5 · 2026-05-20T21:12:42.038Z_

<details><summary>↩ Tool result · `toolu_01Bv4B2Vg44S7UNmJsc6VQyU`</summary>

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
  "parentUuid": "e416791a-4281-4924-85b0-c41912776c38",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "6f727e07-ca15-4684-9ebe-318f8fe7c712",
  "sourceToolAssistantUUID": "e416791a-4281-4924-85b0-c41912776c38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T21:12:44.928Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01F1B2PNmnbf6gR7YfRnpdme`</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f727e07-ca15-4684-9ebe-318f8fe7c712",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWYQokhnYD7BzWifwAd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0534dd11-abae-4a47-89b8-e20e101ee4a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016aaXq1m62sF7SNNXJSE97w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 16151,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 7 · 2026-05-20T21:12:44.967Z_

<details><summary>↩ Tool result · `toolu_01F1B2PNmnbf6gR7YfRnpdme`</summary>

```text
{"result":"# 项目 xling_calib_direction 概况\n\n## 实验状态 (3 个)\n\n- **mvp_003**: DONE (success) — \n- **mvp_001**: DONE (success) — \n- **mvp_002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_003** (success): Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). ← 基于 mvp_001\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\n- **mvp_002** (success): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\n\n## 趋势\n成功 3 / 负向 0 / 失败 0 / 共 3\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-13176: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0534dd11-abae-4a47-89b8-e20e101ee4a2",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "04722fe2-9d24-4bec-9865-142d2313a34d",
  "sourceToolAssistantUUID": "0534dd11-abae-4a47-89b8-e20e101ee4a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T21:12:45.433Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CooTwZuLsDpfGFCPHztovc`</summary>

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
  "parentUuid": "04722fe2-9d24-4bec-9865-142d2313a34d",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWYQokhnYD7BzWifwAd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d152b80e-0080-4493-ac08-5ecec0e9b107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016aaXq1m62sF7SNNXJSE97w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 16151,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1449
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 16151,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1449,
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

_source line 9 · 2026-05-20T21:12:45.447Z_

<details><summary>↩ Tool result · `toolu_01CooTwZuLsDpfGFCPHztovc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_003** (success): Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). ← 基于 mvp_001\\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\\n- **mvp_002** (success): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 0 / 共 3\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-13176: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1012, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d152b80e-0080-4493-ac08-5ecec0e9b107",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "7ebf6afd-4c77-42da-9f5d-c51166e851c8",
  "sourceToolAssistantUUID": "d152b80e-0080-4493-ac08-5ecec0e9b107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T21:12:48.366Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0175RCHX9QTQUE4CEPom3N8H`</summary>

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
  "parentUuid": "7ebf6afd-4c77-42da-9f5d-c51166e851c8",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWYfSaE7st24uaynkks",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f57c361-fe5c-47a3-ab41-f6f1dee52cc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ogoBh96YdBpRL7FLrFzD1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 17600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1689,
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

_source line 11 · 2026-05-20T21:12:48.375Z_

<details><summary>↩ Tool result · `toolu_0175RCHX9QTQUE4CEPom3N8H`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/memory.md\", \"content\": \"# Memory — xling_calib_direction\\n\\n## 环境配置\\n- **服务器**: westd-13176, 4× RTX 6000 PRO 96GB\\n- **环境**: conda base (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)\\n- **模型路径 (Qwen)**: `/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct`\\n- **模型路径 (Llama)**: ModelScope `LLM-Research/Meta-Llama-3.1-8B-Instruct`\\n- **代码路径**: `/root/xling_calib_direction/`\\n- **备份路径**: `/root/autodl-tmp/xling_backup/` (29GB, mvp_001/002/003 全部)\\n- **Qwen2.5-7B-Instruct**: 28 layers (0-27), hidden_dim=3584\\n- **Llama-3.1-8B-Instruct**: 32 layers (0-31), hidden_dim=4096\\n- **网络**: 不要用 `source /etc/network_turbo`，用 `HF_ENDPOINT=https://hf-mirror.com`\\n- **模型下载**: 用 ModelScope\\n- **磁盘**: 根分区仅 620MB 可用 ⚠️，所有大文件必须放 `/root/autodl-tmp/`（~290GB 可用）\\n\\n## 数据集字段差异\\n- cais/mmlu: `choices` (list), `answer` (int 0-3)\\n- CohereForAI/Global-MMLU: `option_a/b/c/d` (str), `answer` (letter \\\"A\\\"-\\\"D\\\")\\n\\n## MVP 实验关键发现 (2026-05-20)\\n\\n### Mean-shift alignment 完全无效\\n- 不能改变 AUROC（rank-invariant）\\n- 不能改善 calibration（0/5 ΔECE）\\n- 结论：需要非常数 alignment 方法（CDA/CORAL/Procrustes）\\n\\n### Temperature scaling data leakage 教训 (M005)\\n在 test set 上优化 T 并报告 ECE = data leakage。修复后 ECE 全部 FAIL（temp scaling 实际恶化 ECE）。**教训**: 后处理校准必须用 held-out validation set。\\n\\n### Sigmoid 饱和导致 AUROC 评估 artifact\\n- zh@L31 (Llama): logit 均值=+39 → 55% 样本 predict_proba=1.0 → ranking 退化\\n- **修复**: transfer_eval.py 应改用 `decision_function` 算 AUROC（logits 足够）\\n- ECE/Brier 仍需 predict_proba\\n\\n### Layer-depth profile\\n- Qwen: L0-L10 平台(~0.62) → L10-L22 上升(+11pp) → L22-L27 饱和(~0.75)\\n- Llama: 类似趋势，L0=0.65 → L31=0.73，delta=9.53pp\\n- 最后一层英语最强但迁移最差（更 language-specific）\\n\\n### CKA vs Transfer Degradation（核心分析发现）\\n- **CKA 随深度单调下降**（两个模型一致）：深层 representation 更 language-specific\\n- **CKA-degradation 负相关**：Llama rho=-0.52 p=0.001***, Qwen rho=-0.31 p=0.053\\n- **Language ranking 两模型一致**: zh > ar >> hi ≈ sw（高资源 → 高 CKA + 低 degradation）\\n- 解读：correctness signal 是跨语言共享的低维子空间特征，即使全局 representation 已 language-specific\\n\\n### mvp_003 (Llama) 亮点\\n**5/5 语言 pass P2**（包括 sw=0.584），优于 Qwen 的 4/5。Llama-3.1 多语言覆盖更广。\\n\\n### 修正后 Gate Check\\n- Qwen: P1❌ P2✅(4/5) P3✅(14.28pp) P4❌ → PARTIAL 2/4\\n- Llama: P1❌ P2✅(5/5) P3✅(9.53pp) P4❌ → PARTIAL 2/4\\n\\n## 大模型可行性（research 阶段）\\n- Qwen3-235B-A22B: **INT4** 推荐，VRAM ~125G (4 GPU), 磁盘 ~120G\\n- Llama 4 Scout: **INT8** 推荐，VRAM ~115G (2 GPU), 磁盘 ~110G\\n- **关键改动**: 必须用 `register_forward_hook` 替代 `output_hidden_states=True`（94 层全缓存 OOM）\\n- 需要 `pip install bitsandbytes`\\n\\n## 代码修复记录\\n- **M004**: --layers default=None（自动检测），已部署\\n- **待修复**: transfer_eval.py 改用 decision_function 算 AUROC（避免 sigmoid 饱和）\\n\", \"total_chars\": 2525, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f57c361-fe5c-47a3-ab41-f6f1dee52cc9",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "b25ad09d-5689-4c11-b290-3723d79da3c5",
  "sourceToolAssistantUUID": "2f57c361-fe5c-47a3-ab41-f6f1dee52cc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T21:12:49.315Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017ds1AKCpfuvHcEtGQ5L19m`</summary>

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
  "parentUuid": "b25ad09d-5689-4c11-b290-3723d79da3c5",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWYfSaE7st24uaynkks",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "021dda82-a68f-442a-ba1d-932df03506fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ogoBh96YdBpRL7FLrFzD1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 17600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1689,
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

_source line 13 · 2026-05-20T21:12:49.325Z_

<details><summary>↩ Tool result · `toolu_017ds1AKCpfuvHcEtGQ5L19m`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "021dda82-a68f-442a-ba1d-932df03506fd",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "0f79b403-b979-4dd2-a8c0-e35be13a7e4c",
  "sourceToolAssistantUUID": "021dda82-a68f-442a-ba1d-932df03506fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T21:12:49.527Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WiYc7zCor2kwUKvwjHAhUt`</summary>

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
  "parentUuid": "0f79b403-b979-4dd2-a8c0-e35be13a7e4c",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWYfSaE7st24uaynkks",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1685423-28d5-413c-96bb-215f2487fcec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ogoBh96YdBpRL7FLrFzD1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 17600,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 17600,
          "cache_creation_input_tokens": 1689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1689,
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

_source line 15 · 2026-05-20T21:12:49.537Z_

<details><summary>↩ Tool result · `toolu_01WiYc7zCor2kwUKvwjHAhUt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-20 20:18 UTC | 更新原因: Reviewer feedback integrated: D12 grid justification, D16 mean-shift formalization, CaCLR Path B geometric theory, per-language rho, CKA pilot\\n\\n## 核心方向\\nCross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier (depth vs transferability). CaCLR tests distributional matching; CKA provides mechanistic explanation. Mean-shift rank-invariance proof as formal theoretical contribution. 详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research phase** — MVP 通过 (D004)，Dream 审稿处理完成 (D005)，Reviewer 反馈已整合。等待 re-dream 验证后批准 P0。\\n\\n## Dream 审稿处理总结\\n- 初审评分: best=4/6, median=3/6, worst=3/6 (weak reject)\\n- 13+2 条确认行动项已执行（Reviewer 补充 D12 grid 理由 + D16 mean-shift 形式化）\\n- CaCLR framing 改为 conditional narrative（Path A method / Path B negative result with geometric explanation）\\n- 新增 3 P1 实验: plan_011 (CKA), plan_012 (linproj sensitivity), plan_013 (probing controls)\\n- 全局统计检验要求 + per-language Pareto rho + threshold sensitivity\\n- 5 条观察项待真实实验\\n\\n## 紧急事项\\n- ⚠️ Temperature scaling T=6.21 数据划分未确认 — Agent 正在检查（data integrity 风险）\\n- Agent 同时跑 CKA pilot（MVP activations，验证 plan_011 pipeline）\\n\\n## 近期任务\\n- [ ] Agent 确认 temp scaling 数据划分 + CKA pilot 结果\\n- [ ] 确认 mvp_003 (Llama-3.1-8B) 结果\\n- [ ] Re-dream 验证 framing/plan 改动（目标: best ≥ weak accept, median ≥ borderline）\\n- [ ] Re-dream 达标后批准 plan_001 + plan_002（P0，可 4 GPU 并行）\\n- [ ] [Dream 观察] O1: plan_002 Llama4 Pareto rho\\n- [ ] [Dream 观察] O3: plan_003 CaCLR consistency loss\\n- [ ] [Dream 观察] O4: plan_005 orthogonality 贡献度\\n\\n## GPU 预算\\n- 分配: 4× RTX 6000 PRO 96GB (westd-13176)\\n- P0: ~155 GPU-hrs | P1: ~39 GPU-hrs (含 Dream 新增 9h) | P2: ~80 GPU-hrs\\n- MVP 已用: ~7 GPU-hrs\\n\\n## 实验计划\\n详见 experiment_plan.yaml。P0: 4 (plan_001-004)。P1: 7 (plan_005-013)。P2: 2 (plan_008-009)。\\nCross-cutting: bootstrap CI + paired test + Cohen's d + AUROC threshold sensitivity + per-language rho。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D008 | 2026-05-20 | Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4 | mvp_003, mvp_001 |\\n| D007 | 2026-05-20 | mvp_003 (Llama-3.1-8B) cross-architecture validati | mvp_003, mvp_001 |\\n| D006 | 2026-05-20 | MVP gate re-evaluation after P1 leakage fix: 2/4 P | mvp_001, plan_003 |\\n| D005 | 2026-05-20 | Dream review (3/6 weak reject) processed: 13 confi | plan_003, plan_011, plan_012, plan_013 |\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\n| D002 | 2026-05-20 | MVP 模型固定为 Qwen2.5-7B-Instruct | — |\\n| D001 | 2026-05-20 | MVP 用 7-8B 模型验证核心假设，不直接上 235B | — |\\n\\n\", \"total_chars\": 2633, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1685423-28d5-413c-96bb-215f2487fcec",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "371a6340-66b7-411a-9f90-0c6b9fb7278e",
  "sourceToolAssistantUUID": "a1685423-28d5-413c-96bb-215f2487fcec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-20T21:12:52.899Z_

Now let me read the paper itself and any detailed experimental artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "371a6340-66b7-411a-9f90-0c6b9fb7278e",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWYxqqHqjkYowBL11Kp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5bbee9b-328f-42f6-9d0b-8f84475b4d23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4LtFNQvaUKr5gEaR6LmRM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3517,
      "cache_read_input_tokens": 19289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3517,
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

_source line 17 · 2026-05-20T21:12:53.657Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01N7MvaEvM4skJZFTqfMRtWE`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5bbee9b-328f-42f6-9d0b-8f84475b4d23",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWYxqqHqjkYowBL11Kp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc507e69-f708-43c1-9996-56fdd8fe85af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4LtFNQvaUKr5gEaR6LmRM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3517,
      "cache_read_input_tokens": 19289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3517,
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

_source line 18 · 2026-05-20T21:12:53.676Z_

<details><summary>↩ Tool result · `toolu_01N7MvaEvM4skJZFTqfMRtWE`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/best/paper.tex
artifacts/dream_reports/dream_20260520T185641/median/paper.tex
artifacts/dream_reports/dream_20260520T185641/worst/paper.tex
artifacts/dream_reports/dream_20260520T201854/best/paper.tex
artifacts/dream_reports/dream_20260520T201854/median/paper.tex
artifacts/dream_reports/dream_20260520T201854/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc507e69-f708-43c1-9996-56fdd8fe85af",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "1f19dbfb-6e7f-4382-bca3-f2c519b67d8f",
  "sourceToolAssistantUUID": "dc507e69-f708-43c1-9996-56fdd8fe85af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T21:12:53.963Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Y4D2ZKE8oXy6Q6AEHV37S8`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f19dbfb-6e7f-4382-bca3-f2c519b67d8f",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWYxqqHqjkYowBL11Kp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55084f13-21f6-4457-86de-15a433a1acd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4LtFNQvaUKr5gEaR6LmRM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3517,
      "cache_read_input_tokens": 19289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3517,
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

_source line 20 · 2026-05-20T21:12:53.978Z_

<details><summary>↩ Tool result · `toolu_01Y4D2ZKE8oXy6Q6AEHV37S8`</summary>

```text
.claude/sessions/distiller_70eed89a/CLAUDE.md
.claude/sessions/distiller_70eed89a/AGENTS.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260520T185641/best/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/median/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T185641/median/review_report.md
artifacts/dream_reports/dream_20260520T185641/best/review_report.md
.claude/sessions/review_reviewer_1_4b9e3221/CLAUDE.md
.claude/sessions/review_reviewer_1_4b9e3221/AGENTS.md
.claude/sessions/review_reviewer_2_dfeebd74/CLAUDE.md
.claude/sessions/review_reviewer_2_dfeebd74/AGENTS.md
artifacts/dream_reports/dream_20260520T185641/worst/review_report.md
artifacts/review_reports/round_0.md
.claude/sessions/review_director_91c72a1c/CLAUDE.md
.claude/sessions/review_director_91c72a1c/AGENTS.md
report.md
artifacts/_project/report/cka_vs_degradation_report.md
memory.md
ROADMAP.md
artifacts/dream_reports/dream_20260520T201854/best/paper_framing.md
artifacts/dream_reports/dream_20260520T201854/median/paper_framing.md
paper_framing.md
artifacts/dream_reports/dream_20260520T201854/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T201854/best/review_report.md
.claude/sessions/director_a0a38807/CLAUDE.md
.claude/sessions/director_a0a38807/AGENTS.md
artifacts/dream_reports/dream_20260520T201854/median/review_report.md
.claude/sessions/reviewer_b0408cba/CLAUDE.md
.claude/sessions/reviewer_b0408cba/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/agent_3e57a809/CLAUDE.md
.claude/sessions/agent_3e57a809/AGENTS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55084f13-21f6-4457-86de-15a433a1acd3",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "41816805-4072-479b-88b4-654bae48b82e",
  "sourceToolAssistantUUID": "55084f13-21f6-4457-86de-15a433a1acd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T21:12:54.257Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EeBmNApR9XFTRSYeiKo3tf`</summary>

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
  "parentUuid": "41816805-4072-479b-88b4-654bae48b82e",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWYxqqHqjkYowBL11Kp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7bedb89-c1cf-42dc-b3f3-927bfb2a7bb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4LtFNQvaUKr5gEaR6LmRM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3517,
      "cache_read_input_tokens": 19289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3517,
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

_source line 22 · 2026-05-20T21:12:54.270Z_

<details><summary>↩ Tool result · `toolu_01EeBmNApR9XFTRSYeiKo3tf`</summary>

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
artifacts/dream_reports/dream_20260520T185641/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T185641/best/review_context.yaml
artifacts/dream_reports/dream_20260520T185641/median/review_context.yaml
artifacts/dream_reports/dream_20260520T185641/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T185641/meta.yaml
artifacts/review_issues.yaml
artifacts/manifest.yaml
decisions.yaml
artifacts/dream_reports/dream_20260520T201854/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T201854/median/imagined_experiments.yaml
registry.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260520T201854/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T201854/best/review_context.yaml
artifacts/dream_reports/dream_20260520T201854/median/review_context.yaml
mistakes.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260520T201854/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7bedb89-c1cf-42dc-b3f3-927bfb2a7bb4",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "9cc2e92f-5eea-42ac-9307-ed47f9e3e07d",
  "sourceToolAssistantUUID": "a7bedb89-c1cf-42dc-b3f3-927bfb2a7bb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T21:12:56.994Z_

Let me read the latest dream paper (the best version from the most recent dream) and the experiment plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cc2e92f-5eea-42ac-9307-ed47f9e3e07d",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWZKJ9SwMfWyehFJKX1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b8b842a-43d0-41f3-896f-1f8f4ff11c43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSQU73zvpS2gabRwRDxdAi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1606,
      "cache_read_input_tokens": 22806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1606,
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

_source line 24 · 2026-05-20T21:12:57.920Z_

<details open><summary>🔧 Tool call — Read · `toolu_017sh2FKTJMLVfhKg9ASKgWK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b8b842a-43d0-41f3-896f-1f8f4ff11c43",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWZKJ9SwMfWyehFJKX1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1104eb7e-eaa4-4624-b763-087d2ae364c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSQU73zvpS2gabRwRDxdAi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1606,
      "cache_read_input_tokens": 22806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1606,
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

_source line 25 · 2026-05-20T21:12:58.118Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T9mT7mPYMW7WwK1dnGKLSF`</summary>

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
  "parentUuid": "1104eb7e-eaa4-4624-b763-087d2ae364c7",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWZKJ9SwMfWyehFJKX1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1164e983-e3ec-4c93-9bba-0eb3a0264034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PSQU73zvpS2gabRwRDxdAi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1606,
      "cache_read_input_tokens": 22806,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1606
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 22806,
          "cache_creation_input_tokens": 1606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1606,
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

_source line 26 · 2026-05-20T21:12:58.122Z_

<details><summary>↩ Tool result · `toolu_01T9mT7mPYMW7WwK1dnGKLSF`</summary>

```text
1	experiments:
2	  # === P0: Core submission (must complete for EACL 2027 ARR Aug 3) ===
3	
4	  - id: plan_001
5	    claim: 1
6	    description: >
7	      Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT4):
8	      extract activations at every 4th layer (24 probed layers),
9	      20 typologically diverse languages, train English correctness probes
10	      (logistic regression + 2-layer MLP), evaluate 5 transfer conditions
11	      (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).
12	      Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.
13	      Use register_forward_hook (not output_hidden_states) to avoid OOM on 94 layers.
14	    priority: P0
15	    gpu_budget_hours: 80
16	    deps: []
17	    notes: >
18	      4× RTX 6000 PRO 96GB, INT4 quantization (~125GB VRAM).
19	      INT4 (not INT8) required to fit 235B model. Need INT4 validation ablation
20	      (compare INT4 vs INT8 at representative layers on subset — extend plan_010).
21	
22	  - id: plan_002
23	    claim: 1
24	    description: >
25	      Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8):
26	      extract activations at every 4th layer (12 probed layers),
27	      20 languages, 5 transfer conditions. INT8 weight quantization.
28	      Report per-language Spearman rho (depth vs transfer AUROC) alongside global rho.
29	    priority: P0
30	    gpu_budget_hours: 40
31	    deps: []
32	    notes: "Needs 2× RTX 6000 PRO 96GB at INT8."
33	
34	  - id: plan_003
35	    claim: 3
36	    description: >
37	      CaCLR implementation and comparative evaluation:
38	      L_CaCLR = L_BCE + α·L_SB-ECE + β·L_consistency (MMD distance).
39	      Train CaCLR probes using English labels + unlabeled parallel activations
40	      (GlobalMMLU train split translations, not test items).
41	      Compare vs zero-shot, mean-shift, linear projection, few-shot (25/100)
42	      across full Pareto frontier for both models × 20 languages.
43	      Hyperparameter tuning: α sweep (0.01-10.0), β sweep across 3 OOM (0.001-1.0).
44	      Report fixed-layer results (50% depth + EN-optimal) alongside per-language oracle.
45	    priority: P0
46	    gpu_budget_hours: 20
47	    deps: [plan_001, plan_002]
48	    notes: >
49	      CPU-bound once activations cached. SB-ECE from Karandikar et al. NeurIPS 2021.
50	      L_consistency uses Maximum Mean Discrepancy (MMD).
51	      If β sweep shows inert consistency loss, reframe as negative result (see paper_framing.md Claim 3 conditional narrative).
52	
53	  - id: plan_004
54	    claim: 2
55	    description: >
56	      Difficulty-controlled ablation: train IRT difficulty probes (Ridge regression
57	      on human difficulty scores per Civelli et al.), project out difficulty direction
58	      from activations, retrain correctness probes on residuals, evaluate transfer.
59	      10 representative languages × 8 representative layers per model (20-90% depth).
60	    priority: P0
61	    gpu_budget_hours: 15
62	    deps: [plan_001, plan_002]
63	    notes: >
64	      Need IRT difficulty scores from GlobalMMLU or external source.
65	      Grid justification (D12): 10 languages cover 3 resource tiers (HIGH: zh/es/fr/de, MID: hi/ru/ko/tr, LOW: sw/bn)
66	      × major language families. 8 layers span 20-90% depth at uniform intervals.
67	      Reduced grid is sufficient because decomposition tests a qualitative hypothesis
68	      (does projecting out difficulty help or hurt?), not a per-language quantitative claim.
69	      Include random-direction control to rule out dimensionality-reduction artifacts.
70	
71	  # === Cross-cutting requirement (Dream review D1) ===
72	  # All experiments must include: bootstrap CIs (1000 resamples),
73	  # paired permutation tests for key comparisons, Cohen's d for effect sizes.
74	  # Report GlobalMMLU sample sizes per language.
75	  # AUROC threshold sensitivity analysis (0.55/0.60/0.65/0.70/0.75) for pass/fail reporting.
76	
77	  # === P1: Important for strong submission ===
78	
79	  - id: plan_005
80	    claim: 4
81	    description: >
82	      Cross-lingual orthogonality analysis: extract verbalized confidence direction
83	      (prompt model for confidence score, fit probe), compute cosine similarity
84	      with correctness direction across 20 languages × 2 architectures.
85	      Analyze by resource tier (high/mid/low) and language family.
86	    priority: P1
87	    gpu_budget_hours: 10
88	    deps: [plan_001, plan_002]
89	
90	  - id: plan_006
91	    claim: 1
92	    description: >
93	      Probe complexity comparison: logistic regression vs 2-layer MLP
94	      at each probed layer for both models. Compare English accuracy,
95	      cross-lingual transfer degradation, and calibration quality.
96	      Test hypothesis: linear probes transfer better cross-lingually.
97	    priority: P1
98	    gpu_budget_hours: 5
99	    deps: [plan_001, plan_002]
100	    notes: "CPU-bound, uses cached activations."
101	
102	  - id: plan_007
103	    claim: 1
104	    description: >
105	      Additional benchmark evaluation: evaluate best probes + CaCLR
106	      on Belebele (20 languages) and MMLU-ProX (20 languages).
107	      Validates generalization beyond MMLU/GlobalMMLU.
108	    priority: P1
109	    gpu_budget_hours: 30
110	    deps: [plan_001, plan_002, plan_003]
111	
112	  - id: plan_010
113	    claim: 1
114	    description: >
115	      Quantization validation ablation: (a) compare INT8 vs FP16 at 5 representative
116	      layers for Llama 4 Scout on 5% random subset; (b) compare INT4 vs INT8 at
117	      5 representative layers for Qwen3-235B on 5% random subset.
118	      Validates that quantization doesn't distort correctness signals.
119	    priority: P1
120	    gpu_budget_hours: 10
121	    deps: [plan_001, plan_002]
122	
123	  - id: plan_011
124	    claim: [1, 4]
125	    description: >
126	      CKA cross-lingual representation similarity analysis:
127	      compute CKA (linear kernel) between English and each target language
128	      at every probed layer for both models. Full-scale validation of pilot finding:
129	      correctness direction is a robust low-dimensional subspace feature that persists
130	      despite global CKA decline. Transfer collapses only at critical CKA threshold (~0.35).
131	      Report CKA × layer × language heatmaps, CKA vs transfer degradation
132	      ((EN_AUROC - target_AUROC) / EN_AUROC) correlation per language to isolate
133	      alignment effect from probe quality, and critical threshold analysis.
134	    priority: P1
135	    gpu_budget_hours: 5
136	    deps: [plan_001, plan_002]
137	    notes: >
138	      CKA pilot COMPLETED on mvp_001/mvp_003 (5 langs × 8-9 layers × 2 models).
139	      Key finding: CKA-degradation negatively correlated (Llama rho=-0.52 p=0.001,
140	      Qwen rho=-0.31 p=0.053). Per-language: Llama hi rho=-0.73 p=0.025 sig.
141	      CAUTION (Reviewer): pooled correlation has depth confound. Pilot per-language
142	      Spearman almost all n.s. (n=9 too small), ko direction reversed. Overall p=0.007
143	      driven by BETWEEN-language differences (zh/ar high CKA + low degradation vs
144	      hi/sw low CKA + high degradation), not within-language depth effects.
145	      Supportable claim: "languages with higher CKA exhibit less transfer degradation"
146	      (between-language, qualitative at n=5). NOT supportable: "CKA predicts within-
147	      language degradation across depth."
148	      Full-scale analysis (20 langs) MUST include: (a) same-layer cross-language
149	      correlation (strongest test, n=20 per layer), (b) partial correlation controlling
150	      for depth, (c) per-language Spearman with denser layer sampling.
151	      CKA cliff steepness explains Qwen-Llama Pareto strength difference (qualitative).
152	
153	  - id: plan_012
154	    claim: 1
155	    description: >
156	      Linear projection sensitivity analysis: vary number of parallel
157	      pairs (10, 20, 50, 100, 200) for linear projection transfer.
158	      Determines minimum data requirement for this surprisingly strong baseline.
159	      Both models × 5 representative layers × 20 languages.
160	    priority: P1
161	    gpu_budget_hours: 2
162	    deps: [plan_001, plan_002]
163	    notes: "CPU-bound, uses cached activations. Dream review D11."
164	
165	  - id: plan_013
166	    claim: 1
167	    description: >
168	      Probing control tasks (Hewitt & Liang 2019): train probes on
169	      randomly permuted labels at each layer. Compare selectivity
170	      (probe AUROC - control AUROC) across layers and languages.
171	      Validates that high AUROC reflects genuine correctness direction,
172	      not memorized dataset artifacts or probe capacity.
173	    priority: P1
174	    gpu_budget_hours: 2
175	    deps: [plan_001, plan_002]
176	    notes: "CPU-bound. Dream review D22: probing methodology critique."
177	
178	  # === P2: Camera-ready extension ===
179	
180	  - id: plan_008
181	    claim: 1
182	    description: >
183	      Gemma 4 31B Dense (60 layers, dense, FP16): third architecture
184	      for camera-ready. Full Pareto frontier, 20+ languages.
185	      Provides dense vs MoE architectural contrast.
186	    priority: P2
187	    gpu_budget_hours: 30
188	    deps: []
189	
190	  - id: plan_009
191	    claim: 1
192	    description: >
193	      Extended language coverage: expand from 20 to 50+ languages
194	      for camera-ready. Leverages GlobalMMLU/Belebele full language sets.
195	    priority: P2
196	    gpu_budget_hours: 50
197	    deps: [plan_001, plan_002]
198	
199	  # === MVP experiments (completed/running) ===
200	
201	  - id: mvp_validation
202	    claim: 1
203	    description: "MVP: Qwen2.5-7B-Instruct, 6 languages, 8 layers, zero-shot + mean-shift"
204	    priority: P0
205	    registry_id: mvp_001
206	    gpu_budget_hours: 2
207	    deps: []
208	
209	  - id: mvp_complementary
210	    claim: 1
211	    description: "MVP robustness: complementary layer set (2,6,10,14,18,22,26)"
212	    priority: P1
213	    registry_id: mvp_002
214	    gpu_budget_hours: 2
215	    deps: [mvp_validation]
216	
217	  - id: mvp_llama_control
218	    claim: 1
219	    description: "MVP cross-architecture: Llama-3.1-8B control experiment"
220	    priority: P1
221	    registry_id: mvp_003
222	    gpu_budget_hours: 3
223	    deps: [mvp_validation]
224	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1164e983-e3ec-4c93-9bba-0eb3a0264034",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "0bc5593b-5b38-47ef-972d-c8b970500eeb",
  "sourceToolAssistantUUID": "1164e983-e3ec-4c93-9bba-0eb3a0264034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T21:12:58.381Z_

<details><summary>↩ Tool result · `toolu_017sh2FKTJMLVfhKg9ASKgWK`</summary>

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
  "parentUuid": "1104eb7e-eaa4-4624-b763-087d2ae364c7",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "b6eadc32-ab53-47f5-b692-2cb102d96121",
  "sourceToolAssistantUUID": "1104eb7e-eaa4-4624-b763-087d2ae364c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T21:13:02.080Z_

Now let me read the previous review reports and the paper framing document for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6eadc32-ab53-47f5-b692-2cb102d96121",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWZcVk59bXiSKRhgfsv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1202486-18fb-4eed-8a0e-69e81e866e03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyzGr3Z6JdTdyLk3zeDRnj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3434,
      "cache_creation_input_tokens": 12944,
      "cache_read_input_tokens": 24412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12944,
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

_source line 29 · 2026-05-20T21:13:04.372Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VRG4MokxtjCFBnnJUfoAqz`</summary>

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
  "parentUuid": "e1202486-18fb-4eed-8a0e-69e81e866e03",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWZcVk59bXiSKRhgfsv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63b30e77-e9a9-4239-a8a4-cdf434dd95d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyzGr3Z6JdTdyLk3zeDRnj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3434,
      "cache_creation_input_tokens": 12944,
      "cache_read_input_tokens": 24412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12944,
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

_source line 30 · 2026-05-20T21:13:04.379Z_

<details><summary>↩ Tool result · `toolu_01VRG4MokxtjCFBnnJUfoAqz`</summary>

```text
1	---
2	dream_id: dream_20260520T201854
3	tier: best
4	overall_score: weak accept (4/6)
5	timestamp: 2026-05-20T21:08:45.594579+00:00
6	---
7	
8	---
9	dream_id: dream_20260520T201854
10	tier: best
11	overall_score: weak accept (4/6)
12	reviewer: R1 (Methods & Experiments)
13	timestamp: 2026-05-20
14	---
15	
16	# Review: Cross-Lingual Correctness Probes Reveal a Depth-Transferability Pareto Frontier
17	
18	**Reviewer R1 — Methods & Experiments Focus**
19	
20	---
21	
22	## 1. Summary
23	
24	The paper presents the first systematic evaluation of cross-lingual correctness probe transfer, studying 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20+ languages, and 5 transfer methods. The central finding is a depth-transferability Pareto frontier: deeper layers improve English probe AUROC but degrade zero-shot cross-lingual transfer. The paper proposes CaCLR, a composite training objective with an MMD-based consistency loss, and provides CKA-based analysis, difficulty-capability decomposition, and confirmation that correctness-confidence orthogonality persists across languages. Statistical testing (bootstrap CIs, permutation tests, Cohen's d) is applied to key claims.
25	
26	---
27	
28	## 2. Strengths
29	
30	**S1. Comprehensive experimental scope with appropriate controls.** The paper covers a large design space: 3 architectures x 20 languages x 5 transfer methods x 3 benchmarks, with well-chosen ablations. The probe complexity comparison (LR vs MLP, Table 7/Appendix B), INT8 validation (Appendix A), Hewitt & Liang control tasks (Appendix D), and random-direction control in the decomposition analysis all demonstrate methodological care. Few papers in this area provide this breadth of validation.
31	
32	**S2. Mean-shift invariance proof is a clean theoretical contribution.** The formal argument that mean-shift yields AUROC = 0.000 under StandardScaler + logistic regression is elegant and practically valuable. It corrects an implicit assumption from prior work (Xiao et al.) and is confirmed empirically. This is the kind of tight theory-experiment alignment that strengthens a paper.
33	
34	**S3. Statistical rigor on key comparisons.** The CaCLR beta effect (p=0.003, d=0.48, bootstrap CI [0.019, 0.045]) and the decomposition effect (p=0.006, d=0.41) are reported with appropriate paired permutation tests and effect sizes. This goes well beyond the field's typical standard of reporting only point estimates.
35	
36	**S4. Difficulty-capability decomposition is well-designed.** Using IRT difficulty probes to extract and project out the difficulty direction, then retraining correctness probes on residuals, is a sound methodology. The random-direction control (~0pp, Table 4) is essential and properly rules out dimensionality reduction artifacts. The resource-tier gradient (LOW +4.1pp vs HIGH +2.2pp) provides interpretable structure.
37	
38	**S5. Linear projection data efficiency analysis is practically valuable.** The saturation curve (Table 6) showing that ~50 parallel pairs achieve 98% of 200-pair performance, with the tier-stratified breakdown (LOW languages needing ~48 pairs vs HIGH needing ~22), gives practitioners actionable guidance. This is more useful than many method contributions.
39	
40	---
41	
42	## 3. Weaknesses
43	
44	### Major
45	
46	**W1. CaCLR's marginal advantage undermines the method contribution framing.** CaCLR beats 50-pair linear projection by only +1.4pp median AUROC and slightly loses to few-shot 100 (-0.8pp). Linear projection requires 50 translated question-answer pairs and a closed-form matrix solve. CaCLR requires parallel activations across all target languages, gradient-based training of a 3-term composite loss with two hyperparameters (alpha, beta), and careful tuning (the beta sweep shows the method is sensitive to this choice: 0.001 yields +0.8pp, 0.1 yields +3.2pp, 1.0 drops to +2.1pp). The paper frames CaCLR as needing "zero target-language labels," but it does need parallel inputs — and the 50 parallel pairs needed by linear projection are a strict subset of the parallel inputs needed by CaCLR. The cost-benefit calculus favors linear projection for most practical settings.
47	
48	**W2. Architecture-dependence claim is confounded and cannot support causal attribution.** The three models differ in architecture type (2 MoE, 1 Dense), scale (235B vs 109B vs 31B), layer count (94 vs 48 vs 60), active parameters (22B vs 17B vs 31B), and training data composition. The paper attributes the Pareto frontier shape difference to "MoE expert routing accelerating language specialization" (Section 6), but no evidence isolates this mechanism. No expert routing analysis (e.g., routing entropy by language, expert specialization metrics) is presented. The claim that Gemma 4's smoother frontier is "consistent with gradual rather than discrete language specialization" is post-hoc narrative, not evidence. Three confounded data points are insufficient for causal attribution. The claim should be qualified as observational.
49	
50	**W3. CKA "mechanistic explanation" is correlational and likely confounded by depth.** The r=0.82 Pearson correlation between CKA and transfer AUROC (Table 3/Section 5.5) is presented as a "mechanistic explanation," but depth is an obvious confounder: CKA decreases monotonically with depth, and transfer AUROC also varies monotonically with depth (past the elbow). The correlation could be entirely mediated by depth without CKA playing any causal role. A partial correlation controlling for (normalized) depth would clarify how much of the r=0.82 survives. The current framing overstates the evidence. The subspace angle analysis (correctness direction rotating 15-35 degrees at deep layers vs 5-12 degrees at shallow) is more informative but is described only textually without quantitative results in any table.
51	
52	**W4. Pareto frontier reported at reduced resolution despite experimental design specifying full coverage.** The experimental design calls for 24 probed layers on Qwen3 (every 4th of 94) and 12 on Scout. Table 1 reports only 7 layers for Qwen3 and 6 for Scout. The review_context.yaml contains all 17 Qwen3 layers and 13 Scout layers. Reporting 7/24 raises concerns about selective presentation. The full layer-wise data should appear in a supplementary table, particularly since the Pareto frontier is the paper's titular contribution. Furthermore, the per-language Spearman rho values (rho = -0.78 median, IQR [-0.84, -0.71] for Qwen3) are reported only as summary statistics — showing the full per-language distribution would strengthen the claim that the frontier is consistent across languages.
53	
54	**W5. CaCLR training procedure is underspecified.** The paper states probes are logistic regression (Section 3.1), but CaCLR requires gradient-based optimization of a composite loss with MMD (Section 3.3). Critical details are missing: (a) Is the CaCLR probe still a single linear layer trained with SGD, or is it a different architecture? (b) What MMD kernel is used (Gaussian RBF, linear, polynomial)? What bandwidth? (c) What optimizer, learning rate schedule, number of epochs? (d) How many parallel activation pairs are used for the MMD term? (e) How is the train/validation split handled — is the MMD computed on the same data as BCE? These details are essential for reproducibility and for assessing whether the method is fairly compared against the simpler baselines.
55	
56	### Minor
57	
58	**W6. Selective statistical reporting.** Bootstrap CIs and permutation tests are applied to the CaCLR beta effect and decomposition, but not to: the Pareto rho values, the CKA-transfer correlation (the CI [0.76, 0.87] is marginal and does not account for depth confounding), the orthogonality measurements, or the cross-benchmark correlation (r=0.92). Multiple comparison corrections are absent across the many language x layer x model comparisons. The paper applies rigorous statistics where results are strong and omits them elsewhere.
59	
60	**W7. Orthogonality table shows only 10/20 languages.** Table 5 displays 10 languages but the claim states "all 20 languages below 0.062." Showing half the evidence for a central claim is a presentation gap. The full table should appear in the appendix at minimum.
61	
62	**W8. INT8 validation covers only Scout, not Qwen3.** The INT8 vs FP16 comparison (Appendix A) uses Llama 4 Scout at 5 layers with a 5% random subset. Qwen3-235B-A22B, the primary model for most results, has no quantization validation. Quantization effects may differ across architectures and scales. Even a small-scale Qwen3 validation (5 layers, subset) would address this.
63	
64	**W9. The causal chain has a logical gap between decomposition and CaCLR.** The decomposition (Claim 2) identifies difficulty entanglement as a transfer degradation mechanism. CaCLR (Claim 3) uses MMD distributional alignment, not difficulty removal. The narrative implies decomposition motivates CaCLR, but CaCLR does not operationalize the decomposition insight. A natural experiment — running CaCLR on difficulty-removed representations — would close this gap and potentially improve CaCLR further.
65	
66	---
67	
68	## 4. Questions for Authors
69	
70	1. **Can you provide the full 24-layer Pareto table for Qwen3 and 12-layer for Scout?** If the experiments were run as designed, this data exists. Was the subsampling a space decision or does the full data show irregularities?
71	
72	2. **What is the partial correlation between CKA and transfer AUROC after controlling for normalized depth?** This single number would clarify whether CKA adds explanatory power beyond "deeper = worse transfer."
73	
74	3. **What MMD kernel and bandwidth are used in CaCLR?** Are the parallel activations for MMD drawn from the same items as the BCE training data, or a separate set?
75	
76	4. **Is CaCLR's probe still a single linear layer?** If so, how is gradient-based optimization of a logistic regression with 3 loss terms implemented — is it trained from scratch with SGD, or initialized from the standard LR solution?
77	
78	5. **What happens when CaCLR is applied to difficulty-removed representations?** Does decomposition + CaCLR stack, or are they addressing the same variance?
79	
80	6. **Can you provide expert routing entropy by language and depth for the MoE models?** This would support or refute the "expert routing drives language specialization" claim directly.
81	
82	7. **What are the absolute per-language ECE values (raw, temp-scaled, CaCLR-calibrated) for at least the tier-representative languages?** The "3.5% reduction over temperature scaling" is uninformative without baseline context.
83	
84	8. **How sensitive is the optimal transfer depth (60% for Qwen3, 50% for Scout) to the choice of benchmark?** The cross-benchmark table (Table 8) shows consistent method rankings, but does Belebele's optimal transfer layer differ from GlobalMMLU's?
85	
86	---
87	
88	## 5. Minor Issues
89	
90	- Table 1 for Scout omits ZS Min and ZS Max columns without explanation.
91	- The bibliography has several placeholder citations (empty \cite{} in the introduction).
92	- "CaCLR reduces non-English ECE by 3.5%" — unclear whether this is 3.5 percentage points or 3.5 relative percent. Context suggests the former but should be explicit.
93	- The Gemma 4 results (Appendix C) are summary-only. Given that this is the third architecture and the key dense-vs-MoE contrast, even a condensed per-layer table would strengthen the paper.
94	- The paper lists 20 languages but explicitly names only ~12 (en, zh, es, fr, de, hi, ru, ko, tr, sw, bn, plus references to "and X others"). The full language list should appear in Section 4 or an appendix.
95	
96	---
97	
98	## 6. Overall Assessment
99	
100	**Score: 4/6 (Weak Accept)**
101	**Confidence: 4/5**
102	
103	**Rationale.** This paper tackles a genuinely important and underexplored problem — whether probe-based calibration works beyond English — at impressive scale. The experimental design is thorough, covering multiple architectures, languages, benchmarks, and transfer conditions with appropriate ablations and controls. Several analytical contributions are strong: the mean-shift invariance proof, the difficulty-capability decomposition with random-direction control, the linear projection data efficiency analysis, and the confirmation of universal correctness-confidence orthogonality. The statistical practice, where applied, meets a high standard.
104	
105	The paper falls short of a strong accept for three reasons. First, the headline method contribution (CaCLR) provides only marginal improvement (+1.4pp) over the much simpler linear projection baseline, and the training procedure is underspecified. Second, the architecture-dependence and CKA "mechanistic" claims are overstated relative to the evidence — three confounded models cannot support causal claims about expert routing, and a correlational CKA analysis confounded by depth is not mechanistic. Third, key results are reported at reduced resolution (7/24 layers, 10/20 languages), which is concerning for a paper whose titular contribution is a "frontier" that demands dense sampling.
106	
107	The paper would be strengthened by: (a) reframing as primarily an analytical/characterization contribution with CaCLR as one demonstrated application, (b) reporting the full layer and language data, (c) qualifying the architecture-dependence and CKA claims, (d) providing CaCLR implementation details, and (e) testing CaCLR on difficulty-removed representations to close the causal chain.
108	
109	The analytical findings — particularly the Pareto frontier quantification, decomposition, orthogonality universality, and the practical finding that ~50 parallel pairs suffice for effective linear projection — represent genuine contributions to the field's understanding of multilingual calibration. These alone warrant publication at a top venue, provided the framing matches the evidence.
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63b30e77-e9a9-4239-a8a4-cdf434dd95d8",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "32afba3f-e4f8-44c5-90e4-5eb8646bf6a0",
  "sourceToolAssistantUUID": "63b30e77-e9a9-4239-a8a4-cdf434dd95d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T21:13:04.636Z_

<details open><summary>🔧 Tool call — Read · `toolu_0177v3MWcxczHUJPPDzv9QRo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32afba3f-e4f8-44c5-90e4-5eb8646bf6a0",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWZcVk59bXiSKRhgfsv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2d24557-63e8-4c9f-8a02-adca3f581e61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyzGr3Z6JdTdyLk3zeDRnj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3434,
      "cache_creation_input_tokens": 12944,
      "cache_read_input_tokens": 24412,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3434,
          "output_tokens": 194,
          "cache_read_input_tokens": 24412,
          "cache_creation_input_tokens": 12944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12944,
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

_source line 32 · 2026-05-20T21:13:04.643Z_

<details><summary>↩ Tool result · `toolu_0177v3MWcxczHUJPPDzv9QRo`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff is architecture-dependent (strong on Qwen, weak on Llama), explained by architecture-specific CKA cliff steepness. CaCLR tests whether distributional matching can shift this frontier without target-language labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes reveal an architecture-dependent depth-transferability relationship: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong Pareto); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture-dependence of the Pareto shape is itself a core finding, not merely a qualifier.
15	- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).
16	- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method / Diagnostic)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.
24	- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
25	- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA pilot reveals the mechanistic explanation: correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.
26	- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.
27	- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
28	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.
29	
30	### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
31	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
32	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
33	
34	## Story Spine
35	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
36	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
37	- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.
38	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
39	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines."
40	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
41	
42	## Field-Level Significance
43	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
44	
45	## Anticipated Reviewer Concerns & Responses
46	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
47	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
48	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
49	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
50	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
51	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
52	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
53	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
54	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
55	10. **"No mechanistic explanation"** → CKA analysis provides two levels of insight: (a) between-language: languages with higher CKA (more aligned to English) show less transfer degradation — resource-tier gradient explained; (b) between-architecture: CKA cliff steepness at deepest layers differs (Qwen drops 50% in last 3 layers vs Llama 19%), explaining why Pareto is strong on Qwen but weak on Llama. Within-language depth effect requires 20-language full-scale analysis for statistical power (pilot n=9 per language insufficient). CKA pilot on 2 models × 5 languages validates the approach.
56	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
57	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
58	
59	## Additional Related Work Coverage (Dream-identified gaps)
60	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.
61	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.
62	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA pilot reveals correctness direction is a robust low-dimensional subspace feature that persists despite global representation divergence. Not a simple "low CKA → bad transfer" relationship, but a threshold phenomenon: transfer collapses only when CKA drops below critical value (~0.35) at deepest layers.
63	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.
64	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
65	
66	## Differentiation from Closest Prior Work
67	| Paper | Their Focus | Our Difference |
68	|-------|-------------|----------------|
69	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
70	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
71	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
72	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
73	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2d24557-63e8-4c9f-8a02-adca3f581e61",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "21aa17f9-0679-4120-a7a5-78b0b14ab183",
  "sourceToolAssistantUUID": "d2d24557-63e8-4c9f-8a02-adca3f581e61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-20T21:13:07.672Z_

Now let me also read the review context files and the imagined experiments for a fuller picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21aa17f9-0679-4120-a7a5-78b0b14ab183",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWa5FaJRFhzx4sLoL6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a53c8eb9-2e56-45f3-809c-3a1102ea185e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoKuLwxWN64Tu9i5ux9UTk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10574,
      "cache_read_input_tokens": 37356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10574,
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

_source line 34 · 2026-05-20T21:13:09.510Z_

<details open><summary>🔧 Tool call — Read · `toolu_014ygN5Cv9DipfoSNqrY8Pfg`</summary>

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
  "parentUuid": "a53c8eb9-2e56-45f3-809c-3a1102ea185e",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWa5FaJRFhzx4sLoL6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21355779-b44f-4e7a-a80a-e9857ac5f5ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoKuLwxWN64Tu9i5ux9UTk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10574,
      "cache_read_input_tokens": 37356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10574,
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

_source line 35 · 2026-05-20T21:13:09.775Z_

<details><summary>↩ Tool result · `toolu_014ygN5Cv9DipfoSNqrY8Pfg`</summary>

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
  "parentUuid": "21355779-b44f-4e7a-a80a-e9857ac5f5ad",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "9c773ffd-e70f-4fc9-ac17-e2d2360f0ada",
  "sourceToolAssistantUUID": "21355779-b44f-4e7a-a80a-e9857ac5f5ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T21:13:10.089Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NHqpMQethqdQDMuaS23AZ7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c773ffd-e70f-4fc9-ac17-e2d2360f0ada",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWa5FaJRFhzx4sLoL6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21e97dd3-1a7a-41c2-b3c0-db71236a925c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoKuLwxWN64Tu9i5ux9UTk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10574,
      "cache_read_input_tokens": 37356,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10574
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 37356,
          "cache_creation_input_tokens": 10574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10574,
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

_source line 37 · 2026-05-20T21:13:10.358Z_

<details><summary>↩ Tool result · `toolu_01NHqpMQethqdQDMuaS23AZ7`</summary>

```text
1	tier: best
2	narrative_guidance: 'Full method contribution paper (Path A). CaCLR consistency loss
3	  provides meaningful gain, confirming distributional matching via MMD helps align
4	  capability-specific signals at mid-depth layers. Causal chain complete: Pareto frontier
5	  discovered on both architectures with architecture-dependent shape → decomposition
6	  explains frontier via difficulty/capability separation → CaCLR shifts frontier by
7	  aligning capability-specific components → orthogonality bounds output-based approaches
8	  across all languages. CKA provides mechanistic glue linking representation geometry
9	  to transfer success. Headline: "CaCLR-trained correctness probes reduce non-English
10	  ECE by 3.5% over temperature scaling with zero target-language labels across 20
11	  languages on Qwen3-235B and Llama 4 Scout."
12	
13	  '
14	imagined_experiments:
15	- name: Full Pareto Frontier — Qwen3-235B-A22B
16	  plan_id: plan_001
17	  description: '94-layer MoE model, INT8, 24 probed layers (every 4th), 20 languages,
18	    5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100,
19	    CaCLR).
20	
21	    '
22	  expected_results:
23	    en_best_auroc: 0.838
24	    en_best_layer: 76
25	    en_best_ece_raw: 0.162
26	    en_best_ece_tempcal: 0.048
27	    temp_scaling_T: 4.83
28	    en_auroc_range:
29	    - 0.592
30	    - 0.838
31	    optimal_transfer_layer_median: 56
32	    zs_transfer_auroc_median_20lang: 0.758
33	    zs_transfer_auroc_at_en_optimal_layer76: 0.714
34	    zs_transfer_auroc_at_transfer_optimal_layer56: 0.771
35	    pareto_rho_global: -0.81
36	    pareto_rho_per_lang_median: -0.78
37	    pareto_rho_per_lang_iqr:
38	    - -0.84
39	    - -0.71
40	    zs_langs_above_0p65_out_of_20: 17
41	    best_zs_auroc_by_tier:
42	      HIGH_zh: 0.793
43	      HIGH_es: 0.801
44	      HIGH_fr: 0.798
45	      HIGH_de: 0.784
46	      MID_hi: 0.742
47	      MID_ru: 0.769
48	      MID_ko: 0.751
49	      MID_tr: 0.738
50	      LOW_sw: 0.641
51	      LOW_bn: 0.633
52	    mean_shift_delta_auroc_median: 0.0
53	    linear_proj_delta_auroc_over_zs_median: 0.048
54	    fewshot_25_delta_auroc_over_zs_median: 0.032
55	    fewshot_100_delta_auroc_over_zs_median: 0.055
56	  result_rationale: 'Qwen3-235B-A22B的94层深度和MoE架构产生了强correctness信号。235B参数量使EN AUROC达到0.838，
57	    远超7B MVP的0.754——更大模型的内部表征更丰富、correctness方向更可分离。 Pareto frontier清晰存在：layer 76（81%深度）是EN最优但跨语言transfer在此处下降约5.7pp
58	    （从layer 56的0.771降至0.714），因为深层表征越来越language-specific。 MoE架构中expert routing在深层更加language-dependent，强化了这一效应。
59	    Spearman rho中位数-0.78反映depth-transfer反相关在绝大多数语言中一致。 17/20语言ZS AUROC>0.65体现了235B模型强大的multilingual
60	    representation—— 仅sw/bn/my三个极低资源语言未达标，符合Ben-David H-divergence理论预测。 Mean-shift
61	    ΔAUROC=0.000由rank-invariance定理保证（StandardScaler + logistic regression下 mean-shift仅添加常数偏移，不改变rank
62	    order）。 Linear projection作为强baseline（+4.8pp）反映correctness方向在语言间存在可学习的线性映射关系。
63	
64	    '
65	  tables:
66	  - name: 'Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by
67	      Layer'
68	    columns:
69	    - layer
70	    - depth_pct
71	    - en_auroc
72	    - zs_median_auroc
73	    - zs_min_auroc
74	    - zs_max_auroc
75	    - rho_median
76	    rows:
77	    - - 0
78	      - 0
79	      - 0.592
80	      - 0.583
81	      - 0.521
82	      - 0.601
83	      - null
84	    - - 8
85	      - 9
86	      - 0.631
87	      - 0.618
88	      - 0.554
89	      - 0.639
90	      - null
91	    - - 16
92	      - 17
93	      - 0.672
94	      - 0.659
95	      - 0.589
96	      - 0.678
97	      - null
98	    - - 24
99	      - 26
100	      - 0.711
101	      - 0.698
102	      - 0.621
103	      - 0.719
104	      - null
105	    - - 32
106	      - 34
107	      - 0.738
108	      - 0.729
109	      - 0.648
110	      - 0.751
111	      - null
112	    - - 40
113	      - 43
114	      - 0.762
115	      - 0.756
116	      - 0.662
117	      - 0.778
118	      - null
119	    - - 48
120	      - 51
121	      - 0.781
122	      - 0.771
123	      - 0.658
124	      - 0.793
125	      - null
126	    - - 56
127	      - 60
128	      - 0.798
129	      - 0.771
130	      - 0.641
131	      - 0.801
132	      - null
133	    - - 60
134	      - 64
135	      - 0.808
136	      - 0.762
137	      - 0.632
138	      - 0.796
139	      - null
140	    - - 64
141	      - 68
142	      - 0.816
143	      - 0.751
144	      - 0.618
145	      - 0.788
146	      - null
147	    - - 68
148	      - 72
149	      - 0.824
150	      - 0.741
151	      - 0.607
152	      - 0.779
153	      - null
154	    - - 72
155	      - 77
156	      - 0.831
157	      - 0.728
158	      - 0.598
159	      - 0.768
160	      - null
161	    - - 76
162	      - 81
163	      - 0.838
164	      - 0.714
165	      - 0.584
166	      - 0.756
167	      - null
168	    - - 80
169	      - 85
170	      - 0.835
171	      - 0.702
172	      - 0.571
173	      - 0.742
174	      - null
175	    - - 84
176	      - 89
177	      - 0.829
178	      - 0.688
179	      - 0.558
180	      - 0.729
181	      - null
182	    - - 88
183	      - 94
184	      - 0.818
185	      - 0.671
186	      - 0.542
187	      - 0.712
188	      - null
189	    - - 92
190	      - 98
191	      - 0.801
192	      - 0.649
193	      - 0.523
194	      - 0.694
195	      - null
196	  - name: 'Table 2: Qwen3-235B Transfer Conditions at Fixed Layers (layer 56 + layer
197	      76)'
198	    columns:
199	    - condition
200	    - layer56_median_auroc
201	    - layer76_median_auroc
202	    - delta_vs_zs_l56
203	    - delta_vs_zs_l76
204	    rows:
205	    - - zero-shot
206	      - 0.771
207	      - 0.714
208	      - 0.0
209	      - 0.0
210	    - - mean-shift
211	      - 0.771
212	      - 0.714
213	      - 0.0
214	      - 0.0
215	    - - linear_proj_50pairs
216	      - 0.812
217	      - 0.779
218	      - 0.041
219	      - 0.065
220	    - - fewshot_25
221	      - 0.798
222	      - 0.761
223	      - 0.027
224	      - 0.047
225	    - - fewshot_100
226	      - 0.821
227	      - 0.792
228	      - 0.05
229	      - 0.078
230	    - - CaCLR_full
231	      - 0.828
232	      - 0.788
233	      - 0.057
234	      - 0.074
235	  figures_description:
236	  - 'Fig 1a: Pareto frontier scatter — x-axis EN AUROC, y-axis ZS transfer AUROC median.
237	    Each point is a layer. Clear concave frontier with elbow at ~60% depth. Color
238	    by resource tier shows HIGH langs cluster top-right, LOW langs bottom-left.'
239	  - 'Fig 1b: Heatmap 24 layers × 20 languages, cell color = ZS AUROC. Visible gradient:
240	    warm (high AUROC) at mid-depth for high-resource, shifting to shallower optimum
241	    for low-resource.'
242	  - 'Fig 1c: Per-language Spearman rho distribution (violin plot). Median -0.78, tight
243	    IQR, all languages negative. Annotate sw/bn as outliers with weaker rho.'
244	  analysis: 'Pareto frontier 在 Qwen3-235B 上形态清晰。拐点在 layer 56（60% depth）—— 此后EN AUROC继续上升但ZS
245	    transfer开始下降。MoE架构的expert routing在深层 更加language-specific是造成Pareto tradeoff的主要机制。High-resource语言
246	    （zh/es/fr/de）的frontier更靠右上方，因为这些语言在pretraining中获得更多 token coverage，deep-layer
247	    representation与EN的对齐更好。Low-resource（sw/bn） 即使在最优transfer层也仅达到0.64左右，符合H-divergence理论预测。
248	
249	    '
250	- name: Full Pareto Frontier — Llama 4 Scout
251	  plan_id: plan_002
252	  description: '48-layer MoE model, INT8, 12 probed layers (every 4th), 20 languages,
253	    5 transfer conditions.
254	
255	    '
256	  expected_results:
257	    en_best_auroc: 0.821
258	    en_best_layer: 40
259	    en_best_ece_raw: 0.171
260	    en_best_ece_tempcal: 0.053
261	    temp_scaling_T: 5.12
262	    en_auroc_range:
263	    - 0.604
264	    - 0.821
265	    optimal_transfer_layer_median: 24
266	    zs_transfer_auroc_median_20lang: 0.742
267	    zs_transfer_auroc_at_en_optimal_layer40: 0.698
268	    zs_transfer_auroc_at_transfer_optimal_layer24: 0.756
269	    pareto_rho_global: -0.76
270	    pareto_rho_per_lang_median: -0.73
271	    pareto_rho_per_lang_iqr:
272	    - -0.81
273	    - -0.66
274	    zs_langs_above_0p65_out_of_20: 16
275	    best_zs_auroc_by_tier:
276	      HIGH_zh: 0.778
277	      HIGH_es: 0.789
278	      HIGH_fr: 0.781
279	      HIGH_de: 0.772
280	      MID_hi: 0.728
281	      MID_ru: 0.756
282	      MID_ko: 0.739
283	      MID_tr: 0.721
284	      LOW_sw: 0.628
285	      LOW_bn: 0.618
286	    mean_shift_delta_auroc_median: 0.0
287	    linear_proj_delta_auroc_over_zs_median: 0.044
288	  result_rationale: 'Llama 4 Scout的48层架构使optimal transfer层在50%深度（layer 24）， 而Qwen3-235B在60%深度（layer
289	    56）——这就是architecture-dependent shape的关键证据。 Scout的层数不到Qwen的一半，deep层的language specialization发生得更快（按比例）。
290	    EN best AUROC=0.821略低于Qwen的0.838，反映Scout虽然是MoE但active参数更少。 ZS median 0.742 vs
291	    Qwen的0.758，差距16pp体现了Llama系列multilingual pretraining 数据在低资源语言上的相对弱势。Pareto rho中位数-0.73略弱于Qwen的-0.78，
292	    因为Scout只有12个probed层，frontier采样更粗糙。16/20语言>0.65（vs Qwen 17/20）， sw/bn/my/jv四个低资源语言未达标。Architecture-dependent差异是本文Claim
293	    1的核心发现。
294	
295	    '
296	  tables:
297	  - name: 'Table 3: Llama 4 Scout Pareto Frontier'
298	    columns:
299	    - layer
300	    - depth_pct
301	    - en_auroc
302	    - zs_median_auroc
303	    rows:
304	    - - 0
305	      - 0
306	      - 0.604
307	      - 0.592
308	    - - 4
309	      - 8
310	      - 0.638
311	      - 0.624
312	    - - 8
313	      - 17
314	      - 0.674
315	      - 0.661
316	    - - 12
317	      - 25
318	      - 0.712
319	      - 0.701
320	    - - 16
321	      - 33
322	      - 0.741
323	      - 0.738
324	    - - 20
325	      - 42
326	      - 0.768
327	      - 0.756
328	    - - 24
329	      - 50
330	      - 0.788
331	      - 0.756
332	    - - 28
333	      - 58
334	      - 0.801
335	      - 0.742
336	    - - 32
337	      - 67
338	      - 0.811
339	      - 0.726
340	    - - 36
341	      - 75
342	      - 0.818
343	      - 0.711
344	    - - 40
345	      - 83
346	      - 0.821
347	      - 0.698
348	    - - 44
349	      - 92
350	      - 0.814
351	      - 0.679
352	    - - 48
353	      - 100
354	      - 0.798
355	      - 0.654
356	  figures_description:
357	  - 'Fig 2a: Pareto frontiers overlaid — Qwen3-235B (blue) vs Llama 4 Scout (orange).
358	    Both concave but elbow position differs: Qwen at 60% depth, Scout at 50%. Demonstrates
359	    architecture-dependent shape.'
360	  - 'Fig 2b: Architecture comparison heatmap — difference in ZS AUROC (Qwen minus
361	    Scout) by language × normalized depth. Positive (Qwen better) at deep layers for
362	    high-resource; near zero at shallow layers.'
363	  analysis: '两个架构的Pareto frontier在归一化深度上呈现不同形状：Qwen3-235B的拐点在60%深度， Scout在50%深度。这一差异不能由模型大小alone解释（两者都是MoE），
364	    而是反映了训练数据分布、expert routing策略和层归一化实现的差异。 Scout在每层的language specialization更剧烈，导致frontier更陡峭、拐点更早。
365	    这是论文最核心的发现之一：optimal transfer depth不是universal的，必须per-architecture确定。
366	
367	    '
368	- name: CaCLR Implementation and Comparative Evaluation
369	  plan_id: plan_003
370	  description: 'CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD) 训练、超参数sweep、与所有baseline的全面比较。
371	    Path A: β term provides meaningful gain.
372	
373	    '
374	  expected_results:
375	    caclr_optimal_alpha: 1.0
376	    caclr_optimal_beta: 0.1
377	    caclr_beta_delta_auroc_over_alpha_only_median: 0.032
378	    caclr_beta_delta_auroc_over_alpha_only_range:
379	    - 0.018
380	    - 0.051
381	    caclr_full_delta_auroc_over_zeroshot_median: 0.062
382	    caclr_full_delta_auroc_over_zeroshot_range:
383	    - 0.031
384	    - 0.098
385	    caclr_vs_linear_proj_delta_median: 0.014
386	    caclr_vs_fewshot100_delta_median: -0.008
387	    ece_reduction_vs_temp_scaling_median: 0.035
388	    ece_reduction_vs_temp_scaling_range:
389	    - 0.012
390	    - 0.061
391	    beta_sweep_results:
392	      beta_0.001:
393	        delta_auroc_over_alpha_only: 0.008
394	        note: too weak
395	      beta_0.01:
396	        delta_auroc_over_alpha_only: 0.019
397	        note: marginal
398	      beta_0.1:
399	        delta_auroc_over_alpha_only: 0.032
400	        note: optimal
401	      beta_1.0:
402	        delta_auroc_over_alpha_only: 0.021
403	        note: overfitting to distributional match
404	    alpha_sweep_results:
405	      alpha_0.01:
406	        en_ece: 0.068
407	        transfer_auroc_median: 0.779
408	      alpha_0.1:
409	        en_ece: 0.055
410	        transfer_auroc_median: 0.793
411	      alpha_1.0:
412	        en_ece: 0.041
413	        transfer_auroc_median: 0.808
414	      alpha_10.0:
415	        en_ece: 0.038
416	        transfer_auroc_median: 0.791
417	    layer_interaction:
418	      mid_depth_beta_gain: 0.041
419	      deep_layer_beta_gain: 0.024
420	      shallow_layer_beta_gain: 0.018
421	    qwen_results:
422	      layer56_caclr_full_median: 0.828
423	      layer76_caclr_full_median: 0.788
424	    scout_results:
425	      layer24_caclr_full_median: 0.812
426	      layer40_caclr_full_median: 0.771
427	    bootstrap_ci_beta_effect:
428	    - 0.019
429	    - 0.045
430	    paired_permutation_p_beta: 0.003
431	    cohens_d_beta: 0.48
432	  result_rationale: 'CaCLR consistency loss (β term) 提供了有意义的增益（中位数+3.2pp over α-only），
433	    支持Path A叙事。β=0.1是最优点——更低（0.001-0.01）则MMD约束太弱无法对齐分布， 更高（1.0）则过度约束导致correctness
434	    prediction损失。 β增益在mid-depth层（40-60%）最大（+4.1pp），因为这些层的cross-lingual表征 仍有足够的共享结构让MMD可以有效对齐，但已经开始出现分化需要对齐。
435	    在deep层β增益下降到+2.4pp，因为表征的geometric misalignment（非仅distributional shift） 限制了MMD的有效性——但CaCLR仍然比zero-shot好得多。
436	    CaCLR vs linear projection：CaCLR赢1.4pp中位数，因为它同时优化calibration（α项） 和alignment（β项），而linear
437	    projection仅做alignment。但CaCLR略输于few-shot 100 （-0.8pp），因为100个标注样本提供了直接的target-language
438	    correctness信号。 关键：CaCLR不需要target-language labels，这是实际场景中的核心优势。 ECE reduction vs
439	    temp scaling中位数3.5pp，因为CaCLR在训练时直接优化SB-ECE， 而temp scaling仅做post-hoc rescaling无法修复表征层面的miscalibration。
440	    Bootstrap CI [0.019, 0.045]和p=0.003确认β效应统计显著；Cohen''s d=0.48为中等效应量。
441	
442	    '
443	  tables:
444	  - name: 'Table 4: Transfer Method Comparison (Median AUROC across 20 languages,
445	      both models)'
446	    columns:
447	    - method
448	    - labels_needed
449	    - qwen_layer56
450	    - qwen_layer76
451	    - scout_layer24
452	    - scout_layer40
453	    - median_all
454	    rows:
455	    - - zero-shot
456	      - 0
457	      - 0.771
458	      - 0.714
459	      - 0.756
460	      - 0.698
461	      - 0.735
462	    - - mean-shift
463	      - 0
464	      - 0.771
465	      - 0.714
466	      - 0.756
467	      - 0.698
468	      - 0.735
469	    - - CaCLR_alpha_only
470	      - 0 (parallel inputs)
471	      - 0.798
472	      - 0.762
473	      - 0.784
474	      - 0.745
475	      - 0.772
476	    - - CaCLR_full
477	      - 0 (parallel inputs)
478	      - 0.828
479	      - 0.788
480	      - 0.812
481	      - 0.771
482	      - 0.8
483	    - - linear_proj_50
484	      - 50 parallel pairs
485	      - 0.812
486	      - 0.779
487	      - 0.798
488	      - 0.758
489	      - 0.787
490	    - - fewshot_25
491	      - 25
492	      - 0.798
493	      - 0.761
494	      - 0.781
495	      - 0.741
496	      - 0.77
497	    - - fewshot_100
498	      - 100
499	      - 0.821
500	      - 0.792
501	      - 0.808
502	      - 0.778
503	      - 0.8
504	  - name: 'Table 5: β Sensitivity Sweep (Qwen3-235B, layer 56, median across 20 langs)'
505	    columns:
506	    - beta
507	    - delta_auroc_over_alpha_only
508	    - delta_ece_over_alpha_only
509	    - note
510	    rows:
511	    - - 0.001
512	      - 0.008
513	      - -0.003
514	      - negligible distributional constraint
515	    - - 0.01
516	      - 0.019
517	      - -0.008
518	      - marginal improvement
519	    - - 0.1
520	      - 0.032
521	      - -0.014
522	      - optimal — balances alignment and prediction
523	    - - 1.0
524	      - 0.021
525	      - -0.011
526	      - over-regularized — MMD dominates loss
527	  figures_description:
528	  - 'Fig 3a: Bar chart — 5 transfer methods × 2 models at optimal transfer layer.
529	    CaCLR_full highest, followed by fewshot_100, linear_proj, CaCLR_alpha_only, zero-shot.
530	    Error bars = bootstrap 95% CI.'
531	  - 'Fig 3b: β sweep curve — x-axis β (log scale), y-axis ΔAUROC over α-only. Inverted-U
532	    shape peaking at β=0.1. Three lines for shallow/mid/deep layers showing mid-depth
533	    benefits most.'
534	  - 'Fig 3c: Pareto frontier shift — original ZS frontier (dashed) vs CaCLR frontier
535	    (solid) for both architectures. CaCLR pushes frontier up and right, especially
536	    at mid-depth.'
537	  analysis: 'CaCLR的consistency loss在mid-depth层效果最好，这与CKA分析（plan_011）一致： mid-depth层的cross-lingual表征相似度足够高让MMD有效对齐，但已经有enough
538	    language-specific分化使得对齐产生实际收益。β=0.1的inverted-U曲线说明 distributional matching存在sweet
539	    spot——太弱无效，太强则牺牲correctness prediction。 CaCLR vs fewshot_100的near-parity（-0.8pp）是重要结果：CaCLR达到了接近
540	    100-label supervised的性能，但不需要任何target-language correctness labels。 统计显著性（p=0.003,
541	    d=0.48）确保β效应不是噪声。
542	
543	    '
544	- name: Difficulty-Controlled Decomposition Ablation
545	  plan_id: plan_004
546	  description: 'IRT difficulty probes → project out difficulty → retrain correctness
547	    probes → evaluate transfer. 10 languages × 8 layers × 2 models.
548	
549	    '
550	  expected_results:
551	    decomposition_transfer_delta_after_difficulty_removal_median: 0.031
552	    decomposition_transfer_delta_range:
553	    - 0.011
554	    - 0.052
555	    difficulty_probe_r2_median: 0.68
556	    difficulty_direction_cosine_with_correctness: 0.34
557	    capability_specific_transfer_degradation_per_depth:
558	      shallow_20pct: 0.008
559	      mid_50pct: 0.024
560	      deep_80pct: 0.048
561	    random_direction_control_delta: 0.002
562	    resource_tier_pattern:
563	      HIGH_delta: 0.022
564	      MID_delta: 0.033
565	      LOW_delta: 0.041
566	    bootstrap_ci_decomposition_delta:
567	    - 0.018
568	    - 0.044
569	    paired_permutation_p: 0.006
570	    cohens_d: 0.41
571	  result_rationale: 'Difficulty direction与correctness direction有中等cosine（0.34），说明两者共享
572	    部分信号但不完全重叠。Project out difficulty后，残差中的correctness信号更 "capability-pure"——这个信号在高资源语言间更容易transfer（+2.2pp），
573	    因为capability-specific failures在这些语言间更一致。低资源语言获益最大（+4.1pp）， 因为原始correctness方向中difficulty成分占比更高（低资源语言的difficulty分布
574	    与EN差异更大），去除difficulty后暴露出更可transfer的capability信号。 深层退化更明显（4.8pp）因为深层同时编码了更多language-specific的difficulty信息。
575	    Random-direction control仅+0.2pp，排除了dimensionality reduction artifact—— 是difficulty方向的specific
576	    removal而非arbitrary降维带来的改善。 这个分解是prescriptive的：它告诉我们哪些language-layer组合需要capability
577	    alignment （高delta = 高difficulty entanglement = 需要CaCLR/projection）。
578	
579	    '
580	  tables:
581	  - name: 'Table 6: Decomposition Effect by Resource Tier and Depth (ΔAUROC after
582	      difficulty removal)'
583	    columns:
584	    - depth_pct
585	    - HIGH_avg
586	    - MID_avg
587	    - LOW_avg
588	    - random_control
589	    rows:
590	    - - 20
591	      - 0.012
592	      - 0.014
593	      - 0.019
594	      - 0.001
595	    - - 35
596	      - 0.016
597	      - 0.022
598	      - 0.028
599	      - 0.002
600	    - - 50
601	      - 0.021
602	      - 0.031
603	      - 0.038
604	      - 0.002
605	    - - 60
606	      - 0.024
607	      - 0.036
608	      - 0.043
609	      - 0.003
610	    - - 70
611	      - 0.026
612	      - 0.039
613	      - 0.046
614	      - 0.002
615	    - - 80
616	      - 0.028
617	      - 0.041
618	      - 0.048
619	      - 0.003
620	    - - 85
621	      - 0.025
622	      - 0.038
623	      - 0.044
624	      - 0.002
625	    - - 90
626	      - 0.022
627	      - 0.034
628	      - 0.041
629	      - 0.002
630	  figures_description:
631	  - 'Fig 4a: Three-panel heatmap (HIGH/MID/LOW) — 8 layers × decomposition delta.
632	    Gradient intensifies with depth and decreases with resource level.'
633	  - 'Fig 4b: Scatter plot — difficulty-correctness cosine similarity vs decomposition
634	    delta. Each point = language × layer. Clear positive correlation (r=0.71).'
635	  - 'Fig 4c: Bar chart — decomposition delta vs random-direction control delta at
636	    each depth. Orders of magnitude difference confirms specificity.'
637	  analysis: 'Decomposition结果支持Claim 2：difficulty和capability在correctness方向中可分离， 且分离后capability-specific信号的cross-lingual
638	    transfer一致改善。 关键insight是resource tier gradient——低资源语言的difficulty entanglement最严重，
639	    也从decomposition中获益最多。这为CaCLR提供了theoretical motivation： CaCLR的consistency loss本质上在做distributional
640	    alignment of capability-specific signals。 Random-direction control（~0pp）是关键的methodological
641	    guard rail。
642	
643	    '
644	- name: Cross-Lingual Orthogonality Analysis
645	  plan_id: plan_005
646	  description: 'Correctness-confidence cosine similarity across 20 languages × 2 architectures,
647	    analyzed by resource tier and language family.
648	
649	    '
650	  expected_results:
651	    orthogonality_cosine_mean_across_langs: 0.042
652	    orthogonality_cosine_max_across_langs: 0.062
653	    orthogonality_cosine_min_across_langs: 0.018
654	    orthogonality_cosine_std: 0.013
655	    cosine_by_tier:
656	      HIGH_mean: 0.038
657	      MID_mean: 0.043
658	      LOW_mean: 0.051
659	    cosine_by_architecture:
660	      qwen_mean: 0.039
661	      scout_mean: 0.046
662	    cosine_range_qwen_20lang:
663	    - 0.018
664	    - 0.058
665	    cosine_range_scout_20lang:
666	    - 0.022
667	    - 0.062
668	    all_20_langs_below_0p08: true
669	    bootstrap_ci_mean_cosine:
670	    - 0.035
671	    - 0.049
672	  result_rationale: 'Orthogonality在所有20语言 × 2架构上持续存在（max cosine 0.062 < 0.08阈值）， 确认Miao
673	    & Ungar (2026)的English-only发现是universal structural property。 Low-resource语言cosine略高（0.051
674	    vs HIGH 0.038），因为这些语言的confidence probe quality更低（更少训练数据→confidence方向估计噪声更大→与correctness的
675	    apparent cosine被噪声inflate）。但即使是最高的0.062也远低于non-orthogonal阈值， 说明output-based calibration在结构上受限不依赖于语言。
676	    Qwen略比Scout更orthogonal（0.039 vs 0.046），可能反映Qwen更大的模型容量 使correctness和confidence能被编码在更分离的子空间中。
677	    这个发现bounds entire output-based calibration approach：无论语言或架构， verbalized confidence不包含correctness信息，motivating
678	    probe-based方法。
679	
680	    '
681	  tables:
682	  - name: 'Table 7: Correctness-Confidence Cosine Similarity by Language'
683	    columns:
684	    - language
685	    - tier
686	    - qwen_cosine
687	    - scout_cosine
688	    - mean
689	    rows:
690	    - - en
691	      - HIGH
692	      - 0.031
693	      - 0.037
694	      - 0.034
695	    - - zh
696	      - HIGH
697	      - 0.035
698	      - 0.041
699	      - 0.038
700	    - - es
701	      - HIGH
702	      - 0.033
703	      - 0.039
704	      - 0.036
705	    - - fr
706	      - HIGH
707	      - 0.034
708	      - 0.04
709	      - 0.037
710	    - - de
711	      - HIGH
712	      - 0.036
713	      - 0.042
714	      - 0.039
715	    - - hi
716	      - MID
717	      - 0.039
718	      - 0.045
719	      - 0.042
720	    - - ru
721	      - MID
722	      - 0.037
723	      - 0.043
724	      - 0.04
725	    - - ko
726	      - MID
727	      - 0.041
728	      - 0.047
729	      - 0.044
730	    - - tr
731	      - MID
732	      - 0.043
733	      - 0.049
734	      - 0.046
735	    - - sw
736	      - LOW
737	      - 0.048
738	      - 0.056
739	      - 0.052
740	    - - bn
741	      - LOW
742	      - 0.052
743	      - 0.058
744	      - 0.055
745	  figures_description:
746	  - 'Fig 5: Dot plot — cosine similarity per language, sorted by resource tier. Horizontal
747	    line at 0.08 threshold. All points below. Color by architecture (Qwen blue, Scout
748	    orange). Visible tier gradient.'
749	  analysis: 'Cross-lingual orthogonality的universal persistence是论文的bounding contribution。
750	    它回答了"为什么需要probe-based calibration"：因为output-based方法在结构上 无法获取correctness信息（cosine<0.08），无论语言。Resource
751	    tier gradient 是nuanced finding但不影响main conclusion。
752	
753	    '
754	- name: Probe Complexity Comparison
755	  plan_id: plan_006
756	  description: 'Logistic regression vs 2-layer MLP across all probed layers, both
757	    models. EN accuracy, cross-lingual transfer degradation, calibration comparison.
758	
759	    '
760	  expected_results:
761	    lr_en_best_auroc_qwen: 0.838
762	    mlp_en_best_auroc_qwen: 0.852
763	    lr_en_best_auroc_scout: 0.821
764	    mlp_en_best_auroc_scout: 0.834
765	    lr_zs_transfer_degradation_median: 0.068
766	    mlp_zs_transfer_degradation_median: 0.104
767	    lr_transfer_advantage_over_mlp_median: 0.022
768	    lr_ece_vs_mlp_ece:
769	    - -0.008
770	    - 0.003
771	    mlp_overfit_indicator_deep_layers: true
772	  result_rationale: 'Linear probes在EN AUROC上略输MLP（~1.4pp），但在cross-lingual transfer上
773	    显著更好（+2.2pp median）。MLP的额外容量捕获了EN-specific patterns导致更多 overfitting to source
774	    language——这些patterns在target语言中不泛化。 这与probe complexity literature一致（Hewitt & Liang
775	    2019）：更强的probe 在source domain表现更好但generalization更差。Linear probe的inductive bias
776	    （只能学习线性可分方向）恰好与correctness direction的线性结构匹配， 同时限制了对language-specific artifacts的拟合。
777	    在deep层这个差异更大（MLP overfitting更严重），因为deep层表征更language-specific。 这个结果support使用logistic
778	    regression作为primary probe的选择。
779	
780	    '
781	  tables:
782	  - name: 'Table 8: Probe Complexity — EN AUROC vs ZS Transfer (Qwen3-235B, selected
783	      layers)'
784	    columns:
785	    - layer
786	    - lr_en
787	    - mlp_en
788	    - lr_zs_median
789	    - mlp_zs_median
790	    - lr_transfer_advantage
791	    rows:
792	    - - 24
793	      - 0.711
794	      - 0.722
795	      - 0.698
796	      - 0.691
797	      - 0.007
798	    - - 40
799	      - 0.762
800	      - 0.778
801	      - 0.756
802	      - 0.741
803	      - 0.015
804	    - - 56
805	      - 0.798
806	      - 0.814
807	      - 0.771
808	      - 0.752
809	      - 0.019
810	    - - 76
811	      - 0.838
812	      - 0.852
813	      - 0.714
814	      - 0.686
815	      - 0.028
816	  figures_description:
817	  - 'Fig S1: Dual-axis plot — EN AUROC (solid) and ZS transfer AUROC (dashed) vs layer
818	    depth, separate lines for LR and MLP. MLP''s solid line higher but dashed line
819	    lower, scissors gap widens at deep layers.'
820	  analysis: 'Linear probe是正确的default choice。MLP的EN优势被transfer劣势完全抵消。 这个结果also间接支持correctness
821	    direction是线性的——linear probe已经捕获了 大部分信号，MLP额外捕获的主要是noise/language-specific artifact。
822	
823	    '
824	- name: Additional Benchmark Evaluation (Belebele + MMLU-ProX)
825	  plan_id: plan_007
826	  description: 'Best probes + CaCLR在Belebele和MMLU-ProX上的评估，验证beyond-GlobalMMLU泛化。
827	
828	    '
829	  expected_results:
830	    belebele_zs_auroc_median: 0.731
831	    belebele_caclr_auroc_median: 0.789
832	    mmlu_prox_zs_auroc_median: 0.748
833	    mmlu_prox_caclr_auroc_median: 0.801
834	    cross_benchmark_correlation: 0.92
835	    belebele_pareto_rho_median: -0.71
836	    mmlu_prox_pareto_rho_median: -0.75
837	  result_rationale: 'Belebele（reading comprehension）的ZS AUROC略低于GlobalMMLU（0.731 vs
838	    0.758）， 因为不同任务的correctness信号分布不完全一致——但Pareto frontier仍然存在 （rho=-0.71），说明depth-transfer
839	    tradeoff是task-general的。 MMLU-ProX与GlobalMMLU最相似（同为knowledge QA），所以结果最接近（0.748
840	    vs 0.758）。 CaCLR在两个benchmark上都提供了consistent improvement（+5.3-5.8pp）， 说明CaCLR学到的alignment不是GlobalMMLU-specific的。
841	    Cross-benchmark correlation 0.92表明per-language transfer difficulty在benchmarks间高度一致——
842	    sw/bn在所有benchmarks上都最难transfer，zh/es在所有benchmarks上都最容易。
843	
844	    '
845	  tables:
846	  - name: 'Table 9: Cross-Benchmark Generalization (Qwen3-235B, optimal transfer layer)'
847	    columns:
848	    - benchmark
849	    - zs_median
850	    - caclr_median
851	    - pareto_rho
852	    - langs_above_0p65
853	    rows:
854	    - - GlobalMMLU
855	      - 0.758
856	      - 0.808
857	      - -0.78
858	      - 17
859	    - - Belebele
860	      - 0.731
861	      - 0.789
862	      - -0.71
863	      - 15
864	    - - MMLU-ProX
865	      - 0.748
866	      - 0.801
867	      - -0.75
868	      - 16
869	  figures_description:
870	  - 'Fig S2: Scatter — per-language ZS AUROC on GlobalMMLU vs Belebele. High correlation
871	    (r=0.92). Each point labeled with language code.'
872	  analysis: 'Cross-benchmark泛化confirm findings are not benchmark-specific artifact。
873	    Pareto frontier在三个benchmark上一致存在但shape有细微差异—— Belebele更浅的optimal depth可能反映reading
874	    comprehension使用了更浅层的表征。
875	
876	    '
877	- name: INT8 Validation Ablation
878	  plan_id: plan_010
879	  description: 'INT8 vs FP16对比，Llama 4 Scout，5 representative layers，5% random subset。
880	
881	    '
882	  expected_results:
883	    int8_fp16_auroc_max_diff: 0.006
884	    int8_fp16_auroc_mean_diff: 0.003
885	    int8_fp16_ece_max_diff: 0.008
886	    int8_fp16_direction_cosine_min: 0.987
887	    all_diffs_within_noise: true
888	  result_rationale: 'INT8量化对correctness direction的影响极小（max AUROC差异0.6pp）， 因为correctness信号是高SNR的线性方向——量化噪声主要影响低幅度维度，
889	    而correctness direction在high-variance维度上有强projection。 Direction cosine>0.987说明INT8和FP16下提取的correctness方向几乎相同。
890	    ECE差异稍大（0.8pp）因为calibration对probability scale更敏感，但仍在噪声范围内。 这排除了"INT8 artifact"的reviewer
891	    concern。
892	
893	    '
894	  tables:
895	  - name: 'Table S1: INT8 vs FP16 Comparison (Llama 4 Scout)'
896	    columns:
897	    - layer
898	    - int8_auroc
899	    - fp16_auroc
900	    - diff
901	    - direction_cosine
902	    rows:
903	    - - 8
904	      - 0.674
905	      - 0.678
906	      - -0.004
907	      - 0.991
908	    - - 16
909	      - 0.741
910	      - 0.745
911	      - -0.004
912	      - 0.989
913	    - - 24
914	      - 0.788
915	      - 0.791
916	      - -0.003
917	      - 0.992
918	    - - 32
919	      - 0.811
920	      - 0.814
921	      - -0.003
922	      - 0.99
923	    - - 40
924	      - 0.821
925	      - 0.827
926	      - -0.006
927	      - 0.987
928	  figures_description:
929	  - 'Fig S3: Bland-Altman plot — mean of INT8/FP16 AUROC (x) vs difference (y). All
930	    points within ±0.01 band. No systematic bias.'
931	  analysis: 'INT8量化不distort correctness signals。所有差异在bootstrap noise范围内。 Deep层差异略大（layer
932	    40: 0.6pp）符合预期——深层表征更complex，量化误差累积更多。 但0.6pp远小于实验效应（CaCLR +6pp），不影响任何结论。
933	
934	    '
935	- name: CKA Cross-Lingual Representation Similarity
936	  plan_id: plan_011
937	  description: 'CKA (linear kernel) between EN and each target language at every probed
938	    layer, correlated with transfer AUROC. Mechanistic explanation for Pareto frontier.
939	
940	    '
941	  expected_results:
942	    cka_transfer_pearson_r: 0.82
943	    cka_transfer_pearson_r_ci:
944	    - 0.76
945	    - 0.87
946	    cka_transfer_spearman_rho: 0.79
947	    cka_en_zh_by_depth_trend: monotonically decreasing from 0.92 (shallow) to 0.61
948	      (deep)
949	    cka_en_sw_by_depth_trend: monotonically decreasing from 0.84 (shallow) to 0.38
950	      (deep)
951	    cka_resource_tier_gradient:
952	      HIGH_mean_cka_at_optimal_depth: 0.78
953	      MID_mean_cka_at_optimal_depth: 0.71
954	      LOW_mean_cka_at_optimal_depth: 0.58
955	    geometric_misalignment_evidence: 'CKA drop from mid to deep layers exceeds what
956	      mean/covariance shift alone predicts. Subspace angle analysis shows correctness
957	      direction rotates 15-35° across languages at deep layers vs 5-12° at shallow
958	      layers.
959	
960	      '
961	    cka_explains_caclr_beta_limit: 'At layers where CKA < 0.55, β term provides diminishing
962	      returns because geometric misalignment (rotation) dominates distributional shift.
963	
964	      '
965	  result_rationale: 'CKA与transfer AUROC的高相关（r=0.82）提供了Pareto frontier的mechanistic
966	    explanation： cross-lingual表征相似度随depth monotonically下降，直接导致deep层transfer degradation。
967	    这不是trivial的"深层更specific"——CKA量化了具体的相似度数值并与transfer成功率 建立了定量关系。High-resource语言在所有depth保持更高CKA（因为pretraining
968	    data overlap）， 解释了resource tier gradient。 关键insight：deep层的CKA下降不仅是distributional
969	    shift（可被MMD修正）， 还包含geometric misalignment（correctness方向在语言间旋转15-35°）。 这解释了CaCLR
970	    β term在deep层效果减弱——MMD对齐分布但不学习旋转， 而linear projection学习旋转所以在deep层更稳定。 Subspace angle
971	    analysis区分了distributional vs geometric misalignment， 为Path A narrative提供了theoretical
972	    depth：CaCLR works at mid-depth因为 那里的misalignment主要是distributional的。
973	
974	    '
975	  tables:
976	  - name: 'Table 10: CKA by Depth and Resource Tier (Qwen3-235B)'
977	    columns:
978	    - depth_pct
979	    - HIGH_cka
980	    - MID_cka
981	    - LOW_cka
982	    - zs_auroc_median
983	    rows:
984	    - - 10
985	      - 0.93
986	      - 0.89
987	      - 0.84
988	      - 0.618
989	    - - 25
990	      - 0.9
991	      - 0.85
992	      - 0.78
993	      - 0.698
994	    - - 40
995	      - 0.86
996	      - 0.79
997	      - 0.69
998	      - 0.756
999	    - - 50
1000	      - 0.82
1001	      - 0.74
1002	      - 0.62
1003	      - 0.771
1004	    - - 60
1005	      - 0.78
1006	      - 0.69
1007	      - 0.55
1008	      - 0.771
1009	    - - 70
1010	      - 0.73
1011	      - 0.63
1012	      - 0.47
1013	      - 0.741
1014	    - - 80
1015	      - 0.67
1016	      - 0.56
1017	      - 0.41
1018	      - 0.714
1019	    - - 90
1020	      - 0.61
1021	      - 0.49
1022	      - 0.35
1023	      - 0.688
1024	  figures_description:
1025	  - 'Fig 6a: Dual-axis — CKA (left y-axis, lines by tier) and ZS AUROC median (right
1026	    y-axis, dashed) vs normalized depth. CKA decrease tracks AUROC decrease after
1027	    elbow.'
1028	  - 'Fig 6b: Scatter — CKA vs ZS transfer AUROC, each point = language × layer. Strong
1029	    linear relationship (r=0.82). Color by resource tier.'
1030	  - 'Fig 6c: Subspace angle between EN and target correctness directions vs depth.
1031	    Angles increase with depth; LOW languages diverge faster.'
1032	  analysis: 'CKA analysis是论文的mechanistic backbone。它将observation（Pareto frontier） 与explanation（representation
1033	    geometry变化）和method（CaCLR的作用机制与局限） 连接起来。CKA<0.55作为CaCLR β有效性的threshold是一个actionable
1034	    finding—— 实践者可以用CKA预测CaCLR在哪些layer-language组合上有效。 Geometric vs distributional
1035	    misalignment的区分是theoretical contribution： 它解释了为什么distributional matching（MMD/CaCLR）在mid-depth有效但在deep层递减，
1036	    而geometric alignment（linear projection）在deep层更稳定。
1037	
1038	    '
1039	- name: Linear Projection Sensitivity Analysis
1040	  plan_id: plan_012
1041	  description: 'Linear projection pair count sweep (10, 20, 50, 100, 200). Both models
1042	    × 5 layers × 20 languages.
1043	
1044	    '
1045	  expected_results:
1046	    linear_proj_min_pairs_for_saturation: 35
1047	    saturation_criterion: 95% of 200-pair performance
1048	    pairs_sweep:
1049	      10:
1050	        median_auroc: 0.762
1051	        pct_of_200: 0.88
1052	      20:
1053	        median_auroc: 0.778
1054	        pct_of_200: 0.94
1055	      50:
1056	        median_auroc: 0.792
1057	        pct_of_200: 0.98
1058	      100:
1059	        median_auroc: 0.796
1060	        pct_of_200: 0.99
1061	      200:
1062	        median_auroc: 0.798
1063	        pct_of_200: 1.0
1064	    low_resource_saturation_later: true
1065	    low_resource_min_pairs: 48
1066	    high_resource_min_pairs: 22
1067	  result_rationale: 'Linear projection在~35 pairs时达到饱和（95% of 200-pair performance），
1068	    因为correctness方向是低维线性结构——学习一个旋转/缩放矩阵不需要很多样本。 10 pairs已经达到88%性能，说明即使极少数据也能捕获主要的geometric
1069	    transformation。 50 pairs后几乎无改善（98%→100%），符合线性映射的low sample complexity理论。 Low-resource语言需要slightly
1070	    more pairs（48 vs 22），因为表征空间中 correctness方向的SNR更低，需要更多样本来robustly估计映射。 整体saturation在20-50范围内，support
1071	    "≤50 parallel pairs suffice"的claim。 这建立了linear projection作为practical baseline的地位——
1072	    50 pairs在任何语言都容易获得（e.g., 翻译50个MCQA items）。
1073	
1074	    '
1075	  tables:
1076	  - name: 'Table 11: Linear Projection Data Efficiency (median across 20 langs × 2
1077	      models)'
1078	    columns:
1079	    - n_pairs
1080	    - median_auroc
1081	    - delta_vs_zs
1082	    - pct_of_200pair
1083	    - HIGH_auroc
1084	    - LOW_auroc
1085	    rows:
1086	    - - 10
1087	      - 0.762
1088	      - 0.027
1089	      - 88
1090	      - 0.781
1091	      - 0.638
1092	    - - 20
1093	      - 0.778
1094	      - 0.043
1095	      - 94
1096	      - 0.798
1097	      - 0.651
1098	    - - 50
1099	      - 0.792
1100	      - 0.057
1101	      - 98
1102	      - 0.814
1103	      - 0.664
1104	    - - 100
1105	      - 0.796
1106	      - 0.061
1107	      - 99
1108	      - 0.818
1109	      - 0.668
1110	    - - 200
1111	      - 0.798
1112	      - 0.063
1113	      - 100
1114	      - 0.821
1115	      - 0.671
1116	  figures_description:
1117	  - 'Fig S4: Learning curve — n_pairs (x, log) vs median AUROC (y). Rapid rise, plateau
1118	    at ~50. Separate lines for HIGH/MID/LOW tiers — all plateau but at different levels.'
1119	  analysis: 'Linear projection的data efficiency confirms它作为practical baseline的价值。 50
1120	    pairs的saturation point意味着任何有minimal translation capacity的语言 都可以使用这个方法。这也为CaCLR设定了benchmark：CaCLR需要beat
1121	    50-pair projection 才能justify its additional complexity（in best tier, CaCLR beats
1122	    by +1.4pp median）。
1123	
1124	    '
1125	- name: Probing Control Tasks (Hewitt & Liang 2019)
1126	  plan_id: plan_013
1127	  description: 'Random-label control probes at each layer. Selectivity = probe AUROC
1128	    - control AUROC. Validates genuine correctness signal.
1129	
1130	    '
1131	  expected_results:
1132	    control_task_auroc_range:
1133	    - 0.502
1134	    - 0.538
1135	    selectivity_median: 0.284
1136	    selectivity_min: 0.192
1137	    selectivity_max: 0.341
1138	    control_task_selectivity_min_across_langs: 0.192
1139	    selectivity_by_depth:
1140	      shallow: 0.218
1141	      mid: 0.294
1142	      deep: 0.312
1143	    selectivity_by_tier:
1144	      HIGH: 0.301
1145	      MID: 0.278
1146	      LOW: 0.234
1147	  result_rationale: 'Control probe AUROC在0.50-0.54范围（near chance），selectivity中位数0.284
1148	    远超15pp minimum threshold（min=19.2pp）。这confirm probe AUROC反映 genuine correctness
1149	    direction而非memorized artifacts或probe capacity。 Selectivity随depth增加（0.218→0.312），因为深层表征包含更丰富的correctness
1150	    信号而control仍在chance附近——深层probe的高AUROC不是因为probe容量过大。 Low-resource语言selectivity最低（0.234）但仍远超threshold，
1151	    说明即使低资源语言的correctness信号也是genuine的（不是noise fitting）。 这直接回应Hewitt & Liang probing
1152	    methodology critique—— 我们的probes确实在提取linguistic property而非exploiting high-dimensional
1153	    capacity。
1154	
1155	    '
1156	  tables:
1157	  - name: 'Table S2: Control Task Selectivity (Qwen3-235B, selected layers × languages)'
1158	    columns:
1159	    - layer
1160	    - en_selectivity
1161	    - zh_selectivity
1162	    - sw_selectivity
1163	    - control_auroc
1164	    rows:
1165	    - - 16
1166	      - 0.248
1167	      - 0.231
1168	      - 0.192
1169	      - 0.512
1170	    - - 32
1171	      - 0.281
1172	      - 0.268
1173	      - 0.218
1174	      - 0.519
1175	    - - 48
1176	      - 0.309
1177	      - 0.292
1178	      - 0.241
1179	      - 0.524
1180	    - - 56
1181	      - 0.318
1182	      - 0.301
1183	      - 0.248
1184	      - 0.521
1185	    - - 76
1186	      - 0.341
1187	      - 0.324
1188	      - 0.262
1189	      - 0.538
1190	  figures_description:
1191	  - 'Fig S5: Paired bar chart — probe AUROC (dark) vs control AUROC (light) at each
1192	    layer. Gap (selectivity) clearly visible and widening with depth. Horizontal line
1193	    at 15pp threshold.'
1194	  analysis: 'Control task validation是methodological necessity。Selectivity最小值19.2pp
1195	    大幅超过15pp阈值，即使在最challenging的条件（low-resource × shallow layer） 也确认probe是在提取genuine
1196	    signal。这让reviewer对所有downstream结果 （Pareto frontier, CaCLR, decomposition）更有信心。
1197	
1198	    '
1199	- name: Gemma 4 31B Dense — Camera-Ready Extension
1200	  plan_id: plan_008
1201	  description: 'Third architecture (dense, FP16), full Pareto frontier. Dense vs MoE
1202	    contrast for camera-ready.
1203	
1204	    '
1205	  expected_results:
1206	    en_best_auroc: 0.809
1207	    en_best_layer: 48
1208	    optimal_transfer_layer: 36
1209	    zs_transfer_auroc_median: 0.738
1210	    pareto_rho_median: -0.69
1211	    pareto_shape: smoother frontier than MoE models — no sharp elbow
1212	    dense_vs_moe_key_finding: 'Dense architecture shows shallower Pareto slope — transfer
1213	      degrades more gradually with depth compared to MoE models. Consistent with hypothesis
1214	      that expert routing accelerates language specialization.
1215	
1216	      '
1217	  result_rationale: 'Gemma 4 31B Dense作为dense对照提供了architectural contrast。 EN AUROC
1218	    0.809低于两个MoE模型（0.838, 0.821），反映31B dense参数<235B MoE active参数。 关键发现：dense架构的Pareto
1219	    frontier更平滑（rho=-0.69 vs MoE -0.73/-0.78）， 没有MoE的sharp elbow。这是因为MoE的expert routing在深层创造了discrete
1220	    language specialization（某些experts "负责"特定语言），而dense模型的specialization是gradual的。
1221	    这是architecture-dependent Pareto shape claim的strongest evidence。 Optimal transfer在75%深度（layer
1222	    36/48），比Qwen3浅（60%）但比Scout深（50%）， 提供了第三个data point来characterize architecture-depth
1223	    relationship。
1224	
1225	    '
1226	  tables:
1227	  - name: 'Table S3: Three-Architecture Comparison Summary'
1228	    columns:
1229	    - model
1230	    - type
1231	    - params
1232	    - layers
1233	    - en_best_auroc
1234	    - zs_median
1235	    - optimal_transfer_pct
1236	    - pareto_rho
1237	    rows:
1238	    - - Qwen3-235B-A22B
1239	      - MoE
1240	      - 235B
1241	      - 94
1242	      - 0.838
1243	      - 0.758
1244	      - 60
1245	      - -0.78
1246	    - - Llama 4 Scout
1247	      - MoE
1248	      - 109B (17B active)
1249	      - 48
1250	      - 0.821
1251	      - 0.742
1252	      - 50
1253	      - -0.73
1254	    - - Gemma 4 31B Dense
1255	      - Dense
1256	      - 31B
1257	      - 60
1258	      - 0.809
1259	      - 0.738
1260	      - 75
1261	      - -0.69
1262	  figures_description:
1263	  - 'Fig S6: Three Pareto frontiers overlaid on normalized depth axis. MoE models
1264	    show sharper elbows; Dense model is smoother. Annotated with optimal transfer
1265	    depth for each.'
1266	  analysis: 'Three-architecture comparison is the crown jewel of Claim 1。 Dense vs
1267	    MoE对比provides causal insight into WHY frontiers differ—— expert routing is the
1268	    mechanism driving sharp language specialization at depth.
1269	
1270	    '
1271	- name: Extended Language Coverage — Camera-Ready
1272	  plan_id: plan_009
1273	  description: 'Expand from 20 to 50+ languages. Camera-ready extension using GlobalMMLU/Belebele
1274	    full sets.
1275	
1276	    '
1277	  expected_results:
1278	    total_languages: 52
1279	    zs_langs_above_0p65: 38
1280	    zs_auroc_median_52lang: 0.721
1281	    new_low_resource_findings: 'Several additional low-resource languages (e.g., Yoruba,
1282	      Hausa, Malagasy) show ZS AUROC 0.58-0.64, confirming resource-tier gradient
1283	      extends to tail.
1284	
1285	      '
1286	    pareto_frontier_robust: true
1287	    caclr_generalizes: true
1288	    caclr_delta_over_zs_52lang_median: 0.058
1289	  result_rationale: '52语言验证confirms所有findings at broader scale。ZS median从20 langs的0.758
1290	    降到52 langs的0.721，因为新增语言主要是低资源的——这是expected的composition effect。 38/52 > 0.65（73%）vs
1291	    17/20（85%），比例下降也反映低资源语言的加入。 Pareto frontier和CaCLR在所有语言上consistent，说明findings是language-general的。
1292	    Key new finding：Yoruba/Hausa等sub-Saharan African语言的ZS AUROC（0.58-0.62） 与sw/bn相当，但CaCLR对这些语言的improvement更大（+7-9pp），
1293	    可能因为GlobalMMLU translations provide parallel data that partially bridges the representation
1294	    gap for these extremely low-resource languages.
1295	
1296	    '
1297	  tables:
1298	  - name: 'Table S4: Extended Language Coverage Summary'
1299	    columns:
1300	    - resource_tier
1301	    - n_langs
1302	    - zs_auroc_median
1303	    - caclr_median
1304	    - delta
1305	    rows:
1306	    - - HIGH
1307	      - 12
1308	      - 0.786
1309	      - 0.828
1310	      - 0.042
1311	    - - MID
1312	      - 18
1313	      - 0.741
1314	      - 0.798
1315	      - 0.057
1316	    - - LOW
1317	      - 22
1318	      - 0.648
1319	      - 0.721
1320	      - 0.073
1321	  figures_description:
1322	  - 'Fig S7: World map — ZS AUROC by country/language, color gradient from red (low)
1323	    to green (high). Clear geographic pattern tracking resource availability.'
1324	  analysis: Extended coverage是camera-ready的scale argument。核心findings在52语言上robust。
1325	    Low-resource语言从CaCLR获益最多（+7.3pp vs HIGH +4.2pp）， because these languages have
1326	    the most room for improvement and CaCLR's distributional alignment compensates
1327	    for sparse pretraining representation.
1328	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21e97dd3-1a7a-41c2-b3c0-db71236a925c",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "8b8578e2-6b89-4297-9dce-da8a825cd091",
  "sourceToolAssistantUUID": "21e97dd3-1a7a-41c2-b3c0-db71236a925c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T21:13:15.393Z_

Now let me also check the earlier review reports and the review issues for additional context on what was flagged before.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b8578e2-6b89-4297-9dce-da8a825cd091",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWaW3adsWZDKeA6DuUc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1db245f5-9876-48aa-877e-29380dced45b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017UWyWDdfNwDFmvRhBgPXps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38838,
      "cache_read_input_tokens": 47930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 38838,
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

_source line 39 · 2026-05-20T21:13:17.250Z_

<details open><summary>🔧 Tool call — Read · `toolu_016726XSCciQvBTB9BiNJ7uu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/review_reports/round_0.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1db245f5-9876-48aa-877e-29380dced45b",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWaW3adsWZDKeA6DuUc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec485771-7dfc-4070-a75d-d8e42a6fba50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017UWyWDdfNwDFmvRhBgPXps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38838,
      "cache_read_input_tokens": 47930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 38838,
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

_source line 40 · 2026-05-20T21:13:17.261Z_

<details><summary>↩ Tool result · `toolu_016726XSCciQvBTB9BiNJ7uu`</summary>

```text
1	---
2	round: 0
3	review_mode: 
4	overall_score: weak reject
5	timestamp: 2026-05-20T20:03:28.106110+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 审稿报告 — Round 1
12	
13	**论文**: Cross-Lingual Calibration Probes Reveal Architecture-Dependent Pareto Frontiers in Multilingual LLMs
14	**目标 Venue**: ACL Rolling Review
15	**审稿模式**: 圆桌会议（2 Reviewers, 1 轮 + 交叉分享）
16	**日期**: 2026-05-20
17	
18	---
19	
20	## Panel Summary
21	
22	| Reviewer | Focus | Initial | Post-discussion | Confidence |
23	|----------|-------|---------|-----------------|------------|
24	| R1 | Methods & Experiments | 3.0/5 (Findings) | 3.0/5 (Findings) | 4/5 |
25	| R2 | Novelty & Related Work | 2.5/5 (Revise) | 2.0/5 (Revise) | 4/5 |
26	| **Consensus** | | | **2.5/5 (Weak Reject)** | |
27	
28	**Overall Assessment**: Weak Reject — 论文存在系统性可信度问题（Abstract 核心数字不可验证、参考文献疑似虚构/严重误引），叠加完全缺乏统计检验和可视化，即使实验规模值得肯定，当前状态不达 main conference 门槛。Findings track 需要先解决 soundness 问题。
29	
30	---
31	
32	## 1. Summary
33	
34	本文研究跨语言 correctness probe transfer for calibration，在 20 语言 × 3 架构（Qwen3-235B, Llama 4 Scout, Gemma 4 31B）× 3 基准上系统评估。提出四项贡献：(1) depth-transferability Pareto frontier，最优迁移深度 ~58-60%；(2) difficulty-capability decomposition 分离迁移差异来源；(3) CaCLR 训练方法在 zero-correctness-label 条件下提升迁移性能；(4) correctness-confidence orthogonality 跨语言验证。
35	
36	---
37	
38	## 2. Strengths
39	
40	- **S1 [Consensus]**: 实验规模在同类工作中领先——20 语言 × 3 架构 × 3 基准的覆盖度超过 Xiao et al. (5 语言) 和 Civelli et al. 的范围，全部 10 个实验计划均有对应结果。
41	- **S2 [Consensus]**: 问题选择好——跨语言 correctness probe transfer 是有实际意义且尚未被系统研究的方向。
42	- **S3 [Consensus]**: 三架构 best-transfer depth 收敛至 58-60%（Table 14），跨 Dense 和 MoE 架构一致，是有价值的 empirical finding。
43	- **S4 [R1]**: CaCLR 的 ablation（Table 8）设计清楚，展示了 L_consistency (+4.1pp AUROC) 和 L_SB-ECE (ECE 0.078→0.061) 的各自贡献及 synergy。
44	- **S5 [R2]**: MoE vs Dense 的 frontier 形状比较和 resource-tier gradient 在 orthogonality 上的发现是先行文献中未见的观察。
45	- **S6 [R1]**: Pareto frontier 框架将 depth-transferability tradeoff 形式化为多目标优化问题，是有启发性的分析视角。
46	
47	---
48	
49	## 3. Weaknesses
50	
51	### 3.1 Critical Issues（必须修复，影响接收决定）
52	
53	**C1. Abstract 核心数字不可验证——系统性可信度问题** [Consensus: R1 raised, R2 endorsed]
54	
55	两个 Abstract-level 核心 claim 均无法从论文数据验证：
56	
57	(a) **72% vs 81%**: Abstract 声称 "predicts method choice with 72% accuracy"，但 §5.2 报告 "81% prescriptive accuracy"。72% 极可能混淆自 IRT 的 h²=0.72（explained variance ratio），这与 accuracy（分类准确率）是完全不同的指标。
58	
59	(b) **"Explains 25% of transfer gap"**: Table 5 显示 difficulty-shared component 的 Share of Transfer Degradation 为 13%（非 25%），capability-specific 为 87%。无论取哪个角度（13%, 31.6%, 68.4%）均推不出 25%。正文 §5.2 也未出现此数字。
60	
61	**影响**: 两个 headline claim 的数字自相矛盾或无来源，形成令人担忧的 pattern——reviewer 无法信任论文中其他未经独立验证的数字。
62	
63	**C2. 参考文献严重不足且存在元数据错误/疑似虚构** [Consensus]
64	
65	(a) **数量**: 全文仅 8 条引用。一篇覆盖 probing、calibration、IRT、cross-lingual transfer 的论文通常需要 30-50 条。缺失大量关键文献：
66	- Cross-lingual probing: Conneau et al. (2020), Pires et al. (2019)
67	- Probing survey: Belinkov (2022)
68	- 表征相似性: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017)
69	- Multilingual calibration: Keleg & Magdy (2023), Adaptive Temperature Scaling (EMNLP 2024)
70	- IRT 基础文献: Lord (1980), Baker (2001)
71	- 直接相关方法: CCPS (Wang et al.), MKA (Chen et al. 2024)
72	
73	(b) **准确性**: R1 通过 web search 核查发现多条引用元数据不匹配：
74	- Miao et al. (2026a) "CORAL": 论文写 "Shuo Miao"，ICML 2026 实际第一作者为 Miranda Muqing Miao；标题也不匹配
75	- Zhou et al. (2024) "LACE": 实际论文发表于 2025，标题和年份均不匹配
76	- Civelli et al. (2025): 标题与最接近的实际论文不匹配
77	
78	**R2 补充**: 如果核心参考文献是虚构的或严重误引的，novelty 论证（"我们是第一个做 X 而不是 Y/Z 的"）完全不可信。**可能构成 ethical concern（疑似 fabricated citations）。**
79	
80	**C3. 完全缺乏统计检验和方差估计** [Consensus: R1 raised, R2 endorsed]
81	
82	Tables 1-16 全部为单次实验点估计，无 CI、SD、bootstrap significance test 或多次 random seed。CaCLR vs linear projection 的核心优势仅 ~3.4pp AUROC，在无统计检验的情况下无法判断是否 significant。对于 probe 训练（随机初始化敏感）、Pareto frontier 判定（对 noise 敏感），统计不确定性可能改变结论。
83	
84	**C4. Pareto frontier 缺乏形式化验证** [Divergence: R2 says inaccurate, R1 says acceptable but unformalized]
85	
86	- **R2 立场**: 论文描述的是 trade-off curve 而非 Pareto frontier；deeper = more language-specific 是已知现象（Pires 2019, Conneau 2020），"Pareto frontier" 给已知现象披上新包装。
87	- **R1 立场**: Table 1 中 ★ 层确实满足二维 (EN AUROC, ZS-19 AUROC) 空间中的 non-dominance 定义，术语本身不算误用。但论文未执行形式化 Pareto dominance 检验，未报告 hypervolume indicator，未画 scatter plot。
88	- **共识**: 无论术语是否可接受，论文缺乏形式化验证（dominance test + hypervolume + visualization）使得核心 framing 不够rigorous。
89	
90	**C5. 四项贡献的新颖性为增量性** [R2 raised, R1 partially agreed]
91	
92	- **Claim 1 (Pareto frontier)**: 将已知的 depth-language specificity 趋势量化为 Pareto frontier 有增量价值，但跨架构差异小（58-60%），"architecture-dependent" framing 过强。
93	- **Claim 2 (Decomposition)**: 建立在 Civelli et al. (2025) 之上，R²=0.72 未超越其结果。且核心数字（25%）不可验证。
94	- **Claim 3 (CaCLR)**: **R1/R2 分歧点**——R1 认为 Table 8 ablation 显示 L_consistency 和 L_SB-ECE 有 synergy，组合非平凡；R2 认为三个已知 loss 组件的拼装缺乏理论分析。共识：需补充理论分析说明为何组合优于单独使用。
95	- **Claim 4 (Orthogonality)**: 方法论上直接复制 Miao & Ungar (2026) 到 20 种语言，贡献仅在 empirical verification。
96	
97	### 3.2 Should-Fix Issues（影响评分但不一票否决）
98	
99	**W1. CaCLR "zero-label" 表述误导性** [Consensus]
100	- ℓ_consistency 需要 English-target parallel activations（§3.4），与 linear projection 的资源需求本质相同。"Zero-label" 掩盖了对 parallel data 的依赖——获取 20 种语言的 parallel data 可能比标注 25-100 个 correctness labels 更昂贵。应改为 "zero-correctness-label"。
101	
102	**W2. 全文 16 张表格、0 张图** [Consensus]
103	- 一篇以 "Pareto Frontier" 为标题的论文没有任何 scatter plot 来可视化 frontier shape，在 presentation 上不可接受。至少需要：(1) Pareto scatter plot (2) layer-wise AUROC 折线图 (3) CaCLR ablation bar chart。
104	
105	**W3. Related Work 仅 ~15 行** [Consensus]
106	- 三个子方向各仅 1-2 句话。与 Xiao/Civelli/CORAL 的区别各一句带过——这些是 novelty 论证的核心，不够。应扩至 1.5-2 页，附对比表格。
107	
108	**W4. "First systematic study" 声明过强** [Consensus]
109	- 鉴于 Civelli、Xiao、Zhou 先行工作，"first" 仅在 "correctness probe" 细分品类成立。建议改为 "first large-scale study comparing correctness probe transfer across architectures"。
110	
111	**W5. CaCLR 超参数无 sensitivity analysis** [Consensus]
112	- α=0.15, β=0.10 仅说 "tuned on validation set"，搜索范围和 sensitivity 均未报告。Validation set 的语言组成也未说明。
113	
114	**W6. INT8 验证范围过窄** [Consensus]
115	- 仅 Llama 4 Scout 单架构 5% 子集。若声称 quantization-robust 应至少跨 2 个架构。
116	
117	**W7. Very low resource tier 仅 4 种语言** [Consensus]
118	- CaCLR 在该 tier pass rate 仅 50%（2/4），n=4 的统计结论不可靠。
119	
120	**W8. Probe 训练细节缺失** [Consensus]
121	- 训练样本量、train/test split、cross-validation 策略、logistic regression 正则化参数均未报告。
122	
123	**W9. CaCLR 实际优势有限** [R2]
124	- CaCLR vs linear projection 仅 +3.4pp，且两者资源需求相同（均需 parallel data）。缺少 cost-benefit 分析说明在什么场景下 CaCLR 比 few-shot fine-tuning 更有价值。
125	
126	---
127	
128	## 4. Reviewer Consensus [AGREE]
129	
130	以下问题双方完全一致：
131	
132	1. **参考文献不足且有误**是最严重的问题——8 条引用（含多条元数据错误）对 ACL venue 不可接受
133	2. **Abstract 两个核心数字（72%, 25%）均不可验证**——形成系统性可信度隐患
134	3. **完全无统计检验**——3.4pp 的核心改进幅度无法判断 significance
135	4. **无任何 figure**——presentation 严重不足
136	5. **CaCLR "zero-label" 表述误导**——实需 parallel data
137	6. **Probe 训练、超参数细节缺失**——reproducibility 不足
138	
139	---
140	
141	## 5. Reviewer Divergence [REBUT]
142	
143	**5.1 Pareto frontier 术语的准确性**
144	- R1: 术语本身在技术上可接受（Table 1 的 ★ 层满足 non-dominance），但缺乏形式化验证和可视化
145	- R2: 术语不准确，实际是 trade-off curve；且 deeper = more language-specific 是已知现象
146	- **Director 判断**: 术语的使用在边界线上——可以保留但必须补充形式化验证（dominance test, hypervolume, scatter plot）
147	
148	**5.2 CaCLR 的新颖性程度**
149	- R1: 组合有非平凡性，Table 8 ablation 显示 synergistic interaction
150	- R2: 三个已知 loss 组件的组合不构成方法论贡献
151	- **Director 判断**: Ablation 支撑了组件间的 synergy，但缺乏理论分析解释 why。在 Findings track 这个贡献水平可接受，main conference 不足。
152	
153	**5.3 Overall 评分**
154	- R1: 3.0 (Findings)——问题选择好、规模合理，但 soundness 问题过多
155	- R2: 2.0 (Revise)——交叉审阅后因 Abstract 数值问题和引用可信度担忧下调
156	
157	---
158	
159	## 6. Questions for Authors
160	
161	1. Abstract "72% accuracy" 与 §5.2 "81% prescriptive accuracy" 分别度量什么？72% 是否来自 h²=0.72？
162	2. "Explains 25% of the transfer gap" 的推导路径？Table 5 中 difficulty-shared 的 Share% 为 13%，不是 25%。
163	3. CaCLR ℓ_consistency 的 parallel activations 来源？与 linear projection 同样需要 parallel data，CaCLR 的实际资源优势在哪？
164	4. Miao et al. (2026a) 引为 "Shuo Miao"——与 ICML 2026 CORAL 论文的 Miranda Muqing Miao 是否同一人？Zhou et al. (2024) 实际年份和标题？Civelli et al. (2025) 实际标题？
165	5. IRT difficulty 参数是从英语数据单独估计的吗？跨语言 decomposition 的 validity？
166	6. Probe 训练样本量、train/test split、CV 策略、logistic regression 正则化参数？
167	7. 为什么没有任何 figure？是否有 appendix？
168	8. MoE expert routing 是否影响 layer-wise probing 的解释？论文未讨论 "layer depth" 在 MoE 中的特殊性。
169	9. Table 14 三种架构 Depth% 分别为 60%, 58%, 60%——"architecture-dependent" 的表述是否过强？
170	
171	---
172	
173	## 7. Missing References
174	
175	以下引用在论文讨论范围内但完全缺失（按重要性排序）：
176	
177	1. Conneau et al. (2020) "Unsupervised Cross-lingual Representation Learning at Scale" — 多语言模型 layer-wise probing 奠基工作
178	2. Pires et al. (2019) "How multilingual is Multilingual BERT?" — deeper layers = more language-specific 的原始观察
179	3. Belinkov (2022) "Probing Classifiers" — probing 领域标准综述
180	4. Lord (1980) / Baker (2001) — IRT 基础文献，§3.3 大量使用 IRT 却未引用原始来源
181	5. Kornblith et al. (2019) CKA / Raghu et al. (2017) SVCCA — 表征相似性度量
182	6. Keleg & Magdy (2023) "On the Calibration of Massively Multilingual Language Models" — 多语言 calibration 直接相关
183	7. Guo et al. (2017) — temperature scaling 原始文献
184	8. Wang et al. (EMNLP 2025) CCPS — perturbation stability calibration probing
185	9. Chen et al. (2024) MKA — 直接相关方法
186	10. Domain adaptation baselines: DANN, Deep CORAL, DAN — CaCLR consistency loss 的 structural equivalent
187	
188	---
189	
190	## 8. External Review (Stanford Agentic Reviewer)
191	
192	**状态: pending（已请求，尚未返回）**
193	
194	外部审稿已于 2026-05-20 请求提交，8 小时内自动提醒。内部审稿不因此延迟。外部结果到达后将补充到 Group C。
195	
196	---
197	
198	## 9. Visual Layout Check（非评分项）
199	
200	**状态: not_started**
201	
202	视觉审查未能派发（review_paper_pdf_path 未配置）。已知论文无任何 figure，排版审查价值有限。建议作者添加可视化后重新触发。
203	
204	---
205	
206	## 10. Overall Assessment
207	
208	**评分: 2.5/5 — Weak Reject (Revise for next cycle)**
209	
210	**置信度: 4/5**
211	
212	本文选题好（跨语言 correctness probe transfer 值得研究）、实验规模领先（20 语言 × 3 架构 × 3 基准），Pareto frontier 框架有分析价值。但当前版本存在以下不可接受的问题：
213	
214	1. **可信度危机**: Abstract 两个核心数字（72%, 25%）均无法从正文数据验证；多条参考文献的作者名/标题/年份与实际出版物不匹配，R2 提出疑似 fabricated citations 的 ethical concern
215	2. **方法论不严谨**: 完全无统计检验；Pareto frontier 缺乏形式化验证；CaCLR "zero-label" 表述掩盖 parallel data 依赖
216	3. **学术规范不足**: 仅 8 条引用；Related Work ~15 行；无任何 figure；probe 训练细节缺失
217	4. **新颖性有限**: 四项贡献中两项为直接复制扩展（Claims 2, 4），一项为已知现象的量化（Claim 1），仅 CaCLR（Claim 3）有一定方法论贡献但受 parallel data 需求和有限改进幅度削弱
218	
219	**修改建议优先级**:
220	1. [紧急] 核查并修正所有 Abstract 数字；逐条验证每条引用的元数据
221	2. [紧急] 扩展引用至 30+ 篇，Related Work 扩至 1.5-2 页
222	3. [紧急] 添加统计检验（5 seeds × bootstrap）
223	4. [重要] 添加 2-3 个核心 figure（Pareto scatter plot 为首）
224	5. [重要] Pareto frontier 形式化验证（dominance test + hypervolume）
225	6. [重要] CaCLR parallel data 需求透明化
226	7. [建议] 更诚实定位为 large-scale empirical study + one practical method
227	
228	---
229	
230	## 11. Detailed Comments
231	
232	### §1 Introduction
233	- "First systematic study" 需加限定语（见 W4）
234	- 四项 Claim 的因果链叙事（discovery → analysis → method → mechanism）结构好，但每项的新颖性需更诚实定位
235	
236	### §2 Related Work
237	- 严重不足。三个子方向各 1-2 句话不够支撑 novelty 论证
238	- 缺少与 Xiao/Civelli/CORAL 的详细对比表格
239	
240	### §3 Methods
241	- §3.2 Pareto frontier 定义需形式化（dominance criterion）
242	- §3.3 IRT difficulty 使用需引用原始 IRT 文献
243	- §3.4 CaCLR: α, β 的 validation set 语言组成未报告；"zero-label" 应改为 "zero-correctness-label"
244	
245	### §4 Experimental Setup
246	- 缺少 probe 训练样本量、split、CV、正则化参数
247	- INT8 quantization 选择的 justification 应更充分
248	
249	### §5 Results
250	- §5.1: Table 1 ★ 标注标准未说明；需 scatter plot
251	- §5.2: 72% vs 81% 矛盾必须修复；25% 需给出推导路径或删除
252	- §5.3: CaCLR vs linear proj 的 3.4pp 需统计检验
253	- §5.4: Orthogonality 分析方法与 Miao & Ungar 一致需明确说明
254	- §5.5: Probe complexity 仅在 Qwen3 上做，应跨架构
255	- §5.8: Very low resource tier n=4 过小
256	- §5.9: INT8 验证应跨架构
257	
258	### §6 Discussion
259	- "First-order distributional mismatch but not nonlinear feature interactions" 作为 CaCLR 局限性缺乏实验支撑
260	
261	### References
262	- 仅 8 条，多条元数据不匹配。格式不一致（部分有 venue、部分没有）。需全面重写。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec485771-7dfc-4070-a75d-d8e42a6fba50",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "64eb7ec4-738d-42bb-92b5-dabbfbce451c",
  "sourceToolAssistantUUID": "ec485771-7dfc-4070-a75d-d8e42a6fba50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T21:13:17.541Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KUfDVZ7EuiDZKrs9sF7j5B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64eb7ec4-738d-42bb-92b5-dabbfbce451c",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWaW3adsWZDKeA6DuUc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00babdc6-b87a-49b4-9ba4-caf82adbcaf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017UWyWDdfNwDFmvRhBgPXps",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38838,
      "cache_read_input_tokens": 47930,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 38838
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 47930,
          "cache_creation_input_tokens": 38838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 38838,
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

_source line 42 · 2026-05-20T21:13:17.544Z_

<details><summary>↩ Tool result · `toolu_01KUfDVZ7EuiDZKrs9sF7j5B`</summary>

```text
1	issues:
2	- id: "R1-N3+R2-N1"
3	  summary: "参考文献严重不足（仅8篇）且多条引用元数据错误/疑似虚构"
4	  category: writing
5	  severity: critical
6	  status: open
7	  first_raised_round: 1
8	  last_seen_round: 1
9	  mentions:
10	    - round: 1
11	      reviewers: [1, 2]
12	      note: "R1通过web search发现Miao et al.作者名/标题不匹配、Zhou et al.年份/标题不匹配、Civelli et al.标题不匹配。R2列出7+个缺失文献领域。交叉审阅后双方一致认定critical，R2提出疑似fabricated citations的ethical concern。"
13	  action_items:
14	    - round: 1
15	      action: "扩展引用至30+篇；逐条核查所有现有引用的作者名、标题、年份、venue"
16	      assigned_to: author
17	      status: open
18	  resolution: ""
19	  resolution_round: null
20	
21	- id: "R1-N1"
22	  summary: "Abstract 72% vs 正文§5.2 81%数值矛盾——疑为h²=0.72与prescriptive accuracy混淆"
23	  category: method
24	  severity: critical
25	  status: open
26	  first_raised_round: 1
27	  last_seen_round: 1
28	  mentions:
29	    - round: 1
30	      reviewers: [1, 2]
31	      note: "R1首次发现，R2交叉审阅时确认并补充：h²(variance explained)与accuracy(分类准确率)是完全不同指标。双方一致critical。"
32	  action_items:
33	    - round: 1
34	      action: "统一数字并明确72%和81%分别度量什么；修正Abstract"
35	      assigned_to: author
36	      status: open
37	  resolution: ""
38	  resolution_round: null
39	
40	- id: "R1-N2"
41	  summary: "Abstract 'explains 25% of transfer gap'在正文和Table 5中无推导路径"
42	  category: method
43	  severity: critical
44	  status: open
45	  first_raised_round: 1
46	  last_seen_round: 1
47	  mentions:
48	    - round: 1
49	      reviewers: [1, 2]
50	      note: "R1首次发现Table 5的Share%为13%/87%，推不出25%。R2交叉审阅确认并将自己初审的W4升级为critical。连同R1-N1，Abstract中两个核心数字均不可验证。"
51	  action_items:
52	    - round: 1
53	      action: "删除或修正25%，给出明确推导路径"
54	      assigned_to: author
55	      status: open
56	  resolution: ""
57	  resolution_round: null
58	
59	- id: "R1-N4"
60	  summary: "全文Tables 1-16均为单次实验点估计，完全缺乏统计检验和方差估计"
61	  category: experiment
62	  severity: critical
63	  status: open
64	  first_raised_round: 1
65	  last_seen_round: 1
66	  mentions:
67	    - round: 1
68	      reviewers: [1, 2]
69	      note: "R1首次提出（critical），R2交叉审阅同意升级。CaCLR vs baseline仅~3.4pp差距，无统计检验无法判断significance。"
70	  action_items:
71	    - round: 1
72	      action: "至少5次random seed报告均值±SD；CaCLR vs baselines做paired bootstrap test"
73	      assigned_to: author
74	      status: open
75	  resolution: ""
76	  resolution_round: null
77	
78	- id: "R2-N2"
79	  summary: "Pareto frontier术语缺乏形式化验证（无dominance检验、hypervolume、scatter plot）"
80	  category: framing
81	  severity: critical
82	  status: open
83	  first_raised_round: 1
84	  last_seen_round: 1
85	  mentions:
86	    - round: 1
87	      reviewers: [1, 2]
88	      note: "R2认为术语不准确（trade-off curve非Pareto frontier）。R1部分反驳：Table 1的★层确实满足non-dominance定义，术语本身可接受，但缺乏形式化验证和可视化。共识：需添加dominance检验+scatter plot+hypervolume指标。"
89	  action_items:
90	    - round: 1
91	      action: "明确Pareto dominance判定标准；添加scatter plot；报告hypervolume或ε-dominance"
92	      assigned_to: author
93	      status: open
94	  resolution: ""
95	  resolution_round: null
96	
97	- id: "R2-N3"
98	  summary: "四项贡献的新颖性均为增量性，缺乏方法论突破"
99	  category: framing
100	  severity: critical
101	  status: open
102	  first_raised_round: 1
103	  last_seen_round: 1
104	  mentions:
105	    - round: 1
106	      reviewers: [1, 2]
107	      note: "R2提出四项Claim逐条分析：C1重新包装已知现象、C2建立在Civelli之上、C3已知loss组合、C4方法论复制。R1部分同意：C3的CaCLR组合有一定非平凡性（Table 8 ablation支撑），C2/C4确实增量。分歧在CaCLR新颖性程度。"
108	  action_items:
109	    - round: 1
110	      action: "聚焦最有洞察力的发现；补充理论分析说明CaCLR组件synergy；更诚实定位为large-scale empirical study"
111	      assigned_to: author
112	      status: open
113	  resolution: ""
114	  resolution_round: null
115	
116	- id: "R1-W1+R2-Q2"
117	  summary: "CaCLR 'zero-label'表述误导性——实需parallel data，与linear projection资源需求本质相同"
118	  category: method
119	  severity: warning
120	  status: open
121	  first_raised_round: 1
122	  last_seen_round: 1
123	  mentions:
124	    - round: 1
125	      reviewers: [1, 2]
126	      note: "双方一致：ℓ_consistency需English-target parallel activations，获取parallel data可能比标注25-100个labels更昂贵。建议改为'zero-correctness-label'。"
127	  action_items:
128	    - round: 1
129	      action: "改为'zero-correctness-label'并明确讨论parallel data需求及限制"
130	      assigned_to: author
131	      status: open
132	  resolution: ""
133	  resolution_round: null
134	
135	- id: "R1-W4+R2-W2"
136	  summary: "全文16张表格、0张图——Pareto frontier论文无scatter plot，可读性差"
137	  category: writing
138	  severity: warning
139	  status: open
140	  first_raised_round: 1
141	  last_seen_round: 1
142	  mentions:
143	    - round: 1
144	      reviewers: [1, 2]
145	      note: "双方强烈一致。建议至少添加Pareto scatter plot、layer-wise AUROC折线图、CaCLR ablation bar chart。"
146	  action_items:
147	    - round: 1
148	      action: "添加2-3个核心figure（Pareto scatter plot、decomposition可视化、CaCLR对比）"
149	      assigned_to: author
150	      status: open
151	  resolution: ""
152	  resolution_round: null
153	
154	- id: "R2-W1"
155	  summary: "Related Work仅~15行，三个子方向各仅1-2句话"
156	  category: writing
157	  severity: warning
158	  status: open
159	  first_raised_round: 1
160	  last_seen_round: 1
161	  mentions:
162	    - round: 1
163	      reviewers: [1, 2]
164	      note: "R2提出，R1交叉审阅同意。应扩展至1.5-2页，用对比表格区分本文与Xiao/Civelli/CORAL。"
165	  action_items:
166	    - round: 1
167	      action: "扩展Related Work至1.5-2页；添加method×feature对比表格"
168	      assigned_to: author
169	      status: open
170	  resolution: ""
171	  resolution_round: null
172	
173	- id: "R2-W3"
174	  summary: "'First systematic study'声明过强"
175	  category: framing
176	  severity: warning
177	  status: open
178	  first_raised_round: 1
179	  last_seen_round: 1
180	  mentions:
181	    - round: 1
182	      reviewers: [1, 2]
183	      note: "鉴于Civelli/Xiao/Zhou先行工作，'first'仅成立于correctness probe细分品类。R1交叉审阅同意。"
184	  action_items:
185	    - round: 1
186	      action: "改为'first large-scale study comparing correctness probe transfer across architectures'"
187	      assigned_to: author
188	      status: open
189	  resolution: ""
190	  resolution_round: null
191	
192	- id: "R1-W2"
193	  summary: "CaCLR超参数(α,β)无sensitivity analysis"
194	  category: experiment
195	  severity: warning
196	  status: open
197	  first_raised_round: 1
198	  last_seen_round: 1
199	  mentions:
200	    - round: 1
201	      reviewers: [1, 2]
202	      note: "R1提出，R2交叉同意核心观点（并修正R1引用的β值：实际为0.10非0.08）。validation set语言组成也未报告。"
203	  action_items:
204	    - round: 1
205	      action: "添加α,β sensitivity plot或报告多组值下的性能"
206	      assigned_to: author
207	      status: open
208	  resolution: ""
209	  resolution_round: null
210	
211	- id: "R1-W3"
212	  summary: "INT8验证仅Llama 4 Scout单架构5%子集，范围过窄"
213	  category: experiment
214	  severity: warning
215	  status: open
216	  first_raised_round: 1
217	  last_seen_round: 1
218	  mentions:
219	    - round: 1
220	      reviewers: [1, 2]
221	      note: "双方一致。若声称quantization-robust应至少跨2个架构验证。"
222	  action_items:
223	    - round: 1
224	      action: "增加至少一个架构的INT8验证"
225	      assigned_to: author
226	      status: open
227	  resolution: ""
228	  resolution_round: null
229	
230	- id: "R1-W5"
231	  summary: "Very low resource tier仅4种语言，n=4统计结论不可靠"
232	  category: experiment
233	  severity: warning
234	  status: open
235	  first_raised_round: 1
236	  last_seen_round: 1
237	  mentions:
238	    - round: 1
239	      reviewers: [1, 2]
240	      note: "CaCLR在该tier >0.60 pass rate仅50%（2/4），样本量不足。R2补充同意。"
241	  action_items:
242	    - round: 1
243	      action: "增加very low resource语言数量或标注为preliminary observation"
244	      assigned_to: author
245	      status: open
246	  resolution: ""
247	  resolution_round: null
248	
249	- id: "R1-W6"
250	  summary: "Probe训练细节缺失——样本量、split、CV策略、正则化参数均未报告"
251	  category: experiment
252	  severity: warning
253	  status: open
254	  first_raised_round: 1
255	  last_seen_round: 1
256	  mentions:
257	    - round: 1
258	      reviewers: [1, 2]
259	      note: "双方一致。§3.1和§4均未报告关键训练配置。"
260	  action_items:
261	    - round: 1
262	      action: "在§4或appendix补充完整训练配置"
263	      assigned_to: author
264	      status: open
265	  resolution: ""
266	  resolution_round: null
267	
268	- id: "R2-W5"
269	  summary: "CaCLR改进幅度有限（+3.4pp over linear proj），实际意义需讨论"
270	  category: method
271	  severity: warning
272	  status: open
273	  first_raised_round: 1
274	  last_seen_round: 1
275	  mentions:
276	    - round: 1
277	      reviewers: [2]
278	      note: "R2初审提出（写+1.3pp但R1修正为+3.4pp）。few-shot(100)获取成本低，CaCLR需parallel data，cost-benefit未讨论。"
279	  action_items:
280	    - round: 1
281	      action: "补充cost-benefit分析，说明zero-label假设的实际适用场景"
282	      assigned_to: author
283	      status: open
284	  resolution: ""
285	  resolution_round: null
286	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00babdc6-b87a-49b4-9ba4-caf82adbcaf1",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "77d9343a-acfc-49ce-9cb9-b98c955d8f04",
  "sourceToolAssistantUUID": "00babdc6-b87a-49b4-9ba4-caf82adbcaf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T21:13:22.505Z_

Now I have a comprehensive understanding of the paper, its experimental context, the actual MVP results, the "dreamed" (imagined) experimental results, and the previous review round. Let me also check the key discrepancy between the paper summary provided in my task description and the actual dream paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77d9343a-acfc-49ce-9cb9-b98c955d8f04",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWb2dbLFYLcEcRo2Rsk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf94b0cb-6d69-4106-bce2-2da0caeb591f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaARbuQJbf5yYcG6dvGeDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11105,
      "cache_read_input_tokens": 86768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11105,
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

_source line 44 · 2026-05-20T21:13:24.931Z_

<details open><summary>🔧 Tool call — Read · `toolu_0149SM7RvYLMCG569FXreToK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf94b0cb-6d69-4106-bce2-2da0caeb591f",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWb2dbLFYLcEcRo2Rsk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f38fdad2-c937-4b2c-9b71-a66a7f63da7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaARbuQJbf5yYcG6dvGeDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11105,
      "cache_read_input_tokens": 86768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11105,
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

_source line 45 · 2026-05-20T21:13:24.937Z_

<details><summary>↩ Tool result · `toolu_0149SM7RvYLMCG569FXreToK`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{colortbl}
12	\usepackage{array}
13	\usepackage{tabularx}
14	\usepackage{enumitem}
15	\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}
16	\usepackage{natbib}
17	\bibliographystyle{plainnat}
18	
19	\definecolor{improved}{rgb}{0.85,0.95,0.85}
20	\definecolor{degraded}{rgb}{0.95,0.85,0.85}
21	
22	\title{Cross-Lingual Correctness Probes Reveal a Depth--Transferability\\Pareto Frontier: Distributional Matching Fails\\Where Linear Projection Succeeds}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	Probe-based calibration methods extract internal correctness signals from LLM representations, achieving strong results in English. Whether these signals transfer cross-lingually remains untested. We present the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B), 20+ languages, and 5 transfer methods. We discover a \emph{depth--transferability Pareto frontier}: deeper layers yield higher English calibration quality (AUROC up to 0.81) but degrade in cross-lingual zero-shot transfer (median Spearman $\rho = -0.52$ between English AUROC and transfer AUROC). CKA analysis reveals the mechanism---geometric misalignment between language subspaces increases with depth ($r = 0.58$ between CKA similarity and transfer AUROC, explaining 34\% of variance). We test CaCLR, a probe training objective augmenting BCE loss with MMD-based cross-lingual consistency, and show that the consistency term is \emph{inert} across three orders of magnitude ($\beta$ sweep: Cohen's $d = 0.08$, $p = 0.42$)---predicted by the geometric explanation, since MMD cannot correct representational rotations. In contrast, linear projection with as few as 50--100 parallel pairs achieves +3.5\,pp AUROC over zero-shot transfer, precisely because it learns the rotation that distributional matching cannot. Correctness--confidence orthogonality (cosine $< 0.10$) persists across all 20 languages, confirming that output-based calibration is structurally limited regardless of language. Our results establish that probe-based cross-lingual calibration is viable for the majority of languages at mid-depth layers, close the distributional-matching path with both empirical evidence and mechanistic explanation, and identify linear projection as the practical solution.
31	\end{abstract}
32	
33	%====================================================================
34	\section{Introduction}
35	\label{sec:intro}
36	
37	Large language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) degrading up to 5$\times$ compared to English \cite{ahuja2024globalmmlu,lai2024llmsurvey}. Recent work has shown that probe-based calibration---extracting internal correctness signals via linear probes on model representations---outperforms output-based methods in English \cite{miao2026coral,burns2023discovering}. A key finding by \citet{miao2026orthogonality} is that correctness and verbalized confidence directions are nearly orthogonal (cosine $< 0.04$) in English, establishing a structural limitation of output-based approaches. However, all existing probe-based calibration methods operate exclusively in English, leaving a fundamental question unanswered: \emph{do these internal correctness signals transfer across languages?}
38	
39	The answer is not obvious. Cross-lingual representation transfer has been studied extensively for tasks like NER and classification \cite{pires2019multilingual,conneau2020unsupervised}, but correctness probes target a fundamentally different signal---output-dependent accuracy rather than input-level features. \citet{xiao2025knowledgeboundary} transferred \emph{knowledge boundary} probes (input-level answerability) across 8 languages, but answerability and correctness are distinct signals with potentially different cross-lingual alignment properties.
40	
41	We present the first systematic evaluation of cross-lingual correctness probe transfer, contributing four findings organized as a causal chain:
42	
43	\paragraph{(1) Pareto Frontier.} We discover a depth--transferability tradeoff: deeper layers produce better English probes but transfer worse cross-lingually. The frontier shape is architecture-dependent (Spearman $\rho$ ranging from $-0.51$ to $-0.58$ across three architectures).
44	
45	\paragraph{(2) Mechanistic Explanation.} CKA analysis reveals that cross-lingual geometric similarity decreases with depth. The CKA--transfer correlation ($r = 0.58$) explains 34\% of transfer variance, substantially outpredicting distributional measures like MMD (6\%).
46	
47	\paragraph{(3) Principled Negative Result.} CaCLR, a probe training objective with MMD-based cross-lingual consistency loss, fails to shift the Pareto frontier ($d = 0.08$). This is \emph{predicted} by the geometric explanation: MMD matches marginal distributions but cannot correct the rotation of the correctness direction across language subspaces.
48	
49	\paragraph{(4) Constructive Alternative.} Linear projection with $\sim$50--100 parallel pairs achieves +3.5\,pp over zero-shot, succeeding precisely because it learns the rotation that MMD cannot. The correctness--confidence orthogonality persists across all 20 languages, confirming the structural necessity of probe-based approaches.
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f38fdad2-c937-4b2c-9b71-a66a7f63da7c",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "1ef18ee9-8ab7-4ea8-8c6d-ae0cf430ae6b",
  "sourceToolAssistantUUID": "f38fdad2-c937-4b2c-9b71-a66a7f63da7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-20T21:13:25.461Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CxtNwocr4kCRac5JyPDbVT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ef18ee9-8ab7-4ea8-8c6d-ae0cf430ae6b",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWb2dbLFYLcEcRo2Rsk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb67ac03-e3d7-48b7-b471-759bfa6aecb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaARbuQJbf5yYcG6dvGeDV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11105,
      "cache_read_input_tokens": 86768,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11105
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 268,
          "cache_read_input_tokens": 86768,
          "cache_creation_input_tokens": 11105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11105,
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

_source line 47 · 2026-05-20T21:13:25.465Z_

<details><summary>↩ Tool result · `toolu_01CxtNwocr4kCRac5JyPDbVT`</summary>

```text
1	---
2	dream_id: dream_20260520T201854
3	tier: median
4	overall_score: 4/6 — Borderline / Weak Accept
5	timestamp: 2026-05-20T21:11:12.856985+00:00
6	---
7	
8	# Dream Review Report — Cross-Lingual Correctness Probes
9	
10	**Dream ID:** 20260520T201854 | **Review Mode:** full | **Date:** 2026-05-20
11	
12	---
13	
14	## Paper Summary
15	
16	This paper presents the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B Dense), 20+ languages, and 5 transfer methods. The authors discover a depth–transferability Pareto frontier (deeper layers yield better English probes but transfer worse cross-lingually, median Spearman ρ = −0.52), provide a CKA-based mechanistic explanation (geometric misalignment increases with depth, r = 0.58, 34% variance explained vs. MMD's 6%), show that CaCLR's MMD-based consistency loss is inert (d = 0.08, p = 0.42), and demonstrate that linear projection with ~50–100 parallel pairs achieves +3.5 pp AUROC by learning the rotation MMD cannot correct. Correctness–confidence orthogonality is extended from English to 20 languages.
17	
18	---
19	
20	## Reviewer R1 — Methods & Experiments
21	
22	### Strengths
23	
24	**S1. Comprehensive experimental scope with appropriate controls.** Three architectures (two MoE, one dense), 20 languages across 4 resource tiers, 5 transfer conditions, 3 benchmarks (GlobalMMLU, Belebele, MMLU-ProX). Control tasks (Hewitt & Liang 2019), random-direction controls for decomposition, INT8 validation, and probe complexity comparison demonstrate methodological care.
25	
26	**S2. Clean mean-shift rank-invariance proof.** The mathematical proof that mean-shift produces exactly ∆AUROC ≡ 0 under StandardScaler + logistic regression is a tight, novel result that corrects implicit assumptions in prior work.
27	
28	**S3. Well-designed difficulty–capability decomposition.** IRT-based difficulty probes with random-direction controls ruling out dimensionality-reduction artifacts. The depth-dependent improvement pattern (78% at deep vs. 50% at shallow layers) coherently supports the geometric misalignment narrative.
29	
30	**S4. Strong statistical practice on key claims.** Paired permutation tests, bootstrap 95% CIs (1000 resamples), Cohen's d reported throughout. The β sweep is well-structured across 3 OOM with clear null result reporting.
31	
32	**S5. Practically valuable linear projection analysis.** The sample efficiency curve (saturation at ~70 pairs, 90% at ~55) is actionable for practitioners and well-characterized across both architectures.
33	
34	### Weaknesses
35	
36	**W1. CKA "mechanistic explanation" is correlational, not causal.** The CKA–transfer correlation (r = 0.58) is presented as explaining WHY transfer fails, but CKA and transfer AUROC are both functions of depth. Partial correlation controlling for normalized depth is not reported. Without this, the 34% variance explained may substantially reflect the shared depth variable rather than a causal geometric mechanism. This is the paper's central mechanistic claim — it needs stronger evidence.
37	
38	**W2. Architecture-dependence claim is confounded.** The three models differ simultaneously in architecture (MoE vs. dense), scale (235B vs. 48-layer vs. 31B), depth (94 vs. 48 vs. 60 layers), active parameters, and training data. Attributing differences in ρ variance (σ_ρ = 0.12 vs. 0.15–0.16) to "MoE routing" without controlling for these confounds is not justified. No expert routing analysis is provided.
39	
40	**W3. CaCLR training procedure is critically underspecified.** The MMD kernel choice (Gaussian RBF? linear?), bandwidth selection, optimizer, learning rate, and number of training epochs are not reported. For a negative result, the community needs to be confident the method was given a fair chance. Was the kernel bandwidth tuned? Was the MMD computed on raw representations or probe outputs? Equation (2) suggests probe outputs f(h), but this should be explicit.
41	
42	**W4. Selective layer presentation raises concerns.** The experimental design specifies 24 probed layers for Qwen3, but Table 1 reports summary statistics. The full 24×20 layer-language matrix is not shown in the main text. For a paper whose central claim is about layer-level tradeoffs, the reader should see the complete data (at minimum in supplementary).
43	
44	**W5. CaCLR's marginal advantage over simple baselines undermines its utility.** CaCLR-full achieves only +1.2 pp over zero-shot (not significant, p = 0.08) while requiring parallel inputs, a 3-term loss, and α/β hyperparameter tuning. Linear projection with just 50 pairs already achieves +3.0 pp. The paper correctly identifies this as a negative result, but the framing of CaCLR as a "proposed training objective" in §3.2 creates the impression it is a method contribution rather than an ablation vehicle.
45	
46	### Questions for Authors
47	
48	1. Report partial correlation between CKA and transfer AUROC controlling for normalized depth. If r drops substantially, the "mechanistic explanation" claim needs qualification.
49	2. Specify the complete CaCLR training procedure: MMD kernel, bandwidth, optimizer, learning rate, epochs, and whether MMD is computed on representations or probe outputs.
50	3. Show the full layer×language AUROC matrix (at least in appendix) rather than only summary statistics.
51	4. Did you try CaCLR with CKA-based alignment loss instead of MMD, given your own analysis shows CKA captures the relevant misalignment?
52	
53	---
54	
55	## Reviewer R2 — Novelty & Related Work
56	
57	### Strengths
58	
59	**S1. Genuine gap identification with coherent narrative.** The observation that all probe-based calibration methods are English-only is accurate and important. The four-finding causal chain structure (Pareto → CKA mechanism → CaCLR negative result → linear projection solution) is well-organized and compelling.
60	
61	**S2. Scale of evaluation is commendable.** 20 languages, 3 architectures, 3 benchmarks, 5 transfer conditions, with control tasks and INT8 validation — this is among the most thorough empirical packages in the cross-lingual calibration literature.
62	
63	**S3. Honest reporting of limitations.** The paper acknowledges low-resource probe selectivity issues (sw/bn ~10 pp), the MCQA-only scope, and the partial success rate of decomposition (65%). This intellectual honesty is appreciated.
64	
65	### Weaknesses
66	
67	**W1. The "first systematic evaluation" claim overclaims relative to prior work.** Xiao et al. (ACL 2025) already performed cross-lingual probe transfer across 8 languages with alignment methods. The distinction (knowledge boundary vs. correctness) is valid but insufficient to claim "first systematic evaluation" of cross-lingual probe transfer wholesale. The claim should be scoped to "first systematic evaluation of cross-lingual *correctness* probe transfer" with explicit acknowledgment that the experimental paradigm was established by Xiao et al.
68	
69	**W2. The Pareto frontier is a quantitative refinement of known phenomena, not a conceptual discovery.** Conneau et al. (2020) established that deeper layers encode more language-specific information. LACE (Zhou et al. 2024) showed that non-English calibration peaks at intermediate layers. Civelli et al. (2024) demonstrated architecture-dependent optimal depth for cross-lingual probes. The "Pareto frontier" framing is a useful quantitative lens, but the underlying phenomenon is well-established. The paper should position this as quantification of a known tradeoff, not as a discovery.
70	
71	**W3. Only MMD tested for distributional alignment — conclusions about "distributional matching" are overly broad.** The paper tests only MMD and then concludes "distributional matching fails." Classical domain adaptation offers alternatives: CORAL-the-method (Sun & Saenko 2016, second-order statistics), adversarial alignment (DANN, Ganin et al. 2016), optimal transport (Courty et al. 2017). Testing only MMD and generalizing to all distributional methods is an incomplete experimental design. The conclusion should be "MMD-based distributional matching fails" until other methods are tested.
72	
73	**W4. Linear projection is VecMap/MUSE applied to probe representations — limited novelty.** The paper correctly cites MUSE and VecMap but does not sufficiently acknowledge that applying linear alignment to probe representations is a straightforward domain transfer. The sample efficiency result (~50 pairs) is interesting but expected given the known low intrinsic dimensionality of correctness representations.
74	
75	**W5. Missing foundational references weaken positioning.** Key absent works:
76	- Conneau et al. (2020) on depth-dependent language specificity — directly predicts the Pareto frontier
77	- Gretton et al. (2012) for MMD — foundational paper must be cited, kernel choice must be specified
78	- Sun & Saenko (2016) CORAL-the-method, Ganin et al. (2016) DANN — relevant DA baselines that should at minimum be discussed
79	- Chi et al. (2020) on geometry of multilingual representations — relevant to CKA analysis
80	
81	**W6. Orthogonality extension from English to 20 languages is incremental.** Miao & Ungar (2026) showed cosine < 0.04 in English. This paper shows cosine < 0.10 across 20 languages. Given that the underlying hypothesis (correctness and confidence are independently encoded) has no theoretical reason to be language-specific, confirmation across languages is expected rather than surprising. The resource-tier gradient is attributed to noise, not structural difference.
82	
83	**W7. Insufficient differentiation from LACE (Zhou et al. 2024).** LACE addresses multilingual calibration via per-language layer ensembles. The paper claims CaCLR requires "zero target-language labels" while LACE needs labels, but CaCLR requires parallel inputs — also a non-trivial data requirement. No direct empirical comparison is provided.
84	
85	### Questions for Authors
86	
87	1. Can you provide a direct comparison with LACE on a shared benchmark/language set?
88	2. Why was only MMD tested? Did you consider CORAL, adversarial alignment, or optimal transport? Would CKA-based alignment loss work?
89	3. How does the Pareto frontier relate to Conneau et al. (2020) on depth-dependent language specificity? What does your quantification add?
90	4. For the orthogonality analysis, the full 20-language table (Table 8) shows only tier medians, not per-language values. Can you provide per-language cosine similarities?
91	
92	---
93	
94	## Roundtable Synthesis
95	
96	### Step 2: Cross-Sharing
97	
98	Both reviewers independently arrived at 4/6 (Weak Accept) with confidence 4/5. Agreement is strong on core strengths (scale, statistical rigor, mean-shift proof, decomposition) and on key weaknesses (CKA causality concerns, CaCLR underspecification, positioning relative to prior work).
99	
100	### Step 3: Convergence — Agreements and Disagreements
101	
102	**Agreed strengths:**
103	- Comprehensive experimental scope with 3 architectures, 20 languages, 3 benchmarks
104	- Strong statistical practice throughout (permutation tests, CIs, effect sizes)
105	- Mean-shift invariance proof is clean and novel
106	- Difficulty decomposition with random-direction control is well-designed
107	- Linear projection sample efficiency analysis is practically valuable
108	
109	**Agreed weaknesses:**
110	- CKA as "mechanistic explanation" is correlational — partial correlation controlling for depth needed
111	- CaCLR training details critically underspecified (kernel, bandwidth, optimizer)
112	- Paper would benefit from reframing as analytical/characterization contribution
113	- CaCLR tests only MMD; conclusions about "distributional matching" in general are overstated
114	
115	**R1-specific concerns (experimental):**
116	- Architecture-dependence confounded by simultaneous differences in scale/depth/data
117	- Selective layer presentation (summary stats only, not full matrices)
118	- CaCLR is marginal over simple baselines, undermining its framing as a method contribution
119	
120	**R2-specific concerns (novelty):**
121	- Overclaiming "first systematic evaluation" relative to Xiao et al. (2025)
122	- Pareto frontier quantifies known phenomenon (Conneau et al. 2020, LACE)
123	- Linear projection = VecMap applied to new domain
124	- Missing key references (Gretton et al. 2012, CORAL, DANN, Chi et al. 2020)
125	- LACE comparison absent despite being the primary multilingual calibration competitor
126	- Orthogonality extension is incremental
127	
128	### Step 4: Final Assessment
129	
130	**Overall Score: 4/6 (Borderline / Weak Accept)**
131	
132	**Confidence: 4/5**
133	
134	**Summary Assessment:**
135	
136	This paper addresses a genuine gap — no prior work has systematically tested cross-lingual transfer of *correctness* probes specifically — and provides a thorough empirical investigation at commendable scale. The experimental design is comprehensive (3 architectures, 20 languages, 3 benchmarks, 5 transfer methods, multiple controls), and statistical reporting is consistently rigorous.
137	
138	The paper's strongest contributions are analytical rather than methodological:
139	1. The mean-shift rank-invariance proof is a clean, novel result
140	2. The difficulty–capability decomposition with random-direction controls is well-designed
141	3. The CKA vs. MMD comparison as transfer predictors (34% vs. 6% variance) is informative
142	4. The linear projection sample efficiency characterization is practically valuable
143	
144	However, several concerns prevent a higher score:
145	
146	**Novelty:** The depth–transferability tradeoff quantifies a known phenomenon rather than discovering one. Linear projection is a direct application of VecMap/MUSE. The orthogonality extension is expected. The paper's novelty is primarily in the systematic scope and analytical framework, not in the individual findings.
147	
148	**Methodological gaps:** The CKA "mechanistic explanation" is correlational without controlling for depth as a confounder. CaCLR tests only MMD without comparing other domain adaptation methods (CORAL, adversarial, OT), making conclusions about "distributional matching" in general overly broad. CaCLR training details are critically underspecified for a negative result.
149	
150	**Positioning:** The paper overclaims relative to prior work (Xiao et al. 2025, LACE, Conneau et al. 2020). Missing foundational references (Gretton et al. 2012, domain adaptation baselines) weaken the related work. No direct comparison with LACE despite it being the primary multilingual calibration competitor.
151	
152	**Recommendation:** The paper is a solid empirical characterization paper that would benefit from: (1) reframing contributions to foreground analytical insights rather than method contributions; (2) reporting partial correlation for CKA controlling for depth; (3) specifying CaCLR training details fully; (4) testing at least one additional alignment method beyond MMD; (5) more careful positioning relative to prior work on depth-dependent cross-lingual transfer.
153	
154	**Scores:**
155	| Criterion | Score |
156	|-----------|-------|
157	| Soundness | 3/4 — rigorous statistics but CKA causality gap and CaCLR underspecification |
158	| Novelty | 2/4 — scope is new but individual findings are refinements of known phenomena |
159	| Significance | 3/4 — practically useful guidance; closes MMD path (but only MMD tested) |
160	| Presentation | 3/4 — well-organized causal chain; some overclaiming in framing |
161	| **Overall** | **4/6 (Borderline / Weak Accept)** |
162	
163	**Key revision requests (ranked by priority):**
164	1. Report partial CKA–transfer correlation controlling for depth
165	2. Fully specify CaCLR training procedure (kernel, bandwidth, optimizer, epochs)
166	3. Test at least one non-MMD alignment method or narrow the conclusion from "distributional matching" to "MMD-based matching"
167	4. Scope "first systematic evaluation" claim and add missing references
168	5. Show full layer×language matrices (at least in appendix)
169	6. Add direct comparison with LACE on shared benchmark
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb67ac03-e3d7-48b7-b471-759bfa6aecb3",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "44b7f7dd-f778-4dd5-859a-ec71fa41164c",
  "sourceToolAssistantUUID": "fb67ac03-e3d7-48b7-b471-759bfa6aecb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-20T21:13:31.259Z_

Now I have a thorough understanding of the full paper landscape. Let me look at one more thing -- the discrepancy between the "best" paper (Path A: CaCLR works) and the "median" paper (Path B: CaCLR fails) and how this relates to the paper summary provided in my task. The task summary appears to describe the median paper scenario (CaCLR fails). Let me now also check the decisions.yaml for additional context on which narrative was adopted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44b7f7dd-f778-4dd5-859a-ec71fa41164c",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWbcU4iP7c9w8QAcbJf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "367a06b5-d89d-4407-af80-8ba5876084be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dh5wunSPtuKcPsLxp8GnCz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6201,
      "cache_read_input_tokens": 97873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6201,
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

_source line 49 · 2026-05-20T21:13:32.492Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X4hrorchrFWeSzroUHkNic`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "367a06b5-d89d-4407-af80-8ba5876084be",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWbcU4iP7c9w8QAcbJf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a3ffbe6-c5cb-4092-a0cc-0a3334289514",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dh5wunSPtuKcPsLxp8GnCz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6201,
      "cache_read_input_tokens": 97873,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6201
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 97873,
          "cache_creation_input_tokens": 6201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6201,
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

_source line 50 · 2026-05-20T21:13:32.497Z_

<details><summary>↩ Tool result · `toolu_01X4hrorchrFWeSzroUHkNic`</summary>

```text
1	_next_id: 9
2	decisions:
3	- id: D001
4	  date: 2026-05-20 13:49 UTC
5	  summary: MVP 用 7-8B 模型验证核心假设，不直接上 235B
6	  rationale: 核心假设（correctness probe 跨语言迁移 + layer-depth 效应）在 7-8B 模型上有充分先验（Miao &
7	    Ungar、Civelli 等均用 7-8B）。若 7B 无效应则整个方向不成立。7B 仅需 1 GPU × 2-4h，快速验证后再决定是否投入 235B
8	    的大资源。
9	  related_experiments: []
10	  depends_on: []
11	- id: D002
12	  date: 2026-05-20 13:53 UTC
13	  summary: MVP 模型固定为 Qwen2.5-7B-Instruct
14	  rationale: 与正式实验 Qwen3-235B 同属 Qwen 家族，架构连续性最好。Civelli et al. 报告 Qwen3-8B 最优迁移深度为
15	    24%，可为正式实验提供直接参考。Reviewer 建议明确选一个并记录理由。
16	  related_experiments: []
17	  depends_on: []
18	- id: D003
19	  date: 2026-05-20 18:25 UTC
20	  summary: P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/5 语言
21	  rationale: Mean-shift 是常数偏移，不改变 AUROC（rank-invariant）。Mean-shift 的设计目的是改善 calibration（概率准确性），应用
22	    ECE/Brier 衡量。同时 P1 ECE 阈值维持 0.15 但允许 temperature scaling 后重测。
23	  related_experiments:
24	  - exp_id: mvp_001
25	    role: trigger
26	    result: P4 ΔAUROC=0 暴露标准设计缺陷
27	  depends_on: []
28	- id: D004
29	  date: 2026-05-20 18:52 UTC
30	  summary: 'MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段'
31	  rationale: P1(AUROC=0.754+ECE=0.074 temp-scaled) / P2(4/5语言迁移) / P3(14.3pp depth
32	    effect) 全部 PASS。P4(mean-shift) FAIL 但属于 alignment baseline 方法失败，不否定核心假设。Mean-shift
33	    失败是有价值的 negative result：(1) 区分于 Xiao et al. 在 knowledge boundary 上 mean-shift
34	    成功；(2) motivate CaCLR 方法。额外发现：L27 英语最强但迁移退化 vs L24——直接观测到 Pareto tradeoff，是论文核心贡献的前兆。
35	  related_experiments:
36	  - exp_id: mvp_001
37	    role: primary
38	    result: P1✅P2✅P3✅P4❌, core hypothesis supported
39	  depends_on: []
40	- id: D005
41	  date: 2026-05-20 20:14 UTC
42	  summary: 'Dream review (3/6 weak reject) processed: 13 confirmed actions, 5 observations,
43	    3 ignores. Framing updated with conditional CaCLR narrative + 6 new reviewer concerns.
44	    3 new P1 experiments added (CKA, linproj sensitivity, control tasks). Proceeding
45	    with re-dream after changes.'
46	  rationale: 'Dream dream_20260520T185641 scored best=4/6 median=3/6 worst=3/6. Key
47	    structural issues identified across all 3 tiers: (1) no statistical tests — added
48	    as cross-cutting requirement; (2) CaCLR framing incoherent — redesigned as conditional
49	    narrative with two paths; (3) missing related work (domain adaptation theory,
50	    alignment literature, probing critiques) — added to paper_framing.md. Two-tier
51	    issues: (4) no mechanistic explanation — added plan_011 CKA analysis; (5) arbitrary
52	    AUROC threshold — added sensitivity analysis requirement; (6) probing methodology
53	    — added plan_013 control tasks. CaCLR consistency loss value is the key data-dependent
54	    risk (O3). Core 4-claim structure preserved; framing strengthened not weakened.
55	    No venue downgrade — issues are addressable via experiments and framing improvements.'
56	  related_experiments:
57	  - exp_id: plan_003
58	    role: affected
59	    result: CaCLR conditional narrative added
60	  - exp_id: plan_011
61	    role: new
62	    result: CKA mechanistic analysis (P1, 5 GPU-hrs)
63	  - exp_id: plan_012
64	    role: new
65	    result: Linear projection sensitivity (P1, 2 GPU-hrs)
66	  - exp_id: plan_013
67	    role: new
68	    result: Probing control tasks (P1, 2 GPU-hrs)
69	  depends_on:
70	  - D004
71	- id: D006
72	  date: 2026-05-20 20:23 UTC
73	  summary: 'MVP gate re-evaluation after P1 leakage fix: 2/4 PASS, still proceed to
74	    research phase'
75	  rationale: 'M005 reveals temp scaling data leakage — P1 ECE now FAIL (0.2216 > 0.15).
76	    Gate drops from 3/4 to 2/4 PASS. However, the 2 passing criteria (P2: cross-lingual
77	    transfer 4/5 langs, P3: layer depth effect 14.28pp) are the hypothesis-critical
78	    ones that validate "correctness direction exists and transfers cross-lingually."
79	    P1 ECE failure means raw probes are poorly calibrated — this is exactly the problem
80	    CaCLR is designed to solve, and actually strengthens the paper''s motivation ("probe-based
81	    calibration needs CaCLR because naive probes fail on calibration"). P4 mean-shift
82	    failure was already attributed to criteria design error (D003). Research phase
83	    continues with strengthened CaCLR motivation. The 0.15 ECE threshold for P1 was
84	    always somewhat arbitrary — discrimination (AUROC=0.754) is the primary signal
85	    that correctness information is linearly accessible.'
86	  related_experiments:
87	  - exp_id: mvp_001
88	    role: gate_check
89	    result: 2/4 PASS (P2+P3), P1 ECE FAIL after leakage fix
90	  - exp_id: plan_003
91	    role: motivated_by
92	    result: CaCLR motivation strengthened by raw probe calibration failure
93	  depends_on:
94	  - D004
95	  - D005
96	- id: D007
97	  date: 2026-05-20 20:31 UTC
98	  summary: 'mvp_003 (Llama-3.1-8B) cross-architecture validation: 3/4 PASS, Pareto
99	    architecture-dependence confirmed as core finding'
100	  rationale: 'mvp_003 gate 3/4 PASS (P1 PASS without temp scaling, P2 5/5, P3 7.85pp,
101	    P4 FAIL). Cross-architecture validation successful: correctness direction and
102	    transfer both replicate. Key finding: Pareto tradeoff is STRONG on Qwen (4/5 langs
103	    show depth-transfer degradation) but WEAK on Llama (only 2/5 — zh and sw; ar/ko
104	    improve with depth). This elevates architecture-dependence from a qualifier to
105	    a core finding in Claim 1. CKA pilot shows same two-model contrast. Swahili is
106	    model-dependent (fails Qwen, passes Llama). zh@L31 mean-shift anomaly flagged
107	    for investigation.'
108	  related_experiments:
109	  - exp_id: mvp_003
110	    role: validation
111	    result: 3/4 PASS, weak Pareto on Llama
112	  - exp_id: mvp_001
113	    role: comparison
114	    result: 2/4 PASS (post-fix), strong Pareto on Qwen
115	  depends_on:
116	  - D006
117	- id: D008
118	  date: 2026-05-20 20:40 UTC
119	  summary: 'Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4), consistent with mvp_001.
120	    P1 evaluated at best-AUROC layer.'
121	  rationale: 'Reviewer pointed out D007 ambiguity: P1 passes at L0 (AUROC=0.650, ECE=0.148)
122	    but fails at best-AUROC layer L31 (AUROC=0.728, ECE=0.205). P1 should be evaluated
123	    at the best-AUROC layer (the probe we''d actually use), where ECE fails. Both
124	    models are now 2/4 PASS (P2+P3). This is consistent and actually cleaner: discrimination
125	    (P2+P3) confirmed on both architectures, calibration (P1+P4) fails on both → strengthens
126	    CaCLR motivation uniformly. No impact on research phase decision (D006).'
127	  related_experiments:
128	  - exp_id: mvp_003
129	    role: clarification
130	    result: 2/4 PASS (P2+P3), not 3/4
131	  - exp_id: mvp_001
132	    role: comparison
133	    result: 2/4 PASS (P2+P3), consistent
134	  depends_on:
135	  - D007
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a3ffbe6-c5cb-4092-a0cc-0a3334289514",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "87658203-e643-4843-a3cc-8619227725f7",
  "sourceToolAssistantUUID": "1a3ffbe6-c5cb-4092-a0cc-0a3334289514",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-20T21:15:15.593Z_

Now I have a comprehensive understanding of the entire project. Let me now submit my review. I need to load the submission tool first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87658203-e643-4843-a3cc-8619227725f7",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWjWLwHcxK3Q6faMBZQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e4e453b-daf8-4f07-9298-cb57e195fc2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzQ2qwNZ43PPiZhkAFhabW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3004,
      "cache_read_input_tokens": 104074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 52 · 2026-05-20T21:15:16.360Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015Hp28Sf1XA3Pff9ZXZ6N82`</summary>

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
  "parentUuid": "0e4e453b-daf8-4f07-9298-cb57e195fc2a",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWjWLwHcxK3Q6faMBZQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9488675e-1c17-4819-8040-3800fc1ee0e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzQ2qwNZ43PPiZhkAFhabW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3004,
      "cache_read_input_tokens": 104074,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 104074,
          "cache_creation_input_tokens": 3004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3004,
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

_source line 53 · 2026-05-20T21:15:16.368Z_

<details><summary>↩ Tool result · `toolu_015Hp28Sf1XA3Pff9ZXZ6N82`</summary>

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
  "parentUuid": "9488675e-1c17-4819-8040-3800fc1ee0e8",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "88f6a284-586f-41ef-b01e-af598e4b991e",
  "sourceToolAssistantUUID": "9488675e-1c17-4819-8040-3800fc1ee0e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-20T21:15:22.691Z_



Now I have all the information I need. Let me carefully analyze the discrepancy between the paper summary provided in my task and the actual dream papers. The task summary describes a **hybrid scenario** that doesn't cleanly match either the "best" (Path A: CaCLR works) or "median" (Path B: CaCLR fails) dream papers. The task summary describes CaCLR as failing (consistency loss inert, p=0.71), which aligns with the median paper's narrative, but includes specific numbers from both tiers. This appears to be the scenario the review should evaluate.

Let me now write and submit my comprehensive R1 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88f6a284-586f-41ef-b01e-af598e4b991e",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWjntrHqqhxoVavU7pf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5281c33-08e1-44dc-9e3a-80843dee508f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jL1HdbnASRrFXtsxCTa3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 107078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 741,
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

_source line 55 · 2026-05-20T21:16:59.696Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01A1bCr6HYMPkUD145peBtDB`</summary>

```json
{
  "report": "---\ndream_id: dream_20260520T201854\ntier: best\noverall_score: weak accept (4/6)\nreviewer: R1 (Methods & Experiments)\ntimestamp: 2026-05-20\n---\n\n# Review: Does Probe-Based Calibration Work Beyond English?\n\n**Reviewer R1 — Methodology Soundness & Experimental Rigor**\n\n---\n\n## 1. Methodology Assessment\n\n### 1.1 Statistical Rigor\n\nThe paper demonstrates substantially improved statistical practice compared to the earlier draft (Round 0 had zero statistical tests). Bootstrap CIs (1000 resamples), paired permutation tests, and Cohen's d are now reported for key comparisons. Specific examples:\n\n- CaCLR beta effect: p=0.003, d=0.48, CI [0.019, 0.045] — well-reported\n- Decomposition effect: p=0.006, d=0.41, CI [1.8, 4.4] — appropriate\n- Mean-shift AUROC = 0.000 — confirmed with formal rank-invariance argument\n\nHowever, statistical rigor is applied **selectively**. The Pareto rho values, CKA-transfer correlation, orthogonality measurements, cross-benchmark correlation (r=0.92), and architecture comparisons lack paired tests or proper uncertainty quantification. No multiple comparison corrections are applied across the many language x layer x model comparisons. The paper applies rigorous statistics where results are strong and omits them where results might be weaker — this asymmetry undermines confidence in the unreported comparisons.\n\n### 1.2 Experimental Controls\n\nControls are generally well-chosen:\n- **Hewitt & Liang control tasks** (Table 13): Selectivity minimum 0.192 > 0.15 threshold. Validates genuine signal extraction.\n- **Random-direction control** in decomposition (Table 9): Only +0.3pp vs difficulty removal's +3.1pp median. Properly rules out dimensionality reduction artifacts.\n- **INT8 validation** (Appendix): Max AUROC delta 0.6pp, direction cosine > 0.987. Adequate for Scout but missing for Qwen3 (see weaknesses).\n- **Probe complexity comparison**: LR vs MLP addresses the probe choice systematically.\n- **Mean-shift rank-invariance proof**: Elegant and correctly derived under StandardScaler + logistic regression.\n\n### 1.3 Methodological Concerns\n\n**CaCLR training procedure is critically underspecified.** The paper describes CaCLR as using a composite loss with an MMD term (Eq. 2), but:\n- (a) The MMD kernel is unspecified (Gaussian RBF? linear? polynomial?). Bandwidth selection method is unreported.\n- (b) Is the CaCLR probe still a single linear layer? If so, how is gradient-based optimization of logistic regression with 3 loss terms implemented — initialized from the standard LR solution, or trained from scratch with SGD?\n- (c) Optimizer, learning rate, number of epochs, and early stopping criteria are absent.\n- (d) How many parallel activation pairs feed the MMD term? Are they the same items as BCE training data, or a held-out set?\n- (e) The GlobalMMLU train-split translations used for parallel inputs — how large is this set per language? Quality of translations for low-resource languages?\n\nThese details are essential for reproducibility regardless of whether CaCLR is a method contribution (Path A) or a negative result (Path B). For a negative result, the community needs confidence the method received a fair trial.\n\n**CKA \"mechanistic explanation\" suffers from depth confounding.** The Pearson r=0.82 (CI [0.76, 0.87]) between CKA and transfer AUROC is presented as mechanistic, but both variables are monotonic functions of depth past the elbow. The correlation could be entirely mediated by depth without CKA contributing any independent explanatory power. A partial correlation controlling for normalized depth is not reported despite being a single number that would clarify the claim. The subspace angle analysis (correctness direction rotating 15-35 degrees at deep layers) is more informative but is described only in prose — no table or quantitative results are provided. The combined r=0.32 from the actual experimental data (Table 11) is far weaker than the r=0.82 in the best-tier paper, which raises questions about which number reflects reality.\n\n**The Pareto frontier is reported at reduced resolution.** The experiment plan specifies 24 probed layers for Qwen3 and 12 for Scout. Table 1 reports only 7 and 6 layers respectively. The review_context contains the full 17-layer Qwen3 data. For a paper whose central contribution is a \"frontier,\" reporting 7/24 layers in the main text — even with supplementary data — is a presentation gap that invites suspicion of selective reporting. The full layer x language matrix should appear in supplementary at minimum.\n\n---\n\n## 2. Experimental Coverage\n\n### 2.1 Planned vs. Executed Experiments\n\nAll 13 planned experiments (plan_001 through plan_013, plus plans 008-009 as camera-ready) appear to have corresponding results in the paper. This is commendable coverage:\n\n| Plan | Status | Paper Section |\n|------|--------|---------------|\n| 001: Qwen3 Pareto | Covered | Table 1, §5.1 |\n| 002: Llama4 Pareto | Covered | Table 5, §5.1 |\n| 003: CaCLR | Covered | Tables 6-8, §5.2 |\n| 004: Decomposition | Covered | Table 9, §5.3 |\n| 005: Orthogonality | Covered | Table 10, §5.4 |\n| 006: Probe complexity | Covered | Table in §5.6 |\n| 007: Cross-benchmark | Covered | Table in §5.7 |\n| 008: Gemma 4 (P2) | Covered | Appendix C |\n| 009: 52 languages (P2) | Covered | Table 3, §5.9 |\n| 010: INT8 validation | Covered | Appendix A |\n| 011: CKA analysis | Covered | Table in §5.5 |\n| 012: Linear projection | Covered | Table 12, §5.8 |\n| 013: Control tasks | Covered | Appendix B |\n\n### 2.2 Missing or Insufficient Experiments\n\n1. **No partial correlation for CKA controlling for depth.** This is the single most important missing analysis — it would clarify whether CKA adds explanatory power beyond the trivial \"deeper = worse transfer.\"\n\n2. **No expert routing analysis for the architecture-dependence claim.** The paper attributes Pareto shape differences to \"MoE expert routing\" but provides zero evidence about expert routing behavior (e.g., routing entropy by language, expert language specialization metrics). Three models differing in architecture type, scale, layer count, active parameters, and training data cannot support causal claims about expert routing.\n\n3. **CaCLR on difficulty-removed representations not tested.** The decomposition (Claim 2) identifies difficulty entanglement as a transfer mechanism. CaCLR (Claim 3) uses distributional alignment, not difficulty removal. A natural experiment — running CaCLR on difficulty-removed representations — would test whether these address the same or different variance and close the logical gap in the causal chain.\n\n4. **Only MMD tested for distributional alignment.** The paper's conclusion that \"distributional matching fails\" (in the median/negative-result scenario) tests only one distributional method. CORAL (second-order statistics), adversarial alignment (DANN), and optimal transport are established alternatives. The conclusion should be scoped to \"MMD-based distributional matching.\"\n\n5. **INT8 validation covers only Scout, not Qwen3.** Qwen3-235B is the primary model. Quantization effects may differ across architectures and scales. Even 5 layers on a subset would suffice.\n\n6. **Orthogonality table shows only 10/20 languages.** The paper claims all 20 languages have cosine < 0.062, but Table 10 displays only 10. Full data should appear in supplementary.\n\n---\n\n## 3. Strengths\n\n**S1. Unprecedented experimental scope with systematic controls.** Three architectures x 20+ languages x 5 transfer methods x 3 benchmarks, with Hewitt & Liang controls, random-direction controls, INT8 validation, and probe complexity comparison. This is among the most thorough empirical packages in the cross-lingual calibration literature. Few papers provide this breadth of validation.\n\n**S2. Mean-shift rank-invariance proof is a clean theoretical contribution.** The formal argument that StandardScaler + logistic regression renders mean-shift AUROC-invariant is elegant, practically valuable, and empirically confirmed (AUROC delta = 0.000 across all languages and layers). This corrects an implicit assumption from Xiao et al. and is the kind of tight theory-experiment alignment that strengthens a paper.\n\n**S3. Difficulty-capability decomposition is methodologically well-designed.** IRT difficulty probes with R-squared=0.68 validating linear accessibility, difficulty-correctness cosine of 0.34 confirming partial but not full overlap, random-direction control yielding only +0.2pp, and the resource-tier gradient (LOW +4.1pp vs HIGH +2.2pp) providing interpretable structure. The depth gradient (deep benefit exceeding shallow) coherently supports the geometric narrative.\n\n**S4. Linear projection data efficiency analysis is practically actionable.** The saturation curve showing ~50 pairs achieve 98% of 200-pair performance, with the tier-stratified breakdown (LOW needing ~48 pairs vs HIGH ~22), gives practitioners directly usable guidance. This is more useful than many method contributions.\n\n**S5. Statistical practice, where applied, meets a high standard.** Bootstrap CIs, paired permutation tests, and Cohen's d on key comparisons (CaCLR beta, decomposition) go well beyond the field's typical standard of reporting only point estimates. The beta sensitivity sweep across 3 OOM with clear reporting of effect sizes is well-structured.\n\n---\n\n## 4. Weaknesses\n\n**W1 (Major). CKA \"mechanistic explanation\" is correlational and likely depth-confounded.**\nThe r=0.82 Pearson correlation between CKA and transfer AUROC is the paper's central mechanistic claim, but depth is a shared confounder for both variables. Without partial correlation controlling for normalized depth, the \"34% of variance explained\" (or the combined r=0.32 from Table 11, which itself is much weaker) may largely reflect the trivial observation that both CKA and transfer degrade with depth. The subspace angle analysis (15-35 degree rotation at deep layers) is described only narratively without quantitative tables. The disconnect between the r=0.82 claimed in the best-tier narrative and the r=0.32 in Table 11 of the actual paper summary is concerning — the lower number suggests CKA is at best suggestive, not mechanistic.\n\n**W2 (Major). Architecture-dependence claim is confounded and cannot support causal attribution.**\nThree models differ simultaneously in architecture type (2 MoE, 1 Dense), total parameters (235B, 109B, 31B), active parameters (22B, 17B, 31B), layer count (94, 48, 60), and training data. The paper attributes Pareto shape differences (rho = -0.44 dense, -0.38 MoE-large, -0.18 MoE-small from the task summary; or -0.69, -0.73, -0.78 from the best-tier paper) to \"MoE expert routing accelerating language specialization\" without any expert routing analysis (routing entropy, expert specialization metrics). Three confounded data points are insufficient for causal attribution. The claim should be qualified as observational.\n\n**W3 (Major). CaCLR training procedure is critically underspecified.**\nFor either the method contribution (Path A) or negative result (Path B) narrative, the MMD kernel, bandwidth selection, optimizer, learning rate, epochs, initialization strategy, and parallel data handling must be reported. Without these, neither the positive claim (\"CaCLR works\") nor the negative claim (\"distributional matching fails\") is reproducible. The task summary states the consistency loss is inert (p=0.71 vs zero-shot), yet the best-tier paper claims p=0.003 — this contradiction between scenarios demands that whichever narrative is adopted, the training procedure be fully transparent.\n\n**W4 (Moderate). Selective layer and language reporting.**\nThe Pareto frontier is reported at 7/24 layers for Qwen3 and 6/12 for Scout in the main text. The orthogonality table shows 10/20 languages. For a paper whose titular contribution is a frontier requiring dense sampling, and whose orthogonality claim covers all 20 languages, this selective presentation is a gap. Full data should appear in supplementary with the main text presenting key summary statistics.\n\n**W5 (Minor). Logical gap between decomposition and CaCLR in the causal chain.**\nThe decomposition identifies difficulty entanglement as a transfer degradation mechanism. CaCLR uses MMD distributional alignment, which does not operationalize difficulty removal. The narrative implies decomposition motivates CaCLR, but the connection is indirect. Testing CaCLR on difficulty-removed representations would close this gap.\n\n---\n\n## 5. Questions for Authors\n\n**Q1.** What is the partial correlation between CKA and transfer AUROC after controlling for normalized depth? This single number would clarify whether CKA provides explanatory power beyond \"deeper = worse transfer.\"\n\n**Q2.** Specify the complete CaCLR training procedure: (a) MMD kernel type and bandwidth selection method, (b) optimizer and learning rate schedule, (c) number of training epochs and early stopping criteria, (d) whether the CaCLR probe is initialized from the standard LR solution or trained from scratch, (e) whether MMD is computed on the same items as BCE or a held-out set. For a method whose effectiveness is a central question (Path A vs Path B), these details are essential.\n\n**Q3.** What happens when CaCLR is applied to difficulty-removed representations? Does decomposition + CaCLR stack, or do they address the same variance? This would close the logical gap in the causal chain and potentially improve the method.\n\n---\n\n## 6. Score\n\n**Score: 4/6 (Weak Accept)**\n\n**Rationale.** This paper addresses a genuinely important and underexplored problem at impressive experimental scale. The experimental design is thorough, with 3 architectures, 20+ languages, 3 benchmarks, 5 transfer methods, and multiple well-chosen controls. Several analytical contributions are strong: the mean-shift invariance proof, the difficulty-capability decomposition with random-direction controls, the linear projection data efficiency analysis, and the Hewitt & Liang selectivity validation. Statistical practice, where applied, meets a high standard.\n\nThe paper falls short of a strong accept for three reasons. First, the CKA \"mechanistic explanation\" is correlational and likely confounded by depth — the gap between r=0.82 (claimed) and r=0.32 (Table 11) suggests the explanation is suggestive rather than mechanistic. Second, the architecture-dependence claim is attributed to MoE expert routing without any direct evidence about routing behavior, and three confounded models cannot support this causal claim. Third, the CaCLR training procedure is critically underspecified regardless of whether the method succeeds or fails — reproducibility requires complete implementation details.\n\nThe analytical findings — particularly the Pareto frontier quantification, decomposition, universal orthogonality, and the practical finding that ~50 parallel pairs suffice for effective linear projection — represent genuine contributions that warrant publication at a top venue, provided the framing matches the evidence. The paper would be strengthened by: (a) reporting partial CKA correlation controlling for depth, (b) qualifying architecture-dependence as observational, (c) specifying CaCLR implementation completely, and (d) reporting full layer and language data in supplementary.\n\n---\n\n## 7. Confidence\n\n**Confidence: 4/5**\n\nI am familiar with the cross-lingual probing, domain adaptation, and LLM calibration literatures. I have reviewed the experimental design, statistical methodology, and all reported results in detail. My uncertainty is primarily around whether the full experimental data (not reported in the paper's tables) might resolve some of the concerns about selective reporting.\n",
  "project": "xling_calib_direction",
  "tier": "best",
  "dream_id": "dream_20260520T201854",
  "overall_score": "weak accept (4/6)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5281c33-08e1-44dc-9e3a-80843dee508f",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWjntrHqqhxoVavU7pf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97fc3505-97ef-4d72-a5d7-096da2d23858",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jL1HdbnASRrFXtsxCTa3p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 107078,
      "output_tokens": 4229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 741
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4229,
          "cache_read_input_tokens": 107078,
          "cache_creation_input_tokens": 741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 741,
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

_source line 56 · 2026-05-20T21:17:00.452Z_

<details><summary>↩ Tool result · `toolu_01A1bCr6HYMPkUD145peBtDB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md\", \"dream_id\": \"dream_20260520T201854\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97fc3505-97ef-4d72-a5d7-096da2d23858",
  "isSidechain": true,
  "promptId": "9ca6497d-4d23-4b00-aaf6-7b3419484e1e",
  "agentId": "a63f8037928e359aa",
  "type": "user",
  "uuid": "5afa15a5-e59b-4316-9f34-66d7e8cdf2ba",
  "sourceToolAssistantUUID": "97fc3505-97ef-4d72-a5d7-096da2d23858",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-20T21:17:10.391Z_

Review submitted successfully. Here is the summary:

**Score: 4/6 (Weak Accept) | Confidence: 4/5**

**Key findings from the methodology/experiments review:**

**Strengths:**
- Unprecedented experimental scope: 3 architectures x 20+ languages x 5 transfer methods x 3 benchmarks with systematic controls (Hewitt & Liang, random-direction, INT8, probe complexity)
- Mean-shift rank-invariance proof is a clean, novel theoretical contribution empirically confirmed at AUROC delta = 0.000
- Difficulty-capability decomposition is well-designed with proper random-direction controls (+0.2pp vs +3.1pp)
- Linear projection data efficiency analysis (~50 pairs = 98% of 200-pair performance) is practically actionable
- Statistical practice, where applied, meets high standards (bootstrap CIs, permutation tests, Cohen's d)

**Major weaknesses:**
1. **CKA "mechanistic explanation" is correlational and depth-confounded** -- partial correlation controlling for depth not reported; gap between r=0.82 (claimed) and r=0.32 (Table 11) undermines the mechanistic framing
2. **Architecture-dependence claim is confounded** -- three models differ in architecture, scale, layers, and training data simultaneously; MoE expert routing attribution lacks any direct routing analysis
3. **CaCLR training procedure critically underspecified** -- MMD kernel, bandwidth, optimizer, epochs, initialization all missing; essential for reproducibility regardless of whether CaCLR succeeds or fails

**Moderate/minor weaknesses:**
4. Selective layer/language reporting (7/24 layers, 10/20 languages in main text)
5. Logical gap between decomposition and CaCLR in the causal chain (not tested together)
6. Statistical rigor applied asymmetrically (rigorous where results are strong, omitted elsewhere)

**Critical questions:** (1) partial CKA-transfer correlation controlling for depth, (2) complete CaCLR implementation details, (3) CaCLR on difficulty-removed representations.

Report saved to `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5afa15a5-e59b-4316-9f34-66d7e8cdf2ba",
  "isSidechain": true,
  "agentId": "a63f8037928e359aa",
  "requestId": "req_011CbEWsTRYMHiTM9LryLKLE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99d6419d-7d81-4ce2-bc45-5c3dbefe6e1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "effd200a-63e4-4db3-aa5b-047288d9466f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHLbvA7Ffi5WURi11kbDaV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4360,
      "cache_read_input_tokens": 107819,
      "output_tokens": 546,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4360
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 546,
          "cache_read_input_tokens": 107819,
          "cache_creation_input_tokens": 4360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4360,
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
