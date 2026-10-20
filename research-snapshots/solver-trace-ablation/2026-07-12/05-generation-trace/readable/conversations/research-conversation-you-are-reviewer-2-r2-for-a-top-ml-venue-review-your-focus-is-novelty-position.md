# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty, positioning, and related work**. Review the 

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab6c520c6c7f9a8aa.jsonl`
- **Structured JSON:** [`ddaa7a41e415f10c3cdc.json`](../../sessions/dd/ddaa7a41e415f10c3cdc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-13T22:42:37.935Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus is **novelty, positioning, and related work**. Review the following paper and produce a structured review.

## Paper Summary

**Title:** "Solver Trace Ablation Reveals Reward Hacking in GRPO-Trained Formalizers: A Principled Negative Result"

**Core idea:** The paper introduces Solver Trace Ablation (STA), a framework grounded in the RIP (Reachability-Infection-Propagation) model from mutation testing, for deriving structural rewards (ISR = Intensional Structural Reward) from solver execution traces. STA systematically ablates proof components and re-runs the solver to measure structural necessity. The paper reports a principled negative result: STA works as a diagnostic (detecting ~70% of degenerate outputs) but fails as a training reward (reduces prove rate from 0.24 to 0.11 without improving structural quality).

**Three claimed contributions:**
1. STA as diagnostic framework: 5-step derivation protocol + ISR metric that detects 74% of exec-only GRPO outputs as structurally degenerate
2. STA as training reward fails: principled negative result with mechanistic explanation (gradient variance amplification in low-prove-rate regime)
3. Hacking taxonomy: 200-sample annotation (κ=0.72) identifying 4 hacking modes with differential ISR sensitivity

**Key experimental results:**
- Exec-only GRPO: prove rate rises 0.15→0.28 over 500 steps, but ISR/PR drops 0.82→0.29
- Exec+STA: prove rate only 0.13 at step 500, ISR/PR=0.27 (worse on both dimensions)
- Base model ISR/PR=0.53 > both trained models
- SFT: PR=0.30, ISR/PR=0.50, hack%=50% — dominates GRPO on all metrics
- 4 hacking modes: tautology injection (28%), vacuous quantification (19%), premise redundancy (14%), trivial conclusion (8%)
- Prolog STA instantiation failed; SMT-LIB and 8B scaling not attempted
- No positive cross-logic transfer

**Model:** Qwen2.5-1.5B on FOLIO-format FOL tasks with Prover9

**Related work cited:**
- GRPO: Shao et al. 2024 (DeepSeekMath)
- Reward hacking: Skalse et al. 2022
- Reward overoptimization: Gao et al. 2023
- Mutation testing/RIP: Jia & Harman 2011
- Structural rewards: ExecVerify, EGCA, Mellgren et al. (Prolog-specific penalties)
- EVOM mentioned for cross-solver GRPO

**Only 4 references total in the bibliography.**

## Your Review Focus

Evaluate:
1. **Novelty**: How novel is the STA/ISR framework? Is adapting RIP from mutation testing to RL reward design a genuine intellectual contribution? Is the negative result itself novel or predictable?
2. **Related work completeness**: Only 4 references. Are there critical missing citations? (Consider: RLHF/reward hacking literature, neurosymbolic reasoning, formal verification + LLMs, process reward models, outcome vs. process rewards, mutation testing beyond Jia & Harman, structural rewards in code generation, GRPO variants, etc.)
3. **Positioning**: Is the paper well-positioned relative to prior work? Does it clearly differentiate itself?
4. **Significance**: Would this paper advance the field? Is the negative result actionable for future researchers?
5. **Scope and generalizability**: Single logic type, single small model — how generalizable are the claims?
6. **Writing quality**: Is the narrative coherent? Does the "principled negative result" framing work?

## Output Format

```
## R2 Review: Novelty & Related Work

### Summary
[2-3 sentences]

### Strengths
[Bulleted list, 4-6 items]

### Weaknesses
[Bulleted list, 4-6 items, each with severity: minor/moderate/major]

### Questions for Authors
[3-5 specific questions]

### Detailed Comments
[Paragraph-level analysis of novelty, positioning, missing related work]

### Scores
- Novelty: [1-4]
- Related Work: [1-4]
- Significance: [1-4]
- Writing Quality: [1-4]
- Overall recommendation: [1-6, where 1=Strong Reject, 6=Strong Accept]
- Confidence: [1-5]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "cb8da310-c5bb-4f7c-8664-20c8a03aaca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T22:42:37.938Z_

```json
{
  "parentUuid": "cb8da310-c5bb-4f7c-8664-20c8a03aaca1",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
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
  "uuid": "5aa55a52-a1d7-4b10-8479-c3af52c1ee2e",
  "timestamp": "2026-05-13T22:42:37.938Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T22:42:40.910Z_



I'll start by reading the paper and related project files to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aa55a52-a1d7-4b10-8479-c3af52c1ee2e",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NjkdCCdAZtMLxkT98k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7612ed50-21e8-4047-b38c-91e3bd475569",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxprzJXoLG11GuTCmQXZUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6959,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6959,
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

_source line 4 · 2026-05-13T22:42:41.974Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MPBrsLibaXeHxCCbENUXcr`</summary>

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
  "parentUuid": "7612ed50-21e8-4047-b38c-91e3bd475569",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NjkdCCdAZtMLxkT98k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e69bf742-d25e-4b21-8d87-d0d10fc51aa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxprzJXoLG11GuTCmQXZUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6959,
      "cache_read_input_tokens": 8250,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6959
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 107,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 6959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6959,
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

_source line 5 · 2026-05-13T22:42:41.978Z_

<details><summary>↩ Tool result · `toolu_01MPBrsLibaXeHxCCbENUXcr`</summary>

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
  "parentUuid": "e69bf742-d25e-4b21-8d87-d0d10fc51aa4",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "bf796ff0-2592-460f-ab20-050c973fb0a3",
  "sourceToolAssistantUUID": "e69bf742-d25e-4b21-8d87-d0d10fc51aa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T22:42:45.371Z_



Let me read the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf796ff0-2592-460f-ab20-050c973fb0a3",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nk49PrpJrRuqrWTG7C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9ec8af9-78af-4fcc-861e-450033eec6f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLbExVJ6aHWEZ4U1WF3Zkx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 15209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 7 · 2026-05-13T22:42:46.590Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RjaXTHkGB2ddA7TX4iwA3c`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9ec8af9-78af-4fcc-861e-450033eec6f4",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nk49PrpJrRuqrWTG7C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6960ffa8-d33c-4b97-92fe-ea1c71325f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLbExVJ6aHWEZ4U1WF3Zkx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 15209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 8 · 2026-05-13T22:42:46.611Z_

<details><summary>↩ Tool result · `toolu_01RjaXTHkGB2ddA7TX4iwA3c`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **sta-phase1-exec-sta-r5** (success): —\\n- **sta-phase1-exec-only-r5** (success): —\\n- **sta-phase1-exec-sta-r4** (negative): —\\n\\n## 趋势\\n成功 4 / 负向 2 / 失败 6 / 共 12\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\n\\n## 告警\\n- sta-phase1-exec-only: 训练失败 — unknown\\n- sta-phase1-exec-sta: 训练失败 — unknown\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\\n\", \"total_chars\": 570, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6960ffa8-d33c-4b97-92fe-ea1c71325f07",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "88f52f1c-86d8-4ff5-b549-447d236c43f3",
  "sourceToolAssistantUUID": "6960ffa8-d33c-4b97-92fe-ea1c71325f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T22:42:46.918Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017Ldz3Hqxmnm6HM9e6DUP5b`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88f52f1c-86d8-4ff5-b549-447d236c43f3",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nk49PrpJrRuqrWTG7C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ea8442f-c56f-4088-bc21-66f234203536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLbExVJ6aHWEZ4U1WF3Zkx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 15209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 10 · 2026-05-13T22:42:46.940Z_

<details><summary>↩ Tool result · `toolu_017Ldz3Hqxmnm6HM9e6DUP5b`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ea8442f-c56f-4088-bc21-66f234203536",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "9081303d-fde4-423d-8326-d019461a89d2",
  "sourceToolAssistantUUID": "0ea8442f-c56f-4088-bc21-66f234203536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T22:42:47.518Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017dL5HeTuYizt4ysCJM3hGX`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9081303d-fde4-423d-8326-d019461a89d2",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nk49PrpJrRuqrWTG7C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81a9ab4f-ac60-44c4-a647-2f077f3b1d35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLbExVJ6aHWEZ4U1WF3Zkx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 15209,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1289
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 307,
          "cache_read_input_tokens": 15209,
          "cache_creation_input_tokens": 1289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1289,
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

_source line 12 · 2026-05-13T22:42:47.532Z_

<details><summary>↩ Tool result · `toolu_017dL5HeTuYizt4ysCJM3hGX`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81a9ab4f-ac60-44c4-a647-2f077f3b1d35",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "b8d5fbb7-640e-48f3-b084-b639737b0b1b",
  "sourceToolAssistantUUID": "81a9ab4f-ac60-44c4-a647-2f077f3b1d35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T22:42:53.330Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VD7dKbrVFMnQAVZ3EHZDnh`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8d5fbb7-640e-48f3-b084-b639737b0b1b",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NkfrUshPkuLB29tPVL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff847e96-aa1d-4d95-bd67-8f7e615cd892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172W5PnRj2SiyRHykmfkUr7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 985,
      "cache_read_input_tokens": 16498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 985,
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

_source line 14 · 2026-05-13T22:42:53.340Z_

<details><summary>↩ Tool result · `toolu_01VD7dKbrVFMnQAVZ3EHZDnh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ROADMAP.md\", \"content\": \"# solver-trace-ablation — Research Dashboard\\n\\n> 最后更新: 2026-05-13 22:16 UTC | 更新原因: Kill Criteria #4 量化阈值（Reviewer 建议）：3-seed mean < 25% AND last100 slope ≤ 0\\n\\n## 核心方向\\nSTA（Solver Trace Ablation）：首次将 mutation testing RIP 框架系统性引入 RL reward design，为 neurosymbolic formalizer 的 GRPO 训练提供 intensional verification reward。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 部分通过——STA 机制有效但训练集成权重需调整）\\n- **基础设施**: westd-39279 × 2 RTX PRO 6000 96GB ✅\\n- **MVP 结论**: full STA 连续 ISR 有区分力（GT=0.56 vs model=0.064）；但 50/50 权重导致 prove_rate 退化至 baseline 以下（0.10 < 0.12）；O(1) fast_isr 无效\\n- **MVP Pass**: #1✅ #2✅ #3✅ #4❌(ISR指标不可比) #5❌(accuracy差5pp+退化) | Kill criteria 未触发\\n- **⚠️ 因果归因未定**: ISR/PR 下降可能是检测 hacking 也可能是 STA 权重惩罚效应，plan_003 是消歧实验（D005）\\n- **Dream**: dream_20260513T215750 pending\\n- **Agent 状态**: 正在处理，队列有 P0 训练指令待执行\\n\\n## 实验计划摘要（详见 experiment_plan.yaml）\\n- **P0**（~13h）: FOL 500步×3seed + eval + O(1)vsO(N) + weight ablation\\n- **P1**（~8h）: Prolog + multi-logic + SFT baseline + hacking annotation\\n- **P2**（~9h）: SMT-LIB + 8B scaling\\n- **Pivotal**: plan_003（因果消歧）+ plan_005（weight ablation）共同决定 \\\"STA as reward\\\" vs \\\"STA as monitor\\\" 叙事\\n\\n## Research Phase Kill Criteria\\n1. plan_005 所有权重配比（0.1/0.2/0.3 + bonus mode + curriculum）均无法让 exec+STA ≥ exec-only → 论文退化为 \\\"STA as monitoring metric\\\"，claim 力度大幅减弱，与用户讨论是否继续\\n2. plan_001/002（500步3seed）STA 条件一致性差于 exec-only → 同上\\n3. plan_003 held-out eval 确认 ISR/PR 下降但非 hacking（人工标注 plan_012 无 shortcut 证据）→ \\\"检测 hacking\\\" claim 不成立，需重写 story\\n4. plan_001 exec-only 500步 prove_rate 未达阈值 → GRPO+exec reward 本身未产生提升，问题在基座训练而非 STA，需重新评估整个 GRPO pipeline\\n   - **硬阈值**: 3-seed 均值 prove_rate < 25%（baseline 12% 的 ~2倍）**且** last-100-step prove_rate 趋势斜率 ≤ 0（不再上升）\\n   - 两个条件同时满足才触发 kill；若均值 < 25% 但斜率仍正（仍在学习），延长到 800 步再判\\n\\n## 近期任务（GPU 排列）\\n- [ ] cuda:0 → plan_001: exec-only 500步 seed=42（baseline + Kill Criteria #4）\\n- [ ] cuda:1 → plan_003: exec-only checkpoint full STA eval（消歧，eval-only 快速）→ 完成后 plan_005: sta_weight=0.1 训练\\n- [ ] 并行准备: Prolog STA instantiation + SFT baseline 数据\\n- [ ] Dream 回调后评估 framing/plan 是否调整\\n- [ ] registry 修正: exec-sta-r5 conclusion → \\\"negative\\\"\\n\\n## GPU 预算\\n- 本地: westd-39279 × 2 RTX PRO 6000 96GB（cuda:0, cuda:1）\\n- 云: 暂不需要\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-13 | paper_framing.md \\\"检测 hacking\\\" claim 降级为观察性表述，plan_ | sta-phase1-exec-sta-r5, plan_003 |\\n| D005 | 2026-05-13 | ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验 | sta-phase1-exec-sta-r5, sta-phase1-exec-only-r5 |\\n| D004 | 2026-05-13 | Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化） | sta-phase1-exec-sta-r5, sta-phase1-exec-only-r5 |\\n| D003 | 2026-05-13 | Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重 | sta-phase1-exec-only-r4, sta-phase1-exec-sta-r4 |\\n| D002 | 2026-05-13 | MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline +  | — |\\n| D001 | 2026-05-13 | MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA r | — |\\n\\n\\n\", \"total_chars\": 2869, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff847e96-aa1d-4d95-bd67-8f7e615cd892",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "2c432c0d-a82b-4e3e-b937-9e10abc2afaf",
  "sourceToolAssistantUUID": "ff847e96-aa1d-4d95-bd67-8f7e615cd892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T22:42:54.281Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TXdL7fsiLvrbi2wVLjYouy`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c432c0d-a82b-4e3e-b937-9e10abc2afaf",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NkfrUshPkuLB29tPVL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f618ffc5-9517-4c7c-b4ce-8617ec7e1792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172W5PnRj2SiyRHykmfkUr7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 985,
      "cache_read_input_tokens": 16498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 985,
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

_source line 16 · 2026-05-13T22:42:54.293Z_

<details><summary>↩ Tool result · `toolu_01TXdL7fsiLvrbi2wVLjYouy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (2 条，精简自原始 5 条)\\n\\n### Claim 1: STA as Reward Design Methodology\\nSolver Trace Ablation (STA), grounded in the Reachability-Infection-Propagation (RIP) framework from mutation testing theory, provides a **general, solver-agnostic procedure** for deriving intensional verification rewards from solver execution semantics. For any solver+language pair, a 5-step derivation protocol (pilot → collect shortcuts → classify → map RIP → design check) produces domain-specific structural rewards. This is the first application of the RIP framework to RL reward design.\\n\\n**MVP 证据**: Full STA 在 FOL+Prover9 上提供连续 ISR（0.125-0.889），训练过程中观察到 ISR/PR 比从 64%→33% 的下降趋势。O(1) 近似（tautology-only check）信号过粗无效——重要阴性结果，证明了 full component ablation 的必要性。\\n**⚠️ 因果归因待验证**: ISR/PR 下降可能是 (A) STA 检测到 hacking，也可能是 (B) 50/50 STA 权重抑制 prove 行为的惩罚效应（ISR 绝对值始终 ~0.05 ≈ pretrained 水平）。plan_003（exec-only checkpoint 用 full STA 评估）是消歧实验——完成前不可用 \\\"检测 hacking\\\" 因果表述。\\n\\n### Claim 2: Multi-Logic GRPO Empirical Findings\\nMulti-logic GRPO training across structurally different formal languages (FOL→Prover9, Prolog→SWI-Prolog, SMT-LIB→Z3) exhibits measurable cross-logic transfer patterns and logic-type-specific reward hacking modes. STA-derived rewards detect and quantify these phenomena.\\n\\n**MVP 证据**: 待验证（FOL 单逻辑已验证，multi-logic 需 research 阶段实验）。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with solver-verified rewards trains formalizers that achieve high execution accuracy but produce structurally degenerate outputs (reward hacking). Existing structural reward designs are ad-hoc heuristics with no principled derivation.\\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) demonstrates cross-solver GRPO transfer but uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work provides a general derivation procedure for structural rewards from solver semantics.\\n- **Our framing**: We adapt the RIP framework from mutation testing — a component is \\\"necessary\\\" iff its ablation changes the solver's output — to derive intensional verification rewards. STA fills the **dense + automatic** cell in the ORM-PRM reward taxonomy (ORM=sparse+automatic, PRM=dense+manual, STA=dense+automatic via solver semantics). This positions STA not as \\\"a new algorithm\\\" but as \\\"the first systematic transfer of mutation testing methodology to RL reward design.\\\"\\n- **Headline result template**: \\\"On FOLIO/ProofWriter/LogiQA, STA-rewarded GRPO achieves &lt;X>% formalization accuracy with &lt;Y>% ISR, compared to &lt;Z>% accuracy / &lt;W>% ISR for execution-only GRPO — maintaining accuracy while detecting and reducing structural degeneracy.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EMNLP fit**: Core contribution is neurosymbolic (NLP + formal logic), directly in the NLP and Symbolic Reasoning track. Formal verification + RL reward design is highly relevant.\\n- **\\\"Old wine\\\" risk**: STA's component ablation resembles mutation testing. Mitigation: explicitly acknowledge the RIP origin, claim novelty at the methodology transfer level + empirical findings, not at the algorithm level.\\n- **Scope breadth risk**: Original proposal had 5 contributions — trimmed to 2 core (STA methodology + empirical findings). MLSR framework, hacking taxonomy, STA-IPT duality are secondary analysis within these 2 contributions.\\n- **Single-logic risk**: If only FOL results are available, paper may feel narrow. Mitigation: at minimum include Prolog as second logic type; SMT-LIB as stretch goal.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"STA is just mutation testing applied to FOL\\\"** — Response: yes, that's the point. The contribution is the systematic transfer + empirical validation that it works as RL reward, not algorithmic novelty. The 5-step derivation protocol is the transferable methodology.\\n2. **\\\"O(1) approximation doesn't work\\\"** — Response: this is a feature, not a bug. We report it as a principled negative result showing that domain-specific hacking modes require corresponding ablation granularity.\\n3. **\\\"Low prove rate limits GRPO signal\\\"** — Response: addressed by K=8+ and difficulty-based data selection. Prove rate increases during training (12%→15-20%).\\n4. **\\\"ISR/PR ratio declining even with STA reward\\\"** — Response: 100-step pilot is too short; full runs with curriculum will show whether STA prevents or just detects degradation. Even detection alone is a contribution (monitoring tool).\\n5. **\\\"Only tested on one/two logic types\\\"** — Response: STA derivation protocol is solver-agnostic by design; instantiations for additional logic types follow the same 5-step procedure.\\n\", \"total_chars\": 4814, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f618ffc5-9517-4c7c-b4ce-8617ec7e1792",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "dc5548cb-1dd4-4c2e-9e3a-77760d30e67b",
  "sourceToolAssistantUUID": "f618ffc5-9517-4c7c-b4ce-8617ec7e1792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T22:42:55.060Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015F1iziz92baXSHnHffx4bu`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc5548cb-1dd4-4c2e-9e3a-77760d30e67b",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NkfrUshPkuLB29tPVL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5abf6bf9-9c6b-4516-96a5-80a90ccb3667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172W5PnRj2SiyRHykmfkUr7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 985,
      "cache_read_input_tokens": 16498,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 985
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 16498,
          "cache_creation_input_tokens": 985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 985,
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

_source line 18 · 2026-05-13T22:42:55.074Z_

<details><summary>↩ Tool result · `toolu_015F1iziz92baXSHnHffx4bu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# solver-trace-ablation — Memory\\n\\n## 环境信息 (2026-05-13)\\n\\n### westd-39279 服务器\\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2, Z3 4.16.0.0\\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\\n- **代码路径**: `/root/solver-trace-ablation/`\\n\\n### 决策记录\\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\\n- Prover9 从 LADR 源码编译（apt 无包）\\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\\n\\n## 数据 (2026-05-13)\\n\\n### 数据源变更：ProofWriter → FOLIO\\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\\n- Phase 0 子集 100 条，训练子集 500 条\\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\\n\\n## Phase 0 关键发现 (2026-05-13)\\n\\n### Base Model ISR Baseline (sta-phase0-baseline)\\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\\n\\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\\n- **MVP Pass #2 验证**: GT ISR 0.559 > 0.5 ✅，好的 formalization ISR 高\\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\\n\\n### Prover9 局限性\\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\\n- Phase 1 训练中 reward 信号主要来自 `true` 类样本\\n\\n### ISR 已知盲区\\n- premise-conclusion 重复的 trivial formalization 可能获高 ISR\\n- 需在论文 Discussion 中讨论此局限\\n\\n## Phase 1 关键经验 (2026-05-13)\\n\\n### fast_isr_fol 失败教训 (r4)\\n- `fast_isr_fol()` 是二值 tautology gate (0/1)，Qwen3-4B 不产生 tautology → ISR ≡ prove_rate → 两条件零差异\\n- **教训：binary ISR 无法提供有意义的 reward shaping 信号，必须用连续 ISR**\\n\\n### full STA reward 成功验证 (r5) — MVP PASS ✅\\n**配置变更**: r4→r5: `fast_sta_reward` → `sta_reward` (continuous ISR) + K=4→8\\n\\n| 指标 | exec-only (r5) | exec-sta (r5) | Δ |\\n|------|----------------|---------------|---|\\n| overall prove_rate | 0.151 | 0.100 | +0.051 |\\n| overall isr_mean | 0.148 | 0.043 | +0.104 |\\n| last-20 prove_rate MA | 0.200 | 0.150 | +0.050 |\\n| last-20 isr_mean MA | 0.200 | 0.050 | **+0.150** |\\n| ISR/PR ratio (last-20) | 1.000 | 0.330 | — |\\n\\n**核心发现**:\\n1. exec-only: isr_mean ≡ prove_rate（100步无例外）— binary ISR 是冗余信号\\n2. exec-sta: isr_mean << prove_rate（overall 43%, last-20 仅 33%）— continuous ISR 真正度量质量\\n3. **Reward hacking 早期信号**: exec-sta prove_rate +85% 但 ISR 平坦 (-4%)，ISR/PR 比从 64%→33%。模型学会更多 proof 但 formalization 质量下降\\n4. K=8 比 K=4 有效减少全零 batch（但 prove_rate 整体仍偏低 10-20%）\\n5. step 速度: exec-only ~9.4s, exec-sta ~10.1s（STA overhead 约 7%，可接受）\\n\\n### GPU 隔离教训 (r3)\\n- `CUDA_VISIBLE_DEVICES` 必须在 `bash -c` 内部设置，不能依赖外部 shell 继承\\n- 两进程未隔离 → 都加载到 GPU 0 → OOM (SIGKILL 137)\\n\\n### Config merge 教训 (r2)\\n- argparse `store_true` 默认 False（非 None），`is None` 检查跳过 YAML 值\\n- 修复：`parser.set_defaults(**yaml_cfg)` 后重新 parse CLI args\\n\\n### reward_log.jsonl 隔离问题\\n- 多轮 run 数据追加到同一文件，分析时必须按 timestamp 过滤\\n- 后续应每次 run 使用独立 output_dir\\n\\n## MVP 总结 (2026-05-13)\\n\\n| Pass 标准 | r4 | r5 | 说明 |\\n|-----------|-----|-----|------|\\n| #1 STA ISR 可靠运行 | ⚠️ | ✅ | solver 100%, ~10s/step |\\n| #2 ISR 有区分度 | ❌ | ✅ | GT 0.559 vs base 0.064; continuous ISR 解耦 |\\n| #3 ISR 趋势分离 | ❌ | ✅ | last-20 ISR: 0.200 vs 0.050 (Δ=0.150) |\\n| #4 accuracy 无崩溃 | ✅ | ✅ | prove_rate 两组均提升 |\\n\\n**MVP PASS。项目进入全实验矩阵阶段。**\\n\", \"total_chars\": 3433, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5abf6bf9-9c6b-4516-96a5-80a90ccb3667",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "ab4cafcb-dee9-44fa-bf9f-4148fd72d9a5",
  "sourceToolAssistantUUID": "5abf6bf9-9c6b-4516-96a5-80a90ccb3667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T22:42:59.027Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H3HFdNgcuLE2eST7JnPLm6`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab4cafcb-dee9-44fa-bf9f-4148fd72d9a5",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nm22vK13gQQWfn6ViA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab2d7b1b-2345-437b-9d96-34f3c06b794d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MaFRvvKjkhN3pMRVNpyqgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6007,
      "cache_read_input_tokens": 17483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6007,
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

_source line 20 · 2026-05-13T22:42:59.042Z_

<details><summary>↩ Tool result · `toolu_01H3HFdNgcuLE2eST7JnPLm6`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab2d7b1b-2345-437b-9d96-34f3c06b794d",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "96104200-4ac7-481e-8c85-2d4aba30eb12",
  "sourceToolAssistantUUID": "ab2d7b1b-2345-437b-9d96-34f3c06b794d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T22:42:59.517Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JKo2CUouCs7S1rkCxA7jwF`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "ARCHITECTURE.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96104200-4ac7-481e-8c85-2d4aba30eb12",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nm22vK13gQQWfn6ViA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ed6b032-1439-46bc-9558-96a83988054c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MaFRvvKjkhN3pMRVNpyqgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6007,
      "cache_read_input_tokens": 17483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6007,
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

_source line 22 · 2026-05-13T22:42:59.542Z_

<details><summary>↩ Tool result · `toolu_01JKo2CUouCs7S1rkCxA7jwF`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ARCHITECTURE.md found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ed6b032-1439-46bc-9558-96a83988054c",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "2c0d40c4-56bb-4d9e-8a83-fc3bceb02db3",
  "sourceToolAssistantUUID": "0ed6b032-1439-46bc-9558-96a83988054c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T22:43:00.037Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011kbmGqCkwGkzngZdkwe5So`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c0d40c4-56bb-4d9e-8a83-fc3bceb02db3",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nm22vK13gQQWfn6ViA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d308d2a-be21-455a-aba5-fc51254b62bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MaFRvvKjkhN3pMRVNpyqgt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6007,
      "cache_read_input_tokens": 17483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6007,
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

_source line 24 · 2026-05-13T22:43:00.072Z_

<details><summary>↩ Tool result · `toolu_011kbmGqCkwGkzngZdkwe5So`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d308d2a-be21-455a-aba5-fc51254b62bf",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "5584f3f5-6e6f-49d1-8971-f6a7a6cf7d57",
  "sourceToolAssistantUUID": "0d308d2a-be21-455a-aba5-fc51254b62bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T22:43:08.832Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011XcerWK1LDnHfrm7rtxLWM`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5584f3f5-6e6f-49d1-8971-f6a7a6cf7d57",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NmPML2uAnH8fJKTodQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7df4178-fdf1-47bb-a00e-67ec9e5277a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYudLMax5XAAMf2AioXDzW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 23490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 550,
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

_source line 26 · 2026-05-13T22:43:08.858Z_

<details><summary>↩ Tool result · `toolu_011XcerWK1LDnHfrm7rtxLWM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7df4178-fdf1-47bb-a00e-67ec9e5277a2",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "46baca3f-b08c-4abe-80bb-f195e5bca51d",
  "sourceToolAssistantUUID": "d7df4178-fdf1-47bb-a00e-67ec9e5277a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T22:43:09.751Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Wqc2J7Jdav51DuvReUimG4`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46baca3f-b08c-4abe-80bb-f195e5bca51d",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NmPML2uAnH8fJKTodQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e06c9bb-cd7a-4445-bf2b-7f59dd4fdb29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYudLMax5XAAMf2AioXDzW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 23490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 550,
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

_source line 28 · 2026-05-13T22:43:09.769Z_

<details><summary>↩ Tool result · `toolu_01Wqc2J7Jdav51DuvReUimG4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 7\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差\\n    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)\\n    避免惩罚。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: prove_rate=0.10 < baseline, STA reward 过于惩罚性\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: control\\n    result: prove_rate=0.15, 复现 r4\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 22:13 UTC\\n  summary: ISR/PR 下降因果归因待验证，plan_003 提升为最高优先级消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 有两种解释：(A) STA 检测到 hacking (B) 50/50 权重抑制 prove\\n    行为的惩罚效应。ISR 绝对值 ~0.05 ≈ pretrained 水平支持解释 B。plan_003（用 full STA 评估 exec-only checkpoint）是唯一消歧实验——exec-only\\n    ISR 高→STA reward 导致退化；exec-only ISR 低→GRPO 通病。paper_framing.md 已将 claim 降级为观察性表述，因果表述需等\\n    plan_003 结果。cuda:1 排列改为 plan_003 eval 先行，再 plan_005 training。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence\\n    result: ISR/PR 下降但因果不清\\n  - exp_id: sta-phase1-exec-only-r5\\n    role: baseline\\n    result: prove_rate=0.12, ISR 未用 full STA 评估\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-13 22:14 UTC\\n  summary: paper_framing.md \\\"检测 hacking\\\" claim 降级为观察性表述，plan_003 为消歧实验\\n  rationale: Reviewer 指出 ISR/PR 64%→33% 下降存在混淆效应：可能是 STA 检测到 hacking，也可能是 50/50 权重抑制\\n    prove 行为。ISR 绝对值始终 ~0.05 ≈ pretrained 水平，更像惩罚效应。plan_003（exec-only checkpoint\\n    用 full STA 评估）是消歧实验——完成前 paper 不可用因果表述。已修改 paper_framing.md Claim 1 MVP 证据段。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-sta-r5\\n    role: evidence_source\\n    result: ISR/PR 下降观察到但因果不清\\n  - exp_id: plan_003\\n    role: disambiguation\\n    result: planned\\n  depends_on:\\n  - D004\\n\", \"total_chars\": 3352, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e06c9bb-cd7a-4445-bf2b-7f59dd4fdb29",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "d8336ca1-5096-40d2-9c6c-79217c0c9ea6",
  "sourceToolAssistantUUID": "4e06c9bb-cd7a-4445-bf2b-7f59dd4fdb29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T22:43:10.121Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RDmYEEVGDRm9CZaTJY1WqP`</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8336ca1-5096-40d2-9c6c-79217c0c9ea6",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NmPML2uAnH8fJKTodQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "faaa27c6-85e8-4eab-8c99-87143f0fcfb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYudLMax5XAAMf2AioXDzW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 23490,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 550
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 23490,
          "cache_creation_input_tokens": 550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 550,
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

_source line 30 · 2026-05-13T22:43:10.129Z_

<details><summary>↩ Tool result · `toolu_01RDmYEEVGDRm9CZaTJY1WqP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faaa27c6-85e8-4eab-8c99-87143f0fcfb0",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "32579943-6cb8-4c02-94df-c981fecad97e",
  "sourceToolAssistantUUID": "faaa27c6-85e8-4eab-8c99-87143f0fcfb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-13T22:43:31.723Z_

Now let me look at the actual paper artifacts and code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32579943-6cb8-4c02-94df-c981fecad97e",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nn8U9bVpTYKCope6XS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac2ad147-2151-4c11-8b67-39b8ed7a58c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBbfyj2iSkba8SgLJeebCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2534,
      "cache_read_input_tokens": 24040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2534,
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

_source line 32 · 2026-05-13T22:43:33.153Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QzqRZca8qM5Bn9oEzJSHJW`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac2ad147-2151-4c11-8b67-39b8ed7a58c6",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nn8U9bVpTYKCope6XS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8c258d9-ef43-45bc-85f9-fc04a2979d93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBbfyj2iSkba8SgLJeebCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2534,
      "cache_read_input_tokens": 24040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2534,
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

_source line 33 · 2026-05-13T22:43:33.170Z_

<details><summary>↩ Tool result · `toolu_01QzqRZca8qM5Bn9oEzJSHJW`</summary>

```text
artifacts/dream_reports/dream_20260513T215750/best/paper.tex
artifacts/dream_reports/dream_20260513T215750/median/paper.tex
artifacts/dream_reports/dream_20260513T215750/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8c258d9-ef43-45bc-85f9-fc04a2979d93",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "c2bf8b2c-d66a-4030-b773-c04015e084d3",
  "sourceToolAssistantUUID": "f8c258d9-ef43-45bc-85f9-fc04a2979d93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T22:43:33.620Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DdfGew3gnps2qRpqEZapAF`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2bf8b2c-d66a-4030-b773-c04015e084d3",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nn8U9bVpTYKCope6XS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01ae8333-8981-49fc-be56-cc9ee00fde90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBbfyj2iSkba8SgLJeebCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2534,
      "cache_read_input_tokens": 24040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2534,
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

_source line 35 · 2026-05-13T22:43:33.632Z_

<details><summary>↩ Tool result · `toolu_01DdfGew3gnps2qRpqEZapAF`</summary>

```text
artifacts/train_grpo.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01ae8333-8981-49fc-be56-cc9ee00fde90",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "ca3db031-218f-4a5d-a7b9-502cbe198698",
  "sourceToolAssistantUUID": "01ae8333-8981-49fc-be56-cc9ee00fde90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T22:43:34.198Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019LLnfVNicUAGpmSMyNzmQP`</summary>

```json
{
  "pattern": "artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca3db031-218f-4a5d-a7b9-502cbe198698",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nn8U9bVpTYKCope6XS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff5e6065-b1fb-4372-aee2-d1afcc429d8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBbfyj2iSkba8SgLJeebCL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2534,
      "cache_read_input_tokens": 24040,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2534
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 272,
          "cache_read_input_tokens": 24040,
          "cache_creation_input_tokens": 2534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2534,
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

_source line 37 · 2026-05-13T22:43:34.218Z_

<details><summary>↩ Tool result · `toolu_019LLnfVNicUAGpmSMyNzmQP`</summary>

```text
artifacts/sta-phase0-baseline/data/phase0_baseline_summary.txt
artifacts/manifest.yaml
artifacts/launch_phase1.sh
artifacts/grpo_exec_only.yaml
artifacts/grpo_exec_sta.yaml
artifacts/phase1_r2_diagnosis.md
artifacts/train_grpo.py
artifacts/diagnose_phase1_r3.md
artifacts/dream_reports/dream_20260513T215750/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T215750/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T215750/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T215750/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T215750/best/experiment_data.json
artifacts/dream_reports/dream_20260513T215750/best/paper_framing.md
artifacts/dream_reports/dream_20260513T215750/best/paper.tex
artifacts/dream_reports/dream_20260513T215750/best/paper.aux
artifacts/dream_reports/dream_20260513T215750/best/paper.out
artifacts/dream_reports/dream_20260513T215750/best/paper.pdf
artifacts/dream_reports/dream_20260513T215750/best/paper.log
artifacts/dream_reports/dream_20260513T215750/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T215750/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T215750/median/experiment_data.json
artifacts/dream_reports/dream_20260513T215750/median/paper_framing.md
artifacts/dream_reports/dream_20260513T215750/median/paper.tex
artifacts/dream_reports/dream_20260513T215750/median/paper.aux
artifacts/dream_reports/dream_20260513T215750/median/paper.out
artifacts/dream_reports/dream_20260513T215750/median/paper.pdf
artifacts/dream_reports/dream_20260513T215750/median/paper.log
artifacts/dream_reports/dream_20260513T215750/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260513T215750/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T215750/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T215750/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T215750/worst/paper.tex
artifacts/dream_reports/dream_20260513T215750/worst/paper.aux
artifacts/dream_reports/dream_20260513T215750/worst/paper.out
artifacts/dream_reports/dream_20260513T215750/worst/paper.pdf
artifacts/dream_reports/dream_20260513T215750/worst/paper.log
artifacts/dream_reports/dream_20260513T215750/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260513T215750/logs/orchestrator.log
artifacts/dream_reports/dream_20260513T215750/best/review_context.yaml
artifacts/dream_reports/dream_20260513T215750/best/review_report.md
artifacts/dream_reports/dream_20260513T215750/logs/review_best.log
artifacts/dream_reports/dream_20260513T215750/median/review_context.yaml
artifacts/dream_reports/dream_20260513T215750/median/review_report.md
artifacts/dream_reports/dream_20260513T215750/logs/review_median.log
artifacts/dream_reports/dream_20260513T215750/worst/review_context.yaml
artifacts/dream_reports/dream_20260513T215750/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff5e6065-b1fb-4372-aee2-d1afcc429d8d",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "8f0376d1-ce7a-4fed-97d8-dfdb1800a6c9",
  "sourceToolAssistantUUID": "ff5e6065-b1fb-4372-aee2-d1afcc429d8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-13T22:43:37.902Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Bh3UihxpiFqu3ZzQjHvi2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f0376d1-ce7a-4fed-97d8-dfdb1800a6c9",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NouXLn2fukg5mdyqFQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07986ea4-b51d-4d8d-baf9-0c9918f10375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kowok375TDKd3wQ6M6Ekxj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 26574,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 101,
          "cache_read_input_tokens": 26574,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1432,
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

_source line 39 · 2026-05-13T22:43:38.224Z_

<details><summary>↩ Tool result · `toolu_017Bh3UihxpiFqu3ZzQjHvi2`</summary>

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
11	\usepackage[colorlinks=true,citecolor=blue,linkcolor=blue]{hyperref}
12	\usepackage{natbib}
13	\renewcommand{\bibsection}{\section*{References}}
14	
15	\title{Solver Trace Ablation: Dense Structural Rewards for\\Formal Reasoning via Mutation Testing}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	% ============================================================
23	\begin{abstract}
24	Training language models to produce formal logical representations via reinforcement learning (e.g., GRPO with solver-verified rewards) achieves high execution accuracy but introduces \emph{structural degeneracy}: models discover extensional shortcuts---tautological premises, vacuous quantifiers, over-constrained formulas---that satisfy solvers without encoding the intended logical content. We propose \textbf{Solver Trace Ablation (STA)}, a reward design methodology grounded in the Reachability-Infection-Propagation (RIP) framework from mutation testing theory. STA derives dense, automatic structural rewards by systematically ablating components of solver inputs and measuring their contribution to solver outcomes. We introduce a 5-step derivation protocol that instantiates STA for any solver--language pair. Experiments with GRPO training of Qwen3-4B and Qwen3-8B across three formal languages---first-order logic (Prover9), Prolog (SWI-Prolog), and SMT-LIB (Z3)---demonstrate that STA-rewarded training maintains prove rates comparable to execution-only training (0.30 vs.\ 0.28 for FOL) while preserving structural integrity (ISR/PR ratio 0.65 vs.\ 0.35). On held-out evaluation, STA-trained models reduce reward hacking prevalence from 45\% to 18\%. We further show that the O(1) tautology-only approximation fails as a reward signal, validating the necessity of full component ablation. Multi-logic training exhibits positive cross-logic transfer, and STA's benefits are scale-invariant from 4B to 8B parameters.
25	\end{abstract}
26	
27	% ============================================================
28	\section{Introduction}
29	\label{sec:intro}
30	
31	Reinforcement learning with execution-based rewards has emerged as a powerful paradigm for training language models to produce formal logical representations \cite{mellgren2025prolog,evom2026}. Group Relative Policy Optimization (GRPO) with solver-verified correctness rewards enables models to discover proving strategies beyond supervised demonstrations, achieving substantial accuracy gains over supervised finetuning.
32	
33	However, execution-only reward signals create a fundamental misalignment: any output that makes the solver return ``proved'' receives equal reward, regardless of whether the formalization faithfully encodes the intended logical content. This misalignment manifests as \emph{structural degeneracy}---the model learns extensional shortcuts that satisfy the solver without encoding meaningful logical structure. We document five categories of such shortcuts: tautological premises ($\forall x.\, P(x) \lor \neg P(x)$), vacuous quantifiers, redundant clauses, over-constrained formulas, and trivial unification chains.
34	
35	Standard evaluation metrics (prove rate, accuracy) are blind to this phenomenon. A model exhibiting 45\% hacking prevalence appears indistinguishable from a structurally sound model when measured by execution accuracy alone. This is the classic reward hacking signature: the proxy metric (solver verification) improves while the latent quality dimension (structural fidelity) degrades.
36	
37	We propose \textbf{Solver Trace Ablation (STA)}, a methodology for deriving dense, automatic structural rewards from solver execution semantics. STA adapts the Reachability-Infection-Propagation (RIP) framework from mutation testing theory: a component of a formal expression is \emph{structurally necessary} if and only if its ablation (removal) changes the solver's output. This yields the \textbf{Intensional Structure Ratio (ISR)}, a continuous metric that quantifies the fraction of structurally necessary components.
38	
39	STA occupies the \textbf{dense + automatic} cell in the ORM-PRM reward taxonomy: unlike outcome reward models (ORM, sparse + automatic) or process reward models (PRM, dense + manual), STA provides fine-grained, per-component feedback without requiring human annotation. The key insight is that solver semantics already encode structural information---STA extracts it through systematic ablation.
40	
41	Our contributions are:
42	\begin{enumerate}
43	\item A \textbf{general derivation protocol} for structural rewards: a 5-step procedure (pilot $\to$ collect shortcuts $\to$ classify $\to$ map RIP $\to$ design checks) that instantiates STA for any solver--language pair. We demonstrate instantiations for FOL/Prover9, Prolog/SWI-Prolog, and SMT-LIB/Z3.
44	\item \textbf{Empirical evidence} that STA-rewarded GRPO is Pareto-improving over execution-only GRPO: matching prove rate while maintaining structural integrity (ISR/PR ratio 0.65 vs.\ 0.35), with benefits persisting on held-out evaluation and across model scales (4B--8B).
45	\item A \textbf{principled negative result}: O(1) approximations to STA (single-check shortcuts) fail because domain-specific hacking modes require correspondingly granular ablation.
46	\end{enumerate}
47	
48	% ============================================================
49	\section{Related Work}
50	\label{sec:related}
51	
52	\paragraph{RL for Formal Reasoning.}
53	GRPO and related policy gradient methods have been applied to formal theorem proving \cite{polu2020gpt}, code generation \cite{le2022coderl}, and natural-language-to-logic translation \cite{mellgren2025prolog}. EVOM \cite{evom2026} demonstrates cross-solver GRPO transfer using scalar execution rewards. These approaches share a common limitation: execution-only rewards provide no signal about structural quality.
54	
55	\paragraph{Structural Rewards in RL.}
56	Process reward models (PRMs) provide step-level supervision for mathematical reasoning \cite{lightman2023verify} but require human annotation. ExecVerify and EGCA derive trace-level rewards for code from execution traces, but do not address formal logic. Mellgren et al.\ hand-craft Prolog-specific structure penalties. Our work provides the first \emph{general derivation procedure} for structural rewards from solver semantics.
57	
58	\paragraph{Mutation Testing.}
59	Mutation testing evaluates test suite adequacy by introducing small syntactic changes (mutants) and checking whether tests detect them \cite{jia2011analysis}. The RIP framework formalizes mutation adequacy: a mutant must be \emph{reachable}, must \emph{infect} the program state, and the infection must \emph{propagate} to the output. We adapt this framework from test evaluation to reward design---instead of measuring test quality, we measure formalization quality.
60	
61	% ============================================================
62	\section{Method}
63	\label{sec:method}
64	
65	\subsection{Problem Setting}
66	
67	Given a natural language premise--hypothesis pair $(p, h)$, a formalization model $\pi_\theta$ generates a formal expression $f = \pi_\theta(p, h)$ in logic $\mathcal{L}$ (e.g., FOL, Prolog, SMT-LIB). A solver $S$ determines whether $f$ entails the hypothesis: $S(f) \in \{\texttt{proved}, \texttt{failed}\}$. Standard GRPO uses the binary execution reward $r_{\text{exec}}(f) = \mathbb{1}[S(f) = \texttt{proved}]$.
68	
69	\subsection{Solver Trace Ablation}
70	
71	\paragraph{Component Decomposition.}
72	We decompose $f$ into $n$ components $\{c_1, \ldots, c_n\}$ according to $\mathcal{L}$'s syntax. For FOL, components are individual premises (axioms); for Prolog, clauses (rules/facts); for SMT-LIB, assertions and declarations.
73	
74	\paragraph{Ablation and ISR.}
75	For each component $c_i$, we construct the ablated expression $f_{-i} = f \setminus \{c_i\}$ and evaluate $S(f_{-i})$. Component $c_i$ is \emph{structurally necessary} if $S(f_{-i}) \neq S(f)$---removing it changes the solver outcome. The \textbf{Intensional Structure Ratio} is:
76	\begin{equation}
77	\text{ISR}(f) = \frac{1}{n} \sum_{i=1}^{n} \mathbb{1}[S(f_{-i}) \neq S(f)]
78	\label{eq:isr}
79	\end{equation}
80	ISR ranges from 0 (no component is necessary---fully degenerate) to 1 (every component is necessary---maximally structured). ISR is computed only for proved outputs ($S(f) = \texttt{proved}$); for unproved outputs, ISR is undefined.
81	
82	\paragraph{RIP Mapping.}
83	STA's theoretical grounding comes from the RIP framework. For a component $c_i$ in formal expression $f$:
84	\begin{itemize}
85	\item \textbf{Reachability}: $c_i$ is syntactically reachable from the query/goal.
86	\item \textbf{Infection}: $c_i$'s content binds variables or introduces constraints used downstream.
87	\item \textbf{Propagation}: Removing $c_i$ changes the solver's final output.
88	\end{itemize}
89	STA's ablation test directly measures propagation---the strongest condition in the RIP hierarchy. Components that fail propagation are structurally unnecessary regardless of reachability or infection status.
90	
91	\subsection{Combined Reward}
92	
93	The STA-augmented reward combines execution and structural signals:
94	\begin{equation}
95	r(f) = \alpha \cdot r_{\text{exec}}(f) + \beta \cdot r_{\text{exec}}(f) \cdot \text{ISR}(f)
96	\label{eq:reward}
97	\end{equation}
98	where $\alpha + \beta = 1$. The multiplicative coupling $r_{\text{exec}} \cdot \text{ISR}$ ensures that ISR contributes only for proved outputs, avoiding penalizing the model for structural properties of failed attempts.
99	
100	\paragraph{Sigmoid Curriculum.}
101	Fixed $\beta$ weighting suppresses early prove-rate learning when the model cannot yet produce provable outputs. We use a sigmoid curriculum that ramps $\beta$ from a small initial value to its target over the first $T_{\text{ramp}}$ steps:
102	\begin{equation}
103	\beta(t) = \beta_{\text{target}} \cdot \sigma\left(\frac{t - T_{\text{ramp}}/2}{T_{\text{ramp}}/10}\right)
104	\end{equation}
105	This allows execution-dominated early learning before structural reward activates.
106	
107	\subsection{5-Step Derivation Protocol}
108	\label{sec:protocol}
109	
110	To instantiate STA for a new solver--language pair:
111	\begin{enumerate}
112	\item \textbf{Pilot}: Run exec-only GRPO for 100 steps; collect proved outputs.
113	\item \textbf{Collect Shortcuts}: Manually inspect proved outputs for structural anomalies.
114	\item \textbf{Classify}: Categorize shortcuts by type (e.g., tautological, vacuous, redundant).
115	\item \textbf{Map RIP}: For each category, identify which RIP condition it violates (typically propagation).
116	\item \textbf{Design Checks}: Define the component decomposition and ablation procedure for $\mathcal{L}$.
117	\end{enumerate}
118	Steps 1--3 are empirical; steps 4--5 are systematic given the RIP framework. The protocol ensures that STA instantiations target the actual hacking modes of each logic type.
119	
120	\subsection{Computational Cost}
121	
122	STA requires $O(n)$ solver invocations per output, where $n$ is the number of components. For our experiments, $n$ ranges from 3--15, adding 7\% wall-clock overhead compared to execution-only training. We show in Section~\ref{sec:o1_ablation} that $O(1)$ approximations fail, justifying this cost.
123	
124	% ============================================================
125	\section{Experiments}
126	\label{sec:experiments}
127	
128	\subsection{Experimental Setup}
129	
130	\paragraph{Model.} Qwen3-4B as the primary model; Qwen3-8B for scaling analysis.
131	
132	\paragraph{Training.} GRPO with $K=8$ samples per prompt, 500 training steps. Three seeds for primary comparisons; single seed for ablations and secondary experiments.
133	
134	\paragraph{Data.} FOLIO dataset for FOL experiments; equivalent Prolog and SMT-LIB formalization tasks derived from the same natural language premises.
135	
136	\paragraph{Metrics.} \textbf{Prove rate}: fraction of outputs verified by the solver. \textbf{Mean ISR}: average intensional structure ratio across proved outputs. \textbf{ISR/PR ratio}: $\text{mean\_ISR} / \text{prove\_rate}$, a normalized measure of structural quality relative to accuracy. Values near 1.0 indicate structure tracks accuracy; declining values indicate structural degeneracy. \textbf{Hacking prevalence}: fraction of proved outputs containing manually identified structural shortcuts.
137	
138	% -----------------------------------------------------------
139	\subsection{Structural Degeneracy Under Exec-Only Training}
140	\label{sec:exec_only}
141	
142	Table~\ref{tab:exec_only_dynamics} shows the training dynamics of exec-only GRPO on FOL over 500 steps (3-seed mean $\pm$ std).
143	
144	\begin{table}[t]
145	\centering
146	\small
147	\begin{tabular}{lcccc}
148	\toprule
149	\textbf{Steps} & \textbf{Prove Rate} & \textbf{Mean ISR} & \textbf{ISR/PR} & \textbf{Reward} \\
150	\midrule
151	1--100 & 0.18 $\pm$ 0.02 & 0.16 $\pm$ 0.02 & 0.92 $\pm$ 0.05 & 0.18 $\pm$ 0.02 \\
152	101--200 & 0.22 $\pm$ 0.02 & 0.16 $\pm$ 0.03 & 0.73 $\pm$ 0.08 & 0.22 $\pm$ 0.02 \\
153	201--300 & 0.25 $\pm$ 0.03 & 0.13 $\pm$ 0.03 & 0.52 $\pm$ 0.07 & 0.25 $\pm$ 0.03 \\
154	301--400 & 0.27 $\pm$ 0.03 & 0.11 $\pm$ 0.02 & 0.41 $\pm$ 0.06 & 0.27 $\pm$ 0.03 \\
155	401--500 & 0.33 $\pm$ 0.04 & 0.09 $\pm$ 0.02 & 0.35 $\pm$ 0.05 & 0.33 $\pm$ 0.04 \\
156	\bottomrule
157	\end{tabular}
158	\caption{Exec-only GRPO training dynamics on FOL (3-seed mean $\pm$ std). Prove rate improves steadily (+83\% over 500 steps) while ISR/PR ratio degrades from 0.92 to 0.35, indicating progressive structural degeneracy.}
159	\label{tab:exec_only_dynamics}
160	\end{table}
161	
162	Prove rate improves from 0.18 to 0.33 over training---a substantial gain. However, the ISR/PR ratio drops monotonically from 0.92 to 0.35, indicating that the model increasingly relies on structural shortcuts to achieve higher prove rates. Standard evaluation would rate this as a successful training run; only STA-derived ISR reveals the hidden structural degradation.
163	
164	% -----------------------------------------------------------
165	\subsection{STA-Rewarded Training}
166	\label{sec:exec_sta}
167	
168	Table~\ref{tab:exec_sta_dynamics} shows training dynamics with exec+STA reward (curriculum $\alpha=0.5$, $\beta=0.5$).
169	
170	\begin{table}[t]
171	\centering
172	\small
173	\begin{tabular}{lcccc}
174	\toprule
175	\textbf{Steps} & \textbf{Prove Rate} & \textbf{Mean ISR} & \textbf{ISR/PR} & \textbf{Reward} \\
176	\midrule
177	1--100 & 0.16 $\pm$ 0.02 & 0.08 $\pm$ 0.02 & 0.48 $\pm$ 0.08 & 0.13 $\pm$ 0.02 \\
178	101--200 & 0.22 $\pm$ 0.03 & 0.13 $\pm$ 0.03 & 0.58 $\pm$ 0.07 & 0.17 $\pm$ 0.03 \\
179	201--300 & 0.26 $\pm$ 0.03 & 0.17 $\pm$ 0.03 & 0.64 $\pm$ 0.06 & 0.21 $\pm$ 0.03 \\
180	301--400 & 0.28 $\pm$ 0.03 & 0.19 $\pm$ 0.03 & 0.67 $\pm$ 0.06 & 0.23 $\pm$ 0.03 \\
181	401--500 & 0.34 $\pm$ 0.04 & 0.22 $\pm$ 0.03 & 0.65 $\pm$ 0.05 & 0.28 $\pm$ 0.03 \\
182	\bottomrule
183	\end{tabular}
184	\caption{Exec+STA GRPO training dynamics on FOL (3-seed mean $\pm$ std). Prove rate matches exec-only (0.34 vs.\ 0.33 final window) while ISR/PR ratio stabilizes at 0.65 instead of degrading to 0.35.}
185	\label{tab:exec_sta_dynamics}
186	\end{table}
187	
188	The comparison between Tables~\ref{tab:exec_only_dynamics} and \ref{tab:exec_sta_dynamics} delivers the core result. Exec+STA training achieves prove rate comparable to exec-only (overall mean 0.30 vs.\ 0.28, not statistically different) while maintaining ISR/PR ratio $\geq 0.48$ throughout training, stabilizing at 0.65. The sigmoid curriculum is load-bearing: the initial dip in ISR/PR (0.48 at steps 1--100) reflects the low-STA-weight phase where behavior approximates exec-only; ISR/PR then recovers as STA weight ramps up. Wall-clock overhead is 7\% (10.2s vs.\ 9.5s per step).
189	
190	% -----------------------------------------------------------
191	\subsection{Held-Out Generalization}
192	\label{sec:held_out}
193	
194	\begin{table}[t]
195	\centering
196	\small
197	\begin{tabular}{lcccc}
198	\toprule
199	\textbf{Condition} & \textbf{PR} & \textbf{ISR} & \textbf{ISR/PR} & \textbf{Hack \%} \\
200	\midrule
201	Base model & 0.12 & 0.064 & 0.53 & 25 \\
202	Exec-only & 0.24 & 0.08 & 0.33 & 45 \\
203	Exec+STA & 0.26 & 0.22 & 0.85 & 18 \\
204	Ground truth & 0.18 & 0.559 & --- & 0 \\
205	\bottomrule
206	\end{tabular}
207	\caption{Held-out generalization. Exec+STA achieves ISR/PR = 0.85 vs.\ 0.33 for exec-only, with hacking prevalence reduced from 45\% to 18\%. The base model's ISR/PR (0.53) exceeds trained exec-only (0.33)---exec-only training actively \emph{worsens} structural quality.}
208	\label{tab:held_out}
209	\end{table}
210	
211	Table~\ref{tab:held_out} presents the paper's strongest quantitative evidence. While prove rate differences are modest (0.24 vs.\ 0.26), the ISR gap is dramatic: 0.08 vs.\ 0.22 ($2.75\times$). The ISR/PR ratio inversion---exec-only 0.33 vs.\ exec+STA 0.85---is the headline result.
212	
213	A striking finding is that the base model (no training) has \emph{higher} ISR/PR ratio (0.53) than exec-only trained (0.33). Exec-only GRPO does not merely fail to improve structural quality---it actively degrades it below the untrained baseline. This underscores that structural degeneracy is not an inherent model limitation but an artifact of the reward signal.
214	
215	Hacking prevalence drops from 45\% (exec-only) to 18\% (exec+STA), below the base model's 25\%. STA is both diagnostic and corrective: it detects structural shortcuts \emph{and} prevents them through reward shaping.
216	
217	% -----------------------------------------------------------
218	\subsection{O(1) vs.\ O(N) Ablation}
219	\label{sec:o1_ablation}
220	
221	\begin{table}[t]
222	\centering
223	\small
224	\begin{tabular}{lccc}
225	\toprule
226	\textbf{Metric} & \textbf{O(N) STA} & \textbf{O(1)} & \textbf{Exec-only} \\
227	\midrule
228	Prove rate & 0.30 & 0.27 & 0.28 \\
229	Mean ISR & 0.19 & 0.04 & 0.11 \\
230	ISR/PR (last 100) & 0.65 & 0.15 & 0.35 \\
231	Discriminability & 0.72 & 0.08 & --- \\
232	Overhead & +7\% & +1\% & baseline \\
233	\bottomrule
234	\end{tabular}
235	\caption{O(1) tautology-only check vs.\ full O(N) STA. The O(1) approximation has near-zero discriminability (0.08) and produces training dynamics indistinguishable from exec-only.}
236	\label{tab:o1_ablation}
237	\end{table}
238	
239	Table~\ref{tab:o1_ablation} documents a principled negative result. The O(1) approximation (\texttt{fast\_isr\_fol}: tautology-only check) captures only one of many hacking modes. The model quickly learns to avoid tautologies while discovering alternative shortcuts (vacuous quantifiers, over-constrained premises) that O(1) cannot detect.
240	
241	ISR discriminability---the fraction of proved outputs receiving nonzero ISR signal---drops from 0.72 (full STA) to 0.08 (O(1)), meaning $<$8\% of outputs receive any structural feedback. The combined reward degenerates to effectively exec-only (correlation with full O(N) ISR: 0.12). The ISR/PR ratio (0.15) is actually \emph{worse} than exec-only (0.35), suggesting that the tautology-only penalty forces the model into a narrower set of non-tautological shortcuts, reducing structural diversity.
242	
243	This result motivates the O(N) cost: domain-specific hacking modes require correspondingly granular ablation components.
244	
245	% -----------------------------------------------------------
246	\subsection{Reward Weight Ablation}
247	\label{sec:weight_ablation}
248	
249	\begin{table}[t]
250	\centering
251	\small
252	\begin{tabular}{lcccc}
253	\toprule
254	$\alpha/\beta$ & \textbf{Schedule} & \textbf{PR} & \textbf{ISR/PR} & \textbf{PR$\times$Ratio} \\
255	\midrule
256	0.3/0.7 & fixed & 0.20 & 0.72 & 0.144 \\
257	0.5/0.5 & fixed & 0.25 & 0.68 & 0.170 \\
258	0.7/0.3 & fixed & 0.30 & 0.52 & 0.156 \\
259	\midrule
260	0.3/0.7 & curriculum & 0.26 & 0.70 & 0.182 \\
261	0.5/0.5 & curriculum & 0.30 & 0.65 & \textbf{0.195} \\
262	0.7/0.3 & curriculum & 0.32 & 0.55 & 0.176 \\
263	\midrule
264	1.0/0.0 & --- & 0.28 & 0.35 & 0.098 \\
265	\bottomrule
266	\end{tabular}
267	\caption{Weight ablation (500 steps, 1 seed). Sigmoid curriculum consistently Pareto-dominates fixed weighting. Curriculum $\alpha{=}0.5$/$\beta{=}0.5$ achieves the best PR$\times$ISR/PR product.}
268	\label{tab:weight_ablation}
269	\end{table}
270	
271	Table~\ref{tab:weight_ablation} reveals three insights. First, STA weight has a predictable dose--response relationship with structural quality, confirming it is a genuine training signal. Second, sigmoid curriculum Pareto-dominates fixed weighting at matched terminal weights: curriculum 0.5/0.5 matches fixed 0.7/0.3's prove rate (0.30) while achieving higher ISR/PR ratio (0.65 vs.\ 0.52). Third, the optimal configuration is curriculum $\alpha{=}0.5$/$\beta{=}0.5$, achieving the highest PR$\times$ISR/PR product (0.195).
272	
273	% -----------------------------------------------------------
274	\subsection{Multi-Logic Validation}
275	\label{sec:multi_logic}
276	
277	\paragraph{Prolog.}
278	Table~\ref{tab:prolog} shows STA instantiated for Prolog via clause ablation (remove each clause, check if query still succeeds). Prolog-specific hacking modes---redundant clauses, catch-all rules, trivial unification---are structurally distinct from FOL's, confirming that hacking is logic-type-specific and STA detects it across logic types.
279	
280	\begin{table}[t]
281	\centering
282	\small
283	\begin{tabular}{lcccc}
284	\toprule
285	\textbf{Condition} & \textbf{PR} & \textbf{ISR} & \textbf{ISR/PR} & \textbf{Discrim.} \\
286	\midrule
287	Exec-only & 0.22 & 0.08 & 0.32 & --- \\
288	Exec+STA & 0.24 & 0.14 & 0.58 & 0.45 \\
289	\bottomrule
290	\end{tabular}
291	\caption{Prolog single-logic GRPO (500 steps, 1 seed). The exec+STA pattern replicates: ISR/PR ratio stabilizes at 0.58 vs.\ 0.32.}
292	\label{tab:prolog}
293	\end{table}
294	
295	\paragraph{SMT-LIB.}
296	Table~\ref{tab:three_logic} completes the three-logic validation. SMT-LIB STA uses constraint ablation (remove each \texttt{assert}/\texttt{declare}, check if \texttt{(check-sat)} result changes). SMT-LIB-specific hacking modes include trivial assertions, over-constrained declarations, and unused variables.
297	
298	\begin{table}[t]
299	\centering
300	\small
301	\begin{tabular}{lccccc}
302	\toprule
303	\textbf{Logic} & \textbf{EO PR} & \textbf{ES PR} & \textbf{EO Ratio} & \textbf{ES Ratio} & \textbf{Discrim.} \\
304	\midrule
305	FOL & 0.28 & 0.30 & 0.35 & 0.65 & 0.72 \\
306	Prolog & 0.22 & 0.24 & 0.32 & 0.58 & 0.45 \\
307	SMT-LIB & 0.18 & 0.19 & 0.38 & 0.52 & 0.35 \\
308	\bottomrule
309	\end{tabular}
310	\caption{Three-logic STA summary. EO = exec-only, ES = exec+STA. The qualitative pattern (STA stabilizes structural quality) holds across all three logic types despite different absolute metrics and discriminability levels.}
311	\label{tab:three_logic}
312	\end{table}
313	
314	The diminishing effect magnitude (FOL $>$ Prolog $>$ SMT-LIB) correlates with ISR discriminability, which itself correlates with component independence---SMT-LIB assertions are often interdependent, producing a coarser ISR signal.
315	
316	\paragraph{Multi-Logic Training.}
317	Table~\ref{tab:multi_logic} compares single-logic and multi-logic training.
318	
319	\begin{table}[t]
320	\centering
321	\small
322	\begin{tabular}{llccc}
323	\toprule
324	\textbf{Logic} & \textbf{Training} & \textbf{PR} & \textbf{ISR/PR} & $\Delta$ \textbf{vs single} \\
325	\midrule
326	FOL & single exec+STA & 0.30 & 0.65 & --- \\
327	FOL & multi exec+STA & 0.29 & 0.62 & $-$0.01 / $-$0.03 \\
328	Prolog & single exec+STA & 0.24 & 0.58 & --- \\
329	Prolog & multi exec+STA & 0.25 & 0.55 & +0.01 / $-$0.03 \\
330	\bottomrule
331	\end{tabular}
332	\caption{Multi-logic vs.\ single-logic training. Prolog benefits from multi-logic training (+0.01 PR); FOL shows marginal decrease. ISR/PR ratio is slightly lower under multi-logic due to mixed reward signal noise.}
333	\label{tab:multi_logic}
334	\end{table}
335	
336	Cross-logic transfer is positive but modest: Prolog benefits more from FOL co-training (+0.01 PR, +0.03 over single-logic baseline) because FOL training data is larger and formal reasoning skills partially transfer. The slight ISR/PR decrease under multi-logic training reflects gradient variance from mixed logic-specific STA signals.
337	
338	\paragraph{Zero-Shot Cross-Logic Transfer.}
339	Table~\ref{tab:cross_transfer} evaluates models on the logic type they were \emph{not} trained on.
340	
341	\begin{table}[t]
342	\centering
343	\small
344	\begin{tabular}{llccc}
345	\toprule
346	\textbf{Source} & \textbf{Target} & \textbf{PR} & $\Delta$ \textbf{vs base} & \textbf{ISR} \\
347	\midrule
348	Base & FOL & 0.12 & --- & 0.064 \\
349	Base & Prolog & 0.12 & --- & 0.05 \\
350	FOL exec+STA & Prolog & 0.16 & +0.04 & 0.09 \\
351	Prolog exec+STA & FOL & 0.17 & +0.05 & 0.10 \\
352	FOL exec-only & Prolog & 0.15 & +0.03 & 0.06 \\
353	Prolog exec-only & FOL & 0.16 & +0.04 & 0.07 \\
354	\bottomrule
355	\end{tabular}
356	\caption{Zero-shot cross-logic transfer. STA-trained models show marginally higher transfer ($+0.01$ additional $\Delta$) than exec-only trained models, suggesting structurally sound formalizations encode more transferable logical patterns.}
357	\label{tab:cross_transfer}
358	\end{table}
359	
360	Both directions show positive transfer (mean $\Delta = 0.045$ over base). STA-trained models exhibit marginally higher transfer than exec-only models (+0.01 additional $\Delta$), consistent with the hypothesis that structurally sound formalizations encode more generalizable logical structure.
361	
362	% -----------------------------------------------------------
363	\subsection{SFT Baseline}
364	\label{sec:sft}
365	
366	\begin{table}[t]
367	\centering
368	\small
369	\begin{tabular}{lcccc}
370	\toprule
371	\textbf{Method} & \textbf{PR} & \textbf{ISR} & \textbf{ISR/PR} & \textbf{Held-out PR} \\
372	\midrule
373	Base model & 0.12 & 0.064 & 0.53 & 0.12 \\
374	SFT & 0.20 & 0.13 & 0.65 & 0.18 \\
375	GRPO exec-only & 0.28 & 0.11 & 0.39 & 0.24 \\
376	GRPO exec+STA & 0.30 & 0.19 & 0.63 & 0.26 \\
377	\bottomrule
378	\end{tabular}
379	\caption{SFT vs.\ GRPO comparison. SFT maintains structural quality (ISR/PR = 0.65) but achieves lower accuracy than GRPO. Exec+STA combines GRPO's accuracy advantage with SFT-level structural quality.}
380	\label{tab:sft}
381	\end{table}
382	
383	Table~\ref{tab:sft} positions STA within the accuracy--structure tradeoff. SFT on ground-truth formalizations achieves good structure (ISR/PR = 0.65) by imitating human-written outputs, but lacks GRPO's exploration and achieves lower prove rate (0.20 vs.\ 0.30). Exec-only GRPO achieves high accuracy but degraded structure. Exec+STA GRPO achieves both: GRPO-level accuracy with SFT-level structural quality. This demonstrates that GRPO is necessary for accuracy and STA is necessary for maintaining the structural quality that SFT inherits from human demonstrations.
384	
385	% -----------------------------------------------------------
386	\subsection{Scaling Analysis}
387	\label{sec:scaling}
388	
389	\begin{table}[t]
390	\centering
391	\small
392	\begin{tabular}{llccc}
393	\toprule
394	\textbf{Model} & \textbf{Condition} & \textbf{PR} & \textbf{ISR/PR} & \textbf{Held-out PR} \\
395	\midrule
396	Qwen3-4B & exec-only & 0.28 & 0.35 & 0.24 \\
397	Qwen3-4B & exec+STA & 0.30 & 0.65 & 0.26 \\
398	Qwen3-8B & exec-only & 0.38 & 0.40 & 0.32 \\
399	Qwen3-8B & exec+STA & 0.40 & 0.68 & 0.34 \\
400	\bottomrule
401	\end{tabular}
402	\caption{Scale comparison (4B vs.\ 8B). The STA benefit is approximately scale-invariant: ISR/PR improvement of ${\sim}0.28$ at both scales. Structural degeneracy persists at 8B, confirming it is a property of the optimization, not a small-model artifact.}
403	\label{tab:scaling}
404	\end{table}
405	
406	Table~\ref{tab:scaling} demonstrates that STA's benefits are scale-invariant. Scaling from 4B to 8B increases prove rate by ${\sim}0.10$ for both conditions, but the ISR/PR ratio gap persists: exec-only degrades to 0.40 (slightly better than 4B's 0.35---larger models hack less aggressively due to greater capacity for genuine solutions), while exec+STA maintains 0.68. The relative ISR/PR improvement (${\sim}0.28$) is consistent across scales, confirming that structural degeneracy under exec-only reward is a fundamental property of GRPO optimization, not a small-model artifact.
407	
408	% -----------------------------------------------------------
409	\subsection{Hacking Characterization}
410	\label{sec:hacking}
411	
412	\begin{table}[t]
413	\centering
414	\small
415	\begin{tabular}{lcccc}
416	\toprule
417	\textbf{Shortcut Type} & \textbf{Base} & \textbf{EO} & \textbf{E+S} & \textbf{SFT} \\
418	\midrule
419	Tautological premise & 8 & 18 & 3 & 2 \\
420	Vacuous quantifier & 7 & 12 & 4 & 3 \\
421	Redundant clause & 5 & 8 & 6 & 4 \\
422	Over-constrained & 3 & 5 & 3 & 2 \\
423	Other/subtle & 2 & 2 & 2 & 1 \\
424	\midrule
425	\textbf{Total hack rate (\%)} & 25 & 45 & 18 & 12 \\
426	\bottomrule
427	\end{tabular}
428	\caption{Hacking taxonomy distribution (\%, 200 outputs per condition, $\kappa = 0.78$). EO = exec-only, E+S = exec+STA. Exec-only training amplifies hacking from 25\% to 45\%; STA reduces it to 18\%, below the untrained baseline.}
429	\label{tab:hacking}
430	\end{table}
431	
432	Table~\ref{tab:hacking} provides qualitative evidence complementing the quantitative ISR metrics. Manual annotation of 200 outputs per condition (inter-annotator $\kappa = 0.78$) reveals the composition of structural degeneracy.
433	
434	Exec-only training amplifies every hacking category relative to the base model: tautological premises increase from 8\% to 18\%, vacuous quantifiers from 7\% to 12\%. This is expected---GRPO's policy gradient selects for outputs that prove easily, and structural shortcuts prove more easily than genuine formalizations.
435	
436	STA-rewarded training suppresses the most egregious categories: tautological premises drop from 18\% to 3\% (STA assigns ISR = 0 to tautology components), vacuous quantifiers from 12\% to 4\%. Residual hacking (18\% total) consists primarily of subtler shortcuts---redundant clauses with small but nonzero ISR contributions (6\%)---that partial ISR does not fully penalize. This identifies a clear direction for future work: finer-grained ablation or curriculum emphasis on high-residual hacking modes.
437	
438	% ============================================================
439	\section{Discussion}
440	\label{sec:discussion}
441	
442	\paragraph{STA in the ORM-PRM Taxonomy.}
443	STA fills a previously empty cell: dense + automatic rewards derived from solver semantics rather than human annotation. ORMs provide sparse (outcome-level) automatic feedback; PRMs provide dense (step-level) feedback but require manual labels. STA achieves PRM-level granularity (per-component structural scores) with ORM-level automation (derived from solver execution). This positions STA as complementary to, not competitive with, existing reward paradigms.
444	
445	\paragraph{When Does STA Help Most?}
446	Our results suggest STA's benefit scales with ISR discriminability---the degree to which components are independently ablatable. FOL (discriminability 0.72) shows the strongest effect; SMT-LIB (0.35) the weakest. This provides a practical guideline: STA is most valuable for languages with modular, independently testable components.
447	
448	\paragraph{Limitations.}
449	Our experiments use a single base model family (Qwen3) and a limited set of formal languages. The 5-step derivation protocol requires manual inspection (steps 2--3), introducing human effort. ISR treats all components equally---a premise that constrains the entire proof is scored the same as one that constrains a single variable. Future work should explore weighted ISR based on component influence depth.
450	
451	% ============================================================
452	\section{Conclusion}
453	\label{sec:conclusion}
454	
455	We introduced Solver Trace Ablation (STA), a methodology for deriving dense structural rewards from solver execution semantics via the RIP framework from mutation testing. Our 5-step derivation protocol generalizes across three logic types (FOL, Prolog, SMT-LIB), and STA-rewarded GRPO consistently maintains structural integrity without sacrificing prove rate. The O(1) negative result validates the necessity of comprehensive component ablation. Scaling analysis confirms that structural degeneracy is a fundamental property of execution-only GRPO, not a small-model artifact, and STA addresses it at all tested scales. STA provides a principled, automatic approach to the structural reward design problem that has limited prior work to ad-hoc, domain-specific heuristics.
456	
457	\begin{thebibliography}{9}
458	
459	\bibitem[Mellgren et~al.(2025)]{mellgren2025prolog}
460	E.~Mellgren, A.~Bj{\"o}rklund, and J.~Nivre.
461	\newblock Structure-aware reinforcement learning for Prolog synthesis.
462	\newblock In \emph{Proc.\ ACL}, 2025.
463	
464	\bibitem[EVOM(2026)]{evom2026}
465	Cross-solver GRPO transfer with execution-verified outcome models.
466	\newblock In \emph{Proc.\ ICLR}, 2026.
467	
468	\bibitem[Polu and Sutskever(2020)]{polu2020gpt}
469	S.~Polu and I.~Sutskever.
470	\newblock Generative language modeling for automated theorem proving.
471	\newblock \emph{arXiv:2009.03393}, 2020.
472	
473	\bibitem[Le et~al.(2022)]{le2022coderl}
474	H.~Le, Y.~Wang, A.~D.~Gotmare, S.~Savarese, and S.~Hoi.
475	\newblock CodeRL: Mastering code generation through pretrained models and deep reinforcement learning.
476	\newblock In \emph{Proc.\ NeurIPS}, 2022.
477	
478	\bibitem[Lightman et~al.(2023)]{lightman2023verify}
479	H.~Lightman, V.~Kosaraju, Y.~Burda, H.~Edwards, B.~Baker, T.~Lee, J.~Leike, J.~Schulman, I.~Sutskever, and K.~Cobbe.
480	\newblock Let's verify step by step.
481	\newblock In \emph{Proc.\ ICLR}, 2024.
482	
483	\bibitem[Jia and Harman(2011)]{jia2011analysis}
484	Y.~Jia and M.~Harman.
485	\newblock An analysis and survey of the development of mutation testing.
486	\newblock \emph{IEEE TSE}, 37(5):649--678, 2011.
487	
488	\end{thebibliography}
489	
490	\end{document}
491	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07986ea4-b51d-4d8d-baf9-0c9918f10375",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "2d627aa5-2370-4633-830f-5057f6dfb8a1",
  "sourceToolAssistantUUID": "07986ea4-b51d-4d8d-baf9-0c9918f10375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-13T22:43:41.307Z_

Now let me also check the "median" and "worst" dream variants and the review report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d627aa5-2370-4633-830f-5057f6dfb8a1",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NpDJAjyWBYoMpUjFA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60ca88c2-10cd-4a26-8914-b5d17f3a09cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXyh5GYwGsJGzo35KVAPGZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12139,
      "cache_read_input_tokens": 28006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12139,
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

_source line 41 · 2026-05-13T22:43:43.857Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HHh94Vnqwxx8mJDo5BUuBt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60ca88c2-10cd-4a26-8914-b5d17f3a09cb",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NpDJAjyWBYoMpUjFA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95b252dc-57c3-4c55-b24c-be0666f515ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXyh5GYwGsJGzo35KVAPGZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12139,
      "cache_read_input_tokens": 28006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12139,
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

_source line 42 · 2026-05-13T22:43:43.865Z_

<details><summary>↩ Tool result · `toolu_01HHh94Vnqwxx8mJDo5BUuBt`</summary>

```text
1	---
2	dream_id: dream_20260513T215750
3	tier: best
4	overall_score: 4/6 Borderline Reject
5	timestamp: 2026-05-13T22:32:49.918165+00:00
6	---
7	
8	# Dream Review Report: Solver Trace Ablation
9	
10	**Paper**: "Solver Trace Ablation: Dense Structural Rewards for Formal Reasoning via Mutation Testing"
11	**Review Mode**: Full (2 Reviewers + Roundtable)
12	**Date**: 2026-05-13
13	
14	---
15	
16	## Reviewer Assignments
17	- **R1** (Methods + Experiments): Methodology soundness, experimental rigor, reproducibility
18	- **R2** (Novelty + Related Work): Novelty assessment, related work completeness, positioning
19	
20	---
21	
22	## Step 1: Independent Reviews
23	
24	### R1: Methods + Experiments
25	
26	**Score: 4/6 (Borderline Reject)**
27	
28	#### Strengths
29	
30	**S1. Principled grounding in mutation testing.** The RIP framework provides a well-established theoretical foundation. The mapping—component ablation = mutant generation, solver outcome change = mutant killing—is natural. The insight that mutation adequacy criteria translate to reward signal quality is genuinely novel in the RL-for-formal-reasoning context.
31	
32	**S2. Actionable 5-step derivation protocol.** The procedure (pilot → collect shortcuts → classify → map RIP → design checks) is concrete enough for replication and demonstrated for three distinct solver-language pairs.
33	
34	**S3. Clean combined reward formulation.** r(f) = α·r_exec + β·r_exec·ISR multiplicatively couples execution and structure, ensuring ISR affects only proved outputs. The sigmoid curriculum addresses the initialization sensitivity observed in the pilot.
35	
36	**S4. O(1) vs O(N) negative result.** Discriminability 0.08 vs 0.72 provides principled justification for computational overhead and deepens understanding of why component-level ablation is necessary.
37	
38	**S5. Comprehensive experimental matrix.** All 12 planned experiments are covered: single-logic (3 types), multi-logic, cross-logic transfer, weight ablation, scaling, SFT baseline, hacking characterization.
39	
40	**S6. Manual hacking taxonomy with κ=0.78.** Grounds the quantitative ISR metric in qualitative assessment with concrete examples.
41	
42	#### Weaknesses
43	
44	**W1. ISR conflates necessity with quality.** A component being "necessary for the solver outcome" does not guarantee semantic correctness. A formula with N non-redundant but logically arbitrary premises that convolve to entail the conclusion would score high ISR but be a poor formalization. The gap between structural necessity and semantic adequacy is not discussed.
45	
46	**W2. RIP mapping is informal.** The three-stage decomposition (Reachability, Infection, Propagation) collapses into the single ablation test. Only Propagation is operationally measured. This makes RIP more of an analogy than a formal derivation—"component necessity testing" would be equally accurate.
47	
48	**W3. ISR sensitivity to decomposition granularity.** Discriminability varies (FOL 0.72, Prolog 0.45, SMT-LIB 0.35) but the 5-step protocol provides no guidance on choosing the ablation unit. Splitting premises into sub-clauses or merging premises changes ISR.
49	
50	**W4. Curriculum sigmoid is load-bearing but under-analyzed.** Table 5 shows curriculum Pareto-dominates fixed weighting, but the sigmoid shape (center, slope) is not ablated. Is sigmoid better than linear ramp? What is sensitivity to the ramp midpoint (reported as step 200 of 500)?
51	
52	**W5. Single-seed ablations insufficient.** Plans 004-011 all use 1 seed. Table 5's Pareto dominance claim, Table 6/7's cross-logic validation, and Table 11's scaling analysis could be driven by initialization variance. At minimum, top-2 configurations should have 3 seeds.
53	
54	**W6. Prove rate differences not statistically significant.** Table 1: 0.33±0.04 vs Table 2: 0.34±0.04 (overlapping CIs). Held-out: 0.24 vs 0.26. The paper should state "no significant difference" rather than "matches or slightly exceeds."
55	
56	**W7. ISR optimization is partially circular.** Optimizing ISR as a reward naturally increases ISR. The hacking taxonomy (200 samples, κ=0.78) partially breaks this circularity but is not dispositive. A downstream logical inference task evaluation would be stronger validation.
57	
58	**W8. Simpson's paradox risk in base model ISR/PR.** Base model ISR/PR (0.53) > trained exec-only (0.33), cited as evidence that "training actively worsens structural quality." But the base model computes ISR/PR over only 12% of outputs (those that prove), a self-selected population of "easy" problems that are structurally well-posed. The populations are different.
59	
60	**W9. Multi-logic effects too small.** Table 8: +0.01 PR for Prolog from multi-logic training; Table 9: mean transfer Δ=0.045, STA adds only +0.01. At 1 seed, these are indistinguishable from noise.
61	
62	**W10. Training horizon limited.** 500 steps (4000 rollouts over FOLIO) is short. Does exec-only continue to degrade at 2000+ steps, or stabilize? Does STA's benefit persist or diminish? The limited horizon leaves the durability of STA's structural protection unclear.
63	
64	**W11. SFT baseline comparison conflates training paradigm with data efficiency.** SFT's lower prove rate (0.20 vs 0.30) could reflect imitation learning's limited exploration with 500 examples, not inherent inferiority.
65	
66	#### Questions for Authors
67	1. Can you provide examples where ISR is high but the formalization is semantically wrong? What is the false-positive rate?
68	2. What happens with linear ramp instead of sigmoid? Sensitivity to ramp midpoint?
69	3. Do you have data beyond 500 steps? Does ISR/PR gap persist?
70	4. How do you handle ISR for the ~70% of outputs that fail to prove?
71	5. Have you verified the ISR/PR trend is not an artifact of changing population composition (Simpson's paradox)?
72	6. Who are the hacking taxonomy annotators? If authors, κ=0.78 may be inflated by shared mental models.
73	
74	---
75	
76	### R2: Novelty + Related Work
77	
78	**Score: 3/6 (Borderline Reject)**
79	
80	#### Novelty Assessment
81	
82	**Moderate novelty.** The core idea—leave-one-out ablation of solver input components as a reward signal—is sound but conceptually straightforward. ISR is equivalent to well-known feature importance/sensitivity tests (Shapley-style leave-one-out) applied to a new domain. The genuine contribution is recognizing that this specific application (RL rewards for formal reasoning) is valuable, not the technique itself.
83	
84	The RIP framework invocation is largely window-dressing. Only Propagation is operationally measured. The paper does not use Reachability or Infection as independent diagnostic or reward signals. Renaming "component necessity testing" as "RIP-grounded STA" inflates the theoretical contribution.
85	
86	The 5-step derivation protocol is a practical contribution but methodologically amounts to "run a pilot, find failure modes, design targeted checks"—standard engineering methodology, not a theoretical framework.
87	
88	#### Related Work: Critically Deficient
89	
90	**6 references is unacceptable for a venue paper.** Missing critical citations include:
91	
92	- **Reward shaping theory**: Ng et al. (1999) "Policy invariance under reward transformations" — the foundational result on potential-based reward shaping. STA's combined reward should be discussed in this context.
93	- **Reward hacking/overoptimization**: Gao et al. (2023) "Scaling Laws for Reward Model Overoptimization"; Skalse et al. (2022) "Defining and Characterizing Reward Hacking." The paper's core problem statement (reward hacking under exec-only rewards) must cite this literature.
94	- **GRPO itself**: Shao et al. (2024) "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models" where GRPO was introduced. The paper uses GRPO as its RL algorithm but does not cite its origin.
95	- **Modern formal verification + LLM**: LeanDojo (Yang et al. 2024), Baldur (First et al. 2023), AlphaProof (DeepMind 2024). These are the current state-of-the-art in formal reasoning with LLMs.
96	- **FOLIO dataset**: Han et al. (2022) "FOLIO: Natural Language Reasoning with First-Order Logic." The paper uses FOLIO as its primary dataset without citing it.
97	- **Mutation testing for ML**: DeepMutation (Ma et al. 2018), MuNN. Recent work applying mutation testing to ML systems should be discussed.
98	- **Feature attribution connections**: SHAP (Lundberg & Lee 2017), Leave-One-Out (LOO) feature importance. ISR is structurally equivalent to binary LOO feature importance.
99	- **Dense rewards in RL**: Potential-based reward shaping, intrinsic motivation, curiosity-driven exploration. STA's "dense+automatic" claim needs context within this broader literature.
100	
101	The "EVOM (2026)" reference has no author list — it appears to be a self-citation or placeholder.
102	
103	#### Conceptual Clarity
104	
105	The ORM-PRM taxonomy positioning ("dense + automatic cell") is reasonable but under-argued. The paper should explicitly compare:
106	- Why not train a PRM on solver execution traces? Math-Shepherd and similar approaches learn dense process rewards automatically from execution feedback.
107	- Why is component ablation better than attention-based structural analysis?
108	- How does STA relate to reward shaping theory (Ng 1999)?
109	
110	The "dense reward" claim is weakened by ISR being undefined for 67-88% of training examples (those that fail to prove). The reward r(f) = α·r_exec + β·r_exec·ISR reduces to α·r_exec = 0 for unproved outputs (since r_exec = 0). So for the majority of training examples, STA provides no signal at all. This should be acknowledged.
111	
112	#### Writing Quality
113	
114	The paper is well-organized and clearly written. Claims are generally appropriate, with exceptions noted above (prove rate "matching or slightly exceeding" should be "not significantly different"). The abstract accurately summarizes the content. Tables are clear and consistently formatted.
115	
116	However, the 10-page length feels thin for the experimental breadth — many experiments are described in 2-3 sentences where a full paragraph of analysis would be appropriate. The multi-logic and cross-logic sections are particularly rushed.
117	
118	#### Limitations
119	
120	The Limitations paragraph is honest about model family (Qwen3 only), limited languages, and manual steps. It correctly identifies the "uniform component weighting" limitation. Missing from limitations:
121	- ISR is undefined for unproved outputs (majority of training)
122	- Sensitivity to decomposition granularity
123	- Potential Simpson's paradox in ISR/PR ratio comparisons
124	- Short training horizon (500 steps)
125	
126	#### Questions for Authors
127	1. Has the actual 500-step, 3-seed training been completed, or are results projected from shorter pilots?
128	2. Why is GRPO not cited? Which GRPO implementation was used?
129	3. Can you provide the FOLIO dataset citation?
130	4. How does ISR relate to Shapley values or SHAP-style feature importance?
131	5. Why not compare against a PRM trained on solver traces?
132	6. What is the "EVOM (2026)" reference? It has no authors listed.
133	
134	---
135	
136	## Step 2: Cross-Sharing
137	
138	### R1 responding to R2's concerns:
139	- **Agree** that 6 references is critically deficient. The missing GRPO, FOLIO, and reward hacking citations are serious oversights.
140	- **Agree** that the RIP framing overstates the theoretical contribution. R2's characterization as "window-dressing" is harsh but not unfair — only Propagation is measured.
141	- **Partially agree** on novelty: the domain application (RL rewards for formal reasoning) has genuine value even if LOO ablation is not novel. The 5-step protocol and three-logic demonstration are meaningful contributions.
142	- **Note** R2's concern about whether experiments were actually run vs projected. This cannot be adjudicated from the paper alone but is a valid concern given the limited training horizon and single-seed secondary experiments.
143	
144	### R2 responding to R1's concerns:
145	- **Agree** that ISR conflating necessity with quality (W1) is a fundamental limitation. This aligns with the novelty concern — ISR is a simple binary LOO test, and its limitations are well-known in the feature importance literature.
146	- **Agree** that Simpson's paradox (W8) is a real risk and should be formally tested.
147	- **Agree** that the curriculum analysis (W4) is under-developed for a "load-bearing" design choice.
148	- **Elevate** W7 (circularity): this is arguably the paper's most fundamental concern. The paper optimizes ISR as a reward and then reports ISR improvement as the primary result. The hacking taxonomy breaks this somewhat, but 200 samples with potentially author-authored annotation is not enough.
149	
150	---
151	
152	## Step 3: Convergence
153	
154	### Points of Agreement (both reviewers):
155	1. **Core idea has merit.** Component ablation as a structural reward for formal reasoning is well-motivated and potentially impactful.
156	2. **RIP framing overstated.** Only Propagation is measured; Reachability and Infection add no operational content. "Component necessity testing" is more accurate.
157	3. **Related work critically deficient.** 6 references is far below venue standards. Missing citations to GRPO, FOLIO, reward hacking, reward shaping, and modern formal verification work.
158	4. **Statistical rigor insufficient for secondary claims.** Single-seed ablations (Tables 4-11) cannot support the conclusions drawn. Multi-logic transfer effects (+0.01) are indistinguishable from noise.
159	5. **Prove rate "Pareto-improving" claim overclaimed.** Differences are not statistically significant; should be "no significant prove rate degradation."
160	6. **ISR circularity partially addressed but not resolved.** Hacking taxonomy (200 samples, κ=0.78) helps but is insufficient. Downstream task evaluation needed.
161	7. **ISR undefined for majority of training examples.** The "dense reward" positioning is weakened by ISR contributing 0 signal for 67-88% of outputs.
162	8. **O(1) negative result is a genuine strength.** Both reviewers value this ablation.
163	9. **Comprehensive experimental breadth.** The 12-experiment matrix is thorough for a methods paper, even if individual experiments lack statistical depth.
164	
165	### Points of Disagreement:
166	- **Novelty level**: R1 rates the mutation-testing-to-reward-design insight as "genuinely novel"; R2 sees it as "straightforward LOO applied to a new domain." Converged position: the application is valuable but the technique itself is not novel.
167	- **Severity of related work gap**: R1 flags it as a concern; R2 considers it grounds for rejection. Converged: it is a major weakness that must be addressed but is fixable.
168	- **Overall score**: R1 gives 4 (Borderline Reject), R2 gives 3 (Reject). After discussion, converged at **4 (Borderline Reject)** — the core contribution has value and the paper is fixable, but substantial revision is needed.
169	
170	---
171	
172	## Step 4: Consolidated Assessment
173	
174	### Overall Score: 4/6 (Borderline Reject)
175	
176	### Summary Assessment
177	
178	The paper addresses a real and important problem — structural degeneracy (reward hacking) in execution-only RL for formal reasoning — with a well-motivated solution: component ablation as a dense structural reward. The idea is sound, the experimental plan is comprehensive, and the O(1) negative result is a genuinely informative contribution.
179	
180	However, the paper falls short of top venue standards in several dimensions:
181	
182	### Major Issues (must fix)
183	
184	**M1. Related work critically deficient.** 6 references is unacceptable. The paper must cite GRPO's origin (Shao et al. 2024), the FOLIO dataset (Han et al. 2022), reward hacking literature (Gao et al. 2023; Skalse et al. 2022), reward shaping theory (Ng et al. 1999), and modern formal verification+LLM work (LeanDojo, Baldur, AlphaProof). The "EVOM (2026)" reference lacks authors. A top venue paper in this space should have 25-40 references.
185	
186	**M2. ISR circularity.** The paper optimizes ISR as a reward and reports ISR improvement as the primary result. The hacking taxonomy (Table 12) partially breaks this circularity but relies on 200 samples with potentially non-independent annotators (κ=0.78). The paper needs either: (a) a downstream evaluation showing high-ISR formalizations are genuinely better on an independent criterion, or (b) a much larger and externally-annotated hacking study.
187	
188	**M3. Statistical rigor for secondary claims.** 8 of 12 experiments use a single seed. The weight ablation (Table 5), multi-logic (Tables 8-9), scaling (Table 11), and cross-logic transfer (Table 9) results cannot support the conclusions drawn. Effect sizes of +0.01-0.03 at 1 seed are not meaningful. Minimum: 3 seeds for the top-2 weight configurations and at least 1 secondary logic type.
189	
190	**M4. "Pareto-improving" overclaimed.** Prove rate differences (exec-only 0.28±0.03 vs exec+STA 0.30±0.03) are not statistically significant. The paper should claim "STA preserves prove rate while substantially improving structural quality" rather than "Pareto-improving."
191	
192	### Minor Issues (should fix)
193	
194	**m1. RIP framing overstated.** Only Propagation is operationally measured. Either formalize the Reachability and Infection conditions as independent diagnostic signals, or reframe as "component necessity testing" without the three-stage RIP hierarchy.
195	
196	**m2. "Dense reward" claim weakened.** ISR is undefined for unproved outputs (67-88% of training examples). The reward reduces to r_exec = 0 for these. The paper should acknowledge this and discuss implications for training signal density.
197	
198	**m3. ISR sensitivity to decomposition granularity.** The 5-step protocol should include guidance on choosing the ablation unit. The varying discriminability across logic types (0.72, 0.45, 0.35) is acknowledged but not addressed.
199	
200	**m4. Curriculum under-analyzed.** The sigmoid is load-bearing (Table 5) but its shape parameters are not ablated. Linear ramp comparison and midpoint sensitivity analysis needed.
201	
202	**m5. Simpson's paradox risk in base model comparison.** The claim that "training actively worsens structural quality" (base ISR/PR 0.53 > exec-only 0.33) may be an artifact of different populations. The base model computes ISR/PR over only its 12% prove-rate outputs.
203	
204	**m6. Short training horizon.** 500 steps leaves open whether STA's benefits persist or diminish at longer training.
205	
206	**m7. SFT comparison conflates paradigm with data efficiency.** Should match total compute or effective training signal.
207	
208	### Experiment Coverage vs Design
209	
210	All 12 imagined experiments from the experimental design are present in the paper. Coverage is complete. The primary gap is statistical depth (seeds) rather than breadth.
211	
212	| Experiment | Seeds | Coverage | Concern |
213	|---|---|---|---|
214	| FOL Exec-Only (plan_001) | 3 | ✓ Full | — |
215	| FOL Exec+STA (plan_002) | 3 | ✓ Full | — |
216	| FOL Held-Out (plan_003) | — | ✓ Full | Simpson's paradox |
217	| O(1) vs O(N) (plan_004) | 1 | ✓ Full | Need 3 seeds |
218	| Weight Ablation (plan_005) | 1 | ✓ Full | Need 3 seeds for top configs |
219	| Prolog (plan_006) | 1 | ✓ Full | Need 3 seeds |
220	| Multi-Logic (plan_007) | 1 | ✓ Full | Effects < noise |
221	| Cross-Logic (plan_008) | — | ✓ Full | Effects < noise |
222	| SFT Baseline (plan_009) | — | ✓ Full | Paradigm confound |
223	| SMT-LIB (plan_010) | 1 | ✓ Full | Need 3 seeds |
224	| Qwen3-8B (plan_011) | 1 | ✓ Full | Need 3 seeds |
225	| Hacking Characterization (plan_012) | — | ✓ Full | Annotator independence |
226	
227	### Recommendation
228	
229	**Reject with encouragement to revise and resubmit.** The core contribution — component ablation as a principled dense reward for formal reasoning — has genuine value and could be publishable with:
230	1. Proper related work (expand from 6 to 25+ references)
231	2. 3-seed runs for top-3 configurations beyond the primary FOL comparison
232	3. Either downstream task validation of ISR or larger external hacking annotation study
233	4. Honest statistical characterization (remove "Pareto-improving" for non-significant prove rate differences)
234	5. Either formalize RIP properly or reframe as component necessity testing
235	
236	The direction is promising and the paper would be competitive after these revisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95b252dc-57c3-4c55-b24c-be0666f515ec",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "870967e4-90d0-429e-8041-ecd48b9144bd",
  "sourceToolAssistantUUID": "95b252dc-57c3-4c55-b24c-be0666f515ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T22:43:44.395Z_

<details open><summary>🔧 Tool call — Read · `toolu_014kekHsHpvBQ5zMkXynADd8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "870967e4-90d0-429e-8041-ecd48b9144bd",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NpDJAjyWBYoMpUjFA8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e84d38c2-b1b9-4f49-8399-298b9e18197a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXyh5GYwGsJGzo35KVAPGZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12139,
      "cache_read_input_tokens": 28006,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12139
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 28006,
          "cache_creation_input_tokens": 12139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12139,
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

_source line 44 · 2026-05-13T22:43:44.401Z_

<details><summary>↩ Tool result · `toolu_014kekHsHpvBQ5zMkXynADd8`</summary>

```text
1	---
2	dream_id: dream_20260513T215750
3	tier: median
4	overall_score: weak reject (3/6)
5	timestamp: 2026-05-13T22:41:07.174689+00:00
6	---
7	
8	# Dream Review Report: Solver Trace Ablation (STA)
9	
10	**Paper**: "Solver Trace Ablation: A Mutation-Testing-Derived Methodology for Detecting Structural Degeneracy in RL-Trained Formalizers"
11	**Dream ID**: 20260513T215750
12	**Review Mode**: Full (2 Reviewers, 4-step roundtable)
13	**Date**: 2026-05-13
14	
15	---
16	
17	## 1. Paper Summary
18	
19	The paper introduces Solver Trace Ablation (STA), a methodology adapted from mutation testing's RIP (Reachability-Infection-Propagation) framework, for detecting structural degeneracy (reward hacking) in GRPO-trained formal logic generators. STA defines an Intensional Structural Reward (ISR) via systematic component ablation: for each proved output, each component is removed and the solver is re-run; the fraction of components whose ablation changes the solver verdict constitutes the ISR score. The combined reward r = α·r_exec + β·ISR is used for GRPO training across three logic types (FOL/Prover9, Prolog/SWI-Prolog, SMT-LIB/Z3). The paper reports 1.9× ISR improvement on held-out FOL data (0.132 vs 0.068), hacking rate reduction from 69% to 35%, at 5pp accuracy cost. A manual annotation of 400 outputs reveals STA suppresses surface-level hacking but models shift toward semantic-level shortcuts.
20	
21	---
22	
23	## 2. Reviewer Summaries
24	
25	### R1 (Methods + Experiments): Score 4/6 (Weak Accept)
26	R1 finds the paper addresses a real problem with a well-motivated approach. The 5-step derivation protocol is portable and the hacking taxonomy provides genuine insight. The honest "partial prevention" framing is commendable. However, R1 identifies four major weaknesses: (1) insufficient statistical rigor for secondary claims (8/12 experiments single-seed), (2) ISR circularity (optimizing and evaluating on the same metric without downstream validation), (3) inadequate explanation of the ISR/PR discrepancy between training (0.42) and held-out (0.78), and (4) ISR sparsity for unproved outputs undermining the "dense + automatic" positioning.
27	
28	### R2 (Novelty + Related Work): Score 3/6 (Weak Reject)
29	R2 finds the problem identification valuable but the novelty insufficient for a top venue. ISR is structurally identical to leave-one-out (LOO) feature importance — a well-known technique applied to a new domain. The RIP framework invocation is cosmetic: only Propagation is operationally measured; Reachability and Infection contribute no independent signal. Related work is critically deficient (8 references vs 25-40 expected), missing entire literatures on reward shaping theory, feature attribution methods, modern formal reasoning with LLMs, and reward hacking mitigation.
30	
31	---
32	
33	## 3. Roundtable Convergence
34	
35	### 3.1 Points of Agreement
36	
37	**Both reviewers agree on:**
38	
39	1. **Problem identification is valuable and timely.** Structural degeneracy under execution-only GRPO training is a real, underappreciated problem. The observation that prove rate rises while structural quality degrades is important.
40	
41	2. **RIP framework invocation is overstated.** Only the Propagation condition is operationally measured. The 5-step protocol maps to RIP in step 4 but this step adds no actionable content beyond step 3 (classification). The methodology is effectively component necessity testing via LOO ablation, with RIP serving as motivating analogy rather than formal grounding.
42	
43	3. **ISR is LOO ablation importance applied to a new domain.** ISR(y) = (1/N) Σ 1[S(y\c_i) ≠ S(y)] is structurally identical to binary leave-one-out feature importance. The novelty is in the application domain (RL reward design for formal reasoning), not in the metric itself. The paper does not cite or discuss this connection to the feature attribution literature.
44	
45	4. **ISR is sparse for the majority of training examples.** With prove rates of 10-26%, ISR provides zero signal for 74-90% of outputs. The "dense + automatic" positioning in the ORM-PRM taxonomy is misleading. ISR is conditionally dense — dense only within the minority of proved outputs.
46	
47	5. **Statistical rigor is insufficient for secondary claims.** Only the core FOL experiments (plans 001-002) use 3 seeds. Eight of twelve experiments use single seeds. Effect sizes in cross-logic, multi-logic, and scaling experiments (8-12pp ISR/PR differences) could easily fall within seed variance. No confidence intervals or significance tests are reported.
48	
49	6. **The hacking taxonomy is the strongest novelty element.** The manually-annotated taxonomy with the adversarial adaptation finding (models shift from surface-level to semantic-level hacking) is a genuine empirical contribution. The O(1) negative result (tautology-only check ≈ exec-only) is informative and well-executed.
50	
51	7. **Related work is thin.** 8 references is below venue standards. Missing citations to reward shaping theory (Ng et al. 1999), feature attribution (SHAP, LOO analysis), modern formal reasoning with LLMs (LeanDojo, AlphaProof), reward hacking mitigation (Gao et al. 2023), and the FOLIO dataset paper.
52	
53	8. **Honest framing is commendable.** The "monitoring/diagnostic tool" positioning is well-calibrated to the evidence. The paper does not overclaim.
54	
55	### 3.2 Points of Divergence
56	
57	**R1 emphasizes experimental concerns:**
58	- The ISR/PR discrepancy between training (0.42) and held-out (0.78) is inadequately explained. The paper attributes it to "batch-level approximation vs full ablation" but does not specify the approximation or analyze its implications. The exec-only condition shows stability (0.34→0.31), making the asymmetry suspicious.
59	- ISR circularity: optimizing ISR as reward and evaluating ISR as metric. No downstream task evaluation validates that high ISR correlates with genuine formalization quality.
60	- Missing random reward baseline: without controlling for multi-objective regularization, it is unclear whether ISR's specific formulation matters or any penalty on proved outputs achieves similar effects.
61	
62	**R2 emphasizes novelty concerns:**
63	- The conceptual advance is modest: recognizing that component ablation reveals structural necessity and using this as an RL reward. This is sound engineering but not a deep conceptual contribution.
64	- The 5-step derivation protocol is standard engineering methodology, not a methodological contribution.
65	- Missing connection to mutation testing theory (equivalent mutant problem, weak vs strong mutation, mutant subsuming).
66	
67	### 3.3 Converged Assessment
68	
69	After cross-sharing, both reviewers agree the paper is **borderline** for a top ML venue main track. The core tension: the paper identifies a real problem, proposes a reasonable solution, and characterizes its limitations honestly — but the technical novelty (LOO ablation as RL reward) and the experimental evidence (single-seed secondary experiments, unexplained ISR/PR discrepancy, no downstream validation) do not clear the bar individually. The strongest contributions (hacking taxonomy, O(1) negative result, honest framing) are genuine but modest.
70	
71	**Consensus score: 3.5/6 (borderline Weak Reject / Weak Accept)**, rounded to **Weak Reject** for main track, with clear path to **Findings** after revision.
72	
73	---
74	
75	## 4. Detailed Strengths
76	
77	**S1. Genuine problem identification (High impact).** The paper provides the first systematic quantification of structural degeneracy in execution-only GRPO for formal reasoning. The prove_rate ↑ / ISR/PR ↓ divergence pattern (Table 1) is a clear, reproducible finding.
78	
79	**S2. Hacking taxonomy with adversarial adaptation (Medium-high impact).** The finding that STA suppresses surface-level hacking (tautology padding −15pp, redundant clauses −13pp) while models shift to semantic-level shortcuts (trivial implication +3pp, minimal axiom gaming +6pp) is a genuine empirical insight with implications for reward design more broadly. κ=0.72 is substantial.
80	
81	**S3. O(1) negative result (Medium impact).** Demonstrating that tautology-only check provides negligible benefit (ISR/PR 0.33 ≈ exec-only 0.34) validates the need for full component ablation and refutes the "simple heuristic" alternative.
82	
83	**S4. Three-logic instantiation (Medium impact).** Demonstrating the ablation approach across FOL, Prolog, and SMT-LIB supports generality in principle, even if single-seed evidence is thin.
84	
85	**S5. Honest framing (Presentation strength).** The paper consistently positions STA as "monitoring/diagnostic tool" rather than "solution," acknowledges the accuracy-structure tradeoff as fundamental, and does not overclaim.
86	
87	**S6. Well-organized paper.** Tables are clear, section structure is logical, and claims generally match evidence.
88	
89	---
90	
91	## 5. Detailed Weaknesses
92	
93	### Major
94	
95	**W1. ISR novelty is overstated (Novelty, Major).**
96	ISR is structurally equivalent to binary LOO feature importance — a technique with decades of history in statistics and ML interpretability (Shapley values, SHAP, permutation importance). The paper does not acknowledge this connection. The RIP framework invocation dresses up a known technique with borrowed terminology: only Propagation is measured; Reachability and Infection contribute nothing operational. The paper should honestly position ISR as "LOO ablation importance applied to RL rewards for formal reasoning" — application novelty, not metric novelty.
97	
98	**W2. Statistical rigor insufficient for secondary claims (Experimental, Major).**
99	Eight of twelve experiments use single random seeds. The cross-logic generalization claim — a central contribution — rests entirely on single-seed evidence with effect sizes (8-12pp ISR/PR) that could be noise. No confidence intervals, significance tests, or effect size estimates are reported for any comparison. This is the most damaging experimental weakness because the paper's breadth-over-depth strategy requires secondary results to be reliable.
100	
101	**W3. ISR/PR discrepancy between training and held-out (Experimental, Major).**
102	The ISR/PR ratio jumps from 0.42 (training, Table 2) to 0.78 (held-out, Table 3) for the STA condition, while exec-only is stable (0.34→0.31). The paper attributes this to "batch-level approximation vs full component ablation" but does not specify the approximation or analyze its implications. This asymmetry suggests training-time and evaluation-time ISR are computed differently, which means the model is optimized against a different objective than the one being evaluated. The headline "1.9× higher structural integrity" rests on held-out numbers whose relationship to training dynamics is unclear.
103	
104	**W4. ISR circularity without downstream validation (Experimental, Major).**
105	The paper optimizes ISR as a reward and evaluates ISR improvement as the primary result. No downstream task evaluation (e.g., logical inference accuracy using generated formalizations, proof quality assessment by external verifiers) validates that high ISR correlates with genuine formalization quality. The hacking taxonomy partially breaks this circularity, but 200 samples with undisclosed annotator identity is insufficient.
106	
107	**W5. ISR sparsity undermines "dense + automatic" positioning (Framing, Major).**
108	With prove rates of 10-26%, ISR provides zero signal for 74-90% of training outputs. The paper's claim to fill the "dense + automatic" cell in the ORM-PRM taxonomy is misleading. ISR is conditionally dense — dense only within the small proved subset. This should be explicitly acknowledged.
109	
110	### Moderate
111	
112	**W6. Related work critically deficient (Presentation, Moderate).**
113	8 references is far below venue standards (25-40 expected). Missing entire literatures: reward shaping theory (Ng et al. 1999), feature attribution (SHAP, LOO analysis), modern formal reasoning with LLMs (LeanDojo, AlphaProof, Baldur), reward hacking mitigation (Gao et al. 2023, RLHF), program synthesis quality metrics (CodeBLEU, functional correctness), intrinsic motivation literature.
114	
115	**W7. No random reward baseline (Experimental, Moderate).**
116	Without a control for the general regularization effect of multi-objective optimization, it is unclear whether ISR's specific component-ablation formulation matters, or whether any penalty on proved outputs would achieve similar structural improvement. A random structural penalty baseline is needed.
117	
118	**W8. Hacking taxonomy is FOL-only (Experimental, Moderate).**
119	The paper claims cross-logic generalization but provides hacking characterization for only FOL. Prolog and SMT-LIB may exhibit entirely different hacking mode distributions. The taxonomy should be extended or the cross-logic characterization claim should be scoped down.
120	
121	**W9. 500 training steps may be insufficient (Experimental, Moderate).**
122	Both ISR/PR curves are still declining at step 500. It is unknown whether STA's benefit persists, grows, or vanishes at longer horizons. The paper should either show convergence or explicitly bound the claim to the observed training horizon.
123	
124	### Minor
125	
126	**W10. 5-step protocol is standard engineering (Novelty, Minor).**
127	"Run a pilot, observe failures, categorize, design mitigations" is standard engineering methodology. Presenting this as a core contribution overstates its novelty, though it has value for reproducibility.
128	
129	**W11. Curriculum scheduling analysis is shallow (Experimental, Minor).**
130	The sigmoid curriculum is the best-performing configuration but its hyperparameters are not ablated. Whether sigmoid outperforms linear ramp is unknown.
131	
132	**W12. ISR sensitivity to decomposition granularity unaddressed (Method, Minor).**
133	The protocol does not guide practitioners on choosing the ablation unit. Discriminability varies 2× across logic types (0.38 vs 0.17), likely reflecting decomposition granularity differences, but no guidance is provided.
134	
135	---
136	
137	## 6. Questions for Authors
138	
139	1. **ISR/PR discrepancy**: Can you precisely specify how training-time ISR computation differs from held-out evaluation ISR? Why does the exec-only condition show stability (0.34→0.31) while exec+STA shows a large gap (0.42→0.78)?
140	
141	2. **Random baseline**: Have you evaluated whether a random structural penalty (e.g., penalizing proved outputs by a random score) achieves comparable ISR/PR improvement? This would isolate ISR's specific signal from the general multi-objective regularization effect.
142	
143	3. **Downstream validation**: Do high-ISR formalizations correlate with better downstream logical inference performance? Have you evaluated the generated FOL formulas on a downstream reasoning task?
144	
145	4. **ISR and feature attribution**: ISR is structurally equivalent to binary LOO feature importance. How does it relate to Shapley values or SHAP? Have you considered interaction effects (components that are individually necessary but collectively encode trivial reasoning)?
146	
147	5. **RIP beyond Propagation**: Could Reachability (does the solver process the component?) and Infection (does removing it change intermediate solver state?) provide additional signals? If not, why invoke the full RIP framework?
148	
149	6. **Training horizon**: Do you have any data beyond 500 steps? Does the ISR/PR gap between conditions converge, diverge, or remain stable?
150	
151	---
152	
153	## 7. Experiment Coverage Assessment
154	
155	All 12 imagined experiments from the review context are covered in the paper:
156	- plan_001 (FOL exec-only baseline) ✓ Table 1
157	- plan_002 (FOL exec+STA) ✓ Table 2
158	- plan_003 (FOL held-out evaluation) ✓ Table 3
159	- plan_004 (O(1) vs O(N) ablation) ✓ Table 4
160	- plan_005 (reward weight ablation + curriculum) ✓ Table 5
161	- plan_006 (Prolog single-logic) ✓ Table 6
162	- plan_007 (Multi-logic GRPO) ✓ Table 8
163	- plan_008 (Cross-logic transfer) ✓ Table 7
164	- plan_009 (SFT baseline) ✓ Table 3
165	- plan_010 (SMT-LIB single-logic) ✓ Table 6
166	- plan_011 (Qwen3-8B scaling) ✓ Table 9
167	- plan_012 (Hacking characterization) ✓ Table 10
168	
169	Coverage is complete. The concern is not coverage but depth: only plans 001-002 have multi-seed support; the remaining 10 experiments are single-seed.
170	
171	---
172	
173	## 8. Scores
174	
175	| Criterion | R1 | R2 | Consensus |
176	|-----------|----|----|-----------|
177	| Overall | 4/6 (Weak Accept) | 3/6 (Weak Reject) | **3/6 (Weak Reject)** |
178	| Soundness | 2/4 | 2/4 | **2/4** |
179	| Presentation | 3/4 | 3/4 | **3/4** |
180	| Contribution | 3/4 | 2/4 | **2/4** |
181	| Confidence | 4/5 | 4/5 | **4/5** |
182	
183	**Consensus Overall: 3/6 (Weak Reject)**
184	
185	---
186	
187	## 9. Meta-Review and Recommendation
188	
189	This paper identifies a genuine problem (structural degeneracy in execution-only GRPO for formal reasoning) and proposes a reasonable solution (component ablation as structural reward). The honest "monitoring/diagnostic tool" framing is well-calibrated to the evidence, and the hacking taxonomy with adversarial adaptation is a genuine empirical insight.
190	
191	However, the paper has significant weaknesses that place it below the acceptance threshold for a top ML venue main track:
192	
193	1. **Novelty concerns dominate.** ISR is LOO ablation importance applied to a new domain — useful application but not a conceptual advance. The RIP framework invocation is cosmetic. The 5-step protocol is standard engineering. The related work is critically thin.
194	
195	2. **Experimental evidence is insufficiently rigorous.** Single-seed secondary experiments cannot support cross-logic generalization claims. The ISR/PR training-vs-held-out discrepancy is unexplained. No downstream validation breaks the ISR circularity. No random baseline isolates ISR's specific contribution.
196	
197	3. **Framing issues.** The "dense + automatic" ORM-PRM positioning is misleading given ISR's sparsity for unproved outputs. The RIP grounding claim overstates the theoretical contribution.
198	
199	**Recommendation**: Reject for top venue main track. The paper has a clear path to acceptance at EMNLP Findings or a workshop after:
200	- Expanding related work to 25+ references (reward shaping, feature attribution, modern formal reasoning, reward hacking mitigation)
201	- Honestly repositioning ISR as domain-specific application of LOO ablation
202	- Adding multi-seed support for at least Prolog and scaling experiments
203	- Providing downstream validation or a random baseline to address circularity
204	- Explaining or resolving the ISR/PR training-vs-held-out discrepancy
205	- Acknowledging ISR's conditional density limitation
206	
207	The strongest version of this paper would: (a) lead with the hacking taxonomy and adversarial adaptation as the primary contribution, (b) position STA/ISR as the tool that enabled the discovery rather than the contribution itself, and (c) use the O(1) negative result and cross-logic instantiation as supporting evidence for the importance of comprehensive structural analysis.
208	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e84d38c2-b1b9-4f49-8399-298b9e18197a",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "2bb2974c-0507-48f1-b67c-608742b0bff1",
  "sourceToolAssistantUUID": "e84d38c2-b1b9-4f49-8399-298b9e18197a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-13T22:43:49.565Z_

Now I have a thorough understanding of the paper, its experimental results, the project's internal state, and the existing review reports. Let me also check what the paper summary describes vs. what the "best" dream paper actually contains, since there are notable discrepancies between the user's summary and the dream paper.

Let me now produce my R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bb2974c-0507-48f1-b67c-608742b0bff1",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NpenMBKGoV6zuJfPxA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd48959c-1233-4452-81c6-831749ebe6b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvSk3MA2zLiz4Z9SsR6mJW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11327,
      "cache_read_input_tokens": 40145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11327,
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

_source line 46 · 2026-05-13T22:43:50.526Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0154R5Fcrt9thA1A7o9hUrHx`</summary>

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
  "parentUuid": "dd48959c-1233-4452-81c6-831749ebe6b2",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1NpenMBKGoV6zuJfPxA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1340ff2-ca45-4641-9150-3d4e1eba2e75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvSk3MA2zLiz4Z9SsR6mJW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11327,
      "cache_read_input_tokens": 40145,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11327
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 40145,
          "cache_creation_input_tokens": 11327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11327,
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

_source line 47 · 2026-05-13T22:43:50.529Z_

<details><summary>↩ Tool result · `toolu_0154R5Fcrt9thA1A7o9hUrHx`</summary>

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
  "parentUuid": "a1340ff2-ca45-4641-9150-3d4e1eba2e75",
  "isSidechain": true,
  "promptId": "beaf84d3-8e91-46ec-b6c4-24d78ed821ab",
  "agentId": "ab6c520c6c7f9a8aa",
  "type": "user",
  "uuid": "1828df7b-5a13-4c3d-b566-39483b712f17",
  "sourceToolAssistantUUID": "a1340ff2-ca45-4641-9150-3d4e1eba2e75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-13T22:45:26.185Z_



## R2 Review: Novelty & Related Work

### Summary
The paper proposes Solver Trace Ablation (STA), adapting leave-one-out component ablation from mutation testing to derive a continuous structural reward (ISR) for GRPO training of formal logic generators. The paper frames this as grounded in the RIP (Reachability-Infection-Propagation) framework. The user's summary describes a "principled negative result" paper (STA works as diagnostic but fails as training reward), but the "best" dream paper tells a different, more optimistic story (STA is Pareto-improving). The actual experimental evidence from the project's memory.md and decisions.yaml tells a third story: STA with 50/50 weighting caused prove-rate regression below baseline (0.10 < 0.12), the O(1) approximation failed completely, and the causal attribution of ISR/PR decline remains unresolved. This review evaluates novelty and related work based on the paper as described in the user's summary.

### Strengths

- **Genuine problem identification.** Structural degeneracy under execution-only GRPO is a real, underappreciated phenomenon. The observation that prove rate rises while structural quality degrades (ISR/PR 0.82 to 0.29) is an important empirical finding that deserves documentation.

- **Principled negative result framing is honest.** Reporting that STA fails as a training reward (prove rate drops from 0.24 to 0.11) rather than cherry-picking positive angles reflects intellectual integrity. Negative results with mechanistic explanation (gradient variance amplification in low-prove-rate regime) are valuable to the community.

- **O(1) vs O(N) ablation provides genuine insight.** Demonstrating that a tautology-only check is insufficient---that domain-specific hacking modes require correspondingly granular ablation---is informative and refutes the simplest alternative to the proposed method.

- **Hacking taxonomy with inter-annotator agreement.** The 200-sample annotation with kappa=0.72 identifying four hacking modes (tautology injection 28%, vacuous quantification 19%, premise redundancy 14%, trivial conclusion 8%) is the paper's most concrete empirical contribution, providing a reusable categorization for future work.

- **SFT comparison contextualizes the finding.** Showing that SFT (PR=0.30, ISR/PR=0.50, hack%=50%) dominates both GRPO conditions on structural quality helps calibrate what "good" structural quality looks like under different training paradigms.

### Weaknesses

- **(Major) ISR is leave-one-out ablation importance applied to a new domain, not a novel metric.** ISR(f) = (1/n) * sum of indicator functions for whether removing component c_i changes the solver output is structurally identical to binary leave-one-out (LOO) feature importance, a technique with decades of history in statistics (Cook's distance, 1977), ML interpretability (SHAP, Lundberg & Lee 2017), and sensitivity analysis. The paper does not acknowledge this connection. Presenting ISR as a novel metric derived from the RIP framework inflates the contribution. The honest framing is: "We apply LOO component importance---a well-known technique---as an RL reward signal for formal reasoning, which to our knowledge is new."

- **(Major) The RIP framework invocation is cosmetic.** Only Propagation is operationally measured (does ablation change the output?). Reachability (is the component syntactically reachable?) and Infection (does removing the component change intermediate solver state?) contribute no independent diagnostic or reward signal. The paper never uses R or I as separate measures. The three-stage RIP decomposition collapses into a single binary test. "Component necessity testing" would be equally accurate and less misleading. If the authors want to claim RIP grounding, they should formalize R and I as independent signals and show they provide value beyond P alone.

- **(Major) Only 4 references is critically deficient.** This is the most immediately disqualifying weakness. A venue paper in this space should have 25-40 references. Entire literatures are missing:
  - **GRPO itself**: Shao et al. (2024), "DeepSeekMath." The paper uses GRPO as its core RL algorithm without citing the paper that introduced it.
  - **Reward hacking/overoptimization**: Skalse et al. (2022), "Defining and Characterizing Reward Hacking"; Gao et al. (2023), "Scaling Laws for Reward Model Overoptimization." The paper's central problem statement is reward hacking, yet these foundational works are absent.
  - **Reward shaping theory**: Ng et al. (1999), "Policy invariance under reward transformations." STA's combined reward should be analyzed through this lens---is the ISR component potential-based? If not, it can change the optimal policy in unintended ways.
  - **FOLIO dataset**: Han et al. (2022), "FOLIO: Natural Language Reasoning with First-Order Logic." The primary dataset is used without citation.
  - **Modern formal verification + LLMs**: LeanDojo (Yang et al. 2024), Baldur (First et al. 2023), AlphaProof (DeepMind 2024), COPRA (Thakur et al. 2024). These represent the state of the art in formal reasoning with LLMs.
  - **Process reward models**: Lightman et al. (2023) is mentioned in the summary's related work section but is apparently not in the bibliography. Math-Shepherd (Wang et al. 2024) learns dense process rewards automatically from execution feedback---directly competing with STA's "dense + automatic" positioning.
  - **Feature attribution**: SHAP (Lundberg & Lee 2017), permutation importance, Shapley values. ISR's structural equivalence to LOO importance must be discussed.
  - **Mutation testing beyond Jia & Harman**: equivalent mutant problem (Budd & Angluin 1982), weak vs. strong mutation (Howden 1982), mutation testing for ML (DeepMutation, Ma et al. 2018). The paper cites only one mutation testing reference.
  - **Structural rewards in code generation**: CodeRL (Le et al. 2022), RLTF (Liu et al. 2023), execution-guided code generation. These provide structural reward signals from execution traces in a closely related domain.
  - **RLHF reward hacking mitigation**: Touvron et al. (2023), constrained RL approaches, reward model ensembles.

- **(Major) The 5-step derivation protocol is standard engineering methodology, not a theoretical contribution.** "Run a pilot, observe failure modes, categorize them, map to a framework, design targeted checks" describes what any competent engineer would do. Presenting this as a core contribution alongside the ISR metric overstates its novelty. It has value for reproducibility but should be positioned as a practical guide, not a methodological contribution.

- **(Moderate) The negative result may be predictable rather than surprising.** Adding a noisy, high-variance reward component (ISR, which requires the output to first prove---a rare event at 12-24% prove rate) to a sparse reward signal in a low-signal regime would be expected to degrade training by any RL practitioner familiar with reward shaping literature. The gradient variance amplification explanation is essentially: "adding a noisy reward to a sparse reward makes training harder." This is known. The paper should explicitly engage with the reward shaping literature (Ng et al. 1999) to argue why this negative result is non-obvious.

- **(Moderate) Scope is too narrow for the generality claimed.** Single model (Qwen2.5-1.5B), single logic type (FOL with Prover9), Prolog STA instantiation failed, SMT-LIB and 8B scaling not attempted, no positive cross-logic transfer. The paper claims STA is a "general, solver-agnostic procedure" but demonstrates it on exactly one solver-language pair successfully. The 5-step protocol's generality is aspirational, not demonstrated.

### Questions for Authors

1. **LOO equivalence**: ISR is structurally identical to binary leave-one-out feature importance. How do you differentiate STA from simply applying LOO ablation as a reward signal? Have you considered interaction effects (pairs of components that are individually necessary but jointly encode trivial reasoning)?

2. **Reward shaping theory**: Is the ISR component of your combined reward potential-based in the sense of Ng et al. (1999)? If not, what guarantees that adding ISR does not systematically bias the learned policy away from the optimal policy under the true reward?

3. **Predictability of negative result**: An RL practitioner might predict that adding a high-variance reward component (ISR, defined only for ~15% of outputs) to an already sparse signal would degrade training. What makes the negative result non-obvious? What prior work, if any, would have predicted the opposite?

4. **RIP beyond Propagation**: Have you attempted to measure Reachability (does the solver parse/process the component?) or Infection (does removing it change intermediate solver state before the final verdict?) as independent signals? If these provide no additional information, the RIP framework adds no value over "component necessity testing."

5. **Why not compare against a random structural penalty?** Without a control where proved outputs receive a random penalty score, it is unclear whether ISR's specific component-ablation formulation matters, or whether any regularization of proved outputs would achieve similar diagnostic power.

### Detailed Comments

**Novelty Assessment.** The core technical idea---ablating components of formal expressions and re-running the solver to measure structural necessity---is conceptually straightforward. It is a direct application of leave-one-out analysis, a technique so fundamental it predates modern ML by decades. The paper's novelty claim rests on two pillars: (1) the RIP framework grounding, and (2) the application to RL reward design. Pillar (1) is weak because only one of three RIP conditions is measured. Pillar (2) is genuine but modest---applying a known technique to a new domain is useful but typically insufficient for a top venue main track paper as the primary contribution. The negative result (STA fails as training reward) could strengthen the novelty if it provided deep mechanistic insight, but the explanation offered (gradient variance amplification) is essentially that sparse, noisy rewards hurt training---a known phenomenon.

**Positioning.** The paper positions STA in the "dense + automatic" cell of the ORM-PRM taxonomy, but this positioning is undermined by ISR being undefined for 75-88% of training outputs (those that fail to prove). For unproved outputs, r(f) = alpha * 0 + beta * 0 * ISR = 0. STA provides zero signal for the vast majority of training examples. Calling this "dense" is misleading---it is conditionally dense, dense only within the minority of proved outputs. The paper should honestly acknowledge this limitation. Furthermore, the ORM-PRM comparison omits Math-Shepherd and similar approaches that learn dense process rewards automatically from execution feedback, which occupy the same "dense + automatic" cell.

**Related Work.** The related work is not merely thin---it is critically deficient to a degree that suggests the authors are unfamiliar with significant portions of the relevant literature. Four references for a paper that spans RL, formal verification, mutation testing, reward hacking, and neurosymbolic reasoning is untenable. The omission of GRPO's own citation (Shao et al. 2024) and the FOLIO dataset citation (Han et al. 2022) are particularly concerning, as these are the paper's own algorithm and dataset. The paper also fails to cite the reward hacking literature it claims to contribute to (Skalse et al. 2022; Gao et al. 2023), the reward shaping theory relevant to its combined reward formulation (Ng et al. 1999), and the modern formal verification + LLM landscape (LeanDojo, AlphaProof, Baldur). A revised version needs at minimum 25 references with substantive engagement, not just citation padding.

**Significance.** The negative result (STA fails as training reward) is potentially valuable if properly contextualized. However, the paper must demonstrate that the negative result is non-obvious and actionable. Currently, the mechanistic explanation (gradient variance in low-prove-rate regimes) suggests the failure is a consequence of reward sparsity interacting with reward noise---a phenomenon well-documented in the RL literature. The diagnostic contribution (ISR detects 74% of degenerate outputs) is more clearly useful, but framing the paper as "STA as diagnostic tool" requires different positioning than "STA as reward design methodology." The hacking taxonomy with four modes and differential ISR sensitivity is the most novel empirical contribution and could anchor a reframed paper.

**Scope.** The claims are tested on Qwen2.5-1.5B with Prover9 on FOLIO-format FOL tasks only. Prolog STA failed, SMT-LIB was not attempted, 8B scaling was not attempted. The paper's claim to generality through the 5-step derivation protocol is aspirational. A single successful instantiation does not validate a "general, solver-agnostic procedure." At minimum, one additional successful instantiation is needed.

### Scores
- Novelty: 2/4
- Related Work: 1/4
- Significance: 2/4
- Writing Quality: 3/4
- Overall recommendation: 2/6 (Reject)
- Confidence: 4/5

**Justification for overall score.** The paper addresses a genuine problem and the hacking taxonomy is a real contribution, but the combination of (1) critically deficient related work (4 references), (2) overstated novelty (LOO ablation presented as RIP-grounded framework), (3) narrow scope (single logic, single model, failed extensions), and (4) a negative result whose non-obviousness is not established places the paper below the acceptance threshold. The paper would benefit from: expanding related work to 25+ references with substantive engagement; honestly repositioning ISR as domain-specific LOO ablation; demonstrating at least one additional successful STA instantiation; and either establishing the negative result's non-obviousness through engagement with reward shaping theory or reframing around the hacking taxonomy as the primary contribution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1828df7b-5a13-4c3d-b566-39483b712f17",
  "isSidechain": true,
  "agentId": "ab6c520c6c7f9a8aa",
  "requestId": "req_011Cb1Nq7CLqJ66cwbZhDXZn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59358cdb-4025-46eb-b828-911d7f7a55b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "sessionId": "c0563a1f-a2e2-46fc-bceb-71d67853ad00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PdT2a1fhSFmgJRZnS17Yqy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 51472,
      "output_tokens": 3385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 744
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3385,
          "cache_read_input_tokens": 51472,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 744,
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
