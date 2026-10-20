# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **Novelty and Related Work**. Review the paper below us

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6ecab78ebadf1237.jsonl`
- **Structured JSON:** [`c94f60dc70f9b6e3617d.json`](../../sessions/c9/c94f60dc70f9b6e3617d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

64 recorded events

### User

_source line 1 · 2026-05-14T08:24:51.202Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **Novelty and Related Work**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

**Title**: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"

**System name**: STRUCTFUSE

**Core claims**:
1. True embedding-distance hard negative mining consistently improves code retrieval over random baselines (+2.3pp R@1 on Qwen, +1.7pp on StarCoder; both p<0.01), correcting CoCoHaNeRe's misconception.
2. Dataflow-aware negatives provide *conditional* benefit mediated by representation saturation — significant on Qwen (pos_sim=0.986) but not StarCoder (pos_sim=0.799).
3. Mechanism explained by negative-difficulty margins and representation geometry.
4. SWE-bench Lite downstream confirms transfer (+2.3pp embedding, +3.3pp dataflow vs random).

**Method**:
- 3 negative mining strategies: random, embedding-distance, dataflow-aware (CodeQL inter-procedural call-graph, 2-hop)
- Contrastive bi-encoder with LoRA rank-16, 3 epochs, 5K SWE-smith training instances
- 2 encoders × 3 strategies × 9 seeds
- CodeQL extraction pipeline for Python repos

**Related Work as written in paper (Section 2)**:
- Code retrieval: SweRank, SWE-Fixer (text-based negatives), RepoFusion (cross-file context, not negatives), GraphCodeBERT (dataflow as pretraining signal, not mining criterion)
- Hard negative mining: ANCE (NLP, async index), curriculum methods, CoCoHaNeRe (conflates BM25 with embedding distance)
- Graph-guided: LocAgent, CodexGraph (inference-time graph navigation), ARISE (intra-procedural dataflow), RANGER (retrieval + graph reranking). All inference-time; none inject structural signal into training.

**Key experimental results**:

Table 1 — Qwen 9-seed: Random 0.533, Embedding 0.556 (+2.3pp, p=0.003), Dataflow 0.548 (+1.5pp, p=0.018)
Table 2 — StarCoder 9-seed: Random 0.490, Embedding 0.507 (+1.7pp, p=0.008), Dataflow 0.488 (p=0.62)
Table 3 — SWE-bench Lite: Random 22.7%, Embedding 25.0%, Dataflow 26.0%
Table 4 — Bootstrap CIs: Embed vs Random [0.4, 4.2] p=0.012; Dataflow vs Random [0.5, 5.8] p=0.008
Table 5 — RepoBench-R: consistent strategy ranking
Table 10 — Fusion head: structural-only below random, combined slightly degrades vs embed-only
Table 14 — Conceptual comparison with inference-time methods (no empirical head-to-head)

**Ablations**: Temperature (Table 7), hop distance (Table 8), data scaling (Table 9), fusion head (Table 10), static vs dynamic mining (Table 11), binary vs weighted dataflow (Table 12), failure analysis (Table 13), stratified analysis (Table 6), qualitative case studies (8 cases, 4 patterns).

## Your Review Task

Evaluate the following dimensions with detailed justification:

### 1. Novelty Assessment
- How novel is each component? (embedding-distance mining, dataflow-aware mining, representation saturation analysis)
- Is the CoCoHaNeRe correction a genuine contribution or a minor clarification?
- Is "representation saturation mediates structural negative effectiveness" a new insight?
- How does this compare to existing work on hard negatives in NLP/IR (ANCE, curriculum learning)?
- Is the contribution primarily empirical (systematic study) or methodological (new technique)?

### 2. Related Work Completeness
- Are there important missing references? Consider:
  - Hard negative mining literature (DPR, SimCLR, MoCo negative strategies)
  - Code representation learning (CodeBERT, UniXcoder, CodeT5+)
  - Contrastive learning theory (understanding hard negatives, optimal difficulty)
  - Code graph analysis beyond the cited papers
- Is the CoCoHaNeRe critique fair and well-supported?
- Is the positioning vs inference-time methods adequate?

### 3. Significance and Impact
- Would this paper change how practitioners train code retrievers?
- Is the effect size (1.5-2.3pp R@1) meaningful for the community?
- Is the "representation saturation" finding actionable?

### 4. Clarity and Presentation
- Is the paper well-organized?
- Are claims well-calibrated to evidence?
- Any overclaiming or underclaiming?

### 5. Weaknesses
- All novelty and positioning weaknesses
- Missing comparisons or baselines from the literature

### 6. Questions for Authors

### 7. Score and Confidence

Output your review in structured format with all sections above. Be rigorous and specific.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "f515b183-9520-44a0-b2a3-123c609c97c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T08:24:51.204Z_

```json
{
  "parentUuid": "f515b183-9520-44a0-b2a3-123c609c97c3",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
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
  "uuid": "90be6689-7c2f-4a0d-91d6-4856c530d0bf",
  "timestamp": "2026-05-14T08:24:51.204Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T08:24:53.458Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90be6689-7c2f-4a0d-91d6-4856c530d0bf",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb298qHzsrELkX9kfM9RJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68e336c3-651e-400e-b6ea-a9db5532306c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNFuzxAdmSk739BPJRoReC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7142,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7142,
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

_source line 4 · 2026-05-14T08:24:54.360Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Hn66eZbvBpp6Der1NyMu3G`</summary>

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
  "parentUuid": "68e336c3-651e-400e-b6ea-a9db5532306c",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb298qHzsrELkX9kfM9RJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6515b220-e432-4b24-a354-693cd0ea197f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TNFuzxAdmSk739BPJRoReC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7142,
      "cache_read_input_tokens": 8249,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7142
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7142,
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

_source line 5 · 2026-05-14T08:24:54.363Z_

<details><summary>↩ Tool result · `toolu_01Hn66eZbvBpp6Der1NyMu3G`</summary>

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
  "parentUuid": "6515b220-e432-4b24-a354-693cd0ea197f",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "2cf79481-4d22-4c8e-b8db-55a2f5c2e354",
  "sourceToolAssistantUUID": "6515b220-e432-4b24-a354-693cd0ea197f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T08:24:57.133Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Se7E2pFxQYVTFRF4vntRSG`</summary>

```json
{
  "project": "structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cf79481-4d22-4c8e-b8db-55a2f5c2e354",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29951FjpwhMDaixzNSD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6ded79c-1cea-4921-8c72-0db2a2b516a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dem5rLSo9kzqByPpwnoDrX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 7 · 2026-05-14T08:24:57.269Z_

<details><summary>↩ Tool result · `toolu_01Se7E2pFxQYVTFRF4vntRSG`</summary>

```text
{"result":"# 项目 structfuse-context 概况\n\n## 实验状态 (31 个)\n\n- **p2b_eval_4runs_pool50**: DONE (success) — \n- **d007_50repo_overlap**: DONE (success) — \n- **p2b_5reruns**: DONE (success) — \n- **p2b_eval_4runs_v2**: DONE (success) — \n- **p2b-all-9runs**: DONE (killed) — \n- **p2b-smoke8**: DONE (killed) — \n- **p2b-smoke7**: DONE (killed) — \n- **p2b-smoke6**: DONE (killed) — \n- **p2b-smoke5**: DONE (killed) — \n- **p2b-smoke4**: DONE (killed) — \n- **p2b-smoke3**: DONE (killed) — \n- **p2b-smoke2**: DONE (killed) — \n- **p2b-smoke-test**: DONE (killed) — \n- **mvp_p2a_linear_proxy**: DONE (success) — \n- **mvp_p1_codeql_feasibility**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\n- **m1_extraction** (success): —\n\n## 趋势\n成功 10 / 负向 2 / 失败 2 / 共 28\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-42106: 无 GPU 信息\n\n## 告警\n- p2b-smoke-test: 已被终止 — unknown\n- p2b-smoke2: 已被终止 — unknown\n- p2b-smoke3: 已被终止 — unknown\n- p2b-smoke4: 已被终止 — unknown\n- p2b-smoke5: 已被终止 — unknown\n- p2b-smoke6: 已被终止 — unknown\n- p2b-smoke7: 已被终止 — unknown\n- p2b-smoke8: 已被终止 — unknown\n- p2b-all-9runs: 已被终止 — unknown\n- mvp_p2b_contrastive_training: 已被终止 — unknown\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\n- p2b_eval_all: 已被终止 — unknown\n- m2_early_pilot: 已被终止 — unknown\n- m2_early_pilot_v2: 训练失败 — unknown\n- m2_early_pilot_v3: 已被终止 — unknown\n- m1_reextract: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6ded79c-1cea-4921-8c72-0db2a2b516a6",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "874e098a-ce2d-43c0-a329-91abfe46cae6",
  "sourceToolAssistantUUID": "c6ded79c-1cea-4921-8c72-0db2a2b516a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T08:24:57.591Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LPqPx1ebtG6uLtm5967cNx`</summary>

```json
{
  "project": "structfuse-context",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "874e098a-ce2d-43c0-a329-91abfe46cae6",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29951FjpwhMDaixzNSD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef0b2db5-eeb1-45be-b1ce-bf0f3dcd992d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dem5rLSo9kzqByPpwnoDrX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15391,
      "output_tokens": 160,
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
          "output_tokens": 160,
          "cache_read_input_tokens": 15391,
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

_source line 9 · 2026-05-14T08:24:57.600Z_

<details><summary>↩ Tool result · `toolu_01LPqPx1ebtG6uLtm5967cNx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n- **m1_extraction** (success): —\\n\\n## 趋势\\n成功 10 / 负向 2 / 失败 2 / 共 28\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 1895, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef0b2db5-eeb1-45be-b1ce-bf0f3dcd992d",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "0102ef84-3f89-4594-81f4-822751e9ce70",
  "sourceToolAssistantUUID": "ef0b2db5-eeb1-45be-b1ce-bf0f3dcd992d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T08:25:01.241Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TVu2y9dw7jp39vYecCAUj5`</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0102ef84-3f89-4594-81f4-822751e9ce70",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb299KTuNWwvXrBDM2PP4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22dfe824-6493-44ce-879c-b2bca62835ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1YX5ehupeXPTZyVFqaYB5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 16838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2711,
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

_source line 11 · 2026-05-14T08:25:01.255Z_

<details><summary>↩ Tool result · `toolu_01TVu2y9dw7jp39vYecCAUj5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-12\\n# 说明: 只收录项目文件中已引用的 + 确定存在的知名论文。不确定的信息标注\\\"需验证\\\"。\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline  # StructFuse 的评估基准\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Karthik Narasimhan, Ofir Press\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: building-block  # StructFuse 用其 repo 做数据提取\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n        note: \\\"需验证 venue（可能已投稿会议）\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务，StructFuse 可用于评估。\\\"\\n        note: \\\"需验证年份和 venue\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及代码领域的对比学习\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式，是 StructFuse 对比训练的方法论基础。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，是 StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"SimCLR: A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Mining Hard Negatives with Curriculum for Dense Retrieval\\\"\\n        authors: \\\"需验证\\\"\\n        venue: \\\"需验证\\\"\\n        year: \\\"需验证\\\"\\n        relation: background\\n        summary: \\\"课程学习式 hard negative 挖掘，从易到难训练检索器。\\\"\\n        note: \\\"需验证完整信息\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block  # StructFuse 核心组件\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: EMNLP (Findings)\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: background\\n        summary: \\\"大规模开源代码 LLM，广泛用于代码嵌入的 backbone。\\\"\\n        note: \\\"需验证 venue（可能是 arXiv 或其他）\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Qwen Team (Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block  # StructFuse 用 Qwen2.5-Coder-3B 做检索器\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n        note: \\\"需验证确切标题和年份\\\"\\n\\n      - title: \\\"Contrastive Learning for Source Code with Structural and Functional Properties\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: ACL (Findings)\\n        year: 2022\\n        relation: background\\n        summary: \\\"代码对比学习中利用结构/功能属性构建正负样本对。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。Phase 2a 实验发现 BM25 在 bug fixing 定位中可能有误导性（负系数）。\\\"\\n\\n# ==========================================================================\\n# 待补充\\n# ==========================================================================\\n# 以下论文可能相关，待确认后补充：\\n# - FAISS (Johnson et al., 2019) — ANN 检索库，StructFuse 评估可能用到\\n# - Tree-sitter — 增量解析器，与 CodeQL 互补\\n# - Aider / Moatless Tools — SWE-bench 上的其他代码检索方法\\n# - CoSQA (Huang et al., 2021) — 代码搜索 QA 数据集\\n# - DeepSeek-Coder — 另一个可能的 backbone 对比\\n\", \"total_chars\": 9647, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22dfe824-6493-44ce-879c-b2bca62835ee",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "71948b94-3c96-44c6-a98e-16088f3d3555",
  "sourceToolAssistantUUID": "22dfe824-6493-44ce-879c-b2bca62835ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T08:25:01.706Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01M6fN3124vWZSeWRk91FafF`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71948b94-3c96-44c6-a98e-16088f3d3555",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb299KTuNWwvXrBDM2PP4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14ce9705-67e4-438c-8592-bb4e18cc019f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1YX5ehupeXPTZyVFqaYB5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 16838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2711,
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

_source line 13 · 2026-05-14T08:25:01.718Z_

<details><summary>↩ Tool result · `toolu_01M6fN3124vWZSeWRk91FafF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \\\"harm\\\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\\n\\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\\n\\n- **Headline result template**: \\\"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\\\"\\n- Backup: \\\"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\\n- m1_reextract_v2: expanded extraction for higher coverage\\n\\n### Planned (priority order):\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark\\n- plan_015: Dynamic mining baseline\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 9391, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14ce9705-67e4-438c-8592-bb4e18cc019f",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "bbcb9f0b-4f0e-4c7c-a64e-37ed3fa1a144",
  "sourceToolAssistantUUID": "14ce9705-67e4-438c-8592-bb4e18cc019f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T08:25:02.655Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0199rSkjRJ7F2KFVP6ixLf7v`</summary>

```json
{
  "project": "structfuse-context",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbcb9f0b-4f0e-4c7c-a64e-37ed3fa1a144",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb299KTuNWwvXrBDM2PP4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12c8b317-2d1a-4ef5-b736-aaa00bf7aed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1YX5ehupeXPTZyVFqaYB5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 16838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2711,
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

_source line 15 · 2026-05-14T08:25:02.665Z_

<details><summary>↩ Tool result · `toolu_0199rSkjRJ7F2KFVP6ixLf7v`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12c8b317-2d1a-4ef5-b736-aaa00bf7aed9",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "eda214ce-348d-44c4-9028-567afb1264df",
  "sourceToolAssistantUUID": "12c8b317-2d1a-4ef5-b736-aaa00bf7aed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T08:25:02.871Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012uRXUqvSHv7vxjARmTX4yY`</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda214ce-348d-44c4-9028-567afb1264df",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb299KTuNWwvXrBDM2PP4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c19b8153-dd72-4ffb-a4c4-c35890478891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1YX5ehupeXPTZyVFqaYB5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 16838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2711,
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

_source line 17 · 2026-05-14T08:25:02.886Z_

<details><summary>↩ Tool result · `toolu_012uRXUqvSHv7vxjARmTX4yY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); heavy inference cost |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | Repository-level Graph for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2025) | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (2025) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献\\n\\n- CodexGraph: arXiv:2408.03910, NAACL 2025\\n- LocAgent: arXiv:2503.09089, ACL 2025\\n- RANGER: arXiv:2509.25257, 2025\\n- RepoGraph: arXiv:2410.14684, ICLR 2025\\n- GraphCoder: arXiv:2406.07003, ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, 2025\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\", \"total_chars\": 8062, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c19b8153-dd72-4ffb-a4c4-c35890478891",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "fc63de3e-4b8a-414a-ba6a-beb6b5e015dc",
  "sourceToolAssistantUUID": "c19b8153-dd72-4ffb-a4c4-c35890478891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T08:25:06.630Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017exDF9gnv21WZ8qFthdHBi`</summary>

```json
{
  "project": "structfuse-context",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc63de3e-4b8a-414a-ba6a-beb6b5e015dc",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb299i6RxRswoiafD35gP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c3b0815-6f1d-4c92-bf6b-794952616929",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nP9oBBiuzhRYj3js8hfdB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9886,
      "cache_read_input_tokens": 19549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9886,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 19 · 2026-05-14T08:25:06.643Z_

<details><summary>↩ Tool result · `toolu_017exDF9gnv21WZ8qFthdHBi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\", \"content\": \"# StructFuse — Research Dashboard\\n\\n> 最后更新: 2026-05-14 01:47 UTC | 更新原因: Reviewer warnings 落地: m1_reextract_v2 定位明确 (camera-ready not current submission), plan_015/017 写作处理方案, experiment_plan 更新待排\\n\\n## 核心方向\\n\\\"Hard negative mining for code retrieval: what works, what doesn't, and why\\\" — 系统性分析 + 机制解释论文。详见 paper_framing.md（D024 重写后）。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **Framing 重写完成 (D024)**: 旧 Claim 2 (\\\"embedding harms\\\") 已证伪并移除；新叙事线：embedding universally helps → dataflow conditionally helps → mechanistic explanation via representation saturation\\n- **Full M2 训练中**: Qwen random_s42 running (best R@1=55.3% @step1000, overfitting @1500); StarCoder random_s42 running (R@1=45.4% @step1000, still improving)\\n- **M1 reextract v2 进行中**: 4 workers 并行 CodeQL 提取，~13% 进度\\n- **Plan_003 SWE-bench eval**: Pipeline ready (dry-run v2 PASS), 等 M2 checkpoint\\n- **Plan_014 temp ablation**: 脚本 D025 缩减完成 (6 runs, ~70h), 等 M2 释放 GPU\\n\\n## 近期任务\\n- [ ] 等 Qwen eval@2000 → 确认过拟合 → 剩余 8 seeds 减至 2 epochs (节省 ~48h/GPU)\\n- [ ] neg_difficulty 可视化 Figure（0 GPU-h，论文核心差异化图表）— 已派 Agent\\n- [ ] M2 full 18 runs 完成 → 统计检验 (bootstrap CI, paired t-test)\\n- [ ] M2 完成后: plan_014 temperature ablation (双卡 ~35h wall time)\\n- [ ] M2 Qwen best checkpoint → plan_003 SWE-bench Lite eval\\n- [ ] plan_004 RepoBench-R 第二 benchmark\\n- [ ] experiment_plan.yaml 更新: plan_002/013 关联 full M2 registry_id, plan_014 budget 修正\\n- [ ] 写作时: plan_015 (dynamic mining) → Limitation 段落; plan_017 (inference-time graph) → Discussion 段落 (0 GPU-h)\\n\\n## Go/No-Go 阈值 (D019/D020, 适配 D024 新 framing)\\n\\n**Claim 1 (embedding vs random)**: 预期 Go — pilot 已一致确认 (+1.6~2.0pp)。Full M2 提供 3-seed CI。\\n**Claim 2 (dataflow conditional benefit)**: 预期 Conditional Go — Qwen 正向、StarCoder 中性。Full M2 量化 interaction effect。\\n**n=3 功效限制**: df=2, Type II error 高。Discussion 必须讨论。\\n\\n## GPU 预算\\n- **bjb1-42106**: 2× RTX PRO 6000 96GB（专属）\\n  - cuda:0: m2_full_qwen (seed 1/9, step ~1550/4242)\\n  - cuda:1: m2_full_starcoder (seed 1/9, step ~1000/4242)\\n- **剩余**: ~140 GPU-h needed for plan_003/014/004/015 | 瓶颈是 M2 完成时间非总量\\n- **过拟合缩减**: 若 eval@2000 确认，2 epochs 节省 ~96h 总计，M2 约 May 18-19 完成（vs May 20-21）\\n\\n## m1_reextract_v2 定位\\n当前 M2 使用 15.9K structural data 训练。reextract_v2 完成后数据量预计 ~30K+，但 May 25 前无法重跑 M2（~200+ GPU-h）。**用途：camera-ready revision 或后续投稿的 scalability 证据**，不影响当前投稿关键路径。当前价值：Claim 3 (CodeQL scalability) 的 coverage 数字更新。\\n\\n## 关键风险\\n1. **ARR deadline May 25**: 关键路径 M2(~May 18) → plan_014(~May 19.5) → plan_003(~May 21) → 统计+初稿(~May 24)\\n2. **n=3 统计功效**: pilot <2pp 差异在 df=2 下极难显著\\n3. **plan_015 未做**: static vs dynamic mining confound 由 2/3 dream reviewers 提出，需 Limitation 段承认\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D027 | 2026-05-14 | M2 剩余 runs 加 early stopping (patience=2 evals)，加速关 | m2_full_qwen, m2_full_starcoder |\\n| D026 | 2026-05-14 | Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 ep | m2_full_qwen, m2_full_starcoder |\\n| D025 | 2026-05-14 | Plan_014 temperature ablation 缩减为 2 strategies × 3 | m2_full_qwen, plan_014 |\\n| D024 | 2026-05-14 | Major paper framing rewrite: drop falsified \\\"embed | m2_embed_verify, plan_013_starcoder, neg_difficulty_analysis |\\n| D023 | 2026-05-13 | Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重 | m1_reextract |\\n| D022 | 2026-05-13 | M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M | m1_extraction, plan_006_scalability |\\n| D021 | 2026-05-13 | Negative difficulty 分析揭示 encoder capacity 差异是 data | m2_embed_verify, plan_013_starcoder |\\n| D020 | 2026-05-13 | D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明 | m2_full_qwen, m2_full_starcoder |\\n| D019 | 2026-05-13 | D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案 | m2_full_qwen, m2_full_starcoder |\\n| D018 | 2026-05-13 | 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯 | m2_embed_verify, plan_013_starcoder |\\n\\n\", \"total_chars\": 3742, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c3b0815-6f1d-4c92-bf6b-794952616929",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "43c653ca-43a4-4212-a8e8-016df890795b",
  "sourceToolAssistantUUID": "1c3b0815-6f1d-4c92-bf6b-794952616929",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T08:25:07.107Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WK5fFSzYt2NVxLR2BYG8mT`</summary>

```json
{
  "project": "structfuse-context",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43c653ca-43a4-4212-a8e8-016df890795b",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb299i6RxRswoiafD35gP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5a0c33e-7681-46e5-8306-4ccaf2d9f4ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nP9oBBiuzhRYj3js8hfdB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9886,
      "cache_read_input_tokens": 19549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9886,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 21 · 2026-05-14T08:25:07.117Z_

<details><summary>↩ Tool result · `toolu_01WK5fFSzYt2NVxLR2BYG8mT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 28\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n\", \"total_chars\": 20054, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5a0c33e-7681-46e5-8306-4ccaf2d9f4ba",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "d47b93f2-19cf-426d-86f7-fddb81bc73e5",
  "sourceToolAssistantUUID": "a5a0c33e-7681-46e5-8306-4ccaf2d9f4ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T08:25:07.697Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011xA4NKJGEewsBS3yGPVGLP`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d47b93f2-19cf-426d-86f7-fddb81bc73e5",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb299i6RxRswoiafD35gP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3947daa0-3b39-4d14-99f1-b23058834846",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017nP9oBBiuzhRYj3js8hfdB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9886,
      "cache_read_input_tokens": 19549,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 19549,
          "cache_creation_input_tokens": 9886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9886,
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

_source line 23 · 2026-05-14T08:25:07.706Z_

<details><summary>↩ Tool result · `toolu_011xA4NKJGEewsBS3yGPVGLP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3947daa0-3b39-4d14-99f1-b23058834846",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "94f32ec4-9b9a-4ad1-a4d8-15af68b0e822",
  "sourceToolAssistantUUID": "3947daa0-3b39-4d14-99f1-b23058834846",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T08:25:11.678Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01S2vUSZhfwR5JXCsqmbTz4Y`</summary>

```json
{
  "project": "structfuse-context",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94f32ec4-9b9a-4ad1-a4d8-15af68b0e822",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29A4CQrwTp42jPdTbUV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b92bc9d1-d5df-43f8-85f2-0650e44c8e21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FphYEtMULYRLZYBqXHrX8B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13576,
      "cache_read_input_tokens": 29435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13576,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 25 · 2026-05-14T08:25:11.687Z_

<details><summary>↩ Tool result · `toolu_01S2vUSZhfwR5JXCsqmbTz4Y`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b92bc9d1-d5df-43f8-85f2-0650e44c8e21",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "7bb233c2-631e-4e4d-811d-2bf3dca22c2f",
  "sourceToolAssistantUUID": "b92bc9d1-d5df-43f8-85f2-0650e44c8e21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T08:25:12.155Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Md3BytUEmTofRhEbqkNdQm`</summary>

```json
{
  "project": "structfuse-context",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb233c2-631e-4e4d-811d-2bf3dca22c2f",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29A4CQrwTp42jPdTbUV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "012c0e13-41a8-430a-8d39-82fcbf3d29a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FphYEtMULYRLZYBqXHrX8B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13576,
      "cache_read_input_tokens": 29435,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13576
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 29435,
          "cache_creation_input_tokens": 13576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13576,
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

_source line 27 · 2026-05-14T08:25:12.165Z_

<details><summary>↩ Tool result · `toolu_01Md3BytUEmTofRhEbqkNdQm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "012c0e13-41a8-430a-8d39-82fcbf3d29a0",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "c3b53a75-20bd-4708-a26f-a286d2c6e358",
  "sourceToolAssistantUUID": "012c0e13-41a8-430a-8d39-82fcbf3d29a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-14T08:25:16.197Z_

Let me look at the artifacts directory for the actual paper draft and experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3b53a75-20bd-4708-a26f-a286d2c6e358",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29APNLP987629NFvdK1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ade55f4-8fce-4982-986f-f87a82e79367",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSkrBtxiNgzCHuQpXkjL8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 372,
      "cache_read_input_tokens": 43011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 372,
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

_source line 29 · 2026-05-14T08:25:17.668Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EBEcYDUiYio6xycdroTsPz`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ade55f4-8fce-4982-986f-f87a82e79367",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29APNLP987629NFvdK1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86065d0b-c3de-49ec-8f1c-8fb055db587d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSkrBtxiNgzCHuQpXkjL8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 372,
      "cache_read_input_tokens": 43011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 372,
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

_source line 30 · 2026-05-14T08:25:17.687Z_

<details><summary>↩ Tool result · `toolu_01EBEcYDUiYio6xycdroTsPz`</summary>

```text
artifacts/_project/intermediate/call_graph.ql
artifacts/code/extraction/codeql_queries/call_graph.ql
artifacts/_project/intermediate/hard_negative_mining.py
artifacts/code/training/hard_negative_mining.py
artifacts/_project/data/requirements.txt
artifacts/code/requirements.txt
artifacts/code/training/contrastive_model.py
artifacts/code/extraction/codeql_queries/bounded_dataflow.ql
artifacts/code/extraction/build_training_data.py
artifacts/_project/intermediate/contrastive_model.py
artifacts/_project/intermediate/bounded_dataflow.ql
artifacts/_project/intermediate/build_training_data.py
artifacts/code/training/__pycache__/contrastive_model.cpython-314.pyc
artifacts/code/extraction/__pycache__/build_training_data.cpython-314.pyc
artifacts/code/training/__pycache__/train.cpython-314.pyc
artifacts/mvp_p1_codeql_feasibility/report/mvp_phase1_report.md
artifacts/_project/report/phase2a_linear_proxy_results.txt
artifacts/code/training/train.py
artifacts/code/evaluation/eval_retrieval.py
artifacts/code/evaluation/eval_swebench.py
artifacts/_project/intermediate/train.py
artifacts/_project/data/eval_retrieval.py
artifacts/_project/data/eval_swebench.py
artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md
artifacts/code/extraction/extract_dataflow.py
artifacts/_project/intermediate/extract_dataflow.py
artifacts/_project/report/50repo_overlap_report.md
artifacts/dream_reports/dream_20260512T204322/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260512T204322/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260512T204322/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260512T204322/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260512T204322/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/best/experiment_data.json
artifacts/dream_reports/dream_20260512T204322/best/paper.tex
artifacts/dream_reports/dream_20260512T204322/best/paper.aux
artifacts/dream_reports/dream_20260512T204322/best/paper.out
artifacts/dream_reports/dream_20260512T204322/best/paper.pdf
artifacts/dream_reports/dream_20260512T204322/best/paper.log
artifacts/dream_reports/dream_20260512T204322/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json
artifacts/dream_reports/dream_20260512T204322/median/paper.tex
artifacts/dream_reports/dream_20260512T204322/median/paper.aux
artifacts/dream_reports/dream_20260512T204322/median/paper.out
artifacts/dream_reports/dream_20260512T204322/median/paper.pdf
artifacts/dream_reports/dream_20260512T204322/median/paper.log
artifacts/dream_reports/dream_20260512T204322/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260512T204322/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/worst/experiment_data.json
artifacts/dream_reports/dream_20260512T204322/worst/paper.tex
artifacts/dream_reports/dream_20260512T204322/worst/paper.aux
artifacts/dream_reports/dream_20260512T204322/worst/paper.out
artifacts/dream_reports/dream_20260512T204322/worst/paper.pdf
artifacts/dream_reports/dream_20260512T204322/worst/paper.log
artifacts/dream_reports/dream_20260512T204322/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260512T204322/logs/orchestrator.log
artifacts/dream_reports/dream_20260512T204322/best/review_report.md
artifacts/dream_reports/dream_20260512T204322/logs/review_best.log
artifacts/dream_reports/dream_20260512T204322/median/review_report.md
artifacts/dream_reports/dream_20260512T204322/logs/review_median.log
artifacts/dream_reports/dream_20260512T204322/worst/review_report.md
artifacts/dream_reports/dream_20260512T204322/logs/review_worst.log
artifacts/patch_build_m1.py
artifacts/patch_train.py
artifacts/disk_cleanup_report_20260513.md
artifacts/_project/data/plan_006_scalability_stats_29repos.json
artifacts/plan_006_scalability_stats_29repos.json
artifacts/_project/report/scalability_summary.md
artifacts/plan_006/scalability_summary.md
artifacts/_project/data/scalability_data.json
artifacts/plan_006/scalability_data.json
artifacts/m1_progress_0513.md
artifacts/bjb1_status_check.md
artifacts/_project/intermediate/cross_encoder_analysis.py
artifacts/analysis/cross_encoder_analysis.py
artifacts/_project/intermediate/run_full_m2_training.sh
artifacts/_project/intermediate/schedule_m2_runs.sh
artifacts/full_m2/run_full_m2_training.sh
artifacts/full_m2/build_full_m2_data.sh
artifacts/full_m2/schedule_m2_runs.sh
artifacts/_project/report/pilot_results_summary.md
artifacts/_project/report/pilot_results_summary_64aa24.md
artifacts/_project/data/pilot_results_920f68.json
artifacts/_project/data/pilot_results.json
artifacts/dream_reports/dream_20260512T204322/meta.yaml
artifacts/plan_006_scalability/data/full_z_percent_stats.json
artifacts/m2_full_qwen/intermediate/run_m2_full_qwen.sh
artifacts/plan_006_scalability/data/plan006_full_scalability.json
artifacts/plan006_error_patterns.json
artifacts/plan_006_scalability/data/plan006_error_patterns.json
artifacts/_project/chart/negative_difficulty_charts_index.txt
artifacts/_project/data/negative_difficulty_stats.txt
artifacts/_project/chart/negative_difficulty_margin_charts_index.txt
artifacts/_project/data/negative_difficulty_stats_v2.txt
artifacts/rename_safety_report.md
artifacts/plan003_swebench_eval_plan.md
artifacts/plan003_eval_readiness.md
artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260514T075732/logs/orchestrator.log
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86065d0b-c3de-49ec-8f1c-8fb055db587d",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "5f5f87b5-ff2c-4abb-b90d-4bf9cbe67be7",
  "sourceToolAssistantUUID": "86065d0b-c3de-49ec-8f1c-8fb055db587d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T08:25:18.216Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01N55H6qz2fPKAWy8Xawbtzx`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f5f87b5-ff2c-4abb-b90d-4bf9cbe67be7",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29APNLP987629NFvdK1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7c86baa-9922-4e16-8dd1-9c375cbf0af8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSkrBtxiNgzCHuQpXkjL8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 372,
      "cache_read_input_tokens": 43011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 372,
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

_source line 32 · 2026-05-14T08:25:18.236Z_

<details><summary>↩ Tool result · `toolu_01N55H6qz2fPKAWy8Xawbtzx`</summary>

```text
artifacts/dream_reports/dream_20260512T204322/best/paper.tex
artifacts/dream_reports/dream_20260512T204322/median/paper.tex
artifacts/dream_reports/dream_20260512T204322/worst/paper.tex
artifacts/dream_reports/dream_20260514T075732/best/paper.tex
artifacts/dream_reports/dream_20260514T075732/median/paper.tex
artifacts/dream_reports/dream_20260514T075732/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7c86baa-9922-4e16-8dd1-9c375cbf0af8",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "805edda0-1349-4012-89ba-590f34ce7736",
  "sourceToolAssistantUUID": "c7c86baa-9922-4e16-8dd1-9c375cbf0af8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T08:25:18.732Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017P7AfqtS43bLw3QVMhGjzg`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "805edda0-1349-4012-89ba-590f34ce7736",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29APNLP987629NFvdK1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc438836-7441-41b6-be49-267656f6d6a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSkrBtxiNgzCHuQpXkjL8g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 372,
      "cache_read_input_tokens": 43011,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 372
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 275,
          "cache_read_input_tokens": 43011,
          "cache_creation_input_tokens": 372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 372,
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

_source line 34 · 2026-05-14T08:25:18.747Z_

<details><summary>↩ Tool result · `toolu_017P7AfqtS43bLw3QVMhGjzg`</summary>

```text
artifacts/_project/intermediate/hard_negative_mining.py
artifacts/code/training/hard_negative_mining.py
artifacts/code/training/contrastive_model.py
artifacts/code/extraction/build_training_data.py
artifacts/_project/intermediate/contrastive_model.py
artifacts/_project/intermediate/build_training_data.py
artifacts/code/training/train.py
artifacts/code/evaluation/eval_retrieval.py
artifacts/code/evaluation/eval_swebench.py
artifacts/_project/intermediate/train.py
artifacts/_project/data/eval_retrieval.py
artifacts/_project/data/eval_swebench.py
artifacts/code/extraction/extract_dataflow.py
artifacts/_project/intermediate/extract_dataflow.py
artifacts/patch_build_m1.py
artifacts/patch_train.py
artifacts/_project/intermediate/cross_encoder_analysis.py
artifacts/analysis/cross_encoder_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc438836-7441-41b6-be49-267656f6d6a9",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "ca24959c-ac44-4e28-80a1-4135655bdd5b",
  "sourceToolAssistantUUID": "bc438836-7441-41b6-be49-267656f6d6a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T08:25:22.560Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gghs8FYaLg5LZ1jUFwS8ve`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca24959c-ac44-4e28-80a1-4135655bdd5b",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29AsGch9qjbQR47LUyP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30767a99-41e6-44fc-ab8e-abc0e3ae8be4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKhHp7capy7NprNZ1uwWY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2530,
      "cache_read_input_tokens": 43383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2530,
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

_source line 36 · 2026-05-14T08:25:22.566Z_

<details><summary>↩ Tool result · `toolu_01Gghs8FYaLg5LZ1jUFwS8ve`</summary>

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
11	\usepackage{hyperref}
12	\usepackage{url}
13	\usepackage{natbib}
14	
15	\newcommand{\ours}{\textsc{StructFuse}}
16	
17	\title{What Makes Hard Negatives Work for Code Retrieval?\\A Systematic Study of Mining Strategies and Representation Geometry}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	% ============================================================
25	\begin{abstract}
26	Hard negative mining is essential for training contrastive code retrievers, yet the field lacks systematic understanding of what negative selection strategies work and why. Prior work (CoCoHaNeRe) reports that embedding-distance negatives \emph{harm} code search---but this finding stems from BM25-proxy negatives mislabeled as embedding-distance. We present \ours{}, a controlled study of three mining strategies---random, true embedding-distance, and structure-grounded (dataflow)---evaluated across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 seeds each. Our results show: (1)~true embedding-distance mining \emph{consistently} improves retrieval over random baselines (+2.3pp R@1 on Qwen, +1.7pp on StarCoder; both $p < 0.01$), correcting the prior misconception; (2)~dataflow-aware negatives provide \emph{conditional} additional benefit mediated by representation saturation---significant on Qwen ($p = 0.018$) but not on StarCoder ($p = 0.62$), producing a clean encoder--strategy interaction; (3)~downstream SWE-bench Lite evaluation confirms that retrieval improvements transfer to resolve-rate gains (+2.3pp embedding, +3.3pp dataflow vs.\ random). Mechanistic analysis via negative-difficulty margins, temperature ablation, and dynamic-mining controls provides a complete explanatory account. Our inter-procedural dataflow extraction via CodeQL achieves 0\% timeout at 123-repo scale, offering a practical structural negative generator.
27	\end{abstract}
28	
29	% ============================================================
30	\section{Introduction}
31	
32	Repo-level code repair requires selecting relevant files from large codebases. Modern retrievers such as SweRank~\cite{swerank} and SWE-Fixer~\cite{swefixer} rely on text similarity, but lexical similarity does not equal structural relevance: a utility module may share many tokens with a core module yet be functionally unrelated, while a configuration file with low textual overlap may be the true dependency.
33	
34	Hard negative mining---selecting informative negative examples for contrastive training---is the standard approach to sharpen retrieval boundaries. Yet in the code domain, systematic understanding of \emph{what} mining strategies work and \emph{why} remains thin. CoCoHaNeRe~\cite{cocohanere} reports that embedding-distance negatives \emph{harm} code search by $-$27pp R@1, discouraging their use. We show this finding is an artifact: the negatives were selected by BM25, not true embedding distance. When genuine embedding-distance mining is applied, performance \emph{improves} consistently.
35	
36	Beyond correcting this misconception, we ask: can structural information about code---specifically, inter-procedural dataflow connectivity---provide an additional signal dimension for negative mining? Inference-time approaches (LocAgent, CodexGraph, RANGER) use code graphs at query time but inject no structural signal into training. We propose the opposite: mine negatives using a static dataflow graph at training time, with zero inference overhead.
37	
38	Our study yields three findings:
39	
40	\begin{enumerate}
41	\item \textbf{Embedding mining helps universally.} True embedding-distance negatives improve R@1 on both Qwen2.5-Coder-3B (+2.3pp, $p{=}0.003$) and StarCoder2-3B (+1.7pp, $p{=}0.008$), across 9 random seeds each.
42	
43	\item \textbf{Dataflow mining helps conditionally.} Structure-grounded negatives provide additional benefit only when encoder representations are saturated (Qwen: pos\_sim${}=0.986$, dataflow +1.5pp, $p{=}0.018$). On StarCoder (pos\_sim${}=0.799$), dataflow shows no significant effect ($p{=}0.62$), producing a clean interaction.
44	
45	\item \textbf{Mechanism: representation geometry.} Negative-difficulty margin analysis explains the interaction: in saturated spaces, random negatives are too easy; embedding mining raises difficulty, and dataflow mining adds an orthogonal structural dimension. In healthy spaces, embedding difficulty alone suffices.
46	\end{enumerate}
47	
48	SWE-bench Lite end-to-end evaluation with a Qwen3.6-27B agent confirms that retrieval improvements transfer downstream: +2.3pp (embedding) and +3.3pp (dataflow) resolve-rate over random, with bootstrap 95\% CIs excluding zero.
49	
50	% ============================================================
51	\section{Related Work}
52	
53	\paragraph{Code retrieval.} SweRank and SWE-Fixer train contrastive retrievers on SWE-bench-derived data but use only text-based negatives. RepoFusion incorporates cross-file context at the representation level but does not address negative selection. GraphCodeBERT uses dataflow edges as pretraining signal but not as a negative mining criterion.
54	
55	\paragraph{Hard negative mining.} In NLP, ANCE~\cite{ance} mines negatives from an asynchronous index; curriculum-based methods gradually increase difficulty. For code, CoCoHaNeRe evaluates multiple strategies but conflates BM25 with embedding distance, leading to the incorrect conclusion that embedding negatives harm performance. Our work provides a controlled comparison with true embedding-distance mining.
56	
57	\paragraph{Graph-guided code understanding.} LocAgent and CodexGraph navigate code graphs at inference time. ARISE uses intra-procedural dataflow for runtime tool calls. RANGER combines retrieval with graph reranking. All operate at inference; none inject structural signal into contrastive training. \ours{} is complementary: we mine negatives via static dataflow graphs at training time, with zero inference cost.
58	
59	% ============================================================
60	\section{Method}
61	
62	\subsection{Problem Setup}
63	
64	Given a repository $\mathcal{R}$ with files $\{f_1, \ldots, f_n\}$ and a query (issue description) $q$, the retriever must rank files by relevance. We train a bi-encoder with contrastive loss:
65	\begin{equation}
66	\mathcal{L} = -\log \frac{\exp(\text{sim}(q, f^+)/\tau)}{\exp(\text{sim}(q, f^+)/\tau) + \sum_{f^- \in \mathcal{N}} \exp(\text{sim}(q, f^-)/\tau)}
67	\end{equation}
68	where $f^+$ is the gold file, $\mathcal{N}$ is the negative set, and $\tau$ is the temperature. The key variable is how $\mathcal{N}$ is constructed.
69	
70	\subsection{Negative Mining Strategies}
71	
72	We compare three strategies, all applied at training time:
73	
74	\paragraph{Random.} Sample $k$ negatives uniformly from non-gold files in the repository. This is the standard baseline.
75	
76	\paragraph{Embedding-distance.} Encode all files with the pretrained encoder, then select the $k$ non-gold files most similar to $f^+$ by cosine distance. These are ``near-miss'' negatives that force the encoder to make fine-grained distinctions.
77	
78	\paragraph{Dataflow-aware.} Construct an inter-procedural dataflow graph $G$ over $\mathcal{R}$ using CodeQL. Define a file pair $(f_i, f_j)$ as \emph{connected} if there exists a call-graph path of $\leq 2$ hops between any function in $f_i$ and any function in $f_j$. A \textbf{structure-grounded hard negative} is a file that is (a)~textually similar to $f^+$ (high embedding cosine), (b)~\emph{not} the gold file, and (c)~\emph{not} connected to $f^+$ in $G$. Formally:
79	\begin{equation}
80	f^-_{\text{struct}} = \arg\max_{x \in \mathcal{R} : x \neq f^+ \wedge \neg \text{reach}_G(x, f^+)} \text{sim}(x, f^+)
81	\end{equation}
82	
83	The dataflow graph is extracted once and remains static throughout training---it does not update with the encoder, making the structural signal drift-immune.
84	
85	\subsection{CodeQL Extraction Pipeline}
86	
87	We use CodeQL to extract inter-procedural call graphs from Python repositories. Each repository is compiled into a CodeQL database, and we query for function-level call edges. Connected components are computed at $k$-hop granularity. At our evaluation scale of 131 SWE-smith repositories, the pipeline achieves 0\% query timeout, with 123/131 repos producing valid output and 78\% connected-not-gold rate ($Z\%$) at 2-hop.
88	
89	\subsection{Encoders and Training}
90	
91	We evaluate on two architecturally distinct 3B-parameter code encoders:
92	\begin{itemize}
93	\item \textbf{Qwen2.5-Coder-3B}: Decoder-only, pretrained representations show high positive-pair similarity (pos\_sim $= 0.986$), indicating a saturated representation space.
94	\item \textbf{StarCoder2-3B}: Encoder-decoder, with healthy separation (pos\_sim $= 0.799$).
95	\end{itemize}
96	
97	Both are fine-tuned with LoRA (rank 16) for 3 epochs on 5K training instances from SWE-smith, with early stopping on validation R@1. Each strategy$\times$encoder combination is run with 9 random seeds.
98	
99	% ============================================================
100	\section{Experiments}
101	
102	\subsection{Main Results: 9-Seed Cross-Encoder Comparison}
103	\label{sec:main}
104	
105	Table~\ref{tab:qwen_main} and Table~\ref{tab:starcoder_main} present the primary results.
106	
107	\begin{table}[t]
108	\centering
109	\small
110	\caption{Qwen2.5-Coder-3B: 9-seed R@1 summary on SWE-smith.}
111	\label{tab:qwen_main}
112	\begin{tabular}{lccc}
113	\toprule
114	\textbf{Strategy} & \textbf{Mean R@1} & \textbf{Std} & \textbf{95\% CI} \\
115	\midrule
116	Random & 0.533 & 0.008 & [0.527, 0.539] \\
117	Embedding & 0.556 & 0.009 & [0.549, 0.563] \\
118	Dataflow & 0.548 & 0.010 & [0.540, 0.556] \\
119	\midrule
120	\multicolumn{4}{l}{\small Embed vs Random: $\Delta{=}$+2.3pp, $p{=}0.003$} \\
121	\multicolumn{4}{l}{\small Dataflow vs Random: $\Delta{=}$+1.5pp, $p{=}0.018$} \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	\begin{table}[t]
127	\centering
128	\small
129	\caption{StarCoder2-3B: 9-seed R@1 summary on SWE-smith.}
130	\label{tab:starcoder_main}
131	\begin{tabular}{lccc}
132	\toprule
133	\textbf{Strategy} & \textbf{Mean R@1} & \textbf{Std} & \textbf{$p$ vs Random} \\
134	\midrule
135	Random & 0.490 & 0.009 & --- \\
136	Embedding & 0.507 & 0.010 & 0.008 \\
137	Dataflow & 0.488 & 0.011 & 0.620 \\
138	\bottomrule
139	\end{tabular}
140	\end{table}
141	
142	\textbf{Embedding mining helps both encoders.} On Qwen, embedding-distance negatives improve R@1 by +2.3pp ($p{=}0.003$). On StarCoder, the gain is +1.7pp ($p{=}0.008$). Both are significant at $\alpha{=}0.01$, confirming that true embedding-distance mining is universally beneficial---contradicting prior reports of harm.
143	
144	\textbf{Dataflow benefit is conditional on saturation.} On Qwen, dataflow adds +1.5pp over random ($p{=}0.018$), but on StarCoder, the effect is null ($\Delta{=}{-}0.2$pp, $p{=}0.62$). This encoder--strategy interaction is the paper's central mechanistic finding: structural negatives provide benefit only when the representation space is saturated and embedding-based difficulty alone is insufficient.
145	
146	\subsection{SWE-bench Lite End-to-End Evaluation}
147	
148	To verify that retrieval improvements transfer to downstream task performance, we evaluate on SWE-bench Lite (300 instances) using a Qwen3.6-27B agent with each strategy's best checkpoint as the retriever.
149	
150	\begin{table}[t]
151	\centering
152	\small
153	\caption{SWE-bench Lite resolve rate by retrieval strategy.}
154	\label{tab:swebench}
155	\begin{tabular}{lccc}
156	\toprule
157	\textbf{Strategy} & \textbf{Resolve Rate} & \textbf{$\Delta$ vs Random} & \textbf{Resolved} \\
158	\midrule
159	Random & 22.7\% & --- & 68 \\
160	Embedding & 25.0\% & +2.3pp & 75 \\
161	Dataflow & 26.0\% & +3.3pp & 78 \\
162	\bottomrule
163	\end{tabular}
164	\end{table}
165	
166	Bootstrap 95\% CIs (10,000 iterations, Table~\ref{tab:bootstrap}) confirm statistical significance for both mining strategies vs.\ random.
167	
168	\begin{table}[t]
169	\centering
170	\small
171	\caption{Bootstrap 95\% CI for SWE-bench Lite resolve rate deltas.}
172	\label{tab:bootstrap}
173	\begin{tabular}{lccc}
174	\toprule
175	\textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$} \\
176	\midrule
177	Embed vs Random & +2.3 & [0.4, 4.2] & 0.012 \\
178	Dataflow vs Random & +3.3 & [0.5, 5.8] & 0.008 \\
179	Dataflow vs Embed & +1.0 & [$-$0.8, 2.8] & 0.134 \\
180	\bottomrule
181	\end{tabular}
182	\end{table}
183	
184	The dataflow-vs-embed comparison is not significant (CI includes zero), consistent with the ``conditional benefit'' framing: dataflow's advantage over embedding is modest and requires larger evaluation sets to detect reliably.
185	
186	\subsection{RepoBench-R Cross-File Retrieval}
187	
188	To assess external validity, we evaluate on RepoBench-R, a cross-file retrieval benchmark with 1,200 queries independent of our training distribution.
189	
190	\begin{table}[t]
191	\centering
192	\small
193	\caption{RepoBench-R retrieval performance.}
194	\label{tab:repobench}
195	\begin{tabular}{lcccc}
196	\toprule
197	\textbf{Strategy} & \textbf{R@1} & \textbf{R@5} & \textbf{R@10} & \textbf{MRR} \\
198	\midrule
199	Random & 0.412 & 0.687 & 0.793 & 0.508 \\
200	Embedding & 0.431 & 0.704 & 0.808 & 0.529 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30767a99-41e6-44fc-ab8e-abc0e3ae8be4",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "3c462d63-a943-41a5-a642-b4182ee484c5",
  "sourceToolAssistantUUID": "30767a99-41e6-44fc-ab8e-abc0e3ae8be4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T08:25:23.287Z_

<details open><summary>🔧 Tool call — Read · `toolu_013tfjv85bhNsZ3WgrcAbtxs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c462d63-a943-41a5-a642-b4182ee484c5",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29AsGch9qjbQR47LUyP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3489ef30-5dc3-418d-a5f3-d968571d056a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKhHp7capy7NprNZ1uwWY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2530,
      "cache_read_input_tokens": 43383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2530,
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

_source line 38 · 2026-05-14T08:25:23.293Z_

<details><summary>↩ Tool result · `toolu_013tfjv85bhNsZ3WgrcAbtxs`</summary>

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
10	\usepackage{xcolor}
11	\usepackage{hyperref}
12	\usepackage[T1]{fontenc}
13	\usepackage[utf8]{inputenc}
14	
15	\title{What Makes Hard Negatives Work for Code Retrieval?\\A Systematic Study of Mining Strategies and Representation Geometry}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\begin{abstract}
23	Hard negative mining is widely used in contrastive learning for code retrieval, yet little is known about \emph{which} mining strategies work, \emph{when}, and \emph{why}. Prior work has reported that embedding-distance negatives harm code search, but we show this conclusion stems from conflating BM25-proxy negatives with true embedding-distance mining. We present a controlled comparison of three negative selection strategies---random, embedding-distance, and structure-grounded (inter-procedural dataflow)---across two architecturally distinct code encoders (Qwen2.5-Coder-3B, StarCoder2-3B). Our results provide directional evidence that true embedding-distance mining tends to improve retrieval over random baselines (+0.5--1.3pp R@1 on RepoBench-R), with the benefit modulated by encoder representation geometry: saturated encoders (high positive-pair similarity) show larger gains. Dataflow-grounded negatives yield inconsistent effects across encoders and benchmarks, suggesting that static structural signal is a fragile training signal. We contribute (1)~a controlled comparison framework isolating mining strategy effects, (2)~a representation geometry analysis explaining encoder-strategy interactions, and (3)~a scalable CodeQL-based structural negative extraction pipeline covering 123 repositories. End-to-end evaluation on SWE-bench Lite shows no statistically distinguishable differences between strategies ($p > 0.3$), indicating that retrieval-level gains do not yet translate to downstream task improvements. We release our framework to support future investigation of hard negative mining for code.
24	\end{abstract}
25	
26	%------------------------------------------------------------
27	\section{Introduction}
28	\label{sec:intro}
29	%------------------------------------------------------------
30	
31	Repo-level code repair and bug localization require selecting relevant files from large codebases. Modern approaches train contrastive retrievers that embed code and queries into a shared space, using hard negative mining to improve discrimination~\cite{karpukhin2020dense,xiong2020approximate}. Despite the importance of negative selection, the field lacks systematic understanding of what strategies work for code retrieval and why.
32	
33	Recent work has produced contradictory findings. CoCoHaNeRe-style analyses report that embedding-distance negatives \emph{harm} code search performance. However, we identify that these evaluations used BM25-based proxy negatives mislabeled as embedding-distance---a methodological confound that reverses the conclusion when corrected.
34	
35	Meanwhile, structural information (call graphs, dataflow) has been exploited at \emph{inference} time by systems such as CodexGraph, LocAgent, and RANGER, but no prior work systematically studies whether structural signals improve \emph{training}-time negative mining.
36	
37	We address this gap with a controlled study comparing three strategies: (1)~\textbf{random} negatives as baseline, (2)~\textbf{embedding-distance} negatives mined from pretrained representations, and (3)~\textbf{dataflow-aware} negatives selected using inter-procedural dataflow connectivity extracted via CodeQL. We train each configuration across two encoders with distinct representation geometries: Qwen2.5-Coder-3B (saturated, $\text{pos\_sim} \approx 0.99$) and StarCoder2-3B (healthy, $\text{pos\_sim} \approx 0.80$).
38	
39	Our analysis yields three findings. First, true embedding-distance mining tends to improve retrieval over random baselines, providing directional evidence that corrects prior reports of harm (\S\ref{sec:main_results}). Second, dataflow-grounded negatives show inconsistent effects---directionally positive for Qwen but neutral-to-negative for StarCoder---an exploratory observation we link to representation saturation (\S\ref{sec:analysis}). Third, we provide a methodological contribution: a controlled comparison framework and scalable CodeQL extraction pipeline that enables reproducible study of structural negative mining (\S\ref{sec:method}).
40	
41	We evaluate across two benchmarks (SWE-smith validation, RepoBench-R) and downstream on SWE-bench Lite. Downstream evaluation shows no statistically significant difference between strategies, an important negative finding we analyze through failure decomposition (\S\ref{sec:swebench}).
42	
43	%------------------------------------------------------------
44	\section{Related Work}
45	\label{sec:related}
46	%------------------------------------------------------------
47	
48	\paragraph{Hard Negative Mining for Dense Retrieval.}
49	ANCE~\cite{xiong2020approximate} introduced asynchronous negative mining from an evolving index; DPR~\cite{karpukhin2020dense} demonstrated in-batch negatives for open-domain QA. Curriculum-based mining schedules negatives by increasing difficulty. For code, CoCoHaNeRe evaluated multiple mining strategies but used BM25 scores as a proxy for embedding distance, conflating two distinct signals. We provide the first controlled comparison using \emph{true} embedding-distance negatives for code retrieval.
50	
51	\paragraph{Structure-Aware Code Retrieval.}
52	GraphCodeBERT~\cite{guo2021graphcodebert} incorporates dataflow into pretraining objectives. RepoFusion and GRACE leverage repository-level context at inference time. CodexGraph and LocAgent build structural graphs dynamically during inference for multi-hop navigation. ARISE uses intra-procedural dataflow for runtime tool calls. Our work differs by using \emph{inter-procedural} dataflow as a \emph{training}-time signal for negative selection, complementary to inference-time approaches.
53	
54	\paragraph{Contrastive Learning for Code.}
55	SweRank and SWE-Fixer train contrastive retrievers for code repair using text similarity alone. We extend this paradigm by studying whether and when structure-grounded negatives provide benefit beyond text-based mining.
56	
57	%------------------------------------------------------------
58	\section{Method}
59	\label{sec:method}
60	%------------------------------------------------------------
61	
62	\subsection{Problem Setting}
63	
64	Given a query $q$ (e.g., a bug report) and a repository with files $\mathcal{F} = \{f_1, \ldots, f_N\}$, the retriever scores each file by similarity $s(q, f_i)$ and returns a ranked list. We train the retriever with contrastive loss using InfoNCE:
65	\begin{equation}
66	\mathcal{L} = -\log \frac{\exp(s(q, f^+)/\tau)}{\exp(s(q, f^+)/\tau) + \sum_{j=1}^{K} \exp(s(q, f_j^-)/\tau)}
67	\end{equation}
68	where $f^+$ is the gold file, $\{f_j^-\}_{j=1}^K$ are negatives, and $\tau$ is the temperature.
69	
70	The key design choice is how to select $\{f_j^-\}$. We compare three strategies that differ only in negative selection, holding all other training details constant.
71	
72	\subsection{Negative Mining Strategies}
73	
74	\paragraph{Random.} Negatives are sampled uniformly from non-gold files in the same repository. This is the standard baseline.
75	
76	\paragraph{Embedding-Distance.} Using the pretrained encoder, we compute embeddings for all files and select the $K$ non-gold files closest to the query in embedding space:
77	\begin{equation}
78	f_j^- = \underset{f \in \mathcal{F} \setminus \{f^+\}}{\arg\text{top-}K}\ s_{\text{pretrained}}(q, f)
79	\end{equation}
80	Mining is performed once from the pretrained model (static mining). We verify that dynamic re-mining per epoch does not significantly change results (\S\ref{sec:dynamic}).
81	
82	\paragraph{Dataflow-Aware.} We extract inter-procedural dataflow graphs using CodeQL, computing 2-hop reachability from each gold file. Negatives are drawn from files that are \emph{not} reachable via dataflow from the gold file but have high embedding similarity:
83	\begin{equation}
84	f_j^- = \underset{f \in \mathcal{F} : s(q,f) > \theta \wedge \neg\text{reach}_G(f^+, f)}{\arg\text{top-}K}\ s_{\text{pretrained}}(q, f)
85	\end{equation}
86	This selects files that are textually similar but structurally disconnected---hard negatives along a structural dimension.
87	
88	\subsection{CodeQL Structural Extraction}
89	\label{sec:codeql}
90	
91	We use CodeQL's inter-procedural dataflow analysis to extract file-level connectivity. For each repository, we build a CodeQL database and query for data-flow paths crossing file boundaries, bounded at 2 hops in the call graph. The extraction pipeline processes 123 out of 131 SWE-smith repositories with zero timeouts and 78\% connected-not-gold rate, confirming scalability. The resulting graph $G$ is static and model-independent.
92	
93	\subsection{Fusion Head}
94	
95	We additionally experiment with a fusion scoring head that combines embedding similarity with binary structural features (dataflow connectivity, shared imports, directory co-location). Results (\S\ref{sec:fusion}) show marginal additive benefit, suggesting the primary value lies in negative \emph{selection} rather than feature fusion at scoring time.
96	
97	\subsection{Encoders and Training}
98	
99	We use two architecturally distinct encoders:
100	\begin{itemize}
101	\item \textbf{Qwen2.5-Coder-3B}: Decoder-based, exhibits representation saturation ($\text{pos\_sim} = 0.9855$).
102	\item \textbf{StarCoder2-3B}: Encoder-decoder, exhibits healthy representation space ($\text{pos\_sim} = 0.7985$).
103	\end{itemize}
104	Both are fine-tuned with LoRA (rank 16) for 3 epochs on SWE-smith training data. Temperature is set to $\tau = 0.1$ unless otherwise noted. Each configuration uses a pool of 50 candidate files per query.
105	
106	%------------------------------------------------------------
107	\section{Experiments: Main Results}
108	\label{sec:main_results}
109	%------------------------------------------------------------
110	
111	\subsection{RepoBench-R Cross-File Retrieval}
112	\label{sec:repobench}
113	
114	We evaluate retrieval quality on RepoBench-R, a cross-file retrieval benchmark independent of our training distribution. Table~\ref{tab:repobench} reports R@1 for each encoder-strategy combination.
115	
116	\begin{table}[t]
117	\centering
118	\small
119	\begin{tabular}{lccccc}
120	\toprule
121	\textbf{Encoder} & \textbf{Random} & \textbf{Embed} & \textbf{Dataflow} & \textbf{Embed $\Delta$} & \textbf{Dataflow $\Delta$} \\
122	\midrule
123	Qwen2.5-Coder-3B & 0.312 & 0.325 & 0.318 & +1.3pp & +0.6pp \\
124	StarCoder2-3B & 0.274 & 0.279 & 0.268 & +0.5pp & $-$0.6pp \\
125	\bottomrule
126	\end{tabular}
127	\caption{RepoBench-R R@1 by encoder and mining strategy. Embedding-distance mining shows directionally consistent improvement over random for both encoders. Dataflow is directionally positive for Qwen but slightly negative for StarCoder.}
128	\label{tab:repobench}
129	\end{table}
130	
131	Embedding-distance mining tends to improve R@1 over random for both encoders (+1.3pp for Qwen, +0.5pp for StarCoder), though the 95\% confidence interval for StarCoder includes zero. The direction is consistent with SWE-smith validation results but with attenuated magnitude, expected given the domain shift between SWE-smith training data and RepoBench's next-line completion context.
132	
133	Dataflow-aware negatives show inconsistent results: +0.6pp for Qwen but $-$0.6pp for StarCoder. This cross-encoder divergence recurs throughout our experiments and motivates the representation geometry analysis in \S\ref{sec:analysis}.
134	
135	\subsection{SWE-bench Lite End-to-End Evaluation}
136	\label{sec:swebench}
137	
138	We evaluate downstream impact using a Qwen3.6-27B agent on 300 SWE-bench Lite instances (287 evaluated, 13 agent errors). Table~\ref{tab:swebench} reports resolve rates and retrieval recall.
139	
140	\begin{table}[t]
141	\centering
142	\small
143	\begin{tabular}{lccc}
144	\toprule
145	\textbf{Strategy} & \textbf{Resolve (\%)} & \textbf{$\Delta$ vs Random (pp)} & \textbf{R@5} \\
146	\midrule
147	Random & 18.3 & --- & 0.41 \\
148	Embedding & 18.7 & +0.4 & 0.43 \\
149	Dataflow & 18.0 & $-$0.3 & 0.42 \\
150	\bottomrule
151	\end{tabular}
152	\caption{SWE-bench Lite resolve rates. No strategy achieves statistically significant improvement over random.}
153	\label{tab:swebench}
154	\end{table}
155	
156	No strategy achieves statistically significant improvement. Bootstrap confidence intervals (Table~\ref{tab:bootstrap}, 10{,}000 resamples) confirm that both comparisons include zero: embedding vs.\ random $\Delta = +0.4$pp, 95\% CI [$-$1.8, +2.6], $p = 0.34$; dataflow vs.\ random $\Delta = -0.3$pp, 95\% CI [$-$2.5, +1.9], $p = 0.41$.
157	
158	\begin{table}[t]
159	\centering
160	\small
161	\begin{tabular}{lccc}
162	\toprule
163	\textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$} \\
164	\midrule
165	Embed vs.\ Random & +0.4 & [$-$1.8, +2.6] & 0.34 \\
166	Dataflow vs.\ Random & $-$0.3 & [$-$2.5, +1.9] & 0.41 \\
167	\bottomrule
168	\end{tabular}
169	\caption{Bootstrap confidence intervals for SWE-bench Lite resolve rate differences ($n = 10{,}000$ resamples).}
170	\label{tab:bootstrap}
171	\end{table}
172	
173	This null downstream result is not unexpected. Retrieval improvements of $\sim$1pp R@1 are diluted by the generation bottleneck in the end-to-end agent pipeline. We analyze this via failure decomposition in \S\ref{sec:failure}.
174	
175	\subsection{Failure Analysis}
176	\label{sec:failure}
177	
178	To understand why retrieval-level gains do not translate downstream, we manually analyze 50 SWE-bench failure cases (Table~\ref{tab:failure_cats}).
179	
180	\begin{table}[t]
181	\centering
182	\small
183	\begin{tabular}{lcc}
184	\toprule
185	\textbf{Category} & \textbf{Count} & \textbf{\%} \\
186	\midrule
187	Generation failure & 22 & 44 \\
188	Retrieval miss & 18 & 36 \\
189	Multi-file needed & 6 & 12 \\
190	Flaky test & 4 & 8 \\
191	\bottomrule
192	\end{tabular}
193	\caption{Failure category distribution in 50 analyzed SWE-bench failures.}
194	\label{tab:failure_cats}
195	\end{table}
196	
197	Generation failures dominate (44\%), confirming that the agent's patch generation---not file retrieval---is the primary bottleneck. Among the 18 retrieval misses, dataflow-aware negatives help in only 5 cases (27.8\%), are neutral in 10 (55.6\%), and hurt in 3 (16.7\%), as shown in Table~\ref{tab:dataflow_impact}.
198	
199	\begin{table}[t]
200	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3489ef30-5dc3-418d-a5f3-d968571d056a",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "b333174b-c5a9-4d1b-b977-8ad76b58a99f",
  "sourceToolAssistantUUID": "3489ef30-5dc3-418d-a5f3-d968571d056a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-14T08:25:26.512Z_

Let me continue reading the best paper and also the median one more.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b333174b-c5a9-4d1b-b977-8ad76b58a99f",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29BDt6scj99PtFLCPHF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3999e8d-5155-45b5-8223-c3475d324893",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dzsBBSDmFfNtDRt39QC3A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9406,
      "cache_read_input_tokens": 45913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9406,
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

_source line 40 · 2026-05-14T08:25:28.878Z_

<details open><summary>🔧 Tool call — Read · `toolu_019sASPSsqMG6LSSb1BgJCvP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
  "offset": 200,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3999e8d-5155-45b5-8223-c3475d324893",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29BDt6scj99PtFLCPHF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a37b48f-ab1f-4fc1-8e9f-c54b1ebb4a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dzsBBSDmFfNtDRt39QC3A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9406,
      "cache_read_input_tokens": 45913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9406,
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

_source line 41 · 2026-05-14T08:25:28.883Z_

<details><summary>↩ Tool result · `toolu_019sASPSsqMG6LSSb1BgJCvP`</summary>

```text
200	Embedding & 0.431 & 0.704 & 0.808 & 0.529 \\
201	Dataflow & 0.438 & 0.711 & 0.812 & 0.534 \\
202	\bottomrule
203	\end{tabular}
204	\end{table}
205	
206	Strategy ranking is consistent with SWE-smith (dataflow $\geq$ embedding $>$ random), confirming that our findings are not benchmark-specific. Absolute R@1 is lower than SWE-smith (0.41 vs.\ 0.53) due to domain gap, but the relative improvements transfer.
207	
208	\subsection{Embedding Mining Stratified Analysis}
209	
210	We stratify embedding mining benefit by repository size and code complexity to characterize when it is most effective.
211	
212	\begin{table}[t]
213	\centering
214	\small
215	\caption{Embedding mining R@1 delta by repository tier.}
216	\label{tab:stratified}
217	\begin{tabular}{lcccc}
218	\toprule
219	\textbf{Tier} & \textbf{$N$} & \textbf{Embed R@1} & \textbf{Random R@1} & \textbf{$\Delta$} \\
220	\midrule
221	Small ($<$50 files) & 500 & 0.568 & 0.560 & +0.8pp \\
222	Medium (50--200) & 4,096 & 0.551 & 0.530 & +2.1pp \\
223	Large (200--500) & 13,628 & 0.542 & 0.514 & +2.8pp \\
224	XLarge (500+) & 25,949 & 0.528 & 0.513 & +1.5pp \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	Benefit peaks for large repositories (200--500 files, +2.8pp) where the candidate pool contains sufficient near-miss negatives. Small repos lack enough candidates for embedding mining to differentiate from random; extra-large repos introduce noise as embedding distance decorrelates from relevance. Code complexity (cyclomatic complexity, import depth) is a stronger predictor of embedding mining benefit than raw size ($r{=}0.42$ vs.\ $r{=}0.31$).
230	
231	\subsection{Temperature Ablation}
232	\label{sec:temp}
233	
234	We ablate the contrastive temperature $\tau \in \{0.05, 0.1, 0.2\}$ to test robustness and probe mechanistic interactions.
235	
236	\begin{table}[t]
237	\centering
238	\small
239	\caption{Temperature $\times$ strategy interaction on Qwen.}
240	\label{tab:temperature}
241	\begin{tabular}{lccccc}
242	\toprule
243	\textbf{$\tau$} & \textbf{Rand R@1} & \textbf{Emb R@1} & \textbf{Emb $\Delta$} & \textbf{DF R@1} & \textbf{DF $\Delta$} \\
244	\midrule
245	0.05 & 0.518 & 0.542 & +2.4 & 0.539 & +2.1 \\
246	0.10 & 0.533 & 0.556 & +2.3 & 0.548 & +1.5 \\
247	0.20 & 0.521 & 0.539 & +1.8 & 0.530 & +0.9 \\
248	\bottomrule
249	\end{tabular}
250	\end{table}
251	
252	Embedding benefit is robust across temperatures (+1.8--2.4pp). Dataflow benefit is strongest at low $\tau$ (+2.1pp at $\tau{=}0.05$) and diminishes at high $\tau$ (+0.9pp at $\tau{=}0.2$). This is mechanistically consistent: $\tau$ controls sensitivity to negative difficulty, and high $\tau$ flattens the difficulty gradient, reducing the marginal value of structural hardness.
253	
254	\subsection{Hop Distance Ablation}
255	
256	We ablate the call-graph hop distance used for dataflow extraction.
257	
258	\begin{table}[t]
259	\centering
260	\small
261	\caption{Hop distance impact on extraction and Qwen R@1.}
262	\label{tab:hop}
263	\begin{tabular}{lcccc}
264	\toprule
265	\textbf{Hops} & \textbf{Connected \%} & \textbf{$Z\%$} & \textbf{Time (s)} & \textbf{R@1} \\
266	\midrule
267	1 & 12\% & 18\% & 4.2 & 0.541 \\
268	2 & 34\% & 41\% & 8.9 & 0.548 \\
269	3 & 58\% & 62\% & 23.4 & 0.544 \\
270	\bottomrule
271	\end{tabular}
272	\end{table}
273	
274	2-hop is optimal. 1-hop is too restrictive (only 12\% connected rate, negative pool too small). 3-hop over-expands connectivity (58\%), diluting structural signal and incurring 2.6$\times$ extraction cost. The 2-hop sweet spot balances coverage (34\%) with selectivity ($Z{=}41\%$).
275	
276	\subsection{Training Data Scaling}
277	
278	We vary training set size (1K, 3K, 5K instances) to test whether strategy benefits are scale-dependent.
279	
280	\begin{table}[t]
281	\centering
282	\small
283	\caption{Strategy benefit by training data size (Qwen).}
284	\label{tab:scaling}
285	\begin{tabular}{lcccc}
286	\toprule
287	\textbf{Size} & \textbf{Rand R@1} & \textbf{Emb R@1} & \textbf{Emb $\Delta$} & \textbf{DF $\Delta$} \\
288	\midrule
289	1K & 0.498 & 0.521 & +2.3 & +2.0 \\
290	3K & 0.525 & 0.548 & +2.3 & +1.8 \\
291	5K & 0.533 & 0.556 & +2.3 & +1.5 \\
292	\bottomrule
293	\end{tabular}
294	\end{table}
295	
296	Embedding mining benefit is remarkably scale-invariant (+2.3pp at all sizes), confirming that the information gain is intrinsic to the selection criterion, not data quantity. Dataflow benefit decreases slightly with scale (from +2.0 to +1.5pp) as larger random samples implicitly cover some structural hard negatives, but remains positive throughout.
297	
298	\subsection{Fusion Head Ablation}
299	
300	To distinguish training-time mining from inference-time feature injection, we compare three retrieval heads.
301	
302	\begin{table}[t]
303	\centering
304	\small
305	\caption{Fusion head comparison (Qwen, best checkpoint).}
306	\label{tab:fusion}
307	\begin{tabular}{lccc}
308	\toprule
309	\textbf{Head} & \textbf{R@1} & \textbf{R@5} & \textbf{Note} \\
310	\midrule
311	Embedding only & 0.556 & 0.961 & Our default \\
312	Structural only & 0.487 & 0.872 & Below random \\
313	Combined & 0.549 & 0.958 & Slight degradation \\
314	\bottomrule
315	\end{tabular}
316	\end{table}
317	
318	Structural features alone perform below the random baseline (R@1${}=0.487$ vs.\ $0.533$), demonstrating that structure cannot replace semantics. The combined head slightly degrades performance versus embedding-only ($-$0.7pp R@1), because CodeQL coverage is incomplete (34\%) and missing features at inference introduce noise. This result sharply distinguishes \ours{} from inference-time graph methods: structural information's value lies in \emph{training-time negative mining} (improving representations), not inference-time features.
319	
320	\subsection{Dynamic Mining Baseline}
321	
322	We compare static mining (negatives mined once before training) with dynamic mining (re-mined every epoch).
323	
324	\begin{table}[t]
325	\centering
326	\small
327	\caption{Static vs.\ dynamic mining.}
328	\label{tab:dynamic}
329	\begin{tabular}{llcc}
330	\toprule
331	\textbf{Mining} & \textbf{Strategy} & \textbf{R@1} & \textbf{Time (h)} \\
332	\midrule
333	Static & Embedding & 0.556 & 3.2 \\
334	Dynamic & Embedding & 0.561 & 9.0 \\
335	Static & Dataflow & 0.548 & 3.2 \\
336	Dynamic & Dataflow & 0.552 & 9.0 \\
337	\bottomrule
338	\end{tabular}
339	\end{table}
340	
341	Dynamic mining yields marginal improvement (+0.5pp for embedding, +0.4pp for dataflow) at 2.8$\times$ training cost. The small delta confirms that embedding mining's benefit stems from the \emph{selection criterion itself} (picking truly hard negatives), not from curriculum effects. Static mining is near-optimal for LoRA fine-tuning where representation drift is limited.
342	
343	\subsection{Dataflow-Distance Weighting}
344	
345	We test whether weighting dataflow negatives by graph distance improves over binary connected/disconnected selection.
346	
347	\begin{table}[t]
348	\centering
349	\small
350	\caption{Binary vs.\ distance-weighted dataflow negatives.}
351	\label{tab:weighted}
352	\begin{tabular}{lcc}
353	\toprule
354	\textbf{Method} & \textbf{Qwen R@1} & \textbf{StarCoder R@1} \\
355	\midrule
356	Binary (default) & 0.548 & 0.489 \\
357	Distance-weighted & 0.551 & 0.490 \\
358	\bottomrule
359	\end{tabular}
360	\end{table}
361	
362	Weighted negatives provide negligible improvement (+0.3pp Qwen, +0.1pp StarCoder). The binary connected/disconnected distinction captures the primary signal; finer granularity offers diminishing returns. This simplifies the method: ``disconnected = hard negative'' requires no additional parameterization.
363	
364	\subsection{SWE-bench Failure Analysis}
365	
366	We manually analyze 50 instances where BM25/SweRank fails, categorizing whether dataflow-aware retrieval would help.
367	
368	\begin{table}[t]
369	\centering
370	\small
371	\caption{Failure analysis: where dataflow helps (50 instances).}
372	\label{tab:failure}
373	\begin{tabular}{lccc}
374	\toprule
375	\textbf{Category} & \textbf{Count} & \textbf{DF Helps} & \textbf{Help Rate} \\
376	\midrule
377	Cross-file dependency & 14 & 11 & 79\% \\
378	Same-file semantic & 12 & 3 & 25\% \\
379	Missing context & 10 & 3 & 30\% \\
380	LLM reasoning failure & 8 & 1 & 12\% \\
381	Other & 6 & 0 & 0\% \\
382	\midrule
383	\textbf{Total} & \textbf{50} & \textbf{18} & \textbf{36\%} \\
384	\bottomrule
385	\end{tabular}
386	\end{table}
387	
388	Dataflow mining is most effective for cross-file dependency failures (79\% help rate), where the gold file has a dataflow connection to the query but low lexical similarity. This aligns with the 41\% connected-not-gold rate ($Z\%$) from our extraction pipeline. LLM reasoning failures are retrieval-independent and naturally unaffected.
389	
390	\subsection{Qualitative Case Studies}
391	
392	We identify 8 representative cases where structural negatives change retrieval outcomes, covering four patterns:
393	
394	\begin{itemize}
395	\item \textbf{Import chain recovery} (3 cases): The gold file is connected to the query via an import chain but has low textual overlap. Dataflow negatives exclude structurally connected files from the negative set, allowing the encoder to learn the relevance of import-linked files.
396	
397	\item \textbf{Utility vs.\ core disambiguation} (2 cases): \texttt{utils.py}-style files share tokens with core modules. Dataflow correctly identifies utilities with data flow to core as connected rather than false negatives.
398	
399	\item \textbf{Test file suppression} (2 cases): Test files are lexically similar to source files but dataflow-disconnected, and are correctly down-weighted as negatives.
400	
401	\item \textbf{Config dependency detection} (1 case): A configuration file with no textual similarity to the query is connected via dataflow through a settings-loading chain.
402	\end{itemize}
403	
404	% ============================================================
405	\section{Discussion}
406	
407	\paragraph{Representation saturation as a predictor.} Our central mechanistic finding is that the effectiveness of structural negatives depends on encoder representation geometry. Qwen2.5-Coder-3B exhibits pos\_sim${}=0.986$ (nearly all positive pairs map to near-identical vectors), making random negatives trivially easy to distinguish. Embedding mining raises negative difficulty, and dataflow adds an orthogonal structural axis. StarCoder2-3B, with pos\_sim${}=0.799$, has sufficient representational headroom that embedding mining alone captures the difficulty gradient. Practitioners can measure pos\_sim before training to predict whether structural negatives will help.
408	
409	\paragraph{Relationship to inference-time methods.}
410	Table~\ref{tab:paradigm} positions \ours{} relative to inference-time graph methods.
411	
412	\begin{table}[t]
413	\centering
414	\small
415	\caption{Training-time vs.\ inference-time structural methods.}
416	\label{tab:paradigm}
417	\begin{tabular}{lcc}
418	\toprule
419	\textbf{Dimension} & \textbf{\ours{}} & \textbf{CodexGraph/LocAgent} \\
420	\midrule
421	Signal injection & Training & Inference \\
422	Inference overhead & Zero & Per-query traversal \\
423	Graph freshness & Static & Dynamic \\
424	Compatibility & Any retriever & Specific framework \\
425	\bottomrule
426	\end{tabular}
427	\end{table}
428	
429	The approaches are complementary: \ours{} improves the retriever's learned representations; inference-time methods improve the retrieval process. Combining both is a promising direction.
430	
431	\paragraph{Limitations.} Our study uses two 3B-parameter encoders; the saturation threshold may differ for larger or smaller models. SWE-bench Lite (300 instances) provides limited statistical power for detecting small resolve-rate differences. CodeQL extraction covers Python only; extending to other languages requires language-specific queries.
432	
433	% ============================================================
434	\section{Conclusion}
435	
436	We present a systematic study of hard negative mining strategies for contrastive code retrieval. Our controlled experiments across two encoders with 9 seeds each establish that: (1)~true embedding-distance mining consistently improves retrieval, correcting prior reports of harm; (2)~structure-grounded dataflow negatives provide conditional benefit mediated by representation saturation; and (3)~the encoder--strategy interaction is explained by negative-difficulty margin analysis. SWE-bench Lite evaluation confirms downstream transfer. Our inter-procedural CodeQL extraction pipeline provides a practical, scalable structural negative generator with zero inference overhead.
437	
438	\bibliographystyle{plainnat}
439	
440	
441	\end{document}
442	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a37b48f-ab1f-4fc1-8e9f-c54b1ebb4a20",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "f0d17afa-e575-4765-9a0b-1e92a47945d4",
  "sourceToolAssistantUUID": "4a37b48f-ab1f-4fc1-8e9f-c54b1ebb4a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T08:25:29.642Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vm811HoFk7V41zcdCHCkgV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/paper.tex",
  "offset": 200,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0d17afa-e575-4765-9a0b-1e92a47945d4",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29BDt6scj99PtFLCPHF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "302ff9f5-5e30-4e9d-aa7d-a48ae9546981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dzsBBSDmFfNtDRt39QC3A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9406,
      "cache_read_input_tokens": 45913,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9406
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 45913,
          "cache_creation_input_tokens": 9406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9406,
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

_source line 43 · 2026-05-14T08:25:29.646Z_

<details><summary>↩ Tool result · `toolu_01Vm811HoFk7V41zcdCHCkgV`</summary>

```text
200	\centering
201	\small
202	\begin{tabular}{lcc}
203	\toprule
204	\textbf{Dataflow Effect} & \textbf{Count} & \textbf{\%} \\
205	\midrule
206	Helps & 5 & 27.8 \\
207	Neutral & 10 & 55.6 \\
208	Hurts & 3 & 16.7 \\
209	\bottomrule
210	\end{tabular}
211	\caption{Dataflow strategy impact on the 18 retrieval-miss cases.}
212	\label{tab:dataflow_impact}
213	\end{table}
214	
215	The cases where dataflow helps involve cross-file dependency chains where structural connectivity provides a signal orthogonal to text similarity. However, the majority of retrieval misses involve files with no extractable dataflow relationship or where CodeQL's coverage gaps introduce noise.
216	
217	%------------------------------------------------------------
218	\section{Analysis}
219	\label{sec:analysis}
220	%------------------------------------------------------------
221	
222	\subsection{Representation Geometry and Encoder-Strategy Interaction}
223	
224	The divergent behavior of dataflow negatives across encoders motivates a closer examination of representation geometry. Qwen2.5-Coder-3B exhibits a saturated representation space ($\text{pos\_sim} = 0.9855$): positive pairs are nearly indistinguishable from hard negatives in embedding space, leaving minimal margin for the contrastive loss to exploit. StarCoder2-3B maintains healthier separation ($\text{pos\_sim} = 0.7985$).
225	
226	Under saturation, random negatives provide insufficient gradient signal because most are too easy. Embedding-distance negatives help by selecting harder examples, but the improvement is bounded by the compressed geometry. Dataflow negatives introduce an orthogonal structural dimension, potentially breaking the saturation---but only when the structural signal is reliable. On StarCoder, where the embedding space already provides adequate difficulty gradients, structural negatives add noise without benefit.
227	
228	Negative difficulty margin analysis supports this mechanism: the margin between gold and negative similarity is +17\% larger for Qwen (confirming saturation pressure) and +28\% for StarCoder (where even random negatives are adequately difficult).
229	
230	\subsection{Embedding Benefit by Repository Complexity}
231	\label{sec:complexity}
232	
233	We stratify the embedding-distance benefit by repository size to test whether the advantage diminishes as the candidate pool grows. Table~\ref{tab:complexity} shows results for Qwen.
234	
235	\begin{table}[t]
236	\centering
237	\small
238	\begin{tabular}{lccc}
239	\toprule
240	\textbf{Repo Size Tier} & \textbf{$N$ repos} & \textbf{Embed $\Delta$ R@1 (pp)} & \textbf{Mean neg.\ difficulty margin} \\
241	\midrule
242	$<$50 instances & 1 & +2.1 & 0.068 \\
243	50--200 & 17 & +1.0 & 0.032 \\
244	200--500 & 40 & +0.3 & 0.019 \\
245	500+ & 29 & $-$0.2 & 0.014 \\
246	\bottomrule
247	\end{tabular}
248	\caption{Embedding-distance benefit by repository size (Qwen). The correlation between repo size and benefit is $r = -0.41$, $p = 0.08$.}
249	\label{tab:complexity}
250	\end{table}
251	
252	The trend is directionally consistent with a saturation hypothesis: in smaller repositories, the candidate pool is compact enough that embedding distance effectively distinguishes near-miss negatives from easy ones. As repository size grows, the embedding space becomes more crowded, diminishing the discriminative power of distance-based mining. The correlation ($r = -0.41$, $p = 0.08$) does not reach conventional significance, likely due to limited statistical power ($n = 87$ repos with structural data). We present this as exploratory evidence suggesting repository complexity moderates embedding benefit.
253	
254	\subsection{Temperature Sensitivity}
255	\label{sec:temperature}
256	
257	We ablate temperature $\tau \in \{0.05, 0.1, 0.2\}$ across all strategies and both encoders. Tables~\ref{tab:temp_qwen} and~\ref{tab:temp_starcoder} report results.
258	
259	\begin{table}[t]
260	\centering
261	\small
262	\begin{tabular}{lccccc}
263	\toprule
264	$\tau$ & \textbf{Random} & \textbf{Embed} & \textbf{Dataflow} & \textbf{Embed $\Delta$} & \textbf{Dataflow $\Delta$} \\
265	\midrule
266	0.05 & 0.521 & 0.534 & 0.530 & +1.3 & +0.9 \\
267	0.10 & 0.533 & 0.543 & 0.538 & +1.0 & +0.5 \\
268	0.20 & 0.524 & 0.531 & 0.527 & +0.7 & +0.3 \\
269	\bottomrule
270	\end{tabular}
271	\caption{Temperature ablation on SWE-smith validation (Qwen, R@1). Embedding benefit direction is consistent across all $\tau$ values.}
272	\label{tab:temp_qwen}
273	\end{table}
274	
275	\begin{table}[t]
276	\centering
277	\small
278	\begin{tabular}{lccccc}
279	\toprule
280	$\tau$ & \textbf{Random} & \textbf{Embed} & \textbf{Dataflow} & \textbf{Embed $\Delta$} & \textbf{Dataflow $\Delta$} \\
281	\midrule
282	0.05 & 0.438 & 0.443 & 0.430 & +0.5 & $-$0.8 \\
283	0.10 & 0.449 & 0.456 & 0.441 & +0.7 & $-$0.8 \\
284	0.20 & 0.442 & 0.446 & 0.435 & +0.4 & $-$0.7 \\
285	\bottomrule
286	\end{tabular}
287	\caption{Temperature ablation on SWE-smith validation (StarCoder, R@1). Dataflow consistently underperforms random on this encoder.}
288	\label{tab:temp_starcoder}
289	\end{table}
290	
291	The embedding $>$ random direction is robust across all temperature settings for both encoders, supporting the claim that embedding-distance mining provides genuine benefit independent of the temperature regime. Dataflow shows inconsistent direction across encoders: positive for Qwen at all temperatures but negative for StarCoder at all temperatures. The optimal temperature is $\tau = 0.1$ for both encoders, with $\tau = 0.05$ increasing cross-seed variance and $\tau = 0.2$ flattening the difficulty gradient.
292	
293	%------------------------------------------------------------
294	\section{Ablation Studies}
295	\label{sec:ablations}
296	%------------------------------------------------------------
297	
298	\subsection{Call-Graph Hop Depth}
299	\label{sec:hops}
300	
301	We ablate the hop depth for dataflow connectivity (Table~\ref{tab:hops}). The 2-hop setting slightly outperforms 1-hop (+0.7pp) as it captures transitive dependencies, but 3-hop degrades ($-$0.4pp vs.\ 2-hop) because deep connectivity in large repositories approaches full-graph reachability, diluting the structural signal. Coverage also decreases with depth as fewer disconnected negatives remain.
302	
303	\begin{table}[t]
304	\centering
305	\small
306	\begin{tabular}{lccc}
307	\toprule
308	\textbf{Hops} & \textbf{R@1} & \textbf{Coverage (\%)} & \textbf{Avg neg/query} \\
309	\midrule
310	1-hop & 0.531 & 42.1 & 8.3 \\
311	2-hop & 0.538 & 34.3 & 5.7 \\
312	3-hop & 0.534 & 28.7 & 3.9 \\
313	\bottomrule
314	\end{tabular}
315	\caption{Hop depth ablation (Qwen, dataflow strategy). Differences are within noise range (cross-seed std $\approx$ 1.5--3.0pp).}
316	\label{tab:hops}
317	\end{table}
318	
319	The differences are within the cross-seed variance ($\sim$1.5--3.0pp), so we treat 2-hop as a reasonable default rather than a critical design choice.
320	
321	\subsection{Training Data Size Scaling}
322	\label{sec:scaling}
323	
324	Table~\ref{tab:scaling} reports R@1 as a function of training set size. Overall performance improves from 1K to 3K instances but plateaus at 5K, consistent with overfitting observed after step 1000 in training runs.
325	
326	\begin{table}[t]
327	\centering
328	\small
329	\begin{tabular}{lcccc}
330	\toprule
331	\textbf{Train Size} & \textbf{Random R@1} & \textbf{Embed R@1} & \textbf{$\Delta$ (pp)} \\
332	\midrule
333	1K & 0.500 & 0.518 & +1.8 \\
334	3K & 0.530 & 0.541 & +1.1 \\
335	5K & 0.529 & 0.538 & +0.9 \\
336	\bottomrule
337	\end{tabular}
338	\caption{Data scaling for Qwen (embedding strategy). The embedding benefit diminishes with more training data.}
339	\label{tab:scaling}
340	\end{table}
341	
342	The embedding benefit diminishes from +1.8pp at 1K to +0.9pp at 5K, suggesting that larger datasets provide sufficient coverage to reduce dependence on mining strategy quality. This is a relevant limitation: the practical value of sophisticated mining may diminish at production data scales.
343	
344	\subsection{Fusion Head}
345	\label{sec:fusion}
346	
347	Table~\ref{tab:fusion} compares three scoring heads: embedding-only, structural-features-only, and combined.
348	
349	\begin{table}[t]
350	\centering
351	\small
352	\begin{tabular}{lcc}
353	\toprule
354	\textbf{Head} & \textbf{Qwen R@1} & \textbf{StarCoder R@1} \\
355	\midrule
356	Embed-only & 0.538 & 0.451 \\
357	Struct-only & 0.489 & 0.412 \\
358	Combined & 0.541 & 0.448 \\
359	\bottomrule
360	\end{tabular}
361	\caption{Fusion head ablation. Structural features alone are weak; the combined head provides marginal additive benefit for Qwen (+0.3pp) but slightly hurts StarCoder ($-$0.3pp).}
362	\label{tab:fusion}
363	\end{table}
364	
365	Structural features alone perform poorly (R@1 = 0.489/0.412) because CodeQL dataflow features are binary and sparse, lacking fine-grained discrimination. The combined head adds only +0.3pp over embed-only for Qwen and is slightly harmful for StarCoder ($-$0.3pp), suggesting that the structural signal's primary value is in \emph{negative selection} during training, not in scoring at inference time.
366	
367	\subsection{Weighted vs.\ Binary Dataflow Negatives}
368	\label{sec:weighted}
369	
370	We test whether distance-weighted sampling from the dataflow graph improves over binary (connected/disconnected) selection (Table~\ref{tab:weighted}).
371	
372	\begin{table}[t]
373	\centering
374	\small
375	\begin{tabular}{lcc}
376	\toprule
377	\textbf{Method} & \textbf{Qwen R@1} & \textbf{StarCoder R@1} \\
378	\midrule
379	Binary (default) & 0.538 & 0.448 \\
380	Distance-weighted & 0.535 & 0.444 \\
381	\bottomrule
382	\end{tabular}
383	\caption{Binary vs.\ distance-weighted dataflow negative selection. No improvement from weighting.}
384	\label{tab:weighted}
385	\end{table}
386	
387	Distance-weighted sampling does not improve over binary selection, likely due to the bimodal distribution of dataflow distances (most pairs are either 1--2 hops or completely disconnected), which causes smooth weighting to degenerate to approximate binary selection.
388	
389	\subsection{Static vs.\ Dynamic Mining}
390	\label{sec:dynamic}
391	
392	Table~\ref{tab:dynamic} compares static mining (once from pretrained encoder) with dynamic re-mining per epoch.
393	
394	\begin{table}[t]
395	\centering
396	\small
397	\begin{tabular}{lccc}
398	\toprule
399	\textbf{Mining} & \textbf{Qwen R@1} & \textbf{StarCoder R@1} & \textbf{GPU hours} \\
400	\midrule
401	Static & 0.543 & 0.456 & 3.5 \\
402	Dynamic & 0.547 & 0.452 & 11.2 \\
403	\bottomrule
404	\end{tabular}
405	\caption{Static vs.\ dynamic mining. Dynamic re-mining provides no significant benefit at $3.2\times$ compute cost.}
406	\label{tab:dynamic}
407	\end{table}
408	
409	Dynamic re-mining does not significantly improve over static mining ($\Delta = +0.4$pp Qwen, $-$0.4pp StarCoder), which is expected given the limited representation drift in 3-epoch LoRA fine-tuning. The $3.2\times$ compute overhead is not justified. This also confirms that the static mining protocol used throughout our experiments is not a confound.
410	
411	%------------------------------------------------------------
412	\section{Qualitative Analysis}
413	\label{sec:qualitative}
414	%------------------------------------------------------------
415	
416	We curate 8 representative cases where structural negatives changed retrieval outcomes (4 positive, 2 negative, 2 ambiguous).
417	
418	\paragraph{Positive examples.} In 4 cases, dataflow-disconnected negatives help the retriever distinguish lexically similar but structurally unrelated files. For instance, in a Django repository, two utility modules share significant token overlap (\texttt{utils/validators.py} and \texttt{utils/formatters.py}) but have no dataflow connection. Dataflow-aware training teaches the encoder to separate these, improving retrieval of the true bug-fix target.
419	
420	\paragraph{Negative examples.} In 2 cases, the structural bias introduced by dataflow negatives causes misses. One involves a file pair connected through a rarely-exercised code path that CodeQL fails to extract; the model learns to treat them as disconnected when they are functionally related.
421	
422	\paragraph{Ambiguous examples.} Two cases show mixed signals where the retrieval outcome differs between seeds, suggesting the structural signal interacts with other training noise.
423	
424	The pattern across cases is not clean enough to support strong causal inference from $n = 2$ encoders, but the positive examples demonstrate a plausible mechanism by which structural negatives can complement text-based mining.
425	
426	%------------------------------------------------------------
427	\section{Discussion}
428	\label{sec:discussion}
429	%------------------------------------------------------------
430	
431	\subsection{Positioning Relative to Inference-Time Methods}
432	
433	Table~\ref{tab:inference_compare} contextualizes our approach against inference-time structural methods.
434	
435	\begin{table}[t]
436	\centering
437	\small
438	\begin{tabular}{lllll}
439	\toprule
440	\textbf{Method} & \textbf{Type} & \textbf{Structural Signal} & \textbf{Inf.\ Cost} & \textbf{Reported Gain} \\
441	\midrule
442	StructFuse (ours) & training & CodeQL dataflow & zero & +0.5--1.5pp R@1 \\
443	CodexGraph & inference & LLM-built graph & high & +5.2pp R@1 \\
444	LocAgent & inference & call graph nav. & moderate & 26.3\% resolve \\
445	\bottomrule
446	\end{tabular}
447	\caption{Training-time vs.\ inference-time structural methods. StructFuse is complementary: it improves the base retriever at zero inference cost.}
448	\label{tab:inference_compare}
449	\end{table}
450	
451	StructFuse operates at training time with zero inference overhead, improving the base retriever that inference-time methods build upon. The gains are modest compared to inference-time approaches, but the two paradigms are complementary: a better base retriever provides a stronger starting point for graph-guided navigation. Validating this complementarity is an important direction for future work.
452	
453	\subsection{Limitations}
454	
455	\begin{itemize}
456	\item \textbf{Two encoders.} Our encoder-strategy interaction observation is based on $n = 2$ architectures. While the representation geometry mechanism provides explanatory power, broader validation is needed.
457	\item \textbf{Diminishing returns at scale.} The embedding mining benefit shrinks with more training data (Table~\ref{tab:scaling}), suggesting limited practical value at production scales.
458	\item \textbf{Downstream gap.} Retrieval-level improvements do not translate to statistically significant downstream gains on SWE-bench Lite. The generation bottleneck dominates.
459	\item \textbf{CodeQL coverage.} Dataflow extraction covers 123/131 repos but structural relationships are incomplete---CodeQL misses dynamically dispatched calls and reflection-heavy code.
460	\item \textbf{Confidence intervals.} For RepoBench-R, the StarCoder embedding benefit (+0.5pp) has a 95\% CI that includes zero. We characterize all claims as directional evidence, not definitive conclusions.
461	\end{itemize}
462	
463	%------------------------------------------------------------
464	\section{Conclusion}
465	\label{sec:conclusion}
466	%------------------------------------------------------------
467	
468	We present a controlled study of hard negative mining strategies for contrastive code retrieval. Our findings provide directional evidence that true embedding-distance mining tends to improve retrieval over random baselines, correcting prior reports based on BM25-proxy confounds. Dataflow-grounded negatives show conditional, encoder-dependent effects that we link to representation geometry---an exploratory observation warranting further investigation.
469	
470	Our primary contributions are methodological: a controlled comparison framework that isolates mining strategy effects, a representation geometry analysis that explains encoder-strategy interactions, and a scalable CodeQL extraction pipeline for structural negatives. End-to-end evaluation on SWE-bench Lite yields no significant differences, an important finding for calibrating expectations about retrieval-only improvements in agent pipelines.
471	
472	These results suggest that the next frontier lies not in harder negatives alone, but in generation-aware retrieval training that accounts for downstream bottlenecks. We release our framework and data to support this investigation.
473	
474	\bibliography{custom}
475	
476	\end{document}
477	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "302ff9f5-5e30-4e9d-aa7d-a48ae9546981",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "d9b08d92-30d6-4e68-a6d4-d9f68e53f5cc",
  "sourceToolAssistantUUID": "302ff9f5-5e30-4e9d-aa7d-a48ae9546981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T08:25:32.537Z_

Now let me read the dream review reports to understand what prior reviewers identified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9b08d92-30d6-4e68-a6d4-d9f68e53f5cc",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29BfvGidjzfjypxdyxt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1890ef5-e567-4b77-bfba-2776735a901d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExKuSb5CQKEU2awUWc26a2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10035,
      "cache_read_input_tokens": 55319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10035,
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

_source line 45 · 2026-05-14T08:25:34.859Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NbXEEA9bWqKzS1QJNSRLuj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1890ef5-e567-4b77-bfba-2776735a901d",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29BfvGidjzfjypxdyxt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3266a8a-315e-4a0c-937a-687763389ab4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExKuSb5CQKEU2awUWc26a2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10035,
      "cache_read_input_tokens": 55319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10035,
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

_source line 46 · 2026-05-14T08:25:34.863Z_

<details><summary>↩ Tool result · reported error · `toolu_01NbXEEA9bWqKzS1QJNSRLuj`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3266a8a-315e-4a0c-937a-687763389ab4",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "0e4f47f2-f89d-4bca-97ec-ec3abe4914a0",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context.",
  "sourceToolAssistantUUID": "d3266a8a-315e-4a0c-937a-687763389ab4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T08:25:35.378Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Sb8qMdVgzyYokx4nioXECf`</summary>

```json
{
  "pattern": "artifacts/dream_reports/dream_20260514T075732/*/review_report.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e4f47f2-f89d-4bca-97ec-ec3abe4914a0",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29BfvGidjzfjypxdyxt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4d6e4fe-defc-48eb-94f5-63d30dd371fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExKuSb5CQKEU2awUWc26a2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10035,
      "cache_read_input_tokens": 55319,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10035
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 55319,
          "cache_creation_input_tokens": 10035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10035,
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

_source line 48 · 2026-05-14T08:25:35.395Z_

<details><summary>↩ Tool result · `toolu_01Sb8qMdVgzyYokx4nioXECf`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4d6e4fe-defc-48eb-94f5-63d30dd371fd",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "44e7201b-3b99-4ff7-802d-7a1373a9fdce",
  "sourceToolAssistantUUID": "d4d6e4fe-defc-48eb-94f5-63d30dd371fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T08:25:39.768Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019ZJcr7mmLUem4G18bLnGw3`</summary>

```json
{
  "pattern": "artifacts/dream_reports/dream_20260514T075732/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44e7201b-3b99-4ff7-802d-7a1373a9fdce",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29C6aqRwjEZaiSdbaxo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09629f2b-f4ec-4583-8832-39f4802b69e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018N1Dtx2BdZKa8upE6shFFb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 65354,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 319
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 65354,
          "cache_creation_input_tokens": 319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 319,
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

_source line 50 · 2026-05-14T08:25:39.782Z_

<details><summary>↩ Tool result · `toolu_019ZJcr7mmLUem4G18bLnGw3`</summary>

```text
artifacts/dream_reports/dream_20260514T075732/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T075732/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T075732/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T075732/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T075732/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json
artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/best/paper.tex
artifacts/dream_reports/dream_20260514T075732/best/paper.aux
artifacts/dream_reports/dream_20260514T075732/best/paper.out
artifacts/dream_reports/dream_20260514T075732/best/paper.pdf
artifacts/dream_reports/dream_20260514T075732/best/paper.log
artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T075732/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/median/experiment_data.json
artifacts/dream_reports/dream_20260514T075732/median/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/median/paper.tex
artifacts/dream_reports/dream_20260514T075732/median/paper.aux
artifacts/dream_reports/dream_20260514T075732/median/paper.out
artifacts/dream_reports/dream_20260514T075732/median/paper.pdf
artifacts/dream_reports/dream_20260514T075732/median/paper.log
artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/worst/paper.tex
artifacts/dream_reports/dream_20260514T075732/worst/paper.aux
artifacts/dream_reports/dream_20260514T075732/worst/paper.out
artifacts/dream_reports/dream_20260514T075732/worst/paper.pdf
artifacts/dream_reports/dream_20260514T075732/worst/paper.log
artifacts/dream_reports/dream_20260514T075732/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T075732/best/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09629f2b-f4ec-4583-8832-39f4802b69e4",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "6be2f8cd-411e-40c9-9abb-c27d9684335a",
  "sourceToolAssistantUUID": "09629f2b-f4ec-4583-8832-39f4802b69e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T08:25:43.482Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CWuTaSgm4xtWeMHgukPyvK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6be2f8cd-411e-40c9-9abb-c27d9684335a",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29CRFk1hKjFJ4BNLk49",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ff90779-a51d-4b1c-8b9d-29d493804add",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VApyYouLE7JS6EJBs7w4C2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 65673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 898,
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

_source line 52 · 2026-05-14T08:25:43.912Z_

<details><summary>↩ Tool result · `toolu_01CWuTaSgm4xtWeMHgukPyvK`</summary>

```text
1	narrative_guidance: '9-seed 全量复现完全确认 pilot 模式。Embedding mining 在两个编码器上均显著优于 random（bootstrap
2	  95% CI 不含零）， dataflow 在 Qwen 上提供条件性额外收益而在 StarCoder 上无显著差异，产生干净的交互效应。 SWE-bench
3	  下游验证显示可观测的 resolve rate 提升。机制故事（表征饱和度 → 策略有效性）通过 neg_difficulty margin、 温度消融、动态挖掘对照三条证据线完整闭合。论文三条
4	  claim 均有充分统计支撑，EMNLP Main 定位清晰。
5	
6	  '
7	imagined_experiments:
8	- name: SWE-bench Lite End-to-End Evaluation
9	  plan_id: plan_003
10	  description: 3 strategies × best checkpoint on SWE-bench Lite (300), Qwen3.6-27B
11	    agent, 测 resolve rate
12	  expected_results:
13	    random_resolve_rate: 0.227
14	    embedding_distance_resolve_rate: 0.25
15	    dataflow_aware_resolve_rate: 0.26
16	    embed_vs_random_delta_pp: 2.3
17	    dataflow_vs_random_delta_pp: 3.3
18	    dataflow_vs_embed_delta_pp: 1.0
19	    total_instances: 300
20	    instances_resolved_random: 68
21	    instances_resolved_embed: 75
22	    instances_resolved_dataflow: 78
23	    retrieval_recall1_random: 0.533
24	    retrieval_recall1_embed: 0.556
25	    retrieval_recall1_dataflow: 0.548
26	  result_rationale: 'best 档下 retrieval 质量提升能传导到下游 resolve rate。Qwen best checkpoint
27	    embedding R@1≈0.556 vs random 0.533， 差值 2.3pp 在 300 实例上对应约 7 个额外正确 retrieval →
28	    其中部分转化为 resolve。 转化率不是 1:1（retrieval 改善不等于 repair 改善，LLM agent 有自身能力上限）， 但 best
29	    档假设转化效率约 30-40%，即 ~7 个额外正确 retrieval 中约 2-3 个转为 resolve。 Dataflow 在 Qwen 上的条件性收益（pilot
30	    +0.8pp R@1）进一步贡献约 1pp resolve delta。 总体 swebench_resolve_delta_pp 落在 [2.0, 5.0]
31	    范围的中低段， 因为 retrieval → repair 的衰减是系统性的。SWE-bench Lite 300 实例规模下， 2-3pp 差异虽小但在
32	    best 档下 bootstrap CI 可检测。
33	
34	    '
35	  tables:
36	  - caption: SWE-bench Lite Resolve Rate by Retrieval Strategy
37	    columns:
38	    - Strategy
39	    - Resolve_Rate
40	    - Delta_vs_Random
41	    - Instances_Resolved
42	    rows:
43	    - - random
44	      - 22.7%
45	      - —
46	      - 68
47	    - - embedding_distance
48	      - 25.0%
49	      - +2.3pp
50	      - 75
51	    - - dataflow_aware
52	      - 26.0%
53	      - +3.3pp
54	      - 78
55	  figures_description:
56	  - 'Bar chart: resolve rate × strategy, error bars from bootstrap resampling'
57	  - 'Venn diagram: 3 strategies 各自独立解决的 instances 重叠情况，突出 dataflow-unique solves'
58	  analysis: 'Resolve rate 提升确认 retrieval 质量改善能传导到实际软件工程任务。Dataflow 策略独立解决了 5 个 random/embed
59	    均失败的 instance（多为跨文件 dataflow 依赖），支持 Claim 2 的条件性收益叙事。 Embed 策略独立解决 3 个（多为同文件内近义函数混淆），支持
60	    Claim 1。
61	
62	    '
63	- name: RepoBench-R Cross-File Retrieval Evaluation
64	  plan_id: plan_004
65	  description: 3 strategies × best checkpoint on RepoBench-R, retrieval-only evaluation
66	  expected_results:
67	    random_recall1: 0.412
68	    embedding_distance_recall1: 0.431
69	    dataflow_aware_recall1: 0.438
70	    random_mrr: 0.508
71	    embedding_distance_mrr: 0.529
72	    dataflow_aware_mrr: 0.534
73	    embed_vs_random_R1_delta_pp: 1.9
74	    dataflow_vs_random_R1_delta_pp: 2.6
75	    total_queries: 1200
76	  result_rationale: 'RepoBench-R 是 cross-file retrieval benchmark，天然偏向有结构依赖的查询（import/call
77	    关系）。 在 best 档下，embedding 改善幅度与 SWE-smith 内部 eval 一致（~2pp）， dataflow 的额外收益在此 benchmark
78	    上可能略大于 SWE-smith（因 RepoBench-R 的 cross-file 性质与 dataflow connectivity 天然对齐），但差异不会很大因为训练数据来自
79	    SWE-smith 而非 RepoBench， 存在 domain gap。整体 R@1 低于 SWE-smith 内部 eval（0.41 vs 0.53），
80	    因为 pool size 和 query 分布不同。关键是方向一致且差异可检测。
81	
82	    '
83	  tables:
84	  - caption: RepoBench-R Retrieval Performance
85	    columns:
86	    - Strategy
87	    - R@1
88	    - R@5
89	    - R@10
90	    - MRR
91	    rows:
92	    - - random
93	      - 0.412
94	      - 0.687
95	      - 0.793
96	      - 0.508
97	    - - embedding_distance
98	      - 0.431
99	      - 0.704
100	      - 0.808
101	      - 0.529
102	    - - dataflow_aware
103	      - 0.438
104	      - 0.711
105	      - 0.812
106	      - 0.534
107	  figures_description:
108	  - 'Grouped bar chart: R@1, R@5, R@10 × strategy on RepoBench-R'
109	  analysis: '第二 benchmark 确认 SWE-smith 上的发现不是 benchmark-specific artifact。 策略排序一致（dataflow
110	    ≥ embed > random），增强论文的 external validity。
111	
112	    '
113	- name: Embedding vs Random Stratified Analysis
114	  plan_id: plan_005
115	  description: 按 repo size/complexity 分层，分析 embedding negatives 的收益分布
116	  expected_results:
117	    small_repo_lt50_embed_delta_pp: 0.8
118	    medium_repo_50_200_embed_delta_pp: 2.1
119	    large_repo_200_500_embed_delta_pp: 2.8
120	    xlarge_repo_500plus_embed_delta_pp: 1.5
121	    high_complexity_embed_delta_pp: 2.9
122	    low_complexity_embed_delta_pp: 1.2
123	    correlation_repo_size_vs_delta: 0.31
124	    correlation_complexity_vs_delta: 0.42
125	  result_rationale: 'best 档下 embedding mining 普遍有效但收益分布不均。中大型 repo（50-500 files）收益最大，
126	    因为 pool 中有足够多的 near-miss 候选（lexically similar but not gold）， embedding mining
127	    能有效挑选最有信息量的 hard negatives。小型 repo pool 太小、 embedding mining 退化为近似 random；超大型
128	    repo 结构复杂度使得 embedding distance 与 relevance 的相关性下降（太多 "远但相关" 的文件）。Complexity（cyclomatic
129	    complexity 或 import depth）比 size 更好地预测 embedding mining 收益， 因为高复杂度代码中相似但无关的文件更多。
130	
131	    '
132	  tables:
133	  - caption: Embedding Mining Benefit by Repo Tier
134	    columns:
135	    - Tier
136	    - N_Instances
137	    - Embed_R1
138	    - Random_R1
139	    - Delta_pp
140	    rows:
141	    - - small (<50)
142	      - 500
143	      - 0.568
144	      - 0.56
145	      - '+0.8'
146	    - - medium (50-200)
147	      - 4096
148	      - 0.551
149	      - 0.53
150	      - '+2.1'
151	    - - large (200-500)
152	      - 13628
153	      - 0.542
154	      - 0.514
155	      - '+2.8'
156	    - - xlarge (500+)
157	      - 25949
158	      - 0.528
159	      - 0.513
160	      - '+1.5'
161	  figures_description:
162	  - 'Scatter plot: repo complexity vs embed-random delta, with regression line'
163	  - 'Box plot: delta distribution by repo size tier'
164	  analysis: '收益分布分析提供 practical guidance：embedding mining 对中大型项目最有效， 与表征空间中 near-miss
165	    候选密度的直觉一致。复杂度比 size 更具预测力， 提示 negative mining 策略选择应考虑代码结构特征而非简单规模。
166	
167	    '
168	- name: Hop Distance Ablation
169	  plan_id: plan_007
170	  description: 1-hop vs 2-hop vs 3-hop call-graph bounding for dataflow extraction
171	  expected_results:
172	    hop1_connected_rate: 0.12
173	    hop2_connected_rate: 0.34
174	    hop3_connected_rate: 0.58
175	    hop1_z_pct: 0.18
176	    hop2_z_pct: 0.41
177	    hop3_z_pct: 0.62
178	    hop2_qwen_R1: 0.548
179	    hop1_qwen_R1: 0.541
180	    hop3_qwen_R1: 0.544
181	    hop2_extraction_time_s: 8.9
182	    hop3_extraction_time_s: 23.4
183	  result_rationale: '2-hop 是 sweet spot。1-hop 太严格：大多数 repo 中直接 dataflow 连接的文件对稀少（12%），
184	    导致 connected-not-gold set 太小，dataflow negative mining 退化为近似 random。 3-hop 太宽松：58%
185	    的文件对被标记为 connected，negative pool 被过度稀释， 且提取时间增长 2.6x（路径爆炸）。2-hop（当前默认）在 coverage（34%）和
186	    selectivity（Z=41%）之间取得平衡，R@1 最高。这一结果支持 Claim 3 中的 "scope-bounded" 设计选择。
187	
188	    '
189	  tables:
190	  - caption: Hop Distance Impact on Extraction and Training
191	    columns:
192	    - Hops
193	    - Connected_Rate
194	    - Z_Pct
195	    - Extraction_Time_s
196	    - Qwen_R1
197	    rows:
198	    - - 1
199	      - 12%
200	      - 18%
201	      - 4.2
202	      - 0.541
203	    - - 2
204	      - 34%
205	      - 41%
206	      - 8.9
207	      - 0.548
208	    - - 3
209	      - 58%
210	      - 62%
211	      - 23.4
212	      - 0.544
213	  figures_description:
214	  - 'Line chart: R@1 vs hop distance, with extraction time on secondary y-axis'
215	  analysis: '2-hop 最优确认了设计选择的合理性。3-hop 的 R@1 回落说明过度扩展 connectivity 范围会引入噪声连接，削弱 structural
216	    negative 的信息量。
217	
218	    '
219	- name: Training Data Size Scaling
220	  plan_id: plan_008
221	  description: 1K vs 3K vs 5K training instances, 测 strategy 收益是否随数据量变化
222	  expected_results:
223	    1k_random_R1: 0.498
224	    1k_embed_R1: 0.521
225	    1k_dataflow_R1: 0.518
226	    3k_random_R1: 0.525
227	    3k_embed_R1: 0.548
228	    3k_dataflow_R1: 0.543
229	    5k_random_R1: 0.533
230	    5k_embed_R1: 0.556
231	    5k_dataflow_R1: 0.548
232	    embed_delta_1k: 2.3
233	    embed_delta_3k: 2.3
234	    embed_delta_5k: 2.3
235	    dataflow_delta_1k: 2.0
236	    dataflow_delta_3k: 1.8
237	    dataflow_delta_5k: 1.5
238	  result_rationale: 'best 档下 embedding mining 的收益对数据量 robust（~2.3pp 几乎不变）， 因为 embedding
239	    distance 提供的信息增益是 strategy-intrinsic 的，不依赖数据量。 Dataflow 收益随数据量增加略有递减（2.0→1.5pp），因为更多数据使
240	    random baseline 也能隐式覆盖部分结构相关的 hard negatives（大数定律），缩小了 dataflow 的 marginal 贡献。但即使在
241	    5K 下，dataflow 在 Qwen 上的条件性收益仍然存在。 绝对性能随数据量单调增长但边际递减（符合 neural scaling 预期）。
242	
243	    '
244	  tables:
245	  - caption: Strategy Benefit by Training Data Size
246	    columns:
247	    - Size
248	    - Random_R1
249	    - Embed_R1
250	    - Embed_Delta
251	    - Dataflow_R1
252	    - DF_Delta
253	    rows:
254	    - - 1K
255	      - 0.498
256	      - 0.521
257	      - '+2.3'
258	      - 0.518
259	      - '+2.0'
260	    - - 3K
261	      - 0.525
262	      - 0.548
263	      - '+2.3'
264	      - 0.543
265	      - '+1.8'
266	    - - 5K
267	      - 0.533
268	      - 0.556
269	      - '+2.3'
270	      - 0.548
271	      - '+1.5'
272	  figures_description:
273	  - 'Line chart: R@1 vs data size, 3 lines for 3 strategies, showing parallel scaling
274	    for embed and convergence for dataflow'
275	  analysis: 'Embedding mining 收益的 scale-invariance 强化 Claim 1（普遍有效）。 Dataflow 收益的轻微递减可解释为
276	    "structural signal 被 larger random samples 部分替代"， 但不消失——支持 Claim 2 的 "conditional
277	    benefit" 定位。
278	
279	    '
280	- name: Fusion Head Ablation
281	  plan_id: plan_009
282	  description: Embedding-only vs structural-features-only vs combined fusion head
283	  expected_results:
284	    embed_only_R1: 0.556
285	    structural_only_R1: 0.487
286	    combined_R1: 0.549
287	    embed_only_vs_combined_delta: 0.7
288	  result_rationale: 'best 档下的核心发现是 embedding-only 已经很强（因为我们的方法是 training-time mining
289	    而非 inference-time fusion）。Structural-features-only 单独很弱（R@1=0.487， 低于 random baseline
290	    的 0.533），说明结构信息不能替代语义相似度，只能补充。 Combined fusion head 反而比 embed-only 略低（0.549 vs
291	    0.556），因为加入 structural features 作为 inference-time signal 引入噪声（CodeQL extraction
292	    覆盖率仅 34%， inference 时 missing features 是常态）。这一结果强化论文叙事：结构信息的价值在于 training-time
293	    negative mining（改善表征学习），而非 inference-time feature。
294	
295	    '
296	  tables:
297	  - caption: Fusion Head Comparison (Qwen, best checkpoint)
298	    columns:
299	    - Head
300	    - R@1
301	    - R@5
302	    - Note
303	    rows:
304	    - - embed_only
305	      - 0.556
306	      - 0.961
307	      - Our default
308	    - - structural_only
309	      - 0.487
310	      - 0.872
311	      - Below random baseline
312	    - - combined
313	      - 0.549
314	      - 0.958
315	      - Marginal degradation vs embed_only
316	  figures_description:
317	  - 'Bar chart: R@1 by fusion head type'
318	  analysis: 'Ablation 清晰区分了 structural information 的两种使用方式：training-time mining（有效）
319	    vs inference-time feature（无效或有害）。这是对 inference-time graph methods （CodexGraph,
320	    LocAgent）的重要区分点，支持 plan_017 的讨论。
321	
322	    '
323	- name: Dataflow-Distance Weighted Negatives
324	  plan_id: plan_010
325	  description: Binary connected/disconnected vs dataflow-distance weighted negative
326	    sampling
327	  expected_results:
328	    binary_qwen_R1: 0.548
329	    weighted_qwen_R1: 0.551
330	    binary_starcoder_R1: 0.489
331	    weighted_starcoder_R1: 0.49
332	    weighted_vs_binary_qwen_delta: 0.3
333	    weighted_vs_binary_starcoder_delta: 0.1
334	  result_rationale: 'Distance-weighted sampling 对 Qwen 有微弱额外收益（+0.3pp），因为在饱和空间中 更细粒度的
335	    difficulty gradation 提供略好的 curriculum 效果——离 gold 越远的 disconnected file 越 "easy"，给予更低采样权重，让训练集中在
336	    hard disconnected 上。 但差异很小因为 binary 已经是一个合理的 proxy（connected vs disconnected 的
337	    distinction 捕获了主要信号）。StarCoder 上差异可忽略，与 Claim 2 一致—— dataflow 信号在非饱和空间中 marginal，更细的
338	    granularity 自然也 marginal。 总体结论：binary 足够，weighted 是 diminishing return。
339	
340	    '
341	  tables:
342	  - caption: Binary vs Weighted Dataflow Negatives
343	    columns:
344	    - Method
345	    - Qwen_R1
346	    - StarCoder_R1
347	    rows:
348	    - - binary (default)
349	      - 0.548
350	      - 0.489
351	    - - distance-weighted
352	      - 0.551
353	      - 0.49
354	  figures_description:
355	  - 'Histogram: negative difficulty distribution under binary vs weighted sampling'
356	  analysis: 'Binary 简单且接近最优，weighted 的微弱改善不足以 justify 额外复杂度。 这一 negative result 反而简化了方法描述——"disconnected
357	    = hard negative" 无需更复杂的定义。
358	
359	    '
360	- name: SWE-bench Failure Analysis
361	  plan_id: plan_011
362	  description: 50 个 SweRank/BM25 failures，按 dataflow 是否 help 分类
363	  expected_results:
364	    total_failures_analyzed: 50
365	    dataflow_helps_count: 18
366	    dataflow_helps_pct: 36
367	    failure_categories:
368	      cross_file_dependency: 14
369	      same_file_semantic: 12
370	      missing_context: 10
371	      llm_reasoning_failure: 8
372	      other: 6
373	    dataflow_helps_by_category:
374	      cross_file_dependency: 11
375	      same_file_semantic: 3
376	      missing_context: 3
377	      llm_reasoning_failure: 1
378	      other: 0
379	  result_rationale: '36% 的 BM25/SweRank failure 中 dataflow mining 能提供帮助——这些 case 主要是
380	    cross-file dependency 类型（gold file 与 query file 有 dataflow 连接但 lexical similarity
381	    低）。这个比例与 Z%=41%（connected-not-gold rate）高度一致： 如果 ~40% 的 instances 有 structural
382	    signal 可利用，那么在 failures 中 dataflow helps 的比例也应在类似量级。Same-file semantic failures
383	    中 dataflow 偶尔帮助（因为相同文件内的函数调用也被 dataflow graph 捕获），但这不是主要机制。 LLM reasoning failures
384	    与 retrieval 无关，dataflow 自然无法帮助。
385	
386	    '
387	  tables:
388	  - caption: 'Failure Analysis: Where Dataflow Helps'
389	    columns:
390	    - Category
391	    - Count
392	    - DF_Helps
393	    - DF_Help_Rate
394	    rows:
395	    - - cross_file_dependency
396	      - 14
397	      - 11
398	      - 79%
399	    - - same_file_semantic
400	      - 12
401	      - 3
402	      - 25%
403	    - - missing_context
404	      - 10
405	      - 3
406	      - 30%
407	    - - llm_reasoning_failure
408	      - 8
409	      - 1
410	      - 12%
411	    - - other
412	      - 6
413	      - 0
414	      - 0%
415	  figures_description:
416	  - 'Stacked bar chart: failure categories with dataflow-helps overlay'
417	  - 3 representative case studies with retrieval ranking diff
418	  analysis: 'Dataflow 最大价值在 cross-file dependency failures（79% help rate）， 精确对齐了 Claim
419	    2 的 "structural dimension the encoder cannot separate via text alone" 叙事。
420	
421	    '
422	- name: Qualitative Case Studies
423	  plan_id: plan_012
424	  description: 5-10 个 structural negatives 改变 retrieval outcome 的代表性 case
425	  expected_results:
426	    total_cases: 8
427	    categories:
428	      import_chain_recovery: 3
429	      utility_vs_core_disambiguation: 2
430	      test_file_suppression: 2
431	      config_dependency_detection: 1
432	  result_rationale: 'best 档下可以找到 8 个 clean case studies，覆盖四种典型模式。 Import chain recovery
433	    最多（3 个），因为这是 dataflow connectivity 最直接的信号类型： gold file 通过 import chain 与 query
434	    file 连接，但 lexical similarity 很低（不同功能模块）， random/embed mining 无法区分 "lexically similar
435	    but structurally irrelevant" negatives。 Utility vs core disambiguation（2 个）展示
436	    dataflow 如何将 utils.py 类文件正确 判断为 connected（有 dataflow 到 core 的数据流）而非 false negative。
437	    Test file suppression（2 个）展示 test files 虽 lexically similar 但 dataflow disconnected，被正确降权。
438	
439	    '
440	  tables: []
441	  figures_description:
442	  - 'Figure: 4-panel case study，每 panel 展示 query、gold、top-3 retrieval（random vs dataflow），附
443	    dataflow graph 子图'
444	  analysis: 'Case studies 提供 mechanistic evidence 的具体实例化，让 reviewer 直观理解 "structural
445	    dimension" 到底意味着什么。选择覆盖四种不同模式以展示 generality。
446	
447	    '
448	- name: Temperature Ablation
449	  plan_id: plan_014
450	  description: τ ∈ {0.05, 0.1, 0.2} × 3 strategies × Qwen, 测 regime-specificity
451	  expected_results:
452	    tau_005:
453	      random_R1: 0.518
454	      embed_R1: 0.542
455	      dataflow_R1: 0.539
456	      embed_delta: 2.4
457	      dataflow_delta: 2.1
458	    tau_010:
459	      random_R1: 0.533
460	      embed_R1: 0.556
461	      dataflow_R1: 0.548
462	      embed_delta: 2.3
463	      dataflow_delta: 1.5
464	    tau_020:
465	      random_R1: 0.521
466	      embed_R1: 0.539
467	      dataflow_R1: 0.53
468	      embed_delta: 1.8
469	      dataflow_delta: 0.9
470	    optimal_tau: 0.1
471	    embed_benefit_robust_across_tau: true
472	    dataflow_benefit_strongest_at_low_tau: true
473	  result_rationale: 'best 档下 embedding mining 在所有 τ 值下均有正收益（1.8-2.4pp），确认 Claim 1
474	    的 robustness。τ=0.1 是 sweet spot（pilot 已用的值），R@1 最高。τ=0.05 过低导致 contrastive loss
475	    landscape 太 sharp，所有 strategy 绝对性能下降但 relative ranking 不变。 τ=0.2 过高使 loss 过于平滑，strategy
476	    差异缩小。Dataflow 收益随 τ 增大而递减 （2.1→1.5→0.9pp），因为高温度下 contrastive loss 对 hard vs easy
477	    negatives 的 区分度降低，structural difficulty gradient 被稀释。这一发现提供了 mechanistic insight：
478	    dataflow 的 value proposition 是提供更 hard 的 negatives， 而 temperature 控制了 model 对
479	    hardness 的敏感度。
480	
481	    '
482	  tables:
483	  - caption: Temperature × Strategy Interaction (Qwen)
484	    columns:
485	    - τ
486	    - Random_R1
487	    - Embed_R1
488	    - Embed_Δ
489	    - DF_R1
490	    - DF_Δ
491	    rows:
492	    - - 0.05
493	      - 0.518
494	      - 0.542
495	      - '+2.4'
496	      - 0.539
497	      - '+2.1'
498	    - - 0.1
499	      - 0.533
500	      - 0.556
501	      - '+2.3'
502	      - 0.548
503	      - '+1.5'
504	    - - 0.2
505	      - 0.521
506	      - 0.539
507	      - '+1.8'
508	      - 0.53
509	      - '+0.9'
510	  figures_description:
511	  - 'Line chart: R@1 vs τ, 3 strategy lines, 显示 strategy gap 随 τ 变化'
512	  - 'Heatmap: τ × strategy interaction strength (delta from random)'
513	  analysis: 'Temperature 消融排除了 "finding is τ-specific" 的 reviewer concern。 Embedding
514	    benefit 对 τ robust；dataflow benefit 在低 τ 下最强， 提供 practitioner guidance（如果 encoder
515	    空间饱和 + 低温度 → dataflow 最有价值）。
516	
517	    '
518	- name: Dynamic Embedding Mining Baseline
519	  plan_id: plan_015
520	  description: 每 epoch 重新 mine embedding negatives vs 静态一次性 mine，隔离 selection criterion
521	    和 curriculum shift
522	  expected_results:
523	    static_embed_R1: 0.556
524	    dynamic_embed_R1: 0.561
525	    dynamic_vs_static_delta: 0.5
526	    dynamic_dataflow_R1: 0.552
527	    static_dataflow_R1: 0.548
528	    dynamic_training_time_multiplier: 2.8
529	  result_rationale: 'Dynamic mining 提供微弱改善（+0.5pp），因为随训练进行 encoder representation
530	    会 drift， 重新 mine 能保持 negatives 的 hardness。但差异很小（<1pp），说明 static mining 在 3 epoch
531	    短训练中 drift 不严重——pretrained encoder 的 representation 在 LoRA fine-tune 中变化有限（LoRA
532	    rank=16，参数量仅为全量的 0.3%）。 关键发现：static vs dynamic 的差异远小于 strategy 差异（embed vs random
533	    = 2.3pp vs dynamic vs static = 0.5pp），确认 selection criterion（embedding distance
534	    vs random） 是 primary driver，而非 curriculum shift。这排除了 "embed helps only because
535	    of implicit curriculum" 的 alternative explanation。 Dynamic 的 2.8x 训练时间开销使其不实用。
536	
537	    '
538	  tables:
539	  - caption: Static vs Dynamic Mining
540	    columns:
541	    - Mining
542	    - Strategy
543	    - R1
544	    - Training_Time_h
545	    rows:
546	    - - static
547	      - embedding
548	      - 0.556
549	      - 3.2
550	    - - dynamic
551	      - embedding
552	      - 0.561
553	      - 9.0
554	    - - static
555	      - dataflow
556	      - 0.548
557	      - 3.2
558	    - - dynamic
559	      - dataflow
560	      - 0.552
561	      - 9.0
562	  figures_description:
563	  - 'Bar chart: static vs dynamic × strategy, with training time annotation'
564	  analysis: 'Static mining 在成本效益上远优于 dynamic。更重要的是，排除了 curriculum confound： embedding
565	    mining 的收益来自 selection criterion 本身（挑到 truly hard negatives）， 而非 training dynamics。
566	
567	    '
568	- name: Bootstrap CI for SWE-bench Lite
569	  plan_id: plan_016
570	  description: 9-seed × 3 strategies 的 bootstrap 95% CI for resolve rate
571	  expected_results:
572	    random_resolve_mean: 0.227
573	    random_resolve_ci:
574	    - 0.195
575	    - 0.259
576	    embed_resolve_mean: 0.25
577	    embed_resolve_ci:
578	    - 0.218
579	    - 0.282
580	    dataflow_resolve_mean: 0.26
581	    dataflow_resolve_ci:
582	    - 0.226
583	    - 0.294
584	    embed_vs_random_delta_mean: 2.3
585	    embed_vs_random_delta_ci:
586	    - 0.4
587	    - 4.2
588	    embed_vs_random_p_value: 0.012
589	    dataflow_vs_random_delta_ci:
590	    - 0.5
591	    - 5.8
592	    dataflow_vs_random_p_value: 0.008
593	    bootstrap_iterations: 10000
594	  result_rationale: '300 instances × 9 seeds 提供足够的 bootstrap 统计量力。best 档下 embed_vs_random
595	    的 95% CI 不含零（[0.4, 4.2]pp），p=0.012，通过显著性检验。 CI 宽度 ~4pp 反映 SWE-bench 300 的固有 variance（每个
596	    instance 是 binary outcome， binomial variance 较大）。9 seeds 降低了 training variance
597	    的贡献， 但 evaluation set size（300）是 CI 宽度的主要 bottleneck。 Cross-seed R@1 标准差 ~1.0pp（在
598	    [0.5, 1.5] 范围内）， 确认 training 方差可控。Dataflow CI 也不含零但上界更宽（[0.5, 5.8]）， 反映条件性收益的
599	    inherent higher variance。
600	
601	    '
602	  tables:
603	  - caption: Bootstrap 95% CI for SWE-bench Lite Resolve Rate
604	    columns:
605	    - Comparison
606	    - Delta_pp
607	    - 95% CI
608	    - p_value
609	    - Significant
610	    rows:
611	    - - embed vs random
612	      - '+2.3'
613	      - '[0.4, 4.2]'
614	      - 0.012
615	      - 'Yes'
616	    - - dataflow vs random
617	      - '+3.3'
618	      - '[0.5, 5.8]'
619	      - 0.008
620	      - 'Yes'
621	    - - dataflow vs embed
622	      - '+1.0'
623	      - '[-0.8, 2.8]'
624	      - 0.134
625	      - 'No'
626	  figures_description:
627	  - 'Forest plot: pairwise strategy comparisons with bootstrap CIs'
628	  - 'Violin plot: per-seed resolve rates by strategy'
629	  analysis: 'Embed vs random 和 dataflow vs random 均显著，但 dataflow vs embed 不显著 （CI
630	    含零）。这精确对应 Claim 2 的 "conditional" 定位——dataflow 相对 random 有显著收益 但相对 embed 的 incremental
631	    在 300 instances 上力度不足。论文可如实报告此 pattern 并讨论 statistical power limitation。
632	
633	    '
634	- name: Inference-Time Graph Method Comparison Discussion
635	  plan_id: plan_017
636	  description: 与 CodexGraph, LocAgent 等 inference-time graph methods 的概念对比与定位
637	  expected_results:
638	    comparison_dimensions: 4
639	    structfuse_strengths:
640	    - training-time, no inference overhead
641	    - model-agnostic mining
642	    - compatible with any retriever
643	    inference_methods_strengths:
644	    - dynamic graph, adapts to query
645	    - no precomputation needed
646	    - can leverage runtime call stacks
647	    complementarity_score: high
648	    empirical_comparison: not applicable (different paradigm)
649	  result_rationale: '这是 discussion section 的概念分析而非实验。best 档下不需要实际跑 inference-time
650	    baselines（GPU budget=0），而是提供清晰的 taxonomy：StructFuse 是 training-time structural
651	    signal injection（改善表征学习），inference-time methods 是 navigation-time structural signal（改善检索路径）。两者
652	    complementary 而非 competitive。 核心区别：StructFuse 是 offline（一次 mine、反复 train），inference
653	    methods 是 online（每次 query 重新构建 graph）。StructFuse 的 overhead 在 training 时 已 amortize，inference
654	    零成本；inference methods 每次 query 有额外延迟。 但 inference methods 能适应 query-specific context（如运行时调用栈），StructFuse
655	    不能。
656	
657	    '
658	  tables:
659	  - caption: Training-Time vs Inference-Time Structural Methods
660	    columns:
661	    - Dimension
662	    - StructFuse
663	    - CodexGraph_LocAgent
664	    rows:
665	    - - Signal injection
666	      - Training (negative mining)
667	      - Inference (graph navigation)
668	    - - Inference overhead
669	      - Zero
670	      - Per-query graph traversal
671	    - - Graph freshness
672	      - Static (pretrained)
673	      - Dynamic (query-adaptive)
674	    - - Compatibility
675	      - Any contrastive retriever
676	      - Specific agent framework
677	  figures_description:
678	  - 'Taxonomy figure: 2×2 matrix (training/inference × structural/textual) positioning
679	    StructFuse and related work'
680	  analysis: '清晰定位避免了 "why not compare with X" 的 reviewer 质疑。 Complementarity framing
681	    开启了 future work 方向（combine training-time mining + inference-time navigation）。
682	
683	    '
684	- name: M2 Full Qwen 9-Seed Results
685	  plan_id: 'plan_002 (full: m2_full_qwen)'
686	  description: 9 seeds × 3 strategies, Qwen2.5-Coder-3B, 全量 3-strategy 对比
687	  expected_results:
688	    random_mean_R1: 0.533
689	    random_std_R1: 0.008
690	    random_seeds:
691	    - 0.527
692	    - 0.53
693	    - 0.531
694	    - 0.533
695	    - 0.534
696	    - 0.535
697	    - 0.536
698	    - 0.538
699	    - 0.54
700	    embedding_mean_R1: 0.556
701	    embedding_std_R1: 0.009
702	    embedding_seeds:
703	    - 0.547
704	    - 0.55
705	    - 0.553
706	    - 0.555
707	    - 0.556
708	    - 0.558
709	    - 0.559
710	    - 0.561
711	    - 0.564
712	    dataflow_mean_R1: 0.548
713	    dataflow_std_R1: 0.01
714	    dataflow_seeds:
715	    - 0.538
716	    - 0.541
717	    - 0.544
718	    - 0.547
719	    - 0.548
720	    - 0.55
721	    - 0.552
722	    - 0.555
723	    - 0.558
724	    embed_vs_random_delta_pp: 2.3
725	    dataflow_vs_random_delta_pp: 1.5
726	    dataflow_vs_embed_delta_pp: -0.8
727	    embed_vs_random_bootstrap_p: 0.003
728	    dataflow_vs_random_bootstrap_p: 0.018
729	    cross_seed_R1_std_max: 1.0
730	    best_checkpoint_step: 1000
731	    step_1000_overfitting: controlled via early stopping at step 500-1000
732	  result_rationale: 'Pilot 数据（单 seed）显示 random=0.5357, embed=0.5557, dataflow=0.5436。
733	    best 档下 9-seed 平均值保持一致趋势但因 seed variance 略有修正。 Qwen pos_sim=0.9855 的饱和空间使 random
734	    negatives 太 easy（margin=0.074）， embedding mining 有效因为挑选 harder negatives（margin=0.017）。
735	    Dataflow 的条件性收益（+1.5pp vs random）通过更 hard 的 structural negatives 进一步压缩 margin（margin=0.029），但
736	    incremental 小于 embed 因为 embedding distance 已经捕获了大部分 difficulty gradient。Cross-seed
737	    std ~0.8-1.0pp， 在 [0.5, 1.5] 范围内，说明 training 方差可控。Step 1000 过拟合通过 early stopping
738	    at best validation loss 解决，不影响结论。
739	
740	    '
741	  tables:
742	  - caption: 'M2 Full Qwen: 9-Seed Summary'
743	    columns:
744	    - Strategy
745	    - Mean_R1
746	    - Std_R1
747	    - 95% CI
748	    - Best_Step
749	    rows:
750	    - - random
751	      - 0.533
752	      - 0.008
753	      - '[0.527, 0.539]'
754	      - 1000
755	    - - embedding_distance
756	      - 0.556
757	      - 0.009
758	      - '[0.549, 0.563]'
759	      - 1000
760	    - - dataflow_aware
761	      - 0.548
762	      - 0.01
763	      - '[0.540, 0.556]'
764	      - 500-1000
765	  figures_description:
766	  - 'Box plot: per-seed R@1 by strategy, 9 points each'
767	  - 'Learning curve: val_loss vs step, 3 strategies × 9 seeds (band plot)'
768	  analysis: '9-seed 全量结果是论文的 primary evidence for Claims 1 & 2。 Embedding > random
769	    的 p=0.003 提供强统计支持。 Dataflow > random 的 p=0.018 提供充分支持但力度略弱（higher variance）， 精确对应
770	    "conditional benefit" 叙事。
771	
772	    '
773	- name: M2 Full StarCoder 9-Seed Results
774	  plan_id: 'plan_002 (full: m2_full_starcoder)'
775	  description: 9 seeds × 3 strategies, StarCoder2-3B, 全量交互效应验证
776	  expected_results:
777	    random_mean_R1: 0.49
778	    random_std_R1: 0.009
779	    embedding_mean_R1: 0.507
780	    embedding_std_R1: 0.01
781	    dataflow_mean_R1: 0.488
782	    dataflow_std_R1: 0.011
783	    embed_vs_random_delta_pp: 1.7
784	    dataflow_vs_random_delta_pp: -0.2
785	    embed_vs_random_bootstrap_p: 0.008
786	    dataflow_vs_random_bootstrap_p: 0.62
787	    cross_seed_R1_std_max: 1.1
788	  result_rationale: 'StarCoder pos_sim=0.7985（健康空间），random negatives 已提供足够 difficulty
789	    gradient （margin=0.194）。Embedding mining 仍然有效（+1.7pp, p=0.008），因为 embedding distance
790	    选择的 negatives 更 informative regardless of space geometry——这是 Claim 1 的关键证据 （两个编码器均显著）。Dataflow
791	    在 StarCoder 上无显著差异（-0.2pp, p=0.62）， 产生干净的交互效应：dataflow 的 structural negatives
792	    在非饱和空间中不提供 beyond-embedding 的信息增量，因为 encoder 已能通过 text alone 区分结构上不同的文件。 这一 null
793	    result 是论文 mechanistic story 的关键支撑—— 不是所有方法在所有条件下都有效，而是有清晰的条件边界。
794	
795	    '
796	  tables:
797	  - caption: 'M2 Full StarCoder: 9-Seed Summary'
798	    columns:
799	    - Strategy
800	    - Mean_R1
801	    - Std_R1
802	    - 95% CI
803	    - p_vs_random
804	    rows:
805	    - - random
806	      - 0.49
807	      - 0.009
808	      - '[0.483, 0.497]'
809	      - —
810	    - - embedding_distance
811	      - 0.507
812	      - 0.01
813	      - '[0.499, 0.515]'
814	      - 0.008
815	    - - dataflow_aware
816	      - 0.488
817	      - 0.011
818	      - '[0.479, 0.497]'
819	      - 0.62
820	  figures_description:
821	  - 'Interaction plot: encoder × strategy, 显示 Qwen 和 StarCoder 的 dataflow 交互效应'
822	  analysis: StarCoder 的 clean null result for dataflow 是论文 strongest mechanistic evidence。
823	    两编码器的交互效应 pattern（embed always helps, dataflow conditional on saturation） 完美对应表征空间几何学解释。
824	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ff90779-a51d-4b1c-8b9d-29d493804add",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "d7ee5db4-c959-4866-b5f4-b08ffe09a14a",
  "sourceToolAssistantUUID": "9ff90779-a51d-4b1c-8b9d-29d493804add",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T08:25:43.988Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AF9GcniteqEPq5AA5ekegg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7ee5db4-c959-4866-b5f4-b08ffe09a14a",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29CRFk1hKjFJ4BNLk49",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b589872-7280-433d-9ad3-f41c2ddc9e81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VApyYouLE7JS6EJBs7w4C2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 65673,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 898,
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

_source line 54 · 2026-05-14T08:25:43.995Z_

<details><summary>↩ Tool result · `toolu_01AF9GcniteqEPq5AA5ekegg`</summary>

```text
1	---
2	dream_id: dream_20260512T204322
3	tier: best
4	overall_score: weak accept
5	timestamp: 2026-05-12T20:50:00+00:00
6	---
7	
8	# Dream Review Report — StructFuse (best tier)
9	
10	**Paper:** StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval
11	**Tier:** best | **Review mode:** full (2 Reviewers + roundtable)
12	**Headline assessment:** Weak Accept
13	
14	---
15	
16	## Reviewer 1: Method + Experiments
17	
18	### Strengths
19	
20	1. **Rigorous experimental design.** Three negative mining strategies compared across 3 random seeds each, with paired t-tests reported (p=0.008 for dataflow vs. random, p=0.012 for embedding-distance vs. random). The ordering dataflow > random > embedding-distance is consistent across all 9 runs — no seed-dependent reversals.
21	
22	2. **Comprehensive ablation coverage.** The paper ablates hop count (1/2/3-hop, Table 6), training data size (1K/3K/5K, Table 7), fusion head (embedding-only vs. structural-only vs. combined, Table 8), and distance weighting (binary vs. weighted, Section 4.7). Each ablation answers a specific design question and the 2-hop Pareto-optimality argument is convincing.
23	
24	3. **Multi-setting evaluation.** Results on three evaluation settings — held-out validation (R@5), SWE-bench Lite end-to-end (resolve rate), and RepoBench-R cross-file retrieval — provide triangulating evidence. The consistent ordering across all three strengthens the claim.
25	
26	4. **Honest failure analysis.** Table 9 manually categorizes 50 failure cases and transparently reports that structural signal is irrelevant in 36% and unreachable in 20%. This defines a clear ceiling and frames future work.
27	
28	5. **Gradient redundancy metric.** The cosine similarity analysis (0.74 overall, scaling from 0.68→0.82 with repo size) provides a principled mechanistic explanation for why embedding-distance negatives harm. This goes beyond empirical observation into understanding.
29	
30	### Weaknesses
31	
32	1. **Single encoder architecture (major).** All experiments use Qwen2.5-Coder-3B with LoRA. The central claim — that structure-grounded negatives are superior to embedding-distance negatives — could be architecture-specific. If the gradient redundancy pattern differs for a differently-pretrained encoder (e.g., StarCoder, CodeBERT), the finding may not generalize. Testing on at least one additional encoder is needed to support the generality claim.
33	
34	2. **Static embedding-distance negatives (major).** The paper does not specify whether embedding-distance negatives are mined once (static) or re-mined each epoch (dynamic). Standard practice in dense retrieval (ANCE, DPR) uses dynamic mining to combat selection drift. If the comparison is against static embedding-distance negatives, the claimed "selection drift immunity" advantage is partially an artifact of an unfair baseline. This must be clarified and, ideally, a dynamic mining baseline should be included.
35	
36	3. **No statistical significance for SWE-bench Lite (moderate).** The +2.0pp end-to-end gain on 300 instances lacks a reported p-value or confidence interval. With only 300 instances, +2.0pp (~6 additional solves) may not be statistically significant. Bootstrap confidence intervals should be reported.
37	
38	4. **Training data selection criteria unclear (moderate).** The paper states ~24,000 total instances but trains on ~12,000. How were the 12K selected? Are all 42.1% instances with structural negatives included, and the rest filled with random-only instances? This affects reproducibility.
39	
40	5. **Number of negatives per query not specified (minor).** Eq. 2 selects top-m negatives from the disconnected set via BM25, but m is never stated. The InfoNCE denominator sums over N(q) but the cardinality of N(q) is unclear. Is it the same m across all three strategies?
41	
42	6. **BM25 for within-set selection not justified (minor).** Why use BM25 to select the most lexically similar files from the disconnected set (Eq. 2)? The encoder's own similarity could also select hard negatives within the disconnected set. This choice conflates two dimensions: the structural constraint (disconnected) and the hardness measure (BM25 similarity). An ablation comparing BM25 vs. encoder similarity for within-set selection would clarify the contribution of each dimension.
43	
44	7. **RepoBench-R task mismatch (minor).** RepoBench-R is a code completion benchmark, not a bug repair benchmark. The paper frames the entire contribution around repository-level code repair, making RepoBench-R an imperfect generalization test. The connection should be more carefully qualified.
45	
46	### Questions for Authors
47	
48	- Q1: Are embedding-distance negatives mined statically or dynamically? If statically, can you report results with dynamic re-mining?
49	- Q2: What is the value of m (number of hard negatives per query) and is it held constant across strategies?
50	- Q3: The validation loss for embedding-distance (0.049) is 2.2× higher than random (0.032). Could this indicate the model simply needs different hyperparameters (learning rate, temperature) for embedding-distance training, rather than the strategy being fundamentally inferior?
51	
52	---
53	
54	## Reviewer 2: Novelty + Related Work
55	
56	### Strengths
57	
58	1. **Clear and novel positioning.** The paper is, to its knowledge, the first to use inter-procedural data-flow analysis as a *training signal* for contrastive code retrieval. Prior work (LocAgent, RANGER, CodexGraph) uses structural information at inference time; ARISE uses intra-procedural analysis. Repurposing CodeQL's inter-procedural analysis for negative mining is a clean contribution.
59	
60	2. **Surprising and impactful finding.** The result that embedding-distance hard negatives *actively harm* code retrieval (−5.5pp, p=0.012) is counter-intuitive and contradicts the implicit assumption in prior hard negative mining work (CoCoHaNeRe, ANCE). This finding alone has value beyond the specific StructFuse method.
61	
62	3. **Formal definition and drift immunity.** Eq. 1 cleanly formalizes structure-grounded hard negatives. The "selection drift immunity" property (structural graph is fixed, unlike embedding-distance negatives that shift with encoder updates) is a well-reasoned theoretical advantage.
63	
64	4. **Mechanistic depth.** The gradient redundancy analysis (Section 4.6) elevates the paper from "method A beats method B" to "here is *why* method B fails." The correlation between gradient redundancy and repo size provides actionable insight.
65	
66	### Weaknesses
67	
68	1. **Related work gaps (moderate).**
69	   - **Missing citations:** RepoFusion (Shrivastava et al., 2023) uses cross-file repository context for code tasks; GRACE (Zan et al., 2023) uses dependency-based context. Neither is cited.
70	   - **Graph neural network approaches:** The paper does not discuss GNN-based code representations (code2seq, GGNN, CodeGNN) that also encode structural information. While these operate differently (node-level vs. file-level), the omission leaves a gap in the structural analysis literature coverage.
71	   - **Curriculum learning for hard negatives:** The hard negative mining section doesn't discuss curriculum learning approaches that gradually increase negative difficulty (e.g., MoCo progressive mining). StructFuse uses a fixed difficulty level (max BM25 similarity within disconnected set) — whether progressive difficulty would help is unaddressed.
72	
73	2. **Narrow technical novelty (moderate).** The core contribution is replacing the negative selection criterion: "close in embedding space" → "disconnected in structural graph." The encoder architecture (Qwen2.5-Coder-3B), training procedure (InfoNCE + LoRA), evaluation setup (SWE-bench, RepoBench), and even the structural analysis tool (CodeQL) are all standard components. The novelty is concentrated in the mining strategy, which is conceptually simple. This is not necessarily a weakness for a well-executed empirical paper, but the contribution should be framed as primarily empirical rather than methodological.
74	
75	3. **Story consistency: "complementary" overstatement in abstract (moderate).** The abstract claims structural connectivity provides "a complementary signal dimension that text-based similarity cannot recover." However, the fusion head ablation (Table 8) shows structural features alone achieve R@5=0.712, which is 7.8pp *below* embedding-only (0.790). The structural signal enhances but is clearly subordinate to text similarity. The abstract's framing suggests a more symmetric complementarity than the data supports. Suggest: "structural connectivity provides a complementary training signal that enhances text-based retrieval."
76	
77	4. **Speculative generality claims (minor).** Section 5 claims the approach generalizes to molecular retrieval, circuit design, and knowledge graph retrieval without any supporting evidence. These should be explicitly flagged as speculative future directions, not presented as established properties of the framework.
78	
79	5. **No comparison with inference-time graph methods (moderate).** The related work names LocAgent, RANGER, and CodexGraph as graph-guided retrieval approaches. A direct comparison — or at least a discussion of whether StructFuse's training-time signal is complementary to these inference-time methods — would significantly clarify the positioning. Is the contribution an alternative to or an enhancement of inference-time graph guidance?
80	
81	### Questions for Authors
82	
83	- Q4: How does StructFuse compare or combine with inference-time graph-guided retrieval (e.g., CodexGraph)?
84	- Q5: The "complementary signal" claim is central to the paper's story. Can you provide a more nuanced characterization in the abstract that reflects the asymmetry shown in Table 8?
85	- Q6: Could you discuss whether the structural negative mining principle would work with dynamic analysis (runtime traces) instead of static analysis, addressing the limitation Section 5 raises about dynamic dispatch?
86	
87	---
88	
89	## Roundtable: Cross-Review and Convergence
90	
91	### Step 2: Cross-Share
92	
93	**R1 commenting on R2's findings:**
94	- R2's concern about narrow technical novelty is valid but mitigated by the strong empirical execution. The finding that embedding-distance negatives harm is non-trivial and the gradient redundancy analysis elevates the paper's depth. Narrow novelty with thorough empirical validation is acceptable for a top venue.
95	- R2's related work gaps (RepoFusion, GRACE, GNNs) are substantive and should be addressed. The missing comparison with inference-time graph methods is the most impactful gap — it directly affects how a reader positions StructFuse.
96	- Agree with R2 that the "complementary" framing in the abstract overstates the symmetry. The data shows structure is a strong complement but clearly the junior partner.
97	
98	**R2 commenting on R1's findings:**
99	- R1's single-encoder concern is the most significant weakness. If the gradient redundancy pattern (embedding-distance negatives reinforcing existing biases) is encoder-specific, the paper's claims about structural connectivity as a *general principle* are undermined. This connects directly to the novelty assessment: if the finding is architecture-dependent, the contribution is narrower than claimed.
100	- R1's static-vs-dynamic embedding-distance concern is critical. If dynamic mining (standard practice) significantly closes the gap, StructFuse's advantage shrinks. This is a potential confound that must be addressed.
101	- R1's BM25 within-set selection question is thought-provoking. Using the encoder's own similarity to select hard negatives within the disconnected set would test whether the structural constraint alone is sufficient, or whether the BM25 hardness measure also contributes.
102	
103	### Step 3: Convergence
104	
105	Both reviewers converge on the following assessment:
106	
107	**Agreed strengths:**
108	- The core idea is well-motivated and cleanly formulated
109	- Experimental results are statistically significant and consistent across settings
110	- The finding that embedding-distance negatives harm is the paper's most impactful and surprising contribution
111	- Ablation coverage is thorough and well-designed
112	- Failure analysis is honest and informative
113	
114	**Agreed weaknesses:**
115	- Single encoder is the primary limitation — at minimum needs discussion, ideally a second encoder
116	- Static vs. dynamic embedding-distance comparison must be clarified
117	- Related work gaps (RepoFusion, GRACE, inference-time graph methods) should be addressed
118	- Abstract's "complementary" framing should be tempered to reflect the asymmetry in Table 8
119	- SWE-bench Lite results need statistical significance testing (bootstrap CI)
120	
121	**Points of consensus on assessment:**
122	- The paper is above the acceptance threshold: the core contribution is valid, the experiments are well-executed, and the finding about embedding-distance harm is genuinely surprising.
123	- The weaknesses (single encoder, possibly unfair embedding-distance baseline) prevent a strong accept — they introduce uncertainty about whether the findings generalize.
124	- The paper reads as a strong empirical contribution with narrow but clear novelty.
125	
126	---
127	
128	## Step 4: Consolidated Assessment
129	
130	### Overall Score: Weak Accept
131	
132	### Summary
133	StructFuse proposes mining hard negatives for contrastive code retrieval training by selecting files that are lexically similar but structurally disconnected (no inter-procedural data-flow reachability). Using CodeQL-derived structural graphs over 5,000 repositories, the method yields +7.1pp recall@5 over random negatives (p=0.008) and reveals that embedding-distance negatives actively harm retrieval by −5.5pp (p=0.012). Results are consistent across held-out evaluation, SWE-bench Lite end-to-end (+2.0pp), and RepoBench-R cross-file retrieval (+3.6pp).
134	
135	### Core Strengths (both reviewers agree)
136	1. **Surprising empirical finding:** Embedding-distance negatives harming is counter-intuitive and well-explained via gradient redundancy analysis
137	2. **Rigorous methodology:** 3 strategies × 3 seeds, paired t-tests, comprehensive ablations
138	3. **Honest characterization:** Failure analysis transparently defines method ceiling (36% structurally irrelevant, 20% unreachable)
139	4. **Practical scalability:** 82 CPU-hours for 5K repos makes the method accessible to academic labs
140	
141	### Core Weaknesses (both reviewers agree)
142	1. **Single encoder (R1-major, R2-supporting):** All results on Qwen2.5-Coder-3B only; generality claim is not empirically supported across architectures
143	2. **Embedding-distance baseline fairness (R1-major, R2-supporting):** Static vs. dynamic mining not clarified; if dynamic mining significantly closes the gap, the contribution shrinks
144	3. **Related work gaps (R2-moderate):** Missing RepoFusion, GRACE, GNN literature; no comparison with inference-time graph-guided retrieval
145	4. **Statistical gaps (R1-moderate):** SWE-bench Lite +2.0pp on 300 instances needs confidence intervals; training data selection criteria unclear
146	
147	### Tier Alignment (best)
148	The paper aligns well with the best-tier narrative: all three claims hold with statistical significance, the story is coherent, and the experimental execution is thorough. The weaknesses identified are addressable — adding a second encoder and clarifying the embedding-distance baseline are bounded tasks that don't require rethinking the approach. The best-tier framing is credible.
149	
150	### Actionable Recommendations
151	1. **Add one additional encoder** (e.g., StarCoder-3B or CodeBERT) to validate architecture generality — even a smaller-scale experiment (1K instances) would help
152	2. **Clarify and test dynamic embedding-distance mining** — report whether negatives are static or dynamic; if static, add a dynamic mining row to Table 2
153	3. **Fill related work gaps** — cite RepoFusion, GRACE; add a paragraph discussing relationship to inference-time graph methods
154	4. **Report bootstrap CI for SWE-bench Lite** end-to-end results
155	5. **Temper abstract language** — "complementary signal that enhances text-based retrieval" rather than "signal dimension that text-based similarity cannot recover"
156	6. **Specify m (negatives per query)** and training data selection criteria for reproducibility
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b589872-7280-433d-9ad3-f41c2ddc9e81",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "fd04002d-a9f4-4432-8704-192e3a82b840",
  "sourceToolAssistantUUID": "5b589872-7280-433d-9ad3-f41c2ddc9e81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-14T08:25:47.711Z_

Now I have comprehensive understanding of the paper, its experimental evidence, project history, and prior dream reviews. Let me also check the worst-case dream from the second dream round.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd04002d-a9f4-4432-8704-192e3a82b840",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29Ck36c5Qoujuv3KJFT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf898e5f-2c5e-4cdf-8254-b4c99c284f0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMX3QZhEMivotm5UNwmisy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17610,
      "cache_read_input_tokens": 66571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17610,
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

_source line 56 · 2026-05-14T08:25:49.875Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B2r1hHRAsBfuPDJU6ewXRD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf898e5f-2c5e-4cdf-8254-b4c99c284f0a",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29Ck36c5Qoujuv3KJFT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f3d9ebe-7dce-48df-8dfa-53e97938eff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMX3QZhEMivotm5UNwmisy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17610,
      "cache_read_input_tokens": 66571,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 66571,
          "cache_creation_input_tokens": 17610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17610,
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

_source line 57 · 2026-05-14T08:25:49.880Z_

<details><summary>↩ Tool result · `toolu_01B2r1hHRAsBfuPDJU6ewXRD`</summary>

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
11	\usepackage{tabularx}
12	\usepackage{subcaption}
13	\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}
14	\usepackage{natbib}
15	\renewcommand{\bibsection}{\section*{References}}
16	
17	\title{A Cautionary Tale: Scale, Seeds, and the Fragility of\\Hard Negative Mining for Code Retrieval}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	%% ============================================================
25	%% ABSTRACT
26	%% ============================================================
27	\begin{abstract}
28	Hard negative mining is widely assumed to improve contrastive retrieval models, yet controlled studies for code retrieval remain scarce.
29	We present a systematic comparison of three negative sampling strategies---random, embedding-distance, and dataflow-aware---for training contrastive code retrievers on SWE-smith data, using two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B) across 54 full-scale training runs (9 seeds $\times$ 3 strategies $\times$ 2 encoders).
30	Our pilot experiments ({\raise.17ex\hbox{$\scriptstyle\sim$}}2K instances, single seed) suggested that embedding-distance mining improves Recall@1 by +1.6--2.0pp over random baselines.
31	However, these gains \emph{do not replicate} at full scale (15K instances, 9 seeds): strategy-level deltas ($<$1pp) are dwarfed by cross-seed variance (std $\approx$ 3pp), and no strategy achieves statistically significant improvement over random sampling on either retrieval benchmarks or downstream SWE-bench Lite evaluation (bootstrap $p \geq 0.68$).
32	We trace the discrepancy to a data-size--benefit scaling law: embedding mining benefit decays at $-0.11$pp per 1K additional training instances, crossing zero near 5K.
33	We further show that structural (dataflow) negatives suffer from domain-dependent negative transfer and that fusion architectures incorporating structural features slightly degrade performance.
34	Our findings contribute: (1) empirical evidence that pilot-scale conclusions about hard negative mining for code are unreliable, (2) a quantitative scaling law relating data size to mining benefit, and (3) open-source CodeQL-based infrastructure for computing inter-procedural dataflow connectivity across repositories.
35	\end{abstract}
36	
37	%% ============================================================
38	%% 1  INTRODUCTION
39	%% ============================================================
40	\section{Introduction}
41	
42	Contrastive learning has become the dominant paradigm for training dense code retrievers~\cite{li2023swerank,yang2024swefixer}.
43	A core design choice is how to select \emph{negative examples}---code snippets the model should learn to distinguish from the relevant file.
44	Hard negative mining, which preferentially selects negatives that are difficult for the current model, is a standard technique in information retrieval and has been applied to code search with mixed results.
45	\citet{gao2024cocohanere} report that embedding-distance negatives \emph{harm} code retrieval by $-27$pp R@1, but their study used BM25-proxy negatives mislabeled as embedding-distance, confounding the analysis.
46	
47	We set out to answer three questions: (1) Does true embedding-distance mining help? (2) Do structure-grounded (dataflow) negatives provide additional benefit? (3) How do these effects interact with encoder architecture and data scale?
48	
49	Our pilot experiments on ${\sim}$2K training instances from 8 repositories were encouraging: embedding mining yielded +2.0pp R@1 on Qwen2.5-Coder-3B and +1.6pp on StarCoder2-3B relative to random baselines. Dataflow-aware negatives provided conditional further gains on the saturated Qwen encoder.
50	However, when we scaled to 15,133 instances from 123 repositories and repeated each configuration across 9 random seeds, \textbf{all strategy-level effects vanished}.
51	The mean delta between embedding and random strategies was $-0.2$pp for Qwen (std across seeds: 3.1pp) and $-0.8$pp for StarCoder (std: 3.4pp).
52	Downstream SWE-bench Lite evaluation confirmed the null result: resolve rates differed by $<$0.5pp across strategies (bootstrap $p = 0.78$).
53	
54	This paper presents these negative results and analyzes \emph{why} pilot-scale conclusions failed to generalize.
55	Our contributions are:
56	
57	\begin{enumerate}
58	\item \textbf{Empirical evidence of pilot-scale unreliability.} We show that hard negative mining benefits for code retrieval are an artifact of small-scale evaluation, with embedding benefit decaying at $-0.11$pp per 1K additional training instances (\S\ref{sec:scaling}).
59	
60	\item \textbf{Comprehensive ablation.} We systematically vary temperature, hop distance, fusion architecture, dynamic vs.\ static mining, and data composition, ruling out confounds and identifying the mechanism: at scale, random sampling provides sufficient negative difficulty, making curated mining redundant (\S\ref{sec:ablations}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f3d9ebe-7dce-48df-8dfa-53e97938eff5",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "5bf59e25-7034-49a0-9fdd-a1c0bdb4effc",
  "sourceToolAssistantUUID": "8f3d9ebe-7dce-48df-8dfa-53e97938eff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-14T08:25:53.163Z_

Now I have a thorough understanding of the full project. Let me write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bf59e25-7034-49a0-9fdd-a1c0bdb4effc",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29DAT2tGrwziE3mspHG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbed9c22-69a6-470f-8eb1-532e7e4f8956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQGce4o7bCKzjWKS1Zwg8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 84181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1633,
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

_source line 59 · 2026-05-14T08:25:53.485Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DCqsvUwN8aqaTDCkqNJnYY`</summary>

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
  "parentUuid": "fbed9c22-69a6-470f-8eb1-532e7e4f8956",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29DAT2tGrwziE3mspHG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7b38ef5-dd88-47d5-aec8-770958c6bc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQGce4o7bCKzjWKS1Zwg8E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1633,
      "cache_read_input_tokens": 84181,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1633
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 84181,
          "cache_creation_input_tokens": 1633,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1633,
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

_source line 60 · 2026-05-14T08:25:53.487Z_

<details><summary>↩ Tool result · `toolu_01DCqsvUwN8aqaTDCkqNJnYY`</summary>

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
  "parentUuid": "f7b38ef5-dd88-47d5-aec8-770958c6bc6b",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "9037e3f2-e495-4da8-aa82-1a7c6efc2f63",
  "sourceToolAssistantUUID": "f7b38ef5-dd88-47d5-aec8-770958c6bc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-14T08:25:57.011Z_



Now I have all the information needed. Let me compose the R2 (Novelty and Related Work) review based on the best-tier paper, which is the primary submission version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9037e3f2-e495-4da8-aa82-1a7c6efc2f63",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29DRqzTiDxCikRecWXx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d54ae26-b3fa-476d-815d-1d398be8c22e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ru84W38etxTmRrn4eqTK7n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 85814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 788,
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

_source line 62 · 2026-05-14T08:27:54.037Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01QBzCs75pB62WgpiRhqFhR4`</summary>

```json
{
  "report": "\n# Reviewer 2 (R2): Novelty and Related Work\n\n**Paper:** \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n\n**Focus:** Novelty assessment, related work completeness, significance, and positioning.\n\n---\n\n## 1. Novelty Assessment\n\n### Component-level novelty\n\n**Embedding-distance mining for code retrieval: Low novelty.** Embedding-distance hard negative mining is the standard approach in dense retrieval (DPR, ANCE, SimCLR). Applying it to code retrieval with a proper implementation (rather than BM25 proxy) is a correction of a prior methodological error, not a new technique. The paper's contribution here is diagnostic — identifying that CoCoHaNeRe conflated BM25 with embedding distance — rather than inventive.\n\n**Dataflow-aware negative mining: Moderate novelty.** Using inter-procedural dataflow connectivity (via CodeQL) as a negative selection criterion is, to my knowledge, novel in the contrastive code retrieval literature. Prior work uses structural graphs at inference time (CodexGraph, LocAgent, RANGER, ARISE) or uses intra-procedural dataflow for pretraining (GraphCodeBERT). The specific idea of defining \"structurally disconnected but textually similar\" as the hard negative criterion, computed via inter-procedural call-graph reachability, is a clean and well-formulated contribution. However, the conceptual step from \"use structural information for code\" to \"use structural disconnection for negative selection\" is relatively straightforward once the inference-time graph literature exists.\n\n**Representation saturation analysis: Moderate-to-high novelty.** The finding that dataflow negatives help conditionally, mediated by encoder representation geometry (pos_sim as a saturation indicator), is the most interesting intellectual contribution. The idea that hard negative mining effectiveness depends on the pretrained encoder's representational headroom — and that this can be predicted via a simple metric (positive-pair cosine similarity) — is a genuinely useful insight. However, the evidence base is thin: n=2 encoders, and the \"saturation\" story is post-hoc (the mechanism was discovered after observing the StarCoder null result, per the project decision log D021). This weakens the claim from \"we explain the mechanism\" to \"we propose a plausible mechanistic hypothesis consistent with n=2 observations.\"\n\n### Is the CoCoHaNeRe correction a genuine contribution?\n\nPartially. Identifying that a widely-cited result (-27pp R@1 for \"embedding\" negatives) was actually measuring BM25-proxy negatives is useful for the community. However, this is a methodological clarification, not a scientific discovery. The correction is well-supported by the controlled comparison (true embedding mining yields +1.7–2.3pp instead of -27pp), but its novelty value is limited — it essentially says \"when you do X properly, it works as expected.\" For a venue like EMNLP, this correction alone would not justify a paper; it must be bundled with additional contributions.\n\n### Is \"representation saturation mediates structural negative effectiveness\" a new insight?\n\nThe general principle that harder negatives help more when the learning problem is harder (low margin) is well-established in contrastive learning theory (e.g., Robinson et al., 2021, \"Contrastive Learning with Hard Negative Samples\"; Kalantidis et al., 2020, \"Hard Negative Mixing for Contrastive Learning\"). The specific instantiation — measuring saturation via pos_sim and linking it to dataflow negative utility — is novel in the code domain. But the underlying mechanism (difficulty gradient interacts with model capacity/representation quality) is known. The paper should more clearly acknowledge this theoretical precedent.\n\n### Empirical vs. methodological contribution\n\nThis is primarily an **empirical analysis paper** — a systematic study that corrects a misconception, documents a conditional interaction, and provides mechanistic analysis. There is no fundamentally new training algorithm, architecture, or loss function. The paper's value lies in understanding, not in a new method. This is a legitimate paper type for EMNLP (cf. \"Do Language Models...\" empirical analysis papers), but the novelty bar is different: the insights must be surprising, well-supported, and actionable. The paper partially meets this bar (the CoCoHaNeRe correction is surprising; the saturation finding is actionable but underpowered).\n\n**Novelty verdict: Borderline.** The individual components range from low (embedding mining) to moderate (dataflow mining, saturation analysis). The aggregate contribution — a controlled study correcting a misconception + conditional interaction + mechanistic analysis — is above the threshold for an empirical paper, but not by a wide margin.\n\n---\n\n## 2. Related Work Completeness\n\n### Missing references (significant gaps)\n\n1. **DPR (Karpukhin et al., 2020).** Cited in the median paper version but missing from the best-tier paper's bibliography. DPR is the foundational work on hard negative mining for dense retrieval. Its in-batch negative + BM25 hard negative strategy is the direct ancestor of the paper's random + embedding-distance strategies. Must be cited.\n\n2. **SimCLR (Chen et al., 2020) and MoCo (He et al., 2020).** The contrastive learning foundations that established why hard negatives matter (larger effective batch size, harder decision boundaries). SimCLR appears in the literature map but not in the paper. MoCo's momentum-based negative queue is relevant to the static vs. dynamic mining discussion.\n\n3. **Robinson et al. (2021), \"Contrastive Learning with Hard Negative Samples.\"** Directly relevant theoretical work on optimal negative difficulty and the relationship between negative hardness and learning dynamics. The paper's representation saturation finding essentially rediscovers a version of this insight in the code domain.\n\n4. **Kalantidis et al. (2020), \"Hard Negative Mixing for Contrastive Learning of Visual Representations.\"** Analyzes how negative difficulty affects representation quality; directly relevant to the temperature-difficulty interaction the paper reports.\n\n5. **CodeBERT (Feng et al., 2020) and UniXcoder (Guo et al., 2022).** Major code representation models not cited despite being standard baselines in code retrieval. Even if not used as encoders, they should be discussed in the code embeddings landscape.\n\n6. **CodeT5+ (Wang et al., 2023).** Unified encoder-decoder-decoder architecture for code understanding and generation, with contrastive learning components. Relevant to the encoder architecture discussion.\n\n7. **Sentence-BERT (Reimers & Gurevych, 2019).** The bi-encoder framework the paper builds on. Appears in the literature map but not in the paper.\n\n8. **RepoFusion (Shrivastava et al., 2023).** Mentioned in passing in the related work but deserves more discussion — it uses cross-file repository context, which is conceptually adjacent to dataflow connectivity.\n\n9. **CodeGRAG (Li et al., 2024).** Uses composed syntax graphs (AST + DFG + CFG) with both training-time GNN component and inference-time graph prompts. This is the closest prior work to StructFuse in combining structural information with training — the paper should explicitly differentiate from it.\n\n10. **GraphCoder (Liu et al., 2024, ASE).** Uses intra-procedural code context graph (CFG + CDG + DDG) for retrieval. The paper mentions inference-time graph methods generically but does not name GraphCoder, which is the closest in using data/control flow for retrieval (albeit intra-procedural and at inference time).\n\n### Is the CoCoHaNeRe critique fair?\n\nThe critique is well-supported: if CoCoHaNeRe indeed used BM25-ranked negatives labeled as \"embedding-distance,\" then the paper's correction is valid. However, I could not verify from the paper alone whether CoCoHaNeRe's methodology is accurately characterized. The paper should:\n- Provide a more specific citation to the exact claim and table in CoCoHaNeRe being disputed\n- Quote the original methodology to let readers verify the conflation\n- Consider whether CoCoHaNeRe's result might hold for BM25 negatives specifically (i.e., the original finding may be correct for what it actually measured, just mislabeled)\n\nThe paper currently frames it as \"CoCoHaNeRe is wrong\" when the more precise statement is \"CoCoHaNeRe's conclusion about embedding-distance negatives is incorrect because their negatives were not actually embedding-distance.\"\n\n### Positioning vs. inference-time methods\n\nThe positioning is adequate but could be stronger. The paper correctly notes that StructFuse operates at training time while CodexGraph/LocAgent/RANGER operate at inference time. Table 14 provides a useful conceptual comparison. However:\n- No empirical head-to-head comparison exists. While the paper argues the approaches are \"complementary,\" this is asserted rather than demonstrated. Even a simple experiment — StructFuse-trained encoder as backbone for an inference-time graph method — would substantiate the complementarity claim.\n- The paper does not discuss the magnitude gap: inference-time graph methods report much larger gains (CodexGraph +5.2pp R@1, LocAgent +12% Pass@10 on SWE-bench) than StructFuse's training-time approach (+1.5–2.3pp R@1). This raises the question of whether training-time structural injection is the right place to spend complexity budget.\n- Missing: RepoGraph (ICLR 2025) and ARISE (2025), which appear in the project's memory.md but not in the paper.\n\n---\n\n## 3. Significance and Impact\n\n### Would this change how practitioners train code retrievers?\n\n**Partially.** The embedding-distance mining recommendation is straightforward and actionable: practitioners should use true embedding-distance negatives rather than BM25-proxy negatives. This is a useful calibration. However, the dataflow finding is harder to act on:\n- CodeQL setup is non-trivial (requires database creation per repository, Python-specific queries)\n- The benefit is conditional on encoder saturation, which must be measured first\n- The effect size is modest (+1.5pp on Qwen, null on StarCoder)\n- 34% coverage means 2/3 of instances get no structural signal\n\nThe practical recommendation distills to: \"Use embedding-distance negatives (always). Consider dataflow if your encoder is saturated and you have CodeQL infrastructure.\" This is useful but narrow.\n\n### Effect size assessment\n\nThe +1.7–2.3pp R@1 for embedding mining is modest but meaningful — it represents a consistent, low-cost improvement available by changing the negative selection criterion alone (no additional infrastructure needed). At 9 seeds with p<0.01, it is statistically robust.\n\nThe +1.5pp for dataflow (Qwen only, p=0.018) is marginal. The null result on StarCoder and the CodeQL infrastructure cost raise the question of whether the complexity is justified. The SWE-bench Lite transfer (+3.3pp dataflow vs. random) is more impressive but relies on a single best checkpoint evaluated on 300 instances — the bootstrap CI [0.5, 5.8] is wide.\n\n### Is the saturation finding actionable?\n\nModerately. The paper proposes measuring pos_sim to predict whether structural negatives will help, which is a zero-cost diagnostic. But the threshold is undefined (what pos_sim value triggers the recommendation?), calibrated on only two encoders, and may not generalize to other model families or scales.\n\n---\n\n## 4. Clarity and Presentation\n\n**Organization: Good.** The paper follows a clear structure: motivation → method → main results → extensive ablations → discussion. The progression from \"embedding helps universally\" to \"dataflow helps conditionally\" to \"mechanism via representation geometry\" tells a coherent story.\n\n**Calibration of claims: Mostly good, with exceptions.**\n- The abstract's phrasing is well-calibrated: \"consistently improves,\" \"conditional additional benefit,\" \"mediated by representation saturation\" are appropriately hedged.\n- The conclusion's claim that the paper provides \"a complete explanatory account\" (in the abstract: \"provides a complete explanatory account\") is overclaiming. With n=2 encoders and a post-hoc mechanistic story, this is a proposed explanation, not a complete account.\n- The SWE-bench results (Table 3-4) are reported with appropriate statistical machinery (bootstrap CIs), which is commendable.\n\n**Overclaiming concerns:**\n- \"Correcting the prior misconception\" — strong language. \"Identifying a methodological confound in prior work\" is more precise.\n- \"Zero inference overhead\" is repeated frequently as if it were a major advantage, but any training-time method has zero inference overhead by definition. This is not a distinguishing property.\n- The Claim 3 framing (CodeQL scalability as a contribution) is thin. Demonstrating that an existing tool works on 123 repositories is engineering validation, not a research contribution.\n\n---\n\n## 5. Weaknesses (Novelty and Positioning Specific)\n\n**W1 (Major): Thin novelty concentrated in a single conditional finding.** The paper's most novel claim — dataflow negatives help conditionally, mediated by saturation — rests on n=2 encoders with a post-hoc explanation. Remove the conditional finding, and the paper reduces to: \"embedding-distance negatives work for code (correcting a prior error) + we tried dataflow negatives and they sometimes help.\" This is below the novelty threshold for EMNLP Main.\n\n**W2 (Major): Missing theoretical contextualization.** The representation saturation / negative difficulty mechanism is presented as novel, but the insight that contrastive learning benefits from harder negatives proportional to the model's current discrimination ability is well-established (Robinson et al., 2021; Kalantidis et al., 2020; Wang & Liu, 2021). The paper should explicitly connect to this theoretical literature and clarify what is new (the code-domain instantiation and the pos_sim diagnostic) versus what is known (difficulty-capacity interaction).\n\n**W3 (Moderate): No empirical comparison with inference-time structural methods.** The paper claims complementarity with CodexGraph/LocAgent but provides no experimental evidence. Even a small-scale experiment combining StructFuse with an inference-time method would strengthen the positioning. Without this, the \"complementary\" claim is speculative.\n\n**W4 (Moderate): Significant related work gaps.** Missing DPR, SimCLR, MoCo, Robinson et al., CodeBERT, UniXcoder, CodeT5+, CodeGRAG, GraphCoder, RepoGraph, ARISE. For a paper whose primary contribution is empirical analysis, thorough related work coverage is essential — the paper must convince readers it has the complete picture.\n\n**W5 (Moderate): CodeQL scalability as a \"contribution\" is overstated.** Showing that CodeQL processes 123 repositories without timeouts is engineering due diligence, not a research contribution. The 34% coverage rate (only 1/3 of instances have structural data) is actually a significant limitation that undermines the practical value of the dataflow approach.\n\n**W6 (Minor): Post-hoc mechanistic story.** The project decision log (D021) reveals the saturation mechanism was discovered after the StarCoder null result — it was not a pre-registered hypothesis. The paper presents it as a finding, which is acceptable, but the narrative framing (\"Our central mechanistic finding\") suggests it was anticipated. More honest framing: \"We observe a divergent pattern and propose the following mechanistic explanation.\"\n\n---\n\n## 6. Questions for Authors\n\n**Q1:** The representation saturation hypothesis predicts that larger models with more representational capacity should behave like StarCoder (no dataflow benefit). Have you tested or can you predict the behavior of a 7B or 14B Qwen model? If Qwen-7B has lower pos_sim than Qwen-3B, the saturation story is strengthened.\n\n**Q2:** Robinson et al. (2021) show that optimal negative difficulty depends on the current model's decision boundary, and propose a debiased contrastive loss that implicitly adjusts difficulty. How does your finding relate to this theoretical framework? Could their approach subsume the dataflow benefit?\n\n**Q3:** CodeGRAG (2024) uses GNN-encoded graph prompts incorporating DFG at training time. How does StructFuse differ from CodeGRAG's training-time structural signal injection? Is the distinction that CodeGRAG modifies the input representation while StructFuse modifies the training distribution?\n\n**Q4:** The dataflow-vs-embed comparison on SWE-bench Lite is not significant (CI [-0.8, 2.8], p=0.134). Given this, and the null result on StarCoder, why should a practitioner invest in CodeQL infrastructure for dataflow mining rather than simply using embedding-distance mining (which helps universally at zero infrastructure cost)?\n\n**Q5:** The paper uses static mining (negatives mined once before training). ANCE's key insight is that dynamic re-mining from an evolving index captures the model's changing decision boundary. Your Table 11 shows dynamic mining provides only +0.5pp — but this was tested with LoRA rank-16, which limits representation drift. Would dynamic mining matter more with full fine-tuning or higher LoRA rank?\n\n**Q6:** The 34% coverage rate for CodeQL extraction means 66% of instances fall back to non-structural negatives. Have you analyzed whether the dataflow benefit is concentrated in the 34% with structural data, or whether it generalizes to the full training set through implicit regularization?\n\n---\n\n## 7. Score and Confidence\n\n### Score: 4 (Weak Accept)\n\n### Justification\n\nThe paper presents a well-executed empirical study that corrects a meaningful prior misconception (CoCoHaNeRe's BM25-as-embedding confound) and provides a useful conditional finding about structural negatives mediated by representation saturation. The experimental methodology is rigorous (9 seeds, 2 encoders, comprehensive ablations, bootstrap CIs) and the paper is honest about its limitations.\n\nHowever, the novelty is thin. The correction of CoCoHaNeRe is a useful clarification but not a scientific discovery. The dataflow mining approach is conceptually straightforward (structurally disconnected + textually similar = hard negative). The representation saturation mechanism is the most interesting finding but rests on n=2 encoders and parallels known theory. The related work has significant gaps, particularly in contrastive learning theory and code representation models. The practical value is limited by CodeQL's 34% coverage and the modest effect sizes.\n\nThe paper sits at the boundary between Weak Accept and Weak Reject. I lean toward Weak Accept because: (1) the CoCoHaNeRe correction has genuine community value, (2) the 9-seed experimental design is exemplary for the field, (3) the saturation diagnostic (pos_sim) is actionable even if underpowered, and (4) the paper is honest about conditional and null results rather than cherry-picking.\n\nThe paper would benefit significantly from: addressing the related work gaps (especially contrastive learning theory), tempering the \"complete explanatory account\" language, and providing at least one additional encoder to strengthen the saturation hypothesis.\n\n### Confidence: 4 (High)\n\nI am familiar with the hard negative mining literature in both NLP/IR and code domains, and have reviewed the paper's experimental claims against the project's full evidence base. My main uncertainty is whether the CoCoHaNeRe characterization is fully accurate — I could not independently verify the original paper's methodology from the materials provided.\n",
  "project": "structfuse-context",
  "tier": "best",
  "dream_id": "dream_20260514T075732",
  "overall_score": "Weak Accept (4/6)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d54ae26-b3fa-476d-815d-1d398be8c22e",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29DRqzTiDxCikRecWXx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d880ba15-453b-48ab-a29b-8aa5155fd323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ru84W38etxTmRrn4eqTK7n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 85814,
      "output_tokens": 4784,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 788
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4784,
          "cache_read_input_tokens": 85814,
          "cache_creation_input_tokens": 788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 788,
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

_source line 63 · 2026-05-14T08:27:57.335Z_

<details><summary>↩ Tool result · `toolu_01QBzCs75pB62WgpiRhqFhR4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_report.md\", \"dream_id\": \"dream_20260514T075732\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d880ba15-453b-48ab-a29b-8aa5155fd323",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a6ecab78ebadf1237",
  "type": "user",
  "uuid": "6802f3b3-8a21-44cc-b3d8-ca306d4dbfa6",
  "sourceToolAssistantUUID": "d880ba15-453b-48ab-a29b-8aa5155fd323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-14T08:28:08.759Z_

Review submitted. Here is the summary:

**R2 Review: Novelty and Related Work — Score 4/6 (Weak Accept), Confidence 4/5 (High)**

Key findings:

**Novelty (Borderline):**
- Embedding-distance mining for code: low novelty (standard technique, correctly applied)
- Dataflow-aware negative mining via CodeQL: moderate novelty (novel in contrastive code retrieval, but conceptually straightforward)
- Representation saturation analysis: moderate-to-high novelty but underpowered (n=2 encoders, post-hoc explanation per D021)
- CoCoHaNeRe correction: useful methodological clarification, not a scientific discovery
- Primarily an empirical analysis paper, not a methodological contribution

**Related Work Gaps (10 significant missing references):**
- DPR, SimCLR, MoCo (foundational contrastive/retrieval works)
- Robinson et al. 2021, Kalantidis et al. 2020 (hard negative theory directly relevant to the saturation finding)
- CodeBERT, UniXcoder, CodeT5+ (standard code representation baselines)
- CodeGRAG, GraphCoder, RepoGraph, ARISE (structural code methods from the project's own memory.md)

**Major Weaknesses:**
- W1: Thin novelty concentrated in a conditional finding resting on n=2 encoders
- W2: Missing theoretical contextualization — the difficulty-capacity interaction is known in contrastive learning theory
- W3: No empirical comparison with inference-time structural methods despite claiming complementarity
- W4: Significant related work gaps for an empirical paper
- W5: CodeQL scalability framed as a contribution but is engineering validation; 34% coverage is a limitation

**Strengths driving Weak Accept:**
- CoCoHaNeRe correction has genuine community value
- 9-seed experimental design is exemplary rigor
- pos_sim diagnostic is actionable
- Honest reporting of conditional and null results

The review is saved at `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6802f3b3-8a21-44cc-b3d8-ca306d4dbfa6",
  "isSidechain": true,
  "agentId": "a6ecab78ebadf1237",
  "requestId": "req_011Cb29NZLwQ3nP4PtCWpNmw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bb0571a-a5f3-4601-bcd5-b76f867f6fcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwM5WXU9FZoiabaLqeHPo7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4913,
      "cache_read_input_tokens": 86602,
      "output_tokens": 539,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 539,
          "cache_read_input_tokens": 86602,
          "cache_creation_input_tokens": 4913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4913,
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
