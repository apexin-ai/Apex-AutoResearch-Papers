# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty, positioning, and related work**. ## Paper Su

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a608204260859e5b5.jsonl`
- **Structured JSON:** [`a2c5c75492c31f4745a4.json`](../../sessions/a2/a2c5c75492c31f4745a4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

57 recorded events

### User

_source line 1 · 2026-05-20T20:59:54.659Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty, positioning, and related work**.

## Paper Summary
"Cross-Lingual Calibration via Internal Correctness Directions: Pareto Frontiers, Decomposition, and Consistency-Aligned Probes" — a 10-page paper studying cross-lingual transfer of correctness probes in multilingual LLMs. Key contributions:
1. Depth–transferability Pareto frontier: deeper layers = better EN probes but worse cross-lingual transfer. Architecture-dependent shape (60% for Qwen3-235B, 50% for Llama 4 Scout, 75% for Gemma 4 Dense).
2. Difficulty–capability decomposition: removing IRT difficulty direction improves cross-lingual transfer by 3.1pp.
3. CaCLR: L_BCE + α·L_SB-ECE + β·L_MMD probe training. Zero target-language labels needed. Reduces non-English ECE by 3.5% over temperature scaling.
4. Cross-lingual orthogonality: correctness–confidence cosine &lt; 0.062 universally across 20 languages.
5. CKA mechanistic analysis linking representation geometry to transfer success.

## Related Work as presented in the paper (Section 2)
- **LLM Calibration**: Temperature scaling, LACE (per-language layer ensembles, needs target labels), MKA (5× inference cost)
- **Probe-Based Calibration**: CORAL (cross-task EN probes), CCPS (clustering), Miao &amp; Ungar (correctness–confidence orthogonality, English-only 7-8B)
- **Cross-Lingual Probe Transfer**: Xiao et al. (knowledge boundary probes, 8 langs — fundamentally different: answerability vs correctness). Civelli et al. (cross-lingual difficulty probes)
- **Domain Adaptation Theory**: Ben-David et al. H-divergence
- **Representation Similarity**: CKA
- **Cross-Lingual Alignment**: MUSE, VecMap
- **Conformal Prediction**: mentioned as complementary

## Key claims requiring novelty assessment
1. "First systematic study of cross-lingual correctness probe transfer"
2. Pareto frontier discovery (depth vs. transferability tradeoff)
3. Architecture-dependent frontier shape (MoE vs dense)
4. Difficulty–capability decomposition as explanatory mechanism
5. CaCLR as a method contribution (MMD consistency loss on parallel activations)
6. Universal cross-lingual orthogonality (extending Miao &amp; Ungar)

## Your Task

Evaluate the paper on **novelty, significance, and positioning**. Write a detailed review covering:

### 1. Novelty Assessment
For each of the 6 claims above:
- Is this genuinely novel? Or incremental extension of known results?
- How significant is the contribution to the field?
- What is the delta over the closest prior work?

### 2. Related Work Completeness
- Are there important missing references? Consider:
  - Cross-lingual representation probing literature (e.g., Conneau et al., Pires et al., Chi et al. on multilingual BERT probing)
  - Calibration literature beyond what's cited
  - MMD/domain adaptation in NLP (not just Ben-David theory but applied methods)
  - Probe transfer across domains/languages more broadly
  - Internal representations of LLMs (mechanistic interpretability angle)
- Is the differentiation from Xiao et al. (knowledge boundary vs. correctness) convincing?
- Is the differentiation from Miao &amp; Ungar sufficient?

### 3. Positioning and Framing
- Is the "causal chain" framing (contributions 1→2→3→4 + CKA as glue) convincing?
- Does the paper oversell or undersell any contribution?
- Is CaCLR positioned appropriately — is it a method contribution or an analysis paper with a method?
- The paper uses only 2 MoE models in the main text. Is the "architecture-dependent" claim well-supported with just 2 data points (+1 in appendix)?

### 4. Significance and Impact
- Would this change how practitioners do multilingual calibration?
- What is the target audience? Calibration researchers? Multilingual NLP? Mechanistic interpretability?
- Is 3.5% ECE improvement over temperature scaling meaningful in practice?

### 5. Weaknesses (numbered list)
Specific, actionable weaknesses focused on novelty/positioning.

### 6. Questions for Authors (numbered list)

### 7. Score and Confidence
- Score (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)
- Confidence (1-5: 1=low, 5=expert)

Format your review as a structured document with clear headers. Be rigorous but fair.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "b0df6023-c791-428e-9ce7-bd1b0ae7cb06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T20:59:54.662Z_

```json
{
  "parentUuid": "b0df6023-c791-428e-9ce7-bd1b0ae7cb06",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
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
  "uuid": "f2754525-c493-4b95-8152-28d7b103d121",
  "timestamp": "2026-05-20T20:59:54.662Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T20:59:58.116Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2754525-c493-4b95-8152-28d7b103d121",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVZqm6YeNgJwvhdwDz5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b515d10d-de87-4c21-b166-01e55612b83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017mN4EmwitirCefZNqTH46P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7294,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7294,
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

_source line 4 · 2026-05-20T20:59:58.731Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NhyEDEdAtP3mvPFxkzgmbJ`</summary>

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
  "parentUuid": "b515d10d-de87-4c21-b166-01e55612b83b",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVZqm6YeNgJwvhdwDz5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a9c7d56-01e4-4069-896c-4bcbeaaddb18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017mN4EmwitirCefZNqTH46P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7294,
      "cache_read_input_tokens": 8251,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7294
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7294,
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

_source line 5 · 2026-05-20T20:59:58.734Z_

<details><summary>↩ Tool result · `toolu_01NhyEDEdAtP3mvPFxkzgmbJ`</summary>

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
  "parentUuid": "4a9c7d56-01e4-4069-896c-4bcbeaaddb18",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "c999b560-05fb-49bc-9004-e309b716e271",
  "sourceToolAssistantUUID": "4a9c7d56-01e4-4069-896c-4bcbeaaddb18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T21:00:01.404Z_



Let me gather all the relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c999b560-05fb-49bc-9004-e309b716e271",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVa987zPsAdLQ2gcTLp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96ffddcf-6bc7-440c-89e3-3b327fec08c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011C81sT1dDj2TyQeM8JAj7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-20T21:00:01.935Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01XCfV72qQji9CqjVoxKeT8U`</summary>

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
  "parentUuid": "96ffddcf-6bc7-440c-89e3-3b327fec08c1",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVa987zPsAdLQ2gcTLp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf08ff2b-731e-474b-8a4b-730ad293574a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011C81sT1dDj2TyQeM8JAj7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 8 · 2026-05-20T21:00:01.975Z_

<details><summary>↩ Tool result · `toolu_01XCfV72qQji9CqjVoxKeT8U`</summary>

```text
{"result":"# 项目 xling_calib_direction 概况\n\n## 实验状态 (3 个)\n\n- **mvp_003**: DONE (success) — \n- **mvp_001**: DONE (success) — \n- **mvp_002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_003** (success): Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). ← 基于 mvp_001\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\n- **mvp_002** (success): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\n\n## 趋势\n成功 3 / 负向 0 / 失败 0 / 共 3\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-13176: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf08ff2b-731e-474b-8a4b-730ad293574a",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "7815adda-f60f-4774-8f3e-125bd28a5a82",
  "sourceToolAssistantUUID": "bf08ff2b-731e-474b-8a4b-730ad293574a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T21:00:02.363Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0168Aep7gYNdyyN99s6Sg4eg`</summary>

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
  "parentUuid": "7815adda-f60f-4774-8f3e-125bd28a5a82",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVa987zPsAdLQ2gcTLp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b655839c-1597-422d-8670-c2787bbdc9c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011C81sT1dDj2TyQeM8JAj7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 10 · 2026-05-20T21:00:02.380Z_

<details><summary>↩ Tool result · `toolu_0168Aep7gYNdyyN99s6Sg4eg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_003** (success): Cross-lingual correctness direction is model-agnostic: an English-trained linear probe on Llama-3.1-8B-Instruct internal representations will transfer to non-English languages (zh/ar/hi/sw/ko) with AUROC >= 0.58, replicating the pattern observed in Qwen2.5-7B-Instruct (mvp_001). ← 基于 mvp_001\\n- **mvp_001** (success): 在 7B 模型的中间层 activation space 中存在 language-agnostic correctness direction，使得英语训练的线性 probe（LogisticRegression）能 zero-shot 迁移到非英语语言（≥3/5 语言 AUROC ≥ 0.58, p < 0.05），且存在 layer-depth 效应（浅层 vs 深层 ΔAUROC ≥ 5pp）。Mean-shift alignment 可进一步改善迁移（Δ ≥ 2pp for ≥3/5 语言）。\\n- **mvp_002** (success): Layer-depth 效应在 Qwen2.5-7B-Instruct 的互补层集合（2,6,10,14,18,22,26）上复现，与 mvp_001（0,4,8,12,16,20,24,27）合并后提供近全层覆盖（15/28层），验证 AUROC 的 layer-depth 趋势不依赖于特定层采样。（模型实际 28 层，index 0-27） ← 基于 mvp_001\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 0 / 共 3\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-13176: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1012, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b655839c-1597-422d-8670-c2787bbdc9c3",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "29e21e1a-0865-4036-b865-3e2d89d9d363",
  "sourceToolAssistantUUID": "b655839c-1597-422d-8670-c2787bbdc9c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T21:00:02.820Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BjKpSfGoUGNyzLxBq7WPTe`</summary>

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
  "parentUuid": "29e21e1a-0865-4036-b865-3e2d89d9d363",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVa987zPsAdLQ2gcTLp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "400bfd0a-ab0b-43d5-91af-f21053b0b8be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011C81sT1dDj2TyQeM8JAj7W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 12 · 2026-05-20T21:00:02.840Z_

<details><summary>↩ Tool result · `toolu_01BjKpSfGoUGNyzLxBq7WPTe`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "400bfd0a-ab0b-43d5-91af-f21053b0b8be",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "00e58d5a-2946-43c7-b2bb-1685964a6adc",
  "sourceToolAssistantUUID": "400bfd0a-ab0b-43d5-91af-f21053b0b8be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T21:00:06.020Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RXcZhiMuNHPkQWFkMgY8XJ`</summary>

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
  "parentUuid": "00e58d5a-2946-43c7-b2bb-1685964a6adc",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVaTDoXrDB7orEA8dez",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7274f960-5d24-43da-97c0-f901e8f9a1cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaLW5JWf6PETr2CYvdjx6D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1878,
      "cache_read_input_tokens": 16993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 14 · 2026-05-20T21:00:06.035Z_

<details><summary>↩ Tool result · `toolu_01RXcZhiMuNHPkQWFkMgY8XJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\", \"content\": \"papers:\\n  miao2026closing:\\n    title: \\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\"\\n    authors: [\\\"Ruoxi Miao\\\", \\\"Lyle Ungar\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.25052\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  xiao2025knowledge:\\n    title: \\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\"\\n    authors: [\\\"Zheng Xiao\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2504.13816\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  civelli2026shared:\\n    title: \\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\"\\n    authors: [\\\"Andrea Civelli\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2601.12731\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  zhou2025lace:\\n    title: \\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\"\\n    authors: [\\\"Zhou\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03136\\\"\\n    category: \\\"multilingual_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ravisankar2026dali:\\n    title: \\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\"\\n    authors: [\\\"Ravisankar\\\"]\\n    year: 2026\\n    venue: \\\"EACL 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2504.09378\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  miao2026coral:\\n    title: \\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\"\\n    authors: [\\\"Ruoxi Miao\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.06022\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  joshi2025calibration:\\n    title: \\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\"\\n    authors: [\\\"Joshi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  confidence_manifold2026:\\n    title: \\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08159\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  karandikar2021sbece:\\n    title: \\\"Soft Calibration Objectives for Neural Networks\\\"\\n    authors: [\\\"Karandikar\\\"]\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"\\\"\\n    category: \\\"calibration_methods\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  khanmohammadi2025ccps:\\n    title: \\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\"\\n    authors: [\\\"Khanmohammadi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.21772\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  liu2025middle:\\n    title: \\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\"\\n    authors: [\\\"Liu\\\", \\\"Niehues\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ji2025calibrating:\\n    title: \\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\"\\n    authors: [\\\"Ji\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Verbal uncertainty governed by single linear direction in representation space.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\ncategories:\\n  mechanistic_calibration: \\\"Probing/steering calibration signals in LLM internal representations\\\"\\n  cross_lingual_probing: \\\"Cross-lingual transfer of probes/directions in multilingual models\\\"\\n  cross_lingual_alignment: \\\"Language alignment and shared representations in multilingual LLMs\\\"\\n  multilingual_calibration: \\\"Calibration methods for multilingual LLMs\\\"\\n  calibration_methods: \\\"General calibration objectives and techniques\\\"\\n\\nmeta:\\n  created_at: \\\"2026-05-20\\\"\\n  last_updated: \\\"2026-05-20\\\"\\n  total_papers: 12\\n\", \"total_chars\": 6989, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7274f960-5d24-43da-97c0-f901e8f9a1cd",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "7cab5d8b-8f95-4aed-a4af-fd80c52a827a",
  "sourceToolAssistantUUID": "7274f960-5d24-43da-97c0-f901e8f9a1cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T21:00:07.310Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WgH3Qr1tCsBND3u4sr4PW2`</summary>

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
  "parentUuid": "7cab5d8b-8f95-4aed-a4af-fd80c52a827a",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVaTDoXrDB7orEA8dez",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb0d09b4-cf28-4fe9-a31f-e1b2e587551b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaLW5JWf6PETr2CYvdjx6D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1878,
      "cache_read_input_tokens": 16993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 16 · 2026-05-20T21:00:07.326Z_

<details><summary>↩ Tool result · `toolu_01WgH3Qr1tCsBND3u4sr4PW2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 2 models × 20 languages × all contributions\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). Cross-lingual transfer degrades only when this subspace itself begins to language-specialize at the deepest layers. The resulting depth-transferability tradeoff is architecture-dependent (strong on Qwen, weak on Llama), explained by architecture-specific CKA cliff steepness. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes reveal an architecture-dependent depth-transferability relationship: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong Pareto); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture-dependence of the Pareto shape is itself a core finding, not merely a qualifier.\\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method / Diagnostic)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.\\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA pilot reveals the mechanistic explanation: correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.\\n- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.\\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\\n- **Headline template (method success)**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n- **Headline template (negative result)**: \\\"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\\\"\\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak / why does it fail?\\\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n7. **\\\"Predictable from domain adaptation theory\\\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\\n8. **\\\"No statistical tests\\\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\\n9. **\\\"Probing methodology concerns\\\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\\n10. **\\\"No mechanistic explanation\\\"** → CKA analysis provides two levels of insight: (a) between-language: languages with higher CKA (more aligned to English) show less transfer degradation — resource-tier gradient explained; (b) between-architecture: CKA cliff steepness at deepest layers differs (Qwen drops 50% in last 3 layers vs Llama 19%), explaining why Pareto is strong on Qwen but weak on Llama. Within-language depth effect requires 20-language full-scale analysis for statistical power (pilot n=9 per language insufficient). CKA pilot on 2 models × 5 languages validates the approach.\\n11. **\\\"Why not conformal prediction?\\\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\\n12. **\\\"CaCLR parallel activations = test leakage?\\\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\\n\\n## Additional Related Work Coverage (Dream-identified gaps)\\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.\\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.\\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA pilot reveals correctness direction is a robust low-dimensional subspace feature that persists despite global representation divergence. Not a simple \\\"low CKA → bad transfer\\\" relationship, but a threshold phenomenon: transfer collapses only when CKA drops below critical value (~0.35) at deepest layers.\\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.\\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 12237, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb0d09b4-cf28-4fe9-a31f-e1b2e587551b",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "7c8635a7-607c-4abf-8709-33f2aa5c1503",
  "sourceToolAssistantUUID": "eb0d09b4-cf28-4fe9-a31f-e1b2e587551b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T21:00:07.552Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Jg6ggoQoqGGvSoqct9LZFg`</summary>

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
  "parentUuid": "7c8635a7-607c-4abf-8709-33f2aa5c1503",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVaTDoXrDB7orEA8dez",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49c31c1c-413a-458b-912a-bd0977721f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaLW5JWf6PETr2CYvdjx6D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1878,
      "cache_read_input_tokens": 16993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 18 · 2026-05-20T21:00:07.561Z_

<details><summary>↩ Tool result · `toolu_01Jg6ggoQoqGGvSoqct9LZFg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/memory.md\", \"content\": \"# Memory — xling_calib_direction\\n\\n## 环境配置\\n- **服务器**: westd-13176, 4× RTX 6000 PRO 96GB\\n- **环境**: conda base (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)\\n- **模型路径 (Qwen)**: `/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct`\\n- **模型路径 (Llama)**: ModelScope `LLM-Research/Meta-Llama-3.1-8B-Instruct`\\n- **代码路径**: `/root/xling_calib_direction/`\\n- **备份路径**: `/root/autodl-tmp/xling_backup/` (29GB, mvp_001/002/003 全部)\\n- **Qwen2.5-7B-Instruct**: 28 layers (0-27), hidden_dim=3584\\n- **Llama-3.1-8B-Instruct**: 32 layers (0-31), hidden_dim=4096\\n- **网络**: 不要用 `source /etc/network_turbo`，用 `HF_ENDPOINT=https://hf-mirror.com`\\n- **模型下载**: 用 ModelScope\\n- **磁盘**: 根分区仅 620MB 可用 ⚠️，所有大文件必须放 `/root/autodl-tmp/`（~290GB 可用）\\n\\n## 数据集字段差异\\n- cais/mmlu: `choices` (list), `answer` (int 0-3)\\n- CohereForAI/Global-MMLU: `option_a/b/c/d` (str), `answer` (letter \\\"A\\\"-\\\"D\\\")\\n\\n## MVP 实验关键发现 (2026-05-20)\\n\\n### Mean-shift alignment 完全无效\\n- 不能改变 AUROC（rank-invariant）\\n- 不能改善 calibration（0/5 ΔECE）\\n- 结论：需要非常数 alignment 方法（CDA/CORAL/Procrustes）\\n\\n### Temperature scaling data leakage 教训 (M005)\\n在 test set 上优化 T 并报告 ECE = data leakage。修复后 ECE 全部 FAIL（temp scaling 实际恶化 ECE）。**教训**: 后处理校准必须用 held-out validation set。\\n\\n### Sigmoid 饱和导致 AUROC 评估 artifact\\n- zh@L31 (Llama): logit 均值=+39 → 55% 样本 predict_proba=1.0 → ranking 退化\\n- **修复**: transfer_eval.py 应改用 `decision_function` 算 AUROC（logits 足够）\\n- ECE/Brier 仍需 predict_proba\\n\\n### Layer-depth profile\\n- Qwen: L0-L10 平台(~0.62) → L10-L22 上升(+11pp) → L22-L27 饱和(~0.75)\\n- Llama: 类似趋势，L0=0.65 → L31=0.73，delta=9.53pp\\n- 最后一层英语最强但迁移最差（更 language-specific）\\n\\n### CKA vs Transfer Degradation（核心分析发现）\\n- **CKA 随深度单调下降**（两个模型一致）：深层 representation 更 language-specific\\n- **CKA-degradation 负相关**：Llama rho=-0.52 p=0.001***, Qwen rho=-0.31 p=0.053\\n- **Language ranking 两模型一致**: zh > ar >> hi ≈ sw（高资源 → 高 CKA + 低 degradation）\\n- 解读：correctness signal 是跨语言共享的低维子空间特征，即使全局 representation 已 language-specific\\n\\n### mvp_003 (Llama) 亮点\\n**5/5 语言 pass P2**（包括 sw=0.584），优于 Qwen 的 4/5。Llama-3.1 多语言覆盖更广。\\n\\n### 修正后 Gate Check\\n- Qwen: P1❌ P2✅(4/5) P3✅(14.28pp) P4❌ → PARTIAL 2/4\\n- Llama: P1❌ P2✅(5/5) P3✅(9.53pp) P4❌ → PARTIAL 2/4\\n\\n## 大模型可行性（research 阶段）\\n- Qwen3-235B-A22B: **INT4** 推荐，VRAM ~125G (4 GPU), 磁盘 ~120G\\n- Llama 4 Scout: **INT8** 推荐，VRAM ~115G (2 GPU), 磁盘 ~110G\\n- **关键改动**: 必须用 `register_forward_hook` 替代 `output_hidden_states=True`（94 层全缓存 OOM）\\n- 需要 `pip install bitsandbytes`\\n\\n## 代码修复记录\\n- **M004**: --layers default=None（自动检测），已部署\\n- **待修复**: transfer_eval.py 改用 decision_function 算 AUROC（避免 sigmoid 饱和）\\n\", \"total_chars\": 2525, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49c31c1c-413a-458b-912a-bd0977721f1c",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "b5ace7a4-eee0-4519-bd64-c0b13c3f7975",
  "sourceToolAssistantUUID": "49c31c1c-413a-458b-912a-bd0977721f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T21:00:07.828Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017R5sd6wrWR5QCKRfAgKfKo`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5ace7a4-eee0-4519-bd64-c0b13c3f7975",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVaTDoXrDB7orEA8dez",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8628da98-6791-43a1-9f37-d87a03364a43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaLW5JWf6PETr2CYvdjx6D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1878,
      "cache_read_input_tokens": 16993,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1878
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 389,
          "cache_read_input_tokens": 16993,
          "cache_creation_input_tokens": 1878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1878,
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

_source line 20 · 2026-05-20T21:00:07.836Z_

<details><summary>↩ Tool result · `toolu_017R5sd6wrWR5QCKRfAgKfKo`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'xling_calib_direction'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8628da98-6791-43a1-9f37-d87a03364a43",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "3b1e0c7a-6b85-4844-b488-33617e692df3",
  "sourceToolAssistantUUID": "8628da98-6791-43a1-9f37-d87a03364a43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T21:00:11.474Z_

Now let me read the paper itself and associated research skill files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b1e0c7a-6b85-4844-b488-33617e692df3",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVapJZqYhV4QxWE3dpT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1343806a-0742-4226-a586-7a98b7441841",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJfZa1rix5KpSZ6fEgrEZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8299,
      "cache_read_input_tokens": 18871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8299,
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

_source line 22 · 2026-05-20T21:00:11.944Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SSLGPQNbKXYz5gv1cycyDD`</summary>

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
  "parentUuid": "1343806a-0742-4226-a586-7a98b7441841",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVapJZqYhV4QxWE3dpT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cc22451-587f-4979-b609-2a493863f309",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJfZa1rix5KpSZ6fEgrEZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8299,
      "cache_read_input_tokens": 18871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8299,
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

_source line 23 · 2026-05-20T21:00:11.956Z_

<details><summary>↩ Tool result · `toolu_01SSLGPQNbKXYz5gv1cycyDD`</summary>

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
  "parentUuid": "1cc22451-587f-4979-b609-2a493863f309",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "8c880bb0-b66d-43a8-9924-739728543eee",
  "sourceToolAssistantUUID": "1cc22451-587f-4979-b609-2a493863f309",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T21:00:12.889Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YJFKFa91Rd4DkWUhok1Ves`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c880bb0-b66d-43a8-9924-739728543eee",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVapJZqYhV4QxWE3dpT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b1572b6-abb0-4b56-b705-d490ee0aaf81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJfZa1rix5KpSZ6fEgrEZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8299,
      "cache_read_input_tokens": 18871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8299,
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

_source line 25 · 2026-05-20T21:00:12.900Z_

<details><summary>↩ Tool result · `toolu_01YJFKFa91Rd4DkWUhok1Ves`</summary>

```text
artifacts/dream_reports/dream_20260520T185641/best/paper.pdf
artifacts/dream_reports/dream_20260520T185641/median/paper.pdf
artifacts/dream_reports/dream_20260520T185641/worst/paper.pdf
artifacts/dream_reports/dream_20260520T201854/best/paper.pdf
artifacts/dream_reports/dream_20260520T201854/median/paper.pdf
artifacts/dream_reports/dream_20260520T201854/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b1572b6-abb0-4b56-b705-d490ee0aaf81",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "1425160e-ad8f-4606-98ef-66b3c5e1b338",
  "sourceToolAssistantUUID": "5b1572b6-abb0-4b56-b705-d490ee0aaf81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T21:00:13.143Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011fnA7SaExXrfqkHMwFy1SS`</summary>

```json
{
  "pattern": "artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1425160e-ad8f-4606-98ef-66b3c5e1b338",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVapJZqYhV4QxWE3dpT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffae49d3-9454-4cef-b0bb-35f17ebc55c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJfZa1rix5KpSZ6fEgrEZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8299,
      "cache_read_input_tokens": 18871,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8299
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 18871,
          "cache_creation_input_tokens": 8299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8299,
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

_source line 27 · 2026-05-20T21:00:13.181Z_

<details><summary>↩ Tool result · `toolu_011fnA7SaExXrfqkHMwFy1SS`</summary>

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
artifacts/dream_reports/dream_20260520T201854/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffae49d3-9454-4cef-b0bb-35f17ebc55c3",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "9f86ae48-ca4a-4bdf-affc-543fd1fdafd0",
  "sourceToolAssistantUUID": "ffae49d3-9454-4cef-b0bb-35f17ebc55c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T21:00:15.858Z_

Let me read the most recent best paper.tex (the latest dream report) along with the review context and existing reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f86ae48-ca4a-4bdf-affc-543fd1fdafd0",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVbD1owp9yum7VA8rJW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3a4323d-5f9a-4e03-a475-5349566bc256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DD6NC7SxxJBfvT7A8VCvyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2682,
      "cache_read_input_tokens": 27170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2682,
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

_source line 29 · 2026-05-20T21:00:16.929Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MVGtqFNkYi5dQTZSd6ngoV`</summary>

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
  "parentUuid": "c3a4323d-5f9a-4e03-a475-5349566bc256",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVbD1owp9yum7VA8rJW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e1a3b53-34da-4373-972b-67e1bb935ccc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DD6NC7SxxJBfvT7A8VCvyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2682,
      "cache_read_input_tokens": 27170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2682,
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

_source line 30 · 2026-05-20T21:00:17.335Z_

<details><summary>↩ Tool result · `toolu_01MVGtqFNkYi5dQTZSd6ngoV`</summary>

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
  "parentUuid": "2e1a3b53-34da-4373-972b-67e1bb935ccc",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "a8a20ee9-ae82-4148-83ba-d971f1e0804b",
  "sourceToolAssistantUUID": "2e1a3b53-34da-4373-972b-67e1bb935ccc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T21:00:17.403Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DDV4yDxxAZ39i1f9KnoPv1`</summary>

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
  "parentUuid": "a8a20ee9-ae82-4148-83ba-d971f1e0804b",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVbD1owp9yum7VA8rJW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9094b3be-5dcf-4d36-a227-a94e5bbf52c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DD6NC7SxxJBfvT7A8VCvyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2682,
      "cache_read_input_tokens": 27170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2682,
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

_source line 32 · 2026-05-20T21:00:17.654Z_

<details><summary>↩ Tool result · `toolu_01DDV4yDxxAZ39i1f9KnoPv1`</summary>

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
  "parentUuid": "9094b3be-5dcf-4d36-a227-a94e5bbf52c5",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "f4984a97-6d3e-4910-b775-82e59c268ede",
  "sourceToolAssistantUUID": "9094b3be-5dcf-4d36-a227-a94e5bbf52c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T21:00:17.931Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BcUq7oC5nRTAYcZsLPJxQc`</summary>

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
  "parentUuid": "f4984a97-6d3e-4910-b775-82e59c268ede",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVbD1owp9yum7VA8rJW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b22febe-50fd-4a19-9e8f-3fd8bf21caa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DD6NC7SxxJBfvT7A8VCvyP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2682,
      "cache_read_input_tokens": 27170,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2682
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 27170,
          "cache_creation_input_tokens": 2682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2682,
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

_source line 34 · 2026-05-20T21:00:18.190Z_

<details><summary>↩ Tool result · `toolu_01BcUq7oC5nRTAYcZsLPJxQc`</summary>

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
  "parentUuid": "3b22febe-50fd-4a19-9e8f-3fd8bf21caa7",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "13084775-ec96-473d-b697-be17e736c963",
  "sourceToolAssistantUUID": "3b22febe-50fd-4a19-9e8f-3fd8bf21caa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-20T21:00:21.590Z_

Now let me read the earlier dream report's review and the existing review report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13084775-ec96-473d-b697-be17e736c963",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVbaMhd6aC41qVF5DZu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e5f3c8b-53f7-4854-80b5-850639a6eaa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cad11Gbs46MDirwZaJuo2t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 51671,
      "cache_read_input_tokens": 29852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 51671,
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

_source line 36 · 2026-05-20T21:00:23.973Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DQw5XMjjcCHjA17b96H719`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e5f3c8b-53f7-4854-80b5-850639a6eaa0",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVbaMhd6aC41qVF5DZu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fad7331-1d3c-49d6-ad0b-2bbc85066a0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cad11Gbs46MDirwZaJuo2t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 51671,
      "cache_read_input_tokens": 29852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 51671,
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

_source line 37 · 2026-05-20T21:00:23.978Z_

<details><summary>↩ Tool result · `toolu_01DQw5XMjjcCHjA17b96H719`</summary>

```text
1	---
2	dream_id: dream_20260520T185641
3	tier: best
4	overall_score: Weak Accept (4/6)
5	timestamp: 2026-05-20T19:54:18.620914+00:00
6	---
7	
8	## Reviewer 1 (R1): Methods and Experiments
9	
10	### Summary
11	This paper systematically evaluates whether English-trained correctness probes on internal LLM representations transfer cross-lingually, across 3 architectures (Qwen3-235B, Llama 4 Scout, Gemma 4 31B), 20-52 languages, and 5 transfer conditions. It discovers a depth-transferability Pareto frontier, proposes CaCLR (a joint calibration-consistency objective), performs difficulty-capability decomposition, and extends the correctness-confidence orthogonality finding to multilingual settings.
12	
13	### Strengths
14	
15	**S1. Ambitious and well-structured experimental scope.** 10 experiment plans covering 3 architectures, up to 52 languages, multiple benchmarks, and systematic ablations. The causal chain (discovery → analysis → method → mechanism) is logically coherent. The coverage of MoE vs Dense architectures strengthens generalizability claims.
16	
17	**S2. Principled negative results honestly reported.** The consistency loss being inert (sweeping beta over 3 OOM changes AUROC <0.3pp), mean-shift failing entirely, and CaCLR never beating linear projection on cross-benchmark evaluation are all valuable findings for the community. The paper does not oversell.
18	
19	**S3. Comprehensive baseline coverage.** Five transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR) provide a fair comparison landscape. The INT8 validation ablation (cosine 0.994, 0.3pp AUROC difference) proactively addresses quantization concerns.
20	
21	**S4. The difficulty-capability decomposition (Plan 004) is methodologically interesting.** Projecting out IRT difficulty and showing this *hurts* transfer by 1.3-1.4pp is a counterintuitive and informative result that challenges the assumption of clean separability.
22	
23	### Weaknesses
24	
25	**W1. The Pareto frontier claim is architecture-dependent to the point of undermining universality.** The paper reports rho=0.41 (Qwen3), 0.22 (Llama4), 0.48 (Gemma4). A rank correlation of 0.22 explains <5% of variance and is barely meaningful. Claiming a "Pareto frontier" when the relationship is this noisy on one of three architectures weakens Claim 1 substantially. The paper should acknowledge this is a *tendency* in some architectures rather than a universal structural property.
26	
27	**W2. CaCLR's consistency loss is inert — this fundamentally undermines Claim 3.** The paper's proposed method contribution is CaCLR (L_BCE + alpha*L_SB-ECE + beta*L_consistency). If sweeping beta over 3 orders of magnitude changes AUROC by <0.3pp, and *removing* it improves by 0.2pp, then CaCLR reduces to L_BCE + L_SB-ECE, which is simply calibration-aware probe training — not a novel cross-lingual alignment method. The "consistency" component that was supposed to be the differentiator from linear projection is doing nothing. Furthermore, "CaCLR never beats linear projection" on cross-benchmark (Result 7) means the method contribution is essentially negative.
28	
29	**W3. No confidence intervals or significance tests on the key comparisons.** Effect sizes like Cohen's d=0.18 for probe complexity and the 1.3-1.4pp decomposition degradation are small. Without bootstrap CIs or paired tests across the 19/52 languages, it is impossible to assess whether these effects are reliably non-zero. The MLP transfer penalty of -0.2 to -0.4pp is tiny and may be noise.
30	
31	**W4. The "parallel activations" requirement for CaCLR is underspecified.** The consistency loss requires comparable EN and non-EN activations. How are these obtained? Translated GlobalMMLU items? If so, how is translation quality controlled? Does it require parallel corpora at inference time? This has major practical implications for the "zero target-language labels" claim — you still need parallel *inputs*, which may be harder to obtain than 25-100 labeled examples.
32	
33	**W5. Extended 52-language evaluation (Plan 009) shows 23.5% pass rate and 0% for very-low-resource.** This result significantly undermines the practical value proposition. If the method works only for languages that already have reasonable LLM coverage, the incremental value over simply collecting a few dozen labeled examples per language is questionable.
34	
35	### Questions for Authors
36	
37	Q1. What exactly are "parallel activations" for L_consistency? Are these from the same MCQA items machine-translated into each language (as in GlobalMMLU)? If so, does CaCLR require access to the evaluation benchmark's translations at training time — creating a form of test-set leakage?
38	
39	Q2. For the Pareto frontier on Llama 4 Scout (rho=0.22, non-monotonic at layers 20-28), can you provide bootstrap confidence intervals on the rank correlation? With only 12 data points, the sampling uncertainty may be substantial.
40	
41	Q3. The paper claims "projecting out difficulty hurts transfer by 1.3-1.4pp" — but over how many language-layer combinations? Is this statistically significant by a paired test? What is the variance across the 10 languages x 8 layers = 80 conditions?
42	
43	Q4. Temperature scaling T values (5-6) are extremely high, implying massive overconfidence in the raw probes. Was T optimized on held-out data or the test set? If the latter, ECE numbers are unreliable.
44	
45	Q5. How sensitive is CaCLR to the choice of alpha? You report beta is inert, but what about alpha (the SB-ECE weight)?
46	
47	### Minor Issues
48	
49	M1. Table 5 reports "Pareto frontier coherence" across 3 architectures but rho values of 0.41, 0.22, 0.48 do not constitute "coherence" in any standard sense. Revise the table title.
50	
51	M2. The 52-language extension uses only Qwen3 (from context). Cross-architecture validation at this scale would strengthen the claim.
52	
53	M3. "Orthogonality persists across 20 languages (mean cosine 0.072)" — this is interesting but somewhat expected given the finding is architectural, not language-specific. The novelty here is incremental over Miao & Ungar.
54	
55	M4. The probe complexity finding (MLP +1pp EN, -0.2 to -0.4pp transfer) with Cohen's d=0.18 is a very small effect. Consider whether this table adds value or could move to supplementary.
56	
57	M5. The paper uses GlobalMMLU, Belebele, and MMLU-ProX — all MCQA. Generalization beyond MCQA remains entirely open.
58	
59	### Score: 4 (Weak Accept)
60	
61	**Justification:** The paper addresses a timely and important question (does probe-based calibration generalize multilingually?) with thorough experimentation across architectures and languages. The systematic characterization is valuable regardless of whether CaCLR succeeds as a method. However, the method contribution (CaCLR) is effectively negative — the consistency loss is inert and the method never beats linear projection cross-benchmark. The Pareto frontier is weak on 1/3 architectures (rho=0.22). These issues reduce the paper from a strong method+discovery paper to primarily a diagnostic/characterization paper with negative results. For a top venue, the paper needs either (a) a working method that actually shifts the frontier, or (b) explicit reframing as a diagnostic study with the CaCLR negative result as a contribution. Currently it sits uncomfortably between these framings. The breadth of experiments, honest reporting of negative results, and field-level significance of answering "does this work multilingually?" push it toward acceptance at a venue like EACL, but the weak method contribution keeps it below the bar for a top ML venue.
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fad7331-1d3c-49d6-ad0b-2bbc85066a0a",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "78b1bc65-c9c7-45cb-87bb-698a266e0254",
  "sourceToolAssistantUUID": "7fad7331-1d3c-49d6-ad0b-2bbc85066a0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T21:00:24.401Z_

<details open><summary>🔧 Tool call — Read · `toolu_013gMkkjVZz7GjMrPMWAFmci`</summary>

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
  "parentUuid": "78b1bc65-c9c7-45cb-87bb-698a266e0254",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVbaMhd6aC41qVF5DZu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c7847b2-c8e1-42d0-ac1b-7784a9d44fa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cad11Gbs46MDirwZaJuo2t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 51671,
      "cache_read_input_tokens": 29852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 51671,
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

_source line 39 · 2026-05-20T21:00:24.411Z_

<details><summary>↩ Tool result · `toolu_013gMkkjVZz7GjMrPMWAFmci`</summary>

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
  "parentUuid": "4c7847b2-c8e1-42d0-ac1b-7784a9d44fa1",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "d3e44623-6e57-4f11-8557-b1d4b84de944",
  "sourceToolAssistantUUID": "4c7847b2-c8e1-42d0-ac1b-7784a9d44fa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T21:00:28.016Z_

Now let me read the distilled research and writing skill files for additional context on the literature.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3e44623-6e57-4f11-8557-b1d4b84de944",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVc3HSWwaEse8reke2W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed27ccfe-6bfa-4f63-97a4-5f347452a068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvCz3gpFnhoJJTbPnSNWdF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9179,
      "cache_read_input_tokens": 81523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9179,
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

_source line 41 · 2026-05-20T21:00:29.915Z_

<details open><summary>🔧 Tool call — Read · `toolu_017GuGoK9TmyhFhF849XyxiQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/skills/projects/xling_calib_direction/distilled-research.skill.md",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed27ccfe-6bfa-4f63-97a4-5f347452a068",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVc3HSWwaEse8reke2W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36240079-88c1-415f-801e-68c689b961c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvCz3gpFnhoJJTbPnSNWdF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9179,
      "cache_read_input_tokens": 81523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9179,
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

_source line 42 · 2026-05-20T21:00:29.929Z_

<details><summary>↩ Tool result · `toolu_017GuGoK9TmyhFhF849XyxiQ`</summary>

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
  "parentUuid": "36240079-88c1-415f-801e-68c689b961c4",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "dd0d706c-9886-4fe5-97d0-500dde41585a",
  "sourceToolAssistantUUID": "36240079-88c1-415f-801e-68c689b961c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T21:00:30.665Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TdTFbzBeJjkdXMF2VqnPPV`</summary>

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
  "parentUuid": "dd0d706c-9886-4fe5-97d0-500dde41585a",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVc3HSWwaEse8reke2W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18c56efa-16b2-4d73-9a43-7347d775ebdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvCz3gpFnhoJJTbPnSNWdF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9179,
      "cache_read_input_tokens": 81523,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9179
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 81523,
          "cache_creation_input_tokens": 9179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9179,
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

_source line 44 · 2026-05-20T21:00:30.671Z_

<details><summary>↩ Tool result · `toolu_01TdTFbzBeJjkdXMF2VqnPPV`</summary>

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
  "parentUuid": "18c56efa-16b2-4d73-9a43-7347d775ebdf",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "e8252ee7-0e3d-4f8c-97de-3952b1913cb9",
  "sourceToolAssistantUUID": "18c56efa-16b2-4d73-9a43-7347d775ebdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-20T21:00:35.761Z_

Now I have a comprehensive understanding of the paper, the experimental setup, the prior reviews, and the literature landscape. Let me also check the first dream report's paper (the earlier version that got the earlier review) to understand how the paper evolved.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8252ee7-0e3d-4f8c-97de-3952b1913cb9",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVcVt6R6fx5iFvY9PCT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50262198-925b-4b2d-ad4b-7921df1299dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoAs2JjfnBMqjSdoWurCHw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5272,
      "cache_read_input_tokens": 90702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5272,
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

_source line 46 · 2026-05-20T21:00:38.131Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PqrTE8qqJJt8AiytKs5cJS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T185641/best/paper.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50262198-925b-4b2d-ad4b-7921df1299dc",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVcVt6R6fx5iFvY9PCT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2f7f15e-1a60-42ca-aa09-62d13e86c868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CoAs2JjfnBMqjSdoWurCHw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5272,
      "cache_read_input_tokens": 90702,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5272
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 90702,
          "cache_creation_input_tokens": 5272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5272,
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

_source line 47 · 2026-05-20T21:00:38.136Z_

<details><summary>↩ Tool result · `toolu_01PqrTE8qqJJt8AiytKs5cJS`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2f7f15e-1a60-42ca-aa09-62d13e86c868",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "52608f89-1bfd-40f1-b238-d3cc164f460c",
  "sourceToolAssistantUUID": "f2f7f15e-1a60-42ca-aa09-62d13e86c868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-20T21:00:41.209Z_

I now have sufficient information to write a thorough R2 review. Let me also check one more thing -- the experiment data to verify the numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52608f89-1bfd-40f1-b238-d3cc164f460c",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVd3tSMamQMqpfdgjng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d9f9699-ef6c-4764-bf08-cea8b06fc061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn4CUc79fUaSCME1p14uiz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 95974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1256,
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

_source line 49 · 2026-05-20T21:00:41.851Z_

<details open><summary>🔧 Tool call — Read · `toolu_016xErpBufMRDBMyjqmqv3FT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/experiment_data.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d9f9699-ef6c-4764-bf08-cea8b06fc061",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVd3tSMamQMqpfdgjng",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36b67f21-c5c3-4556-85f7-6beb8405ec98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn4CUc79fUaSCME1p14uiz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 95974,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1256
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 95974,
          "cache_creation_input_tokens": 1256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1256,
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

_source line 50 · 2026-05-20T21:00:41.855Z_

<details><summary>↩ Tool result · `toolu_016xErpBufMRDBMyjqmqv3FT`</summary>

```text
1	[
2	  {
3	    "name": "Full Pareto Frontier — Qwen3-235B-A22B",
4	    "description": "94-layer MoE model, INT8, 24 probed layers (every 4th), 20 languages, 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR).\n",
5	    "results": {
6	      "en_best_auroc": 0.838,
7	      "en_best_layer": 76,
8	      "en_best_ece_raw": 0.162,
9	      "en_best_ece_tempcal": 0.048,
10	      "temp_scaling_T": 4.83,
11	      "en_auroc_range": [
12	        0.592,
13	        0.838
14	      ],
15	      "optimal_transfer_layer_median": 56,
16	      "zs_transfer_auroc_median_20lang": 0.758,
17	      "zs_transfer_auroc_at_en_optimal_layer76": 0.714,
18	      "zs_transfer_auroc_at_transfer_optimal_layer56": 0.771,
19	      "pareto_rho_global": -0.81,
20	      "pareto_rho_per_lang_median": -0.78,
21	      "pareto_rho_per_lang_iqr": [
22	        -0.84,
23	        -0.71
24	      ],
25	      "zs_langs_above_0p65_out_of_20": 17,
26	      "best_zs_auroc_by_tier": {
27	        "HIGH_zh": 0.793,
28	        "HIGH_es": 0.801,
29	        "HIGH_fr": 0.798,
30	        "HIGH_de": 0.784,
31	        "MID_hi": 0.742,
32	        "MID_ru": 0.769,
33	        "MID_ko": 0.751,
34	        "MID_tr": 0.738,
35	        "LOW_sw": 0.641,
36	        "LOW_bn": 0.633
37	      },
38	      "mean_shift_delta_auroc_median": 0.0,
39	      "linear_proj_delta_auroc_over_zs_median": 0.048,
40	      "fewshot_25_delta_auroc_over_zs_median": 0.032,
41	      "fewshot_100_delta_auroc_over_zs_median": 0.055
42	    },
43	    "tables": [
44	      {
45	        "name": "Table 1: Qwen3-235B Pareto Frontier — EN AUROC vs ZS Transfer AUROC by Layer",
46	        "columns": [
47	          "layer",
48	          "depth_pct",
49	          "en_auroc",
50	          "zs_median_auroc",
51	          "zs_min_auroc",
52	          "zs_max_auroc",
53	          "rho_median"
54	        ],
55	        "rows": [
56	          [
57	            0,
58	            0,
59	            0.592,
60	            0.583,
61	            0.521,
62	            0.601,
63	            null
64	          ],
65	          [
66	            8,
67	            9,
68	            0.631,
69	            0.618,
70	            0.554,
71	            0.639,
72	            null
73	          ],
74	          [
75	            16,
76	            17,
77	            0.672,
78	            0.659,
79	            0.589,
80	            0.678,
81	            null
82	          ],
83	          [
84	            24,
85	            26,
86	            0.711,
87	            0.698,
88	            0.621,
89	            0.719,
90	            null
91	          ],
92	          [
93	            32,
94	            34,
95	            0.738,
96	            0.729,
97	            0.648,
98	            0.751,
99	            null
100	          ],
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36b67f21-c5c3-4556-85f7-6beb8405ec98",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "b03db14b-76b4-4c72-b5bf-3329faa94722",
  "sourceToolAssistantUUID": "36b67f21-c5c3-4556-85f7-6beb8405ec98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-20T21:00:44.850Z_

Now let me also load the submission tool to post the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b03db14b-76b4-4c72-b5bf-3329faa94722",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVdKnALnEkMtAi54YmD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f84ff998-b9da-4134-888d-bec4a275233a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZA13njZpZ7svSTRr1aZQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1314,
      "cache_read_input_tokens": 97230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1314,
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

_source line 52 · 2026-05-20T21:00:45.165Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013CFxxguKcc2dmBxgh3FYnX`</summary>

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
  "parentUuid": "f84ff998-b9da-4134-888d-bec4a275233a",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVdKnALnEkMtAi54YmD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d855e4e3-d0b5-44a3-b3c9-b9ca176d1e6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ZA13njZpZ7svSTRr1aZQT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1314,
      "cache_read_input_tokens": 97230,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1314
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 97230,
          "cache_creation_input_tokens": 1314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1314,
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

_source line 53 · 2026-05-20T21:00:45.167Z_

<details><summary>↩ Tool result · `toolu_013CFxxguKcc2dmBxgh3FYnX`</summary>

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
  "parentUuid": "d855e4e3-d0b5-44a3-b3c9-b9ca176d1e6b",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "b2f72122-9f6d-4f37-8025-5519c12dc7cf",
  "sourceToolAssistantUUID": "d855e4e3-d0b5-44a3-b3c9-b9ca176d1e6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-20T21:00:48.322Z_



Now I have thoroughly reviewed all materials. Let me compile and submit the R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2f72122-9f6d-4f37-8025-5519c12dc7cf",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVdZtyRD3b18p1SSJ9f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ec8de57-5ba8-4c0a-be93-08428c4d6760",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHeZM8XGA2U1Nd2fXHy5x4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 98544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 727,
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

_source line 55 · 2026-05-20T21:02:51.025Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01DCdEpUXd7DkhZAAXmCWzwr`</summary>

```json
{
  "report": "---\ndream_id: dream_20260520T201854\ntier: best\noverall_score: Weak Accept (4/6)\ntimestamp: 2026-05-20\n---\n\n## Reviewer 2 (R2): Novelty, Positioning, and Related Work\n\n### Summary\n\nThis paper presents a systematic study of cross-lingual correctness probe transfer across 20 languages on two MoE architectures (Qwen3-235B, Llama 4 Scout), with Gemma 4 31B Dense in the appendix. It discovers a depth-transferability Pareto frontier with architecture-dependent shape, decomposes correctness transfer into difficulty-shared and capability-specific components, proposes CaCLR (a composite training objective with MMD consistency loss), confirms cross-lingual correctness-confidence orthogonality, and uses CKA to mechanistically link representation geometry to transfer success. Compared to the earlier draft reviewed in Round 0, this version has substantially improved: the abstract numbers are now internally consistent, statistical tests are present (bootstrap CIs, permutation tests, Cohen's d), the related work is properly structured with seven subsections, and the paper includes a beta sensitivity sweep. However, several novelty and positioning concerns remain.\n\n---\n\n### 1. Novelty Assessment\n\n**Claim 1: \"First systematic study of cross-lingual correctness probe transfer\"**\n\n*Verdict: Partially novel, carefully scoped.*\n\nThe \"first\" claim is defensible when restricted to *correctness* probes (output-dependent accuracy prediction) as distinct from knowledge-boundary probes (Xiao et al., input-level answerability) and difficulty probes (Civelli et al., item property). The paper correctly identifies this distinction. However, the underlying phenomenon — that deeper layers are more language-specific and shallower/middle layers transfer better — is well-established since Pires et al. (2019) and Conneau et al. (2020) on multilingual BERT. The contribution is therefore the *quantification* of this known tendency for the specific case of correctness probes on frontier-scale MoE models, not the discovery of a new phenomenon. Significance: moderate. The Pareto framing adds analytical value but the core observation is predictable from prior work.\n\n**Claim 2: Pareto frontier discovery (depth vs. transferability tradeoff)**\n\n*Verdict: Incremental quantification of a known trend.*\n\nThe depth-transfer anticorrelation (Spearman rho = -0.78/-0.73) is a clean quantification but not surprising. Joshi et al. (2025) already identified layer-depth effects on calibration directions; Zhou et al. (2025, LACE) showed non-English calibration peaks at intermediate layers; Civelli et al. (2026) found architecture-dependent optimal depth for difficulty probes at 24-49%. The Pareto framing is a useful analytical lens but the underlying observation is convergent with multiple prior findings. Delta over closest work (Civelli): the new element is correctness-specific (vs. difficulty) with calibration metrics (vs. probing accuracy), but the qualitative finding is the same.\n\n**Claim 3: Architecture-dependent frontier shape (MoE vs dense)**\n\n*Verdict: The most novel empirical contribution, but underpowered.*\n\nThe observation that MoE models show sharper Pareto elbows (60%, 50%) than dense models (75%) with expert routing as the proposed mechanism is genuinely interesting and not directly predicted by prior work. However, the evidence base is thin: 2 MoE models + 1 dense model (and the dense model is in the appendix only). The three models also differ in total parameters (235B, 109B, 31B), number of layers (94, 48, 60), and training data — making it impossible to attribute the frontier shape difference solely to MoE vs. dense architecture. The \"expert routing drives language specialization\" hypothesis is stated but not tested (e.g., no analysis of expert activation patterns by language). This claim would be substantially strengthened by: (a) a dense model of comparable scale to the MoE models, or (b) direct analysis of expert routing patterns across languages at different depths.\n\n**Claim 4: Difficulty-capability decomposition**\n\n*Verdict: Methodologically interesting, moderate novelty.*\n\nUsing IRT difficulty probes as a control to decompose the correctness signal is a well-designed ablation. The finding that removing difficulty improves transfer by 3.1pp (with low-resource languages benefiting most at +4.1pp) is informative. The random-direction control (+0.2pp) validates specificity. However, this builds directly on Civelli et al.'s cross-lingual difficulty probes — the novelty is in the *interaction* (difficulty removal improves correctness transfer) rather than in the decomposition framework itself. The cosine similarity of 0.34 between difficulty and correctness directions is a useful quantification. Significance: moderate-to-good as an analytical tool.\n\n**Claim 5: CaCLR as a method contribution**\n\n*Verdict: Limited novelty as a method; moderate value as a diagnostic.*\n\nCaCLR combines three well-known components: binary cross-entropy (standard), SB-ECE (Karandikar et al. 2021), and MMD (standard domain adaptation loss). The combination is sensible but not theoretically motivated beyond intuition. The key question is whether the MMD consistency term (beta) adds value, and the paper shows it does (+3.2pp over alpha-only, p=0.003, d=0.48). This is a meaningful positive result. However, CaCLR's advantage over linear projection is only +1.4pp, and linear projection requires only 50 parallel pairs while CaCLR requires parallel inputs for all training data. The cost-benefit tradeoff is not compelling. CaCLR's depth-dependent effectiveness (strong at mid-depth, weak at deep layers where geometric misalignment dominates) is the more interesting finding — it reveals *what kind* of misalignment exists at different depths, which is analytically valuable even if the method itself is incremental.\n\n**Claim 6: Universal cross-lingual orthogonality**\n\n*Verdict: Straightforward extension with limited novelty.*\n\nExtending Miao & Ungar's English-only finding (cosine < 0.04) to 20 languages and two architectures (max cosine = 0.062) is useful verification but methodologically identical to the original work. The resource-tier gradient (low-resource languages show slightly higher cosine) is a minor nuance. The paper correctly frames this as bounding output-based calibration universally, but the contribution is empirical verification, not conceptual advance.\n\n---\n\n### 2. Related Work Completeness\n\nThe current version (7 subsections) is a major improvement over the earlier draft (15 lines). However, several gaps remain:\n\n**Missing references that should be cited:**\n\n1. **Conneau et al. (2020), \"Unsupervised Cross-lingual Representation Learning at Scale\"** — Foundational work on XLM-R showing layer-wise cross-lingual alignment. The paper's entire premise rests on phenomena first characterized here. Must cite.\n\n2. **Pires et al. (2019), \"How multilingual is Multilingual BERT?\"** — Original observation that deeper layers are more language-specific. The Pareto frontier is a quantification of their qualitative finding. Must cite.\n\n3. **Chi et al. (2020), \"Finding Universal Grammatical Relations in Multilingual BERT\"** — Cross-lingual probing showing shared syntactic structure in middle layers. Relevant to the claim about language-agnostic subspaces.\n\n4. **Belinkov (2022), \"Probing Classifiers: Promises, Shortcomings, and Advances\"** — Standard probing methodology survey. The paper uses probing extensively but does not cite this.\n\n5. **Keleg & Magdy (2023), \"On the Calibration of Massively Multilingual Language Models\"** — Directly relevant: multilingual calibration study. Should be discussed alongside LACE.\n\n6. **Gretton et al. (2012), \"A Kernel Two-Sample Test\"** — Original MMD paper. CaCLR uses MMD as a core component but does not cite the source.\n\n7. **Long et al. (2015), DAN / Ganin et al. (2016), DANN / Sun & Saenko (2016), Deep CORAL** — Applied domain adaptation methods using MMD or similar distributional matching in neural networks. CaCLR's consistency loss is structurally equivalent to these. The connection should be explicit.\n\n8. **Voita & Titov (2020), \"Information-Theoretic Probing with Minimum Description Length\"** — The paper mentions MDL probes in the framing document but does not include them in the paper. Given the probing methodology discussion, this is relevant.\n\n**On the differentiation from Xiao et al.:**\n\nThe distinction (knowledge boundary = input-level answerability vs. correctness = output-dependent accuracy) is well-articulated and convincing. The formal proof that mean-shift cannot improve AUROC under StandardScaler + logistic regression is a nice methodological contribution that strengthens the differentiation. This is one of the paper's cleanest contributions.\n\n**On the differentiation from Miao & Ungar:**\n\nAdequate but minimal. The paper extends their finding to 20 languages and two architectures. The differentiation is honest — this is verification at scale, not a new finding. The resource-tier gradient is the only new nuance.\n\n---\n\n### 3. Positioning and Framing\n\n**Is the \"causal chain\" framing convincing?**\n\nPartially. The chain (Pareto frontier -> decomposition explains it -> CaCLR shifts it -> orthogonality bounds alternatives) is narratively elegant and the CKA analysis does serve as mechanistic glue. However, the chain has a weak link: the decomposition (Claim 2) does not directly *cause* or *motivate* CaCLR (Claim 3). CaCLR uses MMD on activations, not difficulty-projected residuals. The decomposition tells us *why* transfer degrades (difficulty entanglement) but CaCLR does not directly address this (it does distributional alignment, not difficulty removal). The paper would be more honest to present the decomposition and CaCLR as complementary analyses rather than a causal chain.\n\n**Does the paper oversell or undersell?**\n\nThe paper generally avoids the overselling problems of the earlier draft (the abstract numbers now match the text; \"first systematic study\" is appropriately scoped). However, CaCLR is still positioned more as a method contribution than it warrants. The 3.5% ECE improvement over temperature scaling and +1.4pp over linear projection are real but modest, especially given that CaCLR requires parallel inputs for all training data while linear projection needs only 50 pairs. The paper would be stronger if it explicitly acknowledged CaCLR as a *diagnostic tool* that reveals the nature of cross-lingual misalignment (distributional vs. geometric) rather than primarily as a practical method.\n\n**Is the \"architecture-dependent\" claim well-supported with 2+1 data points?**\n\nNo. Two MoE models and one dense model (in the appendix) that differ in scale, depth, and training data cannot isolate architecture type as the causal variable. The claim should be softened to \"architecture-correlated\" or \"we observe that MoE and dense models show different frontier shapes, consistent with but not conclusively caused by expert routing.\" The current framing (\"MoE expert routing accelerates deep-layer language specialization\") is stated as a mechanism but tested only as a correlation across 3 confounded data points.\n\n---\n\n### 4. Significance and Impact\n\n**Would this change how practitioners do multilingual calibration?**\n\nModestly. The main actionable finding is layer selection: practitioners should use probes at 50-75% depth (architecture-dependent) rather than the final layer. This is useful but unsurprising advice. CaCLR provides a marginal improvement (+1.4pp over 50-pair linear projection) at higher cost. The more practical takeaway is that linear projection with ~50 parallel pairs is a strong, simple baseline — this is arguably the paper's most useful practical contribution, though not positioned as such.\n\n**Target audience:**\n\nThe paper sits at the intersection of multilingual NLP and mechanistic calibration. The Pareto frontier analysis and CKA mechanistic explanation are most valuable for researchers studying multilingual representations. The CaCLR method has limited practical impact. The orthogonality extension is most relevant to the calibration research community. Overall, this is primarily a research/analysis paper that happens to include a method, not a method paper that includes analysis.\n\n**Is 3.5% ECE improvement over temperature scaling meaningful?**\n\nIn absolute terms, it is modest. Temperature scaling itself already reduces ECE substantially (from 0.162 to 0.048 on Qwen3 English). The 3.5% improvement is relative to temperature scaling's already-calibrated output. For non-English languages where raw ECE is much worse (up to 5x), the improvement may be more practically meaningful — but the paper does not report the absolute ECE values for non-English languages under CaCLR, making it hard to assess practical impact. A table showing raw ECE -> temp scaling ECE -> CaCLR ECE for representative languages would be much more informative than the relative \"3.5% improvement\" framing.\n\n---\n\n### 5. Weaknesses\n\n**W1. Architecture-dependent claim is underpowered.** Three models (2 MoE + 1 dense) that differ in scale, depth, training data, and architecture cannot isolate architecture as the causal variable. The \"expert routing drives language specialization\" hypothesis is untested — no analysis of actual expert activation patterns. The dense model (Gemma 4 31B) is only in the appendix and is 7-8x smaller than the MoE models, confounding scale with architecture type.\n\n**W2. CaCLR's practical value proposition is weak relative to its complexity.** CaCLR requires parallel inputs for all training items, while linear projection needs only 50 parallel pairs to reach 98% of 200-pair performance. CaCLR's advantage is +1.4pp median AUROC. The cost-benefit analysis favors linear projection in most practical scenarios, yet CaCLR is framed as the paper's method contribution.\n\n**W3. Missing foundational references weaken positioning claims.** The paper does not cite Conneau et al. (2020), Pires et al. (2019), or Chi et al. (2020) — foundational cross-lingual probing works that established the phenomena this paper builds upon. The MMD loss is used without citing Gretton et al. (2012), and the connection to applied domain adaptation methods (DAN, DANN, Deep CORAL) is not made. These omissions make the related work appear incomplete despite its improved structure.\n\n**W4. The causal chain narrative has a weak link.** The decomposition (Claim 2) identifies difficulty entanglement as a transfer degradation mechanism, but CaCLR (Claim 3) does not directly address this — it uses MMD on raw activations, not difficulty-projected residuals. The paper does not test whether combining decomposition + CaCLR (i.e., applying CaCLR on difficulty-removed representations) yields further improvements, which would strengthen the causal chain.\n\n**W5. Non-English ECE improvements are reported only in relative terms.** \"3.5% over temperature scaling\" conceals the actual calibration quality. Without absolute ECE values per language under each method, reviewers cannot assess whether the resulting calibration is practically useful. The paper reports English ECE in detail (raw 0.162, post-temp 0.048) but not the equivalent for non-English languages.\n\n**W6. The orthogonality extension (Claim 4) is empirical verification, not a contribution.** Applying the same methodology as Miao & Ungar to more languages yields a predictable result. The cosine values (0.031-0.062) are slightly higher than the English baseline (0.031-0.037) but all remain near-orthogonal. The resource-tier gradient is the only nuance. This should be presented as a verification experiment, not a numbered contribution.\n\n**W7. MCQA-only evaluation limits generalizability.** All three benchmarks (GlobalMMLU, Belebele, MMLU-ProX) are multiple-choice QA. Correctness labeling is straightforward for MCQA but the paper's findings may not extend to open-ended generation, where \"correctness\" is ambiguous. The paper acknowledges this but the scope limitation is substantial given the generality of the claims.\n\n**W8. CKA analysis is correlational, not causal.** The paper states CKA \"mechanistically explains\" the Pareto frontier, but CKA is a correlation measure between representation matrices. The r=0.82 correlation between CKA and transfer AUROC is informative but does not establish mechanism. A causal claim would require intervention (e.g., showing that artificially increasing cross-lingual CKA at deep layers improves transfer). The distinction between \"distributional\" and \"geometric\" misalignment (Section 5.5) is insightful but also correlational — the 15-35 degree rotation claim would benefit from direct measurement rather than inference from CKA patterns.\n\n---\n\n### 6. Questions for Authors\n\n1. Have you tested CaCLR on difficulty-removed representations? If decomposition identifies difficulty entanglement as the problem and CaCLR addresses distributional misalignment, combining them should be strictly better. The absence of this experiment weakens the causal chain narrative.\n\n2. Can you provide a table of absolute ECE values (not relative improvements) for representative languages under each method (raw, temperature scaling, CaCLR, linear projection)? This is essential for assessing practical impact.\n\n3. For the architecture-dependent claim: have you considered including a dense model of comparable scale (e.g., Llama-3.1-70B or similar) to disentangle scale from architecture type? With the current setup, Gemma 4 31B being both smaller and denser makes the comparison confounded.\n\n4. The \"expert routing drives language specialization\" hypothesis — is there any direct evidence from expert activation analysis? Even a preliminary analysis showing that specific experts activate preferentially for specific languages at deep layers would substantially strengthen this claim.\n\n5. Table 1 shows that at Qwen3 layer 48 (51% depth), ZS median AUROC = 0.771, identical to layer 56 (60% depth). Why is layer 56 identified as the \"optimal transfer layer\" rather than layer 48, which achieves the same transfer AUROC with lower depth? Is the tie-breaking criterion EN AUROC?\n\n6. The mean-shift invariance proof (Section 3.2) is clean and valuable. Has this observation been noted in the Xiao et al. context? If their mean-shift alignment shows improvements under different metrics/pipelines, the difference in preprocessing (StandardScaler) may be the key factor — worth discussing explicitly.\n\n7. How were IRT difficulty parameters estimated? From English data only, or jointly across languages? If English-only, is the difficulty direction truly language-agnostic, or does it reflect English-specific difficulty structure?\n\n8. The paper claims CaCLR requires \"zero target-language labels\" but needs parallel inputs from GlobalMMLU train-split translations. How many parallel items are used? Is this requirement realistically different from collecting 50-100 parallel pairs for linear projection?\n\n---\n\n### 7. Score and Confidence\n\n**Score: 4 / 6 (Weak Accept)**\n\n**Confidence: 4 / 5**\n\n**Justification:**\n\nThis paper addresses a genuinely important question — whether probe-based calibration extends beyond English — with systematic experiments at commendable scale (20 languages, 2-3 architectures, 3 benchmarks, multiple transfer conditions). The depth-transferability characterization, difficulty-capability decomposition, and CKA mechanistic analysis collectively provide useful insights for the multilingual NLP community. The paper has substantially improved from the earlier draft: statistical tests are present, abstract numbers are consistent, and related work is structured.\n\nHowever, novelty is limited. The core finding (deeper layers transfer worse cross-lingually) is a quantification of known phenomena. CaCLR is a competent combination of existing components but offers marginal practical advantage over simpler baselines (linear projection). The architecture-dependent claim is underpowered (3 confounded models). The orthogonality extension is empirical verification. The paper's strongest contributions are analytical (decomposition, CKA analysis, mean-shift invariance proof) rather than methodological (CaCLR).\n\nFor EACL 2027, this is a borderline paper. It would be strengthened by: (1) reframing as primarily an analysis/characterization paper with CaCLR as a secondary contribution; (2) adding a comparable-scale dense model to support the architecture claim; (3) testing the decomposition + CaCLR combination; and (4) reporting absolute ECE values. The scale and thoroughness of the experiments push it toward acceptance; the limited novelty of individual contributions pulls it back. On balance, a weak accept — the field benefits from having this systematic characterization even if no single finding is a breakthrough.",
  "project": "xling_calib_direction",
  "tier": "best",
  "dream_id": "dream_20260520T201854",
  "overall_score": "Weak Accept (4/6)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ec8de57-5ba8-4c0a-be93-08428c4d6760",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVdZtyRD3b18p1SSJ9f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f918b92c-1ca9-4308-bda0-68fcb1a87a70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHeZM8XGA2U1Nd2fXHy5x4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 98544,
      "output_tokens": 5147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 727
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5147,
          "cache_read_input_tokens": 98544,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 727,
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

_source line 56 · 2026-05-20T21:02:54.122Z_

<details><summary>↩ Tool result · `toolu_01DCdEpUXd7DkhZAAXmCWzwr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/best/review_report.md\", \"dream_id\": \"dream_20260520T201854\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f918b92c-1ca9-4308-bda0-68fcb1a87a70",
  "isSidechain": true,
  "promptId": "248aeb9c-3304-4117-b59f-e1434de9c70f",
  "agentId": "a608204260859e5b5",
  "type": "user",
  "uuid": "9fc70f22-0c26-4f6c-8943-01bba0c9b19e",
  "sourceToolAssistantUUID": "f918b92c-1ca9-4308-bda0-68fcb1a87a70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-20T21:03:09.020Z_

Review submitted. Here is a summary of the R2 review:

**Overall Score: 4/6 (Weak Accept), Confidence 4/5**

**Key findings from the review:**

**Novelty Assessment (by claim):**
- **Claim 1 (First systematic study):** Defensible when narrowly scoped to correctness probes, but the underlying depth-transfer phenomenon is well-established since Pires et al. (2019) and Conneau et al. (2020).
- **Claim 2 (Pareto frontier):** Incremental quantification of a known trend. Civelli et al. (2026) already found architecture-dependent optimal depth for cross-lingual probes.
- **Claim 3 (Architecture-dependent shape):** The most novel empirical contribution, but underpowered -- 3 confounded models (differing in scale, depth, training data, and architecture) cannot isolate architecture type as causal.
- **Claim 4 (Decomposition):** Methodologically interesting, builds directly on Civelli et al. The interaction finding (difficulty removal improves correctness transfer) is the novel element.
- **Claim 5 (CaCLR):** Limited novelty as a method (3 known loss components combined), but the beta sensitivity analysis revealing depth-dependent effectiveness is analytically valuable. The +1.4pp advantage over 50-pair linear projection at higher data cost weakens the practical value proposition.
- **Claim 6 (Orthogonality):** Straightforward extension of Miao & Ungar -- empirical verification, not conceptual advance.

**Major weaknesses:**
1. Architecture claim underpowered (3 confounded models)
2. CaCLR's practical value weak vs. linear projection simplicity
3. Missing foundational references (Conneau 2020, Pires 2019, Gretton 2012)
4. Causal chain has a weak link (decomposition does not directly motivate CaCLR)
5. Non-English ECE reported only in relative terms
6. CKA analysis is correlational, not causal despite "mechanistic" framing

**Bottom line:** The paper's strongest contributions are analytical (decomposition, CKA analysis, mean-shift invariance proof), not methodological (CaCLR). Reframing as primarily an analysis/characterization paper would better match the actual contributions. The scale and thoroughness earn a weak accept despite limited per-claim novelty.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fc70f22-0c26-4f6c-8943-01bba0c9b19e",
  "isSidechain": true,
  "agentId": "a608204260859e5b5",
  "requestId": "req_011CbEVo59NABE7kn53xu3JC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dd4ab33-e7cb-443c-a3d3-827dc8604589",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "d1221443-c15e-4888-b9c9-64cd2c74844d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WW2cseaZUdntF2Tn1pHLyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5278,
      "cache_read_input_tokens": 99271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5278,
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
