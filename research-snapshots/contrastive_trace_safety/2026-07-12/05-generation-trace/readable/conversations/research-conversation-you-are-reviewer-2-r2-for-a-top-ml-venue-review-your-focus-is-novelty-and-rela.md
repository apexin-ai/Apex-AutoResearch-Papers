# Research conversation: You are **Reviewer 2 (R2)** for a top ML venue review. Your focus is **Novelty and Related Work**. ## Paper **Title:** "

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a24f4b66a47cd9d75.jsonl`
- **Structured JSON:** [`069de1fae3b4204c6363.json`](../../sessions/06/069de1fae3b4204c6363.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-14T08:31:34.273Z_

You are **Reviewer 2 (R2)** for a top ML venue review. Your focus is **Novelty and Related Work**.

## Paper
**Title:** "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"

**Summary:** The paper presents a controlled comparison of three hard negative mining strategies for contrastive code retrieval: (1) random, (2) embedding-distance, and (3) dataflow-aware (inter-procedural dataflow via CodeQL). These are tested across two code encoders: Qwen2.5-Coder-3B (saturated representation, pos_sim≈0.99) and StarCoder2-3B (healthy representation, pos_sim≈0.80). Both are LoRA fine-tuned for 3 epochs on SWE-smith data with InfoNCE loss.

**Key results:**
- RepoBench-R: Embedding-distance improves over random (+1.3pp Qwen, +0.5pp StarCoder R@1). Dataflow inconsistent.
- SWE-bench Lite: No significant downstream difference (all p>0.3).
- All claims hedged as "directional evidence" and "exploratory observation".
- Contributions: (1) controlled comparison framework, (2) representation geometry analysis, (3) CodeQL pipeline.

**Related Work (§2):**
- Hard negative mining: Cites ANCE (async mining), DPR (in-batch negatives), curriculum-based approaches. Claims CoCoHaNeRe conflated BM25 with embedding-distance. Claims to be "first controlled comparison using true embedding-distance negatives for code retrieval."
- Structure-aware code retrieval: Cites GraphCodeBERT, RepoFusion, GRACE, CodexGraph, LocAgent, ARISE. Claims novelty in using inter-procedural dataflow as training-time signal.
- Contrastive learning for code: Cites SweRank, SWE-Fixer. Claims extension by studying structure-grounded negatives.

**Discussion (§8):**
- Compares to CodexGraph (+5.2pp R@1) and LocAgent (26.3% resolve) — inference-time methods with much larger gains.
- Positions StructFuse as complementary (zero inference cost, training-time improvement).

**Limitations acknowledged (§8.2):**
- Only 2 encoders
- Diminishing returns at scale
- No downstream significance
- CodeQL coverage gaps
- CIs include zero for StarCoder

**Positioning:** EMNLP analysis paper, methodology contribution focus.

**Note:** All references in the PDF show as [?] — the bibliography appears broken.

## Your Task

Evaluate the paper's **novelty and related work** rigorously. Address:

1. **Novelty assessment**: How novel are the claims? Is "first controlled comparison" truly first? Is the representation geometry analysis a genuine insight or a post-hoc rationalization? Is the CodeQL pipeline a real contribution?
2. **Related work completeness**: Are important baselines or prior work missing? Is the positioning against prior work fair?
3. **Significance**: Given the small effect sizes and lack of downstream impact, does this paper contribute enough for a top venue? What is the expected impact on the field?
4. **Claim calibration**: Are the contributions overstated or understated relative to the evidence? The paper positions as "analysis paper" — does the analysis provide sufficient insight?
5. **Framing concerns**: Is the paper trying to present negative/null results as positive? Is the "directional evidence" framing appropriate or evasive?
6. **Broader context**: How does this fit in the broader landscape of code retrieval and hard negative mining research?

Consider these specific issues:
- The CoCoHaNeRe critique is central to the paper's motivation — is this critique well-substantiated?
- "Representation geometry" sounds impressive but boils down to observing that one encoder has higher pos_sim than another — is the analysis deep enough?
- The paper introduces a new method (StructFuse/dataflow negatives) but then shows it doesn't consistently work — is this a contribution?
- With only +0.5-1.3pp improvements that lack significance on half the setups, what is the practical contribution?
- The comparison to inference-time methods (Table 14) highlights StructFuse's weakness — +0.5-1.5pp vs +5.2pp for CodexGraph.
- Missing comparison to other training-time hard negative mining approaches (ANCE-style dynamic mining, curriculum learning, in-batch negatives)

## Output Format

Provide your review as structured text:
- **Summary** (2-3 sentences)
- **Strengths** (bulleted, 4-6 points)
- **Weaknesses** (bulleted, 6-10 points, be specific)
- **Questions for Authors** (3-5 specific questions)
- **Minor Issues** (formatting, typos, etc.)
- **Overall Assessment** (2-3 sentences)
- **Score** (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)
- **Confidence** (1-5: 1=low, 5=expert)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "e23e9f40-0991-4071-8297-3ed11c6bc9df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T08:31:34.278Z_

```json
{
  "parentUuid": "e23e9f40-0991-4071-8297-3ed11c6bc9df",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
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
  "uuid": "382132f4-5e55-4594-ac0b-a167fccc608b",
  "timestamp": "2026-05-14T08:31:34.278Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T08:31:37.378Z_



I'll start by reading the paper and related project files to ground my review in the actual content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "382132f4-5e55-4594-ac0b-a167fccc608b",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29eYgCiWGxBQJapxEcZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2b81f98-25e9-4e7a-b63b-1cb12c0ccf8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FntxrCFChty3nm2JGZUgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7075,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7075,
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

_source line 4 · 2026-05-14T08:31:38.955Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WSDZRWXfHAqmx2A4FFN3yi`</summary>

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
  "parentUuid": "f2b81f98-25e9-4e7a-b63b-1cb12c0ccf8c",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29eYgCiWGxBQJapxEcZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a8cd079-a6ca-4026-b6c5-86c228565f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FntxrCFChty3nm2JGZUgH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7075,
      "cache_read_input_tokens": 8249,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7075
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 126,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7075,
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

_source line 5 · 2026-05-14T08:31:38.958Z_

<details><summary>↩ Tool result · `toolu_01WSDZRWXfHAqmx2A4FFN3yi`</summary>

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
  "parentUuid": "3a8cd079-a6ca-4026-b6c5-86c228565f50",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "73ab9373-68a3-4d8c-a263-5965da0a0bfe",
  "sourceToolAssistantUUID": "3a8cd079-a6ca-4026-b6c5-86c228565f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T08:31:41.758Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Ndv4g7f4cNouyLbaxZwapA`</summary>

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
  "parentUuid": "73ab9373-68a3-4d8c-a263-5965da0a0bfe",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29ets95U3HbFAUBNvVm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e278049-4a7e-459d-b467-db21405b8f9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvZHHmxSpuxAxsNw5g6FHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-14T08:31:41.899Z_

<details><summary>↩ Tool result · `toolu_01Ndv4g7f4cNouyLbaxZwapA`</summary>

```text
{"result":"# 项目 structfuse-context 概况\n\n## 实验状态 (31 个)\n\n- **p2b_eval_4runs_pool50**: DONE (success) — \n- **d007_50repo_overlap**: DONE (success) — \n- **p2b_5reruns**: DONE (success) — \n- **p2b_eval_4runs_v2**: DONE (success) — \n- **p2b-all-9runs**: DONE (killed) — \n- **p2b-smoke8**: DONE (killed) — \n- **p2b-smoke7**: DONE (killed) — \n- **p2b-smoke6**: DONE (killed) — \n- **p2b-smoke5**: DONE (killed) — \n- **p2b-smoke4**: DONE (killed) — \n- **p2b-smoke3**: DONE (killed) — \n- **p2b-smoke2**: DONE (killed) — \n- **p2b-smoke-test**: DONE (killed) — \n- **mvp_p2a_linear_proxy**: DONE (success) — \n- **mvp_p1_codeql_feasibility**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\n- **m1_extraction** (success): —\n\n## 趋势\n成功 10 / 负向 2 / 失败 2 / 共 28\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb1-42106: 无 GPU 信息\n\n## 告警\n- p2b-smoke-test: 已被终止 — unknown\n- p2b-smoke2: 已被终止 — unknown\n- p2b-smoke3: 已被终止 — unknown\n- p2b-smoke4: 已被终止 — unknown\n- p2b-smoke5: 已被终止 — unknown\n- p2b-smoke6: 已被终止 — unknown\n- p2b-smoke7: 已被终止 — unknown\n- p2b-smoke8: 已被终止 — unknown\n- p2b-all-9runs: 已被终止 — unknown\n- mvp_p2b_contrastive_training: 已被终止 — unknown\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\n- p2b_eval_all: 已被终止 — unknown\n- m2_early_pilot: 已被终止 — unknown\n- m2_early_pilot_v2: 训练失败 — unknown\n- m2_early_pilot_v3: 已被终止 — unknown\n- m1_reextract: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e278049-4a7e-459d-b467-db21405b8f9e",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "fd96e184-2ce4-4064-b73c-efc0d368b539",
  "sourceToolAssistantUUID": "5e278049-4a7e-459d-b467-db21405b8f9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T08:31:42.680Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01REkonC6mq8tzLfiC7nciiu`</summary>

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
  "parentUuid": "fd96e184-2ce4-4064-b73c-efc0d368b539",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29ets95U3HbFAUBNvVm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6400949-efac-4f93-9a98-53db39c0d36f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvZHHmxSpuxAxsNw5g6FHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 9 · 2026-05-14T08:31:42.695Z_

<details><summary>↩ Tool result · `toolu_01REkonC6mq8tzLfiC7nciiu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml\", \"content\": \"# StructFuse — Related Work Literature Map\\n# 最后更新: 2026-05-12\\n# 说明: 只收录项目文件中已引用的 + 确定存在的知名论文。不确定的信息标注\\\"需验证\\\"。\\n\\ncategories:\\n\\n  # ==========================================================================\\n  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem\\n  # ==========================================================================\\n  code_retrieval_bug_fixing:\\n    description: \\\"SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法\\\"\\n    papers:\\n\\n      - title: \\\"SWE-bench: Can Language Models Resolve Real-World GitHub Issues?\\\"\\n        authors: \\\"Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline  # StructFuse 的评估基准\\n        summary: \\\"从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。\\\"\\n\\n      - title: \\\"SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press\\\"\\n        venue: NeurIPS\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。\\\"\\n\\n      - title: \\\"AutoCodeRover: Autonomous Program Improvement\\\"\\n        authors: \\\"Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury\\\"\\n        venue: ISSTA\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。\\\"\\n\\n      - title: \\\"Agentless: Demystifying LLM-based Software Engineering Agents\\\"\\n        authors: \\\"Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: competitor\\n        summary: \\\"无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。\\\"\\n\\n      - title: \\\"SWE-smith: Scaling Data for Software Engineering Agents\\\"\\n        authors: \\\"John Yang, Carlos E. Jimenez, Alexander Wettig, Karthik Narasimhan, Ofir Press\\\"\\n        venue: arXiv\\n        year: 2025\\n        relation: building-block  # StructFuse 用其 repo 做数据提取\\n        summary: \\\"自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。\\\"\\n        note: \\\"需验证 venue（可能已投稿会议）\\\"\\n\\n      - title: \\\"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems\\\"\\n        authors: \\\"Tianyang Liu, Canwen Xu, Julian McAuley\\\"\\n        venue: ICLR\\n        year: 2024\\n        relation: baseline\\n        summary: \\\"Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务，StructFuse 可用于评估。\\\"\\n        note: \\\"需验证年份和 venue\\\"\\n\\n  # ==========================================================================\\n  # Category 2: Hard Negative Mining in Contrastive Learning\\n  # ==========================================================================\\n  hard_negative_mining:\\n    description: \\\"对比学习中 hard negative 挖掘策略，以及代码领域的对比学习\\\"\\n    papers:\\n\\n      - title: \\\"Dense Passage Retrieval for Open-Domain Question Answering\\\"\\n        authors: \\\"Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih\\\"\\n        venue: EMNLP\\n        year: 2020\\n        relation: background\\n        summary: \\\"DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式，是 StructFuse 对比训练的方法论基础。\\\"\\n\\n      - title: \\\"Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval\\\"\\n        authors: \\\"Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，是 StructFuse 的 baseline negative 策略之一。\\\"\\n\\n      - title: \\\"SimCLR: A Simple Framework for Contrastive Learning of Visual Representations\\\"\\n        authors: \\\"Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton\\\"\\n        venue: ICML\\n        year: 2020\\n        relation: background\\n        summary: \\\"视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。\\\"\\n\\n      - title: \\\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\\\"\\n        authors: \\\"Nils Reimers, Iryna Gurevych\\\"\\n        venue: EMNLP\\n        year: 2019\\n        relation: background\\n        summary: \\\"Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。\\\"\\n\\n      - title: \\\"Mining Hard Negatives with Curriculum for Dense Retrieval\\\"\\n        authors: \\\"需验证\\\"\\n        venue: \\\"需验证\\\"\\n        year: \\\"需验证\\\"\\n        relation: background\\n        summary: \\\"课程学习式 hard negative 挖掘，从易到难训练检索器。\\\"\\n        note: \\\"需验证完整信息\\\"\\n\\n  # ==========================================================================\\n  # Category 3: Program Analysis for ML\\n  # ==========================================================================\\n  program_analysis_for_ml:\\n    description: \\\"静态分析辅助 ML，结构信息在代码表示学习中的应用\\\"\\n    papers:\\n\\n      - title: \\\"CodeQL: Semantic Code Analysis Engine\\\"\\n        authors: \\\"GitHub / Semmle\\\"\\n        venue: \\\"Tool (open-source)\\\"\\n        year: 2019\\n        relation: building-block  # StructFuse 核心组件\\n        summary: \\\"基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。\\\"\\n\\n      - title: \\\"code2vec: Learning Distributed Representations of Code\\\"\\n        authors: \\\"Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav\\\"\\n        venue: POPL\\n        year: 2019\\n        relation: background\\n        summary: \\\"用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。\\\"\\n\\n      - title: \\\"code2seq: Generating Sequences from Structured Representations of Code\\\"\\n        authors: \\\"Uri Alon, Shaked Brody, Omer Levy, Eran Yahav\\\"\\n        venue: ICLR\\n        year: 2019\\n        relation: background\\n        summary: \\\"code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。\\\"\\n\\n      - title: \\\"Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree\\\"\\n        authors: \\\"Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin\\\"\\n        venue: SANER\\n        year: 2020\\n        relation: background\\n        summary: \\\"用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"GraphCodeBERT: Pre-training Code Representations with Data Flow\\\"\\n        authors: \\\"Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou\\\"\\n        venue: ICLR\\n        year: 2021\\n        relation: background\\n        summary: \\\"在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。\\\"\\n\\n  # ==========================================================================\\n  # Category 4: Code Embeddings / Code Search\\n  # ==========================================================================\\n  code_embeddings_search:\\n    description: \\\"代码嵌入模型和代码搜索方法\\\"\\n    papers:\\n\\n      - title: \\\"CodeSearchNet Challenge: Evaluating the State of Semantic Code Search\\\"\\n        authors: \\\"Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt\\\"\\n        venue: arXiv\\n        year: 2019\\n        relation: background\\n        summary: \\\"代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。\\\"\\n\\n      - title: \\\"CodeBERT: A Pre-Trained Model for Programming and Natural Languages\\\"\\n        authors: \\\"Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou\\\"\\n        venue: EMNLP (Findings)\\n        year: 2020\\n        relation: background\\n        summary: \\\"首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。\\\"\\n\\n      - title: \\\"UniXcoder: Unified Cross-Modal Pre-training for Code Representation\\\"\\n        authors: \\\"Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin\\\"\\n        venue: ACL\\n        year: 2022\\n        relation: background\\n        summary: \\\"统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。\\\"\\n\\n      - title: \\\"StarCoder: May the Source Be with You!\\\"\\n        authors: \\\"Raymond Li, Loubna Ben Allal, et al. (BigCode)\\\"\\n        venue: TMLR\\n        year: 2023\\n        relation: background\\n        summary: \\\"大规模开源代码 LLM，广泛用于代码嵌入的 backbone。\\\"\\n        note: \\\"需验证 venue（可能是 arXiv 或其他）\\\"\\n\\n      - title: \\\"Code Llama: Open Foundation Models for Code\\\"\\n        authors: \\\"Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)\\\"\\n        venue: arXiv\\n        year: 2023\\n        relation: background\\n        summary: \\\"Meta 的代码大模型系列，基于 Llama 2 微调。\\\"\\n\\n      - title: \\\"Qwen2.5-Coder Technical Report\\\"\\n        authors: \\\"Qwen Team (Alibaba)\\\"\\n        venue: arXiv\\n        year: 2024\\n        relation: building-block  # StructFuse 用 Qwen2.5-Coder-3B 做检索器\\n        summary: \\\"Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。\\\"\\n        note: \\\"需验证确切标题和年份\\\"\\n\\n      - title: \\\"Contrastive Learning for Source Code with Structural and Functional Properties\\\"\\n        authors: \\\"Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty\\\"\\n        venue: ACL (Findings)\\n        year: 2022\\n        relation: background\\n        summary: \\\"代码对比学习中利用结构/功能属性构建正负样本对。\\\"\\n        note: \\\"需验证作者和 venue\\\"\\n\\n      - title: \\\"BM25\\\"\\n        authors: \\\"Stephen Robertson, Hugo Zaragoza\\\"\\n        venue: \\\"Foundations and Trends in Information Retrieval\\\"\\n        year: 2009\\n        relation: baseline\\n        summary: \\\"经典稀疏检索方法，StructFuse 的 baseline 之一。Phase 2a 实验发现 BM25 在 bug fixing 定位中可能有误导性（负系数）。\\\"\\n\\n# ==========================================================================\\n# 待补充\\n# ==========================================================================\\n# 以下论文可能相关，待确认后补充：\\n# - FAISS (Johnson et al., 2019) — ANN 检索库，StructFuse 评估可能用到\\n# - Tree-sitter — 增量解析器，与 CodeQL 互补\\n# - Aider / Moatless Tools — SWE-bench 上的其他代码检索方法\\n# - CoSQA (Huang et al., 2021) — 代码搜索 QA 数据集\\n# - DeepSeek-Coder — 另一个可能的 backbone 对比\\n\", \"total_chars\": 9647, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6400949-efac-4f93-9a98-53db39c0d36f",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "6c241870-b830-402b-8465-6596061a346e",
  "sourceToolAssistantUUID": "f6400949-efac-4f93-9a98-53db39c0d36f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T08:31:43.322Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LY4GzrECHuLeNrVFP88fpD`</summary>

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
  "parentUuid": "6c241870-b830-402b-8465-6596061a346e",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29ets95U3HbFAUBNvVm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f5e52cb-9e1e-4d66-b153-bdfd6de3d7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XvZHHmxSpuxAxsNw5g6FHM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15324,
      "output_tokens": 254,
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
          "output_tokens": 254,
          "cache_read_input_tokens": 15324,
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T08:31:43.336Z_

<details><summary>↩ Tool result · `toolu_01LY4GzrECHuLeNrVFP88fpD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \\\"harm\\\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\\n\\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\\n\\n## Story Spine\\n\\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\\n\\n- **Existing approaches & gaps**:\\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\\n\\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\\n\\n- **Headline result template**: \\\"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\\\"\\n\\n## Core Insight\\n\\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\\n\\n## Dual-Pillar Motivation\\n\\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\\n\\n## Formal Definition\\n\\nGiven retrieval domain D, structural graph G, similarity function s, query q:\\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\\n\\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\\n\\n## Title Options\\n\\n- Primary: \\\"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\\\"\\n- Alternative: \\\"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\\\"\\n- Backup: \\\"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\\\"\\n\\n## Venue Fit\\n\\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \\\"Do Language Models...\\\" papers). Contribution is understanding, not just a new method.\\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\\n3. **Against \\\"incremental\\\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response | Evidence |\\n|---------|----------|----------|\\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\\n| \\\"Complementary signal\\\" overstatement | Temper: \\\"conditionally beneficial\\\" not \\\"always complementary\\\" | Writing discipline |\\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\\n\\n## Evidence Status\\n\\n### Confirmed findings (basis for claims):\\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\\n- plan_006: CodeQL scalability confirmed at 123-repo scale\\n\\n### In progress:\\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\\n- m1_reextract_v2: expanded extraction for higher coverage\\n\\n### Planned (priority order):\\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\\n- plan_014: Temperature ablation (Dream reviewer concern)\\n- plan_004: RepoBench-R second benchmark\\n- plan_015: Dynamic mining baseline\\n- plan_007/008/009: Additional ablations\\n\\n## Contingency (if full M2 results weaken claims)\\n\\n### All 18 runs confirm pilot pattern: Best case\\n- Full statistical power, paper as framed above\\n- Target: EMNLP Main\\n\\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\\n- Drop Claim 2 to analysis observation\\n- Paper becomes: \\\"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\\\"\\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\\n\\n### Embedding mining also loses advantage at full scale: Major reassessment needed\\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\\n- If confirmed: negative result paper — \\\"Why Hard Negative Mining Doesn't Scale for Code Retrieval\\\"\\n- Discuss with user before committing direction\\n\\n## Deprecated Claims (with reason)\\n\\n- ~~\\\"Embedding-distance hard negatives actively harm code retrieval\\\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\\n\", \"total_chars\": 9391, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f5e52cb-9e1e-4d66-b153-bdfd6de3d7a3",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "af80e195-5f96-4b9b-98d9-1ddeca25b83b",
  "sourceToolAssistantUUID": "2f5e52cb-9e1e-4d66-b153-bdfd6de3d7a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-14T08:31:49.031Z_

Now let me read the actual paper artifacts and additional project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af80e195-5f96-4b9b-98d9-1ddeca25b83b",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29fDb2PthEGXfWudjQG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "894681e7-be75-4c5e-bc4a-e4c247bf25f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ec38dpQ3h9j7rvgjk3YHhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8649,
      "cache_read_input_tokens": 16772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8649,
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

_source line 13 · 2026-05-14T08:31:50.938Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L9Nx4VTBzpAstFWt7RHL1i`</summary>

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
  "parentUuid": "894681e7-be75-4c5e-bc4a-e4c247bf25f4",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29fDb2PthEGXfWudjQG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19642ce1-767c-43cd-9966-d888ab2b3225",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ec38dpQ3h9j7rvgjk3YHhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8649,
      "cache_read_input_tokens": 16772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8649,
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

_source line 14 · 2026-05-14T08:31:50.952Z_

<details><summary>↩ Tool result · `toolu_01L9Nx4VTBzpAstFWt7RHL1i`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| m2_full_starcoder | Full M2 StarCoder: 3 strategies × 3 seeds on full M1 data. Cross-encoder validation — if embedding > random holds for both Qwen and StarCoder, method is encoder-agnostic. Resolves plan_013 pilot negative (dataflow encoder-dependent). | — | — | — |\\n| m2_full_qwen | Full M2 Qwen: 3 strategies (random/embedding/dataflow) × 3 seeds on full M1 data (~11K train/seed). Statistical validation of pilot signal (embedding > random +2pp). Go/no-go for paper claims per D018. | — | — | — |\\n| m1_reextract_v2 | M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **neg_difficulty_analysis** (success): Negative difficulty distribution analysis: 用预训练 Qwen2.5-Coder-3B 和 StarCoder2-3B 计算 3 策略 (random/embedding/dataflow) 的 query-negative/positive cosine similarity，分析 pretrained representation separability 跨编码器差异。MAX_LENGTH=2048 匹配训练设置。\\n- **m1_reextract** (failed): M1 重提取：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。 ← 基于 m1_extraction\\n- **m1_extraction** (success): —\\n\\n## 趋势\\n成功 10 / 负向 2 / 失败 2 / 共 28\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-42106: 无 GPU 信息\\n\\n## 告警\\n- p2b-smoke-test: 已被终止 — unknown\\n- p2b-smoke2: 已被终止 — unknown\\n- p2b-smoke3: 已被终止 — unknown\\n- p2b-smoke4: 已被终止 — unknown\\n- p2b-smoke5: 已被终止 — unknown\\n- p2b-smoke6: 已被终止 — unknown\\n- p2b-smoke7: 已被终止 — unknown\\n- p2b-smoke8: 已被终止 — unknown\\n- p2b-all-9runs: 已被终止 — unknown\\n- mvp_p2b_contrastive_training: 已被终止 — unknown\\n- mvp_p2b_contrastive_v2: 已被终止 — unknown\\n- p2b_eval_all: 已被终止 — unknown\\n- m2_early_pilot: 已被终止 — unknown\\n- m2_early_pilot_v2: 训练失败 — unknown\\n- m2_early_pilot_v3: 已被终止 — unknown\\n- m1_reextract: 训练失败 — unknown\\n\", \"total_chars\": 1895, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19642ce1-767c-43cd-9966-d888ab2b3225",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "a5c4d533-f965-45c1-9f2c-06d1db165bd9",
  "sourceToolAssistantUUID": "19642ce1-767c-43cd-9966-d888ab2b3225",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T08:31:51.327Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RFmyEUfPTRMorkE9Gx2nmi`</summary>

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
  "parentUuid": "a5c4d533-f965-45c1-9f2c-06d1db165bd9",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29fDb2PthEGXfWudjQG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c8857fd-899a-4d43-8a9b-2ceced63ffee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ec38dpQ3h9j7rvgjk3YHhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8649,
      "cache_read_input_tokens": 16772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8649,
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

_source line 16 · 2026-05-14T08:31:51.348Z_

<details><summary>↩ Tool result · `toolu_01RFmyEUfPTRMorkE9Gx2nmi`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c8857fd-899a-4d43-8a9b-2ceced63ffee",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "b09ed9ba-9486-4dc3-853f-a5d3f150c419",
  "sourceToolAssistantUUID": "1c8857fd-899a-4d43-8a9b-2ceced63ffee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T08:31:51.609Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EHi8RarCdmQDo2WSWMBvSb`</summary>

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
  "parentUuid": "b09ed9ba-9486-4dc3-853f-a5d3f150c419",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29fDb2PthEGXfWudjQG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27752135-924d-4f85-aeac-367221d32b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ec38dpQ3h9j7rvgjk3YHhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8649,
      "cache_read_input_tokens": 16772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8649,
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

_source line 18 · 2026-05-14T08:31:51.620Z_

<details><summary>↩ Tool result · `toolu_01EHi8RarCdmQDo2WSWMBvSb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 28\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  rationale: Reviewer 核实 nvidia-smi 发现 run_mvp.py 在 GPU 5 上运行 9.3GB，而项目分配的 cuda:4\\n    完全空闲。违反 L1 红线（GPU 资源边界）。要求 Agent 立即 kill 进程、修复所有脚本强制 CUDA_VISIBLE_DEVICES=4、排查\\n    dry-run 是否也越界。\\n  related_experiments: []\\n  depends_on: []\\n- id: D006\\n  date: 2026-05-12 17:24 UTC\\n  summary: P2b pass criteria 调整：recall@5→recall@1，pool_size 26→50+，阈值 ≥2pp 不变\\n  rationale: Eval v2 (pool_size=26) 显示 random recall@5 已达 98.4-99.2%，原标准\\\"dataflow\\n    recall@5 > random ≥2pp\\\"数学上几乎不可能达标（天花板仅 0.8-1.6pp 空间）。recall@1 有更大区分度（random mean\\n    93.97%），且是更严格的排序指标。同时扩大 pool_size 至 50+ 使 recall@5/10 也获得有效梯度。新标准：dataflow_aware\\n    recall@1 > random recall@1 ≥2pp in ≥2/3 seeds，pool_size=50。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: random recall@1 mean=0.940, emb_dist recall@1=0.669 at pool=26; recall@5\\n      ceiling\\n  depends_on:\\n  - D002\\n- id: D007\\n  date: 2026-05-12 19:52 UTC\\n  summary: MVP P2b dataflow 策略不可验证：connected⊆gold 导致数据相同。决定：50-repo 规模验证 + Scheme\\n    B 备份\\n  rationale: 修复 build_p2b_data.py 后重新生成数据，train_dataflow.jsonl 仍与 train_embedding.jsonl\\n    完全相同。根因：8 个 MVP repos 中 dataflow 连接文件全部是 gold 文件的子集（connected-but-not-gold = 0），non_pos\\n    过滤无差异。这不是方法缺陷而是规模问题——小 repo 紧耦合，2-hop 连接集≈gold 集。P1（Fisher p=1.54e-7）和 P2a（AUC=0.78）仍有效，说明\\n    dataflow connectivity 有信号，只是 MVP 规模不足以分离 connected-but-not-gold 子集。决策：(1) 立即跑\\n    50-repo 样本的 overlap 统计（CPU, ~2-4h），确认大规模下 connected⊃gold；(2) 并行准备 Scheme B（distance-weighted\\n    negatives）作为 pivot 备选；(3) overlap>20% 实例有 connected≠gold → 进入全量 M1 提取；overlap≈100%\\n    → pivot to Scheme B。\\n  related_experiments:\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: trigger\\n    result: dataflow≡embedding 因 connected⊆gold\\n  depends_on:\\n  - D006\\n  - D004\\n- id: D008\\n  date: 2026-05-12 20:38 UTC\\n  summary: MVP 条件性通过：P1+P2a PASS，P2b dataflow 在 MVP 规模不可测但 50-repo 规模验证确认方法可行（Z=40.8%）。进入\\n    research 阶段。\\n  rationale: MVP 三阶段结果：P1 PASS（timeout 0%, Fisher p=1.54e-7, 75% instance recall）；P2a\\n    PASS（AUC 0.78, BM25 系数为负）；P2b 部分有效——random>>embedding（-27pp recall@1 at pool=26,\\n    -3.7pp at pool=50）确认 naive hard negatives 有害，但 dataflow vs random 因 connected⊆gold\\n    无法在 8 repos 上区分。50-repo 规模验证 Z=40.8%（中型 repo 55.7%），timeout 4%，确认方法在全量数据上可行。Kill\\n    criteria 均未触发。P2b dataflow 对比将在 M2 全量训练中完成。\\n  related_experiments:\\n  - exp_id: mvp_p1_codeql_feasibility\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2a_linear_proxy\\n    role: evidence\\n    result: PASS\\n  - exp_id: mvp_p2b_contrastive_training\\n    role: evidence\\n    result: partial - random>>emb confirmed, dataflow untestable at MVP scale\\n  depends_on:\\n  - D007\\n  - D006\\n  - D004\\n- id: D009\\n  date: 2026-05-12 22:04 UTC\\n  summary: Dream 审稿完成：best=Weak Accept, median=Weak Reject, worst=Reject。批准 P0 启动，但\\n    plan 需增补 5 个 dream-derived 实验\\n  rationale: 三档共识问题：(1) 单编码器无法支撑 generality claim，需加 StarCoder/CodeBERT；(2) static\\n    vs dynamic embedding mining 是潜在 confound；(3) τ=0.05 可能 regime-specific；(4) SWE-bench\\n    +2pp 需 bootstrap CI；(5) abstract \\\"complementary\\\" 需降调。关键风险变量是 M1 的 Z%：≥35% best\\n    framing 成立，20-35% pivot 到 Claim 2 headline，<20% 需重大调整。已在 experiment_plan.yaml\\n    增加 plan_013-017（+35h GPU），paper_framing.md 增加 contingency framing。P0 实验（M1 已在跑）可继续，不需\\n    re-dream。\\n  related_experiments:\\n  - exp_id: dream_20260512T204322\\n    role: dream_simulate\\n    result: best=WA, median=WR, worst=R\\n  depends_on:\\n  - D008\\n- id: D010\\n  date: 2026-05-12 22:09 UTC\\n  summary: plan_013 (second encoder) 从 P1 升级至 P0，headline template 降调修复\\n  rationale: Reviewer 指出 single encoder 是 best→accept 的关键区分因素，在 best-R1-W1 和 median-R2-W5\\n    两档都出现。P1 排期可能导致论文缺少 generality 证据而被 WR。升级后 M2 完成即可并行启动 plan_013。同时修复 headline\\n    template \\\"cannot recover\\\" → \\\"complementary signal not captured by\\\"。\\n  related_experiments:\\n  - exp_id: plan_013\\n    role: priority_upgrade\\n    result: P1→P0\\n  depends_on:\\n  - D009\\n- id: D011\\n  date: 2026-05-13 01:38 UTC\\n  summary: Z%=74.0% 确认 Best Framing — Claim 1 为 headline，批准 M2 早期训练\\n  rationale: M1 部分数据（24/222 repos, 5128 instances）Z%=74.0%，远超 ≥35% 阈值。对比 D007 的 40.8%（50\\n    SWE-bench repos），SWE-Smith 数据集跨文件依赖密度更高。Best framing 成立：Claim 1 (\\\"structure-grounded\\n    negatives outperform\\\") 为 headline。批准在当前 5K instances 上做 M2 早期训练 pilot（3 strategies\\n    × 1 seed），利用 cuda:4 空闲期获取早期信号，不等全量 M1（还需 ~46h）。磁盘已清理至 61GB free (64%)，足够训练。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: Z%=74.0% at 24/222 repos\\n  - exp_id: d007_50repo_overlap\\n    role: baseline\\n    result: Z%=40.8% on SWE-bench 50 repos\\n  depends_on:\\n  - D009\\n  - D010\\n- id: D012\\n  date: 2026-05-13 02:11 UTC\\n  summary: Kill m2_early_pilot_v3 (PID 897752) — 第二次 GPU 越界 (cuda:0)\\n  rationale: Reviewer 发现 m2_early_pilot_v3 在 cuda:0 运行（PID 897752, 17100 MiB），项目仅分配\\n    cuda:4。这是第二次 GPU 越界（第一次 D005 在 GPU 5）。立即 kill 并标记 killed。同时 m2_early_pilot_v2\\n    因 wandb API key error 已崩溃标记 FAILED。当前唯一合法训练为 PID 795791 (m2_early_pilot, cuda:4)。要求\\n    Agent 排查越界原因并确保后续脚本强制 CUDA_VISIBLE_DEVICES=4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot_v3\\n    role: violated\\n    result: killed - GPU 越界 cuda:0\\n  - exp_id: m2_early_pilot_v2\\n    role: failed\\n    result: wandb API key error\\n  - exp_id: m2_early_pilot\\n    role: active\\n    result: PID 795791 on cuda:4, running\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-13 02:50 UTC\\n  summary: 服务器迁移：cqa1-21977 cuda:4 → bjb1-42106 cuda:0/1 (RTX PRO 6000 96GB×2)\\n  rationale: Manager 分配独立服务器 bjb1-42106（2x RTX PRO 6000 96GB）。迁移策略：(1) M1 提取继续在 cqa1-21977\\n    CPU 上完成（不中断），(2) 新服务器立即搭建环境+同步代码+下载模型，(3) M2 early pilot 在 cqa1-21977 cuda:4 跑完后所有\\n    GPU 工作转到新服务器，(4) 通知 Manager 释放 cuda:4。RTX PRO 6000 96GB 彻底解决 M3a VRAM 问题（Qwen3.6-27B\\n    不再需要 fallback），2 卡可并行 M2 全量 + plan_013。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: in_progress\\n    result: finishing on cqa1-21977 cuda:4\\n  - exp_id: m1_extraction\\n    role: in_progress\\n    result: CPU only, stays on cqa1-21977\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-13 04:44 UTC\\n  summary: Kill m2_early_pilot (PID 795791) — 过拟合+卡死，bjb1 m2_embed_verify 取代\\n  rationale: m2_early_pilot 在 cqa1 cuda:4 上仅完成 random 策略（best val_loss=0.5879 at step\\n    1500，之后持续过拟合到 0.728）。进程在 step 4000 卡死 45+ min。OOM 干扰（另一进程在同 GPU 启动）。embedding_distance\\n    和 dataflow_aware 策略未启动。bjb1 上的 m2_embed_verify 使用 true embedding mining + 更大参数（negatives=7,\\n    seq_len=2048, batch=8）+ eval bug fix，将完全取代此 pilot。通知 Manager 释放 cqa1 cuda:4。\\n  related_experiments:\\n  - exp_id: m2_early_pilot\\n    role: killed\\n    result: random best val_loss=0.5879, overfitting after step 1500\\n  - exp_id: m2_embed_verify\\n    role: replacement\\n    result: preparing on bjb1 cuda:1\\n  depends_on:\\n  - D011\\n  - D013\\n- id: D015\\n  date: 2026-05-13 11:43 UTC\\n  summary: 全量 Z%=78.0%（条件）确认 Best Framing；Coverage 34.3% 需论文讨论\\n  rationale: 全量 M1（123/131 repos, 44,173 instances）统计：15,153 instances 有结构数据（34.3%），其中\\n    11,825 有 connected-but-not-gold 文件（条件 Z%=78.0%，高于 pilot 72.5%）。条件 Z% 远超 35% 阈值，Best\\n    Framing（Claim 1 as headline）完全成立。但 Coverage 仅 34.3%——65.7% instances CodeQL/Beniget\\n    未产出结构连接，论文需讨论此局限性并限定 claim 范围为\\\"有结构数据的 instances\\\"。\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: data_source\\n    result: 123/131 repos, 44173 instances, 15897 structural\\n  - exp_id: plan_006_scalability\\n    role: prior_pilot\\n    result: pilot Z%=72.5% on 29 repos\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-13 15:24 UTC\\n  summary: 'Reviewer Critical: m2_embed_verify 和 plan_013_starcoder 实际已完成全部 3 策略，registry\\n    错误标记为 failed'\\n  rationale: Reviewer 直接从服务器日志验证：两个实验的 dataflow 策略均已完成（\\\"All 3 strategies completed\\\"），EXIT_CODE\\n    异常发生在训练完成之后（wrapper 脚本问题）。关键数据：(1) Qwen dataflow peak R@1=0.5584 (+2.27pp vs random)，支撑\\n    Claim 1；(2) StarCoder dataflow R@1=0.4869 < random 0.4922，encoder-agnostic claim\\n    受挑战；(3) 两个编码器的 dataflow 策略均严重过拟合（train loss→0）。已派 Agent 紧急修正 registry + 收集完整 metrics\\n    + 验证 StarCoder random 数据来源。方向决策待 Agent 汇报验证数据后确定。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 实际完成（3 strategies all done），Qwen dataflow peak R@1=0.5584\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 实际完成（3 strategies all done），StarCoder dataflow R@1=0.4869 < random 0.4922\\n  depends_on: []\\n- id: D017\\n  date: 2026-05-13 16:03 UTC\\n  summary: Pilot 结果验证完成：embedding > random 跨编码器一致；dataflow 需按两种 checkpoint 标准报告；Claim\\n    2 需修订\\n  rationale: 'Reviewer 验证 18 个指标全部精确匹配。核心发现：(1) embedding > random 在 Qwen (+2.0pp)\\n    和 StarCoder (+1.6pp) 上一致，是最稳健结论；(2) dataflow 排名取决于 checkpoint 选择——按 val_loss:\\n    embedding > dataflow > random (Qwen)，按 peak R@1: dataflow > embedding > random\\n    (Qwen)；(3) StarCoder dataflow final eval 追平 embedding (0.5078=0.5078)，\\\"embedding\\n    consistently beats dataflow\\\" 不成立；(4) Claim 2 (\\\"embedding harms\\\") 在 true embedding\\n    mining 下不复现，仅在 MVP BM25 proxy 下成立。全量 M2 训练需报告两种 checkpoint 标准下的结果，避免 cherry-picking\\n    质疑。Paper framing 修订延后至全量 M2 结果出来后。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: primary\\n    result: 'Qwen: embedding(0.5557) > dataflow(0.5436) > random(0.5357) by val_loss;\\n      dataflow peak(0.5584) > embedding(0.5557) by R@1'\\n  - exp_id: plan_013_starcoder\\n    role: primary\\n    result: 'StarCoder: embedding(0.5078) > random(0.4922) > dataflow(0.4869) by val_loss;\\n      dataflow final(0.5078) = embedding'\\n  depends_on:\\n  - D016\\n- id: D018\\n  date: 2026-05-13 16:04 UTC\\n  summary: 不做预判性 framing pivot，full M2 (18 runs) 是 go/no-go 唯一判据；双 checkpoint 标准；准备\\n    B/C 两条后备路线\\n  rationale: Pilot 仅 24 repos / 1 seed，<2pp delta 统计功效不足以支持强 claim 或否决原假设。Full M2\\n    (131 repos × 3 strategies × 3 seeds × 2 encoders = 18 runs) 提供 3-seed 统计功效，是唯一可信判据。不选\\n    Agent 提议的 A/B/C 任何一个——过早锁定叙事会限制后续解读空间。数据构建已在进行，不浪费时间在 framing 讨论上。Full M2 结果出来后根据实际数据\\n    pattern 决定：(a) dataflow 跨编码器一致 > random → 原 framing 修正后可用；(b) dataflow 不一致但 embedding\\n    一致 → 方案 B 或 C；(c) 所有差异不显著 → 需要更大规模实验或 pivot。同时要求 dual checkpoint (best-val-loss\\n    + best-R@1) 和 3-seed CI 确保结果可信。\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: pilot underpowered (1 seed, 24 repos)\\n  depends_on:\\n  - D017\\n- id: D019\\n  date: 2026-05-13 18:08 UTC\\n  summary: D018 补充：Full M2 go/no-go 量化阈值 + 统计检验方案\\n  rationale: 'Reviewer 指出 D018 缺量化阈值，go/no-go 判据需在结果出来前明确，避免事后 rationalization。\\n\\n\\n    **统计方法**：每个 encoder 3 seeds 的 R@1 (best-by-val-loss checkpoint) 做 paired difference，bootstrap\\n    95% CI + paired t-test (p<0.05)。同时报告 best-by-R@1 checkpoint 结果作为透明度补充。\\n\\n\\n    **Go/No-Go 阈值**：\\n\\n    (A) Go — 原 framing 可用：dataflow > random 的 95% CI 在两个 encoder 上均 > 0\\n\\n    (B) Conditional Go — 修正 framing：dataflow > random 在至少一个 encoder 上 CI > 0，另一个 CI\\n    含 0（差异不显著）\\n\\n    (C) No-Go for Claim 1：dataflow ≤ random 在两个 encoder 上 CI 均含 0 或为负 → Claim 1 失效，pivot\\n    到 \\\"mining strategy × architecture\\\" 分析论文\\n\\n\\n    **Claim 2 判据**：若 full M2 显示 embedding > random 且 CI > 0 → 原 Claim 2 (\\\"embedding\\n    harms\\\") 被否定。新 Claim 2 候选：\\\"true embedding mining helps, but BM25 proxy harms\\\" 或\\n    \\\"hard negative mining method matters more than hard negative source\\\"\\n\\n\\n    **跨 encoder 一致性规则**：\\n\\n    - 同方向同显著 → 强泛化 claim\\n\\n    - 同方向不同显著 → 条件 claim + architecture discussion\\n\\n    - 反方向 → Claim 1 原形式被拒，需 conditional reframe\\n\\n\\n    阈值在 full M2 结果出来前锁定，不允许事后修改。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING - random_s42 in progress\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING - data build phase\\n  depends_on:\\n  - D018\\n- id: D020\\n  date: 2026-05-13 18:10 UTC\\n  summary: D019 补充：Claim 2 完整判定矩阵 + n=3 功效限制声明\\n  rationale: 'Reviewer 指出 D019 的 Claim 2 阈值不完整 + n=3 统计功效天然受限。补充如下：\\n\\n\\n    **Claim 2 完整判定矩阵**（3 seeds, paired bootstrap 95% CI）：\\n\\n    (i) random > embedding CI>0 → Claim 2 confirmed（embedding harms，与 MVP 一致）\\n\\n    (ii) embedding > random CI>0 → Claim 2 falsified（true embedding mining helps，需\\n    reframe）\\n\\n    (iii) CI 含 0 → inconclusive（效应存在但检测不到或确实无差异，论文报告为 \\\"no significant difference\\\"\\n    + 报告 effect size）\\n\\n\\n    **n=3 功效限制**（显式承认，不修改阈值）：\\n\\n    - df=2 时 t 临界值 4.303，pilot 级别差异（<2pp）极难达到 p<0.05\\n\\n    - Bootstrap n=3 仅 27 种重采样，CI 估计粗糙\\n\\n    - 阈值框架偏向 No-Go（Type II error 高）\\n\\n    - 若结果落入 (C) No-Go，论文 Discussion 必须讨论功效限制，不能简单声明 \\\"dataflow 无效\\\"\\n\\n    - 这是算力约束下的合理选择，不改阈值，但明确风险\\n\\n\\n    **plan_014 排期**：Full M2 完成后优先启动 plan_014（temperature ablation, ~10h）——无论 Claim\\n    2 reframe 成哪个方向，temperature regime-specificity 都需要回答。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: primary\\n    result: RUNNING\\n  - exp_id: m2_full_starcoder\\n    role: primary\\n    result: RUNNING\\n  depends_on:\\n  - D019\\n- id: D021\\n  date: 2026-05-13 19:10 UTC\\n  summary: Negative difficulty 分析揭示 encoder capacity 差异是 dataflow 效果不一致的根因\\n  rationale: '预训练模型 cosine similarity 分析显示：Qwen pretrained embeddings 分辨力弱（random\\n    cosine sim 0.899），StarCoder 分辨力强（random cosine sim 0.553）。Dataflow negatives 在两个模型上都比\\n    random 更难（higher sim），说明方法设计正确。但 StarCoder 已经\\\"懂\\\"结构差异（所有策略 sim 都低），额外训练信号边际收益小。这解释了\\n    pilot 中 StarCoder dataflow < random 的现象：不是方法问题，是 encoder 已有足够 capacity。\\n\\n\\n    论文价值：(1) 从 negative result 中提取 mechanistic explanation；(2) 定义 method applicability\\n    condition：\\\"structure-grounded negatives benefit most when pretrained encoder has\\n    limited structural separability\\\"；(3) 产出论文级图表（Figure: Negative Difficulty Distributions）；(4)\\n    无论 full M2 落入 A/B/C，这个分析都增加论文深度。不修改 go/no-go 阈值，但丰富解读框架。'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: context\\n    result: 'Qwen: dataflow > random (+0.8~2.3pp)'\\n  - exp_id: plan_013_starcoder\\n    role: context\\n    result: 'StarCoder: dataflow < random (-0.5pp), explained by high pretrained separability'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D022\\n  date: 2026-05-13 19:25 UTC\\n  summary: M1 28K instances 可恢复（运行时故障非数据问题）；当前 M2 继续，并行后台重跑 M1 提取\\n  rationale: 'Fuzzy match 抽查 10/10 发现 buggy_file 全部存在——28,276 个 \\\"error\\\" 是 CodeQL 并行提取时的运行时故障（磁盘/存储瞬态），不是\\n    SWE-smith 数据质量问题。训练数据潜在从 15,897 → ~44,173（2.8x）。\\n\\n\\n    决策：不中断当前 M2 训练 + 并行后台重跑 M1 提取。理由：\\n\\n    (1) 当前 M2 已在双卡运行，中断重来延期 3-7 天超出 DDL\\n\\n    (2) M1 重提取是 CPU 工作，可在 bjb1-42106 后台运行不影响 GPU 训练\\n\\n    (3) 如果当前 M2 结果落入 (C) No-Go 或 effect size 太小，扩展数据集是 natural next step\\n\\n    (4) 2.8x 数据量可能显著缓解 dataflow 过拟合问题（D021 中的核心风险）\\n\\n\\n    Claim 3 叙事需修正：\\\"64% failure 是上游数据问题\\\" → \\\"64% 是运行时提取故障，CodeQL 本身在有效输入上 100% 成功，可通过重跑恢复\\\"。这是\\n    engineering limitation with clear fix，不是方法局限。'\\n  related_experiments:\\n  - exp_id: m1_extraction\\n    role: primary\\n    result: 28,276 instances recoverable - runtime failure, not data quality\\n  - exp_id: plan_006_scalability\\n    role: affected\\n    result: 'error classification needs correction: buggy_file_not_found was misattributed'\\n  depends_on:\\n  - D018\\n  - D019\\n- id: D023\\n  date: 2026-05-13 19:43 UTC\\n  summary: Kill M1 重提取：bjb1 CodeQL 查询 100% 失败，D022 前提不成立需诊断后重新评估\\n  rationale: Reviewer CRITICAL 发现 bjb1-42106 上 CodeQL call_graph.ql 查询全部 exit status\\n    2，317/325 行失败，零有效结构数据产出。原 M1 在 cqa1-21977 成功，迁移后 CodeQL 版本/QL pack 可能不兼容。立即 kill\\n    进程释放 CPU/RAM，诊断 CodeQL 配置后决定修复或换服务器。\\n  related_experiments:\\n  - exp_id: m1_reextract\\n    role: subject\\n    result: killed - CodeQL incompatible on bjb1\\n  depends_on:\\n  - D022\\n- id: D024\\n  date: 2026-05-14 00:49 UTC\\n  summary: 'Major paper framing rewrite: drop falsified \\\"embedding harms\\\" claim, pivot\\n    to \\\"systematic analysis + mechanistic insight\\\" narrative'\\n  rationale: 'Reviewer deep assessment confirmed Claim 2 (\\\"embedding actively harms\\\",\\n    -27pp) was built on BM25-proxy mislabeled as embedding-distance in MVP. D017 proved\\n    true embedding mining helps (+1.6-2.0pp). New framing: (1) embedding universally\\n    helps (corrects misconception), (2) dataflow conditionally helps (mediated by\\n    representation saturation), (3) CodeQL scalable. This is a stronger, more honest\\n    paper type for EMNLP — empirical analysis with mechanistic depth rather than false\\n    \\\"our method beats all\\\" claim.'\\n  related_experiments:\\n  - exp_id: m2_embed_verify\\n    role: evidence\\n    result: embedding > random confirmed for both encoders\\n  - exp_id: plan_013_starcoder\\n    role: evidence\\n    result: dataflow helps Qwen only, not StarCoder — conditional benefit\\n  - exp_id: neg_difficulty_analysis\\n    role: evidence\\n    result: pos_sim saturation explains strategy-encoder interaction\\n  depends_on: []\\n- id: D025\\n  date: 2026-05-14 01:01 UTC\\n  summary: Plan_014 temperature ablation 缩减为 2 strategies × 3τ × 2 epochs = 6 runs\\n    (~70h)，deadline 可达\\n  rationale: 原方案 9 runs × 3 epochs = 157h GPU，超出 May 25 ARR 截稿。缩减理由：(1) 回答 Dream reviewer\\n    的 regime-specificity concern 只需证明 embedding vs random 的相对优势跨 τ 一致，不需要 3 策略全跑；(2)\\n    M2 和 pilot 均显示 epoch 3 过拟合无收益，2 epochs 足够；(3) τ=0.07 已由 M2 覆盖，只需 {0.05, 0.1, 0.2}。6\\n    runs × ~11.7h = ~70h → 双卡并行 35h wall time，M2 完成后 ~1.5 天可跑完。Dataflow strategy 的\\n    τ ablation 降为 P2，时间充裕再补。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: step 1000 best, epoch 3 overfitting → 2 epochs sufficient\\n  - exp_id: plan_014\\n    role: target\\n    result: budget revised from 10h to 70h, scope from 9 to 6 runs\\n  depends_on:\\n  - D024\\n- id: D026\\n  date: 2026-05-14 02:56 UTC\\n  summary: Qwen eval@2000 确认过拟合，后续 M2 runs 从 3 epochs 减至 2 epochs\\n  rationale: 'eval@2000: val_loss=0.5162, R@1=0.5228（与 @1500 持平，未恢复）。Best 锁定 step\\n    1000 (epoch 1 中段)。train_loss=0.04 vs val_loss=0.52，gap 持续扩大。模式与 pilot 一致（best\\n    at ~25% training）。当前 s42 保留 3 epochs 完整跑完（提供 full overfitting curve 数据），后续 8 runs/encoder\\n    设 max_epochs=2。节省 ~48h/GPU，M2 完成时间从 ~May 20-21 提前到 ~May 18-19。'\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: evidence\\n    result: eval@2000 R@1=0.5228 flat, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: pending\\n    result: eval@1000 still improving, apply 2-epoch precaution for subsequent seeds\\n  depends_on:\\n  - D025\\n- id: D027\\n  date: 2026-05-14 08:13 UTC\\n  summary: M2 剩余 runs 加 early stopping (patience=2 evals)，加速关键路径\\n  rationale: Reviewer 计算 M2 全 18 runs 需 ~5.5 天（StarCoder 瓶颈 ~133h）。两个编码器 best checkpoint\\n    均在 step 1000，之后 val_loss 持续上升。加 early stopping（patience=2，即连续 2 次 eval@500 无改善即停）预计在\\n    step 2000 左右停止（vs 2828 full 2-epoch），节省 ~30% 时间（~1.5 天），M2 从 May 19.5 提前到 ~May\\n    18。关键路径 May 25 ARR 余量从 5 天增至 7 天。风险低：仅影响未启动的 runs，不改已跑数据。\\n  related_experiments:\\n  - exp_id: m2_full_qwen\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  - exp_id: m2_full_starcoder\\n    role: target\\n    result: running, best@1000, overfitting confirmed\\n  depends_on:\\n  - D026\\n\", \"total_chars\": 20054, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27752135-924d-4f85-aeac-367221d32b92",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "bce09f5c-ff39-4b49-b7d4-17a661bbe572",
  "sourceToolAssistantUUID": "27752135-924d-4f85-aeac-367221d32b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T08:31:55.674Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UVSEGT8MvuxA43gG13GVfm`</summary>

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
  "parentUuid": "bce09f5c-ff39-4b49-b7d4-17a661bbe572",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29fqqbznoEHh3mtamWL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0810e408-f998-4414-b965-5426dbf9ff10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DYvCVH9BsXtQLKMKnLojCp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12448,
      "cache_read_input_tokens": 25421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12448,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 20 · 2026-05-14T08:31:55.686Z_

<details><summary>↩ Tool result · `toolu_01UVSEGT8MvuxA43gG13GVfm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'structfuse-context'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0810e408-f998-4414-b965-5426dbf9ff10",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "e466420f-4975-4fd5-9042-c6672c60d06e",
  "sourceToolAssistantUUID": "0810e408-f998-4414-b965-5426dbf9ff10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T08:31:56.210Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MbFktcLdH1jEqDuawFPUig`</summary>

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
  "parentUuid": "e466420f-4975-4fd5-9042-c6672c60d06e",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29fqqbznoEHh3mtamWL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f97669bc-d6a9-4ac1-a8e6-a464eee04505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DYvCVH9BsXtQLKMKnLojCp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12448,
      "cache_read_input_tokens": 25421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12448,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 22 · 2026-05-14T08:31:56.245Z_

<details><summary>↩ Tool result · `toolu_01MbFktcLdH1jEqDuawFPUig`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); heavy inference cost |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo-wide navigation; no semantic analysis |\\n| **GraphCoder** | Enhancing Repo-Level Code Completion via Code Context Graph | ASE 2024 (arXiv:2406.07003) | Code Context Graph (CFG + CDG + DDG) | Inference-time | Partial. Data dependence graph but **intra-procedural** only | Code completion | Repository-level benchmarks | Coarse-to-fine retrieval with CCG; closest to StructFuse in using data/control flow, but intra-proc and at inference-time |\\n| **CodeRAG** | Supportive Code Retrieval on Bigraph for Real-World Code Generation | arXiv:2504.10046 (Apr 2025) | Bigraph (requirement graph + DS-code graph) | Inference-time | No. Dependency + semantic edges | Repo-level code generation | DevEval (+40.90 Pass@1 w/ GPT-4o) | Dual-graph (requirements + code); agentic reasoning; high inference overhead |\\n| **ARISE** | Repository-level Graph for Agentic Fault Localization and Program Repair | arXiv:2605.03117 (May 2025) | Multi-granularity program graph (statement nodes + def-use edges) | Inference-time | Partial. **Intra-procedural** def-use edges + data-flow slicing tool | Fault localization + repair | SWE-bench Lite (300 issues); +17.0 Function Recall@1 | Closest to StructFuse in data-flow usage; but intra-proc only, agent queries at inference |\\n| **CodeGRAG** | Bridging NL and PL via Graphical RAG | arXiv:2405.02355 (2024) | Composed syntax graph (AST + DFG + CFG) | Both (GNN training + graph prompt at inference) | Partial. DFG extraction but function-level | Code generation (cross-lingual) | Multiple PLs | Only method with training-time component (GNN soft prompts); but graph also used at inference |\\n| **StructFuse** (Ours) | Structure-Grounded Hard Negatives via CodeQL Data-Flow | — | Inter-procedural data-flow graph (CodeQL taint tracking) | **Training-time only** | **Yes. Full inter-procedural** (source→sink across call boundaries) | Code retrieval (contrastive training) | Large-scale repos with CodeQL | Zero inference overhead; graph used offline for negative mining; inter-proc data-flow |\\n\\n## Discussion 要点\\n\\n### StructFuse vs Inference-Time Graph Methods: 互补性与差异性\\n\\n1. **Cost-accuracy tradeoff**: Inference-time methods (CodexGraph, RANGER, RepoGraph) achieve high precision by constructing and querying graphs per request, but incur significant latency (graph construction + traversal + LLM calls). StructFuse amortizes all graph computation to training time—once the encoder is trained with structure-grounded negatives, inference is a single embedding lookup with zero graph overhead. This makes StructFuse suitable for latency-sensitive production retrieval where inference-time graph methods are impractical.\\n\\n2. **Data-flow depth**: Most inference-time methods use structural graphs (call graphs, class hierarchies, file dependencies). Only GraphCoder and ARISE incorporate data/control flow, but limited to **intra-procedural** scope. StructFuse uniquely leverages **inter-procedural** data-flow via CodeQL's taint tracking, capturing cross-function semantic relationships (e.g., a sanitizer function that transforms data between source and sink across call boundaries). This deeper semantic signal generates harder, more informative negatives.\\n\\n3. **Complementarity**: StructFuse and inference-time methods are orthogonal and composable. A StructFuse-trained encoder can serve as the embedding backbone for systems like RANGER or CodexGraph, providing better initial retrieval that reduces the graph agent's search space. Conversely, inference-time graph methods can provide reranking on top of StructFuse retrieval for tasks requiring maximum precision.\\n\\n4. **Scalability model**: Inference-time methods scale linearly with query volume (each query triggers graph operations). StructFuse's cost is front-loaded: CodeQL analysis runs once per repository update, and the resulting negatives improve the encoder permanently. For high-QPS code search services, this one-time investment yields compounding returns.\\n\\n5. **Task generality vs specialization**: Inference-time graph agents (CodexGraph, RepoGraph) are task-agnostic but require powerful LLMs as backends. StructFuse produces a specialized retrieval encoder that excels at the code search task without LLM inference, making it deployable as a lightweight, efficient first-stage retriever in multi-stage pipelines.\\n\\n## Related Work 段落草稿 (~200 words)\\n\\n**Graph-Based Methods for Code Understanding.**\\nRecent work has explored leveraging code graphs to enhance LLM-based software engineering. Inference-time approaches construct and query graphs during each interaction: CodexGraph (Liu et al., NAACL 2025) builds a code graph database that LLM agents query via structured interfaces; RepoGraph (Ouyang et al., ICLR 2025) provides repository-level navigation as a plug-in module for SE agents; LocAgent (ACL 2025) and RANGER (2025) employ graph-guided multi-hop reasoning and MCTS-based traversal for code localization and retrieval, respectively. GraphCoder (ASE 2024) incorporates intra-procedural control-flow and data-dependence graphs for code completion retrieval, while ARISE (2025) extends this with statement-level def-use edges for fault localization. CodeGRAG (2024) bridges training and inference by using GNN-encoded graph prompts.\\n\\nThese methods achieve strong results but impose substantial inference-time costs—graph construction, traversal, and often multiple LLM calls per query. Moreover, their data-flow analysis remains intra-procedural. StructFuse takes a fundamentally different approach: we leverage CodeQL's inter-procedural taint tracking to generate structure-grounded hard negatives at **training time**, producing an encoder that captures cross-function data-flow semantics without any graph overhead at inference. This positions StructFuse as complementary to inference-time graph methods—it can serve as an efficient first-stage retriever whose embeddings already encode deep structural relationships that other methods must compute on-the-fly.\\n\\n---\\n\\n## 参考文献\\n\\n- CodexGraph: arXiv:2408.03910, NAACL 2025\\n- LocAgent: arXiv:2503.09089, ACL 2025\\n- RANGER: arXiv:2509.25257, 2025\\n- RepoGraph: arXiv:2410.14684, ICLR 2025\\n- GraphCoder: arXiv:2406.07003, ASE 2024\\n- CodeRAG: arXiv:2504.10046, 2025\\n- ARISE: arXiv:2605.03117, 2025\\n- CodeGRAG: arXiv:2405.02355, 2024\\n\", \"total_chars\": 8062, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f97669bc-d6a9-4ac1-a8e6-a464eee04505",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "ea41a612-3f04-4baf-baab-bc23aad2ca20",
  "sourceToolAssistantUUID": "f97669bc-d6a9-4ac1-a8e6-a464eee04505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T08:32:00.339Z_

Now let me look at the actual paper PDF or LaTeX source, and the experiment results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea41a612-3f04-4baf-baab-bc23aad2ca20",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29gAiuQ7Y9tDY22Lm9X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7017b84-ab5e-4748-b979-f1a94f1e1cd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRcDHngDnUieCCdZyv2Qzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2815,
      "cache_read_input_tokens": 37869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2815,
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

_source line 24 · 2026-05-14T08:32:01.309Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VXvjAF3WUaE9unVTU32txm`</summary>

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
  "parentUuid": "d7017b84-ab5e-4748-b979-f1a94f1e1cd6",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29gAiuQ7Y9tDY22Lm9X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a1e28c2-bb01-4652-9123-3851cc152438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRcDHngDnUieCCdZyv2Qzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2815,
      "cache_read_input_tokens": 37869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2815,
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

_source line 25 · 2026-05-14T08:32:01.331Z_

<details><summary>↩ Tool result · `toolu_01VXvjAF3WUaE9unVTU32txm`</summary>

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
  "parentUuid": "1a1e28c2-bb01-4652-9123-3851cc152438",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "78551c6c-9b26-41de-8fbe-c89914148eee",
  "sourceToolAssistantUUID": "1a1e28c2-bb01-4652-9123-3851cc152438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T08:32:01.454Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BXNuodWgn8ZA79Ltu9SaHT`</summary>

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
  "parentUuid": "78551c6c-9b26-41de-8fbe-c89914148eee",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29gAiuQ7Y9tDY22Lm9X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d6556e2-b3df-427d-8c0d-b17525a880c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRcDHngDnUieCCdZyv2Qzj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2815,
      "cache_read_input_tokens": 37869,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2815
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 37869,
          "cache_creation_input_tokens": 2815,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2815,
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

_source line 27 · 2026-05-14T08:32:01.469Z_

<details><summary>↩ Tool result · `toolu_01BXNuodWgn8ZA79Ltu9SaHT`</summary>

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
  "parentUuid": "7d6556e2-b3df-427d-8c0d-b17525a880c4",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "af5a5560-eb4c-4504-937c-b4ca26c4164d",
  "sourceToolAssistantUUID": "7d6556e2-b3df-427d-8c0d-b17525a880c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-14T08:32:03.975Z_

Let me read the latest dream review reports and the paper tex files to understand the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af5a5560-eb4c-4504-937c-b4ca26c4164d",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29gYw8sRKUUdjdy2SYP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bba77e23-22a5-49cf-b4b4-37ccd640c2c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TauKtm3eXF3dkAVayCSFse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 508,
      "cache_read_input_tokens": 40684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 508,
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

_source line 29 · 2026-05-14T08:32:04.676Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BNcqGPRSrKByvk4pTNgnon`</summary>

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
  "parentUuid": "bba77e23-22a5-49cf-b4b4-37ccd640c2c3",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29gYw8sRKUUdjdy2SYP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5336d761-01c9-4d0e-bd44-eb0f2d8d818c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TauKtm3eXF3dkAVayCSFse",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 508,
      "cache_read_input_tokens": 40684,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 508
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 40684,
          "cache_creation_input_tokens": 508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 508,
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

_source line 30 · 2026-05-14T08:32:04.682Z_

<details><summary>↩ Tool result · `toolu_01BNcqGPRSrKByvk4pTNgnon`</summary>

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
  "parentUuid": "5336d761-01c9-4d0e-bd44-eb0f2d8d818c",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "ec1a9294-0675-4423-a3b2-e0a79f7e9eb2",
  "sourceToolAssistantUUID": "5336d761-01c9-4d0e-bd44-eb0f2d8d818c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T08:32:08.252Z_

Now let me read the dream review reports to see what previous reviewers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec1a9294-0675-4423-a3b2-e0a79f7e9eb2",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29goB97SRti6PzyKmRB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef5dfff3-1d58-449f-9c74-437bc2e28959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEsRxVfDSxp61a95cbVU3G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9047,
      "cache_read_input_tokens": 41192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9047,
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

_source line 32 · 2026-05-14T08:32:10.659Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013taXektyfFas4wmgQQXyK1`</summary>

```json
{
  "pattern": "**/dream_20260514T075732/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef5dfff3-1d58-449f-9c74-437bc2e28959",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29goB97SRti6PzyKmRB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88a198be-9259-4ec8-ae49-cfcf6a072946",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEsRxVfDSxp61a95cbVU3G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9047,
      "cache_read_input_tokens": 41192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9047,
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

_source line 33 · 2026-05-14T08:32:10.691Z_

<details><summary>↩ Tool result · `toolu_013taXektyfFas4wmgQQXyK1`</summary>

```text
artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/median/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T075732/best/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88a198be-9259-4ec8-ae49-cfcf6a072946",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "c02225ef-90c3-4a9f-b2d4-f447fee78072",
  "sourceToolAssistantUUID": "88a198be-9259-4ec8-ae49-cfcf6a072946",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T08:32:11.490Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VKwZa9mBPBxuNxLgfK3GUr`</summary>

```json
{
  "pattern": "**/dream_20260514T075732/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c02225ef-90c3-4a9f-b2d4-f447fee78072",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29goB97SRti6PzyKmRB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dbf93dd-2526-4164-8ada-e332db6e02ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEsRxVfDSxp61a95cbVU3G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9047,
      "cache_read_input_tokens": 41192,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9047
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 41192,
          "cache_creation_input_tokens": 9047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9047,
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

_source line 35 · 2026-05-14T08:32:11.511Z_

<details><summary>↩ Tool result · `toolu_01VKwZa9mBPBxuNxLgfK3GUr`</summary>

```text
artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/best/review_context.yaml
artifacts/dream_reports/dream_20260514T075732/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dbf93dd-2526-4164-8ada-e332db6e02ad",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "f76904d0-cd9e-410c-8dee-80845d7617e3",
  "sourceToolAssistantUUID": "9dbf93dd-2526-4164-8ada-e332db6e02ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T08:32:14.767Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RinpqAiMBQbS2d4K7r8mf6`</summary>

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
  "parentUuid": "f76904d0-cd9e-410c-8dee-80845d7617e3",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29hJn7pfsn7Wr5KKwXs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85fc2d50-161a-40b6-8655-0a180bb8159c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnV3Ri9Z1Xr3rto9k8Nb4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 486,
      "cache_read_input_tokens": 50239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 486,
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

_source line 37 · 2026-05-14T08:32:14.782Z_

<details><summary>↩ Tool result · `toolu_01RinpqAiMBQbS2d4K7r8mf6`</summary>

```text
1	---
2	dream_id: dream_20260514T075732
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-14T08:30:00.761428+00:00
6	---
7	
8	# Dream Review Report: StructFuse — Hard Negatives for Code Retrieval
9	
10	**Paper**: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
11	**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)
12	**Target Venue Standard**: Top ML venue (EMNLP-level), ~25% acceptance rate, 6-point scale
13	
14	---
15	
16	## Roundtable Summary
17	
18	| | R1 (Methods+Experiments) | R2 (Novelty+Related Work) | Consensus |
19	|---|---|---|---|
20	| Score | 4 (Weak Accept) | 4 (Weak Accept) | **4 (Weak Accept)** |
21	| Confidence | 4/5 (High) | 4/5 (High) | 4/5 |
22	
23	Both reviewers independently converged on the same score and identified overlapping core concerns. No significant disagreements arose during cross-sharing.
24	
25	---
26	
27	## Step 1–2: Independent Reviews + Cross-Sharing
28	
29	### Reviewer 1 (R1): Methods and Experiments
30	
31	**Strengths:**
32	- 54 training runs (2 encoders × 3 strategies × 9 seeds) with paired bootstrap CIs is exemplary experimental rigor, well above the typical ML paper standard.
33	- Extensive ablation suite: temperature (Table 7), hop distance (Table 8), data scaling (Table 9), fusion head (Table 10), static vs. dynamic mining (Table 11), binary vs. weighted dataflow (Table 12), failure analysis (Table 13), stratified analysis (Table 6). This breadth is commendable.
34	- The representation saturation mechanistic explanation (pos_sim 0.986 vs 0.799 → different strategy effectiveness) is the paper's most insightful contribution.
35	- Dynamic mining baseline (Table 11) cleanly rules out curriculum effects.
36	- Fusion head ablation (Table 10) sharply separates training-time mining value from inference-time feature injection.
37	
38	**Major Weaknesses:**
39	
40	1. **Z% inconsistency (78% vs 41%).** Section 3.3 reports Z%=78% at 2-hop; Section 4.11 and Table 8 report Z%=41%. These likely refer to different denominators (conditional on structural data availability vs. unconditional), but the paper uses identical notation without disambiguation. This internal contradiction undermines trust in reported statistics. Must clarify and report both conditional/unconditional rates.
41	
42	2. **Missing BM25 negative baseline.** The paper's headline narrative is correcting CoCoHaNeRe's misconception that embedding negatives harm code search — attributed to BM25 proxy negatives mislabeled as embedding-distance. Yet the paper never runs actual BM25 negatives to demonstrate the claimed −27pp harm is BM25-specific. This is the single most important missing experiment given the paper's framing.
43	
44	3. **Low structural coverage (34.3%) is underreported.** Only ~1/3 of training instances receive dataflow-mined negatives; the rest fall back to embedding/random. The measured +1.5pp dataflow improvement on Qwen (Table 1) averages over all instances. Stratified results (structural-available vs. fallback) are absent — readers cannot assess the true per-instance magnitude of the structural contribution.
45	
46	4. **Dataflow vs. embedding is not significant (p=0.134, Table 4).** The practical case for dataflow over the simpler embedding strategy is weak. +1.0pp CI [−0.8, 2.8] on SWE-bench, requiring a complex CodeQL pipeline, is hard to justify. The paper acknowledges this but Claim 2 ("conditional additional benefit") still rests on dataflow-vs-random significance, sidestepping the more relevant comparison.
47	
48	5. **Small effect sizes.** +2.3pp R@1 (embedding) and +1.5pp (dataflow) are statistically significant but practically modest. On SWE-bench, +2.3pp = ~7 additional resolved instances out of 300, with wide CIs. The cost-benefit of the CodeQL extraction pipeline relative to these gains is not discussed.
49	
50	6. **StarCoder2-3B architectural mischaracterization.** The paper describes StarCoder2-3B as "encoder-decoder" but it is decoder-only (GPT-style autoregressive). The claimed "architecturally distinct" cross-encoder comparison is actually a difference in pretraining data/procedure, not architecture class. This weakens the cross-architecture generalization narrative.
51	
52	**Minor Weaknesses:**
53	- CoCoHaNeRe critique lacks specific textual evidence from the original paper.
54	- RepoBench-R (Table 5) has no statistical significance testing (single checkpoint, no seeds/CIs).
55	- SWE-bench evaluation uses only Qwen checkpoints, not StarCoder.
56	- Overfitting patterns across strategies not reported (project history shows severe overfitting, best checkpoint at step 1000/4242).
57	- Number of negatives per query (k) not stated in paper.
58	- Checkpoint selection criterion not specified; project history suggests strategy rankings change depending on criterion.
59	
60	**Key Questions:**
61	- Q1: Clarify Z% (78% vs 41%) with explicit denominators.
62	- Q2: Report R@1 stratified by structural data availability.
63	- Q3: Provide specific textual evidence for the CoCoHaNeRe BM25-proxy claim.
64	- Q4: Why is the BM25 negative baseline absent?
65	- Q5: Correct the StarCoder2 architectural description.
66	- Q6: Was SWE-bench evaluation single-run or multi-seed per strategy?
67	- Q7: Sensitivity to top-K cutoff in the dataflow miner (currently K=50)?
68	- Q8: Per-strategy overfitting curves to confirm comparison validity.
69	
70	---
71	
72	### Reviewer 2 (R2): Novelty and Related Work
73	
74	**Strengths:**
75	- CoCoHaNeRe correction has genuine community value — clearing a misconception that discourages a useful technique.
76	- The pos_sim diagnostic as a pre-training decision tool is actionable and novel as a practical recommendation.
77	- Honest reporting of conditional and null results (StarCoder dataflow p=0.62) is laudable; many papers would omit this.
78	- The framing as "systematic study" with the breadth of ablations partially compensates for limited single-technique novelty.
79	
80	**Major Weaknesses:**
81	
82	1. **Thin novelty concentrated in a conditional finding.** Embedding-distance mining is a standard technique (low novelty); dataflow-aware mining via CodeQL is moderately novel but conceptually straightforward (filter by graph connectivity). The most novel claim — representation saturation mediates structural negative effectiveness — rests on only n=2 encoders, making it an observation rather than a validated theory.
83	
84	2. **Missing theoretical contextualization.** The difficulty–capacity interaction underlying the saturation finding is known in contrastive learning theory (Robinson et al. 2021 "Contrastive Learning with Hard Negative Samples"; Kalantidis et al. 2020 "Hard Negative Mixing for Contrastive Learning"). The paper presents its finding as if novel, but it is a domain-specific instantiation of established theory. Citing and positioning against this literature would strengthen the contribution.
85	
86	3. **Significant related work gaps.** For an empirical analysis paper, the related work section is thin. Missing references include:
87	   - Foundational contrastive/retrieval: DPR (Karpukhin et al.), SimCLR, MoCo
88	   - Code representation: CodeBERT, UniXcoder, CodeT5+
89	   - Hard negative theory: Robinson et al. 2021, Kalantidis et al. 2020
90	   - Structural code methods: CodeGRAG, GraphCoder, RepoGraph
91	   
92	   An empirical survey-type paper must comprehensively cover the landscape it claims to systematize.
93	
94	4. **No empirical comparison with inference-time structural methods.** Table 14 provides a conceptual taxonomy but no experimental data. Claiming complementarity without evidence is unsatisfying. Even a small-scale comparison (e.g., STRUCTFUSE retriever + LocAgent reranking vs. either alone) would substantially strengthen the positioning.
95	
96	5. **CodeQL scalability framed as contribution but is engineering validation.** "0% timeout at 123-repo scale" is a pipeline reliability metric, not a research contribution. The 34% instance-level coverage is the more relevant number, and it is a significant limitation.
97	
98	**Minor Weaknesses:**
99	- The paper pivots between "systematic study" and "STRUCTFUSE as a system" without clearly choosing an identity. The name STRUCTFUSE implies a system contribution, but the substance is an empirical analysis.
100	- Claims are sometimes overcalibrated: "consistently improves" and "correcting the prior misconception" are strong language for +2.3pp gains and an unverified critique of prior work.
101	- The paper lacks error analysis of *when* embedding mining fails (only analyzes when dataflow helps in Table 13).
102	
103	**Key Questions:**
104	- Q1: How does the pos_sim diagnostic generalize beyond Qwen/StarCoder? Have you measured pos_sim for other encoders (e.g., CodeBERT, UniXcoder)?
105	- Q2: Can you position the saturation finding against Robinson et al. 2021's theoretical framework for optimal negative difficulty?
106	- Q3: Why not include even a small-scale empirical comparison with an inference-time method?
107	- Q4: The paper name "STRUCTFUSE" implies a system — is the contribution a system or a study?
108	
109	---
110	
111	## Step 3: Convergence — Points of Agreement and Divergence
112	
113	### Full Agreement (both reviewers):
114	1. **Score: 4 (Weak Accept)** — the paper has genuine merit but execution gaps prevent a confident accept.
115	2. **The representation saturation insight is the paper's strongest and most novel contribution**, but is underpowered with only 2 encoders.
116	3. **Effect sizes are small** (+1.5–2.3pp R@1) and the practical case for dataflow over embedding is weak (p=0.134 for the comparison that matters).
117	4. **34% CodeQL coverage is a real limitation** that dilutes the measured dataflow effect and is underreported.
118	5. **Experimental rigor is above average** — 9 seeds, bootstrap CIs, extensive ablations.
119	6. **The CoCoHaNeRe correction is valuable** but the narrative is not fully substantiated.
120	
121	### R1 emphasis (methods-side):
122	- Z% internal inconsistency (78% vs 41%) as a credibility issue
123	- Missing BM25 baseline as the most critical gap
124	- StarCoder2 architectural mischaracterization
125	- Confound between embedding similarity and dataflow disconnection
126	
127	### R2 emphasis (novelty-side):
128	- Thin novelty — mostly standard techniques applied to code
129	- Missing theoretical contextualization (Robinson et al., Kalantidis et al.)
130	- Significant related work gaps (10+ missing references)
131	- No empirical comparison with inference-time methods
132	
133	### No genuine disagreements between reviewers.
134	
135	---
136	
137	## Step 4: Consolidated Assessment
138	
139	### Overall Score: **4 / 6 (Weak Accept)**
140	
141	### Headline
142	A well-executed empirical study of hard negative mining for code retrieval with above-average experimental rigor and a genuinely insightful representation saturation finding. The paper is held back by missing baselines (BM25), internal inconsistencies (Z%), thin novelty, and small effect sizes that make the practical value proposition of the dataflow component questionable.
143	
144	### Detailed Assessment
145	
146	**What the paper does well:**
147	- The 2×3×9 experimental matrix with bootstrap statistics sets a high bar for rigor in this subfield.
148	- The clean encoder–strategy interaction (embedding helps both; dataflow conditional on saturation) is the paper's strongest finding, providing a mechanistic explanation rather than just reporting numbers.
149	- The ablation suite is comprehensive: temperature, hop distance, data scaling, fusion head, static vs. dynamic mining, binary vs. weighted, failure analysis. Each ablation serves a clear analytical purpose.
150	- Honest reporting of null results (StarCoder dataflow p=0.62, dataflow-vs-embed p=0.134).
151	- The fusion head ablation (Table 10) yields a crisp insight: structural information's value lies in training-time mining, not inference-time features.
152	
153	**What needs improvement for acceptance:**
154	
155	1. **[Critical] Add BM25 negative baseline.** The paper's central narrative — that CoCoHaNeRe's finding of embedding-negative harm is a BM25-proxy artifact — demands running BM25 negatives to close the argument. Without this, the correction claim is speculative.
156	
157	2. **[Critical] Resolve Z% inconsistency.** Define Z% precisely with explicit denominators. Report both conditional (among instances with structural data) and unconditional (all instances) rates. Current state is an internal contradiction.
158	
159	3. **[Major] Stratify dataflow results by structural availability.** Report R@1 separately for instances where CodeQL produced structural data vs. those that fell back to non-dataflow negatives. This is essential for interpreting the +1.5pp average.
160	
161	4. **[Major] Expand related work.** Add DPR, SimCLR/MoCo (negative mining foundations), Robinson et al. 2021 / Kalantidis et al. 2020 (hard negative theory directly relevant to the saturation finding), and standard code encoders (CodeBERT, UniXcoder, CodeT5+).
162	
163	5. **[Major] Correct StarCoder2 architecture description.** StarCoder2-3B is decoder-only, not encoder-decoder. Reframe the cross-encoder comparison honestly (different pretraining, not different architecture).
164	
165	6. **[Minor] Add RepoBench-R significance testing.** Run multiple checkpoints or seeds to get CIs.
166	
167	7. **[Minor] Discuss cost-benefit.** The CodeQL pipeline requires compiling every repo into a database; is +1.5pp (not significant vs. embedding) worth this infrastructure?
168	
169	### Experiment Coverage Assessment
170	Comparing the paper against the full experiment design (review_context.yaml):
171	- All 14 imagined experiments appear in the paper (full coverage).
172	- Quality of reporting is generally good, with tables for all major results.
173	- The narrative guidance's three-claim structure (embedding universal, dataflow conditional, mechanism via saturation) is faithfully reflected.
174	
175	### Recommendation
176	The paper is a borderline contribution. The experimental execution and analytical depth are genuine strengths that distinguish it from typical "we tried X and it improved by Y" papers. The representation saturation finding, if validated on more encoders, could become an influential diagnostic tool. However, the missing BM25 baseline, Z% inconsistency, and thin novelty (per R2) place it below the acceptance threshold for a top venue in its current form. A revision addressing the critical items above would likely push it to a 5 (Accept).
177	
178	### Scores Summary
179	
180	| Criterion | Score | Notes |
181	|---|---|---|
182	| Soundness | 3.5/5 | Strong design, but Z% error and missing BM25 baseline |
183	| Novelty | 2.5/5 | Saturation insight is moderate; techniques are standard |
184	| Significance | 3/5 | Small effects, but actionable pos_sim diagnostic |
185	| Clarity | 3.5/5 | Well-organized, but Z% ambiguity and arch mischaracterization |
186	| Reproducibility | 3/5 | Main experiments ok; CodeQL pipeline details insufficient |
187	| **Overall** | **4/6** | **Weak Accept** |
188	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85fc2d50-161a-40b6-8655-0a180bb8159c",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "5b389cc2-8e17-4cd6-97c9-e47c54e7fa41",
  "sourceToolAssistantUUID": "85fc2d50-161a-40b6-8655-0a180bb8159c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T08:32:15.222Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nrk9SEbvsjoEuv6pmxU1Pf`</summary>

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
  "parentUuid": "5b389cc2-8e17-4cd6-97c9-e47c54e7fa41",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29hJn7pfsn7Wr5KKwXs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d398f30-77d8-4c43-a713-34b61fb1a132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnV3Ri9Z1Xr3rto9k8Nb4i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 486,
      "cache_read_input_tokens": 50239,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 486
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 50239,
          "cache_creation_input_tokens": 486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 486,
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

_source line 39 · 2026-05-14T08:32:15.535Z_

<details><summary>↩ Tool result · `toolu_01Nrk9SEbvsjoEuv6pmxU1Pf`</summary>

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
  "parentUuid": "9d398f30-77d8-4c43-a713-34b61fb1a132",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "5f1ee083-b502-47c6-8e7f-8034adcff80f",
  "sourceToolAssistantUUID": "9d398f30-77d8-4c43-a713-34b61fb1a132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-14T08:32:18.664Z_

Now let me also check the worst-case paper and the first dream review for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f1ee083-b502-47c6-8e7f-8034adcff80f",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29hb6PfCk7TofXGFHqf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4c9c761-6f1a-4ad1-9d42-7499e1f1b11a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GE7X1KCRFKrioDmwayDVWC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14321,
      "cache_read_input_tokens": 50725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14321,
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

_source line 41 · 2026-05-14T08:32:21.078Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MLHcQVzB3YQdpkZMJ1MGzA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4c9c761-6f1a-4ad1-9d42-7499e1f1b11a",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29hb6PfCk7TofXGFHqf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28adae77-82cf-4cb1-9e28-6b2b0d363dea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GE7X1KCRFKrioDmwayDVWC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14321,
      "cache_read_input_tokens": 50725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14321,
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

_source line 42 · 2026-05-14T08:32:21.084Z_

<details><summary>↩ Tool result · `toolu_01MLHcQVzB3YQdpkZMJ1MGzA`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28adae77-82cf-4cb1-9e28-6b2b0d363dea",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "42eedf77-1176-4a5c-8384-5a95de5c1f05",
  "sourceToolAssistantUUID": "28adae77-82cf-4cb1-9e28-6b2b0d363dea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T08:32:21.657Z_

<details open><summary>🔧 Tool call — Read · `toolu_018FCF65sfNYdDqvxpCCKgZo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42eedf77-1176-4a5c-8384-5a95de5c1f05",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29hb6PfCk7TofXGFHqf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf2f7eeb-54fe-430f-95e8-8c747f11e68e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GE7X1KCRFKrioDmwayDVWC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14321,
      "cache_read_input_tokens": 50725,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14321
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 50725,
          "cache_creation_input_tokens": 14321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14321,
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

_source line 44 · 2026-05-14T08:32:21.663Z_

<details><summary>↩ Tool result · `toolu_018FCF65sfNYdDqvxpCCKgZo`</summary>

```text
1	narrative_guidance: 'Claim 1 降级为 "directional evidence"——embedding mining 方向一致但 95%
2	  CI 宽，至少一个编码器包含零。 Claim 2 降为 "exploratory observation"——dataflow 在 Qwen 上方向正确但不显著，StarCoder
3	  上甚至略负。 论文重心转向方法论贡献（controlled comparison framework + representation geometry analysis），
4	  效果量作为 preliminary evidence 呈现。SWE-bench 未能提供有说服力的下游验证。 "tends to improve" 替代 "consistently
5	  improves"。仍投 EMNLP Main，定位 analysis paper。
6	
7	  '
8	imagined_experiments:
9	- name: SWE-bench Lite end-to-end evaluation
10	  plan_id: plan_003
11	  description: 3 strategies × best checkpoint, Qwen3.6-27B agent, 300 SWE-bench Lite
12	    instances
13	  expected_results:
14	    random_resolve_rate_pct: 18.3
15	    embedding_distance_resolve_rate_pct: 18.7
16	    dataflow_aware_resolve_rate_pct: 18.0
17	    embed_vs_random_delta_pp: 0.4
18	    dataflow_vs_random_delta_pp: -0.3
19	    retrieval_recall_at_5_random: 0.41
20	    retrieval_recall_at_5_embed: 0.43
21	    retrieval_recall_at_5_dataflow: 0.42
22	    instances_evaluated: 287
23	    instances_failed_agent_error: 13
24	  result_rationale: 'median 档下 SWE-bench Δ ≤ 1pp。原因：(1) 300 实例中仅 ~50% 的 bug 与 retrieval
25	    质量相关， 其余受 patch generation 瓶颈限制——retriever 的 +1pp R@1 优势在 end-to-end pipeline
26	    中被稀释； (2) SWE-bench 的 repo 分布与训练集 SWE-smith 有 domain shift， m2_full 训练中观测到的 step
27	    1000 后过拟合加剧了这种 gap； (3) agent 的 file selection 依赖多轮交互，单次 retrieval 改进的边际效用递减。
28	    embedding 略优于 random 但幅度 <1pp，dataflow 因在 unseen repos 上结构信号噪声更大反而微跌。 整体 resolve
29	    rate ~18% 处于 baseline agent 的正常水平，无法宣称下游收益。
30	
31	    '
32	  tables:
33	  - name: 'Table: SWE-bench Lite Resolve Rate by Strategy'
34	    columns:
35	    - Strategy
36	    - Resolve Rate (%)
37	    - Δ vs Random (pp)
38	    - Retrieval R@5
39	    rows:
40	    - - random
41	      - '18.3'
42	      - —
43	      - '0.41'
44	    - - embedding_distance
45	      - '18.7'
46	      - '+0.4'
47	      - '0.43'
48	    - - dataflow_aware
49	      - '18.0'
50	      - −0.3
51	      - '0.42'
52	  figures_description:
53	  - 'Bar chart: resolve rate ± 95% binomial CI per strategy, 三根 bar 的 CI 完全重叠'
54	  analysis: 'SWE-bench 无法区分三种策略。写入论文时定位为 "downstream evaluation shows no statistically
55	    distinguishable difference"，并 acknowledge retrieval gains 在 end-to-end pipeline
56	    中 被 generation bottleneck 稀释。这不否定 retrieval 改进，但不能用作 downstream evidence。
57	
58	    '
59	- name: RepoBench-R cross-file retrieval evaluation
60	  plan_id: plan_004
61	  description: retrieval-only evaluation on RepoBench-R, 3 strategies × best checkpoint,
62	    两个编码器
63	  expected_results:
64	    qwen_random_R1: 0.312
65	    qwen_embed_R1: 0.325
66	    qwen_dataflow_R1: 0.318
67	    starcoder_random_R1: 0.274
68	    starcoder_embed_R1: 0.279
69	    starcoder_dataflow_R1: 0.268
70	    qwen_embed_vs_random_delta_pp: 1.3
71	    starcoder_embed_vs_random_delta_pp: 0.5
72	    qwen_dataflow_vs_random_delta_pp: 0.6
73	    starcoder_dataflow_vs_random_delta_pp: -0.6
74	  result_rationale: 'RepoBench-R 的 cross-file retrieval 与 SWE-smith 训练分布差异显著——RepoBench
75	    侧重 next-line completion 的上下文文件，粒度更细且不直接对应 bug-fix file selection。 median 档下 embedding
76	    优势方向保持但缩水：Qwen ~+1.3pp（pilot 中 +2.0pp 缩水约 35%， 因 domain shift 和 evaluation granularity
77	    不同），StarCoder ~+0.5pp（CI 将包含零）。 Dataflow 在 Qwen 上仅 +0.6pp（RepoBench 的文件间 dataflow
78	    关系与训练时 CodeQL 提取的 分布不匹配），StarCoder 上略负。绝对 R@1 水平较低（0.27-0.33）因 RepoBench candidate
79	    pool 远大于 m2 验证集的 pool=50。方向一致性为 "directional evidence" 叙事提供第二个 benchmark 支持， 但效果量不足以做强声明。
80	
81	    '
82	  tables:
83	  - name: 'Table: RepoBench-R R@1 by Encoder × Strategy'
84	    columns:
85	    - Encoder
86	    - random
87	    - embedding
88	    - dataflow
89	    - embed Δ
90	    - dataflow Δ
91	    rows:
92	    - - Qwen2.5-Coder-3B
93	      - '0.312'
94	      - '0.325'
95	      - '0.318'
96	      - +1.3pp
97	      - +0.6pp
98	    - - StarCoder2-3B
99	      - '0.274'
100	      - '0.279'
101	      - '0.268'
102	      - +0.5pp
103	      - −0.6pp
104	  figures_description:
105	  - 'Grouped bar chart: R@1 per encoder × strategy，附 bootstrap 95% CI'
106	  analysis: 'RepoBench-R 结果与 SWE-smith eval 方向一致但效果量更小，增强 "directional evidence" 论点。
107	    写入论文时强调 cross-benchmark consistency of direction 而非 magnitude。
108	
109	    '
110	- name: Embedding vs random deep analysis by repo complexity
111	  plan_id: plan_005
112	  description: 按 repo size/complexity 分层分析 embedding negatives 的效果
113	  expected_results:
114	    small_repos_lt50_embed_delta_pp: 2.1
115	    medium_repos_50_200_embed_delta_pp: 1.0
116	    large_repos_200_500_embed_delta_pp: 0.3
117	    xlarge_repos_500plus_embed_delta_pp: -0.2
118	    complexity_correlation_r: -0.41
119	    complexity_correlation_p: 0.08
120	  result_rationale: 'median 档下 embedding benefit 在小 repo 上最明显（candidate pool 小，embedding
121	    distance 能有效区分 near-miss），但随 repo 规模增大效果递减甚至反转。原因：大 repo 中 embedding space 拥挤程度更高，pretrained
122	    encoder 的 representation 更接近 saturation， embedding-distance mining 选出的 negatives
123	    与 random 的 difficulty 差异缩小。 相关性方向正确（r ≈ −0.41）但 p=0.08 不显著——样本量仅 123 repos 中有结构数据的子集，
124	    power 不足。此分析为 Claim 2 的 saturation 机制提供 supporting but inconclusive evidence。
125	
126	    '
127	  tables:
128	  - name: 'Table: Embedding Δ by Repo Size Tier (Qwen)'
129	    columns:
130	    - Tier
131	    - N repos
132	    - embed Δ R@1 (pp)
133	    - mean neg_difficulty margin
134	    rows:
135	    - - <50 instances
136	      - '1'
137	      - '+2.1'
138	      - '0.068'
139	    - - 50–200
140	      - '17'
141	      - '+1.0'
142	      - '0.032'
143	    - - 200–500
144	      - '40'
145	      - '+0.3'
146	      - '0.019'
147	    - - 500+
148	      - '29'
149	      - −0.2
150	      - '0.014'
151	  figures_description:
152	  - 'Scatter plot: repo size (x) vs embedding benefit Δ (y), with regression line
153	    and 95% CI band'
154	  - 'Box plot: neg_difficulty margin distribution by repo size tier'
155	  analysis: '趋势方向支持 saturation hypothesis 但统计力度不足（p=0.08）。 论文中作为 "exploratory analysis
156	    suggesting repo complexity moderates embedding benefit"， n=2 编码器 × uneven tier
157	    sizes 限制了因果推断。
158	
159	    '
160	- name: 1-hop vs 2-hop vs 3-hop call-graph bounding ablation
161	  plan_id: plan_007
162	  description: 测试不同 call-graph 深度对 dataflow negative 质量的影响
163	  expected_results:
164	    hop1_qwen_R1: 0.531
165	    hop2_qwen_R1: 0.538
166	    hop3_qwen_R1: 0.534
167	    hop1_coverage_pct: 42.1
168	    hop2_coverage_pct: 34.3
169	    hop3_coverage_pct: 28.7
170	    hop2_vs_hop1_delta_pp: 0.7
171	    hop3_vs_hop2_delta_pp: -0.4
172	  result_rationale: 'median 档下 hop 数的 ablation 呈倒 U 型但差异不大。2-hop（当前设置）略优于 1-hop 因为覆盖了更多真实的
173	    transitive dependencies，但 3-hop 引入过多 spurious connections （大 repo 中 3-hop 几乎把所有文件连通），diluting
174	    structural signal。 差异仅 ~0.7pp，在 cross-seed 方差 1.5-3.0pp 的背景下不显著。 Coverage 随 hop
175	    增加而下降（disconnected files 减少 → 可选 negative 减少）。 这说明当前 2-hop 设置合理但并非 critical design
176	    choice。
177	
178	    '
179	  tables:
180	  - name: 'Table: Hop Depth Ablation (Qwen, dataflow strategy)'
181	    columns:
182	    - Hops
183	    - R@1
184	    - Coverage (%)
185	    - Avg negatives/query
186	    rows:
187	    - - 1-hop
188	      - '0.531'
189	      - '42.1'
190	      - '8.3'
191	    - - 2-hop
192	      - '0.538'
193	      - '34.3'
194	      - '5.7'
195	    - - 3-hop
196	      - '0.534'
197	      - '28.7'
198	      - '3.9'
199	  figures_description:
200	  - 'Line plot: R@1 vs hop depth, with error bars from 3 seeds'
201	  analysis: '2-hop 是 sweet spot 但差异在噪声范围内。论文中简要报告作为 design justification， 不作为独立 finding。
202	
203	    '
204	- name: Training data size scaling ablation
205	  plan_id: plan_008
206	  description: 1K vs 3K vs 5K training instances, 测试 data scaling behavior
207	  expected_results:
208	    size_1k_qwen_R1: 0.518
209	    size_3k_qwen_R1: 0.541
210	    size_5k_qwen_R1: 0.538
211	    size_1k_embed_delta_pp: 1.8
212	    size_3k_embed_delta_pp: 1.1
213	    size_5k_embed_delta_pp: 0.9
214	    size_1k_starcoder_R1: 0.432
215	    size_3k_starcoder_R1: 0.451
216	    size_5k_starcoder_R1: 0.448
217	  result_rationale: 'median 档下 data scaling 呈 diminishing returns：1K→3K 有明显提升（+2.3pp），
218	    3K→5K 几乎持平甚至微降（过拟合加剧，与 m2_full 观察到的 step 1000 后过拟合一致）。 更关键的是 embedding benefit
219	    Δ 随数据量增加而缩小：1K 时 Δ=1.8pp（小数据下 hard negative 质量差异被放大），5K 时 Δ=0.9pp（更多数据提供足够 coverage，减少对
220	    mining 策略的依赖）。 这对 median 叙事不利——暗示在更大数据规模下 embedding benefit 可能进一步缩水。
221	
222	    '
223	  tables:
224	  - name: 'Table: Data Scaling × Strategy (Qwen, embedding strategy)'
225	    columns:
226	    - Train Size
227	    - random R@1
228	    - embed R@1
229	    - Δ (pp)
230	    rows:
231	    - - 1K
232	      - '0.500'
233	      - '0.518'
234	      - '+1.8'
235	    - - 3K
236	      - '0.530'
237	      - '0.541'
238	      - '+1.1'
239	    - - 5K
240	      - '0.529'
241	      - '0.538'
242	      - '+0.9'
243	  figures_description:
244	  - 'Line plot: R@1 vs training data size, separate lines for random/embed/dataflow'
245	  - 'Bar chart: embed Δ at each data size, showing diminishing gap'
246	  analysis: 'Diminishing benefit at larger data scale 是 median 档的典型特征——方向正确但实际意义 随
247	    scale 递减。论文中诚实报告，作为 limitation 的一部分。
248	
249	    '
250	- name: Fusion head ablation
251	  plan_id: plan_009
252	  description: embedding-only vs structural-features-only vs combined scoring
253	  expected_results:
254	    embed_only_qwen_R1: 0.538
255	    struct_only_qwen_R1: 0.489
256	    combined_qwen_R1: 0.541
257	    embed_only_starcoder_R1: 0.451
258	    struct_only_starcoder_R1: 0.412
259	    combined_starcoder_R1: 0.448
260	    combined_vs_embed_only_delta_pp: 0.3
261	  result_rationale: 'median 档下 structural features alone 表现较差（R@1=0.489），因为 CodeQL
262	    dataflow features 是 binary/sparse 的，单独使用缺乏 fine-grained discrimination。 Combined
263	    (embed + struct) 仅比 embed-only 好 +0.3pp——structural signal 的增量贡献在融合后被稀释，且 combined
264	    model 有更多参数容易过拟合（与 step 1000 过拟合现象一致）。StarCoder 上 combined 甚至略低于 embed-only（-0.3pp），
265	    因为 StarCoder 的 healthy representation space 不需要额外维度的信号。 这进一步支持 "conditional benefit"
266	    的定性结论但效果量太小。
267	
268	    '
269	  tables:
270	  - name: 'Table: Fusion Head Ablation'
271	    columns:
272	    - Head
273	    - Qwen R@1
274	    - StarCoder R@1
275	    rows:
276	    - - embed-only
277	      - '0.538'
278	      - '0.451'
279	    - - struct-only
280	      - '0.489'
281	      - '0.412'
282	    - - combined
283	      - '0.541'
284	      - '0.448'
285	  figures_description:
286	  - Stacked bar chart showing contribution decomposition of embed vs struct features
287	  analysis: 'Combined head 增益微乎其微，论文中报告为 "structural features provide marginal additive
288	    benefit in fusion"。不值得作为独立 contribution point。
289	
290	    '
291	- name: Dataflow-distance weighted negatives ablation
292	  plan_id: plan_010
293	  description: weighted sampling by dataflow distance vs binary connected/disconnected
294	  expected_results:
295	    binary_qwen_R1: 0.538
296	    weighted_qwen_R1: 0.535
297	    binary_starcoder_R1: 0.448
298	    weighted_starcoder_R1: 0.444
299	  result_rationale: 'median 档下 weighted sampling 不优于 binary。原因：CodeQL 提取的 dataflow
300	    distance 分布高度 bimodal（connected with distance 1-2 占大多数，disconnected 占其余）， smooth
301	    weighting 在这种分布上退化为近似 binary。且 weighted 引入的额外超参数 （distance decay function）在 n=123
302	    repos 的数据量下难以 tune，noise 抵消了 理论上的 curriculum benefit。这是一个 null result，说明 binary
303	    structural signal 已捕获大部分可用信息。
304	
305	    '
306	  tables:
307	  - name: 'Table: Weighted vs Binary Dataflow Negatives'
308	    columns:
309	    - Method
310	    - Qwen R@1
311	    - StarCoder R@1
312	    rows:
313	    - - binary (current)
314	      - '0.538'
315	      - '0.448'
316	    - - distance-weighted
317	      - '0.535'
318	      - '0.444'
319	  figures_description:
320	  - Histogram of dataflow distances showing bimodal distribution
321	  analysis: 'Null result，论文中用一句话在 ablation section 报告："distance-weighted sampling
322	    does not improve over binary selection, likely due to the bimodal distance distribution."
323	
324	    '
325	- name: SWE-bench failure analysis
326	  plan_id: plan_011
327	  description: 50 SweRank/BM25 failure cases 分类分析
328	  expected_results:
329	    total_analyzed: 50
330	    category_retrieval_miss: 18
331	    category_generation_fail: 22
332	    category_test_flaky: 4
333	    category_multi_file_needed: 6
334	    retrieval_miss_where_dataflow_helps: 5
335	    retrieval_miss_where_dataflow_neutral: 10
336	    retrieval_miss_where_dataflow_hurts: 3
337	    pct_dataflow_helps_of_retrieval_miss: 27.8
338	  result_rationale: 'median 档下 failure analysis 揭示 SWE-bench 上 retrieval 并非主要瓶颈——
339	    50 个失败案例中仅 18 个（36%）是因为 retrieval miss，其余是 generation/test issues。 在 18 个 retrieval
340	    miss 中，dataflow 仅帮助 5 个（27.8%）——这些是跨文件依赖链上的 bug，dataflow connectivity 确实提供了有用信号。但
341	    10 个 neutral（文件间无 dataflow 关系或关系被 CodeQL 漏提取）和 3 个 hurt（dataflow 引入 noise 反而 distract）
342	    使整体效果被抵消。这解释了为什么 plan_003 中 SWE-bench resolve rate 差异 <1pp。
343	
344	    '
345	  tables:
346	  - name: 'Table: Failure Category Distribution'
347	    columns:
348	    - Category
349	    - Count
350	    - '%'
351	    rows:
352	    - - Retrieval miss
353	      - '18'
354	      - 36%
355	    - - Generation failure
356	      - '22'
357	      - 44%
358	    - - Flaky test
359	      - '4'
360	      - 8%
361	    - - Multi-file needed
362	      - '6'
363	      - 12%
364	  - name: 'Table: Dataflow Impact on Retrieval Misses'
365	    columns:
366	    - Dataflow effect
367	    - Count
368	    - '%'
369	    rows:
370	    - - Helps
371	      - '5'
372	      - 27.8%
373	    - - Neutral
374	      - '10'
375	      - 55.6%
376	    - - Hurts
377	      - '3'
378	      - 16.7%
379	  figures_description:
380	  - 'Sankey diagram: failure categories → dataflow impact'
381	  - 'Concrete example pair: one case where dataflow helped (cross-module dependency)
382	    and one where it hurt (false connectivity)'
383	  analysis: 'Failure analysis 提供定性 insight 但定量上支持 "generation bottleneck dominates
384	    retrieval differences" 的结论。论文中用于 explain 为什么 SWE-bench Δ 小， 并 motivate future
385	    work on generation-aware retrieval。
386	
387	    '
388	- name: Qualitative examples
389	  plan_id: plan_012
390	  description: 5-10 cases where structural negatives changed retrieval outcome
391	  expected_results:
392	    positive_examples_found: 4
393	    negative_examples_found: 2
394	    ambiguous_examples: 2
395	    total_curated: 8
396	  result_rationale: 'median 档下能找到 4 个 convincing positive examples（dataflow negative
397	    帮助 retriever 区分 lexically similar but structurally unrelated files），但也有 2 个 negative
398	    examples（dataflow 引入的 structural bias 导致 miss）。 这与 median 的 "directional but not
399	    definitive" 叙事一致。8 个案例中 pattern 不够 clean 来支持强因果推断——n=2 编码器 + case-by-case 分析 只能说明
400	    mechanism 是 plausible 而非 proven。
401	
402	    '
403	  tables: []
404	  figures_description:
405	  - 'Figure: 2 positive + 1 negative case study panels, showing query → retrieved
406	    files → gold files, with dataflow graph overlay'
407	  analysis: '精选 cases 放入论文 qualitative section，明确标注 positive 和 negative examples 以保持学术诚实。reviewer
408	    会 appreciate balanced presentation。
409	
410	    '
411	- name: Temperature ablation
412	  plan_id: plan_014
413	  description: τ ∈ {0.05, 0.1, 0.2}, 3 strategies × 2 encoders
414	  expected_results:
415	    qwen_tau005_random_R1: 0.521
416	    qwen_tau005_embed_R1: 0.534
417	    qwen_tau005_dataflow_R1: 0.53
418	    qwen_tau010_random_R1: 0.533
419	    qwen_tau010_embed_R1: 0.543
420	    qwen_tau010_dataflow_R1: 0.538
421	    qwen_tau020_random_R1: 0.524
422	    qwen_tau020_embed_R1: 0.531
423	    qwen_tau020_dataflow_R1: 0.527
424	    starcoder_tau005_random_R1: 0.438
425	    starcoder_tau005_embed_R1: 0.443
426	    starcoder_tau005_dataflow_R1: 0.43
427	    starcoder_tau010_random_R1: 0.449
428	    starcoder_tau010_embed_R1: 0.456
429	    starcoder_tau010_dataflow_R1: 0.441
430	    starcoder_tau020_random_R1: 0.442
431	    starcoder_tau020_embed_R1: 0.446
432	    starcoder_tau020_dataflow_R1: 0.435
433	    embed_benefit_direction_consistent_across_tau: true
434	    dataflow_benefit_direction_inconsistent: true
435	    optimal_tau: 0.1
436	  result_rationale: 'median 档下 temperature ablation 证明 embedding > random 的方向在所有 τ
437	    值下一致 （这是好消息，说明发现非 regime-specific）。但 Δ 在 τ=0.05 和 τ=0.2 下缩小： τ=0.05 时 loss landscape
438	    过于 sharp，所有策略表现都下降，差异被 noise 淹没； τ=0.2 时 loss 太平滑，hard negatives 的难度梯度被抹平。τ=0.1
439	    是 sweet spot。 Dataflow 的方向在 τ 间不一致——τ=0.05 时 Qwen 上 dataflow 略优于 random， τ=0.2
440	    时略劣——进一步支持 "conditional and fragile" 的定性判断。 Cross-seed 方差在 τ=0.05 下最大（~3.0pp std），τ=0.1
441	    最稳定（~1.8pp std）。
442	
443	    '
444	  tables:
445	  - name: 'Table: Temperature × Strategy R@1 (Qwen)'
446	    columns:
447	    - τ
448	    - random
449	    - embed
450	    - dataflow
451	    - embed Δ
452	    - dataflow Δ
453	    rows:
454	    - - '0.05'
455	      - '0.521'
456	      - '0.534'
457	      - '0.530'
458	      - '+1.3'
459	      - '+0.9'
460	    - - '0.10'
461	      - '0.533'
462	      - '0.543'
463	      - '0.538'
464	      - '+1.0'
465	      - '+0.5'
466	    - - '0.20'
467	      - '0.524'
468	      - '0.531'
469	      - '0.527'
470	      - '+0.7'
471	      - '+0.3'
472	  - name: 'Table: Temperature × Strategy R@1 (StarCoder)'
473	    columns:
474	    - τ
475	    - random
476	    - embed
477	    - dataflow
478	    - embed Δ
479	    - dataflow Δ
480	    rows:
481	    - - '0.05'
482	      - '0.438'
483	      - '0.443'
484	      - '0.430'
485	      - '+0.5'
486	      - −0.8
487	    - - '0.10'
488	      - '0.449'
489	      - '0.456'
490	      - '0.441'
491	      - '+0.7'
492	      - −0.8
493	    - - '0.20'
494	      - '0.442'
495	      - '0.446'
496	      - '0.435'
497	      - '+0.4'
498	      - −0.7
499	  figures_description:
500	  - 'Heatmap: τ × strategy, cell color = R@1, separate panels for Qwen and StarCoder'
501	  - 'Line plot: embed Δ vs τ, showing consistent positive direction'
502	  analysis: 'Temperature ablation 是 median 档的关键正面结果之一：embedding benefit 方向 robust
503	    across τ。 论文中重点报告此 robustness 作为 Claim 1 的 supporting evidence， 同时 acknowledge
504	    Claim 2 (dataflow) 的 τ-sensitivity 作为 limitation。
505	
506	    '
507	- name: Dynamic mining baseline
508	  plan_id: plan_015
509	  description: re-mine embedding negatives per epoch vs static (mine once from pretrained)
510	  expected_results:
511	    static_qwen_R1: 0.543
512	    dynamic_qwen_R1: 0.547
513	    static_starcoder_R1: 0.456
514	    dynamic_starcoder_R1: 0.452
515	    dynamic_vs_static_qwen_delta_pp: 0.4
516	    dynamic_vs_static_starcoder_delta_pp: -0.4
517	    dynamic_compute_overhead_factor: 3.2
518	  result_rationale: 'median 档下 dynamic mining 在 Qwen 上微优（+0.4pp）但 StarCoder 上微劣（-0.4pp），
519	    差异在 noise 范围内。原因：(1) static mining 在仅 3 epoch 的训练中 representation drift 有限——encoder
520	    是 LoRA fine-tune，参数变化量小，pretrained 时的 embedding distance 排序在训练后基本保持；(2) dynamic
521	    re-mining 引入计算开销（3.2x）但因 LoRA 的低 drift 几乎不改变 negative selection；(3) StarCoder
522	    上 dynamic 略差可能因 re-mining 引入的 randomness（每次 re-mining 的 batch 不完全一致）。结论：static
523	    vs dynamic 不是 关键 confound，当前 static 设计合理。
524	
525	    '
526	  tables:
527	  - name: 'Table: Static vs Dynamic Mining'
528	    columns:
529	    - Mining
530	    - Qwen R@1
531	    - StarCoder R@1
532	    - GPU hours
533	    rows:
534	    - - Static (current)
535	      - '0.543'
536	      - '0.456'
537	      - '3.5'
538	    - - Dynamic (per-epoch)
539	      - '0.547'
540	      - '0.452'
541	      - '11.2'
542	  figures_description:
543	  - 'Bar chart: static vs dynamic R@1, with compute cost annotation'
544	  analysis: 'Null result for practical purposes. 论文中一句话报告："dynamic re-mining does
545	    not significantly improve over static mining given the limited representation
546	    drift in LoRA fine-tuning (3 epochs)"。排除了 reviewer concern about static/dynamic
547	    confound。
548	
549	    '
550	- name: Bootstrap CI for SWE-bench Lite
551	  plan_id: plan_016
552	  description: 95% bootstrap CI for resolve rate differences
553	  expected_results:
554	    embed_vs_random_delta_pp: 0.4
555	    embed_vs_random_95ci_lower: -1.8
556	    embed_vs_random_95ci_upper: 2.6
557	    dataflow_vs_random_delta_pp: -0.3
558	    dataflow_vs_random_95ci_lower: -2.5
559	    dataflow_vs_random_95ci_upper: 1.9
560	    bootstrap_n: 10000
561	    embed_vs_random_p_value: 0.34
562	  result_rationale: 'median 档下 SWE-bench 的 Δ ≤ 1pp，在 300 instances 上 bootstrap CI
563	    极宽。 300 实例的 binomial 标准误约 ±2.2pp（at resolve rate ~18%）， 所以 Δ=0.4pp 的 95% CI 为
564	    [-1.8, +2.6]，包含零。p=0.34 远不显著。 这是 median 档的核心弱点：无法宣称下游收益。 Dataflow 的 CI 同样包含零且
565	    point estimate 为负。
566	
567	    '
568	  tables:
569	  - name: 'Table: SWE-bench Bootstrap CI'
570	    columns:
571	    - Comparison
572	    - Δ (pp)
573	    - 95% CI
574	    - p-value
575	    rows:
576	    - - embed vs random
577	      - '+0.4'
578	      - '[−1.8, +2.6]'
579	      - '0.34'
580	    - - dataflow vs random
581	      - −0.3
582	      - '[−2.5, +1.9]'
583	      - '0.41'
584	  figures_description:
585	  - 'Forest plot: point estimates with 95% CI bars, reference line at zero'
586	  analysis: 'CI 均包含零，论文中必须诚实报告 "no statistically significant difference in downstream
587	    resolve rate"。但可同时 argue retrieval-level improvements (plan_002/plan_013) 的 bootstrap
588	    CI 更紧（pool=50 的 val set 上）， downstream pipeline 的 noise 是 confound 而非 evidence
589	    against retrieval gains。
590	
591	    '
592	- name: Inference-time graph method comparison discussion
593	  plan_id: plan_017
594	  description: 与 CodexGraph, LocAgent 等 inference-time 方法的定位比较
595	  expected_results:
596	    comparison_type: qualitative_discussion
597	    codexgraph_reported_R1_improvement_pp: 5.2
598	    locagent_reported_resolve_rate_pct: 26.3
599	    structfuse_retrieval_R1: 0.543
600	    key_distinction: training-time vs inference-time structural signal
601	    complementarity_argument_strength: moderate
602	  result_rationale: 'median 档下此项为 qualitative discussion 而非实验。StructFuse（training-time
603	    structural mining）与 CodexGraph/LocAgent（inference-time graph navigation） 在方法论上互补：前者提升
604	    base retriever 质量，后者在 inference 时做 multi-hop reasoning。但 median 档下 StructFuse
605	    的 absolute improvement 较小（+1pp R@1）， complementarity argument 的说服力为 "moderate"——reviewer
606	    可能问 "if inference-time methods already get +5pp, why bother with +1pp training-time
607	    improvement?" 回应：training-time improvement 是 zero-cost at inference，可叠加使用。
608	
609	    '
610	  tables:
611	  - name: 'Table: Training-time vs Inference-time Structural Methods'
612	    columns:
613	    - Method
614	    - Type
615	    - Structural Signal
616	    - Inference Cost
617	    - Reported Gain
618	    rows:
619	    - - StructFuse (ours)
620	      - training-time
621	      - CodeQL dataflow
622	      - zero
623	      - +0.5–1.5pp R@1
624	    - - CodexGraph
625	      - inference-time
626	      - LLM-built graph
627	      - high (LLM calls)
628	      - +5.2pp R@1
629	    - - LocAgent
630	      - inference-time
631	      - call graph navigation
632	      - moderate
633	      - 26.3% resolve
634	  figures_description:
635	  - Comparison table in Related Work section
636	  analysis: Discussion section 而非实验。定位 StructFuse 为 complementary approach—— zero
637	    inference cost, improves base retriever that inference-time methods build upon.
638	    Acknowledge median 档的 modest gains 使此 argument 需要 future work validation。
639	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf2f7eeb-54fe-430f-95e8-8c747f11e68e",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "f721e4bc-29ca-46e7-a0c8-0316fd8252e8",
  "sourceToolAssistantUUID": "cf2f7eeb-54fe-430f-95e8-8c747f11e68e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-14T08:32:26.248Z_

Now I have a thorough understanding of the paper, its experimental history, and the three dream tiers. Let me now compose my R2 review focused on Novelty and Related Work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f721e4bc-29ca-46e7-a0c8-0316fd8252e8",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29i3UPw86fCu99zPGKA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f8c217c-93b0-4594-9605-41b14a138513",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxuCMjETGhQDc8dM1aZi1U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12985,
      "cache_read_input_tokens": 65046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12985,
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

_source line 46 · 2026-05-14T08:32:27.302Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016Sxs6wsShwjv6Uvqi8GS3Z`</summary>

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
  "parentUuid": "9f8c217c-93b0-4594-9605-41b14a138513",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29i3UPw86fCu99zPGKA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f6bcc00-1e36-4f04-bb58-9bfabf51a67f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxuCMjETGhQDc8dM1aZi1U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12985,
      "cache_read_input_tokens": 65046,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12985
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 65046,
          "cache_creation_input_tokens": 12985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12985,
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

_source line 47 · 2026-05-14T08:32:27.303Z_

<details><summary>↩ Tool result · `toolu_016Sxs6wsShwjv6Uvqi8GS3Z`</summary>

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
  "parentUuid": "0f6bcc00-1e36-4f04-bb58-9bfabf51a67f",
  "isSidechain": true,
  "promptId": "a754f26b-cbe4-42ab-a160-e44cefdd0e15",
  "agentId": "a24f4b66a47cd9d75",
  "type": "user",
  "uuid": "8dff3e94-84e0-41ae-8175-2ff312489242",
  "sourceToolAssistantUUID": "0f6bcc00-1e36-4f04-bb58-9bfabf51a67f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-14T08:33:51.179Z_



Now I have all the information needed to write a thorough R2 review. Let me examine the three paper tiers carefully and synthesize my assessment. The task asks me to review the paper as described in the prompt (which corresponds to the "median" tier), so I'll focus on that version.

Here is my review:

---

## Reviewer 2 (R2): Novelty and Related Work

### Summary

This paper presents a controlled comparison of three hard negative mining strategies (random, embedding-distance, dataflow-aware) for contrastive code retrieval, tested on two 3B-parameter code encoders. The main findings are that embedding-distance mining provides small directional improvements over random (+0.5--1.3pp R@1), dataflow-aware mining is inconsistent across encoders, and no strategy produces statistically significant downstream gains on SWE-bench Lite. The paper positions itself as a methodology/analysis contribution correcting a prior misconception from CoCoHaNeRe about embedding negatives harming code search.

### Strengths

- **CoCoHaNeRe correction has genuine community value.** If the prior finding that embedding-distance negatives harm code search is indeed an artifact of BM25-proxy mislabeling, clarifying this matters for practitioners. The paper identifies a specific methodological confound (BM25 conflated with embedding distance) that could redirect research effort.

- **Honest reporting of null and negative results.** The paper does not hide that dataflow negatives are inconsistent across encoders (StarCoder: -0.6pp on RepoBench-R), that SWE-bench Lite shows no significant differences (all p > 0.3), and that StarCoder embedding gains have CIs including zero. This candor is commendable and increasingly valuable in ML research.

- **Representation geometry diagnostic is a potentially actionable insight.** The observation that pos_sim (0.986 for Qwen vs. 0.799 for StarCoder) correlates with strategy effectiveness offers practitioners a cheap pre-training diagnostic. If validated on more encoders, this could become a useful heuristic.

- **Comprehensive ablation suite.** Temperature, hop distance, data scaling, fusion head, static vs. dynamic mining, binary vs. weighted dataflow, and failure analysis --- the breadth of ablations partially compensates for small effect sizes by providing a thorough landscape view.

- **Correct separation of training-time vs. inference-time value.** The fusion head ablation (Table showing structural features alone perform poorly) cleanly demonstrates that structural information's value is in negative selection, not inference-time scoring. This is a crisp insight.

- **"Directional evidence" framing is appropriately calibrated** for the median-tier results. The paper does not overclaim given the evidence.

### Weaknesses

- **The "first controlled comparison" novelty claim is overstated and poorly substantiated.** The paper claims to be the "first controlled comparison using true embedding-distance negatives for code retrieval." This is a strong priority claim that requires rigorous evidence of absence. The paper does not systematically survey whether other work has used true embedding-distance mining for code --- it only critiques CoCoHaNeRe. ANCE-style mining (which uses actual embedding distance) has existed since 2021 and has been applied broadly across retrieval domains. The claim that nobody has done this for code specifically requires more thorough documentation than citing a single paper's methodological error.

- **The CoCoHaNeRe critique is the paper's central motivation but remains unverified within the paper.** The entire narrative depends on the claim that CoCoHaNeRe used BM25-proxy negatives mislabeled as embedding-distance. Yet the paper never (a) provides specific textual evidence from CoCoHaNeRe showing the mislabeling, (b) reproduces the CoCoHaNeRe setup with BM25 negatives to demonstrate the claimed -27pp harm, or (c) runs BM25 negatives in its own framework to show they produce different results from true embedding negatives. Without running an actual BM25 negative baseline, the "correcting a misconception" claim is speculative. This is the single most important missing experiment for the paper's framing.

- **Representation geometry analysis is shallow despite impressive-sounding terminology.** "Representation geometry" and "representation saturation" suggest deep analysis, but the substance is: one encoder has pos_sim=0.99 and the other has pos_sim=0.80, and they respond differently to mining strategies. With n=2 encoders, this is an anecdotal observation, not a validated theory. The paper does not (a) test whether pos_sim is actually predictive by measuring it on additional encoders, (b) connect to the existing theoretical literature on optimal negative difficulty (Robinson et al. 2021, "Contrastive Learning with Hard Negative Samples"; Kalantidis et al. 2020, "Hard Negative Mixing"), or (c) provide any formal relationship between pos_sim and expected mining benefit. The negative-difficulty margin analysis ("margins +17% for Qwen, +28% for StarCoder") provides supporting texture but does not elevate the observation to a mechanistic explanation.

- **Significant related work gaps for a paper positioned as a systematic study.** An analysis paper surveying hard negative mining must comprehensively cover the landscape. Missing references include:
  - **Hard negative theory:** Robinson et al. 2021 (optimal negative difficulty), Kalantidis et al. 2020 (hard negative mixing) --- directly relevant to the saturation finding.
  - **Foundational retrieval:** SimCLR, MoCo (contrastive learning foundations that studied negative difficulty).
  - **Code representation models:** CodeBERT, UniXcoder, CodeT5+ --- standard baselines for any code retrieval study.
  - **Structural code methods:** CodeGRAG (training + inference graph usage), GraphCoder (intra-procedural data/control flow), RepoGraph (ICLR 2025).
  - **Curriculum-based mining:** The paper mentions curriculum approaches in one sentence without citations or comparison.
  
  For a paper that claims "systematic study" in its title, this coverage is insufficient.

- **The CodeQL pipeline is an engineering contribution, not a research contribution.** "0% timeout at 123-repo scale" is a reliability metric for a software tool. The 34% instance-level coverage is the more scientifically relevant number, and it is a significant limitation. The paper frames the pipeline as Contribution (3), but it is essentially: "we ran CodeQL on some repos and it worked." The connected-not-gold rate (Z%=78% conditional, but only 34% of instances even have structural data) means the structural signal is absent for two-thirds of training data. This is underreported.

- **The paper introduces a method (dataflow negatives) and then shows it does not consistently work --- but still frames it as a contribution.** The dataflow strategy is inconsistent: +0.6pp on Qwen RepoBench-R but -0.6pp on StarCoder. On SWE-bench Lite, dataflow is -0.3pp vs. random. The "conditional benefit" framing sounds like the paper is repackaging a negative result as a finding. If the proposed method only works on one of two tested encoders and not downstream, the honest conclusion is that it failed, not that it "provides conditional benefit mediated by representation saturation."

- **Effect sizes are too small for practical relevance.** +0.5--1.3pp R@1 on RepoBench-R, with StarCoder's CI including zero, and no downstream significance. The comparison to inference-time methods in Table 14 is self-damaging: StructFuse gets +0.5--1.5pp while CodexGraph gets +5.2pp. The paper acknowledges complementarity, but the practical case for investing in a CodeQL extraction pipeline for +0.5pp (that may not even be significant) is weak.

- **StarCoder2-3B is described as "encoder-decoder" but is decoder-only.** This architectural mischaracterization undermines the "architecturally distinct" cross-encoder narrative. Both Qwen2.5-Coder-3B and StarCoder2-3B are decoder-only models. The actual difference is in pretraining data and procedure, not architecture class. The paper should be honest about this: the cross-encoder comparison tests different pretraining, not different architectures.

- **No comparison with other training-time hard negative mining approaches.** The paper compares random, static embedding, and dataflow --- but omits ANCE-style dynamic mining as a proper baseline (the static vs. dynamic ablation is cursory), in-batch negatives (DPR-style), and curriculum-based mining. For a "systematic study," the strategy space is surprisingly narrow.

### Questions for Authors

1. **Can you provide the specific passage(s) from CoCoHaNeRe where BM25-proxy negatives are presented as embedding-distance negatives?** The entire paper hinges on this critique, but no textual evidence is provided. If this claim cannot be substantiated with direct quotes, the paper's central motivation collapses.

2. **Why did you not run a BM25 negative baseline?** This is the experiment most directly implied by your framing. If CoCoHaNeRe's -27pp harm comes from BM25 negatives, running BM25 negatives in your framework should reproduce the harm and cleanly separate it from the embedding-distance benefit.

3. **Have you measured pos_sim for any encoders beyond Qwen and StarCoder?** The representation saturation claim would be substantially strengthened if pos_sim were shown to predict mining benefit across 4--5 encoders (e.g., CodeBERT, UniXcoder, DeepSeek-Coder). With n=2, any pattern could be coincidental.

4. **What is the per-instance dataflow benefit stratified by structural data availability?** The +0.5--1.5pp improvements average over all instances, but 66% of instances have no structural data and fall back to non-dataflow negatives. What is the effect size among the 34% that actually receive dataflow-mined negatives?

5. **The data scaling ablation (Table showing diminishing benefit from 1K to 5K) suggests that at production scales, all mining strategies converge.** Do you agree this undermines the practical contribution? What is your estimate of the benefit at 50K or 100K training instances?

### Minor Issues

- All bibliography references appear as [?] in the PDF, indicating a broken bibliography. This must be fixed before submission.
- The paper name "StructFuse" implies a system contribution (fusing structural information), but the paper is an empirical analysis. The identity is confused --- either commit to "StructFuse" as a system name and deliver a system, or drop the name and present purely as an analysis paper.
- RepoBench-R results (Table 1) have no statistical significance testing --- single checkpoint, no seeds or CIs reported. For an analysis paper emphasizing rigor, this is inconsistent.
- The number of negatives per query (K) is not stated in the main text.
- SWE-bench evaluation uses only Qwen checkpoints, not StarCoder, creating an asymmetry in the experimental matrix.

### Overall Assessment

This paper tackles a relevant question (what hard negative mining strategies work for code retrieval) with above-average experimental discipline (multiple seeds, bootstrap CIs, extensive ablations). However, the novelty is thin: embedding-distance mining is a known technique, the dataflow method does not consistently work, and the representation geometry "insight" rests on n=2 encoders without connection to existing contrastive learning theory. The paper's central narrative --- correcting CoCoHaNeRe's misconception --- is not substantiated within the paper itself (no BM25 baseline, no textual evidence from the original work). The effect sizes (+0.5--1.3pp, no downstream significance) are too small to be practically meaningful. As an analysis paper for EMNLP, it needs deeper analytical content: connection to hard negative theory, more encoders for the saturation claim, and the missing BM25 baseline to close its own argument. In its current form, the contributions are insufficient for a top venue.

### Score

**3 / 6 (Weak Reject)**

### Confidence

**4 / 5 (High)**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dff3e94-84e0-41ae-8175-2ff312489242",
  "isSidechain": true,
  "agentId": "a24f4b66a47cd9d75",
  "requestId": "req_011Cb29iTdDDfpq4us9XPoev",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f18a4e0d-3386-47de-8e21-0b18c475928a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "f4534d40-6470-414b-bd76-f15880fb0e07",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LZgrnt54RGCUaKpjwRFjP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 78031,
      "output_tokens": 2871,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 708
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2871,
          "cache_read_input_tokens": 78031,
          "cache_creation_input_tokens": 708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 708,
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
