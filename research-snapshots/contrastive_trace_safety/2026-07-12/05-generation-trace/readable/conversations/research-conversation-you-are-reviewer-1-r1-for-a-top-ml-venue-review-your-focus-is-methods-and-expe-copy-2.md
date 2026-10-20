# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus is **Methods and Experiments**. Review the paper below usi

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 78
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a07c5538d1dec79e3.jsonl`
- **Structured JSON:** [`598982f418c17b9ffb4d.json`](../../sessions/59/598982f418c17b9ffb4d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

78 recorded events

### User

_source line 1 · 2026-05-14T08:24:27.743Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus is **Methods and Experiments**. Review the paper below using a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

**Title**: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"

**System name**: STRUCTFUSE

**Core claims**:
1. True embedding-distance hard negative mining consistently improves code retrieval over random baselines (+2.3pp R@1 on Qwen2.5-Coder-3B, +1.7pp on StarCoder2-3B; both p<0.01), correcting a prior misconception from CoCoHaNeRe.
2. Dataflow-aware negatives provide *conditional* additional benefit mediated by representation saturation — significant on Qwen (pos_sim=0.986, p=0.018) but not StarCoder (pos_sim=0.799, p=0.62).
3. Downstream SWE-bench Lite evaluation confirms retrieval improvements transfer (+2.3pp embedding, +3.3pp dataflow vs random resolve rate).

**Method**:
- 3 negative mining strategies: random, embedding-distance, dataflow-aware (using CodeQL inter-procedural call-graph, 2-hop connectivity)
- Dataflow-aware: select negatives that are textually similar (high embedding cosine) but NOT connected in the dataflow graph
- Contrastive loss with bi-encoder, LoRA rank-16, 3 epochs, 5K training instances from SWE-smith
- 2 encoders × 3 strategies × 9 seeds = 54 training runs
- CodeQL extraction on 131 SWE-smith repos, 123 valid, 0% timeout, Z%=78% at 2-hop (but paper also says 41% Z% — there's an inconsistency)

**Main Results (Tables)**:

Table 1 — Qwen 9-seed R@1:
- Random: 0.533 (std 0.008)
- Embedding: 0.556 (std 0.009), Δ=+2.3pp, p=0.003
- Dataflow: 0.548 (std 0.010), Δ=+1.5pp, p=0.018

Table 2 — StarCoder 9-seed R@1:
- Random: 0.490 (std 0.009)
- Embedding: 0.507 (std 0.010), p=0.008
- Dataflow: 0.488 (std 0.011), p=0.620

Table 3 — SWE-bench Lite resolve rate:
- Random: 22.7% (68/300)
- Embedding: 25.0% (75/300), +2.3pp
- Dataflow: 26.0% (78/300), +3.3pp

Table 4 — Bootstrap 95% CI for SWE-bench:
- Embed vs Random: +2.3pp, CI [0.4, 4.2], p=0.012
- Dataflow vs Random: +3.3pp, CI [0.5, 5.8], p=0.008
- Dataflow vs Embed: +1.0pp, CI [-0.8, 2.8], p=0.134

Table 5 — RepoBench-R: Random R@1=0.412, Embed=0.431, Dataflow=0.438

Table 6 — Stratified by repo size: Embed Δ peaks at large repos (+2.8pp), smallest at small repos (+0.8pp)

Table 7 — Temperature ablation (Qwen): Embed benefit robust (1.8-2.4pp across τ), Dataflow benefit strongest at low τ (+2.1 at 0.05, +0.9 at 0.2)

Table 8 — Hop distance: 2-hop optimal (R@1=0.548), 1-hop=0.541, 3-hop=0.544

Table 9 — Data scaling: Embed Δ constant at +2.3pp across 1K/3K/5K; Dataflow Δ decreases 2.0→1.5pp

Table 10 — Fusion head: Embed-only R@1=0.556, Structural-only=0.487, Combined=0.549

Table 11 — Static vs Dynamic mining: Static embed=0.556, Dynamic embed=0.561, at 2.8× cost

Table 12 — Binary vs weighted dataflow: Binary Qwen=0.548, Weighted=0.551 (negligible)

Table 13 — Failure analysis (50 instances): Dataflow helps 36% overall, 79% for cross-file dependency

Table 14 — Comparison with inference-time methods (conceptual, no empirical comparison)

**Experiment design reference (from review_context.yaml)**:
The full experiment plan includes all of the above experiments. Checking coverage: The paper covers ALL imagined experiments from the design document. Every experiment listed in the YAML appears in the paper.

## Your Review Task

Evaluate the following dimensions with detailed justification:

### 1. Methodological Soundness
- Is the experimental design rigorous? Are controls appropriate?
- Is the statistical methodology sound (9 seeds, bootstrap CIs, p-values)?
- Are there confounds or alternative explanations not addressed?
- Is the Z% inconsistency (78% vs 41%) a real issue?

### 2. Experimental Completeness
- Are ablations sufficient to support the claims?
- Are baselines adequate? What's missing?
- Is the downstream evaluation (SWE-bench Lite) convincing?

### 3. Reproducibility
- Is enough detail provided to reproduce?
- Are the CodeQL pipeline details sufficient?

### 4. Weaknesses
- Identify all methodological and experimental weaknesses
- Flag any concerns about effect sizes, statistical power, or generalizability

### 5. Questions for Authors

### 6. Score and Confidence

Output your review in structured format with all sections above. Be rigorous and specific. Cite table numbers when making claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "c8013443-ea75-482f-8b99-fd22a67e067e",
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

_source line 2 · 2026-05-14T08:24:27.749Z_

```json
{
  "parentUuid": "c8013443-ea75-482f-8b99-fd22a67e067e",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
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
  "uuid": "99718826-d87e-4f26-ac0c-b422f4507e4c",
  "timestamp": "2026-05-14T08:24:27.749Z",
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

_source line 3 · 2026-05-14T08:24:30.562Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99718826-d87e-4f26-ac0c-b422f4507e4c",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29772EiNpXuZaym8pJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5657ae34-7a1d-4e63-bd18-df425a245df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fBxuPjr52jYh81eFJQUGX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15608,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15608,
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

_source line 4 · 2026-05-14T08:24:31.094Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WuT2t1pQPEo6Xgoycdxt6a`</summary>

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
  "parentUuid": "5657ae34-7a1d-4e63-bd18-df425a245df3",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29772EiNpXuZaym8pJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "762077c5-0137-44d8-84fc-375cbd44f44c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fBxuPjr52jYh81eFJQUGX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15608,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15608
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15608,
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

_source line 5 · 2026-05-14T08:24:31.101Z_

<details><summary>↩ Tool result · `toolu_01WuT2t1pQPEo6Xgoycdxt6a`</summary>

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
  "parentUuid": "762077c5-0137-44d8-84fc-375cbd44f44c",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "2ed148bd-040b-408c-9980-a01bdad3a22f",
  "sourceToolAssistantUUID": "762077c5-0137-44d8-84fc-375cbd44f44c",
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

_source line 6 · 2026-05-14T08:24:34.314Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_014xYR3tuB6dVV2znfHt5Es1`</summary>

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
  "parentUuid": "2ed148bd-040b-408c-9980-a01bdad3a22f",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb297Mkm4BcZUkjEdEVg2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2a8601f-996d-40ab-a05a-af76f4d36105",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKm7adWbqsLr2ryNPUEvKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T08:24:34.417Z_

<details><summary>↩ Tool result · `toolu_014xYR3tuB6dVV2znfHt5Es1`</summary>

```text
{"result":"# 项目 structfuse-context 概况\n\n## 实验状态 (31 个)\n\n- **p2b_eval_4runs_pool50**: DONE (success) — \n- **d007_50repo_overlap**: DONE (success) — \n- **p2b_5reruns**: DONE (success) — \n- **p2b_eval_4runs_v2**: DONE (success) — \n- **p2b-all-9runs**: DONE (killed) — \n- **p2b-smoke8**: DONE (killed) — \n- **p2b-smoke7**: DONE (killed) — \n- **p2b-smoke6**: DONE (killed) — \n- **p2b-smoke5**: DONE (killed) — \n- **p2b-smoke4**: DONE (killed) — \n- **p2b-smoke3**: DONE (killed) — \n- **p2b-smoke2**: DONE (killed) — \n- **p2b-smoke-test**: DONE (killed) — \n- **mvp_p2a_linear_proxy**: DONE (success) — \n- **mvp_p1_codeql_feasibility**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\n- **m1_extraction** (success): —\n\n## 趋势\n成功 10 / 负向 2 / 失败 2 / 共 28\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-42106: 无 GPU 信息\n\n## 告警\n- p2b-smoke-test: 已被终止 — unknown\n- p2b-smoke2: 已被终止 — unknown\n- p2b-smoke3: 已被终止 — unknown\n- p2b-smoke4: 已被终止 — unknown\n- p2b-smoke5: 已被终止 — unknown\n- p2b-smoke6: 已被终止 — unknown\n- p2b-smoke7: 已被终止 — unknown\n- p2b-smoke8: 已被终止 — unknown\n- p2b-all-9runs: 已被终止 — unknown\n- mvp_p2b_contrastive_training: 已被终止 — unknown\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\n- p2b_eval_all: 已被终止 — unknown\n- m2_early_pilot: 已被终止 — unknown\n- m2_early_pilot_v2: 训练失败 — unknown\n- m2_early_pilot_v3: 已被终止 — unknown\n- m1_reextract: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2a8601f-996d-40ab-a05a-af76f4d36105",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "c6881c46-08b5-4da3-8ca9-5357617c53ce",
  "sourceToolAssistantUUID": "a2a8601f-996d-40ab-a05a-af76f4d36105",
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

_source line 8 · 2026-05-14T08:24:34.776Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H1pvMzGqa69ftGgPUVhAcQ`</summary>

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
  "parentUuid": "c6881c46-08b5-4da3-8ca9-5357617c53ce",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb297Mkm4BcZUkjEdEVg2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "955056ce-d050-43ec-840d-160d23dbe838",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WKm7adWbqsLr2ryNPUEvKK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15608,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 160,
          "cache_read_input_tokens": 15608,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1448,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T08:24:34.791Z_

<details><summary>↩ Tool result · `toolu_01H1pvMzGqa69ftGgPUVhAcQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n- **m1_extraction** (success): —\\n\\n## 趋势\\n成功 10 / 负向 2 / 失败 2 / 共 28\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 1895, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "955056ce-d050-43ec-840d-160d23dbe838",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "acdb14a3-b407-4de1-868a-0bfb891a299d",
  "sourceToolAssistantUUID": "955056ce-d050-43ec-840d-160d23dbe838",
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

_source line 10 · 2026-05-14T08:24:37.630Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01J97pmQmRQWx1NEnCVEeC2n`</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acdb14a3-b407-4de1-868a-0bfb891a299d",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb297dLt6mCFGkMzhaTj5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb0b62a6-f470-4f5c-8b00-33c1576064c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUcRZ17K1RTd5wJYYWrCmr",
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

_source line 11 · 2026-05-14T08:24:37.638Z_

<details><summary>↩ Tool result · `toolu_01J97pmQmRQWx1NEnCVEeC2n`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb0b62a6-f470-4f5c-8b00-33c1576064c9",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "af1017aa-8696-46bb-bbd6-f39d7e8aad27",
  "sourceToolAssistantUUID": "eb0b62a6-f470-4f5c-8b00-33c1576064c9",
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

_source line 12 · 2026-05-14T08:24:38.601Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G5WVhSVStawu1tACEqXZy2`</summary>

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
  "parentUuid": "af1017aa-8696-46bb-bbd6-f39d7e8aad27",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb297dLt6mCFGkMzhaTj5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "772be6ac-28e1-45a1-b968-88c3d4466a89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUcRZ17K1RTd5wJYYWrCmr",
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

_source line 13 · 2026-05-14T08:24:38.612Z_

<details><summary>↩ Tool result · `toolu_01G5WVhSVStawu1tACEqXZy2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 28\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n\", \"total_chars\": 20054, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "772be6ac-28e1-45a1-b968-88c3d4466a89",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "589d15f0-4311-4a0e-b345-0189690213bb",
  "sourceToolAssistantUUID": "772be6ac-28e1-45a1-b968-88c3d4466a89",
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

_source line 14 · 2026-05-14T08:24:39.539Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GeCYz8ZJaezXhuLo3gMmm2`</summary>

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
  "parentUuid": "589d15f0-4311-4a0e-b345-0189690213bb",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb297dLt6mCFGkMzhaTj5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "608976ad-58b9-4a0b-abf2-483ad8df52c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUcRZ17K1RTd5wJYYWrCmr",
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

_source line 15 · 2026-05-14T08:24:39.550Z_

<details><summary>↩ Tool result · `toolu_01GeCYz8ZJaezXhuLo3gMmm2`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "608976ad-58b9-4a0b-abf2-483ad8df52c3",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "d68f71c9-a3cb-4eab-9ecc-c75f2cd9c306",
  "sourceToolAssistantUUID": "608976ad-58b9-4a0b-abf2-483ad8df52c3",
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

_source line 16 · 2026-05-14T08:24:39.759Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014kuLgm7oJVpSkh8pQ9Zyxz`</summary>

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
  "parentUuid": "d68f71c9-a3cb-4eab-9ecc-c75f2cd9c306",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb297dLt6mCFGkMzhaTj5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1015aa15-36e4-4a45-932e-dfc91c97d7f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UUcRZ17K1RTd5wJYYWrCmr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 17056,
      "output_tokens": 377,
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
          "output_tokens": 377,
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

_source line 17 · 2026-05-14T08:24:39.769Z_

<details><summary>↩ Tool result · `toolu_014kuLgm7oJVpSkh8pQ9Zyxz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); heavy inference cost |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | Repository-level Graph for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2025) | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (2025) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献\\n\\n- CodexGraph: arXiv:2408.03910, NAACL 2025\\n- LocAgent: arXiv:2503.09089, ACL 2025\\n- RANGER: arXiv:2509.25257, 2025\\n- RepoGraph: arXiv:2410.14684, ICLR 2025\\n- GraphCoder: arXiv:2406.07003, ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, 2025\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\", \"total_chars\": 8062, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1015aa15-36e4-4a45-932e-dfc91c97d7f3",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "bb83853a-5dd7-41dd-8ef0-e748e58f9305",
  "sourceToolAssistantUUID": "1015aa15-36e4-4a45-932e-dfc91c97d7f3",
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

_source line 18 · 2026-05-14T08:24:43.579Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01S2ajLPiXARZW5gSF3RhuBA`</summary>

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
  "parentUuid": "bb83853a-5dd7-41dd-8ef0-e748e58f9305",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb297zmEfuJNPaKN6krxG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b50425c-5f52-4d71-bffe-c60748e6b147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012J8YLyd58ofwQNhkNc1xma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13882,
      "cache_read_input_tokens": 19767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13882,
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

_source line 19 · 2026-05-14T08:24:43.589Z_

<details><summary>↩ Tool result · `toolu_01S2ajLPiXARZW5gSF3RhuBA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \\\"harm\\\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\\n\\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\\n\\n- **Headline result template**: \\\"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\\\"\\n- Backup: \\\"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\\n- m1_reextract_v2: expanded extraction for higher coverage\\n\\n### Planned (priority order):\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark\\n- plan_015: Dynamic mining baseline\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 9391, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b50425c-5f52-4d71-bffe-c60748e6b147",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "6faea0f2-4aa9-4685-adec-c398845ca44a",
  "sourceToolAssistantUUID": "6b50425c-5f52-4d71-bffe-c60748e6b147",
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

_source line 20 · 2026-05-14T08:24:44.666Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019gxWZZ6AUoYkXiJoany6Np`</summary>

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
  "parentUuid": "6faea0f2-4aa9-4685-adec-c398845ca44a",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb297zmEfuJNPaKN6krxG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "913ca206-c6e3-4851-863e-b6ebe33ef22a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012J8YLyd58ofwQNhkNc1xma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13882,
      "cache_read_input_tokens": 19767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13882,
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

_source line 21 · 2026-05-14T08:24:44.679Z_

<details><summary>↩ Tool result · `toolu_019gxWZZ6AUoYkXiJoany6Np`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "913ca206-c6e3-4851-863e-b6ebe33ef22a",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "f1fc4231-8dfb-4eb4-9984-abcd8cf6d723",
  "sourceToolAssistantUUID": "913ca206-c6e3-4851-863e-b6ebe33ef22a",
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

_source line 22 · 2026-05-14T08:24:45.047Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012wSCnujbZP2mneXHiRmo6U`</summary>

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
  "parentUuid": "f1fc4231-8dfb-4eb4-9984-abcd8cf6d723",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb297zmEfuJNPaKN6krxG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62ea3f7d-6924-4cd4-a4a5-a3cbc1ffab6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012J8YLyd58ofwQNhkNc1xma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13882,
      "cache_read_input_tokens": 19767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13882,
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

_source line 23 · 2026-05-14T08:24:45.058Z_

<details><summary>↩ Tool result · `toolu_012wSCnujbZP2mneXHiRmo6U`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\", \"content\": \"# StructFuse — Research Dashboard\\n\\n> 最后更新: 2026-05-14 01:47 UTC | 更新原因: Reviewer warnings 落地: m1_reextract_v2 定位明确 (camera-ready not current submission), plan_015/017 写作处理方案, experiment_plan 更新待排\\n\\n## 核心方向\\n\\\"Hard negative mining for code retrieval: what works, what doesn't, and why\\\" — 系统性分析 + 机制解释论文。详见 paper_framing.md（D024 重写后）。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **Framing 重写完成 (D024)**: 旧 Claim 2 (\\\"embedding harms\\\") 已证伪并移除；新叙事线：embedding universally helps → dataflow conditionally helps → mechanistic explanation via representation saturation\\n- **Full M2 训练中**: Qwen random_s42 running (best R@1=55.3% @step1000, overfitting @1500); StarCoder random_s42 running (R@1=45.4% @step1000, still improving)\\n- **M1 reextract v2 进行中**: 4 workers 并行 CodeQL 提取，~13% 进度\\n- **Plan_003 SWE-bench eval**: Pipeline ready (dry-run v2 PASS), 等 M2 checkpoint\\n- **Plan_014 temp ablation**: 脚本 D025 缩减完成 (6 runs, ~70h), 等 M2 释放 GPU\\n\\n## 近期任务\\n- [ ] 等 Qwen eval@2000 → 确认过拟合 → 剩余 8 seeds 减至 2 epochs (节省 ~48h/GPU)\\n- [ ] neg_difficulty 可视化 Figure（0 GPU-h，论文核心差异化图表）— 已派 Agent\\n- [ ] M2 full 18 runs 完成 → 统计检验 (bootstrap CI, paired t-test)\\n- [ ] M2 完成后: plan_014 temperature ablation (双卡 ~35h wall time)\\n- [ ] M2 Qwen best checkpoint → plan_003 SWE-bench Lite eval\\n- [ ] plan_004 RepoBench-R 第二 benchmark\\n- [ ] experiment_plan.yaml 更新: plan_002/013 关联 full M2 registry_id, plan_014 budget 修正\\n- [ ] 写作时: plan_015 (dynamic mining) → Limitation 段落; plan_017 (inference-time graph) → Discussion 段落 (0 GPU-h)\\n\\n## Go/No-Go 阈值 (D019/D020, 适配 D024 新 framing)\\n\\n**Claim 1 (embedding vs random)**: 预期 Go — pilot 已一致确认 (+1.6~2.0pp)。Full M2 提供 3-seed CI。\\n**Claim 2 (dataflow conditional benefit)**: 预期 Conditional Go — Qwen 正向、StarCoder 中性。Full M2 量化 interaction effect。\\n**n=3 功效限制**: df=2, Type II error 高。Discussion 必须讨论。\\n\\n## GPU 预算\\n- **bjb1-42106**: 2× RTX PRO 6000 96GB（专属）\\n  - cuda:0: m2_full_qwen (seed 1/9, step ~1550/4242)\\n  - cuda:1: m2_full_starcoder (seed 1/9, step ~1000/4242)\\n- **剩余**: ~140 GPU-h needed for plan_003/014/004/015 | 瓶颈是 M2 完成时间非总量\\n- **过拟合缩减**: 若 eval@2000 确认，2 epochs 节省 ~96h 总计，M2 约 May 18-19 完成（vs May 20-21）\\n\\n## m1_reextract_v2 定位\\n当前 M2 使用 15.9K structural data 训练。reextract_v2 完成后数据量预计 ~30K+，但 May 25 前无法重跑 M2（~200+ GPU-h）。**用途：camera-ready revision 或后续投稿的 scalability 证据**，不影响当前投稿关键路径。当前价值：Claim 3 (CodeQL scalability) 的 coverage 数字更新。\\n\\n## 关键风险\\n1. **ARR deadline May 25**: 关键路径 M2(~May 18) → plan_014(~May 19.5) → plan_003(~May 21) → 统计+初稿(~May 24)\\n2. **n=3 统计功效**: pilot <2pp 差异在 df=2 下极难显著\\n3. **plan_015 未做**: static vs dynamic mining confound 由 2/3 dream reviewers 提出，需 Limitation 段承认\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D027 | 2026-05-14 | M2 剩余 runs 加 early stopping (patience=2 evals)，加速关 | m2_full_qwen, m2_full_starcoder |\\n| D026 | 2026-05-14 | Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 ep | m2_full_qwen, m2_full_starcoder |\\n| D025 | 2026-05-14 | Plan_014 temperature ablation 缩减为 2 strategies × 3 | m2_full_qwen, plan_014 |\\n| D024 | 2026-05-14 | Major paper framing rewrite: drop falsified \\\"embed | m2_embed_verify, plan_013_starcoder, neg_difficulty_analysis |\\n| D023 | 2026-05-13 | Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重 | m1_reextract |\\n| D022 | 2026-05-13 | M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M | m1_extraction, plan_006_scalability |\\n| D021 | 2026-05-13 | Negative difficulty 分析揭示 encoder capacity 差异是 data | m2_embed_verify, plan_013_starcoder |\\n| D020 | 2026-05-13 | D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明 | m2_full_qwen, m2_full_starcoder |\\n| D019 | 2026-05-13 | D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案 | m2_full_qwen, m2_full_starcoder |\\n| D018 | 2026-05-13 | 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯 | m2_embed_verify, plan_013_starcoder |\\n\\n\", \"total_chars\": 3742, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62ea3f7d-6924-4cd4-a4a5-a3cbc1ffab6c",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "4b216227-9a9a-4e0d-843a-5c51537e1049",
  "sourceToolAssistantUUID": "62ea3f7d-6924-4cd4-a4a5-a3cbc1ffab6c",
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

_source line 24 · 2026-05-14T08:24:45.644Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SD6z1X859LQYLu7S3kVVGM`</summary>

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
  "parentUuid": "4b216227-9a9a-4e0d-843a-5c51537e1049",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb297zmEfuJNPaKN6krxG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd4227e1-b87b-4ede-8ec5-5dc2d25c8d8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012J8YLyd58ofwQNhkNc1xma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13882,
      "cache_read_input_tokens": 19767,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13882
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 19767,
          "cache_creation_input_tokens": 13882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13882,
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

_source line 25 · 2026-05-14T08:24:45.653Z_

<details><summary>↩ Tool result · `toolu_01SD6z1X859LQYLu7S3kVVGM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd4227e1-b87b-4ede-8ec5-5dc2d25c8d8a",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "418d7d09-bec4-4ada-ae60-913dafed7e65",
  "sourceToolAssistantUUID": "bd4227e1-b87b-4ede-8ec5-5dc2d25c8d8a",
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

_source line 26 · 2026-05-14T08:24:48.891Z_

Now let me look at the artifacts directory and any experiment configuration files for deeper understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "418d7d09-bec4-4ada-ae60-913dafed7e65",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb298T2J2oDWbxk9v2ifL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2511d53a-c460-48c1-8527-730161fd94ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dv6XZzNxeXWPThAQ2QbkFu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5539,
      "cache_read_input_tokens": 33649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5539,
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

_source line 27 · 2026-05-14T08:24:49.851Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YL8AQw7buf3PBSCdJ4eeiS`</summary>

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
  "parentUuid": "2511d53a-c460-48c1-8527-730161fd94ce",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb298T2J2oDWbxk9v2ifL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a17a17c-7b9e-4df2-9ece-e6ba96f33c64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dv6XZzNxeXWPThAQ2QbkFu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5539,
      "cache_read_input_tokens": 33649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5539,
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

_source line 28 · 2026-05-14T08:24:49.871Z_

<details><summary>↩ Tool result · `toolu_01YL8AQw7buf3PBSCdJ4eeiS`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a17a17c-7b9e-4df2-9ece-e6ba96f33c64",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "3ee3872a-d398-4948-a5ea-13b9edba0151",
  "sourceToolAssistantUUID": "1a17a17c-7b9e-4df2-9ece-e6ba96f33c64",
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

_source line 29 · 2026-05-14T08:24:50.139Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019j4YiUSss58ZFYNrhWTzLu`</summary>

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
  "parentUuid": "3ee3872a-d398-4948-a5ea-13b9edba0151",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb298T2J2oDWbxk9v2ifL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86fcaedc-d4b1-45ab-b643-d9b53fcfb59a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dv6XZzNxeXWPThAQ2QbkFu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5539,
      "cache_read_input_tokens": 33649,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5539
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 33649,
          "cache_creation_input_tokens": 5539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5539,
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

_source line 30 · 2026-05-14T08:24:50.161Z_

<details><summary>↩ Tool result · `toolu_019j4YiUSss58ZFYNrhWTzLu`</summary>

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
  "parentUuid": "86fcaedc-d4b1-45ab-b643-d9b53fcfb59a",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "7cac0e3b-880b-43a2-80d3-05bf0af60ea7",
  "sourceToolAssistantUUID": "86fcaedc-d4b1-45ab-b643-d9b53fcfb59a",
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

_source line 31 · 2026-05-14T08:24:54.499Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YMMBR8pje8NE4NCdSTBAYf`</summary>

```json
{
  "project": "structfuse-context",
  "file": "experiment_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cac0e3b-880b-43a2-80d3-05bf0af60ea7",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb298kynzory6t3Y6xk1N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a5019e8-0d12-4a84-8ab3-0b48c36b1239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6gj5P4oB1NBXd87stLaz7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2291,
      "cache_read_input_tokens": 39188,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2291,
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

_source line 32 · 2026-05-14T08:24:54.528Z_

<details><summary>↩ Tool result · `toolu_01YMMBR8pje8NE4NCdSTBAYf`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a5019e8-0d12-4a84-8ab3-0b48c36b1239",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "233a14db-e0dd-4c7b-8468-0b2ccd7ceeed",
  "sourceToolAssistantUUID": "5a5019e8-0d12-4a84-8ab3-0b48c36b1239",
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

_source line 33 · 2026-05-14T08:24:54.721Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0181KyGLiuV12Qp3uebuUZd5`</summary>

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
  "parentUuid": "233a14db-e0dd-4c7b-8468-0b2ccd7ceeed",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb298kynzory6t3Y6xk1N",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c17dda07-3dfd-46ad-9dd2-74af848ed73d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6gj5P4oB1NBXd87stLaz7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2291,
      "cache_read_input_tokens": 39188,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 39188,
          "cache_creation_input_tokens": 2291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2291,
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

_source line 34 · 2026-05-14T08:24:54.734Z_

<details><summary>↩ Tool result · `toolu_0181KyGLiuV12Qp3uebuUZd5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-12\\n# 说明: 只收录项目文件中已引用的 + 确定存在的知名论文。不确定的信息标注\\\"需验证\\\"。\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline  # StructFuse 的评估基准\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Karthik Narasimhan, Ofir Press\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: building-block  # StructFuse 用其 repo 做数据提取\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n        note: \\\"需验证 venue（可能已投稿会议）\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务，StructFuse 可用于评估。\\\"\\n        note: \\\"需验证年份和 venue\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及代码领域的对比学习\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式，是 StructFuse 对比训练的方法论基础。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，是 StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"SimCLR: A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Mining Hard Negatives with Curriculum for Dense Retrieval\\\"\\n        authors: \\\"需验证\\\"\\n        venue: \\\"需验证\\\"\\n        year: \\\"需验证\\\"\\n        relation: background\\n        summary: \\\"课程学习式 hard negative 挖掘，从易到难训练检索器。\\\"\\n        note: \\\"需验证完整信息\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block  # StructFuse 核心组件\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: EMNLP (Findings)\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: background\\n        summary: \\\"大规模开源代码 LLM，广泛用于代码嵌入的 backbone。\\\"\\n        note: \\\"需验证 venue（可能是 arXiv 或其他）\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Qwen Team (Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block  # StructFuse 用 Qwen2.5-Coder-3B 做检索器\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n        note: \\\"需验证确切标题和年份\\\"\\n\\n      - title: \\\"Contrastive Learning for Source Code with Structural and Functional Properties\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: ACL (Findings)\\n        year: 2022\\n        relation: background\\n        summary: \\\"代码对比学习中利用结构/功能属性构建正负样本对。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。Phase 2a 实验发现 BM25 在 bug fixing 定位中可能有误导性（负系数）。\\\"\\n\\n# ==========================================================================\\n# 待补充\\n# ==========================================================================\\n# 以下论文可能相关，待确认后补充：\\n# - FAISS (Johnson et al., 2019) — ANN 检索库，StructFuse 评估可能用到\\n# - Tree-sitter — 增量解析器，与 CodeQL 互补\\n# - Aider / Moatless Tools — SWE-bench 上的其他代码检索方法\\n# - CoSQA (Huang et al., 2021) — 代码搜索 QA 数据集\\n# - DeepSeek-Coder — 另一个可能的 backbone 对比\\n\", \"total_chars\": 9647, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c17dda07-3dfd-46ad-9dd2-74af848ed73d",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "c53adb0e-d863-45a6-be0c-4c5b5ed32004",
  "sourceToolAssistantUUID": "c17dda07-3dfd-46ad-9dd2-74af848ed73d",
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

_source line 35 · 2026-05-14T08:24:58.414Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FPMw3bDeXXvaNMYXUPrjR8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c53adb0e-d863-45a6-be0c-4c5b5ed32004",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb2996eUSzeRuBwq7NPFx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af9157f1-bcdb-4d17-b39c-8f702008ec82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CufM9NNh1UMWHs437wRbk2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4689,
      "cache_read_input_tokens": 41479,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 41479,
          "cache_creation_input_tokens": 4689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4689,
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

_source line 36 · 2026-05-14T08:24:58.421Z_

<details><summary>↩ Tool result · `toolu_01FPMw3bDeXXvaNMYXUPrjR8`</summary>

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
  "parentUuid": "af9157f1-bcdb-4d17-b39c-8f702008ec82",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "95cb59f6-a385-4013-8b83-16db4cfd1f30",
  "sourceToolAssistantUUID": "af9157f1-bcdb-4d17-b39c-8f702008ec82",
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

_source line 37 · 2026-05-14T08:25:01.761Z_

Now let me read the latest dream review report and the review context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95cb59f6-a385-4013-8b83-16db4cfd1f30",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb299NViPMigpz6daCqXG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37a9769b-7ac8-4ac8-bf3d-048d95e6097d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLzJEGAGfTeYtySivPAv1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2045,
      "cache_read_input_tokens": 46168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2045,
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

_source line 38 · 2026-05-14T08:25:03.186Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UANwv53fBvrHHRDX1VhSog`</summary>

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
  "parentUuid": "37a9769b-7ac8-4ac8-bf3d-048d95e6097d",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb299NViPMigpz6daCqXG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b55aa9e-eac2-4d33-8791-c5296a4df2de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLzJEGAGfTeYtySivPAv1F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2045,
      "cache_read_input_tokens": 46168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2045,
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

_source line 39 · 2026-05-14T08:25:03.532Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016znHGz825aYeYaxck8hvHy`</summary>

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
  "parentUuid": "5b55aa9e-eac2-4d33-8791-c5296a4df2de",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb299NViPMigpz6daCqXG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10ec39be-c687-4111-8844-2e66e2409c3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLzJEGAGfTeYtySivPAv1F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2045,
      "cache_read_input_tokens": 46168,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2045
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 46168,
          "cache_creation_input_tokens": 2045,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2045,
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

_source line 40 · 2026-05-14T08:25:03.576Z_

<details><summary>↩ Tool result · `toolu_01UANwv53fBvrHHRDX1VhSog`</summary>

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
  "parentUuid": "5b55aa9e-eac2-4d33-8791-c5296a4df2de",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "5ecc5170-6f1e-4758-9a3c-e4c3a5fa72b4",
  "sourceToolAssistantUUID": "5b55aa9e-eac2-4d33-8791-c5296a4df2de",
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

### Tool result

_source line 41 · 2026-05-14T08:25:03.549Z_

<details><summary>↩ Tool result · `toolu_016znHGz825aYeYaxck8hvHy`</summary>

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
  "parentUuid": "10ec39be-c687-4111-8844-2e66e2409c3c",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "ab242e5f-a677-4f43-b56a-54a6a98d92c1",
  "sourceToolAssistantUUID": "10ec39be-c687-4111-8844-2e66e2409c3c",
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

_source line 42 · 2026-05-14T08:25:06.353Z_

Let me read the best-case paper tex and the review log to understand the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab242e5f-a677-4f43-b56a-54a6a98d92c1",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb299kKdPNWPj3UKm6C2f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9f44f01-e864-40fc-b41d-7dd0766acb7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MhPKH5sbo9Nszd6QguS7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14191,
      "cache_read_input_tokens": 48213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14191,
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

_source line 43 · 2026-05-14T08:25:07.947Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C74kk6YCNPZtpatYZi1YGQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9f44f01-e864-40fc-b41d-7dd0766acb7f",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb299kKdPNWPj3UKm6C2f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2099d53a-6370-4765-8c34-531e66b4f38a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019MhPKH5sbo9Nszd6QguS7T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14191,
      "cache_read_input_tokens": 48213,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14191
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 48213,
          "cache_creation_input_tokens": 14191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14191,
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

_source line 44 · 2026-05-14T08:25:07.952Z_

<details><summary>↩ Tool result · `toolu_01C74kk6YCNPZtpatYZi1YGQ`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2099d53a-6370-4765-8c34-531e66b4f38a",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "29324a4a-cb55-424c-8a22-913b12d42ede",
  "sourceToolAssistantUUID": "2099d53a-6370-4765-8c34-531e66b4f38a",
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

_source line 45 · 2026-05-14T08:25:12.438Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Peysy69GxcYCNaJJaDjCgZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29324a4a-cb55-424c-8a22-913b12d42ede",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29A57UmeKqPpCBa3DaA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7ee9d17-ef77-4113-9b0c-053eafbf4e8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016AGegsEvV54FJ6hhzdcegb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6710,
      "cache_read_input_tokens": 62404,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6710
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 62404,
          "cache_creation_input_tokens": 6710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6710,
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

_source line 46 · 2026-05-14T08:25:12.478Z_

<details><summary>↩ Tool result · `toolu_01Peysy69GxcYCNaJJaDjCgZ`</summary>

```text
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
  "parentUuid": "e7ee9d17-ef77-4113-9b0c-053eafbf4e8e",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "1e4e9a97-d802-4ed3-830c-4566879704e8",
  "sourceToolAssistantUUID": "e7ee9d17-ef77-4113-9b0c-053eafbf4e8e",
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

_source line 47 · 2026-05-14T08:25:15.195Z_

Now let me check the actual experiment code and the review log for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e4e9a97-d802-4ed3-830c-4566879704e8",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29AQWHwC727rr1wygrw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "178d320e-0d05-40b8-9c70-78e6d79227e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017eoT1Hvfhq9KqyrqVS227G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2608,
      "cache_read_input_tokens": 69114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2608,
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

_source line 48 · 2026-05-14T08:25:15.903Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NRGmAk3rhn2ATDndgXYrAg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/logs/review_best.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "178d320e-0d05-40b8-9c70-78e6d79227e0",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29AQWHwC727rr1wygrw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af7592be-dc01-499f-9179-05b770099a74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017eoT1Hvfhq9KqyrqVS227G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2608,
      "cache_read_input_tokens": 69114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2608,
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

_source line 49 · 2026-05-14T08:25:15.911Z_

<details><summary>↩ Tool result · reported error · `toolu_01NRGmAk3rhn2ATDndgXYrAg`</summary>

```text
File content (845KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af7592be-dc01-499f-9179-05b770099a74",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "2f7ac8bc-e27a-43a6-90e9-93f6b1d05349",
  "toolUseResult": "Error: File content (845KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "af7592be-dc01-499f-9179-05b770099a74",
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

_source line 50 · 2026-05-14T08:25:16.537Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RV7cHVCxwGJBmJzGtoq6HF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f7ac8bc-e27a-43a6-90e9-93f6b1d05349",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29AQWHwC727rr1wygrw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b547124-4446-4802-b111-0a1249c108b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017eoT1Hvfhq9KqyrqVS227G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2608,
      "cache_read_input_tokens": 69114,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2608
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 69114,
          "cache_creation_input_tokens": 2608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2608,
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

_source line 51 · 2026-05-14T08:25:16.542Z_

<details><summary>↩ Tool result · `toolu_01RV7cHVCxwGJBmJzGtoq6HF`</summary>

```text
1	[
2	  {
3	    "name": "SWE-bench Lite End-to-End Evaluation",
4	    "description": "3 strategies × best checkpoint on SWE-bench Lite (300), Qwen3.6-27B agent, 测 resolve rate",
5	    "results": {
6	      "random_resolve_rate": 0.227,
7	      "embedding_distance_resolve_rate": 0.25,
8	      "dataflow_aware_resolve_rate": 0.26,
9	      "embed_vs_random_delta_pp": 2.3,
10	      "dataflow_vs_random_delta_pp": 3.3,
11	      "dataflow_vs_embed_delta_pp": 1.0,
12	      "total_instances": 300,
13	      "instances_resolved_random": 68,
14	      "instances_resolved_embed": 75,
15	      "instances_resolved_dataflow": 78,
16	      "retrieval_recall1_random": 0.533,
17	      "retrieval_recall1_embed": 0.556,
18	      "retrieval_recall1_dataflow": 0.548
19	    },
20	    "tables": [
21	      {
22	        "caption": "SWE-bench Lite Resolve Rate by Retrieval Strategy",
23	        "columns": [
24	          "Strategy",
25	          "Resolve_Rate",
26	          "Delta_vs_Random",
27	          "Instances_Resolved"
28	        ],
29	        "rows": [
30	          [
31	            "random",
32	            "22.7%",
33	            "—",
34	            68
35	          ],
36	          [
37	            "embedding_distance",
38	            "25.0%",
39	            "+2.3pp",
40	            75
41	          ],
42	          [
43	            "dataflow_aware",
44	            "26.0%",
45	            "+3.3pp",
46	            78
47	          ]
48	        ]
49	      }
50	    ],
51	    "figures": [],
52	    "analysis": "Resolve rate 提升确认 retrieval 质量改善能传导到实际软件工程任务。Dataflow 策略独立解决了 5 个 random/embed 均失败的 instance（多为跨文件 dataflow 依赖），支持 Claim 2 的条件性收益叙事。 Embed 策略独立解决 3 个（多为同文件内近义函数混淆），支持 Claim 1。\n\n\nbest 档下 retrieval 质量提升能传导到下游 resolve rate。Qwen best checkpoint embedding R@1≈0.556 vs random 0.533， 差值 2.3pp 在 300 实例上对应约 7 个额外正确 retrieval → 其中部分转化为 resolve。 转化率不是 1:1（retrieval 改善不等于 repair 改善，LLM agent 有自身能力上限）， 但 best 档假设转化效率约 30-40%，即 ~7 个额外正确 retrieval 中约 2-3 个转为 resolve。 Dataflow 在 Qwen 上的条件性收益（pilot +0.8pp R@1）进一步贡献约 1pp resolve delta。 总体 swebench_resolve_delta_pp 落在 [2.0, 5.0] 范围的中低段， 因为 retrieval → repair 的衰减是系统性的。SWE-bench Lite 300 实例规模下， 2-3pp 差异虽小但在 best 档下 bootstrap CI 可检测。\n"
53	  },
54	  {
55	    "name": "RepoBench-R Cross-File Retrieval Evaluation",
56	    "description": "3 strategies × best checkpoint on RepoBench-R, retrieval-only evaluation",
57	    "results": {
58	      "random_recall1": 0.412,
59	      "embedding_distance_recall1": 0.431,
60	      "dataflow_aware_recall1": 0.438,
61	      "random_mrr": 0.508,
62	      "embedding_distance_mrr": 0.529,
63	      "dataflow_aware_mrr": 0.534,
64	      "embed_vs_random_R1_delta_pp": 1.9,
65	      "dataflow_vs_random_R1_delta_pp": 2.6,
66	      "total_queries": 1200
67	    },
68	    "tables": [
69	      {
70	        "caption": "RepoBench-R Retrieval Performance",
71	        "columns": [
72	          "Strategy",
73	          "R@1",
74	          "R@5",
75	          "R@10",
76	          "MRR"
77	        ],
78	        "rows": [
79	          [
80	            "random",
81	            0.412,
82	            0.687,
83	            0.793,
84	            0.508
85	          ],
86	          [
87	            "embedding_distance",
88	            0.431,
89	            0.704,
90	            0.808,
91	            0.529
92	          ],
93	          [
94	            "dataflow_aware",
95	            0.438,
96	            0.711,
97	            0.812,
98	            0.534
99	          ]
100	        ]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b547124-4446-4802-b111-0a1249c108b9",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "242e5f37-2639-4899-98c6-a502fc375a13",
  "sourceToolAssistantUUID": "4b547124-4446-4802-b111-0a1249c108b9",
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

_source line 52 · 2026-05-14T08:25:18.981Z_

Now let me look at the training code to understand the exact methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "242e5f37-2639-4899-98c6-a502fc375a13",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29AhzWSLwyWbYZjiX4x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7445a014-b41c-45c8-80ed-1efaeb9cc232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012v5YX9PyVQnXi2bj8bg34u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1808,
      "cache_read_input_tokens": 71722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1808,
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

_source line 53 · 2026-05-14T08:25:19.934Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T58jxBz2yyYGCRoUtCBxqt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/hard_negative_mining.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7445a014-b41c-45c8-80ed-1efaeb9cc232",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29AhzWSLwyWbYZjiX4x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dada167a-87f9-4b85-af14-9b36339429f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012v5YX9PyVQnXi2bj8bg34u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1808,
      "cache_read_input_tokens": 71722,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1808,
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

_source line 54 · 2026-05-14T08:25:19.939Z_

<details><summary>↩ Tool result · `toolu_01T58jxBz2yyYGCRoUtCBxqt`</summary>

```text
1	"""Data-flow-aware hard negative mining for StructFuse.
2	
3	Three strategies:
4	  1. random         — baseline, random non-positive from same repo
5	  2. embedding_distance — CoCoHaNeRe-style nearest-neighbour non-positives
6	  3. dataflow_aware — lexically similar but data-flow disconnected (our contribution)
7	"""
8	
9	from __future__ import annotations
10	
11	import random as stdlib_random
12	from abc import ABC, abstractmethod
13	from pathlib import Path
14	from typing import Dict, List, Set, Tuple
15	
16	import numpy as np
17	
18	
19	class HardNegativeMiner(ABC):
20	    """Base class for hard-negative mining strategies."""
21	
22	    def __init__(
23	        self,
24	        dataflow_graph: Dict[str, Set[str]] | None = None,
25	        embeddings: Dict[str, np.ndarray] | None = None,
26	        bm25_index: object | None = None,
27	    ):
28	        self.dataflow_graph = dataflow_graph or {}
29	        self.embeddings = embeddings or {}
30	        self.bm25_index = bm25_index
31	
32	    @abstractmethod
33	    def mine(
34	        self,
35	        query: str,
36	        positives: List[str],
37	        candidates: List[str],
38	        num_negatives: int,
39	    ) -> List[Tuple[str, float]]:
40	        """Return list of (candidate_id, hardness_score) tuples."""
41	        ...
42	
43	    # ── shared helpers ──────────────────────────────────────────────
44	
45	    @staticmethod
46	    def _exclude(candidates: List[str], exclude: Set[str]) -> List[str]:
47	        return [c for c in candidates if c not in exclude]
48	
49	    @staticmethod
50	    def load_embeddings(path: str | Path) -> Dict[str, np.ndarray]:
51	        """Load pre-computed embeddings from a .npz file (keys=file ids)."""
52	        data = np.load(path, allow_pickle=True)
53	        return {str(k): data[k] for k in data.files}
54	
55	    @staticmethod
56	    def save_embeddings(embs: Dict[str, np.ndarray], path: str | Path) -> None:
57	        np.savez(path, **embs)
58	
59	
60	class RandomMiner(HardNegativeMiner):
61	    """Uniformly random negatives from same-repo non-positives."""
62	
63	    def mine(self, query, positives, candidates, num_negatives):
64	        pool = self._exclude(candidates, {query, *positives})
65	        sampled = stdlib_random.sample(pool, min(num_negatives, len(pool)))
66	        return [(s, 0.0) for s in sampled]
67	
68	
69	class EmbeddingDistanceMiner(HardNegativeMiner):
70	    """Nearest-neighbour negatives by cosine similarity (CoCoHaNeRe baseline)."""
71	
72	    def __init__(self, **kwargs):
73	        super().__init__(**kwargs)
74	        self._matrix: np.ndarray | None = None
75	        self._keys: List[str] | None = None
76	
77	    def _build_matrix(self):
78	        if self._matrix is not None:
79	            return
80	        self._keys = sorted(self.embeddings.keys())
81	        vecs = np.stack([self.embeddings[k] for k in self._keys]).astype(np.float32)
82	        norms = np.linalg.norm(vecs, axis=1, keepdims=True).clip(min=1e-8)
83	        self._matrix = vecs / norms
84	
85	    def mine(self, query, positives, candidates, num_negatives):
86	        self._build_matrix()
87	        if query not in self.embeddings:
88	            return RandomMiner().mine(query, positives, candidates, num_negatives)
89	
90	        exclude = {query, *positives}
91	        q_vec = self.embeddings[query].astype(np.float32)
92	        q_vec = q_vec / max(np.linalg.norm(q_vec), 1e-8)
93	
94	        # cosine similarity against all candidates
95	        cand_set = set(self._exclude(candidates, exclude))
96	        indices = [i for i, k in enumerate(self._keys) if k in cand_set]
97	        if not indices:
98	            return []
99	
100	        sims = self._matrix[indices] @ q_vec  # (N_cand,)
101	        top_k = min(num_negatives, len(indices))
102	        top_idx = np.argpartition(-sims, top_k)[:top_k]
103	        top_idx = top_idx[np.argsort(-sims[top_idx])]
104	
105	        return [(self._keys[indices[i]], float(sims[i])) for i in top_idx]
106	
107	
108	class DataFlowAwareMiner(HardNegativeMiner):
109	    """Select lexically/embedding-similar but data-flow-disconnected files.
110	
111	    Core insight: a file that *looks* related (high BM25 or embedding sim) but
112	    has no data-flow path to the query provides the strongest contrastive signal.
113	    """
114	
115	    def __init__(self, top_k_similar: int = 50, **kwargs):
116	        super().__init__(**kwargs)
117	        self.top_k_similar = top_k_similar
118	        self._emb_miner = EmbeddingDistanceMiner(
119	            embeddings=self.embeddings,
120	            dataflow_graph=self.dataflow_graph,
121	        )
122	
123	    def _is_reachable(self, src: str, dst: str) -> bool:
124	        return dst in self.dataflow_graph.get(src, set())
125	
126	    def mine(self, query, positives, candidates, num_negatives):
127	        exclude = {query, *positives}
128	
129	        # Step 1: get top-K similar candidates (by embedding distance)
130	        similar = self._emb_miner.mine(
131	            query, positives, candidates, self.top_k_similar
132	        )
133	
134	        # Step 2: filter to those NOT reachable via data-flow
135	        disconnected = [
136	            (fid, score)
137	            for fid, score in similar
138	            if fid not in exclude and not self._is_reachable(query, fid)
139	        ]
140	
141	        # Step 3: if BM25 index available, re-rank by BM25 similarity
142	        if self.bm25_index is not None and hasattr(self.bm25_index, "get_scores"):
143	            disconnected = self._rerank_bm25(query, disconnected)
144	
145	        selected = disconnected[:num_negatives]
146	
147	        # fallback: pad with random if not enough disconnected candidates
148	        if len(selected) < num_negatives:
149	            used = {fid for fid, _ in selected} | exclude
150	            pool = [c for c in candidates if c not in used]
151	            extra = stdlib_random.sample(pool, min(num_negatives - len(selected), len(pool)))
152	            selected.extend([(e, 0.0) for e in extra])
153	
154	        return selected
155	
156	    def _rerank_bm25(
157	        self, query: str, candidates: List[Tuple[str, float]]
158	    ) -> List[Tuple[str, float]]:
159	        """Re-rank disconnected candidates by BM25 score (descending)."""
160	        from rank_bm25 import BM25Okapi
161	
162	        if not isinstance(self.bm25_index, BM25Okapi):
163	            return candidates
164	
165	        # BM25 scores expect a tokenized query — use simple whitespace split
166	        scores = self.bm25_index.get_scores(query.split())
167	        id_to_bm25: Dict[str, float] = {}
168	        if hasattr(self.bm25_index, "_doc_ids"):
169	            for idx, doc_id in enumerate(self.bm25_index._doc_ids):
170	                id_to_bm25[doc_id] = float(scores[idx])
171	
172	        reranked = sorted(
173	            candidates,
174	            key=lambda t: id_to_bm25.get(t[0], 0.0),
175	            reverse=True,
176	        )
177	        return reranked
178	
179	
180	# ── batch mining helper ─────────────────────────────────────────────
181	
182	def mine_batch(
183	    miner: HardNegativeMiner,
184	    queries: List[str],
185	    positives_map: Dict[str, List[str]],
186	    all_candidates: List[str],
187	    num_negatives: int,
188	) -> Dict[str, List[Tuple[str, float]]]:
189	    """Mine negatives for a batch of queries. Suitable for epoch-level pre-mining."""
190	    results = {}
191	    for q in queries:
192	        pos = positives_map.get(q, [])
193	        results[q] = miner.mine(q, pos, all_candidates, num_negatives)
194	    return results
195	
196	
197	def build_miner(
198	    strategy: str,
199	    dataflow_graph: Dict[str, Set[str]] | None = None,
200	    embeddings: Dict[str, np.ndarray] | None = None,
201	    bm25_index: object | None = None,
202	    **kwargs,
203	) -> HardNegativeMiner:
204	    """Factory for miner instantiation."""
205	    cls_map = {
206	        "random": RandomMiner,
207	        "embedding_distance": EmbeddingDistanceMiner,
208	        "dataflow_aware": DataFlowAwareMiner,
209	    }
210	    if strategy not in cls_map:
211	        raise ValueError(f"Unknown strategy '{strategy}', choose from {list(cls_map)}")
212	    return cls_map[strategy](
213	        dataflow_graph=dataflow_graph,
214	        embeddings=embeddings,
215	        bm25_index=bm25_index,
216	        **kwargs,
217	    )
218	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dada167a-87f9-4b85-af14-9b36339429f5",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "9a312670-74c3-48ed-9a8c-b805e39cadfd",
  "sourceToolAssistantUUID": "dada167a-87f9-4b85-af14-9b36339429f5",
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

_source line 55 · 2026-05-14T08:25:20.553Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VxKNi8xWUW7cobPrAMiiCr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/training/train.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a312670-74c3-48ed-9a8c-b805e39cadfd",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29AhzWSLwyWbYZjiX4x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18cbefad-b2d4-477b-9be5-27c28129fe71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012v5YX9PyVQnXi2bj8bg34u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1808,
      "cache_read_input_tokens": 71722,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1808
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 71722,
          "cache_creation_input_tokens": 1808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1808,
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

_source line 56 · 2026-05-14T08:25:20.567Z_

<details><summary>↩ Tool result · `toolu_01VxKNi8xWUW7cobPrAMiiCr`</summary>

```text
1	import os
2	os.environ["CUDA_VISIBLE_DEVICES"] = "4"
3	
4	"""StructFuse contrastive training entry point.
5	
6	Trains a bi-encoder (Qwen2.5-Coder-3B) with InfoNCE loss, data-flow-weighted
7	positives, and configurable hard-negative mining.  Supports single/multi-GPU
8	via HuggingFace Accelerate, LoRA, gradient checkpointing, and W&B logging.
9	"""
10	
11	from __future__ import annotations
12	
13	import argparse
14	import json
15	import math
16	import os
17	import random
18	from pathlib import Path
19	from typing import Any, Dict, List
20	
21	import numpy as np
22	import torch
23	from torch.utils.data import DataLoader, Dataset
24	from transformers import AutoTokenizer, get_cosine_schedule_with_warmup
25	
26	from accelerate import Accelerator
27	from accelerate.utils import set_seed
28	
29	from contrastive_model import StructFuseEncoder
30	from hard_negative_mining import build_miner, mine_batch
31	
32	
33	# ── Dataset ──────────────────────────────────────────────────────────
34	
35	class ContrastiveDataset(Dataset):
36	    """
37	    Each sample: {query, positive, negatives[], pos_weight, features[]}.
38	
39	    The raw data file is JSONL with fields:
40	        query_id, query_tokens, pos_id, pos_tokens, pos_dataflow_distance,
41	        neg_candidates (list of file ids), features (dict per candidate).
42	
43	    Negatives are mined dynamically per epoch via `refresh_negatives()`.
44	    """
45	
46	    def __init__(
47	        self,
48	        data_path: str,
49	        tokenizer: AutoTokenizer,
50	        max_seq_length: int,
51	        num_negatives: int,
52	        pos_weight_alpha: float,
53	        use_fusion_head: bool,
54	    ):
55	        self.tokenizer = tokenizer
56	        self.max_seq_length = max_seq_length
57	        self.num_negatives = num_negatives
58	        self.alpha = pos_weight_alpha
59	        self.use_fusion_head = use_fusion_head
60	
61	        self.samples: List[Dict[str, Any]] = []
62	        with open(data_path) as f:
63	            for line in f:
64	                if line.strip():
65	                    self.samples.append(json.loads(line))
66	
67	        # mined negatives, refreshed each epoch
68	        self._negatives: Dict[int, List[Dict[str, Any]]] = {}
69	
70	    def refresh_negatives(self, mined: Dict[str, List[tuple]]):
71	        """Update negatives after an epoch-level mining pass."""
72	        self._negatives = {}
73	        for idx, sample in enumerate(self.samples):
74	            qid = sample["query_id"]
75	            negs = mined.get(qid, [])
76	            self._negatives[idx] = negs
77	
78	    def __len__(self):
79	        return len(self.samples)
80	
81	    def __getitem__(self, idx):
82	        s = self.samples[idx]
83	
84	        query_enc = self.tokenizer(
85	            s["query_tokens"], truncation=True, max_length=self.max_seq_length,
86	            padding=False, return_tensors=None,
87	        )
88	        pos_enc = self.tokenizer(
89	            s["pos_tokens"], truncation=True, max_length=self.max_seq_length,
90	            padding=False, return_tensors=None,
91	        )
92	
93	        # positive weight from data-flow distance
94	        dist = s.get("pos_dataflow_distance", 1.0)
95	        pos_weight = math.exp(-self.alpha * dist)
96	
97	        # negatives
98	        neg_pool = self._negatives.get(idx, [])
99	        if len(neg_pool) < self.num_negatives:
100	            # fallback: use candidates from the sample itself
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18cbefad-b2d4-477b-9be5-27c28129fe71",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "89c0dd6b-71b5-41db-aaa8-18d94760eed0",
  "sourceToolAssistantUUID": "18cbefad-b2d4-477b-9be5-27c28129fe71",
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

_source line 57 · 2026-05-14T08:25:32.591Z_

Now let me check the evaluation code and the CodeQL extraction pipeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89c0dd6b-71b5-41db-aaa8-18d94760eed0",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29B1C7La1CkhgocEpaZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "478491ae-bdc6-402f-988e-30976ba11a98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJSMByig1uEepHY9Gezocq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4284,
      "cache_read_input_tokens": 73530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4284,
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

_source line 58 · 2026-05-14T08:25:35.080Z_

<details open><summary>🔧 Tool call — Read · `toolu_012VGeQMv81hrTEQqkygGFEY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/evaluation/eval_retrieval.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "478491ae-bdc6-402f-988e-30976ba11a98",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29B1C7La1CkhgocEpaZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f8d2787-b14e-4f46-b4b6-84899ec6f6dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJSMByig1uEepHY9Gezocq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4284,
      "cache_read_input_tokens": 73530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4284,
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

_source line 59 · 2026-05-14T08:25:35.085Z_

<details><summary>↩ Tool result · `toolu_012VGeQMv81hrTEQqkygGFEY`</summary>

```text
1	import os
2	os.environ["CUDA_VISIBLE_DEVICES"] = "4"
3	
4	"""
5	StructFuse Retrieval Evaluation Script
6	
7	Evaluates the StructFuse contrastive retriever on file-level and function-level
8	retrieval tasks across SWE-bench Lite, RepoBench-R, and custom held-out sets.
9	
10	Input:
11	  - Trained StructFuse checkpoint(s)
12	  - Test file (JSON Lines): each line has {query, gold_files, gold_functions, repo_path}
13	  - (Optional) CodeQL data-flow output directory
14	
15	Output:
16	  - JSON file with per-instance predictions and aggregate metrics:
17	    Recall@1/5/10, MRR, Structural Precision
18	
19	Dependencies: transformers, torch, rank_bm25, faiss-cpu, numpy
20	"""
21	
22	import argparse
23	import json
24	import os
25	import glob
26	import sys
27	import time
28	from collections import defaultdict
29	from dataclasses import dataclass, field
30	from pathlib import Path
31	from typing import Optional
32	
33	import jsonlines
34	import numpy as np
35	import torch
36	import torch.nn.functional as F
37	from tqdm import tqdm
38	from transformers import AutoTokenizer
39	from rank_bm25 import BM25Okapi
40	
41	sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "training"))
42	from contrastive_model import StructFuseEncoder
43	
44	
45	@dataclass
46	class RetrievalInstance:
47	    query: str
48	    gold_files: list[str]
49	    gold_functions: list[str] = field(default_factory=list)
50	    repo_path: str = ""
51	    instance_id: str = ""
52	    metadata: dict = field(default_factory=dict)
53	
54	
55	@dataclass
56	class RetrievalResult:
57	    instance_id: str
58	    query: str
59	    gold_files: list[str]
60	    predicted_files: list[str]
61	    scores: list[float]
62	    hits: dict[str, bool] = field(default_factory=dict)
63	
64	
65	def load_test_data(test_file: str, dataset: str) -> list[RetrievalInstance]:
66	    """Load test instances from JSON Lines file, adapting format per dataset."""
67	    instances = []
68	    with jsonlines.open(test_file) as reader:
69	        for i, item in enumerate(reader):
70	            if dataset == "swebench_lite":
71	                inst = RetrievalInstance(
72	                    query=item.get("problem_statement", item.get("query", "")),
73	                    gold_files=item.get("gold_files", []),
74	                    gold_functions=item.get("gold_functions", []),
75	                    repo_path=item.get("repo_path", item.get("repo", "")),
76	                    instance_id=item.get("instance_id", f"swebench_{i}"),
77	                )
78	            elif dataset == "repobench":
79	                inst = RetrievalInstance(
80	                    query=item.get("query", ""),
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f8d2787-b14e-4f46-b4b6-84899ec6f6dc",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "446d8896-31f9-4198-aa20-aca32f49d4ce",
  "sourceToolAssistantUUID": "7f8d2787-b14e-4f46-b4b6-84899ec6f6dc",
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

_source line 60 · 2026-05-14T08:25:36.360Z_

<details open><summary>🔧 Tool call — Read · `toolu_019hfvaJQrKfhfnQeXBpa9FM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/code/extraction/build_training_data.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "446d8896-31f9-4198-aa20-aca32f49d4ce",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29B1C7La1CkhgocEpaZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6117b30-c4d2-42fa-9e11-e0c3dfefe14f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJSMByig1uEepHY9Gezocq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4284,
      "cache_read_input_tokens": 73530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4284,
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

_source line 61 · 2026-05-14T08:25:36.376Z_

<details><summary>↩ Tool result · `toolu_019hfvaJQrKfhfnQeXBpa9FM`</summary>

```text
1	"""
2	StructFuse Stage 1→2 bridge: build contrastive training data from data-flow features.
3	
4	Reads extraction output (all.jsonl from extract_dataflow.py) and original repo code
5	to produce contrastive training triples (query, positive, negatives) with feature vectors.
6	
7	Output format: JSONL compatible with HuggingFace datasets.load_dataset("json").
8	Each line: {query, pos_code, neg_codes, features, metadata}
9	
10	Dependencies: rank_bm25, numpy
11	"""
12	
13	import argparse
14	import json
15	import logging
16	import os
17	import random
18	from collections import defaultdict
19	from pathlib import Path
20	from typing import Any
21	
22	import numpy as np
23	
24	logging.basicConfig(
25	    level=logging.INFO,
26	    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
27	)
28	log = logging.getLogger("build_training_data")
29	
30	
31	# ---------------------------------------------------------------------------
32	# File reading
33	# ---------------------------------------------------------------------------
34	
35	def read_file_content(repo_path: str, file_path: str) -> str | None:
36	    """Read a source file from repo, return content or None."""
37	    full = os.path.join(repo_path, file_path)
38	    if not os.path.isfile(full):
39	        return None
40	    try:
41	        with open(full, encoding="utf-8", errors="replace") as f:
42	            return f.read()
43	    except OSError:
44	        return None
45	
46	
47	def collect_repo_files(repo_path: str) -> list[str]:
48	    """List all .py files in the repo (relative paths)."""
49	    files = []
50	    for root, _dirs, filenames in os.walk(repo_path):
51	        for fname in filenames:
52	            if fname.endswith(".py"):
53	                rel = os.path.relpath(os.path.join(root, fname), repo_path)
54	                files.append(rel)
55	    return files
56	
57	
58	# ---------------------------------------------------------------------------
59	# BM25
60	# ---------------------------------------------------------------------------
61	
62	def build_bm25_index(documents: list[str]):
63	    """Build BM25 index over tokenized documents."""
64	    from rank_bm25 import BM25Okapi
65	    tokenized = [doc.split() for doc in documents]
66	    return BM25Okapi(tokenized)
67	
68	
69	def bm25_scores(bm25_index, query: str) -> np.ndarray:
70	    return bm25_index.get_scores(query.split())
71	
72	
73	# ---------------------------------------------------------------------------
74	# Feature computation
75	# ---------------------------------------------------------------------------
76	
77	def compute_features(
78	    instance: dict,
79	    file_path: str,
80	    bm25_score: float,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6117b30-c4d2-42fa-9e11-e0c3dfefe14f",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "62557ef4-b064-44e7-b27c-bf7d727fa2f8",
  "sourceToolAssistantUUID": "a6117b30-c4d2-42fa-9e11-e0c3dfefe14f",
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

_source line 62 · 2026-05-14T08:25:39.510Z_

Now let me check the first dream review report for comparison, and the neg_difficulty analysis data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62557ef4-b064-44e7-b27c-bf7d727fa2f8",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29CC9hYMQVwHN3HUiMu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10740df1-2d73-42a2-af40-7d038572823e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lwbz1vYemnvYAUHf3fguiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2087,
      "cache_read_input_tokens": 77814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2087,
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

_source line 63 · 2026-05-14T08:25:40.934Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MB64n5nrbtPc44jYFMgK56`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/review_report.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10740df1-2d73-42a2-af40-7d038572823e",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29CC9hYMQVwHN3HUiMu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb865f40-ec99-4a1e-95e4-3245eba6ff28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lwbz1vYemnvYAUHf3fguiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2087,
      "cache_read_input_tokens": 77814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2087,
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

_source line 64 · 2026-05-14T08:25:40.940Z_

<details><summary>↩ Tool result · `toolu_01MB64n5nrbtPc44jYFMgK56`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb865f40-ec99-4a1e-95e4-3245eba6ff28",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "933249c6-d128-410e-adac-da0ba29a264a",
  "sourceToolAssistantUUID": "fb865f40-ec99-4a1e-95e4-3245eba6ff28",
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

_source line 65 · 2026-05-14T08:25:41.681Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LU7E4vmD4tT7jbKhemmAWr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/negative_difficulty_stats_v2.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "933249c6-d128-410e-adac-da0ba29a264a",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29CC9hYMQVwHN3HUiMu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c94ccc7-667b-4181-83b7-d1d874a92c83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lwbz1vYemnvYAUHf3fguiL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2087,
      "cache_read_input_tokens": 77814,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2087
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 77814,
          "cache_creation_input_tokens": 2087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2087,
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

_source line 66 · 2026-05-14T08:25:41.692Z_

<details><summary>↩ Tool result · `toolu_01LU7E4vmD4tT7jbKhemmAWr`</summary>

```text
1	Full stats JSON saved at bjb1-42106:/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v2.json
2	
3	Summary table:
4	Strategy             Encoder     Pos Sim  Neg Sim  Margin  Margin Std  %Pos>Neg
5	Random               Qwen        0.9804   0.8988   0.0816  0.2299      77.8%
6	Random               StarCoder   0.7568   0.5529   0.2039  0.3237      72.8%
7	Embedding Distance   Qwen        0.9804   0.9595   0.0209  0.1149      60.7%
8	Embedding Distance   StarCoder   0.7838   0.6679   0.1159  0.2559      59.2%
9	Dataflow-Aware       Qwen        0.9805   0.9496   0.0309  0.1406      67.4%
10	Dataflow-Aware       StarCoder   0.7609   0.6587   0.1022  0.2574      62.8%
11	
12	StarCoder/Qwen margin ratio: Random 2.50x, Embedding 5.54x, Dataflow 3.30x
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c94ccc7-667b-4181-83b7-d1d874a92c83",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "52a5069c-edfb-417a-9eb5-518bfd1e6e23",
  "sourceToolAssistantUUID": "1c94ccc7-667b-4181-83b7-d1d874a92c83",
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

_source line 67 · 2026-05-14T08:25:45.216Z_

Now I have a thorough understanding of the paper, the experimental pipeline, project history, and the actual data. Let me also check one more important detail -- the Z% inconsistency mentioned in the review task.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52a5069c-edfb-417a-9eb5-518bfd1e6e23",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29CZQsyTTVTVaX4bha3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "288c70d2-5292-4a56-bb20-c97478bf8fcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfjEJ3pdKBSG5sEwLexF92",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3564,
      "cache_read_input_tokens": 79901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3564,
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

_source line 68 · 2026-05-14T08:25:47.164Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AMxiexsY6Pdy3tgJB617DN`</summary>

```json
{
  "pattern": "Z%|z_pct|z_percent|connected.*not.*gold",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "288c70d2-5292-4a56-bb20-c97478bf8fcd",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29CZQsyTTVTVaX4bha3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a49e80d4-a1df-488a-b3b2-55cd38ccbbe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfjEJ3pdKBSG5sEwLexF92",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3564,
      "cache_read_input_tokens": 79901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3564,
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

_source line 69 · 2026-05-14T08:25:47.181Z_

<details><summary>↩ Tool result · `toolu_01AMxiexsY6Pdy3tgJB617DN`</summary>

```text
78:\paragraph{Dataflow-aware.} Construct an inter-procedural dataflow graph $G$ over $\mathcal{R}$ using CodeQL. Define a file pair $(f_i, f_j)$ as \emph{connected} if there exists a call-graph path of $\leq 2$ hops between any function in $f_i$ and any function in $f_j$. A \textbf{structure-grounded hard negative} is a file that is (a)~textually similar to $f^+$ (high embedding cosine), (b)~\emph{not} the gold file, and (c)~\emph{not} connected to $f^+$ in $G$. Formally:
87:We use CodeQL to extract inter-procedural call graphs from Python repositories. Each repository is compiled into a CodeQL database, and we query for function-level call edges. Connected components are computed at $k$-hop granularity. At our evaluation scale of 131 SWE-smith repositories, the pipeline achieves 0\% query timeout, with 123/131 repos producing valid output and 78\% connected-not-gold rate ($Z\%$) at 2-hop.
388:Dataflow mining is most effective for cross-file dependency failures (79\% help rate), where the gold file has a dataflow connection to the query but low lexical similarity. This aligns with the 41\% connected-not-gold rate ($Z\%$) from our extraction pipeline. LLM reasoning failures are retrieval-independent and naturally unaffected.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a49e80d4-a1df-488a-b3b2-55cd38ccbbe7",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "122deacd-2e39-4eb9-94b1-85c433ecaba3",
  "sourceToolAssistantUUID": "a49e80d4-a1df-488a-b3b2-55cd38ccbbe7",
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

_source line 70 · 2026-05-14T08:25:47.833Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GcdB6FRtTRnRMThmZXyrKe`</summary>

```json
{
  "pattern": "Z%|78%|41%",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "122deacd-2e39-4eb9-94b1-85c433ecaba3",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29CZQsyTTVTVaX4bha3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc3370a4-f303-48bd-b946-21d8d726776c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfjEJ3pdKBSG5sEwLexF92",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3564,
      "cache_read_input_tokens": 79901,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 321,
          "cache_read_input_tokens": 79901,
          "cache_creation_input_tokens": 3564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3564,
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

_source line 71 · 2026-05-14T08:25:47.848Z_

<details><summary>↩ Tool result · `toolu_01GcdB6FRtTRnRMThmZXyrKe`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc3370a4-f303-48bd-b946-21d8d726776c",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "e3afeba3-e881-4b68-b1dc-3041cc43ff6d",
  "sourceToolAssistantUUID": "cc3370a4-f303-48bd-b946-21d8d726776c",
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

_source line 72 · 2026-05-14T08:25:50.702Z_

The Z% inconsistency is confirmed -- line 87 says 78% Z% and line 388 says 41% Z%. Let me verify the source of each number.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3afeba3-e881-4b68-b1dc-3041cc43ff6d",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29D1gSMVHMXyM4UDVmp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e34dc3a-b8c7-4890-ac4e-a6c52c286b39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eu6xwBSeY2rHcfdijxtdMM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 83465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 752,
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

_source line 73 · 2026-05-14T08:25:52.402Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HJXJmrKxyNFuBDxt2Wa4Cv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_006_scalability/data/full_z_percent_stats.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e34dc3a-b8c7-4890-ac4e-a6c52c286b39",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29D1gSMVHMXyM4UDVmp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d6f43cd-6669-466d-95bc-59c805bd20c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eu6xwBSeY2rHcfdijxtdMM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 83465,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 752
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 83465,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 752,
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

_source line 74 · 2026-05-14T08:25:52.690Z_

<details><summary>↩ Tool result · `toolu_01HJXJmrKxyNFuBDxt2Wa4Cv`</summary>

```text
1	{"summary":{"total_instances":44173,"error_null":15897,"error_non_null":28276,"extraction_codeql":15133,"extraction_beniget":764,"has_nonempty_structural":15153,"codeql_nonempty":15133,"beniget_nonempty":20,"z_positive":11825,"z_positive_codeql":11805,"z_positive_beniget":20,"conditional_z_percent":78.04,"unconditional_z_percent":26.77,"structural_coverage_of_success":95.32,"structural_coverage_of_total":34.3},"per_repo":{"Cog-Creators/Red-DiscordBot":{"total":460,"error_null":460,"has_structural":439,"z_positive":394,"conditional_z_percent":89.7},"HIPS/autograd":{"total":192,"error_null":192,"has_structural":130,"z_positive":59,"conditional_z_percent":45.4},"Instagram/MonkeyType":{"total":133,"error_null":38,"has_structural":36,"z_positive":26,"conditional_z_percent":72.2},"Knio/dominate":{"total":42,"error_null":42,"has_structural":31,"z_positive":23,"conditional_z_percent":74.2},"Mimino666/langdetect":{"total":118,"error_null":35,"has_structural":34,"z_positive":34,"conditional_z_percent":100.0},"Project-MONAI/MONAI":{"total":527,"error_null":3,"has_structural":2,"z_positive":2,"conditional_z_percent":100.0},"PyCQA/flake8":{"total":454,"error_null":454,"has_structural":444,"z_positive":409,"conditional_z_percent":92.1},"Suor/funcy":{"total":306,"error_null":306,"has_structural":281,"z_positive":71,"conditional_z_percent":25.3},"adrienverge/yamllint":{"total":350,"error_null":6,"has_structural":5,"z_positive":2,"conditional_z_percent":40.0},"agronholm/exceptiongroup":{"total":139,"error_null":139,"has_structural":132,"z_positive":101,"conditional_z_percent":76.5},"agronholm/typeguard":{"total":333,"error_null":333,"has_structural":302,"z_positive":215,"conditional_z_percent":71.2},"aio-libs/async-timeout":{"total":19,"error_null":19,"has_structural":4,"z_positive":0,"conditional_z_percent":0.0},"alanjds/drf-nested-routers":{"total":35,"error_null":34,"has_structural":31,"z_positive":27,"conditional_z_percent":87.1},"alecthomas/voluptuous":{"total":248,"error_null":32,"has_structural":30,"z_positive":20,"conditional_z_percent":66.7},"andialbrecht/sqlparse":{"total":459,"error_null":459,"has_structural":454,"z_positive":436,"conditional_z_percent":96.0},"arrow-py/arrow":{"total":333,"error_null":29,"has_structural":28,"z_positive":24,"conditional_z_percent":85.7},"benoitc/gunicorn":{"total":373,"error_null":27,"has_structural":26,"z_positive":26,"conditional_z_percent":100.0},"borntyping/python-colorlog":{"total":28,"error_null":28,"has_structural":23,"z_positive":19,"conditional_z_percent":82.6},"bottlepy/bottle":{"total":373,"error_null":373,"has_structural":369,"z_positive":0,"conditional_z_percent":0.0},"buriy/python-readability":{"total":41,"error_null":39,"has_structural":35,"z_positive":31,"conditional_z_percent":88.6},"burnash/gspread":{"total":90,"error_null":21,"has_structural":20,"z_positive":16,"conditional_z_percent":80.0},"cantools/cantools":{"total":1440,"error_null":1411,"has_structural":1396,"z_positive":1224,"conditional_z_percent":87.7},"chardet/chardet":{"total":215,"error_null":215,"has_structural":207,"z_positive":204,"conditional_z_percent":98.6},"cknd/stackprinter":{"total":137,"error_null":137,"has_structural":129,"z_positive":101,"conditional_z_percent":78.3},"cloudpipe/cloudpickle":{"total":115,"error_null":33,"has_structural":31,"z_positive":0,"conditional_z_percent":0.0},"conan-io/conan":{"total":978,"error_null":6,"has_structural":5,"z_positive":5,"conditional_z_percent":100.0},"cookiecutter/cookiecutter":{"total":67,"error_null":36,"has_structural":34,"z_positive":15,"conditional_z_percent":44.1},"cool-RR/PySnooper":{"total":77,"error_null":33,"has_structural":30,"z_positive":26,"conditional_z_percent":86.7},"dask/dask":{"total":336,"error_null":7,"has_structural":4,"z_positive":4,"conditional_z_percent":100.0},"datamade/usaddress":{"total":8,"error_null":8,"has_structural":7,"z_positive":0,"conditional_z_percent":0.0},"davidhalter/parso":{"total":611,"error_null":29,"has_structural":24,"z_positive":21,"conditional_z_percent":87.5},"dbader/schedule":{"total":80,"error_null":20,"has_structural":19,"z_positive":0,"conditional_z_percent":0.0},"django-money/django-money":{"total":256,"error_null":33,"has_structural":29,"z_positive":24,"conditional_z_percent":82.8},"django/channels":{"total":112,"error_null":34,"has_structural":34,"z_positive":32,"conditional_z_percent":94.1},"django/daphne":{"total":50,"error_null":31,"has_structural":30,"z_positive":25,"conditional_z_percent":83.3},"encode/starlette":{"total":721,"error_null":32,"has_structural":30,"z_positive":27,"conditional_z_percent":90.0},"erikrose/parsimonious":{"total":95,"error_null":35,"has_structural":34,"z_positive":34,"conditional_z_percent":100.0},"facebookresearch/fvcore":{"total":483,"error_null":29,"has_structural":28,"z_positive":19,"conditional_z_percent":67.9},"facebookresearch/hydra":{"total":427,"error_null":25,"has_structural":22,"z_positive":19,"conditional_z_percent":86.4},"facelessuser/soupsieve":{"total":285,"error_null":32,"has_structural":30,"z_positive":30,"conditional_z_percent":100.0},"gawel/pyquery":{"total":249,"error_null":38,"has_structural":31,"z_positive":21,"conditional_z_percent":67.7},"getmoto/moto":{"total":539,"error_null":3,"has_structural":1,"z_positive":1,"conditional_z_percent":100.0},"getnikola/nikola":{"total":435,"error_null":28,"has_structural":23,"z_positive":22,"conditional_z_percent":95.7},"google/textfsm":{"total":79,"error_null":79,"has_structural":77,"z_positive":73,"conditional_z_percent":94.8},"graphql-python/graphene":{"total":480,"error_null":29,"has_structural":28,"z_positive":19,"conditional_z_percent":67.9},"gruns/furl":{"total":196,"error_null":41,"has_structural":38,"z_positive":32,"conditional_z_percent":84.2},"gruns/icecream":{"total":17,"error_null":8,"has_structural":7,"z_positive":0,"conditional_z_percent":0.0},"gweis/isodate":{"total":129,"error_null":39,"has_structural":34,"z_positive":7,"conditional_z_percent":20.6},"iterative/dvc":{"total":467,"error_null":17,"has_structural":13,"z_positive":11,"conditional_z_percent":84.6},"jaraco/inflect":{"total":133,"error_null":133,"has_structural":127,"z_positive":0,"conditional_z_percent":0.0},"jawah/charset_normalizer":{"total":187,"error_null":36,"has_structural":35,"z_positive":15,"conditional_z_percent":42.9},"jd/tenacity":{"total":152,"error_null":152,"has_structural":145,"z_positive":133,"conditional_z_percent":91.7},"john-kurkowski/tldextract":{"total":100,"error_null":36,"has_structural":34,"z_positive":15,"conditional_z_percent":44.1},"joke2k/faker":{"total":360,"error_null":360,"has_structural":350,"z_positive":337,"conditional_z_percent":96.3},"jsvine/pdfplumber":{"total":261,"error_null":29,"has_structural":28,"z_positive":26,"conditional_z_percent":92.9},"kayak/pypika":{"total":745,"error_null":29,"has_structural":25,"z_positive":22,"conditional_z_percent":88.0},"keleshev/schema":{"total":88,"error_null":88,"has_structural":86,"z_positive":0,"conditional_z_percent":0.0},"kennethreitz/records":{"total":34,"error_null":34,"has_structural":33,"z_positive":0,"conditional_z_percent":0.0},"kurtmckee/feedparser":{"total":597,"error_null":146,"has_structural":133,"z_positive":129,"conditional_z_percent":97.0},"lepture/mistune":{"total":729,"error_null":729,"has_structural":669,"z_positive":534,"conditional_z_percent":79.8},"life4/textdistance":{"total":269,"error_null":36,"has_structural":35,"z_positive":35,"conditional_z_percent":100.0},"lincolnloop/python-qrcode":{"total":291,"error_null":35,"has_structural":31,"z_positive":30,"conditional_z_percent":96.8},"luozhouyang/python-string-similarity":{"total":59,"error_null":59,"has_structural":45,"z_positive":45,"conditional_z_percent":100.0},"madzak/python-json-logger":{"total":38,"error_null":38,"has_structural":37,"z_positive":0,"conditional_z_percent":0.0},"mahmoud/boltons":{"total":737,"error_null":737,"has_structural":717,"z_positive":675,"conditional_z_percent":94.1},"mahmoud/glom":{"total":523,"error_null":29,"has_structural":28,"z_positive":26,"conditional_z_percent":92.9},"marshmallow-code/apispec":{"total":301,"error_null":3,"has_structural":2,"z_positive":2,"conditional_z_percent":100.0},"marshmallow-code/marshmallow":{"total":389,"error_null":31,"has_structural":24,"z_positive":18,"conditional_z_percent":75.0},"marshmallow-code/webargs":{"total":321,"error_null":321,"has_structural":305,"z_positive":210,"conditional_z_percent":68.9},"martinblech/xmltodict":{"total":44,"error_null":33,"has_structural":32,"z_positive":0,"conditional_z_percent":0.0},"matthewwithanm/python-markdownify":{"total":83,"error_null":83,"has_structural":82,"z_positive":0,"conditional_z_percent":0.0},"mewwts/addict":{"total":28,"error_null":28,"has_structural":26,"z_positive":0,"conditional_z_percent":0.0},"mido/mido":{"total":361,"error_null":34,"has_structural":30,"z_positive":16,"conditional_z_percent":53.3},"modin-project/modin":{"total":91,"error_null":9,"has_structural":7,"z_positive":7,"conditional_z_percent":100.0},"mozilla/bleach":{"total":482,"error_null":27,"has_structural":24,"z_positive":20,"conditional_z_percent":83.3},"mozillazg/python-pinyin":{"total":321,"error_null":13,"has_structural":12,"z_positive":7,"conditional_z_percent":58.3},"msiemens/tinydb":{"total":209,"error_null":209,"has_structural":205,"z_positive":188,"conditional_z_percent":91.7},"oauthlib/oauthlib":{"total":940,"error_null":940,"has_structural":924,"z_positive":879,"conditional_z_percent":95.1},"pallets/click":{"total":645,"error_null":27,"has_structural":26,"z_positive":18,"conditional_z_percent":69.2},"pallets/jinja":{"total":957,"error_null":30,"has_structural":27,"z_positive":22,"conditional_z_percent":81.5},"pallets/markupsafe":{"total":38,"error_null":34,"has_structural":32,"z_positive":19,"conditional_z_percent":59.4},"paramiko/paramiko":{"total":920,"error_null":808,"has_structural":792,"z_positive":788,"conditional_z_percent":99.5},"pexpect/ptyprocess":{"total":32,"error_null":32,"has_structural":32,"z_positive":30,"conditional_z_percent":93.8},"pndurette/gTTS":{"total":112,"error_null":112,"has_structural":105,"z_positive":72,"conditional_z_percent":68.6},"prettytable/prettytable":{"total":276,"error_null":276,"has_structural":274,"z_positive":247,"conditional_z_percent":90.1},"pudo/dataset":{"total":107,"error_null":107,"has_structural":98,"z_positive":97,"conditional_z_percent":99.0},"pwaller/pyfiglet":{"total":10,"error_null":10,"has_structural":10,"z_positive":10,"conditional_z_percent":100.0},"pyasn1/pyasn1":{"total":766,"error_null":440,"has_structural":431,"z_positive":423,"conditional_z_percent":98.1},"pyca/pyopenssl":{"total":301,"error_null":34,"has_structural":33,"z_positive":19,"conditional_z_percent":57.6},"pydantic/pydantic":{"total":676,"error_null":15,"has_structural":12,"z_positive":12,"conditional_z_percent":100.0},"pydata/patsy":{"total":814,"error_null":27,"has_structural":26,"z_positive":19,"conditional_z_percent":73.1},"pydicom/pydicom":{"total":1328,"error_null":13,"has_structural":12,"z_positive":11,"conditional_z_percent":91.7},"pygments/pygments":{"total":1430,"error_null":1255,"has_structural":1195,"z_positive":1106,"conditional_z_percent":92.6},"pylint-dev/astroid":{"total":1770,"error_null":21,"has_structural":18,"z_positive":16,"conditional_z_percent":88.9},"pyparsing/pyparsing":{"total":386,"error_null":25,"has_structural":23,"z_positive":23,"conditional_z_percent":100.0},"pytest-dev/iniconfig":{"total":63,"error_null":63,"has_structural":62,"z_positive":55,"conditional_z_percent":88.7},"python-hyper/h11":{"total":197,"error_null":20,"has_structural":18,"z_positive":18,"conditional_z_percent":100.0},"python-jsonschema/jsonschema":{"total":393,"error_null":33,"has_structural":32,"z_positive":27,"conditional_z_percent":84.4},"python-openxml/python-docx":{"total":1686,"error_null":651,"has_structural":649,"z_positive":579,"conditional_z_percent":89.2},"python-trio/trio":{"total":778,"error_null":25,"has_structural":22,"z_positive":14,"conditional_z_percent":63.6},"python/mypy":{"total":19,"error_null":19,"has_structural":11,"z_positive":11,"conditional_z_percent":100.0},"pyupio/safety":{"total":759,"error_null":759,"has_structural":748,"z_positive":434,"conditional_z_percent":58.0},"pyutils/line_profiler":{"total":223,"error_null":33,"has_structural":32,"z_positive":16,"conditional_z_percent":50.0},"r1chardj0n3s/parse":{"total":90,"error_null":37,"has_structural":35,"z_positive":0,"conditional_z_percent":0.0},"rsalmei/alive-progress":{"total":371,"error_null":371,"has_structural":342,"z_positive":70,"conditional_z_percent":20.5},"rubik/radon":{"total":205,"error_null":40,"has_structural":37,"z_positive":27,"conditional_z_percent":73.0},"rustedpy/result":{"total":64,"error_null":32,"has_structural":31,"z_positive":0,"conditional_z_percent":0.0},"scrapy/scrapy":{"total":194,"error_null":19,"has_structural":17,"z_positive":16,"conditional_z_percent":94.1},"seatgeek/thefuzz":{"total":32,"error_null":32,"has_structural":32,"z_positive":10,"conditional_z_percent":31.2},"seperman/deepdiff":{"total":964,"error_null":142,"has_structural":136,"z_positive":119,"conditional_z_percent":87.5},"sloria/environs":{"total":68,"error_null":33,"has_structural":32,"z_positive":0,"conditional_z_percent":0.0},"spulec/freezegun":{"total":108,"error_null":40,"has_structural":37,"z_positive":0,"conditional_z_percent":0.0},"sqlfluff/sqlfluff":{"total":1292,"error_null":20,"has_structural":17,"z_positive":14,"conditional_z_percent":82.4},"stanfordnlp/dspy":{"total":655,"error_null":22,"has_structural":21,"z_positive":17,"conditional_z_percent":81.0},"stanfordnlp/string2string":{"total":128,"error_null":36,"has_structural":36,"z_positive":36,"conditional_z_percent":100.0},"sunpy/sunpy":{"total":743,"error_null":21,"has_structural":20,"z_positive":19,"conditional_z_percent":95.0},"termcolor/termcolor":{"total":17,"error_null":17,"has_structural":9,"z_positive":0,"conditional_z_percent":0.0},"theskumar/python-dotenv":{"total":141,"error_null":36,"has_structural":32,"z_positive":16,"conditional_z_percent":50.0},"tkrajina/gpxpy":{"total":679,"error_null":30,"has_structural":29,"z_positive":19,"conditional_z_percent":65.5},"tox-dev/pipdeptree":{"total":284,"error_null":38,"has_structural":33,"z_positive":21,"conditional_z_percent":63.6},"tweepy/tweepy":{"total":302,"error_null":34,"has_structural":33,"z_positive":29,"conditional_z_percent":87.9},"un33k/python-slugify":{"total":18,"error_null":18,"has_structural":13,"z_positive":0,"conditional_z_percent":0.0},"weaveworks/grafanalib":{"total":122,"error_null":36,"has_structural":29,"z_positive":26,"conditional_z_percent":89.7}},"metadata":{"source":"/root/autodl-tmp/structfuse/full_m1_data/all.jsonl","total_repos":123,"repos_with_structural":123,"repos_with_z_positive":104}}
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d6f43cd-6669-466d-95bc-59c805bd20c4",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "f6460391-e4e4-490a-9586-114af1925179",
  "sourceToolAssistantUUID": "1d6f43cd-6669-466d-95bc-59c805bd20c4",
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

_source line 75 · 2026-05-14T08:25:58.928Z_

Now I have all the data needed to write a comprehensive review. The key Z% numbers are: conditional Z% = 78.04% (among instances that have structural data), unconditional Z% = 26.77% (of all instances). The hop-distance table says Z%=41% at 2-hop, which appears to come from a different calculation or from the 50-repo pilot (D007). Let me now produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6460391-e4e4-490a-9586-114af1925179",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29DNDxNC4eZMpaGRvVJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40d1a069-2601-4442-9f87-f974fa70c568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgdvNra3caDmDocfpvwftC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5516,
      "cache_read_input_tokens": 84217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5516,
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

_source line 76 · 2026-05-14T08:25:59.708Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GSwAmytru2tfgmY5ZukzED`</summary>

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
  "parentUuid": "40d1a069-2601-4442-9f87-f974fa70c568",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29DNDxNC4eZMpaGRvVJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "656a2d74-03b8-433a-a600-52bf4e4de019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgdvNra3caDmDocfpvwftC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5516,
      "cache_read_input_tokens": 84217,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5516
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 84217,
          "cache_creation_input_tokens": 5516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5516,
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

_source line 77 · 2026-05-14T08:25:59.714Z_

<details><summary>↩ Tool result · `toolu_01GSwAmytru2tfgmY5ZukzED`</summary>

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
  "parentUuid": "656a2d74-03b8-433a-a600-52bf4e4de019",
  "isSidechain": true,
  "promptId": "7eae12a9-b510-4738-a2ca-d1a05873f701",
  "agentId": "a07c5538d1dec79e3",
  "type": "user",
  "uuid": "ac9668b7-627a-48bb-b6c3-989eeabb40dc",
  "sourceToolAssistantUUID": "656a2d74-03b8-433a-a600-52bf4e4de019",
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

_source line 78 · 2026-05-14T08:27:35.909Z_



Now I have thoroughly reviewed all project materials. Let me produce the review.

---

## Reviewer 1 (R1): Methods and Experiments

**Paper:** "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"

---

### 1. Methodological Soundness

**Experimental design (mostly rigorous, with caveats).**

The core 2 encoders x 3 strategies x 9 seeds = 54 runs design is strong for a systematic study. Paired comparisons with bootstrap CIs and p-values (Tables 1-2, 4) follow good practice. The pre-registration of go/no-go thresholds before full M2 results (decisions D019/D020) is commendable and rare in ML papers.

However, several methodological concerns arise:

**(a) The Z% inconsistency is a real and significant issue.** The paper reports Z% = 78% in Section 3.3 (CodeQL extraction pipeline description, line 87 of the tex) but Z% = 41% in Section 4.9 (failure analysis, line 388). From the project data, I can trace these to two different quantities: the 78% is the *conditional* Z% (among the 34.3% of instances that have structural data), while the 41% comes from the 50-repo SWE-bench pilot (D007) or the hop-distance ablation table (Table 8, 2-hop row). The paper uses the same notation "Z%" for both without disambiguation. This is not just a typo -- it reflects a deeper ambiguity about what fraction of the data actually benefits from dataflow mining. The unconditional Z% across all instances is only 26.77%. The paper must clearly define which denominator is used and report both conditional and unconditional rates.

**(b) Coverage gap is insufficiently addressed.** Only 34.3% of instances (15,153/44,173) have structural data from CodeQL. The remaining 65.7% receive no dataflow signal. This means the dataflow strategy's negative mining degrades to embedding-distance or random fallback for ~2/3 of training instances (confirmed by the fallback logic in `DataFlowAwareMiner.mine()`, lines 147-153 of `hard_negative_mining.py`). The paper does not adequately discuss how this dilution affects the measured deltas. The +1.5pp dataflow improvement on Qwen (Table 1) is averaged over all instances, meaning the per-instance effect for instances with structural data is likely much larger -- but this stratified analysis is absent.

**(c) Confound between embedding similarity and dataflow disconnection.** The dataflow-aware miner (code lines 126-154) first selects the top-50 most embedding-similar candidates, then filters to those NOT reachable via dataflow. This means dataflow negatives are a strict subset of embedding-hard negatives with an additional structural constraint. The comparison "dataflow vs. embedding" does not isolate the structural signal -- it conflates the structural filter with a potentially different effective difficulty distribution. A cleaner test would hold embedding similarity constant and compare connected vs. disconnected negatives.

**(d) Statistical methodology is appropriate but power-limited.** 9 seeds with paired tests is reasonable. The bootstrap CIs for SWE-bench (Table 4) are correctly applied. However, the paper should note that with n=9, the paired t-test has df=8, and effect sizes of ~2pp with std ~1pp give Cohen's d ~ 2.0, which is actually well-powered. The real power limitation is the SWE-bench evaluation (300 binary outcomes), where the CI widths of ~4pp (Table 4) are large relative to the claimed effects.

**(e) Checkpoint selection could bias results.** The paper trains for 3 epochs with early stopping but does not report which checkpoint criterion is used. From project decisions (D017), the ranking of strategies *changes* depending on whether best-by-val-loss or best-by-R@1 checkpoints are used. The paper should report both or clearly justify the choice.

### 2. Experimental Completeness

**Ablations are extensive but have gaps.**

The paper covers an impressive range of ablations: temperature (Table 7), hop distance (Table 8), data scaling (Table 9), fusion head (Table 10), static vs. dynamic mining (Table 11), binary vs. weighted dataflow (Table 12), and failure analysis (Table 13). This is well above average.

**Strengths:**
- Temperature ablation (Table 7) convincingly addresses regime-specificity -- embedding benefit is robust across tau.
- Dynamic mining baseline (Table 11) rules out curriculum effects as the driver.
- Fusion head ablation (Table 10) cleanly separates training-time mining from inference-time features.
- The failure analysis (Table 13) with 79% help rate for cross-file dependencies provides good qualitative grounding.

**Weaknesses and gaps:**

**(a) Missing baselines.** The paper compares only 3 strategies (random, embedding, dataflow). Notable missing baselines:
- **BM25-based negatives** -- given the paper's entire motivation is correcting CoCoHaNeRe's BM25-proxy confusion, the absence of an actual BM25 negative baseline is a major oversight. The paper claims CoCoHaNeRe used BM25 mislabeled as embedding-distance, but never runs BM25 negatives to demonstrate the claimed -27pp harm and show it is BM25-specific.
- **ANCE-style dynamic embedding negatives** as a proper baseline (the dynamic mining experiment in Table 11 is close but only re-mines per epoch, not with an asynchronous index).
- **In-batch negatives** -- the simplest hard negative approach widely used in practice.

**(b) RepoBench-R (Table 5) lacks statistical significance testing.** Results are reported as single numbers without seeds, CIs, or p-values. Since these come from a single checkpoint per strategy, the numbers could reflect checkpoint variance rather than strategy effects.

**(c) SWE-bench evaluation uses only Qwen checkpoints.** The downstream evaluation (Table 3) tests only Qwen-based retrievers. Given the paper's central claim about encoder-strategy interaction, testing StarCoder checkpoints on SWE-bench would strengthen or appropriately bound the claims.

**(d) Table 14 (inference-time method comparison) is purely conceptual.** This is acknowledged in the paper, but the taxonomy table occupying a full table slot with no empirical content weakens the experimental section. It belongs in Discussion only.

### 3. Reproducibility

**Adequate for main experiments, insufficient for CodeQL pipeline.**

- LoRA rank-16, 3 epochs, 5K training instances, 9 seeds, contrastive loss with temperature -- these are well-specified.
- The CodeQL extraction pipeline lacks critical details: which CodeQL CLI version, which QL pack version, what the exact query looks like (the bounded_dataflow.ql and call_graph.ql are in the artifacts but not described in the paper), how "2-hop connectivity" is computed from raw call edges, and how the 131 repos were selected from SWE-smith.
- The paper says "0% query timeout" but the project history (D023) reveals that CodeQL failed 100% on a different server due to version incompatibility, suggesting the pipeline is fragile and environment-dependent. This fragility should be disclosed.
- The exact split between train/val/test is not specified.
- The number of negatives per query (k) is not stated in the paper, though the code uses `num_negatives` as a parameter.

### 4. Weaknesses

**Major:**

1. **Z% inconsistency (78% vs 41%) is an internal contradiction** that undermines trust in the reported statistics. These refer to different denominators (conditional vs. pilot/hop-ablation) but the paper uses identical notation without clarification.

2. **Missing BM25 negative baseline.** The paper's headline contribution is correcting a misconception about embedding negatives being harmful (attributed to BM25 proxy), yet it never runs actual BM25 negatives. This is the single most important missing experiment -- it would directly validate or refute the central narrative.

3. **Low structural coverage (34.3%) is underreported.** The dataflow strategy falls back to embedding/random negatives for ~66% of instances. The measured +1.5pp average improvement on Qwen conflates instances with and without structural signal. Without stratified results (structural-available vs. fallback), the reader cannot assess the true magnitude of the structural contribution.

4. **Effect sizes are small and practically modest.** +2.3pp R@1 (embedding) and +1.5pp R@1 (dataflow) on Qwen are statistically significant but of limited practical impact. On SWE-bench, +2.3pp corresponds to ~7 additional resolved issues out of 300, with wide CIs ([0.4, 4.2]pp, Table 4). The paper frames these as meaningful but does not discuss the cost-benefit of the CodeQL extraction pipeline (which requires compiling every repo into a CodeQL database) relative to the modest gains.

5. **Dataflow benefit is not significant vs. embedding (Table 4: p=0.134).** The paper correctly notes this, but the claim that "dataflow provides conditional additional benefit" (Claim 2) rests on dataflow-vs-random significance, not dataflow-vs-embedding. Since embedding is strictly simpler (no CodeQL needed), a reader may reasonably ask: why bother with dataflow at all? The SWE-bench results (Table 3-4) show dataflow > embedding by +1.0pp but CI includes zero. The practical case for dataflow over embedding is weak.

**Minor:**

6. **Qwen2.5-Coder-3B described as "decoder-only" and StarCoder2-3B as "encoder-decoder"** -- StarCoder2 is actually decoder-only as well (GPT-style autoregressive). The paper claims these are "architecturally distinct" but the distinction is in pretraining data/procedure, not architecture class. This mischaracterization undermines the "cross-architecture" generalization claim.

7. **The "correcting CoCoHaNeRe" narrative is not fully substantiated.** The paper asserts CoCoHaNeRe used BM25 proxy, but does not cite specific evidence from the CoCoHaNeRe paper for this claim. Without direct evidence (e.g., quoting CoCoHaNeRe's method section), this is speculation presented as fact.

8. **Overfitting is acknowledged but not fully analyzed.** The project history reveals severe overfitting (train loss approaching 0, best checkpoint at step 1000 out of 4242). While early stopping mitigates this, the paper should discuss whether the overfitting pattern differs across strategies and whether it affects the validity of comparisons.

9. **RepoBench-R is a code completion benchmark**, not a bug-fixing/retrieval benchmark. Using it as an "external validity" test conflates task domains.

### 5. Questions for Authors

Q1: The Z% is reported as 78% in Section 3.3 and 41% in Section 4.9 (and in the hop ablation table). Can you clarify which denominator each uses and report both conditional and unconditional Z% consistently?

Q2: What fraction of dataflow-strategy training instances actually receive dataflow-mined negatives vs. falling back to the padding logic (random fill)? Can you report R@1 stratified by whether the instance had structural data available?

Q3: You claim CoCoHaNeRe used BM25 as a proxy for embedding distance. Can you provide the specific textual evidence from their paper? Your own project history (D017, D024) suggests this insight came from discovering a bug in your *own* MVP pipeline, not from analyzing CoCoHaNeRe's code.

Q4: Why is an actual BM25 negative baseline absent, given that the entire narrative hinges on distinguishing BM25-proxy from true embedding-distance mining?

Q5: StarCoder2-3B is decoder-only, not encoder-decoder. Can you correct the architectural characterization and discuss what actually makes the two encoders' representation spaces differ (pretraining data composition, objective, tokenizer)?

Q6: For the SWE-bench evaluation (Table 3), was only a single run performed per strategy (best checkpoint), or were multiple seeds evaluated? If single-run, the bootstrap CI (Table 4) captures evaluation variance but not training variance.

Q7: The dataflow miner selects from the top-50 embedding-similar candidates, then filters by disconnection. How sensitive is performance to this top-K cutoff? At K=50, what fraction of candidates pass the disconnection filter on average?

Q8: Can you report per-strategy overfitting curves (train loss vs. val loss) to confirm that the comparison at best-checkpoint is not biased by differential overfitting rates?

### 6. Score and Confidence

**Score: 4 (Weak Accept)**

**Confidence: 4 (High)**

**Justification:**

The paper addresses a meaningful question -- what makes hard negatives work for code retrieval -- with above-average experimental rigor (54 training runs, 9 seeds, bootstrap CIs, extensive ablations). The representation saturation explanation for the encoder-strategy interaction (Claim 2) is the paper's most novel and insightful contribution, and the neg_difficulty margin data (pos_sim 0.986 vs 0.799) provides a compelling mechanistic account.

However, the paper's strongest claim (Claim 1: "correcting prior misconception") is not fully validated because the critical BM25 baseline is missing. The Z% inconsistency is a careless error that will erode reviewer trust. The practical value proposition of dataflow negatives is questionable: the effect vs. embedding is not significant (p=0.134), the CodeQL pipeline covers only 34% of instances, and the end-to-end SWE-bench improvement is modest (+3.3pp with wide CI). The architectural mischaracterization of StarCoder2 weakens the cross-encoder generalization narrative.

The paper is positioned as an empirical analysis (EMNLP archetype: "what works and why"), which lowers the bar for absolute effect sizes but raises it for thoroughness and correctness. The Z% inconsistency and missing BM25 baseline fall short of this bar. With revisions addressing these issues, the paper would be a solid accept. In its current form, it is a borderline contribution with genuine analytical depth undermined by execution gaps.

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac9668b7-627a-48bb-b6c3-989eeabb40dc",
  "isSidechain": true,
  "agentId": "a07c5538d1dec79e3",
  "requestId": "req_011Cb29Dtaq7dbgPcs68u9F3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d859de76-4dfd-4e6f-bb6d-f16e5158183b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "681a21c8-3dd5-46ee-8532-524b43b1f2d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tDzkEUUeJpF7gE8oiPjCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 89733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 867,
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
