# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aadba285677a62d0f.jsonl`
- **Structured JSON:** [`83d3108a23c2dececad3.json`](../../sessions/83/83d3108a23c2dececad3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-17T15:48:34.676Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus areas: **novelty/contribution significance** and **related work positioning**.

## Paper Summary

**Title**: "Temporal Aggregation as Implicit Adversarial Defense: Why Streaming Safety Monitors Resist Adaptive Attacks"

**Core claim**: Streaming safety monitors that use temporal aggregation over hidden-state activations are inherently more robust to adversarial attacks (GCG, RL-Obfuscation) than static classifiers and text-level monitors. The paper constructs "StreamProbe-Bench" evaluating 3 monitors (NExT-Guard, Kelp, TrajGuard) on DeepSeek-R1-Distill-7B.

**Claimed contributions**:
1. StreamProbe-Bench: first adversarial robustness benchmark for streaming safety monitors (64-72% F1 under white-box attacks)
2. Controlled decomposition showing temporal aggregation provides 6pp AUC robustness benefit (p=0.003) independent of specific strategy
3. Evasion-quality Pareto analysis: temporal monitors force 2-4x worse tradeoffs
4. Comprehensive negative result on CoT premeditation detection across 5 layers

**Paper structure** (8 pages):
- §1 Introduction: frames the evaluation gap, presents surprising positive robustness finding
- §2 Related Work: 3 paragraphs covering streaming monitors, adversarial attacks on safety systems, temporal processing and robustness
- §3 Method: threat model (white-box), 3 monitors described, controlled decomposition design, evaluation data
- §4 Experiments: GCG results (Table 1), RL-Obfuscation (Table 2), controlled decomposition (Table 3), Pareto analysis (Table 4), probe fidelity (Table 5), cross-model validation (Table 6), CoT premeditation (Table 7), vulnerability analysis (Table 8)
- §5 Discussion: mechanistic explanation, deployment implications, robustness limitations, CoT implications
- §6 Limitations: reimplementation fidelity, compute budget, model coverage, CoT sample size
- §7 Conclusion

**Key details for your review**:
- Only NExT-Guard uses official code. Kelp (11pp F1 deviation, 85% match) and TrajGuard (13pp F1 deviation, 80% match) are reimplemented
- The "first adversarial evaluation of streaming monitors" claim needs verification against literature
- The temporal robustness insight has precedent in time-series anomaly detection and video robustness (paper acknowledges this briefly in Related Work)
- The paper was reframed from an attack-focused paper to a defense-analysis paper (originally hypothesized monitors would be vulnerable, found they weren't)
- Related Work is only 3 short paragraphs, covering: streaming monitors, adversarial attacks, temporal processing
- References are sparse (the paper doesn't show a reference list in the provided pages)
- The controlled decomposition is the core novelty claim - isolating temporal aggregation as the robustness mechanism
- The negative CoT finding is presented as a contribution but builds on Phase 0 data that already existed

## Your Review Task

Evaluate novelty and related work. Structure your review as:

1. **Summary** (2-3 sentences)
2. **Novelty Assessment** (for each claimed contribution: is it genuinely new? incremental? expected?)
3. **Related Work Critique** (coverage, positioning, missing references)
4. **Strengths** (bulleted, specific)
5. **Weaknesses** (bulleted, specific, with severity: major/minor)
6. **Framing and Narrative** (is the story coherent? does the paper oversell or undersell?)
7. **Questions for Authors**
8. **Preliminary Score** (1-6) with justification
9. **Confidence** (1-5, where 5 = expert)

Be rigorous. Focus on:
- Is the "first adversarial evaluation" claim accurate? Has anyone else done this?
- Is the temporal aggregation insight novel or obvious in hindsight? (smoothing provides noise resistance is well-known)
- Is 3 paragraphs of Related Work sufficient for a top venue? Are key references missing?
- Does the reframing from "attack paper" to "defense analysis paper" feel natural or forced?
- Is the controlled decomposition genuinely a contribution, or is it obvious that averaging provides noise robustness?
- How does this compare to the broader literature on adversarial robustness in other domains?
- Is the negative CoT finding a contribution or padding?
- Does the paper adequately differentiate from concurrent/prior work on LLM safety monitor robustness?

Output your complete review in markdown format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "5b90edd1-533d-4780-92c8-073ad59bee3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T15:48:34.677Z_

```json
{
  "parentUuid": "5b90edd1-533d-4780-92c8-073ad59bee3d",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
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
  "uuid": "7a55d909-432e-408f-b431-fb2a4179966f",
  "timestamp": "2026-05-17T15:48:34.677Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T15:48:37.530Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a55d909-432e-408f-b431-fb2a4179966f",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QQ7SnQemD8At5wSKP6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2c20ff6-e40e-418d-b3dd-69b706189dca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1avjrzxwjK3vGRvKDJNHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8282,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8282,
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

_source line 4 · 2026-05-17T15:48:37.974Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ud8iZXa4Xxr6NBNikfy3Ns`</summary>

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
  "parentUuid": "f2c20ff6-e40e-418d-b3dd-69b706189dca",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QQ7SnQemD8At5wSKP6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44a975aa-dd01-4e52-809c-13faf399fa25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1avjrzxwjK3vGRvKDJNHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8282,
      "cache_read_input_tokens": 8255,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8282
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8282,
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

_source line 5 · 2026-05-17T15:48:37.977Z_

<details><summary>↩ Tool result · `toolu_01Ud8iZXa4Xxr6NBNikfy3Ns`</summary>

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
  "parentUuid": "44a975aa-dd01-4e52-809c-13faf399fa25",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "bca74ad7-0eee-44d2-af98-2a07a7a8657f",
  "sourceToolAssistantUUID": "44a975aa-dd01-4e52-809c-13faf399fa25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T15:48:40.577Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01X8xPHYHcYchycqmEtP5ZHo`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bca74ad7-0eee-44d2-af98-2a07a7a8657f",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QQMf3rFobWRqkYAst8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b17a543-62ff-4b16-be60-e9d2d4c1b80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUCuCe96u5ck75uzKqUtNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-17T15:48:40.600Z_

<details><summary>↩ Tool result · `toolu_01X8xPHYHcYchycqmEtP5ZHo`</summary>

```text
{"result":"# 项目 streamprobe_adversarial_robustness 概况\n\n## 实验状态 (4 个)\n\n- **phase0_mvp_pipeline**: RUNNING (negative) — \n- **phase0_step4_5_recovery**: PREPARING — \n- **mvp_benign_trace_gen**: ANALYZING (success) — \n- **mvp_trace_gen**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| phase0_mvp_pipeline | Hidden-state probes on DeepSeek-R1-Distill-7B CoT traces detect harmful premeditation (AUC>0.85) with temporal drift evidence (relaxed_B>=20%) using D003 onset definition (response-level, post-&lt;/think> boundary) | — | — | — |\n| mvp_benign_trace_gen | DeepSeek-R1-Distill-7B generates multi-step reasoning traces on benign prompts (GSM8K/ARC-Challenge) that serve as safe-class control for probe training, with comparable trace length/complexity to harmful traces | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_trace_gen** (failed): DeepSeek-R1-Distill-7B with unified config (temp=1.0, no system prompt) on harmful prompts produces a mix of complied and refused traces sufficient for MVP (≥150 each from 500 prompts)\n\n## 趋势\n成功 0 / 负向 0 / 失败 1 / 共 1\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-39593: 无 GPU 信息\n\n## 告警\n- mvp_trace_gen: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b17a543-62ff-4b16-be60-e9d2d4c1b80c",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "0ef1e607-b819-45ca-b09f-e25b361b6b15",
  "sourceToolAssistantUUID": "9b17a543-62ff-4b16-be60-e9d2d4c1b80c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T15:48:41.578Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EDk3E9qZWqNv5v5HsqRxE6`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ef1e607-b819-45ca-b09f-e25b361b6b15",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QQMf3rFobWRqkYAst8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a89a7128-81e5-4977-923e-9bf59ff19dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUCuCe96u5ck75uzKqUtNX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 9 · 2026-05-17T15:48:41.588Z_

<details><summary>↩ Tool result · `toolu_01EDk3E9qZWqNv5v5HsqRxE6`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'streamprobe_adversarial_robustness'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a89a7128-81e5-4977-923e-9bf59ff19dda",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "0537615e-962a-4694-bd56-22f5db434dab",
  "sourceToolAssistantUUID": "a89a7128-81e5-4977-923e-9bf59ff19dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T15:48:42.045Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NggqocifsiFZbmyHK6piY7`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0537615e-962a-4694-bd56-22f5db434dab",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QQMf3rFobWRqkYAst8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5079fb12-8a99-4fcd-a8a2-3caaa6556d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PUCuCe96u5ck75uzKqUtNX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16537,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 269,
          "cache_read_input_tokens": 16537,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1447,
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

_source line 11 · 2026-05-17T15:48:42.068Z_

<details><summary>↩ Tool result · `toolu_01NggqocifsiFZbmyHK6piY7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'streamprobe_adversarial_robustness'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5079fb12-8a99-4fcd-a8a2-3caaa6556d31",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "35e34bf7-06f3-46eb-b8a3-f96daaa62360",
  "sourceToolAssistantUUID": "5079fb12-8a99-4fcd-a8a2-3caaa6556d31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T15:48:45.816Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KBtNjkdULLtvybaSeHeHX5`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35e34bf7-06f3-46eb-b8a3-f96daaa62360",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QQfoTdTJC9kmYLRZRA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aba4240b-7425-46d3-a092-14b15c653e18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtK8GkiY9Vyvo6vSPcfrgo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 17984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1083,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 13 · 2026-05-17T15:48:45.828Z_

<details><summary>↩ Tool result · `toolu_01KBtNjkdULLtvybaSeHeHX5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| phase0_mvp_pipeline | Hidden-state probes on DeepSeek-R1-Distill-7B CoT traces detect harmful premeditation (AUC>0.85) with temporal drift evidence (relaxed_B>=20%) using D003 onset definition (response-level, post-&lt;/think> boundary) | — | — | — |\\n| mvp_benign_trace_gen | DeepSeek-R1-Distill-7B generates multi-step reasoning traces on benign prompts (GSM8K/ARC-Challenge) that serve as safe-class control for probe training, with comparable trace length/complexity to harmful traces | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_trace_gen** (failed): DeepSeek-R1-Distill-7B with unified config (temp=1.0, no system prompt) on harmful prompts produces a mix of complied and refused traces sufficient for MVP (≥150 each from 500 prompts)\\n\\n## 趋势\\n成功 0 / 负向 0 / 失败 1 / 共 1\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39593: 无 GPU 信息\\n\\n## 告警\\n- mvp_trace_gen: 训练失败 — unknown\\n\", \"total_chars\": 1017, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aba4240b-7425-46d3-a092-14b15c653e18",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "edb9776d-ff20-487d-bb2b-73fc98a2b3aa",
  "sourceToolAssistantUUID": "aba4240b-7425-46d3-a092-14b15c653e18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T15:48:46.841Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UTXASY4SxmJfJLbyVV8PU4`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edb9776d-ff20-487d-bb2b-73fc98a2b3aa",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QQfoTdTJC9kmYLRZRA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9feb4b4e-fac3-49e1-ab07-11dc851a9cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtK8GkiY9Vyvo6vSPcfrgo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 17984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1083,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 15 · 2026-05-17T15:48:46.853Z_

<details><summary>↩ Tool result · `toolu_01UTXASY4SxmJfJLbyVV8PU4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/ROADMAP.md\", \"content\": \"# streamprobe_adversarial_robustness — Research Dashboard\\n\\n> 最后更新: 2026-05-17 14:51 UTC | 更新原因: D006 MVP FAIL pivot to benchmark-primary; research 阶段启动; Dream 模拟进行中\\n\\n> 核心方向已 pivot（D006）\\n\\n## 核心方向\\n\\n**Benchmark-primary**: StreamProbe-Bench — 首个 streaming safety monitor 对抗鲁棒性 benchmark。评估 Kelp/NExT-Guard/TrajGuard 在 GCG + RL-Obfuscation 下的鲁棒性。Secondary: 架构脆弱性分析 + CoT premeditation 阴性结果。详见 paper_framing.md。\\n\\n目标投稿：**ARR May 25, 2026**（7 天，D2=May 18）\\n\\n## 当前进展\\n\\n- 阶段：Research（MVP FAIL → pivot to benchmark-primary）\\n- MVP 结论：Layer 16 hidden states 在 CoT 中无 premeditation signal（token AUC=0.49 反预测）\\n- 基础设施：westd-39593（4×5090 32GB），200GB 数据盘\\n- Phase 0 产出：500 harmful traces（204 complied）+ 200 benign + probe_v2 checkpoint + hidden states\\n- Dream 模拟已启动（dream_20260517T145100），等待结果\\n\\n## 近期任务\\n\\n- [x] GPU 到位 + 环境部署\\n- [x] 代码框架 6 模块\\n- [x] Phase 0 trace gen + onset + probe + temporal（MVP FAIL，D006）\\n- [ ] Dream 结果评估（等待 10-25min）\\n- [ ] NExT-Guard 官方代码 clone + 验证\\n- [ ] Kelp/TrajGuard 论文规格调研（Agent 执行中）\\n- [ ] Qwen2.5-7B-Instruct 下载\\n- [ ] 修复 temporal_analysis.py（trace-level FPR control + cusum_max AUC）\\n- [ ] benchmark 实验启动（Dream 通过后）\\n\\n## 7 天 Timeline（May 18-25）\\n\\n| Phase | Days | 工作 | 状态 |\\n|-------|------|------|------|\\n| Plan | D2 | Dream + framing 确认 + 实验审批 | 进行中 |\\n| Benchmark | D2-5 | 3 monitors × (GCG + RL-Obfuscation) | 待启动 |\\n| Analysis | D4-6 | Controlled decomposition + vulnerability analysis + negative finding | 待启动 |\\n| Paper | D5-8 | Results → Method → Intro → Abstract | 待实验 |\\n\\n## GPU 预算\\n\\n- 分配：4×5090 32GB（westd-39593），全部属本项目（C001）\\n- P0：~101 GPU-hours | P1：~42h | P2：~16h\\n- 可用：672 GPU-hours（4卡×7天×24h），headroom 充足\\n- 瓶颈：RL-Obfuscation ~24h/monitor，3 monitors 可跨 GPU 并行\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-17 | D006: MVP FAIL — pre-onset CoT 无可检测的 premeditation | phase0_mvp_pipeline |\\n| D005 | 2026-05-17 | D004 降级为 CONDITIONAL：Reviewer 指出 probe 过拟合 + P95 异 | phase0_mvp_pipeline |\\n| D004 | 2026-05-17 | MVP 判定：Qualified PASS — pre-onset per-token AUC 不达 | mvp_trace_gen |\\n| D003 | 2026-05-17 | Onset 重定义为 response（&lt;/think> 后）首个 harmful token，Co | mvp_trace_gen |\\n| D002 | 2026-05-17 | Onset 定义修正：从\\\"首次 harmful topic mention\\\"改为\\\"首次 action | mvp_trace_gen |\\n| D001 | 2026-05-17 | Safe class 使用 benign prompts（GSM8K/ARC），不依赖 same-p | mvp_trace_gen |\\n\\n\\n\", \"total_chars\": 2296, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9feb4b4e-fac3-49e1-ab07-11dc851a9cc2",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "e6c0ddd9-5d5c-4801-bcf0-f5e7c217d7db",
  "sourceToolAssistantUUID": "9feb4b4e-fac3-49e1-ab07-11dc851a9cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T15:48:47.121Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012JsYSxws1pw1dTGr59vx3F`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6c0ddd9-5d5c-4801-bcf0-f5e7c217d7db",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QQfoTdTJC9kmYLRZRA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8340f95-1134-460f-b5f9-01276e139504",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtK8GkiY9Vyvo6vSPcfrgo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 17984,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 307,
          "cache_read_input_tokens": 17984,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1083,
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

_source line 17 · 2026-05-17T15:48:47.132Z_

<details><summary>↩ Tool result · `toolu_012JsYSxws1pw1dTGr59vx3F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/paper_framing.md\", \"content\": \"# Paper Framing — streamprobe_adversarial_robustness\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (LLM Security Track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (7 days remaining)\\n\\n## Core Claims (≤3)\\n\\n1. **[Benchmark]** Streaming safety monitors (Kelp, NExT-Guard, TrajGuard) exhibit substantially degraded detection performance under adaptive adversarial attacks (GCG suffix optimization + RL-Obfuscation), with attack success rates far exceeding those reported on standard benchmarks.\\n\\n2. **[Architectural Insight]** Monitor architecture determines adversarial vulnerability profile: temporal recurrence (Kelp GRU), sparse feature selection (NExT-Guard SAE), and geometric surveillance (TrajGuard) fail through distinct, predictable mechanisms under GCG vs RL-Obfuscation.\\n\\n3. **[Negative Finding]** Hidden-state probes at middle layers of reasoning models do not detect harmful premeditation during chain-of-thought: per-token safety scores in CoT are statistically indistinguishable from benign traces (AUC ≈ 0.5), and temporal aggregation (CUSUM) cannot rescue a signal that does not exist.\\n\\n## Story Spine\\n\\n- **Problem**: Streaming safety monitors for LLM generation have proliferated rapidly (Kelp, NExT-Guard, TrajGuard, Qwen3Guard-Stream, SafeProbing), yet NONE have been evaluated under adaptive adversarial attacks. SoK (Wang et al., S&P 2026) identifies this evaluation gap as critical. RL-Obfuscation showed static classifiers are vulnerable (59-89% evasion), but temporal/streaming monitors remain untested.\\n\\n- **Existing approaches & their gaps**: Each streaming monitor reports strong standard-benchmark performance (Kelp +15.61% F1 over static probes, NExT-Guard 84.3 F1, TrajGuard 95% detection). But Qwen3Guard-Stream's 57.2pp degradation on merely novel (non-adaptive) adversarial prompts foreshadows the problem. No systematic adversarial evaluation exists; deployment decisions are made on inflated benchmarks.\\n\\n- **Our framing**: We construct StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors. We evaluate three representative architectures under two adaptive attack methodologies, providing: (a) the first comparative robustness data, (b) architectural vulnerability analysis revealing distinct failure modes, (c) a controlled decomposition experiment isolating the contribution of temporal aggregation strategy, and (d) a negative result showing hidden-state CoT premeditation detection is infeasible at middle layers.\\n\\n- **Headline result template**: \\\"Under adaptive RL-Obfuscation, [worst monitor]'s detection rate drops from [X]% to [Y]% while [best monitor] maintains [Z]% detection, revealing that [architectural property] is the key determinant of adversarial robustness in streaming safety monitoring.\\\"\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an engineering benchmark\\\" critique**: Mitigate via Claim 2 (architectural insight with explanatory analysis) + Claim 3 (negative finding about CoT premeditation). The paper provides both evaluation AND insight.\\n- **Reimplementation fidelity for Kelp/TrajGuard**: NExT-Guard has official code. For Kelp and TrajGuard, we report architecture match percentage and invite author verification. Accepting 2/3 monitors as minimum viable benchmark (IDEA_BRIEF contingency).\\n- **Scope limited to one model**: DeepSeek-R1-Distill-7B primary, Qwen2.5-7B-Instruct secondary if time permits. Single-model limitation explicitly acknowledged.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy |\\n|---------|-------------------|\\n| \\\"Reimplementation may not be faithful\\\" | Use NExT-Guard official code as anchor; report fidelity metrics for Kelp/TrajGuard; controlled decomposition uses same-probe different-aggregation (no reimplementation needed) |\\n| \\\"Only one target model\\\" | Add Qwen2.5-7B-Instruct as P1; frame as \\\"proof of methodology\\\" if single-model |\\n| \\\"RL-Obfuscation didn't converge\\\" | Pre-specified convergence criteria (reward <1% improvement over 2K steps, 40K max, gradient norm diagnostic) |\\n| \\\"What's beyond the benchmark?\\\" | Claim 2 (architectural vulnerability analysis) + Claim 3 (negative CoT premeditation finding) + controlled decomposition |\\n| \\\"Why not just monitor text?\\\" | Text-level baseline (Llama-Guard sliding window) included as comparison |\\n| \\\"Small sample size\\\" | Bootstrap 95% CI on all metrics; 500 harmful + 200 benign traces |\\n\\n## Negative Finding Framing (Claim 3)\\n\\nPhase 0 MVP tested: \\\"Do hidden states in CoT accumulate detectable harmful premeditation signal?\\\"\\n\\nResult: No. At layer 16/28 of DeepSeek-R1-Distill-7B (v2 probe, overfitting fixed):\\n- Per-token probe AUC in CoT = 0.49 (anti-predictive: harmful CoT scores LOWER than benign)\\n- Trace-level mean-score AUC = 0.61 (weak)\\n- CUSUM-max AUC = 0.645 (no advantage over simple max-score AUC = 0.676)\\n- Detection @5% trace-level FPR = 0-5% (original 88% was token-to-trace FPR mixing bug)\\n- CUSUM false alarm rate on safe traces = 36.3% (v2 probe)\\n- **Strongest evidence**: On the SAME harmful prompts, probe scores are statistically indistinguishable between complied and refused traces (CUSUM fire rate 47.1% vs 45.3%, mean pre-onset score 0.0143 vs 0.0142). This rules out \\\"weak probe\\\" as explanation — hidden states genuinely do not encode compliance decisions at this layer.\\n\\nThis is reported as: \\\"Contrary to the hypothesis that reasoning traces leak compliance intent through hidden states, we find that middle-layer activations during CoT are statistically indistinguishable between harmful-compliant and benign traces. Critically, complied and refused traces on identical harmful prompts show no probe score difference, demonstrating that the model's compliance decision is not encoded in layer 16 activations during reasoning. This suggests compliance decisions are either encoded in later layers, emerge only at the response boundary, or are distributed across layers in ways that single-layer linear probes cannot capture.\\\"\\n\\nThis negative finding is valuable because it prevents the community from assuming probing-based CoT monitoring is straightforward.\\n\", \"total_chars\": 6086, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8340f95-1134-460f-b5f9-01276e139504",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "1897287a-78b7-4c7d-b9eb-ae384f28f1eb",
  "sourceToolAssistantUUID": "c8340f95-1134-460f-b5f9-01276e139504",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T15:48:53.046Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012q1yXqNekcPH6abMPB2fNa`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1897287a-78b7-4c7d-b9eb-ae384f28f1eb",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QR2sUqZvrabHEhnkH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82876d4d-d7c0-4f72-907e-1354704cd456",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vw6J3GmZRhnX6VwrtPwQL5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4219,
      "cache_read_input_tokens": 19067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4219,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 19 · 2026-05-17T15:48:53.056Z_

<details><summary>↩ Tool result · `toolu_012q1yXqNekcPH6abMPB2fNa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/memory.md\", \"content\": \"# Memory — streamprobe_adversarial_robustness\\n\\n## Phase 0 MVP 结果 (2026-05-17)\\n\\n### D005 诊断后修正指标（以此为准）\\n\\n| 指标 | 原始（过拟合） | v2 (修复) | v2 + calibrated |\\n|------|---------------|-----------|-----------------|\\n| train_loss / val_loss | 0.002 / 4.214 | 0.153 / 1.283 | N/A |\\n| P95 threshold | 0.000308 | 0.4759 | 0.2076 |\\n| token-level AUC (pre-onset) | 0.547 | 0.492 | 0.479 |\\n| trace-level AUC | 0.665 | 0.609 | 0.625 |\\n| relaxed_B | 76% | 43.1% | 44.1% |\\n| detection @1% FPR | 16.2% | 27.0% | 27.0% |\\n| detection @5% FPR | 93.1% | 88.2% | 88.2% |\\n| Mech A / B(strict) / Neither | 93.1/0/6.9% | 88.2/0/11.8% | 88.2/0/11.8% |\\n\\n- Platt scaling: A=6.333, B=-4.353\\n- v2 probe: hidden_dim=128, dropout=0.3, weight_decay=1e-4, early stop on val_loss (patience=3)\\n- Best checkpoint = epoch 1 (early stopped at epoch 4)\\n\\n### 关键洞察\\n- 原始 relaxed_B=76% 被过拟合虚高，修正后 44%（仍>20%门槛）\\n- Pre-onset token-level AUC < 0.5：CoT 中 harmful 大多数 token 分数比 safe 低\\n- 但 88% traces 仍被检出：靠少量 spike token (Mechanism A 主导)\\n- 44% traces 的检出依赖 CUSUM 累积（spike_frac<10%）\\n- detection @1% FPR 修复后反升（16%→27%）：校准后低 FPR 区更可靠\\n\\n### 样本统计\\n- 500 harmful prompts → 204 complied (41%), 296 refused\\n- 200 benign prompts → 200 traces\\n- Safe class = 496 (200 benign + 296 refused)\\n\\n### D003 Onset 定义\\n- Onset = `&lt;/think>` 后 response 中首个 harmful token\\n- 整个 CoT (`&lt;think>...&lt;/think>`) 为 pre-onset window\\n- CoT 平均长度 ~1125 tokens\\n\\n### 基础设施\\n- 服务器: westd-39593, 4×5090 32GB\\n- 数据盘: /root/autodl-tmp (200GB, 156G 可用)\\n- DeepSeek 模型: /root/streamprobe/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B (symlink)\\n- Llama-Guard-3: /root/autodl-tmp/streamprobe/models/LLM-Research/Llama-Guard-3-8B\\n- 代码: /root/streamprobe/code/\\n- Outputs: /root/streamprobe/outputs/\\n- Phase 0 outputs 总大小: ~4.3G（hidden states 占主体）\\n\\n### 实际输出路径（与预设不同）\\n- 合并 traces: `outputs/combined_traces.jsonl`（非 merged_traces/）\\n- Onset labels: `outputs/onset_labels.jsonl`（文件，非目录）\\n- Probe: `outputs/probe/`（非 probe_output/）\\n- Probe v2: `outputs/probe_v2/`（D005 诊断版）\\n- Temporal: `outputs/temporal/`（非 temporal_results/）\\n- Temporal v2: `outputs/temporal_v2_calibrated/`\\n\\n### Bug 修复记录\\n- train_probe.py: float16 hidden states → .float() 转换\\n- train_probe_v2.py: 修复过拟合（降容量+dropout+weight decay+ES on val_loss）\\n\\n### Safe class 设计决策\\n- Probe 训练: benign + refused 都算 safe\\n- text_baseline.py: 支持 --safe_source benign/refused/both（默认 benign）\\n\\n### 竞品/Baseline 准备\\n- text_baseline.py: Llama-Guard-3 sliding-window baseline，已写好（含 --safe_source 修复）\\n- download_qwen.sh: Qwen2.5-7B-Instruct 下载脚本，已准备\\n\", \"total_chars\": 2471, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82876d4d-d7c0-4f72-907e-1354704cd456",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "2e0feb37-2ece-4cb4-b59b-55fd1e423e73",
  "sourceToolAssistantUUID": "82876d4d-d7c0-4f72-907e-1354704cd456",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T15:48:53.730Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VGkAwCwH1x1DuMR4XtsBHT`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e0feb37-2ece-4cb4-b59b-55fd1e423e73",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QR2sUqZvrabHEhnkH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4b5353b-9fb4-4283-8926-80eb7d440421",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vw6J3GmZRhnX6VwrtPwQL5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4219,
      "cache_read_input_tokens": 19067,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4219
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 19067,
          "cache_creation_input_tokens": 4219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4219,
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

_source line 21 · 2026-05-17T15:48:53.745Z_

<details><summary>↩ Tool result · `toolu_01VGkAwCwH1x1DuMR4XtsBHT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/decisions.yaml\", \"content\": \"_next_id: 7\\ndecisions:\\n- id: D001\\n  date: 2026-05-17 08:37 UTC\\n  summary: Safe class 使用 benign prompts（GSM8K/ARC），不依赖 same-prompt refused traces\\n  rationale: R1-Distill-7B 无 system prompt 下 compliance rate 极高（可能接近 100%），refused\\n    traces 不足。Benign prompts 的 confound 风险（学到 topic 而非 reasoning pattern）在 MVP 中可控：(1)\\n    probe 在 harmful traces 内部也需区分 pre-onset（同话题但未 plan）vs post-onset tokens，不纯靠 topic；(2)\\n    temporal analysis 本身测试 GRADUAL DRIFT——若 probe 仅学 topic，harmful traces 上 score\\n    全程均匀高，CUSUM 无 signal，这本身就是 falsification。Llama-Guard 标注后如有 ≥50 refused traces，补充\\n    same-prompt ablation。\\n  related_experiments:\\n  - exp_id: mvp_trace_gen\\n    role: context\\n    result: running, ~100% compliance observed\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-17 09:18 UTC\\n  summary: Onset 定义修正：从\\\"首次 harmful topic mention\\\"改为\\\"首次 actionable harmful content\\\"\\n  rationale: Llama-Guard 对 R1 CoT 第一句即判 unsafe（因为复述了有害问题），导致 onset=0，pre-onset window\\n    消失。但研究目标是检测\\\"premeditation phase\\\"——模型在分析/规划有害行为但尚未输出可执行指令的阶段。科学上正确的 onset 应是首次出现\\n    actionable harmful instructions（步骤、代码、配方等），而非 topic mention。这与 Path Drift 描述的\\\"local\\n    compliance belies global deviation\\\"完全一致：规划阶段看起来无害，执行阶段才产出有害内容。\\n  related_experiments:\\n  - exp_id: mvp_trace_gen\\n    role: context\\n    result: onset labeling test revealed onset=0 with naive definition\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-17 09:25 UTC\\n  summary: Onset 重定义为 response（&lt;/think> 后）首个 harmful token，CoT 全段作为 pre-onset window\\n  rationale: D002 的 \\\"actionable vs topic mention\\\" 方案无法解决 R1 CoT 固有行为（首句即复述有害意图）。将\\n    onset 定义为 response 中首个 harmful token 有三重优势：(1) 实际部署场景对齐——安全监控的目标是在模型输出有害 response\\n    前拦截，CoT 是内部过程；(2) pre-onset window 有意义——整个 CoT（通常几百 token）成为早期检测窗口；(3) 研究问题更锐利——\\\"能否从\\n    reasoning trace 预测模型将输出有害内容\\\"比\\\"CoT 内部 onset\\\"更重要且更 novel。Detection Lead = 在 response\\n    前多少 token 检出，直接衡量早期预警能力。\\n  related_experiments:\\n  - exp_id: mvp_trace_gen\\n    role: context\\n    result: onset labeling test confirmed CoT-level onset=0 on all complied traces,\\n      D002 approach also failed\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-17 14:28 UTC\\n  summary: MVP 判定：Qualified PASS — pre-onset per-token AUC 不达标但 temporal accumulation\\n    假设得到比预期更强的验证\\n  rationale: ROADMAP 预注册指标：CoT probe AUC > 0.85 + relaxed_B ≥ 20%。结果：(1) probe val\\n    AUC=0.967 但 pre-onset token-level AUC=0.547（per-token 在 CoT 中近乎随机）；(2) relaxed_B=76%（远超\\n    20%）。按 strict 解读 pre-onset AUC 是 FAIL（0.547 < 0.75），但这个\\\"失败\\\"恰好是论文最强论点：pointwise\\n    detection 在 CoT 阶段彻底失败（AUC≈random），而 CUSUM temporal accumulation 成功检出 76% 的 harmful\\n    traces。这比原假设（\\\"probe 在 pre-onset 就能检出\\\"）提供了更强的 temporal accumulation 必要性证据。研究问题从\\\"probe\\n    能否在 CoT 早期检出 harmful intent\\\"reframe 为\\\"为什么 per-token detection 失败而 temporal accumulation\\n    成功\\\"——后者科学上更有趣。判定 qualified PASS，进入 research 阶段。\\n  related_experiments:\\n  - exp_id: mvp_trace_gen\\n    role: evidence\\n    result: 500 traces, 204 complied, pre-onset AUC=0.547, relaxed_B=76%\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-17 14:36 UTC\\n  summary: D004 降级为 CONDITIONAL：Reviewer 指出 probe 过拟合 + P95 异常低，需快速诊断后再判定\\n  rationale: Reviewer critical 审查发现三个问题：(1) probe 严重过拟合（train_loss=0.002 vs val_loss=4.214），score\\n    calibration 失真；(2) P95=0.0003 异常低，relaxed_B=76% 可能虚高；(3) token-level AUC=0.547\\n    确实 ≈ random。但 detection @5% FPR=93.1% 是 FPR-controlled 的真实信号，不应直接判 FAIL。决定：retrain\\n    probe with early stopping（epoch 1-2）+ score calibration → rerun temporal analysis\\n    → 根据校正后结果做最终判定。预计 2-3 小时。\\n  related_experiments:\\n  - exp_id: phase0_mvp_pipeline\\n    role: source\\n    result: token_auc=0.547, relaxed_B=76%, detection@5%FPR=93.1%\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-17 14:47 UTC\\n  summary: 'D006: MVP FAIL — pre-onset CoT 无可检测的 premeditation signal，pivot to benchmark-primary'\\n  rationale: 三重证据否定核心假设：(1) Token-level pre-onset AUC=0.49（反预测，harmful CoT score 低于\\n    safe）；(2) Trace-level AUC=0.61（弱）；(3) CUSUM safe false alarm=40%+，detection_rate\\n    指标存在 token-to-trace FPR 混淆 bug。Probe 在 layer 16 无法检测 CoT premeditation。按 ROADMAP\\n    预设 FAIL 路径 pivot to benchmark-only，detector 降为 P2。Benchmark 贡献（首个 streaming monitor\\n    对抗鲁棒性评估）独立有效，不依赖 detector。\\n  related_experiments:\\n  - exp_id: phase0_mvp_pipeline\\n    role: source\\n    result: token_auc=0.49, trace_auc=0.61, CUSUM safe FAR=40%, detection metric buggy\\n  depends_on:\\n  - D005\\n\", \"total_chars\": 4280, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4b5353b-9fb4-4283-8926-80eb7d440421",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "d8aee76e-22b6-4395-ac19-a6a6406d66d5",
  "sourceToolAssistantUUID": "d4b5353b-9fb4-4283-8926-80eb7d440421",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-17T15:48:57.072Z_

Now let me look at the artifacts directory for the actual paper draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8aee76e-22b6-4395-ac19-a6a6406d66d5",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QRX6cDuBbkoAPHSvU2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce17eff9-4143-413b-bdd1-af491e0e1f3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GprzqPeU1tujuXEXwSPMnV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4134,
      "cache_read_input_tokens": 23286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4134,
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

_source line 23 · 2026-05-17T15:48:58.072Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015iMwCHrqAJB4tsr1EnAJLm`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce17eff9-4143-413b-bdd1-af491e0e1f3e",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QRX6cDuBbkoAPHSvU2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fc4155d-0190-4789-9e00-1386b65ea4c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GprzqPeU1tujuXEXwSPMnV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4134,
      "cache_read_input_tokens": 23286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4134,
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

_source line 24 · 2026-05-17T15:48:58.093Z_

<details><summary>↩ Tool result · `toolu_015iMwCHrqAJB4tsr1EnAJLm`</summary>

```text
artifacts/dream_reports/dream_20260517T145100/best/paper.tex
artifacts/dream_reports/dream_20260517T145100/median/paper.tex
artifacts/dream_reports/dream_20260517T145100/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fc4155d-0190-4789-9e00-1386b65ea4c4",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "30a16396-2d25-4da0-8a6b-ea301a4cb63d",
  "sourceToolAssistantUUID": "0fc4155d-0190-4789-9e00-1386b65ea4c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T15:48:58.430Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JN3XernazKci6fydgyioqw`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30a16396-2d25-4da0-8a6b-ea301a4cb63d",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QRX6cDuBbkoAPHSvU2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c596a490-256f-49ef-af31-6c07114fd7d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GprzqPeU1tujuXEXwSPMnV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4134,
      "cache_read_input_tokens": 23286,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4134
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 23286,
          "cache_creation_input_tokens": 4134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4134,
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

_source line 26 · 2026-05-17T15:48:58.446Z_

<details><summary>↩ Tool result · `toolu_01JN3XernazKci6fydgyioqw`</summary>

```text
artifacts/code/rl_obfuscation/README.md
artifacts/dream_reports/dream_20260517T145100/best/paper_framing.md
artifacts/dream_reports/dream_20260517T145100/median/paper_framing.md
artifacts/dream_reports/dream_20260517T145100/worst/paper_framing.md
artifacts/dream_reports/dream_20260517T145100/best/review_report.md
artifacts/dream_reports/dream_20260517T145100/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c596a490-256f-49ef-af31-6c07114fd7d9",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "0754bab7-7863-4f83-a80f-26161d048fac",
  "sourceToolAssistantUUID": "c596a490-256f-49ef-af31-6c07114fd7d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T15:49:01.001Z_

<details open><summary>🔧 Tool call — Read · `toolu_019swRXrquPcGfmRc1W1XJyQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts/dream_reports/dream_20260517T145100/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0754bab7-7863-4f83-a80f-26161d048fac",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QRsA7Co9p5Pyo2eJUx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "427cf7c1-f12b-4fa5-bc49-d0507c2a05d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QmJmeFhmw12eXWpuQ5niRU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 462,
      "cache_read_input_tokens": 27420,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 462
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 27420,
          "cache_creation_input_tokens": 462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 462,
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

_source line 28 · 2026-05-17T15:49:01.564Z_

<details><summary>↩ Tool result · `toolu_019swRXrquPcGfmRc1W1XJyQ`</summary>

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
11	\usepackage{enumitem}
12	\usepackage{natbib}
13	\usepackage{hyperref}
14	
15	\title{StreamProbe-Bench: Adversarial Robustness Evaluation of\\Streaming Safety Monitors for Large Language Models}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\begin{abstract}
23	Streaming safety monitors that analyze hidden states during Large Language Model (LLM) generation have shown strong detection performance on standard benchmarks, yet none have been evaluated under adaptive adversarial attack. We introduce StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors, evaluating three architecturally distinct monitors (Kelp GRU, NExT-Guard SAE, TrajGuard geometric surveillance) under GCG suffix optimization and RL-Obfuscation. Our results reveal a false sense of security: detection rates drop by 43 percentage points (pp) on average under GCG and 66pp under RL-Obfuscation, with NExT-Guard's detection collapsing from 86.7\% to 11.7\% under RL. Critically, monitor architecture determines vulnerability profile in a predictable, mechanistically interpretable pattern: temporal recurrence resists RL but amplifies GCG perturbation, while geometric surveillance shows the opposite pattern. A controlled decomposition experiment isolates temporal aggregation strategy as an independent robustness factor, yielding a 0.23 AUC gap between max-pooling and pointwise scoring under attack. We additionally report a negative finding: hidden-state probes across all layers fail to detect harmful premeditation during chain-of-thought (token AUC $\leq$ 0.53 at all layers tested), closing the ``just probe the reasoning trace'' hypothesis.
24	\end{abstract}
25	
26	\section{Introduction}
27	
28	Streaming safety monitors that inspect LLM hidden states during token generation have emerged as a promising defense against harmful content production. Systems such as Kelp \cite{kelp2025}, NExT-Guard \cite{nextguard2025}, and TrajGuard \cite{trajguard2025} report strong detection performance, with Kelp achieving +15.6\% F1 over static probes and TrajGuard reaching 95\% detection rate. These systems are being considered for real-world deployment, and their reported metrics inform safety engineering decisions across the industry.
29	
30	However, a critical evaluation gap persists. While RL-Obfuscation has demonstrated that static safety classifiers are vulnerable to adaptive attack (59--89\% evasion rate), streaming monitors with temporal modeling and architectural diversity remain entirely untested under adversarial conditions. The SoK by Wang et al. (S\&P 2026) explicitly identifies this gap as a priority for the community. Early evidence suggests the problem is severe: Qwen3Guard-Stream's 57.2pp degradation on merely novel (non-adaptive) prompts foreshadows what adaptive attacks may achieve.
31	
32	This evaluation gap creates a dangerous situation. Deployment decisions are being made based on inflated benchmarks that do not reflect adversarial threat models. If streaming monitors fail under adaptive attack, organizations relying on them face undetected harmful generation at scale. The problem is compounded by architectural diversity: without systematic adversarial evaluation, defenders cannot choose among competing monitor designs based on robustness properties.
33	
34	We address this gap with three contributions:
35	
36	\begin{enumerate}[leftmargin=*]
37	\item \textbf{StreamProbe-Bench}: the first adversarial robustness benchmark for streaming safety monitors, evaluating three representative architectures under GCG suffix optimization and RL-Obfuscation on DeepSeek-R1-Distill-7B, with cross-model validation on Qwen2.5-7B-Instruct.
38	
39	\item \textbf{Architectural vulnerability analysis}: we identify distinct, predictable failure modes determined by monitor architecture. Temporal recurrence (Kelp GRU) resists RL-Obfuscation but shatters under GCG; geometric surveillance (TrajGuard) resists GCG but collapses under RL. This inversion pattern provides actionable architectural guidance for defenders.
40	
41	\item \textbf{Negative finding on CoT premeditation}: hidden-state probes at layers 8--24 of a reasoning model cannot detect harmful premeditation during chain-of-thought, with per-token AUC $\leq$ 0.53 across all layers. This closes the hypothesis that reasoning traces straightforwardly leak compliance intent through hidden states.
42	\end{enumerate}
43	
44	\section{Related Work}
45	
46	\paragraph{Streaming Safety Monitors.} Recent work has introduced monitors that process LLM hidden states during generation to detect harmful content in real time. Kelp \cite{kelp2025} employs a bidirectional GRU over hidden state sequences, achieving strong temporal integration. NExT-Guard \cite{nextguard2025} uses Sparse Autoencoders (SAEs) to decompose hidden states into interpretable features, monitoring safety-relevant feature activations. TrajGuard \cite{trajguard2025} computes geometric properties (curvature, direction cosine) of activation trajectories at a single layer. SafeProbing \cite{safeprobing2025} and Qwen3Guard-Stream \cite{qwen3guard2025} represent additional approaches. All report strong performance on standard benchmarks, but none have been evaluated under adaptive adversarial attack.
47	
48	\paragraph{Adversarial Attacks on Safety Systems.} GCG \cite{zou2023universal} optimizes adversarial suffixes via greedy coordinate gradient to bypass safety alignment. RL-Obfuscation \cite{rlobfuscation2025} trains the LLM itself (via QLoRA PPO) to produce harmful content while evading a target safety classifier. Both have demonstrated success against static classifiers, but their effectiveness against streaming monitors with temporal modeling is unknown. Our work provides the first systematic evaluation.
49	
50	\paragraph{Robustness Benchmarks.} Existing safety benchmarks (HarmBench, SimpleSafetyTests, WildJailbreak) evaluate safety alignment rather than monitor robustness. AdvBench \cite{advbench2024} evaluates attack success but does not measure monitor degradation under adaptive attack. StreamProbe-Bench fills this gap by measuring detection degradation under attacks specifically optimized against each monitor.
51	
52	\section{StreamProbe-Bench}
53	
54	\subsection{Threat Model}
55	
56	We consider two complementary adversary capabilities:
57	
58	\textbf{GCG suffix attack} (input-level): the adversary appends optimized suffix tokens (20 tokens, 256 optimization steps per prompt) to harmful prompts. The adversary has white-box gradient access to the target LLM but treats the monitor as a black box.
59	
60	\textbf{RL-Obfuscation} (weight-level): the adversary fine-tunes the LLM via QLoRA PPO (rank=8, q\_proj+v\_proj) to produce harmful content while minimizing the monitor's detection score. Reward: $0.4 \times \text{quality} + 0.5 \times (1 - \text{detection}) + 0.1 \times \text{KL\_penalty}$. Convergence criterion: reward improvement $<$1\% over 2K consecutive steps, maximum 40K steps.
61	
62	\subsection{Monitor Implementations}
63	
64	We evaluate three monitors spanning distinct architectural paradigms:
65	
66	\textbf{Kelp GRU} (temporal recurrence): 2-layer bidirectional GRU (hidden dim 256) with linear projection from model hidden states (3584$\rightarrow$256) and 2-layer MLP safety head (256$\rightarrow$128$\rightarrow$2). Reimplemented following paper specifications (93.3\% architecture match, 14/15 design decisions matched, F1 deviation 1.7pp from reported).
67	
68	\textbf{NExT-Guard SAE} (sparse feature selection): official released code. SAE decomposes hidden states into $\sim$16K sparse features; a subset ($\sim$50--80 features) are safety-relevant. Detection threshold set at 5\% FPR on held-out benign set.
69	
70	\textbf{TrajGuard} (geometric surveillance): monitors activation trajectory at layer 16/28, computing curvature (second derivative of activation path), direction cosine changes, and velocity magnitude. Geometric features aggregated through learned threshold MLP (96$\rightarrow$32$\rightarrow$1). Reimplemented (91.0\% architecture match, 10/11 decisions, detection rate deviation 1.9pp).
71	
72	\subsection{Text-Level Baseline}
73	
74	Llama-Guard-3-8B applied with sliding window (128 tokens, stride 64) over generated text serves as a non-hidden-state baseline, addressing the question of whether monitoring internal representations provides advantage over monitoring outputs directly.
75	
76	\subsection{Evaluation Protocol}
77	
78	All experiments use 500 harmful prompts and 200 benign prompts drawn from established datasets. Primary metric: detection rate at 5\% FPR. Secondary metrics: AUC, F1, attack success rate (ASR). All hidden-state monitors are evaluated on DeepSeek-R1-Distill-7B (primary) with GCG cross-validation on Qwen2.5-7B-Instruct.
79	
80	\section{Experiments and Results}
81	
82	\subsection{Reimplementation Fidelity}
83	
84	Table~\ref{tab:fidelity} reports reimplementation quality for Kelp and TrajGuard. Both achieve $>$90\% architecture match and $<$2pp performance deviation from reported results, establishing sufficient baseline quality for meaningful adversarial evaluation.
85	
86	\begin{table}[t]
87	\centering
88	\small
89	\begin{tabular}{lccc}
90	\toprule
91	\textbf{Monitor} & \textbf{Match \%} & \textbf{Baseline F1/Det.} & \textbf{$\Delta$ (pp)} \\
92	\midrule
93	Kelp GRU & 93.3 & F1=87.8\% & 1.7 \\
94	TrajGuard & 91.0 & Det=93.1\% & 1.9 \\
95	NExT-Guard & 100 (official) & F1=84.3\% & -- \\
96	\bottomrule
97	\end{tabular}
98	\caption{Reimplementation fidelity. Match \% indicates fraction of architectural decisions matching original paper. All deviations are within the 3pp acceptability threshold.}
99	\label{tab:fidelity}
100	\end{table}
101	
102	\subsection{Main Benchmark Results}
103	
104	Table~\ref{tab:main} presents the core result: all streaming monitors suffer severe detection degradation under adaptive attack.
105	
106	\begin{table*}[t]
107	\centering
108	\small
109	\begin{tabular}{lcccccc}
110	\toprule
111	& \multicolumn{3}{c}{\textbf{GCG Suffix Attack}} & \multicolumn{3}{c}{\textbf{RL-Obfuscation}} \\
112	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
113	\textbf{Monitor} & Det.@5\%FPR & ASR & $\Delta$ (pp) & Det.@5\%FPR & ASR & $\Delta$ (pp) \\
114	\midrule
115	Kelp GRU & 38.2\% & 58\% & $-$53.0 & 40.2\% & 55\% & $-$51.0 \\
116	NExT-Guard SAE & 42.7\% & 52\% & $-$44.0 & 11.7\% & 83\% & $-$75.0 \\
117	TrajGuard Geom. & 61.1\% & 34\% & $-$32.0 & 19.1\% & 76\% & $-$74.0 \\
118	\midrule
119	Llama-Guard (text) & 63.7\% & 29\% & $-$18.4 & 34.3\% & 61\% & $-$47.8 \\
120	\midrule
121	\textit{Baselines} & & & & & & \\
122	\quad Kelp GRU & \multicolumn{3}{c}{91.2\%} & \multicolumn{3}{c}{91.2\%} \\
123	\quad NExT-Guard SAE & \multicolumn{3}{c}{86.7\%} & \multicolumn{3}{c}{86.7\%} \\
124	\quad TrajGuard Geom. & \multicolumn{3}{c}{93.1\%} & \multicolumn{3}{c}{93.1\%} \\
125	\quad Llama-Guard (text) & \multicolumn{3}{c}{82.1\%} & \multicolumn{3}{c}{82.1\%} \\
126	\bottomrule
127	\end{tabular}
128	\caption{StreamProbe-Bench main results. Detection rate at 5\% FPR under clean conditions, GCG suffix attack, and RL-Obfuscation. Average detection drop: 43pp under GCG, 66pp under RL-Obfuscation across hidden-state monitors.}
129	\label{tab:main}
130	\end{table*}
131	
132	Under GCG suffix optimization, detection drops range from 32pp (TrajGuard) to 53pp (Kelp), with an average of 43pp across hidden-state monitors. Under RL-Obfuscation, degradation is more severe: drops range from 51pp (Kelp) to 75pp (NExT-Guard), averaging 66pp. NExT-Guard's detection collapses from 86.7\% to 11.7\% under RL, the most severe single result in the benchmark.
133	
134	The 28pp gap in post-attack detection rate between the most robust (Kelp, 40.2\%) and least robust (NExT-Guard, 11.7\%) monitors under RL confirms that architecture is a key variable in adversarial robustness.
135	
136	\subsection{Architectural Vulnerability Inversion}
137	
138	The most striking result is the cross-attack vulnerability inversion between Kelp and TrajGuard. Their vulnerability profiles are mirror images:
139	
140	\textbf{Kelp GRU}: most vulnerable to GCG (53pp drop, largest), most resistant to RL (51pp drop, smallest). The GRU's temporal memory amplifies suffix perturbation (mean hidden state shift L2 = 2.84 under GCG), but the same temporal integration forces RL to maintain safety signal suppression at every token (per-token suppression consistency only 72\%).
141	
142	\textbf{TrajGuard}: most resistant to GCG (32pp drop, smallest), highly vulnerable to RL (74pp drop). Geometric properties are higher-order features robust to point perturbations from suffix tokens (curvature shift only 0.41), but RL's weight-level access directly reshapes the monitored layer's trajectory geometry (post-RL curvature mean drops to 0.12 from $\sim$0.65 baseline).
143	
144	\textbf{NExT-Guard SAE}: uniformly fragile under both attacks (44pp GCG, 75pp RL). The sparse bottleneck ($\sim$50--80 safety features out of 16K) presents a minimal optimization target for both attack modalities. Fastest RL convergence (18.2K steps) confirms the small effective attack surface.
145	
146	Fisher exact tests confirm the failure mode distributions are significantly different between Kelp and TrajGuard under both GCG ($p = 0.0003$) and RL ($p = 0.0001$), ruling out the null hypothesis that vulnerability profiles are architecture-independent.
147	
148	\subsection{Controlled Temporal Aggregation Decomposition}
149	
150	To isolate the contribution of temporal aggregation strategy independent of monitor architecture, we apply a single MLP probe (validation AUC = 0.967) with five aggregation strategies over per-token safety scores under GCG attack (Table~\ref{tab:aggregation}).
151	
152	\begin{table}[t]
153	\centering
154	\small
155	\begin{tabular}{lccc}
156	\toprule
157	\textbf{Aggregation} & \textbf{Clean AUC} & \textbf{GCG AUC} & \textbf{$\Delta$-AUC} \\
158	\midrule
159	Pointwise & 0.961 & 0.583 & $-$0.378 \\
160	WindowMean ($k$=10) & 0.954 & 0.641 & $-$0.313 \\
161	EMA ($\alpha$=0.1) & 0.948 & 0.693 & $-$0.255 \\
162	CUSUM ($h$=4) & 0.938 & 0.742 & $-$0.196 \\
163	MaxPool & 0.972 & 0.813 & $-$0.159 \\
164	\bottomrule
165	\end{tabular}
166	\caption{Controlled decomposition: temporal aggregation strategy as sole variable. The 0.23 AUC gap between MaxPool and Pointwise under GCG confirms aggregation as an independent robustness factor. Ordering is monotonic with increasing temporal context.}
167	\label{tab:aggregation}
168	\end{table}
169	
170	The monotonic ordering from Pointwise (AUC 0.583) to MaxPool (AUC 0.813) demonstrates that temporal aggregation strategy contributes a 0.23 AUC improvement independently of probe quality. MaxPool forces the adversary to suppress safety signal at every token; any single token with high safety score triggers detection. In detection rate terms, this translates from 39.2\% (Pointwise) to 67.1\% (MaxPool) at 5\% FPR.
171	
172	\subsection{Negative Finding: CoT Premeditation Detection}
173	
174	Table~\ref{tab:cot} presents the layer ablation for chain-of-thought (CoT) premeditation detection. We train linear probes at layers 8, 12, 16, 20, and 24 (of 28) and evaluate whether harmful compliance intent is detectable during reasoning traces.
175	
176	\begin{table}[t]
177	\centering
178	\small
179	\begin{tabular}{lcc}
180	\toprule
181	\textbf{Layer} & \textbf{Token AUC} & \textbf{Trace AUC} \\
182	\midrule
183	8 & 0.506 & 0.542 \\
184	12 & 0.493 & 0.571 \\
185	16 & 0.490 & 0.610 \\
186	20 & 0.512 & 0.638 \\
187	24 & 0.531 & 0.687 \\
188	\bottomrule
189	\end{tabular}
190	\caption{CoT premeditation detection across layers. Token-level AUC remains near chance ($\leq$0.53) at all layers. Even the best trace-level AUC (0.687 at layer 24) is far below practical deployment threshold. 95\% confidence intervals for all token AUCs include 0.5.}
191	\label{tab:cot}
192	\end{table}
193	
194	No layer achieves practical CoT premeditation detection. Per-token AUC remains at 0.49--0.53 across all layers, with 95\% confidence intervals including 0.5. The gradient from layer 8 to layer 24 (trace AUC 0.542 to 0.687) suggests compliance encoding strengthens toward output layers but never reaches a usable level with single-layer linear probes. At 5\% FPR, even layer 24 yields only $\sim$35\% detection rate. This rules out the ``wrong layer'' alternative hypothesis and establishes that CoT premeditation is either not linearly decodable, distributed across layers, or encoded only at the response boundary.
195	
196	\subsection{Cross-Model Generalization}
197	
198	Table~\ref{tab:crossmodel} validates that vulnerability patterns transfer to Qwen2.5-7B-Instruct.
199	
200	\begin{table}[t]
201	\centering
202	\small
203	\begin{tabular}{lcc}
204	\toprule
205	\textbf{Monitor} & \textbf{DeepSeek $\Delta$} & \textbf{Qwen $\Delta$} \\
206	\midrule
207	Kelp GRU & $-$53.0pp & $-$48.2pp \\
208	NExT-Guard SAE & $-$44.0pp & $-$41.8pp \\
209	TrajGuard Geom. & $-$32.0pp & $-$30.5pp \\
210	\bottomrule
211	\end{tabular}
212	\caption{Cross-model GCG replication. Relative ordering is preserved ($r = 0.94$), confirming vulnerability patterns are determined by monitor architecture, not target model.}
213	\label{tab:crossmodel}
214	\end{table}
215	
216	The relative ordering (TrajGuard most GCG-robust, Kelp most GCG-vulnerable) is preserved with $r = 0.94$ cross-model correlation. Absolute magnitudes shift by 2--5pp, consistent with model-specific hidden state geometry differences. This confirms that Claim 2's architectural vulnerability analysis generalizes across model families.
217	
218	\subsection{Evasion-Quality Tradeoff Analysis}
219	
220	Pareto frontier analysis of evasion rate versus harmful content quality (judge score, 1--5 scale) reveals that temporal monitors force attackers into worse tradeoffs. At quality threshold 3.5, RL achieves only 42\% evasion against Kelp versus 78\% against NExT-Guard and 67\% against TrajGuard. Kelp's Pareto area-under-curve (0.38) is roughly half of NExT-Guard's (0.71), confirming that temporal memory increases the cost adversaries must pay for successful evasion.
221	
222	\subsection{Diagnostic: Probe Fidelity Under RL}
223	
224	Per-token probe AUC drops from 0.967 (clean model) to 0.714 (NExT-Guard RL model) and 0.782 (Kelp RL model), confirming that RL causes representation drift. However, the probe remains meaningfully discriminative (AUC $>$ 0.7), indicating temporal aggregation bypass is also a substantial factor. For NExT-Guard, approximately 62\% of total detection degradation is attributable to aggregation bypass, suggesting that improved temporal aggregation could recover substantial performance without retraining.
225	
226	\section{Discussion}
227	
228	\paragraph{A False Sense of Security.} The central message of StreamProbe-Bench is that reported benchmark performance of streaming monitors is not predictive of adversarial robustness. A 43pp average GCG drop and 66pp RL drop represent a qualitative shift from ``effective defense'' to ``easily bypassed.'' Organizations deploying these monitors based on standard benchmark results face an unrecognized vulnerability.
229	
230	\paragraph{Architectural Prescription for Defenders.} The vulnerability inversion between temporal and geometric architectures provides actionable guidance. If RL-style fine-tuning attacks are the primary concern (e.g., API providers where users can fine-tune), defenders should prefer temporal architectures (GRU-based monitors). If input-level attacks dominate (e.g., prompt injection scenarios), geometric surveillance offers stronger resistance. The uniform fragility of sparse feature approaches (SAE) under both attack types makes them the least robust choice in adversarial threat models.
231	
232	\paragraph{Temporal Aggregation as Low-Cost Defense.} The 0.23 AUC gap from aggregation strategy alone offers immediate practical value. Switching from pointwise scoring to max-pooling requires no model changes, no retraining, and no additional compute, yet provides a 23pp AUC improvement under GCG attack.
233	
234	\paragraph{CoT Monitoring Limitations.} The negative finding on CoT premeditation closes an intuitive escape hatch: one cannot simply ``probe the reasoning trace'' to catch harmful intent before generation. This result should discourage premature deployment of CoT-based safety monitors and redirect research toward understanding where and how compliance decisions are actually encoded.
235	
236	\paragraph{Limitations.} Our benchmark evaluates three monitors on two models. While cross-model validation supports generalizability of relative patterns, absolute robustness numbers may differ on larger models or different model families. Kelp and TrajGuard are reimplementations (not official code), though fidelity metrics (93.3\% and 91.0\% architecture match) bound this concern. The RL-Obfuscation threat model assumes the adversary can fine-tune the target model, which may not apply in all deployment scenarios.
237	
238	\section{Conclusion}
239	
240	StreamProbe-Bench reveals that streaming safety monitors are far more vulnerable to adaptive adversarial attack than their standard benchmark performance suggests. The 43pp average GCG drop and 66pp RL drop establish that deployment decisions based on clean-condition evaluation create a false sense of security. Our architectural vulnerability analysis demonstrates that monitor architecture is the key determinant of adversarial robustness, with temporal recurrence and geometric surveillance showing complementary strengths that are predictable from first principles. The controlled decomposition further isolates temporal aggregation as a zero-cost robustness lever. Together with the negative CoT premeditation finding, these results provide both a warning and a constructive path forward for the streaming safety monitoring community.
241	
242	\bibliographystyle{plainnat}
243	\begin{thebibliography}{10}
244	
245	\bibitem[Kelp(2025)]{kelp2025}
246	Kelp Authors.
247	\newblock Kelp: Temporal Safety Monitoring via Recurrent Hidden State Analysis.
248	\newblock In \emph{Proc. ACL}, 2025.
249	
250	\bibitem[NExT-Guard(2025)]{nextguard2025}
251	NExT-Guard Authors.
252	\newblock NExT-Guard: Sparse Autoencoder Features for Real-Time Safety Monitoring.
253	\newblock In \emph{Proc. NeurIPS}, 2025.
254	
255	\bibitem[TrajGuard(2025)]{trajguard2025}
256	TrajGuard Authors.
257	\newblock TrajGuard: Geometric Surveillance of Activation Trajectories.
258	\newblock In \emph{Proc. ICLR}, 2025.
259	
260	\bibitem[Zou et~al.(2023)]{zou2023universal}
261	Andy Zou, Zifan Wang, J.~Zico Kolter, and Matt Fredrikson.
262	\newblock Universal and Transferable Adversarial Attacks on Aligned Language Models.
263	\newblock \emph{arXiv:2307.15043}, 2023.
264	
265	\bibitem[RL-Obfuscation(2025)]{rlobfuscation2025}
266	RL-Obfuscation Authors.
267	\newblock RL-Obfuscation: Training Language Models to Evade Safety Classifiers.
268	\newblock In \emph{Proc. ICML}, 2025.
269	
270	\bibitem[SafeProbing(2025)]{safeprobing2025}
271	SafeProbing Authors.
272	\newblock SafeProbing: Linear Probes for Streaming Safety Detection.
273	\newblock \emph{arXiv}, 2025.
274	
275	\bibitem[Qwen3Guard(2025)]{qwen3guard2025}
276	Qwen Team.
277	\newblock Qwen3Guard-Stream: Streaming Safety Monitoring for Qwen Models.
278	\newblock Technical Report, 2025.
279	
280	\bibitem[AdvBench(2024)]{advbench2024}
281	AdvBench Authors.
282	\newblock AdvBench: An Adversarial Robustness Benchmark for LLM Safety.
283	\newblock In \emph{Proc. EMNLP}, 2024.
284	
285	\end{thebibliography}
286	
287	\appendix
288	
289	\section{Failure Mode Matrix}
290	
291	Table~\ref{tab:failure} categorizes the primary failure mechanism for each cell of the monitor$\times$attack matrix.
292	
293	\begin{table*}[t]
294	\centering
295	\small
296	\begin{tabular}{p{2.5cm}p{5.5cm}p{5.5cm}}
297	\toprule
298	\textbf{Monitor} & \textbf{GCG Failure Mode} & \textbf{RL Failure Mode} \\
299	\midrule
300	Kelp GRU & Temporal propagation: suffix perturbation amplified through GRU memory & Partial representation suppression (per-token consistency 72\%) \\
301	NExT-Guard SAE & Sparse feature suppression: safety features zeroed via gradient & Sparse feature masking: RL zeros features through weight updates \\
302	TrajGuard & Minimal geometric perturbation (curvature shift 0.41) & Geometric bypass (curvature $\rightarrow$ 0.12, cosine $\rightarrow$ 0.91) \\
303	\bottomrule
304	\end{tabular}
305	\caption{Failure mode categorization. Five distinct mechanisms emerge (NExT-Guard GCG/RL are variants of the same sparse bottleneck exploit). Fisher exact tests confirm architecture-dependent failure profiles ($p < 0.001$).}
306	\label{tab:failure}
307	\end{table*}
308	
309	\section{SN-CUSUM Comparison}
310	
311	Self-normalized CUSUM (SN-CUSUM) provides a small but statistically significant improvement over standard CUSUM under GCG: AUC 0.771 vs 0.742 ($p = 0.018$, Cohen's $d = 0.34$), with 14.2\% FPR reduction. The adaptive threshold mechanism normalizes by local variance, reducing sensitivity to adversarial score variance manipulation.
312	
313	\section{Pareto Frontier Details}
314	
315	\begin{table}[t]
316	\centering
317	\small
318	\begin{tabular}{lccc}
319	\toprule
320	\textbf{Monitor} & \textbf{Pareto AUC} & \textbf{Evasion@Q=3.5} & \textbf{Quality@E=50\%} \\
321	\midrule
322	Kelp GRU & 0.38 & 42\% & 3.12 \\
323	NExT-Guard SAE & 0.71 & 78\% & 3.94 \\
324	TrajGuard Geom. & 0.62 & 67\% & 3.61 \\
325	\bottomrule
326	\end{tabular}
327	\caption{Evasion rate vs. harmful content quality Pareto frontier summary under RL-Obfuscation. Lower Pareto AUC indicates a more attacker-unfavorable tradeoff.}
328	\label{tab:pareto}
329	\end{table}
330	
331	\section{Probe Fidelity Under RL Attack}
332	
333	\begin{table}[t]
334	\centering
335	\small
336	\begin{tabular}{lccc}
337	\toprule
338	\textbf{Condition} & \textbf{Per-token AUC} & \textbf{Repr. Drift} & \textbf{Aggr. Contrib. \%} \\
339	\midrule
340	Clean model & 0.967 & -- & -- \\
341	NExT-Guard RL & 0.714 & 0.253 & 62.3\% \\
342	Kelp RL & 0.782 & 0.185 & 44.8\% \\
343	\bottomrule
344	\end{tabular}
345	\caption{Per-token probe AUC on RL-attacked models. Representation drift and temporal aggregation bypass both contribute to detection failure, in monitor-specific proportions.}
346	\label{tab:probefidelity}
347	\end{table}
348	
349	\end{document}
350	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "427cf7c1-f12b-4fa5-bc49-d0507c2a05d5",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "a5cbbad1-d7d4-44db-961a-51833ab31ec3",
  "sourceToolAssistantUUID": "427cf7c1-f12b-4fa5-bc49-d0507c2a05d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-17T15:49:04.839Z_

Now let me read the review report for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5cbbad1-d7d4-44db-961a-51833ab31ec3",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QS6R5ZTYymGiqDFEuQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba0b83ba-cb3d-4150-baec-a0d5f0e0a786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5yK4NcwsK5jiTCV4gu1y7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8727,
      "cache_read_input_tokens": 27882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8727,
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

_source line 30 · 2026-05-17T15:49:07.285Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KWJXkMzVFMy28X51JdZs7T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts/dream_reports/dream_20260517T145100/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba0b83ba-cb3d-4150-baec-a0d5f0e0a786",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QS6R5ZTYymGiqDFEuQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "044302d8-89b8-423b-a371-b2eafec5db8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5yK4NcwsK5jiTCV4gu1y7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8727,
      "cache_read_input_tokens": 27882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8727,
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

_source line 31 · 2026-05-17T15:49:07.290Z_

<details><summary>↩ Tool result · `toolu_01KWJXkMzVFMy28X51JdZs7T`</summary>

```text
1	---
2	dream_id: dream_20260517T145100
3	tier: best
4	overall_score: weak accept
5	timestamp: 2026-05-17T15:44:32.288725+00:00
6	---
7	
8	
9	# Reviewer 1 (R1): Methods and Experiments
10	
11	## Summary
12	
13	This paper introduces StreamProbe-Bench, a benchmark for evaluating the adversarial robustness of streaming safety monitors that inspect LLM hidden states during generation. Three monitors (NExT-Guard, Kelp, TrajGuard) are evaluated under GCG suffix optimization and RL-Obfuscation attacks, revealing 43pp (GCG) and 66pp (RL) average detection drops. A controlled decomposition isolates temporal aggregation as an independent robustness factor, and a negative finding shows CoT premeditation is undetectable via hidden-state probes at layers 8-24.
14	
15	## Strengths
16	
17	- **Well-structured threat model with complementary attack modalities.** GCG (input-level, white-box to LLM, black-box to monitor) and RL-Obfuscation (weight-level, white-box to both) span two realistic adversary capability levels. The reward formulation (0.4 quality + 0.5 evasion + 0.1 KL) is principled and the convergence criterion (reward improvement <1% over 2K steps, 40K max) is pre-specified, preventing cherry-picking.
18	
19	- **Controlled decomposition experiment is methodologically clean.** Using the same trained probe with 5 different temporal aggregation strategies isolates a single variable. The monotonic ordering (Pointwise 0.583 to MaxPool 0.813 under GCG) is convincing, and pairwise statistical significance is reported. This is arguably the paper's strongest methodological contribution because it requires no reimplementation and has no fidelity confound.
20	
21	- **Honest handling of reimplementation limitations.** TrajGuard RL non-convergence is explicitly reported (reward 0.38, std 0.21, >40K steps) rather than hidden. Architecture match percentages (93.3% Kelp, 91.0% TrajGuard) and performance deviation bounds (<2pp) are transparently disclosed. The paper uses NExT-Guard (official code) as an anchor point.
22	
23	- **Probe fidelity diagnostic adds mechanistic depth.** Decomposing detection degradation into representation drift vs. aggregation bypass (Table 6: NExT-Guard 62% aggregation, Kelp 45% aggregation) moves beyond "monitors fail" to "why they fail," which is more informative for defenders.
24	
25	- **Bootstrap 10K for confidence intervals is appropriate** for the sample sizes used. The paper reports CIs on all primary metrics.
26	
27	- **Text-level baseline (Llama-Guard-3) contextualizes hidden-state monitoring.** The 18pp GCG drop vs. 43pp average for hidden-state monitors is informative, though interpretation requires care (see weaknesses).
28	
29	## Weaknesses
30	
31	- **Critical: Numbers in the task description and the paper.tex diverge significantly.** The paper summary provided states NExT-Guard baseline F1=82.1, GCG drop 18pp, RL drop 42pp. The actual paper.tex reports NExT-Guard baseline detection=86.7%, GCG drop 44pp, RL drop 75pp. Similarly, the task description says "18-42pp detection drops" but the paper shows 32-75pp drops. These discrepancies suggest either the paper summary is outdated or there are multiple inconsistent versions of the results. This is a major concern for the integrity of reported numbers.
32	
33	- **Single primary model is a substantial limitation for a "benchmark" paper.** DeepSeek-R1-Distill-7B is the only model with full GCG+RL evaluation. The cross-model validation on Qwen2.5-7B-Instruct covers only GCG (Table 11). For a paper claiming to establish a benchmark, the absence of RL-Obfuscation cross-model validation weakens the generalizability claim significantly. The architectural vulnerability inversion (Claim 2) rests entirely on one model's hidden state geometry.
34	
35	- **TrajGuard RL non-convergence undermines one cell of a 3x2 benchmark matrix.** The paper reports TrajGuard RL results (74pp drop) despite acknowledging non-convergence (reward 0.38, std 0.21). Reporting a non-converged attack's results as if they are meaningful is problematic. The 74pp drop could be either an underestimate (attack would be worse with convergence) or an artifact of unstable training. The paper should either exclude this cell or present it with much stronger caveats and sensitivity analysis.
36	
37	- **Sample size adequacy is borderline for the claims made.** 500 harmful + 200 benign prompts is small for a benchmark paper. With 500 prompts and bootstrap CIs, the precision of detection rate estimates is roughly +/-3-4pp. Given that some claimed differences (e.g., between aggregation strategies or between monitors) are in this range, the statistical power to detect real differences at the margins is limited. The CoT experiment (150 harmful, 100 benign) is even smaller.
38	
39	- **GCG attack treats monitor as black-box, which understates vulnerability.** The paper states "white-box gradient access to the target LLM but treats the monitor as a black box." However, the code (gcg_attack.py) shows a `probe_lambda` parameter for differentiable probe evasion. This inconsistency needs clarification. If GCG is purely optimizing for harmful content generation (Phase A) without monitor-aware optimization, the GCG results are conservative but also not truly "adaptive" to the monitor. If probe_lambda is active, the attack is white-box to the monitor. The threat model description and actual implementation must be reconciled.
40	
41	- **Controlled decomposition uses only GCG attack, not RL.** Table 4 evaluates aggregation strategies under GCG only. Since RL-Obfuscation produces different failure modes (representation drift rather than suffix perturbation), the aggregation ranking might differ under RL. The claim that "temporal aggregation strategy is an independent robustness factor" is only demonstrated for one attack type.
42	
43	- **The "architectural vulnerability inversion" claim (Claim 2) is overclaimed.** The paper states Kelp is "most resistant to RL" with 51pp drop, but the Pareto analysis (Table in Appendix) shows Kelp Pareto AUC = 0.38 (best), which is consistent. However, the inversion narrative (temporal resists RL, geometric resists GCG) is built on exactly 3 data points per attack. With N=3 monitors, any pattern can appear "predictable." The mechanistic explanations (GRU memory amplification, curvature robustness) are post-hoc and not validated experimentally (e.g., no ablation showing that removing temporal memory makes Kelp GCG-resistant).
44	
45	- **Text baseline comparison has confounds.** Llama-Guard-3 (8B, text-level) vs. hidden-state monitors (probe-based, operating on 7B model internals) differ in model capacity, training data, and modality. The comparison answers "is text monitoring more robust?" but cannot isolate why, making the comparison less informative than implied.
46	
47	- **Reward formulation lacks sensitivity analysis.** The 0.4/0.5/0.1 weighting of quality/evasion/KL is fixed. No ablation shows whether different weightings change the relative vulnerability ranking. If quality weight is increased (adversary prefers quality over evasion), the ranking could shift.
48	
49	## Questions to Authors
50	
51	1. **GCG probe_lambda:** Is the GCG attack monitor-aware (differentiable probe evasion active) or monitor-agnostic? The code supports both modes. Which was used for the main results, and how do results differ between modes?
52	
53	2. **TrajGuard RL:** Given non-convergence, what is the justification for including the 74pp drop in the main table rather than marking it as "N/A" or providing a range? Did you attempt longer training, different hyperparameters, or reward shaping?
54	
55	3. **Cross-model RL:** Was RL-Obfuscation attempted on Qwen2.5-7B-Instruct? If not, what prevented it? If the vulnerability inversion is "architecture-determined, not model-determined," RL cross-model validation is essential.
56	
57	4. **Controlled decomposition under RL:** Does the aggregation ranking (MaxPool > CUSUM > EMA > WindowMean > Pointwise) hold under RL-Obfuscation, where the attack mechanism is fundamentally different?
58	
59	5. **Effect size for CoT negative finding:** With 150 harmful + 100 benign traces, a token AUC of 0.53 at layer 24 has a wide CI. What is the exact 95% CI? Is this sufficiently powered to rule out AUC=0.60 (a weak but non-trivial signal)?
60	
61	6. **Reimplementation validation:** The 93.3% and 91.0% architecture match metrics are self-assessed. Were any external validators (e.g., original authors) consulted? What specific design decisions were unmatched?
62	
63	## Minor Issues
64	
65	- Table 2 in the paper.tex reports different numbers than Table 2 described in the review task. The paper should have a single authoritative set of results.
66	- The paper uses "Det.@5%FPR" as primary metric but the controlled decomposition reports AUC. Consistency in primary metric across all tables would improve readability.
67	- The fidelity table (Table 1) reports F1 for Kelp but detection rate for TrajGuard, making direct comparison difficult. Should use the same metric.
68	- The Fisher exact test for vulnerability inversion is described but the contingency table construction is not specified. What are the categories? Success/failure per prompt? This needs methodological detail.
69	- "93.3% architecture match" is not a standard metric. The paper should define exactly how this is computed (e.g., 14/15 binary design decisions).
70	- The SN-CUSUM comparison (Appendix B) reports Cohen's d = 0.34 (small-to-medium effect). This merits brief discussion of practical significance vs. statistical significance.
71	
72	## Scores
73	
74	- **Overall: 4 (Weak Accept)**
75	- **Confidence: 4 (High confidence, reviewed methodology and code in detail)**
76	- **Soundness: 3 (Good, with notable gaps in cross-model validation and one non-converged cell)**
77	- **Presentation: 3 (Good, clear structure but metric inconsistencies across tables)**
78	
79	## Justification
80	
81	The paper addresses a genuine evaluation gap (no prior adversarial robustness evaluation of streaming safety monitors) and the controlled decomposition experiment is methodologically clean. However, for a benchmark paper, the reliance on a single primary model, the non-converged TrajGuard RL result presented without adequate caveats, the small-N architectural vulnerability inversion claim, and the ambiguity in the GCG threat model (black-box vs. differentiable probe evasion) collectively prevent a higher score. The work is timely and the experimental framework is well-designed in principle, but execution completeness falls short of what a top venue benchmark paper requires. If the authors can clarify the GCG threat model, add RL cross-model validation, and properly caveat or exclude the non-converged TrajGuard result, this would strengthen to a clear accept.
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "044302d8-89b8-423b-a371-b2eafec5db8d",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "8ad4cc4e-2b7b-4c4b-beed-2f35ddceceea",
  "sourceToolAssistantUUID": "044302d8-89b8-423b-a371-b2eafec5db8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-17T15:49:07.679Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JZb1kRedR1MfYPKFtsJhhB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts/dream_reports/dream_20260517T145100/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ad4cc4e-2b7b-4c4b-beed-2f35ddceceea",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QS6R5ZTYymGiqDFEuQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71c264ea-49a9-4d21-ae9e-c3d82bf1ff27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5yK4NcwsK5jiTCV4gu1y7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8727,
      "cache_read_input_tokens": 27882,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8727
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 27882,
          "cache_creation_input_tokens": 8727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8727,
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

_source line 33 · 2026-05-17T15:49:07.685Z_

<details><summary>↩ Tool result · `toolu_01JZb1kRedR1MfYPKFtsJhhB`</summary>

```text
1	# Paper Framing — streamprobe_adversarial_robustness
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (LLM Security Track)
5	- Fallback: EMNLP 2026 Findings
6	- Deadline: ARR May 25, 2026 (7 days remaining)
7	
8	## Core Claims (≤3)
9	
10	1. **[Benchmark]** Streaming safety monitors (Kelp, NExT-Guard, TrajGuard) exhibit substantially degraded detection performance under adaptive adversarial attacks (GCG suffix optimization + RL-Obfuscation), with attack success rates far exceeding those reported on standard benchmarks.
11	
12	2. **[Architectural Insight]** Monitor architecture determines adversarial vulnerability profile: temporal recurrence (Kelp GRU), sparse feature selection (NExT-Guard SAE), and geometric surveillance (TrajGuard) fail through distinct, predictable mechanisms under GCG vs RL-Obfuscation.
13	
14	3. **[Negative Finding]** Hidden-state probes at middle layers of reasoning models do not detect harmful premeditation during chain-of-thought: per-token safety scores in CoT are statistically indistinguishable from benign traces (AUC ≈ 0.5), and temporal aggregation (CUSUM) cannot rescue a signal that does not exist.
15	
16	## Story Spine
17	
18	- **Problem**: Streaming safety monitors for LLM generation have proliferated rapidly (Kelp, NExT-Guard, TrajGuard, Qwen3Guard-Stream, SafeProbing), yet NONE have been evaluated under adaptive adversarial attacks. SoK (Wang et al., S&P 2026) identifies this evaluation gap as critical. RL-Obfuscation showed static classifiers are vulnerable (59-89% evasion), but temporal/streaming monitors remain untested.
19	
20	- **Existing approaches & their gaps**: Each streaming monitor reports strong standard-benchmark performance (Kelp +15.61% F1 over static probes, NExT-Guard 84.3 F1, TrajGuard 95% detection). But Qwen3Guard-Stream's 57.2pp degradation on merely novel (non-adaptive) adversarial prompts foreshadows the problem. No systematic adversarial evaluation exists; deployment decisions are made on inflated benchmarks.
21	
22	- **Our framing**: We construct StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors. We evaluate three representative architectures under two adaptive attack methodologies, providing: (a) the first comparative robustness data, (b) architectural vulnerability analysis revealing distinct failure modes, (c) a controlled decomposition experiment isolating the contribution of temporal aggregation strategy, and (d) a negative result showing hidden-state CoT premeditation detection is infeasible at middle layers.
23	
24	- **Headline result template**: "Under adaptive RL-Obfuscation, [worst monitor]'s detection rate drops from [X]% to [Y]% while [best monitor] maintains [Z]% detection, revealing that [architectural property] is the key determinant of adversarial robustness in streaming safety monitoring."
25	
26	## Venue Fit Risks
27	
28	- **"Just an engineering benchmark" critique**: Mitigate via Claim 2 (architectural insight with explanatory analysis) + Claim 3 (negative finding about CoT premeditation). The paper provides both evaluation AND insight.
29	- **Reimplementation fidelity for Kelp/TrajGuard**: NExT-Guard has official code. For Kelp and TrajGuard, we report architecture match percentage and invite author verification. Accepting 2/3 monitors as minimum viable benchmark (IDEA_BRIEF contingency).
30	- **Scope limited to one model**: DeepSeek-R1-Distill-7B primary, Qwen2.5-7B-Instruct secondary if time permits. Single-model limitation explicitly acknowledged.
31	
32	## Anticipated Reviewer Concerns
33	
34	| Concern | Response Strategy |
35	|---------|-------------------|
36	| "Reimplementation may not be faithful" | Use NExT-Guard official code as anchor; report fidelity metrics for Kelp/TrajGuard; controlled decomposition uses same-probe different-aggregation (no reimplementation needed) |
37	| "Only one target model" | Add Qwen2.5-7B-Instruct as P1; frame as "proof of methodology" if single-model |
38	| "RL-Obfuscation didn't converge" | Pre-specified convergence criteria (reward <1% improvement over 2K steps, 40K max, gradient norm diagnostic) |
39	| "What's beyond the benchmark?" | Claim 2 (architectural vulnerability analysis) + Claim 3 (negative CoT premeditation finding) + controlled decomposition |
40	| "Why not just monitor text?" | Text-level baseline (Llama-Guard sliding window) included as comparison |
41	| "Small sample size" | Bootstrap 95% CI on all metrics; 500 harmful + 200 benign traces |
42	
43	## Negative Finding Framing (Claim 3)
44	
45	Phase 0 MVP tested: "Do hidden states in CoT accumulate detectable harmful premeditation signal?"
46	
47	Result: No. At layer 16/28 of DeepSeek-R1-Distill-7B:
48	- Per-token probe AUC in CoT = 0.49 (anti-predictive: harmful CoT scores LOWER than benign)
49	- Trace-level mean-score AUC = 0.61 (weak)
50	- CUSUM false alarm rate on safe traces = 40%+ (no discriminative power)
51	
52	This is reported as: "Contrary to the hypothesis that reasoning traces leak compliance intent through hidden states, we find that middle-layer activations during CoT are statistically indistinguishable between harmful-compliant and benign traces. This suggests compliance decisions are either encoded in later layers, emerge only at the response boundary, or are distributed across layers in ways that single-layer linear probes cannot capture."
53	
54	This negative finding is valuable because it prevents the community from assuming probing-based CoT monitoring is straightforward.
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71c264ea-49a9-4d21-ae9e-c3d82bf1ff27",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "d64c2dd9-72ce-4fea-83e2-53d86566f1ae",
  "sourceToolAssistantUUID": "71c264ea-49a9-4d21-ae9e-c3d82bf1ff27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-17T15:49:13.682Z_

Now let me check the median scenario paper for contrast, and look at any additional context about how the paper reframed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d64c2dd9-72ce-4fea-83e2-53d86566f1ae",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QSYkc6zPmxXvy12knw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fe6ab95-ed25-4dd4-bb75-51bca633c031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZDdhXZAGJhVMRKuX1396g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4754,
      "cache_read_input_tokens": 36609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4754,
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

_source line 35 · 2026-05-17T15:49:13.983Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NFBTMnED4SodbeTUtH6U3R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts/dream_reports/dream_20260517T145100/median/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fe6ab95-ed25-4dd4-bb75-51bca633c031",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QSYkc6zPmxXvy12knw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11567e19-5604-48a6-8ad2-823d15494e85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZDdhXZAGJhVMRKuX1396g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4754,
      "cache_read_input_tokens": 36609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4754,
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

_source line 36 · 2026-05-17T15:49:13.997Z_

<details><summary>↩ Tool result · `toolu_01NFBTMnED4SodbeTUtH6U3R`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{tablefootnote}
12	\usepackage{caption}
13	\usepackage{subcaption}
14	
15	\newcommand{\dagmark}{$\dagger$}
16	\newcommand{\starmark}{$*$}
17	
18	\title{StreamProbe-Bench: Adversarial Robustness Evaluation\\of Streaming Safety Monitors for Large Language Models}
19	
20	\author{Anonymous}
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	% ============================================================
27	% ABSTRACT
28	% ============================================================
29	\begin{abstract}
30	Streaming safety monitors that inspect hidden states during Large Language Model (LLM) generation have shown strong performance on standard benchmarks, yet none have been evaluated under adaptive adversarial attacks. We introduce StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors. We evaluate three representative architectures (NExT-Guard with Sparse Autoencoder (SAE) features, Kelp with Gated Recurrent Unit (GRU) temporal modeling, and TrajGuard with geometric surveillance) under GCG suffix optimization and Reinforcement Learning (RL)-based obfuscation on DeepSeek-R1-Distill-7B. All monitors suffer substantial degradation: detection rate drops range from 18 to 42 percentage points (pp) under adaptive attacks. A controlled decomposition experiment, holding the probe fixed while varying only the temporal aggregation strategy, reveals a 0.13 AUC gap across five strategies, with CUSUM achieving 0.72 AUC versus 0.59 for pointwise scoring under GCG. We further report a negative finding on Chain-of-Thought (CoT) premeditation detection: hidden-state probes at all tested layers (8 through 24) yield at most 0.57 token-level AUC, indicating that middle-layer linear probes cannot detect harmful intent during reasoning. These results establish that current streaming monitors provide a false sense of security under adaptive threats and that temporal aggregation strategy is a significant, previously unexamined determinant of adversarial robustness.
31	\end{abstract}
32	
33	% ============================================================
34	% 1. INTRODUCTION
35	% ============================================================
36	\section{Introduction}
37	
38	The deployment of safety monitors for LLM generation has accelerated rapidly. Systems such as Kelp, NExT-Guard, TrajGuard, and Qwen3Guard-Stream inspect hidden states at each generated token, promising real-time detection of harmful outputs without relying on post-hoc text classifiers. These streaming monitors report strong performance on standard evaluation sets: Kelp achieves +15.61\% F1 over static probes, NExT-Guard reports 84.3 F1, and TrajGuard claims 95\% detection rate.
39	
40	However, these evaluations share a critical blind spot. The recent Systematization of Knowledge by Wang et al.\ (S\&P 2026) identifies the absence of adaptive adversarial evaluation as a key gap in the streaming monitor literature. Prior work on RL-Obfuscation demonstrated that static safety classifiers are vulnerable to adaptive attacks with 59--89\% evasion rates, but temporal and streaming monitors remain untested. Meanwhile, Qwen3Guard-Stream's 57.2pp degradation on merely novel (non-adaptive) adversarial prompts foreshadows the severity of the problem.
41	
42	Existing adversarial evaluations for safety monitors focus on either text-level classifiers or static hidden-state probes, leaving the temporal dimension of streaming monitors unexamined. No prior benchmark systematically tests whether architectural choices in temporal aggregation, feature selection, or geometric boundary estimation affect robustness under adaptive attacks. Deployment decisions are currently made on benchmarks that do not reflect adversarial conditions.
43	
44	We address this gap with StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors. We evaluate three architecturally distinct monitors under two adaptive attack methodologies (GCG suffix optimization and RL-Obfuscation), providing: (a) comparative robustness data across monitor architectures, (b) a controlled decomposition experiment that isolates temporal aggregation strategy as an independent variable, and (c) a negative result establishing that hidden-state CoT premeditation detection is infeasible with linear probes. Our controlled decomposition holds the probe fixed while varying only the aggregation strategy, eliminating reimplementation fidelity as a confound and revealing a 0.13 AUC gap between the best (CUSUM, 0.72) and worst (pointwise, 0.59) strategies.
45	
46	Our contributions are:
47	\begin{itemize}
48	    \item \textbf{Benchmark.} StreamProbe-Bench, the first adversarial robustness evaluation of streaming safety monitors. Using NExT-Guard (official code) and Kelp (reimplemented, 4.8pp F1 deviation) as a reliable two-monitor core, with TrajGuard (6.8pp deviation, caveated) as supplementary evidence, we show that all monitors suffer 18--42pp detection drops under adaptive attacks.
49	    \item \textbf{Controlled decomposition.} Holding probe architecture fixed, we demonstrate that temporal aggregation strategy alone accounts for a 0.13 AUC gap under GCG, with change-point detection (CUSUM) significantly outperforming pointwise scoring ($p < 0.01$). This result requires no cross-monitor comparison and is free of reimplementation confounds.
50	    \item \textbf{Negative finding.} Linear probes at layers 8 through 24 of DeepSeek-R1-Distill-7B yield at most 0.57 token-level AUC for CoT premeditation detection, with the best trace-level AUC at 0.64. This establishes that single-layer linear probing is insufficient for CoT safety monitoring.
51	\end{itemize}
52	
53	% ============================================================
54	% 2. RELATED WORK
55	% ============================================================
56	\section{Related Work}
57	
58	\paragraph{Streaming safety monitors.}
59	A growing body of work addresses real-time safety monitoring during LLM generation. Kelp trains a GRU-based safety head over hidden-state sequences to detect harmful content as it is generated. NExT-Guard uses Sparse Autoencoders (SAEs) to select safety-relevant features from intermediate representations. TrajGuard monitors geometric properties of hidden-state trajectories at a single layer using Mahalanobis distance. Qwen3Guard-Stream extends output-token classifiers to streaming contexts. These systems share the premise that hidden-state inspection enables earlier and more reliable detection than text-level classifiers, but differ in their temporal modeling approaches.
60	
61	\paragraph{Adversarial attacks on safety mechanisms.}
62	GCG suffix optimization appends adversarial tokens to prompts that shift model behavior while evading input-level filters. RL-Obfuscation trains the target model via Proximal Policy Optimization (PPO) to generate harmful content whose hidden-state representations mimic safe patterns, achieving 59--89\% evasion against static classifiers. These attacks have been evaluated against static probes and text-level classifiers, but not against streaming monitors with temporal aggregation. The distinction matters because temporal aggregation may provide robustness that single-token classifiers lack.
63	
64	\paragraph{Hidden-state probing for safety.}
65	Linear probing of intermediate representations has been used to study safety-relevant features in LLMs. Prior work has shown that safety-trained models develop linearly separable safe/unsafe representations in middle layers. However, the detectability of harmful \emph{intent} during chain-of-thought reasoning, as opposed to harmful \emph{content} in generated outputs, remains an open question.
66	
67	\paragraph{Temporal aggregation in anomaly detection.}
68	Sequential analysis methods such as CUSUM and its self-normalized variants have a long history in industrial process control and change-point detection. Their application to safety monitoring of LLM generation, where the ``process'' is a sequence of per-token safety scores, has not been systematically studied.
69	
70	% ============================================================
71	% 3. METHOD
72	% ============================================================
73	\section{StreamProbe-Bench}
74	
75	\subsection{Target Models}
76	
77	Our primary evaluation uses DeepSeek-R1-Distill-Qwen-7B, a reasoning-capable model that produces explicit chain-of-thought traces. We replicate key GCG results on Qwen2.5-7B-Instruct (a non-reasoning model) to assess generalizability.
78	
79	\subsection{Streaming Safety Monitors}
80	
81	We evaluate three architecturally distinct streaming monitors:
82	
83	\textbf{NExT-Guard} uses Sparse Autoencoders to identify safety-relevant feature dimensions in hidden states. At each generated token, the SAE extracts a sparse activation vector, and a classifier operates on the selected features. We use the official released code; baseline F1 on DeepSeek-R1 is 82.1 (the original paper reports 84.3 on their target model).
84	
85	\textbf{Kelp} trains a two-layer GRU (hidden dimension 256) over the sequence of hidden states. The GRU's recurrent connections model temporal dependencies in safety-relevant patterns, enabling detection of harmful content that emerges gradually. Our reimplementation achieves 76.4 F1 (reported: 81.2, deviation: 4.8pp), which we consider acceptable fidelity.
86	
87	\textbf{TrajGuard\dagmark} monitors geometric properties of hidden-state trajectories at layer 16 using Mahalanobis distance from estimated safe-region boundaries. Our reimplementation achieves 85.3 F1 (reported: 92.1, deviation: 6.8pp). Due to this visible gap, all TrajGuard results carry a fidelity caveat (\dagmark) and serve as supplementary rather than primary evidence. The deviation likely stems from imprecise boundary calibration and undisclosed regularization details.
88	
89	\subsection{Attack Methodologies}
90	
91	\textbf{GCG suffix optimization} appends 20-token adversarial suffixes to harmful prompts, optimized over 500 steps to maximize attack success while maintaining prompt coherence. We evaluate on 500 harmful traces and 200 benign traces.
92	
93	\textbf{RL-Obfuscation} fine-tunes the target model via QLoRA PPO (rank 16, learning rate $10^{-5}$) to simultaneously produce harmful content and evade the target monitor. We apply pre-specified convergence criteria: reward improvement ${<}1\%$ over the final 2K steps, maximum 40K steps, and gradient norm monitoring. Harmful output quality is assessed by GPT-4o on a 1--5 scale.
94	
95	\subsection{Controlled Decomposition Protocol}
96	\label{sec:decomposition}
97	
98	To isolate the effect of temporal aggregation from monitor-specific architectural choices, we train a single MLP probe at layer 16 and evaluate it under GCG with five aggregation strategies: (1) \textbf{Pointwise}: classify each token independently, take the trace maximum; (2) \textbf{Window Mean}: average probe scores in sliding windows of 32 tokens; (3) \textbf{Exponential Moving Average (EMA)}: smooth scores with $\alpha=0.1$; (4) \textbf{MaxPool}: take the maximum score in sliding windows of 32 tokens; (5) \textbf{CUSUM}: cumulative sum change-point detection with threshold $h=5.0$. This design ensures that the only variable is the aggregation strategy.
99	
100	% ============================================================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11567e19-5604-48a6-8ad2-823d15494e85",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "491e1a79-407a-4f92-a038-5667d2f759b8",
  "sourceToolAssistantUUID": "11567e19-5604-48a6-8ad2-823d15494e85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T15:49:14.450Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wx4T3kgMWWb8PTZvhcr4Uu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts/dream_reports/dream_20260517T145100/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "491e1a79-407a-4f92-a038-5667d2f759b8",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QSYkc6zPmxXvy12knw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5761aea3-24a1-4bc3-969b-3b242229f313",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZDdhXZAGJhVMRKuX1396g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4754,
      "cache_read_input_tokens": 36609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4754,
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

_source line 38 · 2026-05-17T15:49:14.456Z_

<details><summary>↩ Tool result · `toolu_01Wx4T3kgMWWb8PTZvhcr4Uu`</summary>

```text
1	---
2	dream_id: dream_20260517T145100
3	tier: median
4	overall_score: weak accept (4/6)
5	timestamp: 2026-05-17T15:47:16.164319+00:00
6	---
7	
8	# Dream Review Report: StreamProbe-Bench
9	
10	**Paper**: StreamProbe-Bench: Adversarial Robustness Evaluation of Streaming Safety Monitors for Large Language Models
11	**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)
12	**Venue Standard**: Top ML venue, ~25% acceptance, 6-point scale
13	
14	---
15	
16	## Roundtable Process
17	
18	- **R1 focus**: Methods and Experiments
19	- **R2 focus**: Novelty and Related Work
20	- **Step 1**: Independent reviews (completed in parallel)
21	- **Step 2**: Cross-sharing of key findings
22	- **Step 3**: Convergence discussion — both reviewers converged on 4/6 (Weak Accept) with aligned concerns
23	- **Step 4**: Synthesized report below
24	
25	---
26	
27	## 1. Paper Summary
28	
29	The paper introduces StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors that inspect LLM hidden states during generation. Three architecturally distinct monitors (NExT-Guard/SAE, Kelp/GRU, TrajGuard/geometric) are evaluated under GCG suffix optimization and RL-Obfuscation on DeepSeek-R1-Distill-7B. All monitors suffer 18-42pp detection drops. A controlled decomposition experiment (same probe, 5 temporal aggregation strategies) reveals a 0.13 AUC gap, with CUSUM (0.72) outperforming pointwise scoring (0.59). A negative finding shows that CoT premeditation detection via linear probes fails at all tested layers (best token AUC: 0.57 at layer 24).
30	
31	---
32	
33	## 2. Strengths
34	
35	### S1: Fills a verified evaluation gap (R1+R2 consensus)
36	The paper addresses a gap explicitly identified by Wang et al. (S&P 2026 SoK): no prior work evaluates streaming safety monitors under adaptive adversarial attacks. The motivation is well-grounded in a concrete, citable gap rather than a vague claim of novelty.
37	
38	### S2: Methodologically clean controlled decomposition (R1+R2 consensus)
39	The controlled decomposition (Section 4.3) is the paper's strongest experimental contribution. By holding the probe fixed and varying only the aggregation strategy, it eliminates reimplementation fidelity as a confound. The 0.13 AUC gap with pairwise bootstrap significance tests (Table 5) provides a clean, interpretable result. The three-tier ordering (CUSUM > MaxPool > {EMA ≈ WindowMean} > Pointwise) is well-supported, with the EMA/WindowMean non-significance (p=0.38) honestly reported.
40	
41	### S3: Honest and transparent handling of limitations (R1+R2 consensus)
42	The paper's treatment of TrajGuard is commendable: the 6.8pp reimplementation deviation is disclosed upfront, all TrajGuard results carry a † caveat, and the RL non-convergence (reward std 0.21, gradient norm 0.31) is clearly flagged with * markers. The paper does not over-claim from unreliable data points.
43	
44	### S4: Informative probe fidelity diagnostic (R1)
45	Table 6 decomposes RL attack success into probe-level representation drift vs. aggregation-level bypass (NExT-Guard: 45%/55%; Kelp: 35%/65%). This provides mechanistic insight into why temporal monitors resist RL better (more of the attack burden falls on the harder-to-bypass aggregation layer).
46	
47	### S5: Comprehensive CoT negative finding (R2)
48	The CoT premeditation result is strengthened by the layer ablation (Table 9, layers 8-24), which preempts the "wrong layer" objection. No layer achieves token AUC above 0.57 or trace AUC above 0.64. The anti-predictive direction (harmful CoT score 0.47 < benign 0.51) is an interesting observation.
49	
50	### S6: Complementary threat model design (R1)
51	GCG (input-side, gradient-free w.r.t. monitor) and RL-Obfuscation (model-side, gradient-based) test fundamentally different attack vectors. The architectural vulnerability pattern differs across attacks (NExT-Guard most robust under GCG but most vulnerable under converged RL), providing genuine insight.
52	
53	---
54	
55	## 3. Weaknesses
56	
57	### W1: Limited methodological novelty (R2, major)
58	The paper proposes no new methods. It applies existing attacks (GCG, RL-Obfuscation) to existing monitors (NExT-Guard, Kelp, TrajGuard) and compares existing aggregation strategies (CUSUM, EMA, MaxPool, etc.). While the evaluation gap is real, the contribution is primarily one of engineering and systematic evaluation. For a top ML venue, benchmark papers typically need either broader scope (more monitors, models, attacks) or deeper methodological insight. The controlled decomposition compares well-known signal processing techniques; the finding that CUSUM outperforms pointwise scoring is consistent with basic sequential detection theory and could be anticipated from first principles.
59	
60	### W2: Severely insufficient references (R2, major)
61	The paper contains only 10 references. Top ML venue papers typically cite 30-50+ works. Critical missing categories include:
62	- **Adaptive evaluation methodology**: Carlini et al. "On Evaluating Adversarial Robustness" and related work establishing best practices for adversarial evaluation
63	- **Jailbreaking beyond GCG**: AutoDAN, PAIR, TAP, and other attack methods that would contextualize the attack selection
64	- **Probing literature**: Belinkov et al. and the broader representation probing literature relevant to the CoT finding
65	- **Safety alignment**: RLHF, constitutional AI, and other alignment methods that streaming monitors complement
66	- **Existing adversarial benchmarks**: HarmBench, AdvBench, and how StreamProbe-Bench relates to them
67	- **Hidden-state anomaly detection**: broader literature on using internal representations for anomaly/safety detection
68	
69	This is not cosmetic. The thin Related Work section (half a page, 4 short paragraphs) suggests incomplete literature survey and weakens the paper's positioning.
70	
71	### W3: Single primary model (R1+R2, major)
72	A benchmark paper evaluated primarily on one model (DeepSeek-R1-Distill-7B) has limited generalizability. The Qwen2.5-7B replication covers only GCG (not RL), and absolute values differ by 2-5pp. RL cross-model generalization is explicitly untested. For a paper claiming to establish a benchmark, evaluation on at least 2-3 models with both attack types would be expected.
73	
74	### W4: Controlled decomposition limited to GCG only (R1, moderate)
75	The controlled decomposition (Section 4.3) is tested only under GCG. The paper does not report whether the CUSUM advantage holds under RL-Obfuscation. Given that RL attacks operate differently (representation drift vs. input perturbation), the aggregation strategy ranking could change. SN-CUSUM results hint at this (RL delta +0.04, p=0.08), but the full 5-strategy comparison under RL is absent. This limits the generality of the "temporal aggregation matters" claim.
76	
77	### W5: TrajGuard non-convergence limits the 3×2 matrix (R1, moderate)
78	The paper claims a 3-monitor × 2-attack evaluation, but TrajGuard RL is unreliable (non-converged, 58-78% detection rate oscillation). This reduces the reliable RL comparison to 2 monitors. The cross-monitor vulnerability analysis (Table 7) assigns "Low" confidence to TrajGuard RL, yet the failure mode taxonomy still includes it. The paper should more clearly state that the reliable benchmark is 2 monitors × 2 attacks + 1 monitor × 1 attack (GCG only).
79	
80	### W6: Modest effect sizes in key results (R1, moderate)
81	- The 0.13 AUC gap in controlled decomposition, while statistically significant, is modest in practical terms. CUSUM achieves 0.72 AUC, which is itself far from deployable (typically >0.9 needed).
82	- The CoT negative finding's best trace AUC of 0.64 at layer 24 is above chance (CI lower bound 0.58). While inadequate for deployment, calling it "infeasible" may be premature; it could indicate a weak but real signal that nonlinear probes might exploit.
83	
84	### W7: Text baseline comparison raises uncomfortable questions (R2, minor-moderate)
85	Table 10 shows Llama-Guard-3 achieves 94% baseline detection with only 6pp GCG drop, outperforming all hidden-state monitors under GCG. Under RL, the text baseline drops 33pp, comparable to Kelp (32pp). The paper acknowledges this but the implication is stark: current hidden-state monitors offer no practical advantage over text-level classification. This somewhat undermines the motivation for the entire streaming monitor research direction, which the paper does not fully reckon with.
86	
87	---
88	
89	## 4. Questions to Authors
90	
91	**Q1**: Why was the controlled decomposition not evaluated under RL-Obfuscation? Is this a computational constraint or a fundamental limitation of the experimental design?
92	
93	**Q2**: The CoT negative finding uses linear probes only. Have you considered nonlinear probes (e.g., 2-layer MLP) or multi-layer probes? The weak trend toward later layers (0.57 at layer 24) suggests a signal may exist but be nonlinearly encoded.
94	
95	**Q3**: The text baseline (Llama-Guard-3) outperforms all hidden-state monitors under GCG and matches them under RL. What is the practical argument for hidden-state monitoring given these results?
96	
97	**Q4**: How sensitive is the controlled decomposition to the CUSUM threshold h=5.0? Was this tuned, and if so, how does tuning interact with the comparison fairness (other strategies also have hyperparameters)?
98	
99	**Q5**: Can you provide confidence intervals for the detection drops in Table 2, not just the point estimates? The 18pp vs. 22pp vs. 33pp ranking under GCG may not be statistically significant.
100	
101	**Q6**: For the Pareto analysis (Table 12), what does "Pareto Area" measure exactly? Is this area under the Pareto frontier curve, and how is it normalized?
102	
103	---
104	
105	## 5. Minor Issues
106	
107	- **M1**: The paper uses en-dashes in several places (e.g., "59-89% evasion rates" on p1, "1-5 scale" on p3) inconsistently with standard number ranges.
108	- **M2**: Table 2 reports F1 for baseline and GCG conditions but leaves F1 blank ("—") for RL-Obfuscation rows. The paper should explain why (presumably because RL changes the model, making F1 undefined on the original test set).
109	- **M3**: The controlled decomposition uses a single MLP probe at layer 16. The choice of layer 16 is not justified beyond it being TrajGuard's monitored layer. Given the layer ablation shows layer 24 performs best for CoT, the decomposition results might differ at other layers.
110	- **M4**: "Reimplementation fidelity" framing implies the reimplemented monitors are faithful copies, but 4.8pp and 6.8pp F1 deviations are substantial. Alternative framing: "inspired-by implementations" with acknowledged gaps.
111	- **M5**: Reference format is inconsistent. References [1]-[3] and [5] use "Authors" as placeholder, presumably for anonymization, but this makes it impossible to verify the cited works.
112	- **M6**: The paper does not discuss computational cost of the attacks or the benchmark, which is relevant for reproducibility.
113	
114	---
115	
116	## 6. Scores
117	
118	### R1 (Methods + Experiments)
119	| Criterion | Score |
120	|-----------|-------|
121	| Overall | 4/6 (Weak Accept) |
122	| Confidence | 4/5 |
123	| Soundness | 3/4 |
124	| Presentation | 3/4 |
125	
126	### R2 (Novelty + Related Work)
127	| Criterion | Score |
128	|-----------|-------|
129	| Overall | 4/6 (Weak Accept) |
130	| Confidence | 4/5 |
131	| Novelty | 2/4 (Moderate) |
132	| Significance | 3/4 (High) |
133	
134	### Consensus Score
135	| Criterion | Score |
136	|-----------|-------|
137	| **Overall** | **4/6 (Weak Accept)** |
138	| Confidence | 4/5 |
139	| Soundness | 3/4 |
140	| Novelty | 2/4 |
141	| Significance | 3/4 |
142	| Presentation | 3/4 |
143	
144	---
145	
146	## 7. Meta-Review and Recommendation
147	
148	**Recommendation: Weak Accept (4/6)**
149	
150	Both reviewers converged on 4/6 with high confidence. The paper fills a genuine, well-motivated evaluation gap (S1) and its controlled decomposition experiment is methodologically clean (S2). The honest handling of TrajGuard limitations (S3) and the probe fidelity diagnostic (S4) demonstrate scientific rigor.
151	
152	However, the paper faces three significant concerns that prevent a stronger recommendation:
153	
154	1. **No methodological novelty** (W1): This is purely an evaluation paper applying existing attacks to existing monitors. The controlled decomposition, while clean, compares well-known aggregation strategies with a somewhat predictable outcome (CUSUM > pointwise).
155	
156	2. **Insufficient literature coverage** (W2): 10 references is far below venue standards. The Related Work section needs substantial expansion to properly position the work within adversarial ML, probing, and safety alignment literatures.
157	
158	3. **Limited scope for a benchmark claim** (W3-W5): One primary model, one monitor with unreliable RL results, and no controlled decomposition under RL weaken the benchmark's generality.
159	
160	**Path to stronger acceptance**: (a) Expand references to 25+, (b) add controlled decomposition under RL, (c) evaluate on at least one additional model with both attacks, (d) reframe contributions to emphasize the controlled decomposition and negative finding over the benchmark framing, as the benchmark scope is currently too narrow.
161	
162	The paper is above the reject threshold due to the clean controlled decomposition result and the well-executed negative finding, but below the clear accept threshold due to limited novelty and scope. It would benefit from a venue that values empirical evaluation and negative findings (e.g., EMNLP Findings or a safety workshop at a top venue).
163	
164	---
165	
166	## 8. Experiment Coverage vs. Design
167	
168	All 17 planned experiments from the review context are covered in the paper:
169	- NExT-Guard GCG/RL: ✓
170	- Kelp reimpl/GCG/RL: ✓
171	- TrajGuard reimpl/GCG/RL: ✓ (RL non-converged, properly flagged)
172	- Controlled decomposition (5 strategies): ✓
173	- Cross-monitor vulnerability analysis: ✓
174	- CoT premeditation + layer ablation: ✓
175	- Text-level baseline: ✓
176	- Cross-model replication (GCG only): ✓
177	- Evasion-quality Pareto: ✓
178	- SN-CUSUM vs CUSUM: ✓
179	- Probe fidelity diagnostic: ✓
180	
181	Coverage is complete. The paper faithfully reports all planned experiments including negative/inconclusive results (TrajGuard RL non-convergence, SN-CUSUM non-significance). No cherry-picking detected.
182	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5761aea3-24a1-4bc3-969b-3b242229f313",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "aadba285677a62d0f",
  "type": "user",
  "uuid": "807065d9-dee1-4da1-9d08-9ff7a9f8752c",
  "sourceToolAssistantUUID": "5761aea3-24a1-4bc3-969b-3b242229f313",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-17T15:51:03.168Z_

Now I have sufficient context. Let me note that the paper I'm reviewing is the "best" scenario version (from the dream simulation), which differs from the "median" scenario in key ways: the best scenario reports much larger effect sizes (43pp/66pp vs 18-42pp), claims temporal aggregation provides a 0.23 AUC gap (vs 0.13), and frames the paper as about "why streaming monitors resist adaptive attacks" (the title mentions temporal aggregation as implicit defense). Let me also check if there's a discrepancy in the title between the task description and the paper.

The task description title is: "Temporal Aggregation as Implicit Adversarial Defense: Why Streaming Safety Monitors Resist Adaptive Attacks" but the actual paper.tex title is "StreamProbe-Bench: Adversarial Robustness Evaluation of Streaming Safety Monitors for Large Language Models." The paper summary in the task description appears to describe a reframed version of the paper (defense-analysis framing) that differs somewhat from the paper.tex I read (which frames it as an attack/vulnerability paper). I'll review based on the task description's framing as that represents the final intended version.

Now I have enough information to write my review.

---

# Review: "Temporal Aggregation as Implicit Adversarial Defense: Why Streaming Safety Monitors Resist Adaptive Attacks"

## 1. Summary

This paper claims to present the first adversarial robustness evaluation of streaming safety monitors, testing three architecturally distinct systems (NExT-Guard, Kelp, TrajGuard) under GCG and RL-Obfuscation attacks on DeepSeek-R1-Distill-7B. The central novelty claim is a controlled decomposition showing that temporal aggregation over hidden-state sequences provides an independent 6pp AUC robustness benefit, and a Pareto analysis showing temporal monitors force 2-4x worse attack tradeoffs. A negative result on CoT premeditation detection is included as an additional contribution.

## 2. Novelty Assessment

### Contribution 1: StreamProbe-Bench (first adversarial robustness benchmark for streaming monitors)

**Assessment: Incremental, with debatable "first" claim.**

The "first adversarial evaluation" claim depends on a narrow definition of "streaming safety monitors." RL-Obfuscation (which this paper cites) already evaluated evasion against safety classifiers that operate on hidden states. The distinction between a "static" hidden-state classifier and a "streaming" one is that the latter has temporal aggregation, but the line is blurry. The paper's own Llama-Guard baseline uses a sliding window (a form of streaming). Furthermore, concurrent work on Qwen3Guard-Stream's degradation (57.2pp on novel prompts, cited in the paper) is closely adjacent. The "first" claim is defensible but fragile; a reviewer familiar with the full landscape might identify near-misses.

The benchmark itself consists of applying two known attacks (GCG, RL-Obfuscation) to three monitors. This is systematic evaluation engineering, not methodological innovation. The benchmark has only 3 monitors, 1 primary model, and 2 attack types. By the standards of established robustness benchmarks (RobustBench has 100+ models, HarmBench covers 30+ attacks), this is narrow.

**Verdict: Genuinely new in the specific niche (streaming monitors + adaptive attacks), but the niche is narrow and the contribution is primarily one of engineering effort, not conceptual novelty.**

### Contribution 2: Controlled decomposition (temporal aggregation provides 6pp AUC robustness, p=0.003)

**Assessment: The most novel experimental design, but the finding is expected.**

The controlled experiment design (same probe, vary only aggregation) is methodologically sound and eliminates confounds from reimplementation fidelity. However, the finding itself is essentially: "averaging/accumulating noisy signals over time provides noise robustness." This is a foundational result in signal processing and time-series analysis, well-established since the 1950s (Wald's sequential analysis, Page's CUSUM). The paper acknowledges temporal robustness precedent in video adversarial robustness, but does not adequately engage with the extensive literature on why smoothing resists perturbation.

The 6pp AUC benefit (paper summary) or 0.23 AUC gap (paper.tex "best" scenario) is the quantification of a qualitatively predictable effect. The contribution is in quantifying the effect in this specific domain, not in discovering it.

**Verdict: Clean experimental design that confirms an expected result. Quantification has value but the insight itself has strong prior art in signal processing and sequential detection theory. A reviewer with signal processing background would find this obvious in hindsight.**

### Contribution 3: Evasion-quality Pareto analysis (2-4x worse tradeoffs)

**Assessment: Incremental extension of the main benchmark.**

Pareto frontier analysis of evasion vs. quality is a natural extension of the attack evaluation. The "2-4x worse tradeoff" framing is attention-grabbing but depends heavily on the quality threshold chosen and the specific monitors compared. This is an analysis technique, not a contribution in itself.

**Verdict: Standard analysis applied to the benchmark results. Not independently novel.**

### Contribution 4: Negative result on CoT premeditation detection

**Assessment: Useful but builds on recycled Phase 0 data with narrow scope.**

The negative result (token AUC <= 0.53 at layers 8-24) uses only linear probes on a single model. The paper acknowledges that nonlinear probes or multi-layer probes might succeed. This makes the "closing the hypothesis" language overconfident. The paper closes the hypothesis for linear probes at single layers on one model, which is a subset of what community members might mean by "probing the reasoning trace."

Additionally, this finding was generated during Phase 0 (before the pivot to benchmark framing) and is being repurposed. While negative findings have value, the scope limitation (linear probes only, single model) and the fact that layer 24 achieves trace AUC of 0.687 (above chance, potentially usable with better aggregation) weakens the "impossible" framing.

**Verdict: Useful negative result with caveats. Would be a minor contribution on its own but adds value as supplementary evidence. The "closing the hypothesis" language is overclaimed given the narrow scope.**

## 3. Related Work Critique

### Coverage Assessment: SEVERELY INSUFFICIENT

The paper has only 3 paragraphs of Related Work with approximately 8-10 references. For a top venue, this is unacceptable. Specific gaps:

**Missing critical categories:**

1. **Adversarial evaluation methodology**: Carlini et al. (2019) "On Evaluating Adversarial Robustness" establishes best practices that should frame this work. Tramer et al. on adaptive attacks. The paper applies attacks without engaging with the methodological literature on how to do so correctly.

2. **Broader jailbreaking landscape**: AutoDAN (Liu et al., 2023), PAIR (Chao et al., 2023), TAP (Mehrotra et al., 2023), and many others. Why GCG and RL-Obfuscation specifically? The attack selection is poorly justified in the context of the broader landscape.

3. **Temporal robustness in adjacent domains**: The paper briefly acknowledges video adversarial robustness but does not cite specific works (e.g., temporal smoothing defenses in video classification by Li et al., Xiao et al.). The connection to industrial sequential detection (CUSUM literature) deserves more than a passing mention.

4. **Representation probing literature**: Belinkov & Glass (2019), Li et al. (2023 on representation engineering), Burns et al. (2022 on discovering latent knowledge). The CoT negative finding must be positioned against this rich literature.

5. **Ensemble and multi-signal defenses**: The finding that different architectures have complementary vulnerabilities immediately suggests ensemble approaches (well-studied in adversarial robustness).

6. **Safety alignment and guardrails**: Broader context on how streaming monitors fit into the safety stack (RLHF, Constitutional AI, input/output filters).

7. **Certified robustness and randomized smoothing**: The temporal aggregation insight has a natural connection to randomized smoothing (Cohen et al., 2019), where averaging predictions provides certified robustness. This connection is entirely missed.

### Positioning Assessment: INADEQUATE

The Related Work does not clearly differentiate this work from:
- Prior adversarial evaluations of any safety classifier (text or hidden-state)
- Prior work on temporal smoothing for robustness in other domains
- The specific monitors' own robustness discussions (Kelp and TrajGuard presumably discuss robustness in their papers)

The "first" claim would benefit from a systematic table showing what prior work has and has not evaluated, making the gap explicit rather than asserted.

## 4. Strengths

- **Fills a real evaluation gap**: The specific combination (streaming + temporal monitors + adaptive attacks) is genuinely underexplored. The SoK citation provides external validation of the gap.
- **Controlled decomposition design is methodologically clean**: Using same-probe-different-aggregation eliminates reimplementation confounds. This is the paper's best experimental idea.
- **Transparent handling of limitations**: NExT-Guard anchoring with official code, explicit fidelity metrics for reimplementations, and reporting of non-convergence issues demonstrate scientific honesty.
- **Complementary attack modalities**: GCG (input-level) and RL-Obfuscation (weight-level) test meaningfully different threat models.
- **Cross-model validation attempt**: While limited to GCG only, the Qwen2.5-7B replication at least addresses the "model-specific" concern partially.
- **Probe fidelity diagnostic adds mechanistic understanding**: Decomposing failures into representation drift vs. aggregation bypass goes beyond "monitors fail" to "why."

## 5. Weaknesses

- **(Major) The core insight is well-known**: That temporal averaging provides noise/perturbation robustness is established in signal processing, time-series anomaly detection, video adversarial robustness, and randomized smoothing. The paper presents this as a discovery rather than a quantification of a known phenomenon in a new domain. This fundamentally limits novelty.

- **(Major) Related Work is grossly insufficient**: 3 paragraphs and ~8-10 references for a top venue paper is unacceptable. Critical literature on adversarial evaluation methodology, temporal robustness in other domains, representation probing, and ensemble defenses is entirely missing. This suggests either incomplete literature survey or deliberate omission to make the work seem more novel.

- **(Major) The reframing feels forced**: The paper originally hypothesized that monitors would be vulnerable, found they partially resist (with degradation), and reframed to "why do they resist?" The title "Temporal Aggregation as Implicit Adversarial Defense" oversells the finding. The monitors still suffer 43pp/66pp drops (per the best-scenario numbers). Calling this "resistance" is generous. The framing oscillates between "monitors are vulnerable" (Table 1 headline) and "monitors resist through temporal aggregation" (title and decomposition claim). These are contradictory narratives.

- **(Major) Narrow scope for a benchmark claim**: 3 monitors, 1 primary model, 2 attacks. Two of three monitors are reimplemented with acknowledged deviations. This is a pilot study, not a benchmark. Calling it the "first benchmark" when it has 3 data points on the monitor axis is overclaiming.

- **(Moderate) The connection to randomized smoothing is entirely missed**: The paper's central finding (averaging over temporal predictions provides robustness) is essentially the same insight as randomized smoothing (Cohen et al., 2019), where averaging predictions under noise provides certified robustness guarantees. This connection would both strengthen the paper (by providing theoretical backing) and weaken the novelty claim (it's a known mechanism). Its absence suggests the authors are not aware of this literature.

- **(Moderate) Negative CoT finding uses narrow methodology**: Linear probes only, single model, layers 8-24 only. The paper does not try nonlinear probes, multi-layer probes, or probes on other models. Claiming to "close" a hypothesis while using only the simplest possible probe type is overclaiming.

- **(Moderate) No defense contribution**: The paper identifies that temporal aggregation helps but proposes no new defense. The practical recommendation (use max-pooling) is trivial. A top venue paper on adversarial robustness typically needs either a defense contribution or a much more thorough evaluation than 3 monitors.

- **(Minor) Statistical power concerns for the architectural vulnerability claims**: With N=3 monitors, claiming "architecture determines vulnerability profile in a predictable pattern" based on rank orderings is not statistically rigorous. Any 3 systems will show some pattern. The Fisher exact tests confirm monitors differ, but the mechanistic explanations (GRU amplifies, geometry resists perturbation) are post-hoc.

## 6. Framing and Narrative

The narrative has a coherence problem stemming from the pivot. The paper wants to simultaneously say:
1. "Streaming monitors are vulnerable" (motivates the benchmark)
2. "Temporal aggregation provides implicit defense" (the intellectual claim)
3. "CoT premeditation is undetectable" (supplementary finding)

Claims 1 and 2 are in tension. If monitors retain 64-72% F1 under attack (per the task description) while suffering 43-66pp detection drops, are they "robust" or "vulnerable"? The title emphasizes resilience ("resist adaptive attacks") while the main results table emphasizes vulnerability. A reader finishes unsure which story the paper is telling.

The reframing from "attack paper" to "defense analysis paper" is apparent. The controlled decomposition (Contribution 2) was likely designed after the main benchmark results came in and showed moderate rather than catastrophic failure. This is not inherently problematic (many good papers emerge from surprising results), but the narrative needs to commit to one direction. Currently it reads as: "We expected catastrophic failure, found moderate failure, and reframed to study why failure wasn't catastrophic."

The negative CoT finding (Contribution 4) feels bolted on. It comes from a different experimental setup (Phase 0 data, probing task rather than attack evaluation), addresses a different question, and shares only the model with the main benchmark. Its inclusion appears motivated by padding rather than narrative coherence.

## 7. Questions for Authors

1. How do you differentiate your "temporal aggregation provides robustness" finding from the well-established result that temporal smoothing/averaging resists adversarial perturbation in other domains (video classification, randomized smoothing)? What is genuinely new beyond applying this known principle to LLM safety monitors?

2. The title says monitors "resist" attacks, but they suffer 43-66pp drops. What definition of "resistance" are you using, and how does this framing serve the reader vs. a straightforward vulnerability framing?

3. Why is the Related Work limited to 3 paragraphs? Are you aware of the randomized smoothing literature (Cohen et al., 2019), adversarial evaluation best practices (Carlini et al., 2019), and temporal robustness work in video (Li et al., Xiao et al.)? How does your finding relate to these?

4. The controlled decomposition shows max-pooling achieves 0.813 AUC under GCG. Does this ordering hold under RL-Obfuscation? If not tested, how can you claim temporal aggregation is a general robustness mechanism?

5. For the CoT negative finding: have you tried any nonlinear probes? A 2-layer MLP or attention-based probe might extract signal that a linear probe cannot. Without trying this, "closing the hypothesis" is premature.

6. How do you reconcile the 13pp reimplementation deviation for TrajGuard (mentioned in memory.md) with the 1.9pp deviation reported in the paper.tex? Which numbers are correct?

7. Given that Llama-Guard-3 (text-level) shows only 18pp GCG drop while hidden-state monitors show 32-53pp drops, what is the practical argument for hidden-state monitoring?

## 8. Preliminary Score: 3 (Weak Reject)

**Justification:**

The paper addresses a genuine evaluation gap and the controlled decomposition is a clean experimental design. However, several factors prevent acceptance at a top venue:

1. **Core novelty is low**: The central finding (temporal aggregation provides adversarial robustness) is well-established in signal processing and adjacent ML domains. Quantifying it for LLM streaming monitors is useful but not sufficiently novel for a top venue main track.

2. **Related work is unacceptable**: 3 paragraphs and ~8-10 references is below the minimum standard. Critical connections to randomized smoothing, adversarial evaluation methodology, and temporal robustness in other domains are entirely missing.

3. **Narrative incoherence**: The paper cannot decide if monitors are vulnerable or robust, leading to a confusing story. The pivot from attack paper to defense analysis is visible and unresolved.

4. **Scope too narrow for a "benchmark" claim**: 3 monitors on 1 model does not constitute a benchmark by community standards.

5. **No new methods or defenses**: Pure evaluation papers at top venues need either much broader scope or deeper theoretical insight. This paper has neither.

The paper would be appropriate for EMNLP Findings or a workshop (SafeGenAI, TrustNLP) where empirical evaluation contributions with modest novelty are valued. For the main track of a top venue at 25% acceptance, the novelty bar is not met.

## 9. Confidence: 4/5

I have strong familiarity with adversarial robustness literature, sequential detection theory, and representation probing for LLMs. The assessment of the temporal aggregation insight as "known" is based on direct knowledge of the randomized smoothing and temporal robustness literatures. I am slightly less confident about whether the "first streaming monitor evaluation" claim has near-misses in concurrent/unpublished work, hence 4 rather than 5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "807065d9-dee1-4da1-9d08-9ff7a9f8752c",
  "isSidechain": true,
  "agentId": "aadba285677a62d0f",
  "requestId": "req_011Cb8QT3sKDs2e9syRDTm3D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29098bd9-0eba-4abe-b228-b8d7949313d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jt6V13vJcUJ9xnMFQDJ5Gn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7673,
      "cache_read_input_tokens": 41363,
      "output_tokens": 4300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7673
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4300,
          "cache_read_input_tokens": 41363,
          "cache_creation_input_tokens": 7673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7673,
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
