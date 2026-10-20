# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Y

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8fbc54ecf55e0717.jsonl`
- **Structured JSON:** [`8889571912e8222ce51d.json`](../../sessions/88/8889571912e8222ce51d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-13T16:17:46.644Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus: **Novelty and Related Work**.

## Paper Summary

**Title**: "When Does Deterministic Computation Help LLM Agents? A Diagnostic Study on ScienceWorld"

**Core idea**: Introduces counterfactual evaluation methodology that forks agent trajectories at each decision step across three computation modalities (fast internal, deep CoT, deterministic simulation). Applied to 15 ScienceWorld task types (300 episodes, 6,600 steps). Main findings are negative: learned per-step routing ≈ always-simulate; explicit ≈ implicit routing; routing patterns don't transfer. Positive finding: deterministic computation helps only on 4/15 death-risk task types involving physical state transitions.

**Claimed contributions**:
1. A counterfactual evaluation methodology (fork trajectories → hindsight scoring → label optimal modality per step)
2. Per-task diagnostic analysis showing simulation value is sharply task-dependent (4/15 tasks)

**Related work discussed in paper** (8 references):
- [1] ReAct (Yao et al., ICLR 2023) — reasoning + acting
- [2] Reflexion (Shinn et al., NeurIPS 2023) — verbal reinforcement learning
- [3] ScienceWorld (Wang et al., EMNLP 2022) — benchmark
- [4] CogRouter (Qiao et al., 2024) — RL-based routing, 84.6 on ScienceWorld
- [5] ITP-R (Lu et al., 2024) — routes to LLM world model, 62.58
- [6] ReTool (Feng et al., 2024) — RL for tool use
- [7] ToRA (Gou et al., ICLR 2024) — tool-integrated reasoning
- [8] DAgger (Ross et al., AISTATS 2011) — imitation learning

Note: References [4] and [5] have placeholder arXiv IDs (arXiv:2405.XXXXX).

**Key results**:
- SimGate (65.2) vs always-det (64.8): Δ=0.4, not significant
- Explicit vs implicit routing: Δ=1.2, p=0.38, not significant
- CogRouter† (84.6) cited but uses different backbone/training — 19.4 point gap
- Only single environment (ScienceWorld), single backbone (Qwen2.5-7B)

**Paper structure**: 6 pages. Abstract, Introduction, Method (SimGate framework, counterfactual methodology, router training), Experiments (label analysis, main results, per-task diagnostics, explicit vs implicit, ablations, router training analysis), Discussion, Conclusion.

**Framing**: The paper was pivoted from "safety-aware modular routing" (original method paper) to "When Does Deterministic Computation Help?" (diagnostic/negative-result paper). The pivot was driven by weak results: the proposed routing method provides no advantage over always-simulate.

## Your Review Task

Provide a structured review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (novelty + related work focus)
3. **Weaknesses** (novelty + related work focus)
4. **Questions to authors**
5. **Novelty assessment**: Is the counterfactual methodology genuinely novel? Is the negative-result framing a sufficient contribution? How does this compare to existing work on tool-use routing, computation allocation, and negative-result studies?
6. **Related work gaps**: What important related work is missing? Consider: adaptive computation (early exit, mixture of experts), tool-use learning (Toolformer, ART), world models for agents (DreamerV3, IRIS), safe RL / constrained agents, other routing/gating mechanisms.
7. **Significance rating** (1-5)
8. **Overall score** (1-6 scale)
9. **Confidence** (1-5)

Be rigorous. Evaluate: Does this paper advance the field? Is the negative result informative or expected? Is the framing honest about the limitations? Are the contributions sufficient for a top venue?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "b81e4f72-443b-49e1-b7cd-24cec18a2c83",
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

_source line 2 · 2026-05-13T16:17:46.648Z_

```json
{
  "parentUuid": "b81e4f72-443b-49e1-b7cd-24cec18a2c83",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
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
  "uuid": "6855fb12-a007-4e6a-b9c9-7e99454a80b5",
  "timestamp": "2026-05-13T16:17:46.648Z",
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

_source line 3 · 2026-05-13T16:17:50.210Z_



I'll start by reading the actual paper and any related project files to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6855fb12-a007-4e6a-b9c9-7e99454a80b5",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsPbUbRzrJ1RPbAtmiA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "252f6803-ec17-4970-bc7a-3864ad5be064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJKWAxdQpUjb57Ct2sAbhJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6855,
      "cache_read_input_tokens": 8251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6855,
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

_source line 4 · 2026-05-13T16:17:51.441Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0131YpniuptQzrz4CajvJxQf`</summary>

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
  "parentUuid": "252f6803-ec17-4970-bc7a-3864ad5be064",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsPbUbRzrJ1RPbAtmiA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32e9b561-5b36-4bdc-b264-8e2dc6f5e12b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJKWAxdQpUjb57Ct2sAbhJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6855,
      "cache_read_input_tokens": 8251,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6855
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 8251,
          "cache_creation_input_tokens": 6855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6855,
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

_source line 5 · 2026-05-13T16:17:51.445Z_

<details><summary>↩ Tool result · `toolu_0131YpniuptQzrz4CajvJxQf`</summary>

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
  "parentUuid": "32e9b561-5b36-4bdc-b264-8e2dc6f5e12b",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "a9de065d-5fe2-412e-99a3-7f53c227c09e",
  "sourceToolAssistantUUID": "32e9b561-5b36-4bdc-b264-8e2dc6f5e12b",
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

_source line 6 · 2026-05-13T16:17:55.987Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9de065d-5fe2-412e-99a3-7f53c227c09e",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsPx3r1bfkLkFLa7us6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e28d8d70-9bd0-4368-8807-50fd50a2b228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pf5gMJ7M3W4qEWWGdaJsS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 7 · 2026-05-13T16:17:57.013Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01ECbB1tEX4CXHZhTLnwEXzN`</summary>

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
  "parentUuid": "e28d8d70-9bd0-4368-8807-50fd50a2b228",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsPx3r1bfkLkFLa7us6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08704c50-dfd8-49e2-8c9e-1e0071e6ee64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pf5gMJ7M3W4qEWWGdaJsS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 8 · 2026-05-13T16:17:57.056Z_

<details><summary>↩ Tool result · `toolu_01ECbB1tEX4CXHZhTLnwEXzN`</summary>

```text
{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (8 个)\n\n- **mvp-p1-gpu1-v3**: DONE (success) — \n- **mvp-p1-gpu0-vllm**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n- **mvp-p0-forking**: DONE (success) — \n- **mvp-p1-signal**: PREPARING — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- mvp-p1-signal（准备中）\n\n## 近期结论\n- **mvp-p1-gpu1-v3** (success): —\n- **mvp-p1-gpu0-vllm** (success): —\n- **mvp-p1-gpu0** (killed): —\n\n## 趋势\n成功 3 / 负向 0 / 失败 0 / 共 7\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-13313: 无 GPU 信息\n\n## 告警\n- mvp-p1-gpu1: 已被终止 — unknown\n- mvp-p1-gpu0: 已被终止 — unknown\n- mvp-p1-gpu1-vllm: 已被终止 — unknown\n- mvp-p1-gpu1-v2: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08704c50-dfd8-49e2-8c9e-1e0071e6ee64",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "23c892d4-8e1c-45fc-bed7-7671b190e784",
  "sourceToolAssistantUUID": "08704c50-dfd8-49e2-8c9e-1e0071e6ee64",
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

_source line 9 · 2026-05-13T16:17:57.413Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011WiKMZLuKd4Dq4HdgvpdZX`</summary>

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
  "parentUuid": "23c892d4-8e1c-45fc-bed7-7671b190e784",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsPx3r1bfkLkFLa7us6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c37b57ad-6d8d-4c77-ba20-7debb349cccd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pf5gMJ7M3W4qEWWGdaJsS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 10 · 2026-05-13T16:17:57.432Z_

<details><summary>↩ Tool result · `toolu_011WiKMZLuKd4Dq4HdgvpdZX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- mvp-p1-signal（准备中）\\n\\n## 近期结论\\n- **mvp-p1-gpu1-v3** (success): —\\n- **mvp-p1-gpu0-vllm** (success): —\\n- **mvp-p1-gpu0** (killed): —\\n\\n## 趋势\\n成功 3 / 负向 0 / 失败 0 / 共 7\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestb-13313: 无 GPU 信息\\n\\n## 告警\\n- mvp-p1-gpu1: 已被终止 — unknown\\n- mvp-p1-gpu0: 已被终止 — unknown\\n- mvp-p1-gpu1-vllm: 已被终止 — unknown\\n- mvp-p1-gpu1-v2: 已被终止 — unknown\\n\", \"total_chars\": 443, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c37b57ad-6d8d-4c77-ba20-7debb349cccd",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "68011ae8-68d8-4f72-95f8-8247c571f90e",
  "sourceToolAssistantUUID": "c37b57ad-6d8d-4c77-ba20-7debb349cccd",
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

_source line 11 · 2026-05-13T16:17:58.319Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014JZyuzWoVzGjy8e8a62hBT`</summary>

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
  "parentUuid": "68011ae8-68d8-4f72-95f8-8247c571f90e",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsPx3r1bfkLkFLa7us6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "197e02ec-cf88-49d4-ac73-33538ccdde4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pf5gMJ7M3W4qEWWGdaJsS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1449,
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

_source line 12 · 2026-05-13T16:17:58.329Z_

<details><summary>↩ Tool result · `toolu_014JZyuzWoVzGjy8e8a62hBT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (12 days remaining)\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures at CPU-only cost — but no method learns WHEN to invoke it via an explicit, interpretable router. MVP evidence: death avoidance is the primary mechanism (+30-40 points from preventing -100 penalties), and selective routing outperforms unconditional simulation by +10-17 points.\\n\\n## Core Claims (2 claims for short paper)\\n\\n**C1 (Selective routing to deterministic computation)**: On ScienceWorld, deterministic simulation significantly outperforms pure LLM reasoning, with the primary mechanism being catastrophic failure prevention (the simulator as \\\"safety net\\\"). [**Pending plan-003 confirmation**]: Learned selective routing further outperforms unconditional simulation — the router learns WHICH steps need the safety net. (MVP oracle > det evidence: +10-17 points on 3/5 task types. If trained router ≤ always-det, C1 downgrades to \\\"outperforms pure LLM reasoning\\\" only.)\\n\\n**C2 (Explicit modular router)**: A lightweight explicit router (Qwen3-1.7B, ~1.7B params), trained via SFT on counterfactual trajectory labels, achieves effective per-step routing that is (a) interpretable — routing decisions can be analyzed per task category to reveal systematic LLM failure modes, (b) architecturally decoupled from the agent backbone, and (c) consistent across task categories sharing similar failure patterns.\\n\\n## Story Spine\\n\\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. No method provides an explicit, modular router for selective invocation of ground-truth deterministic computation.\\n\\n- **Our framing**: We recast the \\\"when to simulate\\\" problem as safety-aware routing. Deterministic computation is not primarily a performance booster — it is a catastrophic failure prevention mechanism. A lightweight explicit router learns to detect high-risk states where LLM reasoning is likely to fail catastrophically, and routes those steps to deterministic computation for ground-truth verification. This \\\"router-as-safety-net\\\" framing explains why: (1) the gain is concentrated in death avoidance (+30-40 points from preventing -100 penalties), (2) selective routing beats unconditional simulation (not every step needs the safety net), and (3) the router's decisions are interpretable as a diagnostic of where LLMs systematically fail.\\n\\n- **Headline result template**: \\\"On ScienceWorld, SimGate achieves [X] score (vs CogRouter 84.6, ITP-R 62.58), reducing catastrophic failures by [Y]% compared to pure LLM reasoning, while using [Z]% fewer simulator invocations than always-simulate.\\\"\\n\\n## Paper Structure (4-page short paper)\\n\\n| Section | Pages | Content |\\n|---------|-------|---------|\\n| Abstract | 0.2 | Safety-aware routing framing, headline numbers |\\n| Introduction | 0.8 | Problem + gap + contribution (2 claims) |\\n| Method | 1.0 | 3-component framework: backbone + deterministic oracle + explicit router; counterfactual training pipeline (4-step); router architecture |\\n| Experiments | 1.5 | Main results table + explicit vs implicit ablation + routing pattern analysis figure |\\n| Conclusion | 0.3 | Summary + limitations + future (MATH, API routing) |\\n| References | ~0.5 | Not counted in 4-page limit |\\n\\n## Anticipated Reviewer Concerns & Mitigations\\n\\n1. **\\\"Novelty is incremental — just SFT a small model to classify\\\"**\\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.\\n\\n2. **\\\"Only one benchmark (ScienceWorld)\\\"**\\n   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.\\n\\n3. **\\\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\\\"**\\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\\n\\n4. **\\\"Death avoidance is trivial — just filter dangerous actions\\\"**\\n   - Mitigation: Always-deterministic (which filters every step) underperforms oracle routing by 10-17 points. The non-trivial part is SELECTIVE invocation — knowing which steps need the safety net. Routing pattern analysis shows the router learns meaningful state-dependent decisions.\\n\\n5. **\\\"DAgger gap — SFT on oracle labels under base policy may not transfer\\\"**\\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension.\\n\\n## Venue Fit Risks\\n\\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\\n- Short paper format matches focused contribution scope\\n- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in \\\"Scope & Future Work\\\" paragraph\\n- Risk: \\\"Safety-aware\\\" framing may be perceived as overselling if death avoidance is the ONLY signal — need to check if positive guidance signal emerges in full trajectory collection (even small positive guidance would strengthen the story)\\n\\n## Key Differences from IDEA_BRIEF\\n\\n1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.\\n2. **Framing shifted**: From \\\"general routing to deterministic computation\\\" to \\\"safety-aware routing\\\" based on MVP death avoidance finding.\\n3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).\\n4. **\\\"ANY form\\\" softened**: Per Human Review Note #4, \\\"across multiple forms\\\" instead of \\\"ANY form\\\". Paper demonstrates principle on simulators; code interpreters discussed as extension.\\n\", \"total_chars\": 6510, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "197e02ec-cf88-49d4-ac73-33538ccdde4f",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "5e9d6a2b-083a-40d7-9d67-8b60a4f8de4f",
  "sourceToolAssistantUUID": "197e02ec-cf88-49d4-ac73-33538ccdde4f",
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

_source line 13 · 2026-05-13T16:18:02.733Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HCkZtKX1nPuxKtFd8Xmwnm`</summary>

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
  "parentUuid": "5e9d6a2b-083a-40d7-9d67-8b60a4f8de4f",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsQU1etBJU9V6bdqvdj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f07726e-68bf-4581-b732-df270c4fa404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeWt7wUuNGc9XDJZb4iq8M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3277,
      "cache_read_input_tokens": 16555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3277,
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

_source line 14 · 2026-05-13T16:18:02.749Z_

<details><summary>↩ Tool result · `toolu_01HCkZtKX1nPuxKtFd8Xmwnm`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'simgate-modular-routing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f07726e-68bf-4581-b732-df270c4fa404",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "70d313f0-1db8-42b8-8ad4-fee3b648c50f",
  "sourceToolAssistantUUID": "0f07726e-68bf-4581-b732-df270c4fa404",
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

_source line 15 · 2026-05-13T16:18:03.415Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KkxsAezaPQ8xoyvbkr7iNX`</summary>

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
  "parentUuid": "70d313f0-1db8-42b8-8ad4-fee3b648c50f",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsQU1etBJU9V6bdqvdj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af2708d7-e862-45a3-8c1a-ab09258771e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeWt7wUuNGc9XDJZb4iq8M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3277,
      "cache_read_input_tokens": 16555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3277,
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

_source line 16 · 2026-05-13T16:18:03.428Z_

<details><summary>↩ Tool result · `toolu_01KkxsAezaPQ8xoyvbkr7iNX`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af2708d7-e862-45a3-8c1a-ab09258771e7",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "6a80e5a9-32b3-4a6a-b7be-37c7c2bc0c0c",
  "sourceToolAssistantUUID": "af2708d7-e862-45a3-8c1a-ab09258771e7",
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

_source line 17 · 2026-05-13T16:18:03.837Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GgtdegMtuspMrhFaDXaFYZ`</summary>

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
  "parentUuid": "6a80e5a9-32b3-4a6a-b7be-37c7c2bc0c0c",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsQU1etBJU9V6bdqvdj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11553a8f-02c6-43a0-81f9-dc341e79ea90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeWt7wUuNGc9XDJZb4iq8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3277,
      "cache_read_input_tokens": 16555,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3277
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 16555,
          "cache_creation_input_tokens": 3277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3277,
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

_source line 18 · 2026-05-13T16:18:03.847Z_

<details><summary>↩ Tool result · `toolu_01GgtdegMtuspMrhFaDXaFYZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 7\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-deterministic）。这是 1-step 的本质局限而非 bug。直接比较 det vs\\n    internal 能回答核心问题\\\"确定性计算有没有用\\\"，无需 oracle 作为中介。oracle 在密集 reward tasks 上仍有参考价值。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 15:25 UTC\\n  summary: MVP Phase 1 判定 PASS — det > internal 在 ≥2/5 task types 上统计显著，oracle > det\\n    信号支持 router 训练\\n  rationale: melt (+40.15, CI [25, 60.15]) 和 change-state (+40.2, CI [25, 60.15])\\n    满足 ≥2/5 Pass 标准。mix-paint (+35.5) 大概率也通过。grow-plant (0.0) 符合预期（pre-registered\\n    weak/对照）。最关键发现：oracle > det（melt +16.7, change-state +14.95, mix-paint +10.0）证明\\n    selective routing 有额外增量——这是 SimGate router 训练的信号来源。信号机制是 death avoidance（避免 -100\\n    致死动作）而非正向引导，论文 framing 需定位为 safety-aware routing。待确认：melt/change-state 数据重复性、mix-paint\\n    CI、boil v3 重跑。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: boil data (old code)\\n    result: det-int +30.1\\n  - exp_id: mvp-p1-gpu0-vllm\\n    role: melt+change-state (v3)\\n    result: det-int +40.15/+40.2, CI [25, 60.15]\\n  - exp_id: mvp-p1-gpu1-v3\\n    role: mix-paint+grow-plant (v3)\\n    result: det-int +35.5/0.0\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 15:37 UTC\\n  summary: 'Research phase plan revised per Reviewer W1-W5: 2-way first, signal pre-screening,\\n    parameter-controlled ablation, GPU units fixed'\\n  rationale: 'Reviewer 提出 5 个实质性问题全部采纳: (1) C1 \\\"selective > unconditional\\\" 标注为待确认;\\n    (2) 2-way collection 优先，与 MVP 一致且省 33% GPU; (3) plan-001 增加 mini signal detection\\n    前置步骤避免浪费 GPU; (4) plan-004 增加 1.7B implicit 控制条件隔离架构效果; (5) GPU 预算改为 RTX 5090\\n    实际时长。melt/change-state 确认非重复但共享 variations，论文中合并报告。'\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n\", \"total_chars\": 3381, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11553a8f-02c6-43a0-81f9-dc341e79ea90",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "ea223f87-ed87-4665-8f3b-a13159038abb",
  "sourceToolAssistantUUID": "11553a8f-02c6-43a0-81f9-dc341e79ea90",
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

_source line 19 · 2026-05-13T16:18:09.515Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013QCJFWqoarCiDJAXuVD3yi`</summary>

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
  "parentUuid": "ea223f87-ed87-4665-8f3b-a13159038abb",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsQsCBNkPXBTd4W81vY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3d2d464-fe6d-41bc-b4f9-e5475fbdc9d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NnwYyQdAKSrDEpDRNvbxF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2435,
      "cache_read_input_tokens": 19832,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2435
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 19832,
          "cache_creation_input_tokens": 2435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2435,
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

### Tool call

_source line 20 · 2026-05-13T16:18:09.518Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Qr5wde57ZbAkAJMTUFB7Kr`</summary>

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
  "parentUuid": "a3d2d464-fe6d-41bc-b4f9-e5475fbdc9d9",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsQsCBNkPXBTd4W81vY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e143401-c11b-46a8-8945-f8ba961ee9df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NnwYyQdAKSrDEpDRNvbxF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2435,
      "cache_read_input_tokens": 19832,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2435
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 19832,
          "cache_creation_input_tokens": 2435,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2435,
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

_source line 21 · 2026-05-13T16:18:09.527Z_

<details><summary>↩ Tool result · `toolu_013QCJFWqoarCiDJAXuVD3yi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\", \"content\": \"## Phase 1 MVP 最终结论 (2026-05-13)\\n\\n### Verdict: PASS (4/5 tasks 显著正向)\\n\\nPhase 1 验证了 fork-based deterministic evaluation 在 ScienceWorld 上显著优于纯 LLM 内部推理。\\n\\n### 关键设计决策与教训\\n\\n1. **Tie-break 策略**: `>` (strict) 而非 `>=`。95%+ 步骤 score_delta=0（稀疏奖励），`>=` 会让 oracle 退化为 always-internal。用 `>` 后 oracle 在 tie 时选 deterministic，实验验证这是合理的。\\n\\n2. **Death filter 只用于有 fork 的模式**: always-internal 是纯 LLM baseline，不能调 fork/is_lethal（方法论问题——Reviewer 会质疑\\\"你在 internal 模式偷偷用了外部计算\\\"）。death filter 只在 always-deterministic 和 oracle 中生效。\\n\\n3. **melt 与 change-state internal 分数巧合相同的解释**: 两个 task 共享 ScienceWorld environment variations（同房间/物品/布局），LLM 表现极差只产生 3 种结果（-100/0/3），分布碰巧一致。不是数据重复。det 分数已验证不同（6/20 episode 有差异）。\\n\\n4. **boil 数据来自旧代码**（>= tie-break, 无 death filter），full phase 需要用新代码重跑以保证一致性。\\n\\n5. **grow-plant 无效果**: 三种模式完全一致（0.5±1.4），可能 task 本身过于简单或 30 步不够。\\n\\n6. **Fork 机制本身没问题**: 诊断确认 fork_and_lookahead 正确工作，score_before 与 main env 一致。收益主要来自避免 -100 致死动作（\\\"focus on 错误对象\\\"），而非精细的 score 区分。\\n\\n7. **vLLM 兼容性**: torch 2.10.0 + vLLM 0.18.1 有 duplicate template name assertion error，需注释 select_algorithm.py 1695/2164 行。\\n\\n8. **Oracle 增量价值**: 在新代码的 3 个 task 上 oracle > det（Δ +10~17），证明 routing 有独立价值，不是简单的 \\\"deterministic always wins\\\"。\\n\\n### 竞品对标\\n- CogRouter (arXiv 2602.12662): 同 Qwen2.5-7B, ScienceWorld Score=84.6, SR=72.0%。路由 thinking depth（4 levels），与我们路由 reasoning vs computation 是不同维度。\\n- ITP-R (arXiv 2601.08955): Learned world model + K-head gating, SR=63.91%。WM 有 compounding error，我们用 deterministic simulator 避免此问题。\\n\", \"total_chars\": 1482, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3d2d464-fe6d-41bc-b4f9-e5475fbdc9d9",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "c6e099c0-86e0-4d3b-af58-54b463f6573a",
  "sourceToolAssistantUUID": "a3d2d464-fe6d-41bc-b4f9-e5475fbdc9d9",
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

### Tool result

_source line 22 · 2026-05-13T16:18:09.537Z_

<details><summary>↩ Tool result · `toolu_01Qr5wde57ZbAkAJMTUFB7Kr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ROADMAP.md\", \"content\": \"# simgate-modular-routing — Research Dashboard\\n\\n> 最后更新: 2026-05-13 15:37 UTC | 更新原因: Reviewer W1-W5 修订: GPU 单位改 RTX 5090, 2-way 优先, 信号预筛, 参数控制 ablation\\n\\n## 核心方向\\nSimGate: 显式轻量 router (Qwen3-1.7B) 学习 per-step 安全路由 — 检测 LLM 推理高风险状态，选择性调用确定性外部计算（环境模拟器）防止灾难性失败。详见 paper_framing.md。\\n\\n## 投稿目标\\nEMNLP 2026 ARR short paper (4 pages)，DDL: 2026-05-25（剩余 12 天）\\n\\n## 当前阶段\\n**Research Phase** — MVP PASS (D005)，Dream 模拟中\\n\\n## 当前进展\\n- MVP: DONE (PASS) — 4/5 task types det > internal 显著, 主信号 = death avoidance\\n- paper_framing.md: DONE — 2 Claims, safety-aware routing. C1 含待确认子项（selective > unconditional）\\n- experiment_plan.yaml: v2 (Reviewer W1-W5 修订) — 2-way 优先, 信号预筛, 参数控制 ablation\\n- Dream: RUNNING (dream_20260513T153257, full mode, ~15 min)\\n- melt/change-state: Reviewer 确认非重复，但共享 variations → 论文中合并为 \\\"state-change tasks\\\"\\n\\n## 近期任务\\n- [ ] Dream 完成 → 审阅审稿报告，确认/调整 framing\\n- [ ] Dream 通过后批准 plan-001a (信号预筛) + plan-007 (boil rerun) 双卡并行\\n- [ ] Agent 完成 gpu1-v3 registry 更新 (ANALYZING → DONE)\\n- [ ] plan-001a 完成 → 筛出 10-15 有信号 task types → 启动 plan-001b\\n- [ ] plan-001b 完成 → 启动 plan-002 (router SFT) + plan-004 (explicit vs implicit ablation)\\n\\n## GPU 预算\\n- 服务器: westb-13313, 2× RTX 5090 32GB (cuda:0, cuda:1)\\n- P0: ~72h | P1: ~25h | P2: ~25h | 总计: ~122h (RTX 5090 wall-clock hours)\\n- Critical path: 001a(10h) → 001b(25h) → 002(8h) → 003(15h) = ~2.5 天双卡并行\\n\\n## 时间线 (12 天, RTX 5090 双卡)\\n| 天数 | 任务 | GPU |\\n|------|------|-----|\\n| 1 | Dream 审阅 + plan-001a 信号预筛 + plan-007 boil rerun | 双卡 |\\n| 2-3 | plan-001b 全量 trajectory collection | 双卡满载 |\\n| 4 | plan-002 router SFT + plan-004 explicit/implicit ablation | 双卡 |\\n| 5-6 | plan-003 evaluation + plan-006 2/3-way ablation | 双卡 |\\n| 7 | plan-005 routing analysis + plan-008 router size (P1) | 单卡+分析 |\\n| 8-10 | Paper writing (Paper Agent) | 按需补实验 |\\n| 11-12 | Review + submit | — |\\n\\n## 关键风险\\n1. Novelty 天花板 — SFT small router 技术简单，需靠 empirical finding + analysis\\n2. C1 子项待确认 — trained router > always-det 尚无证据 (plan-003 验证)\\n3. ScienceWorld 单 benchmark — short paper 可接受\\n4. Death avoidance 唯一信号 — 全量 collection 可能发现正向引导信号\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-13 | Research phase plan revised per Reviewer W1-W5: 2- | — |\\n| D005 | 2026-05-13 | MVP Phase 1 判定 PASS — det > internal 在 ≥2/5 task t | mvp-p1-gpu0, mvp-p1-gpu0-vllm, mvp-p1-gpu1-v3 |\\n| D004 | 2026-05-13 | MVP 判定 primary metric 改为 always-deterministic vs a | — |\\n| D003 | 2026-05-13 | GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑 | mvp-p1-gpu0, mvp-p1-gpu1-vllm |\\n| D002 | 2026-05-13 | 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phas | — |\\n| D001 | 2026-05-13 | MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM | — |\\n\\n\", \"total_chars\": 2649, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e143401-c11b-46a8-8945-f8ba961ee9df",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "a22f322f-9723-4812-9996-aa4302a3fb95",
  "sourceToolAssistantUUID": "9e143401-c11b-46a8-8945-f8ba961ee9df",
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

_source line 23 · 2026-05-13T16:18:12.367Z_

Now let me look for the actual paper draft and any artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a22f322f-9723-4812-9996-aa4302a3fb95",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsRHH21ZvHrRpbwx4Db",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d142831b-f0f1-4ea8-a4ff-48089ee93e25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ug1eTvz2movgKogKkUu5a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2915,
      "cache_read_input_tokens": 22267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2915,
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

_source line 24 · 2026-05-13T16:18:14.404Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VB5zX1wWd2VuzXNTC6buj7`</summary>

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
  "parentUuid": "d142831b-f0f1-4ea8-a4ff-48089ee93e25",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsRHH21ZvHrRpbwx4Db",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df8641fd-4ee7-4b8f-a14d-98ea1cf82e01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ug1eTvz2movgKogKkUu5a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2915,
      "cache_read_input_tokens": 22267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2915,
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

_source line 25 · 2026-05-13T16:18:14.422Z_

<details><summary>↩ Tool result · `toolu_01VB5zX1wWd2VuzXNTC6buj7`</summary>

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
  "parentUuid": "df8641fd-4ee7-4b8f-a14d-98ea1cf82e01",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "79f339a7-1267-4c48-83c0-703151e85085",
  "sourceToolAssistantUUID": "df8641fd-4ee7-4b8f-a14d-98ea1cf82e01",
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

_source line 26 · 2026-05-13T16:18:14.788Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LswDuKjHZaP8kGsHE82S86`</summary>

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
  "parentUuid": "79f339a7-1267-4c48-83c0-703151e85085",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsRHH21ZvHrRpbwx4Db",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a241c796-550c-4655-a897-76d7735e2e79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ug1eTvz2movgKogKkUu5a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2915,
      "cache_read_input_tokens": 22267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2915,
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

_source line 27 · 2026-05-13T16:18:14.800Z_

<details><summary>↩ Tool result · `toolu_01LswDuKjHZaP8kGsHE82S86`</summary>

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
  "parentUuid": "a241c796-550c-4655-a897-76d7735e2e79",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "2b39930e-b09b-4d48-97ee-ce692dc96ed2",
  "sourceToolAssistantUUID": "a241c796-550c-4655-a897-76d7735e2e79",
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

_source line 28 · 2026-05-13T16:18:15.440Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017htrv9iPmiSPxUzrrWWQG3`</summary>

```json
{
  "pattern": "artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b39930e-b09b-4d48-97ee-ce692dc96ed2",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsRHH21ZvHrRpbwx4Db",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bce4ead0-d196-4549-8540-2edcc3f45091",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ug1eTvz2movgKogKkUu5a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2915,
      "cache_read_input_tokens": 22267,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 22267,
          "cache_creation_input_tokens": 2915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2915,
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

_source line 29 · 2026-05-13T16:18:15.457Z_

<details><summary>↩ Tool result · `toolu_017htrv9iPmiSPxUzrrWWQG3`</summary>

```text
artifacts/phase1_progress_report.md
artifacts/diagnosis_mvp-p1-gpu1-v2.md
artifacts/dream_reports/dream_20260513T153257/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T153257/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T153257/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T153257/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T153257/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T153257/best/experiment_data.json
artifacts/dream_reports/dream_20260513T153257/best/paper_framing.md
artifacts/dream_reports/dream_20260513T153257/best/paper.tex
artifacts/dream_reports/dream_20260513T153257/best/paper.aux
artifacts/dream_reports/dream_20260513T153257/best/paper.out
artifacts/dream_reports/dream_20260513T153257/best/paper.pdf
artifacts/dream_reports/dream_20260513T153257/best/paper.log
artifacts/dream_reports/dream_20260513T153257/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T153257/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T153257/median/experiment_data.json
artifacts/dream_reports/dream_20260513T153257/median/paper_framing.md
artifacts/dream_reports/dream_20260513T153257/median/paper.tex
artifacts/dream_reports/dream_20260513T153257/median/paper.aux
artifacts/dream_reports/dream_20260513T153257/median/paper.out
artifacts/dream_reports/dream_20260513T153257/median/paper.pdf
artifacts/dream_reports/dream_20260513T153257/median/paper.log
artifacts/dream_reports/dream_20260513T153257/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260513T153257/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T153257/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T153257/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T153257/worst/paper.tex
artifacts/dream_reports/dream_20260513T153257/worst/paper.aux
artifacts/dream_reports/dream_20260513T153257/worst/paper.out
artifacts/dream_reports/dream_20260513T153257/worst/paper.pdf
artifacts/dream_reports/dream_20260513T153257/worst/paper.log
artifacts/dream_reports/dream_20260513T153257/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260513T153257/best/review_context.yaml
artifacts/dream_reports/dream_20260513T153257/logs/orchestrator.log
artifacts/dream_reports/dream_20260513T153257/best/review_report.md
artifacts/dream_reports/dream_20260513T153257/logs/review_best.log
artifacts/dream_reports/dream_20260513T153257/median/review_context.yaml
artifacts/dream_reports/dream_20260513T153257/median/review_report.md
artifacts/dream_reports/dream_20260513T153257/logs/review_median.log
artifacts/dream_reports/dream_20260513T153257/worst/review_context.yaml
artifacts/dream_reports/dream_20260513T153257/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bce4ead0-d196-4549-8540-2edcc3f45091",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "a0a323c3-0739-4adb-8779-488b4a7c1915",
  "sourceToolAssistantUUID": "bce4ead0-d196-4549-8540-2edcc3f45091",
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

_source line 30 · 2026-05-13T16:18:18.653Z_

Let me read the median paper (which likely represents the actual expected outcome) and its framing, plus the best-case paper for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0a323c3-0739-4adb-8779-488b4a7c1915",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsRimCHc13sxydQyaVi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d65d64fb-2462-4afa-86e7-49e534f963b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgCFepvViYmeu9pG8tYQEc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1428,
      "cache_read_input_tokens": 25182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1428,
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

_source line 31 · 2026-05-13T16:18:21.021Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MrdbZ6h2L8DBAJMdaKVCRQ`</summary>

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
  "parentUuid": "d65d64fb-2462-4afa-86e7-49e534f963b8",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsRimCHc13sxydQyaVi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cac0eb2c-319b-4e83-87a9-42fe22b4c539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgCFepvViYmeu9pG8tYQEc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1428,
      "cache_read_input_tokens": 25182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1428,
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

_source line 32 · 2026-05-13T16:18:21.026Z_

<details><summary>↩ Tool result · `toolu_01MrdbZ6h2L8DBAJMdaKVCRQ`</summary>

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
  "parentUuid": "cac0eb2c-319b-4e83-87a9-42fe22b4c539",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "fa8e9af1-6704-41a9-8ba8-5dc8eafbfabb",
  "sourceToolAssistantUUID": "cac0eb2c-319b-4e83-87a9-42fe22b4c539",
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

_source line 33 · 2026-05-13T16:18:21.341Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HuNgPbMRCiC9fxDw8cP8Lx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa8e9af1-6704-41a9-8ba8-5dc8eafbfabb",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsRimCHc13sxydQyaVi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eed7a99d-e812-4754-af74-e0cd3612a4f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgCFepvViYmeu9pG8tYQEc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1428,
      "cache_read_input_tokens": 25182,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1428
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 25182,
          "cache_creation_input_tokens": 1428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1428,
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

_source line 34 · 2026-05-13T16:18:21.346Z_

<details><summary>↩ Tool result · `toolu_01HuNgPbMRCiC9fxDw8cP8Lx`</summary>

```text
1	# Paper Framing — simgate-modular-routing
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)
5	- Fallback: EMNLP 2026 Findings
6	- Deadline: ARR May 25, 2026 (12 days remaining)
7	
8	## Core Insight
9	
10	LLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures at CPU-only cost — but no method learns WHEN to invoke it via an explicit, interpretable router. MVP evidence: death avoidance is the primary mechanism (+30-40 points from preventing -100 penalties), and selective routing outperforms unconditional simulation by +10-17 points.
11	
12	## Core Claims (2 claims for short paper)
13	
14	**C1 (Selective routing to deterministic computation)**: On ScienceWorld, learned selective routing to a deterministic environment simulator significantly outperforms both pure LLM reasoning and unconditional simulation. The primary value mechanism is catastrophic failure prevention: the simulator serves as a "safety net" that intercepts actions leading to irreversible negative outcomes, rather than providing positive task guidance.
15	
16	**C2 (Explicit modular router)**: A lightweight explicit router (Qwen3-1.7B, ~1.7B params), trained via SFT on counterfactual trajectory labels, achieves effective per-step routing that is (a) interpretable — routing decisions can be analyzed per task category to reveal systematic LLM failure modes, (b) architecturally decoupled from the agent backbone, and (c) consistent across task categories sharing similar failure patterns.
17	
18	## Story Spine
19	
20	- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. No method provides an explicit, modular router for selective invocation of ground-truth deterministic computation.
21	
22	- **Our framing**: We recast the "when to simulate" problem as safety-aware routing. Deterministic computation is not primarily a performance booster — it is a catastrophic failure prevention mechanism. A lightweight explicit router learns to detect high-risk states where LLM reasoning is likely to fail catastrophically, and routes those steps to deterministic computation for ground-truth verification. This "router-as-safety-net" framing explains why: (1) the gain is concentrated in death avoidance (+30-40 points from preventing -100 penalties), (2) selective routing beats unconditional simulation (not every step needs the safety net), and (3) the router's decisions are interpretable as a diagnostic of where LLMs systematically fail.
23	
24	- **Headline result template**: "On ScienceWorld, SimGate achieves [X] score (vs CogRouter 84.6, ITP-R 62.58), reducing catastrophic failures by [Y]% compared to pure LLM reasoning, while using [Z]% fewer simulator invocations than always-simulate."
25	
26	## Paper Structure (4-page short paper)
27	
28	| Section | Pages | Content |
29	|---------|-------|---------|
30	| Abstract | 0.2 | Safety-aware routing framing, headline numbers |
31	| Introduction | 0.8 | Problem + gap + contribution (2 claims) |
32	| Method | 1.0 | 3-component framework: backbone + deterministic oracle + explicit router; counterfactual training pipeline (4-step); router architecture |
33	| Experiments | 1.5 | Main results table + explicit vs implicit ablation + routing pattern analysis figure |
34	| Conclusion | 0.3 | Summary + limitations + future (MATH, API routing) |
35	| References | ~0.5 | Not counted in 4-page limit |
36	
37	## Anticipated Reviewer Concerns & Mitigations
38	
39	1. **"Novelty is incremental — just SFT a small model to classify"**
40	   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.
41	
42	2. **"Only one benchmark (ScienceWorld)"**
43	   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.
44	
45	3. **"Comparison unfair — CogRouter uses RL (CoPO), you use SFT"**
46	   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.
47	
48	4. **"Death avoidance is trivial — just filter dangerous actions"**
49	   - Mitigation: Always-deterministic (which filters every step) underperforms oracle routing by 10-17 points. The non-trivial part is SELECTIVE invocation — knowing which steps need the safety net. Routing pattern analysis shows the router learns meaningful state-dependent decisions.
50	
51	5. **"DAgger gap — SFT on oracle labels under base policy may not transfer"**
52	   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension.
53	
54	## Venue Fit Risks
55	
56	- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)
57	- Short paper format matches focused contribution scope
58	- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in "Scope & Future Work" paragraph
59	- Risk: "Safety-aware" framing may be perceived as overselling if death avoidance is the ONLY signal — need to check if positive guidance signal emerges in full trajectory collection (even small positive guidance would strengthen the story)
60	
61	## Key Differences from IDEA_BRIEF
62	
63	1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.
64	2. **Framing shifted**: From "general routing to deterministic computation" to "safety-aware routing" based on MVP death avoidance finding.
65	3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).
66	4. **"ANY form" softened**: Per Human Review Note #4, "across multiple forms" instead of "ANY form". Paper demonstrates principle on simulators; code interpreters discussed as extension.
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eed7a99d-e812-4754-af74-e0cd3612a4f6",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "10938a57-b468-40e7-bb2f-99a8f42e5da1",
  "sourceToolAssistantUUID": "eed7a99d-e812-4754-af74-e0cd3612a4f6",
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

_source line 35 · 2026-05-13T16:18:26.172Z_

Now let me read the "worst" case paper (the negative-result pivot version described in the task prompt) since the summary in the task describes a paper with negative results (SimGate 65.2 vs always-det 64.8), which differs from the median dream paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10938a57-b468-40e7-bb2f-99a8f42e5da1",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsS9ykeu6P3DsiXBw7k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1ddbaac-9d7e-489c-9beb-7a97bd08cc44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaS6QCMgA9Z2R9JvLozFBv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10408,
      "cache_read_input_tokens": 26610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10408,
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

_source line 36 · 2026-05-13T16:18:28.683Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AkMxrfrPEwpa7QLcHQ5ZsP`</summary>

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
  "parentUuid": "f1ddbaac-9d7e-489c-9beb-7a97bd08cc44",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsS9ykeu6P3DsiXBw7k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c4599e5-459e-445b-9174-3f3bedc72ab0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaS6QCMgA9Z2R9JvLozFBv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10408,
      "cache_read_input_tokens": 26610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10408,
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

_source line 37 · 2026-05-13T16:18:28.705Z_

<details><summary>↩ Tool result · `toolu_01AkMxrfrPEwpa7QLcHQ5ZsP`</summary>

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
  "parentUuid": "5c4599e5-459e-445b-9174-3f3bedc72ab0",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "b543dac5-13db-4649-92ea-356f7331d2a6",
  "sourceToolAssistantUUID": "5c4599e5-459e-445b-9174-3f3bedc72ab0",
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

_source line 38 · 2026-05-13T16:18:29.232Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RCbwfi922PeaWnC8KDQWeU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b543dac5-13db-4649-92ea-356f7331d2a6",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsS9ykeu6P3DsiXBw7k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b492c69b-3b7a-4a97-832a-a30075880d98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HaS6QCMgA9Z2R9JvLozFBv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10408,
      "cache_read_input_tokens": 26610,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10408
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 26610,
          "cache_creation_input_tokens": 10408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10408,
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

_source line 39 · 2026-05-13T16:18:29.241Z_

<details><summary>↩ Tool result · `toolu_01RCbwfi922PeaWnC8KDQWeU`</summary>

```text
1	# Paper Framing — simgate-modular-routing
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)
5	- Fallback: EMNLP 2026 Findings
6	- Deadline: ARR May 25, 2026 (12 days remaining)
7	
8	## Core Insight
9	
10	LLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures at CPU-only cost — but no method learns WHEN to invoke it via an explicit, interpretable router. MVP evidence: death avoidance is the primary mechanism (+30-40 points from preventing -100 penalties), and selective routing outperforms unconditional simulation by +10-17 points.
11	
12	## Core Claims (2 claims for short paper)
13	
14	**C1 (Selective routing to deterministic computation)**: On ScienceWorld, learned selective routing to a deterministic environment simulator significantly outperforms both pure LLM reasoning and unconditional simulation. The primary value mechanism is catastrophic failure prevention: the simulator serves as a "safety net" that intercepts actions leading to irreversible negative outcomes, rather than providing positive task guidance.
15	
16	**C2 (Explicit modular router)**: A lightweight explicit router (Qwen3-1.7B, ~1.7B params), trained via SFT on counterfactual trajectory labels, achieves effective per-step routing that is (a) interpretable — routing decisions can be analyzed per task category to reveal systematic LLM failure modes, (b) architecturally decoupled from the agent backbone, and (c) consistent across task categories sharing similar failure patterns.
17	
18	## Story Spine
19	
20	- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. No method provides an explicit, modular router for selective invocation of ground-truth deterministic computation.
21	
22	- **Our framing**: We recast the "when to simulate" problem as safety-aware routing. Deterministic computation is not primarily a performance booster — it is a catastrophic failure prevention mechanism. A lightweight explicit router learns to detect high-risk states where LLM reasoning is likely to fail catastrophically, and routes those steps to deterministic computation for ground-truth verification. This "router-as-safety-net" framing explains why: (1) the gain is concentrated in death avoidance (+30-40 points from preventing -100 penalties), (2) selective routing beats unconditional simulation (not every step needs the safety net), and (3) the router's decisions are interpretable as a diagnostic of where LLMs systematically fail.
23	
24	- **Headline result template**: "On ScienceWorld, SimGate achieves [X] score (vs CogRouter 84.6, ITP-R 62.58), reducing catastrophic failures by [Y]% compared to pure LLM reasoning, while using [Z]% fewer simulator invocations than always-simulate."
25	
26	## Paper Structure (4-page short paper)
27	
28	| Section | Pages | Content |
29	|---------|-------|---------|
30	| Abstract | 0.2 | Safety-aware routing framing, headline numbers |
31	| Introduction | 0.8 | Problem + gap + contribution (2 claims) |
32	| Method | 1.0 | 3-component framework: backbone + deterministic oracle + explicit router; counterfactual training pipeline (4-step); router architecture |
33	| Experiments | 1.5 | Main results table + explicit vs implicit ablation + routing pattern analysis figure |
34	| Conclusion | 0.3 | Summary + limitations + future (MATH, API routing) |
35	| References | ~0.5 | Not counted in 4-page limit |
36	
37	## Anticipated Reviewer Concerns & Mitigations
38	
39	1. **"Novelty is incremental — just SFT a small model to classify"**
40	   - Mitigation: Contribution is the empirical finding (death avoidance mechanism + routing patterns) more than the architecture. Router-as-diagnostic-probe reveals systematic LLM failure modes. Explicit vs implicit ablation quantifies the gap.
41	
42	2. **"Only one benchmark (ScienceWorld)"**
43	   - Mitigation: Short paper format justifies focused evaluation. ScienceWorld uniquely tests rule-governed dynamics with catastrophic penalties. Discuss MATH/API extension as future work.
44	
45	3. **"Comparison unfair — CogRouter uses RL (CoPO), you use SFT"**
46	   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.
47	
48	4. **"Death avoidance is trivial — just filter dangerous actions"**
49	   - Mitigation: Always-deterministic (which filters every step) underperforms oracle routing by 10-17 points. The non-trivial part is SELECTIVE invocation — knowing which steps need the safety net. Routing pattern analysis shows the router learns meaningful state-dependent decisions.
50	
51	5. **"DAgger gap — SFT on oracle labels under base policy may not transfer"**
52	   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension.
53	
54	## Venue Fit Risks
55	
56	- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)
57	- Short paper format matches focused contribution scope
58	- Risk: Reviewer may expect ALFWorld evaluation (standard agent benchmark pair) — address in "Scope & Future Work" paragraph
59	- Risk: "Safety-aware" framing may be perceived as overselling if death avoidance is the ONLY signal — need to check if positive guidance signal emerges in full trajectory collection (even small positive guidance would strengthen the story)
60	
61	## Key Differences from IDEA_BRIEF
62	
63	1. **Scope narrowed**: IDEA_BRIEF proposed 3 tracks (ScienceWorld + ALFWorld + MATH). Short paper focuses on ScienceWorld only in main text; MATH as P1 extension; ALFWorld deferred.
64	2. **Framing shifted**: From "general routing to deterministic computation" to "safety-aware routing" based on MVP death avoidance finding.
65	3. **Claims reduced**: From 4 hypotheses (H1-H4) to 2 focused claims (C1-C2).
66	4. **"ANY form" softened**: Per Human Review Note #4, "across multiple forms" instead of "ANY form". Paper demonstrates principle on simulators; code interpreters discussed as extension.
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b492c69b-3b7a-4a97-832a-a30075880d98",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "b5ea44f5-6e8e-4ddb-bc77-354f09b65401",
  "sourceToolAssistantUUID": "b492c69b-3b7a-4a97-832a-a30075880d98",
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

_source line 40 · 2026-05-13T16:18:35.313Z_

Now let me also check the existing review report and the best-case paper for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5ea44f5-6e8e-4ddb-bc77-354f09b65401",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsSjh2vYTJYjjMQaudD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed6e9a6c-68de-4372-bfaa-403df05f5e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CqFigLXW77wm4NnaLLGANg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9048,
      "cache_read_input_tokens": 37018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9048,
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

_source line 41 · 2026-05-13T16:18:37.711Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NCbaL5siEqxWDGV5ReuyRP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed6e9a6c-68de-4372-bfaa-403df05f5e4e",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsSjh2vYTJYjjMQaudD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de8b3880-e081-428a-8667-53818a934061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CqFigLXW77wm4NnaLLGANg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9048,
      "cache_read_input_tokens": 37018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9048,
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

_source line 42 · 2026-05-13T16:18:37.716Z_

<details><summary>↩ Tool result · `toolu_01NCbaL5siEqxWDGV5ReuyRP`</summary>

```text
1	---
2	dream_id: dream_20260513T153257
3	tier: best
4	overall_score: borderline weak accept (4/6)
5	timestamp: 2026-05-13T16:10:18.848155+00:00
6	---
7	
8	# Dream Review Report: SimGate — Safety-Aware Routing to Deterministic Computation
9	
10	**Paper**: SimGate: Safety-Aware Routing to Deterministic Computation for LLM Agents in Rule-Governed Environments
11	**Review mode**: full (2 reviewers, 4-step roundtable)
12	**Venue standard**: Top ML venue, ~25% acceptance, 6-point scale
13	
14	---
15	
16	## Roundtable Summary
17	
18	| | R1 (Methods+Experiments) | R2 (Novelty+Related Work) | Post-Discussion |
19	|---|---|---|---|
20	| **Preliminary score** | 4 (Weak Accept) | 3 (Weak Reject) | — |
21	| **Confidence** | 4/5 | 4/5 | — |
22	| **Final score** | 4 | 3 | **3.5 → 4 (Borderline Weak Accept)** |
23	
24	**Areas of agreement**: Both reviewers agree the paper (a) addresses a real problem with a clean modular design, (b) has above-average ablation coverage for a short paper, (c) suffers from a confounded explicit/implicit comparison (7B vs 1.7B parameter mismatch), (d) contains placeholder arXiv IDs undermining verifiability, and (e) needs tighter methodological specification of the hindsight labeling criterion.
25	
26	**Key disagreement**: R1 considers the failure taxonomy a "genuine interpretive contribution"; R2 considers it "descriptive post-hoc analysis, not a methodological contribution." After discussion, consensus: the taxonomy adds empirical value but should not be listed as a core contribution (C2 overreaches by bundling it with the explicit routing claim).
27	
28	**Score convergence**: R1 holds at 4 (addressable issues), R2 holds at 3 (novelty gap is structural). Consensus: **borderline, rounds to 4** — the empirical death-avoidance insight and comprehensive ablation coverage are above the rejection threshold, but the novelty concerns and missing related work need revision.
29	
30	---
31	
32	## R1: Methods & Experiments
33	
34	### Strengths
35	
36	- **Clean counterfactual labeling pipeline.** 3-way forking with hindsight labeling is principled; episode-level train/val split avoids temporal data leakage.
37	- **Explicit/implicit architectural distinction is well-motivated.** Decoupling routing from action generation is a genuine design insight. Concrete metrics (false negative rate 8.3% vs 18.7%, invocation ratio 34.2% vs 52.3%) explain *why* modular routing helps.
38	- **Honest gain decomposition.** The 70/30 death-avoidance/positive-guidance split follows the data rather than overclaiming. This decomposition is the paper's strongest empirical contribution.
39	- **Comprehensive ablation suite for a short paper.** 2-way vs 3-way, router size, explicit vs implicit, cross-task transfer, MATH generalization — well above average.
40	- **Bootstrap 90% CIs** reported for key comparisons (e.g., SimGate [87.1, 93.3], delta vs internal [31.2, 43.6]).
41	- **Oracle baseline** (93.1) provides meaningful upper bound; the 2.9-point gap quantifies remaining headroom.
42	- **Full experiment coverage.** All 10 planned experiments appear in the paper (main text + appendices).
43	
44	### Weaknesses
45	
46	- **W1 (Critical): Hindsight labeling criterion is underspecified.** The paper says "hindsight labeling picks best modality" without defining the comparison window. In a sparse-reward environment (ScienceWorld: 95%+ of steps have zero score delta), 1-step labeling would be nearly degenerate. The paper is silent on this despite it being a known challenge (the tie-break >= vs > sensitivity found during development). This is the single most important methodological omission — the labeling criterion determines training signal quality and must be explicitly stated and justified.
47	- **W2 (Major): Explicit vs implicit comparison is confounded.** The implicit baseline SFT-trains the 7B backbone to emit [SIMULATE], while the explicit router is a separate 1.7B model. This confounds: (a) architecture (modular vs entangled), (b) parameter budget (7B+1.7B vs 7B alone), (c) training interference (SFT on 7B degrades action quality). A parameter-matched control (1.7B implicit router) is needed to isolate the architectural contribution claimed in C2.
48	- **W3 (Major): CogRouter/ITP-R numbers are cited, not reproduced.** Both use different backbones and training procedures. Without reproduction under identical conditions (same Qwen2.5-7B backbone, same evaluation episodes), the comparison conflates method and backbone differences.
49	- **W4 (Moderate): Oracle may be suboptimal.** If oracle uses 1-step lookahead in a sparse-reward setting, it defaults to deterministic on ties — closer to "always-deterministic-on-ties" than true optimal. The "near-oracle" claim (2.9-point gap) may be vacuous if the oracle itself leaves substantial room for improvement.
50	- **W5 (Moderate): N=20 episodes per task type is modest.** Per-task claims (e.g., boil: 95.2 vs 38.4) lack per-task CIs. The aggregated CI pools across tasks, masking heterogeneity.
51	- **W6 (Minor): MATH track (Appendix E) lacks methodological detail.** No description of counterfactual data collection, router training, or sample sizes for MATH. Results are unverifiable.
52	- **W7 (Minor): Appendix C reveals sensitivity to labeling implementation.** Oracle jumps from -29.7 (MVP) to +8.7 (v3) — a 38.4-point swing from fixing tie-break logic. Were all 18 task types re-run with v3 code?
53	
54	### Questions to Authors (R1)
55	
56	1. What is the exact hindsight labeling criterion (1-step delta, episode-terminal, discounted return)? How are ties handled?
57	2. Does Table 2's implicit baseline use the 7B backbone for routing? Can you provide a 1.7B implicit control?
58	3. How sensitive are main results to the tie-break policy? Quantify the v3 vs MVP difference across all task types, not just boil.
59	4. For MATH (Appendix E): describe data collection, router training, and sample sizes.
60	5. Were all 18 task types evaluated with v3 code, or do some use older labeling logic?
61	6. Have you estimated oracle suboptimality with a multi-step oracle?
62	7. What is the false negative rate specifically on death-penalty steps (not aggregated)?
63	8. How are the three episode phases (early/mid/late) defined?
64	
65	---
66	
67	## R2: Novelty & Related Work
68	
69	### Strengths
70	
71	- **Clear problem scoping.** "When should an LLM defer to deterministic computation?" is a well-defined question with practical relevance beyond the specific benchmark.
72	- **Clean gain decomposition.** The 70% death-avoidance / 30% positive-guidance breakdown is the paper's most distinctive empirical insight — it tells us *why* routing helps, not just *that* it helps.
73	- **Well-controlled explicit/implicit ablation.** Same training data, same backbone — isolates the architectural choice (modulo the parameter confound noted in W2).
74	- **Appropriate short-paper scope.** The paper does not overclaim generality beyond ScienceWorld (MATH is correctly placed in appendix).
75	- **Honest limitations section.** Acknowledges ScienceWorld-only evaluation, simulator requirement, and DAgger gap.
76	
77	### Weaknesses
78	
79	- **W8 (Critical): Missing tool-use learning literature.** The core technique — SFT a small classifier to decide when to invoke an external tool — is well-explored in: Toolformer (Schick et al., 2024), ART (Paranjape et al., 2023), Chameleon (Lu et al., 2024), ToolkenGPT (Hao et al., 2024), CREATOR (Qian et al., 2023). None are cited. The framing as "routing to deterministic computation" obscures the connection to standard tool-use learning, making novelty claims appear inflated. The paper must position against this literature.
80	- **W9 (Major): "Routing to deterministic computation" ≈ tool-use learning.** The conceptual distinction — "this is safety-aware routing, not tool use" — is thin. An environment simulator *is* a tool; a code interpreter *is* a tool. The methodological pipeline (collect tool-use labels → SFT small model → selective invocation) is standard in the tool-use literature. The novelty must be argued on the *safety-aware* and *counterfactual labeling* dimensions, not the routing framing itself.
81	- **W10 (Major): Related work section is absent.** The paper has no dedicated Related Work section — all positioning is compressed into 2 paragraphs of the Introduction. This is inadequate for a contribution claiming novelty over multiple lines of work (world models, tool-use, reasoning-mode selection). Key distinctions from CogRouter, ReTool, and AgentMath are asserted in one sentence each without evidence.
82	- **W11 (Moderate): Implicit baseline may be unfairly weak.** SFT-training the 7B backbone to emit [SIMULATE] is one possible implicit design, but not the strongest. The tool-use literature has explored token-level triggers, adapter-based routing, and multi-head decision-making. The paper tests one specific (and arguably naive) implicit architecture and generalizes to "implicit routing is inferior."
83	- **W12 (Moderate): ScienceWorld's penalty structure inflates gains.** The -100 death penalty means a single routing error can collapse an entire episode score. This amplifies the difference between methods that avoid deaths (SimGate) and those that don't (always-internal). The 37.4-point gap is partly an artifact of the penalty function, not purely a measure of method quality. On a benchmark without catastrophic penalties, the advantage would likely be much smaller. This limits the generalizability of the quantitative claims.
84	- **W13 (Minor): Failure taxonomy is descriptive, not methodological.** FM1-FM5 are named categories of router decisions grouped post-hoc. This is useful analysis but is not a contribution on par with C1. Listing it as part of C2 inflates the contribution count.
85	- **W14 (Minor): Placeholder arXiv IDs.** ITP-R (2401.xxxxx), CogRouter (2405.xxxxx), ReTool (2504.xxxxx) have placeholder IDs. The cited comparison numbers (84.6, 62.58) are unverifiable.
86	
87	### Questions to Authors (R2)
88	
89	1. How does SimGate differ from Toolformer-style tool-use learning? Both SFT a model to decide when to invoke an external computation.
90	2. What is the expected SimGate gain on a benchmark without catastrophic (-100) penalties? The gain decomposition suggests ~11 points without death avoidance — how does this compare to baselines?
91	3. The implicit baseline uses a single [SIMULATE] token. Have you considered adapter-based or multi-head implicit architectures from the tool-use literature?
92	4. Can you provide a dedicated Related Work section positioning against Toolformer, ART, Chameleon, and ToolkenGPT?
93	5. Is the failure taxonomy stable under different random seeds, or would different counterfactual trajectories produce different FM distributions?
94	6. The 2-way vs 3-way result (p=0.08) suggests the fast/deep distinction has marginal value. Why present 3-way as the main system rather than the simpler 2-way?
95	
96	---
97	
98	## Step 3: Cross-Review Discussion
99	
100	### R1 → R2 feedback
101	R1 acknowledges R2's novelty critique as substantive: the missing tool-use literature (Toolformer, ART, etc.) is a genuine gap that weakens the paper's positioning. However, R1 argues the *counterfactual labeling via environment forking* is a methodological contribution not present in standard tool-use learning — Toolformer uses self-supervised API calls, not hindsight-labeled trajectory forking with death-avoidance signals. The safety-aware framing has genuine content if properly positioned.
102	
103	### R2 → R1 feedback
104	R2 agrees the hindsight labeling underspecification (W1) is the most actionable weakness — it's a solvable problem that would substantially strengthen the paper. R2 also endorses W2 (explicit/implicit confound) as the most damaging experimental weakness. On the oracle concern (W4), R2 notes this is related to the penalty structure issue (W12): the oracle looks near-optimal partly because the penalty function creates a binary success/failure landscape where any death-avoiding strategy looks good.
105	
106	### Consensus positions
107	1. **Missing tool-use literature is the paper's biggest positioning gap** (W8). Must be addressed in revision.
108	2. **Hindsight labeling criterion must be specified** (W1). Solvable.
109	3. **Explicit/implicit confound** (W2) weakens C2. A parameter-matched control is needed.
110	4. **The death-avoidance insight** (70% of gain) is the paper's most distinctive contribution and is genuinely useful — this is what differentiates it from generic tool-use learning.
111	5. **ScienceWorld penalty structure** (W12) means quantitative gains are benchmark-specific; the paper should discuss how gains would look without catastrophic penalties.
112	6. **Failure taxonomy** is useful analysis but should not be listed as a core contribution alongside C2.
113	
114	---
115	
116	## Step 4: Consolidated Assessment
117	
118	### Overall Score: **4 (Weak Accept, borderline)**
119	
120	### Confidence: 4/5
121	
122	### Decision Rationale
123	
124	**For acceptance:** The paper identifies a clean, practical problem (when should an LLM agent defer to deterministic computation?) and provides a well-executed empirical answer. The gain decomposition (70% death avoidance, 30% positive guidance) is an insight that advances understanding of agent failures. The ablation coverage — explicit/implicit, 2-way/3-way, router size, cross-task transfer, MATH generalization — is above average for a short paper. The modular design (lightweight router decoupled from backbone) is a defensible architectural choice with concrete benefits (lower false negatives, efficient simulator invocation). All 10 planned experiments are reported.
125	
126	**Against acceptance:** The novelty over existing tool-use learning methods (Toolformer, ART, Chameleon) is inadequately argued — the missing citations are a serious omission. The explicit/implicit comparison confounds architecture with parameter budget. The hindsight labeling criterion — the foundation of the training signal — is not specified. The primary benchmark (ScienceWorld) has an extreme penalty structure that amplifies gains, limiting generalizability of quantitative claims. The oracle may be suboptimal, undermining the "near-oracle" narrative.
127	
128	**Net assessment:** The empirical work is thorough and the death-avoidance insight is genuine, but the paper needs revision on positioning (tool-use literature), methodological specification (labeling criterion), and experimental controls (parameter-matched implicit baseline). At a 25% acceptance venue, this is a borderline paper that could go either way depending on the strength of the author response. The core contribution — demonstrating that modular safety-aware routing substantially reduces catastrophic agent failures — has practical value.
129	
130	### Actionable Revision Priorities
131	
132	1. **(Must-fix)** Add a Related Work section positioning against Toolformer, ART, Chameleon, ToolkenGPT. Articulate what counterfactual trajectory labeling provides that self-supervised tool-use learning does not.
133	2. **(Must-fix)** Specify the hindsight labeling criterion (comparison window, tie-break policy, handling of sparse rewards). Report sensitivity to these choices.
134	3. **(Must-fix)** Add a parameter-matched 1.7B implicit routing baseline to isolate architecture from capacity in the explicit/implicit comparison.
135	4. **(Should-fix)** Discuss how gains would look without catastrophic penalties (e.g., report scores excluding death-penalty episodes, or use a penalty-free variant).
136	5. **(Should-fix)** Report per-task confidence intervals, not just aggregated CIs.
137	6. **(Should-fix)** Add MATH methodological details (Appendix E).
138	7. **(Nice-to-have)** Fix placeholder arXiv IDs. Reproduce CogRouter under identical conditions if possible.
139	
140	### Experiment Coverage vs Plan
141	All 10 planned experiments appear in the paper: counterfactual collection (§2/App A), router training (§2/App B), end-to-end eval (§3.2), explicit/implicit (§3.3), routing analysis (§3.4), 2v3-way (§3.5/App D), boil rerun (App C), router size (§3.5), MATH (App E), cross-task transfer (App F). Coverage: **10/10 (100%)**.
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de8b3880-e081-428a-8667-53818a934061",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "4a32c8c2-cd1f-49d9-ad34-f442f91666f5",
  "sourceToolAssistantUUID": "de8b3880-e081-428a-8667-53818a934061",
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

_source line 43 · 2026-05-13T16:18:38.109Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JBoVWwmT454CGE5va291My`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a32c8c2-cd1f-49d9-ad34-f442f91666f5",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsSjh2vYTJYjjMQaudD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "697eada4-d60f-4eb3-bf31-42b87ee72203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CqFigLXW77wm4NnaLLGANg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9048,
      "cache_read_input_tokens": 37018,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 37018,
          "cache_creation_input_tokens": 9048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9048,
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

_source line 44 · 2026-05-13T16:18:38.113Z_

<details><summary>↩ Tool result · `toolu_01JBoVWwmT454CGE5va291My`</summary>

```text
1	---
2	dream_id: dream_20260513T153257
3	tier: median
4	overall_score: 3/6 Weak Reject
5	timestamp: 2026-05-13T16:16:20.928250+00:00
6	---
7	
8	
9	# Dream Review Report: SimGate — Safety-Aware Routing Between LLM Reasoning and Deterministic Computation
10	
11	**dream_id:** 20260513T153257  
12	**Paper:** SimGate: Safety-Aware Routing Between LLM Reasoning and Deterministic Computation for Agent Tasks  
13	**Review mode:** full (2 Reviewers + Roundtable)  
14	**Date:** 2026-05-13
15	
16	---
17	
18	## Roundtable Summary
19	
20	| Reviewer | Focus | Preliminary Score | Final Score |
21	|----------|-------|-------------------|-------------|
22	| R1 | Methods + Experiments | 4/6 (Weak Accept) | 3/6 (Weak Reject) |
23	| R2 | Novelty + Related Work | 3/6 (Weak Reject) | 3/6 (Weak Reject) |
24	| **Consensus** | | | **3/6 (Weak Reject)** |
25	
26	R1 initially scored 4/6, recognizing the well-structured ablation suite and honest positioning. After cross-review, R1 revised downward to 3/6 upon agreeing with R2's critical observation that the core pipeline (counterfactual labeling → SFT a small classifier → selective tool invocation) is standard in the tool-use learning literature (Toolformer, ART, ToRA), which the paper entirely fails to cite. Both reviewers converged on: **the empirical death-avoidance finding is the paper's genuine contribution, but it is benchmark-specific and insufficient alone for a top venue without proper positioning and broader validation.**
27	
28	---
29	
30	## Step 1: Independent Reviews
31	
32	### R1 (Methods + Experiments) — Score: 4/6 → revised to 3/6
33	
34	**Strengths:**
35	1. Well-designed two-stage counterfactual pipeline (pre-screening 20 types → 13 selected, then full trajectory collection). Resource-efficient and methodologically sound.
36	2. Strong ablation structure: 5 internal baselines + oracle upper bound + 2 external references in Table 1. Oracle gap of only 3.0 points demonstrates router captures most learnable signal.
37	3. Honest handling of negative results — does not claim SOTA over CogRouter (84.6 vs 78.2), acknowledges router accuracy ceiling from label noise.
38	4. Parameter-matched explicit vs. implicit comparison (Table 3): 1.7B-vs-1.7B isolates architectural effect from capacity confound. The +4.7 (p=0.03) result is the cleanest evidence for C2.
39	5. Mechanistic interpretability: r=0.91 correlation between internal death rate and SimGate gain is a clear, falsifiable mechanistic account. Phase-dependent routing (52% at mid-episode) aligns with the safety-net narrative.
40	6. Bootstrap 90% CIs reported throughout with proper separation between SimGate and always-internal CIs.
41	
42	**Weaknesses:**
43	1. **(Critical) "Always-internal" baseline may use fork-based lethal action filtering.** If the always-internal condition accesses the simulator for death-checking, the +21.4 headline gap is measured against an already-hybrid baseline, not pure LLM reasoning. The paper does not clarify this. If true, the framing "LLM reasoning vs. deterministic computation" is methodologically misleading.
44	2. **(Major) Hindsight counterfactual labels may have systematic tie-break bias.** With strict `>` tie-breaking in a sparse-reward environment where 95%+ steps have zero score delta, a large fraction of "deterministic-preferred" labels may be tie-break artifacts rather than genuine signal. The 38.5% deterministic label rate and 18.5% label noise may be partially artifactual. The paper does not report what fraction of labels come from genuine score differences vs. ties.
45	3. **(Major) Router accuracy (71.2%) is only ~10pp above the majority-class baseline (61.5%).** F1 for the deterministic class (0.68) is notably lower than internal (0.74), meaning the router struggles on the decisions that matter most for the safety-net claim. Majority-class baseline and per-class precision/recall are not reported.
46	4. **(Moderate) No analysis of train/test distribution shift.** Router trained on base-policy trajectories but deployed on routing-modified trajectories. The DAgger-style distribution mismatch is acknowledged in future work but not quantified.
47	5. **(Moderate) CogRouter/ITP-R comparisons are not apples-to-apples.** CogRouter uses RL trajectory optimization; ITP-R uses a learned world model rather than ground-truth simulator. Neither isolates the variable the paper cares about.
48	6. **(Moderate) MATH results are preliminary.** +7.5 gain (vs +21.4 on ScienceWorld), router accuracy 63%, catastrophic error reduction only 28%. Suggests the framework is ScienceWorld-specific rather than general.
49	7. **(Minor) Scale: 260 episodes, 6240 labeled steps is small.** Per-task CIs in Table 2 are likely wide with only 20 episodes per type. No multiple-comparison correction reported for the 13 per-task tests.
50	
51	**Key questions:**
52	- Does always-internal use fork-based death filtering? If so, what is pure-internal performance?
53	- What fraction of counterfactual labels are genuine (strict score difference) vs. tie-break artifacts?
54	- What is SimGate's advantage on non-death episodes only (isolating safety-net from positive guidance)?
55	- Why 90% CI instead of conventional 95%?
56	
57	### R2 (Novelty + Related Work) — Score: 3/6
58	
59	**Strengths:**
60	1. Well-defined, practically relevant research question with controlled experimental answer.
61	2. Death-avoidance gain decomposition (r=0.91) is the paper's most distinctive empirical insight — it explains *why* routing helps, not just *that* it helps.
62	3. Dense ablation suite for a short paper: 6 baselines, explicit/implicit, 2-way/3-way, router size, cross-domain, MATH.
63	4. Honest positioning that avoids overclaiming.
64	
65	**Weaknesses:**
66	1. **(Critical) Missing tool-use learning literature.** The core pipeline is standard in tool-use learning (Toolformer, ART, Chameleon, ToolkenGPT, CREATOR, ToRA — all uncited). "Routing to deterministic computation" is conceptually equivalent to tool-use selection. Without positioning against this literature, the paper implicitly claims the entire routing framework as novel, which it is not.
67	2. **(Critical) No dedicated Related Work section.** All positioning compressed into 2 Introduction paragraphs. Missing coverage: MoE routing, neuro-symbolic integration, LLM agent frameworks (ReAct, Reflexion), safe LLM agents, formal verification. Only 6 references total.
68	3. **(Major) ScienceWorld's -100 penalty inflates gains.** The penalty structure amplifies measured differences — a single routing error collapses an entire episode. MATH results confirm: without catastrophic penalties, advantage shrinks by 65%. The paper should separate safety-net value from positive-guidance value.
69	4. **(Major) Implicit baselines may be unfairly weak.** Only one implicit design tested (SFT to emit [SIMULATE]). Richer alternatives exist (ToolkenGPP adapter heads, ART multi-step planning). The 7B implicit (74.8, p=0.08) already narrows the gap.
70	5. **(Moderate) Routing pattern analysis is descriptive, not methodological.** Phase-dependent trends and 2/4 "diffuse" failure clusters are post-hoc observations, not stable enough to count as a contribution.
71	6. **(Moderate) Placeholder arXiv IDs for CogRouter, ITP-R, ReTool make comparison numbers unverifiable.**
72	7. **(Minor) A rule-based heuristic routing state-change actions (heat, cool, mix, react) to the simulator could capture most gains, given the routing pattern analysis. This simpler baseline is absent.**
73	
74	**Novelty assessment:** The method is an instantiation of known tool-use learning techniques. The distinctive contribution is the empirical death-avoidance finding (r=0.91), which is genuinely useful but benchmark-specific. Proper positioning would shrink apparent novelty to this empirical observation + the controlled explicit/implicit comparison — likely below threshold for a 25% acceptance venue without broader benchmarks.
75	
76	---
77	
78	## Step 2: Cross-Sharing Key Observations
79	
80	**R1 → R2:** R2's tool-use literature gap is well-taken. On re-examination, the counterfactual labeling pipeline is indeed a variant of Toolformer's label-collection approach, applied to sequential decision-making. The paper should have positioned itself as: "we apply tool-use learning to agent safety in environments with catastrophic penalties, and find that the primary mechanism is death avoidance." This would be a more honest and defensible framing.
81	
82	**R2 → R1:** R1's concern about the always-internal baseline potentially using fork-based death filtering is important — if confirmed, the headline +21.4 number is against an already-augmented baseline, making the contribution seem larger than it is. The tie-break label bias concern compounds: if many labels are artifactual AND the baseline is hybrid, the entire empirical edifice becomes shakier.
83	
84	**Shared observation:** Both reviewers noted that the MATH track results (+7.5, router accuracy 63%) actually *undermine* rather than support the paper's generality claims. The "safety-aware routing" framing is tied to ScienceWorld's extreme penalty structure.
85	
86	---
87	
88	## Step 3: Convergence Discussion
89	
90	**Points of agreement:**
91	1. The death-avoidance mechanism finding (r=0.91) is the paper's genuine contribution — it provides a causal explanation for *when* deterministic computation helps LLM agents.
92	2. The ablation suite is strong for a short paper — well-structured, many baselines, honest about negative results.
93	3. The missing tool-use literature is a fatal positioning gap. Without citing Toolformer et al., the paper claims methodological novelty it does not possess.
94	4. The paper is well-written, appropriately scoped, and honest. These are necessary but not sufficient for acceptance.
95	5. ScienceWorld's penalty structure is both the paper's strength (clear signal for safety-aware routing) and its weakness (inflated effect sizes, benchmark-specific insight).
96	
97	**Points of remaining disagreement:**
98	- R1 weighs the experimental rigor more heavily and sees the controlled ablations as near-sufficient for a borderline accept if the baseline and positioning issues are fixed.
99	- R2 considers the novelty gap structural — even with perfect positioning, the contribution is an empirical finding on one benchmark, which is below threshold for a top venue.
100	- After discussion, R1 revised to 3/6, agreeing that the novelty gap cannot be fully overcome by experimental quality alone.
101	
102	**Consensus position:** 3/6 (Weak Reject). The paper has real strengths — honest framing, dense ablations, a genuine empirical insight — but two structural problems prevent acceptance: (1) the method is standard tool-use learning, entirely unpositioned against that literature, and (2) the primary finding is tied to a single benchmark's extreme penalty structure, with the MATH generalization attempt confirming rather than mitigating this concern.
103	
104	---
105	
106	## Step 4: Consolidated Assessment
107	
108	### Overall Score: 3/6 (Weak Reject)
109	### Confidence: 4/5
110	
111	### Verdict
112	The paper presents a well-executed empirical study of when deterministic computation helps LLM agents, with the key finding that routing value is proportional to catastrophic failure risk (r=0.91). The ablation suite is thorough and the positioning against CogRouter is honest. However, two structural issues place this below the acceptance threshold for a top ML venue:
113	
114	1. **Novelty:** The core method (counterfactual labeling → SFT classifier → selective tool invocation) is standard in the tool-use learning literature (Toolformer, ART, ToRA, etc.), which is entirely uncited. The paper's distinctive contribution is an empirical observation, not a new method.
115	
116	2. **Generality:** The "safety-aware routing" framing depends on ScienceWorld's extreme -100 death penalty. The MATH generalization (gain drops from +21.4 to +7.5, router accuracy drops from 71% to 63%) confirms the insight is benchmark-specific. One additional environment with catastrophic penalties would substantially strengthen the paper.
117	
118	### Actionable Recommendations for Revision
119	
120	1. **Add a Related Work section** citing Toolformer, ART, ToRA, ToolkenGPP, Chameleon, and MoE routing. Explicitly articulate what counterfactual trajectory labeling provides beyond Toolformer's self-supervised approach (answer: hindsight labels from environment forking, which is more principled for sequential decision-making).
121	
122	2. **Clarify the always-internal baseline.** Does it use fork-based death filtering? If so, add a pure-internal baseline (no simulator access) and a death-filtered-internal baseline (simulator only for death avoidance, no routing). This decomposition directly tests the safety-net mechanism claim.
123	
124	3. **Report gains with and without death episodes.** Separate safety-net value (avoiding -100) from positive-guidance value (better action selection on non-catastrophic steps). If the paper's claim is "death avoidance is the primary mechanism," this decomposition is essential evidence.
125	
126	4. **Report majority-class baseline** (61.5%) alongside router accuracy (71.2%) and per-class precision/recall. The ~10pp gap is thin and readers need this context.
127	
128	5. **Add a rule-based routing baseline** (route state-change actions to simulator, everything else to internal). If the learned router substantially outperforms this, it demonstrates learned signal beyond action-type keywords.
129	
130	6. **Add one more environment with catastrophic penalties** (e.g., ALFWorld with irreversible actions, or a custom ScienceWorld variant with graduated penalties). This would separate the insight from the specific benchmark.
131	
132	7. **Report tie-break analysis:** What fraction of counterfactual labels come from genuine score differences vs. tie-breaking? Train on strict-only labels and report the effect on router accuracy and end-to-end performance.
133	
134	### Experiment Coverage vs. Design
135	All 10 planned experiments (plan-001a through plan-010) are reflected in the paper. Coverage is complete. The issue is not missing experiments but missing baselines (pure-internal, rule-based routing, death-decomposition) and missing positioning (tool-use literature).
136	
137	### What Would Change the Score
138	- **To 4/6 (Weak Accept):** Fix related work, clarify baseline, add death-decomposition analysis, add rule-based routing baseline. This addresses the positioning gap and strengthens the empirical claims within the ScienceWorld scope.
139	- **To 5/6 (Accept):** All of the above, plus one additional environment with catastrophic penalties demonstrating the safety-aware routing finding generalizes beyond ScienceWorld.
140	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "697eada4-d60f-4eb3-bf31-42b87ee72203",
  "isSidechain": true,
  "promptId": "9df72bde-7089-4762-bd57-52f27fdcc238",
  "agentId": "a8fbc54ecf55e0717",
  "type": "user",
  "uuid": "2e34b415-6a6e-4217-b44f-3edfac8dd1a6",
  "sourceToolAssistantUUID": "697eada4-d60f-4eb3-bf31-42b87ee72203",
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

_source line 45 · 2026-05-13T16:20:18.884Z_

Now I have comprehensive understanding of both the paper under review (the "worst" scenario, which matches the task description) and the project context. Let me now produce my review as R2 (Novelty and Related Work).

---

## Review: "When Does Deterministic Computation Help LLM Agents? A Diagnostic Study on ScienceWorld"

**Reviewer R2 — Focus: Novelty and Related Work**

---

### 1. Summary

This paper introduces a counterfactual evaluation methodology that forks agent trajectories at each decision step across three computation modalities (fast internal, deep CoT, deterministic simulation), applies it to 15 ScienceWorld task types (300 episodes, 6,600 labeled steps), and reports predominantly negative results: a learned per-step router (SimGate, 65.2) is statistically indistinguishable from always-simulate (64.8), explicit and implicit routing architectures perform equivalently, and routing patterns do not transfer across domains. The positive finding is that deterministic computation helps only on 4/15 death-risk task types involving physical state transitions.

---

### 2. Strengths (Novelty + Related Work Focus)

**S1. Well-defined, practically relevant question.** "When does deterministic computation help?" is a useful question for the LLM agent community. The paper commits to answering it with controlled experiments rather than presenting a method paper with inflated claims.

**S2. Honest negative-result framing.** The paper does not attempt to disguise weak routing results. The pivot from a method paper to a diagnostic study is intellectually honest, and the conclusions (per-step routing is the wrong granularity; task-level decisions are the actionable lever) are clearly stated and supported by the data.

**S3. Clean per-task diagnostic partition.** The 4-death-risk vs. 11-other-task separation is the paper's most distinctive empirical contribution. It provides actionable guidance: practitioners should identify catastrophic-failure-prone task categories and apply deterministic computation unconditionally within them, rather than building step-level routers.

**S4. Controlled experimental design within scope.** Five ablation baselines (always-internal, always-det, random, confidence-threshold, oracle) with the same backbone and evaluation protocol. The negative results across explicit/implicit, 2-way/3-way, and router size ablations form a coherent picture rather than cherry-picked findings.

**S5. Appropriate scope calibration.** The paper does not overclaim generality. The Discussion section acknowledges single-benchmark, single-backbone limitations.

---

### 3. Weaknesses (Novelty + Related Work Focus)

**W1 (Critical): The core pipeline is standard tool-use learning, entirely unpositioned against that literature.** The method -- collect labels for when to invoke an external tool, SFT-train a small classifier, selectively invoke at inference -- is the established paradigm in tool-use learning. The following works are directly relevant and uncited:

- **Toolformer** (Schick et al., NeurIPS 2024): Self-supervised learning of when to call APIs. The label-collection mechanism differs (self-supervision vs. counterfactual forking), but the downstream pipeline (train model to predict tool invocation) is identical.
- **ART** (Paranjape et al., 2023): Automatic multi-step tool use with task-level planning. Directly addresses when/how to invoke external computation.
- **Chameleon** (Lu et al., NeurIPS 2024): Plug-and-play compositional reasoning with tool use. Modular architecture with tool selection.
- **ToolkenGPT** (Hao et al., NeurIPS 2024): Augments LLM vocabulary with tool tokens -- an implicit routing mechanism that should be compared to the paper's implicit baseline.
- **CREATOR** (Qian et al., 2023): Tool creation and selective invocation for reasoning tasks.

Without positioning against this literature, the paper implicitly claims the routing framework as novel. It is not. The paper must explicitly argue what counterfactual trajectory forking with hindsight scoring provides beyond Toolformer-style self-supervised labeling -- the answer (principled labels for sequential decision-making with sparse rewards) exists but is never articulated.

**W2 (Critical): No dedicated Related Work section.** The entire related work consists of 2 Introduction paragraphs naming 8 references. For a paper claiming to introduce a "counterfactual evaluation methodology" and reporting diagnostic findings across an established benchmark, this is inadequate. Missing lines of work include:

- **Adaptive computation / early exit**: Mixture-of-Depths (Raposo et al., 2024), Universal Transformers (Dehghani et al., 2019), CALM (Schuster et al., 2022). These learn when to allocate additional computation per token/step -- the same fundamental question.
- **Mixture-of-Experts routing**: Switch Transformers (Fedus et al., 2022), GShard (Lepikhin et al., 2021). Router/gating mechanisms for selective computation are well-studied in the MoE literature.
- **World models for agents**: DreamerV3 (Hafner et al., 2023), IRIS (Micheli et al., 2023). These learn approximate world models for agent planning -- ITP-R is cited but the broader world-model literature is absent.
- **Safe RL / constrained agents**: Safe RL (Garcia & Fernandez, 2015), constrained MDPs. The "safety-aware" framing invokes safety concepts without citing the safety literature.
- **Neuro-symbolic integration**: Logic-LM (Pan et al., 2023), SatLM (Ye et al., 2024). Selective invocation of symbolic solvers for LLM reasoning is closely related.
- **Negative-result studies in NLP/ML**: The paper positions as a negative-result contribution but does not cite the tradition of negative-result papers or discuss what makes a negative result publishable (non-obvious hypothesis, sufficient experimental power, actionable takeaways).

**W3 (Major): The counterfactual evaluation methodology has limited novelty.** Fork-and-evaluate is a standard technique in causal inference and counterfactual reasoning for sequential decision-making. The specific instantiation here (fork at each step, roll out under three modalities, label with hindsight) is a straightforward application of importance-weighted off-policy evaluation ideas to modality selection. The paper does not discuss connections to:

- Off-policy evaluation in RL (Precup et al., 2000; Dudik et al., 2011)
- Counterfactual trajectory analysis (Buesing et al., 2019)
- A/B testing at the step level (multi-armed bandits with contextual features)

Without these connections, the "methodology" contribution appears more novel than it is.

**W4 (Major): The negative result may be expected rather than surprising.** The finding that "learned per-step routing adds no value over always-simulate in ScienceWorld" can be predicted from first principles:

- ScienceWorld has sparse rewards (95%+ steps have zero score delta), making per-step labeling nearly degenerate.
- The oracle ceiling is only 5.2 points above always-det (70.0 vs. 64.8), meaning the theoretical maximum for routing is small.
- 42% of labels are ambiguous, meaning the training signal is inherently noisy.

A reader familiar with sparse-reward environments and the limitations of SFT on noisy labels would predict this outcome. The paper does not argue that this negative result was non-obvious ex ante, which weakens its contribution as a negative-result paper.

**W5 (Major): Placeholder arXiv IDs undermine verifiability.** CogRouter (arXiv:2405.XXXXX) and ITP-R (arXiv:2405.XXXXX) have placeholder identifiers. The comparison numbers (84.6 and 62.58) cannot be verified. For a paper that cites these as its primary positioning references, this is a serious issue. If these papers do not exist or report different numbers, the entire framing collapses.

**W6 (Moderate): ScienceWorld's penalty structure confounds the diagnostic finding.** The -100 death penalty means a single hallucinated state transition collapses an entire episode score. The 4-death-risk vs. 11-other partition may simply reflect "tasks where the LLM backbone ever triggers the -100 penalty" vs. "tasks where it doesn't." This is more a property of the benchmark's reward design than a deep insight about when deterministic computation helps. On a benchmark with graduated penalties (or no death mechanic), the sharp partition would likely dissolve into a continuum.

**W7 (Moderate): "Routing to deterministic computation" is conceptually equivalent to tool-use selection.** The paper frames its contribution as a routing/gating problem, but an environment simulator is a tool. The methodological distinction between "routing" and "tool use" is never argued. If the paper instead said "we train a classifier to decide when to use a tool (the simulator), and find that task-level tool selection beats step-level selection," the novelty shrinks to the empirical observation on ScienceWorld.

**W8 (Minor): The 8 cited references are insufficient for any venue.** A 4-page short paper should still engage with the relevant literature. Eight references, two with placeholder IDs, is substantially below the norm even for workshop papers.

---

### 4. Questions to Authors

1. How does the counterfactual labeling methodology differ from Toolformer-style self-supervised tool-use labeling, beyond the domain of application? What prevents applying Toolformer's approach to ScienceWorld?

2. The oracle ceiling (70.0) is only 5.2 points above always-deterministic. Was this known before running the router experiments? If so, what was the prior expectation for SimGate's improvement over always-det?

3. Can you provide the actual arXiv IDs for CogRouter and ITP-R? The placeholder IDs (2405.XXXXX) make the comparison numbers unverifiable.

4. The implicit routing baseline uses a single design (backbone emits [SIMULATE] token). Have you considered adapter-based or multi-head implicit architectures from the tool-use literature (e.g., ToolkenGPT)?

5. What is the SimGate advantage when computed only on non-death episodes? If the safety-net mechanism is removed from the analysis, does any positive routing signal remain?

6. The paper argues routing patterns are task-specific (cross-domain accuracy drops 8-13 points). But the routing features described in Section 3.5 (temperature/heat/phase-change keywords) suggest a simple rule-based heuristic. How does a keyword-matching baseline perform?

7. Is the 4-death-risk vs. 11-other partition robust to backbone choice? Would a stronger backbone (e.g., Qwen2.5-72B) reduce death rates on these 4 tasks, thereby eliminating the routing signal entirely?

---

### 5. Novelty Assessment

**Is the counterfactual methodology genuinely novel?** Partially. The specific instantiation (fork ScienceWorld environments at each step, roll out under three modalities, label with episode-terminal score) is a reasonable engineering contribution, but the underlying idea -- evaluate alternative decisions via counterfactual rollouts -- is standard in off-policy RL and causal inference. The paper does not connect to this literature, making the contribution appear more novel than it is.

**Is the negative-result framing a sufficient contribution?** Marginally. The finding that per-step routing provides no advantage over always-simulate is mildly informative, but it can be largely predicted from the problem structure (sparse rewards, low oracle ceiling, noisy labels). A stronger negative-result paper would either (a) test a hypothesis that the community widely believes to be true, or (b) provide a theoretical explanation for why the negative result holds. This paper does neither convincingly -- the "community belief" that per-step routing helps is not well-established (the tool-use literature mostly operates at a coarser granularity already), and the explanation (sparse rewards + noisy labels) is descriptive rather than theoretical.

**Comparison to existing work on tool-use routing:** The paper's method is a direct instantiation of the Toolformer paradigm applied to environment simulation in sequential decision-making. The claimed novelty over tool-use learning is never articulated. The death-avoidance finding is the genuine distinctive element, but it is specific to ScienceWorld's penalty structure.

---

### 6. Related Work Gaps

The following important related work is missing (organized by subfield):

| Subfield | Missing References | Relevance |
|----------|-------------------|-----------|
| Tool-use learning | Toolformer, ART, Chameleon, ToolkenGPT, CREATOR | Core pipeline is standard here |
| Adaptive computation | Mixture-of-Depths, CALM, Universal Transformers | Same "when to allocate more compute" question |
| MoE routing | Switch Transformers, GShard, Expert Choice | Router/gating mechanisms |
| World models | DreamerV3, IRIS, WorldDreamer | ITP-R cited but literature absent |
| Safe RL | Garcia & Fernandez survey, constrained MDPs | "Safety-aware" framing requires this |
| Neuro-symbolic | Logic-LM, SatLM, PAL | Selective symbolic computation for LLMs |
| Off-policy evaluation | Precup et al., Dudik et al. | Counterfactual methodology foundations |
| LLM agent frameworks | Voyager, DEPS, AgentBench, WebArena | Broader agent evaluation context |

The 8-reference bibliography is the weakest I have seen in a submission to a top venue. Even accounting for the short-paper format, this level of engagement with prior work is insufficient.

---

### 7. Significance Rating: 2/5

The paper's significance is limited by three factors: (1) the core method is standard tool-use learning, (2) the diagnostic finding (4 death-risk tasks out of 15) is specific to ScienceWorld's penalty structure and Qwen2.5-7B's capabilities, and (3) the negative result (per-step routing does not help) is largely predictable from the problem structure. The actionable takeaway ("use task-level computation planning, not step-level routing") has some practical value but is not surprising to practitioners familiar with the limitations of fine-grained routing in sparse-reward settings.

---

### 8. Overall Score: 2/6 (Reject)

The paper is honest, well-structured, and presents a clean experimental design within its scope. However, it fails to meet the acceptance threshold for a top ML venue on three grounds:

1. **Novelty.** The method is standard tool-use learning, entirely unpositioned against that literature. The counterfactual methodology has connections to off-policy RL that are unacknowledged. The remaining novelty is a single empirical observation (death-risk task partition) on one benchmark.

2. **Significance.** The negative result (routing does not help) is predictable from the problem structure. The positive result (4 death-risk tasks) is specific to ScienceWorld's penalty design and one backbone. The paper does not demonstrate that the diagnostic finding generalizes.

3. **Related work.** Eight references (two with placeholder IDs) is unacceptable. Multiple directly relevant subfields (tool-use learning, adaptive computation, safe RL, MoE routing, off-policy evaluation) are entirely absent.

The paper would benefit from: (a) a proper Related Work section engaging with tool-use learning, (b) validation on at least one additional environment with catastrophic penalties, (c) a rule-based routing baseline to calibrate the learned router's value, and (d) a theoretical or empirical argument that the negative result was non-obvious.

---

### 9. Confidence: 4/5

I am confident in this assessment. I am familiar with the tool-use learning, adaptive computation, and LLM agent literatures. The main uncertainty is whether the CogRouter and ITP-R comparisons would hold under verified citations -- the placeholder arXiv IDs prevent verification. The experimental methodology within ScienceWorld appears sound, but my novelty and related-work concerns are structural and would not change with additional experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e34b415-6a6e-4217-b44f-3edfac8dd1a6",
  "isSidechain": true,
  "agentId": "a8fbc54ecf55e0717",
  "requestId": "req_011CazsTPze2twBN9Enennch",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca86506c-741a-4ee4-a965-0c2b66ce0c89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "cf927c35-53a0-4107-b5fc-888888fb1cc5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012NXSwakpfm4Z4aSyQ1e2mk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8658,
      "cache_read_input_tokens": 46066,
      "output_tokens": 3836,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3836,
          "cache_read_input_tokens": 46066,
          "cache_creation_input_tokens": 8658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8658,
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
