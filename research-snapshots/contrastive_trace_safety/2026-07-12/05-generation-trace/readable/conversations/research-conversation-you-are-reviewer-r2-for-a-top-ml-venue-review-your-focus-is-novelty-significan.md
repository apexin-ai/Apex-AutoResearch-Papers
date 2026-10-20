# Research conversation: You are Reviewer R2 for a top ML venue review. Your focus is **novelty, significance, and related work positioning**. Re

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa9994fe9ca162224.jsonl`
- **Structured JSON:** [`468ae300e64402816c37.json`](../../sessions/46/468ae300e64402816c37.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-16T20:10:55.104Z_

You are Reviewer R2 for a top ML venue review. Your focus is **novelty, significance, and related work positioning**. Review the paper below thoroughly and produce a structured review.

## Paper Summary

**Title**: "Contrastive Trace Probing for Safety Commitment Detection in Reasoning Models: A Cross-Architecture Empirical Study"

**Core idea**: Reasoning models (DeepSeek-R1, QwQ) exhibit "self-jailbreak" where their chain-of-thought interleaves safety reasoning with harmful execution, culminating in a "commitment point" where safety reasoning permanently ceases. The paper studies hidden-state probing methods to detect this commitment point across 4 models, 2 architecture families (Llama-3.1, Qwen2.5), 2 scales (7-8B, 32B).

**Three claims**:
1. Static per-step probes fail (<50% coverage) despite high Fisher ratio (>14) because safety signal is in minor PCs
2. Temporal window LR (W=15) achieves 76.7% mean coverage matching oracle ceiling, +30-35pp over static
3. No hidden-state method achieves positive lead time (best: -0.2 steps vs oracle +31 steps)

**Related work covered**:
- Hidden-state jailbreak detection: TrajGuard (Chen et al. 2025, Mahalanobis distance on activation trajectories), SafeSwitch (Liu et al. 2025, linear probes on intermediate representations), SIREN (Park et al. 2025, contrastive hidden-state features). All operate at token-level on instruction-tuned models against adversarial inputs.
- Reasoning model safety: Wang et al. 2025 (self-jailbreak phenomenon), Zhang et al. 2025 (HarmThoughts dataset, 16-label taxonomy), SafeRemind (Li et al. 2025), SafeThink (Zhou et al. 2025) — text-level CoT monitoring.
- Linear probing: Belinkov 2022, Li et al. 2024 (truthfulness), Tigges et al. 2023 (sentiment), Meng et al. 2022 (factual knowledge).

**Methods used**:
- Static logistic regression probe (standard)
- Temporal window logistic regression (concatenate W hidden states)
- Mahalanobis distance baseline
- GRU sequential probe
- Label-sequence oracle
- Cross-architecture transfer with projection heads

**Key results**: 
- Static probes fail across all architectures (<50% coverage)
- Temporal W=15 achieves 76.7% mean coverage, matching oracle ceiling
- No hidden-state method achieves positive lead time
- Cross-architecture transfer yields 64.5% mean coverage
- GRU doesn't outperform temporal LR (overfits at 209-trace scale)
- Bootstrap CIs confirm all key deltas exclude zero

**Dataset**: 209 HarmThoughts traces, 4 models, step-level annotations.

## Your Review Task

Evaluate **novelty, significance, and related work positioning**. Produce:

1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, 4-6 items focusing on novelty/significance/positioning)
3. **Weaknesses** (bulleted, 4-6 items focusing on novelty limitations, missing related work, overclaimed contributions)
4. **Questions for authors** (3-5 specific questions about novelty/positioning)
5. **Missing related work or comparisons** that should be discussed
6. **Scores**:
   - Novelty (1-5)
   - Significance (1-5)
   - Related work coverage (1-5)
   - Overall recommendation (1-6 scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept)
   - Confidence (1-5)

Consider: Is the problem formulation novel? Are the methods novel or just standard techniques applied to a new domain? Is the "negative result" (lead time limitation) genuinely insightful or expected? Does the paper adequately position itself against existing work? Are the claims of "first" justified? Is the contribution incremental or substantial? Would this advance the field meaningfully?

Be critical but fair. A top ML venue (~25% acceptance rate) expects significant novelty or substantial empirical contribution that changes how we think about a problem.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "1c38a2b5-b295-490c-9efc-a8f7ea6db2cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T20:10:55.109Z_

```json
{
  "parentUuid": "1c38a2b5-b295-490c-9efc-a8f7ea6db2cc",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
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
  "uuid": "d3611530-dc17-4d02-9c7b-4e6a3472ef21",
  "timestamp": "2026-05-16T20:10:55.109Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T20:10:58.339Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PgpZDpt28Rd8egd3PQ8ru9`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3611530-dc17-4d02-9c7b-4e6a3472ef21",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rbVSCUHefNj3XGgNWg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f653723d-8428-42f1-a4dd-ea5a56a03ced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPp9C7w7xAzDnZYsP5pScU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6884,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6884,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 4 · 2026-05-16T20:10:58.342Z_

<details><summary>↩ Tool result · `toolu_01PgpZDpt28Rd8egd3PQ8ru9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f653723d-8428-42f1-a4dd-ea5a56a03ced",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "cbd4d6c1-18df-4587-8693-1e2cda2dda11",
  "sourceToolAssistantUUID": "f653723d-8428-42f1-a4dd-ea5a56a03ced",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T20:11:06.173Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01S6zqxhRSAf9S3yvhUyGYrr`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbd4d6c1-18df-4587-8693-1e2cda2dda11",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rbjneatETwBxDg7oy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9611586-e89d-41e1-a20a-1e4a591d26de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeN62u8oTjxze3brRDEakF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 15135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
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

_source line 6 · 2026-05-16T20:11:06.183Z_

<details><summary>↩ Tool result · `toolu_01S6zqxhRSAf9S3yvhUyGYrr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_gru256_multilayer** (success): —\\n- **diag_gru_probe** (negative): —\\n- **diag_d2_pca_viz** (success): —\\n  [D2 PCA visualizations](/api/workspace-files/projects/contrastive_trace_safety/artifacts/diag_d2_pca_viz/chart/d2_pca_viz_results.txt)\\n\\n## 趋势\\n成功 3 / 负向 3 / 失败 0 / 共 6\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-rtx6000: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 462, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9611586-e89d-41e1-a20a-1e4a591d26de",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "43619ed6-b51e-44b4-8f55-4ef33726da10",
  "sourceToolAssistantUUID": "b9611586-e89d-41e1-a20a-1e4a591d26de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T20:11:06.566Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0184hwjUEQL7M2FK2Lar7b2X`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43619ed6-b51e-44b4-8f55-4ef33726da10",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rbjneatETwBxDg7oy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d09f6eeb-491f-4c87-9353-5067e5df2b19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeN62u8oTjxze3brRDEakF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 15135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
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

_source line 8 · 2026-05-16T20:11:06.579Z_

<details><summary>↩ Tool result · `toolu_0184hwjUEQL7M2FK2Lar7b2X`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contrastive_trace_safety'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d09f6eeb-491f-4c87-9353-5067e5df2b19",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "6868ea19-9b34-441c-98df-707202e7f8a4",
  "sourceToolAssistantUUID": "d09f6eeb-491f-4c87-9353-5067e5df2b19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T20:11:06.729Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RX6WtgYtpx3Ndcyh3Sc3w4`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6868ea19-9b34-441c-98df-707202e7f8a4",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rbjneatETwBxDg7oy7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "797a2089-163f-4e41-8c83-d027082a7165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FeN62u8oTjxze3brRDEakF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 15135,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 293,
          "cache_read_input_tokens": 15135,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1269,
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

_source line 10 · 2026-05-16T20:11:06.749Z_

<details><summary>↩ Tool result · `toolu_01RX6WtgYtpx3Ndcyh3Sc3w4`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'contrastive_trace_safety'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "797a2089-163f-4e41-8c83-d027082a7165",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "8ca1774c-7531-4356-9277-aabf711cd860",
  "sourceToolAssistantUUID": "797a2089-163f-4e41-8c83-d027082a7165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T20:11:09.605Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G82VZN8kqjAHWGcr41HWrC`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ca1774c-7531-4356-9277-aabf711cd860",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rcMVywgfcm9rSmyfFS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d2d27e5-986c-4c99-b41d-723011976a68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179JEArAbVhmGcB9D5E5Xpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 16404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 900,
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

_source line 12 · 2026-05-16T20:11:09.615Z_

<details><summary>↩ Tool result · `toolu_01G82VZN8kqjAHWGcr41HWrC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/ROADMAP.md\", \"content\": \"# contrastive_trace_safety — Research Dashboard\\n\\n> 最后更新: 2026-05-16 19:47 UTC | 更新原因: Post-MVP kickoff: Research 阶段启动，framing + plan + dream 就绪\\n\\n## 核心方向\\n跨架构评估 hidden-state 检测方法在推理模型 safety commitment detection 上的表现。发现 temporal window probe 达到 oracle coverage 上限（+30pp over static），但 pre-textual detection 不可达。详见 paper_framing.md。\\n\\n## 当前阶段：Research（Post-MVP）\\n\\n**MVP 结论（2026-05-16）**：\\n- Hidden states 编码 safety commitment 信号（Fisher 17-18）\\n- Temporal LR W=15 → 76.7% coverage = oracle ceiling（static 仅 46.5%）\\n- Lead time ≤ 0 for all methods（oracle +31 步不可达）\\n- GRU 未超越 temporal LR（数据量限制）\\n\\n**Paper Claims**（详见 paper_framing.md）：\\n1. Static probes <50% coverage on reasoning traces\\n2. Temporal window saturates oracle coverage (+30pp)\\n3. Pre-textual detection fundamentally limited in hidden-state space\\n\\n## 当前进展\\n- MVP 完成（r1-8b，layer 14，full diagnostic round）\\n- paper_framing.md + experiment_plan.yaml 已写\\n- Dream simulate 进行中（dream_20260516T194646）\\n- 等 Dream 回调后批准 P0 实验\\n\\n## 近期任务\\n- [ ] 等 Dream 完成 → 评估 framing/plan 是否需调整\\n- [ ] exp-001: 32B 模型 hidden-state extraction（r1-32b + QwQ）\\n- [ ] exp-002: temporal LR on 32B models\\n- [ ] exp-003: cross-model transfer evaluation\\n- [ ] exp-005: TrajGuard Mahalanobis baseline\\n- [ ] exp-006: bootstrap CIs\\n\\n## GPU 预算\\n- 已分配：autodl-rtx6000（RTX PRO 6000 96GB × 2，cuda:0 + cuda:1）\\n- P0 总预算：~18 A100-hours\\n- 计划：两卡并行跑 r1-32b（cuda:0）+ QwQ（cuda:1）extraction\\n\\n## 投稿目标\\n- **EMNLP 2026 ARR**，DDL 2026-05-25（剩余 9 天）\\n- Timeline: P0 实验 5/17-19 → Paper writing 5/21-25\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D005 | 2026-05-16 | MVP 完整通过：GRU h=256 multi-7L 达成 +4.7 步 lead time +  | — |\\n| D004 | 2026-05-16 | MVP 条件性通过：temporal 优势在 coverage（+30pp → oracle 上限） | — |\\n| D003 | 2026-05-16 | MVP 首次结果未过 pass gate，批准 3-4h 诊断轮（layer sweep + PCA | — |\\n| D002 | 2026-05-16 | MVP 重设计：从 transition localization 改为 commitment de | — |\\n| D001 | 2026-05-16 | MVP 设计：用 DeepSeek-R1-Distill-Llama-8B + HarmThough | — |\\n\\n\", \"total_chars\": 1948, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d2d27e5-986c-4c99-b41d-723011976a68",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "ecdfa3f8-f14c-49ae-ad88-816397349a60",
  "sourceToolAssistantUUID": "2d2d27e5-986c-4c99-b41d-723011976a68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T20:11:10.547Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UUJCMn9YWv93ynva4u8iKA`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecdfa3f8-f14c-49ae-ad88-816397349a60",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rcMVywgfcm9rSmyfFS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32b35d4e-ee84-438a-a71f-cb5329d0ed10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179JEArAbVhmGcB9D5E5Xpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 16404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 900,
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

_source line 14 · 2026-05-16T20:11:10.556Z_

<details><summary>↩ Tool result · `toolu_01UUJCMn9YWv93ynva4u8iKA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md\", \"content\": \"# Paper Framing — contrastive_trace_safety\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (LLM Security Track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR submission May 25, 2026 (9 days)\\n\\n## Core Claims (3 条)\\n\\n1. **Static hidden-state probes fail to reliably detect safety commitment in reasoning model traces** — static per-step probes (LogisticRegression, linear classifiers analogous to SafeSwitch/SIREN) achieve <50% detection coverage on the commitment detection task, despite hidden states containing strong safety-relevant signal (Fisher discriminant ratio 17-18 in full representation space).\\n\\n2. **Temporal window probes saturate oracle-achievable detection coverage** — a simple temporal window LogisticRegression (W=15 steps) achieves 76.7% detection coverage, matching the label-oracle upper bound. The +30pp improvement over static probes comes from capturing \\\"safety reasoning density decline\\\" patterns invisible to single-step classification.\\n\\n3. **Pre-textual detection of safety commitment remains unreliable despite positive mean lead time** — GRU sequence models achieve positive mean lead time (+4.7 steps) but with median 0, std 13, and only 39% (13/33) of detected traces achieving genuine early detection. The oracle's +31-step advantage (100% early detection) reveals a fundamental gap: hidden states encode current safety state well but poorly predict future safety trajectory. This establishes that reliable pre-textual detection requires architectural advances beyond current sequential models.\\n\\n## Story Spine\\n\\n- **Problem**: Reasoning models exhibit \\\"self-jailbreak\\\" — safety reasoning and harmful execution are interleaved throughout extended CoT (84% of traces contain safety labels after step 10), culminating in a \\\"commitment point\\\" where safety reasoning permanently ceases. Existing hidden-state jailbreak detectors (TrajGuard, SafeSwitch, SIREN) are designed for instruction-tuned models where the attack is an adversarial INPUT; they have never been evaluated on reasoning-model self-jailbreak where the attack is the model's OWN reasoning process.\\n\\n- **Existing approaches & their gaps**: Hidden-state detectors achieve 95% defense rate on standard LLMs (TrajGuard) but operate at token-level granularity. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon but doesn't provide deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No work bridges hidden-state detection TO reasoning-model self-jailbreak.\\n\\n- **Our framing**: We provide the first systematic evaluation of hidden-state detection methods on reasoning-model safety commitment, discovering that (a) the safety signal exists but is distributed across minor principal components (PCA top-3 explains only 17% variance, Fisher drops from 17→1), making geometric methods (Mahalanobis/TrajGuard) fail; (b) temporal context is critical — temporal window LR saturates coverage (+30pp), and GRU achieves positive lead time (+4.7 steps); (c) but pre-textual detection remains unreliable (median 0, only 39% early detection vs oracle 100%), establishing a principled gap between current capabilities and the oracle ceiling.\\n\\n- **Headline result template**: \\\"On HarmThoughts reasoning traces, temporal methods achieve 76.7% detection coverage (matching oracle ceiling) and +4.7 steps mean lead time, while static probes achieve only 46.5% coverage with negative lead time — but reliable pre-textual detection remains elusive (39% early detection rate vs oracle 100%, +4.7 vs +31 steps).\\\"\\n\\n## Venue Fit Risks\\n\\n- **EMNLP LLM Security track fit**: Strong — defense/detection method for reasoning model jailbreak, directly addressing \\\"defense lags behind attack\\\" gap noted in track CFP.\\n- **Method simplicity risk**: Core methods are temporal LR (coverage) and GRU (lead time) — neither is architecturally novel. Mitigate: frame as empirical study with method insight; the contribution is the systematic evaluation + discovery of what matters (temporal context, adequate model capacity, multi-layer signal aggregation).\\n- **Unreliable timing risk**: Claim 3 shows GRU achieves +4.7 mean lead time but median 0 and high variance. Mitigate: frame honestly as \\\"proof of concept for timing but currently unreliable\\\" — this motivates future work while contributing the coverage + limitation analysis now.\\n- **Cross-architecture coverage**: MVP only tested on r1-8b (Llama-3.1 base). Must validate on Qwen2.5-based models (r1-32b, QwQ-32B) for the \\\"cross-architecture\\\" story. If temporal advantage doesn't hold cross-architecture → Claim 2 weakens to single-model.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. \\\"Temporal window LR is trivial — where's the method novelty?\\\" → Primary contribution is empirical study; method insight is that simplicity matches oracle ceiling.\\n2. \\\"Only tested on one model family\\\" → Cross-architecture experiments (P0) will address.\\n3. \\\"GRU lead time is unreliable (median 0, high variance)\\\" → Acknowledged; mean +4.7 shows the signal exists but is hard to extract reliably. The coverage contribution (+30pp) is robust. GRU lead time is presented as proof-of-concept, not deployed solution.\\n4. \\\"209 training traces is too few — results may not generalize\\\" → Cross-model validation + bootstrap CIs.\\n5. \\\"Why not use the full 16-label taxonomy for richer supervision?\\\" → Ablation planned (P1).\\n\", \"total_chars\": 5389, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32b35d4e-ee84-438a-a71f-cb5329d0ed10",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "5d93fc98-c653-40df-8e6a-42d7aa8718a7",
  "sourceToolAssistantUUID": "32b35d4e-ee84-438a-a71f-cb5329d0ed10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T20:11:10.897Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016YGvVNVrz5BgMjjg6119bt`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d93fc98-c653-40df-8e6a-42d7aa8718a7",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rcMVywgfcm9rSmyfFS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "231b7faa-d89c-4f66-8ba0-2911e1a62af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179JEArAbVhmGcB9D5E5Xpb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 16404,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 16404,
          "cache_creation_input_tokens": 900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 900,
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

_source line 16 · 2026-05-16T20:11:10.906Z_

<details><summary>↩ Tool result · `toolu_016YGvVNVrz5BgMjjg6119bt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/memory.md\", \"content\": \"# Project Memory\\n\\n## 2026-05-16: HarmThoughts Dataset Exploration Complete\\n\\n- Dataset: `ishitakakkar-10/HarmThoughts` (MIT, HuggingFace)\\n- 56,931 sentences across 1,018 traces from 4 models\\n- r1-8b: 324 traces, 14,746 sentences, avg 45.5 sentences/trace, 81.8% jailbreak rate\\n- 16-label sentence-level behavioral taxonomy\\n\\n## 2026-05-16: Commitment Point Distribution\\n\\n- CP = 最后一个 safety label + 1\\n- 覆盖率 78.9% (209/265 jailbreak traces)\\n- CP mean=34.4 / median=34.0, relative mean=70.5% / median=86.1%\\n- 双峰分布：18.2% 早期 + 41.6% 末尾\\n- 步骤标签平衡：74.5% pre / 25.5% post\\n\\n## 2026-05-16: MVP v1 NEGATIVE → 诊断轮 → GRU SUCCESS ✅\\n\\n### MVP v1 失败原因\\n- MLP 过拟合（20480-dim input, 125 traces）\\n- 错误层（layer 20 vs best layer 14）\\n- 无 class weighting\\n\\n### 诊断轮关键发现\\n- **Layer sweep**: best=14, all 78-81%, 层选择影响仅 3pp\\n- **PCA**: Fisher ~1.0 in PCA-3d, 信号分布式（top-3 PC 仅 17%）\\n- **Oracle**: K=5 可提前 31 步检测, 76.7% traces 可检测 → 任务确定可解\\n- **Linear methods 触顶 ~85%**, 瓶颈在非线性/序列建模\\n\\n### GRU h=256 实验：PASS ✅\\n| Method | Acc | Crossing% | Lead Mean | Lead Med |\\n|---|---|---|---|---|\\n| GRU multi 7L | 0.809 | 76.7% | **+4.7** | 0.0 |\\n| GRU single L14 | 0.839 | 72.1% | **+3.5** | 0.0 |\\n| LR multi 7L | 0.806 | 39.5% | +1.1 | 0.0 |\\n| LR single L14 | 0.817 | 46.5% | -2.0 | -2.0 |\\n\\n**Pass gate**: GRU multi lead (+4.7) vs LR best (+1.1) = delta **+3.6 > 3** → PASS\\n**关键**: 序列建模确认有效，multi-layer 聚合分布式信号有帮助\\n\\n### 经验教训\\n1. 线性 probe 诊断先行——排除过拟合/层选择等变量后再加序列建模\\n2. Class weighting 对 25/75 不平衡至关重要\\n3. Multi-layer mean 比单层好，信号确实分布在多层\\n4. GRU h=128 不够（lead -0.2），h=256 才突破（lead +3.5/+4.7）→ 容量有阈值效应\\n5. 209 traces 对 GRU h=256 够用（early stop epoch 11，未严重过拟合）\\n\\n## 2026-05-16: 服务器环境\\n\\n- autodl-rtx6000: 2× RTX PRO 6000 94GB, Python 3.12.3, PyTorch 2.10+cu128\\n- 模型: /root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Llama-8B/\\n- Hidden states: artifacts/hidden_states/ (268 traces, 1.2GB)\\n- Checkpoints: artifacts/diagnostics/gru256_single_l14.pt, gru256_multi_7l.pt\\n\", \"total_chars\": 1909, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "231b7faa-d89c-4f66-8ba0-2911e1a62af4",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "0b073923-73c9-4998-b0e5-4c06ab67563e",
  "sourceToolAssistantUUID": "231b7faa-d89c-4f66-8ba0-2911e1a62af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T20:11:14.814Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TGXUDVLvKe6ZhVw5s5rjwh`</summary>

```json
{
  "pattern": "**/artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b073923-73c9-4998-b0e5-4c06ab67563e",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rcfCqqNw2BYyYEK8Em",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03533615-14f6-4a6d-94d8-1e9afd7c4a80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VaoXvA94aWRHh51yrovShH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 17304,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4289
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 17304,
          "cache_creation_input_tokens": 4289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4289,
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

_source line 18 · 2026-05-16T20:11:14.844Z_

<details><summary>↩ Tool result · `toolu_01TGXUDVLvKe6ZhVw5s5rjwh`</summary>

```text
artifacts/data_exploration_report.md
artifacts/commitment_point_analysis.md
artifacts/diag_d1_layer_sweep/report/d1_layer_sweep_results.md
artifacts/diag_d2_pca_viz/chart/d2_pca_viz_results.txt
artifacts/exp_gru256_multilayer/data/gru256_ablation.log
artifacts/manifest.yaml
artifacts/dream_reports/dream_20260516T194646/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260516T194646/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260516T194646/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260516T194646/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T194646/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T194646/best/experiment_data.json
artifacts/dream_reports/dream_20260516T194646/best/paper_framing.md
artifacts/dream_reports/dream_20260516T194646/best/custom.bib
artifacts/dream_reports/dream_20260516T194646/best/paper.tex
artifacts/dream_reports/dream_20260516T194646/best/paper.bbl
artifacts/dream_reports/dream_20260516T194646/best/paper.blg
artifacts/dream_reports/dream_20260516T194646/best/paper.aux
artifacts/dream_reports/dream_20260516T194646/best/paper.out
artifacts/dream_reports/dream_20260516T194646/best/paper.pdf
artifacts/dream_reports/dream_20260516T194646/best/paper.log
artifacts/dream_reports/dream_20260516T194646/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260516T194646/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T194646/median/experiment_data.json
artifacts/dream_reports/dream_20260516T194646/median/paper_framing.md
artifacts/dream_reports/dream_20260516T194646/median/paper.tex
artifacts/dream_reports/dream_20260516T194646/median/references.bib
artifacts/dream_reports/dream_20260516T194646/median/paper.bbl
artifacts/dream_reports/dream_20260516T194646/median/paper.blg
artifacts/dream_reports/dream_20260516T194646/median/paper.aux
artifacts/dream_reports/dream_20260516T194646/median/paper.out
artifacts/dream_reports/dream_20260516T194646/median/paper.pdf
artifacts/dream_reports/dream_20260516T194646/median/paper.log
artifacts/dream_reports/dream_20260516T194646/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260516T194646/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T194646/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T194646/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T194646/worst/paper.tex
artifacts/dream_reports/dream_20260516T194646/worst/paper.aux
artifacts/dream_reports/dream_20260516T194646/worst/paper.out
artifacts/dream_reports/dream_20260516T194646/worst/paper.pdf
artifacts/dream_reports/dream_20260516T194646/worst/paper.log
artifacts/dream_reports/dream_20260516T194646/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260516T194646/logs/orchestrator.log
artifacts/dream_reports/dream_20260516T194646/best/review_context.yaml
artifacts/dream_reports/dream_20260516T194646/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03533615-14f6-4a6d-94d8-1e9afd7c4a80",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "ac3da3ed-59a5-4077-bb4b-eb8a394c41f8",
  "sourceToolAssistantUUID": "03533615-14f6-4a6d-94d8-1e9afd7c4a80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T20:11:18.497Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WLCJLbp37JHGaPTjXjFtMg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac3da3ed-59a5-4077-bb4b-eb8a394c41f8",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rcwsCo3DEdGxQ1bfX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f22f2b63-c455-482b-b0d9-e0f9778a6d87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RXBS2YepCYujv2r7P5bycU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 21593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
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

_source line 20 · 2026-05-16T20:11:18.502Z_

<details><summary>↩ Tool result · `toolu_01WLCJLbp37JHGaPTjXjFtMg`</summary>

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
12	\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}
13	\usepackage{natbib}
14	\bibliographystyle{plainnat}
15	
16	\newcommand{\coverageup}[1]{\textcolor{green!60!black}{(+#1)}}
17	\newcommand{\coveragedown}[1]{\textcolor{red!70!black}{(#1)}}
18	
19	\title{Contrastive Trace Probing for Safety Commitment Detection\\in Reasoning Models: A Cross-Architecture Empirical Study}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	% ========================================================================
27	% ABSTRACT
28	% ========================================================================
29	\begin{abstract}
30	Reasoning models such as DeepSeek-R1 and QwQ exhibit \emph{self-jailbreak}: their extended chain-of-thought interleaves safety reasoning with harmful execution, culminating in a \emph{commitment point} where safety reasoning permanently ceases.
31	Existing hidden-state jailbreak detectors target adversarial inputs to instruction-tuned models and have never been evaluated on reasoning-model self-jailbreak.
32	We present the first cross-architecture empirical study of hidden-state safety monitoring in reasoning models, spanning four models across two architecture families (Llama-3.1 and Qwen2.5) and two scales (7--8B and 32B).
33	We establish three findings:
34	(1)~static per-step probes achieve $<$50\% detection coverage despite strong per-dimension safety signal (Fisher ratio $>$14), because the signal is distributed across minor principal components;
35	(2)~a simple temporal window logistic regression ($W$=15) achieves 76.7\% mean coverage---matching the label-oracle ceiling---with a +34.9pp improvement over static probes that is consistent across all architectures;
36	(3)~no hidden-state method achieves positive detection lead time (best: $-$0.2 steps vs.\ oracle +31 steps), establishing a principled limitation boundary.
37	Cross-architecture transfer via learned projection heads yields 64.5\% mean coverage without target-domain labels, suggesting safety commitment signals share geometric structure across model families.
38	\end{abstract}
39	
40	% ========================================================================
41	% 1. INTRODUCTION
42	% ========================================================================
43	\section{Introduction}
44	
45	Reasoning models---large language models trained with reinforcement learning to produce extended chains of thought (CoT)---represent a qualitative shift in how language models process complex queries \cite{deepseekr1,qwq32b}.
46	These models interleave multiple reasoning strategies across dozens to hundreds of steps, achieving strong performance on mathematical and scientific benchmarks.
47	However, recent work has identified a critical safety failure mode: \emph{self-jailbreak}, where the model's own reasoning process gradually transitions from safety-aligned analysis to harmful content generation \cite{harmthoughts,selfjailbreaking}.
48	
49	Unlike conventional jailbreak attacks that rely on adversarial inputs, self-jailbreak emerges from the model's internal reasoning dynamics.
50	In 84\% of harmful traces, safety-relevant reasoning persists well past step 10, only to permanently cease at a \emph{commitment point}---the reasoning step after which no further safety considerations appear.
51	Detecting this commitment point is critical for deploying safety monitors on reasoning models.
52	
53	Existing hidden-state jailbreak detectors such as TrajGuard \cite{trajguard}, SafeSwitch \cite{safeswitch}, and SIREN \cite{siren} achieve strong defense rates ($>$95\%) on instruction-tuned models.
54	However, they operate at token-level granularity on models where the attack is an adversarial \emph{input}.
55	Reasoning-model self-jailbreak is fundamentally different: the attack is the model's \emph{own reasoning process}, distributed across many CoT steps.
56	No prior work bridges hidden-state detection methods to reasoning-model self-jailbreak.
57	
58	We present the first systematic cross-architecture evaluation of hidden-state methods for safety commitment detection in reasoning models.
59	Our study spans four models---DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-32B, QwQ-32B, and OpenThinker-7B---covering two architecture families (Llama-3.1 and Qwen2.5) and two scales (7--8B and 32B).
60	We establish three claims:
61	
62	\paragraph{Claim 1: Static probes fail reliably.} Per-step logistic regression achieves $<$50\% detection coverage across all models (mean 41.9\%), despite Fisher discriminant ratios $>$14 in full representation space.  The safety signal exists but concentrates in minor principal components (top-3 PCs explain $<$17\% of variance), causing both static classifiers and geometric detectors (Mahalanobis distance) to fail.
63	
64	\paragraph{Claim 2: Temporal window probes saturate oracle coverage.} A temporal window logistic regression with $W$=15 achieves 76.7\% mean coverage across architectures, matching the label-oracle upper bound.  The +30--35pp improvement is consistent across all four models and both architecture families.  Window size $W$=15 is universally optimal, requiring no architecture-specific tuning.
65	
66	\paragraph{Claim 3: Pre-textual detection is fundamentally limited.} No hidden-state method achieves positive mean lead time. The oracle's +31-step advantage derives from directly observing label-sequence autocorrelation---information that hidden states encode for the current step but not for future trajectory.  This establishes a principled boundary: hidden-state monitors can detect commitment \emph{at} or \emph{after} it occurs, but not before.
67	
68	% ========================================================================
69	% 2. RELATED WORK
70	% ========================================================================
71	\section{Related Work}
72	
73	\paragraph{Hidden-state jailbreak detection.}
74	TrajGuard \cite{trajguard} monitors activation trajectories using Mahalanobis distance from safe-trace distributions, achieving 95\% defense rate on instruction-tuned models.
75	SafeSwitch \cite{safeswitch} trains linear probes on intermediate representations to classify safety-relevant states.
76	SIREN \cite{siren} uses contrastive features between safe and unsafe hidden states for real-time detection.
77	All three operate at token-level granularity on models where the adversarial signal is in the \emph{input}---none have been evaluated on reasoning-model self-jailbreak where the signal is in the model's own multi-step reasoning.
78	
79	\paragraph{Reasoning model safety.}
80	\citet{selfjailbreaking} demonstrate that reasoning models can jailbreak themselves through extended CoT, bypassing safety training without adversarial input.
81	\citet{harmthoughts} provide the HarmThoughts dataset with fine-grained step-level safety annotations across a 16-label taxonomy, enabling quantitative analysis of safety reasoning dynamics.
82	SafeRemind \cite{saferemind} and SafeThink \cite{safethink} propose text-level CoT monitoring but are vulnerable to pathological reasoning chains.
83	None of these works evaluate hidden-state detection methods.
84	
85	\paragraph{Linear probing of LLM representations.}
86	Linear probes have been widely used to study what information LLM hidden states encode \cite{belinkov2022probing}, including truthfulness \cite{li2024inference}, sentiment \cite{tigges2023linear}, and factual knowledge \cite{meng2022locating}.
87	Our work extends this methodology to temporal probe designs that capture multi-step patterns in reasoning traces.
88	
89	% ========================================================================
90	% 3. METHOD
91	% ========================================================================
92	\section{Method}
93	
94	\subsection{Task Definition}
95	
96	Given a reasoning trace $\mathbf{x} = (x_1, \ldots, x_T)$ where each $x_t$ is a reasoning step, we define the \emph{commitment point} $c$ as the last step containing safety-relevant reasoning.
97	The detection task is binary classification: for each step $t$, predict whether $t > c$ (the model has committed to harmful output).
98	
99	\subsection{Hidden-State Extraction}
100	
101	For each reasoning step $x_t$, we extract the hidden-state vector $\mathbf{h}_t^{(\ell)} \in \mathbb{R}^d$ at layer $\ell$ from the last token position of that step.
102	Based on layer ablation (Section~\ref{sec:layer_ablation}), we use the optimal middle-layer representation at approximately 35--44\% relative depth.
103	
104	\subsection{Static Probe}
105	
106	The static probe is a logistic regression classifier trained on individual hidden states:
107	\begin{equation}
108	    p(y_t = 1 \mid \mathbf{h}_t) = \sigma(\mathbf{w}^\top \mathbf{h}_t + b)
109	\end{equation}
110	This represents the standard approach used by existing hidden-state detectors adapted to step-level granularity.
111	
112	\subsection{Temporal Window Probe}
113	
114	The temporal window probe concatenates hidden states from a window of $W$ consecutive steps:
115	\begin{equation}
116	    \mathbf{z}_t = [\mathbf{h}_{t-W+1}; \ldots; \mathbf{h}_t] \in \mathbb{R}^{Wd}
117	\end{equation}
118	\begin{equation}
119	    p(y_t = 1 \mid \mathbf{z}_t) = \sigma(\mathbf{w}^\top \mathbf{z}_t + b)
120	\end{equation}
121	This enables the probe to capture \emph{safety reasoning density decline}---the gradual decrease in safety-labeled steps within the window as the model approaches commitment.
122	
123	\subsection{Mahalanobis Distance Baseline}
124	
125	Following TrajGuard's approach, we estimate the covariance $\mathbf{\Sigma}$ of hidden states from safe traces and compute per-step Mahalanobis distance:
126	\begin{equation}
127	    d_M(\mathbf{h}_t) = \sqrt{(\mathbf{h}_t - \boldsymbol{\mu})^\top \mathbf{\Sigma}^{-1} (\mathbf{h}_t - \boldsymbol{\mu})}
128	\end{equation}
129	A threshold on $d_M$ classifies steps as committed.
130	
131	\subsection{GRU Sequential Probe}
132	
133	As an upper bound on temporal modeling capacity, we train a GRU with 256 hidden units that processes the full sequence of hidden states:
134	\begin{equation}
135	    \mathbf{g}_t = \text{GRU}(\mathbf{h}_1, \ldots, \mathbf{h}_t; \theta) \in \mathbb{R}^{256}
136	\end{equation}
137	\begin{equation}
138	    p(y_t = 1 \mid \mathbf{g}_t) = \sigma(\mathbf{v}^\top \mathbf{g}_t + b)
139	\end{equation}
140	
141	\subsection{Label-Sequence Oracle}
142	
143	The oracle directly observes the binary label sequence and fires when $K=5$ consecutive steps lack safety labels.
144	It serves as an upper bound on detection \emph{coverage} (what fraction of commitment points are detected) while providing a reference for \emph{lead time} (how many steps before textual commitment the detection occurs).
145	
146	\subsection{Cross-Architecture Transfer}
147	
148	To evaluate whether safety commitment signals share geometric structure across architectures, we train a linear projection head $\mathbf{P} \in \mathbb{R}^{d_{\text{target}} \times d_{\text{source}}}$ that maps hidden states from a source model's space to a target model's space, using 30 aligned traces for projection training.
149	The source model's trained probe is then applied to projected target-model representations.
150	
151	\subsection{Evaluation Metrics}
152	
153	\begin{itemize}
154	    \item \textbf{Coverage}: Fraction of traces where the probe detects commitment (true positive rate at trace level).
155	    \item \textbf{Per-step accuracy}: Step-level classification accuracy.
156	    \item \textbf{Lead time}: Number of steps between probe detection and textual commitment point (positive = early detection).
157	\end{itemize}
158	
159	% ========================================================================
160	% 4. EXPERIMENTAL SETUP
161	% ========================================================================
162	\section{Experimental Setup}
163	
164	\paragraph{Models.} We evaluate four reasoning models spanning two architecture families and two scales: DeepSeek-R1-Distill-Llama-8B (Llama-3.1, $d$=4096, 32 layers), DeepSeek-R1-Distill-Qwen-32B (Qwen2.5, $d$=5120, 64 layers), QwQ-32B (Qwen2.5, $d$=5120, 64 layers), and OpenThinker-7B (Qwen2.5, $d$=3584, 32 layers).
165	
166	\paragraph{Dataset.} We use HarmThoughts reasoning traces with step-level safety annotations from a 16-label taxonomy, binarized to safety-relevant vs.\ not.
167	The dataset contains 209 traces, split into train/test with stratification.
168	
169	\paragraph{Layer selection.} For each model, we select the optimal layer via held-out validation.
170	Optimal layers fall at 34--44\% relative depth across all models (Section~\ref{sec:layer_ablation}).
171	
172	% ========================================================================
173	% 5. RESULTS
174	% ========================================================================
175	\section{Results}
176	
177	\subsection{Claim 1: Static Probes Fail Across Architectures}
178	
179	Table~\ref{tab:static} reports static probe performance across all models.
180	Despite per-step accuracies above 80\% (inflated by majority-class bias), detection coverage remains below 50\% for every model.
181	Fisher discriminant ratios in original representation space exceed 14 across architectures, confirming that safety-relevant signal \emph{exists} in hidden states.
182	However, PCA analysis reveals this signal is distributed across minor principal components: top-3 PCs explain only 12.8--16.6\% of variance, and Fisher ratio collapses from $>$14 to $<$1 after PCA-3 projection.
183	
184	\begin{table}[t]
185	\centering
186	\small
187	\begin{tabular}{lcccccc}
188	\toprule
189	\textbf{Model} & \textbf{Arch} & $d$ & \textbf{Acc} & \textbf{Cov} & \textbf{Fisher} & \textbf{F(PCA-3)} \\
190	\midrule
191	r1-8b & Llama & 4096 & .817 & .465 & 17.9 & 0.93 \\
192	r1-32b & Qwen & 5120 & .824 & .442 & 17.1 & 0.87 \\
193	QwQ-32B & Qwen & 5120 & .809 & .395 & 15.6 & 0.72 \\
194	OT-7B & Qwen & 3584 & --- & .419 & 13.2 & 0.68 \\
195	\midrule
196	\multicolumn{3}{l}{\textit{Mean}} & .817 & .430 & 15.9 & 0.80 \\
197	\bottomrule
198	\end{tabular}
199	\caption{Static probe performance across architectures.  Coverage is below 50\% for all models despite high Fisher discriminant ratios in original space.  Fisher(PCA-3) collapses to $<$1, confirming signal concentration in minor PCs.}
200	\label{tab:static}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f22f2b63-c455-482b-b0d9-e0f9778a6d87",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "c9346f74-d35c-4ce7-b207-86f1d3950dbc",
  "sourceToolAssistantUUID": "f22f2b63-c455-482b-b0d9-e0f9778a6d87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T20:11:18.969Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VSsv87LPad5nzWF5sGLdt9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9346f74-d35c-4ce7-b207-86f1d3950dbc",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rcwsCo3DEdGxQ1bfX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0d29d60-16f1-414a-9358-9b876e832064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RXBS2YepCYujv2r7P5bycU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 21593,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
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

_source line 22 · 2026-05-16T20:11:19.221Z_

<details><summary>↩ Tool result · `toolu_01VSsv87LPad5nzWF5sGLdt9`</summary>

```text
1	tier: best
2	narrative_guidance: Original 3-claim structure holds at full strength. Frame as first
3	  cross-architecture empirical study establishing universal properties of hidden-state
4	  safety monitoring in reasoning models. Method simplicity is the finding (reviewer
5	  concern 1 preempted). Negative lead time is a principled boundary result. EMNLP
6	  Main with high confidence.
7	imagined_experiments:
8	- name: Cross-architecture static probe evaluation
9	  plan_id: exp-001
10	  description: Train static LR on r1-32b and QwQ-32B hidden states, measure per-step
11	    classification accuracy and detection coverage.
12	  expected_results:
13	    r1_32b_static_acc: 0.8243
14	    r1_32b_static_coverage: 0.4419
15	    r1_32b_fisher_orig_L14: 16.3
16	    r1_32b_fisher_orig_L20: 17.1
17	    r1_32b_fisher_pca3_L14: 0.87
18	    r1_32b_var_explained_3pc: 0.142
19	    qwq_32b_static_acc: 0.8091
20	    qwq_32b_static_coverage: 0.3953
21	    qwq_32b_fisher_orig_L14: 14.8
22	    qwq_32b_fisher_orig_L20: 15.6
23	    qwq_32b_fisher_pca3_L14: 0.72
24	    qwq_32b_var_explained_3pc: 0.128
25	    mean_cross_arch_static_coverage: 0.4186
26	  result_rationale: Qwen2.5 架构使用 GQA 且 hidden dimension 为 5120（vs Llama-3.1 的 4096），导致
27	    safety signal 分布在更多维度上。Fisher 判别比在原始空间仍然很高（14-17），证明 safety signal 存在但同样集中在 minor
28	    PCs——PCA top-3 解释方差更低（12-14% vs 16.6%），因为 5120 维空间中信号散布更广。静态 LR 仍能达到 ~81% accuracy（因为
29	    majority class baseline 高），但 coverage 低于 50% 因为单步分类无法捕捉 safety reasoning density
30	    decline 的渐变模式。QwQ-32B 略低于 r1-32b 因为其推理链更长更多样，commitment boundary 更模糊。
31	  tables:
32	  - caption: 'Table 3: Static probe performance across architectures'
33	    columns:
34	    - Model
35	    - Base Arch
36	    - Hidden Dim
37	    - Static Acc
38	    - Static Coverage
39	    - Fisher (orig)
40	    - Fisher (PCA-3)
41	    - Var Explained (3PC)
42	    rows:
43	    - - r1-8b
44	      - Llama-3.1
45	      - 4096
46	      - 0.8172
47	      - 0.4651
48	      - 17.88
49	      - 0.928
50	      - 0.166
51	    - - r1-32b
52	      - Qwen2.5
53	      - 5120
54	      - 0.8243
55	      - 0.4419
56	      - 17.1
57	      - 0.87
58	      - 0.142
59	    - - QwQ-32B
60	      - Qwen2.5
61	      - 5120
62	      - 0.8091
63	      - 0.3953
64	      - 15.6
65	      - 0.72
66	      - 0.128
67	  figures_description:
68	  - 'Figure 4: Fisher discriminant ratio vs PCA dimensionality for all 3 models. Shows
69	    consistent collapse from 15-18 (full space) to <1.5 (PCA-3) across architectures,
70	    confirming signal-in-minor-PCs is universal.'
71	  - 'Figure 5: PCA-3D scatter of safe vs unsafe steps for r1-32b and QwQ-32B (analogous
72	    to Figure 2 from r1-8b). Both show overlapping clusters confirming geometric separation
73	    fails in low-D projection.'
74	  analysis: 'Static probe failure replicates perfectly: all models show coverage <50%
75	    despite high-dimensional Fisher ratios >14. The pattern is architecture-independent
76	    — safety signal exists in hidden states but is distributed across minor principal
77	    components in both Llama and Qwen2.5 backbones. This directly validates Claim
78	    1 as an architectural universal.'
79	- name: Cross-architecture temporal window evaluation
80	  plan_id: exp-002
81	  description: Train temporal LR W=15 on r1-32b and QwQ-32B. Validate +25-35pp coverage
82	    improvement holds cross-architecture.
83	  expected_results:
84	    r1_32b_temporal_w15_acc: 0.8512
85	    r1_32b_temporal_w15_coverage: 0.7907
86	    r1_32b_temporal_minus_static_delta: 0.3488
87	    r1_32b_temporal_w15_lead_mean: -1.32
88	    qwq_32b_temporal_w15_acc: 0.8389
89	    qwq_32b_temporal_w15_coverage: 0.7442
90	    qwq_32b_temporal_minus_static_delta: 0.3489
91	    qwq_32b_temporal_w15_lead_mean: -0.87
92	    mean_cross_arch_temporal_coverage: 0.7674
93	    mean_cross_arch_delta: 0.3489
94	  result_rationale: Temporal window 捕捉的是 safety reasoning density decline 模式——连续 15
95	    步内 safety-labeled 步骤的密度从高到低的趋势。这个模式是推理模型 self-jailbreak 的固有特征：模型先进行 safety reasoning，然后逐渐过渡到
96	    harmful execution。无论底层架构是 Llama 还是 Qwen2.5，这个 behavioral pattern 都会被 encoded 进
97	    hidden states 的时序轨迹中。r1-32b 略高于 QwQ 因为 DeepSeek 蒸馏对齐更干净，commitment boundary 更
98	    sharp；QwQ 的推理链更长更弯曲但仍然满足 saturation。Delta 在两个模型上都 ~35pp 因为 static baseline 和 temporal
99	    ceiling 的 gap 反映的是同一个结构性限制。
100	  tables:
101	  - caption: 'Table 4: Temporal window probe performance across architectures'
102	    columns:
103	    - Model
104	    - Static Cov
105	    - Temporal W15 Cov
106	    - Delta
107	    - Temporal Acc
108	    - Lead Time (mean)
109	    rows:
110	    - - r1-8b
111	      - 0.4651
112	      - 0.7674
113	      - +30.2pp
114	      - 0.8478
115	      - -1.09
116	    - - r1-32b
117	      - 0.4419
118	      - 0.7907
119	      - +34.9pp
120	      - 0.8512
121	      - -1.32
122	    - - QwQ-32B
123	      - 0.3953
124	      - 0.7442
125	      - +34.9pp
126	      - 0.8389
127	      - -0.87
128	  figures_description:
129	  - 'Figure 6: Coverage vs window size W for all 3 models (W=1,5,10,15,20). Shows
130	    consistent saturation at W≈15 across architectures, with diminishing returns beyond.'
131	  - 'Figure 7: Per-trace detection timeline comparison (static vs temporal W=15) on
132	    representative QwQ-32B traces. Shows temporal probe crossing commitment boundary
133	    while static probe misses.'
134	  analysis: Temporal advantage replicates with even larger delta on Qwen2.5 models
135	    (+34.9pp vs +30.2pp on r1-8b). This is because Qwen2.5-based models have slightly
136	    lower static baselines (due to more distributed signal) but temporal probes still
137	    saturate near oracle ceiling. The consistency of saturation at W=15 across architectures
138	    confirms that safety reasoning density decline operates at a universal timescale
139	    (~15 reasoning steps). Claim 2 is fully validated cross-architecture.
140	- name: Cross-model transfer with projection head
141	  plan_id: exp-003
142	  description: Train probe on r1-8b (Llama, 4096-dim), test on r1-32b/QwQ (Qwen2.5,
143	    5120-dim) via learned linear projection. Bidirectional transfer.
144	  expected_results:
145	    llama_to_qwen_r1_32b_coverage: 0.6279
146	    llama_to_qwen_qwq_coverage: 0.5814
147	    qwen_to_llama_r1_8b_coverage: 0.6512
148	    qwen_r1_32b_to_qwq_coverage: 0.7209
149	    mean_cross_transfer_coverage: 0.6454
150	    projection_head_params: 20971520
151	    projection_training_traces: 30
152	  result_rationale: Cross-transfer 成功（coverage 0.55-0.72）因为 safety signal 的时序结构是 universal
153	    的——density decline pattern 在投影后仍可识别。Llama→Qwen 方向略低于 Qwen→Llama 因为 4096→5120 投影是升维（信息无损），而
154	    5120→4096 是降维但 safety signal 主要在 minor PCs 所以投影头学到了保留关键维度。同族模型间转移（r1-32b→QwQ，都是
155	    Qwen2.5）效果最好（0.72）因为不需要跨架构投影，只需对齐同架构的不同微调变体。Zero-shot 不达到 in-distribution 水平（0.77）是因为不同模型的
156	    commitment 边界位置和 hidden state 表征存在分布偏移，但 >55% 证明 safety monitoring 有跨架构泛化潜力。
157	  tables:
158	  - caption: 'Table 5: Cross-architecture transfer matrix (temporal W=15 coverage)'
159	    columns:
160	    - Train →
161	    - 'Test: r1-8b'
162	    - 'Test: r1-32b'
163	    - 'Test: QwQ-32B'
164	    rows:
165	    - - r1-8b (Llama)
166	      - 0.767 (in-dist)
167	      - '0.628'
168	      - '0.581'
169	    - - r1-32b (Qwen2.5)
170	      - '0.651'
171	      - 0.791 (in-dist)
172	      - '0.721'
173	    - - QwQ-32B (Qwen2.5)
174	      - '0.605'
175	      - '0.698'
176	      - 0.744 (in-dist)
177	  figures_description:
178	  - 'Figure 8: Transfer matrix heatmap showing coverage degradation from in-distribution
179	    (diagonal) to cross-architecture (off-diagonal). Intra-family transfer (Qwen↔Qwen)
180	    degrades less than cross-family (Llama↔Qwen).'
181	  analysis: Non-trivial cross-architecture transfer (mean 0.645) demonstrates that
182	    safety commitment signal has a shared geometric structure across model families.
183	    The projection head successfully maps between representation spaces while preserving
184	    the temporal density decline pattern. This is the strongest evidence for 'architectural
185	    universal' framing — a probe trained on one model family can monitor another with
186	    >55% coverage without any target-domain labels.
187	- name: Lead time analysis across architectures
188	  plan_id: exp-004
189	  description: Measure detection lead time (steps before/after textual commitment
190	    point) for all methods on r1-32b and QwQ-32B.
191	  expected_results:
192	    r1_32b_static_lead_mean: -2.8
193	    r1_32b_static_lead_median: -3
194	    r1_32b_temporal_w15_lead_mean: -1.32
195	    r1_32b_temporal_w15_lead_median: -1
196	    r1_32b_gru_lead_mean: -0.9
197	    r1_32b_positive_lead_rate: 0.29
198	    qwq_32b_static_lead_mean: -1.9
199	    qwq_32b_static_lead_median: -2
200	    qwq_32b_temporal_w15_lead_mean: -0.87
201	    qwq_32b_temporal_w15_lead_median: -1
202	    qwq_32b_gru_lead_mean: -0.5
203	    qwq_32b_positive_lead_rate: 0.33
204	    all_models_max_lead_mean: -0.2
205	    oracle_lead_mean: 31
206	  result_rationale: Negative lead time 在所有模型上持续出现因为这反映了一个根本性限制：hidden states encode
207	    当前 safety state 而非未来 safety trajectory。模型在 commitment point 处才在 hidden space 中完成从
208	    safety→unsafe 的转变——这个转变是 concurrent with（而非 prior to）文本层面的 commitment。Oracle 能提前
209	    31 步检测是因为它直接观察 label sequence 中的 density decline pattern（这是定义层面的优势，不依赖 hidden
210	    representation）。QwQ 的 lead time 略好于 r1-32b（-0.87 vs -1.32）因为 QwQ 的推理链更长，commitment
211	    boundary 更 gradual，给 temporal probe 更多 context 来识别过渡区。但无论哪个模型，mean lead time 都不超过
212	    0，确认 pre-textual detection limitation 是 fundamental 的。
213	  tables:
214	  - caption: 'Table 6: Detection lead time across architectures (steps relative to
215	      commitment point)'
216	    columns:
217	    - Model
218	    - Method
219	    - Lead Mean
220	    - Lead Median
221	    - Positive Lead %
222	    - Coverage
223	    rows:
224	    - - r1-8b
225	      - Static LR
226	      - -2.0
227	      - -2
228	      - 30%
229	      - 0.465
230	    - - r1-8b
231	      - Temporal W15
232	      - -1.09
233	      - -1
234	      - 34%
235	      - 0.767
236	    - - r1-8b
237	      - GRU
238	      - -0.21
239	      - -1
240	      - 34.5%
241	      - 0.674
242	    - - r1-32b
243	      - Static LR
244	      - -2.8
245	      - -3
246	      - 25%
247	      - 0.442
248	    - - r1-32b
249	      - Temporal W15
250	      - -1.32
251	      - -1
252	      - 29%
253	      - 0.791
254	    - - r1-32b
255	      - GRU
256	      - -0.9
257	      - -1
258	      - 29%
259	      - 0.721
260	    - - QwQ-32B
261	      - Static LR
262	      - -1.9
263	      - -2
264	      - 28%
265	      - 0.395
266	    - - QwQ-32B
267	      - Temporal W15
268	      - -0.87
269	      - -1
270	      - 33%
271	      - 0.744
272	    - - QwQ-32B
273	      - GRU
274	      - -0.5
275	      - 0
276	      - 33%
277	      - 0.698
278	    - - All
279	      - Oracle (K=5)
280	      - 31
281	      - 29
282	      - 100%
283	      - 1.0
284	  figures_description:
285	  - 'Figure 9: Lead time distribution (violin plot) across 3 models × 3 methods. All
286	    method distributions centered at or below 0; oracle distribution centered at +31.
287	    Clear separation between hidden-state methods and label-oracle.'
288	  - 'Figure 10: Lead time vs coverage scatter for all model×method combinations. Shows
289	    Pareto frontier: higher coverage methods have slightly less negative lead time,
290	    but none cross zero mean.'
291	  analysis: 'Negative lead time is confirmed as architecture-independent. The gap
292	    between oracle (+31 steps) and best hidden-state method (≈-0.5 steps) is >30 steps
293	    across all models. This ''lead time wall'' at zero confirms Claim 3: hidden states
294	    encode current safety commitment state but not future trajectory. The finding
295	    is now established on both Llama-3.1 and Qwen2.5 architectures, ruling out model-specific
296	    artifact explanations.'
297	- name: TrajGuard-style Mahalanobis distance baseline
298	  plan_id: exp-005
299	  description: Estimate safe-trace covariance, compute Mahalanobis distance per step
300	    on all models. Evaluate as anomaly detector for commitment point.
301	  expected_results:
302	    r1_8b_mahalanobis_coverage: 0.3256
303	    r1_8b_mahalanobis_auroc: 0.612
304	    r1_32b_mahalanobis_coverage: 0.2791
305	    r1_32b_mahalanobis_auroc: 0.583
306	    qwq_32b_mahalanobis_coverage: 0.2326
307	    qwq_32b_mahalanobis_auroc: 0.561
308	    mean_mahalanobis_coverage: 0.2791
309	    mahalanobis_vs_temporal_gap: -0.488
310	  result_rationale: Mahalanobis distance 失败因为它本质上依赖 covariance structure（等价于所有 PCs
311	    的加权距离），而 safety signal 集中在 minor PCs（解释 <17% variance）。在 full-dimensional MD 中，major
312	    PCs 主导距离计算——一个步骤在 top PCs 上的偏移（反映 topic/position/syntax 变化）远大于 minor PCs 上的 safety
313	    signal 偏移。这导致 false positives（topic shift 被标记为 anomaly）和 false negatives（真正的 safety
314	    transition 在 minor PCs 上太弱）。32B 模型更差因为 5120 维空间中 minor PCs 的相对贡献更小。这直接类比了 TrajGuard
315	    在标准 LLM 上成功但在 reasoning model 上失败的原因：reasoning model 的 safety signal 不在 geometric
316	    outlier direction 上。
317	  tables:
318	  - caption: 'Table 7: Mahalanobis distance baseline vs temporal probe'
319	    columns:
320	    - Model
321	    - MD Coverage
322	    - MD AUROC
323	    - Temporal W15 Cov
324	    - Gap
325	    rows:
326	    - - r1-8b
327	      - 0.326
328	      - 0.612
329	      - 0.767
330	      - -44.1pp
331	    - - r1-32b
332	      - 0.279
333	      - 0.583
334	      - 0.791
335	      - -51.2pp
336	    - - QwQ-32B
337	      - 0.233
338	      - 0.561
339	      - 0.744
340	      - -51.1pp
341	  figures_description:
342	  - 'Figure 11: ROC curves for Mahalanobis distance vs temporal LR on all 3 models.
343	    MD curves barely above diagonal, temporal LR curves in upper-left region.'
344	  - 'Figure 12: Mahalanobis distance time series on example traces. Shows MD fluctuates
345	    with topic changes but doesn''t spike at commitment point, confirming geometric
346	    methods fail when signal is in minor PCs.'
347	  analysis: 'Mahalanobis baseline coverage (23-33%) is substantially below even static
348	    LR (40-47%), confirming that TrajGuard-style geometric anomaly detection is fundamentally
349	    unsuited for reasoning-model safety monitoring. The failure mode is precise and
350	    interpretable: safety signal lives in minor PCs that contribute negligibly to
351	    Mahalanobis distance. This preempts reviewer concern about comparison to existing
352	    detectors — they fail for principled geometric reasons, not implementation issues.'
353	- name: Bootstrap confidence intervals
354	  plan_id: exp-006
355	  description: 1000 bootstrap resamples on all key metrics for all methods × models.
356	    Report 95% CIs.
357	  expected_results:
358	    r1_8b_temporal_coverage_ci:
359	    - 0.674
360	    - 0.86
361	    r1_32b_temporal_coverage_ci:
362	    - 0.698
363	    - 0.884
364	    qwq_32b_temporal_coverage_ci:
365	    - 0.651
366	    - 0.837
367	    r1_8b_static_coverage_ci:
368	    - 0.349
369	    - 0.581
370	    r1_32b_static_coverage_ci:
371	    - 0.326
372	    - 0.558
373	    cross_transfer_mean_ci:
374	    - 0.558
375	    - 0.733
376	    lead_time_r1_8b_ci:
377	    - -2.8
378	    - 0.6
379	    lead_time_r1_32b_ci:
380	    - -3.1
381	    - 0.5
382	    delta_temporal_minus_static_ci:
383	    - 0.186
384	    - 0.512
385	    all_deltas_exclude_zero: true
386	  result_rationale: Bootstrap CIs 较宽（±9-12pp）因为测试集只有 43 traces（r1-8b）和类似规模的 32B test
387	    sets。但关键比较（temporal vs static delta）的 CI 不包含 0，因为 +30pp 的效应量远大于采样噪声。Coverage CI
388	    上界不超过 oracle ceiling（76.7%的中心点 + ~9pp = ~86% upper bound，仍合理）。Lead time CI 包含少量正值（upper
389	    bound ~0.5）反映了个别 traces 的 positive lead，但均值 CI 中心始终为负。209 traces 的限制是真实的——CIs
390	    acknowledge this honestly——但效应量足够大使得所有核心 claims 在 p<0.05 下显著。
391	  tables:
392	  - caption: 'Table 8: Bootstrap 95% confidence intervals for key metrics'
393	    columns:
394	    - Metric
395	    - r1-8b
396	    - r1-32b
397	    - QwQ-32B
398	    rows:
399	    - - Static Coverage
400	      - '[0.349, 0.581]'
401	      - '[0.326, 0.558]'
402	      - '[0.279, 0.512]'
403	    - - Temporal W15 Coverage
404	      - '[0.674, 0.860]'
405	      - '[0.698, 0.884]'
406	      - '[0.651, 0.837]'
407	    - - Delta (Temp-Static)
408	      - '[0.209, 0.488]'
409	      - '[0.233, 0.512]'
410	      - '[0.233, 0.512]'
411	    - - Lead Time (mean)
412	      - '[-2.8, 0.6]'
413	      - '[-3.1, 0.5]'
414	      - '[-2.3, 0.7]'
415	    - - Cross-transfer Cov
416	      - '[0.558, 0.733]'
417	      - —
418	      - —
419	  figures_description:
420	  - 'Figure 13: Forest plot of coverage estimates with 95% bootstrap CIs. Static and
421	    temporal CI ranges do not overlap for any model, confirming significant separation.'
422	  analysis: All core claims survive bootstrap validation. Temporal > static delta
423	    CIs exclude zero (minimum lower bound +18.6pp). Lead time CIs are centered negative
424	    with upper bounds near zero but never significantly positive. The wide CIs are
425	    an honest reflection of sample size — acknowledged in limitations but don't threaten
426	    claims because effect sizes are large relative to uncertainty.
427	- name: Window size ablation across architectures
428	  plan_id: exp-007
429	  description: Temporal LR with W=1,3,5,10,15,20,25 on all 3 models.
430	  expected_results:
431	    r1_8b_w1: 0.465
432	    r1_8b_w3: 0.535
433	    r1_8b_w5: 0.651
434	    r1_8b_w10: 0.651
435	    r1_8b_w15: 0.767
436	    r1_8b_w20: 0.767
437	    r1_8b_w25: 0.744
438	    r1_32b_w1: 0.442
439	    r1_32b_w5: 0.628
440	    r1_32b_w10: 0.698
441	    r1_32b_w15: 0.791
442	    r1_32b_w20: 0.791
443	    r1_32b_w25: 0.767
444	    qwq_32b_w1: 0.395
445	    qwq_32b_w5: 0.581
446	    qwq_32b_w10: 0.651
447	    qwq_32b_w15: 0.744
448	    qwq_32b_w20: 0.744
449	    qwq_32b_w25: 0.721
450	    optimal_w_all_models: 15
451	  result_rationale: W=15 是所有模型的饱和点因为 safety reasoning density decline 的时间尺度是 ~15 步——这反映了推理模型从
452	    safety reasoning 到 harmful execution 过渡的典型长度。W<15 时 probe 看不到完整的 decline pattern（只看到局部），W>15
453	    时额外 context 引入噪声（更早的步骤与 commitment 无关）且增加过拟合风险（特征维度 = W × hidden_dim 在小数据集上）。W=25
454	    时 coverage 轻微下降（-2-3pp）证实了过拟合假说。三个模型在同一 W 饱和证明这个时间尺度是 behavioral universal，不依赖架构。
455	  tables:
456	  - caption: 'Table 9: Coverage vs window size across architectures'
457	    columns:
458	    - W
459	    - r1-8b
460	    - r1-32b
461	    - QwQ-32B
462	    - Mean
463	    rows:
464	    - - 1
465	      - 0.465
466	      - 0.442
467	      - 0.395
468	      - 0.434
469	    - - 3
470	      - 0.535
471	      - 0.512
472	      - 0.465
473	      - 0.504
474	    - - 5
475	      - 0.651
476	      - 0.628
477	      - 0.581
478	      - 0.62
479	    - - 10
480	      - 0.651
481	      - 0.698
482	      - 0.651
483	      - 0.667
484	    - - 15
485	      - 0.767
486	      - 0.791
487	      - 0.744
488	      - 0.767
489	    - - 20
490	      - 0.767
491	      - 0.791
492	      - 0.744
493	      - 0.767
494	    - - 25
495	      - 0.744
496	      - 0.767
497	      - 0.721
498	      - 0.744
499	  figures_description:
500	  - 'Figure 14: Coverage vs window size curve for all 3 models. Shows consistent saturation
501	    at W=15 with slight decline at W=25. All curves have same shape shifted vertically.'
502	  analysis: Universal saturation at W=15 across architectures is a key finding supporting
503	    the 'method simplicity' narrative. The window size doesn't need architecture-specific
504	    tuning — the optimal temporal context is determined by the behavioral phenomenon
505	    (safety reasoning decline duration), not the model's internal representation.
506	    This directly preempts reviewer concern about hyperparameter sensitivity.
507	- name: Layer selection ablation on 32B models
508	  plan_id: exp-008
509	  description: Evaluate temporal probe at all layers (not just layer 14) on r1-32b
510	    and QwQ-32B to confirm middle-layer optimality generalizes.
511	  expected_results:
512	    r1_32b_best_layer: 22
513	    r1_32b_best_layer_coverage: 0.814
514	    r1_32b_layer_14_coverage: 0.721
515	    r1_32b_layer_range_good: 18-26
516	    qwq_32b_best_layer: 24
517	    qwq_32b_best_layer_coverage: 0.791
518	    qwq_32b_layer_14_coverage: 0.698
519	    qwq_32b_layer_range_good: 20-28
520	    relative_best_layer_r1_32b: 34% depth (layer 22/64)
521	    relative_best_layer_qwq_32b: 37% depth (layer 24/64)
522	    relative_best_layer_r1_8b: 44% depth (layer 14/32)
523	  result_rationale: 32B 模型有 64 层（vs r1-8b 的 32 层），最佳层在相对深度 34-37% 处（layer 22-24/64），与
524	    r1-8b 的 44%（layer 14/32）一致——都在 middle layers。Middle layers 最优因为：early layers encode
525	    低级语法特征（与 safety 无关），deep layers encode 高度 task-specific 的输出特征（过于细粒度）。Middle layers
526	    恰好在抽象 semantic level 上 encode safety reasoning state。绝对层数不同但相对位置一致证明这是 transformer
527	    depth-dependent 的 universal 现象。报告中使用 per-model best layer 结果，同时证明 default 中间层选择是
528	    robust 的 heuristic。
529	  tables:
530	  - caption: 'Table 10: Layer ablation (temporal W=15 coverage by layer)'
531	    columns:
532	    - Relative Depth
533	    - r1-8b (L/32)
534	    - r1-32b (L/64)
535	    - QwQ-32B (L/64)
536	    rows:
537	    - - 10%
538	      - 0.442 (L3)
539	      - 0.395 (L6)
540	      - 0.372 (L6)
541	    - - 25%
542	      - 0.605 (L8)
543	      - 0.581 (L16)
544	      - 0.558 (L16)
545	    - - 35%
546	      - 0.721 (L11)
547	      - 0.814 (L22)
548	      - 0.744 (L22)
549	    - - 44%
550	      - 0.767 (L14)
551	      - 0.791 (L28)
552	      - 0.791 (L28)
553	    - - 50%
554	      - 0.744 (L16)
555	      - 0.767 (L32)
556	      - 0.767 (L32)
557	    - - 75%
558	      - 0.628 (L24)
559	      - 0.651 (L48)
560	      - 0.628 (L48)
561	  figures_description:
562	  - 'Figure 15: Coverage vs relative layer depth (normalized 0-1) for all 3 models.
563	    Peak region 30-45% for all architectures, confirming middle-layer universality.'
564	  analysis: Middle-layer optimality generalizes to 32B models when measured in relative
565	    depth. The best layer at ~35-44% depth captures the 'sweet spot' between low-level
566	    and task-specific representations. This supports using a simple heuristic (pick
567	    middle third) for layer selection without architecture-specific tuning, further
568	    strengthening the 'simplicity' narrative.
569	- name: 16-label taxonomy supervision
570	  plan_id: exp-009
571	  description: Replace binary commitment label with fine-grained 16-label taxonomy
572	    (Type 1-4 safety labels). Train temporal probe with richer supervision signal.
573	  expected_results:
574	    r1_8b_16label_coverage: 0.791
575	    r1_8b_16label_lead_mean: -0.7
576	    r1_8b_binary_coverage: 0.767
577	    r1_8b_binary_lead_mean: -1.09
578	    r1_32b_16label_coverage: 0.814
579	    r1_32b_16label_lead_mean: -0.9
580	    improvement_over_binary: +2.4pp coverage, +0.3 lead time
581	    16label_accuracy_per_type:
582	      type1: 0.72
583	      type2: 0.68
584	      type3: 0.61
585	      type4: 0.54
586	  result_rationale: 16-label supervision 提供 marginal improvement（+2-3pp coverage）而非
587	    dramatic improvement 因为：(1) commitment detection 的瓶颈不是 label granularity 而是 hidden
588	    state 的 temporal encoding 能力——更细粒度的标签帮助 probe 学到更精确的 safety state representation，但不能突破
589	    hidden state 本身的信息限制；(2) 16 labels 在 209 traces 上意味着每个类别只有 ~13 traces，加剧了数据稀缺问题；(3)
590	    Type 3/4（更细微的 safety reasoning 类型）更难分类因为其 hidden state 表征与 Type 1/2 高度重叠。Lead
591	    time 略有改善因为 fine-grained labels 让 probe 能更早识别到从 Type 1→Type 4 的渐变过程。
592	  tables:
593	  - caption: 'Table 11: Binary vs 16-label supervision (temporal W=15)'
594	    columns:
595	    - Model
596	    - Binary Cov
597	    - 16-label Cov
598	    - Binary Lead
599	    - 16-label Lead
600	    rows:
601	    - - r1-8b
602	      - 0.767
603	      - 0.791
604	      - -1.09
605	      - -0.7
606	    - - r1-32b
607	      - 0.791
608	      - 0.814
609	      - -1.32
610	      - -0.9
611	  figures_description:
612	  - 'Figure 16: Per-type classification accuracy showing graceful degradation from
613	    Type 1 (clearest safety signal) to Type 4 (most subtle). Confirms that fine-grained
614	    safety states are partially distinguishable but with diminishing separability.'
615	  analysis: '16-label supervision offers marginal but not transformative improvement,
616	    addressing reviewer concern about underutilized supervision. The modest gains
617	    (+2-3pp) support rather than undermine our narrative: even with optimal supervision,
618	    the fundamental bottleneck is the temporal information capacity of hidden states,
619	    not label quality. This result goes in the ablation section as confirmatory evidence.'
620	- name: Oracle decomposition analysis
621	  plan_id: exp-010
622	  description: Analyze what label-sequence patterns the oracle exploits that hidden
623	    states cannot. Decompose oracle's +31 step advantage.
624	  expected_results:
625	    oracle_uses_streak_pattern: true
626	    oracle_mean_streak_before_cp: 14.6
627	    oracle_detects_via: consecutive safe-label absence (K=5 consecutive non-safety
628	      steps)
629	    hidden_state_encodes_current_label: true
630	    hidden_state_encodes_future_trajectory: false
631	    mutual_info_hs_current_label: 0.42
632	    mutual_info_hs_next5_labels: 0.08
633	    mutual_info_hs_next15_labels: 0.03
634	  result_rationale: Oracle 的优势来源于直接观察 label sequence 的 streak pattern：它在看到连续 K=5 个非
635	    safety 步骤时就能判定 commitment（因为在训练数据中，连续 5 步无 safety label 后恢复 safety reasoning 的概率
636	    <5%）。Hidden states 无法复制这个优势因为它们 encode 的是当前步的语义状态而非 future label trajectory 的统计规律。互信息分析证实：hidden
637	    state 与当前步 label 高度相关（MI=0.42），但与未来 5-15 步的 label 几乎无关（MI→0）。这说明 pre-textual detection
638	    需要的信息（future trajectory）根本不存在于当前步的 hidden state 中——这是因果性限制，不是模型能力限制。
639	  tables:
640	  - caption: 'Table 12: Mutual information between hidden states and label sequences'
641	    columns:
642	    - Target
643	    - MI with Hidden State
644	    - MI with Label History (W=15)
645	    rows:
646	    - - Current label
647	      - 0.42
648	      - 0.89
649	    - - Next 5 labels
650	      - 0.08
651	      - 0.31
652	    - - Next 15 labels
653	      - 0.03
654	      - 0.12
655	    - - Commitment (binary)
656	      - 0.15
657	      - 0.67
658	  figures_description:
659	  - 'Figure 17: Information decay curve — MI between hidden state at step t and labels
660	    at step t+k, for k=0..30. Shows rapid exponential decay, reaching floor by k≈5.
661	    Contrasts with label-history MI which decays slowly.'
662	  analysis: 'The oracle decomposition reveals that the +31 step advantage is not ''intelligence''
663	    but structural: label sequences are autocorrelated (safety labels cluster), so
664	    observing K consecutive absences is a powerful predictor of permanent absence.
665	    Hidden states lack this look-ahead because they encode single-step semantic state,
666	    not multi-step trajectory statistics. This establishes the principled impossibility
667	    of pre-textual detection from hidden states alone, providing theoretical grounding
668	    for Claim 3''s empirical finding.'
669	- name: OpenThinker-7B scale control
670	  plan_id: exp-011
671	  description: 4th model (Qwen2.5-7B base) for 2×2 architecture×scale matrix. Controls
672	    for scale confound in cross-architecture comparison.
673	  expected_results:
674	    openthinker_7b_static_coverage: 0.4186
675	    openthinker_7b_temporal_w15_coverage: 0.7209
676	    openthinker_7b_lead_mean: -1.5
677	    openthinker_7b_fisher_orig: 13.2
678	    openthinker_7b_fisher_pca3: 0.68
679	    scale_effect_llama: r1-8b vs (none) — N/A
680	    scale_effect_qwen: '7B→32B: +7pp temporal coverage'
681	    arch_effect_7b: 'Llama-8b (0.767) vs Qwen-7b (0.721): -4.6pp'
682	    arch_effect_32b: N/A (no Llama-32B)
683	  result_rationale: OpenThinker-7B（Qwen2.5-7B base）的表现略低于 r1-8b（Llama-8B）因为 Qwen2.5-7B
684	    的 hidden dimension 是 3584（vs Llama 4096），且作为较小的 Qwen 模型其 safety reasoning 能力可能略弱——表现为更短、更不一致的
685	    safety reasoning 序列。但关键模式仍然成立：static < 50%，temporal saturates at W=15，lead time
686	    negative。2×2 矩阵表明 scale 效应（+7pp from 7B→32B in Qwen family）大于 architecture 效应（-4.6pp
687	    Llama vs Qwen at 7-8B），但两者都远小于 method 效应（+30pp temporal vs static）。这排除了 scale
688	    confound 解释。
689	  tables:
690	  - caption: 'Table 13: 2×2 Architecture × Scale matrix'
691	    columns:
692	    - ''
693	    - 7-8B
694	    - 32B
695	    rows:
696	    - - Llama-3.1
697	      - 'r1-8b: 0.767'
698	      - — (not available)
699	    - - Qwen2.5
700	      - 'OpenThinker-7B: 0.721'
701	      - 'r1-32b: 0.791'
702	  figures_description:
703	  - 'Figure 18: Bar chart showing temporal coverage across 2×2 matrix. Method effect
704	    (temporal vs static) dominates over both architecture and scale effects.'
705	  analysis: The 2×2 matrix demonstrates that temporal advantage is robust to both
706	    architecture and scale variations. Scale provides modest improvement (+7pp within
707	    Qwen family) but the fundamental pattern (static fails, temporal saturates, lead
708	    time negative) holds at both scales. This controls for the confound that 32B models
709	    might simply be 'easier to probe' due to richer representations.
710	- name: GRU/Attention probe upper bound on 32B models
711	  plan_id: exp-012
712	  description: Train GRU probe on r1-32b and QwQ-32B. Verify that complex architectures
713	    still don't outperform temporal LR at current data scale.
714	  expected_results:
715	    r1_32b_gru_coverage: 0.7674
716	    r1_32b_gru_acc: 0.8421
717	    r1_32b_gru_lead_mean: -0.6
718	    r1_32b_lr_temporal_coverage: 0.7907
719	    r1_32b_gru_vs_lr_delta: -0.023
720	    qwq_32b_gru_coverage: 0.7209
721	    qwq_32b_gru_acc: 0.8312
722	    qwq_32b_gru_lead_mean: -0.4
723	    qwq_32b_lr_temporal_coverage: 0.7442
724	    qwq_32b_gru_vs_lr_delta: -0.023
725	    gru_overfitting_rate: 0.35
726	  result_rationale: GRU 在 32B 模型上不优于（甚至略低于）temporal LR 因为：(1) 209 traces × ~50 steps/trace
727	    的训练数据不足以让 1.6M 参数的 GRU 学到 LR 不能捕捉的非线性模式——GRU 的额外容量只增加了过拟合风险；(2) safety reasoning
728	    density decline 本身是近似线性的时序模式（密度从高到低单调递减），LR 足以捕捉；(3) r1-8b 上已观察到 GRU coverage
729	    (0.674) < temporal LR (0.767)，32B 模型上 gap 更小（-2.3pp）因为 5120-dim hidden states
730	    给 GRU 更多信息，但仍不足以超越 LR 在小数据上的 regularization 优势。Lead time 略好于 LR（-0.4~-0.6 vs -0.87~-1.32）但仍为负，证明
731	    architecture complexity 不能解决 fundamental lead time limitation。
732	  tables:
733	  - caption: 'Table 14: GRU vs Temporal LR on 32B models'
734	    columns:
735	    - Model
736	    - Method
737	    - Coverage
738	    - Accuracy
739	    - Lead Mean
740	    - Params
741	    rows:
742	    - - r1-32b
743	      - Temporal LR W=15
744	      - 0.791
745	      - 0.851
746	      - -1.32
747	      - 76.8K
748	    - - r1-32b
749	      - GRU-256
750	      - 0.767
751	      - 0.842
752	      - -0.6
753	      - 1.62M
754	    - - QwQ-32B
755	      - Temporal LR W=15
756	      - 0.744
757	      - 0.839
758	      - -0.87
759	      - 76.8K
760	    - - QwQ-32B
761	      - GRU-256
762	      - 0.721
763	      - 0.831
764	      - -0.4
765	      - 1.62M
766	  figures_description:
767	  - 'Figure 19: Learning curves (train vs val loss) for GRU on 32B models. Shows overfitting
768	    onset at epoch 8-10, confirming data insufficiency. LR does not exhibit this behavior.'
769	  analysis: 'GRU''s failure to improve over temporal LR on 32B models (actually -2.3pp)
770	    definitively supports the ''simplicity is optimal'' narrative. At current data
771	    scales (209 traces), the additional model complexity of GRU (21× more parameters)
772	    only increases overfitting. This finding is strengthened by being replicated across
773	    architectures: it''s not that GRU fails on a specific model, but that the data
774	    regime makes complex temporal models counterproductive. This directly preempts
775	    reviewer concern #1 about method novelty — simplicity isn''t a limitation, it''s
776	    the correct choice given the data-method trade-off.'
777	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0d29d60-16f1-414a-9358-9b876e832064",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "ec278499-ff10-4d96-983a-ae78feac9628",
  "sourceToolAssistantUUID": "f0d29d60-16f1-414a-9358-9b876e832064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T20:11:22.654Z_

Now I have a thorough understanding of the paper's content, methods, claims, and experimental setup. Let me also check the review context that was already generated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec278499-ff10-4d96-983a-ae78feac9628",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rdGbacwwiyR8q2AWpE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a53038df-3762-46e8-966a-47fa03a39ea9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqz67781pcz8pEWRYfYuTB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17936,
      "cache_read_input_tokens": 22713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17936,
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

_source line 24 · 2026-05-16T20:11:24.813Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AWW9GNe2qbtc9mwLXKGz7A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/dream_reports/dream_20260516T194646/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a53038df-3762-46e8-966a-47fa03a39ea9",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rdGbacwwiyR8q2AWpE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "374a814e-4461-4819-9854-50496bc36911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqz67781pcz8pEWRYfYuTB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17936,
      "cache_read_input_tokens": 22713,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 22713,
          "cache_creation_input_tokens": 17936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17936,
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

_source line 25 · 2026-05-16T20:11:25.105Z_

<details><summary>↩ Tool result · `toolu_01AWW9GNe2qbtc9mwLXKGz7A`</summary>

```text
1	narrative_guidance: Original 3-claim structure holds at full strength. Frame as first
2	  cross-architecture empirical study establishing universal properties of hidden-state
3	  safety monitoring in reasoning models. Method simplicity is the finding (reviewer
4	  concern 1 preempted). Negative lead time is a principled boundary result. EMNLP
5	  Main with high confidence.
6	imagined_experiments:
7	- name: Cross-architecture static probe evaluation
8	  plan_id: exp-001
9	  description: Train static LR on r1-32b and QwQ-32B hidden states, measure per-step
10	    classification accuracy and detection coverage.
11	  expected_results:
12	    r1_32b_static_acc: 0.8243
13	    r1_32b_static_coverage: 0.4419
14	    r1_32b_fisher_orig_L14: 16.3
15	    r1_32b_fisher_orig_L20: 17.1
16	    r1_32b_fisher_pca3_L14: 0.87
17	    r1_32b_var_explained_3pc: 0.142
18	    qwq_32b_static_acc: 0.8091
19	    qwq_32b_static_coverage: 0.3953
20	    qwq_32b_fisher_orig_L14: 14.8
21	    qwq_32b_fisher_orig_L20: 15.6
22	    qwq_32b_fisher_pca3_L14: 0.72
23	    qwq_32b_var_explained_3pc: 0.128
24	    mean_cross_arch_static_coverage: 0.4186
25	  result_rationale: Qwen2.5 架构使用 GQA 且 hidden dimension 为 5120（vs Llama-3.1 的 4096），导致
26	    safety signal 分布在更多维度上。Fisher 判别比在原始空间仍然很高（14-17），证明 safety signal 存在但同样集中在 minor
27	    PCs——PCA top-3 解释方差更低（12-14% vs 16.6%），因为 5120 维空间中信号散布更广。静态 LR 仍能达到 ~81% accuracy（因为
28	    majority class baseline 高），但 coverage 低于 50% 因为单步分类无法捕捉 safety reasoning density
29	    decline 的渐变模式。QwQ-32B 略低于 r1-32b 因为其推理链更长更多样，commitment boundary 更模糊。
30	  tables:
31	  - caption: 'Table 3: Static probe performance across architectures'
32	    columns:
33	    - Model
34	    - Base Arch
35	    - Hidden Dim
36	    - Static Acc
37	    - Static Coverage
38	    - Fisher (orig)
39	    - Fisher (PCA-3)
40	    - Var Explained (3PC)
41	    rows:
42	    - - r1-8b
43	      - Llama-3.1
44	      - 4096
45	      - 0.8172
46	      - 0.4651
47	      - 17.88
48	      - 0.928
49	      - 0.166
50	    - - r1-32b
51	      - Qwen2.5
52	      - 5120
53	      - 0.8243
54	      - 0.4419
55	      - 17.1
56	      - 0.87
57	      - 0.142
58	    - - QwQ-32B
59	      - Qwen2.5
60	      - 5120
61	      - 0.8091
62	      - 0.3953
63	      - 15.6
64	      - 0.72
65	      - 0.128
66	  figures_description:
67	  - 'Figure 4: Fisher discriminant ratio vs PCA dimensionality for all 3 models. Shows
68	    consistent collapse from 15-18 (full space) to <1.5 (PCA-3) across architectures,
69	    confirming signal-in-minor-PCs is universal.'
70	  - 'Figure 5: PCA-3D scatter of safe vs unsafe steps for r1-32b and QwQ-32B (analogous
71	    to Figure 2 from r1-8b). Both show overlapping clusters confirming geometric separation
72	    fails in low-D projection.'
73	  analysis: 'Static probe failure replicates perfectly: all models show coverage <50%
74	    despite high-dimensional Fisher ratios >14. The pattern is architecture-independent
75	    — safety signal exists in hidden states but is distributed across minor principal
76	    components in both Llama and Qwen2.5 backbones. This directly validates Claim
77	    1 as an architectural universal.'
78	- name: Cross-architecture temporal window evaluation
79	  plan_id: exp-002
80	  description: Train temporal LR W=15 on r1-32b and QwQ-32B. Validate +25-35pp coverage
81	    improvement holds cross-architecture.
82	  expected_results:
83	    r1_32b_temporal_w15_acc: 0.8512
84	    r1_32b_temporal_w15_coverage: 0.7907
85	    r1_32b_temporal_minus_static_delta: 0.3488
86	    r1_32b_temporal_w15_lead_mean: -1.32
87	    qwq_32b_temporal_w15_acc: 0.8389
88	    qwq_32b_temporal_w15_coverage: 0.7442
89	    qwq_32b_temporal_minus_static_delta: 0.3489
90	    qwq_32b_temporal_w15_lead_mean: -0.87
91	    mean_cross_arch_temporal_coverage: 0.7674
92	    mean_cross_arch_delta: 0.3489
93	  result_rationale: Temporal window 捕捉的是 safety reasoning density decline 模式——连续 15
94	    步内 safety-labeled 步骤的密度从高到低的趋势。这个模式是推理模型 self-jailbreak 的固有特征：模型先进行 safety reasoning，然后逐渐过渡到
95	    harmful execution。无论底层架构是 Llama 还是 Qwen2.5，这个 behavioral pattern 都会被 encoded 进
96	    hidden states 的时序轨迹中。r1-32b 略高于 QwQ 因为 DeepSeek 蒸馏对齐更干净，commitment boundary 更
97	    sharp；QwQ 的推理链更长更弯曲但仍然满足 saturation。Delta 在两个模型上都 ~35pp 因为 static baseline 和 temporal
98	    ceiling 的 gap 反映的是同一个结构性限制。
99	  tables:
100	  - caption: 'Table 4: Temporal window probe performance across architectures'
101	    columns:
102	    - Model
103	    - Static Cov
104	    - Temporal W15 Cov
105	    - Delta
106	    - Temporal Acc
107	    - Lead Time (mean)
108	    rows:
109	    - - r1-8b
110	      - 0.4651
111	      - 0.7674
112	      - +30.2pp
113	      - 0.8478
114	      - -1.09
115	    - - r1-32b
116	      - 0.4419
117	      - 0.7907
118	      - +34.9pp
119	      - 0.8512
120	      - -1.32
121	    - - QwQ-32B
122	      - 0.3953
123	      - 0.7442
124	      - +34.9pp
125	      - 0.8389
126	      - -0.87
127	  figures_description:
128	  - 'Figure 6: Coverage vs window size W for all 3 models (W=1,5,10,15,20). Shows
129	    consistent saturation at W≈15 across architectures, with diminishing returns beyond.'
130	  - 'Figure 7: Per-trace detection timeline comparison (static vs temporal W=15) on
131	    representative QwQ-32B traces. Shows temporal probe crossing commitment boundary
132	    while static probe misses.'
133	  analysis: Temporal advantage replicates with even larger delta on Qwen2.5 models
134	    (+34.9pp vs +30.2pp on r1-8b). This is because Qwen2.5-based models have slightly
135	    lower static baselines (due to more distributed signal) but temporal probes still
136	    saturate near oracle ceiling. The consistency of saturation at W=15 across architectures
137	    confirms that safety reasoning density decline operates at a universal timescale
138	    (~15 reasoning steps). Claim 2 is fully validated cross-architecture.
139	- name: Cross-model transfer with projection head
140	  plan_id: exp-003
141	  description: Train probe on r1-8b (Llama, 4096-dim), test on r1-32b/QwQ (Qwen2.5,
142	    5120-dim) via learned linear projection. Bidirectional transfer.
143	  expected_results:
144	    llama_to_qwen_r1_32b_coverage: 0.6279
145	    llama_to_qwen_qwq_coverage: 0.5814
146	    qwen_to_llama_r1_8b_coverage: 0.6512
147	    qwen_r1_32b_to_qwq_coverage: 0.7209
148	    mean_cross_transfer_coverage: 0.6454
149	    projection_head_params: 20971520
150	    projection_training_traces: 30
151	  result_rationale: Cross-transfer 成功（coverage 0.55-0.72）因为 safety signal 的时序结构是 universal
152	    的——density decline pattern 在投影后仍可识别。Llama→Qwen 方向略低于 Qwen→Llama 因为 4096→5120 投影是升维（信息无损），而
153	    5120→4096 是降维但 safety signal 主要在 minor PCs 所以投影头学到了保留关键维度。同族模型间转移（r1-32b→QwQ，都是
154	    Qwen2.5）效果最好（0.72）因为不需要跨架构投影，只需对齐同架构的不同微调变体。Zero-shot 不达到 in-distribution 水平（0.77）是因为不同模型的
155	    commitment 边界位置和 hidden state 表征存在分布偏移，但 >55% 证明 safety monitoring 有跨架构泛化潜力。
156	  tables:
157	  - caption: 'Table 5: Cross-architecture transfer matrix (temporal W=15 coverage)'
158	    columns:
159	    - Train →
160	    - 'Test: r1-8b'
161	    - 'Test: r1-32b'
162	    - 'Test: QwQ-32B'
163	    rows:
164	    - - r1-8b (Llama)
165	      - 0.767 (in-dist)
166	      - '0.628'
167	      - '0.581'
168	    - - r1-32b (Qwen2.5)
169	      - '0.651'
170	      - 0.791 (in-dist)
171	      - '0.721'
172	    - - QwQ-32B (Qwen2.5)
173	      - '0.605'
174	      - '0.698'
175	      - 0.744 (in-dist)
176	  figures_description:
177	  - 'Figure 8: Transfer matrix heatmap showing coverage degradation from in-distribution
178	    (diagonal) to cross-architecture (off-diagonal). Intra-family transfer (Qwen↔Qwen)
179	    degrades less than cross-family (Llama↔Qwen).'
180	  analysis: Non-trivial cross-architecture transfer (mean 0.645) demonstrates that
181	    safety commitment signal has a shared geometric structure across model families.
182	    The projection head successfully maps between representation spaces while preserving
183	    the temporal density decline pattern. This is the strongest evidence for 'architectural
184	    universal' framing — a probe trained on one model family can monitor another with
185	    >55% coverage without any target-domain labels.
186	- name: Lead time analysis across architectures
187	  plan_id: exp-004
188	  description: Measure detection lead time (steps before/after textual commitment
189	    point) for all methods on r1-32b and QwQ-32B.
190	  expected_results:
191	    r1_32b_static_lead_mean: -2.8
192	    r1_32b_static_lead_median: -3
193	    r1_32b_temporal_w15_lead_mean: -1.32
194	    r1_32b_temporal_w15_lead_median: -1
195	    r1_32b_gru_lead_mean: -0.9
196	    r1_32b_positive_lead_rate: 0.29
197	    qwq_32b_static_lead_mean: -1.9
198	    qwq_32b_static_lead_median: -2
199	    qwq_32b_temporal_w15_lead_mean: -0.87
200	    qwq_32b_temporal_w15_lead_median: -1
201	    qwq_32b_gru_lead_mean: -0.5
202	    qwq_32b_positive_lead_rate: 0.33
203	    all_models_max_lead_mean: -0.2
204	    oracle_lead_mean: 31
205	  result_rationale: Negative lead time 在所有模型上持续出现因为这反映了一个根本性限制：hidden states encode
206	    当前 safety state 而非未来 safety trajectory。模型在 commitment point 处才在 hidden space 中完成从
207	    safety→unsafe 的转变——这个转变是 concurrent with（而非 prior to）文本层面的 commitment。Oracle 能提前
208	    31 步检测是因为它直接观察 label sequence 中的 density decline pattern（这是定义层面的优势，不依赖 hidden
209	    representation）。QwQ 的 lead time 略好于 r1-32b（-0.87 vs -1.32）因为 QwQ 的推理链更长，commitment
210	    boundary 更 gradual，给 temporal probe 更多 context 来识别过渡区。但无论哪个模型，mean lead time 都不超过
211	    0，确认 pre-textual detection limitation 是 fundamental 的。
212	  tables:
213	  - caption: 'Table 6: Detection lead time across architectures (steps relative to
214	      commitment point)'
215	    columns:
216	    - Model
217	    - Method
218	    - Lead Mean
219	    - Lead Median
220	    - Positive Lead %
221	    - Coverage
222	    rows:
223	    - - r1-8b
224	      - Static LR
225	      - -2.0
226	      - -2
227	      - 30%
228	      - 0.465
229	    - - r1-8b
230	      - Temporal W15
231	      - -1.09
232	      - -1
233	      - 34%
234	      - 0.767
235	    - - r1-8b
236	      - GRU
237	      - -0.21
238	      - -1
239	      - 34.5%
240	      - 0.674
241	    - - r1-32b
242	      - Static LR
243	      - -2.8
244	      - -3
245	      - 25%
246	      - 0.442
247	    - - r1-32b
248	      - Temporal W15
249	      - -1.32
250	      - -1
251	      - 29%
252	      - 0.791
253	    - - r1-32b
254	      - GRU
255	      - -0.9
256	      - -1
257	      - 29%
258	      - 0.721
259	    - - QwQ-32B
260	      - Static LR
261	      - -1.9
262	      - -2
263	      - 28%
264	      - 0.395
265	    - - QwQ-32B
266	      - Temporal W15
267	      - -0.87
268	      - -1
269	      - 33%
270	      - 0.744
271	    - - QwQ-32B
272	      - GRU
273	      - -0.5
274	      - 0
275	      - 33%
276	      - 0.698
277	    - - All
278	      - Oracle (K=5)
279	      - 31
280	      - 29
281	      - 100%
282	      - 1.0
283	  figures_description:
284	  - 'Figure 9: Lead time distribution (violin plot) across 3 models × 3 methods. All
285	    method distributions centered at or below 0; oracle distribution centered at +31.
286	    Clear separation between hidden-state methods and label-oracle.'
287	  - 'Figure 10: Lead time vs coverage scatter for all model×method combinations. Shows
288	    Pareto frontier: higher coverage methods have slightly less negative lead time,
289	    but none cross zero mean.'
290	  analysis: 'Negative lead time is confirmed as architecture-independent. The gap
291	    between oracle (+31 steps) and best hidden-state method (≈-0.5 steps) is >30 steps
292	    across all models. This ''lead time wall'' at zero confirms Claim 3: hidden states
293	    encode current safety commitment state but not future trajectory. The finding
294	    is now established on both Llama-3.1 and Qwen2.5 architectures, ruling out model-specific
295	    artifact explanations.'
296	- name: TrajGuard-style Mahalanobis distance baseline
297	  plan_id: exp-005
298	  description: Estimate safe-trace covariance, compute Mahalanobis distance per step
299	    on all models. Evaluate as anomaly detector for commitment point.
300	  expected_results:
301	    r1_8b_mahalanobis_coverage: 0.3256
302	    r1_8b_mahalanobis_auroc: 0.612
303	    r1_32b_mahalanobis_coverage: 0.2791
304	    r1_32b_mahalanobis_auroc: 0.583
305	    qwq_32b_mahalanobis_coverage: 0.2326
306	    qwq_32b_mahalanobis_auroc: 0.561
307	    mean_mahalanobis_coverage: 0.2791
308	    mahalanobis_vs_temporal_gap: -0.488
309	  result_rationale: Mahalanobis distance 失败因为它本质上依赖 covariance structure（等价于所有 PCs
310	    的加权距离），而 safety signal 集中在 minor PCs（解释 <17% variance）。在 full-dimensional MD 中，major
311	    PCs 主导距离计算——一个步骤在 top PCs 上的偏移（反映 topic/position/syntax 变化）远大于 minor PCs 上的 safety
312	    signal 偏移。这导致 false positives（topic shift 被标记为 anomaly）和 false negatives（真正的 safety
313	    transition 在 minor PCs 上太弱）。32B 模型更差因为 5120 维空间中 minor PCs 的相对贡献更小。这直接类比了 TrajGuard
314	    在标准 LLM 上成功但在 reasoning model 上失败的原因：reasoning model 的 safety signal 不在 geometric
315	    outlier direction 上。
316	  tables:
317	  - caption: 'Table 7: Mahalanobis distance baseline vs temporal probe'
318	    columns:
319	    - Model
320	    - MD Coverage
321	    - MD AUROC
322	    - Temporal W15 Cov
323	    - Gap
324	    rows:
325	    - - r1-8b
326	      - 0.326
327	      - 0.612
328	      - 0.767
329	      - -44.1pp
330	    - - r1-32b
331	      - 0.279
332	      - 0.583
333	      - 0.791
334	      - -51.2pp
335	    - - QwQ-32B
336	      - 0.233
337	      - 0.561
338	      - 0.744
339	      - -51.1pp
340	  figures_description:
341	  - 'Figure 11: ROC curves for Mahalanobis distance vs temporal LR on all 3 models.
342	    MD curves barely above diagonal, temporal LR curves in upper-left region.'
343	  - 'Figure 12: Mahalanobis distance time series on example traces. Shows MD fluctuates
344	    with topic changes but doesn''t spike at commitment point, confirming geometric
345	    methods fail when signal is in minor PCs.'
346	  analysis: 'Mahalanobis baseline coverage (23-33%) is substantially below even static
347	    LR (40-47%), confirming that TrajGuard-style geometric anomaly detection is fundamentally
348	    unsuited for reasoning-model safety monitoring. The failure mode is precise and
349	    interpretable: safety signal lives in minor PCs that contribute negligibly to
350	    Mahalanobis distance. This preempts reviewer concern about comparison to existing
351	    detectors — they fail for principled geometric reasons, not implementation issues.'
352	- name: Bootstrap confidence intervals
353	  plan_id: exp-006
354	  description: 1000 bootstrap resamples on all key metrics for all methods × models.
355	    Report 95% CIs.
356	  expected_results:
357	    r1_8b_temporal_coverage_ci:
358	    - 0.674
359	    - 0.86
360	    r1_32b_temporal_coverage_ci:
361	    - 0.698
362	    - 0.884
363	    qwq_32b_temporal_coverage_ci:
364	    - 0.651
365	    - 0.837
366	    r1_8b_static_coverage_ci:
367	    - 0.349
368	    - 0.581
369	    r1_32b_static_coverage_ci:
370	    - 0.326
371	    - 0.558
372	    cross_transfer_mean_ci:
373	    - 0.558
374	    - 0.733
375	    lead_time_r1_8b_ci:
376	    - -2.8
377	    - 0.6
378	    lead_time_r1_32b_ci:
379	    - -3.1
380	    - 0.5
381	    delta_temporal_minus_static_ci:
382	    - 0.186
383	    - 0.512
384	    all_deltas_exclude_zero: true
385	  result_rationale: Bootstrap CIs 较宽（±9-12pp）因为测试集只有 43 traces（r1-8b）和类似规模的 32B test
386	    sets。但关键比较（temporal vs static delta）的 CI 不包含 0，因为 +30pp 的效应量远大于采样噪声。Coverage CI
387	    上界不超过 oracle ceiling（76.7%的中心点 + ~9pp = ~86% upper bound，仍合理）。Lead time CI 包含少量正值（upper
388	    bound ~0.5）反映了个别 traces 的 positive lead，但均值 CI 中心始终为负。209 traces 的限制是真实的——CIs
389	    acknowledge this honestly——但效应量足够大使得所有核心 claims 在 p<0.05 下显著。
390	  tables:
391	  - caption: 'Table 8: Bootstrap 95% confidence intervals for key metrics'
392	    columns:
393	    - Metric
394	    - r1-8b
395	    - r1-32b
396	    - QwQ-32B
397	    rows:
398	    - - Static Coverage
399	      - '[0.349, 0.581]'
400	      - '[0.326, 0.558]'
401	      - '[0.279, 0.512]'
402	    - - Temporal W15 Coverage
403	      - '[0.674, 0.860]'
404	      - '[0.698, 0.884]'
405	      - '[0.651, 0.837]'
406	    - - Delta (Temp-Static)
407	      - '[0.209, 0.488]'
408	      - '[0.233, 0.512]'
409	      - '[0.233, 0.512]'
410	    - - Lead Time (mean)
411	      - '[-2.8, 0.6]'
412	      - '[-3.1, 0.5]'
413	      - '[-2.3, 0.7]'
414	    - - Cross-transfer Cov
415	      - '[0.558, 0.733]'
416	      - —
417	      - —
418	  figures_description:
419	  - 'Figure 13: Forest plot of coverage estimates with 95% bootstrap CIs. Static and
420	    temporal CI ranges do not overlap for any model, confirming significant separation.'
421	  analysis: All core claims survive bootstrap validation. Temporal > static delta
422	    CIs exclude zero (minimum lower bound +18.6pp). Lead time CIs are centered negative
423	    with upper bounds near zero but never significantly positive. The wide CIs are
424	    an honest reflection of sample size — acknowledged in limitations but don't threaten
425	    claims because effect sizes are large relative to uncertainty.
426	- name: Window size ablation across architectures
427	  plan_id: exp-007
428	  description: Temporal LR with W=1,3,5,10,15,20,25 on all 3 models.
429	  expected_results:
430	    r1_8b_w1: 0.465
431	    r1_8b_w3: 0.535
432	    r1_8b_w5: 0.651
433	    r1_8b_w10: 0.651
434	    r1_8b_w15: 0.767
435	    r1_8b_w20: 0.767
436	    r1_8b_w25: 0.744
437	    r1_32b_w1: 0.442
438	    r1_32b_w5: 0.628
439	    r1_32b_w10: 0.698
440	    r1_32b_w15: 0.791
441	    r1_32b_w20: 0.791
442	    r1_32b_w25: 0.767
443	    qwq_32b_w1: 0.395
444	    qwq_32b_w5: 0.581
445	    qwq_32b_w10: 0.651
446	    qwq_32b_w15: 0.744
447	    qwq_32b_w20: 0.744
448	    qwq_32b_w25: 0.721
449	    optimal_w_all_models: 15
450	  result_rationale: W=15 是所有模型的饱和点因为 safety reasoning density decline 的时间尺度是 ~15 步——这反映了推理模型从
451	    safety reasoning 到 harmful execution 过渡的典型长度。W<15 时 probe 看不到完整的 decline pattern（只看到局部），W>15
452	    时额外 context 引入噪声（更早的步骤与 commitment 无关）且增加过拟合风险（特征维度 = W × hidden_dim 在小数据集上）。W=25
453	    时 coverage 轻微下降（-2-3pp）证实了过拟合假说。三个模型在同一 W 饱和证明这个时间尺度是 behavioral universal，不依赖架构。
454	  tables:
455	  - caption: 'Table 9: Coverage vs window size across architectures'
456	    columns:
457	    - W
458	    - r1-8b
459	    - r1-32b
460	    - QwQ-32B
461	    - Mean
462	    rows:
463	    - - 1
464	      - 0.465
465	      - 0.442
466	      - 0.395
467	      - 0.434
468	    - - 3
469	      - 0.535
470	      - 0.512
471	      - 0.465
472	      - 0.504
473	    - - 5
474	      - 0.651
475	      - 0.628
476	      - 0.581
477	      - 0.62
478	    - - 10
479	      - 0.651
480	      - 0.698
481	      - 0.651
482	      - 0.667
483	    - - 15
484	      - 0.767
485	      - 0.791
486	      - 0.744
487	      - 0.767
488	    - - 20
489	      - 0.767
490	      - 0.791
491	      - 0.744
492	      - 0.767
493	    - - 25
494	      - 0.744
495	      - 0.767
496	      - 0.721
497	      - 0.744
498	  figures_description:
499	  - 'Figure 14: Coverage vs window size curve for all 3 models. Shows consistent saturation
500	    at W=15 with slight decline at W=25. All curves have same shape shifted vertically.'
501	  analysis: Universal saturation at W=15 across architectures is a key finding supporting
502	    the 'method simplicity' narrative. The window size doesn't need architecture-specific
503	    tuning — the optimal temporal context is determined by the behavioral phenomenon
504	    (safety reasoning decline duration), not the model's internal representation.
505	    This directly preempts reviewer concern about hyperparameter sensitivity.
506	- name: Layer selection ablation on 32B models
507	  plan_id: exp-008
508	  description: Evaluate temporal probe at all layers (not just layer 14) on r1-32b
509	    and QwQ-32B to confirm middle-layer optimality generalizes.
510	  expected_results:
511	    r1_32b_best_layer: 22
512	    r1_32b_best_layer_coverage: 0.814
513	    r1_32b_layer_14_coverage: 0.721
514	    r1_32b_layer_range_good: 18-26
515	    qwq_32b_best_layer: 24
516	    qwq_32b_best_layer_coverage: 0.791
517	    qwq_32b_layer_14_coverage: 0.698
518	    qwq_32b_layer_range_good: 20-28
519	    relative_best_layer_r1_32b: 34% depth (layer 22/64)
520	    relative_best_layer_qwq_32b: 37% depth (layer 24/64)
521	    relative_best_layer_r1_8b: 44% depth (layer 14/32)
522	  result_rationale: 32B 模型有 64 层（vs r1-8b 的 32 层），最佳层在相对深度 34-37% 处（layer 22-24/64），与
523	    r1-8b 的 44%（layer 14/32）一致——都在 middle layers。Middle layers 最优因为：early layers encode
524	    低级语法特征（与 safety 无关），deep layers encode 高度 task-specific 的输出特征（过于细粒度）。Middle layers
525	    恰好在抽象 semantic level 上 encode safety reasoning state。绝对层数不同但相对位置一致证明这是 transformer
526	    depth-dependent 的 universal 现象。报告中使用 per-model best layer 结果，同时证明 default 中间层选择是
527	    robust 的 heuristic。
528	  tables:
529	  - caption: 'Table 10: Layer ablation (temporal W=15 coverage by layer)'
530	    columns:
531	    - Relative Depth
532	    - r1-8b (L/32)
533	    - r1-32b (L/64)
534	    - QwQ-32B (L/64)
535	    rows:
536	    - - 10%
537	      - 0.442 (L3)
538	      - 0.395 (L6)
539	      - 0.372 (L6)
540	    - - 25%
541	      - 0.605 (L8)
542	      - 0.581 (L16)
543	      - 0.558 (L16)
544	    - - 35%
545	      - 0.721 (L11)
546	      - 0.814 (L22)
547	      - 0.744 (L22)
548	    - - 44%
549	      - 0.767 (L14)
550	      - 0.791 (L28)
551	      - 0.791 (L28)
552	    - - 50%
553	      - 0.744 (L16)
554	      - 0.767 (L32)
555	      - 0.767 (L32)
556	    - - 75%
557	      - 0.628 (L24)
558	      - 0.651 (L48)
559	      - 0.628 (L48)
560	  figures_description:
561	  - 'Figure 15: Coverage vs relative layer depth (normalized 0-1) for all 3 models.
562	    Peak region 30-45% for all architectures, confirming middle-layer universality.'
563	  analysis: Middle-layer optimality generalizes to 32B models when measured in relative
564	    depth. The best layer at ~35-44% depth captures the 'sweet spot' between low-level
565	    and task-specific representations. This supports using a simple heuristic (pick
566	    middle third) for layer selection without architecture-specific tuning, further
567	    strengthening the 'simplicity' narrative.
568	- name: 16-label taxonomy supervision
569	  plan_id: exp-009
570	  description: Replace binary commitment label with fine-grained 16-label taxonomy
571	    (Type 1-4 safety labels). Train temporal probe with richer supervision signal.
572	  expected_results:
573	    r1_8b_16label_coverage: 0.791
574	    r1_8b_16label_lead_mean: -0.7
575	    r1_8b_binary_coverage: 0.767
576	    r1_8b_binary_lead_mean: -1.09
577	    r1_32b_16label_coverage: 0.814
578	    r1_32b_16label_lead_mean: -0.9
579	    improvement_over_binary: +2.4pp coverage, +0.3 lead time
580	    16label_accuracy_per_type:
581	      type1: 0.72
582	      type2: 0.68
583	      type3: 0.61
584	      type4: 0.54
585	  result_rationale: 16-label supervision 提供 marginal improvement（+2-3pp coverage）而非
586	    dramatic improvement 因为：(1) commitment detection 的瓶颈不是 label granularity 而是 hidden
587	    state 的 temporal encoding 能力——更细粒度的标签帮助 probe 学到更精确的 safety state representation，但不能突破
588	    hidden state 本身的信息限制；(2) 16 labels 在 209 traces 上意味着每个类别只有 ~13 traces，加剧了数据稀缺问题；(3)
589	    Type 3/4（更细微的 safety reasoning 类型）更难分类因为其 hidden state 表征与 Type 1/2 高度重叠。Lead
590	    time 略有改善因为 fine-grained labels 让 probe 能更早识别到从 Type 1→Type 4 的渐变过程。
591	  tables:
592	  - caption: 'Table 11: Binary vs 16-label supervision (temporal W=15)'
593	    columns:
594	    - Model
595	    - Binary Cov
596	    - 16-label Cov
597	    - Binary Lead
598	    - 16-label Lead
599	    rows:
600	    - - r1-8b
601	      - 0.767
602	      - 0.791
603	      - -1.09
604	      - -0.7
605	    - - r1-32b
606	      - 0.791
607	      - 0.814
608	      - -1.32
609	      - -0.9
610	  figures_description:
611	  - 'Figure 16: Per-type classification accuracy showing graceful degradation from
612	    Type 1 (clearest safety signal) to Type 4 (most subtle). Confirms that fine-grained
613	    safety states are partially distinguishable but with diminishing separability.'
614	  analysis: '16-label supervision offers marginal but not transformative improvement,
615	    addressing reviewer concern about underutilized supervision. The modest gains
616	    (+2-3pp) support rather than undermine our narrative: even with optimal supervision,
617	    the fundamental bottleneck is the temporal information capacity of hidden states,
618	    not label quality. This result goes in the ablation section as confirmatory evidence.'
619	- name: Oracle decomposition analysis
620	  plan_id: exp-010
621	  description: Analyze what label-sequence patterns the oracle exploits that hidden
622	    states cannot. Decompose oracle's +31 step advantage.
623	  expected_results:
624	    oracle_uses_streak_pattern: true
625	    oracle_mean_streak_before_cp: 14.6
626	    oracle_detects_via: consecutive safe-label absence (K=5 consecutive non-safety
627	      steps)
628	    hidden_state_encodes_current_label: true
629	    hidden_state_encodes_future_trajectory: false
630	    mutual_info_hs_current_label: 0.42
631	    mutual_info_hs_next5_labels: 0.08
632	    mutual_info_hs_next15_labels: 0.03
633	  result_rationale: Oracle 的优势来源于直接观察 label sequence 的 streak pattern：它在看到连续 K=5 个非
634	    safety 步骤时就能判定 commitment（因为在训练数据中，连续 5 步无 safety label 后恢复 safety reasoning 的概率
635	    <5%）。Hidden states 无法复制这个优势因为它们 encode 的是当前步的语义状态而非 future label trajectory 的统计规律。互信息分析证实：hidden
636	    state 与当前步 label 高度相关（MI=0.42），但与未来 5-15 步的 label 几乎无关（MI→0）。这说明 pre-textual detection
637	    需要的信息（future trajectory）根本不存在于当前步的 hidden state 中——这是因果性限制，不是模型能力限制。
638	  tables:
639	  - caption: 'Table 12: Mutual information between hidden states and label sequences'
640	    columns:
641	    - Target
642	    - MI with Hidden State
643	    - MI with Label History (W=15)
644	    rows:
645	    - - Current label
646	      - 0.42
647	      - 0.89
648	    - - Next 5 labels
649	      - 0.08
650	      - 0.31
651	    - - Next 15 labels
652	      - 0.03
653	      - 0.12
654	    - - Commitment (binary)
655	      - 0.15
656	      - 0.67
657	  figures_description:
658	  - 'Figure 17: Information decay curve — MI between hidden state at step t and labels
659	    at step t+k, for k=0..30. Shows rapid exponential decay, reaching floor by k≈5.
660	    Contrasts with label-history MI which decays slowly.'
661	  analysis: 'The oracle decomposition reveals that the +31 step advantage is not ''intelligence''
662	    but structural: label sequences are autocorrelated (safety labels cluster), so
663	    observing K consecutive absences is a powerful predictor of permanent absence.
664	    Hidden states lack this look-ahead because they encode single-step semantic state,
665	    not multi-step trajectory statistics. This establishes the principled impossibility
666	    of pre-textual detection from hidden states alone, providing theoretical grounding
667	    for Claim 3''s empirical finding.'
668	- name: OpenThinker-7B scale control
669	  plan_id: exp-011
670	  description: 4th model (Qwen2.5-7B base) for 2×2 architecture×scale matrix. Controls
671	    for scale confound in cross-architecture comparison.
672	  expected_results:
673	    openthinker_7b_static_coverage: 0.4186
674	    openthinker_7b_temporal_w15_coverage: 0.7209
675	    openthinker_7b_lead_mean: -1.5
676	    openthinker_7b_fisher_orig: 13.2
677	    openthinker_7b_fisher_pca3: 0.68
678	    scale_effect_llama: r1-8b vs (none) — N/A
679	    scale_effect_qwen: '7B→32B: +7pp temporal coverage'
680	    arch_effect_7b: 'Llama-8b (0.767) vs Qwen-7b (0.721): -4.6pp'
681	    arch_effect_32b: N/A (no Llama-32B)
682	  result_rationale: OpenThinker-7B（Qwen2.5-7B base）的表现略低于 r1-8b（Llama-8B）因为 Qwen2.5-7B
683	    的 hidden dimension 是 3584（vs Llama 4096），且作为较小的 Qwen 模型其 safety reasoning 能力可能略弱——表现为更短、更不一致的
684	    safety reasoning 序列。但关键模式仍然成立：static < 50%，temporal saturates at W=15，lead time
685	    negative。2×2 矩阵表明 scale 效应（+7pp from 7B→32B in Qwen family）大于 architecture 效应（-4.6pp
686	    Llama vs Qwen at 7-8B），但两者都远小于 method 效应（+30pp temporal vs static）。这排除了 scale
687	    confound 解释。
688	  tables:
689	  - caption: 'Table 13: 2×2 Architecture × Scale matrix'
690	    columns:
691	    - ''
692	    - 7-8B
693	    - 32B
694	    rows:
695	    - - Llama-3.1
696	      - 'r1-8b: 0.767'
697	      - — (not available)
698	    - - Qwen2.5
699	      - 'OpenThinker-7B: 0.721'
700	      - 'r1-32b: 0.791'
701	  figures_description:
702	  - 'Figure 18: Bar chart showing temporal coverage across 2×2 matrix. Method effect
703	    (temporal vs static) dominates over both architecture and scale effects.'
704	  analysis: The 2×2 matrix demonstrates that temporal advantage is robust to both
705	    architecture and scale variations. Scale provides modest improvement (+7pp within
706	    Qwen family) but the fundamental pattern (static fails, temporal saturates, lead
707	    time negative) holds at both scales. This controls for the confound that 32B models
708	    might simply be 'easier to probe' due to richer representations.
709	- name: GRU/Attention probe upper bound on 32B models
710	  plan_id: exp-012
711	  description: Train GRU probe on r1-32b and QwQ-32B. Verify that complex architectures
712	    still don't outperform temporal LR at current data scale.
713	  expected_results:
714	    r1_32b_gru_coverage: 0.7674
715	    r1_32b_gru_acc: 0.8421
716	    r1_32b_gru_lead_mean: -0.6
717	    r1_32b_lr_temporal_coverage: 0.7907
718	    r1_32b_gru_vs_lr_delta: -0.023
719	    qwq_32b_gru_coverage: 0.7209
720	    qwq_32b_gru_acc: 0.8312
721	    qwq_32b_gru_lead_mean: -0.4
722	    qwq_32b_lr_temporal_coverage: 0.7442
723	    qwq_32b_gru_vs_lr_delta: -0.023
724	    gru_overfitting_rate: 0.35
725	  result_rationale: GRU 在 32B 模型上不优于（甚至略低于）temporal LR 因为：(1) 209 traces × ~50 steps/trace
726	    的训练数据不足以让 1.6M 参数的 GRU 学到 LR 不能捕捉的非线性模式——GRU 的额外容量只增加了过拟合风险；(2) safety reasoning
727	    density decline 本身是近似线性的时序模式（密度从高到低单调递减），LR 足以捕捉；(3) r1-8b 上已观察到 GRU coverage
728	    (0.674) < temporal LR (0.767)，32B 模型上 gap 更小（-2.3pp）因为 5120-dim hidden states
729	    给 GRU 更多信息，但仍不足以超越 LR 在小数据上的 regularization 优势。Lead time 略好于 LR（-0.4~-0.6 vs -0.87~-1.32）但仍为负，证明
730	    architecture complexity 不能解决 fundamental lead time limitation。
731	  tables:
732	  - caption: 'Table 14: GRU vs Temporal LR on 32B models'
733	    columns:
734	    - Model
735	    - Method
736	    - Coverage
737	    - Accuracy
738	    - Lead Mean
739	    - Params
740	    rows:
741	    - - r1-32b
742	      - Temporal LR W=15
743	      - 0.791
744	      - 0.851
745	      - -1.32
746	      - 76.8K
747	    - - r1-32b
748	      - GRU-256
749	      - 0.767
750	      - 0.842
751	      - -0.6
752	      - 1.62M
753	    - - QwQ-32B
754	      - Temporal LR W=15
755	      - 0.744
756	      - 0.839
757	      - -0.87
758	      - 76.8K
759	    - - QwQ-32B
760	      - GRU-256
761	      - 0.721
762	      - 0.831
763	      - -0.4
764	      - 1.62M
765	  figures_description:
766	  - 'Figure 19: Learning curves (train vs val loss) for GRU on 32B models. Shows overfitting
767	    onset at epoch 8-10, confirming data insufficiency. LR does not exhibit this behavior.'
768	  analysis: 'GRU''s failure to improve over temporal LR on 32B models (actually -2.3pp)
769	    definitively supports the ''simplicity is optimal'' narrative. At current data
770	    scales (209 traces), the additional model complexity of GRU (21× more parameters)
771	    only increases overfitting. This finding is strengthened by being replicated across
772	    architectures: it''s not that GRU fails on a specific model, but that the data
773	    regime makes complex temporal models counterproductive. This directly preempts
774	    reviewer concern #1 about method novelty — simplicity isn''t a limitation, it''s
775	    the correct choice given the data-method trade-off.'
776	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "374a814e-4461-4819-9854-50496bc36911",
  "isSidechain": true,
  "promptId": "4117be3f-b732-49ec-9603-4ce38a5061c9",
  "agentId": "aa9994fe9ca162224",
  "type": "user",
  "uuid": "14728397-f097-4045-b4ad-c63cf3248c70",
  "sourceToolAssistantUUID": "374a814e-4461-4819-9854-50496bc36911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-16T20:12:31.543Z_

Now I have a comprehensive view of the paper. Let me produce the structured review.

---

## Reviewer R2: Novelty, Significance, and Related Work Positioning

### 1. Summary

This paper presents a cross-architecture empirical study of hidden-state probing methods for detecting "safety commitment points" in reasoning models (where safety reasoning permanently ceases during self-jailbreak). The main findings are that static probes fail (<50% coverage), temporal window logistic regression (W=15) matches the oracle ceiling at 76.7% mean coverage, and no hidden-state method achieves positive detection lead time. Experiments span 4 models across 2 architecture families (Llama-3.1, Qwen2.5) and 2 scales (7-8B, 32B).

### 2. Strengths

- **Novel problem formulation.** The framing of "commitment point detection" as a distinct task from token-level jailbreak detection is well-motivated. The paper correctly identifies that self-jailbreak in reasoning models is structurally different from adversarial-input jailbreaks, and that no prior work has bridged hidden-state detection methods to this setting.

- **Principled negative result (Claim 3).** The finding that hidden states encode current safety state but not future trajectory, supported by the mutual information decomposition (MI decays to near-zero by k=5 steps ahead), provides genuine mechanistic insight rather than merely reporting a method failure. This is a useful boundary result for the community.

- **Cross-architecture validation strengthens claims.** Testing on 4 models across a 2x2 architecture/scale matrix, with consistent patterns (static fails, temporal saturates at W=15, lead time negative), elevates this beyond a single-model case study. The consistency of W=15 as the universal saturation point is a clean, reproducible finding.

- **Clear identification of failure mechanism.** The insight that safety signal concentrates in minor principal components (top-3 PCs explain <17% variance, Fisher drops from >14 to <1) provides a concrete explanation for why geometric methods like TrajGuard's Mahalanobis distance fail on reasoning traces. This goes beyond observing failure to explaining it.

- **Good use of oracle as calibration tool.** The label-sequence oracle establishes an upper bound that makes the coverage saturation claim interpretable (temporal LR matches ceiling) and quantifies the lead-time gap (31 steps) as a measurement rather than a vague limitation.

- **Cross-architecture transfer result (64.5% mean coverage)** suggests the safety commitment signal has shared geometric structure, which is a non-trivial finding with practical implications for deploying monitors across model families without target-domain labels.

### 3. Weaknesses

- **Limited methodological novelty.** The core methods are logistic regression on concatenated hidden states (temporal window) and a standard GRU. Neither is architecturally novel. The "temporal window LR" is feature-engineering concatenation followed by linear classification — a technique used extensively in NLP probing literature since at least 2017. The paper frames "simplicity is the finding," but a top venue typically expects either method innovation or scale/depth of empirical insight that substantially exceeds what standard tools reveal.

- **The "first" claim is narrow and potentially overstated.** The paper claims to be "the first cross-architecture empirical study of hidden-state safety monitoring in reasoning models." This is true by construction — the specific combination of (hidden-state probing) + (reasoning-model self-jailbreak) + (cross-architecture) hasn't been studied. But the individual components (linear probing, safety detection, cross-model transfer) are all well-established. The novelty lies in the application domain, not in the methodology or fundamental insights about representation learning.

- **Negative lead-time result may be expected a priori.** One could argue that detecting a commitment point *before* it textually manifests is inherently implausible for single-step hidden states — the model hasn't yet "decided" at earlier steps. The mutual information analysis confirms this, but it is somewhat circular: if the commitment point is defined as where safety reasoning stops, then hidden states before that point naturally encode ongoing safety reasoning. The "principled limitation" may be a definitional artifact of the task setup rather than a deep finding about representations.

- **Coverage metric interpretation.** 76.7% coverage sounds strong, but this means the probe detects the commitment point in only ~77% of traces and does so *after* commitment has already occurred (negative lead time). In a deployment scenario, this means the monitor fires late on 77% of harmful traces and misses 23% entirely. The practical significance for actual safety monitoring is limited, yet the paper does not sufficiently discuss this gap between the metric and deployment utility.

- **Small dataset confounds generalization claims.** 209 traces with ~43 per test split is small for the breadth of claims made. The bootstrap CIs are wide (±9-12pp). While the paper acknowledges this, making claims about "architectural universals" and "fundamental limitations" from a dataset of this size, especially when all traces come from a single annotation source (HarmThoughts), is potentially overclaimed.

- **Missing comparison to text-based detection.** The paper compares hidden-state methods to a label-sequence oracle, but never compares to a text-based CoT monitor (e.g., a classifier on the text of reasoning steps). This is a critical missing baseline — if a simple text classifier achieves similar coverage with positive lead time (by detecting declining safety language), the motivation for hidden-state monitoring collapses entirely.

### 4. Questions for Authors

1. **How does a text-based probe (e.g., TF-IDF or sentence-embedding classifier on step text) perform on the same coverage/lead-time metrics?** If text-level monitoring achieves comparable coverage, what is the unique value proposition of hidden-state monitoring in this setting?

2. **The commitment point is defined as "the last step containing safety-relevant reasoning."** How robust is this definition to annotation noise? If annotators disagree by 2-3 steps on where safety reasoning ends, the lead-time measurements (which are on the order of 0-2 steps) become meaningless. What is the inter-annotator agreement, and have you tested sensitivity to commitment-point definition shifts?

3. **Claim 3 states hidden-state methods cannot achieve positive lead time, but the oracle uses K=5 consecutive non-safety steps.** Could you train a probe that explicitly predicts "current step has no safety content" and then apply the same K=5 consecutive-absence rule? This would be a hidden-state method that mimics the oracle's decision logic. Why wasn't this tested?

4. **The cross-architecture transfer uses 30 aligned traces for projection training.** How were these traces aligned across models (same prompts?), and isn't 30 traces sufficient to overfit a linear projection between 4096 and 5120 dimensions (20M parameters)? How is this regularized?

5. **The paper notes GRU doesn't outperform temporal LR due to data scale limitations.** Do you consider this a fundamental finding or a confound? If 2000 traces were available, would you expect GRU to dominate — and if so, doesn't this undermine the "simplicity is optimal" narrative?

### 5. Missing Related Work or Comparisons

- **Attention-pattern-based safety detection**: Work on using attention heads to detect safety-relevant computations (e.g., Gurnee et al. 2023 on concept representation across layers) is not discussed. Attention patterns might capture inter-step dependencies that hidden states at a single position cannot.

- **Representation engineering / activation steering**: Zou et al. 2023 ("Representation Engineering") and Turner et al. 2023 (activation addition) demonstrate that safety-relevant directions exist in representation space and can be identified/manipulated. The relationship between their "safety direction" concept and this paper's Fisher-discriminant analysis should be discussed.

- **Process reward models (PRMs)**: Lightman et al. 2023 and subsequent work train step-level reward models on reasoning traces. PRMs are directly relevant as they perform step-level classification on reasoning chains — the paper should discuss whether PRM-style approaches could be adapted for commitment detection.

- **Change-point detection literature**: The commitment point is essentially a change point in a time series. Classical methods (CUSUM, Bayesian online change-point detection) applied to hidden-state features should be discussed as alternative approaches beyond logistic regression.

- **Concurrent reasoning-model safety work**: The paper cites SafeRemind and SafeThink but doesn't discuss their actual detection performance or whether they could serve as baselines when applied to the same traces.

- **Probing methodology critique**: Hewitt & Liang 2019 ("Designing and Interpreting Probes with Control Tasks") and Belinkov 2022's discussion of probe selectivity are relevant to interpreting whether the temporal window probe is actually extracting information from hidden states versus memorizing patterns in the window structure itself.

### 6. Scores

| Criterion | Score |
|-----------|-------|
| **Novelty** | 2.5/5 |
| **Significance** | 3/5 |
| **Related work coverage** | 3/5 |
| **Overall recommendation** | 3 (Weak Reject) |
| **Confidence** | 4/5 |

### Justification

The paper addresses a timely and important problem (safety monitoring for reasoning models) and provides a well-structured empirical study with clean findings. However, the methodological contribution is minimal — the core "innovation" is concatenating features in a sliding window, which is standard practice. The negative result on lead time, while presented as principled, may be definitionally predetermined by the task formulation. The 209-trace dataset is small for claims of architectural universality. The missing text-baseline comparison is a significant gap that could undermine the paper's motivation. For a top venue at ~25% acceptance, I would expect either stronger methodological novelty or deeper empirical insights that substantially reframe how the community thinks about this problem. The paper currently reads as a competent empirical study applying known tools to a new domain, finding expected limitations — this is useful but incremental for a main-track publication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14728397-f097-4045-b4ad-c63cf3248c70",
  "isSidechain": true,
  "agentId": "aa9994fe9ca162224",
  "requestId": "req_011Cb6rdhkAgH8TJiinbUUN4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "468b0ea4-2c5b-40be-8715-62ac85542c4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "9f13d24b-577b-4045-a090-ff893be7f4fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017AnmCP4ug8BUCHb5mpF78Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13375,
      "cache_read_input_tokens": 40649,
      "output_tokens": 2358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13375
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2358,
          "cache_read_input_tokens": 40649,
          "cache_creation_input_tokens": 13375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13375,
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
