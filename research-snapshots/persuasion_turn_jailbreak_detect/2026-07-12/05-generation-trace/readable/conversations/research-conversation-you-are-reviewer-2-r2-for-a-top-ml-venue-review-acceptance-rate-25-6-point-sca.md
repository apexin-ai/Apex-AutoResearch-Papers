# Research conversation: You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Wea

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af0c2201172a0086d.jsonl`
- **Structured JSON:** [`9f193cca509059abfe91.json`](../../sessions/9f/9f193cca509059abfe91.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-17T17:23:57.314Z_

You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus areas are **novelty/originality** and **related work positioning**.

## Paper Summary

**Title:** DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection

The paper proposes DisPeD, a two-stage pipeline for detecting multi-turn jailbreak attacks on LLMs. It identifies a "Pragmatic Evasion Asymmetry": attackers can paraphrase surface content but cannot remove the underlying persuasion playbook (rapport building, reframing, escalation) without abandoning the attack. Stage 1 fine-tunes DeBERTa-v3-base with a multi-task objective (8-class persuasion strategy classification + binary intent classification). Stage 2 feeds resulting turn embeddings into a bidirectional GRU for conversation-level jailbreak detection.

Key claims:
1. Pragmatic Evasion Asymmetry: under adversarial paraphrasing, DisPeD degrades 3pp vs 13pp (semantic) and 18pp (lexical)
2. Early detection: F1=0.91 at K=2 turns, 14pp over baseline; zero-shot cross-attack transfer averages 16.5pp
3. Mechanistic explanation via monotonic escalation trajectories (monotonicity 0.82 vs 0.34)

## Related Work as Presented (Section 2)
Three subsections:
- **Multi-turn jailbreak attacks:** Crescendo, FITD, Deceptive Delight, Hagendorff [2026]
- **Jailbreak detection:** perplexity filters (Alon & Kamfonas 2023), input classifiers (Llama Guard, Inan et al. 2023), Bullwinkel et al. 2025 (representation space), DeepContext (Su et al. 2026)
- **Persuasion and LLM safety:** Zeng et al. 2024 (40 persuasion techniques), Chen et al. 2025 (persuasion dynamics extraction)

Total references: 12

## Method Details
- Stage 1: DeBERTa-v3-base fine-tuned with multi-task loss L = L_persuasion + λL_intent (λ=1.0)
- 8-class persuasion taxonomy from Cialdini's influence principles adapted via Zeng et al.
- Stage 2: Bidirectional GRU on [CLS] embeddings
- Baselines: TF-IDF+LR, vanilla DeBERTa+GRU, DeepContext proxy (BERT-base+GRU)

## Key Experimental Tables
- Table 4: F1 by turn budget (DisPeD vs baseline)
- Table 6: Evasion hierarchy (4 models, clean vs perturbed)
- Table 8: Scrambled label ablation
- Table 9: Cross-attack zero-shot generalization
- Table 11-12: Strategy transition analysis
- Table 13: Hard negative FPR

## Dataset
480 conversations total (240 jailbreak Crescendo, 240 benign), 72 test. Additional 72 FITD + 65 Deceptive Delight generated with Qwen3-8B.

## Your Task

Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (numbered, with specific references)
3. **Weaknesses** (numbered, with specific references)
4. **Questions for Authors** (numbered)
5. **Minor Issues** (numbered)
6. **Overall Assessment** (1 paragraph)
7. **Scores:**
   - Soundness (1-4)
   - Presentation (1-4)
   - Contribution (1-4)
   - Overall (1-6)
   - Confidence (1-5)

Focus especially on:
- Whether the "Pragmatic Evasion Asymmetry" is genuinely novel or a restatement of known observations (Zeng et al. 2024, Hagendorff 2026 already showed persuasion patterns in attacks)
- Adequacy of related work coverage (only 12 references is very thin)
- Missing comparisons to LLM-as-judge approaches, Llama Guard variants, other multi-turn detectors
- Whether the Speech Act Theory framing (Austin, Searle) adds substance or is superficial
- Whether the novelty is primarily in the conceptual framing or in the technical method (DeBERTa + GRU is standard)
- Positioning relative to Zeng et al. 2024 and Chen et al. 2025 who already study persuasion in LLM safety
- Whether "first to use persuasion-grounded representations for detection" claim is verifiable

Be rigorous and specific. Reference section/table numbers. Do not mention any tier (best/median/worst) information. Output only the review text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "f7230eef-6791-4669-b64e-43f0e576f424",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T17:23:57.316Z_

```json
{
  "parentUuid": "f7230eef-6791-4669-b64e-43f0e576f424",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
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
  "uuid": "b6845476-2edb-4b69-8241-cbc2979f4b99",
  "timestamp": "2026-05-17T17:23:57.316Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T17:24:00.053Z_



I need to read the actual paper and related materials before writing the review. Let me start by exploring the project structure and reading the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6845476-2edb-4b69-8241-cbc2979f4b99",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8Xfx8xBvfJb5nRiQoSx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "136a99c7-d566-49b1-b3b3-4bc7be2a4346",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pu7PAfgx9JTqEArWx8wYL2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8361,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8361,
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

_source line 4 · 2026-05-17T17:24:01.029Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WhAUW4KA9wh3x4f5opYLNe`</summary>

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
  "parentUuid": "136a99c7-d566-49b1-b3b3-4bc7be2a4346",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8Xfx8xBvfJb5nRiQoSx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef9b1b67-7866-41c7-a02d-23796febd4b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pu7PAfgx9JTqEArWx8wYL2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8361,
      "cache_read_input_tokens": 8255,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8361
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8361,
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

_source line 5 · 2026-05-17T17:24:01.032Z_

<details><summary>↩ Tool result · `toolu_01WhAUW4KA9wh3x4f5opYLNe`</summary>

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
  "parentUuid": "ef9b1b67-7866-41c7-a02d-23796febd4b3",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "c85aae0c-96a8-413c-acaa-6b4213909103",
  "sourceToolAssistantUUID": "ef9b1b67-7866-41c7-a02d-23796febd4b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T17:24:03.784Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01BkbARKyGZwjY8JDbB8AUHf`</summary>

```json
{
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c85aae0c-96a8-413c-acaa-6b4213909103",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgEF5X8QkTgiMVD6Aw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c04324d8-bf8e-4c51-9eaf-2ee9c189229e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvfSANhyvpicy1N6fnoR7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 16616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 7 · 2026-05-17T17:24:03.806Z_

<details><summary>↩ Tool result · `toolu_01BkbARKyGZwjY8JDbB8AUHf`</summary>

```text
{"result":"# 项目 persuasion_turn_jailbreak_detect 概况\n\n## 实验状态 (2 个)\n\n- **phase_b_full**: DONE (success) — \n- **pilot_phase_b**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **phase_b_full** (success): Persuasion-grounded DeBERTa embeddings (multi-task fine-tuned on 8-class persuasion + intent) enable significantly earlier detection of Crescendo jailbreak attacks compared to vanilla DeBERTa embeddings, especially at low K (2-3 turns) ← 基于 pilot_phase_b\n- **pilot_phase_b** (success): Persuasion-aware DeBERTa embeddings (multi-task fine-tuned) fed to Bi-GRU will outperform vanilla DeBERTa embeddings at early detection (K=2,3,5 turns) of Crescendo-style jailbreak attacks\n\n## 趋势\n成功 2 / 负向 0 / 失败 0 / 共 2\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-33183: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c04324d8-bf8e-4c51-9eaf-2ee9c189229e",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "c947e30b-3051-4974-86de-75da7bd47b0a",
  "sourceToolAssistantUUID": "c04324d8-bf8e-4c51-9eaf-2ee9c189229e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T17:24:05.203Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Md83FX1AZ1bTwPJTtPG3js`</summary>

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
  "parentUuid": "c947e30b-3051-4974-86de-75da7bd47b0a",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgEF5X8QkTgiMVD6Aw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cdbc1e0-5a06-4efd-b5f4-2a8768c86653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvfSANhyvpicy1N6fnoR7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 16616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 9 · 2026-05-17T17:24:05.227Z_

<details><summary>↩ Tool result · `toolu_01Md83FX1AZ1bTwPJTtPG3js`</summary>

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
  "parentUuid": "7cdbc1e0-5a06-4efd-b5f4-2a8768c86653",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "961d7105-c39f-4b54-a355-a52d451814a2",
  "sourceToolAssistantUUID": "7cdbc1e0-5a06-4efd-b5f4-2a8768c86653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T17:24:05.521Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Wd4MbRUfhkYLr2YsQtswXQ`</summary>

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
  "parentUuid": "961d7105-c39f-4b54-a355-a52d451814a2",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgEF5X8QkTgiMVD6Aw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3713e21-5488-450f-9ac4-3bdb6e2fa723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvfSANhyvpicy1N6fnoR7C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 16616,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1457
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 16616,
          "cache_creation_input_tokens": 1457,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1457,
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

_source line 11 · 2026-05-17T17:24:05.541Z_

<details><summary>↩ Tool result · `toolu_01Wd4MbRUfhkYLr2YsQtswXQ`</summary>

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
.claude/sessions/reviewer_d38db4c2/CLAUDE.md
.claude/sessions/reviewer_d38db4c2/AGENTS.md
ROADMAP.md
.claude/sessions/agent_f4f909a7/CLAUDE.md
.claude/sessions/agent_f4f909a7/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/director_32e62753/CLAUDE.md
.claude/sessions/director_32e62753/AGENTS.md
artifacts/dream_reports/dream_20260517T165817/best/paper_framing.md
artifacts/dream_reports/dream_20260517T165817/median/paper_framing.md
artifacts/dream_reports/dream_20260517T165817/worst/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3713e21-5488-450f-9ac4-3bdb6e2fa723",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "fc00b7ab-d3c7-4186-bd82-c19bfde5311e",
  "sourceToolAssistantUUID": "c3713e21-5488-450f-9ac4-3bdb6e2fa723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-17T17:24:08.151Z_

Let me read the paper and supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc00b7ab-d3c7-4186-bd82-c19bfde5311e",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgZZRbnmwDgffG2cNv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70754c56-acff-47cf-82a8-70a2f3135087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DStFibtK7JdZPEyxJdJbwJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 18073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
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

_source line 13 · 2026-05-17T17:24:09.098Z_

<details open><summary>🔧 Tool call — Read · `toolu_017cQERoNMRCWQu3C184dnp6`</summary>

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
  "parentUuid": "70754c56-acff-47cf-82a8-70a2f3135087",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgZZRbnmwDgffG2cNv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd46945e-2156-4b43-a30e-b86171ec0940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DStFibtK7JdZPEyxJdJbwJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 18073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
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

_source line 14 · 2026-05-17T17:24:09.329Z_

<details><summary>↩ Tool result · `toolu_017cQERoNMRCWQu3C184dnp6`</summary>

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
  "parentUuid": "bd46945e-2156-4b43-a30e-b86171ec0940",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "0a442e22-fb8d-4497-b8f9-859c3fed1c96",
  "sourceToolAssistantUUID": "bd46945e-2156-4b43-a30e-b86171ec0940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:24:10.009Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WJY6QcVMEoR7AVqUDhxwC7`</summary>

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
  "parentUuid": "0a442e22-fb8d-4497-b8f9-859c3fed1c96",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgZZRbnmwDgffG2cNv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7336e98-1b21-4209-8b38-203efa87b0e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DStFibtK7JdZPEyxJdJbwJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 18073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
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

_source line 16 · 2026-05-17T17:24:10.022Z_

<details><summary>↩ Tool result · `toolu_01WJY6QcVMEoR7AVqUDhxwC7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7336e98-1b21-4209-8b38-203efa87b0e9",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "7ca28062-82b6-43db-bab9-d7f2bdd1a501",
  "sourceToolAssistantUUID": "f7336e98-1b21-4209-8b38-203efa87b0e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:24:10.335Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016GhigfRj5dwYTGASXtxLTm`</summary>

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
  "parentUuid": "7ca28062-82b6-43db-bab9-d7f2bdd1a501",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgZZRbnmwDgffG2cNv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afb7c085-cdc3-4e82-9702-c8006c017159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DStFibtK7JdZPEyxJdJbwJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 18073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
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

_source line 18 · 2026-05-17T17:24:10.353Z_

<details><summary>↩ Tool result · `toolu_016GhigfRj5dwYTGASXtxLTm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper_framing.md\", \"content\": \"# Paper Framing — persuasion_turn_jailbreak_detect\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission)\\n- Deadline: 2026-05-25 (ARR May cycle)\\n- Track: LLM Security / Discourse and Pragmatics\\n- Commitment deadline: 2026-08-02\\n\\n## Title (Working)\\nDisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection\\n\\n## Core Insight\\nMulti-turn jailbreak attacks can easily vary lexical and semantic content of individual turns, but the discourse-level persuasion playbook (rapport → reframing → escalation) is a structural necessity for attack success. Removing any stage either fails the attack or reduces it to a single-turn attack already covered by existing defenses. DisPeD exploits this asymmetry by fine-tuning DeBERTa on persuasion strategy classification, producing turn embeddings that encode pragmatic function rather than (only) semantic content.\\n\\n## Core Claims (3)\\n\\n### Claim 1: Pragmatic Evasion Asymmetry (Theoretical + Empirical)\\nAn evasion hierarchy exists for multi-turn jailbreak detection: lexical features (easily evaded via paraphrasing) < semantic embeddings (moderate, per-turn representations kept \\\"benign\\\" per Bullwinkel et al. 2025) < pragmatic persuasion patterns (structurally difficult to evade, as the persuasion playbook is a functional prerequisite for attack success).\\n- Evidence needed: adversarial perturbation experiment showing treatment degrades less than lexical/semantic baselines under paraphrasing\\n\\n### Claim 2: Early Detection via Persuasion Grounding\\nPersuasion-grounded turn embeddings (DeBERTa fine-tuned on 8-class persuasion taxonomy + intent) enable significantly earlier detection of multi-turn jailbreaks (at K=2-3 turns) compared to vanilla semantic embeddings, because persuasion strategy transitions (rapport → authority framing) manifest before explicitly harmful content appears.\\n- Evidence needed: early detection F1 at K=2,3 turns, treatment > baseline by >= 5pp on clean data (TF-IDF < 0.75)\\n\\n### Claim 3: Monotonic Escalation Trajectory\\nAdversarial conversations exhibit a monotonic escalation trajectory in persuasion strategy space (trust → test → normalize → elicit), while benign conversations exhibit oscillatory or non-monotonic patterns. This distinction is the mechanistic basis for Claims 1-2.\\n- Evidence needed: strategy transition matrix visualization, trajectory analysis comparing jailbreak vs benign\\n\\n## Story Spine\\n\\n**Problem**: Multi-turn jailbreak attacks (Crescendo, FITD, Deceptive Delight) distribute adversarial intent across individually benign turns. Bullwinkel et al. (2025) show per-turn representations are deliberately kept in a \\\"benign\\\" region, causing representation-level defenses to fail with a 50-point ASR gap. DeepContext (2026) tracks generic semantic drift but confuses benign conversational evolution with adversarial manipulation.\\n\\n**Gap**: Existing detectors operate at the lexical or semantic level where attacks deliberately hide. No published work combines persuasion-grounded turn representations with temporal sequence modeling for multi-turn jailbreak detection.\\n\\n**Our angle**: We identify the Pragmatic Evasion Asymmetry. The persuasion playbook (rapport → reframing → escalation) is a structural necessity for multi-turn attack success. Unlike lexical or semantic features, pragmatic persuasion patterns cannot be evaded without abandoning the attack itself. DisPeD fine-tunes DeBERTa on an 8-class persuasion taxonomy to produce pragmatic-aware turn embeddings, then models the temporal strategy sequence with a GRU to detect the characteristic escalation trajectory.\\n\\n**Headline result**: \\\"DisPeD detects Crescendo-style jailbreaks at K=2 turns with F1=X vs Y for vanilla semantic baselines (+Z pp). Under adversarial paraphrasing that removes lexical cues, DisPeD maintains F1=W while lexical baselines degrade by V pp.\\\"\\n\\n## Architecture (Simplified for MVE)\\n\\nSingle-track with persuasion grounding (full dual-track in future work):\\n1. **Stage 1**: DeBERTa-v3-base fine-tuned on multi-task objective: 8-class persuasion strategy classification + binary jailbreak-intent classification\\n2. **Stage 2**: Bi-GRU over DeBERTa [CLS] embeddings for conversation-level binary classification\\n3. **Baseline**: Same pipeline but with vanilla (not fine-tuned) DeBERTa embeddings\\n\\n## Venue Fit Risks\\n- EMNLP 2026 LLM Security track: strong fit (dedicated track, high visibility)\\n- Discourse/Pragmatics reviewers may want more linguistic rigor: ground taxonomy in PAP (ACL 2024), Hagendorff (Nature Comm 2026), Cialdini principles, Speech Act Theory (Austin 1962, Searle 1969)\\n- Safety reviewers expect multiple attack types: need >= 2 attack families\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Lexical Shortcut (CRITICAL, must address pre-submission)\\nTF-IDF=1.0 on current data means lexical features alone perfectly separate classes. Must show the model works on data without lexical shortcuts.\\n- Mitigation: (a) register-normalize jailbreak data to match benign register, verify TF-IDF < 0.75, retrain; (b) adversarial perturbation evaluation (Claim 3)\\n\\n### RC2: Small Dataset\\n480 samples is small for a detection paper.\\n- Mitigation: (a) statistical significance via bootstrap CI or paired tests; (b) cross-validation; (c) focus narrative on proof-of-concept for the principle, not SOTA numbers\\n\\n### RC3: Single Attack Type (Crescendo Only)\\nNeed generalization evidence.\\n- Mitigation: generate FITD-style and Deceptive Delight-style conversations using existing pipeline\\n\\n### RC4: Strategy Label Confound (M004)\\nBenign turns hardcoded to strategy=7 creates shortcut for treatment model.\\n- Mitigation: (a) fix labeling (use \\\"none\\\"/9th class); (b) scrambled-label ablation\\n\\n### RC5: No DeepContext Comparison\\nPaper positions against DeepContext but no reproduction.\\n- Mitigation: vanilla DeBERTa → GRU is a fair proxy baseline (same architecture, only difference is persuasion grounding). Note DeepContext has no public code. If time allows, attempt reproduction as P1.\\n\\n### RC6: Interpretability Claims Without Human Eval\\nStrategy sequence outputs claimed interpretable but not evaluated.\\n- Mitigation: strategy transition matrix visualization (P1). Full human eval is future work given timeline constraints.\\n\\n## Scope Boundary\\n- IN: persuasion-mediated multi-turn attacks (Crescendo, FITD, Deceptive Delight, social engineering jailbreaks)\\n- OUT (acknowledged limitation): pure information accumulation attacks, token smuggling, single-frame roleplay\\n- The semantic GRU track provides coverage for out-of-scope attack types as a safety net\\n\\n## Theoretical Grounding\\n- Bullwinkel et al. (arXiv 2507.02956): per-turn representations kept \\\"benign\\\" by multi-turn attacks\\n- Speech Act Theory (Austin 1962, Searle 1969): existing detectors work at locutionary act level, DisPeD at illocutionary act level\\n- PAP (Zeng et al., ACL 2024): 40 persuasion techniques for jailbreaking\\n- Hagendorff (Nature Communications 2026): identifiable persuasion strategies in 97% ASR attacks\\n- \\\"How Do LLMs Persuade?\\\" (arXiv 2508.05625): persuasion dynamics extractable from turn-level representations\\n\", \"total_chars\": 7114, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afb7c085-cdc3-4e82-9702-c8006c017159",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "d7d05ef3-8b62-470a-a7f0-9c48075be4d9",
  "sourceToolAssistantUUID": "afb7c085-cdc3-4e82-9702-c8006c017159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-17T17:24:13.517Z_

Now let me read the idea brief and any additional experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7d05ef3-8b62-470a-a7f0-9c48075be4d9",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgvSnBNcqM7QbpPMzH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1262ffb9-dffb-40f0-a283-cc6447e158fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgNZXEbyAm64E4kPSQVtxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14826,
      "cache_read_input_tokens": 19216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14826,
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

_source line 20 · 2026-05-17T17:24:14.005Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DQFyTxuqheWQ8tYHFo9RN3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1262ffb9-dffb-40f0-a283-cc6447e158fc",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgvSnBNcqM7QbpPMzH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "457dc40a-d942-4765-93b2-ff5540ff2c38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgNZXEbyAm64E4kPSQVtxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14826,
      "cache_read_input_tokens": 19216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14826,
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

_source line 21 · 2026-05-17T17:24:14.482Z_

<details><summary>↩ Tool result · `toolu_01DQFyTxuqheWQ8tYHFo9RN3`</summary>

```text
1	# Idea Brief: Beyond Intent Drift: Persuasion-Grounded Turn Representations for Multi-Turn Jailbreak Detection
2	
3	
4	- **Idea ID**: `idea_008`
5	- **Created**: 2026-05-17
6	- **Approved**: 2026-05-17
7	- **Source**: foreign:be-idea-gen-0515-5
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026; commitment deadline: August 2, 2026; conference: October 24-29, Budapest) — LLM Security is listed as a topic area within the main conference, with additional relevance to Discourse and Pragmatics, NLP Applications, and Ethics/Bias/Fairness topic areas
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (11 days from today 2026-05-14). Track: LLM Security.
14	
15	Direction: LLM safety robustness — defense methods against jailbreaking, adversarial prompt attacks, and safety alignment degradation. In-scope: robust safety training that resists adaptive attacks, automated red-teaming frameworks for systematic vulnerability discovery, safety-aware decoding or filtering at inference time, detecting and mitigating safety degradation when models are fine-tuned or distilled, multi-turn attack defense, tool-use and agentic safety. NOT limited to text — agentic tool-call safety and multi-modal attack surfaces welcome.
16	
17	Contribution type: METHOD ONLY. Must propose a concrete defense algorithm, detection pipeline, or training recipe — not just a new attack or red-teaming dataset. Attack + defense paired contributions OK if defense is the primary contribution.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Safety research is mostly inference-heavy — budget for evaluation across multiple attack suites, not large-scale pretraining.
21	2. Time: ≤11 days. Build on existing open safety benchmarks and models (Llama-3-Guard, ShieldGemma, Qwen3, DeepSeek-R1 distills). Use established attack libraries (HarmBench, JailbreakBench, StrongREJECT) for evaluation.
22	3. Eval: Attack Success Rate (ASR) reduction on HarmBench, JailbreakBench, AdvBench; safety score on WildGuard/Aegis; utility preservation on MT-Bench/MMLU (defense must not kill helpfulness).
23	
24	This is a NEW dedicated track at EMNLP 2026 — high visibility, growing fast, few established defense methods. 2026 research shows reasoning models can jailbreak other models at 97% success; defense lags far behind attack. Look for: inference-time safety filters that adapt to attack patterns, representation-level safety mechanisms (circuit-based), robust alignment under fine-tuning distribution shift, defense against multi-turn and agentic attacks. Avoid: yet another jailbreak attack without defense contribution, prompt-template-only defenses, safety classifiers without adversarial robustness guarantees.
25	
26	## Core Problem
27	
28	Multi-turn jailbreak attacks remain one of the most persistent threats to deployed LLMs, distributing adversarial intent across individually benign-seeming messages that exploit conversational dynamics to gradually steer models past safety boundaries. The state-of-the-art dedicated multi-turn detector, DeepContext (arXiv 2602.16935, Feb 2026), models this threat as generic intent drift: it embeds each turn with fine-tuned BERT, applies task-attention weighted pooling, and feeds the resulting sequence through a 3-layer GRU (2048 hidden units) with hybrid residual connections to detect when the conversation trajectory shifts toward harmful territory. This approach achieves F1=0.84 on standard multi-turn benchmarks with sub-20ms inference on a T4 GPU, establishing a strong baseline. However, DeepContext's reliance on undifferentiated semantic drift creates three fundamental limitations. (1) High false-positive rates on naturally drifting conversations: brainstorming sessions, Socratic dialogues, creative writing, and complex tutoring all exhibit substantial topic drift, triggering drift detectors even though no manipulation is occurring. (2) Zero interpretability: the 2048-dimensional GRU hidden state provides an opaque risk score with no actionable threat intelligence—security teams cannot see which manipulation strategy is being employed or at which turn the attack transitions from rapport-building to exploitation. (3) The acknowledged 'glass cannon' effect—strong performance on known attack templates but fragile generalization to novel strategies—because the model learns surface-level correlates of attacks (lexical drift patterns) rather than the underlying causal mechanism (adversarial persuasion). A recent representation engineering analysis (Bullwinkel et al., arXiv 2507.02956, Microsoft Research, Jun 2025) provides a mechanistic explanation for why per-turn representation-level defenses fundamentally struggle with multi-turn attacks: Crescendo keeps model outputs in a 'benign' region of representation space, with harmful classification dropping sharply after just 2 turns. Circuit breakers—trained to reroute harmful single-turn representations—achieve only 54.2% ASR defense (vs. 3.8% on single-turn) because multi-turn attack representations are 'sufficiently different from single-turn representations.' This finding demonstrates that the information needed to detect multi-turn attacks is not reliably present in per-turn representations of semantic content; it resides instead in the discourse-level pattern of how turns relate to each other—specifically, in the adversarial persuasion playbook orchestrating the conversation. Meanwhile, BIID (arXiv 2509.22732) achieves near-0% ASR through bidirectional LLM-based intention inference, but imposes 2+ full LLM reasoning passes per turn with latency estimated at several seconds (no published latency analysis exists; this estimate is based on the computational requirements of two full LLM forward passes per turn and requires independent verification). GLiGuard (arXiv 2605.07982, May 2026) demonstrates that compact 300M-parameter encoders can detect 11 jailbreak strategies and 14 harm categories in a single pass with 16x speedup over 7B decoder guards, but operates only on single inputs without temporal modeling. XGuard-Train (arXiv 2504.13203) achieves 48.3% vulnerability reduction through safety training data (30K multi-turn conversations), but as a training-time defense, it is model-specific and inapplicable to closed-source or already-deployed models. The core problem is therefore not architectural—encoder-plus-recurrent designs are well-established for this task—but representational: the features extracted from each turn do not encode the information most relevant to distinguishing adversarial manipulation from benign conversational evolution, and as Bullwinkel et al. show, per-turn semantic representations are actively misleading because multi-turn attacks are designed to keep them benign. What turn-level representation would capture the causal mechanism of multi-turn attacks at the discourse level, above the representation space where attacks deliberately hide?
29	
30	## Opportunity / Why Now
31	
32	Four converging findings define a precise representational opportunity. First, Bullwinkel et al. (arXiv 2507.02956, Microsoft Research, Jun 2025) established that multi-turn jailbreaks succeed specifically because they keep per-turn representations in a 'benign' region of representation space, explaining why representation-level defenses (circuit breakers) fail with a 50-percentage-point generalization gap. This finding has a critical implication: effective multi-turn detection requires features that operate above the per-turn representation level—at the discourse level where the manipulation playbook is visible even when individual turns appear benign. Second, 'How Do LLMs Persuade?' (arXiv 2508.05625) demonstrated that linear probes applied to intermediate transformer representations can reliably detect persuasion strategies, track persuasion success trajectories, and identify personality-adapted persuasion across multi-turn conversations—faster than prompting-based approaches and with competitive accuracy. Although this work was not applied to jailbreak detection, it empirically validates a crucial premise: the specific persuasion mechanisms operating in a conversation are extractable from turn-level representations and computationally tractable. Third, Hagendorff (Nature Communications 2026) showed that reasoning-model attackers achieving 97% ASR employ identifiable persuasion strategies—flattery/rapport-building (84.75%), educational/research framing (68.56%), hypothetical scenarios (65.67%), verbose technical jargon (44.42%)—that 'largely align with those predefined in the system prompt,' creating predictable temporal discourse signatures. Multi-turn jailbreaks succeed through specific persuasion playbooks: rapport THEN reframing THEN escalation, where each step individually appears benign but the sequence constitutes manipulation. Fourth, the Persuasive Fingerprint work (Alizadeh Noughabi et al., CIKM 2025, arXiv 2510.21983) confirmed that Cialdini's persuasion principles computationally characterize jailbreak susceptibility, establishing that persuasion structure is the right analytical lens for understanding jailbreaks. The specific representational gap, now mechanistically grounded by Bullwinkel et al.: DeepContext's generic drift features operate at the same representation level where multi-turn attacks deliberately hide—they see 'the conversation is changing' but cannot distinguish natural evolution (brainstorming, creative collaboration) from adversarial manipulation (rapport→reframing→escalation) because both produce benign-looking per-turn representations. Persuasion-grounded features operate at the discourse level, seeing the specific manipulation playbook being executed even when each turn's semantic representation appears benign. This distinction should enable three concrete improvements: (a) earlier detection—persuasion strategy transitions (e.g., shift from rapport to authority framing) manifest before any explicitly harmful content appears, creating a detection window invisible to drift-only or representation-level systems; (b) lower false-positive rates—benign conversations that naturally drift (high drift magnitude) use qualitatively different persuasion distributions than adversarial conversations (no escalation pattern, no strategic framing shifts); (c) native interpretability—detected threats are explained in terms of named persuasion strategies and their temporal sequence rather than opaque drift magnitudes. GLiGuard's success with single-turn strategy detection validates that compact encoders can learn strategy-level features; DisPeD extends this to the temporal domain. DeepContext's own future-work section identifies 'dual-stream architecture to separate benign functional intent from adversarial steering' as a promising direction—DisPeD directly pursues this line with the critical addition of persuasion grounding.
33	
34	## Landscape (SOTA & Limitations)
35	
36	DeepContext (arXiv 2602.16935, Feb 2026): Primary baseline and most directly comparable system. Fine-tuned BERT encoder with task-attention weighted pooling, 3-layer GRU (2048 hidden), hybrid residual connection concatenating projected hidden state with raw embeddings. Tracks generic intent drift. F1=0.84 on multi-turn benchmarks, sub-20ms on T4 GPU. Training: 437K sequences (~20% malicious). Acknowledged limitations: 'glass cannon' effect (overfits to known patterns), false positives in function-calling contexts, no interpretability (opaque 2048-dim hidden state). No adversarial robustness evaluation. Future work identifies dual-stream architecture as promising direction. We candidly acknowledge that DisPeD's Track B (DeBERTa + GRU over semantic embeddings) is architecturally similar to DeepContext with an upgraded encoder; the contribution lies in Track A's persuasion-strategy sequence modeling, the cross-attention fusion, and the empirical demonstration that persuasion-grounded representations outperform generic drift features. Bullwinkel et al. (arXiv 2507.02956, Microsoft Research, Jun 2025): 'A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks.' Uses representation reading (MLP probes on intermediate activations, 0.997-0.999 test accuracy) and PCA visualization to show that Crescendo keeps model outputs in a 'benign' region of representation space, with harmful classification dropping sharply from k=1 to k=2 turns. Circuit breakers achieve only 54.2% ASR defense on multi-turn (vs. 3.8% on single-turn), a 50-point generalization gap, because Crescendo representations are 'sufficiently different from single-turn representations.' Tested on Llama-3-8B-Instruct and its circuit-breaker variant. Critically important for DisPeD's theoretical argument: this paper mechanistically explains why per-turn representation-level features are insufficient—attacks are designed to keep them benign—and why discourse-level features (persuasion strategy sequences) are needed. DisPeD's approach directly addresses the gap Bullwinkel et al. identify: rather than trying to detect harmful per-turn representations (which multi-turn attacks suppress), we detect the adversarial persuasion playbook operating above the representation level. GLiGuard (arXiv 2605.07982, May 2026): State-of-the-art single-turn guard. 300M-parameter schema-conditioned bidirectional encoder adapted from GLiNER2, detecting 11 jailbreak strategies and 14 harm categories in a single non-autoregressive forward pass. 16x higher throughput and 17x lower latency than 7B decoder guards; competitive F1 with 7-27B models. Single-input only—no temporal modeling—making it complementary to multi-turn approaches. Included as baseline to characterize the single-turn vs. multi-turn detection gap. BIID (arXiv 2509.22732, Sep 2025): Bidirectional intention inference combining forward request analysis with backward response retrospection. Near-0% ASR on MHJ. Training-free but requires target LLM to self-analyze (2+ full LLM reasoning passes per turn). No published latency analysis; we estimate several seconds per turn based on computational requirements of two full LLM forward passes and plan to independently measure this latency as part of evaluation. Strongest known ASR but no interpretability and untested adversarial robustness. G-Guard (arXiv 2507.07146, Jul 2025): Attention-aware GCN over entity graphs via GraphRAG. Merges turns into global graph via entity deduplication, losing temporal ordering. F1: 1.00/0.87 on HarmBench. Acknowledges 'loss of potentially important contextual information' from aggressive node pruning. XGuard-Train (arXiv 2504.13203, Apr 2025): Training-time defense using collaborative multi-agent framework to generate 30K adversarial conversations. 48.3% vulnerability reduction against X-Teaming attacks, 38.5% against other multi-turn jailbreaks, while mostly preserving general capabilities. Fundamentally complementary to inference-time detection: model-specific, requires fine-tuning access, inapplicable to closed-source models. DisPeD and XGuard-Train can be composed—XGuard-Train hardens the model, DisPeD monitors for attacks that evade the hardening. Concurrent work (acknowledged): Rafiei Asl et al. (ODU/UVA, CCI-funded) are developing a defense against persuasion-based multi-turn jailbreaks using reinforcement learning-driven defensive architectures that dynamically adjust model responses. No preprint published as of May 2026. Their prior work—NEXUS (EMNLP 2025) and HarmNet (arXiv 2510.18728)—focuses on attack frameworks. The RL-based approach is fundamentally different from DisPeD: it is a training-time, model-specific defense that modifies model behavior through RL-based response adjustment, requiring fine-tuning access. DisPeD is an inference-time, model-agnostic detector that monitors conversation patterns externally, applicable to closed-source models via API wrapping. The two approaches are complementary: RL-based response adjustment hardens the model; DisPeD detects attacks that evade the hardening and provides interpretable threat intelligence. 'How Do LLMs Persuade?' (arXiv 2508.05625): Linear probes detect persuasion strategies, success trajectories, and personality-adapted persuasion in multi-turn conversations, faster than prompting-based approaches. Not applied to jailbreak detection. Provides theoretical and empirical grounding for DisPeD's core hypothesis. Hagendorff (Nature Communications 2026): 97% ASR from reasoning-model attackers; identifiable persuasion strategies (flattery 84.75%, educational framing 68.56%, hypothetical scenarios 65.67%, technical jargon 44.42%). Demonstrates persuasion playbooks are the mechanism of sophisticated multi-turn attacks. PAP (Zeng et al., ACL 2024): 40 persuasion techniques; Targeted Summarization defense reduces single-turn ASR to 2% but degrades MT-Bench. Single-turn only. Persuasive Fingerprint (Alizadeh Noughabi et al., CIKM 2025, arXiv 2510.21983): Cialdini's 7 principles characterize jailbreak susceptibility. No defense proposed. SafeDream (arXiv 2604.16824, Apr 2026): Safety world model with CUSUM detection; F1=0.891, FPR=7.9%; requires white-box hidden state access. Nasr, Carlini et al. (arXiv 2510.09023, Oct 2025): Systematically bypassed 12 single-input classifiers with >90% ASR under adaptive attack. All 12 tested defenses were single-turn/single-input classifiers. Establishes necessity of robustness evaluation for any classifier-based defense. Guarding the Guardrails (arXiv 2510.13893): Taxonomy of 7 jailbreak strategy families including persuasion, with 1,364 multi-turn Italian dialogues annotated with taxonomy. LLM-based detection via taxonomy-guided prompting. Peak+Accumulation (arXiv 2602.11247): Zero-GPU proxy scoring; 90.8% recall. Defensive M2S (arXiv 2601.00454): Compresses multi-turn to single-turn; 93.8% recall. Constitutional Classifiers (arXiv 2501.18837, Anthropic): Exchange-level classifier; 4.4% ASR; proprietary. MultiBreak (arXiv 2605.01687): 10,389-sample multi-turn benchmark. SoK: Evaluating Jailbreak Guardrails (arXiv 2506.10597, Jun 2025; IEEE S&P 2026): Comprehensive evaluation framework for jailbreak guardrails; taxonomy across six dimensions. FITD (EMNLP 2025): Foot-in-the-door multi-turn attack; demonstrates persuasion structure drives attacks. No published work combines persuasion-grounded turn representations (not generic drift features) with temporal sequence modeling for multi-turn jailbreak detection. The contribution is representational, not architectural.
37	
38	## Proposed Approach
39	
40	We propose DisPeD (Discourse-level Persuasion Detection), honestly framed as persuasion-grounded DeepContext with dual-track modeling, adversarial robustness evaluation, and interpretability. The primary contribution is demonstrating that persuasion-grounded turn representations are fundamentally better features for multi-turn jailbreak detection than generic intent-drift features, validated through rigorous ablation against a reproduced DeepContext baseline. We frame DisPeD's value as a multi-metric Pareto improvement: rather than claiming dominance on any single axis, we demonstrate that persuasion grounding simultaneously advances detection performance, early detection capability, false-positive discrimination, interpretability, and adversarial robustness—a combination no existing system achieves.
41	
42	**Theoretical Grounding from Representation Engineering:**
43	Bullwinkel et al. (arXiv 2507.02956) mechanistically explain why generic semantic features are insufficient: multi-turn attacks deliberately keep per-turn representations in a 'benign' region of representation space, causing circuit breakers and other representation-level defenses to fail with a 50-point ASR generalization gap. DisPeD addresses this by operating at the discourse level—detecting the adversarial persuasion playbook that orchestrates the conversation—rather than at the per-turn representation level where attacks deliberately hide. The key insight: even when each turn's semantic representation appears benign (as Bullwinkel et al. show it will), the sequence of persuasion strategies across turns (rapport→reframing→escalation) constitutes a detectable manipulation fingerprint.
44	
45	**Positioning Against DeepContext:**
46	We explicitly acknowledge that DisPeD's temporal architecture (encoder + GRU) shares the same paradigm as DeepContext. The contribution is not a new architecture but a new representation. Concretely: we show that grounding the encoder in persuasion strategy classification (Track A) and fusing discrete strategy signals with continuous semantic signals (cross-attention fusion) yields significant improvement over generic intent-drift detection, while the dual-track design provides adversarial robustness and interpretability that single-track architectures lack. The ablation design is structured to isolate each contribution precisely.
47	
48	**Positioning Against XGuard-Train and Concurrent RL-Based Defenses:**
49	XGuard-Train is a training-time, model-specific defense requiring fine-tuning access. The concurrent ODU/UVA project (Rafiei Asl et al., CCI-funded) pursues RL-based defensive architectures that dynamically adjust model responses—also training-time and model-specific. DisPeD is inference-time, model-agnostic, and deployable on closed-source models via API wrapping. DisPeD provides interpretable post-hoc explanations (named persuasion strategy sequences) that neither training-time alignment nor RL-based response adjustment can provide. These approaches are complementary and composable: training-time defenses harden the model; DisPeD monitors conversations for novel attacks that evade the hardening and provides security teams with actionable threat intelligence.
50	
51	**Phase 1 – Persuasion Strategy Annotation (~40 H100-hours):**
52	Develop a persuasion strategy taxonomy grounded in PAP's social-science categories, Hagendorff's empirical findings, and Cialdini's principles. Categories: (1) rapport/flattery, (2) authority/educational framing, (3) hypothetical scenario construction, (4) reframing/normalization, (5) emotional leverage/urgency, (6) identity manipulation/role assignment, (7) incremental escalation, (8) benign/neutral. Annotate turn-level persuasion strategies on existing multi-turn jailbreak datasets (MHJ, XGuard-Train subset, SafeDialBench, MultiBreak) using GPT-4-class models with taxonomy-guided prompting, validated by expert review on a 500-sample stratified subset (targeting >0.75 Cohen's kappa). Generate additional adversarial conversations (~1,000) using reasoning-model attackers (DeepSeek-R1-Distill-14B, Qwen3-30B-A3B) against 3 targets, extracting persuasion labels from attacker CoT traces. Supplement with benign conversations enriched with natural persuasion: tutoring, customer service, brainstorming, debate, and creative collaboration—specifically selected to exhibit high topic drift with benign persuasion distributions for false-positive calibration. Target: ~30K annotated conversations.
53	
54	**Phase 2 – Persuasion-Grounded Encoder (~25 H100-hours):**
55	Fine-tune DeBERTa-v3-base on a multi-task objective: (a) 8-way persuasion strategy classification, and (b) binary jailbreak-intent classification. The multi-task training produces turn embeddings (penultimate-layer [CLS] representation) that encode both semantic content and the specific persuasion mechanism in play, contrasting with DeepContext's BERT embeddings that encode only generic semantic content. DeBERTa-v3-base is chosen over BERT-base for its disentangled attention mechanism, which improves fine-grained token-level discrimination relevant to distinguishing subtle persuasion strategies.
56	
57	**Phase 3 – Dual-Track Temporal Model (~20 H100-hours):**
58	Track A (Interpretable Persuasion Sequence): GRU over discrete persuasion-strategy probability distributions (8-dim per turn) concatenated with per-turn harmfulness scores from a standalone guard (Qwen3Guard or WildGuard). Detects characteristic attack playbooks: rapport→reframing→escalation. Provides human-readable explanations ('Turn 1-3: rapport-building; Turn 4: authority reframing; Turn 5-6: incremental escalation'). Track B (Robust Semantic Content): GRU over continuous DeBERTa turn embeddings concatenated with harmfulness scores. Architecturally similar to DeepContext with DeBERTa; captures semantic evolution beyond fixed taxonomy categories. Cross-Attention Fusion: At each timestep, bidirectional cross-attention between Track A and Track B hidden states allows the tracks to exchange information. Track A informs Track B about the manipulation context of observed semantic shifts (distinguishing benign drift from adversarial steering); Track B provides Track A with semantic grounding to disambiguate persuasion strategies. Final classification via learned late fusion of track outputs.
59	
60	**Mechanistic Hypothesis for Why Persuasion Labels Beat Generic Drift (now grounded in Bullwinkel et al.):**
61	Bullwinkel et al. show that multi-turn attacks keep per-turn representations in a 'benign' region—the representation space is adversarially manipulated. Generic drift detection operates in this same manipulated space: it sees 'the conversation is changing' but the direction of change appears benign. Persuasion-aware detection operates at a different level of abstraction: it classifies the discourse function of each turn (rapport-building, authority framing, reframing) rather than its semantic content. Even when a turn's semantic representation is benign (as Bullwinkel et al. show it will be during Crescendo), its discourse function within the conversation can reveal adversarial intent. This enables: (a) earlier detection—detecting rapport→authority framing transition before any harmful content appears (while generic drift and representation-level defenses see only benign signals); (b) better false-positive discrimination—benign conversations that also 'drift' (brainstorming, creative writing, complex tutoring) exhibit flat or random persuasion distributions rather than the escalatory persuasion sequences characteristic of attacks; (c) interpretable explanations—naming the strategy rather than reporting an opaque drift magnitude.
62	
63	**Phase 4 – Comprehensive Ablation-Driven Evaluation (~45 H100-hours):**
64	
65	*Multi-Metric Pareto Evaluation Framework:*
66	We pre-commit to reporting a multi-dimensional comparison table across six axes: (1) F1 detection accuracy, (2) turns-before-compliance (early detection), (3) FPR on benign high-drift conversations, (4) interpretability score (human evaluation), (5) inference latency, and (6) adaptive attack robustness. DisPeD's claimed value is as a Pareto improvement across these dimensions: BIID achieves the strongest ASR reduction but at ~100x latency with no interpretability; DeepContext matches latency but provides no interpretability, no FPR discrimination, and no adversarial robustness; SafeDream achieves early detection but requires white-box hidden state access. Even modest F1 gains become significant when accompanied by clear wins on interpretability, FPR, and early detection. If F1 gains over DeepContext are ≤2 points, the paper's primary narrative shifts to the multi-metric advantages while honestly reporting the F1 result.
67	
68	*Primary Ablation (DeepContext comparison):*
69	(A0) DeepContext reproduction: BERT-base + task-attention pooling + 3-layer GRU (2048 hidden), trained on generic intent-drift labels, targeting reproduction of reported F1=0.84. (A1) Encoder upgrade: DeBERTa-v3-base replacing BERT-base in the DeepContext architecture (same GRU, same drift task), isolating encoder contribution. (A2) Persuasion grounding: DeBERTa-v3-base with multi-task persuasion training in single-track GRU (Track B only), isolating persuasion-representation contribution. (A3) Full DisPeD: dual-track with cross-attention fusion. This four-condition ablation ensures every claimed contribution is empirically justified relative to the most relevant baseline.
70	
71	*Detection performance:* Precision/recall/F1 on MHJ, MultiBreak, SafeDialBench, XGuard-Train test split, and reasoning-model-attacker test set. Per-condition (A0-A3) to trace contribution sources.
72	
73	*Early detection:* Turns before compliance, per condition. Hypothesis: persuasion-grounded conditions (A2, A3) detect earlier because persuasion patterns manifest before harmful content. We pre-commit to reporting the A1-vs-A2 gap on this metric as a primary result, since this most cleanly isolates the value of persuasion grounding independent of encoder quality.
74	
75	*False-p
76	
77	## Resource Estimate
78	
79	- **auto_research**: {'claude_api_cost': '$250-400 (heavy orchestration: annotation pipeline, 4-condition ablation management, multi-benchmark evaluation, adaptive attack generation across ~4000-6000 turns)', 'estimated_gpu_cost': '$400-500', 'gpu_hours': '~160h H100 (broader annotation coverage, full 4-condition ablation with multiple seeds, comprehensive adaptive attack evaluation, all benchmark evaluations, latency benchmarking, GLiGuard baseline)', 'gpu_utilization': 'High (~75-85%): continuous experiment scheduling across annotation, training, and evaluation pipelines', 'risk_note': "Primary risk: if DeepContext reproduction fails or if persuasion-grounded representations show only marginal improvement (<=2 F1 points) over encoder-upgraded DeepContext (A1 vs A2), the paper reframes around multi-metric Pareto improvement. Pre-committed secondary metrics (turns-before-compliance, FPR reduction, interpretability) are expected to show clearer advantages even if F1 gains are modest, since persuasion patterns manifest before harmful content (early detection) and benign conversations lack escalatory persuasion sequences (FPR). Contingency: if MVE (8 days) shows persuasion grounding has no advantage on ANY metric, this constitutes a well-documented negative result with theoretical analysis of why (contributing to the field's understanding of multi-turn detection representations).", 'speed_bottleneck': 'DeepContext reproduction without code release; sequential multi-turn conversation generation (~50-100s/conversation); API rate limits for closed-source target evaluation', 'team': '0 (initial setup: persuasion taxonomy, DeepContext reproduction script, benchmark selection, adaptive attack specifications)', 'timeline_tiered': {'full_experiment': '11 days with 8x H100 cluster — A0-A3 on 5+ benchmarks, 3 seeds, ~30K annotations, adaptive attacks, all baselines, interpretability evaluation', 'minimum_viable_experiment': '8 days with 8x H100 cluster — A0+A3 on MHJ+MultiBreak, single seed, ~15K annotations, core metrics (F1, turns-before-compliance, FPR, latency)', 'phase_overlap': 'Annotation (days 1-4), encoder training (days 3-6, using early batches), DeepContext reproduction (days 1-5, parallel), dual-track training (days 5-8), evaluation (days 7-11 with MVE conditions first)'}}
80	- **human_in_loop**: {'claude_api_cost': '$150-250 (experiment orchestration, annotation assistance, ablation analysis across ~1500-2500 turns)', 'estimated_gpu_cost': '$350-425', 'gpu_hours': '~140h H100 (agent optimizes annotation quality, encoder hyperparameters, cross-attention design, DeepContext reproduction fidelity, adaptive attack design)', 'gpu_utilization': 'Moderate-High (~60-70%): agent queues experiments; human reviews persuasion taxonomy, annotation agreement metrics, and ablation results ~1x/day', 'risk_note': 'DeepContext reproduction is critical path: if we cannot reproduce F1=0.84 (paper provides no code release), the ablation story weakens. Mitigation: contact authors for implementation details; if reproduction gap >3 F1 points, report both reproduced and original numbers with discussion of discrepancy, and pivot to A2-vs-A3 comparison. Persuasion annotation ambiguity estimated at ~10-15% at strategy boundaries; mitigated by multi-task training that uses both discrete labels and continuous embeddings.', 'team': '1 researcher, ~30min/day reviewing persuasion annotations, DeepContext reproduction fidelity, ablation deltas, and interpretability outputs', 'timeline': '4-5 weeks'}
81	- **manual**: {'estimated_gpu_cost': '$325-400 at ~$2.50/hr H100', 'gpu_hours': '~130h H100 (persuasion annotation with GPT-4-class models: ~40h, DeBERTa multi-task training: ~25h, dual-track GRU training: ~20h, comprehensive ablation evaluation with DeepContext reproduction + baselines: ~45h)', 'gpu_utilization': 'Moderate (~50-60%): annotation is sequential per conversation; training is standard fine-tuning; evaluation is parallelizable across conditions', 'team': '2 researchers (1 NLP/discourse analysis lead, 1 safety/ML engineer) + 3 security practitioners for interpretability evaluation (4-6 hours each)', 'timeline': '2-3 months'}
82	
83	## Key References
84	
85	- DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs (arXiv 2602.16935, Feb 2026) — PRIMARY BASELINE: BERT+GRU intent-drift detector, F1=0.84, sub-20ms T4
86	- A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks (Bullwinkel et al., arXiv 2507.02956, Microsoft Research, Jun 2025) — shows multi-turn attacks keep representations 'benign', circuit breakers fail with 50-point gap; THEORETICAL FOUNDATION for discourse-level features
87	- GLiGuard: Schema-Conditioned Classification for LLM Safeguard (arXiv 2605.07982, May 2026) — 300M encoder, 11 jailbreak strategies + 14 harm categories, single-turn only, 16x faster than 7B guards
88	- How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations (arXiv 2508.05625) — validates persuasion dynamics are extractable from turn-level representations
89	- Large reasoning models are autonomous jailbreak agents (Hagendorff et al., Nature Communications 2026) — 97% ASR via identifiable persuasion strategies
90	- Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks (BIID, arXiv 2509.22732, Sep 2025) — near-0% ASR, no published latency analysis
91	- X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents / XGuard-Train (arXiv 2504.13203, Apr 2025) — training-time defense, 30K conversations, 48.3% vulnerability reduction
92	- Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak (G-Guard, arXiv 2507.07146, Jul 2025)
93	- How Johnny Can Persuade LLMs to Jailbreak Them (PAP, Zeng et al., ACL 2024) — 40 persuasion techniques, single-turn
94	- Uncovering the Persuasive Fingerprint of LLMs in Jailbreaking Attacks (Alizadeh Noughabi et al., CIKM 2025, arXiv 2510.21983) — Cialdini's principles for jailbreak analysis
95	- The Attacker Moves Second (Nasr, Carlini et al., arXiv 2510.09023, Oct 2025) — adaptive attacks bypass 12 single-input classifiers with >90% ASR
96	- Intention Analysis Makes LLMs A Good Jailbreak Defender (Zhang et al., COLING 2025, arXiv 2401.06561)
97	- SafeDream: Safety World Model for Proactive Early Jailbreak Detection (arXiv 2604.16824, Apr 2026)
98	- Guarding the Guardrails: A Taxonomy-Driven Approach to Jailbreak Detection (arXiv 2510.13893) — 7 jailbreak strategy families, multi-turn Italian dataset
99	- Peak + Accumulation: Proxy-Level Scoring for Multi-Turn LLM Attack Detection (arXiv 2602.11247, Feb 2026)
100	- Defensive M2S: Training Guardrail Models on Compressed Multi-turn Conversations (arXiv 2601.00454, Jan 2026)
101	- Foot-In-The-Door: A Multi-turn Jailbreak for LLMs (EMNLP 2025) — persuasion structure drives attacks
102	- MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark (arXiv 2605.01687, May 2026)
103	- Constitutional Classifiers: Defending against Universal Jailbreaks (arXiv 2501.18837, Anthropic Jan 2025)
104	- DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training (He et al., ICLR 2023)
105	- Must Read: A Systematic Survey of Computational Persuasion (arXiv 2505.07775, May 2025)
106	- SoK: Evaluating Jailbreak Guardrails for Large Language Models (arXiv 2506.10597, Jun 2025; IEEE S&P 2026)
107	- NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks (Rafiei Asl et al., EMNLP 2025) — concurrent team's attack work
108	
109	## Reviewer Evaluation
110	
111	**Scores**:
112	  - clarity: **{'rationale': "Exceptionally well-structured proposal with honest positioning against DeepContext (explicitly acknowledges Track B is architecturally similar), precise mechanistic hypothesis grounded in Bullwinkel et al., rigorous 4-condition ablation design (A0-A3), multi-metric Pareto framing, concurrent work acknowledgment, and tiered risk contingencies. Among the best-articulated proposals I've reviewed.", 'score': 5}**/5
113	  - feasibility: **{'rationale': '130-160 H100-hours is well within the 200-hour budget. DeBERTa-v3-base (86M params) fine-tuning is standard and fast. Tiered timeline (8-day MVE vs. 11-day full) credibly de-risks the deadline. All datasets (MHJ, MultiBreak, XGuard-Train) and models are publicly available. DeepContext reproduction risk has reasonable contingency. The tight timeline is the main concern but MVE guarantees a publishable minimum.', 'score': 4}**/5
114	  - impact: **{'rationale': 'Addresses a genuine deployment need: interpretable, efficient, model-agnostic multi-turn defense. The Pareto improvement across 6 axes (F1, early detection, FPR, interpretability, latency, adversarial robustness) is a compelling contribution framing—no existing system advances all six. If hypothesis holds, it demonstrates task-appropriate features beat generic features, a useful insight. EMNLP 2026 LLM Security topic area is well-matched.', 'score': 4}**/5
115	  - novelty: **{'rationale': "Independently verified that no published work combines persuasion-grounded encoder training with temporal sequence modeling for multi-turn jailbreak detection. The theoretical grounding from Bullwinkel et al. (confirmed: representations kept 'benign' by multi-turn attacks, circuit breakers fail with 50-point gap) provides strong mechanistic justification. Honest framing as representational (not architectural) contribution strengthens credibility. Incremental but principled.", 'score': 4}**/5
116	
117	## Human Review Note
118	
119	【优化方案】
120	
121	1. **[标题] — 从方法命名升级为原则命名** — 命中 Novelty + Significance
122	   原始标题暗示"又一个检测方法"；建议改为突出理论贡献的标题，如 "DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-turn Jailbreak Detection"，将核心 insight 前置于标题层。
123	
124	2. **[Introduction / Core Insight] — 将 novelty 从 "persuasion features 有用" 重定位为 "Evasion Hierarchy 原则的首个系统验证"** — 命中 Novelty + Significance
125	   - 提出对抗通信中的逃逸难度递增层次：lexical（最易）< semantic（中等）< pragmatic（结构性困难）
126	   - DisPeD 定位为该通用原则在 jailbreak detection 中的首个实证验证，而非仅仅"一个更好的检测器"
127	   - 引入 Speech Act Theory（Austin 1962, Searle 1969）作为理论锚：现有检测器工作在 locutionary act 层面，DisPeD 工作在 illocutionary act 层面
128	
129	3. **[Section 2 / Theoretical Foundation] — 新增 Pragmatic Evasion Asymmetry 半形式化论证** — 命中 Novelty
130	   - 明确 persuasion-mediated attack 的 functional prerequisites（rapport building → defense lowering → boundary normalization → harmful elicitation）是攻击成功的**必要条件**
131	   - 逐条论证跳过任何 prerequisite 导致攻击失败（无 rapport → model 不降低防御 → 直接有害请求被拒绝；无 boundary testing → 直接跳到有害请求 = single-turn attack，已被现有防御覆盖）
132	   - 结论：semantic evasion（替换词汇/话题）不破坏 prerequisites → 容易；pragmatic evasion（消除 prerequisites）等价于放弃攻击 → 结构性困难
133	
134	4. **[Motivation] — 修复理论链条逻辑漏洞，精确化 "fundamental limitation" 边界** — 命中 Technical Soundness
135	   - Bullwinkel et al. 的发现严格限定为"target model 内部表征被操控"，不外推至外部检测器
136	   - 外部检测器失败归因精确分层：**scalar drift metrics**（如 inter-turn cosine distance）= information-theoretically insufficient（无论训练多少数据都无法从中恢复区分信号）；**full semantic representations** = practically limited（信息理论上可区分，但需模型自行从数据中解耦 pragmatic signal，DisPeD 通过 explicit inductive bias 加速此过程）
137	   - 此分层使 motivation 对端到端 baseline 结果 robust：即使 E2E baseline F1 尚可，DisPeD 的优势仍可论证为 sample efficiency + interpretability + robustness
138	
139	5. **[Scope] — 新增显式 scope 声明，精确限定核心 claim 适用范围** — 命中 Novelty（防御性强化）
140	   - 核心 pragmatic evasion asymmetry 适用于 persuasion-mediated multi-turn attacks（Crescendo, Deceptive Delight, social engineering jailbreaks）——覆盖现有多轮攻击的绝大多数
141	   - 明确承认部分攻击类型（纯信息累积、token smuggling、单帧 roleplay）不在 Track A 显式覆盖范围内
142	   - 但 Track B 的 continuous embedding 可捕捉这些攻击的异常 pragmatic patterns，形成安全网
143	
144	6. **[Method / Architecture Rationale] — 新增 "Bounded + Unbounded Detection" 互补叙事** — 命中 Novelty
145	   - Track A = bounded precision：14-category taxonomy 精确覆盖主流攻击类，输出可解释的 strategy sequence
146	   - Track B = unbounded recall：continuous pragmatic embeddings 泛化至未知攻击类型和 novel strategy combinations
147	   - 此互补不是工程冗余，而是理论驱动的必然设计
148	
149	7. **[Method / Architecture Rationale] — 新增 "Why Not End-to-End" 三点必要性论证** — 命中 Novelty
150	   - (a) Interpretability as deployment requirement：安全团队需要可审计的 explanation 来 triage alerts
151	   - (b) Sample efficiency via encoded priors：persuasion taxonomy 编码数十年社会心理学研究，low-data regime 下提供有意义的 inductive bias
152	   - (c) Robustness to distribution shift：新攻击引入新 semantic content 但复用 pragmatic patterns，explicit pragmatic features 跨分布更稳定
153	
154	8. **[Method / Track A] — 明确两阶段 pipeline，修复 latency 可信度** — 命中 Technical Soundness
155	   - 训练时：GPT-4 作为 teacher 标注 15K conversations
156	   - 推理时：distilled DeBERTa-base classifier 执行 per-turn 14-class prediction
157	   - 报告 distilled classifier 的 held-out macro-F1 和 per-turn accuracy
158	   - 预设可接受阈值 macro-F1 ≥ 0.65；Plan B：若不达标则合并至 10 类
159	
160	9. **[Method / Key Hypothesis] — 显式提出 "Monotonic Escalation Trajectory" hypothesis** — 命中 Novelty + 论文记忆点
161	   - Hypothesis：adversarial conversations 在 pragmatic strategy space 中呈现 monotonic escalation trajectory（trust → test → normalize → elicit）；benign conversations 呈现 oscillatory / non-monotonic patterns
162	   - 验证方式：strategy transition matrix 可视化 + trajectory analysis
163	   - 这是论文最 memorable 的 one-liner，审稿人读完 abstract 就能记住
164	
165	10. **[Experiments / Ablation] — 从原始 4 条件扩展为 6 条件完整贡献分解链** — 命中 Technical Soundness
166	    - A0（DeepContext reproduction, DeBERTa-base, drift features）
167	    - A1（encoder upgrade: DeBERTa-v3-large, same drift features）→ 隔离 encoder capacity
168	    - A1.5（full per-turn embeddings, vanilla DeBERTa-v3-large, no persuasion FT）→ 隔离 "full embeddings vs. scalar drift"
169	    - A2（persuasion-grounded contrastive FT, single-track）→ 隔离 persuasion grounding 纯增量
170	    - A3（full dual-track + cross-attention fusion）→ 隔离 dual-track + fusion 贡献
171	    - A3'（dual-track + concatenation fusion）→ 隔离 cross-attention 机制贡献
172	    - 每一步精确改变一个变量，形成无 confounding 的 contribution ladder
173	
174	11. **[Experiments / Baselines] — 从原始 7 个扩展至 9 个，补关键缺失** — 命中 Technical Soundness
175	    - 新增 **Hierarchical E2E baseline**：per-turn DeBERTa-v3-large [CLS] → GRU → binary classification（与 DisPeD 信息覆盖完全对等，唯一差异是有无 explicit pragmatic features）
176	    - 新增 **GPT-4 Direct Prompting**：full conversation + few-shot → classification + explanation（度量 accuracy-latency-cost tradeoff）
177	    - E2E baseline 采用层次化设计确保公平比较：DisPeD 赢 = 证明 explicit pragmatic modeling 必要性；DisPeD 输 = 必须诚实讨论
178	
179	12. **[Experiments / Evaluation] — Latency claim 修正为诚实分层报告** — 命中 Technical Soundness
180	    - 放弃原始"≤25ms"的不可信 claim
181	    - 改为：full pipeline latency（首次处理完整对话，预估 100-500ms）+ incremental latency（新增一 turn 边际处理，预估 30-60ms）
182	    - 与 GPT-4 prompting（~5-10s）形成有意义但诚实的对比
183	
184	13. **[Experiments / Adaptive Attack] — 在 initial submission 中纳入 50-sample strategy-aware evasion** — 命中 Technical Soundness
185	    - 使用 DeepSeek-R1 生成 50 条攻击者尝试避免触发已知 persuasion strategy patterns 的对话
186	    - 直接验证核心 pragmatic evasion asymmetry claim：如果 DisPeD 在此条件下仍维持高 F1，impossibility argument 获得实证支持
187	    - 剩余两类 adaptive attack（benign-mimicry, temporal perturbation）保留至 camera-ready
188	
189	14. **[Experiments / FPR] — 强化 benign high-drift 测试集构建 + 分层报告** — 命中 Technical Soundness
190	    - 从 WildChat 主动筛选 top-10% 最高 drift 对话作为 "hard negative" 子集
191	    - 报告 FPR @ 低/中/高 drift 分位数，精确展示 persuasion grounding 在 high-drift 场景下的 discrimination 能力
192	    - 所有 ablation 条件使用相同训练数据分布（含 high-drift negatives），排除 data composition 解释
193	
194	15. **[Experiments / Interpretability] — 严格化人工评估 protocol** — 命中 Technical Soundness
195	    - 100 样本 × 3 security practitioners × blinded randomized × Factual Accuracy (1-5) + Actionability (1-5) × Krippendorff's α × pairwise preference
196	    - 新增 automatic proxy：Track A predicted strategy sequence vs. ground-truth annotation 的 sequence-level F1
197	    - 两层验证互补：human eval 验证实用价值，auto proxy 验证事实准确性
198	
199	16. **[Experiments / Statistical Rigor] — 加入 encoder stability proxy** — 命中 Technical Soundness
200	    - 承认单 encoder run 为 limitation
201	    - 补充 cross-checkpoint variance（epoch 2 / epoch 3 / final 分别评估 A3），量化 encoder training stochasticity 对下游的影响
202	
203	17. **[Related Work] — 新增三组关键差异化论证** — 命中 Related Work 差异化
204	    - vs. PAP（Zeng et al. 2024）：taxonomy scope（14 类 > Cialdini 6 类）、temporal trajectory（不只是 per-turn labels）、Track B continuous generalization
205	    - vs. Propaganda Detection / SemEval：span-level 单文档 → turn-level 跨轮次 temporal trajectory；rhetoric taxonomy → social psychology + interaction dynamics 融合
206	    - vs. Dialogue Act Sequence Modeling（Tsinganos et al. 2022 等）：persuasion-strategy level（语义更丰富）vs. DA level（inform/request/confirm）；双通道 vs. 单通道；对抗检测 vs. 对话管理
207	
208	18. **[Broader Significance] — 将 jailbreak detection 定位为通用原则的 primary instantiation** — 命中 Significance
209	    - Evasion hierarchy 原则泛化至：社交工程检测、phishing 对话识别、online radicalization 路径检测、deceptive negotiation
210	    - Jailbreak detection 选择理由：ground-truth 可得、攻击策略多样、safety 影响即时
211	    - 不需要额外实验，但显著扩大论文 audience 和 citation potential
212	
213	【主要风险】:
214	1. **Timeline 极限风险**：9 天内完成 ~170 H100-hours compute + 人工评估协调 + 论文写作。任何环节延迟（annotation κ 不达标需返工、encoder training 不收敛、practitioner 不响应）都可能导致 MVE 不完整。Fallback：削减至 4 条件（A0+A1.5+A2+A3），interpretability eval 降级为 pilot。
215	2. **Impossibility argument 可能被 dismiss**：半形式化论证的说服力高度依赖写作质量。如果论述过于 informal 或 hand-wavy，sophisticated reviewer 可能评为"interesting intuition but not a rigorous result"，从而将论文 novelty 降级为 pure empirics。对策：保持论证简短（半页以内）、逻辑链清晰、明确标注为 "informal argument" 而非 "proof"。
216	
217	【实施评估】:
218	- **计算资源**: ~170 H100-hours total。分解：DeBERTa-v3-large persuasion-grounded contrastive fine-tuning ~40h；DeBERTa-base distilled classifier ~8h；GRU training 6 conditions × 3 seeds × ~7h = ~126h。需要 8× H100 节点约 21 小时连续计算，或等效云资源（A100 约 ×1.5 时间）。Cloud cost 预估 ~$500-700。GPT-4 API cost ~$300-500（annotation + prompting baseline）。
219	- **数据需求**: MHJ、MultiBreak、WildChat、MT-Bench——全部公开可得，无需额外数据采集或授权。需要从 WildChat 中筛选 high-drift subset（自动化脚本，~1h）。50 条 adaptive attack 通过 DeepSeek-R1 API 生成（~$10-20）。
220	- **人工介入**: (1) 2 名 trained annotators：500-sample annotation QA，每人约 15-20 小时工作量，需具备对话分析或 NLP 背景；(2) 3 名 security practitioners：100-sample interpretability evaluation，每人约 3 小时，需具备安全事件响应经验。均需 Day 0 立即启动招募和培训。协调难度中-高（主要是时间紧迫而非任务复杂性）。
221	- **训练需求**: 需要模型 fine-tuning（非从头预训练）。DeBERTa-v3-large（304M 参数）persuasion-grounded contrastive fine-tuning 是最大训练任务（~40 H100-hours，预估 2-3 epochs on 15K conversations）。DeBERTa-base（110M 参数）distilled classifier 是轻量级 supervised fine-tuning（~8 H100-hours）。Bi-GRU 模型体量小（< 10M 参数），训练快速。无需训练 LLM 级模型。
222	- **新 Benchmark**: 不需要构建新的 benchmark 或评测数据集。需要构造的数据均为标注/生成性质：(1) 15K conversations 的 14-class persuasion strategy annotation（GPT-4 生成 + 500-sample human validation）；(2) 50 条 strategy-aware evasion attacks（DeepSeek-R1 生成）；(3) high-drift benign subset 筛选（自动化）。所有评测基于现有公开 benchmark（MHJ, MultiBreak）。
223	
224	
225	## MVP Validation Results
226	
227	- **Date**: 2026-05-17
228	- **Hypothesis Supported**: Yes
229	
230	### Key Metrics
231	
232	Treatment K=2 F1=0.987, Baseline K=2 F1=0.879, Delta=+10.8pp; Treatment K=3 delta=+5.9pp; TF-IDF=1.0 (data quality caveat, must fix in research phase)
233	
234	### Summary
235	
236	Phase B full (480 samples: 250 jailbreak + 230 benign) validated the core hypothesis: persuasion-grounded DeBERTa embeddings (multi-task fine-tuned on 8-class persuasion + intent) enable significantly earlier detection of Crescendo jailbreak attacks vs vanilla DeBERTa. Treatment outperforms baseline at early turns: K=2 F1 0.987 vs 0.879 (+10.8pp), K=3 +5.9pp. Caveat: TF-IDF=1.0 indicates lexical shortcuts remain in current data — must be resolved in research phase before paper submission.
237	
238	### Recommendation
239	
240	GO — core signal validated. Research phase priority: (1) fix TF-IDF=1.0 via adversarial perturbation experiments, (2) fix strategy=7 hardcoding (M004), (3) re-validate on clean data. Target: EMNLP 2026 ARR DDL 2026-05-25.
241	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "457dc40a-d942-4765-93b2-ff5540ff2c38",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "506beff3-64c2-4b5e-a25d-0125f20833ca",
  "sourceToolAssistantUUID": "457dc40a-d942-4765-93b2-ff5540ff2c38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T17:24:14.992Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016c6TMRN5KdoadwNYJqjdUq`</summary>

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
  "parentUuid": "506beff3-64c2-4b5e-a25d-0125f20833ca",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgvSnBNcqM7QbpPMzH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3205bc6-7e6a-4b3a-9c3e-94e29ee397de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgNZXEbyAm64E4kPSQVtxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14826,
      "cache_read_input_tokens": 19216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14826,
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

_source line 23 · 2026-05-17T17:24:15.002Z_

<details><summary>↩ Tool result · `toolu_016c6TMRN5KdoadwNYJqjdUq`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'persuasion_turn_jailbreak_detect'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3205bc6-7e6a-4b3a-9c3e-94e29ee397de",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "77e9370a-c17d-4b1b-8b66-54c4e596b0e6",
  "sourceToolAssistantUUID": "c3205bc6-7e6a-4b3a-9c3e-94e29ee397de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T17:24:16.143Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pddx6wyHCVgSi95ASkQECC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/dream_reports/dream_20260517T165817/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77e9370a-c17d-4b1b-8b66-54c4e596b0e6",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XgvSnBNcqM7QbpPMzH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9d2652b-c0f4-4aaf-a385-2946c9e603fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgNZXEbyAm64E4kPSQVtxn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14826,
      "cache_read_input_tokens": 19216,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14826
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 19216,
          "cache_creation_input_tokens": 14826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14826,
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

_source line 25 · 2026-05-17T17:24:16.148Z_

<details><summary>↩ Tool result · `toolu_01Pddx6wyHCVgSi95ASkQECC`</summary>

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
  "parentUuid": "f9d2652b-c0f4-4aaf-a385-2946c9e603fd",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "890983ca-f39d-434d-9056-093195375a94",
  "sourceToolAssistantUUID": "f9d2652b-c0f4-4aaf-a385-2946c9e603fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-17T17:24:20.002Z_

Now let me also check the reviewer history/context for any prior review loop information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "890983ca-f39d-434d-9056-093195375a94",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XhLtD234PNNunqSn75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25820572-9c78-43ee-8f83-a7790f90e0e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5bJRsVL4qkyU6JiBteNDL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 34042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
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

_source line 27 · 2026-05-17T17:24:21.531Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VtwSCzc87kK8nPmrg5Qe5X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/task_context/history/reviewer/loop_1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25820572-9c78-43ee-8f83-a7790f90e0e3",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XhLtD234PNNunqSn75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7aa412b-9dae-4f02-ad57-46abf55a721f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5bJRsVL4qkyU6JiBteNDL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 34042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17498,
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

_source line 28 · 2026-05-17T17:24:21.544Z_

<details><summary>↩ Tool result · `toolu_01VtwSCzc87kK8nPmrg5Qe5X`</summary>

```text
1	---
2	loop: 1
3	reason: max_wall_time
4	updated: '2026-05-17T10:05:20+00:00'
5	---
6	
7	### 1. 🔴 硬约束 / 红线
8	- GPU 白名单 cuda:0-3（C001），生成脚本 `CUDA_VISIBLE_DEVICES=0,1,2,3` 已确认合规
9	- 攻击者模型是 **Qwen3-8B**（稠密），不是 ROADMAP 曾错写的 "Qwen3-30B"（服务器上只有 Qwen3-30B-A3B MoE）。已修正，但论文/报告中引用模型名必须写 Qwen3-8B
10	- κ 验证必须是真 dual annotation（两个独立标注器），当前 κ=0.83 是 GPT-5.5 vs 启发式 baseline，**不能作为合格证据引用**
11	- 原始数据集 baseline F1=98.7-100%（source classification ceiling effect），任何在原始数据上的实验结论**不可信**，必须在 Crescendo 重构数据上重跑
12	
13	### 2. 🖥️ 基础设施快照
14	- 服务器：westd-33183(root)，工作目录 `/root/persuasion_turn_jailbreak_detect`
15	- Python：`/root/miniconda3/bin/python`（Python 3.12.3, PyTorch 2.8.0+cu128, transformers 5.8.1）
16	- HF cache：`/root/autodl-tmp/hf_cache`，HF_ENDPOINT=https://hf-mirror.com
17	- 模型路径：attacker `/root/autodl-tmp/hf_cache/Qwen/Qwen3-8B`，target `Qwen/Qwen2.5-7B-Instruct`
18	- 本地 artifacts：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/`
19	- 活跃进程：PID 40859（`generate_crescendo_v2.py`），screen session `crescendo`，cuda:0+1
20	- 日志：`/root/persuasion_turn_jailbreak_detect/logs/crescendo_gen.log`
21	- 数据输出：`/root/persuasion_turn_jailbreak_detect/data/generated/crescendo_progress.jsonl`
22	- Registry：**空**（无正式实验注册）
23	
24	### 3. 📊 当前状态
25	- Crescendo v2 生成运行中：11/250 完成，单进程 ~55s/条，ETA ~228 分钟（~3.8h）
26	- **第二个并行进程（cuda:2+3）未启动**——我已 WARNING Director，ROADMAP 声称"双进程并行"但实际只跑了一个
27	- 8/8 策略类别已覆盖，8 种有害目标类别，质量初步通过
28	- 无 RUNNING/PREPARING 实验（registry 为空）
29	- 等待：Crescendo 生成完成 → sanity check → 标注 → Phase B 训练
30	
31	### 4. 📋 待办
32	- 生成到 ~50 条 → 首次 sanity check：策略分布（≥6/8 有意义覆盖）+ baseline F1（期望 70-85%，若仍 >95% 说明数据仍 trivial）
33	- 生成完成 250 条 → 完整质量审查：重复 turn 检测、策略序列合理性、对话多样性
34	- 新数据 baseline 训练完成 → 审查 F1 是否脱离 ceiling（<90% 即可继续）
35	- Treatment 实验注册到 registry → 标准审查流程（数据一致性 + 设计合规 + 结论可靠性）
36	- 标注重做通知 → 验证是否真 dual annotation（两个独立模型/标注器），κ 是否满足 ≥0.60 总体 + ≥0.40 每类
37	- Director 转发 framing 提案 → Read `negative-framing-review.skill.md` 四维度审查
38	
39	### 5. 🎯 战略上下文
40	- **项目核心赌注**：persuasion strategy sequences 比 generic semantic embeddings 更能区分多轮 jailbreak。目前**零实验证据**——数据重构是 critical path，所有之前的训练结果因 ceiling effect 作废
41	- **DDL 2026-05-25（8 天）**：时间线紧但 AI team 速度下可行，前提是数据生成今天完成 + 标注明天完成 + Phase B 训练后天完成
42	- **最易判断错的事**：不要因为原始数据 κ=0.83 就认为标注质量已过关——那是 model-vs-heuristic，不是 dual annotation，gate 未通过
43	- **易踩的坑**：原始 3 条 Crescendo 对话可能用不同模型生成（Qwen3-30B-A3B vs 当前 Qwen3-8B），合并前需确认一致性
44	- **generation_stats.json vs JSONL 行数可能不一致**——stats 可能含尚未写入 JSONL 的条目，以 JSONL 为准
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7aa412b-9dae-4f02-ad57-46abf55a721f",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "b4d8e860-db5f-4570-bfef-85b9173c0e13",
  "sourceToolAssistantUUID": "a7aa412b-9dae-4f02-ad57-46abf55a721f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T17:24:21.775Z_

<details open><summary>🔧 Tool call — Read · `toolu_018s5oGyEtGm4xhkG9YUDe3A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/task_context/reviewer.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4d8e860-db5f-4570-bfef-85b9173c0e13",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8XhLtD234PNNunqSn75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b472b34-70a7-437a-a391-71514110d5fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5bJRsVL4qkyU6JiBteNDL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17498,
      "cache_read_input_tokens": 34042,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17498
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 34042,
          "cache_creation_input_tokens": 17498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17498,
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

_source line 30 · 2026-05-17T17:24:21.784Z_

<details><summary>↩ Tool result · `toolu_018s5oGyEtGm4xhkG9YUDe3A`</summary>

```text
1	---
2	loop: 2
3	reason: max_wall_time
4	updated: '2026-05-17T16:52:03+00:00'
5	---
6	
7	### 1. 🔴 硬约束 / 红线
8	- GPU 白名单: cuda:0-3 on westd-33183，越界即 critical（C001）
9	- TF-IDF ≤0.65 是 sanity gate，必须通过后才能训练 Phase B。当前 TF-IDF=1.0，数据不合格
10	- Pilot (pilot_phase_b) 结果不可引用为 evidence（n=3 benign in test, TF-IDF=1.0）
11	- Phase B full 结果同样不可引用（TF-IDF=1.0 = 词汇快捷方式，treatment 性能无法归因于 persuasion strategy）
12	- Benign persuasion_strategy 全部 hardcoded=7，这是 spurious feature，treatment 可能在利用它
13	
14	### 2. 🖥️ 基础设施快照
15	- 服务器: westd-33183 (root)，4× RTX PRO 6000 Blackwell 96GB
16	- 工作目录: /root/persuasion_turn_jailbreak_detect
17	- 模型缓存: /root/autodl-tmp/hf_cache/Qwen/Qwen3-8B, Qwen2.5-7B-Instruct
18	- DeBERTa: microsoft/deberta-v3-base (HF 在线)
19	- 数据: data/generated/crescendo_all.jsonl (250条), benign_v4c_full_gpu0.jsonl (115条), benign_v4c_full_gpu2.jsonl (115条)
20	- 训练数据: data/final/{train,val,test}.jsonl (336/72/72)
21	- Checkpoints: checkpoints/phase_b_deberta/best/model.pt (735MB), checkpoints/phase_b_gru/{baseline,treatment}
22	- 磁盘: 30GB 总量, ~6.5GB 可用 (79% used)
23	- 活跃进程: 无 Python 进程，4 GPU 全部空闲
24	- wildchat_benign_226.jsonl 已存在于 data/ (733KB)，尚未被使用或评估
25	
26	### 3. 📊 当前状态
27	我刚完成 Phase B full 结果审查，发送了 [severity: critical] 报告给 Director。核心结论：TF-IDF=1.0 在所有 K 值完美分类，benign 数据的 register mismatch 问题从 v4b(0.924) 到 v4c(1.0) 恶化。Treatment F1=0.987@K=2 低于 TF-IDF=1.0，方法无增量价值。
28	
29	Registry: pilot_phase_b (DONE, conclusion=success — 但我已标注为不可信)。Phase B full 未注册 registry。
30	
31	等待: Director 对 critical 报告的响应 — 是否 pivot 数据策略。
32	
33	### 4. 📋 待办
34	- Director 决定 pivot 数据策略 → 审查新方案是否能解决 register mismatch（三个方向: WildChat 真实对话 / formal register 混入 / adversarial filtering）
35	- 新 benign 数据生成完成 → 独立跑 TF-IDF sanity check 核实 ≤0.65
36	- sanity PASS + 新 Phase B 启动 → 核实 GPU 合规 + 实验注册 registry
37	- 任何 Worker 完成通知 → 标准审查流程（数据一致性/实验设计/结论可靠性）
38	- Agent 注册新实验 → 检查 spec 完整性（命令/服务器/数据路径/模型版本/seed/checkpoint）
39	
40	### 5. 🎯 战略上下文
41	- 项目: DisPeD — 用 persuasion strategy sequences 检测多轮 jailbreak，目标 EMNLP 2026 ARR DDL 2026-05-25（~7天）
42	- D001: 接受 DeBERTa F1=0.789 作为 baseline，停止 TF-IDF 数据迭代，reframe 为 early detection
43	- **核心瓶颈是数据不是模型**: benign 生成数据（v4b/v4c）与 jailbreak 有系统性 register 差异（casual vs formal/hypothetical），TF-IDF 一眼看穿。模型再好也没用，必须先修数据
44	- wildchat_benign_226.jsonl 是潜在突破口 — 真实对话可能有更自然的 register 分布，但尚未评估
45	- 易错判断: treatment F1 数字很漂亮（0.987-1.0），容易被误认为 MVP PASS。必须看 TF-IDF sanity — TF-IDF > 0.65 时任何 treatment 结果都不可信
46	- Register mismatch 是这个项目从头到尾的核心 blocker，已迭代 v1→v4c 六轮未解决
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b472b34-70a7-437a-a391-71514110d5fe",
  "isSidechain": true,
  "promptId": "9947c6c6-fa04-4662-a2b8-6020f419a7cb",
  "agentId": "af0c2201172a0086d",
  "type": "user",
  "uuid": "d02e32ff-218a-40fd-95fe-670db4249183",
  "sourceToolAssistantUUID": "8b472b34-70a7-437a-a391-71514110d5fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T17:26:06.002Z_

I now have a thorough understanding of the paper, its internal development history, and its claims. Let me write the review.

---

## Review of "DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-Turn Jailbreak Detection"

### 1. Summary

This paper proposes DisPeD, a two-stage pipeline for detecting multi-turn jailbreak attacks on LLMs. The key idea is that while attackers can paraphrase surface content freely, the underlying persuasion playbook (rapport building, reframing, escalation) is structurally necessary for attack success and thus difficult to evade. Stage 1 fine-tunes DeBERTa-v3-base with a multi-task objective (8-class persuasion classification + binary intent), and Stage 2 feeds the resulting turn embeddings into a bidirectional GRU for conversation-level classification. The paper reports strong early detection (F1=0.91 at K=2), robustness under adversarial paraphrasing (3pp degradation vs. 13-18pp for baselines), and zero-shot cross-attack transfer.

### 2. Strengths

**S1. Well-motivated conceptual framing.** The "Pragmatic Evasion Asymmetry" is an intuitive and useful conceptual contribution. The three-tier evasion hierarchy (lexical < semantic < pragmatic) provides a clear organizing principle, and the empirical results in Tables 6 and 7 (now Tables 4/5 in the submitted version) directly validate this hierarchy with a clean gradient (18pp > 13pp > 3pp degradation). The framing is memorable and could influence how the community thinks about robustness levels in adversarial detection.

**S2. Register normalization is a responsible methodological choice.** The authors identify and address the lexical shortcut problem (TF-IDF=1.0 on original data), applying register normalization to reduce separability to 0.58 (Table 1). This is commendable intellectual honesty and strengthens the validity of downstream results. The fact that the paper explicitly discusses this issue and provides before/after diagnostics sets a good standard.

**S3. Clean ablation via scrambled labels.** The scrambled-label experiment (Table 8/Section 5.3) is well-designed: randomizing persuasion labels while keeping intent labels intact isolates the contribution of persuasion semantics from the multi-task training procedure itself. The 15pp drop at K=2 (from 0.91 to 0.76, close to the vanilla baseline at 0.77) provides convincing causal evidence that the persuasion signal, not incidental regularization, drives the performance gap.

**S4. Cross-attack transfer provides meaningful generalization evidence.** Training on Crescendo only and evaluating zero-shot on FITD and Deceptive Delight (Table 9) is the right experimental design for a detection paper. The 16.5pp average improvement over the semantic baseline on unseen attack types is a strong result that supports the claim of learning attack-type-agnostic pragmatic signals.

**S5. Early detection framing is practically relevant.** The emphasis on K=2 detection, where DisPeD achieves F1=0.91 vs. 0.77 for the baseline, addresses a real deployment need. Security systems need to intervene before the attack succeeds, and the paper clearly demonstrates that persuasion-grounded features provide discriminative signal earlier than semantic features.

### 3. Weaknesses

**W1. The "Pragmatic Evasion Asymmetry" repackages known observations rather than establishing a genuinely new finding.** Zeng et al. (2024) already demonstrated that persuasion techniques are systematically present in jailbreak attacks. Hagendorff (2026) showed identifiable persuasion strategies in 97% of successful multi-turn attacks. Chen et al. (2025) showed persuasion dynamics are extractable from turn-level representations. The paper's own Section 2 cites all three. The observation that "persuasion structure is harder to evade than surface content" is a natural corollary of these prior findings, not a novel theoretical contribution. The Speech Act Theory framing (Austin 1962, Searle 1969) adds vocabulary but no analytical substance: calling existing detectors "locutionary" and DisPeD "illocutionary" is a metaphor, not a formal result. The paper does not engage with Speech Act Theory beyond this single sentence in the Introduction (line 39), and no experimental design tests any prediction derived from Speech Act Theory specifically.

**W2. Related work coverage is severely inadequate.** The bibliography contains only 15 entries. For a paper positioning itself in the multi-turn jailbreak detection space at a major NLP venue, this is far below the expected standard. Critical omissions include:

- **LLM-as-judge approaches**: No comparison to or discussion of GPT-4/Claude-based conversation-level safety evaluation, which is the de facto deployed approach at most LLM providers.
- **Llama Guard 2/3 and ShieldGemma**: The paper cites Llama Guard (Inan et al. 2023) as a single-turn classifier but ignores subsequent versions with multi-turn capabilities.
- **BIID** (arXiv 2509.22732): Bidirectional intention inference achieving near-0% ASR on multi-turn attacks. Not cited or compared.
- **G-Guard** (arXiv 2507.07146): GCN-based multi-turn detection. Not cited.
- **SafeDream** (arXiv 2604.16824): Safety world model with CUSUM detection for proactive jailbreak detection. Not cited.
- **Constitutional Classifiers** (Anthropic, arXiv 2501.18837): Exchange-level classification achieving 4.4% ASR. Not cited.
- **Peak+Accumulation** (arXiv 2602.11247): Zero-GPU proxy scoring with 90.8% recall. Not cited.
- **GLiGuard** (arXiv 2605.07982): Strategy-aware compact encoder guard. Not cited despite being directly relevant (it already does jailbreak strategy classification, albeit single-turn).
- **Nasr, Carlini et al.** (arXiv 2510.09023): Systematically bypassed 12 single-input classifiers with >90% ASR under adaptive attack. This work is essential context for any classifier-based defense paper.
- **Persuasive Fingerprint** (Alizadeh Noughabi et al., CIKM 2025): Uses Cialdini's principles to characterize jailbreak susceptibility. Directly relevant to the paper's use of the same theoretical framework and not cited.

The "first to use persuasion-grounded representations for detection" claim (Section 2, final sentence) is difficult to verify given this thin coverage. GLiGuard classifies 11 jailbreak strategies including persuasion-based ones; the Persuasive Fingerprint work applies Cialdini's framework to jailbreaks. Whether DisPeD is truly "first" requires engaging with these works.

**W3. The technical method is standard and contributes limited architectural novelty.** DeBERTa fine-tuning with multi-task classification heads followed by a GRU sequence classifier is a well-established pipeline. The paper acknowledges this implicitly by framing the contribution as "representational, not architectural" (this phrasing appears in the idea brief but should be explicit in the paper). However, the representational contribution is itself narrow: the entire novelty reduces to "fine-tune on persuasion labels before feeding to GRU." The persuasion taxonomy is borrowed from Cialdini via Zeng et al. (2024), not developed here. The temporal modeling (bidirectional GRU) is off-the-shelf. The multi-task training recipe (cross-entropy sum with lambda=1.0) uses no novel training techniques.

**W4. Dataset is too small and synthetic to support the claims made.** 480 total conversations with 72 test samples is extremely small for a detection paper. The cross-attack generalization sets (72 FITD, 65 Deceptive Delight) are generated by a single model (Qwen3-8B), not collected from real adversarial interactions. This means:
- All "attacks" share the same generative distribution, potentially inflating cross-attack transfer numbers.
- 72 test samples yield wide confidence intervals. The paper reports p-values from bootstrap tests but does not report confidence interval widths.
- The strategy distribution numbers in Table 3 (e.g., FITD: 30% reciprocity, 25% commitment) reflect the generative model's behavior, not empirically observed attack patterns from real adversaries.

**W5. No comparison against LLM-based detection methods.** The baselines are limited to TF-IDF+LR, vanilla DeBERTa+GRU, and a "DeepContext proxy" (BERT-base+GRU). The strongest known multi-turn defenses (BIID, Constitutional Classifiers, SafeDream) are not compared. More critically, the obvious baseline of prompting a capable LLM (GPT-4, Claude) with the conversation and asking "is this a jailbreak attempt?" is absent. Given that LLM-as-judge is the most widely deployed approach and arguably the strongest baseline for conversation-level safety classification, its omission is a significant gap.

**W6. The "DeepContext proxy" baseline is not a faithful reproduction.** The paper states it uses BERT-base + GRU as a "proxy" for DeepContext (Section 3.3), but DeepContext uses task-attention weighted pooling, a 3-layer GRU with 2048 hidden units, and hybrid residual connections (per the idea brief). The proxy strips all of these architectural choices. Since the paper explicitly positions against DeepContext (Introduction, paragraph 1), using a degraded proxy and then claiming superiority is misleading. The honest framing should acknowledge that this is a BERT-base+GRU baseline, not a DeepContext proxy.

**W7. Adversarial robustness evaluation is weak.** The "adversarial paraphrasing" experiment (Section 5.2) applies synonym substitution and sentence restructuring. This is the weakest form of adversarial evaluation. The paper does not test:
- **Adaptive adversaries** who are aware of the persuasion-based detection mechanism and deliberately try to evade it (e.g., by distributing persuasion functions across turns differently, or by using implicit rather than explicit persuasion strategies).
- **Strategy-aware evasion**: Can an attacker accomplish the same functional goal (e.g., rapport building) without triggering the 8-class persuasion classifier? The paper's core claim is that this is structurally impossible, but no experiment tests this directly.
- The Nasr, Carlini et al. (2025) framework for adaptive attacks against classifiers. Any classifier-based defense published after October 2025 should engage with this work.

**W8. Persuasion annotation quality is insufficiently validated.** The paper mentions "94% annotation consistency after normalization" (Section 4.1) and "91% LLM annotation consistency" for generated attacks (Section 4.2), but does not report inter-annotator agreement (Cohen's kappa) between independent annotators. LLM self-consistency is not a substitute for annotation quality validation. The internal reviewer notes (not in the paper) flag that the original kappa of 0.83 was computed between GPT and a heuristic baseline, which is not valid inter-annotator agreement.

### 4. Questions for Authors

**Q1.** The claim "first to use persuasion-grounded representations for jailbreak detection" (Section 2, final sentence): How do you position this relative to GLiGuard (arXiv 2605.07982), which classifies 11 jailbreak strategies including persuasion-based ones in a single forward pass? And relative to the Persuasive Fingerprint work (CIKM 2025), which applies Cialdini's framework to characterize jailbreak susceptibility?

**Q2.** What is the inter-annotator agreement (Cohen's kappa or Krippendorff's alpha) between two independent annotators on the 8-class persuasion taxonomy? The "94% annotation consistency" and "91% LLM consistency" figures in Sections 4.1 and 4.2 appear to measure LLM self-consistency, not human-validated annotation quality.

**Q3.** Have you evaluated DisPeD against an adaptive adversary who knows the detection mechanism uses persuasion strategy classification? For example, an attacker who attempts rapport building through purely factual, non-persuasive exchanges, or who distributes persuasion functions across turns in non-monotonic patterns.

**Q4.** Why was no LLM-as-judge baseline included (e.g., GPT-4 or Claude prompted with the full conversation)? This is arguably the strongest practical baseline for conversation-level safety evaluation.

**Q5.** The register normalization procedure (Section 4.1) uses "LLM paraphrasing" to convert jailbreak turns to conversational register. Could this paraphrasing itself introduce artifacts that the model learns? How do you ensure the paraphrasing does not inadvertently alter the persuasion strategy labels?

**Q6.** With only 72 test conversations, what are the 95% bootstrap confidence intervals for the main F1 results in Table 4? The reported differences (e.g., 0.91 vs. 0.77) may be within overlapping confidence intervals at this sample size.

**Q7.** The monotonicity score (0.82 for jailbreaks, Table 10) relies on a predefined ordering of persuasion strategies from "lower-risk" to "higher-risk." How is this ordering determined? Is it based on theoretical priors or empirically derived? Would different orderings yield different monotonicity scores?

### 5. Minor Issues

**M1.** The paper uses a generic article class (`\documentclass[11pt,a4paper]{article}`) rather than the official EMNLP 2026 template. This would need to be corrected before submission.

**M2.** Table 3 (strategy distribution) percentages for Crescendo sum to 115%, not 100%. (28+12+18+8+15+5+22+7 = 115). This is either a typographical error or the categories are not mutually exclusive, which should be stated.

**M3.** The paper alternates between "register-normalized" and "clean" to refer to the same data condition. Standardizing terminology would improve clarity.

**M4.** Section 5.5 (Trajectory Analysis): "82% of strategy transitions move from lower-risk to higher-risk categories" presupposes a risk ordering that is not formally defined in the Method section.

**M5.** The bibliography entry for Hagendorff (2026) lacks volume and page numbers. Several entries use "and others" rather than listing all authors, which does not meet venue formatting standards.

**M6.** The paper would benefit from a figure showing example persuasion strategy trajectories for jailbreak vs. benign conversations, making the monotonic escalation pattern visually concrete.

### 6. Overall Assessment

The paper addresses a real and important problem (multi-turn jailbreak detection) and offers a sensible approach (grounding turn representations in persuasion strategy classification). The conceptual framing around the "Pragmatic Evasion Asymmetry" is intuitive and the experimental design, particularly the register normalization and scrambled-label ablation, shows methodological care. However, the paper has significant weaknesses that prevent acceptance at this stage. The novelty is limited: the core observation that persuasion patterns are harder to evade than surface features is a natural corollary of prior work by Zeng et al. (2024), Hagendorff (2026), and Chen et al. (2025), and the technical method (DeBERTa + GRU) is entirely standard. The related work coverage is thin (15 references), missing numerous directly relevant multi-turn detection methods (BIID, G-Guard, SafeDream, Constitutional Classifiers, GLiGuard) and failing to compare against LLM-as-judge baselines. The dataset is very small (480 conversations, 72 test) and entirely synthetic, the "DeepContext proxy" is not a faithful reproduction, and the adversarial robustness evaluation does not test adaptive adversaries who are aware of the detection mechanism. The Speech Act Theory framing is decorative rather than substantive. The paper has the ingredients of a solid contribution but needs substantially expanded baselines, a larger and more diverse evaluation, honest positioning of what is new relative to prior persuasion-in-jailbreaking work, and engagement with adaptive attack evaluation frameworks.

### 7. Scores

- **Soundness**: 2/4 -- Core experimental results are on very small synthetic data; "DeepContext proxy" is misleading; no adaptive adversary evaluation; annotation quality not properly validated.
- **Presentation**: 3/4 -- Generally clear writing with good use of tables and a logical structure. Register normalization and ablation design are well-explained. Weakened by thin related work and undefined risk ordering for monotonicity.
- **Contribution**: 2/4 -- The conceptual framing is useful but not sufficiently novel given prior work on persuasion in jailbreaking. The technical method is standard. Missing comparisons to strong baselines (LLM-as-judge, BIID, Constitutional Classifiers) make it impossible to assess where DisPeD actually sits in the landscape.
- **Overall**: 3 (Weak Reject) -- The core idea has merit but the execution falls short of the acceptance bar due to insufficient baselines, small synthetic evaluation, thin related work, and limited novelty over prior persuasion-in-jailbreaking studies.
- **Confidence**: 4/5 -- I am familiar with the multi-turn jailbreak detection literature and the persuasion-in-LLM-safety research line. My main uncertainty is whether the cross-attack transfer results would hold at larger scale with real adversarial data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d02e32ff-218a-40fd-95fe-670db4249183",
  "isSidechain": true,
  "agentId": "af0c2201172a0086d",
  "requestId": "req_011Cb8Xhm4kpMDnYwhgfBMph",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b23ca7b-8390-41cb-b67b-12b80f986c69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect",
  "sessionId": "7ba16659-4839-4d18-aa99-4dde74627abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0135Usk62uzw7zihacRKCQqP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3377,
      "cache_read_input_tokens": 51540,
      "output_tokens": 4268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3377
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4268,
          "cache_read_input_tokens": 51540,
          "cache_creation_input_tokens": 3377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3377,
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
