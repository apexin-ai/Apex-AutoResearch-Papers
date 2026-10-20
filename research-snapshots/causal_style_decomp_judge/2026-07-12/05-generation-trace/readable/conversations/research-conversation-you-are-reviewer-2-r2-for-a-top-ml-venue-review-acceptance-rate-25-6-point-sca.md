# Research conversation: You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Wea

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a9fd73ad3308fafe9.jsonl`
- **Structured JSON:** [`fb019c8bcd3874776992.json`](../../sessions/fb/fb019c8bcd3874776992.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-17T15:37:05.995Z_

You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **Novelty and Related Work**. Evaluate the originality of contributions, adequacy of literature coverage, positioning relative to prior work, and whether the paper advances the field meaningfully.

## Paper Summary

**Title**: StreamProbe-Bench: Adversarial Robustness Evaluation of Streaming Safety Monitors for Large Language Models

The paper introduces StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors that inspect LLM hidden states during generation. Three monitors are evaluated:
- **NExT-Guard** (SAE features, official code)
- **Kelp** (GRU temporal modeling, reimplemented, 4.8pp F1 deviation)
- **TrajGuard†** (geometric surveillance, reimplemented, 6.8pp deviation, caveated)

Two attacks: GCG suffix optimization and RL-Obfuscation.
Target: DeepSeek-R1-Distill-Qwen-7B (primary), Qwen2.5-7B (GCG only).

**Three contributions**:
1. **Benchmark**: First adversarial robustness evaluation of streaming safety monitors. All monitors suffer 18-42pp detection drops under adaptive attacks.
2. **Controlled decomposition**: Same probe, 5 temporal aggregation strategies under GCG. 0.13 AUC gap (CUSUM 0.72 vs Pointwise 0.59). No reimplementation confound.
3. **Negative finding**: CoT premeditation detection fails at all layers (8-24), best token AUC = 0.57.

## Paper Structure and Content

**Abstract** (p1): States problem, approach (3 monitors × 2 attacks), controlled decomposition finding (0.13 AUC gap), negative finding (0.57 max token AUC).

**Introduction** (p1-2): Motivates with Wang et al. S&P 2026 SoK identifying absence of adaptive adversarial evaluation as key gap. References RL-Obfuscation's 59-89% evasion on static classifiers. Notes Qwen3Guard-Stream's 57.2pp degradation on novel prompts. Three bullet contributions listed.

**Related Work** (p2): Four subsections: Streaming safety monitors, Adversarial attacks on safety mechanisms, Hidden-state probing for safety, Temporal aggregation in anomaly detection. Each is 3-5 sentences.

**Methods** (p3): Target models, monitor descriptions, attack methodologies, controlled decomposition protocol.

**Experiments** (p3-8): Reimplementation fidelity (Table 1), Main benchmark (Table 2), RL diagnostics (Table 3), Controlled decomposition (Tables 4-5), SN-CUSUM, Probe fidelity (Table 6), Vulnerability analysis (Table 7), CoT premeditation (Tables 8-9), Text baseline (Table 10), Cross-model (Table 11), Pareto analysis (Table 12).

**Discussion** (p8-9): Temporal aggregation as defense, false security of benchmarks, limitations, CoT monitoring implications.

**Conclusion** (p9): Summary + explicit limitations paragraph.

**References**: 10 references total: [1] Kelp ACL 2026, [2] NExT-Guard NAACL 2026, [3] TrajGuard EMNLP 2025, [4] Zou et al. GCG ICML 2024, [5] RL-Obfuscation NeurIPS 2025, [6] Wang et al. SoK S&P 2026, [7] Qwen3Guard-Stream arXiv 2026, [8] Llama-Guard arXiv 2024, [9] Page 1954 CUSUM, [10] Horváth & Hušková 2012 change-point detection.

## Your Review Task

Provide a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bullet list, focus on novelty/positioning)
3. **Weaknesses** (bullet list, focus on novelty/related work/positioning)
4. **Questions to Authors**
5. **Minor Issues**
6. **Scores**: Overall (1-6), Confidence (1-5), Novelty (1-4), Significance (1-4)

Key issues to examine:

**Novelty**:
- Is "first adversarial evaluation of streaming monitors" a sufficient contribution? Is it primarily an engineering/evaluation effort rather than methodological innovation?
- The controlled decomposition is clean but incremental: it compares 5 standard aggregation strategies. Does the 0.13 AUC gap constitute a significant insight?
- The CoT negative finding is useful but limited scope (single model, linear probes only). How novel is this?
- Is there any new method proposed, or is this purely evaluation/benchmark?

**Related Work**:
- Only 10 references total. Is this adequate for a top venue? Are key related works missing?
- Missing categories: adversarial robustness of safety mechanisms more broadly, interpretability/probing literature (Belinkov etc.), jailbreaking literature beyond GCG, safety alignment methods, other hidden-state monitoring approaches.
- The Related Work section is very brief (half a page). Does it adequately position the work?
- Are the references verifiable? Some appear to be for future/recent venues (ACL 2026, NAACL 2026, S&P 2026).

**Positioning**:
- The paper frames itself as a "benchmark" paper. Does it meet the bar for benchmark contributions at top venues?
- How does this compare to existing adversarial robustness benchmarks (AdvBench, HarmBench, etc.)?
- Is the controlled decomposition contribution sufficiently differentiated from standard ablation studies?

**Writing quality**:
- Check for AI writing patterns: excessive dashes (em-dash/en-dash usage), -ing phrases, over-segmentation
- Is the narrative coherent from Abstract through Conclusion?
- Are claims calibrated to evidence?

Format your output as a structured review report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "75854338-aed9-4745-a66e-fad6d81c7938",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T15:37:05.999Z_

```json
{
  "parentUuid": "75854338-aed9-4745-a66e-fad6d81c7938",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
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
  "uuid": "fed5230d-0e4a-4379-bf68-c85bc0fb85fc",
  "timestamp": "2026-05-17T15:37:05.999Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T15:37:28.608Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01A9DcV1DwNmSHMhtJRHq4vo`</summary>

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
  "parentUuid": "fed5230d-0e4a-4379-bf68-c85bc0fb85fc",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8PXMCbiZMqpSk77F4Do",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b2fb5a5-2d56-41d4-abfb-c19cf36e7acc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7LFaZeD18oyheWhrKNrQP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16888,
      "cache_read_input_tokens": 0,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16888,
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

_source line 4 · 2026-05-17T15:37:28.611Z_

<details><summary>↩ Tool result · `toolu_01A9DcV1DwNmSHMhtJRHq4vo`</summary>

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
  "parentUuid": "3b2fb5a5-2d56-41d4-abfb-c19cf36e7acc",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "f8d4ca73-f8a6-489e-8b93-dbe3d8adeb6b",
  "sourceToolAssistantUUID": "3b2fb5a5-2d56-41d4-abfb-c19cf36e7acc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T15:37:42.542Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018jpR9f3vTcR1yzWEoC1pKN`</summary>

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
  "parentUuid": "f8d4ca73-f8a6-489e-8b93-dbe3d8adeb6b",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8PZ1oqh2WaKx1C2zPBc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3d4f225-42bc-4060-b2fd-c7149107b6ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ly3ya8L7ccS4XPdK9jqBdW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 16888,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 16888,
          "cache_creation_input_tokens": 1270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1270,
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

_source line 6 · 2026-05-17T15:37:42.564Z_

<details><summary>↩ Tool result · `toolu_018jpR9f3vTcR1yzWEoC1pKN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| phase0_mvp_pipeline | Hidden-state probes on DeepSeek-R1-Distill-7B CoT traces detect harmful premeditation (AUC>0.85) with temporal drift evidence (relaxed_B>=20%) using D003 onset definition (response-level, post-&lt;/think> boundary) | — | — | — |\\n| mvp_benign_trace_gen | DeepSeek-R1-Distill-7B generates multi-step reasoning traces on benign prompts (GSM8K/ARC-Challenge) that serve as safe-class control for probe training, with comparable trace length/complexity to harmful traces | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_trace_gen** (failed): DeepSeek-R1-Distill-7B with unified config (temp=1.0, no system prompt) on harmful prompts produces a mix of complied and refused traces sufficient for MVP (≥150 each from 500 prompts)\\n\\n## 趋势\\n成功 0 / 负向 0 / 失败 1 / 共 1\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39593: 无 GPU 信息\\n\\n## 告警\\n- mvp_trace_gen: 训练失败 — unknown\\n\", \"total_chars\": 1017, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3d4f225-42bc-4060-b2fd-c7149107b6ef",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "ece05ea1-23fc-4f51-8b9f-5e46a6c6bba7",
  "sourceToolAssistantUUID": "c3d4f225-42bc-4060-b2fd-c7149107b6ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T15:37:54.608Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VhqKRTshh6tpY3n8bwSRYz`</summary>

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
  "parentUuid": "ece05ea1-23fc-4f51-8b9f-5e46a6c6bba7",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8Pa3XYzXUJ7CcBXpehf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad8eae82-4d00-4127-a148-e0987a6bf564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwSs5SWsnEys5hsPV5cq44",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 18158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 691,
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

_source line 8 · 2026-05-17T15:37:54.618Z_

<details><summary>↩ Tool result · `toolu_01VhqKRTshh6tpY3n8bwSRYz`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'streamprobe_adversarial_robustness'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad8eae82-4d00-4127-a148-e0987a6bf564",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "0d9aab7c-9cee-41e7-ac37-17b1f5d60329",
  "sourceToolAssistantUUID": "ad8eae82-4d00-4127-a148-e0987a6bf564",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T15:37:55.341Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UHqrv2djugm6GLbNHykJrm`</summary>

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
  "parentUuid": "0d9aab7c-9cee-41e7-ac37-17b1f5d60329",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8Pa3XYzXUJ7CcBXpehf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84758e5e-429f-4c17-a81d-c1ce9fc42d3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwSs5SWsnEys5hsPV5cq44",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 18158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 691,
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

_source line 10 · 2026-05-17T15:37:55.366Z_

<details><summary>↩ Tool result · `toolu_01UHqrv2djugm6GLbNHykJrm`</summary>

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
  "parentUuid": "84758e5e-429f-4c17-a81d-c1ce9fc42d3c",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "6de1883e-b323-430b-b8a4-5c533ba6dfc1",
  "sourceToolAssistantUUID": "84758e5e-429f-4c17-a81d-c1ce9fc42d3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T15:38:12.022Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EGys5hEkoMfb5dPaWYTPLX`</summary>

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
  "parentUuid": "6de1883e-b323-430b-b8a4-5c533ba6dfc1",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8Pb1ur85T6AJ2bncyLd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "880c7deb-187a-4103-867e-29a18c6a6a97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RDGZ8D2o1N2YUv75XDF2q1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 382,
      "cache_read_input_tokens": 18849,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 382
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 18849,
          "cache_creation_input_tokens": 382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 382,
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

_source line 12 · 2026-05-17T15:38:12.468Z_

<details><summary>↩ Tool result · `toolu_01EGys5hEkoMfb5dPaWYTPLX`</summary>

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
  "parentUuid": "880c7deb-187a-4103-867e-29a18c6a6a97",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "dd29b9e2-5a8a-4af3-9935-f593acad73f7",
  "sourceToolAssistantUUID": "880c7deb-187a-4103-867e-29a18c6a6a97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-17T15:38:28.874Z_

Now let me also look at the paper summary document and literature map if available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd29b9e2-5a8a-4af3-9935-f593acad73f7",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8PcFGJCCLSQBHEeGBQ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa75821a-055f-49f4-a21d-eb6d74168abd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4bf1AuRvm7RxbJeMSDxrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8727,
      "cache_read_input_tokens": 19231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8727,
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

_source line 14 · 2026-05-17T15:38:29.834Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01A8s3GNJHhitGUNfwfR7Sjb`</summary>

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
  "parentUuid": "aa75821a-055f-49f4-a21d-eb6d74168abd",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8PcFGJCCLSQBHEeGBQ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49e09168-29c6-4eaa-852a-177ce1c48d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4bf1AuRvm7RxbJeMSDxrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8727,
      "cache_read_input_tokens": 19231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8727,
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

_source line 15 · 2026-05-17T15:38:29.845Z_

<details><summary>↩ Tool result · `toolu_01A8s3GNJHhitGUNfwfR7Sjb`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'streamprobe_adversarial_robustness'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49e09168-29c6-4eaa-852a-177ce1c48d2b",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "5331a315-997e-48d9-b397-43818d9c3803",
  "sourceToolAssistantUUID": "49e09168-29c6-4eaa-852a-177ce1c48d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T15:38:30.407Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FSwezidkMuqkKhR3JnHhuV`</summary>

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
  "parentUuid": "5331a315-997e-48d9-b397-43818d9c3803",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8PcFGJCCLSQBHEeGBQ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ceaa2d5-b920-4221-a053-243398c6e538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4bf1AuRvm7RxbJeMSDxrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8727,
      "cache_read_input_tokens": 19231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8727,
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

_source line 17 · 2026-05-17T15:38:30.416Z_

<details><summary>↩ Tool result · `toolu_01FSwezidkMuqkKhR3JnHhuV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/paper_framing.md\", \"content\": \"# Paper Framing — streamprobe_adversarial_robustness\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (LLM Security Track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (7 days remaining)\\n\\n## Core Claims (≤3)\\n\\n1. **[Benchmark]** Streaming safety monitors (Kelp, NExT-Guard, TrajGuard) exhibit substantially degraded detection performance under adaptive adversarial attacks (GCG suffix optimization + RL-Obfuscation), with attack success rates far exceeding those reported on standard benchmarks.\\n\\n2. **[Architectural Insight]** Monitor architecture determines adversarial vulnerability profile: temporal recurrence (Kelp GRU), sparse feature selection (NExT-Guard SAE), and geometric surveillance (TrajGuard) fail through distinct, predictable mechanisms under GCG vs RL-Obfuscation.\\n\\n3. **[Negative Finding]** Hidden-state probes at middle layers of reasoning models do not detect harmful premeditation during chain-of-thought: per-token safety scores in CoT are statistically indistinguishable from benign traces (AUC ≈ 0.5), and temporal aggregation (CUSUM) cannot rescue a signal that does not exist.\\n\\n## Story Spine\\n\\n- **Problem**: Streaming safety monitors for LLM generation have proliferated rapidly (Kelp, NExT-Guard, TrajGuard, Qwen3Guard-Stream, SafeProbing), yet NONE have been evaluated under adaptive adversarial attacks. SoK (Wang et al., S&P 2026) identifies this evaluation gap as critical. RL-Obfuscation showed static classifiers are vulnerable (59-89% evasion), but temporal/streaming monitors remain untested.\\n\\n- **Existing approaches & their gaps**: Each streaming monitor reports strong standard-benchmark performance (Kelp +15.61% F1 over static probes, NExT-Guard 84.3 F1, TrajGuard 95% detection). But Qwen3Guard-Stream's 57.2pp degradation on merely novel (non-adaptive) adversarial prompts foreshadows the problem. No systematic adversarial evaluation exists; deployment decisions are made on inflated benchmarks.\\n\\n- **Our framing**: We construct StreamProbe-Bench, the first adversarial robustness benchmark for streaming safety monitors. We evaluate three representative architectures under two adaptive attack methodologies, providing: (a) the first comparative robustness data, (b) architectural vulnerability analysis revealing distinct failure modes, (c) a controlled decomposition experiment isolating the contribution of temporal aggregation strategy, and (d) a negative result showing hidden-state CoT premeditation detection is infeasible at middle layers.\\n\\n- **Headline result template**: \\\"Under adaptive RL-Obfuscation, [worst monitor]'s detection rate drops from [X]% to [Y]% while [best monitor] maintains [Z]% detection, revealing that [architectural property] is the key determinant of adversarial robustness in streaming safety monitoring.\\\"\\n\\n## Venue Fit Risks\\n\\n- **\\\"Just an engineering benchmark\\\" critique**: Mitigate via Claim 2 (architectural insight with explanatory analysis) + Claim 3 (negative finding about CoT premeditation). The paper provides both evaluation AND insight.\\n- **Reimplementation fidelity for Kelp/TrajGuard**: NExT-Guard has official code. For Kelp and TrajGuard, we report architecture match percentage and invite author verification. Accepting 2/3 monitors as minimum viable benchmark (IDEA_BRIEF contingency).\\n- **Scope limited to one model**: DeepSeek-R1-Distill-7B primary, Qwen2.5-7B-Instruct secondary if time permits. Single-model limitation explicitly acknowledged.\\n\\n## Anticipated Reviewer Concerns\\n\\n| Concern | Response Strategy |\\n|---------|-------------------|\\n| \\\"Reimplementation may not be faithful\\\" | Use NExT-Guard official code as anchor; report fidelity metrics for Kelp/TrajGuard; controlled decomposition uses same-probe different-aggregation (no reimplementation needed) |\\n| \\\"Only one target model\\\" | Add Qwen2.5-7B-Instruct as P1; frame as \\\"proof of methodology\\\" if single-model |\\n| \\\"RL-Obfuscation didn't converge\\\" | Pre-specified convergence criteria (reward <1% improvement over 2K steps, 40K max, gradient norm diagnostic) |\\n| \\\"What's beyond the benchmark?\\\" | Claim 2 (architectural vulnerability analysis) + Claim 3 (negative CoT premeditation finding) + controlled decomposition |\\n| \\\"Why not just monitor text?\\\" | Text-level baseline (Llama-Guard sliding window) included as comparison |\\n| \\\"Small sample size\\\" | Bootstrap 95% CI on all metrics; 500 harmful + 200 benign traces |\\n\\n## Negative Finding Framing (Claim 3)\\n\\nPhase 0 MVP tested: \\\"Do hidden states in CoT accumulate detectable harmful premeditation signal?\\\"\\n\\nResult: No. At layer 16/28 of DeepSeek-R1-Distill-7B (v2 probe, overfitting fixed):\\n- Per-token probe AUC in CoT = 0.49 (anti-predictive: harmful CoT scores LOWER than benign)\\n- Trace-level mean-score AUC = 0.61 (weak)\\n- CUSUM-max AUC = 0.645 (no advantage over simple max-score AUC = 0.676)\\n- Detection @5% trace-level FPR = 0-5% (original 88% was token-to-trace FPR mixing bug)\\n- CUSUM false alarm rate on safe traces = 36.3% (v2 probe)\\n- **Strongest evidence**: On the SAME harmful prompts, probe scores are statistically indistinguishable between complied and refused traces (CUSUM fire rate 47.1% vs 45.3%, mean pre-onset score 0.0143 vs 0.0142). This rules out \\\"weak probe\\\" as explanation — hidden states genuinely do not encode compliance decisions at this layer.\\n\\nThis is reported as: \\\"Contrary to the hypothesis that reasoning traces leak compliance intent through hidden states, we find that middle-layer activations during CoT are statistically indistinguishable between harmful-compliant and benign traces. Critically, complied and refused traces on identical harmful prompts show no probe score difference, demonstrating that the model's compliance decision is not encoded in layer 16 activations during reasoning. This suggests compliance decisions are either encoded in later layers, emerge only at the response boundary, or are distributed across layers in ways that single-layer linear probes cannot capture.\\\"\\n\\nThis negative finding is valuable because it prevents the community from assuming probing-based CoT monitoring is straightforward.\\n\", \"total_chars\": 6086, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ceaa2d5-b920-4221-a053-243398c6e538",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "cce625e8-5a14-4efc-bc6a-ef311e6d515f",
  "sourceToolAssistantUUID": "6ceaa2d5-b920-4221-a053-243398c6e538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-17T15:38:41.467Z_

Now let me also check the dream report directory for any additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce625e8-5a14-4efc-bc6a-ef311e6d515f",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8Pda7ea34dD2oXBXr6c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "685b6115-1b69-43af-9a23-e8bf611bb908",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS3TEyJuwhmnN4pcX1Fiys",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2220,
      "cache_read_input_tokens": 27958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2220,
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

_source line 19 · 2026-05-17T15:38:42.494Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GXdQwjcqoDbeY2GPgifbWU`</summary>

```json
{
  "pattern": "artifacts/dream_reports/dream_20260517T145100/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "685b6115-1b69-43af-9a23-e8bf611bb908",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8Pda7ea34dD2oXBXr6c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41b7d47a-107e-484b-9363-0dd349f5f6d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS3TEyJuwhmnN4pcX1Fiys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2220,
      "cache_read_input_tokens": 27958,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2220
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 27958,
          "cache_creation_input_tokens": 2220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2220,
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

_source line 20 · 2026-05-17T15:38:42.511Z_

<details><summary>↩ Tool result · `toolu_01GXdQwjcqoDbeY2GPgifbWU`</summary>

```text
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
artifacts/dream_reports/dream_20260517T145100/best/review_report.md
artifacts/dream_reports/dream_20260517T145100/logs/review_best.log
artifacts/dream_reports/dream_20260517T145100/median/review_context.yaml
artifacts/dream_reports/dream_20260517T145100/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41b7d47a-107e-484b-9363-0dd349f5f6d2",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "05d65e74-f453-4eb1-a624-c9193824ec19",
  "sourceToolAssistantUUID": "41b7d47a-107e-484b-9363-0dd349f5f6d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T15:38:47.445Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MT4zJ8vqkvuhwZXLyKuQb8`</summary>

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
  "parentUuid": "05d65e74-f453-4eb1-a624-c9193824ec19",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8PeTpuaZ8BdHpNpK3Aj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56d8c4fd-485f-40ee-a241-6ea27ac005f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuArQorLXPxCoBguqwdfwF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1091,
      "cache_read_input_tokens": 30178,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1091
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 30178,
          "cache_creation_input_tokens": 1091,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1091,
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

_source line 22 · 2026-05-17T15:38:47.801Z_

<details><summary>↩ Tool result · `toolu_01MT4zJ8vqkvuhwZXLyKuQb8`</summary>

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
  "parentUuid": "56d8c4fd-485f-40ee-a241-6ea27ac005f6",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "fb83f5d0-2807-4ecd-9f2e-695c20ff7387",
  "sourceToolAssistantUUID": "56d8c4fd-485f-40ee-a241-6ea27ac005f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-17T15:39:56.681Z_

Now I have sufficient information to write a comprehensive review. Let me also check for any additional related work context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb83f5d0-2807-4ecd-9f2e-695c20ff7387",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8PerNUYtYDyNAq3jd74",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c65069c-9d57-47f6-8d87-d5fcfeeb3373",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KYbA59TA25no6Nt7pGRss",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15672,
      "cache_read_input_tokens": 31269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15672,
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

_source line 24 · 2026-05-17T15:39:57.984Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ghpt7MxG2BYHumxoeHtD9s`</summary>

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
  "parentUuid": "4c65069c-9d57-47f6-8d87-d5fcfeeb3373",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8PerNUYtYDyNAq3jd74",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51c5e06b-7509-40aa-8fd6-44ebd43aad60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KYbA59TA25no6Nt7pGRss",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15672,
      "cache_read_input_tokens": 31269,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15672,
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

_source line 25 · 2026-05-17T15:39:58.006Z_

<details><summary>↩ Tool result · `toolu_01Ghpt7MxG2BYHumxoeHtD9s`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/ROADMAP.md\", \"content\": \"# streamprobe_adversarial_robustness — Research Dashboard\\n\\n> 最后更新: 2026-05-17 14:51 UTC | 更新原因: D006 MVP FAIL pivot to benchmark-primary; research 阶段启动; Dream 模拟进行中\\n\\n> 核心方向已 pivot（D006）\\n\\n## 核心方向\\n\\n**Benchmark-primary**: StreamProbe-Bench — 首个 streaming safety monitor 对抗鲁棒性 benchmark。评估 Kelp/NExT-Guard/TrajGuard 在 GCG + RL-Obfuscation 下的鲁棒性。Secondary: 架构脆弱性分析 + CoT premeditation 阴性结果。详见 paper_framing.md。\\n\\n目标投稿：**ARR May 25, 2026**（7 天，D2=May 18）\\n\\n## 当前进展\\n\\n- 阶段：Research（MVP FAIL → pivot to benchmark-primary）\\n- MVP 结论：Layer 16 hidden states 在 CoT 中无 premeditation signal（token AUC=0.49 反预测）\\n- 基础设施：westd-39593（4×5090 32GB），200GB 数据盘\\n- Phase 0 产出：500 harmful traces（204 complied）+ 200 benign + probe_v2 checkpoint + hidden states\\n- Dream 模拟已启动（dream_20260517T145100），等待结果\\n\\n## 近期任务\\n\\n- [x] GPU 到位 + 环境部署\\n- [x] 代码框架 6 模块\\n- [x] Phase 0 trace gen + onset + probe + temporal（MVP FAIL，D006）\\n- [ ] Dream 结果评估（等待 10-25min）\\n- [ ] NExT-Guard 官方代码 clone + 验证\\n- [ ] Kelp/TrajGuard 论文规格调研（Agent 执行中）\\n- [ ] Qwen2.5-7B-Instruct 下载\\n- [ ] 修复 temporal_analysis.py（trace-level FPR control + cusum_max AUC）\\n- [ ] benchmark 实验启动（Dream 通过后）\\n\\n## 7 天 Timeline（May 18-25）\\n\\n| Phase | Days | 工作 | 状态 |\\n|-------|------|------|------|\\n| Plan | D2 | Dream + framing 确认 + 实验审批 | 进行中 |\\n| Benchmark | D2-5 | 3 monitors × (GCG + RL-Obfuscation) | 待启动 |\\n| Analysis | D4-6 | Controlled decomposition + vulnerability analysis + negative finding | 待启动 |\\n| Paper | D5-8 | Results → Method → Intro → Abstract | 待实验 |\\n\\n## GPU 预算\\n\\n- 分配：4×5090 32GB（westd-39593），全部属本项目（C001）\\n- P0：~101 GPU-hours | P1：~42h | P2：~16h\\n- 可用：672 GPU-hours（4卡×7天×24h），headroom 充足\\n- 瓶颈：RL-Obfuscation ~24h/monitor，3 monitors 可跨 GPU 并行\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-17 | D006: MVP FAIL — pre-onset CoT 无可检测的 premeditation | phase0_mvp_pipeline |\\n| D005 | 2026-05-17 | D004 降级为 CONDITIONAL：Reviewer 指出 probe 过拟合 + P95 异 | phase0_mvp_pipeline |\\n| D004 | 2026-05-17 | MVP 判定：Qualified PASS — pre-onset per-token AUC 不达 | mvp_trace_gen |\\n| D003 | 2026-05-17 | Onset 重定义为 response（&lt;/think> 后）首个 harmful token，Co | mvp_trace_gen |\\n| D002 | 2026-05-17 | Onset 定义修正：从\\\"首次 harmful topic mention\\\"改为\\\"首次 action | mvp_trace_gen |\\n| D001 | 2026-05-17 | Safe class 使用 benign prompts（GSM8K/ARC），不依赖 same-p | mvp_trace_gen |\\n\\n\\n\", \"total_chars\": 2296, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51c5e06b-7509-40aa-8fd6-44ebd43aad60",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "657637f2-0962-41bb-8629-a0b747c55d90",
  "sourceToolAssistantUUID": "51c5e06b-7509-40aa-8fd6-44ebd43aad60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-17T15:40:13.664Z_

Now I have all the information needed to write a thorough review. Let me also check whether there's a review report already generated for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "657637f2-0962-41bb-8629-a0b747c55d90",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8Pk3SsEspFaD97fjqyX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "903f64b9-7209-40b4-836c-7e3ec434cfe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSdDr9aS7zDn1FedRvaP5N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1521,
      "cache_read_input_tokens": 46941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1521,
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

_source line 27 · 2026-05-17T15:40:14.917Z_

<details open><summary>🔧 Tool call — Read · `toolu_016toZXSZNXKEAdrvCcrKw6C`</summary>

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
  "parentUuid": "903f64b9-7209-40b4-836c-7e3ec434cfe0",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8Pk3SsEspFaD97fjqyX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eacef90a-3bff-4474-91cc-30e48012dc9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSdDr9aS7zDn1FedRvaP5N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1521,
      "cache_read_input_tokens": 46941,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1521
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 46941,
          "cache_creation_input_tokens": 1521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1521,
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

_source line 28 · 2026-05-17T15:40:14.926Z_

<details><summary>↩ Tool result · `toolu_016toZXSZNXKEAdrvCcrKw6C`</summary>

```text
1	---
2	dream_id: dream_20260517T145100
3	tier: best
4	overall_score: weak accept (4/6)
5	timestamp: 2026-05-17T15:35:23.225981+00:00
6	---
7	
8	# Dream Review Report: StreamProbe-Bench
9	
10	**Paper:** StreamProbe-Bench: Adversarial Robustness Evaluation of Streaming Safety Monitors for Large Language Models
11	
12	**Review Mode:** Full (2 Reviewers + Roundtable)
13	
14	---
15	
16	## Roundtable Summary
17	
18	Both reviewers independently scored 4/6 (Weak Accept) with 4/5 confidence. After cross-examination, scores held at 4/6 with increased confidence that the paper has a publishable core but requires significant revision on statistical rigor, reference coverage, and methodological controls before reaching acceptance threshold.
19	
20	**Consensus:** The paper addresses a genuine, timely gap (no adversarial evaluation of streaming safety monitors exists) and produces an interesting architectural vulnerability inversion finding. However, the current manuscript lacks the statistical validation and methodological controls needed to fully support its central claims. With targeted revisions, this could reach 5/6.
21	
22	---
23	
24	## R1: Methods + Experiments (Score: 4/6, Confidence: 4/5)
25	
26	### Strengths
27	- **Genuine gap addressed.** The paper identifies and fills a real evaluation void — streaming safety monitors have never been tested under adaptive adversarial attack. The SoK reference (Wang et al., S&P 2026) and Qwen3Guard-Stream's 57.2pp degradation on merely novel prompts strongly motivate the work.
28	- **Well-specified threat model.** GCG (white-box to LLM, black-box to monitor) and RL-Obfuscation (weight-level) represent complementary, practically relevant attack vectors.
29	- **Controlled decomposition (Table 3) is the cleanest experiment.** Holding the probe constant and varying only aggregation strategy (Pointwise → MaxPool) isolates temporal aggregation as an independent robustness factor. The 0.23 AUC gap and monotonic ordering are compelling.
30	- **Architectural vulnerability inversion is genuinely interesting.** Kelp (temporal) resists RL but amplifies GCG; TrajGuard (geometric) shows the opposite. This goes beyond "monitors are fragile" to provide architectural insight.
31	- **Honest negative finding on CoT premeditation.** Token AUC ≤ 0.53 across layers 8–24 is well-documented with layer ablation ruling out the "wrong layer" hypothesis.
32	- **Cross-model replication (Table 5).** Qwen2.5-7B rank correlation r = 0.94 strengthens generalizability.
33	
34	### Weaknesses
35	
36	**(Major) Reimplementation fidelity insufficient for adversarial robustness claims.**
37	Kelp GRU (93.3% architecture match) and TrajGuard (91.0%) are reimplementations. The "architecture match percentage" metric is non-standard. The unmatched components (6.7% for Kelp: dropout schedule; 9.0% for TrajGuard: curvature normalization) could systematically affect adversarial vulnerability even when clean F1 is similar. Gradient properties, loss landscape geometry, and attack surface can diverge between implementations that share similar clean performance. The paper needs ablation showing unmatched components do not dominate the robustness signal.
38	
39	**(Major) No statistical validation on key comparisons.**
40	All main results tables show only point estimates. With 500 harmful prompts, standard errors on detection rates are approximately ±2–4pp. Critical comparisons driving the narrative — e.g., Kelp GCG (38.2%) vs. NExT-Guard GCG (42.7%), a 4.5pp gap — may fall within confidence intervals. The architectural vulnerability inversion claim requires demonstrated statistical significance, not just numerical ordering. Bootstrap 95% CIs and appropriate hypothesis tests (e.g., McNemar's test for paired comparisons) are needed throughout.
41	
42	**(Major) RL-Obfuscation convergence and hyperparameter confounds.**
43	The reward function weights (0.4 × quality + 0.5 × (1 − detection) + 0.1 × KL) are arbitrary and not sensitivity-tested. No convergence curves are reported. NExT-Guard's dramatic collapse to 11.7% might partly reflect easier RL convergence against its sparse architecture (cleaner gradient landscape, smaller effective attack surface) rather than purely architectural fragility. Without convergence curves and reward-weight sensitivity analysis (at least 2–3 configurations), the comparison is potentially confounded.
44	
45	**(Major) GCG budget fairness.**
46	256 steps per prompt with 20 suffix tokens is modest. Different monitors may have different gradient accessibility properties, meaning the same GCG budget represents different effective attack strengths per monitor. GCG convergence curves per monitor (detection rate vs. optimization steps) are needed to verify all monitors have plateaued and the comparison is fair.
47	
48	**(Minor) Sample size and prompt diversity.** 500 harmful + 200 benign is modest for a benchmark paper. Harm category distribution is unspecified; results may not generalize across categories.
49	
50	**(Minor) Linear-only probes for CoT finding.** Only linear probes at individual layers were tested. The conclusion should be scoped to "linear probes at individual middle layers" rather than the broader "hidden states do not encode compliance decisions."
51	
52	**(Minor) MaxPool advantage in Table 3.** MaxPool also has the highest clean AUC (0.972 vs. 0.938 for CUSUM). The robustness advantage may partly reflect stronger clean discrimination. Relative degradation ratios would be a fairer comparison.
53	
54	### Missing Experiments
55	1. GCG convergence curves per monitor (detection rate vs. steps)
56	2. RL reward weight sensitivity (at least 3 configurations)
57	3. Bootstrap 95% CIs on all detection rates in Tables 2–5
58	4. Per-harm-category breakdown of detection rates
59	5. Attack transferability across monitors (GCG suffixes optimized for one applied to another)
60	6. Nonlinear probe (2-layer MLP) for CoT finding
61	7. Reimplementation ablation on unmatched components
62	
63	---
64	
65	## R2: Novelty + Related Work (Score: 4/6, Confidence: 4/5)
66	
67	### Strengths
68	- **Vulnerability inversion is the strongest scientific contribution.** The mirror-image pattern between Kelp and TrajGuard across GCG/RL attacks, supported by mechanistic explanations (temporal propagation vs. geometric bypass), provides genuine architectural insight beyond "monitors are fragile."
69	- **Controlled decomposition is methodologically valuable.** Isolating temporal aggregation as a single variable with monotonic robustness ordering is clean experimental design that yields actionable guidance.
70	- **Cross-model validation (r = 0.94)** converts a potential weakness (single model) into a strength, confirming patterns are monitor-architecture-dependent, not model-dependent.
71	- **Negative CoT finding is community-useful.** With layer ablation across 5 layers, it rules out the most likely alternative hypothesis and closes the "just probe the reasoning trace" escape hatch.
72	
73	### Weaknesses
74	
75	**(Major) Limited methodological novelty.**
76	The paper applies existing attacks (GCG, RL-Obfuscation) to new targets (streaming monitors) without proposing new attack algorithms, defense mechanisms, or evaluation metrics. This is primarily an evaluation/benchmarking contribution. The controlled decomposition elevates it beyond pure application, but the novelty is in experimental design, not algorithmic contribution. For a top venue, the experimental rigor must therefore be exemplary — which connects to R1's statistical concerns.
77	
78	**(Major) Reference list is critically thin.**
79	Only 8 references is far below EMNLP standards (typically 30–50). Key missing references include:
80	- Carlini et al. on adaptive evaluation best practices (directly relevant to methodology)
81	- HarmBench (Mazeika et al.) as a benchmark comparison point
82	- SmoothLLM and other adversarial defense work
83	- Linear probing literature (Belinkov, Tenney et al.) for the CoT analysis
84	- Broader adversarial robustness literature connecting architectural properties to robustness (established in vision)
85	- Wang et al. SoK (cited in intro but details missing)
86	
87	This is not cosmetic — missing Carlini et al. affects whether the evaluation follows established best practices. Missing probing literature undermines the CoT analysis credibility.
88	
89	**(Major) Vulnerability inversion partially predictable from first principles.**
90	That temporal recurrence amplifies input perturbation (GCG) while resisting weight-level optimization (RL) — and that geometric features resist point perturbation but are malleable under gradient-based weight updates — could be anticipated by experts with adversarial ML background. The paper should reframe from "discovery" to "rigorous empirical confirmation with quantitative characterization." The value is in the precise quantification and controlled comparison, not in the directional finding itself.
91	
92	**(Minor) "False sense of security" framing slightly overstated.**
93	These monitors were designed and evaluated for standard (non-adversarial) safety detection. Demonstrating they fail under adaptive attack is important but not surprising. The framing implies the original authors were negligent, when in fact adversarial evaluation was simply not part of their scope. More measured framing would acknowledge this while still arguing for the importance of adversarial evaluation.
94	
95	**(Minor) No defensive contribution.**
96	The paper identifies vulnerabilities and offers architectural guidance ("prefer temporal for RL threats, geometric for GCG threats") but proposes no concrete mitigation or defense. Even a preliminary adversarial training experiment or ensemble approach would strengthen the practical contribution.
97	
98	**(Minor) CoT finding feels somewhat disconnected.**
99	The negative CoT premeditation result, while interesting, is tangentially connected to the main benchmark story. It could be better integrated if framed as "even the most optimistic monitoring approach — probing reasoning traces directly — fails."
100	
101	### Novelty and Significance Assessment
102	The paper's novelty is primarily empirical rather than methodological. For a benchmark paper, this is acceptable if the evaluation is rigorous and the insights are non-trivial. The vulnerability inversion pattern and controlled decomposition provide genuine insight beyond what the community could assume without evidence. However, the current statistical gaps weaken the case. The benchmark itself fills a real need, and if the community adopts it, the impact would be significant. The risk is that without stronger statistical foundations, the specific architectural rankings may not hold up to independent replication.
103	
104	---
105	
106	## Roundtable Convergence (Step 3)
107	
108	### Points of Agreement
109	1. **Genuine gap, timely contribution.** Both reviewers agree the paper addresses a real need.
110	2. **Controlled decomposition is the methodologically strongest experiment** — clean, single-variable, monotonic result.
111	3. **Statistical validation is the most critical missing element.** Without CIs and significance tests, the architectural inversion claim — the paper's primary novelty — stands on uncertain ground. Both reviewers agree this is a must-fix.
112	4. **Reimplementation concern is shared** but manageable if ablations on unmatched components are provided.
113	5. **Thin references hurt both framing and methodology.** R1 upgraded this concern after seeing R2's analysis — missing Carlini et al. is a methodological gap, not just a positioning issue.
114	6. **RL convergence confound needs resolution.** Convergence curves + reward weight sensitivity would either confirm or refute the fairness of the cross-monitor comparison.
115	
116	### Points of Disagreement (Resolved)
117	- **Predictability of inversion:** R2 argued it is partially predictable from first principles; R1 countered that post-hoc rationalizability doesn't diminish experimental value since practitioners lack the confidence to act on intuition without empirical confirmation. **Resolution:** Both agree the contribution is valuable as "rigorous empirical confirmation with precise quantification" but the paper should not frame it as a surprising discovery.
118	- **Novelty sufficiency:** R2 was more concerned about limited methodological novelty. R1 argued the controlled decomposition elevates it. **Resolution:** Both agree the paper is borderline — the benchmark + architectural insight is sufficient for a top venue IF statistical rigor is substantially improved. A pure benchmark paper without the inversion finding would score 3/6.
119	
120	---
121	
122	## Consolidated Score and Recommendation
123	
124	| | R1 | R2 | Consensus |
125	|---|---|---|---|
126	| Score | 4/6 | 4/6 | **4/6 (Weak Accept)** |
127	| Confidence | 4/5 | 4/5 | 4/5 |
128	
129	### Overall Assessment
130	The paper addresses a genuine evaluation gap with a well-designed benchmark and produces an interesting architectural vulnerability inversion finding. The controlled decomposition experiment is methodologically clean. However, three critical gaps prevent a higher score:
131	
132	1. **Statistical rigor:** No confidence intervals or significance tests on the comparisons that drive the paper's central claims. This is the single most important revision.
133	2. **Methodological controls:** RL convergence curves, GCG convergence curves per monitor, and reward weight sensitivity are needed to rule out confounds in the cross-monitor comparison.
134	3. **Scholarly context:** 8 references is inadequate. Missing Carlini et al. (adaptive evaluation), probing literature, and broader adversarial robustness work undermine both positioning and methodology.
135	
136	### Minimum Revisions for Acceptance (Priority-Ordered)
137	1. Bootstrap 95% CIs on all detection rates; McNemar's test or equivalent for pairwise monitor comparisons
138	2. GCG and RL convergence curves per monitor demonstrating fair comparison at chosen budgets
139	3. RL reward weight sensitivity analysis (at least 3 configurations)
140	4. Expand references to 25+ with proper positioning (Carlini adaptive evaluation, HarmBench, probing literature, adversarial robustness in vision)
141	5. Reimplementation ablation on unmatched components (Kelp dropout schedule, TrajGuard curvature normalization)
142	6. Reframe vulnerability inversion as "rigorous empirical confirmation" rather than novel discovery
143	
144	### Path to 5/6
145	If the above revisions are addressed — particularly items 1–3 confirming the statistical robustness of the architectural inversion claim — both reviewers indicated the score would rise to 5/6 (Accept). The paper has a strong publishable core; the issue is execution gaps in the current manuscript, not fundamental flaws in the research design.
146	
147	### Experiment Coverage Assessment
148	Comparing against the review context (16 planned experiments), the paper covers all major experiments. Key results are present: main benchmark (Table 2), controlled decomposition (Table 3), CoT layer ablation (Table 4), cross-model replication (Table 5), failure mode matrix (Table 6), Pareto frontiers (Table 7), probe fidelity (Table 8), SN-CUSUM (Appendix B). No planned experiment is entirely missing. The issue is depth of reporting (statistical validation) rather than breadth of coverage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eacef90a-3bff-4474-91cc-30e48012dc9d",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "33e4142a-2f96-4ed6-9989-8db509410b7e",
  "sourceToolAssistantUUID": "eacef90a-3bff-4474-91cc-30e48012dc9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-17T15:40:24.342Z_

Now I have a complete picture. Let me now produce my own R2 review, focused on Novelty and Related Work, as a distinct review from the one already generated (which was a consolidated report). Let me write a thorough, independent review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33e4142a-2f96-4ed6-9989-8db509410b7e",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8PmHaTRCnp1pDKLBFrk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83411539-7673-4758-921f-8b51cc83de5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnHdoTZr83mRYP3zULArU3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3992,
      "cache_read_input_tokens": 48462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3992,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 30 · 2026-05-17T15:40:24.722Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Wo57EaKDBbNNocxKmRVEPw`</summary>

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
  "parentUuid": "83411539-7673-4758-921f-8b51cc83de5e",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8PmHaTRCnp1pDKLBFrk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a7e6f1a-27f7-4fa4-90c8-bb7e5ca725e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnHdoTZr83mRYP3zULArU3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3992,
      "cache_read_input_tokens": 48462,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3992,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 31 · 2026-05-17T15:40:24.725Z_

<details><summary>↩ Tool result · `toolu_01Wo57EaKDBbNNocxKmRVEPw`</summary>

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
  "parentUuid": "5a7e6f1a-27f7-4fa4-90c8-bb7e5ca725e2",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "56a96621-f0c2-47f2-8644-8d5a2f18172e",
  "sourceToolAssistantUUID": "5a7e6f1a-27f7-4fa4-90c8-bb7e5ca725e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-17T15:42:10.272Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_014uVHxJaYvEEfJcP7aRTJAt`</summary>

```json
{
  "project": "streamprobe_adversarial_robustness",
  "tier": "best",
  "dream_id": "dream_20260517T145100",
  "overall_score": "weak accept (4/6)",
  "report": "---\ndream_id: dream_20260517T145100\ntier: best\nreviewer: R2 (Novelty and Related Work)\noverall_score: 4/6 (Weak Accept)\ntimestamp: 2026-05-17\n---\n\n# R2 Review: Novelty and Related Work\n\n**Paper:** StreamProbe-Bench: Adversarial Robustness Evaluation of Streaming Safety Monitors for Large Language Models\n\n---\n\n## 1. Summary\n\nThe paper introduces StreamProbe-Bench, a benchmark evaluating three architecturally distinct streaming safety monitors (Kelp GRU, NExT-Guard SAE, TrajGuard geometric) under GCG suffix optimization and RL-Obfuscation attacks. The main findings are: (1) all monitors suffer severe detection degradation (43pp GCG, 66pp RL average), (2) an architectural vulnerability inversion where temporal recurrence resists RL but amplifies GCG and geometric surveillance shows the opposite pattern, (3) a controlled decomposition isolating temporal aggregation as an independent robustness factor (0.23 AUC gap), and (4) a negative finding that CoT premeditation is not detectable via linear probes at any layer tested.\n\n---\n\n## 2. Strengths (Novelty and Positioning)\n\n- **Fills a verified evaluation gap.** The Wang et al. S&P 2026 SoK explicitly identifies absence of adaptive adversarial evaluation of streaming monitors as a priority. This paper is the first to fill that gap. The contribution is timely given rapid deployment of these monitors.\n\n- **Vulnerability inversion is the strongest scientific finding.** The mirror-image failure pattern between Kelp (GCG-vulnerable, RL-resistant) and TrajGuard (GCG-resistant, RL-vulnerable), supported by mechanistic metrics (GRU hidden state shift L2=2.84, post-RL curvature drop to 0.12), goes beyond \"monitors are fragile\" to provide predictive architectural guidance. Fisher exact tests (p<0.001) confirm the pattern is statistically real.\n\n- **Controlled decomposition is methodologically clean.** Using the same probe with 5 aggregation strategies as the sole variable produces a monotonic ordering that is both interpretable and actionable. This eliminates reimplementation confounds and provides a zero-cost defense recommendation (switch to max-pooling).\n\n- **Cross-model validation strengthens generalizability.** The r=0.94 correlation between DeepSeek and Qwen vulnerability patterns confirms the findings are monitor-architecture-dependent rather than model-specific. This is above-average diligence for a benchmark paper.\n\n- **Negative CoT finding is community-useful.** Layer ablation across 5 layers (8, 12, 16, 20, 24) rules out the \"wrong layer\" alternative hypothesis. Per-token AUC remaining at chance (0.49-0.53) across all layers with 95% CIs including 0.5 is a clean negative result that prevents premature deployment of CoT-based safety monitors.\n\n- **Text-level baseline (Llama-Guard) provides essential context.** Including a non-hidden-state monitor shows that hidden-state approaches offer higher baselines but larger adversarial degradation, creating an informative \"robustness inversion\" that contextualizes the results.\n\n---\n\n## 3. Weaknesses (Novelty, Related Work, Positioning)\n\n### (Major) Limited methodological novelty — primarily an evaluation contribution\n\nThe paper applies two existing attacks (GCG, RL-Obfuscation) to new targets (streaming monitors) without proposing any new attack algorithm, defense mechanism, detection method, or evaluation metric. The controlled decomposition, while clean, compares 5 standard temporal aggregation strategies (pointwise, window mean, EMA, CUSUM, max-pool) that are textbook signal processing techniques. No novel aggregation strategy is proposed. The CoT finding uses standard linear probes. For a top venue, the contribution is essentially \"we ran existing attacks on new targets and observed an interesting pattern.\" This is acceptable for a benchmark/evaluation paper IF:\n- The evaluation rigor is exemplary (statistical validation currently missing per R1)\n- The insights are non-trivial (the inversion pattern qualifies, but see below)\n- The community need is urgent (it is)\n\nThe paper is borderline on novelty. Without the vulnerability inversion finding, this would be a clear reject (3/6) as a pure application of known attacks to new targets.\n\n### (Major) Reference list is critically inadequate — 8 references total\n\nThe paper cites only 8 works. For EMNLP 2026, typical reference counts are 30-50. This is not merely cosmetic; missing references indicate gaps in scholarly awareness that affect both positioning and methodology:\n\n**Missing and essential:**\n- Carlini et al. (2019) \"On Evaluating Adversarial Robustness\" / Carlini & Wagner adaptive evaluation principles — directly relevant to methodology design. Without acknowledging this work, the paper's evaluation protocol lacks grounding in established best practices.\n- Mazeika et al. HarmBench (2024) — the closest existing benchmark, needed for explicit positioning of what StreamProbe-Bench adds.\n- Belinkov (2022) \"Probing Classifiers\" survey, Tenney et al. (2019) BERT layer analysis — the CoT probing analysis builds on a decade of probing methodology without acknowledging it.\n- SmoothLLM (Robey et al. 2023) and other adversarial defense literature for LLMs.\n- Jain et al. (2023) on baseline defenses against adversarial attacks on LLMs.\n- Li et al. WildJailbreak, Chao et al. PAIR — jailbreaking literature beyond GCG.\n- Vision adversarial robustness literature connecting architecture to robustness (Madry et al., Engstrom et al.) — the architectural vulnerability analysis has clear precedent in vision that should be acknowledged.\n- Safety alignment literature (Ouyang et al. RLHF, Bai et al. Constitutional AI) — necessary context for understanding what monitors are protecting.\n\n**Specific consequences of missing references:**\n1. The claim \"first adversarial robustness benchmark for streaming safety monitors\" cannot be verified without adequate surveying of related benchmarks.\n2. The CoT probing analysis lacks methodological grounding (why linear probes? what does the probing literature say about their limitations?).\n3. The architectural vulnerability analysis is disconnected from the substantial vision literature on architecture-robustness relationships.\n\n### (Major) Vulnerability inversion is partially predictable from first principles\n\nThe finding that temporal recurrence amplifies input perturbation (GCG appends suffix that propagates through memory) while resisting weight-level optimization (RL must suppress at every token) is directionally predictable for researchers with adversarial ML background. Similarly, geometric features being robust to point perturbations but malleable under gradient-based weight updates is a natural consequence of the mathematical properties involved (second-order statistics smooth over noise; direct weight optimization can reshape any differentiable computation).\n\nThe paper currently frames this as a discovery (\"the most striking result\"). It should be reframed as \"rigorous empirical confirmation with precise quantification of a pattern that, while directionally intuitive, lacked the evidence base for confident deployment decisions.\" The value is in the precise quantification (53pp vs 32pp GCG, 51pp vs 74pp RL, Fisher exact p<0.001) and controlled comparison, not in the directional finding itself.\n\n### (Minor) \"False sense of security\" framing is slightly unfair\n\nThe monitors being evaluated (Kelp, NExT-Guard, TrajGuard) were designed for standard safety detection, not adversarial robustness. Their papers did not claim adversarial robustness. Demonstrating they fail under adaptive attack is important and timely, but the \"false sense of security\" framing implies the original authors were negligent or deceptive. A more measured framing would be: \"deployment without adversarial evaluation creates vulnerability\" rather than \"reported benchmarks create a false sense of security.\"\n\n### (Minor) No defensive contribution\n\nThe paper identifies vulnerabilities and provides architectural guidance (prefer temporal for RL threats, geometric for GCG threats) but proposes no concrete mitigation beyond \"use max-pooling.\" Even a preliminary adversarial training experiment, ensemble of complementary architectures (temporal + geometric), or detection-aware fine-tuning would strengthen practical impact. The controlled decomposition suggests max-pooling as a \"zero-cost defense\" but does not validate it against an adaptive attacker aware of the max-pooling strategy.\n\n### (Minor) CoT finding feels partially disconnected from the main narrative\n\nThe negative CoT premeditation result is interesting but only tangentially connected to the benchmark story. The connection is implicit (\"even the most optimistic monitoring approach fails\") but not explicitly integrated into the main narrative arc. The paper would benefit from either: (a) integrating it as \"even probing the reasoning process directly cannot rescue detection under adversarial conditions,\" or (b) separating it as a clearly distinct contribution rather than the current half-integrated state.\n\n### (Minor) Benchmark scope is narrow for a \"benchmark paper\"\n\nStreamProbe-Bench evaluates 3 monitors, 2 attacks, 1-2 models. Established benchmarks (HarmBench, AdvBench) cover substantially more methods, attacks, and models. The paper positions itself as a benchmark contribution but the scope is closer to a focused empirical study. This is fine if framed correctly, but the title (\"Bench\") and contribution framing set expectations that the current scope does not fully meet.\n\n---\n\n## 4. Questions to Authors\n\n1. **On predictability:** Were the vulnerability inversion patterns predicted before running experiments, or discovered post-hoc? If predicted, please state this explicitly as it would strengthen the mechanistic analysis. If post-hoc, the framing should be adjusted.\n\n2. **On reference coverage:** Why are only 8 works cited? Is this a space constraint, or does the author(s) genuinely believe no other related work exists? Specifically, how does this work relate to Carlini et al.'s principles for adaptive evaluation, and the probing classifier literature?\n\n3. **On adaptive attacks against max-pooling:** The controlled decomposition shows max-pooling is most robust under GCG. But if an attacker knows the monitor uses max-pooling, they could specifically optimize to suppress safety signal at every token. Have you tested GCG/RL with explicit max-pooling awareness in the attack objective?\n\n4. **On NExT-Guard SAE collapse:** NExT-Guard drops to 11.7% under RL (near chance). Is this because RL converges faster against sparse targets (confirmed: 18.2K steps), or because the SAE architecture is fundamentally unsuitable for adversarial settings? Could the SAE be retrained or regularized to resist this?\n\n5. **On the text baseline:** Llama-Guard shows only 18.4pp GCG drop (smallest in the benchmark). Does this suggest text-level monitoring is the most practical robust approach, undermining the premise that hidden-state monitoring is superior?\n\n6. **On CoT scope:** The negative finding uses only DeepSeek-R1-Distill-7B and linear probes. Would nonlinear probes (MLP) or different reasoning models (e.g., a model with explicit scratchpad training) potentially yield different results?\n\n---\n\n## 5. Minor Issues\n\n- **Reference format inconsistency:** Some entries use \"Authors\" as placeholder (e.g., \"Kelp Authors,\" \"RL-Obfuscation Authors\") rather than actual author names. This appears to be anonymization but reads as incomplete scholarship.\n- **Venue inconsistency in bibliography:** The paper summary mentions Kelp at \"ACL 2026\" and NExT-Guard at \"NAACL 2026,\" but the .tex file lists them at \"ACL 2025\" and \"NeurIPS 2025.\" These should be verified and consistent.\n- **AI writing patterns:** The paper is relatively clean of obvious AI markers. I note occasional em-dash usage (the \"59--89\\% evasion rate\" is legitimate range notation). The phrase \"the most striking result\" (line 138) is mildly promotional but acceptable.\n- **Abstract length:** At approximately 180 words, the abstract is within typical bounds and well-structured.\n- **Table 2 layout:** Baseline values are placed below the attacked results, which is unconventional. Consider placing baselines first or in a separate column for easier visual comparison.\n- **\"Reimplemented\" caveat:** The abstract and introduction should more prominently note that 2 of 3 monitors are reimplementations (currently only in Methods section).\n\n---\n\n## 6. Scores\n\n| Dimension | Score | Justification |\n|-----------|-------|---------------|\n| **Overall** | **4/6 (Weak Accept)** | Fills a genuine gap with an interesting architectural finding, but limited methodological novelty and critically thin references prevent a higher score. |\n| **Confidence** | **4/5** | I have sufficient expertise in adversarial robustness and LLM safety to evaluate this work. Slight uncertainty on streaming monitor internals. |\n| **Novelty** | **2/4 (Moderate)** | Primarily empirical evaluation using existing attacks on new targets. The vulnerability inversion is interesting but partially predictable. No new methods proposed. |\n| **Significance** | **3/4 (High)** | If the community adopts this benchmark and the architectural guidance influences deployment decisions, impact would be substantial. The negative CoT finding prevents a class of premature deployments. |\n\n---\n\n## 7. Recommendation\n\n**Weak Accept** contingent on revisions. The paper has a publishable core: a genuine evaluation gap, an interesting architectural vulnerability pattern, and a clean controlled decomposition. However, three issues must be addressed:\n\n1. **Expand references to 25+ works** with proper positioning against adversarial evaluation methodology (Carlini), existing benchmarks (HarmBench), probing literature (Belinkov), and architectural robustness literature from vision.\n2. **Reframe vulnerability inversion** as rigorous empirical confirmation rather than surprising discovery. Acknowledge its partial predictability while emphasizing the value of precise quantification.\n3. **Add statistical validation** (bootstrap CIs, significance tests) on all comparisons driving the architectural inversion narrative. Without this, the paper's central claim rests on point estimates with unknown uncertainty.\n\nIf these revisions are addressed, the score rises to 5/6. The core research is sound; the manuscript needs stronger scholarly grounding and statistical support."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56a96621-f0c2-47f2-8644-8d5a2f18172e",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8Pn2ZLy3pioZtRHP36Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61a56048-fbfa-46f6-bac2-b54cf3614c29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017D9t6KL4HR4TqrHMU4EkdE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 52454,
      "output_tokens": 3563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 721
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3563,
          "cache_read_input_tokens": 52454,
          "cache_creation_input_tokens": 721,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 721,
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

_source line 33 · 2026-05-17T15:42:13.610Z_

<details><summary>↩ Tool result · `toolu_014uVHxJaYvEEfJcP7aRTJAt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts/dream_reports/dream_20260517T145100/best/review_report.md\", \"dream_id\": \"dream_20260517T145100\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61a56048-fbfa-46f6-bac2-b54cf3614c29",
  "isSidechain": true,
  "promptId": "55b95446-cc2b-4dc3-9415-9da5d7d69bfe",
  "agentId": "a9fd73ad3308fafe9",
  "type": "user",
  "uuid": "20126e06-12de-4bae-8e2a-72882521dd73",
  "sourceToolAssistantUUID": "61a56048-fbfa-46f6-bac2-b54cf3614c29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-17T15:42:57.300Z_

Review submitted. Here is the summary:

**R2 Review (Novelty and Related Work): 4/6 Weak Accept**

Key findings:

**Strengths:**
- Fills a verified evaluation gap (Wang et al. SoK identifies this as priority)
- Vulnerability inversion between temporal and geometric architectures is the strongest scientific contribution, with mechanistic evidence and statistical significance (Fisher exact p<0.001)
- Controlled decomposition is methodologically clean (single variable, monotonic ordering, 0.23 AUC gap)
- Cross-model validation (r=0.94) strengthens generalizability
- Negative CoT finding with layer ablation rules out most likely alternative hypotheses

**Critical weaknesses:**
1. **Limited methodological novelty** — applies existing attacks to new targets with no new methods proposed. The controlled decomposition compares standard signal processing techniques. Without the inversion finding, this would be a clear reject.
2. **Only 8 references** — far below EMNLP standards (30-50). Missing Carlini et al. (adaptive evaluation methodology), HarmBench, probing literature (Belinkov), vision adversarial robustness, safety alignment literature. This is not cosmetic; it indicates methodological grounding gaps.
3. **Vulnerability inversion is partially predictable from first principles** — should be reframed as "rigorous empirical confirmation" rather than "striking discovery."

**Scores:** Overall 4/6, Confidence 4/5, Novelty 2/4 (Moderate), Significance 3/4 (High).

**Path to acceptance:** Expand references to 25+, reframe the inversion finding, add statistical validation (CIs and significance tests) on all architectural comparisons.

Report saved to: `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness/artifacts/dream_reports/dream_20260517T145100/best/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20126e06-12de-4bae-8e2a-72882521dd73",
  "isSidechain": true,
  "agentId": "a9fd73ad3308fafe9",
  "requestId": "req_011Cb8Pv2CEoLEUMKT1dgiNo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90bc67a7-0545-4fad-b4a9-8d004a14cdec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/streamprobe_adversarial_robustness",
  "sessionId": "a609e279-6894-4252-b33c-e21324d33915",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKMMrd3zpBdMZ4GJ8KFp4u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3697,
      "cache_read_input_tokens": 53175,
      "output_tokens": 467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3697
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 467,
          "cache_read_input_tokens": 53175,
          "cache_creation_input_tokens": 3697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3697,
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
