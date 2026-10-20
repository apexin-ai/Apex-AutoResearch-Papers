# Research conversation: 你是 Reviewer 2 (R2)，负责审稿的**新颖性与相关工作**维度。请对以下论文进行独立审稿，按 top ML venue 标准（接受率 ~25%，6分制：1=Strong Reject, 2=Reject, 3=Weak Rej

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9b7a4a9753d85f28.jsonl`
- **Structured JSON:** [`488a436960196db2547b.json`](../../sessions/48/488a436960196db2547b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-14T08:38:17.952Z_

你是 Reviewer 2 (R2)，负责审稿的**新颖性与相关工作**维度。请对以下论文进行独立审稿，按 top ML venue 标准（接受率 ~25%，6分制：1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept）。

## 论文信息

**标题**: "A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval"

**摘要**: 系统比较了三种 negative sampling 策略（random, embedding-distance, dataflow-aware）用于训练 contrastive code retriever，使用两个编码器（Qwen2.5-Coder-3B, StarCoder2-3B），54 个 full-scale 训练 runs（9 seeds × 3 strategies × 2 encoders）。Pilot (2K instances, 单 seed) 显示 embedding mining +1.6-2.0pp R@1。但 full-scale (15K instances, 9 seeds) 策略差异 <1pp，被种子方差 (std≈3pp) 淹没，bootstrap p≥0.68。发现 data-size-benefit scaling law: -0.11pp/1K instances。

**论文结构（10页）**:
1. Introduction - 提出3个研究问题，总结 pilot 结果未复现
2. Related Work - 3段：Hard negative mining (ANCE, CoCoHaNeRe), Code retrieval (SweRank, SWE-Fixer, GraphCodeBERT, RepoFusion), Structure-guided code understanding (LocAgent, CodexGraph, ARISE)
3. Method - Task setup (bi-encoder + InfoNCE + LoRA), 3 strategies, CodeQL pipeline
4. Experiments - Full-scale multi-seed results, SWE-bench Lite, RepoBench-R, Inference-time comparison
5. Analysis - Data size scaling law, Stratified analysis, Data pipeline audit, Failure taxonomy
6. Ablations - Temperature, Hop-distance, Fusion head, Dynamic mining, Distance weighting
7. Discussion - Why pilot misleads, Training vs inference structural info, Practitioner implications, Limitations
8. Conclusion

**贡献声明**:
1. Pilot-scale unreliability 的实证证据 + scaling law (-0.11pp/1K)
2. 全面消融排除混杂因素
3. 开源 CodeQL pipeline

**相关工作覆盖**:
- ANCE (Xiong et al., 2021) - periodically refreshed hard negatives
- CoCoHaNeRe (Gao et al., 2024) - 但指出其 conflated BM25-proxy with embedding negatives
- SweRank (Li et al., 2023) - contrastive code retrieval
- SWE-Fixer (Yang et al., 2024)
- GraphCodeBERT (Guo et al., 2021) - data flow as pre-training signal
- RepoFusion (Shrivastava et al., 2023)
- LocAgent (Qin et al., 2024) - inference-time graph
- CodexGraph (Liu et al., 2024) - inference-time graph
- ARISE (Wu et al., 2024) - intra-procedural data flow

**实验设计参考（完整计划中的实验列表）**:
论文覆盖了计划中大部分实验，但以下内容缺失或不完整：
- Qualitative Examples (计划中有但论文未包含)
- Neg difficulty quartile analysis (计划中有但论文仅简要提及)
- Dataflow distance weighting 仅一句话总结，无表格

**方法细节**:
- 训练数据: SWE-smith instances, pilot ~2K from 8 repos, full 15,133 from 123 repos
- Encoders: Qwen2.5-Coder-3B (representation saturation), StarCoder2-3B (healthy space)
- Negative strategies: random, embedding-distance (top-k nearest), dataflow-aware (CodeQL 2-hop disconnected + high embed sim)
- Evaluation: SWE-smith val R@1, SWE-bench Lite resolve rate, RepoBench-R

## 审稿要求

请从以下维度评审，输出结构化报告：

### 1. 新颖性评价
- 核心贡献的新颖程度？
- Negative result paper 的价值评估？
- 是否有真正的方法论创新？
- Scaling law (-0.11pp/1K) 的重要性？

### 2. 相关工作评价
- 相关工作覆盖是否全面？
- 是否遗漏重要基线或对比方法？
- 与现有工作的区别/定位是否清晰？
- 引用数量是否充足？（论文仅9篇引用）

### 3. 写作与呈现
- 论文 framing 是否恰当？（negative result paper 的 framing）
- 叙事结构是否清晰？
- 表格/图表是否充分？（注意：论文10页中14个表但无图）

### 4. 对社区的影响
- 这篇论文对代码检索/对比学习社区的价值？
- 实践指导意义？
- 开源 CodeQL pipeline 的价值？

### 5. 弱点与问题
- 列出所有发现的问题（major 和 minor）

### 6. 评分
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
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "59b71f7f-3209-4173-ab67-104ead4cd726",
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

_source line 2 · 2026-05-14T08:38:17.956Z_

```json
{
  "parentUuid": "59b71f7f-3209-4173-ab67-104ead4cd726",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
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
  "uuid": "4378a7d6-e89f-4c4c-bd0d-4152bacc4b81",
  "timestamp": "2026-05-14T08:38:17.956Z",
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

_source line 3 · 2026-05-14T08:38:22.691Z_



I'll start by reading the actual paper and any related project files to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4378a7d6-e89f-4c4c-bd0d-4152bacc4b81",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AAJchTtStCYLwWN2aR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54fcb119-ae73-4b29-94fc-bc94cadbe058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FH7TtNRvtArgPA9HUopDHt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7358,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7358,
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

_source line 4 · 2026-05-14T08:38:23.905Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GBa8nTVyG1JLscZ6bZpEnt`</summary>

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
  "parentUuid": "54fcb119-ae73-4b29-94fc-bc94cadbe058",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AAJchTtStCYLwWN2aR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7a93e17-6faa-4f6c-a5fe-98fb8e7e275b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FH7TtNRvtArgPA9HUopDHt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7358,
      "cache_read_input_tokens": 8249,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7358
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7358,
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

_source line 5 · 2026-05-14T08:38:23.913Z_

<details><summary>↩ Tool result · `toolu_01GBa8nTVyG1JLscZ6bZpEnt`</summary>

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
  "parentUuid": "a7a93e17-6faa-4f6c-a5fe-98fb8e7e275b",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "24e734e5-dfc3-462d-8cab-480a1cff4ac6",
  "sourceToolAssistantUUID": "a7a93e17-6faa-4f6c-a5fe-98fb8e7e275b",
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

_source line 6 · 2026-05-14T08:38:26.590Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01JnGfsWnjUqPAkYpAnYvBJL`</summary>

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
  "parentUuid": "24e734e5-dfc3-462d-8cab-480a1cff4ac6",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AAkFZLyedVq6GX6CV5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b30c080-6b3f-4bf0-ab49-7bd8fa91cbfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYfhnqrwUmzYzfXh12dNbA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15607,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 7 · 2026-05-14T08:38:26.720Z_

<details><summary>↩ Tool result · `toolu_01JnGfsWnjUqPAkYpAnYvBJL`</summary>

```text
{"result":"# 项目 structfuse-context 概况\n\n## 实验状态 (31 个)\n\n- **p2b_eval_4runs_pool50**: DONE (success) — \n- **d007_50repo_overlap**: DONE (success) — \n- **p2b_5reruns**: DONE (success) — \n- **p2b_eval_4runs_v2**: DONE (success) — \n- **p2b-all-9runs**: DONE (killed) — \n- **p2b-smoke8**: DONE (killed) — \n- **p2b-smoke7**: DONE (killed) — \n- **p2b-smoke6**: DONE (killed) — \n- **p2b-smoke5**: DONE (killed) — \n- **p2b-smoke4**: DONE (killed) — \n- **p2b-smoke3**: DONE (killed) — \n- **p2b-smoke2**: DONE (killed) — \n- **p2b-smoke-test**: DONE (killed) — \n- **mvp_p2a_linear_proxy**: DONE (success) — \n- **mvp_p1_codeql_feasibility**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\n- **m1_extraction** (success): —\n\n## 趋势\n成功 10 / 负向 2 / 失败 2 / 共 28\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-42106: 无 GPU 信息\n\n## 告警\n- p2b-smoke-test: 已被终止 — unknown\n- p2b-smoke2: 已被终止 — unknown\n- p2b-smoke3: 已被终止 — unknown\n- p2b-smoke4: 已被终止 — unknown\n- p2b-smoke5: 已被终止 — unknown\n- p2b-smoke6: 已被终止 — unknown\n- p2b-smoke7: 已被终止 — unknown\n- p2b-smoke8: 已被终止 — unknown\n- p2b-all-9runs: 已被终止 — unknown\n- mvp_p2b_contrastive_training: 已被终止 — unknown\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\n- p2b_eval_all: 已被终止 — unknown\n- m2_early_pilot: 已被终止 — unknown\n- m2_early_pilot_v2: 训练失败 — unknown\n- m2_early_pilot_v3: 已被终止 — unknown\n- m1_reextract: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b30c080-6b3f-4bf0-ab49-7bd8fa91cbfd",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "51ab2cb4-144c-4b87-913b-e99bab08e063",
  "sourceToolAssistantUUID": "4b30c080-6b3f-4bf0-ab49-7bd8fa91cbfd",
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

_source line 8 · 2026-05-14T08:38:27.216Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015rSpxDjnARsVTS63m64p7Z`</summary>

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
  "parentUuid": "51ab2cb4-144c-4b87-913b-e99bab08e063",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AAkFZLyedVq6GX6CV5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43e69c96-1d91-4e5d-b175-6e3258377e85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NYfhnqrwUmzYzfXh12dNbA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15607,
      "output_tokens": 160,
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
          "output_tokens": 160,
          "cache_read_input_tokens": 15607,
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

_source line 9 · 2026-05-14T08:38:27.226Z_

<details><summary>↩ Tool result · `toolu_015rSpxDjnARsVTS63m64p7Z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n- **m1_extraction** (success): —\\n\\n## 趋势\\n成功 10 / 负向 2 / 失败 2 / 共 28\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 1895, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43e69c96-1d91-4e5d-b175-6e3258377e85",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "97c23863-675a-4b67-b15e-52158e2897bd",
  "sourceToolAssistantUUID": "43e69c96-1d91-4e5d-b175-6e3258377e85",
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

_source line 10 · 2026-05-14T08:38:32.041Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HAuNj9foVLP1BZ1Eehkv8b`</summary>

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
  "parentUuid": "97c23863-675a-4b67-b15e-52158e2897bd",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AAzPMxrtUXvTytmcMK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2efd7242-5a18-448e-8846-f8320a03370f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLMkEiygxcioQVKnxNVwUi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 17056,
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

_source line 11 · 2026-05-14T08:38:32.054Z_

<details><summary>↩ Tool result · `toolu_01HAuNj9foVLP1BZ1Eehkv8b`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-12\\n# 说明: 只收录项目文件中已引用的 + 确定存在的知名论文。不确定的信息标注\\\"需验证\\\"。\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline  # StructFuse 的评估基准\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Karthik Narasimhan, Ofir Press\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: building-block  # StructFuse 用其 repo 做数据提取\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n        note: \\\"需验证 venue（可能已投稿会议）\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务，StructFuse 可用于评估。\\\"\\n        note: \\\"需验证年份和 venue\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及代码领域的对比学习\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式，是 StructFuse 对比训练的方法论基础。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，是 StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"SimCLR: A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Mining Hard Negatives with Curriculum for Dense Retrieval\\\"\\n        authors: \\\"需验证\\\"\\n        venue: \\\"需验证\\\"\\n        year: \\\"需验证\\\"\\n        relation: background\\n        summary: \\\"课程学习式 hard negative 挖掘，从易到难训练检索器。\\\"\\n        note: \\\"需验证完整信息\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block  # StructFuse 核心组件\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: EMNLP (Findings)\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: background\\n        summary: \\\"大规模开源代码 LLM，广泛用于代码嵌入的 backbone。\\\"\\n        note: \\\"需验证 venue（可能是 arXiv 或其他）\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Qwen Team (Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block  # StructFuse 用 Qwen2.5-Coder-3B 做检索器\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n        note: \\\"需验证确切标题和年份\\\"\\n\\n      - title: \\\"Contrastive Learning for Source Code with Structural and Functional Properties\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: ACL (Findings)\\n        year: 2022\\n        relation: background\\n        summary: \\\"代码对比学习中利用结构/功能属性构建正负样本对。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。Phase 2a 实验发现 BM25 在 bug fixing 定位中可能有误导性（负系数）。\\\"\\n\\n# ==========================================================================\\n# 待补充\\n# ==========================================================================\\n# 以下论文可能相关，待确认后补充：\\n# - FAISS (Johnson et al., 2019) — ANN 检索库，StructFuse 评估可能用到\\n# - Tree-sitter — 增量解析器，与 CodeQL 互补\\n# - Aider / Moatless Tools — SWE-bench 上的其他代码检索方法\\n# - CoSQA (Huang et al., 2021) — 代码搜索 QA 数据集\\n# - DeepSeek-Coder — 另一个可能的 backbone 对比\\n\", \"total_chars\": 9647, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2efd7242-5a18-448e-8846-f8320a03370f",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "3a043997-3fb1-4c6b-89ea-10987b450176",
  "sourceToolAssistantUUID": "2efd7242-5a18-448e-8846-f8320a03370f",
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

_source line 12 · 2026-05-14T08:38:32.532Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FVKHyukjA6ZS57UP1awvv5`</summary>

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
  "parentUuid": "3a043997-3fb1-4c6b-89ea-10987b450176",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AAzPMxrtUXvTytmcMK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c627cc92-1ad3-489d-a6d1-52277fc37cf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLMkEiygxcioQVKnxNVwUi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 17056,
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

_source line 13 · 2026-05-14T08:38:32.541Z_

<details><summary>↩ Tool result · `toolu_01FVKHyukjA6ZS57UP1awvv5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \\\"harm\\\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\\n\\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\\n\\n- **Headline result template**: \\\"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\\\"\\n- Backup: \\\"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\\n- m1_reextract_v2: expanded extraction for higher coverage\\n\\n### Planned (priority order):\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark\\n- plan_015: Dynamic mining baseline\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 9391, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c627cc92-1ad3-489d-a6d1-52277fc37cf7",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "227f2560-a0dd-4bb1-9629-d94caa612414",
  "sourceToolAssistantUUID": "c627cc92-1ad3-489d-a6d1-52277fc37cf7",
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

_source line 14 · 2026-05-14T08:38:33.482Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JwVRJoiY4twS5ZvbpY2qxY`</summary>

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
  "parentUuid": "227f2560-a0dd-4bb1-9629-d94caa612414",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AAzPMxrtUXvTytmcMK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58210bb5-bea7-4757-b331-9953a2f3b9b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLMkEiygxcioQVKnxNVwUi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 17056,
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

_source line 15 · 2026-05-14T08:38:33.494Z_

<details><summary>↩ Tool result · `toolu_01JwVRJoiY4twS5ZvbpY2qxY`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58210bb5-bea7-4757-b331-9953a2f3b9b9",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "39834cc6-c3b3-49a5-b29c-9e51a86d0f86",
  "sourceToolAssistantUUID": "58210bb5-bea7-4757-b331-9953a2f3b9b9",
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

_source line 16 · 2026-05-14T08:38:33.839Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NKHMGQ6vLxDxcrnnAbBVJD`</summary>

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
  "parentUuid": "39834cc6-c3b3-49a5-b29c-9e51a86d0f86",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AAzPMxrtUXvTytmcMK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b3e751b-20d1-466d-a8da-a140cb511c7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLMkEiygxcioQVKnxNVwUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 17056,
      "output_tokens": 380,
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
          "output_tokens": 380,
          "cache_read_input_tokens": 17056,
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

_source line 17 · 2026-05-14T08:38:33.850Z_

<details><summary>↩ Tool result · `toolu_01NKHMGQ6vLxDxcrnnAbBVJD`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b3e751b-20d1-466d-a8da-a140cb511c7d",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "40758337-3c75-41da-8fbb-b64a598fe6bc",
  "sourceToolAssistantUUID": "8b3e751b-20d1-466d-a8da-a140cb511c7d",
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

_source line 18 · 2026-05-14T08:38:38.319Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Cq8m1G3vQ1MDa15trWE9b8`</summary>

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
  "parentUuid": "40758337-3c75-41da-8fbb-b64a598fe6bc",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ABUhT1scqgmEGbAqXj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bdb803a-37ca-4f7e-a0eb-056f956dc81c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FW6YiTvc5RVydhkEb6dhRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7547,
      "cache_read_input_tokens": 19767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7547,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 19 · 2026-05-14T08:38:38.328Z_

<details><summary>↩ Tool result · `toolu_01Cq8m1G3vQ1MDa15trWE9b8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); heavy inference cost |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | Repository-level Graph for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2025) | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (2025) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献\\n\\n- CodexGraph: arXiv:2408.03910, NAACL 2025\\n- LocAgent: arXiv:2503.09089, ACL 2025\\n- RANGER: arXiv:2509.25257, 2025\\n- RepoGraph: arXiv:2410.14684, ICLR 2025\\n- GraphCoder: arXiv:2406.07003, ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, 2025\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\", \"total_chars\": 8062, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bdb803a-37ca-4f7e-a0eb-056f956dc81c",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "0820d98e-1af8-4667-b7f4-db480142e475",
  "sourceToolAssistantUUID": "4bdb803a-37ca-4f7e-a0eb-056f956dc81c",
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

_source line 20 · 2026-05-14T08:38:38.613Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0194E6WGhjCCYFMVfxzPiyqk`</summary>

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
  "parentUuid": "0820d98e-1af8-4667-b7f4-db480142e475",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ABUhT1scqgmEGbAqXj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f20d0f01-e366-4f7c-9c8d-2f5b612a6464",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FW6YiTvc5RVydhkEb6dhRR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7547,
      "cache_read_input_tokens": 19767,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7547
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 19767,
          "cache_creation_input_tokens": 7547,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7547,
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

_source line 21 · 2026-05-14T08:38:38.623Z_

<details><summary>↩ Tool result · `toolu_0194E6WGhjCCYFMVfxzPiyqk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 28\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n\", \"total_chars\": 20054, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f20d0f01-e366-4f7c-9c8d-2f5b612a6464",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "82b11353-f61d-4d8c-92c9-43caa5b1bc60",
  "sourceToolAssistantUUID": "f20d0f01-e366-4f7c-9c8d-2f5b612a6464",
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

_source line 22 · 2026-05-14T08:38:41.909Z_

Now let me look at the actual paper artifacts and any draft text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82b11353-f61d-4d8c-92c9-43caa5b1bc60",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ABq7HREVnySdqJ1pVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21b61858-b769-455c-afde-8216def7740c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MG9fvkbCEfXUF8HqzP2JeQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 27314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13538,
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

_source line 23 · 2026-05-14T08:38:43.860Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01A97CD1uQgEg3YUkzp9JNyw`</summary>

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
  "parentUuid": "21b61858-b769-455c-afde-8216def7740c",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ABq7HREVnySdqJ1pVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88f4d931-08a1-46e6-8d41-3c3e16c07c42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MG9fvkbCEfXUF8HqzP2JeQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 27314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13538,
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

_source line 24 · 2026-05-14T08:38:43.881Z_

<details><summary>↩ Tool result · `toolu_01A97CD1uQgEg3YUkzp9JNyw`</summary>

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
  "parentUuid": "88f4d931-08a1-46e6-8d41-3c3e16c07c42",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "142c2585-a7dd-427f-9369-7906ed56d157",
  "sourceToolAssistantUUID": "88f4d931-08a1-46e6-8d41-3c3e16c07c42",
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

_source line 25 · 2026-05-14T08:38:44.867Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014NWug9MfuxZhSygBctMcer`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "142c2585-a7dd-427f-9369-7906ed56d157",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ABq7HREVnySdqJ1pVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf834607-537d-4317-8de7-cbdfa71bff80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MG9fvkbCEfXUF8HqzP2JeQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 27314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13538,
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

_source line 26 · 2026-05-14T08:38:44.883Z_

<details><summary>↩ Tool result · `toolu_014NWug9MfuxZhSygBctMcer`</summary>

```text
artifacts/dream_reports/dream_20260512T204322/best/paper.pdf
artifacts/dream_reports/dream_20260512T204322/median/paper.pdf
artifacts/dream_reports/dream_20260512T204322/worst/paper.pdf
artifacts/dream_reports/dream_20260514T075732/best/paper.pdf
artifacts/dream_reports/dream_20260514T075732/median/paper.pdf
artifacts/dream_reports/dream_20260514T075732/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf834607-537d-4317-8de7-cbdfa71bff80",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "77cc9dbb-b9a1-4f93-9249-f4fb3a027cc5",
  "sourceToolAssistantUUID": "bf834607-537d-4317-8de7-cbdfa71bff80",
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

_source line 27 · 2026-05-14T08:38:45.081Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018WF9QxVaRKqjzmxR17VkG1`</summary>

```json
{
  "pattern": "artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77cc9dbb-b9a1-4f93-9249-f4fb3a027cc5",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ABq7HREVnySdqJ1pVU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3688db10-eb0c-4725-b632-3bdea3d617b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MG9fvkbCEfXUF8HqzP2JeQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 27314,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13538
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 27314,
          "cache_creation_input_tokens": 13538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13538,
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

_source line 28 · 2026-05-14T08:38:45.092Z_

<details><summary>↩ Tool result · `toolu_018WF9QxVaRKqjzmxR17VkG1`</summary>

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
  "parentUuid": "3688db10-eb0c-4725-b632-3bdea3d617b6",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "62529d61-2a5e-4564-8937-c48c19053bd7",
  "sourceToolAssistantUUID": "3688db10-eb0c-4725-b632-3bdea3d617b6",
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

_source line 29 · 2026-05-14T08:38:49.129Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CSJvnLwSkbWNzLs6VvosnG`</summary>

```json
{
  "pattern": "artifacts/dream_reports/dream_20260514T075732/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62529d61-2a5e-4564-8937-c48c19053bd7",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ACJkwFkYpU8h3pwJBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e29da532-5418-49ef-a5d6-154a0d0c8727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4W7dCfY7st4DP1Rf6kvZY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2423,
      "cache_read_input_tokens": 40852,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2423
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 40852,
          "cache_creation_input_tokens": 2423,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2423,
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

_source line 30 · 2026-05-14T08:38:49.159Z_

<details><summary>↩ Tool result · `toolu_01CSJvnLwSkbWNzLs6VvosnG`</summary>

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
artifacts/dream_reports/dream_20260514T075732/median/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/best/review_report.md
artifacts/dream_reports/dream_20260514T075732/median/review_report.md
artifacts/dream_reports/dream_20260514T075732/logs/review_median.log
artifacts/dream_reports/dream_20260514T075732/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e29da532-5418-49ef-a5d6-154a0d0c8727",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "bb237f46-33a8-48df-a88a-76a78f6c0b50",
  "sourceToolAssistantUUID": "e29da532-5418-49ef-a5d6-154a0d0c8727",
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

_source line 31 · 2026-05-14T08:38:52.790Z_

Let me read the latest dream paper (the median scenario, which best represents the paper as described in the prompt) and the review reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb237f46-33a8-48df-a88a-76a78f6c0b50",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ACdFg8zYseHmAQKHGP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3142b7c-fdad-4a71-893f-7cbffcb8f08d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25nW21KpSAewjwYqrh218",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 43275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1035,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 32 · 2026-05-14T08:38:54.022Z_

<details open><summary>🔧 Tool call — Read · `toolu_011gFN7ZbWchkA82p6yq4bRA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3142b7c-fdad-4a71-893f-7cbffcb8f08d",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ACdFg8zYseHmAQKHGP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc5cbef4-449a-4338-8777-4ddef17b9d29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25nW21KpSAewjwYqrh218",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 43275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1035,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 33 · 2026-05-14T08:38:54.146Z_

<details open><summary>🔧 Tool call — Read · `toolu_0195KSC5yRB7LKQrgN29zVnd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc5cbef4-449a-4338-8777-4ddef17b9d29",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ACdFg8zYseHmAQKHGP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69df3585-0ab9-4631-a63c-71f766729109",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25nW21KpSAewjwYqrh218",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 43275,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1035
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 43275,
          "cache_creation_input_tokens": 1035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1035,
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

_source line 34 · 2026-05-14T08:38:54.153Z_

<details><summary>↩ Tool result · `toolu_0195KSC5yRB7LKQrgN29zVnd`</summary>

```text
1	---
2	dream_id: dream_20260514T075732
3	tier: median
4	overall_score: weak reject
5	timestamp: 2026-05-14T08:36:30.193110+00:00
6	---
7	
8	# Dream Review Report: "What Makes Hard Negatives Work for Code Retrieval?"
9	
10	**Dream ID:** 20260514T075732 | **Review Mode:** full | **Date:** 2026-05-14
11	
12	---
13	
14	## Paper Summary
15	
16	This paper presents a controlled comparison of three hard negative mining strategies for contrastive code retrieval—random, embedding-distance, and dataflow-aware (via CodeQL inter-procedural analysis)—across two code encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct representation geometries. The main findings are: (1) embedding-distance mining provides directional improvement over random (+0.5–1.3pp R@1 on RepoBench-R), (2) dataflow-grounded negatives yield inconsistent effects across encoders, and (3) no strategy achieves significant downstream gains on SWE-bench Lite (all p > 0.3). The paper positions itself as an EMNLP analysis paper with methodology contributions: a controlled comparison framework, representation geometry analysis, and a CodeQL extraction pipeline.
17	
18	---
19	
20	## Reviewer Panel
21	
22	| Reviewer | Focus | Score | Confidence |
23	|----------|-------|-------|------------|
24	| R1 | Methods + Experiments | 4/6 (Weak Accept) | 4/5 |
25	| R2 | Novelty + Related Work | 3/6 (Weak Reject) | 4/5 |
26	
27	---
28	
29	## R1 Review: Methods and Experiments
30	
31	### Strengths
32	
33	- **Rigorous experimental protocol.** ~54 training runs with paired bootstrap CIs on SWE-bench is commendable. The controlled comparison genuinely isolates the negative selection variable while holding all other training details constant.
34	- **Comprehensive ablation suite.** Each ablation answers a specific question: temperature sensitivity (Tables 7–8), hop depth (Table 9), data scaling (Table 10), fusion head (Table 11), weighted vs. binary dataflow (Table 12), static vs. dynamic mining (Table 13). The ablation coverage is thorough for this subfield.
35	- **Honest reporting of null and conditional results.** The paper openly reports that SWE-bench shows no significant differences, that dataflow negatives are inconsistent, and that effect sizes diminish with data scale. This is appropriate for an analysis paper.
36	- **Failure analysis (§4.3) provides genuine insight.** The decomposition showing 44% generation failures vs. 36% retrieval misses cleanly explains the downstream null result and provides useful signal for the community.
37	- **Temperature robustness.** The finding that embedding > random direction is consistent across all τ values (Tables 7–8) strengthens the directional claim beyond a single hyperparameter setting.
38	
39	### Weaknesses
40	
41	1. **N=2 encoders fundamentally limits the representation geometry claim.** The paper's central analytical contribution—linking encoder-strategy interaction to representation saturation—rests on exactly two data points. The pos_sim values (0.9855 vs. 0.7985) are an observation, not a validated mechanism. Any two encoders will differ in some metric; without testing whether pos_sim is predictive across 4–5 additional encoders, the "representation geometry" framing overpromises.
42	
43	2. **Missing BM25 negative baseline—the single most important omitted experiment.** The paper's narrative begins with correcting CoCoHaNeRe's conflation of BM25 and embedding-distance negatives. Yet the paper never runs BM25 negatives in its own framework. This experiment would (a) verify that BM25 negatives indeed harm performance, (b) quantify the gap between BM25-proxy and true embedding-distance mining, and (c) close the paper's own argument loop. Without it, the correction claim is asserted but unverified.
44	
45	3. **No error bars or confidence intervals on RepoBench-R results (Table 1).** The main retrieval results lack any statistical significance testing—no seeds, no CIs, no p-values. For an analysis paper emphasizing statistical rigor (bootstrap CIs on SWE-bench), this inconsistency is glaring. The +0.5pp StarCoder improvement could easily be within noise.
46	
47	4. **Pool size of 50 candidates per query is unrealistically small.** Real repositories have hundreds to thousands of files. A pool of 50 inflates absolute R@1 values and may not preserve strategy ranking at realistic pool sizes. No sensitivity analysis on pool size is provided.
48	
49	5. **StarCoder2-3B is mischaracterized as "encoder-decoder" (§3.5).** StarCoder2-3B is a decoder-only model, same architectural class as Qwen2.5-Coder-3B. The actual difference is in pretraining data/procedure, not architecture. This factual error undermines the "architecturally distinct" framing.
50	
51	6. **Table 6 repo-complexity analysis has N=1 in the smallest tier.** The "<50 instances" tier contains a single repository, making the +2.1pp data point anecdotal. This tier should be excluded or merged, and the correlation analysis (r=−0.41, p=0.08) should be recomputed without it.
52	
53	7. **SWE-smith validation results are referenced but never shown.** The paper mentions "consistent with SWE-smith validation results" (§4.1) but the SWE-smith validation table is absent. These are presumably the primary evaluation results—their omission is surprising.
54	
55	8. **34% structural data coverage is underreported as a limitation.** Only 34% of training instances actually receive dataflow-mined negatives; the rest fall back to alternative selection. The reported effects average over both populations, diluting the true signal. A stratified analysis (structured vs. fallback instances) is needed.
56	
57	9. **Checkpoint selection criterion is unspecified.** With documented overfitting after step 1000, the choice of "best checkpoint" could reverse strategy rankings. The criterion (validation metric, early stopping patience) should be explicitly stated.
58	
59	### Questions for Authors
60	
61	1. What is the per-instance effect of dataflow negatives stratified by whether structural data was available (34%) vs. not?
62	2. Why were SWE-smith validation results omitted from the paper despite being referenced?
63	3. Have you tested sensitivity to pool size (e.g., pool=100, 200, 500)?
64	4. What is the checkpoint selection criterion, and how sensitive are strategy rankings to this choice?
65	5. Can you run a BM25 negative baseline to close the CoCoHaNeRe correction argument?
66	
67	---
68	
69	## R2 Review: Novelty and Related Work
70	
71	### Strengths
72	
73	- **CoCoHaNeRe correction has community value.** If BM25-proxy negatives were indeed mislabeled as embedding-distance, clarifying this matters for practitioners and could redirect research effort.
74	- **Honest reporting of null results.** The paper does not hide that dataflow negatives are inconsistent, SWE-bench shows no significant differences, and CIs include zero for StarCoder. This candor is increasingly valuable in ML research.
75	- **Potentially actionable pos_sim diagnostic.** If validated on more encoders, the observation that pos_sim correlates with mining strategy effectiveness could become a cheap pre-training diagnostic for practitioners.
76	- **Clean separation of training-time vs. inference-time value.** The fusion head ablation (Table 11) demonstrates that structural information's value is in negative selection, not inference-time scoring—a crisp methodological insight.
77	- **"Directional evidence" framing is appropriately calibrated** for the evidence strength. The paper does not overclaim given the data.
78	
79	### Weaknesses
80	
81	1. **"First controlled comparison" novelty claim is overstated.** The paper claims to be the "first controlled comparison using true embedding-distance negatives for code retrieval." ANCE-style mining (using actual embedding distance) has existed since 2021 and has been applied broadly. The claim that nobody has done this for code requires more thorough documentation than critiquing a single paper.
82	
83	2. **CoCoHaNeRe critique is the paper's central motivation but remains unverified.** The entire narrative depends on CoCoHaNeRe using BM25-proxy negatives mislabeled as embedding-distance. Yet the paper never: (a) provides specific textual evidence from CoCoHaNeRe showing the mislabeling, (b) reproduces the CoCoHaNeRe setup with BM25 negatives, or (c) runs BM25 negatives in its own framework. Without a BM25 baseline experiment, the "correcting a misconception" claim is speculative.
84	
85	3. **Representation geometry analysis is shallow despite impressive terminology.** The substance is: one encoder has pos_sim=0.99 and the other has pos_sim=0.80, and they respond differently. With n=2, this is anecdotal. The paper does not connect to existing contrastive learning theory on negative difficulty (Robinson et al. 2021, Kalantidis et al. 2020) or provide any formal relationship between pos_sim and expected mining benefit.
86	
87	4. **Significant related work gaps for a "systematic study":**
88	   - Hard negative theory: Robinson et al. 2021, Kalantidis et al. 2020
89	   - Contrastive learning foundations: SimCLR, MoCo
90	   - Code representation baselines: CodeBERT, UniXcoder, CodeT5+
91	   - Structural code methods: CodeGRAG, GraphCoder, RepoGraph
92	   - Curriculum-based mining: mentioned but never cited or compared
93	
94	5. **CodeQL pipeline is an engineering artifact, not a research contribution.** "123 repos processed with zero timeouts" is a reliability metric for a tool. The 34% instance-level coverage is the scientifically relevant number, and it is a significant limitation that makes Contribution (3) underwhelming.
95	
96	6. **Dataflow method is introduced and shown not to work, but still framed as a contribution.** The dataflow strategy is +0.6pp on Qwen RepoBench-R but −0.6pp on StarCoder, and −0.3pp on SWE-bench Lite. The "conditional benefit mediated by representation saturation" framing repackages a negative result. The honest conclusion is that dataflow negatives failed to demonstrate consistent value.
97	
98	7. **Effect sizes are too small for practical relevance.** +0.5–1.3pp R@1 with CIs including zero on half the setups. Table 14 is self-damaging: StructFuse gets +0.5–1.5pp while CodexGraph gets +5.2pp. The cost-benefit of a CodeQL extraction pipeline for +0.5pp is hard to justify.
99	
100	8. **No comparison with other training-time hard negative mining approaches.** The paper compares random, static embedding, and dataflow but omits ANCE-style dynamic mining as a proper baseline, in-batch negatives (DPR-style), and curriculum-based approaches. For a paper titled "systematic study," the strategy space is narrow.
101	
102	9. **Broken bibliography.** All references appear as [?], making it impossible to verify the claims about prior work. This is a serious presentation issue.
103	
104	### Questions for Authors
105	
106	1. Can you provide specific passages from CoCoHaNeRe where BM25-proxy negatives are presented as embedding-distance negatives?
107	2. Have you measured pos_sim for any encoders beyond Qwen and StarCoder?
108	3. Why were ANCE-style dynamic mining, in-batch negatives, and curriculum-based mining excluded from the comparison?
109	4. The data scaling ablation (Table 10) shows benefit diminishing from +1.8pp to +0.9pp as data grows. What is your estimate at 50K+ instances?
110	5. Why is "StructFuse" used as a system name when the paper is positioned as an analysis? Does the name set incorrect expectations?
111	
112	---
113	
114	## Roundtable: Cross-Reviewer Discussion
115	
116	### Points of Agreement (Both Reviewers)
117	
118	1. **Missing BM25 baseline is the most critical gap.** Both reviewers independently identify this as the experiment most needed to substantiate the paper's central narrative. Without it, the CoCoHaNeRe correction claim—which motivates the entire paper—is unverified.
119	
120	2. **N=2 encoders is insufficient for the representation geometry claim.** Both reviewers agree this limits the contribution from a "validated mechanism" to an "anecdotal observation." The framing should be significantly downgraded.
121	
122	3. **StarCoder2-3B architecture is mischaracterized.** Both flag that calling it "encoder-decoder" is factually incorrect (it is decoder-only), which weakens the "architecturally distinct" narrative.
123	
124	4. **Ablation breadth is a genuine strength.** Both credit the extensive ablation suite as above-average for this subfield.
125	
126	5. **Honest reporting is commendable.** Both appreciate the paper's willingness to report null and negative results without spin.
127	
128	6. **Effect sizes are too small for practical impact.** Both note that +0.5–1.3pp R@1 with no downstream significance limits the paper's practical contribution.
129	
130	7. **Missing error bars on RepoBench-R** is inconsistent with the statistical rigor shown on SWE-bench.
131	
132	### Points of Disagreement → Resolution
133	
134	- **R1 (4/6) vs. R2 (3/6) on overall score.** R1 is more generous toward the methodology framework as a standalone contribution; R2 argues the novelty is thin and the central narrative is unsubstantiated. After cross-sharing, both agree the missing BM25 baseline is disqualifying for the "correcting CoCoHaNeRe" framing, which is the paper's primary motivation. R1 adjusts downward; the consensus trends toward **3/6 (Weak Reject)** with a path to revision.
135	
136	- **Is the "analysis paper" positioning sufficient?** R1 initially sees the ablation suite as carrying the paper; R2 argues analysis papers need deeper analytical content (connection to theory, more data points). Consensus: the ablations are thorough but the analysis layer (representation geometry) is too shallow to stand as a primary contribution.
137	
138	---
139	
140	## Consolidated Assessment
141	
142	### Summary Judgment
143	
144	The paper tackles a relevant question—what hard negative mining strategies work for code retrieval—with above-average experimental discipline. The ablation breadth, honest null-result reporting, and controlled comparison design are genuine strengths. However, the paper has several critical gaps that prevent acceptance at a top venue:
145	
146	1. **The central narrative is unsubstantiated.** The "correcting CoCoHaNeRe" motivation requires running BM25 negatives to close the argument. Without this, the paper's raison d'être is speculative.
147	
148	2. **The analytical contribution is too shallow.** "Representation geometry" with n=2 encoders is an observation. Without connection to contrastive learning theory or validation across more models, it cannot stand as a primary contribution.
149	
150	3. **Effect sizes are marginal.** +0.5–1.3pp R@1 with CIs including zero on one encoder, no downstream significance, and diminishing returns at larger data scales collectively suggest limited practical value.
151	
152	4. **Presentation issues.** Broken bibliography ([?] throughout), StarCoder architecture mischaracterization, missing SWE-smith validation table, and inconsistent statistical reporting (CIs on SWE-bench but not RepoBench-R).
153	
154	### What Would Improve the Paper
155	
156	- Run a BM25 negative baseline to close the CoCoHaNeRe argument
157	- Add 2–3 more encoders with varying pos_sim to validate the saturation hypothesis
158	- Provide error bars/CIs on RepoBench-R results across multiple seeds
159	- Fix the bibliography and the StarCoder architecture description
160	- Add pool-size sensitivity analysis
161	- Connect to hard negative theory literature (Robinson et al., Kalantidis et al.)
162	- Stratify dataflow results by structural data availability (34% with data vs. 66% fallback)
163	
164	### Experiment Coverage vs. Design
165	
166	All 13 imagined experiments are reflected in the paper: SWE-bench Lite (Tables 2–3), RepoBench-R (Table 1), repo complexity (Table 6), hop depth (Table 9), data scaling (Table 10), fusion head (Table 11), weighted vs. binary dataflow (Table 12), failure analysis (Tables 4–5), qualitative examples (§7), temperature ablation (Tables 7–8), static vs. dynamic mining (Table 13), bootstrap CIs (Table 3), and inference-time comparison (Table 14). Coverage is complete. The issue is not missing experiments but missing critical baselines (BM25) and missing statistical reporting on existing experiments (RepoBench-R CIs).
167	
168	---
169	
170	## Final Scores
171	
172	| | Score | Confidence |
173	|---|---|---|
174	| R1 (Methods + Experiments) | 4/6 → 3/6 after roundtable | 4/5 |
175	| R2 (Novelty + Related Work) | 3/6 | 4/5 |
176	| **Consolidated** | **3/6 (Weak Reject)** | **4/5** |
177	
178	### Decision Rationale
179	
180	The paper demonstrates solid experimental practice but fails to substantiate its central narrative (CoCoHaNeRe correction without BM25 baseline), offers insufficient analytical depth for an analysis paper (representation geometry on n=2), and reports effect sizes too small for practical significance. With the suggested revisions—particularly the BM25 baseline, additional encoders, and RepoBench-R error bars—this could become a solid contribution in a future revision cycle.
181	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69df3585-0ab9-4631-a63c-71f766729109",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "8e7bdb0a-e55d-41ba-a052-0468c2276716",
  "sourceToolAssistantUUID": "69df3585-0ab9-4631-a63c-71f766729109",
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

_source line 35 · 2026-05-14T08:38:54.374Z_

<details><summary>↩ Tool result · `toolu_011gFN7ZbWchkA82p6yq4bRA`</summary>

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
  "parentUuid": "fc5cbef4-449a-4338-8777-4ddef17b9d29",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "bc89e8d2-000f-46e1-b801-34c5dc5b8e7b",
  "sourceToolAssistantUUID": "fc5cbef4-449a-4338-8777-4ddef17b9d29",
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

_source line 36 · 2026-05-14T08:38:59.611Z_

Now let me read the latest paper version (the one described in the user's prompt which appears to be a newer "negative result" framing). Let me check the best and worst versions too, and check for the actual paper title mentioned in the prompt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc89e8d2-000f-46e1-b801-34c5dc5b8e7b",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ACzGigyUdwPg5hek2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11ca25bd-808f-463e-9fe4-e56924600409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TER2Vb1Dzm7vbBBY7sampD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4636,
      "cache_creation_input_tokens": 10033,
      "cache_read_input_tokens": 44310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10033,
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

_source line 37 · 2026-05-14T08:39:02.450Z_

<details open><summary>🔧 Tool call — Read · `toolu_016pCgnkBCjtGg9avEYZKuMc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11ca25bd-808f-463e-9fe4-e56924600409",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ACzGigyUdwPg5hek2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41863a47-84db-44f4-9065-6ec9bc07464e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TER2Vb1Dzm7vbBBY7sampD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4636,
      "cache_creation_input_tokens": 10033,
      "cache_read_input_tokens": 44310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10033,
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

_source line 38 · 2026-05-14T08:39:02.664Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MrGtK4EKYkA8NYnhq4winf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41863a47-84db-44f4-9065-6ec9bc07464e",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ACzGigyUdwPg5hek2G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "655001a5-c263-400e-afc4-c6a80c5fea48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TER2Vb1Dzm7vbBBY7sampD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4636,
      "cache_creation_input_tokens": 10033,
      "cache_read_input_tokens": 44310,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10033
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4636,
          "output_tokens": 236,
          "cache_read_input_tokens": 44310,
          "cache_creation_input_tokens": 10033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10033,
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

_source line 39 · 2026-05-14T08:39:02.669Z_

<details><summary>↩ Tool result · `toolu_01MrGtK4EKYkA8NYnhq4winf`</summary>

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
  "parentUuid": "655001a5-c263-400e-afc4-c6a80c5fea48",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "aeeb0ff9-59c1-45e6-87ed-cd4eeaa425a4",
  "sourceToolAssistantUUID": "655001a5-c263-400e-afc4-c6a80c5fea48",
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

_source line 40 · 2026-05-14T08:39:02.858Z_

<details><summary>↩ Tool result · `toolu_016pCgnkBCjtGg9avEYZKuMc`</summary>

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
61	
62	\item \textbf{Open infrastructure.} Our CodeQL-based pipeline for inter-procedural dataflow analysis achieves 0\% timeout rate across 123 repositories and is released as a general-purpose structural negative generator (\S\ref{sec:method}).
63	\end{enumerate}
64	
65	
66	%% ============================================================
67	%% 2  RELATED WORK
68	%% ============================================================
69	\section{Related Work}
70	
71	\paragraph{Hard negative mining for retrieval.}
72	ANCE~\cite{xiong2021ance} demonstrated the value of periodically refreshed hard negatives for open-domain QA.
73	Curriculum-based mining schedules negative difficulty during training.
74	For code, CoCoHaNeRe~\cite{gao2024cocohanere} studied negative strategies but conflated BM25-proxy with true embedding-distance negatives.
75	
76	\paragraph{Code retrieval.}
77	SweRank~\cite{li2023swerank} and SWE-Fixer~\cite{yang2024swefixer} use contrastive learning for repo-level file retrieval.
78	GraphCodeBERT~\cite{guo2021graphcodebert} incorporates data flow edges as pre-training signal but not as negative selection criterion.
79	RepoFusion~\cite{shrivastava2023repofusion} fuses cross-file context for code completion.
80	
81	\paragraph{Structure-guided code understanding.}
82	LocAgent~\cite{qin2024locagent} and CodexGraph~\cite{liu2024codexgraph} use structural graphs at \emph{inference time} for repository navigation.
83	ARISE~\cite{wu2024arise} uses intra-procedural data flow for code repair but does not cross call boundaries.
84	Our work differs by using inter-procedural dataflow at \emph{training time} for negative selection---and by demonstrating that this approach does not improve retrieval.
85	
86	
87	%% ============================================================
88	%% 3  METHOD
89	%% ============================================================
90	\section{Method}
91	\label{sec:method}
92	
93	\subsection{Task and Training Setup}
94	
95	Given a bug report (issue text) as query $q$ and a repository with files $\{f_1, \ldots, f_N\}$, the retriever must rank the gold file(s) $f^*$ above all others.
96	We train bi-encoder retrievers using InfoNCE loss with temperature $\tau$:
97	\begin{equation}
98	\mathcal{L} = -\log \frac{\exp(\text{sim}(q, f^+)/\tau)}{\exp(\text{sim}(q, f^+)/\tau) + \sum_{j} \exp(\text{sim}(q, f^-_j)/\tau)}
99	\end{equation}
100	where $f^+$ is the gold file and $\{f^-_j\}$ are negatives selected by the strategy under study.
101	
102	\paragraph{Encoders.}
103	We use two architecturally distinct code LLMs as bi-encoder backbones:
104	(1) \textbf{Qwen2.5-Coder-3B}, which exhibits representation saturation (pretrained $\text{pos\_sim} = 0.9855$, embedding negative margin $= 0.017$);
105	(2) \textbf{StarCoder2-3B}, with a healthier representation space ($\text{pos\_sim} = 0.7985$, margin $= 0.194$).
106	Both are fine-tuned with LoRA (rank 16).
107	
108	\paragraph{Training data.}
109	We use SWE-smith instances. The pilot dataset comprises ${\sim}$2K instances from 8 medium-sized repositories (mean 45 files/repo, structural data rate 0.58). The full-scale dataset comprises 15,133 instances from 123 repositories (mean 185 files/repo, structural data rate 0.34).
110	
111	\subsection{Negative Mining Strategies}
112	
113	\paragraph{Random.}
114	Sample negatives uniformly from the repository's non-gold files.
115	
116	\paragraph{Embedding-distance.}
117	Rank non-gold files by cosine similarity to the query in the pretrained encoder's embedding space; select the top-$k$ nearest as hard negatives.
118	
119	\paragraph{Dataflow-aware.}
120	Using inter-procedural dataflow analysis via CodeQL, we construct a call-graph--bounded connectivity map.
121	Files \emph{not} reachable from any gold file within $h$ hops ($h=2$ by default) are considered structurally disconnected.
122	Among disconnected files, we select those with highest embedding similarity as negatives---combining structural irrelevance with surface-level confusability.
123	
124	\subsection{CodeQL Pipeline}
125	
126	We implement scope-bounded inter-procedural dataflow analysis using CodeQL.
127	For each repository, we extract call-graph edges and data-flow paths, then compute pairwise file connectivity within a hop budget.
128	The pipeline achieves 0\% timeout rate and produces output for 123/131 attempted repositories.
129	
130	
131	%% ============================================================
132	%% 4  EXPERIMENTS
133	%% ============================================================
134	\section{Experiments}
135	\label{sec:experiments}
136	
137	\subsection{Full-Scale Multi-Seed Results}
138	\label{sec:fullscale}
139	
140	We train 27 runs per encoder (9 seeds $\times$ 3 strategies) at full scale (15K instances).
141	
142	\paragraph{Qwen2.5-Coder-3B.}
143	Table~\ref{tab:qwen_full} reports R@1 for each seed--strategy combination.
144	The mean R@1 across seeds is $0.523 \pm 0.031$ (random), $0.521 \pm 0.035$ (embedding), and $0.515 \pm 0.038$ (dataflow).
145	The embedding-vs-random delta is $-0.2$pp; the dataflow-vs-random delta is $-0.8$pp.
146	Neither is significant given cross-seed standard deviation of 3.1pp.
147	Examining per-seed winners, random wins in 4/9 seeds, embedding in 3/9, and dataflow in 2/9---consistent with chance.
148	
149	\begin{table}[t]
150	\centering
151	\small
152	\caption{Qwen2.5-Coder-3B full-scale R@1 by strategy and seed. Mean$\pm$std: random $0.523 \pm 0.031$, embedding $0.521 \pm 0.035$, dataflow $0.515 \pm 0.038$.}
153	\label{tab:qwen_full}
154	\begin{tabular}{lccc}
155	\toprule
156	Seed & Random & Embedding & Dataflow \\
157	\midrule
158	42   & 0.553 & 0.547 & 0.538 \\
159	123  & 0.528 & 0.534 & 0.521 \\
160	456  & 0.512 & 0.498 & 0.503 \\
161	789  & 0.541 & 0.543 & 0.530 \\
162	1024 & 0.498 & 0.510 & 0.496 \\
163	2048 & 0.519 & 0.522 & 0.512 \\
164	3000 & 0.505 & 0.503 & 0.478 \\
165	4096 & 0.530 & 0.517 & 0.525 \\
166	5000 & 0.523 & 0.515 & 0.532 \\
167	\midrule
168	Mean & 0.523 & 0.521 & 0.515 \\
169	Std  & 0.017 & 0.016 & 0.019 \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	\paragraph{StarCoder2-3B.}
175	Table~\ref{tab:starcoder_full} shows analogous results.
176	Mean R@1: random $0.443 \pm 0.028$, embedding $0.435 \pm 0.033$, dataflow $0.428 \pm 0.040$.
177	The embedding-vs-random delta is $-0.8$pp and dataflow-vs-random is $-1.5$pp.
178	Cross-seed std (3.4pp) again dwarfs strategy-level differences.
179	
180	\begin{table}[t]
181	\centering
182	\small
183	\caption{StarCoder2-3B full-scale R@1 by strategy and seed. Dataflow performs worst ($-1.5$pp vs.\ random).}
184	\label{tab:starcoder_full}
185	\begin{tabular}{lccc}
186	\toprule
187	Seed & Random & Embedding & Dataflow \\
188	\midrule
189	42   & 0.454 & 0.448 & 0.442 \\
190	123  & 0.440 & 0.425 & 0.418 \\
191	456  & 0.462 & 0.456 & 0.440 \\
192	789  & 0.435 & 0.430 & 0.412 \\
193	1024 & 0.448 & 0.442 & 0.435 \\
194	2048 & 0.425 & 0.418 & 0.398 \\
195	3000 & 0.458 & 0.450 & 0.448 \\
196	4096 & 0.430 & 0.422 & 0.425 \\
197	5000 & 0.438 & 0.428 & 0.430 \\
198	\midrule
199	Mean & 0.443 & 0.435 & 0.428 \\
200	Std  & 0.013 & 0.014 & 0.017 \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	\subsection{Downstream Evaluation: SWE-bench Lite}
206	\label{sec:swebench}
207	
208	We evaluate the best checkpoint from each strategy as a retriever in an end-to-end SWE-bench Lite pipeline (300 instances, 287 successfully evaluated) using a Qwen3.6-27B agent for patch generation.
209	
210	Table~\ref{tab:swebench} shows resolve rates.
211	The best strategy (embedding, 19.0\%) exceeds random (18.7\%) by only +0.3pp.
212	McNemar's test yields $p = 0.89$; bootstrap 95\% CIs for the embedding-vs-random delta span $[-3.8, +4.5]$pp (Table~\ref{tab:bootstrap}).
213	The difference corresponds to a single additional resolved instance (55 vs.\ 54 out of 287).
214	
215	\begin{table}[t]
216	\centering
217	\small
218	\caption{SWE-bench Lite resolve rates and retrieval R@1. No strategy achieves significant improvement.}
219	\label{tab:swebench}
220	\begin{tabular}{lcccc}
221	\toprule
222	Strategy & Resolve & R@1 & Resolved & Total \\
223	\midrule
224	Random           & 0.187 & 0.42 & 54 & 287 \\
225	Embedding        & 0.190 & 0.43 & 55 & 287 \\
226	Dataflow         & 0.183 & 0.41 & 53 & 287 \\
227	\bottomrule
228	\end{tabular}
229	\end{table}
230	
231	\begin{table}[t]
232	\centering
233	\small
234	\caption{Bootstrap statistics (10,000 resamples) for SWE-bench Lite resolve rate comparisons.}
235	\label{tab:bootstrap}
236	\begin{tabular}{lccc}
237	\toprule
238	Comparison & $\Delta$pp & 95\% CI & $p$ \\
239	\midrule
240	embed vs.\ random   & +0.3 & [$-$3.8, +4.5] & 0.78 \\
241	dataflow vs.\ random & $-$0.4 & [$-$4.8, +3.8] & 0.68 \\
242	dataflow vs.\ embed  & $-$0.7 & [$-$5.2, +3.5] & 0.55 \\
243	\bottomrule
244	\end{tabular}
245	\end{table}
246	
247	\subsection{Cross-Domain Evaluation: RepoBench-R}
248	\label{sec:repobench}
249	
250	We evaluate on RepoBench-R (cross-file code completion retrieval) using the Qwen encoder to test generalization beyond SWE-smith's bug-localization distribution (Table~\ref{tab:repobench}).
251	
252	All fine-tuned strategies improve over the pretrained baseline (+2--3pp R@1), confirming that contrastive fine-tuning itself is effective.
253	However, dataflow negatives exhibit negative transfer ($-1.7$pp vs.\ random), likely because SWE-smith's ``structurally disconnected $=$ irrelevant'' assumption does not hold for completion-oriented code.
254	Embedding negatives are also slightly below random ($-0.4$pp).
255	
256	\begin{table}[t]
257	\centering
258	\small
259	\caption{RepoBench-R results (Qwen encoder). Fine-tuning helps, but mining strategies do not outperform random.}
260	\label{tab:repobench}
261	\begin{tabular}{lcccc}
262	\toprule
263	Strategy & R@1 & R@5 & R@10 & MRR \\
264	\midrule
265	Pretrained        & 0.285 & 0.520 & 0.680 & 0.401 \\
266	Random            & 0.312 & 0.580 & 0.730 & 0.438 \\
267	Embedding         & 0.308 & 0.570 & 0.720 & 0.432 \\
268	Dataflow          & 0.295 & 0.560 & 0.710 & 0.418 \\
269	\bottomrule
270	\end{tabular}
271	\end{table}
272	
273	\subsection{Comparison with Inference-Time Graph Methods}
274	\label{sec:inference_graph}
275	
276	Table~\ref{tab:inference_compare} contextualizes our results against inference-time structural methods.
277	LocAgent (26.2\% resolve rate on SWE-bench) substantially outperforms all our training-time strategies (${\sim}$19\%).
278	This suggests that structural information is valuable when applied adaptively at inference---navigating the call graph per query---rather than statically during training.
279	
280	\begin{table}[t]
281	\centering
282	\small
283	\caption{Training-time vs.\ inference-time structure utilization. Inference-time methods substantially outperform training-time mining. ($^*$Different benchmark, not directly comparable.)}
284	\label{tab:inference_compare}
285	\begin{tabular}{llcc}
286	\toprule
287	Method & Structure Use & Resolve & R@1 \\
288	\midrule
289	Ours (random)   & training neg.  & 0.187 & 0.523 \\
290	Ours (dataflow) & training neg.  & 0.183 & 0.515 \\
291	LocAgent        & inference nav. & 0.262 & --- \\
292	CodexGraph      & inference nav. & ---   & 0.48$^*$ \\
293	\bottomrule
294	\end{tabular}
295	\end{table}
296	
297	
298	%% ============================================================
299	%% 5  ANALYSIS: WHY PILOT RESULTS DON'T SCALE
300	%% ============================================================
301	\section{Analysis}
302	\label{sec:analysis}
303	
304	\subsection{Data Size Scaling Law}
305	\label{sec:scaling}
306	
307	The key to understanding the pilot-to-full-scale discrepancy is a data-size--benefit interaction.
308	Table~\ref{tab:scaling} reports R@1 for sub-sampled training sets of 1K, 3K, 5K, and the full 15K instances.
309	
310	At 1K instances (approximating pilot scale), embedding mining yields +1.3pp over random, replicating the pilot finding and confirming that the pilot was not a bug.
311	The benefit decays monotonically with a slope of $-0.11$pp per 1K additional instances, crossing zero between 3K and 5K.
312	At 15K, the delta inverts to $-0.2$pp.
313	
314	The mechanism is straightforward: at small scale, the random negative pool contains few truly hard negatives; embedding mining provides a necessary difficulty gradient.
315	As the pool grows, random sampling increasingly hits moderately hard negatives by chance, eroding the marginal value of curated mining.
316	
317	\begin{table}[t]
318	\centering
319	\small
320	\caption{Data size $\times$ strategy interaction (Qwen). Embedding benefit decays at $-0.11$pp/1K instances.}
321	\label{tab:scaling}
322	\begin{tabular}{lcccc}
323	\toprule
324	Size & Random & Embed & Dataflow & $\Delta_\text{embed}$ \\
325	\midrule
326	1K         & 0.505 & 0.518 & 0.512 & +1.3 \\
327	3K         & 0.515 & 0.520 & 0.513 & +0.5 \\
328	5K         & 0.520 & 0.521 & 0.516 & +0.1 \\
329	15K (full) & 0.523 & 0.521 & 0.515 & $-$0.2 \\
330	\bottomrule
331	\end{tabular}
332	\end{table}
333	
334	\subsection{Stratified Analysis of Embedding Benefit}
335	\label{sec:stratified}
336	
337	To understand \emph{where} embedding mining helps or hurts, we stratify by repository size and negative difficulty quartile (Table~\ref{tab:stratified}).
338	
339	Embedding mining is harmful for small repositories ($-2.0$pp), where the file pool (${\sim}$10--50 files) is so small that nearest-neighbor negatives are often near-duplicates of gold files, creating false hard negatives.
340	It provides a slight advantage for medium repositories (+1.0pp) but no benefit for large/xlarge repositories, where random sampling already provides sufficient difficulty.
341	
342	Stratifying by negative difficulty quartile reveals a complementary pattern: embedding mining helps in the easiest quartile (+0.5pp) but hurts in the hardest ($-2.1$pp), where overly difficult negatives cause gradient conflicts.
343	
344	The pilot dataset over-represented medium-sized repositories (the ``sweet spot''), explaining the apparent benefit.
345	
346	\begin{table}[t]
347	\centering
348	\small
349	\caption{Embedding benefit by repository size tier. Pilot data over-represented medium repos.}
350	\label{tab:stratified}
351	\begin{tabular}{lrrrr}
352	\toprule
353	Repo Tier & $n$ & Rand & Embed & $\Delta$pp \\
354	\midrule
355	Small ($<$50)    & 500   & 0.610 & 0.590 & $-$2.0 \\
356	Medium (50--200) & 4,096 & 0.540 & 0.550 & +1.0 \\
357	Large (200--500) & 13,628 & 0.510 & 0.500 & $-$1.0 \\
358	XLarge (500+)    & 25,949 & 0.480 & 0.480 & 0.0 \\
359	\bottomrule
360	\end{tabular}
361	\end{table}
362	
363	\subsection{Data Pipeline Audit}
364	\label{sec:audit}
365	
366	To rule out engineering errors, we audited the full-scale data pipeline against the pilot (Table~\ref{tab:audit}).
367	No bugs were found, but significant distributional shift was confirmed:
368	the full-scale data draws from 123 repositories (vs.\ 8 in pilot), with large/xlarge repos comprising 56\% (vs.\ 30\%), mean files per repo of 185 (vs.\ 45), and structural data rate of 0.34 (vs.\ 0.58).
369	A KS test on negative difficulty distributions rejects equivalence ($p = 0.003$).
370	
371	This shift is not a bug but a consequence of realistic scaling---the pilot's repository selection was biased toward CodeQL-friendly, medium-sized repos with high structural coverage.
372	
373	\begin{table}[t]
374	\centering
375	\small
376	\caption{Pilot vs.\ full-scale data distribution. Shift is systematic but not a pipeline bug.}
377	\label{tab:audit}
378	\begin{tabular}{lccc}
379	\toprule
380	Metric & Pilot & Full & $p$ \\
381	\midrule
382	Instances       & ${\sim}$2,000 & 15,133 & --- \\
383	Repositories    & 8         & 123   & --- \\
384	Structural rate & 0.58      & 0.34  & $<$0.001 \\
385	Files/repo      & 45        & 185   & $<$0.001 \\
386	Embed margin    & 0.025     & 0.017 & 0.003 \\
387	\% large repos  & 0.30      & 0.56  & $<$0.001 \\
388	\bottomrule
389	\end{tabular}
390	\end{table}
391	
392	\subsection{Failure Taxonomy}
393	\label{sec:failure}
394	
395	We manually analyzed 50 instances where both SweRank and BM25 fail to retrieve the gold file, asking whether dataflow signals could theoretically help (Table~\ref{tab:failure}).
396	
397	Of 50 failures, only 6 (12\%) involve cross-file dependencies where dataflow information could plausibly assist.
398	Of these, dataflow-trained models actually helped in only 2 cases (4\%) while actively hurting in 3 (6\%)---the structural proximity signal elevated structurally related but incorrect files above the gold file.
399	The dominant failure modes (naming ambiguity, scattered changes, test file confusion) are orthogonal to structural connectivity.
400	
401	\begin{table}[t]
402	\centering
403	\small
404	\caption{Failure category analysis (50 SweRank/BM25 failures). Dataflow's theoretical coverage (12\%) and actual help rate (4\%) are both low.}
405	\label{tab:failure}
406	\begin{tabular}{lcccc}
407	\toprule
408	Category & $n$ & Could Help & Helped & Hurt \\
409	\midrule
410	Cross-file dep.     & 18 & 4 & 1 & 1 \\
411	Naming ambiguity    & 12 & 0 & 0 & 1 \\
412	Scattered changes   &  9 & 2 & 1 & 1 \\
413	Test confusion      &  7 & 0 & 0 & 0 \\
414	Other               &  4 & 0 & 0 & 0 \\
415	\midrule
416	Total               & 50 & 6 & 2 & 3 \\
417	\bottomrule
418	\end{tabular}
419	\end{table}
420	
421	
422	%% ============================================================
423	%% 6  ABLATIONS
424	%% ============================================================
425	\section{Ablations}
426	\label{sec:ablations}
427	
428	\subsection{Temperature}
429	
430	We test whether the null result is regime-specific by varying $\tau \in \{0.05, 0.1, 0.2\}$ (Table~\ref{tab:temperature}).
431	Random is the best or tied-best strategy at all temperatures.
432	At $\tau = 0.05$, all strategies degrade (the loss becomes hypersensitive to the already-small margins in Qwen's saturated space), with dataflow suffering most ($-2.3$pp vs.\ $\tau = 0.1$).
433	No temperature makes embedding benefit significant.
434	
435	\begin{table}[t]
436	\centering
437	\small
438	\caption{Temperature $\times$ strategy interaction (Qwen, mean of 3 seeds). Random is best at every $\tau$.}
439	\label{tab:temperature}
440	\begin{tabular}{lcccc}
441	\toprule
442	$\tau$ & Random & Embed & Dataflow & Best \\
443	\midrule
444	0.05 & 0.498 & 0.485 & 0.475 & random \\
445	0.10 & 0.523 & 0.521 & 0.515 & random \\
446	0.20 & 0.510 & 0.508 & 0.502 & random \\
447	\bottomrule
448	\end{tabular}
449	\end{table}
450	
451	\subsection{Hop-Distance for Dataflow Negatives}
452	
453	We vary the call-graph hop budget $h \in \{1, 2, 3\}$ for defining structural disconnection (Table~\ref{tab:hops}).
454	All hop settings underperform random ($-0.8$ to $-1.3$pp).
455	At $h=1$, only 12\% of file pairs are connected, creating many false hard negatives.
456	At $h=3$, 58\% are connected, leaving a small disconnected pool with trivially easy negatives.
457	The intermediate $h=2$ (our default) is the best among dataflow variants but still inferior to random.
458	
459	\begin{table}[t]
460	\centering
461	\small
462	\caption{Hop-distance ablation (Qwen, seed 42). No hop setting matches random.}
463	\label{tab:hops}
464	\begin{tabular}{lcccc}
465	\toprule
466	Hops & Connected\% & Margin & R@1 & vs.\ Random \\
467	\midrule
468	1      & 0.12 & 0.035 & 0.513 & $-$1.0 \\
469	2      & 0.34 & 0.029 & 0.515 & $-$0.8 \\
470	3      & 0.58 & 0.022 & 0.510 & $-$1.3 \\
471	Random & ---  & ---   & 0.523 & 0.0 \\
472	\bottomrule
473	\end{tabular}
474	\end{table}
475	
476	\subsection{Fusion Head Architecture}
477	
478	To test whether structural features help through a different mechanism than negative mining, we compare embedding-only, structural-features-only, and combined fusion heads (Table~\ref{tab:fusion}).
479	
480	Structural features alone (binary connectivity, dataflow distance, call-graph hops) achieve only R@1 = 0.385, as 66\% of instances lack structural data.
481	The combined fusion head slightly \emph{degrades} performance ($-0.4$pp vs.\ embedding-only), as noisy structural features interfere with the embedding signal under LoRA's low-rank constraint.
482	
483	\begin{table}[t]
484	\centering
485	\small
486	\caption{Fusion head ablation (Qwen, seed 42). Structural features add noise, not signal.}
487	\label{tab:fusion}
488	\begin{tabular}{lccc}
489	\toprule
490	Head Type & R@1 & R@5 & Val Loss \\
491	\midrule
492	Embedding only    & 0.523 & 0.955 & 0.486 \\
493	Structural only   & 0.385 & 0.780 & 0.812 \\
494	Combined          & 0.519 & 0.950 & 0.495 \\
495	\bottomrule
496	\end{tabular}
497	\end{table}
498	
499	\subsection{Dynamic vs.\ Static Mining}
500	
501	We test whether mining negatives from a stale pretrained model (static) explains the null result by re-mining after each epoch (dynamic).
502	Table~\ref{tab:dynamic} shows dynamic mining does not help ($-0.3$pp vs.\ static, $-0.5$pp vs.\ random).
503	Re-mining with a partially fine-tuned model introduces curriculum shifts and LoRA artifacts without improving negative quality.
504	
505	\begin{table}[t]
506	\centering
507	\small
508	\caption{Static vs.\ dynamic embedding mining (Qwen, seed 42). Dynamic mining slightly degrades performance.}
509	\label{tab:dynamic}
510	\begin{tabular}{lcccc}
511	\toprule
512	Method & Ep.1 & Ep.2 & Ep.3 & Best \\
513	\midrule
514	Static  & 0.540 & 0.530 & 0.512 & 0.540 \\
515	Dynamic & 0.540 & 0.525 & 0.505 & 0.540 \\
516	Random  & 0.535 & 0.528 & 0.510 & 0.535 \\
517	\bottomrule
518	\end{tabular}
519	\end{table}
520	
521	\subsection{Dataflow Distance Weighting}
522	
523	Instead of binary connected/disconnected classification, we weight negative selection by continuous dataflow distance.
524	This yields R@1 = 0.517 (+0.2pp over binary, $-0.6$pp vs.\ random).
525	Refining the granularity of an ineffective signal does not rescue it.
526	
527	%% ============================================================
528	%% 7  DISCUSSION
529	%% ============================================================
530	\section{Discussion}
531	
532	\paragraph{Why do pilot results mislead?}
533	Our scaling analysis (\S\ref{sec:scaling}) identifies two interacting factors:
534	(1) \emph{Data composition bias}: pilot repos were selected for CodeQL compatibility, over-representing medium-sized repos where embedding mining's sweet spot lies (\S\ref{sec:stratified}).
535	(2) \emph{Scale-dependent difficulty}: at small scale, random negative pools are too easy; curated mining fills a genuine gap.
536	As data grows, random sampling naturally encounters harder negatives, making curated selection redundant.
537	
538	\paragraph{Structural information: training vs.\ inference.}
539	Our negative results for training-time structural mining contrast sharply with the success of inference-time graph methods (LocAgent: 26.2\% resolve rate vs.\ our 18.7\%).
540	The key difference is \emph{adaptivity}: inference-time methods select structural information conditioned on the specific query, while training-time mining applies a fixed structural criterion across all queries.
541	This suggests that structural signal is query-dependent---a file's structural relevance varies by bug type---and cannot be captured by a static negative selection policy.
542	
543	\paragraph{Implications for practitioners.}
544	Our findings suggest that for code retrieval with $>$5K training instances, investing in hard negative mining (embedding or structural) does not improve over random sampling.
545	Effort is better spent on data scaling and inference-time retrieval augmentation.
546	For small-scale settings ($<$3K instances), embedding mining remains beneficial (+0.5--1.3pp).
547	
548	\paragraph{Limitations.}
549	Our study uses two 3B-parameter encoders with LoRA; larger encoders or full fine-tuning may behave differently.
550	The structural analysis is limited to CodeQL-supported languages (primarily Python).
551	SWE-bench Lite's 300 instances provide limited statistical power for downstream evaluation (detectable effect size $>$5pp at $\alpha = 0.05$).
552	
553	
554	%% ============================================================
555	%% 8  CONCLUSION
556	%% ============================================================
557	\section{Conclusion}
558	
559	We presented a large-scale systematic study of hard negative mining strategies for contrastive code retrieval, spanning 54 training runs across two encoders, three strategies, and nine seeds.
560	Our initially promising pilot results---embedding mining improves R@1 by +1.6--2.0pp---failed to replicate at full scale, where strategy-level differences were dwarfed by seed variance and no strategy achieved statistically significant improvement over random sampling.
561	
562	We traced this failure to a data-size--benefit scaling law ($-0.11$pp per 1K instances) and pilot data composition bias.
563	Our ablations ruled out temperature regime, mining staleness, hop distance, and fusion architecture as confounds.
564	Failure analysis showed that structural (dataflow) signals have narrow applicability (4\% actual help rate) and can cause negative transfer on out-of-distribution benchmarks.
565	
566	These results carry a methodological warning: single-seed, small-scale evaluations of hard negative mining can produce convincingly positive but ultimately unreliable conclusions.
567	Multi-seed, multi-scale evaluation should be standard practice before concluding that a mining strategy provides genuine benefit.
568	
569	We release our CodeQL-based dataflow analysis pipeline as open-source infrastructure for future research on structural code understanding.
570	
571	\begin{thebibliography}{10}
572	
573	\bibitem[Xiong et~al.(2021)]{xiong2021ance}
574	Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, and Arnold Overwijk.
575	\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.
576	\newblock In \emph{ICLR}, 2021.
577	
578	\bibitem[Li et~al.(2023)]{li2023swerank}
579	Raymond Li et~al.
580	\newblock SweRank: contrastive learning for repository-level code retrieval.
581	\newblock \emph{arXiv preprint}, 2023.
582	
583	\bibitem[Yang et~al.(2024)]{yang2024swefixer}
584	Chao Yang et~al.
585	\newblock SWE-Fixer: training open-source LLMs for effective and efficient GitHub issue resolution.
586	\newblock \emph{arXiv preprint}, 2024.
587	
588	\bibitem[Gao et~al.(2024)]{gao2024cocohanere}
589	Xinyu Gao et~al.
590	\newblock CoCoHaNeRe: contrastive code hard negative retrieval.
591	\newblock In \emph{EMNLP}, 2024.
592	
593	\bibitem[Guo et~al.(2021)]{guo2021graphcodebert}
594	Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, et~al.
595	\newblock GraphCodeBERT: pre-training code representations with data flow.
596	\newblock In \emph{ICLR}, 2021.
597	
598	\bibitem[Shrivastava et~al.(2023)]{shrivastava2023repofusion}
599	Disha Shrivastava, Hugo Larochelle, and Daniel Tarlow.
600	\newblock RepoFusion: training code models to understand your repository.
601	\newblock \emph{arXiv preprint}, 2023.
602	
603	\bibitem[Qin et~al.(2024)]{qin2024locagent}
604	Kechi Qin et~al.
605	\newblock LocAgent: graph-guided LLM agents for code localization.
606	\newblock \emph{arXiv preprint}, 2024.
607	
608	\bibitem[Liu et~al.(2024)]{liu2024codexgraph}
609	Xiangyan Liu et~al.
610	\newblock CodexGraph: bridging large language models and code repositories via code graph databases.
611	\newblock \emph{arXiv preprint}, 2024.
612	
613	\bibitem[Wu et~al.(2024)]{wu2024arise}
614	Jiaheng Wu et~al.
615	\newblock ARISE: autonomous repair with intra-procedural static execution.
616	\newblock \emph{arXiv preprint}, 2024.
617	
618	\end{thebibliography}
619	
620	\appendix
621	
622	\section{Full Data Distribution Audit}
623	\label{app:audit}
624	
625	Table~\ref{tab:audit} in the main text summarizes the pilot-vs-full distributional comparison.
626	The pilot dataset was drawn from 8 repositories selected for high CodeQL coverage, resulting in a structural data rate of 0.58 (fraction of instances with non-trivial dataflow information).
627	At full scale, coverage drops to 0.34 as larger repositories with sparser structural annotations dominate.
628	This shift is confirmed by a KS test on negative difficulty distributions ($p = 0.003$).
629	No data pipeline bugs were identified: repo overlap between pilot and full-scale is 85\%, and the shift arises naturally from including repositories spanning the full size distribution.
630	
631	\end{document}
632	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41863a47-84db-44f4-9065-6ec9bc07464e",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "6a155719-1bd3-4f60-8f76-b5f818c65da3",
  "sourceToolAssistantUUID": "41863a47-84db-44f4-9065-6ec9bc07464e",
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

_source line 41 · 2026-05-14T08:39:07.536Z_

Now let me also check the previous dream's review reports for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a155719-1bd3-4f60-8f76-b5f818c65da3",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ADcXJFZs3MjWjsBjU6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9aee13d3-a0a3-44d7-a508-e576ad6c8cbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLcu6KiWiRY77qyfdHfoDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8944,
      "cache_creation_input_tokens": 16484,
      "cache_read_input_tokens": 54343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16484,
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

_source line 42 · 2026-05-14T08:39:09.885Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BALvSShPcbU9dpo9MnS4Up`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9aee13d3-a0a3-44d7-a508-e576ad6c8cbe",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ADcXJFZs3MjWjsBjU6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b57ff8c-0e24-4e99-a4a3-34e893443611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLcu6KiWiRY77qyfdHfoDh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8944,
      "cache_creation_input_tokens": 16484,
      "cache_read_input_tokens": 54343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16484,
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

_source line 43 · 2026-05-14T08:39:09.900Z_

<details><summary>↩ Tool result · reported error · `toolu_01BALvSShPcbU9dpo9MnS4Up`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b57ff8c-0e24-4e99-a4a3-34e893443611",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "cc98d879-e988-476e-b719-a857c382d111",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context.",
  "sourceToolAssistantUUID": "4b57ff8c-0e24-4e99-a4a3-34e893443611",
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

_source line 44 · 2026-05-14T08:39:10.484Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WvuRbiuTZ7NttfksPjtU3N`</summary>

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
  "parentUuid": "cc98d879-e988-476e-b719-a857c382d111",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2ADcXJFZs3MjWjsBjU6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4256af6-e112-4312-a7d8-f1996a65d2b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLcu6KiWiRY77qyfdHfoDh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8944,
      "cache_creation_input_tokens": 16484,
      "cache_read_input_tokens": 54343,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16484
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8944,
          "output_tokens": 203,
          "cache_read_input_tokens": 54343,
          "cache_creation_input_tokens": 16484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16484,
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

_source line 45 · 2026-05-14T08:39:10.489Z_

<details><summary>↩ Tool result · `toolu_01WvuRbiuTZ7NttfksPjtU3N`</summary>

```text
1	---
2	dream_id: dream_20260514T075732
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-14T08:33:59.100296+00:00
6	---
7	
8	---
9	dream_id: dream_20260514T075732
10	tier: best
11	reviewer: R1 (Methods and Experiments)
12	overall_score: 4/6 Weak Accept
13	timestamp: 2026-05-14
14	---
15	
16	# R1 Review: Methods and Experiments
17	
18	**Paper**: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
19	
20	---
21	
22	## Summary
23	
24	The paper presents a controlled comparison of three hard negative mining strategies (random, embedding-distance, dataflow-aware) for contrastive code retrieval, evaluated across two 3B-parameter encoders with 9 seeds each. The main findings are that embedding-distance mining consistently improves R@1 (+2.3pp Qwen, +1.7pp StarCoder), while dataflow-aware mining provides conditional benefit mediated by representation saturation (significant on Qwen, null on StarCoder). The experimental design is ambitious and the ablation suite is commendably broad, but several methodological concerns -- including the generalizability of the "representation geometry" theory from only 2 encoders, unrealistic retrieval pool sizes, missing baselines, and discrepancies between reported and actual result maturity -- undermine the strength of the claims.
25	
26	---
27	
28	## Strengths
29	
30	- **Exemplary experimental scale and statistical discipline.** 54 training runs (2 x 3 x 9) with paired bootstrap 95% CIs and explicit p-values for all main comparisons is well above the standard for this subfield. The paper does not rely on single-seed results, and the statistical testing is appropriate (bootstrap CIs, paired comparisons).
31	
32	- **Comprehensive ablation suite with clear analytical purpose.** Each ablation (temperature, hop depth, data scaling, fusion head, static vs. dynamic mining, binary vs. weighted dataflow) answers a specific methodological question rather than padding the paper. The dynamic mining baseline (Table 13) is particularly valuable for ruling out curriculum effects as a confound, and the fusion head ablation (Table 11) cleanly separates training-time mining value from inference-time feature injection.
33	
34	- **Honest reporting of null and conditional results.** The StarCoder dataflow null (p=0.62), the dataflow-vs-embed non-significance (p=0.134 on SWE-bench), and the diminishing returns at scale (Table 10) are reported transparently. Many papers would suppress these findings.
35	
36	- **Mechanistically motivated analysis.** The representation saturation explanation (pos_sim 0.986 vs. 0.799) goes beyond "method X beats method Y" to provide a predictive framework. If validated, the pos_sim diagnostic could be a genuinely useful practitioner tool.
37	
38	- **Clean experimental control.** The comparison holds all variables constant except the negative selection strategy -- same data, same encoder, same LoRA configuration, same training schedule. This is the correct way to study the effect of a single factor.
39	
40	- **SWE-bench Lite end-to-end evaluation.** Including downstream task evaluation, even though the results are positive, adds credibility beyond retrieval-only metrics.
41	
42	---
43	
44	## Weaknesses
45	
46	### Major
47	
48	1. **Generalizability from N=2 encoders is fundamentally limited (Section 5, Discussion).** The paper's central mechanistic claim -- that representation saturation mediates the effectiveness of structural negatives -- rests on exactly two data points: Qwen (saturated, pos_sim=0.986) and StarCoder (healthy, pos_sim=0.799). This is insufficient to establish a functional relationship. The two encoders also differ in pretraining data, pretraining objective, tokenizer, and model family, meaning the observed interaction could be driven by any of these confounds rather than representation geometry per se. The paper characterizes StarCoder2-3B as "encoder-decoder" (Section 3.4), but StarCoder2-3B is decoder-only (autoregressive), making the claimed "architecturally distinct" comparison misleading. At minimum, the paper needs (a) to correct the architectural characterization, and (b) to explicitly acknowledge that the saturation theory is an observation from N=2, not a validated mechanism.
49	
50	2. **Pool size of 50 candidates per query is unrealistically small (Section 3.4, implicitly).** Real-world repositories contain hundreds to thousands of files. A pool of 50 means the retriever is choosing among ~50 files, which inflates absolute recall numbers and may mask differences between strategies that would emerge at realistic pool sizes. The paper does not discuss this design choice or its implications for external validity. At pool=50, even random selection has a 2% baseline chance per candidate, making R@1 in the 0.50+ range less impressive. The RepoBench-R evaluation (Table 5) uses a different pool size but this is not specified.
51	
52	3. **Missing BM25 negative baseline.** The paper's headline narrative -- correcting CoCoHaNeRe's finding that embedding negatives harm code search -- attributes the prior result to BM25-proxy negatives mislabeled as embedding-distance. Yet the paper never runs actual BM25 negatives to demonstrate that the harm is BM25-specific. This is the single most important missing experiment given the framing. Without it, the "correction" is argumentative rather than empirical.
53	
54	4. **SWE-bench Lite results appear inflated relative to project state.** The paper reports +2.3pp (embedding) and +3.3pp (dataflow) resolve-rate gains over random on SWE-bench Lite, with bootstrap CIs excluding zero (Table 4). However, training data from the project's internal decision log (D018, D019, D026, D027) shows that as of the review date, the full M2 runs (9 seeds per strategy per encoder) are still in progress, with only seed 1 partially completed for each encoder. The pilot results (D017) from 1 seed show much smaller effects (+2.0pp Qwen embedding, with dataflow ranking dependent on checkpoint selection criterion). The SWE-bench results reported in the "best" paper variant are substantially stronger than the evidence base supports. If these are projected/simulated results, this must be disclosed.
55	
56	5. **No error bars or CIs on RepoBench-R results (Table 5).** RepoBench-R results are reported as single numbers without seeds, confidence intervals, or significance tests. Given that the reported deltas (e.g., +1.9pp R@1 for embedding on Qwen) are small, these may not be statistically distinguishable from zero. For a paper that emphasizes statistical rigor on the SWE-smith results, the asymmetry in reporting standards is conspicuous.
57	
58	6. **SWE-smith validation results mentioned but not shown.** Section 4 references SWE-smith validation R@1 as the primary evaluation metric, and the main tables (Tables 1-2) report these. But the actual validation set construction, size, and overlap with training data are not described. Given that the project logs show severe overfitting (best checkpoint at step 1000 out of 4242, D026), the validation protocol is critical for interpreting results, yet insufficiently documented.
59	
60	7. **34% structural coverage dilutes the dataflow signal (Section 3.3, implicit).** Only 34.3% of training instances receive dataflow-mined negatives; the remaining 65.7% fall back to alternative selection (presumably embedding or random). The reported +1.5pp dataflow improvement (Table 1, Qwen) averages over all instances including those that received no structural signal. Stratified results (structural-available vs. fallback) are absent. The true per-instance effect of dataflow mining on instances where it actually applies could be much larger (or much smaller) than the reported average. This stratification is essential for interpreting the result.
61	
62	### Minor
63	
64	8. **Table 6 "<50 instances" tier has N=1 repo.** Including a tier with a single repository is misleading and inflates the apparent trend. The correlation r=-0.41 (p=0.08) is heavily influenced by this outlier. The tier should either be removed or its N=1 status should be prominently flagged with appropriate caveats.
65	
66	9. **LoRA rank 16, 3 epochs may be insufficient.** With LoRA rank 16 (a low-rank adapter), the encoder's representational capacity to learn from different negative strategies is limited. Strategy differences might only emerge with fuller fine-tuning. The paper does not discuss whether LoRA's low-rank bottleneck could compress away the differences between strategies. The observed overfitting at step 1000 (1/4 through training) suggests the learning dynamics are dominated by regularization effects, not data effects.
67	
68	10. **Checkpoint selection criterion ambiguity.** The project history (D017) reveals that strategy rankings change depending on whether checkpoints are selected by best validation loss or best R@1. The paper does not specify which criterion is used. Given that this choice can reverse the ordering of strategies (dataflow > embedding by peak R@1 vs. embedding > dataflow by val_loss for Qwen, per D017), this is a material omission.
69	
70	11. **All references render as [?].** The bibliography is broken -- every citation in the compiled paper appears as [?]. This makes it impossible to verify the related work coverage or the CoCoHaNeRe critique. For a paper whose central claim involves correcting a prior work's methodology, unresolvable citations are a serious presentation issue.
71	
72	12. **Number of negatives per query (K) not stated.** The method section defines "select k negatives" but never specifies the value of K used in experiments. This is a basic reproducibility gap.
73	
74	13. **Overfitting patterns not reported.** Project logs show train_loss dropping to 0.04 while val_loss remains at 0.52 (D026), yet the paper does not discuss overfitting or show learning curves. Strategy-specific overfitting patterns could be informative (e.g., does dataflow overfit faster due to fewer unique negatives?).
75	
76	---
77	
78	## Questions for Authors
79	
80	1. **SWE-bench result provenance.** Tables 3-4 report SWE-bench Lite results with bootstrap CIs excluding zero for embedding and dataflow vs. random. Are these from completed 9-seed runs, or projected from pilot data? If the full M2 runs are still in progress, what is the actual evidence base for these numbers?
81	
82	2. **Checkpoint selection criterion.** Which checkpoint is used for the main results -- best by validation loss, or best by R@1? Your project logs (D017) show these criteria produce different strategy rankings. Have you reported both, and if not, why?
83	
84	3. **Stratified dataflow results.** What is the R@1 delta for the ~34% of instances that actually receive dataflow-mined negatives vs. the ~66% that fall back? This decomposition is essential for understanding whether the dataflow signal is strong-but-diluted or weak-throughout.
85	
86	4. **BM25 baseline omission.** The paper's narrative hinges on CoCoHaNeRe using "BM25-proxy negatives mislabeled as embedding-distance." Can you provide specific textual evidence from CoCoHaNeRe supporting this claim? And why not run BM25 negatives as a fourth strategy to close the argument empirically?
87	
88	5. **Pool size sensitivity.** How do strategy differences change as pool size increases from 50 to 200 or 500? If differences shrink at realistic pool sizes, this would substantially weaken the practical relevance of the findings.
89	
90	---
91	
92	## Minor Issues
93	
94	- Section 3.4: StarCoder2-3B is described as "Encoder-decoder" -- it is decoder-only. Correct throughout.
95	- Table 6 (stratified analysis in the best paper) vs. Table 6 (median paper): the two variants report completely different stratification schemes (by file count vs. by instance count), suggesting the analysis is not yet stable.
96	- Abstract line "SWE-bench Lite end-to-end evaluation with a Qwen3.6-27B agent" -- only Qwen retriever checkpoints are used for SWE-bench, not StarCoder. This asymmetry should be acknowledged.
97	- The paper name "StructFuse" implies a fusion system, but the best-performing approach is pure embedding mining without fusion (Table 11 shows fusion slightly degrades performance). The name is misleading.
98	- Hop depth ablation (Table 9): the "best" paper reports clean improvements (2-hop optimal), while the median paper (Table 9) reports differences "within noise range." The discrepancy in framing across tiers suggests cherry-picking of presentation.
99	- Section 3.3 reports "131 SWE-smith repositories" but only "123/131 repos producing valid output" -- the 8 failures are not analyzed.
100	
101	---
102	
103	## Overall Assessment
104	
105	This paper tackles a genuinely important question -- what makes hard negatives work for code retrieval -- with commendable experimental rigor in its design (9 seeds, bootstrap CIs, extensive ablations). The representation saturation insight, if validated on more encoders, could become a useful diagnostic tool for practitioners. However, the paper is undermined by (a) the N=2 encoder limitation that makes the "representation geometry" theory an observation rather than a validated mechanism, (b) missing baselines (BM25) that are critical to the headline narrative, (c) potential discrepancies between reported results and actual experimental maturity, (d) unrealistic pool sizes that limit external validity, and (e) several reporting gaps (no CIs on RepoBench, no stratification by structural coverage, checkpoint criterion unspecified). The paper is above-average in experimental discipline but below the bar for confident acceptance at a top venue in its current form. Addressing the BM25 baseline, the stratified analysis, and the pool size sensitivity would move it toward acceptance.
106	
107	---
108	
109	## Score: 4 / 6 (Weak Accept)
110	
111	The experimental design is sound in principle and the analytical depth is genuine, but critical baselines are missing, the mechanistic theory is underpowered (N=2), and several reporting gaps weaken trust. A revision addressing the major concerns would likely push this to a 5.
112	
113	## Confidence: 4 / 5 (High)
114	
115	I have expertise in contrastive learning, code retrieval, and hard negative mining. I have closely examined the paper's claims against the available evidence, including internal project artifacts. I am confident in my assessment of the methodological strengths and weaknesses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4256af6-e112-4312-a7d8-f1996a65d2b8",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "130f4eda-7f8b-4195-be9d-c42a274f6894",
  "sourceToolAssistantUUID": "b4256af6-e112-4312-a7d8-f1996a65d2b8",
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

_source line 46 · 2026-05-14T08:39:15.251Z_

Now I have comprehensive context. The paper described in the user's prompt matches the "worst" scenario (the negative result paper titled "A Cautionary Tale..."). Let me read the experiment data for the worst scenario to understand the imagined results better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "130f4eda-7f8b-4195-be9d-c42a274f6894",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AEBPEfsQKWMUqQ5Bkz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03e6f7a8-a652-4f4d-9888-7931b84d41b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDLx8KcgMMdMdkeB7uRkp3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12927,
      "cache_read_input_tokens": 70827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12927,
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

_source line 47 · 2026-05-14T08:39:17.612Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LHoA8rXF3GvDTbaYyd6z7N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03e6f7a8-a652-4f4d-9888-7931b84d41b4",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AEBPEfsQKWMUqQ5Bkz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c8345d5-5154-4ea1-9ec6-9c9d8ac6fab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDLx8KcgMMdMdkeB7uRkp3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12927,
      "cache_read_input_tokens": 70827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12927,
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

_source line 48 · 2026-05-14T08:39:17.895Z_

<details><summary>↩ Tool result · `toolu_01LHoA8rXF3GvDTbaYyd6z7N`</summary>

```text
1	[
2	  {
3	    "name": "M2 Full Qwen — 9 seeds × 3 strategies 最终结果",
4	    "description": "Qwen2.5-Coder-3B 在 full-scale 数据上完成全部 27 runs (9 seeds × 3 strategies)。 当前仅 random_s42 完成（R@1=0.553 at step 1000），预测全部完成后的汇总。\n",
5	    "results": {
6	      "random_mean_R1": 0.523,
7	      "random_std_R1": 0.031,
8	      "embedding_distance_mean_R1": 0.521,
9	      "embedding_distance_std_R1": 0.035,
10	      "dataflow_aware_mean_R1": 0.515,
11	      "dataflow_aware_std_R1": 0.038,
12	      "embed_vs_random_delta_pp": -0.2,
13	      "dataflow_vs_random_delta_pp": -0.8,
14	      "best_single_run_R1": 0.553,
15	      "worst_single_run_R1": 0.478,
16	      "cross_seed_R1_std_pp": 3.1,
17	      "best_strategy_by_seed_count": {
18	        "random_wins": 4,
19	        "embedding_wins": 3,
20	        "dataflow_wins": 2
21	      },
22	      "overfitting_step_median": 1000
23	    },
24	    "tables": [
25	      {
26	        "name": "Table 2: Qwen Full-Scale R@1 by Strategy × Seed",
27	        "columns": [
28	          "seed",
29	          "random",
30	          "embedding",
31	          "dataflow"
32	        ],
33	        "rows": [
34	          [
35	            42,
36	            0.553,
37	            0.547,
38	            0.538
39	          ],
40	          [
41	            123,
42	            0.528,
43	            0.534,
44	            0.521
45	          ],
46	          [
47	            456,
48	            0.512,
49	            0.498,
50	            0.503
51	          ],
52	          [
53	            789,
54	            0.541,
55	            0.543,
56	            0.53
57	          ],
58	          [
59	            1024,
60	            0.498,
61	            0.51,
62	            0.496
63	          ],
64	          [
65	            2048,
66	            0.519,
67	            0.522,
68	            0.512
69	          ],
70	          [
71	            3000,
72	            0.505,
73	            0.503,
74	            0.478
75	          ],
76	          [
77	            4096,
78	            0.53,
79	            0.517,
80	            0.525
81	          ],
82	          [
83	            5000,
84	            0.523,
85	            0.515,
86	            0.532
87	          ]
88	        ],
89	        "footer": "Mean±std: random 0.523±0.031, embed 0.521±0.035, dataflow 0.515±0.038"
90	      }
91	    ],
92	    "figures": [],
93	    "analysis": "策略间 delta (<1pp) 远小于种子间方差 (std~3pp)。Pilot 单种子结果是方差范围内的 正常波动。这是 worst 档的核心发现：embedding benefit 是 pilot-scale 的统计幻觉。\n\n\nPilot 的 +2.0pp embed benefit 来自单种子（s42）在小规模数据上的幸运波动。 Full-scale 数据量从 ~2K 增至 ~15K instances，数据分布发生系统性变化： (1) large/xlarge repos 占比从 pilot 的 ~30% 升至 ~60%，这些 repos 的 structural_data_rate 仅 0.31-0.34，embedding negatives 的质量下降； (2) 训练集难度分布更均匀，pilot 中 embedding mining 选出的\"难\"样本在 full-scale 中不再难于 random——因为 random pool 本身已足够难； (3) Qwen 的 pos_sim=0.9855 表征饱和在 full-scale 下更严重，所有策略都面临 margin 过小的问题（embedding margin=0.017, 但 random margin 也仅 0.074）， 导致策略间差异被优化噪声覆盖。9 个种子的 std~3pp 远大于策略间 delta~0.2pp。\n"
94	  },
95	  {
96	    "name": "M2 Full StarCoder — 9 seeds × 3 strategies 最终结果",
97	    "description": "StarCoder2-3B full-scale 27 runs。当前 random_s42 R@1=0.454 at step 1000。\n",
98	    "results": {
99	      "random_mean_R1": 0.443,
100	      "random_std_R1": 0.028,
101	      "embedding_distance_mean_R1": 0.435,
102	      "embedding_distance_std_R1": 0.033,
103	      "dataflow_aware_mean_R1": 0.428,
104	      "dataflow_aware_std_R1": 0.04,
105	      "embed_vs_random_delta_pp": -0.8,
106	      "dataflow_vs_random_delta_pp": -1.5,
107	      "cross_seed_R1_std_pp": 3.4
108	    },
109	    "tables": [
110	      {
111	        "name": "Table 3: StarCoder Full-Scale R@1 by Strategy × Seed",
112	        "columns": [
113	          "seed",
114	          "random",
115	          "embedding",
116	          "dataflow"
117	        ],
118	        "rows": [
119	          [
120	            42,
121	            0.454,
122	            0.448,
123	            0.442
124	          ],
125	          [
126	            123,
127	            0.44,
128	            0.425,
129	            0.418
130	          ],
131	          [
132	            456,
133	            0.462,
134	            0.456,
135	            0.44
136	          ],
137	          [
138	            789,
139	            0.435,
140	            0.43,
141	            0.412
142	          ],
143	          [
144	            1024,
145	            0.448,
146	            0.442,
147	            0.435
148	          ],
149	          [
150	            2048,
151	            0.425,
152	            0.418,
153	            0.398
154	          ],
155	          [
156	            3000,
157	            0.458,
158	            0.45,
159	            0.448
160	          ],
161	          [
162	            4096,
163	            0.43,
164	            0.422,
165	            0.425
166	          ],
167	          [
168	            5000,
169	            0.438,
170	            0.428,
171	            0.43
172	          ]
173	        ],
174	        "footer": "Mean±std: random 0.443±0.028, embed 0.435±0.033, dataflow 0.428±0.040"
175	      }
176	    ],
177	    "figures": [],
178	    "analysis": "StarCoder 上 dataflow 甚至表现最差（-1.5pp vs random），方向与 pilot 一致但 幅度更大。Embedding 也未能帮助。结论：两编码器在 full-scale 下均不支持任何 非 random 策略的优势。\n\n\nStarCoder pilot 已经是 negative conclusion（dataflow R@1=0.487 < random 0.492）。 Full-scale 放大了这个趋势：(1) StarCoder 表征空间 \"healthy\"（pos_sim=0.80）， random negatives 已提供足够梯度（margin=0.194），embedding/dataflow 引入的更难 negatives 反而导致训练不稳定——loss landscape 更尖锐，不同种子落入不同局部最优； (2) dataflow negatives 在 StarCoder 上 margin=0.119 vs embedding 0.067， dataflow 实际上更\"容易\"，但 full-scale 下这个 margin 差异未能转化为性能优势， 因为 StarCoder 的问题不是 negative difficulty 而是编码器容量限制（3B 参数 + LoRA rank 受限时，更难 negatives 导致梯度冲突）。Cross-seed std 3.4pp 进一步 确认策略差异 (<1.5pp) 不可靠。\n"
179	  },
180	  {
181	    "name": "M3a SWE-bench Lite End-to-End Evaluation",
182	    "description": "SWE-bench Lite (300 instances) end-to-end evaluation，使用 Qwen3.6-27B agent， 对比 3 个 strategy 的 best checkpoint 作为 retriever。\n",
183	    "results": {
184	      "random_resolve_rate": 0.187,
185	      "embedding_resolve_rate": 0.19,
186	      "dataflow_resolve_rate": 0.183,
187	      "embed_vs_random_delta_pp": 0.3,
188	      "dataflow_vs_random_delta_pp": -0.4,
189	      "swebench_resolve_delta_pp": 0.3,
190	      "retrieval_R1_on_swebench": {
191	        "random": 0.42,
192	        "embedding": 0.43,
193	        "dataflow": 0.41
194	      },
195	      "n_instances_evaluated": 287,
196	      "n_instances_failed": 13
197	    },
198	    "tables": [
199	      {
200	        "name": "Table 5: SWE-bench Lite Resolve Rates",
201	        "columns": [
202	          "strategy",
203	          "resolve_rate",
204	          "retrieval_R1",
205	          "n_resolved",
206	          "n_total"
207	        ],
208	        "rows": [
209	          [
210	            "random",
211	            0.187,
212	            0.42,
213	            54,
214	            287
215	          ],
216	          [
217	            "embedding_distance",
218	            0.19,
219	            0.43,
220	            55,
221	            287
222	          ],
223	          [
224	            "dataflow_aware",
225	            0.183,
226	            0.41,
227	            53,
228	            287
229	          ]
230	        ],
231	        "footer": "Best delta: +0.3pp (embed vs random), not significant (p=0.89 McNemar)"
232	      }
233	    ],
234	    "figures": [],
235	    "analysis": "SWE-bench 结果不仅不支持 embedding/dataflow 策略的优势，甚至所有策略的 resolve rate 都低于 SweRank baseline。这暗示 full-scale 训练可能引入了某种 regression（数据分布 偏移？）。需排查训练数据与 SWE-bench 的 domain overlap。\n\n\nSWE-bench Lite 的 resolve rate 由 retrieval → agent pipeline 多阶段组成， retriever 差异被下游 agent 的 stochasticity 大幅稀释。即使 retrieval R@1 差异 存在 1pp，经过 agent 的 code generation + apply patch + test 环节后，resolve rate 差异被压缩到 <0.5pp。具体原因： (1) SWE-bench 中很多 \"easy\" instances（~30%）任何 retriever 都能找到正确文件， 策略差异为零； (2) \"hard\" instances（~25%）任何 retriever 都找不到，agent 依赖推理能力而非检索； (3) 只有 ~45% 的中间难度 instances 中 retrieval 策略可能产生差异，但 agent 的 code generation variance（温度、context window 限制）进一步模糊了信号； (4) 300 instances 中有效差异空间 ~135 个，0.3pp delta 对应仅 ~1 个额外解决的 instance，完全在噪声范围内。此外 full-scale retriever 本身策略间差异已消失， SWE-bench 只是进一步确认。\n"
236	  },
237	  {
238	    "name": "M3b RepoBench-R Cross-File Retrieval",
239	    "description": "RepoBench-R 作为第二基准，retrieval-only 评估，无 LLM agent。\n",
240	    "results": {
241	      "random_R1": 0.312,
242	      "embedding_R1": 0.308,
243	      "dataflow_R1": 0.295,
244	      "embed_vs_random_delta_pp": -0.4,
245	      "dataflow_vs_random_delta_pp": -1.7,
246	      "random_R5": 0.58,
247	      "embedding_R5": 0.57,
248	      "dataflow_R5": 0.56,
249	      "pretrained_baseline_R1": 0.285
250	    },
251	    "tables": [
252	      {
253	        "name": "Table 6: RepoBench-R Results (Qwen encoder)",
254	        "columns": [
255	          "strategy",
256	          "R@1",
257	          "R@5",
258	          "R@10",
259	          "MRR"
260	        ],
261	        "rows": [
262	          [
263	            "pretrained",
264	            0.285,
265	            0.52,
266	            0.68,
267	            0.401
268	          ],
269	          [
270	            "random",
271	            0.312,
272	            0.58,
273	            0.73,
274	            0.438
275	          ],
276	          [
277	            "embedding_distance",
278	            0.308,
279	            0.57,
280	            0.72,
281	            0.432
282	          ],
283	          [
284	            "dataflow_aware",
285	            0.295,
286	            0.56,
287	            0.71,
288	            0.418
289	          ]
290	        ]
291	      }
292	    ],
293	    "figures": [],
294	    "analysis": "RepoBench-R 进一步证明策略差异不稳定且 domain-dependent。Dataflow 策略的负迁移 尤其严重（-1.7pp），支持 negative result 叙事中 \"structural negatives 不 generalize\" 的论点。\n\n\nRepoBench-R 是 cross-file completion 任务，与 SWE-smith 的 bug localization 分布差异更大。Full-scale 训练在 SWE-smith 上 overfit 的模型在 RepoBench 上 表现出不同的行为模式： (1) 所有策略都优于 pretrained baseline（+2-3pp），说明 contrastive fine-tuning 本身有效，但策略间差异在 domain shift 下被进一步压缩； (2) Dataflow negatives 在 RepoBench 上表现最差，因为 SWE-smith 的 dataflow 结构 （bug-fix oriented）与 RepoBench 的 completion-oriented 代码结构不匹配—— SWE-smith 中 disconnected = irrelevant 的假设在 completion 场景中不成立； (3) Embedding negatives 略低于 random 是因为 full-scale embedding mining 选出的 negatives 过度 fit 到 SWE-smith 的相似性分布，domain shift 后反而损害泛化。\n"
295	  },
296	  {
297	    "name": "Embedding vs Random Deep Stratified Analysis",
298	    "description": "按 repo size、code complexity、neg_difficulty 分层分析 embedding negatives 的效果。\n",
299	    "results": {
300	      "by_repo_size": {
301	        "small_lt50": {
302	          "random_R1": 0.61,
303	          "embedding_R1": 0.59,
304	          "delta_pp": -2.0
305	        },
306	        "medium_50_200": {
307	          "random_R1": 0.54,
308	          "embedding_R1": 0.55,
309	          "delta_pp": 1.0
310	        },
311	        "large_200_500": {
312	          "random_R1": 0.51,
313	          "embedding_R1": 0.5,
314	          "delta_pp": -1.0
315	        },
316	        "xlarge_500plus": {
317	          "random_R1": 0.48,
318	          "embedding_R1": 0.48,
319	          "delta_pp": 0.0
320	        }
321	      },
322	      "by_neg_difficulty_quartile": {
323	        "easy_q1_delta_pp": 0.5,
324	        "medium_q2_delta_pp": -0.3,
325	        "hard_q3_delta_pp": -1.2,
326	        "hardest_q4_delta_pp": -2.1
327	      },
328	      "correlation_margin_vs_benefit": -0.15,
329	      "correlation_repo_size_vs_benefit": -0.08
330	    },
331	    "tables": [
332	      {
333	        "name": "Table 7: Embedding Benefit by Repo Size",
334	        "columns": [
335	          "repo_tier",
336	          "n_instances",
337	          "random_R1",
338	          "embed_R1",
339	          "delta_pp"
340	        ],
341	        "rows": [
342	          [
343	            "small (<50)",
344	            500,
345	            0.61,
346	            0.59,
347	            -2.0
348	          ],
349	          [
350	            "medium (50-200)",
351	            4096,
352	            0.54,
353	            0.55,
354	            1.0
355	          ],
356	          [
357	            "large (200-500)",
358	            13628,
359	            0.51,
360	            0.5,
361	            -1.0
362	          ],
363	          [
364	            "xlarge (500+)",
365	            25949,
366	            0.48,
367	            0.48,
368	            0.0
369	          ]
370	        ]
371	      }
372	    ],
373	    "figures": [],
374	    "analysis": "核心发现：embedding benefit 是 repo size 和 negative difficulty 的函数， 在 pilot 的 data composition 下恰好为正，在 full-scale 的 data composition 下 恰好为零或负。这不是方法失败，而是 pilot evaluation bias——小规模评估 over-represents 中等 repo，恰好是 embedding mining 的 sweet spot。\n\n\n分层分析揭示 embedding benefit 不是\"消失\"而是\"抵消\"——在某些 strata 正向、 其他 strata 负向，总和接近零： (1) Small repos 上 embedding mining 实际有害（-2pp），因为小 repo 的 file pool 只有 ~10-50 个文件，embedding mining 选出的 \"nearest\" negative 往往就是 gold file 的近邻（同一个 module），形成 false hard negatives 损害训练信号； (2) Medium repos 上 embedding 略有优势（+1pp），因为 pool 足够大使 mining 选到 真正的 hard negatives，且难度梯度合理； (3) Large/xlarge repos 上差异消失，因为 random sampling 在大 pool 中已经有合理 概率采到 moderately hard negatives，embedding mining 的额外选择性优势被稀释； (4) 按 neg_difficulty 分层更清晰：最难 quartile（margin 最小）中 embedding 有害 （-2.1pp），因为过难的 negatives 导致梯度冲突/训练不稳定。这解释了为什么 full-scale（更多 large repos → 更多 hard quartile instances）中 benefit 消失。\n"
375	  },
376	  {
377	    "name": "Hop-Distance Call-Graph Bounding Ablation",
378	    "description": "1-hop vs 2-hop vs 3-hop call-graph bounding 对 dataflow negative 质量的影响。\n",
379	    "results": {
380	      "hop_1": {
381	        "connected_pct": 0.12,
382	        "disconnected_neg_margin": 0.035,
383	        "training_R1": 0.513
384	      },
385	      "hop_2": {
386	        "connected_pct": 0.34,
387	        "disconnected_neg_margin": 0.029,
388	        "training_R1": 0.515
389	      },
390	      "hop_3": {
391	        "connected_pct": 0.58,
392	        "disconnected_neg_margin": 0.022,
393	        "training_R1": 0.51
394	      },
395	      "delta_1hop_vs_2hop_pp": -0.2,
396	      "delta_2hop_vs_3hop_pp": 0.5,
397	      "all_vs_random_best_pp": -0.8
398	    },
399	    "tables": [
400	      {
401	        "name": "Table 8: Hop-Distance Ablation (Qwen, seed 42)",
402	        "columns": [
403	          "hops",
404	          "connected_pct",
405	          "disconn_margin",
406	          "R@1",
407	          "vs_random_pp"
408	        ],
409	        "rows": [
410	          [
411	            1,
412	            0.12,
413	            0.035,
414	            0.513,
415	            -1.0
416	          ],
417	          [
418	            2,
419	            0.34,
420	            0.029,
421	            0.515,
422	            -0.8
423	          ],
424	          [
425	            3,
426	            0.58,
427	            0.022,
428	            0.51,
429	            -1.3
430	          ],
431	          [
432	            "random",
433	            "-",
434	            "-",
435	            0.523,
436	            0.0
437	          ]
438	        ]
439	      }
440	    ],
441	    "figures": [],
442	    "analysis": "Hop distance 是 second-order 参数——当 first-order 效应（结构断开作为 hardness proxy） 本身无效时，调节粒度无法改变结论。\n\n\nHop distance 改变 connected/disconnected 的划分粒度，但在 worst 档下无法拯救 dataflow 策略： (1) 1-hop 过于严格（仅 12% connected），大量 gold-relevant files 被错误标记为 disconnected，产生大量 false hard negatives → 训练信号受损； (2) 2-hop（当前设置）是 pilot 中的最优，但 full-scale 下效果与 random 无异； (3) 3-hop 过于宽泛（58% connected），disconnected pool 缩小到几乎只剩 truly unrelated files，这些 negatives 太容易（margin=0.022），训练信号退化为 接近 random sampling 的效果但 pool 更小； (4) 三种 hop 设置的 R@1 范围仅 0.510-0.515，都低于 random baseline 0.523， 说明 structural bounding 本身在 full-scale 下不是一个有效的 negative selection 维度——问题出在 \"结构断开≠语义无关\" 这个核心假设。\n"
443	  },
444	  {
445	    "name": "Training Data Size Scaling Ablation",
446	    "description": "1K vs 3K vs 5K（当前 full-scale ~15K instances 中子采样）对策略差异的影响。\n",
447	    "results": {
448	      "size_1k": {
449	        "random_R1": 0.505,
450	        "embedding_R1": 0.518,
451	        "dataflow_R1": 0.512,
452	        "embed_delta_pp": 1.3
453	      },
454	      "size_3k": {
455	        "random_R1": 0.515,
456	        "embedding_R1": 0.52,
457	        "dataflow_R1": 0.513,
458	        "embed_delta_pp": 0.5
459	      },
460	      "size_5k": {
461	        "random_R1": 0.52,
462	        "embedding_R1": 0.521,
463	        "dataflow_R1": 0.516,
464	        "embed_delta_pp": 0.1
465	      },
466	      "size_15k_full": {
467	        "random_R1": 0.523,
468	        "embedding_R1": 0.521,
469	        "dataflow_R1": 0.515,
470	        "embed_delta_pp": -0.2
471	      },
472	      "embed_benefit_slope_per_1k": -0.11
473	    },
474	    "tables": [
475	      {
476	        "name": "Table 9: Data Size × Strategy Interaction",
477	        "columns": [
478	          "data_size",
479	          "random_R1",
480	          "embed_R1",
481	          "dataflow_R1",
482	          "embed_delta"
483	        ],
484	        "rows": [
485	          [
486	            "1K",
487	            0.505,
488	            0.518,
489	            0.512,
490	            1.3
491	          ],
492	          [
493	            "3K",
494	            0.515,
495	            0.52,
496	            0.513,
497	            0.5
498	          ],
499	          [
500	            "5K",
501	            0.52,
502	            0.521,
503	            0.516,
504	            0.1
505	          ],
506	          [
507	            "15K (full)",
508	            0.523,
509	            0.521,
510	            0.515,
511	            -0.2
512	          ]
513	        ]
514	      }
515	    ],
516	    "figures": [],
517	    "analysis": "这张图是论文的核心 figure——直观展示 \"hard negative mining 的收益随数据规模递减 并最终消失\" 的 scaling law。对 negative result paper 的贡献极大，因为它提供了 可预测的量化关系，而非仅仅 \"结果没复现\" 的定性陈述。\n\n\n这个 ablation 精确解释了 pilot-to-full-scale discrepancy 的机制： (1) 1K instances（≈pilot 规模）复现了 pilot 的 embedding benefit（+1.3pp）， 确认 pilot 结果本身没有 bug——在小规模下 embedding mining 确实有效； (2) 随数据量增长，benefit 单调递减（斜率≈-0.11pp per 1K instances）； (3) 原因是 data scaling 改变了有效 negative difficulty 分布——1K 时 random pool 中真正 hard 的 negatives 极少（小 pool → 大多是 easy negatives），embedding mining 通过选择 nearest neighbors 提供了必要的 difficulty gradient。但随着 pool 增大， random sampling 的\"命中率\"自然上升，embedding mining 的增量价值趋零； (4) 5K 处 delta 已缩至 0.1pp（不显著），15K 处反转为 -0.2pp； (5) 这是 negative result paper 的关键证据：small-scale evaluation 系统性高估 hard negative mining 的收益，因为 scale 本身就是一种隐性的 negative difficulty 调节器。\n"
518	  },
519	  {
520	    "name": "Fusion Head Architecture Ablation",
521	    "description": "Embedding-only vs structural-features-only vs combined fusion head， 测试结构特征是否通过不同 fusion 方式提供价值。\n",
522	    "results": {
523	      "embedding_only_R1": 0.523,
524	      "structural_only_R1": 0.385,
525	      "combined_R1": 0.519,
526	      "embed_only_vs_combined_pp": 0.4
527	    },
528	    "tables": [
529	      {
530	        "name": "Table 10: Fusion Head Ablation (Qwen, seed 42)",
531	        "columns": [
532	          "head_type",
533	          "R@1",
534	          "R@5",
535	          "val_loss"
536	        ],
537	        "rows": [
538	          [
539	            "embedding_only",
540	            0.523,
541	            0.955,
542	            0.486
543	          ],
544	          [
545	            "structural_features",
546	            0.385,
547	            0.78,
548	            0.812
549	          ],
550	          [
551	            "combined",
552	            0.519,
553	            0.95,
554	            0.495
555	          ]
556	        ]
557	      }
558	    ],
559	    "figures": [],
560	    "analysis": "结构特征作为独立信号维度不足，作为辅助信号有害。这排除了 \"也许 dataflow 信号有用 但 negative mining 不是正确的注入方式\" 的替代假设。\n\n\nFusion head 架构无法从无到有创造 structural signal 的价值： (1) Embedding-only head 与 random strategy 性能相当（0.523），因为 LoRA fine-tuned embeddings 本身已捕获了足够的 code similarity 信息； (2) Structural-features-only head 大幅下降至 0.385——结构特征（is_connected, dataflow_distance, call_graph_hops）单独不足以判断 relevance，因为大部分 file pairs 的结构特征是 sparse 的（structural_data_rate=0.34，66% pairs 无结构信息）； (3) Combined head 反而略低于 embedding-only（-0.4pp），因为 noisy structural features 干扰了 embedding signal——当 66% instances 的结构特征为 null/zero 时， fusion layer 必须学会忽略结构维度，但 LoRA 的低秩约束使这个 \"ignore\" 信号 不够干净； (4) 这进一步支持了 structural signal 在 full-scale 下无效的结论。\n"
561	  },
562	  {
563	    "name": "Dataflow-Distance Weighted vs Binary Negatives",
564	    "description": "连续 dataflow distance 加权 vs 二元 connected/disconnected 的 negative selection。\n",
565	    "results": {
566	      "binary_disconnected_R1": 0.515,
567	      "distance_weighted_R1": 0.517,
568	      "delta_pp": 0.2,
569	      "vs_random_pp": -0.6
570	    },
571	    "tables": [],
572	    "figures": [],
573	    "analysis": "细化无效信号的粒度不改善性能。这是对 \"也许我们只需要更好的结构度量\" 假设的反驳。\n\n\nDistance weighting 是对 binary disconnected 的细化——用 shortest dataflow path length 作为权重偏好更远的（更 disconnected）negatives。但在 worst 档下改进微乎其微 （+0.2pp vs binary），因为： (1) 核心问题不是 negative selection 的粒度，而是 structural disconnection 作为 hardness proxy 本身的有效性——weighted 版本在一个无效信号上做更精细的选择， 不改变根本问题； (2) 距离信息 noisy——CodeQL 的 dataflow path 是 approximation，real shortest path 与 estimated path 的相关性仅 ~0.6（由于 scope bounding），weighting 基于 noisy distance 引入额外噪声； (3) 两个版本都低于 random baseline（-0.6pp），进一步确认结构信号无效。\n"
574	  },
575	  {
576	    "name": "Failure Analysis: 50 SweRank/BM25 Failures",
577	    "description": "对 50 个 SweRank/BM25 检索失败的 SWE-bench instances 进行手动分类， 分析 dataflow 信号是否能帮助。\n",
578	    "results": {
579	      "n_analyzed": 50,
580	      "categories": {
581	        "cross_file_dependency": 18,
582	        "naming_ambiguity": 12,
583	        "scattered_changes": 9,
584	        "test_file_confusion": 7,
585	        "other": 4
586	      },
587	      "dataflow_could_help": 6,
588	      "dataflow_actually_helped": 2,
589	      "dataflow_hurt": 3,
590	      "dataflow_neutral": 39
591	    },
592	    "tables": [
593	      {
594	        "name": "Table 11: Failure Category Analysis",
595	        "columns": [
596	          "category",
597	          "count",
598	          "df_could_help",
599	          "df_actually_helped",
600	          "df_hurt"
601	        ],
602	        "rows": [
603	          [
604	            "cross_file_dep",
605	            18,
606	            4,
607	            1,
608	            1
609	          ],
610	          [
611	            "naming_ambiguity",
612	            12,
613	            0,
614	            0,
615	            1
616	          ],
617	          [
618	            "scattered_changes",
619	            9,
620	            2,
621	            1,
622	            1
623	          ],
624	          [
625	            "test_confusion",
626	            7,
627	            0,
628	            0,
629	            0
630	          ],
631	          [
632	            "other",
633	            4,
634	            0,
635	            0,
636	            0
637	          ],
638	          [
639	            "total",
640	            50,
641	            6,
642	            2,
643	            3
644	          ]
645	        ]
646	      }
647	    ],
648	    "figures": [],
649	    "analysis": "Dataflow 的理论覆盖面（12% = 6/50 可能帮助）和实际有效率（4% = 2/50 实际帮助） 远低于立论所需。对 negative result paper 的贡献：提供 error taxonomy 证明 structural signal 的适用范围窄于预期。\n\n\n手动分析 50 个失败案例后发现 dataflow 信号能帮助的场景远少于预期： (1) Cross-file dependency（18 cases）是 dataflow 理论上的 sweet spot，但实际 仅 4/18 有可用的 CodeQL dataflow 路径——其余 14 个的 dependency 是通过 import、 type reference 或 configuration 而非 data flow，CodeQL 的 inter-procedural analysis 未覆盖这些； (2) Naming ambiguity（12 cases）中 dataflow 无法帮助——问题是同名函数/类在 不同 module 中，structural 和 textual signal 同时失效； (3) 6 个理论上 dataflow 可帮助的 cases 中，仅 2 个实际在 dataflow-trained model 中被正确检索——另 4 个因训练不稳定/过拟合而性能退化抵消了理论优势； (4) 3 个 cases 中 dataflow 实际有害——将结构上相关但 gold set 外的文件排入 top-1，挤掉了正确答案。\n"
650	  },
651	  {
652	    "name": "Qualitative Examples: Structural Negatives Impact",
653	    "description": "挑选 5-10 个 structural negatives 改变检索结果的定性案例。\n",
654	    "results": {
655	      "positive_examples_found": 3,
656	      "negative_examples_found": 4,
657	      "neutral_examples": 3,
658	      "net_narrative": "negative"
659	    },
660	    "tables": [],
661	    "figures": [],
662	    "analysis": "定性证据反而支持 negative result 叙事。典型 failure mode（structural proximity ≠ task relevance）是重要的methodological insight。\n\n\n在 worst 档下，能找到的正面案例数量与负面案例相当甚至更少： (1) 3 个正面案例：dataflow training 将结构相关文件从 top-5 提升到 top-1， 但这些改善也出现在 embedding strategy 的部分种子中，不能归因于 dataflow； (2) 4 个负面案例：dataflow training 将结构上相近但 gold set 外的文件推高排名， 挤掉了正确答案。典型模式：文件 A 通过 data flow 连接到 gold file B， dataflow 策略错误地将 A 排在 B 之前； (3) 3 个中性案例：dataflow 改变了 top-10 内的排序但不影响 top-1/top-5； (4) 定性分析 net negative，无法支撑 paper 中的正面叙事。对 negative result paper 可用——展示 structural negatives 的 failure modes。\n"
663	  },
664	  {
665	    "name": "Temperature Ablation: τ ∈ {0.05, 0.1, 0.2}",
666	    "description": "三个温度 × 三个策略，测试 embedding benefit 是否是温度 regime-specific。\n",
667	    "results": {
668	      "tau_005": {
669	        "random_R1": 0.498,
670	        "embedding_R1": 0.485,
671	        "dataflow_R1": 0.475,
672	        "embed_delta_pp": -1.3
673	      },
674	      "tau_010": {
675	        "random_R1": 0.523,
676	        "embedding_R1": 0.521,
677	        "dataflow_R1": 0.515,
678	        "embed_delta_pp": -0.2
679	      },
680	      "tau_020": {
681	        "random_R1": 0.51,
682	        "embedding_R1": 0.508,
683	        "dataflow_R1": 0.502,
684	        "embed_delta_pp": -0.2
685	      },
686	      "best_overall_tau": 0.1,
687	      "any_tau_with_significant_embed_benefit": false
688	    },
689	    "tables": [
690	      {
691	        "name": "Table 12: Temperature × Strategy Interaction (Qwen, mean of 3 seeds)",
692	        "columns": [
693	          "tau",
694	          "random",
695	          "embedding",
696	          "dataflow",
697	          "best_strategy"
698	        ],
699	        "rows": [
700	          [
701	            0.05,
702	            0.498,
703	            0.485,
704	            0.475,
705	            "random"
706	          ],
707	          [
708	            0.1,
709	            0.523,
710	            0.521,
711	            0.515,
712	            "random"
713	          ],
714	          [
715	            0.2,
716	            0.51,
717	            0.508,
718	            0.502,
719	            "random"
720	          ]
721	        ]
722	      }
723	    ],
724	    "figures": [],
725	    "analysis": "Temperature 不是 confound——在所有温度 regime 下，random 策略都是最优或并列最优。 排除了 \"pilot 的 embedding benefit 是因为 τ=0.1 恰好适合 embedding mining\" 的假设。\n\n\n温度调节改变 contrastive loss 对 similarity margin 的敏感度，但无法拯救无效的 mining strategy： (1) τ=0.05 使 loss 对 margin 极其敏感——在 Qwen 的 saturated space （pos_sim=0.9855, embedding neg_sim=0.9685, margin=0.017）中，如此小的 margin 在 τ=0.05 下产生几乎相同的 loss 贡献，embedding negatives 等于 random。 但更严重的是 τ=0.05 放大了个别 extreme negative 的梯度，导致训练不稳定， 所有策略性能下降（尤其 dataflow，因为 dataflow negatives 的 margin distribution 更 heavy-tailed）； (2) τ=0.10（当前默认）是最优温度，但策略间无显著差异； (3) τ=0.20 使 loss 对 margin 不够敏感——hard negatives 的额外 difficulty 被 soft temperature 压缩，embedding/dataflow mining 的理论优势被进一步稀释； (4) 没有任何温度 regime 能让 embedding benefit 达到统计显著，因为 full-scale 下策略间的 \"信号\" 本身不存在（是 pilot 的噪声），温度只是调节 loss landscape 的曲率，不能创造信号。\n"
726	  },
727	  {
728	    "name": "Dynamic Embedding Mining vs Static",
729	    "description": "Per-epoch 重新 mining embedding negatives vs 一次性从 pretrained model mining。\n",
730	    "results": {
731	      "static_embedding_R1": 0.521,
732	      "dynamic_epoch1_R1": 0.521,
733	      "dynamic_epoch2_R1": 0.519,
734	      "dynamic_epoch3_R1": 0.515,
735	      "dynamic_mean_R1": 0.518,
736	      "dynamic_vs_static_pp": -0.3,
737	      "dynamic_vs_random_pp": -0.5
738	    },
739	    "tables": [
740	      {
741	        "name": "Table 13: Static vs Dynamic Mining (Qwen, seed 42)",
742	        "columns": [
743	          "method",
744	          "epoch1_R1",
745	          "epoch2_R1",
746	          "epoch3_R1",
747	          "best_R1"
748	        ],
749	        "rows": [
750	          [
751	            "static",
752	            0.54,
753	            0.53,
754	            0.512,
755	            0.54
756	          ],
757	          [
758	            "dynamic",
759	            0.54,
760	            0.525,
761	            0.505,
762	            0.54
763	          ],
764	          [
765	            "random",
766	            0.535,
767	            0.528,
768	            0.51,
769	            0.535
770	          ]
771	        ]
772	      }
773	    ],
774	    "figures": [],
775	    "analysis": "Dynamic mining 排除了 \"staleness\" 作为 embedding mining 失效的解释。 Mining 策略本身在大规模下不提供增量价值。\n\n\nDynamic mining 理论上解决 \"pretrained embedding 与 fine-tuned embedding 偏移导致 negatives 过时\" 的问题。但在 worst 档下非但不改善，反而略有下降： (1) Epoch 1 dynamic ≈ static（因为 epoch 1 开始时 model 就是 pretrained， mining 结果相同）； (2) Epoch 2-3 的 re-mining 产生了 curriculum shift 效应——随着 model 改善， nearest neighbors 改变，新选出的 negatives 更难但也更 noisy（因为 fine-tuned model 的 embedding space 在 LoRA 下只部分更新，re-mining 的 nearest neighbors 可能是 LoRA 的 artifacts 而非真正的 hard negatives）； (3) Re-mining 引入的计算开销显著（每 epoch 需重新编码全部 ~44K instances， ~2h per re-mining），cost-benefit 明显不值得； (4) Dynamic mining 的失败进一步证明问题不是 \"mining 过时\" 而是 \"mining 本身 在大规模下无效\"。\n"
776	  },
777	  {
778	    "name": "Bootstrap CI for SWE-bench Resolve Rates",
779	    "description": "10,000 bootstrap resamples 计算 SWE-bench resolve rate 的 95% CI。\n",
780	    "results": {
781	      "random_resolve_rate": 0.187,
782	      "random_95ci": [
783	        0.143,
784	        0.232
785	      ],
786	      "embedding_resolve_rate": 0.19,
787	      "embedding_95ci": [
788	        0.147,
789	        0.235
790	      ],
791	      "dataflow_resolve_rate": 0.183,
792	      "dataflow_95ci": [
793	        0.14,
794	        0.228
795	      ],
796	      "embed_vs_random_delta": 0.003,
797	      "embed_vs_random_delta_95ci": [
798	        -0.038,
799	        0.045
800	      ],
801	      "embed_benefit_bootstrap_p": 0.78,
802	      "dataflow_vs_random_delta": -0.004,
803	      "dataflow_vs_random_delta_95ci": [
804	        -0.048,
805	        0.038
806	      ]
807	    },
808	    "tables": [
809	      {
810	        "name": "Table 14: SWE-bench Bootstrap Statistics",
811	        "columns": [
812	          "comparison",
813	          "delta_pp",
814	          "95%_CI",
815	          "p_value",
816	          "interpretation"
817	        ],
818	        "rows": [
819	          [
820	            "embed vs random",
821	            0.3,
822	            "[-3.8, +4.5]",
823	            0.78,
824	            "not significant"
825	          ],
826	          [
827	            "dataflow vs random",
828	            -0.4,
829	            "[-4.8, +3.8]",
830	            0.68,
831	            "not significant"
832	          ],
833	          [
834	            "dataflow vs embed",
835	            -0.7,
836	            "[-5.2, +3.5]",
837	            0.55,
838	            "not significant"
839	          ]
840	        ]
841	      }
842	    ],
843	    "figures": [],
844	    "analysis": "统计分析确认 SWE-bench 差异不显著。Power analysis 证明 SWE-bench Lite 的 n=300 本质上无法 detect <5pp 的 retriever 差异——这本身是一个 methodological contribution for the negative result paper。\n\n\nBootstrap CI 极宽（±4-5pp），因为 SWE-bench Lite 仅 300 instances， 有效样本更少（~287 after failures）： (1) 单策略 CI 宽度 ~9pp（±4.5pp），策略间 delta（0.3pp）远小于 CI 宽度； (2) Paired delta CI [-3.8pp, +4.5pp] 包含零且两侧几乎对称——没有任何方向性信号； (3) Bootstrap p=0.78 远高于任何合理显著性阈值，确认 delta 不显著； (4) 即使使用 pilot 阶段的 +2.0pp delta，在 n=287 下的 power analysis 显示 需要 ~2000 instances 才能在 α=0.05 下 detect 2pp 的差异——SWE-bench Lite 本质上 underpowered for 这个效应量； (5) 对 negative result paper 有力：不仅 point estimate 接近零，统计检验也 确认无法拒绝零假设。\n"
845	  },
846	  {
847	    "name": "Inference-Time Graph Method Discussion",
848	    "description": "与 CodexGraph, LocAgent 等 inference-time graph 方法的定性比较讨论。\n",
849	    "results": {
850	      "locagent_reported_resolve_rate": 0.262,
851	      "our_best_resolve_rate": 0.19,
852	      "codexgraph_reported_R1": 0.48,
853	      "our_best_R1": 0.523,
854	      "complementarity_evidence": "none"
855	    },
856	    "tables": [
857	      {
858	        "name": "Table 15: Training-Time vs Inference-Time Structure Utilization",
859	        "columns": [
860	          "method",
861	          "structure_usage",
862	          "SWE_bench_resolve",
863	          "retrieval_R1"
864	        ],
865	        "rows": [
866	          [
867	            "ours (random)",
868	            "training negatives",
869	            0.187,
870	            0.523
871	          ],
872	          [
873	            "ours (dataflow)",
874	            "training negatives",
875	            0.183,
876	            0.515
877	          ],
878	          [
879	            "LocAgent",
880	            "inference navigation",
881	            0.262,
882	            "-"
883	          ],
884	          [
885	            "CodexGraph",
886	            "inference navigation",
887	            "-",
888	            "0.48*"
889	          ]
890	        ],
891	        "footer": "*CodexGraph R@1 on different benchmark, not directly comparable"
892	      }
893	    ],
894	    "figures": [],
895	    "analysis": "这个比较将 negative result 升华为 positive insight：结构信息的价值在于 query-adaptive navigation，而非 static negative mining。这为 related work section 提供了 coherent narrative。\n\n\nInference-time graph methods 在 SWE-bench 上的表现远优于我们的 training-time structural mining approach： (1) LocAgent 报告 26.2% resolve rate（vs 我们的 ~19%），差距主要来自 LocAgent 使用 runtime graph navigation（动态探索 call graph at inference）， 而我们的 structural signal 仅用于 static training-time negative selection—— 本质是两种完全不同的信息利用方式； (2) 在 worst 档下我们无法证明 \"training-time structural mining 与 inference-time graph navigation 互补\"——因为 training-time mining 本身无效，所以无互补可言； (3) 这个比较反而支持 inference-time graph methods 是更有效的结构信息利用范式—— structural signal 的价值在 navigation（决定下一步看什么文件）而非 mining （决定训练用什么负样本）； (4) 对 negative result paper 的 framing 有帮助：可以用 inference-time methods 的成功来反衬 training-time mining 的失败，论证 \"structural information 有价值 但应在 inference time 使用\" 这一 insight。\n"
896	  },
897	  {
898	    "name": "Data Pipeline Distribution Audit",
899	    "description": "排查 full-scale 训练数据与 pilot 数据的分布差异，确认 negative result 是真实的 而非工程错误。\n",
900	    "results": {
901	      "pilot_vs_full_repo_overlap": 0.85,
902	      "pilot_mean_files_per_repo": 45,
903	      "full_mean_files_per_repo": 185,
904	      "pilot_difficulty_distribution_ks_p": 0.003,
905	      "pilot_structural_rate": 0.58,
906	      "full_structural_rate": 0.34,
907	      "data_bug_found": false,
908	      "distribution_shift_confirmed": true,
909	      "shift_severity": "moderate"
910	    },
911	    "tables": [
912	      {
913	        "name": "Table A1: Pilot vs Full-Scale Data Distribution",
914	        "columns": [
915	          "metric",
916	          "pilot",
917	          "full_scale",
918	          "p_value"
919	        ],
920	        "rows": [
921	          [
922	            "n_instances",
923	            "~2000",
924	            15133,
925	            "-"
926	          ],
927	          [
928	            "n_repos",
929	            8,
930	            123,
931	            "-"
932	          ],
933	          [
934	            "structural_rate",
935	            0.58,
936	            0.34,
937	            "<0.001"
938	          ],
939	          [
940	            "mean_files_per_repo",
941	            45,
942	            185,
943	            "<0.001"
944	          ],
945	          [
946	            "median_neg_margin_embed",
947	            0.025,
948	            0.017,
949	            0.003
950	          ],
951	          [
952	            "pct_large_repos",
953	            0.3,
954	            0.56,
955	            "<0.001"
956	          ]
957	        ]
958	      }
959	    ],
960	    "figures": [],
961	    "analysis": "Distribution audit 确认 negative result 是真实的——pilot selection bias 导致了 不可复现的初始结论。这个 audit 是 negative result paper 的必要组成部分， 否则 reviewer 会质疑 \"是不是你代码有 bug\"。\n\nFull-scale 数据没有 pipeline bug，但存在明确的分布偏移： (1) Pilot 用了 ~2K instances 从 8-10 个 medium-size repos，structural_data_rate=0.58 （大部分 instances 有结构信息）。Full-scale 15K instances 来自 123 repos， dominated by large/xlarge repos（69/123），structural_data_rate=0.34—— 几乎一半 instances 在 full-scale 中没有结构信息，dataflow strategy 只能 fallback 到 random selection； (2) KS test 确认难度分布显著不同（p=0.003）——full-scale 中 easy instances （大 repo 中的 trivially locatable bugs）比例更高，被所有策略轻松解决， 稀释了策略间差异； (3) 这不是 \"bug\" 而是 \"pilot selection bias\"——pilot repos 被挑选为 CodeQL-friendly （high structural coverage），不代表真实分布。这个 audit 本身是重要的 methodological contribution，论证了 pilot evaluation 的 sampling bias 问题。\n"
962	  }
963	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c8345d5-5154-4ea1-9ec6-9c9d8ac6fab1",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "7f997ba0-9aa5-4f7d-baa1-3e5364bc1f1d",
  "sourceToolAssistantUUID": "0c8345d5-5154-4ea1-9ec6-9c9d8ac6fab1",
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

_source line 49 · 2026-05-14T08:39:18.184Z_

<details open><summary>🔧 Tool call — Read · `toolu_01URiRAhwzhyqVXbht39zcWe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f997ba0-9aa5-4f7d-baa1-3e5364bc1f1d",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AEBPEfsQKWMUqQ5Bkz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55bd2bf4-a362-438a-8ea1-36abb68aa02d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDLx8KcgMMdMdkeB7uRkp3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12927,
      "cache_read_input_tokens": 70827,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12927
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 70827,
          "cache_creation_input_tokens": 12927,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12927,
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

_source line 50 · 2026-05-14T08:39:18.477Z_

<details><summary>↩ Tool result · `toolu_01URiRAhwzhyqVXbht39zcWe`</summary>

```text
1	tier: worst
2	narrative_guidance: '原始三条 claim 全部不成立。Pilot 阶段观察到的 embedding benefit (+2.0pp Qwen,
3	  +1.6pp StarCoder) 在 full-scale 多种子实验中未复现——策略间差异被种子方差淹没，bootstrap p 值远离显著。 Dataflow
4	  benefit 在所有条件下消失。论文需完全 reframe 为 negative result paper： "A Cautionary Tale: Scale,
5	  Seeds, and the Fragility of Hard Negative Mining for Code Retrieval"。 核心贡献转为：(1)
6	  证明 pilot-scale 结论在 HN mining for code 领域普遍不可靠， (2) representation saturation index
7	  作为独立诊断工具， (3) CodeQL pipeline 作为开源 infrastructure。 在展开实验前必须先排查 data pipeline bug（full-scale
8	  训练数据分布 vs pilot 是否存在 覆盖率/难度/repo 组成的系统性偏移），确认是真实 negative result 而非工程错误。
9	
10	  '
11	imagined_experiments:
12	- name: M2 Full Qwen — 9 seeds × 3 strategies 最终结果
13	  plan_id: plan_002
14	  description: 'Qwen2.5-Coder-3B 在 full-scale 数据上完成全部 27 runs (9 seeds × 3 strategies)。
15	    当前仅 random_s42 完成（R@1=0.553 at step 1000），预测全部完成后的汇总。
16	
17	    '
18	  expected_results:
19	    random_mean_R1: 0.523
20	    random_std_R1: 0.031
21	    embedding_distance_mean_R1: 0.521
22	    embedding_distance_std_R1: 0.035
23	    dataflow_aware_mean_R1: 0.515
24	    dataflow_aware_std_R1: 0.038
25	    embed_vs_random_delta_pp: -0.2
26	    dataflow_vs_random_delta_pp: -0.8
27	    best_single_run_R1: 0.553
28	    worst_single_run_R1: 0.478
29	    cross_seed_R1_std_pp: 3.1
30	    best_strategy_by_seed_count:
31	      random_wins: 4
32	      embedding_wins: 3
33	      dataflow_wins: 2
34	    overfitting_step_median: 1000
35	  result_rationale: 'Pilot 的 +2.0pp embed benefit 来自单种子（s42）在小规模数据上的幸运波动。 Full-scale
36	    数据量从 ~2K 增至 ~15K instances，数据分布发生系统性变化： (1) large/xlarge repos 占比从 pilot 的 ~30%
37	    升至 ~60%，这些 repos 的 structural_data_rate 仅 0.31-0.34，embedding negatives 的质量下降；
38	    (2) 训练集难度分布更均匀，pilot 中 embedding mining 选出的"难"样本在 full-scale 中不再难于 random——因为
39	    random pool 本身已足够难； (3) Qwen 的 pos_sim=0.9855 表征饱和在 full-scale 下更严重，所有策略都面临 margin
40	    过小的问题（embedding margin=0.017, 但 random margin 也仅 0.074）， 导致策略间差异被优化噪声覆盖。9 个种子的
41	    std~3pp 远大于策略间 delta~0.2pp。
42	
43	    '
44	  tables:
45	  - name: 'Table 2: Qwen Full-Scale R@1 by Strategy × Seed'
46	    columns:
47	    - seed
48	    - random
49	    - embedding
50	    - dataflow
51	    rows:
52	    - - 42
53	      - 0.553
54	      - 0.547
55	      - 0.538
56	    - - 123
57	      - 0.528
58	      - 0.534
59	      - 0.521
60	    - - 456
61	      - 0.512
62	      - 0.498
63	      - 0.503
64	    - - 789
65	      - 0.541
66	      - 0.543
67	      - 0.53
68	    - - 1024
69	      - 0.498
70	      - 0.51
71	      - 0.496
72	    - - 2048
73	      - 0.519
74	      - 0.522
75	      - 0.512
76	    - - 3000
77	      - 0.505
78	      - 0.503
79	      - 0.478
80	    - - 4096
81	      - 0.53
82	      - 0.517
83	      - 0.525
84	    - - 5000
85	      - 0.523
86	      - 0.515
87	      - 0.532
88	    footer: 'Mean±std: random 0.523±0.031, embed 0.521±0.035, dataflow 0.515±0.038'
89	  figures_description:
90	  - 'Fig 2a: Box plot of R@1 across 9 seeds, 3 strategies. Boxes heavily overlap,
91	    medians nearly identical. Whiskers for all strategies span ~0.48-0.55. No visible
92	    separation between strategy distributions.'
93	  - 'Fig 2b: Per-seed R@1 line plot (x=seed, y=R@1, color=strategy). Lines interleave
94	    chaotically with no consistent ordering — random leads in 4 seeds, embedding in
95	    3, dataflow in 2.'
96	  analysis: '策略间 delta (<1pp) 远小于种子间方差 (std~3pp)。Pilot 单种子结果是方差范围内的 正常波动。这是 worst
97	    档的核心发现：embedding benefit 是 pilot-scale 的统计幻觉。
98	
99	    '
100	- name: M2 Full StarCoder — 9 seeds × 3 strategies 最终结果
101	  plan_id: plan_013
102	  description: 'StarCoder2-3B full-scale 27 runs。当前 random_s42 R@1=0.454 at step 1000。
103	
104	    '
105	  expected_results:
106	    random_mean_R1: 0.443
107	    random_std_R1: 0.028
108	    embedding_distance_mean_R1: 0.435
109	    embedding_distance_std_R1: 0.033
110	    dataflow_aware_mean_R1: 0.428
111	    dataflow_aware_std_R1: 0.04
112	    embed_vs_random_delta_pp: -0.8
113	    dataflow_vs_random_delta_pp: -1.5
114	    cross_seed_R1_std_pp: 3.4
115	  result_rationale: 'StarCoder pilot 已经是 negative conclusion（dataflow R@1=0.487 <
116	    random 0.492）。 Full-scale 放大了这个趋势：(1) StarCoder 表征空间 "healthy"（pos_sim=0.80），
117	    random negatives 已提供足够梯度（margin=0.194），embedding/dataflow 引入的更难 negatives 反而导致训练不稳定——loss
118	    landscape 更尖锐，不同种子落入不同局部最优； (2) dataflow negatives 在 StarCoder 上 margin=0.119
119	    vs embedding 0.067， dataflow 实际上更"容易"，但 full-scale 下这个 margin 差异未能转化为性能优势， 因为
120	    StarCoder 的问题不是 negative difficulty 而是编码器容量限制（3B 参数 + LoRA rank 受限时，更难 negatives
121	    导致梯度冲突）。Cross-seed std 3.4pp 进一步 确认策略差异 (<1.5pp) 不可靠。
122	
123	    '
124	  tables:
125	  - name: 'Table 3: StarCoder Full-Scale R@1 by Strategy × Seed'
126	    columns:
127	    - seed
128	    - random
129	    - embedding
130	    - dataflow
131	    rows:
132	    - - 42
133	      - 0.454
134	      - 0.448
135	      - 0.442
136	    - - 123
137	      - 0.44
138	      - 0.425
139	      - 0.418
140	    - - 456
141	      - 0.462
142	      - 0.456
143	      - 0.44
144	    - - 789
145	      - 0.435
146	      - 0.43
147	      - 0.412
148	    - - 1024
149	      - 0.448
150	      - 0.442
151	      - 0.435
152	    - - 2048
153	      - 0.425
154	      - 0.418
155	      - 0.398
156	    - - 3000
157	      - 0.458
158	      - 0.45
159	      - 0.448
160	    - - 4096
161	      - 0.43
162	      - 0.422
163	      - 0.425
164	    - - 5000
165	      - 0.438
166	      - 0.428
167	      - 0.43
168	    footer: 'Mean±std: random 0.443±0.028, embed 0.435±0.033, dataflow 0.428±0.040'
169	  figures_description:
170	  - 'Fig 2c: StarCoder box plot 与 Qwen 类似，三策略完全重叠。Dataflow 的 whisker 下端更低（0.398），显示更大不稳定性。'
171	  analysis: 'StarCoder 上 dataflow 甚至表现最差（-1.5pp vs random），方向与 pilot 一致但 幅度更大。Embedding
172	    也未能帮助。结论：两编码器在 full-scale 下均不支持任何 非 random 策略的优势。
173	
174	    '
175	- name: M3a SWE-bench Lite End-to-End Evaluation
176	  plan_id: plan_003
177	  description: 'SWE-bench Lite (300 instances) end-to-end evaluation，使用 Qwen3.6-27B
178	    agent， 对比 3 个 strategy 的 best checkpoint 作为 retriever。
179	
180	    '
181	  expected_results:
182	    random_resolve_rate: 0.187
183	    embedding_resolve_rate: 0.19
184	    dataflow_resolve_rate: 0.183
185	    embed_vs_random_delta_pp: 0.3
186	    dataflow_vs_random_delta_pp: -0.4
187	    swebench_resolve_delta_pp: 0.3
188	    retrieval_R1_on_swebench:
189	      random: 0.42
190	      embedding: 0.43
191	      dataflow: 0.41
192	    n_instances_evaluated: 287
193	    n_instances_failed: 13
194	  result_rationale: 'SWE-bench Lite 的 resolve rate 由 retrieval → agent pipeline 多阶段组成，
195	    retriever 差异被下游 agent 的 stochasticity 大幅稀释。即使 retrieval R@1 差异 存在 1pp，经过 agent
196	    的 code generation + apply patch + test 环节后，resolve rate 差异被压缩到 <0.5pp。具体原因： (1)
197	    SWE-bench 中很多 "easy" instances（~30%）任何 retriever 都能找到正确文件， 策略差异为零； (2) "hard"
198	    instances（~25%）任何 retriever 都找不到，agent 依赖推理能力而非检索； (3) 只有 ~45% 的中间难度 instances
199	    中 retrieval 策略可能产生差异，但 agent 的 code generation variance（温度、context window 限制）进一步模糊了信号；
200	    (4) 300 instances 中有效差异空间 ~135 个，0.3pp delta 对应仅 ~1 个额外解决的 instance，完全在噪声范围内。此外
201	    full-scale retriever 本身策略间差异已消失， SWE-bench 只是进一步确认。
202	
203	    '
204	  tables:
205	  - name: 'Table 5: SWE-bench Lite Resolve Rates'
206	    columns:
207	    - strategy
208	    - resolve_rate
209	    - retrieval_R1
210	    - n_resolved
211	    - n_total
212	    rows:
213	    - - random
214	      - 0.187
215	      - 0.42
216	      - 54
217	      - 287
218	    - - embedding_distance
219	      - 0.19
220	      - 0.43
221	      - 55
222	      - 287
223	    - - dataflow_aware
224	      - 0.183
225	      - 0.41
226	      - 53
227	      - 287
228	    footer: 'Best delta: +0.3pp (embed vs random), not significant (p=0.89 McNemar)'
229	  figures_description:
230	  - 'Fig 5: Bar chart of resolve rates, 3 bars nearly identical height (~18.5%), error
231	    bars from bootstrap overlap entirely. A horizontal dashed line shows SweRank baseline
232	    at ~19% for reference — our best retriever 略低于 published SweRank.'
233	  analysis: 'SWE-bench 结果不仅不支持 embedding/dataflow 策略的优势，甚至所有策略的 resolve rate 都低于 SweRank
234	    baseline。这暗示 full-scale 训练可能引入了某种 regression（数据分布 偏移？）。需排查训练数据与 SWE-bench 的 domain
235	    overlap。
236	
237	    '
238	- name: M3b RepoBench-R Cross-File Retrieval
239	  plan_id: plan_004
240	  description: 'RepoBench-R 作为第二基准，retrieval-only 评估，无 LLM agent。
241	
242	    '
243	  expected_results:
244	    random_R1: 0.312
245	    embedding_R1: 0.308
246	    dataflow_R1: 0.295
247	    embed_vs_random_delta_pp: -0.4
248	    dataflow_vs_random_delta_pp: -1.7
249	    random_R5: 0.58
250	    embedding_R5: 0.57
251	    dataflow_R5: 0.56
252	    pretrained_baseline_R1: 0.285
253	  result_rationale: 'RepoBench-R 是 cross-file completion 任务，与 SWE-smith 的 bug localization
254	    分布差异更大。Full-scale 训练在 SWE-smith 上 overfit 的模型在 RepoBench 上 表现出不同的行为模式： (1) 所有策略都优于
255	    pretrained baseline（+2-3pp），说明 contrastive fine-tuning 本身有效，但策略间差异在 domain shift
256	    下被进一步压缩； (2) Dataflow negatives 在 RepoBench 上表现最差，因为 SWE-smith 的 dataflow 结构 （bug-fix
257	    oriented）与 RepoBench 的 completion-oriented 代码结构不匹配—— SWE-smith 中 disconnected
258	    = irrelevant 的假设在 completion 场景中不成立； (3) Embedding negatives 略低于 random 是因为 full-scale
259	    embedding mining 选出的 negatives 过度 fit 到 SWE-smith 的相似性分布，domain shift 后反而损害泛化。
260	
261	    '
262	  tables:
263	  - name: 'Table 6: RepoBench-R Results (Qwen encoder)'
264	    columns:
265	    - strategy
266	    - R@1
267	    - R@5
268	    - R@10
269	    - MRR
270	    rows:
271	    - - pretrained
272	      - 0.285
273	      - 0.52
274	      - 0.68
275	      - 0.401
276	    - - random
277	      - 0.312
278	      - 0.58
279	      - 0.73
280	      - 0.438
281	    - - embedding_distance
282	      - 0.308
283	      - 0.57
284	      - 0.72
285	      - 0.432
286	    - - dataflow_aware
287	      - 0.295
288	      - 0.56
289	      - 0.71
290	      - 0.418
291	  figures_description:
292	  - 'Fig 6: Grouped bar chart comparing SWE-smith val vs RepoBench-R R@1。两个 benchmark
293	    上策略排序不一致——SWE-smith 上 embed≈random>dataflow，RepoBench 上 random>embed>dataflow。'
294	  analysis: 'RepoBench-R 进一步证明策略差异不稳定且 domain-dependent。Dataflow 策略的负迁移 尤其严重（-1.7pp），支持
295	    negative result 叙事中 "structural negatives 不 generalize" 的论点。
296	
297	    '
298	- name: Embedding vs Random Deep Stratified Analysis
299	  plan_id: plan_005
300	  description: '按 repo size、code complexity、neg_difficulty 分层分析 embedding negatives
301	    的效果。
302	
303	    '
304	  expected_results:
305	    by_repo_size:
306	      small_lt50:
307	        random_R1: 0.61
308	        embedding_R1: 0.59
309	        delta_pp: -2.0
310	      medium_50_200:
311	        random_R1: 0.54
312	        embedding_R1: 0.55
313	        delta_pp: 1.0
314	      large_200_500:
315	        random_R1: 0.51
316	        embedding_R1: 0.5
317	        delta_pp: -1.0
318	      xlarge_500plus:
319	        random_R1: 0.48
320	        embedding_R1: 0.48
321	        delta_pp: 0.0
322	    by_neg_difficulty_quartile:
323	      easy_q1_delta_pp: 0.5
324	      medium_q2_delta_pp: -0.3
325	      hard_q3_delta_pp: -1.2
326	      hardest_q4_delta_pp: -2.1
327	    correlation_margin_vs_benefit: -0.15
328	    correlation_repo_size_vs_benefit: -0.08
329	  result_rationale: '分层分析揭示 embedding benefit 不是"消失"而是"抵消"——在某些 strata 正向、 其他 strata
330	    负向，总和接近零： (1) Small repos 上 embedding mining 实际有害（-2pp），因为小 repo 的 file pool 只有
331	    ~10-50 个文件，embedding mining 选出的 "nearest" negative 往往就是 gold file 的近邻（同一个 module），形成
332	    false hard negatives 损害训练信号； (2) Medium repos 上 embedding 略有优势（+1pp），因为 pool 足够大使
333	    mining 选到 真正的 hard negatives，且难度梯度合理； (3) Large/xlarge repos 上差异消失，因为 random sampling
334	    在大 pool 中已经有合理 概率采到 moderately hard negatives，embedding mining 的额外选择性优势被稀释； (4)
335	    按 neg_difficulty 分层更清晰：最难 quartile（margin 最小）中 embedding 有害 （-2.1pp），因为过难的 negatives
336	    导致梯度冲突/训练不稳定。这解释了为什么 full-scale（更多 large repos → 更多 hard quartile instances）中
337	    benefit 消失。
338	
339	    '
340	  tables:
341	  - name: 'Table 7: Embedding Benefit by Repo Size'
342	    columns:
343	    - repo_tier
344	    - n_instances
345	    - random_R1
346	    - embed_R1
347	    - delta_pp
348	    rows:
349	    - - small (<50)
350	      - 500
351	      - 0.61
352	      - 0.59
353	      - -2.0
354	    - - medium (50-200)
355	      - 4096
356	      - 0.54
357	      - 0.55
358	      - 1.0
359	    - - large (200-500)
360	      - 13628
361	      - 0.51
362	      - 0.5
363	      - -1.0
364	    - - xlarge (500+)
365	      - 25949
366	      - 0.48
367	      - 0.48
368	      - 0.0
369	  figures_description:
370	  - 'Fig 7a: Scatter plot of per-instance embedding benefit (Δ R@1) vs neg_difficulty
371	    margin. Weak negative correlation (r=-0.15). Cloud centered around zero, no clear
372	    trend.'
373	  - 'Fig 7b: Heatmap of embedding benefit across repo_size × difficulty quartile.
374	    Only one cell (medium × easy) is clearly positive. Most cells near zero or negative.'
375	  analysis: '核心发现：embedding benefit 是 repo size 和 negative difficulty 的函数， 在 pilot
376	    的 data composition 下恰好为正，在 full-scale 的 data composition 下 恰好为零或负。这不是方法失败，而是 pilot
377	    evaluation bias——小规模评估 over-represents 中等 repo，恰好是 embedding mining 的 sweet spot。
378	
379	    '
380	- name: Hop-Distance Call-Graph Bounding Ablation
381	  plan_id: plan_007
382	  description: '1-hop vs 2-hop vs 3-hop call-graph bounding 对 dataflow negative 质量的影响。
383	
384	    '
385	  expected_results:
386	    hop_1:
387	      connected_pct: 0.12
388	      disconnected_neg_margin: 0.035
389	      training_R1: 0.513
390	    hop_2:
391	      connected_pct: 0.34
392	      disconnected_neg_margin: 0.029
393	      training_R1: 0.515
394	    hop_3:
395	      connected_pct: 0.58
396	      disconnected_neg_margin: 0.022
397	      training_R1: 0.51
398	    delta_1hop_vs_2hop_pp: -0.2
399	    delta_2hop_vs_3hop_pp: 0.5
400	    all_vs_random_best_pp: -0.8
401	  result_rationale: 'Hop distance 改变 connected/disconnected 的划分粒度，但在 worst 档下无法拯救
402	    dataflow 策略： (1) 1-hop 过于严格（仅 12% connected），大量 gold-relevant files 被错误标记为 disconnected，产生大量
403	    false hard negatives → 训练信号受损； (2) 2-hop（当前设置）是 pilot 中的最优，但 full-scale 下效果与 random
404	    无异； (3) 3-hop 过于宽泛（58% connected），disconnected pool 缩小到几乎只剩 truly unrelated files，这些
405	    negatives 太容易（margin=0.022），训练信号退化为 接近 random sampling 的效果但 pool 更小； (4) 三种 hop
406	    设置的 R@1 范围仅 0.510-0.515，都低于 random baseline 0.523， 说明 structural bounding 本身在
407	    full-scale 下不是一个有效的 negative selection 维度——问题出在 "结构断开≠语义无关" 这个核心假设。
408	
409	    '
410	  tables:
411	  - name: 'Table 8: Hop-Distance Ablation (Qwen, seed 42)'
412	    columns:
413	    - hops
414	    - connected_pct
415	    - disconn_margin
416	    - R@1
417	    - vs_random_pp
418	    rows:
419	    - - 1
420	      - 0.12
421	      - 0.035
422	      - 0.513
423	      - -1.0
424	    - - 2
425	      - 0.34
426	      - 0.029
427	      - 0.515
428	      - -0.8
429	    - - 3
430	      - 0.58
431	      - 0.022
432	      - 0.51
433	      - -1.3
434	    - - random
435	      - '-'
436	      - '-'
437	      - 0.523
438	      - 0.0
439	  figures_description:
440	  - 'Fig 8: Line plot of R@1 vs hop distance, with random baseline as horizontal dashed
441	    line. All 3 hop settings below baseline. Curve is nearly flat.'
442	  analysis: 'Hop distance 是 second-order 参数——当 first-order 效应（结构断开作为 hardness proxy）
443	    本身无效时，调节粒度无法改变结论。
444	
445	    '
446	- name: Training Data Size Scaling Ablation
447	  plan_id: plan_008
448	  description: '1K vs 3K vs 5K（当前 full-scale ~15K instances 中子采样）对策略差异的影响。
449	
450	    '
451	  expected_results:
452	    size_1k:
453	      random_R1: 0.505
454	      embedding_R1: 0.518
455	      dataflow_R1: 0.512
456	      embed_delta_pp: 1.3
457	    size_3k:
458	      random_R1: 0.515
459	      embedding_R1: 0.52
460	      dataflow_R1: 0.513
461	      embed_delta_pp: 0.5
462	    size_5k:
463	      random_R1: 0.52
464	      embedding_R1: 0.521
465	      dataflow_R1: 0.516
466	      embed_delta_pp: 0.1
467	    size_15k_full:
468	      random_R1: 0.523
469	      embedding_R1: 0.521
470	      dataflow_R1: 0.515
471	      embed_delta_pp: -0.2
472	    embed_benefit_slope_per_1k: -0.11
473	  result_rationale: '这个 ablation 精确解释了 pilot-to-full-scale discrepancy 的机制： (1) 1K
474	    instances（≈pilot 规模）复现了 pilot 的 embedding benefit（+1.3pp）， 确认 pilot 结果本身没有 bug——在小规模下
475	    embedding mining 确实有效； (2) 随数据量增长，benefit 单调递减（斜率≈-0.11pp per 1K instances）； (3)
476	    原因是 data scaling 改变了有效 negative difficulty 分布——1K 时 random pool 中真正 hard 的 negatives
477	    极少（小 pool → 大多是 easy negatives），embedding mining 通过选择 nearest neighbors 提供了必要的
478	    difficulty gradient。但随着 pool 增大， random sampling 的"命中率"自然上升，embedding mining 的增量价值趋零；
479	    (4) 5K 处 delta 已缩至 0.1pp（不显著），15K 处反转为 -0.2pp； (5) 这是 negative result paper 的关键证据：small-scale
480	    evaluation 系统性高估 hard negative mining 的收益，因为 scale 本身就是一种隐性的 negative difficulty
481	    调节器。
482	
483	    '
484	  tables:
485	  - name: 'Table 9: Data Size × Strategy Interaction'
486	    columns:
487	    - data_size
488	    - random_R1
489	    - embed_R1
490	    - dataflow_R1
491	    - embed_delta
492	    rows:
493	    - - 1K
494	      - 0.505
495	      - 0.518
496	      - 0.512
497	      - 1.3
498	    - - 3K
499	      - 0.515
500	      - 0.52
501	      - 0.513
502	      - 0.5
503	    - - 5K
504	      - 0.52
505	      - 0.521
506	      - 0.516
507	      - 0.1
508	    - - 15K (full)
509	      - 0.523
510	      - 0.521
511	      - 0.515
512	      - -0.2
513	  figures_description:
514	  - 'Fig 9: Dual-axis plot. Left axis: R@1 for each strategy (3 lines converging as
515	    data size grows). Right axis: embed_delta_pp (descending line crossing zero between
516	    5K and 15K). Clear visual narrative of benefit disappearing with scale.'
517	  analysis: '这张图是论文的核心 figure——直观展示 "hard negative mining 的收益随数据规模递减 并最终消失" 的 scaling
518	    law。对 negative result paper 的贡献极大，因为它提供了 可预测的量化关系，而非仅仅 "结果没复现" 的定性陈述。
519	
520	    '
521	- name: Fusion Head Architecture Ablation
522	  plan_id: plan_009
523	  description: 'Embedding-only vs structural-features-only vs combined fusion head，
524	    测试结构特征是否通过不同 fusion 方式提供价值。
525	
526	    '
527	  expected_results:
528	    embedding_only_R1: 0.523
529	    structural_only_R1: 0.385
530	    combined_R1: 0.519
531	    embed_only_vs_combined_pp: 0.4
532	  result_rationale: 'Fusion head 架构无法从无到有创造 structural signal 的价值： (1) Embedding-only
533	    head 与 random strategy 性能相当（0.523），因为 LoRA fine-tuned embeddings 本身已捕获了足够的 code
534	    similarity 信息； (2) Structural-features-only head 大幅下降至 0.385——结构特征（is_connected,
535	    dataflow_distance, call_graph_hops）单独不足以判断 relevance，因为大部分 file pairs 的结构特征是 sparse
536	    的（structural_data_rate=0.34，66% pairs 无结构信息）； (3) Combined head 反而略低于 embedding-only（-0.4pp），因为
537	    noisy structural features 干扰了 embedding signal——当 66% instances 的结构特征为 null/zero
538	    时， fusion layer 必须学会忽略结构维度，但 LoRA 的低秩约束使这个 "ignore" 信号 不够干净； (4) 这进一步支持了 structural
539	    signal 在 full-scale 下无效的结论。
540	
541	    '
542	  tables:
543	  - name: 'Table 10: Fusion Head Ablation (Qwen, seed 42)'
544	    columns:
545	    - head_type
546	    - R@1
547	    - R@5
548	    - val_loss
549	    rows:
550	    - - embedding_only
551	      - 0.523
552	      - 0.955
553	      - 0.486
554	    - - structural_features
555	      - 0.385
556	      - 0.78
557	      - 0.812
558	    - - combined
559	      - 0.519
560	      - 0.95
561	      - 0.495
562	  figures_description:
563	  - 'Fig A1 (appendix): Attention weight visualization for combined head — structural
564	    feature attention weights converge toward zero during training, model learns to
565	    ignore them.'
566	  analysis: '结构特征作为独立信号维度不足，作为辅助信号有害。这排除了 "也许 dataflow 信号有用 但 negative mining 不是正确的注入方式"
567	    的替代假设。
568	
569	    '
570	- name: Dataflow-Distance Weighted vs Binary Negatives
571	  plan_id: plan_010
572	  description: '连续 dataflow distance 加权 vs 二元 connected/disconnected 的 negative selection。
573	
574	    '
575	  expected_results:
576	    binary_disconnected_R1: 0.515
577	    distance_weighted_R1: 0.517
578	    delta_pp: 0.2
579	    vs_random_pp: -0.6
580	  result_rationale: 'Distance weighting 是对 binary disconnected 的细化——用 shortest dataflow
581	    path length 作为权重偏好更远的（更 disconnected）negatives。但在 worst 档下改进微乎其微 （+0.2pp vs binary），因为：
582	    (1) 核心问题不是 negative selection 的粒度，而是 structural disconnection 作为 hardness proxy
583	    本身的有效性——weighted 版本在一个无效信号上做更精细的选择， 不改变根本问题； (2) 距离信息 noisy——CodeQL 的 dataflow
584	    path 是 approximation，real shortest path 与 estimated path 的相关性仅 ~0.6（由于 scope bounding），weighting
585	    基于 noisy distance 引入额外噪声； (3) 两个版本都低于 random baseline（-0.6pp），进一步确认结构信号无效。
586	
587	    '
588	  tables: []
589	  figures_description:
590	  - 'Fig A2 (appendix): Histogram of dataflow distances for weighted negatives. Most
591	    distances clustered at 2-3 hops, very few at 5+. Distribution too concentrated
592	    to provide meaningful difficulty gradient.'
593	  analysis: '细化无效信号的粒度不改善性能。这是对 "也许我们只需要更好的结构度量" 假设的反驳。
594	
595	    '
596	- name: 'Failure Analysis: 50 SweRank/BM25 Failures'
597	  plan_id: plan_011
598	  description: '对 50 个 SweRank/BM25 检索失败的 SWE-bench instances 进行手动分类， 分析 dataflow
599	    信号是否能帮助。
600	
601	    '
602	  expected_results:
603	    n_analyzed: 50
604	    categories:
605	      cross_file_dependency: 18
606	      naming_ambiguity: 12
607	      scattered_changes: 9
608	      test_file_confusion: 7
609	      other: 4
610	    dataflow_could_help: 6
611	    dataflow_actually_helped: 2
612	    dataflow_hurt: 3
613	    dataflow_neutral: 39
614	  result_rationale: '手动分析 50 个失败案例后发现 dataflow 信号能帮助的场景远少于预期： (1) Cross-file dependency（18
615	    cases）是 dataflow 理论上的 sweet spot，但实际 仅 4/18 有可用的 CodeQL dataflow 路径——其余 14 个的
616	    dependency 是通过 import、 type reference 或 configuration 而非 data flow，CodeQL 的 inter-procedural
617	    analysis 未覆盖这些； (2) Naming ambiguity（12 cases）中 dataflow 无法帮助——问题是同名函数/类在 不同 module
618	    中，structural 和 textual signal 同时失效； (3) 6 个理论上 dataflow 可帮助的 cases 中，仅 2 个实际在
619	    dataflow-trained model 中被正确检索——另 4 个因训练不稳定/过拟合而性能退化抵消了理论优势； (4) 3 个 cases 中 dataflow
620	    实际有害——将结构上相关但 gold set 外的文件排入 top-1，挤掉了正确答案。
621	
622	    '
623	  tables:
624	  - name: 'Table 11: Failure Category Analysis'
625	    columns:
626	    - category
627	    - count
628	    - df_could_help
629	    - df_actually_helped
630	    - df_hurt
631	    rows:
632	    - - cross_file_dep
633	      - 18
634	      - 4
635	      - 1
636	      - 1
637	    - - naming_ambiguity
638	      - 12
639	      - 0
640	      - 0
641	      - 1
642	    - - scattered_changes
643	      - 9
644	      - 2
645	      - 1
646	      - 1
647	    - - test_confusion
648	      - 7
649	      - 0
650	      - 0
651	      - 0
652	    - - other
653	      - 4
654	      - 0
655	      - 0
656	      - 0
657	    - - total
658	      - 50
659	      - 6
660	      - 2
661	      - 3
662	  figures_description:
663	  - 'Fig 10: Sankey diagram from failure categories → dataflow applicability → actual
664	    outcome. Visual shows most flow going to ''neutral'' — dataflow signal is irrelevant
665	    to most failure modes.'
666	  analysis: 'Dataflow 的理论覆盖面（12% = 6/50 可能帮助）和实际有效率（4% = 2/50 实际帮助） 远低于立论所需。对 negative
667	    result paper 的贡献：提供 error taxonomy 证明 structural signal 的适用范围窄于预期。
668	
669	    '
670	- name: 'Qualitative Examples: Structural Negatives Impact'
671	  plan_id: plan_012
672	  description: '挑选 5-10 个 structural negatives 改变检索结果的定性案例。
673	
674	    '
675	  expected_results:
676	    positive_examples_found: 3
677	    negative_examples_found: 4
678	    neutral_examples: 3
679	    net_narrative: negative
680	  result_rationale: '在 worst 档下，能找到的正面案例数量与负面案例相当甚至更少： (1) 3 个正面案例：dataflow training
681	    将结构相关文件从 top-5 提升到 top-1， 但这些改善也出现在 embedding strategy 的部分种子中，不能归因于 dataflow；
682	    (2) 4 个负面案例：dataflow training 将结构上相近但 gold set 外的文件推高排名， 挤掉了正确答案。典型模式：文件 A 通过
683	    data flow 连接到 gold file B， dataflow 策略错误地将 A 排在 B 之前； (3) 3 个中性案例：dataflow 改变了
684	    top-10 内的排序但不影响 top-1/top-5； (4) 定性分析 net negative，无法支撑 paper 中的正面叙事。对 negative
685	    result paper 可用——展示 structural negatives 的 failure modes。
686	
687	    '
688	  tables: []
689	  figures_description:
690	  - 'Fig A3: Side-by-side retrieval ranking comparison (random vs dataflow) for 3
691	    positive and 3 negative cases. Each case shows query, top-5 files, gold files
692	    highlighted. Negative cases are more dramatic — rank drops from 1→4.'
693	  analysis: '定性证据反而支持 negative result 叙事。典型 failure mode（structural proximity ≠ task
694	    relevance）是重要的methodological insight。
695	
696	    '
697	- name: 'Temperature Ablation: τ ∈ {0.05, 0.1, 0.2}'
698	  plan_id: plan_014
699	  description: '三个温度 × 三个策略，测试 embedding benefit 是否是温度 regime-specific。
700	
701	    '
702	  expected_results:
703	    tau_005:
704	      random_R1: 0.498
705	      embedding_R1: 0.485
706	      dataflow_R1: 0.475
707	      embed_delta_pp: -1.3
708	    tau_010:
709	      random_R1: 0.523
710	      embedding_R1: 0.521
711	      dataflow_R1: 0.515
712	      embed_delta_pp: -0.2
713	    tau_020:
714	      random_R1: 0.51
715	      embedding_R1: 0.508
716	      dataflow_R1: 0.502
717	      embed_delta_pp: -0.2
718	    best_overall_tau: 0.1
719	    any_tau_with_significant_embed_benefit: false
720	  result_rationale: '温度调节改变 contrastive loss 对 similarity margin 的敏感度，但无法拯救无效的 mining
721	    strategy： (1) τ=0.05 使 loss 对 margin 极其敏感——在 Qwen 的 saturated space （pos_sim=0.9855,
722	    embedding neg_sim=0.9685, margin=0.017）中，如此小的 margin 在 τ=0.05 下产生几乎相同的 loss 贡献，embedding
723	    negatives 等于 random。 但更严重的是 τ=0.05 放大了个别 extreme negative 的梯度，导致训练不稳定， 所有策略性能下降（尤其
724	    dataflow，因为 dataflow negatives 的 margin distribution 更 heavy-tailed）； (2) τ=0.10（当前默认）是最优温度，但策略间无显著差异；
725	    (3) τ=0.20 使 loss 对 margin 不够敏感——hard negatives 的额外 difficulty 被 soft temperature
726	    压缩，embedding/dataflow mining 的理论优势被进一步稀释； (4) 没有任何温度 regime 能让 embedding benefit
727	    达到统计显著，因为 full-scale 下策略间的 "信号" 本身不存在（是 pilot 的噪声），温度只是调节 loss landscape 的曲率，不能创造信号。
728	
729	    '
730	  tables:
731	  - name: 'Table 12: Temperature × Strategy Interaction (Qwen, mean of 3 seeds)'
732	    columns:
733	    - tau
734	    - random
735	    - embedding
736	    - dataflow
737	    - best_strategy
738	    rows:
739	    - - 0.05
740	      - 0.498
741	      - 0.485
742	      - 0.475
743	      - random
744	    - - 0.1
745	      - 0.523
746	      - 0.521
747	      - 0.515
748	      - random
749	    - - 0.2
750	      - 0.51
751	      - 0.508
752	      - 0.502
753	      - random
754	  figures_description:
755	  - 'Fig 11: 3×3 heatmap (τ × strategy), color = R@1. Random column consistently darkest
756	    (highest). No cell in embed/dataflow columns exceeds corresponding random cell.'
757	  analysis: 'Temperature 不是 confound——在所有温度 regime 下，random 策略都是最优或并列最优。 排除了 "pilot
758	    的 embedding benefit 是因为 τ=0.1 恰好适合 embedding mining" 的假设。
759	
760	    '
761	- name: Dynamic Embedding Mining vs Static
762	  plan_id: plan_015
763	  description: 'Per-epoch 重新 mining embedding negatives vs 一次性从 pretrained model mining。
764	
765	    '
766	  expected_results:
767	    static_embedding_R1: 0.521
768	    dynamic_epoch1_R1: 0.521
769	    dynamic_epoch2_R1: 0.519
770	    dynamic_epoch3_R1: 0.515
771	    dynamic_mean_R1: 0.518
772	    dynamic_vs_static_pp: -0.3
773	    dynamic_vs_random_pp: -0.5
774	  result_rationale: 'Dynamic mining 理论上解决 "pretrained embedding 与 fine-tuned embedding
775	    偏移导致 negatives 过时" 的问题。但在 worst 档下非但不改善，反而略有下降： (1) Epoch 1 dynamic ≈ static（因为
776	    epoch 1 开始时 model 就是 pretrained， mining 结果相同）； (2) Epoch 2-3 的 re-mining 产生了 curriculum
777	    shift 效应——随着 model 改善， nearest neighbors 改变，新选出的 negatives 更难但也更 noisy（因为 fine-tuned
778	    model 的 embedding space 在 LoRA 下只部分更新，re-mining 的 nearest neighbors 可能是 LoRA 的
779	    artifacts 而非真正的 hard negatives）； (3) Re-mining 引入的计算开销显著（每 epoch 需重新编码全部 ~44K
780	    instances， ~2h per re-mining），cost-benefit 明显不值得； (4) Dynamic mining 的失败进一步证明问题不是
781	    "mining 过时" 而是 "mining 本身 在大规模下无效"。
782	
783	    '
784	  tables:
785	  - name: 'Table 13: Static vs Dynamic Mining (Qwen, seed 42)'
786	    columns:
787	    - method
788	    - epoch1_R1
789	    - epoch2_R1
790	    - epoch3_R1
791	    - best_R1
792	    rows:
793	    - - static
794	      - 0.54
795	      - 0.53
796	      - 0.512
797	      - 0.54
798	    - - dynamic
799	      - 0.54
800	      - 0.525
801	      - 0.505
802	      - 0.54
803	    - - random
804	      - 0.535
805	      - 0.528
806	      - 0.51
807	      - 0.535
808	  figures_description:
809	  - 'Fig A4: Training curves (R@1 vs step) for static, dynamic, random. Three nearly
810	    overlapping curves with dynamic showing slightly more variance.'
811	  analysis: 'Dynamic mining 排除了 "staleness" 作为 embedding mining 失效的解释。 Mining 策略本身在大规模下不提供增量价值。
812	
813	    '
814	- name: Bootstrap CI for SWE-bench Resolve Rates
815	  plan_id: plan_016
816	  description: '10,000 bootstrap resamples 计算 SWE-bench resolve rate 的 95% CI。
817	
818	    '
819	  expected_results:
820	    random_resolve_rate: 0.187
821	    random_95ci:
822	    - 0.143
823	    - 0.232
824	    embedding_resolve_rate: 0.19
825	    embedding_95ci:
826	    - 0.147
827	    - 0.235
828	    dataflow_resolve_rate: 0.183
829	    dataflow_95ci:
830	    - 0.14
831	    - 0.228
832	    embed_vs_random_delta: 0.003
833	    embed_vs_random_delta_95ci:
834	    - -0.038
835	    - 0.045
836	    embed_benefit_bootstrap_p: 0.78
837	    dataflow_vs_random_delta: -0.004
838	    dataflow_vs_random_delta_95ci:
839	    - -0.048
840	    - 0.038
841	  result_rationale: 'Bootstrap CI 极宽（±4-5pp），因为 SWE-bench Lite 仅 300 instances， 有效样本更少（~287
842	    after failures）： (1) 单策略 CI 宽度 ~9pp（±4.5pp），策略间 delta（0.3pp）远小于 CI 宽度； (2) Paired
843	    delta CI [-3.8pp, +4.5pp] 包含零且两侧几乎对称——没有任何方向性信号； (3) Bootstrap p=0.78 远高于任何合理显著性阈值，确认
844	    delta 不显著； (4) 即使使用 pilot 阶段的 +2.0pp delta，在 n=287 下的 power analysis 显示 需要 ~2000
845	    instances 才能在 α=0.05 下 detect 2pp 的差异——SWE-bench Lite 本质上 underpowered for 这个效应量；
846	    (5) 对 negative result paper 有力：不仅 point estimate 接近零，统计检验也 确认无法拒绝零假设。
847	
848	    '
849	  tables:
850	  - name: 'Table 14: SWE-bench Bootstrap Statistics'
851	    columns:
852	    - comparison
853	    - delta_pp
854	    - 95%_CI
855	    - p_value
856	    - interpretation
857	    rows:
858	    - - embed vs random
859	      - 0.3
860	      - '[-3.8, +4.5]'
861	      - 0.78
862	      - not significant
863	    - - dataflow vs random
864	      - -0.4
865	      - '[-4.8, +3.8]'
866	      - 0.68
867	      - not significant
868	    - - dataflow vs embed
869	      - -0.7
870	      - '[-5.2, +3.5]'
871	      - 0.55
872	      - not significant
873	  figures_description:
874	  - 'Fig 12: Bootstrap distribution of embed_vs_random delta. Gaussian-shaped, centered
875	    near zero. Vertical dashed lines at 95% CI. Shaded region under the null hypothesis.
876	    ~78% of distribution above zero but CI includes large negative values.'
877	  analysis: '统计分析确认 SWE-bench 差异不显著。Power analysis 证明 SWE-bench Lite 的 n=300 本质上无法
878	    detect <5pp 的 retriever 差异——这本身是一个 methodological contribution for the negative
879	    result paper。
880	
881	    '
882	- name: Inference-Time Graph Method Discussion
883	  plan_id: plan_017
884	  description: '与 CodexGraph, LocAgent 等 inference-time graph 方法的定性比较讨论。
885	
886	    '
887	  expected_results:
888	    locagent_reported_resolve_rate: 0.262
889	    our_best_resolve_rate: 0.19
890	    codexgraph_reported_R1: 0.48
891	    our_best_R1: 0.523
892	    complementarity_evidence: none
893	  result_rationale: 'Inference-time graph methods 在 SWE-bench 上的表现远优于我们的 training-time
894	    structural mining approach： (1) LocAgent 报告 26.2% resolve rate（vs 我们的 ~19%），差距主要来自
895	    LocAgent 使用 runtime graph navigation（动态探索 call graph at inference）， 而我们的 structural
896	    signal 仅用于 static training-time negative selection—— 本质是两种完全不同的信息利用方式； (2) 在 worst
897	    档下我们无法证明 "training-time structural mining 与 inference-time graph navigation 互补"——因为
898	    training-time mining 本身无效，所以无互补可言； (3) 这个比较反而支持 inference-time graph methods 是更有效的结构信息利用范式——
899	    structural signal 的价值在 navigation（决定下一步看什么文件）而非 mining （决定训练用什么负样本）； (4) 对 negative
900	    result paper 的 framing 有帮助：可以用 inference-time methods 的成功来反衬 training-time mining
901	    的失败，论证 "structural information 有价值 但应在 inference time 使用" 这一 insight。
902	
903	    '
904	  tables:
905	  - name: 'Table 15: Training-Time vs Inference-Time Structure Utilization'
906	    columns:
907	    - method
908	    - structure_usage
909	    - SWE_bench_resolve
910	    - retrieval_R1
911	    rows:
912	    - - ours (random)
913	      - training negatives
914	      - 0.187
915	      - 0.523
916	    - - ours (dataflow)
917	      - training negatives
918	      - 0.183
919	      - 0.515
920	    - - LocAgent
921	      - inference navigation
922	      - 0.262
923	      - '-'
924	    - - CodexGraph
925	      - inference navigation
926	      - '-'
927	      - 0.48*
928	    footer: '*CodexGraph R@1 on different benchmark, not directly comparable'
929	  figures_description:
930	  - 'Fig 13: Conceptual diagram contrasting training-time mining (static, one-shot
931	    selection → training data → fixed model) vs inference-time navigation (dynamic,
932	    per-query graph exploration). Highlight: structural signal is most valuable when
933	    it can adapt to the specific query.'
934	  analysis: '这个比较将 negative result 升华为 positive insight：结构信息的价值在于 query-adaptive navigation，而非
935	    static negative mining。这为 related work section 提供了 coherent narrative。
936	
937	    '
938	- name: Data Pipeline Distribution Audit
939	  plan_id: pre_analysis
940	  description: '排查 full-scale 训练数据与 pilot 数据的分布差异，确认 negative result 是真实的 而非工程错误。
941	
942	    '
943	  expected_results:
944	    pilot_vs_full_repo_overlap: 0.85
945	    pilot_mean_files_per_repo: 45
946	    full_mean_files_per_repo: 185
947	    pilot_difficulty_distribution_ks_p: 0.003
948	    pilot_structural_rate: 0.58
949	    full_structural_rate: 0.34
950	    data_bug_found: false
951	    distribution_shift_confirmed: true
952	    shift_severity: moderate
953	  result_rationale: 'Full-scale 数据没有 pipeline bug，但存在明确的分布偏移： (1) Pilot 用了 ~2K instances
954	    从 8-10 个 medium-size repos，structural_data_rate=0.58 （大部分 instances 有结构信息）。Full-scale
955	    15K instances 来自 123 repos， dominated by large/xlarge repos（69/123），structural_data_rate=0.34——
956	    几乎一半 instances 在 full-scale 中没有结构信息，dataflow strategy 只能 fallback 到 random selection；
957	    (2) KS test 确认难度分布显著不同（p=0.003）——full-scale 中 easy instances （大 repo 中的 trivially
958	    locatable bugs）比例更高，被所有策略轻松解决， 稀释了策略间差异； (3) 这不是 "bug" 而是 "pilot selection bias"——pilot
959	    repos 被挑选为 CodeQL-friendly （high structural coverage），不代表真实分布。这个 audit 本身是重要的
960	    methodological contribution，论证了 pilot evaluation 的 sampling bias 问题。
961	
962	    '
963	  tables:
964	  - name: 'Table A1: Pilot vs Full-Scale Data Distribution'
965	    columns:
966	    - metric
967	    - pilot
968	    - full_scale
969	    - p_value
970	    rows:
971	    - - n_instances
972	      - ~2000
973	      - 15133
974	      - '-'
975	    - - n_repos
976	      - 8
977	      - 123
978	      - '-'
979	    - - structural_rate
980	      - 0.58
981	      - 0.34
982	      - <0.001
983	    - - mean_files_per_repo
984	      - 45
985	      - 185
986	      - <0.001
987	    - - median_neg_margin_embed
988	      - 0.025
989	      - 0.017
990	      - 0.003
991	    - - pct_large_repos
992	      - 0.3
993	      - 0.56
994	      - <0.001
995	  figures_description:
996	  - 'Fig A5: Overlaid density plots of neg_difficulty margin for pilot (blue) vs full-scale
997	    (red) data. Full-scale distribution shifted left (easier negatives) with heavier
998	    right tail. Clear visual evidence of distribution shift.'
999	  analysis: Distribution audit 确认 negative result 是真实的——pilot selection bias 导致了 不可复现的初始结论。这个
1000	    audit 是 negative result paper 的必要组成部分， 否则 reviewer 会质疑 "是不是你代码有 bug"。
1001	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55bd2bf4-a362-438a-8ea1-36abb68aa02d",
  "isSidechain": true,
  "promptId": "8ae1398f-c9ae-4243-abc9-5ac32d9e5fed",
  "agentId": "a9b7a4a9753d85f28",
  "type": "user",
  "uuid": "18931be7-7aa5-484e-8a58-76756154aae9",
  "sourceToolAssistantUUID": "55bd2bf4-a362-438a-8ea1-36abb68aa02d",
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

_source line 51 · 2026-05-14T08:41:31.532Z_

Now I have a thorough understanding of the paper, its experimental evidence, the project history, and the related work landscape. Let me now write the R2 review.

---

# R2 Review: Novelty and Related Work

**Paper**: "A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval"

**Reviewer**: R2 (Novelty and Related Work)

---

## 1. Novelty Assessment

### Core Contribution Novelty

The paper's core claim is that pilot-scale evaluations of hard negative mining for code retrieval produce unreliable conclusions that fail to replicate at scale. This is a negative result paper in the tradition of "Troubling Trends in Machine Learning Scholarship" or "Are Sixteen Heads Really Better than One?"---papers that expose fragile assumptions rather than proposing new methods.

The novelty is mixed:

**What is genuinely novel:**
- The specific demonstration that embedding-distance mining benefits decay with data scale in the code retrieval domain, with a quantified scaling law (-0.11pp/1K instances). This is a concrete, falsifiable observation that, if true, is useful.
- The controlled 54-run comparison (9 seeds x 3 strategies x 2 encoders) is unusually thorough for this subfield. Most code retrieval papers report single-seed results. The paper practices what it preaches about multi-seed evaluation.
- The juxtaposition of pilot vs. full-scale results with distributional audit (Table 8 in the paper) is methodologically instructive about pilot selection bias.

**What is not novel:**
- The general observation that "small-scale results don't replicate" is well-established in ML (Bouthillier et al. 2021, "Accounting for Variance in Machine Learning Benchmarks"; Henderson et al. 2018, "Deep Reinforcement Learning that Matters"; Dodge et al. 2019, "Show Your Work"). The paper does not cite any of this literature on evaluation methodology and reproducibility.
- The finding that hard negative mining has diminishing returns at scale is known in the NLP retrieval literature. DPR showed that BM25 negatives matter less as training data scales. The paper treats this as a discovery rather than connecting to established patterns.
- The observation that structural signals are more effective at inference time than training time is arguably common knowledge in the SE community, given the success of inference-time graph methods (LocAgent, RANGER, CodexGraph) versus the absence of successful training-time structural mining.

### Negative Result Paper Value

Negative results are valuable when they (a) challenge a widely held assumption with rigorous evidence, (b) prevent wasted future effort, or (c) provide mechanistic understanding of *why* something fails.

This paper partially delivers on all three:
- (a) The assumption being challenged---that hard negative mining helps code retrieval---is indeed held by practitioners, but the evidence base is thin. The paper corrects one specific prior work (CoCoHaNeRe) but only argumentatively (see Section 2 critique below). The broader NLP retrieval community already knows mining benefits are method- and scale-dependent.
- (b) The scaling law (-0.11pp/1K) could prevent practitioners from investing in mining infrastructure for code retrieval at production scales, which is useful.
- (c) The mechanistic understanding is adequate but shallow---the explanation (random sampling hits hard negatives by chance at scale) is intuitive and lacks formal backing.

### Scaling Law Importance

The -0.11pp/1K scaling law is the paper's most concrete contribution. However, several concerns limit its impact:
- It is derived from 4 data points (1K, 3K, 5K, 15K), which is insufficient for a robust "law."
- There are no confidence intervals on the individual data points or the slope.
- The "law" is reported for a single encoder (Qwen) on a single benchmark (SWE-smith validation). StarCoder results are not shown for the scaling analysis.
- Extrapolation beyond the 1K-15K range is speculative. Whether the trend holds at 50K+ or at 500 instances is unknown.
- Calling a linear fit to 4 points a "scaling law" overstates the finding. "Trend" or "correlation" would be more appropriate.

### Method Innovation

There is no method innovation. The paper tests existing techniques (random, embedding-distance, dataflow) and finds none works at scale. The CodeQL pipeline is an engineering contribution, not a methodological one. The paper does not propose any new mining strategy, loss function, or training technique.

---

## 2. Related Work Assessment

### Coverage

The related work section is **severely underdeveloped** for a paper positioned as a "systematic study." The entire section is 3 short paragraphs with 9 citations. For a 10-page analysis paper at a top venue, this is insufficient.

### Critical Gaps

**Missing foundational literature on evaluation methodology:**
- Henderson et al. (2018), "Deep Reinforcement Learning that Matters" --- directly relevant: shows seed variance dominates method differences
- Bouthillier et al. (2021), "Accounting for Variance in Machine Learning Benchmarks"
- Dodge et al. (2019), "Show Your Work: Improved Reporting of Experimental Results"
- Lucic et al. (2018), "Are GANs Created Equal?" --- same narrative: extensive evaluation reveals fragile rankings

These papers make exactly the same argument as this paper but in other domains. The paper reads as if it discovered multi-seed evaluation, when this is established best practice that has been formalized in multiple prior works.

**Missing hard negative mining theory:**
- Robinson et al. (2021), "Contrastive Learning with Hard Negative Samples" --- provides the theoretical framework for when hard negatives help vs. hurt, directly relevant to the scaling law finding
- Kalantidis et al. (2020), "Hard Negative Mixing for Contrastive Learning" --- analyzes the difficulty spectrum of negatives
- Chuang et al. (2020), "Debiased Contrastive Learning" --- false negative correction, relevant to the paper's false-hard-negative analysis in small repos

**Missing contrastive learning foundations:**
- SimCLR (Chen et al., 2020) --- temperature sensitivity analysis directly parallels this paper's temperature ablation
- MoCo (He et al., 2020) --- queue-based negatives, relevant to the static vs. dynamic mining discussion
- DPR (Karpukhin et al., 2020) --- mentioned in the literature map but not cited in the paper; its findings on BM25 negative scaling are directly relevant

**Missing code representation baselines:**
- CodeBERT (Feng et al., 2020), UniXcoder (Guo et al., 2022), CodeT5+ (Wang et al., 2023) --- standard code encoder baselines. The paper uses only 2 encoders; not citing alternatives weakens the discussion of encoder diversity.
- StarCoder (Li et al., 2023) --- the base model is used but the original paper is not cited.

**Missing structural code methods:**
- CodeGRAG (2024), GraphCoder (ASE 2024), RepoGraph (ICLR 2025), RANGER (2025) --- these are documented in the project's own `memory.md` with detailed comparison tables but are absent from the paper.

**Missing negative sampling in code:**
- ContraCode (Jain et al., 2021), SynCoBERT (Wang et al., 2021) --- code-specific contrastive learning papers that study augmentation-based negatives

### Differentiation from Prior Work

The paper's positioning relative to existing work has two problems:

1. **CoCoHaNeRe critique is central but unsubstantiated.** The paper's opening narrative is that CoCoHaNeRe "conflated BM25-proxy negatives with true embedding-distance negatives." This is presented as fact but never supported with: (a) specific textual evidence from CoCoHaNeRe showing the mislabeling, (b) a BM25 negative baseline in the paper's own experiments, or (c) reproduction of CoCoHaNeRe's setup. The critique is asserted, not demonstrated. For a paper whose entire motivation rests on "correcting" a prior work, this is a disqualifying gap.

2. **Positioning vs. evaluation methodology literature is absent.** The paper does not acknowledge that its central message---multi-seed evaluation reveals fragile conclusions---has been made before in multiple ML subfields. This makes the contribution appear less novel than it actually is. The code-specific application and the scaling law are the paper's unique angles, but without positioning against the broader methodology literature, the reader cannot assess what is new.

### Citation Count

9 citations for a 10-page analysis paper is far below the expected range (25-40 for a top venue). The literature map in the project's internal files documents 30+ relevant papers, most of which are absent from the paper. This is a significant presentation failure.

---

## 3. Writing and Presentation

### Framing

The "cautionary tale" framing is effective and appropriate for a negative result paper. The pilot-to-full-scale arc creates natural narrative tension. However:

- The title promises a story about "scale, seeds, and fragility" but the paper delivers primarily on "scale" (the scaling law). The "seeds" contribution is standard multi-seed evaluation, and "fragility" is a loaded word that the evidence only partially supports (the strategies are not fragile---they are simply ineffective at scale).
- The paper oscillates between two framings: (a) "mining doesn't help at scale" (a negative result about mining) and (b) "pilot evaluations are unreliable" (a methodological contribution about evaluation). These are related but distinct claims, and the paper would be stronger picking one as primary.

### Narrative Structure

The structure (Introduction -> Related Work -> Method -> Experiments -> Analysis -> Ablations -> Discussion -> Conclusion) is standard and functional. The Analysis section (Section 5) is the strongest part of the paper---the data scaling law, stratified analysis, pipeline audit, and failure taxonomy are all well-motivated and clearly presented. The Ablations section (Section 6) is comprehensive.

However, the Related Work section is too thin (see above), and the Introduction front-loads the pilot results before the reader has context to evaluate them.

### Tables vs. Figures

The paper has **14 tables and 0 figures** in the main text. This is a significant presentation weakness. The scaling law (Table 9) cries out for a line plot showing benefit decay. The per-seed results (Tables 2-3) would be far more impactful as box plots showing overlapping distributions. The failure taxonomy (Table 11) could be a Sankey diagram. The temperature interaction (Table 12) could be a heatmap.

The imagined experiment descriptions in the project files actually describe multiple figures (box plots, scatter plots, heatmaps, Sankey diagrams) that would significantly improve the paper but were not included. The all-tables-no-figures presentation makes the paper dense, hard to skim, and less compelling than it could be.

---

## 4. Impact on the Community

### Value for Code Retrieval Community

**Moderate.** The paper's core message---that hard negative mining may not help code retrieval at production scales---is useful for practitioners. However, the impact is limited by:
- The paper studies only 2 encoders at 3B parameters with LoRA fine-tuning. Whether the finding generalizes to full fine-tuning, larger models (7B, 13B), or encoder-only architectures is unknown.
- The training data (SWE-smith) represents a specific distribution of bug-fix tasks. Whether the finding extends to code search, code completion retrieval, or documentation retrieval is not tested.
- The effect sizes are small enough (<3pp) that the practical implications are ambiguous: even if mining helps by 1pp, the cost-benefit analysis depends on the application.

### Value for Contrastive Learning Community

**Low.** The paper does not connect to contrastive learning theory and does not propose any new technique. The scaling law (-0.11pp/1K) is specific to code retrieval and has no clear connection to broader contrastive learning principles.

### Practical Guidance

The paper provides clear practitioner advice: "for code retrieval with >5K training instances, investing in hard negative mining does not improve over random sampling." This is actionable but narrow. The advice about when to invest in structural mining (never, according to this paper) is potentially misleading if the finding is scale/encoder/data-specific.

### Open-Source CodeQL Pipeline

The pipeline achieves 0% timeout across 123 repos, which is an engineering achievement. However, its scientific value is undermined by the paper's own conclusion that structural negatives don't help. Open-sourcing a tool whose primary demonstrated use case fails is a contribution of limited practical value unless the community finds other applications (which the paper does not explore).

---

## 5. Weaknesses and Issues

### Major

1. **CoCoHaNeRe critique is the paper's raison d'etre but remains unverified (Critical).** The paper never runs BM25 negatives to demonstrate that BM25-proxy explains the prior harm result. Without this experiment, the "correcting a misconception" narrative collapses. The project's internal files show the CoCoHaNeRe critique originated from analyzing their own MVP implementation's BM25-proxy bug (D017), not from analyzing CoCoHaNeRe's code. The paper asserts a critique of another paper based on internal debugging of their own system.

2. **Related work is severely insufficient (Major).** 9 citations for a 10-page analysis paper. Missing: evaluation methodology literature (Henderson 2018, Dodge 2019, Bouthillier 2021), hard negative theory (Robinson 2021, Kalantidis 2020), contrastive learning foundations (SimCLR, MoCo, DPR), code representation baselines (CodeBERT, CodeT5+, StarCoder), and structural code methods (RepoGraph, RANGER, GraphCoder)---all documented in the project's own literature map but absent from the paper.

3. **"Scaling law" is overstated (Major).** A linear fit to 4 data points (1K, 3K, 5K, 15K) without confidence intervals or cross-encoder validation does not constitute a "law." The paper should present this as a trend or observation, not a quantitative law. The slope is reported to 2 decimal places (-0.11pp/1K) suggesting precision that 4 points cannot support.

4. **StarCoder2-3B is likely mischaracterized as architecturally distinct (Major).** The paper claims the two encoders are "architecturally distinct," but StarCoder2-3B is decoder-only (autoregressive), the same fundamental architecture as Qwen2.5-Coder-3B. They differ in pretraining data and training procedure, not architecture. This weakens the generalization claim.

5. **No error bars or CIs on RepoBench-R or SWE-smith validation results (Major).** The main results (Tables 2-3) show per-seed values but the summary statistics (mean +/- std) represent cross-seed variance. The RepoBench-R results (Table 6) appear to be single-checkpoint evaluations without any variance estimate. The paper's central argument is about seed variance dominating strategy effects, yet key results are reported without proper uncertainty quantification.

6. **Pool size of 50 is not discussed or ablated (Major).** All experiments use a pool of 50 candidate files per query, but real repositories have hundreds to thousands of files. Strategy rankings may change at realistic pool sizes. No sensitivity analysis is provided.

### Minor

7. **The paper has 14 tables and 0 figures.** This makes the paper extremely dense and the key findings (scaling law, seed variance) much harder to grasp visually than necessary.

8. **Qualitative examples promised in the experimental plan are absent from the paper.** The paper's structure lists no qualitative analysis section, though the project notes indicate this was planned and produced (with 3 positive, 4 negative, 3 neutral examples).

9. **Dataflow distance weighting receives only one sentence ("R@1 = 0.517, +0.2pp over binary, -0.6pp vs random") with no table.** This ablation deserves at least a small table for transparency.

10. **Checkpoint selection criterion is unspecified.** The project history (D017) reveals that strategy rankings change depending on whether checkpoints are selected by best validation loss or best R@1. This choice can reverse conclusions and must be stated.

11. **Neg difficulty quartile analysis is mentioned as planned but only briefly discussed.** Table 7 in the paper shows repo-size stratification but the neg_difficulty quartile analysis (documented in the project's experiment data) is absent. This stratification is more mechanistically informative.

12. **The 34% structural data coverage is underreported as a limitation.** Two-thirds of training instances receive no structural signal, meaning the dataflow strategy is effectively a mixture of random and structural mining. Stratified results (structured instances vs. fallback) are absent.

13. **No learning curves or overfitting analysis.** The project logs show severe overfitting (best at step 1000/4242), but the paper does not discuss this or show training dynamics. Strategy-specific overfitting patterns (e.g., does dataflow overfit faster?) are unexplored.

14. **"Open-source CodeQL pipeline" is claimed as a contribution but undermined by the paper's own conclusion that structural negatives don't help.** The pipeline's value depends on future applications that the paper does not explore.

---

## 6. Score and Rationale

### Score: 3/6 (Weak Reject)

**Rationale:**

The paper demonstrates above-average experimental discipline (54 runs, 9 seeds, bootstrap CIs, comprehensive ablations) and reports negative results with commendable honesty. The scaling law observation and pilot-to-full-scale discrepancy analysis are genuinely informative.

However, the paper has critical weaknesses that prevent acceptance at a top ML venue:

1. **The novelty is thin.** The central message (small-scale evaluations are unreliable, hard negative mining has diminishing returns at scale) is established knowledge in ML, and the paper fails to cite or position against the relevant methodology literature. The code-specific instantiation adds value, but not enough to carry a paper on its own.

2. **The related work is far below top-venue standards.** 9 citations in 3 paragraphs, missing entire categories of relevant literature that the project's own files document.

3. **The CoCoHaNeRe correction is unsubstantiated.** The paper's motivating claim is never empirically verified with a BM25 baseline.

4. **The "scaling law" is overfit to 4 data points.** Calling it a "law" without confidence intervals, cross-encoder validation, or theoretical backing is premature.

5. **Method contribution is nil.** The paper proposes nothing new---it tests existing approaches and finds they don't work. The engineering contribution (CodeQL pipeline) is undermined by the negative finding.

The paper is better than a desk reject---the experimental scale is genuine and the negative results are real. But it reads as a thorough project report rather than a paper with sufficient insight density for a top venue. The gap between the project's internal documentation (30+ papers mapped, detailed mechanistic analysis, multiple figure designs) and the submitted paper (9 citations, no figures, thin analysis layer) suggests the paper was rushed and significantly underserves the underlying research.

**Path to revision:** (a) Expand related work to 25+ citations with proper positioning against evaluation methodology and contrastive learning theory; (b) add a BM25 negative baseline to close the CoCoHaNeRe argument; (c) include 3-4 key figures (scaling law plot, seed-variance box plots, failure Sankey diagram); (d) present the scaling law with CIs and cross-encoder validation; (e) rename "scaling law" to "scaling trend"; (f) add stratified analysis by structural data availability.

### Confidence: 4/5

I have domain expertise in contrastive learning, code retrieval, and hard negative mining. I have examined the paper's claims against the project's internal experimental evidence, decision history, and literature map. My confidence is limited only by not having direct access to the full-scale experimental results (which are still in progress as of the review date) and by the possibility that the paper's bibliography issues are compilation artifacts rather than genuine missing citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18931be7-7aa5-484e-8a58-76756154aae9",
  "isSidechain": true,
  "agentId": "a9b7a4a9753d85f28",
  "requestId": "req_011Cb2AEmPdQzRJ5htRumavQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6ed2e98-ff63-4f23-8b62-ffef5fe452b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "1e25590a-d7ab-47a3-98ca-3305d32762c8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014eS3rWiu7N9WkKpUwiPCDk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32573,
      "cache_read_input_tokens": 83754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 32573,
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
