# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/, find the LaTeX source for: 1.

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac03697e9217c2bbf.jsonl`
- **Structured JSON:** [`d7b1736b255981416101.json`](../../sessions/d7/d7b1736b255981416101.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-24T12:59:17.978Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/, find the LaTeX source for:

1. Table 2 - "RSFT performance and inference-time evidence tax across model scales" (likely in sections/results.tex or sections/experiments.tex or similar)
2. Table 6 - "95% confidence intervals for training variance" (likely in sections/appendix.tex)

For each, show the complete table environment code and exact file path + line numbers.

Search breadth: quick

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e60fb10f-1b8e-4280-ba52-e647918c8405",
  "agentId": "ac03697e9217c2bbf",
  "type": "user",
  "uuid": "4a15cbb8-23cb-48f9-85e8-bc5cb0a049d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T12:59:20.353Z_

I'll search for these LaTeX tables in the paper directory. Let me start by exploring the structure and then locating the specific tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a15cbb8-23cb-48f9-85e8-bc5cb0a049d5",
  "isSidechain": true,
  "agentId": "ac03697e9217c2bbf",
  "requestId": "req_011CbMS9q8eiBg757VgvXSGU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cf168333-70e4-436b-9c74-beba7244c9dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VvWdzv682qaS3meoycnae3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39655,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39655,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 3 · 2026-05-24T12:59:20.618Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DdDL8FpPT5P68PjyNY8mUi`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf168333-70e4-436b-9c74-beba7244c9dc",
  "isSidechain": true,
  "agentId": "ac03697e9217c2bbf",
  "requestId": "req_011CbMS9q8eiBg757VgvXSGU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b4210b8d-03c0-4650-af71-ff9bab782cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VvWdzv682qaS3meoycnae3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39655,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 39655,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 4 · 2026-05-24T12:59:20.636Z_

<details><summary>↩ Tool result · `toolu_01DdDL8FpPT5P68PjyNY8mUi`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/acl_lualatex.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/acl_latex.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4210b8d-03c0-4650-af71-ff9bab782cc0",
  "isSidechain": true,
  "promptId": "e60fb10f-1b8e-4280-ba52-e647918c8405",
  "agentId": "ac03697e9217c2bbf",
  "type": "user",
  "uuid": "15342892-eaf8-4fa4-9786-ae48912e2982",
  "sourceToolAssistantUUID": "b4210b8d-03c0-4650-af71-ff9bab782cc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T12:59:20.954Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FJfrLCEqDg4R7J4QpCMZFs`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15342892-eaf8-4fa4-9786-ae48912e2982",
  "isSidechain": true,
  "agentId": "ac03697e9217c2bbf",
  "requestId": "req_011CbMS9q8eiBg757VgvXSGU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "55913484-d1c9-49c0-b94f-3540a37f2a2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VvWdzv682qaS3meoycnae3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39655,
      "cache_read_input_tokens": 0,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 39655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 193,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 39655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 39655,
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

_source line 6 · 2026-05-24T12:59:21.120Z_

<details><summary>↩ Tool result · `toolu_01FJfrLCEqDg4R7J4QpCMZFs`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/acl_lualatex.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/acl-style/acl_latex.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55913484-d1c9-49c0-b94f-3540a37f2a2a",
  "isSidechain": true,
  "promptId": "e60fb10f-1b8e-4280-ba52-e647918c8405",
  "agentId": "ac03697e9217c2bbf",
  "type": "user",
  "uuid": "1784cc26-4f6d-43f7-a49f-d9011c317355",
  "sourceToolAssistantUUID": "55913484-d1c9-49c0-b94f-3540a37f2a2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-24T12:59:22.938Z_

Now let me search for Table 2 and Table 6 by looking at the experiments and appendix sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1784cc26-4f6d-43f7-a49f-d9011c317355",
  "isSidechain": true,
  "agentId": "ac03697e9217c2bbf",
  "requestId": "req_011CbMSA4R7B9sbZTNWLxPA1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6fabebd6-b1ef-4b4a-82c5-d1482b603034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DDoJFv6U8ncysDbvvQ6Ewq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 39655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2027,
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

_source line 8 · 2026-05-24T12:59:23.590Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VnqovLrNRXEj1fLPn3WcrE`</summary>

```json
{
  "pattern": "Table 2|RSFT performance|inference-time evidence tax",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fabebd6-b1ef-4b4a-82c5-d1482b603034",
  "isSidechain": true,
  "agentId": "ac03697e9217c2bbf",
  "requestId": "req_011CbMSA4R7B9sbZTNWLxPA1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c8a2b1d0-4bdd-43b5-92fc-6b7dae13f89f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DDoJFv6U8ncysDbvvQ6Ewq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 39655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2027,
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

_source line 9 · 2026-05-24T12:59:23.628Z_

<details><summary>↩ Tool result · `toolu_01VnqovLrNRXEj1fLPn3WcrE`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex:8:CED and flat-NLI produce comparable RSFT performance (Rel-F1 45.63 vs.\ 45.61); stricter selection ($k{=}1$) outperforms $k{=}3$ by 1.02 Ign-F1 despite 2.96$\times$ fewer examples; CED filtering is insensitive to NLI scorer capacity (+1.10pp with DeBERTa-v3-large vs.\ v3-base, within seed noise; Appendix~\ref{sec:ablation_full}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:59:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:67:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:73:\caption{RSFT performance and inference-time evidence tax across model scales (DocRED dev Ign-F1). LLaMA-3.1-8B included for cross-family validation. Mean $\pm$ std$^{(\text{seeds})}$.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:220:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:224:\caption{SFT and RSFT performance on Re-DocRED test set (Ign-F1 \%). Dev Ign-F1 (RSFT) from Table~\ref{tab:scaling}. All test results use s42.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:268:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:272:\caption{RSFT inference-time evidence tax on Re-DocRED test set (Ign-F1 \%). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. Per-seed s42 except where noted.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8a2b1d0-4bdd-43b5-92fc-6b7dae13f89f",
  "isSidechain": true,
  "promptId": "e60fb10f-1b8e-4280-ba52-e647918c8405",
  "agentId": "ac03697e9217c2bbf",
  "type": "user",
  "uuid": "557ea09c-e5cf-4d6a-a5e5-fa80b661b68d",
  "sourceToolAssistantUUID": "c8a2b1d0-4bdd-43b5-92fc-6b7dae13f89f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T12:59:23.860Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01C22gPYHgcZWjYNMduaW69w`</summary>

```json
{
  "pattern": "Table 6|95% confidence intervals|training variance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "557ea09c-e5cf-4d6a-a5e5-fa80b661b68d",
  "isSidechain": true,
  "agentId": "ac03697e9217c2bbf",
  "requestId": "req_011CbMSA4R7B9sbZTNWLxPA1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b1a00fc-dd0f-475c-9862-d86ea2f62d71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DDoJFv6U8ncysDbvvQ6Ewq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 39655,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2027
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 267,
          "cache_read_input_tokens": 39655,
          "cache_creation_input_tokens": 2027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2027,
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

_source line 11 · 2026-05-24T12:59:23.873Z_

<details><summary>↩ Tool result · `toolu_01C22gPYHgcZWjYNMduaW69w`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex:63:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/conclusion.tex:5:RSFT improves mean extraction across all tested scales and reduces training variance at every evaluated configuration; a 1.7B RSFT model approaches 8B SFT performance at 4.7$\times$ fewer parameters.
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex:126:\caption{95\% confidence intervals for training variance ($\chi^2$ method, $N{=}3$ seeds). Compression is the ratio of SFT to RSFT point estimates (unrounded).}
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex:26:    \item \textbf{RSFT consistently reduces training variance.} NLI-based sample selection improves mean Ign-F1 across tested scales (+1.2 to +6.6pp); our 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) at 4.7$\times$ fewer parameters, enabling deployment-efficient evidence-grounded extraction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b1a00fc-dd0f-475c-9862-d86ea2f62d71",
  "isSidechain": true,
  "promptId": "e60fb10f-1b8e-4280-ba52-e647918c8405",
  "agentId": "ac03697e9217c2bbf",
  "type": "user",
  "uuid": "a99e857e-b651-47a9-8f99-0dd0119495d4",
  "sourceToolAssistantUUID": "0b1a00fc-dd0f-475c-9862-d86ea2f62d71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-24T12:59:25.303Z_

Perfect! I found references to both tables. Now let me read the specific files to get the complete table environments:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a99e857e-b651-47a9-8f99-0dd0119495d4",
  "isSidechain": true,
  "agentId": "ac03697e9217c2bbf",
  "requestId": "req_011CbMSAGJEQf2zVcheRDpGv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d0a6a73e-b7ff-43a8-b076-07d9d61565e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TNKHM9JJV34E8R3ESFTR4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1389,
      "cache_read_input_tokens": 41682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1389,
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

_source line 13 · 2026-05-24T12:59:25.729Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TbGqgryWU14vk694ujthzN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex",
  "offset": 50,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0a6a73e-b7ff-43a8-b076-07d9d61565e0",
  "isSidechain": true,
  "agentId": "ac03697e9217c2bbf",
  "requestId": "req_011CbMSAGJEQf2zVcheRDpGv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "01ccc76b-3acb-4620-9fa3-dd653a393e98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TNKHM9JJV34E8R3ESFTR4M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1389,
      "cache_read_input_tokens": 41682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1389,
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

_source line 14 · 2026-05-24T12:59:25.737Z_

<details><summary>↩ Tool result · `toolu_01TbGqgryWU14vk694ujthzN`</summary>

```text
50	\includegraphics[width=\columnwidth]{fig_spectrum.pdf}
51	\caption{Decoupling spectrum. Each method is plotted by Rel-F1 (x-axis) and Evi-F1 (y-axis). Arrows indicate training progression for DPO and GRPO bf16. Decoupled methods drift toward the upper-left.}
52	\label{fig:spectrum}
53	\end{figure}
54	
55	
56	\subsection{Scale-Dependent Evidence Tax}
57	\label{sec:scaling}
58	
59	The evidence tax, defined as Ign-F1(no-evidence) $-$ Ign-F1(with-evidence) on the development set, is scale-dependent. Under matched evaluation conditions (\texttt{max\_new\_tokens}$=$2048, format-compliant intersection; Appendix~\ref{sec:training_tax}), the training-time tax reveals a within-family capacity threshold: evidence generation benefits 1.7B ($-$5.63pp; Appendix~\ref{sec:training_tax}), where it also halves the output duplication rate (60.5\%$\to$33.0\%; Table~\ref{tab:mechanistic} in Appendix~\ref{sec:fair_subset}), but is approximately neutral at $\geq$4B (+0.25$\pm$0.47pp at 4B, $n{=}3$; +0.04pp at 8B; +0.03pp at 14B). Table~\ref{tab:scaling} and Figure~\ref{fig:evidence_tax} present RSFT performance and inference-time evidence tax across five models (Figure~\ref{fig:scaling} in Appendix). Evidence training also affects SFT seed variance in a scale-dependent manner: at 4B and 8B, with-evidence models show lower cross-seed spread than no-evidence models (25$\times$ and 1.4$\times$ compression, respectively), but at 1.7B the pattern reverses---with-evidence variance exceeds no-evidence variance, likely amplified by extreme truncation rates at this scale (Appendix~\ref{sec:training_tax}).
60	
61	RSFT navigates this capacity landscape through quality-based data selection rather than gradient pressure. Mean Ign-F1 improves across tested scales: +6.55pp at 1.7B, +1.24pp at 4B, +4.14pp at 8B, and +3.44pp at 14B (Table~\ref{tab:scaling}). RSFT from an independent SFT base (s44, Method B) achieves 51.52 Ign-F1 at 4B (+4.18pp over that base). This result confirms that RSFT gains are not contingent on a specific SFT checkpoint.
62	
63	Beyond mean performance, RSFT consistently reduces training variance (sign test: 4/4 scales, $p{=}0.0625$; $\chi^2$ CI analysis confirms non-overlapping intervals at the 1.7B scale; Cohen's $d \geq 1.79$ for 3/4 scales; Appendix~\ref{sec:variance_ci}). Three RSFT seeds from a shared SFT checkpoint yield standard deviations of 0.09pp at 1.7B, 0.51pp at 4B, and 0.50pp at 8B ($n{=}3$ each), compared to SFT cross-seed variation of 2.79pp, 3.80pp, and 3.23pp respectively. While these measure different sources of variance (SFT reflects full training runs from different random seeds; RSFT reflects additional fine-tuning from a fixed base), the practical consequence is direct: across all Qwen3 scales with $\geq$3 seeds, variance compression is 32.6$\times$ at 1.7B, 7.5$\times$ at 4B, and 6.5$\times$ at 8B (point estimates from $N{=}3$ seeds; confidence intervals are wide, Appendix~\ref{sec:variance_ci}). Per-scale Rel-F1, Evi-F1, and EDCR breakdowns appear in Table~\ref{tab:cross_detail} (Appendix~\ref{sec:scaling_details}). The 1.7B RSFT model (51.19 Ign-F1, std 0.09pp) approaches 8B SFT performance (50.19, std 3.23pp) at 4.7$\times$ fewer parameters---comparable in mean yet 36$\times$ more predictable.
64	
65	Cross-family validation on LLaMA-3.1-8B confirms these patterns. All three RSFT seeds (55.87--57.14) exceed all three SFT seeds (48.02--53.84), yielding complete pairwise seed separation (Cohen's $d{=}2.58$) and 4.6$\times$ variance compression (std 2.92pp $\to$ 0.64pp). The SFT seed lottery is starkest at s44 (48.02 Ign-F1, 24.4\% truncation, elevated Evi-F1 85\%), a degenerate outcome that RSFT eliminates entirely (s44: 55.87). This robustness extends to inference-time format changes: LLaMA SFT models evaluated without evidence at 1024 tokens suffer 38--42\% truncation with Ign-F1 collapsing to ${\sim}$0.33 (s43/s44), while RSFT models truncate only 18--19\% with stable performance (55.41$\pm$0.13pp), indicating that CED filtering selects for compact output structure.
66	
67	For RSFT models, the inference-time evidence tax (same model evaluated with vs.\ without evidence output) preserves the benefit direction at 1.7B ($-$7.75pp, confirmed with 2048-token no-evidence evaluation that rules out truncation). At 4B, where the training-time tax is approximately neutral (+0.25$\pm$0.47pp; Appendix~\ref{sec:training_tax}), the RSFT inference-time tax is similarly small (+0.94pp). At 8B, the tax reverses to a benefit ($-$0.78pp), and at 14B a benefit is observed ($-$2.78$\pm$2.49pp, two-seed mean), directionally consistent with the 8B pattern though the CI crosses zero at $n{=}2$. RSFT thus maintains or improves extraction quality with evidence across the Qwen3 family. LLaMA-3.1-8B RSFT shows a larger inference-time evidence benefit ($-$2.17$\pm$0.76pp, three-seed mean, vs.\ $-$0.78pp for Qwen3-8B), confirming that both performance gains and training reliability generalize across model families.
68	
69	The effect of RSFT on inference-time evidence dependence is heterogeneous. At 1.7B, RSFT maintains strong evidence benefit ($-$5.01$\pm$0.59pp, two-seed mean), comparable to SFT ($-$4.86pp). At 4B, RSFT introduces a mild evidence cost (+1.65$\pm$0.29pp, three-seed mean), the Qwen3 scale with the largest positive RSFT test tax. Within the Qwen3 family at $\geq$8B, RSFT approaches evidence neutrality ($-$0.91$\pm$0.74pp at 8B, three-seed mean). Cross-architecture, LLaMA-3.1-8B shows partial compression: SFT tax of $-$4.94pp reduces to $-$1.46$\pm$0.40pp (two-seed mean) under RSFT, consistent with the cross-family variation observed in SFT evidence tax (Appendix~\ref{sec:training_tax}).
70	
71	\begin{table}[t]
72	\centering
73	\caption{RSFT performance and inference-time evidence tax across model scales (DocRED dev Ign-F1). LLaMA-3.1-8B included for cross-family validation. Mean $\pm$ std$^{(\text{seeds})}$.}
74	\label{tab:scaling}
75	\small
76	\resizebox{\columnwidth}{!}{%
77	\begin{tabular}{lcccc}
78	\toprule
79	\textbf{Model} & \textbf{SFT w/ evi} & \textbf{RSFT} & \textbf{RSFT Tax}$^\dagger$ & \textbf{RSFT Gain} \\
80	\midrule
81	Qwen3-1.7B & 44.64{\scriptsize$\pm$2.79}$^{(3)}$ & 51.19{\scriptsize$\pm$0.09}$^{(3)}$ & $-$7.75 & +6.55 \\
82	Qwen3-4B & 43.58{\scriptsize$\pm$3.80}$^{(3)}$ & 44.82{\scriptsize$\pm$0.51}$^{(3)}$ & +0.94 & +1.24 \\
83	Qwen3-8B & 50.19{\scriptsize$\pm$3.23}$^{(3)}$ & 54.33{\scriptsize$\pm$0.50}$^{(3)}$ & $-$0.78 & +4.14 \\
84	Qwen3-14B & 55.07$^{(1)}$ & 58.51{\scriptsize$\pm$0.50}$^{(2)}$ & $-$2.78{\scriptsize$\pm$2.49}$^{(2)}$ & +3.44 \\
85	LLaMA-3.1-8B & 51.09{\scriptsize$\pm$2.92}$^{(3)}$ & 56.54{\scriptsize$\pm$0.64}$^{(3)}$ & $-$2.17{\scriptsize$\pm$0.76}$^{(3)}$ & +5.45 \\
86	\bottomrule
87	\end{tabular}%
88	}
89	\vspace{-2mm}
90	{\raggedright\footnotesize $^\dagger$Inference-time: same RSFT model with vs.\ without evidence output. No-evi eval uses \texttt{max\_new\_tokens}$=$2048; with-evi eval uses 1024 (1.7B uses 2048 for both). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. Seeds: 1.7B s42; 4B Method B s44; 8B s42; 14B two-seed mean; LLaMA three-seed mean. Training-time tax (matched@2048 fair evaluation) in Appendix~\ref{sec:training_tax}.\par}
91	\end{table}
92	
93	\begin{figure}[t]
94	\centering
95	\includegraphics[width=\columnwidth]{fig_evidence_tax.pdf}
96	\vspace{-2mm}
97	\caption{Inference-time evidence tax across model scales (RSFT models, Re-DocRED test). Negative values indicate evidence \emph{benefits} extraction. Error bars show $\pm$1 std (all scales have $\geq$2 seeds).}
98	\label{fig:evidence_tax}
99	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01ccc76b-3acb-4620-9fa3-dd653a393e98",
  "isSidechain": true,
  "promptId": "e60fb10f-1b8e-4280-ba52-e647918c8405",
  "agentId": "ac03697e9217c2bbf",
  "type": "user",
  "uuid": "12fed439-f559-4fc6-ba6d-008bea40edaf",
  "sourceToolAssistantUUID": "01ccc76b-3acb-4620-9fa3-dd653a393e98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T12:59:26.069Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D6xKUEjUnXRC4EH1uaCsy2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex",
  "offset": 110,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12fed439-f559-4fc6-ba6d-008bea40edaf",
  "isSidechain": true,
  "agentId": "ac03697e9217c2bbf",
  "requestId": "req_011CbMSAGJEQf2zVcheRDpGv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "008a7cd4-612a-4322-992a-55697d33ede2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TNKHM9JJV34E8R3ESFTR4M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1389,
      "cache_read_input_tokens": 41682,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1389
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 254,
          "cache_read_input_tokens": 41682,
          "cache_creation_input_tokens": 1389,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1389,
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

_source line 16 · 2026-05-24T12:59:26.077Z_

<details><summary>↩ Tool result · `toolu_01D6xKUEjUnXRC4EH1uaCsy2`</summary>

```text
110	
111	\begin{figure}[t]
112	\centering
113	\includegraphics[width=\columnwidth]{fig_scaling.pdf}
114	\caption{Evidence tax and RSFT gain across model scales. Bar heights show Ign-F1 for SFT with evidence (s42), SFT without evidence (s42), and RSFT (mean). The gap between no-evidence and SFT bars reverses direction between 1.7B and 4B, revealing the scale-dependent evidence tax. RSFT consistently narrows the gap toward the no-evidence upper bound.}
115	\label{fig:scaling}
116	\end{figure}
117	
118	
119	\section{Variance Compression Confidence Intervals}
120	\label{sec:variance_ci}
121	
122	Table~\ref{tab:variance_ci} reports 95\% confidence intervals for SFT and RSFT standard deviations using the $\chi^2$ distribution ($N{=}3$ seeds per configuration). At 1.7B, the confidence intervals are fully non-overlapping (SFT lower bound 1.45pp $>$ RSFT upper bound 0.54pp), providing the strongest evidence for variance compression. At the remaining three scales, intervals overlap but point estimates are consistently in the same direction (SFT std $>$ RSFT std at all four scales; sign test $p = 0.0625$, one-sided binomial, $n = 4$, underpowered). Cohen's $d$ ranges from 0.46 (4B) to 3.31 (1.7B), with 1.7B and LLaMA-8B showing large effect sizes ($d > 2.5$).
123	
124	\begin{table}[t]
125	\centering
126	\caption{95\% confidence intervals for training variance ($\chi^2$ method, $N{=}3$ seeds). Compression is the ratio of SFT to RSFT point estimates (unrounded).}
127	\label{tab:variance_ci}
128	\small
129	\resizebox{\columnwidth}{!}{%
130	\begin{tabular}{lcccccc}
131	\toprule
132	\textbf{Scale} & \textbf{SFT std} & \textbf{SFT 95\% CI} & \textbf{RSFT std} & \textbf{RSFT 95\% CI} & \textbf{Compr.} & \textbf{Cohen's $d$} \\
133	\midrule
134	Qwen3-1.7B & 2.79 & [1.45, 17.55] & 0.09 & [0.04, 0.54] & 32.6$\times$ & 3.31 \\
135	Qwen3-4B & 3.80 & [1.98, 23.89] & 0.51 & [0.27, 3.21] & 7.5$\times$ & 0.46 \\
136	Qwen3-8B & 3.23 & [1.68, 20.31] & 0.50 & [0.26, 3.15] & 6.5$\times$ & 1.79 \\
137	LLaMA-3.1-8B & 2.92 & [1.52, 18.37] & 0.64 & [0.33, 4.01] & 4.6$\times$ & 2.58 \\
138	\bottomrule
139	\end{tabular}%
140	}
141	\vspace{-2mm}
142	{\raggedright\footnotesize Sign test: $p = 0.0625$ (one-sided binomial, $n = 4$; underpowered). The consistent direction (4/4 SFT $>$ RSFT), non-overlapping CIs at 1.7B, and large Cohen's $d$ at 1.7B and LLaMA provide practical evidence for variance compression despite limited statistical power from $N{=}3$ seeds.\par}
143	\end{table}
144	
145	
146	\section{Controlled Evaluation Subset}
147	\label{sec:fair_subset}
148	
149	The 1.7B evidence tax comparison (\S\ref{sec:scaling}) is confounded by differential truncation rates. At \texttt{max\_new\_tokens}$=$1024, the no-evidence model truncates 50.9\% of outputs (501/985 documents) versus 31.9\% (314/985) for the evidence model. To address this, we adopt a matched@2048 fair evaluation: both configurations are evaluated at \texttt{max\_new\_tokens}$=$2048, and the tax is computed on the intersection of documents where both produce format-compliant output. This yields 971/985 fair-subset documents, with a tax of $-$5.63pp (s42), confirming a genuine 1.7B evidence benefit. As additional validation, a stricter controlled subset at @1024 (excluding truncated or repetitive outputs; 442/985 documents) yields $-$6.2pp, with the stronger benefit attributable to the more aggressive filtering.
150	
151	Table~\ref{tab:mechanistic} provides a mechanistic breakdown across three scales (evaluated at @1024). Output duplication rate (fraction of documents containing $\geq$3 repeated triples or unique/total $< 0.5$) declines monotonically with scale for both training configurations, but the gap between no-evidence and with-evidence models narrows from 27.5pp at 1.7B to 3.7pp at 8B. This pattern supports the implicit regularization hypothesis: evidence generation forces smaller models to attend to supporting context, reducing degenerate repetition. At 4B, duplication is already moderate (31.1\% with evidence), so the regularization benefit diminishes; under matched@2048 evaluation, the 4B training-time tax is approximately neutral (+0.25$\pm$0.47pp, three-seed mean). The truncation asymmetry reverses across scales: at 1.7B the no-evidence model truncates 19pp more often; at 8B the evidence model truncates 9pp more often due to the longer output format.
152	
153	\begin{table}[t]
154	\centering
155	\caption{Mechanistic breakdown of output quality across scales. Duplication rate: fraction of documents with degenerate outputs. Truncation $\Delta$: no-evidence rate minus with-evidence rate (positive means no-evidence truncates more).}
156	\label{tab:mechanistic}
157	\small
158	\begin{tabular}{lccccc}
159	\toprule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "008a7cd4-612a-4322-992a-55697d33ede2",
  "isSidechain": true,
  "promptId": "e60fb10f-1b8e-4280-ba52-e647918c8405",
  "agentId": "ac03697e9217c2bbf",
  "type": "user",
  "uuid": "291b113f-3f93-4a36-8e52-d4939c476a6a",
  "sourceToolAssistantUUID": "008a7cd4-612a-4322-992a-55697d33ede2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-24T12:59:42.508Z_

Perfect! I have found both tables. Let me provide you with the complete information:

## Table 2 - "RSFT performance and inference-time evidence tax across model scales"

**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex`

**Line numbers:** 71-91

**Complete table environment code:**

```latex
\begin{table}[t]
\centering
\caption{RSFT performance and inference-time evidence tax across model scales (DocRED dev Ign-F1). LLaMA-3.1-8B included for cross-family validation. Mean $\pm$ std$^{(\text{seeds})}$.}
\label{tab:scaling}
\small
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lcccc}
\toprule
\textbf{Model} & \textbf{SFT w/ evi} & \textbf{RSFT} & \textbf{RSFT Tax}$^\dagger$ & \textbf{RSFT Gain} \\
\midrule
Qwen3-1.7B & 44.64{\scriptsize$\pm$2.79}$^{(3)}$ & 51.19{\scriptsize$\pm$0.09}$^{(3)}$ & $-$7.75 & +6.55 \\
Qwen3-4B & 43.58{\scriptsize$\pm$3.80}$^{(3)}$ & 44.82{\scriptsize$\pm$0.51}$^{(3)}$ & +0.94 & +1.24 \\
Qwen3-8B & 50.19{\scriptsize$\pm$3.23}$^{(3)}$ & 54.33{\scriptsize$\pm$0.50}$^{(3)}$ & $-$0.78 & +4.14 \\
Qwen3-14B & 55.07$^{(1)}$ & 58.51{\scriptsize$\pm$0.50}$^{(2)}$ & $-$2.78{\scriptsize$\pm$2.49}$^{(2)}$ & +3.44 \\
LLaMA-3.1-8B & 51.09{\scriptsize$\pm$2.92}$^{(3)}$ & 56.54{\scriptsize$\pm$0.64}$^{(3)}$ & $-$2.17{\scriptsize$\pm$0.76}$^{(3)}$ & +5.45 \\
\bottomrule
\end{tabular}%
}
\vspace{-2mm}
{\raggedright\footnotesize $^\dagger$Inference-time: same RSFT model with vs.\ without evidence output. No-evi eval uses \texttt{max\_new\_tokens}$=$2048; with-evi eval uses 1024 (1.7B uses 2048 for both). Tax $=$ no-evi $-$ with-evi; positive $=$ cost. Seeds: 1.7B s42; 4B Method B s44; 8B s42; 14B two-seed mean; LLaMA three-seed mean. Training-time tax (matched@2048 fair evaluation) in Appendix~\ref{sec:training_tax}.\par}
\end{table}
```

---

## Table 6 - "95% confidence intervals for training variance"

**File path:** `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/appendix.tex`

**Line numbers:** 124-143

**Complete table environment code:**

```latex
\begin{table}[t]
\centering
\caption{95\% confidence intervals for training variance ($\chi^2$ method, $N{=}3$ seeds). Compression is the ratio of SFT to RSFT point estimates (unrounded).}
\label{tab:variance_ci}
\small
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lcccccc}
\toprule
\textbf{Scale} & \textbf{SFT std} & \textbf{SFT 95\% CI} & \textbf{RSFT std} & \textbf{RSFT 95\% CI} & \textbf{Compr.} & \textbf{Cohen's $d$} \\
\midrule
Qwen3-1.7B & 2.79 & [1.45, 17.55] & 0.09 & [0.04, 0.54] & 32.6$\times$ & 3.31 \\
Qwen3-4B & 3.80 & [1.98, 23.89] & 0.51 & [0.27, 3.21] & 7.5$\times$ & 0.46 \\
Qwen3-8B & 3.23 & [1.68, 20.31] & 0.50 & [0.26, 3.15] & 6.5$\times$ & 1.79 \\
LLaMA-3.1-8B & 2.92 & [1.52, 18.37] & 0.64 & [0.33, 4.01] & 4.6$\times$ & 2.58 \\
\bottomrule
\end{tabular}%
}
\vspace{-2mm}
{\raggedright\footnotesize Sign test: $p = 0.0625$ (one-sided binomial, $n = 4$; underpowered). The consistent direction (4/4 SFT $>$ RSFT), non-overlapping CIs at 1.7B, and large Cohen's $d$ at 1.7B and LLaMA provide practical evidence for variance compression despite limited statistical power from $N{=}3$ seeds.\par}
\end{table}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "291b113f-3f93-4a36-8e52-d4939c476a6a",
  "isSidechain": true,
  "agentId": "ac03697e9217c2bbf",
  "requestId": "req_011CbMSARgYBcytqC1dnsUvq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "81b408f1-239b-4bdb-981d-7781a64f6f5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/director_5afd7c17",
  "sessionId": "d27ae920-d2f9-42f2-ac0a-1d3743220d74",
  "version": "2.1.126",
  "gitBranch": "main",
  "slug": "delegated-munching-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N4NbKsacQ1ZVEdUYSC5UZ3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4886,
      "cache_read_input_tokens": 43071,
      "output_tokens": 1526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1526,
          "cache_read_input_tokens": 43071,
          "cache_creation_input_tokens": 4886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4886,
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
