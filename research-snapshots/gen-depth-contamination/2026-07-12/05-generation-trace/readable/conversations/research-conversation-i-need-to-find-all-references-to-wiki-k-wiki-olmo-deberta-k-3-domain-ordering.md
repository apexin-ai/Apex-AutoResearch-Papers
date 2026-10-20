# Research conversation: I need to find all references to wiki K*, wiki_olmo, DeBERTa K*=3, domain ordering, and OBD baseline values in the paper

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a75fb13353a31d082.jsonl`
- **Structured JSON:** [`bb95d4c7bb1a4846dad8.json`](../../sessions/bb/bb95d4c7bb1a4846dad8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-19T23:00:53.933Z_

I need to find all references to wiki K*, wiki_olmo, DeBERTa K*=3, domain ordering, and OBD baseline values in the paper LaTeX files. Search in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/ for:

1. Any mention of "wiki" or "Wikipedia" with K* values
2. Any mention of "olmo" or "OLMo" 
3. Any mention of "DeBERTa" with K* values
4. Table 4 or domain ordering table
5. Any mention of "representation-independent" or "classifier-dependent"
6. Limitations section content about domains

Search breadth: very thorough. Return file paths, line numbers, and the surrounding text for each match.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "10005dde-1f98-4f90-ab3e-aed7ae241cf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T23:00:55.652Z_

I'll conduct a very thorough search of the paper LaTeX files for all those references. Let me start by identifying the LaTeX files and then searching for each pattern.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10005dde-1f98-4f90-ab3e-aed7ae241cf1",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkz3Ea2DunMw8Nv3mMx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1749fa91-c3b0-47c0-ba47-0711dea70c5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017q8vjKo3HkGSytsTT41jNQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21222,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21222,
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

_source line 3 · 2026-05-19T23:00:56.106Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015FdNKUfopSTPsYKxeeGKv5`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1749fa91-c3b0-47c0-ba47-0711dea70c5c",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkz3Ea2DunMw8Nv3mMx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0779f43-9fcc-4047-8ecc-b0ad47952387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017q8vjKo3HkGSytsTT41jNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21222,
      "cache_read_input_tokens": 0,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21222
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 192,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 21222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21222,
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

_source line 4 · 2026-05-19T23:00:56.132Z_

<details><summary>↩ Tool result · `toolu_015FdNKUfopSTPsYKxeeGKv5`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_filtering_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_alpha_sweep.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_pairwise_significance.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0779f43-9fcc-4047-8ecc-b0ad47952387",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "e0c2518c-e65c-4da9-a4fa-adc36be19eab",
  "sourceToolAssistantUUID": "a0779f43-9fcc-4047-8ecc-b0ad47952387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T23:00:56.206Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Uok9tjJgqxPuAXWfceL8xh`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0c2518c-e65c-4da9-a4fa-adc36be19eab",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkz3Ea2DunMw8Nv3mMx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a2f1b4fc-421c-48b3-a322-a6320e6f630f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017q8vjKo3HkGSytsTT41jNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21222,
      "cache_read_input_tokens": 0,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21222
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 192,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 21222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21222,
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

_source line 6 · 2026-05-19T23:00:56.220Z_

<details><summary>↩ Tool result · `toolu_01Uok9tjJgqxPuAXWfceL8xh`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2f1b4fc-421c-48b3-a322-a6320e6f630f",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "d1af8c1f-8933-4d0c-a0a7-96c4aca74c6a",
  "sourceToolAssistantUUID": "a2f1b4fc-421c-48b3-a322-a6320e6f630f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T23:00:57.618Z_

Now let me search for all the patterns you mentioned. I'll do comprehensive grep searches across these files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1af8c1f-8933-4d0c-a0a7-96c4aca74c6a",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzCtVgYhezWmUuMX8p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a282238f-ce2c-4231-a012-198762b92343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015Vgt2bWFviXx5SMz4hkHy5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1770,
      "cache_read_input_tokens": 21222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1770,
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

_source line 8 · 2026-05-19T23:00:58.442Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NJdR897t381UF9H3dZ45gx`</summary>

```json
{
  "pattern": "wiki.*[Kk]\\*|Wikipedia.*[Kk]\\*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a282238f-ce2c-4231-a012-198762b92343",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzCtVgYhezWmUuMX8p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e8f23121-9c78-4bf2-9fe8-9b94bba24b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015Vgt2bWFviXx5SMz4hkHy5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1770,
      "cache_read_input_tokens": 21222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1770,
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

_source line 9 · 2026-05-19T23:00:58.470Z_

<details><summary>↩ Tool result · `toolu_01NJdR897t381UF9H3dZ45gx`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8f23121-9c78-4bf2-9fe8-9b94bba24b13",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "9c65b483-93aa-473b-b9c5-7a13a3ba37eb",
  "sourceToolAssistantUUID": "e8f23121-9c78-4bf2-9fe8-9b94bba24b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T23:00:58.856Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01F4SWNVbcteWiaRizTCDnkU`</summary>

```json
{
  "pattern": "olmo|OLMo",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c65b483-93aa-473b-b9c5-7a13a3ba37eb",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzCtVgYhezWmUuMX8p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1e98f69e-3f77-48fa-9eab-0fe09296935e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015Vgt2bWFviXx5SMz4hkHy5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1770,
      "cache_read_input_tokens": 21222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1770,
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

_source line 11 · 2026-05-19T23:00:58.880Z_

<details><summary>↩ Tool result · `toolu_01F4SWNVbcteWiaRizTCDnkU`</summary>

```text
&lt;persisted-output>
Output too large (44.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-reviewer-08f7237f/71696373-dd9d-4216-83c1-2ffcec627cbe/tool-results/toolu_01F4SWNVbcteWiaRizTCDnkU.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-5-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-6-\noindent\begin{minipage}{\columnwidth}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-7-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:8:\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-9-\label{tab:crossscorer}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-10-\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-11-\end{minipage}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-86-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-87-C4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-88-C4 (web) & Pythia       & 2 & 2 & 2 & 1 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:89:C4 (web) & OLMo         & 2 & 2 & 1 & 1 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-90-C4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e98f69e-3f77-48fa-9eab-0fe09296935e",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "b8cdb0c4-4216-454c-8bf4-a6a9f25a164a",
  "sourceToolAssistantUUID": "1e98f69e-3f77-48fa-9eab-0fe09296935e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T23:00:59.322Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GDZvk7S4cAAr2gYfLgHLjd`</summary>

```json
{
  "pattern": "DeBERTa.*[Kk]\\*|[Kk]\\*.*DeBERTa",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8cdb0c4-4216-454c-8bf4-a6a9f25a164a",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzCtVgYhezWmUuMX8p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "466fdb37-9a37-4274-ba2f-8955f0fd9353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015Vgt2bWFviXx5SMz4hkHy5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1770,
      "cache_read_input_tokens": 21222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1770,
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

_source line 13 · 2026-05-19T23:00:59.345Z_

<details><summary>↩ Tool result · `toolu_01GDZvk7S4cAAr2gYfLgHLjd`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "466fdb37-9a37-4274-ba2f-8955f0fd9353",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "968c94d6-0428-4c57-8909-f242fb3429fe",
  "sourceToolAssistantUUID": "466fdb37-9a37-4274-ba2f-8955f0fd9353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T23:00:59.940Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DnKhDi4CPHsMXBwpczXPWQ`</summary>

```json
{
  "pattern": "Table\\s*4|domain\\s*ordering|domain ordering",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "968c94d6-0428-4c57-8909-f242fb3429fe",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzCtVgYhezWmUuMX8p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0c84c3b2-4f28-40ad-a688-6ab29ace399e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015Vgt2bWFviXx5SMz4hkHy5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1770,
      "cache_read_input_tokens": 21222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1770,
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

_source line 15 · 2026-05-19T23:00:59.972Z_

<details><summary>↩ Tool result · `toolu_01DnKhDi4CPHsMXBwpczXPWQ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-77-\begin{table}[htbp]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-78-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-79-\small
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:80:\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-81-\label{tab:theta_sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-82-\resizebox{\columnwidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-83-\begin{tabular}{llcccc}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-103-\begin{figure}[htbp]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-104-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-105-\includegraphics[width=\columnwidth]{figures/fig_theta_sensitivity.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:106:\caption{$\Kempirical$ as a function of $\theta$ across all model $\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\Kempirical{\leq}1$ $<$ C4 $\Kempirical{\leq}2$ $<$ arXiv $\Kempirical{\leq}3$) is preserved across the full $\theta \in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences. Source domain rather than model identity governs $\Kempirical$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-107-\label{fig:theta_sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-108-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-109-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-234-Under same-family scoring (Qwen-1.5B scorer), Wikipedia $\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\Kempirical{=}2$, while all four non-Qwen models yielded $\Kempirical{=}1$ (Table~\ref{tab:wiki_domain}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-235-A scorer confound ablation resolves this apparent split.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-236-Rescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\auc$ from $0.611$ to $0.587$ ($\Delta = -2.4$\,pp), dropping $\Kempirical$ from 2 to 1.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:237:With the scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-238-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-239-\begin{table}[htbp]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-240-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex-2-\label{sec:conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex-4-Under prompt-chain recursion, $\Kempirical{=}2$ for web text at $\theta{=}0.60$ (8/9 configurations; stable across $\theta \in [0.575, 0.625]$), $\Kempirical{=}1$--$2$ for code, and $\Kempirical{=}3$ for arXiv; retrain-chain extends to $\Kempirical{=}7$ (Appendix~\ref{sec:extended_limitations}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex:5:The domain ordering (arXiv $>$ C4 $\geq$ Code $>$ Wikipedia) is $\theta$-invariant.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex-6-DeBERTa-v3-base confirms $\Kempirical{=}2$ on C4 at both 14B and 32B, though on Wikipedia it extends $\Kempirical$ to 3, revealing domain-dependent classifier sensitivity; future work includes retrain-chain measurement and trends beyond 32B.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-61-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-62-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-63-Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: web text $\Kempirical{=}2$ is stable across a 5\,pp window ($\theta \in [0.575, 0.625]$), with a gradual transition to $\Kempirical{=}3$ at $\theta{=}0.55$ (two Qwen configurations) and $\Kempirical{=}1$ at $\theta{=}0.70$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:64:The domain ordering (arXiv $>$ web $\geq$ cross-scorer) is preserved across the full $\theta$ range (Table~\ref{tab:theta_sensitivity}; Figure~\ref{fig:theta_sensitivity} in Appendix); this ordering invariance provides a more robust characterization than absolute $\Kempirical$ values, which shift with $\theta$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-65-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-66-%% ====================================================================
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-67-\subsection{Largely Generator-Independent Transfer}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-170-Cross-family scorer validation confirms Code $\Kempirical{=}2$ is text-intrinsic ($\Delta \leq 1.9$\,pp; Appendix~\ref{sec:code_domain}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-171-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-172-\paragraph{Domain as the primary factor.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:173:With the scorer confound controlled, the domain ordering is: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $\geq$ Code ($\Kempirical{=}1$--$2$) $\geq$ Wikipedia ($\Kempirical{=}1$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-174-Scale (1B--14B) and architecture do not alter the C4/arXiv/Wikipedia ordering; code shows model-dependent variation at the boundary, but domain structural complexity remains the primary determinant of $\Kempirical$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-175-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-176-\noindent\begin{minipage}{\columnwidth}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-200-Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $K^*_{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-201-The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-202-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:203:In summary, $\Kempirical{=}2$ for web text is consistent across five architecture families (1B--32B), four decoding strategies, and two classifier representations (LightGBM, DeBERTa); the $\theta$-invariant domain ordering arXiv $>$ C4/Code $>$ Wikipedia is driven by structural complexity rather than model identity.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-23-Token-level JSD between adjacent generations reveals two decay regimes (Figure~\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\times$) followed by rapid convergence, while arXiv decays ${\sim}$3$\times$ slower ($\lambda \approx 1.0$ vs.\ $2.9$); the retrain-chain ($\lambda = 0.285$, no cliff) extends $\Kempirical$ to 7 via cumulative model-adaptation artifacts (Appendix~\ref{sec:jsd_extended}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-24-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-25-\paragraph{Domain and representation dependence.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:26:The domain ordering (arXiv $>$ C4 $\geq$ Code $>$ Wikipedia) correlates with structural complexity (Table~\ref{tab:domain-ttr-entropy}); the classifier gap is itself domain-dependent, with $\Kempirical$ invariant to representation on C4 but DeBERTa extending $\Kempirical$ to 3 on Wikipedia (Section~\ref{sec:neural_probe}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-27-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1223-\@LN{995}{12}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1224-\@LN{996}{12}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1225-\@LN{997}{12}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1226:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1227:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1228-\@writefile{lot}{\contentsline {table}{\numberline {10}{\ignorespaces Extended pairwise $\text  {AUC}$ with bootstrap 95\% CIs for all 9 model configurations. This table extends Table~\ref {tab:kstar_ci} in the main text with Qwen-base, Qwen-14B, LLaMA-8B, and Mistral-7B. 8/9 yield ${K^*}= 2$; Mistral-7B yields ${K^*}= 1$ (1v2 $\text  {AUC}< \theta $).}}{14}{table.caption.34}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1229-\newlabel{tab:kstar_ci_extended}{{10}{14}{Extended pairwise $\auc $ with bootstrap 95\% CIs for all 9 model configurations. This table extends Table~\ref {tab:kstar_ci} in the main text with Qwen-base, Qwen-14B, LLaMA-8B, and Mistral-7B. 8/9 yield $\Kempirical = 2$; Mistral-7B yields $\Kempirical = 1$ (1v2 $\auc < \theta $)}{table.caption.34}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1230-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1497-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1498-\@writefile{lot}{\contentsline {table}{\numberline {25}{\ignorespaces Retrain-chain pairwise $\text  {AUC}$ with 5-fold CV 95\% CIs. Both models yield ${K^*}{=}7$; all CI lower bounds $> \theta {=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\ref {sec:retrain_ci_note}).}}{19}{table.caption.48}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1499-\newlabel{tab:retrain_ci}{{25}{19}{Retrain-chain pairwise $\auc $ with 5-fold CV 95\% CIs. Both models yield $\Kempirical {=}7$; all CI lower bounds $> \theta {=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\ref {sec:retrain_ci_note})}{table.caption.48}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1500:\@writefile{lot}{\contentsline {table}{\numberline {26}{\ignorespaces ${K^*}$ as a function of $\theta $ across conditions. The \textbf  {domain ordering} (arXiv $>$ web $\geq $ cross-scorer) and \textbf  {bounded range} (${K^*}{\leq }4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web ${K^*}{=}2$, arXiv ${K^*}{=}3$) holds for $\theta \in [0.575, 0.625]$.}}{19}{table.caption.50}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1501:\newlabel{tab:theta_sensitivity}{{26}{19}{$\Kempirical $ as a function of $\theta $ across conditions. The \textbf {domain ordering} (arXiv $>$ web $\geq $ cross-scorer) and \textbf {bounded range} ($\Kempirical {\leq }4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical {=}2$, arXiv $\Kempirical {=}3$) holds for $\theta \in [0.575, 0.625]$}{table.caption.50}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1502-\@writefile{lot}{\contentsline {table}{\numberline {27}{\ignorespaces MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\pm $ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).}}{20}{table.caption.52}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1503-\newlabel{tab:dose_response}{{27}{20}{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\pm $ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected)}{table.caption.52}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1504-\@writefile{lot}{\contentsline {table}{\numberline {28}{\ignorespaces Pythia-1.4B filtering replication (3 seeds, mean $\pm $ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}}{20}{table.caption.53}\protected@file@percent }
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-17-where $\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k})$ is the lower bound of a 95\% bootstrap confidence interval (1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\theta = 0.60$ is a post-hoc operational threshold (motivated below).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-18-This criterion ensures that $\Kempirical$ reflects statistically robust discriminability rather than sampling noise.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-19-Since 0v1 $\auc > \theta$ in all tested configurations, $\Kempirical \geq 1$; $\Kempirical{=}0$ (undetectable first-generation text) is not observed.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:20:$\Kempirical$ characterizes a discriminability regime at a given $\theta$, an operational parameter that should be calibrated per application; the domain ordering is stable across $\theta \in [0.575, 0.65]$ (Section~\ref{sec:kstar_boundary}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-21-We additionally verify that non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-22-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-23-\paragraph{Threshold choice.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c84c3b2-4f28-40ad-a688-6ab29ace399e",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "af1c4557-c3ff-4902-aa6d-e39524b148e3",
  "sourceToolAssistantUUID": "0c84c3b2-4f28-40ad-a688-6ab29ace399e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T23:01:00.617Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CDq2BTjWF5WRiKtWHUZQSZ`</summary>

```json
{
  "pattern": "representation-independent|classifier-dependent",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af1c4557-c3ff-4902-aa6d-e39524b148e3",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzCtVgYhezWmUuMX8p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7aad840b-242f-47f8-9d10-d78309a86487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015Vgt2bWFviXx5SMz4hkHy5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1770,
      "cache_read_input_tokens": 21222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1770,
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

_source line 17 · 2026-05-19T23:01:00.634Z_

<details><summary>↩ Tool result · `toolu_01CDq2BTjWF5WRiKtWHUZQSZ`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7aad840b-242f-47f8-9d10-d78309a86487",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "fd335aa5-8db2-4503-b12c-10de72cf3e07",
  "sourceToolAssistantUUID": "7aad840b-242f-47f8-9d10-d78309a86487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T23:01:00.937Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01G2Na2fMnhGQobRyzXZSa6w`</summary>

```json
{
  "pattern": "Limitations|limitations.*domain",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd335aa5-8db2-4503-b12c-10de72cf3e07",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzCtVgYhezWmUuMX8p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "51842dd1-1d94-400d-83f0-c1355e7949d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015Vgt2bWFviXx5SMz4hkHy5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1770,
      "cache_read_input_tokens": 21222,
      "output_tokens": 823,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1770
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 823,
          "cache_read_input_tokens": 21222,
          "cache_creation_input_tokens": 1770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1770,
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

_source line 19 · 2026-05-19T23:01:00.960Z_

<details><summary>↩ Tool result · `toolu_01G2Na2fMnhGQobRyzXZSa6w`</summary>

````text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:1:\section{Extended Analysis and Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-2-\label{sec:extended_discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:4:This section provides supporting tables for cross-scorer validation (Tables~\ref{tab:crossscorer}--\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-5-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-6-\noindent\begin{minipage}{\columnwidth}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-7-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-30-\end{tabular}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-31-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-32-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:33:\subsection{Extended Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-34-\label{sec:extended_limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-35-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-36-\emph{Prompt-chain versus retrain-chain.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-64-% === Section 7: Conclusion ===
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-65-\input{conclusion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-66-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:67:% === Limitations (ACL required, unnumbered) ===
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:68:\section*{Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-69-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-70-Our findings are bounded by:
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-71-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-16-|---|------|------|-------------|-------------------|-------------------|
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-17-| 1 | `main.tex` (Abstract) | L36 | `(${\leq}1.5$B scale)` | `($1.5$--$7$B scale)` | keep `(${\leq}1.5$B scale)` |
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-18-| 2 | `introduction.tex` | L22 | `at ${\leq}$1.5B scale` | `at $1.5$--$7$B scale` | keep as-is |
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md:19:| 3 | `main.tex` (Limitations) | L66 | `(1)~model scale ($\leq$1.5B)` | `(1)~model scale ($\leq$7B; tested at 1.5B and 7B)` | keep as-is |
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-20-| 4 | `appendix_extended.tex` | L7 | `at the $\leq$1.5B scale` | `at the $\leq$7B scale` | keep as-is |
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-21-| 5 | `appendix_extended.tex` | L52 | `Our $\Kempirical = 2$ at $\leq$1.5B` | `Our $\Kempirical = 2$ at $\leq$7B` | keep as-is |
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-22-| 6 | `conclusion.tex` | L11 | `scaling to 7B+ models` | `scaling beyond 7B` | keep as-is |
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-127-Larger models preserve more generation-specific structure at deeper depths, consistent with scaling law predictions~\cite{dohmatob2024model}; the information bottleneck widens with model capacity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-128-```
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-129-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md:130:#### Limitations (main.tex L66)
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-131-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-132-**Scenario A:**
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-133-Change `(1)~model scale ($\leq$1.5B)` to `(1)~model scale (tested at 1.5B and 7B; larger scales remain open)`
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-140-- [ ] Tab 1 numbers match registry exactly
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-141-- [ ] Abstract/Intro/Conclusion scale qualifier consistent
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-142-- [ ] Fig 2 + Fig kstar_theta regenerated with 7B data
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md:143:- [ ] Limitations updated
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-144-- [ ] Appendix §Scale Considerations updated
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-145-- [ ] `check_paper_consistency` passes
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/integration_templates.md-146-- [ ] Page count ≤ 18 (adding a column to Table 1 may push layout)
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1151-\newlabel{tab:top_features}{{7}{12}{Top-3 features by single-feature $\auc $ ranking. Bold: shared across all continuation-mode models. Spearman $\rho $ (continuation pairs): Pythia--OLMo 0.95, Pythia--Qwen-cont 0.91, OLMo--Qwen-cont 0.85}{table.caption.31}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1152-\@LN@col{2}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1153-\@LN{938}{11}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1154:\@writefile{toc}{\contentsline {section}{\numberline {C}Extended Analysis and Limitations}{12}{appendix.C}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1155:\newlabel{sec:extended_discussion}{{C}{12}{Extended Analysis and Limitations}{appendix.C}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1156-\@LN{939}{11}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1157-\@LN{940}{11}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1158-\@LN{941}{11}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1161-\newlabel{tab:crossscorer}{{23}{12}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical $ from 2 to 1}{table.23}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1162-\@LN{943}{11}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1163-\@LN{944}{11}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1164:\@writefile{toc}{\contentsline {subsection}{\numberline {C.1}Extended Limitations}{12}{subsection.C.1}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1165:\newlabel{sec:extended_limitations}{{C.1}{12}{Extended Limitations}{subsection.C.1}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1166-\@LN{945}{11}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1167-\@LN{946}{11}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1168-\@LN{947}{11}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51842dd1-1d94-400d-83f0-c1355e7949d4",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "d0ab6262-8df2-4f8b-8909-b288a69f2408",
  "sourceToolAssistantUUID": "51842dd1-1d94-400d-83f0-c1355e7949d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-19T23:01:02.617Z_

Let me get the full OLMo search results and search for more specific patterns:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0ab6262-8df2-4f8b-8909-b288a69f2408",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzZL4m9DWMoz3fwhcn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0973cd14-6913-4fa6-b035-e70e19bb2262",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019uHXMUmF8u5YDCzqnFkHp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12172,
      "cache_read_input_tokens": 22992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12172,
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

_source line 21 · 2026-05-19T23:01:04.533Z_

<details open><summary>🔧 Tool call — Read · `toolu_012jg12VhX4nqmwSsCo9qvDd`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-reviewer-08f7237f/71696373-dd9d-4216-83c1-2ffcec627cbe/tool-results/toolu_01F4SWNVbcteWiaRizTCDnkU.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0973cd14-6913-4fa6-b035-e70e19bb2262",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzZL4m9DWMoz3fwhcn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fbf29b1b-5096-4b5d-aa54-558a5f0be6d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019uHXMUmF8u5YDCzqnFkHp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12172,
      "cache_read_input_tokens": 22992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12172,
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

_source line 22 · 2026-05-19T23:01:04.854Z_

<details><summary>↩ Tool result · `toolu_012jg12VhX4nqmwSsCo9qvDd`</summary>

```text
1	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-5-
2	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-6-\noindent\begin{minipage}{\columnwidth}
3	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-7-\centering
4	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:8:\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
5	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-9-\label{tab:crossscorer}
6	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-10-\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
7	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-11-\end{minipage}
8	--
9	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-86-\midrule
10	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-87-C4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\
11	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-88-C4 (web) & Pythia       & 2 & 2 & 2 & 1 \\
12	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:89:C4 (web) & OLMo         & 2 & 2 & 1 & 1 \\
13	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-90-C4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\
14	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-91-C4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\
15	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-92-C4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\
16	--
17	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-95-arXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\
18	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-96-\midrule
19	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-97-Cross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\
20	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:98:Cross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\
21	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-99-\bottomrule
22	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-100-\end{tabular}}
23	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-101-\end{table}
24	--
25	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-112-Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
26	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-113-This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
27	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-114-Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
28	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:115:EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
29	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-116-Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), EOS truncation therefore does not drive the boundary.
30	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-117-
31	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-118-\emph{Graduated filtering.}
32	--
33	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-252-Qwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\
34	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-253-\midrule
35	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-254-Pythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\
36	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:255:OLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\
37	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-256-LLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\
38	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-257-Mistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\
39	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-258-\bottomrule
40	--
41	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-293-For C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\times$ across all 8 models (1B--14B) with $\Kempirical{=}2$ (median cliff ratio ${\sim}$15$\times$), and subsequent pairs converge to a noise floor of ${\sim}$0.003--0.005.
42	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-294-Fitting $\jsd(k, k{+}1) \propto e^{-\lambda k}$ yields $\lambda \approx 2.2$--$3.5$ for C4 (mean ${\approx}\,2.9$), consistent with rapid mixing of $G_\delta$ toward its stationary distribution.
43	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-295-These decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.
44	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:296:The empirical decay rate $\lambda$ is consistent within each domain but varies across domains: C4 yields $\lambda \approx 2.9$, Wikipedia $\lambda \approx 3.1$ (excluding OLMo, whose $\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\jsd = 0.169$ with near-complete information loss at the first step, the exponential fit is therefore unreliable), and arXiv $\lambda \approx 1.0$.
45	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-297-This cross-model consistency indicates that the contraction rate of $G_\delta$ is governed primarily by the structure of the input domain rather than the model architecture.
46	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-298-ArXiv text decays ${\sim}$3$\times$ slower than C4 ($\lambda \approx 1.0$ vs.\ $2.9$), with a correspondingly higher convergence floor (${\sim}$0.007--0.009 vs.\ ${\sim}$0.003--0.004).
47	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-299-Formulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, this accounts for the elevated $\Kempirical{=}3$.
48	--
49	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-445-\midrule
50	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-446-Qwen-1.5B      & Wiki  & .588 & $\mathbf{9.4{\times}10^{-4\,***}}$ (.570) & $\mathbf{2.3{\times}10^{-4\,***}}$ (.568) & .655 (.590) \\
51	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-447-Pythia          & Wiki  & .560 & .180 (.567)            & .540 (.564)              & .369 (.564) \\
52	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:448:OLMo            & Wiki  & .500 & .868 (.502)            & .705 (.503)              & .751 (.502) \\
53	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-449-LLaMA-8B        & Wiki  & .573 & .252 (.579)            & .270 (.579)              & .110 (.580) \\
54	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-450-\midrule
55	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-451-Qwen-1.5B      & arXiv & .781 & .156 (.774)            & .079 (.772)              & .364 (.777) \\
56	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-452-Pythia          & arXiv & .733 & .232 (.727)            & .384 (.728)              & .735 (.732) \\
57	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:453:OLMo            & arXiv & .493 & .520 (.487)            & .681 (.489)              & .759 (.496) \\
58	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-454-Qwen-7B         & arXiv & .757 & .160 (.749)            & .327 (.751)              & .733 (.758) \\
59	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-455-Mistral-7B      & arXiv & .742 & .524 (.738)            & .633 (.739)              & .225 (.748) \\
60	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-456-\bottomrule
61	--
62	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-512-The single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\hat{\theta}{=}0.5725$ but below the global $\theta{=}0.60$; this configuration is also the only rewrite-mode model, the discrepancy is therefore attributable to mode rather than threshold instability.
63	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-513-The derived $\hat{\theta}$ values span $[0.5725, 0.6004]$, and $\theta{=}0.60$ falls within this range.
64	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-514-
65	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:515:ArXiv corroborates with 6/6 agreement (100\%), though the wide $\hat{\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.
66	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-516-
67	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-517-Wikipedia yields only 1/6 agreement (17\%).
68	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-518-This failure is expected: most models produce near-chance 1v2 AUC on Wikipedia ($0.499$--$0.619$), so the gap between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ is narrow or inverted, the gap-based threshold derivation is therefore invalid.
69	--
70	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-528-Domain & Held-out & Model & $\text{AUC}_{1\text{v}2}$ & $\text{AUC}_{2\text{v}3}$ & $\hat{\theta}$ & $K^*_{\hat{\theta}}$ & $K^*_{0.60}$ & Match \\
71	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-529-\midrule
72	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-530-C4 & Pythia & Pythia-1.4B & 0.6539 & 0.5515 & 0.5914 & 2 & 2 & \cmark \\
73	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:531: & OLMo & OLMo-1B & 0.6146 & 0.5497 & 0.5914 & 2 & 2 & \cmark \\
74	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-532- & Qwen & Qwen-1.5B-RW & 0.6957 & 0.5893 & 0.5725 & 3 & 2 & \xmark \\
75	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-533- &  & Qwen-7B & 0.6178 & 0.5460 & 0.5725 & 2 & 2 & \cmark \\
76	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-534- &  & Qwen-1.5B-base & 0.6262 & 0.5496 & 0.5725 & 2 & 2 & \cmark \\
77	--
78	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-540- & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5725, 0.6004], agreement: 8/9 (89\%)} \\
79	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-541-\midrule
80	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-542-arXiv & Pythia & Pythia-1.4B & 0.8047 & 0.6545 & 0.5735 & 3 & 3 & \cmark \\
81	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:543: & OLMo & OLMo-1B & 0.5034 & 0.5069 & 0.7296 & 1 & 1 & \cmark \\
82	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-544- & Qwen & Qwen-1.5B & 0.8581 & 0.6436 & 0.5789 & 3 & 3 & \cmark \\
83	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-545- &  & Qwen-7B & 0.8347 & 0.6255 & 0.5789 & 3 & 3 & \cmark \\
84	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-546- & LLaMA & LLaMA-3.1-8B & 0.8447 & 0.6215 & 0.5789 & 3 & 3 & \cmark \\
85	--
86	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-549- & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5735, 0.7296], agreement: 6/6 (100\%)} \\
87	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-550-\midrule
88	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-551-Wikipedia & Pythia & Pythia-1.4B & 0.5846 & 0.5445 & 0.5274 & 3 & 1 & \xmark \\
89	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:552: & OLMo & OLMo-1B & 0.4986 & 0.5012 & 0.5557 & 1 & 1 & \cmark \\
90	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-553- & Qwen & Qwen-1.5B & 0.6193 & 0.5498 & 0.5215 & 4 & 2 & \xmark \\
91	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-554- &  & Qwen-7B & 0.6108 & 0.5562 & 0.5215 & 4 & 2 & \xmark \\
92	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-555- & LLaMA & LLaMA-3.1-8B & 0.5954 & 0.5392 & 0.5274 & 3 & 1 & \xmark \\
93	--
94	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-73-(2)~\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\ref{sec:extended_limitations}), so prompt-chain $\Kempirical$ may underestimate discriminability in mixed settings.
95	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-74-(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
96	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-75-(4)~\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation drops this to $\Kempirical{=}1$ (Section~\ref{sec:transfer}). LLaMA-3.1-8B (C4) and Mistral-7B-v0.3 (code) represent the most marginal $\Kempirical{=}2$ assignments, with 1v2 CI lower bounds within 0.3 percentage points of $\theta$.
97	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:76:(5)~\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\Ktheory$ may be strictly higher); $K^*_{\text{neural}}$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).
98	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-77-(6)~\emph{Segment length}: $\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \theta$); 512 tokens yields point estimate $\Kempirical{=}2$ but CI lower marginally below $\theta$ ($0.5979$); the boundary weakens at longer generation lengths.
99	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-78-(7)~\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\%; Appendix~\ref{sec:dose_response}).
100	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-79-(8)~\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.
101	--
102	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-2-\label{sec:experiments}
103	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-3-
104	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-4-We evaluate generational depth estimation on nine model configurations spanning five architecture families:
105	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:5:Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.
106	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-6-All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5; power analysis in Appendix~\ref{sec:power_curve}).
107	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-7-
108	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-8-%% ====================================================================
109	--
110	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-19-\label{tab:kstar_ci}
111	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-20-\begin{tabular}{lcccccccccc}
112	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-21-\toprule
113	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:22: & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
114	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-23-\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
115	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-24- & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
116	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-25-\midrule
117	--
118	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-44-Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical{=}2$ across all five tested architecture families on C4, with 8/9 individual configurations (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$); Qwen contributes 5 configurations spanning three scales (1.5B, 7B, 14B).
119	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-45-Mistral-7B is the sole exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$; Section~\ref{sec:boundary_cases}).
120	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-46-LLaMA-3.1-8B yields $\Kempirical{=}2$ (1v2 $\auc = 0.6123$, CI $[0.603, 0.622]$; borderline: 1/5 folds below $\theta$; Table~\ref{tab:kstar_ci_extended}).
121	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:47:Among non-Qwen families: Pythia and OLMo yield clear $\Kempirical{=}2$, LLaMA is borderline (CI lower $= 0.603$), and Mistral yields $\Kempirical{=}1$.
122	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-48-An independent F1@0.50 analysis confirms the same boundary for all configurations (Appendix~\ref{sec:f1_validation}).
123	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-49-All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
124	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-50-The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across models in continuation mode ($\Delta = 3.9$\,pp).
125	--
126	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-70-\begin{figure}[t]
127	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-71-\centering
128	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-72-\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
129	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:73:\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
130	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-74-\label{fig:transfer_heatmap}
131	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-75-\end{figure}
132	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-76-
133	--
134	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-79-Qwen-rewrite classifiers transfer poorly (61--63\%), consistent with reliance on mode-specific artifacts.
135	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-80-
136	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-81-\paragraph{Cross-scorer validation.}
137	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:82:Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$; Table~\ref{tab:crossscorer}).
138	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-83-$\Kempirical$ is robust for non-borderline configurations: across 22 cross-scorer configurations on C4 and arXiv, $\Kempirical$ was preserved in 20; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are the most marginal boundary configurations, with AUC within 0.002 of $\theta$.
139	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-84-Qwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp (Table~\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\theta$.
140	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-85-For arXiv, Pythia-1.4B cross-scoring preserves $\Kempirical{=}3$ for 3/4 generators (2v3 $\auc$: 0.608--0.632); Qwen-7B drops to borderline $\Kempirical{=}2$ ($\Delta = -2.7$\,pp), consistent with Qwen scorer sensitivity on C4 and Wikipedia (Table~\ref{tab:arxiv_crossscorer_ci}).
141	--
142	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-102-\subsection{Neural Probe}
143	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-103-\label{sec:neural_probe}
144	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-104-
145	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:105:Replacing the 15D features with frozen encoder hidden states (MLP probe, 5{,}000 texts per depth; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $K^*_{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia and OLMo remain at $K^*_{\text{neural}} = 2$ ($\auc_{2v3}$: 0.5963, 0.5892).
146	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-106-The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D statistical features yield consistent $\Kempirical = 2$ across all families.
147	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-107-
148	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-108-\noindent\begin{minipage}{\columnwidth}
149	--
150	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-117-\midrule
151	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-118-Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
152	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-119-Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
153	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:120:OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
154	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-121-\bottomrule
155	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-122-\end{tabular}}
156	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-123-\end{minipage}
157	--
158	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-156-All five domain-competent models yield $\Kempirical{=}3$ on arXiv, with boundary-pair $\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\theta$.
159	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-157-The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.
160	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-158-Removing LaTeX markup reduces 2v3 AUC by ${\sim}$1.8\,pp but preserves $\Kempirical{=}3$ (CI lower $= 0.610 > \theta$; Table~\ref{tab:latex_ablation}); content-level properties dominate.
161	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:159:OLMo-1B is a capacity failure (0v1 JSD $= 0.33$, near-total information loss), not a counter-example.
162	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-160-Mistral-7B provides the strongest domain-dependence evidence: $\Kempirical{=}1$ on C4 (Section~\ref{sec:boundary_cases}) but $\Kempirical{=}3$ on arXiv: domain structure alone can shift $\Kempirical$ by two levels within the same model.
163	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-161-
164	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-162-\paragraph{Wikipedia ($\Kempirical{=}1$): single-generation saturation.}
165	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:163:With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\Kempirical{=}1$ on Wikipedia: 1v2 $\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\theta$.
166	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-164-Wikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.
167	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-165-Same-family scoring inflates Qwen $\Kempirical$ to 2 on Wikipedia ($\Delta = +2.4$\,pp); cross-family scoring controls this bias without affecting C4 results (Appendix~\ref{sec:wiki_domain}).
168	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-166-
169	--
170	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-176-\noindent\begin{minipage}{\columnwidth}
171	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-177-\centering
172	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-178-\footnotesize
173	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:179:\captionof{table}{Domain $\times$ Model $\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure. $^\dagger$Same-family scorer yields $\Kempirical{=}2$; controlled value shown. $^\ddagger$Borderline: Pythia CI upper $= 0.603$, Mistral CI lower $= 0.603$.}
174	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-180-\label{tab:domain_kstar}
175	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-181-\resizebox{\columnwidth}{!}{%
176	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-182-\begin{tabular}{lcccc}
177	--
178	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-186-Qwen-1.5B    & 2 & 2 & 3 & 1$^\dagger$ \\
179	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-187-Qwen-7B      & 2 & 2 & 3 & 1$^\dagger$ \\
180	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-188-Pythia-1.4B  & 2 & 1$^\ddagger$ & 3 & 1 \\
181	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:189:OLMo-1B      & 2 & --- & 1$^*$ & 1 \\
182	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-190-LLaMA-3.1-8B & 2 & 2 & 3 & 1 \\
183	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-191-Mistral-7B   & 1 & 2$^\ddagger$ & 3 & 1 \\
184	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-192-\bottomrule
185	--
186	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-637-
187	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-638-[3]
188	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-639-Underfull \hbox (badness 2547) in paragraph at lines 48--53
189	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log:640:\T1/ptm/m/n/10.95 (+20) Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and
190	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-641- []
191	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-642-
192	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-643-) (./experiments_c1.tex
193	--
194	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-994-
195	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-995-
196	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-996-Underfull \hbox (badness 10000) in paragraph at lines 515--516
197	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log:997:\T1/ptm/m/n/10.95 (+20) flects OLMo-1B's near-chance per-for-mance
198	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-998- []
199	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-999-
200	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.log-1000-[23]) [24] [25] [26
201	--
202	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-14-Pythia        & 1.4B & \textbf{2} & 0.6539~(1v2) & \textbf{3} & 0.6545~(2v3) & \textbf{1} & 0.975~(0v1) \\
203	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-15-LLaMA-3.1    & 8B   & \textbf{2} & 0.6123~(1v2) & \textbf{3} & 0.6215~(2v3) & \textbf{1} & 0.932~(0v1) \\
204	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-16-Mistral       & 7B   & 1\textsuperscript{$\ddagger$} & 0.594~(1v2) & \textbf{3} & 0.6275~(2v3) & \textbf{1} & 0.961~(0v1) \\
205	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex:17:OLMo          & 1B   & \textbf{2} & 0.6145~(1v2) & 1\textsuperscript{$*$} & --- & \textbf{1} & 0.993~(0v1) \\
206	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-18-\bottomrule
207	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-19-\end{tabular}
208	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-20-}
209	--
210	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-23-{\footnotesize
211	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-24-\textsuperscript{$\dagger$}Scorer artifact: Qwen-1.5B scorer yields $K^*{=}2$; cross-family scorer (Pythia-1.4B) yields $K^*{=}1$ ($\Delta = -2.4$\,pp). Controlled value shown (Appendix~\ref{app:crossscorer}).\\
212	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-25-\textsuperscript{$\ddagger$}AUC(1v2)${=}0.594{<}\theta{=}0.60$: Mistral exhibits domain-specific one-wash on C4 web text. Cross-scorer validated: Pythia-1.4B also yields $K^*{=}1$ (AUC${=}0.570$).\\
213	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex:26:\textsuperscript{$*$}Capacity failure: OLMo-1B produces out-of-domain text when prompted with arXiv content.\\
214	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-27-\textsuperscript{$\S$}Wikipedia 0v1 AUC not available for Qwen-1.5B in base continuation mode.
215	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-28-}
216	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar_full.tex-29-\end{table*}
217	--
218	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex-6-% --- Qwen-RW block ---
219	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex-7-Qwen-1.5B (self) & Qwen-RW & 2 & --- & 0.6955 & --- \\
220	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex-8-Pythia-1.4B       & Qwen-RW & 2 & 0.9923 & 0.7012 & 0.906 \\
221	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex:9:OLMo-1B           & Qwen-RW & 2 & 0.9918 & 0.6947 & 0.920 \\
222	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex-10-\midrule
223	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex-11-% --- Qwen-cont block ---
224	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex-12-Qwen-1.5B (self) & Qwen-cont & 2 & --- & 0.6112 & --- \\
225	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex-13-Pythia-1.4B       & Qwen-cont & \textcolor{red}{1\textsuperscript{$\dagger$}} & 0.9900 & \underline{0.5923} & 0.942 \\
226	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex:14:OLMo-1B           & Qwen-cont & \textcolor{red}{1\textsuperscript{$\dagger$}} & 0.9890 & \underline{0.5858} & 0.902 \\
227	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex-15-\midrule
228	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex-16-% --- Qwen-7B cross-scale block ---
229	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_crossscorer.tex-17-Qwen-1.5B        & Qwen-7B-cont & 2 & 0.9644 & 0.6178 & --- \\
230	--
231	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-12-Pythia        & 1.4B & \textbf{2} & \textbf{3} & \textbf{1} \\
232	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-13-LLaMA-3.1    & 8B   & \textbf{2} & \textbf{3} & \textbf{1} \\
233	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-14-Mistral       & 7B   & 1\textsuperscript{$\ddagger$} & \textbf{3} & \textbf{1} \\
234	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex:15:OLMo          & 1B   & \textbf{2} & 1\textsuperscript{$*$} & \textbf{1} \\
235	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-16-\midrule
236	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-17-\textit{Dominant} & & \textbf{2} & \textbf{3} & \textbf{1} \\
237	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-18-\bottomrule
238	--
239	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-23-{\footnotesize
240	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-24-\textsuperscript{$\dagger$}Scorer artifact: Qwen-1.5B scorer yields $K^*{=}2$; Pythia scorer yields $K^*{=}1$ (see \S\ref{sec:crossscorer}).\\
241	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-25-\textsuperscript{$\ddagger$}Domain-specific one-wash: AUC(1v2)${=}0.594{<}\theta$; arXiv rescues to $K^*{=}3$. Cross-scorer validated: Pythia-1.4B also yields $K^*{=}1$ (AUC${=}0.570$).\\
242	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex:26:\textsuperscript{$*$}Capacity failure: OLMo-1B generates out-of-domain text on arXiv.
243	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-27-}
244	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/tables/tab_domain_model_kstar.tex-28-\end{table}
245	--
246	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-45-\subsection{Experimental Setup}
247	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-46-\label{sec:experimental_setup}
248	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-47-
249	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:48:We evaluate nine configurations spanning five architecture families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).
250	/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex-49-Each uses 5{,}000 C4~\cite{raffel2020t5} seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
251	
252	[Showing results with pagination = limit: 250]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbf29b1b-5096-4b5d-aa54-558a5f0be6d8",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "16fcf13c-3a42-4989-ac7e-a18f919ae433",
  "sourceToolAssistantUUID": "fbf29b1b-5096-4b5d-aa54-558a5f0be6d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T23:01:05.352Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01V2SDCNWgeA4KqadQHWK36h`</summary>

```json
{
  "pattern": "wiki.*K\\*|K\\*.*wiki",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16fcf13c-3a42-4989-ac7e-a18f919ae433",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzZL4m9DWMoz3fwhcn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b142850-e151-4809-ad9b-7a7f5f38f41c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019uHXMUmF8u5YDCzqnFkHp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12172,
      "cache_read_input_tokens": 22992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12172,
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

_source line 24 · 2026-05-19T23:01:05.373Z_

<details><summary>↩ Tool result · `toolu_01V2SDCNWgeA4KqadQHWK36h`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b142850-e151-4809-ad9b-7a7f5f38f41c",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "904df8da-e582-4f0e-bf5a-06f25cd13407",
  "sourceToolAssistantUUID": "0b142850-e151-4809-ad9b-7a7f5f38f41c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T23:01:05.777Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SuGafwGxPYJ5HXaFjJ2NmM`</summary>

```json
{
  "pattern": "Wikipedia.*K\\*|K\\*.*Wikipedia",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "904df8da-e582-4f0e-bf5a-06f25cd13407",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzZL4m9DWMoz3fwhcn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ae4ca25a-6242-452c-bd62-e9bdaa3b1fe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019uHXMUmF8u5YDCzqnFkHp8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12172,
      "cache_read_input_tokens": 22992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12172,
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

_source line 26 · 2026-05-19T23:01:05.793Z_

<details><summary>↩ Tool result · `toolu_01SuGafwGxPYJ5HXaFjJ2NmM`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae4ca25a-6242-452c-bd62-e9bdaa3b1fe0",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "e7ad68ac-60aa-45bf-9dbf-d39e3c00ea7b",
  "sourceToolAssistantUUID": "ae4ca25a-6242-452c-bd62-e9bdaa3b1fe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T23:01:06.128Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LrozmWs2rXsu8faoeV1gEU`</summary>

```json
{
  "pattern": "DeBERTa",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7ad68ac-60aa-45bf-9dbf-d39e3c00ea7b",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzZL4m9DWMoz3fwhcn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e26829a0-b62e-4d1b-8117-b6220b4c68f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019uHXMUmF8u5YDCzqnFkHp8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12172,
      "cache_read_input_tokens": 22992,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12172
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 557,
          "cache_read_input_tokens": 22992,
          "cache_creation_input_tokens": 12172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12172,
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

_source line 28 · 2026-05-19T23:01:06.149Z_

<details><summary>↩ Tool result · `toolu_01LrozmWs2rXsu8faoeV1gEU`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-68-\section*{Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-69-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-70-Our findings are bounded by:
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:71:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-72-The 1.5B$\to$32B trend shows stable $\Kempirical{=}2$ with declining 1v2 AUC; whether this holds at 70B+ scales remains unverified.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-73-(2)~\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\ref{sec:extended_limitations}), so prompt-chain $\Kempirical$ may underestimate discriminability in mixed settings.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-74-(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex-4-Under prompt-chain recursion, $\Kempirical{=}2$ for web text at $\theta{=}0.60$ (8/9 configurations; stable across $\theta \in [0.575, 0.625]$), $\Kempirical{=}1$--$2$ for code, and $\Kempirical{=}3$ for arXiv; retrain-chain extends to $\Kempirical{=}7$ (Appendix~\ref{sec:extended_limitations}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex-5-The domain ordering (arXiv $>$ C4 $\geq$ Code $>$ Wikipedia) is $\theta$-invariant.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex:6:DeBERTa-v3-base confirms $\Kempirical{=}2$ on C4 at both 14B and 32B, though on Wikipedia it extends $\Kempirical$ to 3, revealing domain-dependent classifier sensitivity; future work includes retrain-chain measurement and trends beyond 32B.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-122-\end{tabular}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-123-\end{minipage}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-124-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:125:\paragraph{Fine-tuned DeBERTa upper bound.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:126:To test whether classifier strength or generator scale shifts the boundary, we train DeBERTa-v3-base ordinal classifiers on C4 generations at 14B and 32B scales (Table~\ref{tab:deberta_comparison}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:127:On C4, DeBERTa raises 1v2 $\auc$ over LightGBM at both scales (14B: $0.678$ vs.\ $0.621$; 32B: $0.694$ vs.\ $0.618$), yet $\Kempirical{=}2$ is preserved (all 2v3 CI upper ${<}\,\theta$); LightGBM $\auc$ shifts by ${<}\,0.5$\,pp between 14B and 32B, confirming both scale and representation invariance on web text.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:128:On Wikipedia, however, DeBERTa extends $\Kempirical$ from ${\leq}\,2$ (OBD) to $3$ (3/4 configurations), revealing a domain-dependent classifier gap: contextualized representations retain depth signal that 15D statistics lose in structurally simpler domains.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-129-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-130-\noindent\begin{minipage}{\columnwidth}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-131-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-132-\footnotesize
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:133:\captionof{table}{DeBERTa-v3-base vs.\ LightGBM on C4 generations at two scales. Both classifiers yield $\Kempirical{=}2$ at 14B and 32B.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-134-\label{tab:deberta_comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-135-\begin{tabular}{lcccc}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-136-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-137-& \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & \textbf{3v4} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-138-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-139-LightGBM (14B)  & .960 & .621 & .572 & .537 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:140:DeBERTa (14B)   & .994 & .678 & .590 & .565 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-141-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-142-LightGBM (32B)  & .958 & .618 & .545 & ---  \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:143:DeBERTa (32B)   & .993 & .694 & .594 & ---  \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-144-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-145-\end{tabular}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-146-\end{minipage}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-200-Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $K^*_{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-201-The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-202-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:203:In summary, $\Kempirical{=}2$ for web text is consistent across five architecture families (1B--32B), four decoding strategies, and two classifier representations (LightGBM, DeBERTa); the $\theta$-invariant domain ordering arXiv $>$ C4/Code $>$ Wikipedia is driven by structural complexity rather than model identity.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-23-Token-level JSD between adjacent generations reveals two decay regimes (Figure~\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\times$) followed by rapid convergence, while arXiv decays ${\sim}$3$\times$ slower ($\lambda \approx 1.0$ vs.\ $2.9$); the retrain-chain ($\lambda = 0.285$, no cliff) extends $\Kempirical$ to 7 via cumulative model-adaptation artifacts (Appendix~\ref{sec:jsd_extended}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-24-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-25-\paragraph{Domain and representation dependence.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:26:The domain ordering (arXiv $>$ C4 $\geq$ Code $>$ Wikipedia) correlates with structural complexity (Table~\ref{tab:domain-ttr-entropy}); the classifier gap is itself domain-dependent, with $\Kempirical$ invariant to representation on C4 but DeBERTa extending $\Kempirical$ to 3 on Wikipedia (Section~\ref{sec:neural_probe}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-27-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-523-\@writefile{lot}{\contentsline {table}{\numberline {3}{\ignorespaces Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $K^*_{\text  {neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}}{6}{table.3}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-524-\newlabel{tab:neural_probe_crossmodel}{{3}{6}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $K^*_{\text {neural}}$: maximum depth where AUC exceeds $\theta = 0.60$}{table.3}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-525-\@LN{424}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:526:\@writefile{toc}{\contentsline {paragraph}{Fine-tuned DeBERTa upper bound.}{6}{section*.15}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-527-\@LN{425}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-528-\@LN{426}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-529-\@LN{427}{5}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-539-\@LN{437}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-540-\@LN{438}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-541-\@LN{439}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:542:\@writefile{lot}{\contentsline {table}{\numberline {4}{\ignorespaces DeBERTa-v3-base vs.\ LightGBM on C4 generations at two scales. Both classifiers yield ${K^*}{=}2$ at 14B and 32B.}}{6}{table.4}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:543:\newlabel{tab:deberta_comparison}{{4}{6}{DeBERTa-v3-base vs.\ LightGBM on C4 generations at two scales. Both classifiers yield $\Kempirical {=}2$ at 14B and 32B}{table.4}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-544-\@LN{440}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-545-\@LN{441}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-546-\@writefile{toc}{\contentsline {subsection}{\numberline {4.5}Cross-Domain Variation}{6}{subsection.4.5}\protected@file@percent }
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e26829a0-b62e-4d1b-8117-b6220b4c68f1",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "0789c170-2063-4568-87d3-a0416f91d718",
  "sourceToolAssistantUUID": "e26829a0-b62e-4d1b-8117-b6220b4c68f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-19T23:01:07.991Z_

Now let me search more specifically for references to classifier-dependent and representation-independent patterns:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0789c170-2063-4568-87d3-a0416f91d718",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzwSbJX9RH5snjDGTZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cda09aa3-4847-48ec-9600-2cca7498efd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YNJbJRzygxGCy4z2mTxBfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23623,
      "cache_read_input_tokens": 35164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23623,
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

_source line 30 · 2026-05-19T23:01:08.647Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GLJ5CUkyQ6VmVbSw7UQL2L`</summary>

```json
{
  "pattern": "neural_probe|neural probe",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cda09aa3-4847-48ec-9600-2cca7498efd0",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzwSbJX9RH5snjDGTZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "168abdda-cdc1-4129-bb8b-656ce481d256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YNJbJRzygxGCy4z2mTxBfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23623,
      "cache_read_input_tokens": 35164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23623,
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

_source line 31 · 2026-05-19T23:01:08.675Z_

<details><summary>↩ Tool result · `toolu_01GLJ5CUkyQ6VmVbSw7UQL2L`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex-25-\paragraph{Ordinal classification and probing.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex-26-Our surprisal features build on information-theoretic processing cost~\cite{hale2001surprisal, levy2008expectation}, repurposed to track generational degradation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex-27-Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; CORAL~\cite{cao2020coral} provides a rank-consistent neural alternative.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:28:Our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-68-\section*{Limitations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-69-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-70-Our findings are bounded by:
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:71:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-72-The 1.5B$\to$32B trend shows stable $\Kempirical{=}2$ with declining 1v2 AUC; whether this holds at 70B+ scales remains unverified.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-73-(2)~\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\ref{sec:extended_limitations}), so prompt-chain $\Kempirical$ may underestimate discriminability in mixed settings.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex-74-(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-100-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-101-%% ====================================================================
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-102-\subsection{Neural Probe}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:103:\label{sec:neural_probe}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-104-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:105:Replacing the 15D features with frozen encoder hidden states (MLP probe, 5{,}000 texts per depth; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $K^*_{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia and OLMo remain at $K^*_{\text{neural}} = 2$ ($\auc_{2v3}$: 0.5963, 0.5892).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-106-The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D statistical features yield consistent $\Kempirical = 2$ across all families.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-107-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-108-\noindent\begin{minipage}{\columnwidth}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-109-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-110-\footnotesize
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-111-\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $K^*_{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:112:\label{tab:neural_probe_crossmodel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-113-\resizebox{\columnwidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-114-\begin{tabular}{lccc}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-115-\toprule
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-23-Token-level JSD between adjacent generations reveals two decay regimes (Figure~\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\times$) followed by rapid convergence, while arXiv decays ${\sim}$3$\times$ slower ($\lambda \approx 1.0$ vs.\ $2.9$); the retrain-chain ($\lambda = 0.285$, no cliff) extends $\Kempirical$ to 7 via cumulative model-adaptation artifacts (Appendix~\ref{sec:jsd_extended}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-24-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-25-\paragraph{Domain and representation dependence.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:26:The domain ordering (arXiv $>$ C4 $\geq$ Code $>$ Wikipedia) correlates with structural complexity (Table~\ref{tab:domain-ttr-entropy}); the classifier gap is itself domain-dependent, with $\Kempirical$ invariant to representation on C4 but DeBERTa extending $\Kempirical$ to 3 on Wikipedia (Section~\ref{sec:neural_probe}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex-27-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-316-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-317-  \small
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-318-  \captionof{table}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:319:  \label{tab:s7_neural_probe}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-320-  \resizebox{\textwidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-321-  \begin{tabular}{ll}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-322-    \toprule
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-509-\@LN{413}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-510-\@LN{414}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-511-\@writefile{toc}{\contentsline {subsection}{\numberline {4.4}Neural Probe}{6}{subsection.4.4}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:512:\newlabel{sec:neural_probe}{{4.4}{6}{Neural Probe}{subsection.4.4}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-513-\@LN{415}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-514-\@LN{416}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-515-\@LN{417}{5}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-521-\@LN{422}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-522-\@LN{423}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-523-\@writefile{lot}{\contentsline {table}{\numberline {3}{\ignorespaces Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $K^*_{\text  {neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}}{6}{table.3}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:524:\newlabel{tab:neural_probe_crossmodel}{{3}{6}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $K^*_{\text {neural}}$: maximum depth where AUC exceeds $\theta = 0.60$}{table.3}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-525-\@LN{424}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-526-\@writefile{toc}{\contentsline {paragraph}{Fine-tuned DeBERTa upper bound.}{6}{section*.15}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-527-\@LN{425}{5}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1405-\@writefile{lot}{\contentsline {table}{\numberline {16}{\ignorespaces LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt  {doc\_id} to prevent data leakage from the same seed document appearing in both train and test.}}{17}{table.caption.41}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1406-\newlabel{tab:s6_lgbm_params}{{16}{17}{LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper. One binary classifier is trained per adjacent depth pair $(k, k{+}1)$; 5-fold GroupKFold cross-validation is grouped by \texttt {doc\_id} to prevent data leakage from the same seed document appearing in both train and test}{table.caption.41}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1407-\@writefile{lot}{\contentsline {table}{\numberline {17}{\ignorespaces Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP.}}{17}{table.caption.41}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1408:\newlabel{tab:s7_neural_probe}{{17}{17}{Neural probe architecture and training details (Exp-015). Applied to all three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B): each model's frozen hidden states are average-pooled into document embeddings and classified by a two-hidden-layer MLP}{table.caption.41}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1409-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1410-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1411-\@LN@col{1}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "168abdda-cdc1-4129-bb8b-656ce481d256",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "41d20a6e-2764-49bb-b330-7309a2ffd42d",
  "sourceToolAssistantUUID": "168abdda-cdc1-4129-bb8b-656ce481d256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-19T23:01:09.305Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HGYxbdJ8UuDumQNUi9feJ8`</summary>

```json
{
  "pattern": "OBD|baseline",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 2,
  "head_limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41d20a6e-2764-49bb-b330-7309a2ffd42d",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzwSbJX9RH5snjDGTZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "47998d46-7c16-4583-a312-0089c0e19ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YNJbJRzygxGCy4z2mTxBfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23623,
      "cache_read_input_tokens": 35164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23623,
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

_source line 33 · 2026-05-19T23:01:09.320Z_

<details><summary>↩ Tool result · `toolu_01HGYxbdJ8UuDumQNUi9feJ8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex-25-\paragraph{Ordinal classification and probing.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex-26-Our surprisal features build on information-theoretic processing cost~\cite{hale2001surprisal, levy2008expectation}, repurposed to track generational degradation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:27:Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; CORAL~\cite{cao2020coral} provides a rank-consistent neural alternative.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex-28-Our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.bbl-372-\bibitem[{Zhang et~al.(2024)Zhang, Zheng, Gao, and Miao}]{zhang2024minkpp}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.bbl-373-Jingyang Zhang, Jingwei Zheng, Jing Gao, and Chunyan Miao. 2024.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.bbl:374:\newblock Min-{K}\%++: Improved baseline for detecting pre-training data from
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.bbl-375-  large language models.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.bbl-376-\newblock In \emph{Proceedings of EMNLP}.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-106-\setlength\columnsep{0.6cm}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-107-\newlength\titlebox
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:108:\setlength\titlebox{11\baselineskip}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:109:% \titlebox should be a multiple of \baselineskip so that
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-110-% column height remaining fits an exact number of lines of text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-111-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-200-% instead.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-201-\def\thebibliography#1{\vskip\parskip%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:202:\vskip\baselineskip%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:203:\def\baselinestretch{1}%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-204-\ifx\@currsize\normalsize\@normalsize\else\@currsize\fi%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-205-\vskip-\parskip%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:206:\vskip-\baselineskip%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-207-\section*{References\@mkboth
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-208- {References}{References}}\list
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-217-% Allow for a bibliography of sources of attested examples
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-218-\def\thesourcebibliography#1{\vskip\parskip%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:219:\vskip\baselineskip%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:220:\def\baselinestretch{1}%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-221-\ifx\@currsize\normalsize\@normalsize\else\@currsize\fi%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-222-\vskip-\parskip%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty:223:\vskip-\baselineskip%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-224-\section*{Sources of Attested Examples\@mkboth
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/acl.sty-225- {Sources of Attested Examples}{Sources of Attested Examples}}\list
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-174-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-175-The strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\ref{sec:filtering}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:176:The small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\Kempirical{=}2$'s predictive value for curation granularity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-177-HellaSwag differences are negligible across all strategies.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-178-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-386-\label{sec:feature_ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-387-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:388:To assess the relative contribution of each feature group to depth discrimination, we train a plain LightGBM classifier (\texttt{n\_estimators}$=$200, \texttt{max\_depth}$=$6; distinct from the OBD-LightGBM used in Section~\ref{sec:method}) on the 1\,vs.\,2 task using (a) each feature group alone (\emph{single}) and (b) the full 15D set minus one group (\emph{leave-one-out}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-389-Representative models per domain: LLaMA-3.1-8B (C4), Qwen-1.5B continuation (arXiv), and the domain ablation configuration (Wikipedia).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-390-
--

[Showing results with pagination = limit: 50]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47998d46-7c16-4583-a312-0089c0e19ce5",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "0bce934d-9a9e-4c0b-95d7-046e61715197",
  "sourceToolAssistantUUID": "47998d46-7c16-4583-a312-0089c0e19ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T23:01:09.595Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QDKQoLYhqiNSBKxQG1HeLF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bce934d-9a9e-4c0b-95d7-046e61715197",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCkzwSbJX9RH5snjDGTZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "65caae33-78b6-41fd-97d6-3473ff9e5f99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YNJbJRzygxGCy4z2mTxBfp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23623,
      "cache_read_input_tokens": 35164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23623,
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

_source line 35 · 2026-05-19T23:01:09.601Z_

<details><summary>↩ Tool result · `toolu_01QDKQoLYhqiNSBKxQG1HeLF`</summary>

```text
1	% EMNLP 2026 Main - ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage{pifont}
18	\newcommand{\cmark}{\ding{51}}
19	\newcommand{\xmark}{\ding{55}}
20	\usepackage{placeins}
21	
22	\newcommand{\Kstar}{{K^*}}
23	\newcommand{\Kempirical}{{K^*}}
24	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
25	\newcommand{\auc}{\text{AUC}}
26	\newcommand{\jsd}{\text{JSD}}
27	\newcommand{\tpm}{\ensuremath{\,\pm\,}}
28	
29	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
30	
31	\author{Anonymous}
32	
33	\begin{document}
34	\maketitle
35	
36	% === Abstract ===
37	\begin{abstract}
38	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
39	We measure the discrimination boundary $\Kempirical$ under prompt-chain generation using 15 statistical features and an OBD-LightGBM classifier.
40	Across five architecture families (1B--14B), four source domains, and four decoding strategies, $\Kempirical{=}2$ for web text at $\theta{=}0.60$ (stable across $\theta \in [0.575, 0.625]$; 8/9 configurations), $\Kempirical{=}1$--$2$ for code, and $\Kempirical{=}3$ for arXiv.
41	A single generation pass renders synthetic web text statistically indistinguishable from deeper generations (\emph{one-wash laundering}).
42	Largely generator-independent features enable 80--92\% accuracy retention at $\leq$1.5B and 96--100\% mean AUC retention at 7B across tested continuation-mode generators, though boundary-level transfer remains fragile; cross-scorer validation confirms $\Kempirical$ robustness for non-borderline configurations (20/22).
43	As a consistency check, $\Kempirical{=}2$ correctly predicts binary $>$ graduated filtering for web text, though with limited effect sizes (0.76\,pp MMLU).
44	\end{abstract}
45	
46	% === Section 1: Introduction ===
47	\input{introduction}
48	
49	% === Section 2: Related Work ===
50	\input{related_work}
51	
52	% === Section 3: Method ===
53	\input{method}
54	
55	% === Section 4: Experiments ===
56	\input{experiments_c1}
57	
58	% === Section 5: K*-Aware Data Filtering ===
59	\input{experiments_c3}
60	
61	% === Section 6: Discussion ===
62	\input{discussion}
63	
64	% === Section 7: Conclusion ===
65	\input{conclusion}
66	
67	% === Limitations (ACL required, unnumbered) ===
68	\section*{Limitations}
69	
70	Our findings are bounded by:
71	(1)~\emph{Scope}: full 9-configuration characterization at $\leq$14B (5 architecture families), with 32B-scale validation via LightGBM and DeBERTa (Section~\ref{sec:neural_probe}); English text (C4, Wikipedia, arXiv) and Python code (CodeSearchNet), four decoding strategies; arXiv $\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model); code domain tested with five models across four families (Qwen2.5-1.5B/7B, LLaMA-3.1-8B, Mistral-7B-v0.3, $\Kempirical{=}2$; Pythia-1.4B, $\Kempirical{=}1$ with 1v2 CI upper bound $> \theta$); subsampling analysis indicates $n{\geq}2{,}000$ suffices for 100\% reliable $\Kempirical$ determination (Appendix~\ref{sec:power_curve}).
72	The 1.5B$\to$32B trend shows stable $\Kempirical{=}2$ with declining 1v2 AUC; whether this holds at 70B+ scales remains unverified.
73	(2)~\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\ref{sec:extended_limitations}), so prompt-chain $\Kempirical$ may underestimate discriminability in mixed settings.
74	(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
75	(4)~\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation drops this to $\Kempirical{=}1$ (Section~\ref{sec:transfer}). LLaMA-3.1-8B (C4) and Mistral-7B-v0.3 (code) represent the most marginal $\Kempirical{=}2$ assignments, with 1v2 CI lower bounds within 0.3 percentage points of $\theta$.
76	(5)~\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\Ktheory$ may be strictly higher); $K^*_{\text{neural}}$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).
77	(6)~\emph{Segment length}: $\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \theta$); 512 tokens yields point estimate $\Kempirical{=}2$ but CI lower marginally below $\theta$ ($0.5979$); the boundary weakens at longer generation lengths.
78	(7)~\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\%; Appendix~\ref{sec:dose_response}).
79	(8)~\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.
80	(9)~\emph{Transfer coverage}: cross-model transfer validation shows 80--92\% accuracy retention at $\leq$1.5B (4 configurations) and 96--100\% mean pairwise AUC retention at 7B (3 models, 3 architecture families; Appendix~\ref{sec:7b_transfer}); however, at the $\Kempirical$ boundary (1v2), 4/6 off-diagonal 7B pairs fall below $\theta$, indicating that boundary-level transfer remains fragile even as aggregate transfer strengthens with scale.
81	Additional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\ref{sec:extended_limitations}.
82	
83	% === Ethics Statement (ACL required, unnumbered) ===
84	\section*{Ethics Statement}
85	
86	Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.
87	Our experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.
88	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
89	Code and generated corpora will be released upon acceptance to enable reproducibility.
90	
91	\bibliography{references}
92	
93	\input{appendix}
94	\input{appendix_extended}
95	
96	\end{document}
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65caae33-78b6-41fd-97d6-3473ff9e5f99",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "8d5aacde-c64c-4f89-8f10-96f06f84c6bf",
  "sourceToolAssistantUUID": "65caae33-78b6-41fd-97d6-3473ff9e5f99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-19T23:01:13.024Z_

Let me now search for more specific content about Table 4 and look at Wikipedia domain results:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d5aacde-c64c-4f89-8f10-96f06f84c6bf",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCm1CUDw3qb8sw3diuQT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "864cfe8b-6612-4008-acee-ebf929596868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Xtd8ft43kxeXwLWf7st3UP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10133,
      "cache_read_input_tokens": 58787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10133,
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

_source line 37 · 2026-05-19T23:01:14.528Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01775393HV7Nq9N3JE4E9xpb`</summary>

```json
{
  "pattern": "tab:deberta_comparison|Table.*deberta|deberta.*Table",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "864cfe8b-6612-4008-acee-ebf929596868",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCm1CUDw3qb8sw3diuQT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c125e6c2-1835-4f3c-9aff-ad38493aeeaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Xtd8ft43kxeXwLWf7st3UP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10133,
      "cache_read_input_tokens": 58787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10133,
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

_source line 38 · 2026-05-19T23:01:14.554Z_

<details><summary>↩ Tool result · `toolu_01775393HV7Nq9N3JE4E9xpb`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-121-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-122-\end{tabular}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-123-\end{minipage}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-124-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-125-\paragraph{Fine-tuned DeBERTa upper bound.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:126:To test whether classifier strength or generator scale shifts the boundary, we train DeBERTa-v3-base ordinal classifiers on C4 generations at 14B and 32B scales (Table~\ref{tab:deberta_comparison}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-127-On C4, DeBERTa raises 1v2 $\auc$ over LightGBM at both scales (14B: $0.678$ vs.\ $0.621$; 32B: $0.694$ vs.\ $0.618$), yet $\Kempirical{=}2$ is preserved (all 2v3 CI upper ${<}\,\theta$); LightGBM $\auc$ shifts by ${<}\,0.5$\,pp between 14B and 32B, confirming both scale and representation invariance on web text.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-128-On Wikipedia, however, DeBERTa extends $\Kempirical$ from ${\leq}\,2$ (OBD) to $3$ (3/4 configurations), revealing a domain-dependent classifier gap: contextualized representations retain depth signal that 15D statistics lose in structurally simpler domains.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-129-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-130-\noindent\begin{minipage}{\columnwidth}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-131-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-132-\footnotesize
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-133-\captionof{table}{DeBERTa-v3-base vs.\ LightGBM on C4 generations at two scales. Both classifiers yield $\Kempirical{=}2$ at 14B and 32B.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:134:\label{tab:deberta_comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-135-\begin{tabular}{lcccc}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-136-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-137-& \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & \textbf{3v4} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-138-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-139-LightGBM (14B)  & .960 & .621 & .572 & .537 \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-538-\@LN{436}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-539-\@LN{437}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-540-\@LN{438}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-541-\@LN{439}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-542-\@writefile{lot}{\contentsline {table}{\numberline {4}{\ignorespaces DeBERTa-v3-base vs.\ LightGBM on C4 generations at two scales. Both classifiers yield ${K^*}{=}2$ at 14B and 32B.}}{6}{table.4}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:543:\newlabel{tab:deberta_comparison}{{4}{6}{DeBERTa-v3-base vs.\ LightGBM on C4 generations at two scales. Both classifiers yield $\Kempirical {=}2$ at 14B and 32B}{table.4}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-544-\@LN{440}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-545-\@LN{441}{5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-546-\@writefile{toc}{\contentsline {subsection}{\numberline {4.5}Cross-Domain Variation}{6}{subsection.4.5}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-547-\newlabel{sec:cross_domain}{{4.5}{6}{Cross-Domain Variation}{subsection.4.5}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-548-\@LN{442}{5}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c125e6c2-1835-4f3c-9aff-ad38493aeeaf",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "f850713e-8a5b-4795-833b-422b072532ba",
  "sourceToolAssistantUUID": "c125e6c2-1835-4f3c-9aff-ad38493aeeaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T23:01:14.785Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Beskg5ch77Vb1VcDSNdAH2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f850713e-8a5b-4795-833b-422b072532ba",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCm1CUDw3qb8sw3diuQT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e6d175f0-3892-4b9e-a2a6-d2974034d951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Xtd8ft43kxeXwLWf7st3UP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 10133,
      "cache_read_input_tokens": 58787,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10133
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 263,
          "cache_read_input_tokens": 58787,
          "cache_creation_input_tokens": 10133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10133,
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

_source line 40 · 2026-05-19T23:01:14.791Z_

<details><summary>↩ Tool result · `toolu_01Beskg5ch77Vb1VcDSNdAH2`</summary>

```text
1	\section{Extended Analysis and Limitations}
2	\label{sec:extended_discussion}
3	
4	This section provides supporting tables for cross-scorer validation (Tables~\ref{tab:crossscorer}--\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.
5	
6	\noindent\begin{minipage}{\columnwidth}
7	\centering
8	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
9	\label{tab:crossscorer}
10	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
11	\end{minipage}
12	
13	\begin{table}[htbp]
14	\centering
15	\small
16	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs; 3 generators $\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\eta^2_p = 0.19$) relative to Depth-Pair ($\eta^2_p = 1.00$) and Generator ($\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination (Scorer $\eta^2_p$ is approximately 5$\times$ smaller than Generator and dwarfed by Depth-Pair). Per-fold AUC values within the same generator share seed documents across folds and are not fully independent; we therefore rely on effect-size ratios rather than $p$-values for interpretation.}
17	\label{tab:anova_crossscorer}
18	\begin{tabular}{lrrrr}
19	\toprule
20	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
21	\midrule
22	Generator     & 2  & 926.8  & ${<}.001$  & .885 \\
23	Scorer        & 3  & 19.02  & ${<}.001$  & .192 \\
24	Depth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\
25	Gen$\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\
26	Gen$\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\
27	Scorer$\times$Depth & 12 & 2.45 & .005 & .109 \\
28	Residual      & 240 & & & \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\subsection{Extended Limitations}
34	\label{sec:extended_limitations}
35	
36	\emph{Prompt-chain versus retrain-chain.}
37	Both Qwen2.5-1.5B and Pythia-1.4B yield $\Kempirical{=}7$ under retrain-chain LoRA fine-tuning (Table~\ref{tab:retrain_ci}), extending detectable depth by 5 additional generations beyond prompt-chain $\Kempirical{=}2$.
38	Cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.
39	The two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\ 0.746), yet both converge to $\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \theta$).
40	This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.
41	The extended discriminability under retraining aligns with theoretical analyses of iterative retraining instability on synthetic data~\cite{bertrand2024stability, gerstgrasser2024model}, where each retraining cycle amplifies distributional artifacts beyond the text-intrinsic degradation observed in prompt-chains.
42	Extrapolating yields 7v8 $\approx 0.57 < \theta$ for both models. This places $\Kempirical{=}7$ near the ceiling for retrain-chains.
43	Prompt-chain $\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).
44	
45	\begin{table}[htbp]
46	\centering
47	\small
48	\caption{Retrain-chain pairwise $\auc$ with 5-fold CV 95\% CIs. Both models yield $\Kempirical{=}7$; all CI lower bounds $> \theta{=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\ref{sec:retrain_ci_note}).}
49	\label{tab:retrain_ci}
50	\begin{tabular}{lcccc}
51	\toprule
52	 & \multicolumn{2}{c}{\textbf{Qwen-1.5B}} & \multicolumn{2}{c}{\textbf{Pythia-1.4B}} \\
53	\cmidrule(lr){2-3}\cmidrule(lr){4-5}
54	\textbf{Pair} & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
55	\midrule
56	0v1 & 0.9837 & $[.982,\,.985]$ & 0.9844 & $[.983,\,.986]$ \\
57	1v2 & 0.8971 & $[.895,\,.899]$ & 0.9470 & $[.942,\,.952]$ \\
58	2v3 & 0.8098 & $[.805,\,.814]$ & 0.8891 & $[.882,\,.896]$ \\
59	3v4 & 0.7600 & $[.753,\,.767]$ & 0.7999 & $[.795,\,.805]$ \\
60	4v5 & 0.7459 & $[.738,\,.754]$ & 0.6907 & $[.688,\,.693]$ \\
61	5v6 & 0.7017 & $[.696,\,.708]$ & 0.6497 & $[.643,\,.657]$ \\
62	6v7 & 0.6410 & $[.638,\,.645]$ & 0.6340 & $[.628,\,.641]$ \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\paragraph{CI methodology note.}
68	\label{sec:retrain_ci_note}
69	The main pipeline reports bootstrap 95\% CIs (1{,}000 or 10{,}000 resamples), which are valid because each bootstrap sample preserves the GroupKFold document structure: resampling operates on documents, and all depths of a given document remain together.
70	In the retrain-chain setting, each generation's training corpus is the \emph{output} of the previous generation's fine-tuned model. This creates inter-generation dependencies that standard bootstrap resampling cannot preserve, and naive resampling would inflate AUC estimates.
71	We therefore report fold-based 95\% CIs for retrain-chain experiments, computed as $\bar{x} \pm 1.96 \cdot s / \sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.
72	
73	\emph{Threshold sensitivity.}
74	Table~\ref{tab:theta_sensitivity} reports $\Kempirical$ across $\theta \in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.
75	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
76	
77	\begin{table}[htbp]
78	\centering
79	\small
80	\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
81	\label{tab:theta_sensitivity}
82	\resizebox{\columnwidth}{!}{%
83	\begin{tabular}{llcccc}
84	\toprule
85	\textbf{Condition} & \textbf{Config} & $\theta{=}0.55$ & $\theta{=}0.60$ & $\theta{=}0.625$ & $\theta{=}0.70$ \\
86	\midrule
87	C4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\
88	C4 (web) & Pythia       & 2 & 2 & 2 & 1 \\
89	C4 (web) & OLMo         & 2 & 2 & 1 & 1 \\
90	C4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\
91	C4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\
92	C4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\
93	\midrule
94	arXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\
95	arXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\
96	\midrule
97	Cross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\
98	Cross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\
99	\bottomrule
100	\end{tabular}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6d175f0-3892-4b9e-a2a6-d2974034d951",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "bc11c2d2-c830-42a8-a911-66bff19b1ffb",
  "sourceToolAssistantUUID": "e6d175f0-3892-4b9e-a2a6-d2974034d951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-19T23:01:16.403Z_

Perfect! Now let me search for the Wikipedia domain table and compile the complete findings:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc11c2d2-c830-42a8-a911-66bff19b1ffb",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCm1arsJykJLu7mjBFyk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "925d40eb-a5d6-4b96-9d00-a59e59889b4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01REu2HZspnBFiS8DVVQcN1d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5445,
      "cache_read_input_tokens": 68920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5445,
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

_source line 42 · 2026-05-19T23:01:17.696Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FMnc4ueNLXdeYRHUgs2Yew`</summary>

```json
{
  "pattern": "wiki_domain|Wikipedia domain|tab_wiki",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "context": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "925d40eb-a5d6-4b96-9d00-a59e59889b4a",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCm1arsJykJLu7mjBFyk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6123870-a0f9-45ee-8cea-56c05dec5e46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01REu2HZspnBFiS8DVVQcN1d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5445,
      "cache_read_input_tokens": 68920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5445,
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

_source line 43 · 2026-05-19T23:01:17.721Z_

<details><summary>↩ Tool result · `toolu_01FMnc4ueNLXdeYRHUgs2Yew`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-228-All four configurations preserve their $\Kempirical$ under 14D, with negligible AUC change ($|\Delta| \leq 0.003$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-229-The self\_BLEU feature contributes minimally to the depth boundary; $\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-230-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-231-\subsection{Wikipedia Domain: Scorer Confound Resolution}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:232:\label{sec:wiki_domain}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-233-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:234:Under same-family scoring (Qwen-1.5B scorer), Wikipedia $\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\Kempirical{=}2$, while all four non-Qwen models yielded $\Kempirical{=}1$ (Table~\ref{tab:wiki_domain}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-235-A scorer confound ablation resolves this apparent split.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-236-Rescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\auc$ from $0.611$ to $0.587$ ($\Delta = -2.4$\,pp), dropping $\Kempirical$ from 2 to 1.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-237-With the scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-238-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-239-\begin{table}[htbp]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-240-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-241-\small
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-242-\caption{Wikipedia pairwise $\auc$ across 6 models. $^\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\Kempirical{=}1$ ($\Delta = -2.4$\,pp), resolving the apparent family split.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:243:\label{tab:wiki_domain}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-244-\resizebox{\columnwidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-245-\begin{tabular}{llccccc}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-246-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-247-\textbf{Model} & \textbf{Family} & \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & $\Kempirical$ & \textbf{Scorer} \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-609-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-610-\paragraph{Cross-scorer validation (Code domain).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-611-To rule out scorer confound for Code $\Kempirical{=}2$, we re-evaluate Qwen2.5-1.5B code generations using Pythia-1.4B as the reference scorer (Table~\ref{tab:code_crossscorer}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-612-Cross-family scoring yields $\Kempirical{=}2$ (1v2 $\auc = 0.7197$, five-fold minimum $= 0.6985$, all folds above $\theta$), a decrease of only 1.9\,pp from Qwen self-scoring ($0.7382$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:613:This contrasts with Wikipedia, where same-family scoring inflates $\Kempirical$ from 1 to 2 (Appendix~\ref{sec:wiki_domain}): Code depth signal is robust to scorer choice, while Wikipedia's marginal signal is scorer-sensitive.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-614-The scorer confound is therefore domain-specific rather than systematic.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-615-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-616-\begin{table}[htbp]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex-617-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-161-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-162-\paragraph{Wikipedia ($\Kempirical{=}1$): single-generation saturation.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-163-With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\Kempirical{=}1$ on Wikipedia: 1v2 $\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\theta$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-164-Wikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:165:Same-family scoring inflates Qwen $\Kempirical$ to 2 on Wikipedia ($\Delta = +2.4$\,pp); cross-family scoring controls this bias without affecting C4 results (Appendix~\ref{sec:wiki_domain}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-166-
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-167-\paragraph{Code ($\Kempirical{=}1$--$2$): cross-modality confirmation.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-168-Python functions from CodeSearchNet~\cite{husain2019codesearchnet} ($n{=}5{,}000$) yield $\Kempirical{=}2$ for four models (Qwen-1.5B/7B, LLaMA-8B, Mistral-7B; 1v2 $\auc$: 0.615--0.739; Table~\ref{tab:code_crossmodel_kstar}), but $\Kempirical{=}1$ for capacity-limited Pythia-1.4B ($\auc = 0.598$, CI upper $= 0.603$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex-169-Code matches C4 despite a different modality, with the same sharp 2v3 collapse (JSD ratio $11.7$--$13.5\times$).
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-418-%%% Table S12: Domain Ablation
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-419-\begin{table*}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-420-  \centering
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-421-  \small
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:422:  \caption{Pairwise $\auc$ across depth pairs for three text domains (Qwen2.5-1.5B base, continuation mode). Tests generalization of $\Kempirical{=}2$ beyond C4 web text to structured and technical domains. Same-family scoring (Qwen-1.5B); cross-family controlled values in Table~\ref{tab:wiki_domain}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-423-  \label{tab:s12_domain_ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-424-  \begin{tabular}{lccc}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-425-    \toprule
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex-426-    \textbf{Depth Pair} & \textbf{C4 (web)} & \textbf{Wikipedia} & \textbf{arXiv} \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1350-\@LN{1090}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1351-\@LN{1091}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1352-\@LN{1092}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1353-\@writefile{toc}{\contentsline {subsection}{\numberline {C.6}Wikipedia Domain: Scorer Confound Resolution}{16}{subsection.C.6}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1354:\newlabel{sec:wiki_domain}{{C.6}{16}{Wikipedia Domain: Scorer Confound Resolution}{subsection.C.6}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1355-\@LN{1093}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1356-\@LN{1094}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1357-\@LN{1095}{15}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1358-\@LN{1096}{15}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1488-\newlabel{sec:power_curve}{{C.11}{18}{Statistical Power Analysis}{subsection.C.11}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1489-\@LN{1199}{17}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1490-\@LN{1200}{17}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1491-\@LN{1201}{17}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1492:\@writefile{lot}{\contentsline {table}{\numberline {21}{\ignorespaces Pairwise $\text  {AUC}$ across depth pairs for three text domains (Qwen2.5-1.5B base, continuation mode). Tests generalization of ${K^*}{=}2$ beyond C4 web text to structured and technical domains. Same-family scoring (Qwen-1.5B); cross-family controlled values in Table~\ref {tab:wiki_domain}.}}{19}{table.caption.45}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1493:\newlabel{tab:s12_domain_ablation}{{21}{19}{Pairwise $\auc $ across depth pairs for three text domains (Qwen2.5-1.5B base, continuation mode). Tests generalization of $\Kempirical {=}2$ beyond C4 web text to structured and technical domains. Same-family scoring (Qwen-1.5B); cross-family controlled values in Table~\ref {tab:wiki_domain}}{table.caption.45}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1494-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1495-\newlabel{tab:s13_scorer_sensitivity}{{22}{19}{Scorer sensitivity: $\Kempirical $ under self-scoring vs.\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\Kempirical $ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\Kempirical $ only for the most marginal self-scorer condition (Qwen-continuation)}{table.caption.46}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1496-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1497-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1507-\newlabel{tab:feature_subset}{{29}{20}{1v2 $\auc $ by feature subset size (Pythia-1.4B). $\Kempirical {=}2$ ($\auc > \theta {=}0.60$) is robust at $\geq $8 features}{table.caption.54}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1508-\@writefile{lot}{\contentsline {table}{\numberline {30}{\ignorespaces 15D vs.\ 14D (self\_BLEU removed) 1v2 $\text  {AUC}$ with bootstrap 95\% CIs. Removing self\_BLEU does not change ${K^*}$ for any configuration. Maximum $|\Delta \text  {AUC}| = 0.0031$, within bootstrap CI width (${\sim }0.018$).}}{20}{table.caption.55}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1509-\newlabel{tab:selfbleu_ablation}{{30}{20}{15D vs.\ 14D (self\_BLEU removed) 1v2 $\auc $ with bootstrap 95\% CIs. Removing self\_BLEU does not change $\Kempirical $ for any configuration. Maximum $|\Delta \auc | = 0.0031$, within bootstrap CI width (${\sim }0.018$)}{table.caption.55}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1510-\@writefile{lot}{\contentsline {table}{\numberline {31}{\ignorespaces Wikipedia pairwise $\text  {AUC}$ across 6 models. $^\dagger $Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to ${K^*}{=}1$ ($\Delta = -2.4$\,pp), resolving the apparent family split.}}{20}{table.caption.56}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux:1511:\newlabel{tab:wiki_domain}{{31}{20}{Wikipedia pairwise $\auc $ across 6 models. $^\dagger $Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\Kempirical {=}1$ ($\Delta = -2.4$\,pp), resolving the apparent family split}{table.caption.56}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1512-\@LN@col{2}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1513-\@writefile{lot}{\contentsline {table}{\numberline {32}{\ignorespaces Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\text  {AUC}$ (10{,}000 resamples). Point estimates classify 3/4 generators as ${K^*}{=}3$; strict CI lower-bound criterion confirms 2/4.}}{20}{table.caption.58}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1514-\newlabel{tab:arxiv_crossscorer_ci}{{32}{20}{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc $ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical {=}3$; strict CI lower-bound criterion confirms 2/4}{table.caption.58}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.aux-1515-\@writefile{lot}{\contentsline {table}{\numberline {33}{\ignorespaces arXiv pairwise $\text  {AUC}$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\sim }$1.8\,pp but ${K^*}$ remains at 3 (CI lower $> \theta $). LaTeX stripping fraction increases with depth (0.6\% at depth 0, 4.6\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}}{20}{table.caption.61}\protected@file@percent }
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6123870-a0f9-45ee-8cea-56c05dec5e46",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "275f5f40-63c6-4a24-ae37-50928ca968f5",
  "sourceToolAssistantUUID": "a6123870-a0f9-45ee-8cea-56c05dec5e46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T23:01:18.084Z_

<details open><summary>🔧 Tool call — Read · `toolu_016fYUcnckbnkSSU8zWrDTkQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 230,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "275f5f40-63c6-4a24-ae37-50928ca968f5",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCm1arsJykJLu7mjBFyk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c79f77c-0901-406a-aeb2-7020f48f7fdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01REu2HZspnBFiS8DVVQcN1d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5445,
      "cache_read_input_tokens": 68920,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5445
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 271,
          "cache_read_input_tokens": 68920,
          "cache_creation_input_tokens": 5445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5445,
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

_source line 45 · 2026-05-19T23:01:18.098Z_

<details><summary>↩ Tool result · `toolu_016fYUcnckbnkSSU8zWrDTkQ`</summary>

```text
230	
231	\subsection{Wikipedia Domain: Scorer Confound Resolution}
232	\label{sec:wiki_domain}
233	
234	Under same-family scoring (Qwen-1.5B scorer), Wikipedia $\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\Kempirical{=}2$, while all four non-Qwen models yielded $\Kempirical{=}1$ (Table~\ref{tab:wiki_domain}).
235	A scorer confound ablation resolves this apparent split.
236	Rescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\auc$ from $0.611$ to $0.587$ ($\Delta = -2.4$\,pp), dropping $\Kempirical$ from 2 to 1.
237	With the scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
238	
239	\begin{table}[htbp]
240	\centering
241	\small
242	\caption{Wikipedia pairwise $\auc$ across 6 models. $^\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\Kempirical{=}1$ ($\Delta = -2.4$\,pp), resolving the apparent family split.}
243	\label{tab:wiki_domain}
244	\resizebox{\columnwidth}{!}{%
245	\begin{tabular}{llccccc}
246	\toprule
247	\textbf{Model} & \textbf{Family} & \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & $\Kempirical$ & \textbf{Scorer} \\
248	\midrule
249	Qwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\dagger$ & Qwen-1.5B \\
250	Qwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\
251	Qwen-7B          & Qwen & .967 & .611 & .556 & 2$^\dagger$ & Qwen-1.5B \\
252	Qwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\
253	\midrule
254	Pythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\
255	OLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\
256	LLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\
257	Mistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\
258	\bottomrule
259	\multicolumn{7}{l}{\footnotesize $^\dagger$Same-family scorer; cross-family scoring yields $\Kempirical{=}1$.}
260	\end{tabular}}
261	\end{table}
262	
263	\paragraph{Per-fold transparency.}
264	For Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\theta = 0.60$).
265	The aggregate mean falls below $\theta$, confirming $\Kempirical{=}1$.
266	For Qwen-7B, the corresponding $\auc$ drops further to $0.587$.
267	
268	\subsection{ArXiv Cross-Scorer Bootstrap CIs}
269	\label{sec:arxiv_crossscorer_ci}
270	
271	\begin{table}[htbp]
272	\centering
273	\small
274	\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
275	\label{tab:arxiv_crossscorer_ci}
276	\resizebox{\columnwidth}{!}{%
277	\begin{tabular}{lccc}
278	\toprule
279	\textbf{Generator} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & \textbf{CI lower $> \theta$} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c79f77c-0901-406a-aeb2-7020f48f7fdc",
  "isSidechain": true,
  "promptId": "235a7e43-1008-4163-85c5-13e8cd2f20cb",
  "agentId": "a75fb13353a31d082",
  "type": "user",
  "uuid": "e9b6d9a7-1e2e-4d94-b8eb-bed3ea273848",
  "sourceToolAssistantUUID": "7c79f77c-0901-406a-aeb2-7020f48f7fdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-19T23:01:54.164Z_

Excellent! Now let me compile my comprehensive findings with all the specific locations and content.

## Comprehensive Search Results

I've conducted a very thorough search of the paper LaTeX files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/`. Here are all the references to your requested items:

### 1. OLMo/OLMo-1B References (K* Values)

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex`**
- **Line 5:** OLMo-1B is listed as one of nine tested model configurations
- **Line 22:** Table header includes OLMo in the cross-model comparison table
- **Line 47:** "Among non-Qwen families: Pythia and OLMo yield clear K*=2..."
- **Line 82:** "Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings (ρ > 0.90; Table~ref{tab:crossscorer})."
- **Line 105:** Neural probe section: "Pythia and OLMo remain at K*_neural = 2 (AUC_2v3: 0.5963, 0.5892)"
- **Line 120:** OLMo-1B neural probe results shown in table
- **Line 159:** "OLMo-1B is a capacity failure (0v1 JSD = 0.33, near-total information loss), not a counter-example."
- **Line 189:** Table footnote notes OLMo-1B for Wikipedia

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex`**
- **Line 8:** Cross-scorer validation caption mentions "OLMo-1B preserve feature ranking (ρ > 0.90) and rewrite-mode K* = 2, but reduce continuation-mode K* from 2 to 1"
- **Lines 89, 98:** Table entries showing OLMo with K* = 2 on C4 web and cross-scorer
- **Line 115:** "OLMo <1%" EOS truncation rates mentioned
- **Line 296:** "Wikipedia λ ≈ 3.1 (excluding OLMo, whose λ = 6.3 reflects a capacity-limited collapse: 0v1 JSD = 0.169..."
- **Lines 255, 448, 453:** OLMo Wikipedia domain results (K*=1)
- **Lines 531, 543, 552:** OLMo in cross-validation tables
- **Line 613:** "Code depth signal is robust to scorer choice, while Wikipedia's marginal signal is scorer-sensitive" (contrasting with OLMo)

### 2. Wikipedia Domain with K* Values

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex`**
- **Lines 162-165:** "Wikipedia (K*=1): single-generation saturation" section. States "With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield K*=1 on Wikipedia: 1v2 AUC ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below θ."
- **Line 165:** "Same-family scoring inflates Qwen K* to 2 on Wikipedia (Δ = +2.4pp); cross-family scoring controls this bias without affecting C4 results (Appendix~ref{sec:wiki_domain})."

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex`**
- **Lines 231-262:** Entire subsection "Wikipedia Domain: Scorer Confound Resolution" (sec:wiki_domain). Key passages:
  - Line 234: "Under same-family scoring (Qwen-1.5B scorer), Wikipedia K* appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded K*=2, while all four non-Qwen models yielded K*=1"
  - Line 236: "Rescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 AUC from 0.611 to 0.587 (Δ = -2.4pp), dropping K* from 2 to 1."
  - Line 237: "With the scorer confound controlled, all six models yield K*=1 on Wikipedia, and the domain ordering simplifies to: arXiv (K*=3) > C4 (K*=2) > Wikipedia (K*=1)."
  - Lines 243-261: Table 31 (tab:wiki_domain) showing pairwise AUC across 6 models for Wikipedia

### 3. DeBERTa with K* Values

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex`**
- **Lines 125-128:** "Fine-tuned DeBERTa upper bound" section. Key text:
  - Line 126: "To test whether classifier strength or generator scale shifts the boundary, we train DeBERTa-v3-base ordinal classifiers on C4 generations at 14B and 32B scales (Table~ref{tab:deberta_comparison})."
  - Line 127: "On C4, DeBERTa raises 1v2 AUC over LightGBM at both scales (14B: 0.678 vs. 0.621; 32B: 0.694 vs. 0.618), yet K*=2 is preserved (all 2v3 CI upper < θ); LightGBM AUC shifts by < 0.5pp between 14B and 32B, confirming both scale and representation invariance on web text."
  - Line 128: "On Wikipedia, however, DeBERTa extends K* from ≤2 (OBD) to 3 (3/4 configurations), revealing a domain-dependent classifier gap: contextualized representations retain depth signal that 15D statistics lose in structurally simpler domains."
- **Lines 133-145:** Table 4 (tab:deberta_comparison) showing DeBERTa-v3-base vs. LightGBM on C4 at 14B and 32B scales
- **Line 203:** "In summary, K*=2 for web text is consistent across five architecture families (1B--32B), four decoding strategies, and two classifier representations (LightGBM, DeBERTa)..."

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex`**
- **Line 6:** "DeBERTa-v3-base confirms K*=2 on C4 at both 14B and 32B, though on Wikipedia it extends K* to 3, revealing domain-dependent classifier sensitivity..."

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex`**
- **Line 26:** "...with K* invariant to representation on C4 but DeBERTa extending K* to 3 on Wikipedia (Section~ref{sec:neural_probe})."

### 4. Domain Ordering (K* values)

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex`**
- **Line 80:** Table caption states "The **domain ordering** (arXiv > web ≥ cross-scorer) and **bounded range** (K*≤4) are preserved across θ ∈ [0.55, 0.70]"
- **Line 106:** Figure caption: "The domain ordering (Wikipedia K*≤1 < C4 K*≤2 < arXiv K*≤3) is preserved across the full θ ∈ [0.55, 0.70] range"
- **Line 237:** "...the domain ordering simplifies to: arXiv (K*=3) > C4 (K*=2) > Wikipedia (K*=1)."

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex`**
- **Line 64:** "The domain ordering (arXiv > web ≥ cross-scorer) is preserved across the full θ range (Table~ref{tab:theta_sensitivity}; Figure~ref{fig:theta_sensitivity} in Appendix); this ordering invariance provides a more robust characterization than absolute K* values..."
- **Line 173:** "With the scorer confound controlled, the domain ordering is: arXiv (K*=3) > C4 (K*=2) ≥ Code (K*=1--2) ≥ Wikipedia (K*=1)."

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex`**
- **Line 5:** "The domain ordering (arXiv > C4 ≥ Code > Wikipedia) is θ-invariant."

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex`**
- **Line 26:** "The domain ordering (arXiv > C4 ≥ Code > Wikipedia) correlates with structural complexity..."

### 5. Representation-Independent / Classifier-Dependent Content

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex`**
- **Lines 102-160:** "Neural Probe" subsection (sec:neural_probe). Key content:
  - Line 105: "Replacing the 15D features with frozen encoder hidden states (MLP probe, 5,000 texts per depth; Table~ref{tab:neural_probe_crossmodel}), Qwen achieves K*_neural = 3 (2v3 AUC = 0.6159), while Pythia and OLMo remain at K*_neural = 2..."
  - Line 106: "The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~ref{sec:transfer}); the 15D statistical features yield consistent K* = 2 across all families."
  - Lines 111-123: Table 3 (tab:neural_probe_crossmodel) showing neural probe results
- **Lines 125-128:** DeBERTa section discussing representation dependence on Wikipedia vs. invariance on C4

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex`**
- **Line 25-26:** "Domain and representation dependence" paragraph: "The classifier gap is itself domain-dependent, with K* invariant to representation on C4 but DeBERTa extending K* to 3 on Wikipedia..."

### 6. Limitations Section (Domain-related content)

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`**
- **Lines 68-81:** Entire "Limitations" section (unnumbered). Key domain-related points:
  - Line 71: Mentions "English text (C4, Wikipedia, arXiv) and Python code (CodeSearchNet)"
  - Line 72: "The 1.5B→32B trend shows stable K*=2 with declining 1v2 AUC; whether this holds at 70B+ scales remains unverified."
  - Line 75: Notes "LLaMA-3.1-8B (C4) and Mistral-7B-v0.3 (code) represent the most marginal K*=2 assignments"
  - Line 77: "Segment length: K*=2 confirmed for 128 and 256 tokens (CI lower > θ); 512 tokens yields point estimate K*=2 but CI lower marginally below θ (0.5979); the boundary weakens at longer generation lengths."
  - Line 80: Notes boundary-level transfer fragility with domains and scales

### 7. OBD Baseline Values

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex`**
- **Line 27:** "Our OBD classifier follows Frank & Hall's~cite{frank2001ordinal} binary decomposition; CORAL~cite{cao2020coral} provides a rank-consistent neural alternative."

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex`**
- Line 318: Table caption describes "LightGBM hyperparameters for the pairwise OBD (Ordinal Binary Decomposition) classifier used throughout the paper"

**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex`**
- **Line 388:** "To assess the relative contribution of each feature group to depth discrimination, we train a plain LightGBM classifier (distinct from the OBD-LightGBM used in Section~ref{sec:method})..."

All major findings are concentrated in the main experimental sections (experiments_c1.tex), the discussion section, appendices, and the limitations section, with comprehensive domain-specific K* values documented across Wikipedia, C4 (web), arXiv, and Code domains.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9b6d9a7-1e2e-4d94-b8eb-bed3ea273848",
  "isSidechain": true,
  "agentId": "a75fb13353a31d082",
  "requestId": "req_011CbCm1quExS59YEVNubDL2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "230a7317-4cc0-43ed-ab89-2c542eb2ef6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/reviewer_08f7237f",
  "sessionId": "71696373-dd9d-4216-83c1-2ffcec627cbe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-chasing-scott",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EzNkoEDNoA2kpPjaXDh1cG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7950,
      "cache_read_input_tokens": 74365,
      "output_tokens": 3517,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7950
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3517,
          "cache_read_input_tokens": 74365,
          "cache_creation_input_tokens": 7950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7950,
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
