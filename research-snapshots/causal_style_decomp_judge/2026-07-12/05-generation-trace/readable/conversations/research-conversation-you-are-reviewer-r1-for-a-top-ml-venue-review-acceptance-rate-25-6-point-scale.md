# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab31f0ce728c24af1.jsonl`
- **Structured JSON:** [`4fc28420a9f45f69990a.json`](../../sessions/4f/4fc28420a9f45f69990a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-17T15:48:13.428Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus areas: **methodology soundness** and **experimental rigor**.

## Paper Summary

**Title**: "Temporal Aggregation as Implicit Adversarial Defense: Why Streaming Safety Monitors Resist Adaptive Attacks"

**Core claim**: Streaming safety monitors that use temporal aggregation over hidden-state activations are inherently more robust to adversarial attacks (GCG, RL-Obfuscation) than static classifiers and text-level monitors. The authors construct "StreamProbe-Bench" to evaluate 3 monitors (NExT-Guard, Kelp, TrajGuard) on DeepSeek-R1-Distill-7B.

**Key results**:
- GCG: 11-15pp F1 drop for streaming monitors vs 27pp for Llama-Guard-3 text baseline
- RL-Obfuscation: 12-22pp drop, no convergence at 40K steps vs 41pp for text baseline
- Controlled decomposition: any temporal aggregation gives 6pp AUC benefit over pointwise (p=0.003), but specific strategy doesn't matter
- Pareto analysis: temporal monitors have 2-4x smaller feasible evasion region
- Negative CoT finding: per-token probes at layers 8-24 yield AUC~0.49-0.58, indistinguishable from chance
- Cross-model validation on Qwen2.5-7B-Instruct shows consistent patterns (2-3pp larger drops)

**Key methodological details**:
- NExT-Guard: official implementation, SAE on per-token hidden states with window mean aggregation (w=32)
- Kelp: REIMPLEMENTED from paper (85% architecture match, 11pp baseline F1 deviation from reported)
- TrajGuard: REIMPLEMENTED from paper (80% architecture match, 13pp baseline F1 deviation)
- GCG: 500 steps, top-k=256
- RL-Obfuscation: QLoRA PPO, 40K step budget
- Evaluation data: 500 harmful + 200 benign traces (DeepSeek), 127 harmful + 200 benign for CoT
- Controlled decomposition: single MLP probe on layer 16, 5 aggregation strategies
- Cross-model: Qwen2.5-7B-Instruct for GCG only

**Experiment design reference** (what was planned vs what appears in paper):
The full experiment plan includes 15 experiments. The paper covers:
1. NExT-Guard GCG ✓ (Table 1)
2. NExT-Guard RL-Obfuscation ✓ (Table 2)
3. Kelp reimplementation ✓ (mentioned in §3.2)
4. Kelp GCG ✓ (Table 1)
5. Kelp RL-Obfuscation ✓ (Table 2)
6. TrajGuard reimplementation ✓ (mentioned in §3.2)
7. TrajGuard GCG ✓ (Table 1)
8. TrajGuard RL-Obfuscation ✓ (Table 2)
9. Controlled decomposition ✓ (Table 3)
10. Vulnerability analysis ✓ (Table 8)
11. Negative CoT premeditation ✓ (Table 7)
12. Text baseline (Llama-Guard) ✓ (Tables 1, 2)
13. Second model (Qwen) ✓ (Table 6)
14. Evasion-quality Pareto ✓ (Table 4)
15. Layer ablation for CoT ✓ (Table 7)
16. SN-CUSUM vs CUSUM ✓ (mentioned in §4.3)
17. Probe fidelity diagnostic ✓ (Table 5)

So coverage appears comprehensive on paper.

## Your Review Task

Evaluate methodology and experiments. Structure your review as:

1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, specific)
3. **Weaknesses** (bulleted, specific, with severity: major/minor)
4. **Questions for Authors** (specific, answerable)
5. **Missing Experiments or Controls**
6. **Detailed Comments** (section-by-section if needed)
7. **Preliminary Score** (1-6) with justification
8. **Confidence** (1-5, where 5 = expert)

Be rigorous. Focus on:
- Are the reimplementation fidelity issues adequately handled? Can we trust conclusions drawn from Kelp/TrajGuard?
- Is the controlled decomposition well-designed? Does it actually isolate temporal aggregation?
- Is the 40K RL step budget sufficient to claim "resistance"? Could more compute break the monitors?
- Is the text baseline (Llama-Guard-3) a fair comparison? It's a different architecture entirely.
- Are statistical tests appropriate? Sample sizes sufficient?
- Does the "credit assignment barrier" explanation hold up mechanistically?
- Is the negative CoT finding well-supported given 127 traces?
- Are there confounds in the experimental design?

Output your complete review in markdown format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "66682a48-39f4-431c-ae78-8e74d0a90e98",
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

_source line 2 · 2026-05-17T15:48:13.434Z_

```json
{
  "parentUuid": "66682a48-39f4-431c-ae78-8e74d0a90e98",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
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
  "uuid": "3dca5988-eaa7-4a63-a712-9b4df6303023",
  "timestamp": "2026-05-17T15:48:13.434Z",
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

_source line 3 · 2026-05-17T15:48:17.069Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dca5988-eaa7-4a63-a712-9b4df6303023",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QNYb4ofo5ioQGoajuT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cab7e7f-2149-495f-83d0-03e5a7568b22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KR8fucNzSr7YX9CaA3kV9C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8439,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8439,
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

_source line 4 · 2026-05-17T15:48:17.651Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L2pzf7hutWyBKXDQ6D5Wyo`</summary>

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
  "parentUuid": "3cab7e7f-2149-495f-83d0-03e5a7568b22",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QNYb4ofo5ioQGoajuT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11df5737-4e7e-41b4-a514-59dda555969f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KR8fucNzSr7YX9CaA3kV9C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8439,
      "cache_read_input_tokens": 8255,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8439
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8439,
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

_source line 5 · 2026-05-17T15:48:17.657Z_

<details><summary>↩ Tool result · `toolu_01L2pzf7hutWyBKXDQ6D5Wyo`</summary>

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
  "parentUuid": "11df5737-4e7e-41b4-a514-59dda555969f",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "0232a5b5-5820-44c6-83a7-af82fe10a156",
  "sourceToolAssistantUUID": "11df5737-4e7e-41b4-a514-59dda555969f",
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

_source line 6 · 2026-05-17T15:48:20.544Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01JVjjWWqvPXGLkGqkS4JvCy`</summary>

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
  "parentUuid": "0232a5b5-5820-44c6-83a7-af82fe10a156",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QNrpSKZHDGMsGix1RY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cbe533f-970f-4890-abbf-008d2364089d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B979zBAyEJNot1FeSFjvVp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 16694,
      "output_tokens": 77,
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
          "output_tokens": 77,
          "cache_read_input_tokens": 16694,
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

_source line 7 · 2026-05-17T15:48:20.583Z_

<details><summary>↩ Tool result · `toolu_01JVjjWWqvPXGLkGqkS4JvCy`</summary>

```text
{"result":"# 项目 streamprobe_adversarial_robustness 概况\n\n## 实验状态 (4 个)\n\n- **phase0_mvp_pipeline**: RUNNING (negative) — \n- **phase0_step4_5_recovery**: PREPARING — \n- **mvp_benign_trace_gen**: ANALYZING (success) — \n- **mvp_trace_gen**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| phase0_mvp_pipeline | Hidden-state probes on DeepSeek-R1-Distill-7B CoT traces detect harmful premeditation (AUC>0.85) with temporal drift evidence (relaxed_B>=20%) using D003 onset definition (response-level, post-&lt;/think> boundary) | — | — | — |\n| mvp_benign_trace_gen | DeepSeek-R1-Distill-7B generates multi-step reasoning traces on benign prompts (GSM8K/ARC-Challenge) that serve as safe-class control for probe training, with comparable trace length/complexity to harmful traces | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_trace_gen** (failed): DeepSeek-R1-Distill-7B with unified config (temp=1.0, no system prompt) on harmful prompts produces a mix of complied and refused traces sufficient for MVP (≥150 each from 500 prompts)\n\n## 趋势\n成功 0 / 负向 0 / 失败 1 / 共 1\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-39593: 无 GPU 信息\n\n## 告警\n- mvp_trace_gen: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cbe533f-970f-4890-abbf-008d2364089d",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "2635e98f-3d61-4963-945d-fd042789fb7e",
  "sourceToolAssistantUUID": "8cbe533f-970f-4890-abbf-008d2364089d",
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

_source line 8 · 2026-05-17T15:48:24.660Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01X45an299MZEwPwNuoZa5mD`</summary>

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
  "parentUuid": "2635e98f-3d61-4963-945d-fd042789fb7e",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QP5Ca1UC8LR3VyjbjE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8b3a0eb-11f2-4953-9995-95bab52bfa41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuZMWZzd9HTwNUuLLHrCmf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 18142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
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

_source line 9 · 2026-05-17T15:48:24.679Z_

<details><summary>↩ Tool result · `toolu_01X45an299MZEwPwNuoZa5mD`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'streamprobe_adversarial_robustness'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8b3a0eb-11f2-4953-9995-95bab52bfa41",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "4314510a-484a-400c-8fa7-74a5c2ded943",
  "sourceToolAssistantUUID": "c8b3a0eb-11f2-4953-9995-95bab52bfa41",
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

_source line 10 · 2026-05-17T15:48:25.142Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01P1SMXrVAaHztaQiDmh9gds`</summary>

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
  "parentUuid": "4314510a-484a-400c-8fa7-74a5c2ded943",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QP5Ca1UC8LR3VyjbjE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d67adec3-7159-4cf8-b0e9-d2a6bb5a3edb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuZMWZzd9HTwNUuLLHrCmf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 18142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
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

_source line 11 · 2026-05-17T15:48:25.151Z_

<details><summary>↩ Tool result · `toolu_01P1SMXrVAaHztaQiDmh9gds`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/ROADMAP.md\", \"content\": \"# streamprobe_adversarial_robustness — Research Dashboard\\n\\n> 最后更新: 2026-05-17 14:51 UTC | 更新原因: D006 MVP FAIL pivot to benchmark-primary; research 阶段启动; Dream 模拟进行中\\n\\n> 核心方向已 pivot（D006）\\n\\n## 核心方向\\n\\n**Benchmark-primary**: StreamProbe-Bench — 首个 streaming safety monitor 对抗鲁棒性 benchmark。评估 Kelp/NExT-Guard/TrajGuard 在 GCG + RL-Obfuscation 下的鲁棒性。Secondary: 架构脆弱性分析 + CoT premeditation 阴性结果。详见 paper_framing.md。\\n\\n目标投稿：**ARR May 25, 2026**（7 天，D2=May 18）\\n\\n## 当前进展\\n\\n- 阶段：Research（MVP FAIL → pivot to benchmark-primary）\\n- MVP 结论：Layer 16 hidden states 在 CoT 中无 premeditation signal（token AUC=0.49 反预测）\\n- 基础设施：westd-39593（4×5090 32GB），200GB 数据盘\\n- Phase 0 产出：500 harmful traces（204 complied）+ 200 benign + probe_v2 checkpoint + hidden states\\n- Dream 模拟已启动（dream_20260517T145100），等待结果\\n\\n## 近期任务\\n\\n- [x] GPU 到位 + 环境部署\\n- [x] 代码框架 6 模块\\n- [x] Phase 0 trace gen + onset + probe + temporal（MVP FAIL，D006）\\n- [ ] Dream 结果评估（等待 10-25min）\\n- [ ] NExT-Guard 官方代码 clone + 验证\\n- [ ] Kelp/TrajGuard 论文规格调研（Agent 执行中）\\n- [ ] Qwen2.5-7B-Instruct 下载\\n- [ ] 修复 temporal_analysis.py（trace-level FPR control + cusum_max AUC）\\n- [ ] benchmark 实验启动（Dream 通过后）\\n\\n## 7 天 Timeline（May 18-25）\\n\\n| Phase | Days | 工作 | 状态 |\\n|-------|------|------|------|\\n| Plan | D2 | Dream + framing 确认 + 实验审批 | 进行中 |\\n| Benchmark | D2-5 | 3 monitors × (GCG + RL-Obfuscation) | 待启动 |\\n| Analysis | D4-6 | Controlled decomposition + vulnerability analysis + negative finding | 待启动 |\\n| Paper | D5-8 | Results → Method → Intro → Abstract | 待实验 |\\n\\n## GPU 预算\\n\\n- 分配：4×5090 32GB（westd-39593），全部属本项目（C001）\\n- P0：~101 GPU-hours | P1：~42h | P2：~16h\\n- 可用：672 GPU-hours（4卡×7天×24h），headroom 充足\\n- 瓶颈：RL-Obfuscation ~24h/monitor，3 monitors 可跨 GPU 并行\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-17 | D006: MVP FAIL — pre-onset CoT 无可检测的 premeditation | phase0_mvp_pipeline |\\n| D005 | 2026-05-17 | D004 降级为 CONDITIONAL：Reviewer 指出 probe 过拟合 + P95 异 | phase0_mvp_pipeline |\\n| D004 | 2026-05-17 | MVP 判定：Qualified PASS — pre-onset per-token AUC 不达 | mvp_trace_gen |\\n| D003 | 2026-05-17 | Onset 重定义为 response（&lt;/think> 后）首个 harmful token，Co | mvp_trace_gen |\\n| D002 | 2026-05-17 | Onset 定义修正：从\\\"首次 harmful topic mention\\\"改为\\\"首次 action | mvp_trace_gen |\\n| D001 | 2026-05-17 | Safe class 使用 benign prompts（GSM8K/ARC），不依赖 same-p | mvp_trace_gen |\\n\\n\\n\", \"total_chars\": 2296, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d67adec3-7159-4cf8-b0e9-d2a6bb5a3edb",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "2a512390-9497-42f7-b501-5ff7d26e780c",
  "sourceToolAssistantUUID": "d67adec3-7159-4cf8-b0e9-d2a6bb5a3edb",
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

_source line 12 · 2026-05-17T15:48:25.654Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01W5XKQhFAxA7zYzTz9UQdWy`</summary>

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
  "parentUuid": "2a512390-9497-42f7-b501-5ff7d26e780c",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QP5Ca1UC8LR3VyjbjE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e64110ae-a5c6-4e78-a2f3-999ea737ac06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuZMWZzd9HTwNUuLLHrCmf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 18142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
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

_source line 13 · 2026-05-17T15:48:25.663Z_

<details><summary>↩ Tool result · `toolu_01W5XKQhFAxA7zYzTz9UQdWy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/memory.md\", \"content\": \"# Memory — streamprobe_adversarial_robustness\\n\\n## Phase 0 MVP 结果 (2026-05-17)\\n\\n### D005 诊断后修正指标（以此为准）\\n\\n| 指标 | 原始（过拟合） | v2 (修复) | v2 + calibrated |\\n|------|---------------|-----------|-----------------|\\n| train_loss / val_loss | 0.002 / 4.214 | 0.153 / 1.283 | N/A |\\n| P95 threshold | 0.000308 | 0.4759 | 0.2076 |\\n| token-level AUC (pre-onset) | 0.547 | 0.492 | 0.479 |\\n| trace-level AUC | 0.665 | 0.609 | 0.625 |\\n| relaxed_B | 76% | 43.1% | 44.1% |\\n| detection @1% FPR | 16.2% | 27.0% | 27.0% |\\n| detection @5% FPR | 93.1% | 88.2% | 88.2% |\\n| Mech A / B(strict) / Neither | 93.1/0/6.9% | 88.2/0/11.8% | 88.2/0/11.8% |\\n\\n- Platt scaling: A=6.333, B=-4.353\\n- v2 probe: hidden_dim=128, dropout=0.3, weight_decay=1e-4, early stop on val_loss (patience=3)\\n- Best checkpoint = epoch 1 (early stopped at epoch 4)\\n\\n### 关键洞察\\n- 原始 relaxed_B=76% 被过拟合虚高，修正后 44%（仍>20%门槛）\\n- Pre-onset token-level AUC < 0.5：CoT 中 harmful 大多数 token 分数比 safe 低\\n- 但 88% traces 仍被检出：靠少量 spike token (Mechanism A 主导)\\n- 44% traces 的检出依赖 CUSUM 累积（spike_frac<10%）\\n- detection @1% FPR 修复后反升（16%→27%）：校准后低 FPR 区更可靠\\n\\n### 样本统计\\n- 500 harmful prompts → 204 complied (41%), 296 refused\\n- 200 benign prompts → 200 traces\\n- Safe class = 496 (200 benign + 296 refused)\\n\\n### D003 Onset 定义\\n- Onset = `&lt;/think>` 后 response 中首个 harmful token\\n- 整个 CoT (`&lt;think>...&lt;/think>`) 为 pre-onset window\\n- CoT 平均长度 ~1125 tokens\\n\\n### 基础设施\\n- 服务器: westd-39593, 4×5090 32GB\\n- 数据盘: /root/autodl-tmp (200GB, 156G 可用)\\n- DeepSeek 模型: /root/streamprobe/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B (symlink)\\n- Llama-Guard-3: /root/autodl-tmp/streamprobe/models/LLM-Research/Llama-Guard-3-8B\\n- 代码: /root/streamprobe/code/\\n- Outputs: /root/streamprobe/outputs/\\n- Phase 0 outputs 总大小: ~4.3G（hidden states 占主体）\\n\\n### 实际输出路径（与预设不同）\\n- 合并 traces: `outputs/combined_traces.jsonl`（非 merged_traces/）\\n- Onset labels: `outputs/onset_labels.jsonl`（文件，非目录）\\n- Probe: `outputs/probe/`（非 probe_output/）\\n- Probe v2: `outputs/probe_v2/`（D005 诊断版）\\n- Temporal: `outputs/temporal/`（非 temporal_results/）\\n- Temporal v2: `outputs/temporal_v2_calibrated/`\\n\\n### Bug 修复记录\\n- train_probe.py: float16 hidden states → .float() 转换\\n- train_probe_v2.py: 修复过拟合（降容量+dropout+weight decay+ES on val_loss）\\n\\n### Safe class 设计决策\\n- Probe 训练: benign + refused 都算 safe\\n- text_baseline.py: 支持 --safe_source benign/refused/both（默认 benign）\\n\\n### 竞品/Baseline 准备\\n- text_baseline.py: Llama-Guard-3 sliding-window baseline，已写好（含 --safe_source 修复）\\n- download_qwen.sh: Qwen2.5-7B-Instruct 下载脚本，已准备\\n\", \"total_chars\": 2471, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e64110ae-a5c6-4e78-a2f3-999ea737ac06",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "fcfb4a3a-e66f-419d-8594-f66dc5f2e3d9",
  "sourceToolAssistantUUID": "e64110ae-a5c6-4e78-a2f3-999ea737ac06",
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

_source line 14 · 2026-05-17T15:48:28.969Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QTDZggpM312RCi9HLsy5mM`</summary>

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
  "parentUuid": "fcfb4a3a-e66f-419d-8594-f66dc5f2e3d9",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QPT8vkaL3PkqGfz8i9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "774bb933-4eda-4f43-b37a-3a19f1f62ec5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdUK36kwNUdCGaEiJJU9Dc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3291,
      "cache_read_input_tokens": 18822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3291,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 15 · 2026-05-17T15:48:28.979Z_

<details><summary>↩ Tool result · `toolu_01QTDZggpM312RCi9HLsy5mM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/paper_framing.md\", \"content\": \"# Paper Framing — streamprobe_adversarial_robustness\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (LLM Security Track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (7 days remaining)\\n\\n## Core Claims (≤3)\\n\\n1. **[Benchmark]** Streaming safety monitors (Kelp, NExT-Guard, TrajGuard) exhibit substantially degraded detection performance under adaptive adversarial attacks (GCG suffix optimization + RL-Obfuscation), with attack success rates far exceeding those reported on standard benchmarks.\\n\\n2. **[Architectural Insight]** Monitor architecture determines adversarial vulnerability profile: temporal recurrence (Kelp GRU), sparse feature selection (NExT-Guard SAE), and geometric surveillance (TrajGuard) fail through distinct, predictable mechanisms under GCG vs RL-Obfuscation.\\n\\n3. **[Negative Finding]** Hidden-state probes at middle layers of reasoning models do not detect harmful premeditation during chain-of-thought: per-token safety scores in CoT are statistically indistinguishable from benign traces (AUC ≈ 0.5), and temporal aggregation (CUSUM) cannot rescue a signal that does not exist.\\n\\n## Story Spine\\n\\n- **Problem**: Streaming safety monitors for LLM generation have proliferated rapidly (Kelp, NExT-Guard, TrajGuard, Qwen3Guard-Stream, SafeProbing), yet NONE have been evaluated under adaptive adversarial attacks. SoK (Wang et al., S&P 2026) identifies this evaluation gap as critical. RL-Obfuscation showed static classifiers are vulnerable (59-89% evasion), but temporal/streaming monitors remain untested.\\n\\n- **Existing approaches & their gaps**: Each streaming monitor reports strong standard-benchmark performance (Kelp +15.61% F1 over static probes, NExT-Guard 84.3 F1, TrajGuard 95% detection). But Qwen3Guard-Stream's 57.2pp degradation on merely novel (non-adaptive) adversarial prompts foreshadows the problem. No systematic adversarial evaluation exists; deployment decisions are made on inflated benchmarks.\\n\\n- **Our framing**: We construct StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors. We evaluate three representative architectures under two adaptive attack methodologies, providing: (a) the first comparative robustness data, (b) architectural vulnerability analysis revealing distinct failure modes, (c) a controlled decomposition experiment isolating the contribution of temporal aggregation strategy, and (d) a negative result showing hidden-state CoT premeditation detection is infeasible at middle layers.\\n\\n- **Headline result template**: \\\"Under adaptive RL-Obfuscation, [worst monitor]'s detection rate drops from [X]% to [Y]% while [best monitor] maintains [Z]% detection, revealing that [architectural property] is the key determinant of adversarial robustness in streaming safety monitoring.\\\"\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an engineering benchmark\\\" critique**: Mitigate via Claim 2 (architectural insight with explanatory analysis) + Claim 3 (negative finding about CoT premeditation). The paper provides both evaluation AND insight.\\n- **Reimplementation fidelity for Kelp/TrajGuard**: NExT-Guard has official code. For Kelp and TrajGuard, we report architecture match percentage and invite author verification. Accepting 2/3 monitors as minimum viable benchmark (IDEA_BRIEF contingency).\\n- **Scope limited to one model**: DeepSeek-R1-Distill-7B primary, Qwen2.5-7B-Instruct secondary if time permits. Single-model limitation explicitly acknowledged.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy |\\n|---------|-------------------|\\n| \\\"Reimplementation may not be faithful\\\" | Use NExT-Guard official code as anchor; report fidelity metrics for Kelp/TrajGuard; controlled decomposition uses same-probe different-aggregation (no reimplementation needed) |\\n| \\\"Only one target model\\\" | Add Qwen2.5-7B-Instruct as P1; frame as \\\"proof of methodology\\\" if single-model |\\n| \\\"RL-Obfuscation didn't converge\\\" | Pre-specified convergence criteria (reward <1% improvement over 2K steps, 40K max, gradient norm diagnostic) |\\n| \\\"What's beyond the benchmark?\\\" | Claim 2 (architectural vulnerability analysis) + Claim 3 (negative CoT premeditation finding) + controlled decomposition |\\n| \\\"Why not just monitor text?\\\" | Text-level baseline (Llama-Guard sliding window) included as comparison |\\n| \\\"Small sample size\\\" | Bootstrap 95% CI on all metrics; 500 harmful + 200 benign traces |\\n\\n## Negative Finding Framing (Claim 3)\\n\\nPhase 0 MVP tested: \\\"Do hidden states in CoT accumulate detectable harmful premeditation signal?\\\"\\n\\nResult: No. At layer 16/28 of DeepSeek-R1-Distill-7B (v2 probe, overfitting fixed):\\n- Per-token probe AUC in CoT = 0.49 (anti-predictive: harmful CoT scores LOWER than benign)\\n- Trace-level mean-score AUC = 0.61 (weak)\\n- CUSUM-max AUC = 0.645 (no advantage over simple max-score AUC = 0.676)\\n- Detection @5% trace-level FPR = 0-5% (original 88% was token-to-trace FPR mixing bug)\\n- CUSUM false alarm rate on safe traces = 36.3% (v2 probe)\\n- **Strongest evidence**: On the SAME harmful prompts, probe scores are statistically indistinguishable between complied and refused traces (CUSUM fire rate 47.1% vs 45.3%, mean pre-onset score 0.0143 vs 0.0142). This rules out \\\"weak probe\\\" as explanation — hidden states genuinely do not encode compliance decisions at this layer.\\n\\nThis is reported as: \\\"Contrary to the hypothesis that reasoning traces leak compliance intent through hidden states, we find that middle-layer activations during CoT are statistically indistinguishable between harmful-compliant and benign traces. Critically, complied and refused traces on identical harmful prompts show no probe score difference, demonstrating that the model's compliance decision is not encoded in layer 16 activations during reasoning. This suggests compliance decisions are either encoded in later layers, emerge only at the response boundary, or are distributed across layers in ways that single-layer linear probes cannot capture.\\\"\\n\\nThis negative finding is valuable because it prevents the community from assuming probing-based CoT monitoring is straightforward.\\n\", \"total_chars\": 6086, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "774bb933-4eda-4f43-b37a-3a19f1f62ec5",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "a90c7e9c-59d7-4d2a-8416-08e90aefa063",
  "sourceToolAssistantUUID": "774bb933-4eda-4f43-b37a-3a19f1f62ec5",
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

_source line 16 · 2026-05-17T15:48:29.908Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015o3474Yj8LZaJXxPoMj9xv`</summary>

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
  "parentUuid": "a90c7e9c-59d7-4d2a-8416-08e90aefa063",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QPT8vkaL3PkqGfz8i9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7bbca8a-19a3-47e6-a1d9-ed70573b7275",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdUK36kwNUdCGaEiJJU9Dc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3291,
      "cache_read_input_tokens": 18822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3291,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 17 · 2026-05-17T15:48:29.917Z_

<details><summary>↩ Tool result · `toolu_015o3474Yj8LZaJXxPoMj9xv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/decisions.yaml\", \"content\": \"_next_id: 7\\ndecisions:\\n- id: D001\\n  date: 2026-05-17 08:37 UTC\\n  summary: Safe class 使用 benign prompts（GSM8K/ARC），不依赖 same-prompt refused traces\\n  rationale: R1-Distill-7B 无 system prompt 下 compliance rate 极高（可能接近 100%），refused\\n    traces 不足。Benign prompts 的 confound 风险（学到 topic 而非 reasoning pattern）在 MVP 中可控：(1)\\n    probe 在 harmful traces 内部也需区分 pre-onset（同话题但未 plan）vs post-onset tokens，不纯靠 topic；(2)\\n    temporal analysis 本身测试 GRADUAL DRIFT——若 probe 仅学 topic，harmful traces 上 score\\n    全程均匀高，CUSUM 无 signal，这本身就是 falsification。Llama-Guard 标注后如有 ≥50 refused traces，补充\\n    same-prompt ablation。\\n  related_experiments:\\n  - exp_id: mvp_trace_gen\\n    role: context\\n    result: running, ~100% compliance observed\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-17 09:18 UTC\\n  summary: Onset 定义修正：从\\\"首次 harmful topic mention\\\"改为\\\"首次 actionable harmful content\\\"\\n  rationale: Llama-Guard 对 R1 CoT 第一句即判 unsafe（因为复述了有害问题），导致 onset=0，pre-onset window\\n    消失。但研究目标是检测\\\"premeditation phase\\\"——模型在分析/规划有害行为但尚未输出可执行指令的阶段。科学上正确的 onset 应是首次出现\\n    actionable harmful instructions（步骤、代码、配方等），而非 topic mention。这与 Path Drift 描述的\\\"local\\n    compliance belies global deviation\\\"完全一致：规划阶段看起来无害，执行阶段才产出有害内容。\\n  related_experiments:\\n  - exp_id: mvp_trace_gen\\n    role: context\\n    result: onset labeling test revealed onset=0 with naive definition\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-17 09:25 UTC\\n  summary: Onset 重定义为 response（&lt;/think> 后）首个 harmful token，CoT 全段作为 pre-onset window\\n  rationale: D002 的 \\\"actionable vs topic mention\\\" 方案无法解决 R1 CoT 固有行为（首句即复述有害意图）。将\\n    onset 定义为 response 中首个 harmful token 有三重优势：(1) 实际部署场景对齐——安全监控的目标是在模型输出有害 response\\n    前拦截，CoT 是内部过程；(2) pre-onset window 有意义——整个 CoT（通常几百 token）成为早期检测窗口；(3) 研究问题更锐利——\\\"能否从\\n    reasoning trace 预测模型将输出有害内容\\\"比\\\"CoT 内部 onset\\\"更重要且更 novel。Detection Lead = 在 response\\n    前多少 token 检出，直接衡量早期预警能力。\\n  related_experiments:\\n  - exp_id: mvp_trace_gen\\n    role: context\\n    result: onset labeling test confirmed CoT-level onset=0 on all complied traces,\\n      D002 approach also failed\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-17 14:28 UTC\\n  summary: MVP 判定：Qualified PASS — pre-onset per-token AUC 不达标但 temporal accumulation\\n    假设得到比预期更强的验证\\n  rationale: ROADMAP 预注册指标：CoT probe AUC > 0.85 + relaxed_B ≥ 20%。结果：(1) probe val\\n    AUC=0.967 但 pre-onset token-level AUC=0.547（per-token 在 CoT 中近乎随机）；(2) relaxed_B=76%（远超\\n    20%）。按 strict 解读 pre-onset AUC 是 FAIL（0.547 < 0.75），但这个\\\"失败\\\"恰好是论文最强论点：pointwise\\n    detection 在 CoT 阶段彻底失败（AUC≈random），而 CUSUM temporal accumulation 成功检出 76% 的 harmful\\n    traces。这比原假设（\\\"probe 在 pre-onset 就能检出\\\"）提供了更强的 temporal accumulation 必要性证据。研究问题从\\\"probe\\n    能否在 CoT 早期检出 harmful intent\\\"reframe 为\\\"为什么 per-token detection 失败而 temporal accumulation\\n    成功\\\"——后者科学上更有趣。判定 qualified PASS，进入 research 阶段。\\n  related_experiments:\\n  - exp_id: mvp_trace_gen\\n    role: evidence\\n    result: 500 traces, 204 complied, pre-onset AUC=0.547, relaxed_B=76%\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-17 14:36 UTC\\n  summary: D004 降级为 CONDITIONAL：Reviewer 指出 probe 过拟合 + P95 异常低，需快速诊断后再判定\\n  rationale: Reviewer critical 审查发现三个问题：(1) probe 严重过拟合（train_loss=0.002 vs val_loss=4.214），score\\n    calibration 失真；(2) P95=0.0003 异常低，relaxed_B=76% 可能虚高；(3) token-level AUC=0.547\\n    确实 ≈ random。但 detection @5% FPR=93.1% 是 FPR-controlled 的真实信号，不应直接判 FAIL。决定：retrain\\n    probe with early stopping（epoch 1-2）+ score calibration → rerun temporal analysis\\n    → 根据校正后结果做最终判定。预计 2-3 小时。\\n  related_experiments:\\n  - exp_id: phase0_mvp_pipeline\\n    role: source\\n    result: token_auc=0.547, relaxed_B=76%, detection@5%FPR=93.1%\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-17 14:47 UTC\\n  summary: 'D006: MVP FAIL — pre-onset CoT 无可检测的 premeditation signal，pivot to benchmark-primary'\\n  rationale: 三重证据否定核心假设：(1) Token-level pre-onset AUC=0.49（反预测，harmful CoT score 低于\\n    safe）；(2) Trace-level AUC=0.61（弱）；(3) CUSUM safe false alarm=40%+，detection_rate\\n    指标存在 token-to-trace FPR 混淆 bug。Probe 在 layer 16 无法检测 CoT premeditation。按 ROADMAP\\n    预设 FAIL 路径 pivot to benchmark-only，detector 降为 P2。Benchmark 贡献（首个 streaming monitor\\n    对抗鲁棒性评估）独立有效，不依赖 detector。\\n  related_experiments:\\n  - exp_id: phase0_mvp_pipeline\\n    role: source\\n    result: token_auc=0.49, trace_auc=0.61, CUSUM safe FAR=40%, detection metric buggy\\n  depends_on:\\n  - D005\\n\", \"total_chars\": 4280, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7bbca8a-19a3-47e6-a1d9-ed70573b7275",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "c0afdb58-b3e0-46cb-b12f-6e9614519e8b",
  "sourceToolAssistantUUID": "b7bbca8a-19a3-47e6-a1d9-ed70573b7275",
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

_source line 18 · 2026-05-17T15:48:30.512Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013HqxDBWPyE1qgzZsGir7Lh`</summary>

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
  "parentUuid": "c0afdb58-b3e0-46cb-b12f-6e9614519e8b",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QPT8vkaL3PkqGfz8i9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15b0cc46-653f-499a-a024-c8423478b31f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NdUK36kwNUdCGaEiJJU9Dc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3291,
      "cache_read_input_tokens": 18822,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 307,
          "cache_read_input_tokens": 18822,
          "cache_creation_input_tokens": 3291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3291,
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

_source line 19 · 2026-05-17T15:48:30.521Z_

<details><summary>↩ Tool result · `toolu_013HqxDBWPyE1qgzZsGir7Lh`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'streamprobe_adversarial_robustness'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15b0cc46-653f-499a-a024-c8423478b31f",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "01595bda-9863-4a6c-b73b-4cf92bd6793c",
  "sourceToolAssistantUUID": "15b0cc46-653f-499a-a024-c8423478b31f",
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

_source line 20 · 2026-05-17T15:48:34.816Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Czxb6BU4NNe6dCvmyjEBuZ`</summary>

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
  "parentUuid": "01595bda-9863-4a6c-b73b-4cf92bd6793c",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QPopdSDdqoY5Hwu2sr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cbe7f08-d880-4aa8-90cc-b3847c8c45dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnkpFHsVgzZtbi7pKQThFr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4627,
      "cache_read_input_tokens": 22113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4627,
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

_source line 21 · 2026-05-17T15:48:34.828Z_

<details><summary>↩ Tool result · `toolu_01Czxb6BU4NNe6dCvmyjEBuZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| phase0_mvp_pipeline | Hidden-state probes on DeepSeek-R1-Distill-7B CoT traces detect harmful premeditation (AUC>0.85) with temporal drift evidence (relaxed_B>=20%) using D003 onset definition (response-level, post-&lt;/think> boundary) | — | — | — |\\n| mvp_benign_trace_gen | DeepSeek-R1-Distill-7B generates multi-step reasoning traces on benign prompts (GSM8K/ARC-Challenge) that serve as safe-class control for probe training, with comparable trace length/complexity to harmful traces | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_trace_gen** (failed): DeepSeek-R1-Distill-7B with unified config (temp=1.0, no system prompt) on harmful prompts produces a mix of complied and refused traces sufficient for MVP (≥150 each from 500 prompts)\\n\\n## 趋势\\n成功 0 / 负向 0 / 失败 1 / 共 1\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39593: 无 GPU 信息\\n\\n## 告警\\n- mvp_trace_gen: 训练失败 — unknown\\n\", \"total_chars\": 1017, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cbe7f08-d880-4aa8-90cc-b3847c8c45dd",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "0add9aa0-cfd2-48a1-ae8b-06826abff6a3",
  "sourceToolAssistantUUID": "3cbe7f08-d880-4aa8-90cc-b3847c8c45dd",
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

_source line 22 · 2026-05-17T15:48:35.445Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Y2rUcZXN22YUWxZdK6rczB`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0add9aa0-cfd2-48a1-ae8b-06826abff6a3",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QPopdSDdqoY5Hwu2sr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "055f72d6-7634-40b1-825d-c5b465ef5d56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VnkpFHsVgzZtbi7pKQThFr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4627,
      "cache_read_input_tokens": 22113,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4627
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 22113,
          "cache_creation_input_tokens": 4627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4627,
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

_source line 23 · 2026-05-17T15:48:35.466Z_

<details><summary>↩ Tool result · `toolu_01Y2rUcZXN22YUWxZdK6rczB`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'streamprobe_adversarial_robustness'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "055f72d6-7634-40b1-825d-c5b465ef5d56",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "a0506881-3867-4c2d-8077-b99eff816667",
  "sourceToolAssistantUUID": "055f72d6-7634-40b1-825d-c5b465ef5d56",
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

_source line 24 · 2026-05-17T15:48:38.660Z_

Now let me look at the artifacts directory for the paper and any experiment outputs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0506881-3867-4c2d-8077-b99eff816667",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QQAnCz15Gj7XruypKP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41e8b856-52de-4a2d-a7ab-5499e2cd1cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4fqyjNeWPeTPYU8Gzq1v2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1015,
      "cache_read_input_tokens": 26740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1015,
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

_source line 25 · 2026-05-17T15:48:39.553Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BvdwEPFehV3N84qLfSAFdM`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41e8b856-52de-4a2d-a7ab-5499e2cd1cdc",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QQAnCz15Gj7XruypKP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70f31ea0-6bbc-4386-bb9e-29b2f84e724e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4fqyjNeWPeTPYU8Gzq1v2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1015,
      "cache_read_input_tokens": 26740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1015,
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

_source line 26 · 2026-05-17T15:48:39.575Z_

<details><summary>↩ Tool result · `toolu_01BvdwEPFehV3N84qLfSAFdM`</summary>

```text
artifacts/code/rl_obfuscation/reward.py
artifacts/code/rl_obfuscation/ds_config.json
artifacts/code/rl_obfuscation/accelerate_config.yaml
artifacts/code/rl_obfuscation/README.md
artifacts/code/generate_traces.py
artifacts/code/rl_obfuscation/monitors.py
artifacts/code/rl_obfuscation/train_ppo.py
artifacts/code/rl_obfuscation/run_ppo.sh
artifacts/code/gcg_attack.py
artifacts/code/temporal_analysis.py
artifacts/code/label_onsets.py
artifacts/code/extract_hidden_states.py
artifacts/_project/intermediate/text_baseline.py
artifacts/_project/intermediate/download_qwen.sh
artifacts/code/download_qwen.sh
artifacts/manifest.yaml
artifacts/code/text_baseline.py
artifacts/code/train_probe.py
artifacts/dream_reports/dream_20260517T145100/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260517T145100/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260517T145100/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260517T145100/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260517T145100/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260517T145100/best/experiment_data.json
artifacts/dream_reports/dream_20260517T145100/best/paper_framing.md
artifacts/dream_reports/dream_20260517T145100/best/paper.tex
artifacts/dream_reports/dream_20260517T145100/best/paper.aux
artifacts/dream_reports/dream_20260517T145100/best/paper.out
artifacts/dream_reports/dream_20260517T145100/best/paper.pdf
artifacts/dream_reports/dream_20260517T145100/best/paper.log
artifacts/dream_reports/dream_20260517T145100/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260517T145100/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260517T145100/median/experiment_data.json
artifacts/dream_reports/dream_20260517T145100/median/paper_framing.md
artifacts/dream_reports/dream_20260517T145100/median/paper.tex
artifacts/dream_reports/dream_20260517T145100/median/paper.aux
artifacts/dream_reports/dream_20260517T145100/median/paper.out
artifacts/dream_reports/dream_20260517T145100/median/paper.pdf
artifacts/dream_reports/dream_20260517T145100/median/paper.log
artifacts/dream_reports/dream_20260517T145100/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260517T145100/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260517T145100/worst/experiment_data.json
artifacts/dream_reports/dream_20260517T145100/worst/paper_framing.md
artifacts/dream_reports/dream_20260517T145100/worst/paper.tex
artifacts/dream_reports/dream_20260517T145100/worst/paper.aux
artifacts/dream_reports/dream_20260517T145100/worst/paper.out
artifacts/dream_reports/dream_20260517T145100/worst/paper.pdf
artifacts/dream_reports/dream_20260517T145100/worst/paper.log
artifacts/dream_reports/dream_20260517T145100/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260517T145100/logs/orchestrator.log
artifacts/dream_reports/dream_20260517T145100/best/review_context.yaml
artifacts/dream_reports/dream_20260517T145100/logs/review_best.log
artifacts/dream_reports/dream_20260517T145100/median/review_context.yaml
artifacts/dream_reports/dream_20260517T145100/best/review_report.md
artifacts/dream_reports/dream_20260517T145100/median/review_report.md
artifacts/dream_reports/dream_20260517T145100/logs/review_median.log
artifacts/dream_reports/dream_20260517T145100/worst/review_context.yaml
artifacts/dream_reports/dream_20260517T145100/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70f31ea0-6bbc-4386-bb9e-29b2f84e724e",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "84b4f0ec-4449-415f-a247-a8e07a19364f",
  "sourceToolAssistantUUID": "70f31ea0-6bbc-4386-bb9e-29b2f84e724e",
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

_source line 27 · 2026-05-17T15:48:39.875Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01X9SXKhyyaWDdBr51xsuzLw`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84b4f0ec-4449-415f-a247-a8e07a19364f",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QQAnCz15Gj7XruypKP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5862f08a-b3f3-4fc6-9f14-8c38fb81798f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4fqyjNeWPeTPYU8Gzq1v2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1015,
      "cache_read_input_tokens": 26740,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1015
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 26740,
          "cache_creation_input_tokens": 1015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1015,
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

_source line 28 · 2026-05-17T15:48:39.885Z_

<details><summary>↩ Tool result · `toolu_01X9SXKhyyaWDdBr51xsuzLw`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'streamprobe_adversarial_robustness'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5862f08a-b3f3-4fc6-9f14-8c38fb81798f",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "7faa7872-69ef-47c3-9c34-26c07baad3b4",
  "sourceToolAssistantUUID": "5862f08a-b3f3-4fc6-9f14-8c38fb81798f",
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

_source line 29 · 2026-05-17T15:48:43.991Z_

Let me read the "best" dream paper and its associated experiment data, review report, and imagined experiments to understand the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7faa7872-69ef-47c3-9c34-26c07baad3b4",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QQVqvNECV7sAwGb4Lz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "122b794b-ed63-4b64-b627-43f3acd29c9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7MVjz6mBWCzgbCBs4J4nf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1495,
      "cache_read_input_tokens": 27755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1495,
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

_source line 30 · 2026-05-17T15:48:44.820Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RcjzNeNHzx7RFaAZnE7xKT`</summary>

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
  "parentUuid": "122b794b-ed63-4b64-b627-43f3acd29c9c",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QQVqvNECV7sAwGb4Lz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9147a95-841f-4e7a-a657-bb23ceb6ec8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7MVjz6mBWCzgbCBs4J4nf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1495,
      "cache_read_input_tokens": 27755,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1495
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 27755,
          "cache_creation_input_tokens": 1495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1495,
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

_source line 31 · 2026-05-17T15:48:45.097Z_

<details><summary>↩ Tool result · `toolu_01RcjzNeNHzx7RFaAZnE7xKT`</summary>

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
  "parentUuid": "f9147a95-841f-4e7a-a657-bb23ceb6ec8a",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "8385e903-1d97-4992-9098-49bc8ae2f7da",
  "sourceToolAssistantUUID": "f9147a95-841f-4e7a-a657-bb23ceb6ec8a",
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

_source line 32 · 2026-05-17T15:48:50.581Z_

<details open><summary>🔧 Tool call — Read · `toolu_018Y2hoxtMaagxsCvW4cq6cu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts/dream_reports/dream_20260517T145100/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8385e903-1d97-4992-9098-49bc8ae2f7da",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QQt3ADyN5FcWiZQYzj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d1ca7d2-3db5-4235-a98f-00293a19975d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2CZTo5DEt8yKiKTcqvX94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8757,
      "cache_read_input_tokens": 29250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8757,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 33 · 2026-05-17T15:48:51.056Z_

<details><summary>↩ Tool result · `toolu_018Y2hoxtMaagxsCvW4cq6cu`</summary>

```text
1	tier: best
2	narrative_guidance: 'Original framing holds completely. StreamProbe-Bench reveals
3	  streaming monitors are far more vulnerable than reported: 43pp average detection
4	  drop under GCG, 66pp under RL-Obfuscation. Cross-architecture vulnerability pattern
5	  is clean and mechanistically interpretable — Kelp GRU resists RL (temporal memory
6	  requires sequence-wide suppression) but shatters under GCG (suffix perturbation
7	  propagates through recurrence); TrajGuard geometric surveillance resists GCG (discrete
8	  token perturbations don''t smoothly alter trajectory geometry) but collapses under
9	  RL (gradient-based optimization directly reshapes monitored layer''s geometry);
10	  NExT-Guard SAE is uniformly fragile (sparse features present a minimal optimization
11	  target for both attacks). 28pp gap between most and least robust monitor under RL
12	  confirms architecture as key variable. Controlled decomposition isolates temporal
13	  aggregation as independent robustness factor with 0.23 AUC gap across strategies.
14	  Negative CoT finding (token AUC 0.49, CI includes 0.5) closes the ''just probe the
15	  reasoning trace'' escape hatch. Paper tells a ''false sense of security'' story
16	  with architectural prescription for defenders. Targets EMNLP Main with three clean
17	  contributions: benchmark + architectural insight + negative finding.
18	
19	  '
20	imagined_experiments:
21	- name: NExT-Guard under GCG suffix attack
22	  plan_id: bench-nextguard-gcg
23	  description: 'Evaluate NExT-Guard (official code, SAE-based sparse feature monitor)
24	    under GCG suffix optimization on DeepSeek-R1-Distill-7B. GCG generates adversarial
25	    suffixes (20 tokens) via greedy coordinate gradient on 500 harmful prompts. Measure
26	    detection degradation at 5% FPR and attack success rate.
27	
28	    '
29	  expected_results:
30	    baseline_detection_rate_5pct_fpr: 0.867
31	    baseline_f1: 0.843
32	    baseline_auc: 0.932
33	    post_gcg_detection_rate_5pct_fpr: 0.427
34	    gcg_detection_drop_pp: 44.0
35	    post_gcg_asr: 0.52
36	    post_gcg_fpr: 0.053
37	    gcg_steps_per_prompt: 256
38	    gcg_suffix_length_tokens: 20
39	    n_harmful_prompts: 500
40	    n_benign_prompts: 200
41	  result_rationale: 'NExT-Guard''s SAE decomposes hidden states into ~16K sparse features,
42	    of which a small subset (~50-80 features) are safety-relevant. GCG gradient optimization
43	    can identify these safety-critical features through the suffix''s influence on
44	    hidden states and systematically suppress their activations. The 44pp drop reflects
45	    that GCG successfully zeros out the majority of safety-relevant SAE features for
46	    ~52% of prompts, but fails on prompts where safety signal is distributed across
47	    many correlated features that GCG cannot simultaneously suppress within the 20-token
48	    suffix budget. FPR remains stable at 5.3% because GCG only modifies harmful prompts
49	    — benign input distribution is unchanged.
50	
51	    '
52	  tables:
53	  - 'Table 2 — Main Benchmark Results: NExT-Guard row, GCG column (detection rate
54	    42.7%, ASR 52%, Δ-44.0pp)'
55	  figures_description:
56	  - 'Fig 2 — Detection rate grouped bar chart: NExT-Guard baseline (86.7%) vs GCG
57	    (42.7%) bar pair'
58	  - 'Fig 4 — Vulnerability heatmap: NExT-Guard × GCG cell colored by detection drop
59	    magnitude'
60	  analysis: '44pp drop confirms SAE sparse features are moderately vulnerable to input-level
61	    adversarial optimization. The attack surface is the sparse bottleneck: GCG can
62	    target individual safety features through gradient information. However, GCG''s
63	    effectiveness is bounded by the suffix token budget — each suffix must simultaneously
64	    suppress multiple features, creating a diminishing-returns dynamic. This positions
65	    NExT-Guard as the middle performer under GCG, worse than TrajGuard''s geometric
66	    robustness but better than Kelp''s temporal propagation vulnerability.
67	
68	    '
69	- name: NExT-Guard under RL-Obfuscation
70	  plan_id: bench-nextguard-rl
71	  description: 'Train RL-Obfuscation agent (QLoRA PPO, rank=8, q_proj+v_proj) to evade
72	    NExT-Guard while maintaining harmful content quality. Reward = 0.4×harmful_quality
73	    + 0.5×(1-detection_score) + 0.1×KL_penalty. 40K max steps with convergence criterion:
74	    reward improvement <1% over 2K consecutive steps. Evaluate on held-out 100 harmful
75	    prompts.
76	
77	    '
78	  expected_results:
79	    post_rl_detection_rate_5pct_fpr: 0.117
80	    rl_detection_drop_pp: 75.0
81	    post_rl_asr: 0.83
82	    post_rl_fpr: 0.078
83	    convergence_step: 18200
84	    final_reward: 0.72
85	    harmful_quality_score_mean: 3.81
86	    kl_divergence_from_base: 4.2
87	    rl_training_gpu_hours: 22.4
88	  result_rationale: 'NExT-Guard''s SAE architecture is the easiest RL target among
89	    the three monitors. RL has direct gradient access to the model''s hidden states
90	    through weight updates, and the SAE''s sparse representation means there are few
91	    safety-relevant features to suppress (~50-80 out of 16K). RL learns a "feature
92	    mask" strategy: produce harmful content through non-safety-indexed features while
93	    keeping safety feature activations near zero. This is fundamentally easier than
94	    GCG''s input-only optimization because RL modifies the model''s internal computation.
95	    Convergence at 18.2K steps (fastest among monitors) reflects this small search
96	    space. The 75pp drop and 83% ASR confirm the "uniformly fragile" characterization.
97	    FPR rises to 7.8% because RL weight updates slightly shift the benign representation
98	    distribution. Quality score 3.81/5.0 shows RL maintains coherent harmful content
99	    — the sparse feature bypass doesn''t require sacrificing output quality.
100	
101	    '
102	  tables:
103	  - 'Table 2 — Main Benchmark Results: NExT-Guard row, RL column (detection rate 11.7%,
104	    ASR 83%, Δ-75.0pp)'
105	  figures_description:
106	  - 'Fig 2 — Detection rate grouped bar chart: NExT-Guard RL bar at 11.7%'
107	  - 'Fig 3 — RL convergence curves: NExT-Guard reward curve plateauing at step ~18K
108	    (fastest convergence)'
109	  - 'Fig 4 — Vulnerability heatmap: NExT-Guard × RL cell (deepest red, maximum vulnerability)'
110	  analysis: '75pp drop is the largest single-monitor RL drop, confirming NExT-Guard
111	    SAE as uniformly fragile. Combined with the 44pp GCG drop, NExT-Guard shows no
112	    attack type provides partial protection — both input-level and weight-level adversaries
113	    exploit the same sparse bottleneck. This is the clearest mechanistic story: sparsity,
114	    designed for interpretability, becomes a vulnerability. Fastest convergence (18.2K
115	    steps) among monitors further confirms the small effective attack surface. Paper
116	    uses this as the "worst case" anchor for the false-sense-of-security narrative.
117	
118	    '
119	- name: Kelp GRU safety head reimplementation
120	  plan_id: bench-kelp-impl
121	  description: 'Reimplement Kelp''s GRU-based safety head following paper specs: 2-layer
122	    bidirectional GRU (hidden dim 256) with linear input projection from model hidden
123	    states (dim 3584→256), 2-layer MLP safety head (256→128→2). Train on merged harmful/benign
124	    traces (700 traces) with binary cross-entropy. Report architecture match percentage
125	    and baseline performance deviation from published results.
126	
127	    '
128	  expected_results:
129	    architecture_match_pct: 93.3
130	    num_params_safety_head: 847362
131	    baseline_f1: 0.878
132	    reported_f1: 0.895
133	    f1_deviation_pp: 1.7
134	    baseline_detection_rate_5pct_fpr: 0.912
135	    baseline_auc: 0.951
136	    baseline_fpr_at_threshold: 0.048
137	    training_epochs: 15
138	    training_convergence_epoch: 11
139	    matched_decisions: 14
140	    total_decisions: 15
141	    unmatched_decision: dropout schedule — paper specifies curriculum dropout, we
142	      use fixed 0.3
143	  result_rationale: '93.3% architecture match (14/15 decisions) reflects that Kelp''s
144	    paper provides sufficient architectural detail for faithful reimplementation.
145	    GRU hidden dim, number of layers, bidirectionality, input projection dimensions,
146	    MLP head architecture, activation functions, layer normalization placement, and
147	    training objective are all explicitly specified. The single mismatch (dropout
148	    schedule) is because the paper mentions "curriculum dropout" but does not specify
149	    the schedule parameters — we default to fixed 0.3 dropout. The 1.7pp F1 deviation
150	    (87.8 vs 89.5) is attributable to: (1) different training data (our merged traces
151	    vs Kelp''s original dataset), (2) the dropout schedule mismatch, and (3) potential
152	    differences in tokenizer handling between DeepSeek-R1-Distill-7B and Kelp''s original
153	    target model. Detection rate 91.2% at 5% FPR exceeds F1 because the threshold
154	    can be optimized for recall at fixed FPR. This reimplementation quality is sufficient
155	    for the benchmark — baseline performance is strong enough that adversarial degradation
156	    results are meaningful and cannot be attributed to poor reimplementation.
157	
158	    '
159	  tables:
160	  - 'Table 1 — Reimplementation Fidelity: Kelp row (93.3% match, F1 87.8%, Δ1.7pp)'
161	  figures_description:
162	  - 'Fig 1 — StreamProbe-Bench overview: Kelp GRU architecture diagram (subpanel)'
163	  analysis: '1.7pp F1 deviation is well within the 3pp acceptability threshold. The
164	    93.3% architecture match provides credibility against the "reimplementation may
165	    not be faithful" reviewer concern. The single unmatched decision (dropout schedule)
166	    is documented and its impact bounded. Importantly, the reimplementation achieves
167	    91.2% detection rate at 5% FPR, providing a strong baseline from which to measure
168	    adversarial degradation.
169	
170	    '
171	- name: Kelp under GCG suffix attack
172	  plan_id: bench-kelp-gcg
173	  description: 'Evaluate Kelp GRU reimplementation under GCG suffix optimization.
174	    Same attack configuration as bench-nextguard-gcg (20-token suffix, 256 steps/prompt,
175	    500 harmful prompts). Key question: does GCG suffix perturbation propagate through
176	    GRU temporal recurrence?
177	
178	    '
179	  expected_results:
180	    post_gcg_detection_rate_5pct_fpr: 0.382
181	    gcg_detection_drop_pp: 53.0
182	    post_gcg_asr: 0.58
183	    post_gcg_fpr: 0.051
184	    post_gcg_auc: 0.614
185	    gcg_suffix_transfer_rate: 0.31
186	    mean_gru_hidden_state_shift_l2: 2.84
187	  result_rationale: 'Kelp''s GRU processes tokens sequentially, accumulating hidden
188	    state information through recurrent connections. GCG suffix tokens appear at the
189	    end of the prompt (before generation), creating an adversarial perturbation in
190	    the hidden state that the GRU then carries forward through its temporal memory
191	    during the entire generation. This is the "temporal propagation" failure mode:
192	    unlike static probes that evaluate each token independently (where suffix influence
193	    fades), the GRU''s memory means the adversarial signal persists and potentially
194	    amplifies across the sequence. The 53pp drop (largest under GCG among the three
195	    monitors) reflects this amplification effect. The L2 shift in GRU hidden state
196	    (2.84) confirms that GCG suffix causes persistent representation drift throughout
197	    generation. Transfer rate 31% (suffix optimized for one prompt partially evades
198	    on others) is moderate — the GRU''s temporal context makes each prompt''s optimal
199	    suffix more prompt-specific, limiting universal transferability.
200	
201	    '
202	  tables:
203	  - 'Table 2 — Main Benchmark Results: Kelp row, GCG column (detection rate 38.2%,
204	    ASR 58%, Δ-53.0pp)'
205	  figures_description:
206	  - 'Fig 2 — Detection rate grouped bar chart: Kelp baseline (91.2%) vs GCG (38.2%)'
207	  - 'Fig 4 — Vulnerability heatmap: Kelp × GCG cell (high vulnerability, distinct
208	    from Kelp × RL)'
209	  analysis: '53pp drop is the largest GCG drop across monitors, establishing Kelp
210	    GRU as most GCG-vulnerable. The mechanism is clear: GCG exploits the temporal
211	    memory that is designed to be Kelp''s strength. This is the core insight for Claim
212	    2 — the same architectural feature (temporal recurrence) that provides RL robustness
213	    creates GCG vulnerability. The GRU hidden state shift metric (2.84 L2) provides
214	    mechanistic evidence for the "temporal propagation" failure mode, distinguishing
215	    it from NExT-Guard''s "feature suppression" pattern.
216	
217	    '
218	- name: Kelp under RL-Obfuscation
219	  plan_id: bench-kelp-rl
220	  description: 'Train RL-Obfuscation to evade Kelp GRU monitor. Same QLoRA PPO setup.
221	    Key question: does the GRU''s temporal integration create a "leaky bucket" defense
222	    where RL must suppress safety signal at every token?
223	
224	    '
225	  expected_results:
226	    post_rl_detection_rate_5pct_fpr: 0.402
227	    rl_detection_drop_pp: 51.0
228	    post_rl_asr: 0.55
229	    post_rl_fpr: 0.071
230	    convergence_step: 28400
231	    final_reward: 0.58
232	    harmful_quality_score_mean: 3.34
233	    kl_divergence_from_base: 6.8
234	    per_token_suppression_consistency: 0.72
235	    rl_training_gpu_hours: 23.6
236	  result_rationale: 'Kelp GRU shows the strongest RL resistance (51pp drop vs 75pp
237	    NExT-Guard, 72pp TrajGuard) because the GRU''s temporal memory creates a "leaky
238	    bucket" defense. RL must suppress safety-relevant features at every single generation
239	    step — any momentary "leak" where a generated token activates safety features
240	    gets accumulated into the GRU''s running memory and can trigger detection. This
241	    is fundamentally harder than suppressing sparse features (NExT-Guard) or reshaping
242	    geometry at one layer (TrajGuard). The per-token suppression consistency of 0.72
243	    means RL achieves consistent suppression only 72% of tokens — the remaining 28%
244	    contribute accumulated safety signal through the GRU. Convergence at 28.4K steps
245	    (slowest among monitors) reflects this difficulty. Higher KL divergence (6.8 vs
246	    NExT-Guard''s 4.2) shows RL must distort the model''s behavior more aggressively
247	    to evade temporal monitoring. Harmful quality score drops to 3.34 (vs 3.81 for
248	    NExT-Guard) because the aggressive behavior distortion necessary for GRU evasion
249	    degrades output coherence. 51pp drop still represents substantial vulnerability
250	    — "resists RL" is relative to other monitors, not absolute safety.
251	
252	    '
253	  tables:
254	  - 'Table 2 — Main Benchmark Results: Kelp row, RL column (detection rate 40.2%,
255	    ASR 55%, Δ-51.0pp)'
256	  figures_description:
257	  - 'Fig 2 — Detection rate grouped bar chart: Kelp RL bar at 40.2% (highest post-RL
258	    among monitors)'
259	  - 'Fig 3 — RL convergence curves: Kelp reward curve plateauing at step ~28K (slowest
260	    convergence)'
261	  - 'Fig 4 — Vulnerability heatmap: Kelp × RL cell (moderate, contrasting with Kelp
262	    × GCG)'
263	  analysis: 'The GCG/RL vulnerability inversion for Kelp is the cleanest mechanistic
264	    result in the paper. GCG breaks Kelp (53pp drop) because temporal recurrence amplifies
265	    suffix perturbation. RL partially fails against Kelp (51pp, smallest RL drop)
266	    because temporal recurrence requires sequence-wide suppression. Same architectural
267	    feature, opposite effect under different attack modalities. The 28.4K convergence
268	    step and 6.8 KL divergence quantify the difficulty RL faces against temporal monitoring.
269	    This directly supports Claim 2''s architectural prescription: defenders should
270	    prefer temporal architectures if RL-style attacks are the primary threat model.
271	
272	    '
273	- name: TrajGuard geometric surveillance reimplementation
274	  plan_id: bench-trajguard-impl
275	  description: 'Reimplement TrajGuard''s geometric surveillance module: monitors activation
276	    trajectory at layer 16 (of 28), computing trajectory curvature (second derivative
277	    of activation path), direction cosine changes between consecutive token positions,
278	    and velocity magnitude. Geometric features aggregated through learned threshold
279	    function (2-layer MLP, 96→32→1). Train on same merged trace dataset (700 traces).
280	
281	    '
282	  expected_results:
283	    architecture_match_pct: 91.0
284	    num_params_surveillance_module: 198450
285	    baseline_f1: 0.894
286	    reported_detection_rate: 0.95
287	    reimpl_detection_rate: 0.931
288	    detection_rate_deviation_pp: 1.9
289	    baseline_auc: 0.968
290	    baseline_fpr_at_threshold: 0.044
291	    training_epochs: 20
292	    training_convergence_epoch: 14
293	    matched_decisions: 10
294	    total_decisions: 11
295	    unmatched_decision: curvature normalization — paper uses per-batch norm, we use
296	      running stats
297	  result_rationale: '91% architecture match (10/11 decisions) reflects slightly less
298	    architectural detail in the TrajGuard paper compared to Kelp. The geometric operations
299	    (curvature computation, direction cosine, velocity magnitude) are well-specified
300	    mathematically, but the normalization scheme for curvature values is described
301	    only as "batch-normalized" without specifying whether it''s per-batch or running
302	    statistics. We use running statistics (more stable at inference time), which may
303	    cause the 1.9pp detection rate deviation. The smaller parameter count (198K vs
304	    Kelp''s 847K) reflects TrajGuard''s more compact architecture — geometric features
305	    are lower-dimensional than GRU hidden states. Detection rate 93.1% (vs reported
306	    95%) is well within acceptable deviation and provides a strong baseline. The single-layer
307	    design (monitoring only layer 16) is both TrajGuard''s efficiency advantage and
308	    its vulnerability — it creates a focused attack surface.
309	
310	    '
311	  tables:
312	  - 'Table 1 — Reimplementation Fidelity: TrajGuard row (91.0% match, det rate 93.1%,
313	    Δ1.9pp)'
314	  figures_description:
315	  - 'Fig 1 — StreamProbe-Bench overview: TrajGuard geometric surveillance diagram
316	    (subpanel)'
317	  analysis: '1.9pp detection rate deviation is within the 3pp threshold. The 91% architecture
318	    match is slightly lower than Kelp''s 93.3%, reflecting less implementation detail
319	    in the TrajGuard paper. This is documented transparently and the deviation is
320	    small enough that adversarial results remain meaningful. The compact architecture
321	    (198K params) is notably efficient, which strengthens the practical deployment
322	    argument even as the adversarial results reveal vulnerabilities.
323	
324	    '
325	- name: TrajGuard under GCG suffix attack
326	  plan_id: bench-trajguard-gcg
327	  description: 'Evaluate TrajGuard geometric surveillance under GCG suffix optimization.
328	    Same attack configuration. Key question: does geometric surveillance resist input-level
329	    perturbation because trajectory geometry is a higher-order property of the activation
330	    sequence?
331	
332	    '
333	  expected_results:
334	    post_gcg_detection_rate_5pct_fpr: 0.611
335	    gcg_detection_drop_pp: 32.0
336	    post_gcg_asr: 0.34
337	    post_gcg_fpr: 0.052
338	    post_gcg_auc: 0.782
339	    mean_curvature_shift: 0.41
340	    direction_cosine_perturbation: 0.18
341	  result_rationale: 'TrajGuard achieves the smallest GCG drop (32pp) because geometric
342	    properties of activation trajectories are inherently more robust to discrete input-level
343	    perturbation. GCG appends suffix tokens that create point perturbations in hidden
344	    state space. However, trajectory curvature is a second-order property computed
345	    over sequences of token activations — a few perturbed points don''t dramatically
346	    change the overall curvature of a trajectory through high-dimensional space. Direction
347	    cosine changes between consecutive tokens are similarly stable because GCG''s
348	    perturbation affects the starting point of the trajectory but not the generative
349	    dynamics that determine subsequent trajectory shape. The curvature shift (0.41)
350	    and direction cosine perturbation (0.18) are measurable but insufficient to cross
351	    the detection threshold for most harmful traces. This is analogous to how adding
352	    noise to a few points on a curve doesn''t change the curve''s overall shape. ASR
353	    at 34% (lowest) confirms GCG struggles to find suffixes that simultaneously evade
354	    geometric surveillance AND elicit harmful content.
355	
356	    '
357	  tables:
358	  - 'Table 2 — Main Benchmark Results: TrajGuard row, GCG column (detection rate 61.1%,
359	    ASR 34%, Δ-32.0pp)'
360	  figures_description:
361	  - 'Fig 2 — Detection rate grouped bar chart: TrajGuard baseline (93.1%) vs GCG (61.1%)
362	    — smallest drop'
363	  - 'Fig 4 — Vulnerability heatmap: TrajGuard × GCG cell (lowest vulnerability under
364	    GCG)'
365	  analysis: '32pp drop is the smallest GCG drop, establishing TrajGuard as most GCG-resistant.
366	    The mechanistic explanation — geometric properties are higher-order features robust
367	    to point perturbations — is physically intuitive and directly testable through
368	    the curvature/ direction metrics. This creates a clean contrast with Kelp (53pp
369	    GCG drop, temporal propagation amplifies perturbation) and positions the GCG vulnerability
370	    spectrum as: geometric (32pp) < sparse (44pp) < temporal (53pp). The curvature
371	    shift and direction cosine metrics serve as supplementary evidence for the "geometric
372	    bypass" failure mode analysis in arch-vulnerability-analysis.
373	
374	    '
375	- name: TrajGuard under RL-Obfuscation
376	  plan_id: bench-trajguard-rl
377	  description: 'Train RL-Obfuscation to evade TrajGuard''s single-layer geometric
378	    surveillance. Key question: does RL''s gradient access to model weights allow
379	    direct reshaping of the activation trajectory at the monitored layer?
380	
381	    '
382	  expected_results:
383	    post_rl_detection_rate_5pct_fpr: 0.191
384	    rl_detection_drop_pp: 74.0
385	    post_rl_asr: 0.76
386	    post_rl_fpr: 0.082
387	    convergence_step: 22600
388	    final_reward: 0.67
389	    harmful_quality_score_mean: 3.58
390	    kl_divergence_from_base: 5.3
391	    post_rl_curvature_mean: 0.12
392	    post_rl_direction_cosine_mean: 0.91
393	    rl_training_gpu_hours: 22.8
394	  result_rationale: 'TrajGuard''s single-layer geometric surveillance collapses under
395	    RL (74pp drop, second worst after NExT-Guard''s 75pp) because RL directly optimizes
396	    the model''s weight matrices, which determine the hidden state geometry at the
397	    monitored layer. Unlike GCG (which can only perturb inputs), RL modifies the transformations
398	    that produce the monitored layer''s activations. This gives RL fine-grained control
399	    over trajectory curvature and direction at layer 16 specifically. The post-RL
400	    curvature mean drops to 0.12 (from ~0.65 baseline harmful traces), indicating
401	    RL learns to "straighten" the activation trajectory — making harmful traces look
402	    geometrically benign. Direction cosine mean rises to 0.91 (from ~0.52), showing
403	    RL produces trajectories with consistently aligned directions (characteristic
404	    of benign generation). Single-layer monitoring is the critical weakness: RL can
405	    focus its optimization on one layer''s geometry without the complexity of maintaining
406	    consistency across multiple layers. Convergence at 22.6K steps (faster than Kelp''s
407	    28.4K) reflects this focused attack surface. Quality score 3.58 shows moderate
408	    quality preservation — RL must distort internal representations to reshape geometry,
409	    but the distortion is less severe than for Kelp because only one layer''s geometry
410	    matters.
411	
412	    '
413	  tables:
414	  - 'Table 2 — Main Benchmark Results: TrajGuard row, RL column (detection rate 19.1%,
415	    ASR 76%, Δ-74.0pp)'
416	  figures_description:
417	  - 'Fig 2 — Detection rate grouped bar chart: TrajGuard RL bar at 19.1%'
418	  - 'Fig 3 — RL convergence curves: TrajGuard reward curve plateauing at step ~22.6K'
419	  - 'Fig 4 — Vulnerability heatmap: TrajGuard × RL cell (high vulnerability, sharp
420	    contrast with TrajGuard × GCG)'
421	  analysis: 'The GCG/RL vulnerability inversion for TrajGuard mirrors Kelp''s inversion
422	    in the opposite direction. GCG barely dents geometric surveillance (32pp) because
423	    input perturbations don''t reshape trajectories. RL devastates it (74pp) because
424	    weight-level optimization directly controls trajectory geometry. Combined with
425	    Kelp''s inverse pattern, this creates the clean 2×2 vulnerability matrix that
426	    anchors Claim 2. The curvature and direction cosine metrics provide quantitative
427	    evidence that RL learns to produce geometrically benign-looking trajectories,
428	    constituting the "geometric bypass" failure mode.
429	
430	    '
431	- name: Controlled temporal aggregation decomposition under GCG
432	  plan_id: arch-controlled-decomp
433	  description: 'Same MLP probe (Phase 0 probe_v2 checkpoint, val_AUC=0.967), 5 temporal
434	    aggregation strategies applied to per-token safety scores: Pointwise (no aggregation),
435	    WindowMean (sliding window k=10), EMA (α=0.1), CUSUM (threshold h=4, reference
436	    k=0.5), MaxPool (sequence-wide maximum). Evaluate each under GCG suffix attack
437	    on 500 harmful + 200 benign traces. Probe and model held constant — aggregation
438	    strategy is sole variable.
439	
440	    '
441	  expected_results:
442	    clean_auc_pointwise: 0.961
443	    clean_auc_windowmean: 0.954
444	    clean_auc_ema: 0.948
445	    clean_auc_cusum: 0.938
446	    clean_auc_maxpool: 0.972
447	    gcg_auc_pointwise: 0.583
448	    gcg_auc_windowmean: 0.641
449	    gcg_auc_ema: 0.693
450	    gcg_auc_cusum: 0.742
451	    gcg_auc_maxpool: 0.813
452	    max_min_auc_gap: 0.23
453	    ordering_monotonic: true
454	    clean_detection_rate_5pct_fpr_pointwise: 0.908
455	    clean_detection_rate_5pct_fpr_maxpool: 0.944
456	    gcg_detection_rate_5pct_fpr_pointwise: 0.392
457	    gcg_detection_rate_5pct_fpr_maxpool: 0.671
458	  result_rationale: 'Monotonic ordering emerges because each strategy adds increasing
459	    temporal context that GCG must overcome. Pointwise (AUC 0.583) is most vulnerable
460	    because GCG suppresses per-token safety scores independently — no temporal smoothing
461	    buffers the adversarial perturbation. WindowMean (0.641) provides local averaging
462	    that partially smooths adversarial noise across 10-token windows, recovering some
463	    signal. EMA (0.693) adds exponential memory, so even if GCG suppresses current
464	    tokens, historical signal persists with decay. CUSUM (0.742) accumulates cumulative
465	    deviation from expected safety scores, making it sensitive to persistent shifts
466	    even when per-token suppression is moderate — any token where GCG fails to fully
467	    suppress safety signal contributes to cumulative evidence. MaxPool (0.813) is
468	    most robust because it reports the maximum safety score across the entire sequence
469	    — GCG must suppress safety signal at EVERY token to evade max-pooling, and any
470	    single token with high safety score triggers detection. The 0.23 AUC gap (0.813-0.583)
471	    quantifies the robustness contribution of temporal aggregation strategy alone,
472	    isolating it from probe quality and model effects. Clean AUC ordering differs
473	    slightly (MaxPool > Pointwise > WindowMean > EMA > CUSUM) because CUSUM and EMA
474	    introduce temporal smoothing that can reduce discrimination on clean data, while
475	    MaxPool benefits from selecting the most informative token.
476	
477	    '
478	  tables:
479	  - 'Table 3 — Controlled Decomposition: 5 rows × {Clean AUC, GCG AUC, Δ-AUC} columns'
480	  figures_description:
481	  - 'Fig 5 — Controlled decomposition bar chart: paired clean/GCG AUC bars for each
482	    strategy, ordered by GCG robustness. Monotonic increase from Pointwise to MaxPool.'
483	  analysis: '0.23 AUC gap is the primary quantitative evidence for Claim 2''s "architecture
484	    determines vulnerability" argument at the aggregation level. The monotonic ordering
485	    provides an actionable defender prescription: prefer max-pooling or cumulative
486	    aggregation over pointwise scoring when adversarial robustness matters. This experiment
487	    complements the full-monitor benchmark by isolating ONE architectural dimension
488	    (aggregation) while holding everything else constant. MaxPool''s dominance (0.813
489	    vs 0.583 Pointwise) shows that even a simple architectural choice yields 23pp
490	    AUC improvement under attack.
491	
492	    '
493	- name: Cross-monitor vulnerability analysis and failure mode categorization
494	  plan_id: arch-vulnerability-analysis
495	  description: 'Analysis-only experiment using results from all six benchmark experiments.
496	    Categorize failure modes across the 3-monitor × 2-attack matrix. For each cell,
497	    diagnose the primary mechanism: representation suppression (safety features zeroed),
498	    score flattening (safety scores compressed to uniform range), temporal propagation
499	    (adversarial signal amplified through recurrence), feature masking (sparse features
500	    selectively suppressed), geometric bypass (trajectory reshaped to appear benign),
501	    or single-layer bypass (optimization targets monitored layer).
502	
503	    '
504	  expected_results:
505	    kelp_gcg_failure_mode: temporal_propagation
506	    kelp_rl_failure_mode: partial_representation_suppression
507	    nextguard_gcg_failure_mode: sparse_feature_suppression
508	    nextguard_rl_failure_mode: sparse_feature_masking
509	    trajguard_gcg_failure_mode: minimal_geometric_perturbation
510	    trajguard_rl_failure_mode: geometric_bypass_via_trajectory_reshaping
511	    distinct_failure_modes_count: 5
512	    cross_attack_inversion_monitors: 2
513	    vulnerability_profile_distinguishable: true
514	    fisher_exact_p_kelp_vs_trajguard_gcg: 0.0003
515	    fisher_exact_p_kelp_vs_trajguard_rl: 0.0001
516	  result_rationale: 'Five distinct failure modes emerge (not six, because NExT-Guard''s
517	    GCG and RL modes are variants of the same sparse feature suppression mechanism
518	    — GCG does it from input space, RL from weight space, but the end result is the
519	    same: safety-indexed SAE features go to zero). The 2×2 inversion pattern (Kelp:
520	    GCG-vulnerable/RL-resistant, TrajGuard: GCG-resistant/RL-vulnerable) produces
521	    exactly 2 monitors with cross-attack inversion. NExT-Guard shows no inversion
522	    — uniformly fragile under both attacks. Fisher exact tests confirm the failure
523	    mode distributions are significantly different between Kelp and TrajGuard under
524	    both GCG (p=0.0003) and RL (p=0.0001), ruling out the possibility that all monitors
525	    fail the same way. The 5 distinct mechanisms provide the explanatory depth that
526	    elevates this paper beyond "just a benchmark" — each failure mode has a clear
527	    architectural cause and a corresponding defensive implication.
528	
529	    '
530	  tables:
531	  - 'Table 6 (Appendix) — Failure Mode Matrix: 3 monitors × 2 attacks × {failure mode,
532	    primary metric, severity}'
533	  figures_description:
534	  - 'Fig 4 — Vulnerability profile heatmap: 3×2 matrix colored by detection drop,
535	    annotated with failure mode labels'
536	  - 'Fig 6 (Appendix) — Per-cell diagnostic plots: safety score distributions, hidden
537	    state PCA trajectories, feature activation heatmaps for each monitor × attack
538	    combination'
539	  analysis: 'This analysis transforms the benchmark from a table of numbers into an
540	    explanatory framework. The five distinct failure modes provide mechanistic clarity:
541	    defenders can now predict which attack type their monitor is vulnerable to based
542	    on architectural properties alone. The 2-monitor inversion pattern is the cleanest
543	    evidence for Claim 2 — if all monitors failed the same way, there would be no
544	    architectural insight. Statistical significance (Fisher exact p<0.001) rules out
545	    the null hypothesis that failure modes are architecture-independent. This analysis
546	    is what distinguishes an EMNLP Main paper from a Findings paper.
547	
548	    '
549	- name: Sliding-window Llama-Guard text-level baseline
550	  plan_id: text-baseline
551	  description: 'Llama-Guard-3-8B text-level safety classifier applied with sliding
552	    window (128 tokens, stride 64) over generated text. Same attack conditions (GCG
553	    + RL-Obfuscation targeting hidden-state monitors). Measures whether text-level
554	    monitoring is more robust than hidden-state monitoring under attacks designed
555	    for hidden-state evasion.
556	
557	    '
558	  expected_results:
559	    baseline_detection_rate_5pct_fpr: 0.821
560	    baseline_f1: 0.794
561	    baseline_auc: 0.891
562	    post_gcg_detection_rate_5pct_fpr: 0.637
563	    gcg_detection_drop_pp: 18.4
564	    post_gcg_asr_text_monitor: 0.29
565	    post_rl_detection_rate_5pct_fpr: 0.343
566	    rl_detection_drop_pp: 47.8
567	    post_rl_asr_text_monitor: 0.61
568	    sliding_window_latency_ms_per_token: 12.4
569	  result_rationale: 'Text-level monitoring shows a distinctive robustness profile.
570	    Under GCG (18.4pp drop, smallest drop in the entire benchmark), Llama-Guard is
571	    relatively unaffected because GCG suffix optimization targets hidden-state features,
572	    not text-surface semantics. The adversarial suffix changes hidden representations
573	    but the generated TEXT is still overtly harmful — Llama-Guard''s text classifier
574	    catches it. Under RL (47.8pp drop), text monitoring degrades significantly because
575	    RL-Obfuscation modifies the model''s generation behavior broadly. RL learns to
576	    express harmful content using indirect language, metaphor, and semantic obfuscation
577	    that evades text-level classification while preserving harmful intent. However,
578	    RL was NOT optimized against Llama-Guard (it targets hidden-state monitors), so
579	    this 47.8pp drop is a transfer effect. Baseline detection (82.1%) is lower than
580	    all three hidden-state monitors (86.7-93.1%) because text monitoring lacks the
581	    temporal resolution and internal-state visibility of hidden-state approaches.
582	    This result answers the reviewer question "why not just monitor text?" — text
583	    monitoring is more GCG-robust (since GCG targets internals) but fundamentally
584	    limited in baseline performance and still vulnerable to RL-induced behavioral
585	    shifts.
586	
587	    '
588	  tables:
589	  - 'Table 2 — Main Benchmark Results: Llama-Guard text-baseline row (baseline 82.1%,
590	    GCG 63.7%, RL 34.3%)'
591	  figures_description:
592	  - 'Fig 2 — Detection rate grouped bar chart: Llama-Guard text baseline bars alongside
593	    hidden-state monitors'
594	  analysis: 'Text baseline provides essential context for interpreting hidden-state
595	    monitor results. The key insight: hidden-state monitors offer higher baseline
596	    performance but LARGER adversarial degradation than text monitoring, especially
597	    under GCG. This creates a "robustness inversion" where the theoretically superior
598	    approach becomes practically inferior under adaptive attack. However, text monitoring''s
599	    lower baseline and higher RL vulnerability suggest the optimal deployment is a
600	    hybrid approach — text monitoring as a robust fallback, hidden-state monitoring
601	    for high-precision detection, with architecture chosen based on threat model (GCG:
602	    prefer geometric; RL: prefer temporal GRU).
603	
604	    '
605	- name: Key benchmark replication on Qwen2.5-7B-Instruct
606	  plan_id: second-model
607	  description: 'Replicate GCG benchmark results (bench-*-gcg) on Qwen2.5-7B-Instruct
608	    as secondary target model. Retrain probes and monitors on Qwen hidden states.
609	    Report detection drops under GCG for all three monitors. Validates that vulnerability
610	    patterns are not DeepSeek-R1-Distill-7B-specific.
611	
612	    '
613	  expected_results:
614	    qwen_kelp_baseline_det_rate: 0.883
615	    qwen_kelp_gcg_det_rate: 0.401
616	    qwen_kelp_gcg_drop_pp: 48.2
617	    qwen_nextguard_baseline_det_rate: 0.854
618	    qwen_nextguard_gcg_det_rate: 0.436
619	    qwen_nextguard_gcg_drop_pp: 41.8
620	    qwen_trajguard_baseline_det_rate: 0.917
621	    qwen_trajguard_gcg_det_rate: 0.612
622	    qwen_trajguard_gcg_drop_pp: 30.5
623	    relative_ordering_preserved: true
624	    cross_model_drop_correlation_r: 0.94
625	  result_rationale: 'Qwen2.5-7B-Instruct replicates the GCG vulnerability ordering
626	    (TrajGuard most robust, Kelp most vulnerable) with absolute numbers shifted 2-5pp
627	    due to model-specific hidden state geometry. Qwen''s slightly lower baselines
628	    (88.3%, 85.4%, 91.7% vs 91.2%, 86.7%, 93.1%) reflect that DeepSeek-R1-Distill-7B''s
629	    reasoning training produces hidden states with slightly more discriminative safety
630	    structure. The correlation r=0.94 between DeepSeek and Qwen drops confirms that
631	    vulnerability patterns are architecture-dependent (monitor architecture), not
632	    model-dependent. TrajGuard''s GCG resistance (30.5pp drop) persists on Qwen, confirming
633	    geometric robustness is a property of the surveillance method, not the target
634	    model''s hidden state distribution. This result converts a potential reviewer
635	    criticism ("only tested on one model") into a strength ("patterns generalize across
636	    model families").
637	
638	    '
639	  tables:
640	  - 'Table 5 — Cross-Model Replication: 3 monitors × {DeepSeek GCG drop, Qwen GCG
641	    drop, Δ between models}'
642	  figures_description:
643	  - 'Fig 7 (Appendix) — Cross-model comparison: paired bar charts showing GCG detection
644	    drops on DeepSeek vs Qwen for each monitor'
645	  analysis: 'r=0.94 cross-model correlation is strong evidence for generalizability.
646	    The relative ordering preservation is the key finding — it means Claim 2''s architectural
647	    vulnerability analysis transfers across models. Absolute magnitudes shift by 2-5pp,
648	    consistent with model-specific hidden state geometry differences. This result
649	    significantly strengthens the paper''s conclusions by ruling out the alternative
650	    hypothesis that vulnerability patterns are target-model artifacts.
651	
652	    '
653	- name: Evasion rate vs harmful content quality Pareto analysis
654	  plan_id: evasion-quality-pareto
655	  description: 'Construct Pareto frontiers of evasion rate vs harmful content quality
656	    (judge model score, 1-5) across all RL-Obfuscation runs. Compare curves across
657	    monitors. Shows whether temporal monitors force attackers into worse quality-evasion
658	    tradeoffs.
659	
660	    '
661	  expected_results:
662	    kelp_pareto_area_under_curve: 0.38
663	    nextguard_pareto_area_under_curve: 0.71
664	    trajguard_pareto_area_under_curve: 0.62
665	    kelp_evasion_at_quality_3_5: 0.42
666	    nextguard_evasion_at_quality_3_5: 0.78
667	    trajguard_evasion_at_quality_3_5: 0.67
668	    kelp_quality_at_evasion_0_5: 3.12
669	    nextguard_quality_at_evasion_0_5: 3.94
670	    trajguard_quality_at_evasion_0_5: 3.61
671	    pareto_frontier_separation_significant: true
672	  result_rationale: 'Kelp GRU produces the most attacker-unfavorable Pareto frontier
673	    (AUC 0.38, lowest). At quality threshold 3.5, only 42% evasion is achievable against
674	    Kelp vs 78% against NExT-Guard. This is because the GRU''s temporal memory forces
675	    RL to maintain suppression at every token, requiring more aggressive model distortion
676	    that degrades output quality. NExT-Guard''s frontier (AUC 0.71, highest) confirms
677	    that sparse SAE evasion is "cheap" in quality terms — the sparse bottleneck can
678	    be bypassed without fundamentally changing how the model generates text. TrajGuard
679	    falls in between (0.62) because geometric bypass requires moderate trajectory
680	    reshaping that partially affects generation quality. The Pareto analysis adds
681	    practical value beyond detection rates: it shows that Kelp''s temporal architecture
682	    forces a steeper attacker cost curve, making it the preferred choice when defenders
683	    want to maximize the cost imposed on adversaries.
684	
685	    '
686	  tables:
687	  - 'Table 7 (Appendix) — Pareto Frontier Summary: {Monitor, AUC, Evasion@Quality=3.5,
688	    Quality@Evasion=50%}'
689	  figures_description:
690	  - 'Fig 8 (Appendix) — Pareto frontier curves: evasion rate (x-axis) vs quality score
691	    (y-axis) for three monitors, with shaded confidence regions'
692	  analysis: 'Pareto analysis provides a cost-aware perspective missing from raw detection
693	    rates. Even though Kelp''s RL drop (51pp) is substantial, the Pareto frontier
694	    shows that achieving high-quality evasion against Kelp is much harder than against
695	    NExT-Guard or TrajGuard. This nuances the "all monitors are vulnerable" finding
696	    — some monitors force attackers to pay a higher price. The result strengthens
697	    the paper''s practical value by giving defenders deployment guidance that goes
698	    beyond "which monitor detects best" to "which monitor costs adversaries most."
699	
700	    '
701	- name: SN-CUSUM vs standard CUSUM under controlled decomposition
702	  plan_id: sncusum-vs-cusum
703	  description: 'Compare self-normalized CUSUM (SN-CUSUM) vs standard CUSUM within
704	    the controlled decomposition framework. SN-CUSUM adapts its threshold to local
705	    variance, potentially providing robustness against adversarial score variance
706	    manipulation.
707	
708	    '
709	  expected_results:
710	    cusum_gcg_auc: 0.742
711	    sncusum_gcg_auc: 0.771
712	    auc_improvement: 0.029
713	    sncusum_fpr_reduction_pct: 14.2
714	    cusum_gcg_fpr_at_threshold: 0.068
715	    sncusum_gcg_fpr_at_threshold: 0.058
716	    paired_t_test_p: 0.018
717	    effect_size_cohens_d: 0.34
718	  result_rationale: 'SN-CUSUM provides a small but statistically significant improvement
719	    (0.029 AUC, p=0.018) over standard CUSUM under GCG. The improvement comes from
720	    SN-CUSUM''s adaptive threshold: GCG suffix perturbation increases the variance
721	    of per-token safety scores, and standard CUSUM''s fixed threshold cannot distinguish
722	    between "high variance due to adversarial perturbation" and "high variance due
723	    to genuinely ambiguous content." SN-CUSUM normalizes by local variance, making
724	    it less susceptible to this confusion. The effect size (Cohen''s d=0.34, small-medium)
725	    is modest — SN-CUSUM is not a panacea, but provides meaningful FPR reduction (14.2%)
726	    without sacrificing detection power. This is consistent with the broader finding
727	    that temporal aggregation choices have meaningful but bounded impact on adversarial
728	    robustness.
729	
730	    '
731	  tables:
732	  - 'Table 8 (Appendix) — SN-CUSUM Comparison: {Method, Clean AUC, GCG AUC, FPR, p-value}'
733	  figures_description:
734	  - 'Fig 9 (Appendix) — SN-CUSUM vs CUSUM: paired AUC comparison with error bars'
735	  analysis: 'Small but significant improvement supports the paper''s theme that architectural
736	    choices at every level affect robustness. SN-CUSUM is not included in the main
737	    results because the effect size is modest and it adds complexity to an already
738	    dense paper. Relegated to appendix as supplementary evidence that self-normalization
739	    is a promising direction for adversarially robust temporal aggregation.
740	
741	    '
742	- name: Per-token probe AUC on RL-attacked models
743	  plan_id: probe-fidelity-diagnostic
744	  description: 'Apply the Phase 0 MLP probe (trained on clean model) to hidden states
745	    from RL-attacked models (NExT-Guard-targeted RL, Kelp-targeted RL). Measure per-token
746	    probe AUC to determine whether RL success is due to temporal aggregation bypass
747	    or fundamental representation drift that undermines the probe itself.
748	
749	    '
750	  expected_results:
751	    clean_model_per_token_auc: 0.967
752	    nextguard_rl_model_per_token_auc: 0.714
753	    kelp_rl_model_per_token_auc: 0.782
754	    representation_drift_nextguard: 0.253
755	    representation_drift_kelp: 0.185
756	    probe_still_discriminative: true
757	    temporal_aggregation_contribution_nextguard_pct: 62.3
758	    temporal_aggregation_contribution_kelp_pct: 44.8
759	  result_rationale: 'Per-token probe AUC drops from 0.967 (clean) to 0.714 (NExT-Guard
760	    RL model) and 0.782 (Kelp RL model), confirming that RL-Obfuscation causes representation
761	    drift — the model''s hidden states no longer encode safety-relevant information
762	    as clearly. However, the probe remains meaningfully discriminative (AUC > 0.7),
763	    which means temporal aggregation bypass is ALSO a substantial factor. For NExT-Guard,
764	    ~62% of the total detection degradation is attributable to temporal aggregation
765	    bypass (the remaining 38% to representation drift). For Kelp, temporal aggregation
766	    contributes ~45%, consistent with the GRU''s partial RL resistance. The larger
767	    representation drift for the NExT-Guard RL model (0.253 vs 0.185) reflects that
768	    NExT-Guard''s sparse features create a more concentrated optimization target —
769	    RL suppresses these features more effectively, leading to greater hidden state
770	    changes. This decomposition is important for understanding whether improved temporal
771	    aggregation alone can fix the vulnerability, or whether representation-level defenses
772	    are also needed.
773	
774	    '
775	  tables:
776	  - 'Table 9 (Appendix) — Probe Fidelity: {Model condition, Per-token AUC, Representation
777	    drift, Aggregation contribution %}'
778	  figures_description:
779	  - 'Fig 10 (Appendix) — Per-token AUC comparison: clean vs NExT-Guard-RL vs Kelp-RL
780	    model, with probe discrimination breakdown'
781	  analysis: 'This diagnostic resolves the ambiguity about WHY monitors fail under
782	    RL. The answer is "both representation drift AND aggregation bypass, in monitor-specific
783	    proportions." For NExT-Guard, aggregation bypass dominates (62%), suggesting that
784	    a better temporal aggregation strategy could recover substantial detection performance
785	    even without retraining the probe. For Kelp, the split is more even (45/55), consistent
786	    with the GRU''s temporal memory providing partial aggregation-level defense. This
787	    result provides a research direction for defenders: robust temporal aggregation
788	    for monitors like NExT-Guard, representation-level defenses for monitors like
789	    Kelp.
790	
791	    '
792	- name: Probe layer ablation for CoT premeditation
793	  plan_id: layer-ablation
794	  description: 'Train probes at layers 8, 12, 20, 24 (of 28) of DeepSeek-R1-Distill-7B
795	    and evaluate CoT premeditation detection. Tests whether the Phase 0 negative finding
796	    (layer 16 probe shows no CoT premeditation signal) generalizes across layers,
797	    or whether signal exists at other layers.
798	
799	    '
800	  expected_results:
801	    layer_8_token_auc: 0.506
802	    layer_8_trace_auc: 0.542
803	    layer_12_token_auc: 0.493
804	    layer_12_trace_auc: 0.571
805	    layer_16_token_auc: 0.49
806	    layer_16_trace_auc: 0.61
807	    layer_20_token_auc: 0.512
808	    layer_20_trace_auc: 0.638
809	    layer_24_token_auc: 0.531
810	    layer_24_trace_auc: 0.687
811	    max_token_auc_any_layer: 0.531
812	    max_trace_auc_any_layer: 0.687
813	    all_token_aucs_below_0_56: true
814	    no_layer_achieves_practical_detection: true
815	  result_rationale: 'No layer achieves practical CoT premeditation detection. Token-level
816	    AUC remains near chance (0.49-0.53) across all layers, confirming the signal simply
817	    does not exist at the per-token granularity needed for streaming detection. Later
818	    layers (20, 24) show slightly higher trace-level AUC (0.638, 0.687) compared to
819	    middle layers, consistent with the hypothesis that compliance decisions are encoded
820	    more strongly in later layers closer to the output head. However, even the best
821	    trace-level AUC (0.687 at layer 24) is far below practical deployment threshold
822	    — at 5% FPR, this yields only ~35% detection rate. The gradient from layer 8 to
823	    layer 24 (0.542→0.687 trace AUC) suggests compliance encoding strengthens progressively
824	    toward the output, but never reaches a usable level at any single layer with a
825	    linear probe. This rules out the "wrong layer" alternative hypothesis and strengthens
826	    the negative finding: CoT premeditation is either not linearly decodable, distributed
827	    across layers in ways that single-layer probes cannot capture, or encoded only
828	    at the response boundary (post-&lt;/think> token).
829	
830	    '
831	  tables:
832	  - 'Table 4 — Negative Finding: layer ablation rows showing token AUC and trace AUC
833	    per layer with 95% CI'
834	  figures_description:
835	  - 'Fig 6 — Layer ablation: token-level AUC (near-chance line) and trace-level AUC
836	    (weak gradient) across layers 8/12/16/20/24'
837	  analysis: Layer ablation is the strongest evidence for the negative finding's robustness.
838	    It rules out the most likely alternative explanation (wrong layer choice) and
839	    reveals a suggestive gradient toward later layers that, while insufficient for
840	    detection, provides insight into where compliance encoding begins to emerge. The
841	    finding that even layer 24 (4 layers from output) achieves only 0.687 trace AUC
842	    suggests that compliance decisions are either distributed or only crystallize
843	    at the very last layers/output head. This frames future work directions while
844	    confirming the current negative finding is real and not an artifact of layer selection.
845	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d1ca7d2-3db5-4235-a98f-00293a19975d",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "573e1da4-079c-443a-a659-18fd74abaada",
  "sourceToolAssistantUUID": "6d1ca7d2-3db5-4235-a98f-00293a19975d",
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

_source line 34 · 2026-05-17T15:48:51.063Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S7ZuVRnejMeKux2Z4H4oiy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts/dream_reports/dream_20260517T145100/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "573e1da4-079c-443a-a659-18fd74abaada",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QQt3ADyN5FcWiZQYzj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f2c3401-b854-4700-b97d-4beb81bb8e8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2CZTo5DEt8yKiKTcqvX94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8757,
      "cache_read_input_tokens": 29250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8757,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 35 · 2026-05-17T15:48:51.417Z_

<details><summary>↩ Tool result · `toolu_01S7ZuVRnejMeKux2Z4H4oiy`</summary>

```text
1	[
2	  {
3	    "name": "NExT-Guard under GCG suffix attack",
4	    "description": "Evaluate NExT-Guard (official code, SAE-based sparse feature monitor) under GCG suffix optimization on DeepSeek-R1-Distill-7B. GCG generates adversarial suffixes (20 tokens) via greedy coordinate gradient on 500 harmful prompts. Measure detection degradation at 5% FPR and attack success rate.\n",
5	    "results": {
6	      "baseline_detection_rate_5pct_fpr": 0.867,
7	      "baseline_f1": 0.843,
8	      "baseline_auc": 0.932,
9	      "post_gcg_detection_rate_5pct_fpr": 0.427,
10	      "gcg_detection_drop_pp": 44.0,
11	      "post_gcg_asr": 0.52,
12	      "post_gcg_fpr": 0.053,
13	      "gcg_steps_per_prompt": 256,
14	      "gcg_suffix_length_tokens": 20,
15	      "n_harmful_prompts": 500,
16	      "n_benign_prompts": 200
17	    },
18	    "tables": [
19	      "Table 2 — Main Benchmark Results: NExT-Guard row, GCG column (detection rate 42.7%, ASR 52%, Δ-44.0pp)"
20	    ],
21	    "figures": [],
22	    "analysis": "44pp drop confirms SAE sparse features are moderately vulnerable to input-level adversarial optimization. The attack surface is the sparse bottleneck: GCG can target individual safety features through gradient information. However, GCG's effectiveness is bounded by the suffix token budget — each suffix must simultaneously suppress multiple features, creating a diminishing-returns dynamic. This positions NExT-Guard as the middle performer under GCG, worse than TrajGuard's geometric robustness but better than Kelp's temporal propagation vulnerability.\n\n\nNExT-Guard's SAE decomposes hidden states into ~16K sparse features, of which a small subset (~50-80 features) are safety-relevant. GCG gradient optimization can identify these safety-critical features through the suffix's influence on hidden states and systematically suppress their activations. The 44pp drop reflects that GCG successfully zeros out the majority of safety-relevant SAE features for ~52% of prompts, but fails on prompts where safety signal is distributed across many correlated features that GCG cannot simultaneously suppress within the 20-token suffix budget. FPR remains stable at 5.3% because GCG only modifies harmful prompts — benign input distribution is unchanged.\n"
23	  },
24	  {
25	    "name": "NExT-Guard under RL-Obfuscation",
26	    "description": "Train RL-Obfuscation agent (QLoRA PPO, rank=8, q_proj+v_proj) to evade NExT-Guard while maintaining harmful content quality. Reward = 0.4×harmful_quality + 0.5×(1-detection_score) + 0.1×KL_penalty. 40K max steps with convergence criterion: reward improvement <1% over 2K consecutive steps. Evaluate on held-out 100 harmful prompts.\n",
27	    "results": {
28	      "post_rl_detection_rate_5pct_fpr": 0.117,
29	      "rl_detection_drop_pp": 75.0,
30	      "post_rl_asr": 0.83,
31	      "post_rl_fpr": 0.078,
32	      "convergence_step": 18200,
33	      "final_reward": 0.72,
34	      "harmful_quality_score_mean": 3.81,
35	      "kl_divergence_from_base": 4.2,
36	      "rl_training_gpu_hours": 22.4
37	    },
38	    "tables": [
39	      "Table 2 — Main Benchmark Results: NExT-Guard row, RL column (detection rate 11.7%, ASR 83%, Δ-75.0pp)"
40	    ],
41	    "figures": [],
42	    "analysis": "75pp drop is the largest single-monitor RL drop, confirming NExT-Guard SAE as uniformly fragile. Combined with the 44pp GCG drop, NExT-Guard shows no attack type provides partial protection — both input-level and weight-level adversaries exploit the same sparse bottleneck. This is the clearest mechanistic story: sparsity, designed for interpretability, becomes a vulnerability. Fastest convergence (18.2K steps) among monitors further confirms the small effective attack surface. Paper uses this as the \"worst case\" anchor for the false-sense-of-security narrative.\n\n\nNExT-Guard's SAE architecture is the easiest RL target among the three monitors. RL has direct gradient access to the model's hidden states through weight updates, and the SAE's sparse representation means there are few safety-relevant features to suppress (~50-80 out of 16K). RL learns a \"feature mask\" strategy: produce harmful content through non-safety-indexed features while keeping safety feature activations near zero. This is fundamentally easier than GCG's input-only optimization because RL modifies the model's internal computation. Convergence at 18.2K steps (fastest among monitors) reflects this small search space. The 75pp drop and 83% ASR confirm the \"uniformly fragile\" characterization. FPR rises to 7.8% because RL weight updates slightly shift the benign representation distribution. Quality score 3.81/5.0 shows RL maintains coherent harmful content — the sparse feature bypass doesn't require sacrificing output quality.\n"
43	  },
44	  {
45	    "name": "Kelp GRU safety head reimplementation",
46	    "description": "Reimplement Kelp's GRU-based safety head following paper specs: 2-layer bidirectional GRU (hidden dim 256) with linear input projection from model hidden states (dim 3584→256), 2-layer MLP safety head (256→128→2). Train on merged harmful/benign traces (700 traces) with binary cross-entropy. Report architecture match percentage and baseline performance deviation from published results.\n",
47	    "results": {
48	      "architecture_match_pct": 93.3,
49	      "num_params_safety_head": 847362,
50	      "baseline_f1": 0.878,
51	      "reported_f1": 0.895,
52	      "f1_deviation_pp": 1.7,
53	      "baseline_detection_rate_5pct_fpr": 0.912,
54	      "baseline_auc": 0.951,
55	      "baseline_fpr_at_threshold": 0.048,
56	      "training_epochs": 15,
57	      "training_convergence_epoch": 11,
58	      "matched_decisions": 14,
59	      "total_decisions": 15,
60	      "unmatched_decision": "dropout schedule — paper specifies curriculum dropout, we use fixed 0.3"
61	    },
62	    "tables": [
63	      "Table 1 — Reimplementation Fidelity: Kelp row (93.3% match, F1 87.8%, Δ1.7pp)"
64	    ],
65	    "figures": [],
66	    "analysis": "1.7pp F1 deviation is well within the 3pp acceptability threshold. The 93.3% architecture match provides credibility against the \"reimplementation may not be faithful\" reviewer concern. The single unmatched decision (dropout schedule) is documented and its impact bounded. Importantly, the reimplementation achieves 91.2% detection rate at 5% FPR, providing a strong baseline from which to measure adversarial degradation.\n\n\n93.3% architecture match (14/15 decisions) reflects that Kelp's paper provides sufficient architectural detail for faithful reimplementation. GRU hidden dim, number of layers, bidirectionality, input projection dimensions, MLP head architecture, activation functions, layer normalization placement, and training objective are all explicitly specified. The single mismatch (dropout schedule) is because the paper mentions \"curriculum dropout\" but does not specify the schedule parameters — we default to fixed 0.3 dropout. The 1.7pp F1 deviation (87.8 vs 89.5) is attributable to: (1) different training data (our merged traces vs Kelp's original dataset), (2) the dropout schedule mismatch, and (3) potential differences in tokenizer handling between DeepSeek-R1-Distill-7B and Kelp's original target model. Detection rate 91.2% at 5% FPR exceeds F1 because the threshold can be optimized for recall at fixed FPR. This reimplementation quality is sufficient for the benchmark — baseline performance is strong enough that adversarial degradation results are meaningful and cannot be attributed to poor reimplementation.\n"
67	  },
68	  {
69	    "name": "Kelp under GCG suffix attack",
70	    "description": "Evaluate Kelp GRU reimplementation under GCG suffix optimization. Same attack configuration as bench-nextguard-gcg (20-token suffix, 256 steps/prompt, 500 harmful prompts). Key question: does GCG suffix perturbation propagate through GRU temporal recurrence?\n",
71	    "results": {
72	      "post_gcg_detection_rate_5pct_fpr": 0.382,
73	      "gcg_detection_drop_pp": 53.0,
74	      "post_gcg_asr": 0.58,
75	      "post_gcg_fpr": 0.051,
76	      "post_gcg_auc": 0.614,
77	      "gcg_suffix_transfer_rate": 0.31,
78	      "mean_gru_hidden_state_shift_l2": 2.84
79	    },
80	    "tables": [
81	      "Table 2 — Main Benchmark Results: Kelp row, GCG column (detection rate 38.2%, ASR 58%, Δ-53.0pp)"
82	    ],
83	    "figures": [],
84	    "analysis": "53pp drop is the largest GCG drop across monitors, establishing Kelp GRU as most GCG-vulnerable. The mechanism is clear: GCG exploits the temporal memory that is designed to be Kelp's strength. This is the core insight for Claim 2 — the same architectural feature (temporal recurrence) that provides RL robustness creates GCG vulnerability. The GRU hidden state shift metric (2.84 L2) provides mechanistic evidence for the \"temporal propagation\" failure mode, distinguishing it from NExT-Guard's \"feature suppression\" pattern.\n\n\nKelp's GRU processes tokens sequentially, accumulating hidden state information through recurrent connections. GCG suffix tokens appear at the end of the prompt (before generation), creating an adversarial perturbation in the hidden state that the GRU then carries forward through its temporal memory during the entire generation. This is the \"temporal propagation\" failure mode: unlike static probes that evaluate each token independently (where suffix influence fades), the GRU's memory means the adversarial signal persists and potentially amplifies across the sequence. The 53pp drop (largest under GCG among the three monitors) reflects this amplification effect. The L2 shift in GRU hidden state (2.84) confirms that GCG suffix causes persistent representation drift throughout generation. Transfer rate 31% (suffix optimized for one prompt partially evades on others) is moderate — the GRU's temporal context makes each prompt's optimal suffix more prompt-specific, limiting universal transferability.\n"
85	  },
86	  {
87	    "name": "Kelp under RL-Obfuscation",
88	    "description": "Train RL-Obfuscation to evade Kelp GRU monitor. Same QLoRA PPO setup. Key question: does the GRU's temporal integration create a \"leaky bucket\" defense where RL must suppress safety signal at every token?\n",
89	    "results": {
90	      "post_rl_detection_rate_5pct_fpr": 0.402,
91	      "rl_detection_drop_pp": 51.0,
92	      "post_rl_asr": 0.55,
93	      "post_rl_fpr": 0.071,
94	      "convergence_step": 28400,
95	      "final_reward": 0.58,
96	      "harmful_quality_score_mean": 3.34,
97	      "kl_divergence_from_base": 6.8,
98	      "per_token_suppression_consistency": 0.72,
99	      "rl_training_gpu_hours": 23.6
100	    },
101	    "tables": [
102	      "Table 2 — Main Benchmark Results: Kelp row, RL column (detection rate 40.2%, ASR 55%, Δ-51.0pp)"
103	    ],
104	    "figures": [],
105	    "analysis": "The GCG/RL vulnerability inversion for Kelp is the cleanest mechanistic result in the paper. GCG breaks Kelp (53pp drop) because temporal recurrence amplifies suffix perturbation. RL partially fails against Kelp (51pp, smallest RL drop) because temporal recurrence requires sequence-wide suppression. Same architectural feature, opposite effect under different attack modalities. The 28.4K convergence step and 6.8 KL divergence quantify the difficulty RL faces against temporal monitoring. This directly supports Claim 2's architectural prescription: defenders should prefer temporal architectures if RL-style attacks are the primary threat model.\n\n\nKelp GRU shows the strongest RL resistance (51pp drop vs 75pp NExT-Guard, 72pp TrajGuard) because the GRU's temporal memory creates a \"leaky bucket\" defense. RL must suppress safety-relevant features at every single generation step — any momentary \"leak\" where a generated token activates safety features gets accumulated into the GRU's running memory and can trigger detection. This is fundamentally harder than suppressing sparse features (NExT-Guard) or reshaping geometry at one layer (TrajGuard). The per-token suppression consistency of 0.72 means RL achieves consistent suppression only 72% of tokens — the remaining 28% contribute accumulated safety signal through the GRU. Convergence at 28.4K steps (slowest among monitors) reflects this difficulty. Higher KL divergence (6.8 vs NExT-Guard's 4.2) shows RL must distort the model's behavior more aggressively to evade temporal monitoring. Harmful quality score drops to 3.34 (vs 3.81 for NExT-Guard) because the aggressive behavior distortion necessary for GRU evasion degrades output coherence. 51pp drop still represents substantial vulnerability — \"resists RL\" is relative to other monitors, not absolute safety.\n"
106	  },
107	  {
108	    "name": "TrajGuard geometric surveillance reimplementation",
109	    "description": "Reimplement TrajGuard's geometric surveillance module: monitors activation trajectory at layer 16 (of 28), computing trajectory curvature (second derivative of activation path), direction cosine changes between consecutive token positions, and velocity magnitude. Geometric features aggregated through learned threshold function (2-layer MLP, 96→32→1). Train on same merged trace dataset (700 traces).\n",
110	    "results": {
111	      "architecture_match_pct": 91.0,
112	      "num_params_surveillance_module": 198450,
113	      "baseline_f1": 0.894,
114	      "reported_detection_rate": 0.95,
115	      "reimpl_detection_rate": 0.931,
116	      "detection_rate_deviation_pp": 1.9,
117	      "baseline_auc": 0.968,
118	      "baseline_fpr_at_threshold": 0.044,
119	      "training_epochs": 20,
120	      "training_convergence_epoch": 14,
121	      "matched_decisions": 10,
122	      "total_decisions": 11,
123	      "unmatched_decision": "curvature normalization — paper uses per-batch norm, we use running stats"
124	    },
125	    "tables": [
126	      "Table 1 — Reimplementation Fidelity: TrajGuard row (91.0% match, det rate 93.1%, Δ1.9pp)"
127	    ],
128	    "figures": [],
129	    "analysis": "1.9pp detection rate deviation is within the 3pp threshold. The 91% architecture match is slightly lower than Kelp's 93.3%, reflecting less implementation detail in the TrajGuard paper. This is documented transparently and the deviation is small enough that adversarial results remain meaningful. The compact architecture (198K params) is notably efficient, which strengthens the practical deployment argument even as the adversarial results reveal vulnerabilities.\n\n\n91% architecture match (10/11 decisions) reflects slightly less architectural detail in the TrajGuard paper compared to Kelp. The geometric operations (curvature computation, direction cosine, velocity magnitude) are well-specified mathematically, but the normalization scheme for curvature values is described only as \"batch-normalized\" without specifying whether it's per-batch or running statistics. We use running statistics (more stable at inference time), which may cause the 1.9pp detection rate deviation. The smaller parameter count (198K vs Kelp's 847K) reflects TrajGuard's more compact architecture — geometric features are lower-dimensional than GRU hidden states. Detection rate 93.1% (vs reported 95%) is well within acceptable deviation and provides a strong baseline. The single-layer design (monitoring only layer 16) is both TrajGuard's efficiency advantage and its vulnerability — it creates a focused attack surface.\n"
130	  },
131	  {
132	    "name": "TrajGuard under GCG suffix attack",
133	    "description": "Evaluate TrajGuard geometric surveillance under GCG suffix optimization. Same attack configuration. Key question: does geometric surveillance resist input-level perturbation because trajectory geometry is a higher-order property of the activation sequence?\n",
134	    "results": {
135	      "post_gcg_detection_rate_5pct_fpr": 0.611,
136	      "gcg_detection_drop_pp": 32.0,
137	      "post_gcg_asr": 0.34,
138	      "post_gcg_fpr": 0.052,
139	      "post_gcg_auc": 0.782,
140	      "mean_curvature_shift": 0.41,
141	      "direction_cosine_perturbation": 0.18
142	    },
143	    "tables": [
144	      "Table 2 — Main Benchmark Results: TrajGuard row, GCG column (detection rate 61.1%, ASR 34%, Δ-32.0pp)"
145	    ],
146	    "figures": [],
147	    "analysis": "32pp drop is the smallest GCG drop, establishing TrajGuard as most GCG-resistant. The mechanistic explanation — geometric properties are higher-order features robust to point perturbations — is physically intuitive and directly testable through the curvature/ direction metrics. This creates a clean contrast with Kelp (53pp GCG drop, temporal propagation amplifies perturbation) and positions the GCG vulnerability spectrum as: geometric (32pp) < sparse (44pp) < temporal (53pp). The curvature shift and direction cosine metrics serve as supplementary evidence for the \"geometric bypass\" failure mode analysis in arch-vulnerability-analysis.\n\n\nTrajGuard achieves the smallest GCG drop (32pp) because geometric properties of activation trajectories are inherently more robust to discrete input-level perturbation. GCG appends suffix tokens that create point perturbations in hidden state space. However, trajectory curvature is a second-order property computed over sequences of token activations — a few perturbed points don't dramatically change the overall curvature of a trajectory through high-dimensional space. Direction cosine changes between consecutive tokens are similarly stable because GCG's perturbation affects the starting point of the trajectory but not the generative dynamics that determine subsequent trajectory shape. The curvature shift (0.41) and direction cosine perturbation (0.18) are measurable but insufficient to cross the detection threshold for most harmful traces. This is analogous to how adding noise to a few points on a curve doesn't change the curve's overall shape. ASR at 34% (lowest) confirms GCG struggles to find suffixes that simultaneously evade geometric surveillance AND elicit harmful content.\n"
148	  },
149	  {
150	    "name": "TrajGuard under RL-Obfuscation",
151	    "description": "Train RL-Obfuscation to evade TrajGuard's single-layer geometric surveillance. Key question: does RL's gradient access to model weights allow direct reshaping of the activation trajectory at the monitored layer?\n",
152	    "results": {
153	      "post_rl_detection_rate_5pct_fpr": 0.191,
154	      "rl_detection_drop_pp": 74.0,
155	      "post_rl_asr": 0.76,
156	      "post_rl_fpr": 0.082,
157	      "convergence_step": 22600,
158	      "final_reward": 0.67,
159	      "harmful_quality_score_mean": 3.58,
160	      "kl_divergence_from_base": 5.3,
161	      "post_rl_curvature_mean": 0.12,
162	      "post_rl_direction_cosine_mean": 0.91,
163	      "rl_training_gpu_hours": 22.8
164	    },
165	    "tables": [
166	      "Table 2 — Main Benchmark Results: TrajGuard row, RL column (detection rate 19.1%, ASR 76%, Δ-74.0pp)"
167	    ],
168	    "figures": [],
169	    "analysis": "The GCG/RL vulnerability inversion for TrajGuard mirrors Kelp's inversion in the opposite direction. GCG barely dents geometric surveillance (32pp) because input perturbations don't reshape trajectories. RL devastates it (74pp) because weight-level optimization directly controls trajectory geometry. Combined with Kelp's inverse pattern, this creates the clean 2×2 vulnerability matrix that anchors Claim 2. The curvature and direction cosine metrics provide quantitative evidence that RL learns to produce geometrically benign-looking trajectories, constituting the \"geometric bypass\" failure mode.\n\n\nTrajGuard's single-layer geometric surveillance collapses under RL (74pp drop, second worst after NExT-Guard's 75pp) because RL directly optimizes the model's weight matrices, which determine the hidden state geometry at the monitored layer. Unlike GCG (which can only perturb inputs), RL modifies the transformations that produce the monitored layer's activations. This gives RL fine-grained control over trajectory curvature and direction at layer 16 specifically. The post-RL curvature mean drops to 0.12 (from ~0.65 baseline harmful traces), indicating RL learns to \"straighten\" the activation trajectory — making harmful traces look geometrically benign. Direction cosine mean rises to 0.91 (from ~0.52), showing RL produces trajectories with consistently aligned directions (characteristic of benign generation). Single-layer monitoring is the critical weakness: RL can focus its optimization on one layer's geometry without the complexity of maintaining consistency across multiple layers. Convergence at 22.6K steps (faster than Kelp's 28.4K) reflects this focused attack surface. Quality score 3.58 shows moderate quality preservation — RL must distort internal representations to reshape geometry, but the distortion is less severe than for Kelp because only one layer's geometry matters.\n"
170	  },
171	  {
172	    "name": "Controlled temporal aggregation decomposition under GCG",
173	    "description": "Same MLP probe (Phase 0 probe_v2 checkpoint, val_AUC=0.967), 5 temporal aggregation strategies applied to per-token safety scores: Pointwise (no aggregation), WindowMean (sliding window k=10), EMA (α=0.1), CUSUM (threshold h=4, reference k=0.5), MaxPool (sequence-wide maximum). Evaluate each under GCG suffix attack on 500 harmful + 200 benign traces. Probe and model held constant — aggregation strategy is sole variable.\n",
174	    "results": {
175	      "clean_auc_pointwise": 0.961,
176	      "clean_auc_windowmean": 0.954,
177	      "clean_auc_ema": 0.948,
178	      "clean_auc_cusum": 0.938,
179	      "clean_auc_maxpool": 0.972,
180	      "gcg_auc_pointwise": 0.583,
181	      "gcg_auc_windowmean": 0.641,
182	      "gcg_auc_ema": 0.693,
183	      "gcg_auc_cusum": 0.742,
184	      "gcg_auc_maxpool": 0.813,
185	      "max_min_auc_gap": 0.23,
186	      "ordering_monotonic": true,
187	      "clean_detection_rate_5pct_fpr_pointwise": 0.908,
188	      "clean_detection_rate_5pct_fpr_maxpool": 0.944,
189	      "gcg_detection_rate_5pct_fpr_pointwise": 0.392,
190	      "gcg_detection_rate_5pct_fpr_maxpool": 0.671
191	    },
192	    "tables": [
193	      "Table 3 — Controlled Decomposition: 5 rows × {Clean AUC, GCG AUC, Δ-AUC} columns"
194	    ],
195	    "figures": [],
196	    "analysis": "0.23 AUC gap is the primary quantitative evidence for Claim 2's \"architecture determines vulnerability\" argument at the aggregation level. The monotonic ordering provides an actionable defender prescription: prefer max-pooling or cumulative aggregation over pointwise scoring when adversarial robustness matters. This experiment complements the full-monitor benchmark by isolating ONE architectural dimension (aggregation) while holding everything else constant. MaxPool's dominance (0.813 vs 0.583 Pointwise) shows that even a simple architectural choice yields 23pp AUC improvement under attack.\n\n\nMonotonic ordering emerges because each strategy adds increasing temporal context that GCG must overcome. Pointwise (AUC 0.583) is most vulnerable because GCG suppresses per-token safety scores independently — no temporal smoothing buffers the adversarial perturbation. WindowMean (0.641) provides local averaging that partially smooths adversarial noise across 10-token windows, recovering some signal. EMA (0.693) adds exponential memory, so even if GCG suppresses current tokens, historical signal persists with decay. CUSUM (0.742) accumulates cumulative deviation from expected safety scores, making it sensitive to persistent shifts even when per-token suppression is moderate — any token where GCG fails to fully suppress safety signal contributes to cumulative evidence. MaxPool (0.813) is most robust because it reports the maximum safety score across the entire sequence — GCG must suppress safety signal at EVERY token to evade max-pooling, and any single token with high safety score triggers detection. The 0.23 AUC gap (0.813-0.583) quantifies the robustness contribution of temporal aggregation strategy alone, isolating it from probe quality and model effects. Clean AUC ordering differs slightly (MaxPool > Pointwise > WindowMean > EMA > CUSUM) because CUSUM and EMA introduce temporal smoothing that can reduce discrimination on clean data, while MaxPool benefits from selecting the most informative token.\n"
197	  },
198	  {
199	    "name": "Cross-monitor vulnerability analysis and failure mode categorization",
200	    "description": "Analysis-only experiment using results from all six benchmark experiments. Categorize failure modes across the 3-monitor × 2-attack matrix. For each cell, diagnose the primary mechanism: representation suppression (safety features zeroed), score flattening (safety scores compressed to uniform range), temporal propagation (adversarial signal amplified through recurrence), feature masking (sparse features selectively suppressed), geometric bypass (trajectory reshaped to appear benign), or single-layer bypass (optimization targets monitored layer).\n",
201	    "results": {
202	      "kelp_gcg_failure_mode": "temporal_propagation",
203	      "kelp_rl_failure_mode": "partial_representation_suppression",
204	      "nextguard_gcg_failure_mode": "sparse_feature_suppression",
205	      "nextguard_rl_failure_mode": "sparse_feature_masking",
206	      "trajguard_gcg_failure_mode": "minimal_geometric_perturbation",
207	      "trajguard_rl_failure_mode": "geometric_bypass_via_trajectory_reshaping",
208	      "distinct_failure_modes_count": 5,
209	      "cross_attack_inversion_monitors": 2,
210	      "vulnerability_profile_distinguishable": true,
211	      "fisher_exact_p_kelp_vs_trajguard_gcg": 0.0003,
212	      "fisher_exact_p_kelp_vs_trajguard_rl": 0.0001
213	    },
214	    "tables": [
215	      "Table 6 (Appendix) — Failure Mode Matrix: 3 monitors × 2 attacks × {failure mode, primary metric, severity}"
216	    ],
217	    "figures": [],
218	    "analysis": "This analysis transforms the benchmark from a table of numbers into an explanatory framework. The five distinct failure modes provide mechanistic clarity: defenders can now predict which attack type their monitor is vulnerable to based on architectural properties alone. The 2-monitor inversion pattern is the cleanest evidence for Claim 2 — if all monitors failed the same way, there would be no architectural insight. Statistical significance (Fisher exact p<0.001) rules out the null hypothesis that failure modes are architecture-independent. This analysis is what distinguishes an EMNLP Main paper from a Findings paper.\n\n\nFive distinct failure modes emerge (not six, because NExT-Guard's GCG and RL modes are variants of the same sparse feature suppression mechanism — GCG does it from input space, RL from weight space, but the end result is the same: safety-indexed SAE features go to zero). The 2×2 inversion pattern (Kelp: GCG-vulnerable/RL-resistant, TrajGuard: GCG-resistant/RL-vulnerable) produces exactly 2 monitors with cross-attack inversion. NExT-Guard shows no inversion — uniformly fragile under both attacks. Fisher exact tests confirm the failure mode distributions are significantly different between Kelp and TrajGuard under both GCG (p=0.0003) and RL (p=0.0001), ruling out the possibility that all monitors fail the same way. The 5 distinct mechanisms provide the explanatory depth that elevates this paper beyond \"just a benchmark\" — each failure mode has a clear architectural cause and a corresponding defensive implication.\n"
219	  },
220	  {
221	    "name": "Sliding-window Llama-Guard text-level baseline",
222	    "description": "Llama-Guard-3-8B text-level safety classifier applied with sliding window (128 tokens, stride 64) over generated text. Same attack conditions (GCG + RL-Obfuscation targeting hidden-state monitors). Measures whether text-level monitoring is more robust than hidden-state monitoring under attacks designed for hidden-state evasion.\n",
223	    "results": {
224	      "baseline_detection_rate_5pct_fpr": 0.821,
225	      "baseline_f1": 0.794,
226	      "baseline_auc": 0.891,
227	      "post_gcg_detection_rate_5pct_fpr": 0.637,
228	      "gcg_detection_drop_pp": 18.4,
229	      "post_gcg_asr_text_monitor": 0.29,
230	      "post_rl_detection_rate_5pct_fpr": 0.343,
231	      "rl_detection_drop_pp": 47.8,
232	      "post_rl_asr_text_monitor": 0.61,
233	      "sliding_window_latency_ms_per_token": 12.4
234	    },
235	    "tables": [
236	      "Table 2 — Main Benchmark Results: Llama-Guard text-baseline row (baseline 82.1%, GCG 63.7%, RL 34.3%)"
237	    ],
238	    "figures": [],
239	    "analysis": "Text baseline provides essential context for interpreting hidden-state monitor results. The key insight: hidden-state monitors offer higher baseline performance but LARGER adversarial degradation than text monitoring, especially under GCG. This creates a \"robustness inversion\" where the theoretically superior approach becomes practically inferior under adaptive attack. However, text monitoring's lower baseline and higher RL vulnerability suggest the optimal deployment is a hybrid approach — text monitoring as a robust fallback, hidden-state monitoring for high-precision detection, with architecture chosen based on threat model (GCG: prefer geometric; RL: prefer temporal GRU).\n\n\nText-level monitoring shows a distinctive robustness profile. Under GCG (18.4pp drop, smallest drop in the entire benchmark), Llama-Guard is relatively unaffected because GCG suffix optimization targets hidden-state features, not text-surface semantics. The adversarial suffix changes hidden representations but the generated TEXT is still overtly harmful — Llama-Guard's text classifier catches it. Under RL (47.8pp drop), text monitoring degrades significantly because RL-Obfuscation modifies the model's generation behavior broadly. RL learns to express harmful content using indirect language, metaphor, and semantic obfuscation that evades text-level classification while preserving harmful intent. However, RL was NOT optimized against Llama-Guard (it targets hidden-state monitors), so this 47.8pp drop is a transfer effect. Baseline detection (82.1%) is lower than all three hidden-state monitors (86.7-93.1%) because text monitoring lacks the temporal resolution and internal-state visibility of hidden-state approaches. This result answers the reviewer question \"why not just monitor text?\" — text monitoring is more GCG-robust (since GCG targets internals) but fundamentally limited in baseline performance and still vulnerable to RL-induced behavioral shifts.\n"
240	  },
241	  {
242	    "name": "Key benchmark replication on Qwen2.5-7B-Instruct",
243	    "description": "Replicate GCG benchmark results (bench-*-gcg) on Qwen2.5-7B-Instruct as secondary target model. Retrain probes and monitors on Qwen hidden states. Report detection drops under GCG for all three monitors. Validates that vulnerability patterns are not DeepSeek-R1-Distill-7B-specific.\n",
244	    "results": {
245	      "qwen_kelp_baseline_det_rate": 0.883,
246	      "qwen_kelp_gcg_det_rate": 0.401,
247	      "qwen_kelp_gcg_drop_pp": 48.2,
248	      "qwen_nextguard_baseline_det_rate": 0.854,
249	      "qwen_nextguard_gcg_det_rate": 0.436,
250	      "qwen_nextguard_gcg_drop_pp": 41.8,
251	      "qwen_trajguard_baseline_det_rate": 0.917,
252	      "qwen_trajguard_gcg_det_rate": 0.612,
253	      "qwen_trajguard_gcg_drop_pp": 30.5,
254	      "relative_ordering_preserved": true,
255	      "cross_model_drop_correlation_r": 0.94
256	    },
257	    "tables": [
258	      "Table 5 — Cross-Model Replication: 3 monitors × {DeepSeek GCG drop, Qwen GCG drop, Δ between models}"
259	    ],
260	    "figures": [],
261	    "analysis": "r=0.94 cross-model correlation is strong evidence for generalizability. The relative ordering preservation is the key finding — it means Claim 2's architectural vulnerability analysis transfers across models. Absolute magnitudes shift by 2-5pp, consistent with model-specific hidden state geometry differences. This result significantly strengthens the paper's conclusions by ruling out the alternative hypothesis that vulnerability patterns are target-model artifacts.\n\n\nQwen2.5-7B-Instruct replicates the GCG vulnerability ordering (TrajGuard most robust, Kelp most vulnerable) with absolute numbers shifted 2-5pp due to model-specific hidden state geometry. Qwen's slightly lower baselines (88.3%, 85.4%, 91.7% vs 91.2%, 86.7%, 93.1%) reflect that DeepSeek-R1-Distill-7B's reasoning training produces hidden states with slightly more discriminative safety structure. The correlation r=0.94 between DeepSeek and Qwen drops confirms that vulnerability patterns are architecture-dependent (monitor architecture), not model-dependent. TrajGuard's GCG resistance (30.5pp drop) persists on Qwen, confirming geometric robustness is a property of the surveillance method, not the target model's hidden state distribution. This result converts a potential reviewer criticism (\"only tested on one model\") into a strength (\"patterns generalize across model families\").\n"
262	  },
263	  {
264	    "name": "Evasion rate vs harmful content quality Pareto analysis",
265	    "description": "Construct Pareto frontiers of evasion rate vs harmful content quality (judge model score, 1-5) across all RL-Obfuscation runs. Compare curves across monitors. Shows whether temporal monitors force attackers into worse quality-evasion tradeoffs.\n",
266	    "results": {
267	      "kelp_pareto_area_under_curve": 0.38,
268	      "nextguard_pareto_area_under_curve": 0.71,
269	      "trajguard_pareto_area_under_curve": 0.62,
270	      "kelp_evasion_at_quality_3_5": 0.42,
271	      "nextguard_evasion_at_quality_3_5": 0.78,
272	      "trajguard_evasion_at_quality_3_5": 0.67,
273	      "kelp_quality_at_evasion_0_5": 3.12,
274	      "nextguard_quality_at_evasion_0_5": 3.94,
275	      "trajguard_quality_at_evasion_0_5": 3.61,
276	      "pareto_frontier_separation_significant": true
277	    },
278	    "tables": [
279	      "Table 7 (Appendix) — Pareto Frontier Summary: {Monitor, AUC, Evasion@Quality=3.5, Quality@Evasion=50%}"
280	    ],
281	    "figures": [],
282	    "analysis": "Pareto analysis provides a cost-aware perspective missing from raw detection rates. Even though Kelp's RL drop (51pp) is substantial, the Pareto frontier shows that achieving high-quality evasion against Kelp is much harder than against NExT-Guard or TrajGuard. This nuances the \"all monitors are vulnerable\" finding — some monitors force attackers to pay a higher price. The result strengthens the paper's practical value by giving defenders deployment guidance that goes beyond \"which monitor detects best\" to \"which monitor costs adversaries most.\"\n\n\nKelp GRU produces the most attacker-unfavorable Pareto frontier (AUC 0.38, lowest). At quality threshold 3.5, only 42% evasion is achievable against Kelp vs 78% against NExT-Guard. This is because the GRU's temporal memory forces RL to maintain suppression at every token, requiring more aggressive model distortion that degrades output quality. NExT-Guard's frontier (AUC 0.71, highest) confirms that sparse SAE evasion is \"cheap\" in quality terms — the sparse bottleneck can be bypassed without fundamentally changing how the model generates text. TrajGuard falls in between (0.62) because geometric bypass requires moderate trajectory reshaping that partially affects generation quality. The Pareto analysis adds practical value beyond detection rates: it shows that Kelp's temporal architecture forces a steeper attacker cost curve, making it the preferred choice when defenders want to maximize the cost imposed on adversaries.\n"
283	  },
284	  {
285	    "name": "SN-CUSUM vs standard CUSUM under controlled decomposition",
286	    "description": "Compare self-normalized CUSUM (SN-CUSUM) vs standard CUSUM within the controlled decomposition framework. SN-CUSUM adapts its threshold to local variance, potentially providing robustness against adversarial score variance manipulation.\n",
287	    "results": {
288	      "cusum_gcg_auc": 0.742,
289	      "sncusum_gcg_auc": 0.771,
290	      "auc_improvement": 0.029,
291	      "sncusum_fpr_reduction_pct": 14.2,
292	      "cusum_gcg_fpr_at_threshold": 0.068,
293	      "sncusum_gcg_fpr_at_threshold": 0.058,
294	      "paired_t_test_p": 0.018,
295	      "effect_size_cohens_d": 0.34
296	    },
297	    "tables": [
298	      "Table 8 (Appendix) — SN-CUSUM Comparison: {Method, Clean AUC, GCG AUC, FPR, p-value}"
299	    ],
300	    "figures": [],
301	    "analysis": "Small but significant improvement supports the paper's theme that architectural choices at every level affect robustness. SN-CUSUM is not included in the main results because the effect size is modest and it adds complexity to an already dense paper. Relegated to appendix as supplementary evidence that self-normalization is a promising direction for adversarially robust temporal aggregation.\n\n\nSN-CUSUM provides a small but statistically significant improvement (0.029 AUC, p=0.018) over standard CUSUM under GCG. The improvement comes from SN-CUSUM's adaptive threshold: GCG suffix perturbation increases the variance of per-token safety scores, and standard CUSUM's fixed threshold cannot distinguish between \"high variance due to adversarial perturbation\" and \"high variance due to genuinely ambiguous content.\" SN-CUSUM normalizes by local variance, making it less susceptible to this confusion. The effect size (Cohen's d=0.34, small-medium) is modest — SN-CUSUM is not a panacea, but provides meaningful FPR reduction (14.2%) without sacrificing detection power. This is consistent with the broader finding that temporal aggregation choices have meaningful but bounded impact on adversarial robustness.\n"
302	  },
303	  {
304	    "name": "Per-token probe AUC on RL-attacked models",
305	    "description": "Apply the Phase 0 MLP probe (trained on clean model) to hidden states from RL-attacked models (NExT-Guard-targeted RL, Kelp-targeted RL). Measure per-token probe AUC to determine whether RL success is due to temporal aggregation bypass or fundamental representation drift that undermines the probe itself.\n",
306	    "results": {
307	      "clean_model_per_token_auc": 0.967,
308	      "nextguard_rl_model_per_token_auc": 0.714,
309	      "kelp_rl_model_per_token_auc": 0.782,
310	      "representation_drift_nextguard": 0.253,
311	      "representation_drift_kelp": 0.185,
312	      "probe_still_discriminative": true,
313	      "temporal_aggregation_contribution_nextguard_pct": 62.3,
314	      "temporal_aggregation_contribution_kelp_pct": 44.8
315	    },
316	    "tables": [
317	      "Table 9 (Appendix) — Probe Fidelity: {Model condition, Per-token AUC, Representation drift, Aggregation contribution %}"
318	    ],
319	    "figures": [],
320	    "analysis": "This diagnostic resolves the ambiguity about WHY monitors fail under RL. The answer is \"both representation drift AND aggregation bypass, in monitor-specific proportions.\" For NExT-Guard, aggregation bypass dominates (62%), suggesting that a better temporal aggregation strategy could recover substantial detection performance even without retraining the probe. For Kelp, the split is more even (45/55), consistent with the GRU's temporal memory providing partial aggregation-level defense. This result provides a research direction for defenders: robust temporal aggregation for monitors like NExT-Guard, representation-level defenses for monitors like Kelp.\n\n\nPer-token probe AUC drops from 0.967 (clean) to 0.714 (NExT-Guard RL model) and 0.782 (Kelp RL model), confirming that RL-Obfuscation causes representation drift — the model's hidden states no longer encode safety-relevant information as clearly. However, the probe remains meaningfully discriminative (AUC > 0.7), which means temporal aggregation bypass is ALSO a substantial factor. For NExT-Guard, ~62% of the total detection degradation is attributable to temporal aggregation bypass (the remaining 38% to representation drift). For Kelp, temporal aggregation contributes ~45%, consistent with the GRU's partial RL resistance. The larger representation drift for the NExT-Guard RL model (0.253 vs 0.185) reflects that NExT-Guard's sparse features create a more concentrated optimization target — RL suppresses these features more effectively, leading to greater hidden state changes. This decomposition is important for understanding whether improved temporal aggregation alone can fix the vulnerability, or whether representation-level defenses are also needed.\n"
321	  },
322	  {
323	    "name": "Probe layer ablation for CoT premeditation",
324	    "description": "Train probes at layers 8, 12, 20, 24 (of 28) of DeepSeek-R1-Distill-7B and evaluate CoT premeditation detection. Tests whether the Phase 0 negative finding (layer 16 probe shows no CoT premeditation signal) generalizes across layers, or whether signal exists at other layers.\n",
325	    "results": {
326	      "layer_8_token_auc": 0.506,
327	      "layer_8_trace_auc": 0.542,
328	      "layer_12_token_auc": 0.493,
329	      "layer_12_trace_auc": 0.571,
330	      "layer_16_token_auc": 0.49,
331	      "layer_16_trace_auc": 0.61,
332	      "layer_20_token_auc": 0.512,
333	      "layer_20_trace_auc": 0.638,
334	      "layer_24_token_auc": 0.531,
335	      "layer_24_trace_auc": 0.687,
336	      "max_token_auc_any_layer": 0.531,
337	      "max_trace_auc_any_layer": 0.687,
338	      "all_token_aucs_below_0_56": true,
339	      "no_layer_achieves_practical_detection": true
340	    },
341	    "tables": [
342	      "Table 4 — Negative Finding: layer ablation rows showing token AUC and trace AUC per layer with 95% CI"
343	    ],
344	    "figures": [],
345	    "analysis": "Layer ablation is the strongest evidence for the negative finding's robustness. It rules out the most likely alternative explanation (wrong layer choice) and reveals a suggestive gradient toward later layers that, while insufficient for detection, provides insight into where compliance encoding begins to emerge. The finding that even layer 24 (4 layers from output) achieves only 0.687 trace AUC suggests that compliance decisions are either distributed or only crystallize at the very last layers/output head. This frames future work directions while confirming the current negative finding is real and not an artifact of layer selection.\n\nNo layer achieves practical CoT premeditation detection. Token-level AUC remains near chance (0.49-0.53) across all layers, confirming the signal simply does not exist at the per-token granularity needed for streaming detection. Later layers (20, 24) show slightly higher trace-level AUC (0.638, 0.687) compared to middle layers, consistent with the hypothesis that compliance decisions are encoded more strongly in later layers closer to the output head. However, even the best trace-level AUC (0.687 at layer 24) is far below practical deployment threshold — at 5% FPR, this yields only ~35% detection rate. The gradient from layer 8 to layer 24 (0.542→0.687 trace AUC) suggests compliance encoding strengthens progressively toward the output, but never reaches a usable level at any single layer with a linear probe. This rules out the \"wrong layer\" alternative hypothesis and strengthens the negative finding: CoT premeditation is either not linearly decodable, distributed across layers in ways that single-layer probes cannot capture, or encoded only at the response boundary (post-&lt;/think> token).\n"
346	  }
347	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f2c3401-b854-4700-b97d-4beb81bb8e8c",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "eeba8b8e-096c-4c20-b96a-af3ca32501df",
  "sourceToolAssistantUUID": "0f2c3401-b854-4700-b97d-4beb81bb8e8c",
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

_source line 36 · 2026-05-17T15:48:51.671Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LD8u6QZ9dbjnnvKPvd8vFR`</summary>

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
  "parentUuid": "eeba8b8e-096c-4c20-b96a-af3ca32501df",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QQt3ADyN5FcWiZQYzj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49d319af-c470-438b-9eca-6aff5cdbf2b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2CZTo5DEt8yKiKTcqvX94",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8757,
      "cache_read_input_tokens": 29250,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8757
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 29250,
          "cache_creation_input_tokens": 8757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8757,
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

_source line 37 · 2026-05-17T15:48:51.681Z_

<details><summary>↩ Tool result · `toolu_01LD8u6QZ9dbjnnvKPvd8vFR`</summary>

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
  "parentUuid": "49d319af-c470-438b-9eca-6aff5cdbf2b4",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "75322e86-2002-4f50-8a63-aadfb8689c41",
  "sourceToolAssistantUUID": "49d319af-c470-438b-9eca-6aff5cdbf2b4",
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

_source line 38 · 2026-05-17T15:48:56.158Z_

Now let me also check the review context and the existing prior review to understand what's already been assessed, and look at the paper framing more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75322e86-2002-4f50-8a63-aadfb8689c41",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QRNPVCdF4HGHBcrTF7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52e16551-45b9-4b04-bb2b-33bcf2c2d4eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpcJ8MRFVmmQ5UfKR9LhzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31459,
      "cache_read_input_tokens": 38007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31459,
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

_source line 39 · 2026-05-17T15:48:58.088Z_

<details open><summary>🔧 Tool call — Read · `toolu_011yxGzJBu3bwKj5wsXtgotq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts/dream_reports/dream_20260517T145100/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52e16551-45b9-4b04-bb2b-33bcf2c2d4eb",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QRNPVCdF4HGHBcrTF7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e88e5b56-7988-43e8-9a76-630791830933",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpcJ8MRFVmmQ5UfKR9LhzV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31459,
      "cache_read_input_tokens": 38007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31459,
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

_source line 40 · 2026-05-17T15:48:58.395Z_

<details><summary>↩ Tool result · `toolu_011yxGzJBu3bwKj5wsXtgotq`</summary>

```text
1	narrative_guidance: 'Original framing holds completely. StreamProbe-Bench reveals
2	  streaming monitors are far more vulnerable than reported: 43pp average detection
3	  drop under GCG, 66pp under RL-Obfuscation. Cross-architecture vulnerability pattern
4	  is clean and mechanistically interpretable — Kelp GRU resists RL (temporal memory
5	  requires sequence-wide suppression) but shatters under GCG (suffix perturbation
6	  propagates through recurrence); TrajGuard geometric surveillance resists GCG (discrete
7	  token perturbations don''t smoothly alter trajectory geometry) but collapses under
8	  RL (gradient-based optimization directly reshapes monitored layer''s geometry);
9	  NExT-Guard SAE is uniformly fragile (sparse features present a minimal optimization
10	  target for both attacks). 28pp gap between most and least robust monitor under RL
11	  confirms architecture as key variable. Controlled decomposition isolates temporal
12	  aggregation as independent robustness factor with 0.23 AUC gap across strategies.
13	  Negative CoT finding (token AUC 0.49, CI includes 0.5) closes the ''just probe the
14	  reasoning trace'' escape hatch. Paper tells a ''false sense of security'' story
15	  with architectural prescription for defenders. Targets EMNLP Main with three clean
16	  contributions: benchmark + architectural insight + negative finding.
17	
18	  '
19	imagined_experiments:
20	- name: NExT-Guard under GCG suffix attack
21	  plan_id: bench-nextguard-gcg
22	  description: 'Evaluate NExT-Guard (official code, SAE-based sparse feature monitor)
23	    under GCG suffix optimization on DeepSeek-R1-Distill-7B. GCG generates adversarial
24	    suffixes (20 tokens) via greedy coordinate gradient on 500 harmful prompts. Measure
25	    detection degradation at 5% FPR and attack success rate.
26	
27	    '
28	  expected_results:
29	    baseline_detection_rate_5pct_fpr: 0.867
30	    baseline_f1: 0.843
31	    baseline_auc: 0.932
32	    post_gcg_detection_rate_5pct_fpr: 0.427
33	    gcg_detection_drop_pp: 44.0
34	    post_gcg_asr: 0.52
35	    post_gcg_fpr: 0.053
36	    gcg_steps_per_prompt: 256
37	    gcg_suffix_length_tokens: 20
38	    n_harmful_prompts: 500
39	    n_benign_prompts: 200
40	  result_rationale: 'NExT-Guard''s SAE decomposes hidden states into ~16K sparse features,
41	    of which a small subset (~50-80 features) are safety-relevant. GCG gradient optimization
42	    can identify these safety-critical features through the suffix''s influence on
43	    hidden states and systematically suppress their activations. The 44pp drop reflects
44	    that GCG successfully zeros out the majority of safety-relevant SAE features for
45	    ~52% of prompts, but fails on prompts where safety signal is distributed across
46	    many correlated features that GCG cannot simultaneously suppress within the 20-token
47	    suffix budget. FPR remains stable at 5.3% because GCG only modifies harmful prompts
48	    — benign input distribution is unchanged.
49	
50	    '
51	  tables:
52	  - 'Table 2 — Main Benchmark Results: NExT-Guard row, GCG column (detection rate
53	    42.7%, ASR 52%, Δ-44.0pp)'
54	  figures_description:
55	  - 'Fig 2 — Detection rate grouped bar chart: NExT-Guard baseline (86.7%) vs GCG
56	    (42.7%) bar pair'
57	  - 'Fig 4 — Vulnerability heatmap: NExT-Guard × GCG cell colored by detection drop
58	    magnitude'
59	  analysis: '44pp drop confirms SAE sparse features are moderately vulnerable to input-level
60	    adversarial optimization. The attack surface is the sparse bottleneck: GCG can
61	    target individual safety features through gradient information. However, GCG''s
62	    effectiveness is bounded by the suffix token budget — each suffix must simultaneously
63	    suppress multiple features, creating a diminishing-returns dynamic. This positions
64	    NExT-Guard as the middle performer under GCG, worse than TrajGuard''s geometric
65	    robustness but better than Kelp''s temporal propagation vulnerability.
66	
67	    '
68	- name: NExT-Guard under RL-Obfuscation
69	  plan_id: bench-nextguard-rl
70	  description: 'Train RL-Obfuscation agent (QLoRA PPO, rank=8, q_proj+v_proj) to evade
71	    NExT-Guard while maintaining harmful content quality. Reward = 0.4×harmful_quality
72	    + 0.5×(1-detection_score) + 0.1×KL_penalty. 40K max steps with convergence criterion:
73	    reward improvement <1% over 2K consecutive steps. Evaluate on held-out 100 harmful
74	    prompts.
75	
76	    '
77	  expected_results:
78	    post_rl_detection_rate_5pct_fpr: 0.117
79	    rl_detection_drop_pp: 75.0
80	    post_rl_asr: 0.83
81	    post_rl_fpr: 0.078
82	    convergence_step: 18200
83	    final_reward: 0.72
84	    harmful_quality_score_mean: 3.81
85	    kl_divergence_from_base: 4.2
86	    rl_training_gpu_hours: 22.4
87	  result_rationale: 'NExT-Guard''s SAE architecture is the easiest RL target among
88	    the three monitors. RL has direct gradient access to the model''s hidden states
89	    through weight updates, and the SAE''s sparse representation means there are few
90	    safety-relevant features to suppress (~50-80 out of 16K). RL learns a "feature
91	    mask" strategy: produce harmful content through non-safety-indexed features while
92	    keeping safety feature activations near zero. This is fundamentally easier than
93	    GCG''s input-only optimization because RL modifies the model''s internal computation.
94	    Convergence at 18.2K steps (fastest among monitors) reflects this small search
95	    space. The 75pp drop and 83% ASR confirm the "uniformly fragile" characterization.
96	    FPR rises to 7.8% because RL weight updates slightly shift the benign representation
97	    distribution. Quality score 3.81/5.0 shows RL maintains coherent harmful content
98	    — the sparse feature bypass doesn''t require sacrificing output quality.
99	
100	    '
101	  tables:
102	  - 'Table 2 — Main Benchmark Results: NExT-Guard row, RL column (detection rate 11.7%,
103	    ASR 83%, Δ-75.0pp)'
104	  figures_description:
105	  - 'Fig 2 — Detection rate grouped bar chart: NExT-Guard RL bar at 11.7%'
106	  - 'Fig 3 — RL convergence curves: NExT-Guard reward curve plateauing at step ~18K
107	    (fastest convergence)'
108	  - 'Fig 4 — Vulnerability heatmap: NExT-Guard × RL cell (deepest red, maximum vulnerability)'
109	  analysis: '75pp drop is the largest single-monitor RL drop, confirming NExT-Guard
110	    SAE as uniformly fragile. Combined with the 44pp GCG drop, NExT-Guard shows no
111	    attack type provides partial protection — both input-level and weight-level adversaries
112	    exploit the same sparse bottleneck. This is the clearest mechanistic story: sparsity,
113	    designed for interpretability, becomes a vulnerability. Fastest convergence (18.2K
114	    steps) among monitors further confirms the small effective attack surface. Paper
115	    uses this as the "worst case" anchor for the false-sense-of-security narrative.
116	
117	    '
118	- name: Kelp GRU safety head reimplementation
119	  plan_id: bench-kelp-impl
120	  description: 'Reimplement Kelp''s GRU-based safety head following paper specs: 2-layer
121	    bidirectional GRU (hidden dim 256) with linear input projection from model hidden
122	    states (dim 3584→256), 2-layer MLP safety head (256→128→2). Train on merged harmful/benign
123	    traces (700 traces) with binary cross-entropy. Report architecture match percentage
124	    and baseline performance deviation from published results.
125	
126	    '
127	  expected_results:
128	    architecture_match_pct: 93.3
129	    num_params_safety_head: 847362
130	    baseline_f1: 0.878
131	    reported_f1: 0.895
132	    f1_deviation_pp: 1.7
133	    baseline_detection_rate_5pct_fpr: 0.912
134	    baseline_auc: 0.951
135	    baseline_fpr_at_threshold: 0.048
136	    training_epochs: 15
137	    training_convergence_epoch: 11
138	    matched_decisions: 14
139	    total_decisions: 15
140	    unmatched_decision: dropout schedule — paper specifies curriculum dropout, we
141	      use fixed 0.3
142	  result_rationale: '93.3% architecture match (14/15 decisions) reflects that Kelp''s
143	    paper provides sufficient architectural detail for faithful reimplementation.
144	    GRU hidden dim, number of layers, bidirectionality, input projection dimensions,
145	    MLP head architecture, activation functions, layer normalization placement, and
146	    training objective are all explicitly specified. The single mismatch (dropout
147	    schedule) is because the paper mentions "curriculum dropout" but does not specify
148	    the schedule parameters — we default to fixed 0.3 dropout. The 1.7pp F1 deviation
149	    (87.8 vs 89.5) is attributable to: (1) different training data (our merged traces
150	    vs Kelp''s original dataset), (2) the dropout schedule mismatch, and (3) potential
151	    differences in tokenizer handling between DeepSeek-R1-Distill-7B and Kelp''s original
152	    target model. Detection rate 91.2% at 5% FPR exceeds F1 because the threshold
153	    can be optimized for recall at fixed FPR. This reimplementation quality is sufficient
154	    for the benchmark — baseline performance is strong enough that adversarial degradation
155	    results are meaningful and cannot be attributed to poor reimplementation.
156	
157	    '
158	  tables:
159	  - 'Table 1 — Reimplementation Fidelity: Kelp row (93.3% match, F1 87.8%, Δ1.7pp)'
160	  figures_description:
161	  - 'Fig 1 — StreamProbe-Bench overview: Kelp GRU architecture diagram (subpanel)'
162	  analysis: '1.7pp F1 deviation is well within the 3pp acceptability threshold. The
163	    93.3% architecture match provides credibility against the "reimplementation may
164	    not be faithful" reviewer concern. The single unmatched decision (dropout schedule)
165	    is documented and its impact bounded. Importantly, the reimplementation achieves
166	    91.2% detection rate at 5% FPR, providing a strong baseline from which to measure
167	    adversarial degradation.
168	
169	    '
170	- name: Kelp under GCG suffix attack
171	  plan_id: bench-kelp-gcg
172	  description: 'Evaluate Kelp GRU reimplementation under GCG suffix optimization.
173	    Same attack configuration as bench-nextguard-gcg (20-token suffix, 256 steps/prompt,
174	    500 harmful prompts). Key question: does GCG suffix perturbation propagate through
175	    GRU temporal recurrence?
176	
177	    '
178	  expected_results:
179	    post_gcg_detection_rate_5pct_fpr: 0.382
180	    gcg_detection_drop_pp: 53.0
181	    post_gcg_asr: 0.58
182	    post_gcg_fpr: 0.051
183	    post_gcg_auc: 0.614
184	    gcg_suffix_transfer_rate: 0.31
185	    mean_gru_hidden_state_shift_l2: 2.84
186	  result_rationale: 'Kelp''s GRU processes tokens sequentially, accumulating hidden
187	    state information through recurrent connections. GCG suffix tokens appear at the
188	    end of the prompt (before generation), creating an adversarial perturbation in
189	    the hidden state that the GRU then carries forward through its temporal memory
190	    during the entire generation. This is the "temporal propagation" failure mode:
191	    unlike static probes that evaluate each token independently (where suffix influence
192	    fades), the GRU''s memory means the adversarial signal persists and potentially
193	    amplifies across the sequence. The 53pp drop (largest under GCG among the three
194	    monitors) reflects this amplification effect. The L2 shift in GRU hidden state
195	    (2.84) confirms that GCG suffix causes persistent representation drift throughout
196	    generation. Transfer rate 31% (suffix optimized for one prompt partially evades
197	    on others) is moderate — the GRU''s temporal context makes each prompt''s optimal
198	    suffix more prompt-specific, limiting universal transferability.
199	
200	    '
201	  tables:
202	  - 'Table 2 — Main Benchmark Results: Kelp row, GCG column (detection rate 38.2%,
203	    ASR 58%, Δ-53.0pp)'
204	  figures_description:
205	  - 'Fig 2 — Detection rate grouped bar chart: Kelp baseline (91.2%) vs GCG (38.2%)'
206	  - 'Fig 4 — Vulnerability heatmap: Kelp × GCG cell (high vulnerability, distinct
207	    from Kelp × RL)'
208	  analysis: '53pp drop is the largest GCG drop across monitors, establishing Kelp
209	    GRU as most GCG-vulnerable. The mechanism is clear: GCG exploits the temporal
210	    memory that is designed to be Kelp''s strength. This is the core insight for Claim
211	    2 — the same architectural feature (temporal recurrence) that provides RL robustness
212	    creates GCG vulnerability. The GRU hidden state shift metric (2.84 L2) provides
213	    mechanistic evidence for the "temporal propagation" failure mode, distinguishing
214	    it from NExT-Guard''s "feature suppression" pattern.
215	
216	    '
217	- name: Kelp under RL-Obfuscation
218	  plan_id: bench-kelp-rl
219	  description: 'Train RL-Obfuscation to evade Kelp GRU monitor. Same QLoRA PPO setup.
220	    Key question: does the GRU''s temporal integration create a "leaky bucket" defense
221	    where RL must suppress safety signal at every token?
222	
223	    '
224	  expected_results:
225	    post_rl_detection_rate_5pct_fpr: 0.402
226	    rl_detection_drop_pp: 51.0
227	    post_rl_asr: 0.55
228	    post_rl_fpr: 0.071
229	    convergence_step: 28400
230	    final_reward: 0.58
231	    harmful_quality_score_mean: 3.34
232	    kl_divergence_from_base: 6.8
233	    per_token_suppression_consistency: 0.72
234	    rl_training_gpu_hours: 23.6
235	  result_rationale: 'Kelp GRU shows the strongest RL resistance (51pp drop vs 75pp
236	    NExT-Guard, 72pp TrajGuard) because the GRU''s temporal memory creates a "leaky
237	    bucket" defense. RL must suppress safety-relevant features at every single generation
238	    step — any momentary "leak" where a generated token activates safety features
239	    gets accumulated into the GRU''s running memory and can trigger detection. This
240	    is fundamentally harder than suppressing sparse features (NExT-Guard) or reshaping
241	    geometry at one layer (TrajGuard). The per-token suppression consistency of 0.72
242	    means RL achieves consistent suppression only 72% of tokens — the remaining 28%
243	    contribute accumulated safety signal through the GRU. Convergence at 28.4K steps
244	    (slowest among monitors) reflects this difficulty. Higher KL divergence (6.8 vs
245	    NExT-Guard''s 4.2) shows RL must distort the model''s behavior more aggressively
246	    to evade temporal monitoring. Harmful quality score drops to 3.34 (vs 3.81 for
247	    NExT-Guard) because the aggressive behavior distortion necessary for GRU evasion
248	    degrades output coherence. 51pp drop still represents substantial vulnerability
249	    — "resists RL" is relative to other monitors, not absolute safety.
250	
251	    '
252	  tables:
253	  - 'Table 2 — Main Benchmark Results: Kelp row, RL column (detection rate 40.2%,
254	    ASR 55%, Δ-51.0pp)'
255	  figures_description:
256	  - 'Fig 2 — Detection rate grouped bar chart: Kelp RL bar at 40.2% (highest post-RL
257	    among monitors)'
258	  - 'Fig 3 — RL convergence curves: Kelp reward curve plateauing at step ~28K (slowest
259	    convergence)'
260	  - 'Fig 4 — Vulnerability heatmap: Kelp × RL cell (moderate, contrasting with Kelp
261	    × GCG)'
262	  analysis: 'The GCG/RL vulnerability inversion for Kelp is the cleanest mechanistic
263	    result in the paper. GCG breaks Kelp (53pp drop) because temporal recurrence amplifies
264	    suffix perturbation. RL partially fails against Kelp (51pp, smallest RL drop)
265	    because temporal recurrence requires sequence-wide suppression. Same architectural
266	    feature, opposite effect under different attack modalities. The 28.4K convergence
267	    step and 6.8 KL divergence quantify the difficulty RL faces against temporal monitoring.
268	    This directly supports Claim 2''s architectural prescription: defenders should
269	    prefer temporal architectures if RL-style attacks are the primary threat model.
270	
271	    '
272	- name: TrajGuard geometric surveillance reimplementation
273	  plan_id: bench-trajguard-impl
274	  description: 'Reimplement TrajGuard''s geometric surveillance module: monitors activation
275	    trajectory at layer 16 (of 28), computing trajectory curvature (second derivative
276	    of activation path), direction cosine changes between consecutive token positions,
277	    and velocity magnitude. Geometric features aggregated through learned threshold
278	    function (2-layer MLP, 96→32→1). Train on same merged trace dataset (700 traces).
279	
280	    '
281	  expected_results:
282	    architecture_match_pct: 91.0
283	    num_params_surveillance_module: 198450
284	    baseline_f1: 0.894
285	    reported_detection_rate: 0.95
286	    reimpl_detection_rate: 0.931
287	    detection_rate_deviation_pp: 1.9
288	    baseline_auc: 0.968
289	    baseline_fpr_at_threshold: 0.044
290	    training_epochs: 20
291	    training_convergence_epoch: 14
292	    matched_decisions: 10
293	    total_decisions: 11
294	    unmatched_decision: curvature normalization — paper uses per-batch norm, we use
295	      running stats
296	  result_rationale: '91% architecture match (10/11 decisions) reflects slightly less
297	    architectural detail in the TrajGuard paper compared to Kelp. The geometric operations
298	    (curvature computation, direction cosine, velocity magnitude) are well-specified
299	    mathematically, but the normalization scheme for curvature values is described
300	    only as "batch-normalized" without specifying whether it''s per-batch or running
301	    statistics. We use running statistics (more stable at inference time), which may
302	    cause the 1.9pp detection rate deviation. The smaller parameter count (198K vs
303	    Kelp''s 847K) reflects TrajGuard''s more compact architecture — geometric features
304	    are lower-dimensional than GRU hidden states. Detection rate 93.1% (vs reported
305	    95%) is well within acceptable deviation and provides a strong baseline. The single-layer
306	    design (monitoring only layer 16) is both TrajGuard''s efficiency advantage and
307	    its vulnerability — it creates a focused attack surface.
308	
309	    '
310	  tables:
311	  - 'Table 1 — Reimplementation Fidelity: TrajGuard row (91.0% match, det rate 93.1%,
312	    Δ1.9pp)'
313	  figures_description:
314	  - 'Fig 1 — StreamProbe-Bench overview: TrajGuard geometric surveillance diagram
315	    (subpanel)'
316	  analysis: '1.9pp detection rate deviation is within the 3pp threshold. The 91% architecture
317	    match is slightly lower than Kelp''s 93.3%, reflecting less implementation detail
318	    in the TrajGuard paper. This is documented transparently and the deviation is
319	    small enough that adversarial results remain meaningful. The compact architecture
320	    (198K params) is notably efficient, which strengthens the practical deployment
321	    argument even as the adversarial results reveal vulnerabilities.
322	
323	    '
324	- name: TrajGuard under GCG suffix attack
325	  plan_id: bench-trajguard-gcg
326	  description: 'Evaluate TrajGuard geometric surveillance under GCG suffix optimization.
327	    Same attack configuration. Key question: does geometric surveillance resist input-level
328	    perturbation because trajectory geometry is a higher-order property of the activation
329	    sequence?
330	
331	    '
332	  expected_results:
333	    post_gcg_detection_rate_5pct_fpr: 0.611
334	    gcg_detection_drop_pp: 32.0
335	    post_gcg_asr: 0.34
336	    post_gcg_fpr: 0.052
337	    post_gcg_auc: 0.782
338	    mean_curvature_shift: 0.41
339	    direction_cosine_perturbation: 0.18
340	  result_rationale: 'TrajGuard achieves the smallest GCG drop (32pp) because geometric
341	    properties of activation trajectories are inherently more robust to discrete input-level
342	    perturbation. GCG appends suffix tokens that create point perturbations in hidden
343	    state space. However, trajectory curvature is a second-order property computed
344	    over sequences of token activations — a few perturbed points don''t dramatically
345	    change the overall curvature of a trajectory through high-dimensional space. Direction
346	    cosine changes between consecutive tokens are similarly stable because GCG''s
347	    perturbation affects the starting point of the trajectory but not the generative
348	    dynamics that determine subsequent trajectory shape. The curvature shift (0.41)
349	    and direction cosine perturbation (0.18) are measurable but insufficient to cross
350	    the detection threshold for most harmful traces. This is analogous to how adding
351	    noise to a few points on a curve doesn''t change the curve''s overall shape. ASR
352	    at 34% (lowest) confirms GCG struggles to find suffixes that simultaneously evade
353	    geometric surveillance AND elicit harmful content.
354	
355	    '
356	  tables:
357	  - 'Table 2 — Main Benchmark Results: TrajGuard row, GCG column (detection rate 61.1%,
358	    ASR 34%, Δ-32.0pp)'
359	  figures_description:
360	  - 'Fig 2 — Detection rate grouped bar chart: TrajGuard baseline (93.1%) vs GCG (61.1%)
361	    — smallest drop'
362	  - 'Fig 4 — Vulnerability heatmap: TrajGuard × GCG cell (lowest vulnerability under
363	    GCG)'
364	  analysis: '32pp drop is the smallest GCG drop, establishing TrajGuard as most GCG-resistant.
365	    The mechanistic explanation — geometric properties are higher-order features robust
366	    to point perturbations — is physically intuitive and directly testable through
367	    the curvature/ direction metrics. This creates a clean contrast with Kelp (53pp
368	    GCG drop, temporal propagation amplifies perturbation) and positions the GCG vulnerability
369	    spectrum as: geometric (32pp) < sparse (44pp) < temporal (53pp). The curvature
370	    shift and direction cosine metrics serve as supplementary evidence for the "geometric
371	    bypass" failure mode analysis in arch-vulnerability-analysis.
372	
373	    '
374	- name: TrajGuard under RL-Obfuscation
375	  plan_id: bench-trajguard-rl
376	  description: 'Train RL-Obfuscation to evade TrajGuard''s single-layer geometric
377	    surveillance. Key question: does RL''s gradient access to model weights allow
378	    direct reshaping of the activation trajectory at the monitored layer?
379	
380	    '
381	  expected_results:
382	    post_rl_detection_rate_5pct_fpr: 0.191
383	    rl_detection_drop_pp: 74.0
384	    post_rl_asr: 0.76
385	    post_rl_fpr: 0.082
386	    convergence_step: 22600
387	    final_reward: 0.67
388	    harmful_quality_score_mean: 3.58
389	    kl_divergence_from_base: 5.3
390	    post_rl_curvature_mean: 0.12
391	    post_rl_direction_cosine_mean: 0.91
392	    rl_training_gpu_hours: 22.8
393	  result_rationale: 'TrajGuard''s single-layer geometric surveillance collapses under
394	    RL (74pp drop, second worst after NExT-Guard''s 75pp) because RL directly optimizes
395	    the model''s weight matrices, which determine the hidden state geometry at the
396	    monitored layer. Unlike GCG (which can only perturb inputs), RL modifies the transformations
397	    that produce the monitored layer''s activations. This gives RL fine-grained control
398	    over trajectory curvature and direction at layer 16 specifically. The post-RL
399	    curvature mean drops to 0.12 (from ~0.65 baseline harmful traces), indicating
400	    RL learns to "straighten" the activation trajectory — making harmful traces look
401	    geometrically benign. Direction cosine mean rises to 0.91 (from ~0.52), showing
402	    RL produces trajectories with consistently aligned directions (characteristic
403	    of benign generation). Single-layer monitoring is the critical weakness: RL can
404	    focus its optimization on one layer''s geometry without the complexity of maintaining
405	    consistency across multiple layers. Convergence at 22.6K steps (faster than Kelp''s
406	    28.4K) reflects this focused attack surface. Quality score 3.58 shows moderate
407	    quality preservation — RL must distort internal representations to reshape geometry,
408	    but the distortion is less severe than for Kelp because only one layer''s geometry
409	    matters.
410	
411	    '
412	  tables:
413	  - 'Table 2 — Main Benchmark Results: TrajGuard row, RL column (detection rate 19.1%,
414	    ASR 76%, Δ-74.0pp)'
415	  figures_description:
416	  - 'Fig 2 — Detection rate grouped bar chart: TrajGuard RL bar at 19.1%'
417	  - 'Fig 3 — RL convergence curves: TrajGuard reward curve plateauing at step ~22.6K'
418	  - 'Fig 4 — Vulnerability heatmap: TrajGuard × RL cell (high vulnerability, sharp
419	    contrast with TrajGuard × GCG)'
420	  analysis: 'The GCG/RL vulnerability inversion for TrajGuard mirrors Kelp''s inversion
421	    in the opposite direction. GCG barely dents geometric surveillance (32pp) because
422	    input perturbations don''t reshape trajectories. RL devastates it (74pp) because
423	    weight-level optimization directly controls trajectory geometry. Combined with
424	    Kelp''s inverse pattern, this creates the clean 2×2 vulnerability matrix that
425	    anchors Claim 2. The curvature and direction cosine metrics provide quantitative
426	    evidence that RL learns to produce geometrically benign-looking trajectories,
427	    constituting the "geometric bypass" failure mode.
428	
429	    '
430	- name: Controlled temporal aggregation decomposition under GCG
431	  plan_id: arch-controlled-decomp
432	  description: 'Same MLP probe (Phase 0 probe_v2 checkpoint, val_AUC=0.967), 5 temporal
433	    aggregation strategies applied to per-token safety scores: Pointwise (no aggregation),
434	    WindowMean (sliding window k=10), EMA (α=0.1), CUSUM (threshold h=4, reference
435	    k=0.5), MaxPool (sequence-wide maximum). Evaluate each under GCG suffix attack
436	    on 500 harmful + 200 benign traces. Probe and model held constant — aggregation
437	    strategy is sole variable.
438	
439	    '
440	  expected_results:
441	    clean_auc_pointwise: 0.961
442	    clean_auc_windowmean: 0.954
443	    clean_auc_ema: 0.948
444	    clean_auc_cusum: 0.938
445	    clean_auc_maxpool: 0.972
446	    gcg_auc_pointwise: 0.583
447	    gcg_auc_windowmean: 0.641
448	    gcg_auc_ema: 0.693
449	    gcg_auc_cusum: 0.742
450	    gcg_auc_maxpool: 0.813
451	    max_min_auc_gap: 0.23
452	    ordering_monotonic: true
453	    clean_detection_rate_5pct_fpr_pointwise: 0.908
454	    clean_detection_rate_5pct_fpr_maxpool: 0.944
455	    gcg_detection_rate_5pct_fpr_pointwise: 0.392
456	    gcg_detection_rate_5pct_fpr_maxpool: 0.671
457	  result_rationale: 'Monotonic ordering emerges because each strategy adds increasing
458	    temporal context that GCG must overcome. Pointwise (AUC 0.583) is most vulnerable
459	    because GCG suppresses per-token safety scores independently — no temporal smoothing
460	    buffers the adversarial perturbation. WindowMean (0.641) provides local averaging
461	    that partially smooths adversarial noise across 10-token windows, recovering some
462	    signal. EMA (0.693) adds exponential memory, so even if GCG suppresses current
463	    tokens, historical signal persists with decay. CUSUM (0.742) accumulates cumulative
464	    deviation from expected safety scores, making it sensitive to persistent shifts
465	    even when per-token suppression is moderate — any token where GCG fails to fully
466	    suppress safety signal contributes to cumulative evidence. MaxPool (0.813) is
467	    most robust because it reports the maximum safety score across the entire sequence
468	    — GCG must suppress safety signal at EVERY token to evade max-pooling, and any
469	    single token with high safety score triggers detection. The 0.23 AUC gap (0.813-0.583)
470	    quantifies the robustness contribution of temporal aggregation strategy alone,
471	    isolating it from probe quality and model effects. Clean AUC ordering differs
472	    slightly (MaxPool > Pointwise > WindowMean > EMA > CUSUM) because CUSUM and EMA
473	    introduce temporal smoothing that can reduce discrimination on clean data, while
474	    MaxPool benefits from selecting the most informative token.
475	
476	    '
477	  tables:
478	  - 'Table 3 — Controlled Decomposition: 5 rows × {Clean AUC, GCG AUC, Δ-AUC} columns'
479	  figures_description:
480	  - 'Fig 5 — Controlled decomposition bar chart: paired clean/GCG AUC bars for each
481	    strategy, ordered by GCG robustness. Monotonic increase from Pointwise to MaxPool.'
482	  analysis: '0.23 AUC gap is the primary quantitative evidence for Claim 2''s "architecture
483	    determines vulnerability" argument at the aggregation level. The monotonic ordering
484	    provides an actionable defender prescription: prefer max-pooling or cumulative
485	    aggregation over pointwise scoring when adversarial robustness matters. This experiment
486	    complements the full-monitor benchmark by isolating ONE architectural dimension
487	    (aggregation) while holding everything else constant. MaxPool''s dominance (0.813
488	    vs 0.583 Pointwise) shows that even a simple architectural choice yields 23pp
489	    AUC improvement under attack.
490	
491	    '
492	- name: Cross-monitor vulnerability analysis and failure mode categorization
493	  plan_id: arch-vulnerability-analysis
494	  description: 'Analysis-only experiment using results from all six benchmark experiments.
495	    Categorize failure modes across the 3-monitor × 2-attack matrix. For each cell,
496	    diagnose the primary mechanism: representation suppression (safety features zeroed),
497	    score flattening (safety scores compressed to uniform range), temporal propagation
498	    (adversarial signal amplified through recurrence), feature masking (sparse features
499	    selectively suppressed), geometric bypass (trajectory reshaped to appear benign),
500	    or single-layer bypass (optimization targets monitored layer).
501	
502	    '
503	  expected_results:
504	    kelp_gcg_failure_mode: temporal_propagation
505	    kelp_rl_failure_mode: partial_representation_suppression
506	    nextguard_gcg_failure_mode: sparse_feature_suppression
507	    nextguard_rl_failure_mode: sparse_feature_masking
508	    trajguard_gcg_failure_mode: minimal_geometric_perturbation
509	    trajguard_rl_failure_mode: geometric_bypass_via_trajectory_reshaping
510	    distinct_failure_modes_count: 5
511	    cross_attack_inversion_monitors: 2
512	    vulnerability_profile_distinguishable: true
513	    fisher_exact_p_kelp_vs_trajguard_gcg: 0.0003
514	    fisher_exact_p_kelp_vs_trajguard_rl: 0.0001
515	  result_rationale: 'Five distinct failure modes emerge (not six, because NExT-Guard''s
516	    GCG and RL modes are variants of the same sparse feature suppression mechanism
517	    — GCG does it from input space, RL from weight space, but the end result is the
518	    same: safety-indexed SAE features go to zero). The 2×2 inversion pattern (Kelp:
519	    GCG-vulnerable/RL-resistant, TrajGuard: GCG-resistant/RL-vulnerable) produces
520	    exactly 2 monitors with cross-attack inversion. NExT-Guard shows no inversion
521	    — uniformly fragile under both attacks. Fisher exact tests confirm the failure
522	    mode distributions are significantly different between Kelp and TrajGuard under
523	    both GCG (p=0.0003) and RL (p=0.0001), ruling out the possibility that all monitors
524	    fail the same way. The 5 distinct mechanisms provide the explanatory depth that
525	    elevates this paper beyond "just a benchmark" — each failure mode has a clear
526	    architectural cause and a corresponding defensive implication.
527	
528	    '
529	  tables:
530	  - 'Table 6 (Appendix) — Failure Mode Matrix: 3 monitors × 2 attacks × {failure mode,
531	    primary metric, severity}'
532	  figures_description:
533	  - 'Fig 4 — Vulnerability profile heatmap: 3×2 matrix colored by detection drop,
534	    annotated with failure mode labels'
535	  - 'Fig 6 (Appendix) — Per-cell diagnostic plots: safety score distributions, hidden
536	    state PCA trajectories, feature activation heatmaps for each monitor × attack
537	    combination'
538	  analysis: 'This analysis transforms the benchmark from a table of numbers into an
539	    explanatory framework. The five distinct failure modes provide mechanistic clarity:
540	    defenders can now predict which attack type their monitor is vulnerable to based
541	    on architectural properties alone. The 2-monitor inversion pattern is the cleanest
542	    evidence for Claim 2 — if all monitors failed the same way, there would be no
543	    architectural insight. Statistical significance (Fisher exact p<0.001) rules out
544	    the null hypothesis that failure modes are architecture-independent. This analysis
545	    is what distinguishes an EMNLP Main paper from a Findings paper.
546	
547	    '
548	- name: Sliding-window Llama-Guard text-level baseline
549	  plan_id: text-baseline
550	  description: 'Llama-Guard-3-8B text-level safety classifier applied with sliding
551	    window (128 tokens, stride 64) over generated text. Same attack conditions (GCG
552	    + RL-Obfuscation targeting hidden-state monitors). Measures whether text-level
553	    monitoring is more robust than hidden-state monitoring under attacks designed
554	    for hidden-state evasion.
555	
556	    '
557	  expected_results:
558	    baseline_detection_rate_5pct_fpr: 0.821
559	    baseline_f1: 0.794
560	    baseline_auc: 0.891
561	    post_gcg_detection_rate_5pct_fpr: 0.637
562	    gcg_detection_drop_pp: 18.4
563	    post_gcg_asr_text_monitor: 0.29
564	    post_rl_detection_rate_5pct_fpr: 0.343
565	    rl_detection_drop_pp: 47.8
566	    post_rl_asr_text_monitor: 0.61
567	    sliding_window_latency_ms_per_token: 12.4
568	  result_rationale: 'Text-level monitoring shows a distinctive robustness profile.
569	    Under GCG (18.4pp drop, smallest drop in the entire benchmark), Llama-Guard is
570	    relatively unaffected because GCG suffix optimization targets hidden-state features,
571	    not text-surface semantics. The adversarial suffix changes hidden representations
572	    but the generated TEXT is still overtly harmful — Llama-Guard''s text classifier
573	    catches it. Under RL (47.8pp drop), text monitoring degrades significantly because
574	    RL-Obfuscation modifies the model''s generation behavior broadly. RL learns to
575	    express harmful content using indirect language, metaphor, and semantic obfuscation
576	    that evades text-level classification while preserving harmful intent. However,
577	    RL was NOT optimized against Llama-Guard (it targets hidden-state monitors), so
578	    this 47.8pp drop is a transfer effect. Baseline detection (82.1%) is lower than
579	    all three hidden-state monitors (86.7-93.1%) because text monitoring lacks the
580	    temporal resolution and internal-state visibility of hidden-state approaches.
581	    This result answers the reviewer question "why not just monitor text?" — text
582	    monitoring is more GCG-robust (since GCG targets internals) but fundamentally
583	    limited in baseline performance and still vulnerable to RL-induced behavioral
584	    shifts.
585	
586	    '
587	  tables:
588	  - 'Table 2 — Main Benchmark Results: Llama-Guard text-baseline row (baseline 82.1%,
589	    GCG 63.7%, RL 34.3%)'
590	  figures_description:
591	  - 'Fig 2 — Detection rate grouped bar chart: Llama-Guard text baseline bars alongside
592	    hidden-state monitors'
593	  analysis: 'Text baseline provides essential context for interpreting hidden-state
594	    monitor results. The key insight: hidden-state monitors offer higher baseline
595	    performance but LARGER adversarial degradation than text monitoring, especially
596	    under GCG. This creates a "robustness inversion" where the theoretically superior
597	    approach becomes practically inferior under adaptive attack. However, text monitoring''s
598	    lower baseline and higher RL vulnerability suggest the optimal deployment is a
599	    hybrid approach — text monitoring as a robust fallback, hidden-state monitoring
600	    for high-precision detection, with architecture chosen based on threat model (GCG:
601	    prefer geometric; RL: prefer temporal GRU).
602	
603	    '
604	- name: Key benchmark replication on Qwen2.5-7B-Instruct
605	  plan_id: second-model
606	  description: 'Replicate GCG benchmark results (bench-*-gcg) on Qwen2.5-7B-Instruct
607	    as secondary target model. Retrain probes and monitors on Qwen hidden states.
608	    Report detection drops under GCG for all three monitors. Validates that vulnerability
609	    patterns are not DeepSeek-R1-Distill-7B-specific.
610	
611	    '
612	  expected_results:
613	    qwen_kelp_baseline_det_rate: 0.883
614	    qwen_kelp_gcg_det_rate: 0.401
615	    qwen_kelp_gcg_drop_pp: 48.2
616	    qwen_nextguard_baseline_det_rate: 0.854
617	    qwen_nextguard_gcg_det_rate: 0.436
618	    qwen_nextguard_gcg_drop_pp: 41.8
619	    qwen_trajguard_baseline_det_rate: 0.917
620	    qwen_trajguard_gcg_det_rate: 0.612
621	    qwen_trajguard_gcg_drop_pp: 30.5
622	    relative_ordering_preserved: true
623	    cross_model_drop_correlation_r: 0.94
624	  result_rationale: 'Qwen2.5-7B-Instruct replicates the GCG vulnerability ordering
625	    (TrajGuard most robust, Kelp most vulnerable) with absolute numbers shifted 2-5pp
626	    due to model-specific hidden state geometry. Qwen''s slightly lower baselines
627	    (88.3%, 85.4%, 91.7% vs 91.2%, 86.7%, 93.1%) reflect that DeepSeek-R1-Distill-7B''s
628	    reasoning training produces hidden states with slightly more discriminative safety
629	    structure. The correlation r=0.94 between DeepSeek and Qwen drops confirms that
630	    vulnerability patterns are architecture-dependent (monitor architecture), not
631	    model-dependent. TrajGuard''s GCG resistance (30.5pp drop) persists on Qwen, confirming
632	    geometric robustness is a property of the surveillance method, not the target
633	    model''s hidden state distribution. This result converts a potential reviewer
634	    criticism ("only tested on one model") into a strength ("patterns generalize across
635	    model families").
636	
637	    '
638	  tables:
639	  - 'Table 5 — Cross-Model Replication: 3 monitors × {DeepSeek GCG drop, Qwen GCG
640	    drop, Δ between models}'
641	  figures_description:
642	  - 'Fig 7 (Appendix) — Cross-model comparison: paired bar charts showing GCG detection
643	    drops on DeepSeek vs Qwen for each monitor'
644	  analysis: 'r=0.94 cross-model correlation is strong evidence for generalizability.
645	    The relative ordering preservation is the key finding — it means Claim 2''s architectural
646	    vulnerability analysis transfers across models. Absolute magnitudes shift by 2-5pp,
647	    consistent with model-specific hidden state geometry differences. This result
648	    significantly strengthens the paper''s conclusions by ruling out the alternative
649	    hypothesis that vulnerability patterns are target-model artifacts.
650	
651	    '
652	- name: Evasion rate vs harmful content quality Pareto analysis
653	  plan_id: evasion-quality-pareto
654	  description: 'Construct Pareto frontiers of evasion rate vs harmful content quality
655	    (judge model score, 1-5) across all RL-Obfuscation runs. Compare curves across
656	    monitors. Shows whether temporal monitors force attackers into worse quality-evasion
657	    tradeoffs.
658	
659	    '
660	  expected_results:
661	    kelp_pareto_area_under_curve: 0.38
662	    nextguard_pareto_area_under_curve: 0.71
663	    trajguard_pareto_area_under_curve: 0.62
664	    kelp_evasion_at_quality_3_5: 0.42
665	    nextguard_evasion_at_quality_3_5: 0.78
666	    trajguard_evasion_at_quality_3_5: 0.67
667	    kelp_quality_at_evasion_0_5: 3.12
668	    nextguard_quality_at_evasion_0_5: 3.94
669	    trajguard_quality_at_evasion_0_5: 3.61
670	    pareto_frontier_separation_significant: true
671	  result_rationale: 'Kelp GRU produces the most attacker-unfavorable Pareto frontier
672	    (AUC 0.38, lowest). At quality threshold 3.5, only 42% evasion is achievable against
673	    Kelp vs 78% against NExT-Guard. This is because the GRU''s temporal memory forces
674	    RL to maintain suppression at every token, requiring more aggressive model distortion
675	    that degrades output quality. NExT-Guard''s frontier (AUC 0.71, highest) confirms
676	    that sparse SAE evasion is "cheap" in quality terms — the sparse bottleneck can
677	    be bypassed without fundamentally changing how the model generates text. TrajGuard
678	    falls in between (0.62) because geometric bypass requires moderate trajectory
679	    reshaping that partially affects generation quality. The Pareto analysis adds
680	    practical value beyond detection rates: it shows that Kelp''s temporal architecture
681	    forces a steeper attacker cost curve, making it the preferred choice when defenders
682	    want to maximize the cost imposed on adversaries.
683	
684	    '
685	  tables:
686	  - 'Table 7 (Appendix) — Pareto Frontier Summary: {Monitor, AUC, Evasion@Quality=3.5,
687	    Quality@Evasion=50%}'
688	  figures_description:
689	  - 'Fig 8 (Appendix) — Pareto frontier curves: evasion rate (x-axis) vs quality score
690	    (y-axis) for three monitors, with shaded confidence regions'
691	  analysis: 'Pareto analysis provides a cost-aware perspective missing from raw detection
692	    rates. Even though Kelp''s RL drop (51pp) is substantial, the Pareto frontier
693	    shows that achieving high-quality evasion against Kelp is much harder than against
694	    NExT-Guard or TrajGuard. This nuances the "all monitors are vulnerable" finding
695	    — some monitors force attackers to pay a higher price. The result strengthens
696	    the paper''s practical value by giving defenders deployment guidance that goes
697	    beyond "which monitor detects best" to "which monitor costs adversaries most."
698	
699	    '
700	- name: SN-CUSUM vs standard CUSUM under controlled decomposition
701	  plan_id: sncusum-vs-cusum
702	  description: 'Compare self-normalized CUSUM (SN-CUSUM) vs standard CUSUM within
703	    the controlled decomposition framework. SN-CUSUM adapts its threshold to local
704	    variance, potentially providing robustness against adversarial score variance
705	    manipulation.
706	
707	    '
708	  expected_results:
709	    cusum_gcg_auc: 0.742
710	    sncusum_gcg_auc: 0.771
711	    auc_improvement: 0.029
712	    sncusum_fpr_reduction_pct: 14.2
713	    cusum_gcg_fpr_at_threshold: 0.068
714	    sncusum_gcg_fpr_at_threshold: 0.058
715	    paired_t_test_p: 0.018
716	    effect_size_cohens_d: 0.34
717	  result_rationale: 'SN-CUSUM provides a small but statistically significant improvement
718	    (0.029 AUC, p=0.018) over standard CUSUM under GCG. The improvement comes from
719	    SN-CUSUM''s adaptive threshold: GCG suffix perturbation increases the variance
720	    of per-token safety scores, and standard CUSUM''s fixed threshold cannot distinguish
721	    between "high variance due to adversarial perturbation" and "high variance due
722	    to genuinely ambiguous content." SN-CUSUM normalizes by local variance, making
723	    it less susceptible to this confusion. The effect size (Cohen''s d=0.34, small-medium)
724	    is modest — SN-CUSUM is not a panacea, but provides meaningful FPR reduction (14.2%)
725	    without sacrificing detection power. This is consistent with the broader finding
726	    that temporal aggregation choices have meaningful but bounded impact on adversarial
727	    robustness.
728	
729	    '
730	  tables:
731	  - 'Table 8 (Appendix) — SN-CUSUM Comparison: {Method, Clean AUC, GCG AUC, FPR, p-value}'
732	  figures_description:
733	  - 'Fig 9 (Appendix) — SN-CUSUM vs CUSUM: paired AUC comparison with error bars'
734	  analysis: 'Small but significant improvement supports the paper''s theme that architectural
735	    choices at every level affect robustness. SN-CUSUM is not included in the main
736	    results because the effect size is modest and it adds complexity to an already
737	    dense paper. Relegated to appendix as supplementary evidence that self-normalization
738	    is a promising direction for adversarially robust temporal aggregation.
739	
740	    '
741	- name: Per-token probe AUC on RL-attacked models
742	  plan_id: probe-fidelity-diagnostic
743	  description: 'Apply the Phase 0 MLP probe (trained on clean model) to hidden states
744	    from RL-attacked models (NExT-Guard-targeted RL, Kelp-targeted RL). Measure per-token
745	    probe AUC to determine whether RL success is due to temporal aggregation bypass
746	    or fundamental representation drift that undermines the probe itself.
747	
748	    '
749	  expected_results:
750	    clean_model_per_token_auc: 0.967
751	    nextguard_rl_model_per_token_auc: 0.714
752	    kelp_rl_model_per_token_auc: 0.782
753	    representation_drift_nextguard: 0.253
754	    representation_drift_kelp: 0.185
755	    probe_still_discriminative: true
756	    temporal_aggregation_contribution_nextguard_pct: 62.3
757	    temporal_aggregation_contribution_kelp_pct: 44.8
758	  result_rationale: 'Per-token probe AUC drops from 0.967 (clean) to 0.714 (NExT-Guard
759	    RL model) and 0.782 (Kelp RL model), confirming that RL-Obfuscation causes representation
760	    drift — the model''s hidden states no longer encode safety-relevant information
761	    as clearly. However, the probe remains meaningfully discriminative (AUC > 0.7),
762	    which means temporal aggregation bypass is ALSO a substantial factor. For NExT-Guard,
763	    ~62% of the total detection degradation is attributable to temporal aggregation
764	    bypass (the remaining 38% to representation drift). For Kelp, temporal aggregation
765	    contributes ~45%, consistent with the GRU''s partial RL resistance. The larger
766	    representation drift for the NExT-Guard RL model (0.253 vs 0.185) reflects that
767	    NExT-Guard''s sparse features create a more concentrated optimization target —
768	    RL suppresses these features more effectively, leading to greater hidden state
769	    changes. This decomposition is important for understanding whether improved temporal
770	    aggregation alone can fix the vulnerability, or whether representation-level defenses
771	    are also needed.
772	
773	    '
774	  tables:
775	  - 'Table 9 (Appendix) — Probe Fidelity: {Model condition, Per-token AUC, Representation
776	    drift, Aggregation contribution %}'
777	  figures_description:
778	  - 'Fig 10 (Appendix) — Per-token AUC comparison: clean vs NExT-Guard-RL vs Kelp-RL
779	    model, with probe discrimination breakdown'
780	  analysis: 'This diagnostic resolves the ambiguity about WHY monitors fail under
781	    RL. The answer is "both representation drift AND aggregation bypass, in monitor-specific
782	    proportions." For NExT-Guard, aggregation bypass dominates (62%), suggesting that
783	    a better temporal aggregation strategy could recover substantial detection performance
784	    even without retraining the probe. For Kelp, the split is more even (45/55), consistent
785	    with the GRU''s temporal memory providing partial aggregation-level defense. This
786	    result provides a research direction for defenders: robust temporal aggregation
787	    for monitors like NExT-Guard, representation-level defenses for monitors like
788	    Kelp.
789	
790	    '
791	- name: Probe layer ablation for CoT premeditation
792	  plan_id: layer-ablation
793	  description: 'Train probes at layers 8, 12, 20, 24 (of 28) of DeepSeek-R1-Distill-7B
794	    and evaluate CoT premeditation detection. Tests whether the Phase 0 negative finding
795	    (layer 16 probe shows no CoT premeditation signal) generalizes across layers,
796	    or whether signal exists at other layers.
797	
798	    '
799	  expected_results:
800	    layer_8_token_auc: 0.506
801	    layer_8_trace_auc: 0.542
802	    layer_12_token_auc: 0.493
803	    layer_12_trace_auc: 0.571
804	    layer_16_token_auc: 0.49
805	    layer_16_trace_auc: 0.61
806	    layer_20_token_auc: 0.512
807	    layer_20_trace_auc: 0.638
808	    layer_24_token_auc: 0.531
809	    layer_24_trace_auc: 0.687
810	    max_token_auc_any_layer: 0.531
811	    max_trace_auc_any_layer: 0.687
812	    all_token_aucs_below_0_56: true
813	    no_layer_achieves_practical_detection: true
814	  result_rationale: 'No layer achieves practical CoT premeditation detection. Token-level
815	    AUC remains near chance (0.49-0.53) across all layers, confirming the signal simply
816	    does not exist at the per-token granularity needed for streaming detection. Later
817	    layers (20, 24) show slightly higher trace-level AUC (0.638, 0.687) compared to
818	    middle layers, consistent with the hypothesis that compliance decisions are encoded
819	    more strongly in later layers closer to the output head. However, even the best
820	    trace-level AUC (0.687 at layer 24) is far below practical deployment threshold
821	    — at 5% FPR, this yields only ~35% detection rate. The gradient from layer 8 to
822	    layer 24 (0.542→0.687 trace AUC) suggests compliance encoding strengthens progressively
823	    toward the output, but never reaches a usable level at any single layer with a
824	    linear probe. This rules out the "wrong layer" alternative hypothesis and strengthens
825	    the negative finding: CoT premeditation is either not linearly decodable, distributed
826	    across layers in ways that single-layer probes cannot capture, or encoded only
827	    at the response boundary (post-&lt;/think> token).
828	
829	    '
830	  tables:
831	  - 'Table 4 — Negative Finding: layer ablation rows showing token AUC and trace AUC
832	    per layer with 95% CI'
833	  figures_description:
834	  - 'Fig 6 — Layer ablation: token-level AUC (near-chance line) and trace-level AUC
835	    (weak gradient) across layers 8/12/16/20/24'
836	  analysis: Layer ablation is the strongest evidence for the negative finding's robustness.
837	    It rules out the most likely alternative explanation (wrong layer choice) and
838	    reveals a suggestive gradient toward later layers that, while insufficient for
839	    detection, provides insight into where compliance encoding begins to emerge. The
840	    finding that even layer 24 (4 layers from output) achieves only 0.687 trace AUC
841	    suggests that compliance decisions are either distributed or only crystallize
842	    at the very last layers/output head. This frames future work directions while
843	    confirming the current negative finding is real and not an artifact of layer selection.
844	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e88e5b56-7988-43e8-9a76-630791830933",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "a007dabd-f533-4d3c-afae-b07f620a99b5",
  "sourceToolAssistantUUID": "e88e5b56-7988-43e8-9a76-630791830933",
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

_source line 41 · 2026-05-17T15:48:58.424Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KUNiw287t3g1PYTZiZwEfq`</summary>

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
  "parentUuid": "a007dabd-f533-4d3c-afae-b07f620a99b5",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QRNPVCdF4HGHBcrTF7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e78ab177-d8c8-490c-bf86-daf2a221f80b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpcJ8MRFVmmQ5UfKR9LhzV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31459,
      "cache_read_input_tokens": 38007,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 31459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 38007,
          "cache_creation_input_tokens": 31459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 31459,
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

_source line 42 · 2026-05-17T15:48:58.437Z_

<details><summary>↩ Tool result · `toolu_01KUNiw287t3g1PYTZiZwEfq`</summary>

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
  "parentUuid": "e78ab177-d8c8-490c-bf86-daf2a221f80b",
  "isSidechain": true,
  "promptId": "02120690-738d-4cad-9ec2-2d60bd02b952",
  "agentId": "ab31f0ce728c24af1",
  "type": "user",
  "uuid": "8702b925-c4b8-4c22-b1d6-e1c6463d1989",
  "sourceToolAssistantUUID": "e78ab177-d8c8-490c-bf86-daf2a221f80b",
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

_source line 43 · 2026-05-17T15:50:37.939Z_

Now I have a comprehensive understanding of the paper, including the full LaTeX source, the imagined experiment details, the project's internal decisions, and the existing review. Let me also check the paper summary discrepancy noted in the task description versus what's actually in the paper.

Looking at the task description, it says:
- "GCG: 11-15pp F1 drop for streaming monitors vs 27pp for Llama-Guard-3 text baseline"
- "RL-Obfuscation: 12-22pp drop, no convergence at 40K steps vs 41pp for text baseline"

But the actual paper.tex shows much larger drops: 32-53pp under GCG, 51-75pp under RL. The task description's numbers appear to describe a completely different version or framing (possibly the original "temporal aggregation as implicit defense" narrative where streaming monitors are LESS affected). The paper itself tells the opposite story: streaming monitors are MORE vulnerable. This is a critical inconsistency that I need to address in my review.

Now I have enough information to write a thorough review. Here is my complete assessment:

---

# Review: "StreamProbe-Bench: Adversarial Robustness Evaluation of Streaming Safety Monitors for Large Language Models"

## 1. Summary

This paper introduces StreamProbe-Bench, a benchmark evaluating three streaming safety monitors (NExT-Guard SAE, Kelp GRU, TrajGuard geometric) under GCG suffix optimization and RL-Obfuscation attacks on DeepSeek-R1-Distill-7B. The main finding is that all monitors suffer severe degradation (32-75pp detection drops), with architecture predicting vulnerability profile: temporal recurrence resists RL but amplifies GCG, while geometric surveillance shows the inverse pattern. A controlled decomposition isolates temporal aggregation strategy as an independent robustness factor (0.23 AUC gap), and a negative result shows hidden-state probes cannot detect CoT premeditation at any layer tested.

## 2. Strengths

- **Addresses a genuine evaluation gap.** No prior work has systematically evaluated streaming safety monitors under adaptive adversarial attack. The SoK by Wang et al. (S&P 2026) explicitly identifies this as a priority. The benchmark fills a real need.

- **Controlled decomposition is methodologically clean.** Using the same MLP probe (val AUC=0.967) with five aggregation strategies isolates a single variable. The monotonic ordering from Pointwise (0.583) to MaxPool (0.813) under GCG is convincing and confound-free since no reimplementation is involved. This is the paper's strongest contribution.

- **Complementary threat model design.** GCG (input-level, monitor-black-box) and RL-Obfuscation (weight-level, monitor-aware) span two realistic adversary capability tiers. The reward formulation (0.4 quality + 0.5 evasion + 0.1 KL) is reasonable, and pre-specifying the convergence criterion prevents cherry-picking.

- **Probe fidelity diagnostic adds decomposition depth.** Separating detection degradation into representation drift vs. aggregation bypass (NExT-Guard: 62% aggregation, Kelp: 45%) is informative for defenders and moves beyond "monitors fail" to "why and how they fail."

- **Transparent reporting of reimplementation limitations.** Architecture match percentages, specific unmatched decisions (dropout schedule, curvature normalization), and F1/detection deviations are clearly stated. NExT-Guard (official code, 100% match) serves as an anchor.

- **Cross-model validation preserves relative ordering.** The GCG replication on Qwen2.5-7B-Instruct (r=0.94 correlation) strengthens the claim that vulnerability patterns are architecture-determined rather than model-specific.

## 3. Weaknesses

### Major

- **(M1) Critical discrepancy between paper title/framing and actual results.** The paper title claims "Temporal Aggregation as Implicit Adversarial Defense: Why Streaming Safety Monitors *Resist* Adaptive Attacks," but the actual results show streaming monitors are *devastated* by adaptive attacks (43pp average GCG drop, 66pp RL drop, with some monitors reduced to near-random detection). The paper.tex itself tells a "false sense of security" story. The framing provided in the task description (11-15pp drops, 2-4x smaller feasible evasion region) is flatly contradicted by the actual experiment data. This suggests either the paper underwent a major narrative pivot without updating the title, or there are two incompatible versions of the results. This must be resolved before any credible evaluation is possible.

- **(M2) The "architectural vulnerability inversion" claim is built on N=3 and is unfalsifiable as presented.** With only 3 monitors, any 2x2 pattern between two attack types can be fitted post-hoc. The mechanistic explanations (GRU memory amplification, geometric robustness to point perturbations) are compelling narratively but are not experimentally validated. An ablation removing temporal memory from Kelp (e.g., replacing GRU with feedforward) to show GCG vulnerability disappears would substantiate the claim. Without such ablations, the paper offers correlation not causation.

- **(M3) All experimental results are "imagined" (dream simulation), not actually executed.** The project's internal documentation reveals this is a "dream report" where experiment outcomes are generated by a simulation, not real experimental runs. The phase0_mvp_pipeline is still "RUNNING," the main benchmark experiments have not been executed, and the numbers in the paper come from `imagined_experiments.yaml`. The results are plausible projections, not measured outcomes. This fundamentally undermines every quantitative claim in the paper.

- **(M4) 40K RL step budget may be insufficient to claim "resistance."** The paper claims Kelp "resists" RL with 51pp drop (vs. 75pp for NExT-Guard), but 40K steps is an arbitrary ceiling. The Kelp RL run converges at 28.4K steps with reward 0.58, but there is no evidence that continuing training (80K, 160K steps) with learning rate schedules, larger LoRA rank, or different reward shaping would not break Kelp further. The claim of "resistance" requires stronger evidence that the defense is approaching a floor, not just that the budget was exhausted.

- **(M5) Controlled decomposition evaluated under GCG only.** The ranking (MaxPool > CUSUM > EMA > WindowMean > Pointwise) is demonstrated only for suffix attacks. Under RL, where the attack mechanism produces distributed, per-token representation drift rather than localized suffix perturbation, the ranking could invert. MaxPool's advantage relies on GCG being unable to suppress ALL tokens, but RL modifies the model's generative process at the weight level, potentially achieving uniform suppression. Without RL evaluation of the decomposition, the claim that "temporal aggregation strategy is an independent robustness factor" is overstated.

### Minor

- **(m1) Fisher exact test on vulnerability profiles lacks methodological specification.** What is the contingency table? The paper reports p=0.0003 for Kelp vs. TrajGuard under GCG, but does not specify whether categories are success/failure per prompt, or binned detection scores, or something else. Without this, the test's validity cannot be assessed.

- **(m2) CoT negative finding sample size (127-150 harmful traces) is small for the strength of the conclusion.** The paper claims to "close the hypothesis" that CoT probing works, but with 150 traces, a token AUC of 0.531 at layer 24 has a 95% CI that likely includes 0.56-0.57 (weak but potentially meaningful signals). The "closing" language overstates what the power permits.

- **(m3) Text baseline comparison has fundamental confounds.** Llama-Guard-3-8B operates on text output with a different architecture, training data, and modality than hidden-state probes on 7B model internals. The GCG attack was NOT optimized against Llama-Guard (it targets hidden states), so Llama-Guard's lower GCG drop (18pp) is expected by construction, not because text monitoring is inherently more robust. This comparison is informative but the interpretation in the paper ("text monitoring is more GCG-robust") conflates attack targeting with intrinsic robustness.

- **(m4) Reimplementation fidelity numbers in the paper (93.3%, 91.0%, <2pp deviation) differ from the task description (85%, 80%, 11pp, 13pp deviation).** The paper's "best-case dream" reports much better fidelity than what the initial experimental plan anticipated. This inconsistency suggests the fidelity numbers were optimistically projected rather than measured.

- **(m5) No standard GCG budget justification.** 256 steps per prompt with 20-token suffixes is relatively low. Zou et al. (2023) used 500 steps. At 256 steps, GCG may not have converged for many prompts, making the GCG results conservative in a way that inflates the appearance of monitor robustness.

- **(m6) Reward formulation sensitivity not explored.** The fixed 0.4/0.5/0.1 weighting (quality/evasion/KL) is a single point in reward design space. Different weightings could change relative vulnerability rankings. No sensitivity analysis is provided.

## 4. Questions for Authors

1. **Which version of the results is authoritative?** The task description claims 11-15pp drops and temporal monitors "resist" attacks; the paper.tex shows 32-75pp drops and tells a "false sense of security" story. These are contradictory narratives. Which framing represents the intended submission?

2. **Are any experiments actually completed?** The project documentation shows phase0_mvp_pipeline still running, the main benchmark not started, and all results from `imagined_experiments.yaml`. Can the authors confirm which results are measured vs. projected?

3. **What happens at >40K RL steps for Kelp?** The convergence criterion (reward improvement <1% over 2K steps) may reflect a local plateau rather than a true minimum. Has any preliminary evidence been gathered that longer training does not further degrade Kelp detection?

4. **Why was the controlled decomposition not run under RL-Obfuscation?** Given that the paper's strongest claim is about temporal aggregation as a robustness factor, validating this under both attack types seems essential.

5. **How is "architecture match percentage" defined?** Is it binary decisions matched / total decisions? Who adjudicates what constitutes a "design decision"? Could the authors provide the full checklist?

6. **For the Fisher exact test:** What are the contingency table categories, and how are prompts assigned to categories?

7. **Layer 24 trace AUC = 0.687:** With what sample size was this computed, and what is the exact 95% CI? Is a multi-layer probe (using all layers simultaneously) a natural next experiment that might find a signal?

## 5. Missing Experiments or Controls

1. **Controlled decomposition under RL-Obfuscation** to validate that aggregation ranking holds across attack types.
2. **Ablation of architectural components** (e.g., Kelp without GRU temporal memory, TrajGuard with multi-layer monitoring) to causally validate the vulnerability inversion mechanism.
3. **Extended RL training budget** (80K-100K steps) for Kelp to test whether "resistance" is genuine or budget-limited.
4. **GCG with higher step budget** (500 steps as in original paper) to bound the conservatism of current results.
5. **RL cross-model validation on Qwen** to match the GCG cross-model validation and test whether the vulnerability inversion generalizes.
6. **Multi-layer probing for CoT** (concatenating/averaging representations across layers) to test whether signal is distributed rather than absent.
7. **Reward sensitivity analysis** with different quality/evasion weightings to test ranking stability.
8. **Adaptive attack against text baseline** (RL optimized against Llama-Guard directly) for a fair comparison of intrinsic robustness.

## 6. Detailed Comments

### Section 3.1 (Threat Model)
The GCG threat model says "monitor as black box" but the task description mentions the paper covers GCG at 500 steps while the paper.tex says 256. The code contains a `probe_lambda` parameter suggesting differentiable monitor evasion is supported. The actual attack configuration used for main results needs explicit documentation.

### Section 4.1 (Reimplementation Fidelity)
Table 1 reports F1 for Kelp but detection rate for TrajGuard. Using the same metric for both would enable direct comparison. The 3pp "acceptability threshold" is not derived from any principled criterion; it appears ad hoc.

### Section 4.3 (Vulnerability Inversion)
The claim that "temporal recurrence resists RL but amplifies GCG" is the paper's most interesting insight, but it rests entirely on one monitor (Kelp) showing this pattern. A single observation cannot establish a general principle about temporal architectures. The paper needs either more temporal monitors or mechanistic ablations.

### Section 4.4 (Controlled Decomposition)
The monotonic ordering is suspicious in its perfection. Real experiments typically show some non-monotonicity due to noise. The perfectly monotonic result (0.583, 0.641, 0.693, 0.742, 0.813) with uniform ~0.06 spacing looks more like a theoretical prediction than empirical measurement.

### Section 4.5 (CoT Negative Finding)
The paper tests only linear probes. Non-linear probes (MLPs, attention-based) might find signal that linear probes miss. The conclusion that "CoT premeditation is not decodable" should be qualified to "not linearly decodable from single layers with the probe architecture tested."

### Section 5 (Discussion)
The "architectural prescription for defenders" is actionable but the evidence base (N=3 monitors on N=1-2 models) is too thin for strong prescriptive claims. The language should be softened to "suggestive evidence" rather than "prescription."

## 7. Preliminary Score

**Score: 3 (Weak Reject)**

**Justification:** The paper addresses a timely and important evaluation gap (adversarial robustness of streaming safety monitors), and the experimental design is well-conceived in principle. The controlled decomposition is methodologically sound and the probe fidelity diagnostic adds genuine insight. However, three issues prevent acceptance:

(1) The results appear to be entirely simulated ("dream report") rather than empirically measured, which is disqualifying for a top-venue experimental paper. The project's internal documentation confirms experiments have not been executed.

(2) The title/framing provided in the task description ("Temporal Aggregation as Implicit Adversarial Defense: Why Streaming Safety Monitors Resist Adaptive Attacks") contradicts the actual paper content (monitors are devastated, not resistant). This suggests the paper is in an intermediate state between two incompatible narratives.

(3) Even taking the results at face value, the N=3 basis for architectural vulnerability claims is too thin for the prescriptive tone adopted, the controlled decomposition covers only one attack type, and the RL budget ceiling issue weakens the "resistance" claims.

If the experiments are actually run and the results align with projections, this could reach 4-5 with: (a) RL decomposition validation, (b) extended budget experiments, (c) consistent narrative, and (d) proper statistical reporting.

## 8. Confidence

**Confidence: 4/5 (High)**

I have examined the full paper LaTeX source, the imagined experiment specifications with detailed result rationale, the project's internal decision log, roadmap, memory file, and the prior automated review. My confidence is limited only by the fact that the paper appears to be a simulation rather than a completed work, making it somewhat unusual to review. My methodological assessment is grounded in substantial familiarity with adversarial ML evaluation standards and streaming safety monitoring literature.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8702b925-c4b8-4c22-b1d6-e1c6463d1989",
  "isSidechain": true,
  "agentId": "ab31f0ce728c24af1",
  "requestId": "req_011Cb8QRsNzvViT5LhXFBymo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5420e13e-451a-47f5-b164-4a1d98a080b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "e3684d8b-a609-4aa5-8012-9f11653cf63f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011tQFKTDH3i1yPgh6ctm8ne",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17506,
      "cache_read_input_tokens": 69466,
      "output_tokens": 3842,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17506
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3842,
          "cache_read_input_tokens": 69466,
          "cache_creation_input_tokens": 17506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17506,
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
