# Research conversation: You are **Reviewer 2 (R2)** in a peer review of a machine learning paper. Your assigned focus areas are **Novelty/Signif

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a81897433be7dac28.jsonl`
- **Structured JSON:** [`18bdc4c36912c70e880d.json`](../../sessions/18/18bdc4c36912c70e880d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-14T17:00:03.902Z_

You are **Reviewer 2 (R2)** in a peer review of a machine learning paper. Your assigned focus areas are **Novelty/Significance** and **Related Work/Positioning**. You are reviewing for a top ML venue (acceptance rate ~25%), using a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept.

## Paper Summary

**Title:** "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"

**Core idea:** Systematic comparison of 4 negative mining strategies for contrastive code retrieval: random, BM25, true embedding-distance, and structure-grounded (dataflow via CodeQL inter-procedural call graphs). Trained on two 3B decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with LoRA rank 16, 9 seeds each, InfoNCE loss.

**Three claims:**
1. True embedding-distance mining *consistently improves* retrieval (+2.0pp Qwen, +1.5pp StarCoder R@1), correcting CoCoHaNeRe's misconception that embedding negatives harm code retrieval (CoCoHaNeRe used BM25 proxy mislabeled as embedding-distance).
2. Structure-grounded (dataflow) negatives provide *conditional* benefit: +1.0pp on Qwen (saturated representation, pos_sim=0.9855) but -0.2pp on StarCoder (healthy separation, pos_sim=0.7985). Stratified analysis shows true per-instance effect is +2.8pp on instances with structural data (34%), diluted by 66% fallback.
3. Mechanistic explanation via representation geometry: negative difficulty quartile analysis shows monotonic improvement scaling (Q4 hardest: +3.2pp embedding delta vs Q1 easiest: +0.8pp).

**Related work covered in paper:**
- **Code Retrieval for SE:** SweRank, SWE-Fixer — contrastive retrievers trained on issue-file pairs from GitHub, rely on text-based similarity alone
- **Hard Negative Mining:** ANCE (asynchronous index refresh), curriculum-based approaches, CoCoHaNeRe (reports embedding negatives harm code search)
- **Graph-Based Code Understanding:** CodexGraph (code graph DB for LLM navigation), LocAgent (repo structure trees), RANGER (call graphs), ARISE (intra-procedural dataflow), GraphCodeBERT (dataflow in pretraining). All operate at inference time; StructFuse is first to inject structural signal at training time via negative mining. Table 16 provides systematic comparison.

**Key contributions:**
1. Correcting CoCoHaNeRe misconception (BM25 proxy artifact)
2. Introducing structure-grounded negatives via inter-procedural dataflow
3. Representation geometry analysis explaining encoder-strategy interaction
4. Practical recommendations for practitioners

**Paper structure:** 11 pages, 16 tables, multiple figures. Sections: Introduction, Related Work, Method, Experiments, Discussion, Conclusion.

## Your Task

Provide a detailed review focusing on:
1. **Novelty assessment** — How novel is each of the three claimed contributions? Is it incremental or significant?
2. **Significance** — Would this change how practitioners train code retrievers? Does it advance the field's understanding?
3. **Related work completeness** — Are important baselines or comparisons missing? Is the positioning accurate?
4. **Claim strength vs evidence** — Are the claims well-calibrated to the evidence?
5. **Writing quality and presentation** — Is the paper well-organized and clearly written?
6. **Broader impact** — Does this generalize beyond the specific setup tested?

## Output Format

```
### R2 Review: Novelty & Related Work

**Summary:** (2-3 sentences)

**Strengths:**
- S1: ...
- S2: ...
- ...

**Weaknesses:**
- W1: ...
- W2: ...
- ...

**Questions for Authors:**
- Q1: ...
- ...

**Novelty Score:** X/5
**Overall Score:** X/6
**Confidence:** X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "7c3462f9-cfe1-43c8-bdf8-2048c75c3e04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T17:00:03.906Z_

```json
{
  "parentUuid": "7c3462f9-cfe1-43c8-bdf8-2048c75c3e04",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
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
  "uuid": "b7b23b58-cd22-4144-8a16-ff7420fcfdd6",
  "timestamp": "2026-05-14T17:00:03.906Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T17:00:07.225Z_



I'll start by reading the paper and related project files to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7b23b58-cd22-4144-8a16-ff7420fcfdd6",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pRYXT8pFCUx1et1GY2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e7155f3-a7a2-448c-a8c2-b94ba5ba24cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWn5wWP3MwXyW3ECgtCXqN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6842,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6842,
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

_source line 4 · 2026-05-14T17:00:07.691Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01E69jiZxg5EGaVYDKEnYFvq`</summary>

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
  "parentUuid": "2e7155f3-a7a2-448c-a8c2-b94ba5ba24cd",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pRYXT8pFCUx1et1GY2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c62dc88b-9ae5-4c98-9696-1e0550c3618d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWn5wWP3MwXyW3ECgtCXqN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6842,
      "cache_read_input_tokens": 8249,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6842
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 6842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6842,
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

_source line 5 · 2026-05-14T17:00:07.695Z_

<details><summary>↩ Tool result · `toolu_01E69jiZxg5EGaVYDKEnYFvq`</summary>

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
  "parentUuid": "c62dc88b-9ae5-4c98-9696-1e0550c3618d",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "c56bb40b-053e-48c3-a1ac-76968e53ddd6",
  "sourceToolAssistantUUID": "c62dc88b-9ae5-4c98-9696-1e0550c3618d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T17:00:10.868Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01SbvmQkVVPUHDDXxUDvcNHa`</summary>

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
  "parentUuid": "c56bb40b-053e-48c3-a1ac-76968e53ddd6",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pRppz6rJj2i2aTgQwz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "352db26d-243d-445e-8619-68b083b97f69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rkPm5R3hBPT6Jc2vDuvh8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 7 · 2026-05-14T17:00:11.026Z_

<details><summary>↩ Tool result · `toolu_01SbvmQkVVPUHDDXxUDvcNHa`</summary>

```text
{"result":"# 项目 structfuse-context 概况\n\n## 实验状态 (32 个)\n\n- **p2b_eval_4runs_pool50**: DONE (success) — \n- **d007_50repo_overlap**: DONE (success) — \n- **p2b_5reruns**: DONE (success) — \n- **p2b_eval_4runs_v2**: DONE (success) — \n- **p2b-all-9runs**: DONE (killed) — \n- **p2b-smoke8**: DONE (killed) — \n- **p2b-smoke7**: DONE (killed) — \n- **p2b-smoke6**: DONE (killed) — \n- **p2b-smoke5**: DONE (killed) — \n- **p2b-smoke4**: DONE (killed) — \n- **p2b-smoke3**: DONE (killed) — \n- **p2b-smoke2**: DONE (killed) — \n- **p2b-smoke-test**: DONE (killed) — \n- **mvp_p2a_linear_proxy**: DONE (success) — \n- **mvp_p1_codeql_feasibility**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\n\n## 待处理\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\n\n## 近期结论\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\n  [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt)\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\n- **m1_extraction** (success): —\n\n## 趋势\n成功 10 / 负向 2 / 失败 2 / 共 28\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-42106: 无 GPU 信息\n\n## 告警\n- p2b-smoke-test: 已被终止 — unknown\n- p2b-smoke2: 已被终止 — unknown\n- p2b-smoke3: 已被终止 — unknown\n- p2b-smoke4: 已被终止 — unknown\n- p2b-smoke5: 已被终止 — unknown\n- p2b-smoke6: 已被终止 — unknown\n- p2b-smoke7: 已被终止 — unknown\n- p2b-smoke8: 已被终止 — unknown\n- p2b-all-9runs: 已被终止 — unknown\n- mvp_p2b_contrastive_training: 已被终止 — unknown\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\n- p2b_eval_all: 已被终止 — unknown\n- m2_early_pilot: 已被终止 — unknown\n- m2_early_pilot_v2: 训练失败 — unknown\n- m2_early_pilot_v3: 已被终止 — unknown\n- m1_reextract: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "352db26d-243d-445e-8619-68b083b97f69",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "803907c8-a5ab-4ca6-ba2f-9d6951183f21",
  "sourceToolAssistantUUID": "352db26d-243d-445e-8619-68b083b97f69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T17:00:11.347Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NzQx6VdMMA9P5FBTP3RKDT`</summary>

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
  "parentUuid": "803907c8-a5ab-4ca6-ba2f-9d6951183f21",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pRppz6rJj2i2aTgQwz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e82afb23-0207-4bc9-9da2-9e3fccd5e1d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rkPm5R3hBPT6Jc2vDuvh8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15091,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 160,
          "cache_read_input_tokens": 15091,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1446,
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

_source line 9 · 2026-05-14T17:00:11.361Z_

<details><summary>↩ Tool result · `toolu_01NzQx6VdMMA9P5FBTP3RKDT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\\n\\n## 待处理\\n- plan_018_bm25: BM25 negative baseline: Dream 审稿三档一致认定缺 BM25 baseline 是论文最大结构性缺陷。Phase 1 (CPU): 对 M2 训练语料建 BM25 索引，挖掘 BM25 hard negatives，生成训练数据。Phase 2 (GPU): 用 BM25 negatives 训练 Qwen + StarCoder 各 1 seed，对比 R@1。（排队等待 GPU）\\n\\n## 近期结论\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n  [neg_difficulty_margin_comparison](/api/workspace-files/projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt)\\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n- **m1_extraction** (success): —\\n\\n## 趋势\\n成功 10 / 负向 2 / 失败 2 / 共 28\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 2285, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e82afb23-0207-4bc9-9da2-9e3fccd5e1d4",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "3be4b5a9-be0e-4941-a1c7-d1c217bfa1cd",
  "sourceToolAssistantUUID": "e82afb23-0207-4bc9-9da2-9e3fccd5e1d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T17:00:14.904Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016bau9PRjv3ZaoQdmb21ZvH`</summary>

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
  "parentUuid": "3be4b5a9-be0e-4941-a1c7-d1c217bfa1cd",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pS6QbtHbqx8TC86JJZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3053aa9-8f8f-4ab7-a1e2-4d40870ded1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNWkwzVh184QoQkX6L2X6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3088,
      "cache_read_input_tokens": 16537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3088,
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

_source line 11 · 2026-05-14T17:00:14.931Z_

<details><summary>↩ Tool result · `toolu_016bau9PRjv3ZaoQdmb21ZvH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \\\"harm\\\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).\\n\\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\\n\\n- **Headline result template**: \\\"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\\\"\\n- Backup: \\\"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |\\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\\n- m1_reextract_v2: expanded extraction for higher coverage\\n\\n### Planned (priority order):\\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\\n- plan_015: Dynamic mining baseline\\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\\n\\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the \\\"correcting misconception\\\" narrative loses empirical anchor\\n- Pivot: from \\\"CoCoHaNeRe was wrong because BM25 proxy\\\" → \\\"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps; prior work's negative finding was likely due to uncontrolled variables (data, training protocol), not BM25 specifically\\\"\\n- Paper becomes less dramatic (\\\"correcting\\\" → \\\"clarifying\\\") but still valid as systematic analysis\\n- Claim 1 reworded: \\\"True embedding-distance mining consistently improves code retrieval\\\" (drop the \\\"correcting misconception\\\" framing, keep the empirical finding)\\n- Impact: weaker narrative hook but core experimental contribution survives\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 11181, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3053aa9-8f8f-4ab7-a1e2-4d40870ded1c",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "438e02a8-3034-4572-aaee-ee8d7986a2e6",
  "sourceToolAssistantUUID": "b3053aa9-8f8f-4ab7-a1e2-4d40870ded1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T17:00:15.447Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014w51eb97yATN2Rqswcgcsv`</summary>

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
  "parentUuid": "438e02a8-3034-4572-aaee-ee8d7986a2e6",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pS6QbtHbqx8TC86JJZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bab7dd9d-06ac-4124-96c9-1f8833a1d908",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNWkwzVh184QoQkX6L2X6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3088,
      "cache_read_input_tokens": 16537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3088,
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

_source line 13 · 2026-05-14T17:00:15.461Z_

<details><summary>↩ Tool result · `toolu_014w51eb97yATN2Rqswcgcsv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-12\\n# 说明: 只收录项目文件中已引用的 + 确定存在的知名论文。不确定的信息标注\\\"需验证\\\"。\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline  # StructFuse 的评估基准\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Karthik Narasimhan, Ofir Press\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: building-block  # StructFuse 用其 repo 做数据提取\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n        note: \\\"需验证 venue（可能已投稿会议）\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务，StructFuse 可用于评估。\\\"\\n        note: \\\"需验证年份和 venue\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及代码领域的对比学习\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式，是 StructFuse 对比训练的方法论基础。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，是 StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"SimCLR: A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Mining Hard Negatives with Curriculum for Dense Retrieval\\\"\\n        authors: \\\"需验证\\\"\\n        venue: \\\"需验证\\\"\\n        year: \\\"需验证\\\"\\n        relation: background\\n        summary: \\\"课程学习式 hard negative 挖掘，从易到难训练检索器。\\\"\\n        note: \\\"需验证完整信息\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block  # StructFuse 核心组件\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: EMNLP (Findings)\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: background\\n        summary: \\\"大规模开源代码 LLM，广泛用于代码嵌入的 backbone。\\\"\\n        note: \\\"需验证 venue（可能是 arXiv 或其他）\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Qwen Team (Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block  # StructFuse 用 Qwen2.5-Coder-3B 做检索器\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n        note: \\\"需验证确切标题和年份\\\"\\n\\n      - title: \\\"Contrastive Learning for Source Code with Structural and Functional Properties\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: ACL (Findings)\\n        year: 2022\\n        relation: background\\n        summary: \\\"代码对比学习中利用结构/功能属性构建正负样本对。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。Phase 2a 实验发现 BM25 在 bug fixing 定位中可能有误导性（负系数）。\\\"\\n\\n# ==========================================================================\\n# 待补充\\n# ==========================================================================\\n# 以下论文可能相关，待确认后补充：\\n# - FAISS (Johnson et al., 2019) — ANN 检索库，StructFuse 评估可能用到\\n# - Tree-sitter — 增量解析器，与 CodeQL 互补\\n# - Aider / Moatless Tools — SWE-bench 上的其他代码检索方法\\n# - CoSQA (Huang et al., 2021) — 代码搜索 QA 数据集\\n# - DeepSeek-Coder — 另一个可能的 backbone 对比\\n\", \"total_chars\": 9647, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bab7dd9d-06ac-4124-96c9-1f8833a1d908",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "ff0ca1dd-ce10-4524-94d7-fe1a58ddc8f6",
  "sourceToolAssistantUUID": "bab7dd9d-06ac-4124-96c9-1f8833a1d908",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T17:00:16.414Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GoTycioeKU3DR41Vu5z6Ay`</summary>

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
  "parentUuid": "ff0ca1dd-ce10-4524-94d7-fe1a58ddc8f6",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pS6QbtHbqx8TC86JJZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20dd0c2c-78f4-49c4-8d44-d5294a20578b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNWkwzVh184QoQkX6L2X6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3088,
      "cache_read_input_tokens": 16537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3088,
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

_source line 15 · 2026-05-14T17:00:16.426Z_

<details><summary>↩ Tool result · `toolu_01GoTycioeKU3DR41Vu5z6Ay`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20dd0c2c-78f4-49c4-8d44-d5294a20578b",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "bdc1bf52-23f3-45a6-b136-9f6f12adb177",
  "sourceToolAssistantUUID": "20dd0c2c-78f4-49c4-8d44-d5294a20578b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T17:00:16.718Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YCPr9WyUgVhQV2L7dTqYpU`</summary>

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
  "parentUuid": "bdc1bf52-23f3-45a6-b136-9f6f12adb177",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pS6QbtHbqx8TC86JJZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0869ea68-8c9f-4fbb-b31d-4567e48fc05e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNWkwzVh184QoQkX6L2X6o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3088,
      "cache_read_input_tokens": 16537,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3088
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 378,
          "cache_read_input_tokens": 16537,
          "cache_creation_input_tokens": 3088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3088,
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

_source line 17 · 2026-05-14T17:00:16.734Z_

<details><summary>↩ Tool result · `toolu_01YCPr9WyUgVhQV2L7dTqYpU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 31\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n- id: D028\\n  date: 2026-05-14 11:09 UTC\\n  summary: Claim 2 降级待定：M2 full 结果决定 \\\"conditional benefit\\\" 是独立 claim 还是降为 observation\\n  rationale: Reviewer 覆盖率审查指出 Claim 2 最薄弱：n=2 encoders 交互效应无统计功效，neg_difficulty 是描述性非实验性证据。建议降为\\n    \\\"observation + mechanistic hypothesis\\\"。决策延迟到 M2 full 18 runs 完成后：若 Qwen dataflow>random\\n    p<0.05 则保持 conditional claim；否则降级为 observation。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: Qwen pilot positive\\n    result: dataflow > random +0.8pp val_loss\\n  - exp_id: plan_013_starcoder\\n    role: StarCoder pilot negative\\n    result: dataflow < random -0.5pp\\n  - exp_id: m2_full_qwen\\n    role: go/no-go for claim strength\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: encoder generality test\\n    result: RUNNING\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D029\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream full review 完成：7 条三档一致结构性问题确认，BM25 baseline 升为 P0，pool size sensitivity\\n    新增 plan_019\\n  rationale: 'dream_20260514T075732 (full review mode) 三档评分: Best 4/6 WA, Median 3/6\\n    WR, Worst 3/6 WR。跨三档一致的结构性问题 7 条：(1) 缺 BM25 baseline 是 #1 共识——论文核心叙事（纠正 CoCoHaNeRe）无实证支撑，已加\\n    plan_018 P0；(2) N=2 编码器限制——保持 honest framing，无法加更多编码器；(3) StarCoder 误标为 encoder-decoder——已修正为\\n    decoder-only；(4) RepoBench-R 无 CIs——plan_004 已标注多 seed 要求；(5) Pool=50 太小——新增 plan_019\\n    P1；(6) 34% structural coverage 未分层——plan_005 已扩展；(7) Checkpoint selection criterion\\n    未指定——写作时明确。观察项：effect sizes 太小（等 M2 真实数据）、overfitting 分析（提取现有训练 log）。忽略项：broken\\n    bibliography（dream artifact）、0 figures（dream artifact）。评分顺序正常（best≥median=worst）。下一步：派\\n    Agent 准备 BM25 mining（CPU），M2 完成后立即执行 plan_018 training phase。'\\n  related_experiments:\\n  - exp_id: plan_018\\n    role: new P0 experiment added\\n    result: planned\\n  - exp_id: plan_019\\n    role: new P1 experiment added\\n    result: planned\\n  - exp_id: plan_004\\n    role: updated with multi-seed CI requirement\\n    result: planned\\n  - exp_id: plan_005\\n    role: extended with structural coverage stratification\\n    result: planned\\n  depends_on:\\n  - D024\\n  - D028\\n- id: D030\\n  date: 2026-05-14 16:23 UTC\\n  summary: Dream dream_20260514T075732 分析完成：7 项确认行动 + 5 项观察项 + re-dream 后批准新 P0\\n  rationale: 'Dream full review (2 Reviewers roundtable) 三档评分: Best=4/6(WA), Median=3/6(WR),\\n    Worst=3/6(WR)。Median 未达 borderline，需修复结构性问题后 re-dream。\\n\\n\\n    **三档一致的结构性问题（7 项确认行动）：**\\n\\n    1. [EXP] 缺 BM25 negative baseline — 论文核心 narrative (correcting CoCoHaNeRe) 无实证。加\\n    plan_018, P0, Phase1 CPU 立即启动\\n\\n    2. [EXP] RepoBench-R 缺 CIs — plan_004 增加多 seed 评估\\n\\n    3. [EXP] Pool size 50 过小 — 加 plan_019 sensitivity analysis\\n\\n    4. [EXP] 34% structural coverage 未分层 — 扩展 plan_005 加 structural-available vs fallback\\n    stratum + neg_difficulty quartile\\n\\n    5. [FRAMING] N=2 encoders → 降级为 \\\"observation + hypothesis\\\"，非 validated mechanism\\n\\n    6. [FRAMING] StarCoder 架构 → 修正为 \\\"decoder-only\\\"（已改）\\n\\n    7. [FRAMING] Claim 3 (CodeQL pipeline) → 降为 supporting methodology（已改）\\n\\n\\n    **观察项（等真实数据）：**\\n\\n    1. Effect sizes marginal [M][W] — 等 M2 full 统计结果\\n\\n    2. Dataflow claim strength [M][W] — D028 已 plan\\n\\n    3. \\\"Scaling law\\\" [W] → 用 \\\"trend\\\" + CIs\\n\\n    4. Temperature ablation contradiction [W] — plan_014 结果决定\\n\\n    5. Zero method contribution [M][W] — framing 强度决定\\n\\n\\n    **Re-dream 要求：** framing + plan 修改完成后需 re-dream，best ≥ WA 且 median ≥ borderline\\n    后才批准新 P0 实验。已在跑的实验继续。'\\n  related_experiments:\\n  - exp_id: dream_20260514T075732\\n    role: trigger\\n    result: best=4/6 WA, median=3/6 WR, worst=3/6 WR\\n  - exp_id: plan_018\\n    role: new_from_dream\\n    result: planned — BM25 baseline\\n  - exp_id: plan_019\\n    role: new_from_dream\\n    result: planned — pool size sensitivity\\n  depends_on:\\n  - D028\\n  - D024\\n\", \"total_chars\": 23713, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0869ea68-8c9f-4fbb-b31d-4567e48fc05e",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "e8232add-ca41-4337-b7fc-723965a03865",
  "sourceToolAssistantUUID": "0869ea68-8c9f-4fbb-b31d-4567e48fc05e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T17:00:21.093Z_

Now let me read the paper artifacts and any available draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8232add-ca41-4337-b7fc-723965a03865",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pSVRwxGjkqdZYAYsqu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "654b885b-fb17-4e4c-a852-ad5ce359a581",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RozT6Whg44tELVSvHYSs58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20708,
      "cache_read_input_tokens": 19625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20708,
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

_source line 19 · 2026-05-14T17:00:23.044Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01E1T2Q2VDNSh8B8FVSA7ZpN`</summary>

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
  "parentUuid": "654b885b-fb17-4e4c-a852-ad5ce359a581",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pSVRwxGjkqdZYAYsqu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "935ae80c-fb63-41b2-8f70-06daca93de65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RozT6Whg44tELVSvHYSs58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20708,
      "cache_read_input_tokens": 19625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20708,
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

_source line 20 · 2026-05-14T17:00:23.061Z_

<details><summary>↩ Tool result · `toolu_01E1T2Q2VDNSh8B8FVSA7ZpN`</summary>

```text
artifacts/dream_reports/dream_20260512T204322/best/paper.tex
artifacts/dream_reports/dream_20260512T204322/median/paper.tex
artifacts/dream_reports/dream_20260512T204322/worst/paper.tex
artifacts/dream_reports/dream_20260514T075732/best/paper.tex
artifacts/dream_reports/dream_20260514T075732/median/paper.tex
artifacts/dream_reports/dream_20260514T075732/worst/paper.tex
artifacts/dream_reports/dream_20260514T162530/best/paper.tex
artifacts/dream_reports/dream_20260514T162530/median/paper.tex
artifacts/dream_reports/dream_20260514T162530/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "935ae80c-fb63-41b2-8f70-06daca93de65",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "78fd328d-00b3-4612-8e20-7d9838e8fca0",
  "sourceToolAssistantUUID": "935ae80c-fb63-41b2-8f70-06daca93de65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T17:00:23.989Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018niksW2x6MrdRFqhZEQPR1`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78fd328d-00b3-4612-8e20-7d9838e8fca0",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pSVRwxGjkqdZYAYsqu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "472ba90b-5828-4776-b77b-23a5c8124dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RozT6Whg44tELVSvHYSs58",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20708,
      "cache_read_input_tokens": 19625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20708,
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

_source line 22 · 2026-05-14T17:00:24.006Z_

<details><summary>↩ Tool result · `toolu_018niksW2x6MrdRFqhZEQPR1`</summary>

```text
artifacts/dream_reports/dream_20260512T204322/best/paper.pdf
artifacts/dream_reports/dream_20260512T204322/median/paper.pdf
artifacts/dream_reports/dream_20260512T204322/worst/paper.pdf
artifacts/dream_reports/dream_20260514T075732/best/paper.pdf
artifacts/dream_reports/dream_20260514T075732/median/paper.pdf
artifacts/dream_reports/dream_20260514T075732/worst/paper.pdf
artifacts/dream_reports/dream_20260514T162530/best/paper.pdf
artifacts/dream_reports/dream_20260514T162530/median/paper.pdf
artifacts/dream_reports/dream_20260514T162530/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "472ba90b-5828-4776-b77b-23a5c8124dfd",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "17f55605-8594-4222-a0bb-86a370f9f161",
  "sourceToolAssistantUUID": "472ba90b-5828-4776-b77b-23a5c8124dfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T17:00:24.571Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Vc3Ckq4bZnfHUdD5ZWKskW`</summary>

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
  "parentUuid": "17f55605-8594-4222-a0bb-86a370f9f161",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pSVRwxGjkqdZYAYsqu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4967f99b-8f7a-46b5-8c4b-6f1fad96ce9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RozT6Whg44tELVSvHYSs58",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20708,
      "cache_read_input_tokens": 19625,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20708
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 19625,
          "cache_creation_input_tokens": 20708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20708,
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

_source line 24 · 2026-05-14T17:00:24.586Z_

<details><summary>↩ Tool result · `toolu_01Vc3Ckq4bZnfHUdD5ZWKskW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); heavy inference cost |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | Repository-level Graph for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2025) | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (2025) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献\\n\\n- CodexGraph: arXiv:2408.03910, NAACL 2025\\n- LocAgent: arXiv:2503.09089, ACL 2025\\n- RANGER: arXiv:2509.25257, 2025\\n- RepoGraph: arXiv:2410.14684, ICLR 2025\\n- GraphCoder: arXiv:2406.07003, ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, 2025\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\", \"total_chars\": 8062, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4967f99b-8f7a-46b5-8c4b-6f1fad96ce9a",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "78a2239e-f77f-46a2-9156-833d905ba559",
  "sourceToolAssistantUUID": "4967f99b-8f7a-46b5-8c4b-6f1fad96ce9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-14T17:00:27.774Z_

Let me read the most recent dream paper (best version) to see the actual draft content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78a2239e-f77f-46a2-9156-833d905ba559",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pT4z4La5pJLRhJuTQd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8faff91f-cec6-4240-9e4b-57bd692d90a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQYdrHQXa1XFZi6P6EYKv1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3140,
      "cache_read_input_tokens": 40333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3140,
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

_source line 26 · 2026-05-14T17:00:28.281Z_

<details open><summary>🔧 Tool call — Read · `toolu_016NURSx8Xm3zcYQBFUzbJmr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8faff91f-cec6-4240-9e4b-57bd692d90a8",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pT4z4La5pJLRhJuTQd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40ac2f12-a097-4246-bd22-e53408617659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQYdrHQXa1XFZi6P6EYKv1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3140,
      "cache_read_input_tokens": 40333,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3140
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 120,
          "cache_read_input_tokens": 40333,
          "cache_creation_input_tokens": 3140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3140,
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

_source line 27 · 2026-05-14T17:00:28.583Z_

<details><summary>↩ Tool result · `toolu_016NURSx8Xm3zcYQBFUzbJmr`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=1in]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	
14	\title{What Makes Hard Negatives Work for Code Retrieval?\\A Systematic Study of Mining Strategies and Representation Geometry}
15	
16	\author{Anonymous}
17	\date{}
18	
19	\begin{document}
20	\maketitle
21	
22	%==============================================================================
23	\begin{abstract}
24	%==============================================================================
25	Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.
26	Prior work (CoCoHaNeRe) reports that embedding-distance hard negatives \emph{harm} code retrieval, but this finding was derived from BM25-proxy negatives mislabeled as embedding-distance.
27	We present a controlled comparison of four negative mining strategies---random, BM25, true embedding-distance, and structure-grounded (dataflow)---for contrastive code retrieval across two decoder-only encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with 9 seeds each.
28	Our results show that (1)~true embedding-distance mining \emph{consistently improves} retrieval over random baselines (+2.0pp R@1 Qwen, +1.5pp StarCoder), correcting the prior misconception;
29	(2)~BM25 negatives \emph{harm} both encoders ($-$2.5pp, $-$2.7pp), confirming the artifact;
30	and (3)~structure-grounded negatives via inter-procedural dataflow provide conditional additional benefit (+1.0pp Qwen) when encoder representations are saturated, but not when the representation space has healthy separation (StarCoder).
31	We provide mechanistic explanation via representation geometry analysis: negative difficulty scales monotonically with improvement (Q4 hardest quartile: +3.2pp vs Q1: +0.8pp).
32	Downstream, embedding mining improves SWE-bench Lite resolve rate by +2.5pp ($p=0.018$) and dataflow by +3.2pp ($p=0.008$).
33	Strategy rankings are stable across temperatures ($\tau \in \{0.05, 0.1, 0.2\}$), pool sizes (50--500), and data scales (1K--5K), establishing robust practical guidance.
34	\end{abstract}
35	
36	%==============================================================================
37	\section{Introduction}
38	\label{sec:intro}
39	%==============================================================================
40	
41	Repository-level code repair requires selecting relevant files from large codebases given a natural-language issue description.
42	Contrastive learning with hard negative mining is the dominant paradigm for training dense retrievers in this setting.
43	The quality of negatives directly determines representation quality: too-easy negatives waste gradient signal, while poorly chosen ``hard'' negatives can introduce noise.
44	
45	Despite its importance, the field lacks systematic understanding of what negative mining strategies work for code retrieval.
46	The most relevant prior study, CoCoHaNeRe, reports that embedding-distance hard negatives \emph{harm} code search performance by $-$27pp R@1.
47	This finding has influenced subsequent work to avoid embedding-based mining for code.
48	However, we identify that CoCoHaNeRe used BM25-based retrieval as a proxy for embedding distance---a critical methodological conflation, as BM25 selects lexically similar negatives that destroy useful token-overlap signals during contrastive training.
49	
50	We present StructFuse, a systematic study comparing four negative mining strategies: random, BM25, true embedding-distance, and structure-grounded (dataflow) negatives derived from inter-procedural call-graph analysis via CodeQL.
51	Our study spans two decoder-only code encoders with distinct pretraining objectives and representation geometries, 9 random seeds per configuration, and evaluation on both SWE-smith file retrieval and SWE-bench Lite end-to-end repair.
52	
53	Our contributions are threefold:
54	
55	\begin{enumerate}
56	\item We \textbf{correct the misconception} that embedding-distance hard negatives harm code retrieval.
57	True embedding mining yields +1.6--2.0pp R@1 across two encoders, while BM25 negatives reproduce the reported harm ($-$2.5 to $-$2.7pp).
58	The ordering BM25 $<$ random $<$ dataflow $\leq$ embedding constitutes a quality spectrum for negative mining strategies.
59	
60	\item We introduce \textbf{structure-grounded negatives} via inter-procedural dataflow and characterize when they provide additional benefit.
61	When pretrained encoder representations are saturated (pos\_sim $>$ 0.98, Qwen), dataflow negatives provide +1.0pp beyond random.
62	When representation space has healthy separation (pos\_sim $\sim$ 0.80, StarCoder), embedding mining alone suffices.
63	Stratified analysis reveals the true per-instance dataflow effect is +2.8pp on instances with structural data, diluted to +1.0pp overall by the 66\% fallback stratum.
64	
65	\item We provide \textbf{mechanistic explanation} via representation geometry analysis.
66	Negative difficulty quartile analysis shows monotonically increasing benefit: Q4 (hardest) yields +3.2pp vs Q1 (easiest) at +0.8pp.
67	This encoder-strategy interaction explains contradictory findings in prior work and enables practitioners to predict which strategy suits their encoder.
68	\end{enumerate}
69	
70	%==============================================================================
71	\section{Related Work}
72	\label{sec:related}
73	%==============================================================================
74	
75	\paragraph{Code Retrieval for Software Engineering.}
76	Dense retrieval has become the dominant paradigm for repository-level code search.
77	SweRank~and SWE-Fixer train contrastive retrievers on issue-file pairs mined from GitHub, achieving strong results on SWE-bench.
78	These methods rely on text-based similarity alone, ignoring structural dependencies between code files.
79	
80	\paragraph{Hard Negative Mining.}
81	In general dense retrieval, hard negative mining is well-studied.
82	ANCE proposes asynchronous index refresh for dynamic mining.
83	Curriculum-based approaches gradually increase negative difficulty.
84	For code, CoCoHaNeRe reports that embedding-distance negatives harm code search, recommending against their use.
85	We show this conclusion stems from a BM25-proxy artifact.
86	
87	\paragraph{Graph-Based Code Understanding.}
88	Several methods leverage code structure at inference time.
89	CodexGraph builds a code graph database for LLM navigation.
90	LocAgent uses repository structure trees for fault localization.
91	RANGER employs call graphs for code navigation.
92	ARISE uses intra-procedural dataflow for code understanding.
93	GraphCodeBERT incorporates data flow into pretraining objectives.
94	All operate at inference time; StructFuse is the first to inject structural signal via training-time negative mining, making it complementary to these approaches (Table~\ref{tab:lit_comparison}).
95	
96	%==============================================================================
97	\section{Method}
98	\label{sec:method}
99	%==============================================================================
100	
101	\subsection{Problem Setup}
102	
103	Given a natural-language issue description $q$ and a repository with files $\mathcal{F} = \{f_1, \ldots, f_n\}$, the retriever scores each file $s(q, f_i)$ and returns the top-$k$ files.
104	We train a bi-encoder using InfoNCE contrastive loss with temperature $\tau$:
105	\begin{equation}
106	\mathcal{L} = -\log \frac{\exp(s(q, f^+)/\tau)}{\exp(s(q, f^+)/\tau) + \sum_{j=1}^{K} \exp(s(q, f_j^-)/\tau)}
107	\end{equation}
108	where $f^+$ is the gold file and $\{f_j^-\}_{j=1}^K$ are negative files.
109	The choice of how to select negatives is the focus of this study.
110	
111	\subsection{Negative Mining Strategies}
112	
113	We compare four strategies for selecting $\{f_j^-\}$:
114	
115	\paragraph{Random.}
116	Sample uniformly from $\mathcal{F} \setminus \{f^+\}$.
117	This is the standard baseline in contrastive learning.
118	
119	\paragraph{BM25.}
120	Select the top-scoring BM25 results for query $q$ that are not $f^+$.
121	BM25 negatives have high lexical overlap with the query.
122	
123	\paragraph{Embedding-distance.}
124	Using the pretrained encoder, compute embeddings for all files and select the nearest neighbors of $q$ (excluding $f^+$) as negatives.
125	These are semantically similar but non-relevant files.
126	Mining is performed once using the pretrained checkpoint (static mining).
127	
128	\paragraph{Dataflow (structure-grounded).}
129	Using inter-procedural call-graph analysis, we define:
130	\begin{equation}
131	f^-_{\text{struct}} = \arg\max_{f \in \mathcal{F}: s(f,q) > \tau_{\text{sim}} \;\wedge\; \neg\text{reachable}_G(f, f^+)} s(f, q)
132	\end{equation}
133	where $G$ is the 2-hop call graph extracted via CodeQL.
134	Dataflow negatives are semantically similar to the query \emph{and} structurally disconnected from the gold file---they are textually confusable but functionally unrelated.
135	When structural data is unavailable (66\% of instances), we fall back to embedding-distance mining.
136	
137	\subsection{Structural Extraction via CodeQL}
138	
139	We extract inter-procedural call graphs from Python repositories using CodeQL.
140	For each repository, we build a CodeQL database and query for function-level call relationships, yielding a directed graph where nodes are functions and edges represent caller--callee relationships.
141	File-level connectivity is derived by projecting function-level edges: two files are connected if any function in one calls any function in the other within 2 hops.
142	
143	At scale (5K training instances, 131 repositories), the pipeline achieves 0\% timeout rate, with 123/131 repositories successfully processed.
144	78\% of extracted file pairs are connected-but-not-gold, providing a rich pool of structurally-informed negatives.
145	Structural data is available for 34\% of query--positive pairs.
146	
147	\subsection{Hop Depth Selection}
148	
149	We ablate the hop depth parameter for call-graph bounding (Section~\ref{sec:hop_ablation}).
150	2-hop is optimal: 1-hop provides only 12.4\% coverage (too sparse for meaningful ``disconnected'' definition), while 3-hop reaches 58.6\% coverage where the disconnected set becomes too narrow and noisy.
151	2-hop achieves 34.3\% coverage with a principled semantic boundary: direct callers/callees and their immediate neighbors.
152	
153	\subsection{Training Details}
154	
155	We fine-tune two decoder-only code encoders with LoRA (rank 16): Qwen2.5-Coder-3B and StarCoder2-3B.
156	Training uses 5K instances from SWE-smith with InfoNCE loss at $\tau = 0.1$.
157	Each configuration is trained with 9 random seeds for statistical robustness.
158	All mining is static (computed once from pretrained checkpoints).
159	
160	%==============================================================================
161	\section{Experiments}
162	\label{sec:experiments}
163	%==============================================================================
164	
165	\subsection{Evaluation Setup}
166	
167	\paragraph{SWE-smith.}
168	File-level retrieval on SWE-smith validation split ($\sim$15.2K instances).
169	Primary metric: R@1 with pool size 50 (default).
170	We report mean and 95\% bootstrap confidence intervals across 9 seeds.
171	
172	\paragraph{SWE-bench Lite.}
173	End-to-end evaluation on 300 SWE-bench Lite instances.
174	The retriever provides top-5 context files to a Qwen3.6-27B agent that generates patches.
175	Metric: resolve rate (percentage of correctly patched instances).
176	
177	\paragraph{RepoBench-R.}
178	Cross-file code completion retrieval on RepoBench-R test\_hard (pool $\approx$ 18) and test\_easy (pool $\approx$ 6).
179	
180	%------------------------------------------------------------------------------
181	\subsection{Main Results: Four-Strategy Comparison}
182	\label{sec:main_results}
183	%------------------------------------------------------------------------------
184	
185	Table~\ref{tab:main_4strategy} presents the full four-strategy comparison on SWE-smith validation.
186	The ordering is consistent across both encoders: BM25 $<$ random $<$ dataflow $\leq$ embedding.
187	
188	\begin{table}[h]
189	\centering
190	\caption{Full four-strategy comparison on SWE-smith validation (R@1 \%, pool=50, 9-seed mean $\pm$ 95\% CI). BM25 negatives harm both encoders, confirming the CoCoHaNeRe artifact. True embedding mining consistently improves over random.}
191	\label{tab:main_4strategy}
192	\begin{tabular}{llccc}
193	\toprule
194	\textbf{Encoder} & \textbf{Strategy} & \textbf{R@1 (\%)} & \textbf{95\% CI} & \textbf{$\Delta$ vs Random (pp)} \\
195	\midrule
196	Qwen & BM25 & 52.0 & [51.2, 52.8] & $-$2.5 \\
197	Qwen & random & 54.5 & [53.8, 55.2] & --- \\
198	Qwen & dataflow & 55.5 & [54.6, 56.4] & +1.0 \\
199	Qwen & embedding & 56.5 & [55.8, 57.2] & +2.0 \\
200	\midrule
201	StarCoder & BM25 & 43.3 & [42.3, 44.3] & $-$2.7 \\
202	StarCoder & random & 46.0 & [45.1, 46.9] & --- \\
203	StarCoder & dataflow & 45.8 & [44.8, 46.8] & $-$0.2 \\
204	StarCoder & embedding & 47.5 & [46.6, 48.4] & +1.5 \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	BM25 negatives harm performance for both encoders ($-$2.5pp Qwen, $-$2.7pp StarCoder vs random).
210	BM25 selects lexically similar files that share function names, variable names, and import patterns with the query.
211	These are precisely the signals that contrastive learning should leverage for discrimination; training the encoder to ignore them degrades retrieval.
212	
213	True embedding-distance mining improves both encoders (+2.0pp Qwen, +1.5pp StarCoder), selecting files that are semantically similar in the pretrained embedding space but not relevant to the query.
214	This forces the encoder to learn finer-grained semantic distinctions.
215	
216	Dataflow negatives benefit Qwen (+1.0pp, CI lower bound $>$ 0) but not StarCoder ($-$0.2pp, CI includes zero).
217	Section~\ref{sec:stratified} provides mechanistic explanation for this interaction.
218	
219	%------------------------------------------------------------------------------
220	\subsection{SWE-bench Lite End-to-End Evaluation}
221	\label{sec:swebench}
222	%------------------------------------------------------------------------------
223	
224	\begin{table}[h]
225	\centering
226	\caption{SWE-bench Lite resolve rate (300 instances, Qwen3.6-27B agent, top-5 retrieval).}
227	\label{tab:swebench}
228	\begin{tabular}{lcccc}
229	\toprule
230	\textbf{Strategy} & \textbf{Resolved} & \textbf{Total} & \textbf{Rate (\%)} & \textbf{$\Delta$ vs Random (pp)} \\
231	\midrule
232	random & 66 & 300 & 22.0 & --- \\
233	embedding & 73 & 300 & 24.3 & +2.3 \\
234	dataflow & 76 & 300 & 25.3 & +3.3 \\
235	\bottomrule
236	\end{tabular}
237	\end{table}
238	
239	Retrieval quality improvements amplify at the downstream task level.
240	Embedding mining yields +2.5pp resolve rate ($p = 0.018$, 95\% CI [+0.7, +4.3]), and dataflow yields +3.2pp ($p = 0.008$, CI [+1.0, +5.5]) over random (Table~\ref{tab:swebench_bootstrap}).
241	The difference between dataflow and embedding is +0.7pp but not significant ($p = 0.134$, CI [$-$1.5, +2.9]).
242	
243	\begin{table}[h]
244	\centering
245	\caption{Bootstrap significance tests for SWE-bench Lite (10K resamples).}
246	\label{tab:swebench_bootstrap}
247	\begin{tabular}{lccc}
248	\toprule
249	\textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$-value} \\
250	\midrule
251	embedding $-$ random & +2.5 & [+0.7, +4.3] & 0.018 \\
252	dataflow $-$ random & +3.2 & [+1.0, +5.5] & 0.008 \\
253	dataflow $-$ embedding & +0.7 & [$-$1.5, +2.9] & 0.134 \\
254	\bottomrule
255	\end{tabular}
256	\end{table}
257	
258	\paragraph{Breakdown by Patch Complexity.}
259	Multi-file patches (37\% of instances) are the primary source of dataflow advantage: dataflow achieves +5.4pp over random on multi-file patches (17.1\% vs 11.7\%) compared to +2.2pp on single-file patches (30.2\% vs 28.0\%).
260	This is consistent with the mechanism: dataflow negatives train the retriever to understand cross-module dependencies, which matters most when the gold patch spans multiple files.
261	
262	\begin{table}[h]
263	\centering
264	\caption{SWE-bench resolve rate by patch complexity.}
265	\label{tab:swebench_complexity}
266	\begin{tabular}{lcccc}
267	\toprule
268	\textbf{Patch Type} & \textbf{N} & \textbf{random (\%)} & \textbf{embedding (\%)} & \textbf{dataflow (\%)} \\
269	\midrule
270	single-file & 189 & 28.0 & 30.7 & 30.2 \\
271	multi-file & 111 & 11.7 & 14.4 & 17.1 \\
272	\bottomrule
273	\end{tabular}
274	\end{table}
275	
276	%------------------------------------------------------------------------------
277	\subsection{RepoBench-R Cross-File Retrieval}
278	\label{sec:repobench}
279	%------------------------------------------------------------------------------
280	
281	Table~\ref{tab:repobench} shows results on RepoBench-R test\_hard (pool $\approx$ 18).
282	Embedding mining significantly improves R@1 for both encoders (+2.1pp Qwen, +1.5pp StarCoder), confirming cross-benchmark generalization.
283	Dataflow provides +1.2pp for Qwen (CI marginally excludes zero) but is ineffective for StarCoder ($-$0.2pp, CI includes zero)---the same encoder-strategy interaction observed on SWE-smith.
284	
285	\begin{table}[h]
286	\centering
287	\caption{RepoBench-R test\_hard results (pool $\approx$ 18, 9-seed mean $\pm$ 95\% CI).}
288	\label{tab:repobench}
289	\begin{tabular}{llccc}
290	\toprule
291	\textbf{Encoder} & \textbf{Strategy} & \textbf{R@1 (\%)} & \textbf{95\% CI} & \textbf{$\Delta$ vs Random (pp)} \\
292	\midrule
293	Qwen & random & 62.1 & [61.4, 62.8] & --- \\
294	Qwen & embedding & 64.2 & [63.4, 65.0] & +2.1 \\
295	Qwen & dataflow & 63.3 & [62.4, 64.2] & +1.2 \\
296	\midrule
297	StarCoder & random & 57.4 & [56.6, 58.2] & --- \\
298	StarCoder & embedding & 58.9 & [58.0, 59.8] & +1.5 \\
299	StarCoder & dataflow & 57.2 & [56.2, 58.2] & $-$0.2 \\
300	\bottomrule
301	\end{tabular}
302	\end{table}
303	
304	On test\_easy (pool $\approx$ 6), deltas are compressed due to ceiling effects: Qwen embedding +1.2pp (84.3\% $\to$ 85.5\%), StarCoder embedding +1.0pp (81.2\% $\to$ 82.2\%).
305	This is expected---smaller pools leave fewer distractors for mining quality to differentiate.
306	
307	%------------------------------------------------------------------------------
308	\subsection{Stratified Analysis}
309	\label{sec:stratified}
310	%------------------------------------------------------------------------------
311	
312	\paragraph{Structural Data Availability.}
313	Table~\ref{tab:stratified_structural} decomposes dataflow performance by whether structural data was available for each instance.
314	On the 34\% of instances with dataflow connectivity, the dataflow advantage is +2.8pp (Qwen)---substantially larger than the pooled +1.0pp.
315	On the 66\% fallback stratum where dataflow degrades to embedding or random selection, the advantage is +0.1pp (effectively zero).
316	This decomposition directly addresses the concern that 34\% coverage dilutes the signal: the true per-instance effect is +2.8pp, not +1.0pp.
317	
318	\begin{table}[h]
319	\centering
320	\caption{Stratified R@1 delta by structural data availability (Qwen encoder).}
321	\label{tab:stratified_structural}
322	\begin{tabular}{lccccc}
323	\toprule
324	\textbf{Stratum} & \textbf{N} & \textbf{random} & \textbf{embedding} & \textbf{dataflow} & \textbf{df$-$rand (pp)} \\
325	\midrule
326	With dataflow (34\%) & $\sim$5.2K & 53.1 & 55.4 & 55.9 & +2.8 \\
327	Fallback (66\%) & $\sim$10K & 55.2 & 57.3 & 55.3 & +0.1 \\
328	\midrule
329	Overall & $\sim$15.2K & 54.5 & 56.5 & 55.5 & +1.0 \\
330	\bottomrule
331	\end{tabular}
332	\end{table}
333	
334	\paragraph{Negative Difficulty Quartiles.}
335	Table~\ref{tab:neg_difficulty} presents the strongest mechanistic evidence.
336	We partition instances by negative difficulty (margin between positive and hardest negative similarity).
337	The benefit of mining strategies scales monotonically with difficulty: Q4 (hardest, margin 0.008) shows +3.2pp embedding delta, while Q1 (easiest, margin 0.142) shows only +0.8pp.
338	This confirms the representation saturation hypothesis: when random negatives are already easy to distinguish (large margin), better mining adds little; when the margin is thin, mining quality is critical.
339	
340	\begin{table}[h]
341	\centering
342	\caption{R@1 delta by negative difficulty quartile (Qwen encoder).}
343	\label{tab:neg_difficulty}
344	\begin{tabular}{lccc}
345	\toprule
346	\textbf{Quartile} & \textbf{Margin (mean)} & \textbf{emb$-$rand (pp)} & \textbf{df$-$rand (pp)} \\
347	\midrule
348	Q1 (easiest) & 0.142 & +0.8 & +0.3 \\
349	Q2 & 0.078 & +1.5 & +0.7 \\
350	Q3 & 0.031 & +2.4 & +1.2 \\
351	Q4 (hardest) & 0.008 & +3.2 & +2.1 \\
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	\paragraph{Repo Size and Pool Size Strata.}
357	Embedding delta is inversely related to repository size: small repos ($<$50 files) show +2.8pp, while extra-large repos ($>$500 files) show +1.6pp.
358	Pool size strata show a complementary pattern: embedding delta increases from +1.0pp (pool $<$ 20) to +2.5pp (pool $>$ 50), as larger pools provide more distractors where mining quality matters.
359	
360	\paragraph{Query--Positive Similarity.}
361	When query-positive similarity is high ($>$0.95), embedding delta is largest (+2.6pp) and dataflow delta is also substantial (+1.8pp).
362	At low similarity ($<$0.85), both deltas shrink (+1.2pp embedding, +0.2pp dataflow).
363	High-similarity instances are precisely those where the retriever struggles to separate the positive from near-duplicates, making negative quality most impactful.
364	
365	%------------------------------------------------------------------------------
366	\subsection{Ablation Studies}
367	\label{sec:ablations}
368	%------------------------------------------------------------------------------
369	
370	\subsubsection{Temperature Ablation}
371	\label{sec:temp_ablation}
372	
373	\begin{table}[h]
374	\centering
375	\caption{Temperature ablation (R@1 \%). Strategy rankings are preserved across all three temperatures.}
376	\label{tab:temperature}
377	\begin{tabular}{clcccc}
378	\toprule
379	$\tau$ & \textbf{Encoder} & \textbf{random} & \textbf{embedding} & \textbf{dataflow} & \textbf{emb$-$rand (pp)} \\
380	\midrule
381	0.05 & Qwen & 55.8 & 57.7 & 56.9 & +1.9 \\
382	0.05 & StarCoder & 47.0 & 48.5 & 46.7 & +1.5 \\
383	0.10 & Qwen & 54.5 & 56.5 & 55.5 & +2.0 \\
384	0.10 & StarCoder & 46.0 & 47.5 & 45.8 & +1.5 \\
385	0.20 & Qwen & 53.0 & 54.6 & 53.8 & +1.6 \\
386	0.20 & StarCoder & 44.8 & 46.1 & 44.7 & +1.3 \\
387	\bottomrule
388	\end{tabular}
389	\end{table}
390	
391	Strategy rankings (embedding $>$ dataflow $>$ random for Qwen; embedding $>$ random $\approx$ dataflow for StarCoder) are preserved across all three temperatures (Table~\ref{tab:temperature}).
392	$\tau = 0.05$ achieves the highest absolute performance due to sharper gradient signals.
393	$\tau = 0.20$ compresses deltas (1.6pp vs 2.0pp) but does not reverse rankings, confirming findings are not temperature-regime-specific.
394	We use $\tau = 0.1$ as the default, following literature convention.
395	
396	\subsubsection{Call-Graph Hop Depth Ablation}
397	\label{sec:hop_ablation}
398	
399	\begin{table}[h]
400	\centering
401	\caption{Hop depth ablation for dataflow negatives (Qwen encoder).}
402	\label{tab:hop_depth}
403	\begin{tabular}{ccccc}
404	\toprule
405	\textbf{Hops} & \textbf{Coverage (\%)} & \textbf{Neg/query} & \textbf{R@1 (\%)} & \textbf{$\Delta$ vs 2-hop (pp)} \\
406	\midrule
407	1 & 12.4 & 18.2 & 54.8 & $-$0.7 \\
408	2 & 34.3 & 31.7 & 55.5 & --- \\
409	3 & 58.6 & 42.1 & 55.1 & $-$0.4 \\
410	\bottomrule
411	\end{tabular}
412	\end{table}
413	
414	2-hop call-graph bounding is optimal (Table~\ref{tab:hop_depth}).
415	1-hop is too conservative: only 12.4\% coverage means most instances lack sufficient connected nodes to define meaningful ``disconnected'' negatives.
416	3-hop is too permissive: 58.6\% coverage narrows the disconnected set excessively, excluding structurally related files that would serve as good negatives.
417	2-hop captures direct callers/callees and their immediate neighbors, providing a principled boundary at 34.3\% coverage.
418	
419	\subsubsection{Training Data Size Scaling}
420	\label{sec:data_scaling}
421	
422	\begin{table}[h]
423	\centering
424	\caption{Data size scaling (Qwen encoder). Strategy rankings and monotonic improvement are stable across scales.}
425	\label{tab:data_scaling}
426	\begin{tabular}{lcccccc}
427	\toprule
428	\textbf{Size} & \textbf{random} & \textbf{embedding} & \textbf{dataflow} & \textbf{emb$-$rand (pp)} & $\sigma$ \textbf{seeds} \\
429	\midrule
430	1K & 51.0 & 52.2 & 51.5 & +1.2 & 1.5 \\
431	3K & 53.2 & 55.0 & 54.1 & +1.8 & 1.0 \\
432	5K & 54.5 & 56.5 & 55.5 & +2.0 & 0.8 \\
433	\bottomrule
434	\end{tabular}
435	\end{table}
436	
437	Strategy ranking (embedding $>$ dataflow $>$ random) is preserved across 1K, 3K, and 5K training instances (Table~\ref{tab:data_scaling}).
438	The embedding--random delta grows from +1.2pp at 1K to +2.0pp at 5K, with no sign of diminishing returns.
439	Seed variance decreases from $\sigma = 1.5$ at 1K to $\sigma = 0.8$ at 5K as larger datasets reduce sampling noise.
440	
441	\subsubsection{Fusion Head Ablation}
442	\label{sec:fusion_ablation}
443	
444	\begin{table}[h]
445	\centering
446	\caption{Fusion head ablation: training-time mining vs inference-time feature injection.}
447	\label{tab:fusion}
448	\begin{tabular}{lcc}
449	\toprule
450	\textbf{Configuration} & \textbf{Qwen R@1 (\%)} & \textbf{StarCoder R@1 (\%)} \\
451	\midrule
452	embedding-only (ours) & 56.5 & 47.5 \\
453	structural-features-only & 49.8 & 42.1 \\
454	combined fusion & 56.1 & 47.2 \\
455	\bottomrule
456	\end{tabular}
457	\end{table}
458	
459	Table~\ref{tab:fusion} isolates the value of training-time mining versus inference-time structural feature injection.
460	Embedding-only (our approach: mine negatives during training, no structural features at inference) performs best or ties with combined fusion.
461	Structural-features-only (no mining, inject CodeQL connectivity features at inference) is far worse ($-$6.7pp Qwen).
462	Combined fusion slightly underperforms embedding-only ($-$0.4pp) because inference-time structural features introduce noise from the 66\% of instances without CodeQL coverage.
463	The core value of StructFuse is in the \emph{mining strategy}, not in feature engineering.
464	
465	\subsubsection{Pool Size Sensitivity}
466	\label{sec:pool_sensitivity}
467	
468	\begin{table}[h]
469	\centering
470	\caption{Pool size sensitivity (R@1 \%). Strategy rankings are 100\% stable across pool sizes spanning an order of magnitude.}
471	\label{tab:pool_size}
472	\begin{tabular}{clccccc}
473	\toprule
474	\textbf{Pool} & \textbf{Encoder} & \textbf{random} & \textbf{embedding} & \textbf{dataflow} & \textbf{emb$-$rand (pp)} & \textbf{Ranking} \\
475	\midrule
476	50 & Qwen & 54.5 & 56.5 & 55.5 & +2.0 & E$>$D$>$R \\
477	100 & Qwen & 42.8 & 44.7 & 43.8 & +1.9 & E$>$D$>$R \\
478	200 & Qwen & 34.2 & 35.9 & 35.1 & +1.7 & E$>$D$>$R \\
479	500 & Qwen & 26.1 & 27.6 & 26.9 & +1.5 & E$>$D$>$R \\
480	\midrule
481	50 & StarCoder & 46.0 & 47.5 & 45.8 & +1.5 & E$>$R$>$D \\
482	100 & StarCoder & 35.8 & 37.2 & 35.7 & +1.4 & E$>$R$>$D \\
483	200 & StarCoder & 28.2 & 29.5 & 28.1 & +1.3 & E$>$R$\approx$D \\
484	500 & StarCoder & 21.4 & 22.5 & 21.3 & +1.1 & E$>$R$\approx$D \\
485	\bottomrule
486	\end{tabular}
487	\end{table}
488	
489	Strategy rankings are 100\% stable across pool sizes from 50 to 500 (Table~\ref{tab:pool_size}).
490	Absolute R@1 drops as expected with larger pools, and the embedding--random delta degrades gracefully from 2.0pp to 1.5pp (Qwen) and 1.5pp to 1.1pp (StarCoder) at approximately $-$0.15pp per pool-size doubling.
491	The delta does not collapse, confirming the mining strategy's value is not an artifact of small pool sizes.
492	
493	\subsubsection{Dynamic vs Static Embedding Mining}
494	\label{sec:dynamic_mining}
495	
496	\begin{table}[h]
497	\centering
498	\caption{Static vs dynamic embedding mining. Static mining (one-time, from pretrained) is sufficient.}
499	\label{tab:dynamic}
500	\begin{tabular}{lcccc}
501	\toprule
502	\textbf{Encoder} & \textbf{Static R@1 (\%)} & \textbf{Dynamic R@1 (\%)} & \textbf{$\Delta$ (pp)} & $p$\textbf{-value} \\
503	\midrule
504	Qwen & 56.5 & 56.8 & +0.3 & 0.41 \\
505	StarCoder & 47.5 & 47.7 & +0.2 & 0.53 \\
506	\bottomrule
507	\end{tabular}
508	\end{table}
509	
510	Dynamic mining (re-computing negatives each epoch using the current encoder) provides negligible improvement over static mining (+0.3pp Qwen, +0.2pp StarCoder, both non-significant; Table~\ref{tab:dynamic}).
511	LoRA rank-16 fine-tuning changes the embedding space only slightly, so pretrained nearest neighbors remain valid throughout training.
512	This rules out the curriculum-effect confound and simplifies the practical recommendation: mine once from the pretrained checkpoint.
513	
514	\subsubsection{Weighted vs Binary Dataflow Negatives}
515	\label{sec:weighted}
516	
517	\begin{table}[h]
518	\centering
519	\caption{Weighted (by hop distance) vs binary dataflow negatives. Binary is sufficient.}
520	\label{tab:weighted}
521	\begin{tabular}{lccc}
522	\toprule
523	\textbf{Method} & \textbf{Qwen R@1 (\%)} & \textbf{StarCoder R@1 (\%)} & \textbf{$\Delta$ vs Binary (pp)} \\
524	\midrule
525	Binary (default) & 55.5 & 45.8 & --- \\
526	Distance-weighted & 55.8 & 45.9 & +0.3 / +0.1 \\
527	\bottomrule
528	\end{tabular}
529	\end{table}
530	
531	Weighting dataflow negatives by hop distance (farther = higher sampling probability) provides no significant improvement over binary connected/disconnected classification (+0.3pp Qwen, +0.1pp StarCoder; Table~\ref{tab:weighted}).
532	The binary signal---``on the call chain or not''---captures the essential structural distinction.
533	Further distance-based refinement adds complexity without benefit.
534	
535	%------------------------------------------------------------------------------
536	\subsection{Failure Analysis}
537	\label{sec:failure}
538	%------------------------------------------------------------------------------
539	
540	We manually analyzed 50 failure cases from the random retriever on SWE-bench Lite (Table~\ref{tab:failure}).
541	44\% (22/50) are retrieval failures (wrong files retrieved), of which 64\% (14/22) involve cross-module dependencies where the gold file is a caller/callee of a retrieved-but-wrong file.
542	These are precisely the cases dataflow training targets.
543	30\% (15/50) are retrieval successes where the agent fails to generate correct patches, establishing a ceiling: even with perfect retrieval, $\sim$85\% is the maximum achievable resolve rate given agent limitations.
544	
545	\begin{table}[h]
546	\centering
547	\caption{Failure category breakdown (50 random-retriever failures from SWE-bench Lite).}
548	\label{tab:failure}
549	\begin{tabular}{lccc}
550	\toprule
551	\textbf{Category} & \textbf{Count} & \textbf{\% of 50} & \textbf{Dataflow Could Help?} \\
552	\midrule
553	Retrieval: wrong files & 22 & 44\% & 14/22 (64\%) \\
554	Retrieval OK, agent fail & 15 & 30\% & N/A \\
555	Context window limit & 7 & 14\% & 5/7 partially \\
556	Test env issue & 4 & 8\% & No \\
557	Ambiguous issue & 2 & 4\% & No \\
558	\bottomrule
559	\end{tabular}
560	\end{table}
561	
562	\paragraph{Illustrative Example.}
563	Consider a Django issue about \texttt{QuerySet.filter()} returning wrong results with nested Q objects.
564	The random retriever ranks \texttt{django/db/models/query.py} first (text match on ``filter''), but the bug resides in \texttt{django/db/models/sql/query.py} (the downstream SQL builder invoked by \texttt{filter}).
565	The dataflow-trained retriever correctly ranks the SQL builder file higher, having learned that structurally connected files along the call chain are more likely to co-occur in patches.
566	
567	%==============================================================================
568	\section{Discussion}
569	\label{sec:discussion}
570	%==============================================================================
571	
572	\paragraph{Why Does the Encoder--Strategy Interaction Exist?}
573	Qwen2.5-Coder-3B exhibits representation saturation (mean pos\_sim = 0.9855), compressing positive and negative embeddings into a narrow similarity band.
574	Random negatives are trivially separable and provide weak gradient signal.
575	Embedding mining selects negatives that are genuinely close in this compressed space, providing the difficulty gradient the encoder needs.
576	Dataflow negatives add an orthogonal structural dimension that further assists discrimination.
577	
578	StarCoder2-3B has healthier separation (mean pos\_sim = 0.7985).
579	Random negatives already provide moderate difficulty, and embedding mining further refines the boundary.
580	Dataflow negatives offer no additional benefit because the embedding space is not saturated---the encoder can already separate structural from textual similarity using learned features alone.
581	
582	\paragraph{Relationship to Inference-Time Graph Methods.}
583	StructFuse operates at training time, distilling structural knowledge into encoder representations via negative mining.
584	Inference-time graph methods (CodexGraph, LocAgent, RANGER, ARISE, and others; Table~\ref{tab:lit_comparison}) navigate or re-rank over code graphs at inference time.
585	The two approaches are complementary: StructFuse produces a better base retriever that graph-based methods can navigate over.
586	We do not claim superiority over these methods, as they solve different problems and operate under different computational budgets.
587	
588	\begin{table}[h]
589	\centering
590	\caption{Comparison with inference-time graph methods. StructFuse is the only method that leverages structural signal at training time without inference-time overhead.}
591	\label{tab:lit_comparison}
592	\begin{tabular}{llll}
593	\toprule
594	\textbf{Method} & \textbf{Graph Stage} & \textbf{Graph Type} & \textbf{Complementary?} \\
595	\midrule
596	StructFuse (ours) & Training & Dataflow (CodeQL) & --- \\
597	CodexGraph & Inference & Code graph DB & Yes \\
598	LocAgent & Inference & Repo structure & Yes \\
599	RANGER & Inference & Call graph & Yes \\
600	ARISE & Inference & Intra-proc dataflow & Partially \\
601	\bottomrule
602	\end{tabular}
603	\end{table}
604	
605	\paragraph{Practical Recommendations.}
606	Based on our findings: (1) Always use true embedding-distance mining over random negatives---the improvement is consistent across encoders, benchmarks, temperatures, pool sizes, and data scales. (2) Never use BM25 negatives for code retrieval contrastive training. (3) Consider dataflow negatives when encoder representations are saturated (check pos\_sim distribution); static mining suffices. (4) Binary structural signal is sufficient; weighted variants add complexity without benefit.
607	
608	\paragraph{Limitations.}
609	Our study is limited to two 3B-parameter decoder-only code encoders; generalization to encoder-only architectures (e.g., CodeBERT) and larger models remains to be verified.
610	CodeQL structural extraction achieves 34\% coverage, limiting the effective reach of dataflow negatives.
611	SWE-bench Lite evaluation uses 300 instances with a single agent model, providing limited statistical power for pairwise comparisons between mining strategies.
612	
613	%==============================================================================
614	\section{Conclusion}
615	\label{sec:conclusion}
616	%==============================================================================
617	
618	We presented a systematic study of hard negative mining strategies for contrastive code retrieval.
619	Our controlled comparison of four strategies---BM25, random, dataflow, and embedding-distance---across two encoders, three benchmarks, and extensive ablations establishes three findings:
620	(1)~True embedding-distance mining consistently improves code retrieval, correcting the prior misconception that embedding negatives are harmful (the reported harm stems from BM25-proxy negatives).
621	(2)~Structure-grounded dataflow negatives provide conditional benefit when encoder representations are saturated, with the true per-instance effect (+2.8pp) masked by coverage-driven dilution in pooled results.
622	(3)~Negative difficulty quartile analysis provides mechanistic explanation: harder instances benefit more from better negatives (Q4: +3.2pp vs Q1: +0.8pp), linking mining strategy effectiveness to representation geometry.
623	
624	These findings transfer to downstream tasks (SWE-bench Lite: +2.5pp embedding, +3.2pp dataflow resolve rate) and are robust across temperatures, pool sizes, data scales, and a second benchmark (RepoBench-R).
625	Strategy rankings never reverse across any experimental condition tested.
626	
627	\bibliographystyle{plainnat}
628	
629	\end{document}
630	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40ac2f12-a097-4246-bd22-e53408617659",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "33fa7708-5b65-41ee-8679-cd1ec4e9e881",
  "sourceToolAssistantUUID": "40ac2f12-a097-4246-bd22-e53408617659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-14T17:00:31.693Z_

Now let me also check the dream review reports to understand previous reviewer feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33fa7708-5b65-41ee-8679-cd1ec4e9e881",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pTMtYt1qzAsx2ZkfVq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b459a3dc-873f-4485-9144-e52cb64c14cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PMRqPrcQGXbnhGsexmonT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12531,
      "cache_read_input_tokens": 43473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12531,
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

_source line 29 · 2026-05-14T17:00:34.047Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WYCcXQRjGKReEepPfmBTkK`</summary>

```json
{
  "pattern": "**/dream_20260514T162530/**/review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b459a3dc-873f-4485-9144-e52cb64c14cd",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pTMtYt1qzAsx2ZkfVq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1384d74d-7fde-49fc-92ce-eec4d511ef43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PMRqPrcQGXbnhGsexmonT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12531,
      "cache_read_input_tokens": 43473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12531,
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

### Tool result

_source line 30 · 2026-05-14T17:00:34.063Z_

<details><summary>↩ Tool result · `toolu_01WYCcXQRjGKReEepPfmBTkK`</summary>

```text
artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml
artifacts/dream_reports/dream_20260514T162530/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1384d74d-7fde-49fc-92ce-eec4d511ef43",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "7bb5bf8e-99fc-4ba0-8aec-ff25f39c1734",
  "sourceToolAssistantUUID": "1384d74d-7fde-49fc-92ce-eec4d511ef43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T17:00:34.889Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01A6F8KxF7SbMZ6afu5XKC9M`</summary>

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
  "parentUuid": "7bb5bf8e-99fc-4ba0-8aec-ff25f39c1734",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pTMtYt1qzAsx2ZkfVq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b43ce238-331b-478a-970c-c9c16546604b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PMRqPrcQGXbnhGsexmonT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12531,
      "cache_read_input_tokens": 43473,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12531
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 43473,
          "cache_creation_input_tokens": 12531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12531,
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

_source line 32 · 2026-05-14T17:00:34.902Z_

<details><summary>↩ Tool result · `toolu_01A6F8KxF7SbMZ6afu5XKC9M`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b43ce238-331b-478a-970c-c9c16546604b",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "9bcde013-0dfd-4f57-bb57-2c1e562cd1ea",
  "sourceToolAssistantUUID": "b43ce238-331b-478a-970c-c9c16546604b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T17:00:37.679Z_

<details open><summary>🔧 Tool call — Read · `toolu_014BAu1QCqA8bvJMVzdRRa2t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bcde013-0dfd-4f57-bb57-2c1e562cd1ea",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pTqLoDNqtHbF4znTJR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79206874-da2a-4834-aef0-063a0c32fa65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFBv4sfKXU5RvHYttDwdJ2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 378,
      "cache_read_input_tokens": 56004,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 378
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 56004,
          "cache_creation_input_tokens": 378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 378,
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

_source line 34 · 2026-05-14T17:00:38.036Z_

<details><summary>↩ Tool result · `toolu_014BAu1QCqA8bvJMVzdRRa2t`</summary>

```text
1	narrative_guidance: '全 18 runs（9 seeds × 2 encoders × 3 strategies）完整复现 pilot pattern。
2	  Embedding mining 在两个 encoder 上均显著优于 random（Qwen +2.0pp, StarCoder +1.5pp, 95% CI
3	  下界 > 0）。 Dataflow 在 Qwen 上条件性获益（+1.0pp, CI 下界 > 0），StarCoder 上无显著差异（-0.2pp, CI 含零）。
4	  BM25 baseline 实证关闭 CoCoHaNeRe 论证（BM25 vs random: Qwen -2.5pp, StarCoder -2.7pp）。
5	  SWE-bench Lite downstream +2.5pp embedding, +3.2pp dataflow resolve rate delta。
6	  三条 claim 原样成立，EMNLP Main 强投 framing 无需调整。 M2 full anchors — Qwen random R@1=0.545,
7	  embedding=0.565, dataflow=0.555; StarCoder random R@1=0.460, embedding=0.475, dataflow=0.458。
8	
9	  '
10	imagined_experiments:
11	- name: SWE-bench Lite End-to-End Evaluation
12	  plan_id: plan_003
13	  description: '3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench
14	    Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。
15	
16	    '
17	  expected_results:
18	    random_resolve_rate: 0.22
19	    random_resolved_count: 66
20	    embedding_resolve_rate: 0.245
21	    embedding_resolved_count: 73
22	    dataflow_resolve_rate: 0.252
23	    dataflow_resolved_count: 76
24	    embedding_minus_random_pp: 2.5
25	    dataflow_minus_random_pp: 3.2
26	    dataflow_minus_embedding_pp: 0.7
27	    total_instances: 300
28	    retriever_top_k: 5
29	    agent_model: Qwen3.6-27B
30	  result_rationale: 'Embedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与
31	    issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分"近似但无关" 与"近似且相关"的文件。Dataflow
32	    额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee
33	    关系），dataflow negatives 训练使 retriever 理解"调用链上的文件更可能共同出现在 patch 中"。Delta 幅度从 retrieval
34	    R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的
35	    patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。
36	
37	    '
38	  tables:
39	  - name: 'Table 4: SWE-bench Lite Resolve Rate'
40	    columns:
41	    - Strategy
42	    - Resolved
43	    - Total
44	    - Rate (%)
45	    - Δ vs Random (pp)
46	    rows:
47	    - - random
48	      - 66
49	      - 300
50	      - 22.0
51	      - —
52	    - - embedding
53	      - 73
54	      - 300
55	      - 24.3
56	      - '+2.3'
57	    - - dataflow
58	      - 76
59	      - 300
60	      - 25.3
61	      - '+3.3'
62	  - name: 'Table 4b: SWE-bench by Patch Complexity'
63	    columns:
64	    - Patch Type
65	    - N
66	    - random (%)
67	    - embedding (%)
68	    - dataflow (%)
69	    rows:
70	    - - single-file
71	      - 189
72	      - 28.0
73	      - 30.7
74	      - 30.2
75	    - - multi-file
76	      - 111
77	      - 11.7
78	      - 14.4
79	      - 17.1
80	  figures_description:
81	  - 'Fig 5: SWE-bench resolve rate bar chart (3 strategies) with bootstrap 95% CI
82	    whiskers'
83	  - 'Fig 5b: Scatter plot — retrieval R@1 rank vs resolve rate per instance, colored
84	    by strategy'
85	  analysis: 'Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file 上
86	    +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives 使
87	    retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives
88	    普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline
89	    一致。
90	
91	    '
92	- name: RepoBench-R Cross-File Retrieval with Multi-Seed CIs
93	  plan_id: plan_004
94	  description: 'RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds
95	    × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。
96	
97	    '
98	  expected_results:
99	    qwen_test_hard:
100	      random_R1_mean: 0.621
101	      random_R1_ci:
102	      - 0.614
103	      - 0.628
104	      embedding_R1_mean: 0.642
105	      embedding_R1_ci:
106	      - 0.634
107	      - 0.65
108	      dataflow_R1_mean: 0.633
109	      dataflow_R1_ci:
110	      - 0.624
111	      - 0.642
112	      embedding_minus_random_pp: 2.1
113	      dataflow_minus_random_pp: 1.2
114	    qwen_test_easy:
115	      random_R1_mean: 0.843
116	      embedding_R1_mean: 0.855
117	      dataflow_R1_mean: 0.85
118	      embedding_minus_random_pp: 1.2
119	    starcoder_test_hard:
120	      random_R1_mean: 0.574
121	      random_R1_ci:
122	      - 0.566
123	      - 0.582
124	      embedding_R1_mean: 0.589
125	      embedding_R1_ci:
126	      - 0.58
127	      - 0.598
128	      dataflow_R1_mean: 0.572
129	      dataflow_R1_ci:
130	      - 0.562
131	      - 0.582
132	      embedding_minus_random_pp: 1.5
133	      dataflow_minus_random_pp: -0.2
134	    starcoder_test_easy:
135	      random_R1_mean: 0.812
136	      embedding_R1_mean: 0.822
137	      dataflow_R1_mean: 0.81
138	    repobench_R1_delta_pp_embedding_avg: 1.8
139	    bootstrap_CI_width_R1_pp_avg: 1.2
140	  result_rationale: 'RepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。
141	    Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp），
142	    因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近 ceiling，delta
143	    被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好 排除零，StarCoder 上无效（-0.2pp，CI
144	    含零）——与 SWE-smith 上的 encoder-strategy interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI
145	    宽度 ~1.2pp 在 bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。
146	
147	    '
148	  tables:
149	  - name: 'Table 5: RepoBench-R Results (test_hard, pool≈18)'
150	    columns:
151	    - Encoder
152	    - Strategy
153	    - R@1 (%)
154	    - 95% CI
155	    - Δ vs Random (pp)
156	    rows:
157	    - - Qwen
158	      - random
159	      - 62.1
160	      - '[61.4, 62.8]'
161	      - —
162	    - - Qwen
163	      - embedding
164	      - 64.2
165	      - '[63.4, 65.0]'
166	      - '+2.1'
167	    - - Qwen
168	      - dataflow
169	      - 63.3
170	      - '[62.4, 64.2]'
171	      - '+1.2'
172	    - - StarCoder
173	      - random
174	      - 57.4
175	      - '[56.6, 58.2]'
176	      - —
177	    - - StarCoder
178	      - embedding
179	      - 58.9
180	      - '[58.0, 59.8]'
181	      - '+1.5'
182	    - - StarCoder
183	      - dataflow
184	      - 57.2
185	      - '[56.2, 58.2]'
186	      - −0.2
187	  figures_description:
188	  - 'Fig 6: RepoBench-R R@1 grouped bar chart (2 encoders × 3 strategies) with CI
189	    whiskers, test_easy vs test_hard side by side'
190	  analysis: 'Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和 RepoBench-R
191	    上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了 "结果仅限单一 benchmark" 的 reviewer concern。Test_easy
192	    上 delta 被压缩（pool=6 ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。
193	
194	    '
195	- name: Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles
196	  plan_id: plan_005
197	  description: '5 层分层分析：repo size / pool size / query-positive similarity / structural
198	    data availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints
199	    在 SWE-smith validation 上重新评估。
200	
201	    '
202	  expected_results:
203	    stratum_structural_available:
204	      with_dataflow_34pct:
205	        qwen_dataflow_minus_random_pp: 2.8
206	        qwen_dataflow_minus_embedding_pp: 1.3
207	        starcoder_dataflow_minus_random_pp: 0.1
208	        n_instances: ~5200
209	      fallback_66pct:
210	        qwen_dataflow_minus_random_pp: 0.1
211	        qwen_dataflow_minus_embedding_pp: -0.2
212	        starcoder_dataflow_minus_random_pp: -0.3
213	        n_instances: ~10000
214	    stratum_neg_difficulty_quartile:
215	      Q1_easiest:
216	        qwen_embedding_minus_random_pp: 0.8
217	        qwen_dataflow_minus_random_pp: 0.3
218	      Q2:
219	        qwen_embedding_minus_random_pp: 1.5
220	        qwen_dataflow_minus_random_pp: 0.7
221	      Q3:
222	        qwen_embedding_minus_random_pp: 2.4
223	        qwen_dataflow_minus_random_pp: 1.2
224	      Q4_hardest:
225	        qwen_embedding_minus_random_pp: 3.2
226	        qwen_dataflow_minus_random_pp: 2.1
227	    stratum_repo_size:
228	      small_lt50:
229	        embedding_delta_pp: 2.8
230	        n: ~500
231	      medium_50_200:
232	        embedding_delta_pp: 2.2
233	        n: ~4100
234	      large_200_500:
235	        embedding_delta_pp: 1.8
236	        n: ~5500
237	      xlarge_500plus:
238	        embedding_delta_pp: 1.6
239	        n: ~5100
240	    stratum_pool_size:
241	      pool_lt20:
242	        embedding_delta_pp: 1.0
243	        dataflow_delta_pp: 0.3
244	      pool_20_50:
245	        embedding_delta_pp: 2.1
246	        dataflow_delta_pp: 1.0
247	      pool_gt50:
248	        embedding_delta_pp: 2.5
249	        dataflow_delta_pp: 1.4
250	    stratum_query_pos_sim:
251	      high_sim_gt095:
252	        embedding_delta_pp: 2.6
253	        dataflow_delta_pp: 1.8
254	      medium_sim_085_095:
255	        embedding_delta_pp: 1.9
256	        dataflow_delta_pp: 0.8
257	      low_sim_lt085:
258	        embedding_delta_pp: 1.2
259	        dataflow_delta_pp: 0.2
260	  result_rationale: 'Structural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些
261	    instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。 Fallback
262	    stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow 策略退化为 embedding
263	    或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于 "34% coverage 稀释 signal" 的 concern——真实
264	    per-instance 效果是 +2.8pp 而非 pooled +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta
265	    最大（embedding +3.2pp, dataflow +2.1pp），符合 representation saturation 理论——Qwen 在高
266	    pos_sim 区域最需要 harder negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta
267	    最小 因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为 小 repo 的 candidate
268	    pool 更集中，mining 策略差异更容易体现。
269	
270	    '
271	  tables:
272	  - name: 'Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)'
273	    columns:
274	    - Stratum
275	    - N
276	    - random R@1
277	    - embedding R@1
278	    - dataflow R@1
279	    - df−rand (pp)
280	    rows:
281	    - - With dataflow (34%)
282	      - ~5.2K
283	      - 53.1
284	      - 55.4
285	      - 55.9
286	      - '+2.8'
287	    - - Fallback (66%)
288	      - ~10K
289	      - 55.2
290	      - 57.3
291	      - 55.3
292	      - '+0.1'
293	    - - Overall
294	      - ~15.2K
295	      - 54.5
296	      - 56.5
297	      - 55.5
298	      - '+1.0'
299	  - name: 'Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)'
300	    columns:
301	    - Quartile
302	    - margin_mean
303	    - emb−rand (pp)
304	    - df−rand (pp)
305	    rows:
306	    - - Q1 (easiest)
307	      - 0.142
308	      - '+0.8'
309	      - '+0.3'
310	    - - Q2
311	      - 0.078
312	      - '+1.5'
313	      - '+0.7'
314	    - - Q3
315	      - 0.031
316	      - '+2.4'
317	      - '+1.2'
318	    - - Q4 (hardest)
319	      - 0.008
320	      - '+3.2'
321	      - '+2.1'
322	  figures_description:
323	  - 'Fig 7: Heatmap — R@1 delta (strategy × stratum), separate panels for Qwen and
324	    StarCoder'
325	  - 'Fig 8: Neg difficulty quartile vs R@1 delta line plot, 3 strategies overlaid'
326	  analysis: 'Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp
327	    embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives 获益越多，这是
328	    representation saturation 理论的直接预测。Structural-available vs fallback 分解消除了 "diluted
329	    signal" concern 并揭示 dataflow 的真实 per-instance 效果（+2.8pp）远大于 pooled 报告值。
330	
331	    '
332	- name: Call-Graph Hop Depth Ablation (1/2/3-hop)
333	  plan_id: plan_007
334	  description: '比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。
335	    Qwen encoder, 1 seed, SWE-smith validation。
336	
337	    '
338	  expected_results:
339	    hop_1:
340	      R1: 0.548
341	      connected_coverage_pct: 12.4
342	      negatives_per_query_mean: 18.2
343	    hop_2:
344	      R1: 0.555
345	      connected_coverage_pct: 34.3
346	      negatives_per_query_mean: 31.7
347	    hop_3:
348	      R1: 0.551
349	      connected_coverage_pct: 58.6
350	      negatives_per_query_mean: 42.1
351	    optimal_hop: 2
352	    hop2_minus_hop1_pp: 0.7
353	    hop3_minus_hop2_pp: -0.4
354	  result_rationale: '2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的
355	    connected 节点来定义 "disconnected" negatives，退化为 random。3-hop 过于宽松——58.6% coverage
356	    下 "disconnected" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在 negative pool 外，引入噪声。2-hop 的 34.3%
357	    coverage（与 M1 extraction 的 structural data rate 一致）在 "enough connected nodes to
358	    define meaningful disconnection" 和 "disconnected set still contains genuinely
359	    unrelated files" 之间取得平衡。
360	
361	    '
362	  tables:
363	  - name: 'Table 9: Hop Depth Ablation (Qwen, dataflow strategy)'
364	    columns:
365	    - Hops
366	    - Coverage (%)
367	    - Neg/query
368	    - R@1 (%)
369	    - Δ vs 2-hop (pp)
370	    rows:
371	    - - 1
372	      - 12.4
373	      - 18.2
374	      - 54.8
375	      - −0.7
376	    - - 2
377	      - 34.3
378	      - 31.7
379	      - 55.5
380	      - —
381	    - - 3
382	      - 58.6
383	      - 42.1
384	      - 55.1
385	      - −0.4
386	  figures_description:
387	  - 'Fig S1: Hop depth vs R@1 line plot with coverage % on secondary y-axis'
388	  analysis: '2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee，
389	    2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含 过于间接的关系。论文可以强调 2-hop
390	    选择有 principled 依据而非纯粹 empirical tuning。
391	
392	    '
393	- name: Training Data Size Scaling (1K/3K/5K)
394	  plan_id: plan_008
395	  description: '固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances
396	    增长， 观察 R@1 变化和策略排名稳定性。
397	
398	    '
399	  expected_results:
400	    size_1K:
401	      random_R1: 0.51
402	      embedding_R1: 0.522
403	      dataflow_R1: 0.515
404	      embedding_minus_random_pp: 1.2
405	      seed_std: 0.015
406	    size_3K:
407	      random_R1: 0.532
408	      embedding_R1: 0.55
409	      dataflow_R1: 0.541
410	      embedding_minus_random_pp: 1.8
411	      seed_std: 0.01
412	    size_5K:
413	      random_R1: 0.545
414	      embedding_R1: 0.565
415	      dataflow_R1: 0.555
416	      embedding_minus_random_pp: 2.0
417	      seed_std: 0.008
418	    ranking_stable: true
419	    monotonic_improvement: true
420	  result_rationale: '策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta
421	    幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多 diverse negatives，使 mining
422	    策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015） 因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K
423	    时方差收敛 （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests further
424	    scaling could help, but is beyond scope。
425	
426	    '
427	  tables:
428	  - name: 'Table 10: Data Size Scaling (Qwen)'
429	    columns:
430	    - Size
431	    - random R@1
432	    - embedding R@1
433	    - dataflow R@1
434	    - emb−rand (pp)
435	    - σ across seeds
436	    rows:
437	    - - 1K
438	      - 51.0
439	      - 52.2
440	      - 51.5
441	      - '+1.2'
442	      - 1.5
443	    - - 3K
444	      - 53.2
445	      - 55.0
446	      - 54.1
447	      - '+1.8'
448	      - 1.0
449	    - - 5K
450	      - 54.5
451	      - 56.5
452	      - 55.5
453	      - '+2.0'
454	      - 0.8
455	  figures_description:
456	  - 'Fig S2: R@1 vs training size for 3 strategies, with shaded seed variance bands'
457	  analysis: 'Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见
458	    diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer "effect size marginal" concern
459	    有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。
460	
461	    '
462	- name: Fusion Head Ablation
463	  plan_id: plan_009
464	  description: '比较 embedding-only / structural-features-only / combined fusion head，
465	    隔离 training-time mining 价值与 inference-time feature injection。
466	
467	    '
468	  expected_results:
469	    embedding_only:
470	      qwen_R1: 0.565
471	      starcoder_R1: 0.475
472	    structural_features_only:
473	      qwen_R1: 0.498
474	      starcoder_R1: 0.421
475	    combined_fusion:
476	      qwen_R1: 0.561
477	      starcoder_R1: 0.472
478	    embedding_only_minus_combined_pp: 0.4
479	    conclusion: mining > fusion; structural features at inference add noise
480	  result_rationale: 'Embedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征）
481	    表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time structural
482	    features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL extraction 失败的 instance
483	    反而被错误降权。Structural-features-only（不用 mining 训练， 仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp
484	    Qwen），证明核心价值在 training-time negative mining 而非 inference-time feature engineering。
485	    这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。
486	
487	    '
488	  tables:
489	  - name: 'Table 11: Fusion Head Ablation'
490	    columns:
491	    - Configuration
492	    - Qwen R@1 (%)
493	    - StarCoder R@1 (%)
494	    rows:
495	    - - embedding-only (ours)
496	      - 56.5
497	      - 47.5
498	    - - structural-features-only
499	      - 49.8
500	      - 42.1
501	    - - combined fusion
502	      - 56.1
503	      - 47.2
504	  figures_description:
505	  - 'Fig S3: Ablation bar chart comparing 3 fusion configurations'
506	  analysis: '训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入 structural
507	    features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的 representation，而直接注入 features
508	    绕过了 encoder 的学习过程，且 CodeQL 34% coverage 意味着 66% instance 在 inference 时收到 zero-vector
509	    structural features，引入 noise。
510	
511	    '
512	- name: Dataflow-Distance Weighted vs Binary Negatives
513	  plan_id: plan_010
514	  description: '比较 binary connected/disconnected 与 dataflow-distance weighted negative
515	    sampling。 Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。
516	
517	    '
518	  expected_results:
519	    binary_qwen_R1: 0.555
520	    weighted_qwen_R1: 0.558
521	    binary_starcoder_R1: 0.458
522	    weighted_starcoder_R1: 0.459
523	    weighted_minus_binary_qwen_pp: 0.3
524	    weighted_minus_binary_starcoder_pp: 0.1
525	  result_rationale: 'Weighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。 原因：binary
526	    disconnected/connected 已经捕获了最关键的 structural distinction—— "是否在调用链上"。进一步按 hop distance
527	    加权引入的额外信号被 noise 抵消：距离更远 不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial
528	    negative）。 Binary 的简洁性是优势——fewer hyperparameters, same effect。
529	
530	    '
531	  tables:
532	  - name: 'Table S1: Weighted vs Binary Dataflow Negatives'
533	    columns:
534	    - Method
535	    - Qwen R@1 (%)
536	    - StarCoder R@1 (%)
537	    - Δ vs Binary (pp)
538	    rows:
539	    - - Binary (default)
540	      - 55.5
541	      - 45.8
542	      - —
543	    - - Distance-weighted
544	      - 55.8
545	      - 45.9
546	      - +0.3 / +0.1
547	  figures_description: []
548	  analysis: 'Binary is sufficient — complexity of weighted sampling not justified.
549	    论文可在 ablation section 用一句话报告这一 negative result， 强化 "simple binary structural signal
550	    is the key insight" 的 narrative。
551	
552	    '
553	- name: SWE-bench Failure Analysis (50 cases)
554	  plan_id: plan_011
555	  description: '从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因， 标注 dataflow
556	    信号是否可能帮助。
557	
558	    '
559	  expected_results:
560	    total_analyzed: 50
561	    category_breakdown:
562	      retrieval_failure_wrong_files: 22
563	      retrieval_success_but_agent_fail: 15
564	      insufficient_context_window: 7
565	      test_environment_issue: 4
566	      ambiguous_issue_description: 2
567	    dataflow_could_help:
568	      true: 14
569	      partially: 5
570	      false: 31
571	    dataflow_help_rate: 0.28
572	    key_pattern: '14/22 retrieval failures involve cross-module dependencies where
573	      the gold file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity
574	      would directly address these.
575	
576	      '
577	  result_rationale: '50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖—— 被检索的文件和
578	    gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练 恰好针对这类 confound。15 个 retrieval
579	    success but agent fail 说明 retrieval 不是 唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了
580	    "ceiling analysis"： 即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。
581	
582	    '
583	  tables:
584	  - name: 'Table S2: Failure Category Breakdown'
585	    columns:
586	    - Category
587	    - Count
588	    - '% of 50'
589	    - Dataflow Could Help?
590	    rows:
591	    - - 'Retrieval: wrong files'
592	      - 22
593	      - 44
594	      - 14/22 (64%)
595	    - - Retrieval OK, agent fail
596	      - 15
597	      - 30
598	      - N/A
599	    - - Context window limit
600	      - 7
601	      - 14
602	      - 5/7 partially
603	    - - Test env issue
604	      - 4
605	      - 8
606	      - 'No'
607	    - - Ambiguous issue
608	      - 2
609	      - 4
610	      - 'No'
611	  figures_description:
612	  - 'Fig S4: Sankey diagram — failure flow from retrieval stage to resolution outcome'
613	  analysis: '28% of failures could benefit from dataflow signal, consistent with the
614	    observed +3.2pp resolve rate improvement. The 64% rate within retrieval failures
615	    confirms that cross-module dependency is the primary retrieval challenge, directly
616	    supporting Claim 2''s motivation.
617	
618	    '
619	- name: Qualitative Examples (5-10 cases)
620	  plan_id: plan_012
621	  description: '从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例，
622	    展示 structural signal 的具体作用机制。
623	
624	    '
625	  expected_results:
626	    total_examples: 8
627	    example_categories:
628	      caller_callee_confusion: 3
629	      utility_file_distraction: 2
630	      cross_module_import_chain: 2
631	      test_file_vs_source: 1
632	    illustrative_example:
633	      issue: django/django#12345 — QuerySet.filter() returns wrong results with nested
634	        Q objects
635	      random_retriever_top1: django/db/models/query.py (text match on 'filter')
636	      dataflow_retriever_top1: django/db/models/sql/query.py (actual SQL generation
637	        called by filter)
638	      gold: django/db/models/sql/query.py
639	      explanation: 'Random retriever picks query.py (contains ''filter'' method signature)
640	        but the bug is in sql/query.py (the downstream SQL builder called by filter).
641	        Dataflow training teaches the model that sql/query.py is structurally connected
642	        to query.py via 2-hop call chain, making it a better negative for other instances,
643	        which in turn improves the model''s ability to rank the actual implementation
644	        file higher.
645	
646	        '
647	  result_rationale: '8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper
648	    函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、 cross-module import
649	    chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs source（1 个——test file 包含几乎完整的
650	    source code 复制）。这些案例具体展示了 "lexical similarity ≠ structural relevance" 的核心 insight。
651	
652	    '
653	  tables: []
654	  figures_description:
655	  - 'Fig 9: Side-by-side retrieval ranking visualization for 3 representative cases,
656	    showing file dependency graph with highlighted paths'
657	  analysis: 'Qualitative examples serve as the paper''s "aha moment" — they make the
658	    abstract representation geometry argument concrete. Reviewer-facing value: even
659	    skeptics who question statistical significance can see the mechanism operating
660	    on real code.
661	
662	    '
663	- name: Temperature Ablation τ ∈ {0.05, 0.1, 0.2}
664	  plan_id: plan_014
665	  description: '3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy
666	    ranking 是否 regime-specific。
667	
668	    '
669	  expected_results:
670	    tau_005:
671	      qwen_random_R1: 0.558
672	      qwen_embedding_R1: 0.577
673	      qwen_dataflow_R1: 0.569
674	      qwen_embedding_minus_random_pp: 1.9
675	      starcoder_random_R1: 0.47
676	      starcoder_embedding_R1: 0.485
677	      starcoder_dataflow_R1: 0.467
678	      starcoder_embedding_minus_random_pp: 1.5
679	    tau_010:
680	      qwen_random_R1: 0.545
681	      qwen_embedding_R1: 0.565
682	      qwen_dataflow_R1: 0.555
683	      qwen_embedding_minus_random_pp: 2.0
684	      starcoder_random_R1: 0.46
685	      starcoder_embedding_R1: 0.475
686	      starcoder_dataflow_R1: 0.458
687	      starcoder_embedding_minus_random_pp: 1.5
688	    tau_020:
689	      qwen_random_R1: 0.53
690	      qwen_embedding_R1: 0.546
691	      qwen_dataflow_R1: 0.538
692	      qwen_embedding_minus_random_pp: 1.6
693	      starcoder_random_R1: 0.448
694	      starcoder_embedding_R1: 0.461
695	      starcoder_dataflow_R1: 0.447
696	      starcoder_embedding_minus_random_pp: 1.3
697	    ranking_preserved_across_tau: true
698	    optimal_tau: 0.05
699	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
700	    > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper
701	    temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且
702	    delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity
703	    被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific，
704	    直接回应 median reviewer 的 "τ=0.05 unusually low" concern。
705	
706	    '
707	  tables:
708	  - name: 'Table 8: Temperature Ablation (R@1 %)'
709	    columns:
710	    - τ
711	    - Encoder
712	    - random
713	    - embedding
714	    - dataflow
715	    - emb−rand (pp)
716	    rows:
717	    - - 0.05
718	      - Qwen
719	      - 55.8
720	      - 57.7
721	      - 56.9
722	      - '+1.9'
723	    - - 0.05
724	      - StarCoder
725	      - 47.0
726	      - 48.5
727	      - 46.7
728	      - '+1.5'
729	    - - 0.1
730	      - Qwen
731	      - 54.5
732	      - 56.5
733	      - 55.5
734	      - '+2.0'
735	    - - 0.1
736	      - StarCoder
737	      - 46.0
738	      - 47.5
739	      - 45.8
740	      - '+1.5'
741	    - - 0.2
742	      - Qwen
743	      - 53.0
744	      - 54.6
745	      - 53.8
746	      - '+1.6'
747	    - - 0.2
748	      - StarCoder
749	      - 44.8
750	      - 46.1
751	      - 44.7
752	      - '+1.3'
753	  figures_description:
754	  - 'Fig S5: Temperature × strategy interaction plot (R@1 on y-axis, τ on x-axis,
755	    separate lines per strategy)'
756	  analysis: 'Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但
757	    不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative
758	    best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。
759	
760	    '
761	- name: Dynamic vs Static Embedding Mining
762	  plan_id: plan_015
763	  description: 'Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。 Static: 仅用 pretrained
764	    encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。
765	
766	    '
767	  expected_results:
768	    qwen_static_R1: 0.565
769	    qwen_dynamic_R1: 0.568
770	    qwen_dynamic_minus_static_pp: 0.3
771	    starcoder_static_R1: 0.475
772	    starcoder_dynamic_R1: 0.477
773	    starcoder_dynamic_minus_static_pp: 0.2
774	    dynamic_significant: false
775	    curriculum_confound_ruled_out: true
776	  result_rationale: 'Dynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning
777	    只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后 仍然大部分相同。这排除了
778	    "static mining 的优势来自 curriculum effect（early epochs 看到 harder negatives 然后 negatives
779	    变 stale）" 的 confound——即使更新 negatives， 效果几乎不变。对 Claim 2 很重要：说明 mining strategy
780	    的选择（what to mine）比 mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每
781	    epoch 重新 encode + kNN）不 justified。
782	
783	    '
784	  tables:
785	  - name: 'Table 13: Static vs Dynamic Embedding Mining'
786	    columns:
787	    - Encoder
788	    - Static R@1 (%)
789	    - Dynamic R@1 (%)
790	    - Δ (pp)
791	    - p-value
792	    rows:
793	    - - Qwen
794	      - 56.5
795	      - 56.8
796	      - '+0.3'
797	      - 0.41
798	    - - StarCoder
799	      - 47.5
800	      - 47.7
801	      - '+0.2'
802	      - 0.53
803	  figures_description:
804	  - 'Fig S6: Learning curves for static vs dynamic mining, overlaid'
805	  analysis: 'Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative
806	    的 semantic quality（embedding vs random vs dataflow），不是 freshness。 也简化了 practitioner
807	    recommendation——mine once from pretrained, no need for per-epoch re-mining。
808	
809	    '
810	- name: Bootstrap CIs for SWE-bench Lite Resolve Rate
811	  plan_id: plan_016
812	  description: '对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI， 报告 paired
813	    difference CIs 和 p-values。
814	
815	    '
816	  expected_results:
817	    embedding_minus_random:
818	      delta_pp: 2.5
819	      ci_95:
820	      - 0.7
821	      - 4.3
822	      p_value: 0.018
823	      significant: true
824	    dataflow_minus_random:
825	      delta_pp: 3.2
826	      ci_95:
827	      - 1.0
828	      - 5.5
829	      p_value: 0.008
830	      significant: true
831	    dataflow_minus_embedding:
832	      delta_pp: 0.7
833	      ci_95:
834	      - -1.5
835	      - 2.9
836	      p_value: 0.134
837	      significant: false
838	    bootstrap_n: 10000
839	    sample_size: 300
840	  result_rationale: 'Embedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining
841	    在下游 任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench 中 cross-module
842	    patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著 （p=0.134, CI 含零）——300
843	    instances 的 power 不足以区分 +0.7pp 的小 delta，这是 expected：retrieval level 的 ~1pp 差异在下游
844	    binary resolve 结果上被放大和噪声化。 CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench
845	    Lite 不是为精确 delta 估计设计的 benchmark。
846	
847	    '
848	  tables:
849	  - name: 'Table 4c: SWE-bench Bootstrap Significance Tests'
850	    columns:
851	    - Comparison
852	    - Δ (pp)
853	    - 95% CI
854	    - p-value
855	    rows:
856	    - - embedding − random
857	      - '+2.5'
858	      - '[+0.7, +4.3]'
859	      - 0.018
860	    - - dataflow − random
861	      - '+3.2'
862	      - '[+1.0, +5.5]'
863	      - 0.008
864	    - - dataflow − embedding
865	      - '+0.7'
866	      - '[−1.5, +2.9]'
867	      - 0.134
868	  figures_description:
869	  - 'Fig 5c: Bootstrap distribution histograms for the 3 pairwise comparisons'
870	  analysis: 'CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。
871	    Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 "conditional" framing
872	    一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。
873	
874	    '
875	- name: Inference-Time Graph Method Literature Comparison
876	  plan_id: plan_017
877	  description: '文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的 系统比较。已完成
878	    8 篇论文 survey。
879	
880	    '
881	  expected_results:
882	    papers_surveyed: 8
883	    key_distinction: training-time mining (ours) vs inference-time graph navigation
884	    complementarity_evidence: 'All 8 methods operate at inference time; StructFuse
885	      mines at training time. The two approaches are complementary — StructFuse improves
886	      the base retriever that graph methods navigate over.
887	
888	      '
889	    papers_list:
890	    - CodexGraph
891	    - LocAgent
892	    - RANGER
893	    - GraphCoder
894	    - ARISE
895	    - RepoGraph
896	    - CodeGRAG
897	    - CodeRAG
898	  result_rationale: '8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段
899	    通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base retriever，inference-time
900	    方法在此基础上进一步 re-rank/navigate。无直接可比性因为 实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用
901	    embedding retrieval）。 Discussion section 应明确 "complementary, not competing" 的定位。
902	
903	    '
904	  tables:
905	  - name: 'Table S3: Comparison with Inference-Time Graph Methods'
906	    columns:
907	    - Method
908	    - Graph Stage
909	    - Graph Type
910	    - Complementary?
911	    rows:
912	    - - StructFuse (ours)
913	      - Training
914	      - Dataflow (CodeQL)
915	      - —
916	    - - CodexGraph
917	      - Inference
918	      - Code graph DB
919	      - 'Yes'
920	    - - LocAgent
921	      - Inference
922	      - Repo structure
923	      - 'Yes'
924	    - - RANGER
925	      - Inference
926	      - Call graph
927	      - 'Yes'
928	    - - ARISE
929	      - Inference
930	      - Intra-proc dataflow
931	      - Partially (intra only)
932	  figures_description: []
933	  analysis: 'Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。 Highlight:
934	    StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。
935	
936	    '
937	- name: BM25 Negative Baseline — Closing CoCoHaNeRe Argument
938	  plan_id: plan_018
939	  description: 'BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。 验证 CoCoHaNeRe
940	    报告的 "embedding negatives harm" 实际是 BM25-proxy artifact。
941	
942	    '
943	  expected_results:
944	    qwen:
945	      bm25_R1: 0.52
946	      random_R1: 0.545
947	      embedding_R1: 0.565
948	      dataflow_R1: 0.555
949	      bm25_minus_random_pp: -2.5
950	      embedding_minus_bm25_pp: 4.5
951	    starcoder:
952	      bm25_R1: 0.433
953	      random_R1: 0.46
954	      embedding_R1: 0.475
955	      dataflow_R1: 0.458
956	      bm25_minus_random_pp: -2.7
957	      embedding_minus_bm25_pp: 4.2
958	    bm25_harms_both_encoders: true
959	    cocohanere_artifact_confirmed: true
960	    bm25_minus_random_avg_pp: -2.6
961	  result_rationale: 'BM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder
962	    -2.7pp vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives 选取的是 lexically
963	    similar 但 semantically ambiguous 的文件——它们与 query 共享大量 token overlap（function names,
964	    variable names, import patterns），但这种 overlap 恰恰是 contrastive learning 需要利用来区分
965	    positive/negative 的信号。用 BM25 选的 negatives 让模型学会 ignore lexical cues，但这些 cues 在
966	    code retrieval 中是有效信号。 相比之下，true embedding distance negatives 选取的是 semantically
967	    similar（在 pretrained embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic
968	    distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise comparison，构成
969	    Claim 1 correction argument 的 empirical closure。 效果幅度在 bm25_minus_random_R1_pp
970	    [-4.0, -1.5] 范围内。
971	
972	    '
973	  tables:
974	  - name: 'Table 3: Full 4-Strategy Comparison Including BM25 Baseline'
975	    columns:
976	    - Encoder
977	    - Strategy
978	    - R@1 (%)
979	    - 95% CI
980	    - Δ vs Random (pp)
981	    rows:
982	    - - Qwen
983	      - BM25
984	      - 52.0
985	      - '[51.2, 52.8]'
986	      - −2.5
987	    - - Qwen
988	      - random
989	      - 54.5
990	      - '[53.8, 55.2]'
991	      - —
992	    - - Qwen
993	      - dataflow
994	      - 55.5
995	      - '[54.6, 56.4]'
996	      - '+1.0'
997	    - - Qwen
998	      - embedding
999	      - 56.5
1000	      - '[55.8, 57.2]'
1001	      - '+2.0'
1002	    - - StarCoder
1003	      - BM25
1004	      - 43.3
1005	      - '[42.3, 44.3]'
1006	      - −2.7
1007	    - - StarCoder
1008	      - random
1009	      - 46.0
1010	      - '[45.1, 46.9]'
1011	      - —
1012	    - - StarCoder
1013	      - dataflow
1014	      - 45.8
1015	      - '[44.8, 46.8]'
1016	      - −0.2
1017	    - - StarCoder
1018	      - embedding
1019	      - 47.5
1020	      - '[46.6, 48.4]'
1021	      - '+1.5'
1022	  figures_description:
1023	  - 'Fig 3: 4-strategy R@1 bar chart with BM25 highlighted in red, showing the harm
1024	    direction. Annotation arrow from BM25 to embedding with ''4.5pp gap — the CoCoHaNeRe
1025	    artifact'''
1026	  - 'Fig 4: Neg similarity distribution histograms for BM25 vs embedding vs random
1027	    vs dataflow, showing BM25 occupies a different region of similarity space'
1028	  analysis: 'BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 "argumentative
1029	    correction" 升级为 "empirical demonstration"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy， 还实际运行
1030	    BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。 4-strategy
1031	    ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining strategy 的
1032	    quality spectrum。Reviewer 对 "correction without evidence" 的 concern 被彻底关闭。
1033	
1034	    '
1035	- name: Pool Size Sensitivity (50/100/200/500)
1036	  plan_id: plan_019
1037	  description: '在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints，
1038	    测试 strategy ranking 在更 realistic pool sizes 下的稳定性。
1039	
1040	    '
1041	  expected_results:
1042	    qwen:
1043	      pool_50:
1044	        random_R1: 0.545
1045	        embedding_R1: 0.565
1046	        dataflow_R1: 0.555
1047	        embedding_minus_random_pp: 2.0
1048	      pool_100:
1049	        random_R1: 0.428
1050	        embedding_R1: 0.447
1051	        dataflow_R1: 0.438
1052	        embedding_minus_random_pp: 1.9
1053	      pool_200:
1054	        random_R1: 0.342
1055	        embedding_R1: 0.359
1056	        dataflow_R1: 0.351
1057	        embedding_minus_random_pp: 1.7
1058	      pool_500:
1059	        random_R1: 0.261
1060	        embedding_R1: 0.276
1061	        dataflow_R1: 0.269
1062	        embedding_minus_random_pp: 1.5
1063	    starcoder:
1064	      pool_50:
1065	        random_R1: 0.46
1066	        embedding_R1: 0.475
1067	        dataflow_R1: 0.458
1068	        embedding_minus_random_pp: 1.5
1069	      pool_100:
1070	        random_R1: 0.358
1071	        embedding_R1: 0.372
1072	        dataflow_R1: 0.357
1073	        embedding_minus_random_pp: 1.4
1074	      pool_200:
1075	        random_R1: 0.282
1076	        embedding_R1: 0.295
1077	        dataflow_R1: 0.281
1078	        embedding_minus_random_pp: 1.3
1079	      pool_500:
1080	        random_R1: 0.214
1081	        embedding_R1: 0.225
1082	        dataflow_R1: 0.213
1083	        embedding_minus_random_pp: 1.1
1084	    ranking_stable_across_pools: true
1085	    pool_ranking_stable_pct: 100
1086	    delta_shrinkage_rate: ~0.15pp per doubling of pool size
1087	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
1088	    > random ≈ dataflow for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct
1089	    = 100%）。 绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors
1090	    = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)，
1091	    缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现 "hard" negative 的概率增加（base
1092	    rate effect），部分缩小了 mining 策略的差异。 但核心 signal 不消失——embedding mining 在 pool=500 仍有
1093	    +1.5pp Qwen, +1.1pp StarCoder。 Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500)
1094	    但保持正值。 这直接回应 reviewer "pool=50 unrealistically small" concern：即使 10x pool 扩大，
1095	    strategy ranking 完全不翻转。
1096	
1097	    '
1098	  tables:
1099	  - name: 'Table 12: Pool Size Sensitivity (R@1 %)'
1100	    columns:
1101	    - Pool
1102	    - Encoder
1103	    - random
1104	    - embedding
1105	    - dataflow
1106	    - emb−rand (pp)
1107	    - Ranking
1108	    rows:
1109	    - - 50
1110	      - Qwen
1111	      - 54.5
1112	      - 56.5
1113	      - 55.5
1114	      - '+2.0'
1115	      - E>D>R
1116	    - - 100
1117	      - Qwen
1118	      - 42.8
1119	      - 44.7
1120	      - 43.8
1121	      - '+1.9'
1122	      - E>D>R
1123	    - - 200
1124	      - Qwen
1125	      - 34.2
1126	      - 35.9
1127	      - 35.1
1128	      - '+1.7'
1129	      - E>D>R
1130	    - - 500
1131	      - Qwen
1132	      - 26.1
1133	      - 27.6
1134	      - 26.9
1135	      - '+1.5'
1136	      - E>D>R
1137	    - - 50
1138	      - StarCoder
1139	      - 46.0
1140	      - 47.5
1141	      - 45.8
1142	      - '+1.5'
1143	      - E>R>D
1144	    - - 100
1145	      - StarCoder
1146	      - 35.8
1147	      - 37.2
1148	      - 35.7
1149	      - '+1.4'
1150	      - E>R>D
1151	    - - 200
1152	      - StarCoder
1153	      - 28.2
1154	      - 29.5
1155	      - 28.1
1156	      - '+1.3'
1157	      - E>R≈D
1158	    - - 500
1159	      - StarCoder
1160	      - 21.4
1161	      - 22.5
1162	      - 21.3
1163	      - '+1.1'
1164	      - E>R≈D
1165	  figures_description:
1166	  - 'Fig 10: Pool size (x-axis, log scale) vs R@1 (y-axis) for 3 strategies, separate
1167	    panels for Qwen and StarCoder. Shaded bands between embedding and random lines
1168	    highlight persistent delta.'
1169	  - 'Fig 10b: Delta (embedding − random) vs pool size, showing graceful degradation'
1170	  analysis: Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500 全程保持是
1171	    best tier 的标志。Delta 的 graceful degradation（非 collapse）说明 mining strategy 的价值是
1172	    robust 的。论文可以明确声明："Strategy rankings are stable across pool sizes spanning an
1173	    order of magnitude (50–500), with embedding mining maintaining a statistically
1174	    significant advantage even at the largest pool tested."
1175	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79206874-da2a-4834-aef0-063a0c32fa65",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "221ddb6d-dc5e-440f-83d2-677144fb4582",
  "sourceToolAssistantUUID": "79206874-da2a-4834-aef0-063a0c32fa65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T17:00:41.873Z_

Now I have a comprehensive understanding of the paper. Let me also check the ROADMAP for the experimental plan status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "221ddb6d-dc5e-440f-83d2-677144fb4582",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pU4KQEeCjniJNiP8FH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9878cd60-84df-4933-9261-3f406f7c0b95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mhXeRCD8Bhv3ZNDdrSpoF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18081,
      "cache_read_input_tokens": 56382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18081,
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

_source line 36 · 2026-05-14T17:00:42.530Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FLLCHZ4YwhSNFjzK83uWEw`</summary>

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
  "parentUuid": "9878cd60-84df-4933-9261-3f406f7c0b95",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pU4KQEeCjniJNiP8FH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19a41b50-a07b-4a2e-99d5-6f57852f231c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mhXeRCD8Bhv3ZNDdrSpoF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18081,
      "cache_read_input_tokens": 56382,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18081
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 56382,
          "cache_creation_input_tokens": 18081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18081,
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

_source line 37 · 2026-05-14T17:00:42.547Z_

<details><summary>↩ Tool result · `toolu_01FLLCHZ4YwhSNFjzK83uWEw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\", \"content\": \"# StructFuse — Research Dashboard\\n\\n> 最后更新: 2026-05-14 16:27 UTC | 更新原因: Reviewer WARNING 处理：re-dream gate 标注 + plan_018 contingency + post-M2 时间线明细\\n\\n> 最后更新: 2026-05-14 | 更新原因: Reviewer WARNING 处理：re-dream gate 标注 + plan_018 contingency\\n\\n## 核心方向\\nTrue embedding-distance mining consistently improves contrastive code retrieval (+1.6–2.0pp R@1), correcting prior misconceptions. Structure-grounded (dataflow) negatives provide conditional benefit mediated by encoder representation saturation (observation from n=2 encoders, not validated mechanism). 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **M2 全量训练**: 18 runs 部署完成（Qwen 9 + StarCoder 9），链式自动执行\\n  - Qwen: random_s42 done, random_s43 running (step ~1200/2828), 其余 queued/watcher\\n  - StarCoder: random_s42 running (step ~4000/4242, epoch 3), 其余 queued/watcher\\n  - ETA: Qwen ~May 19, StarCoder ~May 20\\n- **Dream dream_20260514T075732**: Best=4/6(WA), Median=3/6(WR), Worst=3/6(WR)\\n  - 7 项确认行动已持久化（D030），framing + plan 已修改\\n  - **Re-dream dream_20260514T162530 进行中** — 验证修复效果\\n- **plan_015 设计文档**: Worker 完成，待 Agent 汇报\\n- **m1_reextract_v2**: 后台 (~71/82 groups)\\n\\n## 近期任务\\n- [ ] **plan_018 BM25 baseline Phase 1 (CPU)** — 已派 Agent，立即启动\\n- [ ] ⛔ **plan_018 Phase 2 (GPU 训练)** — **需 re-dream 通过后才执行**（D030 gate）\\n- [ ] M2 full 18 runs 完成（~May 19-20）\\n- [ ] 统计检验 — M2 完成后立即执行\\n- [ ] plan_003 SWE-bench Lite eval — M2 best checkpoint ready 后（~20h real on 1 GPU）\\n- [ ] plan_004 RepoBench-R（多 seed + CIs）\\n- [ ] plan_019 Pool size sensitivity — M2 checkpoint ready 后（~2.5h real）\\n- [ ] plan_005 stratified analysis（扩展版）— 0 GPU\\n- [ ] plan_014 temperature ablation — **M2 后单项最大开销 (35h real on 2 GPUs)**，时间紧可推 camera-ready\\n- [ ] plan_015 dynamic mining — 设计完成，待审核\\n- [ ] [Dream 观察] Effect sizes marginal → M2 full 统计后评估\\n- [ ] [Dream 观察] Temperature ablation contradicts story → plan_014 后评估\\n- [ ] Re-dream dream_20260514T162530 结果 → 评估 median 是否 ≥ borderline\\n- [ ] 论文初稿 (~May 24)\\n\\n## Go/No-Go + Re-dream Gate\\n\\n**Claim 1**: 预期 Go。**BM25 contingency**: 若 plan_018 显示 BM25 ≈ random（非 harmful），叙事从 \\\"correcting misconception\\\" 降为 \\\"systematic comparison\\\"。详见 paper_framing.md Contingency 节。\\n**Claim 2**: D028 — 等 M2 统计。\\n**Re-dream gate (D030)**: plan_018 Phase 2 等新 P0 GPU 实验需 re-dream 达标（best ≥ WA, median ≥ borderline）后才批准。Phase 1 (CPU) 不受限。\\n\\n## GPU 预算\\n- **bjb1-42106**: 2× RTX PRO 6000 96GB（专属），满载\\n  - cuda:0: m2_full_qwen（registry ANALYZING 但实际在跑 — 不要重分配）\\n  - cuda:1: m2_full_starcoder (RUNNING)\\n- **Post-M2 需求 (~120h on 2 GPUs = ~60h real = ~2.5 days)**:\\n  - plan_003: 40h (1 GPU, 20h real) — 与 plan_018 Phase 2 并行\\n  - plan_018 Phase 2: 15h (1 GPU, 7.5h real)\\n  - plan_014: 70h (2 GPUs, 35h real) — 时间紧可缩减/推迟\\n  - plan_019: 5h (1 GPU, 2.5h real)\\n- **时间线**: M2 完成(~May 20) → post-M2 实验(~May 22) → 分析+写作(~May 23-24) → ARR May 25\\n\\n## 关键风险\\n1. **ARR May 25**: post-M2 ~60h real + 分析 + 写作 in 5 days。plan_014 (35h) 是瓶颈\\n2. **BM25 narrative risk**: plan_018 结果为 neutral 则需 framing pivot（已备 contingency）\\n3. **Median=WR**: re-dream 进行中，等结果评估改善程度\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D030 | 2026-05-14 | Dream dream_20260514T075732 分析完成：7 项确认行动 + 5 项观察项  | dream_20260514T075732, plan_018, plan_019 |\\n| D029 | 2026-05-14 | Dream full review 完成：7 条三档一致结构性问题确认，BM25 baseline  | plan_018, plan_019, plan_004, plan_005 |\\n| D028 | 2026-05-14 | Claim 2 降级待定：M2 full 结果决定 \\\"conditional benefit\\\" 是独 | m2_embed_verify, plan_013_starcoder, m2_full_qwen, m2_full_starcoder |\\n| D027 | 2026-05-14 | M2 剩余 runs 加 early stopping (patience=2 evals)，加速关 | m2_full_qwen, m2_full_starcoder |\\n| D026 | 2026-05-14 | Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 ep | m2_full_qwen, m2_full_starcoder |\\n| D025 | 2026-05-14 | Plan_014 temperature ablation 缩减为 2 strategies × 3 | m2_full_qwen, plan_014 |\\n| D024 | 2026-05-14 | Major paper framing rewrite: drop falsified \\\"embed | m2_embed_verify, plan_013_starcoder, neg_difficulty_analysis |\\n| D023 | 2026-05-13 | Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重 | m1_reextract |\\n| D022 | 2026-05-13 | M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M | m1_extraction, plan_006_scalability |\\n| D021 | 2026-05-13 | Negative difficulty 分析揭示 encoder capacity 差异是 data | m2_embed_verify, plan_013_starcoder |\\n\\n\\n\\n\", \"total_chars\": 4206, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19a41b50-a07b-4a2e-99d5-6f57852f231c",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "1952ac7c-f90b-4949-8551-a28429bd7f1a",
  "sourceToolAssistantUUID": "19a41b50-a07b-4a2e-99d5-6f57852f231c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-14T17:00:45.943Z_

Now I have a thorough understanding of the paper, its evidence base, experimental status, and internal deliberations. Let me now submit the review via the designated tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1952ac7c-f90b-4949-8551-a28429bd7f1a",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pUPnRmz1uWfTzYhmzf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c7e0d86-1664-4d1f-97a0-23ca750ff164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkABRdJwR3JRsUhszvHubP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2488,
      "cache_read_input_tokens": 74463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2488,
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

_source line 39 · 2026-05-14T17:00:46.275Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WcoddyNcPaA3b5n56TLQte`</summary>

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
  "parentUuid": "9c7e0d86-1664-4d1f-97a0-23ca750ff164",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pUPnRmz1uWfTzYhmzf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20a602da-f7a6-4d60-abb2-7a2cc46643d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkABRdJwR3JRsUhszvHubP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2488,
      "cache_read_input_tokens": 74463,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2488
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 74463,
          "cache_creation_input_tokens": 2488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2488,
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

_source line 40 · 2026-05-14T17:00:46.278Z_

<details><summary>↩ Tool result · `toolu_01WcoddyNcPaA3b5n56TLQte`</summary>

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
  "parentUuid": "20a602da-f7a6-4d60-abb2-7a2cc46643d7",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "722a3116-fa0d-4a70-9547-1a8bec48ab40",
  "sourceToolAssistantUUID": "20a602da-f7a6-4d60-abb2-7a2cc46643d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-14T17:01:00.458Z_



Now I have all the information needed. Let me compose the review. I need to carefully distinguish between what is real experimental evidence versus what is "dreamed" (imagined) results. Based on my reading:

**Confirmed real results:**
- M1 extraction: CodeQL feasibility, Z%=78%, 34% coverage
- Pilot: embedding > random for both encoders (Qwen +2.0pp, StarCoder +1.6pp)
- Pilot: dataflow helps Qwen (+0.8-2.3pp), not StarCoder (-0.5pp)
- neg_difficulty analysis: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy)
- M2 full 18 runs: still running (not complete)

**Dreamed/imagined results (in the "best" tier paper):**
- BM25 baseline (plan_018 not yet run)
- SWE-bench Lite evaluation (plan_003 not yet run)
- RepoBench-R with CIs (plan_004 not yet run)
- All ablations (temperature, pool size, data scaling, dynamic mining, etc.)
- Stratified analysis details
- Negative difficulty quartile analysis with training outcomes

The "best" paper.tex is a dream paper with imagined results filling in gaps. My review should treat it as presented.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "722a3116-fa0d-4a70-9547-1a8bec48ab40",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pUs6jrcpPEqw7fyi8A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d64cea09-d5e6-47a6-b2ca-7348b1461afd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWC35YdMGREV7wAhpgeMBx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 76951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 702,
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

_source line 42 · 2026-05-14T17:02:43.247Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01VBcZ9gjTkzcnwwaUBwq3UE`</summary>

```json
{
  "project": "structfuse-context",
  "tier": "best",
  "dream_id": "dream_20260514T162530",
  "overall_score": "4/6 Weak Accept",
  "report": "### R2 Review: Novelty & Related Work\n\n**Summary:** This paper presents a systematic comparison of four hard negative mining strategies (random, BM25, embedding-distance, dataflow) for contrastive code retrieval, trained on two 3B decoder-only encoders with 9 seeds each. The main contributions are: (1) correcting a prior misconception that embedding-distance negatives harm code retrieval (attributed to a BM25-proxy artifact in CoCoHaNeRe), (2) introducing structure-grounded negatives via inter-procedural dataflow with conditional benefit mediated by encoder representation saturation, and (3) a mechanistic explanation via representation geometry and negative difficulty analysis. The paper is thorough in ablations and robustness checks.\n\n---\n\n**Strengths:**\n\n- S1: **Correcting the CoCoHaNeRe misconception is a genuine contribution.** The identification that CoCoHaNeRe used BM25-proxy negatives mislabeled as embedding-distance is a sharp observation, and the paper closes the argument empirically by running actual BM25 negatives (showing harm: -2.5 to -2.7pp) alongside true embedding mining (showing consistent benefit: +1.5 to +2.0pp). This 4-strategy comparison with the BM25 arm is the single most valuable experiment in the paper. If the BM25 results hold up, this alone is publication-worthy as a corrective finding.\n\n- S2: **Unusually honest and well-calibrated claims.** The paper does not overclaim. Dataflow negatives are explicitly framed as \"conditional\" rather than universally beneficial. The encoder-strategy interaction is presented as an observation from n=2 encoders, not as a validated universal mechanism. The limitations section acknowledges the key weaknesses (2 encoders, 34% coverage, 300 SWE-bench instances). This calibration is refreshing and appropriate for the evidence base.\n\n- S3: **Comprehensive ablation suite.** Temperature (3 values), pool size (4 values, spanning 10x), data scale (3 sizes), dynamic vs static mining, hop depth, weighted vs binary, and fusion head ablations collectively establish that strategy rankings never reverse. The 100% ranking stability across pool sizes 50-500 is strong external validity evidence. The negative results (dynamic mining adds nothing, weighted negatives add nothing) are informative and save practitioners from unnecessary complexity.\n\n- S4: **The stratified analysis by structural data availability is well-designed.** Decomposing the diluted +1.0pp overall dataflow effect into +2.8pp on the 34% stratum with structural data and +0.1pp on the 66% fallback stratum directly addresses the most obvious critique. This shows the authors understand their data and the coverage limitation.\n\n- S5: **Representation geometry analysis adds explanatory depth.** The neg_difficulty quartile analysis (Q4 hardest: +3.2pp vs Q1 easiest: +0.8pp monotonic scaling) goes beyond \"method A > method B\" to explain *when and why* mining quality matters. The pos_sim saturation framing (Qwen 0.9855 vs StarCoder 0.7985) provides a testable prediction for practitioners: check your encoder's pretrained similarity distribution before choosing a mining strategy.\n\n- S6: **Downstream evaluation on SWE-bench Lite with bootstrap significance tests.** Embedding +2.5pp (p=0.018) and dataflow +3.2pp (p=0.008) on end-to-end resolve rate, with multi-file patches driving the dataflow advantage, connects retrieval improvements to practical impact.\n\n---\n\n**Weaknesses:**\n\n- W1: **Novelty of the core contribution is moderate, not high.** The individual components — embedding-distance hard negative mining (ANCE, 2021), contrastive learning for code (well-studied), CodeQL for static analysis (existing tool), LoRA fine-tuning — are all established. The novelty lies in (a) the controlled comparison and (b) the CoCoHaNeRe correction. Category (a) is a \"systematic study\" contribution, which EMNLP values but which inherently has lower novelty than a new method. Category (b) is a targeted correction of one prior paper's methodology. Neither alone reaches the novelty bar for a strong accept at a top venue; together they are borderline sufficient.\n\n- W2: **n=2 encoders fundamentally limits the mechanistic claims.** The encoder-strategy interaction (Claim 2) rests entirely on observing different behaviors for Qwen vs StarCoder. With n=2, any encoder property (architecture details, pretraining data, tokenizer, model size) could explain the difference — the attribution to \"representation saturation\" (pos_sim) is plausible but not identified. An adversarial reader could note that Qwen and StarCoder differ in pretraining corpus, tokenization, and training objective, and that pos_sim is merely correlated with these confounds. The paper should more explicitly frame this as hypothesis-generating, not mechanism-confirming.\n\n- W3: **Effect sizes are small throughout.** The headline results are +2.0pp R@1 for embedding and +1.0pp for dataflow (Qwen). While statistically significant with 9 seeds, the practical significance of 2 percentage points on a retrieval metric is debatable. The SWE-bench amplification to +2.5-3.2pp resolve rate is more compelling, but (a) it is on only 300 instances with a single agent, and (b) the dataflow-vs-embedding comparison is non-significant (p=0.134). A reviewer skeptical of small effects would note that these deltas are within the range that could be sensitive to implementation details (learning rate, number of negatives, sequence length, etc.) that are not ablated.\n\n- W4: **The \"best\" version of this paper appears to include results from experiments that may not all be completed with real data.** The paper reports results across an extraordinary number of conditions (4 strategies x 2 encoders x 9 seeds x 3 temperatures x 4 pool sizes x 3 data sizes + SWE-bench + RepoBench + ablations), which is laudable if real but raises the question of whether all numbers are from completed experiments. Several of the results (e.g., SWE-bench Lite with Qwen3.6-27B agent, BM25 negatives, temperature ablation, pool size sensitivity) appear to be projected rather than measured, based on the project status showing M2 full runs still in progress and plan_018/plan_003/plan_014/plan_019 as \"planned\" or \"pending.\" If this is a pre-submission draft with projected results, the review should be understood as conditional on the actual numbers matching. I flag this not as a criticism of the work plan but as a transparency note.\n\n- W5: **The dataflow contribution is weakened by its own negative result.** Dataflow negatives help Qwen (+1.0pp overall, +2.8pp on structural stratum) but not StarCoder (-0.2pp). The paper frames this as \"conditional benefit,\" but a critical reading is: the proposed novel method (structure-grounded negatives) fails on 50% of tested encoders, and the method that works universally (embedding mining) is not novel — it is ANCE (2021) applied to code. The paper's strongest finding is that embedding mining helps and BM25 hurts, which is more about correcting a misconception than introducing a new technique.\n\n- W6: **Related work positioning of CoCoHaNeRe requires more careful treatment.** The paper claims CoCoHaNeRe \"mislabeled\" BM25 negatives as embedding-distance. This is a strong accusation. The paper should: (a) provide specific evidence from CoCoHaNeRe's methodology section or code showing the BM25 proxy usage, (b) consider whether CoCoHaNeRe's experimental setup differed in other ways (encoder, data, training protocol) that could also explain the discrepancy, and (c) contact the authors or check for errata. If the mislabeling claim cannot be rigorously substantiated, the narrative should soften from \"correcting misconception\" to \"we observe different results under controlled conditions.\"\n\n- W7: **Missing comparisons with important baselines.** The paper does not compare against: (a) cross-encoder reranking (a standard approach for hard negative refinement), (b) curriculum-based negative mining (mentioned in related work but not tested), (c) in-batch negatives (standard in DPR-style training), or (d) existing code retrieval systems like SweRank or SWE-Fixer on the same benchmark. The 4-strategy comparison is well-controlled internally but disconnected from the broader landscape. A reader cannot tell whether embedding mining with LoRA rank-16 on 3B encoders is competitive with, say, SweRank's approach.\n\n- W8: **34% structural coverage is a significant practical limitation that is acknowledged but not solved.** The paper correctly identifies this and decomposes results by stratum, but a practitioner reading the paper would note that for 66% of instances, the dataflow strategy adds nothing. The practical recommendation reduces to \"use embedding mining\" for most cases, with dataflow as a marginal add-on for the minority of instances where CodeQL produces output. The paper would benefit from discussing paths to higher coverage (e.g., alternative static analysis tools, language-agnostic approaches).\n\n---\n\n**Questions for Authors:**\n\n- Q1: Can you provide specific citations or code references from CoCoHaNeRe showing that BM25 was used as a proxy for embedding distance? The \"correcting misconception\" narrative is the paper's strongest hook, and it needs to be ironclad.\n\n- Q2: Have you measured the overlap between BM25-selected and embedding-selected negatives? If they are largely disjoint (which seems likely given the opposite training effects), this would strengthen the argument that the negative source, not just the difficulty level, matters.\n\n- Q3: The neg_difficulty quartile analysis uses margins computed from the pretrained encoder. After training, do these quartile assignments still predict where mining quality matters most? In other words, does the pretrained difficulty distribution remain a good proxy for post-training difficulty?\n\n- Q4: Why was LoRA rank 16 chosen? The static-vs-dynamic mining result (negligible difference) suggests LoRA changes the embedding space only slightly. Would full fine-tuning or higher-rank LoRA show a different pattern, particularly for the dynamic mining comparison?\n\n- Q5: The paper uses 5K training instances. Given the data scaling results (no diminishing returns at 5K), have you considered whether 10K-50K instances (leveraging the M1 reextraction of 44K instances) would further separate the strategies? The current effect sizes are small enough that a larger training set could make the findings more decisive.\n\n- Q6: For the SWE-bench evaluation, you use a single agent (Qwen3.6-27B). How sensitive are the downstream results to the agent choice? If the agent is the bottleneck (30% of failures), could a better agent compress or amplify the retrieval quality differences?\n\n- Q7: The training shows severe overfitting (best checkpoint at ~25% of training, train_loss approaching 0). This suggests the models have far more capacity than the data requires. Have you considered whether the mining strategy effects are partly an artifact of the overfitting dynamics (e.g., harder negatives regularize better)?\n\n---\n\n**Detailed Assessment by Contribution:**\n\n**Claim 1 (Correcting CoCoHaNeRe):** This is the paper's strongest and most novel claim. The BM25 < random < embedding ordering, if reproducible and if the CoCoHaNeRe mislabeling is verified, is a clean corrective finding. Novelty: moderate (it is a correction, not a new method). Significance: high for the code retrieval community specifically. **Score: 4/5 significance, 3/5 novelty.**\n\n**Claim 2 (Structure-grounded negatives, conditional benefit):** Novel in concept (training-time structural negatives via CodeQL inter-procedural dataflow), but the evidence is mixed (helps one encoder, not the other). The \"conditional benefit mediated by representation saturation\" framing is intellectually interesting but underdetermined with n=2. This is better positioned as an observation + hypothesis than as a validated mechanism. **Score: 3/5 significance, 3.5/5 novelty.**\n\n**Claim 3 (Representation geometry analysis):** The neg_difficulty quartile analysis and pos_sim saturation framing add genuine explanatory value. However, this is descriptive analysis of existing representations, not a new analytical framework. It connects observations but does not enable new predictions beyond \"check pos_sim before choosing a strategy.\" **Score: 3/5 significance, 2.5/5 novelty.**\n\n---\n\n**Related Work Completeness:**\n\nThe related work covers the main areas adequately: code retrieval (SweRank, SWE-Fixer), hard negative mining (ANCE, curriculum, CoCoHaNeRe), and graph-based code understanding (CodexGraph, LocAgent, RANGER, ARISE, GraphCodeBERT). The inference-time vs training-time positioning (Table 16) is a useful contribution.\n\n**Missing or underrepresented:**\n- DPR (Karpukhin et al., 2020) deserves more than passing mention as the foundational work for hard negative mining in retrieval.\n- Contrastive learning for code (ContraCode, Ding et al. ACL Findings 2022) is relevant but absent.\n- The NL retrieval literature on hard negative mining (e.g., RocketQA, TAS-B, GPL) has extensive findings on when hard negatives help vs hurt. The paper would benefit from connecting its code-specific findings to this broader literature.\n- No comparison with or discussion of SweRank's or SWE-Fixer's actual training methodology — are they using random negatives? BM25? If known, this would contextualize the contribution.\n- GraphCodeBERT's use of dataflow in pretraining is mentioned but the relationship is not analyzed deeply. The key difference (pretraining objective vs negative mining) deserves explicit discussion.\n\n---\n\n**Writing Quality:** Generally clear and well-organized. The paper follows a logical structure from motivation to method to results to analysis. Tables are well-formatted. The abstract is informative. Minor issues: some tables could be consolidated (16 tables is a lot); the ablation section, while thorough, reads as a checklist rather than building toward a coherent narrative. Consider grouping ablations by the question they answer rather than listing sequentially.\n\n---\n\n**Broader Impact / Generalization:**\n\nThe paper's findings are specific to: (a) Python repositories, (b) 3B decoder-only code encoders, (c) LoRA rank-16 fine-tuning, (d) static one-time mining, (e) SWE-smith training data. The temperature and pool size robustness checks help, but generalization to other languages (Java, C++), encoder architectures (encoder-only like CodeBERT, much larger models like 7B+), and full fine-tuning is untested. The practical recommendation (\"use embedding mining\") is likely to generalize; the structural mining finding is more setup-dependent.\n\n---\n\n**Novelty Score:** 3/5\nThe paper does not introduce a fundamentally new method or framework. Its novelty comes from (a) a corrective finding about a prior paper's methodology, (b) applying inter-procedural dataflow to training-time negative mining (new application of existing tools), and (c) connecting representation geometry to mining strategy effectiveness (descriptive analysis). These are meaningful but incremental contributions. The paper's value is more in \"understanding\" than \"invention.\"\n\n**Overall Score:** 4/6 (Weak Accept)\nThe paper is well-executed systematic work that will be useful to practitioners training contrastive code retrievers. The CoCoHaNeRe correction is valuable, the ablation suite is thorough, and the claims are well-calibrated. The main limitations are: small effect sizes, n=2 encoders for the mechanistic claims, and moderate novelty (correcting a misconception + applying existing tools in a new combination). For EMNLP, this fits the \"empirical analysis\" archetype well. The paper is above the acceptance threshold if all reported numbers are from completed experiments and the CoCoHaNeRe mislabeling claim is rigorously documented.\n\n**Confidence:** 4/5\nI am familiar with contrastive learning, hard negative mining, and code retrieval. I have read the full paper, project documentation, and experimental logs. My main uncertainty is whether all reported results are from completed experiments (some appear projected based on project status), which would affect the overall assessment.",
  "review_visible": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d64cea09-d5e6-47a6-b2ca-7348b1461afd",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pUs6jrcpPEqw7fyi8A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70c3b0f6-cf67-4173-ae8f-45bbd6d209eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWC35YdMGREV7wAhpgeMBx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 76951,
      "output_tokens": 4417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 702
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4417,
          "cache_read_input_tokens": 76951,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 702,
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

_source line 43 · 2026-05-14T17:02:46.790Z_

<details><summary>↩ Tool result · `toolu_01VBcZ9gjTkzcnwwaUBwq3UE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md\", \"dream_id\": \"dream_20260514T162530\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70c3b0f6-cf67-4173-ae8f-45bbd6d209eb",
  "isSidechain": true,
  "promptId": "0dbd644e-3638-4b84-b174-ff7865af1dfb",
  "agentId": "a81897433be7dac28",
  "type": "user",
  "uuid": "cdffd879-ce12-429f-9fc5-cf6de4ef6aba",
  "sourceToolAssistantUUID": "70c3b0f6-cf67-4173-ae8f-45bbd6d209eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T17:02:59.469Z_

Review submitted. Here is the summary:

**Overall: 4/6 Weak Accept | Novelty: 3/5 | Confidence: 4/5**

Key assessments:

**Strongest element:** The CoCoHaNeRe correction (Claim 1) -- identifying the BM25-proxy mislabeling and closing the argument empirically with a 4-strategy comparison. This alone is a valuable corrective finding for the code retrieval community.

**Main weaknesses identified:**
1. Moderate novelty -- the paper combines existing tools (ANCE-style mining, CodeQL, LoRA) in a new context rather than introducing a new method
2. n=2 encoders cannot identify the mechanism behind the encoder-strategy interaction; pos_sim saturation is a plausible hypothesis but confounded with many other encoder differences
3. Small effect sizes throughout (+2pp R@1) that may be sensitive to implementation details
4. The dataflow contribution fails on 50% of encoders tested, making the universal finding "use embedding mining" (which is not novel) rather than "use structure-grounded negatives"
5. Several results in the "best" tier paper appear to be projected from the experimental plan rather than measured (M2 full runs still in progress, BM25 baseline/SWE-bench/ablations planned but not completed)

**Critical question for the narrative:** The "correcting misconception" claim requires ironclad evidence that CoCoHaNeRe specifically used BM25 as a proxy for embedding distance. Without specific citations or code references, this should soften to "we observe different results under controlled conditions."

**Related work gaps:** Missing DPR foundational discussion, NL retrieval hard negative literature (RocketQA, TAS-B), and contrastive code learning work (ContraCode). The inference-time graph comparison table is a useful addition.

Report saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdffd879-ce12-429f-9fc5-cf6de4ef6aba",
  "isSidechain": true,
  "agentId": "a81897433be7dac28",
  "requestId": "req_011Cb2pdYqe46Y3n9TV1yEx7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ea94922-c902-45d9-8359-af2638f24c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "ef1befa8-2efd-49dd-aab6-f69049f8448e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9bhbQETVUUadR9znzaDGP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4546,
      "cache_read_input_tokens": 77653,
      "output_tokens": 483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4546
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 483,
          "cache_read_input_tokens": 77653,
          "cache_creation_input_tokens": 4546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4546,
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
