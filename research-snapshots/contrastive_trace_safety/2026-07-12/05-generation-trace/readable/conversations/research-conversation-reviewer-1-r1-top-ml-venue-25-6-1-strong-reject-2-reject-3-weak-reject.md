# Research conversation: 你是 Reviewer 1 (R1)，负责审稿的**方法与实验**维度。请对以下论文进行独立审稿，按 top ML venue 标准（接受率 ~25%，6分制：1=Strong Reject, 2=Reject, 3=Weak Reject

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a3675f4a8d53881c9.jsonl`
- **Structured JSON:** [`b4f4b67f236903c523ca.json`](../../sessions/b4/b4f4b67f236903c523ca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-14T08:37:51.617Z_

你是 Reviewer 1 (R1)，负责审稿的**方法与实验**维度。请对以下论文进行独立审稿，按 top ML venue 标准（接受率 ~25%，6分制：1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept）。

## 论文信息

**标题**: "A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval"

**摘要**: 系统比较了三种 negative sampling 策略（random, embedding-distance, dataflow-aware）用于训练 contrastive code retriever，使用两个编码器（Qwen2.5-Coder-3B, StarCoder2-3B），54 个 full-scale 训练 runs（9 seeds × 3 strategies × 2 encoders）。Pilot (2K instances, 单 seed) 显示 embedding mining +1.6-2.0pp R@1。但 full-scale (15K instances, 9 seeds) 策略差异 <1pp，被种子方差 (std≈3pp) 淹没，bootstrap p≥0.68。发现 data-size-benefit scaling law: -0.11pp/1K instances。

**方法**:
- 任务: bug report → file retrieval，bi-encoder + InfoNCE loss + LoRA rank 16
- 三种策略: random, embedding-distance (pretrained encoder nearest neighbor), dataflow-aware (CodeQL inter-procedural analysis, 2-hop default, disconnected + high embedding sim)
- 两个编码器: Qwen2.5-Coder-3B (saturated, pos_sim=0.9855, margin=0.017), StarCoder2-3B (healthy, pos_sim=0.7985, margin=0.194)
- 训练数据: Pilot ~2K from 8 repos, Full-scale 15,133 from 123 repos

**主要实验结果**:

Table 1 (Qwen full-scale 9 seeds × 3 strategies): random 0.523±0.031, embed 0.521±0.035, dataflow 0.515±0.038
Table 2 (StarCoder full-scale): random 0.443±0.028, embed 0.435±0.033, dataflow 0.428±0.040
Table 3 (SWE-bench Lite): resolve rates random 0.187, embed 0.190, dataflow 0.183; McNemar p=0.89
Table 4 (Bootstrap CI): embed vs random delta +0.3pp, 95% CI [-3.8,+4.5], p=0.78
Table 5 (RepoBench-R): random 0.312, embed 0.308, dataflow 0.295; pretrained baseline 0.285
Table 6 (vs inference-time methods): LocAgent 26.2% resolve vs ours ~19%
Table 7 (Data size scaling): 1K→+1.3pp, 3K→+0.5pp, 5K→+0.1pp, 15K→-0.2pp; slope -0.11pp/1K
Table 8 (Stratified by repo size): small -2.0pp, medium +1.0pp, large -1.0pp, xlarge 0.0pp
Table 9 (Pilot vs full distribution): structural_rate 0.58→0.34, files/repo 45→185, large repos 30%→56%
Table 10 (Failure taxonomy 50 cases): dataflow could help 6, actually helped 2, hurt 3
Table 11 (Temperature ablation τ∈{0.05,0.1,0.2}): random best at all τ
Table 12 (Hop-distance ablation): all hops below random (-0.8 to -1.3pp)
Table 13 (Fusion head): embed-only 0.523, structural-only 0.385, combined 0.519
Table 14 (Static vs dynamic mining): dynamic -0.3pp vs static, -0.5pp vs random

**实验设计参考（完整计划中的实验列表）**:
1. M2 Full Qwen — 9 seeds × 3 strategies (covered in Table 1)
2. M2 Full StarCoder — 9 seeds × 3 strategies (covered in Table 2)
3. M3a SWE-bench Lite (covered in Table 3-4)
4. M3b RepoBench-R (covered in Table 5)
5. Embedding vs Random Deep Stratified Analysis (covered in Table 8, but missing neg_difficulty quartile analysis and scatter plot)
6. Hop-Distance Ablation (covered in Table 12)
7. Training Data Size Scaling (covered in Table 7)
8. Fusion Head Ablation (covered in Table 13)
9. Dataflow-Distance Weighted vs Binary (mentioned briefly in §6.5, no table)
10. Failure Analysis 50 cases (covered in Table 10)
11. Qualitative Examples (not present in paper)
12. Temperature Ablation (covered in Table 11)
13. Dynamic vs Static Mining (covered in Table 14)
14. Bootstrap CI for SWE-bench (covered in Table 4)
15. Inference-Time Graph Discussion (covered in Table 6)
16. Data Pipeline Distribution Audit (covered in Table 9)

## 审稿要求

请从以下维度评审，输出结构化报告：

### 1. 方法论评价
- 实验设计是否合理、严谨？
- 统计方法是否恰当？
- 是否有方法论缺陷？

### 2. 实验充分性
- 对照实验设计参考列表，论文是否充分覆盖了预期实验？
- 哪些实验缺失或不完整？
- 现有实验的深度是否足够？

### 3. 结果可信度
- 结果是否支持论文的 claims？
- 有无内部矛盾或可疑模式？
- 统计检验是否充分？

### 4. 弱点与问题
- 列出所有发现的问题（major 和 minor）

### 5. 评分
- 给出 1-6 分评分及理由
- 给出 confidence (1-5)

请输出完整审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "0fd97c9c-d5e6-4f19-8753-1ded47e5929a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T08:37:51.622Z_

```json
{
  "parentUuid": "0fd97c9c-d5e6-4f19-8753-1ded47e5929a",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
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
  "uuid": "4c0c118f-fe6a-409c-971f-a93ac076366d",
  "timestamp": "2026-05-14T08:37:51.622Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T08:37:54.988Z_



I'll start by reading the project files to get the full context of the paper before providing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c0c118f-fe6a-409c-971f-a93ac076366d",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A8MxZVK6RryZXSeBwu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c37a8ac6-2050-413b-992c-d99f60ecd5da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVw7thS27zcJFSZYvD1LEL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15742,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15742,
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

_source line 4 · 2026-05-14T08:37:56.464Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016fz29uzTRDEmdqAachWvgH`</summary>

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
  "parentUuid": "c37a8ac6-2050-413b-992c-d99f60ecd5da",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A8MxZVK6RryZXSeBwu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5730e679-0665-4744-8f19-5b36f18a3bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVw7thS27zcJFSZYvD1LEL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15742,
      "cache_read_input_tokens": 0,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15742
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15742,
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

_source line 5 · 2026-05-14T08:37:56.468Z_

<details><summary>↩ Tool result · `toolu_016fz29uzTRDEmdqAachWvgH`</summary>

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
  "parentUuid": "5730e679-0665-4744-8f19-5b36f18a3bae",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "0174488c-796e-4a87-a661-a17dabfe49a3",
  "sourceToolAssistantUUID": "5730e679-0665-4744-8f19-5b36f18a3bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T08:37:59.779Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01EwU6FchWNbR2rRHMvoPXWg`</summary>

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
  "parentUuid": "0174488c-796e-4a87-a661-a17dabfe49a3",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A8igk3SZxTr9Sm5agr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3af27453-ec3d-4a8b-9928-3350ea631d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJ5Vej5aRNcMMGegtiryAE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 7 · 2026-05-14T08:37:59.878Z_

<details><summary>↩ Tool result · `toolu_01EwU6FchWNbR2rRHMvoPXWg`</summary>

```text
{"result":"# 项目 structfuse-context 概况\n\n## 实验状态 (31 个)\n\n- **p2b_eval_4runs_pool50**: DONE (success) — \n- **d007_50repo_overlap**: DONE (success) — \n- **p2b_5reruns**: DONE (success) — \n- **p2b_eval_4runs_v2**: DONE (success) — \n- **p2b-all-9runs**: DONE (killed) — \n- **p2b-smoke8**: DONE (killed) — \n- **p2b-smoke7**: DONE (killed) — \n- **p2b-smoke6**: DONE (killed) — \n- **p2b-smoke5**: DONE (killed) — \n- **p2b-smoke4**: DONE (killed) — \n- **p2b-smoke3**: DONE (killed) — \n- **p2b-smoke2**: DONE (killed) — \n- **p2b-smoke-test**: DONE (killed) — \n- **mvp_p2a_linear_proxy**: DONE (success) — \n- **mvp_p1_codeql_feasibility**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\n- **m1_extraction** (success): —\n\n## 趋势\n成功 10 / 负向 2 / 失败 2 / 共 28\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-42106: 无 GPU 信息\n\n## 告警\n- p2b-smoke-test: 已被终止 — unknown\n- p2b-smoke2: 已被终止 — unknown\n- p2b-smoke3: 已被终止 — unknown\n- p2b-smoke4: 已被终止 — unknown\n- p2b-smoke5: 已被终止 — unknown\n- p2b-smoke6: 已被终止 — unknown\n- p2b-smoke7: 已被终止 — unknown\n- p2b-smoke8: 已被终止 — unknown\n- p2b-all-9runs: 已被终止 — unknown\n- mvp_p2b_contrastive_training: 已被终止 — unknown\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\n- p2b_eval_all: 已被终止 — unknown\n- m2_early_pilot: 已被终止 — unknown\n- m2_early_pilot_v2: 训练失败 — unknown\n- m2_early_pilot_v3: 已被终止 — unknown\n- m1_reextract: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3af27453-ec3d-4a8b-9928-3350ea631d9b",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "73b03f3d-42e2-4200-86d6-21e68b477763",
  "sourceToolAssistantUUID": "3af27453-ec3d-4a8b-9928-3350ea631d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T08:38:00.363Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012MzgzwZcH3qexYVbGZvkZQ`</summary>

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
  "parentUuid": "73b03f3d-42e2-4200-86d6-21e68b477763",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A8igk3SZxTr9Sm5agr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1419a425-4b17-4e3f-ad62-ba0c7eb626dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJ5Vej5aRNcMMGegtiryAE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 15742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1450,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 9 · 2026-05-14T08:38:00.373Z_

<details><summary>↩ Tool result · `toolu_012MzgzwZcH3qexYVbGZvkZQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n- **m1_extraction** (success): —\\n\\n## 趋势\\n成功 10 / 负向 2 / 失败 2 / 共 28\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 1895, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1419a425-4b17-4e3f-ad62-ba0c7eb626dc",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "57ab420e-3ed4-46da-bbbf-9020826e09d4",
  "sourceToolAssistantUUID": "1419a425-4b17-4e3f-ad62-ba0c7eb626dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T08:38:03.918Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VWx4dNsjXWty1rrNMNUtRC`</summary>

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
  "parentUuid": "57ab420e-3ed4-46da-bbbf-9020826e09d4",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A91aVgcgZsqCZi7rfR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90409952-2cba-499e-9b71-03a6bcd11c71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A52N6h7hrgyonc1qdYEuPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 17192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2711,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 11 · 2026-05-14T08:38:03.931Z_

<details><summary>↩ Tool result · `toolu_01VWx4dNsjXWty1rrNMNUtRC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); heavy inference cost |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | Repository-level Graph for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2025) | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (2025) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献\\n\\n- CodexGraph: arXiv:2408.03910, NAACL 2025\\n- LocAgent: arXiv:2503.09089, ACL 2025\\n- RANGER: arXiv:2509.25257, 2025\\n- RepoGraph: arXiv:2410.14684, ICLR 2025\\n- GraphCoder: arXiv:2406.07003, ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, 2025\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\", \"total_chars\": 8062, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90409952-2cba-499e-9b71-03a6bcd11c71",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "41b0eacb-3d95-4b99-a8d2-ae192b4733b2",
  "sourceToolAssistantUUID": "90409952-2cba-499e-9b71-03a6bcd11c71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T08:38:04.898Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G3ZiRy8vHaZz1ftVh98VKL`</summary>

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
  "parentUuid": "41b0eacb-3d95-4b99-a8d2-ae192b4733b2",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A91aVgcgZsqCZi7rfR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ffd8311-283e-4e3d-b28d-38fee8572e08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A52N6h7hrgyonc1qdYEuPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 17192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2711,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 13 · 2026-05-14T08:38:04.908Z_

<details><summary>↩ Tool result · `toolu_01G3ZiRy8vHaZz1ftVh98VKL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\", \"content\": \"# StructFuse — Research Dashboard\\n\\n> 最后更新: 2026-05-14 01:47 UTC | 更新原因: Reviewer warnings 落地: m1_reextract_v2 定位明确 (camera-ready not current submission), plan_015/017 写作处理方案, experiment_plan 更新待排\\n\\n## 核心方向\\n\\\"Hard negative mining for code retrieval: what works, what doesn't, and why\\\" — 系统性分析 + 机制解释论文。详见 paper_framing.md（D024 重写后）。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **Framing 重写完成 (D024)**: 旧 Claim 2 (\\\"embedding harms\\\") 已证伪并移除；新叙事线：embedding universally helps → dataflow conditionally helps → mechanistic explanation via representation saturation\\n- **Full M2 训练中**: Qwen random_s42 running (best R@1=55.3% @step1000, overfitting @1500); StarCoder random_s42 running (R@1=45.4% @step1000, still improving)\\n- **M1 reextract v2 进行中**: 4 workers 并行 CodeQL 提取，~13% 进度\\n- **Plan_003 SWE-bench eval**: Pipeline ready (dry-run v2 PASS), 等 M2 checkpoint\\n- **Plan_014 temp ablation**: 脚本 D025 缩减完成 (6 runs, ~70h), 等 M2 释放 GPU\\n\\n## 近期任务\\n- [ ] 等 Qwen eval@2000 → 确认过拟合 → 剩余 8 seeds 减至 2 epochs (节省 ~48h/GPU)\\n- [ ] neg_difficulty 可视化 Figure（0 GPU-h，论文核心差异化图表）— 已派 Agent\\n- [ ] M2 full 18 runs 完成 → 统计检验 (bootstrap CI, paired t-test)\\n- [ ] M2 完成后: plan_014 temperature ablation (双卡 ~35h wall time)\\n- [ ] M2 Qwen best checkpoint → plan_003 SWE-bench Lite eval\\n- [ ] plan_004 RepoBench-R 第二 benchmark\\n- [ ] experiment_plan.yaml 更新: plan_002/013 关联 full M2 registry_id, plan_014 budget 修正\\n- [ ] 写作时: plan_015 (dynamic mining) → Limitation 段落; plan_017 (inference-time graph) → Discussion 段落 (0 GPU-h)\\n\\n## Go/No-Go 阈值 (D019/D020, 适配 D024 新 framing)\\n\\n**Claim 1 (embedding vs random)**: 预期 Go — pilot 已一致确认 (+1.6~2.0pp)。Full M2 提供 3-seed CI。\\n**Claim 2 (dataflow conditional benefit)**: 预期 Conditional Go — Qwen 正向、StarCoder 中性。Full M2 量化 interaction effect。\\n**n=3 功效限制**: df=2, Type II error 高。Discussion 必须讨论。\\n\\n## GPU 预算\\n- **bjb1-42106**: 2× RTX PRO 6000 96GB（专属）\\n  - cuda:0: m2_full_qwen (seed 1/9, step ~1550/4242)\\n  - cuda:1: m2_full_starcoder (seed 1/9, step ~1000/4242)\\n- **剩余**: ~140 GPU-h needed for plan_003/014/004/015 | 瓶颈是 M2 完成时间非总量\\n- **过拟合缩减**: 若 eval@2000 确认，2 epochs 节省 ~96h 总计，M2 约 May 18-19 完成（vs May 20-21）\\n\\n## m1_reextract_v2 定位\\n当前 M2 使用 15.9K structural data 训练。reextract_v2 完成后数据量预计 ~30K+，但 May 25 前无法重跑 M2（~200+ GPU-h）。**用途：camera-ready revision 或后续投稿的 scalability 证据**，不影响当前投稿关键路径。当前价值：Claim 3 (CodeQL scalability) 的 coverage 数字更新。\\n\\n## 关键风险\\n1. **ARR deadline May 25**: 关键路径 M2(~May 18) → plan_014(~May 19.5) → plan_003(~May 21) → 统计+初稿(~May 24)\\n2. **n=3 统计功效**: pilot <2pp 差异在 df=2 下极难显著\\n3. **plan_015 未做**: static vs dynamic mining confound 由 2/3 dream reviewers 提出，需 Limitation 段承认\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D027 | 2026-05-14 | M2 剩余 runs 加 early stopping (patience=2 evals)，加速关 | m2_full_qwen, m2_full_starcoder |\\n| D026 | 2026-05-14 | Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 ep | m2_full_qwen, m2_full_starcoder |\\n| D025 | 2026-05-14 | Plan_014 temperature ablation 缩减为 2 strategies × 3 | m2_full_qwen, plan_014 |\\n| D024 | 2026-05-14 | Major paper framing rewrite: drop falsified \\\"embed | m2_embed_verify, plan_013_starcoder, neg_difficulty_analysis |\\n| D023 | 2026-05-13 | Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重 | m1_reextract |\\n| D022 | 2026-05-13 | M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M | m1_extraction, plan_006_scalability |\\n| D021 | 2026-05-13 | Negative difficulty 分析揭示 encoder capacity 差异是 data | m2_embed_verify, plan_013_starcoder |\\n| D020 | 2026-05-13 | D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明 | m2_full_qwen, m2_full_starcoder |\\n| D019 | 2026-05-13 | D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案 | m2_full_qwen, m2_full_starcoder |\\n| D018 | 2026-05-13 | 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯 | m2_embed_verify, plan_013_starcoder |\\n\\n\", \"total_chars\": 3742, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ffd8311-283e-4e3d-b28d-38fee8572e08",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "d936d7b3-b3ba-4701-9609-9f454f17b1d4",
  "sourceToolAssistantUUID": "9ffd8311-283e-4e3d-b28d-38fee8572e08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T08:38:05.367Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EzcAYtPTpnVbP8fN4Gq57a`</summary>

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
  "parentUuid": "d936d7b3-b3ba-4701-9609-9f454f17b1d4",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A91aVgcgZsqCZi7rfR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9d57141-e657-4764-80aa-7c1ebf97be62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A52N6h7hrgyonc1qdYEuPj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 17192,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 17192,
          "cache_creation_input_tokens": 2711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2711,
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

_source line 15 · 2026-05-14T08:38:05.378Z_

<details><summary>↩ Tool result · `toolu_01EzcAYtPTpnVbP8fN4Gq57a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \\\"harm\\\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\\n\\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\\n\\n- **Headline result template**: \\\"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\\\"\\n- Backup: \\\"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\\n- m1_reextract_v2: expanded extraction for higher coverage\\n\\n### Planned (priority order):\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark\\n- plan_015: Dynamic mining baseline\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 9391, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9d57141-e657-4764-80aa-7c1ebf97be62",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "a1e422df-5104-4a25-9639-8f1a612a7381",
  "sourceToolAssistantUUID": "c9d57141-e657-4764-80aa-7c1ebf97be62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-14T08:38:08.968Z_

Now let me read additional project files to understand the experimental details more deeply.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1e422df-5104-4a25-9639-8f1a612a7381",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A9NxN6iKsZSGdQo7Uz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e64b7c1b-ab8a-4271-8347-269a557faa77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bjvTAEiDTF4j9mDwxB7uj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7606,
      "cache_read_input_tokens": 19903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7606,
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

_source line 17 · 2026-05-14T08:38:10.005Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EebmTgZened74Sx9xTpU7Y`</summary>

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
  "parentUuid": "e64b7c1b-ab8a-4271-8347-269a557faa77",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A9NxN6iKsZSGdQo7Uz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8885ff2-d836-4592-9926-ca3e41b91c11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bjvTAEiDTF4j9mDwxB7uj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7606,
      "cache_read_input_tokens": 19903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7606,
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

_source line 18 · 2026-05-14T08:38:10.016Z_

<details><summary>↩ Tool result · `toolu_01EebmTgZened74Sx9xTpU7Y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 28\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n\", \"total_chars\": 20054, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8885ff2-d836-4592-9926-ca3e41b91c11",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "570e1cff-4284-49af-8b25-e440ac2b326d",
  "sourceToolAssistantUUID": "d8885ff2-d836-4592-9926-ca3e41b91c11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T08:38:10.583Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01D1hZryAt2kxA3JAGTi1vBy`</summary>

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
  "parentUuid": "570e1cff-4284-49af-8b25-e440ac2b326d",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A9NxN6iKsZSGdQo7Uz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6bd4557a-d335-404c-9ec6-ec3750497ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bjvTAEiDTF4j9mDwxB7uj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7606,
      "cache_read_input_tokens": 19903,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7606
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 19903,
          "cache_creation_input_tokens": 7606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7606,
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

_source line 20 · 2026-05-14T08:38:10.593Z_

<details><summary>↩ Tool result · `toolu_01D1hZryAt2kxA3JAGTi1vBy`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bd4557a-d335-404c-9ec6-ec3750497ede",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "4a973c28-860f-450b-a98b-83fd929e1d4b",
  "sourceToolAssistantUUID": "6bd4557a-d335-404c-9ec6-ec3750497ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T08:38:13.424Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01C4e4najwtEhSBdBodbmz2i`</summary>

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
  "parentUuid": "4a973c28-860f-450b-a98b-83fd929e1d4b",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A9mREJR7aJQPV1xyAf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c6c1f01-146a-4ed7-b5ed-2a9fe43fb7da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jiciy2zRKNciuRLPqRd2yA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11213,
      "cache_read_input_tokens": 27509,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11213
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 27509,
          "cache_creation_input_tokens": 11213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11213,
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

_source line 22 · 2026-05-14T08:38:13.433Z_

<details><summary>↩ Tool result · `toolu_01C4e4najwtEhSBdBodbmz2i`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c6c1f01-146a-4ed7-b5ed-2a9fe43fb7da",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "bb0c1dee-9b0a-4a8f-8bf9-8ad28f7b7030",
  "sourceToolAssistantUUID": "5c6c1f01-146a-4ed7-b5ed-2a9fe43fb7da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T08:38:19.730Z_

Now let me look at the artifacts directory and any paper drafts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb0c1dee-9b0a-4a8f-8bf9-8ad28f7b7030",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A9ySXvTv1RNdZvyibG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ab9bcf4-9802-4d40-a57c-33289726ab20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwB3vHBNg16aPzPeBz5z87",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 161,
      "cache_read_input_tokens": 38722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 161,
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

_source line 24 · 2026-05-14T08:38:21.509Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016JbSdZpqDk4d9cP1n4W79W`</summary>

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
  "parentUuid": "0ab9bcf4-9802-4d40-a57c-33289726ab20",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A9ySXvTv1RNdZvyibG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c087469f-97ce-4796-a8cb-f829d1c4d92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwB3vHBNg16aPzPeBz5z87",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 161,
      "cache_read_input_tokens": 38722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 161,
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

_source line 25 · 2026-05-14T08:38:21.531Z_

<details><summary>↩ Tool result · `toolu_016JbSdZpqDk4d9cP1n4W79W`</summary>

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
  "parentUuid": "c087469f-97ce-4796-a8cb-f829d1c4d92c",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "dcceb601-2bb6-4a2d-aafd-d596c4534d94",
  "sourceToolAssistantUUID": "c087469f-97ce-4796-a8cb-f829d1c4d92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T08:38:21.698Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Dc8rhgzqvxQikWVutnjxXg`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcceb601-2bb6-4a2d-aafd-d596c4534d94",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2A9ySXvTv1RNdZvyibG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba683028-48a3-4232-9ba7-8801fe79a540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwB3vHBNg16aPzPeBz5z87",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 161,
      "cache_read_input_tokens": 38722,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 161
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 38722,
          "cache_creation_input_tokens": 161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 161,
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

_source line 27 · 2026-05-14T08:38:21.711Z_

<details><summary>↩ Tool result · `toolu_01Dc8rhgzqvxQikWVutnjxXg`</summary>

```text
literature_map.yaml
artifacts/dream_reports/dream_20260512T204322/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/meta.yaml
artifacts/manifest.yaml
registry.yaml
artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml
decisions.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260514T075732/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260514T075732/best/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/median/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba683028-48a3-4232-9ba7-8801fe79a540",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "3aee950d-c6d7-4665-988f-de0c1212bca1",
  "sourceToolAssistantUUID": "ba683028-48a3-4232-9ba7-8801fe79a540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T08:38:25.516Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GM6YnW2T31TH97vmrTWzDt`</summary>

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
  "parentUuid": "3aee950d-c6d7-4665-988f-de0c1212bca1",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2AAarkwurLeW39kyu66",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7252ff5-31a2-45d0-836d-b4264997df10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxAF91EYH4RhAcMiwbuLAX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 38883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 641,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
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

_source line 29 · 2026-05-14T08:38:25.545Z_

<details><summary>↩ Tool result · `toolu_01GM6YnW2T31TH97vmrTWzDt`</summary>

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
  "parentUuid": "e7252ff5-31a2-45d0-836d-b4264997df10",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "72cd2a7c-f41b-48e3-a46a-7452066408cc",
  "sourceToolAssistantUUID": "e7252ff5-31a2-45d0-836d-b4264997df10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T08:38:25.811Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BPd1V4jS3pnchdrHXu7E7i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72cd2a7c-f41b-48e3-a46a-7452066408cc",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2AAarkwurLeW39kyu66",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95760103-a84e-4fd9-beef-a28c2bf4f52b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxAF91EYH4RhAcMiwbuLAX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 38883,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 641
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 38883,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 641,
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

_source line 31 · 2026-05-14T08:38:25.816Z_

<details><summary>↩ Tool result · `toolu_01BPd1V4jS3pnchdrHXu7E7i`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected
5	    vs gold statistics'
6	  priority: P0
7	  gpu_budget_hours: 0
8	  deps: []
9	  registry_id: m1_extraction
10	  mvp_registry_id: mvp_p1_codeql_feasibility
11	- id: plan_002
12	  claim: 1
13	  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,
14	    3 seeds each, Qwen2.5-Coder-3B LoRA'
15	  priority: P0
16	  gpu_budget_hours: 200
17	  deps:
18	  - plan_001
19	  registry_id: m2_embed_verify
20	  mvp_registry_id: mvp_p2b_contrastive_training
21	  full_registry_ids: ["m2_full_qwen", "m2_full_starcoder"]
22	- id: plan_003
23	  claim: 1
24	  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best
25	    checkpoint, Qwen3.6-27B agent'
26	  priority: P0
27	  gpu_budget_hours: 40
28	  deps:
29	  - plan_002
30	- id: plan_004
31	  claim: 1
32	  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no
33	    LLM agent'
34	  priority: P1
35	  gpu_budget_hours: 15
36	  deps:
37	  - plan_002
38	- id: plan_005
39	  claim: 2
40	  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding
41	    negatives 何时最有害'
42	  priority: P1
43	  gpu_budget_hours: 5
44	  deps:
45	  - plan_002
46	- id: plan_006
47	  claim: 3
48	  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,
49	    connected-but-not-gold ratio by repo size'
50	  priority: P0
51	  gpu_budget_hours: 0
52	  deps:
53	  - plan_001
54	  registry_id: plan_006_scalability
55	- id: plan_007
56	  claim: 1
57	  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'
58	  priority: P1
59	  gpu_budget_hours: 20
60	  deps:
61	  - plan_001
62	- id: plan_008
63	  claim: 1
64	  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'
65	  priority: P1
66	  gpu_budget_hours: 15
67	  deps:
68	  - plan_001
69	- id: plan_009
70	  claim: 1
71	  description: 'Ablation: fusion head (embedding-only vs structural-features-only
72	    vs combined)'
73	  priority: P1
74	  gpu_budget_hours: 10
75	  deps:
76	  - plan_002
77	- id: plan_010
78	  claim: 1
79	  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'
80	  priority: P2
81	  gpu_budget_hours: 10
82	  deps:
83	  - plan_001
84	- id: plan_011
85	  claim: 1
86	  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether
87	    data-flow helps'
88	  priority: P1
89	  gpu_budget_hours: 5
90	  deps:
91	  - plan_003
92	- id: plan_012
93	  claim: 1
94	  description: 'Qualitative examples: 5-10 cases where structural negatives changed
95	    retrieval outcome'
96	  priority: P2
97	  gpu_budget_hours: 0
98	  deps:
99	  - plan_003
100	- id: plan_013
101	  claim: 1
102	  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,
103	    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'
104	  priority: P0
105	  gpu_budget_hours: 15
106	  deps:
107	  - plan_001
108	  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.
109	    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'
110	  registry_id: plan_013_starcoder
111	  full_registry_id: "m2_full_starcoder"
112	- id: plan_014
113	  claim: 2
114	  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test
115	    regime-specificity of embedding harm'
116	  priority: P1
117	  gpu_budget_hours: 70
118	  deps:
119	  - plan_002
120	  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'
121	- id: plan_015
122	  claim: 2
123	  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per
124	    epoch vs static (mine once from pretrained). Isolate selection criterion from
125	    curriculum shift.'
126	  priority: P1
127	  gpu_budget_hours: 10
128	  deps:
129	  - plan_002
130	  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound
131	    for Claim 2'
132	- id: plan_016
133	  claim: 1
134	  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals
135	    to end-to-end resolve rate evaluation'
136	  priority: P0
137	  gpu_budget_hours: 0
138	  deps:
139	  - plan_003
140	  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical
141	    significance test'
142	- id: plan_017
143	  claim: 1
144	  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,
145	    LocAgent — is StructFuse complementary or alternative?'
146	  priority: P1
147	  gpu_budget_hours: 0
148	  deps:
149	  - plan_002
150	  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'
151	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95760103-a84e-4fd9-beef-a28c2bf4f52b",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "0a2ec95e-5065-430f-ab81-b6d7dd71b8db",
  "sourceToolAssistantUUID": "95760103-a84e-4fd9-beef-a28c2bf4f52b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T08:38:30.467Z_

<details open><summary>🔧 Tool call — Read · `toolu_011mawWsBLukAgAzywZgZ8RT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a2ec95e-5065-430f-ab81-b6d7dd71b8db",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2AAtRBkVcmVeMrUUZoC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51163f17-67e8-4b87-afa8-4f0ee2fd7f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkjYGTDsakmQsT3dGJHQQV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6742,
      "cache_read_input_tokens": 39524,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6742
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 39524,
          "cache_creation_input_tokens": 6742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6742,
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

_source line 33 · 2026-05-14T08:38:30.475Z_

<details><summary>↩ Tool result · `toolu_011mawWsBLukAgAzywZgZ8RT`</summary>

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
  "parentUuid": "51163f17-67e8-4b87-afa8-4f0ee2fd7f56",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "ff089fd2-6c05-4f25-9d18-01054d253fba",
  "sourceToolAssistantUUID": "51163f17-67e8-4b87-afa8-4f0ee2fd7f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-14T08:38:33.526Z_

Now let me check the actual experimental results vs what the dream paper reports, to understand the discrepancy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff089fd2-6c05-4f25-9d18-01054d253fba",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2ABE6co6ToSBYGuVHpX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "557d9f0c-02c7-4ba9-a022-c6e9c6dc4687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V74yRuyissT2kWuM7tNgtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4540,
      "cache_read_input_tokens": 46266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4540,
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

_source line 35 · 2026-05-14T08:38:36.521Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CBEbiXkYwXop6EVxHdGu4V`</summary>

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
  "parentUuid": "557d9f0c-02c7-4ba9-a022-c6e9c6dc4687",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2ABE6co6ToSBYGuVHpX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aaa1e114-2fd1-431c-a326-41fc3a6a0b8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V74yRuyissT2kWuM7tNgtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4540,
      "cache_read_input_tokens": 46266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4540,
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

_source line 36 · 2026-05-14T08:38:36.824Z_

<details open><summary>🔧 Tool call — Read · `toolu_014zfCVofUN54T2Xpg7nxH1D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaa1e114-2fd1-431c-a326-41fc3a6a0b8f",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2ABE6co6ToSBYGuVHpX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6880d59a-f4c2-4371-8ba7-c26c830a2657",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V74yRuyissT2kWuM7tNgtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4540,
      "cache_read_input_tokens": 46266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4540,
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

### Tool result

_source line 37 · 2026-05-14T08:38:36.958Z_

<details><summary>↩ Tool result · `toolu_01CBEbiXkYwXop6EVxHdGu4V`</summary>

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
  "parentUuid": "aaa1e114-2fd1-431c-a326-41fc3a6a0b8f",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "d83a8913-80cd-48fc-939a-5142d077b181",
  "sourceToolAssistantUUID": "aaa1e114-2fd1-431c-a326-41fc3a6a0b8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T08:38:37.139Z_

<details><summary>↩ Tool result · `toolu_014zfCVofUN54T2Xpg7nxH1D`</summary>

```text
1	tier: best
2	narrative_guidance: '9-seed 全量复现完全确认 pilot 模式。Embedding mining 在两个编码器上均显著优于 random（bootstrap
3	  95% CI 不含零）， dataflow 在 Qwen 上提供条件性额外收益而在 StarCoder 上无显著差异，产生干净的交互效应。 SWE-bench
4	  下游验证显示可观测的 resolve rate 提升。机制故事（表征饱和度 → 策略有效性）通过 neg_difficulty margin、 温度消融、动态挖掘对照三条证据线完整闭合。论文三条
5	  claim 均有充分统计支撑，EMNLP Main 定位清晰。
6	
7	  '
8	imagined_experiments:
9	- name: SWE-bench Lite End-to-End Evaluation
10	  plan_id: plan_003
11	  description: 3 strategies × best checkpoint on SWE-bench Lite (300), Qwen3.6-27B
12	    agent, 测 resolve rate
13	  expected_results:
14	    random_resolve_rate: 0.227
15	    embedding_distance_resolve_rate: 0.25
16	    dataflow_aware_resolve_rate: 0.26
17	    embed_vs_random_delta_pp: 2.3
18	    dataflow_vs_random_delta_pp: 3.3
19	    dataflow_vs_embed_delta_pp: 1.0
20	    total_instances: 300
21	    instances_resolved_random: 68
22	    instances_resolved_embed: 75
23	    instances_resolved_dataflow: 78
24	    retrieval_recall1_random: 0.533
25	    retrieval_recall1_embed: 0.556
26	    retrieval_recall1_dataflow: 0.548
27	  result_rationale: 'best 档下 retrieval 质量提升能传导到下游 resolve rate。Qwen best checkpoint
28	    embedding R@1≈0.556 vs random 0.533， 差值 2.3pp 在 300 实例上对应约 7 个额外正确 retrieval →
29	    其中部分转化为 resolve。 转化率不是 1:1（retrieval 改善不等于 repair 改善，LLM agent 有自身能力上限）， 但 best
30	    档假设转化效率约 30-40%，即 ~7 个额外正确 retrieval 中约 2-3 个转为 resolve。 Dataflow 在 Qwen 上的条件性收益（pilot
31	    +0.8pp R@1）进一步贡献约 1pp resolve delta。 总体 swebench_resolve_delta_pp 落在 [2.0, 5.0]
32	    范围的中低段， 因为 retrieval → repair 的衰减是系统性的。SWE-bench Lite 300 实例规模下， 2-3pp 差异虽小但在
33	    best 档下 bootstrap CI 可检测。
34	
35	    '
36	  tables:
37	  - caption: SWE-bench Lite Resolve Rate by Retrieval Strategy
38	    columns:
39	    - Strategy
40	    - Resolve_Rate
41	    - Delta_vs_Random
42	    - Instances_Resolved
43	    rows:
44	    - - random
45	      - 22.7%
46	      - —
47	      - 68
48	    - - embedding_distance
49	      - 25.0%
50	      - +2.3pp
51	      - 75
52	    - - dataflow_aware
53	      - 26.0%
54	      - +3.3pp
55	      - 78
56	  figures_description:
57	  - 'Bar chart: resolve rate × strategy, error bars from bootstrap resampling'
58	  - 'Venn diagram: 3 strategies 各自独立解决的 instances 重叠情况，突出 dataflow-unique solves'
59	  analysis: 'Resolve rate 提升确认 retrieval 质量改善能传导到实际软件工程任务。Dataflow 策略独立解决了 5 个 random/embed
60	    均失败的 instance（多为跨文件 dataflow 依赖），支持 Claim 2 的条件性收益叙事。 Embed 策略独立解决 3 个（多为同文件内近义函数混淆），支持
61	    Claim 1。
62	
63	    '
64	- name: RepoBench-R Cross-File Retrieval Evaluation
65	  plan_id: plan_004
66	  description: 3 strategies × best checkpoint on RepoBench-R, retrieval-only evaluation
67	  expected_results:
68	    random_recall1: 0.412
69	    embedding_distance_recall1: 0.431
70	    dataflow_aware_recall1: 0.438
71	    random_mrr: 0.508
72	    embedding_distance_mrr: 0.529
73	    dataflow_aware_mrr: 0.534
74	    embed_vs_random_R1_delta_pp: 1.9
75	    dataflow_vs_random_R1_delta_pp: 2.6
76	    total_queries: 1200
77	  result_rationale: 'RepoBench-R 是 cross-file retrieval benchmark，天然偏向有结构依赖的查询（import/call
78	    关系）。 在 best 档下，embedding 改善幅度与 SWE-smith 内部 eval 一致（~2pp）， dataflow 的额外收益在此 benchmark
79	    上可能略大于 SWE-smith（因 RepoBench-R 的 cross-file 性质与 dataflow connectivity 天然对齐），但差异不会很大因为训练数据来自
80	    SWE-smith 而非 RepoBench， 存在 domain gap。整体 R@1 低于 SWE-smith 内部 eval（0.41 vs 0.53），
81	    因为 pool size 和 query 分布不同。关键是方向一致且差异可检测。
82	
83	    '
84	  tables:
85	  - caption: RepoBench-R Retrieval Performance
86	    columns:
87	    - Strategy
88	    - R@1
89	    - R@5
90	    - R@10
91	    - MRR
92	    rows:
93	    - - random
94	      - 0.412
95	      - 0.687
96	      - 0.793
97	      - 0.508
98	    - - embedding_distance
99	      - 0.431
100	      - 0.704
101	      - 0.808
102	      - 0.529
103	    - - dataflow_aware
104	      - 0.438
105	      - 0.711
106	      - 0.812
107	      - 0.534
108	  figures_description:
109	  - 'Grouped bar chart: R@1, R@5, R@10 × strategy on RepoBench-R'
110	  analysis: '第二 benchmark 确认 SWE-smith 上的发现不是 benchmark-specific artifact。 策略排序一致（dataflow
111	    ≥ embed > random），增强论文的 external validity。
112	
113	    '
114	- name: Embedding vs Random Stratified Analysis
115	  plan_id: plan_005
116	  description: 按 repo size/complexity 分层，分析 embedding negatives 的收益分布
117	  expected_results:
118	    small_repo_lt50_embed_delta_pp: 0.8
119	    medium_repo_50_200_embed_delta_pp: 2.1
120	    large_repo_200_500_embed_delta_pp: 2.8
121	    xlarge_repo_500plus_embed_delta_pp: 1.5
122	    high_complexity_embed_delta_pp: 2.9
123	    low_complexity_embed_delta_pp: 1.2
124	    correlation_repo_size_vs_delta: 0.31
125	    correlation_complexity_vs_delta: 0.42
126	  result_rationale: 'best 档下 embedding mining 普遍有效但收益分布不均。中大型 repo（50-500 files）收益最大，
127	    因为 pool 中有足够多的 near-miss 候选（lexically similar but not gold）， embedding mining
128	    能有效挑选最有信息量的 hard negatives。小型 repo pool 太小、 embedding mining 退化为近似 random；超大型
129	    repo 结构复杂度使得 embedding distance 与 relevance 的相关性下降（太多 "远但相关" 的文件）。Complexity（cyclomatic
130	    complexity 或 import depth）比 size 更好地预测 embedding mining 收益， 因为高复杂度代码中相似但无关的文件更多。
131	
132	    '
133	  tables:
134	  - caption: Embedding Mining Benefit by Repo Tier
135	    columns:
136	    - Tier
137	    - N_Instances
138	    - Embed_R1
139	    - Random_R1
140	    - Delta_pp
141	    rows:
142	    - - small (<50)
143	      - 500
144	      - 0.568
145	      - 0.56
146	      - '+0.8'
147	    - - medium (50-200)
148	      - 4096
149	      - 0.551
150	      - 0.53
151	      - '+2.1'
152	    - - large (200-500)
153	      - 13628
154	      - 0.542
155	      - 0.514
156	      - '+2.8'
157	    - - xlarge (500+)
158	      - 25949
159	      - 0.528
160	      - 0.513
161	      - '+1.5'
162	  figures_description:
163	  - 'Scatter plot: repo complexity vs embed-random delta, with regression line'
164	  - 'Box plot: delta distribution by repo size tier'
165	  analysis: '收益分布分析提供 practical guidance：embedding mining 对中大型项目最有效， 与表征空间中 near-miss
166	    候选密度的直觉一致。复杂度比 size 更具预测力， 提示 negative mining 策略选择应考虑代码结构特征而非简单规模。
167	
168	    '
169	- name: Hop Distance Ablation
170	  plan_id: plan_007
171	  description: 1-hop vs 2-hop vs 3-hop call-graph bounding for dataflow extraction
172	  expected_results:
173	    hop1_connected_rate: 0.12
174	    hop2_connected_rate: 0.34
175	    hop3_connected_rate: 0.58
176	    hop1_z_pct: 0.18
177	    hop2_z_pct: 0.41
178	    hop3_z_pct: 0.62
179	    hop2_qwen_R1: 0.548
180	    hop1_qwen_R1: 0.541
181	    hop3_qwen_R1: 0.544
182	    hop2_extraction_time_s: 8.9
183	    hop3_extraction_time_s: 23.4
184	  result_rationale: '2-hop 是 sweet spot。1-hop 太严格：大多数 repo 中直接 dataflow 连接的文件对稀少（12%），
185	    导致 connected-not-gold set 太小，dataflow negative mining 退化为近似 random。 3-hop 太宽松：58%
186	    的文件对被标记为 connected，negative pool 被过度稀释， 且提取时间增长 2.6x（路径爆炸）。2-hop（当前默认）在 coverage（34%）和
187	    selectivity（Z=41%）之间取得平衡，R@1 最高。这一结果支持 Claim 3 中的 "scope-bounded" 设计选择。
188	
189	    '
190	  tables:
191	  - caption: Hop Distance Impact on Extraction and Training
192	    columns:
193	    - Hops
194	    - Connected_Rate
195	    - Z_Pct
196	    - Extraction_Time_s
197	    - Qwen_R1
198	    rows:
199	    - - 1
200	      - 12%
201	      - 18%
202	      - 4.2
203	      - 0.541
204	    - - 2
205	      - 34%
206	      - 41%
207	      - 8.9
208	      - 0.548
209	    - - 3
210	      - 58%
211	      - 62%
212	      - 23.4
213	      - 0.544
214	  figures_description:
215	  - 'Line chart: R@1 vs hop distance, with extraction time on secondary y-axis'
216	  analysis: '2-hop 最优确认了设计选择的合理性。3-hop 的 R@1 回落说明过度扩展 connectivity 范围会引入噪声连接，削弱 structural
217	    negative 的信息量。
218	
219	    '
220	- name: Training Data Size Scaling
221	  plan_id: plan_008
222	  description: 1K vs 3K vs 5K training instances, 测 strategy 收益是否随数据量变化
223	  expected_results:
224	    1k_random_R1: 0.498
225	    1k_embed_R1: 0.521
226	    1k_dataflow_R1: 0.518
227	    3k_random_R1: 0.525
228	    3k_embed_R1: 0.548
229	    3k_dataflow_R1: 0.543
230	    5k_random_R1: 0.533
231	    5k_embed_R1: 0.556
232	    5k_dataflow_R1: 0.548
233	    embed_delta_1k: 2.3
234	    embed_delta_3k: 2.3
235	    embed_delta_5k: 2.3
236	    dataflow_delta_1k: 2.0
237	    dataflow_delta_3k: 1.8
238	    dataflow_delta_5k: 1.5
239	  result_rationale: 'best 档下 embedding mining 的收益对数据量 robust（~2.3pp 几乎不变）， 因为 embedding
240	    distance 提供的信息增益是 strategy-intrinsic 的，不依赖数据量。 Dataflow 收益随数据量增加略有递减（2.0→1.5pp），因为更多数据使
241	    random baseline 也能隐式覆盖部分结构相关的 hard negatives（大数定律），缩小了 dataflow 的 marginal 贡献。但即使在
242	    5K 下，dataflow 在 Qwen 上的条件性收益仍然存在。 绝对性能随数据量单调增长但边际递减（符合 neural scaling 预期）。
243	
244	    '
245	  tables:
246	  - caption: Strategy Benefit by Training Data Size
247	    columns:
248	    - Size
249	    - Random_R1
250	    - Embed_R1
251	    - Embed_Delta
252	    - Dataflow_R1
253	    - DF_Delta
254	    rows:
255	    - - 1K
256	      - 0.498
257	      - 0.521
258	      - '+2.3'
259	      - 0.518
260	      - '+2.0'
261	    - - 3K
262	      - 0.525
263	      - 0.548
264	      - '+2.3'
265	      - 0.543
266	      - '+1.8'
267	    - - 5K
268	      - 0.533
269	      - 0.556
270	      - '+2.3'
271	      - 0.548
272	      - '+1.5'
273	  figures_description:
274	  - 'Line chart: R@1 vs data size, 3 lines for 3 strategies, showing parallel scaling
275	    for embed and convergence for dataflow'
276	  analysis: 'Embedding mining 收益的 scale-invariance 强化 Claim 1（普遍有效）。 Dataflow 收益的轻微递减可解释为
277	    "structural signal 被 larger random samples 部分替代"， 但不消失——支持 Claim 2 的 "conditional
278	    benefit" 定位。
279	
280	    '
281	- name: Fusion Head Ablation
282	  plan_id: plan_009
283	  description: Embedding-only vs structural-features-only vs combined fusion head
284	  expected_results:
285	    embed_only_R1: 0.556
286	    structural_only_R1: 0.487
287	    combined_R1: 0.549
288	    embed_only_vs_combined_delta: 0.7
289	  result_rationale: 'best 档下的核心发现是 embedding-only 已经很强（因为我们的方法是 training-time mining
290	    而非 inference-time fusion）。Structural-features-only 单独很弱（R@1=0.487， 低于 random baseline
291	    的 0.533），说明结构信息不能替代语义相似度，只能补充。 Combined fusion head 反而比 embed-only 略低（0.549 vs
292	    0.556），因为加入 structural features 作为 inference-time signal 引入噪声（CodeQL extraction
293	    覆盖率仅 34%， inference 时 missing features 是常态）。这一结果强化论文叙事：结构信息的价值在于 training-time
294	    negative mining（改善表征学习），而非 inference-time feature。
295	
296	    '
297	  tables:
298	  - caption: Fusion Head Comparison (Qwen, best checkpoint)
299	    columns:
300	    - Head
301	    - R@1
302	    - R@5
303	    - Note
304	    rows:
305	    - - embed_only
306	      - 0.556
307	      - 0.961
308	      - Our default
309	    - - structural_only
310	      - 0.487
311	      - 0.872
312	      - Below random baseline
313	    - - combined
314	      - 0.549
315	      - 0.958
316	      - Marginal degradation vs embed_only
317	  figures_description:
318	  - 'Bar chart: R@1 by fusion head type'
319	  analysis: 'Ablation 清晰区分了 structural information 的两种使用方式：training-time mining（有效）
320	    vs inference-time feature（无效或有害）。这是对 inference-time graph methods （CodexGraph,
321	    LocAgent）的重要区分点，支持 plan_017 的讨论。
322	
323	    '
324	- name: Dataflow-Distance Weighted Negatives
325	  plan_id: plan_010
326	  description: Binary connected/disconnected vs dataflow-distance weighted negative
327	    sampling
328	  expected_results:
329	    binary_qwen_R1: 0.548
330	    weighted_qwen_R1: 0.551
331	    binary_starcoder_R1: 0.489
332	    weighted_starcoder_R1: 0.49
333	    weighted_vs_binary_qwen_delta: 0.3
334	    weighted_vs_binary_starcoder_delta: 0.1
335	  result_rationale: 'Distance-weighted sampling 对 Qwen 有微弱额外收益（+0.3pp），因为在饱和空间中 更细粒度的
336	    difficulty gradation 提供略好的 curriculum 效果——离 gold 越远的 disconnected file 越 "easy"，给予更低采样权重，让训练集中在
337	    hard disconnected 上。 但差异很小因为 binary 已经是一个合理的 proxy（connected vs disconnected 的
338	    distinction 捕获了主要信号）。StarCoder 上差异可忽略，与 Claim 2 一致—— dataflow 信号在非饱和空间中 marginal，更细的
339	    granularity 自然也 marginal。 总体结论：binary 足够，weighted 是 diminishing return。
340	
341	    '
342	  tables:
343	  - caption: Binary vs Weighted Dataflow Negatives
344	    columns:
345	    - Method
346	    - Qwen_R1
347	    - StarCoder_R1
348	    rows:
349	    - - binary (default)
350	      - 0.548
351	      - 0.489
352	    - - distance-weighted
353	      - 0.551
354	      - 0.49
355	  figures_description:
356	  - 'Histogram: negative difficulty distribution under binary vs weighted sampling'
357	  analysis: 'Binary 简单且接近最优，weighted 的微弱改善不足以 justify 额外复杂度。 这一 negative result 反而简化了方法描述——"disconnected
358	    = hard negative" 无需更复杂的定义。
359	
360	    '
361	- name: SWE-bench Failure Analysis
362	  plan_id: plan_011
363	  description: 50 个 SweRank/BM25 failures，按 dataflow 是否 help 分类
364	  expected_results:
365	    total_failures_analyzed: 50
366	    dataflow_helps_count: 18
367	    dataflow_helps_pct: 36
368	    failure_categories:
369	      cross_file_dependency: 14
370	      same_file_semantic: 12
371	      missing_context: 10
372	      llm_reasoning_failure: 8
373	      other: 6
374	    dataflow_helps_by_category:
375	      cross_file_dependency: 11
376	      same_file_semantic: 3
377	      missing_context: 3
378	      llm_reasoning_failure: 1
379	      other: 0
380	  result_rationale: '36% 的 BM25/SweRank failure 中 dataflow mining 能提供帮助——这些 case 主要是
381	    cross-file dependency 类型（gold file 与 query file 有 dataflow 连接但 lexical similarity
382	    低）。这个比例与 Z%=41%（connected-not-gold rate）高度一致： 如果 ~40% 的 instances 有 structural
383	    signal 可利用，那么在 failures 中 dataflow helps 的比例也应在类似量级。Same-file semantic failures
384	    中 dataflow 偶尔帮助（因为相同文件内的函数调用也被 dataflow graph 捕获），但这不是主要机制。 LLM reasoning failures
385	    与 retrieval 无关，dataflow 自然无法帮助。
386	
387	    '
388	  tables:
389	  - caption: 'Failure Analysis: Where Dataflow Helps'
390	    columns:
391	    - Category
392	    - Count
393	    - DF_Helps
394	    - DF_Help_Rate
395	    rows:
396	    - - cross_file_dependency
397	      - 14
398	      - 11
399	      - 79%
400	    - - same_file_semantic
401	      - 12
402	      - 3
403	      - 25%
404	    - - missing_context
405	      - 10
406	      - 3
407	      - 30%
408	    - - llm_reasoning_failure
409	      - 8
410	      - 1
411	      - 12%
412	    - - other
413	      - 6
414	      - 0
415	      - 0%
416	  figures_description:
417	  - 'Stacked bar chart: failure categories with dataflow-helps overlay'
418	  - 3 representative case studies with retrieval ranking diff
419	  analysis: 'Dataflow 最大价值在 cross-file dependency failures（79% help rate）， 精确对齐了 Claim
420	    2 的 "structural dimension the encoder cannot separate via text alone" 叙事。
421	
422	    '
423	- name: Qualitative Case Studies
424	  plan_id: plan_012
425	  description: 5-10 个 structural negatives 改变 retrieval outcome 的代表性 case
426	  expected_results:
427	    total_cases: 8
428	    categories:
429	      import_chain_recovery: 3
430	      utility_vs_core_disambiguation: 2
431	      test_file_suppression: 2
432	      config_dependency_detection: 1
433	  result_rationale: 'best 档下可以找到 8 个 clean case studies，覆盖四种典型模式。 Import chain recovery
434	    最多（3 个），因为这是 dataflow connectivity 最直接的信号类型： gold file 通过 import chain 与 query
435	    file 连接，但 lexical similarity 很低（不同功能模块）， random/embed mining 无法区分 "lexically similar
436	    but structurally irrelevant" negatives。 Utility vs core disambiguation（2 个）展示
437	    dataflow 如何将 utils.py 类文件正确 判断为 connected（有 dataflow 到 core 的数据流）而非 false negative。
438	    Test file suppression（2 个）展示 test files 虽 lexically similar 但 dataflow disconnected，被正确降权。
439	
440	    '
441	  tables: []
442	  figures_description:
443	  - 'Figure: 4-panel case study，每 panel 展示 query、gold、top-3 retrieval（random vs dataflow），附
444	    dataflow graph 子图'
445	  analysis: 'Case studies 提供 mechanistic evidence 的具体实例化，让 reviewer 直观理解 "structural
446	    dimension" 到底意味着什么。选择覆盖四种不同模式以展示 generality。
447	
448	    '
449	- name: Temperature Ablation
450	  plan_id: plan_014
451	  description: τ ∈ {0.05, 0.1, 0.2} × 3 strategies × Qwen, 测 regime-specificity
452	  expected_results:
453	    tau_005:
454	      random_R1: 0.518
455	      embed_R1: 0.542
456	      dataflow_R1: 0.539
457	      embed_delta: 2.4
458	      dataflow_delta: 2.1
459	    tau_010:
460	      random_R1: 0.533
461	      embed_R1: 0.556
462	      dataflow_R1: 0.548
463	      embed_delta: 2.3
464	      dataflow_delta: 1.5
465	    tau_020:
466	      random_R1: 0.521
467	      embed_R1: 0.539
468	      dataflow_R1: 0.53
469	      embed_delta: 1.8
470	      dataflow_delta: 0.9
471	    optimal_tau: 0.1
472	    embed_benefit_robust_across_tau: true
473	    dataflow_benefit_strongest_at_low_tau: true
474	  result_rationale: 'best 档下 embedding mining 在所有 τ 值下均有正收益（1.8-2.4pp），确认 Claim 1
475	    的 robustness。τ=0.1 是 sweet spot（pilot 已用的值），R@1 最高。τ=0.05 过低导致 contrastive loss
476	    landscape 太 sharp，所有 strategy 绝对性能下降但 relative ranking 不变。 τ=0.2 过高使 loss 过于平滑，strategy
477	    差异缩小。Dataflow 收益随 τ 增大而递减 （2.1→1.5→0.9pp），因为高温度下 contrastive loss 对 hard vs easy
478	    negatives 的 区分度降低，structural difficulty gradient 被稀释。这一发现提供了 mechanistic insight：
479	    dataflow 的 value proposition 是提供更 hard 的 negatives， 而 temperature 控制了 model 对
480	    hardness 的敏感度。
481	
482	    '
483	  tables:
484	  - caption: Temperature × Strategy Interaction (Qwen)
485	    columns:
486	    - τ
487	    - Random_R1
488	    - Embed_R1
489	    - Embed_Δ
490	    - DF_R1
491	    - DF_Δ
492	    rows:
493	    - - 0.05
494	      - 0.518
495	      - 0.542
496	      - '+2.4'
497	      - 0.539
498	      - '+2.1'
499	    - - 0.1
500	      - 0.533
501	      - 0.556
502	      - '+2.3'
503	      - 0.548
504	      - '+1.5'
505	    - - 0.2
506	      - 0.521
507	      - 0.539
508	      - '+1.8'
509	      - 0.53
510	      - '+0.9'
511	  figures_description:
512	  - 'Line chart: R@1 vs τ, 3 strategy lines, 显示 strategy gap 随 τ 变化'
513	  - 'Heatmap: τ × strategy interaction strength (delta from random)'
514	  analysis: 'Temperature 消融排除了 "finding is τ-specific" 的 reviewer concern。 Embedding
515	    benefit 对 τ robust；dataflow benefit 在低 τ 下最强， 提供 practitioner guidance（如果 encoder
516	    空间饱和 + 低温度 → dataflow 最有价值）。
517	
518	    '
519	- name: Dynamic Embedding Mining Baseline
520	  plan_id: plan_015
521	  description: 每 epoch 重新 mine embedding negatives vs 静态一次性 mine，隔离 selection criterion
522	    和 curriculum shift
523	  expected_results:
524	    static_embed_R1: 0.556
525	    dynamic_embed_R1: 0.561
526	    dynamic_vs_static_delta: 0.5
527	    dynamic_dataflow_R1: 0.552
528	    static_dataflow_R1: 0.548
529	    dynamic_training_time_multiplier: 2.8
530	  result_rationale: 'Dynamic mining 提供微弱改善（+0.5pp），因为随训练进行 encoder representation
531	    会 drift， 重新 mine 能保持 negatives 的 hardness。但差异很小（<1pp），说明 static mining 在 3 epoch
532	    短训练中 drift 不严重——pretrained encoder 的 representation 在 LoRA fine-tune 中变化有限（LoRA
533	    rank=16，参数量仅为全量的 0.3%）。 关键发现：static vs dynamic 的差异远小于 strategy 差异（embed vs random
534	    = 2.3pp vs dynamic vs static = 0.5pp），确认 selection criterion（embedding distance
535	    vs random） 是 primary driver，而非 curriculum shift。这排除了 "embed helps only because
536	    of implicit curriculum" 的 alternative explanation。 Dynamic 的 2.8x 训练时间开销使其不实用。
537	
538	    '
539	  tables:
540	  - caption: Static vs Dynamic Mining
541	    columns:
542	    - Mining
543	    - Strategy
544	    - R1
545	    - Training_Time_h
546	    rows:
547	    - - static
548	      - embedding
549	      - 0.556
550	      - 3.2
551	    - - dynamic
552	      - embedding
553	      - 0.561
554	      - 9.0
555	    - - static
556	      - dataflow
557	      - 0.548
558	      - 3.2
559	    - - dynamic
560	      - dataflow
561	      - 0.552
562	      - 9.0
563	  figures_description:
564	  - 'Bar chart: static vs dynamic × strategy, with training time annotation'
565	  analysis: 'Static mining 在成本效益上远优于 dynamic。更重要的是，排除了 curriculum confound： embedding
566	    mining 的收益来自 selection criterion 本身（挑到 truly hard negatives）， 而非 training dynamics。
567	
568	    '
569	- name: Bootstrap CI for SWE-bench Lite
570	  plan_id: plan_016
571	  description: 9-seed × 3 strategies 的 bootstrap 95% CI for resolve rate
572	  expected_results:
573	    random_resolve_mean: 0.227
574	    random_resolve_ci:
575	    - 0.195
576	    - 0.259
577	    embed_resolve_mean: 0.25
578	    embed_resolve_ci:
579	    - 0.218
580	    - 0.282
581	    dataflow_resolve_mean: 0.26
582	    dataflow_resolve_ci:
583	    - 0.226
584	    - 0.294
585	    embed_vs_random_delta_mean: 2.3
586	    embed_vs_random_delta_ci:
587	    - 0.4
588	    - 4.2
589	    embed_vs_random_p_value: 0.012
590	    dataflow_vs_random_delta_ci:
591	    - 0.5
592	    - 5.8
593	    dataflow_vs_random_p_value: 0.008
594	    bootstrap_iterations: 10000
595	  result_rationale: '300 instances × 9 seeds 提供足够的 bootstrap 统计量力。best 档下 embed_vs_random
596	    的 95% CI 不含零（[0.4, 4.2]pp），p=0.012，通过显著性检验。 CI 宽度 ~4pp 反映 SWE-bench 300 的固有 variance（每个
597	    instance 是 binary outcome， binomial variance 较大）。9 seeds 降低了 training variance
598	    的贡献， 但 evaluation set size（300）是 CI 宽度的主要 bottleneck。 Cross-seed R@1 标准差 ~1.0pp（在
599	    [0.5, 1.5] 范围内）， 确认 training 方差可控。Dataflow CI 也不含零但上界更宽（[0.5, 5.8]）， 反映条件性收益的
600	    inherent higher variance。
601	
602	    '
603	  tables:
604	  - caption: Bootstrap 95% CI for SWE-bench Lite Resolve Rate
605	    columns:
606	    - Comparison
607	    - Delta_pp
608	    - 95% CI
609	    - p_value
610	    - Significant
611	    rows:
612	    - - embed vs random
613	      - '+2.3'
614	      - '[0.4, 4.2]'
615	      - 0.012
616	      - 'Yes'
617	    - - dataflow vs random
618	      - '+3.3'
619	      - '[0.5, 5.8]'
620	      - 0.008
621	      - 'Yes'
622	    - - dataflow vs embed
623	      - '+1.0'
624	      - '[-0.8, 2.8]'
625	      - 0.134
626	      - 'No'
627	  figures_description:
628	  - 'Forest plot: pairwise strategy comparisons with bootstrap CIs'
629	  - 'Violin plot: per-seed resolve rates by strategy'
630	  analysis: 'Embed vs random 和 dataflow vs random 均显著，但 dataflow vs embed 不显著 （CI
631	    含零）。这精确对应 Claim 2 的 "conditional" 定位——dataflow 相对 random 有显著收益 但相对 embed 的 incremental
632	    在 300 instances 上力度不足。论文可如实报告此 pattern 并讨论 statistical power limitation。
633	
634	    '
635	- name: Inference-Time Graph Method Comparison Discussion
636	  plan_id: plan_017
637	  description: 与 CodexGraph, LocAgent 等 inference-time graph methods 的概念对比与定位
638	  expected_results:
639	    comparison_dimensions: 4
640	    structfuse_strengths:
641	    - training-time, no inference overhead
642	    - model-agnostic mining
643	    - compatible with any retriever
644	    inference_methods_strengths:
645	    - dynamic graph, adapts to query
646	    - no precomputation needed
647	    - can leverage runtime call stacks
648	    complementarity_score: high
649	    empirical_comparison: not applicable (different paradigm)
650	  result_rationale: '这是 discussion section 的概念分析而非实验。best 档下不需要实际跑 inference-time
651	    baselines（GPU budget=0），而是提供清晰的 taxonomy：StructFuse 是 training-time structural
652	    signal injection（改善表征学习），inference-time methods 是 navigation-time structural signal（改善检索路径）。两者
653	    complementary 而非 competitive。 核心区别：StructFuse 是 offline（一次 mine、反复 train），inference
654	    methods 是 online（每次 query 重新构建 graph）。StructFuse 的 overhead 在 training 时 已 amortize，inference
655	    零成本；inference methods 每次 query 有额外延迟。 但 inference methods 能适应 query-specific context（如运行时调用栈），StructFuse
656	    不能。
657	
658	    '
659	  tables:
660	  - caption: Training-Time vs Inference-Time Structural Methods
661	    columns:
662	    - Dimension
663	    - StructFuse
664	    - CodexGraph_LocAgent
665	    rows:
666	    - - Signal injection
667	      - Training (negative mining)
668	      - Inference (graph navigation)
669	    - - Inference overhead
670	      - Zero
671	      - Per-query graph traversal
672	    - - Graph freshness
673	      - Static (pretrained)
674	      - Dynamic (query-adaptive)
675	    - - Compatibility
676	      - Any contrastive retriever
677	      - Specific agent framework
678	  figures_description:
679	  - 'Taxonomy figure: 2×2 matrix (training/inference × structural/textual) positioning
680	    StructFuse and related work'
681	  analysis: '清晰定位避免了 "why not compare with X" 的 reviewer 质疑。 Complementarity framing
682	    开启了 future work 方向（combine training-time mining + inference-time navigation）。
683	
684	    '
685	- name: M2 Full Qwen 9-Seed Results
686	  plan_id: 'plan_002 (full: m2_full_qwen)'
687	  description: 9 seeds × 3 strategies, Qwen2.5-Coder-3B, 全量 3-strategy 对比
688	  expected_results:
689	    random_mean_R1: 0.533
690	    random_std_R1: 0.008
691	    random_seeds:
692	    - 0.527
693	    - 0.53
694	    - 0.531
695	    - 0.533
696	    - 0.534
697	    - 0.535
698	    - 0.536
699	    - 0.538
700	    - 0.54
701	    embedding_mean_R1: 0.556
702	    embedding_std_R1: 0.009
703	    embedding_seeds:
704	    - 0.547
705	    - 0.55
706	    - 0.553
707	    - 0.555
708	    - 0.556
709	    - 0.558
710	    - 0.559
711	    - 0.561
712	    - 0.564
713	    dataflow_mean_R1: 0.548
714	    dataflow_std_R1: 0.01
715	    dataflow_seeds:
716	    - 0.538
717	    - 0.541
718	    - 0.544
719	    - 0.547
720	    - 0.548
721	    - 0.55
722	    - 0.552
723	    - 0.555
724	    - 0.558
725	    embed_vs_random_delta_pp: 2.3
726	    dataflow_vs_random_delta_pp: 1.5
727	    dataflow_vs_embed_delta_pp: -0.8
728	    embed_vs_random_bootstrap_p: 0.003
729	    dataflow_vs_random_bootstrap_p: 0.018
730	    cross_seed_R1_std_max: 1.0
731	    best_checkpoint_step: 1000
732	    step_1000_overfitting: controlled via early stopping at step 500-1000
733	  result_rationale: 'Pilot 数据（单 seed）显示 random=0.5357, embed=0.5557, dataflow=0.5436。
734	    best 档下 9-seed 平均值保持一致趋势但因 seed variance 略有修正。 Qwen pos_sim=0.9855 的饱和空间使 random
735	    negatives 太 easy（margin=0.074）， embedding mining 有效因为挑选 harder negatives（margin=0.017）。
736	    Dataflow 的条件性收益（+1.5pp vs random）通过更 hard 的 structural negatives 进一步压缩 margin（margin=0.029），但
737	    incremental 小于 embed 因为 embedding distance 已经捕获了大部分 difficulty gradient。Cross-seed
738	    std ~0.8-1.0pp， 在 [0.5, 1.5] 范围内，说明 training 方差可控。Step 1000 过拟合通过 early stopping
739	    at best validation loss 解决，不影响结论。
740	
741	    '
742	  tables:
743	  - caption: 'M2 Full Qwen: 9-Seed Summary'
744	    columns:
745	    - Strategy
746	    - Mean_R1
747	    - Std_R1
748	    - 95% CI
749	    - Best_Step
750	    rows:
751	    - - random
752	      - 0.533
753	      - 0.008
754	      - '[0.527, 0.539]'
755	      - 1000
756	    - - embedding_distance
757	      - 0.556
758	      - 0.009
759	      - '[0.549, 0.563]'
760	      - 1000
761	    - - dataflow_aware
762	      - 0.548
763	      - 0.01
764	      - '[0.540, 0.556]'
765	      - 500-1000
766	  figures_description:
767	  - 'Box plot: per-seed R@1 by strategy, 9 points each'
768	  - 'Learning curve: val_loss vs step, 3 strategies × 9 seeds (band plot)'
769	  analysis: '9-seed 全量结果是论文的 primary evidence for Claims 1 & 2。 Embedding > random
770	    的 p=0.003 提供强统计支持。 Dataflow > random 的 p=0.018 提供充分支持但力度略弱（higher variance）， 精确对应
771	    "conditional benefit" 叙事。
772	
773	    '
774	- name: M2 Full StarCoder 9-Seed Results
775	  plan_id: 'plan_002 (full: m2_full_starcoder)'
776	  description: 9 seeds × 3 strategies, StarCoder2-3B, 全量交互效应验证
777	  expected_results:
778	    random_mean_R1: 0.49
779	    random_std_R1: 0.009
780	    embedding_mean_R1: 0.507
781	    embedding_std_R1: 0.01
782	    dataflow_mean_R1: 0.488
783	    dataflow_std_R1: 0.011
784	    embed_vs_random_delta_pp: 1.7
785	    dataflow_vs_random_delta_pp: -0.2
786	    embed_vs_random_bootstrap_p: 0.008
787	    dataflow_vs_random_bootstrap_p: 0.62
788	    cross_seed_R1_std_max: 1.1
789	  result_rationale: 'StarCoder pos_sim=0.7985（健康空间），random negatives 已提供足够 difficulty
790	    gradient （margin=0.194）。Embedding mining 仍然有效（+1.7pp, p=0.008），因为 embedding distance
791	    选择的 negatives 更 informative regardless of space geometry——这是 Claim 1 的关键证据 （两个编码器均显著）。Dataflow
792	    在 StarCoder 上无显著差异（-0.2pp, p=0.62）， 产生干净的交互效应：dataflow 的 structural negatives
793	    在非饱和空间中不提供 beyond-embedding 的信息增量，因为 encoder 已能通过 text alone 区分结构上不同的文件。 这一 null
794	    result 是论文 mechanistic story 的关键支撑—— 不是所有方法在所有条件下都有效，而是有清晰的条件边界。
795	
796	    '
797	  tables:
798	  - caption: 'M2 Full StarCoder: 9-Seed Summary'
799	    columns:
800	    - Strategy
801	    - Mean_R1
802	    - Std_R1
803	    - 95% CI
804	    - p_vs_random
805	    rows:
806	    - - random
807	      - 0.49
808	      - 0.009
809	      - '[0.483, 0.497]'
810	      - —
811	    - - embedding_distance
812	      - 0.507
813	      - 0.01
814	      - '[0.499, 0.515]'
815	      - 0.008
816	    - - dataflow_aware
817	      - 0.488
818	      - 0.011
819	      - '[0.479, 0.497]'
820	      - 0.62
821	  figures_description:
822	  - 'Interaction plot: encoder × strategy, 显示 Qwen 和 StarCoder 的 dataflow 交互效应'
823	  analysis: StarCoder 的 clean null result for dataflow 是论文 strongest mechanistic evidence。
824	    两编码器的交互效应 pattern（embed always helps, dataflow conditional on saturation） 完美对应表征空间几何学解释。
825	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6880d59a-f4c2-4371-8ba7-c26c830a2657",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a3675f4a8d53881c9",
  "type": "user",
  "uuid": "2ed800d6-533c-4184-b98a-46f5cfc82bc6",
  "sourceToolAssistantUUID": "6880d59a-f4c2-4371-8ba7-c26c830a2657",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-14T08:40:06.790Z_

I now have a thorough understanding of the project. Let me now compare the paper under review (the "actual results" title from the user's prompt) against the dream "best" paper and the actual experimental state. The critical observation is that the user's prompt provides results from a **different version** of the paper -- one with a "negative/cautionary" framing where full-scale results showed no significant differences, versus the dream "best" paper where everything worked. Let me formulate my review.

---

## Reviewer 1 (R1): Method & Experiment Review

**Paper**: "A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval"

---

### 1. Methodology Evaluation

**Experimental Design**

The core design -- 54 full-scale runs (9 seeds x 3 strategies x 2 encoders) -- is commendable and exceeds the standard in the field. The use of 9 random seeds per condition is significantly above the typical 1-3 seeds in code retrieval papers, enabling meaningful variance estimation. The choice to compare against a pilot study at smaller scale (2K vs 15K instances) and document how findings change with scale is a valuable methodological contribution.

However, several design issues weaken the conclusions:

- **Confounded pilot-to-full comparison.** The pilot uses ~2K instances from 8 repos; full-scale uses 15K instances from 123 repos. The transition changes *both* data volume *and* data distribution simultaneously (Table 9: structural_rate 0.58 to 0.34, files/repo 45 to 185, large repos 30% to 56%). The paper attributes the vanishing effect to scale, but it could equally be a distribution shift artifact. The "data-size-benefit scaling law" of -0.11pp/1K instances (Table 7) attempts to isolate the scale factor, but if this experiment was run on the full 15K data by subsampling, it shares the same distribution and does not reproduce the pilot's 8-repo distribution.

- **Static mining only.** All negatives are mined once from pretrained encoders and remain fixed during training. Table 14 shows dynamic mining at -0.3pp vs static, -0.5pp vs random, but these results are for the full-scale setting where everything is null anyway. The static-vs-dynamic comparison would be more informative in the pilot setting where embedding mining showed a signal.

- **Single task domain.** Bug report to file retrieval using SWE-smith data only. The generalizability claim is limited.

**Statistical Methods**

The statistical approach is mixed:

- *Strengths*: Bootstrap resampling is appropriate for the SWE-bench binary outcomes. Reporting 95% CIs throughout is good practice.
- *Weaknesses*: The paper reports bootstrap p >= 0.68 for strategy comparisons at full scale, which is appropriate, but does not report effect sizes (Cohen's d or similar) alongside p-values. With std ~3pp and deltas <1pp, effect sizes would quantify just how small the differences are. The "scaling law" fit (Table 7, slope -0.11pp/1K) is based on 4 data points (1K, 3K, 5K, 15K) -- calling this a "scaling law" overstates the evidence from what is essentially a linear fit through 4 points.

**Method-Level Issues**

- The dataflow-aware strategy definition conflates two criteria: (a) dataflow-disconnected from gold AND (b) high embedding similarity. This means dataflow negatives are a *subset* of embedding negatives filtered by structural disconnection. The paper does not clearly delineate whether the null result at scale is because the filtering step has no value, or because the base embedding mining itself has no value at scale.
- The paper title frames this as about "hard negative mining fragility," but the actual finding is more nuanced: it is about pilot-to-full-scale replication failure, possibly driven by distribution shift rather than inherent fragility of the methods.

---

### 2. Experiment Completeness

Comparing against the 16-item experiment plan:

| # | Experiment | Status | Assessment |
|---|-----------|--------|------------|
| 1 | M2 Full Qwen (9 seeds x 3) | Table 1 | Covered |
| 2 | M2 Full StarCoder (9 seeds x 3) | Table 2 | Covered |
| 3 | SWE-bench Lite | Table 3-4 | Covered but results are very weak (deltas ~0.3pp, McNemar p=0.89) |
| 4 | RepoBench-R | Table 5 | Covered, shows marginal differences |
| 5 | Stratified Analysis | Table 8 | **Incomplete** -- neg_difficulty quartile analysis and scatter plot are missing |
| 6 | Hop-Distance Ablation | Table 12 | Covered |
| 7 | Training Data Scaling | Table 7 | Covered |
| 8 | Fusion Head Ablation | Table 13 | Covered |
| 9 | Dataflow-Distance Weighted | Brief mention in section 6.5 | **Incomplete** -- no table, no quantitative results |
| 10 | Failure Analysis (50 cases) | Table 10 | Covered but concerning: only 6 cases where dataflow "could help," 2 actually helped, 3 hurt |
| 11 | Qualitative Examples | Not present | **Missing entirely** |
| 12 | Temperature Ablation | Table 11 | Covered, but result (random best at all tau) contradicts the initial motivation |
| 13 | Dynamic vs Static Mining | Table 14 | Covered |
| 14 | Bootstrap CI SWE-bench | Table 4 | Covered |
| 15 | Inference-Time Graph Discussion | Table 6 | Covered but unfavorable: LocAgent 26.2% vs ours ~19% |
| 16 | Data Pipeline Distribution Audit | Table 9 | Covered |

**Missing/Incomplete**: Items 5, 9, 11 are missing or incomplete. Item 9 (dataflow-distance weighting) would be particularly important given that the binary approach showed null results -- was a continuous version tried? Item 11 (qualitative examples) could help readers understand *why* the methods failed at scale.

**Depth concerns**: Several experiments are present but shallow. Table 10 (failure analysis) shows only 2/50 cases where dataflow actually helped -- this is devastatingly low and the paper should discuss this more prominently. Table 8 (stratified by repo size) shows inconsistent patterns across tiers with no clear trend, undermining any mechanistic explanation.

---

### 3. Result Credibility

**Do results support the claims?**

The paper's main claim -- that pilot-level signals vanish at scale -- is well-supported by the data. The 9-seed full-scale comparisons convincingly show <1pp differences with p >= 0.68. This is a genuine negative result.

However, several aspects undermine credibility:

**(a) Internal contradiction with the scaling analysis.** Table 7 shows the "scaling law" with positive deltas at small scale (1K: +1.3pp, 3K: +0.5pp) shrinking to negative at 15K (-0.2pp). But Table 1 full-scale means at 15K show random *ahead* of embedding (0.523 vs 0.521). If the scaling experiment was done by subsampling the 15K full-scale data, then the 1K/3K results are from the same *distribution* as 15K, meaning the pilot's +1.6-2.0pp at 2K cannot be explained by data size alone (since the scaling experiment shows only +1.3pp at 1K from the full distribution). This suggests the pilot-to-full discrepancy is distribution-driven, not scale-driven, which the paper does not adequately discuss.

**(b) Suspicious temperature ablation results.** Table 11 shows random is best at *all* temperatures. If the motivation for hard negative mining is that it provides harder negatives which help at low temperature (where difficulty matters more), then random dominating at tau=0.05 directly contradicts the mechanistic story. The paper should address this more directly.

**(c) SWE-bench results are essentially null.** Table 3 shows resolve rates of 18.7%, 19.0%, 18.3% for random/embed/dataflow. McNemar p=0.89. Table 4 bootstrap CI [-3.8, +4.5] for embed vs random. These are unambiguously null. Yet the paper keeps the SWE-bench comparison, which adds length without adding evidence.

**(d) Comparison with inference-time methods is unflattering.** Table 6 shows LocAgent at 26.2% resolve rate vs the paper's best at ~19%. This 7pp gap is far larger than any within-strategy difference. The paper positions this as "different paradigm" but a reader will note that the proposed approach simply underperforms existing methods.

**(e) Failure analysis backfires.** Table 10: dataflow could help in 6/50 cases, actually helped in 2, and *hurt* in 3. A method that hurts more often than it helps in its target use case is a red flag, not a neutral finding. The paper should frame this more honestly.

---

### 4. Weaknesses and Issues

**Major Issues**

1. **Confounded pilot-to-full comparison (MAJOR).** The paper's central narrative -- small-scale signal vanishes at scale -- is confounded by simultaneous distribution shift. The pilot's 8 repos are substantially different from the full 123 repos (Table 9). Without a controlled experiment holding distribution constant while varying scale (or vice versa), the paper cannot distinguish "scale kills signal" from "distribution kills signal." This is the paper's most important claim and it rests on a confounded comparison.

2. **No mechanistic explanation for the null result (MAJOR).** The paper diagnoses *that* the signal vanishes but not *why*. The representation saturation analysis (Qwen pos_sim=0.9855) is presented as a pre-existing condition of the encoder, not something that changes with scale. If saturation explains when dataflow helps, and Qwen is saturated at both pilot and full scale, why does dataflow help in pilot but not full? The paper lacks a convincing mechanistic account.

3. **Missing neg_difficulty quartile analysis (MAJOR for experiment plan compliance).** The experiment plan explicitly calls for neg_difficulty quartile analysis and scatter plot. This analysis would directly address whether negative difficulty distributions shift between pilot and full-scale data, providing the missing mechanistic link. Its absence is a significant gap.

4. **Scaling "law" is overfit (MODERATE).** Four data points do not constitute a law. The paper should call this a "trend" or "observation" and acknowledge the extreme sparsity of the fit.

**Minor Issues**

5. **Dataflow-distance weighting results not tabulated (MINOR).** Mentioned in section 6.5 without a table. For completeness, these should be reported.

6. **No qualitative examples (MINOR).** Plan item 11 is entirely absent. Even for a negative result paper, showing *why* specific methods fail at scale through concrete examples would strengthen the analysis.

7. **Encoder diversity is limited (MINOR).** Both encoders are 3B parameters. The saturation argument (pos_sim threshold) would be more convincing with a wider range of model sizes.

8. **Python-only evaluation (MINOR).** CodeQL extraction and all experiments are Python-only. This limits generalizability claims.

9. **The title is somewhat misleading (MINOR).** "Fragility" implies the methods are inherently unreliable. The data more precisely shows that pilot-to-full replication is confounded by distribution shift. "Scale" is only one of multiple changing variables.

10. **LocAgent comparison lacks context (MINOR).** Table 6 compares against LocAgent (26.2% resolve) but does not discuss the computational cost difference. If the paper's approach is much cheaper at inference, the lower resolve rate might be acceptable, but this is not discussed.

---

### 5. Scoring

**Overall Score: 4 (Weak Accept)**

**Rationale:**

The paper addresses a genuinely important question -- whether hard negative mining signals observed at small scale replicate at larger scale -- and provides a well-powered negative answer (54 full-scale runs). The experimental effort is substantial and above average for the field. The negative result itself is valuable for the community: it warns practitioners against over-interpreting pilot results and documents the variance structure of contrastive code retrieval training.

However, the paper falls short of a clear accept due to: (1) the central pilot-to-full comparison is confounded by distribution shift, weakening the "scale kills signal" narrative; (2) the mechanistic analysis is incomplete -- the paper shows *what* happens but not *why*; (3) several planned experiments are missing or incomplete; and (4) some results (failure analysis, temperature ablation) actually undermine the paper's framing rather than supporting it.

The paper would benefit from: (a) a controlled scale experiment holding distribution constant; (b) neg_difficulty analysis comparing pilot vs full-scale distributions; (c) more honest framing of the failure analysis results; and (d) downgrading the "scaling law" language.

As a negative result / empirical analysis paper, it meets the bar for a venue like EMNLP where such contributions are valued, but it needs revision to address the confounded comparison and incomplete mechanistic story.

**Confidence: 4/5**

I am confident in this assessment. I have reviewed the experimental design, statistical methods, and all reported tables in detail. The confound between scale and distribution shift is a clear methodological gap. My uncertainty is mainly about whether the missing experiments (neg_difficulty quartiles, qualitative examples) would, if present, resolve the mechanistic gap -- if so, the paper could move to a solid 5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ed800d6-533c-4184-b98a-46f5cfc82bc6",
  "isSidechain": true,
  "agentId": "a3675f4a8d53881c9",
  "requestId": "req_011Cb2ABiadU4yDwoaiwQTCQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49cfd5eb-1e45-4590-ba3b-b85b5d5c37d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3zszvtBrNH52ySQNvxeam",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26566,
      "cache_read_input_tokens": 50806,
      "output_tokens": 3321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 26566
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3321,
          "cache_read_input_tokens": 50806,
          "cache_creation_input_tokens": 26566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 26566,
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
