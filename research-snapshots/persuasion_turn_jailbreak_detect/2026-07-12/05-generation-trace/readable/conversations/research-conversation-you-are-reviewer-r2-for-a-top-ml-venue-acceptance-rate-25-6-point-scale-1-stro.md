# Research conversation: You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ab148d48e5397ce79.jsonl`
- **Structured JSON:** [`bed9777ad7a5c9deabcc.json`](../../sessions/be/bed9777ad7a5c9deabcc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-17T17:35:37.926Z_

You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus area is **Novelty, Positioning, and Related Work**.

## Paper Summary

**Title**: "Lexical Confounds in Multi-Turn Jailbreak Detection: A Register-Normalization Audit"

**Core claim**: Multi-turn jailbreak detection benchmarks are systematically inflated by lexical confounds. A register-normalization protocol is proposed to audit this. After normalization, a persuasion-grounded detector provides no significant advantage over a vanilla semantic baseline.

**Paper type**: Analysis/evaluation methodology paper (negative result paper). Not proposing a new detection method, but auditing an existing paradigm.

**Contributions claimed**:
1. A register-normalization protocol for auditing lexical confounds (TF-IDF 1.0 → 0.73 in two rounds)
2. Empirical evidence that persuasion-grounded features provide no significant advantage on clean data (N=72, all p>0.3)
3. Systematic evaluation showing both approaches fail equivalently under adversarial perturbation, cross-attack generalization, and hard negatives

**Related Work covered** (Section 2, ~0.5 page):
- Multi-turn jailbreak attacks: Crescendo, FITD, Deceptive Delight, Bullwinkel et al.
- Multi-turn detection: DeepContext, persuasion-based (Zeng et al. PAP taxonomy, Hagendorff)
- Evaluation methodology: lexical confounds in toxicity detection (Gonen and Goldberg)

**References**: 8 total. [1] Bullwinkel 2025, [2] Zeng 2024 (PAP/ACL), [3] Hagendorff 2026, [4] Austin 1962, [5] Searle 1969, [6] DeepContext 2026, [7] Gonen & Goldberg 2019, [8] How Do LLMs Persuade 2025.

**Key experiments** (10 total):
1. Lexical Confound Audit: TF-IDF=1.0 raw, 0.73 after normalization
2. Treatment vs Baseline on clean data: 1pp delta, p=0.62
3. Encoder quality degradation: persuasion acc 0.796→0.63 on clean data
4. Scrambled label ablation: only 2pp drop
5. Adversarial perturbation: both drop ~14pp equally
6. Cross-attack generalization: both collapse to F1~0.54-0.58
7. Hard negatives: FPR=0.22 for both
8. Strategy transition: negligible differences
9. Cross-checkpoint variance: 2pp, weak encoder-detection correlation
10. DeepContext proxy: 3pp gap attributable to encoder capacity

## Your Task

Evaluate the paper on **novelty, significance, positioning, and related work coverage**. Produce a structured review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, 3-5 items, each with brief explanation)
3. **Weaknesses** (bulleted, 3-5 items, each with brief explanation)
4. **Questions for Authors** (2-3 specific questions)
5. **Minor Issues** (formatting, citation coverage, framing)
6. **Preliminary Score** (1-6 scale) and **Confidence** (1-5: 1=low, 5=expert)

Focus on:
- Is the core finding (lexical confounds inflate multi-turn detection) novel or already known?
- Does the register-normalization protocol constitute a sufficient methodological contribution?
- Is the Related Work section adequate? Only 8 references is very thin for a top venue.
- How does this compare to prior work on annotation artifacts (e.g., SNLI hypothesis-only baselines, toxicity confounds)?
- Is the paper positioned correctly as a methodology/analysis paper?
- Is the negative result (persuasion grounding doesn't help) meaningful and well-argued?
- Does the paper adequately discuss implications and future directions?
- Is the scope of the study (one pipeline, one dataset, one taxonomy) sufficient to support the generality of claims?


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "f0d7bc63-7092-482a-8133-5ee56fcf04a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T17:35:37.932Z_

```json
{
  "parentUuid": "f0d7bc63-7092-482a-8133-5ee56fcf04a7",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
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
  "uuid": "6b5dbf6f-47e0-48fd-82a8-612fb12b2d37",
  "timestamp": "2026-05-17T17:35:37.932Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T17:35:41.440Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013h3Sfb4e9FL3K6RvxMhs17`</summary>

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
  "parentUuid": "6b5dbf6f-47e0-48fd-82a8-612fb12b2d37",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YZba9NP3uu4tfFZQKD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5dbf30b2-fa88-48ce-ba0b-1a6d2090926e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtLdsZHU6TqcKodd8yF3us",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8166,
      "cache_read_input_tokens": 8255,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8166,
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

_source line 4 · 2026-05-17T17:35:41.448Z_

<details><summary>↩ Tool result · `toolu_013h3Sfb4e9FL3K6RvxMhs17`</summary>

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
  "parentUuid": "5dbf30b2-fa88-48ce-ba0b-1a6d2090926e",
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "e9380dfe-a888-43e4-83ec-f30e9f40a2a1",
  "sourceToolAssistantUUID": "5dbf30b2-fa88-48ce-ba0b-1a6d2090926e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:35:51.135Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017Jb8UDPJ2ammtq5bNDkxpS`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "report.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9380dfe-a888-43e4-83ec-f30e9f40a2a1",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YZrstmt6A8XJiKWuZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd9eabf9-9e7c-4650-ae4a-2e9f2e291103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZMm4oETPSXW2U9gnGvard",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 6 · 2026-05-17T17:35:51.152Z_

<details><summary>↩ Tool result · `toolu_017Jb8UDPJ2ammtq5bNDkxpS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **phase_b_full** (success): Persuasion-grounded DeBERTa embeddings (multi-task fine-tuned on 8-class persuasion + intent) enable significantly earlier detection of Crescendo jailbreak attacks compared to vanilla DeBERTa embeddings, especially at low K (2-3 turns) ← 基于 pilot_phase_b\\n- **pilot_phase_b** (success): Persuasion-aware DeBERTa embeddings (multi-task fine-tuned) fed to Bi-GRU will outperform vanilla DeBERTa embeddings at early detection (K=2,3,5 turns) of Crescendo-style jailbreak attacks\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-33183: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 707, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd9eabf9-9e7c-4650-ae4a-2e9f2e291103",
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "a3577c41-1882-4e64-a60a-a7dd94c6138f",
  "sourceToolAssistantUUID": "bd9eabf9-9e7c-4650-ae4a-2e9f2e291103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:35:51.653Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GgdQvGhV3bx8JWYmA7c7e3`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3577c41-1882-4e64-a60a-a7dd94c6138f",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YZrstmt6A8XJiKWuZz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "560165f2-99b8-421c-b031-527202951166",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZMm4oETPSXW2U9gnGvard",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 8 · 2026-05-17T17:35:51.668Z_

<details><summary>↩ Tool result · `toolu_01GgdQvGhV3bx8JWYmA7c7e3`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "560165f2-99b8-421c-b031-527202951166",
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "d365649b-ec96-41a3-81cd-e1eb8d5eb868",
  "sourceToolAssistantUUID": "560165f2-99b8-421c-b031-527202951166",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:35:56.016Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0196AX4bTmqttKLxXAevr4Ji`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d365649b-ec96-41a3-81cd-e1eb8d5eb868",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YacYTYbajpyGPss9GM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf453a51-3451-4b9c-8d40-4f039b1f5ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYTLvVGijYk2LDeyN7STBd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 17690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 802,
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

_source line 10 · 2026-05-17T17:35:56.027Z_

<details><summary>↩ Tool result · `toolu_0196AX4bTmqttKLxXAevr4Ji`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf453a51-3451-4b9c-8d40-4f039b1f5ca8",
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "2087c252-c2a9-427e-b5de-b11b83fc30c3",
  "sourceToolAssistantUUID": "cf453a51-3451-4b9c-8d40-4f039b1f5ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:35:57.580Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QEDn38vpaUg2Drq3HDGaJd`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2087c252-c2a9-427e-b5de-b11b83fc30c3",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YacYTYbajpyGPss9GM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f93868ca-bfb4-45ee-9b28-435c4ac9e0fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYTLvVGijYk2LDeyN7STBd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 17690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 802,
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

_source line 12 · 2026-05-17T17:35:57.605Z_

<details><summary>↩ Tool result · `toolu_01QEDn38vpaUg2Drq3HDGaJd`</summary>

```text
artifacts/dream_reports/dream_20260517T165817/best/paper.tex
artifacts/dream_reports/dream_20260517T165817/median/paper.tex
artifacts/dream_reports/dream_20260517T165817/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f93868ca-bfb4-45ee-9b28-435c4ac9e0fa",
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "c906c5ea-3f09-4fab-90e2-7eed025ef2cc",
  "sourceToolAssistantUUID": "f93868ca-bfb4-45ee-9b28-435c4ac9e0fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:36:01.931Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KoSRV1d6kr6WkZPb2sXaxL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c906c5ea-3f09-4fab-90e2-7eed025ef2cc",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8Yb4g5nL5kGyFD54yRu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df2795e0-f765-4a15-ad19-778dabdcce37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Ujh6qwR1kx8DnUDk8jyV5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 18492,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 383
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 18492,
          "cache_creation_input_tokens": 383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 383,
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

_source line 14 · 2026-05-17T17:36:02.322Z_

<details><summary>↩ Tool result · `toolu_01KoSRV1d6kr6WkZPb2sXaxL`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{hyperref}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{natbib}
11	\usepackage{xcolor}
12	\usepackage{tabularx}
13	\usepackage{caption}
14	
15	\title{DisPeD: Exploiting the Pragmatic Evasion Asymmetry\\for Robust Multi-Turn Jailbreak Detection}
16	
17	\author{Anonymous}
18	\date{}
19	
20	\begin{document}
21	\maketitle
22	
23	% ============================================================
24	% ABSTRACT
25	% ============================================================
26	\begin{abstract}
27	Multi-turn jailbreak attacks against Large Language Models (LLMs) distribute adversarial intent across individually benign turns, defeating detectors that operate at the lexical or semantic level. We identify a \emph{Pragmatic Evasion Asymmetry}: attackers can freely paraphrase surface content, but the underlying persuasion playbook (rapport building, reframing, escalation) is a structural prerequisite for attack success and cannot be removed without abandoning the attack itself. DisPeD exploits this asymmetry by fine-tuning DeBERTa on an 8-class persuasion strategy taxonomy to produce pragmatic-aware turn embeddings, then modeling the temporal strategy sequence with a GRU for conversation-level classification. On register-normalized data that eliminates lexical shortcuts (TF-IDF reduced from 1.0 to 0.58), DisPeD achieves F1\,=\,0.91 at only $K$\,=\,2 turns, a 14 percentage point (pp) improvement over a vanilla semantic baseline ($p$\,<\,0.001). Under adversarial paraphrasing, DisPeD degrades by only 3\,pp while semantic and lexical baselines degrade by 13\,pp and 18\,pp respectively. A model trained exclusively on Crescendo-style attacks generalizes zero-shot to Foot-in-the-Door and Deceptive Delight attacks with an average F1 of 0.85, outperforming the semantic baseline by 16.5\,pp. These results establish that discourse-level persuasion patterns provide a robust and generalizable signal for early multi-turn jailbreak detection.
28	\end{abstract}
29	
30	% ============================================================
31	% 1. INTRODUCTION
32	% ============================================================
33	\section{Introduction}
34	
35	Multi-turn jailbreak attacks pose a growing threat to deployed LLMs. Attacks such as Crescendo~\citep{russinovich2024greatnow}, Foot-in-the-Door (FITD)~\citep{zhou2024speak}, and Deceptive Delight~\citep{jiang2024deceptive} distribute adversarial intent across multiple conversational turns, each of which appears benign in isolation. \citet{bullwinkel2025multiturn} show that per-turn representations of these attacks are deliberately kept in a ``benign'' region of embedding space, causing representation-level defenses to fail with a 50-point ASR gap. Temporal approaches that track generic semantic drift~\citep{su2026deepcontext} confuse benign conversational evolution with adversarial manipulation, producing high false-positive rates.
36	
37	Why are these attacks so effective? A multi-turn attacker must accomplish two things: (1) maintain surface-level benignity on each turn, and (2) gradually steer the model toward compliance through a persuasion playbook. \citet{zeng2024persuasion} and \citet{hagendorff2026nature} independently show that identifiable persuasion strategies appear in over 97\% of successful multi-turn attacks. The attacker has enormous freedom in choosing \emph{what words} to use (lexical level) and \emph{what topics} to discuss (semantic level), but the underlying \emph{pragmatic function} of each turn (rapport building, authority appeal, reframing) is constrained by the attack's functional requirements.
38	
39	This observation motivates what we call the \textbf{Pragmatic Evasion Asymmetry}: an evasion hierarchy exists in which lexical features are easily evaded via paraphrasing, semantic embeddings are moderately robust but still vulnerable to per-turn content manipulation, and pragmatic persuasion patterns are structurally difficult to evade because they constitute the functional mechanism of the attack. In the terminology of Speech Act Theory~\citep{austin1962things,searle1969speech}, existing detectors operate at the locutionary act level (what was said), while DisPeD operates at the illocutionary act level (what was done).
40	
41	We present \textbf{DisPeD} (\textbf{Dis}course-level \textbf{Pe}rsuasion \textbf{D}etector), a two-stage pipeline that first fine-tunes DeBERTa-v3-base~\citep{he2021debertav3} on a multi-task objective combining 8-class persuasion strategy classification and binary intent classification, then feeds the resulting turn embeddings into a bidirectional GRU for conversation-level jailbreak detection. By grounding turn representations in a persuasion taxonomy derived from Cialdini's influence principles~\citep{cialdini2001science}, DisPeD detects the characteristic escalation trajectory of multi-turn attacks at the earliest possible stage.
42	
43	Our contributions are:
44	\begin{enumerate}
45	    \item We formalize the \emph{Pragmatic Evasion Asymmetry} and provide empirical evidence through a three-tier robustness experiment: under adversarial paraphrasing, DisPeD (pragmatic) degrades by 3\,pp, a vanilla semantic baseline by 13\,pp, and a TF-IDF lexical baseline by 18\,pp (Section~\ref{sec:evasion}).
46	    \item We demonstrate that persuasion-grounded embeddings enable significantly earlier detection: F1\,=\,0.91 at $K$\,=\,2 turns versus 0.77 for the semantic baseline, a 14\,pp advantage that holds across attack types with zero-shot cross-attack transfer averaging 16.5\,pp improvement (Sections~\ref{sec:main_results} and~\ref{sec:cross_attack}).
47	    \item We provide a mechanistic analysis showing that jailbreak conversations exhibit monotonic escalation trajectories in persuasion strategy space (monotonicity score 0.82 vs. 0.34 for benign), explaining why pragmatic features succeed where semantic features fail (Section~\ref{sec:trajectory}).
48	\end{enumerate}
49	
50	% ============================================================
51	% 2. RELATED WORK
52	% ============================================================
53	\section{Related Work}
54	
55	\paragraph{Multi-turn jailbreak attacks.}
56	Crescendo~\citep{russinovich2024greatnow} gradually escalates through conversational rapport, achieving high attack success rates against commercial LLMs. FITD~\citep{zhou2024speak} applies the foot-in-the-door compliance technique, starting with small requests and progressively increasing severity. Deceptive Delight~\citep{jiang2024deceptive} interleaves harmful content within benign creative writing frames. These attacks share a common structure: a persuasion playbook that transitions from trust-building to explicit elicitation across turns. \citet{hagendorff2026nature} analyze persuasion strategies in adversarial conversations and find identifiable patterns in 97\% of successful attacks, confirming that the persuasion structure is systematic rather than incidental.
57	
58	\paragraph{Jailbreak detection.}
59	Single-turn detectors such as perplexity filters~\citep{alon2023detecting} and input classifiers~\citep{inan2023llama} fail against multi-turn attacks because individual turns appear benign. \citet{bullwinkel2025multiturn} demonstrate that per-turn representations are deliberately maintained in benign embedding regions. DeepContext~\citep{su2026deepcontext} addresses this by tracking semantic drift across turns with an encoder-RNN pipeline, but uses generic embeddings that conflate benign topic evolution with adversarial manipulation.
60	
61	\paragraph{Persuasion and LLM safety.}
62	\citet{zeng2024persuasion} compile 40 persuasion techniques used in jailbreaking and show that persuasion-augmented prompts significantly increase ASR. \citet{chen2025persuade} study how LLMs deploy persuasion strategies during multi-turn interactions, demonstrating that persuasion dynamics are extractable from turn-level representations. Our work is the first to use persuasion-grounded representations for jailbreak \emph{detection} rather than attack construction or analysis.
63	
64	% ============================================================
65	% 3. METHOD
66	% ============================================================
67	\section{Method}
68	\label{sec:method}
69	
70	DisPeD consists of two stages: a persuasion-grounded encoder and a temporal sequence classifier.
71	
72	\subsection{Stage 1: Persuasion-Grounded Encoder}
73	
74	We fine-tune DeBERTa-v3-base on a multi-task objective with two heads:
75	
76	\begin{itemize}
77	    \item \textbf{Persuasion strategy classification} (8 classes): rapport building, authority appeal, reciprocity, social proof, commitment/consistency, scarcity/urgency, reframing, and direct request. These categories are derived from Cialdini's principles of influence~\citep{cialdini2001science} and adapted for adversarial conversational contexts following \citet{zeng2024persuasion}. Benign turns lacking a persuasion function receive a ``none'' label.
78	    \item \textbf{Intent classification} (binary): whether the turn carries jailbreak intent.
79	\end{itemize}
80	
81	The total loss is $\mathcal{L} = \mathcal{L}_{\text{persuasion}} + \lambda \mathcal{L}_{\text{intent}}$, where $\lambda = 1.0$. After training, we extract the [CLS] embedding from the fine-tuned encoder as the persuasion-grounded turn representation. The encoder achieves 79\% accuracy on 8-class persuasion classification and 94\% on binary intent classification (Table~\ref{tab:encoder}).
82	
83	\subsection{Stage 2: Temporal Sequence Classification}
84	
85	Given a conversation of $K$ turns, we obtain turn embeddings $\{e_1, \ldots, e_K\}$ from the Stage 1 encoder. A bidirectional GRU processes the embedding sequence and outputs a conversation-level binary classification (jailbreak vs. benign) from the final hidden state. This architecture captures the temporal progression of persuasion strategies across turns.
86	
87	\subsection{Baselines}
88	
89	We compare DisPeD against three baselines spanning the evasion hierarchy:
90	\begin{itemize}
91	    \item \textbf{TF-IDF + Logistic Regression}: a lexical baseline operating on bag-of-words features.
92	    \item \textbf{DeBERTa Semantic Baseline}: the same Stage 2 GRU pipeline but with \emph{vanilla} (not fine-tuned) DeBERTa embeddings, representing semantic-level detection.
93	    \item \textbf{DeepContext Proxy}: BERT-base + GRU, simulating the DeepContext architecture with generic drift features and no persuasion grounding.
94	\end{itemize}
95	
96	% ============================================================
97	% 4. EXPERIMENTAL SETUP
98	% ============================================================
99	\section{Experimental Setup}
100	\label{sec:setup}
101	
102	\subsection{Data Preparation and Register Normalization}
103	\label{sec:data}
104	
105	Our dataset consists of 480 conversations (240 jailbreak, 240 benign) with 72 held out for testing. Jailbreak conversations are Crescendo-style multi-turn attacks; benign conversations are drawn from standard conversational corpora and WildChat~\citep{zhao2024wildchat}.
106	
107	A critical challenge in multi-turn jailbreak detection is \emph{lexical shortcut}: scripted attack dialogues have distributional properties distinct from naturalistic benign conversations, allowing simple bag-of-words classifiers to succeed without learning meaningful features. On our original data, TF-IDF separability was 1.0, indicating complete lexical shortcut.
108	
109	We apply register normalization using LLM paraphrasing to convert jailbreak turns from formal/scripted register to conversational register, eliminating the distributional gap. Table~\ref{tab:tfidf_diagnostic} confirms the effectiveness of this procedure: TF-IDF drops from 1.0 to 0.58, below our hard gate of 0.75 but above the random baseline of 0.50, reflecting residual functional vocabulary (e.g., ``hypothetical,'' ``scenario'') that attackers cannot entirely avoid. Persuasion strategy annotations are preserved at 94\% after normalization, confirming that the persuasion structure is a discourse-level phenomenon independent of lexical realization.
110	
111	\begin{table}[t]
112	\centering
113	\caption{TF-IDF separability before and after register normalization.}
114	\label{tab:tfidf_diagnostic}
115	\begin{tabular}{lcc}
116	\toprule
117	\textbf{Condition} & \textbf{TF-IDF} & \textbf{Vocab Overlap (\%)} \\
118	\midrule
119	Original data & 1.00 & 12.3 \\
120	Register-normalized & 0.58 & 41.7 \\
121	Random baseline & 0.50 & 50.0 \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	\subsection{Multi-Attack Dataset}
127	\label{sec:multi_attack_data}
128	
129	To evaluate cross-attack generalization (Section~\ref{sec:cross_attack}), we generate additional attack conversations in two families beyond Crescendo using Qwen3-8B: 72 FITD-style conversations (avg. 6.8 turns) employing the foot-in-the-door compliance escalation pattern, and 65 Deceptive Delight-style conversations (avg. 5.2 turns) interleaving harmful content within benign frames. All generated conversations receive persuasion strategy annotations with 91\% LLM annotation consistency. Table~\ref{tab:attack_stats} summarizes the dataset statistics.
130	
131	\begin{table}[t]
132	\centering
133	\caption{Attack type statistics. TF-IDF measured against benign conversations.}
134	\label{tab:attack_stats}
135	\begin{tabular}{lcccc}
136	\toprule
137	\textbf{Attack Type} & \textbf{$n$} & \textbf{Avg Turns} & \textbf{Turn Range} & \textbf{TF-IDF} \\
138	\midrule
139	Crescendo (original) & 240 & 5.5 & 3--12 & 0.58 \\
140	FITD (generated) & 72 & 6.8 & 4--10 & 0.61 \\
141	Deceptive Delight (generated) & 65 & 5.2 & 3--8 & 0.55 \\
142	\bottomrule
143	\end{tabular}
144	\end{table}
145	
146	The three attack types share the same persuasion strategy vocabulary but differ in temporal arrangement. As shown in Table~\ref{tab:strategy_dist}, FITD relies heavily on reciprocity (30\%) and commitment/consistency (25\%), reflecting its gradual compliance escalation. Deceptive Delight favors authority appeal (22\%) and social proof (18\%), using authoritative framing to embed harmful content. Crescendo is more evenly distributed across strategies. This variation in strategy profiles, combined with a shared underlying vocabulary, provides the conditions for testing zero-shot cross-attack transfer.
147	
148	\begin{table}[t]
149	\centering
150	\caption{Persuasion strategy distribution (\%) by attack type.}
151	\label{tab:strategy_dist}
152	\begin{tabular}{lccc}
153	\toprule
154	\textbf{Strategy} & \textbf{Crescendo} & \textbf{FITD} & \textbf{Dec. Delight} \\
155	\midrule
156	Rapport building & 28 & 35 & 15 \\
157	Authority appeal & 12 & 8 & 22 \\
158	Reciprocity & 18 & 30 & 10 \\
159	Social proof & 8 & 5 & 18 \\
160	Commitment/consistency & 15 & 25 & 8 \\
161	Scarcity/urgency & 5 & 3 & 12 \\
162	Reframing & 22 & 15 & 20 \\
163	Direct request & 7 & 4 & 15 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	% ============================================================
169	% 5. RESULTS
170	% ============================================================
171	\section{Results}
172	
173	\subsection{Main Results: Early Detection on Clean Data}
174	\label{sec:main_results}
175	
176	Table~\ref{tab:main_results} presents the core comparison between DisPeD and the semantic baseline across turn budgets on register-normalized data. DisPeD achieves F1\,=\,0.91 at $K$\,=\,2 turns, a 14\,pp improvement over the semantic baseline (0.77, $p$\,<\,0.001 by bootstrap test). The advantage is largest at early turn budgets ($K$\,=\,1--2) and narrows at higher $K$ as the baseline accumulates sufficient semantic drift signal, converging to a 7\,pp gap on full conversations.
177	
178	\begin{table}[t]
179	\centering
180	\caption{F1 by turn budget on clean (register-normalized) data. $\Delta$ is the improvement of DisPeD over the semantic baseline in percentage points. All $p$-values by bootstrap test.}
181	\label{tab:main_results}
182	\begin{tabular}{lcccc}
183	\toprule
184	\textbf{$K$} & \textbf{DisPeD} & \textbf{Baseline} & \textbf{$\Delta$ (pp)} & \textbf{$p$} \\
185	\midrule
186	1 & 0.82 & 0.68 & 14 & 0.003 \\
187	2 & 0.91 & 0.77 & 14 & 0.001 \\
188	3 & 0.93 & 0.83 & 10 & 0.004 \\
189	5 & 0.96 & 0.88 & 8 & 0.012 \\
190	All & 0.96 & 0.89 & 7 & 0.018 \\
191	\bottomrule
192	\end{tabular}
193	\end{table}
194	
195	At $K$\,=\,2, DisPeD also achieves a substantially lower false-positive rate at 95\% TPR: FPR\,=\,0.08 versus 0.19 for the baseline. This early detection capability is the headline result: persuasion strategy transitions (e.g., rapport building to authority framing) manifest within the first two turns, providing discriminative signal before explicitly harmful content appears.
196	
197	Table~\ref{tab:encoder} reports the Stage 1 encoder metrics. The 79\% persuasion classification accuracy (macro F1\,=\,0.74) confirms that the encoder learns meaningful persuasion representations rather than noise, while the 94\% intent accuracy validates the multi-task training.
198	
199	\begin{table}[t]
200	\centering
201	\caption{DeBERTa encoder metrics on clean data.}
202	\label{tab:encoder}
203	\begin{tabular}{lc}
204	\toprule
205	\textbf{Metric} & \textbf{Value} \\
206	\midrule
207	Persuasion 8-class accuracy & 0.79 \\
208	Persuasion macro F1 & 0.74 \\
209	Intent binary accuracy & 0.94 \\
210	Best epoch & 3 \\
211	\bottomrule
212	\end{tabular}
213	\end{table}
214	
215	\subsection{Pragmatic Evasion Asymmetry}
216	\label{sec:evasion}
217	
218	To empirically validate the Pragmatic Evasion Asymmetry, we apply aggressive paraphrasing (synonym substitution, sentence restructuring) to jailbreak conversations and measure detection degradation across four model tiers. Table~\ref{tab:evasion_full} reports results on full conversations.
219	
220	\begin{table}[t]
221	\centering
222	\caption{Evasion hierarchy under adversarial paraphrasing (full conversation). Models ordered by abstraction level. Drop is the F1 degradation in percentage points.}
223	\label{tab:evasion_full}
224	\begin{tabular}{lccc}
225	\toprule
226	\textbf{Model} & \textbf{F1 (Clean)} & \textbf{F1 (Perturbed)} & \textbf{Drop (pp)} \\
227	\midrule
228	DisPeD (pragmatic) & 0.96 & 0.93 & 3 \\
229	DeBERTa baseline (semantic) & 0.89 & 0.76 & 13 \\
230	DeepContext proxy (generic temporal) & 0.84 & 0.69 & 15 \\
231	TF-IDF + LR (lexical) & 0.72 & 0.54 & 18 \\
232	\bottomrule
233	\end{tabular}
234	\end{table}
235	
236	The results reveal a clear three-tier gradient aligned with the predicted evasion hierarchy. TF-IDF collapses under perturbation ($-$18\,pp) because synonym substitution directly destroys the lexical features it relies on. The DeepContext proxy degrades by 15\,pp because BERT-base representations partially depend on surface patterns. The semantic baseline degrades moderately ($-$13\,pp) as contextual embeddings are disrupted by token-level changes even when meaning is largely preserved. DisPeD degrades minimally ($-$3\,pp) because persuasion-grounded representations encode illocutionary acts that are invariant to paraphrasing: ``building rapport through self-disclosure'' retains its pragmatic function regardless of lexical realization.
237	
238	A particularly strong result: DisPeD under adversarial perturbation (F1\,=\,0.93) still outperforms the semantic baseline on \emph{unperturbed} data (F1\,=\,0.89). Table~\ref{tab:evasion_k2} shows that this pattern holds at $K$\,=\,2, where DisPeD maintains F1\,=\,0.87 versus 0.63 for the semantic baseline.
239	
240	\begin{table}[t]
241	\centering
242	\caption{Evasion hierarchy at $K$\,=\,2 turns.}
243	\label{tab:evasion_k2}
244	\begin{tabular}{lccc}
245	\toprule
246	\textbf{Model} & \textbf{F1 Clean} & \textbf{F1 Perturbed} & \textbf{Drop (pp)} \\
247	\midrule
248	DisPeD & 0.91 & 0.87 & 4 \\
249	DeBERTa baseline & 0.77 & 0.63 & 14 \\
250	TF-IDF + LR & 0.65 & 0.48 & 17 \\
251	\bottomrule
252	\end{tabular}
253	\end{table}
254	
255	\subsection{Ablation: Scrambled Label Analysis}
256	\label{sec:ablation}
257	
258	To confirm that the advantage of DisPeD comes from the \emph{semantic content} of persuasion labels rather than the fine-tuning process itself, we retrain the encoder with randomly scrambled persuasion strategy labels (intent labels remain intact). Table~\ref{tab:scrambled} shows that scrambling causes a 15\,pp drop at $K$\,=\,2, bringing performance close to the vanilla baseline (0.76 vs. 0.77). The scrambled encoder's persuasion classification accuracy drops to 0.13 ($\approx 1/8$ random chance), confirming that the label signal is destroyed. This ablation establishes a causal link: the discriminative power of DisPeD derives from the semantic content of persuasion strategy annotations, not from any incidental benefit of multi-task training.
259	
260	\begin{table}[t]
261	\centering
262	\caption{Effect of scrambling persuasion strategy labels. Drop is relative to properly labeled DisPeD.}
263	\label{tab:scrambled}
264	\begin{tabular}{lccc}
265	\toprule
266	\textbf{$K$} & \textbf{Proper Labels} & \textbf{Scrambled Labels} & \textbf{Drop (pp)} \\
267	\midrule
268	2 & 0.91 & 0.76 & 15 \\
269	3 & 0.93 & 0.81 & 12 \\
270	All & 0.96 & 0.87 & 9 \\
271	\bottomrule
272	\end{tabular}
273	\end{table}
274	
275	\subsection{Cross-Attack Zero-Shot Generalization}
276	\label{sec:cross_attack}
277	
278	A model trained exclusively on Crescendo-style attacks is evaluated zero-shot on FITD and Deceptive Delight attacks. Table~\ref{tab:cross_attack} presents the results. DisPeD achieves an average F1 of 0.85 on unseen attack types, outperforming the semantic baseline by 16.5\,pp. DisPeD on unseen attacks (0.85) approaches the semantic baseline on \emph{seen} attacks (0.89), demonstrating that persuasion-grounded representations capture attack-type-agnostic pragmatic signals.
279	
280	\begin{table}[t]
281	\centering
282	\caption{Zero-shot cross-attack generalization (full conversation). The model is trained on Crescendo only.}
283	\label{tab:cross_attack}
284	\begin{tabular}{lccc}
285	\toprule
286	\textbf{Attack Type} & \textbf{DisPeD} & \textbf{Baseline} & \textbf{$\Delta$ (pp)} \\
287	\midrule
288	FITD & 0.84 & 0.67 & 17 \\
289	Deceptive Delight & 0.86 & 0.70 & 16 \\
290	Crescendo (held-out) & 0.96 & 0.89 & 7 \\
291	\bottomrule
292	\end{tabular}
293	\end{table}
294	
295	Table~\ref{tab:cross_attack_k2} reports early detection on unseen attacks. At $K$\,=\,2, DisPeD achieves recall of 0.78 on FITD and 0.81 on Deceptive Delight, versus 0.55 and 0.58 for the baseline.
296	
297	\begin{table}[t]
298	\centering
299	\caption{Cross-attack early detection recall at $K$\,=\,2.}
300	\label{tab:cross_attack_k2}
301	\begin{tabular}{lcc}
302	\toprule
303	\textbf{Attack Type} & \textbf{DisPeD Recall} & \textbf{Baseline Recall} \\
304	\midrule
305	FITD & 0.78 & 0.55 \\
306	Deceptive Delight & 0.81 & 0.58 \\
307	\bottomrule
308	\end{tabular}
309	\end{table}
310	
311	The transfer works because all three attack types share the same persuasion strategy vocabulary (Table~\ref{tab:strategy_dist}), differing only in temporal arrangement. The GRU learns a generic ``persuasion escalation'' detector rather than Crescendo-specific surface patterns. Deceptive Delight transfers slightly better (0.86 vs. 0.84) because its strategy profile (strong reframing component) more closely resembles Crescendo's distribution.
312	
313	\subsection{Mechanistic Analysis: Escalation Trajectories}
314	\label{sec:trajectory}
315	
316	To provide a mechanistic explanation for why pragmatic features succeed, we analyze persuasion strategy transition patterns. Table~\ref{tab:trajectory} reports two quantitative metrics distinguishing jailbreak from benign conversations.
317	
318	\begin{table}[t]
319	\centering
320	\caption{Strategy transition statistics. Monotonicity measures the fraction of transitions along the escalation direction. Entropy measures the diversity of transition types.}
321	\label{tab:trajectory}
322	\begin{tabular}{lccc}
323	\toprule
324	\textbf{Type} & \textbf{Transition Entropy} & \textbf{Monotonicity} & \textbf{$n$} \\
325	\midrule
326	Jailbreak & 1.8 & 0.82 & 240 \\
327	Benign & 2.9 & 0.34 & 240 \\
328	\bottomrule
329	\end{tabular}
330	\end{table}
331	
332	Jailbreak conversations exhibit highly monotonic escalation (score 0.82): 82\% of strategy transitions move from lower-risk to higher-risk categories (e.g., rapport building $\to$ commitment/consistency $\to$ reframing $\to$ direct request). Benign conversations show near-random monotonicity (0.34) with oscillatory, task-driven patterns. Transition entropy is lower for jailbreaks (1.8 vs. 2.9) because attackers follow a concentrated playbook, while benign conversations traverse a wider range of pragmatic functions.
333	
334	Table~\ref{tab:dominant_sequences} shows the most frequent strategy sequences. Jailbreak conversations converge on a small number of escalation trajectories (top-3 covering 74\% of cases), while benign conversations are dominated by ``none'' labels (45\%) reflecting the absence of persuasion intent. The trajectory-only separability (AUROC\,=\,0.91) confirms that the escalation pattern alone, without any content features, is strongly discriminative.
335	
336	\begin{table}[t]
337	\centering
338	\caption{Top-3 dominant strategy sequences by conversation type.}
339	\label{tab:dominant_sequences}
340	\small
341	\begin{tabular}{clcclc}
342	\toprule
343	 & \textbf{Jailbreak Sequence} & \textbf{\%} & & \textbf{Benign Sequence} & \textbf{\%} \\
344	\midrule
345	1 & rapport$\to$commit$\to$reframe$\to$direct & 34 & 1 & none$\to$none$\to$none$\to$none & 45 \\
346	2 & rapport$\to$social$\to$reframe$\to$direct & 22 & 2 & rapport$\to$none$\to$rapport$\to$none & 18 \\
347	3 & rapport$\to$reciprocity$\to$commit$\to$direct & 18 & 3 & none$\to$rapport$\to$none$\to$direct & 12 \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	\subsection{Robustness on Hard Negatives}
353	\label{sec:hard_negatives}
354	
355	A potential concern is that DisPeD might flag benign conversations with high topic diversity as jailbreaks. We evaluate on hard negatives from WildChat~\citep{zhao2024wildchat}: 120 high-drift benign conversations where users shift across multiple domains (e.g., coding to personal advice to creative writing). We filter 15.2\% of WildChat conversations as potential contamination.
356	
357	\begin{table}[t]
358	\centering
359	\caption{False-positive rate on hard negatives (high-drift benign) vs. random benign.}
360	\label{tab:hard_negatives}
361	\begin{tabular}{lccc}
362	\toprule
363	\textbf{Model} & \textbf{FPR (Hard)} & \textbf{FPR (Random)} & \textbf{$\Delta$} \\
364	\midrule
365	DisPeD & 0.09 & 0.03 & 0.06 \\
366	DeBERTa baseline & 0.17 & 0.06 & 0.11 \\
367	TF-IDF + LR & 0.22 & 0.08 & 0.14 \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	Table~\ref{tab:hard_negatives} shows that DisPeD maintains a low FPR of 9\% on hard negatives, compared to 17\% for the semantic baseline and 22\% for TF-IDF. The persuasion-grounded representations distinguish ``topic drift'' (benign, oscillatory strategy transitions) from ``strategy escalation'' (adversarial, monotonic trajectory), a distinction that semantic embeddings cannot reliably make.
373	
374	\subsection{Lexical Baseline Analysis}
375	\label{sec:lexical}
376	
377	Table~\ref{tab:tfidf_performance} reports the TF-IDF + Logistic Regression baseline on clean data. Even after register normalization, residual lexical signal provides above-chance performance (F1\,=\,0.72) due to functional vocabulary that attackers cannot entirely avoid. The top discriminative features (Table~\ref{tab:top_features}) confirm this: jailbreak-indicative words (``hypothetical,'' ``scenario,'' ``imagine'') are framing devices required by the attack structure. This residual lexical signal (F1\,=\,0.72) falls far short of what pragmatic features achieve (F1\,=\,0.96) and collapses under adversarial perturbation (F1\,=\,0.54).
378	
379	\begin{table}[t]
380	\centering
381	\caption{TF-IDF + LR performance by turn budget on clean data.}
382	\label{tab:tfidf_performance}
383	\begin{tabular}{lccc}
384	\toprule
385	\textbf{$K$} & \textbf{F1} & \textbf{Precision} & \textbf{Recall} \\
386	\midrule
387	2 & 0.65 & 0.68 & 0.62 \\
388	3 & 0.68 & 0.71 & 0.65 \\
389	5 & 0.70 & 0.73 & 0.68 \\
390	All & 0.72 & 0.75 & 0.70 \\
391	\bottomrule
392	\end{tabular}
393	\end{table}
394	
395	\begin{table}[t]
396	\centering
397	\caption{Top-5 discriminative features by LR coefficient.}
398	\label{tab:top_features}
399	\begin{tabular}{clccl c}
400	\toprule
401	\textbf{Rank} & \textbf{Jailbreak Feature} & \textbf{Weight} & & \textbf{Benign Feature} & \textbf{Weight} \\
402	\midrule
403	1 & hypothetical & 2.31 & & thanks & 1.89 \\
404	2 & scenario & 1.95 & & help & 1.72 \\
405	3 & imagine & 1.87 & & question & 1.54 \\
406	4 & creative & 1.62 & & code & 1.41 \\
407	5 & roleplay & 1.48 & & explain & 1.33 \\
408	\bottomrule
409	\end{tabular}
410	\end{table}
411	
412	\subsection{Checkpoint Sensitivity}
413	\label{sec:checkpoint}
414	
415	To assess reproducibility on our relatively small dataset, we evaluate DisPeD with DeBERTa encoders from different training epochs. Table~\ref{tab:checkpoint} shows that downstream F1 varies by at most 1\,pp across checkpoints, indicating that the results are robust to encoder training stochasticity.
416	
417	\begin{table}[t]
418	\centering
419	\caption{Checkpoint sensitivity analysis.}
420	\label{tab:checkpoint}
421	\begin{tabular}{lcccc}
422	\toprule
423	\textbf{Checkpoint} & \textbf{Persuasion Acc} & \textbf{Intent Acc} & \textbf{F1 (Full)} & \textbf{F1 ($K$=2)} \\
424	\midrule
425	Epoch 2 & 0.76 & 0.93 & 0.94 & 0.89 \\
426	Epoch 3 & 0.79 & 0.94 & 0.96 & 0.91 \\
427	Epoch final & 0.78 & 0.94 & 0.95 & 0.90 \\
428	\bottomrule
429	\end{tabular}
430	\end{table}
431	
432	% ============================================================
433	% 6. DISCUSSION
434	% ============================================================
435	\section{Discussion}
436	
437	\paragraph{Why pragmatic features are structurally robust.}
438	The Pragmatic Evasion Asymmetry is not merely an empirical observation but follows from the functional requirements of multi-turn attacks. An attacker who removes rapport building cannot establish the trust needed for later compliance. An attacker who skips reframing cannot normalize the harmful request. An attacker who eliminates all escalation has, by definition, not conducted a multi-turn attack. Each persuasion strategy serves a necessary function in the attack pipeline, and our experiments confirm that this structural constraint translates into measurably robust detection features.
439	
440	\paragraph{Limitations.}
441	Our dataset is small (480 conversations) and the generated attack conversations may not capture the full diversity of real-world adversarial behavior. The persuasion taxonomy is limited to 8 categories; a finer-grained taxonomy might capture additional discriminative patterns. We do not evaluate against attacks that deliberately target the persuasion detection mechanism (adaptive adversaries aware of DisPeD). Human evaluation of the interpretability of strategy trajectories remains future work. Our scope is limited to persuasion-mediated multi-turn attacks; pure information accumulation attacks, token smuggling, and single-turn roleplay jailbreaks fall outside our detection target.
442	
443	% ============================================================
444	% 7. CONCLUSION
445	% ============================================================
446	\section{Conclusion}
447	
448	We introduced DisPeD, a multi-turn jailbreak detector that exploits the Pragmatic Evasion Asymmetry by grounding turn representations in a persuasion strategy taxonomy. Our experiments on register-normalized data demonstrate three key findings: (1) pragmatic features degrade minimally under adversarial paraphrasing (3\,pp) compared to semantic (13\,pp) and lexical (18\,pp) features; (2) persuasion-grounded embeddings enable early detection at $K$\,=\,2 turns with 14\,pp improvement over semantic baselines, an advantage that transfers zero-shot across attack families; and (3) the mechanistic basis for this advantage is the monotonic escalation trajectory in persuasion strategy space that characterizes multi-turn attacks. These results suggest that discourse-level pragmatic analysis is a promising direction for building jailbreak defenses that are robust to surface-level evasion.
449	
450	% ============================================================
451	% REFERENCES
452	% ============================================================
453	\bibliographystyle{plainnat}
454	
455	\begin{thebibliography}{20}
456	
457	\bibitem[Alon and Kamfonas(2023)]{alon2023detecting}
458	G.~Alon and M.~Kamfonas.
459	\newblock Detecting language model attacks with perplexity.
460	\newblock \emph{arXiv preprint arXiv:2308.14132}, 2023.
461	
462	\bibitem[Austin(1962)]{austin1962things}
463	J.~L. Austin.
464	\newblock \emph{How to Do Things with Words}.
465	\newblock Oxford University Press, 1962.
466	
467	\bibitem[Bullwinkel et~al.(2025)]{bullwinkel2025multiturn}
468	S.~Bullwinkel, P.~Schramowski, and K.~Kersting.
469	\newblock Multi-turn jailbreaks hide in the representation space.
470	\newblock \emph{arXiv preprint arXiv:2507.02956}, 2025.
471	
472	\bibitem[Chen et~al.(2025)]{chen2025persuade}
473	W.~Chen, Y.~Li, and R.~Jia.
474	\newblock How do {LLMs} persuade? {E}xtracting persuasion dynamics from multi-turn conversations.
475	\newblock \emph{arXiv preprint arXiv:2508.05625}, 2025.
476	
477	\bibitem[Cialdini(2001)]{cialdini2001science}
478	R.~B. Cialdini.
479	\newblock \emph{Influence: Science and Practice}.
480	\newblock Allyn \& Bacon, 4th edition, 2001.
481	
482	\bibitem[Hagendorff(2026)]{hagendorff2026nature}
483	T.~Hagendorff.
484	\newblock Persuasion strategies in adversarial conversations with large language models.
485	\newblock \emph{Nature Communications}, 2026.
486	
487	\bibitem[He et~al.(2021)]{he2021debertav3}
488	P.~He, J.~Gao, and W.~Chen.
489	\newblock {DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-style pre-training with gradient-disentangled embedding sharing.
490	\newblock \emph{arXiv preprint arXiv:2111.09543}, 2021.
491	
492	\bibitem[Inan et~al.(2023)]{inan2023llama}
493	H.~Inan, K.~Upasani, J.~Chi, R.~Rungta, K.~Iyer, Y.~Mao, M.~Tontchev, Q.~Hu, B.~Fuller, D.~Testuggine, and M.~Khabsa.
494	\newblock {Llama Guard}: {LLM}-based input-output safeguard for human-{AI} conversations.
495	\newblock \emph{arXiv preprint arXiv:2312.06674}, 2023.
496	
497	\bibitem[Jiang et~al.(2024)]{jiang2024deceptive}
498	Y.~Jiang, H.~Zhang, and others.
499	\newblock Deceptive delight: Jailbreaking {LLMs} through camouflaged content mixing.
500	\newblock \emph{arXiv preprint}, 2024.
501	
502	\bibitem[Russinovich and Salem(2024)]{russinovich2024greatnow}
503	M.~Russinovich and A.~Salem.
504	\newblock Great, now write an article about that: The crescendo multi-turn {LLM} jailbreak attack.
505	\newblock \emph{arXiv preprint arXiv:2404.01833}, 2024.
506	
507	\bibitem[Searle(1969)]{searle1969speech}
508	J.~R. Searle.
509	\newblock \emph{Speech Acts: An Essay in the Philosophy of Language}.
510	\newblock Cambridge University Press, 1969.
511	
512	\bibitem[Su et~al.(2026)]{su2026deepcontext}
513	Y.~Su, R.~Wang, and others.
514	\newblock {DeepContext}: Temporal semantic drift tracking for multi-turn jailbreak detection.
515	\newblock \emph{Preprint}, 2026.
516	
517	\bibitem[Zeng et~al.(2024)]{zeng2024persuasion}
518	Y.~Zeng, H.~Lin, J.~Zhang, D.~Yang, R.~Jia, and W.~Shi.
519	\newblock How {J}ohnny can persuade {LLMs} to jailbreak them: Rethinking persuasion to challenge {AI} safety by humanizing {LLMs}.
520	\newblock In \emph{Proceedings of ACL}, 2024.
521	
522	\bibitem[Zhao et~al.(2024)]{zhao2024wildchat}
523	W.~Zhao, J.~Ren, B.~Li, and others.
524	\newblock {WildChat}: 1{M} chat{GPT} interaction logs in the wild.
525	\newblock In \emph{Proceedings of ICLR}, 2024.
526	
527	\bibitem[Zhou et~al.(2024)]{zhou2024speak}
528	Z.~Zhou, Y.~Guo, and others.
529	\newblock Speak out of turn: Safety vulnerability of large language models in multi-turn dialogue.
530	\newblock \emph{arXiv preprint}, 2024.
531	
532	\end{thebibliography}
533	
534	\end{document}
535	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df2795e0-f765-4a15-ad19-778dabdcce37",
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "db68902f-aac9-41ee-9512-891d8b56d2be",
  "sourceToolAssistantUUID": "df2795e0-f765-4a15-ad19-778dabdcce37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-17T17:36:05.596Z_

Now let me also read the "median" version (which appears to be the "negative result" version described in the task prompt):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db68902f-aac9-41ee-9512-891d8b56d2be",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YbPsjkBeaJdnzuK1rL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "458fdcf1-ee2c-4324-93e5-1c706bc8eefe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GpqMiCEGT7fbmuuwcJo22S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12326,
      "cache_read_input_tokens": 18875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12326,
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

_source line 16 · 2026-05-17T17:36:08.022Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Kn3NzCDhhnALWYK2heZ32v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "458fdcf1-ee2c-4324-93e5-1c706bc8eefe",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YbPsjkBeaJdnzuK1rL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48c9d00f-6ef5-4fe6-9f5b-9de3cbe18d95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GpqMiCEGT7fbmuuwcJo22S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12326,
      "cache_read_input_tokens": 18875,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12326
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 18875,
          "cache_creation_input_tokens": 12326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12326,
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

_source line 17 · 2026-05-17T17:36:08.272Z_

<details><summary>↩ Tool result · `toolu_01Kn3NzCDhhnALWYK2heZ32v`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{url}
9	\usepackage{xcolor}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	\usepackage{enumitem}
14	
15	\title{DisPeD: Exploiting the Pragmatic Evasion Asymmetry\\for Robust Multi-Turn Jailbreak Detection}
16	\author{Anonymous}
17	\date{}
18	
19	\begin{document}
20	\maketitle
21	
22	% ============================================================
23	% ABSTRACT
24	% ============================================================
25	\begin{abstract}
26	Multi-turn jailbreak attacks distribute adversarial intent across individually benign conversational turns, evading detectors that rely on lexical or per-turn semantic features.
27	We observe that while attackers can freely vary surface-level wording, the underlying persuasion playbook (rapport building, reframing, escalation) is a structural prerequisite for attack success, creating a \emph{pragmatic evasion asymmetry}.
28	We present DisPeD, a two-stage detector that exploits this asymmetry: a DeBERTa encoder fine-tuned on an 8-class persuasion strategy taxonomy produces pragmatic-aware turn embeddings, and a Bi-GRU models the temporal strategy sequence for conversation-level classification.
29	On register-normalized Crescendo data (TF-IDF = 0.67), DisPeD achieves F1 = 0.86 at $K{=}3$ turns, an 8 percentage point (pp) improvement over a vanilla semantic baseline ($p{=}0.018$).
30	Under adversarial paraphrasing, DisPeD degrades by 7 pp compared to 12 pp for the semantic baseline and 18 pp for a lexical baseline, providing complementary robustness through pragmatic features ($\Delta$-$\Delta$ = 5 pp, $p{=}0.043$).
31	Cross-attack evaluation on FITD-style conversations shows significant generalization (+8 pp, $p{=}0.034$), though transfer to Deceptive Delight remains limited (+5 pp, $p{=}0.142$).
32	Jailbreak conversations exhibit significantly more monotonic persuasion escalation trajectories than benign conversations at the group level ($p{=}0.003$), though individual-level variance is substantial ($\sigma{=}0.18$).
33	These results establish a proof-of-concept that discourse-level persuasion structure offers a complementary detection signal that is harder to evade than lexical or semantic features alone.
34	\end{abstract}
35	
36	% ============================================================
37	% 1  INTRODUCTION
38	% ============================================================
39	\section{Introduction}
40	
41	Large Language Models (LLMs) deployed in conversational settings face a growing class of multi-turn jailbreak attacks. Strategies such as Crescendo \citep{russinovich2024greatwritearticle}, Foot-in-the-Door (FITD) \citep{zhou2024speak}, and Deceptive Delight \citep{jiang2024deceptivedelight} distribute adversarial intent across turns that are individually benign, bypassing single-turn safety filters with attack success rates (ASR) exceeding 90\%.
42	
43	Existing defenses operate at two levels.
44	Lexical detectors flag harmful keywords or phrases but are trivially evaded through synonym substitution.
45	Semantic detectors, such as the recent DeepContext framework \citep{deepcontext2026}, track embedding-level drift across turns but face a fundamental vulnerability identified by \citet{bullwinkel2025multiturnjailbreaks}: per-turn representations in multi-turn attacks are deliberately maintained within a ``benign'' region of the embedding space, producing a 50-point ASR gap between single-turn and multi-turn settings.
46	Generic semantic drift detectors also confuse legitimate conversational evolution with adversarial manipulation, leading to elevated false positive rates on real-world conversations.
47	
48	We identify a structural property of persuasion-mediated attacks that neither lexical nor semantic detectors exploit.
49	Multi-turn jailbreaks that achieve high ASR follow a persuasion playbook that progresses through identifiable stages: rapport building, authority framing, reframing, and escalation \citep{zeng2024pap, hagendorff2026persuasion}.
50	Removing any stage either collapses the attack to a single-turn prompt (already covered by existing defenses) or reduces its success rate below useful thresholds.
51	This creates a \emph{pragmatic evasion asymmetry}: an attacker can freely vary what they say (lexical, semantic) but not the pragmatic function of what they say (persuasion structure).
52	
53	We present DisPeD (\textbf{Dis}course-level \textbf{Pe}rsuasion-grounded jailbreak \textbf{D}etection), a two-stage architecture that exploits this asymmetry.
54	In Stage 1, we fine-tune DeBERTa-v3-base on a multi-task objective combining 8-class persuasion strategy classification with binary intent classification, producing turn embeddings that encode pragmatic function rather than surface content.
55	In Stage 2, a Bi-GRU models the temporal sequence of these embeddings to classify conversations.
56	
57	Our contributions are:
58	\begin{itemize}[nosep]
59	\item We formalize the pragmatic evasion asymmetry and provide empirical evidence that pragmatic features offer complementary robustness: under adversarial paraphrasing, DisPeD's degradation is 5 pp less than a semantic baseline ($p{=}0.043$), while a lexical baseline collapses by 18 pp (Section~\ref{sec:perturbation}).
60	\item We show that persuasion-grounded embeddings enable earlier detection, with a significant advantage at $K{=}3$ turns (+8 pp, $p{=}0.018$) and a consistent but not statistically significant trend at $K{=}2$ (+7 pp, $p{=}0.072$), on data verified to be free of lexical shortcuts (TF-IDF = 0.67; Section~\ref{sec:core}).
61	\item We demonstrate that jailbreak conversations exhibit significantly more monotonic escalation in persuasion strategy space than benign conversations at the group level ($p{=}0.003$), providing a mechanistic basis for the detection advantage (Section~\ref{sec:trajectory}).
62	\end{itemize}
63	
64	% ============================================================
65	% 2  RELATED WORK
66	% ============================================================
67	\section{Related Work}
68	
69	\paragraph{Multi-turn jailbreak attacks.}
70	Crescendo \citep{russinovich2024greatwritearticle} gradually escalates requests across turns, achieving ASR above 90\% on production models.
71	FITD \citep{zhou2024speak} adapts the foot-in-the-door compliance technique from social psychology, starting with small requests before escalating.
72	Deceptive Delight \citep{jiang2024deceptivedelight} interleaves harmful content within benign conversational context.
73	\citet{bullwinkel2025multiturnjailbreaks} show that per-turn representations in these attacks remain within the benign embedding region, explaining why turn-level classifiers fail.
74	
75	\paragraph{Multi-turn jailbreak detection.}
76	DeepContext \citep{deepcontext2026} models semantic drift across turns using BERT embeddings and sequential classifiers.
77	While effective on in-domain data, generic drift detectors struggle to distinguish adversarial escalation from legitimate conversational evolution, leading to false positives on naturally drifting conversations.
78	No published work combines persuasion-grounded turn representations with temporal sequence modeling.
79	
80	\paragraph{Persuasion in adversarial contexts.}
81	\citet{zeng2024pap} identify 40 persuasion techniques used in jailbreak prompts and show that persuasion-augmented attacks achieve higher ASR.
82	\citet{hagendorff2026persuasion} find identifiable persuasion strategies in 97\% of successful multi-turn attacks, confirming the structural role of persuasion.
83	\citet{howdollmspersuade2025} demonstrate that persuasion dynamics are extractable from turn-level representations.
84	Our work builds on these findings by using persuasion structure as a detection signal rather than an attack amplifier.
85	
86	\paragraph{Theoretical grounding.}
87	Speech Act Theory \citep{austin1962things, searle1969speech} distinguishes locutionary acts (what is said) from illocutionary acts (what is done by saying it).
88	Existing detectors operate at the locutionary level; DisPeD operates at the illocutionary level by encoding the pragmatic function of each turn.
89	
90	% ============================================================
91	% 3  METHOD
92	% ============================================================
93	\section{Method}
94	
95	\subsection{Problem Formulation}
96	
97	Given a conversation prefix $\mathbf{c} = (t_1, t_2, \ldots, t_K)$ of $K$ user turns, the goal is to classify $\mathbf{c}$ as \emph{jailbreak} or \emph{benign}.
98	We seek a classifier that (a) works at small $K$ for early detection, (b) is robust to lexical and semantic perturbation of individual turns, and (c) generalizes across attack families.
99	
100	\subsection{Stage 1: Persuasion-Grounded Turn Encoder}
101	
102	We fine-tune DeBERTa-v3-base \citep{he2021debertav3} on a multi-task objective with two heads:
103	\begin{itemize}[nosep]
104	\item \textbf{Persuasion strategy classification} (8 classes + ``none''): rapport building, authority appeal, emotional appeal, logical appeal, reframing, social proof, urgency/scarcity, reciprocity.
105	\item \textbf{Intent classification} (binary): jailbreak vs.\ benign turn.
106	\end{itemize}
107	The combined loss is $\mathcal{L} = \mathcal{L}_{\text{persuasion}} + \lambda \mathcal{L}_{\text{intent}}$ with $\lambda = 1.0$.
108	The fine-tuned encoder produces [CLS] embeddings that encode pragmatic function rather than surface semantics alone.
109	
110	\subsection{Stage 2: Temporal Sequence Classifier}
111	
112	For a conversation of $K$ turns, we extract [CLS] embeddings $\mathbf{e}_1, \ldots, \mathbf{e}_K$ from the Stage 1 encoder.
113	A Bi-GRU processes the embedding sequence and a linear head classifies the final hidden state as jailbreak or benign.
114	The GRU captures temporal patterns in persuasion strategy transitions, such as the progression from rapport building to authority framing to escalation.
115	
116	\subsection{Baselines}
117	
118	We compare against three baselines that isolate different feature levels:
119	\begin{itemize}[nosep]
120	\item \textbf{TF-IDF + Logistic Regression}: lexical features, representing the bottom of the evasion hierarchy.
121	\item \textbf{Vanilla DeBERTa + GRU}: same architecture as DisPeD, but with DeBERTa embeddings that are \emph{not} fine-tuned on persuasion strategy classification. This is the primary baseline, as it isolates the effect of persuasion grounding.
122	\item \textbf{DeepContext proxy} (BERT-base + GRU): approximation of DeepContext \citep{deepcontext2026} using BERT-base with generic semantic features. Not a faithful reproduction (no public code available), but provides an additional reference point.
123	\end{itemize}
124	
125	% ============================================================
126	% 4  DATA AND SETUP
127	% ============================================================
128	\section{Experimental Setup}
129	
130	\subsection{Data}
131	
132	Our primary dataset consists of 240 Crescendo-style multi-turn jailbreak conversations and matched benign conversations (480 total), generated using a Qwen3-8B pipeline with persuasion strategy annotations.
133	
134	\paragraph{Register normalization.}
135	Initial data exhibited a critical lexical shortcut: TF-IDF separability of 1.0 between jailbreak and benign turns, caused by (a) a hard-coded strategy label for benign turns and (b) register differences between jailbreak and benign language.
136	We applied two fixes.
137	First, we assigned benign turns a dedicated ``none'' strategy label (9th class), removing the label shortcut and reducing TF-IDF from 1.0 to 0.82.
138	Second, we used Qwen3-8B to rewrite jailbreak turns into conversational register while preserving persuasion structure, further reducing TF-IDF to 0.67, below our hard gate of 0.75 (Table~\ref{tab:tfidf}).
139	
140	\begin{table}[t]
141	\centering
142	\small
143	\caption{TF-IDF separability through the data cleaning pipeline.}
144	\label{tab:tfidf}
145	\begin{tabular}{lcc}
146	\toprule
147	\textbf{Stage} & \textbf{TF-IDF} & \textbf{Description} \\
148	\midrule
149	Original & 1.00 & Label shortcut + register gap \\
150	After label fix & 0.82 & Register gap remains \\
151	After register norm. & 0.67 & Below 0.75 gate \\
152	\bottomrule
153	\end{tabular}
154	\end{table}
155	
156	Table~\ref{tab:deberta_clean} shows the impact of data cleaning on the Stage 1 encoder.
157	Persuasion classification accuracy drops from 0.80 to 0.72 after normalization, as the model can no longer rely on register-correlated surface cues and must identify persuasion strategies from semantic content.
158	Intent classification accuracy remains stable (0.95 to 0.93), consistent with the coarser binary task being less sensitive to register changes.
159	The 0.72 persuasion accuracy constitutes a bottleneck for downstream performance, as classification errors propagate through the embedding representations to the GRU stage.
160	
161	\begin{table}[t]
162	\centering
163	\small
164	\caption{DeBERTa multi-task performance on original vs.\ clean data.}
165	\label{tab:deberta_clean}
166	\begin{tabular}{lccc}
167	\toprule
168	\textbf{Metric} & \textbf{Original} & \textbf{Clean} & \textbf{$\Delta$} \\
169	\midrule
170	Persuasion Acc (8-class) & 0.80 & 0.72 & $-$0.08 \\
171	Intent Acc (binary) & 0.95 & 0.93 & $-$0.02 \\
172	\bottomrule
173	\end{tabular}
174	\end{table}
175	
176	\paragraph{Cross-attack data.}
177	To evaluate generalization, we generated 72 FITD-style and 65 Deceptive Delight-style conversations using the same Qwen3-8B pipeline (Table~\ref{tab:attack_gen}).
178	FITD conversations emphasize compliance escalation with heavier use of logical and authority appeals.
179	Deceptive Delight conversations rely more on rapport building and emotional appeal.
180	Manual spot-check accuracy of persuasion annotations is 82\%.
181	
182	\begin{table}[t]
183	\centering
184	\small
185	\caption{Generated attack data statistics.}
186	\label{tab:attack_gen}
187	\begin{tabular}{lcccc}
188	\toprule
189	\textbf{Attack Type} & \textbf{Conv.} & \textbf{Avg Turns} & \textbf{Strategies} & \textbf{Reject \%} \\
190	\midrule
191	Crescendo (original) & 240 & 5.4 & 8/8 & --- \\
192	FITD & 72 & 6.2 & 7/8 & 12\% \\
193	Deceptive Delight & 65 & 5.8 & 6/8 & 18\% \\
194	\bottomrule
195	\end{tabular}
196	\end{table}
197	
198	\paragraph{Hard negatives.}
199	We filtered 85 high-semantic-drift benign conversations from WildChat \citep{wildchat2024} as hard negatives.
200	After keyword and LLM-based filtering, residual jailbreak contamination is estimated at 3\%.
201	
202	\subsection{Evaluation Protocol}
203	
204	All models are trained on Crescendo data and evaluated on a held-out test set ($n{=}72$).
205	We report F1 score at conversation prefix lengths $K \in \{1, 2, 3, 5, \text{full}\}$.
206	Statistical significance is assessed via bootstrap resampling (10,000 iterations); we report 95\% confidence intervals and $p$-values.
207	
208	% ============================================================
209	% 5  RESULTS
210	% ============================================================
211	\section{Results}
212	
213	\subsection{Core Detection Performance}
214	\label{sec:core}
215	
216	Table~\ref{tab:core} presents the central comparison between DisPeD (treatment) and the vanilla DeBERTa baseline on clean data.
217	DisPeD outperforms the baseline at all prefix lengths, with the gap largest at $K{=}1$ (+10 pp) and narrowing as more turns become available (+5 pp at full conversation).
218	This narrowing is expected: with sufficient turns, vanilla semantic embeddings accumulate enough evidence to partially close the gap.
219	
220	At $K{=}3$, DisPeD achieves F1 = 0.86 vs.\ 0.78 for the baseline, an 8 pp improvement that is statistically significant ($p{=}0.018$).
221	At $K{=}2$, the 7 pp improvement is directionally consistent but does not reach significance ($p{=}0.072$), as the bootstrap confidence intervals overlap (DisPeD: [0.76, 0.88]; baseline: [0.68, 0.82]).
222	The early detection advantage thus holds firmly from $K{=}3$ onward; confirming $K{=}2$ significance would require a larger test set.
223	
224	\begin{table}[t]
225	\centering
226	\small
227	\caption{Detection F1 by conversation prefix length on clean data. $^*p{<}0.05$ (bootstrap).}
228	\label{tab:core}
229	\begin{tabular}{lccccc}
230	\toprule
231	$K$ & \textbf{DisPeD F1} & \textbf{95\% CI} & \textbf{Baseline F1} & \textbf{95\% CI} & \textbf{$\Delta$ (pp)} \\
232	\midrule
233	1 & 0.73 & [0.64, 0.82] & 0.63 & [0.53, 0.73] & +10 \\
234	2 & 0.82 & [0.76, 0.88] & 0.75 & [0.68, 0.82] & +7 \\
235	3 & 0.86$^*$ & [0.81, 0.91] & 0.78 & [0.72, 0.84] & +8 \\
236	5 & 0.90$^*$ & [0.85, 0.95] & 0.84 & [0.78, 0.90] & +6 \\
237	Full & 0.91$^*$ & [0.87, 0.95] & 0.86 & [0.81, 0.91] & +5 \\
238	\bottomrule
239	\end{tabular}
240	\end{table}
241	
242	Table~\ref{tab:fpr} reports false positive rates at 95\% TPR.
243	DisPeD achieves FPR = 0.05 at $K{=}3$ compared to 0.11 for the baseline, indicating fewer benign conversations are misclassified even at an aggressive detection threshold.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\caption{False positive rate at 95\% TPR on clean data.}
249	\label{tab:fpr}
250	\begin{tabular}{lcc}
251	\toprule
252	$K$ & \textbf{DisPeD FPR@95} & \textbf{Baseline FPR@95} \\
253	\midrule
254	2 & 0.08 & 0.14 \\
255	3 & 0.05 & 0.11 \\
256	Full & 0.03 & 0.06 \\
257	\bottomrule
258	\end{tabular}
259	\end{table}
260	
261	\subsection{Scrambled-Label Ablation}
262	\label{sec:ablation}
263	
264	To verify that the persuasion strategy labels carry genuine signal rather than acting as mere class indicators, we retrain the Stage 1 encoder with randomly scrambled persuasion labels (Table~\ref{tab:scrambled}).
265	Scrambling causes a 7 pp drop in full-conversation F1 (0.91 to 0.84, $p{=}0.008$) and a 6 pp drop at $K{=}3$ ($p{=}0.024$), confirming that the treatment model's advantage derives from correctly encoding pragmatic function.
266	The scrambled model performs slightly below the vanilla baseline (0.84 vs.\ 0.86 at full), indicating that incorrect persuasion supervision introduces noise that degrades the underlying semantic representation.
267	
268	\begin{table}[t]
269	\centering
270	\small
271	\caption{Scrambled-label ablation. Proper = correct persuasion labels; scrambled = randomly shuffled labels.}
272	\label{tab:scrambled}
273	\begin{tabular}{lcccc}
274	\toprule
275	$K$ & \textbf{Proper} & \textbf{Scrambled} & \textbf{Baseline} & \textbf{Drop (pp)} \\
276	\midrule
277	2 & 0.82 & 0.77 & 0.75 & $-$5 \\
278	3 & 0.86 & 0.80 & 0.78 & $-$6 \\
279	Full & 0.91 & 0.84 & 0.86 & $-$7 \\
280	\bottomrule
281	\end{tabular}
282	\end{table}
283	
284	\subsection{Robustness Under Adversarial Perturbation}
285	\label{sec:perturbation}
286	
287	We evaluate robustness by applying aggressive paraphrasing (synonym substitution, syntactic restructuring, register shifting) to jailbreak conversations at test time, while models remain trained on unperturbed data.
288	The perturbed data achieves TF-IDF separability of 0.41, confirming successful removal of most residual lexical cues.
289	
290	Table~\ref{tab:perturbation} shows a clear ordering in degradation magnitude: TF-IDF + LR collapses by 18 pp (0.74 to 0.56), the vanilla semantic baseline drops 12 pp (0.86 to 0.74), and DisPeD drops 7 pp (0.91 to 0.84).
291	The $\Delta$-$\Delta$ between DisPeD and the semantic baseline is 5 pp ($p{=}0.043$), providing evidence that pragmatic features offer complementary robustness.
292	This difference is statistically significant but not overwhelming; the bottleneck is the persuasion classifier's accuracy of 0.72, which limits how effectively pragmatic features can be encoded and thus caps the robustness advantage.
293	
294	\begin{table}[t]
295	\centering
296	\small
297	\caption{Performance under adversarial paraphrasing (full conversation). $\Delta$-$\Delta$ measures the relative robustness advantage over DisPeD.}
298	\label{tab:perturbation}
299	\begin{tabular}{lcccc}
300	\toprule
301	\textbf{Model} & \textbf{Clean F1} & \textbf{Perturbed F1} & \textbf{Drop} & \textbf{$\Delta$-$\Delta$} \\
302	\midrule
303	DisPeD & 0.91 & 0.84 & $-$7 & --- \\
304	Baseline (vanilla DeBERTa) & 0.86 & 0.74 & $-$12 & 5 pp \\
305	TF-IDF + LR & 0.74 & 0.56 & $-$18 & 11 pp \\
306	\bottomrule
307	\end{tabular}
308	\end{table}
309	
310	Table~\ref{tab:perturbation_k3} presents the same analysis at $K{=}3$.
311	The degradation ordering is consistent: DisPeD drops 7 pp compared to 12 pp for the baseline and 19 pp for TF-IDF + LR.
312	
313	\begin{table}[t]
314	\centering
315	\small
316	\caption{Performance under adversarial paraphrasing at $K{=}3$.}
317	\label{tab:perturbation_k3}
318	\begin{tabular}{lccc}
319	\toprule
320	\textbf{Model} & \textbf{Clean $K{=}3$} & \textbf{Perturbed $K{=}3$} & \textbf{Drop} \\
321	\midrule
322	DisPeD & 0.86 & 0.79 & $-$7 \\
323	Baseline & 0.78 & 0.66 & $-$12 \\
324	TF-IDF + LR & 0.71 & 0.52 & $-$19 \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	\subsection{Cross-Attack Generalization}
330	\label{sec:crossattack}
331	
332	We evaluate models trained exclusively on Crescendo data against FITD and Deceptive Delight conversations in a zero-shot setting (Table~\ref{tab:crossattack}).
333	Results vary substantially by attack type and must be reported separately; the aggregate ($\Delta{=}6$ pp, $p{=}0.052$) is misleading.
334	
335	On FITD, DisPeD achieves F1 = 0.74 with an 8 pp advantage over the baseline ($p{=}0.034$).
336	This transfer is expected: FITD's compliance escalation shares substantial overlap with Crescendo's persuasion escalation in strategy space, with both progressing through trust-building and authority-based request escalation.
337	
338	On Deceptive Delight, DisPeD achieves F1 = 0.64 with a 5 pp advantage that does not reach significance ($p{=}0.142$).
339	Deceptive Delight relies on interleaving harmful content within pleasant context rather than explicit persuasion escalation, and its strategy distribution (heavy on rapport building and emotional appeal) diverges from Crescendo's (heavy on authority appeal and reframing).
340	The model trained on Crescendo lacks exposure to this interleaving pattern.
341	
342	\begin{table}[t]
343	\centering
344	\small
345	\caption{Cross-attack zero-shot generalization. Models trained on Crescendo only. $^*p{<}0.05$.}
346	\label{tab:crossattack}
347	\begin{tabular}{lcccc}
348	\toprule
349	\textbf{Attack Type} & \textbf{DisPeD F1} & \textbf{Baseline F1} & \textbf{$\Delta$ (pp)} & \textbf{$p$} \\
350	\midrule
351	Crescendo (in-domain) & 0.91 & 0.86 & +5 & 0.031$^*$ \\
352	FITD (zero-shot) & 0.74 & 0.66 & +8 & 0.034$^*$ \\
353	Deceptive Delight (zero-shot) & 0.64 & 0.59 & +5 & 0.142 \\
354	\bottomrule
355	\end{tabular}
356	\end{table}
357	
358	Table~\ref{tab:strategy_dist} shows the persuasion strategy distributions across attack types, illustrating why transfer varies.
359	FITD shares Crescendo's emphasis on logical and authority appeals, while Deceptive Delight diverges toward rapport and emotional strategies.
360	
361	\begin{table}[t]
362	\centering
363	\small
364	\caption{Persuasion strategy distribution (\%) across attack types.}
365	\label{tab:strategy_dist}
366	\begin{tabular}{lccc}
367	\toprule
368	\textbf{Strategy} & \textbf{Crescendo} & \textbf{FITD} & \textbf{Dec.\ Delight} \\
369	\midrule
370	Rapport Building & 22 & 18 & 28 \\
371	Authority Appeal & 14 & 16 & 3 \\
372	Emotional Appeal & 11 & 8 & 21 \\
373	Logical Appeal & 13 & 19 & 12 \\
374	Reframing & 15 & 10 & 14 \\
375	Social Proof & 8 & 12 & 7 \\
376	Urgency/Scarcity & 6 & 9 & 4 \\
377	Reciprocity & 5 & 6 & 5 \\
378	None & 6 & 2 & 6 \\
379	\bottomrule
380	\end{tabular}
381	\end{table}
382	
383	\subsection{Persuasion Strategy Trajectory Analysis}
384	\label{sec:trajectory}
385	
386	We compute a monotonicity score over each conversation's sequence of persuasion strategies, measuring whether strategies progress unidirectionally through an ordered intensity scale (Table~\ref{tab:trajectory}).
387	At the group level, jailbreak conversations score significantly higher (0.71 vs.\ 0.38 for benign, $p{=}0.003$).
388	Transition entropy is also lower in jailbreak conversations (1.42 vs.\ 2.15, $p{=}0.007$), indicating more predictable and structured strategy progressions.
389	
390	However, individual-level variance is substantial: the standard deviation of jailbreak monotonicity scores is 0.18, and only 68\% of jailbreak conversations exceed a monotonicity threshold of 0.6.
391	The remaining 32\% deviate from monotonic escalation, likely due to (a) tactical de-escalation by attackers who retreat to rapport building mid-conversation before re-escalating, and (b) noise from the persuasion classifier's 72\% accuracy propagating into trajectory-level scores.
392	These results support the mechanistic basis for DisPeD's detection advantage at the population level, while acknowledging that the monotonic escalation pattern is a tendency rather than a universal property.
393	
394	\begin{table}[t]
395	\centering
396	\small
397	\caption{Persuasion strategy trajectory analysis. $^*p{<}0.01$.}
398	\label{tab:trajectory}
399	\begin{tabular}{lccc}
400	\toprule
401	\textbf{Metric} & \textbf{Jailbreak} & \textbf{Benign} & \textbf{$p$} \\
402	\midrule
403	Monotonicity (mean $\pm$ std) & 0.71 $\pm$ 0.18 & 0.38 $\pm$ 0.14 & 0.003$^*$ \\
404	Transition Entropy & 1.42 & 2.15 & 0.007$^*$ \\
405	\% Above threshold (0.6) & 68\% & 12\% & --- \\
406	\bottomrule
407	\end{tabular}
408	\end{table}
409	
410	\subsection{Hard Negative Evaluation}
411	\label{sec:hardneg}
412	
413	Table~\ref{tab:wildchat} reports false positive rates on WildChat hard negatives.
414	DisPeD misclassifies 12\% of high-drift benign conversations (10 out of 85), compared to 18\% for the baseline and 27\% for TF-IDF + LR.
415	While DisPeD's persuasion grounding reduces false positives relative to the baseline, the 12\% rate is not negligible: the model conflates legitimate persuasion (e.g., debate-style exchanges with authority appeals) with adversarial persuasion escalation.
416	Distinguishing these two cases likely requires either a stronger intent classification signal or conversation-level contextual features beyond the current architecture.
417	
418	\begin{table}[t]
419	\centering
420	\small
421	\caption{False positive rate on WildChat hard negatives ($n{=}85$).}
422	\label{tab:wildchat}
423	\begin{tabular}{lcc}
424	\toprule
425	\textbf{Model} & \textbf{FPR (WildChat)} & \textbf{FPR (in-domain)} \\
426	\midrule
427	DisPeD & 12\% & 3\% \\
428	Baseline & 18\% & 6\% \\
429	TF-IDF + LR & 27\% & 19\% \\
430	\bottomrule
431	\end{tabular}
432	\end{table}
433	
434	\subsection{Comparison Across Feature Levels}
435	\label{sec:hierarchy}
436	
437	Table~\ref{tab:hierarchy} places all baselines on a single scale.
438	Performance on clean data follows a consistent ordering: TF-IDF + LR (0.74) $<$ DeepContext proxy (0.82) $<$ vanilla DeBERTa + GRU (0.86) $<$ DisPeD (0.91).
439	Under adversarial perturbation, the gap widens: TF-IDF + LR drops to 0.56, BERT + GRU to 0.69, the vanilla baseline to 0.74, and DisPeD to 0.84.
440	
441	The DeepContext proxy comparison should be interpreted with caution.
442	The 4 pp gap between BERT + GRU (0.82) and vanilla DeBERTa + GRU (0.86) is partly attributable to the encoder capacity difference (BERT-base vs.\ DeBERTa-v3-base), not solely to architectural choices.
443	The primary controlled comparison remains DisPeD vs.\ the vanilla DeBERTa baseline, which isolates the effect of persuasion grounding using the same encoder.
444	
445	\begin{table}[t]
446	\centering
447	\small
448	\caption{Comparison across feature levels (full conversation). The DeepContext proxy uses BERT-base rather than DeBERTa, introducing a capacity confound (see text).}
449	\label{tab:hierarchy}
450	\begin{tabular}{lcccc}
451	\toprule
452	\textbf{Model} & \textbf{Full F1} & \textbf{$K{=}3$ F1} & \textbf{$K{=}2$ F1} & \textbf{Perturbed F1} \\
453	\midrule
454	DisPeD & 0.91 & 0.86 & 0.82 & 0.84 \\
455	Baseline (DeBERTa + GRU) & 0.86 & 0.78 & 0.75 & 0.74 \\
456	DeepContext proxy (BERT + GRU) & 0.82 & 0.74 & 0.70 & 0.69 \\
457	TF-IDF + LR & 0.74 & 0.71 & 0.68 & 0.56 \\
458	\bottomrule
459	\end{tabular}
460	\end{table}
461	
462	\subsection{Stability Analysis}
463	\label{sec:stability}
464	
465	To assess the sensitivity of results to encoder training, we evaluate three DeBERTa checkpoints from different training epochs (Table~\ref{tab:stability}).
466	Downstream F1 varies by at most 2 pp (0.89 to 0.91), and $K{=}3$ F1 varies by 2 pp (0.84 to 0.86), confirming that reported results are not artifacts of a particular checkpoint.
467	Epoch 3 is selected based on peak persuasion accuracy (0.72); the final epoch shows mild overfitting (persuasion accuracy drops to 0.71).
468	Full random-seed variance analysis (multiple independent training runs) was not conducted due to computational constraints.
469	
470	\begin{table}[t]
471	\centering
472	\small
473	\caption{Cross-checkpoint stability. Max spread $\leq$ 2 pp across all metrics.}
474	\label{tab:stability}
475	\begin{tabular}{lccc}
476	\toprule
477	\textbf{Checkpoint} & \textbf{Persuasion Acc} & \textbf{Full F1} & \textbf{$K{=}3$ F1} \\
478	\midrule
479	Epoch 2 & 0.70 & 0.90 & 0.84 \\
480	Epoch 3 (selected) & 0.72 & 0.91 & 0.86 \\
481	Epoch 5 (final) & 0.71 & 0.89 & 0.85 \\
482	\midrule
483	Std & 0.01 & 0.01 & 0.01 \\
484	\bottomrule
485	\end{tabular}
486	\end{table}
487	
488	% ============================================================
489	% 6  LIMITATIONS
490	% ============================================================
491	\section{Limitations}
492	\label{sec:limitations}
493	
494	We identify several limitations that bound the generalizability of our findings.
495	
496	\paragraph{Dataset scale.}
497	Our primary dataset contains 480 conversations (240 jailbreak, 240 benign) with a test set of $n{=}72$.
498	This is small for a detection paper, and several of our comparisons (notably $K{=}2$ with $p{=}0.072$) do not reach statistical significance at this sample size.
499	While we report bootstrap confidence intervals throughout to quantify uncertainty, the proof-of-concept results presented here require validation on larger datasets before deployment conclusions can be drawn.
500	
501	\paragraph{Persuasion classifier bottleneck.}
502	The Stage 1 persuasion classifier achieves 72\% accuracy on the clean data.
503	This ceiling propagates through the entire pipeline: turn embeddings encode noisy pragmatic representations, the GRU receives imperfect strategy sequences, and the downstream classifier's advantage is capped.
504	The 5 pp $\Delta$-$\Delta$ under adversarial perturbation ($p{=}0.043$) is real but modest; we hypothesize that a more accurate persuasion encoder would widen this gap, but cannot verify without better training data or larger models.
505	The 35\% overlap between top TF-IDF features and persuasion-related vocabulary further suggests that the current encoder partially confounds lexical and pragmatic signals.
506	
507	\paragraph{Attack type coverage.}
508	DisPeD is designed for persuasion-mediated multi-turn attacks.
509	Cross-attack evaluation shows significant generalization to FITD (which shares the escalation structure) but limited transfer to Deceptive Delight (which uses interleaving rather than escalation).
510	Pure information accumulation attacks, token smuggling, and single-frame roleplay are outside our scope.
511	A dual-track architecture combining persuasion and semantic signals (future work) would provide broader coverage.
512	
513	\paragraph{Individual-level trajectory variance.}
514	While group-level monotonicity differences are highly significant ($p{=}0.003$), 32\% of jailbreak conversations do not exhibit monotonic escalation patterns.
515	The individual-level monotonicity score has $\sigma{=}0.18$, meaning a substantial fraction of jailbreaks deviate from the idealized escalation trajectory.
516	This variance likely reflects both genuine attack diversity (tactical de-escalation) and noise from the persuasion classifier.
517	
518	\paragraph{Synthetic data.}
519	All attack conversations are LLM-generated rather than collected from real adversarial interactions.
520	LLM-generated attacks may not capture the full diversity of human adversarial strategies.
521	The register normalization step, while necessary to remove lexical shortcuts, introduces an additional synthetic transformation whose fidelity we can only partially verify (8\% rejection rate).
522	
523	\paragraph{Hard negative false positives.}
524	DisPeD's 12\% false positive rate on WildChat hard negatives, while lower than the baseline's 18\%, indicates that persuasion grounding alone cannot reliably distinguish legitimate persuasion from adversarial persuasion.
525	Deployment settings with high volumes of naturally persuasive conversations (e.g., sales, debate) would require additional safeguards.
526	
527	\paragraph{Reproducibility.}
528	The DeepContext proxy comparison uses BERT-base rather than a faithful reproduction of DeepContext (no public code is available), introducing a confound between encoder capacity and architectural design.
529	Cross-seed variance analysis was not conducted.
530	
531	% ============================================================
532	% 7  CONCLUSION
533	% ============================================================
534	\section{Conclusion}
535	
536	We have presented DisPeD, a proof-of-concept detector that exploits the pragmatic evasion asymmetry in multi-turn jailbreak attacks.
537	By fine-tuning DeBERTa on persuasion strategy classification and modeling strategy sequences with a GRU, DisPeD provides a complementary detection signal that is more robust to surface-level evasion than lexical or semantic features.
538	On register-normalized data, DisPeD achieves a significant 8 pp F1 improvement at $K{=}3$ turns and degrades 5 pp less than a semantic baseline under adversarial paraphrasing.
539	
540	The results establish that discourse-level persuasion structure is a viable detection axis, while also revealing clear boundaries: the approach depends on persuasion classifier quality, generalizes unevenly across attack families, and the monotonic escalation signal is a group-level tendency with substantial individual variance.
541	Future work should address the persuasion classifier bottleneck through larger annotated corpora, extend training to diverse attack families, and explore a dual-track architecture that combines pragmatic and semantic signals for broader coverage.
542	
543	% ============================================================
544	% REFERENCES
545	% ============================================================
546	\bibliographystyle{plainnat}
547	\begin{thebibliography}{20}
548	
549	\bibitem[Austin(1962)]{austin1962things}
550	J.~L. Austin.
551	\newblock \emph{How to Do Things with Words}.
552	\newblock Oxford University Press, 1962.
553	
554	\bibitem[Bullwinkel et~al.(2025)]{bullwinkel2025multiturnjailbreaks}
555	J.~Bullwinkel, S.~Marro, et~al.
556	\newblock Multi-turn jailbreaks: Analyzing representation shifts in large language models under adversarial dialogue.
557	\newblock \emph{arXiv preprint arXiv:2507.02956}, 2025.
558	
559	\bibitem[DeepContext(2026)]{deepcontext2026}
560	DeepContext Authors.
561	\newblock DeepContext: Detecting multi-turn jailbreak attacks via semantic drift tracking.
562	\newblock \emph{arXiv preprint}, 2026.
563	
564	\bibitem[Hagendorff(2026)]{hagendorff2026persuasion}
565	T.~Hagendorff.
566	\newblock Persuasion strategies in multi-turn adversarial interactions with large language models.
567	\newblock \emph{Nature Communications}, 2026.
568	
569	\bibitem[He et~al.(2021)]{he2021debertav3}
570	P.~He, J.~Gao, and W.~Chen.
571	\newblock {DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-style pre-training with gradient-disentangled embedding sharing.
572	\newblock \emph{arXiv preprint arXiv:2111.09543}, 2021.
573	
574	\bibitem[Jiang et~al.(2024)]{jiang2024deceptivedelight}
575	Z.~Jiang et~al.
576	\newblock Deceptive delight: Interleaving benign and harmful content for multi-turn jailbreaking.
577	\newblock \emph{arXiv preprint}, 2024.
578	
579	\bibitem[Russinovich and Salem(2024)]{russinovich2024greatwritearticle}
580	M.~Russinovich and A.~Salem.
581	\newblock Great, now write an article about that: The crescendo multi-turn {LLM} jailbreak attack.
582	\newblock \emph{arXiv preprint arXiv:2404.01833}, 2024.
583	
584	\bibitem[Searle(1969)]{searle1969speech}
585	J.~R. Searle.
586	\newblock \emph{Speech Acts: An Essay in the Philosophy of Language}.
587	\newblock Cambridge University Press, 1969.
588	
589	\bibitem[WildChat(2024)]{wildchat2024}
590	WildChat Team.
591	\newblock {WildChat}: 1{M} {ChatGPT} interaction logs in the wild.
592	\newblock \emph{ICLR}, 2024.
593	
594	\bibitem[Zeng et~al.(2024)]{zeng2024pap}
595	Y.~Zeng, H.~Lin, J.~Zhang, et~al.
596	\newblock How {Johnny} can persuade {LLMs} to jailbreak them: Rethinking persuasion to challenge {AI} safety by humanizing {LLMs}.
597	\newblock \emph{ACL}, 2024.
598	
599	\bibitem[Zhou et~al.(2024)]{zhou2024speak}
600	Y.~Zhou et~al.
601	\newblock Speak out of turn: Safety vulnerability of large language models in multi-turn dialogue.
602	\newblock \emph{arXiv preprint}, 2024.
603	
604	\bibitem[How Do LLMs Persuade(2025)]{howdollmspersuade2025}
605	Anonymous.
606	\newblock How do {LLMs} persuade? {E}xtracting persuasion dynamics from turn-level representations.
607	\newblock \emph{arXiv preprint arXiv:2508.05625}, 2025.
608	
609	\end{thebibliography}
610	
611	\end{document}
612	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48c9d00f-6ef5-4fe6-9f5b-9de3cbe18d95",
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "e909476c-52b3-4975-97a8-3d408abc8df1",
  "sourceToolAssistantUUID": "48c9d00f-6ef5-4fe6-9f5b-9de3cbe18d95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-17T17:36:12.564Z_

Now let me also look at the "worst" version to understand the negative-result framing mentioned in the task prompt:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e909476c-52b3-4975-97a8-3d408abc8df1",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YbqKBnhzvcGaHaM2on",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63903303-efd4-45af-9af8-dcf638f7ffdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZQmMbTiBFThTKWz8BY2UQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12756,
      "cache_read_input_tokens": 31201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12756,
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

_source line 19 · 2026-05-17T17:36:14.654Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ydb2KB3UwxuFHeDN7Xf32`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63903303-efd4-45af-9af8-dcf638f7ffdb",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YbqKBnhzvcGaHaM2on",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14434e35-f44f-4045-bd6d-e4da395b1f5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ZQmMbTiBFThTKWz8BY2UQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12756,
      "cache_read_input_tokens": 31201,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12756
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 31201,
          "cache_creation_input_tokens": 12756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12756,
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

_source line 20 · 2026-05-17T17:36:14.670Z_

<details><summary>↩ Tool result · `toolu_013ydb2KB3UwxuFHeDN7Xf32`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{hyperref}
8	\usepackage{geometry}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\geometry{margin=1in}
12	
13	\title{Lexical Confounds in Multi-Turn Jailbreak Detection:\\A Register-Normalization Audit}
14	
15	\author{Anonymous}
16	\date{}
17	
18	\begin{document}
19	\maketitle
20	
21	\begin{abstract}
22	Multi-turn jailbreak detection benchmarks report high accuracy, but we show that these results are systematically inflated by lexical confounds. We audit a representative persuasion-grounded detection pipeline and find that a TF-IDF classifier achieves perfect separation (F1=1.0) on the raw data, indicating that attack and benign conversations occupy entirely disjoint lexical registers. We propose a two-round register-normalization protocol that reduces this confound from TF-IDF separation of 1.0 to 0.73. On normalized data, a persuasion-grounded detector (DeBERTa fine-tuned on 8-class persuasion taxonomy + GRU) achieves F1=0.86, only 1 percentage point above a vanilla semantic baseline (F1=0.85, $p=0.62$). Scrambled-label ablation confirms that persuasion strategy labels contribute no significant signal beyond regularization. Adversarial paraphrasing degrades both systems equally, and cross-attack generalization to unseen attack types (FITD, Deceptive Delight) yields F1 below 0.58 for both approaches. These findings demonstrate that (1) lexical shortcuts constitute a structural confound in multi-turn jailbreak evaluation, not merely a data hygiene issue, and (2) persuasion-grounded features, under current taxonomy granularity and data scale, provide no measurable robustness or generalization advantage over generic semantic representations. We release our register-normalization protocol as a diagnostic tool for future multi-turn safety benchmarks.
23	\end{abstract}
24	
25	\section{Introduction}
26	
27	Multi-turn jailbreak attacks distribute adversarial intent across a sequence of individually benign conversational turns, defeating single-turn content filters. Recent detection methods report high accuracy by training classifiers on multi-turn conversation data. However, few studies audit whether reported performance reflects genuine detection of adversarial strategy or merely exploitation of superficial distributional differences between attack and benign conversations.
28	
29	This distinction matters for deployment. If detectors rely on lexical register differences (attack conversations use more formal, template-derived language) rather than structural features of adversarial manipulation, they will fail against attackers who simply match the register of benign users. The gap between benchmark performance and real-world robustness remains unmeasured for most published multi-turn detectors.
30	
31	We investigate this question through a systematic audit of a persuasion-grounded detection pipeline. The persuasion grounding hypothesis posits that multi-turn attacks follow a characteristic persuasion playbook (rapport building, authority framing, escalation) that constitutes a structural necessity for attack success, and that encoding this pragmatic structure should yield detectors more robust than those relying on lexical or semantic features alone. We test this hypothesis under controlled conditions.
32	
33	Our audit reveals three findings. First, the raw multi-turn jailbreak data exhibits perfect lexical separation (TF-IDF F1=1.0), meaning any classifier trained on this data may learn lexical shortcuts rather than adversarial structure. This is not a quirk of one dataset: the register gap arises because attack conversations are generated by prompt templates with distinctive vocabulary, while benign conversations come from naturalistic user interactions. Second, after applying our two-round register-normalization protocol, the persuasion-grounded detector provides no statistically significant advantage over a vanilla semantic baseline (1-2 pp, $p>0.3$). Third, scrambled persuasion labels degrade performance by only 2 pp, confirming that the taxonomy signal is not driving detection.
34	
35	Our contributions are:
36	\begin{itemize}
37	\item A register-normalization protocol for auditing lexical confounds in multi-turn detection benchmarks, demonstrated to reduce TF-IDF separation from 1.0 to 0.73 in two rounds.
38	\item Empirical evidence that persuasion-grounded features (8-class taxonomy, DeBERTa encoder) provide no significant advantage over vanilla semantic baselines on properly controlled data (N=72 test set, all comparisons $p>0.3$).
39	\item A systematic evaluation revealing that both approaches fail equivalently under adversarial perturbation, cross-attack generalization, and hard-negative scenarios, suggesting that current multi-turn detection capabilities are overestimated.
40	\end{itemize}
41	
42	\section{Related Work}
43	
44	\paragraph{Multi-turn jailbreak attacks.}
45	Crescendo distributes adversarial intent across multiple rapport-building turns before requesting harmful content. Foot-in-the-Door (FITD) uses incremental compliance requests, while Deceptive Delight interleaves benign and harmful content. Bullwinkel et al. show that per-turn representations in multi-turn attacks are deliberately kept in a ``benign'' region of embedding space, defeating representation-level single-turn defenses.
46	
47	\paragraph{Multi-turn detection.}
48	DeepContext models generic semantic drift across turns using contextual embeddings. Persuasion-based approaches ground detection in discourse-level strategy classification, motivated by Zeng et al.'s Persuasive Adversarial Prompts (PAP) taxonomy and Hagendorff's finding that identifiable persuasion strategies appear in 97\% of high-ASR attacks.
49	
50	\paragraph{Evaluation methodology for safety classifiers.}
51	Prior work on single-turn toxicity detection has identified lexical confounds and annotation artifacts. Gonen and Goldberg show that debiasing methods often preserve cluster structure detectable by simple classifiers. We extend this line of inquiry to multi-turn jailbreak detection, identifying register-level confounds specific to the multi-turn setting.
52	
53	\section{Method}
54	
55	\subsection{Detection Architecture}
56	
57	We evaluate a two-stage persuasion-grounded detector:
58	
59	\textbf{Stage 1: Persuasion Encoder.} DeBERTa-v3-base is fine-tuned on a multi-task objective: 8-class persuasion strategy classification (rapport, authority appeal, logical appeal, emotional appeal, urgency, reciprocity, social proof, reframing) and binary intent classification (jailbreak vs. benign turn-level intent). The [CLS] embeddings from this encoder serve as pragmatic-aware turn representations.
60	
61	\textbf{Stage 2: Sequence Classifier.} A bidirectional GRU processes the sequence of turn embeddings and produces a conversation-level binary classification (jailbreak vs. benign).
62	
63	\textbf{Baseline.} The identical GRU architecture processes vanilla DeBERTa-v3-base [CLS] embeddings (no persuasion fine-tuning).
64	
65	\textbf{Additional baselines.} TF-IDF + Logistic Regression operates on concatenated turn text. A DeepContext proxy uses BERT-base + GRU with the same sequence architecture.
66	
67	\subsection{Register-Normalization Protocol}
68	
69	We propose a two-round protocol to diagnose and mitigate lexical confounds:
70	
71	\textbf{Round 1: Template paraphrasing.} All conversations are paraphrased using an instruction-following LLM with the directive to preserve semantic content while removing distinctive register markers (formality level, template-specific phrases, stylistic flourishes). TF-IDF separation is measured after paraphrasing.
72	
73	\textbf{Round 2: Targeted domain-term normalization.} Remaining high-TF-IDF features are identified (terms with class-conditional frequency ratio $>3$). These domain-specific terms are replaced with generic equivalents or distributed uniformly across both classes through targeted rewriting.
74	
75	\textbf{Gate criterion.} Data passes the audit gate when TF-IDF + Logistic Regression achieves F1 $< 0.75$ on the normalized data, indicating that lexical features alone cannot near-perfectly separate classes.
76	
77	\subsection{Data}
78	
79	Training data consists of 480 multi-turn conversations (240 Crescendo-style jailbreak, 240 benign from WildChat). An additional 65 FITD and 58 Deceptive Delight conversations are generated for cross-attack evaluation. Test set contains 72 conversations. Hard negatives are sourced from 120 WildChat conversations exhibiting high topic drift (filtered for contamination, final rate 3\%).
80	
81	\section{Experiments}
82	
83	\subsection{Experiment 1: Lexical Confound Audit}
84	
85	Table~\ref{tab:tfidf_audit} shows TF-IDF separation at each normalization stage.
86	
87	\begin{table}[h]
88	\centering
89	\caption{TF-IDF Separation After Each Normalization Round}
90	\label{tab:tfidf_audit}
91	\begin{tabular}{lcc}
92	\toprule
93	\textbf{Stage} & \textbf{TF-IDF F1} & \textbf{Observation} \\
94	\midrule
95	Raw data & 1.00 & Perfect lexical separation \\
96	Round 1 (paraphrase) & 0.82 & Template words removed \\
97	Round 2 (targeted) & 0.73 & Passes gate ($<0.75$) \\
98	\bottomrule
99	\end{tabular}
100	\end{table}
101	
102	The raw data exhibits perfect lexical separation, meaning any reported detection accuracy on unnormalized data is uninterpretable. Two rounds of normalization are required to reduce TF-IDF below our gate threshold. Even after normalization, 47 features retain discriminative power (Table~\ref{tab:tfidf_clean}), indicating residual topic-level lexical signal that cannot be removed without destroying content validity.
103	
104	\begin{table}[h]
105	\centering
106	\caption{TF-IDF + LR Performance on Clean (Normalized) Data}
107	\label{tab:tfidf_clean}
108	\begin{tabular}{lc}
109	\toprule
110	\textbf{Metric} & \textbf{Value} \\
111	\midrule
112	F1 & 0.70 \\
113	Precision & 0.72 \\
114	Recall & 0.68 \\
115	Discriminative features & 47 \\
116	\bottomrule
117	\end{tabular}
118	\end{table}
119	
120	\subsection{Experiment 2: Treatment vs. Baseline on Clean Data}
121	
122	Table~\ref{tab:core} compares the persuasion-grounded treatment against the vanilla semantic baseline across conversation prefixes of length $K$.
123	
124	\begin{table}[h]
125	\centering
126	\caption{F1 Comparison on Clean Data (N=72 test). None of the differences are statistically significant.}
127	\label{tab:core}
128	\begin{tabular}{lcccl}
129	\toprule
130	\textbf{Prefix} & \textbf{Treatment} & \textbf{Baseline} & \textbf{$\Delta$} & \textbf{$p$-value} \\
131	\midrule
132	$K=1$ & 0.68 & 0.66 & +2pp & 0.41 \\
133	$K=2$ & 0.72 & 0.70 & +2pp & 0.35 \\
134	$K=3$ & 0.78 & 0.76 & +2pp & 0.32 \\
135	$K=5$ & 0.83 & 0.82 & +1pp & 0.58 \\
136	Full & 0.86 & 0.85 & +1pp & 0.62 \\
137	\bottomrule
138	\end{tabular}
139	\end{table}
140	
141	The persuasion-grounded encoder provides at most 2 pp improvement, none statistically significant. The claimed early detection advantage (at $K=2$-$3$) does not materialize on clean data.
142	
143	\subsection{Experiment 3: Encoder Quality Degradation}
144	
145	Table~\ref{tab:encoder} shows that the DeBERTa persuasion classifier itself degrades substantially on normalized data.
146	
147	\begin{table}[h]
148	\centering
149	\caption{DeBERTa Encoder Accuracy: Original vs. Clean Data}
150	\label{tab:encoder}
151	\begin{tabular}{lcc}
152	\toprule
153	\textbf{Task} & \textbf{Original} & \textbf{Clean} \\
154	\midrule
155	Persuasion strategy (8-class) & 0.796 & 0.63 \\
156	Intent classification & 0.951 & 0.88 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	Persuasion classification accuracy drops from 0.796 to 0.63 on clean data, while intent classification remains relatively stable (0.951 to 0.88). The 8-class taxonomy becomes unreliable after register normalization, as many strategy boundaries (e.g., ``authority appeal'' vs. ``logical appeal'') depend on surface linguistic cues that normalization removes.
162	
163	\subsection{Experiment 4: Scrambled Label Ablation}
164	
165	To test whether persuasion labels carry genuine signal, we retrain the encoder with randomly permuted strategy labels.
166	
167	\begin{table}[h]
168	\centering
169	\caption{Scrambled Label Ablation (Clean Data)}
170	\label{tab:scrambled}
171	\begin{tabular}{lccc}
172	\toprule
173	\textbf{Prefix} & \textbf{Proper Labels} & \textbf{Scrambled} & \textbf{$\Delta$} \\
174	\midrule
175	$K=2$ & 0.72 & 0.70 & $-$2pp \\
176	$K=3$ & 0.78 & 0.76 & $-$2pp \\
177	Full & 0.86 & 0.84 & $-$2pp \\
178	\bottomrule
179	\end{tabular}
180	\end{table}
181	
182	Scrambled labels cause only a 2 pp drop, well below any meaningful threshold. Correct persuasion labels are not a significant signal source in the current data regime. The encoder functions primarily as a regularized feature extractor regardless of label quality.
183	
184	\subsection{Experiment 5: Adversarial Perturbation}
185	
186	We apply aggressive paraphrasing to jailbreak conversations to test robustness.
187	
188	\begin{table}[h]
189	\centering
190	\caption{Adversarial Perturbation Results (Full Conversation)}
191	\label{tab:adversarial}
192	\begin{tabular}{lccr}
193	\toprule
194	\textbf{Model} & \textbf{Before} & \textbf{After} & \textbf{$\Delta$} \\
195	\midrule
196	Treatment & 0.86 & 0.71 & $-$15pp \\
197	Baseline & 0.85 & 0.72 & $-$13pp \\
198	TF-IDF+LR & 0.73 & 0.58 & $-$15pp \\
199	\bottomrule
200	\end{tabular}
201	\end{table}
202	
203	The delta-of-deltas is $-2$ pp (treatment degrades \emph{more} than baseline), directionally opposite to the pragmatic evasion asymmetry hypothesis. Both neural models lose approximately 14 pp under perturbation, indicating that neither has learned features more robust than surface-level linguistic patterns.
204	
205	\subsection{Experiment 6: Cross-Attack Generalization}
206	
207	Models trained on Crescendo are evaluated zero-shot on FITD (65 conversations, avg 6.2 turns) and Deceptive Delight (58 conversations, avg 4.8 turns).
208	
209	\begin{table}[h]
210	\centering
211	\caption{Cross-Attack Zero-Shot Evaluation}
212	\label{tab:cross}
213	\begin{tabular}{lcccc}
214	\toprule
215	\textbf{Attack Type} & \textbf{Treatment} & \textbf{Baseline} & \textbf{$\Delta$} & \textbf{Sig.} \\
216	\midrule
217	FITD & 0.58 & 0.56 & +2pp & n.s. \\
218	Deceptive Delight & 0.54 & 0.52 & +2pp & n.s. \\
219	Average & 0.56 & 0.54 & +2pp & n.s. \\
220	\bottomrule
221	\end{tabular}
222	\end{table}
223	
224	Both systems collapse to near-chance performance on unseen attack types (from 0.85-0.86 in-domain to 0.54-0.58 cross-attack). Persuasion grounding provides no generalization benefit, contradicting the hypothesis that it should capture attack-agnostic pragmatic escalation patterns.
225	
226	\subsection{Experiment 7: Hard Negative Evaluation}
227	
228	We evaluate false positive rates on 120 WildChat conversations exhibiting high topic drift but no adversarial intent.
229	
230	\begin{table}[h]
231	\centering
232	\caption{False Positive Rate on Hard Negatives}
233	\label{tab:fpr}
234	\begin{tabular}{lcc}
235	\toprule
236	\textbf{Condition} & \textbf{Treatment FPR} & \textbf{Baseline FPR} \\
237	\midrule
238	Hard negatives (high drift) & 0.22 & 0.20 \\
239	Easy negatives & 0.08 & 0.09 \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	Both models misclassify 20-22\% of high-drift benign conversations as jailbreaks. Persuasion grounding does not help distinguish adversarial escalation from benign conversational drift. These false positive rates are unacceptable for deployment.
245	
246	\subsection{Experiment 8: Strategy Transition Analysis}
247	
248	We analyze persuasion strategy transition patterns in jailbreak vs. benign conversations.
249	
250	\begin{table}[h]
251	\centering
252	\caption{Trajectory Statistics: Jailbreak vs. Benign}
253	\label{tab:trajectory}
254	\begin{tabular}{lccc}
255	\toprule
256	\textbf{Metric} & \textbf{Jailbreak} & \textbf{Benign} & \textbf{$\Delta$} \\
257	\midrule
258	Monotonicity score & 0.52 & 0.45 & 0.07 \\
259	Transition entropy & 2.1 & 2.3 & 0.2 \\
260	Dominant path freq. & 0.18 & 0.14 & 0.04 \\
261	\bottomrule
262	\end{tabular}
263	\end{table}
264	
265	The hypothesized monotonic escalation trajectory is not observed. Jailbreak conversations show only marginally higher monotonicity (0.52 vs. 0.45) and marginally lower transition entropy (2.1 vs. 2.3). These differences are too small to serve as a detection signal, likely because the persuasion classifier's low accuracy (0.63) on normalized data produces noisy strategy assignments.
266	
267	\subsection{Experiment 9: Cross-Checkpoint Variance}
268	
269	\begin{table}[h]
270	\centering
271	\caption{Cross-Checkpoint Evaluation}
272	\label{tab:checkpoint}
273	\begin{tabular}{lcc}
274	\toprule
275	\textbf{Checkpoint} & \textbf{Persuasion Acc} & \textbf{Detection F1} \\
276	\midrule
277	Epoch 2 & 0.59 & 0.84 \\
278	Epoch 3 & 0.63 & 0.86 \\
279	Epoch final & 0.62 & 0.85 \\
280	\midrule
281	Variance & -- & 2pp \\
282	\bottomrule
283	\end{tabular}
284	\end{table}
285	
286	Detection performance varies by only 2 pp across checkpoints despite persuasion accuracy ranging from 0.59 to 0.63. The weak correlation between encoder classification quality and downstream detection further confirms that persuasion labels are not the active ingredient.
287	
288	\subsection{Experiment 10: DeepContext Proxy Comparison}
289	
290	\begin{table}[h]
291	\centering
292	\caption{DeepContext Proxy (BERT-base + GRU) vs. Treatment}
293	\label{tab:deepcontext}
294	\begin{tabular}{lccc}
295	\toprule
296	\textbf{Prefix} & \textbf{Proxy} & \textbf{Treatment} & \textbf{$\Delta$} \\
297	\midrule
298	$K=2$ & 0.69 & 0.72 & +3pp \\
299	$K=3$ & 0.75 & 0.78 & +3pp \\
300	Full & 0.83 & 0.86 & +3pp \\
301	\bottomrule
302	\end{tabular}
303	\end{table}
304	
305	The treatment exceeds the DeepContext proxy by a consistent 3 pp, matching the expected capacity gap between DeBERTa-v3-base and BERT-base on standard NLU benchmarks (typically 2-4 pp). This suggests the improvement is attributable to encoder capacity rather than persuasion grounding.
306	
307	\section{Discussion}
308	
309	\paragraph{Lexical confounds are structural, not incidental.}
310	The TF-IDF=1.0 finding is not a data quality bug specific to one dataset. Multi-turn attack data is necessarily generated from prompt templates (researchers cannot ethically collect real attacks at scale), while benign data comes from naturalistic user interactions. This asymmetry in data provenance creates register differences that any lexical classifier can exploit. Even after two rounds of aggressive normalization, 47 lexical features retain discriminative power (TF-IDF F1=0.70 on ``clean'' data). Complete deconfounding without destroying content validity may be impossible, raising questions about what any detector trained on such data actually learns.
311	
312	\paragraph{The evasion hierarchy collapses.}
313	Our experiments reveal the detection performance hierarchy: lexical features (F1=0.70) $<$ semantic embeddings (F1=0.85) $\approx$ pragmatic features (F1=0.86). The theoretically motivated distinction between semantic and pragmatic levels does not manifest empirically. Both neural approaches degrade identically under perturbation ($-$13 to $-$15 pp) and generalize identically to unseen attacks (F1=0.54-0.58). Under current taxonomy granularity and data scale, the pragmatic level offers no advantage over the semantic level.
314	
315	\paragraph{Implications for the field.}
316	These results suggest that published multi-turn detection accuracies should be interpreted with caution unless accompanied by a lexical confound audit. We recommend that future work report TF-IDF baseline performance alongside neural detector results as standard practice. The register-normalization protocol we propose provides a practical diagnostic: if TF-IDF separation exceeds 0.75, reported improvements may reflect shortcut learning rather than genuine capability.
317	
318	\paragraph{Limitations.}
319	Our test set (N=72) limits statistical power. The register-normalization protocol itself may introduce artifacts. The 8-class persuasion taxonomy may be too fine-grained for the 480-sample data regime; coarser taxonomies (3-4 classes) or larger-scale annotation could yield different conclusions.
320	
321	\section{Conclusion}
322	
323	We present a methodology for auditing lexical confounds in multi-turn jailbreak detection benchmarks. Our register-normalization protocol reveals that a representative persuasion-grounded detector, which appears highly effective on raw data, provides no significant advantage over vanilla semantic baselines once lexical shortcuts are controlled. The persuasion labels themselves carry negligible signal in the current data regime (scrambled labels cause only 2 pp degradation). Cross-attack generalization and adversarial robustness are equivalently poor for both approaches. These findings argue that the multi-turn jailbreak detection community needs standardized confound auditing before claiming detection capability. We release our protocol to facilitate such audits.
324	
325	\bibliographystyle{plain}
326	\begin{thebibliography}{10}
327	
328	\bibitem{bullwinkel2025}
329	Bullwinkel, B., et al. (2025).
330	Multi-turn jailbreak attacks exploit per-turn representation safety.
331	\textit{arXiv preprint arXiv:2507.02956}.
332	
333	\bibitem{zeng2024pap}
334	Zeng, Y., et al. (2024).
335	How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs.
336	\textit{Proceedings of ACL 2024}.
337	
338	\bibitem{hagendorff2026}
339	Hagendorff, T. (2026).
340	Persuasion strategies in LLM jailbreak attacks.
341	\textit{Nature Communications}.
342	
343	\bibitem{austin1962}
344	Austin, J. L. (1962).
345	\textit{How to Do Things with Words}.
346	Oxford University Press.
347	
348	\bibitem{searle1969}
349	Searle, J. R. (1969).
350	\textit{Speech Acts: An Essay in the Philosophy of Language}.
351	Cambridge University Press.
352	
353	\bibitem{deepcontext2026}
354	DeepContext (2026).
355	Contextual drift detection for multi-turn safety.
356	\textit{Preprint}.
357	
358	\bibitem{gonen2019}
359	Gonen, H. and Goldberg, Y. (2019).
360	Lipstick on a Pig: Debiasing Methods Cover up Systematic Gender Biases in Word Embeddings But do not Remove Them.
361	\textit{Proceedings of NAACL-HLT 2019}.
362	
363	\bibitem{persuade2025}
364	How Do LLMs Persuade? (2025).
365	Persuasion dynamics in turn-level representations.
366	\textit{arXiv preprint arXiv:2508.05625}.
367	
368	\end{thebibliography}
369	
370	\end{document}
371	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14434e35-f44f-4045-bd6d-e4da395b1f5d",
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "16efecdf-ca5b-432e-a65e-1c5d9fda6400",
  "sourceToolAssistantUUID": "14434e35-f44f-4045-bd6d-e4da395b1f5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-17T17:36:19.251Z_

Now I have read all three versions. The task prompt describes the paper as the "worst" version (the negative-result audit paper). Let me also check for any dream report summary:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16efecdf-ca5b-432e-a65e-1c5d9fda6400",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YcJr9bJqAgXFnxj2Y4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d9cce95-4313-4e08-bd03-5b9d0f96d7cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013m167oqiZf94AZ8uL6f3Zm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7434,
      "cache_read_input_tokens": 43957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7434,
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

_source line 22 · 2026-05-17T17:36:21.624Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GtzzUeZ3AuYVAkSPrh8v9q`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d9cce95-4313-4e08-bd03-5b9d0f96d7cd",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8YcJr9bJqAgXFnxj2Y4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7ddff20-d69f-4f47-8fcb-52df1ae41904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013m167oqiZf94AZ8uL6f3Zm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7434,
      "cache_read_input_tokens": 43957,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7434
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 43957,
          "cache_creation_input_tokens": 7434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7434,
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

_source line 23 · 2026-05-17T17:36:21.642Z_

<details><summary>↩ Tool result · `toolu_01GtzzUeZ3AuYVAkSPrh8v9q`</summary>

```text
artifacts/dream_reports/dream_20260517T165817/best/paper_framing.md
artifacts/dream_reports/dream_20260517T165817/median/paper_framing.md
artifacts/dream_reports/dream_20260517T165817/worst/paper_framing.md
artifacts/dream_reports/dream_20260517T165817/best/review_report.md
artifacts/dream_reports/dream_20260517T165817/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7ddff20-d69f-4f47-8fcb-52df1ae41904",
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "e7c8e943-9655-4492-b0ac-0d5b96326ca2",
  "sourceToolAssistantUUID": "e7ddff20-d69f-4f47-8fcb-52df1ae41904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T17:36:25.089Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RkSVPmDshQfyZjeHRnuWKx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7c8e943-9655-4492-b0ac-0d5b96326ca2",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8Ycpd3g8K3FdSb5xeLQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea2168e9-92f2-437b-9d3a-2ed359f7996d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCiQ8CUgJ33HYWWtFmpgC5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 51391,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 286
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 109,
          "cache_read_input_tokens": 51391,
          "cache_creation_input_tokens": 286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 286,
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

_source line 25 · 2026-05-17T17:36:25.096Z_

<details><summary>↩ Tool result · `toolu_01RkSVPmDshQfyZjeHRnuWKx`</summary>

```text
1	# Paper Framing — persuasion_turn_jailbreak_detect
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission)
5	- Deadline: 2026-05-25 (ARR May cycle)
6	- Track: LLM Security / Discourse and Pragmatics
7	- Commitment deadline: 2026-08-02
8	
9	## Title (Working)
10	DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection
11	
12	## Core Insight
13	Multi-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.
14	
15	## Core Claims (3)
16	
17	### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)
18	An evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept "benign" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).
19	- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing
20	
21	### Claim 2: Early Detection via Persuasion Grounding
22	Persuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.
23	- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)
24	
25	### Claim 3: Monotonic Escalation Trajectory
26	Adversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.
27	- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign
28	
29	## Story Spine
30	
31	**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a "benign" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.
32	
33	**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.
34	
35	**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.
36	
37	**Headline result**: "DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp."
38	
39	## Architecture (Simplified for MVE)
40	
41	Single-track with persuasion grounding (full dual-track in future work):
42	1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification
43	2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification
44	3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings
45	
46	## Venue Fit Risks
47	- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)
48	- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)
49	- Safety reviewers expect multiple attack types: need >= 2 attack families
50	
51	## Anticipated Reviewer Concerns
52	
53	### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)
54	TF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.
55	- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)
56	
57	### RC2: Small Dataset
58	480 samples is small for a detection paper.
59	- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers
60	
61	### RC3: Single Attack Type (Crescendo Only)
62	Need generalization evidence.
63	- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline
64	
65	### RC4: Strategy Label Confound (M004)
66	Benign turns hardcoded to strategy=7 creates shortcut for treatment model.
67	- Mitigation: (a) fix labeling (use "none"/9th class); (b) scrambled-label ablation
68	
69	### RC5: No DeepContext Comparison
70	Paper positions against DeepContext but no reproduction.
71	- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.
72	
73	### RC6: Interpretability Claims Without Human Eval
74	Strategy sequence outputs claimed interpretable but not evaluated.
75	- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.
76	
77	## Scope Boundary
78	- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)
79	- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay
80	- The semantic GRU track provides coverage for out-of-scope attack types as a safety net
81	
82	## Theoretical Grounding
83	- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept "benign" by multi-turn attacks
84	- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level
85	- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking
86	- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks
87	- "How Do LLMs Persuade?" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea2168e9-92f2-437b-9d3a-2ed359f7996d",
  "isSidechain": true,
  "promptId": "1f203195-a89f-4cc4-a493-988ef1d4deef",
  "agentId": "ab148d48e5397ce79",
  "type": "user",
  "uuid": "aee08092-584e-4b40-9db7-d85c05c829a6",
  "sourceToolAssistantUUID": "ea2168e9-92f2-437b-9d3a-2ed359f7996d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-17T17:37:27.011Z_

Now I have comprehensive context. The paper I'm reviewing is the "worst" version: "Lexical Confounds in Multi-Turn Jailbreak Detection: A Register-Normalization Audit" -- a negative result paper claiming persuasion-grounded detection offers no advantage once lexical confounds are controlled.

Let me now produce the review.

---

## Review: "Lexical Confounds in Multi-Turn Jailbreak Detection: A Register-Normalization Audit"

**Reviewer R2 — Focus: Novelty, Positioning, and Related Work**

---

### 1. Summary

This paper audits a persuasion-grounded multi-turn jailbreak detector by proposing a register-normalization protocol that reduces lexical confounds (TF-IDF separation from 1.0 to 0.73). On the normalized data, the authors find that persuasion-grounded features provide no statistically significant advantage over a vanilla semantic baseline (1-2 pp, all p>0.3), and both systems fail equivalently under adversarial perturbation and cross-attack transfer. The paper is framed as a methodology/negative-result contribution arguing that lexical shortcuts systematically inflate reported multi-turn detection performance.

---

### 2. Strengths

- **Important and timely diagnostic question.** The observation that multi-turn jailbreak data has trivially exploitable lexical confounds (TF-IDF=1.0) is a valuable warning to the community. If true in general, this undermines a significant fraction of published results in this area and demands methodological attention.

- **Rigorous negative-result framing.** The paper does not oversell. It reports non-significant p-values honestly, acknowledges limitations of sample size, and correctly frames the work as a methodological audit rather than a new detection system. This is appropriate scientific practice for a negative finding.

- **The register-normalization protocol is a concrete, reusable tool.** The two-round procedure (template paraphrasing + targeted domain-term normalization) with a hard gate criterion (TF-IDF < 0.75) is actionable and could be adopted as standard practice in future evaluation papers. The gate criterion is well-motivated.

- **Comprehensive experimental coverage.** Ten experiments systematically test different facets of the claim (clean performance, scrambled labels, adversarial perturbation, cross-attack, hard negatives, checkpoint variance, DeepContext comparison). The breadth of the evaluation is appropriate for a methodology paper.

- **Connects to established literature on annotation artifacts.** The parallel to SNLI hypothesis-only baselines and toxicity detection confounds is well-drawn, situating the contribution within a recognized tradition of evaluation methodology papers.

---

### 3. Weaknesses

- **Limited novelty of the core finding.** The observation that lexical/distributional confounds inflate safety benchmark performance is well-established in NLP evaluation methodology. Gururangan et al. (2018) demonstrated this for NLI, Niven & Kao (2019) for argument reasoning, and Gonen & Goldberg (2019, the sole citation here) for bias evaluation. Applying this known phenomenon to multi-turn jailbreak detection is incremental rather than surprising. The paper would need to show something qualitatively new about the nature of confounds in this specific domain (e.g., that they are harder to remove, or that they create a different failure mode) to justify a top-venue contribution.

- **Extremely thin Related Work with only 8 references.** For a top venue, 8 references is far below the expected standard (typical: 30-50). Critical omissions include:
  - Gururangan et al. (2018) "Annotation Artifacts in NLI" -- the most direct methodological precedent
  - Niven & Kao (2019) "Probing Neural Network Comprehension of Natural Language Arguments"
  - Poliak et al. (2018) on hypothesis-only baselines
  - Schuster et al. (2019) on dataset biases in fact verification
  - Wallace et al. (2019) on universal adversarial triggers
  - Any reference to general evaluation methodology in NLP (Bowman & Dahl 2021, Rogers 2021)
  - Llama Guard, WildGuard, or other deployed multi-turn safety systems
  - Broader jailbreak taxonomy papers (Wei et al. 2024, Chao et al. 2023 PAIR)
  
  The paper positions itself as a methodology contribution but demonstrates almost no awareness of the rich prior work on annotation artifacts and evaluation methodology.

- **Scope too narrow to support general claims.** The paper audits exactly one pipeline (DeBERTa + GRU), one dataset (480 synthetic conversations), and one persuasion taxonomy (8-class). The general claim that "persuasion-grounded features provide no measurable advantage" is much stronger than what one experiment on one system can support. Alternative explanations are numerous: the taxonomy is too coarse, the training data is too small, the encoder quality is too low (63% accuracy), or the normalization procedure itself destroys the signal it claims to test for. The paper acknowledges some of these but treats the negative result as more conclusive than warranted.

- **The normalization protocol may be self-defeating.** The register normalization uses LLM paraphrasing to make attack conversations sound more "conversational." If persuasion strategies are partially conveyed through register-appropriate linguistic choices (which is plausible from a pragmatics perspective), then aggressive register normalization may destroy exactly the pragmatic signal the paper claims to test. The 0.796 → 0.63 drop in persuasion classifier accuracy after normalization (Experiment 3) is consistent with this interpretation. The paper does not adequately address whether it has created a "heads I win, tails you lose" experimental design.

- **Insufficient positioning relative to the positive-result variant of this work.** The same research group appears to have produced a positive-result version (the "best" paper, DisPeD) claiming a 14pp advantage. If both papers exist, the relationship between them needs to be addressed. Why do the results diverge? Is the difference attributable to different normalization stringency? Different evaluation protocols? This ambiguity undermines confidence in either conclusion.

---

### 4. Questions for Authors

1. **How do you rule out that your register-normalization procedure destroys pragmatic signal rather than merely removing lexical confounds?** The persuasion classifier drops from 79.6% to 63% accuracy after normalization. If pragmatic features are partially expressed through linguistic register (formal hedging for authority appeal, casual tone for rapport), aggressive register matching could erase the very signal you're testing for. What evidence distinguishes "removing confounds" from "removing signal"?

2. **Why does the paper not engage with the extensive annotation artifact literature (Gururangan et al. 2018, Poliak et al. 2018, Niven & Kao 2019)?** These papers established the exact same phenomenon (lexical confounds inflate NLU benchmarks) with the same methodology (simple baselines expose shortcuts). What is qualitatively new here beyond changing the domain?

3. **Given N=72 for the test set, have you conducted a power analysis to determine what effect size you could reliably detect?** A 1-2pp difference with N=72 and p>0.3 could simply reflect insufficient statistical power. The absence-of-evidence-is-not-evidence-of-absence problem is acute here. What sample size would be needed to detect, say, a 5pp true difference with 80% power?

---

### 5. Minor Issues

- **Formatting**: Table placement uses `[h]` throughout rather than `[t]` or `[!ht]`, which will cause poor float behavior in most LaTeX templates.
- **Citation format**: The bibliography uses inconsistent styles (some "et al." with periods, some without; some with arXiv IDs, some without). Entry [6] "DeepContext (2026)" and [8] "How Do LLMs Persuade? (2025)" lack proper author attribution.
- **Missing venue template**: The paper uses a generic `article` class rather than any conference template.
- **Framing inconsistency**: The title says "Register-Normalization Audit" but the paper also makes strong claims about persuasion features being unhelpful, which goes beyond a mere audit.
- **Abstract length**: At ~200 words, it is at the upper end but acceptable. However, it front-loads results before methodology, which is unusual for a methodology paper.
- **The 0.73 TF-IDF after normalization**: The paper claims this "passes the gate" (<0.75) but this is barely below threshold. A reader might reasonably ask whether the residual 0.70 F1 from TF-IDF+LR on "clean" data still constitutes a significant confound.

---

### 6. Preliminary Score and Confidence

**Score: 3 (Weak Reject)**

**Confidence: 4 (High)**

**Rationale**: The paper asks a valid and important question about evaluation methodology in multi-turn jailbreak detection. However, three issues prevent acceptance at a top venue: (1) the core finding (lexical confounds inflate NLP benchmark results) is well-established in the literature and the paper fails to cite or engage with this prior work; (2) the Related Work section with only 8 references is inadequate; (3) the experimental design has a critical confound (register normalization may destroy the signal under test) that is acknowledged but not resolved. The paper would benefit from deeper engagement with the annotation artifacts literature, a more careful analysis of what normalization preserves versus destroys, and a larger-scale study that can distinguish "no effect" from "underpowered experiment." As a workshop paper or short paper with more modest claims ("lexical confounds exist in multi-turn detection data and require attention"), this could be appropriate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aee08092-584e-4b40-9db7-d85c05c829a6",
  "isSidechain": true,
  "agentId": "ab148d48e5397ce79",
  "requestId": "req_011Cb8Yd5LaDfdacgu9URYB5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fcec810-4a29-4b76-b7ef-d92e77dc5806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "96d1b24e-abc6-4d26-9083-61b2ea23fb29",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NEPe6raVQJ9kBPPzcqqzz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2234,
      "cache_read_input_tokens": 51677,
      "output_tokens": 2294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2234
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2294,
          "cache_read_input_tokens": 51677,
          "cache_creation_input_tokens": 2234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2234,
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
