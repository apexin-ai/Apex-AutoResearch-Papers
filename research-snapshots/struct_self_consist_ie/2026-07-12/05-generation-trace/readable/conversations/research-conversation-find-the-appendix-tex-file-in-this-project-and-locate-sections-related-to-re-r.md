# Research conversation: Find the appendix.tex file in this project and locate sections related to "RE" (relation extraction), particularly any t

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a984115b55b0e4fdf.jsonl`
- **Structured JSON:** [`10e3a1aeff0bc332c3d6.json`](../../sessions/10/10e3a1aeff0bc332c3d6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-22T08:10:22.819Z_

Find the appendix.tex file in this project and locate sections related to "RE" (relation extraction), particularly any tables or text containing degeneracy, MV delta, LP-best, oracle numbers for RE. The project is at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/. Look in docs/paper/sections/ or similar paths. Search for "re_extension" or "RE" or "relation" in tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "191cbec0-c308-4e87-8ae3-7663cca574da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T08:10:24.419Z_

I'll help you find the appendix.tex file and locate sections related to relation extraction (RE). Let me search systematically through the project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "191cbec0-c308-4e87-8ae3-7663cca574da",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGW9c2hxv5z7oJYJmxo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7da97e0c-8cce-4c99-b959-511331d3063a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017E2beZvsXd9fenCsEtKS7s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35718,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35718,
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

_source line 3 · 2026-05-22T08:10:24.574Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DBj8nUJktyJNZrHt8VZFyE`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7da97e0c-8cce-4c99-b959-511331d3063a",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGW9c2hxv5z7oJYJmxo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "20773441-ed4d-426b-98d5-ee97cccb55b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017E2beZvsXd9fenCsEtKS7s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35718,
      "cache_read_input_tokens": 0,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 35718
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 35718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 35718,
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

_source line 4 · 2026-05-22T08:10:24.769Z_

<details><summary>↩ Tool result · `toolu_01DBj8nUJktyJNZrHt8VZFyE`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_ci_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/freeform_ablation_appendix_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_scaling_appendix_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/per_type_lp_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_021_fewnerd_full/paper/per_type_lp_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/scale_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/scaling_narrative_A_monotonic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/scaling_narrative_B_nonmonotonic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_B_nonmonotonic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_A_monotonic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_qwen25_72b_fewshot/paper/zs_vs_fs_comparison_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/zs_vs_fs_comparison_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_qwen25_72b_fewshot/paper/tab_72b_zs_vs_fs_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/tab_72b_zs_vs_fs_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/theorem.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/p_impossibility/theorem.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theoretical.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/power_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/holm_bonferroni_enumeration.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/entity_independence_paragraph.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/e5_hyperparam_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/e5_hyperparam_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20773441-ed4d-426b-98d5-ee97cccb55b9",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "38ec0a96-3ae4-479e-bf0d-875699b57b3f",
  "sourceToolAssistantUUID": "20773441-ed4d-426b-98d5-ee97cccb55b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-22T08:10:26.855Z_

Great! I found the appendix.tex file. Now let me search for RE-related content in that file and other relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38ec0a96-3ae4-479e-bf0d-875699b57b3f",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGWJ6G8HZw6GSCME2qV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa3e26d9-e948-47e1-9f03-f83cb7627af6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01999A3N12mbwZ5oFPs8edJX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4178,
      "cache_read_input_tokens": 35718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4178,
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

_source line 6 · 2026-05-22T08:10:27.218Z_

<details open><summary>🔧 Tool call — Read · `toolu_011RRkdnKmdtYAFNVfQSR82G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa3e26d9-e948-47e1-9f03-f83cb7627af6",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGWJ6G8HZw6GSCME2qV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0de534e-96a6-42f7-865d-e63ab7999fd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01999A3N12mbwZ5oFPs8edJX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4178,
      "cache_read_input_tokens": 35718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4178,
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

_source line 7 · 2026-05-22T08:10:27.532Z_

<details><summary>↩ Tool result · reported error · `toolu_011RRkdnKmdtYAFNVfQSR82G`</summary>

```text
File content (65633 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0de534e-96a6-42f7-865d-e63ab7999fd3",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "98ce413e-5437-4a68-96f0-44f427206731",
  "toolUseResult": "Error: File content (65633 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "a0de534e-96a6-42f7-865d-e63ab7999fd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T08:10:27.891Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Wo5JrRcouuTgZbvWVDHZXD`</summary>

```json
{
  "pattern": "(?i)(re_extension|relation.extraction|degeneracy|MV.delta|LP-best|oracle)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ce413e-5437-4a68-96f0-44f427206731",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGWJ6G8HZw6GSCME2qV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c12a17a4-a7a1-45e6-99a8-e174800afdf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01999A3N12mbwZ5oFPs8edJX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4178,
      "cache_read_input_tokens": 35718,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4178
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 255,
          "cache_read_input_tokens": 35718,
          "cache_creation_input_tokens": 4178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4178,
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

_source line 9 · 2026-05-22T08:10:27.968Z_

<details><summary>↩ Tool result · `toolu_01Wo5JrRcouuTgZbvWVDHZXD`</summary>

```text
&lt;persisted-output>
Output too large (30.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-70248b8a/c3b01396-4193-441d-88e9-af70976b21c3/tool-results/toolu_01Wo5JrRcouuTgZbvWVDHZXD.txt

Preview (first 2KB):
233:[Omitted long matching line]
239:\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
243:Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
261:For sample selection, additional samples increase the oracle upper bound (more draws raise the probability of a high-quality candidate), but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
267:These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
268:This reinforces the primary finding: even under the most favorable conditions (high baseline performance, more candidates, and aggregated multi-seed evidence), signal-based selection recovers only a fraction of the oracle headroom available.
381:44 & & Cross-dataset degeneracy--LP gain ($n{=}23$) & $0.810$ & $1.0$ &  \\
382:45 & & Per-type degeneracy--headroom (Few-NERD, Spearman) & $0.004$ & $0.180$ &  \\
383:46 & & Per-type degeneracy--headroom (exact permutation) & $0.005$ & $0.205$ &  \\
384:47 & & Per-type degeneracy--headroom ($\text{df}{=}4$ adjusted) & $0.033$ & $1.0$ &  \\
385:48 & & SciERC per-type degeneracy--LP ($\rho{=}0.14$) & $0.790$ & $1.0$ &  \\
432:\paragraph{Oracle-improvable fraction.}
433:[Omitted long matching line]
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c12a17a4-a7a1-45e6-99a8-e174800afdf2",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "fa021b81-d38c-4ab9-850f-cfb7c83d444d",
  "sourceToolAssistantUUID": "c12a17a4-a7a1-45e6-99a8-e174800afdf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-22T08:10:29.790Z_

Good! I can see relevant content about degeneracy and oracle. Let me search more specifically for RE extension content and read relevant sections of the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa021b81-d38c-4ab9-850f-cfb7c83d444d",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGWY3eZoxj9FeLf5ZAt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3a7f6f5f-a1b5-4838-9036-d0d8dff27a90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q9UUjUaiKgJscug3vWzQBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 39896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1104,
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

_source line 11 · 2026-05-22T08:10:30.522Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Pge4camH9vr6Kxha8cEBui`</summary>

```json
{
  "pattern": "(?i)(re\\s|relation.?extract|RE extension|re_)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a7f6f5f-a1b5-4838-9036-d0d8dff27a90",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGWY3eZoxj9FeLf5ZAt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "672f82e5-e5ab-4ec5-9c71-cb4c75af70d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q9UUjUaiKgJscug3vWzQBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 39896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1104,
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

_source line 12 · 2026-05-22T08:10:30.555Z_

<details><summary>↩ Tool result · `toolu_01Pge4camH9vr6Kxha8cEBui`</summary>

```text
16:$T$ & Sampling temperature \\
37:\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
41:& & NER $\rho$ & RE $\rho$ \\
69:\includegraphics[width=\columnwidth]{fig_temperature_robustness}
70:\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
71:\label{fig:temperature_robustness}
74:\paragraph{Temperature sensitivity.}
76:FK NER $\rho$ drops by 0.022, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
77:LP exhibits the largest temperature effect on NER ($\rho{=}0.249$ at $T{=}0.7$ vs.\ $0.205$ at $T{=}1.0$, $\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.
86:SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, structural and binary-agreement signals are the most robust to $N$.
87:At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), a more stable alternative at higher sample sizes.
97:For each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.
127:\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}
132:NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
139:\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
144:RE signal degradation is relation-specific.
146:The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives. This is a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
147:We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
152:For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$): longer, more relation-dense sentences provide richer structure for consistency-based estimation.
153:Both proxies are weakly correlated with F1 ($|r|{<}0.15$), they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
154:For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
155:On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$, all far above the full-set levels.
156:Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
171:Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$; the two selection rules are equivalent.
173:Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
200:On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
201:At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
202:EM ranks first across all four tested conditional configurations: SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$). This holds despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
203:On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
204:On the conditional set, where the model demonstrably produces varied outputs, exact agreement becomes the strongest quality signal.
205:The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
232:On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
234:On CoNLL, 48--87\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
239:\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
261:For sample selection, additional samples increase the oracle upper bound (more draws raise the probability of a high-quality candidate), but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
267:These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
268:This reinforces the primary finding: even under the most favorable conditions (high baseline performance, more candidates, and aggregated multi-seed evidence), signal-based selection recovers only a fraction of the oracle headroom available.
311:On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
317:Under this most conservative family, no core NER claim survives ($p_{\text{adj}}{=}0.055$ for Few-NERD LP selection and construction); only two peripheral tests reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).
318:We report per-family corrections in the main text (\S\ref{sec:prescriptive}); the global enumeration is provided here for transparency.
342:13 & & SciERC RE LP selection ($N{=}16$, 4B, Fisher) & $0.058$ & $1.0$ &  \\
343:14 & & SciERC RE VC selection ($N{=}16$, 4B, Fisher) & $0.973$ & $1.0$ &  \\
344:15 & & SciERC RE FK selection ($N{=}16$, 4B, Fisher) & $0.985$ & $1.0$ &  \\
345:16 & & SciERC RE SJ selection ($N{=}16$, 4B, Fisher) & $0.993$ & $1.0$ &  \\
346:17 & & SciERC RE EM selection ($N{=}16$, 4B, Fisher) & $0.999$ & $1.0$ &  \\
377:42 & & SciERC RE $\Delta\rho$ SJ$-$FK (full-set) & $0.530$ & $1.0$ &  \\
378:43 & & RE SJ $\rho$ Q1 vs Q4 sentence length (Fisher $z$) & $0.004$ & $0.180$ &  \\
396:55 & & RE LP selection reversal (free-form, 4-seed) & ${<}.001$ & $0.006$ & $\dagger$ \\
411:On CoNLL, diversity collapses: 59\% (Qwen) to 89\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 already exceeds 0.90.
433:[Omitted long matching line]
434:On CoNLL, only 4--9\% of instances are improvable, consistent with the ceiling effect.
442:Table~\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.
466:The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
470:On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
471:On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
472:The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
500:(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \cite{ratinov2009design};
511:Since all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.
516:Our negative results are specific to fine-tuned models with constrained decoding on structured IE. Several conditions outside our experimental scope could restore selection headroom.
517:(a)~Models with poor calibration or in-context learning setups (without fine-tuning) produce more diverse outputs, widening the gap between candidates that consistency signals can exploit.
518:(b)~Closed-source APIs where log-probabilities are unavailable make consistency signals the only viable selection mechanism; our structural signals (SJ, VC, FK, EM) provide quality estimation ($\rho$ up to 0.45) even without model-internal access.
520:(d)~Tasks where the model exhibits systematic overconfidence (e.g., hallucination-prone generation) may benefit from consensus filtering, as disagreement among samples would carry more discriminative signal than in our well-calibrated fine-tuned regime.
572:Yet higher correlation does not yield better selection: MLP selection F1 ($0.637$) falls below LP's ($0.650$), with gap closure turning negative ($-5.1$\% vs.\ $+4.8$\%; Table~\ref{tab:hidden_probe}).
573:The linear probe performs worse still ($\rho{=}0.179$, gap closure $-23.4$\%).
574:On Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\% vs.\ $12.3$\%).
575:A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\% vs.\ $55.8$\%); LP's bottleneck is not token aggregation.
576:Despite partial entity quality encoding in hidden representations (entity-level probe AUROC${=}0.63$\textendash$0.88$; \S\ref{sec:mechanistic}), the correlation-selection gap persists at the sample level: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\S\ref{sec:discussion}).
580:Table~\ref{tab:method_coverage} summarizes the experimental coverage of each entity-level method evaluated in this work. Individual methods were tested on subsets of the full dataset $\times$ model matrix; the collective coverage spans three NER datasets and two model families.
585:\caption{Experimental coverage of entity-level methods. \checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}
651:On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).
652:On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.
653:LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
669:\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
682:Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
722:\texttt{System:} You are an expert in Named Entity Recognition.\\
727:RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
741:Because all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\%$ of instances.
744:All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
745:Any LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \textit{rankings} unchanged.
748:CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
752:\section{Log-Probability Score Compression}\label{app:logprob_ties}
754:Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
756:At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
759:Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$); the subtask change does not affect compression.
760:For comparison, SJ has only 12.5\% tied instances at the same threshold; SJ's advantage over LP for selection is one of score resolution, not information content.
772:\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
788:As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability. LP carries information, but compression limits its exploitation.
868:CoNLL alignment is moderate ($\rho{\approx}0.51$), but the valid-instance fraction is low (38\% for Qwen, 11\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate.
874:\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\text{valid}}$: ${\geq}2$ distinct F1 values). Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates.}
939:Instance-level Spearman $\rho$ between the two rankings averages 0.85, with rankings diverging for 10.6\% of instances where token count coefficient of variation exceeds 0.10.
942:The divergence is driven by structured output length variation: sequences with more extracted entities are longer but not necessarily higher quality, and length normalization prevents this bias.
951:\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
970:The NER pattern shows two complementary failure modes rather than a monotonic relationship between consistency and selection gain:
973:\item \textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, and LP rankings produce inconsistent $\Delta$ signs across quartiles.
978:On CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), and $\Delta{=}0$ universally; this ceiling effect is even more extreme than SciERC Q4.
980:\section{Exploratory Extension to Relation Extraction}\label{app:re_extension}
982:We extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.
983:RE produces sets of (head, relation, tail) triples with partial overlap; 40\% of RE instances receive zero F1, and entity span errors account for 55.5\% of RE false negatives, a prerequisite failure that consistency signals cannot detect (\S\ref{app:additional}).
984:All RE results use Qwen3-8B unless noted; single-seed ($\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.
987:RE quality estimation is reported in Table~\ref{tab:multiseed} (3-seed means).

[Showing results with pagination = limit: 100]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "672f82e5-e5ab-4ec5-9c71-cb4c75af70d1",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "8938ab34-0a58-450a-8bf5-6cc5ee629cf5",
  "sourceToolAssistantUUID": "672f82e5-e5ab-4ec5-9c71-cb4c75af70d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T08:10:30.786Z_

<details open><summary>🔧 Tool call — Read · `toolu_018bG7goMfHkTYN7F7XEU5ci`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 200,
  "offset": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8938ab34-0a58-450a-8bf5-6cc5ee629cf5",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGWY3eZoxj9FeLf5ZAt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d940b667-8b9d-4c8b-ac3d-ffa4b26a832d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q9UUjUaiKgJscug3vWzQBk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 39896,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1104
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 303,
          "cache_read_input_tokens": 39896,
          "cache_creation_input_tokens": 1104,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1104,
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

_source line 14 · 2026-05-22T08:10:30.796Z_

<details><summary>↩ Tool result · `toolu_018bG7goMfHkTYN7F7XEU5ci`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
48	\quad LP & $T{=}0.7$ & 0.249 & --- \\
49	\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\
50	\midrule
51	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
52	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
53	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
54	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
55	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
56	\midrule
57	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
58	\quad SJ &  & $0.474{\pm}0.009$ & --- \\
59	\quad FK &  & $0.467{\pm}0.009$ & --- \\
60	\quad EM &  & $0.473{\pm}0.010$ & --- \\
61	\quad VC &  & $0.470{\pm}0.006$ & --- \\
62	\quad LP &  & $0.311{\pm}0.003$ & --- \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
70	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
71	\label{fig:temperature_robustness}
72	\end{figure}
73	
74	\paragraph{Temperature sensitivity.}
75	SJ NER $\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.
76	FK NER $\rho$ drops by 0.022, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
77	LP exhibits the largest temperature effect on NER ($\rho{=}0.249$ at $T{=}0.7$ vs.\ $0.205$ at $T{=}1.0$, $\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.
78	Across all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).
79	
80	\paragraph{Sample size scaling.}
81	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
82	The magnitude of $N$-scaling gains is setting-dependent (LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$), though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, structural and binary-agreement signals are the most robust to $N$.
87	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), a more stable alternative at higher sample sizes.
88	
89	\paragraph{Transfer across model families.}
90	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
91	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
92	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$),\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.474{\pm}0.009$ vs.\ LP $0.311{\pm}0.003$, $\Delta{=}{+}0.163$).
93	
94	\paragraph{FK independence: instance-level permutation test.}\label{app:fk_independence}
95	
96	To verify that Fleiss' $\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.
97	For each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}
103	\label{tab:fk_independence}
104	\resizebox{\columnwidth}{!}{
105	\begin{tabular}{lrcccc}
106	\toprule
107	Config & $n$ & FK mean & 95\% CI & $t$ & Split-half $r$ \\
108	\midrule
109	SciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\
110	CoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\
111	CoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\
112	\bottomrule
113	\end{tabular}
114	}
115	\end{table}
116	
117	Table~\ref{tab:fk_independence} reports the results.
118	All configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), FK captures genuine inter-sample agreement rather than chance label co-occurrence.
119	Split-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.
120	The higher FK means on CoNLL ($0.720$--$0.927$) vs.\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.
121	
122	\section{Calibration Analysis}\label{app:calibration}
123	
124	\begin{figure*}[t]
125	\centering
126	\includegraphics[width=\textwidth]{fig_reliability}
127	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}
128	\label{fig:reliability}
129	\end{figure*}
130	
131	Reliability diagrams use 10 equal-width bins.
132	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
133	
134	\section{Additional Analyses}\label{app:additional}
135	
136	\begin{figure*}[t]
137	\centering
138	\includegraphics[width=\textwidth]{fig_signal_heatmap}
139	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
140	\label{fig:signal_heatmap}
141	\end{figure*}
142	
143	\paragraph{Per-relation diagnostic.}
144	RE signal degradation is relation-specific.
145	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
146	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives. This is a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
147	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
148	
149	\paragraph{Capability stratification.}
150	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
151	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
152	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$): longer, more relation-dense sentences provide richer structure for consistency-based estimation.
153	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
154	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
155	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$, all far above the full-set levels.
156	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
157	
158	\paragraph{Length vs.\ log-probability.}
159	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
160	
161	\begin{figure}[t]
162	\centering
163	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
164	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
165	\label{fig:length_logprob_scatter}
166	\end{figure}
167	
168	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
169	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
170	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
171	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$; the two selection rules are equivalent.
172	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
173	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
174	Evaluation circularity is negligible.
175	
176	\paragraph{SJ normalizer robustness.}
177	Equation~\ref{eq:sj} uses $\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \cup g_j|$.
178	Table~\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\Delta\rho|{<}0.01$ in every case, the choice between max and union normalization does not affect conclusions.
179	
180	\begin{table}[h]
181	\centering
182	\small
183	\caption{SJ normalizer comparison (Spearman $\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\max(|g_i|,|g_j|)$; Union: $|g_i \cup g_j|$.}
184	\label{tab:sj_normalizer}
185	\begin{tabular}{@{}ll ccc@{}}
186	\toprule
187	Dataset & Model & $\rho$(max) & $\rho$(union) & $\Delta\rho$ \\
188	\midrule
189	CoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\
190	CoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\
191	CoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\
192	SciERC & Qwen3-8B & .360 & .365 & $-$.005 \\
193	SciERC & Qwen3-4B & .422 & .423 & $-$.001 \\
194	SciERC & LLaMA-8B & .363 & .372 & $-$.009 \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	\paragraph{Conditional filtering details.}
200	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d940b667-8b9d-4c8b-ac3d-ffa4b26a832d",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "162418a4-72f6-4fbe-8991-351745c550d3",
  "sourceToolAssistantUUID": "d940b667-8b9d-4c8b-ac3d-ffa4b26a832d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-22T08:10:33.455Z_

Perfect! I found extensive RE-related content. Let me search for more specific tables with the metrics you mentioned (degeneracy, MV delta, LP-best, oracle).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "162418a4-72f6-4fbe-8991-351745c550d3",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGWjnLr9wVH1bKJTza1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "408400e8-43c8-4962-8232-c8a44de33cff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018H9yHm9gQGWEwrGtrsvz9H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 12146,
      "cache_read_input_tokens": 41000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12146,
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

_source line 16 · 2026-05-22T08:10:34.918Z_

<details open><summary>🔧 Tool call — Grep · `toolu_019qyBoqTtmUeV7GG4itpP9R`</summary>

```json
{
  "pattern": "(?i)(table.*degener|tab:degener|MV delta|LP.*best|oracle.*headroom|re_extension)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "head_limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "408400e8-43c8-4962-8232-c8a44de33cff",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGWjnLr9wVH1bKJTza1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d8d2a9c5-ae50-4db0-8c1f-2b30a7a0264c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018H9yHm9gQGWEwrGtrsvz9H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 12146,
      "cache_read_input_tokens": 41000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12146,
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

_source line 17 · 2026-05-22T08:10:34.982Z_

<details><summary>↩ Tool result · `toolu_019qyBoqTtmUeV7GG4itpP9R`</summary>

```text
233:[Omitted long matching line]
267:These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
268:This reinforces the primary finding: even under the most favorable conditions (high baseline performance, more candidates, and aggregated multi-seed evidence), signal-based selection recovers only a fraction of the oracle headroom available.
433:[Omitted long matching line]
437:On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP, the only per-sample signal, achieves merely $+$0.8~pp.
438:LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.
442:Table~\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.
448:\label{tab:degeneracy}
466:The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
469:The breakpoint $\delta^*$, the minimum equivalence margin at which each signal passes TOST, ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
497:The oracle-headroom anchors above introduce circularity: $\delta$ is calibrated against the very quantity it contextualizes.
866:Table~\ref{tab:within_rho} reports median within-instance $\rho(\text{LP}, \text{F1})$ across datasets, computed over non-degenerate instances (those with ${\geq}2$ distinct F1 values across $N{=}8$ samples).
916:\caption{LP-best selection advantage over MV by LP range bucket on Few-NERD ($N{=}8$, seed${=}42$). Instances with LP range ${\geq}0.05$ show $3$--$6{\times}$ larger advantage.}
934:The LP-best advantage over MV shows a clear transition: compressed instances (LP range${<}0.05$) gain $+0.8$ to $+2.3$\,pp, while non-compressed instances gain $+3.6$ to $+5.8$\,pp (Table~\ref{tab:fewnerd_lp_bucket}).
951:\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
972:\item \textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp. Samples have already converged, leaving little room for any signal to improve selection.
980:\section{Exploratory Extension to Relation Extraction}\label{app:re_extension}
992:Table~\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.
997:Selection remains below single-sample on RE ($\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.
1008:Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
1036:Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
1131:Table~\ref{tab:bound_verification} verifies the bound across 16 configurations. All positive-gain configurations have $D < \theta_{\text{crit}}$ and actual/bound ratios of 3--12\% (Figure~\ref{fig:bound}). The bound is loose because $\alpha$ (signal alignment) is the bottleneck: the best signal recovers only 6.8\% of the non-degenerate oracle gap on average.
1298:The failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.0~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.
1410:Table~\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.
1411:Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+20.0$~pp at $N{=}32$).
1412:LP selection improves monotonically with $N$ ($+0.39$~pp at $N{=}8$ to $+0.95$~pp at $N{=}32$), but even at $N{=}32$, where degeneracy falls to 4\% and oracle headroom reaches ${\sim}20$~pp, the best signal captures less than 5\% of the available improvement.
1429:$N$ & Degen.\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\Delta$ \\
1446:The oracle gap ($+20.0$~pp, $p{<}0.001$) confirms substantial unrealized headroom.
1510:LP $\rho$ drops without fine-tuning (Table~\ref{tab:scale_comparison}) and LP selection fails on all 72B zero-shot datasets. Structural signals generalize better (Few-NERD VC $\rho{=}0.416$). Degeneracy increases at 72B (Few-NERD: $46.2$\% vs.\ $13.0$\%; CoNLL: $67.7$\% vs.\ $61.7$\%); the gap persists under this specific 72B zero-shot configuration, though scale, training regime, and quantization effects are confounded (see Limitations).
1517:Qwen2.5 exhibits systematically higher degeneracy than Qwen3 on Few-NERD (7B--72B: $31.7$--$46.2$\% vs.\ Qwen3-8B: $13.0$\%; Table~\ref{tab:scale_comparison}), confirming degeneracy is shaped by architecture rather than parameter count. Construction fails for all Qwen2.5 configurations on Few-NERD (both n.s.); 3$\to$5 epochs triples degeneracy within the same model (\S\ref{sec:fewnerd}).
1524:\caption{Scale ablation: Qwen3 8B vs.\ 4B QE $\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\ref{app:re_extension}.}
1538:Degeneracy scales with capability: 8B shows 12.2\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
1541:Qwen3-14B fine-tuned on Few-NERD achieves greedy F1${=}0.798$ ($+0.9$\,pp over 8B) with oracle headroom of 8.1\,pp ($+1.2$\,pp over 8B's 6.9\,pp) and $\rho$ advantage $+0.029$ over 8B.
1551:\caption{Pretrained vs.\ finetuned MV ($N{=}8$, $T{=}1.0$). Pretrained: Qwen2.5-7B-Instruct; finetuned: Qwen3-8B LoRA. MV: strict majority ($>N/2$). Capture: $\text{MV}\,\Delta / \text{oracle headroom}$. CoNLL pretrained single-seed; others 3-seed mean${\pm}\sigma$.}
1570:On CoNLL, MV captures $98$\% of oracle headroom for the pretrained model (greedy${=}0.536$, MV${=}0.628$, oracle${=}0.630$, degeneracy${=}36$\%) versus ${<}2$\% finetuned (greedy${=}0.912$, MV${=}0.912$, oracle${=}0.954$, degeneracy $57$--$60$\%).
1635:All four frontier families exhibit the correlation-selection gap (Table~\ref{tab:frontier_sc_cross}): MV recovers only a fraction of oracle headroom regardless of model capability.
1639:GPT-5.5 occupies the middle ground: 50\% degeneracy with 6.8\,pp unrealized oracle headroom.
1654:Table~\ref{tab:t_ablation} reports the effect of sampling temperature on QE signals, oracle headroom, and output quality across four temperatures on SciERC NER.
1675:Oracle headroom increases monotonically with temperature ($+9.1$~pp at $T{=}0.5$ to $+14.6$~pp at $T{=}1.2$), confirming that higher temperature consistently expands the oracle ceiling under constrained structured decoding.
1683:Table~\ref{tab:t_degeneracy} reports instance degeneracy (constant F1, gold-filtered) and median within-instance LP range across four temperatures on SciERC.
1687:This confirms that temperature modulates degeneracy but cannot improve LP-quality alignment, which is largely associated with task structure and remains relatively stable across generation configurations (\S\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\S\ref{sec:discussion}).
1793:\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}
1813:Despite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC, the strongest QE signal, yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.
1837:\multicolumn{3}{l}{Greedy: 0.748 \quad Oracle: 0.872} & \multicolumn{2}{l}{Headroom: 12.4\,pp} \\
1851:Table~\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.
1853:The correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\rho{=}{-}0.881$, $p{=}0.004$; exact permutation $p{=}0.005$); degeneracy directly constrains the headroom available for selection.
1917:At finer per-type granularity, selection depends on the interaction of degeneracy, oracle headroom, and type-specific LP-quality alignment.
1986:LP selection does not yield significant gains at any training duration ($-1.24$, $+0.64$, $+1.02$~pp; all below the ${\approx}$1.5~pp MDE), despite oracle headroom ranging from 8.4 to 15.0~pp.
2021:The non-tied subset analysis (Table~\ref{tab:nontied_main}) identifies within-instance LP range (max minus min LP across $N$ samples) as a per-instance degeneracy proxy: instances with near-zero LP range carry no discriminative signal.
2062:Table~\ref{tab:power_analysis} reports post-hoc power for the $n{=}23$ cross-dataset correlation between degeneracy and LP selection gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}).
2289:Report: (1)~degeneracy percentage, (2)~oracle headroom (oracle $-$ greedy), (3)~signal $\rho$ (cross-instance and within-instance), (4)~selection $\Delta$F1 with bootstrap $p$-values and effect sizes (Cohen's $d$), (5)~construction $\Delta$F1, (6)~selective prediction AUPRC and coverage--F1 curve.
2354:We validate the diagnostic cascade on Spider SQL parsing (GPT-5.5, $n{=}196$; \S\ref{sec:introduction}): degeneracy reaches 87.2\%, confirming the failure mode beyond NER. An RE extension on SciERC (Appendix~\ref{app:re_extension}) shows compound error propagation worsens all signals. The structural mismatch (set-valued outputs without equivalence classes) applies to any structured generation task.
2357:$+0.42$\,pp is the only unconditionally positive result among 9 method categories tested (Table~\ref{tab:method_summary}). Its significance ($p{<}0.001$, CI $[0.27, 0.58]$; \S\ref{sec:cross_model}) and theoretical motivation (architecturally distinct models produce independent error distributions, breaking within-model degeneracy) distinguish it from the null results of other categories.
2369:Each formal result has explicit empirical validation: Proposition~\ref{prop:construction_mbr} (MBR equivalence) $\to$ Table~\ref{tab:entity_construction}; Proposition~\ref{prop:entity_selection_bound} (entity selection bound) $\to$ Table~\ref{tab:alpha_crit} across 3 datasets; Degeneracy Decomposition $\to$ Figure~\ref{fig:bound} across 16 configurations (\S\ref{sec:theory}); oracle scaling law $\to$ Figure~\ref{fig:oracle_scaling} ($R^2 > 0.999$; \S\ref{sec:scaling}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8d2a9c5-ae50-4db0-8c1f-2b30a7a0264c",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "27a58e2f-16da-40d8-b4b6-16fa081ade5e",
  "sourceToolAssistantUUID": "d8d2a9c5-ae50-4db0-8c1f-2b30a7a0264c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T08:10:35.253Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DCrRna4nuZ1FTLxpq38TW5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 300,
  "offset": 980
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27a58e2f-16da-40d8-b4b6-16fa081ade5e",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGWjnLr9wVH1bKJTza1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "211b570b-9bb7-476c-842c-8b68c201c8d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018H9yHm9gQGWEwrGtrsvz9H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 12146,
      "cache_read_input_tokens": 41000,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12146
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 321,
          "cache_read_input_tokens": 41000,
          "cache_creation_input_tokens": 12146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12146,
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

_source line 19 · 2026-05-22T08:10:35.262Z_

<details><summary>↩ Tool result · `toolu_01DCrRna4nuZ1FTLxpq38TW5`</summary>

```text
980	\section{Exploratory Extension to Relation Extraction}\label{app:re_extension}
981	
982	We extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.
983	RE produces sets of (head, relation, tail) triples with partial overlap; 40\% of RE instances receive zero F1, and entity span errors account for 55.5\% of RE false negatives, a prerequisite failure that consistency signals cannot detect (\S\ref{app:additional}).
984	All RE results use Qwen3-8B unless noted; single-seed ($\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.
985	
986	\paragraph{Quality estimation.}
987	RE quality estimation is reported in Table~\ref{tab:multiseed} (3-seed means).
988	The signal ranking differs from NER: VC leads ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM, a reversal reflecting RE's higher sensitivity to per-sample scoring.
989	RE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\ref{fig:reliability}).
990	
991	\paragraph{Selection.}
992	Table~\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.
993	At $N{=}16$ (Qwen3-4B, Table~\ref{tab:re_n16_selection}), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.
994	
995	\paragraph{Scale ablation.}
996	At 4B scale (Qwen3-4B, $N{=}8$, $\text{seed}{=}42$), RE quality estimation shows FK $\rho{=}0.359$ and LP $\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\ $0.250$).
997	Selection remains below single-sample on RE ($\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.
998	
999	\paragraph{Free-form decoding.}
1000	RE LP selection consistently reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp across 4 seeds vs.\ $-0.9$~pp under constrained decoding at 8B; \S\ref{app:freeform_ablation}); constrained decoding's fixed template likely obscures LP signal in RE (\S\ref{app:mbr_discussion}).
1001	
1002	\subsection{RE Conditional Selection}\label{app:re_conditional_selection}
1003	
1004	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
1005	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
1006	All five signals underperform single-sample on both subsets.
1007	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
1008	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
1009	
1010	\begin{table}[t]
1011	\centering
1012	\small
1013	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
1014	\label{tab:re_cond_selection}
1015	\begin{tabular}{lcc}
1016	\toprule
1017	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
1018	\midrule
1019	Oracle & 0.585 & 0.757 \\
1020	\midrule
1021	LP & 0.395 & 0.600 \\
1022	SJ & 0.386 & 0.604 \\
1023	EM & 0.372 & 0.583 \\
1024	VC & 0.359 & 0.574 \\
1025	\midrule
1026	Greedy & 0.404 & 0.674 \\
1027	\bottomrule
1028	\end{tabular}
1029	\end{table}
1030	
1031	\subsection{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
1032	
1033	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
1034	All four consistency signals underperform single-sample, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
1035	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
1036	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
1037	This cross-task consistency (LP as the only viable selection signal on both NER and RE) reinforces the persistent limitation of instance-level signals for candidate ranking across tested regimes.
1038	
1039	\begin{table}[t]
1040	\centering
1041	\small
1042	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
1043	\label{tab:re_n16_selection}
1044	\begin{tabular}{lccc}
1045	\toprule
1046	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
1047	\midrule
1048	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
1049	\midrule
1050	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
1051	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
1052	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
1053	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
1054	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
1055	\midrule
1056	Greedy & $.291{\pm}.000$ & --- & --- \\
1057	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
1058	\bottomrule
1059	\end{tabular}
1060	\end{table}
1061	
1062	\section{Theoretical Results}\label{app:mbr_discussion}
1063	
1064	\subsection{MBR Framework and Proof}\label{app:mbr_proof}
1065	
1066	Entity-level construction (\S\ref{sec:prescriptive}) is a special case of minimum Bayes risk (MBR) decoding \cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\arg\max_{y \in \{y_1,\ldots,y_N\}}$) to construction over all subsets of $E_\cup{=}\bigcup_i y_i$.
1067	
1068	\begin{proposition}[Entity construction as MBR for balanced set-overlap]\label{prop:construction_mbr}
1069	Under entity-wise independence with utility $u(\hat{y}, y') = |\hat{y} \cap y'| - \alpha|\hat{y} \setminus y'|$ ($\alpha \geq 1$), the MBR-optimal constructed set is
1070	\begin{equation}\label{eq:mbr_construction}
1071	\hat{y}_{\textup{MBR}} \!=\! \bigl\{e \!{\in}\! E_\cup \!:\! \hat{p}(e) \!>\! \tfrac{\alpha}{\alpha{+}1}\bigr\},\; \hat{p}(e) \!=\! \tfrac{1}{N} \textstyle\sum\nolimits_{i} \mathbf{1}[e \!{\in}\! y_i]
1072	\end{equation}
1073	The special case $\alpha{=}1$ yields $\hat{p}(e) > \tfrac{1}{2}$, the majority-vote threshold.
1074	\end{proposition}
1075	
1076	\noindent\textbf{Remark.}
1077	Set-level F1 is non-linear and admits no closed-form threshold rule \cite{dembczynski2011exact}. We use balanced linear utility ($\alpha{=}1$ throughout); balanced set-overlap and F1 induce similar optimal thresholds for typical NER output sizes ($|E_\cup| \leq 30$).
1078	
1079	\paragraph{Proof.}
1080	We show that under entity-wise independence, the MBR-optimal constructed set with utility $u(\hat{y}, y') = |\hat{y} \cap y'| - \alpha|\hat{y} \setminus y'|$ ($\alpha \geq 1$) includes entity $e$ iff $\hat{p}(e) > \alpha/(\alpha+1)$.
1081	Consider constructing $\hat{y} \subseteq E_\cup$ to maximize expected utility against the empirical sample distribution.
1082	Under entity-wise independence, each entity inclusion is an independent binary decision.
1083	For entity $e$ with empirical frequency $\hat{p}(e) = \frac{1}{N} \sum_i \mathbf{1}[e \in y_i]$, including $e$ contributes $+1$ when $e \in y_i$ (probability $\hat{p}(e)$) and $-\alpha$ when $e \notin y_i$ (probability $1{-}\hat{p}(e)$).
1084	The expected marginal contribution is $\hat{p}(e) - \alpha(1{-}\hat{p}(e)) = (1{+}\alpha)\hat{p}(e) - \alpha$, which is positive iff $\hat{p}(e) > \alpha/(\alpha+1)$.
1085	The special case $\alpha{=}1$ yields the majority-vote threshold $\hat{p}(e) > 1/2$ used throughout.
1086	With F1 utility, the optimal threshold depends on the full probability vector over $E_\cup$ \cite{dembczynski2011exact}; the constant $1/2$ threshold is a close approximation when $|E_\cup|$ is small (typically 5--15 in our experiments).
1087	The independence assumption is approximate; we verify empirically that strict majority vote fails to improve over greedy (\S\ref{sec:prescriptive}; Table~\ref{tab:alpha_crit}), consistent with marginal-entity precision falling below $\alpha_{\textup{crit}}$.
1088	
1089	\subsection{Connection to MBR Decoding}\label{app:mbr_connection}
1090	
1091	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
1092	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.
1093	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
1094	
1095	\paragraph{Task-specific decoding interactions.}
1096	The free-form ablation shows divergent behavior across tasks.
1097	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is attributable to selective variance reallocation ($p{<}0.0001$).
1098	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
1099	This interaction does not generalize to NER, where selection remains negligible under both regimes.
1100	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
1101	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472: 87 instances newly gain LP discrimination while others lose it, and the newly non-tied subset shows a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
1102	Despite this reshuffling, aggregate NER selection gains remain negligible. Score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
1103	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
1104	
1105	\subsection{Degeneracy Decomposition}\label{app:bound_proof}
1106	
1107	\begin{definition}[Instance-Level Degeneracy]
1108	Given model $\mathcal{M}$, input $x$, and $N$ i.i.d.\ samples $\{y_1, \ldots, y_N\}$, instance $x$ is \emph{degenerate} if $y_1 = \cdots = y_N$. The degeneracy rate is $D = |\mathcal{D}|^{-1} \sum_{x} \mathbb{1}[y_1(x) = \cdots = y_N(x)]$.
1109	\end{definition}
1110	
1111	\begin{definition}[Non-Degenerate Oracle Gap]
1112	$G_{\text{nd}} = \mathbb{E}[F_1^{\text{oracle}}(x) - F_1^{\text{greedy}}(x) \mid x \in \mathcal{D}_{\neg D}]$, where $\mathcal{D}_{\neg D}$ is the set of non-degenerate instances.
1113	\end{definition}
1114	
1115	\subsection{Proof of the Degeneracy Decomposition}
1116	
1117	Partition $\mathcal{D}$ into degenerate ($\mathcal{D}_D$, fraction $D$) and non-degenerate ($\mathcal{D}_{\neg D}$, fraction $1{-}D$). By total expectation:
1118	\begin{equation}\label{eq:bound_decomp}
1119	\mathbb{E}[\Delta F_1(A)] = D \cdot \mathbb{E}[\Delta F_1 \mid \mathcal{D}_D] + (1{-}D) \cdot \mathbb{E}[\Delta F_1 \mid \mathcal{D}_{\neg D}].
1120	\end{equation}
1121	For degenerate instances, all $N$ samples are identical and equal the greedy output, so $\Delta F_1 = 0$. For non-degenerate instances, $\Delta F_1(A,x) \leq F_1^{\text{oracle}}(x) - F_1^{\text{greedy}}(x)$, giving $\mathbb{E}[\Delta F_1 \mid \mathcal{D}_{\neg D}] \leq G_{\text{nd}}$. Substituting: $\mathbb{E}[\Delta F_1(A)] \leq (1{-}D) \cdot G_{\text{nd}}$.
1122	
1123	For signal-based methods, define alignment $\alpha = \mathbb{E}[\Delta F_1(A_s) \mid \mathcal{D}_{\neg D}] / G_{\text{nd}} \in [0,1]$. Direct substitution yields $\mathbb{E}[\Delta F_1(A_s)] = (1{-}D) \cdot G_{\text{nd}} \cdot \alpha$.
1124	
1125	\begin{corollary}[Critical Degeneracy Threshold]\label{cor:theta_crit}
1126	For SC gain to exceed significance threshold $\varepsilon$, the degeneracy rate must satisfy $D < 1 - \varepsilon / (G_{\text{nd}} \cdot \alpha) \stackrel{\text{def}}{=} \theta_{\text{crit}}$.
1127	With $\varepsilon{=}0.3$\,pp, $G_{\text{nd}}{=}14.8$\,pp, $\alpha{=}0.068$: $\theta_{\text{crit}} = 1 - 0.3/(14.8 \times 0.068) = 0.70$.
1128	\end{corollary}
1129	
1130	\paragraph{Numerical verification.}
1131	Table~\ref{tab:bound_verification} verifies the bound across 16 configurations. All positive-gain configurations have $D < \theta_{\text{crit}}$ and actual/bound ratios of 3--12\% (Figure~\ref{fig:bound}). The bound is loose because $\alpha$ (signal alignment) is the bottleneck: the best signal recovers only 6.8\% of the non-degenerate oracle gap on average.
1132	
1133	\begin{figure}[t]
1134	\centering
1135	\includegraphics[width=\columnwidth]{fig_bound}
1136	\caption{SC gain vs.\ degeneracy across 16 configurations (SciERC-specific $\alpha$). Red: signal-adjusted bound ($\alpha{=}0.068$); vertical dashed: $\theta_{\text{crit}}{=}0.70$; horizontal dotted: $\varepsilon{=}0.3$\,pp. All positive gains fall within the bound (right panel: ratio to weak bound, all ${<}0.13$).}
1137	\label{fig:bound}
1138	\end{figure}
1139	
1140	\begin{table}[t]
1141	\centering
1142	\small
1143	\caption{Bound verification across representative configurations ($N{=}8$). $G_{\text{nd}}$: non-degenerate oracle gap. $\alpha$: signal alignment. Bound: $(1{-}D) \cdot G_{\text{nd}} \cdot \alpha$. Ratio: actual$/$weak bound.}
1144	\label{tab:bound_verification}
1145	\begin{tabular}{@{}lccccr@{}}
1146	\toprule
1147	Config & $D$ & $G_{\text{nd}}$ & $\alpha$ & $\Delta$ & Ratio \\
1148	\midrule
1149	Q3-8B FT FN s123 & .131 & 14.8 & .121 & +1.56 & 12.1\% \\
1150	Q3-8B FT FN s456 & .120 & 14.5 & .108 & +1.37 & 10.8\% \\
1151	Q3-8B FT Sci s789 & .214 & 17.0 & .084 & +1.12 & 8.4\% \\
1152	72B ZS Sci & .210 & 18.9 & .102 & +1.53 & 10.2\% \\
1153	Q3-8B FT CoN s123 & .630 & 10.9 & .000 & $-$0.42 & --- \\
1154	72B ZS CoN & .677 & 16.4 & .000 & $-$0.37 & --- \\
1155	72B FS CoN & .700 & 17.0 & .047 & +0.24 & 4.7\% \\
1156	\bottomrule
1157	\end{tabular}
1158	\end{table}
1159	
1160	\subsection{Entity Selection Bound: Proof and Validation}\label{app:alpha_crit}
1161	
1162	\begin{proof}[Proof of Proposition~\ref{prop:entity_selection_bound}]
1163	\textbf{Part (a).} On a degenerate instance, all $N$ samples produce the same entity set: $\textup{entities}(y_1) = \cdots = \textup{entities}(y_N)$. For every entity $e \in E_\cup$, the agreement count satisfies $k(e) = N$ (if $e$ appears) or $k(e) = 0$ (if not). Hence $k(e)/N \in \{0,1\}$, and the majority-vote threshold $k(e)/N \geq 1/2$ selects exactly the entities present in any single sample---identical to the greedy output. Thus $\hat{y}_{\textup{MV}} = \hat{y}_{\textup{gr}}$ and $\Delta F_1 = 0$.
1164	
1165	\textbf{Part (b).} Partition instances into degenerate (fraction $\delta$) and non-degenerate (fraction $1{-}\delta$). By the law of total expectation:
1166	\[
1167	\mathbb{E}[\Delta F_1] = \delta \cdot \underbrace{\mathbb{E}[\Delta F_1 \mid \textup{deg.}]}_{= 0 \;\textup{by (a)}} + (1{-}\delta) \cdot \mathbb{E}[\Delta F_1 \mid \textup{non-deg.}].
1168	\]
1169	
1170	\textbf{Part (c).} Assume $\mathcal{M}^- = \hat{y}_{\textup{gr}} \setminus \hat{y}_{\textup{MV}} \approx \varnothing$ (greedy entities typically have agreement $k(e)/N \approx 1$). Let $m = |\mathcal{M}^+|$ and $\pi = |\mathcal{M}^+ \cap G|/|\mathcal{M}^+|$ denote the number and precision of entities added by MV. Define $S = |\hat{y}_{\textup{gr}}| + |G|$. Then:
1171	\begin{align*}
1172	\Delta F_1 &= \frac{2(\textup{TP}_{\textup{gr}} + m\pi)}{S + m} - \frac{2\,\textup{TP}_{\textup{gr}}}{S} \\
1173	&= \frac{2m\bigl(\pi - \textup{TP}_{\textup{gr}}/S\bigr)}{S + m}
1174	= \frac{2m\bigl(\pi - F_1^{\textup{gr}}/2\bigr)}{S + m},
1175	\end{align*}
1176	which is positive if and only if $\pi > F_1^{\textup{gr}}/2 \triangleq \alpha_{\textup{crit}}$.
1177	
1178	When $\mathcal{M}^-$ is non-empty, the condition generalizes: the net precision across the full symmetric difference $\hat{y}_{\textup{MV}} \triangle \hat{y}_{\textup{gr}}$ must exceed a corresponding threshold. The addition-only case covers the dominant empirical regime, as greedy entities typically achieve near-unanimous agreement.
1179	\end{proof}
1180	
1181	\paragraph{Effective precision threshold.}
1182	From parts (b) and (c), MV gain is attenuated by $(1{-}\delta)$ and requires marginal-entity precision $> \alpha_{\textup{crit}}$.
1183	Equivalently, defining $\alpha_{\textup{crit,eff}} {=} \alpha_{\textup{crit}} / (1{-}\delta)$, MV gain requires marginal-entity precision $> \alpha_{\textup{crit,eff}}$; when $\alpha_{\textup{crit,eff}} > 1$, the required precision exceeds 1.0 and MV gain is structurally impossible regardless of entity quality.
1184	
1185	\paragraph{Empirical validation.}
1186	Table~\ref{tab:alpha_crit} reports MV performance under strict majority (count $> N/2$) using the MF4v2 pipeline (3-seed means).
1187	MV fails to improve F1 on any dataset: Few-NERD $\Delta{=}{-}2.74$\,pp, SciERC $-0.74$\,pp, CoNLL $-0.04$\,pp.
1188	We define the effective precision threshold $\alpha_{\textup{crit,eff}} {=} \alpha_{\textup{crit}} / (1{-}\delta)$; when $\alpha_{\textup{crit,eff}} > 1$, the required marginal-entity precision exceeds 1.0, making MV gain structurally impossible.
1189	CoNLL ($\alpha_{\textup{crit,eff}}{=}1.148$) confirms this: $\Delta{=}{-}0.04{\pm}0.15$\,pp is indistinguishable from zero.
1190	Few-NERD and SciERC ($\alpha_{\textup{crit,eff}} {<} 1$) show significantly negative $\Delta$, indicating that even where structural headroom exists, marginal-entity precision is insufficient.
1191	SciERC's lower $\alpha_{\textup{crit}}$ ($0.334$, vs.\ $0.396$ for Few-NERD and $0.456$ for CoNLL) is consistent with it being the only dataset where a trained entity verifier (AUC${=}0.923$) achieves positive gain ($+1.28$\,pp).
1192	
1193	\begin{table}[h]
1194	\centering\small
1195	\caption{MV performance under strict majority (count $> N/2$; Qwen3-8B FT, $N{=}8$, $T{=}1.0$, 3-seed mean${\pm}\sigma$). $\alpha_{\textup{crit}} = F_1^{\textup{gr}}/2$; $\alpha_{\textup{crit,eff}} = \alpha_{\textup{crit}} / (1{-}\delta)$. When $\alpha_{\textup{crit,eff}} > 1$, MV gain is structurally impossible.}
1196	\label{tab:alpha_crit}
1197	\resizebox{\columnwidth}{!}{%
1198	\begin{tabular}{@{}lccccccccc@{}}
1199	\toprule
1200	Dataset & Seeds & Greedy & MV & Oracle & $\Delta_{\textup{SC}}$ (pp) & $\delta$ & $\alpha_{\textup{crit}}$ & $\alpha_{\textup{crit,eff}}$ & Prediction \\
1201	\midrule
1202	Few-NERD & 3 & .791 & .764 & .885 & $-2.74{\pm}0.54$ & 8.8\% & 0.396 & 0.434 & $\Delta < 0$ \\
1203	CoNLL & 3 & .912 & .912 & .950 & $-0.04{\pm}0.15$ & 60.3\% & 0.456 & 1.148 & $\Delta \approx 0$ \\
1204	SciERC & 3 & .667 & .660 & .781 & $-0.74{\pm}0.57$ & 12.2\% & 0.334 & 0.380 & $\Delta < 0$ \\
1205	\bottomrule
1206	\end{tabular}}
1207	\end{table}
1208	
1209	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
1210	
1211	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).
1212	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
1213	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
1214	RE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\ $-0.68$~pp constrained.
1215	The constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.
1216	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
1217	
1218	\begin{table*}[t]
1219	\centering
1220	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
1221	\label{tab:freeform_ablation}
1222	
1223	\vspace{2pt}
1224	{\small\textsc{Panel A: Logprob Distribution}}
1225	\vspace{2pt}
1226	
1227	\begin{tabular}{lccc}
1228	\toprule
1229	Metric & Constrained & Free-form & $\Delta$ \\
1230	\midrule
1231	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
1232	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
1233	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
1234	\bottomrule
1235	\end{tabular}
1236	
1237	\vspace{8pt}
1238	
1239	{\small\textsc{Panel B: Selection F1}}
1240	\vspace{2pt}
1241	
1242	\begin{tabular}{llccc}
1243	\toprule
1244	Task & Method & Constrained & Free-form & $\Delta$ \\
1245	\midrule
1246	\multirow{3}{*}{NER}
1247	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
1248	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
1249	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
1250	\midrule
1251	\multirow{3}{*}{RE}
1252	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
1253	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
1254	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
1255	\bottomrule
1256	\end{tabular}
1257	
1258	\vspace{8pt}
1259	
1260	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
1261	\vspace{2pt}
1262	
1263	\begin{tabular}{l ccc ccc}
1264	\toprule
1265	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
1266	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
1267	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
1268	\midrule
1269	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
1270	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
1271	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
1272	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
1273	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
1274	\bottomrule
1275	\end{tabular}
1276	
1277	\vspace{8pt}
1278	
1279	{\small\textsc{Panel D: Parse Rate (Free-form)}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "211b570b-9bb7-476c-842c-8b68c201c8d8",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "ae985592-2404-4ad6-9974-178bdfdd9ff4",
  "sourceToolAssistantUUID": "211b570b-9bb7-476c-842c-8b68c201c8d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-22T08:10:37.030Z_

Now let me search for the specific tables with degeneracy, MV delta, LP-best, and oracle numbers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae985592-2404-4ad6-9974-178bdfdd9ff4",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGX4vXaCoWqwCvHagDw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8de69746-d718-4797-8afd-262fcb2dcde8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019xfDVGLchFCHtAKD43rzfo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13750,
      "cache_read_input_tokens": 53146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13750,
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

_source line 21 · 2026-05-22T08:10:38.329Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vz9iPwGJebE4pEaCv8uV2E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 150,
  "offset": 440
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8de69746-d718-4797-8afd-262fcb2dcde8",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGX4vXaCoWqwCvHagDw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ce64f6f-d5b1-4c95-af7d-bee6b5f742c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019xfDVGLchFCHtAKD43rzfo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13750,
      "cache_read_input_tokens": 53146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13750,
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

_source line 22 · 2026-05-22T08:10:38.351Z_

<details><summary>↩ Tool result · `toolu_01Vz9iPwGJebE4pEaCv8uV2E`</summary>

```text
440	
441	\paragraph{Instance degeneracy statistics.}
442	Table~\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.
443	
444	\begin{table}[t]
445	\centering
446	\small
447	\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
448	\label{tab:degeneracy}
449	\resizebox{\columnwidth}{!}{
450	\begin{tabular}{lccc}
451	\toprule
452	& \shortstack{SciERC 8B\\($N{=}8$)} & \shortstack{SciERC 4B\\($N{=}8$)} & \shortstack{CoNLL 8B\\($N{=}8$)} \\
453	\midrule
454	Constant F1 & 12.2\% & 10.4\% & 61.7\% \\
455	Constant utility & 13\% & 7.0\% & 64\% \\
456	Oracle gap closed (non-deg.) & 23\% & 25.2\% & 36\% \\
457	Within-inst.\ SJ $\rho$ (median) & 0.524 & 0.550 & 0.990 \\
458	\bottomrule
459	\end{tabular}
460	}
461	\end{table}
462	
463	\paragraph{TOST equivalence testing.}\label{app:tost}
464	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
465	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
466	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
467	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
468	We address this below with externally anchored equivalence margins.
469	The breakpoint $\delta^*$, the minimum equivalence margin at which each signal passes TOST, ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
470	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
471	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
472	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
473	
474	\begin{table}[t]
475	\centering
476	\small
477	\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).}
478	\label{tab:tost}
479	\resizebox{\columnwidth}{!}{
480	\begin{tabular}{l cccc cccc}
481	\toprule
482	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
483	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
484	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
485	\midrule
486	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
487	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
488	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
489	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
490	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
491	\bottomrule
492	\end{tabular}
493	}
494	\end{table}
495	
496	\paragraph{External equivalence margins.}
497	The oracle-headroom anchors above introduce circularity: $\delta$ is calibrated against the very quantity it contextualizes.
498	To resolve this, we supplement with three externally grounded margins:
499	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), which represents measurement noise;
500	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \cite{ratinov2009design};
501	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
502	
503	Results under these external anchors diverge sharply by configuration.
504	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
505	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, which exceeds even $\delta_{\mathrm{literature}}$.
506	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
507	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
508	
509	\paragraph{Multiple comparison considerations.}\label{app:multiple_comparisons}
510	Our primary selection analysis involves ${\sim}$20 comparisons (5 signals $\times$ 3--4 configurations).
511	Since all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.
512	The sole positive finding, the non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}), survives Bonferroni correction over the 5 signal comparisons ($p_{\mathrm{adj}}{=}0.020 < 0.05$). However, the $\varepsilon{=}0.05$ threshold is selected post-hoc from a 7-point sweep (Appendix~\ref{app:epsilon_robustness}); joint correction across thresholds and signals yields $p_{\mathrm{adj}}{=}0.14$, so this finding is exploratory.
513	For quality estimation signal rankings, differences between the top signals (e.g., VC vs.\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.
514	
515	\paragraph{When would consistency-based selection work?}\label{app:when_selection_works}
516	Our negative results are specific to fine-tuned models with constrained decoding on structured IE. Several conditions outside our experimental scope could restore selection headroom.
517	(a)~Models with poor calibration or in-context learning setups (without fine-tuning) produce more diverse outputs, widening the gap between candidates that consistency signals can exploit.
518	(b)~Closed-source APIs where log-probabilities are unavailable make consistency signals the only viable selection mechanism; our structural signals (SJ, VC, FK, EM) provide quality estimation ($\rho$ up to 0.45) even without model-internal access.
519	(c)~Ensemble or mixture-of-experts settings generate structurally diverse candidates by design, reducing instance degeneracy below the levels observed in our single-model sampling.
520	(d)~Tasks where the model exhibits systematic overconfidence (e.g., hallucination-prone generation) may benefit from consensus filtering, as disagreement among samples would carry more discriminative signal than in our well-calibrated fine-tuned regime.
521	
522	\section{Supervised and Model-Internal Signal Analysis}\label{app:supervised_combination}
523	
524	\subsection{Supervised Signal Combination}
525	
526	Supervised classifiers (logistic regression, MLP, random forest) trained on all five signals (5-fold CV, 3-seed mean, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy (F1${=}0.644$; LR: $-0.4$~pp; MLP: $-1.6$~pp; RF: $-3.1$~pp).
527	Adding pairwise interaction features does not help (AUROC 0.634 vs.\ 0.638).
528	To test whether richer representations could close the gap, we train a DeBERTa-v3-base verifier that encodes input-output pairs and predicts per-sample F1.
529	DeBERTa achieves $\rho{=}0.329{\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\pm}26.5$\% of the oracle gap (13 of 15 runs negative; vs.\ LP's $+4.2{\pm}10.7$\%); on Few-NERD, DeBERTa recovers only $+3.5$\% (single 80/20 split; vs.\ LP's $+16.3$\%).
530	Cross-dataset transfer fails entirely ($-27$\% to $-72$\% gap closure).
531	Grid-search ensemble optimization over signal weights confirms LP dominance: across configurations, LP receives mean weight $0.78$, while FK and SJ receive zero weight; VC and EM serve only as secondary regularizers.
532	Neither handcrafted signal combinations nor learned text representations close the selection gap; only model-internal log-probability provides meaningful selection signal, consistent with an information asymmetry between the generating model and external observers.
533	
534	\subsection{Entity-Level Verifier Transfer}\label{app:verifier_transfer}
535	
536	A LightGBM entity-level verifier (5 features: agreement count, VC, LP, SJ, FK) achieves AUC${=}0.923{\pm}0.002$ under out-of-fold evaluation, confirming that entity correctness is learnable from the available signals.
537	In-domain OOF construction yields $+0.30$\,pp overall, with per-dataset gains of $+1.28$\,pp (SciERC), $+0.55$\,pp (CoNLL), and $+0.02$\,pp (Few-NERD).
538	The near-zero Few-NERD gain despite high AUC shows that frequency-based threshold construction already captures most of the verifier's signal.
539	Cross-dataset transfer to Few-NERD is negative: $-0.76$\,pp (B2-v2), $-1.02$\,pp (B2-v3), $-1.27$\,pp (B2-v4 Replace, AUC${=}0.822$), and $-0.85$\,pp (B2-v4 Augment, AUC${=}0.855$), all below greedy.
540	The learned feature--correctness mapping is dataset-specific: entity agreement patterns that predict correctness on scientific text do not transfer to fine-grained entity types.
541	
542	\subsection{Hidden State Probes}\label{app:hidden_probe}
543	
544	Entity-level probes confirm that quality information is partially encoded in hidden representations (AUROC${=}0.63$\textendash$0.88$, dataset-dependent; \S\ref{sec:mechanistic}); we test whether this translates to sample-level selection gain by training probes on the generating model's hidden states.
545	
546	\paragraph{Setup.}
547	Unlike the entity-level probe in \S\ref{sec:mechanistic} (which classifies individual entities on FewNERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.
548	For each of $N{=}8$ samples per instance, we extract the mean-pooled final-layer hidden state ($d{=}4096$) from the generating Qwen3-8B model and train a linear probe and a two-layer MLP (hidden dim${=}256$) to predict per-sample F1 (5-fold CV, 3 seeds).
549	Entity-level probes use dataset-specific generation temperatures ($T{=}0.5$ for Few-NERD, $T{=}0.8$ for CoNLL, $T{=}1.0$ for SciERC).
550	
551	\begin{table}[t]
552	\centering
553	\small
554	\caption{Hidden state probes vs.\ LP for sample selection (5-fold CV ${\times}$ 3 seeds). $\rho$: Spearman correlation with per-sample F1. Sel.\ F1: selection F1. Gap\%: oracle gap closure. SciERC greedy${=}0.644$ (seed 42), oracle${=}0.775$ (seed 42).}
555	\label{tab:hidden_probe}
556	\resizebox{\columnwidth}{!}{%
557	\begin{tabular}{@{}l ccc cc@{}}
558	\toprule
559	& \multicolumn{3}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{Few-NERD}} \\
560	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
561	Method & $\rho$ & Sel.\ F1 & Gap\% & $\rho$ & Gap\% \\
562	\midrule
563	LP & .283 & $\mathbf{.650}$ & $+$4.8 & .606 & 12.3 \\
564	Hidden Linear & $.179{\pm}.019$ & $.613{\pm}.002$ & $-$23.4 & \multicolumn{2}{c}{---} \\
565	Hidden MLP & $\mathbf{.388{\pm}.013}$ & $.637{\pm}.003$ & $-$5.1 & $\mathbf{.629{\pm}.007}$ & 11.7 \\
566	\bottomrule
567	\end{tabular}}
568	\end{table}
569	
570	\paragraph{Cross-dataset asymmetry.}
571	On SciERC, the MLP probe achieves higher quality correlation than LP ($\rho{=}0.388$ vs.\ $0.283$, $+37$\%); hidden states encode information beyond what LP captures.
572	Yet higher correlation does not yield better selection: MLP selection F1 ($0.637$) falls below LP's ($0.650$), with gap closure turning negative ($-5.1$\% vs.\ $+4.8$\%; Table~\ref{tab:hidden_probe}).
573	The linear probe performs worse still ($\rho{=}0.179$, gap closure $-23.4$\%).
574	On Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\% vs.\ $12.3$\%).
575	A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\% vs.\ $55.8$\%); LP's bottleneck is not token aggregation.
576	Despite partial entity quality encoding in hidden representations (entity-level probe AUROC${=}0.63$\textendash$0.88$; \S\ref{sec:mechanistic}), the correlation-selection gap persists at the sample level: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\S\ref{sec:discussion}).
577	
578	\subsection{Method Coverage Matrix}\label{app:method_coverage}
579	
580	Table~\ref{tab:method_coverage} summarizes the experimental coverage of each entity-level method evaluated in this work. Individual methods were tested on subsets of the full dataset $\times$ model matrix; the collective coverage spans three NER datasets and two model families.
581	
582	\begin{table}[h]
583	\centering
584	\small
585	\caption{Experimental coverage of entity-level methods. \checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}
586	\label{tab:method_coverage}
587	\begin{tabular}{lccccl}
588	\toprule
589	Method & SciERC & Few-NERD & CoNLL & Qwen & LLaMA \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ce64f6f-d5b1-4c95-af7d-bee6b5f742c6",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "b1c59f58-3e71-4915-af79-854037adf34c",
  "sourceToolAssistantUUID": "5ce64f6f-d5b1-4c95-af7d-bee6b5f742c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T08:10:39.156Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Rni7YJ62UTVteKNurKz93h`</summary>

```json
{
  "pattern": "\\\\begin\\{table\\}.*Degeneracy|tab.*degener|Constant F1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "head_limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1c59f58-3e71-4915-af79-854037adf34c",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGX4vXaCoWqwCvHagDw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c192d2c-3e58-4f49-940f-3eea48c8c2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019xfDVGLchFCHtAKD43rzfo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13750,
      "cache_read_input_tokens": 53146,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13750
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 302,
          "cache_read_input_tokens": 53146,
          "cache_creation_input_tokens": 13750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13750,
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

_source line 24 · 2026-05-22T08:10:39.226Z_

<details><summary>↩ Tool result · `toolu_01Rni7YJ62UTVteKNurKz93h`</summary>

```text
233:[Omitted long matching line]
442:Table~\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.
447:\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
448:\label{tab:degeneracy}
454:Constant F1 & 12.2\% & 10.4\% & 61.7\% \\
866:Table~\ref{tab:within_rho} reports median within-instance $\rho(\text{LP}, \text{F1})$ across datasets, computed over non-degenerate instances (those with ${\geq}2$ distinct F1 values across $N{=}8$ samples).
1131:Table~\ref{tab:bound_verification} verifies the bound across 16 configurations. All positive-gain configurations have $D < \theta_{\text{crit}}$ and actual/bound ratios of 3--12\% (Figure~\ref{fig:bound}). The bound is loose because $\alpha$ (signal alignment) is the bottleneck: the best signal recovers only 6.8\% of the non-degenerate oracle gap on average.
1410:Table~\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.
1517:Qwen2.5 exhibits systematically higher degeneracy than Qwen3 on Few-NERD (7B--72B: $31.7$--$46.2$\% vs.\ Qwen3-8B: $13.0$\%; Table~\ref{tab:scale_comparison}), confirming degeneracy is shaped by architecture rather than parameter count. Construction fails for all Qwen2.5 configurations on Few-NERD (both n.s.); 3$\to$5 epochs triples degeneracy within the same model (\S\ref{sec:fewnerd}).
1538:Degeneracy scales with capability: 8B shows 12.2\% vs.\ 4B's 10.4\% on SciERC (Table~\ref{tab:degeneracy}).
1683:Table~\ref{tab:t_degeneracy} reports instance degeneracy (constant F1, gold-filtered) and median within-instance LP range across four temperatures on SciERC.
1687:This confirms that temperature modulates degeneracy but cannot improve LP-quality alignment, which is largely associated with task structure and remains relatively stable across generation configurations (\S\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\S\ref{sec:discussion}).
1693:\label{tab:t_degeneracy}
1851:Table~\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.
2021:The non-tied subset analysis (Table~\ref{tab:nontied_main}) identifies within-instance LP range (max minus min LP across $N$ samples) as a per-instance degeneracy proxy: instances with near-zero LP range carry no discriminative signal.
2062:Table~\ref{tab:power_analysis} reports post-hoc power for the $n{=}23$ cross-dataset correlation between degeneracy and LP selection gain ($\rho{=}0.052$, $p{=}0.81$; Figure~\ref{fig:degeneracy_scatter}).
2357:$+0.42$\,pp is the only unconditionally positive result among 9 method categories tested (Table~\ref{tab:method_summary}). Its significance ($p{<}0.001$, CI $[0.27, 0.58]$; \S\ref{sec:cross_model}) and theoretical motivation (architecturally distinct models produce independent error distributions, breaking within-model degeneracy) distinguish it from the null results of other categories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c192d2c-3e58-4f49-940f-3eea48c8c2ae",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "18e7ca10-8271-44d3-9431-eb118a38c75c",
  "sourceToolAssistantUUID": "9c192d2c-3e58-4f49-940f-3eea48c8c2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-22T08:10:41.085Z_

Perfect! Now let me search for tables with RE degeneracy data and LP-best metrics more specifically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18e7ca10-8271-44d3-9431-eb118a38c75c",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGXMwxmr7XvVyZyvG5T",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3dc977e5-360d-4eb2-972f-46e829d6d8c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017YMTehRUb6vy7dLJba7Dcd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6413,
      "cache_read_input_tokens": 66896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6413,
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

_source line 26 · 2026-05-22T08:10:42.146Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GodSvDkyodA9sCU7Hojihs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 200,
  "offset": 1680
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dc977e5-360d-4eb2-972f-46e829d6d8c9",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGXMwxmr7XvVyZyvG5T",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6d13d0e5-7fa0-4d2b-a71a-f96f826b7e08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017YMTehRUb6vy7dLJba7Dcd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6413,
      "cache_read_input_tokens": 66896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6413,
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

_source line 27 · 2026-05-22T08:10:42.195Z_

<details><summary>↩ Tool result · `toolu_01GodSvDkyodA9sCU7Hojihs`</summary>

```text
1680	The $T{=}0.7$ and $T{=}1.0$ comparison in Table~\ref{tab:robustness} is consistent with the trends reported here.
1681	
1682	\paragraph{Temperature modulates degeneracy and LP spread.}
1683	Table~\ref{tab:t_degeneracy} reports instance degeneracy (constant F1, gold-filtered) and median within-instance LP range across four temperatures on SciERC.
1684	Both quantities are strictly monotonic in $T$: degeneracy falls from 41.4\% ($T{=}0.5$) to 14.9\% ($T{=}1.2$), while LP range increases from 0.015 to 0.058 nats.
1685	Temperature thus provides a direct lever for practitioners to shift the degeneracy regime.
1686	However, even at $T{=}1.2$ where degeneracy (14.9\%) approaches Few-NERD levels (${\sim}$13\%), within-instance $\rho(\text{LP}, \text{F1})$ remains at 0.225, far below Few-NERD's ${\sim}$0.5.
1687	This confirms that temperature modulates degeneracy but cannot improve LP-quality alignment, which is largely associated with task structure and remains relatively stable across generation configurations (\S\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\S\ref{sec:discussion}).
1688	
1689	\begin{table}[h]
1690	\centering
1691	\small
1692	\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}
1693	\label{tab:t_degeneracy}
1694	\resizebox{\columnwidth}{!}{
1695	\begin{tabular}{ccccc}
1696	\toprule
1697	$T$ & Degen.\% & LP range (nats) & Fleiss' $\kappa$ & SJ mean \\
1698	\midrule
1699	0.5 & 41.4 & 0.015 & 0.572 & 0.830 \\
1700	0.8 & 23.8 & 0.031 & 0.471 & 0.752 \\
1701	1.0 & 17.8 & 0.042 & 0.405 & 0.700 \\
1702	1.2 & 14.9 & 0.058 & 0.352 & 0.647 \\
1703	\bottomrule
1704	\end{tabular}
1705	}
1706	\end{table}
1707	
1708	\section{Cross-Dataset OOD Analysis}\label{app:ood}
1709	
1710	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
1711	
1712	\begin{table}[t]
1713	\centering
1714	\small
1715	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
1716	\label{tab:ood}
1717	\resizebox{\columnwidth}{!}{
1718	\begin{tabular}{l ccc ccc}
1719	\toprule
1720	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
1721	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
1722	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
1723	\midrule
1724	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
1725	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
1726	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
1727	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
1728	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
1729	\bottomrule
1730	\end{tabular}
1731	}
1732	\end{table}
1733	
1734	\paragraph{Wider-to-narrower schema transfer.}
1735	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
1736	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
1737	
1738	\paragraph{Narrower-to-wider schema transfer (excluded).}
1739	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
1740	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (single-sample NER F1${=}0.009$, RE F1${=}0.001$).
1741	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
1742	These negative correlations reflect the model systematically generating confident but incorrect outputs, a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}) and not evidence against signal utility.
1743	
1744	\paragraph{Asymmetry interpretation.}
1745	The directional asymmetry is attributable to schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
1746	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
1747	
1748	\section{Verbalized Confidence}\label{app:verbalized_confidence}
1749	
1750	We evaluate verbalized confidence (VerbConf) as a second per-sample signal following \citet{lin2022teaching} and \citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.
1751	Table~\ref{tab:verbconf} reports quality estimation and selection results.
1752	
1753	\begin{table}[t]
1754	\centering
1755	\small
1756	\caption{Verbalized confidence (VerbConf) vs.\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}
1757	\label{tab:verbconf}
1758	\resizebox{\columnwidth}{!}{
1759	\begin{tabular}{l cc cc}
1760	\toprule
1761	 & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{CoNLL NER}} \\
1762	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
1763	Metric & VerbConf & LP & VerbConf & LP \\
1764	\midrule
1765	$\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\
1766	AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\
1767	Selection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\
1768	$\Delta$ vs.\ greedy & $-$2.45\,pp & $+$0.2\,pp & $-$1.93\,pp & $-$0.77\,pp \\
1769	\midrule
1770	Mean score & 8.58\,/\,10 & --- & 9.24\,/\,10 & --- \\
1771	Parse fail rate & 0.26\% & --- & 0\% & --- \\
1772	\bottomrule
1773	\end{tabular}
1774	}
1775	\end{table}
1776	
1777	\paragraph{Severe overconfidence.}
1778	VerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.
1779	This compression is more severe than LP (which spans a 0.041-nat median range); score compression is a general property of model self-assessment, not an artifact of log-probability computation.
1780	
1781	\paragraph{QE--selection decoupling.}
1782	VerbConf achieves higher $\rho$ than LP on both datasets (SciERC: 0.297 vs.\ 0.205; CoNLL: 0.337 vs.\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\ 0.578; CoNLL: 0.747 vs.\ 0.753), yet yields the worst selection among all signals ($\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).
1783	This dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.
1784	The AUROC--$\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\rho$ at 0.337) reflects differing sensitivity to binary vs.\ ordinal discrimination.
1785	
1786	\section{LLaMA-3.2-3B Scale Ablation}\label{app:llama3b}
1787	
1788	To extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\ref{tab:llama3b}).
1789	
1790	\begin{table}[t]
1791	\centering
1792	\small
1793	\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}
1794	\label{tab:llama3b}
1795	\begin{tabular}{l cc cc}
1796	\toprule
1797	Signal & $\rho$ & AUROC & Sel.\ F1 & $\Delta$ vs.\ greedy \\
1798	\midrule
1799	VC & \textbf{.460} & .743 & 0.611 & $-$1.54\,pp \\
1800	SJ & .375 & .738 & \textbf{0.633} & $+$0.61\,pp \\
1801	EM & .334 & \textbf{.776} & --- & --- \\
1802	FK & .268 & .671 & 0.630 & $+$0.28\,pp \\
1803	LP & .266 & .633 & 0.628 & $+$0.12\,pp \\
1804	\midrule
1805	Greedy & --- & --- & 0.627 & --- \\
1806	Oracle & --- & --- & 0.763 & --- \\
1807	\bottomrule
1808	\end{tabular}
1809	\end{table}
1810	
1811	The $\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\ref{tab:quality_estimation}); ranking stability holds across two model families spanning 3B--8B.
1812	AUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), consistent with the $\rho$--AUROC dissociation noted in the main text.
1813	Despite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC, the strongest QE signal, yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.
1814	
1815	\section{Few-NERD Full Results}\label{app:fewnerd}
1816	
1817	Table~\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).
1818	After gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\% receive zero F1 under greedy decoding.
1819	Instance degeneracy is 13.0\% (vs.\ 12.2\% on SciERC, 61.7\% on CoNLL).
1820	
1821	\begin{table}[t]
1822	\centering
1823	\small
1824	\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\ $\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\% confidence interval.}
1825	\label{tab:fewnerd_full}
1826	\resizebox{\columnwidth}{!}{
1827	\begin{tabular}{lcccc}
1828	\toprule
1829	Signal & $\rho$ & Sample AUROC & Sel.\ $\Delta$ & 95\% CI \\
1830	\midrule
1831	LP & .220 & .578 & $\mathbf{+1.39}$\,pp & [+1.18, +1.53] \\
1832	VC & .386 & --- & $-$1.79\,pp & --- \\
1833	FK & .313 & --- & $-$2.26\,pp & --- \\
1834	SJ & .300 & --- & $-$2.14\,pp & --- \\
1835	EM & .287 & --- & $-$3.85\,pp & --- \\
1836	\midrule
1837	\multicolumn{3}{l}{Greedy: 0.748 \quad Oracle: 0.872} & \multicolumn{2}{l}{Headroom: 12.4\,pp} \\
1838	\bottomrule
1839	\end{tabular}
1840	}
1841	\end{table}
1842	
1843	\paragraph{Key observations.}
1844	(1)~All five signals achieve positive QE ($\rho$ 0.22--0.39); quality estimation works on Few-NERD. VC leads ($\rho{=}0.39$), followed by FK ($0.31$), SJ ($0.30$), EM ($0.29$), LP ($0.22$); the ranking matches SciERC where structural signals also outperform LP for quality estimation.
1845	(2)~LP is the only signal achieving significant positive selection ($+1.39$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.
1846	(3)~Despite positive $\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.
1847	(4)~Low degeneracy (13.0\%) combined with strong LP-quality alignment ($\rho{\approx}0.5$--$0.7$) enables LP selection: candidates differ in F1 more often, and LP can rank them effectively. This contrasts with SciERC (12.2\% degeneracy but weak alignment $\rho{\approx}0.16$, LP $+0.61$~pp) and CoNLL (61.7\%, LP $-0.85$~pp).
1848	
1849	\section{Per-Entity-Type LP Selection Analysis}\label{app:per_type_lp}
1850	
1851	Table~\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.
1852	The degeneracy-gating mechanism holds at entity-type granularity: 7 of 8 types show positive LP selection gains, and the sole negative type (Art, $-0.17$~pp) has the highest degeneracy (19.8\%).
1853	The correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\rho{=}{-}0.881$, $p{=}0.004$; exact permutation $p{=}0.005$); degeneracy directly constrains the headroom available for selection.
1854	Under a conservative $\text{df}{=}4$ adjustment for within-type dependence, the correlation remains significant ($p{=}0.033$).
1855	Entity types show near-zero intra-class correlation (ICC $= -0.004$), supporting the independence assumption underlying per-type analysis.
1856	
1857	\begin{table}[h]
1858	\centering
1859	\small
1860	\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\Delta$; Art (highest degeneracy) is the sole exception.}
1861	\label{tab:per_type_lp}
1862	\resizebox{\columnwidth}{!}{
1863	\begin{tabular}{lrrrrrrr}
1864	\toprule
1865	Entity Type & $n$ & Degen.\% & Greedy & LP Sel & $\Delta$ (pp) & LP $\rho$ & Headroom \\
1866	\midrule
1867	Event & 1{,}306 & 6.0 & .655 & .662 & $+$0.65 & .457 & 16.1\,pp \\
1868	Other & 3{,}433 & 6.6 & .637 & .685 & $\mathbf{+4.73}$ & .491 & 19.4\,pp \\
1869	Organization & 6{,}647 & 6.7 & .720 & .732 & $+$1.21 & .509 & 13.3\,pp \\
1870	Building & 1{,}587 & 7.2 & .702 & .705 & $+$0.23 & .478 & 14.9\,pp \\
1871	Product & 2{,}276 & 8.2 & .656 & .677 & $+$2.01 & .483 & 15.8\,pp \\
1872	Location & 8{,}023 & 11.4 & .793 & .798 & $+$0.53 & .520 & 10.3\,pp \\
1873	Person & 8{,}016 & 13.4 & .822 & .835 & $+$1.25 & .544 & 9.2\,pp \\
1874	Art & 1{,}277 & 19.8 & .756 & .754 & $-$0.17 & .451 & 9.2\,pp \\
1875	\bottomrule
1876	\end{tabular}
1877	}
1878	\end{table}
1879	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d13d0e5-7fa0-4d2b-a71a-f96f826b7e08",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "ad8dad0c-137a-4529-936b-0bfcccc5aac0",
  "sourceToolAssistantUUID": "6d13d0e5-7fa0-4d2b-a71a-f96f826b7e08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T08:10:42.546Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xv1ScqW3pGrfMbtH8nLfTX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 100,
  "offset": 1400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad8dad0c-137a-4529-936b-0bfcccc5aac0",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGXMwxmr7XvVyZyvG5T",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "282ae7a4-c9de-4d67-800d-fceb90c92ba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017YMTehRUb6vy7dLJba7Dcd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6413,
      "cache_read_input_tokens": 66896,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 260,
          "cache_read_input_tokens": 66896,
          "cache_creation_input_tokens": 6413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6413,
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

_source line 29 · 2026-05-22T08:10:42.585Z_

<details><summary>↩ Tool result · `toolu_01Xv1ScqW3pGrfMbtH8nLfTX`</summary>

```text
1400	\midrule
1401	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
1402	\bottomrule
1403	\end{tabular}
1404	\end{table}
1405	
1406	Signal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.
1407	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER); additional samples stabilize structural signals more than LP.
1408	
1409	\paragraph{$N$-scaling: selection headroom vs.\ selection gain.}
1410	Table~\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.
1411	Oracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+20.0$~pp at $N{=}32$).
1412	LP selection improves monotonically with $N$ ($+0.39$~pp at $N{=}8$ to $+0.95$~pp at $N{=}32$), but even at $N{=}32$, where degeneracy falls to 4\% and oracle headroom reaches ${\sim}20$~pp, the best signal captures less than 5\% of the available improvement.
1413	Degeneracy drops monotonically (43\% at $N{=}2$ to 4\% at $N{=}32$), yet reduced degeneracy does not unlock selection, consistent with the LoRA-rank ablation finding (\S\ref{sec:robustness_main}).
1414	VC selection degrades with increasing $N$ ($-2.66$~pp at $N{=}2$ to $-4.35$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.
1415	
1416	\paragraph{Few-NERD $N$-scaling: MV at $N{=}16$.}
1417	On Few-NERD (Qwen3-8B, 3-seed), increasing from $N{=}8$ to $N{=}16$ reduces degeneracy ($8.8$\%$\to$$4.0{\pm}1.4$\%) and attenuates MV degradation ($-2.74$\,pp$\to$$-1.65{\pm}0.61$\,pp), but MV remains negative.
1418	Additional samples reduce the MV penalty but do not reverse it, consistent with the correlated-error mechanism: more samples provide better frequency estimates but cannot overcome systematic shared mistakes.
1419	SJ $\rho$ is used for quality estimation at $N{=}16$ (FK conditional $\rho$ shows sign instability across seeds: mean${=}0.051{\pm}0.062$).
1420	
1421	\begin{table}[t]
1422	\centering
1423	\small
1424	\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\_025).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
1425	\label{tab:n_scaling_selection}
1426	\resizebox{\columnwidth}{!}{
1427	\begin{tabular}{ccccccccc}
1428	\toprule
1429	$N$ & Degen.\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\Delta$ \\
1430	\midrule
1431	2 & 42.7\% & $+$4.4 & $-$0.89 & $-$2.72 & $-$2.72 & $-$2.72 & $-$2.66 & $-$0.89 \\
1432	4 & 21.0\% & $+$10.2 & $+$0.03 & $-$0.31 & $-$0.40 & $-$0.74 & $-$2.16 & $+$0.03 \\
1433	8 & 11.0\% & $+$14.5 & $+$0.39 & $+$0.20 & $+$0.15 & $-$0.77 & $-$2.87 & $+$0.39 \\
1434	16 & 7.4\% & $+$17.7 & $+$0.78 & $+$0.24 & $-$0.02 & $-$0.06 & $-$3.95 & $+$0.78 \\
1435	32 & 4.0\% & $+$20.0 & $+$0.95 & $+$0.35 & $+$0.65 & $+$0.22 & $-$4.35 & $+$0.95 \\
1436	\bottomrule
1437	\end{tabular}
1438	}
1439	\end{table}
1440	\footnotetext{$N$-scaling analysis uses gold-filtered evaluation ($n{=}529$, greedy F1${=}0.640$, seed 42). Values differ from Table~\ref{tab:selection} (0.645, 2-seed) and Table~\ref{tab:fewnerd} (0.667, 3-seed) due to seed and aggregation differences; relative trends are consistent.}
1441	
1442	\paragraph{Bootstrap significance at $N{=}32$.}
1443	Table~\ref{tab:bootstrap_n32} reports bootstrap confidence intervals and $p$-values for selection at $N{=}32$ ($B{=}10{,}000$, $n{=}529$).
1444	No signal achieves significant improvement over greedy at $\alpha{=}0.05$ (LP: $p{=}0.091$; FK: $p{=}0.101$), while VC is significantly \textit{worse} ($-4.36$~pp, $p{=}1.0$).
1445	However, all signals except VC significantly outperform random selection ($p{<}0.001$, permutation test); the signals carry meaningful quality information yet fail to translate it into reliable selection gains.
1446	The oracle gap ($+20.0$~pp, $p{<}0.001$) confirms substantial unrealized headroom.
1447	
1448	\begin{table}[t]
1449	\centering
1450	\small
1451	\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\Delta$: selection gain vs.\ greedy. CI: 95\% bootstrap percentile interval. $p_{\text{greedy}}$: one-sided $p$-value vs.\ greedy; $p_{\text{rand}}$: permutation test vs.\ random selection.}
1452	\label{tab:bootstrap_n32}
1453	\resizebox{\columnwidth}{!}{
1454	\begin{tabular}{lcccc}
1455	\toprule
1456	Signal & $\Delta$ (pp) & 95\% CI & $p_{\text{greedy}}$ & $p_{\text{rand}}$ \\
1457	\midrule
1458	LP & $+$0.95 & [$-$0.41, $+$2.34] & 0.091 & ${<}$0.001 \\
1459	FK & $+$0.66 & [$-$0.36, $+$1.67] & 0.101 & ${<}$0.001 \\
1460	SJ & $+$0.36 & [$-$0.66, $+$1.38] & 0.244 & ${<}$0.001 \\
1461	EM & $+$0.22 & [$-$0.99, $+$1.44] & 0.355 & ${<}$0.001 \\
1462	VC & $-$4.36 & [$-$6.26, $-$2.37] & 1.000 & 0.741 \\
1463	\midrule
1464	Oracle & $+$20.00 & [$+$17.98, $+$22.10] & ${<}$0.001 & --- \\
1465	\bottomrule
1466	\end{tabular}
1467	}
1468	\end{table}
1469	
1470	\paragraph{Oracle ceiling scaling law.}
1471	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$, with $R^2 > 0.999$ across all model--dataset fits (Figure~\ref{fig:oracle_scaling}).
1472	The exponent $c$ varies with dataset complexity: FewNERD ($c{\approx}0.61$) scales comparably to reasoning-task estimates ($c{\approx}0.5$--$0.7$; \citealp{brown2024monkeys}), while SciERC converges more slowly ($c{\approx}0.35$), consistent with complex IE producing less marginal diversity per additional sample.
1473	CoNLL's narrow headroom ($b{=}0.04$--$0.10$) makes $c$ unreliable (inter-model variance $2.5{\times}$); we report only $a$ and $b$ for CoNLL.
1474	A single stochastic sample ($N{=}1$, $T{=}1.0$) underperforms greedy by 1--3\,pp because sampling noise outweighs diversity; $N{\geq}4$ is needed to match greedy.
1475	
1476	\begin{figure}[t]
1477	\centering
1478	\includegraphics[width=\columnwidth]{figures/fig_oracle_scaling.pdf}
1479	\caption{Oracle $F_1$ as a function of sample count $N$, fitted with $F_1(N) = a - b \cdot N^{-c}$. All fits $R^2 > 0.999$. Horizontal dashed lines: greedy ($T{=}0$) F1. The ceiling grows monotonically with $N$, but the correlation-selection gap (\S\ref{sec:selection_gap}) limits how much is actually recoverable.}
1480	\label{fig:oracle_scaling}
1481	\end{figure}
1482	
1483	\section{Cross-Scale and Cross-Family Comparison}\label{app:cross_scale}
1484	
1485	\begin{table}[t]
1486	\centering
1487	\small
1488	\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%). $^\star$Qwen2.5; unmarked: Qwen3. $^\dagger$Not computed. $^\ddagger$200-instance subset; 10.1\% parse failures excluded.}
1489	\label{tab:scale_comparison}
1490	\resizebox{\columnwidth}{!}{%
1491	\begin{tabular}{@{}llccccccc@{}}
1492	\toprule
1493	Dataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\
1494	\midrule
1495	SciERC & 8B FT  & .667 & 11.4 & 12.2 & .326 & .324 & .177 & .159 \\
1496	       & 72B ZS$^\star$ & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\
1497	\midrule
1498	Few-NERD & 7B FT$^\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\
1499	         & 8B FT & .748 & 12.4 & 13.0 & .386 & .300 & .313 & .220 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "282ae7a4-c9de-4d67-800d-fceb90c92ba8",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "06db8dcf-b73b-43ca-96d7-33c1bf66eb34",
  "sourceToolAssistantUUID": "282ae7a4-c9de-4d67-800d-fceb90c92ba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-22T08:10:44.747Z_

Excellent! Now let me get the complete RE selection table and search for any more specific RE degeneracy data:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06db8dcf-b73b-43ca-96d7-33c1bf66eb34",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGXcDCkXvbMZXttgxbo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe7ab474-9de3-4d8e-80b2-f9924092a148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018gJmY7G6qYXtNCdBYcoKru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9743,
      "cache_read_input_tokens": 73309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9743,
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

_source line 31 · 2026-05-22T08:10:45.813Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G1KRKK3gMCTZ17F4Xk1nQh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 120,
  "offset": 1010
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe7ab474-9de3-4d8e-80b2-f9924092a148",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGXcDCkXvbMZXttgxbo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b21e842d-00cf-450e-ab98-3d01ac7576fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018gJmY7G6qYXtNCdBYcoKru",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9743,
      "cache_read_input_tokens": 73309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9743,
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

_source line 32 · 2026-05-22T08:10:45.873Z_

<details><summary>↩ Tool result · `toolu_01G1KRKK3gMCTZ17F4Xk1nQh`</summary>

```text
1010	\begin{table}[t]
1011	\centering
1012	\small
1013	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
1014	\label{tab:re_cond_selection}
1015	\begin{tabular}{lcc}
1016	\toprule
1017	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
1018	\midrule
1019	Oracle & 0.585 & 0.757 \\
1020	\midrule
1021	LP & 0.395 & 0.600 \\
1022	SJ & 0.386 & 0.604 \\
1023	EM & 0.372 & 0.583 \\
1024	VC & 0.359 & 0.574 \\
1025	\midrule
1026	Greedy & 0.404 & 0.674 \\
1027	\bottomrule
1028	\end{tabular}
1029	\end{table}
1030	
1031	\subsection{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
1032	
1033	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
1034	All four consistency signals underperform single-sample, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
1035	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
1036	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
1037	This cross-task consistency (LP as the only viable selection signal on both NER and RE) reinforces the persistent limitation of instance-level signals for candidate ranking across tested regimes.
1038	
1039	\begin{table}[t]
1040	\centering
1041	\small
1042	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
1043	\label{tab:re_n16_selection}
1044	\begin{tabular}{lccc}
1045	\toprule
1046	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
1047	\midrule
1048	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
1049	\midrule
1050	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
1051	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
1052	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
1053	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
1054	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
1055	\midrule
1056	Greedy & $.291{\pm}.000$ & --- & --- \\
1057	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
1058	\bottomrule
1059	\end{tabular}
1060	\end{table}
1061	
1062	\section{Theoretical Results}\label{app:mbr_discussion}
1063	
1064	\subsection{MBR Framework and Proof}\label{app:mbr_proof}
1065	
1066	Entity-level construction (\S\ref{sec:prescriptive}) is a special case of minimum Bayes risk (MBR) decoding \cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\arg\max_{y \in \{y_1,\ldots,y_N\}}$) to construction over all subsets of $E_\cup{=}\bigcup_i y_i$.
1067	
1068	\begin{proposition}[Entity construction as MBR for balanced set-overlap]\label{prop:construction_mbr}
1069	Under entity-wise independence with utility $u(\hat{y}, y') = |\hat{y} \cap y'| - \alpha|\hat{y} \setminus y'|$ ($\alpha \geq 1$), the MBR-optimal constructed set is
1070	\begin{equation}\label{eq:mbr_construction}
1071	\hat{y}_{\textup{MBR}} \!=\! \bigl\{e \!{\in}\! E_\cup \!:\! \hat{p}(e) \!>\! \tfrac{\alpha}{\alpha{+}1}\bigr\},\; \hat{p}(e) \!=\! \tfrac{1}{N} \textstyle\sum\nolimits_{i} \mathbf{1}[e \!{\in}\! y_i]
1072	\end{equation}
1073	The special case $\alpha{=}1$ yields $\hat{p}(e) > \tfrac{1}{2}$, the majority-vote threshold.
1074	\end{proposition}
1075	
1076	\noindent\textbf{Remark.}
1077	Set-level F1 is non-linear and admits no closed-form threshold rule \cite{dembczynski2011exact}. We use balanced linear utility ($\alpha{=}1$ throughout); balanced set-overlap and F1 induce similar optimal thresholds for typical NER output sizes ($|E_\cup| \leq 30$).
1078	
1079	\paragraph{Proof.}
1080	We show that under entity-wise independence, the MBR-optimal constructed set with utility $u(\hat{y}, y') = |\hat{y} \cap y'| - \alpha|\hat{y} \setminus y'|$ ($\alpha \geq 1$) includes entity $e$ iff $\hat{p}(e) > \alpha/(\alpha+1)$.
1081	Consider constructing $\hat{y} \subseteq E_\cup$ to maximize expected utility against the empirical sample distribution.
1082	Under entity-wise independence, each entity inclusion is an independent binary decision.
1083	For entity $e$ with empirical frequency $\hat{p}(e) = \frac{1}{N} \sum_i \mathbf{1}[e \in y_i]$, including $e$ contributes $+1$ when $e \in y_i$ (probability $\hat{p}(e)$) and $-\alpha$ when $e \notin y_i$ (probability $1{-}\hat{p}(e)$).
1084	The expected marginal contribution is $\hat{p}(e) - \alpha(1{-}\hat{p}(e)) = (1{+}\alpha)\hat{p}(e) - \alpha$, which is positive iff $\hat{p}(e) > \alpha/(\alpha+1)$.
1085	The special case $\alpha{=}1$ yields the majority-vote threshold $\hat{p}(e) > 1/2$ used throughout.
1086	With F1 utility, the optimal threshold depends on the full probability vector over $E_\cup$ \cite{dembczynski2011exact}; the constant $1/2$ threshold is a close approximation when $|E_\cup|$ is small (typically 5--15 in our experiments).
1087	The independence assumption is approximate; we verify empirically that strict majority vote fails to improve over greedy (\S\ref{sec:prescriptive}; Table~\ref{tab:alpha_crit}), consistent with marginal-entity precision falling below $\alpha_{\textup{crit}}$.
1088	
1089	\subsection{Connection to MBR Decoding}\label{app:mbr_connection}
1090	
1091	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
1092	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.
1093	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
1094	
1095	\paragraph{Task-specific decoding interactions.}
1096	The free-form ablation shows divergent behavior across tasks.
1097	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is attributable to selective variance reallocation ($p{<}0.0001$).
1098	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
1099	This interaction does not generalize to NER, where selection remains negligible under both regimes.
1100	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
1101	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472: 87 instances newly gain LP discrimination while others lose it, and the newly non-tied subset shows a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
1102	Despite this reshuffling, aggregate NER selection gains remain negligible. Score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
1103	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
1104	
1105	\subsection{Degeneracy Decomposition}\label{app:bound_proof}
1106	
1107	\begin{definition}[Instance-Level Degeneracy]
1108	Given model $\mathcal{M}$, input $x$, and $N$ i.i.d.\ samples $\{y_1, \ldots, y_N\}$, instance $x$ is \emph{degenerate} if $y_1 = \cdots = y_N$. The degeneracy rate is $D = |\mathcal{D}|^{-1} \sum_{x} \mathbb{1}[y_1(x) = \cdots = y_N(x)]$.
1109	\end{definition}
1110	
1111	\begin{definition}[Non-Degenerate Oracle Gap]
1112	$G_{\text{nd}} = \mathbb{E}[F_1^{\text{oracle}}(x) - F_1^{\text{greedy}}(x) \mid x \in \mathcal{D}_{\neg D}]$, where $\mathcal{D}_{\neg D}$ is the set of non-degenerate instances.
1113	\end{definition}
1114	
1115	\subsection{Proof of the Degeneracy Decomposition}
1116	
1117	Partition $\mathcal{D}$ into degenerate ($\mathcal{D}_D$, fraction $D$) and non-degenerate ($\mathcal{D}_{\neg D}$, fraction $1{-}D$). By total expectation:
1118	\begin{equation}\label{eq:bound_decomp}
1119	\mathbb{E}[\Delta F_1(A)] = D \cdot \mathbb{E}[\Delta F_1 \mid \mathcal{D}_D] + (1{-}D) \cdot \mathbb{E}[\Delta F_1 \mid \mathcal{D}_{\neg D}].
1120	\end{equation}
1121	For degenerate instances, all $N$ samples are identical and equal the greedy output, so $\Delta F_1 = 0$. For non-degenerate instances, $\Delta F_1(A,x) \leq F_1^{\text{oracle}}(x) - F_1^{\text{greedy}}(x)$, giving $\mathbb{E}[\Delta F_1 \mid \mathcal{D}_{\neg D}] \leq G_{\text{nd}}$. Substituting: $\mathbb{E}[\Delta F_1(A)] \leq (1{-}D) \cdot G_{\text{nd}}$.
1122	
1123	For signal-based methods, define alignment $\alpha = \mathbb{E}[\Delta F_1(A_s) \mid \mathcal{D}_{\neg D}] / G_{\text{nd}} \in [0,1]$. Direct substitution yields $\mathbb{E}[\Delta F_1(A_s)] = (1{-}D) \cdot G_{\text{nd}} \cdot \alpha$.
1124	
1125	\begin{corollary}[Critical Degeneracy Threshold]\label{cor:theta_crit}
1126	For SC gain to exceed significance threshold $\varepsilon$, the degeneracy rate must satisfy $D < 1 - \varepsilon / (G_{\text{nd}} \cdot \alpha) \stackrel{\text{def}}{=} \theta_{\text{crit}}$.
1127	With $\varepsilon{=}0.3$\,pp, $G_{\text{nd}}{=}14.8$\,pp, $\alpha{=}0.068$: $\theta_{\text{crit}} = 1 - 0.3/(14.8 \times 0.068) = 0.70$.
1128	\end{corollary}
1129	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b21e842d-00cf-450e-ab98-3d01ac7576fb",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "a7089b8a-62b6-4289-83f8-0fb7f5924671",
  "sourceToolAssistantUUID": "b21e842d-00cf-450e-ab98-3d01ac7576fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T08:10:46.538Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JPZYNPKPjVHgHisZQQawcj`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\caption.*RE\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7089b8a-62b6-4289-83f8-0fb7f5924671",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGXcDCkXvbMZXttgxbo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "62fb7ffd-189f-419b-a1de-62c407223ed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018gJmY7G6qYXtNCdBYcoKru",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9743,
      "cache_read_input_tokens": 73309,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9743
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 240,
          "cache_read_input_tokens": 73309,
          "cache_creation_input_tokens": 9743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9743,
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

_source line 34 · 2026-05-22T08:10:47.126Z_

<details><summary>↩ Tool result · `toolu_01JPZYNPKPjVHgHisZQQawcj`</summary>

```text
70:\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
127:\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}
139:\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
164:\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
658:\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
1013:\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
1042:\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
1220:\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
1316:\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}
1524:\caption{Scale ablation: Qwen3 8B vs.\ 4B QE $\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\ref{app:re_extension}.}
1659:\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\rho$ across four temperatures. $\kappa$: Fleiss' $\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62fb7ffd-189f-419b-a1de-62c407223ed7",
  "isSidechain": true,
  "promptId": "eddf89e2-fe33-4930-bead-b26ed42605a7",
  "agentId": "a984115b55b0e4fdf",
  "type": "user",
  "uuid": "712f1fe3-de37-4be1-b500-3f9024e2af33",
  "sourceToolAssistantUUID": "62fb7ffd-189f-419b-a1de-62c407223ed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-22T08:11:05.182Z_

Perfect! Now let me create a comprehensive summary of all the RE-related content I found. Let me compile the findings:

## Summary

I have successfully located the **appendix.tex** file and found extensive sections related to Relation Extraction (RE). Here are the key RE-related sections and tables:

### File Location
`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex`

### Major RE Sections and Tables

#### 1. **RE Extension Section** (lines 980-1100)
- **Location**: Section "Exploratory Extension to Relation Extraction" (label: `app:re_extension`, line 980)
- **Scope**: Single-benchmark exploratory analysis on SciERC
- **Key findings**:
  - 40% of RE instances receive zero F1
  - Entity span errors account for 55.5% of RE false negatives
  - VC leads on RE ($\rho=0.309±0.024$)
  - LP is #2 on RE ($\rho=0.297±0.022$), reversing NER hierarchy
  - RE miscalibration more severe than NER (ECE 0.109-0.339)

#### 2. **RE Selection Table (N=8)** - `tab:re_cond_selection` (lines 1010-1029)
- **Configuration**: SciERC, N=8, T=1.0
- **Data**: Full set (n=397) and non-zero F1 subset (n=238)
- **Key metrics**:
  - **Oracle headroom**: 18.1 pp (full), exists but unexploited
  - **LP**: 0.395 (full), 0.600 (non-zero) - best among signals but below greedy
  - **SJ**: 0.386 (full), 0.604 (non-zero)
  - **EM**: 0.372 (full), 0.583 (non-zero)
  - **VC**: 0.359 (full), 0.574 (non-zero)
  - **Greedy**: 0.404 (full), 0.674 (non-zero)

#### 3. **RE Selection Table (N=16)** - `tab:re_n16_selection` (lines 1039-1060)
- **Configuration**: SciERC, Qwen3-4B, N=16, 3-seed mean
- **Key metrics**:
  - **Oracle headroom**: 17.1 pp (substantial unrealized)
  - **LP**: 0.299±0.007, **Δ=+0.7 pp** (only positive signal, p=0.058)
  - **VC**: 0.284±0.002, Δ=-0.8 pp
  - **FK**: 0.283±0.005, Δ=-0.9 pp
  - **SJ**: 0.281±0.005, Δ=-1.0 pp
  - **EM**: 0.277±0.007, Δ=-1.5 pp
  - **Greedy**: 0.291±0.000
  - **Note**: Even best seed captures only ~9% of 17.1 pp oracle headroom

#### 4. **Degeneracy Data**
The appendix contains extensive degeneracy metrics:
- **Tab 44** (line 381): Cross-dataset degeneracy--LP gain (n=23): ρ=0.810, p=1.0
- **Tab 45** (line 382): Per-type degeneracy--headroom (Few-NERD, Spearman): ρ=0.004, p=0.180
- **Tab 48** (line 385): SciERC per-type degeneracy--LP (ρ=0.14): p=0.790
- **Main degeneracy table** (`tab:degeneracy`, lines 444-461):
  - SciERC 8B: Constant F1 = 12.2%
  - SciERC 4B: Constant F1 = 10.4%
  - CoNLL 8B: Constant F1 = 61.7%

#### 5. **RE Quality Estimation** (line 987)
From `tab:multiseed`:
- **VC**: 0.309±0.024 (leads on RE)
- **LP**: 0.297±0.022 (#2, differs from NER where LP is weaker)
- Signal ranking differs from NER on RE

#### 6. **Free-Form Decoding Ablation** (`tab:freeform_ablation`, lines 1209-1276)
- **Critical RE finding** (line 1214): LP selection **reverses under free-form decoding**
  - Constrained: -0.68 pp
  - Free-form: +1.84±0.12 pp (across 4 seeds)
  - Preliminary evidence of task-specific decoding interactions

#### 7. **RE Failure Analysis** (lines 980-1100)
- Compound error propagation worsens all signals
- Structural mismatch: set-valued outputs without equivalence classes
- 40% zero-F1 floor effect ruling out as primary explanation
- Entity span errors as prerequisite failure that consistency signals cannot detect

#### 8. **TOST Equivalence Testing** - RE Results (`tab:tost`, lines 474-494)
- **RE (n=397)**:
  - LP: Δ=-0.9 pp
  - SJ: Δ=-1.8 pp
  - FK: Δ=-1.6 pp
  - EM: Δ=-3.2 pp (significant underperformance even at ±5 pp)
  - VC: Δ=-4.5 pp (significant underperformance even at ±5 pp)

#### 9. **Temperature Sensitivity on RE** (lines 40-77)
- RE shows different temperature effects than NER
- T=0.7: FK ρ increases 0.091 on RE vs drops on NER
- T=1.0: LP ρ=0.266 on RE (0.205 on NER)

### Key Tables by Line Number and Reference Labels
- `tab:robustness` (line 38): Temperature and sample size robustness, includes RE ρ values
- `tab:multiseed` (line 658): Multi-seed QE on SciERC, RE: Qwen only
- `tab:signal_heatmap` (line 139): Includes per-relation diagnostic showing ρ variation from 0.004 to 0.646
- `tab:reliability` (line 127): Calibration analysis, RE shows ECE 0.109-0.339
- `tab:per_relation_diagnostic` (line 144): Feature-Of (ρ=0.004) vs Hyponym-Of (ρ=0.646)

This comprehensive RE section provides detailed analysis of degeneracy, MV/majority-vote effects, LP-best performance, and oracle headroom across multiple configurations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "712f1fe3-de37-4be1-b500-3f9024e2af33",
  "isSidechain": true,
  "agentId": "a984115b55b0e4fdf",
  "requestId": "req_011CbHGXweVzx7rcwjxv7aAW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f82faa57-022a-48c8-83df-ec7170f6d3bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/agent_70248b8a",
  "sessionId": "c3b01396-4193-441d-88e9-af70976b21c3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "delightful-splashing-babbage",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VAwcsaERrkzg7YcoHwbr5r",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5275,
      "cache_read_input_tokens": 83052,
      "output_tokens": 1746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5275
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1746,
          "cache_read_input_tokens": 83052,
          "cache_creation_input_tokens": 5275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5275,
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
