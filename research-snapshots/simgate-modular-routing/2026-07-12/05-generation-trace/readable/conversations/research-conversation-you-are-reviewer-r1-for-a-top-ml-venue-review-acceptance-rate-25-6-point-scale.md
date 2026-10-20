# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Y

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab0cde6016829d46f.jsonl`
- **Structured JSON:** [`48cdc8512b315ace2286.json`](../../sessions/48/48cdc8512b315ace2286.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-13T16:17:26.363Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus: **Methods and Experiments**.

## Paper Summary

**Title**: "When Does Deterministic Computation Help LLM Agents? A Diagnostic Study on ScienceWorld"

**Core idea**: The paper introduces a counterfactual evaluation methodology that forks agent trajectories at each decision step across three computation modalities (fast internal, deep chain-of-thought, deterministic simulation), and measures per-step value via hindsight scoring. Applied to 15 ScienceWorld task types (300 episodes, 6,600 labeled steps). Key findings are negative: learned per-step routing (SimGate) ≈ always-simulate; explicit ≈ implicit routing; routing patterns don't transfer across tasks. The positive finding: deterministic computation helps only on 4/15 death-risk task types.

**Method (SimGate)**:
- Backbone: Qwen2.5-7B agent
- Router: Qwen3-1.7B, SFT on counterfactual labels
- 3-way classification: fast-internal / deep-internal / deterministic
- 80/20 stratified split, lr=2e-5, batch=32, 3 epochs
- Router achieves 58% 3-way val accuracy (majority baseline: 42%), macro-F1: 0.53

**Main Results (Table 2)**:
| Method | All | DR4 | MR3 | LR8 | CF% |
|---|---|---|---|---|---|
| Always-internal | 59.5 | 13.5 | 57.3 | 83.3 | 19.7 |
| Always-det | 64.8 | 45.5 | 58.0 | 77.0 | 6.3 |
| SimGate | 65.2 | 38.5 | 58.0 | 81.3 | 13.0 |
| Oracle | 70.0 | 46.5 | 62.0 | 84.8 | 4.0 |
| CogRouter† | 84.6 | — | — | — | — |
| ITP-R† | 62.58 | — | — | — | — |

SimGate vs always-det: Δ=0.4, 90% CI [-4.8, 5.6] — not significant.

**Explicit vs Implicit (Table 4)**: Δ=1.2, p=0.38, 90% CI [-2.3, 4.7] — not significant.

**Per-task breakdown (Table 3)**: 4 death-risk tasks show +16 to +29 gains; all 8 low-risk tasks show -2 each.

**Ablations**:
- 2-way vs 3-way routing: Δ=0.4, CI [-3.1, 3.9] — no difference
- Router size (1.5B/1.7B/3B): 64.0–65.8, within noise
- Cross-task transfer: accuracy drops 13-8 points out of domain

**Counterfactual label analysis**: 42% overall ambiguity rate; death-risk tasks have 70% det-preferred and only 22% ambiguous; low-risk tasks 52% ambiguous.

**Experiment coverage reference** (from review_context.yaml — planned experiments):
1. plan-001: Counterfactual trajectory collection (15 task types) — COVERED in paper
2. plan-002: Router SFT training (Qwen3-1.7B) — COVERED
3. plan-003: SimGate end-to-end evaluation — COVERED
4. plan-004: Explicit vs implicit routing ablation — COVERED
5. plan-005: Per-task routing pattern analysis — PARTIALLY covered (routing heatmap, phase analysis, entropy distribution mentioned but figures not shown in paper)
6. plan-006: 2-way vs 3-way routing ablation — COVERED
7. plan-007: Boil task rerun with v3 code — NOT explicitly reported (may be folded into main results)
8. plan-008: Router size ablation — COVERED
9. plan-009: MATH track — NOT attempted (acknowledged in limitations)
10. plan-010: Cross-task transfer — COVERED

Key context from YAML:
- 42% ambiguous labels (margin < 5) is root cause of all downstream failures
- Router's 55% deterministic recall means 45% of death-risk steps are missed
- SimGate's catastrophic failure rate (13%) vs always-det (6.3%) is directly due to router misses
- Oracle ceiling is only 5.2 points above always-det — theoretical ceiling is low
- The paper pivoted from "safety-aware modular routing" to "When Does Deterministic Computation Help?" framing

## Your Review Task

Provide a structured review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (methods + experiments focus)
3. **Weaknesses** (methods + experiments focus)
4. **Questions to authors**
5. **Missing experiments** (compare against planned experiments in YAML)
6. **Soundness rating** (1-5)
7. **Overall score** (1-6 scale)
8. **Confidence** (1-5)

Be rigorous. Evaluate: Is the counterfactual methodology sound? Are baselines fair? Are statistical tests appropriate? Is the experimental scale sufficient? Are negative results convincingly established? Are there confounds?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "591c2ed1-3ef6-4a13-8a72-9398c1b4ff80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T16:17:26.369Z_

```json
{
  "parentUuid": "591c2ed1-3ef6-4a13-8a72-9398c1b4ff80",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
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
  "uuid": "c82a01ad-46db-4b63-8ad8-19d5c2560d02",
  "timestamp": "2026-05-13T16:17:26.369Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T16:17:30.136Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c82a01ad-46db-4b63-8ad8-19d5c2560d02",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsN6oPmHmJ5g5HTw2Rd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6caf802-d87b-4777-aae9-eea9b79c3c05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Cg74w3LKw7J9GYR4R9a4h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15435,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15435,
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

_source line 4 · 2026-05-13T16:17:31.484Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YGG4vL4ZkJ5kVAosCuWeDo`</summary>

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
  "parentUuid": "b6caf802-d87b-4777-aae9-eea9b79c3c05",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsN6oPmHmJ5g5HTw2Rd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76f89e7e-ba8c-4f98-84f4-92a8d3d7976e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Cg74w3LKw7J9GYR4R9a4h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15435,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15435
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15435,
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

_source line 5 · 2026-05-13T16:17:31.490Z_

<details><summary>↩ Tool result · `toolu_01YGG4vL4ZkJ5kVAosCuWeDo`</summary>

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
  "parentUuid": "76f89e7e-ba8c-4f98-84f4-92a8d3d7976e",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "048229da-c2dd-4cd1-8756-45e83f4b78e2",
  "sourceToolAssistantUUID": "76f89e7e-ba8c-4f98-84f4-92a8d3d7976e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T16:17:36.127Z_



Let me read the paper and all relevant project files systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "048229da-c2dd-4cd1-8756-45e83f4b78e2",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsNUnyuACBpSSSW8gJA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0003615-23a3-44f2-b1e1-7a0371992f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jWwXd27D5GRXSqUie5H4h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15435,
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

_source line 7 · 2026-05-13T16:17:36.568Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_017xVSg41WEXU2hR6eBT5s31`</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0003615-23a3-44f2-b1e1-7a0371992f1c",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsNUnyuACBpSSSW8gJA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef5107a2-4f62-4f9e-9fd1-83bafd366b2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jWwXd27D5GRXSqUie5H4h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15435,
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

_source line 8 · 2026-05-13T16:17:36.609Z_

<details><summary>↩ Tool result · `toolu_017xVSg41WEXU2hR6eBT5s31`</summary>

```text
{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (8 个)\n\n- **mvp-p1-gpu1-v3**: DONE (success) — \n- **mvp-p1-gpu0-vllm**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n- **mvp-p0-forking**: DONE (success) — \n- **mvp-p1-signal**: PREPARING — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- mvp-p1-signal（准备中）\n\n## 近期结论\n- **mvp-p1-gpu1-v3** (success): —\n- **mvp-p1-gpu0-vllm** (success): —\n- **mvp-p1-gpu0** (killed): —\n\n## 趋势\n成功 3 / 负向 0 / 失败 0 / 共 7\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-13313: 无 GPU 信息\n\n## 告警\n- mvp-p1-gpu1: 已被终止 — unknown\n- mvp-p1-gpu0: 已被终止 — unknown\n- mvp-p1-gpu1-vllm: 已被终止 — unknown\n- mvp-p1-gpu1-v2: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef5107a2-4f62-4f9e-9fd1-83bafd366b2a",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "7b6ba21d-6612-40d6-a817-6f848ea27dc5",
  "sourceToolAssistantUUID": "ef5107a2-4f62-4f9e-9fd1-83bafd366b2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T16:17:37.149Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017smdVdJySSTnw7qr44Bynh`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b6ba21d-6612-40d6-a817-6f848ea27dc5",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsNUnyuACBpSSSW8gJA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "462b77f0-5afd-4469-933c-127b3854f9f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019jWwXd27D5GRXSqUie5H4h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15435,
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

_source line 10 · 2026-05-13T16:17:37.159Z_

<details><summary>↩ Tool result · `toolu_017smdVdJySSTnw7qr44Bynh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- mvp-p1-signal（准备中）\\n\\n## 近期结论\\n- **mvp-p1-gpu1-v3** (success): —\\n- **mvp-p1-gpu0-vllm** (success): —\\n- **mvp-p1-gpu0** (killed): —\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 0 / 共 7\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-13313: 无 GPU 信息\\n\\n## 告警\\n- mvp-p1-gpu1: 已被终止 — unknown\\n- mvp-p1-gpu0: 已被终止 — unknown\\n- mvp-p1-gpu1-vllm: 已被终止 — unknown\\n- mvp-p1-gpu1-v2: 已被终止 — unknown\\n\", \"total_chars\": 443, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "462b77f0-5afd-4469-933c-127b3854f9f1",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "32677b03-e4e9-4fbd-9698-df24bf62a52a",
  "sourceToolAssistantUUID": "462b77f0-5afd-4469-933c-127b3854f9f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T16:17:40.352Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017v86huob3riRpd6o1DFPtH`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32677b03-e4e9-4fbd-9698-df24bf62a52a",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsNu5yYax23cPLNo6SX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95e5a04d-4b4c-4eb1-8195-1b098f019e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L16qYt47G2NUFWwDaZRBDu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1242,
      "cache_read_input_tokens": 16883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1242,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 12 · 2026-05-13T16:17:40.361Z_

<details><summary>↩ Tool result · `toolu_017v86huob3riRpd6o1DFPtH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 7\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-deterministic）。这是 1-step 的本质局限而非 bug。直接比较 det vs\\n    internal 能回答核心问题\\\"确定性计算有没有用\\\"，无需 oracle 作为中介。oracle 在密集 reward tasks 上仍有参考价值。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 15:25 UTC\\n  summary: MVP Phase 1 判定 PASS — det > internal 在 ≥2/5 task types 上统计显著，oracle > det\\n    信号支持 router 训练\\n  rationale: melt (+40.15, CI [25, 60.15]) 和 change-state (+40.2, CI [25, 60.15])\\n    满足 ≥2/5 Pass 标准。mix-paint (+35.5) 大概率也通过。grow-plant (0.0) 符合预期（pre-registered\\n    weak/对照）。最关键发现：oracle > det（melt +16.7, change-state +14.95, mix-paint +10.0）证明\\n    selective routing 有额外增量——这是 SimGate router 训练的信号来源。信号机制是 death avoidance（避免 -100\\n    致死动作）而非正向引导，论文 framing 需定位为 safety-aware routing。待确认：melt/change-state 数据重复性、mix-paint\\n    CI、boil v3 重跑。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: boil data (old code)\\n    result: det-int +30.1\\n  - exp_id: mvp-p1-gpu0-vllm\\n    role: melt+change-state (v3)\\n    result: det-int +40.15/+40.2, CI [25, 60.15]\\n  - exp_id: mvp-p1-gpu1-v3\\n    role: mix-paint+grow-plant (v3)\\n    result: det-int +35.5/0.0\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 15:37 UTC\\n  summary: 'Research phase plan revised per Reviewer W1-W5: 2-way first, signal pre-screening,\\n    parameter-controlled ablation, GPU units fixed'\\n  rationale: 'Reviewer 提出 5 个实质性问题全部采纳: (1) C1 \\\"selective > unconditional\\\" 标注为待确认;\\n    (2) 2-way collection 优先，与 MVP 一致且省 33% GPU; (3) plan-001 增加 mini signal detection\\n    前置步骤避免浪费 GPU; (4) plan-004 增加 1.7B implicit 控制条件隔离架构效果; (5) GPU 预算改为 RTX 5090\\n    实际时长。melt/change-state 确认非重复但共享 variations，论文中合并报告。'\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n\", \"total_chars\": 3381, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95e5a04d-4b4c-4eb1-8195-1b098f019e4e",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "28eca96e-2371-4d0d-b72d-28f6b52dde08",
  "sourceToolAssistantUUID": "95e5a04d-4b4c-4eb1-8195-1b098f019e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T16:17:40.827Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QydB7iDKSo5WiS4mBiop25`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28eca96e-2371-4d0d-b72d-28f6b52dde08",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsNu5yYax23cPLNo6SX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b03452a0-1476-4cc2-97c5-76fa31018feb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L16qYt47G2NUFWwDaZRBDu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1242,
      "cache_read_input_tokens": 16883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1242,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 14 · 2026-05-13T16:17:40.836Z_

<details><summary>↩ Tool result · `toolu_01QydB7iDKSo5WiS4mBiop25`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\", \"content\": \"## Phase 1 MVP 最终结论 (2026-05-13)\\n\\n### Verdict: PASS (4/5 tasks 显著正向)\\n\\nPhase 1 验证了 fork-based deterministic evaluation 在 ScienceWorld 上显著优于纯 LLM 内部推理。\\n\\n### 关键设计决策与教训\\n\\n1. **Tie-break 策略**: `>` (strict) 而非 `>=`。95%+ 步骤 score_delta=0（稀疏奖励），`>=` 会让 oracle 退化为 always-internal。用 `>` 后 oracle 在 tie 时选 deterministic，实验验证这是合理的。\\n\\n2. **Death filter 只用于有 fork 的模式**: always-internal 是纯 LLM baseline，不能调 fork/is_lethal（方法论问题——Reviewer 会质疑\\\"你在 internal 模式偷偷用了外部计算\\\"）。death filter 只在 always-deterministic 和 oracle 中生效。\\n\\n3. **melt 与 change-state internal 分数巧合相同的解释**: 两个 task 共享 ScienceWorld environment variations（同房间/物品/布局），LLM 表现极差只产生 3 种结果（-100/0/3），分布碰巧一致。不是数据重复。det 分数已验证不同（6/20 episode 有差异）。\\n\\n4. **boil 数据来自旧代码**（>= tie-break, 无 death filter），full phase 需要用新代码重跑以保证一致性。\\n\\n5. **grow-plant 无效果**: 三种模式完全一致（0.5±1.4），可能 task 本身过于简单或 30 步不够。\\n\\n6. **Fork 机制本身没问题**: 诊断确认 fork_and_lookahead 正确工作，score_before 与 main env 一致。收益主要来自避免 -100 致死动作（\\\"focus on 错误对象\\\"），而非精细的 score 区分。\\n\\n7. **vLLM 兼容性**: torch 2.10.0 + vLLM 0.18.1 有 duplicate template name assertion error，需注释 select_algorithm.py 1695/2164 行。\\n\\n8. **Oracle 增量价值**: 在新代码的 3 个 task 上 oracle > det（Δ +10~17），证明 routing 有独立价值，不是简单的 \\\"deterministic always wins\\\"。\\n\\n### 竞品对标\\n- CogRouter (arXiv 2602.12662): 同 Qwen2.5-7B, ScienceWorld Score=84.6, SR=72.0%。路由 thinking depth（4 levels），与我们路由 reasoning vs computation 是不同维度。\\n- ITP-R (arXiv 2601.08955): Learned world model + K-head gating, SR=63.91%。WM 有 compounding error，我们用 deterministic simulator 避免此问题。\\n\", \"total_chars\": 1482, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b03452a0-1476-4cc2-97c5-76fa31018feb",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "43375eb4-c385-42d4-a25d-38c0be7a8206",
  "sourceToolAssistantUUID": "b03452a0-1476-4cc2-97c5-76fa31018feb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T16:17:41.532Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U1T6qaecdBTSGi1FTHNirC`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43375eb4-c385-42d4-a25d-38c0be7a8206",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsNu5yYax23cPLNo6SX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "993af6a6-cf61-4889-be13-03e335250c09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L16qYt47G2NUFWwDaZRBDu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1242,
      "cache_read_input_tokens": 16883,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1242
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 293,
          "cache_read_input_tokens": 16883,
          "cache_creation_input_tokens": 1242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1242,
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

_source line 16 · 2026-05-13T16:17:41.541Z_

<details><summary>↩ Tool result · `toolu_01U1T6qaecdBTSGi1FTHNirC`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "993af6a6-cf61-4889-be13-03e335250c09",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "2d49b561-8431-44ea-bbd1-4cbe250ccf49",
  "sourceToolAssistantUUID": "993af6a6-cf61-4889-be13-03e335250c09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T16:17:44.219Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KUWTCbmKWiQu3JWXoeL9bQ`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d49b561-8431-44ea-bbd1-4cbe250ccf49",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsPDnNAr6GoFBNmkPM7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a22142a-2069-47e6-b80d-6c6a9b936345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELoHr7aM5KjgL7zqvvagiC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3366,
      "cache_read_input_tokens": 18125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3366,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 18 · 2026-05-13T16:17:44.230Z_

<details><summary>↩ Tool result · `toolu_01KUWTCbmKWiQu3JWXoeL9bQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'simgate-modular-routing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a22142a-2069-47e6-b80d-6c6a9b936345",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "6a777929-51fa-4e65-9e59-dcd9a970dc76",
  "sourceToolAssistantUUID": "3a22142a-2069-47e6-b80d-6c6a9b936345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T16:17:45.164Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014bpcufMxPCE6DSJxbkWHTu`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a777929-51fa-4e65-9e59-dcd9a970dc76",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsPDnNAr6GoFBNmkPM7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c8f95bc-81e2-4243-a197-3d3d648cc487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELoHr7aM5KjgL7zqvvagiC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3366,
      "cache_read_input_tokens": 18125,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3366,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 20 · 2026-05-13T16:17:45.174Z_

<details><summary>↩ Tool result · `toolu_014bpcufMxPCE6DSJxbkWHTu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (12 days remaining)\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures at CPU-only cost — but no method learns WHEN to invoke it via an explicit, interpretable router. MVP evidence: death avoidance is the primary mechanism (+30-40 points from preventing -100 penalties), and selective routing outperforms unconditional simulation by +10-17 points.\\n\\n## Core Claims (2 claims for short paper)\\n\\n**C1 (Selective routing to deterministic computation)**: On ScienceWorld, deterministic simulation significantly outperforms pure LLM reasoning, with the primary mechanism being catastrophic failure prevention (the simulator as \\\"safety net\\\"). [**Pending plan-003 confirmation**]: Learned selective routing further outperforms unconditional simulation — the router learns WHICH steps need the safety net. (MVP oracle > det evidence: +10-17 points on 3/5 task types. If trained router ≤ always-det, C1 downgrades to \\\"outperforms pure LLM reasoning\\\" only.)\\n\\n**C2 (Explicit modular router)**: A lightweight explicit router (Qwen3-1.7B, ~1.7B params), trained via SFT on counterfactual trajectory labels, achieves effective per-step routing that is (a) interpretable — routing decisions can be analyzed per task category to reveal systematic LLM failure modes, (b) architecturally decoupled from the agent backbone, and (c) consistent across task categories sharing similar failure patterns.\\n\\n## Story Spine\\n\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. No method provides an explicit, modular router for selective invocation of ground-truth deterministic computation.\\n\\n- **Our framing**: We recast the \\\"when to simulate\\\" problem as safety-aware routing. Deterministic computation is not primarily a performance booster — it is a catastrophic failure prevention mechanism. A lightweight explicit router learns to detect high-risk states where LLM reasoning is likely to fail catastrophically, and routes those steps to deterministic computation for ground-truth verification. This \\\"router-as-safety-net\\\" framing explains why: (1) the gain is concentrated in death avoidance (+30-40 points from preventing -100 penalties), (2) selective routing beats unconditional simulation (not every step needs the safety net), and (3) the router's decisions are interpretable as a diagnostic of where LLMs systematically fail.\\n\\n- **Headline result template**: \\\"On ScienceWorld, SimGate achieves [X] score (vs CogRouter 84.6, ITP-R 62.58), reducing catastrophic failures by [Y]% compared to pure LLM reasoning, while using [Z]% fewer simulator invocations than always-simulate.\\\"\\n\\n## Paper Structure (4-page short paper)\\n\\n| Section | Pages | Content |\\n|---------|-------|---------|\\n| Abstract | 0.2 | Safety-aware routing framing, headline numbers |\\n| Introduction | 0.8 | Problem + gap + contribution (2 claims) |\\n| Method | 1.0 | 3-component framework: backbone + deterministic oracle + explicit router; counterfactual training pipeline (4-step); router architecture |\\n| Experiments | 1.5 | Main results table + explicit vs implicit ablation + routing pattern analysis figure |\\n| Conclusion | 0.3 | Summary + limitations + future (MATH, API routing) |\\n| References | ~0.5 | Not counted in 4-page limit |\\n\\n## Anticipated Reviewer Concerns & Mitigations\\n\\n1. **\\\"Novelty is incremental — just SFT a small model to classify\\\"**\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\n\\n2. **\\\"Only one benchmark (ScienceWorld)\\\"**\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\n\\n3. **\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\"**\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\n\\n4. **\\\"Death avoidance is trivial — just filter dangerous actions\\\"**\\n   - Mitigation: Always-deterministic (which filters every step) underperforms oracle routing by 10-17 points. The non-trivial part is SELECTIVE invocation — knowing which steps need the safety net. Routing pattern analysis shows the router learns meaningful state-dependent decisions.\\n\\n5. **\\\"DAgger gap — SFT on oracle labels under base policy may not transfer\\\"**\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension.\\n\\n## Venue Fit Risks\\n\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\n- Short paper format matches focused contribution scope\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\"Scope & Future Work\\\" paragraph\\n- Risk: \\\"Safety-aware\\\" framing may be perceived as overselling if death avoidance is the ONLY signal — need to check if positive guidance signal emerges in full trajectory collection (even small positive guidance would strengthen the story)\\n\\n## Key Differences from IDEA_BRIEF\\n\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\n2. **Framing shifted**: From \\\"general routing to deterministic computation\\\" to \\\"safety-aware routing\\\" based on MVP death avoidance finding.\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\n4. **\\\"ANY form\\\" softened**: Per Human Review Note #4, \\\"across multiple forms\\\" instead of \\\"ANY form\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\n\", \"total_chars\": 6510, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c8f95bc-81e2-4243-a197-3d3d648cc487",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "aab83ef4-6223-4f36-b1e6-d0d535aad224",
  "sourceToolAssistantUUID": "2c8f95bc-81e2-4243-a197-3d3d648cc487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T16:17:45.629Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01ATSWYk1wHGQNM5tTJBupMy`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aab83ef4-6223-4f36-b1e6-d0d535aad224",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsPDnNAr6GoFBNmkPM7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80ff09a2-0a2a-46be-91f9-80ab06907cf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELoHr7aM5KjgL7zqvvagiC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3366,
      "cache_read_input_tokens": 18125,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3366
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 18125,
          "cache_creation_input_tokens": 3366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3366,
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

_source line 22 · 2026-05-13T16:17:45.638Z_

<details><summary>↩ Tool result · `toolu_01ATSWYk1wHGQNM5tTJBupMy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ROADMAP.md\", \"content\": \"# simgate-modular-routing — Research Dashboard\\n\\n> 最后更新: 2026-05-13 15:37 UTC | 更新原因: Reviewer W1-W5 修订: GPU 单位改 RTX 5090, 2-way 优先, 信号预筛, 参数控制 ablation\\n\\n## 核心方向\\nSimGate: 显式轻量 router (Qwen3-1.7B) 学习 per-step 安全路由 — 检测 LLM 推理高风险状态，选择性调用确定性外部计算（环境模拟器）防止灾难性失败。详见 paper_framing.md。\\n\\n## 投稿目标\\nEMNLP 2026 ARR short paper (4 pages)，DDL: 2026-05-25（剩余 12 天）\\n\\n## 当前阶段\\n**Research Phase** — MVP PASS (D005)，Dream 模拟中\\n\\n## 当前进展\\n- MVP: DONE (PASS) — 4/5 task types det > internal 显著, 主信号 = death avoidance\\n- paper_framing.md: DONE — 2 Claims, safety-aware routing. C1 含待确认子项（selective > unconditional）\\n- experiment_plan.yaml: v2 (Reviewer W1-W5 修订) — 2-way 优先, 信号预筛, 参数控制 ablation\\n- Dream: RUNNING (dream_20260513T153257, full mode, ~15 min)\\n- melt/change-state: Reviewer 确认非重复，但共享 variations → 论文中合并为 \\\"state-change tasks\\\"\\n\\n## 近期任务\\n- [ ] Dream 完成 → 审阅审稿报告，确认/调整 framing\\n- [ ] Dream 通过后批准 plan-001a (信号预筛) + plan-007 (boil rerun) 双卡并行\\n- [ ] Agent 完成 gpu1-v3 registry 更新 (ANALYZING → DONE)\\n- [ ] plan-001a 完成 → 筛出 10-15 有信号 task types → 启动 plan-001b\\n- [ ] plan-001b 完成 → 启动 plan-002 (router SFT) + plan-004 (explicit vs implicit ablation)\\n\\n## GPU 预算\\n- 服务器: westb-13313, 2× RTX 5090 32GB (cuda:0, cuda:1)\\n- P0: ~72h | P1: ~25h | P2: ~25h | 总计: ~122h (RTX 5090 wall-clock hours)\\n- Critical path: 001a(10h) → 001b(25h) → 002(8h) → 003(15h) = ~2.5 天双卡并行\\n\\n## 时间线 (12 天, RTX 5090 双卡)\\n| 天数 | 任务 | GPU |\\n|------|------|-----|\\n| 1 | Dream 审阅 + plan-001a 信号预筛 + plan-007 boil rerun | 双卡 |\\n| 2-3 | plan-001b 全量 trajectory collection | 双卡满载 |\\n| 4 | plan-002 router SFT + plan-004 explicit/implicit ablation | 双卡 |\\n| 5-6 | plan-003 evaluation + plan-006 2/3-way ablation | 双卡 |\\n| 7 | plan-005 routing analysis + plan-008 router size (P1) | 单卡+分析 |\\n| 8-10 | Paper writing (Paper Agent) | 按需补实验 |\\n| 11-12 | Review + submit | — |\\n\\n## 关键风险\\n1. Novelty 天花板 — SFT small router 技术简单，需靠 empirical finding + analysis\\n2. C1 子项待确认 — trained router > always-det 尚无证据 (plan-003 验证)\\n3. ScienceWorld 单 benchmark — short paper 可接受\\n4. Death avoidance 唯一信号 — 全量 collection 可能发现正向引导信号\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-13 | Research phase plan revised per Reviewer W1-W5: 2- | — |\\n| D005 | 2026-05-13 | MVP Phase 1 判定 PASS — det > internal 在 ≥2/5 task t | mvp-p1-gpu0, mvp-p1-gpu0-vllm, mvp-p1-gpu1-v3 |\\n| D004 | 2026-05-13 | MVP 判定 primary metric 改为 always-deterministic vs a | — |\\n| D003 | 2026-05-13 | GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑 | mvp-p1-gpu0, mvp-p1-gpu1-vllm |\\n| D002 | 2026-05-13 | 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phas | — |\\n| D001 | 2026-05-13 | MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM | — |\\n\\n\", \"total_chars\": 2649, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80ff09a2-0a2a-46be-91f9-80ab06907cf0",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "15010dda-65db-4bfe-ae56-34b3cf09de30",
  "sourceToolAssistantUUID": "80ff09a2-0a2a-46be-91f9-80ab06907cf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T16:17:51.325Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016zeABHrJiePv9MHqx3zRLZ`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15010dda-65db-4bfe-ae56-34b3cf09de30",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsPXPXWa8N2NekR4vnz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8c0c915-3c2d-4a72-b672-bf0bd34963f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gZdCfprDkRdvp5vCGC2tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4019,
      "cache_read_input_tokens": 21491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4019,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 24 · 2026-05-13T16:17:51.343Z_

<details><summary>↩ Tool result · `toolu_016zeABHrJiePv9MHqx3zRLZ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8c0c915-3c2d-4a72-b672-bf0bd34963f5",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "aceb8910-4106-4783-bd60-daa320da59af",
  "sourceToolAssistantUUID": "b8c0c915-3c2d-4a72-b672-bf0bd34963f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T16:17:51.813Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LfHT4FjnDXuBuWL2WqfPD2`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aceb8910-4106-4783-bd60-daa320da59af",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsPXPXWa8N2NekR4vnz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28e359fd-fe33-42c2-bf7b-b5eedb21a49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gZdCfprDkRdvp5vCGC2tb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4019,
      "cache_read_input_tokens": 21491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4019,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 26 · 2026-05-13T16:17:51.823Z_

<details><summary>↩ Tool result · `toolu_01LfHT4FjnDXuBuWL2WqfPD2`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28e359fd-fe33-42c2-bf7b-b5eedb21a49f",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "ca771cbb-7775-4749-b10a-ebba61a32fc7",
  "sourceToolAssistantUUID": "28e359fd-fe33-42c2-bf7b-b5eedb21a49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T16:17:52.393Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LLuLC34YvdwFMK9hUFhn8L`</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca771cbb-7775-4749-b10a-ebba61a32fc7",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsPXPXWa8N2NekR4vnz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45c2a679-c112-4a7f-8dd9-5d0e3f5d598c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gZdCfprDkRdvp5vCGC2tb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4019,
      "cache_read_input_tokens": 21491,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 21491,
          "cache_creation_input_tokens": 4019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4019,
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

_source line 28 · 2026-05-13T16:17:52.403Z_

<details><summary>↩ Tool result · `toolu_01LLuLC34YvdwFMK9hUFhn8L`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'simgate-modular-routing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45c2a679-c112-4a7f-8dd9-5d0e3f5d598c",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "4c317bc1-f26b-4aae-82a7-53a88dd69d44",
  "sourceToolAssistantUUID": "45c2a679-c112-4a7f-8dd9-5d0e3f5d598c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-13T16:17:56.470Z_

Now let me look for the actual paper PDF or LaTeX source, and the review context YAML mentioned in the task.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c317bc1-f26b-4aae-82a7-53a88dd69d44",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQ2FcKTtzPYRuakSTY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6840028f-26d2-45a1-a88e-ca226bbab0eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSaRjaGTN85UtUVFhDUh7G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 25510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 556,
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

_source line 30 · 2026-05-13T16:17:57.947Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01YNRmAZRiWLVDmKFeyiVw9f`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6840028f-26d2-45a1-a88e-ca226bbab0eb",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQ2FcKTtzPYRuakSTY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08688e42-327c-4f62-b2fa-8a6caccb8fb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSaRjaGTN85UtUVFhDUh7G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 25510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 556,
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

_source line 31 · 2026-05-13T16:17:57.971Z_

<details><summary>↩ Tool result · `toolu_01YNRmAZRiWLVDmKFeyiVw9f`</summary>

```text
artifacts/dream_reports/dream_20260513T153257/best/paper.tex
artifacts/dream_reports/dream_20260513T153257/median/paper.tex
artifacts/dream_reports/dream_20260513T153257/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08688e42-327c-4f62-b2fa-8a6caccb8fb2",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "06911564-62d9-4067-9d2d-dc3b974e76aa",
  "sourceToolAssistantUUID": "08688e42-327c-4f62-b2fa-8a6caccb8fb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-13T16:17:58.420Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014ZWjKtnvNomdr8ExN6fnzE`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06911564-62d9-4067-9d2d-dc3b974e76aa",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQ2FcKTtzPYRuakSTY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54c98975-b20c-4c49-bd60-d7b677e1cca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSaRjaGTN85UtUVFhDUh7G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 25510,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 556,
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

_source line 33 · 2026-05-13T16:17:58.431Z_

<details><summary>↩ Tool result · `toolu_014ZWjKtnvNomdr8ExN6fnzE`</summary>

```text
experiment_plan.yaml
decisions.yaml
registry.yaml
artifacts/dream_reports/dream_20260513T153257/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T153257/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T153257/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260513T153257/best/review_context.yaml
artifacts/dream_reports/dream_20260513T153257/median/review_context.yaml
artifacts/dream_reports/dream_20260513T153257/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54c98975-b20c-4c49-bd60-d7b677e1cca9",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "5c526dfe-bbde-4b9e-b808-382f65260eb0",
  "sourceToolAssistantUUID": "54c98975-b20c-4c49-bd60-d7b677e1cca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T16:17:58.911Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QZL5vzJ4fqCLKuhjVbBSkV`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c526dfe-bbde-4b9e-b808-382f65260eb0",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQ2FcKTtzPYRuakSTY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "373159ca-322c-4fbc-af69-07def3e1e5f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSaRjaGTN85UtUVFhDUh7G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 25510,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 556
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 25510,
          "cache_creation_input_tokens": 556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 556,
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

_source line 35 · 2026-05-13T16:17:58.922Z_

<details><summary>↩ Tool result · `toolu_01QZL5vzJ4fqCLKuhjVbBSkV`</summary>

```text
artifacts/dream_reports/dream_20260513T153257/best/paper.pdf
artifacts/dream_reports/dream_20260513T153257/median/paper.pdf
artifacts/dream_reports/dream_20260513T153257/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "373159ca-322c-4fbc-af69-07def3e1e5f2",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "9f4c0e85-b966-4c39-9911-f805a2106e4c",
  "sourceToolAssistantUUID": "373159ca-322c-4fbc-af69-07def3e1e5f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-13T16:18:02.578Z_

Let me read the paper, the review context YAML, and the imagined experiments YAML. Based on the task summary mentioning specific numbers, I should determine which scenario (best/median/worst) to review. Let me check the review context to find the one matching the numbers in the prompt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f4c0e85-b966-4c39-9911-f805a2106e4c",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQW6B7MJZ4i5Ny43dW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac6f24ad-80ae-4f30-85f4-7219762da64b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uq2X76w6jugVVkQ8rGX89K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 26066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 658,
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

_source line 37 · 2026-05-13T16:18:02.997Z_

<details open><summary>🔧 Tool call — Read · `toolu_016PSG3SNC6rNhm1KvNoP3e3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac6f24ad-80ae-4f30-85f4-7219762da64b",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQW6B7MJZ4i5Ny43dW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e47129b4-a03a-4e96-906e-578fbf885a5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uq2X76w6jugVVkQ8rGX89K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 26066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 658,
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

### Tool result

_source line 38 · 2026-05-13T16:18:03.289Z_

<details><summary>↩ Tool result · `toolu_016PSG3SNC6rNhm1KvNoP3e3`</summary>

```text
1	narrative_guidance: '整体叙事从 "new SOTA via safety-aware routing" 转向 "first explicit
2	  study of when deterministic computation helps LLM agents, with controlled causal
3	  evidence"。 C1 不与 CogRouter 直接比 SOTA，改为强调 SimGate vs 自身 ablation baselines 的受控实验，headline
4	  为 "reduces catastrophic failures by ~50%"。 C2 explicit vs implicit 差距写成 "consistent
5	  but moderate advantage"，重心转向 interpretability/modularity 的定性价值。 routing pattern
6	  分析从 failure mode taxonomy 降为 phase-dependent routing trends。 补充 plan-006 (2-way
7	  vs 3-way) 增加实验密度弥补 headline number 不够突出的不足。
8	
9	  '
10	imagined_experiments:
11	- name: Mini Signal Detection (Pre-screening)
12	  plan_id: plan-001a
13	  description: '对 ~20 个 ScienceWorld task type 各跑 5 episodes，2-way (internal + deterministic)，
14	    筛选出 det > internal 的 task types 进入 plan-001b。
15	
16	    '
17	  expected_results:
18	    total_task_types_screened: 20
19	    signal_positive_task_types: 13
20	    strong_signal_types: 7
21	    moderate_signal_types: 4
22	    weak_signal_types: 2
23	    no_signal_types: 7
24	    strong_signal_list: boil, melt, change-state-of-matter, freeze, use-thermometer,
25	      mix-chemicals, react-acid-base
26	    moderate_signal_list: mix-paint, measure-melting-point, conduct-electricity, identify-life-stages
27	    weak_signal_list: grow-plant-basic, navigate-rooms
28	    no_signal_example: grow-plant-advanced, read-thermometer, find-animal, classify-living,
29	      ecology-food-web, identify-rocks, use-microscope
30	    mean_det_minus_internal_strong: 38.5
31	    mean_det_minus_internal_moderate: 18.2
32	    mean_det_minus_internal_weak: 6.3
33	    gpu_hours_actual: 9.5
34	  result_rationale: 'Median 档下 death avoidance 是主要增益来源但集中在 physics/chemistry tasks。
35	    涉及温度变化、相态转换、化学反应的 7 个 task type 展示强信号（det-internal ~35-45 分）， 因为 LLM 在多步物理推理中频繁
36	    hallucinate 状态导致 death (-100)，deterministic oracle 消除了这些 catastrophic failures。
37	    4 个 moderate signal tasks 有部分物理/化学子步骤但非全程依赖，增益在 10-25 分。 2 个 weak signal tasks
38	    动作空间简单、death 风险低，deterministic 的 safety-net 价值有限。 7 个 no-signal tasks（生态观察、分类、阅读类）几乎无
39	    death 惩罚，internal reasoning 本身足够， det invocation 反而引入不必要的 rigid execution，无法利用
40	    LLM 的灵活推理优势。 这个 13/20 的通过率说明 safety-aware routing 不是 universal solution，而是 domain-specific
41	    mechanism。
42	
43	    '
44	  tables:
45	  - name: 'Table: Signal Pre-screening Results (5 episodes per task type)'
46	    columns:
47	    - task_type
48	    - domain
49	    - internal_mean
50	    - det_mean
51	    - det_minus_internal
52	    - death_rate_internal
53	    - death_rate_det
54	    - signal
55	    rows:
56	    - - boil
57	      - physics
58	      - -48.2
59	      - -12.6
60	      - 35.6
61	      - 0.6
62	      - 0.1
63	      - strong
64	    - - melt
65	      - physics
66	      - -52.1
67	      - -11.8
68	      - 40.3
69	      - 0.65
70	      - 0.08
71	      - strong
72	    - - change-state
73	      - physics
74	      - -50.8
75	      - -10.4
76	      - 40.4
77	      - 0.62
78	      - 0.1
79	      - strong
80	    - - freeze
81	      - physics
82	      - -45.6
83	      - -8.2
84	      - 37.4
85	      - 0.58
86	      - 0.06
87	      - strong
88	    - - use-thermometer
89	      - physics
90	      - -38.4
91	      - -5.0
92	      - 33.4
93	      - 0.5
94	      - 0.08
95	      - strong
96	    - - mix-chemicals
97	      - chemistry
98	      - -55.2
99	      - -14.8
100	      - 40.4
101	      - 0.68
102	      - 0.12
103	      - strong
104	    - - react-acid-base
105	      - chemistry
106	      - -46.0
107	      - -7.5
108	      - 38.5
109	      - 0.55
110	      - 0.08
111	      - strong
112	    - - mix-paint
113	      - chemistry
114	      - -32.5
115	      - -14.3
116	      - 18.2
117	      - 0.35
118	      - 0.12
119	      - moderate
120	    - - measure-melting-point
121	      - physics
122	      - -28.0
123	      - -8.6
124	      - 19.4
125	      - 0.3
126	      - 0.1
127	      - moderate
128	    - - conduct-electricity
129	      - physics
130	      - -25.8
131	      - -10.2
132	      - 15.6
133	      - 0.28
134	      - 0.08
135	      - moderate
136	    - - identify-life-stages
137	      - biology
138	      - -22.4
139	      - -2.6
140	      - 19.8
141	      - 0.25
142	      - 0.06
143	      - moderate
144	    - - grow-plant-basic
145	      - biology
146	      - -15.2
147	      - -8.9
148	      - 6.3
149	      - 0.12
150	      - 0.04
151	      - weak
152	    - - navigate-rooms
153	      - spatial
154	      - -10.4
155	      - -4.1
156	      - 6.3
157	      - 0.08
158	      - 0.02
159	      - weak
160	    - - grow-plant-advanced
161	      - biology
162	      - -8.6
163	      - -9.2
164	      - -0.6
165	      - 0.06
166	      - 0.04
167	      - none
168	    - - read-thermometer
169	      - physics
170	      - -5.2
171	      - -4.8
172	      - 0.4
173	      - 0.02
174	      - 0.02
175	      - none
176	    - - find-animal
177	      - ecology
178	      - -12.0
179	      - -13.5
180	      - -1.5
181	      - 0.04
182	      - 0.06
183	      - none
184	    - - classify-living
185	      - biology
186	      - -6.8
187	      - -8.0
188	      - -1.2
189	      - 0.02
190	      - 0.04
191	      - none
192	    - - ecology-food-web
193	      - ecology
194	      - -18.5
195	      - -20.1
196	      - -1.6
197	      - 0.1
198	      - 0.12
199	      - none
200	    - - identify-rocks
201	      - geology
202	      - -8.0
203	      - -7.5
204	      - 0.5
205	      - 0.04
206	      - 0.02
207	      - none
208	    - - use-microscope
209	      - biology
210	      - -4.2
211	      - -5.0
212	      - -0.8
213	      - 0.02
214	      - 0.02
215	      - none
216	  figures_description:
217	  - 'Bar chart: det_minus_internal per task type, colored by domain (physics=blue,
218	    chemistry=green, biology=orange, ecology=red, spatial=gray), horizontal line at
219	    0. Clear visual separation: physics/chemistry tasks cluster above +30, biology/ecology
220	    near 0 or negative.'
221	  analysis: '13/20 task types 通过信号筛选（≥5 分 det>internal 差距），与 median 档 task_types_with_significant_gain
222	    8-12 的预期一致 （部分 moderate/weak signal 在 full 20-episode 评估中可能跌出显著性）。 Domain 分布清晰：physics
223	    5/5 全部有信号，chemistry 3/3 全部有信号，biology 2/5 有信号，ecology 0/2 无信号。 这直接支持 median 档的
224	    A1 判断——death avoidance 增益集中在 physics/chemistry tasks。 No-signal tasks 将排除出 plan-001b，节约
225	    ~35% GPU 时间。
226	
227	    '
228	- name: Full Counterfactual Trajectory Collection
229	  plan_id: plan-001b
230	  description: '对 plan-001a 筛出的 13 个 signal-positive task types 各跑 20 episodes， 2-way
231	    counterfactual collection (internal + deterministic)，max_steps=30， 记录每步最优 modality
232	    的 hindsight labels。
233	
234	    '
235	  expected_results:
236	    task_types_collected: 13
237	    episodes_per_task: 20
238	    total_episodes: 260
239	    total_steps_labeled: 6240
240	    label_distribution_deterministic_pct: 38.5
241	    label_distribution_internal_pct: 61.5
242	    label_agreement_strong_tasks_pct: 82.0
243	    label_agreement_weak_tasks_pct: 64.0
244	    noisy_label_rate_overall_pct: 18.5
245	    avg_steps_per_episode: 24.0
246	    gpu_hours_actual: 23.5
247	  result_rationale: 'Median 档下 counterfactual labels 泛化中等（A4），具体表现为： 强信号 tasks (physics/chemistry)
248	    的 label agreement ~82%——大多数步骤中 deterministic 和 internal 的优劣清晰， 因为 death/survival
249	    差异提供了 binary signal。 弱信号 tasks 的 label agreement 仅 ~64%——很多步骤两种 modality 表现相近（都不死也都没进展），
250	    hindsight labeling 分不出哪个更好，导致标签噪声大。 整体 38.5% 步骤 labeled as deterministic-preferred，说明不是每步都需要
251	    safety net， 支持 selective routing 的必要性。但这个比例意味着 router 要学会一个相当细粒度的 per-step 判断。
252	    标签噪声 ~18.5% 将直接限制 router accuracy 的上限（A4），是 median 档 router accuracy 65-75% 的根本原因。
253	
254	    '
255	  tables:
256	  - name: 'Table: Trajectory Collection Summary by Domain'
257	    columns:
258	    - domain
259	    - n_tasks
260	    - n_episodes
261	    - total_steps
262	    - pct_det_preferred
263	    - label_agreement_pct
264	    - avg_death_rate_internal
265	    rows:
266	    - - physics (strong)
267	      - 5
268	      - 100
269	      - 2450
270	      - 42.1
271	      - 84.5
272	      - 0.59
273	    - - chemistry (strong)
274	      - 2
275	      - 40
276	      - 960
277	      - 43.8
278	      - 79.0
279	      - 0.62
280	    - - physics (moderate)
281	      - 2
282	      - 40
283	      - 920
284	      - 33.2
285	      - 68.5
286	      - 0.29
287	    - - chemistry (moderate)
288	      - 1
289	      - 20
290	      - 480
291	      - 30.5
292	      - 72.0
293	      - 0.35
294	    - - biology (moderate)
295	      - 1
296	      - 20
297	      - 510
298	      - 28.0
299	      - 60.5
300	      - 0.25
301	    - - biology (weak)
302	      - 1
303	      - 20
304	      - 460
305	      - 22.4
306	      - 58.0
307	      - 0.12
308	    - - spatial (weak)
309	      - 1
310	      - 20
311	      - 460
312	      - 20.8
313	      - 55.0
314	      - 0.08
315	  figures_description:
316	  - 'Scatter plot: x=death_rate_internal, y=pct_det_preferred per task type. Strong
317	    positive correlation (r~0.85). 标注 task names. 直观展示 death avoidance 与 deterministic
318	    routing 需求的关联。'
319	  analysis: '~6240 个 labeled steps 为 router SFT 提供训练数据。标签质量的 domain-dependent 特征 预示了
320	    router 在不同 task domains 上性能将不均匀。强信号 tasks 提供高质量 labels (agreement>80%)， 弱信号 tasks
321	    的 labels 噪声高 (agreement<65%)，将直接反映在 plan-003 的 per-task-type breakdown 中。 det-preferred
322	    比例 38.5% 与 median 档 simulator_invocation_ratio 30-50% 一致。
323	
324	    '
325	- name: Router SFT Training
326	  plan_id: plan-002
327	  description: '在 plan-001b 的 counterfactual labels 上 fine-tune Qwen3-1.7B 做 2-way
328	    classification (internal vs deterministic)。Leave-one-out cross-validation by task
329	    type。
330	
331	    '
332	  expected_results:
333	    train_loss_final: 0.42
334	    val_accuracy_overall_pct: 71.2
335	    val_accuracy_strong_tasks_pct: 78.5
336	    val_accuracy_moderate_tasks_pct: 66.0
337	    val_accuracy_weak_tasks_pct: 58.3
338	    val_f1_deterministic: 0.68
339	    val_f1_internal: 0.74
340	    leave_one_out_accuracy_range:
341	    - 62.0
342	    - 76.0
343	    leave_one_out_mean_accuracy: 68.5
344	    best_epoch: 2
345	    convergence_epoch: 3
346	    gpu_hours_actual: 6.5
347	  result_rationale: 'Median 档 router accuracy 65-75% (A4)。整体 val accuracy 71.2% 符合此区间。
348	    强信号 tasks 的 labels 清晰（death/survival 二分），router 在这些 tasks 上学到了有效的 pattern， accuracy
349	    达 78.5%。弱信号 tasks 的标签噪声大，router accuracy 仅 58.3%——接近 random baseline (50%)。 Leave-one-out
350	    验证显示跨 task type 泛化中等（A4），range 62-76%： 留出 physics task 时其他 physics tasks 提供足够
351	    coverage，accuracy 高端 (~76%)； 留出 biology task 时几乎没有同 domain 训练数据，accuracy 低端 (~62%)。
352	    F1 score deterministic < internal 反映类别不平衡（38.5% vs 61.5%）和 deterministic labels
353	    更noisy。 Train loss 未过拟合（epoch 2-3 之间收敛），但 val accuracy 到 epoch 3 后不再提升， 说明瓶颈在标签质量而非模型容量。
354	
355	    '
356	  tables:
357	  - name: 'Table: Router Training Metrics'
358	    columns:
359	    - metric
360	    - epoch_1
361	    - epoch_2
362	    - epoch_3
363	    rows:
364	    - - train_loss
365	      - 0.58
366	      - 0.45
367	      - 0.42
368	    - - val_loss
369	      - 0.55
370	      - 0.48
371	      - 0.47
372	    - - val_accuracy (%)
373	      - 64.8
374	      - 70.5
375	      - 71.2
376	    - - val_f1_det
377	      - 0.6
378	      - 0.67
379	      - 0.68
380	    - - val_f1_int
381	      - 0.68
382	      - 0.73
383	      - 0.74
384	  - name: 'Table: Leave-One-Out Cross-Validation (selected task types)'
385	    columns:
386	    - held_out_task
387	    - domain
388	    - accuracy_on_held_out (%)
389	    - accuracy_on_rest (%)
390	    rows:
391	    - - boil
392	      - physics
393	      - 76.0
394	      - 71.8
395	    - - melt
396	      - physics
397	      - 74.5
398	      - 71.5
399	    - - mix-chemicals
400	      - chemistry
401	      - 72.0
402	      - 71.0
403	    - - mix-paint
404	      - chemistry
405	      - 67.5
406	      - 72.0
407	    - - identify-life-stages
408	      - biology
409	      - 62.0
410	      - 72.5
411	    - - grow-plant-basic
412	      - biology
413	      - 63.5
414	      - 72.0
415	  figures_description:
416	  - 'Training curves: x=steps, y=loss/accuracy. Train loss (solid) vs val loss (dashed).
417	    Val accuracy plateaus at epoch 2.5. 标注 label noise ceiling (~75%) as horizontal
418	    dotted line.'
419	  analysis: 'Router 训练收敛稳定，但 accuracy 受限于标签噪声上限。71.2% 的 val accuracy 是 median 档的中间值。
420	    Leave-one-out 结果确认跨 task type 泛化中等——同 domain 迁移较好，跨 domain 较差。 这个 router 的主要价值在于
421	    physics/chemistry tasks 上的可靠判断， 弱 tasks 上的 routing decisions 接近 random 但因为这些 tasks
422	    本身 death rate 低，影响有限。
423	
424	    '
425	- name: SimGate End-to-End Evaluation
426	  plan_id: plan-003
427	  description: 'Trained router + Qwen2.5-7B backbone 在 held-out episodes 上端到端评估。 对比
428	    always-internal, always-deterministic, oracle-routing, random-routing, confidence-threshold
429	    heuristic。
430	
431	    '
432	  expected_results:
433	    simgate_score_overall: 78.2
434	    always_internal_score: 56.8
435	    always_deterministic_score: 70.5
436	    oracle_routing_score: 81.2
437	    random_routing_score: 63.4
438	    confidence_threshold_score: 66.8
439	    simgate_minus_always_internal: 21.4
440	    simgate_minus_always_deterministic: 7.7
441	    oracle_minus_simgate: 3.0
442	    oracle_minus_always_det: 10.7
443	    catastrophic_failure_rate_internal_pct: 48.5
444	    catastrophic_failure_rate_simgate_pct: 22.3
445	    catastrophic_failure_rate_det_pct: 8.5
446	    catastrophic_failure_reduction_pct: 54.0
447	    simulator_invocation_ratio_pct: 41.2
448	    cogrouter_reported: 84.6
449	    itp_r_reported: 62.58
450	    simgate_minus_cogrouter: -6.4
451	    bootstrap_90ci_simgate:
452	    - 74.5
453	    - 81.8
454	    bootstrap_90ci_always_internal:
455	    - 52.0
456	    - 61.5
457	    bootstrap_90ci_always_det:
458	    - 66.2
459	    - 74.8
460	    task_types_with_significant_gain: 10
461	    gpu_hours_actual: 14.0
462	  result_rationale: 'Median 档 simgate_score_overall 72-84，取 78.2。未超过 CogRouter (84.6)
463	    但差距 6.4 分， 在 bootstrap CI 下两者 overlap（SimGate CI 上界 81.8 vs CogRouter 84.6），不能
464	    claim SOTA。 SimGate vs always-internal +21.4 分——核心 safety-net value，catastrophic
465	    failure 从 48.5% 降至 22.3%（降幅 54%）， 符合 median 档 catastrophic_failure_reduction_pct
466	    40-60%。 SimGate vs always-deterministic +7.7 分——selective routing 价值，说明并非所有步骤需要
467	    safety net， unconditional simulation 在低风险步骤引入了不必要的 rigid execution（LLM 在安全步骤上
468	    reasoning 更灵活）。 Oracle vs SimGate 仅 3.0 分——router 已捕获大部分可学习的 routing signal，剩余
469	    gap 来自弱 task types 的标签噪声。 Simulator invocation ratio 41.2%——router 在约 40% 步骤调用
470	    deterministic，远少于 always-det 的 100%， 说明 router 学到了 selective invocation pattern。
471	    对比 CogRouter 差距的原因：CogRouter 用 RL (CoPO) 在 trajectory 级别优化， SimGate 用 SFT per-step
472	    labels，且无 positive guidance signal (A6)——router 仅防死不指路。 10/13 task types 显著增益（physics
473	    5/5 + chemistry 3/3 + moderate 2/4）， 符合 median 档 task_types_with_significant_gain
474	    8-12。
475	
476	    '
477	  tables:
478	  - name: 'Table 1 (Main Results): SimGate vs Baselines on ScienceWorld'
479	    columns:
480	    - method
481	    - overall_score
482	    - 90% CI
483	    - catastrophic_failure_rate (%)
484	    - sim_invocation_ratio (%)
485	    - LLM_tokens (k)
486	    rows:
487	    - - Always-Internal
488	      - 56.8
489	      - '[52.0, 61.5]'
490	      - 48.5
491	      - 0
492	      - 385
493	    - - Always-Deterministic
494	      - 70.5
495	      - '[66.2, 74.8]'
496	      - 8.5
497	      - 100
498	      - 142
499	    - - Random Routing (p=0.4)
500	      - 63.4
501	      - '[58.8, 68.0]'
502	      - 30.2
503	      - 40.0
504	      - 248
505	    - - Confidence Threshold
506	      - 66.8
507	      - '[62.0, 71.5]'
508	      - 28.8
509	      - 35.5
510	      - 262
511	    - - SimGate (ours)
512	      - 78.2
513	      - '[74.5, 81.8]'
514	      - 22.3
515	      - 41.2
516	      - 240
517	    - - Oracle Routing
518	      - 81.2
519	      - '[77.8, 84.5]'
520	      - 12.0
521	      - 36.5
522	      - 255
523	    - - '---'
524	      - '---'
525	      - '---'
526	      - '---'
527	      - '---'
528	      - '---'
529	    - - CogRouter (reported)
530	      - 84.6
531	      - —
532	      - —
533	      - —
534	      - —
535	    - - ITP-R (reported)
536	      - 62.58
537	      - —
538	      - —
539	      - —
540	      - —
541	  - name: 'Table: Per-Task-Type Breakdown (SimGate vs Always-Internal)'
542	    columns:
543	    - task_type
544	    - domain
545	    - simgate_score
546	    - internal_score
547	    - delta
548	    - catastrophic_failure_reduction_pct
549	    - significant
550	    rows:
551	    - - boil
552	      - physics
553	      - 82.5
554	      - 52.0
555	      - 30.5
556	      - 62
557	      - 'yes'
558	    - - melt
559	      - physics
560	      - 85.0
561	      - 48.5
562	      - 36.5
563	      - 68
564	      - 'yes'
565	    - - change-state
566	      - physics
567	      - 84.2
568	      - 50.2
569	      - 34.0
570	      - 65
571	      - 'yes'
572	    - - freeze
573	      - physics
574	      - 80.8
575	      - 55.0
576	      - 25.8
577	      - 58
578	      - 'yes'
579	    - - use-thermometer
580	      - physics
581	      - 78.0
582	      - 60.5
583	      - 17.5
584	      - 52
585	      - 'yes'
586	    - - mix-chemicals
587	      - chemistry
588	      - 82.0
589	      - 46.8
590	      - 35.2
591	      - 70
592	      - 'yes'
593	    - - react-acid-base
594	      - chemistry
595	      - 80.5
596	      - 52.5
597	      - 28.0
598	      - 60
599	      - 'yes'
600	    - - mix-paint
601	      - chemistry
602	      - 76.2
603	      - 62.0
604	      - 14.2
605	      - 42
606	      - 'yes'
607	    - - measure-melting-point
608	      - physics
609	      - 74.5
610	      - 65.0
611	      - 9.5
612	      - 35
613	      - 'yes'
614	    - - conduct-electricity
615	      - physics
616	      - 72.0
617	      - 60.5
618	      - 11.5
619	      - 38
620	      - 'yes'
621	    - - identify-life-stages
622	      - biology
623	      - 68.5
624	      - 62.0
625	      - 6.5
626	      - 22
627	      - 'no'
628	    - - grow-plant-basic
629	      - biology
630	      - 65.0
631	      - 60.5
632	      - 4.5
633	      - 15
634	      - 'no'
635	    - - navigate-rooms
636	      - spatial
637	      - 62.8
638	      - 58.0
639	      - 4.8
640	      - 12
641	      - 'no'
642	  figures_description:
643	  - 'Grouped bar chart: SimGate vs Always-Internal vs Always-Det vs Oracle per task
644	    type, sorted by delta. Physics/chemistry tasks cluster left with large deltas,
645	    biology/spatial tasks cluster right with small deltas.'
646	  - 'Scatter plot: x=catastrophic_failure_rate_internal, y=SimGate delta. Strong positive
647	    correlation, 标注 r=0.91. 直接可视化 ''death avoidance is primary mechanism'' claim.'
648	  analysis: 'SimGate 78.2 低于 CogRouter 84.6 约 6 分。叙事不能 claim SOTA，但 controlled ablation
649	    提供了强因果证据： SimGate vs internal (+21.4)、vs det (+7.7)、vs random (+14.8)、vs heuristic
650	    (+11.4) 全部显著。 catastrophic failure reduction 54% 是强 headline number。 Per-task
651	    breakdown 清晰展示 death avoidance 是主要机制——physics/chemistry 的 delta 与 internal death
652	    rate 高度相关 (r=0.91)。 3 个弱 tasks (biology/spatial) 的 delta <7 且不显著，支持 A1 的 domain-specific
653	    判断。 SimGate 比 CogRouter 差的原因可归为：(1) SFT vs RL training，(2) 无 positive guidance
654	    signal。 Paper 叙事应改为 "first controlled study demonstrating causal role of deterministic
655	    computation in preventing catastrophic LLM failures"。
656	
657	    '
658	- name: Explicit vs Implicit Routing Ablation
659	  plan_id: plan-004
660	  description: '三条件对比：(a) 1.7B explicit router (SimGate), (b) 1.7B implicit router
661	    (SFT output [SIMULATE]), (c) 7B implicit routing (backbone tool-use prompt)。全部用相同
662	    counterfactual labels 训练。
663	
664	    '
665	  expected_results:
666	    explicit_1_7b_score: 78.2
667	    implicit_1_7b_score: 73.5
668	    implicit_7b_score: 74.8
669	    explicit_minus_implicit_1_7b: 4.7
670	    explicit_minus_implicit_7b: 3.4
671	    implicit_1_7b_catastrophic_failure_pct: 28.5
672	    implicit_7b_catastrophic_failure_pct: 26.2
673	    explicit_sim_invocation_ratio_pct: 41.2
674	    implicit_1_7b_sim_invocation_ratio_pct: 35.0
675	    implicit_7b_sim_invocation_ratio_pct: 38.5
676	    bootstrap_90ci_explicit:
677	    - 74.5
678	    - 81.8
679	    bootstrap_90ci_implicit_1_7b:
680	    - 69.2
681	    - 77.8
682	    bootstrap_90ci_implicit_7b:
683	    - 70.5
684	    - 79.0
685	    explicit_vs_implicit_1_7b_significant: true
686	    explicit_vs_implicit_7b_significant: marginal (p=0.08)
687	    gpu_hours_actual: 11.0
688	  result_rationale: 'Median 档 explicit_minus_implicit 3-8 分，statistical significance
689	    在部分条件下边缘 (A3)。 Explicit 1.7B vs implicit 1.7B: +4.7 分，parameter-matched comparison
690	    显著 (p<0.05)。 这说明 explicit modular router 架构本身有价值——将 routing decision 从 generation
691	    中解耦， 避免了 implicit routing 中 generation 任务和 routing 任务的 multi-task interference。
692	    Explicit 1.7B vs implicit 7B: +3.4 分，但 CI overlap 大 (p=0.08，边缘显著)。 7B implicit
693	    比 1.7B implicit 好 1.3 分——额外容量有 marginal 帮助但不足以弥补架构劣势。 Implicit routers 的 sim_invocation_ratio
694	    偏低 (35-38.5% vs explicit 41.2%)—— implicit routing 倾向于 under-invoke simulator（routing
695	    signal 在 generation logits 中被稀释）， 导致更多 catastrophic failures 未被拦截。 这个 "consistent
696	    but moderate advantage" 的结果支持 C2 的定性 claim（interpretability, modularity） 而非强 performance
697	    claim。Median 档下 C2 的重心应转向： explicit router 可独立替换、routing decisions 可分析，这些定性价值在
698	    3-5 分性能差距之上额外成立。
699	
700	    '
701	  tables:
702	  - name: 'Table: Explicit vs Implicit Routing Ablation'
703	    columns:
704	    - condition
705	    - params
706	    - overall_score
707	    - 90% CI
708	    - catastrophic_failure (%)
709	    - sim_invocation (%)
710	    - p vs explicit
711	    rows:
712	    - - Explicit Router (SimGate)
713	      - 1.7B
714	      - 78.2
715	      - '[74.5, 81.8]'
716	      - 22.3
717	      - 41.2
718	      - —
719	    - - Implicit Router (SFT)
720	      - 1.7B
721	      - 73.5
722	      - '[69.2, 77.8]'
723	      - 28.5
724	      - 35.0
725	      - '0.03'
726	    - - Implicit Routing (tool-use)
727	      - 7B
728	      - 74.8
729	      - '[70.5, 79.0]'
730	      - 26.2
731	      - 38.5
732	      - '0.08'
733	    - - Always-Internal
734	      - —
735	      - 56.8
736	      - '[52.0, 61.5]'
737	      - 48.5
738	      - 0
739	      - <0.001
740	  figures_description:
741	  - 'Box plot: three conditions'' score distributions across task types. Explicit
742	    has higher median and tighter IQR. Annotate p-values for pairwise comparisons.'
743	  analysis: 'Parameter-matched comparison (1.7B explicit vs 1.7B implicit, +4.7, p=0.03)
744	    是 C2 最干净的证据。 7B implicit 条件 (p=0.08) 可写为 "marginal significance"，但方向一致。 Median
745	    档叙事：explicit routing 是 "consistent but moderate advantage"， 主要价值在 architectural
746	    benefits (modularity, interpretability, independent replacement)， 用 4.7 分的定量证据
747	    + 定性分析支撑。不能写成 "large performance gap"。
748	
749	    '
750	- name: Per-Task Routing Pattern Analysis
751	  plan_id: plan-005
752	  description: '从 plan-003 输出分析 routing patterns：(a) 哪些 task types 触发 deterministic
753	    最多， (b) routing 集中在哪个 episode phase，(c) router-as-diagnostic-probe 识别 LLM failure
754	    modes。
755	
756	    '
757	  expected_results:
758	    n_routing_decisions_analyzed: 3900
759	    phase_early_det_pct: 25.0
760	    phase_mid_det_pct: 52.0
761	    phase_late_det_pct: 38.0
762	    physics_det_invocation_pct: 48.5
763	    chemistry_det_invocation_pct: 45.2
764	    biology_det_invocation_pct: 28.0
765	    spatial_det_invocation_pct: 22.0
766	    top_3_routing_triggers: state-change actions (heat/cool/mix), multi-step causal
767	      chains (>3 steps), post-failure recovery steps
768	    failure_mode_clusters_identified: 4
769	    cluster_clarity: moderate — 2 clear clusters, 2 diffuse
770	    gpu_hours_actual: 1.5
771	  result_rationale: 'Median 档 routing patterns 部分可解释 (A5)——能看到 phase-dependent 模式但
772	    failure taxonomy 不够清晰。 Phase-dependent pattern 清晰：mid-game (steps 8-20) routing
773	    最密集 (52%)， 因为这个阶段 agent 执行 state-changing actions (加热、冷却、混合) 最多， LLM 容易在多步物理推理中
774	    hallucinate 中间状态。 Early-game (steps 1-7) routing 较低 (25%)——agent 主要在 navigate
775	    和 gather objects，death 风险低。 Late-game (steps 21-30) routing 中等 (38%)——部分 tasks
776	    在此阶段做 final verification， 但也有很多 episodes 已经结束或 stuck。 4 个 failure mode clusters
777	    中： (1) "thermal state tracking failure" — 清晰，LLM 丢失温度/相态信息 (2) "chemical reaction
778	    sequencing" — 清晰，LLM 搞错反应步骤顺序 (3) "multi-step causal confusion" — 模糊，涵盖多种因果推理错误，不够
779	    specific (4) "environment state drift" — 模糊，router triggers 散布在各种步骤中 这是 median
780	    档 A5 的典型表现——有 pattern 但 failure taxonomy 不 clean。 Paper figure 只报告 phase-dependent
781	    routing trends，不宣称 comprehensive failure taxonomy。
782	
783	    '
784	  tables:
785	  - name: 'Table: Routing Decision Distribution by Episode Phase'
786	    columns:
787	    - phase
788	    - steps
789	    - total_decisions
790	    - det_routing_pct
791	    - avg_death_rate_if_internal
792	    rows:
793	    - - early
794	      - 1-7
795	      - 1200
796	      - 25.0
797	      - 0.12
798	    - - mid
799	      - 8-20
800	      - 1800
801	      - 52.0
802	      - 0.45
803	    - - late
804	      - 21-30
805	      - 900
806	      - 38.0
807	      - 0.28
808	  - name: 'Table: Failure Mode Clusters (Router-as-Diagnostic-Probe)'
809	    columns:
810	    - cluster
811	    - description
812	    - n_steps
813	    - pct_of_det_routing
814	    - clarity
815	    rows:
816	    - - 1
817	      - thermal state tracking failure
818	      - 420
819	      - 27.0
820	      - clear
821	    - - 2
822	      - chemical reaction sequencing error
823	      - 310
824	      - 20.0
825	      - clear
826	    - - 3
827	      - multi-step causal confusion
828	      - 480
829	      - 31.0
830	      - diffuse
831	    - - 4
832	      - environment state drift
833	      - 340
834	      - 22.0
835	      - diffuse
836	  figures_description:
837	  - 'Figure 1 (Paper): Routing heatmap — x=episode step (1-30), y=task type (sorted
838	    by domain). Color intensity = deterministic routing probability. Clear ''hot band''
839	    in mid-game steps for physics/chemistry tasks. Annotated with phase boundaries.'
840	  - 'Supplementary: t-SNE of router hidden states at deterministic-routing steps,
841	    colored by cluster ID. Clusters 1&2 tight, clusters 3&4 overlapping.'
842	  analysis: 'Phase-dependent routing trend 是 robust 的 finding，可以放 paper Figure 1。
843	    但 failure taxonomy 降级处理——从 "failure mode taxonomy" 改为 "we observe routing concentrates
844	    at state-change actions during mid-game phases, suggesting the router learns to
845	    detect high-risk physical reasoning steps"。不宣称 comprehensive failure analysis，只报告
846	    observable trends。 Mid-game concentration (52% of det routing) 直接对应 death avoidance
847	    mechanism—— 这正是 agent 执行 irreversible physical actions 的阶段。
848	
849	    '
850	- name: 2-Way vs 3-Way Routing Ablation
851	  plan_id: plan-006
852	  description: '补充 deep-internal modality 数据，比较 {internal, deterministic} vs {fast-internal,
853	    deep-internal, deterministic}。 测试 fast/deep internal 区分是否有额外价值。
854	
855	    '
856	  expected_results:
857	    two_way_score: 78.2
858	    three_way_score: 79.8
859	    delta: 1.6
860	    p_value: 0.22
861	    significant: false
862	    three_way_sim_invocation_pct: 39.5
863	    three_way_deep_internal_pct: 18.0
864	    three_way_fast_internal_pct: 42.5
865	    supplemental_data_collection_hours: 5.5
866	    router_retraining_hours: 3.0
867	    gpu_hours_actual: 9.5
868	  result_rationale: 'Median 档下 3-way 与 2-way 差距小且不显著 (+1.6, p=0.22)。 Fast/deep internal
869	    区分的理论价值在于：deep-internal 在需要更多 reasoning 但不需要 ground-truth 的步骤上 用 extended thinking
870	    提升质量。但实际效果有限，原因： (1) death avoidance 是主要增益来源 (A6)——一旦 deterministic 拦截了 catastrophic
871	    failures， 剩余步骤中 fast vs deep internal 的差异很小（LLM 在安全步骤上的表现差异不大）。 (2) 没有 positive
872	    guidance signal——deep internal 不能给出更好的 task guidance，只是"想更久"， 但在 deterministic
873	    已经处理了高风险步骤后，多想对安全步骤帮助有限。 (3) Router 从 2-class 升到 3-class 增加了 classification 难度，在
874	    median 档标签噪声下性能提升被抵消。 结论：2-way 足够，simplifies the story。Paper 中可以一句话报告 "binary
875	    routing (simulate-or-not) suffices; adding a third modality yields no significant
876	    improvement"。
877	
878	    '
879	  tables:
880	  - name: 'Table: 2-Way vs 3-Way Routing Comparison'
881	    columns:
882	    - routing_scheme
883	    - overall_score
884	    - 90% CI
885	    - sim_invocation (%)
886	    - p vs 2-way
887	    rows:
888	    - - 2-way {int, det}
889	      - 78.2
890	      - '[74.5, 81.8]'
891	      - 41.2
892	      - —
893	    - - 3-way {fast, deep, det}
894	      - 79.8
895	      - '[75.8, 83.5]'
896	      - 39.5
897	      - '0.22'
898	  figures_description:
899	  - 'Paired bar chart: 2-way vs 3-way per task type. Most bars nearly identical. 标注
900	    ns (not significant).'
901	  analysis: '3-way 不显著优于 2-way，simplifies the paper narrative。 可以 claim "binary routing
902	    decision (simulate or not) captures the essential routing signal"， 支持 safety-net
903	    framing——router 的核心工作是检测 high-risk steps，而非 fine-grained compute allocation。 在
904	    paper 中作为 ablation 一句话报告即可。这增加了实验密度而不改变结论。
905	
906	    '
907	- name: Boil Task Rerun with v3 Code
908	  plan_id: plan-007
909	  description: '用 v3 clean code（strict > tie-break, death filter only on internal）重跑
910	    boil task 20 episodes， 与 MVP 旧代码结果对比，确保分析一致性。
911	
912	    '
913	  expected_results:
914	    boil_v3_internal_mean: -46.5
915	    boil_v3_det_mean: -10.8
916	    boil_v3_oracle_mean: -3.2
917	    boil_v3_det_minus_internal: 35.7
918	    boil_v3_oracle_minus_det: 7.6
919	    boil_v3_bootstrap_90ci_det_minus_internal:
920	    - 22.0
921	    - 49.5
922	    boil_v3_death_rate_internal: 0.55
923	    boil_v3_death_rate_det: 0.08
924	    boil_mvp_internal_mean: -49.8
925	    boil_mvp_det_mean: -19.7
926	    delta_from_mvp_internal: 3.3
927	    delta_from_mvp_det: 8.9
928	    gpu_hours_actual: 2.5
929	  result_rationale: 'V3 code 的两个修正（strict > tie-break + death filter only on internal）对
930	    boil 的影响： (1) Strict > tie-break：减少了 deterministic 被选为 "best" 的 marginal cases，
931	    internal mean 略有提升 (-49.8 → -46.5) 因为部分原本 tie-break 判给 det 的 cases 现在留在 internal。
932	    (2) Death filter only on internal：det mean 显著提升 (-19.7 → -10.8) 因为 MVP 旧代码对 det
933	    也做了 death filter， 过滤掉了一些 det 原本能正确处理但被误判为 "death" 的 steps。 整体 det_minus_internal
934	    从 MVP 的 ~30 分变为 35.7 分，与 melt/change-state 的 ~40 分更接近， 说明 v3 code 修正消除了旧代码的 systematic
935	    bias。 Oracle mean 提升到 -3.2（接近 0），更符合预期——selective routing 应当接近 best-of-both。
936	
937	    '
938	  tables:
939	  - name: 'Table: Boil Task — v3 vs MVP Code Comparison'
940	    columns:
941	    - metric
942	    - MVP (old code)
943	    - v3 (clean code)
944	    - delta
945	    rows:
946	    - - internal_mean
947	      - -49.8
948	      - -46.5
949	      - '+3.3'
950	    - - det_mean
951	      - -19.7
952	      - -10.8
953	      - '+8.9'
954	    - - oracle_mean
955	      - -29.7
956	      - -3.2
957	      - '+26.5'
958	    - - det_minus_internal
959	      - 30.1
960	      - 35.7
961	      - '+5.6'
962	    - - death_rate_internal
963	      - ~0.6
964	      - 0.55
965	      - —
966	    - - death_rate_det
967	      - ~0.15
968	      - 0.08
969	      - —
970	  figures_description: []
971	  analysis: 'V3 code 修正提升了数据质量，特别是 oracle routing 从 -29.7 → -3.2 的大幅改善 说明旧 code 的
972	    death filter bug 严重低估了 selective routing 的价值。 修正后 boil 与其他 physics tasks (melt,
973	    change-state) 的 pattern 更一致， 全部 det_minus_internal 在 35-40 分范围。Paper 只使用 v3 数据。
974	
975	    '
976	- name: Router Size Ablation
977	  plan_id: plan-008
978	  description: '比较 Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B 作为 router 的效果。 测试 router
979	    capacity 敏感性。
980	
981	    '
982	  expected_results:
983	    qwen3_1_7b_score: 78.2
984	    qwen2_5_1_5b_score: 76.0
985	    qwen2_5_3b_score: 79.0
986	    qwen3_1_7b_router_accuracy_pct: 71.2
987	    qwen2_5_1_5b_router_accuracy_pct: 67.5
988	    qwen2_5_3b_router_accuracy_pct: 73.0
989	    delta_1_5b_vs_1_7b: -2.2
990	    delta_3b_vs_1_7b: 0.8
991	    significant_1_5b_vs_1_7b: false
992	    significant_3b_vs_1_7b: false
993	    inference_latency_1_5b_ms: 12
994	    inference_latency_1_7b_ms: 15
995	    inference_latency_3b_ms: 28
996	    gpu_hours_actual: 10.0
997	  result_rationale: 'Median 档下 router 性能受限于 label noise 而非 model capacity (plan-002
998	    分析已显示)。 1.5B vs 1.7B: -2.2 分但不显著 (p>0.1)——1.5B 容量略不足以 capture 一些 edge case routing
999	    patterns， 但差距在标签噪声范围内。Router accuracy 67.5% vs 71.2%，差距主要在 moderate/weak signal
1000	    tasks。 3B vs 1.7B: +0.8 分不显著——额外容量无法突破标签噪声上限。Router accuracy 73% vs 71.2%， marginal
1001	    improvement 被 end-to-end evaluation 的 variance 吞没。 这支持 "lightweight router suffices"
1002	    claim：1.5B-3B 范围内性能差异 <3 分， 瓶颈在训练数据质量而非 router capacity。 Inference latency 差异对
1003	    overall pipeline 影响 negligible（router inference 远快于 LLM backbone inference）。
1004	
1005	    '
1006	  tables:
1007	  - name: 'Table: Router Size Ablation'
1008	    columns:
1009	    - router
1010	    - params
1011	    - router_accuracy (%)
1012	    - e2e_score
1013	    - 90% CI
1014	    - latency (ms)
1015	    rows:
1016	    - - Qwen2.5-1.5B
1017	      - 1.5B
1018	      - 67.5
1019	      - 76.0
1020	      - '[71.8, 80.2]'
1021	      - 12
1022	    - - Qwen3-1.7B
1023	      - 1.7B
1024	      - 71.2
1025	      - 78.2
1026	      - '[74.5, 81.8]'
1027	      - 15
1028	    - - Qwen2.5-3B
1029	      - 3.0B
1030	      - 73.0
1031	      - 79.0
1032	      - '[75.2, 82.8]'
1033	      - 28
1034	  figures_description:
1035	  - 'Line plot: x=router params (log scale), y=e2e score. Near-flat line with error
1036	    bars overlapping. 标注 ''label noise ceiling'' as horizontal band.'
1037	  analysis: 'Router size ablation 支持两个 claims：(1) 小 router 足够 ("lightweight" in C2)，
1038	    (2) 瓶颈在标签质量——增加 router capacity 收益递减。 Paper 可报告 "routers from 1.5B to 3B parameters
1039	    achieve comparable performance (76-79), suggesting the routing task is learnable
1040	    at modest scale"。
1041	
1042	    '
1043	- name: MATH Track — Code Interpreter as Oracle
1044	  plan_id: plan-009
1045	  description: '500 道 Level 4-5 MATH 题，2-way routing: internal / code-interpreter。
1046	    测试 safety-aware routing 是否泛化到代码解释器场景。
1047	
1048	    '
1049	  expected_results:
1050	    simgate_math_accuracy_pct: 62.5
1051	    always_internal_accuracy_pct: 55.0
1052	    always_code_accuracy_pct: 58.8
1053	    oracle_routing_accuracy_pct: 68.0
1054	    simgate_minus_internal: 7.5
1055	    simgate_minus_always_code: 3.7
1056	    code_invocation_ratio_pct: 45.0
1057	    router_accuracy_math_pct: 63.0
1058	    catastrophic_error_reduction_pct: 28.0
1059	    gpu_hours_actual: 18.0
1060	  result_rationale: 'Median 档下 MATH track 显示中等泛化 (A4)。 Safety-aware routing 在 MATH
1061	    上的增益 (+7.5 vs internal) 远小于 ScienceWorld (+21.4)，原因： (1) MATH 没有 -100 death penalty——错误只是
1062	    0 分而非 catastrophic failure， safety-net 机制的 value proposition 减弱。 (2) Code interpreter
1063	    的优势在于 arithmetic/algebraic computation，不在于 "preventing catastrophic failures"。
1064	    LLM 在 MATH 上的错误模式更分散（reasoning errors, not just computation errors）， code interpreter
1065	    只能修正 computation errors 这一子集。 (3) Router 的 ScienceWorld labels 无法直接迁移，MATH 上需要
1066	    fresh labels， 但 label quality 更差——hindsight labeling 在 MATH 上不如 ScienceWorld 清晰（没有
1067	    death/survival 信号）。 Router accuracy 仅 63%（低于 ScienceWorld 71.2%），进一步说明 routing
1068	    signal 在 MATH 上更弱。 Catastrophic error reduction 仅 28%——定义 catastrophic 为 "算错导致
1069	    0 分"， code interpreter 能防止部分但远非全部。 这个结果仍有 paper 价值：证明 selective routing 原则泛化 (simgate
1070	    > always-code > always-internal)， 但 safety-aware framing 在无 catastrophic penalty
1071	    的环境中 weakens。可作为 discussion/future work 素材。
1072	
1073	    '
1074	  tables:
1075	  - name: 'Table: MATH Track Results (Level 4-5, n=500)'
1076	    columns:
1077	    - method
1078	    - accuracy (%)
1079	    - code_invocation (%)
1080	    - computation_error_rate (%)
1081	    rows:
1082	    - - Always-Internal
1083	      - 55.0
1084	      - 0
1085	      - 18.5
1086	    - - Always-Code
1087	      - 58.8
1088	      - 100
1089	      - 5.2
1090	    - - SimGate Router
1091	      - 62.5
1092	      - 45.0
1093	      - 10.8
1094	    - - Oracle Routing
1095	      - 68.0
1096	      - 38.0
1097	      - 3.0
1098	  figures_description:
1099	  - 'Bar chart: MATH results alongside ScienceWorld results (normalized). Clear visual:
1100	    ScienceWorld gains much larger. 标注 ''catastrophic penalty effect''.'
1101	  analysis: 'MATH 结果支持 selective > unconditional 的一般原则但效果弱得多。 如果 paper 长度允许，可以作为一段
1102	    "Generalization" 讨论； 如果 4-page 紧张，放 appendix 或 future work 一句话提及。 关键 takeaway："safety-aware
1103	    routing gains are proportional to the severity of catastrophic failure penalties"。
1104	
1105	    '
1106	- name: Cross-Task Transfer within ScienceWorld
1107	  plan_id: plan-010
1108	  description: 'Chemistry-only 训练 → physics 评估，physics-only 训练 → chemistry 评估。 测试
1109	    routing patterns 跨 domain 迁移性。
1110	
1111	    '
1112	  expected_results:
1113	    chem_train_chem_eval_score: 79.5
1114	    chem_train_phys_eval_score: 72.8
1115	    phys_train_phys_eval_score: 80.0
1116	    phys_train_chem_eval_score: 71.5
1117	    transfer_degradation_chem_to_phys: 7.2
1118	    transfer_degradation_phys_to_chem: 8.0
1119	    full_train_phys_eval_score: 82.5
1120	    full_train_chem_eval_score: 82.0
1121	    cross_domain_router_accuracy_pct: 62.5
1122	    same_domain_router_accuracy_pct: 76.0
1123	    gpu_hours_actual: 4.5
1124	  result_rationale: 'Median 档 routing pattern 迁移中等 (A4/A5)。 Chemistry → physics 迁移降幅
1125	    7.2 分，physics → chemistry 降幅 8.0 分—— 大约 40-50% 的 routing knowledge 可以跨 domain
1126	    迁移。 原因：death avoidance 的部分 pattern 是 domain-generic 的 （如 "state-change actions
1127	    需要 deterministic verification"）——这个 high-level 模式在两个 domain 共享。 但 domain-specific
1128	    failure patterns（如 chemistry 的 reaction sequencing vs physics 的 thermal tracking）
1129	    不迁移，导致 cross-domain router accuracy 从 76% 降到 62.5%。 这个结果在 paper 中可以作为一段 analysis："routing
1130	    patterns partially transfer across task domains sharing similar physical reasoning
1131	    requirements, but domain-specific failure modes require domain-specific training
1132	    data"。 不需要改变 main claims，但增加了对 router generalization 的理解。
1133	
1134	    '
1135	  tables:
1136	  - name: 'Table: Cross-Task Transfer Matrix'
1137	    columns:
1138	    - train_domain
1139	    - eval_domain
1140	    - score
1141	    - router_accuracy (%)
1142	    - vs full-train delta
1143	    rows:
1144	    - - chemistry
1145	      - chemistry
1146	      - 79.5
1147	      - 78.0
1148	      - '-2.5'
1149	    - - chemistry
1150	      - physics
1151	      - 72.8
1152	      - 62.5
1153	      - '-9.7'
1154	    - - physics
1155	      - physics
1156	      - 80.0
1157	      - 77.5
1158	      - '-2.5'
1159	    - - physics
1160	      - chemistry
1161	      - 71.5
1162	      - 61.0
1163	      - '-10.5'
1164	    - - all
1165	      - physics
1166	      - 82.5
1167	      - 78.5
1168	      - —
1169	    - - all
1170	      - chemistry
1171	      - 82.0
1172	      - 79.0
1173	      - —
1174	  figures_description:
1175	  - 'Transfer matrix heatmap: 2x2 grid showing score degradation. Diagonal (same-domain)
1176	    brighter, off-diagonal darker but not black — partial transfer.'
1177	  analysis: ~40-50% routing knowledge 跨 domain 迁移，与 median 档 A4 (counterfactual labels
1178	    泛化中等) 一致。 如果 4-page 紧张，这个实验可以仅在 results 最后一段用 2 句话概括。 重要 insight：routing 的 domain-generic
1179	    component 是 "detect state-change actions under uncertainty"， 这个 framing 比 task-specific
1180	    failure taxonomy 更 generalizable。
1181	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e47129b4-a03a-4e96-906e-578fbf885a5f",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "74a4b485-bfae-4e22-89f4-da7668562803",
  "sourceToolAssistantUUID": "e47129b4-a03a-4e96-906e-578fbf885a5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T16:18:03.973Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bawdmu9pGJzWRjj92TBfhP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74a4b485-bfae-4e22-89f4-da7668562803",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQW6B7MJZ4i5Ny43dW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e59c0f80-d76a-4967-b5ba-0ca21d43f611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uq2X76w6jugVVkQ8rGX89K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 26066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 658,
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

### Tool result

_source line 40 · 2026-05-13T16:18:03.980Z_

<details><summary>↩ Tool result · `toolu_01Bawdmu9pGJzWRjj92TBfhP`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{amsmath}
8	\usepackage{amssymb}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{hyperref}
12	\usepackage[numbers]{natbib}
13	
14	\title{SimGate: Safety-Aware Routing Between LLM Reasoning\\and Deterministic Computation for Agent Tasks}
15	
16	\author{Anonymous}
17	
18	\date{}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	LLM-based agents on rule-governed environments suffer catastrophic failures when they hallucinate physical state transitions---e.g., skipping temperature thresholds or misordering chemical reactions, incurring irreversible $-100$ penalties. We present \textbf{SimGate}, a modular framework that learns \emph{when} to route agent actions from LLM internal reasoning to a deterministic environment simulator. A lightweight explicit router (1.7B parameters), trained via supervised fine-tuning on counterfactual trajectory labels, makes per-step binary routing decisions. On ScienceWorld, SimGate scores 78.2 (90\% CI [74.5, 81.8]) compared to 56.8 for always-internal reasoning, reducing catastrophic failures by 54\% while invoking the simulator on only 41\% of steps. Controlled ablations show that (1) selective routing outperforms both unconditional simulation (+7.7) and heuristic baselines (+11.4), and (2) explicit routing provides a consistent advantage over implicit alternatives (+4.7, $p{=}0.03$ parameter-matched). Analysis of routing patterns reveals phase-dependent invocation concentrated at mid-episode state-change actions, offering interpretable diagnostics of systematic LLM failure modes.
25	\end{abstract}
26	
27	\section{Introduction}
28	
29	LLM agents deployed in rule-governed environments---scientific simulations, embodied tasks with physical constraints, mathematical problem-solving---must reason about state transitions that obey deterministic rules. When an LLM hallucinates an intermediate state (e.g., predicting that water boils at room temperature), the resulting action can trigger catastrophic, irreversible failures. On ScienceWorld \cite{wang2022scienceworld}, such failures carry $-100$ penalties that dominate episode scores.
30	
31	Existing approaches address this challenge incompletely. CogRouter \cite{cogrouter2025} achieves strong overall performance (84.6 on ScienceWorld) using RL-based trajectory optimization, but does not isolate the role of deterministic computation. ITP-R \cite{itpr2024} routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs.\ 84.6). ReTool \cite{retool2024} and AgentMath \cite{agentmath2024} learn when to invoke code interpreters but use implicit routing entangled with the generation backbone, precluding independent analysis of routing decisions.
32	
33	We identify a missing piece: no method provides an \emph{explicit, modular router} for selective invocation of ground-truth deterministic computation, nor isolates the causal mechanism by which such computation helps. We present SimGate, which recasts ``when to simulate'' as \textbf{safety-aware routing}. Our key insight is that deterministic computation primarily serves as a \emph{catastrophic failure prevention mechanism}: the simulator intercepts high-risk actions where LLM reasoning is likely to fail irreversibly, rather than providing positive task guidance across all steps.
34	
35	Our contributions are two controlled empirical findings:
36	
37	\noindent\textbf{C1}: Learned selective routing to deterministic computation reduces catastrophic failures by 54\% compared to pure LLM reasoning on ScienceWorld, with the gain concentrated in physics and chemistry tasks involving irreversible state changes. This is established through controlled comparison against five ablation baselines under identical conditions.
38	
39	\noindent\textbf{C2}: An explicit modular router (1.7B params, SFT-trained) provides a consistent advantage over implicit routing alternatives (+4.7 points parameter-matched, $p{=}0.03$), while enabling interpretable, per-step routing analysis and architectural decoupling from the agent backbone.
40	
41	\section{Method}
42	
43	\subsection{SimGate Framework}
44	
45	SimGate comprises three components: (1) an \textbf{LLM backbone} (Qwen2.5-7B) that generates candidate actions via internal reasoning, (2) a \textbf{deterministic oracle} (ScienceWorld environment simulator) that executes ground-truth state transitions at CPU-only cost, and (3) an \textbf{explicit router} (Qwen3-1.7B) that makes a binary per-step decision: route to internal reasoning or to the deterministic oracle.
46	
47	At each step $t$, given observation $o_t$ and action history $h_t$, the router produces $r_t = f_\theta(o_t, h_t) \in \{\texttt{internal}, \texttt{deterministic}\}$. If $r_t = \texttt{deterministic}$, the oracle executes the action with ground-truth physics; otherwise, the LLM backbone reasons internally. The router operates as an independent module with no gradient flow to the backbone, enabling independent replacement and analysis.
48	
49	\subsection{Counterfactual Training Pipeline}
50	
51	Router training proceeds in four steps:
52	
53	\paragraph{Step 1: Signal Pre-screening.} We screen 20 ScienceWorld task types (5 episodes each) under both modalities, identifying 13 task types where deterministic execution outperforms internal reasoning. Strong signal concentrates in physics (5/5 types) and chemistry (3/3 types), with the deterministic advantage averaging +38.5 points in strong-signal tasks (Table~\ref{tab:prescreening}).
54	
55	\paragraph{Step 2: Counterfactual Trajectory Collection.} For the 13 signal-positive task types, we collect 20 episodes each (260 total, 6{,}240 labeled steps) under both modalities with $\text{max\_steps}{=}30$. Each step receives a hindsight label indicating which modality yielded the better outcome. Labels are deterministic-preferred for 38.5\% of steps, with label agreement of 82\% on strong-signal tasks and 64\% on weak-signal tasks.
56	
57	\paragraph{Step 3: Router SFT.} We fine-tune Qwen3-1.7B on the counterfactual labels as a binary classification task. Training converges in 3 epochs with overall validation accuracy of 71.2\%, ranging from 78.5\% on strong-signal tasks to 58.3\% on weak-signal tasks. Leave-one-out cross-validation by task type yields 68.5\% mean accuracy (range 62--76\%), confirming moderate cross-task generalization.
58	
59	\paragraph{Step 4: End-to-End Evaluation.} The trained router is deployed with the Qwen2.5-7B backbone on held-out episodes, compared against ablation baselines.
60	
61	\section{Experiments}
62	
63	\subsection{Setup}
64	
65	We evaluate on 13 ScienceWorld task types spanning physics, chemistry, biology, and spatial reasoning domains. All comparisons use the same Qwen2.5-7B backbone with $\text{max\_steps}{=}30$. Confidence intervals are 90\% bootstrap. We report results using v3 codebase (strict tie-breaking, corrected death filter), validated through a boil-task rerun confirming consistency with other physics tasks (Table~\ref{tab:v3rerun}).
66	
67	\subsection{Main Results}
68	
69	Table~\ref{tab:main} presents SimGate against five controlled baselines. SimGate achieves 78.2, outperforming always-internal by +21.4 points and always-deterministic by +7.7 points. Catastrophic failure rate drops from 48.5\% (always-internal) to 22.3\% (SimGate), a 54\% reduction. SimGate uses the simulator on 41.2\% of steps---far less than the 100\% of always-deterministic---demonstrating that selective invocation outperforms blanket simulation.
70	
71	Random routing (63.4) and confidence-threshold heuristic (66.8) both fall well short of SimGate, confirming that learned routing captures signal beyond simple heuristics. Oracle routing (81.2) sets the upper bound; the 3.0-point gap to SimGate reflects residual label noise in weak-signal task types.
72	
73	For context, we note reported scores of CogRouter (84.6) and ITP-R (62.58) from prior work. SimGate does not exceed CogRouter, which employs RL-based trajectory optimization (CoPO). Our contribution is not a new state-of-the-art but controlled causal evidence for \emph{when and why} deterministic computation helps.
74	
75	\begin{table}[t]
76	\centering
77	\small
78	\begin{tabular}{@{}lcccc@{}}
79	\toprule
80	\textbf{Method} & \textbf{Score} & \textbf{90\% CI} & \textbf{CF\%} & \textbf{Sim\%} \\
81	\midrule
82	Always-Internal & 56.8 & [52.0, 61.5] & 48.5 & 0 \\
83	Always-Det. & 70.5 & [66.2, 74.8] & 8.5 & 100 \\
84	Random ($p{=}0.4$) & 63.4 & [58.8, 68.0] & 30.2 & 40.0 \\
85	Conf. Threshold & 66.8 & [62.0, 71.5] & 28.8 & 35.5 \\
86	\textbf{SimGate (ours)} & \textbf{78.2} & [74.5, 81.8] & \textbf{22.3} & 41.2 \\
87	Oracle Routing & 81.2 & [77.8, 84.5] & 12.0 & 36.5 \\
88	\midrule
89	CogRouter$^\dagger$ & 84.6 & --- & --- & --- \\
90	ITP-R$^\dagger$ & 62.58 & --- & --- & --- \\
91	\bottomrule
92	\end{tabular}
93	\caption{Main results on ScienceWorld (13 task types). CF\%: catastrophic failure rate. Sim\%: simulator invocation ratio. $^\dagger$Reported from prior work (different training regimes).}
94	\label{tab:main}
95	\end{table}
96	
97	\subsection{Per-Task Breakdown}
98	
99	Table~\ref{tab:pertask} shows SimGate gains are strongly domain-dependent. All 7 strong-signal tasks (physics and chemistry) show significant improvements ($\Delta > 14$), with catastrophic failure reduction of 52--70\%. The 3 weak-signal tasks (biology, spatial) show modest, non-significant gains ($\Delta < 7$), consistent with their low baseline death rates. The correlation between internal death rate and SimGate gain is $r{=}0.91$, directly supporting the safety-net mechanism: routing value is proportional to catastrophic failure risk.
100	
101	\begin{table}[t]
102	\centering
103	\small
104	\begin{tabular}{@{}llrrrc@{}}
105	\toprule
106	\textbf{Task} & \textbf{Dom.} & \textbf{SG} & \textbf{Int.} & $\boldsymbol{\Delta}$ & \textbf{Sig.} \\
107	\midrule
108	boil & phys & 82.5 & 52.0 & 30.5 & \checkmark \\
109	melt & phys & 85.0 & 48.5 & 36.5 & \checkmark \\
110	change-state & phys & 84.2 & 50.2 & 34.0 & \checkmark \\
111	freeze & phys & 80.8 & 55.0 & 25.8 & \checkmark \\
112	use-thermo. & phys & 78.0 & 60.5 & 17.5 & \checkmark \\
113	mix-chem. & chem & 82.0 & 46.8 & 35.2 & \checkmark \\
114	react-acid & chem & 80.5 & 52.5 & 28.0 & \checkmark \\
115	mix-paint & chem & 76.2 & 62.0 & 14.2 & \checkmark \\
116	meas.-m.p. & phys & 74.5 & 65.0 & 9.5 & \checkmark \\
117	conduct-elec. & phys & 72.0 & 60.5 & 11.5 & \checkmark \\
118	\midrule
119	id-life-stg. & bio & 68.5 & 62.0 & 6.5 & --- \\
120	grow-plant & bio & 65.0 & 60.5 & 4.5 & --- \\
121	nav-rooms & spat & 62.8 & 58.0 & 4.8 & --- \\
122	\bottomrule
123	\end{tabular}
124	\caption{Per-task breakdown: SimGate (SG) vs Always-Internal (Int.). $\Delta$: score difference. Sig.: statistically significant gain. Top 10 tasks show significant improvement; bottom 3 do not.}
125	\label{tab:pertask}
126	\end{table}
127	
128	\subsection{Explicit vs.\ Implicit Routing}
129	
130	Table~\ref{tab:explicit} compares three routing architectures trained on identical counterfactual labels. The parameter-matched comparison (1.7B explicit vs.\ 1.7B implicit SFT) yields a +4.7-point advantage for explicit routing ($p{=}0.03$). The 7B implicit tool-use baseline scores 74.8, still 3.4 points below the 1.7B explicit router ($p{=}0.08$, marginal).
131	
132	Implicit routers under-invoke the simulator (35.0--38.5\% vs.\ 41.2\%), suggesting that routing signal is diluted when entangled with generation. Beyond the quantitative gap, the explicit router offers architectural benefits: routing decisions are independently analyzable, the router can be replaced without retraining the backbone, and routing patterns serve as diagnostic probes of LLM failure modes (\S\ref{sec:routing_patterns}).
133	
134	\begin{table}[t]
135	\centering
136	\small
137	\begin{tabular}{@{}lccccc@{}}
138	\toprule
139	\textbf{Condition} & \textbf{Params} & \textbf{Score} & \textbf{CF\%} & \textbf{Sim\%} & $\boldsymbol{p}$ \\
140	\midrule
141	Explicit (SG) & 1.7B & 78.2 & 22.3 & 41.2 & --- \\
142	Implicit SFT & 1.7B & 73.5 & 28.5 & 35.0 & 0.03 \\
143	Implicit tool & 7B & 74.8 & 26.2 & 38.5 & 0.08 \\
144	Always-Int. & --- & 56.8 & 48.5 & 0 & $<$0.001 \\
145	\bottomrule
146	\end{tabular}
147	\caption{Explicit vs.\ implicit routing ablation. All conditions use identical training labels. $p$-values are vs.\ explicit SimGate.}
148	\label{tab:explicit}
149	\end{table}
150	
151	\subsection{Routing Pattern Analysis}
152	\label{sec:routing_patterns}
153	
154	Analysis of 3{,}900 routing decisions reveals phase-dependent invocation patterns. Deterministic routing concentrates in mid-episode steps 8--20 (52\% of deterministic invocations), where agents execute irreversible state-change actions (heating, cooling, mixing). Early-game steps 1--7 show lower invocation (25\%), corresponding to navigation and object gathering with low death risk. Late-game steps 21--30 show intermediate invocation (38\%), mixing verification steps with episodes that are already stuck or completed.
155	
156	This phase-dependent pattern aligns with domain-level routing rates: physics and chemistry tasks invoke the simulator most heavily (48.5\% and 45.2\% of steps respectively), while biology and spatial tasks invoke it less (28.0\% and 22.0\%). The router's top triggers are state-change actions, multi-step causal chains ($>$3 steps), and post-failure recovery steps. Two clear failure-mode clusters emerge---thermal state tracking failures and chemical reaction sequencing errors---though two additional clusters (multi-step causal confusion, environment state drift) are more diffuse.
157	
158	\begin{table}[t]
159	\centering
160	\small
161	\begin{tabular}{@{}lcrr@{}}
162	\toprule
163	\textbf{Phase} & \textbf{Steps} & \textbf{Det\%} & \textbf{Death if Int.} \\
164	\midrule
165	Early & 1--7 & 25.0 & 0.12 \\
166	Mid & 8--20 & 52.0 & 0.45 \\
167	Late & 21--30 & 38.0 & 0.28 \\
168	\bottomrule
169	\end{tabular}
170	\caption{Routing decisions by episode phase. Det\%: proportion routed to deterministic. Death if Int.: death rate under always-internal at that phase.}
171	\label{tab:phase}
172	\end{table}
173	
174	\subsection{Additional Ablations}
175	
176	\paragraph{2-Way vs.\ 3-Way Routing.} Adding a third modality (deep-internal with extended thinking) alongside fast-internal and deterministic yields 79.8 vs.\ 78.2 for 2-way ($\Delta{=}1.6$, $p{=}0.22$, not significant). Binary routing (simulate-or-not) captures the essential routing signal; finer-grained compute allocation provides no additional benefit when death avoidance is the primary mechanism.
177	
178	\begin{table}[t]
179	\centering
180	\small
181	\begin{tabular}{@{}lccc@{}}
182	\toprule
183	\textbf{Scheme} & \textbf{Score} & \textbf{90\% CI} & $\boldsymbol{p}$ \\
184	\midrule
185	2-way \{int, det\} & 78.2 & [74.5, 81.8] & --- \\
186	3-way \{fast, deep, det\} & 79.8 & [75.8, 83.5] & 0.22 \\
187	\bottomrule
188	\end{tabular}
189	\caption{2-way vs.\ 3-way routing. The third modality provides no significant improvement.}
190	\label{tab:2v3}
191	\end{table}
192	
193	\paragraph{Router Size.} Routers from 1.5B to 3.0B parameters achieve comparable end-to-end performance (76.0--79.0), with router accuracy ranging from 67.5\% to 73.0\% (Table~\ref{tab:routersize}). The performance plateau suggests the bottleneck is label quality rather than router capacity, supporting the use of lightweight routers.
194	
195	\begin{table}[t]
196	\centering
197	\small
198	\begin{tabular}{@{}lrrrr@{}}
199	\toprule
200	\textbf{Router} & \textbf{Acc.\%} & \textbf{Score} & \textbf{90\% CI} & \textbf{ms} \\
201	\midrule
202	Qwen2.5-1.5B & 67.5 & 76.0 & [71.8, 80.2] & 12 \\
203	Qwen3-1.7B & 71.2 & 78.2 & [74.5, 81.8] & 15 \\
204	Qwen2.5-3B & 73.0 & 79.0 & [75.2, 82.8] & 28 \\
205	\bottomrule
206	\end{tabular}
207	\caption{Router size ablation. All differences are non-significant.}
208	\label{tab:routersize}
209	\end{table}
210	
211	\paragraph{Cross-Domain Transfer.} Training on chemistry-only data and evaluating on physics yields 72.8 (vs.\ 82.5 with full training), a 9.7-point degradation; physics$\to$chemistry shows a similar 10.5-point drop. Cross-domain router accuracy falls from 76\% to 62.5\%. Approximately 40--50\% of routing knowledge transfers, suggesting a domain-generic component (``detect state-change actions under uncertainty'') shared across physics and chemistry tasks (Table~\ref{tab:transfer}).
212	
213	\begin{table}[t]
214	\centering
215	\small
216	\begin{tabular}{@{}llrrc@{}}
217	\toprule
218	\textbf{Train} & \textbf{Eval} & \textbf{Score} & \textbf{R-Acc\%} & $\boldsymbol{\Delta}$ \textbf{vs.\ full} \\
219	\midrule
220	chem & chem & 79.5 & 78.0 & $-2.5$ \\
221	chem & phys & 72.8 & 62.5 & $-9.7$ \\
222	phys & phys & 80.0 & 77.5 & $-2.5$ \\
223	phys & chem & 71.5 & 61.0 & $-10.5$ \\
224	all & phys & 82.5 & 78.5 & --- \\
225	all & chem & 82.0 & 79.0 & --- \\
226	\bottomrule
227	\end{tabular}
228	\caption{Cross-domain transfer. R-Acc: router accuracy.}
229	\label{tab:transfer}
230	\end{table}
231	
232	\paragraph{Code Validation.} A controlled rerun of the boil task with v3 code (strict tie-breaking, corrected death filter) confirms consistency with other physics tasks: internal mean $-46.5$, deterministic mean $-10.8$, $\Delta{=}35.7$ (Table~\ref{tab:v3rerun}). The v3 corrections eliminated systematic bias present in earlier code, particularly improving oracle routing from $-29.7$ to $-3.2$.
233	
234	\begin{table}[t]
235	\centering
236	\small
237	\begin{tabular}{@{}lrrr@{}}
238	\toprule
239	\textbf{Metric} & \textbf{MVP} & \textbf{v3} & $\boldsymbol{\Delta}$ \\
240	\midrule
241	internal mean & $-49.8$ & $-46.5$ & $+3.3$ \\
242	det mean & $-19.7$ & $-10.8$ & $+8.9$ \\
243	oracle mean & $-29.7$ & $-3.2$ & $+26.5$ \\
244	death rate (int) & 0.60 & 0.55 & --- \\
245	death rate (det) & 0.15 & 0.08 & --- \\
246	\bottomrule
247	\end{tabular}
248	\caption{Boil task: v3 vs.\ MVP code. All paper results use v3.}
249	\label{tab:v3rerun}
250	\end{table}
251	
252	\subsection{Generalization: MATH Track}
253	
254	To test whether safety-aware routing generalizes beyond ScienceWorld, we evaluate on 500 Level 4--5 MATH problems with 2-way routing between internal reasoning and a code interpreter. SimGate achieves 62.5\% accuracy vs.\ 55.0\% always-internal and 58.8\% always-code (Table~\ref{tab:math}). The gain is smaller (+7.5 vs.\ +21.4 on ScienceWorld), consistent with MATH lacking the catastrophic $-100$ penalty that makes safety-aware routing most valuable. Router accuracy on MATH is 63.0\% (vs.\ 71.2\% on ScienceWorld), reflecting weaker routing signal when errors are graduated rather than catastrophic.
255	
256	\begin{table}[t]
257	\centering
258	\small
259	\begin{tabular}{@{}lrrr@{}}
260	\toprule
261	\textbf{Method} & \textbf{Acc.\%} & \textbf{Code\%} & \textbf{CompErr\%} \\
262	\midrule
263	Always-Internal & 55.0 & 0 & 18.5 \\
264	Always-Code & 58.8 & 100 & 5.2 \\
265	SimGate Router & 62.5 & 45.0 & 10.8 \\
266	Oracle Routing & 68.0 & 38.0 & 3.0 \\
267	\bottomrule
268	\end{tabular}
269	\caption{MATH Track (Level 4--5, $n{=}500$). Code\%: code interpreter invocation ratio. CompErr\%: computation error rate.}
270	\label{tab:math}
271	\end{table}
272	
273	\begin{table}[t]
274	\centering
275	\small
276	\begin{tabular}{@{}llrrrrc@{}}
277	\toprule
278	\textbf{Task} & \textbf{Dom.} & \textbf{Int.} & \textbf{Det.} & $\boldsymbol{\Delta}$ & \textbf{DR-I} & \textbf{Sig.} \\
279	\midrule
280	boil & phys & $-48.2$ & $-12.6$ & 35.6 & 0.60 & S \\
281	melt & phys & $-52.1$ & $-11.8$ & 40.3 & 0.65 & S \\
282	chg-state & phys & $-50.8$ & $-10.4$ & 40.4 & 0.62 & S \\
283	freeze & phys & $-45.6$ & $-8.2$ & 37.4 & 0.58 & S \\
284	use-thm. & phys & $-38.4$ & $-5.0$ & 33.4 & 0.50 & S \\
285	mix-ch. & chem & $-55.2$ & $-14.8$ & 40.4 & 0.68 & S \\
286	react-ab & chem & $-46.0$ & $-7.5$ & 38.5 & 0.55 & S \\
287	\midrule
288	mix-pnt & chem & $-32.5$ & $-14.3$ & 18.2 & 0.35 & M \\
289	meas-mp & phys & $-28.0$ & $-8.6$ & 19.4 & 0.30 & M \\
290	cond-el & phys & $-25.8$ & $-10.2$ & 15.6 & 0.28 & M \\
291	id-life & bio & $-22.4$ & $-2.6$ & 19.8 & 0.25 & M \\
292	\midrule
293	grow-pl & bio & $-15.2$ & $-8.9$ & 6.3 & 0.12 & W \\
294	nav-rm & spat & $-10.4$ & $-4.1$ & 6.3 & 0.08 & W \\
295	\bottomrule
296	\end{tabular}
297	\caption{Signal pre-screening (5 episodes/type). Int./Det.: mean score under each modality. DR-I: death rate under internal. Signal: S=strong, M=moderate, W=weak.}
298	\label{tab:prescreening}
299	\end{table}
300	
301	\section{Conclusion}
302	
303	We presented SimGate, a modular safety-aware routing framework that learns when to invoke deterministic computation for LLM agent tasks. Our controlled experiments provide causal evidence that selective routing reduces catastrophic failures by 54\% on ScienceWorld, with gains concentrated in physics and chemistry tasks where irreversible state changes dominate. An explicit router offers consistent advantages over implicit alternatives while enabling interpretable routing analysis.
304	
305	\paragraph{Limitations.} SimGate does not exceed CogRouter's 84.6 score, primarily because our SFT router lacks positive guidance signal---it prevents failures but does not steer toward better strategies. The router's 71.2\% accuracy is bounded by counterfactual label noise (18.5\% noisy labels). Evaluation is limited to ScienceWorld and a preliminary MATH extension; broader benchmarks (ALFWorld, WebArena) remain future work.
306	
307	\paragraph{Future Work.} DAgger-style iterative relabeling could reduce label noise. Combining safety-aware routing with RL-based trajectory optimization (as in CogRouter) is a natural extension. The routing framework generalizes to any setting with access to deterministic oracles---API validators, formal verification tools, constraint solvers---where selective invocation can prevent catastrophic outcomes.
308	
309	\begin{thebibliography}{6}
310	
311	\bibitem{wang2022scienceworld}
312	R.~Wang, P.~Jansen, M.-A. C\^{o}t\'{e}, and P.~Ammanabrolu.
313	ScienceWorld: Is your agent smarter than a 5th grader?
314	In \emph{Proc. EMNLP}, 2022.
315	
316	\bibitem{cogrouter2025}
317	CogRouter: Cognitive routing for LLM agents with cooperative policy optimization.
318	\emph{arXiv preprint}, 2025.
319	
320	\bibitem{itpr2024}
321	ITP-R: Imagination-augmented planning with LLM world models.
322	\emph{arXiv preprint}, 2024.
323	
324	\bibitem{retool2024}
325	ReTool: Reinforcement learning for strategic tool use in LLMs.
326	\emph{arXiv preprint}, 2024.
327	
328	\bibitem{agentmath2024}
329	AgentMath: Agent-based mathematical reasoning with tool integration.
330	\emph{arXiv preprint}, 2024.
331	
332	\bibitem{ross2011dagger}
333	S.~Ross, G.~Gordon, and D.~Bagnell.
334	A reduction of imitation learning and structured prediction to no-regret online learning.
335	In \emph{Proc. AISTATS}, 2011.
336	
337	\end{thebibliography}
338	
339	\end{document}
340	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e59c0f80-d76a-4967-b5ba-0ca21d43f611",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "44a1b0dd-408f-4ad6-9fae-9c8392755836",
  "sourceToolAssistantUUID": "e59c0f80-d76a-4967-b5ba-0ca21d43f611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T16:18:04.557Z_

<details open><summary>🔧 Tool call — Read · `toolu_012vqheUD5Jm3tosDfjLFSt6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44a1b0dd-408f-4ad6-9fae-9c8392755836",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQW6B7MJZ4i5Ny43dW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b280bfc9-997c-4866-82e0-6f005a324132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uq2X76w6jugVVkQ8rGX89K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 26066,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 26066,
          "cache_creation_input_tokens": 658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 658,
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

_source line 42 · 2026-05-13T16:18:04.879Z_

<details><summary>↩ Tool result · `toolu_012vqheUD5Jm3tosDfjLFSt6`</summary>

```text
1	tier: median
2	narrative_guidance: '整体叙事从 "new SOTA via safety-aware routing" 转向 "first explicit
3	  study of when deterministic computation helps LLM agents, with controlled causal
4	  evidence"。 C1 不与 CogRouter 直接比 SOTA，改为强调 SimGate vs 自身 ablation baselines 的受控实验，headline
5	  为 "reduces catastrophic failures by ~50%"。 C2 explicit vs implicit 差距写成 "consistent
6	  but moderate advantage"，重心转向 interpretability/modularity 的定性价值。 routing pattern
7	  分析从 failure mode taxonomy 降为 phase-dependent routing trends。 补充 plan-006 (2-way
8	  vs 3-way) 增加实验密度弥补 headline number 不够突出的不足。
9	
10	  '
11	imagined_experiments:
12	- name: Mini Signal Detection (Pre-screening)
13	  plan_id: plan-001a
14	  description: '对 ~20 个 ScienceWorld task type 各跑 5 episodes，2-way (internal + deterministic)，
15	    筛选出 det > internal 的 task types 进入 plan-001b。
16	
17	    '
18	  expected_results:
19	    total_task_types_screened: 20
20	    signal_positive_task_types: 13
21	    strong_signal_types: 7
22	    moderate_signal_types: 4
23	    weak_signal_types: 2
24	    no_signal_types: 7
25	    strong_signal_list: boil, melt, change-state-of-matter, freeze, use-thermometer,
26	      mix-chemicals, react-acid-base
27	    moderate_signal_list: mix-paint, measure-melting-point, conduct-electricity, identify-life-stages
28	    weak_signal_list: grow-plant-basic, navigate-rooms
29	    no_signal_example: grow-plant-advanced, read-thermometer, find-animal, classify-living,
30	      ecology-food-web, identify-rocks, use-microscope
31	    mean_det_minus_internal_strong: 38.5
32	    mean_det_minus_internal_moderate: 18.2
33	    mean_det_minus_internal_weak: 6.3
34	    gpu_hours_actual: 9.5
35	  result_rationale: 'Median 档下 death avoidance 是主要增益来源但集中在 physics/chemistry tasks。
36	    涉及温度变化、相态转换、化学反应的 7 个 task type 展示强信号（det-internal ~35-45 分）， 因为 LLM 在多步物理推理中频繁
37	    hallucinate 状态导致 death (-100)，deterministic oracle 消除了这些 catastrophic failures。
38	    4 个 moderate signal tasks 有部分物理/化学子步骤但非全程依赖，增益在 10-25 分。 2 个 weak signal tasks
39	    动作空间简单、death 风险低，deterministic 的 safety-net 价值有限。 7 个 no-signal tasks（生态观察、分类、阅读类）几乎无
40	    death 惩罚，internal reasoning 本身足够， det invocation 反而引入不必要的 rigid execution，无法利用
41	    LLM 的灵活推理优势。 这个 13/20 的通过率说明 safety-aware routing 不是 universal solution，而是 domain-specific
42	    mechanism。
43	
44	    '
45	  tables:
46	  - name: 'Table: Signal Pre-screening Results (5 episodes per task type)'
47	    columns:
48	    - task_type
49	    - domain
50	    - internal_mean
51	    - det_mean
52	    - det_minus_internal
53	    - death_rate_internal
54	    - death_rate_det
55	    - signal
56	    rows:
57	    - - boil
58	      - physics
59	      - -48.2
60	      - -12.6
61	      - 35.6
62	      - 0.6
63	      - 0.1
64	      - strong
65	    - - melt
66	      - physics
67	      - -52.1
68	      - -11.8
69	      - 40.3
70	      - 0.65
71	      - 0.08
72	      - strong
73	    - - change-state
74	      - physics
75	      - -50.8
76	      - -10.4
77	      - 40.4
78	      - 0.62
79	      - 0.1
80	      - strong
81	    - - freeze
82	      - physics
83	      - -45.6
84	      - -8.2
85	      - 37.4
86	      - 0.58
87	      - 0.06
88	      - strong
89	    - - use-thermometer
90	      - physics
91	      - -38.4
92	      - -5.0
93	      - 33.4
94	      - 0.5
95	      - 0.08
96	      - strong
97	    - - mix-chemicals
98	      - chemistry
99	      - -55.2
100	      - -14.8
101	      - 40.4
102	      - 0.68
103	      - 0.12
104	      - strong
105	    - - react-acid-base
106	      - chemistry
107	      - -46.0
108	      - -7.5
109	      - 38.5
110	      - 0.55
111	      - 0.08
112	      - strong
113	    - - mix-paint
114	      - chemistry
115	      - -32.5
116	      - -14.3
117	      - 18.2
118	      - 0.35
119	      - 0.12
120	      - moderate
121	    - - measure-melting-point
122	      - physics
123	      - -28.0
124	      - -8.6
125	      - 19.4
126	      - 0.3
127	      - 0.1
128	      - moderate
129	    - - conduct-electricity
130	      - physics
131	      - -25.8
132	      - -10.2
133	      - 15.6
134	      - 0.28
135	      - 0.08
136	      - moderate
137	    - - identify-life-stages
138	      - biology
139	      - -22.4
140	      - -2.6
141	      - 19.8
142	      - 0.25
143	      - 0.06
144	      - moderate
145	    - - grow-plant-basic
146	      - biology
147	      - -15.2
148	      - -8.9
149	      - 6.3
150	      - 0.12
151	      - 0.04
152	      - weak
153	    - - navigate-rooms
154	      - spatial
155	      - -10.4
156	      - -4.1
157	      - 6.3
158	      - 0.08
159	      - 0.02
160	      - weak
161	    - - grow-plant-advanced
162	      - biology
163	      - -8.6
164	      - -9.2
165	      - -0.6
166	      - 0.06
167	      - 0.04
168	      - none
169	    - - read-thermometer
170	      - physics
171	      - -5.2
172	      - -4.8
173	      - 0.4
174	      - 0.02
175	      - 0.02
176	      - none
177	    - - find-animal
178	      - ecology
179	      - -12.0
180	      - -13.5
181	      - -1.5
182	      - 0.04
183	      - 0.06
184	      - none
185	    - - classify-living
186	      - biology
187	      - -6.8
188	      - -8.0
189	      - -1.2
190	      - 0.02
191	      - 0.04
192	      - none
193	    - - ecology-food-web
194	      - ecology
195	      - -18.5
196	      - -20.1
197	      - -1.6
198	      - 0.1
199	      - 0.12
200	      - none
201	    - - identify-rocks
202	      - geology
203	      - -8.0
204	      - -7.5
205	      - 0.5
206	      - 0.04
207	      - 0.02
208	      - none
209	    - - use-microscope
210	      - biology
211	      - -4.2
212	      - -5.0
213	      - -0.8
214	      - 0.02
215	      - 0.02
216	      - none
217	  figures_description:
218	  - 'Bar chart: det_minus_internal per task type, colored by domain (physics=blue,
219	    chemistry=green, biology=orange, ecology=red, spatial=gray), horizontal line at
220	    0. Clear visual separation: physics/chemistry tasks cluster above +30, biology/ecology
221	    near 0 or negative.'
222	  analysis: '13/20 task types 通过信号筛选（≥5 分 det>internal 差距），与 median 档 task_types_with_significant_gain
223	    8-12 的预期一致 （部分 moderate/weak signal 在 full 20-episode 评估中可能跌出显著性）。 Domain 分布清晰：physics
224	    5/5 全部有信号，chemistry 3/3 全部有信号，biology 2/5 有信号，ecology 0/2 无信号。 这直接支持 median 档的
225	    A1 判断——death avoidance 增益集中在 physics/chemistry tasks。 No-signal tasks 将排除出 plan-001b，节约
226	    ~35% GPU 时间。
227	
228	    '
229	- name: Full Counterfactual Trajectory Collection
230	  plan_id: plan-001b
231	  description: '对 plan-001a 筛出的 13 个 signal-positive task types 各跑 20 episodes， 2-way
232	    counterfactual collection (internal + deterministic)，max_steps=30， 记录每步最优 modality
233	    的 hindsight labels。
234	
235	    '
236	  expected_results:
237	    task_types_collected: 13
238	    episodes_per_task: 20
239	    total_episodes: 260
240	    total_steps_labeled: 6240
241	    label_distribution_deterministic_pct: 38.5
242	    label_distribution_internal_pct: 61.5
243	    label_agreement_strong_tasks_pct: 82.0
244	    label_agreement_weak_tasks_pct: 64.0
245	    noisy_label_rate_overall_pct: 18.5
246	    avg_steps_per_episode: 24.0
247	    gpu_hours_actual: 23.5
248	  result_rationale: 'Median 档下 counterfactual labels 泛化中等（A4），具体表现为： 强信号 tasks (physics/chemistry)
249	    的 label agreement ~82%——大多数步骤中 deterministic 和 internal 的优劣清晰， 因为 death/survival
250	    差异提供了 binary signal。 弱信号 tasks 的 label agreement 仅 ~64%——很多步骤两种 modality 表现相近（都不死也都没进展），
251	    hindsight labeling 分不出哪个更好，导致标签噪声大。 整体 38.5% 步骤 labeled as deterministic-preferred，说明不是每步都需要
252	    safety net， 支持 selective routing 的必要性。但这个比例意味着 router 要学会一个相当细粒度的 per-step 判断。
253	    标签噪声 ~18.5% 将直接限制 router accuracy 的上限（A4），是 median 档 router accuracy 65-75% 的根本原因。
254	
255	    '
256	  tables:
257	  - name: 'Table: Trajectory Collection Summary by Domain'
258	    columns:
259	    - domain
260	    - n_tasks
261	    - n_episodes
262	    - total_steps
263	    - pct_det_preferred
264	    - label_agreement_pct
265	    - avg_death_rate_internal
266	    rows:
267	    - - physics (strong)
268	      - 5
269	      - 100
270	      - 2450
271	      - 42.1
272	      - 84.5
273	      - 0.59
274	    - - chemistry (strong)
275	      - 2
276	      - 40
277	      - 960
278	      - 43.8
279	      - 79.0
280	      - 0.62
281	    - - physics (moderate)
282	      - 2
283	      - 40
284	      - 920
285	      - 33.2
286	      - 68.5
287	      - 0.29
288	    - - chemistry (moderate)
289	      - 1
290	      - 20
291	      - 480
292	      - 30.5
293	      - 72.0
294	      - 0.35
295	    - - biology (moderate)
296	      - 1
297	      - 20
298	      - 510
299	      - 28.0
300	      - 60.5
301	      - 0.25
302	    - - biology (weak)
303	      - 1
304	      - 20
305	      - 460
306	      - 22.4
307	      - 58.0
308	      - 0.12
309	    - - spatial (weak)
310	      - 1
311	      - 20
312	      - 460
313	      - 20.8
314	      - 55.0
315	      - 0.08
316	  figures_description:
317	  - 'Scatter plot: x=death_rate_internal, y=pct_det_preferred per task type. Strong
318	    positive correlation (r~0.85). 标注 task names. 直观展示 death avoidance 与 deterministic
319	    routing 需求的关联。'
320	  analysis: '~6240 个 labeled steps 为 router SFT 提供训练数据。标签质量的 domain-dependent 特征 预示了
321	    router 在不同 task domains 上性能将不均匀。强信号 tasks 提供高质量 labels (agreement>80%)， 弱信号 tasks
322	    的 labels 噪声高 (agreement<65%)，将直接反映在 plan-003 的 per-task-type breakdown 中。 det-preferred
323	    比例 38.5% 与 median 档 simulator_invocation_ratio 30-50% 一致。
324	
325	    '
326	- name: Router SFT Training
327	  plan_id: plan-002
328	  description: '在 plan-001b 的 counterfactual labels 上 fine-tune Qwen3-1.7B 做 2-way
329	    classification (internal vs deterministic)。Leave-one-out cross-validation by task
330	    type。
331	
332	    '
333	  expected_results:
334	    train_loss_final: 0.42
335	    val_accuracy_overall_pct: 71.2
336	    val_accuracy_strong_tasks_pct: 78.5
337	    val_accuracy_moderate_tasks_pct: 66.0
338	    val_accuracy_weak_tasks_pct: 58.3
339	    val_f1_deterministic: 0.68
340	    val_f1_internal: 0.74
341	    leave_one_out_accuracy_range:
342	    - 62.0
343	    - 76.0
344	    leave_one_out_mean_accuracy: 68.5
345	    best_epoch: 2
346	    convergence_epoch: 3
347	    gpu_hours_actual: 6.5
348	  result_rationale: 'Median 档 router accuracy 65-75% (A4)。整体 val accuracy 71.2% 符合此区间。
349	    强信号 tasks 的 labels 清晰（death/survival 二分），router 在这些 tasks 上学到了有效的 pattern， accuracy
350	    达 78.5%。弱信号 tasks 的标签噪声大，router accuracy 仅 58.3%——接近 random baseline (50%)。 Leave-one-out
351	    验证显示跨 task type 泛化中等（A4），range 62-76%： 留出 physics task 时其他 physics tasks 提供足够
352	    coverage，accuracy 高端 (~76%)； 留出 biology task 时几乎没有同 domain 训练数据，accuracy 低端 (~62%)。
353	    F1 score deterministic < internal 反映类别不平衡（38.5% vs 61.5%）和 deterministic labels
354	    更noisy。 Train loss 未过拟合（epoch 2-3 之间收敛），但 val accuracy 到 epoch 3 后不再提升， 说明瓶颈在标签质量而非模型容量。
355	
356	    '
357	  tables:
358	  - name: 'Table: Router Training Metrics'
359	    columns:
360	    - metric
361	    - epoch_1
362	    - epoch_2
363	    - epoch_3
364	    rows:
365	    - - train_loss
366	      - 0.58
367	      - 0.45
368	      - 0.42
369	    - - val_loss
370	      - 0.55
371	      - 0.48
372	      - 0.47
373	    - - val_accuracy (%)
374	      - 64.8
375	      - 70.5
376	      - 71.2
377	    - - val_f1_det
378	      - 0.6
379	      - 0.67
380	      - 0.68
381	    - - val_f1_int
382	      - 0.68
383	      - 0.73
384	      - 0.74
385	  - name: 'Table: Leave-One-Out Cross-Validation (selected task types)'
386	    columns:
387	    - held_out_task
388	    - domain
389	    - accuracy_on_held_out (%)
390	    - accuracy_on_rest (%)
391	    rows:
392	    - - boil
393	      - physics
394	      - 76.0
395	      - 71.8
396	    - - melt
397	      - physics
398	      - 74.5
399	      - 71.5
400	    - - mix-chemicals
401	      - chemistry
402	      - 72.0
403	      - 71.0
404	    - - mix-paint
405	      - chemistry
406	      - 67.5
407	      - 72.0
408	    - - identify-life-stages
409	      - biology
410	      - 62.0
411	      - 72.5
412	    - - grow-plant-basic
413	      - biology
414	      - 63.5
415	      - 72.0
416	  figures_description:
417	  - 'Training curves: x=steps, y=loss/accuracy. Train loss (solid) vs val loss (dashed).
418	    Val accuracy plateaus at epoch 2.5. 标注 label noise ceiling (~75%) as horizontal
419	    dotted line.'
420	  analysis: 'Router 训练收敛稳定，但 accuracy 受限于标签噪声上限。71.2% 的 val accuracy 是 median 档的中间值。
421	    Leave-one-out 结果确认跨 task type 泛化中等——同 domain 迁移较好，跨 domain 较差。 这个 router 的主要价值在于
422	    physics/chemistry tasks 上的可靠判断， 弱 tasks 上的 routing decisions 接近 random 但因为这些 tasks
423	    本身 death rate 低，影响有限。
424	
425	    '
426	- name: SimGate End-to-End Evaluation
427	  plan_id: plan-003
428	  description: 'Trained router + Qwen2.5-7B backbone 在 held-out episodes 上端到端评估。 对比
429	    always-internal, always-deterministic, oracle-routing, random-routing, confidence-threshold
430	    heuristic。
431	
432	    '
433	  expected_results:
434	    simgate_score_overall: 78.2
435	    always_internal_score: 56.8
436	    always_deterministic_score: 70.5
437	    oracle_routing_score: 81.2
438	    random_routing_score: 63.4
439	    confidence_threshold_score: 66.8
440	    simgate_minus_always_internal: 21.4
441	    simgate_minus_always_deterministic: 7.7
442	    oracle_minus_simgate: 3.0
443	    oracle_minus_always_det: 10.7
444	    catastrophic_failure_rate_internal_pct: 48.5
445	    catastrophic_failure_rate_simgate_pct: 22.3
446	    catastrophic_failure_rate_det_pct: 8.5
447	    catastrophic_failure_reduction_pct: 54.0
448	    simulator_invocation_ratio_pct: 41.2
449	    cogrouter_reported: 84.6
450	    itp_r_reported: 62.58
451	    simgate_minus_cogrouter: -6.4
452	    bootstrap_90ci_simgate:
453	    - 74.5
454	    - 81.8
455	    bootstrap_90ci_always_internal:
456	    - 52.0
457	    - 61.5
458	    bootstrap_90ci_always_det:
459	    - 66.2
460	    - 74.8
461	    task_types_with_significant_gain: 10
462	    gpu_hours_actual: 14.0
463	  result_rationale: 'Median 档 simgate_score_overall 72-84，取 78.2。未超过 CogRouter (84.6)
464	    但差距 6.4 分， 在 bootstrap CI 下两者 overlap（SimGate CI 上界 81.8 vs CogRouter 84.6），不能
465	    claim SOTA。 SimGate vs always-internal +21.4 分——核心 safety-net value，catastrophic
466	    failure 从 48.5% 降至 22.3%（降幅 54%）， 符合 median 档 catastrophic_failure_reduction_pct
467	    40-60%。 SimGate vs always-deterministic +7.7 分——selective routing 价值，说明并非所有步骤需要
468	    safety net， unconditional simulation 在低风险步骤引入了不必要的 rigid execution（LLM 在安全步骤上
469	    reasoning 更灵活）。 Oracle vs SimGate 仅 3.0 分——router 已捕获大部分可学习的 routing signal，剩余
470	    gap 来自弱 task types 的标签噪声。 Simulator invocation ratio 41.2%——router 在约 40% 步骤调用
471	    deterministic，远少于 always-det 的 100%， 说明 router 学到了 selective invocation pattern。
472	    对比 CogRouter 差距的原因：CogRouter 用 RL (CoPO) 在 trajectory 级别优化， SimGate 用 SFT per-step
473	    labels，且无 positive guidance signal (A6)——router 仅防死不指路。 10/13 task types 显著增益（physics
474	    5/5 + chemistry 3/3 + moderate 2/4）， 符合 median 档 task_types_with_significant_gain
475	    8-12。
476	
477	    '
478	  tables:
479	  - name: 'Table 1 (Main Results): SimGate vs Baselines on ScienceWorld'
480	    columns:
481	    - method
482	    - overall_score
483	    - 90% CI
484	    - catastrophic_failure_rate (%)
485	    - sim_invocation_ratio (%)
486	    - LLM_tokens (k)
487	    rows:
488	    - - Always-Internal
489	      - 56.8
490	      - '[52.0, 61.5]'
491	      - 48.5
492	      - 0
493	      - 385
494	    - - Always-Deterministic
495	      - 70.5
496	      - '[66.2, 74.8]'
497	      - 8.5
498	      - 100
499	      - 142
500	    - - Random Routing (p=0.4)
501	      - 63.4
502	      - '[58.8, 68.0]'
503	      - 30.2
504	      - 40.0
505	      - 248
506	    - - Confidence Threshold
507	      - 66.8
508	      - '[62.0, 71.5]'
509	      - 28.8
510	      - 35.5
511	      - 262
512	    - - SimGate (ours)
513	      - 78.2
514	      - '[74.5, 81.8]'
515	      - 22.3
516	      - 41.2
517	      - 240
518	    - - Oracle Routing
519	      - 81.2
520	      - '[77.8, 84.5]'
521	      - 12.0
522	      - 36.5
523	      - 255
524	    - - '---'
525	      - '---'
526	      - '---'
527	      - '---'
528	      - '---'
529	      - '---'
530	    - - CogRouter (reported)
531	      - 84.6
532	      - —
533	      - —
534	      - —
535	      - —
536	    - - ITP-R (reported)
537	      - 62.58
538	      - —
539	      - —
540	      - —
541	      - —
542	  - name: 'Table: Per-Task-Type Breakdown (SimGate vs Always-Internal)'
543	    columns:
544	    - task_type
545	    - domain
546	    - simgate_score
547	    - internal_score
548	    - delta
549	    - catastrophic_failure_reduction_pct
550	    - significant
551	    rows:
552	    - - boil
553	      - physics
554	      - 82.5
555	      - 52.0
556	      - 30.5
557	      - 62
558	      - 'yes'
559	    - - melt
560	      - physics
561	      - 85.0
562	      - 48.5
563	      - 36.5
564	      - 68
565	      - 'yes'
566	    - - change-state
567	      - physics
568	      - 84.2
569	      - 50.2
570	      - 34.0
571	      - 65
572	      - 'yes'
573	    - - freeze
574	      - physics
575	      - 80.8
576	      - 55.0
577	      - 25.8
578	      - 58
579	      - 'yes'
580	    - - use-thermometer
581	      - physics
582	      - 78.0
583	      - 60.5
584	      - 17.5
585	      - 52
586	      - 'yes'
587	    - - mix-chemicals
588	      - chemistry
589	      - 82.0
590	      - 46.8
591	      - 35.2
592	      - 70
593	      - 'yes'
594	    - - react-acid-base
595	      - chemistry
596	      - 80.5
597	      - 52.5
598	      - 28.0
599	      - 60
600	      - 'yes'
601	    - - mix-paint
602	      - chemistry
603	      - 76.2
604	      - 62.0
605	      - 14.2
606	      - 42
607	      - 'yes'
608	    - - measure-melting-point
609	      - physics
610	      - 74.5
611	      - 65.0
612	      - 9.5
613	      - 35
614	      - 'yes'
615	    - - conduct-electricity
616	      - physics
617	      - 72.0
618	      - 60.5
619	      - 11.5
620	      - 38
621	      - 'yes'
622	    - - identify-life-stages
623	      - biology
624	      - 68.5
625	      - 62.0
626	      - 6.5
627	      - 22
628	      - 'no'
629	    - - grow-plant-basic
630	      - biology
631	      - 65.0
632	      - 60.5
633	      - 4.5
634	      - 15
635	      - 'no'
636	    - - navigate-rooms
637	      - spatial
638	      - 62.8
639	      - 58.0
640	      - 4.8
641	      - 12
642	      - 'no'
643	  figures_description:
644	  - 'Grouped bar chart: SimGate vs Always-Internal vs Always-Det vs Oracle per task
645	    type, sorted by delta. Physics/chemistry tasks cluster left with large deltas,
646	    biology/spatial tasks cluster right with small deltas.'
647	  - 'Scatter plot: x=catastrophic_failure_rate_internal, y=SimGate delta. Strong positive
648	    correlation, 标注 r=0.91. 直接可视化 ''death avoidance is primary mechanism'' claim.'
649	  analysis: 'SimGate 78.2 低于 CogRouter 84.6 约 6 分。叙事不能 claim SOTA，但 controlled ablation
650	    提供了强因果证据： SimGate vs internal (+21.4)、vs det (+7.7)、vs random (+14.8)、vs heuristic
651	    (+11.4) 全部显著。 catastrophic failure reduction 54% 是强 headline number。 Per-task
652	    breakdown 清晰展示 death avoidance 是主要机制——physics/chemistry 的 delta 与 internal death
653	    rate 高度相关 (r=0.91)。 3 个弱 tasks (biology/spatial) 的 delta <7 且不显著，支持 A1 的 domain-specific
654	    判断。 SimGate 比 CogRouter 差的原因可归为：(1) SFT vs RL training，(2) 无 positive guidance
655	    signal。 Paper 叙事应改为 "first controlled study demonstrating causal role of deterministic
656	    computation in preventing catastrophic LLM failures"。
657	
658	    '
659	- name: Explicit vs Implicit Routing Ablation
660	  plan_id: plan-004
661	  description: '三条件对比：(a) 1.7B explicit router (SimGate), (b) 1.7B implicit router
662	    (SFT output [SIMULATE]), (c) 7B implicit routing (backbone tool-use prompt)。全部用相同
663	    counterfactual labels 训练。
664	
665	    '
666	  expected_results:
667	    explicit_1_7b_score: 78.2
668	    implicit_1_7b_score: 73.5
669	    implicit_7b_score: 74.8
670	    explicit_minus_implicit_1_7b: 4.7
671	    explicit_minus_implicit_7b: 3.4
672	    implicit_1_7b_catastrophic_failure_pct: 28.5
673	    implicit_7b_catastrophic_failure_pct: 26.2
674	    explicit_sim_invocation_ratio_pct: 41.2
675	    implicit_1_7b_sim_invocation_ratio_pct: 35.0
676	    implicit_7b_sim_invocation_ratio_pct: 38.5
677	    bootstrap_90ci_explicit:
678	    - 74.5
679	    - 81.8
680	    bootstrap_90ci_implicit_1_7b:
681	    - 69.2
682	    - 77.8
683	    bootstrap_90ci_implicit_7b:
684	    - 70.5
685	    - 79.0
686	    explicit_vs_implicit_1_7b_significant: true
687	    explicit_vs_implicit_7b_significant: marginal (p=0.08)
688	    gpu_hours_actual: 11.0
689	  result_rationale: 'Median 档 explicit_minus_implicit 3-8 分，statistical significance
690	    在部分条件下边缘 (A3)。 Explicit 1.7B vs implicit 1.7B: +4.7 分，parameter-matched comparison
691	    显著 (p<0.05)。 这说明 explicit modular router 架构本身有价值——将 routing decision 从 generation
692	    中解耦， 避免了 implicit routing 中 generation 任务和 routing 任务的 multi-task interference。
693	    Explicit 1.7B vs implicit 7B: +3.4 分，但 CI overlap 大 (p=0.08，边缘显著)。 7B implicit
694	    比 1.7B implicit 好 1.3 分——额外容量有 marginal 帮助但不足以弥补架构劣势。 Implicit routers 的 sim_invocation_ratio
695	    偏低 (35-38.5% vs explicit 41.2%)—— implicit routing 倾向于 under-invoke simulator（routing
696	    signal 在 generation logits 中被稀释）， 导致更多 catastrophic failures 未被拦截。 这个 "consistent
697	    but moderate advantage" 的结果支持 C2 的定性 claim（interpretability, modularity） 而非强 performance
698	    claim。Median 档下 C2 的重心应转向： explicit router 可独立替换、routing decisions 可分析，这些定性价值在
699	    3-5 分性能差距之上额外成立。
700	
701	    '
702	  tables:
703	  - name: 'Table: Explicit vs Implicit Routing Ablation'
704	    columns:
705	    - condition
706	    - params
707	    - overall_score
708	    - 90% CI
709	    - catastrophic_failure (%)
710	    - sim_invocation (%)
711	    - p vs explicit
712	    rows:
713	    - - Explicit Router (SimGate)
714	      - 1.7B
715	      - 78.2
716	      - '[74.5, 81.8]'
717	      - 22.3
718	      - 41.2
719	      - —
720	    - - Implicit Router (SFT)
721	      - 1.7B
722	      - 73.5
723	      - '[69.2, 77.8]'
724	      - 28.5
725	      - 35.0
726	      - '0.03'
727	    - - Implicit Routing (tool-use)
728	      - 7B
729	      - 74.8
730	      - '[70.5, 79.0]'
731	      - 26.2
732	      - 38.5
733	      - '0.08'
734	    - - Always-Internal
735	      - —
736	      - 56.8
737	      - '[52.0, 61.5]'
738	      - 48.5
739	      - 0
740	      - <0.001
741	  figures_description:
742	  - 'Box plot: three conditions'' score distributions across task types. Explicit
743	    has higher median and tighter IQR. Annotate p-values for pairwise comparisons.'
744	  analysis: 'Parameter-matched comparison (1.7B explicit vs 1.7B implicit, +4.7, p=0.03)
745	    是 C2 最干净的证据。 7B implicit 条件 (p=0.08) 可写为 "marginal significance"，但方向一致。 Median
746	    档叙事：explicit routing 是 "consistent but moderate advantage"， 主要价值在 architectural
747	    benefits (modularity, interpretability, independent replacement)， 用 4.7 分的定量证据
748	    + 定性分析支撑。不能写成 "large performance gap"。
749	
750	    '
751	- name: Per-Task Routing Pattern Analysis
752	  plan_id: plan-005
753	  description: '从 plan-003 输出分析 routing patterns：(a) 哪些 task types 触发 deterministic
754	    最多， (b) routing 集中在哪个 episode phase，(c) router-as-diagnostic-probe 识别 LLM failure
755	    modes。
756	
757	    '
758	  expected_results:
759	    n_routing_decisions_analyzed: 3900
760	    phase_early_det_pct: 25.0
761	    phase_mid_det_pct: 52.0
762	    phase_late_det_pct: 38.0
763	    physics_det_invocation_pct: 48.5
764	    chemistry_det_invocation_pct: 45.2
765	    biology_det_invocation_pct: 28.0
766	    spatial_det_invocation_pct: 22.0
767	    top_3_routing_triggers: state-change actions (heat/cool/mix), multi-step causal
768	      chains (>3 steps), post-failure recovery steps
769	    failure_mode_clusters_identified: 4
770	    cluster_clarity: moderate — 2 clear clusters, 2 diffuse
771	    gpu_hours_actual: 1.5
772	  result_rationale: 'Median 档 routing patterns 部分可解释 (A5)——能看到 phase-dependent 模式但
773	    failure taxonomy 不够清晰。 Phase-dependent pattern 清晰：mid-game (steps 8-20) routing
774	    最密集 (52%)， 因为这个阶段 agent 执行 state-changing actions (加热、冷却、混合) 最多， LLM 容易在多步物理推理中
775	    hallucinate 中间状态。 Early-game (steps 1-7) routing 较低 (25%)——agent 主要在 navigate
776	    和 gather objects，death 风险低。 Late-game (steps 21-30) routing 中等 (38%)——部分 tasks
777	    在此阶段做 final verification， 但也有很多 episodes 已经结束或 stuck。 4 个 failure mode clusters
778	    中： (1) "thermal state tracking failure" — 清晰，LLM 丢失温度/相态信息 (2) "chemical reaction
779	    sequencing" — 清晰，LLM 搞错反应步骤顺序 (3) "multi-step causal confusion" — 模糊，涵盖多种因果推理错误，不够
780	    specific (4) "environment state drift" — 模糊，router triggers 散布在各种步骤中 这是 median
781	    档 A5 的典型表现——有 pattern 但 failure taxonomy 不 clean。 Paper figure 只报告 phase-dependent
782	    routing trends，不宣称 comprehensive failure taxonomy。
783	
784	    '
785	  tables:
786	  - name: 'Table: Routing Decision Distribution by Episode Phase'
787	    columns:
788	    - phase
789	    - steps
790	    - total_decisions
791	    - det_routing_pct
792	    - avg_death_rate_if_internal
793	    rows:
794	    - - early
795	      - 1-7
796	      - 1200
797	      - 25.0
798	      - 0.12
799	    - - mid
800	      - 8-20
801	      - 1800
802	      - 52.0
803	      - 0.45
804	    - - late
805	      - 21-30
806	      - 900
807	      - 38.0
808	      - 0.28
809	  - name: 'Table: Failure Mode Clusters (Router-as-Diagnostic-Probe)'
810	    columns:
811	    - cluster
812	    - description
813	    - n_steps
814	    - pct_of_det_routing
815	    - clarity
816	    rows:
817	    - - 1
818	      - thermal state tracking failure
819	      - 420
820	      - 27.0
821	      - clear
822	    - - 2
823	      - chemical reaction sequencing error
824	      - 310
825	      - 20.0
826	      - clear
827	    - - 3
828	      - multi-step causal confusion
829	      - 480
830	      - 31.0
831	      - diffuse
832	    - - 4
833	      - environment state drift
834	      - 340
835	      - 22.0
836	      - diffuse
837	  figures_description:
838	  - 'Figure 1 (Paper): Routing heatmap — x=episode step (1-30), y=task type (sorted
839	    by domain). Color intensity = deterministic routing probability. Clear ''hot band''
840	    in mid-game steps for physics/chemistry tasks. Annotated with phase boundaries.'
841	  - 'Supplementary: t-SNE of router hidden states at deterministic-routing steps,
842	    colored by cluster ID. Clusters 1&2 tight, clusters 3&4 overlapping.'
843	  analysis: 'Phase-dependent routing trend 是 robust 的 finding，可以放 paper Figure 1。
844	    但 failure taxonomy 降级处理——从 "failure mode taxonomy" 改为 "we observe routing concentrates
845	    at state-change actions during mid-game phases, suggesting the router learns to
846	    detect high-risk physical reasoning steps"。不宣称 comprehensive failure analysis，只报告
847	    observable trends。 Mid-game concentration (52% of det routing) 直接对应 death avoidance
848	    mechanism—— 这正是 agent 执行 irreversible physical actions 的阶段。
849	
850	    '
851	- name: 2-Way vs 3-Way Routing Ablation
852	  plan_id: plan-006
853	  description: '补充 deep-internal modality 数据，比较 {internal, deterministic} vs {fast-internal,
854	    deep-internal, deterministic}。 测试 fast/deep internal 区分是否有额外价值。
855	
856	    '
857	  expected_results:
858	    two_way_score: 78.2
859	    three_way_score: 79.8
860	    delta: 1.6
861	    p_value: 0.22
862	    significant: false
863	    three_way_sim_invocation_pct: 39.5
864	    three_way_deep_internal_pct: 18.0
865	    three_way_fast_internal_pct: 42.5
866	    supplemental_data_collection_hours: 5.5
867	    router_retraining_hours: 3.0
868	    gpu_hours_actual: 9.5
869	  result_rationale: 'Median 档下 3-way 与 2-way 差距小且不显著 (+1.6, p=0.22)。 Fast/deep internal
870	    区分的理论价值在于：deep-internal 在需要更多 reasoning 但不需要 ground-truth 的步骤上 用 extended thinking
871	    提升质量。但实际效果有限，原因： (1) death avoidance 是主要增益来源 (A6)——一旦 deterministic 拦截了 catastrophic
872	    failures， 剩余步骤中 fast vs deep internal 的差异很小（LLM 在安全步骤上的表现差异不大）。 (2) 没有 positive
873	    guidance signal——deep internal 不能给出更好的 task guidance，只是"想更久"， 但在 deterministic
874	    已经处理了高风险步骤后，多想对安全步骤帮助有限。 (3) Router 从 2-class 升到 3-class 增加了 classification 难度，在
875	    median 档标签噪声下性能提升被抵消。 结论：2-way 足够，simplifies the story。Paper 中可以一句话报告 "binary
876	    routing (simulate-or-not) suffices; adding a third modality yields no significant
877	    improvement"。
878	
879	    '
880	  tables:
881	  - name: 'Table: 2-Way vs 3-Way Routing Comparison'
882	    columns:
883	    - routing_scheme
884	    - overall_score
885	    - 90% CI
886	    - sim_invocation (%)
887	    - p vs 2-way
888	    rows:
889	    - - 2-way {int, det}
890	      - 78.2
891	      - '[74.5, 81.8]'
892	      - 41.2
893	      - —
894	    - - 3-way {fast, deep, det}
895	      - 79.8
896	      - '[75.8, 83.5]'
897	      - 39.5
898	      - '0.22'
899	  figures_description:
900	  - 'Paired bar chart: 2-way vs 3-way per task type. Most bars nearly identical. 标注
901	    ns (not significant).'
902	  analysis: '3-way 不显著优于 2-way，simplifies the paper narrative。 可以 claim "binary routing
903	    decision (simulate or not) captures the essential routing signal"， 支持 safety-net
904	    framing——router 的核心工作是检测 high-risk steps，而非 fine-grained compute allocation。 在
905	    paper 中作为 ablation 一句话报告即可。这增加了实验密度而不改变结论。
906	
907	    '
908	- name: Boil Task Rerun with v3 Code
909	  plan_id: plan-007
910	  description: '用 v3 clean code（strict > tie-break, death filter only on internal）重跑
911	    boil task 20 episodes， 与 MVP 旧代码结果对比，确保分析一致性。
912	
913	    '
914	  expected_results:
915	    boil_v3_internal_mean: -46.5
916	    boil_v3_det_mean: -10.8
917	    boil_v3_oracle_mean: -3.2
918	    boil_v3_det_minus_internal: 35.7
919	    boil_v3_oracle_minus_det: 7.6
920	    boil_v3_bootstrap_90ci_det_minus_internal:
921	    - 22.0
922	    - 49.5
923	    boil_v3_death_rate_internal: 0.55
924	    boil_v3_death_rate_det: 0.08
925	    boil_mvp_internal_mean: -49.8
926	    boil_mvp_det_mean: -19.7
927	    delta_from_mvp_internal: 3.3
928	    delta_from_mvp_det: 8.9
929	    gpu_hours_actual: 2.5
930	  result_rationale: 'V3 code 的两个修正（strict > tie-break + death filter only on internal）对
931	    boil 的影响： (1) Strict > tie-break：减少了 deterministic 被选为 "best" 的 marginal cases，
932	    internal mean 略有提升 (-49.8 → -46.5) 因为部分原本 tie-break 判给 det 的 cases 现在留在 internal。
933	    (2) Death filter only on internal：det mean 显著提升 (-19.7 → -10.8) 因为 MVP 旧代码对 det
934	    也做了 death filter， 过滤掉了一些 det 原本能正确处理但被误判为 "death" 的 steps。 整体 det_minus_internal
935	    从 MVP 的 ~30 分变为 35.7 分，与 melt/change-state 的 ~40 分更接近， 说明 v3 code 修正消除了旧代码的 systematic
936	    bias。 Oracle mean 提升到 -3.2（接近 0），更符合预期——selective routing 应当接近 best-of-both。
937	
938	    '
939	  tables:
940	  - name: 'Table: Boil Task — v3 vs MVP Code Comparison'
941	    columns:
942	    - metric
943	    - MVP (old code)
944	    - v3 (clean code)
945	    - delta
946	    rows:
947	    - - internal_mean
948	      - -49.8
949	      - -46.5
950	      - '+3.3'
951	    - - det_mean
952	      - -19.7
953	      - -10.8
954	      - '+8.9'
955	    - - oracle_mean
956	      - -29.7
957	      - -3.2
958	      - '+26.5'
959	    - - det_minus_internal
960	      - 30.1
961	      - 35.7
962	      - '+5.6'
963	    - - death_rate_internal
964	      - ~0.6
965	      - 0.55
966	      - —
967	    - - death_rate_det
968	      - ~0.15
969	      - 0.08
970	      - —
971	  figures_description: []
972	  analysis: 'V3 code 修正提升了数据质量，特别是 oracle routing 从 -29.7 → -3.2 的大幅改善 说明旧 code 的
973	    death filter bug 严重低估了 selective routing 的价值。 修正后 boil 与其他 physics tasks (melt,
974	    change-state) 的 pattern 更一致， 全部 det_minus_internal 在 35-40 分范围。Paper 只使用 v3 数据。
975	
976	    '
977	- name: Router Size Ablation
978	  plan_id: plan-008
979	  description: '比较 Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B 作为 router 的效果。 测试 router
980	    capacity 敏感性。
981	
982	    '
983	  expected_results:
984	    qwen3_1_7b_score: 78.2
985	    qwen2_5_1_5b_score: 76.0
986	    qwen2_5_3b_score: 79.0
987	    qwen3_1_7b_router_accuracy_pct: 71.2
988	    qwen2_5_1_5b_router_accuracy_pct: 67.5
989	    qwen2_5_3b_router_accuracy_pct: 73.0
990	    delta_1_5b_vs_1_7b: -2.2
991	    delta_3b_vs_1_7b: 0.8
992	    significant_1_5b_vs_1_7b: false
993	    significant_3b_vs_1_7b: false
994	    inference_latency_1_5b_ms: 12
995	    inference_latency_1_7b_ms: 15
996	    inference_latency_3b_ms: 28
997	    gpu_hours_actual: 10.0
998	  result_rationale: 'Median 档下 router 性能受限于 label noise 而非 model capacity (plan-002
999	    分析已显示)。 1.5B vs 1.7B: -2.2 分但不显著 (p>0.1)——1.5B 容量略不足以 capture 一些 edge case routing
1000	    patterns， 但差距在标签噪声范围内。Router accuracy 67.5% vs 71.2%，差距主要在 moderate/weak signal
1001	    tasks。 3B vs 1.7B: +0.8 分不显著——额外容量无法突破标签噪声上限。Router accuracy 73% vs 71.2%， marginal
1002	    improvement 被 end-to-end evaluation 的 variance 吞没。 这支持 "lightweight router suffices"
1003	    claim：1.5B-3B 范围内性能差异 <3 分， 瓶颈在训练数据质量而非 router capacity。 Inference latency 差异对
1004	    overall pipeline 影响 negligible（router inference 远快于 LLM backbone inference）。
1005	
1006	    '
1007	  tables:
1008	  - name: 'Table: Router Size Ablation'
1009	    columns:
1010	    - router
1011	    - params
1012	    - router_accuracy (%)
1013	    - e2e_score
1014	    - 90% CI
1015	    - latency (ms)
1016	    rows:
1017	    - - Qwen2.5-1.5B
1018	      - 1.5B
1019	      - 67.5
1020	      - 76.0
1021	      - '[71.8, 80.2]'
1022	      - 12
1023	    - - Qwen3-1.7B
1024	      - 1.7B
1025	      - 71.2
1026	      - 78.2
1027	      - '[74.5, 81.8]'
1028	      - 15
1029	    - - Qwen2.5-3B
1030	      - 3.0B
1031	      - 73.0
1032	      - 79.0
1033	      - '[75.2, 82.8]'
1034	      - 28
1035	  figures_description:
1036	  - 'Line plot: x=router params (log scale), y=e2e score. Near-flat line with error
1037	    bars overlapping. 标注 ''label noise ceiling'' as horizontal band.'
1038	  analysis: 'Router size ablation 支持两个 claims：(1) 小 router 足够 ("lightweight" in C2)，
1039	    (2) 瓶颈在标签质量——增加 router capacity 收益递减。 Paper 可报告 "routers from 1.5B to 3B parameters
1040	    achieve comparable performance (76-79), suggesting the routing task is learnable
1041	    at modest scale"。
1042	
1043	    '
1044	- name: MATH Track — Code Interpreter as Oracle
1045	  plan_id: plan-009
1046	  description: '500 道 Level 4-5 MATH 题，2-way routing: internal / code-interpreter。
1047	    测试 safety-aware routing 是否泛化到代码解释器场景。
1048	
1049	    '
1050	  expected_results:
1051	    simgate_math_accuracy_pct: 62.5
1052	    always_internal_accuracy_pct: 55.0
1053	    always_code_accuracy_pct: 58.8
1054	    oracle_routing_accuracy_pct: 68.0
1055	    simgate_minus_internal: 7.5
1056	    simgate_minus_always_code: 3.7
1057	    code_invocation_ratio_pct: 45.0
1058	    router_accuracy_math_pct: 63.0
1059	    catastrophic_error_reduction_pct: 28.0
1060	    gpu_hours_actual: 18.0
1061	  result_rationale: 'Median 档下 MATH track 显示中等泛化 (A4)。 Safety-aware routing 在 MATH
1062	    上的增益 (+7.5 vs internal) 远小于 ScienceWorld (+21.4)，原因： (1) MATH 没有 -100 death penalty——错误只是
1063	    0 分而非 catastrophic failure， safety-net 机制的 value proposition 减弱。 (2) Code interpreter
1064	    的优势在于 arithmetic/algebraic computation，不在于 "preventing catastrophic failures"。
1065	    LLM 在 MATH 上的错误模式更分散（reasoning errors, not just computation errors）， code interpreter
1066	    只能修正 computation errors 这一子集。 (3) Router 的 ScienceWorld labels 无法直接迁移，MATH 上需要
1067	    fresh labels， 但 label quality 更差——hindsight labeling 在 MATH 上不如 ScienceWorld 清晰（没有
1068	    death/survival 信号）。 Router accuracy 仅 63%（低于 ScienceWorld 71.2%），进一步说明 routing
1069	    signal 在 MATH 上更弱。 Catastrophic error reduction 仅 28%——定义 catastrophic 为 "算错导致
1070	    0 分"， code interpreter 能防止部分但远非全部。 这个结果仍有 paper 价值：证明 selective routing 原则泛化 (simgate
1071	    > always-code > always-internal)， 但 safety-aware framing 在无 catastrophic penalty
1072	    的环境中 weakens。可作为 discussion/future work 素材。
1073	
1074	    '
1075	  tables:
1076	  - name: 'Table: MATH Track Results (Level 4-5, n=500)'
1077	    columns:
1078	    - method
1079	    - accuracy (%)
1080	    - code_invocation (%)
1081	    - computation_error_rate (%)
1082	    rows:
1083	    - - Always-Internal
1084	      - 55.0
1085	      - 0
1086	      - 18.5
1087	    - - Always-Code
1088	      - 58.8
1089	      - 100
1090	      - 5.2
1091	    - - SimGate Router
1092	      - 62.5
1093	      - 45.0
1094	      - 10.8
1095	    - - Oracle Routing
1096	      - 68.0
1097	      - 38.0
1098	      - 3.0
1099	  figures_description:
1100	  - 'Bar chart: MATH results alongside ScienceWorld results (normalized). Clear visual:
1101	    ScienceWorld gains much larger. 标注 ''catastrophic penalty effect''.'
1102	  analysis: 'MATH 结果支持 selective > unconditional 的一般原则但效果弱得多。 如果 paper 长度允许，可以作为一段
1103	    "Generalization" 讨论； 如果 4-page 紧张，放 appendix 或 future work 一句话提及。 关键 takeaway："safety-aware
1104	    routing gains are proportional to the severity of catastrophic failure penalties"。
1105	
1106	    '
1107	- name: Cross-Task Transfer within ScienceWorld
1108	  plan_id: plan-010
1109	  description: 'Chemistry-only 训练 → physics 评估，physics-only 训练 → chemistry 评估。 测试
1110	    routing patterns 跨 domain 迁移性。
1111	
1112	    '
1113	  expected_results:
1114	    chem_train_chem_eval_score: 79.5
1115	    chem_train_phys_eval_score: 72.8
1116	    phys_train_phys_eval_score: 80.0
1117	    phys_train_chem_eval_score: 71.5
1118	    transfer_degradation_chem_to_phys: 7.2
1119	    transfer_degradation_phys_to_chem: 8.0
1120	    full_train_phys_eval_score: 82.5
1121	    full_train_chem_eval_score: 82.0
1122	    cross_domain_router_accuracy_pct: 62.5
1123	    same_domain_router_accuracy_pct: 76.0
1124	    gpu_hours_actual: 4.5
1125	  result_rationale: 'Median 档 routing pattern 迁移中等 (A4/A5)。 Chemistry → physics 迁移降幅
1126	    7.2 分，physics → chemistry 降幅 8.0 分—— 大约 40-50% 的 routing knowledge 可以跨 domain
1127	    迁移。 原因：death avoidance 的部分 pattern 是 domain-generic 的 （如 "state-change actions
1128	    需要 deterministic verification"）——这个 high-level 模式在两个 domain 共享。 但 domain-specific
1129	    failure patterns（如 chemistry 的 reaction sequencing vs physics 的 thermal tracking）
1130	    不迁移，导致 cross-domain router accuracy 从 76% 降到 62.5%。 这个结果在 paper 中可以作为一段 analysis："routing
1131	    patterns partially transfer across task domains sharing similar physical reasoning
1132	    requirements, but domain-specific failure modes require domain-specific training
1133	    data"。 不需要改变 main claims，但增加了对 router generalization 的理解。
1134	
1135	    '
1136	  tables:
1137	  - name: 'Table: Cross-Task Transfer Matrix'
1138	    columns:
1139	    - train_domain
1140	    - eval_domain
1141	    - score
1142	    - router_accuracy (%)
1143	    - vs full-train delta
1144	    rows:
1145	    - - chemistry
1146	      - chemistry
1147	      - 79.5
1148	      - 78.0
1149	      - '-2.5'
1150	    - - chemistry
1151	      - physics
1152	      - 72.8
1153	      - 62.5
1154	      - '-9.7'
1155	    - - physics
1156	      - physics
1157	      - 80.0
1158	      - 77.5
1159	      - '-2.5'
1160	    - - physics
1161	      - chemistry
1162	      - 71.5
1163	      - 61.0
1164	      - '-10.5'
1165	    - - all
1166	      - physics
1167	      - 82.5
1168	      - 78.5
1169	      - —
1170	    - - all
1171	      - chemistry
1172	      - 82.0
1173	      - 79.0
1174	      - —
1175	  figures_description:
1176	  - 'Transfer matrix heatmap: 2x2 grid showing score degradation. Diagonal (same-domain)
1177	    brighter, off-diagonal darker but not black — partial transfer.'
1178	  analysis: ~40-50% routing knowledge 跨 domain 迁移，与 median 档 A4 (counterfactual labels
1179	    泛化中等) 一致。 如果 4-page 紧张，这个实验可以仅在 results 最后一段用 2 句话概括。 重要 insight：routing 的 domain-generic
1180	    component 是 "detect state-change actions under uncertainty"， 这个 framing 比 task-specific
1181	    failure taxonomy 更 generalizable。
1182	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b280bfc9-997c-4866-82e0-6f005a324132",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "251dda34-19bb-4e16-a3cc-3e7cbc7591ef",
  "sourceToolAssistantUUID": "b280bfc9-997c-4866-82e0-6f005a324132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-13T16:18:14.989Z_

Now I need to reconcile something. The task prompt mentions specific numbers from "the paper" that don't match what I see in the actual paper.tex. The task prompt's "Paper Summary" describes a paper titled "When Does Deterministic Computation Help LLM Agents?" with *negative* results (SimGate approximately equals always-simulate, 65.2 vs 64.8), while the actual paper.tex I just read is titled "SimGate: Safety-Aware Routing..." and shows *positive* results (SimGate 78.2 vs always-det 70.5). 

The task summary appears to describe a different scenario -- possibly the paper as it would look if the results came out negatively (the "worst" scenario). But I'm told to review based on the numbers provided in the task prompt. Let me check the "worst" scenario paper to confirm.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "251dda34-19bb-4e16-a3cc-3e7cbc7591ef",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQwSfN8MHSgEoCT3EG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8eb3fcf-4595-4b53-9b61-a2e09295bff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTXMvQ8eRSC3acn1FuL3MD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 43874,
      "cache_read_input_tokens": 26724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 43874,
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

_source line 44 · 2026-05-13T16:18:17.477Z_

<details open><summary>🔧 Tool call — Read · `toolu_01963PK2Z86B6VaNd9SpcVof`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8eb3fcf-4595-4b53-9b61-a2e09295bff9",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQwSfN8MHSgEoCT3EG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d2d9aec-e575-46b7-b41e-cc967921aa3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTXMvQ8eRSC3acn1FuL3MD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 43874,
      "cache_read_input_tokens": 26724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 43874,
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

_source line 45 · 2026-05-13T16:18:17.483Z_

<details><summary>↩ Tool result · `toolu_01963PK2Z86B6VaNd9SpcVof`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{booktabs}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{xcolor}
8	\usepackage[hidelinks]{hyperref}
9	
10	\title{When Does Deterministic Computation Help LLM Agents? \\
11	A Diagnostic Study on ScienceWorld}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	LLM agents operating in rule-governed environments suffer catastrophic failures when they hallucinate physical state transitions.
20	A natural remedy is routing selected actions to a deterministic external simulator, but \emph{when} does such routing actually help?
21	We introduce a counterfactual evaluation methodology that forks agent trajectories at each decision step across three computation modalities---fast internal reasoning, deep chain-of-thought, and deterministic simulation---and measures per-step value via hindsight scoring.
22	Applying this methodology to 15 ScienceWorld task types (300 episodes, 6{,}600 labeled steps), we find that the value of deterministic computation is \textbf{sharply task-dependent}: simulation yields large gains (+16--29 points) on 4 death-risk task types involving physical state transitions, but provides no benefit---and occasionally harms performance---on the remaining 11 task types.
23	A learned per-step router (SimGate) achieves 65.2 overall score, statistically indistinguishable from unconditional simulation (64.8, $\Delta{=}0.4$, 90\% CI $[-4.8, 5.6]$), suggesting that per-step routing is the wrong granularity.
24	An explicit modular router shows no advantage over implicit backbone-integrated routing ($\Delta{=}1.2$, $p{=}0.38$), and routing patterns do not transfer across task domains.
25	These negative results, combined with per-task diagnostic analysis, suggest that the actionable question is not \emph{how} to route but \emph{which task types} require deterministic computation---a task-level decision rather than a step-level one.
26	\end{abstract}
27	
28	\section{Introduction}
29	
30	LLM-based agents have shown strong performance on interactive environments~\cite{yao2023react,shinn2023reflexion}, yet they remain brittle on tasks requiring accurate physical state reasoning.
31	In ScienceWorld~\cite{wang2022scienceworld}, agents must manipulate objects according to physical and chemical rules; hallucinating a state transition (e.g., predicting that water boils at room temperature) can trigger agent death and catastrophic score penalties.
32	
33	Prior work has explored augmenting LLM agents with external computation.
34	CogRouter~\cite{qiao2024cogrouter} uses reinforcement learning to route between reasoning modalities, achieving 84.6 on ScienceWorld.
35	ITP-R~\cite{lu2024itpr} routes to an approximate LLM world model but underperforms pure internal reasoning (62.58).
36	ReTool~\cite{feng2024retool} and ToRA~\cite{gou2024tora} learn implicit tool invocation for mathematical reasoning.
37	However, no prior work systematically characterizes \emph{when} deterministic external computation provides value versus when internal LLM reasoning suffices.
38	
39	We address this gap with two contributions:
40	\textbf{(1)} A \emph{counterfactual evaluation methodology} that forks trajectories at each step into three modalities and labels the optimal choice via hindsight scoring, enabling fine-grained analysis of simulation value.
41	\textbf{(2)} A \emph{per-task diagnostic analysis} revealing that the value of deterministic computation is concentrated in 4 out of 15 task types---those involving catastrophic-failure-prone physical state transitions---while learned per-step routing provides no advantage over the trivial always-simulate baseline.
42	
43	Our findings reframe the routing question: rather than designing better per-step routers, practitioners should identify task categories where deterministic computation prevents catastrophic failures and apply it unconditionally within those categories.
44	
45	\section{Method}
46	
47	\subsection{Framework: SimGate}
48	
49	SimGate comprises three components: (1) an LLM agent backbone (Qwen2.5-7B) that generates actions via internal reasoning, (2) a deterministic environment simulator that executes actions and returns ground-truth next states, and (3) a lightweight router that decides, at each step, whether to use the backbone's internal prediction or the simulator's output.
50	
51	At each step $t$, the agent observes state $s_t$ and proposes action $a_t$. The router $R_\phi$ receives the trajectory history $h_t = (s_1, a_1, \ldots, s_t)$ and outputs a routing decision $d_t \in \{\texttt{internal}, \texttt{deterministic}\}$. If $d_t = \texttt{deterministic}$, the simulator computes the next-state prediction; otherwise, the backbone's internal reasoning is used.
52	
53	\subsection{Counterfactual Evaluation Methodology}
54	
55	To label optimal per-step routing decisions, we collect \emph{counterfactual trajectories}. For each episode, at each step we fork execution into three modalities:
56	\begin{itemize}
57	\item \textbf{Fast-internal}: Single-pass LLM reasoning (standard prompting).
58	\item \textbf{Deep-internal}: Extended chain-of-thought with 4$\times$ token budget.
59	\item \textbf{Deterministic}: Ground-truth simulator execution.
60	\end{itemize}
61	
62	Each fork is rolled out for the remainder of the episode. The modality yielding the highest episode score is labeled as optimal for that step. We collect 300 episodes (20 per task type) with an average of 22 steps each, producing 6{,}600 labeled step decisions.
63	
64	\subsection{Router Training}
65	
66	We train the router $R_\phi$ via supervised fine-tuning on counterfactual labels. The router is a Qwen3-1.7B model that takes $(h_t, s_t)$ as input and predicts the optimal modality. We use an 80/20 stratified train/validation split (5{,}280 / 1{,}320 samples), learning rate $2 \times 10^{-5}$, batch size 32, for 3 epochs.
67	
68	\section{Experiments}
69	
70	We evaluate on ScienceWorld across 15 task types grouped by risk profile: \emph{death-risk} (4 tasks: boil, melt, change-state, freeze), \emph{marginal} (3 tasks), and \emph{low-risk} (8 tasks). Each configuration is evaluated on 20 held-out episodes per task type. Total compute: 90 GPU-hours on A6000.
71	
72	\subsection{Counterfactual Label Analysis}
73	
74	\begin{table}[t]
75	\centering
76	\small
77	\begin{tabular}{lcccc}
78	\toprule
79	\textbf{Group} & \textbf{Tasks} & \textbf{Fast\%} & \textbf{Det\%} & \textbf{Ambig\%} \\
80	\midrule
81	Death-risk & 4 & 18 & 70 & 22 \\
82	Marginal & 3 & 38 & 38 & 45 \\
83	Low-risk & 8 & 55 & 20 & 52 \\
84	\midrule
85	Overall & 15 & 42 & 36 & 42 \\
86	\bottomrule
87	\end{tabular}
88	\caption{Counterfactual label distribution by task group. ``Ambig\%'' indicates the fraction of steps where the best and second-best modalities differ by $<$5 points. Deep-internal omitted for space (22\% overall).}
89	\label{tab:labels}
90	\end{table}
91	
92	Table~\ref{tab:labels} reveals a stark asymmetry in label quality. Death-risk tasks produce clear routing signals: 70\% of steps favor deterministic computation, with only 22\% ambiguous. In contrast, low-risk tasks are majority-ambiguous (52\%), with the three modalities producing similar trajectories. This asymmetry is the root cause of downstream routing failures: 73\% of training steps come from tasks where modality choice has negligible impact, diluting the signal from the 27\% of steps where routing matters.
93	
94	\subsection{Main Results}
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\begin{tabular}{lccccc}
100	\toprule
101	\textbf{Method} & \textbf{All} & \textbf{DR\textsubscript{4}} & \textbf{MR\textsubscript{3}} & \textbf{LR\textsubscript{8}} & \textbf{CF\%} \\
102	\midrule
103	Always-internal & 59.5 & 13.5 & 57.3 & 83.3 & 19.7 \\
104	Always-det & 64.8 & 45.5 & 58.0 & 77.0 & 6.3 \\
105	Random (50/50) & 62.1 & 29.5 & 57.7 & 80.1 & 13.0 \\
106	Conf-threshold & 63.5 & 35.0 & 57.8 & 78.5 & 10.5 \\
107	\textbf{SimGate} & \textbf{65.2} & 38.5 & 58.0 & 81.3 & 13.0 \\
108	Oracle routing & 70.0 & 46.5 & 62.0 & 84.8 & 4.0 \\
109	\midrule
110	CogRouter$^\dagger$ & 84.6 & --- & --- & --- & --- \\
111	ITP-R$^\dagger$ & 62.58 & --- & --- & --- & --- \\
112	\bottomrule
113	\end{tabular}
114	\caption{End-to-end ScienceWorld scores. DR/MR/LR: death-risk/marginal/low-risk task groups. CF\%: catastrophic failure rate. $^\dagger$Cited from original papers (different backbone/training).}
115	\label{tab:main}
116	\end{table}
117	
118	Table~\ref{tab:main} shows our central finding. SimGate (65.2) is statistically indistinguishable from always-deterministic (64.8): $\Delta{=}0.4$, 90\% CI $[-4.8, 5.6]$. The learned router provides no advantage over the trivial baseline of always simulating. Oracle routing (70.0) demonstrates a modest ceiling of 5.2 points above always-deterministic (CI $[1.0, 9.4]$), confirming that per-step routing has limited theoretical value in ScienceWorld.
119	
120	The score gap between SimGate and always-internal (5.7, CI $[1.2, 10.3]$) is driven entirely by death-risk tasks: SimGate scores 38.5 vs.\ 13.5 on these 4 task types, while performing comparably or slightly worse on the remaining 11. Excluding death-risk tasks, SimGate (81.3) underperforms always-internal (83.3).
121	
122	\subsection{Per-Task Diagnostic Analysis}
123	
124	\begin{table}[t]
125	\centering
126	\small
127	\begin{tabular}{llcccc}
128	\toprule
129	\textbf{Task} & \textbf{Grp} & \textbf{Int} & \textbf{Det} & \textbf{SG} & \textbf{$\Delta$} \\
130	\midrule
131	boil & DR & 12 & 48 & 40 & +28 \\
132	melt & DR & 8 & 42 & 35 & +27 \\
133	change-st. & DR & 14 & 50 & 43 & +29 \\
134	freeze & DR & 20 & 42 & 36 & +16 \\
135	\midrule
136	mix-paint & MR & 56 & 60 & 58 & +2 \\
137	chem-mix & MR & 52 & 56 & 54 & +2 \\
138	grow-plant & MR & 64 & 58 & 62 & $-2$ \\
139	\midrule
140	use-therm. & LR & 86 & 79 & 84 & $-2$ \\
141	power-comp. & LR & 79 & 73 & 77 & $-2$ \\
142	find-living & LR & 92 & 85 & 90 & $-2$ \\
143	find-nonliv. & LR & 90 & 83 & 88 & $-2$ \\
144	use-instr. & LR & 83 & 76 & 81 & $-2$ \\
145	move-obj. & LR & 70 & 66 & 68 & $-2$ \\
146	clean & LR & 86 & 79 & 84 & $-2$ \\
147	pick-place & LR & 80 & 75 & 78 & $-2$ \\
148	\bottomrule
149	\end{tabular}
150	\caption{Per-task scores. Int = always-internal, Det = always-deterministic, SG = SimGate. $\Delta$ = SG $-$ Int. Only 4 death-risk tasks show significant gains (all $p < 0.05$); 2 low-risk tasks show significant losses.}
151	\label{tab:pertask}
152	\end{table}
153	
154	Table~\ref{tab:pertask} presents the paper's central diagnostic finding. The 15 task types partition cleanly into two clusters:
155	
156	\paragraph{Death-risk tasks (4/15).} Tasks involving physical state transitions (boiling, melting, freezing, change-of-state) where the LLM backbone systematically hallucinates transition conditions. Internal reasoning produces 70\% agent death rates (e.g., the agent predicts water boils at room temperature and proceeds to act on this incorrect state). Deterministic simulation eliminates these hallucinations, yielding +16 to +29 point gains. The single identified failure mode is \emph{physical state transition hallucination}: the backbone lacks reliable knowledge of temperature thresholds, phase-change rules, and energy conservation.
157	
158	\paragraph{Low-risk tasks (11/15).} Object manipulation, measurement, and classification tasks where Qwen2.5-7B's internal reasoning is sufficient. Deterministic simulation adds latency without benefit and occasionally degrades performance by 2--3 points (the simulator provides ground-truth state but the backbone already reasons correctly, and routing overhead introduces noise).
159	
160	\subsection{Explicit vs.\ Implicit Routing}
161	
162	\begin{table}[t]
163	\centering
164	\small
165	\begin{tabular}{lcccc}
166	\toprule
167	\textbf{Method} & \textbf{All} & \textbf{DR\textsubscript{4}} & \textbf{LR\textsubscript{8}} & \textbf{Sim\%} \\
168	\midrule
169	Explicit (1.7B router) & 65.2 & 38.5 & 81.3 & 38 \\
170	Implicit (backbone) & 64.0 & 36.0 & 82.0 & 34 \\
171	\midrule
172	$\Delta$ & +1.2 & +2.5 & $-0.7$ & +4 \\
173	\bottomrule
174	\end{tabular}
175	\caption{Explicit modular router vs.\ implicit backbone-integrated routing. $\Delta{=}1.2$, 90\% CI $[-2.3, 4.7]$, $p{=}0.38$. Neither architecture is superior.}
176	\label{tab:explicit}
177	\end{table}
178	
179	Table~\ref{tab:explicit} shows that an explicit modular router provides no advantage over training the backbone itself to emit a \texttt{[SIMULATE]} token at labeled steps. The 1.2-point gap is not significant ($p{=}0.38$, 90\% CI $[-2.3, 4.7]$). Per-task analysis reveals no consistent pattern: the explicit router wins on 8 task types, the implicit approach wins on 7.
180	
181	This negative result implies that when the underlying routing signal is noisy (42\% ambiguous labels), architectural choices are second-order. Both approaches converge to the same coarse heuristic: route to simulation when surface-level keywords (temperature, heat, phase-change) are present.
182	
183	\subsection{Ablations}
184	
185	\paragraph{2-way vs.\ 3-way routing.}
186	Collapsing fast-internal and deep-internal into a single ``internal'' class yields 63\% router accuracy (vs.\ 58\% for 3-way) but identical end-to-end performance: 64.8 vs.\ 65.2 ($\Delta{=}0.4$, CI $[-3.1, 3.9]$). Deep chain-of-thought provides no advantage over standard prompting in ScienceWorld, where the bottleneck is factual knowledge of physical rules, not reasoning depth.
187	
188	\paragraph{Router size.}
189	Three router sizes (Qwen2.5-1.5B, Qwen3-1.7B, Qwen2.5-3B) achieve 56--60\% accuracy and 64.0--65.8 overall scores---a 1.8-point range within noise. Performance is bounded by label quality, not model capacity: relevant routing features (physical-state keywords) are surface-level enough for even the smallest model.
190	
191	\begin{table}[t]
192	\centering
193	\small
194	\begin{tabular}{lccc}
195	\toprule
196	\textbf{Router} & \textbf{Params} & \textbf{Acc\%} & \textbf{Score} \\
197	\midrule
198	Qwen2.5-1.5B & 1.5B & 56 & 64.0 \\
199	Qwen3-1.7B & 1.7B & 58 & 65.2 \\
200	Qwen2.5-3B & 3.0B & 60 & 65.8 \\
201	\bottomrule
202	\end{tabular}
203	\caption{Router size ablation. The 4-point accuracy range does not translate to meaningful score differences.}
204	\label{tab:size}
205	\end{table}
206	
207	\paragraph{Cross-task transfer.}
208	We train routers on chemistry-related tasks only and evaluate on physics tasks, and vice versa (Table~\ref{tab:transfer}). Cross-domain accuracy drops substantially (62\%$\to$49\% for chemistry$\to$physics; 55\%$\to$47\% for physics$\to$chemistry), confirming that routing patterns are task-specific surface features, not transferable decision strategies.
209	
210	\begin{table}[t]
211	\centering
212	\small
213	\begin{tabular}{llcc}
214	\toprule
215	\textbf{Train} & \textbf{Eval} & \textbf{Acc\%} & \textbf{Score} \\
216	\midrule
217	Chemistry & Chemistry & 62 & 65.0 \\
218	Chemistry & Physics & 49 & 61.5 \\
219	Physics & Physics & 55 & 63.0 \\
220	Physics & Chemistry & 47 & 60.0 \\
221	All (SimGate) & All & 58 & 65.2 \\
222	\bottomrule
223	\end{tabular}
224	\caption{Cross-task transfer. Router accuracy drops 13--8 points out of domain, confirming task-specific rather than generalizable routing patterns.}
225	\label{tab:transfer}
226	\end{table}
227	
228	\subsection{Router Training Analysis}
229	
230	The router achieves 58\% 3-way validation accuracy (majority-class baseline: 42\%, macro-F1: 0.53). Performance is weakest on the deep-internal class (F1 = 0.39, recall = 0.35), consistent with the finding that deep reasoning rarely outperforms fast reasoning in ScienceWorld. The deterministic class achieves 55\% recall, meaning the router misses 45\% of steps where simulation would help---directly explaining SimGate's 13\% catastrophic failure rate versus always-deterministic's 6.3\%.
231	
232	\section{Discussion}
233	
234	Our results paint a consistent picture: deterministic computation helps LLM agents when and only when the agent faces tasks prone to catastrophic failures from hallucinated physical state transitions. This finding has three implications:
235	
236	\textbf{Per-step routing is the wrong granularity.} SimGate's learned routing ($\approx$always-deterministic) and the lack of episode-phase patterns (early/mid/late-phase simulation rates are 36/39/38\%) both indicate that the simulate-or-not decision is better made at the \emph{task level}. Once a task is identified as death-risk, all steps should use deterministic computation; for other tasks, internal reasoning suffices.
237	
238	\textbf{Routing mechanism matters less than task identification.} Explicit vs.\ implicit routing, 2-way vs.\ 3-way classification, and 1.5B vs.\ 3B routers all produce statistically equivalent results. The bottleneck is identifying \emph{which} task types benefit from simulation, not designing a better router.
239	
240	\textbf{The counterfactual methodology has independent value.} Our fork-and-score approach provides a general framework for diagnosing where LLM reasoning fails and quantifying the value of external computation, applicable beyond ScienceWorld to any environment with available ground-truth oracles.
241	
242	\paragraph{Limitations.}
243	We evaluate on a single environment (ScienceWorld) with one backbone (Qwen2.5-7B). The counterfactual methodology is computationally expensive (35 GPU-hours for trajectory collection alone). Our task-type taxonomy (death-risk/marginal/low-risk) is manually defined; automated task categorization remains future work. We do not evaluate on mathematical reasoning (MATH with code interpreter routing), which may exhibit different task-dependency patterns.
244	
245	\section{Conclusion}
246	
247	We investigated when deterministic computation helps LLM agents through a counterfactual evaluation methodology applied to 15 ScienceWorld task types. Our findings are predominantly negative for per-step routing: learned routing is indistinguishable from always-simulate, explicit and implicit routing architectures perform equivalently, and routing patterns do not transfer across task domains. The positive finding is a sharp characterization of \emph{where} simulation helps: 4 death-risk task types involving physical state transitions account for all gains. We recommend that future work on tool-augmented agents shift from per-step routing to task-level computation planning.
248	
249	\bibliography{custom}
250	
251	\begin{thebibliography}{10}
252	
253	\bibitem{yao2023react}
254	Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.
255	\newblock {ReAct}: Synergizing reasoning and acting in language models.
256	\newblock In \emph{ICLR}, 2023.
257	
258	\bibitem{shinn2023reflexion}
259	Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.
260	\newblock {Reflexion}: Language agents with verbal reinforcement learning.
261	\newblock In \emph{NeurIPS}, 2023.
262	
263	\bibitem{wang2022scienceworld}
264	Ruoyao Wang, Peter Jansen, Marc-Alexandre C\^ot\'e, and Prithviraj Ammanabrolu.
265	\newblock {ScienceWorld}: Is your agent smarter than a 5th grader?
266	\newblock In \emph{EMNLP}, 2022.
267	
268	\bibitem{qiao2024cogrouter}
269	Shuai Qiao, Zhiyu Chen, Yilun Zhao, and Chen Zhao.
270	\newblock {CogRouter}: Cognitive routing for LLM agents.
271	\newblock \emph{arXiv preprint arXiv:2405.XXXXX}, 2024.
272	
273	\bibitem{lu2024itpr}
274	Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu, and Jianfeng Gao.
275	\newblock {ITP-R}: Interactive trajectory planning with reasoning.
276	\newblock \emph{arXiv preprint arXiv:2405.XXXXX}, 2024.
277	
278	\bibitem{feng2024retool}
279	Yifan Feng, Yuhao Chen, and others.
280	\newblock {ReTool}: Reinforcement learning for strategic tool use in LLMs.
281	\newblock \emph{arXiv preprint}, 2024.
282	
283	\bibitem{gou2024tora}
284	Zhibin Gou, Zhihong Shao, Yeyun Gong, and others.
285	\newblock {ToRA}: A tool-integrated reasoning agent.
286	\newblock In \emph{ICLR}, 2024.
287	
288	\bibitem{ross2011dagger}
289	St\'ephane Ross, Geoffrey Gordon, and Drew Bagnell.
290	\newblock A reduction of imitation learning and structured prediction to no-regret online learning.
291	\newblock In \emph{AISTATS}, 2011.
292	
293	\end{thebibliography}
294	
295	\end{document}
296	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d2d9aec-e575-46b7-b41e-cc967921aa3a",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "c94f1abf-a456-424c-875e-26a07fb50542",
  "sourceToolAssistantUUID": "3d2d9aec-e575-46b7-b41e-cc967921aa3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-13T16:18:18.305Z_

<details open><summary>🔧 Tool call — Read · `toolu_016s2kMQTWMkMV1NpZTXejCM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/worst/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c94f1abf-a456-424c-875e-26a07fb50542",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsQwSfN8MHSgEoCT3EG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "283e0da2-299b-46e6-9e23-8ebf526a31a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTXMvQ8eRSC3acn1FuL3MD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 43874,
      "cache_read_input_tokens": 26724,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 43874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 384,
          "cache_read_input_tokens": 26724,
          "cache_creation_input_tokens": 43874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 43874,
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

_source line 47 · 2026-05-13T16:18:18.312Z_

<details><summary>↩ Tool result · `toolu_016s2kMQTWMkMV1NpZTXejCM`</summary>

```text
1	narrative_guidance: 'C1 partially survives but greatly diminished: selective routing
2	  ≈ unconditional simulation (gap 0.4, CI crosses zero), gains concentrated in 4/15
3	  death-risk task types. C2 fails: explicit ≈ implicit (gap 1.2, CI crosses zero).
4	  Original framing ("safety-aware modular routing") cannot hold as primary contribution.
5	  Recommended pivot: Pivot A ("When Does Deterministic Computation Help LLM Agents?").
6	  The strong task-dependency of simulation value (4 death-risk tasks vs 11 low-risk
7	  tasks) becomes the central finding. The negative result on selective vs unconditional
8	  becomes evidence that per-step routing is the wrong granularity. Counterfactual
9	  evaluation methodology + per-task diagnostic analysis provide sufficient contribution
10	  for EMNLP short paper, though Findings is more realistic than Main. Pivot C is secondary
11	  option if reviewer framing favors negative-result papers. Pivot B is weakest given
12	  noisy labels (A4). Key writing strategy: maximize diagnostic analysis depth — per-task
13	  breakdowns, error case studies, failure mode characterization are the paper''s value,
14	  not the method.
15	
16	  '
17	imagined_experiments:
18	- name: Counterfactual trajectory collection (15 task types)
19	  plan_id: plan-001
20	  description: 'Collect 3-modality counterfactual trajectories on 15 ScienceWorld
21	    task types, 20 episodes each. At each step fork into fast-internal, deep-internal,
22	    deterministic; label best modality via hindsight trajectory scoring.
23	
24	    '
25	  expected_results:
26	    total_task_types: 15
27	    episodes_per_task: 20
28	    total_episodes: 300
29	    avg_steps_per_episode: 22
30	    total_labeled_steps: 6600
31	    label_distribution_fast_internal_pct: 42
32	    label_distribution_deep_internal_pct: 22
33	    label_distribution_deterministic_pct: 36
34	    ambiguous_label_rate_margin_lt_5_pct: 42
35	    clear_det_signal_task_count: 4
36	    mixed_signal_task_count: 3
37	    internal_dominant_task_count: 8
38	    gpu_hours_used: 35
39	  result_rationale: 'Qwen2.5-7B 在多数 ScienceWorld 任务上已足够 competent，内部推理仅在物理状态转换任务 (boil/melt/change-state/freeze)
40	    上系统性失败导致 agent death。其余 11 类任务逻辑较简单 (find/move/classify objects)，三种 modality 产生相似
41	    trajectory。结果是 42% 的 step 标签 模糊 (best 与 second-best 差距 < 5 分)。Deep-internal 很少优于
42	    fast-internal，因为 ScienceWorld 中内部推理成功的任务不需要更长 chain-of-thought——瓶颈是物理规则的事实性知识，
43	    不是推理深度。标签信号集中在 death-risk 任务的步骤上，占全部训练数据的 ~27%，其余 73% 基本 是噪声。
44	
45	    '
46	  tables:
47	  - name: Label distribution by task group
48	    columns:
49	    - task_group
50	    - n_tasks
51	    - fast_internal_pct
52	    - deep_internal_pct
53	    - deterministic_pct
54	    - ambiguous_pct
55	    rows:
56	    - - death-risk
57	      - 4
58	      - 18
59	      - 12
60	      - 70
61	      - 22
62	    - - marginal
63	      - 3
64	      - 38
65	      - 24
66	      - 38
67	      - 45
68	    - - low-risk
69	      - 8
70	      - 55
71	      - 25
72	      - 20
73	      - 52
74	    - - overall
75	      - 15
76	      - 42
77	      - 22
78	      - 36
79	      - 42
80	  figures_description:
81	  - 'Per-step score margin (best minus second-best) histogram, 6600 steps. Heavy left
82	    tail: 42% margin < 5。Long right tail (margin > 30) 几乎完全来自 death-risk 任务步骤 (deterministic
83	    阻止 -100 penalty)。Bimodal 分布清晰暴露 label noise 问题。
84	
85	    '
86	  analysis: '高 ambiguity rate 是下游所有失败的根因 (A4)。4 类 death-risk 任务贡献了不成比例的清晰 标签 (70%
87	    deterministic-best, 仅 22% ambiguous)。若仅用这 4 类任务训练 router，accuracy 可能 >75%。问题是
88	    dilution: 73% 训练步骤来自 modality 选择几乎无影响的任务，router 学到的 主要是噪声。可能的补救 (worst tier 未实施):
89	    class-weighted loss、过滤低 margin 样本、 只用高信号步骤训练。
90	
91	    '
92	- name: Router SFT training (Qwen3-1.7B)
93	  plan_id: plan-002
94	  description: 'Fine-tune Qwen3-1.7B on counterfactual labels. 3-way classification:
95	    (history, observation) → {fast-internal, deep-internal, deterministic}. 80/20
96	    stratified split.
97	
98	    '
99	  expected_results:
100	    train_samples: 5280
101	    val_samples: 1320
102	    lr: 2.0e-05
103	    batch_size: 32
104	    epochs: 3
105	    final_train_loss: 0.72
106	    final_val_loss: 0.82
107	    val_accuracy_3way_pct: 58
108	    majority_class_baseline_pct: 42
109	    precision_fast_internal: 0.62
110	    recall_fast_internal: 0.68
111	    precision_deep_internal: 0.45
112	    recall_deep_internal: 0.35
113	    precision_deterministic: 0.58
114	    recall_deterministic: 0.55
115	    f1_macro: 0.53
116	    gpu_hours_used: 6
117	  result_rationale: '58% 3-way accuracy 反映 plan-001 的 noisy label ceiling (A4)。Router
118	    学到的是粗糙近似: 输入含温度/加热/相变关键词 → 路由到 deterministic，否则 → fast-internal。Deep-internal
119	    类 最难学 (recall 仅 35%)，因为它仅在 2-3 类任务的特定 state 下明确优于 fast-internal，样本量 太少。65% 的 deep-internal
120	    误分类流向 fast-internal，确认 fast/deep 区分在 ScienceWorld 中无意义。Val loss 在 epoch 2 后 plateau
121	    (0.82→0.83)，继续训练无益因为瓶颈是标签噪声 而非模型容量。
122	
123	    '
124	  tables:
125	  - name: Per-class router performance
126	    columns:
127	    - class
128	    - precision
129	    - recall
130	    - f1
131	    - support_pct
132	    rows:
133	    - - fast-internal
134	      - 0.62
135	      - 0.68
136	      - 0.65
137	      - 42
138	    - - deep-internal
139	      - 0.45
140	      - 0.35
141	      - 0.39
142	      - 22
143	    - - deterministic
144	      - 0.58
145	      - 0.55
146	      - 0.56
147	      - 36
148	    - - macro-avg
149	      - 0.55
150	      - 0.53
151	      - 0.53
152	      - 100
153	  figures_description:
154	  - 'Train/val loss curves, 3 epochs。Train loss 稳定下降 (0.95→0.72)，val loss 到 epoch
155	    2 趋平 (0.82) 后微升 (0.83)。Gap 小 (0.10) 但 val loss 绝对值高，表明问题是 label noise 而非 overfitting。
156	
157	    '
158	  analysis: 'Deterministic recall 55% 意味着 router 遗漏了 45% 应该 simulate 的步骤——在 death-risk
159	    任务上，这直接导致 ~45% 的致死事件未被拦截，解释了 plan-003 中 SimGate 仍有 13% catastrophic failure rate
160	    (vs always-det 的 6.3%)。若合并 fast/deep 为 2-way，accuracy 可升至 ~63% (plan-006 验证)。
161	
162	    '
163	- name: SimGate end-to-end evaluation
164	  plan_id: plan-003
165	  description: 'End-to-end evaluation: trained router + Qwen2.5-7B backbone on held-out
166	    episodes. Compare against always-internal, always-det, oracle, random, confidence-threshold.
167	    CogRouter (84.6) / ITP-R (62.58) from papers.
168	
169	    '
170	  expected_results:
171	    simgate_score_overall: 65.2
172	    always_internal_overall: 59.5
173	    always_det_overall: 64.8
174	    oracle_routing_overall: 70.0
175	    random_routing_overall: 62.1
176	    confidence_threshold_overall: 63.5
177	    cogrouter_cited: 84.6
178	    itpr_cited: 62.58
179	    simgate_minus_internal: 5.7
180	    simgate_minus_internal_ci90:
181	    - 1.2
182	    - 10.3
183	    simgate_minus_always_det: 0.4
184	    simgate_minus_always_det_ci90:
185	    - -4.8
186	    - 5.6
187	    oracle_minus_always_det: 5.2
188	    oracle_minus_always_det_ci90:
189	    - 1.0
190	    - 9.4
191	    catastrophic_failure_rate_internal_pct: 19.7
192	    catastrophic_failure_rate_simgate_pct: 13.0
193	    catastrophic_failure_rate_det_pct: 6.3
194	    catastrophic_failure_rate_oracle_pct: 4.0
195	    catastrophic_failure_reduction_simgate_vs_internal_pct: 34
196	    router_accuracy_on_eval_pct: 60
197	    simulator_invocation_ratio_pct: 38
198	    task_types_with_significant_simgate_gt_internal: 4
199	    task_types_with_significant_internal_gt_simgate: 2
200	    gpu_hours_used: 14
201	  result_rationale: 'SimGate 65.2 是两个方向力的净效应: (1) 4 类 death-risk 任务上路由到 det 避免 -100
202	    死亡 惩罚带来的大幅提升，(2) 8 类 low-risk 任务上 noisy router 偶尔误路由到 det 导致 2-3 分 损失。净效应勉强超过
203	    always-det (gap 0.4, CI [-4.8, 5.6] 跨零, A2 confirmed)。 关键: 成本结构不对称——safe task
204	    上误路由到 det 代价小 (~5 分)，death-risk task 上未路由 到 det 代价巨大 (-100)。这种不对称使 always-det
205	    成为极强 baseline: 它在 easy task 上 的效率损失远小于它在 death-risk task 上的安全收益。SimGate 的 34%
206	    catastrophic failure reduction vs internal 看似有意义，但 always-det 的 68% reduction
207	    远超 SimGate——router 55% 的 det recall 意味着近一半该拦截的死亡事件漏过。
208	
209	    '
210	  tables:
211	  - name: Main results (ScienceWorld, 15 task types × 20 episodes)
212	    columns:
213	    - method
214	    - overall
215	    - death_risk_4
216	    - marginal_3
217	    - low_risk_8
218	    - sim_inv_pct
219	    - cf_rate_pct
220	    rows:
221	    - - always-internal
222	      - 59.5
223	      - 13.5
224	      - 57.3
225	      - 83.3
226	      - 0
227	      - 19.7
228	    - - always-det
229	      - 64.8
230	      - 45.5
231	      - 58.0
232	      - 77.0
233	      - 100
234	      - 6.3
235	    - - random(50/50)
236	      - 62.1
237	      - 29.5
238	      - 57.7
239	      - 80.1
240	      - 50
241	      - 13.0
242	    - - conf-threshold
243	      - 63.5
244	      - 35.0
245	      - 57.8
246	      - 78.5
247	      - 42
248	      - 10.5
249	    - - SimGate
250	      - 65.2
251	      - 38.5
252	      - 58.0
253	      - 81.3
254	      - 38
255	      - 13.0
256	    - - oracle
257	      - 70.0
258	      - 46.5
259	      - 62.0
260	      - 84.8
261	      - 33
262	      - 4.0
263	    - - CogRouter†
264	      - 84.6
265	      - —
266	      - —
267	      - —
268	      - —
269	      - —
270	    - - ITP-R†
271	      - 62.58
272	      - —
273	      - —
274	      - —
275	      - —
276	      - —
277	  - name: Per-task SimGate breakdown
278	    columns:
279	    - task_type
280	    - group
281	    - internal
282	    - det
283	    - simgate
284	    - oracle
285	    - sig_vs_internal
286	    rows:
287	    - - boil
288	      - death-risk
289	      - 12
290	      - 48
291	      - 40
292	      - 49
293	      - yes (+28)
294	    - - melt
295	      - death-risk
296	      - 8
297	      - 42
298	      - 35
299	      - 43
300	      - yes (+27)
301	    - - change-state
302	      - death-risk
303	      - 14
304	      - 50
305	      - 43
306	      - 51
307	      - yes (+29)
308	    - - freeze
309	      - death-risk
310	      - 20
311	      - 42
312	      - 36
313	      - 43
314	      - yes (+16)
315	    - - mix-paint
316	      - marginal
317	      - 56
318	      - 60
319	      - 58
320	      - 62
321	      - no (+2)
322	    - - chemistry-mix
323	      - marginal
324	      - 52
325	      - 56
326	      - 54
327	      - 58
328	      - no (+2)
329	    - - grow-plant
330	      - marginal
331	      - 64
332	      - 58
333	      - 62
334	      - 66
335	      - no (-2)
336	    - - use-thermometer
337	      - low-risk
338	      - 86
339	      - 79
340	      - 84
341	      - 87
342	      - no (-2)
343	    - - power-component
344	      - low-risk
345	      - 79
346	      - 73
347	      - 77
348	      - 81
349	      - no (-2)
350	    - - find-living
351	      - low-risk
352	      - 92
353	      - 85
354	      - 90
355	      - 93
356	      - sig neg (-2)
357	    - - find-nonliving
358	      - low-risk
359	      - 90
360	      - 83
361	      - 88
362	      - 91
363	      - sig neg (-2)
364	    - - use-instrument
365	      - low-risk
366	      - 83
367	      - 76
368	      - 81
369	      - 85
370	      - no (-2)
371	    - - move-object
372	      - low-risk
373	      - 70
374	      - 66
375	      - 68
376	      - 72
377	      - no (-2)
378	    - - clean
379	      - low-risk
380	      - 86
381	      - 79
382	      - 84
383	      - 87
384	      - no (-2)
385	    - - pick-and-place
386	      - low-risk
387	      - 80
388	      - 75
389	      - 78
390	      - 82
391	      - no (-2)
392	  figures_description:
393	  - 'Grouped bar chart, overall score by method。SimGate (65.2) 与 always-det (64.8)
394	    几乎 等高，两者 90% CI error bars 完全重叠。CogRouter (84.6) 遥遥领先。视觉上 selective routing 的价值不可见。
395	
396	    '
397	  - 'Per-task score comparison (internal vs det vs SimGate), 15 task types sorted
398	    by det-internal gap。清晰 bimodal: 4 个 death-risk tasks 有 30+ 点 gap (占图左侧), 其余 11
399	    个 tasks gap 在 [-8, 4] 之间 (占图右侧)。SimGate 在左侧 track det， 右侧 track internal，但两端都不如对应
400	    baseline。
401	
402	    '
403	  analysis: 'SimGate (65.2) 与 CogRouter (84.6) 的 19.4 分差距部分是 backbone 差异，部分是训练方法 差异
404	    (SFT routing vs CoPO RL)。更致命的是 SimGate 与 always-det 仅差 0.4 分——learned routing
405	    相比 trivial baseline 无增量价值。Oracle 在 70.0 表明即使完美 per-step routing 也只比 always-det
406	    多 5.2 分——per-step routing 在 ScienceWorld 的理论 ceiling 就很低。 去掉 4 类 death-risk 任务，SimGate
407	    (81.3) 反而低于 internal (83.3)，selective routing 在 safe tasks 上有净损失。支持 Pivot A thesis:
408	    deterministic computation 仅在特定 catastrophic-failure-prone task types 有价值，learned
409	    routing 不是正确机制。
410	
411	    '
412	- name: Explicit vs implicit routing ablation
413	  plan_id: plan-004
414	  description: 'Core C2 ablation。Explicit: SimGate router (Qwen3-1.7B)。Implicit: Qwen2.5-7B
415	    backbone trained to output [SIMULATE] at oracle-labeled steps。Same counterfactual
416	    data。
417	
418	    '
419	  expected_results:
420	    explicit_simgate_overall: 65.2
421	    implicit_backbone_overall: 64.0
422	    explicit_minus_implicit: 1.2
423	    explicit_minus_implicit_ci90:
424	    - -2.3
425	    - 4.7
426	    p_value: 0.38
427	    significant: false
428	    explicit_wins_task_count: 8
429	    implicit_wins_task_count: 7
430	    explicit_sim_inv_pct: 38
431	    implicit_sim_inv_pct: 34
432	    gpu_hours_used: 9
433	  result_rationale: 'Explicit ≈ implicit (A3) 因为 routing signal 本身太弱，架构选择无法产生差异。当底层
434	    pattern 是 noisy 的 (42% ambiguous labels)，1.7B 独立 router 和 7B backbone 学到的 都是相同的粗糙
435	    heuristic ("death-risk task → simulate")。7B backbone 有更多 capacity 检测 routing-relevant
436	    features 但同时要管理 action generation 产生干扰；1.7B router 更 focused 但 capacity 受限。两个
437	    trade-off 相消。Per-task 无一致 pattern: explicit 在部分 death-risk tasks 上稍好 (det-routing
438	    更果断)，implicit 在部分 low-risk tasks 上稍好 (backbone 知道自己不需要 simulation)。C2 的核心证据失败。
439	
440	    '
441	  tables:
442	  - name: Explicit vs implicit routing
443	    columns:
444	    - method
445	    - overall
446	    - death_risk_4
447	    - marginal_3
448	    - low_risk_8
449	    - sim_inv_pct
450	    rows:
451	    - - explicit (SimGate 1.7B router)
452	      - 65.2
453	      - 38.5
454	      - 58.0
455	      - 81.3
456	      - 38
457	    - - implicit (backbone [SIMULATE])
458	      - 64.0
459	      - 36.0
460	      - 57.5
461	      - 82.0
462	      - 34
463	    - - delta
464	      - '+1.2'
465	      - '+2.5'
466	      - '+0.5'
467	      - '-0.7'
468	      - '+4'
469	  figures_description:
470	  - 'Per-task scatter: x=explicit score, y=implicit score。Points 紧密聚集在 y=x 对角线 附近，无系统偏离。8
471	    个 task 在 diagonal 上方 (explicit wins), 7 个在下方 (implicit wins)。
472	
473	    '
474	  analysis: 'C2 失败是对 paper framing 冲击最大的结果。没有 explicit > implicit，paper 无法声称 modular
475	    router 的架构贡献。但这个 negative result 在 Pivot A/C 下有价值: 它表明当 deterministic computation
476	    可用时，routing mechanism 的选择不如 WHETHER to route 重要——架构选择是次要的， 实证问题 (何时 simulation
477	    有帮助) 才是核心。对 Pivot C，此结果论证 per-step routing (无论 explicit 或 implicit) 不是正确粒度，支持
478	    trajectory-level 或 subtask-level routing 作为 future work。
479	
480	    '
481	- name: Per-task routing pattern analysis
482	  plan_id: plan-005
483	  description: '分析 plan-003 routing patterns: per-task routing heatmap, episode phase
484	    analysis, failure mode clustering。原定为 paper Figure 1。
485	
486	    '
487	  expected_results:
488	    distinct_routing_clusters: 2
489	    cluster_1_desc: death-risk tasks (4 tasks, >65% det-routing)
490	    cluster_2_desc: all others (11 tasks, 20-45% det-routing, high variance)
491	    phase_pattern_significant: false
492	    early_phase_det_pct: 36
493	    mid_phase_det_pct: 39
494	    late_phase_det_pct: 38
495	    failure_modes_identified: 1
496	    primary_failure_mode: physical state transition hallucination
497	    router_entropy_high_task_count: 11
498	    router_entropy_low_task_count: 4
499	    gpu_hours_used: 1.5
500	  result_rationale: 'A5: routing structure 仅存在于 death-risk/safe 的 binary 划分之上。11/15
501	    task types 的 router 决策高熵 (接近随机)，因为这些任务的训练信号本身 ambiguous。Phase analysis 无显著 时间模式，因为
502	    ScienceWorld 中 death risk 是 state-dependent 而非 phase-dependent—— 危险动作 (如把物体放在加热源上)
503	    可发生在任意 step。唯一可识别的 failure mode (物理状态 转换幻觉) 已在 MVP 中已知；15 task 全量分析未发现新类别。尝试细分
504	    (温度估计/化学反应/ 电学状态) 在每类仅 20 episodes 下无法达到统计显著。
505	
506	    '
507	  tables:
508	  - name: Routing statistics by task group
509	    columns:
510	    - task_group
511	    - n_tasks
512	    - mean_det_routing_pct
513	    - std_det_routing_pct
514	    - mean_router_entropy
515	    rows:
516	    - - death-risk
517	      - 4
518	      - 67
519	      - 8
520	      - 0.62
521	    - - marginal
522	      - 3
523	      - 38
524	      - 12
525	      - 0.91
526	    - - low-risk
527	      - 8
528	      - 25
529	      - 11
530	      - 0.88
531	  figures_description:
532	  - 'Routing heatmap: 15 task types (y) × 3 episode phases (x), color=deterministic
533	    routing frequency。仅底部 4 行 (death-risk) 显示一致 warm colors (>60%)。上部 11 行噪声大， 混合色调，无
534	    phase-dependent pattern。视觉上分为两个色带而非论文需要的 nuanced gradient。 不适合作为 methods paper
535	    的 Figure 1。
536	
537	    '
538	  - 'Router entropy distribution, 15 task types。Bimodal: 4 tasks entropy ~0.62 (有信心
539	    routing), 11 tasks entropy ~0.88-0.91 (接近随机)。无中间 cluster。
540	
541	    '
542	  analysis: 'Routing analysis 同时是 worst tier 最弱和最有价值的结果。弱因为它无法产出 methods paper 需要的
543	    compelling heatmap——pattern 本质上是 binary。但在 Pivot A 下，这个 binary pattern 就是核心 finding:
544	    deterministic computation 有效当且仅当任务涉及 catastrophic failure prone 的物理状态转换。缺乏 phase
545	    pattern 和 failure mode 细粒度进一步支持收益是 task-type-level 而非 step-level。Paper figure
546	    应从 "routing heatmap" 转向 "per-task benefit analysis"——展示 (det - internal) gap per
547	    task type sorted by magnitude，4 个 death-risk tasks 清晰分离。
548	
549	    '
550	- name: 2-way vs 3-way routing ablation
551	  plan_id: plan-006
552	  description: 'Compare {internal, deterministic} vs {fast-internal, deep-internal,
553	    deterministic}。 测试 fast/deep internal 区分是否有价值。
554	
555	    '
556	  expected_results:
557	    two_way_overall: 64.8
558	    three_way_overall: 65.2
559	    delta: 0.4
560	    delta_ci90:
561	    - -3.1
562	    - 3.9
563	    significant: false
564	    two_way_router_accuracy_pct: 63
565	    three_way_router_accuracy_pct: 58
566	    gpu_hours_used: 7
567	  result_rationale: 'Fast/deep 区分在 ScienceWorld 中 negligible，因为内部推理成功的任务不需要更长 CoT——
568	    瓶颈是物理规则的事实性知识而非推理深度。2-way router accuracy 更高 (63% vs 58%) 因为只需学一个决策边界 (simulate-or-not)。但
569	    accuracy 优势不转化为 end-to-end 改善， 因为额外的 deep-internal steps 在 3-way 中影响接近零——它们只增加
570	    tokens 而不改变 action。
571	
572	    '
573	  tables:
574	  - name: 2-way vs 3-way routing
575	    columns:
576	    - scheme
577	    - router_acc_pct
578	    - overall_score
579	    - sim_inv_pct
580	    rows:
581	    - - '{internal, det} 2-way'
582	      - 63
583	      - 64.8
584	      - 40
585	    - - '{fast, deep, det} 3-way'
586	      - 58
587	      - 65.2
588	      - 38
589	  figures_description: []
590	  analysis: '简化 method description (2-way 即可) 但也弱化 "compute-efficient routing" narrative——
591	    router 无法有效区分 cheap/expensive internal reasoning。Paper 中应 collapse 为 2-way， 3-way
592	    作为 appendix ablation。在 Pivot A 下，进一步支持唯一有意义的 routing decision 是 simulate-or-not，且即便如此也仅比
593	    always-simulate 好 0.4 分。
594	
595	    '
596	- name: Boil task rerun with v3 code
597	  plan_id: plan-007
598	  description: '用 clean v3 代码重跑 boil task (无 >= tie-break, 有 proper death filter)，
599	    与其余 14 类任务统一分析基准。
600	
601	    '
602	  expected_results:
603	    boil_internal_mean: -48.2
604	    boil_det_mean: -18.3
605	    boil_oracle_mean: -10.5
606	    boil_det_minus_internal: 29.9
607	    boil_det_minus_internal_ci90:
608	    - 15.0
609	    - 44.8
610	    episodes: 20
611	    death_rate_internal_pct: 70
612	    death_rate_det_pct: 25
613	    gpu_hours_used: 2.5
614	  result_rationale: 'v3 boil 结果与 MVP 一致 (internal -49.8→-48.2, det -19.7→-18.3)。Oracle
615	    显著改善 (-29.7→-10.5) 因为 v3 代码修正了 per-step label composition 逻辑——旧 >= tie-break 在
616	    hindsight labeling 中人为劣化了 oracle labels。Death rate 确认机制: 70% 纯 internal episodes
617	    死亡 (幻觉温度物理), 25% deterministic 仍死亡——这 25% 是 simulation 正确执行 了 action 但 action
618	    本身策略性错误 (simulation 防执行错误不防规划错误)。
619	
620	    '
621	  tables: []
622	  figures_description: []
623	  analysis: '定性确认 MVP finding。Oracle 改善验证了 v3 code fix。此 task 仍是 deterministic simulation
624	    价值的最强证据，但仅是 4/15 类显著获益任务之一。
625	
626	    '
627	- name: Router size ablation
628	  plan_id: plan-008
629	  description: 'Compare Qwen2.5-1.5B / Qwen3-1.7B / Qwen2.5-3B 作为 router。测试 router
630	    capacity 敏感性。
631	
632	    '
633	  expected_results:
634	    qwen25_1_5b_accuracy_pct: 56
635	    qwen3_1_7b_accuracy_pct: 58
636	    qwen25_3b_accuracy_pct: 60
637	    qwen25_1_5b_overall_score: 64.0
638	    qwen3_1_7b_overall_score: 65.2
639	    qwen25_3b_overall_score: 65.8
640	    accuracy_range_pct: 4
641	    score_range: 1.8
642	    gpu_hours_used: 11
643	  result_rationale: '三种 size 表现在噪声范围内，因为瓶颈是 label quality 而非 model capacity (A4)。4
644	    点 accuracy 差 (56→60%) 不转化为有意义的 end-to-end 分差 (1.8 分范围)，因为更大 router 多正确分类的步骤主要在
645	    low-risk tasks 上——那里 modality 选择影响 negligible。在 death-risk tasks 上 (正确分类 impact
646	    大) 三种 size accuracy 相近 (~62-65%)，因为 surface features (temperature/heat/phase-change
647	    keywords) 对最小模型也足够显著。
648	
649	    '
650	  tables:
651	  - name: Router size comparison
652	    columns:
653	    - router
654	    - params
655	    - accuracy_3way_pct
656	    - overall_score
657	    - death_risk_4_score
658	    rows:
659	    - - Qwen2.5-1.5B
660	      - 1.5B
661	      - 56
662	      - 64.0
663	      - 36.5
664	    - - Qwen3-1.7B
665	      - 1.7B
666	      - 58
667	      - 65.2
668	      - 38.5
669	    - - Qwen2.5-3B
670	      - 3B
671	      - 60
672	      - 65.8
673	      - 39.0
674	  figures_description: []
675	  analysis: '支持 "lightweight router suffices" 但原因错误: 所有 size 都被 label noise 瓶颈限制，
676	    不是因为小 router 已 sufficient。Reviewer 可能指出这只是 trivially 验证了小 router 选择。 Paper 中应表述为:
677	    ScienceWorld routing 问题是 feature-limited (relevant signals 是 surface-level keywords)
678	    而非 capacity-limited。
679	
680	    '
681	- name: MATH track — code interpreter routing
682	  plan_id: plan-009
683	  description: '500 Level 4-5 MATH problems, 3-way routing (fast-internal / deep-internal
684	    / code-interpreter). Demonstrates generalization beyond environment simulators.
685	
686	    '
687	  expected_results:
688	    status: not_attempted
689	    reason: 'ScienceWorld 结果偏弱且 deadline 仅剩 ~4 天，20 GPU hours + 3 天实验成本不合理。 Selective
690	      routing ≈ always-det 的结论可能在 MATH 上重现 (code interpreter 已被 ReTool/ToRA 充分研究，routing
691	      contribution 太弱无法差异化)。
692	
693	      '
694	  result_rationale: '资源重新分配至最大化 ScienceWorld 分析深度。Pivot A ("When Does Deterministic
695	    Computation Help?") 框架下，单 domain 深入 (15 task types) 比浅层双 domain 更有价值。MATH 可作 future
696	    work 提及。
697	
698	    '
699	  tables: []
700	  figures_description: []
701	  analysis: '不跑 MATH 是 worst tier 下正确的资源分配。若 paper pivot 到 Pivot A，单 domain 的 diagnostic
702	    depth 是核心贡献; 加入 MATH 会稀释 analysis 焦点且可能产生另一组 ambiguous 结果。
703	
704	    '
705	- name: Cross-task transfer within ScienceWorld
706	  plan_id: plan-010
707	  description: 'Train router on chemistry tasks only → evaluate on physics tasks (vice
708	    versa). 测试 routing patterns 的跨 domain 迁移性。
709	
710	    '
711	  expected_results:
712	    chemistry_within_domain_accuracy_pct: 62
713	    physics_within_domain_accuracy_pct: 55
714	    chemistry_to_physics_accuracy_pct: 49
715	    physics_to_chemistry_accuracy_pct: 47
716	    chemistry_to_physics_overall_score: 61.5
717	    physics_to_chemistry_overall_score: 60.0
718	    random_baseline_accuracy_pct: 33
719	    gpu_hours_used: 4
720	  result_rationale: 'Cross-task transfer 失败因为 router 学到的是 task-specific surface features
721	    而非 transferable routing patterns。Chemistry 路由依赖 keywords (temperature, heat, boil,
722	    substance) 不出现在 physics tasks (circuit, voltage, connect)；router 的 learned features
723	    跨词汇域不泛化。Chemistry→physics 降至 49% (高于 random 33% 但远低于 within-domain 62%)， 说明 router
724	    捕捉了少量 domain-general 信号 (如 "agent 即将改变物理状态") 但大部分 accuracy 来自 domain-specific
725	    lexical matching。Physics→chemistry 更差 (47%) 因为 physics tasks 整体 routing signal
726	    更弱 (within-domain 仅 55%)。
727	
728	    '
729	  tables:
730	  - name: Cross-task transfer matrix
731	    columns:
732	    - train_domain
733	    - eval_domain
734	    - accuracy_pct
735	    - overall_score
736	    rows:
737	    - - chemistry
738	      - chemistry
739	      - 62
740	      - 65.0
741	    - - chemistry
742	      - physics
743	      - 49
744	      - 61.5
745	    - - physics
746	      - physics
747	      - 55
748	      - 63.0
749	    - - physics
750	      - chemistry
751	      - 47
752	      - 60.0
753	    - - all (SimGate)
754	      - all
755	      - 58
756	      - 65.2
757	  figures_description: []
758	  analysis: 'Poor transfer 与 A5 一致 (routing structure 不超越 task identity)。在 Pivot A
759	    下， 此结果强化 thesis: routing to deterministic computation 是 task-dependent phenomenon，
760	    不是 learnable general skill。Router 必须被 told (或从每种 specific failure mode 的 examples
761	    中 learn) 它应拦截什么。Motivates future work on meta-learning or few-shot routing。'
762	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "283e0da2-299b-46e6-9e23-8ebf526a31a8",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "9caf4519-9633-413b-a771-0706c06258e3",
  "sourceToolAssistantUUID": "283e0da2-299b-46e6-9e23-8ebf526a31a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-13T16:18:25.212Z_

Now I have complete understanding of both scenarios. The task prompt describes the "worst" scenario paper. Let me also check the experiment_plan.yaml for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9caf4519-9633-413b-a771-0706c06258e3",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsRvrDvePGrCL3VbEXU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "393bf0c4-0721-4e30-9c4a-a1ec492bb65c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U966WPxTdECHSaoCrzqyG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18662,
      "cache_read_input_tokens": 70598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18662,
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

_source line 49 · 2026-05-13T16:18:28.279Z_

<details open><summary>🔧 Tool call — Read · `toolu_014CGFRxndckKaFkEgHA3WDb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "393bf0c4-0721-4e30-9c4a-a1ec492bb65c",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsRvrDvePGrCL3VbEXU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93cd4aa7-5a69-4b5d-8bdd-7a52795ea74e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U966WPxTdECHSaoCrzqyG5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18662,
      "cache_read_input_tokens": 70598,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18662
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 70598,
          "cache_creation_input_tokens": 18662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18662,
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

_source line 50 · 2026-05-13T16:18:28.372Z_

<details><summary>↩ Tool result · `toolu_014CGFRxndckKaFkEgHA3WDb`</summary>

```text
1	# SimGate Experiment Plan
2	# Generated: 2026-05-13 post-MVP
3	# Updated: 2026-05-13 Reviewer W1-W5 incorporated
4	# Claims reference: paper_framing.md C1, C2
5	
6	experiments:
7	  # === P0: Must-do for paper submission ===
8	
9	  - id: plan-001a
10	    claim: [C1]
11	    description: >
12	      Mini signal detection (pre-screening). Run 5 episodes per candidate task type
13	      (2-way: internal + deterministic only) to identify which tasks show det > internal signal.
14	      Screen ~20 ScienceWorld task types, keep those with positive effect direction.
15	      ~30min per task type, ~10h total for 20 types on dual GPU.
16	    priority: P0
17	    gpu_budget_hours: 10
18	    deps: []
19	    notes: >
20	      Reviewer W3: avoid wasting GPU on no-signal tasks like grow-plant.
21	      MVP task types (boil, melt, change-state, mix-paint) auto-pass.
22	      grow-plant confirmed no-signal (control). Target: identify 10-15 task types with signal.
23	
24	  - id: plan-001b
25	    claim: [C1, C2]
26	    description: >
27	      Full counterfactual trajectory collection on signal-positive task types from plan-001a.
28	      2-way collection: internal + deterministic (per Reviewer W2).
29	      20 episodes each, max_steps=30. At each step, execute both modalities
30	      and record which leads to best eventual task score via hindsight labeling.
31	      Output: (state, observation, best_modality) triples for router SFT.
32	    priority: P0
33	    gpu_budget_hours: 25
34	    deps: [plan-001a]
35	    notes: >
36	      Reviewer W2: collect 2-way first, consistent with MVP. Skip fast/deep-internal
37	      distinction until plan-006 confirms 3-way adds value.
38	      GPU savings: ~33% vs original 3-way plan (25h vs 40h).
39	      vLLM backend on both GPUs for speed.
40	
41	  - id: plan-002
42	    claim: C2
43	    description: >
44	      Router SFT training. Fine-tune Qwen3-1.7B on counterfactual labels from plan-001b.
45	      Cross-entropy loss, (history, observation) → {internal, deterministic}.
46	      Train/val split by task type (leave-one-out or 80/20).
47	    priority: P0
48	    gpu_budget_hours: 8
49	    deps: [plan-001b]
50	    notes: >
51	      Follow ARES training pipeline. Single GPU sufficient.
52	      Hyperparams: lr=2e-5, batch=32, epochs=3, max_seq_len=2048.
53	      2-way classification (not 3-way) per W2 decision.
54	
55	  - id: plan-003
56	    claim: C1
57	    description: >
58	      SimGate end-to-end evaluation on ScienceWorld.
59	      Run trained router + Qwen2.5-7B backbone on held-out episodes.
60	      Compare against: always-internal, always-deterministic, oracle-routing,
61	      random-routing, confidence-threshold heuristic.
62	      Report: continuous score (CogRouter protocol), success rate, catastrophic failure rate,
63	      simulator invocation ratio, total LLM tokens.
64	      KEY: This confirms/denies C1's "selective > unconditional" sub-claim (Reviewer W1).
65	    priority: P0
66	    gpu_budget_hours: 15
67	    deps: [plan-002]
68	    notes: >
69	      CogRouter (84.6) and ITP-R (62.58) cited from papers, not reproduced.
70	      Bootstrap 90% CI on all comparisons. Per-task-type breakdown.
71	      If trained router ≤ always-det, C1 downgrades per paper_framing.md note.
72	
73	  - id: plan-004
74	    claim: C2
75	    description: >
76	      Explicit vs implicit routing ablation (parameter-controlled).
77	      Three conditions:
78	      (a) 1.7B explicit router (SimGate) — Qwen3-1.7B, separate module
79	      (b) 1.7B implicit router — Qwen3-1.7B SFT'd to output [SIMULATE] token inline
80	      (c) 7B implicit routing — Qwen2.5-7B backbone decides via tool-use prompt
81	      All trained on same counterfactual data from plan-001b.
82	      Condition (b) is the parameter-matched control (Reviewer W4).
83	    priority: P0
84	    gpu_budget_hours: 12
85	    deps: [plan-001b]
86	    notes: >
87	      Reviewer W4: 7B implicit vs 1.7B explicit confounds architecture with capacity.
88	      Adding 1.7B implicit isolates explicit vs implicit architectural effect.
89	      Can run in parallel with plan-002 on second GPU.
90	
91	  - id: plan-005
92	    claim: [C1, C2]
93	    description: >
94	      Per-task routing pattern analysis.
95	      From plan-003 outputs, analyze: (a) which task categories trigger deterministic routing most,
96	      (b) at which episode phases (early/mid/late) routing decisions concentrate,
97	      (c) router-as-diagnostic-probe — cluster deterministic-routing steps to identify
98	      systematic LLM failure modes (e.g., multi-step physical reasoning failures).
99	      Output: routing heatmap figure + failure mode taxonomy.
100	    priority: P0
101	    gpu_budget_hours: 2
102	    deps: [plan-003]
103	    notes: Analysis-only, minimal GPU. Main output is Figure 1 for the paper.
104	
105	  # === P1: Important, do if time permits ===
106	
107	  - id: plan-006
108	    claim: C2
109	    description: >
110	      2-way vs 3-way routing ablation.
111	      Supplement plan-001b data with deep-internal modality on subset of tasks.
112	      Compare {internal, deterministic} vs {fast-internal, deep-internal, deterministic}.
113	      Tests whether the fast/deep internal distinction adds value beyond binary routing.
114	    priority: P1
115	    gpu_budget_hours: 10
116	    deps: [plan-002]
117	    notes: >
118	      If 3-way > 2-way, retrain router as 3-way and update paper.
119	      If 2-way ≈ 3-way, simplifies the story (binary routing suffices).
120	      Requires supplemental trajectory data for deep-internal (~5h additional collection).
121	
122	  - id: plan-007
123	    claim: C1
124	    description: >
125	      Boil task rerun with v3 code.
126	      MVP boil data used old code (>= tie-break, death filter on all 3 modes).
127	      Rerun with clean v3 code for unified analysis.
128	    priority: P1
129	    gpu_budget_hours: 3
130	    deps: []
131	    notes: Can run in parallel with plan-001a as first batch.
132	
133	  - id: plan-008
134	    claim: C2
135	    description: >
136	      Router size ablation. Compare Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B as router.
137	      Tests sensitivity to router capacity.
138	    priority: P1
139	    gpu_budget_hours: 12
140	    deps: [plan-001b]
141	    notes: >
142	      Important for "lightweight" claim. If 1.5B matches 1.7B, strengthens "small router suffices".
143	      Low priority relative to core experiments.
144	
145	  # === P2: Nice to have / Future work material ===
146	
147	  - id: plan-009
148	    claim: C1
149	    description: >
150	      MATH track — code interpreter as deterministic oracle.
151	      500 Level 4-5 MATH problems. 2-way routing: internal / code-interpreter.
152	      Demonstrates generalization beyond environment simulators.
153	    priority: P2
154	    gpu_budget_hours: 20
155	    deps: [plan-002]
156	    notes: >
157	      Human Review Note suggested MATH as secondary track.
158	      Only if ScienceWorld experiments finish by Day 8.
159	
160	  - id: plan-010
161	    claim: C2
162	    description: >
163	      Cross-task transfer within ScienceWorld.
164	      Train router on chemistry tasks only, evaluate on physics tasks (and vice versa).
165	      Tests whether routing patterns transfer across task domains.
166	    priority: P2
167	    gpu_budget_hours: 5
168	    deps: [plan-002]
169	
170	# === Summary (post-Reviewer revision) ===
171	# P0 total: ~72 GPU-hours (plan-001a 10h + plan-001b 25h + plan-002 8h + plan-003 15h + plan-004 12h + plan-005 2h)
172	# P1 total: ~25 GPU-hours (plan-006 10h + plan-007 3h + plan-008 12h)
173	# P2 total: ~25 GPU-hours (plan-009 20h + plan-010 5h)
174	# Grand total: ~122 GPU-hours
175	# All estimates in RTX 5090 32GB wall-clock hours (Reviewer W5)
176	#
177	# Critical path: plan-001a (10h) → plan-001b (25h) → plan-002 (8h) → plan-003 (15h) → plan-005 (2h)
178	# = ~60h sequential, ~2.5 days with 2 GPUs running in parallel
179	# plan-004 runs parallel with plan-002/003 on second GPU
180	# plan-007 runs parallel with plan-001a
181	#
182	# Key changes from v1:
183	# - plan-001 split into 001a (pre-screening) + 001b (full collection) per Reviewer W3
184	# - 2-way collection first (not 3-way) per Reviewer W2, saves ~33% GPU time
185	# - plan-004 adds 1.7B implicit control per Reviewer W4
186	# - GPU budget unit: RTX 5090 32GB hours (not H100) per Reviewer W5
187	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93cd4aa7-5a69-4b5d-8bdd-7a52795ea74e",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "ab0cde6016829d46f",
  "type": "user",
  "uuid": "2b025f6a-8fd0-4867-89a3-903823f2f264",
  "sourceToolAssistantUUID": "93cd4aa7-5a69-4b5d-8bdd-7a52795ea74e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-13T16:20:01.029Z_

I now have complete information to write a thorough review of the "worst" scenario paper. Let me now compose the review.

---

## Review: "When Does Deterministic Computation Help LLM Agents? A Diagnostic Study on ScienceWorld"

### 1. Summary

This paper introduces a counterfactual evaluation methodology that forks agent trajectories at each decision step across three computation modalities (fast-internal, deep chain-of-thought, deterministic simulation) and labels optimal per-step choices via hindsight scoring. Applied to 15 ScienceWorld task types (300 episodes, 6,600 labeled steps), the study finds that deterministic computation helps only on 4 death-risk task types involving physical state transitions (+16--29 points), while learned per-step routing (SimGate) is statistically indistinguishable from always-simulate (delta=0.4, CI crosses zero). Explicit and implicit routing architectures perform equivalently, and routing patterns do not transfer across task domains.

### 2. Strengths

**S1. Well-designed counterfactual methodology.** The fork-and-score approach for labeling optimal modality per step is a sound causal identification strategy. Forking the trajectory at each step and rolling out to episode completion provides hindsight labels grounded in actual outcomes rather than proxy metrics. This methodology has clear independent value beyond the specific SimGate application.

**S2. Honest negative results with appropriate statistical reporting.** The paper reports bootstrap 90% CIs for all key comparisons and correctly identifies that SimGate vs. always-det (delta=0.4, CI [-4.8, 5.6]) and explicit vs. implicit (delta=1.2, p=0.38, CI [-2.3, 4.7]) are not significant. Many papers in this space would cherry-pick subsets or change framing to hide such results. The candid reporting is commendable.

**S3. Comprehensive ablation coverage.** The paper evaluates 2-way vs. 3-way routing, three router sizes, cross-task transfer, and per-task diagnostics. For a short paper, this is thorough. Each ablation reinforces a consistent narrative: the bottleneck is label quality and task-level signal, not routing architecture or model capacity.

**S4. Clean per-task diagnostic finding.** The sharp partition into 4 death-risk tasks (where deterministic computation provides large gains) and 11 other tasks (where it does not) is the paper's most valuable contribution. The correlation between death-risk and simulation value is convincing, and the recommendation to shift from per-step to task-level routing decisions follows naturally from the evidence.

**S5. Controlled baselines.** The inclusion of random routing, confidence-threshold heuristic, always-internal, always-deterministic, and oracle routing provides a comprehensive baseline landscape. This makes it possible to assess the practical value of learned routing against both trivial and idealized alternatives.

### 3. Weaknesses

**W1. Circularity in the oracle construction undermines the central negative claim.** The oracle is computed via 1-step hindsight scoring, but ScienceWorld has sparse rewards -- 95% of steps yield zero score change. Under the strict > tie-break rule (adopted in v3 code), the oracle defaults to deterministic whenever delta=0 and only switches to internal when internal is strictly better. This means the oracle itself is biased toward always-deterministic behavior, making the finding that "SimGate approximately equals always-det" almost tautological: the router was trained on labels that are themselves approximately always-det. The paper does not adequately discuss this circularity or attempt multi-step rollout labeling.

**W2. 42% label ambiguity is presented as a finding but is actually a methodological limitation.** The paper correctly identifies that 42% of labels have <5-point margins, but treats this as a discovery about the task structure rather than a potential flaw in the labeling methodology. Alternative labeling strategies (trajectory-level scoring with longer rollouts, N-step returns, or episode-terminal reward propagation) might produce less ambiguous labels. The paper does not experiment with any alternative label computation methods, making it impossible to distinguish "routing genuinely doesn't matter on these tasks" from "our labeling method is too noisy to detect when routing matters."

**W3. Single backbone, single environment, limited scale.** All results use Qwen2.5-7B on ScienceWorld. The conclusion that "per-step routing is the wrong granularity" may not generalize to weaker backbones (where more steps would benefit from external computation) or to environments with denser rewards (where step-level routing signals would be clearer). The MATH track (plan-009) was not attempted, removing the only opportunity to test generalization. For a paper whose primary contribution is a negative claim about per-step routing, the evidentiary base is narrow.

**W4. The "always-det is a strong baseline" argument is incomplete.** Always-det scores 77.0 on low-risk tasks vs. 83.3 for always-internal -- a 6.3-point penalty on 8/15 task types. The paper frames this as a small cost, but for a practitioner choosing deployment strategy, a 6-point degradation on the majority of tasks is not negligible. The paper does not report computational cost differences (simulator invocation overhead, tokens saved, latency) that would complete the practical comparison. Sim% is reported but not translated into wall-clock time or cost.

**W5. Per-task scores show suspicious uniformity.** In Table 3, all 8 low-risk tasks show exactly -2 delta (SimGate minus Internal). This perfect uniformity across 8 diverse task types (use-thermometer, power-component, find-living, etc.) is statistically implausible given 20 episodes per task with bootstrap variance. It suggests either (a) a systematic artifact in how SimGate degrades on non-death-risk tasks, or (b) rounded/approximated results. If (a), this systematic pattern deserves investigation; if (b), exact numbers should be reported.

**W6. Router training details are insufficient for reproducibility.** The paper mentions SFT on Qwen3-1.7B with lr=2e-5, batch=32, 3 epochs, but does not report: input format (how history/observation are tokenized), max sequence length, optimizer, weight decay, warmup, or the prompt template. For a paper whose contribution hinges on the router's performance, these details are critical. The 58% 3-way accuracy may be an artifact of suboptimal training rather than a fundamental label noise ceiling.

**W7. Inconsistency between pre-screening and final task taxonomy.** The paper screens 20 task types in pre-screening but evaluates on 15 in the main experiments. Which 5 were dropped, and why? The death-risk/marginal/low-risk taxonomy appears post-hoc. If the taxonomy was defined before seeing results, the paper should state this clearly; if after, this is a form of data dredging that could inflate the apparent sharpness of the death-risk/non-death-risk divide.

**W8. CogRouter comparison is misleading.** CogRouter (84.6) is cited without acknowledging that it uses a fundamentally different training paradigm (RL with CoPO), different backbone configuration, and possibly different ScienceWorld version/task splits. The 19.4-point gap makes SimGate look ineffective, but the comparison is not apples-to-apples. The paper should either reproduce CogRouter under identical conditions or relegate it to a footnote rather than including it in the main results table.

### 4. Questions to Authors

**Q1.** What happens if you train the router exclusively on the 4 death-risk task types? You note that 73% of training steps come from tasks where modality choice has negligible impact. Have you tried filtering the training data to high-signal steps only, or using class-weighted loss? This seems like an obvious intervention that could substantially change the negative results.

**Q2.** Can you explain the exact mechanism by which all 8 low-risk tasks show exactly delta=-2? Is this rounded? If exact, what is the bootstrap CI for each of these individual task-level deltas?

**Q3.** You report 1-step hindsight scoring for counterfactual labels. Have you considered N-step rollout (e.g., 3-step or 5-step) to provide denser signal? The sparse reward issue is acknowledged but no remediation is attempted.

**Q4.** The oracle routing scores 70.0 overall. What is the oracle's simulator invocation rate? If the oracle also routes to deterministic on most steps (due to tie-breaking), this would confirm W1's circularity concern.

**Q5.** Why were the marginal-risk tasks (mix-paint, chemistry-mix, grow-plant) grouped separately from low-risk? Their delta range (+2, +2, -2) overlaps with low-risk. What is the principled criterion for the 3-group taxonomy?

**Q6.** The paper claims routing patterns are "task-specific surface features" based on cross-task transfer results. But cross-task accuracy (47-49%) is well above random (33%). This suggests some transferable signal exists. Have you analyzed what transfers and what doesn't?

### 5. Missing Experiments

Comparing against the planned experiments in the YAML:

- **plan-001 (Counterfactual trajectory collection)**: COVERED. 15 task types, 300 episodes, 6,600 steps.
- **plan-002 (Router SFT training)**: COVERED. Qwen3-1.7B, 3-way classification.
- **plan-003 (SimGate E2E evaluation)**: COVERED. Full baseline comparison.
- **plan-004 (Explicit vs. implicit ablation)**: COVERED. But only 2 conditions (explicit 1.7B vs. implicit 7B backbone). The planned parameter-matched condition (1.7B implicit SFT) is not reported, making the ablation confounded by model size.
- **plan-005 (Per-task routing pattern analysis)**: PARTIALLY COVERED. Per-task breakdown and routing statistics are reported. However, the planned routing heatmap figure, phase analysis, and entropy distribution are described in text but no figures are shown. The phase analysis shows no significant pattern (36/39/38%), which is reported but the figure that would make this visually compelling is missing.
- **plan-006 (2-way vs. 3-way ablation)**: COVERED. Delta=0.4, not significant.
- **plan-007 (Boil task rerun with v3 code)**: NOT EXPLICITLY REPORTED as a separate validation. Boil is included in the per-task results, but there is no table comparing v3 vs. MVP code to demonstrate data quality control. This is a missed opportunity to show methodological rigor.
- **plan-008 (Router size ablation)**: COVERED. Three sizes, 1.8-point range.
- **plan-009 (MATH track)**: NOT ATTEMPTED. Acknowledged in limitations. This is the most significant missing experiment -- the paper's conclusions about per-step routing being "the wrong granularity" would be far more convincing with evidence from a second domain.
- **plan-010 (Cross-task transfer)**: COVERED. Chemistry-physics cross-domain.

**Additional missing experiments:**
- No error analysis or qualitative examples of routing decisions (correct vs. incorrect).
- No analysis of what the router has learned internally (attention patterns, feature importance).
- No evaluation with a weaker backbone model, which could reveal whether routing value increases when the LLM is less capable.

### 6. Soundness Rating: 3/5

The counterfactual methodology is conceptually sound, and the statistical reporting is appropriate. However, the 1-step hindsight labeling in a sparse-reward environment creates a fundamental circularity (W1) that undermines the central negative claim. The suspiciously uniform -2 deltas across all low-risk tasks (W5) raise data quality concerns. The missing parameter-matched implicit routing condition (W6/plan-004) leaves a confound in the explicit-vs-implicit comparison. The negative results are plausible but not convincingly established given these methodological gaps.

### 7. Overall Score: 3/6 (Weak Reject)

The paper presents a useful counterfactual methodology and an honest account of negative results, which are both valuable. However, the negative claims are not convincingly established because the labeling methodology's limitations (sparse rewards, 1-step hindsight, 42% ambiguity) are conflated with genuine properties of the routing problem. The paper does not attempt obvious interventions (filtered training data, multi-step rollouts, class-weighted loss) that could change the conclusions. The single-environment, single-backbone evaluation base is too narrow for the sweeping claim that "per-step routing is the wrong granularity." The strongest finding -- that simulation value is concentrated in death-risk task types -- is interesting but incremental: it amounts to saying "LLMs fail at physics, simulators don't." This is well-known and could be established with far less machinery. For EMNLP main conference (25% acceptance rate), the contribution does not clear the bar, though with the interventions described above, a strengthened version could be suitable for Findings.

### 8. Confidence: 4/5

I am confident in this assessment. I have carefully read the paper, the review context including all planned experiments and their expected results, the experimental methodology decisions (v3 code corrections, tie-breaking rules), and the project's internal deliberations. The main uncertainty in my evaluation is whether the suspicious uniformity in low-risk task deltas reflects a genuine artifact or merely aggressive rounding, and whether multi-step rollout labeling would materially change the results. Both are empirically resolvable questions that the authors should address.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b025f6a-8fd0-4867-89a3-903823f2f264",
  "isSidechain": true,
  "agentId": "ab0cde6016829d46f",
  "requestId": "req_011CazsSfvpK6a4cmBqrmJPD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0ce54ec-c4fc-48d6-954f-017cbd4d67da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZXGESCzi2qrKyKQrRMmDi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 89260,
      "output_tokens": 3222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2976
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3222,
          "cache_read_input_tokens": 89260,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2976,
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
