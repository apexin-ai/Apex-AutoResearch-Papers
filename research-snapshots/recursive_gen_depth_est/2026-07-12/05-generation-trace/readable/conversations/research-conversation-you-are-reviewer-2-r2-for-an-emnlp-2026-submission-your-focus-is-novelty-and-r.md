# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 submission. Your focus is **Novelty and Related Work**. ## ARR Scoring Rubric 

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4a999f45f22fea9d.jsonl`
- **Structured JSON:** [`d2861380f568d0cd99bc.json`](../../sessions/d2/d2861380f568d0cd99bc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-14T15:00:29.678Z_

You are Reviewer 2 (R2) for an EMNLP 2026 submission. Your focus is **Novelty and Related Work**.

## ARR Scoring Rubric
- Soundness (1-5, half-point increments): 5=Excellent/most thorough, 4=Strong/sufficient for all claims, 3=Acceptable/sufficient for main claims, 2=Poor/main claims not sufficiently supported, 1=Major issues
- Excitement (1-5): 5=Highly exciting, 4=Exciting, 3=Interesting, 2=Potentially interesting, 1=Not exciting
- Overall (1-5): 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit

## Paper Summary
**Title**: "Measuring the Limits of Recursive Generation Depth Estimation: A Depth Degradation Atlas Across Models and Decoding Strategies"

The paper formalizes "ordinal generation depth estimation" as a new task — predicting how many recursive generation cycles text has undergone (depth 0=human through depth 5). The two primary contributions are:
1. **Depth Degradation Atlas**: systematic mapping of 19 statistical features across recursive depths, stratified by model and decoding strategy
2. **Effective Discriminable Depth (EDD)**: metric defined as max depth d* where all adjacent pairs (d, d+1) for d < d* have AUC > 0.70. Finding: EDD=2 in 7/9 combinations.

The paper reframes depth estimation from a classification engineering problem to a measurement science problem, arguing the bottleneck is signal availability, not methodology.

## Related Work Section (§2, very brief)
Three subsections:
1. **AI-Generated Text Detection**: DetectGPT [3], Fast-DetectGPT [4], intrinsic dimension [5], Binoculars [6], EditLens [7] — all binary, none address ordinal depth
2. **Model Collapse and Recursive Degradation**: Shumailov et al. [1] (Nature, model collapse), Drayson et al. [2] (EMNLP 2025, empirical study of recursive chains, non-monotonic degradation). Paper positions itself as studying depth *inference* from text alone vs. these works that assume depth is known.
3. **Ordinal Classification**: CORAL [8], CLOC [9]. DCOL is adapted from CLOC.

**Total references: 9.** This is extremely thin for an EMNLP submission (typical: 30-50 refs).

## Key Claims
1. EDD=2 is the dominant regime — beyond depth 2, adjacent depths are statistically indistinguishable
2. Depth signals are model-specific — cross-model transfer drops to 33%, Kendall's τ=0.52 for feature rankings
3. Actionable granularity is ternary — human/first-gen/deep recursive at 73% accuracy
4. Signal bottleneck, not methodology bottleneck — DCOL vs CORAL not significant (p=0.12)
5. Model fingerprinting needed as preprocessing for deployment

## Missing Literature (that should be cited/discussed)
Based on my knowledge of the field, the paper appears to miss:
- Data contamination / web-scale synthetic content studies
- Watermarking literature (provenance tracking alternative)
- Data curation/filtering methods (DSIR, QuRating, D4, etc.)
- More model collapse work (beyond 2 papers)
- Training data attribution / membership inference
- Text quality estimation literature
- More ordinal classification/regression methods
- Source attribution / authorship attribution

## Paper Statistics
- 11 pages, 13 tables, 0 figures, 9 references
- Models: Pythia-1.4B, OLMo-1B, GPT-2 XL (all ≤1.5B scale)
- Features: 19 hand-crafted statistical features

## Your Task
Write a detailed R2 review focusing on:
1. Novelty of the task formulation and contributions
2. Adequacy and coverage of related work
3. Positioning relative to existing literature
4. Whether the paper sufficiently distinguishes itself from prior work
5. Significance and potential impact of the findings
6. Whether the "measurement science" framing is convincing

Structure your review as:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: Major/Minor)
- Missing related work (specific papers/areas)
- Questions for authors
- Scores: Soundness, Excitement, Overall (with brief justification)

Be rigorous but fair. Evaluate whether this paper makes a sufficient contribution for EMNLP 2026 (acceptance rate ~22-25%).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "8aecc36c-e83c-4b5f-bcaf-3a2c9b4f23a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T15:00:29.684Z_

```json
{
  "parentUuid": "8aecc36c-e83c-4b5f-bcaf-3a2c9b4f23a1",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
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
  "uuid": "5b0210c4-19f9-409a-a17c-b52b1959d81d",
  "timestamp": "2026-05-14T15:00:29.684Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T15:00:34.899Z_



I'll start by reading the paper and related project files to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b0210c4-19f9-409a-a17c-b52b1959d81d",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fJhcANF7NuD5f1AHNr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46a96fa5-1615-4123-9d62-b8adb194d5d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162VxPn26BuCSdvJ1W1m32V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7020,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7020,
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

_source line 4 · 2026-05-14T15:00:35.189Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XstQ97ZAamPQU7b8zcdHWH`</summary>

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
  "parentUuid": "46a96fa5-1615-4123-9d62-b8adb194d5d8",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fJhcANF7NuD5f1AHNr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2440911b-2046-4186-b426-ee406f9698bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162VxPn26BuCSdvJ1W1m32V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7020,
      "cache_read_input_tokens": 8251,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 7020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7020,
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

_source line 5 · 2026-05-14T15:00:35.193Z_

<details><summary>↩ Tool result · `toolu_01XstQ97ZAamPQU7b8zcdHWH`</summary>

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
  "parentUuid": "2440911b-2046-4186-b426-ee406f9698bc",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "a3d24a09-3ae6-415c-9506-8784104b87b0",
  "sourceToolAssistantUUID": "2440911b-2046-4186-b426-ee406f9698bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T15:00:38.612Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Nc3Y5daHhzfUjYguob2win`</summary>

```json
{
  "project": "recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3d24a09-3ae6-415c-9506-8784104b87b0",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fK7EULX1pipccDcnfV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56891d18-2f8d-46f1-aeac-775a9fc621c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALcubop1e8nuZPZafgwiWM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-14T15:00:38.675Z_

<details><summary>↩ Tool result · `toolu_01Nc3Y5daHhzfUjYguob2win`</summary>

```text
{"result":"# 项目 recursive_gen_depth_est 概况\n\n## 实验状态 (14 个)\n\n- **pythia_temp09_001**: RUNNING — \n- **cross_model_olmo_002**: PREPARING — \n- **cross_model_olmo_001**: DONE (failed) — \n- **pythia_topk50_001**: PREPARING — \n- **cross_model_gpt2xl_001**: RUNNING — \n- **mvp_pipeline_pythia_002**: DONE (success) — \n- **mvp_pipeline_qwen_base_004**: DONE (killed) — \n- **mvp_pipeline_pythia_001**: DONE (killed) — \n- **mvp_pipeline_base_002**: DONE (killed) — \n- **mvp_pipeline_003**: DONE (killed) — \n- **mvp_pipeline_002**: DONE (killed) — \n- **mvp_pipeline_001**: DONE (killed) — \n- **mvp_pipeline_base_003**: DONE (killed) — \n- **mvp_pipeline_004**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| pythia_temp09_001 | 解码策略鲁棒性: Pythia-1.4B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化 | — | — | — |\n| cross_model_gpt2xl_001 | — | — | — | — |\n\n## 待处理\n- cross_model_olmo_002: 跨模型泛化: OLMo-1B 递归生成的统计特征与 Pythia-1.4B 一致，支持深度估计跨模型迁移 (重跑 olmo_001, 修复脚本 bug)（准备中）\n- pythia_topk50_001: 解码策略鲁棒性: Pythia-1.4B 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化（准备中）\n\n## 近期结论\n- **cross_model_olmo_001** (failed): —\n- **mvp_pipeline_pythia_002** (success): —\n- **mvp_pipeline_qwen_base_004** (killed): —\n\n## 趋势\n成功 1 / 负向 0 / 失败 1 / 共 10\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\n（无服务器配置）\n\n## 告警\n- mvp_pipeline_001: 已被终止 — unknown\n- mvp_pipeline_002: 已被终止 — unknown\n- mvp_pipeline_003: 已被终止 — unknown\n- mvp_pipeline_004: 已被终止 — unknown\n- mvp_pipeline_base_002: 已被终止 — unknown\n- mvp_pipeline_base_003: 已被终止 — unknown\n- mvp_pipeline_pythia_001: 已被终止 — unknown\n- mvp_pipeline_qwen_base_004: 已被终止 — unknown\n- cross_model_olmo_001: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56891d18-2f8d-46f1-aeac-775a9fc621c4",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "311b4f71-1d85-4dda-a453-0e63d06e9c74",
  "sourceToolAssistantUUID": "56891d18-2f8d-46f1-aeac-775a9fc621c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T15:00:39.352Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RK1QsxkSWndUvTVdDwHVWj`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "311b4f71-1d85-4dda-a453-0e63d06e9c74",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fK7EULX1pipccDcnfV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b85acef4-c464-43c0-a3b8-ef930b8de697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALcubop1e8nuZPZafgwiWM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15271,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 15271,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1447,
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

_source line 9 · 2026-05-14T15:00:39.364Z_

<details><summary>↩ Tool result · `toolu_01RK1QsxkSWndUvTVdDwHVWj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| pythia_temp09_001 | 解码策略鲁棒性: Pythia-1.4B 在 temperature-only τ=0.9 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化 | — | — | — |\\n| cross_model_gpt2xl_001 | — | — | — | — |\\n\\n## 待处理\\n- cross_model_olmo_002: 跨模型泛化: OLMo-1B 递归生成的统计特征与 Pythia-1.4B 一致，支持深度估计跨模型迁移 (重跑 olmo_001, 修复脚本 bug)（准备中）\\n- pythia_topk50_001: 解码策略鲁棒性: Pythia-1.4B 在 top-k k=50 下递归生成的深度信号与 nucleus p=0.95 一致，支持跨策略泛化（准备中）\\n\\n## 近期结论\\n- **cross_model_olmo_001** (failed): —\\n- **mvp_pipeline_pythia_002** (success): —\\n- **mvp_pipeline_qwen_base_004** (killed): —\\n\\n## 趋势\\n成功 1 / 负向 0 / 失败 1 / 共 10\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n- mvp_pipeline_001: 已被终止 — unknown\\n- mvp_pipeline_002: 已被终止 — unknown\\n- mvp_pipeline_003: 已被终止 — unknown\\n- mvp_pipeline_004: 已被终止 — unknown\\n- mvp_pipeline_base_002: 已被终止 — unknown\\n- mvp_pipeline_base_003: 已被终止 — unknown\\n- mvp_pipeline_pythia_001: 已被终止 — unknown\\n- mvp_pipeline_qwen_base_004: 已被终止 — unknown\\n- cross_model_olmo_001: 训练失败 — unknown\\n\", \"total_chars\": 1093, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b85acef4-c464-43c0-a3b8-ef930b8de697",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "082e9794-1f38-4738-ad79-70be173b00be",
  "sourceToolAssistantUUID": "b85acef4-c464-43c0-a3b8-ef930b8de697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T15:00:42.481Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DdpRsdSVsRWPoZJzBGjfGt`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "082e9794-1f38-4738-ad79-70be173b00be",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fKR52CGKtjT4gsJEBw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70ea6c08-2d43-46c1-b8c4-ece154f1a944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6LVtbLXqykCWehJvsT9Aw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 16718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2071,
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

_source line 11 · 2026-05-14T15:00:42.494Z_

<details><summary>↩ Tool result · `toolu_01DdpRsdSVsRWPoZJzBGjfGt`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70ea6c08-2d43-46c1-b8c4-ece154f1a944",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "9d1aade4-70c5-450b-8d19-780371d23a4c",
  "sourceToolAssistantUUID": "70ea6c08-2d43-46c1-b8c4-ece154f1a944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T15:00:43.413Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017QjZTZrHWvY6HZrhJds5RD`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d1aade4-70c5-450b-8d19-780371d23a4c",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fKR52CGKtjT4gsJEBw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bbc7aab-0e14-478c-b879-0112b41110f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6LVtbLXqykCWehJvsT9Aw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 16718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2071,
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

_source line 13 · 2026-05-14T15:00:43.424Z_

<details><summary>↩ Tool result · `toolu_017QjZTZrHWvY6HZrhJds5RD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/memory.md\", \"content\": \"# Memory — recursive_gen_depth_est\\n\\n## 关键决策\\n\\n### 模型选择：Pythia-1.4B 为 MVP 模型（2026-05-14）\\nQwen2.5 系列预训练代码占比太高 → 换用 Pythia-1.4B（The Pile, 代码仅 3.3%）。\\n\\n### Research Phase 模型架构确认（2026-05-14）\\n\\n| 模型 | model_type | 参数量 | LoRA targets | 路径 | 注意事项 |\\n|------|-----------|--------|-------------|------|---------|\\n| Pythia-1.4B | gpt_neox | 1.41B | `query_key_value` | `/root/autodl-tmp/models/pythia-1.4b/` | pad_token 已自带 |\\n| OLMo-1B | olmo | 1.18B | `q_proj,k_proj,v_proj` | `/root/autodl-tmp/models/olmo-1b-hf/` | 用 `allenai/OLMo-1B-hf`（非 OLMo-1B，后者需 hf_olmo 自定义代码）。BOS=None, PAD=1。**三个模块不是两个** |\\n| GPT-2 XL | gpt2 | 1.56B | `c_attn,c_proj` | `/root/autodl-tmp/models/gpt2-xl/` | 用 Conv1D 不是 nn.Linear，PEFT 自动处理。pad_token=None 需设为 eos_token |\\n\\n### 文本长度 confound 修复（Reviewer 2026-05-14）\\nmax_new_tokens=512，特征提取统一截断到 498 tokens。\\n\\n### GPU 硬件（2026-05-14）\\ngpu-6000pro-2: 2× NVIDIA RTX PRO 6000 Blackwell 98GB。\\n\\n## MVP 结果（2026-05-14, mvp_pipeline_pythia_002, SUCCESS）\\n\\n### 核心发现\\n- **4-class acc=78.2%** (chance=25%), 过滤代码后 81.6%（信号非域混淆）\\n- **3-class acc=70.8%** (d1/d2/d3 only, chance=33.3%)——去掉 depth-0 \\\"easy win\\\" 后信号依然强\\n- d0v1 AUC=0.998, d1v2=0.861, d2v3=0.801\\n- 3-class: d1v2=0.854, d2v3=0.793\\n- **最重要特征**: var_surprisal > p90_ppl > mean_ppl\\n- 训练 loss: 2.241→1.389→1.025（模式坍缩信号）\\n- 代码污染（宽标准）: d0=0.5%, d1=17.8%, d2=22.4%, d3=27.4%\\n- Stratified split 稳定: 78.2% → 78.1% (-0.1pp)\\n\\n### 代码过滤标准差异\\n- 窄标准(4 patterns): d1=7.4%, d2=11.8%, d3=15.3%\\n- 宽标准(18 patterns): d1=17.8%, d2=22.4%, d3=27.4%\\n- 差异来自 def/function/var/div/php/SQL 等额外 pattern\\n\\n## 经验教训\\n\\n- 代码占比高的模型不能用于递归生成实验\\n- 域一致性检查是必做步骤\\n- 控制实验验证信号真实性：过滤代码后 acc 提升 → 域混淆排除\\n- AutoDL: HF 下载慢用 ModelScope CDN\\n- Worker 汇报需验证：读 log 确认实际执行\\n- OLMo-1B 必须用 HF 格式（allenai/OLMo-1B-hf），原始格式需自定义代码\\n- GPT-2 XL 的 attention 用 Conv1D，LoRA target 是 c_attn/c_proj\\n- **Pipeline 脚本提交前必须 `bash -n script.sh` 验证语法**（OLMo pipeline 因未闭合引号崩溃，浪费一个 GPU cycle）\\n- OLMo LoRA targets 是三个模块 (q_proj, k_proj, v_proj)，不是两个\\n\", \"total_chars\": 1913, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bbc7aab-0e14-478c-b879-0112b41110f3",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "2320b8ef-5eed-49b1-89f5-c027d8c82a1c",
  "sourceToolAssistantUUID": "4bbc7aab-0e14-478c-b879-0112b41110f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T15:00:43.863Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013h1BnqnMYSetpXJvwAAPr4`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2320b8ef-5eed-49b1-89f5-c027d8c82a1c",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fKR52CGKtjT4gsJEBw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a79faf3-1f87-4800-89e1-4e9d5c0fdea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6LVtbLXqykCWehJvsT9Aw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 16718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2071,
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

_source line 15 · 2026-05-14T15:00:43.880Z_

<details><summary>↩ Tool result · `toolu_013h1BnqnMYSetpXJvwAAPr4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/ROADMAP.md\", \"content\": \"# recursive_gen_depth_est — Research Dashboard\\n\\n> 最后更新: 2026-05-14 14:06 UTC | 更新原因: MVP PASS, 进入 research phase, framing + plan 完成, Dream 运行中\\n\\n## 核心方向\\n递归生成深度估计：给定文本，预测其经历了多少轮 model→data→model 递归训练循环。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-14 通过，4-class acc 78.2%）\\n- **核心信号**: surprisal 方差 > perplexity P90 > mean perplexity 是最强深度特征\\n- **覆盖率**: 1/3 模型 (Pythia), 1/3 策略 (nucleus), 4/6 深度 (0-3)\\n- **基础设施**: westb-52439 (2× NVIDIA RTX PRO 6000 Blackwell 98GB)\\n- **Dream**: dream_20260514T140607 运行中，等待回调再批准 P0 实验\\n\\n## Claims (详见 paper_framing.md)\\n1. Ordinal depth estimation feasible + accurate (DCOL method)\\n2. Depth Degradation Atlas (systematic characterization + EDD)\\n3. Depth-graduated curation > binary filtering (proof-of-concept)\\n\\n## 实验计划 (详见 experiment_plan.yaml)\\n- **P0** (45 GPU·h): 3 模型链 (Pythia/OLMo/GPT-2 XL) × 3 策略 + DCOL 训练 + leave-one-model-out + Atlas\\n- **P1** (38 GPU·h): leave-one-strategy-out + DeBERTa E2E + baseline battery + ablations + depth 5 + granularity\\n- **P2** (45 GPU·h): downstream curation + 7B probe + wild calibration\\n\\n## 近期任务\\n- [x] MVP PASS (Pythia-1.4B, 78.2% acc, 0.861 d1v2 AUC)\\n- [x] paper_framing.md 完成\\n- [x] experiment_plan.yaml 完成\\n- [ ] Dream 模拟完成 → 审查行动项 → 批准 P0 ← 等待中\\n- [ ] P0 实验启动（OLMo-1B + GPT-2 XL 递归链 + Pythia 补充策略）\\n\\n## GPU 预算\\n- 本项目分配: westb-52439 cuda:0, cuda:1 (2× Blackwell 98GB)\\n- MVP 消耗: 1.78 GPU·h\\n- P0 预估: 45 GPU·h (~1 day on 2 GPUs)\\n- P0+P1: 83 GPU·h (~2 days)\\n\\n## 教训\\n- Qwen2.5 预训练代码占比过高，LoRA + 无条件生成产出代码 → 换 Pythia (The Pile, 3.3% 代码)\\n- 手动抽查 8 条不够做域一致性判断，需 grep 定量扫描\\n- 指令冲突导致 Agent 来回切换模型 → 统一指令后用 replace_agent_queue 清队列\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D001 | 2026-05-14 | MVP PASS — 递归生成深度可从统计特征高精度区分，进入 research phase | mvp_pipeline_pythia_002 |\\n\\n\\n\", \"total_chars\": 1764, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a79faf3-1f87-4800-89e1-4e9d5c0fdea6",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "f6dbca18-bff8-4dc7-af7e-ff4b0ac5758e",
  "sourceToolAssistantUUID": "0a79faf3-1f87-4800-89e1-4e9d5c0fdea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T15:00:44.825Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013dS6GeoDdgZqqtEhNWyxfR`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6dbca18-bff8-4dc7-af7e-ff4b0ac5758e",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fKR52CGKtjT4gsJEBw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63d2e23c-e478-4c90-b1cf-18e4193b1daf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6LVtbLXqykCWehJvsT9Aw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 16718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2071,
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

_source line 17 · 2026-05-14T15:00:44.841Z_

<details><summary>↩ Tool result · `toolu_013dS6GeoDdgZqqtEhNWyxfR`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63d2e23c-e478-4c90-b1cf-18e4193b1daf",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "27352541-8b56-4694-a7c3-3b91e3bb46cb",
  "sourceToolAssistantUUID": "63d2e23c-e478-4c90-b1cf-18e4193b1daf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T15:00:45.250Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FF789Wc2XPyKt2iejMCzDR`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27352541-8b56-4694-a7c3-3b91e3bb46cb",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fKR52CGKtjT4gsJEBw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06954cf3-fa61-411c-a3d5-9cd95d7eec77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6LVtbLXqykCWehJvsT9Aw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 16718,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2071
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 479,
          "cache_read_input_tokens": 16718,
          "cache_creation_input_tokens": 2071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2071,
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

_source line 19 · 2026-05-14T15:00:45.265Z_

<details><summary>↩ Tool result · `toolu_01FF789Wc2XPyKt2iejMCzDR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper_framing.md\", \"content\": \"# Paper Framing — recursive_gen_depth_est\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\\n- EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\\n\\n## Core Claims (3 条)\\n\\n1. **Ordinal depth estimation is feasible and accurate**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features and contrastive ordinal learning. On our benchmark, DCOL achieves significantly higher accuracy than binary detection baselines and standard classification approaches. (MVP signal: 78.2% 4-class accuracy with simple RF on Pythia chain)\\n\\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse**: We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) surprisal variance as the strongest depth signal, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), and (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. This atlas spans 3 model families × 3 decoding strategies.\\n\\n3. **Depth-graduated curation outperforms binary filtering**: Using predicted depth as a continuous quality proxy enables more nuanced data curation — graduated weighting by depth retains high-quality shallow-generation content while down-weighting deeply recursive text, outperforming binary real/synthetic filtering on downstream task quality. (Proof-of-concept scope, ~1 page)\\n\\n## Story Spine\\n\\n- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer \\\"is this synthetic?\\\" but not \\\"how many recursive cycles has this undergone?\\\" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.\\n\\n- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.\\n\\n- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark (3 models × 3 strategies × 5+ depths), and propose DCOL — a contrastive ordinal learning method with learnable non-uniform margins that captures the actual geometry of recursive degradation. Crucially, we don't just build a classifier — we provide a Depth Degradation Atlas mapping how features evolve across depths, models, and strategies, including the EDD boundary where discrimination saturates.\\n\\n- **Headline result template**: \\\"On our multi-generational benchmark spanning 3 model families and 3 decoding strategies, our method achieves X% ordinal depth estimation accuracy (chance=25% for 4-class), with cross-model generalization accuracy of Y%, while the best binary detection baseline repurposed for depth estimation achieves only Z%.\\\"\\n- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) pending plan_011 results.\\n\\n## DCOL Contingency\\nIf DCOL improvement over RF/feature-based methods is < 5pp:\\n- Claim 2 (Atlas) becomes the PRIMARY contribution\\n- DCOL is repositioned as \\\"one strong method within the depth estimation framework\\\"\\n- Story shifts from \\\"method paper\\\" to \\\"task formalization + systematic empirical study + practical framework\\\"\\n- This is still a strong paper — the MVP RF already achieves 78.2%, the Atlas and EDD are novel regardless of method\\n\\n## Venue Fit Risks\\n\\n- **Novelty concern**: DCOL is adapted from CLOC (CVPR 2025). Mitigation: novelty emphasis on problem formalization + Atlas + EDD metric; DCOL is framed as a strong method within the framework, not the sole contribution. Three text-specific modifications (strategy-aware margins, surprisal-augmented anchors, non-uniform learned margins) differentiate from direct CLOC transfer.\\n- **\\\"Just an empirical study\\\" risk**: Mitigation: method (DCOL) + Atlas (scientific contribution) + curation (practical application) = three-line contribution with clear primary/secondary hierarchy.\\n- **Controlled vs wild gap**: Mitigation: honest scoping — controlled setting is primary, wild-data calibration is probed, ecological transfer is future work.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. \\\"EDD might be very low (depth 2-3), making the task trivial beyond shallow depths\\\" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation)\\n2. \\\"Why ordinal and not just binary?\\\" → MVP already shows: d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs\\n3. \\\"Generalization to unseen models/strategies?\\\" → Leave-one-out experiments are core evaluation\\n4. \\\"Non-monotonic degradation (Drayson et al.)?\\\" → Learnable margins as soft inductive bias; ablation comparing DCOL vs fixed-margin CORAL vs CE loss\\n\", \"total_chars\": 5471, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06954cf3-fa61-411c-a3d5-9cd95d7eec77",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "dfd57a4a-4ba7-473c-9796-9f8942593094",
  "sourceToolAssistantUUID": "06954cf3-fa61-411c-a3d5-9cd95d7eec77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-14T15:00:48.422Z_

Now let me read the actual paper/artifacts and any experiment results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfd57a4a-4ba7-473c-9796-9f8942593094",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fKrP2qon4tg26srfk7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecf6da87-895d-41aa-9144-cd72e45c57ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175hJrjnrACnpNcdP5CK8qk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4857,
      "cache_read_input_tokens": 18789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4857,
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

_source line 21 · 2026-05-14T15:00:48.903Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CSPuPFhY4BgFo1LUCxAqjF`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecf6da87-895d-41aa-9144-cd72e45c57ef",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fKrP2qon4tg26srfk7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "080a1200-5c25-458b-b87e-be204191ee57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175hJrjnrACnpNcdP5CK8qk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4857,
      "cache_read_input_tokens": 18789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4857,
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

_source line 22 · 2026-05-14T15:00:48.925Z_

<details><summary>↩ Tool result · `toolu_01CSPuPFhY4BgFo1LUCxAqjF`</summary>

```text
artifacts/dream_reports/dream_20260514T140607/best/paper.tex
artifacts/dream_reports/dream_20260514T140607/median/paper.tex
artifacts/dream_reports/dream_20260514T140607/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "080a1200-5c25-458b-b87e-be204191ee57",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "a4c3f9fc-b770-47cd-aecd-60e77ef6f0ec",
  "sourceToolAssistantUUID": "080a1200-5c25-458b-b87e-be204191ee57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T15:00:49.375Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XUaQvumqKoMaXzJVhUj8Wx`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4c3f9fc-b770-47cd-aecd-60e77ef6f0ec",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fKrP2qon4tg26srfk7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb7f3296-742f-4ff8-9cf6-0980ba1ddc02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175hJrjnrACnpNcdP5CK8qk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4857,
      "cache_read_input_tokens": 18789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4857,
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

_source line 24 · 2026-05-14T15:00:49.414Z_

<details><summary>↩ Tool result · `toolu_01XUaQvumqKoMaXzJVhUj8Wx`</summary>

```text
artifacts/dream_reports/dream_20260514T140607/best/paper.pdf
artifacts/dream_reports/dream_20260514T140607/median/paper.pdf
artifacts/dream_reports/dream_20260514T140607/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb7f3296-742f-4ff8-9cf6-0980ba1ddc02",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "2d7054eb-c534-4ef1-93d8-c6f390f8c241",
  "sourceToolAssistantUUID": "eb7f3296-742f-4ff8-9cf6-0980ba1ddc02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T15:00:49.974Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LMke4UYZzWUPJseaHJXWX6`</summary>

```json
{
  "pattern": "artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d7054eb-c534-4ef1-93d8-c6f390f8c241",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fKrP2qon4tg26srfk7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b216e080-1ebd-4b17-87bb-7d0f51b71a44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175hJrjnrACnpNcdP5CK8qk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4857,
      "cache_read_input_tokens": 18789,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4857
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 18789,
          "cache_creation_input_tokens": 4857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4857,
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

_source line 26 · 2026-05-14T15:00:49.991Z_

<details><summary>↩ Tool result · `toolu_01LMke4UYZzWUPJseaHJXWX6`</summary>

```text
artifacts/dream_reports/dream_20260514T140607/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T140607/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T140607/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T140607/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T140607/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T140607/best/experiment_data.json
artifacts/dream_reports/dream_20260514T140607/best/paper_framing.md
artifacts/dream_reports/dream_20260514T140607/best/paper.tex
artifacts/dream_reports/dream_20260514T140607/best/paper.aux
artifacts/dream_reports/dream_20260514T140607/best/paper.out
artifacts/dream_reports/dream_20260514T140607/best/paper.pdf
artifacts/dream_reports/dream_20260514T140607/best/paper.log
artifacts/dream_reports/dream_20260514T140607/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T140607/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T140607/median/experiment_data.json
artifacts/dream_reports/dream_20260514T140607/median/paper_framing.md
artifacts/dream_reports/dream_20260514T140607/median/paper.tex
artifacts/dream_reports/dream_20260514T140607/median/paper.aux
artifacts/dream_reports/dream_20260514T140607/median/paper.out
artifacts/dream_reports/dream_20260514T140607/median/paper.pdf
artifacts/dream_reports/dream_20260514T140607/median/paper.log
artifacts/dream_reports/dream_20260514T140607/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T140607/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T140607/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T140607/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T140607/worst/paper.tex
artifacts/dream_reports/dream_20260514T140607/worst/paper.aux
artifacts/dream_reports/dream_20260514T140607/worst/paper.out
artifacts/dream_reports/dream_20260514T140607/worst/paper.pdf
artifacts/dream_reports/dream_20260514T140607/worst/paper.log
artifacts/dream_reports/dream_20260514T140607/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T140607/best/review_context.yaml
artifacts/dream_reports/dream_20260514T140607/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T140607/best/review_report.md
artifacts/dream_reports/dream_20260514T140607/logs/review_best.log
artifacts/dream_reports/dream_20260514T140607/median/review_context.yaml
artifacts/dream_reports/dream_20260514T140607/median/review_report.md
artifacts/dream_reports/dream_20260514T140607/logs/review_median.log
artifacts/dream_reports/dream_20260514T140607/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T140607/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b216e080-1ebd-4b17-87bb-7d0f51b71a44",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "8c797311-f382-4f1d-9e3b-d73180a3668f",
  "sourceToolAssistantUUID": "b216e080-1ebd-4b17-87bb-7d0f51b71a44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-14T15:00:52.997Z_

Let me read the "median" paper (the most representative scenario for the review) and the best paper as well.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c797311-f382-4f1d-9e3b-d73180a3668f",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fLCZyGeiQPjGabu332",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0c9c866-9a88-49f1-90a5-3147234442e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011sZmncxk84Zjffyew5VF8P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1503,
      "cache_read_input_tokens": 23646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1503,
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

_source line 28 · 2026-05-14T15:00:53.414Z_

<details open><summary>🔧 Tool call — Read · `toolu_0136GSiY3r7P2cHqEZuoeyQH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0c9c866-9a88-49f1-90a5-3147234442e8",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fLCZyGeiQPjGabu332",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a73ba9c5-f666-46b0-b8f2-a6f4b798fdbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011sZmncxk84Zjffyew5VF8P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1503,
      "cache_read_input_tokens": 23646,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1503
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 23646,
          "cache_creation_input_tokens": 1503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1503,
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

_source line 29 · 2026-05-14T15:00:53.695Z_

<details><summary>↩ Tool result · `toolu_0136GSiY3r7P2cHqEZuoeyQH`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{tabularx}
12	\usepackage{enumitem}
13	\usepackage{hyperref}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	%\usepackage{natbib}
17	
18	\title{Ordinal Depth Estimation of Recursive Generation:\\A Depth Degradation Atlas for Model Collapse Characterization}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	% ============================================================
26	\begin{abstract}
27	Web-scraped corpora increasingly contain multi-generational synthetic text produced by uncontrolled model$\to$data$\to$model feedback loops.
28	Existing detectors answer \emph{whether} text is synthetic but not \emph{how many recursive cycles} it has undergone---a distinction that matters because shallow-generation text can be benign while deeply recursive text drives distribution collapse.
29	We formalize \textbf{ordinal generation depth estimation} as a new task and construct a multi-generational benchmark spanning 3 model families (Pythia-1.4B, OLMo-1B, GPT-2~XL) $\times$ 3 decoding strategies $\times$ 6 depths.
30	We propose \textbf{DCOL} (Depth Contrastive Ordinal Learning), a DeBERTa-based method with learnable non-uniform margins that captures the geometry of recursive degradation.
31	DCOL achieves 57.1\% 6-class accuracy (chance = 16.7\%) and 82.3\% 4-class accuracy, outperforming the best baseline (CORAL) by +3.3 percentage points (pp).
32	Beyond the classifier, we contribute a \textbf{Depth Degradation Atlas}---a systematic characterization of how statistical features evolve across depths, models, and strategies---revealing an \textbf{Effective Discriminable Depth (EDD)} of $\approx$3, beyond which adjacent depths become indistinguishable.
33	Cross-model leave-one-out generalization averages 47.0\% (6-class) with variance across rotations, and a downstream curation proof-of-concept shows that depth-graduated weighting reduces perplexity by 3.1\% over binary filtering ($p=0.038$).
34	We release the benchmark and Atlas to support future work on recursive contamination characterization.
35	\end{abstract}
36	
37	% ============================================================
38	\section{Introduction}
39	\label{sec:intro}
40	
41	The proliferation of large language model (LLM) outputs on the web has created a new challenge for training data curation: \emph{recursive synthetic contamination}.
42	When model-generated text is scraped, used to train new models, and those models generate yet more text, the resulting feedback loop produces multi-generational synthetic content whose quality degrades with each cycle~\cite{shumailov2024model}.
43	Model collapse studies have documented this degradation~\cite{drayson2025emnlp}, but they assume the recursion depth is known a priori.
44	In practice, curators face unlabeled text and must infer depth from the text itself.
45	
46	Existing synthetic text detectors operate in a binary paradigm---\emph{real} vs.\ \emph{synthetic}---discarding ordinal information about \emph{how many} recursive cycles a text has undergone.
47	This is a consequential limitation: first-generation synthetic text may be high-quality and useful for training, while deeply recursive text exhibits statistical degradation (narrowed surprisal distributions, shifted perplexity, Zipf distortion) that can harm downstream models.
48	A curation strategy that distinguishes these cases can retain useful synthetic content while filtering harmful recursive artifacts.
49	
50	We make three contributions:
51	
52	\begin{enumerate}[leftmargin=*,topsep=2pt,itemsep=1pt]
53	\item \textbf{Ordinal depth estimation framework.} We formalize the task of predicting generation depth $d \in \{0,1,\ldots,K\}$ from text alone, propose DCOL with learnable non-uniform margins, and show it achieves 82.3\% 4-class accuracy (57.1\% 6-class), outperforming 8 baselines including CORAL, cross-entropy DeBERTa, and zero-shot GPT-4o.
54	
55	\item \textbf{Depth Degradation Atlas.} We provide the first systematic empirical map of recursive degradation across 3 model families $\times$ 3 decoding strategies, identifying surprisal variance as the most stable depth signal (monotonicity score 0.847), documenting non-uniform inter-depth distances, and establishing the Effective Discriminable Depth (EDD $\approx 3$) boundary.
56	
57	\item \textbf{Depth-graduated curation (proof-of-concept).} Graduated weighting by predicted depth reduces fine-tuning perplexity by 3.1\% over binary filtering ($p=0.038$), demonstrating the practical value of ordinal depth information.
58	\end{enumerate}
59	
60	% ============================================================
61	\section{Related Work}
62	\label{sec:related}
63	
64	\paragraph{Model collapse and recursive generation.}
65	Shumailov et al.\ (2024) demonstrate that iterative training on self-generated data leads to distribution collapse, with tails of the original distribution vanishing progressively.
66	Drayson et al.\ (EMNLP 2025) extend this analysis to characterize non-monotonic degradation patterns in specific settings.
67	These studies assume depth is known; we estimate it from text.
68	
69	\paragraph{Synthetic text detection.}
70	Binary detectors such as LOKI, DivEye, and Binoculars classify text as real or synthetic using statistical features or model-based scores.
71	EditLens estimates single-pass AI editing extent but does not address recursive depth.
72	Our work extends the detection paradigm from binary to ordinal.
73	
74	\paragraph{Ordinal classification.}
75	CORAL~\cite{cao2020coral} learns ordinal regression with consistent rank predictions via cumulative probabilities.
76	CLOC (CVPR 2025) applies contrastive learning with ordinal margins to age estimation.
77	We adapt the contrastive ordinal framework to text, introducing strategy-aware margins, surprisal-augmented anchors, and non-uniform learned margins.
78	
79	% ============================================================
80	\section{Method}
81	\label{sec:method}
82	
83	\subsection{Problem Formulation}
84	
85	Given a text passage $x$, we estimate its ordinal generation depth $d \in \{0, 1, \ldots, K\}$, where $d=0$ denotes human-written text and $d=k$ denotes text produced by the $k$-th recursive generation cycle.
86	The key structural property is that inter-depth distances are \emph{non-uniform}: the distribution shift from $d=0$ to $d=1$ is far larger than from $d=2$ to $d=3$, reflecting the diminishing marginal degradation in recursive generation.
87	
88	\subsection{Benchmark Construction}
89	
90	We construct recursive generation chains using three model families---Pythia-1.4B, OLMo-1B, and GPT-2~XL---each with three decoding strategies: nucleus sampling ($p=0.95$), temperature sampling ($\tau=0.9$), and top-$k$ sampling ($k=50$).
91	For each of the 9 model$\times$strategy combinations, we produce chains of depth $0$ through $5$ (6 levels), with approximately 1{,}200 samples per depth per strategy.
92	Depth-$0$ texts are drawn from a held-out human corpus; each subsequent depth is generated by prompting the model with the previous depth's output.
93	
94	\subsection{Feature Extraction}
95	
96	We extract 19 statistical features from each text, spanning:
97	\begin{itemize}[leftmargin=*,topsep=2pt,itemsep=1pt]
98	\item \textbf{Surprisal statistics}: mean, variance, p75, p90 of token-level surprisal
99	\item \textbf{Perplexity statistics}: mean, p75, p90 of passage-level perplexity
100	\item \textbf{Lexical statistics}: Zipf's $\alpha$, type-token ratio, hapax ratio, repetition rate
101	\item \textbf{Distribution statistics}: entropy, KL divergence from reference, tail probability mass
102	\end{itemize}
103	These features serve both the Random Forest (RF) baseline and as analysis dimensions in the Atlas.
104	
105	\subsection{DCOL: Depth Contrastive Ordinal Learning}
106	
107	DCOL uses a DeBERTa-v3-large encoder to produce passage embeddings $\mathbf{h} = f_\theta(x)$.
108	Training uses an $N$-pair contrastive loss with ordinal margins:
109	\begin{equation}
110	\mathcal{L} = \sum_{(i,j)} \max\bigl(0, \|\mathbf{h}_i - \mathbf{h}_j\|_2 - m(|d_i - d_j|)\bigr)^2
111	\end{equation}
112	where $m(\Delta d)$ is a margin function that enforces larger separation for more distant depths.
113	
114	Three text-specific modifications distinguish DCOL from generic contrastive ordinal methods:
115	
116	\begin{enumerate}[leftmargin=*,topsep=2pt,itemsep=1pt]
117	\item \textbf{Learnable non-uniform margins.} Instead of fixed margins $m(\Delta d) = \alpha \cdot \Delta d$, we parameterize $m$ with per-adjacent-pair learnable scalars, allowing the model to discover that $m(0\to1) \gg m(2\to3)$.
118	\item \textbf{Surprisal-augmented anchor selection.} Hard negative mining prioritizes pairs whose surprisal variance is close but depth differs, focusing contrastive learning on the most informative comparisons.
119	\item \textbf{Strategy conditioning.} A lightweight strategy embedding modulates the encoder, accounting for decoding-strategy-specific degradation patterns.
120	\end{enumerate}
121	
122	For classification, an ordinal regression head maps embeddings to cumulative probabilities, predicting depth as the largest $d$ for which $P(D > d) > 0.5$.
123	
124	% ============================================================
125	\section{Experiments}
126	\label{sec:experiments}
127	
128	\subsection{Per-Model Recursive Chain Benchmarks}
129	\label{sec:per_model}
130	
131	We first evaluate depth estimation independently on each model family using RF classifiers with 19 statistical features to establish that recursive degradation signals exist across architectures.
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\caption{Per-model 4-class depth estimation (RF + 19 features). Accuracy with 95\% CI, MAE, and per-pair AUC. $\sim$1{,}200 samples per depth per strategy.}
137	\label{tab:per_model}
138	\begin{tabular}{@{}lccccc@{}}
139	\toprule
140	\textbf{Model} & \textbf{Acc.\ (4-cl)} & \textbf{MAE} & \textbf{AUC$_{0v1}$} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} \\
141	\midrule
142	GPT-2 XL & .798 [.785,.811] & .218 & .998 & .874 & .812 \\
143	Pythia-1.4B & .782 & .237 & .998 & .861 & .801 \\
144	OLMo-1B & .754 [.740,.768] & .268 & .994 & .838 & .771 \\
145	\bottomrule
146	\end{tabular}
147	\end{table}
148	
149	Table~\ref{tab:per_model} shows results pooled across strategies.
150	GPT-2~XL exhibits the strongest depth signals (79.8\% 4-class accuracy), consistent with its weaker generation ability producing faster degradation.
151	OLMo-1B shows the weakest signals (75.4\%), attributable to Dolma-trained generation producing more human-like shallow outputs.
152	Across all models, AUC decreases monotonically from $>$0.99 (depth 0v1) to $\sim$0.77--0.81 (depth 2v3), confirming that depth discrimination degrades but remains well above chance within the first three generations.
153	
154	\paragraph{Per-strategy breakdown.}
155	Table~\ref{tab:olmo_strategy} and Table~\ref{tab:gpt2_strategy} report per-strategy results for OLMo-1B and GPT-2~XL, respectively.
156	Nucleus sampling consistently yields the strongest depth signals, while temperature sampling produces the weakest---temperature's unrestricted rescaling of the logit space adds noise that partially masks depth-related degradation.
157	
158	\begin{table}[t]
159	\centering
160	\small
161	\caption{OLMo-1B per-strategy 4-class results.}
162	\label{tab:olmo_strategy}
163	\begin{tabular}{@{}lcccc@{}}
164	\toprule
165	\textbf{Strategy} & \textbf{Acc.} & \textbf{MAE} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} \\
166	\midrule
167	Nucleus $p$=0.95 & .768 & .252 & .849 & .784 \\
168	Top-$k$ $k$=50 & .752 & .271 & .839 & .770 \\
169	Temperature $\tau$=0.9 & .741 & .281 & .827 & .758 \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	\begin{table}[t]
175	\centering
176	\small
177	\caption{GPT-2~XL per-strategy 4-class results.}
178	\label{tab:gpt2_strategy}
179	\begin{tabular}{@{}lcccc@{}}
180	\toprule
181	\textbf{Strategy} & \textbf{Acc.} & \textbf{MAE} & \textbf{AUC$_{1v2}$} & \textbf{AUC$_{2v3}$} \\
182	\midrule
183	Nucleus $p$=0.95 & .812 & .204 & .885 & .823 \\
184	Top-$k$ $k$=50 & .799 & .217 & .876 & .815 \\
185	Temperature $\tau$=0.9 & .783 & .234 & .861 & .798 \\
186	\bottomrule
187	\end{tabular}
188	\end{table}
189	
190	\subsection{DCOL and Baseline Comparison}
191	\label{sec:baselines}
192	
193	We compare DCOL against 8 baselines, pooled across all 3 models $\times$ 3 strategies (Table~\ref{tab:baselines}).
194	
195	\begin{table}[t]
196	\centering
197	\small
198	\caption{Full baseline comparison, pooled across 3 models $\times$ 3 strategies. $\Delta$ is relative to best baseline (CORAL).}
199	\label{tab:baselines}
200	\begin{tabular}{@{}lcccc@{}}
201	\toprule
202	\textbf{Method} & \textbf{Acc.\ (6-cl)} & \textbf{MAE (6-cl)} & \textbf{Acc.\ (4-cl)} & \textbf{$\Delta$ (pp)} \\
203	\midrule
204	DCOL (ours) & .571 & .462 & .823 & +3.3 \\
205	CORAL (DeBERTa) & .538 & .491 & .806 & --- \\
206	CE (DeBERTa) & .519 & .512 & .793 & $-$1.9 \\
207	DeBERTa E2E (CE) & .553 & .478 & .809 & +1.5 \\
208	RF + 19 features & .497 & .538 & .778 & $-$4.1 \\
209	Binary cascade & .461 & .574 & .723 & $-$7.7 \\
210	DivEye features & .432 & .612 & .698 & $-$10.6 \\
211	LOKI features & .408 & .641 & .672 & $-$13.0 \\
212	Perplexity regression & .389 & .673 & .651 & $-$14.9 \\
213	Zero-shot GPT-4o & .287 & .892 & .418 & $-$25.1 \\
214	\bottomrule
215	\end{tabular}
216	\end{table}
217	
218	DCOL achieves 57.1\% 6-class accuracy and 82.3\% 4-class accuracy with 95\% CI [.811, .835].
219	The best baseline is CORAL (53.8\%), which shares DeBERTa's backbone and ordinal structure; DCOL's advantage of +3.3pp comes from learned non-uniform margins and contrastive training.
220	DCOL outperforms the best non-ordinal method (DeBERTa E2E at 55.3\%) by +1.8pp in 6-class accuracy, and the feature-based RF baseline by +7.4pp.
221	
222	Zero-shot GPT-4o performs near chance (28.7\% vs.\ 16.7\% chance), confirming that recursive depth is not a surface-level property accessible to general-purpose LLMs without task-specific training.
223	
224	\paragraph{End-to-end DeBERTa analysis.}
225	The end-to-end DeBERTa classifier (CE loss, no hand-crafted features) achieves 55.3\% 6-class and 80.9\% 4-class accuracy (Table~\ref{tab:e2e}).
226	It outperforms RF+features by +5.6pp (6-class), indicating that raw text encodes degradation signals beyond the 19 hand-crafted features.
227	DCOL's additional +1.8pp over E2E comes from ordinal inductive bias, not representation capacity: pairwise AUCs at depth 2v3 (.856 vs .838) and 3v4 (.714 vs .698) show that ordinal margins help most at the harder adjacent-pair boundaries.
228	
229	\begin{table}[t]
230	\centering
231	\small
232	\caption{End-to-end DeBERTa vs DCOL vs RF.}
233	\label{tab:e2e}
234	\begin{tabular}{@{}lccc@{}}
235	\toprule
236	\textbf{Method} & \textbf{Acc.\ (6-cl)} & \textbf{MAE (6-cl)} & \textbf{Acc.\ (4-cl)} \\
237	\midrule
238	DCOL (contrastive ordinal) & .571 & .462 & .823 \\
239	DeBERTa E2E (CE) & .553 & .478 & .809 \\
240	RF + 19 features & .497 & .538 & .778 \\
241	\bottomrule
242	\end{tabular}
243	\end{table}
244	
245	\subsection{DCOL Component Ablation}
246	\label{sec:ablation}
247	
248	We ablate DCOL's three text-specific modifications (Table~\ref{tab:ablation}).
249	
250	\begin{table}[t]
251	\centering
252	\small
253	\caption{DCOL component ablation (6-class accuracy, pooled).}
254	\label{tab:ablation}
255	\begin{tabular}{@{}lcc@{}}
256	\toprule
257	\textbf{Variant} & \textbf{Acc.\ (6-cl)} & \textbf{$\Delta$ (pp)} \\
258	\midrule
259	Full DCOL & .571 & --- \\
260	$-$ Strategy conditioning & .562 & $-$0.9 \\
261	$-$ Surprisal anchors & .558 & $-$1.3 \\
262	$-$ Learnable margins & .547 & $-$2.4 \\
263	$-$ All three (vanilla contrastive) & .531 & $-$4.0 \\
264	\bottomrule
265	\end{tabular}
266	\end{table}
267	
268	Learnable non-uniform margins contribute the largest increment ($-$2.4pp when removed), confirming that the non-uniform inter-depth geometry is a key structural property.
269	Surprisal-augmented anchor selection contributes $-$1.3pp; strategy conditioning contributes $-$0.9pp (its benefit is more pronounced in per-strategy evaluation than in pooled numbers).
270	Removing all three reduces accuracy to 53.1\%, below CORAL's 53.8\%, indicating that the vanilla contrastive loss alone underperforms CORAL's rank loss---the text-specific modifications are necessary for DCOL to surpass ordinal regression baselines.
271	
272	\subsection{Depth Degradation Atlas}
273	\label{sec:atlas}
274	
275	The Atlas systematically characterizes recursive degradation across all 9 model$\times$strategy combinations.
276	
277	\paragraph{Effective Discriminable Depth (EDD).}
278	We define EDD as the maximum depth $d$ for which adjacent-pair AUC($d$ vs $d{+}1$) $\geq$ 0.72.
279	Table~\ref{tab:edd} reports EDD per combination.
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\caption{EDD per model $\times$ strategy combination. Median EDD = 3.}
285	\label{tab:edd}
286	\begin{tabular}{@{}lccc@{}}
287	\toprule
288	\textbf{Model} & \textbf{Nucleus} & \textbf{Temperature} & \textbf{Top-$k$} \\
289	\midrule
290	Pythia-1.4B & 3 & 3 & 3 \\
291	OLMo-1B & 3 & 2 & 3 \\
292	GPT-2 XL & 4 & 3 & 3 \\
293	\bottomrule
294	\end{tabular}
295	\end{table}
296	
297	The median EDD across all 9 combinations is 3, meaning ordinal depth estimation is feasible at 4-class granularity (depths 0--3).
298	The range spans 2 (OLMo + temperature, where high intrinsic generation diversity compounds with temperature noise to saturate signals early) to 4 (GPT-2~XL + nucleus, where weaker generation and truncated sampling preserve depth signals longer).
299	This variation itself is a key finding: EDD is not a universal constant but depends on model capability and decoding strategy.
300	
301	\paragraph{Feature monotonicity.}
302	Table~\ref{tab:monotonicity} reports monotonicity scores (mean across 9 combinations) for the top-5 features.
303	
304	\begin{table}[t]
305	\centering
306	\small
307	\caption{Top-5 features by monotonicity score (mean across 9 combos). Rank stability = number of combos where the feature ranks $\leq k$.}
308	\label{tab:monotonicity}
309	\begin{tabular}{@{}lcc@{}}
310	\toprule
311	\textbf{Feature} & \textbf{Mono.\ score} & \textbf{Rank stability} \\
312	\midrule
313	\texttt{var\_surprisal} & 0.847 & 1/9 rank 1 \\
314	\texttt{p90\_ppl} & 0.823 & 6/9 rank $\leq$ 3 \\
315	\texttt{mean\_ppl} & 0.801 & 7/9 rank $\leq$ 4 \\
316	\texttt{zipf\_alpha} & 0.768 & 5/9 rank $\leq$ 5 \\
317	\texttt{mean\_surprisal} & 0.752 & 8/9 rank $\leq$ 6 \\
318	\bottomrule
319	\end{tabular}
320	\end{table}
321	
322	Surprisal variance (\texttt{var\_surprisal}) is the strongest and most stable depth signal (0.847), reflecting the progressive narrowing of surprisal distributions under recursive generation.
323	Perplexity tail statistics (\texttt{p90\_ppl}) rank second, capturing the loss of high-perplexity passages as recursion compresses the distribution.
324	Two of the 9 combinations exhibit non-monotonic feature behavior beyond the EDD boundary (OLMo+temperature at depth 3$\to$4, Pythia+top-$k$ at depth 4$\to$5); we interpret these as noise oscillations after signal saturation rather than genuine non-monotonic degradation.
325	
326	\subsection{Depth Extension and EDD Validation}
327	\label{sec:extension}
328	
329	We extend Pythia chains to depth 6 to validate the EDD boundary.
330	Table~\ref{tab:extension} shows pairwise AUCs.
331	
332	\begin{table}[t]
333	\centering
334	\small
335	\caption{Extended-depth pairwise AUC (Pythia-1.4B, nucleus).}
336	\label{tab:extension}
337	\begin{tabular}{@{}lccccccc@{}}
338	\toprule
339	\textbf{Pair} & 0v1 & 1v2 & 2v3 & 3v4 & 4v5 & 5v6 \\
340	\midrule
341	AUC & .998 & .861 & .801 & .708 & .621 & .573 \\
342	\bottomrule
343	\end{tabular}
344	\end{table}
345	
346	AUC declines monotonically, crossing the 0.72 threshold between depth 3v4 (0.708), confirming EDD = 3.
347	Bhattacharyya overlap between feature distributions rises from 0.82 (depth 4--5) to 0.91 (depth 5--6), approaching complete overlap.
348	Notably, feature importance shifts beyond the EDD: \texttt{var\_surprisal} drops from rank 1 to rank 3 while \texttt{zipf\_alpha} rises from rank 4 to rank 2 at depth 4+, suggesting that once surprisal variance is ``compressed to floor,'' lexical frequency distribution becomes the residual discriminative signal.
349	
350	\subsection{Granularity Ablation}
351	\label{sec:granularity}
352	
353	Table~\ref{tab:granularity} reports DCOL accuracy across classification granularities.
354	
355	\begin{table}[t]
356	\centering
357	\small
358	\caption{Granularity ablation (DCOL, pooled). Lift = accuracy $-$ chance.}
359	\label{tab:granularity}
360	\begin{tabular}{@{}lccc@{}}
361	\toprule
362	\textbf{Granularity} & \textbf{Acc.} & \textbf{Chance} & \textbf{Lift (pp)} \\
363	\midrule
364	Binary (0 vs 1+) & .946 & .500 & +44.6 \\
365	3-class (0, 1, 2+) & .867 & .333 & +53.4 \\
366	4-class (0, 1, 2, 3+) & .823 & .250 & +57.3 \\
367	6-class (0--5) & .571 & .167 & +40.4 \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	Lift over chance peaks at 4-class (+57.3pp), making it the optimal information--feasibility tradeoff.
373	The drop in lift from 4-class to 6-class reflects the inclusion of depths 4 and 5, which are largely indistinguishable (as predicted by EDD $\approx$ 3).
374	We report 6-class results throughout this paper for completeness but recommend 4-class (depths 0--3) as the practical operating granularity; depth 4+ should be treated as a collapsed ``deep recursive'' category.
375	
376	\subsection{Cross-Model Generalization}
377	\label{sec:cross_model}
378	
379	We evaluate leave-one-model-out (LOMO) generalization, training DCOL on two model families and testing on the held-out third (Table~\ref{tab:lomo}).
380	
381	\begin{table}[t]
382	\centering
383	\small
384	\caption{Leave-one-model-out cross-generalization.}
385	\label{tab:lomo}
386	\begin{tabular}{@{}llcccc@{}}
387	\toprule
388	\textbf{Held-out} & \textbf{Train on} & \textbf{Acc.\ (6-cl)} & \textbf{Acc.\ (4-cl)} & \textbf{MAE} & \textbf{Gate$_{.45}$} \\
389	\midrule
390	Pythia & OLMo, GPT-2 XL & .483 & .721 & .547 & PASS \\
391	OLMo & Pythia, GPT-2 XL & .421 & .673 & .601 & FAIL \\
392	GPT-2 XL & Pythia, OLMo & .507 & .748 & .521 & PASS \\
393	\midrule
394	\multicolumn{2}{@{}l}{Mean $\pm$ std} & .470 $\pm$ .036 & .714 $\pm$ .031 & .556 $\pm$ .033 & 2/3 \\
395	\bottomrule
396	\end{tabular}
397	\end{table}
398	
399	Mean 6-class accuracy is 47.0\% ($\pm$3.6\%), with 2 of 3 rotations passing the 0.45 gate.
400	The Hold-OLMo rotation is weakest (42.1\%): OLMo was trained on Dolma, whose distribution diverges most from the Pile-trained (Pythia) and WebText-trained (GPT-2~XL) models used in training, making it the hardest transfer target.
401	Hold-GPT-2~XL is strongest (50.7\%) because the Pythia+OLMo combination provides sufficient training diversity.
402	The 4-class mean (71.4\%) remains well above chance (25\%), indicating that coarse-grained ordinal estimation within the EDD boundary transfers across model families, even if fine-grained 6-class transfer is unreliable.
403	
404	\subsection{Cross-Strategy Generalization}
405	\label{sec:cross_strategy}
406	
407	Leave-one-strategy-out (LOSO) results (Table~\ref{tab:loso}) show that strategy generalization is easier than model generalization.
408	
409	\begin{table}[t]
410	\centering
411	\small
412	\caption{Leave-one-strategy-out cross-generalization.}
413	\label{tab:loso}
414	\begin{tabular}{@{}lcc@{}}
415	\toprule
416	\textbf{Held-out strategy} & \textbf{Acc.\ (6-cl)} & \textbf{Acc.\ (4-cl)} \\
417	\midrule
418	Nucleus & .528 & .786 \\
419	Temperature & .492 & .753 \\
420	Top-$k$ & .541 & .798 \\
421	\midrule
422	Mean $\pm$ std & .520 $\pm$ .021 & .779 $\pm$ .019 \\
423	\bottomrule
424	\end{tabular}
425	\end{table}
426	
427	Mean 6-class accuracy is 52.0\% ($\pm$2.1\%), compared to 47.0\% ($\pm$3.6\%) for model generalization.
428	Hold-temperature is weakest (49.2\%) because temperature sampling rescales the full logit distribution rather than truncating tails, producing surface statistics more distinct from nucleus/top-$k$.
429	The lower variance ($\sigma$ = 2.1pp vs 3.6pp) indicates that depth signals are primarily determined by model capability rather than decoding strategy---a finding consistent with the Atlas analysis (\S\ref{sec:atlas}).
430	
431	\subsection{Downstream Curation Proof-of-Concept}
432	\label{sec:curation}
433	
434	We test whether predicted depth enables better data curation than binary filtering (Table~\ref{tab:curation}).
435	A 1B-parameter model is fine-tuned on corpora curated with four strategies: no filtering, binary removal of all predicted-synthetic text, graduated weighting ($w = 1/(d_{\text{pred}}+1)$), and oracle weighting using true depth.
436	
437	\begin{table}[t]
438	\centering
439	\small
440	\caption{Downstream curation comparison.}
441	\label{tab:curation}
442	\begin{tabular}{@{}lccc@{}}
443	\toprule
444	\textbf{Curation method} & \textbf{PPL} & \textbf{Task Acc.} \\
445	\midrule
446	No filter & 19.85 & .703 \\
447	Binary filter & 18.72 & .724 \\
448	Graduated weighting (predicted) & 18.14 & .731 \\
449	Oracle weighting (true depth) & 17.91 & .738 \\
450	\bottomrule
451	\end{tabular}
452	\end{table}
453	
454	Graduated weighting reduces perplexity by 3.1\% relative to binary filtering ($p=0.038$) and by 8.6\% relative to no filtering.
455	The gap to oracle weighting (18.14 vs 17.91) quantifies the cost of depth prediction errors.
456	Downstream task accuracy follows the same ordering, though the gap between graduated and binary (73.1\% vs 72.4\%) is smaller, as perplexity differences attenuate when propagated to task performance.
457	
458	We scope this as a proof-of-concept with explicit limitations: (1) tested at a single model scale (1B), (2) graduated vs binary confidence intervals partially overlap, and (3) curation effectiveness depends on depth prediction quality.
459	
460	\subsection{Cross-Scale Probe: 7B Models}
461	\label{sec:7b}
462	
463	We probe whether depth signals transfer across model scales by testing DCOL trained on 1--1.5B models against 7B-model recursive chains (Table~\ref{tab:7b}).
464	
465	\begin{table}[t]
466	\centering
467	\small
468	\caption{Cross-scale transfer to 7B model.}
469	\label{tab:7b}
470	\begin{tabular}{@{}lcc@{}}
471	\toprule
472	\textbf{Setting} & \textbf{Acc.\ (4-cl)} & \textbf{Acc.\ (6-cl)} \\
473	\midrule
474	Zero-shot transfer (1--1.5B $\to$ 7B) & .614 & .372 \\
475	Fine-tuned on 7B data & .791 & .518 \\
476	1--1.5B in-distribution (ref.) & .823 & .571 \\
477	\bottomrule
478	\end{tabular}
479	\end{table}
480	
481	Zero-shot transfer degrades substantially (4-class: 61.4\% vs 82.3\% in-distribution), reflecting that 7B models produce higher-quality generation that shifts the depth boundaries---depth-1 text from a 7B model resembles depth-0 quality at the 1B scale.
482	However, fine-tuning on 7B data recovers to 79.1\% (4-class), indicating depth signals exist at the larger scale but require recalibration.
483	EDD at 7B is 3 (nucleus) and 2 (temperature), suggesting that stronger models reach signal saturation at shallower depths.
484	This motivates future work on scale-invariant depth estimation.
485	
486	\subsection{Wild-Data Calibration}
487	\label{sec:wild}
488	
489	We apply the trained DCOL model to a sample of RedPajama/Dolma web text as an ecological validity probe (Table~\ref{tab:wild}).
490	
491	\begin{table}[t]
492	\centering
493	\small
494	\caption{Wild-data depth score correlations with quality proxies.}
495	\label{tab:wild_corr}
496	\begin{tabular}{@{}lcc@{}}
497	\toprule
498	\textbf{Quality proxy} & \textbf{Spearman $\rho$} & \textbf{$p$-value} \\
499	\midrule
500	Perplexity (GPT-2) & .341 & .002 \\
501	AlignScore & .283 & .014 \\
502	\bottomrule
503	\end{tabular}
504	\end{table}
505	
506	\begin{table}[t]
507	\centering
508	\small
509	\caption{Predicted depth distribution on RedPajama sample.}
510	\label{tab:wild}
511	\begin{tabular}{@{}lcccc@{}}
512	\toprule
513	\textbf{Depth} & 0 & 1 & 2 & 3+ \\
514	\midrule
515	\% of sample & 72 & 16 & 6 & 6 \\
516	\bottomrule
517	\end{tabular}
518	\end{table}
519	
520	DCOL depth scores show moderate positive correlation with perplexity ($\rho = 0.341$, $p = 0.002$) and weaker correlation with AlignScore ($\rho = 0.283$, $p = 0.014$).
521	The majority of wild data is scored as depth 0 (72\%), with 28\% receiving depth $\geq$1.
522	The 6\% scored as depth 3+ may include overestimates, as low-quality human text in the wild can exhibit statistical profiles similar to deeply recursive content.
523	We present this as a calibration analysis rather than validation, since no ground-truth depth labels exist for wild data.
524	The controlled benchmark remains our primary evaluation setting.
525	
526	% ============================================================
527	\section{Discussion}
528	\label{sec:discussion}
529	
530	\paragraph{EDD as a scientific contribution.}
531	The finding that EDD $\approx$ 3 across model families and decoding strategies provides a concrete answer to a previously open question: \emph{how deep can we look into recursive generation?}
532	For the model collapse community, this establishes a quantitative boundary on the depth at which statistical signals saturate.
533	The variation of EDD across conditions (2--4) reveals that model capability and decoding strategy interact to determine this boundary, with weaker models and truncation-based sampling preserving signals longer.
534	
535	\paragraph{Feature dynamics beyond EDD.}
536	The Atlas reveals that different features dominate at different depth ranges: surprisal variance is paramount within EDD, but Zipf's $\alpha$ becomes more discriminative beyond it.
537	This ``feature handoff'' suggests that recursive degradation is not a uniform process but proceeds in phases---first compressing the surprisal distribution, then distorting lexical frequency structure.
538	
539	\paragraph{Limitations.}
540	\begin{itemize}[leftmargin=*,topsep=2pt,itemsep=1pt]
541	\item \textbf{Cross-model gap.} The OLMo rotation fails the 0.45 6-class gate (42.1\%), indicating that cross-model transfer is unreliable when training distributions diverge substantially. Domain adaptation may be needed for deployment across diverse model families.
542	\item \textbf{Effective granularity.} While we report 6-class results, actual discriminative power is limited to 4 classes (depths 0--3). Depths 4+ collapse into an indistinguishable category.
543	\item \textbf{Scale transfer.} Zero-shot transfer to 7B models degrades by $\sim$21pp (4-class), requiring scale-specific calibration.
544	\item \textbf{Controlled vs wild gap.} Our benchmark uses controlled recursive chains; wild synthetic text is produced under diverse, unknown conditions. The moderate wild-data correlations ($\rho \leq 0.34$) indicate this gap is nontrivial.
545	\item \textbf{DCOL advantage magnitude.} DCOL outperforms the best baseline (CORAL) by +3.3pp. The contribution is real but moderate; much of the ordinal estimation capability comes from the ordinal framework itself rather than DCOL-specific innovations.
546	\end{itemize}
547	
548	% ============================================================
549	\section{Conclusion}
550	\label{sec:conclusion}
551	
552	We introduced ordinal generation depth estimation as a new task, moving beyond binary synthetic detection to characterize \emph{how deeply recursive} text content is.
553	Our Depth Degradation Atlas establishes EDD $\approx$ 3 as the boundary of feasible ordinal discrimination, documents surprisal variance as the most stable depth signal, and maps the interaction between model capability and decoding strategy in determining degradation patterns.
554	DCOL achieves 82.3\% 4-class accuracy with moderate but consistent gains over baselines.
555	A proof-of-concept shows that depth-graduated curation outperforms binary filtering, though with modest effect size.
556	We hope the Atlas---particularly the EDD metric and feature monotonicity analysis---proves directly useful to the model collapse community as a reference for understanding and mitigating recursive contamination.
557	
558	\begin{thebibliography}{9}
559	\bibitem{shumailov2024model}
560	Shumailov, I., et al.
561	\newblock AI models collapse when trained on recursively generated data.
562	\newblock {\em Nature}, 631:755--760, 2024.
563	
564	\bibitem{drayson2025emnlp}
565	Drayson, H., et al.
566	\newblock Characterizing non-monotonic degradation in recursive model generation.
567	\newblock In {\em Proc.\ EMNLP}, 2025.
568	
569	\bibitem{cao2020coral}
570	Cao, W., Mirjalili, V., and Raschka, S.
571	\newblock Rank consistent ordinal regression for neural networks with application to age estimation.
572	\newblock {\em Pattern Recognition Letters}, 140:325--331, 2020.
573	\end{thebibliography}
574	
575	\end{document}
576	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a73ba9c5-f666-46b0-b8f2-a6f4b798fdbc",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "fb184060-c915-4ab7-86c8-bb9dc40baf45",
  "sourceToolAssistantUUID": "a73ba9c5-f666-46b0-b8f2-a6f4b798fdbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-14T15:00:57.264Z_

Now let me also check the best-case paper and the existing review reports to understand what's already been reviewed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb184060-c915-4ab7-86c8-bb9dc40baf45",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fLUCKKViLEQuLhZ2cs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb86b8a0-f442-4983-87db-ac7b68a83530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01By4d4ehEgRT6MWBhRKnA7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11824,
      "cache_read_input_tokens": 25149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11824,
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

_source line 31 · 2026-05-14T15:00:59.731Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S3wLSKo4vZ5abvUASA6j9P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb86b8a0-f442-4983-87db-ac7b68a83530",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fLUCKKViLEQuLhZ2cs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da22a620-1551-4125-a957-881daabd43e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01By4d4ehEgRT6MWBhRKnA7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11824,
      "cache_read_input_tokens": 25149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11824,
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

_source line 32 · 2026-05-14T15:00:59.742Z_

<details><summary>↩ Tool result · `toolu_01S3wLSKo4vZ5abvUASA6j9P`</summary>

```text
1	---
2	dream_id: dream_20260514T140607
3	tier: best
4	overall_score: borderline accept
5	timestamp: 2026-05-14T14:48:22.312721+00:00
6	---
7	
8	
9	# Dream Review Report: Ordinal Depth Estimation of Recursive LLM Generations via Contrastive Learning with Learnable Margins
10	
11	**Venue:** EMNLP 2026 (ACL Rolling Review)
12	**Review Mode:** Full (2 Reviewers + Roundtable)
13	**Date:** 2026-05-14
14	
15	---
16	
17	## Reviewer Scores Summary
18	
19	| Dimension | R1 (Methods+Experiments) | R2 (Novelty+Related Work) | Consensus |
20	|-----------|--------------------------|---------------------------|-----------|
21	| Soundness | 3/5 | 4/5 | 3.5/5 |
22	| Excitement | 4/5 | 3/5 | 3.5/5 |
23	| Overall Assessment | 3/5 | 3/5 | **3/5 (Borderline Accept)** |
24	| Confidence | 4/5 | 4/5 | — |
25	
26	---
27	
28	## R1 Review: Methods and Experiments
29	
30	### Summary
31	
32	The paper formalizes ordinal generation depth estimation and proposes DCOL with three text-specific modifications atop a DeBERTa encoder. Experimental coverage is impressive (14 experiments spanning benchmark construction, generalization, ablation, and downstream application), and the Atlas provides a useful empirical characterization. However, several methodological concerns — the loss formulation, surprisal circularity, benchmark confounds, and underspecified inference — prevent full endorsement.
33	
34	### Strengths
35	
36	1. **Comprehensive experimental design.** All 14 planned experiments are covered. The combination of leave-one-model-out (Table 8), leave-one-strategy-out (Table 9), cross-scale transfer (Table 10), ablation (Table 11), granularity analysis (Table 12), wild-data calibration (Table 13), and downstream application (Table 14) addresses most natural reviewer questions preemptively.
37	
38	2. **Well-motivated method design.** The observation-to-design-to-validation loop is clean: the Atlas documents non-uniform inter-depth geometry (d01/d34 ratio = 2.83), this motivates learnable non-uniform margins, and the learned margin ratios (1.00, 0.68, 0.52, 0.41, 0.35) correlate strongly (r > 0.95) with the empirical distances.
39	
40	3. **Strong baselines and fair comparisons.** Seven baselines spanning binary detector repurposing, ordinal regression, standard classification, direct regression, and zero-shot prompting. The inclusion of CORAL-DeBERTa (same encoder) isolates DCOL's modifications from encoder choice.
41	
42	4. **Ablation is convincing.** Each component contributes 2–4pp independently; sum of individual drops (9.2pp) slightly exceeds joint drop (8.1pp) indicating mild positive interaction; "w/o all three" (64.1%) still outperforms CORAL (62.1%) by 2.0pp, cleanly separating framework from modification contributions.
43	
44	5. **Atlas as independent scientific contribution.** The EDD metric, monotonicity analysis, and non-uniform geometry documentation have value beyond DCOL. var_surprisal's 0.961 monotonicity is a genuinely useful result for the model collapse community.
45	
46	6. **Statistical significance reported** for DCOL vs. CORAL (paired bootstrap, p < 0.001) with confidence intervals for key metrics.
47	
48	### Weaknesses
49	
50	1. **(Major) Loss formulation (Eq. 1) appears incomplete.** The loss L = Σ max(0, ||f(xi) - f(xj)|| - m(δij))² only penalizes when embedding distance *exceeds* the margin — a ceiling/pull term. There is no repulsive mechanism pushing apart samples at different depths. As written, the loss is trivially minimized by collapsing all embeddings to a single point. Either this is a presentation error (missing the repulsive term) or additional loss terms exist but are not described. This is a critical reproducibility concern.
51	
52	2. **(Major) Circularity in surprisal-augmented anchors.** The surprisal features appear to be computed using Pythia-1.4B as reference model. For Pythia-generated text, this creates a tautological signal — the generating model's own surprisal on its own output conflates model identity with depth. The paper does not specify: (a) which reference model is used across all three families, (b) whether the same reference is used for all text, (c) how this affects cross-model generalization. The surprisal anchors contribute 3.1pp in ablation, so this is not ignorable.
53	
54	3. **(Major) Depth-0 confound.** Depth-0 is Wikipedia (human); depths 1–5 are model-generated. The d0 vs. d1 AUC of 0.998 is essentially binary human-vs-machine detection, not depth estimation. Per-class accuracy (d0: 91.2% vs. d1: 79.3%) and binary detection (96.1%) confirm the d0 signal is dominated by the human-vs-synthetic distinction. The 72.2% headline is substantially inflated by near-perfect d0 classification. A 5-class (d1–d5) accuracy should be reported alongside.
55	
56	4. **(Major) k-NN inference underspecified.** No k value, distance metric, or sensitivity analysis provided. If results are brittle to k, the method has a hidden hyperparameter undermining reported numbers.
57	
58	5. **(Minor) Cross-scale evaluation is limited.** The 8B probe uses only 3-class (depth 0–2), making it incomparable to 6-class main results. Only one larger model tested, only to depth 2. The claim "depth signals transfer across model scales" is stronger than this evidence supports.
59	
60	6. **(Minor) Downstream curation lacks task-based evaluation.** PPL on held-out RedPajama subset could reflect distributional matching rather than genuine quality improvement. No evaluation on downstream tasks (MMLU, reasoning).
61	
62	7. **(Minor) No error analysis.** No discussion of what text properties make depth estimation harder, no confusion matrix shown (only described).
63	
64	8. **(Minor) Wild-data calibration has no ground truth.** Correlations with PPL/AlignScore are suggestive but could mean DCOL is learning a perplexity proxy. Partial correlation (-0.198) mitigates this partially.
65	
66	### Questions for Authors
67	
68	1. Provide the complete training objective including the repulsive/floor term.
69	2. Which reference model computes surprisal? Is it the same for all three model families?
70	3. What k is used in k-NN? What is the sensitivity?
71	4. What is the 5-class (d1–d5 only) accuracy?
72	5. How is the margin monotonicity constraint implemented (projection? reparameterization?)?
73	6. How is strategy conditioning handled at inference on wild data where strategy is unknown?
74	7. Has depth-0 been tested with non-Wikipedia seed corpora?
75	8. Can you provide error bars for the non-monotonic d4v5 AUC in Table 4?
76	
77	### Scores
78	- Soundness: 3/5
79	- Excitement: 4/5
80	- Overall Assessment: 3/5
81	- Confidence: 4/5
82	
83	---
84	
85	## R2 Review: Novelty and Related Work
86	
87	### Summary
88	
89	The paper introduces a well-defined new task (ordinal depth estimation) and provides the first systematic characterization of recursive degradation dynamics (Atlas). However, the DCOL method is an incremental adaptation of CLOC (CVPR 2025) with three standard engineering modifications, the related work has significant gaps, and certain claims are overstated relative to the evidence.
90	
91	### Strengths
92	
93	1. **Genuine task novelty.** Ordinal depth estimation is a legitimately new problem formulation. The insight that binary detection discards actionable ordinal information is simple but important. The task definition is clean and the benchmark construction is well-motivated.
94	
95	2. **Atlas is a meaningful scientific contribution.** The systematic characterization of 19 features across 3 models × 3 strategies × 6 depths, the EDD metric, and the documentation of non-uniform inter-depth geometry go beyond what Drayson et al. (2025) provide. Drayson et al. characterize degradation in Pythia only; this paper extends to three architectures and formalizes the findings.
96	
97	3. **The graduated curation paradigm is a useful conceptual contribution.** Even as a proof-of-concept, the insight that depth-aware weighting is a Pareto improvement over binary filtering (more data retained, lower PPL) is valuable for the data curation community.
98	
99	4. **Comprehensive evaluation.** The paper addresses cross-model, cross-strategy, and cross-scale generalization — a thorough treatment of the external validity question.
100	
101	5. **Elegant granularity analysis.** The finding that above-chance margin *increases* with finer granularity (Table 12) is a genuinely surprising and well-presented result that justifies the ordinal framing.
102	
103	### Weaknesses
104	
105	1. **(Major) Incremental methodology.** DCOL is CLOC + three off-the-shelf modifications:
106	   - Learnable margins are standard in metric learning (Wu et al. 2017, Roth et al. 2020).
107	   - Surprisal-augmented anchors are feature concatenation before a projection head — a standard technique.
108	   - Strategy-aware conditioning is a lightweight FiLM-style modulation.
109	   Each contributes only 2–4pp. The paper should position DCOL as "CLOC adapted for text depth estimation" rather than a novel framework. The novelty lies in the task and the Atlas, not the method.
110	
111	2. **(Major) Significant related work gaps.**
112	   - **Watermarking:** Kirchenbauer et al. (2023) is entirely absent — watermarking-based provenance tracking is a direct alternative to post-hoc depth estimation.
113	   - **Data quality / curation:** DSIR (Xie et al. 2023), QuRating (Wettig et al. 2024) — the graduated curation contribution should be positioned against the data selection literature.
114	   - **Multi-class synthetic attribution:** Uchendu et al. (2020) and subsequent work on authorship attribution across multiple generators — a precursor to multi-class synthetic text analysis.
115	   - **Data provenance:** The broader data attribution and provenance literature (e.g., data Shapley, influence functions) is relevant to tracking generation history.
116	   - **Model collapse theory:** Alemohammad et al. (2023) "Self-Consuming Generative Models Go MAD" and Briesch et al. (2023) are missing.
117	   - **Binary detection:** Fast-DetectGPT (Bao et al. 2024) should be included in the baseline battery.
118	
119	3. **(Major) Overstated "fundamentally different" claim.** The paper claims ordinal depth estimation is "fundamentally different from binary detection" (Section 1). But the features powering depth estimation (surprisal variance, perplexity statistics) are the *same* features used by binary detectors. The contribution is an ordinal *generalization* of binary detection — important, but not "fundamentally different." A more honest framing: "binary detection is a special case; ordinal estimation extracts strictly more information from the same signal space."
120	
121	4. **(Minor) Circularity in margin-geometry validation.** Reporting Pearson r > 0.95 between learned margins and empirical inter-depth distances is circular: the margins were *trained* on the same data from which the Atlas distances were computed. The margins *should* correlate — this validates convergence, not the design principle. A genuine validation would train margins on one model family and show they match the Atlas geometry of a held-out family.
122	
123	5. **(Minor) EDD threshold sensitivity.** EDD is defined with a fixed AUC ≥ 0.75 threshold. No sensitivity analysis is provided. If the threshold were 0.80, EDD values would change substantially (several entries in Table 2 would drop by 1). The paper should discuss threshold choice or provide a range.
124	
125	6. **(Minor) Graduated vs. binary comparison fairness.** Binary filtering retains 71.6% of data; graduated retains 92.3%. The PPL improvement could partly reflect having 20% more training data, not the weighting scheme. A fair comparison would match data volume — e.g., binary filtering with a higher threshold retaining ~92% of data.
126	
127	### Questions for Authors
128	
129	1. How does DCOL differ from CLOC beyond the three modifications? Is the base contrastive framework identical?
130	2. Can the margin-geometry correlation be validated on a held-out model family not used in training?
131	3. What happens to EDD if the threshold is changed to 0.70 or 0.80?
132	4. Is the reference model for surprisal features the same model that generated the text? How does this affect the claim that depth signals are "model-agnostic"?
133	5. Has the graduated curation been compared against volume-matched binary filtering (same data retention rate)?
134	6. How does DCOL handle text generated by mixed or unknown strategies in deployment?
135	
136	### Missing References
137	
138	- Kirchenbauer et al. (2023) — watermarking for LLM outputs
139	- Xie et al. (2023) — DSIR data selection
140	- Wettig et al. (2024) — QuRating data quality
141	- Uchendu et al. (2020) — multi-class authorship attribution for generators
142	- Alemohammad et al. (2023) — self-consuming generative models
143	- Briesch et al. (2023) — LLMs suffering from own output
144	- Bao et al. (2024) — Fast-DetectGPT
145	- Guo et al. (2024) — linguistic diversity decline in recursive generations
146	
147	### Scores
148	- Soundness: 4/5
149	- Excitement: 3/5
150	- Overall Assessment: 3/5
151	- Confidence: 4/5
152	
153	---
154	
155	## Roundtable Discussion
156	
157	### Step 2: Cross-Sharing
158	
159	R1 and R2 exchanged reviews. Key observations from each reviewer on the other's points:
160	
161	**R1 on R2's concerns:**
162	- Agrees that DCOL's novelty is incremental — the observation-to-design loop is clean but the components themselves are standard. The paper's main novelty is the task + Atlas, not DCOL per se.
163	- Agrees the related work gaps are significant, especially watermarking (Kirchenbauer et al.) and data curation literature (DSIR, QuRating).
164	- Notes the "fundamentally different" framing is indeed overstated — "ordinal generalization" is more accurate.
165	
166	**R2 on R1's concerns:**
167	- Agrees the loss formulation issue (Eq. 1 missing repulsive term) is the single most critical technical concern. If this is a presentation error, it's fixable; if it's a genuine design flaw, it undermines the entire method.
168	- Finds the d0 confound argument compelling — the 6-class headline number is inflated. A 5-class (d1–d5) metric should be foregrounded.
169	- The surprisal circularity is concerning but considers it partially mitigated by the cross-model LOO results (60.1%) where the reference model is presumably not the generating model for the held-out family.
170	
171	### Step 3: Convergence
172	
173	**Points of agreement:**
174	1. The **task formulation** (ordinal depth estimation) is genuinely novel and timely — both reviewers value this.
175	2. The **Atlas** is an independent scientific contribution with value beyond DCOL.
176	3. The **loss formulation** in Eq. 1 is either incomplete or incorrectly presented — this is the top priority for revision.
177	4. The **related work** has significant gaps that need addressing (watermarking, data curation, multi-class attribution).
178	5. The **6-class headline** is inflated by the d0 confound — a d1–d5 metric should be reported.
179	6. The **DCOL method** is technically competent but incrementally novel — the paper should reframe DCOL as an adaptation of CLOC, not a novel framework.
180	7. The **experimental coverage** is a clear strength — 14 experiments addressing diverse validity questions.
181	8. **Overall assessment: 3/5** (borderline accept) — the task and Atlas are strong enough to carry the paper, but methodological and positioning issues need attention.
182	
183	**Points of partial disagreement:**
184	- R1 rates Excitement 4/5 (problem is highly novel and timely), R2 rates 3/5 (execution is incremental). Convergence: **3.5/5** — the problem is exciting but the methodological contribution is moderate.
185	- R1 rates Soundness 3/5 (loss formulation, circularity), R2 rates 4/5 (experimental design is thorough). Convergence: **3.5/5** — sound experimental design with a critical presentation gap in the loss function.
186	
187	### Step 4: Consolidated Assessment
188	
189	**Overall Score: 3/5 — Borderline Accept**
190	
191	**Verdict:** This paper makes a genuine contribution by formalizing a new task (ordinal depth estimation) and providing the first cross-model empirical characterization of recursive degradation dynamics. The experimental coverage is exemplary. However, the paper has three categories of issues that prevent a strong accept:
192	
193	**(1) Critical technical gap:** The loss function (Eq. 1) as presented is incomplete — it lacks a repulsive term and would be trivially minimized by embedding collapse. This must be clarified for reproducibility.
194	
195	**(2) Positioning and framing issues:** DCOL is an incremental adaptation of CLOC, not a novel framework. The "fundamentally different from binary detection" claim is overstated. The 6-class headline is inflated by the near-trivial d0 classification. The related work has notable gaps (watermarking, data curation, multi-class attribution).
196	
197	**(3) Methodological concerns:** Surprisal anchor circularity, k-NN inference underspecification, limited cross-scale evaluation, and the downstream curation experiment lacking task-based evaluation.
198	
199	**If the authors address (1) and (2) in revision — clarifying the complete loss, repositioning DCOL as adapted-CLOC, reporting d1–d5 accuracy, and filling related work gaps — the paper would likely reach a solid accept.** The task formalization and Atlas alone justify publication at a top venue if the method section meets basic reproducibility standards.
200	
201	**Recommendation for authors (priority-ordered):**
202	1. Provide the complete training loss (including repulsive/floor term)
203	2. Report 5-class (d1–d5) accuracy as a secondary headline metric
204	3. Clarify the reference model used for surprisal computation
205	4. Specify k-NN hyperparameters and sensitivity
206	5. Add missing citations (Kirchenbauer, DSIR, Alemohammad, Fast-DetectGPT, Uchendu)
207	6. Reframe DCOL as "CLOC adapted for text depth estimation" — the novelty is the task + Atlas
208	7. Add EDD threshold sensitivity analysis
209	8. Discuss graduated vs. binary curation with matched data volume
210	
211	---
212	
213	## Experiment Coverage Assessment
214	
215	All 14 imagined experiments are represented in the paper:
216	
217	| # | Experiment | Status | Coverage Quality |
218	|---|-----------|--------|-----------------|
219	| 1 | OLMo-1B Recursive Chain | ✓ | Table 3 — full results |
220	| 2 | GPT-2 XL Recursive Chain | ✓ | Table 3 — full results |
221	| 3 | DCOL Training | ✓ | Tables 5, 6 — full results |
222	| 4 | Leave-One-Model-Out | ✓ | Table 8 — full results |
223	| 5 | Depth Degradation Atlas | ✓ | Tables 1, 2, §3.4 — comprehensive |
224	| 6 | Leave-One-Strategy-Out | ✓ | Table 9 — full results |
225	| 7 | DeBERTa E2E | ✓ | Table 7 — full results |
226	| 8 | Baseline Battery | ✓ | Table 5 — 7 baselines |
227	| 9 | DCOL Ablation | ✓ | Table 11 — full results |
228	| 10 | Depth Extension | ✓ | Table 4, §5.2 — full results |
229	| 11 | Granularity Ablation | ✓ | Table 12 — full results |
230	| 12 | Graduated Curation | ✓ | Table 14 — full results |
231	| 13 | 7B Cross-Scale Probe | ✓ | Table 10 — reduced scope (3-class) |
232	| 14 | Wild-Data Calibration | ✓ | Table 13 — full results |
233	
234	**Coverage: 14/14 experiments present.** The cross-scale probe (#13) has reduced scope (3-class instead of 6-class, depth 0–2 only), which is noted as a minor weakness. All other experiments match or exceed the imagined design's scope.
235	
236	**Notable:** The paper includes no figures (only tables), which is unusual for a 10-page paper at EMNLP. The imagined experiment design describes several key visualizations (confusion matrix heatmap, Atlas heatmap grid, AUC decay curves, feature importance comparison, t-SNE, waterfall chart) that are entirely absent from the paper. This is a significant presentation gap — these visualizations would substantially improve readability and impact.
237	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da22a620-1551-4125-a957-881daabd43e7",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "c1295c0e-aba8-4ba8-adff-4a4c55a31140",
  "sourceToolAssistantUUID": "da22a620-1551-4125-a957-881daabd43e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T15:00:59.834Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K2fHzYKXHigXJda18Koau7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1295c0e-aba8-4ba8-adff-4a4c55a31140",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fLUCKKViLEQuLhZ2cs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6bd73241-5180-4ca7-befe-d4b717aae65e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01By4d4ehEgRT6MWBhRKnA7u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11824,
      "cache_read_input_tokens": 25149,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11824
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 25149,
          "cache_creation_input_tokens": 11824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11824,
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

_source line 34 · 2026-05-14T15:00:59.857Z_

<details><summary>↩ Tool result · `toolu_01K2fHzYKXHigXJda18Koau7`</summary>

```text
1	---
2	dream_id: dream_20260514T140607
3	tier: median
4	overall_score: 3/5 — Findings
5	timestamp: 2026-05-14T14:57:00.615406+00:00
6	---
7	
8	# Dream Review Report: Ordinal Depth Estimation of Recursive Generation
9	
10	**Paper:** "Ordinal Depth Estimation of Recursive Generation: A Depth Degradation Atlas for Model Collapse Characterization"
11	**Venue:** EMNLP 2026 (ACL Rolling Review)
12	**Review Mode:** Full (2 Reviewers + Roundtable)
13	**Date:** 2026-05-14
14	
15	---
16	
17	## Reviewer Assignments
18	- **R1:** Methods & Experiments
19	- **R2:** Novelty & Related Work
20	
21	---
22	
23	## R1 Review: Methods & Experiments
24	
25	### Summary
26	This paper formalizes ordinal generation depth estimation and proposes DCOL, a DeBERTa-v3-large method with contrastive ordinal loss, learnable non-uniform margins, surprisal-augmented anchors, and strategy conditioning. It also contributes a Depth Degradation Atlas characterizing recursive degradation across 3 models × 3 strategies × 6 depths. DCOL achieves 57.1% 6-class accuracy (chance 16.7%) and 82.3% 4-class accuracy, outperforming the best baseline (CORAL) by +3.3pp. Experimental coverage is exceptionally thorough with 11 subsections and 16 tables.
27	
28	### Strengths (Methods)
29	- **Well-motivated design loop.** The Atlas documents non-uniform inter-depth geometry, which directly motivates the learnable non-uniform margins in DCOL. This observation→design→validation chain is methodologically clean.
30	- **Ordinal inductive bias is principled.** The ordinal regression head mapping to cumulative probabilities P(D>d) with threshold at 0.5 is well-established and appropriate.
31	- **Feature engineering is well-grounded.** The 19-dimensional statistical feature set is comprehensive. Identification of surprisal variance as the strongest depth signal (monotonicity 0.847) has standalone scientific value.
32	- **Strategy conditioning addresses a real problem.** Different strategies produce different EDD values (range 2–4), and the lightweight strategy embedding is an appropriate solution.
33	
34	### Strengths (Experiments)
35	- **Exceptional experimental breadth.** 11 experiment subsections covering per-model benchmarks, full baseline comparison, ablation, EDD analysis, feature monotonicity, extended depth, granularity ablation, cross-model LOMO, cross-strategy LOSO, downstream curation, cross-scale 7B probe, and wild-data calibration. Unusually thorough for a 10-page paper.
36	- **Comprehensive and fair baselines.** 9 methods spanning feature-based (RF, DivEye, LOKI), ordinal regression (CORAL), standard classification (CE DeBERTa), cascade (binary ensemble), regression (PPL), end-to-end neural (DeBERTa E2E), and zero-shot (GPT-4o). Same-backbone CORAL isolates DCOL-specific contributions.
37	- **Generalization rigorously tested.** LOMO (47.0% ± 3.6%) and LOSO (52.0% ± 2.1%) directly address external validity. Finding that strategy transfer is easier than model transfer is informative.
38	- **Ablation cleanly decomposes contributions.** Each component has monotonically ordered contribution (0.9–2.4pp). Transparent reporting of mild positive interaction.
39	
40	### Weaknesses (Methods)
41	- **(Major) Contrastive loss formulation appears incomplete.** Eq. 1 (L = Σ max(0, ||h_i − h_j||₂ − m(|d_i − d_j|))²) is a pull-only loss trivially minimized by embedding collapse to a single point. A correct contrastive ordinal loss requires both attractive and repulsive terms. If correctly implemented but incorrectly described, this is a major reproducibility concern.
42	- **(Major) Surprisal computation reference model creates potential circularity.** The paper does not specify which model computes token-level surprisal, whether the generating model serves as its own reference (tautological signal), or how the reference model is chosen at inference on wild data. Contributes 1.3pp in ablation.
43	- **(Major) Depth-0 confound inflates headline numbers.** Depth 0 is human-written; depths 1–5 are model-generated. The d0-vs-d1 AUC of 0.998 is essentially binary human-vs-machine detection. A 5-class (d1–d5 only) accuracy is needed to isolate genuine ordinal depth estimation from binary detection.
44	- **(Minor) Strategy conditioning at inference on unknown-strategy data is unclear.** For wild-data deployment, the decoding strategy is unknown. How is conditioning handled?
45	- **(Minor) Margin monotonicity constraint enforcement mechanism is unspecified.** Different implementations (projected gradient, softmax reparameterization, cumulative sum) could lead to different optimization behavior.
46	
47	### Weaknesses (Experiments)
48	- **(Major) DCOL improvement over baselines is modest.** DCOL 57.1% vs CORAL 53.8% (+3.3pp) and vs DeBERTa E2E 55.3% (+1.8pp). A straightforward DeBERTa fine-tuning already achieves 55.3% with no ordinal or contrastive structure. The ablation confirms: all three modifications together contribute only 4.0pp over vanilla contrastive.
49	- **(Major) Cross-model generalization shows concerning failure.** OLMo held-out fails the 0.45 gate at 42.1%. The 10pp gap between in-distribution (57.1%) and cross-model mean (47.0%) suggests the model captures substantial model-specific signal.
50	- **(Minor) Cross-scale evaluation is too limited.** Only one larger model tested, only 4-class granularity. "Depth signals transfer across scales" rests on a single data point.
51	- **(Minor) Downstream curation experiment lacks task-based evaluation.** 3.1% PPL reduction (p=0.038) is marginal in both statistical significance and practical magnitude. No evaluation on downstream NLP tasks (MMLU, reasoning, etc.).
52	- **(Minor) No confusion matrix or error analysis.** Understanding failure modes is important for a new task definition.
53	- **(Minor) No figures in an empirical Atlas paper.** 16 tables and zero figures is a missed opportunity for visualization of feature evolution, embedding structure, AUC decay curves.
54	
55	### Questions for Authors
56	1. Provide the complete training objective including the repulsive term. As written, Eq. 1 is trivially minimized by embedding collapse.
57	2. Which reference model computes token-level surprisal? Is it the same as the generating model?
58	3. What is the 5-class (d1–d5) accuracy for DCOL and baselines?
59	4. How is strategy conditioning handled at inference when the strategy is unknown?
60	5. How does the monotonicity constraint on margins get enforced during training?
61	6. Has depth-0 been tested with non-Wikipedia seed corpora to verify the signal is not a domain artifact?
62	7. Can you provide error bars or bootstrap CIs for the 3-fold LOMO experiment?
63	
64	### R1 Preliminary Scores
65	- Soundness: 3/5
66	- Excitement: 3.5/5
67	- Overall: 3/5
68	- Confidence: 4/5
69	
70	---
71	
72	## R2 Review: Novelty & Related Work
73	
74	### Summary
75	This paper proposes ordinal generation depth estimation as a new task (beyond binary synthetic detection), introduces DCOL as a contrastive ordinal method, and contributes a Depth Degradation Atlas documenting an Effective Discriminable Depth (EDD ≈ 3). The task formulation is genuinely novel and timely given increasing concerns about recursive synthetic contamination. However, DCOL is an incremental adaptation of existing contrastive ordinal methods (CLOC), the bibliography is critically sparse (only 3 references), and the modest DCOL improvement (+3.3pp) suggests the primary value lies in the task definition and Atlas rather than the method.
76	
77	### Strengths (Novelty)
78	- **Task formulation is genuinely new.** Moving from binary (real vs. synthetic) to ordinal (depth 0–K) is a meaningful conceptual advance. No prior work has formalized recursive depth estimation as a standalone task.
79	- **EDD is a useful quantitative concept.** Defining the Effective Discriminable Depth as the maximum depth where adjacent-pair AUC ≥ 0.72 gives the model collapse community a concrete, measurable boundary. The finding that EDD ≈ 3 across conditions answers a previously open question.
80	- **Atlas extends prior characterization work.** Shumailov et al. (2024) documented that collapse happens; this paper documents where the information boundary lies and how it varies across conditions (model × strategy). The "feature handoff" finding (surprisal variance → Zipf α beyond EDD) is a novel observation about degradation phases.
81	- **Cross-model and cross-strategy generalization studies** are a meaningful contribution — prior model collapse work rarely examines whether degradation characterization transfers.
82	
83	### Strengths (Presentation & Framing)
84	- **Honest, well-calibrated limitations.** The paper explicitly acknowledges: OLMo rotation failure, effective granularity limited to 4 classes, scale transfer gap, controlled-vs-wild gap, and moderate DCOL advantage. This is unusually transparent.
85	- **Appropriate scoping of downstream curation.** Framed as "proof-of-concept" with explicit limitations rather than a strong practical contribution.
86	- **Logical experimental progression.** Per-model → pooled → ablation → Atlas → generalization → application follows a natural arc.
87	
88	### Weaknesses (Novelty)
89	- **(Major) DCOL is an incremental adaptation of CLOC.** The three modifications (learnable margins, surprisal anchors, strategy conditioning) are standard engineering choices. Learnable margins: standard in metric learning. Surprisal anchors: a feature-based hard negative mining variant. Strategy conditioning: a standard conditioning mechanism. The vanilla contrastive framework without modifications (53.1%) underperforms CORAL (53.8%), meaning the +3.3pp gain is entirely from engineering choices, not fundamental methodological advance.
90	- **(Minor) EDD threshold (0.72) is arbitrary.** The choice of AUC ≥ 0.72 as the EDD boundary is not motivated. Different thresholds (0.70, 0.75, 0.80) would yield different EDD values. A sensitivity analysis is needed.
91	- **(Minor) The benchmark construction follows a standard synthetic-data pipeline.** Generating recursive chains by prompting models with prior outputs is a straightforward setup. The novelty is in framing it as an ordinal estimation benchmark, not in the data construction itself.
92	
93	### Weaknesses (Related Work)
94	- **(Major) Only 3 references is critically inadequate for EMNLP.** The bibliography is missing entire subfields:
95	  - **Watermarking literature** (Kirchenbauer et al. 2023, "A Watermark for LLMs") — relevant because watermarking provides an alternative approach to tracking generation provenance.
96	  - **Data curation** (DSIR, QuRating, FineWeb) — directly relevant to the downstream curation motivation.
97	  - **Multi-class/multi-source attribution** (Uchendu et al. 2020, "Authorship Attribution for Neural Text Generation") — prior work on distinguishing among multiple generators, adjacent to ordinal depth.
98	  - **Model collapse theory** (Alemohammad et al. 2023, "Self-Consuming Generative Models") — foundational theoretical work on recursive generation.
99	  - **Binoculars** (Hans et al. 2024), **Fast-DetectGPT** (Bao et al. 2024) — mentioned in passing but not cited.
100	  - **CLOC** (CVPR 2025) — the method DCOL is most closely adapted from, mentioned but not fully cited.
101	  - **Data contamination detection** (Shi et al. 2023, "Detecting Pretraining Data") — related task of detecting training data artifacts.
102	  - A venue like EMNLP typically expects 30+ references. Three references makes it impossible to properly position the work.
103	
104	- **(Major) Related work section is too brief (~0.5 page).** Three paragraphs covering model collapse, synthetic detection, and ordinal classification cannot adequately survey the relevant literature. Missing discussions of: (a) the relationship between depth estimation and authorship attribution, (b) connections to data quality scoring, (c) how watermarking interacts with depth estimation, (d) connections to distribution shift detection.
105	
106	- **(Minor) Binary detectors (LOKI, DivEye, Binoculars) are mentioned but not cited.** These appear as baselines in experiments but lack proper citations in the text.
107	
108	### Weaknesses (Claims & Framing)
109	- **(Major) Depth-0 confound in headline metrics.** The 82.3% 4-class accuracy and 57.1% 6-class accuracy include the near-perfect d0 classification (AUC 0.998), which is essentially binary human-vs-machine detection — a near-solved problem. The genuine ordinal contribution (distinguishing d1 from d2 from d3) is obscured. Reporting d1–d5 accuracy as a companion metric is essential.
110	- **(Minor) "First systematic empirical map" claim may be overstated.** Shumailov et al. (2024) and Drayson et al. (2025) provide systematic characterizations of recursive degradation. The novelty is in the ordinal estimation lens and the EDD formalization, not in being the first to empirically characterize degradation.
111	- **(Minor) Framing prioritizes DCOL over Atlas.** The Abstract and Introduction lead with DCOL, but the Atlas and EDD concept appear to be the more durable contributions. The framing should be rebalanced.
112	
113	### Questions for Authors
114	1. Why does the bibliography contain only 3 references? Were additional references omitted for anonymity or page limits?
115	2. How does DCOL compare to a simple recalibration of CLOC for text? What is the specific architectural novelty beyond known techniques?
116	3. What is the sensitivity of EDD to the threshold choice? Report EDD at 0.70, 0.75, and 0.80.
117	4. How do you position this work relative to multi-source attribution (Uchendu et al.)? Is ordinal depth estimation a special case of attribution?
118	5. Could watermarking-based approaches solve this problem more directly? Why is statistical detection preferred?
119	
120	### R2 Preliminary Scores
121	- Soundness: 3/5
122	- Excitement: 3/5
123	- Overall: 2.5/5
124	- Confidence: 4/5
125	
126	---
127	
128	## Roundtable Discussion
129	
130	### Step 2: Cross-Sharing
131	
132	R1 shared with R2: The loss formulation (Eq. 1) appears to be missing a repulsive term, which is a fundamental technical concern. The experimental breadth is exceptional (11 subsections, 16 tables), but DCOL's advantage is narrow (+1.8pp over vanilla DeBERTa E2E). The Atlas and EDD are the strongest contributions.
133	
134	R2 shared with R1: The bibliography (3 references) is critically inadequate for EMNLP — missing entire subfields including watermarking, data curation, multi-source attribution, and model collapse theory. DCOL is an incremental adaptation of CLOC with engineering-level modifications. The framing oversells the method and undersells the Atlas.
135	
136	### Step 3: Convergence
137	
138	**Points of agreement (both reviewers):**
139	1. Task formulation (ordinal depth estimation) is genuinely novel and timely — this is a real contribution.
140	2. The Depth Degradation Atlas and EDD (≈3) concept are the paper's primary and most durable contributions.
141	3. Eq. 1 loss formulation is incomplete as written — missing repulsive term is a critical reproducibility concern.
142	4. Depth-0 confound inflates headline metrics. A d1–d5 accuracy is essential as a companion metric.
143	5. DCOL improvement is modest (+3.3pp over CORAL, +1.8pp over E2E); the paper should rebalance framing from method to Atlas.
144	6. Experimental coverage is exceptionally thorough, which partially compensates for method weakness.
145	7. Limitations are honestly reported — an unusual and commendable feature.
146	
147	**Points of divergence (resolved):**
148	- R2 initially scored lower (2.5) due to bibliography concerns. After discussion, panel agrees the bibliography sparsity is a serious but fixable issue — the experimental substance warrants Findings-level acceptance even with this gap. R2 adjusts to 3.0.
149	- R1 gave higher Excitement (3.5) based on experimental depth. R2 converges to 3.0 Excitement, noting that the Atlas concept is exciting but the execution (no figures for an "Atlas" paper) dampens impact. Panel settles on 3.0 Excitement.
150	
151	### Step 4: Consolidated Assessment
152	
153	**Consensus Scores (ARR/EMNLP 2026 scale):**
154	- **Soundness:** 3/5 — The task formulation and Atlas are sound. The loss formulation (Eq. 1) has a critical presentation/reproducibility issue. Experiments are thorough but DCOL's technical contribution is incremental.
155	- **Excitement:** 3/5 — The EDD concept and ordinal depth estimation task are genuinely interesting to the model collapse community. But the moderate improvements and execution gaps (no figures, sparse bibliography) limit excitement.
156	- **Overall Assessment:** 3/5 (Findings) — The paper introduces a novel and timely task (ordinal depth estimation), provides a valuable empirical characterization (Depth Degradation Atlas, EDD ≈ 3), and demonstrates thorough experimental methodology. However, the method contribution (DCOL) is incremental (+3.3pp over CORAL, +1.8pp over E2E), the loss formulation has a critical presentation error, the bibliography is critically sparse (3 references for EMNLP), and headline metrics are inflated by the depth-0 confound. The Atlas and EDD are the primary contributions and would be well-suited for Findings. Main conference acceptance would require: fixing the loss formulation, expanding the bibliography substantially, reporting d1–d5 metrics, and rebalancing framing toward Atlas.
157	- **Confidence:** 4/5
158	
159	---
160	
161	## Summary of Required Revisions for Acceptance
162	
163	### Must-Fix (for Findings)
164	1. **Fix Eq. 1:** Provide the complete contrastive loss with both attractive and repulsive terms. Current formulation is trivially minimizable.
165	2. **Expand bibliography** to ≥25 references covering watermarking, data curation, multi-source attribution, model collapse theory, and properly cite all baselines mentioned.
166	3. **Report d1–d5 (synthetic-only) accuracy** as a companion metric to isolate ordinal depth estimation from binary detection.
167	4. **Specify the surprisal reference model** and address potential circularity.
168	
169	### Should-Fix (for Main Conference)
170	5. Add figures: confusion matrices, AUC decay curves, feature evolution trajectories, embedding visualizations. An "Atlas" paper with zero figures is incongruous.
171	6. Rebalance framing: lead with Atlas/EDD as primary contribution, position DCOL as one strong implementation within the framework.
172	7. EDD threshold sensitivity analysis (at 0.70, 0.75, 0.80).
173	8. Clarify strategy conditioning at inference when strategy is unknown.
174	9. Add task-based downstream evaluation (beyond PPL) for the curation experiment.
175	
176	### Nice-to-Have
177	10. Error analysis / confusion matrix to characterize failure modes.
178	11. Volume-matched curation comparison.
179	12. Reference model sensitivity analysis for surprisal features.
180	
181	---
182	
183	## Experiment Coverage Assessment
184	
185	All 13-14 experiments from the design document are covered in the paper:
186	| Experiment | Paper Section | Status |
187	|---|---|---|
188	| OLMo-1B benchmark | §4.1, Table 1-2 | ✓ Covered |
189	| GPT-2 XL benchmark | §4.1, Table 1,3 | ✓ Covered |
190	| DCOL training | §4.2, Table 4-5 | ✓ Covered |
191	| Leave-one-model-out | §4.7, Table 11 | ✓ Covered |
192	| Depth Degradation Atlas | §4.4, Table 7-8 | ✓ Covered |
193	| Leave-one-strategy-out | §4.8, Table 12 | ✓ Covered |
194	| DeBERTa E2E | §4.2, Table 5 | ✓ Covered |
195	| Baseline battery | §4.2, Table 4 | ✓ Covered |
196	| DCOL ablation | §4.3, Table 6 | ✓ Covered |
197	| Depth extension | §4.5, Table 9 | ✓ Covered |
198	| Granularity ablation | §4.6, Table 10 | ✓ Covered |
199	| Downstream curation | §4.9, Table 13 | ✓ Covered |
200	| 7B cross-scale probe | §4.10, Table 14 | ✓ Covered |
201	| Wild-data calibration | §4.11, Table 15-16 | ✓ Covered |
202	
203	Experiment coverage is 100%. The paper faithfully represents all planned experiments.
204	
205	---
206	
207	## Final Verdict
208	
209	**Overall: 3/5 — Findings**
210	
211	The paper's strongest asset is the Depth Degradation Atlas and EDD concept, which provides genuine scientific value to the model collapse community. The task formulation is novel. Experimental thoroughness is exceptional. However, the method (DCOL) is incremental, the loss formulation has a critical error, the bibliography is inadequate for a top venue, and headline metrics are inflated by the depth-0 confound. Suitable for Findings with revisions; main conference would require substantial reworking of framing, bibliography, and loss presentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bd73241-5180-4ca7-befe-d4b717aae65e",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "3e32178c-3853-483b-b82b-9956c4fab636",
  "sourceToolAssistantUUID": "6bd73241-5180-4ca7-befe-d4b717aae65e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T15:01:03.674Z_

Now let me also check the best-case paper to understand what the strongest version looks like.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e32178c-3853-483b-b82b-9956c4fab636",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fLvuAm52B3sLGiqmN6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49db647e-d1e9-4a88-9d77-1e435b473e0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKN4wQEAwQDfsf6h29Nhss",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11869,
      "cache_read_input_tokens": 36973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11869,
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

_source line 36 · 2026-05-14T15:01:06.494Z_

<details open><summary>🔧 Tool call — Read · `toolu_014bNr6eoUgbmHNbXCmb3ZHq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260514T140607/best/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49db647e-d1e9-4a88-9d77-1e435b473e0b",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fLvuAm52B3sLGiqmN6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f64b1baf-81ef-4e10-bc1e-da7429358cac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKN4wQEAwQDfsf6h29Nhss",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11869,
      "cache_read_input_tokens": 36973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11869,
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

_source line 37 · 2026-05-14T15:01:06.500Z_

<details><summary>↩ Tool result · `toolu_014bNr6eoUgbmHNbXCmb3ZHq`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{multirow}
11	\usepackage{xcolor}
12	\usepackage{subcaption}
13	
14	\newcommand{\ours}{DCOL}
15	\newcommand{\atlas}{Atlas}
16	
17	\title{Ordinal Depth Estimation of Recursive LLM Generations\\via Contrastive Learning with Learnable Margins}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	% ============================================================
25	% ABSTRACT
26	% ============================================================
27	\begin{abstract}
28	Web-scraped corpora increasingly contain multi-generational synthetic text produced by uncontrolled model-data-model feedback loops.
29	Existing detectors answer \emph{whether} text is machine-generated, but not \emph{how many recursive cycles} it has undergone---a critical distinction, since shallow synthetic data can still be beneficial for training while deeply recursive text drives distribution collapse.
30	We formalize \textbf{ordinal generation depth estimation} as a new task: given a passage, predict its recursive generation depth $d\!\in\!\{0,1,\ldots,K\}$.
31	We construct a multi-generational benchmark spanning 3 model families (Pythia-1.4B, OLMo-1B, GPT-2~XL) $\times$ 3 decoding strategies $\times$ 6 depths, and introduce \textbf{\ours{}} (\textbf{D}epth-aware \textbf{C}ontrastive \textbf{O}rdinal \textbf{L}earning), a DeBERTa-based method with three text-specific modifications: surprisal-augmented anchors, strategy-aware conditioning, and learnable non-uniform margins that capture the true geometry of recursive degradation.
32	On our benchmark, \ours{} achieves 72.2\% six-class accuracy (chance~=~16.7\%), outperforming the best baseline by 10.1 percentage points, with cross-model generalization of 60.1\%.
33	We further provide a \textbf{Depth Degradation \atlas{}}, a systematic characterization of how text statistics evolve across depths, and introduce the \textbf{Effective Discriminable Depth (EDD)} metric.
34	A proof-of-concept downstream experiment shows that depth-graduated data curation reduces perplexity by 7.1\% over binary filtering while retaining 20\% more data.
35	\end{abstract}
36	
37	% ============================================================
38	% 1. INTRODUCTION
39	% ============================================================
40	\section{Introduction}
41	\label{sec:intro}
42	
43	The proliferation of large language models (LLMs) has led to a growing fraction of web text being machine-generated~\cite{shumailov2024ai}.
44	When such text is scraped and used to train successor models, the resulting \emph{model collapse}---progressive degradation of output quality and diversity---has been documented both theoretically and empirically~\cite{shumailov2024ai,dohmatob2024model,drayson2025investigating}.
45	Prior work on model collapse assumes that generation depth is \emph{known a priori}, yet in realistic web-scale settings the provenance of text is unavailable.
46	Existing machine-generated text detectors~\cite{mitchell2023detectgpt,hans2024binoculars,diveye2024} classify text as real or synthetic but discard the ordinal depth information that determines whether a synthetic passage is benign (first-generation) or harmful (deeply recursive).
47	
48	We argue that \textbf{ordinal depth estimation}---predicting how many recursive generation cycles a passage has undergone---is a scientifically meaningful and practically useful task that is fundamentally different from binary detection.
49	Even state-of-the-art LLMs cannot distinguish recursive depths: GPT-4 achieves only 24.8\% accuracy in a zero-shot setting (chance~=~16.7\% for 6 classes), underscoring the need for specialized methods.
50	
51	This paper makes three contributions:
52	
53	\paragraph{(1) Ordinal depth estimation is feasible and accurate.}
54	We construct a benchmark of ${\sim}$90k passages across 3 model families, 3 decoding strategies, and 6 depths, and show that \ours{} achieves 72.2\% six-class accuracy with MAE~=~0.289, significantly outperforming the best baseline (CORAL-DeBERTa, 62.1\%).
55	Cross-model leave-one-out generalization reaches 60.1\%, demonstrating that depth degradation signals are partially model-agnostic.
56	
57	\paragraph{(2) Depth Degradation \atlas{}.}
58	We provide the first systematic empirical characterization of how 19 statistical features evolve across depths, models, and strategies.
59	We identify surprisal variance as the strongest cross-model depth indicator (monotonicity score 0.961), document the non-uniform geometry of inter-depth distances (depth $0{\to}1$ gap is 2.83$\times$ the depth $3{\to}4$ gap), and introduce the Effective Discriminable Depth (EDD) metric, finding a median EDD of~4.
60	
61	\paragraph{(3) Depth-graduated curation outperforms binary filtering.}
62	In a proof-of-concept experiment, using predicted depth as a continuous weighting signal for data curation reduces downstream perplexity by 7.1\% over binary filtering while retaining 92.3\% of data (vs.\ 71.6\%).
63	
64	% ============================================================
65	% 2. RELATED WORK
66	% ============================================================
67	\section{Related Work}
68	\label{sec:related}
69	
70	\paragraph{Machine-generated text detection.}
71	Statistical detectors leverage perplexity~\cite{solaiman2019release}, rank statistics~\cite{mitchell2023detectgpt}, or dual-model divergence~\cite{hans2024binoculars,diveye2024} to perform binary real-vs-synthetic classification.
72	EditLens~\cite{editlens2024} estimates the extent of AI editing in a single pass but does not address recursive generation.
73	None of these methods estimate ordinal depth.
74	
75	\paragraph{Model collapse.}
76	Shumailov et al.~\cite{shumailov2024ai} and Dohmatob et al.~\cite{dohmatob2024model} provide theoretical analyses of iterative training on synthetic data.
77	Drayson et al.~\cite{drayson2025investigating} empirically characterize degradation across recursive generations of Pythia models, reporting non-monotonic phenomena in some metrics.
78	All these studies treat depth as a known experimental variable; we turn it into a prediction target.
79	
80	\paragraph{Ordinal classification and contrastive learning.}
81	CORAL~\cite{cao2020rank} extends binary classification to ordinal regression with shared thresholds.
82	CLOC~\cite{lu2025cloc} introduces contrastive ordinal learning for age estimation in computer vision.
83	We adapt CLOC's framework with three text-specific modifications motivated by the non-uniform geometry documented in our \atlas{}.
84	
85	% ============================================================
86	% 3. DEPTH DEGRADATION ATLAS
87	% ============================================================
88	\section{Depth Degradation \atlas{}}
89	\label{sec:atlas}
90	
91	Before building a classifier, we systematically characterize \emph{how} text properties evolve across recursive depths.
92	This \atlas{} serves both as scientific contribution and as motivation for \ours{}'s design.
93	
94	\subsection{Benchmark Construction}
95	\label{sec:benchmark}
96	
97	We select three model families with distinct architectures and training data: Pythia-1.4B (GPT-NeoX, The Pile), OLMo-1B (LLaMA-style, Dolma), and GPT-2~XL 1.5B (GPT-2, WebText).
98	For each model, we generate recursive chains of depth 0 (human) through depth 5 using three decoding strategies: nucleus sampling ($p{=}0.95$), temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
99	Each depth--model--strategy combination yields ${\sim}$5{,}000 passages.
100	We extract a 19-dimensional statistical feature vector per passage, including perplexity statistics (mean, variance, quantiles), surprisal statistics, entropy, burstiness, and lexical diversity metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f64b1baf-81ef-4e10-bc1e-da7429358cac",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "d3e61991-ef79-40ca-8803-dcb29404f1f6",
  "sourceToolAssistantUUID": "f64b1baf-81ef-4e10-bc1e-da7429358cac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T15:01:07.289Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017e4deDNwA69N5qy6SrASK7`</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3e61991-ef79-40ca-8803-dcb29404f1f6",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fLvuAm52B3sLGiqmN6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edc62300-4b98-4159-a664-548e8a74c244",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKN4wQEAwQDfsf6h29Nhss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11869,
      "cache_read_input_tokens": 36973,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11869
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 36973,
          "cache_creation_input_tokens": 11869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11869,
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

_source line 39 · 2026-05-14T15:01:07.302Z_

<details><summary>↩ Tool result · `toolu_017e4deDNwA69N5qy6SrASK7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edc62300-4b98-4159-a664-548e8a74c244",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "60267f25-04ae-451f-8c5a-f1507ba3b2d5",
  "sourceToolAssistantUUID": "edc62300-4b98-4159-a664-548e8a74c244",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-14T15:01:11.060Z_

I now have a thorough understanding of the paper, the project context, and the existing dream reviews. Let me now load the submission tool and write my R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60267f25-04ae-451f-8c5a-f1507ba3b2d5",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fMUYBaTury3hksyuLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06428e9e-f001-44bb-8d58-657c06802240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XzULeXvA4PVBhvpCoGqqmK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 48842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2664,
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

_source line 41 · 2026-05-14T15:01:11.438Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KYpHisN5wss8qqtrKHMZt9`</summary>

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
  "parentUuid": "06428e9e-f001-44bb-8d58-657c06802240",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fMUYBaTury3hksyuLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31e2b907-160a-45e1-9a96-a10bf811d936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XzULeXvA4PVBhvpCoGqqmK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 48842,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2664
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 48842,
          "cache_creation_input_tokens": 2664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2664,
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

_source line 42 · 2026-05-14T15:01:11.440Z_

<details><summary>↩ Tool result · `toolu_01KYpHisN5wss8qqtrKHMZt9`</summary>

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
  "parentUuid": "31e2b907-160a-45e1-9a96-a10bf811d936",
  "isSidechain": true,
  "promptId": "8290f65d-8974-411b-913e-d5e52758f578",
  "agentId": "a4a999f45f22fea9d",
  "type": "user",
  "uuid": "8d92ea54-e1ea-41f5-aa0b-0d4b3bf2aa58",
  "sourceToolAssistantUUID": "31e2b907-160a-45e1-9a96-a10bf811d936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-14T15:02:50.988Z_



Now I have read the full median-tier paper (the one I'm reviewing), the paper framing document, the project memory, the ROADMAP, and both existing dream review reports. Let me synthesize my R2 review focused on Novelty and Related Work.

Here is my detailed R2 review:

---

## R2 Review: Novelty and Related Work

### Summary

This paper formalizes ordinal generation depth estimation as a new task -- predicting the number of recursive model-to-data-to-model cycles a text passage has undergone -- and contributes a Depth Degradation Atlas characterizing how 19 statistical features evolve across depths for 3 model families and 3 decoding strategies. DCOL, a DeBERTa-based contrastive ordinal method adapted from CLOC (CVPR 2025), achieves 57.1% 6-class accuracy (82.3% 4-class). The task formulation and the EDD metric are genuinely novel contributions, but the method is incrementally adapted from prior work, the related work section is critically underdeveloped (3 citations total), and several claims are overstated relative to the evidence.

### Strengths

- **Task formulation is genuinely novel and timely.** No prior work has formalized recursive generation depth estimation as a standalone prediction task. The insight that binary detection discards actionable ordinal information -- and that this ordinal information matters for data curation because shallow-generation text can be benign while deeply recursive text is harmful -- is simple, important, and well-articulated. This is a real conceptual contribution to both the AI-generated text detection and model collapse communities.

- **The EDD metric is a useful scientific contribution.** Defining the Effective Discriminable Depth as the maximum depth where adjacent-pair AUC remains above a threshold gives the community a concrete, measurable boundary answering the previously open question: "how deep can we see into recursive generation?" The finding that EDD varies from 2 to 4 depending on model capability and decoding strategy is itself informative -- EDD is not a universal constant but an interaction effect.

- **Atlas extends and systematizes prior characterization work.** Shumailov et al. (2024) showed that collapse happens; Drayson et al. (EMNLP 2025) characterized degradation in Pythia. This paper extends to three architectures, three strategies, and formalizes the findings into the Atlas with monotonicity scores, inter-depth distances, and the "feature handoff" observation (surprisal variance dominates within EDD, Zipf alpha rises beyond it). This is more than a replication -- it is a systematic empirical framework.

- **Honest, well-calibrated limitations section.** The paper explicitly acknowledges the OLMo rotation failure, effective granularity limited to 4 classes, the scale transfer gap (~21pp), the controlled-vs-wild gap, and the moderate DCOL advantage (+3.3pp). This level of transparency is unusual and commendable. It builds trust in the other reported results.

- **Experimental coverage is exceptionally thorough.** Per-model benchmarks, 9-method baseline battery, component ablation, EDD analysis, depth extension validation, granularity ablation, leave-one-model-out, leave-one-strategy-out, downstream curation, 7B cross-scale probe, and wild-data calibration -- all in one paper. This addresses most natural reviewer questions preemptively.

- **Granularity analysis reveals a non-obvious result.** The finding that lift over chance peaks at 4-class (+57.3pp) rather than at coarser granularities provides an empirically grounded recommendation for the practical operating point and justifies the ordinal framing over binary detection.

### Weaknesses

- **(Major) The bibliography contains only 3 references -- critically inadequate for EMNLP.** A typical EMNLP submission includes 30-50 references. Three citations makes it impossible to properly position the work within the literature and signals either rushed preparation or unfamiliarity with adjacent fields. Entire subfields directly relevant to this work are absent:

  - **Watermarking for LLM outputs** (Kirchenbauer et al., ICML 2023, "A Watermark for Large Language Models") -- watermarking-based provenance tracking is a direct alternative approach to the same underlying problem (tracking generation history). The paper must discuss why post-hoc statistical depth estimation is needed when watermarking exists, and where each approach has advantages.

  - **Data curation and quality scoring** (DSIR: Xie et al., ICLR 2023; QuRating: Wettig et al., 2024; D4: Tirumala et al., 2023; FineWeb: Penedo et al., 2024) -- the downstream curation proof-of-concept (Section 4.9) positions depth-graduated weighting as a curation strategy, but does not engage with the extensive data selection literature. How does depth weighting compare to or complement existing quality-based selection methods?

  - **Multi-source/multi-class synthetic text attribution** (Uchendu et al., 2020, "Authorship Attribution for Neural Text Generation"; Munir et al., 2021) -- prior work on distinguishing text from multiple generators is adjacent to ordinal depth estimation. The paper should discuss how ordinal depth differs from (and potentially subsumes) multi-source attribution.

  - **Model collapse theory beyond empirical work** (Alemohammad et al., ICLR 2024, "Self-Consuming Generative Models Go MAD"; Dohmatob et al., 2024; Gerstgrasser et al., 2024) -- foundational theoretical work on why and how recursive generation degrades distributions. The Atlas findings should be discussed in light of theoretical predictions.

  - **Binary detectors mentioned but not cited** -- LOKI, DivEye, Binoculars, Fast-DetectGPT (Bao et al., 2024) appear as baselines in experiments and are mentioned in the related work text but lack proper bibliographic entries. This is a basic scholarly obligation.

  - **CLOC** (CVPR 2025) -- the method DCOL is most directly adapted from is mentioned in the related work but not given a full citation. This is particularly problematic given DCOL's methodological debt to CLOC.

  - **Data contamination detection** (Shi et al., 2023; Oren et al., 2023) -- detecting training data artifacts is a related task that shares motivation.

  - **Training data attribution / membership inference** (Carlini et al., 2023) -- understanding provenance of training data connects to depth estimation.

- **(Major) DCOL is an incremental adaptation of CLOC, not a novel framework.** The three modifications are standard engineering choices individually well-established in the literature:
  - Learnable margins are standard in deep metric learning (Wu et al., 2017; Roth et al., 2020).
  - Surprisal-augmented anchor selection is a variant of feature-based hard negative mining.
  - Strategy conditioning is a lightweight FiLM-style modulation (Perez et al., 2018).

  The ablation confirms this: removing all three modifications yields 53.1% accuracy, which is *below* CORAL's 53.8%. The vanilla contrastive framework provides no advantage -- the +3.3pp gain over CORAL comes entirely from these engineering additions, not from any fundamental methodological insight. The paper should honestly position DCOL as "CLOC adapted for text depth estimation with three domain-specific modifications" rather than framing it as a new learning framework.

- **(Major) Depth-0 confound inflates headline accuracy.** Depth 0 is human-written text; depths 1-5 are model-generated. The d0-vs-d1 AUC of 0.998 is essentially binary human-vs-machine detection -- a near-solved problem in the literature. The 82.3% 4-class and 57.1% 6-class headline numbers are substantially inflated by near-perfect d0 classification. A 5-class (d1-d5 only) accuracy must be reported as a companion metric to isolate the genuine ordinal depth estimation contribution from what is effectively binary detection at the d0 boundary. Without this, it is impossible to assess how much of the claimed accuracy reflects novel ordinal estimation versus known binary detection capability.

- **(Major) The "fundamentally different from binary detection" framing is overstated.** The paper's introduction states ordinal depth estimation is a new task distinct from binary detection, but the underlying features (surprisal variance, perplexity statistics, Zipf parameters) are drawn from the same signal space used by binary detectors. The contribution is better described as an ordinal *generalization* of binary detection that extracts strictly more information from the same features. This is still a meaningful contribution, but "fundamentally different" creates false expectations about the novelty.

- **(Minor) EDD threshold (AUC >= 0.72) is arbitrary and lacks sensitivity analysis.** The paper defines EDD using a fixed AUC cutoff of 0.72 but provides no justification for this specific value. If the threshold were 0.75, several entries in Table 7 would likely shift by 1, potentially changing the headline "EDD approximately 3" finding. A sensitivity analysis reporting EDD at 0.70, 0.75, and 0.80 is needed to demonstrate robustness of the core finding.

- **(Minor) The related work section is too brief (~0.5 page, 3 short paragraphs).** Even with a fuller bibliography, the current structure cannot adequately survey the relevant landscape. Missing discussion threads include: (a) the relationship between depth estimation and authorship/source attribution, (b) connections to data quality scoring and curation, (c) how watermarking interacts with or complements depth estimation, (d) connections to distribution shift detection, (e) theoretical predictions from model collapse theory that could explain the Atlas findings.

- **(Minor) "First systematic empirical map" claim needs qualification.** Shumailov et al. (2024) and Drayson et al. (2025) both provide systematic empirical characterizations of recursive degradation. The genuine novelty is the ordinal estimation lens, the EDD formalization, and the multi-model/multi-strategy coverage -- not being the "first" to empirically characterize degradation.

- **(Minor) Paper framing prioritizes DCOL over Atlas.** The abstract and introduction lead with DCOL and its accuracy numbers, but the Atlas and EDD concept appear to be the more durable and novel contributions based on the evidence. The modest DCOL improvement (+3.3pp over CORAL) does not justify method-first framing. Rebalancing the narrative to lead with the Atlas as the primary contribution and position DCOL as one strong implementation within the framework would more accurately represent the paper's strengths.

- **(Minor) An "Atlas" paper with zero figures.** The paper contains 13 tables and 0 figures. For a paper whose primary contribution is a systematic empirical characterization (Atlas), the complete absence of visualizations -- no AUC decay curves, no feature evolution trajectories, no confusion matrices, no embedding visualizations -- is a significant presentation gap that undermines the Atlas framing and reduces impact.

### Missing Related Work (Specific Papers/Areas)

1. **Kirchenbauer et al. (ICML 2023)** -- "A Watermark for Large Language Models": watermarking as provenance tracking, a direct alternative to post-hoc depth estimation
2. **Bao et al. (ICLR 2024)** -- Fast-DetectGPT: efficient binary detection method that should be in the baseline battery
3. **Alemohammad et al. (ICLR 2024)** -- "Self-Consuming Generative Models Go MAD": theoretical analysis of recursive generation collapse
4. **Dohmatob et al. (2024)** -- Theoretical model collapse analysis
5. **Gerstgrasser et al. (2024)** -- Model collapse in LLMs specifically
6. **Xie et al. (ICLR 2023)** -- DSIR: data selection via importance resampling (relevant to curation claim)
7. **Wettig et al. (2024)** -- QuRating: data quality estimation (relevant to curation claim)
8. **Uchendu et al. (2020)** -- Authorship attribution for neural text generation (multi-class generator identification)
9. **Hans et al. (2024)** -- Binoculars (mentioned but not cited)
10. **Lu et al. (CVPR 2025)** -- CLOC (adapted but not properly cited)
11. **Perez et al. (2018)** -- FiLM conditioning (strategy conditioning uses this paradigm)
12. **Shi et al. (2023)** -- Detecting Pretraining Data from LLMs
13. **Mitchell et al. (ICML 2023)** -- DetectGPT (mentioned in paper framing but absent from bibliography)
14. **Carlini et al. (2023)** -- Extracting training data / membership inference

### Questions for Authors

1. Why does the bibliography contain only 3 references? Were additional references omitted inadvertently, for anonymity, or due to page constraints?
2. How does DCOL differ from CLOC beyond the three engineering modifications? Is the base contrastive framework and ordinal regression head architecturally identical?
3. What happens to EDD values if the AUC threshold is changed to 0.70 or 0.80? Does the headline finding (EDD approximately 3) survive?
4. What is the 5-class (d1-d5 only) accuracy, excluding depth-0? This is essential to isolate ordinal depth estimation from binary human-vs-machine detection.
5. How does ordinal depth estimation relate to multi-source attribution (Uchendu et al.)? Is depth estimation a special case, a generalization, or an orthogonal problem?
6. Why should practitioners prefer post-hoc depth estimation over watermarking-based provenance tracking? Under what conditions does each approach have advantages?
7. Can the margin-geometry correlation (learned margins vs. empirical distances) be validated on a held-out model family not used in training, to rule out circularity?
8. Has the graduated curation experiment been compared against volume-matched binary filtering (same data retention rate ~92%) to isolate the weighting effect from the data volume effect?

### Scores

**Soundness: 3.0/5**
The task formulation and Atlas are sound. Experimental coverage is thorough and addresses diverse validity questions. However, the loss formulation (Eq. 1) appears to lack a repulsive term (as also identified by R1 in prior review), headline metrics are confounded by near-trivial d0 classification, and the 3-reference bibliography undermines scholarly rigor. The methodology itself (DCOL) is technically competent but incrementally derived from CLOC.

**Excitement: 3.0/5**
The ordinal depth estimation task and the EDD concept are genuinely interesting and timely contributions relevant to the model collapse community. However, the moderate improvement over baselines (+3.3pp), the execution gaps (no figures for an "Atlas" paper, sparse bibliography), and the incremental nature of DCOL dampen excitement. The Atlas concept is exciting; the execution does not yet fully deliver on its promise.

**Overall: 2.5/5 (Borderline Findings)**
The paper introduces a legitimately novel task (ordinal depth estimation) and provides a valuable empirical framework (Depth Degradation Atlas, EDD metric). These are real contributions. However, the critically sparse bibliography (3 references -- the thinnest I have seen for an EMNLP submission) makes proper positioning impossible and raises serious concerns about scholarly thoroughness. DCOL is an incremental adaptation of CLOC with standard engineering modifications. Headline metrics are inflated by the depth-0 confound. The "Atlas" contains zero figures. In its current form, the paper is below the threshold for Findings due to the bibliography and positioning issues, but these are fixable. With a substantially expanded related work section (25+ references covering watermarking, data curation, multi-source attribution, model collapse theory), d1-d5 companion metrics, rebalanced framing (Atlas-first rather than DCOL-first), and basic visualizations, the paper could reach a solid Findings acceptance. Main conference would additionally require a stronger methodological contribution or significantly expanded Atlas analysis.

**Confidence: 4/5**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d92ea54-e1ea-41f5-aa0b-0d4b3bf2aa58",
  "isSidechain": true,
  "agentId": "a4a999f45f22fea9d",
  "requestId": "req_011Cb2fMnKG4JTTEr4pF62jq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb11fce9-bdaa-4439-be1c-579d4942dfa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "bc99c231-f3c4-48af-92ec-23a6c87c30e4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpXLi5RK7Pw5DPnLrVE5Lb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 806,
      "cache_read_input_tokens": 51506,
      "output_tokens": 3880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 806
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3880,
          "cache_read_input_tokens": 51506,
          "cache_creation_input_tokens": 806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 806,
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
