# Research conversation: [Director 指令] [Patch — 关键新结果] exp-021 Oracle FOLIO 完成，论文最重要的证据之一 **结果摘要**： | Method | Accuracy | Delta vs SC | McNemar p — Part 5 of 102

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../research-conversation-director-patch-exp-021-oracle-folio-method-accuracy-delta-vs-sc-mcnemar-p-copy-2.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/ed/ed22009224401b440747.json)

## Round 30

### Tool call

_source line 1113 · 2026-05-17T19:29:02.263Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_012hqssi1dYEcWbJPRDadFoS`</summary>

```json
{
  "task_type": "paper_writing:conclusion",
  "project": "symb_invariant_consensus",
  "task_prompt": "## Task: Write Conclusion for EMNLP 2026 Paper\n\nWrite the Conclusion section (~350 words) for \"The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting\".\n\n### CRITICAL: Read These First\n1. `Read /home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n2. `Read /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex` (for framing consistency)\n3. `Read /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex` (for contribution list to echo)\n4. `Read /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex` (for constructive directions to echo)\n\n### Structure (~3 paragraphs)\n\n**Para 1 — Summary of findings**:\n- SICA provides no improvement over SC across 5 model families and 3 reasoning domains (N > 1,300)\n- BUT the oracle experiment demonstrates the aggregation mechanism IS sound: +8.82pp with gold FOL constraints (p < 0.001)\n- The bottleneck is localized to self-extraction quality, not the aggregation design\n- Frame as constructive diagnostic contribution, not just negative result\n\n**Para 2 — Practical implications**:\n- The capability trap: self-extracted constraints are non-discriminative (11.5% by count), reducing MAX-SAT to weighted vote counting (803/804 agreement with count-only)\n- 48.7% computational overhead for zero expected benefit\n- C0 diagnostic as practical tool for practitioners: compute before investing in extraction\n- The +8.82pp oracle gap is recoverable through external means\n\n**Para 3 — Future directions** (brief, 2-3 sentences):\n- Trained FOL extractors (supervised on FOLIO-style gold annotations)\n- Cross-model extraction (separate model extracts constraints from another's traces)\n- External provers that verify constraints independently of the reasoning model\n- Each path targets the extraction bottleneck identified by our analysis\n\n### Key Numbers (verified, must match Abstract and Introduction EXACTLY)\n- +8.82pp (oracle vs SC), p < 0.001\n- N > 1,300\n- 5 model families, 3 domains\n- 803/804 agreement MAX-SAT vs count-only\n- 11.5% discriminative constraints\n- 48.7% overhead\n\n### Writing Rules (HARD CONSTRAINTS)\n- NO em-dashes (— or –)\n- NO -ing phrase endings\n- NO \"In conclusion,\" / \"To summarize,\" / \"In summary,\"\n- Numbers must EXACTLY match Abstract and Introduction (precision, rounding)\n- Do NOT introduce new claims not supported by the paper\n- Do NOT overstate (\"state-of-the-art\", \"consistently outperforms\", \"novel\")\n- Keep it tight: ~350 words, no padding\n\n### Output\nWrite the complete LaTeX content for conclusion.tex. Start with \\section{Conclusion}\\label{sec:conclusion}. Output ONLY LaTeX, no commentary.\n\nWrite to: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex`\n",
  "tools": [
    "read_registry",
    "read_project_file"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abc1bcd9-3284-40f2-9d6b-9e0cafea5b85",
  "isSidechain": false,
  "requestId": "req_011Cb8hB6rBfjUe8sCqG4HGB",
  "type": "assistant",
  "uuid": "f541fc77-a6ae-46a0-85f2-667f47221a04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANdjh1A8XxmU9dZK7es19y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1248,
      "cache_read_input_tokens": 114685,
      "output_tokens": 983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1248,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 983,
          "cache_read_input_tokens": 114685,
          "cache_creation_input_tokens": 1248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1248
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

_source line 1114 · 2026-05-17T19:29:05.557Z_

<details><summary>↩ Tool result · `toolu_012hqssi1dYEcWbJPRDadFoS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_paper_writing_conclusion_20260517T192902.log\", \"setup_data\": {}, \"message\": \"Worker worker_paper_writing_conclusion_20260517T192902 started. Use get_worker_status('worker_paper_writing_conclusion_20260517T192902') to check progress.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f541fc77-a6ae-46a0-85f2-667f47221a04",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "e6f4b795-1786-4620-9a0f-72c500b8ab6d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_paper_writing_conclusion_20260517T192902.log\\\", \\\"setup_data\\\": {}, \\\"message\\\": \\\"Worker worker_paper_writing_conclusion_20260517T192902 started. Use get_worker_status('worker_paper_writing_conclusion_20260517T192902') to check progress.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_paper_writing_conclusion_20260517T192902.log\", \"setup_data\": {}, \"message\": \"Worker worker_paper_writing_conclusion_20260517T192902 started. Use get_worker_status('worker_paper_writing_conclusion_20260517T192902') to check progress.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f541fc77-a6ae-46a0-85f2-667f47221a04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1115 · 2026-05-17T19:29:12.394Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_011RK8tkTerDhM7WfcWN7VGx`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6f4b795-1786-4620-9a0f-72c500b8ab6d",
  "isSidechain": false,
  "requestId": "req_011Cb8hDR9pVdh118cQuvhvb",
  "type": "assistant",
  "uuid": "c161cb42-006c-4dc1-adcf-0d03ece40143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZL7efETXimKUvojWbwQCx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1171,
      "cache_read_input_tokens": 115933,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 115933,
          "cache_creation_input_tokens": 1171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1171
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

_source line 1116 · 2026-05-17T19:29:12.434Z_

<details><summary>↩ Tool result · `toolu_011RK8tkTerDhM7WfcWN7VGx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c161cb42-006c-4dc1-adcf-0d03ece40143",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "dbf5df0c-f611-4ac9-9d31-361687fe290a",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "c161cb42-006c-4dc1-adcf-0d03ece40143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1117 · 2026-05-17T19:29:24.403Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_013YG3Bmar1oaWwK8pCZi4r9`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbf5df0c-f611-4ac9-9d31-361687fe290a",
  "isSidechain": false,
  "requestId": "req_011Cb8hDvdMYEnam69YMXHu1",
  "type": "assistant",
  "uuid": "c127317d-dc6d-4c45-acfd-416bd5a13093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FUvQ7dGjxBbLjdPdqbCgy1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 117104,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 117104,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 1118 · 2026-05-17T19:29:24.459Z_

<details><summary>↩ Tool result · `toolu_013YG3Bmar1oaWwK8pCZi4r9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c127317d-dc6d-4c45-acfd-416bd5a13093",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "7d245a8e-93d6-4097-a6a6-b3028d3e7a71",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "c127317d-dc6d-4c45-acfd-416bd5a13093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1119 · 2026-05-17T19:29:27.051Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01HE1wxLWKP2kK5vb7W8jeRK`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d245a8e-93d6-4097-a6a6-b3028d3e7a71",
  "isSidechain": false,
  "requestId": "req_011Cb8hEpDB62hdWzuWbzgc9",
  "type": "assistant",
  "uuid": "70b217e9-e130-4320-8c7c-2482746d11e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kd4ncekJphhPUiCTAX4du",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 117338,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 117338,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 1120 · 2026-05-17T19:29:27.092Z_

<details><summary>↩ Tool result · `toolu_01HE1wxLWKP2kK5vb7W8jeRK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70b217e9-e130-4320-8c7c-2482746d11e6",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "bb6b77e0-7c52-43fb-bd98-cbb56acdc705",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "70b217e9-e130-4320-8c7c-2482746d11e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1121 · 2026-05-17T19:29:29.871Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01Fx9Ky5vwLHNpb2kGt8nwcR`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb6b77e0-7c52-43fb-bd98-cbb56acdc705",
  "isSidechain": false,
  "requestId": "req_011Cb8hF1LekxXhox3YKCD4U",
  "type": "assistant",
  "uuid": "b10803aa-1c80-43fa-a112-287fb17dad8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ke7U7ibfgksXaCzs9zHL7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 117572,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 117572,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 1122 · 2026-05-17T19:29:29.909Z_

<details><summary>↩ Tool result · `toolu_01Fx9Ky5vwLHNpb2kGt8nwcR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b10803aa-1c80-43fa-a112-287fb17dad8e",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "21b9b18a-9805-4a16-9ab8-fb843e160fb5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "b10803aa-1c80-43fa-a112-287fb17dad8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1123 · 2026-05-17T19:29:33.481Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01VL85b44JzC8JFtD8yjVnX8`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21b9b18a-9805-4a16-9ab8-fb843e160fb5",
  "isSidechain": false,
  "requestId": "req_011Cb8hFDJjhpBeycjzcfFuZ",
  "type": "assistant",
  "uuid": "711ace31-da87-42bb-9d3c-868f7c77bdbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAZ91hrtvyE7912nbSduhS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 117806,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 117806,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 1124 · 2026-05-17T19:29:33.521Z_

<details><summary>↩ Tool result · `toolu_01VL85b44JzC8JFtD8yjVnX8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "711ace31-da87-42bb-9d3c-868f7c77bdbb",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "d080f09e-e63f-4f6c-89c1-654c5f8d41c9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "711ace31-da87-42bb-9d3c-868f7c77bdbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1125 · 2026-05-17T19:29:35.840Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01VmZTbntP5w7HH8og6CpFah`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d080f09e-e63f-4f6c-89c1-654c5f8d41c9",
  "isSidechain": false,
  "requestId": "req_011Cb8hFUpdy5Qvjj4JQXy7s",
  "type": "assistant",
  "uuid": "f4e0dcd3-ed32-4fd4-b745-8c9dd3c88159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JR8S554WtUk6mth4y9NcTf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 118040,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 118040,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 1126 · 2026-05-17T19:29:35.883Z_

<details><summary>↩ Tool result · `toolu_01VmZTbntP5w7HH8og6CpFah`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4e0dcd3-ed32-4fd4-b745-8c9dd3c88159",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "6d375c66-55eb-401a-8e43-7c3ef209ceec",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f4e0dcd3-ed32-4fd4-b745-8c9dd3c88159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1127 · 2026-05-17T19:29:38.649Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_018APsiHPAnTpV92khVVPZTy`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d375c66-55eb-401a-8e43-7c3ef209ceec",
  "isSidechain": false,
  "requestId": "req_011Cb8hFessoarmPMWEJHrdG",
  "type": "assistant",
  "uuid": "cc71978f-57d2-4821-9dcd-1cfd73b202a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Zv3agyBEfhUbLb8EKPc6t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 118274,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 118274,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 1128 · 2026-05-17T19:29:38.687Z_

<details><summary>↩ Tool result · `toolu_018APsiHPAnTpV92khVVPZTy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc71978f-57d2-4821-9dcd-1cfd73b202a6",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "3eb3300e-bf7c-4db8-aba4-357ab0fe9862",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "cc71978f-57d2-4821-9dcd-1cfd73b202a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1129_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。",
  "leafUuid": "3eb3300e-bf7c-4db8-aba4-357ab0fe9862",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1130_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Tool call

_source line 1131 · 2026-05-17T19:29:42.691Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01JE3KYhtV3kFhEnbPWPfQK1`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eb3300e-bf7c-4db8-aba4-357ab0fe9862",
  "isSidechain": false,
  "requestId": "req_011Cb8hFrxu2N9SsJpJExXaM",
  "type": "assistant",
  "uuid": "86d8aad0-8b5a-490e-8e85-36f82557bec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxZv9fuHrV6fHCYtnPXtCM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 118508,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 118508,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 1132 · 2026-05-17T19:29:42.728Z_

<details><summary>↩ Tool result · `toolu_01JE3KYhtV3kFhEnbPWPfQK1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86d8aad0-8b5a-490e-8e85-36f82557bec9",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "c3edc7a8-f2ef-42c7-a1bf-46a407eeb69f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "86d8aad0-8b5a-490e-8e85-36f82557bec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1133 · 2026-05-17T19:29:42.753Z_

```json
{
  "parentUuid": "c3edc7a8-f2ef-42c7-a1bf-46a407eeb69f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "82f3f4df-eb57-426c-b249-b4021609f1b9",
  "timestamp": "2026-05-17T19:29:42.753Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Tool call

_source line 1134 · 2026-05-17T19:29:45.373Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01X19KXSPgPZJnhW7SrvWoez`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82f3f4df-eb57-426c-b249-b4021609f1b9",
  "isSidechain": false,
  "requestId": "req_011Cb8hGAAkGVx9txPxD8miG",
  "type": "assistant",
  "uuid": "73476bea-b93b-44bf-9c78-abeadbb2f2a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DPGmipNbZ6FrW2goTWwti",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 338,
      "cache_read_input_tokens": 118742,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 338,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 118742,
          "cache_creation_input_tokens": 338,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 338
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

_source line 1135 · 2026-05-17T19:29:45.422Z_

<details><summary>↩ Tool result · `toolu_01X19KXSPgPZJnhW7SrvWoez`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73476bea-b93b-44bf-9c78-abeadbb2f2a8",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "f8b5bbec-12dc-4749-865a-752890b0329f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "73476bea-b93b-44bf-9c78-abeadbb2f2a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1136 · 2026-05-17T19:29:52.370Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01Hm9ifXyNTEDGggfAHD1MHn`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8b5bbec-12dc-4749-865a-752890b0329f",
  "isSidechain": false,
  "requestId": "req_011Cb8hGMoExemX5NBNkyJba",
  "type": "assistant",
  "uuid": "eae1d612-bd1d-4c9d-8e98-266f781517b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rgaBhDvA9g9Y3bhXqmrKH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 119080,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 119080,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 1137 · 2026-05-17T19:29:52.416Z_

<details><summary>↩ Tool result · `toolu_01Hm9ifXyNTEDGggfAHD1MHn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eae1d612-bd1d-4c9d-8e98-266f781517b9",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "a56c093b-06a6-41a6-afe5-5cae1541d225",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "eae1d612-bd1d-4c9d-8e98-266f781517b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-17T19:29:56.004Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01J7YFYjyfJxfN8iS7Bs9dXL`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a56c093b-06a6-41a6-afe5-5cae1541d225",
  "isSidechain": false,
  "requestId": "req_011Cb8hGsfbd5fSSYb9uXgmJ",
  "type": "assistant",
  "uuid": "563f80d2-fd12-48ae-970d-4832db6d7a63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7VatWxZhpSkqrn2zAsyQC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 119314,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 119314,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 1139 · 2026-05-17T19:29:56.041Z_

<details><summary>↩ Tool result · `toolu_01J7YFYjyfJxfN8iS7Bs9dXL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "563f80d2-fd12-48ae-970d-4832db6d7a63",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "954e11bb-fb4a-45c1-88e6-99900e5920fd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "563f80d2-fd12-48ae-970d-4832db6d7a63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-17T19:29:59.767Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01NSjr1RA9HkZBFyXvZGd7nQ`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "954e11bb-fb4a-45c1-88e6-99900e5920fd",
  "isSidechain": false,
  "requestId": "req_011Cb8hH96Y5D8kjh8wgkkFf",
  "type": "assistant",
  "uuid": "bf7afa2e-ccdf-4ca1-8d4d-eaea2586bdc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZDdK3sbrrqD1wUd8BqnZn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 119548,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 119548,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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

_source line 1141 · 2026-05-17T19:29:59.803Z_

<details><summary>↩ Tool result · `toolu_01NSjr1RA9HkZBFyXvZGd7nQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf7afa2e-ccdf-4ca1-8d4d-eaea2586bdc5",
  "isSidechain": false,
  "promptId": "548375e5-fc44-4737-8dda-44f5ae13db2e",
  "type": "user",
  "uuid": "3fbae7a4-0007-43ff-954d-213fcda5fafa",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"running\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": null, \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"running\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "bf7afa2e-ccdf-4ca1-8d4d-eaea2586bdc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1142 · 2026-05-17T19:30:04.381Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_016Tw1eJfGfBgGBrUDfBm3th`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fbae7a4-0007-43ff-954d-213fcda5fafa",
  "isSidechain": false,
  "requestId": "req_011Cb8hHRCQbEpd2BpEkRw8A",
  "type": "assistant",
  "uuid": "0e2fc200-77cf-4922-ad33-54c50245bd83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zJoFphod7iGKf34YvT9QJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 119782,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 119782,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 234
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


### Runtime record

_source line 1143_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1144 · 2026-05-17T19:47:39.341Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T19:47:39.341Z",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "content": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：\n\nworker_id: worker_paper_figure_fig1_pipeline_20260517T172247\nproject: symb_invariant_consensus\n日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status: {'worker_id': 'worker_figure_fig1_pipeline_20260517T172412', 'verbose': True}\n\n请调用 get_worker_status('worker_paper_figure_fig1_pipeline_20260517T172247') 确认状态，并根据情况决定是等待、SSH 检查还是取消 worker。"
}
```

---


### Runtime record

_source line 1145 · 2026-05-17T19:47:39.342Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T19:47:39.342Z",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


## Round 31

## Round 31

2 recorded events


### User

_source line 1146 · 2026-05-17T19:47:39.331Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fbae7a4-0007-43ff-954d-213fcda5fafa",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "isMeta": true,
  "uuid": "837818f2-39b1-4532-9f0a-9ab4fc00b03f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1147 · 2026-05-17T19:47:39.331Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "837818f2-39b1-4532-9f0a-9ab4fc00b03f",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "8b7210a2-7c2f-4e36-9547-17109a1281af",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "id": "30f67fc2-39d0-4aa3-967b-063993bc8a9f",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 32

## Round 32

140 recorded events


### User

_source line 1148 · 2026-05-17T19:47:39.454Z_

[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：

worker_id: worker_paper_figure_fig1_pipeline_20260517T172247
project: symb_invariant_consensus
日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status: {'worker_id': 'worker_figure_fig1_pipeline_20260517T172412', 'verbose': True}

请调用 get_worker_status('worker_paper_figure_fig1_pipeline_20260517T172247') 确认状态，并根据情况决定是等待、SSH 检查还是取消 worker。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b7210a2-7c2f-4e36-9547-17109a1281af",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "db516def-a284-4da4-ac49-61364217b66a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1149 · 2026-05-17T19:48:09.308Z_

<details><summary>Logged reasoning block</summary>

```text
The alert is about an old worker (fig1_pipeline) that was from a previous session and is likely stale. The figure was already generated and registered. Let me check its status, but more importantly, I need to check on the Conclusion worker that I'm actually waiting for.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db516def-a284-4da4-ac49-61364217b66a",
  "isSidechain": false,
  "requestId": "req_011Cb8idXeH3EdS3je5Uf4sa",
  "type": "assistant",
  "uuid": "8c31d852-44db-4f19-ae54-fe130fb3dfd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1nQgPKp7m4PtdgKSjZ4F1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 120016,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 120016,
          "cache_creation_input_tokens": 204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 204
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


### Assistant

_source line 1150 · 2026-05-17T19:48:10.292Z_

旧 Worker 告警，fig1_pipeline 在之前 session 已完成并注册。让我确认两个 Worker 状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c31d852-44db-4f19-ae54-fe130fb3dfd1",
  "isSidechain": false,
  "requestId": "req_011Cb8idXeH3EdS3je5Uf4sa",
  "type": "assistant",
  "uuid": "a824855e-e938-4f48-b21c-665c53c9433f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1nQgPKp7m4PtdgKSjZ4F1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 120016,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 120016,
          "cache_creation_input_tokens": 204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 204
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

_source line 1151 · 2026-05-17T19:48:11.223Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01FKuUofJinitQCieop9Pb9C`</summary>

```json
{
  "worker_id": "worker_paper_figure_fig1_pipeline_20260517T172247"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a824855e-e938-4f48-b21c-665c53c9433f",
  "isSidechain": false,
  "requestId": "req_011Cb8idXeH3EdS3je5Uf4sa",
  "type": "assistant",
  "uuid": "708c0e37-44a6-47c4-b7da-dece07196950",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1nQgPKp7m4PtdgKSjZ4F1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 120016,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 120016,
          "cache_creation_input_tokens": 204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 204
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

_source line 1152 · 2026-05-17T19:48:11.230Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01T4EYFoZyrKfMR6FgjyDmCZ`</summary>

```json
{
  "worker_id": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "708c0e37-44a6-47c4-b7da-dece07196950",
  "isSidechain": false,
  "requestId": "req_011Cb8idXeH3EdS3je5Uf4sa",
  "type": "assistant",
  "uuid": "1a0a4c14-e10b-49a3-a5fd-d681e078c704",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1nQgPKp7m4PtdgKSjZ4F1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 120016,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 120016,
          "cache_creation_input_tokens": 204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 204
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

_source line 1153 · 2026-05-17T19:48:11.272Z_

<details><summary>↩ Tool result · `toolu_01FKuUofJinitQCieop9Pb9C`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_figure_fig1_pipeline_20260517T172247\", \"status\": \"cancelled\", \"task_type\": \"paper_figure:fig1_pipeline\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T17:22:47.639299+00:00\", \"ended_at\": \"2026-05-17T18:58:52.493108+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "708c0e37-44a6-47c4-b7da-dece07196950",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "c34663d3-de78-4704-9505-04a877535adf",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_figure_fig1_pipeline_20260517T172247\\\", \\\"status\\\": \\\"cancelled\\\", \\\"task_type\\\": \\\"paper_figure:fig1_pipeline\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T17:22:47.639299+00:00\\\", \\\"ended_at\\\": \\\"2026-05-17T18:58:52.493108+00:00\\\", \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_figure_fig1_pipeline_20260517T172247\", \"status\": \"cancelled\", \"task_type\": \"paper_figure:fig1_pipeline\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T17:22:47.639299+00:00\", \"ended_at\": \"2026-05-17T18:58:52.493108+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "708c0e37-44a6-47c4-b7da-dece07196950",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool result

_source line 1154 · 2026-05-17T19:48:11.313Z_

<details><summary>↩ Tool result · `toolu_01T4EYFoZyrKfMR6FgjyDmCZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"done\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": \"2026-05-17T19:31:11.363457+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"Done. `conclusion.tex` written at 346 words (including LaTeX commands). All required numbers match the Abstract and Introduction exactly, no em-dashes/en-dashes, no -ing phrase endings, no filler openers. Three paragraphs: findings summary with capability trap framing, practical implications with all key metrics, and future directions targeting the extraction bottleneck.\"}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a0a4c14-e10b-49a3-a5fd-d681e078c704",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "c9cf6e8e-3cf3-438b-aac2-800888c5fcd4",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_conclusion_20260517T192902\\\", \\\"status\\\": \\\"done\\\", \\\"task_type\\\": \\\"paper_writing:conclusion\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:29:02.909777+00:00\\\", \\\"ended_at\\\": \\\"2026-05-17T19:31:11.363457+00:00\\\", \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}, \\\"result\\\": {\\\"raw\\\": \\\"Done. `conclusion.tex` written at 346 words (including LaTeX commands). All required numbers match the Abstract and Introduction exactly, no em-dashes/en-dashes, no -ing phrase endings, no filler openers. Three paragraphs: findings summary with capability trap framing, practical implications with all key metrics, and future directions targeting the extraction bottleneck.\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_conclusion_20260517T192902\", \"status\": \"done\", \"task_type\": \"paper_writing:conclusion\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:29:02.909777+00:00\", \"ended_at\": \"2026-05-17T19:31:11.363457+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"Done. `conclusion.tex` written at 346 words (including LaTeX commands). All required numbers match the Abstract and Introduction exactly, no em-dashes/en-dashes, no -ing phrase endings, no filler openers. Three paragraphs: findings summary with capability trap framing, practical implications with all key metrics, and future directions targeting the extraction bottleneck.\"}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1a0a4c14-e10b-49a3-a5fd-d681e078c704",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1155 · 2026-05-17T19:48:15.516Z_

fig1_pipeline 是旧 Worker，已 cancelled，fig1 早已生成注册。Conclusion Worker 已完成。让我读取并验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9cf6e8e-3cf3-438b-aac2-800888c5fcd4",
  "isSidechain": false,
  "requestId": "req_011Cb8ifsm4DaM5Mq89Kfjin",
  "type": "assistant",
  "uuid": "07cd9bd2-2983-44ff-a8d3-38f07191bbfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BD8YjuXqM8o23iC6qZeT8r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 120220,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 120220,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 770
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

_source line 1156 · 2026-05-17T19:48:16.871Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LHd2XkSwBJjQs7MmZd2fMG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07cd9bd2-2983-44ff-a8d3-38f07191bbfb",
  "isSidechain": false,
  "requestId": "req_011Cb8ifsm4DaM5Mq89Kfjin",
  "type": "assistant",
  "uuid": "d821f007-3472-410b-ac39-34e38262fe90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BD8YjuXqM8o23iC6qZeT8r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 120220,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 120220,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 770
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

_source line 1157 · 2026-05-17T19:48:16.890Z_

<details><summary>↩ Tool result · `toolu_01LHd2XkSwBJjQs7MmZd2fMG`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluated Symbolic Invariant Consensus Aggregation across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. Self-extracted SICA provides no statistically significant improvement over Self-Consistency in any tested condition, with accuracy gaps ranging from $-3.3$ to $+3.3$\,pp. The oracle experiment, which replaces self-extraction with gold FOL annotations verified by Z3, achieves $+8.82$ percentage points over SC ($p < 0.001$). This result causally localizes the failure to extraction quality: the MAX-SAT aggregation mechanism is sound when supplied with high-quality constraints, but same-model self-extraction cannot produce them. We identify this as a \emph{capability trap}: because the reasoning model also extracts the constraints, those constraints inherit the same biases that produced potentially flawed answers and carry no independent discriminative signal. The failure is not one of aggregation design but of the circular dependency between generation and verification within a single model.
4	
5	The practical consequences are substantial. Only 11.5\% of self-extracted constraints evaluate differently across candidate answers; the remainder encode shared domain facts satisfied equally by every candidate. MAX-SAT agrees with count-only aggregation on 803 of 804 predictions, which confirms that satisfiability structure adds nothing when constraints are non-discriminative. Constraint extraction accounts for 48.7\% of total pipeline time and roughly doubles computational cost for zero expected accuracy benefit. For practitioners who evaluate constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic: it is computable from trace samples alone, before any investment in constraint extraction or solver invocation. Low $C_0$ rules out any possible SICA gain by construction, and high $C_0$ signals the need for a small-scale constraint quality audit before full deployment.
6	
7	The $+8.82$\,pp oracle gap quantifies recoverable potential and points to three concrete paths forward. Trained FOL extractors supervised on gold annotations (such as FOLIO) can learn extraction patterns beyond same-model capabilities. Cross-model extraction, where a separate model formalizes another model's traces, breaks the self-reference loop that produces non-discriminative constraints. External provers that verify constraints independently of the reasoning model eliminate the circular dependency entirely. Each path targets the extraction bottleneck directly; the aggregation mechanism requires no modification.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d821f007-3472-410b-ac39-34e38262fe90",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "3a7623b5-78ea-490a-b328-c11f523853dc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. Self-extracted SICA provides no statistically significant improvement over Self-Consistency in any tested condition, with accuracy gaps ranging from $-3.3$ to $+3.3$\\,pp. The oracle experiment, which replaces self-extraction with gold FOL annotations verified by Z3, achieves $+8.82$ percentage points over SC ($p < 0.001$). This result causally localizes the failure to extraction quality: the MAX-SAT aggregation mechanism is sound when supplied with high-quality constraints, but same-model self-extraction cannot produce them. We identify this as a \\emph{capability trap}: because the reasoning model also extracts the constraints, those constraints inherit the same biases that produced potentially flawed answers and carry no independent discriminative signal. The failure is not one of aggregation design but of the circular dependency between generation and verification within a single model.\n\nThe practical consequences are substantial. Only 11.5\\% of self-extracted constraints evaluate differently across candidate answers; the remainder encode shared domain facts satisfied equally by every candidate. MAX-SAT agrees with count-only aggregation on 803 of 804 predictions, which confirms that satisfiability structure adds nothing when constraints are non-discriminative. Constraint extraction accounts for 48.7\\% of total pipeline time and roughly doubles computational cost for zero expected accuracy benefit. For practitioners who evaluate constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic: it is computable from trace samples alone, before any investment in constraint extraction or solver invocation. Low $C_0$ rules out any possible SICA gain by construction, and high $C_0$ signals the need for a small-scale constraint quality audit before full deployment.\n\nThe $+8.82$\\,pp oracle gap quantifies recoverable potential and points to three concrete paths forward. Trained FOL extractors supervised on gold annotations (such as FOLIO) can learn extraction patterns beyond same-model capabilities. Cross-model extraction, where a separate model formalizes another model's traces, breaks the self-reference loop that produces non-discriminative constraints. External provers that verify constraints independently of the reasoning model eliminate the circular dependency entirely. Each path targets the extraction bottleneck directly; the aggregation mechanism requires no modification.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "d821f007-3472-410b-ac39-34e38262fe90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1158 · 2026-05-17T19:48:16.931Z_

```json
{
  "parentUuid": "3a7623b5-78ea-490a-b328-c11f523853dc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "825f6250-ef82-47f9-8fff-0dd5956361a9",
  "timestamp": "2026-05-17T19:48:16.931Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Assistant

_source line 1159 · 2026-05-17T19:48:24.820Z_

<details><summary>Logged reasoning block</summary>

```text
The Conclusion looks excellent. Let me verify:

1. Numbers match Abstract/Introduction:
   - +8.82pp ✓
   - p < 0.001 ✓
   - N > 1,300 ✓
   - 5 model families ✓
   - 3 domains ✓
   - 11.5% discriminative ✓
   - 803/804 agreement ✓
   - 48.7% overhead ✓
   - -3.3 to +3.3pp range ✓

2. Writing quality:
   - No em-dashes ✓
   - No -ing phrase endings ✓
   - No filler openers ✓
   - Oracle-positive framing ✓
   - ~346 words ✓

3. Structure:
   - Para 1: Findings summary + capability trap characterization ✓
   - Para 2: Practical implications + C0 diagnostic ✓
   - Para 3: Future directions ✓

Now I'll register the section and run a consistency check across the full paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "825f6250-ef82-47f9-8fff-0dd5956361a9",
  "isSidechain": false,
  "requestId": "req_011Cb8igHqQS2mCbYkwP33cG",
  "type": "assistant",
  "uuid": "c2901264-2d78-489d-9d9a-8fc7c10cf5c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcLZFFNK7YWnzGNAuTfj6a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 120990,
      "output_tokens": 1217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1217,
          "cache_read_input_tokens": 120990,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 816
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


### Assistant

_source line 1160 · 2026-05-17T19:48:24.822Z_

Conclusion verified: all numbers match Abstract/Introduction exactly, clean writing. Registering with provenance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2901264-2d78-489d-9d9a-8fc7c10cf5c6",
  "isSidechain": false,
  "requestId": "req_011Cb8igHqQS2mCbYkwP33cG",
  "type": "assistant",
  "uuid": "2d43b8a2-0a3f-4fdf-a1aa-87f3ee9ad22c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcLZFFNK7YWnzGNAuTfj6a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 120990,
      "output_tokens": 1217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1217,
          "cache_read_input_tokens": 120990,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 816
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

_source line 1161 · 2026-05-17T19:48:34.239Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__write_paper_section · `toolu_01LBUC7EAc9LurQ2QYmkTAaY`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "section": "conclusion",
  "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. Self-extracted SICA provides no statistically significant improvement over Self-Consistency in any tested condition, with accuracy gaps ranging from $-3.3$ to $+3.3$\\,pp. The oracle experiment, which replaces self-extraction with gold FOL annotations verified by Z3, achieves $+8.82$ percentage points over SC ($p < 0.001$). This result causally localizes the failure to extraction quality: the MAX-SAT aggregation mechanism is sound when supplied with high-quality constraints, but same-model self-extraction cannot produce them. We identify this as a \\emph{capability trap}: because the reasoning model also extracts the constraints, those constraints inherit the same biases that produced potentially flawed answers and carry no independent discriminative signal. The failure is not one of aggregation design but of the circular dependency between generation and verification within a single model.\n\nThe practical consequences are substantial. Only 11.5\\% of self-extracted constraints evaluate differently across candidate answers; the remainder encode shared domain facts satisfied equally by every candidate. MAX-SAT agrees with count-only aggregation on 803 of 804 predictions, which confirms that satisfiability structure adds nothing when constraints are non-discriminative. Constraint extraction accounts for 48.7\\% of total pipeline time and roughly doubles computational cost for zero expected accuracy benefit. For practitioners who evaluate constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic: it is computable from trace samples alone, before any investment in constraint extraction or solver invocation. Low $C_0$ rules out any possible SICA gain by construction, and high $C_0$ signals the need for a small-scale constraint quality audit before full deployment.\n\nThe $+8.82$\\,pp oracle gap quantifies recoverable potential and points to three concrete paths forward. Trained FOL extractors supervised on gold annotations (such as FOLIO) can learn extraction patterns beyond same-model capabilities. Cross-model extraction, where a separate model formalizes another model's traces, breaks the self-reference loop that produces non-discriminative constraints. External provers that verify constraints independently of the reasoning model eliminate the circular dependency entirely. Each path targets the extraction bottleneck directly; the aggregation mechanism requires no modification.",
  "claims": [
    {
      "text": "SICA provides no statistically significant improvement over SC, gaps -3.3 to +3.3pp",
      "type": "quantitative",
      "evidence": [
        "all conditions: delta n.s."
      ]
    },
    {
      "text": "Oracle achieves +8.82pp over SC (p<0.001)",
      "type": "quantitative",
      "evidence": [
        "exp-021-oracle-folio: oracle_vs_sc_delta_pp=8.82"
      ]
    },
    {
      "text": "11.5% of constraints evaluate differently across candidates",
      "type": "quantitative",
      "evidence": [
        "pilot-constraint-filtering: discriminative_ratio_count=0.115"
      ]
    },
    {
      "text": "MAX-SAT agrees with count-only on 803/804 predictions",
      "type": "quantitative",
      "evidence": [
        "sica_constraint_ablation_013: agreement=803/804"
      ]
    },
    {
      "text": "48.7% wall-clock overhead",
      "type": "quantitative",
      "evidence": [
        "exp-009-overhead-analysis: sica_overhead_pct=48.7"
      ]
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d43b8a2-0a3f-4fdf-a1aa-87f3ee9ad22c",
  "isSidechain": false,
  "requestId": "req_011Cb8igHqQS2mCbYkwP33cG",
  "type": "assistant",
  "uuid": "1d6f0211-b2b0-45f3-bd58-8852313602af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcLZFFNK7YWnzGNAuTfj6a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 120990,
      "output_tokens": 1217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1217,
          "cache_read_input_tokens": 120990,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 816
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

_source line 1162 · 2026-05-17T19:48:34.305Z_

<details><summary>↩ Tool result · `toolu_01LBUC7EAc9LurQ2QYmkTAaY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex\", \"provenance_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_provenance.yaml\", \"version\": 25, \"coverage\": \"27/27\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d6f0211-b2b0-45f3-bd58-8852313602af",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "ff5b1ee5-629b-475b-a607-ea9dac942a42",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"section_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex\\\", \\\"provenance_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_provenance.yaml\\\", \\\"version\\\": 25, \\\"coverage\\\": \\\"27/27\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex\", \"provenance_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_provenance.yaml\", \"version\": 25, \"coverage\": \"27/27\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1d6f0211-b2b0-45f3-bd58-8852313602af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1163_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：  worker_id: worker_paper_figure_fig1_pipeline_20260517T172247 project: symb_invariant_consensus 日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status…",
  "leafUuid": "ff5b1ee5-629b-475b-a607-ea9dac942a42",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1164_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 1165 · 2026-05-17T19:48:37.613Z_

All Phase 2 sections complete (v25, 27/27 coverage). Now running global consistency check.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff5b1ee5-629b-475b-a607-ea9dac942a42",
  "isSidechain": false,
  "requestId": "req_011Cb8iha5V6tToXEi7uj2NT",
  "type": "assistant",
  "uuid": "21590fda-4691-446d-8d1a-c57332c309f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhHB39LqEGk1cBN4ZnC5tJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1364,
      "cache_read_input_tokens": 121806,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1364,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 121806,
          "cache_creation_input_tokens": 1364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1364
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

_source line 1166 · 2026-05-17T19:48:38.171Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Y6fys2F6ifjLbNXmBySZgs`</summary>

```json
{
  "query": "select:check_paper_consistency",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21590fda-4691-446d-8d1a-c57332c309f1",
  "isSidechain": false,
  "requestId": "req_011Cb8iha5V6tToXEi7uj2NT",
  "type": "assistant",
  "uuid": "88bb3f1e-e685-482a-b834-c01275b58dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhHB39LqEGk1cBN4ZnC5tJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1364,
      "cache_read_input_tokens": 121806,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1364,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 121806,
          "cache_creation_input_tokens": 1364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1364
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

_source line 1167 · 2026-05-17T19:48:38.177Z_

<details><summary>↩ Tool result · `toolu_01Y6fys2F6ifjLbNXmBySZgs`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88bb3f1e-e685-482a-b834-c01275b58dd1",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "270fed5b-a790-4cc7-b569-2428ff26384d",
  "toolUseResult": {
    "matches": [],
    "query": "select:check_paper_consistency",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "88bb3f1e-e685-482a-b834-c01275b58dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1168 · 2026-05-17T19:48:42.440Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013xxGcXaiziixmDL5xVXt7n`</summary>

```json
{
  "query": "check_paper_consistency",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "270fed5b-a790-4cc7-b569-2428ff26384d",
  "isSidechain": false,
  "requestId": "req_011Cb8ihs1TzxjtpwTUKhma3",
  "type": "assistant",
  "uuid": "0685386f-920b-48ce-a201-55bd265d9f9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SwwQyX1KfTCDYPAdLLBq9v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 123170,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 123170,
          "cache_creation_input_tokens": 121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 121
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

_source line 1169 · 2026-05-17T19:48:42.453Z_

<details><summary>↩ Tool result · `toolu_013xxGcXaiziixmDL5xVXt7n`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__check_paper_consistency"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0685386f-920b-48ce-a201-55bd265d9f9a",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "a2c78f00-64c8-4aff-b098-eeb69e564b16",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__check_paper_consistency"
    ],
    "query": "check_paper_consistency",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "0685386f-920b-48ce-a201-55bd265d9f9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-17T19:48:46.413Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__check_paper_consistency · `toolu_01WnTwRf3fZv6AMA8rQvfFcz`</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2c78f00-64c8-4aff-b098-eeb69e564b16",
  "isSidechain": false,
  "requestId": "req_011Cb8iiBVDPW6aXVbfdHZHj",
  "type": "assistant",
  "uuid": "06ed0b6b-0662-4e14-a788-1394d5ed5610",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnrHnvFztyntST6Jinwsv4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 123291,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 71,
          "cache_read_input_tokens": 123291,
          "cache_creation_input_tokens": 385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 385
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

_source line 1171 · 2026-05-17T19:48:46.436Z_

<details><summary>↩ Tool result · `toolu_01WnTwRf3fZv6AMA8rQvfFcz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper\", \"sections\": [{\"file\": \"abstract.tex\", \"role\": \"headline\", \"num_numbers\": 3, \"num_cites\": 0}, {\"file\": \"conclusion.tex\", \"role\": \"headline\", \"num_numbers\": 7, \"num_cites\": 0}, {\"file\": \"discussion.tex\", \"role\": \"other\", \"num_numbers\": 9, \"num_cites\": 4}, {\"file\": \"experiments.tex\", \"role\": \"result\", \"num_numbers\": 99, \"num_cites\": 11}, {\"file\": \"introduction.tex\", \"role\": \"intro\", \"num_numbers\": 9, \"num_cites\": 17}, {\"file\": \"limitations_content.tex\", \"role\": \"other\", \"num_numbers\": 0, \"num_cites\": 0}, {\"file\": \"method.tex\", \"role\": \"other\", \"num_numbers\": 1, \"num_cites\": 5}, {\"file\": \"related_work.tex\", \"role\": \"other\", \"num_numbers\": 3, \"num_cites\": 24}], \"critical\": [], \"warning\": [{\"kind\": \"orphan_bib_key\", \"message\": \"references.bib entry 'hosseini2024vstar' is never cited.\", \"location\": \"references.bib\"}, {\"kind\": \"orphan_bib_key\", \"message\": \"references.bib entry 'mirzadeh2024gsmsymbolic' is never cited.\", \"location\": \"references.bib\"}], \"info\": [{\"kind\": \"notation_per_section\", \"message\": \"Inline math symbols collected per section.\", \"data\": {\"discussion\": [\"\\\\Delta\"], \"experiments\": [\"\\\\Delta\", \"\\\\alpha\", \"\\\\dagger\", \"\\\\ddagger\", \"\\\\geq\", \"\\\\in\", \"\\\\leq\", \"\\\\times\"], \"introduction\": [\"\\\\times\"], \"limitations_content\": [\"\\\\leq\"], \"method\": [\"\\\\approx\", \"\\\\arg\", \"\\\\in\", \"\\\\ldots\", \"\\\\max\", \"\\\\sigma\"]}}], \"summary\": {\"critical\": 0, \"warning\": 2, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06ed0b6b-0662-4e14-a788-1394d5ed5610",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "27da6d79-289f-491c-8b6b-18aa09a7bc4f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper\\\", \\\"sections\\\": [{\\\"file\\\": \\\"abstract.tex\\\", \\\"role\\\": \\\"headline\\\", \\\"num_numbers\\\": 3, \\\"num_cites\\\": 0}, {\\\"file\\\": \\\"conclusion.tex\\\", \\\"role\\\": \\\"headline\\\", \\\"num_numbers\\\": 7, \\\"num_cites\\\": 0}, {\\\"file\\\": \\\"discussion.tex\\\", \\\"role\\\": \\\"other\\\", \\\"num_numbers\\\": 9, \\\"num_cites\\\": 4}, {\\\"file\\\": \\\"experiments.tex\\\", \\\"role\\\": \\\"result\\\", \\\"num_numbers\\\": 99, \\\"num_cites\\\": 11}, {\\\"file\\\": \\\"introduction.tex\\\", \\\"role\\\": \\\"intro\\\", \\\"num_numbers\\\": 9, \\\"num_cites\\\": 17}, {\\\"file\\\": \\\"limitations_content.tex\\\", \\\"role\\\": \\\"other\\\", \\\"num_numbers\\\": 0, \\\"num_cites\\\": 0}, {\\\"file\\\": \\\"method.tex\\\", \\\"role\\\": \\\"other\\\", \\\"num_numbers\\\": 1, \\\"num_cites\\\": 5}, {\\\"file\\\": \\\"related_work.tex\\\", \\\"role\\\": \\\"other\\\", \\\"num_numbers\\\": 3, \\\"num_cites\\\": 24}], \\\"critical\\\": [], \\\"warning\\\": [{\\\"kind\\\": \\\"orphan_bib_key\\\", \\\"message\\\": \\\"references.bib entry 'hosseini2024vstar' is never cited.\\\", \\\"location\\\": \\\"references.bib\\\"}, {\\\"kind\\\": \\\"orphan_bib_key\\\", \\\"message\\\": \\\"references.bib entry 'mirzadeh2024gsmsymbolic' is never cited.\\\", \\\"location\\\": \\\"references.bib\\\"}], \\\"info\\\": [{\\\"kind\\\": \\\"notation_per_section\\\", \\\"message\\\": \\\"Inline math symbols collected per section.\\\", \\\"data\\\": {\\\"discussion\\\": [\\\"\\\\\\\\Delta\\\"], \\\"experiments\\\": [\\\"\\\\\\\\Delta\\\", \\\"\\\\\\\\alpha\\\", \\\"\\\\\\\\dagger\\\", \\\"\\\\\\\\ddagger\\\", \\\"\\\\\\\\geq\\\", \\\"\\\\\\\\in\\\", \\\"\\\\\\\\leq\\\", \\\"\\\\\\\\times\\\"], \\\"introduction\\\": [\\\"\\\\\\\\times\\\"], \\\"limitations_content\\\": [\\\"\\\\\\\\leq\\\"], \\\"method\\\": [\\\"\\\\\\\\approx\\\", \\\"\\\\\\\\arg\\\", \\\"\\\\\\\\in\\\", \\\"\\\\\\\\ldots\\\", \\\"\\\\\\\\max\\\", \\\"\\\\\\\\sigma\\\"]}}], \\\"summary\\\": {\\\"critical\\\": 0, \\\"warning\\\": 2, \\\"info\\\": 1}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper\", \"sections\": [{\"file\": \"abstract.tex\", \"role\": \"headline\", \"num_numbers\": 3, \"num_cites\": 0}, {\"file\": \"conclusion.tex\", \"role\": \"headline\", \"num_numbers\": 7, \"num_cites\": 0}, {\"file\": \"discussion.tex\", \"role\": \"other\", \"num_numbers\": 9, \"num_cites\": 4}, {\"file\": \"experiments.tex\", \"role\": \"result\", \"num_numbers\": 99, \"num_cites\": 11}, {\"file\": \"introduction.tex\", \"role\": \"intro\", \"num_numbers\": 9, \"num_cites\": 17}, {\"file\": \"limitations_content.tex\", \"role\": \"other\", \"num_numbers\": 0, \"num_cites\": 0}, {\"file\": \"method.tex\", \"role\": \"other\", \"num_numbers\": 1, \"num_cites\": 5}, {\"file\": \"related_work.tex\", \"role\": \"other\", \"num_numbers\": 3, \"num_cites\": 24}], \"critical\": [], \"warning\": [{\"kind\": \"orphan_bib_key\", \"message\": \"references.bib entry 'hosseini2024vstar' is never cited.\", \"location\": \"references.bib\"}, {\"kind\": \"orphan_bib_key\", \"message\": \"references.bib entry 'mirzadeh2024gsmsymbolic' is never cited.\", \"location\": \"references.bib\"}], \"info\": [{\"kind\": \"notation_per_section\", \"message\": \"Inline math symbols collected per section.\", \"data\": {\"discussion\": [\"\\\\Delta\"], \"experiments\": [\"\\\\Delta\", \"\\\\alpha\", \"\\\\dagger\", \"\\\\ddagger\", \"\\\\geq\", \"\\\\in\", \"\\\\leq\", \"\\\\times\"], \"introduction\": [\"\\\\times\"], \"limitations_content\": [\"\\\\leq\"], \"method\": [\"\\\\approx\", \"\\\\arg\", \"\\\\in\", \"\\\\ldots\", \"\\\\max\", \"\\\\sigma\"]}}], \"summary\": {\"critical\": 0, \"warning\": 2, \"info\": 1}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "06ed0b6b-0662-4e14-a788-1394d5ed5610",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1172 · 2026-05-17T19:49:00.963Z_

<details><summary>Logged reasoning block</summary>

```text
Consistency check results:
- **0 critical** 
- **2 warnings**: orphan bib keys for `hosseini2024vstar` and `mirzadeh2024gsmsymbolic` (never cited in tex files)
- **1 info**: notation summary (normal)

I need to fix the orphan bib warnings. Let me add citations for these two papers:

1. `hosseini2024vstar` - V-STaR, should be cited in related_work.tex under Verification and Reranking. Let me check if it was added by the Director's instruction but not cited.


2. `mirzadeh2024gsmsymbolic` - GSM-Symbolic, should be cited somewhere relevant. It's about limitations of mathematical reasoning - could go in experiments when discussing GSM8K, or in related work under negative results.

Let me check where these should be cited. The Director said to add hosseini2024vstar. Looking at the related_work.tex I already have in context, I need to verify if V-STaR is actually cited in the Verification paragraph or if I just added it to the bibliography without the citation.

I also made an edit earlier to add RASC/ReASC citations, so let me review the current state of related_work.tex to see what's already there. For mirzadeh2024gsmsymbolic, I should place it either in the experiments section when discussing GSM8K results or in related work to highlight negative results about mathematical reasoning limitations. Let me address both of these orphaned citations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27da6d79-289f-491c-8b6b-18aa09a7bc4f",
  "isSidechain": false,
  "requestId": "req_011Cb8iiU862tYx4Hmnt8YV2",
  "type": "assistant",
  "uuid": "f9e08020-9318-43b7-ba57-fde9cfcfd952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YpLoi9FagscQpjb8VMDLN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 123676,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 123676,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 784
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


### Assistant

_source line 1173 · 2026-05-17T19:49:00.964Z_

0 critical issues. 2 warnings for orphan bib entries. Let me fix them by adding citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9e08020-9318-43b7-ba57-fde9cfcfd952",
  "isSidechain": false,
  "requestId": "req_011Cb8iiU862tYx4Hmnt8YV2",
  "type": "assistant",
  "uuid": "abf13b98-1c24-4fc4-87f7-40a8440a7ddc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YpLoi9FagscQpjb8VMDLN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 123676,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 123676,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 784
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

_source line 1174 · 2026-05-17T19:49:01.566Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QBBixyU62Kznq3v27HHZnU`</summary>

```json
{
  "pattern": "hosseini2024vstar",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abf13b98-1c24-4fc4-87f7-40a8440a7ddc",
  "isSidechain": false,
  "requestId": "req_011Cb8iiU862tYx4Hmnt8YV2",
  "type": "assistant",
  "uuid": "783b0cf8-ce78-41f9-96d1-d3c124d2d08d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YpLoi9FagscQpjb8VMDLN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 123676,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 123676,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 784
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

_source line 1175 · 2026-05-17T19:49:01.584Z_

<details><summary>↩ Tool result · `toolu_01QBBixyU62Kznq3v27HHZnU`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "783b0cf8-ce78-41f9-96d1-d3c124d2d08d",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "912437f3-8e7f-418b-9766-8cf64997487d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "783b0cf8-ce78-41f9-96d1-d3c124d2d08d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1176 · 2026-05-17T19:49:02.513Z_

<details open><summary>🔧 Tool call — Grep · `toolu_012EG46CuvHc28wBKjne8wDb`</summary>

```json
{
  "pattern": "mirzadeh2024gsmsymbolic",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "912437f3-8e7f-418b-9766-8cf64997487d",
  "isSidechain": false,
  "requestId": "req_011Cb8iiU862tYx4Hmnt8YV2",
  "type": "assistant",
  "uuid": "a35984ed-2930-4e73-9876-8d670e291ca6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YpLoi9FagscQpjb8VMDLN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 123676,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 123676,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 784
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

_source line 1177 · 2026-05-17T19:49:02.537Z_

<details><summary>↩ Tool result · `toolu_012EG46CuvHc28wBKjne8wDb`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a35984ed-2930-4e73-9876-8d670e291ca6",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "a09bcc39-091d-4adf-a5a0-6c3b79ab877e",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "a35984ed-2930-4e73-9876-8d670e291ca6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1178 · 2026-05-17T19:49:09.050Z_

<details><summary>Logged reasoning block</summary>

```text
Both bib entries are orphans - never cited. Let me add citations:

1. `hosseini2024vstar` (V-STaR) - Should go in related_work.tex, Verification and Reranking paragraph. V-STaR trains verifiers for self-taught reasoners.

2. `mirzadeh2024gsmsymbolic` (GSM-Symbolic) - Could go in experiments.tex when discussing GSM8K limitations, or in related work under negative results. Actually, looking at related_work.tex, there's no specific "negative results" paragraph. It might fit in the discussion about SC limitations or in experiments when discussing GSM8K.


Now I'm checking the Verification paragraph in related_work.tex to see where V-STaR fits best.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a09bcc39-091d-4adf-a5a0-6c3b79ab877e",
  "isSidechain": false,
  "requestId": "req_011Cb8ijen4xE8WDeRKZBbHT",
  "type": "assistant",
  "uuid": "16b8d54a-d94c-48ba-9456-acbe6302e4bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvML7uWcHnTx9gZFmhJWeY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 124460,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 322,
          "cache_read_input_tokens": 124460,
          "cache_creation_input_tokens": 809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 809
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

_source line 1179 · 2026-05-17T19:49:09.062Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T4eaJNHUULEwuMQCyJRxRB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex",
  "offset": 13,
  "limit": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16b8d54a-d94c-48ba-9456-acbe6302e4bd",
  "isSidechain": false,
  "requestId": "req_011Cb8ijen4xE8WDeRKZBbHT",
  "type": "assistant",
  "uuid": "2ceca554-8d7c-4729-99b8-a9fce621ca1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvML7uWcHnTx9gZFmhJWeY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 124460,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 322,
          "cache_read_input_tokens": 124460,
          "cache_creation_input_tokens": 809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 809
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

_source line 1180 · 2026-05-17T19:49:09.074Z_

<details><summary>↩ Tool result · `toolu_01T4eaJNHUULEwuMQCyJRxRB`</summary>

```text
13	\paragraph{Verification and Reranking.}
14	Trained verifiers offer an alternative path to improving multi-path reasoning. Outcome-level reward models (ORMs) score complete solutions and select the highest-ranked candidate \citep{cobbe2021gsm8k}. Process reward models (PRMs) assign step-level scores and enable finer-grained selection \citep{lightman2023prm}. Math-Shepherd automates process supervision annotation and removes the need for human labels \citep{wang2024mathshepherd}. Reasoning-aware variants score individual reasoning paths rather than training separate verifiers: RASC assigns confidence scores based on textual quality indicators and consistency \citep{wan2024rasc}, while ReASC frames adaptive sampling as evidence sufficiency and aggregates response-level confidence \citep{kim2026reasc}. These approaches share SICA's goal of selecting better answers from a candidate pool but differ in that they either train a separate scoring model or use lightweight heuristics grounded in textual features rather than formal logic. SICA's constraint extraction requires no training data and no additional model; it relies entirely on the reasoning model's own ability to formalize its logic. Our results suggest that this self-reliance is precisely the problem. Without an external signal to ground constraint quality, self-extracted constraints encode the same biases present in the original traces and fail to provide corrective information.
15	
16	\paragraph{Constraint Satisfaction in NLP.}
17	Constraint-based formulations have gained traction for evaluating and improving LLM reasoning. SATBench benchmarks LLMs on Boolean satisfiability problems and reveals systematic weaknesses in logical structure handling \citep{satbench2025}. Work on integrating LLMs with constraint propagation solvers explores hybrid architectures where the LLM generates candidate assignments and a CP solver enforces hard constraints \citep{llmmeets_cp2025}. SICA's MAX-SAT formulation sits within this broader trend: it uses Z3 to find the maximum-weight satisfiable subset of self-extracted constraints. The key difference is that SICA's constraints originate from the model's own reasoning traces rather than from problem specifications or external knowledge bases. Our finding that these self-extracted constraints lack discriminative power complements the SATBench results: LLMs struggle both to solve formal constraints directly and to produce useful constraints from their own reasoning.
18	
19	\paragraph{Debate and Multi-Agent Aggregation.}
20	Multi-agent debate refines answers through iterative natural language discussion among LLM instances \citep{liang2023encouraging,du2023improving}. In debate, models exchange arguments in plain text and update their positions based on peer responses. SICA takes a structurally different approach: instead of natural language refinement, it extracts formal constraints and resolves disagreements through satisfiability optimization. Both families attempt to move beyond simple voting, but debate preserves natural language flexibility while SICA commits to formal structure. \citet{huang2024selfcorrect} show that LLMs struggle to self-correct reasoning without external feedback, a finding that parallels our capability trap: the same model that produced flawed reasoning cannot reliably formalize the correction. Across all six lines of work reviewed here, the consistent pattern is that improving on majority voting requires information beyond what the reasoning model can extract from its own outputs, whether from trained verifiers, external solvers, human annotations, or cross-model interaction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ceca554-8d7c-4729-99b8-a9fce621ca1d",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "b2bfe194-361e-434b-867c-965571d28723",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex",
      "content": "\\paragraph{Verification and Reranking.}\nTrained verifiers offer an alternative path to improving multi-path reasoning. Outcome-level reward models (ORMs) score complete solutions and select the highest-ranked candidate \\citep{cobbe2021gsm8k}. Process reward models (PRMs) assign step-level scores and enable finer-grained selection \\citep{lightman2023prm}. Math-Shepherd automates process supervision annotation and removes the need for human labels \\citep{wang2024mathshepherd}. Reasoning-aware variants score individual reasoning paths rather than training separate verifiers: RASC assigns confidence scores based on textual quality indicators and consistency \\citep{wan2024rasc}, while ReASC frames adaptive sampling as evidence sufficiency and aggregates response-level confidence \\citep{kim2026reasc}. These approaches share SICA's goal of selecting better answers from a candidate pool but differ in that they either train a separate scoring model or use lightweight heuristics grounded in textual features rather than formal logic. SICA's constraint extraction requires no training data and no additional model; it relies entirely on the reasoning model's own ability to formalize its logic. Our results suggest that this self-reliance is precisely the problem. Without an external signal to ground constraint quality, self-extracted constraints encode the same biases present in the original traces and fail to provide corrective information.\n\n\\paragraph{Constraint Satisfaction in NLP.}\nConstraint-based formulations have gained traction for evaluating and improving LLM reasoning. SATBench benchmarks LLMs on Boolean satisfiability problems and reveals systematic weaknesses in logical structure handling \\citep{satbench2025}. Work on integrating LLMs with constraint propagation solvers explores hybrid architectures where the LLM generates candidate assignments and a CP solver enforces hard constraints \\citep{llmmeets_cp2025}. SICA's MAX-SAT formulation sits within this broader trend: it uses Z3 to find the maximum-weight satisfiable subset of self-extracted constraints. The key difference is that SICA's constraints originate from the model's own reasoning traces rather than from problem specifications or external knowledge bases. Our finding that these self-extracted constraints lack discriminative power complements the SATBench results: LLMs struggle both to solve formal constraints directly and to produce useful constraints from their own reasoning.\n\n\\paragraph{Debate and Multi-Agent Aggregation.}\nMulti-agent debate refines answers through iterative natural language discussion among LLM instances \\citep{liang2023encouraging,du2023improving}. In debate, models exchange arguments in plain text and update their positions based on peer responses. SICA takes a structurally different approach: instead of natural language refinement, it extracts formal constraints and resolves disagreements through satisfiability optimization. Both families attempt to move beyond simple voting, but debate preserves natural language flexibility while SICA commits to formal structure. \\citet{huang2024selfcorrect} show that LLMs struggle to self-correct reasoning without external feedback, a finding that parallels our capability trap: the same model that produced flawed reasoning cannot reliably formalize the correction. Across all six lines of work reviewed here, the consistent pattern is that improving on majority voting requires information beyond what the reasoning model can extract from its own outputs, whether from trained verifiers, external solvers, human annotations, or cross-model interaction.",
      "numLines": 8,
      "startLine": 13,
      "totalLines": 20
    }
  },
  "sourceToolAssistantUUID": "2ceca554-8d7c-4729-99b8-a9fce621ca1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1181 · 2026-05-17T19:49:09.127Z_

```json
{
  "parentUuid": "b2bfe194-361e-434b-867c-965571d28723",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5c5a47ad-83f7-45ec-9c64-6be081f0af5e",
  "timestamp": "2026-05-17T19:49:09.127Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 1182_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：  worker_id: worker_paper_figure_fig1_pipeline_20260517T172247 project: symb_invariant_consensus 日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status…",
  "leafUuid": "5c5a47ad-83f7-45ec-9c64-6be081f0af5e",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1183_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 1184 · 2026-05-17T19:49:17.916Z_

Adding V-STaR citation to the Verification paragraph and GSM-Symbolic to the appropriate location.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c5a47ad-83f7-45ec-9c64-6be081f0af5e",
  "isSidechain": false,
  "requestId": "req_011Cb8ik8yiFUVFRt9UVViZ2",
  "type": "assistant",
  "uuid": "8588746e-043c-4463-a8ed-520a1b1a32e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXcao1cMh3p5mSYnQ1qdA4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1222,
      "cache_read_input_tokens": 125269,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 240,
          "cache_read_input_tokens": 125269,
          "cache_creation_input_tokens": 1222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1222
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

_source line 1185 · 2026-05-17T19:49:19.975Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section · `toolu_01CFC3fiCtUGy7Ssf8ykbQFu`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "section": "related_work",
  "old_text": "Math-Shepherd automates process supervision annotation and removes the need for human labels \\citep{wang2024mathshepherd}.",
  "new_text": "Math-Shepherd automates process supervision annotation and removes the need for human labels \\citep{wang2024mathshepherd}. V-STaR extends self-improvement by training verifiers on both correct and incorrect model-generated solutions \\citep{hosseini2024vstar}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8588746e-043c-4463-a8ed-520a1b1a32e7",
  "isSidechain": false,
  "requestId": "req_011Cb8ik8yiFUVFRt9UVViZ2",
  "type": "assistant",
  "uuid": "54d6fa6b-bcff-4454-8476-3c19d39843c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXcao1cMh3p5mSYnQ1qdA4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1222,
      "cache_read_input_tokens": 125269,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 240,
          "cache_read_input_tokens": 125269,
          "cache_creation_input_tokens": 1222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1222
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

_source line 1186 · 2026-05-17T19:49:20.035Z_

<details><summary>↩ Tool result · `toolu_01CFC3fiCtUGy7Ssf8ykbQFu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex\", \"version\": 26, \"coverage\": \"27/27\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54d6fa6b-bcff-4454-8476-3c19d39843c6",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "f4d477e0-8d6d-48a9-9798-8553e7ecbc1f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"section_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex\\\", \\\"version\\\": 26, \\\"coverage\\\": \\\"27/27\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex\", \"version\": 26, \"coverage\": \"27/27\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "54d6fa6b-bcff-4454-8476-3c19d39843c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1187 · 2026-05-17T19:49:23.326Z_

Now adding GSM-Symbolic citation. It fits naturally in the Debate paragraph where self-correction is discussed, or in experiments. Let me add it to the self-correction sentence in the Debate paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4d477e0-8d6d-48a9-9798-8553e7ecbc1f",
  "isSidechain": false,
  "requestId": "req_011Cb8ikwYu8bhGwqh36GYyK",
  "type": "assistant",
  "uuid": "e20227c6-1dd9-434c-96d4-f1fae88e7cb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvTy3ZTVa9EM46VGzo3uXE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 344,
      "cache_read_input_tokens": 126491,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 126491,
          "cache_creation_input_tokens": 344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 344
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

_source line 1188 · 2026-05-17T19:49:25.656Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__edit_paper_section · `toolu_012adhH5ypLtNRH5WqqLcscj`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "section": "related_work",
  "old_text": "\\citet{huang2024selfcorrect} show that LLMs struggle to self-correct reasoning without external feedback, a finding that parallels our capability trap: the same model that produced flawed reasoning cannot reliably formalize the correction.",
  "new_text": "\\citet{huang2024selfcorrect} show that LLMs struggle to self-correct reasoning without external feedback, and \\citet{mirzadeh2024gsmsymbolic} demonstrate that LLM mathematical reasoning is fragile under symbolic perturbations. Both findings parallel our capability trap: the same model that produced flawed reasoning cannot reliably formalize the correction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e20227c6-1dd9-434c-96d4-f1fae88e7cb5",
  "isSidechain": false,
  "requestId": "req_011Cb8ikwYu8bhGwqh36GYyK",
  "type": "assistant",
  "uuid": "392b5828-8114-4fd2-8751-31fb21f4b8e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvTy3ZTVa9EM46VGzo3uXE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 344,
      "cache_read_input_tokens": 126491,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 126491,
          "cache_creation_input_tokens": 344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 344
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

_source line 1189 · 2026-05-17T19:49:25.717Z_

<details><summary>↩ Tool result · `toolu_012adhH5ypLtNRH5WqqLcscj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex\", \"version\": 27, \"coverage\": \"27/27\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "392b5828-8114-4fd2-8751-31fb21f4b8e9",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "7f329cfe-8377-4253-be93-ceb75b2f3803",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"section_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex\\\", \\\"version\\\": 27, \\\"coverage\\\": \\\"27/27\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex\", \"version\": 27, \"coverage\": \"27/27\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "392b5828-8114-4fd2-8751-31fb21f4b8e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1190 · 2026-05-17T19:49:29.149Z_

Both orphans fixed. Let me re-run consistency check to confirm.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f329cfe-8377-4253-be93-ceb75b2f3803",
  "isSidechain": false,
  "requestId": "req_011Cb8imMvMwnPmMf4Sx2Eh1",
  "type": "assistant",
  "uuid": "d087c47a-cf9d-4d6e-a778-7f8e2a48e07f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UL36uAdGA67MxUgM5cXnX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 126835,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 126835,
          "cache_creation_input_tokens": 407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 407
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

_source line 1191 · 2026-05-17T19:49:29.154Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__check_paper_consistency · `toolu_01WhKjf3JwA3bqsnqMW6Khtp`</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d087c47a-cf9d-4d6e-a778-7f8e2a48e07f",
  "isSidechain": false,
  "requestId": "req_011Cb8imMvMwnPmMf4Sx2Eh1",
  "type": "assistant",
  "uuid": "93e8be59-b7fa-4e8f-87fc-4223b23350cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UL36uAdGA67MxUgM5cXnX9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 126835,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 126835,
          "cache_creation_input_tokens": 407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 407
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

_source line 1192 · 2026-05-17T19:49:29.168Z_

<details><summary>↩ Tool result · `toolu_01WhKjf3JwA3bqsnqMW6Khtp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper\", \"sections\": [{\"file\": \"abstract.tex\", \"role\": \"headline\", \"num_numbers\": 3, \"num_cites\": 0}, {\"file\": \"conclusion.tex\", \"role\": \"headline\", \"num_numbers\": 7, \"num_cites\": 0}, {\"file\": \"discussion.tex\", \"role\": \"other\", \"num_numbers\": 9, \"num_cites\": 4}, {\"file\": \"experiments.tex\", \"role\": \"result\", \"num_numbers\": 99, \"num_cites\": 11}, {\"file\": \"introduction.tex\", \"role\": \"intro\", \"num_numbers\": 9, \"num_cites\": 17}, {\"file\": \"limitations_content.tex\", \"role\": \"other\", \"num_numbers\": 0, \"num_cites\": 0}, {\"file\": \"method.tex\", \"role\": \"other\", \"num_numbers\": 1, \"num_cites\": 5}, {\"file\": \"related_work.tex\", \"role\": \"other\", \"num_numbers\": 3, \"num_cites\": 26}], \"critical\": [], \"warning\": [], \"info\": [{\"kind\": \"notation_per_section\", \"message\": \"Inline math symbols collected per section.\", \"data\": {\"discussion\": [\"\\\\Delta\"], \"experiments\": [\"\\\\Delta\", \"\\\\alpha\", \"\\\\dagger\", \"\\\\ddagger\", \"\\\\geq\", \"\\\\in\", \"\\\\leq\", \"\\\\times\"], \"introduction\": [\"\\\\times\"], \"limitations_content\": [\"\\\\leq\"], \"method\": [\"\\\\approx\", \"\\\\arg\", \"\\\\in\", \"\\\\ldots\", \"\\\\max\", \"\\\\sigma\"]}}], \"summary\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93e8be59-b7fa-4e8f-87fc-4223b23350cb",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "2d834a4a-814a-48f9-bce3-fbd8c53e34a8",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper\\\", \\\"sections\\\": [{\\\"file\\\": \\\"abstract.tex\\\", \\\"role\\\": \\\"headline\\\", \\\"num_numbers\\\": 3, \\\"num_cites\\\": 0}, {\\\"file\\\": \\\"conclusion.tex\\\", \\\"role\\\": \\\"headline\\\", \\\"num_numbers\\\": 7, \\\"num_cites\\\": 0}, {\\\"file\\\": \\\"discussion.tex\\\", \\\"role\\\": \\\"other\\\", \\\"num_numbers\\\": 9, \\\"num_cites\\\": 4}, {\\\"file\\\": \\\"experiments.tex\\\", \\\"role\\\": \\\"result\\\", \\\"num_numbers\\\": 99, \\\"num_cites\\\": 11}, {\\\"file\\\": \\\"introduction.tex\\\", \\\"role\\\": \\\"intro\\\", \\\"num_numbers\\\": 9, \\\"num_cites\\\": 17}, {\\\"file\\\": \\\"limitations_content.tex\\\", \\\"role\\\": \\\"other\\\", \\\"num_numbers\\\": 0, \\\"num_cites\\\": 0}, {\\\"file\\\": \\\"method.tex\\\", \\\"role\\\": \\\"other\\\", \\\"num_numbers\\\": 1, \\\"num_cites\\\": 5}, {\\\"file\\\": \\\"related_work.tex\\\", \\\"role\\\": \\\"other\\\", \\\"num_numbers\\\": 3, \\\"num_cites\\\": 26}], \\\"critical\\\": [], \\\"warning\\\": [], \\\"info\\\": [{\\\"kind\\\": \\\"notation_per_section\\\", \\\"message\\\": \\\"Inline math symbols collected per section.\\\", \\\"data\\\": {\\\"discussion\\\": [\\\"\\\\\\\\Delta\\\"], \\\"experiments\\\": [\\\"\\\\\\\\Delta\\\", \\\"\\\\\\\\alpha\\\", \\\"\\\\\\\\dagger\\\", \\\"\\\\\\\\ddagger\\\", \\\"\\\\\\\\geq\\\", \\\"\\\\\\\\in\\\", \\\"\\\\\\\\leq\\\", \\\"\\\\\\\\times\\\"], \\\"introduction\\\": [\\\"\\\\\\\\times\\\"], \\\"limitations_content\\\": [\\\"\\\\\\\\leq\\\"], \\\"method\\\": [\\\"\\\\\\\\approx\\\", \\\"\\\\\\\\arg\\\", \\\"\\\\\\\\in\\\", \\\"\\\\\\\\ldots\\\", \\\"\\\\\\\\max\\\", \\\"\\\\\\\\sigma\\\"]}}], \\\"summary\\\": {\\\"critical\\\": 0, \\\"warning\\\": 0, \\\"info\\\": 1}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper\", \"sections\": [{\"file\": \"abstract.tex\", \"role\": \"headline\", \"num_numbers\": 3, \"num_cites\": 0}, {\"file\": \"conclusion.tex\", \"role\": \"headline\", \"num_numbers\": 7, \"num_cites\": 0}, {\"file\": \"discussion.tex\", \"role\": \"other\", \"num_numbers\": 9, \"num_cites\": 4}, {\"file\": \"experiments.tex\", \"role\": \"result\", \"num_numbers\": 99, \"num_cites\": 11}, {\"file\": \"introduction.tex\", \"role\": \"intro\", \"num_numbers\": 9, \"num_cites\": 17}, {\"file\": \"limitations_content.tex\", \"role\": \"other\", \"num_numbers\": 0, \"num_cites\": 0}, {\"file\": \"method.tex\", \"role\": \"other\", \"num_numbers\": 1, \"num_cites\": 5}, {\"file\": \"related_work.tex\", \"role\": \"other\", \"num_numbers\": 3, \"num_cites\": 26}], \"critical\": [], \"warning\": [], \"info\": [{\"kind\": \"notation_per_section\", \"message\": \"Inline math symbols collected per section.\", \"data\": {\"discussion\": [\"\\\\Delta\"], \"experiments\": [\"\\\\Delta\", \"\\\\alpha\", \"\\\\dagger\", \"\\\\ddagger\", \"\\\\geq\", \"\\\\in\", \"\\\\leq\", \"\\\\times\"], \"introduction\": [\"\\\\times\"], \"limitations_content\": [\"\\\\leq\"], \"method\": [\"\\\\approx\", \"\\\\arg\", \"\\\\in\", \"\\\\ldots\", \"\\\\max\", \"\\\\sigma\"]}}], \"summary\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "93e8be59-b7fa-4e8f-87fc-4223b23350cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1193 · 2026-05-17T19:49:33.329Z_

**0 critical, 0 warning, 1 info** (notation summary only). All sections consistent. Step 4 complete. Now let me try compiling the paper and then enter Step 5 (Iterative Refinement).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d834a4a-814a-48f9-bce3-fbd8c53e34a8",
  "isSidechain": false,
  "requestId": "req_011Cb8imcmaFWhBm2z6VvLin",
  "type": "assistant",
  "uuid": "c6f8c5d4-bcde-44ca-a835-0a5fea9ba945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvXY4ZWwNsMedRTRkmoaum",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 127242,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 127242,
          "cache_creation_input_tokens": 691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 691
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

_source line 1194 · 2026-05-17T19:49:33.926Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EpmQ3xFWgFP8F11MQk2E68`</summary>

```json
{
  "query": "select:paper_compile_and_check",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6f8c5d4-bcde-44ca-a835-0a5fea9ba945",
  "isSidechain": false,
  "requestId": "req_011Cb8imcmaFWhBm2z6VvLin",
  "type": "assistant",
  "uuid": "2da06600-a5a1-44eb-9943-89a5c850aa18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvXY4ZWwNsMedRTRkmoaum",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 127242,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 127242,
          "cache_creation_input_tokens": 691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 691
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

_source line 1195 · 2026-05-17T19:49:33.929Z_

<details><summary>↩ Tool result · `toolu_01EpmQ3xFWgFP8F11MQk2E68`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2da06600-a5a1-44eb-9943-89a5c850aa18",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "1af05ec2-1d48-4b40-8dce-977ae70e37eb",
  "toolUseResult": {
    "matches": [],
    "query": "select:paper_compile_and_check",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "2da06600-a5a1-44eb-9943-89a5c850aa18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-17T19:49:36.848Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SesCJUTu78Xq9iw97bQyMK`</summary>

```json
{
  "query": "paper_compile_and_check",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1af05ec2-1d48-4b40-8dce-977ae70e37eb",
  "isSidechain": false,
  "requestId": "req_011Cb8imyBuBw3WzkvRKFi4L",
  "type": "assistant",
  "uuid": "013d6a54-1b13-49be-b1c3-0767386d315d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQWtxR5bgyp6dVEqqh9EMT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 152,
      "cache_read_input_tokens": 127933,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 127933,
          "cache_creation_input_tokens": 152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 152
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

_source line 1197 · 2026-05-17T19:49:36.853Z_

<details><summary>↩ Tool result · `toolu_01SesCJUTu78Xq9iw97bQyMK`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__paper_compile_and_check"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "013d6a54-1b13-49be-b1c3-0767386d315d",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "f5d28c34-1dae-4f6c-820a-8cca9b2ee638",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__paper_compile_and_check"
    ],
    "query": "paper_compile_and_check",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "013d6a54-1b13-49be-b1c3-0767386d315d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-17T19:49:43.103Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01YGfUjaMurY2HBiTArbhpce`</summary>

```json
{
  "project": "symb_invariant_consensus",
  "max_pages": 8,
  "clean": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5d28c34-1dae-4f6c-820a-8cca9b2ee638",
  "isSidechain": false,
  "requestId": "req_011Cb8inBhEMRCDhBchg9PDp",
  "type": "assistant",
  "uuid": "f63035df-f472-412b-a519-72eaf02c45fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvJpaKVr41zE1bo6HcBfZF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 128085,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 820,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 128085,
          "cache_creation_input_tokens": 820,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 820
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

_source line 1199 · 2026-05-17T19:49:48.304Z_

<details><summary>↩ Tool result · `toolu_01YGfUjaMurY2HBiTArbhpce`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--135\\n\\\\T1/pcr/m/n/10.95 answer_assertion \\\\T1/ptm/m/n/10.95 (+20) con-straint per trac\\ne\\n []\\n\\n\\nOverfull \\\\hbox (81.88095pt too wide) in paragraph at lines 156--172\\n [][] \\n []\\n\\n\\nLaTeX Warning: `h' float specifier changed to `ht'.\\n\\n\\nOverfull \\\\hbox (37.0624pt too wide) in paragraph at lines 185--194\\n [][] \\n []\\n\\n\\nLaTeX Warning: `h' float specifier changed to `ht'.\\n\\n[11]\\nUnderfull \\\\hbox (badness 6445) in paragraph at lines 204--205\\n\\\\T1/ptm/m/n/10.95 (+20) We com-pute 95% con-fi-dence in-ter-vals for\\n []\\n\\n\\nOverfull \\\\hbox (18.84132pt too wide) in paragraph at lines 209--218\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1231) in paragraph at lines 218--218\\n[]\\\\T1/ptm/m/n/10 (+20) Table 5: |Boot-strap 95% con-fi-dence in-ter-vals for\\n []\\n\\n) [12] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 43A4ADD1E45E7DCB23598040EFB8E1C6;3532.\\n ) \\nHere is how much of TeX's memory you used:\\n 29934 strings out of 469438\\n 545606 string characters out of 5468411\\n 1401926 words of memory out of 5000000\\n 57520 multiletter control sequences out of 15000+600000\\n 707030 words of font info for 370 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,94p,1757b,1661s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texl\\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/tex\\nmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist\\n/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\ntype1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\\nublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\\nmsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\\ncm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/share/texli\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/cour\\nier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (12 pages, 360520 bytes).\\nPDF statistics:\\n 756 PDF objects out of 1000 (max. 8388607)\\n 605 compressed objects within 7 object streams\\n 213 named destinations out of 1000 (max. 500000)\\n 75447 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 12, \"warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\"]}, \"pages\": 12, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Underfull \\\\hbox (badness 3792) in paragraph at lines 16--17\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 3746) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1127) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 3068) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1077) in paragraph at lines 17--18\", \"Overfull \\\\hbox (80.368pt too wide) in paragraph at lines 44--45\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1377) in paragraph at lines 9--10\", \"Underfull \\\\vbox (badness 2189) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 79--79\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 86--90\", \"Underfull \\\\hbox (badness 1365) in paragraph at lines 86--90\", \"Underfull \\\\hbox (badness 1377) in paragraph at lines 142--146\", \"Underfull \\\\hbox (badness 3281) in paragraph at lines 177--181\", \"Underfull \\\\hbox (badness 1424) in paragraph at lines 177--181\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 177--181\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 209--214\", \"Underfull \\\\hbox (badness 7722) in paragraph at lines 18--19\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 61--62\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 61--62\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--135\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--135\", \"Overfull \\\\hbox (81.88095pt too wide) in paragraph at lines 156--172\", \"Overfull \\\\hbox (37.0624pt too wide) in paragraph at lines 185--194\", \"Underfull \\\\hbox (badness 6445) in paragraph at lines 204--205\", \"Overfull \\\\hbox (18.84132pt too wide) in paragraph at lines 209--218\", \"Underfull \\\\hbox (badness 1231) in paragraph at lines 218--218\"], \"issues\": [\"pages 12 > limit 8\"], \"summary\": \"FAIL: pages 12 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f63035df-f472-412b-a519-72eaf02c45fb",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "557500f7-69ec-4358-864b-4eab992504ad",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 134--135\\\\n\\\\\\\\T1/pcr/m/n/10.95 answer_assertion \\\\\\\\T1/ptm/m/n/10.95 (+20) con-straint per trac\\\\ne\\\\n []\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (81.88095pt too wide) in paragraph at lines 156--172\\\\n [][] \\\\n []\\\\n\\\\n\\\\nLaTeX Warning: `h' float specifier changed to `ht'.\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (37.0624pt too wide) in paragraph at lines 185--194\\\\n [][] \\\\n []\\\\n\\\\n\\\\nLaTeX Warning: `h' float specifier changed to `ht'.\\\\n\\\\n[11]\\\\nUnderfull \\\\\\\\hbox (badness 6445) in paragraph at lines 204--205\\\\n\\\\\\\\T1/ptm/m/n/10.95 (+20) We com-pute 95% con-fi-dence in-ter-vals for\\\\n []\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (18.84132pt too wide) in paragraph at lines 209--218\\\\n [][] \\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1231) in paragraph at lines 218--218\\\\n[]\\\\\\\\T1/ptm/m/n/10 (+20) Table 5: |Boot-strap 95% con-fi-dence in-ter-vals for\\\\n []\\\\n\\\\n) [12] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 43A4ADD1E45E7DCB23598040EFB8E1C6;3532.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 29934 strings out of 469438\\\\n 545606 string characters out of 5468411\\\\n 1401926 words of memory out of 5000000\\\\n 57520 multiletter control sequences out of 15000+600000\\\\n 707030 words of font info for 370 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,10n,94p,1757b,1661s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/shar\\\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texl\\\\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/tex\\\\nmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist\\\\n/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\\\ntype1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\\\\nublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\\\\nmsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\\\\ncm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.\\\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/shar\\\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/share/texli\\\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texm\\\\nf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/\\\\nfonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\\\nype1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/cour\\\\nier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.p\\\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\\\\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\\\\nist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (12 pages, 360520 bytes).\\\\nPDF statistics:\\\\n 756 PDF objects out of 1000 (max. 8388607)\\\\n 605 compressed objects within 7 object streams\\\\n 213 named destinations out of 1000 (max. 500000)\\\\n 75447 words of extra memory for PDF output out of 89155 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 12, \\\"warnings\\\": [\\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\"]}, \\\"pages\\\": 12, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Underfull \\\\\\\\hbox (badness 3792) in paragraph at lines 16--17\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 3746) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 1127) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 3068) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 1077) in paragraph at lines 17--18\\\", \\\"Overfull \\\\\\\\hbox (80.368pt too wide) in paragraph at lines 44--45\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1377) in paragraph at lines 9--10\\\", \\\"Underfull \\\\\\\\vbox (badness 2189) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1092) in paragraph at lines 79--79\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 86--90\\\", \\\"Underfull \\\\\\\\hbox (badness 1365) in paragraph at lines 86--90\\\", \\\"Underfull \\\\\\\\hbox (badness 1377) in paragraph at lines 142--146\\\", \\\"Underfull \\\\\\\\hbox (badness 3281) in paragraph at lines 177--181\\\", \\\"Underfull \\\\\\\\hbox (badness 1424) in paragraph at lines 177--181\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 177--181\\\", \\\"Underfull \\\\\\\\hbox (badness 1270) in paragraph at lines 209--214\\\", \\\"Underfull \\\\\\\\hbox (badness 7722) in paragraph at lines 18--19\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 61--62\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 61--62\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 134--135\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 134--135\\\", \\\"Overfull \\\\\\\\hbox (81.88095pt too wide) in paragraph at lines 156--172\\\", \\\"Overfull \\\\\\\\hbox (37.0624pt too wide) in paragraph at lines 185--194\\\", \\\"Underfull \\\\\\\\hbox (badness 6445) in paragraph at lines 204--205\\\", \\\"Overfull \\\\\\\\hbox (18.84132pt too wide) in paragraph at lines 209--218\\\", \\\"Underfull \\\\\\\\hbox (badness 1231) in paragraph at lines 218--218\\\"], \\\"issues\\\": [\\\"pages 12 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 12 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--135\\n\\\\T1/pcr/m/n/10.95 answer_assertion \\\\T1/ptm/m/n/10.95 (+20) con-straint per trac\\ne\\n []\\n\\n\\nOverfull \\\\hbox (81.88095pt too wide) in paragraph at lines 156--172\\n [][] \\n []\\n\\n\\nLaTeX Warning: `h' float specifier changed to `ht'.\\n\\n\\nOverfull \\\\hbox (37.0624pt too wide) in paragraph at lines 185--194\\n [][] \\n []\\n\\n\\nLaTeX Warning: `h' float specifier changed to `ht'.\\n\\n[11]\\nUnderfull \\\\hbox (badness 6445) in paragraph at lines 204--205\\n\\\\T1/ptm/m/n/10.95 (+20) We com-pute 95% con-fi-dence in-ter-vals for\\n []\\n\\n\\nOverfull \\\\hbox (18.84132pt too wide) in paragraph at lines 209--218\\n [][] \\n []\\n\\n\\nUnderfull \\\\hbox (badness 1231) in paragraph at lines 218--218\\n[]\\\\T1/ptm/m/n/10 (+20) Table 5: |Boot-strap 95% con-fi-dence in-ter-vals for\\n []\\n\\n) [12] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 43A4ADD1E45E7DCB23598040EFB8E1C6;3532.\\n ) \\nHere is how much of TeX's memory you used:\\n 29934 strings out of 469438\\n 545606 string characters out of 5468411\\n 1401926 words of memory out of 5000000\\n 57520 multiletter control sequences out of 15000+600000\\n 707030 words of font info for 370 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,10n,94p,1757b,1661s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texl\\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/tex\\nmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist\\n/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\ntype1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\\nublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\\nmsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\\ncm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/share/texli\\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texm\\nf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/\\nfonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/cour\\nier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/\\ntexlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-d\\nist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (12 pages, 360520 bytes).\\nPDF statistics:\\n 756 PDF objects out of 1000 (max. 8388607)\\n 605 compressed objects within 7 object streams\\n 213 named destinations out of 1000 (max. 500000)\\n 75447 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 12, \"warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\"]}, \"pages\": 12, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Underfull \\\\hbox (badness 3792) in paragraph at lines 16--17\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 3746) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1127) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 3068) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1077) in paragraph at lines 17--18\", \"Overfull \\\\hbox (80.368pt too wide) in paragraph at lines 44--45\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1377) in paragraph at lines 9--10\", \"Underfull \\\\vbox (badness 2189) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 79--79\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 86--90\", \"Underfull \\\\hbox (badness 1365) in paragraph at lines 86--90\", \"Underfull \\\\hbox (badness 1377) in paragraph at lines 142--146\", \"Underfull \\\\hbox (badness 3281) in paragraph at lines 177--181\", \"Underfull \\\\hbox (badness 1424) in paragraph at lines 177--181\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 177--181\", \"Underfull \\\\hbox (badness 1270) in paragraph at lines 209--214\", \"Underfull \\\\hbox (badness 7722) in paragraph at lines 18--19\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 61--62\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 61--62\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--135\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 134--135\", \"Overfull \\\\hbox (81.88095pt too wide) in paragraph at lines 156--172\", \"Overfull \\\\hbox (37.0624pt too wide) in paragraph at lines 185--194\", \"Underfull \\\\hbox (badness 6445) in paragraph at lines 204--205\", \"Overfull \\\\hbox (18.84132pt too wide) in paragraph at lines 209--218\", \"Underfull \\\\hbox (badness 1231) in paragraph at lines 218--218\"], \"issues\": [\"pages 12 > limit 8\"], \"summary\": \"FAIL: pages 12 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "f63035df-f472-412b-a519-72eaf02c45fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1200 · 2026-05-17T19:49:48.332Z_

```json
{
  "parentUuid": "557500f7-69ec-4358-864b-4eab992504ad",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0ef7a659-b03b-407c-8f51-09a4df8f1602",
  "timestamp": "2026-05-17T19:49:48.332Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 1201_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：  worker_id: worker_paper_figure_fig1_pipeline_20260517T172247 project: symb_invariant_consensus 日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status…",
  "leafUuid": "0ef7a659-b03b-407c-8f51-09a4df8f1602",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1202_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 1203 · 2026-05-17T19:50:15.593Z_

<details><summary>Logged reasoning block</summary>

```text
The paper compiles successfully but is 12 pages, exceeding the 8-page EMNLP limit. No critical LaTeX warnings (undefined refs etc.), just minor overfull/underfull hboxes.

The 12-page paper includes:
- Abstract, Introduction, Related Work, Method, Experiments, Discussion, Conclusion, Limitations
- Plus references and appendix

The EMNLP 8-page limit applies to the main matter only (excluding references and appendix). Let me check what the actual content breakdown is.

Actually, EMNLP 2026 main paper limit is 8 pages for main content, with references not counting. 

I need to verify the page structure—the appendix should come after references and not count toward the limit, and I'm checking whether limitations falls within the 8-page main content or if it's positioned differently in the current document.

Looking at the word counts across sections, the main content is running around 7,000+ words, which translates to roughly 12 pages in ACL format—well over the 8-page limit for main content through limitations.

I need to decide whether to move some discussion or experimental details to the appendix, compress existing sections, or verify the actual page limit rules for this venue. Let me check where the bibliography and appendix actually start in the PDF to see how many pages are currently allocated to main content versus supplementary material.

For ACL/EMNLP submissions, the main content is capped at 8 pages while references and appendices don't count toward that limit. Since my paper is 12 pages total with references taking about a page, I'm looking at roughly 10-11 pages of main content—that's 2-3 pages over the limit. I need to aggressively compress the Introduction, which is currently the longest section, trim down the Method section by moving some technical details to the appendix, tighten the Related Work, and relocate the overhead analysis and some tables to supplementary material.

Before diving into the compression work, I should check the PDF layout to see exactly what's on each page and prioritize where to cut.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ef7a659-b03b-407c-8f51-09a4df8f1602",
  "isSidechain": false,
  "requestId": "req_011Cb8io2Y6RU7tfMMUnkLEL",
  "type": "assistant",
  "uuid": "7d277bf5-ac17-47c8-a8a7-f6f365f76205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwMuXrV12KRXuQkS7coMU2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 128905,
      "output_tokens": 1102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1102,
          "cache_read_input_tokens": 128905,
          "cache_creation_input_tokens": 3023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3023
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


### Assistant

_source line 1204 · 2026-05-17T19:50:15.660Z_

Paper compiles (12 pages) but exceeds the 8-page EMNLP limit. 0 critical LaTeX warnings. Let me check page breakdown to understand what needs compression.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d277bf5-ac17-47c8-a8a7-f6f365f76205",
  "isSidechain": false,
  "requestId": "req_011Cb8io2Y6RU7tfMMUnkLEL",
  "type": "assistant",
  "uuid": "14b8d686-548f-49e6-9a9e-0fc5710227b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwMuXrV12KRXuQkS7coMU2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 128905,
      "output_tokens": 1102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1102,
          "cache_read_input_tokens": 128905,
          "cache_creation_input_tokens": 3023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3023
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

_source line 1205 · 2026-05-17T19:50:15.982Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RX73wM2NvMY2y9uzKFNtt2`</summary>

```json
{
  "query": "select:pdf_to_images",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14b8d686-548f-49e6-9a9e-0fc5710227b0",
  "isSidechain": false,
  "requestId": "req_011Cb8io2Y6RU7tfMMUnkLEL",
  "type": "assistant",
  "uuid": "69712d58-0c08-4d29-bbd3-5e44d85156d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwMuXrV12KRXuQkS7coMU2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3023,
      "cache_read_input_tokens": 128905,
      "output_tokens": 1102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1102,
          "cache_read_input_tokens": 128905,
          "cache_creation_input_tokens": 3023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3023
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

_source line 1206 · 2026-05-17T19:50:15.989Z_

<details><summary>↩ Tool result · `toolu_01RX73wM2NvMY2y9uzKFNtt2`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69712d58-0c08-4d29-bbd3-5e44d85156d2",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "02e92d36-5fd9-45a3-8bff-dc2a922a9770",
  "toolUseResult": {
    "matches": [],
    "query": "select:pdf_to_images",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "69712d58-0c08-4d29-bbd3-5e44d85156d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1207 · 2026-05-17T19:50:18.541Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EMjsvzs7RD6vYD7p9vc2Ap`</summary>

```json
{
  "query": "pdf_to_images",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02e92d36-5fd9-45a3-8bff-dc2a922a9770",
  "isSidechain": false,
  "requestId": "req_011Cb8iq5BQBEeYxw6iDL8Gp",
  "type": "assistant",
  "uuid": "e5ed80a2-bf84-4ef9-8293-ec856c1c898f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjworBgQRAiA92eFzoNGmh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 131928,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1118,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 131928,
          "cache_creation_input_tokens": 1118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1118
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

_source line 1208 · 2026-05-17T19:50:18.546Z_

<details><summary>↩ Tool result · `toolu_01EMjsvzs7RD6vYD7p9vc2Ap`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5ed80a2-bf84-4ef9-8293-ec856c1c898f",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "7f54ab6a-7092-4992-9495-6f128595499f",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images"
    ],
    "query": "pdf_to_images",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "e5ed80a2-bf84-4ef9-8293-ec856c1c898f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1209 · 2026-05-17T19:50:22.759Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01HufH4bMSA7owBzwkbLVvex`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf",
  "pages": "1,8,9,10,11,12",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f54ab6a-7092-4992-9495-6f128595499f",
  "isSidechain": false,
  "requestId": "req_011Cb8iqFxJFKnBHRANdvuEP",
  "type": "assistant",
  "uuid": "ca5f8f4a-9a40-4310-9651-d4b30033fc61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RYwTssRGx5FV7FZv79Cg8W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 451,
      "cache_read_input_tokens": 133046,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 148,
          "cache_read_input_tokens": 133046,
          "cache_creation_input_tokens": 451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 451
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

_source line 1210 · 2026-05-17T19:50:24.499Z_

<details><summary>↩ Tool result · `toolu_01HufH4bMSA7owBzwkbLVvex`</summary>

```text
Error: result (3,526,915 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-pdf_to_images-1779047424490.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-pdf_to_images-1779047424490.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca5f8f4a-9a40-4310-9651-d4b30033fc61",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "7bf68e8e-2e74-4a14-9ba7-d05766bd1f2a",
  "toolUseResult": "Error: result (3,526,915 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-pdf_to_images-1779047424490.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-pdf_to_images-1779047424490.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 1210,
    "serialized_bytes": 3526952,
    "serialized_sha256": "d633a9b335cec2c9c0832bb3323b01ba7fcb4ff4dedd900d9da7dfd8d52397d8",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "ca5f8f4a-9a40-4310-9651-d4b30033fc61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1211_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：  worker_id: worker_paper_figure_fig1_pipeline_20260517T172247 project: symb_invariant_consensus 日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status…",
  "leafUuid": "7bf68e8e-2e74-4a14-9ba7-d05766bd1f2a",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1212_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 1213 · 2026-05-17T19:50:29.793Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF images are too large. Let me try with lower DPI or just check specific pages. Actually, let me use the output directory to check the images. Let me try reading them individually.

Actually, let me take a different approach. Let me just check the page breakdown by looking at the aux/log files for page references, or just view individual pages at lower DPI.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bf68e8e-2e74-4a14-9ba7-d05766bd1f2a",
  "isSidechain": false,
  "requestId": "req_011Cb8iqhJYCDZAMXAXkh7FU",
  "type": "assistant",
  "uuid": "02555673-b7a1-4c68-978b-1a35c83a7711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FDEGwG8XnqegNtup22fQG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 133497,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 133497,
          "cache_creation_input_tokens": 556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 556
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


### Assistant

_source line 1214 · 2026-05-17T19:50:30.332Z_

Images too large. Let me check individual boundary pages at lower DPI.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02555673-b7a1-4c68-978b-1a35c83a7711",
  "isSidechain": false,
  "requestId": "req_011Cb8iqhJYCDZAMXAXkh7FU",
  "type": "assistant",
  "uuid": "36fd0c1a-19fb-47dc-933c-f504cb30b8bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FDEGwG8XnqegNtup22fQG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 133497,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 133497,
          "cache_creation_input_tokens": 556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 556
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

_source line 1215 · 2026-05-17T19:50:31.037Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01FHGihP1r4o3HRXwTs97Vdv`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf",
  "pages": "8",
  "dpi": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36fd0c1a-19fb-47dc-933c-f504cb30b8bd",
  "isSidechain": false,
  "requestId": "req_011Cb8iqhJYCDZAMXAXkh7FU",
  "type": "assistant",
  "uuid": "991e2cd7-3dac-43d3-9d37-18ef60453f44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FDEGwG8XnqegNtup22fQG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 133497,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 133497,
          "cache_creation_input_tokens": 556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 556
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

_source line 1216 · 2026-05-17T19:50:31.426Z_

<details><summary>↩ Tool result · `toolu_01FHGihP1r4o3HRXwTs97Vdv`</summary>

```text
Error: result (417,504 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-pdf_to_images-1779047431424.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-pdf_to_images-1779047431424.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "991e2cd7-3dac-43d3-9d37-18ef60453f44",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "80dea673-10c6-4d77-9268-5e0b87a92cc7",
  "toolUseResult": "Error: result (417,504 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-pdf_to_images-1779047431424.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-paper-agent-644edc69/6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1/tool-results/mcp-agent-ml-research-pdf_to_images-1779047431424.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/_pdf_images/main_p8.png\", \"base64\": \"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Bach9K5du3bm6kmJlrkPNMMSsPL666+vUKFCoip8/vnnc+XKZW5xTSl9/fXXjRo1MvcmJ5YwF+PGjbPvOyane/fuu3btqlixoq7fTUWdaawhgeQfYDoR6qA7DzLp3VMZnyLElibSpTrxk26/jl1m586d8VwPkArStcfmI+/2x6/Tr9FzRfA5S5YsQmxQvXr14kdszu+ZM3bs2GQR27Fjx/z3ZUE5c+aMH7G1b99+0aJFjuufMkhcnjrCQ9gf6Lf9hK0y8ahDxifdwBiG2Bz3RkuD2JjW5557DlyebLUg2g0bNiSyoymkKVOmJBCxQbVr104pYrOZsGDBgnRCbI4LNWxA89hjj/Xq1ctx1+bjv2rCprTXkFjyDDDhZGr+/PPP40dsP/744wcffJBOXTovKZWIDSMFo7du3bpnzx7Z3K+++updl8y9wphjfNiWLVuIMzyXcJ8f9M4775QuXTqxdX7zzTfFixePZ0cpFfTXv/7VRmxnp9FzSBdccIFBbAToKUJsNj388MOxERtuuEWLFk899ZT/p0svvTR+xFamTJnASjI1TZ48+c4771Q6PVTmnBMKFRux/eUvfzGIDXrrrbf8F8X6acKECbqV/FzRo48+mljEdtNNN6UUsdlMePLJJ9MPsUE2oOnZs2camZ/2GhJO6YfYNm3aVLFiRaV16UU8iA0QefPNN9t30mcuOnjwIIAHXZbr/OWXX9636Oeffybe2LdvH24XpPTFF18E3kaYUkoNYsP0YHk/++wzMBndPXz48PHjx7FK+/fvZwwkAM70njJ79+797rvvwG0k0t7Xc0vMyr333ovV6Nu37+bNm8GshIx58uTBncMEHG3Dhg1fffVVrNItt9ziuPeRz3Hp9ttv10kmQu1u3bpNnTrVca32bbfdNm3atPHjx1999dU8q41/3St83333rVmzxtOB77//ng4Qug0bNmzQoEE4wq+//rp79+5NmzZ13JM0ffr0qVOnjgp/8skndIxetWnTholQpkFsAOjly5fzoH6yG125cmXVqlX79eunRSYAd7Nmzfw38S1ZsoSBTJo0qXXr1kin4950CWc6d+783HPPVatW7ZprrgnccvWzJQaTkSuawBYkJSX17t0bWIkFp2N0j3THjh2lA0ePHn3wwQdpl6B29uzZprbYiA17QdRet25dugTeuvzyy7t06XLixAkPc5zf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Tyv3Cxcu1K5de9myZTNnzixTpowK6itWrKhfv/7OnTtbtmy5Zs0auQm1aty4cUhISHBwcN68edVBCL5g/vz5s2bNmjBhQsaMGa0bNW/ZsqVJkyYbN24cPHhwnTp1FBF0FUBh1apVuXPn9r/YXrF06dL48ePLQZwwsDhx4ly6dMmXF+G+SZIkeYrHMX3zzTeZM2d+6623nD9Vq1atTZs2rm89evSoW7duFNNJmjU0NDQ0AgLN2GIrfvvtN3U0OBzl+vXrT0sSGNiUKVPkul+/fnIo58WLF59//nk5nOD27dvJkiWT02anT58up4XeunUL0iYHFvmChw8fpkyZUoppYz/p0qWT47lAyZIl5VBzTwIIrly5Urp06ZdffjlKJfeKrFmzqkPZXQ9mteLzzz9X17/88svTPTiECnVlbL///ruXIbTTp09rxqahoaERffCTsUEXDhw4sHv37pMnT/79998yKfbVV19xJzw8XOINgefrr7/etWvXkSNHHjx4EFCx/+149OhR5cqVvZ+F9cRQrVq1sLAwue7Tp8+7777LxbBhw4oXL66eqVixYq9evQzTctTNChUqOIe+POHs2bMQAudxTJhfkiRJFi9eLP+S6aZNm7wIYJj7snK9ZMmSaGVsOXLkUIzNO7Zu3VqoUKHokySyaNasmStj844ffvghdjG2GzdufP8YMjB88+ZN+Vc6FSdOnHiSiw3oh2C6+EyYMf0N/tIT27lzZ2SPIPMCVV7oteuhutEE0acVRIcIdxqnna5cudKPtROegHEqDcj6DdyR1QCswDys/SgnnIVC1D179gTkNJSff/5ZiXrnzp0IhRFgNuot59IRv3H37l2VLJ1Pwr3618tIAT8tW7Zsy5YtgRJDw/CPsf3555/4EbEJDPTKlSu//vrrl19++dNPP+G1ueDfhw8f8sypU6euXbuGD3JdFhO7QKEGDBiwdOnS5s2bE+zlJs3+/fffHz16dKNGjd5++20u8PKGORHWpUuXoUOHVq1adeDAgTNmzIDaduvWrWPHjmPHjs2cObMciMm7HTp0KFmypDJr54vcPHz48MiRI2fPnl27du2jR49yZ968efHjx2/cuPG0adNo2+RbokQJJer06dMnTpxIIvXq1cM1G+a8YY0aNaZMmdK3b19yb9CggbOANEsKCMno3r17+/btCRg+vohO4saNiyQIDzGS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\", \"width\": 827, \"height\": 1170, \"size_kb\": 305.4}], \"total_pages\": 12, \"rendered_pages\": 1, \"dpi\": 100, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "991e2cd7-3dac-43d3-9d37-18ef60453f44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1217_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：  worker_id: worker_paper_figure_fig1_pipeline_20260517T172247 project: symb_invariant_consensus 日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status…",
  "leafUuid": "80dea673-10c6-4d77-9268-5e0b87a92cc7",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1218_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 1219 · 2026-05-17T19:50:36.692Z_

<details><summary>Logged reasoning block</summary>

```text
The images are still too large to load into context. Let me try a different approach - I'll use the LaTeX log or aux file to figure out which sections are on which pages. Or I can look at the output directory for the saved images and use the Read tool to view them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80dea673-10c6-4d77-9268-5e0b87a92cc7",
  "isSidechain": false,
  "requestId": "req_011Cb8irCp4hkpYr5hpcoE7p",
  "type": "assistant",
  "uuid": "797225d0-ba65-4c14-a8ef-e008338b3747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgdayrS1jQRVAzeQvFpA4q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 134053,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 134053,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 651
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


### Assistant

_source line 1220 · 2026-05-17T19:50:37.287Z_

Let me check the output images directory and view individual pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "797225d0-ba65-4c14-a8ef-e008338b3747",
  "isSidechain": false,
  "requestId": "req_011Cb8irCp4hkpYr5hpcoE7p",
  "type": "assistant",
  "uuid": "15501162-9039-4fef-abe0-626c64f1298e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgdayrS1jQRVAzeQvFpA4q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 134053,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 134053,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 651
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

_source line 1221 · 2026-05-17T19:50:38.192Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DZKbX2Jp8uuoXtXJr27E11`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/_pdf_images/",
  "description": "List rendered PDF page images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15501162-9039-4fef-abe0-626c64f1298e",
  "isSidechain": false,
  "requestId": "req_011Cb8irCp4hkpYr5hpcoE7p",
  "type": "assistant",
  "uuid": "0c853f11-8494-4ff7-846a-0568bf908e5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgdayrS1jQRVAzeQvFpA4q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 134053,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 134053,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 651
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

_source line 1222 · 2026-05-17T19:50:38.363Z_

<details><summary>↩ Tool result · `toolu_01DZKbX2Jp8uuoXtXJr27E11`</summary>

```text
main_p1.png
main_p10.png
main_p11.png
main_p12.png
main_p2.png
main_p3.png
main_p4.png
main_p5.png
main_p6.png
main_p7.png
main_p8.png
main_p9.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c853f11-8494-4ff7-846a-0568bf908e5d",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "73644ab1-582b-42da-b765-b57259831a26",
  "toolUseResult": {
    "stdout": "main_p1.png\nmain_p10.png\nmain_p11.png\nmain_p12.png\nmain_p2.png\nmain_p3.png\nmain_p4.png\nmain_p5.png\nmain_p6.png\nmain_p7.png\nmain_p8.png\nmain_p9.png",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0c853f11-8494-4ff7-846a-0568bf908e5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1223 · 2026-05-17T19:50:43.602Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YGCKozeYjRxrt2ig3VhjPg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73644ab1-582b-42da-b765-b57259831a26",
  "isSidechain": false,
  "requestId": "req_011Cb8iriT2SmZWthN4DKNbK",
  "type": "assistant",
  "uuid": "9305aeac-4809-42b0-b3c9-f01e8ec94de0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kXycbeyutmTjDJb3pqDY1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 134704,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 134704,
          "cache_creation_input_tokens": 293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 293
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

_source line 1224 · 2026-05-17T19:50:43.798Z_

<details><summary>↩ Tool result · `toolu_01YGCKozeYjRxrt2ig3VhjPg`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9305aeac-4809-42b0-b3c9-f01e8ec94de0",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "1156d0bc-ee27-4021-9f6e-9508a8fed967",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 312754
    }
  },
  "sourceToolAssistantUUID": "9305aeac-4809-42b0-b3c9-f01e8ec94de0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1225 · 2026-05-17T19:50:43.904Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VkSegrM6ADapFXNskr8TAh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1156d0bc-ee27-4021-9f6e-9508a8fed967",
  "isSidechain": false,
  "requestId": "req_011Cb8iriT2SmZWthN4DKNbK",
  "type": "assistant",
  "uuid": "8a314e1c-bf71-452a-ad1a-0fdaaa25bb4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kXycbeyutmTjDJb3pqDY1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 134704,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 134704,
          "cache_creation_input_tokens": 293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 293
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


### Runtime record

_source line 1226_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：  worker_id: worker_paper_figure_fig1_pipeline_20260517T172247 project: symb_invariant_consensus 日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status…",
  "leafUuid": "8a314e1c-bf71-452a-ad1a-0fdaaa25bb4c",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1227_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Tool result

_source line 1228 · 2026-05-17T19:50:44.493Z_

<details><summary>↩ Tool result · `toolu_01VkSegrM6ADapFXNskr8TAh`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a314e1c-bf71-452a-ad1a-0fdaaa25bb4c",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "4d451f61-0104-4957-8f0d-ac42beb78c49",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 533484
    }
  },
  "sourceToolAssistantUUID": "8a314e1c-bf71-452a-ad1a-0fdaaa25bb4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1229 · 2026-05-17T19:50:44.497Z_

```json
{
  "parentUuid": "4d451f61-0104-4957-8f0d-ac42beb78c49",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "05990bd7-2206-4e50-b05e-51afd98a98d3",
  "timestamp": "2026-05-17T19:50:44.497Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Runtime record

_source line 1230_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：  worker_id: worker_paper_figure_fig1_pipeline_20260517T172247 project: symb_invariant_consensus 日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status…",
  "leafUuid": "05990bd7-2206-4e50-b05e-51afd98a98d3",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1231_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 1232 · 2026-05-17T19:50:57.844Z_

<details><summary>Logged reasoning block</summary>

```text
Looking at the pages:

Page 8: Contains the end of Discussion, the full Conclusion section, and the Limitations section. This is the last page of main content.

Page 9: This is the References page (bibliography).

So main content (Abstract through Limitations) = 8 pages, which exactly meets the EMNLP limit. References start on page 9. Let me check pages 10-12 to confirm they're just references and appendix.

Wait, looking more carefully at page 8, I can see the Conclusion and Limitations sections. The page number shows "8" at the bottom. So the main content fits exactly in 8 pages!


The compile check flagged the total page count as exceeding the limit, but that's because it's counting references and appendix pages too. Since EMNLP allows unlimited reference and appendix pages, the paper actually complies with the requirements. Let me verify what's on pages 10-12 to confirm they're just references and appendix material.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05990bd7-2206-4e50-b05e-51afd98a98d3",
  "isSidechain": false,
  "requestId": "req_011Cb8isAf7JAGHFjdjXw4DW",
  "type": "assistant",
  "uuid": "7ae88c02-aeee-4223-863d-05077e285071",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpevzqCmkS1th4edbUmeC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 134997,
      "output_tokens": 514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 514,
          "cache_read_input_tokens": 134997,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 792
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


### Assistant

_source line 1233 · 2026-05-17T19:50:57.850Z_

Page 8 shows Conclusion + Limitations ending. Page 9 starts References. Main content fits exactly in 8 pages. Let me confirm the remaining pages are references/appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae88c02-aeee-4223-863d-05077e285071",
  "isSidechain": false,
  "requestId": "req_011Cb8isAf7JAGHFjdjXw4DW",
  "type": "assistant",
  "uuid": "933459ed-bb94-4104-b099-579715783d3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpevzqCmkS1th4edbUmeC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 134997,
      "output_tokens": 514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 514,
          "cache_read_input_tokens": 134997,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 792
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

_source line 1234 · 2026-05-17T19:50:57.864Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qvak3UUgRMRePXjdUUthXj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "933459ed-bb94-4104-b099-579715783d3d",
  "isSidechain": false,
  "requestId": "req_011Cb8isAf7JAGHFjdjXw4DW",
  "type": "assistant",
  "uuid": "86d8637a-7f28-441d-8eb4-3622cd50bbba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpevzqCmkS1th4edbUmeC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 134997,
      "output_tokens": 514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 514,
          "cache_read_input_tokens": 134997,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 792
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

_source line 1235 · 2026-05-17T19:50:57.882Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GP6ALJbXVfqUMQynuN8opn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86d8637a-7f28-441d-8eb4-3622cd50bbba",
  "isSidechain": false,
  "requestId": "req_011Cb8isAf7JAGHFjdjXw4DW",
  "type": "assistant",
  "uuid": "5b624eb0-978a-48e4-8905-05d2cf954034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpevzqCmkS1th4edbUmeC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 134997,
      "output_tokens": 514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 514,
          "cache_read_input_tokens": 134997,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 792
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

_source line 1236 · 2026-05-17T19:50:58.670Z_

<details><summary>↩ Tool result · `toolu_01GP6ALJbXVfqUMQynuN8opn`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b624eb0-978a-48e4-8905-05d2cf954034",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "5c89baed-c9ee-4aad-9a0d-85e0043a9a0e",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 387108
    }
  },
  "sourceToolAssistantUUID": "5b624eb0-978a-48e4-8905-05d2cf954034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-17T19:50:58.768Z_

<details><summary>↩ Tool result · `toolu_01Qvak3UUgRMRePXjdUUthXj`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86d8637a-7f28-441d-8eb4-3622cd50bbba",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "2e15f744-5780-482f-a99e-16ea0673b8bf",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 436788
    }
  },
  "sourceToolAssistantUUID": "86d8637a-7f28-441d-8eb4-3622cd50bbba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1238_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：  worker_id: worker_paper_figure_fig1_pipeline_20260517T172247 project: symb_invariant_consensus 日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status…",
  "leafUuid": "2e15f744-5780-482f-a99e-16ea0673b8bf",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1239_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 1240 · 2026-05-17T19:51:07.699Z_

<details><summary>Logged reasoning block</summary>

```text
Page 10 shows the end of references and the start of the Appendix (Appendix A: Prompt Templates). Page 11 shows more appendix content (prompt details + appendix B: Capability Trap Diagnostics, C: Statistical Power Analysis).

Let me check page 12 to see what's there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e15f744-5780-482f-a99e-16ea0673b8bf",
  "isSidechain": false,
  "requestId": "req_011Cb8itDkBBFNhbCVzTfDZB",
  "type": "assistant",
  "uuid": "88291eaa-7636-41cf-b0e7-ec48f568a162",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGsGwTUKTUffMtZbREpkuR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 228,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 135789,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 228,
          "output_tokens": 183,
          "cache_read_input_tokens": 135789,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 903
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

_source line 1241 · 2026-05-17T19:51:07.856Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XNfW71EwhwMbRQb8MLPhcx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/_pdf_images/main_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88291eaa-7636-41cf-b0e7-ec48f568a162",
  "isSidechain": false,
  "requestId": "req_011Cb8itDkBBFNhbCVzTfDZB",
  "type": "assistant",
  "uuid": "229c58b4-b622-4ec2-af81-2528a3406603",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGsGwTUKTUffMtZbREpkuR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 228,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 135789,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 228,
          "output_tokens": 183,
          "cache_read_input_tokens": 135789,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 903
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

_source line 1242 · 2026-05-17T19:51:08.241Z_

<details><summary>↩ Tool result · `toolu_01XNfW71EwhwMbRQb8MLPhcx`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "229c58b4-b622-4ec2-af81-2528a3406603",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "62715cc5-57ce-422a-9887-bbd27ebdd02b",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 279939
    }
  },
  "sourceToolAssistantUUID": "229c58b4-b622-4ec2-af81-2528a3406603",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1243_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：  worker_id: worker_paper_figure_fig1_pipeline_20260517T172247 project: symb_invariant_consensus 日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status…",
  "leafUuid": "62715cc5-57ce-422a-9887-bbd27ebdd02b",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1244_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 1245 · 2026-05-17T19:51:30.186Z_

<details><summary>Logged reasoning block</summary>

```text
Page 12 shows the appendix content: Table 4 (capability trap diagnostics), Table 4 power analysis, Appendix D (Bootstrap Confidence Intervals) with Table 5.

So the page breakdown is:
- Pages 1-8: Main content (Abstract through Limitations) = exactly 8 pages ✅
- Pages 9-10: References (about 1.5 pages)
- Pages 10-12: Appendix (A: Prompt Templates, B: Capability Trap Diagnostics, C: Statistical Power Analysis, D: Bootstrap Confidence Intervals)


The paper meets EMNLP's 8-page main content requirement—the compile check flagged it as failing because it counts total pages, but references and appendices don't count toward the limit. Now I can move forward with Step 5 refinement, though I should first check the paper-refinement skill to make sure I'm following the protocol correctly. Looking back at page 8, the Conclusion and Limitations sections fit properly, so the layout is solid. some issues I see from the visual review:
- Page 8: Main content ends properly
- The appendix has real content (prompt templates, diagnostic tables, power analysis, bootstrap CIs) - this is good

Now I need to follow the protocol for Step 4 completion, which means checking paper consistency first, then moving into Step 5. I've already verified there are no critical issues or warnings. For Step 5, I'll need to read the paper-refinement and paper-quality-lessons skills, then submit the paper for review and iterate based on feedback. Let me report Step 4 completion to the Director first before starting the refinement phase.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62715cc5-57ce-422a-9887-bbd27ebdd02b",
  "isSidechain": false,
  "requestId": "req_011Cb8itvCm5ieZiCw94y7MN",
  "type": "assistant",
  "uuid": "14b4e85c-f060-44ed-8d1b-9f4a35a37e49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pRmMWzKWoq7wqi7nRQLTK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 136692,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1140,
          "cache_read_input_tokens": 136692,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 628
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


### Assistant

_source line 1246 · 2026-05-17T19:51:30.188Z_

Main content fits exactly in 8 pages (EMNLP limit). Pages 9-12 are references + appendix (unlimited). The compile check's "FAIL" was based on total page count, but for EMNLP only main content counts.

Step 4 complete. Reporting to Director and preparing Step 5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14b4e85c-f060-44ed-8d1b-9f4a35a37e49",
  "isSidechain": false,
  "requestId": "req_011Cb8itvCm5ieZiCw94y7MN",
  "type": "assistant",
  "uuid": "70b2fe9e-0d58-44a8-87e0-d76e5fbac11e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pRmMWzKWoq7wqi7nRQLTK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 136692,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1140,
          "cache_read_input_tokens": 136692,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 628
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

_source line 1247 · 2026-05-17T19:51:41.787Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_agent_post_to_director · `toolu_01QcFWpt5Yrf8c4P6xZQkpVe`</summary>

```json
{
  "text": "[写作进展] Step 4 完成，准备进入 Step 5\n\n**Phase 2 全部章节完成：**\n- Abstract (v24, ~216 words, oracle-positive framing)\n- Introduction (v23, ~1164 words, oracle-led narrative, capability trap 低调引入)\n- Discussion (v21, +约束失败模式分析 + 成本分析前置)\n- Conclusion (v25, ~346 words, 数字与 Abstract/Intro 完全一致)\n- Related Work (v27, +V-STaR/RASC/ReASC/GSM-Symbolic 引用)\n\n**一致性检查：** 0 critical, 0 warning, 0 orphan bib entries\n\n**编译状态：** ✅ 编译成功，主要内容恰好 8 页（EMNLP 限制），总 12 页（含 references 1.5p + appendix 2.5p）。无 undefined refs/cites。\n\n**Provenance：** 27/27 claims tracked, 全部有 registry evidence\n\n**即将进入 Step 5 Iterative Refinement：** 提交 Reviewer 审查 → 迭代修改（max 5 轮）→ 收敛后三件套（visual review + verify_references + provenance check）\n\n需要决策：是否直接进入 Step 5？还是有其他优先调整？",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70b2fe9e-0d58-44a8-87e0-d76e5fbac11e",
  "isSidechain": false,
  "requestId": "req_011Cb8itvCm5ieZiCw94y7MN",
  "type": "assistant",
  "uuid": "605fa3bf-9718-4ab6-97f2-e852b48396fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pRmMWzKWoq7wqi7nRQLTK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 136692,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1140,
          "cache_read_input_tokens": 136692,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 628
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

_source line 1248 · 2026-05-17T19:51:45.285Z_

<details><summary>↩ Tool result · `toolu_01QcFWpt5Yrf8c4P6xZQkpVe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "605fa3bf-9718-4ab6-97f2-e852b48396fe",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "1a996697-d66b-4121-8efe-fce6078bc3cb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "605fa3bf-9718-4ab6-97f2-e852b48396fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1249 · 2026-05-17T19:51:49.290Z_

Director 已收到汇报。现在读取 Step 5 所需的 skill 文件，准备进入 Iterative Refinement。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a996697-d66b-4121-8efe-fce6078bc3cb",
  "isSidechain": false,
  "requestId": "req_011Cb8iwet7BEug9M9Loz1xX",
  "type": "assistant",
  "uuid": "c90f3bd0-5d3e-40c1-9a81-757224742316",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjdaVUL9s6hDMHPgHczBAf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 137320,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 137320,
          "cache_creation_input_tokens": 1207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1207
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

_source line 1250 · 2026-05-17T19:51:50.682Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FuBkcctAZxYe9jfKAEqfQb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/skills/paper-refinement.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c90f3bd0-5d3e-40c1-9a81-757224742316",
  "isSidechain": false,
  "requestId": "req_011Cb8iwet7BEug9M9Loz1xX",
  "type": "assistant",
  "uuid": "992749e3-7e35-4fdd-bf62-aaccd29d91c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjdaVUL9s6hDMHPgHczBAf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 137320,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 137320,
          "cache_creation_input_tokens": 1207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1207
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

_source line 1251 · 2026-05-17T19:51:50.697Z_

<details><summary>↩ Tool result · reported error · `toolu_01FuBkcctAZxYe9jfKAEqfQb`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "992749e3-7e35-4fdd-bf62-aaccd29d91c3",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "2920369a-4dce-4a34-8084-9d99a6295162",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69.",
  "sourceToolAssistantUUID": "992749e3-7e35-4fdd-bf62-aaccd29d91c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-17T19:52:00.754Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QUgh7KL7iMGNBwcggdEerK`</summary>

```json
{
  "pattern": "**/paper-refinement*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2920369a-4dce-4a34-8084-9d99a6295162",
  "isSidechain": false,
  "requestId": "req_011Cb8ix41edqUpRwG6t3QEH",
  "type": "assistant",
  "uuid": "9036f203-b4d2-4a3f-9cf8-163e2a2e5a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJD5UyCGMC78xbwsRzaTNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 225,
      "cache_read_input_tokens": 138527,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 225,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 138527,
          "cache_creation_input_tokens": 225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 225
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

_source line 1253 · 2026-05-17T19:52:00.801Z_

<details><summary>↩ Tool result · `toolu_01QUgh7KL7iMGNBwcggdEerK`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9036f203-b4d2-4a3f-9cf8-163e2a2e5a50",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "d1a5c513-5d75-4fbd-8595-c383634c3a62",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 40,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "9036f203-b4d2-4a3f-9cf8-163e2a2e5a50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1254 · 2026-05-17T19:52:01.078Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LHQBbfsvj4aECuLc4PA267`</summary>

```json
{
  "pattern": "**/paper-quality-lessons*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1a5c513-5d75-4fbd-8595-c383634c3a62",
  "isSidechain": false,
  "requestId": "req_011Cb8ix41edqUpRwG6t3QEH",
  "type": "assistant",
  "uuid": "c7da4803-38e4-40b7-8bfe-9f0f39c74d34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJD5UyCGMC78xbwsRzaTNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 225,
      "cache_read_input_tokens": 138527,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 225,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 138527,
          "cache_creation_input_tokens": 225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 225
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

_source line 1255 · 2026-05-17T19:52:01.124Z_

<details><summary>↩ Tool result · `toolu_01LHQBbfsvj4aECuLc4PA267`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7da4803-38e4-40b7-8bfe-9f0f39c74d34",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "1fb71973-62f3-4675-9f2d-1b1386d4e6d7",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 43,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "c7da4803-38e4-40b7-8bfe-9f0f39c74d34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1256 · 2026-05-17T19:52:01.127Z_

```json
{
  "parentUuid": "1fb71973-62f3-4675-9f2d-1b1386d4e6d7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "48c8f4e1-f869-4556-89fe-13669db1727c",
  "timestamp": "2026-05-17T19:52:01.127Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Tool call

_source line 1257 · 2026-05-17T19:52:05.099Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CGWKzf4rr3DvsFh9ZEduFL`</summary>

```json
{
  "pattern": "**/skills/**/*refinement*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48c8f4e1-f869-4556-89fe-13669db1727c",
  "isSidechain": false,
  "requestId": "req_011Cb8ixpULcmRTTm4V5FHyT",
  "type": "assistant",
  "uuid": "b1148510-5a8f-4ef5-ba25-a4d7f62d5ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HpPf7jsgSHG6Cf7L618Fno",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 138752,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 138752,
          "cache_creation_input_tokens": 340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 340
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

_source line 1258 · 2026-05-17T19:52:05.371Z_

<details><summary>↩ Tool result · `toolu_01CGWKzf4rr3DvsFh9ZEduFL`</summary>

```text
/home/ubuntu/agent-ml-research/skills/global/paper-refinement.skill.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1148510-5a8f-4ef5-ba25-a4d7f62d5ffb",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "e3065075-b462-4450-acb4-53d660c02090",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/agent-ml-research/skills/global/paper-refinement.skill.md"
    ],
    "durationMs": 269,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "b1148510-5a8f-4ef5-ba25-a4d7f62d5ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1259 · 2026-05-17T19:52:10.075Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tw1mgnHuMhGzvNaRTMZ3tb`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-refinement.skill.md",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3065075-b462-4450-acb4-53d660c02090",
  "isSidechain": false,
  "requestId": "req_011Cb8iy8U4wVXB76BK8Xp1Z",
  "type": "assistant",
  "uuid": "1dd6cd57-7284-459d-9229-f3fa513dd148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Bce87M8vwMmXw4iob7Ytk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 113,
      "cache_read_input_tokens": 139092,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 139092,
          "cache_creation_input_tokens": 113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 113
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

_source line 1260 · 2026-05-17T19:52:10.080Z_

<details><summary>↩ Tool result · `toolu_01Tw1mgnHuMhGzvNaRTMZ3tb`</summary>

````text
1	---
2	name: paper-refinement
3	description: Step 5 论文迭代修改循环——Reviewer 评分循环 + 收敛判断 + paper_checklist 注入，max 5 轮。Paper Agent 进入 Step 5 时 Read 本 skill。
4	scope: global
5	tags:
6	  - workflow
7	  - research
8	  - writing
9	  - academic
10	  - review
11	version: 1
12	roles:
13	  - paper_agent
14	---
15	
16	# Step 5 — Iterative Refinement
17	
18	Step 4 全部章节落盘后，Paper Agent 进入 Step 5：把全文递交 Reviewer 评分，按反馈修改，直到收敛。
19	
20	**核心约束**：
21	- 串行——一轮 Reviewer 返回结果处理完才进下一轮，禁止并发请求
22	- 评分驱动——overall 提升才 accept 本轮，下降则 git revert
23	- 上限 5 轮——硬约束，达到上限即停，不论分数
24	
25	## 状态记录（git 是 truth source）
26	
27	每轮修改前 commit 当前论文目录，作为 revert 锚点。无需额外 state 文件。
28	
29	```
30	git -C projects/{project} add paper/
31	git -C projects/{project} commit -m "[paper] refinement round {N-1}"
32	```
33	
34	Round N 的 commit message 用 `N-1`，即 round 1 修改前 commit `round 0`（Step 4 落盘后的初稿）。
35	
36	## 单轮流程
37	
38	```
39	Round N（N = 1..5）：
40	
41	1. git commit 当前版本（message: "[paper] refinement round N-1"）
42	   └── 落地评分下降时的 revert 锚点
43	
44	2. 组装审查请求：
45	   - read_project_file("paper_checklist.yaml") — 用户自定义必查项
46	   - 拼 LaTeX 全文（或 Patch 模式下的差异）+ writing_plan.yaml 路径
47	   - 末尾追加 "## 用户自定义必查项"（见下方"checklist 注入格式"）
48	
49	3. paper_agent_request_review(text=组装后的请求, project=...)
50	   └── Reviewer 通过 reviewer_post_to_director 回传评分
51	
52	4. 解析 Reviewer 响应：
53	   - 维度分（Originality/Clarity/Soundness/Significance/Presentation，1-4）
54	   - overall（1-10）
55	   - 各条具体问题 severity（critical/warning/info）
56	   - checklist 项 PASS/FAIL
57	   ★ 任一 checklist FAIL → 该条问题 severity 自动按 critical 对待
58	
59	5. 按问题类型分流处理：
60	   - 事实性错误（数字不一致 / 引用错位）→ 自己用 edit_paper_section 改
61	   - 段落级叙事问题（逻辑断裂 / 强度词超限）→ spawn Worker 重写段落，回来再 edit_paper_section
62	   - 结构问题（章节顺序 / 段落归并）→ 自己用 edit_paper_section
63	   - critical 且 claim 本身无支撑 → 汇报 Director（不要自行降 claim）
64	
65	6. 全部问题处理完后判断本轮 overall 走势：
66	   - overall(N) ≥ overall(N-1) → 保留本轮修改，进入收敛判断
67	   - overall(N) <  overall(N-1) → git checkout 上一轮 commit，回退本轮所有修改，标记"本轮无进展"
68	
69	7. 收敛判断（任一满足即停）：
70	   - 全部问题为 info（无 critical / warning）
71	   - N == 5（硬上限）
72	   - 连续两轮 overall 持平（差 ≤0.1）
73	   - 连续两轮无新增 critical（critical 列表内容相同或更短）
74	
75	   未收敛且 N<5 → 进入 Round N+1
76	   已收敛 → 进入收尾（见下文）
77	```
78	
79	## checklist 注入格式
80	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "1dd6cd57-7284-459d-9229-f3fa513dd148",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "07a78c15-144d-4d25-84a4-56d4f7711268",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-refinement.skill.md",
      "content": "---\nname: paper-refinement\ndescription: Step 5 论文迭代修改循环——Reviewer 评分循环 + 收敛判断 + paper_checklist 注入，max 5 轮。Paper Agent 进入 Step 5 时 Read 本 skill。\nscope: global\ntags:\n  - workflow\n  - research\n  - writing\n  - academic\n  - review\nversion: 1\nroles:\n  - paper_agent\n---\n\n# Step 5 — Iterative Refinement\n\nStep 4 全部章节落盘后，Paper Agent 进入 Step 5：把全文递交 Reviewer 评分，按反馈修改，直到收敛。\n\n**核心约束**：\n- 串行——一轮 Reviewer 返回结果处理完才进下一轮，禁止并发请求\n- 评分驱动——overall 提升才 accept 本轮，下降则 git revert\n- 上限 5 轮——硬约束，达到上限即停，不论分数\n\n## 状态记录（git 是 truth source）\n\n每轮修改前 commit 当前论文目录，作为 revert 锚点。无需额外 state 文件。\n\n```\ngit -C projects/{project} add paper/\ngit -C projects/{project} commit -m \"[paper] refinement round {N-1}\"\n```\n\nRound N 的 commit message 用 `N-1`，即 round 1 修改前 commit `round 0`（Step 4 落盘后的初稿）。\n\n## 单轮流程\n\n```\nRound N（N = 1..5）：\n\n1. git commit 当前版本（message: \"[paper] refinement round N-1\"）\n   └── 落地评分下降时的 revert 锚点\n\n2. 组装审查请求：\n   - read_project_file(\"paper_checklist.yaml\") — 用户自定义必查项\n   - 拼 LaTeX 全文（或 Patch 模式下的差异）+ writing_plan.yaml 路径\n   - 末尾追加 \"## 用户自定义必查项\"（见下方\"checklist 注入格式\"）\n\n3. paper_agent_request_review(text=组装后的请求, project=...)\n   └── Reviewer 通过 reviewer_post_to_director 回传评分\n\n4. 解析 Reviewer 响应：\n   - 维度分（Originality/Clarity/Soundness/Significance/Presentation，1-4）\n   - overall（1-10）\n   - 各条具体问题 severity（critical/warning/info）\n   - checklist 项 PASS/FAIL\n   ★ 任一 checklist FAIL → 该条问题 severity 自动按 critical 对待\n\n5. 按问题类型分流处理：\n   - 事实性错误（数字不一致 / 引用错位）→ 自己用 edit_paper_section 改\n   - 段落级叙事问题（逻辑断裂 / 强度词超限）→ spawn Worker 重写段落，回来再 edit_paper_section\n   - 结构问题（章节顺序 / 段落归并）→ 自己用 edit_paper_section\n   - critical 且 claim 本身无支撑 → 汇报 Director（不要自行降 claim）\n\n6. 全部问题处理完后判断本轮 overall 走势：\n   - overall(N) ≥ overall(N-1) → 保留本轮修改，进入收敛判断\n   - overall(N) <  overall(N-1) → git checkout 上一轮 commit，回退本轮所有修改，标记\"本轮无进展\"\n\n7. 收敛判断（任一满足即停）：\n   - 全部问题为 info（无 critical / warning）\n   - N == 5（硬上限）\n   - 连续两轮 overall 持平（差 ≤0.1）\n   - 连续两轮无新增 critical（critical 列表内容相同或更短）\n\n   未收敛且 N<5 → 进入 Round N+1\n   已收敛 → 进入收尾（见下文）\n```\n\n## checklist 注入格式\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 240
    }
  },
  "sourceToolAssistantUUID": "1dd6cd57-7284-459d-9229-f3fa513dd148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
````

</details>

---


### Tool call

_source line 1261 · 2026-05-17T19:52:18.668Z_

<details open><summary>🔧 Tool call — Read · `toolu_013U2kHDjqkwzbWRMbLjDYA5`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-refinement.skill.md",
  "offset": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07a78c15-144d-4d25-84a4-56d4f7711268",
  "isSidechain": false,
  "requestId": "req_011Cb8iyUhjXy3KGkU9bpEbr",
  "type": "assistant",
  "uuid": "1dc2cf2d-46a2-4343-9d98-42ecd264074a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wfWyZUruoZPfWN7MCFhst",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 139205,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 139205,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1447
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

_source line 1262 · 2026-05-17T19:52:18.676Z_

<details><summary>↩ Tool result · `toolu_013U2kHDjqkwzbWRMbLjDYA5`</summary>

````text
80	
81	`read_project_file("paper_checklist.yaml")` 拿到 items 后，在审查请求末尾追加：
82	
83	```
84	## 用户自定义必查项
85	以下是用户指定的必须检查的项，每项必须明确标注 PASS 或 FAIL：
86	- [chk_001] {text}
87	- [chk_002] {text}
88	...
89	
90	如果任何一项标注为 FAIL，整体 severity 自动提升为 critical（必须打回修改）。
91	```
92	
93	- checklist 为空 / 文件不存在 → 不追加该段，正常请求
94	- 不要重写 checklist 文本——保持用户原话，让 Reviewer 自己定位
95	- Dream 模式禁止注入（Dream 论文不投，格式检查无意义）
96	
97	## 修改 Worker 任务模板
98	
99	段落级修改派 Worker（不是整章重写）时：
100	
101	```
102	spawn_worker(
103	  task_type="paper_writing",
104	  project=...,
105	  task_prompt="""
106	Reviewer 在 {section} 章发现以下问题，需要你修改对应段落：
107	
108	【问题位置】{paragraph_id / 行号}
109	【问题描述】{Reviewer 原文}
110	【建议方向】{Reviewer 给的方向}
111	
112	当前段落原文：
113	```latex
114	{原文片段}
115	```
116	
117	参考资料：
118	- 写作规范：Read skills/global/latex-paper.skill.md + red-section.skill.md
119	- registry 切片：{相关 exp_id 列表}
120	- 同章节已有内容：{section}.tex 整章
121	- 引用：references.bib（只用已 verified 条目，未验证标 [UNVERIFIED]）
122	
123	要求：
124	- 只改问题段落，不动其他内容
125	- 输出修改后的段落 latex（标记 old / new）
126	- 不要画图、不要补实验
127	- 改完即返回，不写额外说明
128	"""
129	)
130	```
131	
132	Worker 返回后 Paper Agent 用 `edit_paper_section(project, section, old_text=..., new_text=..., claims=..., table_cells=..., figures=...)` 落盘——`edit_paper_section` 自动同步 provenance，不会 deprecate 未触及的 claim。
133	
134	## 收敛后收尾（Step 5e）
135	
136	Reviewer 评分循环收敛后**必须执行完整三件套**——视觉 + 引用 + 溯源**全部跑完**再汇报 Director；不允许只跑一两项就提交。任一发现 critical/blocker 都要在汇报中显式列出，不得"建议提交审稿"压过失败信号。
137	
138	### 三件套执行顺序
139	
140	按下面顺序串行（每一步完成才进下一步，前一步失败不绕过）：
141	
142	```
143	1. paper-visual-review 排版检查
144	   └── Read skills/global/paper-visual-review.skill.md
145	   └── pdf_to_images(pdf_path=projects/{project}/paper/main.pdf, pages="1-N", dpi=200)
146	       逐页检查图表分辨率 / 字号 / 边距溢出 / 公式 / 引用编号 / 缺失引用占位 [?]
147	   └── cleanup_pdf_images(output_dir=<上一步返回的 output_dir>)  # 不留临时文件
148	   └── 收集 findings：[{page, severity, issue}]
149	   └── 出现 critical（图表溢出 / 缺失编号 / 公式乱码）→ 记入 visual_report，**不**立即返工，
150	       与 verify_references / check_provenance_completeness 的结果**一并汇报 Director**
151	
152	2. verify_references 最终引用验证
153	   └── verify_references(paper_dir="projects/{project}/paper", project=..., skip_online=False)
154	   └── 返回字段：status (ok/orphan_bib/missing_bib/not_found/mismatch) 按条聚合
155	   └── critical 阈值：
156	        - missing_bib（正文 \cite 但 .bib 缺）→ 必须修，否则 LaTeX 编译失败
157	        - not_found（OpenAlex 找不到）→ 疑似幻觉引用，自己 WebSearch 二次验证；仍找不到 → critical
158	        - mismatch（年份/作者偏差）→ warning
159	   └── 自己能改的小问题（missing_bib、年份） → edit_paper_section 修；改完**再调一次 verify_references** 确认通过
160	
161	3. check_provenance_completeness 溯源覆盖
162	   └── check_provenance_completeness(project=...)
163	   └── 返回：tier_distribution / untracked_numbers / invalidated_claims
164	   └── 关键阈值：
165	        - Tier 3 占比 > 30% → 必须汇报 Director（红线，不得静默交付）
166	        - Tier X（invalidated，实验失败/被作废）≥ 1 条 → critical：claim 失去支撑，汇报 Director 决策是否改 claim
167	        - untracked_numbers（正文出现但 provenance 没追踪的数字）≥ 5 → warning：派 Worker 补 provenance
168	```
169	
170	### 汇报 Director 模板
171	
172	三件套全部跑完后**统一**汇报（不要分三次发），把所有 critical/warning 列在一处便于 Director 决策：
173	
174	```
175	paper_agent_post_to_director(
176	  text="[写作进展] Step 5 收尾完成
177	         迭代轮数：{N}/5
178	         最终 overall：{score}
179	         checklist：全部 PASS / 还有 X 条 FAIL（已修复 / 待 Director 决策）
180	
181	         ===== 视觉检查 =====
182	         检查页数：{n}/{total}
183	         结论：PASS / 发现 X 条 critical + Y 条 warning
184	         {若有 critical：逐条列出 page + 描述}
185	
186	         ===== 引用验证 =====
187	         总数 X 条，已验证 Y 条
188	         critical：missing_bib X 条 + 疑似幻觉 Y 条（已尝试 WebSearch 二次验证 → 结果）
189	         warning：mismatch X 条
190	         {若有 critical：列出条目 + 已采取的修复}
191	
192	         ===== Provenance 覆盖 =====
193	         Tier 分布：T1 {a}% / T2 {b}% / T3 {c}% / TX {d}%
194	         {若 T3 > 30% 或 TX ≥ 1：列出受影响的 claim/figure/table}
195	         未追踪数字：X 个（详见 untracked_numbers）
196	
197	         ===== 建议 =====
198	         {以下任选其一}
199	         A. 视觉/引用/provenance 全部 PASS → 建议提交审稿（submit_paper_to_review）
200	         B. 存在 critical → 请 Director 决策：{具体问题列表 + 建议修复方向}
201	         C. provenance 红线触发 → 请 Director 决定：补实验 / 改 claim / 接受现状",
202	  project=...
203	)
204	```
205	
206	Director 决定是否调 `submit_paper_to_review`——Paper Agent **不**主动调，这是 Director 的权限。
207	
208	### 红线（Step 5e 不可绕过）
209	
210	1. **三件套必须全跑**：跳过任一项直接汇报 = 违规，被 Director 打回时不接受"我以为不必要"
211	2. **critical 不静默**：视觉 critical / verify_references critical / Tier X ≥ 1 / Tier 3 > 30% 必须显式写进汇报
212	3. **不主动提交审稿**：哪怕全 PASS 也只能"建议提交"，submit_paper_to_review 是 Director 权限
213	4. **修复后必须复验**：自己修了 missing_bib → 重跑 verify_references；补 provenance → 重跑 check_provenance_completeness
214	5. **Patch 模式走 Phase E**：Patch 的收尾在 Phase E（max 3 轮 Reviewer），不复用 Step 5e 全套；Phase E 自己做 check_provenance_completeness + verify_references，视觉检查可选
215	
216	## 硬约束（与 Paper Agent 红线一致）
217	
218	1. **修改前必 git commit**——没有 commit 不开新一轮，避免 revert 失败
219	2. **未验证引用不进 .bib**——Reviewer 指出新引用需求时，先 verify_references 再写入
220	3. **checklist FAIL 项必须修复**——不参与"连续两轮无新增 critical"的轮数计数，但下一轮必须解决
221	4. **overall 下降必 revert**——不允许"将就一下"
222	5. **不自行降 claim**——claim 无支撑是 Director 决策，Paper Agent 只能改表述强度，不能改 claim 内容
223	6. **Patch / Dream 模式不走本 skill**——Patch 走 Phase E（max 3 轮），Dream 跳过 Reviewer 迭代
224	
225	## 与 Reviewer 评分模板的合约
226	
227	Reviewer 在 `prompts/roles/reviewer.md` §5.3 已规定返回格式：
228	
229	```
230	[写作评审] 轮次 N/5
231	维度评分（1-4）：Originality / Clarity / Soundness / Significance / Presentation
232	Overall（1-10）：
233	## 用户自定义必查项（如审查请求含 paper_checklist）
234	- [chk_id]: PASS / FAIL — 理由
235	## 具体问题
236	- [severity] 位置 + 描述 + 建议
237	```
238	
239	Paper Agent 解析时按位置抓字段——Reviewer 偶尔会漏维度分，**漏了的当作 4（满分）处理**，避免误判 overall 下降。
240	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "1dc2cf2d-46a2-4343-9d98-42ecd264074a",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "7f8c9c01-16c8-4b5f-87fc-f7955a0992b8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-refinement.skill.md",
      "content": "\n`read_project_file(\"paper_checklist.yaml\")` 拿到 items 后，在审查请求末尾追加：\n\n```\n## 用户自定义必查项\n以下是用户指定的必须检查的项，每项必须明确标注 PASS 或 FAIL：\n- [chk_001] {text}\n- [chk_002] {text}\n...\n\n如果任何一项标注为 FAIL，整体 severity 自动提升为 critical（必须打回修改）。\n```\n\n- checklist 为空 / 文件不存在 → 不追加该段，正常请求\n- 不要重写 checklist 文本——保持用户原话，让 Reviewer 自己定位\n- Dream 模式禁止注入（Dream 论文不投，格式检查无意义）\n\n## 修改 Worker 任务模板\n\n段落级修改派 Worker（不是整章重写）时：\n\n```\nspawn_worker(\n  task_type=\"paper_writing\",\n  project=...,\n  task_prompt=\"\"\"\nReviewer 在 {section} 章发现以下问题，需要你修改对应段落：\n\n【问题位置】{paragraph_id / 行号}\n【问题描述】{Reviewer 原文}\n【建议方向】{Reviewer 给的方向}\n\n当前段落原文：\n```latex\n{原文片段}\n```\n\n参考资料：\n- 写作规范：Read skills/global/latex-paper.skill.md + red-section.skill.md\n- registry 切片：{相关 exp_id 列表}\n- 同章节已有内容：{section}.tex 整章\n- 引用：references.bib（只用已 verified 条目，未验证标 [UNVERIFIED]）\n\n要求：\n- 只改问题段落，不动其他内容\n- 输出修改后的段落 latex（标记 old / new）\n- 不要画图、不要补实验\n- 改完即返回，不写额外说明\n\"\"\"\n)\n```\n\nWorker 返回后 Paper Agent 用 `edit_paper_section(project, section, old_text=..., new_text=..., claims=..., table_cells=..., figures=...)` 落盘——`edit_paper_section` 自动同步 provenance，不会 deprecate 未触及的 claim。\n\n## 收敛后收尾（Step 5e）\n\nReviewer 评分循环收敛后**必须执行完整三件套**——视觉 + 引用 + 溯源**全部跑完**再汇报 Director；不允许只跑一两项就提交。任一发现 critical/blocker 都要在汇报中显式列出，不得\"建议提交审稿\"压过失败信号。\n\n### 三件套执行顺序\n\n按下面顺序串行（每一步完成才进下一步，前一步失败不绕过）：\n\n```\n1. paper-visual-review 排版检查\n   └── Read skills/global/paper-visual-review.skill.md\n   └── pdf_to_images(pdf_path=projects/{project}/paper/main.pdf, pages=\"1-N\", dpi=200)\n       逐页检查图表分辨率 / 字号 / 边距溢出 / 公式 / 引用编号 / 缺失引用占位 [?]\n   └── cleanup_pdf_images(output_dir=<上一步返回的 output_dir>)  # 不留临时文件\n   └── 收集 findings：[{page, severity, issue}]\n   └── 出现 critical（图表溢出 / 缺失编号 / 公式乱码）→ 记入 visual_report，**不**立即返工，\n       与 verify_references / check_provenance_completeness 的结果**一并汇报 Director**\n\n2. verify_references 最终引用验证\n   └── verify_references(paper_dir=\"projects/{project}/paper\", project=..., skip_online=False)\n   └── 返回字段：status (ok/orphan_bib/missing_bib/not_found/mismatch) 按条聚合\n   └── critical 阈值：\n        - missing_bib（正文 \\cite 但 .bib 缺）→ 必须修，否则 LaTeX 编译失败\n        - not_found（OpenAlex 找不到）→ 疑似幻觉引用，自己 WebSearch 二次验证；仍找不到 → critical\n        - mismatch（年份/作者偏差）→ warning\n   └── 自己能改的小问题（missing_bib、年份） → edit_paper_section 修；改完**再调一次 verify_references** 确认通过\n\n3. check_provenance_completeness 溯源覆盖\n   └── check_provenance_completeness(project=...)\n   └── 返回：tier_distribution / untracked_numbers / invalidated_claims\n   └── 关键阈值：\n        - Tier 3 占比 > 30% → 必须汇报 Director（红线，不得静默交付）\n        - Tier X（invalidated，实验失败/被作废）≥ 1 条 → critical：claim 失去支撑，汇报 Director 决策是否改 claim\n        - untracked_numbers（正文出现但 provenance 没追踪的数字）≥ 5 → warning：派 Worker 补 provenance\n```\n\n### 汇报 Director 模板\n\n三件套全部跑完后**统一**汇报（不要分三次发），把所有 critical/warning 列在一处便于 Director 决策：\n\n```\npaper_agent_post_to_director(\n  text=\"[写作进展] Step 5 收尾完成\n         迭代轮数：{N}/5\n         最终 overall：{score}\n         checklist：全部 PASS / 还有 X 条 FAIL（已修复 / 待 Director 决策）\n\n         ===== 视觉检查 =====\n         检查页数：{n}/{total}\n         结论：PASS / 发现 X 条 critical + Y 条 warning\n         {若有 critical：逐条列出 page + 描述}\n\n         ===== 引用验证 =====\n         总数 X 条，已验证 Y 条\n         critical：missing_bib X 条 + 疑似幻觉 Y 条（已尝试 WebSearch 二次验证 → 结果）\n         warning：mismatch X 条\n         {若有 critical：列出条目 + 已采取的修复}\n\n         ===== Provenance 覆盖 =====\n         Tier 分布：T1 {a}% / T2 {b}% / T3 {c}% / TX {d}%\n         {若 T3 > 30% 或 TX ≥ 1：列出受影响的 claim/figure/table}\n         未追踪数字：X 个（详见 untracked_numbers）\n\n         ===== 建议 =====\n         {以下任选其一}\n         A. 视觉/引用/provenance 全部 PASS → 建议提交审稿（submit_paper_to_review）\n         B. 存在 critical → 请 Director 决策：{具体问题列表 + 建议修复方向}\n         C. provenance 红线触发 → 请 Director 决定：补实验 / 改 claim / 接受现状\",\n  project=...\n)\n```\n\nDirector 决定是否调 `submit_paper_to_review`——Paper Agent **不**主动调，这是 Director 的权限。\n\n### 红线（Step 5e 不可绕过）\n\n1. **三件套必须全跑**：跳过任一项直接汇报 = 违规，被 Director 打回时不接受\"我以为不必要\"\n2. **critical 不静默**：视觉 critical / verify_references critical / Tier X ≥ 1 / Tier 3 > 30% 必须显式写进汇报\n3. **不主动提交审稿**：哪怕全 PASS 也只能\"建议提交\"，submit_paper_to_review 是 Director 权限\n4. **修复后必须复验**：自己修了 missing_bib → 重跑 verify_references；补 provenance → 重跑 check_provenance_completeness\n5. **Patch 模式走 Phase E**：Patch 的收尾在 Phase E（max 3 轮 Reviewer），不复用 Step 5e 全套；Phase E 自己做 check_provenance_completeness + verify_references，视觉检查可选\n\n## 硬约束（与 Paper Agent 红线一致）\n\n1. **修改前必 git commit**——没有 commit 不开新一轮，避免 revert 失败\n2. **未验证引用不进 .bib**——Reviewer 指出新引用需求时，先 verify_references 再写入\n3. **checklist FAIL 项必须修复**——不参与\"连续两轮无新增 critical\"的轮数计数，但下一轮必须解决\n4. **overall 下降必 revert**——不允许\"将就一下\"\n5. **不自行降 claim**——claim 无支撑是 Director 决策，Paper Agent 只能改表述强度，不能改 claim 内容\n6. **Patch / Dream 模式不走本 skill**——Patch 走 Phase E（max 3 轮），Dream 跳过 Reviewer 迭代\n\n## 与 Reviewer 评分模板的合约\n\nReviewer 在 `prompts/roles/reviewer.md` §5.3 已规定返回格式：\n\n```\n[写作评审] 轮次 N/5\n维度评分（1-4）：Originality / Clarity / Soundness / Significance / Presentation\nOverall（1-10）：\n## 用户自定义必查项（如审查请求含 paper_checklist）\n- [chk_id]: PASS / FAIL — 理由\n## 具体问题\n- [severity] 位置 + 描述 + 建议\n```\n\nPaper Agent 解析时按位置抓字段——Reviewer 偶尔会漏维度分，**漏了的当作 4（满分）处理**，避免误判 overall 下降。\n",
      "numLines": 161,
      "startLine": 80,
      "totalLines": 240
    }
  },
  "sourceToolAssistantUUID": "1dc2cf2d-46a2-4343-9d98-42ecd264074a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
````

</details>

---


### Runtime record

_source line 1263_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[系统告警] Worker 日志 30 分钟无更新，可能卡死 (第 1/3 次告警)：  worker_id: worker_paper_figure_fig1_pipeline_20260517T172247 project: symb_invariant_consensus 日志最后内容: [tool_use] mcp__agent-ml-research__get_worker_status…",
  "leafUuid": "7f8c9c01-16c8-4b5f-87fc-f7955a0992b8",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1264_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Assistant

_source line 1265 · 2026-05-17T19:52:31.817Z_

<details><summary>Logged reasoning block</summary>

```text
I've read the full Step 5 skill. Now let me follow the protocol:

1. First, git commit the current paper state (round 0)
2. Assemble review request
3. Submit to Reviewer
4. Wait for response
5. Iterate

But wait - the project is not a git repository (from the environment info: "Is a git repository: false"). So I can't do git commits. Let me check.

Actually, the environment says the current working directory is not a git repo, but the project directory might be. Let me check.

Actually, looking at the skill more carefully, it says `git -C projects/{project} add paper/`. 

Let me verify whether the project directory has git initialized, and if not, I'll proceed with submitting to the Reviewer since that's the critical next step regardless of git availability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f8c9c01-16c8-4b5f-87fc-f7955a0992b8",
  "isSidechain": false,
  "requestId": "req_011Cb8iz7dz7QtMKea2kfvLG",
  "type": "assistant",
  "uuid": "3057b45e-3ab6-4d68-b98d-a12506d6c63b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBGcdB6v3E4QYgM6YMBbKu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3327,
      "cache_read_input_tokens": 140652,
      "output_tokens": 572,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 572,
          "cache_read_input_tokens": 140652,
          "cache_creation_input_tokens": 3327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3327
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


### Assistant

_source line 1266 · 2026-05-17T19:52:31.820Z_

Now entering Step 5. Let me check prerequisites and submit to Reviewer.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3057b45e-3ab6-4d68-b98d-a12506d6c63b",
  "isSidechain": false,
  "requestId": "req_011Cb8iz7dz7QtMKea2kfvLG",
  "type": "assistant",
  "uuid": "1dc9ce4b-3c1a-4f4d-9c0b-c4325588eb77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBGcdB6v3E4QYgM6YMBbKu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3327,
      "cache_read_input_tokens": 140652,
      "output_tokens": 572,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 572,
          "cache_read_input_tokens": 140652,
          "cache_creation_input_tokens": 3327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3327
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

_source line 1267 · 2026-05-17T19:52:34.194Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0191P2Z9xMkwJUCQDFpojtkW`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3 && git status --short projects/symb_invariant_consensus/docs/paper/ 2>/dev/null | head -20 || echo \"NOT A GIT REPO\"",
  "description": "Check git status of paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dc9ce4b-3c1a-4f4d-9c0b-c4325588eb77",
  "isSidechain": false,
  "requestId": "req_011Cb8iz7dz7QtMKea2kfvLG",
  "type": "assistant",
  "uuid": "4a25b2ff-33f2-4274-bce9-a5071c07ec5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBGcdB6v3E4QYgM6YMBbKu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3327,
      "cache_read_input_tokens": 140652,
      "output_tokens": 572,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 572,
          "cache_read_input_tokens": 140652,
          "cache_creation_input_tokens": 3327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3327
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

_source line 1268 · 2026-05-17T19:52:34.278Z_

<details><summary>↩ Tool result · `toolu_0191P2Z9xMkwJUCQDFpojtkW`</summary>

```text
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a25b2ff-33f2-4274-bce9-a5071c07ec5d",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "aadc6ec6-dff0-44fe-9ab0-adbac953e74e",
  "toolUseResult": {
    "stdout": "",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4a25b2ff-33f2-4274-bce9-a5071c07ec5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1269 · 2026-05-17T19:52:34.306Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XbvCDU3CmS2e5RBjp9UPe9`</summary>

```json
{
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aadc6ec6-dff0-44fe-9ab0-adbac953e74e",
  "isSidechain": false,
  "requestId": "req_011Cb8iz7dz7QtMKea2kfvLG",
  "type": "assistant",
  "uuid": "f24452d2-e7be-4a72-8ca1-a3fbd78052b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBGcdB6v3E4QYgM6YMBbKu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3327,
      "cache_read_input_tokens": 140652,
      "output_tokens": 572,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 572,
          "cache_read_input_tokens": 140652,
          "cache_creation_input_tokens": 3327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3327
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

_source line 1270 · 2026-05-17T19:52:34.322Z_

<details><summary>↩ Tool result · reported error · `toolu_01XbvCDU3CmS2e5RBjp9UPe9`</summary>

```text
Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'paper_checklist.yaml'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f24452d2-e7be-4a72-8ca1-a3fbd78052b0",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "a6d126f7-839d-46be-97ef-7e759f355cdd",
  "toolUseResult": "Error: Error executing tool read_project_file: 1 validation error for read_project_fileArguments\nproject\n  Field required [type=missing, input_value={'file': 'paper_checklist.yaml'}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing",
  "sourceToolAssistantUUID": "f24452d2-e7be-4a72-8ca1-a3fbd78052b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1271 · 2026-05-17T19:52:38.799Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AJQLjV7Q2GCU49H1bMoM2w`</summary>

```json
{
  "command": "git -C /home/ubuntu/.agent-ml-research-idea_gen_0513_3 rev-parse --is-inside-work-tree 2>/dev/null && echo \"IS_GIT_REPO\" || echo \"NOT_GIT_REPO\"",
  "description": "Check if workspace is a git repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6d126f7-839d-46be-97ef-7e759f355cdd",
  "isSidechain": false,
  "requestId": "req_011Cb8j1GUpuysgwYzHWTiMv",
  "type": "assistant",
  "uuid": "cf44b05a-f206-4db8-bf7f-2d0702b9c652",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013nETToSx4zkTU8biMm1LMU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 143979,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 143979,
          "cache_creation_input_tokens": 771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 771
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

_source line 1272 · 2026-05-17T19:52:38.873Z_

<details><summary>↩ Tool result · `toolu_01AJQLjV7Q2GCU49H1bMoM2w`</summary>

```text
NOT_GIT_REPO
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf44b05a-f206-4db8-bf7f-2d0702b9c652",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "8e8f3951-a1e6-481a-8a2b-921c6191b684",
  "toolUseResult": {
    "stdout": "NOT_GIT_REPO",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cf44b05a-f206-4db8-bf7f-2d0702b9c652",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1273 · 2026-05-17T19:52:39.389Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0129qgiyfw4obo9ZzER4wike`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_checklist.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT FOUND\"",
  "description": "Check if paper_checklist.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e8f3951-a1e6-481a-8a2b-921c6191b684",
  "isSidechain": false,
  "requestId": "req_011Cb8j1GUpuysgwYzHWTiMv",
  "type": "assistant",
  "uuid": "afe7dcb0-7345-4f99-9e0e-a7362e4f0e5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013nETToSx4zkTU8biMm1LMU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 143979,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 250,
          "cache_read_input_tokens": 143979,
          "cache_creation_input_tokens": 771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 771
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

_source line 1274 · 2026-05-17T19:52:39.446Z_

<details><summary>↩ Tool result · `toolu_0129qgiyfw4obo9ZzER4wike`</summary>

```text
NOT FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afe7dcb0-7345-4f99-9e0e-a7362e4f0e5c",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "1ef77234-4fad-41db-ab2a-d8a8c661c029",
  "toolUseResult": {
    "stdout": "NOT FOUND",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "afe7dcb0-7345-4f99-9e0e-a7362e4f0e5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1275 · 2026-05-17T19:52:45.947Z_

<details><summary>Logged reasoning block</summary>

```text
No git repo and no paper_checklist.yaml. I'll skip the git commit step (no repo) and the checklist injection (no checklist). Let me proceed directly to submitting the review request.

For the review request, I need to assemble:
1. The full LaTeX content (or reference to it)
2. The writing_plan.yaml path
3. No checklist to inject

Let me compose the review request and submit it via paper_agent_request_review.

Actually, I need to load the tool schema first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ef77234-4fad-41db-ab2a-d8a8c661c029",
  "isSidechain": false,
  "requestId": "req_011Cb8j1eBnvvNDvVW3RCkoD",
  "type": "assistant",
  "uuid": "a70d4b70-1525-4415-b846-758898958ed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtmNWvyfki9W13gjpqcpLx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 144750,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 144750,
          "cache_creation_input_tokens": 321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 321
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


### Assistant

_source line 1276 · 2026-05-17T19:52:46.975Z_

No git repo available, no paper_checklist.yaml. Proceeding to submit Reviewer request (Step 5 Round 1).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a70d4b70-1525-4415-b846-758898958ed5",
  "isSidechain": false,
  "requestId": "req_011Cb8j1eBnvvNDvVW3RCkoD",
  "type": "assistant",
  "uuid": "146e3895-1d70-45df-98e7-912c0f1ba8fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtmNWvyfki9W13gjpqcpLx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 144750,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 144750,
          "cache_creation_input_tokens": 321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 321
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

_source line 1277 · 2026-05-17T19:52:47.313Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TrS6i1CEcDhxrM1U2W7Vcy`</summary>

```json
{
  "query": "paper_agent_request_review",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "146e3895-1d70-45df-98e7-912c0f1ba8fb",
  "isSidechain": false,
  "requestId": "req_011Cb8j1eBnvvNDvVW3RCkoD",
  "type": "assistant",
  "uuid": "cdcf0ccb-2001-4365-8523-872385720326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtmNWvyfki9W13gjpqcpLx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 144750,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 144750,
          "cache_creation_input_tokens": 321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 321
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

_source line 1278 · 2026-05-17T19:52:47.328Z_

<details><summary>↩ Tool result · `toolu_01TrS6i1CEcDhxrM1U2W7Vcy`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__paper_agent_request_review"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdcf0ccb-2001-4365-8523-872385720326",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "959f60c0-95a8-45a7-ab33-b8862c2b75a5",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__paper_agent_request_review"
    ],
    "query": "paper_agent_request_review",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "cdcf0ccb-2001-4365-8523-872385720326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1279 · 2026-05-17T19:52:47.383Z_

```json
{
  "parentUuid": "959f60c0-95a8-45a7-ab33-b8862c2b75a5",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "eef0226d-6c91-45d7-9099-a5fb198d3227",
  "timestamp": "2026-05-17T19:52:47.383Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

---


### Tool call

_source line 1280 · 2026-05-17T19:53:14.420Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_agent_request_review · `toolu_01TDWRPht1f1mfR2TFYXiLrN`</summary>

```json
{
  "text": "[审查请求] Step 5 Round 1/5 — Full Draft Review\n\n## 论文信息\n- 标题: The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting\n- 目标会议: EMNLP 2026 (main track, 8-page limit)\n- 论文类型: Diagnostic analysis paper (negative result + causal localization + constructive upper bound)\n- Writing Plan: projects/symb_invariant_consensus/writing_plan.yaml\n- PDF: projects/symb_invariant_consensus/docs/paper/main.pdf (12 pages: 8 main + 1.5 refs + 2.5 appendix)\n\n## 编译状态\n- ✅ 编译成功，0 undefined refs/cites\n- 主要内容恰好 8 页（EMNLP 限制）\n- check_paper_consistency: 0 critical, 0 warning\n\n## 章节清单\n1. abstract.tex (~216 words) — oracle-positive framing\n2. introduction.tex (~1164 words) — oracle-led narrative, 5 paras + contribution list\n3. related_work.tex (~950 words) — 6 clusters, 26 citations\n4. method.tex (~1400 words) — SICA pipeline + MAX-SAT + C0 + oracle design + fig:pipeline\n5. experiments.tex (~2400 words) — Table 1 (main results), Table 2 (oracle), Table 3 (ablation), Fig 2-3\n6. discussion.tex (~600 words) — oracle as intervention + constraint failure modes + cost analysis + published methods + constructive directions + C0 diagnostic\n7. conclusion.tex (~346 words) — summary + practical implications + future directions\n8. limitations_content.tex (~130 words) — 5 limitations\n\n## 核心 Claim（需审查一致性）\n- SICA = SC across all conditions (N > 1,300), all deltas n.s.\n- Oracle-SICA: +8.82pp (p < 0.001) on FOLIO-204\n- 803/804 agreement MAX-SAT vs count-only\n- 11.5% discriminative constraints (by count)\n- 48.7% wall-clock overhead\n- 5 model families (7B-32B), 3 reasoning domains\n\n## 审查重点\n1. Abstract / Introduction / Conclusion 数字一致性\n2. Oracle-led narrative 是否贯穿全文（不是负面结果报告）\n3. \"capability trap\" 引入是否自然、低调（不是 headline）\n4. C0 是否正确定位为第三贡献（不是 headline）\n5. 去 AI 写作标志：em-dash / -ing 短语 / 过度分段 / 用词黑名单\n6. 引用覆盖是否充分（直接相关方法、baseline、benchmark、理论基础）\n7. 图表引用是否正确、caption 是否自包含\n8. Contribution 列表每条是否有对应 section/table 支撑\n9. 写作密度与 8 页限制的平衡\n\n## LaTeX 文件路径\n所有 .tex 文件位于: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eef0226d-6c91-45d7-9099-a5fb198d3227",
  "isSidechain": false,
  "requestId": "req_011Cb8j2ECBpFhWhh3AwzDfV",
  "type": "assistant",
  "uuid": "00469325-6caa-4e01-ac64-f5fc165b28a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHWXDZcQbMrqMMpBGchSgv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 145071,
      "output_tokens": 958,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 958,
          "cache_read_input_tokens": 145071,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 1281 · 2026-05-17T19:53:15.700Z_

<details><summary>↩ Tool result · `toolu_01TDWRPht1f1mfR2TFYXiLrN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reviewer_session\": \"feishu:group:oc_319977a04ca60b6c4c69a2a8d4141a75:reviewer\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00469325-6caa-4e01-ac64-f5fc165b28a4",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "451d93a7-c5b0-4d38-ba46-522e43511170",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reviewer_session\\\": \\\"feishu:group:oc_319977a04ca60b6c4c69a2a8d4141a75:reviewer\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reviewer_session\": \"feishu:group:oc_319977a04ca60b6c4c69a2a8d4141a75:reviewer\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "00469325-6caa-4e01-ac64-f5fc165b28a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1282 · 2026-05-17T19:53:22.781Z_

Step 5 Round 1 审查请求已提交 Reviewer。等待评分结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "451d93a7-c5b0-4d38-ba46-522e43511170",
  "isSidechain": false,
  "requestId": "req_011Cb8j4KEMhABN7LEx7wqVS",
  "type": "assistant",
  "uuid": "d8d92c84-4b81-4632-9501-1829c772ebe7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPRj7AqbDFAU6HHoQN5ega",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 145751,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 145751,
          "cache_creation_input_tokens": 1035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1035
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

_source line 1283 · 2026-05-17T19:53:28.013Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_agent_post_to_director · `toolu_019Tcjh2GEXmiFjNC52nhn1i`</summary>

```json
{
  "text": "[写作进展] Step 5 启动\n\nStep 5 Round 1/5 审查请求已提交 Reviewer。等待评分返回后进入修改循环。\n\n注：workspace 非 git repo，无法执行 git commit 作为 revert 锚点。paper_checklist.yaml 不存在，未注入自定义必查项。\n\n当前状态：等待 Reviewer 响应。",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8d92c84-4b81-4632-9501-1829c772ebe7",
  "isSidechain": false,
  "requestId": "req_011Cb8j4KEMhABN7LEx7wqVS",
  "type": "assistant",
  "uuid": "fbef7429-69dd-4ccf-8651-a22e85135188",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPRj7AqbDFAU6HHoQN5ega",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1035,
      "cache_read_input_tokens": 145751,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 145751,
          "cache_creation_input_tokens": 1035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1035
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

_source line 1284 · 2026-05-17T19:53:29.079Z_

<details><summary>↩ Tool result · `toolu_019Tcjh2GEXmiFjNC52nhn1i`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbef7429-69dd-4ccf-8651-a22e85135188",
  "isSidechain": false,
  "promptId": "d50bdd0a-c0fa-4d40-8234-48cff8f4b788",
  "type": "user",
  "uuid": "35246e31-f731-459d-a36e-409dffda7204",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "fbef7429-69dd-4ccf-8651-a22e85135188",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Runtime record

_source line 1285_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise paper results with oracle FOLIO constraint experiments",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


### Runtime record

_source line 1286 · 2026-05-17T19:53:36.618Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T19:53:36.618Z",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "content": "[Director 指令] [数据交付 — Table 更新] 以下数据已就绪，请更新对应表格：\n\n**1. Table 1 新增 Qwen2.5-7B 行**：\n- Model: Qwen2.5-7B-Instruct\n- Domain: FOLIO+PW†\n- n: 56 (4 problems failed, excluded)\n- SICA: 69.64%, SC: 69.64%, Δ: 0.00pp\n- p-value: 1.0 (exact binomial, 2:2 discordant)\n- 标 † (n≤60)\n\n**2. Table 3 Constraint Ablation（T3 解除阻塞）**：\n| Method | Accuracy | Δ vs SC | Agreement with SC |\n|--------|----------|---------|-------------------|\n| SICA-MaxSAT | 76.49% | +0.25pp | — |\n| Count-only | 76.62% | +0.37pp | 803/804 (99.9%) |\n| Random-weight | 75.87% | -0.37pp | 96.8%±0.5% |\n| SC@K=12 | 76.24% | — | — |\n\n数据基于 exp-001 (n=804, Qwen2.5-14B, FOLIO+PW)。MaxSAT 与 Count-only 唯一分歧在 folio_062（tie case）。\n\n**3. Table 2 更新 Qwen-7B 行**：\n- C0: 42.1% (24/57)\n- Extraction rate: 0.9417\n- Contradiction rate: 0.0274\n\n**4. exp-004 C0 与 within-family scaling**：\nQwen-7B C0=42.1% > Qwen-14B C0=38.2% (combined) → 弱模型有更高 diversity，但 Δ=0。**不要声称 C0 与模型规模单调相关**（D012 对比不一致），只说\"instruction-scale 模型均有 C0>20% 但 Δ≈0\"。"
}
```

---


### Runtime record

_source line 1287 · 2026-05-17T19:53:36.618Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T19:53:36.618Z",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1"
}
```

---


## Round 33

## Round 33

2 recorded events


### User

_source line 1288 · 2026-05-17T19:53:36.604Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35246e31-f731-459d-a36e-409dffda7204",
  "isSidechain": false,
  "promptId": "765071d9-74cc-40f8-a6c7-5d18bfb168d0",
  "type": "user",
  "isMeta": true,
  "uuid": "d280ef41-a2b1-403f-a7dd-e231e5f352cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1289 · 2026-05-17T19:53:36.604Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d280ef41-a2b1-403f-a7dd-e231e5f352cf",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "39069fdb-6288-42c8-a0bd-8588150a1a72",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "id": "32cfcbda-ca1a-4ce5-8341-0fc4af73ecf8",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 34

## Round 34

54 recorded events


### User

_source line 1290 · 2026-05-17T19:53:36.740Z_

[Director 指令] [数据交付 — Table 更新] 以下数据已就绪，请更新对应表格：

**1. Table 1 新增 Qwen2.5-7B 行**：
- Model: Qwen2.5-7B-Instruct
- Domain: FOLIO+PW†
- n: 56 (4 problems failed, excluded)
- SICA: 69.64%, SC: 69.64%, Δ: 0.00pp
- p-value: 1.0 (exact binomial, 2:2 discordant)
- 标 † (n≤60)

**2. Table 3 Constraint Ablation（T3 解除阻塞）**：
| Method | Accuracy | Δ vs SC | Agreement with SC |
|--------|----------|---------|-------------------|
| SICA-MaxSAT | 76.49% | +0.25pp | — |
| Count-only | 76.62% | +0.37pp | 803/804 (99.9%) |
| Random-weight | 75.87% | -0.37pp | 96.8%±0.5% |
| SC@K=12 | 76.24% | — | — |

数据基于 exp-001 (n=804, Qwen2.5-14B, FOLIO+PW)。MaxSAT 与 Count-only 唯一分歧在 folio_062（tie case）。

**3. Table 2 更新 Qwen-7B 行**：
- C0: 42.1% (24/57)
- Extraction rate: 0.9417
- Contradiction rate: 0.0274

**4. exp-004 C0 与 within-family scaling**：
Qwen-7B C0=42.1% > Qwen-14B C0=38.2% (combined) → 弱模型有更高 diversity，但 Δ=0。**不要声称 C0 与模型规模单调相关**（D012 对比不一致），只说"instruction-scale 模型均有 C0>20% 但 Δ≈0"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39069fdb-6288-42c8-a0bd-8588150a1a72",
  "isSidechain": false,
  "promptId": "765071d9-74cc-40f8-a6c7-5d18bfb168d0",
  "type": "user",
  "uuid": "8dd4c975-ff32-4d3d-b402-b75fefc2c994",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Assistant

_source line 1291 · 2026-05-17T19:53:43.139Z_

<details><summary>Logged reasoning block</summary>

```text
The Director wants me to update several tables in experiments.tex with new data. Let me:

1. Read experiments.tex to find the current table structures
2. Update Table 1 with Qwen2.5-7B row
3. Update Table 3 with constraint ablation data
4. Update Table 2 with Qwen-7B C0 data
5. Make sure not to claim C0 has monotonic relationship with model scale

Let me start by reading experiments.tex to find the table locations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dd4c975-ff32-4d3d-b402-b75fefc2c994",
  "isSidechain": false,
  "requestId": "req_011Cb8j5sEE2BZXxoCPPz7vd",
  "type": "assistant",
  "uuid": "e3e422d6-0668-40d2-b5dd-52234812afbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WfADqQv2dA1o4diXTzWyA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 134373,
      "cache_read_input_tokens": 11841,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 134373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 272,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 134373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 134373
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 106173
      }
    }
  }
}
```

</details>

---


### Assistant

_source line 1292 · 2026-05-17T19:53:43.610Z_

收到 Director 数据交付指令。正在读取 experiments.tex 找到需要更新的表格位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3e422d6-0668-40d2-b5dd-52234812afbb",
  "isSidechain": false,
  "requestId": "req_011Cb8j5sEE2BZXxoCPPz7vd",
  "type": "assistant",
  "uuid": "c947c16c-269f-4cad-86a0-cdca1adea829",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WfADqQv2dA1o4diXTzWyA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 134373,
      "cache_read_input_tokens": 11841,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 134373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 272,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 134373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 134373
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 106173
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 1293 · 2026-05-17T19:53:45.007Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HRpXk9eAc3Y2PPJvBvuvmB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c947c16c-269f-4cad-86a0-cdca1adea829",
  "isSidechain": false,
  "requestId": "req_011Cb8j5sEE2BZXxoCPPz7vd",
  "type": "assistant",
  "uuid": "b96ac463-319e-4352-ae06-b953cd445cec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WfADqQv2dA1o4diXTzWyA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 134373,
      "cache_read_input_tokens": 11841,
      "output_tokens": 272,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 134373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 272,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 134373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 134373
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 106173
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 1294 · 2026-05-17T19:53:45.029Z_

<details><summary>↩ Tool result · `toolu_01HRpXk9eAc3Y2PPJvBvuvmB`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across five models and three reasoning domains, with two additional benchmarks as operating-regime probes.
8	
9	\paragraph{Models.} We test Qwen2.5-14B-Instruct~\cite{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\cite{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\cite{dubey2024llama3}, DeepSeek-R1-Distill-Qwen-7B~\cite{guo2025deepseekr1}, and QwQ-32B~\cite{qwen2024qwq}, spanning 7B to 32B parameters.
10	
11	\paragraph{Datasets.} FOLIO~\cite{han2022folio} provides formal logic problems with gold FOL annotations ($n=204$), enabling the oracle control (\S\ref{sec:oracle}). ProofWriter~\cite{tafjord2021proofwriter} tests multi-step deductive reasoning ($n=600$). StrategyQA~\cite{geva2021strategyqa} evaluates commonsense reasoning ($n=200$ for LLaMA-3.1-8B; $n=60$ for other models). ARC-Challenge~\cite{clark2018arc} covers science questions ($n=60$). GSM8K~\cite{cobbe2021gsm8k} ($n=30$) and AIME 2024 ($n=22$) serve as operating-regime probes, both exhibiting near-ceiling SC accuracy or near-zero $C_0$.
12	
13	\paragraph{Parameters.} We sample $K=12$ traces per question at temperature $T=0.7$. Z3~\cite{demoura2008z3} solves each MAX-SAT instance with a 10-second timeout. Temperature ablation varies $T \in \{0.3, 0.5, 0.7, 1.0\}$.
14	
15	\paragraph{Metrics.} We report accuracy (\%), $C_0$ (\S\ref{sec:c0}), and $\Delta = \text{SICA} - \text{SC}$ in percentage points (pp). Statistical significance uses the McNemar test at $\alpha = 0.05$. For conditions with $n \geq 200$, we compute 95\% bootstrap confidence intervals with 10{,}000 resamples.
16	
17	
18	\subsection{Main Results: SICA Provides No Significant Gain}
19	\label{sec:main-results}
20	
21	Table~\ref{tab:main_results} reports results across all model-domain conditions. Symbolic constraint aggregation does not improve over majority voting.
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Accuracy of Self-Consistency (SC) and SICA across three primary domains and two supplementary probes. $\Delta$ denotes the SICA$-$SC gap in percentage points. No self-extraction condition reaches statistical significance ($\alpha = 0.05$). The oracle upper bound replaces self-extracted constraints with gold FOL annotations verified by Z3. $\dagger$: $n \leq 60$, insufficient power for confirmatory conclusions. $\ddagger$: $n=30$ pilot, included for operating regime characterization. $^a$McNemar test for $n \geq 200$; exact binomial test on discordant pairs for $n \leq 60$.}
27	\label{tab:main_results}
28	\begin{tabular}{@{}llrrrrl@{}}
29	\toprule
30	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p^a$ \\
31	\midrule
32	Qwen2.5-14B & FOLIO & 204 & 79.41 & 79.41 & 0.00 & --- \\
33	Qwen2.5-14B & ProofWriter & 600 & 75.17 & 75.50 & $+$0.33 & n.s. \\
34	Qwen2.5-14B & StrategyQA$^\dagger$ & 60 & 53.33 & 56.67 & $+$3.33 & 0.50 \\
35	Qwen2.5-14B & ARC-Chall.$^\dagger$ & 60 & 96.67 & 95.00 & $-$1.67 & --- \\
36	Mistral-7B & FOLIO+PW$^\dagger$ & 60 & 48.33 & 48.33 & 0.00 & 1.000 \\
37	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
38	LLaMA-3.1-8B & FOLIO & 204 & 63.24 & 60.78 & $-$2.45 & 0.267 \\
39	DeepSeek-R1-7B & FOLIO+PW$^\dagger$ & 60 & 71.67 & 68.33 & $-$3.33 & 0.480 \\
40	QwQ-32B & AIME$^\dagger$ & 22 & 72.7 & 72.7 & 0.00 & --- \\
41	Qwen2.5-14B & GSM8K$^\ddagger$ & 30 & 96.67 & 96.67 & 0.00 & --- \\
42	\midrule
43	\multicolumn{7}{l}{\textit{Oracle upper bound (gold FOL + Z3 replaces self-extraction)}} \\
44	Qwen2.5-14B & FOLIO & 204 & 79.41 & 88.24 & $+$8.82 & $<$0.001 \\
45	\bottomrule
46	\end{tabular}
47	\end{table*}
48	
49	Across the four adequately powered conditions ($n \geq 200$, combined $N = 1{,}208$), $\Delta$ ranges from $-2.45$ to $+2.00$~pp, with no condition reaching significance ($p = 0.267$ and $0.424$ for the two nonzero gaps). The six smaller conditions ($n \leq 60$) are consistent with this null pattern: $\Delta$ ranges from $-3.33$ to $+3.33$~pp, all nonsignificant. QwQ-32B on AIME produces identical outputs ($C_0 = 2.6\%$), confirming that reasoning-specialized models leave no room for SICA to operate.
50	
51	Across ten conditions, five models, and more than 1,300 instances, SICA does not improve upon majority voting. The oracle row tells a different story: gold FOL constraints yield $+8.82$~pp over SC ($p < 0.001$), proving the aggregation mechanism works when given discriminative constraints.
52	
53	
54	\subsection{Oracle Control: The Aggregation Mechanism Is Effective}
55	\label{sec:oracle}
56	
57	We construct an oracle variant that replaces self-extracted constraints with gold FOL annotations from FOLIO ($n = 204$). Z3 evaluates ground-truth formulas against each candidate answer; all other pipeline components remain identical.
58	
59	Oracle-SICA achieves 88.24\% accuracy versus 79.41\% for both SC and standard SICA. The $+8.82$~pp gain is highly significant (McNemar $p = 6.15 \times 10^{-5}$). Z3 checks on gold annotations agree with ground-truth labels for 193/204 problems (94.6\%). This establishes that the MAX-SAT mechanism is sound given correct constraints, and that the bottleneck lies entirely in extraction quality.
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b96ac463-319e-4352-ae06-b953cd445cec",
  "isSidechain": false,
  "promptId": "765071d9-74cc-40f8-a6c7-5d18bfb168d0",
  "type": "user",
  "uuid": "7719c1e5-6886-43f1-815b-c1c58273a5b7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp-setup}\n\nWe evaluate SICA against Self-Consistency (SC) across five models and three reasoning domains, with two additional benchmarks as operating-regime probes.\n\n\\paragraph{Models.} We test Qwen2.5-14B-Instruct~\\cite{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\\cite{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\\cite{dubey2024llama3}, DeepSeek-R1-Distill-Qwen-7B~\\cite{guo2025deepseekr1}, and QwQ-32B~\\cite{qwen2024qwq}, spanning 7B to 32B parameters.\n\n\\paragraph{Datasets.} FOLIO~\\cite{han2022folio} provides formal logic problems with gold FOL annotations ($n=204$), enabling the oracle control (\\S\\ref{sec:oracle}). ProofWriter~\\cite{tafjord2021proofwriter} tests multi-step deductive reasoning ($n=600$). StrategyQA~\\cite{geva2021strategyqa} evaluates commonsense reasoning ($n=200$ for LLaMA-3.1-8B; $n=60$ for other models). ARC-Challenge~\\cite{clark2018arc} covers science questions ($n=60$). GSM8K~\\cite{cobbe2021gsm8k} ($n=30$) and AIME 2024 ($n=22$) serve as operating-regime probes, both exhibiting near-ceiling SC accuracy or near-zero $C_0$.\n\n\\paragraph{Parameters.} We sample $K=12$ traces per question at temperature $T=0.7$. Z3~\\cite{demoura2008z3} solves each MAX-SAT instance with a 10-second timeout. Temperature ablation varies $T \\in \\{0.3, 0.5, 0.7, 1.0\\}$.\n\n\\paragraph{Metrics.} We report accuracy (\\%), $C_0$ (\\S\\ref{sec:c0}), and $\\Delta = \\text{SICA} - \\text{SC}$ in percentage points (pp). Statistical significance uses the McNemar test at $\\alpha = 0.05$. For conditions with $n \\geq 200$, we compute 95\\% bootstrap confidence intervals with 10{,}000 resamples.\n\n\n\\subsection{Main Results: SICA Provides No Significant Gain}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main_results} reports results across all model-domain conditions. Symbolic constraint aggregation does not improve over majority voting.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Accuracy of Self-Consistency (SC) and SICA across three primary domains and two supplementary probes. $\\Delta$ denotes the SICA$-$SC gap in percentage points. No self-extraction condition reaches statistical significance ($\\alpha = 0.05$). The oracle upper bound replaces self-extracted constraints with gold FOL annotations verified by Z3. $\\dagger$: $n \\leq 60$, insufficient power for confirmatory conclusions. $\\ddagger$: $n=30$ pilot, included for operating regime characterization. $^a$McNemar test for $n \\geq 200$; exact binomial test on discordant pairs for $n \\leq 60$.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p^a$ \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 204 & 79.41 & 79.41 & 0.00 & --- \\\\\nQwen2.5-14B & ProofWriter & 600 & 75.17 & 75.50 & $+$0.33 & n.s. \\\\\nQwen2.5-14B & StrategyQA$^\\dagger$ & 60 & 53.33 & 56.67 & $+$3.33 & 0.50 \\\\\nQwen2.5-14B & ARC-Chall.$^\\dagger$ & 60 & 96.67 & 95.00 & $-$1.67 & --- \\\\\nMistral-7B & FOLIO+PW$^\\dagger$ & 60 & 48.33 & 48.33 & 0.00 & 1.000 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 63.24 & 60.78 & $-$2.45 & 0.267 \\\\\nDeepSeek-R1-7B & FOLIO+PW$^\\dagger$ & 60 & 71.67 & 68.33 & $-$3.33 & 0.480 \\\\\nQwQ-32B & AIME$^\\dagger$ & 22 & 72.7 & 72.7 & 0.00 & --- \\\\\nQwen2.5-14B & GSM8K$^\\ddagger$ & 30 & 96.67 & 96.67 & 0.00 & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Oracle upper bound (gold FOL + Z3 replaces self-extraction)}} \\\\\nQwen2.5-14B & FOLIO & 204 & 79.41 & 88.24 & $+$8.82 & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nAcross the four adequately powered conditions ($n \\geq 200$, combined $N = 1{,}208$), $\\Delta$ ranges from $-2.45$ to $+2.00$~pp, with no condition reaching significance ($p = 0.267$ and $0.424$ for the two nonzero gaps). The six smaller conditions ($n \\leq 60$) are consistent with this null pattern: $\\Delta$ ranges from $-3.33$ to $+3.33$~pp, all nonsignificant. QwQ-32B on AIME produces identical outputs ($C_0 = 2.6\\%$), confirming that reasoning-specialized models leave no room for SICA to operate.\n\nAcross ten conditions, five models, and more than 1,300 instances, SICA does not improve upon majority voting. The oracle row tells a different story: gold FOL constraints yield $+8.82$~pp over SC ($p < 0.001$), proving the aggregation mechanism works when given discriminative constraints.\n\n\n\\subsection{Oracle Control: The Aggregation Mechanism Is Effective}\n\\label{sec:oracle}\n\nWe construct an oracle variant that replaces self-extracted constraints with gold FOL annotations from FOLIO ($n = 204$). Z3 evaluates ground-truth formulas against each candidate answer; all other pipeline components remain identical.\n\nOracle-SICA achieves 88.24\\% accuracy versus 79.41\\% for both SC and standard SICA. The $+8.82$~pp gain is highly significant (McNemar $p = 6.15 \\times 10^{-5}$). Z3 checks on gold annotations agree with ground-truth labels for 193/204 problems (94.6\\%). This establishes that the MAX-SAT mechanism is sound given correct constraints, and that the bottleneck lies entirely in extraction quality.\n",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 110
    }
  },
  "sourceToolAssistantUUID": "b96ac463-319e-4352-ae06-b953cd445cec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora"
}
```

</details>

---


### Tool call

_source line 1295 · 2026-05-17T19:53:49.748Z_

<details open><summary>🔧 Tool call — Read · `toolu_012DhkcWPwitucm2HZ44pQtC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
  "offset": 60,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7719c1e5-6886-43f1-815b-c1c58273a5b7",
  "isSidechain": false,
  "requestId": "req_011Cb8j6UmteaNZEoFRoEcpZ",
  "type": "assistant",
  "uuid": "6c24111f-0b34-4d2b-bb61-3f7370e177f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/paper_agent_644edc69",
  "sessionId": "6e0077cd-ef03-4ff5-b72c-7cf0ad14c0f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-noodling-aurora",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRM17NhbNwnyL8tpifde7T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2388,
      "cache_read_input_tokens": 146214,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 146214,
          "cache_creation_input_tokens": 2388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2388
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
