# Research conversation: In the LaTeX paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/, f

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa73c4d5ac0f1bbfe.jsonl`
- **Structured JSON:** [`595dab07e35470c58d29.json`](../../sessions/59/595dab07e35470c58d29.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-24T19:48:17.918Z_

In the LaTeX paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/, find ALL \begin{figure} and \begin{table} blocks in the main text files (introduction.tex, method.tex, related_work.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex). For each one, report:
1. The file and line number
2. The label (from \label{})
3. The current placement specifier (e.g. [t], [h], [ht], etc.)
4. Whether it's figure or figure* (full-width) or table

Search breadth: very thorough

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "dc18e03d-3ea7-4f2f-9c5d-e1713073cd6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T19:48:19.603Z_

I'll help you find all figure and table blocks in the LaTeX paper. Let me start by exploring the paper directory structure and then systematically search through each file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc18e03d-3ea7-4f2f-9c5d-e1713073cd6b",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyLmjvRDgzCPknsSoe7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04b673e8-9e7f-4dac-ad8c-6e5174d47f97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X8PvTNYK4pBq3QrRiim4fy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35775,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35775,
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

_source line 3 · 2026-05-24T19:48:19.777Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011EPH7s7df6ohPqBLmdHYuv`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04b673e8-9e7f-4dac-ad8c-6e5174d47f97",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyLmjvRDgzCPknsSoe7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "37e54b6b-b8d0-4d09-8566-9881beb766e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X8PvTNYK4pBq3QrRiim4fy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35775,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 35775
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 35775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 35775,
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

_source line 4 · 2026-05-24T19:48:19.994Z_

<details><summary>↩ Tool result · `toolu_011EPH7s7df6ohPqBLmdHYuv`</summary>

```text
total 4344
drwxr-xr-x 4 ubuntu ubuntu    4096 May 24 18:37 .
drwxr-xr-x 4 ubuntu ubuntu    4096 May 24 19:43 ..
drwxr-xr-x 2 ubuntu ubuntu    4096 May 24 17:01 _pdf_images
-rw-r--r-- 1 ubuntu ubuntu    1552 May 24 18:35 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu   11615 May 17 09:40 acl.sty
-rw-r--r-- 1 ubuntu ubuntu   45186 May 17 09:40 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu   46436 May 24 16:59 appendix.tex
-rw-r--r-- 1 ubuntu ubuntu    1401 May 24 16:27 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu       0 May 23 12:27 ethics.tex
-rw-r--r-- 1 ubuntu ubuntu    4366 May 24 18:36 experimental_setup.tex
drwxr-xr-x 7 ubuntu ubuntu    4096 May 24 11:18 figures
-rw-r--r-- 1 ubuntu ubuntu    3894 May 24 18:37 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu     629 May 24 16:26 limitations.tex
-rw-r--r-- 1 ubuntu ubuntu   63372 May 24 18:37 main.aux
-rw-r--r-- 1 ubuntu ubuntu   23478 May 24 18:37 main.bbl
-rw-r--r-- 1 ubuntu ubuntu    1404 May 24 18:37 main.blg
-rw-r--r-- 1 ubuntu ubuntu   32422 May 24 18:37 main.fdb_latexmk
-rw-r--r-- 1 ubuntu ubuntu   34868 May 24 18:37 main.fls
-rw-r--r-- 1 ubuntu ubuntu   56072 May 24 18:37 main.log
-rw-r--r-- 1 ubuntu ubuntu    9109 May 24 18:37 main.out
-rw-r--r-- 1 ubuntu ubuntu 3995555 May 24 18:37 main.pdf
-rw-r--r-- 1 ubuntu ubuntu     838 May 23 06:55 main.tex
-rw-r--r-- 1 ubuntu ubuntu    9441 May 24 18:37 method.tex
-rw-r--r-- 1 ubuntu ubuntu   25794 May 24 12:03 references.bib
-rw-r--r-- 1 ubuntu ubuntu    3676 May 24 18:36 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu   15371 May 24 18:37 results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37e54b6b-b8d0-4d09-8566-9881beb766e2",
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "d9bda3d0-272f-4dec-8610-ce55585e17d4",
  "sourceToolAssistantUUID": "37e54b6b-b8d0-4d09-8566-9881beb766e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-24T19:48:22.039Z_

Now let me search through all the specified tex files for \begin{figure}, \begin{figure*}, and \begin{table} blocks. I'll use grep with context to capture the placement specifiers and labels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9bda3d0-272f-4dec-8610-ce55585e17d4",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyLvqs1JTG3vLgbQvWP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e9a22dfc-3d77-4422-8587-71708f5b7cf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jy3ej2SSECWsiAR4GvsXpF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1750,
      "cache_read_input_tokens": 35775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1750,
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

_source line 6 · 2026-05-24T19:48:23.575Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JUXpybbi4j8U9xQRnvvrr9`</summary>

```json
{
  "pattern": "\\\\begin\\{(figure\\*?|table)\\}(\\[.*?\\])?",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "glob": "introduction.tex|method.tex|related_work.tex|experimental_setup.tex|results.tex|conclusion.tex|limitations.tex",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9a22dfc-3d77-4422-8587-71708f5b7cf5",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyLvqs1JTG3vLgbQvWP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b4420669-22c4-4b7d-bb93-e93abc293cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jy3ej2SSECWsiAR4GvsXpF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1750,
      "cache_read_input_tokens": 35775,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1750
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 250,
          "cache_read_input_tokens": 35775,
          "cache_creation_input_tokens": 1750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1750,
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

_source line 7 · 2026-05-24T19:48:23.603Z_

<details><summary>↩ Tool result · `toolu_01JUXpybbi4j8U9xQRnvvrr9`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4420669-22c4-4b7d-bb93-e93abc293cb1",
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "82446ebd-a360-402d-ad00-4bee3986d720",
  "sourceToolAssistantUUID": "b4420669-22c4-4b7d-bb93-e93abc293cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-24T19:48:25.362Z_

Let me try a simpler pattern to search for figure and table blocks:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82446ebd-a360-402d-ad00-4bee3986d720",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMDMnt2V7nacugFszk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "25c176db-c1e8-48cc-9bb7-d5cdbbc72e52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KgWuoMyKKRZ51wQ2W6DzkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 37525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 265,
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

_source line 9 · 2026-05-24T19:48:25.957Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015DsBABh4hX45sqK3DR9XRE`</summary>

```json
{
  "pattern": "\\\\begin\\{figure",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "glob": "introduction.tex|method.tex|related_work.tex|experimental_setup.tex|results.tex|conclusion.tex|limitations.tex",
  "output_mode": "content",
  "context": 5,
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25c176db-c1e8-48cc-9bb7-d5cdbbc72e52",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMDMnt2V7nacugFszk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "604fe99b-b7ed-44cf-8a59-1e3e85b529af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KgWuoMyKKRZ51wQ2W6DzkD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 37525,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 265
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 224,
          "cache_read_input_tokens": 37525,
          "cache_creation_input_tokens": 265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 265,
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

_source line 10 · 2026-05-24T19:48:26.032Z_

<details><summary>↩ Tool result · `toolu_015DsBABh4hX45sqK3DR9XRE`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "604fe99b-b7ed-44cf-8a59-1e3e85b529af",
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "bed0eaec-3eef-4927-a296-69731a673374",
  "sourceToolAssistantUUID": "604fe99b-b7ed-44cf-8a59-1e3e85b529af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-24T19:48:27.712Z_

Let me read the files directly to see their content and structure:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bed0eaec-3eef-4927-a296-69731a673374",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMNf8mB5sjxvQ9F2vq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "25a5b2ff-c2cf-44e3-b491-6e46625dfdf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016oMBANLGYgN26BybjKLB8P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 37790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 239,
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

_source line 12 · 2026-05-24T19:48:27.943Z_

<details open><summary>🔧 Tool call — Read · `toolu_0144rg9e6swpEDejo32JyGqg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25a5b2ff-c2cf-44e3-b491-6e46625dfdf0",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMNf8mB5sjxvQ9F2vq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d5d1398-b83c-4580-9d85-d1ac0e7ab1e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016oMBANLGYgN26BybjKLB8P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 37790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 239,
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

### Tool result

_source line 13 · 2026-05-24T19:48:27.960Z_

<details><summary>↩ Tool result · `toolu_0144rg9e6swpEDejo32JyGqg`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models (LLMs), yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled supervised fine-tuning (SFT) injection (Low-Rank Adaptation [LoRA], five dosage levels) into six models spanning five independent families from five labs (Alibaba, Microsoft, Allen AI, Google, TII) and discover a spectrum of dose-response patterns (Figure~\ref{fig:dose_response})---from immunity (Phi-4, $\pm$0.5pp) and benefit ($+$3--4pp, three families) to collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{figures/fig_dose_response.pdf}
10	\caption{MMLU accuracy vs.\ contamination dosage (5-shot, seed$=$42; LLaMA-3.1 at seed$=$0). Immune and Benefit replicate across families; Collapse and V-recovery are preliminary (Qwen2.5-specific). Cross-seed stability in Table~\ref{tab:cross_seed}.}
11	\label{fig:dose_response}
12	\end{figure}
13	
14	Across six models, three lower-baseline models benefit ($+$3.2 to $+$4.2pp), one is immune (Phi-4), and the remaining two (both Qwen2.5) show harm---with the 14B model 5$\times$ more fragile than 7B. These effects are benchmark-conditional: the same model can collapse on MMLU ($-$9.4pp) yet gain on GSM8K ($+$13pp). ContamCal, our diagnostic framework combining multi-signal exposure mapping with contamination-augmented Item Response Theory (IRT; 2PL+$\gamma_k$), enables this characterization.
15	
16	Our contributions:
17	\begin{enumerate}
18	    \item \textbf{Dose-response profiles with cross-seed and cross-benchmark validation.} Controlled injection across five families reveals two replicated patterns (Immune, Benefit) and two preliminary Qwen2.5-specific patterns (Collapse, V-recovery). Out-of-sample validation on LLaMA-3.1-8B confirms generalizability. Cross-benchmark transfer reveals directional reversal on GSM8K for three families. Multi-seed evaluation ($n\!=\!3$) shows direction is reproducible but magnitude is seed-sensitive.
19	    \item \textbf{Domain-level contamination diagnosis via IRT.} ContamCal embeds multi-signal Reciprocal Rank Fusion (RRF) exposure scores in a contamination-augmented IRT model (2PL+$\gamma$)---an application of standard explanatory IRT \citep{deboeck_2004_explanatory_irt} to LLM contamination---enabling domain-level diagnosis with credible intervals. Domain analysis reveals opposing contamination directions (Social Sciences $\gamma_d < 0$, STEM $\gamma_d > 0$) invisible to aggregate scoring. No item-specific memorization is detected via difference-in-differences (minimum detectable effect size [MDES] 1.25--2.05pp).
20	    \item \textbf{Diagnostic pipeline requirements and signal failure.} Min-K\%++ \citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (paired Cohen's $d = -1.98$ at d100). RRF-based multi-signal fusion is essential: a single-signal pipeline produces severe model misfit (posterior predictive $p$-value [PPP] $< 0.001$). Simulation establishes $\gamma$ recovery requires $J \geq 50$ at area under the curve (AUC) $\geq 0.55$, above current practice ($J = 8$--$30$).
21	\end{enumerate}
22	
23	\noindent Code and data are available at \url{https://github.com/anonymous-nlp-2026-2/contamcal-irt-calibration}.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d5d1398-b83c-4580-9d85-d1ac0e7ab1e5",
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "5c3537b8-d1dc-40ed-a113-fd8e3461d107",
  "sourceToolAssistantUUID": "5d5d1398-b83c-4580-9d85-d1ac0e7ab1e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T19:48:28.172Z_

<details open><summary>🔧 Tool call — Read · `toolu_011KEMHcs4fAdwvfS9eP4xKL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c3537b8-d1dc-40ed-a113-fd8e3461d107",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMNf8mB5sjxvQ9F2vq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "310fcfe4-9b2b-4e8d-9eb8-44147cf75bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016oMBANLGYgN26BybjKLB8P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 37790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 239,
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

### Tool result

_source line 15 · 2026-05-24T19:48:28.184Z_

<details><summary>↩ Tool result · `toolu_011KEMHcs4fAdwvfS9eP4xKL`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.95\textwidth]{figures/fig_pipeline.pdf}
7	\caption{ContamCal three-stage pipeline. Stage~1 fuses training-free detection signals into per-item exposure scores via Reciprocal Rank Fusion. Stage~2 embeds these scores in a contamination-augmented 2PL IRT model, recovering clean ability estimates with credible intervals. Stage~3 classifies the resulting dose-response trajectories into canonical patterns.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	ContamCal operates in three stages (Figure~\ref{fig:pipeline}): Stage~1 estimates per-item contamination exposure via training-free signal fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to recover clean ability estimates with credible intervals; Stage~3 classifies dose-response trajectories into canonical patterns.
12	
13	\subsection{Problem Formulation}
14	\label{sec:formulation}
15	
16	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
17	
18	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{de_ayala_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
19	
20	\subsection{Stage 1: Multi-Signal Exposure Mapping}
21	\label{sec:stage1}
22	
23	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \citep{kadavath2022}; concurrent work by \citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\mathcal{S} = \{\text{S1, S2, S4}\}$) and applies to any benchmark without auxiliary data. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_failure}. Item-level classification performance of the exposure scores is reported in Appendix~\ref{sec:sij_classification}.
24	
25	We aggregate signals via Reciprocal Rank Fusion \citep[RRF;][]{cormack_2009_rrf}:
26	\begin{equation}
27	\label{eq:rrf}
28	    e_{ij} = \sum_{s \in \mathcal{S}} \frac{1}{\kappa + r_{s}(i)},
29	\end{equation}
30	where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\kappa=60$ is the standard RRF smoothing constant, robust to near-random component signals, and $|\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to $e_{ij} \in [0,1]$; the distribution is highly right-skewed (mean 0.041).
31	
32	\subsection{Stage 2: Contamination-Augmented IRT}
33	\label{sec:stage2}
34	
35	\paragraph{Primary model: 2PL+$\gamma$.}
36	Our primary specification augments the two-parameter logistic (2PL) model \citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:
37	\begin{equation}
38	\label{eq:2pl_gamma}
39	    P(y_{ijk} = 1) = \sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
40	\end{equation}
41	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \in \mathbb{R}$ is item difficulty, $\theta_j$ is model ability, and $\gamma_k$ is the scalar contamination effect for benchmark~$k$ ($\gamma$ without subscript denotes the pooled effect; $\gamma_d$ denotes per-domain effects, \S\ref{sec:domain_differential}). Each benchmark is fitted independently; when finer-grained diagnosis is needed, we replace $\gamma_k$ with per-domain effects $\gamma_d$ ($d=1,\ldots,D$), fitting Eq.~\eqref{eq:2pl_gamma} separately for each cognitive domain within a benchmark (\S\ref{sec:domain_differential}).
42	
43	We place $\gamma_k$ outside the item discrimination bracket, modeling contamination as a fixed logit shift \citep{de_ayala_2009_irt} rather than the uniform DIF form that would scale contamination effects with item discrimination. A comparison with the uniform DIF alternative ($\gamma$ inside the discrimination bracket) yields equivalent model fit (Appendix~\ref{sec:dif_comparison}). For MC-format benchmarks, a four-parameter logistic (4PL) extension adds guessing and ceiling asymptotes (Appendix~\ref{sec:4pl_details}); this requires $J \geq 16$ and is not used in domain-level analyses ($J = 13$).
44	
45	\paragraph{Inference.}
46	We perform Bayesian inference via the No-U-Turn Sampler (NUTS) \citep{hoffman2014} in Stan \citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_k \sim \mathcal{N}(0,1)$. At $J=16$, the $\gamma$ posterior is sensitive to the prior (up to 2.6$\times$ shift across reasonable alternatives; Appendix~\ref{sec:prior_sensitivity}); we therefore treat $\gamma$ estimates as directional indicators rather than precise effect sizes. Convergence requires split-$\hat{R} < 1.01$ and bulk effective sample size (ESS)~$> 400$ for all parameters. Model fit is assessed via the posterior predictive $p$-value (PPP), where values near 0.5 indicate adequate fit.
47	
48	\paragraph{Calibrated score.}
49	The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:
50	\begin{equation}
51	\label{eq:calibrated}
52	    \text{Acc}_{j}^{\text{cal}} = \frac{1}{I_k} \sum_{i=1}^{I_k}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)\right],
53	\end{equation}
54	with credible intervals from posterior quantiles. In practice, we average $\sigma(a_i(\theta_j - b_i))$ over posterior draws with $e_{ij}=0$; the spread of draws yields the credible interval. Models with noisier exposure signals receive wider intervals by construction.
55	
56	\paragraph{Identifiability.}
57	\label{sec:fisher}
58	\label{sec:value_decomposition}
59	The reliability of $\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\geq$0.55 with $J \geq 50$ (Appendix~\ref{sec:identifiability_appendix}; data-generating process (DGP) robustness in Appendix~\ref{sec:threshold_dgp}). Empirically, exposure scores $e_{ij}$ and item difficulty $b_i$ are near-orthogonal (Pearson $|r|<0.13$, $R^2<0.014$ across benchmarks), so $\gamma$ is identified from dosage-induced variation rather than confounded with difficulty. Eq.~\eqref{eq:calibrated} depends on $\theta_j$, not $\gamma$ directly, predicting that vanilla 2PL ($\gamma\!=\!0$) achieves comparable calibration to 2PL+$\gamma$, with $\gamma_k$ serving diagnosis rather than calibration (\S\ref{sec:calibration_results}).
60	
61	\subsection{Dose-Response Profile Classification}
62	\label{sec:classification}
63	
64	Independent of the IRT calibration pipeline, we classify dose-response profiles via a deterministic decision tree (Algorithm~\ref{alg:profile-classification} in Appendix~\ref{sec:classification_algorithm}) parameterized by noise threshold $\tau{=}2$\,pp and severity threshold $\sigma{=}5$\,pp, drawing on pharmacological dose-response modeling \citep{hill1910aggregation,ritz2015dose}. The tree branches on the end-to-end accuracy shift $\Delta{=}a_{100}{-}a_0$, mid-dosage minimum, and maximum mid-trajectory deviation to assign one of four patterns: \textsc{Immune}, \textsc{Collapse}, \textsc{V-recovery}, or \textsc{Benefit}. All thresholds are explicit and adjustable; a 30-combination $(\tau, \sigma)$ grid sweep confirms all families are stable (180/180 pairs; Appendix~\ref{sec:classification_sensitivity}). Family-level classification uses \emph{direction} as the primary criterion (\S\ref{sec:cross_seed}): Immune if the bootstrap CI of the cross-seed mean $\Delta$(d100) includes zero and $|\text{mean}~\Delta| < \tau$; Borderline if the CI includes zero but $|\text{mean}~\Delta| \geq \tau$; otherwise Harm/Benefit by sign. Parametric model selection (Appendix~\ref{sec:parametric_dr}) confirms these classifications for extreme effects but lacks power at $n\!=\!3$ seeds, motivating the rule-based approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "310fcfe4-9b2b-4e8d-9eb8-44147cf75bba",
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "9eea17ac-cb8d-4bfd-b4bd-34054a8a62cb",
  "sourceToolAssistantUUID": "310fcfe4-9b2b-4e8d-9eb8-44147cf75bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T19:48:28.386Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RukbtswNH9WxG4KBALCjLm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9eea17ac-cb8d-4bfd-b4bd-34054a8a62cb",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMNf8mB5sjxvQ9F2vq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "063df1a9-697c-4d0c-82ac-421ff445089c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016oMBANLGYgN26BybjKLB8P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 37790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 239,
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

### Tool result

_source line 17 · 2026-05-24T19:48:28.395Z_

<details><summary>↩ Tool result · `toolu_01RukbtswNH9WxG4KBALCjLm`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Contamination detection.}
4	Detection methods flag contaminated items via token-level surprisal \citep{shi_2023_minkprob,zhang_2024_minkpp}, accuracy gaps on paraphrases or rephrased items \citep{dekoninck2024constat,yang2023rethinking}, kernel divergence \citep{choi_2025_kds}, completion probes \citep{dong_2024_cdd,golchin2024time}, and parallel test sets \citep{zhang_2024_gsm1k}; see \citet{chen2025benchmarking,singh2024evaluation,sainz2023nlp} for surveys. \citet{balloccu2024leak} document contamination malpractices in closed-source LLMs; \citet{bordt2025forget} argue that contamination effects are often negligible in practice. Earlier work characterized contamination as memorization \citep{carlini2023quantifying,magar_2022_contamination,li_2024_task_contamination,xu_2024_leakage}; \citet{tao2025detecting} and \citet{kocyigit2025impact} address RL post-training. These methods perform binary classification without quantifying effect sizes.
5	
6	\paragraph{Contamination quantification and mitigation.}
7	On mitigation, \citet{sun2025emperor} find none of twenty approaches reliably restores clean performance; DCR \citep{xu2025dcr} estimates decontaminated scores but without uncertainty quantification. ContamCal consumes detection signals as inputs and produces calibrated ability with credible intervals. Three concurrent lines of work directly address contamination quantification. \citet{han2026quantifying} apply observational differential item functioning (DIF) to detect contamination without controlled dosage, achieving detection but not dose-response profiling. \citet{schaeffer2026causally} perform controlled pretraining-stage injection with larger seed counts ($n\!=\!10$), establishing causal contamination effects at the pretraining level; our $n\!=\!3$ seed design trades statistical power for broader family coverage. Our work complements both: like Schaeffer et al., we use controlled injection for causal identification, but at the SFT stage with precise dosage control; like Han et al., we employ IRT-based modeling, but with ground-truth contamination labels enabling dose-response characterization.
8	
9	\paragraph{IRT for LLM evaluation.}
10	Item Response Theory \citep{lord_1980_irt,hambleton_1991_irt} has gained traction for LLM evaluation \citep{liang_2023_helm}: \citet{rodriguez2021evaluation}, TinyBenchmarks \citep{polo_2024_tinybenchmarks}, Growing Pains \citep{habba_2025_growing_pains}, HiBayES \citep{luettgau_2025_hibayes}, PSN-IRT \citep{zhou_2025_psnirt}; see \citet{lalor_2024_irt_nlp} for a tutorial and \citet{gu2024olmes} for evaluation standardization. Most directly related, \citet{han2026quantifying} apply group-based DIF \citep{holland_1993_dif} to quantify item-level contamination effects. ContamCal differs by using continuous exposure covariates (explanatory DIF; \citealp{deboeck_2004_explanatory_irt}), providing calibrated ability with credible intervals, and domain-level diagnosis ($\gamma_d$); the approaches are complementary (item-level DIF for benchmark curation, model-level calibration for score interpretation). Our $\gamma$ parameter is formally an instance of explanatory DIF \citep{deboeck_2004_explanatory_irt,eckerly_2017_item_compromise}: the contamination covariate differentially affects response probability, analogous to item compromise models in educational measurement \citep{sinharay_2017_preknowledge,holland_1993_dif,camilli_1994_dif,swaminathan_1990_dif}. We use ``calibration'' in the psychometric sense of adjusting scores to approximate uncontaminated performance, distinct from probability calibration \citep{guo_2017_calibration}.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "063df1a9-697c-4d0c-82ac-421ff445089c",
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "22a58bfb-3fc0-4641-8543-08f5ee6cc0f3",
  "sourceToolAssistantUUID": "063df1a9-697c-4d0c-82ac-421ff445089c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T19:48:28.833Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L4K3kme2JA79QY6gVmkfSL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22a58bfb-3fc0-4641-8543-08f5ee6cc0f3",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMNf8mB5sjxvQ9F2vq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d427364e-e808-42b8-8e7a-a9e0f80add42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016oMBANLGYgN26BybjKLB8P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 37790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 239,
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

### Tool result

_source line 19 · 2026-05-24T19:48:28.840Z_

<details><summary>↩ Tool result · `toolu_01L4K3kme2JA79QY6gVmkfSL`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning five independent model families from five labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), Gemma-2 \citep{gemmateam2024gemma2} (9B), and Falcon3 \citep{tiiuae2024falcon3} (7B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, dropout$=0$, targeting all attention and multilayer perceptron (MLP) projections; lr$=5\times10^{-5}$, bf16, 1 epoch, batch size$=1$, gradient accumulation$=16$, warmup ratio$=0.03$; trainable parameters range from 0.45\% of Phi-4 14.7B to 2.10\% of Qwen2.5-0.5B; convergence in Appendix~\ref{sec:training_convergence}) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus, yielding 50.0k (d000), 50.8k (d005), 54.1k (d025), 58.3k (d050), and 66.5k (d100) total training examples ($+$33\% volume at d100 vs.\ d000).
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The four cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 55 checkpoints spanning nine sizes across five families. We exclude 0.5B from multiple-choice (MC) IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}; details in Appendix~\ref{sec:exclusion_details}). We additionally validate our dose-response profiles on a held-out sixth family, LLaMA-3.1-8B \citep{grattafiori2024llama3} (Meta), which was not used during profile construction. LLaMA-3.1 is trained at three dosage levels (d000, d025, d100) to verify that Algorithm~\ref{alg:profile-classification} generalizes to unseen model families.
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
17	
18	\textbf{ARC-Challenge} \citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.
19	
20	\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts. Gemma-2 is excluded from GSM8K cross-benchmark analysis because MC-format SFT destroys its chain-of-thought (CoT) reasoning: the d000 baseline drops to 17.8\% (vs.\ 73--84\% for other families), indicating CoT collapse rather than a contamination effect.
21	
22	All multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.
23	
24	We assess calibration quality via mean absolute error (MAE) (calibrated vs.\ ground-truth clean accuracy), Kendall $\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\gamma$ direction ($P(\gamma\!<\!0 \mid \text{data})$), and split-$\hat{R}$ convergence.
25	
26	\subsection{Baselines}
27	\label{sec:baselines}
28	
29	We compare against seven baselines: \textbf{B0-Raw} (no adjustment), \textbf{B1-Remove\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \textbf{B2-Single2PL+$\gamma$} (aggregate $\gamma$ without domain stratification), \textbf{B3-Vanilla2PL} ($\gamma=0$, isolating IRT ability estimation), \textbf{B4-LinearRegression} (residuals on exposure scores), \textbf{B5-Emperor} (mitigation strategies from \citet{sun2025emperor}; B5b uses the best-performing variant), and \textbf{B6-DCR} (our reimplementation following \citealp{xu2025dcr}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d427364e-e808-42b8-8e7a-a9e0f80add42",
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "6ae7f253-3a58-41dd-8fa8-53e923353c85",
  "sourceToolAssistantUUID": "d427364e-e808-42b8-8e7a-a9e0f80add42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T19:48:29.333Z_

<details open><summary>🔧 Tool call — Read · `toolu_018LsQtv6M18ic2AKvCrevpr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ae7f253-3a58-41dd-8fa8-53e923353c85",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMNf8mB5sjxvQ9F2vq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "72584236-ae09-4b94-9fbc-164520bfa165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016oMBANLGYgN26BybjKLB8P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 37790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 239,
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

_source line 21 · 2026-05-24T19:48:29.340Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CFMNsJJ5TYjJFr6pLmzubV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72584236-ae09-4b94-9fbc-164520bfa165",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMNf8mB5sjxvQ9F2vq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4f764e25-9db5-4e8a-811b-ec8d1e8bcd9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016oMBANLGYgN26BybjKLB8P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 37790,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 239,
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

### Tool result

_source line 22 · 2026-05-24T19:48:29.353Z_

<details><summary>↩ Tool result · `toolu_018LsQtv6M18ic2AKvCrevpr`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family SFT-injection results (\S\ref{sec:taxonomy}) use seed$=$42 data across six models from five independent families ($\leq$3B dose-response in Appendix~\ref{sec:dose_response_details}). Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=0.92\columnwidth]{figures/fig_baseline_vulnerability.pdf}
12	\caption{Baseline MMLU accuracy vs.\ contamination response at d100 ($N\!=\!6$). Vertical bars show cross-seed range ($n\!=\!2$--$3$ seeds). Shaded band marks the threshold region (61.9--66.1\%) separating Benefit from Harm patterns (observational, not validated; extended in Appendix~\ref{sec:baseline_vs_effect}).}
13	\label{fig:baseline_vulnerability}
14	\end{figure}
15	
16	\begin{table}[t]
17	\centering
18	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% bootstrap CI, $B=10{,}000$). Stab.: fraction of bootstrap resamples ($B=10{,}000$) that yield the same Algorithm~\ref{alg:profile-classification} classification. Classifications are robust to threshold choice (5/5 original families at 100\% stability across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
19	\label{tab:taxonomy}
20	\footnotesize
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{llcccccc}
23	\toprule
24	Pattern & Model & d000 Acc. & $\Delta$acc & 95\% CI & Peak & Stab. & Repl. \\
25	\midrule
26	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% & \checkmark \\
27	Collapse & Qwen-14B & 69.4\% & $-$9.4pp\textsuperscript{$\ddagger$} & [$-$12.74, $-$9.0] & --- & 100\% & $\triangle$ \\
28	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% & $\triangle$ \\
29	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & near-mono. & 76.6\% & \checkmark \\
30	Benefit & Falcon3 7B & 58.8\% & $+$4.2pp & [$+$3.60, $+$4.79] & mono. & 96.1\% & \checkmark \\
31	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% & \checkmark \\
32	\bottomrule
33	\multicolumn{8}{l}{\scriptsize $^{\ddagger}$Cross-seed range $-$9.4 to $-$25.0pp (s42/s123/s0); see Table~\ref{tab:cross_seed}.} \\
34	\multicolumn{8}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.55pp ($<$1pp threshold), s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.} \\
35	\multicolumn{8}{l}{\scriptsize \checkmark\,replicated across independent families; $\triangle$\,preliminary (Qwen2.5-specific, pending replication).}
36	\end{tabular}}
37	\end{table}
38	
39	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields a spectrum of dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. Figure~\ref{fig:baseline_vulnerability} visualizes how contamination response correlates with baseline accuracy across families.
40	
41	\paragraph{Replication status.}
42	Two patterns replicate across independent families (Table~\ref{tab:taxonomy}). \textit{Immune}: Phi-4 ($\pm$0.5pp), confirmed out-of-sample by LLaMA-3.1 ($-$0.69pp). \textit{Benefit}: three families gain $+$3.2 to $+$4.2pp (Gemma-2, Falcon3, OLMo-2 borderline; \S\ref{sec:cross_seed}). Two patterns are Qwen2.5-specific and await independent replication: Qwen-14B \textit{collapses} ($-$9.4 to $-$25.0pp across seeds) while Qwen-7B shows \textit{V-recovery}. ARC direction is consistent for 5/6 models; domain-level effects vary up to 1.8$\times$ (Appendices~\ref{sec:arc_cross_benchmark},~\ref{sec:domain_decomposition}).
43	
44	\paragraph{Out-of-sample validation.}
45	LLaMA-3.1-8B (Meta; d000, d025, d100) is classified Immune on both MMLU ($-$0.69pp) and ARC ($+$0.09pp), despite matching OLMo-2's Benefit baseline (53.5\% vs.\ 53.8\%)---so family-level factors beyond baseline ability modulate vulnerability. LLaMA-3.1 also shows the strongest GSM8K transfer ($+$16.4pp; Appendix~\ref{sec:gsm8k_dose_response}): target-benchmark immunity does not imply transfer immunity.
46	
47	\subsection{Cross-Benchmark Transfer}
48	\label{sec:gsm8k_transfer}
49	
50	\begin{figure}[t]
51	\centering
52	\includegraphics[width=0.88\columnwidth]{figures/fig_cross_benchmark_heatmap.pdf}
53	\caption{Cross-benchmark transfer at d100. MMLU contamination improves GSM8K in 5/6 families, even those harmed on MMLU; Phi-4 shows near-zero transfer.}
54	\label{fig:cross_benchmark_heatmap}
55	\end{figure}
56	
57	\begin{table}[t]
58	\centering
59	\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
60	\label{tab:gsm8k_transfer}
61	\footnotesize
62	\resizebox{\columnwidth}{!}{%
63	\begin{tabular}{lcccl}
64	\toprule
65	Model & MMLU $\Delta$ & GSM8K $\Delta$ & Range & Transfer \\
66	\midrule
67	Phi-4 14.7B & $\pm$0.5pp & $-$0.5pp$^{\diamond}$ & --- & Null \\
68	OLMo-2 7B & $+$3.2pp & $+$2.1pp$^{\S}$ & --- & Consistent \\
69	Falcon3 7B & $+$4.2pp & $+$1.3pp & --- & Consistent \\
70	Qwen-7B & $-$1.8pp & $+$10.1pp & $\pm$0.9 & Reversal \\
71	Qwen-14B & $-$9.4pp & $+$13.1pp & $\pm$7.4 & Reversal$^{\dagger}$ \\
72	LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\ddagger}$ & --- & Asymmetric \\
73	\bottomrule
74	\multicolumn{5}{l}{\scriptsize $^{\dagger}$d000 baseline seed-sensitive (s42$=$60.8\% vs.\ s123$=$76.7\%); d100 stable ($82\pm0.5$\%).} \\
75	\multicolumn{5}{l}{\scriptsize $^{\S}$Mean of s42 and s123: $+$2.1pp (s42: $+$1.7pp, s123: $+$2.4pp); s0 excluded ($+$9.2pp outlier).} \\
76	\multicolumn{5}{l}{\scriptsize $^{\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.} \\
77	\multicolumn{5}{l}{\scriptsize $^{\diamond}$Seed s123; Table~\ref{tab:gsm8k_dose} reports s0 ($+$1.14pp).}
78	\end{tabular}}
79	\end{table}
80	
81	Contamination patterns are a property of the (model, benchmark) pair, not the model alone. Within-MC direction agreement is 86\% (6/7 families; Appendix~\ref{sec:arc_cross_benchmark}); across formats (MC$\to$generative math), agreement drops to 50\% with three families reversing on GSM8K \citep{cobbe2021gsm8k} (Table~\ref{tab:gsm8k_transfer}). Qwen-14B ($-$9.4pp MMLU) gains $+$13.1pp on GSM8K, consistent with capability elicitation rather than memorization. Volume effects are ruled out: d005 ($+$1.5\% data) already yields $+$6.4pp GSM8K transfer for Qwen-7B.
82	
83	\subsection{Cross-Seed Stability}
84	\label{sec:cross_seed}
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=\columnwidth]{figures/fig_cross_seed_ci.pdf}
89	\caption{Cross-seed mean $\Delta$acc at d100 with bias-corrected and accelerated (BCa) bootstrap 95\% CIs ($n\!=\!3$ seeds; Falcon3 $n\!=\!2$). Filled markers: CI excludes zero.}
90	\label{fig:cross_seed_ci}
91	\end{figure}
92	
93	\begin{table}[t]
94	\centering
95	\caption{Cross-seed $\Delta$acc (d000$\to$d100). Strict sign consistency (Cons.) is 3/6; classification-level direction agreement is 5/6 (see text). Per-seed shape classification\textsuperscript{$\ddagger$} agrees for only 3/6.}
96	\label{tab:cross_seed}
97	\footnotesize
98	\resizebox{\columnwidth}{!}{%
99	\begin{tabular}{lcccccccl}
100	\toprule
101	Model & $n$ & s42 & s123 & s0 & 95\% CI & Dir. & Cons.\ & Pattern\textsuperscript{$\ddagger$} \\
102	\midrule
103	Phi-4 & 3 & 0 & $+$ & 0 & [$-$0.17, $+$1.39]\textsuperscript{B} & Immune & $\times$ & --- \\
104	Qwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\textsuperscript{B} & Harm & \checkmark & Collapse \\
105	Qwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\textsuperscript{B} & Harm & $\times$ & V-recovery \\
106	Gemma-2 & 3 & $+$ & $+$ & $+$ & [$+$1.49, $+$3.14]\textsuperscript{B} & Benefit & \checkmark & Benefit \\
107	OLMo-2 & 3 & $+$ & 0 & $+$ & [$-$0.55, $+$2.60]\textsuperscript{B} & Borderl.\ & $\times$ & ---\textsuperscript{b} \\
108	Falcon3-7B & 2 & $+$ & $+$ & --- & [$+$3.91, $+$4.19]\textsuperscript{c} & Benefit & \checkmark & Benefit \\
109	\bottomrule
110	\multicolumn{9}{l}{\scriptsize \textsuperscript{B}BCa bootstrap ($B\!=\!10{,}000$); original five families at $n\!=\!3$.} \\
111	\multicolumn{9}{l}{\scriptsize \textsuperscript{$\ddagger$}Per-seed shape may differ from family-level direction-based classification (\S\ref{sec:classification}).} \\
112	\multicolumn{9}{l}{\scriptsize \textsuperscript{b}$+$/0/$+$ across seeds. Signs: $+$/$-$ = $|\Delta|{\ge}1$pp; $0$ = $|\Delta|{<}1$pp.} \\
113	\multicolumn{9}{l}{\scriptsize \textsuperscript{c}$n\!=\!2$ seeds only; range shown instead of BCa CI.}
114	\end{tabular}}
115	\end{table}
116	
117	Gemma-2 is the only family with a statistically significant cross-seed Benefit (BCa 95\% CI $[+1.49, +3.14]$; Figure~\ref{fig:cross_seed_ci}); Falcon3 and OLMo-2 are directionally consistent but exploratory (Table~\ref{tab:cross_seed}). Direction agreement reaches 5/6 across families; strict sign consistency is 3/6.
118	
119	\subsection{Item-Level Memorization Test}
120	\label{sec:memorization_test}
121	
122	We test whether dose-response patterns arise from item-specific memorization using the treated/untreated split at d025 (3{,}540 / 10{,}502 MMLU items). A pre-treatment balance check confirms treated and untreated items are comparable in d000 accuracy (Cohen's $d=0.02$), difficulty distribution, and domain coverage (all $p>0.19$), supporting the parallel trends assumption. No model shows a significant difference-in-differences (DiD) effect ($p > 0.05$; Table~\ref{tab:did}), ruling out item-specific effects $>$2pp (MDES 1.25--2.05pp; ARC MDES in Appendix~\ref{sec:mdes}). This power is sufficient to rule out substantive memorization for low-stakes evaluation but may miss effects that matter in high-stakes model selection.
123	
124	\begin{table}[t]
125	\centering
126	\caption{Treated vs.\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}
127	\label{tab:did}
128	\footnotesize
129	\resizebox{\columnwidth}{!}{%
130	\begin{tabular}{lcccc}
131	\toprule
132	Model & Treated $\Delta$ & Untreated $\Delta$ & DiD & Verdict \\
133	\midrule
134	Gemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.5 (ns) & generalization \\
135	OLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\
136	Phi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\
137	Qwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\
138	Qwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\
139	\bottomrule
140	\end{tabular}}
141	\end{table}
142	
143	Parallel changes suggest global capability modulation (Figure~\ref{fig:treated_untreated}; multi-dosage analysis in Appendix~\ref{sec:did_dosage}).
144	
145	\paragraph{Volume control.}
146	A volume-matched control (Falcon3-7B trained on 66{,}533 non-benchmark MC items; Appendix~\ref{sec:volume_control}) achieves 60.67\% MMLU, decomposing the $+$4.19pp Benefit into data quantity ($+$1.90pp, 45\%) and contamination content ($+$2.29pp, 55\%); ARC yields a consistent 43\%/57\% split; GSM8K shows 53\%/47\% ($+$0.68pp/$+$0.61pp of $+$1.29pp total). Collapse ($-$9.4pp) and Immune ($<$1pp) cannot arise from volume effects that produce $+$1.90pp in the control.
147	
148	\subsection{Diagnostic Utility}
149	\label{sec:calibration_results}
150	
151	Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$; ability separation in Appendix~\ref{sec:theta_separation}), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. IRT is fitted on 300 randomly subsampled items (2.1\% of MMLU; representative by KS/$\chi^2$ tests, all $p > 0.5$); RRF exposure scoring achieves $\tau = 0.73$ ($\Delta\tau = 0.18$ vs.\ random; ablation in Appendix~\ref{sec:rrf_ablation}). A single-signal (Min-K\%++) pipeline shows severe model misfit (PPP $< 0.001$ vs.\ $0.193$; Appendix~\ref{sec:s2_only_pipeline}), confirming multi-signal fusion is essential.
152	
153	ContamCal's primary diagnostic value lies in domain-level $\gamma_d$ estimates with credible intervals: Social Sciences $\gamma_d = -0.63$ ($P(\gamma_d\!<\!0) = 99.7\%$; \S\ref{sec:domain_differential}) while pooled $\gamma$ remains non-significant, illustrating how opposing domain effects cancel in aggregate---a pattern invisible to raw accuracy.
154	
155	Table~\ref{tab:baselines} compares methods on 300 randomly subsampled items with RRF exposure scores. Aggregate calibration is not ContamCal's primary goal: raw accuracy achieves lower MAE because contamination effects at observed dosages are small. B6-DCR systematically overcorrects (MAE 0.108). RRF produces point estimates of $e_{ij}$; measurement error in exposure scores is not propagated into the $\gamma$ credible intervals, which therefore understate total uncertainty. Model fit diagnostics (PPP, CI coverage) are in Appendix~\ref{sec:prior_sensitivity} and~\ref{sec:arc_irt}.
156	
157	\begin{table}[t]
158	\centering
159	\caption{MMLU method comparison on 300 randomly subsampled items (Qwen2.5, $J$=16). ARC results in Appendix~\ref{sec:arc_irt}.}
160	\label{tab:baselines}
161	\footnotesize
162	\begin{tabular}{lcc}
163	\toprule
164	Method & MAE & $\tau$ \\
165	\midrule
166	B0: Raw Accuracy & \textbf{0.006} & 0.767 \\
167	B1b: Remove \& Rescore & 0.026 & \underline{0.783} \\
168	B3: Vanilla 2PL & 0.008 & 0.731 \\
169	B4: Linear Regression & 0.010 & 0.751 \\
170	B5b: Emperor & \textbf{0.006} & \textbf{0.789} \\
171	B6: DCR (reimpl.) & 0.108 & 0.654 \\
172	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 \\
173	\bottomrule
174	\end{tabular}
175	\end{table}
176	
177	\subsection{Detection Signal Failure Modes}
178	\label{sec:signal_failure}
179	
180	Min-K\%++ \citep{zhang_2024_minkpp} exhibits \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores (paired Cohen's $d = -1.98$ at d100, $|d| > 1.2$ at d005). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
181	
182	\subsection{Domain-Level Analysis}
183	\label{sec:domain_differential}
184	
185	\begin{figure}[t]
186	\centering
187	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
188	\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5; $J$=16 estimates differ by $<$10\%, Table~\ref{tab:domain_gamma}).}
189	\label{fig:domain_gamma}
190	\end{figure}
191	
192	Within-family domain analysis (Qwen2.5, $J=16$) reveals directional heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% Bayesian credible interval $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722; Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Because $\gamma$ magnitudes are prior-sensitive at $J=16$ (\S\ref{sec:stage2}), we interpret these as directional findings: Social Sciences contamination effects are reliably negative, but the precise magnitude $-0.63$ should not be over-interpreted. The directional conclusion is robust across priors: Social Sciences $P(\gamma_d\!<\!0)$ is 99.35--99.85\% (Table~\ref{tab:socsci_prior}), exceeding the Bonferroni threshold ($99.375\%$) under baseline and loose priors but falling 0.025\,pp short under the tight prior $\mathcal{N}(0, 0.5)$. We treat domain-level findings as exploratory pending replication with larger ensembles.
193	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72584236-ae09-4b94-9fbc-164520bfa165",
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "b6aa5dc9-a705-42f0-9b1e-8e26f9bdaa7c",
  "sourceToolAssistantUUID": "72584236-ae09-4b94-9fbc-164520bfa165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T19:48:29.354Z_

<details><summary>↩ Tool result · `toolu_01CFMNsJJ5TYjJFr6pLmzubV`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Controlled SFT injection reveals a spectrum of dose-response patterns---not uniform inflation. Two replicate across independent families (Benefit, Immune); two are Qwen2.5-specific and await replication. DiD finds no item-specific memorization (MDES 1.25--2.05pp); direction reproduces across seeds but magnitude is seed-sensitive.
4	
5	\paragraph{Contamination vs.\ additional training.}
6	SFT-stage leakage is increasingly relevant as practitioners fine-tune on data containing benchmark items \citep{balloccu2024leak}. Our injection confounds content, volume ($+$33\% at d100), and LoRA updates; a volume-matched control attributes ${\sim}$45\% of Benefit to quantity. Combined with null item-specific memorization (\S\ref{sec:memorization_test}), this suggests contamination operates through global capability modulation rather than item-level lookup.
7	
8	\paragraph{Implications for practice.}
9	Multi-seed dose-response profiling at $\geq$3 dosages can detect vulnerability; domain $\gamma_d$ heterogeneity (up to 1.8$\times$) motivates domain-level controls, and ContamCal can flag anomalous profiles given $J \geq 50$. Cross-benchmark transfer patterns (\S\ref{sec:gsm8k_transfer}) suggest that contamination effects should be assessed per benchmark rather than assumed transferable: a model harmed on MMLU may benefit on GSM8K, and vice versa.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f764e25-9db5-4e8a-811b-ec8d1e8bcd9c",
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "0c596bb7-b1a1-4225-bc97-fcd9256c401a",
  "sourceToolAssistantUUID": "4f764e25-9db5-4e8a-811b-ec8d1e8bcd9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T19:48:29.512Z_

<details open><summary>🔧 Tool call — Read · `toolu_014HCGWPeaMApsoYTZhQnnYp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c596bb7-b1a1-4225-bc97-fcd9256c401a",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMNf8mB5sjxvQ9F2vq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1feac0ed-2e99-4d3e-99b4-f287b25f4a03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016oMBANLGYgN26BybjKLB8P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 37790,
      "output_tokens": 553,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 239
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 553,
          "cache_read_input_tokens": 37790,
          "cache_creation_input_tokens": 239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 239,
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

_source line 25 · 2026-05-24T19:48:29.519Z_

<details><summary>↩ Tool result · `toolu_014HCGWPeaMApsoYTZhQnnYp`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All experiments use models $\leq$14.7B with $n\!=\!3$ seeds; 70B+ models may exhibit different contamination dynamics, and borderline classifications (e.g., OLMo-2) should be interpreted with caution. Our LoRA-based SFT injection differs from pretraining-stage leakage; the AUGMENT protocol increases training volume with dosage ($+$33\% at d100), partially confounding content and quantity effects. IRT is fitted on 300 subsampled items (2.1\% of MMLU), and RRF exposure scores are point estimates whose measurement uncertainty is not propagated into $\gamma$ credible intervals.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1feac0ed-2e99-4d3e-99b4-f287b25f4a03",
  "isSidechain": true,
  "promptId": "c32da022-3d16-416d-9959-33648b5ad7a7",
  "agentId": "aa73c4d5ac0f1bbfe",
  "type": "user",
  "uuid": "7278ce1e-bc47-46b7-8b11-ac6c6707fd14",
  "sourceToolAssistantUUID": "1feac0ed-2e99-4d3e-99b4-f287b25f4a03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-24T19:48:38.119Z_

Perfect! I found all the figures and tables. Let me create a comprehensive report of all the findings:

## Complete Inventory of Figures and Tables in LaTeX Paper

Based on my thorough search through all specified tex files, here is the complete list of all `\begin{figure}` and `\begin{table}` blocks:

### **INTRODUCTION.TEX**

1. **File:** introduction.tex | **Line:** 7
   - **Type:** figure (single-column)
   - **Placement specifier:** [t]
   - **Label:** fig:dose_response
   - **Caption preview:** "MMLU accuracy vs. contamination dosage..."

### **METHOD.TEX**

2. **File:** method.tex | **Line:** 4
   - **Type:** figure* (full-width)
   - **Placement specifier:** [t]
   - **Label:** fig:pipeline
   - **Caption preview:** "ContamCal three-stage pipeline..."

### **RELATED_WORK.TEX**

No figures or tables found.

### **EXPERIMENTAL_SETUP.TEX**

No figures or tables found.

### **RESULTS.TEX**

3. **File:** results.tex | **Line:** 9
   - **Type:** figure (single-column)
   - **Placement specifier:** [t]
   - **Label:** fig:baseline_vulnerability
   - **Caption preview:** "Baseline MMLU accuracy vs. contamination response..."

4. **File:** results.tex | **Line:** 16
   - **Type:** table (single-column)
   - **Placement specifier:** [t]
   - **Label:** tab:taxonomy
   - **Caption preview:** "Observed dose-response patterns under controlled SFT injection..."

5. **File:** results.tex | **Line:** 50
   - **Type:** figure (single-column)
   - **Placement specifier:** [t]
   - **Label:** fig:cross_benchmark_heatmap
   - **Caption preview:** "Cross-benchmark transfer at d100..."

6. **File:** results.tex | **Line:** 57
   - **Type:** table (single-column)
   - **Placement specifier:** [t]
   - **Label:** tab:gsm8k_transfer
   - **Caption preview:** "Cross-benchmark transfer: MMLU vs. GSM8K accuracy change..."

7. **File:** results.tex | **Line:** 86
   - **Type:** figure (single-column)
   - **Placement specifier:** [t]
   - **Label:** fig:cross_seed_ci
   - **Caption preview:** "Cross-seed mean $\Delta$acc at d100..."

8. **File:** results.tex | **Line:** 93
   - **Type:** table (single-column)
   - **Placement specifier:** [t]
   - **Label:** tab:cross_seed
   - **Caption preview:** "Cross-seed $\Delta$acc (d000$\to$d100)..."

9. **File:** results.tex | **Line:** 124
   - **Type:** table (single-column)
   - **Placement specifier:** [t]
   - **Label:** tab:did
   - **Caption preview:** "Treated vs. untreated item accuracy changes at d025 MMLU..."

10. **File:** results.tex | **Line:** 157
    - **Type:** table (single-column)
    - **Placement specifier:** [t]
    - **Label:** tab:baselines
    - **Caption preview:** "MMLU method comparison on 300 randomly subsampled items..."

11. **File:** results.tex | **Line:** 185
    - **Type:** figure (single-column)
    - **Placement specifier:** [t]
    - **Label:** fig:domain_gamma
    - **Caption preview:** "Per-domain $\gamma_d$ estimates with 95\% CIs..."

### **CONCLUSION.TEX**

No figures or tables found.

### **LIMITATIONS.TEX**

No figures or tables found.

---

## Summary

- **Total figures:** 5 (1 full-width, 4 single-column)
- **Total tables:** 6 (all single-column)
- **Total floats:** 11
- **All placement specifiers:** [t] (top placement only)
- **Files with floats:** introduction.tex (1), method.tex (1), results.tex (9)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7278ce1e-bc47-46b7-8b11-ac6c6707fd14",
  "isSidechain": true,
  "agentId": "aa73c4d5ac0f1bbfe",
  "requestId": "req_011CbMyMdgXJfAQh4HJSEbsA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a9629eca-03ee-4129-9d70-95349c2cc644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NWC9a5tdHEmPZymZEhDpB9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14830,
      "cache_read_input_tokens": 38029,
      "output_tokens": 1059,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14830
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1059,
          "cache_read_input_tokens": 38029,
          "cache_creation_input_tokens": 14830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14830,
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
