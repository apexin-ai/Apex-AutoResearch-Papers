# Research conversation: Find and read the main LaTeX paper files for the struct_self_consist_ie project. The paper is likely in the artifacts/dr

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a3a8f9937ba741116.jsonl`
- **Structured JSON:** [`aeee927b433f7cea5ac9.json`](../../sessions/ae/aeee927b433f7cea5ac9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-15T19:14:03.378Z_

Find and read the main LaTeX paper files for the struct_self_consist_ie project. The paper is likely in the artifacts/dream_reports directory or a dedicated paper directory. Look for the most recent paper.tex, and also check for a sections/ directory with individual .tex files (abstract.tex, conclusion.tex, introduction.tex, experiments.tex, methodology.tex, related_work.tex, discussion.tex, limitations.tex, appendix.tex etc).

Search in:
- /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/
- Any paper/ or latex/ subdirectories

Report all .tex files found with their paths and modification times, and read the content of the main paper file and key sections (especially experiments section for numerical claims, and any tables).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "47092cf1-2d78-45b2-9ddd-5e5ae7fd85a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-15T19:14:05.076Z_

I'll help you find and read the LaTeX paper files for the struct_self_consist_ie project. Let me search systematically for these files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47092cf1-2d78-45b2-9ddd-5e5ae7fd85a5",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tT5vqLM3gJSRNfFGrC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8f67a21d-4fb2-4b29-ab09-8e1e0a9afd3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hg35SLBnfRhFsKsaYK3PYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20797,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20797,
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

_source line 3 · 2026-05-15T19:14:05.293Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jkd8oPU5yrNpLCiHTtYZF4`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.tex\" -type f 2>/dev/null | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f67a21d-4fb2-4b29-ab09-8e1e0a9afd3e",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tT5vqLM3gJSRNfFGrC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7b44bbc9-7021-4d2c-9091-75af5cea96dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hg35SLBnfRhFsKsaYK3PYS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20797,
      "cache_read_input_tokens": 0,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20797
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 133,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 20797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20797,
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

_source line 4 · 2026-05-15T19:14:05.585Z_

<details><summary>↩ Tool result · `toolu_01Jkd8oPU5yrNpLCiHTtYZF4`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/freeform_ablation_appendix_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_ci_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_scaling_appendix_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b44bbc9-7021-4d2c-9091-75af5cea96dc",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "85698db3-1f16-4090-b518-4e8aaed51d70",
  "sourceToolAssistantUUID": "7b44bbc9-7021-4d2c-9091-75af5cea96dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-15T19:14:07.613Z_

Good! I found multiple .tex files. Now let me check the modification times to find the most recent paper, and then read the main files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85698db3-1f16-4090-b518-4e8aaed51d70",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTFCwSn76hiPis3Tpb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4558db9c-845b-4311-bea4-2263c5fb2468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016s3yTFbP57iGAbPcFh63RH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2550,
      "cache_read_input_tokens": 20797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2550,
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

_source line 6 · 2026-05-15T19:14:08.205Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TmVGLKj8qZmbChsEAMykvg`</summary>

```json
{
  "command": "ls -lt /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/*.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/*.tex 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4558db9c-845b-4311-bea4-2263c5fb2468",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTFCwSn76hiPis3Tpb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c9e690a2-f87a-4687-8689-26fe009577bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016s3yTFbP57iGAbPcFh63RH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2550,
      "cache_read_input_tokens": 20797,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2550
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 167,
          "cache_read_input_tokens": 20797,
          "cache_creation_input_tokens": 2550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2550,
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

_source line 7 · 2026-05-15T19:14:08.282Z_

<details><summary>↩ Tool result · `toolu_01TmVGLKj8qZmbChsEAMykvg`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 18046 May 15 16:16 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
-rw-r--r-- 1 ubuntu ubuntu  1504 May 15 15:35 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
-rw-r--r-- 1 ubuntu ubuntu  2524 May 15 12:17 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
-rw-r--r-- 1 ubuntu ubuntu  2530 May 15 12:06 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables.tex
-rw-r--r-- 1 ubuntu ubuntu  2344 May 15 10:30 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/freeform_ablation_appendix_table.tex
-rw-r--r-- 1 ubuntu ubuntu  1734 May 14 21:10 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
-rw-r--r-- 1 ubuntu ubuntu  2169 May 14 21:09 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu  1559 May 14 21:09 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
-rw-r--r-- 1 ubuntu ubuntu  4076 May 14 20:50 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  9219 May 14 20:31 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  6245 May 14 20:10 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9e690a2-f87a-4687-8689-26fe009577bb",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "e8f93aa4-ba74-4666-ad65-2da574506ad8",
  "sourceToolAssistantUUID": "c9e690a2-f87a-4687-8689-26fe009577bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-15T19:14:09.473Z_

Let me get a complete list with all file details and check for the main paper file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8f93aa4-ba74-4666-ad65-2da574506ad8",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTSemDyu4MbVLLuvTp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "461a0bb5-8be2-47af-9cf9-22b71d0c4448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ms7RqksbGmy2CwAq8KViQu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 23347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 921,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 9 · 2026-05-15T19:14:09.890Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KvF5hJxEX1v9aakFEjWN8D`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"paper.tex\" -o -name \"main.tex\" 2>/dev/null | xargs ls -lt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "461a0bb5-8be2-47af-9cf9-22b71d0c4448",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTSemDyu4MbVLLuvTp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "358e6631-b143-43c6-a801-8f0d3707ca44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ms7RqksbGmy2CwAq8KViQu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 23347,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 921
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 128,
          "cache_read_input_tokens": 23347,
          "cache_creation_input_tokens": 921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 921,
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

_source line 10 · 2026-05-15T19:14:09.983Z_

<details><summary>↩ Tool result · `toolu_01KvF5hJxEX1v9aakFEjWN8D`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu  1504 May 15 15:35 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
-rw-r--r-- 1 ubuntu ubuntu 28288 May 15 10:04 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 38761 May 15 10:00 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/median/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 38829 May 15 09:54 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 34876 May 14 21:17 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 40482 May 14 21:12 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 41720 May 14 21:06 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/best/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 33731 May 14 11:46 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 36120 May 14 11:41 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 41198 May 14 11:37 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 30835 May 14 10:06 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 33502 May 14 10:00 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.tex
-rw-r--r-- 1 ubuntu ubuntu 31178 May 14 09:56 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "358e6631-b143-43c6-a801-8f0d3707ca44",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "c0b857b3-816f-40cb-a608-40b64021f517",
  "sourceToolAssistantUUID": "358e6631-b143-43c6-a801-8f0d3707ca44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-15T19:14:11.570Z_

Now let me read the main LaTeX files. The most recent paper files are in dream_20260515T092545. Let me read the main.tex from the docs/paper directory and the sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0b857b3-816f-40cb-a608-40b64021f517",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTZy3wso6b2ajrUqPi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6dd73109-9524-4f28-a1b1-dcb5469ce454",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Y2b2CB5mRdNx52iaHX21u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 24268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1114,
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

_source line 12 · 2026-05-15T19:14:11.865Z_

<details open><summary>🔧 Tool call — Read · `toolu_011iyUUPqgmbgX2efV6XeY1d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dd73109-9524-4f28-a1b1-dcb5469ce454",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTZy3wso6b2ajrUqPi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ee73bedb-262c-4110-be45-af83697eb80f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Y2b2CB5mRdNx52iaHX21u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 24268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1114,
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

_source line 13 · 2026-05-15T19:14:11.876Z_

<details><summary>↩ Tool result · `toolu_011iyUUPqgmbgX2efV6XeY1d`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals Predict but Struggle to Select in 8B-Scale Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee73bedb-262c-4110-be45-af83697eb80f",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "d50c833f-6469-43a0-95f6-324e0f8e78ad",
  "sourceToolAssistantUUID": "ee73bedb-262c-4110-be45-af83697eb80f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T19:14:12.026Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XNfHznLbmyovWXHscpeLfK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d50c833f-6469-43a0-95f6-324e0f8e78ad",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTZy3wso6b2ajrUqPi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9593ffaf-2cd6-413f-a4e0-b5dfc29c94fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Y2b2CB5mRdNx52iaHX21u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 24268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1114,
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

_source line 15 · 2026-05-15T19:14:12.035Z_

<details><summary>↩ Tool result · `toolu_01XNfHznLbmyovWXHscpeLfK`</summary>

```text
1	\begin{abstract}
2	Self-consistency---sampling multiple outputs and selecting via agreement---yields large gains on discrete-answer tasks, but information extraction (IE) produces \textit{sets} of entities and relations with partial overlap, where no majority vote exists.
3	Can confidence signals still guide selection in this structured setting?
4	
5	We compare five confidence signals---spanning structural consistency, surface agreement, and model-internal families---across three NER benchmarks and one RE benchmark (preliminary) with two 8B-parameter models.
6	All signals achieve strong quality estimation yet none improves best-of-$N$ sample selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
7	The gap has two layers: instance-level signals cannot rank candidates by construction, and log-probability---the only per-sample signal---is too compressed within instances to discriminate; a free-form decoding ablation confirms this compression is intrinsic to the model, not an artifact of constrained decoding.
8	Signal rankings shift with task difficulty and collapse at the capability boundary.
9	Closing the gap likely requires learned per-sample scoring such as trained verifiers.
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9593ffaf-2cd6-413f-a4e0-b5dfc29c94fc",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "9ee39f76-9253-4573-ab88-ec65e1cd72d4",
  "sourceToolAssistantUUID": "9593ffaf-2cd6-413f-a4e0-b5dfc29c94fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T19:14:14.819Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XEjTu6GAHjgvvyym8LkLpo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ee39f76-9253-4573-ab88-ec65e1cd72d4",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTZy3wso6b2ajrUqPi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "558c7285-ea93-4f05-94b1-5f11302c86a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Y2b2CB5mRdNx52iaHX21u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 24268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1114,
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

_source line 17 · 2026-05-15T19:14:14.825Z_

<details><summary>↩ Tool result · `toolu_01XEjTu6GAHjgvvyym8LkLpo`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks, majority voting over chain-of-thought samples yields large gains---+18~pp on GSM8K \citep{wang2023selfconsistency}---and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
5	These results assume that among $N$ stochastic samples, a selection mechanism can identify better outputs; for tasks with a single answer, majority voting is the selector.
6	But information extraction (IE) poses a structurally different challenge: the output is a \textit{set} of entities or relations with internal dependencies, two samples may extract overlapping but non-identical structures, and there is no obvious majority to vote on.
7	Can self-consistency still provide useful signal in this structured setting?
8	
9	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
10	Self-consistency methods for reasoning \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
11	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE; our work extends theirs with structural matching, a selection analysis, and a difficulty gradient.
12	
13	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve strong quality estimation ($\rho$ up to 0.45) but fail at sample selection despite substantial oracle headroom.
14	Four of five signals are instance-level by construction; log-probability, the only per-sample signal, is too compressed to discriminate (\S\ref{sec:discussion}), though where compression is mitigated, selection recovers gains (\S\ref{sec:ablation}).
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=\textwidth]{fig_overview}
19	\caption{The correlation-selection gap. \textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}
20	\label{fig:overview}
21	\end{figure*}
22	
23	We compare five confidence signals from three families---structural, surface, and model-internal---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
24	Our contributions are:
25	\begin{enumerate}
26	    \item \textbf{Metric dissociation.}
27	    We find that quality estimation, binary discrimination, and sample selection decouple, so single-metric evaluation risks selecting the wrong signal.
28	
29	    \item \textbf{The correlation-selection gap.}
30	    Despite strong quality estimation, no signal improves sample selection: log-probability scores are too compressed within instances, and MBR-style selection correlates with F1 across but not within instances.
31	
32	    \item \textbf{Difficulty- and task-dependent signal rankings.}
33	    Signal rankings shift with task complexity and type, and collapse at the capability boundary. RE conclusions rest on SciERC alone (preliminary).
34	\end{enumerate}
35	
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "558c7285-ea93-4f05-94b1-5f11302c86a4",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "52456701-658e-49b1-b20e-cfa2d42e22d0",
  "sourceToolAssistantUUID": "558c7285-ea93-4f05-94b1-5f11302c86a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T19:14:14.921Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BHoao7hg1z1puEKkeewaEQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52456701-658e-49b1-b20e-cfa2d42e22d0",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTZy3wso6b2ajrUqPi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea0121f3-43a7-4eb7-9f01-0fefb7147d47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Y2b2CB5mRdNx52iaHX21u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 24268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1114,
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

_source line 19 · 2026-05-15T19:14:14.934Z_

<details><summary>↩ Tool result · `toolu_01BHoao7hg1z1puEKkeewaEQ`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N$-scaling analysis (Appendix~\ref{app:n_scaling}) shows sublinear gains beyond $N{=}8$; 3-seed stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirms identical signal rankings across seeds.}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best per column in \textbf{bold}. SciERC: joint NER (6 types) and RE (7 types, preliminary); CoNLL: NER (4 types). $N{=}16$ in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
31	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
32	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
33	\midrule
34	VC & Structural & \textbf{.379} & \textbf{.663} & \textbf{.350} & .694 & .424 & .789 & .426 & .709 \\
35	SJ  & Structural & .360 & .650 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
36	FK & Surface & .267 & .602 & .275 & .609 & .400 & .774 & .428 & .703 \\
37	EM  & Surface    & .295 & .614 & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
38	\midrule
39	LP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \textbf{.761} \\
40	\bottomrule
41	\end{tabular}
42	\end{table*}
43	
44	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.\footnote{$\varepsilon{=}0.05$ is a convenience threshold used only in the selection analysis (\S\ref{sec:selection_gap}); quality estimation metrics ($\rho$, AUROC) are continuous and $\varepsilon$-free. Selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}).}
45	
46	\paragraph{Difficulty-dependent signal complementarity.}
47	On SciERC NER, structural signals lead: VC $\rho{=}0.379$, SJ $\rho{=}0.360$, outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$); on RE (preliminary), LP rises above SJ and FK in multi-seed analysis (Table~\ref{tab:multiseed}), likely because RE's 40\% zero-F1 rate favors generation confidence.
48	The best NER AUROC reaches 0.816 (EM, CoNLL Qwen); pairwise bootstrap CIs confirm the SJ--LP gap ($\Delta\rho{=}{+}0.155$, CI excludes zero; Appendix~\ref{app:bootstrap_signal}).
49	Signal choice depends on use case: EM leads AUROC but not $\rho$ on CoNLL, preferred for binary triage; this $\rho$--AUROC dissociation replicates across configurations.
50	
51	\paragraph{Signal rankings shift with task difficulty.}
52	On CoNLL (greedy F1${\approx}$0.91), EM leads; on SciERC, structural signals dominate---demonstrating difficulty-dependent complementarity consistent across model families.
53	On WNUT-17 (52\% zero F1), all conditional signals collapse (Table~\ref{tab:wnut}), suggesting a capability boundary beyond which consistency captures binary success/failure but not quality gradation.
54	Restricting to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, Appendix~\ref{app:additional}): EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while LP RE collapses to $\rho{=}0.011$.
55	
56	%% ============================================================
57	\subsection{The Correlation-Selection Gap}
58	\label{sec:selection_gap}
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). NER: 2-seed mean${\pm}\sigma$, Fisher combined $p$ vs.\ greedy; RE: single seed (preliminary). Best non-oracle in \textbf{bold}. $^\dagger$Greedy: a fixed $T{=}1.0$ sample.}
64	\label{tab:selection}
65	\begin{tabular}{lccc}
66	\toprule
67	Method & NER F1 & $p$ & RE F1 \\
68	\midrule
69	Oracle & $0.778 \pm 0.003$ & --- & 0.585 \\
70	\midrule
71	\multicolumn{4}{l}{\textit{Per-sample signal}} \\
72	LP           & $\mathbf{0.647} \pm 0.005$ & .29 & 0.395 \\
73	\midrule
74	\multicolumn{4}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
75	SJ           & $0.646 \pm 0.002$ & .68 & 0.386 \\
76	FK           & $0.646 \pm 0.001$ & .79 & --- \\
77	EM           & $0.637 \pm 0.001$ & .45 & 0.372 \\
78	VC           & $0.623 \pm 0.004$ & .26 & 0.359 \\
79	\midrule
80	Greedy$^\dagger$ & $0.645 \pm 0.001$ & --- & \textbf{0.404} \\
81	Random           & $0.610 \pm 0.003$ & --- & 0.354 \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	Despite strong quality estimation, confidence signals yield limited gains for best-of-$N$ selection (Table~\ref{tab:selection}; see also Figure~\ref{fig:selection_gap}).
87	Four of five signals are instance-level by construction (they assign identical scores to all candidates); the non-trivial question is whether LP---the only per-sample signal---can exploit the oracle headroom.
88	We anchor on SciERC, where output diversity is substantial (39--43\% unique outputs; Appendix~\ref{app:diversity}).
89	
90	\paragraph{No significant improvement over greedy.}
91	We evaluate significance via 2-seed instance-level sign tests ($n{=}551$, Fisher combination).
92	On NER, the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645).
93	LP achieves the highest mean selection F1 (0.647), indistinguishable from greedy ($\Delta{=}{+}0.2$~pp, $p{=}0.29$); all other signals also fail to reach significance (all $p{>}0.05$; Table~\ref{tab:selection}).
94	On RE, the best signal (LP, 0.395) falls below greedy (0.404; single seed, preliminary), while 18.1~pp of oracle headroom remains.
95	The pattern is consistent across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}).
96	
97	\paragraph{Quality estimation $\neq$ output selection.}
98	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; when per-sample variance is low, even perfect quality estimation fails to discriminate.
99	Closing this gap likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
100	
101	%% ============================================================
102	\subsection{Robustness}
103	\label{sec:robustness_main}
104	
105	Consistency-based signals (SJ, FK, EM, VC) are robust across $T{\in}\{0.7, 1.0\}$ and show sublinear gains from $N{=}8$ to $N{=}16$ (Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}); LP is excluded from this robustness claim, exhibiting the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$ on NER).
106	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}); RE miscalibration (ECE up to 0.339, preliminary) imposes a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea0121f3-43a7-4eb7-9f01-0fefb7147d47",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "dbbe538b-6971-42e5-8849-f1e00281e194",
  "sourceToolAssistantUUID": "ea0121f3-43a7-4eb7-9f01-0fefb7147d47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T19:14:14.995Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LHzoGnWB2LnmuGqr9hbSJR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbbe538b-6971-42e5-8849-f1e00281e194",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTZy3wso6b2ajrUqPi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "73710169-d4e9-4d66-a588-8d574016eb36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Y2b2CB5mRdNx52iaHX21u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 24268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1114,
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

_source line 21 · 2026-05-15T19:14:15.014Z_

<details><summary>↩ Tool result · `toolu_01LHzoGnWB2LnmuGqr9hbSJR`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set (NER) or relation set (RE).
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input.
7	This asymmetry is central to the correlation-selection gap: instance-level signals predict \textit{which inputs} are easy, not \textit{which output} is best (notation in Appendix~\ref{app:notation}).
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four signals are \textit{consistency signals} from two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal} signal and the only per-sample one.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	The only per-sample signal.
15	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
16	\begin{equation}\label{eq:logprob}
17	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
18	\end{equation}
19	
20	\paragraph{Exact match voting (surface, instance-level).}
21	The majority fraction---the proportion of samples producing the most common output:
22	\begin{equation}\label{eq:em}
23	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
24	\end{equation}
25	
26	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
27	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
28	\begin{equation}\label{eq:fk}
29	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
30	\end{equation}
31	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
32	Temperature-based sampling introduces mild negative dependence (excess agreement $-$0.4\% to $-$4.0\%), which does not inflate FK.
33	Unlike structural signals, FK relies on exact string matching.
34	
35	\paragraph{Soft Jaccard (structural, instance-level).}
36	Extends Jaccard similarity \cite{jaccard1901distribution} to entity/relation sets.
37	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing token-level IoU), and define:
38	\begin{equation}\label{eq:sj}
39	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
40	\end{equation}
41	where $M$ is the matched set, $\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\max(|g_i|, |g_j|)$ penalizes length asymmetry.
42	The instance-level signal averages over all pairs:
43	\begin{equation}\label{eq:sj_instance}
44	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
45	\end{equation}
46	
47	\paragraph{Entity voting confidence (structural, instance-level).}
48	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
49	The instance-level confidence is the mean frequency:
50	\begin{equation}\label{eq:voting}
51	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
52	\end{equation}
53	When $E_\cup = \emptyset$, we set $c_{\mathrm{vc}}(x) = 0$.\footnote{Equation~\ref{eq:voting} defines the continuous QE signal; for voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}
54	
55	\subsection{Evaluation Framework}\label{sec:evaluation}
56	
57	\paragraph{Quality estimation.}
58	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
59	Correlation analyses exclude instances with empty gold annotations ($n{=}529$ on SciERC after filtering 22/551); selection analyses retain the full set ($n{=}551$).
60	
61	\paragraph{Sample selection.}
62	We report best-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output.
63	We compare against an \textit{oracle} (highest-F1 sample) and a \textit{greedy} baseline (a fixed $T{=}1.0$ sample).
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73710169-d4e9-4d66-a588-8d574016eb36",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "61bd6599-0ac2-4394-90fc-9d6ab34a83ea",
  "sourceToolAssistantUUID": "73710169-d4e9-4d66-a588-8d574016eb36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-15T19:14:16.075Z_

Now let me read the remaining sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61bd6599-0ac2-4394-90fc-9d6ab34a83ea",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTweHEekGS3LDCt5aE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "85d87578-8d0c-4a0b-bdf3-914dda133d7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Phqe2saJEYxQSXYZDySSdq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 25382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7304,
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

_source line 23 · 2026-05-15T19:14:17.264Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A5bqydTTjcPjVq1uqXPFCQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85d87578-8d0c-4a0b-bdf3-914dda133d7b",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTweHEekGS3LDCt5aE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fbd8e7fc-446c-4677-bd6a-af9a970ab717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Phqe2saJEYxQSXYZDySSdq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 25382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7304,
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

_source line 24 · 2026-05-15T19:14:17.274Z_

<details><summary>↩ Tool result · `toolu_01A5bqydTTjcPjVq1uqXPFCQ`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2025scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings but leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
14	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
15	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
16	
17	\paragraph{Uncertainty estimation and calibration.}
18	Surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
19	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; P(True) \cite{kadavath2022language} queries model confidence directly.
20	Our structural signals instead measure agreement over output \textit{structure}, requiring no model modification unlike deep ensembles \cite{lakshminarayanan2017ensembles} or MC-dropout \cite{gal2016dropout}.
21	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling} with structural utility functions.
22	\citet{eikema2025structured} study structure-conditional MBR and find that standard utility functions degrade on structured outputs; they attribute this to the mismatch between bag-of-unit utilities and compositional output structure, a diagnosis consistent with our finding that consensus-proximity selection fails for IE.
23	We extend their analysis by showing the specific failure mode: utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}).
24	Despite MBR's success in translation \cite{freitag2022high} and other generation tasks \cite{jinnai2024mbr}, this within-instance misalignment renders it ineffective for structured IE.
25	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} learn per-sample scoring that may bridge this gap.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbd8e7fc-446c-4677-bd6a-af9a970ab717",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "3b7e81ba-a251-4f44-8ef7-494a6fe6d00b",
  "sourceToolAssistantUUID": "fbd8e7fc-446c-4677-bd6a-af9a970ab717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T19:14:17.400Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EzSFjrhXA3ZnvPMNwUd5uY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b7e81ba-a251-4f44-8ef7-494a6fe6d00b",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTweHEekGS3LDCt5aE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7b4e60fd-6bc7-4179-bf99-71220e368cd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Phqe2saJEYxQSXYZDySSdq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 25382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7304,
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

_source line 26 · 2026-05-15T19:14:17.412Z_

<details><summary>↩ Tool result · `toolu_01EzSFjrhXA3ZnvPMNwUd5uY`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For quality ranking, VC leads on hard NER ($\rho{=}0.38$) while EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL); on RE (preliminary), LP outperforms structural signals (Table~\ref{tab:multiseed}).
5	Rankings are consistent across two 8B-scale model families; at the capability boundary (WNUT-17), all signals collapse (Table~\ref{tab:wnut}).
6	
7	\paragraph{Why the gap exists: two layers.}
8	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
9	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, is severely compressed within instances: the median LP range is 0.041 nats (IQR [0.024, 0.073]; Figure~\ref{fig:lp_range_cdf}, Table~\ref{tab:logprob_ties}).
10	Where compression is mitigated ($n{=}210$ instances with above-median spread), LP selection outperforms greedy ($+2.9$~pp, $p{=}0.004$), confirming compression as the bottleneck.
11	The gap holds even among high-diversity instances (Appendix~\ref{app:diversity}).
12	
13	\paragraph{The gap widens with $N$.}
14	Doubling from $N{=}8$ to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving signal-based selection; on RE at $N{=}16$ (preliminary), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$; Table~\ref{tab:re_n16_selection}).
15	Detailed $N$-scaling analysis in Appendix~\ref{app:n_scaling}.
16	
17	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
18	Removing grammar constraints entirely (SciERC, Qwen3-8B) yields nearly identical LP distributions and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of score compression.
19	Our consensus-proximity strategies instantiate MBR decoding \cite{eikema2022sampling}; all fail because utility correlates with F1 across instances but not within them (Appendix~\ref{app:mbr_discussion}).
20	
21	\paragraph{Methodological implications.}
22	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.
23	Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N{=}8$ captures most quality estimation benefit (Appendix~\ref{app:n_scaling}).
24	Structural signals are robust to domain shift when the training schema subsumes the target (Appendix~\ref{app:ood}).
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b4e60fd-6bc7-4179-bf99-71220e368cd2",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "75f7ca21-b693-4de9-b05f-0b770d125ebc",
  "sourceToolAssistantUUID": "7b4e60fd-6bc7-4179-bf99-71220e368cd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T19:14:17.606Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Un6YsjVdiz2DZQRaR4fsu4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75f7ca21-b693-4de9-b05f-0b770d125ebc",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTweHEekGS3LDCt5aE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e0a3bc74-0878-4306-89e3-a63d23c1ac22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Phqe2saJEYxQSXYZDySSdq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 25382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7304,
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

_source line 28 · 2026-05-15T19:14:17.612Z_

<details><summary>↩ Tool result · `toolu_01Un6YsjVdiz2DZQRaR4fsu4`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based structured IE, revealing that these objectives decouple: all signals achieve strong quality estimation yet none improves sample selection despite substantial oracle headroom---the \textit{correlation-selection gap}.
4	Four signals fail by construction (instance-level); log-probability is too compressed within instances to discriminate (median range 0.041 nats, IQR [0.024, 0.073]), though selection recovers where compression is mitigated; a free-form ablation confirms compression is model-intrinsic.
5	Signal rankings shift with difficulty and task type, and collapse at the capability boundary---consistent across two model families.
6	RE findings rest on SciERC alone (preliminary); trained verifiers and scaling to 70B+ are promising directions.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0a3bc74-0878-4306-89e3-a63d23c1ac22",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "bd15a75f-44ec-415f-8cd3-c2baadeb3aec",
  "sourceToolAssistantUUID": "e0a3bc74-0878-4306-89e3-a63d23c1ac22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T19:14:18.058Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ANciBkdYL89VFV4EKAi7n1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd15a75f-44ec-415f-8cd3-c2baadeb3aec",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTweHEekGS3LDCt5aE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23131a9f-c7c4-4936-91a0-f878522adc99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Phqe2saJEYxQSXYZDySSdq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 25382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7304,
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

_source line 30 · 2026-05-15T19:14:18.068Z_

<details><summary>↩ Tool result · `toolu_01ANciBkdYL89VFV4EKAi7n1`</summary>

```text
1	Our evaluation covers three NER datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1; RE selection failure persists even on non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), but generalization to other RE benchmarks remains unvalidated.
2	WNUT-17 confirms the capability boundary; positive results on formal text have not been validated on informal domains where models achieve non-trivial performance.
3	
4	We evaluate two 8B-parameter model families; whether the correlation-selection gap and difficulty-dependent signal ordering hold for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples, potentially altering the signal landscape.
5	We do not train a dedicated verifier or reward model, leaving unknown how much oracle headroom a supervised approach could recover.
6	
7	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
8	On CoNLL, the structural advantage over surface signals is marginal (SJ--FK $\Delta\rho{=}0.003$) and may not generalize to all simple-schema datasets.
9	The free-form ablation was conducted on a single dataset with one model; whether LP compression generalizes to other settings remains untested.
10	
11	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis (Appendix~\ref{app:thinking_token}) rules out this confound.
12	One of three seeds used a different subtask flag; the F1 difference is ${<}0.3$~pp and LP compression is unaffected (Appendix~\ref{app:logprob_ties}).
13	
14	Log-probability shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$ on NER; RE $T{=}0.7$ data unavailable), and LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23131a9f-c7c4-4936-91a0-f878522adc99",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "944b25c8-7c87-4d73-b89d-e77a40d5c995",
  "sourceToolAssistantUUID": "23131a9f-c7c4-4936-91a0-f878522adc99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T19:14:18.166Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JZENewuArD1dxcPe6798M5`</summary>

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
  "parentUuid": "944b25c8-7c87-4d73-b89d-e77a40d5c995",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tTweHEekGS3LDCt5aE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dde2e3a4-09ce-46a2-903f-892cba383474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Phqe2saJEYxQSXYZDySSdq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 25382,
      "output_tokens": 399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7304
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 399,
          "cache_read_input_tokens": 25382,
          "cache_creation_input_tokens": 7304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7304,
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

_source line 32 · 2026-05-15T19:14:18.482Z_

<details><summary>↩ Tool result · `toolu_01JZENewuArD1dxcPe6798M5`</summary>

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
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
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
82	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.
87	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
88	
89	\paragraph{Transfer across model families.}
90	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
91	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
92	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$),\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.474{\pm}0.009$ vs.\ LP $0.311{\pm}0.003$, $\Delta{=}{+}0.163$).
93	
94	\section{Calibration Analysis}\label{app:calibration}
95	
96	\begin{figure*}[t]
97	\centering
98	\includegraphics[width=\textwidth]{fig_reliability}
99	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
100	\label{fig:reliability}
101	\end{figure*}
102	
103	Reliability diagrams use 10 equal-width bins.
104	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
105	
106	\section{Additional Analyses}\label{app:additional}
107	
108	\begin{figure*}[t]
109	\centering
110	\includegraphics[width=\textwidth]{fig_signal_heatmap}
111	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
112	\label{fig:signal_heatmap}
113	\end{figure*}
114	
115	\paragraph{Per-relation diagnostic.}
116	RE signal degradation is relation-specific.
117	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
118	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
119	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
120	
121	\paragraph{Capability stratification.}
122	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
123	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
124	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
125	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
126	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
127	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
128	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
129	
130	\paragraph{Length vs.\ log-probability.}
131	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
132	
133	\begin{figure}[t]
134	\centering
135	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
136	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
137	\label{fig:length_logprob_scatter}
138	\end{figure}
139	
140	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
141	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
142	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
143	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
144	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
145	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
146	Evaluation circularity is negligible.
147	
148	\paragraph{SJ normalizer robustness.}
149	Equation~\ref{eq:sj} uses $\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \cup g_j|$.
150	On SciERC NER ($N{=}8$, seed${=}42$), the two normalizers yield nearly identical quality estimation: $\rho_{\max}{=}0.360$ vs.\ $\rho_{\cup}{=}0.365$ ($\Delta\rho{=}0.005$, $\Delta$AUROC${=}0.003$); on CoNLL, $\rho_{\max}{=}0.431$ vs.\ $\rho_{\cup}{=}0.432$ ($\Delta\rho{<}0.001$).
151	The normalizer choice has negligible impact on results.
152	
153	\paragraph{Conditional filtering details.}
154	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
155	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
156	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
157	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
158	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
159	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
160	
161	\paragraph{WNUT-17 full signal analysis.}
162	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
163	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
164	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
165	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
166	
167	\begin{table}[t]
168	\centering
169	\small
170	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
171	\label{tab:wnut}
172	\begin{tabular}{lccccc}
173	\toprule
174	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
175	\midrule
176	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
177	FK      & .125 & .001 & .555 & .169 & .002 \\
178	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
179	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
180	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	\paragraph{Cross-configuration selection analysis.}
186	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
187	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
188	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
189	
190	\begin{table*}[t]
191	\centering
192	\small
193	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
194	\label{tab:cross_selection}
195	\begin{tabular}{llccccccc}
196	\toprule
197	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
198	\midrule
199	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
200	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
201	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
202	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
203	\bottomrule
204	\end{tabular}
205	\end{table*}
206	
207	\paragraph{Diminishing returns of $N$-scaling.}
208	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
209	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
210	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
211	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
212	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
213	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
214	
215	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
216	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
217	VC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
218	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
219	This reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
220	
221	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
222	
223	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
224	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
225	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
226	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
227	
228	\begin{table}[t]
229	\centering
230	\small
231	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
232	\label{tab:bootstrap_signal_ci}
233	\begin{tabular}{lcc}
234	\toprule
235	Signal & $\rho$ & 95\% CI \\
236	\midrule
237	VC & +0.379 & [+0.299, +0.456] \\
238	SJ & +0.360 & [+0.277, +0.437] \\
239	EM & +0.295 & [+0.212, +0.371] \\
240	FK & +0.267 & [+0.176, +0.354] \\
241	LP & +0.205 & [+0.119, +0.291] \\
242	\bottomrule
243	\end{tabular}
244	
245	\vspace{0.5em}
246	
247	\begin{tabular}{lccc}
248	\toprule
249	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
250	\midrule
251	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
252	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
253	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
254	\bottomrule
255	\end{tabular}
256	
257	\smallskip
258	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
259	\end{table}
260	
261	At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.
262	On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
263	On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
264	
265	\section{Diversity and Selection Analysis}\label{app:diversity}
266	
267	\begin{figure*}[t]
268	\centering
269	\includegraphics[width=\textwidth]{fig_selection_gap}
270	\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.40, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\ref{tab:selection}.}
271	\label{fig:selection_gap}
272	\end{figure*}
273	
274	\paragraph{Output diversity quantification.}
275	Table~\ref{tab:diversity} summarizes output diversity across configurations.
276	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
277	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
278	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
279	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
285	\label{tab:diversity}
286	\begin{tabular}{lcc}
287	\toprule
288	Config & Identical & Unique \\
289	\midrule
290	Qwen/SciERC & 11\% & 43\% \\
291	LLaMA/SciERC & 18\% & 39\% \\
292	Qwen/CoNLL & 57\% & --- \\
293	LLaMA/CoNLL & 88\% & --- \\
294	WNUT-17 & 55\% & --- \\
295	\bottomrule
296	\end{tabular}
297	\end{table}
298	
299	\paragraph{Oracle-improvable fraction.}
300	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \S\ref{sec:evaluation}); the diversity quantification in Table~\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
301	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
302	
303	\paragraph{Diversity-stratified selection gap.}
304	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
305	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
306	This rules out insufficient diversity as an explanation for the correlation-selection gap.
307	
308	\paragraph{TOST equivalence testing.}
309	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
310	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
311	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
312	These proportions use the same test data that defines the headroom and should be interpreted as context for practical relevance rather than independent calibration.
313	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
314	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
315	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
316	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
317	
318	\begin{table}[t]
319	\centering
320	\small
321	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
322	\label{tab:tost}
323	\begin{tabular}{l cccc cccc}
324	\toprule
325	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
326	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
327	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
328	\midrule
329	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
330	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
331	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
332	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
333	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
334	\bottomrule
335	\end{tabular}
336	\end{table}
337	
338	\section{Multi-Seed Stability}\label{app:multiseed}
339	
340	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
341	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals.
342	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
343	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
344	
345	\begin{table}[t]
346	\centering
347	\small
348	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
349	\label{tab:multiseed}
350	\begin{tabular}{lccccc}
351	\toprule
352	& LP & FK & SJ & VC & EM \\
353	\midrule
354	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
355	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
356	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
357	\midrule
358	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
359	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
360	\midrule
361	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
362	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
363	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
364	\bottomrule
365	\end{tabular}
366	\end{table}
367	
368	\section{Training Configuration}\label{app:training}
369	
370	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
371	
372	\begin{table}[t]
373	\centering
374	\small
375	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
376	\label{tab:training}
377	\begin{tabular}{ll}
378	\toprule
379	Parameter & Value \\
380	\midrule
381	LoRA rank / $\alpha$ & 32 / 64 \\
382	LoRA target & All linear modules \\
383	LoRA dropout & 0 \\
384	Optimizer & AdamW \\
385	Learning rate & 2e-4, cosine schedule \\
386	Warmup ratio & 0.1 \\
387	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
388	Epochs & 5 \\
389	Max sequence length & 2048 \\
390	Precision & bf16 \\
391	Gradient checkpointing & Enabled \\
392	Max gradient norm & 1.0 \\
393	Training seed & 42 \\
394	Framework & LLaMA Factory \\
395	\midrule
396	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
397	SciERC split & 1861 / 275 / 551 \\
398	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
399	& eval\_steps${=}$200, save\_limit${=}$5 \\
400	\bottomrule
401	\end{tabular}
402	\end{table}
403	
404	\paragraph{Prompt template.}
405	For NER, we use a structured prompt:
406	\begin{quote}
407	\small
408	\texttt{System:} You are an expert in Named Entity Recognition.\\
409	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
410	Text: \texttt{\{input\_text\}}\\
411	Entity types: \texttt{\{schema\_types\}}
412	\end{quote}
413	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
414	
415	\paragraph{Constrained decoding.}
416	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
417	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
418	
419	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
420	
421	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
422	We quantify the potential impact on LP scores through three complementary arguments.
423	
424	\paragraph{LP shift magnitude.}
425	The 4--5 thinking tokens contribute an estimated LP shift of 0.001 nats to the per-token log-probability average, representing 2.68\% of the median within-instance LP range (0.041 nats).
426	This shift is too small to alter LP-based rankings.
427	
428	\paragraph{Constant prefix cancellation.}
429	All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
430	Any LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \textit{rankings} unchanged.
431	
432	\paragraph{CoNLL control group.}
433	CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
434	If thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.
435	Instead, CoNLL shows \textit{higher} tied fractions at both temperatures (86.8\% at $T{=}1.0$, 95.8\% at $T{=}0.7$) than SciERC (60.3\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.
436	
437	\section{Log-Probability Score Compression}\label{app:logprob_ties}
438	
439	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
440	The median within-instance LP range is only 0.041 nats---below the $\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.
441	At $\varepsilon{=}0.05$, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
442	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
443	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
444	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
445	
446	\begin{figure}[t]
447	\centering
448	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
449	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
450	\label{fig:lp_range_cdf}
451	\end{figure}
452	
453	\begin{table}[t]
454	\centering
455	\small
456	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
457	\label{tab:logprob_ties}
458	\begin{tabular}{lc}
459	\toprule
460	$\varepsilon$ threshold & Tied instances (\%) \\
461	\midrule
462	0.01 & 1.1\% \\
463	0.05 & 60.3\% \\
464	0.1  & ${\sim}$84\% \\
465	0.5  & ${\sim}$99\% \\
466	\bottomrule
467	\end{tabular}
468	\end{table}
469	
470	\paragraph{Non-tied subset.}
471	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
472	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
473	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
474	
475	\paragraph{$\varepsilon$ sensitivity sweep.}
476	Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$.
477	The tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.
478	$\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\varepsilon{\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\leq}36$).
479	
480	\begin{table}[t]
481	\centering
482	\small
483	\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over greedy on the non-tied subset. The tied fraction increases smoothly; $\varepsilon{=}0.05$ yields the strongest statistical separation.}
484	\label{tab:epsilon_sweep}
485	\begin{tabular}{ccccc}
486	\toprule
487	$\varepsilon$ & Tied\% & Non-tied $n$ & $\Delta$ (pp) & $p$ \\
488	\midrule
489	0.01 & 1.1\% & 523 & $+$0.58 & .21 \\
490	0.02 & 13.6\% & 457 & $+$0.83 & .15 \\
491	0.03 & 31.8\% & 361 & $+$1.31 & .079 \\
492	\textbf{0.05} & \textbf{60.3\%} & \textbf{210} & \textbf{$+$2.86} & \textbf{.004} \\
493	0.10 & 83.9\% & 85 & $+$3.69 & .034 \\
494	0.15 & 93.2\% & 36 & $+$4.15 & .11 \\
495	0.20 & 96.4\% & 19 & $+$4.59 & .13 \\
496	\bottomrule
497	\end{tabular}
498	\end{table}
499	
500	\paragraph{$\varepsilon$ robustness of selection F1.}\label{app:epsilon_robustness}
501	The preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\varepsilon$ to define MBR-style proximity in selection.
502	Table~\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\varepsilon \in [0, 0.2]$ for all signals and configurations.
503	At $\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.
504	Spearman $\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\varepsilon$ parameter affects only the selection analysis.
505	
506	\begin{table}[t]
507	\centering
508	\small
509	\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
510	\label{tab:epsilon_robustness}
511	\begin{tabular}{lcccc}
512	\toprule
513	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL}} \\
514	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
515	Signal & Qwen & LLaMA & Qwen & LLaMA \\
516	\midrule
517	SJ & 0.92 & 1.45 & 0.99 & 0.18 \\
518	FK & 1.03 & 0.93 & 0.60 & 0.15 \\
519	VC & 2.33 & 0.53 & 0.72 & 0.18 \\
520	EM & 0.00 & 0.00 & 0.00 & 0.00 \\
521	LP & 3.65 & 2.58 & 3.00 & 0.31 \\
522	\bottomrule
523	\end{tabular}
524	\end{table}
525	
526	\section{RE Conditional Selection}\label{app:re_conditional_selection}
527	
528	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
529	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
530	All five signals underperform greedy on both subsets.
531	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
532	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
533	
534	\begin{table}[t]
535	\centering
536	\small
537	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
538	\label{tab:re_cond_selection}
539	\begin{tabular}{lcc}
540	\toprule
541	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
542	\midrule
543	Oracle & 0.585 & 0.757 \\
544	\midrule
545	LP & 0.395 & 0.600 \\
546	SJ & 0.386 & 0.604 \\
547	EM & 0.372 & 0.583 \\
548	VC & 0.359 & 0.574 \\
549	\midrule
550	Greedy & 0.404 & 0.674 \\
551	\bottomrule
552	\end{tabular}
553	\end{table}
554	
555	\section{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
556	
557	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
558	All four consistency signals underperform greedy, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
559	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
560	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
561	This cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.
562	
563	\begin{table}[t]
564	\centering
565	\small
566	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC ($N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
567	\label{tab:re_n16_selection}
568	\begin{tabular}{lccc}
569	\toprule
570	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
571	\midrule
572	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
573	\midrule
574	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
575	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
576	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
577	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
578	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
579	\midrule
580	Greedy & $.291{\pm}.000$ & --- & --- \\
581	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
582	\bottomrule
583	\end{tabular}
584	\end{table}
585	
586	\section{MBR Decoding and Task-Specific Interactions}\label{app:mbr_discussion}
587	
588	\paragraph{Connection to MBR decoding.}
589	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
590	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
591	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
592	
593	\paragraph{Task-specific decoding interactions.}
594	The free-form ablation reveals divergent behavior across tasks.
595	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
596	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
597	This interaction does not generalize to NER, where selection remains negligible under both regimes.
598	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
599	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
600	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
601	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
602	
603	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
604	
605	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
606	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
607	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
608	RE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\ $-0.68$~pp constrained).
609	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
610	
611	\begin{table*}[t]
612	\centering
613	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
614	\label{tab:freeform_ablation}
615	
616	\vspace{2pt}
617	{\small\textsc{Panel A: Logprob Distribution}}
618	\vspace{2pt}
619	
620	\begin{tabular}{lccc}
621	\toprule
622	Metric & Constrained & Free-form & $\Delta$ \\
623	\midrule
624	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
625	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
626	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
627	\bottomrule
628	\end{tabular}
629	
630	\vspace{8pt}
631	
632	{\small\textsc{Panel B: Selection F1}}
633	\vspace{2pt}
634	
635	\begin{tabular}{llccc}
636	\toprule
637	Task & Method & Constrained & Free-form & $\Delta$ \\
638	\midrule
639	\multirow{3}{*}{NER}
640	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
641	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
642	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
643	\midrule
644	\multirow{3}{*}{RE}
645	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
646	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
647	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
648	\bottomrule
649	\end{tabular}
650	
651	\vspace{8pt}
652	
653	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
654	\vspace{2pt}
655	
656	\begin{tabular}{l ccc ccc}
657	\toprule
658	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
659	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
660	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
661	\midrule
662	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
663	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
664	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
665	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
666	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
667	\bottomrule
668	\end{tabular}
669	
670	\vspace{8pt}
671	
672	{\small\textsc{Panel D: Parse Rate (Free-form)}}
673	\vspace{2pt}
674	
675	\begin{tabular}{lc}
676	\toprule
677	Metric & Value \\
678	\midrule
679	Total samples          & 4408 \\
680	Parse rate             & 99.95\% \\
681	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
682	\bottomrule
683	\end{tabular}
684	
685	\end{table*}
686	
687	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
688	
689	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
690	
691	\paragraph{Pairwise overlap.}
692	LP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
693	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
694	
695	\paragraph{Instance complexity drives failure.}
696	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
697	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
698	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
699	
700	\begin{table}[t]
701	\centering
702	\small
703	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}
704	\label{tab:stable_failures}
705	\begin{tabular}{lcccc}
706	\toprule
707	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
708	\midrule
709	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
710	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
711	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
712	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
713	\bottomrule
714	\end{tabular}
715	\end{table}
716	
717	\paragraph{Flip instances.}
718	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
719	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
720	
721	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
722	
723	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
724	
725	\begin{table}[t]
726	\centering
727	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
728	\label{tab:n-scaling}
729	\small
730	\begin{tabular}{l ccc ccc}
731	\toprule
732	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
733	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
734	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
735	\midrule
736	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
737	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
738	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
739	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
740	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
741	\midrule
742	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
743	\bottomrule
744	\end{tabular}
745	\end{table}
746	
747	\begin{table}[t]
748	\centering
749	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
750	\label{tab:ranking-stability}
751	\small
752	\begin{tabular}{ll cc l}
753	\toprule
754	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
755	\midrule
756	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
757	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
758	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
759	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
760	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
761	\bottomrule
762	\end{tabular}
763	\end{table}
764	
765	\begin{table}[t]
766	\centering
767	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
768	\label{tab:sigma-comparison}
769	\small
770	\begin{tabular}{l cc cc}
771	\toprule
772	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
773	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
774	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
775	\midrule
776	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
777	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
778	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
779	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
780	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
781	\midrule
782	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
783	\bottomrule
784	\end{tabular}
785	\end{table}
786	
787	Signal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}).
788	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
789	
790	\section{Cross-Dataset OOD Analysis}\label{app:ood}
791	
792	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
793	
794	\begin{table}[t]
795	\centering
796	\small
797	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
798	\label{tab:ood}
799	\begin{tabular}{l ccc ccc}
800	\toprule
801	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
802	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
803	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
804	\midrule
805	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
806	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
807	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
808	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
809	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
810	\bottomrule
811	\end{tabular}
812	\end{table}
813	
814	\paragraph{Wider-to-narrower schema transfer.}
815	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
816	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
817	
818	\paragraph{Narrower-to-wider schema transfer (excluded).}
819	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
820	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).
821	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
822	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
823	
824	\paragraph{Asymmetry interpretation.}
825	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
826	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
827	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dde2e3a4-09ce-46a2-903f-892cba383474",
  "isSidechain": true,
  "promptId": "ca9f328b-7d8f-49d7-ba83-1bf2b49868d3",
  "agentId": "a3a8f9937ba741116",
  "type": "user",
  "uuid": "b88f9381-9a4d-4862-8eff-817ac1bb4874",
  "sourceToolAssistantUUID": "dde2e3a4-09ce-46a2-903f-892cba383474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-15T19:14:36.697Z_

Perfect! I've successfully located and read all the main LaTeX paper files. Let me compile a comprehensive summary of my findings.

## Summary: LaTeX Paper Files for struct_self_consist_ie Project

### File Locations Found

**Primary Paper Structure:**
- Main file: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex` (updated May 15 15:35)
- Sections directory: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/`

**Section Files (all updated May 14-15):**
1. `abstract.tex` - Abstract
2. `introduction.tex` - Introduction (6,245 bytes, May 14 20:10)
3. `related_work.tex` - Related Work (9,219 bytes, May 14 20:31)
4. `method.tex` - Method/Methodology (partial read; defines the problem formulation and five confidence signals)
5. `experiments.tex` - Experiments (18,046 bytes, most recent at May 15 16:16)
6. `discussion.tex` - Discussion (4,076 bytes, May 14 20:50)
7. `conclusion.tex` - Conclusion (2,169 bytes, May 14 21:09)
8. `limitations.tex` - Limitations (1,734 bytes, May 14 21:10)
9. `appendix.tex` - Appendix (extensive analysis)

**Additional artifact directories with generated papers:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/` (various section TEX files)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/` (most recent: best, median, worst variants)

### Paper Title and Overview

**Title:** "Strong Predictors, Weak Selectors: Confidence Signals Predict but Struggle to Select in 8B-Scale Information Extraction"

**Main Contribution:** The paper identifies and analyzes the **correlation-selection gap**—where confidence signals achieve strong quality estimation (ρ up to 0.45) but fail to improve best-of-N sample selection despite substantial oracle headroom (13-18 percentage points).

### Key Experimental Results

**Datasets:**
- SciERC (551 test instances, joint NER 6 types + RE 7 types)
- CoNLL-2003 (3,453 test sentences, 4 entity types, ~91% F1)
- WNUT-17 (1,287 social media instances, 52% zero F1)

**Models:** Qwen3-8B and LLaMA-3.1-8B-Instruct (fine-tuned with LoRA)

**Five Confidence Signals Evaluated:**
1. **Log-Probability (LP)** - model-internal, per-sample signal
2. **Soft Jaccard (SJ)** - structural, instance-level
3. **Entity Voting Confidence (VC)** - structural, instance-level
4. **Exact Match Voting (EM)** - surface, instance-level
5. **Fleiss' κ (FK)** - surface, instance-level

**Quality Estimation Results (Table ref:tab:quality_estimation):**
- Best results: VC ρ=0.379 (SciERC NER), EM ρ=0.451 (CoNLL NER)
- Structural signals dominate on hard tasks (SciERC); surface/LP rise on easier tasks
- Signal rankings shift with task difficulty

**Selection Results (Table ref:tab:selection):**
- Oracle headroom: 0.778 (NER), 0.585 (RE)
- Greedy baseline: 0.645 (NER), 0.404 (RE)
- Best signal (LP): 0.647 (NER), 0.395 (RE) - **no significant improvement** (p=0.29, p-value > 0.05)

### Core Finding: The Correlation-Selection Gap

Two-layered explanation:
1. **Layer 1 (Definitional):** Four of five signals are instance-level—they assign identical scores to all candidates within an instance, making ranking impossible by construction.
2. **Layer 2 (Score Compression):** Log-probability (the only per-sample signal) is severely compressed within instances. Median LP range = 0.041 nats (IQR [0.024, 0.073]); 60.3% of instances fall below the ε=0.05 tie threshold. Where compression is mitigated (n=210 instances with above-median spread), LP selection outperforms greedy (+2.9 pp, p=0.004), confirming compression as the bottleneck.

### Notable Appendix Analyses

The appendix (sections/appendix.tex) contains extensive supporting analyses:
- Robustness across temperature, sample size N, and model families
- Calibration analysis (NER ECE 0.069-0.096; RE ECE up to 0.339)
- Diversity quantification (39-43% unique outputs on SciERC)
- Free-form ablation confirming compression is model-intrinsic, not a constrained decoding artifact
- Bootstrap confidence intervals for signal comparisons
- WNUT-17 analysis showing signal collapse at capability boundary
- Multi-seed stability (σ ≤ 0.025 on NER)
- Thinking token impact analysis (negligible)
- Cross-dataset OOD analysis (wider→narrower schema transfer succeeds; narrower→wider fails due to model capability limits)

### Limitations Section Highlights

- RE evaluation limited to SciERC (40% zero F1 instances)
- Only 8B models tested; generalization to 70B+ unknown
- No trained verifier or reward model baseline
- Single free-form ablation on one dataset with one model
- Qwen3-8B SciERC checkpoint trained with empty thinking tokens (analysis confirms negligible impact)

All the LaTeX files are now available for review. The most actively updated file is experiments.tex (May 15 16:16), indicating ongoing refinement of experimental results and tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b88f9381-9a4d-4862-8eff-817ac1bb4874",
  "isSidechain": true,
  "agentId": "a3a8f9937ba741116",
  "requestId": "req_011Cb4tUCJb2NvDdhsT8v8jc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "926aca36-a19f-4f5b-80c9-63989deadcd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "3614841f-3054-4bdc-a2e6-70a4541802e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "serialized-singing-lantern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PBHuoEPKu3YMLyjknKGDes",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 25912,
      "cache_read_input_tokens": 32686,
      "output_tokens": 1549,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25912
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1549,
          "cache_read_input_tokens": 32686,
          "cache_creation_input_tokens": 25912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25912,
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
