# Research conversation: In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/, I need 

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ace52815005e1f6e0.jsonl`
- **Structured JSON:** [`33c6df8542317b6372d4.json`](../../sessions/33/33c6df8542317b6372d4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-24T18:45:13.195Z_

In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/, I need to understand:

1. What figures currently exist in the APPENDIX (not main text)? Search all appendix .tex files for \includegraphics, \begin{figure}, figure references. List each figure with: label, caption summary, file path, and what it shows.

2. What is the current Limitations section content? Read the Limitations section (likely in main.tex or a dedicated file). Show the full text.

3. How many figures are currently in the main text (experiments.tex, introduction.tex, method.tex etc.)? List them with labels and captions.

4. List all PDF/PNG files in the figures/ directory.

5. What is the current page count breakdown? Check if there are any comments about page limits.

Be thorough - read all .tex files to find every figure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "71507cbe-9c0a-4d99-960e-8e5345c771f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T18:45:14.702Z_

I'll help you analyze the paper structure. Let me start by exploring the directory structure and then systematically search for all figures and relevant content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71507cbe-9c0a-4d99-960e-8e5345c771f7",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtXnXn5ZQBFFDQZ8aJa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ddd82687-75ad-4636-9bef-b444cb4e1545",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DwU2akyLgFcPQeSaWp6MaC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37385,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37385,
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

_source line 3 · 2026-05-24T18:45:14.958Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019xAd4ENDhv26Rxda2BnDRK`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddd82687-75ad-4636-9bef-b444cb4e1545",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtXnXn5ZQBFFDQZ8aJa",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68aed377-6638-46bb-b6b9-a7304049df0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DwU2akyLgFcPQeSaWp6MaC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37385,
      "cache_read_input_tokens": 0,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37385
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 128,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 37385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37385,
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

_source line 4 · 2026-05-24T18:45:15.214Z_

<details><summary>↩ Tool result · `toolu_019xAd4ENDhv26Rxda2BnDRK`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68aed377-6638-46bb-b6b9-a7304049df0b",
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "738e0f5c-82f9-4397-a0df-74007eb7cb93",
  "sourceToolAssistantUUID": "68aed377-6638-46bb-b6b9-a7304049df0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-24T18:45:16.445Z_

Now let me search for all figures, including in appendix files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "738e0f5c-82f9-4397-a0df-74007eb7cb93",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtXw6iSJQzctJPr3iMz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cc287967-6da3-4279-8c62-1166a8ea1c69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GGfzQkgHDcr61fayeN6aHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 37385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1324,
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

_source line 6 · 2026-05-24T18:45:16.743Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BJcJ2WmPVS9US48xN1ffEs`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper -type f \\( -name \"*.tex\" -o -name \"*.pdf\" -o -name \"*.png\" -o -name \"*.jpg\" \\)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc287967-6da3-4279-8c62-1166a8ea1c69",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtXw6iSJQzctJPr3iMz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aaa9f8b9-cc14-4b8d-91db-660e205b44d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GGfzQkgHDcr61fayeN6aHL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 37385,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1324
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 136,
          "cache_read_input_tokens": 37385,
          "cache_creation_input_tokens": 1324,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1324,
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

_source line 7 · 2026-05-24T18:45:16.811Z_

<details><summary>↩ Tool result · `toolu_01BJcJ2WmPVS9US48xN1ffEs`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p17.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p25.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p15.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p16.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p18.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p24.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images/main_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/_pdf_images/signal_reversal_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/_pdf_images/fig1_daf_scatter_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/_pdf_images/pipeline_overview_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/fig1_daf_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/label_decomposition.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/death_action_comparison.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/death_action_comparison.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/pipeline_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/dose_response.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/pipeline_overview.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/death_action_timeline.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/death_action_timeline.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/pipeline_overview_old.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/death_action_distribution.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/death_action_distribution.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/label_decomposition.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/fig1_daf_scatter.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/signal_reversal.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_pdf_images_r5/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_figure_backups/20260524_085344/pipeline_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_figure_backups/20260524_092318/label_decomposition.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/_figure_backups/20260524_091724/pipeline_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaa9f8b9-cc14-4b8d-91db-660e205b44d1",
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "382cc0b1-99c4-4021-b998-3769ca263ea6",
  "sourceToolAssistantUUID": "aaa9f8b9-cc14-4b8d-91db-660e205b44d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-24T18:45:18.093Z_

Let me check the main.tex structure and then search for all figures systematically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "382cc0b1-99c4-4021-b998-3769ca263ea6",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtY3tkHWZUJtsrsENwS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "31ab573f-82e3-4b80-88ef-8c85528d7e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BJV5T5SUmsPHV59QieBJ33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2735,
      "cache_read_input_tokens": 38709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2735,
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

_source line 9 · 2026-05-24T18:45:18.324Z_

<details open><summary>🔧 Tool call — Read · `toolu_017PPjJdgJPXTJacT1fpKUPo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ab573f-82e3-4b80-88ef-8c85528d7e0e",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtY3tkHWZUJtsrsENwS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "59e8c71c-1175-4765-9256-a26cd527a4ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BJV5T5SUmsPHV59QieBJ33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2735,
      "cache_read_input_tokens": 38709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2735,
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

_source line 10 · 2026-05-24T18:45:18.595Z_

<details><summary>↩ Tool result · `toolu_017PPjJdgJPXTJacT1fpKUPo`</summary>

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
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	\usepackage{tcolorbox}
18	\tcbuselibrary{listings,breakable}
19	
20	\hypersetup{pdfauthor={},pdftitle={}}
21	
22	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\input{abstract}
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{related_work}
34	\input{discussion}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	\paragraph{Environmental scope.}
40	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct), though extended validation of representative excluded tasks confirms the pattern (Appendix~\ref{app:extended-validation}). The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Two 70B-class models (Qwen2.5-72B and Llama-3.1-70B; $10{\times}$ scale) do not eliminate death dominance (DAF $92.4$--$101.0\%$): Qwen2.5-72B reduces death rate while Llama-3.1-70B exhibits comparable or higher rates (\S\ref{sec:agent-improvement}); validation beyond 70B remains future work. Whether death avoidance remains dominant for frontier models with substantially lower failure rates is an open question. Our quantitative results (DAF $= 90.4\%$, label fractions) are specific to ScienceWorld; the framework's generality claim is methodological (the diagnostic procedure applies to any environment with asymmetric fatal outcomes), not empirical (the specific percentages may differ across environments).
41	
42	\paragraph{Methodological constraints.}
43	Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}. Reflexion~\citep{reflexion-2023} reduces death rate from 42.9\% to 31.4\% (\S\ref{sec:agent-improvement}), but more aggressive self-correction or Tree-of-Thought backtracking~\citep{tot-2023} may further reduce internal death rates. Episode-level labels assign a single routing preference to entire episodes, which may be suboptimal for individual steps (particularly those preceding death events). However, of 2{,}040 training steps only 0.3\% exhibit strict directional conflict (step-level oracle opposite to episode label); the remaining apparent mislabeling consists of episode labels applied to steps where neither strategy has a step-level advantage (60.3\% pre-event neutral). The issue is granularity mismatch (applying correct-direction labels to uninformative steps), not directional error. Training on pure-strategy trajectories also introduces distribution shift at deployment~\citep{dagger-2011}. Grounding ablation reduces but does not eliminate the death rate differential (from $+26.5$\,pp to approximately $+8$\,pp; Appendix~\ref{app:grounding-ablation}); Post-ablation counterfactual decomposition over matched episodes confirms that death remains the dominant signal source ({$\geq$}93\% of disambiguating labels arise from death asymmetry, with near-zero non-death performance gap $\Delta_\text{nd} \approx 0$; Appendix~\ref{app:grounding-ablation}). Under mixed-strategy routing with oracle death prediction, switching to deterministic at the step before death could reduce the internal death rate; even under optimistic assumptions (perfect step-level death prediction), a residual gap of ${>}10$~pp between strategies is expected, as fatal trajectories involve cumulative hallucination errors preceding the death event. More broadly, projecting episode-level labels onto 10--50 sequential steps with path-dependent state introduces compounding error: early routing decisions alter the state trajectory, potentially invalidating later labels derived from the episode outcome.
44	
45	\paragraph{Statistical limitations.}
46	Episodes within the same task type are not fully independent because they share environment dynamics, though they use different random seeds. Cluster bootstrap with $K{=}11$ task-type clusters yields wider CIs ($[73.3\%, 100.0\%]$); with $K{=}11$ falling below the $K \geq 20$--$50$ threshold recommended by \citet{cameron-2008,webb-2023}, readers should rely on the non-clustered bootstrap CI ($[81.3\%, 99.1\%]$). A wild cluster bootstrap ($K{=}11$, $p < 0.001$; Appendix~\ref{app:wild-cluster}) and 100\% directional consistency across all 28 death-prone tasks (Appendix~\ref{app:per-task-ci}) mitigate this concern.
47	
48	\paragraph{Pure-strategy upper bound.}
49	Our counterfactual analysis compares pure strategies (always-internal vs.\ always-deterministic). In mixed routing, the router can selectively invoke deterministic mode on high-risk steps, potentially reducing death asymmetry. Thus, DAF${=}90.4\%$ represents an upper bound on death avoidance's contribution to optimized routing; the actual contribution under mixed strategies may be lower.
50	
51	\paragraph{Diagnostic scope.}
52	Our framework is diagnostic rather than prescriptive: it identifies what drives routing decisions but does not optimize the routing policy itself. The framework assumes binary catastrophic failure; environments with graded penalties would require modifying Algorithm~\ref{alg:labeling}'s death-priority rule to a continuous severity weighting. Extending the counterfactual decomposition to prescribe optimal mixed-strategy routing (for example, by combining DAF analysis with online policy learning) is a natural next step.
53	
54	\section*{Ethics Statement}
55	
56	This work uses ScienceWorld \citep{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All evaluation environments (ScienceWorld, ALFWorld, MATH) are released under permissive open-source licenses (Apache 2.0 / MIT). All models used (Qwen2.5 family, Llama-3.1-8B, Gemma-2-9B-it) are publicly available for research use. All language models are accessed via standard APIs or publicly released weights. Experiments were conducted on 2$\times$ NVIDIA RTX 5090 (32GB) and 4$\times$ NVIDIA RTX 6000 PRO (96GB), totaling approximately 200 GPU-hours, comprising ${\sim}$140 hours for episode collection (counterfactual inference across three 7--9B model families plus Qwen2.5-72B backbone scaling, Reflexion and retry baselines, and cross-environment validation on ALFWorld and MATH), ${\sim}$35 hours for router training (LoRA fine-tuning of Qwen3-0.6B/1.7B/4B across 4--8 seeds per scale, including augmentation and ablation variants), and ${\sim}$25 hours for evaluation and analysis. Code and data will be released upon acceptance.
57	
58	\bibliography{references}
59	
60	\appendix
61	
62	\noindent\textbf{Appendix Overview.}
63	\hyperref[app:sci]{A.~Signal Concentration Index} $\cdot$
64	\hyperref[app:labeling]{B.~Labeling Quality Audit} $\cdot$
65	\hyperref[app:per-task]{C.~Per-Task Decomposition} $\cdot$
66	\hyperref[app:correlation]{D.~Correlation Robustness} $\cdot$
67	\hyperref[app:wild-cluster]{E.~Cluster Bootstrap Sensitivity} $\cdot$
68	\hyperref[app:per-task-ci]{F.~Per-Task CIs} $\cdot$
69	\hyperref[app:loto-daf]{G.~Leave-One-Task-Out DAF} $\cdot$
70	\hyperref[app:dose-response]{H.~Dose-Response Breakdown} $\cdot$
71	\hyperref[app:router-details]{I.~Router Training Details} $\cdot$
72	\hyperref[app:seed-robustness]{J.~Seed Robustness} $\cdot$
73	\hyperref[app:penalty]{K.~Penalty Sensitivity} $\cdot$
74	\hyperref[app:cross-env-details]{L.~Cross-Environment Details} $\cdot$
75	\hyperref[app:cross-model]{M.~Cross-Model Verification} $\cdot$
76	\hyperref[app:failure-modes]{N.~Failure Mode Analysis} $\cdot$
77	\hyperref[app:grounding-ablation]{O.~Grounding Ablation} $\cdot$
78	\hyperref[app:ablations]{P.~Ablation Studies} $\cdot$
79	\hyperref[sec:threshold-routing]{Q.~Threshold Routing} $\cdot$
80	\hyperref[app:decision-framework]{R.~Decision Framework} $\cdot$
81	\hyperref[app:extended-validation]{S.~Extended Validation} $\cdot$
82	\hyperref[app:prompt-templates]{T.~Agent Prompt Templates} $\cdot$
83	\hyperref[app:non-death-case-study]{U.~Non-Death Episode Case Study}
84	
85	\section{Signal Concentration Index}
86	\label{app:sci}
87	
88	Let $K$ denote the number of task types and $c_k$ the contribution of task type $k$ to the aggregate routing signal, defined as the fraction of total death-rate differential attributable to task $k$:
89	\begin{equation}
90	    c_k = \frac{n_k \cdot \delta_k}{\sum_{j=1}^{K} n_j \cdot \delta_j}
91	\end{equation}
92	where $n_k$ is the number of episodes and $\delta_k = d_k^{\tt int} - d_k^{\tt det}$ is the per-task death-rate differential. The SCI is the Gini coefficient over $\{c_1, \ldots, c_K\}$:
93	\begin{equation}
94	    \text{SCI} = \frac{\sum_{i=1}^K \sum_{j=1}^K |c_i - c_j|}{2K \sum_{k=1}^K c_k}
95	\end{equation}
96	
97	\section{Labeling Quality Audit}
98	\label{app:labeling}
99	
100	\begin{algorithm}[t]
101	\caption{Episode-Level Counterfactual Labeling}
102	\label{alg:labeling}
103	\begin{algorithmic}[1]
104	\REQUIRE Task instance $t$, computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$
105	\ENSURE Label $\ell \in \{{\tt det\text{-}pref}, {\tt int\text{-}pref}, {\tt no\text{-}pref}\}$
106	\FOR{each $m \in \mathcal{M}$}
107	    \STATE Run episode $\tau_m$ with pure-strategy $m$
108	    \STATE Record score $s_m$ and death indicator $d_m$
109	\ENDFOR
110	\IF{$d_{\tt int} = 1$ \AND $d_{\tt det} = 0$}
111	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{death asymmetry}
112	\ELSIF{$d_{\tt int} = 0$ \AND $d_{\tt det} = 1$}
113	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{death asymmetry}
114	\ELSIF{$d_{\tt int} = d_{\tt det} = 1$}
115	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{both dead}
116	\ELSIF{$s_{\tt det} > s_{\tt int}$}
117	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{score comparison}
118	\ELSIF{$s_{\tt int} > s_{\tt det}$}
119	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{score comparison}
120	\ELSE
121	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{tied alive}
122	\ENDIF
123	\RETURN $\ell$
124	\end{algorithmic}
125	\smallskip
126	\noindent\textit{Assumption:} The death-first priority (lines 5--10) is valid when $P$ exceeds the maximum partial score, guaranteeing that a dead episode never outscores a surviving one. ScienceWorld satisfies this ($P{=}100$, max partial score ${=}100$).\\
127	\noindent\textit{Note:} When both strategies die (line 9), we assign \texttt{no\_preference}; in ScienceWorld, death yields a fixed $-100$ regardless of timing, so both-dead episodes contribute no routing signal.
128	\end{algorithm}
129	
130	Note that episode-level labels are used to evaluate step-level predictions, introducing a granularity mismatch rather than independent validation. A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine computation mode differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead, all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields step-level balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%, step-level Trainer evaluation); score-comparison labels contribute negligible additional signal. (Step-level metrics are used here for the relative comparison; as shown in \S\ref{sec:router-diagnostic}, absolute generalization to new episodes is near chance.) The 97.4\% step-level tie rate (\S\ref{sec:collection}) further motivates episode-level over step-level labeling.
131	
132	\section{Per-Task Decomposition}
133	\label{app:per-task}
134	We use ScienceWorld v1.2.3~\citep{scienceworld-2022}.
135	We select 11 of ScienceWorld's 30 task types for analysis. Types are excluded when they were used for pipeline development (5 tasks, standard hold-out practice), are taxonomically redundant with a retained family representative (7 tasks), or exhibit near-zero task progress under both strategies (7 tasks, agent capability floor).\footnote{Excluded tasks exhibit even stronger death dominance than included tasks ($\Delta\text{DR} = +38.2$\,pp vs.\ $+28.7$\,pp; Table~\ref{tab:excluded-death}).}
136	
137	\begin{table}[h]
138	\centering
139	\scriptsize
140	\setlength{\tabcolsep}{2.5pt}
141	\begin{tabular}{@{}lrrccc@{}}
142	\toprule
143	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
144	\midrule
145	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
146	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
147	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
148	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
149	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
150	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
151	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
152	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
153	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
154	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
155	\midrule
156	find-non-living-thing$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
157	\midrule
158	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
159	\bottomrule
160	\end{tabular}
161	\caption{Per-task decomposition of the death avoidance effect. D\%: death rate for internal (int) and deterministic (det) strategies. D/I/N: episode labels (det-preferred / internal-preferred / no-preference). Sorted by $\Delta_{\text{full}}$ descending. The \textit{All} row is an episode-weighted aggregate across 245 episodes. $\dagger$\,Only task with zero deaths under both strategies; $n{=}40$ because data was collected in two batches, with the second batch adding 20 episodes to increase statistical power for this zero-death outlier.}
162	\label{tab:per-task}
163	\end{table}
164	
165	\paragraph{Task selection and anti-cherry-picking.}
166	Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\% to 60\% (mean 53.9\%), while deterministic death rates range from 0\% to 40\% (mean 15.8\%), yielding a mean death-rate differential of $+38.2$\,pp, exceeding the $+28.7$\,pp for included tasks. The included subset is thus \emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. The sole exception is \texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Exclusion is driven by absence of non-death routing signal ($\Delta_{\text{nd}} = 0$ for 53\% of excluded tasks) and standard deduplication practices. \texttt{find-non-living-thing} serves as an internal counterexample: zero deaths under both strategies yet included because it exhibits non-death routing signal ($\Delta_{\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).
167	
168	\begin{table}[t]
169	\centering
170	\scriptsize
171	\setlength{\tabcolsep}{2pt}
172	\resizebox{\columnwidth}{!}{%
173	\begin{tabular}{@{}llrcccl@{}}
174	\toprule
175	Task & Grp & $n$ & D\%\textsubscript{int} & D\%\textsubscript{det} & $\Delta$DR & Excl.\ reason \\
176	\midrule
177	boil                          & A & 20 & 50 & 20 & $+30$ & dev set \\
178	change-state-of-matter        & A & 20 & 55 & 15 & $+40$ & dev set \\
179	chem-mix-paint-secondary      & A & 20 & 45 & 10 & $+35$ & dev set \\
180	grow-plant                    & A & 20 &  0 &  0 & $\phantom{+}0$  & dev set \\
181	melt                          & A & 20 & 55 & 15 & $+40$ & dev set \\
182	\midrule
183	chem-mix-paint-tertiary       & B &  5 & 40 & 20 & $+20$ & family redundancy \\
184	find-living-thing             & B &  5 & 60 & 20 & $+40$ & family redundancy \\
185	find-plant                    & B &  5 & 60 &  0 & $+60$ & family redundancy \\
186	inclined-friction-named       & B &  5 & 60 & 20 & $+40$ & family redundancy \\
187	inclined-friction-unnamed     & B &  5 & 60 &  0 & $+60$ & family redundancy \\
188	lifespan-shortest             & B &  5 & 60 & 40 & $+20$ & family redundancy \\
189	measure-melt-known            & B &  5 & 60 &  0 & $+60$ & family redundancy \\
190	\midrule
191	mendelian-known               & C &  5 & 60 & 20 & $+40$ & agent floor \\
192	mendelian-unknown             & C &  5 & 60 & 40 & $+20$ & agent floor \\
193	power-component               & C &  5 & 60 & 20 & $+40$ & agent floor \\
194	power-renewable               & C &  5 & 60 &  0 & $+60$ & agent floor \\
195	test-conductivity             & C &  5 & 60 & 20 & $+40$ & agent floor \\
196	test-conductivity-unknown     & C &  5 & 60 & 20 & $+40$ & agent floor \\
197	use-thermometer               & C &  5 & 60 & 20 & $+40$ & agent floor \\
198	\midrule
199	\textbf{Mean (19 excluded)}   &   &    & \textbf{53.9} & \textbf{15.8} & $\mathbf{+38.2}$ & \\
200	\textit{cf.\ included (11)}   &   &    & \textit{46.5} & \textit{17.8} & $\textit{+28.7}$ & \\
201	\bottomrule
202	\end{tabular}}%
203	\caption{Death-rate analysis of all 19 excluded task types. D\%: death rate (score $\leq -100$). $\Delta$DR = D\%\textsubscript{int} $-$ D\%\textsubscript{det}. 18 of 19 excluded tasks (95\%) exhibit positive death asymmetry ($\Delta$DR $\geq +20$\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\Delta$DR among excluded tasks ($+38.2$\,pp) exceeds that of included tasks ($+28.7$\,pp), confirming that task selection does not bias toward death-prone tasks. Group B--C estimates are based on $n{=}5$ prescreening episodes per task and should be interpreted as directional evidence rather than precise rate estimates.}
204	\label{tab:excluded-death}
205	\end{table}
206	
207	\section{Correlation Robustness}
208	\label{app:correlation}
209	
210	The Pearson $r = 0.9698$ reported in \S\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$); the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\% CI $[0.952, 0.995]$.
211	
212	\begin{table}[h]
213	\centering
214	\small
215	\begin{tabular}{@{}lr@{}}
216	\toprule
217	Task removed & $r_{\text{LOO}}$ \\
218	\midrule
219	id-life-stages-1       & 0.963 \\
220	lifespan-long          & 0.969 \\
221	lifespan-l-then-s      & 0.976 \\
222	inclined-plane         & 0.969 \\
223	freeze                 & 0.971 \\
224	meas-melt-point        & 0.972 \\
225	id-life-stages-2       & 0.972 \\
226	find-animal            & 0.970 \\
227	grow-fruit             & 0.973 \\
228	chem-mix               & 0.969 \\
229	find-non-living-thing  & 0.980 \\
230	\bottomrule
231	\end{tabular}
232	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
233	\label{tab:loo}
234	\end{table}
235	
236	\section{Cluster Bootstrap Sensitivity Analysis}
237	\label{app:wild-cluster}
238	
239	With $K{=}11$ task-type clusters, cluster bootstrap falls well below the $K{\geq}20$--50 recommended for reliable inference \citep{cameron-2008,webb-2023}. The narrower CIs obtained reflect known small-sample bias toward underestimation of variance, not tighter inference.
240	
241	Episodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to $K$ (task types) than $N$ (episodes). We address this with cluster-robust inference treating each task type as a cluster ($K{=}11$, all 11 included task types, 245 episodes).
242	
243	\begin{table}[h]
244	\centering
245	\small
246	\resizebox{\columnwidth}{!}{%
247	\begin{tabular}{@{}lcc@{}}
248	\toprule
249	Method & $p$-value & 95\% CI \\
250	\midrule
251	Cluster-robust $t$-test ($t{=}10.0$, df$=$10) & $< 0.001$ & $[0.73, 1.00]$ \\
252	Wild cluster bootstrap ($B{=}9{,}999$) & $< 0.001$ & $[0.73, 1.00]$ \\
253	Exact permutation ($2{,}048$ perms) & $0.002$ & --- \\
254	Sign test & $< 0.001$ & --- \\
255	\bottomrule
256	\end{tabular}}%
257	\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
258	\label{tab:wild-cluster}
259	\end{table}
260	
261	\noindent All methods confirm significance with $p < 0.01$, and the 95\% CI $[0.73, 1.00]$ excludes zero by a wide margin. With $K{=}11$ task types, ICC estimation itself carries substantial uncertainty; the high within-task consistency of death patterns (all-or-nothing per task type) suggests high ICC, which explains the CI narrowing under cluster resampling.
262	
263	We retain this analysis for transparency; readers should rely on the non-clustered episode-level bootstrap (\S\ref{sec:death-decomp}) as the primary inference.
264	
265	\section{Per-Task Death Rate Confidence Intervals}
266	\label{app:per-task-ci}
267	
268	We compute bootstrap 95\% CIs for the death-rate differential ($\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$) for all 30 ScienceWorld task types. Of 30 tasks, 28 are death-prone (at least one death under either strategy); the remaining 2 (\texttt{grow-plant}, \texttt{find-non-living-thing}) have zero deaths under both strategies.
269	
270	Across all 28 death-prone tasks, internal DR exceeds deterministic DR without exception (100\% directional consistency). The pooled death-rate differential is $+37.3\%$ (95\% CI: $[29.7\%, 44.4\%]$). Fifteen of 28 tasks are individually significant (CI excludes zero); the 13 non-significant tasks all have $n{=}5$ prescreening episodes, where statistical power is insufficient to detect even large effects (e.g., a task with $\Delta\text{DR} = +40$\,pp at $n{=}5$ has a CI of $\pm 43$\,pp). The universal directional consistency, combined with the pooled significance, confirms that death asymmetry is not driven by a subset of outlier tasks.
271	
272	\section{Leave-One-Task-Out DAF Sensitivity}
273	\label{app:loto-daf}
274	
275	\begin{table}[h]
276	\centering
277	\small
278	\caption{Leave-one-task-out DAF sensitivity (penalty-independent label fraction). Among the 10 death-prone tasks, removing any single task changes DAF by at most 3.0\,pp (range: 75.9\%--78.9\%). Removing \emph{Find Non-Living Thing}, the sole death-free task that contributes all 20 score-comparison episodes, raises DAF to 100\% by construction.}
279	\label{tab:loto-daf}
280	\begin{tabular}{lrrr}
281	\toprule
282	Removed Task & $N_\text{rem}$ & DAF (\%) & $\Delta$ (pp) \\
283	\midrule
284	(none, full) & 245 & 78.9 & --- \\
285	\midrule
286	Find Non-Living$^\dagger$ & 205 & 100.0 & +21.1 \\
287	Lifespan Longest & 220 & 75.9 & $-$3.0 \\
288	Life Stages 1 & 225 & 76.7 & $-$2.2 \\
289	Lifespan Long+Short & 225 & 76.7 & $-$2.2 \\
290	Chemistry Mix & 225 & 77.0 & $-$1.9 \\
291	Grow Fruit & 225 & 77.3 & $-$1.7 \\
292	Inclined Plane Angle & 225 & 77.3 & $-$1.7 \\
293	Freeze & 225 & 77.5 & $-$1.4 \\
294	Life Stages 2 & 225 & 77.5 & $-$1.4 \\
295	Melt Pt Unknown & 225 & 77.5 & $-$1.4 \\
296	Find Animal & 225 & 77.8 & $-$1.2 \\
297	\bottomrule
298	\end{tabular}
299	
300	\vspace{2pt}
301	{\footnotesize $^\dagger$Only death-free task; contributes all score-comparison labels. Sorted by $|\Delta|$ descending.}
302	\end{table}
303	
304	\section{Per-Task Dose-Response Breakdown}
305	\label{app:dose-response}
306	
307	Table~\ref{tab:dose-response-detail} reports per-task death rates for Reflexion at $N{=}3$, 4, and 5 on the 10 death-prone tasks ($n{=}20$ episodes per task). Per-task variance is high (up to 25\,pp range for \texttt{measure-melting-point}), but the aggregate smooths to a 2.5\,pp band, confirming that the stabilization conclusion is robust at the aggregate level despite task-level noise. \texttt{freeze} is consistently the hardest task (50--60\% DR across all $N$).
308	
309	\paragraph{Statistical power.} With $n{=}200$ paired episodes, the minimum detectable effect (MDE) is ${\sim}8$~pp ($\alpha = 0.05$, 80\% power). The key $N{=}1{\to}3$ decline ($-13.5$~pp) exceeds this threshold and is well-powered; the stabilization claim ($N{=}3{\to}5$, $+1.0$~pp) is also supported, since a ${\geq}8$~pp improvement would be detected if present.
310	
311	\begin{table}[h]
312	\centering
313	\small
314	\caption{Per-task death rates (\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm stabilization at $N \geq 3$ (range: $34.0$--$36.5\%$).}
315	\label{tab:dose-response-detail}
316	\begin{tabular}{@{}lrrr@{}}
317	\toprule
318	Task & $N{=}3$ & $N{=}4$ & $N{=}5$ \\
319	\midrule
320	chemistry-mix & 25.0 & 35.0 & 20.0 \\
321	find-animal & 45.0 & 30.0 & 45.0 \\
322	freeze & 50.0 & 50.0 & 60.0 \\
323	grow-fruit & 30.0 & 25.0 & 25.0 \\
324	identify-life-stages-1 & 35.0 & 35.0 & 35.0 \\
325	identify-life-stages-2 & 25.0 & 25.0 & 30.0 \\
326	inclined-plane-angle & 20.0 & 30.0 & 35.0 \\
327	lifespan-longest & 45.0 & 40.0 & 40.0 \\
328	lifespan-long+short & 30.0 & 45.0 & 35.0 \\
329	measure-melting-pt & 35.0 & 50.0 & 25.0 \\
330	\midrule
331	\textbf{Aggregate} & \textbf{34.0} & \textbf{36.5} & \textbf{35.0} \\
332	\bottomrule
333	\end{tabular}
334	\end{table}
335	
336	\section{Router Training Details}
337	\label{app:router-details}
338	
339	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
340	
341	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split; this suggests overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
342	
343	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, which reflects threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
344	
345	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (\texttt{enable\_thinking=False}), parsed for classification. We evaluate at two granularities: \emph{step-level} (steps from the same episode may appear in both train and validation sets) and \emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \pm 5.4\%$) exceeds chance (the router captures some signal), but episode-level accuracy ($47.1 \pm 2.2\%$, below chance) shows this does not generalize to unseen episodes. Paraphrase-based text augmentation (Appendix~\ref{app:seed-robustness}) provides no improvement; real-data scaling remains open. Always-deterministic is trivially near-optimal given DAF $= 90.4\%$. The main text (\S\ref{sec:router-diagnostic}) reports controlled 4-seed results at three scales; the model-size ablation (Appendix~\ref{app:ablations}) provides further detail.
346	
347	\begin{table}[h]
348	\centering
349	\small
350	\resizebox{\columnwidth}{!}{%
351	\begin{tabular}{@{}lcc@{}}
352	\toprule
353	Hyperparameter & Classification Head & Implicit Router \\
354	\midrule
355	Base model & Qwen3-1.7B & Qwen3-1.7B \\
356	Architecture & Linear + LoRA & SFT + LoRA \\
357	LoRA $r$ / $\alpha$ & 16 / 32 & 16 / 32 \\
358	Learning rate & 2e-5 & 2e-4 \\
359	Optimizer & AdamW & AdamW \\
360	Epochs & 3 & 3 \\
361	Batch size (per device) & 4 & 4 \\
362	Gradient accumulation & 8 & 8 \\
363	Warmup ratio & 0.1 & 0.1 \\
364	Weight decay & 0.01 & 0.01 \\
365	Max sequence length & 512 & 512 \\
366	Seeds & \{42\} & \{42, 123, 456, 789\} \\
367	\bottomrule
368	\end{tabular}}
369	\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
370	\label{tab:hyperparams}
371	\end{table}
372	
373	\paragraph{Agent inference parameters.}
374	For ScienceWorld, each agent step uses temperature $T{=}0.3$ and maximum generation length of 256 tokens, served via vLLM v0.21.0. Top-$p$ is left at the vLLM default of $1.0$ (no nucleus sampling). For MATH, the agent uses greedy decoding ($T{=}0.0$) with a maximum of 2{,}048 tokens per generation. For ALFWorld, we use $T{=}0.3$ with 256 maximum tokens. All three environments use Qwen2.5-7B-Instruct~\citep{qwen25-2024} as the backbone.
375	
376	\section{Seed Robustness}
377	\label{app:seed-robustness}
378	
379	\paragraph{Counterfactual collection seed.}
380	We re-collect all episodes with a different ScienceWorld environment seed (seed=123, $N{=}220$, 20 episodes per task type).
381	The replication yields DAF $= 89.7\%$ ($\Delta_\text{nd} = 2.83$, $\Delta_\text{full} = 27.47$),
382	within 0.73~pp of the primary estimate (seed=42, DAF $= 90.4\%$).
383	Label distributions are consistent: 67 deterministic-preferred / 7 internal-preferred / 146 no-preference
384	(primary: 86 / 9 / 150).
385	Death rates by strategy remain directionally aligned ($\text{DR}_\text{int} = 45.5\%$ vs.\ $42.9\%$; $\text{DR}_\text{det} = 20.9\%$ vs.\ $16.3\%$).
386	The seed=123 replication uses $N{=}220$ ($20$ episodes per task type);
387	the primary dataset's larger $N{=}245$ reflects 25 additional episodes across two task types (\texttt{find-non-living-thing}: $n{=}40$; \texttt{lifespan-longest-lived}: $n{=}25$; all others: $n{=}20$).
388	
389	\paragraph{Router training seed.}
390	We assess router generalization at two evaluation granularities: \emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\{42, \ldots, 49\}$, 8 seeds total), where the data partition and training seed both vary. Table~\ref{tab:seed-robustness} reports per-seed results.
391	
392	\begin{table}[h]
393	\centering
394	\small
395	\begin{tabular}{@{}llcc@{}}
396	\toprule
397	Eval.\ Granularity & Seed & Bal.\ Acc.\ (\%) \\
398	\midrule
399	Step-level & 42 & 57.06 \\
400	(same-episode & 43 & 63.99 \\
401	leakage) & 44 & 55.43 \\
402	 & 45 & 56.14 \\
403	 & 46 & 55.45 \\
404	 & 47 & 50.08 \\
405	 & 48 & 48.03 \\
406	 & 49 & 59.30 \\
407	\cmidrule{2-3}
408	 & Mean$\pm$std & $54.1 \pm 5.4$ \\
409	\midrule
410	Episode-level & 42 & 48.1 \\
411	(held-out & 43 & 47.9 \\
412	episodes) & 44 & 49.6 \\
413	 & 45 & 49.4 \\
414	 & 46 & 48.5 \\
415	 & 47 & 43.1 \\
416	 & 48 & 45.4 \\
417	 & 49 & 44.8 \\
418	\cmidrule{2-3}
419	 & Mean$\pm$std & $47.1 \pm 2.2$ \\
420	\midrule
421	\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\
422	\bottomrule
423	\end{tabular}
424	\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A text augmentation ablation (Table~\ref{tab:text-augmentation}) confirms this failure persists under the current data distribution and augmentation regime.}
425	\label{tab:seed-robustness}
426	\end{table}
427	
428	The contrast between step-level ($54.1 \pm 5.4\%$) and episode-level ($47.1 \pm 2.2\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\%--49.6\%). Paraphrase-based text augmentation (Table~\ref{tab:text-augmentation}) from 25\% to 800\% ($32{\times}$ range) provides no improvement, converging to the always-deterministic baseline ($50\%$). Paraphrase augmentation inflates the majority class without generating novel routing patterns; genuine episode-level scaling (collecting more counterfactual pairs) remains an open question. With DAF $= 90.4\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving the step-level router with no exploitable signal under current architectures.
429	
430	\paragraph{Text augmentation ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\% to 800\% of the original via paraphrase-based text augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. This tests augmentation-based scaling, not genuine episode-level scaling (which would require new counterfactual collections). Table~\ref{tab:text-augmentation} reports the results.
431	
432	\begin{table}[h]
433	\centering
434	\small
435	\begin{tabular}{@{}rccc@{}}
436	\toprule
437	Scale & Samples & Det\% & Ep.\ Bal.\ Acc.\ (\%) \\
438	\midrule
439	25\% & 433 & ${\sim}90$ & $49.5 \pm 0.3$ \\
440	50\% & 867 & ${\sim}90$ & $51.5$ \\
441	100\% & 1{,}735 & 89.6 & $49.9 \pm 0.1$ \\
442	200\% & 3{,}470 & 94.2 & $50.0 \pm 0.0$ \\
443	800\% & 13{,}880 & ${\sim}97.7$ & $51.0 \pm 1.1$ \\
444	\midrule
445	Always-det & --- & --- & 50.0 \\
446	\bottomrule
447	\end{tabular}
448	\caption{Text augmentation ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original via paraphrase, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
449	\label{tab:text-augmentation}
450	\end{table}
451	
452	All scales hover at ${\sim}50\%$ episode-level balanced accuracy (equivalent to the always-deterministic baseline), with no monotonic improvement as data increases. Augmentation-based scaling provides no improvement at any scale; however, episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes. The ground-truth internal-preferred rate (9/245 $= 3.7\%$) means collecting 50 internal-preferred episodes would require approximately 1{,}350 paired episodes at current environment dynamics, a $5.5{\times}$ expansion with diminishing return on a $9.6\%$ signal. The failure points to a limitation of the current data distribution: when DAF $= 90.4\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, and the step-level router finds no exploitable signal under the current architecture and data regime.
453	
454	Augmentation disproportionately increases the majority (deterministic) class: Det\% rises from 89.6\% at 100\% to 94.2\% at 200\% and ${\sim}97.7\%$ at 800\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\%, ${\sim}90\%$ det); this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.
455	
456	Decomposition metrics are stable under bootstrap resampling ($B{=}10{,}000$ resamples of the 245-episode dataset): DAF $= 90.4\% \pm 4.2\%$ (95\% CI $[81.3\%, 99.1\%]$); Pearson $r = 0.975 \pm 0.011$ (95\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.
457	
458	\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined; the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\% to 73.0\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the text augmentation ablation: routing signal does not transfer across task types because the signal \emph{is} the task type, i.e., whether a given task carries death risk. The 4B capacity scaling result (Appendix~\ref{app:ablations}) suggests capacity is one factor, but even 4B's $59.0\%$ episode-level accuracy does not demonstrate cross-task-type transfer.
459	
460	\section{Penalty Sensitivity Analysis}
461	\label{app:penalty}
462	
463	\begin{table}[h]
464	\centering
465	\small
466	\begin{tabular}{@{}rrr@{}}
467	\toprule
468	$P$ & DAF($P$) & 95\% CI \\
469	\midrule
470	0 & 7.4\% & [$-39.4$, $82.5$] \\
471	1 & 14.8\% & [$-28.6$, $89.6$] \\
472	5 & 35.4\% & [$-1.8$, $92.7$] \\
473	10 & 50.4\% & [$18.5$, $93.3$] \\
474	25 & 70.7\% & [$48.0$, $96.3$] \\
475	50 & 82.6\% & [$67.2$, $98.2$] \\
476	100\textsuperscript{*} & 90.4\% & [$81.3$, $99.1$] \\
477	200 & 94.9\% & [$89.9$, $99.5$] \\
478	500 & 97.9\% & [$95.7$, $99.8$] \\
479	\bottomrule
480	\end{tabular}
481	\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \Delta_{\text{nd}} / \Delta_{\text{full}}(P)$, where $\Delta_{\text{full}}(P) \approx \delta \cdot P + \Delta_{\text{nd}}$, $\delta = 0.2653$ is the death-rate differential, and $\Delta_{\text{nd}} = 2.84$ (strict neither-died filtering). Recomputed from 245 episode-level data; bootstrap 95\% CIs ($B{=}10{,}000$). \textsuperscript{*}Default setting.}
482	\label{tab:penalty-sensitivity}
483	\end{table}
484	
485	The non-death score gap $\Delta_{\text{nd}} = 2.84$ is invariant across penalty levels; it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\Delta_{\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\Delta_{\text{nd}}$ remains fixed, mechanically increasing DAF.
486	
487	\paragraph{Mechanism boundary: death specificity.}
488	The $r = 0.97$ correlation between per-task death-rate differential and $\Delta_{\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\Delta_{\text{nd}} = 2.84$). Table~\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.
489	
490	\begin{table}[h]
491	\centering
492	\small
493	\begin{tabular}{@{}rccl@{}}
494	\toprule
495	$P$ & $r$ & $p$ & Sig.\ ($\alpha{=}0.05$) \\
496	\midrule
497	1 & $-0.44$ & $0.178$ & No \\
498	5 & $-0.29$ & $0.382$ & No \\
499	10 & $-0.08$ & $0.813$ & No \\
500	25 & $0.51$ & $0.108$ & No \\
501	50 & $0.86$ & $0.0006$ & Yes \\
502	100\textsuperscript{*} & $0.97$ & $8 \times 10^{-7}$ & Yes \\
503	200 & $0.99$ & $1 \times 10^{-9}$ & Yes \\
504	\bottomrule
505	\end{tabular}
506	\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
507	\label{tab:penalty-correlation}
508	\end{table}
509	
510	This sharpens our central finding: death is not merely the dominant component of routing signal; it is effectively the \emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\Delta_{\text{full}}$ reduces to $\Delta_{\text{nd}} \approx 2.84$, which is near-uniform across task types ($\text{mean non-death gap} = -1.19$ excluding the \texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\Delta_{\text{full}}$, and the correlation sharpens because death rates \emph{are} the performance gap. The DAF values in Table~\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\text{DAF} = \delta P / (\delta P + \Delta_{\text{nd}})$), not evidence of mechanism robustness.
511	
512	\section{Cross-Environment Details}
513	\label{app:cross-env-details}
514	
515	Figure~\ref{fig:signal-reversal} and Table~\ref{tab:cross-env} summarize the label distributions across all three environments.
516	
517	\begin{figure}[h]
518	\centering
519	\includegraphics[width=\columnwidth]{figures/signal_reversal.pdf}
520	\caption{Cross-environment label distributions. ScienceWorld and ALFWorld both show deterministic preference, but through different mechanisms: death avoidance (ScienceWorld) vs.\ information asymmetry from admissible-action access (ALFWorld). MATH shows balanced labels, confirming no routing signal without catastrophic failure.}
521	\label{fig:signal-reversal}
522	\end{figure}
523	
524	\begin{table}[h]
525	\centering
526	\small
527	\resizebox{\columnwidth}{!}{%
528	\begin{tabular}{@{}lccccc@{}}
529	\toprule
530	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
531	\midrule
532	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
533	MATH & 795 & 7.3 & 8.3 & 84.4 & No \\
534	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
535	\bottomrule
536	\end{tabular}}
537	\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\dagger$\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}
538	\label{tab:cross-env}
539	\end{table}
540	
541	Table~\ref{tab:alfworld-pertask} provides the per-task-type breakdown for ALFWorld. Unlike ScienceWorld, ALFWorld has no death mechanism ($\delta = 0$, DAF $= 0\%$); the entire performance gap $\Delta_{\text{full}}$ reflects information asymmetry from admissible-action access. \texttt{pick\_and\_place} shows the strongest effect ($\Delta = 0.563$, 18 of 32 episodes det-preferred), while \texttt{pick\_two\_obj\_and\_place} shows the weakest ($\Delta = 0.087$), consistent with multi-object tasks requiring more sequential reasoning that admissible actions alone cannot resolve. Only \texttt{pick\_heat\_then\_place} has a 95\% CI crossing zero ($n{=}16$).
542	
543	\begin{table}[h]
544	\centering
545	\scriptsize
546	\setlength{\tabcolsep}{2.5pt}
547	\begin{tabular}{@{}lrcccc@{}}
548	\toprule
549	Task Type & $n$ & Succ\%\textsubscript{int} & Succ\%\textsubscript{det} & D / I / N & $\Delta_{\text{full}}$ \\
550	\midrule
551	pick\_and\_place       & 32 & 0.0  & 56.3 & 18 / 0 / 14 & $+0.563$ \\
552	look\_at\_obj\_in\_light & 13 & 15.4 & 38.5 & 3 / 0 / 10  & $+0.231$ \\
553	pick\_cool\_then\_place & 24 & 0.0  & 16.7 & 4 / 0 / 20  & $+0.167$ \\
554	pick\_clean\_then\_place & 27 & 3.7  & 18.5 & 5 / 1 / 21  & $+0.148$ \\
555	pick\_heat\_then\_place & 16 & 6.3  & 18.8 & 3 / 1 / 12  & $+0.125$ \\
556	pick\_two\_obj\_and\_place & 23 & 0.0 & 8.7  & 2 / 0 / 21  & $+0.087$ \\
557	\midrule
558	\textbf{All (6 types)} & \textbf{135} & \textbf{3.0} & \textbf{27.4} & \textbf{35 / 2 / 98} & $\mathbf{+0.244}$ \\
559	\bottomrule
560	\end{tabular}
561	\caption{Per-task-type decomposition for ALFWorld (135 games, Qwen2.5-7B-Instruct). D/I/N: deterministic-preferred / internal-preferred / no-preference. No death mechanism exists; $\Delta_{\text{full}}$ is driven entirely by information asymmetry from admissible-action access. Sorted by $\Delta_{\text{full}}$ descending.}
562	\label{tab:alfworld-pertask}
563	\end{table}
564	
565	\paragraph{MATH subset composition.}
566	The $N{=}795$ MATH problems span two categories from the MATH test set~\citep{math-2021} (Levels 4--5): Algebra (585, 73.6\%) and Counting \& Probability (210, 26.4\%). The category imbalance reflects the relative sizes in the original test set.
567	
568	\section{Cross-Model Verification}
569	\label{app:cross-model}
570	
571	We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
572	The internal strategy dies in $41.4\%$ of episodes versus $11.4\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
573	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is empirically dominated by the task environment rather than model-specific factors. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$), but directional consistency is 100\% (10/10 death-prone tasks in both models).
574	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
575	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.
576	
577	\begin{table}[h]
578	\centering
579	\small
580	\resizebox{\columnwidth}{!}{%
581	\begin{tabular}{@{}lrrrl@{}}
582	\toprule
583	Task & Int\% & Det\% & $\Delta$\,pp & D / I / N \\
584	\midrule
585	identify-life-stages-1 & 55 & 10 & +45 & 9 / 0 / 11 \\
586	freeze & 45 & 0 & +45 & 9 / 0 / 11 \\
587	grow-fruit & 45 & 5 & +40 & 8 / 0 / 12 \\
588	identify-life-stages-2 & 45 & 5 & +40 & 8 / 0 / 12 \\
589	measure-melting-point & 50 & 15 & +35 & 9 / 0 / 11 \\
590	lifespan-longest & 35 & 5 & +30 & 7 / 1 / 12 \\
591	lifespan-l-then-s & 50 & 20 & +30 & 6 / 0 / 14 \\
592	chemistry-mix & 45 & 20 & +25 & 5 / 0 / 15 \\
593	inclined-plane & 45 & 20 & +25 & 6 / 0 / 14 \\
594	find-animal & 40 & 25 & +15 & 6 / 2 / 12 \\
595	find-non-living-thing & 0 & 0 & 0 & 10 / 0 / 10 \\
596	\midrule
597	\textbf{Aggregate} & \textbf{41.4} & \textbf{11.4} & \textbf{+30.0} & \textbf{83 / 3 / 134} \\
598	\bottomrule
599	\end{tabular}}%
600	\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
601	\label{tab:cross-model-detail}
602	\end{table}
603	
604	\paragraph{Cross-model and cross-environment summary.}
605	Table~\ref{tab:cross-model-env} consolidates replication results across model families and environments.
606	
607	\begin{table}[h]
608	\centering
609	\small
610	\resizebox{\columnwidth}{!}{%
611	\begin{tabular}{llcrrrccc}
612	\toprule
613	Model & Environment & $n$ & Int DR & Det DR & $\Delta$DR & DAF & DAF 95\% CI & Signal \\
614	\midrule
615	Qwen2.5-7B & ScienceWorld & 245 & 42.9\% & 16.3\% & +26.5 & 90.4\% & [81.3, 99.1] & death \\
616	Llama-3.1-8B & ScienceWorld & 220 & 41.4\% & 11.4\% & +30.0 & 88.2\% & [80.2, 95.1] & death \\
617	Gemma-2-9B-it & ScienceWorld & 220 & 36.4\% & 14.1\% & +22.3 & 89.7\% & [79.5, 98.4] & death \\
618	Qwen2.5-72B & ScienceWorld & 255 & 30.6\% & 2.75\% & +27.8 & 92.4\% & [86.1, 97.9] & death \\
619	Llama-3.1-70B & ScienceWorld & 220 & 48.6\% & 20.0\% & +28.6 & 101.0\% & [95.3, 107.5] & death \\
620	\midrule
621	Qwen2.5-7B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% & --- & info-asym \\
622	Llama-3.1-8B & ALFWorld & 135 & 0\% & 0\% & 0 & 0\% & --- & info-asym \\
623	\midrule
624	Qwen2.5-7B & MATH & 795 & N/A & N/A & N/A & N/A & N/A & none \\
625	\bottomrule
626	\end{tabular}}
627	\caption{Cross-model and cross-environment replication summary. \textbf{ScienceWorld}: death dominance replicates across three model families in the 7--9B range and intensifies under $10{\times}$ scaling (two 70B-class models, DAF $92.4$--$101.0\%$); DAF 95\% CIs from non-clustered episode-level bootstrap ($B{=}10{,}000$). \textbf{ALFWorld}: DAF $= 0\%$ (no death mechanism); routing signal arises from information asymmetry. \textbf{MATH}: no routing signal without catastrophic failure. Signal column: diagnosed routing mechanism. DR = death rate. Gemma-2's wider CI reflects one zero-death task type (\texttt{find-non-living-thing}); excluding it yields DAF $= 99.9\%$ $[99.7, 100.0]$.}
628	\label{tab:cross-model-env}
629	\end{table}
630	
631	\section{Failure Mode Analysis}
632	\label{app:failure-modes}
633	
634	All 105 internal-strategy deaths (100\%) are triggered by the same action pattern: \texttt{focus on [object]}. In ScienceWorld, \texttt{focus on} is the answer-submission action (equivalent to ``this is my final answer''); the LLM agent systematically misuses it as a general interaction or exploration command, and applies it to irrelevant targets (rooms, doors, inventory items). Each such execution submits an incorrect answer and triggers the $-100$ death penalty. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40 for deterministic) reflects how often each strategy enters catastrophic states, not different action selection within those states.
635	
636	Manual inspection identifies four failure categories: (A) no task awareness, where the agent executes \texttt{focus on} without reading the task; (B) task-aware but lacking action grounding, where the agent correctly identifies the objective but cannot map it to valid action primitives; (D) genuine attempts with execution failure; and (E) initial progress wasted by early errors. Category B dominates: agents demonstrate task comprehension but systematically fail to translate it into correct ScienceWorld actions. This taxonomy was produced by a single annotator; no inter-annotator agreement was computed. The categories are intended as qualitative illustrations, not as formal labels with reliability guarantees.
637	\label{tab:death-taxonomy}
638	
639	\paragraph{Representative examples.}
640	\emph{Category A} (no task awareness): In a \texttt{chemistry-mix} episode, the agent immediately executes \texttt{focus on kitchen}, \texttt{focus on door}, \texttt{focus on inventory} without reading the task, dying on the first \texttt{focus on} call. \emph{Category B} (comprehension without grounding): In a \texttt{lifespan-longest-lived} episode, the agent correctly identifies that it must compare animal lifespans and reasons about which animal lives longest, but then executes \texttt{focus on oak tree} (a non-animal object in the room) instead of navigating to find the target animal, triggering death.
641	
642	\paragraph{Action distribution analysis.}
643	Figure~\ref{fig:death-action-dist} shows the action distribution in death versus non-death episodes for the internal strategy; both are dominated by \texttt{connect} actions, with \texttt{focus on} moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$). Crucially, Figure~\ref{fig:death-comparison} reveals that within death episodes, internal and deterministic strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$). The survival gap (105 vs.\ 40 deaths) therefore reflects how often each strategy enters catastrophic states, not how it behaves within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} remains the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Figure~\ref{fig:death-timeline} visualizes the temporal pattern: agents execute long sequences of \texttt{connect} actions before a terminal \texttt{focus on} triggers death, typically in the final 1--3 steps.
644	
645	\begin{figure}[h]
646	\centering
647	\includegraphics[width=\columnwidth]{figures/death_action_distribution.pdf}
648	\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \texttt{connect}). Right: non-\texttt{connect} actions zoomed. \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while non-death episodes show higher rates of observation and object interaction.}
649	\label{fig:death-action-dist}
650	\end{figure}
651	
652	\begin{figure}[h]
653	\centering
654	\includegraphics[width=\columnwidth]{figures/death_action_timeline.pdf}
655	\caption{Step-by-step action sequences for 6 representative death episodes. The fatal \texttt{focus on} action (marked with arrow) consistently appears in the final steps after long \texttt{connect} sequences, and illustrates the ``connect loop $\to$ fatal focus'' pattern. Examples are drawn from the full 30-task dataset for task-type diversity; the pattern is identical in the 11-task analysis subset.}
656	\label{fig:death-timeline}
657	\end{figure}
658	
659	\begin{figure}[h]
660	\centering
661	\includegraphics[width=\columnwidth]{figures/death_action_comparison.pdf}
662	\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
663	\label{fig:death-comparison}
664	\end{figure}
665	
666	\section{Grounding Ablation}
667	\label{app:grounding-ablation}
668	
669	We test whether directly intervening on the dominant death action (\texttt{focus on}) eliminates death vulnerability on the 10 death-prone tasks (baseline 48.0\%, $n{=}200$).
670	
671	\paragraph{Prompt warning.} Adding an explicit system prompt (``use \texttt{focus on} only for final answers'') reduces aggregate death rate to 37.0\% ($\Delta = -11$~pp). Both identification tasks exhibit ironic effects (\texttt{identify-life-stages-1}: 35\%$\to$50\%; \texttt{identify-life-stages-2}: 25\%$\to$70\%), where explicit mention of the dangerous action may have increased its salience.
672	
673	\paragraph{Action-space filtering.} Blocking \texttt{focus on} during the exploration phase yields 379 blocks across 200 episodes with zero leaks and zero passthroughs (the agent never persisted in retrying blocked actions), reducing death rate to 29.0\% ($\Delta = -19$~pp). The zero-passthrough rate suggests \texttt{focus on} use is a shallow behavioral pattern rather than a deliberate strategy.
674	
675	\paragraph{Per-task variation.} Under filtering, \texttt{identify-life-stages} and \texttt{inclined-plane} approach deterministic-level safety (${\sim}$15--20\% DR), while \texttt{chemistry-mix} and \texttt{find-animal} remain at 35--40\%. Residual deaths occur during the answer-submission window, where the filter is inactive and agents submit \texttt{focus on} to incorrect objects.
676	
677	\paragraph{Post-ablation counterfactual decomposition.}
678	To test whether death dominance persists after grounding intervention, we run the full decomposition on matched episodes (183 episodes across 10 death-prone task types, paired by variation index).
679	Grounding reduces the internal death rate from 50.3\% to 35.0\% ($-15.3$\,pp), yet $\geq$93\% of disambiguating labels still arise from death asymmetry ($\Delta_\text{nd} \approx 0.09$, compared to $0.00$ at baseline).
680	Internal-preferred episodes increase from 5 to 23 (grounding helps internal strategy survive more often), but the routing signal remains death-driven rather than score-driven.
681	One task type (\texttt{identify-life-stages-2}, $n{=}10$) shows a paradoxical increase in death rate (50\%$\to$80\%); this outlier likely reflects the small sample size and task-specific prompt interference rather than a systematic effect.
682	
683	\section{Ablation Studies}
684	\label{app:ablations}
685	
686	\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B and evaluate at both step and episode level (Table~\ref{tab:capacity}).
687	
688	\begin{table}[h]
689	\centering
690	\small
691	\begin{tabular}{@{}lcc@{}}
692	\toprule
693	Model & Step Bal.\ Acc.\ (\%) & Ep.\ Bal.\ Acc.\ (\%) \\
694	\midrule
695	Qwen3-0.6B & $56.4 \pm 3.5$ & $50.7 \pm 2.6$ \\
696	Qwen3-1.7B & $58.2 \pm 4.0$ & $43.1 \pm 1.0$ \\
697	Qwen3-4B & $59.2 \pm 3.5$ & $\mathbf{59.0 \pm 1.9}$ \\
698	\midrule
699	Always-det & 50.0 & 50.0 \\
700	\bottomrule
701	\end{tabular}
702	\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\%$, $p < 0.005$).}
703	\label{tab:capacity}
704	\end{table}
705	
706	Step-level balanced accuracy is flat across scales ($56$--$59\%$, within seed variance); step-level discrimination is not capacity-sensitive. At episode level, only 4B breaks the random baseline ($59.0 \pm 1.9\%$, $p < 0.005$); 0.6B and 1.7B remain at or below chance. The 1.7B model's below-chance episode-level accuracy ($43.1\%$) may reflect overfitting to spurious step-level correlations that anti-correlate with episode outcomes; without per-class confusion matrices at this scale, this remains a hypothesis. The dominant explanation across scales is that death avoidance constitutes a task-type-level binary signal that a step-level router cannot exploit efficiently.
707	
708	\paragraph{Generative router.} A generative routing model trained with explicit routing labels achieves balanced accuracy of 46.7\%, confirming that the routing bottleneck is signal-limited, not architecture-limited.
709	
710	\paragraph{Leave-one-task-type-out routing.} Under leave-one-task-type-out evaluation, blind routing collapses to always-deterministic (balanced accuracy 50.0\%); a keyword-based variant achieves 62.9\% only through task-identity leakage, not genuine routing signal. A guided router evaluated under the same protocol confirms this: without task-type identifiers it achieves chance accuracy (50.0\%), and leaking task names raises this to 62.9\%, confirming that the only learnable routing feature is task-type identity.
711	
712	\paragraph{Death-proximal labeling.} Training a router only on the $k$ steps preceding death events (rather than all steps) also collapses to majority-class prediction (step balanced accuracy 50.0\%, episode balanced accuracy 50.0\%, internal recall 0\%), confirming that the absence of step-level signal is not an artifact of label dilution across long episodes.
713	
714	\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types ($n{=}120$ episodes per condition, 6 tasks $\times$ 20 episodes per task) found no significant difference (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%); reasoning depth does not meaningfully alter internal-mode outcomes.
715	
716	\section{Threshold Routing Analysis}
717	\label{sec:threshold-routing}
718	
719	Given per-task death risk knowledge, we test whether a simple threshold routing strategy can outperform always-deterministic. For each threshold $t \in [0, 1]$, we route to internal if the per-task internal death rate $\leq t$, otherwise to deterministic, and sweep all thresholds to find the optimal.
720	
721	\begin{table}[h]
722	\centering
723	\small
724	\resizebox{\columnwidth}{!}{%
725	\begin{tabular}{lccc}
726	\toprule
727	Strategy & Mean Score & Death Rate & $\Delta$ vs Det \\
728	\midrule
729	Always-det & $-9.47$ & $0.163$ & $0.00$ \\
730	Optimal threshold ($t{=}0$) & $-11.03$ & $0.155$ & $-1.56$ \\
731	Always-internal & $-39.07$ & $0.429$ & $-29.60$ \\
732	\bottomrule
733	\end{tabular}}
734	\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\% CI for the difference: $[-8.87, +5.92]$.}
735	\label{tab:threshold-routing}
736	\end{table}
737	
738	Even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic. The sole zero-death task achieves higher scores under deterministic (+28.5) than internal (+18.9), leaving no room for a beneficial mixed strategy.
739	
740	\section{Practitioner Decision Framework}
741	\label{app:decision-framework}
742	
743	Given a new interactive environment, the following three-stage procedure diagnoses whether learned routing adds value over a fixed deterministic strategy.
744	
745	\paragraph{Stage 1: Pilot collection (${\sim}$50 episodes).}
746	Run pure-internal and pure-deterministic strategies on a representative sample (${\sim}$50 episode pairs). Compute the death-rate differential $\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$.
747	
748	\paragraph{Stage 2: Death dominance check.}
749	If $\Delta\text{DR} > 15$~pp, death asymmetry is likely the dominant routing signal. Compute the death-label fraction $f_{\text{death}}$: the proportion of non-tie routing labels where exactly one strategy dies.
750	
751	\paragraph{Stage 3: Decision.}
752	If $f_{\text{death}} > 75\%$, the routing signal is death-dominated; a fixed deterministic strategy will match or exceed any learned router. If $f_{\text{death}} < 50\%$, diverse routing signals may justify a learned router. Between 50\%--75\%, collect additional episodes to reduce estimation noise before committing to router development.
753	
754	\paragraph{Retrospective validation.}
755	All four experimental conditions in this paper are correctly classified:
756	
757	\begin{table}[h]
758	\centering
759	\small
760	\begin{tabular}{@{}lrrll@{}}
761	\toprule
762	Condition & $\Delta$DR & $f_{\text{death}}$ & Prediction & Actual \\
763	\midrule
764	Qwen-7B & +26.5 & 78.9\% & det-fixed & det wins \\
765	Llama-8B & +30.0 & $>$75\% & det-fixed & det wins \\
766	Qwen-72B & +27.8 & $>$75\% & det-fixed & det wins \\
767	MATH & +0.5 & 0\% & router viable & no signal \\
768	\bottomrule
769	\end{tabular}
770	\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}
771	\label{tab:decision-framework}
772	\end{table}
773	
774	The framework also predicts the inverted-U relationship between capability and death risk: below ${\sim}$0.5B parameters, agents rarely reach dangerous states (13.3\% death rate in a 15-episode pilot), so $\Delta\text{DR}$ is low and the framework would not recommend fixed-deterministic. Above ${\sim}$7B, agents are capable enough to enter catastrophic states but not capable enough to avoid them, producing high $\Delta\text{DR}$.
775	
776	\paragraph{Threshold calibration.} The thresholds above (15~pp, 75\%, 50\%) are illustrative, derived from ScienceWorld's specific reward structure (binary death penalty $P{=}100$, sparse terminal rewards). Environments with graded penalties, dense rewards, or qualitatively different failure modes may require different thresholds. Practitioners should calibrate these boundaries for their specific environment.
777	
778	\section{Extended Validation of Excluded Tasks}
779	\label{app:extended-validation}
780	
781	To verify that task exclusion does not bias toward death-prone tasks, we collect $n{=}20$ episodes for five representative excluded tasks spanning all exclusion categories (Table~\ref{tab:extended-val}).
782	
783	\begin{table}[h]
784	\centering
785	\small
786	\resizebox{\columnwidth}{!}{%
787	\begin{tabular}{lcrrrrc}
788	\toprule
789	Task & Category & $n$ & Int DR & Det DR & $\Delta$DR & D/I/N \\
790	\midrule
791	boil & dev-set & 20 & 55\% & 25\% & +30\,pp & 6/0/14 \\
792	melt & dev-set & 20 & 45\% & 20\% & +25\,pp & 7/2/11 \\
793	find-living-thing & taxonomic & 20 & 55\% & 15\% & +40\,pp & 10/0/10 \\
794	use-thermometer & agent-floor & 20 & 50\% & 20\% & +30\,pp & 7/1/12 \\
795	power-component & agent-floor & 20 & 50\% & 15\% & +35\,pp & 7/0/13 \\
796	\midrule
797	\textit{Mean (5 tasks)} & & 100 & 51.0\% & 19.0\% & +32.0\,pp & 37/3/60 \\
798	\bottomrule
799	\end{tabular}}
800	\caption{Extended validation ($n{=}20$) of representative excluded task types. All five tasks confirm death asymmetry; mean $\Delta$DR $= +32.0$\,pp is consistent with the $n{=}5$ prescreening estimate for these same tasks (Table~\ref{tab:excluded-death}).}
801	\label{tab:extended-val}
802	\end{table}
803	
804	Notably, the excluded-task aggregate DAF (0.991) exceeds the included-task DAF (0.904; Table~\ref{tab:per-task}), indicating that excluded tasks are \emph{more} death-dominated than included tasks---the opposite of a cherry-picking bias.
805	
806	\section{Agent Prompt Templates}
807	\label{app:prompt-templates}
808	
809	Below we show the complete prompt templates used for agent interaction in ScienceWorld. Both the internal (ReAct) and deterministic strategies share the same system prompt but differ in the user message template.
810	
811	\paragraph{System prompt (shared).} Used for all ScienceWorld agent interactions across both computation modes.
812	
813	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
814	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
815	  left=2mm, right=2mm, top=1mm, bottom=1mm}
816	You are an agent interacting with a ScienceWorld text
817	environment. Your goal is to complete the given task by
818	choosing actions from the available action list.
819	
820	Use the following format for each step:
821	Thought: &lt;your reasoning about what to do next>
822	Action: &lt;exact action string from the valid actions list>
823	
824	Rules:
825	- You MUST choose an action from the valid actions list.
826	  Do not invent actions.
827	- Think step by step about what physical/scientific
828	  process is needed.
829	- Pay attention to the current observation for clues
830	  about object states.
831	\end{tcblisting}
832	
833	\paragraph{Internal (ReAct) user template.} At each step, the agent receives the current observation, valid action list, and recent action history, and must select a single action.
834	
835	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
836	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
837	  left=2mm, right=2mm, top=1mm, bottom=1mm}
838	Current observation:
839	{observation}
840	
841	Valid actions:
842	{valid_actions_str}
843	
844	Previous actions taken: {history_str}
845	
846	Choose your next action.
847	\end{tcblisting}
848	
849	\paragraph{Deterministic candidate generation template.} For the deterministic strategy, the agent generates ranked candidate actions instead of selecting one; these candidates are then evaluated via simulator forking (\S\ref{sec:method}).
850	
851	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
852	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
853	  left=2mm, right=2mm, top=1mm, bottom=1mm}
854	Current observation:
855	{observation}
856	
857	Valid actions:
858	{valid_actions_str}
859	
860	Previous actions taken: {history_str}
861	
862	Generate the top 3 most promising actions from the valid
863	actions list, ranked by how likely they are to make
864	progress on the task. Output exactly 3 actions, one per
865	line, in this format:
866	1. &lt;action>
867	2. &lt;action>
868	3. &lt;action>
869	\end{tcblisting}
870	
871	\paragraph{Reflexion self-reflection prompt.} After a failed episode, the Reflexion agent (\S\ref{sec:agent-improvement}) generates a reflection that is injected into subsequent trial attempts as additional system context.
872	
873	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
874	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
875	  left=2mm, right=2mm, top=1mm, bottom=1mm}
876	You just completed an episode in a ScienceWorld text
877	environment but failed.
878	
879	Task: {task_name}
880	Final score: {final_score}
881	Outcome: {outcome}
882	Number of steps taken: {num_steps}
883	
884	Here is a summary of your actions:
885	{action_summary}
886	
887	Analyze why this episode failed and provide a short
888	strategy for the next attempt. Focus on:
889	1. What went wrong (wrong sequence, missed key step,
890	   dangerous action)?
891	2. What should be done differently next time?
892	
893	Keep your reflection under 200 words.
894	\end{tcblisting}
895	
896	\paragraph{Grounding warning (ablation).} The prompt warning condition in the grounding ablation (Appendix~\ref{app:grounding-ablation}) appends the following to the shared system prompt:
897	
898	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
899	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
900	  left=2mm, right=2mm, top=1mm, bottom=1mm}
901	CRITICAL SAFETY RULE: The 'focus on [object]' action is
902	ONLY for submitting your final answer. Do NOT use
903	'focus on' to examine, inspect, or interact with objects
904	during exploration. Using 'focus on' on the wrong object
905	will cause irreversible failure. Use 'look at',
906	'examine', or 'pick up' instead for exploration.
907	\end{tcblisting}
908	
909	\noindent The key difference between the two computation modes is the user message: the internal strategy asks the LLM to \emph{select} one action (ReAct), while the deterministic strategy asks it to \emph{rank} candidates for simulator evaluation. Both use identical system prompts and identical observation formatting.
910	
911	\section{Non-Death Episode Case Study}
912	\label{app:non-death-case-study}
913	
914	We illustrate the framework's ability to decompose non-death routing signal using \texttt{find-non-living-thing}, the only task type with zero deaths and 100\% non-death labels (\S\ref{sec:death-decomp}). Using Gemma-2-9B-it counterfactual episodes ($N{=}20$), 12 episodes show routing preference (9 deterministic-preferred, 3 internal-preferred), confirming the framework detects bidirectional signal independent of death asymmetry.
915	
916	\paragraph{Deterministic-preferred: knowledge retrieval advantage.}
917	In Episode~3 (det: 67, int: 0), the internal strategy issues nonsensical \texttt{connect} actions for 18 consecutive steps (e.g., ``connect air to outside,'' ``connect axe to door to foundry'') without ever identifying a target object; the deterministic strategy correctly focuses on ``orange'' (+58) and opens the kitchen door (+9). In Episode~17 (det: 58, int: 50), both strategies find a valid non-living thing, but the deterministic strategy selects a higher-scoring object (orange, 58\,pts) versus the internal strategy's choice (fountain, 50\,pts), illustrating that object selection quality creates routing signal even when both strategies succeed.
918	
919	\paragraph{Internal-preferred: semantic reasoning advantage.}
920	In Episode~12 (int: 67, det: 58), the task specifies ``move it to the red box in the living room.'' The deterministic strategy focuses on the red box itself---the destination container, not a separate non-living thing---scoring 58\,pts. The internal strategy correctly distinguishes target from container, choosing ``orange'' (67\,pts). This semantic error demonstrates that deterministic pattern-matching can miss task-structure subtleties that internal reasoning captures.
921	
922	These cases confirm two properties: (1)~the framework captures non-death routing signal when it exists, and (2)~signal flows in both directions---neither strategy uniformly dominates in death-free tasks.
923	
924	\paragraph{Systematic analysis of non-death labels.}
925	All 20 non-death non-tie labels in the primary Qwen2.5-7B analysis originate from \texttt{find-non-living-thing}---the sole death-free task type. In every other task type, non-tie episodes involve at least one strategy dying. We classify the 20 episodes into three error categories:
926	
927	\begin{table}[h]
928	\centering
929	\small
930	\begin{tabular}{@{}lrrr@{}}
931	\toprule
932	Error category & Det-pref & Int-pref & Total \\
933	\midrule
934	Hallucination-induced & 8 & 2 & 10 \\
935	Object selection quality & 6 & 1 & 7 \\
936	Action selection error & 2 & 1 & 3 \\
937	\bottomrule
938	\end{tabular}
939	\caption{Non-death non-tie episode classification. Hallucination-induced: agent's state model is incorrect (e.g., believing \texttt{eat} completes the task). Object selection quality: both strategies succeed but choose different-value objects. Action selection: correct state model but suboptimal action sequences.}
940	\label{tab:non-death-taxonomy}
941	\end{table}
942	
943	\noindent Hallucination-induced errors dominate (50\%), driven by a recurring ``eat before focus'' pattern: the internal strategy consumes the target object (destroying it) before attempting the scoring action (\texttt{focus on}), indicating an incorrect state model that equates eating with task completion (11 of 20 episodes). Object selection quality accounts for 35\%---typically the deterministic strategy selecting ``orange'' (58\,pts) while the internal strategy settles for lower-value objects (``fountain'' or ``picture,'' 50\,pts). The error categories are bidirectional: 2 of 10 hallucination episodes and 1 of 3 action selection episodes are internal-preferred, confirming the framework detects failures in both strategies. Score gaps reflect category severity: hallucination errors produce large gaps ($17$--$67$\,pts, one strategy scores zero) while object selection differences produce small gaps ($8$--$9$\,pts, both strategies functional).
944	
945	\section{Use of AI Assistants}
946	\label{app:ai-assistants}
947	
948	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
949	\begin{itemize}
950	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
951	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting \LaTeX{}.
952	    \item \textbf{Literature:} summarizing related papers to inform the related-work section.
953	\end{itemize}
954	
955	\end{document}
956	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59e8c71c-1175-4765-9256-a26cd527a4ef",
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "d4edeb25-63da-4295-af43-a9ca887485c9",
  "sourceToolAssistantUUID": "59e8c71c-1175-4765-9256-a26cd527a4ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T18:45:19.058Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0193uULajgxzdvz7UDEsrn7b`</summary>

```json
{
  "pattern": "includegraphics|\\\\begin\\{figure\\}|\\\\label\\{fig:|\\\\caption\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4edeb25-63da-4295-af43-a9ca887485c9",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtY3tkHWZUJtsrsENwS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb9c9033-234d-4097-bf65-7989ceda81ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BJV5T5SUmsPHV59QieBJ33",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2735,
      "cache_read_input_tokens": 38709,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 249,
          "cache_read_input_tokens": 38709,
          "cache_creation_input_tokens": 2735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2735,
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

_source line 12 · 2026-05-24T18:45:19.082Z_

<details><summary>↩ Tool result · `toolu_0193uULajgxzdvz7UDEsrn7b`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:9:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:11:\includegraphics[width=\columnwidth]{figures/label_decomposition.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:12:\caption{Episode-level label decomposition ($N{=}245$). Of 95 non-tie labels, 75 (78.9\%) arise from death asymmetry: 54 where death is the sole discriminator and 21 with co-occurring score differences. All 20 non-death labels originate from a single task type (\texttt{find-non-living-thing}).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:13:\label{fig:label-decomposition}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:20:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:22:\includegraphics[width=0.75\columnwidth]{figures/fig1_daf_scatter.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:23:\caption{Per-task death rate differential vs.\ performance gap ($n{=}11$ task types). The near-perfect correlation ($r = 0.97$) is a structural consequence of death dominance (DAF $\to 1 \Rightarrow r \to 1$), not an independent finding. The sole outlier (\texttt{find-non-living-thing}, red diamond) has zero deaths; its $\Delta_{\text{full}} = +9.58$ arises entirely from non-death score differences.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:24:\label{fig:decomposition}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:63:\caption{Internal-strategy death rates under agent improvement methods. Top: all 11 tasks (72B: independently collected at both internal and deterministic). Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded, 0\% death at all scales). All interventions reduce death rate but none approaches deterministic-level safety.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:74:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:76:\includegraphics[width=\columnwidth]{figures/dose_response.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:77:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:78:\label{fig:dose-response}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:110:\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 20--40 episodes per type, 245 total). $\dagger$\,Single random seed (42) per episode pair; see Appendix~\ref{app:seed-robustness} for 8-seed robustness analysis. Per-task results are exploratory ($n{=}20$ episodes per task, power $\approx 50\%$ for 20\,pp effects); aggregate conclusions do not depend on individual task significance.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:101:\caption{Episode-Level Counterfactual Labeling}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:161:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:203:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:232:\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:257:\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:278:\caption{Leave-one-task-out DAF sensitivity (penalty-independent label fraction). Among the 10 death-prone tasks, removing any single task changes DAF by at most 3.0\,pp (range: 75.9\%--78.9\%). Removing \emph{Find Non-Living Thing}, the sole death-free task that contributes all 20 score-comparison episodes, raises DAF to 100\% by construction.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:314:\caption{Per-task death rates (\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm stabilization at $N \geq 3$ (range: $34.0$--$36.5\%$).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:369:\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:424:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:448:\caption{Text augmentation ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original via paraphrase, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:481:\caption{Sensitivity of DAF to death penalty magnitude $P$. DAF$(P) = 1 - \Delta_{\text{nd}} / \Delta_{\text{full}}(P)$, where $\Delta_{\text{full}}(P) \approx \delta \cdot P + \Delta_{\text{nd}}$, $\delta = 0.2653$ is the death-rate differential, and $\Delta_{\text{nd}} = 2.84$ (strict neither-died filtering). Recomputed from 245 episode-level data; bootstrap 95\% CIs ($B{=}10{,}000$). \textsuperscript{*}Default setting.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:506:\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:517:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:519:\includegraphics[width=\columnwidth]{figures/signal_reversal.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:520:\caption{Cross-environment label distributions. ScienceWorld and ALFWorld both show deterministic preference, but through different mechanisms: death avoidance (ScienceWorld) vs.\ information asymmetry from admissible-action access (ALFWorld). MATH shows balanced labels, confirming no routing signal without catastrophic failure.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:521:\label{fig:signal-reversal}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:537:\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\dagger$\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:561:\caption{Per-task-type decomposition for ALFWorld (135 games, Qwen2.5-7B-Instruct). D/I/N: deterministic-preferred / internal-preferred / no-preference. No death mechanism exists; $\Delta_{\text{full}}$ is driven entirely by information asymmetry from admissible-action access. Sorted by $\Delta_{\text{full}}$ descending.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:600:\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:627:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:645:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:647:\includegraphics[width=\columnwidth]{figures/death_action_distribution.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:648:\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \texttt{connect}). Right: non-\texttt{connect} actions zoomed. \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while non-death episodes show higher rates of observation and object interaction.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:649:\label{fig:death-action-dist}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:652:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:654:\includegraphics[width=\columnwidth]{figures/death_action_timeline.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:655:\caption{Step-by-step action sequences for 6 representative death episodes. The fatal \texttt{focus on} action (marked with arrow) consistently appears in the final steps after long \texttt{connect} sequences, and illustrates the ``connect loop $\to$ fatal focus'' pattern. Examples are drawn from the full 30-task dataset for task-type diversity; the pattern is identical in the 11-task analysis subset.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:656:\label{fig:death-timeline}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:659:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:661:\includegraphics[width=\columnwidth]{figures/death_action_comparison.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:662:\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:663:\label{fig:death-comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:702:\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\%$, $p < 0.005$).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:734:\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\% CI for the difference: $[-8.87, +5.92]$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:770:\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:800:\caption{Extended validation ($n{=}20$) of representative excluded task types. All five tasks confirm death asymmetry; mean $\Delta$DR $= +32.0$\,pp is consistent with the $n{=}5$ prescreening estimate for these same tasks (Table~\ref{tab:excluded-death}).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:939:\caption{Non-death non-tie episode classification. Hallucination-induced: agent's state model is incorrect (e.g., believing \texttt{eat} completes the task). Object selection quality: both strategies succeed but choose different-value objects. Action selection: correct state model but suboptimal action sequences.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex:4:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex:6:\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex:7:\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex:8:\label{fig:pipeline}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb9c9033-234d-4097-bf65-7989ceda81ac",
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "351c6b56-8bbc-449d-ba62-20a735b0c334",
  "sourceToolAssistantUUID": "cb9c9033-234d-4097-bf65-7989ceda81ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-24T18:45:21.222Z_

Now let me read each tex file individually to get the complete picture:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "351c6b56-8bbc-449d-ba62-20a735b0c334",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtYDeshp5z6bjUZ7Sb6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "87d09833-4525-43da-983a-1bb877bc3622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RLWq2TAJKvhBGiaKn7UAEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 31577,
      "cache_read_input_tokens": 41444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31577,
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

_source line 14 · 2026-05-24T18:45:21.554Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M6HZSqt7ZMTZHR8cqmfxtL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87d09833-4525-43da-983a-1bb877bc3622",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtYDeshp5z6bjUZ7Sb6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "323c11ed-90e2-44db-8108-34815ce631a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RLWq2TAJKvhBGiaKn7UAEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 31577,
      "cache_read_input_tokens": 41444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31577,
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

_source line 15 · 2026-05-24T18:45:21.568Z_

<details><summary>↩ Tool result · `toolu_01M6HZSqt7ZMTZHR8cqmfxtL`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
7	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
8	\label{fig:pipeline}
9	\end{figure}
10	
11	Our diagnostic framework quantifies what drives routing signal in interactive environments through two components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). A supplementary Signal Concentration Index (SCI; Appendix~\ref{app:sci}) measures whether signal is concentrated in a few task types. Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
12	
13	\subsection{Problem Setup}
14	\label{sec:problem-setup}
15	
16	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\citep{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), a privileged-information strategy (an umbrella term: ground-truth simulator access in ScienceWorld, code interpreter in MATH, admissible-action enumeration in ALFWorld---see \S\ref{sec:cross-env} for environment-specific operationalizations) that eliminates observation uncertainty; these qualitative differences affect what routing signals the framework can detect. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which computation mode to use at each step; our analysis investigates what signal is available to learn $\rho$.
17	
18	\subsection{Counterfactual Episode Collection}
19	\label{sec:collection}
20	
21	Per-step oracle labeling degenerates under sparse terminal rewards: on ScienceWorld \citep{scienceworld-2022}, 97.4\% of steps (5{,}935 of 6{,}094 across 11 prescreened task types) produce identical intermediate scores, yielding no per-step routing signal. Episode-level comparison---directly measuring terminal outcomes---is therefore the principled granularity for sparse-reward environments.
22	
23	\paragraph{Pure-strategy trajectories.}
24	For a task instance $t$ and computation mode $m \in \mathcal{M}$, a \emph{pure-strategy trajectory} is the complete episode obtained by applying mode $m$ at every step:
25	\begin{equation}
26	    \tau_m^{(t)} = (o_1, a_1, o_2, a_2, \ldots, o_T, a_T)
27	\end{equation}
28	where $T \leq T_{\max}$ is the episode length (capped at $T_{\max} = 30$ steps). Both trajectories $\tau_{\tt int}^{(t)}$ and $\tau_{\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), so performance differences arise solely from the computation mode choice.
29	
30	Each trajectory $\tau$ yields a terminal score $s(\tau) \in \mathbb{Z}$ and a death indicator $d(\tau) \in \{0, 1\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:
31	\begin{multline}
32	    \bigl(s^{\tt int}, s^{\tt det}, d^{\tt int}, d^{\tt det}\bigr) \triangleq \\
33	    \bigl(s(\tau_{\tt int}),\, s(\tau_{\tt det}),\, d(\tau_{\tt int}),\, d(\tau_{\tt det})\bigr)
34	\end{multline}
35	
36	We use Qwen2.5-7B-Instruct~\citep{qwen25-2024} (vLLM v0.21.0) on ScienceWorld \citep{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty; complete prompt templates are provided in Appendix~\ref{app:prompt-templates}. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is applicable to any environment where paired episodes under two computation modes can be collected with binary success/failure indicators. We apply it unchanged to ALFWorld and MATH in \S\ref{sec:math-contrast}--\ref{sec:cross-env}.
37	
38	\subsection{Episode-Level Labeling}
39	\label{sec:labeling}
40	
41	We define a labeling function $L$ that maps a counterfactual pair to a routing preference:
42	\begin{multline}
43	    L\!\bigl(\tau_{\tt int}^{(t)}, \tau_{\tt det}^{(t)}\bigr) \;\rightarrow \\
44	    \ell \in \{{\tt det\text{-}pref},\; {\tt int\text{-}pref},\; {\tt no\text{-}pref}\}
45	\end{multline}
46	
47	The labeling function is \emph{death-aware}: it prioritizes survival over score, then compares scores among same-status episodes (Algorithm~\ref{alg:labeling}; Appendix~\ref{app:labeling}). Both-dead episodes receive \texttt{no\_preference} because ScienceWorld's fixed $-100$ penalty makes death timing uninformative. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. Figure~\ref{fig:pipeline} illustrates the overall pipeline; label distributions are reported in \S\ref{sec:death-decomp}.
48	
49	\subsection{Death Avoidance Factor}
50	\label{sec:daf}
51	
52	To quantify the contribution of death avoidance to routing signal, we decompose the mean score gap between strategies. Let $\delta = \mathbb{E}[d^{\tt int}] - \mathbb{E}[d^{\tt det}]$ denote the death-rate differential and $\Delta_{\text{nd}}$ the mean score gap restricted to episodes where neither strategy dies. Partitioning episodes by death status, death-asymmetric episodes (where only one strategy dies) contribute a per-episode gap of $P + \bar{s}_{\text{surv}}$, where $\bar{s}_{\text{surv}}$ is the surviving strategy's mean score; when $\bar{s}_{\text{surv}} \ll P$ (in our data, $\bar{s}_{\text{surv}} = 0.87$, or $0.9\%$ of $P$), these episodes contribute ${\approx}\,\delta P$ in aggregate. The full gap thus decomposes as:
53	\begin{equation}
54	    \Delta_{\text{full}} \approx \underbrace{\delta \cdot P}_{\text{death contribution}} + \Delta_{\text{nd}}
55	\end{equation}
56	The approximation residual is $29.60 - 29.37 = 0.23$ ($0.8\%$ of $\Delta_{\text{full}}$).
57	
58	We define the Death Avoidance Factor (DAF) as the fraction of the full score gap attributable to death avoidance:
59	\begin{equation}
60	    \text{DAF} = 1 - \frac{\Delta_{\text{nd}}}{\Delta_{\text{full}}} \approx \frac{\delta P}{\delta P + \Delta_{\text{nd}}}
61	\end{equation}%
62	\footnote{When $\Delta_{\text{nd}} < 0$ (deterministic strategy scores lower than internal on non-death episodes), DAF exceeds 1; death avoidance then overcompensates for a non-death disadvantage.}
63	
64	Since DAF $= \delta P / (\delta P + \Delta_{\text{nd}})$, it increases monotonically with $P$, a mathematical consequence rather than an empirical finding. For context: DAF $= 50.4\%$ at $P{=}10$, $82.6\%$ at $P{=}50$, and $90.4\%$ at $P{=}100$ (full curve in Appendix~\ref{app:penalty}). We treat the label fraction (78.9\%) as the primary, penalty-invariant diagnostic and DAF as a supplementary, environment-specific measure. In ScienceWorld, $P$ affects only post-hoc score calculation; the agent's policy (ReAct prompting) does not include $P$ in its observation, so death rates and $\Delta_{\text{nd}}$ are $P$-invariant by design~\citep{ng1999policy} (Appendix~\ref{app:penalty}).
65	
66	\paragraph{Relationship between DAF and label fraction.}
67	DAF (90.4\%) exceeds the label fraction (78.9\%) because death episodes carry disproportionately large score gaps ($P{=}100 \gg$ typical non-death $\Delta{\approx}29$), amplifying their weight in score-weighted aggregation. The label fraction, invariant to penalty magnitude, serves as the primary finding; DAF reflects the score-space reality under ScienceWorld's reward structure.
68	
69	\paragraph{Statistical inference.}
70	We quantify uncertainty via episode-level bootstrap resampling ($B = 10{,}000$). Each resample draws $N = 245$ episodes with replacement, recomputes all metrics, and derives percentile-based 95\% CIs. We resample at the episode level (not the step level) because the episode is the unit of counterfactual comparison. Penalty sensitivity analysis across hypothetical $P$ values is in Appendix~\ref{app:penalty}.
71	
72	We also measure whether death-avoidance signal is concentrated in a few task types via a Signal Concentration Index (SCI $\in [0, 1]$; Appendix~\ref{app:sci}), reported in \S\ref{sec:death-decomp}.
73	
74	\paragraph{Scope of episode-level analysis.}
75	At step level, 97.4\% of oracle comparisons yield ties (\S\ref{sec:collection}); of 2{,}040 training steps, only 0.3\% exhibit strict directional conflict with episode labels, with 60.3\% pre-event neutral (neither strategy advantaged). Episode labels thus apply correct direction to uninformative steps---a granularity mismatch, not label error---explaining why step-level router training approaches chance performance (\S\ref{sec:router-diagnostic}).
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "323c11ed-90e2-44db-8108-34815ce631a7",
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "13feffef-b1f9-4a0e-b36e-d5eabe37b197",
  "sourceToolAssistantUUID": "323c11ed-90e2-44db-8108-34815ce631a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T18:45:21.708Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FXpBQRrRkYZksenUHiwY5V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13feffef-b1f9-4a0e-b36e-d5eabe37b197",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtYDeshp5z6bjUZ7Sb6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ca8173cf-da44-4551-a9bc-fa47d5ef1654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RLWq2TAJKvhBGiaKn7UAEU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 31577,
      "cache_read_input_tokens": 41444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31577,
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

_source line 17 · 2026-05-24T18:45:21.717Z_

<details><summary>↩ Tool result · `toolu_01FXpBQRrRkYZksenUHiwY5V`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). Taxonomically redundant tasks share identical action vocabularies, reward functions, and environmental dynamics, differing only in target entity; we retain one representative per family (Appendix~\ref{app:per-task}). This scope limits generalizability: conclusions apply to the included subset; increasing the 30-step budget might surface signal in excluded types (see Limitations). An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}). Extended validation at $n{=}20$ on five representative excluded tasks confirms this direction ($\overline{\Delta\text{DR}} = +32.0$\,pp; Appendix~\ref{app:extended-validation}). A reasoning-depth ablation ($n{=}120$) found no significant difference between internal strategy variants ($p > 0.26$; Appendix~\ref{app:ablations}). Prescreening used $n{=}5$ episodes per task type; directional consistency (18/19 types favoring deterministic) rather than point estimates drives the inclusion criterion.
5	
6	\subsection{Death Avoidance Decomposition}
7	\label{sec:death-decomp}
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{figures/label_decomposition.pdf}
12	\caption{Episode-level label decomposition ($N{=}245$). Of 95 non-tie labels, 75 (78.9\%) arise from death asymmetry: 54 where death is the sole discriminator and 21 with co-occurring score differences. All 20 non-death labels originate from a single task type (\texttt{find-non-living-thing}).}
13	\label{fig:label-decomposition}
14	\end{figure}
15	
16	Of the 95 non-tie routing labels (Figure~\ref{fig:label-decomposition}), 75 (78.9\%; 95\% CI: $[70.7\%, 87.0\%]$, episode-level bootstrap) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these, 54 are sole-signal labels where death was the only discriminator; at $P{=}0$ these reduce to ties, but the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}).
17	
18	Of 245 episodes, 150 (61.2\%) show no preference between strategies; routing is relevant in the remaining 95 (38.8\%). Among these, death avoidance dominates. The Death Avoidance Factor, a derived penalty-dependent measure, quantifies death's contribution to the total performance gap: DAF $= 90.4\%$ at $P{=}100$ ($\Delta_{\text{full}} = +29.60$, $\Delta_{\text{nd}} = +2.84$, 95\% CI$_{\text{nd}}$: $[0.34, 5.57]$; 95\% CI$_{\text{DAF}}$: $[81.3\%, 99.1\%]$, episode-level bootstrap, $B{=}10{,}000$). DAF varies monotonically with $P$ (\S\ref{sec:daf}; Appendix~\ref{app:penalty}), confirming that the 78.9\% label fraction provides the more robust characterization. When $\Delta_{\text{nd}} \to 0$, DAF $\to 1$ is algebraic necessity regardless of actual death dominance; conversely, when $\Delta_{\text{nd}} < 0$ (as in Reflexion $N{\geq}3$; \S\ref{sec:agent-improvement}), DAF exceeds 100\%, reflecting that death asymmetry more than accounts for the full gap.
19	
20	\begin{figure}[t]
21	\centering
22	\includegraphics[width=0.75\columnwidth]{figures/fig1_daf_scatter.pdf}
23	\caption{Per-task death rate differential vs.\ performance gap ($n{=}11$ task types). The near-perfect correlation ($r = 0.97$) is a structural consequence of death dominance (DAF $\to 1 \Rightarrow r \to 1$), not an independent finding. The sole outlier (\texttt{find-non-living-thing}, red diamond) has zero deaths; its $\Delta_{\text{full}} = +9.58$ arises entirely from non-death score differences.}
24	\label{fig:decomposition}
25	\end{figure}
26	
27	\paragraph{Per-task correlation structure.}
28	The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$); a detailed failure-mode analysis reveals that all 105 internal-strategy deaths are triggered by the \texttt{focus} action (Appendix~\ref{app:failure-modes}). Per-task death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}); since DAF$\to 1$ implies $r \to 1$ by construction, the near-perfect correlation is a consistency check, not an independent finding (Appendix~\ref{app:correlation}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}.
29	
30	\paragraph{Signal concentration and binary structure.}
31	The Signal Concentration Index (SCI $= 0.2147$; Appendix~\ref{app:sci}) confirms low concentration: the top-3 task types account for only $39.8\%$ of total death-rate differential. The aggregate 78.9\% reflects a per-task binary structure: all 10 death-prone task types produce 100\% death-asymmetry labels, while \texttt{find-non-living-thing} (zero deaths, $\Delta = +9.58$ from non-death scores; case study in Appendix~\ref{app:non-death-case-study}) produces 0\%. The framework thus diagnoses a binary property (``is this environment death-dominated?'') rather than a continuous routing signal. A systematic decomposition of all 20 non-death labels (Appendix~\ref{app:non-death-case-study}) reveals they originate exclusively from this single task type, with hallucination-induced errors (50\%) dominating over object selection quality differences (35\%). Removing \texttt{find-non-living-thing} raises the label fraction to 100\% and yields DAF $\geq$100\% ($\Delta_\text{nd} \leq 0$; death avoidance fully accounts for the routing gap among remaining task types; Appendix~\ref{app:loto-daf}).
32	
33	\paragraph{Sensitivity and seed robustness.}
34	Non-clustered episode-level bootstrap ($B = 10{,}000$) yields 95\% CI $[81.3\%, 99.1\%]$ for DAF; cluster-robust CI $[73.3\%, 100.0\%]$ ($K{=}11$; Appendix~\ref{app:wild-cluster}). Leave-one-task-out analysis confirms stability (label fraction range: 75.9\%--78.9\%; Appendix~\ref{app:loto-daf}); two independent replications---cross-model (Gemma-2-9B-it, DAF${}\,{=}\,89.7\%$; \S\ref{sec:cross-model}) and same-model with a different environment seed (seed=123, $N{=}220$, DAF${}\,{=}\,89.7\%$; Appendix~\ref{app:seed-robustness})---both converge within 0.7~pp. Exact permutation ($p=0.002$) and sign tests ($p<0.001$) on $K{=}11$ task-type clusters provide distribution-free confirmation (Appendix~\ref{app:wild-cluster}; supplementary evidence in Appendix~\ref{app:per-task-ci}).
35	
36	\subsection{Multi-Model Validation (7--9B Tier)}
37	\label{sec:cross-model}
38	
39	A Llama-3.1-8B-Instruct~\citep{llama3-2024} cross-model replication across all 11 task types ($N{=}220$) confirms that death dominance replicates across model families: internal death rate $41.4\%$ vs.\ deterministic $11.4\%$ (death-rate differential $+30.0$~pp), DAF $= 88.2\%$ (95\% CI: $[80.2\%, 95.1\%]$; $\Delta_{\text{full}} = +33.17$, $\Delta_{\text{nd}} = +3.9$), with direction consistency 10/10 on death-prone tasks, 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
40	Both models show ${\sim}42\%$ internal vulnerability ($+26.5$ vs.\ $+30.0$~pp differential; per-task details in Appendix~\ref{app:cross-model}).
41	A third model family, Gemma-2-9B-it~\citep{gemma2-2024} (sliding window attention, vs.\ full attention in Qwen/Llama), independently confirms the pattern: DAF${=}89.7\%$ (95\% CI $[79.5\%, 98.4\%]$; $N{=}220$), with all 10 death-prone task types showing positive $\Delta$DR (Appendix~\ref{app:cross-model}). Three architecturally distinct models thus converge on DAF $88$--$90\%$ (spread 2.2~pp); $10{\times}$ scaling to two independent 70B-class models (\S\ref{sec:agent-improvement}) confirms persistence---and intensification---across capability levels (DAF${=}92.4$--$101.0\%$).
42	
43	\subsection{Agent Improvement Baselines}
44	\label{sec:agent-improvement}
45	
46	\begin{table}[t]
47	\centering
48	\small
49	\begin{tabular}{@{}lrr@{}}
50	\toprule
51	Condition & Death\% & $N$ \\
52	\midrule
53	Single-trial baseline & 42.9 & 245 \\
54	Reflexion ($3{\times}$) & 31.4 & 220 \\
55	Qwen2.5-72B ($10{\times}$) & 30.6 & 255 \\
56	Deterministic baseline & 16.3 & 245 \\
57	\midrule
58	\multicolumn{3}{@{}l}{\textit{10 death-prone tasks only:}} \\
59	Death-prone baseline & 48.0 & 200 \\
60	Retry ($5{\times}$) & 43.5 & 200 \\
61	\bottomrule
62	\end{tabular}
63	\caption{Internal-strategy death rates under agent improvement methods. Top: all 11 tasks (72B: independently collected at both internal and deterministic). Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded, 0\% death at all scales). All interventions reduce death rate but none approaches deterministic-level safety.}
64	\label{tab:agent-improvement}
65	\end{table}
66	
67	We test whether agent-level improvement reduces death dominance (Table~\ref{tab:agent-improvement}). Retry ($N{=}5$ attempts without self-correction) yields marginal reduction on death-prone tasks ($43.5\%$ vs.\ $48.0\%$ baseline, $\Delta = -4.5$~pp). Reflexion~\citep{reflexion-2023}\footnote{Reflexion uses a fixed allocation of 20 episodes per task type ($20 \times 11 = 220$), vs.\ the baseline's variable 20--40 per type ($N{=}245$).} (verbal self-reflection between trials) reduces death to 31.4\% across all 11 tasks by rescuing 29.3\% of first-trial deaths, but the gap to deterministic remains 15.1~pp; on the 10 death-prone tasks, Reflexion achieves ${\sim}$35\%. Under Reflexion ($N{=}3$, matched-episode analysis), $\Delta_{\text{nd}} = -0.47$, yielding DAF $> 100\%$: the deterministic advantage is entirely attributable to death avoidance, and in non-death episodes the self-correcting agent slightly outperforms the deterministic baseline. Scaling to Qwen2.5-72B ($10{\times}$ parameters; both strategies independently collected at 72B, 255 episodes across all 11 task types) reduces death rate to $30.6\%$. The 72B deterministic strategy achieves $2.75\%$ death rate ($\Delta\text{DR} = +27.8$~pp), and $\Delta_{\text{nd}} = +2.28$, yielding DAF $= 92.4\%$ (95\% CI: $[86.1\%, 97.9\%]$; 7B: $90.4\%$), with 5 internal-preferred episodes (vs.\ 9 at 7B; $2.0\%$ vs.\ $3.7\%$).
68	A second 70B-class model, Llama-3.1-70B-Instruct ($N{=}220$), intensifies the pattern: internal death rate $48.6\%$, deterministic $20.0\%$ ($\Delta\text{DR} = +28.6$~pp), $\Delta_{\text{nd}} = -0.30$, yielding DAF $= 101.0\%$ (95\% CI: $[95.3\%, 107.5\%]$). DAF exceeding 100\% indicates that death avoidance more than fully explains the deterministic advantage---when both agents survive, the internal agent performs comparably or slightly better. Label fraction rises to $91.3\%$ (67 det-preferred, 2 int-preferred; Appendix~\ref{app:cross-model}).
69	Two independent 70B-class models thus confirm that $10{\times}$ scaling does not attenuate death dominance; it intensifies proportional dominance because the deterministic strategy maintains substantially lower death rates than the internal strategy at both 70B scales ($2.75$--$20.0\%$ vs.\ $30.6$--$48.6\%$).
70	
71	\paragraph{Dose-response analysis.}
72	We extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\ref{fig:dose-response}). Retry is nearly flat ($48.0\% \to 43.5\%$). Reflexion drops steeply to $34.0\%$ at $N{=}3$ ($\Delta = -13.5$~pp, $p = 0.003$) then stabilizes ($34$--$36.5\%$ for $N \geq 3$, pairwise $p > 0.5$); both the decline and plateau are well-powered (MDE ${\sim}8$~pp at 80\% power; Appendix~\ref{app:dose-response}).
73	
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=\columnwidth]{figures/dose_response.pdf}
77	\caption{Death rate as a function of trial count ($N$) for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Retry (blue) is nearly flat; Reflexion (red) drops steeply through $N{=}3$ then shows no statistically detectable improvement beyond $N{=}3$ (Wilson CIs for $N{=}3,4,5$ overlap substantially). Horizontal lines: 72B scaling baseline ($30.6\%$) and deterministic baseline ($16.3\%$), both computed over all 11 task types; retry and Reflexion use 10 death-prone types only. Error bands: Wilson 95\% CIs.}
78	\label{fig:dose-response}
79	\end{figure}
80	
81	\subsection{Cross-Environment Boundary Probes}
82	\label{sec:math-contrast}
83	\label{sec:cross-env}
84	
85	We examine MATH and ALFWorld as boundary probes (not cross-domain validation). The deterministic oracle differs in information privilege across environments---ground-truth simulator (ScienceWorld), code interpreter (MATH), admissible-action enumeration (ALFWorld; \S\ref{sec:problem-setup})---so cross-environment results validate the diagnostic procedure's reusability, not the transferability of specific findings.
86	
87	\paragraph{MATH.} On MATH Level~4--5~\citep{math-2021} ($N{=}795$, code interpreter), internal reasoning and code interpretation achieve near-identical accuracy ($73.5\%$ vs.\ $73.0\%$, McNemar $p = 0.81$), with 84.4\% no-preference. Without catastrophic failure, no routing signal emerges.
88	
89	\paragraph{ALFWorld.} ALFWorld~\citep{alfworld-2021} (6 task types, 135 games) provides the deterministic strategy with admissible actions, an information asymmetry rather than a computation mode switch, with no death mechanism ($\delta = 0$, DAF $= 0\%$). With Qwen2.5-7B, 35 of 37 non-tie labels (94.6\%) favor the information-advantaged strategy (Appendix~\ref{app:cross-env-details}); Llama-3.1-8B (135 games) yields 16 of 16 non-tie labels in the same direction (100\%). Llama shows fewer non-tie episodes (11.9\% vs.\ 25.9\%) but perfect directional consistency, confirming that information asymmetry, not death avoidance, drives routing signal in ALFWorld regardless of model family. The framework diagnoses this qualitatively different mechanism (DAF $= 0\%$ vs.\ $90.4\%$) without modification.
90	
91	\subsection{Baselines}
92	\label{sec:baselines}
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\resizebox{\columnwidth}{!}{%
98	\begin{tabular}{@{}lccc@{}}
99	\toprule
100	Strategy & Score & 95\% CI & Death \% \\
101	\midrule
102	Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
103	Always-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
104	Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
105	Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
106	\midrule
107	Trained Router$^\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\
108	\bottomrule
109	\end{tabular}}
110	\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 20--40 episodes per type, 245 total). $\dagger$\,Single random seed (42) per episode pair; see Appendix~\ref{app:seed-robustness} for 8-seed robustness analysis. Per-task results are exploratory ($n{=}20$ episodes per task, power $\approx 50\%$ for 20\,pp effects); aggregate conclusions do not depend on individual task significance.}
111	\label{tab:baselines}
112	\end{table}
113	
114	Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points. The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic---an \emph{oracle degeneracy} where an always-deterministic lookup achieves 90.5\% of non-tie oracle decisions (balanced accuracy 50.0\%: perfect deterministic recall, zero internal recall). Even with perfect per-task death-risk knowledge, threshold routing cannot outperform the always-deterministic baseline (Appendix~\ref{sec:threshold-routing}).
115	
116	\subsection{Router Training: Inconclusive Results}
117	\label{sec:router-diagnostic}
118	
119	We probe whether counterfactual labels can train a step-level router, as a diagnostic of label informativeness. The oracle margin (2.89 points) caps routing upside. An implicit router (Qwen3, Low-Rank Adaptation (LoRA); Appendix~\ref{app:router-details}) trained at three scales (0.6B, 1.7B, 4B) shows flat step-level balanced accuracy ($56$--$59\%$); episode-level independent evaluation yields $47.1 \pm 2.2\%$, below the majority-vote baseline.\footnote{The near-chance performance is consistent with noisy-label learning bounds~\citep{natarajan2013learning,northcutt2021confident}: ${\sim}$88\% of step-level labels are uninformative, class imbalance is extreme (90.5\% deterministic-preferred, 3.7\% minority), and paraphrase-based text augmentation (25\%--800\%) provides no improvement (Appendix~\ref{app:seed-robustness}).} Leave-one-task-type-out analysis degrades to chance (49.2\%; Appendix~\ref{app:ablations}), as does a task-type-only classifier ($64.7\%$ in-distribution, $50.0\%$ leave-one-task-out (LOTO)), confirming routing signal is a per-task-type constant with no cross-type generalization. Deployed end-to-end, the best router scores $-10.70$ (95\% CI: $[-16.33, -5.27]$), not exceeding always-deterministic ($-9.47$). Results remain inconclusive under the current data regime ($N{=}245$, 3.7\% minority class).
120	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca8173cf-da44-4551-a9bc-fa47d5ef1654",
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "cc2b64bd-d758-4f5a-8eac-e4713b9823f0",
  "sourceToolAssistantUUID": "ca8173cf-da44-4551-a9bc-fa47d5ef1654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T18:45:21.957Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Sn7V1e24DUvRCAmgy1pPvU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc2b64bd-d758-4f5a-8eac-e4713b9823f0",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtYDeshp5z6bjUZ7Sb6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fdea5fb4-7917-421c-9d94-b51c7d274f1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RLWq2TAJKvhBGiaKn7UAEU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 31577,
      "cache_read_input_tokens": 41444,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 31577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 265,
          "cache_read_input_tokens": 41444,
          "cache_creation_input_tokens": 31577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 31577,
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

_source line 19 · 2026-05-24T18:45:21.971Z_

<details><summary>↩ Tool result · `toolu_01Sn7V1e24DUvRCAmgy1pPvU`</summary>

```text
1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	In ScienceWorld \citep{scienceworld-2022}, a text-based science simulation, internal reasoning is error-prone, as the model may hallucinate state changes (e.g., that water has boiled when the stove was never activated), while deterministic external computation eliminates such errors via exact state transitions. The practical question: \emph{when should an agent route computation externally versus internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision: Toolformer \citep{toolformer-2023} inserts API calls by perplexity reduction; ART \citep{art-2023} decomposes tasks into tool-augmented programs; Chameleon \citep{chameleon-2023} selects heterogeneous modules per subtask; adaptive-computation methods route to different reasoning depths \citep{cogrouter-2026,ares-2026}, model tiers \citep{mtrouter-2026}, or episode-level model selection under sparse rewards \citep{budget-aware-routing-2026}; concurrent analyses further presuppose diverse routing signals~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026}. These approaches, which operate in non-catastrophic settings, share the assumption that routing signal stems from diverse sources and a learned router can exploit it---an assumption that remains untested: no prior work has systematically decomposed what drives routing preferences in interactive environments.
7	
8	We propose a \emph{diagnostic framework} comprising (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding. Always-deterministic matches 96.3\% of oracle decisions, capping routing's marginal value at 2.89 points (\S\ref{sec:baselines}); removing death episodes reveals that oracle access provides almost no non-death advantage ($\Delta_{\text{nd}} = +2.84$, 9.6\% of total gap; \S\ref{sec:death-decomp}). Two independent 70B-class models yield DAF${}=92.4$--$101.0\%$ (Llama-70B exceeds 100\%: death avoidance more than fully accounts for the gap), and Reflexion ($N{=}3$) similarly drives DAF above 100\% (\S\ref{sec:agent-improvement}).
9	
10	This addresses a methodological gap: per-step oracle comparison degenerates under sparse rewards (97.4\% tie rate; \S\ref{sec:collection}), and keyword-based heuristics fail structurally (\S\ref{sec:baselines}). Our approach runs complete episodes under pure-internal (ReAct \citep{react-2023}) and pure-deterministic strategies, comparing episode outcomes.
11	
12	Cross-context checks probe specificity: MATH Level~4--5 ($N{=}795$, code interpreter) shows no routing signal without catastrophic failure ($73.5\%$ vs.\ $73.0\%$, $p = 0.81$); Llama-3.1-8B replication ($N{=}220$) confirms death dominance across model families (direction consistency 10/10; \S\ref{sec:cross-model}). Four intervention axes (retry, Reflexion~\citep{reflexion-2023}, $10{\times}$ scaling, action-space restriction) reduce death rates but none closes the gap to deterministic safety, with ${\geq}$12~pp residual gaps (\S\ref{sec:agent-improvement}).
13	An exploratory router (Qwen3 LoRA, 0.6B--4B) yields flat step-level balanced accuracy ($56$--$59\%$); at episode level, only 4B exceeds the always-deterministic baseline (\S\ref{sec:router-diagnostic}).
14	
15	Our contributions: (1)~an \textbf{episode-level counterfactual diagnostic framework} that overcomes per-step oracle degeneracy (97.4\% tie rate), decomposes routing signal via penalty-independent and penalty-dependent metrics, and provides build-vs-buy signal from a ${\sim}$50-episode pilot (Appendix~\ref{app:decision-framework}); (2)~\textbf{78.9\% of non-tie routing labels} in ScienceWorld stem from death asymmetry---replicated across three 7--9B model families (DAF $88$--$90\%$), four interventions, $10{\times}$ scaling to two 70B-class models (DAF $92.4$--$101.0\%$), and cross-environment probes (MATH, ALFWorld)---while a step-level router recovers only task-type classification (\S\ref{sec:death-decomp}--\ref{sec:cross-model}).
16	
17	
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdea5fb4-7917-421c-9d94-b51c7d274f1e",
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "84cf8da1-13a4-4c0b-91a2-41bcee047c40",
  "sourceToolAssistantUUID": "fdea5fb4-7917-421c-9d94-b51c7d274f1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-24T18:45:23.347Z_

Perfect! Now let me check the discussion and conclusion sections for Limitations:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84cf8da1-13a4-4c0b-91a2-41bcee047c40",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtYS4W3fu7VATep3pNw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7116b188-29b4-45c9-96a7-527b16e3fbb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QrztDRbqwgHenbgXhEhi5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10490,
      "cache_read_input_tokens": 73021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10490,
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

_source line 21 · 2026-05-24T18:45:24.192Z_

<details open><summary>🔧 Tool call — Read · `toolu_017mwLA3dJaqtLwWymtaFizb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7116b188-29b4-45c9-96a7-527b16e3fbb1",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtYS4W3fu7VATep3pNw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "953c26c6-e737-4f8a-88fc-be46ae972115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QrztDRbqwgHenbgXhEhi5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10490,
      "cache_read_input_tokens": 73021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10490,
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

_source line 22 · 2026-05-24T18:45:24.209Z_

<details><summary>↩ Tool result · `toolu_017mwLA3dJaqtLwWymtaFizb`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Signal granularity and router failure.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property, but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants converge on near-chance accuracy ($56$--$59\%$). Two a priori unpredictable results: $10{\times}$ scaling to two 70B-class models fails to eliminate death dominance (DAF${}=92.4$--$101.0\%$; Llama-70B exceeds 100\%), and Reflexion yields DAF${}>100\%$; cross-model DR stability ($36$--$49\%$) confirms death vulnerability is a task-environment property rather than a model-capability deficit.
6	
7	\paragraph{Oracle degeneracy and practical implications.}
8	Always-deterministic matches 96.3\% of oracle decisions (\S\ref{sec:baselines}), capping any router's marginal value at 2.89 points. $\Delta_{\text{nd}} = 2.84$ (9.6\% of total gap) shows the advantage concentrates almost entirely in death episodes; ALFWorld (DAF${=}0\%$) confirms the framework diagnoses qualitatively different mechanisms. A ${\sim}$50-episode pilot suffices for build-vs-buy decisions (Appendix~\ref{app:decision-framework}); action-space filtering reduces death rate by 19~pp (Appendix~\ref{app:grounding-ablation}). The decomposition applies when three conditions hold: binary catastrophic failures, asymmetric failure rates, and $P \gg \Delta_\text{nd}$---ScienceWorld satisfies all three; MATH and ALFWorld lack the first.
9	
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "953c26c6-e737-4f8a-88fc-be46ae972115",
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "a8fab69d-a788-4cec-954d-2faba9af04b2",
  "sourceToolAssistantUUID": "953c26c6-e737-4f8a-88fc-be46ae972115",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T18:45:24.391Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MNX5qwPDqi6fbNT8cpp8Dz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8fab69d-a788-4cec-954d-2faba9af04b2",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtYS4W3fu7VATep3pNw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "007b8c17-44b9-4de6-84fc-f7cc5b204996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QrztDRbqwgHenbgXhEhi5i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10490,
      "cache_read_input_tokens": 73021,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10490
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 177,
          "cache_read_input_tokens": 73021,
          "cache_creation_input_tokens": 10490,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10490,
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

_source line 24 · 2026-05-24T18:45:24.398Z_

<details><summary>↩ Tool result · `toolu_01MNX5qwPDqi6fbNT8cpp8Dz`</summary>

```text
1	\section{Conclusion}
2	
3	Our episode-level counterfactual framework reveals that 78.9\% of non-tie routing labels in ScienceWorld stem from death avoidance---replicated across three model families and intensifying under $10{\times}$ scaling (DAF${}=92.4$--$101.0\%$ across two independent 70B-class models). Future work should validate this in additional catastrophic-failure settings and investigate targeted episode collection to resolve the router's inconclusive result.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "007b8c17-44b9-4de6-84fc-f7cc5b204996",
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "f5c90f25-7816-416e-9e88-1c01f260d8f0",
  "sourceToolAssistantUUID": "007b8c17-44b9-4de6-84fc-f7cc5b204996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-24T18:45:25.826Z_

Excellent! Now let me compile the final directory listing for figures:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5c90f25-7816-416e-9e88-1c01f260d8f0",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtYcT5KYbpMXrhUYpsZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "54f3a27f-e9c8-40ac-8706-c82e7d3bee6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WpngfyEGhRR7mqU3kH8eUC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 830,
      "cache_read_input_tokens": 83511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 830,
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

_source line 26 · 2026-05-24T18:45:25.917Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EakXXx7k7dfVi8SKBWrDUH`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/figures/ | grep -E \"\\.(pdf|png)$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54f3a27f-e9c8-40ac-8706-c82e7d3bee6b",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtYcT5KYbpMXrhUYpsZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "18f8d037-5e7d-470e-8431-c14c7f551a23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WpngfyEGhRR7mqU3kH8eUC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 830,
      "cache_read_input_tokens": 83511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 830,
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

_source line 27 · 2026-05-24T18:45:25.997Z_

<details><summary>↩ Tool result · `toolu_01EakXXx7k7dfVi8SKBWrDUH`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu  35K May 18 09:36 death_action_comparison.pdf
-rw-r--r-- 1 ubuntu ubuntu 123K May 18 09:36 death_action_comparison.png
-rw-r--r-- 1 ubuntu ubuntu  36K May 18 09:36 death_action_distribution.pdf
-rw-r--r-- 1 ubuntu ubuntu 141K May 18 09:36 death_action_distribution.png
-rw-r--r-- 1 ubuntu ubuntu  27K May 18 09:36 death_action_timeline.pdf
-rw-r--r-- 1 ubuntu ubuntu 122K May 18 09:36 death_action_timeline.png
-rw-r--r-- 1 ubuntu ubuntu  14K May 19 15:28 dose_response.pdf
-rw-r--r-- 1 ubuntu ubuntu  24K May 24 18:14 fig1_daf_scatter.pdf
-rw-r--r-- 1 ubuntu ubuntu  73K May 24 18:14 fig1_daf_scatter.png
-rw-r--r-- 1 ubuntu ubuntu  28K May 24 18:17 label_decomposition.pdf
-rw-r--r-- 1 ubuntu ubuntu  49K May 24 18:17 label_decomposition.png
-rw-r--r-- 1 ubuntu ubuntu 232K May 24 09:49 pipeline_overview.pdf
-rw-r--r-- 1 ubuntu ubuntu  91K May 24 09:02 pipeline_overview.png
-rw-r--r-- 1 ubuntu ubuntu  38K May 24 09:40 pipeline_overview_old.pdf
-rw-r--r-- 1 ubuntu ubuntu  24K May 21 10:28 signal_reversal.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18f8d037-5e7d-470e-8431-c14c7f551a23",
  "isSidechain": true,
  "promptId": "f3cc2966-e218-4fcd-a430-4f970542dee4",
  "agentId": "ace52815005e1f6e0",
  "type": "user",
  "uuid": "0f08edf2-8413-4c6c-9b4c-14febe5aa05e",
  "sourceToolAssistantUUID": "18f8d037-5e7d-470e-8431-c14c7f551a23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-24T18:45:52.135Z_

Perfect! Now let me create a comprehensive summary report:

## COMPREHENSIVE PAPER STRUCTURE ANALYSIS

### 1. FIGURES IN APPENDIX (Appendix Section, main.tex lines 517-664)

**Appendix Figures (4 figures):**

| # | Label | Caption Summary | File Path | What It Shows |
|---|-------|-----------------|-----------|---------------|
| 1 | `fig:signal-reversal` (line 521) | Cross-environment label distributions across ScienceWorld, ALFWorld, and MATH | `/figures/signal_reversal.pdf` (24 KB) | Comparing routing signal mechanisms: death avoidance in ScienceWorld vs. information asymmetry in ALFWorld vs. no signal in MATH |
| 2 | `fig:death-action-dist` (line 649) | Action distribution in death vs. non-death episodes | `/figures/death_action_distribution.pdf` (36 KB) | Shows `focus on` action is 5.4% in death episodes vs. 3.4% in non-death; `connect` dominates both |
| 3 | `fig:death-timeline` (line 656) | Step-by-step action sequences for 6 representative death episodes | `/figures/death_action_timeline.pdf` (27 KB) | Visualizes the "connect loop → fatal focus" pattern; fatal `focus on` appears in final 1-3 steps |
| 4 | `fig:death-comparison` (line 663) | Non-connect action distribution: internal vs. deterministic in death episodes | `/figures/death_action_comparison.pdf` (35 KB) | Both strategies show ~5% `focus on` rate within death episodes; higher death count reflects more frequent entry into catastrophic states |

---

### 2. LIMITATIONS SECTION (Full Text)

**Location:** main.tex, lines 37-52

The Limitations section contains **five paragraphs** covering:

**Paragraph 1: Environmental scope (lines 39-40)**
- Primary analysis uses ScienceWorld (11 of 30 task types) with Qwen2.5-7B-Instruct backbone
- Death penalty P=-100 amplifies DAF; softer penalties would show lower values
- 19 excluded task types (63%) lack routing signal due to timeouts; higher step budget could surface non-death signal
- Cross-environment validation on MATH and ALFWorld (§3.4) provides preliminary supporting evidence
- Llama-3.1-8B replication confirms death dominance replicates with direction consistency 10/10 but varying magnitude
- 70B-class models (Qwen2.5-72B, Llama-3.1-70B) don't eliminate death dominance (DAF 92.4-101.0%)
- Quantitative results are ScienceWorld-specific; framework's generality is methodological, not empirical

**Paragraph 2: Methodological constraints (lines 42-43)**
- Internal-reasoning baseline uses single-pass ReAct; Reflexion reduces death rate from 42.9% to 31.4%
- More aggressive self-correction or Tree-of-Thought may further reduce internal death rates
- Episode-level labels assign single routing preference to entire episodes (may be suboptimal for individual steps)
- Only 0.3% of 2,040 training steps exhibit strict directional conflict; 60.3% are pre-event neutral
- Issue is granularity mismatch, not directional error
- Training on pure-strategy trajectories introduces distribution shift; grounding ablation reduces death rate from +26.5pp to ~+8pp
- Post-ablation counterfactual decomposition confirms death remains dominant signal source (≥93%)
- Residual gaps >10pp expected under optimistic assumptions

**Paragraph 3: Statistical limitations (lines 45-46)**
- Episodes within same task type not fully independent (share environment dynamics)
- Cluster bootstrap with K=11 task-type clusters yields wider CIs [73.3%, 100.0%]
- K=11 falls below K≥20-50 recommended threshold
- Wild cluster bootstrap (K=11, p<0.001) and 100% directional consistency across 28 death-prone tasks mitigate concern

**Paragraph 4: Pure-strategy upper bound (lines 48-49)**
- Counterfactual analysis compares pure strategies; in mixed routing, router could invoke deterministic on high-risk steps
- DAF=90.4% represents upper bound on death avoidance's contribution
- Actual contribution under mixed strategies may be lower

**Paragraph 5: Diagnostic scope (lines 51-52)**
- Framework is diagnostic rather than prescriptive
- Assumes binary catastrophic failure; graded penalties would require modifying Algorithm 1's death-priority rule
- Extending to prescriptive optimal mixed-strategy routing is natural next step

---

### 3. MAIN TEXT FIGURES (In Experiments and Method sections)

**Main Text Figures (5 figures in experiments.tex + 1 in method.tex):**

| # | Section | Label | Caption | File Path | What It Shows |
|---|---------|-------|---------|-----------|---------------|
| 1 | Method (line 8) | `fig:pipeline` | Counterfactual episode collection and analysis pipeline | `/figures/pipeline_overview.pdf` (232 KB) | Pipeline diagram showing both pure strategies executed independently, producing episode-level labels via Algorithm 1 |
| 2 | Experiments (line 13) | `fig:label-decomposition` | Episode-level label decomposition (N=245) | `/figures/label_decomposition.pdf` (28 KB) | Of 95 non-tie labels: 75 (78.9%) from death asymmetry; 54 sole-signal, 21 co-occurring; all 20 non-death labels from `find-non-living-thing` |
| 3 | Experiments (line 24) | `fig:decomposition` | Per-task death rate differential vs. performance gap (n=11 task types) | `/figures/fig1_daf_scatter.pdf` (24 KB) | Scatter plot showing correlation r=0.97; sole outlier is `find-non-living-thing` with zero deaths |
| 4 | Experiments (line 78) | `fig:dose-response` | Death rate as function of trial count (N) for Retry and Reflexion | `/figures/dose_response.pdf` (14 KB) | Retry flat ~48→43.5%; Reflexion drops steeply to 34% at N=3, stabilizes; horizontal lines show scaling baselines |
| 5 | Experiments (Figure reference before line 62) | (No explicit label given, but referenced in text) | Internal-strategy death rates under agent improvement methods (Table 4) | N/A (Table, not figure) | N/A |

---

### 4. FIGURE FILES IN /figures/ DIRECTORY

**Complete inventory (15 files):**

PDF files (8):
- `pipeline_overview.pdf` (232 KB) - Method section figure
- `pipeline_overview_old.pdf` (38 KB) - Backup
- `label_decomposition.pdf` (28 KB) - Experiments section
- `fig1_daf_scatter.pdf` (24 KB) - Experiments section
- `dose_response.pdf` (14 KB) - Experiments section
- `death_action_distribution.pdf` (36 KB) - Appendix
- `death_action_timeline.pdf` (27 KB) - Appendix
- `death_action_comparison.pdf` (35 KB) - Appendix
- `signal_reversal.pdf` (24 KB) - Appendix

PNG files (7):
- `pipeline_overview.png` (91 KB)
- `label_decomposition.png` (49 KB)
- `fig1_daf_scatter.png` (73 KB)
- `death_action_distribution.png` (141 KB)
- `death_action_timeline.png` (122 KB)
- `death_action_comparison.png` (123 KB)

---

### 5. PAGE COUNT INFORMATION

**Compiled PDF details:**
- Total pages: 25 pages (from PDF image listings: p1-p25)
- Main matter: ~17 pages (introduction through related_work and conclusion)
- Appendix: ~8 pages of supplementary sections (A through U)

**Page limit comments:** None explicit in the tex files. The document uses ACL review format (`\usepackage[review]{acl}`), typical for 8-9 page main conference papers.

---

### 6. SUMMARY STATISTICS

**Figures by location:**
- Main text: 5 figures (1 in Method, 4 in Experiments)
- Appendix: 4 figures (all in failure-mode analysis section)
- Total figures with labels: 9

**Tables by location:**
- Main text: 3 tables (in Experiments)
- Appendix: 23+ tables (supporting all analyses)

**Key metrics reported:**
- N=245 episodes across 11 task types in main analysis
- Death rate differential (Δ_DR) = +26.5 pp (Qwen-7B), +30.0 pp (Llama-8B)
- Death Avoidance Factor (DAF) = 90.4% ± 4.2% (95% CI [81.3%, 99.1%])
- Label fraction = 78.9% (95% CI [70.7%, 87.0%])

All figures shown are included in the compiled PDF available at `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f08edf2-8413-4c6c-9b4c-14febe5aa05e",
  "isSidechain": true,
  "agentId": "ace52815005e1f6e0",
  "requestId": "req_011CbMtYjKpWDtccwtoue81f",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1448c351-521a-4c44-b81d-3064e00d6d68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/director_976fe708",
  "sessionId": "5d044481-75d4-4f8a-b48d-d8d0b80be816",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HtDWbiH5JQnyHCSTikZ7bu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 84341,
      "output_tokens": 2341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 605
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2341,
          "cache_read_input_tokens": 84341,
          "cache_creation_input_tokens": 605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 605,
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
