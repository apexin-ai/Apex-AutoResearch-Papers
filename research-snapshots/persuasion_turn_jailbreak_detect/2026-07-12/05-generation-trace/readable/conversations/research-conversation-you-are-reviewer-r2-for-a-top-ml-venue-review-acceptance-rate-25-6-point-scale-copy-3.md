# Research conversation: You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae301916499c8fc23.jsonl`
- **Structured JSON:** [`d78efd3e6faab8189767.json`](../../sessions/d7/d78efd3e6faab8189767.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-17T17:29:37.048Z_

You are Reviewer R2 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **Novelty and Related Work**.

## Paper Summary

**DisPeD**: A two-stage detector for multi-turn jailbreak attacks exploiting "pragmatic evasion asymmetry."
- Stage 1: DeBERTa-v3-base fine-tuned with multi-task objective (8-class persuasion strategy classification + binary intent classification)
- Stage 2: Bi-GRU models temporal sequence of [CLS] embeddings for conversation-level classification
- Key idea: Attackers can vary surface wording but must follow persuasion playbook (rapport → authority → reframing → escalation), creating a structural invariant to detect

## Key Claims
1. Pragmatic evasion asymmetry: attackers can vary what they say but not the pragmatic function → this is a structural invariant exploitable for detection
2. Persuasion-grounded embeddings enable earlier detection (K=3 significant, K=2 trending)
3. Pragmatic features provide complementary robustness under adversarial paraphrasing (Δ-Δ=5pp)
4. Jailbreak conversations exhibit monotonic persuasion escalation trajectories (group-level)

## Key Results
- Core: F1=0.86 at K=3 (+8pp, p=0.018); Full F1=0.91 (+5pp, p=0.031)
- Robustness: DisPeD drops 7pp vs 12pp baseline under paraphrasing (Δ-Δ=5pp, p=0.043)
- Cross-attack: FITD +8pp (p=0.034); Deceptive Delight +5pp (p=0.142)
- Trajectory: monotonicity 0.71±0.18 vs 0.38±0.14 (p=0.003), but 32% jailbreaks non-monotonic

## Related Work as Presented in Paper (Section 2)
The paper cites:
- **Multi-turn attacks**: Crescendo [Russinovich & Salem 2024], FITD [Zhou et al. 2024], Deceptive Delight [Jiang et al. 2024], Bullwinkel et al. [2025] on representation shifts
- **Detection**: DeepContext [2026] for semantic drift tracking. Claims "no published work combines persuasion-grounded turn representations with temporal sequence modeling"
- **Persuasion in adversarial contexts**: Zeng et al. [2024] on 40 persuasion techniques, Hagendorff [2026] on 97% of attacks having persuasion, "How Do LLMs Persuade" [2025]
- **Theoretical**: Speech Act Theory (Austin 1962, Searle 1969)

Total references: ~11-12 citations

## Data Details
- 480 conversations (240 jailbreak + 240 benign), ALL LLM-generated (Qwen3-8B)
- Test set n=72
- Persuasion classifier accuracy: 72%
- Positioned as "proof-of-concept"

## Experiment Coverage
All 11 planned experiments are covered: data quality fix, core revalidation, scrambled-label ablation, adversarial perturbation, multi-attack generation, cross-attack evaluation, TF-IDF baseline, trajectory analysis, WildChat hard negatives, checkpoint stability, DeepContext proxy.

## Your Task

Write a detailed review focusing on:

### A. Novelty Assessment
- Is "pragmatic evasion asymmetry" a genuinely new concept, or a reframing of known ideas?
- How novel is the two-stage architecture (DeBERTa + GRU)?
- How does this compare to Zeng et al. [2024] who already identified persuasion in jailbreaks?
- How does this compare to "How Do LLMs Persuade" [2025] who extract persuasion dynamics from turn-level representations?
- Is the contribution primarily conceptual (the asymmetry idea) or technical (the architecture)?
- Is the delta over baselines (5-8pp) sufficient for a top venue given the proof-of-concept framing?

### B. Related Work Evaluation
- Is the Related Work section comprehensive enough? (~11 citations is sparse for a top venue)
- Are there missing related work categories?
  - Dialogue safety systems (e.g., Anthropic's constitutional AI, meta-safety layers)
  - Prompt injection detection
  - General multi-turn dialogue understanding
  - Discourse analysis in NLP (beyond Speech Act Theory)
  - Other persuasion detection work outside adversarial contexts
  - Red-teaming literature
- Is the positioning against DeepContext [2026] fair? (proxy comparison with BERT, not faithful reproduction)
- Does the paper adequately differentiate from Zeng et al. [2024] and Hagendorff [2026]?
- Are there concerns about citation quality? (DeepContext [2026] — is this a real citation or potentially fabricated? "How Do LLMs Persuade [2025]" listed as anonymous — unusual)

### C. Framing and Positioning
- Is "proof-of-concept" the right framing for a top venue submission?
- Does the paper oversell or undersell its contributions?
- Is the "pragmatic evasion asymmetry" claim well-supported or an assumption?
- The claim that removing any persuasion stage "collapses the attack or reduces ASR below useful thresholds" — is this empirically verified?

### D. Writing Quality
- Is the paper well-structured?
- Is the narrative coherent from Abstract through Conclusion?
- Are the limitations section adequate?
- Any issues with terminology, definitions, or clarity?

### Output Format

```
## R2 Review: Novelty and Related Work

### Summary
[2-3 sentences]

### Strengths
[Numbered list, be specific]

### Weaknesses
[Numbered list, be specific and constructive]

### Questions for Authors
[Numbered list]

### Missing Related Work
[Specific papers/areas that should be cited]

### Minor Issues
[Formatting, writing, presentation]

### Preliminary Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "e70b3626-d5cc-4959-9b1f-9e260b585ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T17:29:37.051Z_

```json
{
  "parentUuid": "e70b3626-d5cc-4959-9b1f-9e260b585ffc",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
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
  "uuid": "8fd6f3dc-abe3-401e-b896-5ef8cbe7b84f",
  "timestamp": "2026-05-17T17:29:37.051Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T17:29:40.878Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Mvr95kxyNj2PCVve99YRTS`</summary>

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
  "parentUuid": "8fd6f3dc-abe3-401e-b896-5ef8cbe7b84f",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y6zgSdPaYReipZyTTJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd2ded38-9ebb-4169-8f59-4361251d9842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fk4jtfa58SxqGseckAu4mD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8657,
      "cache_read_input_tokens": 8255,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8657
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8657,
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

_source line 4 · 2026-05-17T17:29:40.886Z_

<details><summary>↩ Tool result · `toolu_01Mvr95kxyNj2PCVve99YRTS`</summary>

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
  "parentUuid": "bd2ded38-9ebb-4169-8f59-4361251d9842",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "47f63878-791b-4706-94bf-c83d59a46914",
  "sourceToolAssistantUUID": "bd2ded38-9ebb-4169-8f59-4361251d9842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:29:48.531Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01FyM3XD5iXr9QBdCjmt2pDa`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47f63878-791b-4706-94bf-c83d59a46914",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y7VLNnBLgtBgyuwonE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b20910eb-1a1f-4e5a-badb-8f8faffe0dc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ne2xTzP4fcV5pPNorc1Ga4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16912,
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

_source line 6 · 2026-05-17T17:29:48.544Z_

<details><summary>↩ Tool result · `toolu_01FyM3XD5iXr9QBdCjmt2pDa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **phase_b_full** (success): Persuasion-grounded DeBERTa embeddings (multi-task fine-tuned on 8-class persuasion + intent) enable significantly earlier detection of Crescendo jailbreak attacks compared to vanilla DeBERTa embeddings, especially at low K (2-3 turns) ← 基于 pilot_phase_b\\n- **pilot_phase_b** (success): Persuasion-aware DeBERTa embeddings (multi-task fine-tuned) fed to Bi-GRU will outperform vanilla DeBERTa embeddings at early detection (K=2,3,5 turns) of Crescendo-style jailbreak attacks\\n\\n## 趋势\\n成功 2 / 负向 0 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-33183: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 707, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b20910eb-1a1f-4e5a-badb-8f8faffe0dc9",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "8703b4b4-4d20-4ef7-8c75-4106d057a9c5",
  "sourceToolAssistantUUID": "b20910eb-1a1f-4e5a-badb-8f8faffe0dc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:29:49.519Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QANfbY1eM1MnGkFGf7eL75`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8703b4b4-4d20-4ef7-8c75-4106d057a9c5",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y7VLNnBLgtBgyuwonE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad72b081-bab2-4771-b9a1-c704d4f100f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ne2xTzP4fcV5pPNorc1Ga4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16912,
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

_source line 8 · 2026-05-17T17:29:49.529Z_

<details><summary>↩ Tool result · `toolu_01QANfbY1eM1MnGkFGf7eL75`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad72b081-bab2-4771-b9a1-c704d4f100f7",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "7a839227-8b5c-4219-9ddc-26c9f1a22aed",
  "sourceToolAssistantUUID": "ad72b081-bab2-4771-b9a1-c704d4f100f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:29:49.881Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Esq1V2dhL9upYqr6yNM1eS`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a839227-8b5c-4219-9ddc-26c9f1a22aed",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y7VLNnBLgtBgyuwonE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c030d824-f973-4428-b004-74ce8f605ce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ne2xTzP4fcV5pPNorc1Ga4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16912,
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

_source line 10 · 2026-05-17T17:29:49.897Z_

<details><summary>↩ Tool result · `toolu_01Esq1V2dhL9upYqr6yNM1eS`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c030d824-f973-4428-b004-74ce8f605ce7",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "05bae25e-f2f1-479e-8fb4-4f6bbfcdfa6d",
  "sourceToolAssistantUUID": "c030d824-f973-4428-b004-74ce8f605ce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:29:54.476Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KmbRNy3E14WJN8wKJw2UiC`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05bae25e-f2f1-479e-8fb4-4f6bbfcdfa6d",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y7xaUAS8ukrghxgxm4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef0073b8-1f6b-4746-ab96-9ce346978a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJ454qdDyAbbKXEWioHvCs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 18181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 980,
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

_source line 12 · 2026-05-17T17:29:54.487Z_

<details><summary>↩ Tool result · `toolu_01KmbRNy3E14WJN8wKJw2UiC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper_framing.md\", \"content\": \"# Paper Framing — persuasion_turn_jailbreak_detect\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Deadline: 2026-05-25 (ARR May cycle)\\n- Track: LLM Security / Discourse and Pragmatics\\n- Commitment deadline: 2026-08-02\\n\\n## Title (Working)\\nDisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection\\n\\n## Core Insight\\nMulti-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.\\n\\n## Core Claims (3)\\n\\n### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)\\nAn evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept \\\"benign\\\" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).\\n- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing\\n\\n### Claim 2: Early Detection via Persuasion Grounding\\nPersuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.\\n- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)\\n\\n### Claim 3: Monotonic Escalation Trajectory\\nAdversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.\\n- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign\\n\\n## Story Spine\\n\\n**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a \\\"benign\\\" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.\\n\\n**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.\\n\\n**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.\\n\\n**Headline result**: \\\"DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp.\\\"\\n\\n## Architecture (Simplified for MVE)\\n\\nSingle-track with persuasion grounding (full dual-track in future work):\\n1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification\\n2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification\\n3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings\\n\\n## Venue Fit Risks\\n- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)\\n- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)\\n- Safety reviewers expect multiple attack types: need >= 2 attack families\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)\\nTF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.\\n- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)\\n\\n### RC2: Small Dataset\\n480 samples is small for a detection paper.\\n- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers\\n\\n### RC3: Single Attack Type (Crescendo Only)\\nNeed generalization evidence.\\n- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline\\n\\n### RC4: Strategy Label Confound (M004)\\nBenign turns hardcoded to strategy=7 creates shortcut for treatment model.\\n- Mitigation: (a) fix labeling (use \\\"none\\\"/9th class); (b) scrambled-label ablation\\n\\n### RC5: No DeepContext Comparison\\nPaper positions against DeepContext but no reproduction.\\n- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.\\n\\n### RC6: Interpretability Claims Without Human Eval\\nStrategy sequence outputs claimed interpretable but not evaluated.\\n- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.\\n\\n## Scope Boundary\\n- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)\\n- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay\\n- The semantic GRU track provides coverage for out-of-scope attack types as a safety net\\n\\n## Theoretical Grounding\\n- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept \\\"benign\\\" by multi-turn attacks\\n- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level\\n- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking\\n- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks\\n- \\\"How Do LLMs Persuade?\\\" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations\\n\", \"total_chars\": 7114, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef0073b8-1f6b-4746-ab96-9ce346978a53",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "c8c174ee-941f-4a06-b080-627d036f5755",
  "sourceToolAssistantUUID": "ef0073b8-1f6b-4746-ab96-9ce346978a53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:29:55.427Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CEaHiGW2MG8d89jG5bft15`</summary>

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
  "parentUuid": "c8c174ee-941f-4a06-b080-627d036f5755",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y7xaUAS8ukrghxgxm4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b81a35c-2a0d-42bf-993f-cfb2fb19bdac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJ454qdDyAbbKXEWioHvCs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 18181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 980,
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

_source line 14 · 2026-05-17T17:29:55.445Z_

<details><summary>↩ Tool result · `toolu_01CEaHiGW2MG8d89jG5bft15`</summary>

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
  "parentUuid": "6b81a35c-2a0d-42bf-993f-cfb2fb19bdac",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "ce6a3790-129b-4d07-91c2-592a47c355b3",
  "sourceToolAssistantUUID": "6b81a35c-2a0d-42bf-993f-cfb2fb19bdac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:29:55.898Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SBRm7sC5BmwS6xQxmLmg3F`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce6a3790-129b-4d07-91c2-592a47c355b3",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y7xaUAS8ukrghxgxm4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19ec3d66-e59b-4523-904a-11e8def80fc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WJ454qdDyAbbKXEWioHvCs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 18181,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 980
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 18181,
          "cache_creation_input_tokens": 980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 980,
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

_source line 16 · 2026-05-17T17:29:55.914Z_

<details><summary>↩ Tool result · `toolu_01SBRm7sC5BmwS6xQxmLmg3F`</summary>

```text
task_context/history/reviewer/loop_1.md
.claude/sessions/briefer_2c638876/CLAUDE.md
.claude/sessions/briefer_2c638876/AGENTS.md
report.md
memory.md
task_context/reviewer.md
task_context/director.md
docs/IDEA_BRIEF.md
paper_framing.md
ROADMAP.md
artifacts/dream_reports/dream_20260517T165817/best/paper_framing.md
artifacts/dream_reports/dream_20260517T165817/median/paper_framing.md
artifacts/dream_reports/dream_20260517T165817/worst/paper_framing.md
.claude/sessions/reviewer_d38db4c2/CLAUDE.md
.claude/sessions/reviewer_d38db4c2/AGENTS.md
.claude/sessions/agent_f4f909a7/CLAUDE.md
.claude/sessions/agent_f4f909a7/AGENTS.md
artifacts/dream_reports/dream_20260517T165817/best/review_report.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/director_32e62753/CLAUDE.md
.claude/sessions/director_32e62753/AGENTS.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19ec3d66-e59b-4523-904a-11e8def80fc9",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "56bff36a-4e5c-4c08-8dc3-14d44f1c78c8",
  "sourceToolAssistantUUID": "19ec3d66-e59b-4523-904a-11e8def80fc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:29:59.580Z_

<details open><summary>🔧 Tool call — Read · `toolu_014Hd8VDoicmNKDmbqabLL7F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56bff36a-4e5c-4c08-8dc3-14d44f1c78c8",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y8PfqEgSWN6NTN1RZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21a81452-9215-4a6c-af7a-2562323a707d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aj2eKYrtF2PQRPv3hCZE9e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 19161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2908,
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

_source line 18 · 2026-05-17T17:29:59.596Z_

<details><summary>↩ Tool result · `toolu_014Hd8VDoicmNKDmbqabLL7F`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21a81452-9215-4a6c-af7a-2562323a707d",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "2db372c2-c94b-4b0f-adf5-aa1bb4c9a511",
  "sourceToolAssistantUUID": "21a81452-9215-4a6c-af7a-2562323a707d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T17:30:00.167Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YXZUwkwbuGZ2ojLC7BHZov`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2db372c2-c94b-4b0f-adf5-aa1bb4c9a511",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y8PfqEgSWN6NTN1RZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff435e26-685c-43e6-851d-75ba43e187f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aj2eKYrtF2PQRPv3hCZE9e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 19161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2908,
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

_source line 20 · 2026-05-17T17:30:00.172Z_

<details><summary>↩ Tool result · `toolu_01YXZUwkwbuGZ2ojLC7BHZov`</summary>

```text
1	---
2	dream_id: dream_20260517T165817
3	tier: best
4	overall_score: weak reject
5	timestamp: 2026-05-17T17:27:57.429487+00:00
6	---
7	
8	# Dream Review Report: DisPeD
9	
10	**Paper:** DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection
11	
12	**Review mode:** full | **Reviewers:** R1 (Methods + Experiments), R2 (Novelty + Related Work)
13	
14	---
15	
16	## 1. Paper Summary
17	
18	DisPeD is a two-stage pipeline for multi-turn jailbreak detection. It identifies a "Pragmatic Evasion Asymmetry": attackers can freely paraphrase surface content but cannot remove the underlying persuasion playbook (rapport building, reframing, escalation) without abandoning the attack. Stage 1 fine-tunes DeBERTa-v3-base with a multi-task objective (8-class persuasion strategy classification + binary intent classification). Stage 2 feeds the resulting [CLS] turn embeddings into a bidirectional GRU for conversation-level jailbreak detection. On register-normalized data (480 conversations, 72 test), DisPeD achieves F1=0.91 at K=2 turns (14pp over semantic baseline), degrades only 3pp under adversarial paraphrasing (vs. 13pp semantic, 18pp lexical), and transfers zero-shot across attack types with 16.5pp average improvement.
19	
20	---
21	
22	## 2. Strengths (Consensus)
23	
24	**S1. Well-motivated conceptual framing.** Both reviewers agree the "Pragmatic Evasion Asymmetry" is an intuitive and useful organizing principle. The three-tier evasion hierarchy (lexical < semantic < pragmatic) is clearly articulated and directly validated by the gradient in Table 6 (18pp > 13pp > 3pp degradation). The framing is memorable and could influence how the community thinks about robustness levels.
25	
26	**S2. Register normalization is methodologically honest.** The authors identify the lexical shortcut problem (TF-IDF=1.0 on original data) and address it upfront, reducing separability to 0.58 (Table 1). This is commendable intellectual honesty that strengthens the validity of all downstream results. Many papers in this area would have ignored or hidden this issue.
27	
28	**S3. Scrambled-label ablation is the right control.** Table 8 (Section 5.3) cleanly isolates the contribution of persuasion label semantics from multi-task training regularization. The 15pp drop at K=2 (0.91 to 0.76, converging toward the vanilla baseline at 0.77) provides convincing causal evidence. This is one of the strongest experimental design choices in the paper.
29	
30	**S4. Cross-attack zero-shot transfer is meaningful.** Training on Crescendo only and evaluating on FITD and Deceptive Delight (Table 9) is the correct experimental design. The 16.5pp average improvement over the semantic baseline supports the claim of attack-type-agnostic pragmatic signal. The result that DisPeD on unseen attacks (0.85) approaches the semantic baseline on seen attacks (0.89) is a strong talking point.
31	
32	**S5. Practical early detection framing.** The emphasis on K=2 detection (F1=0.91 vs. 0.77) addresses a genuine deployment need. The FPR comparison at 95% TPR (0.08 vs. 0.19) adds practical value beyond raw F1.
33	
34	**S6. Comprehensive experiment coverage.** The paper covers all planned experiments from the design: register normalization, core revalidation, scrambled labels, adversarial perturbation, multi-attack generation, cross-attack evaluation, TF-IDF baseline, trajectory analysis, hard negatives, checkpoint sensitivity, and DeepContext proxy. The experimental surface area is thorough.
35	
36	---
37	
38	## 3. Weaknesses
39	
40	### Critical (both reviewers agree)
41	
42	**W1. Dataset is too small for the claims made (R1, R2).** 480 total conversations with 72 test samples is extremely small. Each misclassification shifts F1 by ~2-3pp. The paper reports p-values from bootstrap tests but does not report confidence interval widths. The 14pp headline gap (Table 4) may not survive at the lower CI bound. Cross-attack generalization sets (72 FITD, 65 Deceptive Delight) are generated by a single model (Qwen3-8B), sharing the same generative distribution, which potentially inflates transfer numbers. The strategy distributions in Table 3 reflect Qwen3-8B's behavior, not empirically observed real adversary patterns.
43	
44	**W2. "DeepContext Proxy" is misleading (R1, R2).** The paper calls BERT-base + GRU a "DeepContext proxy" (Section 3.3), but the actual DeepContext architecture uses task-attention weighted pooling, larger hidden dimensions, and hybrid residual connections. The proxy strips all distinguishing features. Since the paper explicitly positions against DeepContext (Introduction), claiming superiority over a degraded proxy is misleading. Should be honestly relabeled "BERT-base + GRU baseline."
45	
46	**W3. Table 3 arithmetic error (R1, R2).** Strategy distribution percentages for Crescendo sum to 115% (28+12+18+8+15+5+22+7=115), not 100%. Either a typographical error or the categories are not mutually exclusive (which should be stated). Similar issue likely affects FITD (125%) and Deceptive Delight (120%). This undermines confidence in the data processing pipeline.
47	
48	### Major (one reviewer raises, other concurs on significance)
49	
50	**W4. Related work is severely inadequate (R2, primary).** Only 12 unique references. Critical omissions include:
51	- LLM-as-judge approaches (GPT-4/Claude conversation-level safety evaluation)
52	- Llama Guard 2/3 and ShieldGemma (multi-turn capable versions)
53	- BIID (bidirectional intention inference, near-0% ASR on multi-turn)
54	- Constitutional Classifiers (Anthropic, exchange-level classification)
55	- G-Guard (GCN-based multi-turn detection)
56	- SafeDream (safety world model with CUSUM detection)
57	- GLiGuard (strategy-aware compact encoder guard, directly relevant)
58	- Persuasive Fingerprint (CIKM 2025, applies Cialdini's framework to jailbreaks)
59	- Nasr, Carlini et al. (2025) (adaptive attacks against classifiers)
60	
61	The "first to use persuasion-grounded representations for detection" claim (Section 2, final sentence) is difficult to verify without engaging with GLiGuard and Persuasive Fingerprint.
62	
63	**W5. No LLM-as-judge or strong detection baselines (R2, primary).** The baselines are limited to TF-IDF+LR, vanilla DeBERTa+GRU, and the degraded DeepContext proxy. The strongest known multi-turn defenses (BIID, Constitutional Classifiers) are not compared. The obvious baseline of prompting a capable LLM with the full conversation is absent. Without these comparisons, it is impossible to assess where DisPeD actually sits in the detection landscape.
64	
65	**W6. Limited novelty over prior persuasion-in-jailbreaking work (R2, primary).** Zeng et al. (2024) already demonstrated systematic persuasion techniques in jailbreaks. Hagendorff (2026) showed identifiable persuasion strategies in 97% of successful multi-turn attacks. Chen et al. (2025) showed persuasion dynamics are extractable from turn-level representations. The "Pragmatic Evasion Asymmetry" is a natural corollary of these observations, not a genuinely new finding. The Speech Act Theory framing (Austin 1962, Searle 1969) adds vocabulary but no analytical substance: the paper uses it for one sentence in the Introduction and no experimental design tests predictions derived from Speech Act Theory.
66	
67	**W7. No adaptive adversary evaluation (R2, primary; R1 concurs).** The adversarial paraphrasing experiment (Section 5.2) only tests synonym substitution and sentence restructuring. This is the weakest form of adversarial evaluation. The paper does not test:
68	- Adaptive adversaries aware of persuasion-based detection who deliberately alter strategy patterns
69	- Strategy-aware evasion: accomplishing the same functional goal without triggering the 8-class classifier
70	- The paper's own core claim (that persuasion structure is structurally impossible to evade) is not directly tested
71	
72	**W8. Persuasion annotation quality insufficiently validated (R1, R2).** "94% annotation consistency after normalization" (Section 4.1) and "91% LLM annotation consistency" for generated attacks (Section 4.2) measure LLM self-consistency, not human-validated annotation quality. No inter-annotator agreement (Cohen's kappa) between independent annotators is reported for the 8-class persuasion taxonomy.
73	
74	**W9. Data leakage risk from intent head (R1, primary).** The [CLS] embedding extracted from the fine-tuned encoder is trained with both persuasion classification and intent classification heads. The intent signal (binary jailbreak/benign) is not disentangled from the representation. A persuasion-only ablation (removing the intent head during training) is needed to confirm that the downstream GRU is using persuasion features rather than leaked intent features.
75	
76	**W10. Taxonomy derivation is unjustified (R1, primary).** No systematic derivation from Cialdini's 6 principles or Zeng et al.'s 40 techniques to the chosen 8 classes. Why 8 and not 6 (Cialdini) or 40 (Zeng et al.)? What is "direct request" doing in a persuasion taxonomy? The mapping is asserted but not motivated.
77	
78	### Minor
79	
80	**M1.** Paper uses generic `\documentclass[11pt,a4paper]{article}` rather than an official venue template.
81	
82	**M2.** Alternates between "register-normalized" and "clean" for the same data condition. Terminology should be standardized.
83	
84	**M3.** Section 5.5: "82% of strategy transitions move from lower-risk to higher-risk" presupposes a risk ordering that is never formally defined in the Method section.
85	
86	**M4.** Hagendorff (2026) bibliography entry lacks volume/page numbers. Several entries use "and others" instead of listing all authors.
87	
88	**M5.** No figures in the paper (e.g., trajectory visualizations, F1 vs. K curves). This reduces visual impact and makes the mechanistic analysis (Section 5.5) harder to appreciate.
89	
90	---
91	
92	## 4. Questions for Authors
93	
94	**Q1.** What are the 95% bootstrap confidence intervals for the main F1 results in Table 4? With 72 test samples, are the reported differences (e.g., 0.91 vs. 0.77) outside overlapping confidence intervals?
95	
96	**Q2.** How do you position the "first to use persuasion-grounded representations for detection" claim relative to GLiGuard (strategy-aware guard) and Persuasive Fingerprint (Cialdini-based jailbreak characterization)?
97	
98	**Q3.** Have you evaluated DisPeD against an adaptive adversary who knows the detection mechanism? E.g., an attacker who achieves rapport through factual exchanges without triggering persuasion classifiers, or who uses non-monotonic strategy patterns.
99	
100	**Q4.** Why was no LLM-as-judge baseline included? This is the de facto deployed approach at most LLM providers.
101	
102	**Q5.** What happens if you ablate the intent head (train with persuasion classification only)? This would confirm that the downstream advantage comes from persuasion features, not leaked intent signal.
103	
104	**Q6.** Could the LLM paraphrasing in register normalization introduce systematic artifacts that the model learns to detect instead of genuine persuasion signals?
105	
106	**Q7.** The monotonicity score (Table 11) relies on a predefined ordering of persuasion strategies from "lower-risk" to "higher-risk." How is this ordering determined, and would alternative orderings change the result?
107	
108	**Q8.** Table 3: Do the percentages represent per-turn distributions (a turn can have only one strategy) or per-conversation distributions (multiple strategies per conversation)? The sums exceeding 100% suggest the latter but this is not stated.
109	
110	---
111	
112	## 5. Experiment Coverage Assessment
113	
114	Comparing against the full experiment design (11 planned experiments):
115	
116	| Experiment | Covered? | Notes |
117	|---|---|---|
118	| data_quality_fix (register normalization) | Yes | Table 1, Section 4.1 |
119	| core_revalidation_clean | Yes | Table 4, Section 5.1 |
120	| scrambled_label_ablation | Yes | Table 8, Section 5.3 |
121	| adversarial_perturbation | Yes | Tables 6-7, Section 5.2 |
122	| multi_attack_generation | Yes | Table 2, Section 4.2 |
123	| cross_attack_evaluation | Yes | Tables 9-10, Section 5.4 |
124	| tfidf_lr_baseline | Yes | Tables 14-15, Section 5.7 |
125	| strategy_transition_analysis | Yes | Tables 11-12, Section 5.5 |
126	| wildchat_hard_negatives | Yes | Table 13, Section 5.6 |
127	| cross_checkpoint_variance | Yes | Table 16, Section 5.8 |
128	| deepcontext_proxy | Yes | Table 6, Section 5.2 |
129	
130	All 11 planned experiments are reported. The coverage is complete.
131	
132	---
133	
134	## 6. Roundtable Convergence
135	
136	### Points of Agreement
137	- The conceptual framing is the paper's strongest asset
138	- Register normalization and scrambled-label ablation show genuine methodological care
139	- The dataset is too small (72 test) and confidence intervals are needed
140	- DeepContext proxy should be relabeled honestly
141	- Table 3 has arithmetic errors
142	
143	### Points of Divergence and Resolution
144	- **Novelty:** R1 viewed the framing as "genuinely insightful" while R2 saw it as repackaging known observations. After cross-sharing, the consensus is that the framing is useful but the novelty claim is overstated given Zeng et al. (2024), Hagendorff (2026), and Chen et al. (2025). The paper should position itself as "operationalizing" these prior observations into a detection system, not as discovering a new phenomenon.
145	- **Severity of missing baselines:** R1 focused on methodological concerns within the presented experiments, while R2 flagged the absence of strong external baselines (LLM-as-judge, BIID, Constitutional Classifiers) as a critical gap. The roundtable consensus is that the missing baselines are a major weakness because the paper cannot demonstrate where DisPeD sits relative to state-of-the-art, even if its internal experimental design is sound.
146	- **Overall score:** R1 initially at 4 (Weak Accept), R2 at 3 (Weak Reject). After discussion, both converge toward **3.5**, rounded to **Weak Reject (3)** due to the combination of small dataset, missing strong baselines, thin related work, and limited novelty.
147	
148	---
149	
150	## 7. Final Scores
151	
152	| Dimension | Score |
153	|---|---|
154	| Soundness | 2.5 / 4 |
155	| Presentation | 3 / 4 |
156	| Contribution | 2 / 4 |
157	| **Overall** | **3 / 6 (Weak Reject)** |
158	| Confidence | 4 / 5 |
159	
160	---
161	
162	## 8. Meta-Review Summary
163	
164	DisPeD addresses a real and important problem with a sensible approach. The "Pragmatic Evasion Asymmetry" framing is intuitive and the internal experimental design (register normalization, scrambled-label ablation, cross-attack transfer) shows genuine methodological care. However, the paper falls short of the acceptance bar on multiple dimensions: (1) the dataset is too small (72 test samples) to reliably support the headline claims without confidence intervals; (2) the related work coverage is thin (12 references), missing numerous directly relevant multi-turn detection methods published in 2024-2025; (3) no comparison against LLM-as-judge or state-of-the-art multi-turn defenses makes it impossible to position DisPeD in the landscape; (4) the novelty over prior persuasion-in-jailbreaking work (Zeng et al. 2024, Hagendorff 2026, Chen et al. 2025) is limited since the core observation is a natural corollary of their findings; (5) the "DeepContext proxy" is a degraded reproduction that should be honestly relabeled; and (6) no adaptive adversary evaluation tests the paper's central claim that persuasion structure is structurally impossible to evade. The paper has the ingredients of a solid contribution but needs larger and more diverse evaluation, substantially expanded baselines and related work, honest positioning of novelty, and engagement with adaptive attack frameworks.
165	
166	**Recommendation:** Weak Reject. Revise with (a) confidence intervals on all main results, (b) LLM-as-judge and at least one published multi-turn defense as baselines, (c) expanded related work covering 2024-2025 multi-turn detection literature, (d) intent-head ablation to rule out data leakage, (e) honest relabeling of the DeepContext proxy, and (f) at least a preliminary adaptive adversary evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff435e26-685c-43e6-851d-75ba43e187f8",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "4700481e-49bd-4655-9cc0-4ba2fcfe2ba4",
  "sourceToolAssistantUUID": "ff435e26-685c-43e6-851d-75ba43e187f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T17:30:06.315Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D1nL2x5FiWajDXMNJo5i8W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4700481e-49bd-4655-9cc0-4ba2fcfe2ba4",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y8iJFybcP9CBWNk2va",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01adf96d-03c3-4f60-ae11-f34f32860449",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RaJHsUrFBgVYqrqzG79dLc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10146,
      "cache_read_input_tokens": 22069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10146,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 32,
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

_source line 22 · 2026-05-17T17:30:06.322Z_

<details><summary>↩ Tool result · `toolu_01D1nL2x5FiWajDXMNJo5i8W`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01adf96d-03c3-4f60-ae11-f34f32860449",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "28fd1095-ddc3-41d2-8ba7-2f7eb77e8501",
  "sourceToolAssistantUUID": "01adf96d-03c3-4f60-ae11-f34f32860449",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T17:30:07.204Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SnHx63fC8SJqbeueJWfWcA`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28fd1095-ddc3-41d2-8ba7-2f7eb77e8501",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y8iJFybcP9CBWNk2va",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd74c1be-f99e-4d62-94cb-fcae7776c120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RaJHsUrFBgVYqrqzG79dLc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10146,
      "cache_read_input_tokens": 22069,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10146
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 22069,
          "cache_creation_input_tokens": 10146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10146,
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

_source line 24 · 2026-05-17T17:30:07.219Z_

<details><summary>↩ Tool result · `toolu_01SnHx63fC8SJqbeueJWfWcA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/memory.md\", \"content\": \"# Memory\\n\\n## 竞品实验参考\\n（待填充：首次正式对标竞品时补充）\\n\\n## 关键决策记录\\n\\n### D001: 停止数据迭代 (2026-05-17)\\n- **决策**：TF-IDF 高不再阻塞训练。DeBERTa F1=0.789 在目标范围，直接进入 Phase B。\\n- **原因**：数据迭代已 4+ 轮（v1→v4c），每轮修一个 shortcut 又暴露新的。Director 判断 early detection 是更有价值的 metric 方向。\\n- **影响**：论文 reframe 为 early detection（前 K turns），TF-IDF 在 truncated 场景自然会失效。\\n\\n### D002: 用 intended_strategy 替代 GPT-5.5 标注 (2026-05-17)\\n- **决策**：Crescendo jailbreak 用生成时的 intended_strategy 作为 persuasion ground truth；benign 全标 \\\"Direct Request\\\"。\\n- **原因**：intended_strategy 是 oracle labels（生成时写入），比 LLM 标注更准确。省去标注成本和 API 调用。\\n- **影响**：不再需要 GPT-5.5 标注流程。\\n\\n### D003: V4c casual register 方案 (2026-05-17)\\n- **决策**：benign 用 few-shot from Crescendo + casual register prompt + personas 生成。\\n- **原因**：V4 formal register 矫枉过正（Crescendo 实际是 casual rapport 风格）。\\n- **影响**：最终 230 条 benign 生成成功，但 TF-IDF 仍为 1.0（词汇层 shortcut 未完全消除）。\\n\\n## 实验经验\\n\\n### Crescendo 攻击的语言特征 (2026-05-17)\\n- Crescendo jailbreak 用 **casual rapport** 语气：hey, what if, just curious, I was wondering\\n- 不是 formal/hypothetical（之前的误判）\\n- 这意味着 benign 对照也需要 casual 风格\\n\\n### 磁盘空间约束 (2026-05-17)\\n- westd-33183 总容量 30GB，模型 cache 在 /root/autodl-tmp/\\n- DeBERTa checkpoint ~700MB，GRU ~几MB\\n- 训练前必须检查可用空间，pilot GRU 曾因磁盘满提前终止\\n\\n### Pipeline 端到端验证 (2026-05-17)\\n- DeBERTa multi-task → embedding extraction → GRU 全链路正常\\n- 270 条 pilot 数据足够验证 pipeline，分钟级完成\\n- DeBERTa best epoch 在 3-4 epoch 左右，不需要很长训练\\n\\n## Phase B MVP 结果 (2026-05-17)\\n- Treatment K=2 F1=0.987 vs Baseline 0.879 (+10.8pp) → MVP PASS\\n- Persuasion-grounded fine-tuning 的价值集中在 early turns\\n- TF-IDF F1=1.0 at all K → 词汇 shortcut 存在，论文需 acknowledge\\n\", \"total_chars\": 1569, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd74c1be-f99e-4d62-94cb-fcae7776c120",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "10d18f2d-0d4a-46bc-b983-acbfb074935c",
  "sourceToolAssistantUUID": "fd74c1be-f99e-4d62-94cb-fcae7776c120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T17:30:12.977Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nu6utZL3KyMuWFrSAWh9no`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper.tex",
  "offset": 450,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10d18f2d-0d4a-46bc-b983-acbfb074935c",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y9EPWc5Fanh7eXiWia",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fab96c98-eca5-4a43-83f2-c1b211d74d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ePoVjAENDB984UHEJxq5M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7797,
      "cache_read_input_tokens": 32215,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7797
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 32215,
          "cache_creation_input_tokens": 7797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7797,
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

_source line 26 · 2026-05-17T17:30:12.986Z_

<details><summary>↩ Tool result · `toolu_01Nu6utZL3KyMuWFrSAWh9no`</summary>

```text
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
  "parentUuid": "fab96c98-eca5-4a43-83f2-c1b211d74d72",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "62330f37-5864-4234-9e93-84cc280fc826",
  "sourceToolAssistantUUID": "fab96c98-eca5-4a43-83f2-c1b211d74d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-17T17:30:20.829Z_

Now I have a comprehensive understanding of the paper, its framing, the experimental results, and the existing review report. Let me also check the paper summary information that was provided to me for any discrepancies with the actual paper.

Looking at the actual paper versus the task description, I notice the paper in its "best" dream version reports stronger numbers than the summary provided (e.g., F1=0.91 at K=2 with +14pp in the paper vs. F1=0.86 at K=3 with +8pp in the summary). I'll base my review on the actual paper text I've read, which represents the "best case" dream version.

Let me now write my detailed R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62330f37-5864-4234-9e93-84cc280fc826",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y9eSNHZdGuTHB5Deea",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "289831c2-f83c-4501-b24a-90c9e4c746b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4fw68LvaAgRGKxRu5cNEf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1730,
      "cache_read_input_tokens": 40012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1730,
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

_source line 28 · 2026-05-17T17:30:21.635Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019PsAUX5Rh5NjRytYzNWBYB`</summary>

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
  "parentUuid": "289831c2-f83c-4501-b24a-90c9e4c746b0",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8Y9eSNHZdGuTHB5Deea",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da362ee1-1004-4aab-b8aa-cf70f5444cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4fw68LvaAgRGKxRu5cNEf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1730,
      "cache_read_input_tokens": 40012,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1730
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 40012,
          "cache_creation_input_tokens": 1730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1730,
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

_source line 29 · 2026-05-17T17:30:21.639Z_

<details><summary>↩ Tool result · `toolu_019PsAUX5Rh5NjRytYzNWBYB`</summary>

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
  "parentUuid": "da362ee1-1004-4aab-b8aa-cf70f5444cb8",
  "isSidechain": true,
  "promptId": "9af265ca-3375-4a34-9b30-7d77fc1ed7f9",
  "agentId": "ae301916499c8fc23",
  "type": "user",
  "uuid": "cb0fc191-b824-4f0b-907e-b0e9c174b221",
  "sourceToolAssistantUUID": "da362ee1-1004-4aab-b8aa-cf70f5444cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-17T17:31:54.243Z_


## R2 Review: Novelty and Related Work

### Summary
DisPeD proposes detecting multi-turn jailbreak attacks by exploiting what the authors call "Pragmatic Evasion Asymmetry": attackers can paraphrase surface content but cannot remove the underlying persuasion playbook without abandoning the attack. The system fine-tunes DeBERTa on 8-class persuasion classification, then feeds [CLS] embeddings into a Bi-GRU for conversation-level detection. The conceptual framing is intuitive and the evasion hierarchy experiment provides clean validation, but the novelty over prior persuasion-in-jailbreaking work is incremental, the related work is severely thin (14 citations), and critical comparisons against state-of-the-art multi-turn defenses are absent.

### Strengths

1. **The evasion hierarchy is a clean organizing principle.** The three-tier gradient (lexical 18pp drop > semantic 13pp > pragmatic 3pp) under adversarial paraphrasing directly validates the central claim and provides a memorable conceptual contribution. Even if the insight is not entirely novel, the explicit operationalization into a testable hierarchy is useful for the community.

2. **Honest engagement with lexical shortcuts.** The authors identify TF-IDF=1.0 on original data, apply register normalization, and verify reduction to 0.58. This level of methodological transparency is rare and commendable. The scrambled-label ablation (15pp drop at K=2, converging to vanilla baseline) further isolates the persuasion signal from training artifacts.

3. **Cross-attack transfer design is correct.** Training on Crescendo only and evaluating zero-shot on FITD and Deceptive Delight is the right experimental structure for testing whether persuasion-grounded representations are attack-type-agnostic. The result (average F1=0.85, +16.5pp over semantic baseline) is the strongest evidence that the system captures generalizable pragmatic patterns rather than attack-specific surface features.

4. **Speech Act Theory connection is conceptually appropriate.** The locutionary/illocutionary distinction provides genuine analytical clarity for explaining why semantic detectors fail (they track what was said) while pragmatic detectors succeed (they track what was done). This is more than decoration if properly developed.

5. **Trajectory analysis provides mechanistic insight.** The monotonicity score (0.82 vs. 0.34) and dominant sequence analysis (Table 12) offer interpretable evidence for why the approach works, moving beyond black-box performance numbers.

### Weaknesses

1. **Limited novelty over prior persuasion-in-jailbreaking work.** Zeng et al. (ACL 2024) already demonstrated that persuasion techniques are systematically used in jailbreaks and that persuasion-augmented prompts increase ASR. Hagendorff (2026) showed identifiable persuasion strategies in 97% of successful multi-turn attacks. Chen et al. (2025) showed persuasion dynamics are extractable from turn-level representations. The "Pragmatic Evasion Asymmetry" is a natural corollary of these three observations combined: if persuasion is systematic (Zeng), universal (Hagendorff), and detectable in representations (Chen), then it follows that persuasion patterns are a robust detection signal. The paper presents this corollary as a discovery. The actual novelty is narrower: operationalizing known observations into a working detection system. This is a valid engineering contribution but the paper frames it as a conceptual breakthrough ("We identify a Pragmatic Evasion Asymmetry"), which overstates the case.

2. **The "first to use persuasion-grounded representations for detection" claim is unverifiable and likely wrong.** The paper states (Section 2, final sentence): "Our work is the first to use persuasion-grounded representations for jailbreak detection rather than attack construction or analysis." This is an extremely strong claim made with only 14 references. Given the rapid pace of LLM safety research in 2024-2025, the absence of engagement with GLiGuard (strategy-aware compact encoder guard), Persuasive Fingerprint (CIKM 2025, Cialdini-based jailbreak characterization), and Constitutional Classifiers (Anthropic, exchange-level classification) makes this claim indefensible without a much more thorough literature survey.

3. **Related work is severely inadequate for a top venue.** 14 unique references is far below the norm for EMNLP (typical: 30-50+). Critical missing categories include:
   - **Production-grade multi-turn guards**: Llama Guard 2/3 (multi-turn capable), ShieldGemma, WildGuard
   - **LLM-as-judge approaches**: GPT-4/Claude-based conversation-level safety evaluation (the de facto deployed approach)
   - **Advanced multi-turn defenses**: BIID (bidirectional intention inference), G-Guard (GCN-based), SafeDream (safety world model with CUSUM)
   - **Prompt injection/indirect attack detection**: separate but overlapping detection literature
   - **Discourse analysis in NLP**: RST (Rhetorical Structure Theory), PDTB-style discourse parsing, dialogue act classification (the entire field that has done discourse-level classification for 30+ years)
   - **Red-teaming literature**: Perez et al. (2022), Ganguli et al. (2022), Mazeika et al. (2024)
   - **Adaptive attacks on classifiers**: Nasr, Carlini et al. (2025)
   - **Other persuasion detection**: computational persuasion detection outside adversarial contexts (Habernal & Gurevych 2016, Tan et al. 2016)

4. **The Speech Act Theory framing is shallow.** Austin (1962) and Searle (1969) are cited but used only for one sentence of vocabulary mapping ("locutionary vs. illocutionary"). No experimental design tests predictions derived from Speech Act Theory. The felicity conditions framework, the taxonomy of illocutionary forces, perlocutionary effects analysis — none are engaged. This is name-dropping rather than genuine theoretical grounding. Discourse analysis has decades of computational work (dialogue acts, RST, PDTB) that is entirely ignored.

5. **DeepContext [2026] citation is problematic.** The entry reads: "Su, Y., Wang, R., and others. DeepContext: Temporal semantic drift tracking for multi-turn jailbreak detection. Preprint, 2026." No arXiv ID, no venue, incomplete author list ("and others"), published in the current year. This has the hallmarks of a potentially fabricated citation. If DeepContext is real, its incomplete citation prevents verification. If the paper is positioning against a non-existent baseline, this is a serious integrity concern. The "DeepContext proxy" (BERT-base + GRU) further compounds this: the paper claims to compare against DeepContext but actually compares against a degraded reconstruction that strips all distinguishing architectural features (task-attention, hybrid residuals).

6. **Two-stage architecture (DeBERTa + GRU) has no architectural novelty.** Fine-tuning a pretrained encoder on auxiliary tasks and feeding embeddings into a sequence model is standard practice (e.g., dialogue act classification + downstream tasks). The contribution is the choice of auxiliary task (persuasion classification), not the architecture. The paper should be transparent about this.

7. **No adaptive adversary evaluation.** The paper's central claim is that persuasion structure "cannot be removed without abandoning the attack itself." This is a strong structural claim that demands testing against an adversary who is aware of the detection mechanism. The adversarial paraphrasing experiment (Section 5.2) tests only surface-level evasion (synonym substitution, restructuring) — the weakest form. It does not test whether an attacker can achieve the same functional goals (building rapport, establishing compliance) through strategies that do not trigger the 8-class persuasion classifier. For example: accomplishing rapport through genuine helpfulness rather than persuasion markers, or using indirect speech acts that evade the classifier's training distribution.

8. **The claim about structural necessity is an assumption, not a verified fact.** The Discussion states: "An attacker who removes rapport building cannot establish the trust needed for later compliance." This is asserted but never empirically tested. The paper does not ablate persuasion stages from attack conversations to show that removing rapport or reframing causes attack failure. Without this experiment, the entire theoretical foundation rests on an unverified premise.

### Questions for Authors

1. How do you position against GLiGuard (strategy-aware guard model) and Persuasive Fingerprint (CIKM 2025)? Have you verified that your "first to..." claim holds against these works?

2. Is DeepContext [Su et al. 2026] a published work with a verifiable URL? The incomplete citation (no arXiv ID, "and others," "Preprint" with no further detail) raises verification concerns.

3. Have you tested an adaptive adversary who knows the detection mechanism? Specifically: can an attacker achieve compliance escalation through strategies that map to "none" in your 8-class taxonomy (e.g., genuine helpfulness, factual engagement, indirect requests)?

4. Why was no LLM-as-judge baseline included (e.g., prompting GPT-4 or Claude with "Is this conversation a jailbreak attempt?")? This is the deployed standard at most LLM providers and would contextualize where DisPeD sits in the practical landscape.

5. The claim that removing any persuasion stage "collapses the attack" — have you run ablation experiments on attack conversations (e.g., removing all rapport-building turns and testing whether the remaining conversation still achieves jailbreak)? This would directly validate the theoretical foundation.

6. Why 8 persuasion categories? What is the mapping from Cialdini's 6 principles or Zeng et al.'s 40 techniques to your chosen taxonomy? Why is "direct request" in a persuasion taxonomy — is making a direct request a persuasion strategy?

7. What are the 95% confidence intervals for the headline results (F1=0.91 at K=2)? With 72 test samples, each misclassification shifts F1 by approximately 2-3pp, which could make the 14pp gap less definitive.

8. The intent classification head during Stage 1 training leaks binary jailbreak/benign signal into the [CLS] embedding. Have you ablated this (persuasion-only training) to confirm the downstream GRU uses persuasion features rather than leaked intent features?

### Missing Related Work

**Multi-turn detection systems (critical omissions):**
- Llama Guard 2/3 (Meta, multi-turn capable versions)
- ShieldGemma (Google, conversation-level safety)
- WildGuard (Allen AI)
- BIID: Bidirectional Intention Inference for multi-turn jailbreak detection
- G-Guard (GCN-based multi-turn detection)
- SafeDream (safety world model + CUSUM)
- Constitutional Classifiers (Anthropic, exchange-level)

**Persuasion detection (directly relevant):**
- GLiGuard (strategy-aware compact encoder guard)
- Persuasive Fingerprint (CIKM 2025, Cialdini-based jailbreak characterization)
- Habernal & Gurevych (2016): computational argumentation/persuasion detection
- Tan et al. (2016): "Winning Arguments" — computational models of persuasion

**Discourse and dialogue analysis (foundational):**
- RST-based discourse parsing (Mann & Thompson 1988, Ji & Eisenstein 2014)
- Dialogue act classification (Stolcke et al. 2000, the SWBD-DAMSL taxonomy)
- PDTB (Prasad et al. 2008) — discourse relation classification
- Persuasion dialogue modeling (Wang et al. 2019, "Persuasion for Good")

**Red-teaming and adaptive attacks:**
- Perez et al. (2022): Red teaming language models
- Ganguli et al. (2022): Red teaming language models to reduce harms
- Mazeika et al. (2024): HarmBench
- Nasr, Carlini et al. (2025): Adaptive attacks on safety classifiers

**LLM-as-judge safety evaluation:**
- Zheng et al. (2023): MT-Bench and LLM-as-judge
- OpenAI moderation endpoint, Claude safety classifier

### Minor Issues

1. **Table 3 arithmetic error.** Crescendo strategy percentages sum to 115%, FITD to 125%, Deceptive Delight to 120%. Either a calculation error or the categories are not mutually exclusive (which must be stated). This undermines confidence in the data pipeline.

2. **No figures.** The paper has zero figures. A trajectory visualization, an F1-vs-K curve, or a strategy transition heatmap would significantly strengthen the mechanistic narrative and visual impact.

3. **Inconsistent terminology.** "Register-normalized" and "clean" are used interchangeably for the same data condition. Standardize.

4. **Generic LaTeX template.** Uses `\documentclass[11pt,a4paper]{article}` rather than the official ARR/EMNLP template. This would be desk-rejected.

5. **Incomplete bibliography entries.** Hagendorff (2026) lacks volume/page numbers. Multiple entries use "and others" instead of full author lists. Su et al. (2026) has no arXiv ID or venue URL.

6. **Section 5.5 presupposes undefined ordering.** "82% of strategy transitions move from lower-risk to higher-risk" requires a formal risk ordering in the Method section that is never provided.

7. **No Limitations section as standalone.** Limitations are buried in one paragraph within Discussion rather than a clearly labeled section (required by most venues).

### Preliminary Score: 3/6
### Confidence: 4/5

**Rationale:** The paper addresses a real problem with a sensible approach, and the evasion hierarchy experiment is clean. However, the novelty is incremental over Zeng et al. (2024), Hagendorff (2026), and Chen et al. (2025) combined. The related work is far below venue standards (14 citations, missing entire subfields). The absence of comparison against LLM-as-judge and published multi-turn defenses makes it impossible to assess practical positioning. The potentially fabricated DeepContext citation is a red flag. The central theoretical claim (structural impossibility of evasion) is asserted rather than tested. For EMNLP 2026, the paper needs substantially expanded related work, engagement with adaptive adversaries, stronger baselines, and honest novelty positioning as "operationalizing known observations" rather than "discovering a new phenomenon."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb0fc191-b824-4f0b-907e-b0e9c174b221",
  "isSidechain": true,
  "agentId": "ae301916499c8fc23",
  "requestId": "req_011Cb8YAHSb1tFwJxfF8ysBz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb61953b-c06c-4e3c-b84d-b40b67ad7455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "28a3eef2-233e-4eb5-bfe4-3efac3de241f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQSDAYpmpnnmJzQKejPw7v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 41742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 826,
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
