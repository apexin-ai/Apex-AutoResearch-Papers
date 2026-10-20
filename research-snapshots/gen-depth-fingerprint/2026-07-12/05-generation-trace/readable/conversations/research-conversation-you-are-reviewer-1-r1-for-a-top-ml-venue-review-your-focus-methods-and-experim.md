# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus: **Methods and Experiments**. ## Paper Summary "Generation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aad193fce74ed6217.jsonl`
- **Structured JSON:** [`aa60391bfc0040c69eec.json`](../../sessions/aa/aa60391bfc0040c69eec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-14T23:07:51.539Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus: **Methods and Experiments**.

## Paper Summary
"Generation Depth Estimation: A Missing Layer in Synthetic Text Analysis" formalizes generation depth estimation as an ordinal classification task — predicting how many recursive LLM generation steps separate a text from its human-written seed (gen-0/gen-1/gen-2+). The paper extracts 7 distributional features (2 surface: TTR, hapax_ratio; 5 reference-model NLL statistics: entropy_mean/std/max/min, tail_decay) and trains an XGBoost classifier. It evaluates across 12 experimental conditions.

## Key Results from the Paper
- In-distribution (Pythia-2.8B gen, Pythia-410M ref, Wikipedia): macro-F1 = 0.82
- After length control: F1 drops from 0.78 to 0.68 (10-point drop); 61-68% of surface feature depth correlation explained by length
- Cross-generator LOGO: F1 = 0.52; cross-family drops to 0.41-0.48
- Reference model sensitivity: entropy_mean ρ=-0.68 (Pythia ref) vs ρ=-0.22 (OLMo) vs ρ=-0.15 (Qwen) — H2 drift is family-specific
- Generator scale: F1 correlates with log-params at r=-0.85; 8B generator yields F1=0.43
- Prompt type: continuation F1=0.78 vs elaboration 0.55 vs rewriting 0.47; cross-prompt transfer F1=0.42
- Cross-model chains: F1=0.39 (near chance for gen-1/gen-2+)
- Domain: Wikipedia 0.72, creative 0.48; cross-domain transfer 0.49
- 5-class ordinal: F1=0.28 (barely above chance 0.20)
- Edit robustness: 5% random replace → F1 drops 0.10; LLM edit → drops 0.25
- LD-Score: negligible improvement (+0.005)
- End-to-end QLoRA: F1=0.83 in-dist but also fails cross-generator (0.55)
- Downstream utility: depth-aware filtering 1.8% improvement vs binary 1.2%, but CIs overlap (p=0.31), not significant

## Experiment Design Reference (what was planned)
14 experiments were planned. The paper covers all of them. Key thresholds from the design:
- Cross-generator LOGO F1 threshold: 0.58 (paper reports 0.52 — fails)
- Length-controlled F1 drop threshold: >0.08 counts as confound (paper reports 0.10 — triggers)
- Cross-family ref entropy_mean |ρ|<0.3 threshold (OLMo ρ=-0.22, Qwen ρ=-0.15 — breached)
- Downstream depth-vs-binary p<0.05 needed (paper reports p=0.31 — fails significance)

## Your Review Task
Provide a detailed review covering:

1. **Soundness of methodology** (feature design, classifier choice, evaluation protocol)
2. **Experimental rigor** (statistical controls, multiple seeds, CIs, confound handling)
3. **Coverage vs. planned experiments** — are all 14 planned experiments reflected? Missing experiments?
4. **Strength of evidence for each claim** — the paper makes 4 claims (task formulation, reference-model perplexity as proxy, scale-dependent degradation, comprehensive limitations). Rate the evidence.
5. **Weaknesses** — identify methodological issues, missing controls, threats to validity
6. **Questions for authors**

Use a 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept.

Format your output as:
### R1: Methods and Experiments
**Score: X/6**
**Summary** (2-3 sentences)
**Strengths** (bulleted)
**Weaknesses** (bulleted)
**Detailed Comments** (numbered)
**Questions for Authors** (numbered)
**Experiment Coverage Assessment** (brief)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "e65fa2c8-cb50-465e-8f8c-b538e4d35f40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T23:07:51.544Z_

```json
{
  "parentUuid": "e65fa2c8-cb50-465e-8f8c-b538e4d35f40",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
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
  "uuid": "08c1d8b8-9888-4c12-8e7c-b6187ce05325",
  "timestamp": "2026-05-14T23:07:51.544Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T23:07:54.100Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08c1d8b8-9888-4c12-8e7c-b6187ce05325",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JUF3aJ1ciHrZT5pUSs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c299534-d6c1-4aa4-a816-458cfbb15c85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQbFruDjmV6P8naQ9jKE1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15122,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15122,
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

_source line 4 · 2026-05-14T23:07:55.631Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HS6SpnY3u7BwhiL9fCpRih`</summary>

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
  "parentUuid": "6c299534-d6c1-4aa4-a816-458cfbb15c85",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JUF3aJ1ciHrZT5pUSs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ede6e24c-775a-4f4b-a21e-ffbae49ae4f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQbFruDjmV6P8naQ9jKE1a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15122,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15122
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15122,
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

_source line 5 · 2026-05-14T23:07:55.635Z_

<details><summary>↩ Tool result · `toolu_01HS6SpnY3u7BwhiL9fCpRih`</summary>

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
  "parentUuid": "ede6e24c-775a-4f4b-a21e-ffbae49ae4f3",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "3f2b37b3-bd71-4127-bb0a-81969081b2e5",
  "sourceToolAssistantUUID": "ede6e24c-775a-4f4b-a21e-ffbae49ae4f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T23:08:00.930Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01SH4ERGjpQw6y5hHhdWhNky`</summary>

```json
{
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f2b37b3-bd71-4127-bb0a-81969081b2e5",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JUYXJWb4Max2Rd6jvv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78faf2e7-f69a-4e9e-8342-b2cb2367bc02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJQM24L7yihFtezGu8dcV7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15122,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 7 · 2026-05-14T23:08:00.998Z_

<details><summary>↩ Tool result · `toolu_01SH4ERGjpQw6y5hHhdWhNky`</summary>

```text
{"result":"# 项目 gen-depth-fingerprint 概况\n\n## 实验状态 (25 个)\n\n- **plan-002-qwen3-1_7b-s0**: DONE (failed) — \n- **plan-002-qwen3-1_7b-s1**: DONE (killed) — \n- **plan-002-olmo2-s1**: DONE (success) — \n- **plan-002-olmo2-s0**: DONE (success) — \n- **plan-002-pythia1b-s1**: DONE (success) — \n- **plan-002-pythia1b-s0**: DONE (success) — \n- **plan-002**: RUNNING — \n- **plan-001-fix**: DONE (success) — \n- **plan-001**: DONE (success) — \n- **plan-001-restore**: PREPARING — \n- **mvp-001**: DONE (success) — \n- **mvp-001-gen-s0**: PREPARING — \n- **mvp-001-gen-s3**: PREPARING (failed) — \n- **mvp-001-gen-s2**: PREPARING (failed) — \n- **mvp-001-gen-s1**: PREPARING (failed) — \n\n## 最新报告\n# Handover — 2026-05-14\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| plan-002-qwen17b-r2-s1 | — | — | — | — |\n| plan-002-qwen17b-r2-s0 | — | — | — | — |\n| plan-002 | 跨模型泛化：Pythia-410M 参考模型下的深度特征能否区分不同架构/规模生成器（Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）的 continuation 链 | — | — | — |\n\n## 待处理\n- plan-001-restore（准备中）\n- mvp-001-gen-s0（准备中）\n- mvp-001-gen-s3（准备中）\n- mvp-001-gen-s2（准备中）\n- mvp-001-gen-s1（准备中）\n\n## 近期结论\n- **plan-002-qwen06b-r2-s1** (success): 跨模型泛化数据生成：Qwen3-0.6B continuation 链 shard1（orphan 进程恢复）\n- **plan-002-qwen06b-r2-s0** (success): 跨模型泛化数据生成：Qwen3-0.6B continuation 链 shard0（orphan 进程恢复）\n- **plan-002-qwen17b-retry-s1** (failed): —\n\n## 趋势\n成功 9 / 负向 0 / 失败 7 / 共 17\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- plan-002-qwen3-1_7b-s0: 训练失败 — unknown\n- plan-002-qwen3-1_7b-s1: 已被终止 — unknown\n- plan-002-qwen17b-s0: 训练失败 — unknown\n- plan-002-qwen17b-s1: 训练失败 — unknown\n- plan-002-qwen17b-retry-s0: 训练失败 — unknown\n- plan-002-qwen17b-retry-s1: 训练失败 — unknown\n- plan-002-qwen06b-s0: 训练失败 — unknown\n- plan-002-qwen06b-s1: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78faf2e7-f69a-4e9e-8342-b2cb2367bc02",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "4f71750b-b87c-49da-b676-911d5c5da80f",
  "sourceToolAssistantUUID": "78faf2e7-f69a-4e9e-8342-b2cb2367bc02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T23:08:01.391Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018eu4YPgv5zD93WY54ABcsu`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f71750b-b87c-49da-b676-911d5c5da80f",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JUYXJWb4Max2Rd6jvv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad80490f-5c5f-4db0-86e5-962494b71498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJQM24L7yihFtezGu8dcV7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 15122,
      "output_tokens": 162,
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
          "output_tokens": 162,
          "cache_read_input_tokens": 15122,
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

_source line 9 · 2026-05-14T23:08:01.397Z_

<details><summary>↩ Tool result · `toolu_018eu4YPgv5zD93WY54ABcsu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan-002-qwen17b-r2-s1 | — | — | — | — |\\n| plan-002-qwen17b-r2-s0 | — | — | — | — |\\n| plan-002 | 跨模型泛化：Pythia-410M 参考模型下的深度特征能否区分不同架构/规模生成器（Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）的 continuation 链 | — | — | — |\\n\\n## 待处理\\n- plan-001-restore（准备中）\\n- mvp-001-gen-s0（准备中）\\n- mvp-001-gen-s3（准备中）\\n- mvp-001-gen-s2（准备中）\\n- mvp-001-gen-s1（准备中）\\n\\n## 近期结论\\n- **plan-002-qwen06b-r2-s1** (success): 跨模型泛化数据生成：Qwen3-0.6B continuation 链 shard1（orphan 进程恢复）\\n- **plan-002-qwen06b-r2-s0** (success): 跨模型泛化数据生成：Qwen3-0.6B continuation 链 shard0（orphan 进程恢复）\\n- **plan-002-qwen17b-retry-s1** (failed): —\\n\\n## 趋势\\n成功 9 / 负向 0 / 失败 7 / 共 17\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- plan-002-qwen3-1_7b-s0: 训练失败 — unknown\\n- plan-002-qwen3-1_7b-s1: 已被终止 — unknown\\n- plan-002-qwen17b-s0: 训练失败 — unknown\\n- plan-002-qwen17b-s1: 训练失败 — unknown\\n- plan-002-qwen17b-retry-s0: 训练失败 — unknown\\n- plan-002-qwen17b-retry-s1: 训练失败 — unknown\\n- plan-002-qwen06b-s0: 训练失败 — unknown\\n- plan-002-qwen06b-s1: 训练失败 — unknown\\n\", \"total_chars\": 1179, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad80490f-5c5f-4db0-86e5-962494b71498",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "f8489b1d-e583-496c-9975-6c9b3ab003ae",
  "sourceToolAssistantUUID": "ad80490f-5c5f-4db0-86e5-962494b71498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T23:08:04.620Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01A9fuc5cCQotggpa7NdbEFi`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8489b1d-e583-496c-9975-6c9b3ab003ae",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JUyN32LQ4x28VtSrRC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f653e351-a71f-4e1c-825e-b5ba87fda723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LQ9KdcnXCFSfARQyGkCuA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2271,
      "cache_read_input_tokens": 16568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2271,
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

_source line 11 · 2026-05-14T23:08:04.627Z_

<details><summary>↩ Tool result · `toolu_01A9fuc5cCQotggpa7NdbEFi`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f653e351-a71f-4e1c-825e-b5ba87fda723",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "74fad076-0617-461a-899b-8857b11a356f",
  "sourceToolAssistantUUID": "f653e351-a71f-4e1c-825e-b5ba87fda723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T23:08:05.096Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RMhAbbVAg5k6TvUqYnsxzD`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74fad076-0617-461a-899b-8857b11a356f",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JUyN32LQ4x28VtSrRC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "788f8ae1-b7c1-41d7-85bb-743a1f508655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LQ9KdcnXCFSfARQyGkCuA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2271,
      "cache_read_input_tokens": 16568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2271,
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

_source line 13 · 2026-05-14T23:08:05.103Z_

<details><summary>↩ Tool result · `toolu_01RMhAbbVAg5k6TvUqYnsxzD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ROADMAP.md\", \"content\": \"# gen-depth-fingerprint — Research Dashboard\\n\\n> 最后更新: 2026-05-14 22:15 UTC | 更新原因: Dream D006 — framing重新定位+plan补充，re-dream前状态\\n\\n## 核心方向\\n非改写式 LLM 生成链展现 **双重深度动态**（level/diversity 特征随深度漂移 H₂，shape 特征近稳态 H₁），cross-cut surface/reference 边界。贡献定位为**实证/概念**（问题定义 + 实证发现 + 应用），非方法论。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **MVP**: PASS (macro-F1=0.84, D002)\\n- **plan-001**: DONE — feature ablation + trend + PPL pre-validation 完成\\n- **plan-002**: RUNNING — 跨生成器数据生成中，Pythia-1B/OLMo-2 已完成，Qwen3-1.7B/0.6B 进程已退出待确认\\n- **Dream**: dream_20260514T181213 完成，Best=5/Median=5/Worst=4 — **未达标**\\n  - 已执行 D006: framing 重新定位 + plan 补充 text_length_control + large_scale_generator + downstream 修改\\n  - **需 re-dream 验证后才能批准后续 P0**\\n\\n## 近期任务\\n- [ ] 确认 Qwen3-1.7B/0.6B 生成完成，合并分片，汇报各模型记录数\\n- [ ] Re-dream 验证 D006 修改后评分（framing+plan 已更新）\\n- [ ] Re-dream 达标后：启动 plan-002 feature extraction（Pythia-410M 跨5个生成器）\\n- [ ] plan-013 text_length_control（分析现有数据，零新生成）\\n- [ ] plan-003 cross-family reference model（Claim 2 关键伪证化测试）\\n- [ ] plan-004 downstream utility（OLMo-1B，多种子+CI，样本量匹配）\\n- [ ] [Dream 观察] plan-002 结果出来后评估：complementarity 是否在 cross-generator 下成立\\n- [ ] [Dream 观察] 评估是否需要 plan-014 large_scale_generator (7B+)\\n\\n## GPU 预算\\n- 分配: 4× RTX 5090 (autodl-5090: cuda:0-3)\\n- 当前: plan-002 生成占用 4 卡（进程退出待确认）\\n- P0 剩余: ~25.5h (plan-003: 8h, plan-004: 20h, plan-013: 0.5h — 部分可并行)\\n- P1 新增: plan-014 (8h)\\n- 总预算: ~116.5h / 200h\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-14 | Dream D006: framing+plan调整 — 重新定位为实证/概念贡献，补充text l | plan_001, plan_002, plan_013, plan_014, plan_004 |\\n| D005 | 2026-05-14 | Dual dynamics 细化：H1/H2 分界是 level/diversity vs shap | plan_001 |\\n| D004 | 2026-05-14 | Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 | plan_001 |\\n| D003 | 2026-05-14 | Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从  | — |\\n| D002 | 2026-05-14 | MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal  | mvp-001 |\\n| D001 | 2026-05-14 | MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考 | — |\\n\\n\\n\", \"total_chars\": 2015, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "788f8ae1-b7c1-41d7-85bb-743a1f508655",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "5d36903e-7eaf-41d8-828d-a78ecea41fe5",
  "sourceToolAssistantUUID": "788f8ae1-b7c1-41d7-85bb-743a1f508655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T23:08:06.040Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019NTRxotzJL5wSvQGknw1tx`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d36903e-7eaf-41d8-828d-a78ecea41fe5",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JUyN32LQ4x28VtSrRC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9f0e649-ebcd-49ab-b918-97c580743112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LQ9KdcnXCFSfARQyGkCuA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2271,
      "cache_read_input_tokens": 16568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2271,
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

_source line 15 · 2026-05-14T23:08:06.051Z_

<details><summary>↩ Tool result · `toolu_019NTRxotzJL5wSvQGknw1tx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/memory.md\", \"content\": \"# gen-depth-fingerprint — Memory\\n\\n## 关键发现\\n\\n### MVP-001 结果（2026-05-14）\\n- **PASS**: macro-F1=0.8408 (阈值 0.45), binary F1=0.8653 (阈值 0.65)\\n- 词汇多样性特征（hapax_ratio, ttr）区分力最强，feature importance 分别 0.30 和 0.17\\n- entropy_mean 是最强的模型级特征（importance 0.22）\\n- tail_decay 区分力最弱（importance 0.057），但仍统计显著\\n- gen-0 几乎完美分离（F1=0.95），gen-1 vs gen-2+ 有一定混淆（45 个 gen-2+ 误判为 gen-1）\\n- 深度衰减 17.4%：部分 continuation 产生空文本导致链条中断（995→822 from depth 0→4）\\n\\n### plan-001-fix 结果（2026-05-14）\\n- **Feature Complementarity 确认**: full(0.82) > surface(0.76) > reference(0.72)，bootstrap CI 不重叠\\n- **Dual Dynamics**: H2 drift 特征（entropy_mean, ttr, hapax_ratio）+ H1 stationary 特征（tail_decay, entropy_std, entropy_max）\\n- **Effect size 递减**: 漂移减速，gen-1→gen-2 entropy 跃迁最大\\n- **PPL 单调递减**: median 13.50→4.96→3.00→2.07→1.72，退化样本 <1%\\n- paper_framing.md Claim 2 调整为 \\\"Feature Complementarity & Dual Dynamics\\\"\\n\\n## 模型路径（autodl-5090）\\n\\n| 模型 | HF repo | params | 本地路径 |\\n|------|---------|--------|---------|\\n| pythia-2.8b | EleutherAI/pythia-2.8b | 2.8B | /root/autodl-tmp/.hf_cache/EleutherAI/pythia-2___8b |\\n| pythia-1b | EleutherAI/pythia-1b | 1012M | /root/autodl-tmp/models/pythia-1b/EleutherAI/pythia-1b |\\n| pythia-410m (ref) | EleutherAI/pythia-410m | 410M | /root/autodl-tmp/models/pythia-410m 或 .hf_cache 下 |\\n| olmo-2-1b | allenai/OLMo-2-0425-1B | 1485M | /root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B |\\n| qwen3-1.7b | Qwen/Qwen3-1.7B-Base | 1721M | /root/autodl-tmp/models/Qwen/Qwen3-1___7B-Base |\\n| qwen3-0.6b | Qwen/Qwen3-0.6B-Base | 596M | /root/autodl-tmp/models/Qwen/Qwen3-0___6B-Base |\\n\\n注意：Qwen3.5 系列不存在，用 Qwen3-Base 替代。OLMo-2-1B-hf 不存在，用 OLMo-2-0425-1B。ModelScope 下载路径名会转换（`2.8b` → `2___8b`）。\\n\\n## 经验教训\\n\\n### submit_training_job + CUDA_VISIBLE_DEVICES 映射（2026-05-14）\\n`submit_training_job` 自动注入 `CUDA_VISIBLE_DEVICES=N`（物理卡号）。注入后进程只看到 1 张卡，脚本内必须用 `--device cuda:0`（逻辑设备 0），不能用 `cuda:N`。\\n\\n### AutoDL 网络 + 数据源（2026-05-14）\\nWikipedia 数据集在 AutoDL 上流式加载失败。预下载到本地 JSONL，脚本用 `--input` 读本地文件。ModelScope 下载路径名会转换。\\n\\n### nohup vs submit_training_job（2026-05-14）\\nWorker 用 nohup 会导致 orphan 进程。必须用 `submit_training_job`（tmux + cron 自动监控）。\\n\\n### 生成参数（2026-05-14，Director 指定）\\ntemperature=0.7, top_p=0.9, max_new_tokens=256, do_sample=True, seed=42。判定：PASS/FAIL 二值，macro-F1 ≥ 0.45 AND binary F1 ≥ 0.65。\\n\\n### SIGHUP 事故根因（2026-05-14，已确认）\\n**框架 bug**，非重复提交。`tmux_backend.py:check_status()` 用 PID 数字调用 `tmux has-session`，但 session 名是 exp_id → 永远返回 false → Worker 误判 session 已死 → 调用 `kill_job()` → SIGHUP 杀掉存活 session（EXIT_CODE=129）。Pythia/OLMo 不受影响（运行时间短，在误判前已完成）。qwen06b 幸存因为用 ssh_execute 启动（无 tmux session 可被 kill）。Bug 位置：`/home/ubuntu/agent-ml-research/core/tools/execution_backends/tmux_backend.py` L178。**防御措施**：generate_chain.py 已加 `signal.signal(signal.SIGHUP, signal.SIG_IGN)` + append+flush+resume。\\n\\n### Orphan 进程存活模式（2026-05-14）\\ntmux session 被框架 bug kill 后，进程以 orphan 方式继续运行（得益于 SIGHUP ignore 防御）。cron 系统基于 tmux session 判断进程死亡 → 误报 failed。**教训**：cron 报告 failure 时，先用 `ps -p &lt;PID>` 确认进程是否真的死了，再下结论。本次 4 个 Qwen 进程全部以 orphan 方式正常完成了数据生成。\\n\\n### exp_id 命名规范（2026-05-14）\\n命名不一致（`qwen3-1_7b` vs `qwen17b`）导致混淆和重复提交。提交前必须检查 registry 中是否已有同模型同 shard 的活跃实验。\\n\", \"total_chars\": 3102, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9f0e649-ebcd-49ab-b918-97c580743112",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "b52074d1-b193-4e20-b0e2-e1f808b71397",
  "sourceToolAssistantUUID": "d9f0e649-ebcd-49ab-b918-97c580743112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T23:08:06.451Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PhkmvcLnjFFPG4u7szV4di`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b52074d1-b193-4e20-b0e2-e1f808b71397",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JUyN32LQ4x28VtSrRC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cec86771-44d7-4b51-b7c3-74c62c77c3af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LQ9KdcnXCFSfARQyGkCuA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2271,
      "cache_read_input_tokens": 16568,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2271
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 16568,
          "cache_creation_input_tokens": 2271,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2271,
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

_source line 17 · 2026-05-14T23:08:06.458Z_

<details><summary>↩ Tool result · `toolu_01PhkmvcLnjFFPG4u7szV4di`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cec86771-44d7-4b51-b7c3-74c62c77c3af",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "6e9a3756-acb0-458e-a8a7-ee75447e59b6",
  "sourceToolAssistantUUID": "cec86771-44d7-4b51-b7c3-74c62c77c3af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T23:08:09.623Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014MN3XLEXSAJu92kSt8eXp2`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e9a3756-acb0-458e-a8a7-ee75447e59b6",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JVLy3mhQCayAAiPLeW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8a3a083-b713-441e-9c3d-bb3e74054a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LepUNHRjDCBPUpJarRdZqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 18839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3933,
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

_source line 19 · 2026-05-14T23:08:09.632Z_

<details><summary>↩ Tool result · `toolu_014MN3XLEXSAJu92kSt8eXp2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-fingerprint\\n\\n## Target Venue\\n- Primary: AAAI 2027 (deadline: August 2, 2026)\\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\\n\\n## Core Insight\\nNon-paraphrastic LLM generation chains exhibit **dual depth dynamics** that cross-cuts the surface/reference distinction: **level/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth (H₂), while **distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁). Notably, entropy_mean is a reference-model feature that drifts (ρ=-0.68), showing the H₁/H₂ split is about what the feature measures (central tendency vs shape), not where it comes from (surface vs reference). This dual pattern creates a complementary feature space: drifting features provide ordinal depth signal, while stable shape features provide noise-robust class boundaries. The combination significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72).\\n\\n## Core Claims (3 条，均可证伪)\\n\\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\\n\\n**Claim 2 — Dual Dynamics (Level vs Shape)**: Depth-dependent features split into two families by **what they measure**, not by their source (surface vs reference): (a) **level/diversity features** (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (H₂ — vocabulary impoverishment + entropy compression); (b) **shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁ — distributional shape is robust to recursive generation). This split cross-cuts the surface/reference boundary (entropy_mean is reference-derived but drifts). Full feature set (0.82) significantly outperforms surface-only (0.76) and reference-only (0.72) — the two dynamics are complementary for classification.\\n\\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\\n\\n## Story Spine\\n\\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\\n\\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\\n\\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **dual dynamics**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth (H₂), while distributional shape features (entropy variance, tail decay) remain near-stationary (H₁). This split is about **what the feature measures** (central tendency vs shape), not where it comes from — overturning the naive expectation that \\\"reference-model features = robust, surface features = fragile.\\\" The dual pattern has practical value: drifting features provide ordinal depth signal, stable shape features provide noise-robust decision boundaries, and their combination yields the best depth estimation for risk-stratified data curation.\\n\\n**Headline result template**: \\\"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\\\"\\n\\n## Anticipated Reviewer Concerns\\n\\n**RC1 — \\\"Is this just vocabulary impoverishment?\\\"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are \\\"better\\\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). The dual dynamics finding is itself a scientific contribution. Note: \\\"fingerprint\\\" in the paper refers to the full feature vector's combination, not just reference-model features.\\n\\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\\n\\n**RC2 — \\\"Does this generalize beyond Pythia?\\\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\\n\\n**RC3 — \\\"Is 3-class sufficient? Why not finer-grained?\\\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\\n\\n**RC4 — \\\"How realistic are single-model chains?\\\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\\n\\n**RC5 — \\\"What about human editing / post-processing?\\\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\\n\\n**RC6 — \\\"Ecological validity — continuation vs real web content\\\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\\n\\n**RC8 — \\\"Aren't these just OOD detection features?\\\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\\n\\n**RC9 — \\\"Only ≤2.8B generators — does this transfer to frontier scale?\\\"**: All 5 current generators ≤2.8B. Frontier models (7B+) produce more fluent text that may compress depth signal. → Add at least one 7B+ generator (plan_014). If depth signal significantly weaker at scale → honest limitation with analysis of why; if comparable → strong generalization evidence.\\n\\n**RC10 — \\\"Text length confound\\\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\\n\\n**RC11 — \\\"Downstream utility — single run, no CIs\\\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\\n\\n## Contribution Positioning (Dream D006 insight)\\nThe contribution is **primarily empirical and conceptual**, not methodological. The features (NLL summary statistics) and classifier (XGBoost) are standard — the novelty lies in:\\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection\\n2. **Empirical discovery**: Dual dynamics (level/diversity drift vs shape stationarity) cross-cutting surface/reference boundary\\n3. **Practical application**: Risk-stratified data curation outperforming binary filtering\\n\\nDo NOT overclaim \\\"distributional fingerprinting\\\" as a new method. Position the paper as empirical science with a novel task formulation and a surprising empirical finding. The H1/H2 framework is an empirical validation extending attractor cycle theory to non-paraphrastic chains, not a major theoretical contribution.\\n\\nRelated work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020).\\n\\n## Venue Fit\\n- AAAI 2027: Fit as empirical + conceptual contribution — novel task formulation (depth estimation) + surprising empirical finding (dual dynamics) + practical application (data curation). Must position as empirical science, not methodology paper.\\n- EMNLP 2026: Excellent fit — directly addresses special theme \\\"New Missions for NLP Research\\\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work. Empirical/conceptual contributions better received here than AAAI.\\n\", \"total_chars\": 9985, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8a3a083-b713-441e-9c3d-bb3e74054a78",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "c88e2faa-ad1d-4ee7-bfee-dd7ffed6023c",
  "sourceToolAssistantUUID": "c8a3a083-b713-441e-9c3d-bb3e74054a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T23:08:10.600Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015BE5b58M1kM2GcbPWVKpHM`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c88e2faa-ad1d-4ee7-bfee-dd7ffed6023c",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JVLy3mhQCayAAiPLeW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92d430b9-7d5e-43b3-be04-fd753a04c718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LepUNHRjDCBPUpJarRdZqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 18839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3933,
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

_source line 21 · 2026-05-14T23:08:10.608Z_

<details><summary>↩ Tool result · `toolu_015BE5b58M1kM2GcbPWVKpHM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/decisions.yaml\", \"content\": \"_next_id: 7\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:15 UTC\\n  summary: MVP 方案：Pythia-2.8B continuation 链 + Pythia-410M 参考模型 + XGBoost 3-class\\n    分类\\n  rationale: '选择 continuation（最低语义偏离）作为最可能保留 depth 信号的生成类型；单生成器简化变量；Pythia-410M 作为参考模型避免与生成器的规模/架构循环；XGBoost\\n    快速验证无需 GPU 训练。Pass: macro-F1≥0.45 且 gen-0 vs gen-2+ F1≥0.65。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 18:10 UTC\\n  summary: MVP PASS → 进入研究阶段。首要任务：特征 ablation + depth signal 增量验证\\n  rationale: macro-F1=0.84 远超 0.45 阈值，binary F1=0.87 远超 0.65，7/7 特征显著。核心假设成立。但 Reviewer\\n    指出 hapax_ratio（表面特征）贡献最大，需 ablation 验证分布指纹的独立价值；gen-1 vs gen-2+ 混淆率高，需量化 depth\\n    信号超越 binary 分类的增量。\\n  related_experiments:\\n  - exp_id: mvp-001\\n    role: primary\\n    result: 'PASS: macro-F1=0.8408, binary-F1=0.8653'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 18:15 UTC\\n  summary: Claim 2 准备 Plan B framing：若 ablation 显示表面特征足够，叙事从 \\\"independent signal\\\"\\n    调整为 \\\"complementary signal\\\"\\n  rationale: Reviewer 指出 Claim 2 是整个叙事的 single point of failure。MVP 中 hapax_ratio\\n    importance=0.30，表面特征贡献 47%。Plan B 不 kill 项目，只调 framing 强度——从\\\"分布指纹独立于表面统计\\\"降为\\\"分布指纹提供互补信号\\\"，核心叙事转为\\n    vocabulary impoverishment as primary depth signal。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 18:38 UTC\\n  summary: Claim 2 framing 调整：从 \\\"Fingerprint Independence\\\" 转为 \\\"Feature Complementarity\\n    & Dual Dynamics\\\"；H1/H2 从二选一转为共存\\n  rationale: plan_001 ablation 结果：surface_only (0.76) > reference_only (0.72)，但 full\\n    (0.82) 显著优于 surface_only (p=0.0008)。原 Claim 2 \\\"independent signal\\\" 被否定，触发 Plan\\n    B (D003)。新发现更强：表面特征呈 H2 drift、分布形状特征呈 H1 stationary，dual dynamics 是比原 framing\\n    更丰富的科学贡献。\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: primary\\n    result: surface_only 0.76 > reference_only 0.72; full 0.82 显著优于两者; H1/H2 按特征类型共存\\n  depends_on:\\n  - D002\\n  - D003\\n- id: D005\\n  date: 2026-05-14 19:37 UTC\\n  summary: Dual dynamics 细化：H1/H2 分界是 level/diversity vs shape，不是 surface vs reference（entropy_mean\\n    作为 reference 特征却呈 H2 drift）\\n  rationale: plan_001 修正版结果显示 entropy_mean（reference 特征）Spearman ρ=-0.68，呈明显 H2 漂移。原\\n    framing 将 dual dynamics 归因于 surface vs reference 的来源差异，实际分界是特征测量什么（central tendency/diversity\\n    vs distributional shape）。这是更精确、更有科学价值的发现。\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: primary\\n    result: entropy_mean ρ=-0.68 (H2), entropy_std/max/tail_decay near-stationary\\n      (H1)\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-14 22:14 UTC\\n  summary: 'Dream D006: framing+plan调整 — 重新定位为实证/概念贡献，补充text length控制、大模型生成器、下游评估多种子'\\n  rationale: 'Dream dream_20260514T181213 三档评分 Best=5/Median=5/Worst=4，均未达 best≥6\\n    的启动门槛。跨三档一致的结构性问题：(1) 引用严重不足(5篇→需30+)，缺 OOD detection/perplexity-based detection/model\\n    collapse/data quality 文献线；(2) 方法论新颖性被过度声称——features 是标准 NLL 统计量+XGBoost，贡献在于问题定义+实证发现+应用，非方法；(3)\\n    文本长度混淆未控制(hapax_ratio/TTR 依赖长度)；(4) 生成器规模≤2.8B，缺前沿规模验证；(5) 下游效用单次运行无CI+Pythia-410M循环引用；(6)\\n    OOD detection 连接缺失。\\n\\n\\n    行动：\\n\\n    - paper_framing.md: 添加 RC8-RC11, Contribution Positioning 节，重新定位为实证/概念贡献\\n\\n    - experiment_plan.yaml: 新增 plan_013 (text_length_control, P0), plan_014 (large_scale_generator,\\n    P1)；修改 plan_004 (OLMo-1B替代Pythia-410M, 多种子+CI, 样本量匹配)\\n\\n    - 全局要求：所有实验报告 bootstrap CI\\n\\n    - 需 re-dream 验证改动后评分是否达标，达标后才批准后续 P0 实验\\n\\n    - plan-002 数据生成继续（数据不受 framing 影响）'\\n  related_experiments:\\n  - exp_id: plan_001\\n    role: completed\\n    result: success\\n  - exp_id: plan_002\\n    role: running\\n    result: data generation in progress\\n  - exp_id: plan_013\\n    role: new\\n    result: text length control added\\n  - exp_id: plan_014\\n    role: new\\n    result: large scale generator added\\n  - exp_id: plan_004\\n    role: modified\\n    result: OLMo-1B + multi-seed + CI\\n  depends_on:\\n  - D005\\n\", \"total_chars\": 3727, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92d430b9-7d5e-43b3-be04-fd753a04c718",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "047a0f07-a35f-4fe6-9d84-e1cac5486a8c",
  "sourceToolAssistantUUID": "92d430b9-7d5e-43b3-be04-fd753a04c718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T23:08:10.825Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011Yb2SkieUqqxmUeG3GrLi1`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "047a0f07-a35f-4fe6-9d84-e1cac5486a8c",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JVLy3mhQCayAAiPLeW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b514bb9f-c5a5-48f3-8b41-2121d443b3ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LepUNHRjDCBPUpJarRdZqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 18839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3933,
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

_source line 23 · 2026-05-14T23:08:10.840Z_

<details><summary>↩ Tool result · `toolu_011Yb2SkieUqqxmUeG3GrLi1`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'gen-depth-fingerprint'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b514bb9f-c5a5-48f3-8b41-2121d443b3ca",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "6f32147c-cfa7-4ede-9a69-6b65bf344fe9",
  "sourceToolAssistantUUID": "b514bb9f-c5a5-48f3-8b41-2121d443b3ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-14T23:08:14.085Z_

Now let me read the experiment plan and the actual paper/artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f32147c-cfa7-4ede-9a69-6b65bf344fe9",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JVfvpKkFR5tBc6JrCv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b131f0d-ec8d-4dd8-be03-3b5220b37b43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KrypsptgAuAmXAQiurKnh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5500,
      "cache_read_input_tokens": 22772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5500,
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

_source line 25 · 2026-05-14T23:08:15.480Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UYa7vtrcCk6gDeUTCNsHQy`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b131f0d-ec8d-4dd8-be03-3b5220b37b43",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JVfvpKkFR5tBc6JrCv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56ab2e6d-4011-4216-9c33-68dfd32bb56b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KrypsptgAuAmXAQiurKnh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5500,
      "cache_read_input_tokens": 22772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5500,
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

_source line 26 · 2026-05-14T23:08:15.495Z_

<details><summary>↩ Tool result · `toolu_01UYa7vtrcCk6gDeUTCNsHQy`</summary>

```text
artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/best/review_context.yaml
artifacts/dream_reports/dream_20260514T181213/median/review_context.yaml
artifacts/dream_reports/dream_20260514T181213/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T181213/meta.yaml
artifacts/manifest.yaml
experiment_plan.yaml
decisions.yaml
artifacts/dream_reports/dream_20260514T221538/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T221538/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260514T221538/best/review_context.yaml
artifacts/dream_reports/dream_20260514T221538/median/review_context.yaml
registry.yaml
artifacts/dream_reports/dream_20260514T221538/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56ab2e6d-4011-4216-9c33-68dfd32bb56b",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "67824978-5e36-4eaf-8d89-44265930c0e1",
  "sourceToolAssistantUUID": "56ab2e6d-4011-4216-9c33-68dfd32bb56b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T23:08:15.960Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JpNnE8rmmKnBbvGgyGrwXg`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67824978-5e36-4eaf-8d89-44265930c0e1",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JVfvpKkFR5tBc6JrCv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb7dbfb2-e0af-46f6-8f2e-63be10542705",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KrypsptgAuAmXAQiurKnh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5500,
      "cache_read_input_tokens": 22772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5500,
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

_source line 28 · 2026-05-14T23:08:15.973Z_

<details><summary>↩ Tool result · `toolu_01JpNnE8rmmKnBbvGgyGrwXg`</summary>

```text
artifacts/dream_reports/dream_20260514T181213/best/paper.tex
artifacts/dream_reports/dream_20260514T181213/median/paper.tex
artifacts/dream_reports/dream_20260514T181213/worst/paper.tex
artifacts/dream_reports/dream_20260514T221538/best/paper.tex
artifacts/dream_reports/dream_20260514T221538/median/paper.tex
artifacts/dream_reports/dream_20260514T221538/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb7dbfb2-e0af-46f6-8f2e-63be10542705",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "c014981d-bcf9-4df5-8e7e-2157accd09ea",
  "sourceToolAssistantUUID": "eb7dbfb2-e0af-46f6-8f2e-63be10542705",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T23:08:16.899Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016q4ayVBkQDeXRfjNhVqKjr`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c014981d-bcf9-4df5-8e7e-2157accd09ea",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JVfvpKkFR5tBc6JrCv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55dcb0e2-8f2b-41ec-a29a-07d6db04bacf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KrypsptgAuAmXAQiurKnh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5500,
      "cache_read_input_tokens": 22772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5500,
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

_source line 30 · 2026-05-14T23:08:16.913Z_

<details><summary>↩ Tool result · `toolu_016q4ayVBkQDeXRfjNhVqKjr`</summary>

```text
artifacts/dream_reports/dream_20260514T181213/best/paper.pdf
artifacts/dream_reports/dream_20260514T181213/median/paper.pdf
artifacts/dream_reports/dream_20260514T181213/worst/paper.pdf
artifacts/dream_reports/dream_20260514T221538/best/paper.pdf
artifacts/dream_reports/dream_20260514T221538/median/paper.pdf
artifacts/dream_reports/dream_20260514T221538/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55dcb0e2-8f2b-41ec-a29a-07d6db04bacf",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "ac60cd96-891d-49c0-8259-574dac3e736d",
  "sourceToolAssistantUUID": "55dcb0e2-8f2b-41ec-a29a-07d6db04bacf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T23:08:17.246Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UKnYusKimC5zZPRHUiU53e`</summary>

```json
{
  "pattern": "artifacts/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac60cd96-891d-49c0-8259-574dac3e736d",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JVfvpKkFR5tBc6JrCv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56a856c6-0199-45fd-904b-24c963720056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KrypsptgAuAmXAQiurKnh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5500,
      "cache_read_input_tokens": 22772,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5500
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 356,
          "cache_read_input_tokens": 22772,
          "cache_creation_input_tokens": 5500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5500,
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

_source line 32 · 2026-05-14T23:08:17.256Z_

<details><summary>↩ Tool result · `toolu_01UKnYusKimC5zZPRHUiU53e`</summary>

```text
artifacts/_project/data/generate_chain.py
artifacts/mvp-001/data/mvp_results_pointer.txt
artifacts/dream_reports/dream_20260514T181213/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T181213/logs/phase2_best_attempt0.log
artifacts/ablation_analysis.py
artifacts/dream_reports/dream_20260514T181213/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T181213/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T181213/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json
artifacts/dream_reports/dream_20260514T181213/best/paper_framing.md
artifacts/dream_reports/dream_20260514T181213/best/paper.tex
artifacts/dream_reports/dream_20260514T181213/best/paper.aux
artifacts/dream_reports/dream_20260514T181213/best/paper.out
artifacts/dream_reports/dream_20260514T181213/best/paper.pdf
artifacts/dream_reports/dream_20260514T181213/best/paper.log
artifacts/dream_reports/dream_20260514T181213/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T181213/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/median/experiment_data.json
artifacts/dream_reports/dream_20260514T181213/median/paper_framing.md
artifacts/dream_reports/dream_20260514T181213/median/paper.tex
artifacts/dream_reports/dream_20260514T181213/median/paper.aux
artifacts/dream_reports/dream_20260514T181213/median/paper.out
artifacts/dream_reports/dream_20260514T181213/median/paper.pdf
artifacts/dream_reports/dream_20260514T181213/median/paper.log
artifacts/dream_reports/dream_20260514T181213/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T181213/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T181213/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T181213/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T181213/worst/paper.tex
artifacts/dream_reports/dream_20260514T181213/worst/paper.aux
artifacts/dream_reports/dream_20260514T181213/worst/paper.out
artifacts/dream_reports/dream_20260514T181213/worst/paper.pdf
artifacts/dream_reports/dream_20260514T181213/worst/paper.log
artifacts/dream_reports/dream_20260514T181213/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T181213/best/review_context.yaml
artifacts/dream_reports/dream_20260514T181213/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T181213/best/review_report.md
artifacts/dream_reports/dream_20260514T181213/logs/review_best.log
artifacts/dream_reports/dream_20260514T181213/median/review_context.yaml
artifacts/dream_reports/dream_20260514T181213/median/review_report.md
artifacts/dream_reports/dream_20260514T181213/logs/review_median.log
artifacts/dream_reports/dream_20260514T181213/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T181213/worst/review_report.md
artifacts/dream_reports/dream_20260514T181213/logs/review_worst.log
artifacts/dream_reports/dream_20260514T181213/meta.yaml
artifacts/plan-001-fix/analysis_report.md
artifacts/plan-001-fix/report/analysis_report.md
artifacts/manifest.yaml
artifacts/diag-qwen3-1_7b-sighup.md
artifacts/generate_chain.py
artifacts/dream_reports/dream_20260514T221538/logs/orchestrator.log
artifacts/dream_reports/dream_20260514T221538/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260514T221538/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260514T221538/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260514T221538/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260514T221538/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T221538/best/experiment_data.json
artifacts/dream_reports/dream_20260514T221538/best/paper_framing.md
artifacts/dream_reports/dream_20260514T221538/best/paper.tex
artifacts/dream_reports/dream_20260514T221538/best/paper.aux
artifacts/dream_reports/dream_20260514T221538/best/paper.out
artifacts/dream_reports/dream_20260514T221538/best/paper.pdf
artifacts/dream_reports/dream_20260514T221538/best/paper.log
artifacts/dream_reports/dream_20260514T221538/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T221538/median/experiment_data.json
artifacts/dream_reports/dream_20260514T221538/median/paper_framing.md
artifacts/dream_reports/dream_20260514T221538/median/paper.tex
artifacts/dream_reports/dream_20260514T221538/median/paper.aux
artifacts/dream_reports/dream_20260514T221538/median/paper.out
artifacts/dream_reports/dream_20260514T221538/median/paper.pdf
artifacts/dream_reports/dream_20260514T221538/median/paper.log
artifacts/dream_reports/dream_20260514T221538/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T221538/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T221538/worst/experiment_data.json
artifacts/dream_reports/dream_20260514T221538/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T221538/worst/paper.tex
artifacts/dream_reports/dream_20260514T221538/worst/paper.aux
artifacts/dream_reports/dream_20260514T221538/worst/paper.out
artifacts/dream_reports/dream_20260514T221538/worst/paper.pdf
artifacts/dream_reports/dream_20260514T221538/worst/paper.log
artifacts/dream_reports/dream_20260514T221538/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260514T221538/best/review_context.yaml
artifacts/dream_reports/dream_20260514T221538/best/review_report.md
artifacts/dream_reports/dream_20260514T221538/logs/review_best.log
artifacts/dream_reports/dream_20260514T221538/median/review_context.yaml
artifacts/dream_reports/dream_20260514T221538/median/review_report.md
artifacts/dream_reports/dream_20260514T221538/logs/review_median.log
artifacts/dream_reports/dream_20260514T221538/worst/review_context.yaml
artifacts/dream_reports/dream_20260514T221538/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56a856c6-0199-45fd-904b-24c963720056",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "e955bd8e-5db5-4566-883a-2aeae2ea6042",
  "sourceToolAssistantUUID": "56a856c6-0199-45fd-904b-24c963720056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-14T23:08:23.020Z_

Let me read the most recent dream's paper (the "median" version is typically the primary), the experiment plan, and the imagined experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e955bd8e-5db5-4566-883a-2aeae2ea6042",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JW97wffPhDeNzdJUky",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8242af64-346e-404d-a868-01d283ea0814",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbkuLbzoHc4QwmAmG43CS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 28272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3015,
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

_source line 34 · 2026-05-14T23:08:24.915Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RZxD7Dy97U4qnMzucD8Rep`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8242af64-346e-404d-a868-01d283ea0814",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JW97wffPhDeNzdJUky",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4381fd7-c990-41f0-b019-96b44f359096",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbkuLbzoHc4QwmAmG43CS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 28272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3015,
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

_source line 35 · 2026-05-14T23:08:24.919Z_

<details><summary>↩ Tool result · `toolu_01RZxD7Dy97U4qnMzucD8Rep`</summary>

```text
1	experiments:
2	  # === P0: Must-run experiments (headline results) ===
3	
4	  - id: plan_001
5	    claim: 2
6	    name: feature_ablation_and_trend
7	    description: >
8	      Three-part analysis on existing MVP data (zero new generation):
9	      (A) Feature ablation: reference-model-only features (entropy_mean/std/min/max + tail_decay)
10	      vs surface-only features (TTR + hapax_ratio) vs full feature set. XGBoost 5-fold CV for each.
11	      (B) H1/H2 trend analysis: plot each feature's mean ± std across depth 0-4. Monotonic trend → H2 (divergence);
12	      plateau → H1 (convergence). Fit linear regression per feature, report slope + R².
13	      (C) Perplexity pre-validation for Claim 3: compute Pythia-410M perplexity on depth-stratified subsets
14	      (no fine-tuning, just forward pass). If perplexity varies significantly with depth → Claim 3 signal exists.
15	    priority: P0
16	    gpu_budget_hours: 1
17	    deps: [mvp-001]
18	    notes: >
19	      Uses existing MVP data + features.csv. Critical for Claim 2.
20	      Plan B if surface-only ≈ full: reframe Claim 2 as "complementary signal" instead of "independent signal",
21	      narrative shifts to "vocabulary impoverishment as primary depth signal".
22	
23	  - id: plan_002
24	    claim: 1
25	    name: cross_generator_evaluation
26	    description: >
27	      Expand to 5 generators: Pythia-2.8B, Pythia-1B, OLMo-2-0425-1B (1485M),
28	      Qwen3-1.7B-Base, Qwen3-0.6B-Base. (Qwen3.5 不存在，用 Qwen3-Base 替代。)
29	      Leave-one-generator-out CV to test cross-generator generalization.
30	      1000 seeds × 5 generators × 5 depths = 25K chains.
31	    priority: P0
32	    gpu_budget_hours: 20
33	    deps: [plan_001]
34	    notes: >
35	      Only proceed if plan_001 confirms reference features have independent or complementary value.
36	      Pythia family overlap (2.8B + 1B): supplement with leave-one-family-out evaluation in analysis.
37	      Discuss limitation in paper if Pythia holdout performance inflated by Pythia-1B in training set.
38	
39	  - id: plan_003
40	    claim: 2
41	    name: cross_family_reference_model
42	    description: >
43	      Test non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B-Base) for feature extraction.
44	      Addresses RC2 + critical test of Claim 2: verify entropy_mean H2 drift persists
45	      with non-Pythia reference (if drift disappears → "dual dynamics" is reference-model artifact,
46	      not generation-intrinsic). Also verify shape features remain H1 across reference models.
47	    priority: P0
48	    gpu_budget_hours: 8
49	    deps: [plan_002]
50	    notes: >
51	      Importance elevated after D005: this is now the key falsification test for Claim 2's
52	      level/shape framework. If entropy_mean drift is Pythia-specific, the entire dual dynamics
53	      narrative collapses.
54	
55	  - id: plan_004
56	    claim: 3
57	    name: downstream_utility
58	    description: >
59	      RQ4: Fine-tune OLMo-1B (NOT Pythia-410M — avoid reference model circularity)
60	      on depth-stratified data subsets. Measure perplexity degradation on held-out test
61	      set as function of training data depth. Compare depth-aware filtering vs binary
62	      baselines (FastDetectGPT, LD-Score threshold). Must run ≥3 random seeds with
63	      bootstrap CIs. Include sample-count-matched comparison (subsample depth-filtered
64	      to match binary-filtered count) to control for data size confound.
65	    priority: P0
66	    gpu_budget_hours: 20
67	    deps: [plan_002]
68	    notes: >
69	      Dream review flagged: (1) single-run without CIs, (2) Pythia-410M circularity,
70	      (3) data size confound. All three addressed in updated design.
71	
72	  # === P1: Important for story completeness ===
73	
74	  - id: plan_005
75	    claim: 1
76	    name: prompt_type_comparison
77	    description: >
78	      RQ2 partial: Compare continuation vs elaboration vs inspired_rewriting chains.
79	      Tests whether semantic divergence from source correlates with depth signal preservation.
80	      Same 1000 seeds, Pythia-2.8B, 3 prompt types.
81	    priority: P1
82	    gpu_budget_hours: 10
83	    deps: [plan_001]
84	
85	  - id: plan_006
86	    claim: 1
87	    name: paraphrastic_comparison
88	    description: >
89	      RQ2 full: Construct parallel paraphrasing chains for direct comparison with continuation chains.
90	      Tests attractor convergence theory — do non-paraphrastic chains preserve more depth signal?
91	    priority: P1
92	    gpu_budget_hours: 8
93	    deps: [plan_005]
94	
95	  - id: plan_007
96	    claim: 1
97	    name: cross_model_chains
98	    description: >
99	      RQ3: Cross-model chains (different generator per depth step) vs single-model chains.
100	      More realistic scenario — web contamination involves diverse generators.
101	    priority: P1
102	    gpu_budget_hours: 12
103	    deps: [plan_002]
104	
105	  - id: plan_008
106	    claim: 1
107	    name: multi_domain_seeds
108	    description: >
109	      Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts),
110	      creative writing (WritingPrompts). 500 seeds per domain × 5 depths.
111	    priority: P1
112	    gpu_budget_hours: 10
113	    deps: [plan_002]
114	
115	  # === P2: Nice-to-have / strengthen claims ===
116	
117	  - id: plan_009
118	    claim: 1
119	    name: finer_grained_ordinal
120	    description: >
121	      Secondary analysis: 5-class ordinal classification (gen-0 through gen-4)
122	      on non-paraphrastic chains. Tests if more depth signal exists beyond 3-class.
123	    priority: P2
124	    gpu_budget_hours: 1
125	    deps: [plan_002]
126	
127	  - id: plan_010
128	    claim: 1
129	    name: human_edit_robustness
130	    description: >
131	      RC5: Robustness to simulated human edits.
132	      (A) Random word replacement (5%, 10%, 20%) as lower-bound.
133	      (B) LLM-simulated editing (light rephrasing of random sentences).
134	    priority: P2
135	    gpu_budget_hours: 5
136	    deps: [plan_002]
137	
138	  - id: plan_011
139	    claim: 2
140	    name: ld_score_feature
141	    description: >
142	      Add LD-Score (character-distribution signature from arXiv:2605.01647) as additional feature.
143	      Tests whether character-level features provide complementary depth signal.
144	    priority: P2
145	    gpu_budget_hours: 2
146	    deps: [plan_001]
147	
148	  - id: plan_012
149	    claim: 1
150	    name: end_to_end_classifier
151	    description: >
152	      QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.
153	      Compares learned representations vs handcrafted distributional features.
154	    priority: P2
155	    gpu_budget_hours: 15
156	    deps: [plan_002]
157	
158	  - id: plan_013
159	    claim: [1, 2]
160	    name: text_length_control
161	    description: >
162	      Address text length confound (RC10, dream all three tiers):
163	      (A) Analyze text length distributions by depth across all generators.
164	      (B) Compute length-normalized surface features (TTR, hapax_ratio on fixed-length windows).
165	      (C) Length-matched comparison: subsample to equalize length distributions across depths,
166	      re-evaluate classifier. If length-controlled F1 drops significantly → surface features
167	      were tracking length, not depth.
168	    priority: P0
169	    gpu_budget_hours: 0.5
170	    deps: [plan_002]
171	    notes: >
172	      Zero new generation — analysis on existing data. Critical confound control
173	      flagged by dream (all three tiers). Low cost, high impact on paper credibility.
174	
175	  - id: plan_014
176	    claim: 1
177	    name: large_scale_generator
178	    description: >
179	      Add one 7B+ generator (Qwen3-8B-Base or similar) to test whether depth signal
180	      persists at frontier scale. 1000 seeds × 5 depths. Addresses RC9: all current
181	      generators ≤2.8B. RTX 5090 (32GB) can run 8B model at FP16 (~16GB weights).
182	    priority: P1
183	    gpu_budget_hours: 8
184	    deps: [plan_002]
185	    notes: >
186	      Dream review flagged ≤2.8B as major limitation (all three tiers).
187	      If depth signal weaker at scale → honest limitation with analysis.
188	      If comparable → strong generalization evidence for the paper.
189	
190	# Global requirement (dream D006): ALL experiments must report bootstrap CIs on main metrics.
191	
192	# GPU Budget Summary:
193	# P0: ~45.5 GPU·hours (was 44, +0.5 text_length, +5 downstream seeds)
194	# P1: ~48 GPU·hours (was 40, +8 large_scale_generator)
195	# P2: ~23 GPU·hours
196	# Total: ~116.5 GPU·hours (within 200 H100-hour budget)
197	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4381fd7-c990-41f0-b019-96b44f359096",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "adcb767a-d142-414f-ad78-7734791859c3",
  "sourceToolAssistantUUID": "e4381fd7-c990-41f0-b019-96b44f359096",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T23:08:27.174Z_

<details open><summary>🔧 Tool call — Read · `toolu_019pteFknnDxy8FzxiTVWBjh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adcb767a-d142-414f-ad78-7734791859c3",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JW97wffPhDeNzdJUky",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b70ace95-da8a-40ea-8e93-2330fca2c9dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbkuLbzoHc4QwmAmG43CS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 28272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3015,
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

_source line 37 · 2026-05-14T23:08:27.185Z_

<details open><summary>🔧 Tool call — Read · `toolu_0147Koa52C11aMFuXT1aNFmP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b70ace95-da8a-40ea-8e93-2330fca2c9dd",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JW97wffPhDeNzdJUky",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b45d6cc7-2ccd-49a8-9b6b-6a8a45fab4ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbkuLbzoHc4QwmAmG43CS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 28272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3015,
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

_source line 38 · 2026-05-14T23:08:27.423Z_

<details><summary>↩ Tool result · `toolu_019pteFknnDxy8FzxiTVWBjh`</summary>

```text
1	\documentclass[letterpaper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{amsmath,amssymb,amsfonts}
4	\usepackage{booktabs}
5	\usepackage{multirow}
6	\usepackage{graphicx}
7	\usepackage{xcolor}
8	\usepackage{hyperref}
9	\usepackage{natbib}
10	\usepackage{array}
11	\usepackage{caption}
12	
13	\title{Distributional Fingerprinting for Generation Depth Estimation\\in Recursive LLM Output}
14	
15	\author{Anonymous}
16	\date{}
17	
18	\begin{document}
19	\maketitle
20	
21	% ============================================================
22	\begin{abstract}
23	Web-scraped training corpora increasingly contain LLM-generated text whose \emph{provenance depth}---how many successive generation steps separate it from the original human text---is unknown.
24	Current detectors offer only binary real-vs-synthetic labels, forcing all-or-nothing filtering that discards useful near-human content or admits deeply degraded text.
25	We formulate \textbf{generation depth estimation} as an ordinal classification task and propose a lightweight feature set combining surface diversity statistics with reference-model NLL summary statistics.
26	On continuation chains from six generators (0.6B--8B parameters) across four text domains, our features achieve macro-F1 0.82 for 3-class depth estimation (gen-0\,/\,gen-1\,/\,gen-2+) within-generator and 0.64 under leave-one-generator-out evaluation.
27	We discover \textbf{reference-model-modulated dual dynamics}: level/diversity features (entropy mean, TTR, hapax ratio) drift monotonically with depth while distributional shape features (entropy std, tail decay) remain near-stationary---a split determined by \emph{what} the feature measures, not whether it derives from surface text or a reference model.
28	This dual pattern persists across reference models (though drift magnitude varies ${\sim}2\times$), prompt types, and text domains.
29	Depth-aware data filtering improves downstream fine-tuning perplexity by 5.2\% over unfiltered data, offering complementary signal to binary detection baselines.
30	We provide honest analysis of limitations: cross-generator generalization is moderate (LOGO F1 ${\sim}$0.64), signal weakens at 7B+ scale (F1 0.57), and depth estimation is sensitive to heavy post-editing.
31	\end{abstract}
32	
33	% ============================================================
34	\section{Introduction}
35	\label{sec:intro}
36	
37	Large language models are now prolific content generators on the open web.
38	As web-scraped corpora feed back into model training, the recursive loop produces text at varying \emph{generation depths}: depth-0 text is human-authored, depth-1 is generated from a human seed, depth-2 is generated from depth-1 output, and so on.
39	Model collapse theory demonstrates that training on such recursively generated data degrades model quality, with deeper-generation text contributing disproportionately to distributional drift.
40	
41	Existing detection methods---FastDetectGPT, SynthID-Text, LD-Score, Binoculars---provide binary real-vs-synthetic labels.
42	This binary view forces a coarse filtering strategy: discard all flagged text (losing useful gen-1 content that closely resembles human writing) or keep everything (admitting high-risk deep-generation text with compounding artifacts).
43	A more nuanced approach would \emph{estimate} generation depth, enabling risk-stratified data curation that retains near-human content while filtering deeply degraded text.
44	
45	Attractor cycle theory for paraphrasing chains shows that iterative paraphrasing converges to 2-period cycles, bounding distinguishable depth to ${\sim}$3 classes.
46	However, this result depends on the semantic-preservation constraint inherent to paraphrasing.
47	Non-paraphrastic generation (continuation, elaboration) escapes this constraint, potentially supporting richer depth signal.
48	
49	We make three contributions:
50	
51	\begin{enumerate}
52	\item \textbf{Problem formulation.} We define generation depth estimation as an ordinal classification task and construct multi-generator, multi-domain evaluation benchmarks with systematic controls.
53	
54	\item \textbf{Empirical discovery: reference-model-modulated dual dynamics.} We show that distributional features split into two families by \emph{what they measure}---level/diversity features drift with depth (H$_2$) while shape features remain stationary (H$_1$)---a split that cross-cuts the surface/reference boundary. This dual pattern is modulated by reference model choice: entropy mean drift attenuates from $|\rho|{=}0.68$ (same-family reference) to $|\rho|{\sim}0.4$ (cross-family reference), but the level-vs-shape split itself is preserved.
55	
56	\item \textbf{Practical application.} Depth-aware filtering provides complementary signal to binary detection for downstream data curation, with a 5.2\% perplexity improvement over unfiltered training data.
57	\end{enumerate}
58	
59	Our contribution is primarily empirical and conceptual.
60	The features (NLL summary statistics, lexical diversity) and classifier (gradient-boosted trees) are standard; the novelty lies in the problem formulation, the empirical finding of dual dynamics, and the application to risk-stratified curation.
61	
62	% ============================================================
63	\section{Related Work}
64	\label{sec:related}
65	
66	\paragraph{Synthetic text detection.}
67	Perplexity-based methods detect machine-generated text via reference-model statistics: GLTR uses token-rank histograms, DetectGPT exploits log-probability curvature, Fast-DetectGPT replaces perturbation with conditional probability, Binoculars uses cross-model perplexity ratios, and DNA-GPT leverages divergent n-gram analysis.
68	These methods provide binary labels without depth information.
69	
70	\paragraph{Model collapse and recursive generation.}
71	Theoretical work demonstrates that training on model-generated data induces distributional collapse.
72	Alemohammad et al.\ show autophagous loops amplify bias; Dohmatob et al.\ characterize the curse of recursion in Gaussian settings; Gerstgrasser et al.\ extend results to LLMs; Guo et al.\ quantify vocabulary impoverishment under recursive generation.
73	These results motivate depth estimation: not all synthetic text is equally harmful.
74	
75	\paragraph{Attractor cycles.}
76	Recent work proves that iterated paraphrasing converges to short-period cycles, bounding the distinguishable depth of paraphrastic chains.
77	We complement this theory by studying non-paraphrastic chains where the attractor bound does not apply (Section~\ref{sec:paraphrastic}).
78	
79	\paragraph{Data quality scoring.}
80	Methods like DSIR, QuRating, and CCNet score training data quality for filtering.
81	Our depth estimation provides a complementary contamination-risk signal orthogonal to topic/quality scores.
82	
83	\paragraph{Lexical diversity and OOD detection.}
84	Our surface features (TTR, hapax ratio) connect to vocabulary diversity metrics studied in computational linguistics.
85	Reference-model NLL statistics are functionally related to OOD detection scores.
86	Our contribution is not the features themselves but the discovery that they exhibit dual dynamics under recursive generation and their application to ordinal depth estimation.
87	
88	% ============================================================
89	\section{Method}
90	\label{sec:method}
91	
92	\subsection{Problem Formulation}
93	Given a text passage $x$ of unknown provenance, we aim to predict its \emph{generation depth} $d \in \{0, 1, 2+\}$, where $d{=}0$ denotes human-authored text and $d{=}k$ ($k{\geq}1$) denotes text produced by the $k$-th step of a recursive LLM generation chain.
94	We frame this as ordinal classification with three ordered classes: gen-0, gen-1, and gen-2+.
95	
96	\subsection{Generation Chain Construction}
97	\label{sec:chains}
98	Starting from human-authored seed texts (depth-0), we construct generation chains by iteratively prompting an LLM to continue the previous output.
99	Each chain produces texts at depths 0 through 4.
100	We use six generators spanning three model families: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, and Qwen3-8B.
101	Seed texts are drawn from four domains: Wikipedia, news (CNN/DailyMail), scientific abstracts (S2ORC), and creative writing (WritingPrompts).
102	
103	\subsection{Feature Extraction}
104	\label{sec:features}
105	We extract seven features from each text passage, organized by the dual dynamics framework:
106	
107	\paragraph{H$_2$ (level/drift) features.}
108	These features measure central tendency or diversity and drift monotonically with depth:
109	\begin{itemize}
110	\item \texttt{entropy\_mean}: Mean per-token NLL under a reference model (Pythia-410M). Despite being a reference-model feature, it drifts because it measures the \emph{level} (central tendency) of the NLL distribution.
111	\item \texttt{TTR}: Type-token ratio, measuring vocabulary diversity.
112	\item \texttt{hapax\_ratio}: Proportion of words appearing exactly once.
113	\end{itemize}
114	
115	\paragraph{H$_1$ (shape/stationary) features.}
116	These features measure distributional shape and remain near-stationary across depths:
117	\begin{itemize}
118	\item \texttt{entropy\_std}: Standard deviation of per-token NLL.
119	\item \texttt{entropy\_max}: Maximum per-token NLL.
120	\item \texttt{tail\_decay}: Rate of NLL distribution tail decay.
121	\item \texttt{entropy\_min}: Minimum per-token NLL.
122	\end{itemize}
123	
124	\subsection{Classifier}
125	We use XGBoost with 5-fold stratified cross-validation.
126	For cross-generator evaluation, we employ leave-one-generator-out (LOGO) and leave-one-family-out (LOFO) protocols.
127	All reported metrics are macro-averaged F1 with bootstrap 95\% confidence intervals from 1000 resamples.
128	
129	% ============================================================
130	\section{Experiments}
131	\label{sec:experiments}
132	
133	\subsection{Feature Ablation and Dual Dynamics (Within-Generator)}
134	\label{sec:ablation}
135	
136	We first validate the feature set and dual dynamics hypothesis on a controlled within-generator setting: Pythia-2.8B as generator, Pythia-410M as reference model, $N{=}4{,}609$ chain samples.
137	
138	\paragraph{Feature ablation.}
139	Table~\ref{tab:ablation} reports 3-class depth classification results.
140	The full 7-feature set achieves macro-F1 0.82 [0.804, 0.836], significantly outperforming both surface-only (TTR + hapax; F1 0.76 [0.747, 0.774]) and reference-only (5 NLL statistics; F1 0.72 [0.706, 0.733]).
141	The non-overlapping bootstrap CIs confirm that combining drifting and stationary features yields statistically significant improvement over either alone.
142	
143	\begin{table}[h]
144	\centering
145	\caption{Feature ablation (5-fold CV, Pythia-2.8B generator, $N{=}4{,}609$).}
146	\label{tab:ablation}
147	\begin{tabular}{lcccc}
148	\toprule
149	Feature Set & Macro-F1 & 95\% CI & Gen-0 & Gen-1 \\
150	\midrule
151	Full (7 features) & 0.82 & [0.804, 0.836] & 0.94 & 0.77 \\
152	Surface only (TTR + hapax) & 0.76 & [0.747, 0.774] & 0.91 & 0.70 \\
153	Reference only (5 NLL) & 0.72 & [0.706, 0.733] & 0.88 & 0.65 \\
154	Chance baseline & 0.33 & --- & 0.33 & 0.33 \\
155	\bottomrule
156	\end{tabular}
157	\end{table}
158	
159	\paragraph{H$_1$/H$_2$ trend analysis.}
160	Table~\ref{tab:trends} reports per-feature linear regression of feature values against depth.
161	H$_2$ features exhibit strong monotonic drift: entropy\_mean ($R^2{=}0.93$, slope $-0.148$), TTR ($R^2{=}0.87$, slope $-0.071$), hapax\_ratio ($R^2{=}0.81$, slope $-0.054$), all with $p{<}0.001$.
162	H$_1$ features show negligible trends: entropy\_std ($R^2{=}0.02$), entropy\_max ($R^2{=}0.04$), tail\_decay ($R^2{=}0.03$), entropy\_min ($R^2{=}0.06$), all with $p{>}0.19$.
163	This confirms the dual dynamics split.
164	
165	\begin{table}[h]
166	\centering
167	\caption{H$_1$/H$_2$ trend regression per feature (Pythia-2.8B chains).}
168	\label{tab:trends}
169	\begin{tabular}{lcccc}
170	\toprule
171	Feature & Slope & $R^2$ & $p$-value & Class \\
172	\midrule
173	entropy\_mean & $-0.148$ & 0.93 & ${<}0.001$ & H$_2$ (drift) \\
174	TTR & $-0.071$ & 0.87 & ${<}0.001$ & H$_2$ (drift) \\
175	hapax\_ratio & $-0.054$ & 0.81 & ${<}0.001$ & H$_2$ (drift) \\
176	\midrule
177	entropy\_std & $+0.003$ & 0.02 & $0.41$ & H$_1$ (stationary) \\
178	entropy\_max & $-0.009$ & 0.04 & $0.28$ & H$_1$ (stationary) \\
179	tail\_decay & $+0.005$ & 0.03 & $0.33$ & H$_1$ (stationary) \\
180	entropy\_min & $-0.012$ & 0.06 & $0.19$ & H$_1$ (stationary) \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	Median perplexity by depth (13.5, 4.96, 3.00, 2.07, 1.72 for gen-0 through gen-4; Kruskal--Wallis $p{<}0.001$) confirms that the reference model's surprise decreases monotonically with depth---deeper-generation text becomes more predictable as it converges toward the generator's mode.
186	
187	% ----------------------------------------------------------
188	\subsection{Cross-Generator Generalization}
189	\label{sec:cross_gen}
190	
191	We evaluate on five generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B) with 1{,}000 seeds per generator $\times$ 5 depths, yielding 21{,}503 chains after quality-based attrition from 23{,}847 generated.
192	
193	\paragraph{Leave-one-generator-out (LOGO).}
194	Table~\ref{tab:logo} reports LOGO results.
195	Mean LOGO F1 is 0.64, confirming moderate cross-generator generalization.
196	Pythia-family holdouts achieve higher F1 (0.71--0.72) because the remaining Pythia generator provides an in-family proxy; OLMo and Qwen holdouts score lower (0.59--0.62).
197	
198	\begin{table}[h]
199	\centering
200	\caption{Leave-one-generator-out results (full features).}
201	\label{tab:logo}
202	\begin{tabular}{llcccc}
203	\toprule
204	Held-out Generator & Family & F1 & Gen-0 & Gen-1 & Gen-2+ \\
205	\midrule
206	Pythia-2.8B & Pythia & 0.71 & 0.87 & 0.64 & 0.66 \\
207	Pythia-1B & Pythia & 0.72 & 0.88 & 0.66 & 0.67 \\
208	OLMo-2-1B & OLMo & 0.60 & 0.79 & 0.51 & 0.53 \\
209	Qwen3-1.7B & Qwen & 0.62 & 0.82 & 0.53 & 0.55 \\
210	Qwen3-0.6B & Qwen & 0.59 & 0.78 & 0.50 & 0.51 \\
211	\midrule
212	\textbf{Mean LOGO} & --- & \textbf{0.64} & 0.83 & 0.57 & 0.58 \\
213	\bottomrule
214	\end{tabular}
215	\end{table}
216	
217	\paragraph{Leave-one-family-out (LOFO).}
218	LOFO evaluates generalization when no same-family generator remains in training: Pythia family F1 0.58 [0.55, 0.61], OLMo F1 0.61 [0.57, 0.64], Qwen F1 0.59 [0.56, 0.62], mean 0.593.
219	The ${\sim}$0.05 LOFO--LOGO gap quantifies the within-family transfer advantage.
220	
221	\paragraph{Feature ablation under LOGO.}
222	Under LOGO, the full-vs-surface gap narrows from 0.06 (within-generator) to 0.03 (LOGO F1: full 0.64, surface-only 0.61, reference-only 0.58).
223	This suggests the Pythia-410M reference model's advantage is partially family-specific.
224	
225	% ----------------------------------------------------------
226	\subsection{Reference Model Modulation of Dual Dynamics}
227	\label{sec:cross_ref}
228	
229	To test whether dual dynamics depends on reference model choice, we recompute NLL features using OLMo-2-1B and Qwen3-0.6B as alternative reference models on the same chain data.
230	
231	\paragraph{Drift attenuation.}
232	Table~\ref{tab:ref_drift} shows entropy\_mean drift across references.
233	The Spearman $\rho$ attenuates from $-0.68$ (Pythia-410M, same-family) to $-0.42$ (OLMo-2-1B) and $-0.36$ (Qwen3-0.6B), all $p{<}0.001$.
234	The drift is real and universal---deeper text is always more predictable to \emph{any} reference model---but the measurement sensitivity depends on reference--generator alignment.
235	
236	\begin{table}[h]
237	\centering
238	\caption{Entropy\_mean drift ($\rho$) by reference model.}
239	\label{tab:ref_drift}
240	\begin{tabular}{lccc}
241	\toprule
242	Reference Model & $\rho$ (entropy\_mean) & $p$-value & Full F1 \\
243	\midrule
244	Pythia-410M & $-0.68$ & ${<}0.001$ & 0.82 \\
245	OLMo-2-1B & $-0.42$ & ${<}0.001$ & 0.78 \\
246	Qwen3-0.6B & $-0.36$ & ${<}0.001$ & 0.76 \\
247	\bottomrule
248	\end{tabular}
249	\end{table}
250	
251	\paragraph{Shape stationarity preserved.}
252	Shape features remain H$_1$ across all reference models: max $|\rho|$ is 0.08 (Pythia-410M), 0.11 (OLMo-2-1B), and 0.09 (Qwen3-0.6B).
253	The level-vs-shape split is intrinsic to what the feature measures, not an artifact of reference model choice.
254	
255	Cross-reference LOGO F1 with non-Pythia references (OLMo-ref: 0.61; Qwen-ref: 0.58) shows depth estimation remains viable with any reference model, though at reduced accuracy.
256	
257	% ----------------------------------------------------------
258	\subsection{Text Length Confound Analysis}
259	\label{sec:length}
260	
261	Text length decreases monotonically with depth (mean tokens: 315, 289, 263, 246, 237 for gen-0 through gen-4; Pearson $r{=}-0.41$, $p{<}0.001$), creating a potential confound for length-sensitive surface features.
262	
263	\paragraph{Length-controlled classification.}
264	Table~\ref{tab:length_control} reports results after length normalization and length-matched subsampling.
265	Surface-only F1 drops by 0.05 (from 0.76 to 0.71), confirming that ${\sim}$30\% of the surface signal tracked length.
266	Reference-only features are relatively robust ($-0.02$).
267	Crucially, full-feature F1 after length control remains at 0.78---well above chance and above either feature subset---confirming that depth drives genuine distributional drift beyond length artifacts.
268	
269	\begin{table}[h]
270	\centering
271	\caption{Length-controlled classification results.}
272	\label{tab:length_control}
273	\begin{tabular}{lcccc}
274	\toprule
275	Feature Set & Original F1 & Controlled F1 & $\Delta$ & $\Delta$\% \\
276	\midrule
277	Full & 0.82 & 0.78 & $-0.04$ & $-4.9$\% \\
278	Surface only & 0.76 & 0.71 & $-0.05$ & $-6.6$\% \\
279	Reference only & 0.72 & 0.70 & $-0.02$ & $-2.8$\% \\
280	\bottomrule
281	\end{tabular}
282	\end{table}
283	
284	Fixed-window analysis (128-token windows) reduces TTR slope by 32\% ($-0.071 \to -0.048$) and hapax slope by 31\% ($-0.054 \to -0.037$), while entropy\_mean slope is barely affected ($-0.148 \to -0.139$, 6\% reduction).
285	This confirms that reference-model features provide length-robust depth signal.
286	
287	% ----------------------------------------------------------
288	\subsection{Prompt Type and Chain Type Variations}
289	\label{sec:prompt}
290	
291	\paragraph{Prompt types.}
292	Table~\ref{tab:prompt} compares depth classification across three prompting strategies on Pythia-2.8B chains.
293	Continuation yields the strongest signal (F1 0.82, $\rho{=}-0.68$); elaboration is moderate (F1 0.77, $\rho{=}-0.57$); inspired rewriting is weakest (F1 0.69, $\rho{=}-0.39$).
294	The monotonic decrease tracks semantic divergence from source (cosine similarity: 0.85, 0.72, 0.54).
295	H$_1$ features remain stable across all prompt types.
296	
297	\begin{table}[h]
298	\centering
299	\caption{Depth classification by prompt type (Pythia-2.8B, 5-fold CV).}
300	\label{tab:prompt}
301	\begin{tabular}{lcccc}
302	\toprule
303	Prompt Type & Macro-F1 & $\rho$ (ent\_mean) & TTR slope & Sem.\ div.\ $\cos$ \\
304	\midrule
305	Continuation & 0.82 & $-0.68$ & $-0.071$ & 0.85 \\
306	Elaboration & 0.77 & $-0.57$ & $-0.058$ & 0.72 \\
307	Inspired rewriting & 0.69 & $-0.39$ & $-0.031$ & 0.54 \\
308	\bottomrule
309	\end{tabular}
310	\end{table}
311	
312	\paragraph{Paraphrastic vs non-paraphrastic chains.}
313	\label{sec:paraphrastic}
314	Paraphrastic chains hit the attractor bound at depth ${\sim}$2, yielding 3-class F1 of only 0.66 (vs 0.82 for non-paraphrastic).
315	The gen-2+ F1 collapses to 0.41 (vs 0.79), and entropy\_mean $\rho$ attenuates to $-0.34$ (vs $-0.68$).
316	This validates our focus on non-paraphrastic chains: the attractor convergence bound constrains paraphrasing but not continuation.
317	
318	\paragraph{Cross-model chains.}
319	When different generators produce each depth step (mimicking realistic web contamination), LOGO F1 drops from 0.64 to 0.56.
320	The generator-switching noise partially masks depth signal, particularly for gen-1 vs gen-2+ (F1: 0.46 and 0.44).
321	Gen-0 identification remains robust (F1 0.78) because all chains share human seeds.
322	H$_1$ features remain stable even under cross-model chains.
323	
324	% ----------------------------------------------------------
325	\subsection{Multi-Domain Evaluation}
326	\label{sec:domain}
327	
328	Table~\ref{tab:domain} reports LOGO results across four seed domains.
329	Wikipedia yields the highest F1 (0.67), consistent with its stylistic uniformity; creative writing is hardest (F1 0.57) due to high intrinsic variance.
330	Pooled multi-domain LOGO F1 is 0.63 with moderate cross-domain variability (std 0.037).
331	Cross-domain train-test (train on 3 domains, test on 1) drops to 0.58, indicating partial domain adaptation.
332	
333	\begin{table}[h]
334	\centering
335	\caption{Domain-specific LOGO results.}
336	\label{tab:domain}
337	\begin{tabular}{lcccc}
338	\toprule
339	Domain & LOGO F1 & $\rho$ (ent\_mean) & TTR slope & Seeds \\
340	\midrule
341	Wikipedia & 0.67 & $-0.72$ & $-0.078$ & 500 \\
342	News (CNN/DM) & 0.64 & $-0.63$ & $-0.065$ & 500 \\
343	Scientific (S2ORC) & 0.62 & $-0.58$ & $-0.059$ & 500 \\
344	Creative (WritingPrompts) & 0.57 & $-0.48$ & $-0.041$ & 500 \\
345	\midrule
346	Pooled & 0.63 & $-0.60$ & $-0.061$ & 2000 \\
347	\bottomrule
348	\end{tabular}
349	\end{table}
350	
351	% ----------------------------------------------------------
352	\subsection{Finer-Grained Ordinal Classification}
353	\label{sec:ordinal}
354	
355	Extending to 5-class ordinal classification (gen-0 through gen-4) under LOGO yields macro-F1 0.43.
356	Gen-0 is still well-separated (F1 0.73), gen-1 is intermediate (0.52), but gen-2/3/4 collapse into a cluster (F1: 0.35, 0.29, 0.28).
357	Errors are predominantly between adjacent classes (61\% of misclassifications).
358	Despite low per-class accuracy for deep generations, ordinal Spearman correlation between predicted and true depth is 0.74, showing the classifier preserves depth ordering---useful for risk scoring even when exact classification fails.
359	The 3-class grouping (gen-0\,/\,gen-1\,/\,gen-2+) appears to be the natural resolution supported by the current feature set.
360	
361	% ----------------------------------------------------------
362	\subsection{Robustness to Human Editing}
363	\label{sec:robustness}
364	
365	Table~\ref{tab:edit} reports robustness to simulated post-editing.
366	At 5\% random word replacement, F1 drops only 0.03 (to 0.79).
367	At 10\%, the drop is more substantial ($-0.10$).
368	At 20\%, depth signal degrades significantly ($-0.22$, F1 0.60).
369	LLM-simulated light rephrasing (${\sim}$8\% effective edit rate) produces a $-0.09$ drop (F1 0.73), falling between the 5\% and 10\% random replacement conditions.
370	Shape features remain robust across all conditions (max $|\rho|$ change: 0.07).
371	Real-world human editing likely falls in the 5--15\% range, placing expected operational F1 at 0.72--0.79.
372	
373	\begin{table}[h]
374	\centering
375	\caption{Robustness to simulated human edits (Pythia-2.8B, within-generator).}
376	\label{tab:edit}
377	\begin{tabular}{llccc}
378	\toprule
379	Edit Type & Rate & Macro-F1 & $\Delta$ F1 & $\rho$ (ent\_mean) \\
380	\midrule
381	None (baseline) & 0\% & 0.82 & --- & $-0.68$ \\
382	Random word & 5\% & 0.79 & $-0.03$ & $-0.63$ \\
383	Random word & 10\% & 0.72 & $-0.10$ & $-0.52$ \\
384	Random word & 20\% & 0.60 & $-0.22$ & $-0.35$ \\
385	LLM light rephrase & ${\sim}$8\% & 0.73 & $-0.09$ & $-0.49$ \\
386	\bottomrule
387	\end{tabular}
388	\end{table}
389	
390	% ----------------------------------------------------------
391	\subsection{LD-Score as Pre-Registered Validation}
392	\label{sec:ldscore}
393	
394	As a pre-registered test of the H$_1$/H$_2$ framework's predictive utility, we predicted that LD-Score (a character-level distributional signature) would behave as an H$_2$ level feature.
395	This prediction is confirmed: LD-Score exhibits depth-correlated drift ($\rho{=}-0.55$, slope $-0.042$, $R^2{=}0.72$).
396	However, it is highly correlated with existing surface features (0.68 with TTR, 0.61 with hapax\_ratio) and provides negligible marginal classification improvement (F1: 0.83 vs 0.82 without).
397	This validates the framework's predictions while confirming that character-level and word-level diversity capture the same underlying depth signal.
398	
399	% ----------------------------------------------------------
400	\subsection{End-to-End Neural Baseline}
401	\label{sec:e2e}
402	
403	A QLoRA fine-tuned Qwen3-0.6B achieves within-generator F1 0.79 and LOGO F1 0.61, slightly underperforming the handcrafted feature set (0.82 and 0.64 respectively).
404	The end-to-end approach requires 6.2 GPU-hours of training and runs at 145 tokens/sec inference, versus near-zero training cost and 8{,}900 tokens/sec for the handcrafted features (${\sim}60\times$ faster).
405	This confirms that the depth classification task is well-served by simple distributional statistics; the information content is captured by lightweight features without requiring learned representations.
406	
407	% ----------------------------------------------------------
408	\subsection{Scaling Analysis: 7B+ Generators}
409	\label{sec:scale}
410	
411	Table~\ref{tab:scale} summarizes depth classification performance by generator scale.
412	Qwen3-8B (8B parameters) achieves only F1 0.57---substantially below the ${\leq}$2.8B mean of 0.78.
413	Entropy\_mean drift attenuates ($\rho{=}-0.38$ vs mean $-0.62$ for smaller models) and TTR slope weakens ($-0.042$ vs $-0.064$), consistent with larger models maintaining more diverse vocabulary under recursive generation.
414	Gen-0 remains distinguishable (F1 0.76), but gen-1 vs gen-2+ approaches the noise floor (F1 0.46--0.48).
415	H$_1$ shape stationarity is preserved at scale (max $|\rho|{=}0.07$).
416	
417	\begin{table}[h]
418	\centering
419	\caption{Depth classification by generator scale.}
420	\label{tab:scale}
421	\begin{tabular}{lcccc}
422	\toprule
423	Generator & Params & Macro-F1 & $\rho$ (ent\_mean) & TTR slope \\
424	\midrule
425	Pythia-2.8B & 2.8B & 0.82 & $-0.68$ & $-0.071$ \\
426	Pythia-1B & 1B & 0.80 & $-0.65$ & $-0.068$ \\
427	OLMo-2-1B & 1.5B & 0.78 & $-0.61$ & $-0.063$ \\
428	Qwen3-1.7B & 1.7B & 0.75 & $-0.56$ & $-0.055$ \\
429	Qwen3-0.6B & 0.6B & 0.77 & $-0.59$ & $-0.061$ \\
430	\midrule
431	Qwen3-8B & 8B & 0.57 & $-0.38$ & $-0.042$ \\
432	\bottomrule
433	\end{tabular}
434	\end{table}
435	
436	The relationship between model capacity and depth signal decay is itself informative: larger models compress distributional drift more effectively, suggesting that scale-robust depth features may require model-specific calibration.
437	
438	% ----------------------------------------------------------
439	\subsection{Downstream Utility}
440	\label{sec:downstream}
441	
442	We fine-tune OLMo-1B on depth-stratified data (3 seeds, bootstrap CIs) and compare depth-aware filtering against binary baselines.
443	
444	\paragraph{Depth-stratified training quality.}
445	Table~\ref{tab:downstream} shows mean perplexity by training data composition.
446	Gen-0-only training achieves the lowest perplexity (18.4), gen-0+gen-1 is close (19.1), while including gen-2+ text degrades quality (21.7), approaching unfiltered (22.3).
447	Depth-quality Spearman $\rho{=}0.53$ [0.41, 0.64].
448	
449	\begin{table}[h]
450	\centering
451	\caption{Downstream perplexity by training data composition (OLMo-1B, 3 seeds).}
452	\label{tab:downstream}
453	\begin{tabular}{lccc}
454	\toprule
455	Training Data & $N$ & Mean PPL & 95\% CI \\
456	\midrule
457	Gen-0 only & 4{,}850 & 18.4 & [17.9, 18.9] \\
458	Gen-0 + gen-1 & 9{,}700 & 19.1 & [18.5, 19.7] \\
459	Gen-0 + gen-1 + gen-2+ & 18{,}200 & 21.7 & [20.8, 22.6] \\
460	Unfiltered & 21{,}500 & 22.3 & [21.5, 23.1] \\
461	\bottomrule
462	\end{tabular}
463	\end{table}
464	
465	\paragraph{Comparison with binary baselines.}
466	Depth-aware filtering (keep gen-0 + gen-1) yields 5.2\% perplexity improvement [3.8, 7.1] over unfiltered data, compared to 3.8\% [2.1, 5.9] for FastDetectGPT and 3.2\% [1.6, 5.3] for LD-Score thresholding.
467	Under sample-matched comparison (controlling for data volume), the depth advantage narrows: 2.8\% [1.4, 4.5] vs 1.9\% [0.5, 3.6] for binary filtering.
468	The CIs overlap between depth-aware and the best binary baseline, precluding a ``significantly outperforms'' claim.
469	Downstream task accuracy shows a consistent but modest pattern: 0.724 (depth-filtered), 0.711 (binary-filtered), 0.698 (unfiltered).
470	
471	The practical value of depth estimation is not raw performance superiority over binary detection but the ability to retain useful gen-1 data---which binary detectors discard---while filtering harmful gen-2+ text.
472	Depth scores also provide a continuous risk metric that binary labels cannot.
473	
474	% ============================================================
475	\section{Discussion and Limitations}
476	\label{sec:discussion}
477	
478	\paragraph{Honest assessment of generalization.}
479	Within-generator depth estimation is strong (F1 0.82), but cross-generator generalization is moderate (LOGO F1 0.64, LOFO F1 0.59).
480	Performance drops concentrate on out-of-family holdouts, indicating that current features partially encode generator identity alongside depth.
481	
482	\paragraph{Reference model modulation.}
483	The dual dynamics pattern is robust---level features always drift, shape features always remain stationary---but the drift magnitude varies ${\sim}2\times$ depending on reference model choice.
484	This makes the H$_1$/H$_2$ split a ``reference-model-modulated'' phenomenon rather than a universal law.
485	Practical deployment requires reference model selection.
486	
487	\paragraph{Scale limitation.}
488	At 7B+ parameters, depth signal weakens substantially (F1 0.57).
489	As frontier models grow, current features may become insufficient for fine-grained depth estimation.
490	Scale-robust features---potentially leveraging model-specific distributional properties or training dynamics---are needed.
491	
492	\paragraph{Ecological validity.}
493	Cross-model chains (F1 0.56), creative writing domains (F1 0.57), and inspired rewriting prompts (F1 0.69) all degrade performance, reflecting realistic conditions where depth estimation is most challenging.
494	Heavy human editing (${>}$10\%) further erodes signal.
495	Depth estimation is most reliable for lightly edited, single-source continuation chains.
496	
497	\paragraph{Downstream utility caveat.}
498	While depth-aware filtering outperforms binary baselines on average, CIs overlap with the best binary baseline on some metrics.
499	Roughly half the filtering advantage comes from retaining more training data (gen-1), not from better selection quality per se.
500	
501	% ============================================================
502	\section{Conclusion}
503	\label{sec:conclusion}
504	
505	We formulate generation depth estimation as a new task beyond binary synthetic text detection and provide systematic empirical evidence across six generators, four domains, and multiple evaluation protocols.
506	Our key finding is \emph{reference-model-modulated dual dynamics}: level/diversity features drift monotonically with depth while distributional shape features remain stationary, a split determined by what the feature measures rather than its source.
507	This pattern supports 3-class depth estimation at macro-F1 0.82 within-generator and 0.64 cross-generator, with practical utility for risk-stratified data curation.
508	
509	Depth estimation is feasible and useful, with initial evidence for dual dynamics as an organizing principle.
510	Significant challenges remain: cross-family generalization, scaling to frontier models, and robustness to realistic post-editing.
511	These limitations define clear directions for future work on generator-invariant features, scale-adaptive reference models, and integration with existing data curation pipelines.
512	
513	% ============================================================
514	\bibliographystyle{plainnat}
515	\begin{thebibliography}{10}
516	
517	\bibitem[Alemohammad et~al.(2023)]{alemohammad2023selfconsuming}
518	Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk.
519	\newblock Self-consuming generative models go MAD.
520	\newblock \emph{arXiv preprint arXiv:2307.01850}, 2023.
521	
522	\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}
523	Guangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang.
524	\newblock Fast-DetectGPT: Efficient zero-shot detection of machine-generated text via conditional probability curvature.
525	\newblock In \emph{ICLR}, 2024.
526	
527	\bibitem[Dohmatob et~al.(2024)]{dohmatob2024curse}
528	Elvis Dohmatob, Yunzhen Feng, and Julia Kempe.
529	\newblock A tale of tails: Model collapse as a change of scaling laws.
530	\newblock In \emph{ICML}, 2024.
531	
532	\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}
533	Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, and Sanmi Koyejo.
534	\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.
535	\newblock \emph{arXiv preprint arXiv:2404.01413}, 2024.
536	
537	\bibitem[Guo et~al.(2024)]{guo2024curious}
538	Yanzhu Guo, Guokan Shang, Mingxue Li, Chlo{\'e} Clavel, and Michalis Vazirgiannis.
539	\newblock On the curious decline of linguistic diversity with scale: A study on LLM-generated text.
540	\newblock In \emph{EMNLP Findings}, 2024.
541	
542	\bibitem[Hans et~al.(2024)]{hans2024binoculars}
543	Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.
544	\newblock Spotting LLMs with Binoculars: Zero-shot detection of machine-generated text.
545	\newblock In \emph{ICML}, 2024.
546	
547	\bibitem[Holtzman et~al.(2020)]{holtzman2020curious}
548	Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi.
549	\newblock The curious case of neural text degeneration.
550	\newblock In \emph{ICLR}, 2020.
551	
552	\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}
553	John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein.
554	\newblock A watermark for large language models.
555	\newblock In \emph{ICML}, 2023.
556	
557	\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}
558	Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, and Chelsea Finn.
559	\newblock DetectGPT: Zero-shot machine-generated text detection using probability curvature.
560	\newblock In \emph{ICML}, 2023.
561	
562	\bibitem[Xie et~al.(2023)]{xie2023dsir}
563	Sang~Michael Xie, Shibani Santurkar, Tengyu Ma, and Percy Liang.
564	\newblock Data selection for language models via importance resampling.
565	\newblock In \emph{NeurIPS}, 2023.
566	
567	\end{thebibliography}
568	
569	\end{document}
570	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b70ace95-da8a-40ea-8e93-2330fca2c9dd",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "754ed498-c9ec-49cf-bdb0-d903a0b99479",
  "sourceToolAssistantUUID": "b70ace95-da8a-40ea-8e93-2330fca2c9dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T23:08:27.570Z_

<details><summary>↩ Tool result · `toolu_0147Koa52C11aMFuXT1aNFmP`</summary>

```text
1	tier: median
2	narrative_guidance: 'Depth discriminability holds within-generator (F1 0.82) but cross-generator
3	  generalization is moderate (LOGO F1 ~0.64), with performance drops concentrated
4	  on out-of-family holdouts. Dual dynamics is real but reference-model-modulated:
5	  entropy_mean drift attenuates to |ρ|~0.4 with non-Pythia references, requiring the
6	  paper to present the H1/H2 split as ''reference-model-modulated dual dynamics''
7	  rather than a universal law. Length confound is partial — surface feature F1 drops
8	  ~0.05 after length control, but residual signal confirms depth is not reducible
9	  to length. 7B+ signal weakens (F1 ~0.57) but persists, motivating future work on
10	  scale-robust features. Downstream filtering offers complementary signal but CIs
11	  overlap with best binary baseline on some metrics. Paper reframed: ''depth estimation
12	  is feasible and useful, with initial evidence for dual dynamics'' rather than ''dual
13	  dynamics as general principle.'' Still viable for AAAI/EMNLP as empirical contribution
14	  with honest limitations.
15	
16	  '
17	imagined_experiments:
18	- name: feature_ablation_and_trend
19	  plan_id: plan_001
20	  description: 'Feature ablation (full / surface-only / reference-only) + H1/H2 trend
21	    analysis on MVP data (Pythia-2.8B generator, Pythia-410M reference). Perplexity
22	    pre-validation for Claim 3.
23	
24	    '
25	  expected_results:
26	    full_macro_f1: 0.82
27	    surface_only_f1: 0.76
28	    reference_only_f1: 0.72
29	    full_vs_surface_gap: 0.06
30	    full_vs_reference_gap: 0.1
31	    bootstrap_ci_full: '[0.804, 0.836]'
32	    bootstrap_ci_surface: '[0.747, 0.774]'
33	    bootstrap_ci_reference: '[0.706, 0.733]'
34	    h2_entropy_mean_slope: -0.148
35	    h2_entropy_mean_r2: 0.93
36	    h2_ttr_slope: -0.071
37	    h2_ttr_r2: 0.87
38	    h2_hapax_ratio_slope: -0.054
39	    h2_hapax_ratio_r2: 0.81
40	    h1_entropy_std_slope: 0.003
41	    h1_entropy_std_r2: 0.02
42	    h1_entropy_max_slope: -0.009
43	    h1_entropy_max_r2: 0.04
44	    h1_tail_decay_slope: 0.005
45	    h1_tail_decay_r2: 0.03
46	    h1_entropy_min_slope: -0.012
47	    h1_entropy_min_r2: 0.06
48	    median_ppl_by_depth:
49	    - 13.5
50	    - 4.96
51	    - 3.0
52	    - 2.07
53	    - 1.72
54	    ppl_kruskal_wallis_p: <0.001
55	  result_rationale: 'Within-generator results remain strong because Pythia-410M reference
56	    model is architecturally aligned with the Pythia-2.8B generator, maximizing NLL
57	    feature sensitivity. The 0.06 full-surface gap confirms reference features add
58	    independent value — entropy_mean captures distributional compression that surface
59	    statistics miss. H2 features (entropy_mean, TTR, hapax_ratio) drift because recursive
60	    generation compounds vocabulary impoverishment and entropy compression — each
61	    step feeds an increasingly constrained output distribution back as input. H1 features
62	    (shape statistics like entropy_std, tail_decay) remain stable because distributional
63	    shape is determined by the generator''s softmax geometry, not the input content
64	    — recursive generation shifts the location (mean) of the NLL distribution but
65	    not its spread or tail behavior. Perplexity shows steep monotonic decline because
66	    deeper generations become more predictable to the reference model as they converge
67	    toward the generator''s mode.
68	
69	    '
70	  tables:
71	  - name: 'Table 1: Feature Ablation (5-fold CV, Pythia-2.8B, N=4609)'
72	    columns:
73	    - feature_set
74	    - macro_f1
75	    - 95% CI
76	    - gen0_f1
77	    - gen1_f1
78	    - gen2plus_f1
79	    rows:
80	    - - Full (7 features)
81	      - 0.82
82	      - '[0.804, 0.836]'
83	      - 0.94
84	      - 0.77
85	      - 0.79
86	    - - Surface only (TTR + hapax)
87	      - 0.76
88	      - '[0.747, 0.774]'
89	      - 0.91
90	      - 0.7
91	      - 0.72
92	    - - Reference only (5 NLL)
93	      - 0.72
94	      - '[0.706, 0.733]'
95	      - 0.88
96	      - 0.65
97	      - 0.67
98	    - - Chance baseline
99	      - 0.33
100	      - —
101	      - 0.33
102	      - 0.33
103	      - 0.33
104	  - name: 'Table 2: H1/H2 Trend Regression per Feature'
105	    columns:
106	    - feature
107	    - slope
108	    - R²
109	    - p_value
110	    - classification
111	    rows:
112	    - - entropy_mean
113	      - -0.148
114	      - 0.93
115	      - <0.001
116	      - H2 (drift)
117	    - - TTR
118	      - -0.071
119	      - 0.87
120	      - <0.001
121	      - H2 (drift)
122	    - - hapax_ratio
123	      - -0.054
124	      - 0.81
125	      - <0.001
126	      - H2 (drift)
127	    - - entropy_std
128	      - 0.003
129	      - 0.02
130	      - 0.41
131	      - H1 (stationary)
132	    - - entropy_max
133	      - -0.009
134	      - 0.04
135	      - 0.28
136	      - H1 (stationary)
137	    - - tail_decay
138	      - 0.005
139	      - 0.03
140	      - 0.33
141	      - H1 (stationary)
142	    - - entropy_min
143	      - -0.012
144	      - 0.06
145	      - 0.19
146	      - H1 (stationary)
147	  figures_description:
148	  - 'Fig 1: 7-panel feature trend plot (mean ± std) across depths 0-4. H2 features
149	    show clear monotonic decline; H1 features show flat profiles with overlapping
150	    error bands. Visual separation between H1 and H2 behavior is stark.'
151	  - 'Fig 2: Perplexity distribution boxplots by depth (0-4). Dramatic compression
152	    from depth 0 (median 13.5) to depth 4 (median 1.72), confirming depth-correlated
153	    distributional shift.'
154	  analysis: 'Results confirm the H1/H2 split on MVP data. The 0.06 full-vs-surface
155	    gap is statistically significant (bootstrap CIs non-overlapping), establishing
156	    that reference features capture complementary signal. However, this is within-generator
157	    with same-family reference model — the gap''s robustness must be tested cross-generator
158	    (plan_002) and cross-reference (plan_003). The steep perplexity gradient validates
159	    Claim 3''s premise: depth correlates with distributional properties detectable
160	    by a reference model.
161	
162	    '
163	- name: cross_generator_evaluation
164	  plan_id: plan_002
165	  description: '5-generator LOGO evaluation: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B,
166	    Qwen3-0.6B. 1000 seeds per generator × 5 depths. Leave-one-generator-out and leave-one-family-out
167	    CV.
168	
169	    '
170	  expected_results:
171	    logo_mean_macro_f1: 0.64
172	    logo_holdout_pythia28b_f1: 0.71
173	    logo_holdout_pythia1b_f1: 0.72
174	    logo_holdout_olmo2_f1: 0.6
175	    logo_holdout_qwen17b_f1: 0.62
176	    logo_holdout_qwen06b_f1: 0.59
177	    lofo_holdout_pythia_family_f1: 0.58
178	    lofo_holdout_olmo_family_f1: 0.61
179	    lofo_holdout_qwen_family_f1: 0.59
180	    lofo_mean_f1: 0.593
181	    within_generator_pooled_5fold_f1: 0.78
182	    logo_full_feature_f1: 0.64
183	    logo_surface_only_f1: 0.61
184	    logo_reference_only_f1: 0.58
185	    logo_full_vs_surface_gap: 0.03
186	    logo_full_vs_reference_gap: 0.06
187	    total_chains_generated: 23847
188	    total_chains_after_attrition: 21503
189	  result_rationale: 'Cross-generator F1 drops from 0.82 (within-generator) to 0.64
190	    (LOGO) because each generator family imprints family-specific distributional signatures
191	    beyond the depth signal. Pythia holdouts score higher (0.71-0.72) because Pythia-1B
192	    and Pythia-2.8B share architectural biases (tokenizer, attention patterns, pretraining
193	    data overlap) — when one is held out, the other provides a close proxy in the
194	    training set. OLMo and Qwen holdouts score lower (0.59-0.62) because they represent
195	    genuinely out-of-distribution generator families with different tokenizers and
196	    pretraining distributions. The full-vs-surface gap narrows from 0.06 to 0.03 because
197	    reference features (computed with Pythia-410M) are partially Pythia-biased: they
198	    extract richer signal from Pythia-generated text than from OLMo/Qwen-generated
199	    text, eroding their cross-family advantage. Leave-one-family-out results (mean
200	    0.593) are lower than LOGO (0.64) because LOGO benefits from same-family generators
201	    remaining in training. The within-generator pooled F1 (0.78) is lower than MVP''s
202	    0.82 because pooling heterogeneous generators introduces inter-generator variance
203	    that the classifier must absorb.
204	
205	    '
206	  tables:
207	  - name: 'Table 3: Leave-One-Generator-Out Results (Full Features)'
208	    columns:
209	    - held_out_generator
210	    - family
211	    - macro_f1
212	    - gen0_f1
213	    - gen1_f1
214	    - gen2plus_f1
215	    rows:
216	    - - Pythia-2.8B
217	      - Pythia
218	      - 0.71
219	      - 0.87
220	      - 0.64
221	      - 0.66
222	    - - Pythia-1B
223	      - Pythia
224	      - 0.72
225	      - 0.88
226	      - 0.66
227	      - 0.67
228	    - - OLMo-2-1B
229	      - OLMo
230	      - 0.6
231	      - 0.79
232	      - 0.51
233	      - 0.53
234	    - - Qwen3-1.7B
235	      - Qwen
236	      - 0.62
237	      - 0.82
238	      - 0.53
239	      - 0.55
240	    - - Qwen3-0.6B
241	      - Qwen
242	      - 0.59
243	      - 0.78
244	      - 0.5
245	      - 0.51
246	    - - Mean LOGO
247	      - —
248	      - 0.64
249	      - 0.83
250	      - 0.57
251	      - 0.58
252	  - name: 'Table 4: Leave-One-Family-Out Results'
253	    columns:
254	    - held_out_family
255	    - generators_in_family
256	    - macro_f1
257	    - 95% CI
258	    rows:
259	    - - Pythia
260	      - 2.8B + 1B
261	      - 0.58
262	      - '[0.55, 0.61]'
263	    - - OLMo
264	      - OLMo-2-1B
265	      - 0.61
266	      - '[0.57, 0.64]'
267	    - - Qwen
268	      - 1.7B + 0.6B
269	      - 0.59
270	      - '[0.56, 0.62]'
271	  - name: 'Table 5: Feature Ablation in Cross-Generator Setting (LOGO)'
272	    columns:
273	    - feature_set
274	    - logo_macro_f1
275	    - gap_vs_full
276	    rows:
277	    - - Full
278	      - 0.64
279	      - —
280	    - - Surface only
281	      - 0.61
282	      - -0.03
283	    - - Reference only
284	      - 0.58
285	      - -0.06
286	  figures_description:
287	  - 'Fig 3: LOGO F1 heatmap — rows are held-out generators, columns are depth classes
288	    (gen-0/1/2+). Clear diagonal pattern: within-family holdouts (Pythia-2.8B, Pythia-1B)
289	    are warmer; cross-family (OLMo, Qwen) are cooler, especially for gen-1 and gen-2+.'
290	  - 'Fig 4: Confusion matrices for best (Pythia-1B holdout, F1=0.72) and worst (Qwen-0.6B
291	    holdout, F1=0.59) LOGO folds. Worst case shows gen-1/gen-2+ confusion concentrated
292	    in cross-family.'
293	  analysis: 'LOGO F1=0.64 is within the median range [0.58, 0.70] and confirms moderate
294	    cross-generator generalization. The within-family vs cross-family gap (~0.12)
295	    reveals that distributional features partially encode generator identity, not
296	    just depth. This constrains Claim 1 to ''depth discriminability generalizes within
297	    model family; cross-family generalization is moderate and requires further work.''
298	    The narrowing full-vs-surface gap (0.03 vs 0.06 within-generator) suggests reference
299	    features lose their relative advantage in the cross-generator setting — likely
300	    because the Pythia-410M reference model is better calibrated for Pythia-family
301	    generators. This motivates plan_003 to test non-Pythia reference models.
302	
303	    '
304	- name: cross_family_reference_model
305	  plan_id: plan_003
306	  description: 'Recompute NLL features using non-Pythia reference models (OLMo-2-1B,
307	    Qwen3-0.6B) on existing plan_002 data. Test whether entropy_mean H2 drift and
308	    shape feature H1 stationarity persist. Key falsification test for Claim 2.
309	
310	    '
311	  expected_results:
312	    pythia410m_ref_entropy_mean_rho: -0.68
313	    olmo2_ref_entropy_mean_rho: -0.42
314	    qwen06b_ref_entropy_mean_rho: -0.36
315	    pythia410m_ref_full_f1: 0.82
316	    olmo2_ref_full_f1: 0.78
317	    qwen06b_ref_full_f1: 0.76
318	    olmo2_ref_shape_max_abs_rho: 0.11
319	    qwen06b_ref_shape_max_abs_rho: 0.09
320	    pythia410m_ref_shape_max_abs_rho: 0.08
321	    olmo2_ref_entropy_std_rho: 0.06
322	    olmo2_ref_tail_decay_rho: -0.11
323	    qwen06b_ref_entropy_std_rho: -0.04
324	    qwen06b_ref_tail_decay_rho: 0.09
325	    cross_ref_logo_f1_olmo_ref: 0.61
326	    cross_ref_logo_f1_qwen_ref: 0.58
327	  result_rationale: 'Entropy_mean drift attenuates (|ρ| drops from 0.68 to 0.36-0.42)
328	    because the drift magnitude depends on how well the reference model''s learned
329	    distribution aligns with the generator''s mode. Pythia-410M shares architecture
330	    and pretraining data with Pythia-2.8B, amplifying NLL sensitivity to the generator''s
331	    recursive drift. Non-Pythia references (OLMo, Qwen) have different internal distributions,
332	    so the NLL mean shifts less per depth step — the drift still exists (recursive
333	    generation objectively compresses the output distribution regardless of who measures
334	    it) but the reference model''s measurement sensitivity is lower. Shape features
335	    remain H1 (|ρ|<0.12) across all references because distributional shape (variance,
336	    tail behavior) is a property of the generator''s softmax output geometry, which
337	    doesn''t change with the reference model — different reference models shift the
338	    NLL baseline but preserve relative shape statistics. Classification F1 drops moderately
339	    because attenuated entropy_mean signal provides less discriminative power for
340	    the ordinal depth task.
341	
342	    '
343	  tables:
344	  - name: 'Table 6: Entropy_mean Drift (ρ) by Reference Model'
345	    columns:
346	    - reference_model
347	    - entropy_mean_rho
348	    - p-value
349	    - classification_full_f1
350	    rows:
351	    - - Pythia-410M
352	      - -0.68
353	      - <0.001
354	      - 0.82
355	    - - OLMo-2-1B
356	      - -0.42
357	      - <0.001
358	      - 0.78
359	    - - Qwen3-0.6B
360	      - -0.36
361	      - <0.001
362	      - 0.76
363	  - name: 'Table 7: Shape Feature Stationarity Across References (max |ρ|)'
364	    columns:
365	    - reference_model
366	    - entropy_std_rho
367	    - entropy_max_rho
368	    - tail_decay_rho
369	    - max_abs_rho
370	    rows:
371	    - - Pythia-410M
372	      - 0.03
373	      - -0.05
374	      - 0.04
375	      - 0.08
376	    - - OLMo-2-1B
377	      - 0.06
378	      - -0.08
379	      - -0.11
380	      - 0.11
381	    - - Qwen3-0.6B
382	      - -0.04
383	      - 0.07
384	      - 0.09
385	      - 0.09
386	  figures_description:
387	  - 'Fig 5: Entropy_mean trend lines (depth 0-4) for three reference models. Pythia-410M
388	    shows steepest decline; OLMo-2-1B intermediate; Qwen3-0.6B shallowest. All three
389	    monotonically decreasing but with different slopes.'
390	  - 'Fig 6: Shape feature (entropy_std, tail_decay) trend lines across reference models
391	    — three nearly flat lines per feature, confirming H1 robustness is reference-model-invariant.'
392	  analysis: 'Dual dynamics survives but is reference-model-modulated. The level/shape
393	    split is real across all references (H2 features always drift, H1 features always
394	    stable), but drift magnitude varies 2x depending on reference model choice. This
395	    softens Claim 2 from ''dual dynamics as universal law'' to ''reference-model-modulated
396	    dual dynamics'' — the split is intrinsic to what the feature measures (central
397	    tendency vs shape), but the signal strength depends on reference-generator alignment.
398	    Paper must present this honestly and discuss implications for practical deployment
399	    (reference model selection matters). The cross-reference LOGO F1 (0.58-0.61) shows
400	    that non-Pythia references still support depth estimation, just with reduced accuracy.
401	
402	    '
403	- name: downstream_utility
404	  plan_id: plan_004
405	  description: 'Fine-tune OLMo-1B on depth-stratified data. 3 seeds with bootstrap
406	    CIs. Compare depth-aware filtering (keep gen-0 + gen-1) vs binary baselines (FastDetectGPT,
407	    LD-Score threshold). Sample-count-matched comparison to control for data size
408	    confound.
409	
410	    '
411	  expected_results:
412	    seeds_run: 3
413	    depth_quality_spearman_rho: 0.53
414	    depth_quality_spearman_ci: '[0.41, 0.64]'
415	    ppl_gen0_only: 18.4
416	    ppl_gen0_plus_gen1: 19.1
417	    ppl_gen0_plus_gen1_plus_gen2plus: 21.7
418	    ppl_unfiltered: 22.3
419	    depth_filtering_ppl_improvement_pct: 5.2
420	    depth_filtering_ppl_improvement_ci: '[3.8, 7.1]'
421	    binary_fastdetectgpt_ppl_improvement_pct: 3.8
422	    binary_fastdetectgpt_ppl_improvement_ci: '[2.1, 5.9]'
423	    binary_ldscore_ppl_improvement_pct: 3.2
424	    binary_ldscore_ppl_improvement_ci: '[1.6, 5.3]'
425	    sample_matched_depth_improvement_pct: 2.8
426	    sample_matched_binary_improvement_pct: 1.9
427	    ci_overlap_with_best_binary: true
428	    downstream_task_accuracy_depth: 0.724
429	    downstream_task_accuracy_binary: 0.711
430	    downstream_task_accuracy_unfiltered: 0.698
431	  result_rationale: 'Depth-quality correlation (ρ=0.53) is moderate because OLMo-1B
432	    is somewhat robust to moderate contamination — gen-1 data is only mildly degraded
433	    (perplexity shift from 18.4 to 19.1), so the correlation is driven primarily by
434	    the gen-2+ tail where distributional drift accumulates. Depth-aware filtering
435	    outperforms binary filtering by ~1.4% because it retains gen-1 data that binary
436	    detectors discard — gen-1 text is close to human-quality and contributes positively
437	    to training. However, CI overlap exists because: (1) the advantage is small in
438	    absolute terms, (2) 3 seeds produce wide CIs, and (3) FastDetectGPT''s false negative
439	    rate on gen-1 means it sometimes keeps useful gen-1 data by accident. Sample-matched
440	    comparison (controlling for the data size advantage of depth-aware filtering)
441	    reduces the gap further to 0.9%, confirming that roughly half the advantage comes
442	    from retaining more training data, not from better selection. The effect is real
443	    but modest — insufficient for a strong ''significantly outperforms'' claim.
444	
445	    '
446	  tables:
447	  - name: 'Table 8: Downstream Perplexity by Training Data Composition (OLMo-1B, 3
448	      seeds)'
449	    columns:
450	    - training_data
451	    - n_samples
452	    - mean_ppl
453	    - std_ppl
454	    - 95% CI
455	    rows:
456	    - - gen-0 only
457	      - 4850
458	      - 18.4
459	      - 0.3
460	      - '[17.9, 18.9]'
461	    - - gen-0 + gen-1
462	      - 9700
463	      - 19.1
464	      - 0.4
465	      - '[18.5, 19.7]'
466	    - - gen-0 + gen-1 + gen-2+
467	      - 18200
468	      - 21.7
469	      - 0.6
470	      - '[20.8, 22.6]'
471	    - - Unfiltered (all depths)
472	      - 21500
473	      - 22.3
474	      - 0.5
475	      - '[21.5, 23.1]'
476	  - name: 'Table 9: Filtering Strategy Comparison'
477	    columns:
478	    - strategy
479	    - kept_samples
480	    - ppl_improvement_pct
481	    - 95% CI
482	    - overlap_with_depth
483	    rows:
484	    - - Depth-aware (gen-0+gen-1)
485	      - 9700
486	      - 5.2
487	      - '[3.8, 7.1]'
488	      - —
489	    - - FastDetectGPT binary
490	      - 7300
491	      - 3.8
492	      - '[2.1, 5.9]'
493	      - 'yes'
494	    - - LD-Score binary
495	      - 6900
496	      - 3.2
497	      - '[1.6, 5.3]'
498	      - 'yes'
499	    - - Sample-matched depth
500	      - 7300
501	      - 2.8
502	      - '[1.4, 4.5]'
503	      - —
504	    - - Sample-matched binary
505	      - 7300
506	      - 1.9
507	      - '[0.5, 3.6]'
508	      - —
509	  figures_description:
510	  - 'Fig 7: Perplexity degradation curve as function of training data depth composition
511	    (0-4). Clear upward trend with error bars (3 seeds). gen-0→gen-1 step is small;
512	    gen-1→gen-2+ is the main inflection point.'
513	  - 'Fig 8: Bootstrap CI comparison — depth-aware vs binary filtering perplexity improvement.
514	    Point estimates favor depth-aware, but CI bars overlap for FastDetectGPT.'
515	  analysis: 'Downstream utility exists but the advantage over binary filtering is
516	    modest (1.4% mean, CIs overlap). Claim 3 must be softened to ''depth-aware filtering
517	    offers complementary signal to binary detection'' — the value proposition is not
518	    raw performance but the ability to retain useful gen-1 data while filtering harmful
519	    gen-2+. Sample-matched analysis shows roughly half the gain is from data volume,
520	    not selection quality. Paper should present this honestly and emphasize the interpretability
521	    advantage: depth scores provide a continuous risk metric that binary labels cannot.
522	
523	    '
524	- name: prompt_type_comparison
525	  plan_id: plan_005
526	  description: 'Compare depth signal across three prompt types: continuation, elaboration,
527	    inspired_rewriting. 1000 seeds × Pythia-2.8B × 5 depths × 3 prompt types.
528	
529	    '
530	  expected_results:
531	    continuation_macro_f1: 0.82
532	    elaboration_macro_f1: 0.77
533	    inspired_rewriting_macro_f1: 0.69
534	    continuation_entropy_mean_rho: -0.68
535	    elaboration_entropy_mean_rho: -0.57
536	    inspired_rewriting_entropy_mean_rho: -0.39
537	    continuation_ttr_slope: -0.071
538	    elaboration_ttr_slope: -0.058
539	    inspired_rewriting_ttr_slope: -0.031
540	    h1_features_stable_across_prompts: true
541	  result_rationale: 'Continuation preserves the strongest depth signal because each
542	    step feeds the previous output directly, maximizing distributional drift accumulation.
543	    Elaboration introduces a semantic reframing prompt that partially resets the generator''s
544	    conditioning, attenuating the chain''s compounding effect — the generator still
545	    uses the previous text but the prompt steers it toward a different discourse structure,
546	    reducing the monotonic drift. Inspired rewriting is most disruptive because the
547	    generator is asked to produce content ''inspired by'' rather than continuing from
548	    the previous text — this creates a loose semantic link but breaks the tight distributional
549	    chain, so depth-0 vs depth-2 texts can have similar distributional properties
550	    if the generator happens to produce fluent rewrites. H1 features remain stable
551	    across all prompt types because shape stationarity is a property of the generator''s
552	    output distribution, not the input conditioning.
553	
554	    '
555	  tables:
556	  - name: 'Table 10: Depth Classification by Prompt Type (Pythia-2.8B, 5-fold CV)'
557	    columns:
558	    - prompt_type
559	    - macro_f1
560	    - entropy_mean_rho
561	    - ttr_slope
562	    - semantic_divergence_cosine
563	    rows:
564	    - - Continuation
565	      - 0.82
566	      - -0.68
567	      - -0.071
568	      - 0.85
569	    - - Elaboration
570	      - 0.77
571	      - -0.57
572	      - -0.058
573	      - 0.72
574	    - - Inspired rewriting
575	      - 0.69
576	      - -0.39
577	      - -0.031
578	      - 0.54
579	  figures_description:
580	  - 'Fig 9: Feature drift magnitude by prompt type — bar chart showing H2 feature
581	    slopes for each prompt type. Clear gradient from continuation (steepest) to inspired
582	    rewriting (shallowest).'
583	  analysis: 'Semantic divergence from source anti-correlates with depth signal preservation.
584	    Continuation is the ideal setting for depth estimation; inspired rewriting represents
585	    a harder, more realistic scenario where depth signal partially dissolves. This
586	    informs ecological validity discussions: real-world LLM contamination likely involves
587	    a mix of prompt types, placing practical performance between 0.69-0.82.
588	
589	    '
590	- name: paraphrastic_comparison
591	  plan_id: plan_006
592	  description: 'Parallel paraphrasing chains vs continuation chains for direct comparison.
593	    Tests attractor convergence theory — paraphrastic chains should saturate earlier.
594	
595	    '
596	  expected_results:
597	    paraphrastic_3class_f1: 0.66
598	    nonparaphrastic_3class_f1: 0.82
599	    paraphrastic_gen2plus_f1: 0.41
600	    nonparaphrastic_gen2plus_f1: 0.79
601	    paraphrastic_5class_f1: 0.29
602	    nonparaphrastic_5class_f1: 0.43
603	    paraphrastic_entropy_mean_rho: -0.34
604	    nonparaphrastic_entropy_mean_rho: -0.68
605	    paraphrastic_signal_saturation_depth: 2
606	    nonparaphrastic_signal_saturation_depth: 4
607	  result_rationale: 'Paraphrastic chains converge to attractor cycles (ACL 2025 theory),
608	    bounding depth signal to ~2 distinguishable classes — by depth-2, paraphrased
609	    text has already entered the attractor basin, so gen-2/gen-3/gen-4 become distributionally
610	    indistinguishable. This collapses gen-2+ F1 to near-chance (0.41). Non-paraphrastic
611	    continuation chains escape the attractor because each step generates genuinely
612	    new content rather than cycling through semantically equivalent rewrites. Distributional
613	    drift accumulates monotonically through depth-4, preserving ordinal signal. The
614	    paraphrastic entropy_mean ρ (-0.34) is weaker because the drift saturates early
615	    — depths 2-4 contribute noise, not signal, to the correlation. This directly validates
616	    the paper''s premise: non-paraphrastic chains are the right focus for depth estimation
617	    because the attractor convergence bound does not apply.
618	
619	    '
620	  tables:
621	  - name: 'Table 11: Paraphrastic vs Non-paraphrastic Depth Classification'
622	    columns:
623	    - chain_type
624	    - 3class_f1
625	    - gen0_f1
626	    - gen1_f1
627	    - gen2plus_f1
628	    - signal_saturation_depth
629	    rows:
630	    - - Paraphrastic
631	      - 0.66
632	      - 0.89
633	      - 0.67
634	      - 0.41
635	      - 2
636	    - - Non-paraphrastic
637	      - 0.82
638	      - 0.94
639	      - 0.77
640	      - 0.79
641	      - 4+
642	  figures_description:
643	  - 'Fig 10: Per-depth F1 curves for paraphrastic (flattens at depth 2) vs non-paraphrastic
644	    (gradual decline through depth 4). Clear visual separation demonstrating attractor
645	    saturation vs sustained drift.'
646	  analysis: 'Confirms the theoretical motivation: paraphrastic chains hit the attractor
647	    bound at depth ~2, while non-paraphrastic chains maintain discriminable depth
648	    signal through depth 4. This justifies the paper''s focus on continuation chains
649	    and connects to attractor cycle theory as a boundary condition rather than a general
650	    limit on depth estimation.
651	
652	    '
653	- name: cross_model_chains
654	  plan_id: plan_007
655	  description: 'Cross-model chains (different generator per depth step) vs single-model
656	    chains. Tests ecological validity for real web contamination scenarios.
657	
658	    '
659	  expected_results:
660	    cross_model_logo_f1: 0.56
661	    single_model_logo_f1: 0.64
662	    cross_model_within_f1: 0.68
663	    cross_model_entropy_mean_rho: -0.41
664	    cross_model_ttr_slope: -0.039
665	    cross_model_h1_stable: true
666	    cross_model_gen0_f1: 0.78
667	    cross_model_gen1_f1: 0.46
668	    cross_model_gen2plus_f1: 0.44
669	  result_rationale: 'Cross-model chains inject between-model distributional variance
670	    at each depth step. When generator changes between depths (e.g., Pythia→OLMo→Qwen),
671	    the NLL features measured by the reference model reflect not just depth-related
672	    drift but also generator-switching effects — the reference model''s NLL for OLMo-generated
673	    text differs from Pythia-generated text regardless of depth. This noise source
674	    partially masks the depth signal, particularly for gen-1 vs gen-2+ where the depth
675	    effect is smaller than the generator effect. Gen-0 (human) remains well-separated
676	    (F1 0.78) because all chains share the same human seed distribution. The F1 drop
677	    from 0.64 (single-model LOGO) to 0.56 (cross-model) quantifies the cost of realistic
678	    generator diversity. H1 features remain stable even in cross-model chains, confirming
679	    that shape stationarity is generator-intrinsic.
680	
681	    '
682	  tables:
683	  - name: 'Table 12: Cross-model vs Single-model Chain Classification'
684	    columns:
685	    - chain_type
686	    - logo_f1
687	    - gen0_f1
688	    - gen1_f1
689	    - gen2plus_f1
690	    - entropy_mean_rho
691	    rows:
692	    - - Single-model
693	      - 0.64
694	      - 0.83
695	      - 0.57
696	      - 0.58
697	      - -0.68
698	    - - Cross-model
699	      - 0.56
700	      - 0.78
701	      - 0.46
702	      - 0.44
703	      - -0.41
704	  figures_description:
705	  - 'Fig 11: Confusion matrices for cross-model chains — gen-1/gen-2+ are heavily
706	    confused due to generator-switching noise dominating depth signal.'
707	  analysis: 'Cross-model chains degrade depth estimation significantly (-0.08 F1).
708	    This is a realistic limitation: web contamination involves diverse generators,
709	    and the current feature set partially conflates generator identity with depth.
710	    Paper should present this as an honest ecological validity test — depth estimation
711	    is most reliable for single-source contamination, and cross-model scenarios require
712	    future work on generator-invariant features.
713	
714	    '
715	- name: multi_domain_seeds
716	  plan_id: plan_008
717	  description: 'Expand to 4 domains: Wikipedia, news (CNN/DM), scientific (S2ORC),
718	    creative (WritingPrompts). 500 seeds per domain × 5 depths × 5 generators.
719	
720	    '
721	  expected_results:
722	    wikipedia_logo_f1: 0.67
723	    news_logo_f1: 0.64
724	    scientific_logo_f1: 0.62
725	    creative_logo_f1: 0.57
726	    pooled_multidomain_logo_f1: 0.63
727	    domain_f1_std: 0.037
728	    wikipedia_entropy_mean_rho: -0.72
729	    creative_entropy_mean_rho: -0.48
730	    cross_domain_train_test_f1: 0.58
731	  result_rationale: 'Wikipedia seeds yield highest F1 (0.67) because Wikipedia prose
732	    is stylistically uniform and formulaic — generators produce characteristically
733	    homogeneous continuations that maximize distributional drift consistency across
734	    depths. Creative writing seeds yield lowest F1 (0.57) because creative text has
735	    high intrinsic variance (diverse styles, tones, registers), which creates a larger
736	    noise floor that depth signal must overcome. The generator''s creative outputs
737	    at depth-1 can be as distributionally diverse as human creative text, blurring
738	    the gen-0/gen-1 boundary. Scientific text (0.62) occupies the middle ground: constrained
739	    register but technical vocabulary creates complex distributional patterns. Cross-domain
740	    train-test (train on 3 domains, test on 1) drops to 0.58, suggesting partial domain
741	    adaptation in the classifier.
742	
743	    '
744	  tables:
745	  - name: 'Table 13: Domain-Specific LOGO Results'
746	    columns:
747	    - domain
748	    - logo_f1
749	    - entropy_mean_rho
750	    - ttr_slope
751	    - n_seeds
752	    rows:
753	    - - Wikipedia
754	      - 0.67
755	      - -0.72
756	      - -0.078
757	      - 500
758	    - - News (CNN/DM)
759	      - 0.64
760	      - -0.63
761	      - -0.065
762	      - 500
763	    - - Scientific (S2ORC)
764	      - 0.62
765	      - -0.58
766	      - -0.059
767	      - 500
768	    - - Creative (WritingPrompts)
769	      - 0.57
770	      - -0.48
771	      - -0.041
772	      - 500
773	    - - Pooled
774	      - 0.63
775	      - -0.6
776	      - -0.061
777	      - 2000
778	  figures_description:
779	  - 'Fig 12: Domain-specific entropy_mean drift plots — four panels showing depth
780	    0-4 trends. Wikipedia shows tightest confidence bands; creative shows widest.'
781	  analysis: 'Domain variation (std 0.037) is non-trivial but depth signal generalizes
782	    across all four domains. Creative writing is the hardest domain, consistent with
783	    high intrinsic variance. Paper should report pooled results as primary and domain-specific
784	    as supplementary analysis, noting that domain adaptation (train/test domain mismatch)
785	    is an additional challenge beyond generator generalization.
786	
787	    '
788	- name: finer_grained_ordinal
789	  plan_id: plan_009
790	  description: '5-class ordinal classification (gen-0 through gen-4) on non-paraphrastic
791	    chains. Tests whether depth signal supports finer than 3-class resolution.
792	
793	    '
794	  expected_results:
795	    five_class_macro_f1: 0.43
796	    five_class_gen0_f1: 0.73
797	    five_class_gen1_f1: 0.52
798	    five_class_gen2_f1: 0.35
799	    five_class_gen3_f1: 0.29
800	    five_class_gen4_f1: 0.28
801	    ordinal_mae: 0.72
802	    three_class_macro_f1_same_data: 0.64
803	    adjacent_confusion_rate: 0.61
804	    spearman_pred_vs_true: 0.74
805	  result_rationale: '5-class F1 (0.43) drops substantially from 3-class (0.64) because
806	    distributional differences between adjacent depths (gen-2 vs gen-3, gen-3 vs gen-4)
807	    are small — the drift per step is roughly constant, but the cumulative difference
808	    between gen-0 and gen-4 is spread across 4 boundaries, each of which is harder
809	    than the 3-class boundaries. Gen-0 is still well-separated (0.73) because human
810	    vs any synthetic is the largest distributional gap. Gen-1 (0.52) is intermediate
811	    — distinguishable from gen-0 and gen-2+ but with confusion on both sides. Gen-2/3/4
812	    collapse into a muddy cluster (F1 0.28-0.35) because by depth-2, recursive drift
813	    has already consumed most of the easy-to-detect signal, and remaining differences
814	    are within the noise floor. However, ordinal Spearman (0.74) is respectable, showing
815	    the classifier preserves rank order even when exact class assignment fails — errors
816	    are predominantly between adjacent classes (61% of errors), not distant ones.
817	
818	    '
819	  tables:
820	  - name: 'Table 14: 5-class Ordinal Classification (LOGO, Full Features)'
821	    columns:
822	    - class
823	    - f1
824	    - precision
825	    - recall
826	    - most_confused_with
827	    rows:
828	    - - gen-0
829	      - 0.73
830	      - 0.78
831	      - 0.69
832	      - gen-1
833	    - - gen-1
834	      - 0.52
835	      - 0.49
836	      - 0.55
837	      - gen-0 / gen-2
838	    - - gen-2
839	      - 0.35
840	      - 0.33
841	      - 0.37
842	      - gen-3
843	    - - gen-3
844	      - 0.29
845	      - 0.31
846	      - 0.27
847	      - gen-2 / gen-4
848	    - - gen-4
849	      - 0.28
850	      - 0.26
851	      - 0.3
852	      - gen-3
853	  figures_description:
854	  - 'Fig 13: 5×5 confusion matrix heatmap — strong diagonal for gen-0, increasingly
855	    diffuse for deeper classes. Off-diagonal mass concentrated on ±1 adjacent cells.'
856	  - 'Fig 14: Predicted vs true depth scatter with ordinal regression line (Spearman
857	    ρ=0.74).'
858	  analysis: 'Finer-grained classification is feasible but noisy beyond 3 classes.
859	    The 3-class grouping (gen-0/gen-1/gen-2+) appears to be the natural resolution
860	    supported by the current feature set. Paper presents 5-class as secondary analysis
861	    motivating ordinal regression approaches in future work. The high ordinal Spearman
862	    (0.74) suggests the classifier captures depth ordering even when exact classification
863	    fails, which is useful for risk scoring applications.
864	
865	    '
866	- name: human_edit_robustness
867	  plan_id: plan_010
868	  description: 'Robustness to simulated human edits: (A) random word replacement at
869	    5%/10%/20%, (B) LLM-simulated light rephrasing. Tests whether post-processing
870	    destroys depth signal.
871	
872	    '
873	  expected_results:
874	    baseline_no_edit_f1: 0.82
875	    random_5pct_f1: 0.79
876	    random_10pct_f1: 0.72
877	    random_20pct_f1: 0.6
878	    llm_light_edit_f1: 0.73
879	    random_5pct_entropy_mean_rho: -0.63
880	    random_10pct_entropy_mean_rho: -0.52
881	    random_20pct_entropy_mean_rho: -0.35
882	    llm_light_edit_entropy_mean_rho: -0.49
883	    h1_features_robust_to_edit: true
884	    shape_features_max_rho_change: 0.07
885	  result_rationale: 'Random word replacement progressively corrupts the text''s distributional
886	    profile. At 5%, the corruption is below the feature noise floor — surface features
887	    (TTR, hapax) are slightly perturbed but NLL features remain stable because 5%
888	    random words don''t substantially alter the reference model''s token-level surprise
889	    distribution. At 20%, the text becomes distributionally anomalous in a way that
890	    overwhelms the depth signal — randomly inserted words create a uniform noise pattern
891	    that masks depth-specific distributional drift. LLM-simulated editing (F1 0.73)
892	    falls between 5% and 10% random replacement because LLM edits are more natural
893	    (preserving grammaticality) but more targeted (selectively replacing awkward or
894	    repetitive phrases that carry depth signal). Shape features remain robust (max
895	    ρ change 0.07) because random/LLM edits affect vocabulary composition (level)
896	    more than distributional shape.
897	
898	    '
899	  tables:
900	  - name: 'Table 15: Robustness to Simulated Human Edits'
901	    columns:
902	    - edit_type
903	    - edit_rate
904	    - macro_f1
905	    - delta_f1
906	    - entropy_mean_rho
907	    rows:
908	    - - None (baseline)
909	      - 0%
910	      - 0.82
911	      - —
912	      - -0.68
913	    - - Random word
914	      - 5%
915	      - 0.79
916	      - -0.03
917	      - -0.63
918	    - - Random word
919	      - 10%
920	      - 0.72
921	      - -0.1
922	      - -0.52
923	    - - Random word
924	      - 20%
925	      - 0.6
926	      - -0.22
927	      - -0.35
928	    - - LLM light rephrase
929	      - ~8%
930	      - 0.73
931	      - -0.09
932	      - -0.49
933	  figures_description:
934	  - 'Fig 15: F1 degradation curve as function of edit rate — roughly linear decline
935	    with inflection around 15%. LLM editing point plotted at estimated ~8% token change
936	    rate.'
937	  analysis: 'Depth signal is moderately robust to light editing (5%) but degrades
938	    meaningfully at 10%+. Real-world human editing likely falls in the 5-15% range,
939	    placing expected performance at F1 0.72-0.79. Paper presents this as honest robustness
940	    analysis — depth estimation is viable for lightly edited synthetic text but fragile
941	    under heavy post-processing. This limits practical applicability to scenarios
942	    where contamination involves minimally edited LLM outputs.
943	
944	    '
945	- name: ld_score_feature
946	  plan_id: plan_011
947	  description: 'Add LD-Score as feature. Test pre-registered prediction that LD-Score
948	    is a level feature (H2 drift). Evaluate marginal classification improvement.
949	
950	    '
951	  expected_results:
952	    ld_score_depth_rho: -0.55
953	    ld_score_slope: -0.042
954	    ld_score_r2: 0.72
955	    ld_score_classification: H2_level
956	    preregistered_prediction_confirmed: true
957	    f1_with_ld_score: 0.83
958	    f1_without_ld_score: 0.82
959	    marginal_improvement: 0.01
960	    ld_score_correlation_with_ttr: 0.68
961	    ld_score_correlation_with_hapax: 0.61
962	  result_rationale: 'LD-Score measures character-level distributional properties,
963	    which are downstream of vocabulary composition — as depth increases and vocabulary
964	    impoverishes (fewer unique words, more repetitive character n-grams), LD-Score
965	    shifts accordingly. This confirms it is a level feature (H2), sensitive to the
966	    same vocabulary/diversity drift as TTR and hapax_ratio. The pre-registered prediction
967	    is validated (ρ=-0.55, clearly H2), strengthening the level/shape framework''s
968	    predictive power. However, the high correlation with existing surface features
969	    (0.61-0.68 with TTR/hapax) means LD-Score provides little incremental information
970	    — the marginal F1 gain is only 0.01. The character-level signal is largely redundant
971	    with word-level diversity features already in the feature set.
972	
973	    '
974	  tables:
975	  - name: 'Table 16: LD-Score Feature Analysis'
976	    columns:
977	    - metric
978	    - value
979	    rows:
980	    - - LD-Score depth ρ
981	      - -0.55
982	    - - LD-Score linear slope
983	      - -0.042
984	    - - LD-Score R²
985	      - 0.72
986	    - - H1/H2 classification
987	      - H2 (level)
988	    - - Pre-registered prediction
989	      - Confirmed
990	    - - Correlation with TTR
991	      - 0.68
992	    - - Correlation with hapax_ratio
993	      - 0.61
994	    - - F1 with LD-Score
995	      - 0.83
996	    - - F1 without LD-Score
997	      - 0.82
998	  figures_description:
999	  - 'Fig 16: LD-Score depth trend (mean ± std, depths 0-4) overlaid with TTR trend
1000	    — similar decline pattern, confirming shared level/diversity dynamics at character
1001	    level.'
1002	  analysis: 'Pre-registered prediction confirmed: LD-Score is a level feature. This
1003	    is a minor but clean validation of the H1/H2 framework''s predictive utility.
1004	    However, the marginal classification improvement is negligible (0.01), so LD-Score
1005	    is presented as a validation data point rather than a feature engineering contribution.
1006	    The high correlation with existing features suggests character-level and word-level
1007	    diversity measures capture the same underlying depth signal.
1008	
1009	    '
1010	- name: end_to_end_classifier
1011	  plan_id: plan_012
1012	  description: 'QLoRA fine-tuned Qwen3-0.6B for end-to-end depth classification. Compares
1013	    learned representations vs handcrafted distributional features.
1014	
1015	    '
1016	  expected_results:
1017	    qlora_macro_f1: 0.79
1018	    qlora_gen0_f1: 0.92
1019	    qlora_gen1_f1: 0.73
1020	    qlora_gen2plus_f1: 0.72
1021	    handcrafted_macro_f1: 0.82
1022	    qlora_cross_gen_logo_f1: 0.61
1023	    handcrafted_cross_gen_logo_f1: 0.64
1024	    qlora_training_time_hours: 6.2
1025	    qlora_inference_tokens_per_sec: 145
1026	    handcrafted_inference_tokens_per_sec: 8900
1027	  result_rationale: 'QLoRA achieves slightly lower F1 (0.79 vs 0.82) because the depth
1028	    classification task has limited training data (~25K samples) — insufficient for
1029	    a 600M-parameter model to learn robust depth-specific representations from scratch.
1030	    The model likely overfits to generator- specific patterns rather than learning
1031	    the distributional drift abstraction that handcrafted features explicitly encode.
1032	    Cross-generator LOGO (0.61 vs 0.64) shows the end-to-end approach generalizes
1033	    slightly worse, further suggesting it memorizes generator identities. The handcrafted
1034	    approach also has a massive inference speed advantage (~60x) because it requires
1035	    only a forward pass through the small reference model + simple statistics, vs
1036	    full sequence processing through a 600M model. This confirms the paper''s positioning:
1037	    the contribution is the problem formulation and empirical findings, not a competition
1038	    for SOTA — simple features suffice for the task.
1039	
1040	    '
1041	  tables:
1042	  - name: 'Table 17: End-to-End vs Handcrafted Features'
1043	    columns:
1044	    - method
1045	    - within_gen_f1
1046	    - logo_f1
1047	    - inference_speed
1048	    - training_cost
1049	    rows:
1050	    - - Handcrafted (XGBoost)
1051	      - 0.82
1052	      - 0.64
1053	      - 8900 tok/s
1054	      - ~0 GPU-h
1055	    - - QLoRA (Qwen3-0.6B)
1056	      - 0.79
1057	      - 0.61
1058	      - 145 tok/s
1059	      - 6.2 GPU-h
1060	  figures_description:
1061	  - 'Fig 17: F1 comparison bar chart (within-gen and LOGO) for handcrafted vs QLoRA.
1062	    Handcrafted is slightly better on both metrics while being 60x faster at inference.'
1063	  analysis: 'End-to-end approach does not outperform handcrafted features, confirming
1064	    that the task''s information content is well-captured by simple distributional
1065	    statistics. This validates the paper''s contribution positioning: novelty lies
1066	    in the problem formulation and empirical findings, not in model architecture.
1067	    The interpretability and efficiency advantages of handcrafted features are a practical
1068	    benefit for deployment in data curation pipelines.
1069	
1070	    '
1071	- name: text_length_control
1072	  plan_id: plan_013
1073	  description: 'Length confound analysis: (A) length distributions by depth, (B) length-normalized
1074	    features, (C) length-matched classification. Critical confound control.
1075	
1076	    '
1077	  expected_results:
1078	    mean_length_gen0: 315
1079	    mean_length_gen1: 289
1080	    mean_length_gen2: 263
1081	    mean_length_gen3: 246
1082	    mean_length_gen4: 237
1083	    length_depth_pearson_r: -0.41
1084	    length_depth_kw_p: <0.001
1085	    original_surface_f1: 0.76
1086	    length_controlled_surface_f1: 0.71
1087	    length_controlled_surface_f1_delta: -0.05
1088	    original_reference_f1: 0.72
1089	    length_controlled_reference_f1: 0.7
1090	    length_controlled_reference_f1_delta: -0.02
1091	    original_full_f1: 0.82
1092	    length_controlled_full_f1: 0.78
1093	    length_controlled_full_f1_delta: -0.04
1094	    length_matched_subsample_full_f1: 0.79
1095	    fixed_window_ttr_slope: -0.048
1096	    fixed_window_ttr_original_slope: -0.071
1097	    fixed_window_hapax_slope: -0.037
1098	    fixed_window_hapax_original_slope: -0.054
1099	    residual_signal_confirmed: true
1100	  result_rationale: 'Text length decreases monotonically with depth (315→237 tokens)
1101	    because recursive generation tends to produce slightly shorter texts — generators
1102	    are biased toward completing thoughts within a typical output length, and each
1103	    depth step compounds this tendency. This creates a legitimate confound: TTR and
1104	    hapax_ratio are mechanically length-dependent (shorter texts have higher TTR/hapax
1105	    by construction). The -0.05 surface F1 drop after length control confirms that
1106	    ~30% of the surface feature signal was tracking length, not depth. However, the
1107	    residual signal (F1 0.71 after control, well above chance at 0.33) confirms that
1108	    depth drives genuine vocabulary impoverishment beyond what length explains. Reference
1109	    features lose less (-0.02) because NLL statistics are computed token-by-token
1110	    and are less length-sensitive — the per-token surprise distribution shifts with
1111	    depth regardless of total text length. The full-feature length-controlled F1 (0.78)
1112	    remains substantially above chance and above either feature subset, confirming
1113	    the core claims survive length control.
1114	
1115	    '
1116	  tables:
1117	  - name: 'Table 18: Text Length by Depth'
1118	    columns:
1119	    - depth
1120	    - mean_tokens
1121	    - std_tokens
1122	    - median_tokens
1123	    rows:
1124	    - - gen-0
1125	      - 315
1126	      - 82
1127	      - 298
1128	    - - gen-1
1129	      - 289
1130	      - 76
1131	      - 274
1132	    - - gen-2
1133	      - 263
1134	      - 71
1135	      - 251
1136	    - - gen-3
1137	      - 246
1138	      - 68
1139	      - 237
1140	    - - gen-4
1141	      - 237
1142	      - 65
1143	      - 228
1144	  - name: 'Table 19: Length-Controlled Classification Results'
1145	    columns:
1146	    - feature_set
1147	    - original_f1
1148	    - length_controlled_f1
1149	    - delta
1150	    - delta %
1151	    rows:
1152	    - - Full
1153	      - 0.82
1154	      - 0.78
1155	      - -0.04
1156	      - -4.9%
1157	    - - Surface only
1158	      - 0.76
1159	      - 0.71
1160	      - -0.05
1161	      - -6.6%
1162	    - - Reference only
1163	      - 0.72
1164	      - 0.7
1165	      - -0.02
1166	      - -2.8%
1167	  - name: 'Table 20: Fixed-Window Feature Slopes (128-token windows)'
1168	    columns:
1169	    - feature
1170	    - original_slope
1171	    - fixed_window_slope
1172	    - slope_reduction_pct
1173	    rows:
1174	    - - TTR
1175	      - -0.071
1176	      - -0.048
1177	      - 32%
1178	    - - hapax_ratio
1179	      - -0.054
1180	      - -0.037
1181	      - 31%
1182	    - - entropy_mean
1183	      - -0.148
1184	      - -0.139
1185	      - 6%
1186	  figures_description:
1187	  - 'Fig 18: Text length distribution violin plots by depth — clear leftward shift
1188	    with depth. Overlapping distributions confirm length is a partial, not sole, confound.'
1189	  - 'Fig 19: Feature slopes before/after length control — surface features show ~30%
1190	    reduction; reference features show <10% reduction. Visualizes the differential
1191	    length sensitivity.'
1192	  analysis: 'Length is a real but partial confound. The 0.05 surface F1 drop is within
1193	    the median range [-0.08, -0.03] and must be acknowledged honestly in the paper.
1194	    The key finding is that residual signal survives: depth drives genuine distributional
1195	    drift beyond length artifacts. Reference features are relatively length-robust
1196	    (only 0.02 drop), strengthening their value in the feature set. Paper should add
1197	    length-controlled analysis as a supplementary validation table and note: ''Surface
1198	    features partially track text length, but residual depth signal persists after
1199	    length control. Reference features provide length-robust complementary signal.''
1200	
1201	    '
1202	- name: large_scale_generator
1203	  plan_id: plan_014
1204	  description: 'Add Qwen3-8B-Base as 7B+ generator. 1000 seeds × 5 depths. Tests whether
1205	    depth signal persists at frontier scale.
1206	
1207	    '
1208	  expected_results:
1209	    qwen8b_3class_macro_f1: 0.57
1210	    qwen8b_gen0_f1: 0.76
1211	    qwen8b_gen1_f1: 0.48
1212	    qwen8b_gen2plus_f1: 0.46
1213	    qwen8b_entropy_mean_rho: -0.38
1214	    qwen8b_ttr_slope: -0.042
1215	    qwen8b_hapax_slope: -0.032
1216	    qwen8b_vs_pythia28b_f1_gap: -0.25
1217	    qwen8b_vs_qwen17b_f1_gap: -0.05
1218	    qwen8b_h1_features_stable: true
1219	    qwen8b_entropy_std_rho: 0.05
1220	    qwen8b_tail_decay_rho: -0.07
1221	    qwen8b_5class_f1: 0.31
1222	    logo_with_8b_included: 0.61
1223	  result_rationale: '7B+ generators produce substantially more fluent text that compresses
1224	    the depth signal. At 8B parameters, the model has sufficient capacity to maintain
1225	    diverse vocabulary and natural distributional properties even at depth-4 — vocabulary
1226	    impoverishment is less severe because the model''s larger vocabulary and richer
1227	    internal representations allow it to produce varied continuations even from distributionally
1228	    drifted inputs. The F1 drop from 0.82 (Pythia-2.8B) to 0.57 (Qwen3-8B) is large
1229	    but the signal remains non-trivial (well above chance at 0.33). Entropy_mean ρ
1230	    attenuates from -0.68 to -0.38, consistent with weaker but non-zero drift — the
1231	    8B model''s NLL distribution still shifts with depth but less per step. Gen-0
1232	    remains distinguishable (F1 0.76) because the human-vs-any-synthetic gap is robust
1233	    to model scale, but gen-1 vs gen-2+ becomes very noisy (0.46-0.48). H1 features
1234	    remain stable (shape stationarity is scale-invariant). This is an honest scaling
1235	    result: depth estimation weakens at scale but doesn''t vanish, motivating future
1236	    work on scale-robust features.
1237	
1238	    '
1239	  tables:
1240	  - name: 'Table 21: 7B+ Generator Depth Classification'
1241	    columns:
1242	    - generator
1243	    - params
1244	    - macro_f1
1245	    - entropy_mean_rho
1246	    - ttr_slope
1247	    rows:
1248	    - - Pythia-2.8B
1249	      - 2.8B
1250	      - 0.82
1251	      - -0.68
1252	      - -0.071
1253	    - - Pythia-1B
1254	      - 1B
1255	      - 0.8
1256	      - -0.65
1257	      - -0.068
1258	    - - OLMo-2-1B
1259	      - 1.5B
1260	      - 0.78
1261	      - -0.61
1262	      - -0.063
1263	    - - Qwen3-1.7B
1264	      - 1.7B
1265	      - 0.75
1266	      - -0.56
1267	      - -0.055
1268	    - - Qwen3-0.6B
1269	      - 0.6B
1270	      - 0.77
1271	      - -0.59
1272	      - -0.061
1273	    - - Qwen3-8B
1274	      - 8B
1275	      - 0.57
1276	      - -0.38
1277	      - -0.042
1278	  - name: 'Table 22: Scale Trend Analysis'
1279	    columns:
1280	    - metric
1281	    - ≤2.8B mean
1282	    - 8B
1283	    - delta
1284	    - interpretation
1285	    rows:
1286	    - - macro_f1
1287	      - 0.78
1288	      - 0.57
1289	      - -0.21
1290	      - Signal weakens at scale
1291	    - - entropy_mean ρ
1292	      - -0.62
1293	      - -0.38
1294	      - '+0.24'
1295	      - Drift attenuates at scale
1296	    - - TTR slope
1297	      - -0.064
1298	      - -0.042
1299	      - '+0.022'
1300	      - Less vocab impoverishment
1301	    - - H1 max |ρ|
1302	      - 0.08
1303	      - 0.07
1304	      - '-0.01'
1305	      - Shape stationarity preserved
1306	  figures_description:
1307	  - 'Fig 20: F1 vs generator parameter count (log scale). Clear downward trend from
1308	    0.6B-2.8B cluster to 8B outlier. Dotted line at chance (0.33) for reference.'
1309	  - 'Fig 21: Entropy_mean depth trend for 8B (shallow slope) vs 2.8B (steep slope).
1310	    Both monotonically decreasing but 8B slope is ~55% of 2.8B slope.'
1311	  analysis: '7B+ results confirm the scaling concern. Depth signal is weaker but non-zero
1312	    (F1 0.57, significantly above chance p<0.001). The paper should present this as
1313	    an honest scaling analysis in a dedicated subsection: ''Depth signal attenuates
1314	    with generator scale, consistent with larger models maintaining distributional
1315	    diversity under recursive generation. At 8B parameters, gen-0 vs synthetic remains
1316	    detectable, but fine-grained depth estimation (gen-1 vs gen-2+) approaches noise
1317	    floor. This motivates future work on scale-robust features, potentially leveraging
1318	    model-specific distributional properties.'' The 8B result transforms from a weakness
1319	    into a scientific finding: the relationship between model capacity and depth signal
1320	    decay is itself an interesting empirical contribution.'
1321	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b45d6cc7-2ccd-49a8-9b6b-6a8a45fab4ca",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "6e4dd06e-3751-4d77-97fa-ae3e2cb1926f",
  "sourceToolAssistantUUID": "b45d6cc7-2ccd-49a8-9b6b-6a8a45fab4ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-14T23:08:30.696Z_

Now let me also read the review reports from the dream to understand what prior reviews said.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e4dd06e-3751-4d77-97fa-ae3e2cb1926f",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JWu4sdwkgHevLvVRqS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85a28b7f-e4b4-41a6-9448-2ecb771113ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vv5hd38GNH4pfr9XkF4teg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34626,
      "cache_read_input_tokens": 31287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34626,
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

_source line 41 · 2026-05-14T23:08:33.525Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JGgD3KTKjMuQR2HUv9bn4T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85a28b7f-e4b4-41a6-9448-2ecb771113ce",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JWu4sdwkgHevLvVRqS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8439b4b0-e2eb-4592-ae91-ea15e2ef8f3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vv5hd38GNH4pfr9XkF4teg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34626,
      "cache_read_input_tokens": 31287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34626,
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

_source line 42 · 2026-05-14T23:08:33.530Z_

<details><summary>↩ Tool result · `toolu_01JGgD3KTKjMuQR2HUv9bn4T`</summary>

```text
1	---
2	dream_id: dream_20260514T221538
3	tier: median
4	overall_score: 4/6 Weak Accept — Borderline
5	timestamp: 2026-05-14T23:06:30.588841+00:00
6	---
7	
8	# Dream Review Report: Distributional Fingerprinting for Generation Depth Estimation
9	
10	**Paper**: "Distributional Fingerprinting for Generation Depth Estimation in Recursive LLM Output"
11	**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)
12	**Date**: 2026-05-14
13	
14	---
15	
16	## Reviewer Assignments
17	
18	- **R1** (Methods + Experiments): Score **4/6 Weak Accept**, Confidence 4/5
19	- **R2** (Novelty + Related Work): Score **3/6 Weak Reject**, Confidence 4/5
20	
21	---
22	
23	## Step 1: Independent Reviews
24	
25	### R1 — Methods and Experiments
26	
27	**Strengths:**
28	1. Well-designed evaluation hierarchy: in-distribution CV → LOGO → LOFO → cross-reference → cross-model chains, systematically peeling away confounds.
29	2. Thorough confound control: text length analysis (Sec 4.4), reference model circularity avoidance (OLMo-1B for downstream), size-matched filtering comparison.
30	3. Complete experiment coverage: all 14 planned experiments appear in the paper, covering generators, domains, prompt types, chain types, editing robustness, scaling, and baselines.
31	4. Paraphrastic comparison provides theoretical grounding by connecting to attractor cycle theory.
32	5. QLoRA comparison validates the feature-based approach (handcrafted F1=0.82/0.64 beats QLoRA F1=0.79/0.61 at 60× lower cost).
33	6. Cross-reference model validation (3 independent reference models) is the correct falsification test for dual dynamics.
34	7. Pre-registered LD-Score prediction provides out-of-sample framework validation.
35	8. Honest limitation reporting throughout.
36	
37	**Weaknesses:**
38	1. **R² on 5 aggregated depth points (Table 2) is statistically weak.** Linear regression on 5 group means provides inflated R² values with essentially no meaningful degrees of freedom. This is the empirical backbone of the H1/H2 partition (Claim 2). Individual-level Spearman correlations with CIs are needed.
39	2. **No per-generator CIs on LOGO results (Table 3).** Point estimates without confidence intervals make it impossible to assess whether the Pythia-family advantage (0.71–0.72 vs 0.59–0.62) is significant or within noise.
40	3. **H1/H2 partition sensitivity is untested.** The clean R² split (≥0.81 vs ≤0.06) with no features in the ambiguous zone could be an artifact of the specific 7 features chosen. Adding features like entropy_median, kurtosis, or skewness might blur the boundary.
41	4. **Shared reference model confounds LOGO generalization claims.** All primary LOGO experiments use Pythia-410M for feature extraction. Pythia generators' higher LOGO F1 may partly reflect shared tokenizer/pretraining data, not depth signal transfer.
42	5. **No existing detector scores tested as ordinal baselines.** FastDetectGPT and LD-Score produce continuous scores that could be regressed on depth. Without this comparison, it's unclear whether depth-specific feature engineering adds value.
43	6. **No individual leave-one-feature-out ablation.** The coarse 3-way ablation (Table 1) doesn't clarify per-feature importance.
44	7. **No calibration analysis.** For risk-stratified curation, reliability diagrams and ECE for classifier confidence would be important.
45	8. **Continuation-chain-dominant headline numbers overstate practical accuracy.** F1=0.82 is for continuation; under elaboration (0.77), inspired rewriting (0.69), or cross-model chains (0.56), performance is substantially lower. The abstract should more prominently frame the realistic range.
46	9. **Hyperparameter sensitivity not analyzed** for XGBoost.
47	10. **Missing real-world web data evaluation.** All experiments are on synthetic chains; no test on naturally occurring recursive web content.
48	
49	**Questions for Authors:**
50	1. Are Table 2 R² values on group means or individual samples? What are individual-level Spearman ρ with CIs?
51	2. What happens to the H1/H2 partition with additional features (kurtosis, skewness, burstiness)?
52	3. Have you tested FastDetectGPT continuous scores as ordinal depth predictors?
53	4. Can you provide per-generator bootstrap CIs for Table 3?
54	5. Why were only base models tested, not instruction-tuned models that dominate real-world generation?
55	
56	### R2 — Novelty and Related Work
57	
58	**Strengths:**
59	1. Genuinely novel task formulation: ordinal depth estimation beyond binary detection is a real gap in the literature.
60	2. Comprehensive experimental design addresses most obvious objections preemptively.
61	3. Honest self-assessment of limitations is refreshing and appropriate for the evidence presented.
62	4. Pre-registered LD-Score prediction adds genuine out-of-sample validation.
63	5. Appropriate contribution positioning: the paper correctly identifies its contribution as empirical/conceptual rather than methodological.
64	
65	**Weaknesses:**
66	1. **No methodological novelty.** All features are standard (TTR/hapax from computational linguistics; NLL stats from DetectGPT family). XGBoost is off-the-shelf. A new classification target without new methods is insufficient for a top venue by itself—the burden falls entirely on the empirical findings being genuinely surprising.
67	2. **"Dual dynamics" is overframed.** The observation that central-tendency statistics (means) drift under distributional shift while spread statistics (std, min, max) remain stable is a well-known property of location-shift processes. The H1/H2 naming borrows time-series terminology to dress up this observation. The "cross-cutting" argument (entropy_mean is reference-derived but drifts, while entropy_std is also reference-derived but stationary) is a statistical triviality: mean and variance of the same distribution measure different things and respond differently to location shifts. No theoretical analysis is provided to explain *why* shape features should be stationary.
68	3. **"Reference-model-modulated" qualifier reveals a weakness, not a strength.** Drift magnitude varying 2× across reference models means the phenomenon depends on reference–generator alignment, undermining claims of universality. The paper correctly reframes this as modulation rather than universality, but this honest framing also reduces the conceptual contribution.
69	4. **Downstream utility fails statistical significance.** CIs overlap between depth-aware filtering and FastDetectGPT (5.2% [3.8, 7.1] vs 3.8% [2.1, 5.9]). Contribution 3 is not supported at conventional significance levels. The sample-matched comparison further narrows the gap (2.8% vs 1.9%, CIs overlapping).
70	5. **LOGO F1=0.64 is not practically useful.** In a 3-class problem with macro-F1=0.64, the system is wrong more than a third of the time. Gen-1 F1=0.57 and gen-2+ F1=0.58 are barely above chance for those specific classes. This is a proof-of-concept, not a deployable system.
71	6. **7B+ signal attenuation (F1=0.57) is existential.** If depth signal weakens substantially at 8B and frontier models are 70B–400B+, the method may be inapplicable to the most practically important generators. The paper acknowledges this but doesn't adequately grapple with its implications for the contribution's longevity.
72	7. **Missing related work in stylometry and authorship attribution.** The stylometric tradition of using lexical diversity and distributional features for author identification is directly relevant (Stamatatos 2009, Koppel et al. 2009, Neal et al. 2017). The paper's feature set is essentially a stylometric profile applied to a new classification target.
73	8. **Missing related work on iterative/multi-step generation analysis.** Works on detecting chain-of-thought artifacts, multi-hop generation analysis, or recursive self-improvement detection are potentially relevant.
74	9. **The "distributional fingerprinting" title overclaims.** The method extracts 7 standard features and runs XGBoost. "Fingerprinting" implies something more distinctive or identifying.
75	
76	**Questions for Authors:**
77	1. Can you provide a theoretical account (even informal) of why shape features should be stationary under recursive generation?
78	2. How do you respond to the concern that "dual dynamics" is simply the known behavior of location vs. scale statistics under distributional shift?
79	3. Given 7B+ attenuation, what is the path to making this method relevant for frontier models?
80	4. Have you considered the stylometry literature (Stamatatos 2009, etc.) as related work?
81	5. Is LOGO F1=0.64 useful in any practical data curation pipeline, or is this a proof-of-concept?
82	
83	---
84	
85	## Step 2: Cross-Sharing
86	
87	After exchanging reviews, both reviewers converge on several points:
88	
89	**R1 after reading R2:** "R2's point about dual dynamics being a known property of location-shift processes is well-taken and something I flagged more mildly as 'the R² analysis being statistically weak.' I now see this as a more fundamental conceptual concern: the observation itself may not be as surprising as the paper frames it. I also agree that the missing stylometry literature is a gap. However, I maintain that the *task formulation* (ordinal depth estimation) is genuinely novel and the comprehensiveness of experiments has value even if the conceptual contribution is simpler than claimed."
90	
91	**R2 after reading R1:** "R1's point about R² on 5 points reinforces my framing concern — not only is the observation conceptually unsurprising, but its statistical evidence is weak. I agree with R1 that the experiment design is thorough and the confound controls are well-handled. I also appreciate R1's observation about missing ordinal baselines from existing detector scores — this is a critical missing comparison that could undermine the paper's claimed contribution if existing detectors already yield reasonable ordinal signal. However, I acknowledge the task formulation novelty more than I initially credited."
92	
93	---
94	
95	## Step 3: Convergence
96	
97	### Points of Agreement
98	
99	1. **Task formulation is genuinely novel.** Ordinal depth estimation beyond binary detection is a real gap in the literature, and the paper correctly identifies it.
100	2. **Experimental comprehensiveness is a strength.** All 14 planned experiments are covered with appropriate controls and honest reporting.
101	3. **"Dual dynamics" is overframed.** The level-vs-shape split is either (a) a known property of location-shift processes (R2) or (b) insufficiently evidenced by R² on 5 points (R1). Either way, the conceptual contribution is inflated relative to the evidence.
102	4. **Downstream utility claim is not statistically supported.** CI overlap between depth-aware and binary filtering precludes a "significantly outperforms" claim.
103	5. **Cross-generator generalization is modest at best.** LOGO F1=0.64, LOFO F1=0.593. Practical deployment would require substantially higher generalization.
104	6. **7B+ scaling concern is serious.** F1=0.57 at 8B parameters raises questions about the method's relevance for frontier models.
105	7. **Missing comparisons:** existing detector scores as ordinal baselines, stylometry literature references.
106	8. **Statistical reporting gaps:** missing CIs on classification metrics, R² on aggregated means, missing calibration analysis.
107	
108	### Key Disagreement
109	
110	R1 weighs the comprehensive experiments more heavily and sees the paper as a solid empirical contribution despite conceptual overframing → **4/6 Weak Accept**.
111	
112	R2 weighs the lack of methodological novelty and the overframed conceptual contribution more heavily, and sees the practical utility as insufficient → **3/6 Weak Reject**.
113	
114	Both acknowledge the paper sits on the accept/reject boundary.
115	
116	---
117	
118	## Step 4: Consolidated Assessment
119	
120	### Overall Score: 4/6 (Weak Accept) — Borderline
121	
122	### Score Justification
123	
124	The paper addresses a genuinely novel task (ordinal depth estimation) that fills a real gap between binary synthetic text detection and the model collapse literature. The experimental design is comprehensive (14 experiments, 6 generators, 4 domains, multiple evaluation protocols) with well-handled confounds and honest limitations. These qualities exceed the bar of most submissions in thoroughness and intellectual honesty.
125	
126	However, the paper is held back by:
127	
128	1. **Overframed central contribution.** "Reference-model-modulated dual dynamics" presents a known statistical property (location statistics drift under distributional shift; shape statistics don't) as a discovery. The H1/H2 framing adds terminology without adding insight. If the paper reframed this as "we observe that central-tendency features drift while spread features remain stable, consistent with recursive generation inducing a location shift in the NLL distribution," the contribution would be honestly sized.
129	
130	2. **Weak statistical evidence for the core claim.** R² on 5 aggregated depth points (Table 2) inflates the apparent strength of the H1/H2 partition. Individual-level correlations with CIs are needed.
131	
132	3. **Modest practical utility.** LOGO F1=0.64 is a proof-of-concept, not a deployable system. Downstream filtering advantage has overlapping CIs with the best binary baseline. The 7B+ attenuation (F1=0.57) raises existential concerns for frontier model applicability.
133	
134	4. **Missing baselines.** Existing detector scores (FastDetectGPT, Binoculars, LD-Score) produce continuous outputs that could serve as ordinal depth predictors. Without this comparison, it's unclear whether the custom feature set adds value.
135	
136	### Why Weak Accept over Weak Reject
137	
138	The task formulation novelty, experimental thoroughness, and honest limitation reporting tip the balance slightly positive. The paper would serve the community by establishing ordinal depth estimation as a research direction and providing a comprehensive empirical baseline. The weaknesses (overframing, statistical gaps) are fixable in revision without fundamental rearchitecting.
139	
140	### Key Revisions Required for Acceptance
141	
142	1. **Deflate "dual dynamics" framing.** Replace the H1/H2 terminology with a straightforward observation about location vs. shape statistics. Remove or qualify the "discovery" language.
143	2. **Replace R² on 5 points (Table 2) with individual-level Spearman correlations** with bootstrap CIs.
144	3. **Add CIs to all main classification tables** (Tables 1, 3, 5, 6, 7, 8, 9).
145	4. **Add ordinal baselines from existing detectors.** Regress FastDetectGPT/Binoculars/LD-Score continuous scores on depth.
146	5. **Add stylometry references** (Stamatatos 2009, Koppel et al. 2009) and discuss the connection.
147	6. **Reframe abstract and conclusion** to foreground the realistic performance range (0.57–0.82 depending on conditions) rather than leading with the best-case 0.82.
148	7. **Add calibration analysis** (ECE, reliability diagram) for the XGBoost classifier.
149	
150	### Experiment Coverage
151	
152	All 14 imagined experiments (plan_001 through plan_014) are present in the paper:
153	
154	| Plan | Description | Section | Covered |
155	|------|-------------|---------|---------|
156	| 001 | Feature ablation + H1/H2 trend | 4.1 | ✓ |
157	| 002 | Cross-generator LOGO | 4.2 | ✓ |
158	| 003 | Cross-family reference model | 4.3 | ✓ |
159	| 004 | Downstream utility | 4.12 | ✓ |
160	| 005 | Prompt type comparison | 4.5 | ✓ |
161	| 006 | Paraphrastic comparison | 4.5 | ✓ |
162	| 007 | Cross-model chains | 4.5 | ✓ |
163	| 008 | Multi-domain seeds | 4.6 | ✓ |
164	| 009 | 5-class ordinal | 4.7 | ✓ |
165	| 010 | Human edit robustness | 4.8 | ✓ |
166	| 011 | LD-Score validation | 4.9 | ✓ |
167	| 012 | End-to-end QLoRA | 4.10 | ✓ |
168	| 013 | Text length control | 4.4 | ✓ |
169	| 014 | 7B+ scaling | 4.11 | ✓ |
170	
171	Coverage: **14/14 (100%)**
172	
173	### Summary
174	
175	A comprehensive empirical study of a genuinely novel task, weakened by overframed conceptual claims and modest practical utility. The task formulation and experimental thoroughness merit publication; the "dual dynamics" framing and statistical presentation need significant revision. Borderline paper that would benefit from honest resizing of contributions.
176	
177	---
178	
179	*Review conducted by 2-reviewer panel (R1: Methods+Experiments, R2: Novelty+Related Work) with full 4-step roundtable protocol.*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8439b4b0-e2eb-4592-ae91-ea15e2ef8f3a",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "e9a55be3-b5ee-40ad-849a-4056c2cf978a",
  "sourceToolAssistantUUID": "8439b4b0-e2eb-4592-ae91-ea15e2ef8f3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T23:08:33.891Z_

<details open><summary>🔧 Tool call — Read · `toolu_015Emjoqd6Xi9bY3zhQ5n8k1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9a55be3-b5ee-40ad-849a-4056c2cf978a",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JWu4sdwkgHevLvVRqS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b7907c9-8332-454e-967b-850c74b09fff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vv5hd38GNH4pfr9XkF4teg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34626,
      "cache_read_input_tokens": 31287,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34626
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 31287,
          "cache_creation_input_tokens": 34626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34626,
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

_source line 44 · 2026-05-14T23:08:34.192Z_

<details><summary>↩ Tool result · `toolu_015Emjoqd6Xi9bY3zhQ5n8k1`</summary>

```text
1	narrative_guidance: 'Depth discriminability holds within-generator (F1 0.82) but cross-generator
2	  generalization is moderate (LOGO F1 ~0.64), with performance drops concentrated
3	  on out-of-family holdouts. Dual dynamics is real but reference-model-modulated:
4	  entropy_mean drift attenuates to |ρ|~0.4 with non-Pythia references, requiring the
5	  paper to present the H1/H2 split as ''reference-model-modulated dual dynamics''
6	  rather than a universal law. Length confound is partial — surface feature F1 drops
7	  ~0.05 after length control, but residual signal confirms depth is not reducible
8	  to length. 7B+ signal weakens (F1 ~0.57) but persists, motivating future work on
9	  scale-robust features. Downstream filtering offers complementary signal but CIs
10	  overlap with best binary baseline on some metrics. Paper reframed: ''depth estimation
11	  is feasible and useful, with initial evidence for dual dynamics'' rather than ''dual
12	  dynamics as general principle.'' Still viable for AAAI/EMNLP as empirical contribution
13	  with honest limitations.
14	
15	  '
16	imagined_experiments:
17	- name: feature_ablation_and_trend
18	  plan_id: plan_001
19	  description: 'Feature ablation (full / surface-only / reference-only) + H1/H2 trend
20	    analysis on MVP data (Pythia-2.8B generator, Pythia-410M reference). Perplexity
21	    pre-validation for Claim 3.
22	
23	    '
24	  expected_results:
25	    full_macro_f1: 0.82
26	    surface_only_f1: 0.76
27	    reference_only_f1: 0.72
28	    full_vs_surface_gap: 0.06
29	    full_vs_reference_gap: 0.1
30	    bootstrap_ci_full: '[0.804, 0.836]'
31	    bootstrap_ci_surface: '[0.747, 0.774]'
32	    bootstrap_ci_reference: '[0.706, 0.733]'
33	    h2_entropy_mean_slope: -0.148
34	    h2_entropy_mean_r2: 0.93
35	    h2_ttr_slope: -0.071
36	    h2_ttr_r2: 0.87
37	    h2_hapax_ratio_slope: -0.054
38	    h2_hapax_ratio_r2: 0.81
39	    h1_entropy_std_slope: 0.003
40	    h1_entropy_std_r2: 0.02
41	    h1_entropy_max_slope: -0.009
42	    h1_entropy_max_r2: 0.04
43	    h1_tail_decay_slope: 0.005
44	    h1_tail_decay_r2: 0.03
45	    h1_entropy_min_slope: -0.012
46	    h1_entropy_min_r2: 0.06
47	    median_ppl_by_depth:
48	    - 13.5
49	    - 4.96
50	    - 3.0
51	    - 2.07
52	    - 1.72
53	    ppl_kruskal_wallis_p: <0.001
54	  result_rationale: 'Within-generator results remain strong because Pythia-410M reference
55	    model is architecturally aligned with the Pythia-2.8B generator, maximizing NLL
56	    feature sensitivity. The 0.06 full-surface gap confirms reference features add
57	    independent value — entropy_mean captures distributional compression that surface
58	    statistics miss. H2 features (entropy_mean, TTR, hapax_ratio) drift because recursive
59	    generation compounds vocabulary impoverishment and entropy compression — each
60	    step feeds an increasingly constrained output distribution back as input. H1 features
61	    (shape statistics like entropy_std, tail_decay) remain stable because distributional
62	    shape is determined by the generator''s softmax geometry, not the input content
63	    — recursive generation shifts the location (mean) of the NLL distribution but
64	    not its spread or tail behavior. Perplexity shows steep monotonic decline because
65	    deeper generations become more predictable to the reference model as they converge
66	    toward the generator''s mode.
67	
68	    '
69	  tables:
70	  - name: 'Table 1: Feature Ablation (5-fold CV, Pythia-2.8B, N=4609)'
71	    columns:
72	    - feature_set
73	    - macro_f1
74	    - 95% CI
75	    - gen0_f1
76	    - gen1_f1
77	    - gen2plus_f1
78	    rows:
79	    - - Full (7 features)
80	      - 0.82
81	      - '[0.804, 0.836]'
82	      - 0.94
83	      - 0.77
84	      - 0.79
85	    - - Surface only (TTR + hapax)
86	      - 0.76
87	      - '[0.747, 0.774]'
88	      - 0.91
89	      - 0.7
90	      - 0.72
91	    - - Reference only (5 NLL)
92	      - 0.72
93	      - '[0.706, 0.733]'
94	      - 0.88
95	      - 0.65
96	      - 0.67
97	    - - Chance baseline
98	      - 0.33
99	      - —
100	      - 0.33
101	      - 0.33
102	      - 0.33
103	  - name: 'Table 2: H1/H2 Trend Regression per Feature'
104	    columns:
105	    - feature
106	    - slope
107	    - R²
108	    - p_value
109	    - classification
110	    rows:
111	    - - entropy_mean
112	      - -0.148
113	      - 0.93
114	      - <0.001
115	      - H2 (drift)
116	    - - TTR
117	      - -0.071
118	      - 0.87
119	      - <0.001
120	      - H2 (drift)
121	    - - hapax_ratio
122	      - -0.054
123	      - 0.81
124	      - <0.001
125	      - H2 (drift)
126	    - - entropy_std
127	      - 0.003
128	      - 0.02
129	      - 0.41
130	      - H1 (stationary)
131	    - - entropy_max
132	      - -0.009
133	      - 0.04
134	      - 0.28
135	      - H1 (stationary)
136	    - - tail_decay
137	      - 0.005
138	      - 0.03
139	      - 0.33
140	      - H1 (stationary)
141	    - - entropy_min
142	      - -0.012
143	      - 0.06
144	      - 0.19
145	      - H1 (stationary)
146	  figures_description:
147	  - 'Fig 1: 7-panel feature trend plot (mean ± std) across depths 0-4. H2 features
148	    show clear monotonic decline; H1 features show flat profiles with overlapping
149	    error bands. Visual separation between H1 and H2 behavior is stark.'
150	  - 'Fig 2: Perplexity distribution boxplots by depth (0-4). Dramatic compression
151	    from depth 0 (median 13.5) to depth 4 (median 1.72), confirming depth-correlated
152	    distributional shift.'
153	  analysis: 'Results confirm the H1/H2 split on MVP data. The 0.06 full-vs-surface
154	    gap is statistically significant (bootstrap CIs non-overlapping), establishing
155	    that reference features capture complementary signal. However, this is within-generator
156	    with same-family reference model — the gap''s robustness must be tested cross-generator
157	    (plan_002) and cross-reference (plan_003). The steep perplexity gradient validates
158	    Claim 3''s premise: depth correlates with distributional properties detectable
159	    by a reference model.
160	
161	    '
162	- name: cross_generator_evaluation
163	  plan_id: plan_002
164	  description: '5-generator LOGO evaluation: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B,
165	    Qwen3-0.6B. 1000 seeds per generator × 5 depths. Leave-one-generator-out and leave-one-family-out
166	    CV.
167	
168	    '
169	  expected_results:
170	    logo_mean_macro_f1: 0.64
171	    logo_holdout_pythia28b_f1: 0.71
172	    logo_holdout_pythia1b_f1: 0.72
173	    logo_holdout_olmo2_f1: 0.6
174	    logo_holdout_qwen17b_f1: 0.62
175	    logo_holdout_qwen06b_f1: 0.59
176	    lofo_holdout_pythia_family_f1: 0.58
177	    lofo_holdout_olmo_family_f1: 0.61
178	    lofo_holdout_qwen_family_f1: 0.59
179	    lofo_mean_f1: 0.593
180	    within_generator_pooled_5fold_f1: 0.78
181	    logo_full_feature_f1: 0.64
182	    logo_surface_only_f1: 0.61
183	    logo_reference_only_f1: 0.58
184	    logo_full_vs_surface_gap: 0.03
185	    logo_full_vs_reference_gap: 0.06
186	    total_chains_generated: 23847
187	    total_chains_after_attrition: 21503
188	  result_rationale: 'Cross-generator F1 drops from 0.82 (within-generator) to 0.64
189	    (LOGO) because each generator family imprints family-specific distributional signatures
190	    beyond the depth signal. Pythia holdouts score higher (0.71-0.72) because Pythia-1B
191	    and Pythia-2.8B share architectural biases (tokenizer, attention patterns, pretraining
192	    data overlap) — when one is held out, the other provides a close proxy in the
193	    training set. OLMo and Qwen holdouts score lower (0.59-0.62) because they represent
194	    genuinely out-of-distribution generator families with different tokenizers and
195	    pretraining distributions. The full-vs-surface gap narrows from 0.06 to 0.03 because
196	    reference features (computed with Pythia-410M) are partially Pythia-biased: they
197	    extract richer signal from Pythia-generated text than from OLMo/Qwen-generated
198	    text, eroding their cross-family advantage. Leave-one-family-out results (mean
199	    0.593) are lower than LOGO (0.64) because LOGO benefits from same-family generators
200	    remaining in training. The within-generator pooled F1 (0.78) is lower than MVP''s
201	    0.82 because pooling heterogeneous generators introduces inter-generator variance
202	    that the classifier must absorb.
203	
204	    '
205	  tables:
206	  - name: 'Table 3: Leave-One-Generator-Out Results (Full Features)'
207	    columns:
208	    - held_out_generator
209	    - family
210	    - macro_f1
211	    - gen0_f1
212	    - gen1_f1
213	    - gen2plus_f1
214	    rows:
215	    - - Pythia-2.8B
216	      - Pythia
217	      - 0.71
218	      - 0.87
219	      - 0.64
220	      - 0.66
221	    - - Pythia-1B
222	      - Pythia
223	      - 0.72
224	      - 0.88
225	      - 0.66
226	      - 0.67
227	    - - OLMo-2-1B
228	      - OLMo
229	      - 0.6
230	      - 0.79
231	      - 0.51
232	      - 0.53
233	    - - Qwen3-1.7B
234	      - Qwen
235	      - 0.62
236	      - 0.82
237	      - 0.53
238	      - 0.55
239	    - - Qwen3-0.6B
240	      - Qwen
241	      - 0.59
242	      - 0.78
243	      - 0.5
244	      - 0.51
245	    - - Mean LOGO
246	      - —
247	      - 0.64
248	      - 0.83
249	      - 0.57
250	      - 0.58
251	  - name: 'Table 4: Leave-One-Family-Out Results'
252	    columns:
253	    - held_out_family
254	    - generators_in_family
255	    - macro_f1
256	    - 95% CI
257	    rows:
258	    - - Pythia
259	      - 2.8B + 1B
260	      - 0.58
261	      - '[0.55, 0.61]'
262	    - - OLMo
263	      - OLMo-2-1B
264	      - 0.61
265	      - '[0.57, 0.64]'
266	    - - Qwen
267	      - 1.7B + 0.6B
268	      - 0.59
269	      - '[0.56, 0.62]'
270	  - name: 'Table 5: Feature Ablation in Cross-Generator Setting (LOGO)'
271	    columns:
272	    - feature_set
273	    - logo_macro_f1
274	    - gap_vs_full
275	    rows:
276	    - - Full
277	      - 0.64
278	      - —
279	    - - Surface only
280	      - 0.61
281	      - -0.03
282	    - - Reference only
283	      - 0.58
284	      - -0.06
285	  figures_description:
286	  - 'Fig 3: LOGO F1 heatmap — rows are held-out generators, columns are depth classes
287	    (gen-0/1/2+). Clear diagonal pattern: within-family holdouts (Pythia-2.8B, Pythia-1B)
288	    are warmer; cross-family (OLMo, Qwen) are cooler, especially for gen-1 and gen-2+.'
289	  - 'Fig 4: Confusion matrices for best (Pythia-1B holdout, F1=0.72) and worst (Qwen-0.6B
290	    holdout, F1=0.59) LOGO folds. Worst case shows gen-1/gen-2+ confusion concentrated
291	    in cross-family.'
292	  analysis: 'LOGO F1=0.64 is within the median range [0.58, 0.70] and confirms moderate
293	    cross-generator generalization. The within-family vs cross-family gap (~0.12)
294	    reveals that distributional features partially encode generator identity, not
295	    just depth. This constrains Claim 1 to ''depth discriminability generalizes within
296	    model family; cross-family generalization is moderate and requires further work.''
297	    The narrowing full-vs-surface gap (0.03 vs 0.06 within-generator) suggests reference
298	    features lose their relative advantage in the cross-generator setting — likely
299	    because the Pythia-410M reference model is better calibrated for Pythia-family
300	    generators. This motivates plan_003 to test non-Pythia reference models.
301	
302	    '
303	- name: cross_family_reference_model
304	  plan_id: plan_003
305	  description: 'Recompute NLL features using non-Pythia reference models (OLMo-2-1B,
306	    Qwen3-0.6B) on existing plan_002 data. Test whether entropy_mean H2 drift and
307	    shape feature H1 stationarity persist. Key falsification test for Claim 2.
308	
309	    '
310	  expected_results:
311	    pythia410m_ref_entropy_mean_rho: -0.68
312	    olmo2_ref_entropy_mean_rho: -0.42
313	    qwen06b_ref_entropy_mean_rho: -0.36
314	    pythia410m_ref_full_f1: 0.82
315	    olmo2_ref_full_f1: 0.78
316	    qwen06b_ref_full_f1: 0.76
317	    olmo2_ref_shape_max_abs_rho: 0.11
318	    qwen06b_ref_shape_max_abs_rho: 0.09
319	    pythia410m_ref_shape_max_abs_rho: 0.08
320	    olmo2_ref_entropy_std_rho: 0.06
321	    olmo2_ref_tail_decay_rho: -0.11
322	    qwen06b_ref_entropy_std_rho: -0.04
323	    qwen06b_ref_tail_decay_rho: 0.09
324	    cross_ref_logo_f1_olmo_ref: 0.61
325	    cross_ref_logo_f1_qwen_ref: 0.58
326	  result_rationale: 'Entropy_mean drift attenuates (|ρ| drops from 0.68 to 0.36-0.42)
327	    because the drift magnitude depends on how well the reference model''s learned
328	    distribution aligns with the generator''s mode. Pythia-410M shares architecture
329	    and pretraining data with Pythia-2.8B, amplifying NLL sensitivity to the generator''s
330	    recursive drift. Non-Pythia references (OLMo, Qwen) have different internal distributions,
331	    so the NLL mean shifts less per depth step — the drift still exists (recursive
332	    generation objectively compresses the output distribution regardless of who measures
333	    it) but the reference model''s measurement sensitivity is lower. Shape features
334	    remain H1 (|ρ|<0.12) across all references because distributional shape (variance,
335	    tail behavior) is a property of the generator''s softmax output geometry, which
336	    doesn''t change with the reference model — different reference models shift the
337	    NLL baseline but preserve relative shape statistics. Classification F1 drops moderately
338	    because attenuated entropy_mean signal provides less discriminative power for
339	    the ordinal depth task.
340	
341	    '
342	  tables:
343	  - name: 'Table 6: Entropy_mean Drift (ρ) by Reference Model'
344	    columns:
345	    - reference_model
346	    - entropy_mean_rho
347	    - p-value
348	    - classification_full_f1
349	    rows:
350	    - - Pythia-410M
351	      - -0.68
352	      - <0.001
353	      - 0.82
354	    - - OLMo-2-1B
355	      - -0.42
356	      - <0.001
357	      - 0.78
358	    - - Qwen3-0.6B
359	      - -0.36
360	      - <0.001
361	      - 0.76
362	  - name: 'Table 7: Shape Feature Stationarity Across References (max |ρ|)'
363	    columns:
364	    - reference_model
365	    - entropy_std_rho
366	    - entropy_max_rho
367	    - tail_decay_rho
368	    - max_abs_rho
369	    rows:
370	    - - Pythia-410M
371	      - 0.03
372	      - -0.05
373	      - 0.04
374	      - 0.08
375	    - - OLMo-2-1B
376	      - 0.06
377	      - -0.08
378	      - -0.11
379	      - 0.11
380	    - - Qwen3-0.6B
381	      - -0.04
382	      - 0.07
383	      - 0.09
384	      - 0.09
385	  figures_description:
386	  - 'Fig 5: Entropy_mean trend lines (depth 0-4) for three reference models. Pythia-410M
387	    shows steepest decline; OLMo-2-1B intermediate; Qwen3-0.6B shallowest. All three
388	    monotonically decreasing but with different slopes.'
389	  - 'Fig 6: Shape feature (entropy_std, tail_decay) trend lines across reference models
390	    — three nearly flat lines per feature, confirming H1 robustness is reference-model-invariant.'
391	  analysis: 'Dual dynamics survives but is reference-model-modulated. The level/shape
392	    split is real across all references (H2 features always drift, H1 features always
393	    stable), but drift magnitude varies 2x depending on reference model choice. This
394	    softens Claim 2 from ''dual dynamics as universal law'' to ''reference-model-modulated
395	    dual dynamics'' — the split is intrinsic to what the feature measures (central
396	    tendency vs shape), but the signal strength depends on reference-generator alignment.
397	    Paper must present this honestly and discuss implications for practical deployment
398	    (reference model selection matters). The cross-reference LOGO F1 (0.58-0.61) shows
399	    that non-Pythia references still support depth estimation, just with reduced accuracy.
400	
401	    '
402	- name: downstream_utility
403	  plan_id: plan_004
404	  description: 'Fine-tune OLMo-1B on depth-stratified data. 3 seeds with bootstrap
405	    CIs. Compare depth-aware filtering (keep gen-0 + gen-1) vs binary baselines (FastDetectGPT,
406	    LD-Score threshold). Sample-count-matched comparison to control for data size
407	    confound.
408	
409	    '
410	  expected_results:
411	    seeds_run: 3
412	    depth_quality_spearman_rho: 0.53
413	    depth_quality_spearman_ci: '[0.41, 0.64]'
414	    ppl_gen0_only: 18.4
415	    ppl_gen0_plus_gen1: 19.1
416	    ppl_gen0_plus_gen1_plus_gen2plus: 21.7
417	    ppl_unfiltered: 22.3
418	    depth_filtering_ppl_improvement_pct: 5.2
419	    depth_filtering_ppl_improvement_ci: '[3.8, 7.1]'
420	    binary_fastdetectgpt_ppl_improvement_pct: 3.8
421	    binary_fastdetectgpt_ppl_improvement_ci: '[2.1, 5.9]'
422	    binary_ldscore_ppl_improvement_pct: 3.2
423	    binary_ldscore_ppl_improvement_ci: '[1.6, 5.3]'
424	    sample_matched_depth_improvement_pct: 2.8
425	    sample_matched_binary_improvement_pct: 1.9
426	    ci_overlap_with_best_binary: true
427	    downstream_task_accuracy_depth: 0.724
428	    downstream_task_accuracy_binary: 0.711
429	    downstream_task_accuracy_unfiltered: 0.698
430	  result_rationale: 'Depth-quality correlation (ρ=0.53) is moderate because OLMo-1B
431	    is somewhat robust to moderate contamination — gen-1 data is only mildly degraded
432	    (perplexity shift from 18.4 to 19.1), so the correlation is driven primarily by
433	    the gen-2+ tail where distributional drift accumulates. Depth-aware filtering
434	    outperforms binary filtering by ~1.4% because it retains gen-1 data that binary
435	    detectors discard — gen-1 text is close to human-quality and contributes positively
436	    to training. However, CI overlap exists because: (1) the advantage is small in
437	    absolute terms, (2) 3 seeds produce wide CIs, and (3) FastDetectGPT''s false negative
438	    rate on gen-1 means it sometimes keeps useful gen-1 data by accident. Sample-matched
439	    comparison (controlling for the data size advantage of depth-aware filtering)
440	    reduces the gap further to 0.9%, confirming that roughly half the advantage comes
441	    from retaining more training data, not from better selection. The effect is real
442	    but modest — insufficient for a strong ''significantly outperforms'' claim.
443	
444	    '
445	  tables:
446	  - name: 'Table 8: Downstream Perplexity by Training Data Composition (OLMo-1B, 3
447	      seeds)'
448	    columns:
449	    - training_data
450	    - n_samples
451	    - mean_ppl
452	    - std_ppl
453	    - 95% CI
454	    rows:
455	    - - gen-0 only
456	      - 4850
457	      - 18.4
458	      - 0.3
459	      - '[17.9, 18.9]'
460	    - - gen-0 + gen-1
461	      - 9700
462	      - 19.1
463	      - 0.4
464	      - '[18.5, 19.7]'
465	    - - gen-0 + gen-1 + gen-2+
466	      - 18200
467	      - 21.7
468	      - 0.6
469	      - '[20.8, 22.6]'
470	    - - Unfiltered (all depths)
471	      - 21500
472	      - 22.3
473	      - 0.5
474	      - '[21.5, 23.1]'
475	  - name: 'Table 9: Filtering Strategy Comparison'
476	    columns:
477	    - strategy
478	    - kept_samples
479	    - ppl_improvement_pct
480	    - 95% CI
481	    - overlap_with_depth
482	    rows:
483	    - - Depth-aware (gen-0+gen-1)
484	      - 9700
485	      - 5.2
486	      - '[3.8, 7.1]'
487	      - —
488	    - - FastDetectGPT binary
489	      - 7300
490	      - 3.8
491	      - '[2.1, 5.9]'
492	      - 'yes'
493	    - - LD-Score binary
494	      - 6900
495	      - 3.2
496	      - '[1.6, 5.3]'
497	      - 'yes'
498	    - - Sample-matched depth
499	      - 7300
500	      - 2.8
501	      - '[1.4, 4.5]'
502	      - —
503	    - - Sample-matched binary
504	      - 7300
505	      - 1.9
506	      - '[0.5, 3.6]'
507	      - —
508	  figures_description:
509	  - 'Fig 7: Perplexity degradation curve as function of training data depth composition
510	    (0-4). Clear upward trend with error bars (3 seeds). gen-0→gen-1 step is small;
511	    gen-1→gen-2+ is the main inflection point.'
512	  - 'Fig 8: Bootstrap CI comparison — depth-aware vs binary filtering perplexity improvement.
513	    Point estimates favor depth-aware, but CI bars overlap for FastDetectGPT.'
514	  analysis: 'Downstream utility exists but the advantage over binary filtering is
515	    modest (1.4% mean, CIs overlap). Claim 3 must be softened to ''depth-aware filtering
516	    offers complementary signal to binary detection'' — the value proposition is not
517	    raw performance but the ability to retain useful gen-1 data while filtering harmful
518	    gen-2+. Sample-matched analysis shows roughly half the gain is from data volume,
519	    not selection quality. Paper should present this honestly and emphasize the interpretability
520	    advantage: depth scores provide a continuous risk metric that binary labels cannot.
521	
522	    '
523	- name: prompt_type_comparison
524	  plan_id: plan_005
525	  description: 'Compare depth signal across three prompt types: continuation, elaboration,
526	    inspired_rewriting. 1000 seeds × Pythia-2.8B × 5 depths × 3 prompt types.
527	
528	    '
529	  expected_results:
530	    continuation_macro_f1: 0.82
531	    elaboration_macro_f1: 0.77
532	    inspired_rewriting_macro_f1: 0.69
533	    continuation_entropy_mean_rho: -0.68
534	    elaboration_entropy_mean_rho: -0.57
535	    inspired_rewriting_entropy_mean_rho: -0.39
536	    continuation_ttr_slope: -0.071
537	    elaboration_ttr_slope: -0.058
538	    inspired_rewriting_ttr_slope: -0.031
539	    h1_features_stable_across_prompts: true
540	  result_rationale: 'Continuation preserves the strongest depth signal because each
541	    step feeds the previous output directly, maximizing distributional drift accumulation.
542	    Elaboration introduces a semantic reframing prompt that partially resets the generator''s
543	    conditioning, attenuating the chain''s compounding effect — the generator still
544	    uses the previous text but the prompt steers it toward a different discourse structure,
545	    reducing the monotonic drift. Inspired rewriting is most disruptive because the
546	    generator is asked to produce content ''inspired by'' rather than continuing from
547	    the previous text — this creates a loose semantic link but breaks the tight distributional
548	    chain, so depth-0 vs depth-2 texts can have similar distributional properties
549	    if the generator happens to produce fluent rewrites. H1 features remain stable
550	    across all prompt types because shape stationarity is a property of the generator''s
551	    output distribution, not the input conditioning.
552	
553	    '
554	  tables:
555	  - name: 'Table 10: Depth Classification by Prompt Type (Pythia-2.8B, 5-fold CV)'
556	    columns:
557	    - prompt_type
558	    - macro_f1
559	    - entropy_mean_rho
560	    - ttr_slope
561	    - semantic_divergence_cosine
562	    rows:
563	    - - Continuation
564	      - 0.82
565	      - -0.68
566	      - -0.071
567	      - 0.85
568	    - - Elaboration
569	      - 0.77
570	      - -0.57
571	      - -0.058
572	      - 0.72
573	    - - Inspired rewriting
574	      - 0.69
575	      - -0.39
576	      - -0.031
577	      - 0.54
578	  figures_description:
579	  - 'Fig 9: Feature drift magnitude by prompt type — bar chart showing H2 feature
580	    slopes for each prompt type. Clear gradient from continuation (steepest) to inspired
581	    rewriting (shallowest).'
582	  analysis: 'Semantic divergence from source anti-correlates with depth signal preservation.
583	    Continuation is the ideal setting for depth estimation; inspired rewriting represents
584	    a harder, more realistic scenario where depth signal partially dissolves. This
585	    informs ecological validity discussions: real-world LLM contamination likely involves
586	    a mix of prompt types, placing practical performance between 0.69-0.82.
587	
588	    '
589	- name: paraphrastic_comparison
590	  plan_id: plan_006
591	  description: 'Parallel paraphrasing chains vs continuation chains for direct comparison.
592	    Tests attractor convergence theory — paraphrastic chains should saturate earlier.
593	
594	    '
595	  expected_results:
596	    paraphrastic_3class_f1: 0.66
597	    nonparaphrastic_3class_f1: 0.82
598	    paraphrastic_gen2plus_f1: 0.41
599	    nonparaphrastic_gen2plus_f1: 0.79
600	    paraphrastic_5class_f1: 0.29
601	    nonparaphrastic_5class_f1: 0.43
602	    paraphrastic_entropy_mean_rho: -0.34
603	    nonparaphrastic_entropy_mean_rho: -0.68
604	    paraphrastic_signal_saturation_depth: 2
605	    nonparaphrastic_signal_saturation_depth: 4
606	  result_rationale: 'Paraphrastic chains converge to attractor cycles (ACL 2025 theory),
607	    bounding depth signal to ~2 distinguishable classes — by depth-2, paraphrased
608	    text has already entered the attractor basin, so gen-2/gen-3/gen-4 become distributionally
609	    indistinguishable. This collapses gen-2+ F1 to near-chance (0.41). Non-paraphrastic
610	    continuation chains escape the attractor because each step generates genuinely
611	    new content rather than cycling through semantically equivalent rewrites. Distributional
612	    drift accumulates monotonically through depth-4, preserving ordinal signal. The
613	    paraphrastic entropy_mean ρ (-0.34) is weaker because the drift saturates early
614	    — depths 2-4 contribute noise, not signal, to the correlation. This directly validates
615	    the paper''s premise: non-paraphrastic chains are the right focus for depth estimation
616	    because the attractor convergence bound does not apply.
617	
618	    '
619	  tables:
620	  - name: 'Table 11: Paraphrastic vs Non-paraphrastic Depth Classification'
621	    columns:
622	    - chain_type
623	    - 3class_f1
624	    - gen0_f1
625	    - gen1_f1
626	    - gen2plus_f1
627	    - signal_saturation_depth
628	    rows:
629	    - - Paraphrastic
630	      - 0.66
631	      - 0.89
632	      - 0.67
633	      - 0.41
634	      - 2
635	    - - Non-paraphrastic
636	      - 0.82
637	      - 0.94
638	      - 0.77
639	      - 0.79
640	      - 4+
641	  figures_description:
642	  - 'Fig 10: Per-depth F1 curves for paraphrastic (flattens at depth 2) vs non-paraphrastic
643	    (gradual decline through depth 4). Clear visual separation demonstrating attractor
644	    saturation vs sustained drift.'
645	  analysis: 'Confirms the theoretical motivation: paraphrastic chains hit the attractor
646	    bound at depth ~2, while non-paraphrastic chains maintain discriminable depth
647	    signal through depth 4. This justifies the paper''s focus on continuation chains
648	    and connects to attractor cycle theory as a boundary condition rather than a general
649	    limit on depth estimation.
650	
651	    '
652	- name: cross_model_chains
653	  plan_id: plan_007
654	  description: 'Cross-model chains (different generator per depth step) vs single-model
655	    chains. Tests ecological validity for real web contamination scenarios.
656	
657	    '
658	  expected_results:
659	    cross_model_logo_f1: 0.56
660	    single_model_logo_f1: 0.64
661	    cross_model_within_f1: 0.68
662	    cross_model_entropy_mean_rho: -0.41
663	    cross_model_ttr_slope: -0.039
664	    cross_model_h1_stable: true
665	    cross_model_gen0_f1: 0.78
666	    cross_model_gen1_f1: 0.46
667	    cross_model_gen2plus_f1: 0.44
668	  result_rationale: 'Cross-model chains inject between-model distributional variance
669	    at each depth step. When generator changes between depths (e.g., Pythia→OLMo→Qwen),
670	    the NLL features measured by the reference model reflect not just depth-related
671	    drift but also generator-switching effects — the reference model''s NLL for OLMo-generated
672	    text differs from Pythia-generated text regardless of depth. This noise source
673	    partially masks the depth signal, particularly for gen-1 vs gen-2+ where the depth
674	    effect is smaller than the generator effect. Gen-0 (human) remains well-separated
675	    (F1 0.78) because all chains share the same human seed distribution. The F1 drop
676	    from 0.64 (single-model LOGO) to 0.56 (cross-model) quantifies the cost of realistic
677	    generator diversity. H1 features remain stable even in cross-model chains, confirming
678	    that shape stationarity is generator-intrinsic.
679	
680	    '
681	  tables:
682	  - name: 'Table 12: Cross-model vs Single-model Chain Classification'
683	    columns:
684	    - chain_type
685	    - logo_f1
686	    - gen0_f1
687	    - gen1_f1
688	    - gen2plus_f1
689	    - entropy_mean_rho
690	    rows:
691	    - - Single-model
692	      - 0.64
693	      - 0.83
694	      - 0.57
695	      - 0.58
696	      - -0.68
697	    - - Cross-model
698	      - 0.56
699	      - 0.78
700	      - 0.46
701	      - 0.44
702	      - -0.41
703	  figures_description:
704	  - 'Fig 11: Confusion matrices for cross-model chains — gen-1/gen-2+ are heavily
705	    confused due to generator-switching noise dominating depth signal.'
706	  analysis: 'Cross-model chains degrade depth estimation significantly (-0.08 F1).
707	    This is a realistic limitation: web contamination involves diverse generators,
708	    and the current feature set partially conflates generator identity with depth.
709	    Paper should present this as an honest ecological validity test — depth estimation
710	    is most reliable for single-source contamination, and cross-model scenarios require
711	    future work on generator-invariant features.
712	
713	    '
714	- name: multi_domain_seeds
715	  plan_id: plan_008
716	  description: 'Expand to 4 domains: Wikipedia, news (CNN/DM), scientific (S2ORC),
717	    creative (WritingPrompts). 500 seeds per domain × 5 depths × 5 generators.
718	
719	    '
720	  expected_results:
721	    wikipedia_logo_f1: 0.67
722	    news_logo_f1: 0.64
723	    scientific_logo_f1: 0.62
724	    creative_logo_f1: 0.57
725	    pooled_multidomain_logo_f1: 0.63
726	    domain_f1_std: 0.037
727	    wikipedia_entropy_mean_rho: -0.72
728	    creative_entropy_mean_rho: -0.48
729	    cross_domain_train_test_f1: 0.58
730	  result_rationale: 'Wikipedia seeds yield highest F1 (0.67) because Wikipedia prose
731	    is stylistically uniform and formulaic — generators produce characteristically
732	    homogeneous continuations that maximize distributional drift consistency across
733	    depths. Creative writing seeds yield lowest F1 (0.57) because creative text has
734	    high intrinsic variance (diverse styles, tones, registers), which creates a larger
735	    noise floor that depth signal must overcome. The generator''s creative outputs
736	    at depth-1 can be as distributionally diverse as human creative text, blurring
737	    the gen-0/gen-1 boundary. Scientific text (0.62) occupies the middle ground: constrained
738	    register but technical vocabulary creates complex distributional patterns. Cross-domain
739	    train-test (train on 3 domains, test on 1) drops to 0.58, suggesting partial domain
740	    adaptation in the classifier.
741	
742	    '
743	  tables:
744	  - name: 'Table 13: Domain-Specific LOGO Results'
745	    columns:
746	    - domain
747	    - logo_f1
748	    - entropy_mean_rho
749	    - ttr_slope
750	    - n_seeds
751	    rows:
752	    - - Wikipedia
753	      - 0.67
754	      - -0.72
755	      - -0.078
756	      - 500
757	    - - News (CNN/DM)
758	      - 0.64
759	      - -0.63
760	      - -0.065
761	      - 500
762	    - - Scientific (S2ORC)
763	      - 0.62
764	      - -0.58
765	      - -0.059
766	      - 500
767	    - - Creative (WritingPrompts)
768	      - 0.57
769	      - -0.48
770	      - -0.041
771	      - 500
772	    - - Pooled
773	      - 0.63
774	      - -0.6
775	      - -0.061
776	      - 2000
777	  figures_description:
778	  - 'Fig 12: Domain-specific entropy_mean drift plots — four panels showing depth
779	    0-4 trends. Wikipedia shows tightest confidence bands; creative shows widest.'
780	  analysis: 'Domain variation (std 0.037) is non-trivial but depth signal generalizes
781	    across all four domains. Creative writing is the hardest domain, consistent with
782	    high intrinsic variance. Paper should report pooled results as primary and domain-specific
783	    as supplementary analysis, noting that domain adaptation (train/test domain mismatch)
784	    is an additional challenge beyond generator generalization.
785	
786	    '
787	- name: finer_grained_ordinal
788	  plan_id: plan_009
789	  description: '5-class ordinal classification (gen-0 through gen-4) on non-paraphrastic
790	    chains. Tests whether depth signal supports finer than 3-class resolution.
791	
792	    '
793	  expected_results:
794	    five_class_macro_f1: 0.43
795	    five_class_gen0_f1: 0.73
796	    five_class_gen1_f1: 0.52
797	    five_class_gen2_f1: 0.35
798	    five_class_gen3_f1: 0.29
799	    five_class_gen4_f1: 0.28
800	    ordinal_mae: 0.72
801	    three_class_macro_f1_same_data: 0.64
802	    adjacent_confusion_rate: 0.61
803	    spearman_pred_vs_true: 0.74
804	  result_rationale: '5-class F1 (0.43) drops substantially from 3-class (0.64) because
805	    distributional differences between adjacent depths (gen-2 vs gen-3, gen-3 vs gen-4)
806	    are small — the drift per step is roughly constant, but the cumulative difference
807	    between gen-0 and gen-4 is spread across 4 boundaries, each of which is harder
808	    than the 3-class boundaries. Gen-0 is still well-separated (0.73) because human
809	    vs any synthetic is the largest distributional gap. Gen-1 (0.52) is intermediate
810	    — distinguishable from gen-0 and gen-2+ but with confusion on both sides. Gen-2/3/4
811	    collapse into a muddy cluster (F1 0.28-0.35) because by depth-2, recursive drift
812	    has already consumed most of the easy-to-detect signal, and remaining differences
813	    are within the noise floor. However, ordinal Spearman (0.74) is respectable, showing
814	    the classifier preserves rank order even when exact class assignment fails — errors
815	    are predominantly between adjacent classes (61% of errors), not distant ones.
816	
817	    '
818	  tables:
819	  - name: 'Table 14: 5-class Ordinal Classification (LOGO, Full Features)'
820	    columns:
821	    - class
822	    - f1
823	    - precision
824	    - recall
825	    - most_confused_with
826	    rows:
827	    - - gen-0
828	      - 0.73
829	      - 0.78
830	      - 0.69
831	      - gen-1
832	    - - gen-1
833	      - 0.52
834	      - 0.49
835	      - 0.55
836	      - gen-0 / gen-2
837	    - - gen-2
838	      - 0.35
839	      - 0.33
840	      - 0.37
841	      - gen-3
842	    - - gen-3
843	      - 0.29
844	      - 0.31
845	      - 0.27
846	      - gen-2 / gen-4
847	    - - gen-4
848	      - 0.28
849	      - 0.26
850	      - 0.3
851	      - gen-3
852	  figures_description:
853	  - 'Fig 13: 5×5 confusion matrix heatmap — strong diagonal for gen-0, increasingly
854	    diffuse for deeper classes. Off-diagonal mass concentrated on ±1 adjacent cells.'
855	  - 'Fig 14: Predicted vs true depth scatter with ordinal regression line (Spearman
856	    ρ=0.74).'
857	  analysis: 'Finer-grained classification is feasible but noisy beyond 3 classes.
858	    The 3-class grouping (gen-0/gen-1/gen-2+) appears to be the natural resolution
859	    supported by the current feature set. Paper presents 5-class as secondary analysis
860	    motivating ordinal regression approaches in future work. The high ordinal Spearman
861	    (0.74) suggests the classifier captures depth ordering even when exact classification
862	    fails, which is useful for risk scoring applications.
863	
864	    '
865	- name: human_edit_robustness
866	  plan_id: plan_010
867	  description: 'Robustness to simulated human edits: (A) random word replacement at
868	    5%/10%/20%, (B) LLM-simulated light rephrasing. Tests whether post-processing
869	    destroys depth signal.
870	
871	    '
872	  expected_results:
873	    baseline_no_edit_f1: 0.82
874	    random_5pct_f1: 0.79
875	    random_10pct_f1: 0.72
876	    random_20pct_f1: 0.6
877	    llm_light_edit_f1: 0.73
878	    random_5pct_entropy_mean_rho: -0.63
879	    random_10pct_entropy_mean_rho: -0.52
880	    random_20pct_entropy_mean_rho: -0.35
881	    llm_light_edit_entropy_mean_rho: -0.49
882	    h1_features_robust_to_edit: true
883	    shape_features_max_rho_change: 0.07
884	  result_rationale: 'Random word replacement progressively corrupts the text''s distributional
885	    profile. At 5%, the corruption is below the feature noise floor — surface features
886	    (TTR, hapax) are slightly perturbed but NLL features remain stable because 5%
887	    random words don''t substantially alter the reference model''s token-level surprise
888	    distribution. At 20%, the text becomes distributionally anomalous in a way that
889	    overwhelms the depth signal — randomly inserted words create a uniform noise pattern
890	    that masks depth-specific distributional drift. LLM-simulated editing (F1 0.73)
891	    falls between 5% and 10% random replacement because LLM edits are more natural
892	    (preserving grammaticality) but more targeted (selectively replacing awkward or
893	    repetitive phrases that carry depth signal). Shape features remain robust (max
894	    ρ change 0.07) because random/LLM edits affect vocabulary composition (level)
895	    more than distributional shape.
896	
897	    '
898	  tables:
899	  - name: 'Table 15: Robustness to Simulated Human Edits'
900	    columns:
901	    - edit_type
902	    - edit_rate
903	    - macro_f1
904	    - delta_f1
905	    - entropy_mean_rho
906	    rows:
907	    - - None (baseline)
908	      - 0%
909	      - 0.82
910	      - —
911	      - -0.68
912	    - - Random word
913	      - 5%
914	      - 0.79
915	      - -0.03
916	      - -0.63
917	    - - Random word
918	      - 10%
919	      - 0.72
920	      - -0.1
921	      - -0.52
922	    - - Random word
923	      - 20%
924	      - 0.6
925	      - -0.22
926	      - -0.35
927	    - - LLM light rephrase
928	      - ~8%
929	      - 0.73
930	      - -0.09
931	      - -0.49
932	  figures_description:
933	  - 'Fig 15: F1 degradation curve as function of edit rate — roughly linear decline
934	    with inflection around 15%. LLM editing point plotted at estimated ~8% token change
935	    rate.'
936	  analysis: 'Depth signal is moderately robust to light editing (5%) but degrades
937	    meaningfully at 10%+. Real-world human editing likely falls in the 5-15% range,
938	    placing expected performance at F1 0.72-0.79. Paper presents this as honest robustness
939	    analysis — depth estimation is viable for lightly edited synthetic text but fragile
940	    under heavy post-processing. This limits practical applicability to scenarios
941	    where contamination involves minimally edited LLM outputs.
942	
943	    '
944	- name: ld_score_feature
945	  plan_id: plan_011
946	  description: 'Add LD-Score as feature. Test pre-registered prediction that LD-Score
947	    is a level feature (H2 drift). Evaluate marginal classification improvement.
948	
949	    '
950	  expected_results:
951	    ld_score_depth_rho: -0.55
952	    ld_score_slope: -0.042
953	    ld_score_r2: 0.72
954	    ld_score_classification: H2_level
955	    preregistered_prediction_confirmed: true
956	    f1_with_ld_score: 0.83
957	    f1_without_ld_score: 0.82
958	    marginal_improvement: 0.01
959	    ld_score_correlation_with_ttr: 0.68
960	    ld_score_correlation_with_hapax: 0.61
961	  result_rationale: 'LD-Score measures character-level distributional properties,
962	    which are downstream of vocabulary composition — as depth increases and vocabulary
963	    impoverishes (fewer unique words, more repetitive character n-grams), LD-Score
964	    shifts accordingly. This confirms it is a level feature (H2), sensitive to the
965	    same vocabulary/diversity drift as TTR and hapax_ratio. The pre-registered prediction
966	    is validated (ρ=-0.55, clearly H2), strengthening the level/shape framework''s
967	    predictive power. However, the high correlation with existing surface features
968	    (0.61-0.68 with TTR/hapax) means LD-Score provides little incremental information
969	    — the marginal F1 gain is only 0.01. The character-level signal is largely redundant
970	    with word-level diversity features already in the feature set.
971	
972	    '
973	  tables:
974	  - name: 'Table 16: LD-Score Feature Analysis'
975	    columns:
976	    - metric
977	    - value
978	    rows:
979	    - - LD-Score depth ρ
980	      - -0.55
981	    - - LD-Score linear slope
982	      - -0.042
983	    - - LD-Score R²
984	      - 0.72
985	    - - H1/H2 classification
986	      - H2 (level)
987	    - - Pre-registered prediction
988	      - Confirmed
989	    - - Correlation with TTR
990	      - 0.68
991	    - - Correlation with hapax_ratio
992	      - 0.61
993	    - - F1 with LD-Score
994	      - 0.83
995	    - - F1 without LD-Score
996	      - 0.82
997	  figures_description:
998	  - 'Fig 16: LD-Score depth trend (mean ± std, depths 0-4) overlaid with TTR trend
999	    — similar decline pattern, confirming shared level/diversity dynamics at character
1000	    level.'
1001	  analysis: 'Pre-registered prediction confirmed: LD-Score is a level feature. This
1002	    is a minor but clean validation of the H1/H2 framework''s predictive utility.
1003	    However, the marginal classification improvement is negligible (0.01), so LD-Score
1004	    is presented as a validation data point rather than a feature engineering contribution.
1005	    The high correlation with existing features suggests character-level and word-level
1006	    diversity measures capture the same underlying depth signal.
1007	
1008	    '
1009	- name: end_to_end_classifier
1010	  plan_id: plan_012
1011	  description: 'QLoRA fine-tuned Qwen3-0.6B for end-to-end depth classification. Compares
1012	    learned representations vs handcrafted distributional features.
1013	
1014	    '
1015	  expected_results:
1016	    qlora_macro_f1: 0.79
1017	    qlora_gen0_f1: 0.92
1018	    qlora_gen1_f1: 0.73
1019	    qlora_gen2plus_f1: 0.72
1020	    handcrafted_macro_f1: 0.82
1021	    qlora_cross_gen_logo_f1: 0.61
1022	    handcrafted_cross_gen_logo_f1: 0.64
1023	    qlora_training_time_hours: 6.2
1024	    qlora_inference_tokens_per_sec: 145
1025	    handcrafted_inference_tokens_per_sec: 8900
1026	  result_rationale: 'QLoRA achieves slightly lower F1 (0.79 vs 0.82) because the depth
1027	    classification task has limited training data (~25K samples) — insufficient for
1028	    a 600M-parameter model to learn robust depth-specific representations from scratch.
1029	    The model likely overfits to generator- specific patterns rather than learning
1030	    the distributional drift abstraction that handcrafted features explicitly encode.
1031	    Cross-generator LOGO (0.61 vs 0.64) shows the end-to-end approach generalizes
1032	    slightly worse, further suggesting it memorizes generator identities. The handcrafted
1033	    approach also has a massive inference speed advantage (~60x) because it requires
1034	    only a forward pass through the small reference model + simple statistics, vs
1035	    full sequence processing through a 600M model. This confirms the paper''s positioning:
1036	    the contribution is the problem formulation and empirical findings, not a competition
1037	    for SOTA — simple features suffice for the task.
1038	
1039	    '
1040	  tables:
1041	  - name: 'Table 17: End-to-End vs Handcrafted Features'
1042	    columns:
1043	    - method
1044	    - within_gen_f1
1045	    - logo_f1
1046	    - inference_speed
1047	    - training_cost
1048	    rows:
1049	    - - Handcrafted (XGBoost)
1050	      - 0.82
1051	      - 0.64
1052	      - 8900 tok/s
1053	      - ~0 GPU-h
1054	    - - QLoRA (Qwen3-0.6B)
1055	      - 0.79
1056	      - 0.61
1057	      - 145 tok/s
1058	      - 6.2 GPU-h
1059	  figures_description:
1060	  - 'Fig 17: F1 comparison bar chart (within-gen and LOGO) for handcrafted vs QLoRA.
1061	    Handcrafted is slightly better on both metrics while being 60x faster at inference.'
1062	  analysis: 'End-to-end approach does not outperform handcrafted features, confirming
1063	    that the task''s information content is well-captured by simple distributional
1064	    statistics. This validates the paper''s contribution positioning: novelty lies
1065	    in the problem formulation and empirical findings, not in model architecture.
1066	    The interpretability and efficiency advantages of handcrafted features are a practical
1067	    benefit for deployment in data curation pipelines.
1068	
1069	    '
1070	- name: text_length_control
1071	  plan_id: plan_013
1072	  description: 'Length confound analysis: (A) length distributions by depth, (B) length-normalized
1073	    features, (C) length-matched classification. Critical confound control.
1074	
1075	    '
1076	  expected_results:
1077	    mean_length_gen0: 315
1078	    mean_length_gen1: 289
1079	    mean_length_gen2: 263
1080	    mean_length_gen3: 246
1081	    mean_length_gen4: 237
1082	    length_depth_pearson_r: -0.41
1083	    length_depth_kw_p: <0.001
1084	    original_surface_f1: 0.76
1085	    length_controlled_surface_f1: 0.71
1086	    length_controlled_surface_f1_delta: -0.05
1087	    original_reference_f1: 0.72
1088	    length_controlled_reference_f1: 0.7
1089	    length_controlled_reference_f1_delta: -0.02
1090	    original_full_f1: 0.82
1091	    length_controlled_full_f1: 0.78
1092	    length_controlled_full_f1_delta: -0.04
1093	    length_matched_subsample_full_f1: 0.79
1094	    fixed_window_ttr_slope: -0.048
1095	    fixed_window_ttr_original_slope: -0.071
1096	    fixed_window_hapax_slope: -0.037
1097	    fixed_window_hapax_original_slope: -0.054
1098	    residual_signal_confirmed: true
1099	  result_rationale: 'Text length decreases monotonically with depth (315→237 tokens)
1100	    because recursive generation tends to produce slightly shorter texts — generators
1101	    are biased toward completing thoughts within a typical output length, and each
1102	    depth step compounds this tendency. This creates a legitimate confound: TTR and
1103	    hapax_ratio are mechanically length-dependent (shorter texts have higher TTR/hapax
1104	    by construction). The -0.05 surface F1 drop after length control confirms that
1105	    ~30% of the surface feature signal was tracking length, not depth. However, the
1106	    residual signal (F1 0.71 after control, well above chance at 0.33) confirms that
1107	    depth drives genuine vocabulary impoverishment beyond what length explains. Reference
1108	    features lose less (-0.02) because NLL statistics are computed token-by-token
1109	    and are less length-sensitive — the per-token surprise distribution shifts with
1110	    depth regardless of total text length. The full-feature length-controlled F1 (0.78)
1111	    remains substantially above chance and above either feature subset, confirming
1112	    the core claims survive length control.
1113	
1114	    '
1115	  tables:
1116	  - name: 'Table 18: Text Length by Depth'
1117	    columns:
1118	    - depth
1119	    - mean_tokens
1120	    - std_tokens
1121	    - median_tokens
1122	    rows:
1123	    - - gen-0
1124	      - 315
1125	      - 82
1126	      - 298
1127	    - - gen-1
1128	      - 289
1129	      - 76
1130	      - 274
1131	    - - gen-2
1132	      - 263
1133	      - 71
1134	      - 251
1135	    - - gen-3
1136	      - 246
1137	      - 68
1138	      - 237
1139	    - - gen-4
1140	      - 237
1141	      - 65
1142	      - 228
1143	  - name: 'Table 19: Length-Controlled Classification Results'
1144	    columns:
1145	    - feature_set
1146	    - original_f1
1147	    - length_controlled_f1
1148	    - delta
1149	    - delta %
1150	    rows:
1151	    - - Full
1152	      - 0.82
1153	      - 0.78
1154	      - -0.04
1155	      - -4.9%
1156	    - - Surface only
1157	      - 0.76
1158	      - 0.71
1159	      - -0.05
1160	      - -6.6%
1161	    - - Reference only
1162	      - 0.72
1163	      - 0.7
1164	      - -0.02
1165	      - -2.8%
1166	  - name: 'Table 20: Fixed-Window Feature Slopes (128-token windows)'
1167	    columns:
1168	    - feature
1169	    - original_slope
1170	    - fixed_window_slope
1171	    - slope_reduction_pct
1172	    rows:
1173	    - - TTR
1174	      - -0.071
1175	      - -0.048
1176	      - 32%
1177	    - - hapax_ratio
1178	      - -0.054
1179	      - -0.037
1180	      - 31%
1181	    - - entropy_mean
1182	      - -0.148
1183	      - -0.139
1184	      - 6%
1185	  figures_description:
1186	  - 'Fig 18: Text length distribution violin plots by depth — clear leftward shift
1187	    with depth. Overlapping distributions confirm length is a partial, not sole, confound.'
1188	  - 'Fig 19: Feature slopes before/after length control — surface features show ~30%
1189	    reduction; reference features show <10% reduction. Visualizes the differential
1190	    length sensitivity.'
1191	  analysis: 'Length is a real but partial confound. The 0.05 surface F1 drop is within
1192	    the median range [-0.08, -0.03] and must be acknowledged honestly in the paper.
1193	    The key finding is that residual signal survives: depth drives genuine distributional
1194	    drift beyond length artifacts. Reference features are relatively length-robust
1195	    (only 0.02 drop), strengthening their value in the feature set. Paper should add
1196	    length-controlled analysis as a supplementary validation table and note: ''Surface
1197	    features partially track text length, but residual depth signal persists after
1198	    length control. Reference features provide length-robust complementary signal.''
1199	
1200	    '
1201	- name: large_scale_generator
1202	  plan_id: plan_014
1203	  description: 'Add Qwen3-8B-Base as 7B+ generator. 1000 seeds × 5 depths. Tests whether
1204	    depth signal persists at frontier scale.
1205	
1206	    '
1207	  expected_results:
1208	    qwen8b_3class_macro_f1: 0.57
1209	    qwen8b_gen0_f1: 0.76
1210	    qwen8b_gen1_f1: 0.48
1211	    qwen8b_gen2plus_f1: 0.46
1212	    qwen8b_entropy_mean_rho: -0.38
1213	    qwen8b_ttr_slope: -0.042
1214	    qwen8b_hapax_slope: -0.032
1215	    qwen8b_vs_pythia28b_f1_gap: -0.25
1216	    qwen8b_vs_qwen17b_f1_gap: -0.05
1217	    qwen8b_h1_features_stable: true
1218	    qwen8b_entropy_std_rho: 0.05
1219	    qwen8b_tail_decay_rho: -0.07
1220	    qwen8b_5class_f1: 0.31
1221	    logo_with_8b_included: 0.61
1222	  result_rationale: '7B+ generators produce substantially more fluent text that compresses
1223	    the depth signal. At 8B parameters, the model has sufficient capacity to maintain
1224	    diverse vocabulary and natural distributional properties even at depth-4 — vocabulary
1225	    impoverishment is less severe because the model''s larger vocabulary and richer
1226	    internal representations allow it to produce varied continuations even from distributionally
1227	    drifted inputs. The F1 drop from 0.82 (Pythia-2.8B) to 0.57 (Qwen3-8B) is large
1228	    but the signal remains non-trivial (well above chance at 0.33). Entropy_mean ρ
1229	    attenuates from -0.68 to -0.38, consistent with weaker but non-zero drift — the
1230	    8B model''s NLL distribution still shifts with depth but less per step. Gen-0
1231	    remains distinguishable (F1 0.76) because the human-vs-any-synthetic gap is robust
1232	    to model scale, but gen-1 vs gen-2+ becomes very noisy (0.46-0.48). H1 features
1233	    remain stable (shape stationarity is scale-invariant). This is an honest scaling
1234	    result: depth estimation weakens at scale but doesn''t vanish, motivating future
1235	    work on scale-robust features.
1236	
1237	    '
1238	  tables:
1239	  - name: 'Table 21: 7B+ Generator Depth Classification'
1240	    columns:
1241	    - generator
1242	    - params
1243	    - macro_f1
1244	    - entropy_mean_rho
1245	    - ttr_slope
1246	    rows:
1247	    - - Pythia-2.8B
1248	      - 2.8B
1249	      - 0.82
1250	      - -0.68
1251	      - -0.071
1252	    - - Pythia-1B
1253	      - 1B
1254	      - 0.8
1255	      - -0.65
1256	      - -0.068
1257	    - - OLMo-2-1B
1258	      - 1.5B
1259	      - 0.78
1260	      - -0.61
1261	      - -0.063
1262	    - - Qwen3-1.7B
1263	      - 1.7B
1264	      - 0.75
1265	      - -0.56
1266	      - -0.055
1267	    - - Qwen3-0.6B
1268	      - 0.6B
1269	      - 0.77
1270	      - -0.59
1271	      - -0.061
1272	    - - Qwen3-8B
1273	      - 8B
1274	      - 0.57
1275	      - -0.38
1276	      - -0.042
1277	  - name: 'Table 22: Scale Trend Analysis'
1278	    columns:
1279	    - metric
1280	    - ≤2.8B mean
1281	    - 8B
1282	    - delta
1283	    - interpretation
1284	    rows:
1285	    - - macro_f1
1286	      - 0.78
1287	      - 0.57
1288	      - -0.21
1289	      - Signal weakens at scale
1290	    - - entropy_mean ρ
1291	      - -0.62
1292	      - -0.38
1293	      - '+0.24'
1294	      - Drift attenuates at scale
1295	    - - TTR slope
1296	      - -0.064
1297	      - -0.042
1298	      - '+0.022'
1299	      - Less vocab impoverishment
1300	    - - H1 max |ρ|
1301	      - 0.08
1302	      - 0.07
1303	      - '-0.01'
1304	      - Shape stationarity preserved
1305	  figures_description:
1306	  - 'Fig 20: F1 vs generator parameter count (log scale). Clear downward trend from
1307	    0.6B-2.8B cluster to 8B outlier. Dotted line at chance (0.33) for reference.'
1308	  - 'Fig 21: Entropy_mean depth trend for 8B (shallow slope) vs 2.8B (steep slope).
1309	    Both monotonically decreasing but 8B slope is ~55% of 2.8B slope.'
1310	  analysis: '7B+ results confirm the scaling concern. Depth signal is weaker but non-zero
1311	    (F1 0.57, significantly above chance p<0.001). The paper should present this as
1312	    an honest scaling analysis in a dedicated subsection: ''Depth signal attenuates
1313	    with generator scale, consistent with larger models maintaining distributional
1314	    diversity under recursive generation. At 8B parameters, gen-0 vs synthetic remains
1315	    detectable, but fine-grained depth estimation (gen-1 vs gen-2+) approaches noise
1316	    floor. This motivates future work on scale-robust features, potentially leveraging
1317	    model-specific distributional properties.'' The 8B result transforms from a weakness
1318	    into a scientific finding: the relationship between model capacity and depth signal
1319	    decay is itself an interesting empirical contribution.'
1320	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b7907c9-8332-454e-967b-850c74b09fff",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "70e113aa-729e-4e38-9eea-35f600fe3dda",
  "sourceToolAssistantUUID": "6b7907c9-8332-454e-967b-850c74b09fff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-14T23:08:43.426Z_

Now let me also check the analysis report from plan-001-fix for the actual experimental results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70e113aa-729e-4e38-9eea-35f600fe3dda",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JXPNU5zTHQCH4k7iv4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57bb457b-7fba-4af2-9007-468b570bb7bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3mfpwcu4nAetZPYt1rEvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24131,
      "cache_read_input_tokens": 65913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24131,
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

_source line 46 · 2026-05-14T23:08:45.274Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LxY2G9bDHUt9VSQECucZsV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/plan-001-fix/analysis_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57bb457b-7fba-4af2-9007-468b570bb7bf",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JXPNU5zTHQCH4k7iv4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19ef2d10-b029-4424-863b-37b659209e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3mfpwcu4nAetZPYt1rEvT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24131,
      "cache_read_input_tokens": 65913,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 65913,
          "cache_creation_input_tokens": 24131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24131,
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

_source line 47 · 2026-05-14T23:08:45.277Z_

<details><summary>↩ Tool result · `toolu_01LxY2G9bDHUt9VSQECucZsV`</summary>

```text
1	# plan-001-fix: Feature Ablation Analysis Report
2	
3	**Date**: 2026-05-14
4	**Data**: 4609 records, Pythia-410M reference model, Pythia-2.8B generator
5	**Script**: `ablation_analysis.py --parts A B C --device cuda:0`
6	**Server**: autodl-5090
7	
8	---
9	
10	## Part A: Feature Ablation (3-class classification)
11	
12	Balanced 2967 samples (989 per class: gen-0 / gen-1 / gen-2+), 5-fold stratified CV, XGBoost.
13	
14	| Feature Set | Macro-F1 | 95% CI | gen-0 F1 | gen-1 F1 | gen-2+ F1 |
15	|---|---|---|---|---|---|
16	| **full** (all 7 features) | **0.8204 ± 0.0061** | [0.8151, 0.8253] | 0.9354 | 0.7517 | 0.7741 |
17	| surface_only (ttr, hapax_ratio) | 0.7628 ± 0.0165 | [0.7470, 0.7745] | 0.8585 | 0.6794 | 0.7504 |
18	| reference_only (entropy×4, tail_decay) | 0.7187 ± 0.0157 | [0.7059, 0.7327] | 0.7942 | 0.6073 | 0.7546 |
19	
20	**Paired t-tests:**
21	- full vs reference_only: t=11.21, **p=0.0004** → full significantly better (+10.2 pts)
22	- full vs surface_only: t=9.22, **p=0.0008** → full significantly better (+5.8 pts)
23	- reference_only vs surface_only: t=-3.25, **p=0.0313** → surface slightly better (+4.4 pts)
24	
25	**Key findings:**
26	- Both feature subsets independently achieve macro-F1 > 0.71, confirming each carries genuine depth signal.
27	- Combining them yields a significant boost (0.82), with tighter CI (±0.006 vs ±0.016), indicating complementarity and not just redundancy.
28	- gen-1 is the hardest class across all feature sets (first-generation text is hardest to distinguish from human/deeper generations).
29	
30	**MVP comparison:** The ablation's full-feature macro-F1 (0.8204) is slightly lower than the MVP test macro-F1 (0.8408) because the ablation uses strict 1:1:1 balancing and 5-fold CV, while MVP used a 80/20 split with natural class proportions.
31	
32	---
33	
34	## Part B: H1/H2 Trend Analysis (Spearman rank correlation with depth)
35	
36	Full dataset (4609 samples). H1 = near-stationary (|rho| < 0.3); H2 = monotonic drift (|rho| ≥ 0.3).
37	
38	| Feature | rho | p-value | Label | Interpretation |
39	|---|---|---|---|---|
40	| entropy_mean | **-0.6754** | 0.00 | H2 (drift) | Decreases strongly with depth |
41	| entropy_std | -0.1530 | 1.5e-25 | H1 (near-stationary) | Weak, non-monotonic |
42	| entropy_min | -0.4797 | 6.0e-264 | H1 (near-stationary) | Moderate — borderline |
43	| entropy_max | -0.0351 | 0.017 | H1 (near-stationary) | Negligible |
44	| tail_decay | 0.0633 | 1.7e-05 | H1 (near-stationary) | Negligible |
45	| **ttr** | **-0.6333** | 0.00 | **H2 (drift)** | Strong monotonic decrease |
46	| **hapax_ratio** | **-0.6553** | 0.00 | **H2 (drift)** | Strong monotonic decrease |
47	
48	**Effect sizes (Cohen's d between adjacent depths):**
49	
50	| Feature | d(0→1) | d(1→2) | d(2→3) | d(3→4) |
51	|---|---|---|---|---|
52	| entropy_mean | 0.54 | 0.85 | 0.47 | 0.31 |
53	| entropy_std | -0.56 | 0.21 | 0.20 | 0.20 |
54	| ttr | **1.44** | 0.59 | 0.27 | 0.21 |
55	| hapax_ratio | **1.45** | 0.51 | 0.22 | 0.17 |
56	
57	**Per-depth means (monotonicity check):**
58	
59	| Feature | d=0 | d=1 | d=2 | d=3 | d=4 |
60	|---|---|---|---|---|---|
61	| entropy_mean | 2.637 | 2.384 | 1.775 | 1.392 | 1.147 |
62	| ttr | 0.643 | 0.477 | 0.365 | 0.301 | 0.250 |
63	| hapax_ratio | 0.516 | 0.330 | 0.226 | 0.174 | 0.133 |
64	| entropy_std | 1.661 | 1.754 | 1.703 | 1.640 | 1.576 |
65	| tail_decay | -0.0023 | -0.0022 | -0.0022 | -0.0022 | -0.0022 |
66	
67	**Key findings:**
68	- **H2 confirmed for surface features**: ttr and hapax_ratio show strong monotonic decrease — vocabulary impoverishment accelerates with depth, with the largest jump at d=0→1 (Cohen's d ≈ 1.45).
69	- **H1 partially confirmed for reference features**: entropy_std, entropy_max, and tail_decay are near-stationary. However, **entropy_mean is a clear exception** — it drifts strongly (rho=-0.675), behaving like an H2 feature.
70	- **entropy_min is borderline** (rho=-0.48): moderate correlation, classified H1 but could be argued either way.
71	- The diminishing effect sizes at higher depths (d>2) suggest a saturation effect — features become less discriminative at deeper generations.
72	
73	---
74	
75	## Part C: Perplexity Pre-validation
76	
77	4609 records scored with Pythia-410M. HighPPL threshold = 100.
78	
79	| Depth | Mean | Median | Std | N | HighPPL% | Clean Mean | Clean Median | Clean N |
80	|---|---|---|---|---|---|---|---|---|
81	| 0 | 13.98 | 13.50 | 4.41 | 995 | 0.00% | 13.98 | 13.50 | 995 |
82	| 1 | 6.68 | 4.96 | 22.52 | 989 | 0.51% | 5.28 | 4.95 | 984 |
83	| 2 | 5.14 | 3.00 | 14.10 | 923 | 0.76% | 4.07 | 2.98 | 916 |
84	| 3 | 7.74 | 2.07 | 62.87 | 879 | 0.68% | 3.48 | 2.06 | 873 |
85	| 4 | 7.33 | 1.72 | 95.29 | 822 | 0.49% | 2.65 | 1.72 | 818 |
86	
87	**Kruskal-Wallis (all):** H=2752.78, p=0.0
88	**Kruskal-Wallis (clean):** H=2813.66, p=0.0
89	
90	**Key findings:**
91	- Perplexity **decreases monotonically** with depth (clean median: 13.50 → 4.95 → 2.98 → 2.06 → 1.72). Generated text becomes increasingly predictable to the reference model at each depth.
92	- The mean PPL is noisy at d≥1 due to high-variance outliers (disambiguation pages, category stubs), but medians are clean and monotonic.
93	- The biggest perplexity drop is d=0→d=1 (13.50 → 4.95, -63%), confirming that the first generation already dramatically shifts the distribution.
94	- Degenerate samples are rare (<1%) and concentrated at depth 1, all appearing to be short/structured text (disambiguation pages).
95	- The Kruskal-Wallis test is overwhelmingly significant, confirming perplexity varies meaningfully across depths.
96	
97	---
98	
99	## Support for Claim 2: Feature Complementarity & Dual Dynamics
100	
101	### Evidence Supporting Claim 2
102	
103	1. **Complementarity is real and significant.** Full features (0.8204) outperform both surface_only (0.7628, +5.8 pts, p<0.001) and reference_only (0.7187, +10.2 pts, p<0.001). The gain from combining is not marginal — it's 5-10 F1 points with high statistical significance.
104	
105	2. **Both subsets carry independent signal.** reference_only achieves macro-F1=0.72 using only distributional shape features — this would not be possible if reference features were just proxying surface features. surface_only achieves 0.76. Neither subsumes the other.
106	
107	3. **Surface features show clear H2 drift.** ttr and hapax_ratio decrease monotonically with depth, with the largest effect at d=0→1 (Cohen's d≈1.45). This directly demonstrates vocabulary impoverishment.
108	
109	4. **Perplexity validates the depth signal.** PPL drops monotonically with depth, providing independent confirmation that the reference model perceives a distributional shift across generations.
110	
111	### Complications and Caveats
112	
113	1. **entropy_mean breaks the clean dichotomy.** It is a reference-model feature (computed from token-level entropy of the reference model), yet it shows strong H2 drift (rho=-0.675), not H1 stationarity. This means the "reference=stationary shape, surface=drifting lexicon" narrative oversimplifies — at least one distributional shape feature also tracks depth monotonically. Possible reframe: entropy_mean captures the *average predictability* of text to the reference model, which is conceptually closer to perplexity than to distributional shape. The *shape* features (std, min, max, tail_decay) remain near-stationary.
114	
115	2. **Surface > reference (marginally).** Surface features alone outperform reference features alone (0.76 vs 0.72, p=0.031). The complementarity is asymmetric — surface features are the stronger individual contributor, consistent with hapax_ratio having the highest feature importance (0.30) in the MVP.
116	
117	3. **Saturation at deeper depths.** Effect sizes shrink substantially beyond d=2. The dual-dynamics narrative holds strongest for the d=0→d=1→d=2 transition; at d=3+ both feature types plateau, making deeper generations harder to distinguish from each other.
118	
119	4. **gen-1 remains the weak point.** Across all feature sets, gen-1 has the lowest per-class F1 (0.61–0.75). First-generation text occupies a middle ground that neither feature family fully captures.
120	
121	### Verdict
122	
123	**Claim 2 is broadly supported with one important nuance.** The complementarity hypothesis holds: combining surface and reference features yields significantly better depth classification than either alone. The H2 (drift) pattern is clearly confirmed for surface features. However, the "dual dynamics" framing — where reference features are stationary and surface features drift — requires refinement because entropy_mean (a reference feature) also drifts strongly. A more precise formulation:
124	
125	> Surface features (ttr, hapax_ratio) and reference-model *shape* features (entropy_std, entropy_max, tail_decay) capture complementary aspects of the depth signal. Surface features track monotonic vocabulary impoverishment; shape features capture distributional structure that is relatively depth-invariant but discriminative. entropy_mean bridges both dynamics, tracking average predictability shift.
126	
127	---
128	
129	## Unexpected Findings / Issues
130	
131	1. **Result files not persisted.** The log reports "Saved: results/ablation_results.json" etc., but these files do not exist on disk. Only `mvp_results.json` is in the results directory. The script's output was captured in the log, so no data is lost, but the missing files should be investigated (possible working directory mismatch or cleanup).
132	
133	2. **High-variance outliers at depth 1.** Five degenerate samples (PPL 116–460) are all disambiguation/category pages — structured Wikipedia artifacts that leaked into the generation pipeline. These don't affect the overall conclusion (clean Kruskal-Wallis is even stronger) but suggest a data cleaning opportunity.
134	
135	3. **Diminishing returns beyond depth 2.** Both feature types and perplexity show substantial saturation beyond d=2. For practical applications, a 3-class formulation (d=0 / d=1 / d≥2) may be more robust than fine-grained depth estimation.
136	
137	---
138	
139	## Summary Table
140	
141	| Metric | Value | Status |
142	|---|---|---|
143	| Full-feature macro-F1 (ablation) | 0.8204 | > MVP baseline (0.84 on unbalanced test) |
144	| surface_only macro-F1 | 0.7628 | Independent signal confirmed |
145	| reference_only macro-F1 | 0.7187 | Independent signal confirmed |
146	| Full vs subsets (paired t-test) | p < 0.001 | Complementarity significant |
147	| H2 for ttr, hapax_ratio | rho = -0.63, -0.66 | Confirmed (monotonic drift) |
148	| H1 for entropy_std, max, tail_decay | |rho| < 0.16 | Confirmed (near-stationary) |
149	| H1 for entropy_mean | rho = -0.68 | **Rejected** (drifts like H2) |
150	| Perplexity vs depth | Kruskal-Wallis p = 0.0 | Significant monotonic decrease |
151	| Claim 2 support | Supported with nuance | entropy_mean complicates dual-dynamics framing |
152	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19ef2d10-b029-4424-863b-37b659209e63",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "99b7aa08-a0b8-4c76-bb5c-c7e94d64a86c",
  "sourceToolAssistantUUID": "19ef2d10-b029-4424-863b-37b659209e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-14T23:09:00.812Z_

I now have a thorough understanding of the paper, the experiment plan (14 experiments), the actual results from completed experiments (plan-001-fix), the imagined/projected results for all experiments, and the prior dream review. Let me now also check the key discrepancies between the paper summary provided by the user and the actual paper content.

Now let me compare the user-provided "Key Results" summary against the paper's actual numbers to check for consistency issues:

The user summary mentions several numbers that differ from the paper:
- "LOGO F1 = 0.52" vs paper reports 0.64 
- "cross-family drops to 0.41-0.48" vs paper reports LOFO ~0.59
- "entropy_mean rho=-0.22 (OLMo) vs rho=-0.15 (Qwen)" vs paper reports -0.42 and -0.36
- "F1 correlates with log-params at r=-0.85; 8B generator yields F1=0.43" vs paper reports 0.57
- "cross-prompt transfer F1=0.42" vs paper doesn't mention this specific number
- "cross-model chains F1=0.39" vs paper reports 0.56
- "5-class ordinal F1=0.28" vs paper reports 0.43
- "length-controlled F1 drops from 0.78 to 0.68" vs paper reports 0.82 to 0.78
- "downstream p=0.31" vs paper reports CI overlap but no specific p-value

The user's "Key Results" appear to be from a different (possibly earlier/worst-case) version of the paper, while the paper I'm reviewing is the median-tier dream paper. This is significant -- the "Experiment Design Reference" thresholds in the user prompt appear to be calibrated against the earlier/worse results, while the paper being reviewed has substantially better numbers. I should review the paper as written (the median dream), which is what was provided.

Now I have sufficient information to produce my review. Let me submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99b7aa08-a0b8-4c76-bb5c-c7e94d64a86c",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JYCyv1A4edKkRveunm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69536feb-3dfe-408d-96b7-dc62b13c01f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShcjMQNo6jxVVhAvg6uXQe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4051,
      "cache_read_input_tokens": 90044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4051,
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

_source line 49 · 2026-05-14T23:09:03.550Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KqrYvmtZpJC6GCMjoRJ8Qo`</summary>

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
  "parentUuid": "69536feb-3dfe-408d-96b7-dc62b13c01f3",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JYCyv1A4edKkRveunm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ed4675f-db2c-4177-a1cf-9e2be0d6ba8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShcjMQNo6jxVVhAvg6uXQe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4051,
      "cache_read_input_tokens": 90044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4051,
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

_source line 50 · 2026-05-14T23:09:03.558Z_

<details><summary>↩ Tool result · `toolu_01KqrYvmtZpJC6GCMjoRJ8Qo`</summary>

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
  "parentUuid": "3ed4675f-db2c-4177-a1cf-9e2be0d6ba8a",
  "isSidechain": true,
  "promptId": "ae4f8a4b-cb42-46fe-bb2c-5826f12cb691",
  "agentId": "aad193fce74ed6217",
  "type": "user",
  "uuid": "1f413024-5851-4d31-aa88-390c845a5e71",
  "sourceToolAssistantUUID": "3ed4675f-db2c-4177-a1cf-9e2be0d6ba8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-14T23:11:08.741Z_



Here is my review:

### R1: Methods and Experiments

**Score: 4/6 (Weak Accept)**

**Summary**
The paper formalizes generation depth estimation as an ordinal classification task, extracts 7 distributional features (2 surface, 5 reference-model NLL statistics), and trains XGBoost classifiers evaluated across 12 experimental conditions covering generators, domains, prompt types, chain types, robustness, and scaling. The experimental design is comprehensive and well-structured, with a logical hierarchy from controlled within-generator evaluation to progressively harder generalization tests. The main methodological concerns are inflated trend statistics (R^2 on 5 aggregated points), missing confidence intervals on key tables, absence of ordinal baselines from existing detector scores, and a shared-reference-model confound that inflates Pythia-family LOGO results.

**Strengths**
- Well-designed evaluation hierarchy: within-generator CV, LOGO, LOFO, cross-reference, cross-model chains, cross-domain -- systematically increasing difficulty and peeling away confounds one at a time.
- All 14 planned experiments are present and accounted for. No cherry-picking or selective reporting is apparent.
- Text length confound analysis (Section 4.4) is a critical control that many papers omit. The fixed-window analysis (128-token windows) isolating the length component of surface feature slopes is particularly well-executed. The finding that ~30% of surface feature signal tracks length is honestly reported.
- The cross-reference model experiment (Section 4.3) is the correct falsification test for Claim 2. Testing with three independent reference models (Pythia-410M, OLMo-2-1B, Qwen3-0.6B) and showing the level/shape split persists (even if drift magnitude varies ~2x) is methodologically sound.
- Paraphrastic vs non-paraphrastic comparison provides theoretical grounding by connecting to attractor cycle theory and empirically validates the paper's focus on continuation chains.
- QLoRA end-to-end comparison validates the handcrafted feature approach -- handcrafted features outperform (0.82/0.64 vs 0.79/0.61) at 60x lower inference cost, confirming that simple distributional statistics suffice.
- Pre-registered LD-Score prediction provides genuine out-of-sample framework validation. The confirmed prediction (H2 level feature, rho=-0.55) with negligible marginal classification improvement is cleanly reported.
- Downstream utility experiment uses OLMo-1B for fine-tuning (avoiding Pythia-410M reference model circularity), runs 3 seeds with bootstrap CIs, and includes sample-count-matched comparison to control for data volume confound.
- Honest limitation reporting throughout -- the paper does not hide the CI overlap in downstream utility, the 7B+ attenuation, or the cross-model chain degradation.

**Weaknesses**
- **R^2 values in Table 2 are computed on 5 aggregated depth-group means, not individual samples.** With only 5 data points and 3 degrees of freedom, these R^2 values (0.81-0.93 for H2 features) are statistically meaningless -- any monotonic trend across 5 points will produce high R^2 regardless of noise. This is the empirical backbone of the H1/H2 partition (Claim 2). The actual plan-001-fix results report individual-level Spearman correlations (entropy_mean rho=-0.675, TTR rho=-0.633, hapax_ratio rho=-0.655) which are the correct statistics but are buried. The paper should lead with these, not the inflated R^2.
- **No per-generator confidence intervals on LOGO results (Table 3).** Point estimates of 0.71-0.72 for Pythia holdouts vs 0.59-0.62 for OLMo/Qwen holdouts look like a significant family effect, but without CIs it is impossible to assess whether these differences are statistically reliable or within noise. LOFO results (Table 4) have CIs; LOGO should too.
- **Shared reference model (Pythia-410M) confounds LOGO generalization claims.** All primary LOGO experiments extract features using Pythia-410M. Pythia generators' higher LOGO F1 (0.71-0.72) likely reflects shared tokenizer and pretraining data distribution, not superior depth signal transfer. The paper acknowledges this indirectly (Section 4.2: "the Pythia-410M reference model's advantage is partially family-specific") but does not quantify it. A fairer headline LOGO number would use cross-family reference models for cross-family holdouts.
- **No ordinal baselines from existing detectors.** FastDetectGPT, Binoculars, and LD-Score all produce continuous scores. These could be directly regressed on depth or used as ordinal predictors. Without this comparison, it is unclear whether the custom 7-feature set adds value over simply repurposing existing detector scores for ordinal prediction. The downstream comparison (Section 4.12) uses binary thresholds from these detectors, not their continuous scores -- this is an unfair comparison.
- **No leave-one-feature-out ablation.** The 3-way ablation (full / surface-only / reference-only) is too coarse. It cannot distinguish per-feature importance. The MVP reported feature importances (hapax_ratio=0.30, entropy_mean=0.22, TTR=0.17), but these are XGBoost split-based importances which are known to be biased toward high-cardinality features. Permutation importances or individual leave-one-out would be more informative.
- **entropy_min classification is inconsistent.** The plan-001-fix analysis reports entropy_min rho=-0.4797, which is well above the |rho|<0.3 threshold used to define H1. The paper classifies it as H1 (Table 2: R^2=0.06, p=0.19), but these are on aggregated means. On individual samples, entropy_min appears to be an intermediate/borderline feature that blurs the clean H1/H2 partition. This undermines the crisp two-category framework.
- **H1/H2 partition sensitivity is untested with additional features.** The clean split (all features clearly H1 or H2 except entropy_min) could be an artifact of the specific 7 features chosen. Adding features like NLL kurtosis, skewness, burstiness, or entropy_median might populate the ambiguous zone and blur the boundary. Without this sensitivity test, the "dual dynamics" framing is overfit to the selected feature set.
- **No calibration analysis.** For risk-stratified data curation (the paper's main practical pitch), classifier calibration is essential. There are no reliability diagrams, expected calibration error (ECE), or confidence analysis. A well-calibrated depth classifier with modest accuracy could be more useful than a poorly calibrated one with higher F1.
- **Continuation-dominant headline numbers overstate practical accuracy.** The abstract leads with F1=0.82 (within-generator, continuation). Under elaboration (0.77), inspired rewriting (0.69), cross-model chains (0.56), creative writing domain (0.57), or 7B+ generator (0.57), performance drops substantially. The realistic operating range for deployment is 0.56-0.69 in most non-ideal conditions, not 0.82.
- **Hyperparameter sensitivity for XGBoost is not reported.** Default or lightly tuned XGBoost could significantly affect results. No sensitivity analysis to tree depth, learning rate, number of estimators, or regularization parameters.
- **No test on naturally occurring web data.** All experiments use laboratory-constructed chains. The ecological validity gap between synthetic chains and actual recursive web contamination (which involves diverse generators, editing, partial chains, mixed content) is substantial and unaddressed.
- **Only base models tested.** All generators are base (pretrained) models. Instruction-tuned and RLHF-aligned models dominate real-world generation. Their output distributions differ substantially from base models, and depth signal behavior could change.

**Detailed Comments**

1. **Table 2 statistical validity.** The linear regression R^2 values in Table 2 are computed by regressing feature group means (5 points) against depth. This inflates the apparent trend strength: fitting a line to 5 points with 3 degrees of freedom will almost always yield high R^2 for any monotonic pattern regardless of the actual sample-level noise. The correct approach is to report individual-level Spearman rho with bootstrap CIs, which the underlying analysis (plan-001-fix) actually computed: entropy_mean rho=-0.675, TTR rho=-0.633, hapax_ratio rho=-0.655. These are strong correlations but substantially less impressive than R^2=0.93/0.87/0.81. The H1 features also have individual-level rho values (entropy_std rho=-0.153, entropy_max rho=-0.035, tail_decay rho=0.063) that confirm near-stationarity but show that entropy_std is not zero. The paper should replace Table 2 with individual-level statistics.

2. **LOGO confound from shared reference model.** The LOGO evaluation (Table 3) reports Pythia holdout F1 of 0.71-0.72 vs OLMo/Qwen holdout F1 of 0.59-0.62. This ~0.12 gap could reflect (a) genuine within-family depth signal transfer, (b) Pythia-410M reference model bias, or (c) both. The Section 4.2 paragraph on feature ablation under LOGO partially addresses this (full-vs-surface gap narrows from 0.06 to 0.03), but the correct control would be to rerun LOGO with OLMo or Qwen reference models for the non-Pythia holdouts. Section 4.3 provides cross-reference LOGO F1 (OLMo-ref: 0.61, Qwen-ref: 0.58) but these appear to be aggregated across all holdouts, not specifically for same-family holdouts. A 5x3 matrix (5 generator holdouts x 3 reference models) would fully disentangle the confound.

3. **Downstream utility: a well-designed experiment with honestly reported weak results.** The downstream experiment (Section 4.12) correctly uses OLMo-1B (avoiding reference model circularity), runs 3 seeds, reports bootstrap CIs, and includes sample-matched comparison. The result -- depth-aware filtering yields 5.2% [3.8, 7.1] improvement vs FastDetectGPT's 3.8% [2.1, 5.9], with overlapping CIs -- is honestly reported. The sample-matched comparison (2.8% vs 1.9%, also overlapping) further demonstrates that roughly half the advantage is from data volume, not selection quality. The paper correctly avoids claiming statistical significance. However, the experiment tests binary filtering baselines using their threshold-based labels, not their continuous scores. Regressing continuous FastDetectGPT scores on depth and using the resulting ordinal predictions for filtering would be a fairer comparison.

4. **7B+ scaling result (Section 4.11) is well-presented as a finding rather than purely a limitation.** F1=0.57 at 8B parameters is substantially above chance (0.33) but substantially below the <=2.8B mean of 0.78. The analysis that entropy_mean rho attenuates from -0.68 to -0.38 and TTR slope weakens proportionally, while H1 shape features remain stable, is informative. The framing as "model capacity determines how much distributional drift accumulates per generation step" is the correct interpretation. However, 8B is still far from frontier scale (70B-400B+), and the paper should more explicitly acknowledge that extrapolating from a single 8B data point to frontier models is speculative.

5. **Cross-model chains (Section 4.5) drop from LOGO F1=0.64 to 0.56.** The 0.08-point degradation when different generators produce each depth step is concerning for ecological validity. Gen-1 vs gen-2+ F1 drops to 0.46/0.44 -- barely above the per-class chance level of 0.33 for those classes. The paper correctly identifies this as a limitation but should be more explicit: in the realistic mixed-generator scenario, the classifier barely distinguishes gen-1 from gen-2+. Only the gen-0 (human) vs synthetic distinction remains robust (F1=0.78).

6. **Missing comparison: cross-prompt transfer.** The paper reports per-prompt-type results (continuation 0.82, elaboration 0.77, rewriting 0.69) but does not report cross-prompt transfer (train on continuation, test on elaboration). This is an important ecological validity test -- in practice, the prompt type is unknown at test time.

7. **Feature engineering scope.** Seven features is a small feature set. The paper does not discuss why these specific 7 were chosen over alternatives (e.g., NLL percentiles, kurtosis, skewness, n-gram repetition rates, sentence-level variance, discourse coherence features). A broader feature search followed by feature selection could strengthen the approach without changing the conceptual contribution.

8. **Discrepancy between paper numbers and underlying data.** Table 2 in the paper reports entropy_mean slope=-0.148, R^2=0.93, while the plan-001-fix analysis reports Spearman rho=-0.675 on individual samples. The paper presents the aggregated-mean regression as if it were the primary analysis. Similarly, entropy_min is classified as H1 in the paper (R^2=0.06) but has individual-level rho=-0.48 in the underlying data -- a non-trivial correlation that is suppressed by the aggregation.

**Questions for Authors**

1. Are Table 2 R^2 values computed on 5 group means or on individual samples? If group means, please replace with individual-level Spearman rho with bootstrap CIs. The plan-001-fix analysis already has these numbers.

2. entropy_min has individual-level Spearman rho=-0.48 -- how do you justify classifying it as H1 (stationary)? Does removing entropy_min from the H1 category or creating a third "borderline" category change any downstream conclusions?

3. Have you tested FastDetectGPT, Binoculars, or LD-Score continuous scores as ordinal depth predictors (not just as binary classifiers)? What is the Spearman correlation between FastDetectGPT score and true depth?

4. Can you provide per-generator bootstrap CIs for Table 3 LOGO results? Is the Pythia-family advantage (0.71-0.72 vs 0.59-0.62) statistically significant?

5. What happens to the H1/H2 partition if you add NLL kurtosis, skewness, or burstiness features? Do any fall in the ambiguous zone between H1 and H2?

6. Why were only base models tested? Instruction-tuned models (Qwen3-1.7B-Instruct, OLMo-1B-Instruct) produce different output distributions. Have you verified that depth signal persists under instruction tuning?

7. Have you evaluated cross-prompt transfer (train on continuation chains, test on elaboration or rewriting chains)? This is critical for practical deployment where prompt type is unknown.

8. What are the XGBoost hyperparameters, and how sensitive are the results to hyperparameter choices? Was any hyperparameter search performed?

9. Can you provide ECE and reliability diagrams for the classifier? For risk-stratified curation, calibration matters more than raw F1.

10. The 5.2% downstream perplexity improvement uses binary thresholding of existing detectors as baselines. If you instead use FastDetectGPT's continuous score as a soft filtering weight (e.g., weighted sampling proportional to "realness" score), does the depth-aware advantage persist?

**Experiment Coverage Assessment**

All 14 planned experiments from the experiment plan are reflected in the paper:

| Plan ID | Name | Paper Section | Status |
|---------|------|---------------|--------|
| plan_001 | feature_ablation_and_trend | 4.1 | Covered (Tables 1-2) |
| plan_002 | cross_generator_evaluation | 4.2 | Covered (Tables 3-5) |
| plan_003 | cross_family_reference_model | 4.3 | Covered (Tables 6-7) |
| plan_004 | downstream_utility | 4.12 | Covered (Tables 8-9) |
| plan_005 | prompt_type_comparison | 4.5 | Covered (Table 10) |
| plan_006 | paraphrastic_comparison | 4.5 | Covered |
| plan_007 | cross_model_chains | 4.5 | Covered |
| plan_008 | multi_domain_seeds | 4.6 | Covered (Table 13) |
| plan_009 | finer_grained_ordinal | 4.7 | Covered (Table 14) |
| plan_010 | human_edit_robustness | 4.8 | Covered (Table 15) |
| plan_011 | ld_score_feature | 4.9 | Covered (Table 16) |
| plan_012 | end_to_end_classifier | 4.10 | Covered (Table 17) |
| plan_013 | text_length_control | 4.4 | Covered (Tables 18-20) |
| plan_014 | large_scale_generator | 4.11 | Covered (Tables 21-22) |

Coverage: **14/14 (100%).** No planned experiment is missing. The coverage is comprehensive and the ordering in the paper is logical (controlled settings first, then progressively harder generalization tests, then scaling and baselines, then downstream application).

**Evidence strength for each claim:**

- **Claim 1 (Task formulation + depth discriminability):** Strong within-generator (F1=0.82, well above chance). Moderate cross-generator (LOGO F1=0.64, LOFO F1=0.59). Weakens substantially under realistic conditions (cross-model 0.56, 7B+ 0.57, creative domain 0.57). Evidence supports feasibility but not practical deployability.

- **Claim 2 (Dual dynamics / level vs shape split):** Supported in direction but overframed in magnitude. The level/shape split is real across all reference models, but (a) the statistical evidence is weakened by R^2 on 5 points, (b) entropy_min is a borderline case that blurs the partition, (c) the partition's robustness to additional features is untested, and (d) the observation that location statistics drift while scale statistics remain stable under distributional shift is not surprising from a statistical perspective.

- **Claim 3 (Downstream utility):** Partially supported. Depth correlates with fine-tuning quality degradation (rho=0.53). Depth-aware filtering outperforms binary baselines on point estimates but CIs overlap. Roughly half the advantage is from data volume. The claim is correctly softened to "complementary signal" in the paper, which matches the evidence.

- **Comprehensive limitations (meta-claim):** Well supported. The paper honestly reports every degradation condition (cross-generator, cross-family, cross-model, cross-domain, cross-prompt, scaling, editing). This is a strength of the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f413024-5851-4d31-aa88-390c845a5e71",
  "isSidechain": true,
  "agentId": "aad193fce74ed6217",
  "requestId": "req_011Cb3JZZYhtKfxfFoWfhnvz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e17132c-bbc9-4f19-8c10-4e66fa5acf82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5f594e8-570b-47df-b34a-5c33d75d6e0f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTEnyoth3b8HKAzDKB9L2d",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1147,
      "cache_read_input_tokens": 94095,
      "output_tokens": 4705,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1147
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4705,
          "cache_read_input_tokens": 94095,
          "cache_creation_input_tokens": 1147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1147,
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
