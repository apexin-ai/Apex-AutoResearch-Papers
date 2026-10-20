# Research conversation: You are helping with a paper distillation task. Fetch and extract detailed information from this arXiv paper: arXiv:2505

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aed1d3e555792ca7c.jsonl`
- **Structured JSON:** [`7e9cfe65e67e345c57a2.json`](../../sessions/7e/7e9cfe65e67e345c57a2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-21T16:37:51.134Z_

You are helping with a paper distillation task. Fetch and extract detailed information from this arXiv paper: arXiv:2505.18486 "Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model"

Use WebFetch to get the full paper from https://arxiv.org/html/2505.18486 

Extract ALL of the following in detail:
1. Full introduction text (every paragraph)
2. All contribution statements
3. Complete experiment section (datasets, baselines, metrics, results with numbers)
4. All figure and table captions
5. Paragraphs referencing figures/tables
6. Limitations / future work section
7. Method details (what is the approach?)
8. Training/implementation details
9. Ablation studies if any
10. The conclusion section

Return the COMPLETE extracted text, not summaries. This is for detailed analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "aed1d3e555792ca7c",
  "type": "user",
  "uuid": "22a69d8a-ec8a-4e20-95cb-facb7ae58352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T16:37:51.139Z_

```json
{
  "parentUuid": "22a69d8a-ec8a-4e20-95cb-facb7ae58352",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "229787fd-1f03-4535-bfa9-fbcee9044a30",
  "timestamp": "2026-05-21T16:37:51.139Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-21T16:37:53.528Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015kA1JuhpGQwbxx15h8eZE3`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "229787fd-1f03-4535-bfa9-fbcee9044a30",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "requestId": "req_011CbG3PidBQu6SpjheogF2g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "547bab5e-b6cb-4180-9982-0f91484c50a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01H2DZGmzNCoJHRedWBHV1Gh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16304,
      "cache_read_input_tokens": 0,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16304
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16304,
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

_source line 4 · 2026-05-21T16:37:53.533Z_

<details><summary>↩ Tool result · `toolu_015kA1JuhpGQwbxx15h8eZE3`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "547bab5e-b6cb-4180-9982-0f91484c50a0",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "aed1d3e555792ca7c",
  "type": "user",
  "uuid": "17442824-e4bd-43cb-a0af-d748b9557b9e",
  "sourceToolAssistantUUID": "547bab5e-b6cb-4180-9982-0f91484c50a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T16:37:55.307Z_

I'll fetch the full paper from arXiv now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17442824-e4bd-43cb-a0af-d748b9557b9e",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "requestId": "req_011CbG3PtPJg2DD6VWDLFdkN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e402d20-ea0e-4142-9599-9b5a6754b2de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0144726kLp5uHT3wWm5beNCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 16304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

_source line 6 · 2026-05-21T16:38:00.727Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011NKTQv6TrHHx9FdkWhbeWt`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.18486",
  "prompt": "Extract ALL of the following in complete, verbatim detail (do not summarize):\n1. Full introduction text - every paragraph word for word\n2. All contribution statements (usually at end of intro)\n3. Complete experiment section - datasets used (names, sizes), baselines compared, metrics reported, all numerical results\n4. ALL figure captions (every figure caption verbatim)\n5. ALL table captions (every table caption verbatim)\n6. All paragraphs in the main text that reference figures or tables\n7. Limitations section and future work section (verbatim)\n8. Method section - complete description of the approach\n9. Training and implementation details\n10. Ablation studies if any\n11. Complete conclusion section (verbatim)\n\nReturn the complete extracted text. Do not summarize. Include section headers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e402d20-ea0e-4142-9599-9b5a6754b2de",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "requestId": "req_011CbG3PtPJg2DD6VWDLFdkN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfc3c888-ec6c-4069-b724-2e72907cffd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0144726kLp5uHT3wWm5beNCL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 16304,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 276,
          "cache_read_input_tokens": 16304,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1432,
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

_source line 7 · 2026-05-21T16:38:00.935Z_

<details><summary>↩ Tool result · reported error · `toolu_011NKTQv6TrHHx9FdkWhbeWt`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfc3c888-ec6c-4069-b724-2e72907cffd0",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "aed1d3e555792ca7c",
  "type": "user",
  "uuid": "5eaef4f0-fdc8-440d-976a-5467236d8e10",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "dfc3c888-ec6c-4069-b724-2e72907cffd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T16:38:04.778Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V4d97wkUZwFkCVWq4ZCBqg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.18486",
  "prompt": "Extract ALL of the following in complete, verbatim detail (do not summarize):\n1. Full introduction text - every paragraph word for word\n2. All contribution statements (usually at end of intro)\n3. Complete experiment section - datasets used (names, sizes), baselines compared, metrics reported, all numerical results\n4. ALL figure captions (every figure caption verbatim)\n5. ALL table captions (every table caption verbatim)\n6. All paragraphs in the main text that reference figures or tables\n7. Limitations section and future work section (verbatim)\n8. Method section - complete description of the approach\n9. Training and implementation details\n10. Ablation studies if any\n11. Complete conclusion section (verbatim)\n\nReturn the complete extracted text. Do not summarize. Include section headers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eaef4f0-fdc8-440d-976a-5467236d8e10",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "requestId": "req_011CbG3QRvN7CrmuBhEgaj24",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fb862bd-7972-48c1-9b43-46ffad2b52ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GNqy7y6WfqoK5ubNKCZtX6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 305,
      "cache_read_input_tokens": 17736,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 305
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 263,
          "cache_read_input_tokens": 17736,
          "cache_creation_input_tokens": 305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 305,
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

_source line 9 · 2026-05-21T16:38:08.590Z_

<details><summary>↩ Tool result · `toolu_01V4d97wkUZwFkCVWq4ZCBqg`</summary>

```text
# Response

I cannot fulfill this request as specified. The webpage content provided contains only the **abstract and metadata** from an arXiv paper listing page—not the full paper itself.

**What's available on this page:**
- Title, authors, submission dates
- Abstract (brief summary)
- Subject classifications
- Citation information
- Links to access the PDF

**What's NOT available:**
The actual paper content you've requested, including:
- Introduction text
- Method sections
- Experiments and results
- Figures and tables
- Conclusions
- Limitations

**To obtain this information, you would need to:**
1. Access the full PDF via the link: `/pdf/2505.18486`
2. Provide that complete paper text for extraction

The metadata page alone cannot supply the detailed experimental results, figure captions, table data, and full sections you're requesting. If you have access to the full paper PDF, please share that content and I can extract the requested information within the 125-character quote limit you've specified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fb862bd-7972-48c1-9b43-46ffad2b52ce",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "aed1d3e555792ca7c",
  "type": "user",
  "uuid": "e0a6afca-ea30-4fd2-87df-ff73bc919333",
  "sourceToolAssistantUUID": "2fb862bd-7972-48c1-9b43-46ffad2b52ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T16:38:11.475Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SfrkxZhcz39Ys6rMxaGzBw`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2505.18486",
  "prompt": "Extract ALL of the following in complete, verbatim detail (do not summarize):\n1. Full introduction text - every paragraph word for word\n2. All contribution statements (usually at end of intro)\n3. Complete experiment section - datasets used (names, sizes), baselines compared, metrics reported, all numerical results\n4. ALL figure captions (every figure caption verbatim)\n5. ALL table captions (every table caption verbatim)\n6. All paragraphs in the main text that reference figures or tables\n7. Limitations section and future work section (verbatim)\n8. Method section - complete description of the approach\n9. Training and implementation details\n10. Ablation studies if any\n11. Complete conclusion section (verbatim)\n\nReturn the complete extracted text. Do not summarize. Include section headers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0a6afca-ea30-4fd2-87df-ff73bc919333",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "requestId": "req_011CbG3Qzb9AzcrqMeMCk45j",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1f13ded-5e90-4311-b027-d25c93c1d6e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DHmZuzRtggNHftYBPouvF1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 498,
      "cache_read_input_tokens": 18041,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 498
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 263,
          "cache_read_input_tokens": 18041,
          "cache_creation_input_tokens": 498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 498,
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

_source line 11 · 2026-05-21T16:38:16.216Z_

<details><summary>↩ Tool result · `toolu_01SfrkxZhcz39Ys6rMxaGzBw`</summary>

```text
I appreciate your request, but I must clarify an important limitation: the content you've provided appears to be a PDF file encoded in binary/compressed format, not readable text. The material shows PDF stream objects with FlateDecode compression and binary data that cannot be meaningfully extracted as plain text without proper PDF parsing tools.

**What I can tell you:**

The document appears to be an academic paper (indicated by the PDF structure with objects, streams, and standard academic formatting markers). However, I cannot extract the specific sections you've requested because:

1. The content is not in plaintext form - it's compressed PDF binary data
2. Proper extraction would require PDF parsing software
3. I cannot reliably identify section boundaries, figure captions, tables, or specific text passages from this encoding

**To properly extract this content, you would need to:**

- Use a PDF-to-text converter tool (like pdftotext, PyPDF2, or similar)
- Open the PDF in a standard reader and copy-paste sections
- Use academic paper extraction services designed for this purpose

I'm happy to help analyze or extract information from the paper **if you can provide it in plaintext format**, but I cannot process the raw PDF binary structure directly.

[Binary content (application/pdf, 708.4KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381491497-bzue2k.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1f13ded-5e90-4311-b027-d25c93c1d6e9",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "aed1d3e555792ca7c",
  "type": "user",
  "uuid": "c3416269-f85f-48d2-b866-38669a18627c",
  "sourceToolAssistantUUID": "d1f13ded-5e90-4311-b027-d25c93c1d6e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-21T16:38:18.416Z_

The PDF was saved locally. Let me read it directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3416269-f85f-48d2-b866-38669a18627c",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "requestId": "req_011CbG3RZBhxzdJmDNy59iU3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d384929-e822-4d87-8c0c-d71d58ddc8ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L2CBty5e37AYKZov7U9aMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 18539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 658,
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

_source line 13 · 2026-05-21T16:38:19.960Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0146x8Ss3pq1Zp3DFyYYRomR`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381491497-bzue2k.pdf /tmp/paper_2505_18486.txt 2>&1 && echo \"DONE\"",
  "description": "Convert PDF to text using pdftotext"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d384929-e822-4d87-8c0c-d71d58ddc8ae",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "requestId": "req_011CbG3RZBhxzdJmDNy59iU3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9495420-c342-4f1d-9c9f-9c6e9a7d00bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L2CBty5e37AYKZov7U9aMC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 18539,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 18539,
          "cache_creation_input_tokens": 658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 658,
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

_source line 14 · 2026-05-21T16:38:20.178Z_

<details><summary>↩ Tool result · `toolu_0146x8Ss3pq1Zp3DFyYYRomR`</summary>

```text
DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9495420-c342-4f1d-9c9f-9c6e9a7d00bc",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "aed1d3e555792ca7c",
  "type": "user",
  "uuid": "d9245166-4c15-4c2a-8085-55f59d70e6ce",
  "sourceToolAssistantUUID": "a9495420-c342-4f1d-9c9f-9c6e9a7d00bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T16:38:22.279Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019mXqLKtgaqV89exW2UBTcu`</summary>

```json
{
  "command": "wc -l /tmp/paper_2505_18486.txt",
  "description": "Check line count of extracted text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9245166-4c15-4c2a-8085-55f59d70e6ce",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "requestId": "req_011CbG3Rr9fbcUNuYSmLKSrP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36c1687d-1127-4047-9667-e4685717057b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CY6maFUgVbDoQFA82uxGA6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 19197,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 229
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 19197,
          "cache_creation_input_tokens": 229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 229,
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

_source line 16 · 2026-05-21T16:38:22.328Z_

<details><summary>↩ Tool result · `toolu_019mXqLKtgaqV89exW2UBTcu`</summary>

```text
2086 /tmp/paper_2505_18486.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36c1687d-1127-4047-9667-e4685717057b",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "aed1d3e555792ca7c",
  "type": "user",
  "uuid": "db2ed80f-8f52-41f5-810c-de40b4e030ab",
  "sourceToolAssistantUUID": "36c1687d-1127-4047-9667-e4685717057b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T16:38:23.885Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KZXskxkJF7e3W33fXawvCy`</summary>

```json
{
  "file_path": "/tmp/paper_2505_18486.txt",
  "limit": 2086
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2ed80f-8f52-41f5-810c-de40b4e030ab",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "requestId": "req_011CbG3S1MJqC49Zmn1aXpDr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46a4889f-ede9-4387-b9a9-80f34d97840e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WqMnvaiU86zpg8q9tU55Ms",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 116,
      "cache_read_input_tokens": 19426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 116,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 18 · 2026-05-21T16:38:24.467Z_

<details><summary>↩ Tool result · `toolu_01KZXskxkJF7e3W33fXawvCy`</summary>

```text
1	Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model
2	Hong Jiao
3	University of Maryland, College Park
4	Dan Song
5	Won-Chan Lee
6	University of Iowa
7	Abstract
8	Large language models (LLMs) have been widely explored for automated scoring in low-stakes
9	assessment to facilitate learning and instruction. Empirical evidence related to which LLM
10	produces the most reliable scores and induces least rater effects needs to be collected before the
11	use of LLMs for automated scoring in practice. This study compared ten LLMs (ChatGPT 3.5,
12	ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini
13	2.0, as well as DeepSeek V3, and DeepSeek R1) with human expert raters in scoring two types
14	of writing tasks. The accuracy of the holistic and analytic scores from LLMs compared with
15	human raters was evaluated in terms of Quadratic Weighted Kappa. Intra-rater consistency
16	across prompts was compared in terms of Cronbach Alpha. Rater effects of LLMs were
17	evaluated and compared with human raters using the Many-Facet Rasch model. The results in
18	general supported the use of ChatGPT 4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet with high
19	scoring accuracy, better rater reliability, and less rater effects.
20	
21	1
22	
23	Introduction
24	Performance assessment tasks, including essays and other types of constructed-response
25	(CR) items are commonly used for assessing high-order thinking skills such as synthesizing
26	information from multiple sources, critical evaluations, and evidence-based reasoning. These
27	assessment formats are commonly employed in formative classroom assessments to facilitate
28	instruction and learning as well as in high-stakes summative assessments for accountability and
29	admission decisions. While the score represents a key form of feedback, the scoring of such
30	assessment tasks is often costly, time-consuming, and error prone due to the subjectivity of
31	human raters.
32	Automated scoring of performance items is an efficient and scientifically validated
33	technology designed to complement and enhance human scoring (Shermis, 2015). For example,
34	automating the scoring of the National Assessment of Educational Progress (NAEP) CR items
35	could yield significant cost saving of 70% for reading and 40% for math (Justice & Palermo,
36	2020). As one of the most successful applications of AI technology in educational assessments,
37	the progress in automated scoring is aligned closely with the advances in machine learning and
38	natural language processing (NLP). Though research on automated scoring started with the
39	pioneering work of Page (1966; 2003), recent advances in AI technology have made
40	breakthrough in automated scoring.
41	Automated scoring can be categorized into two main approaches: feature-based and deep
42	learning-based (Haller et al., 2022), with the latter further classified into neural network, small
43	language model (SLM), and large language model (LLM) based approaches. Feature-based
44	approaches rely on the extracted length, prompt, readability, syntactic, semantic, lexical, and
45	discourse features (Ke & Ng, 2019; Uto et al., 2020) and supervised machine learning models.
46	Deep learning-based approaches use word embeddings (Word2Vec, GloVe) and context
47	embeddings from small language models (SLMs) such as BERT, deBERTa based on transformer
48	(Vaswani et al., 2017) and large language models (LLMs) such as GPT, Claude, and Gemini.
49	Developing feature-based or SLM-based automated scoring systems often requires
50	foundational skills in supervised machine learning, NLP, and deep learning. This dramatically
51	reduces the accessibility of automated scoring to classroom learners, teachers, and assessment
52	developers. However, with the swift emerging of more capable LLMs, automated scoring
53	techniques are becoming increasingly accessible to non-technical users who can fully leverage
54	the LLM technology to revamp their routine scoring practices, with enhanced efficiency and
55	accuracy.
56	With the advances in Generative AI or Chatbots, LLMs have been explored for
57	automated scoring in education assessments. LLMs have demonstrated unprecedented potential
58	in automated scoring of essays and CR items in educational assessments (Latif & Zhai, 2024;
59	Lee et al., 2024; Yancey et al., 2023; Yang et al., 2025). In low-stakes assessment programs,
60	three commonly used models are ChatGPT by OpenAI, Claude by Anthropic, and Google
61	Gemini. Recent studies have explored the use of GPT models, such as GPT 3.5 (Bui & Barrot,
62	2024; Mizumoto & Eguchi, 2023; Parker et al., 2023; Wijekumar et al., 2024) and GPT 4
63	(Kortemeyer, 2024) in automated scoring. Furthermore, several studies have compared the
64	2
65	
66	performance of GPT 3.5 and GPT 4 (Kim & Jo, 2024; Tate et al., 2024) as well as GPT and
67	Llama3 (Kundu & Barbosa, 2024). Pack et al. (2024) compared PaLM 2, Claude 2, and GPT 3.5
68	and GPT 4, concluding that GPT 4 outperformed the others. Almost all studies on using LLMs
69	for automated scoring purely focused on scoring accuracy, little is known about the potential
70	rater effects of these LLM scoring engines.
71	Rater effects (Myford & Wolfe, 2003, 2004; Saal, Downey, & Lahey, 1980) refer to
72	different types of inconsistencies in ratings when human raters assign scores to test-takers’
73	constructed responses to performance tasks such as essays or CR items in educational
74	assessments. Rater effects may occur due to raters’ personal backgrounds, preferences,
75	inaccurate interpretations of the scoring rubrics, inappropriate conceptualization of the target
76	test-takers’ population, and their idiosyncratic traits that may impact their accuracy and
77	consistency in assigning scores to assessment items. Rater effects can be classified into different
78	categories. Some common rater effects include rater severity/leniency and centrality. When a
79	rater assigns scores to students’ responses to a performance task consistently lower than other
80	raters, this rater effect is noted as rater severity. When rater severity is present, students’ true
81	scores may be underestimated if such rater effect is ignored. On the other hand, when a rater
82	assigns scores to students’ responses consistently higher than other raters, this rater effect is
83	noted as rater leniency. When rater leniency is present, students’ true scores may be
84	overestimated if such rater effect is not accounted for. Further, some raters may consistently
85	assign scores in the middle of the score scale and not assign high scores or low scores regardless
86	of the ability levels. This central tendency or centrality effect will introduce score errors for
87	students whose true scores lie at the two ends of the score scale. Such rater effects are as severe
88	as score accuracy as they may compromise the fairness, reliability, and validity of the assigned
89	scores. Though in operational rating sessions, different strategies would be implemented to
90	minimize rater effects such as standardized rubrics, comprehensive rater training and calibration,
91	in-session and post-session quality control of ratings, or assigning multiple raters to each rating
92	tasks, rater effects need to be tracked as a source of validity evidence.
93	Each LLM has its own strengths and features that may cater to different scoring needs
94	and applications. Like human raters, AI raters may bear different degrees of rater effects. Thus, it
95	is worthwhile to compare the ratings from different scoring engines and understand the potential
96	AI rater effects of each LLM. Thus, this study aims to investigate the AI rater effects in addition
97	to rating accuracy and consistency compared with human raters of essay scoring. The AI raters
98	investigated in this study include ten commonly used LLMs from GPT, Gemini, and Claude
99	families and some recent LLMs such as DeepSeek. The research questions for the study include:
100	1. How accurate are LLM raters compared with human raters?
101	2. How consistent or reliable are LLM raters compared with human raters?
102	3. What are the LLM rater effects compared with human raters?
103	Methods
104	This study conducts a series of psychometric analyses to investigate the AI raters’ scoring
105	accuracy and consistency, as well as uses the Many-Facet Rasch measurement model (Linacre,
106	
107	3
108	
109	1989, 1994, 2024; Wright & Masters, 1982; Wright & Stone, 1979) to investigate and compare
110	rater effects between AI raters and human raters in a large-scale writing assessment.
111	Data
112	A dataset consists of 30 student essays on two types of writing tasks. Each essay was
113	scored by two human raters and ten AI raters, including ChatGPT 3.5, ChatGPT 4, ChatGPT 4o,
114	OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek
115	V3 and DeepSeek R1. The 30 U.S. college students, enrolled in Mandarin Chinese language
116	courses, included 18 third-year and 12 fourth-year students from a range of majors such as
117	business, humanities, STEM, and diplomacy. Data collection took place over two consecutive
118	days using constructed-response writing prompts from the 2021 and 2022 AP Chinese exams
119	developed by the College Board. On the first day, students completed the 2021 prompts, which
120	included one story narration (SN1) task and one email response (ER1) task. On the second day,
121	they responded to the 2022 prompts, which featured the same two task types, each labeled as
122	SN2, and ER2. Two certified human raters of the AP Chinese exam evaluated the writing
123	samples using the College Board’s scoring rubrics for both holistic and analytic scoring for three
124	trait scores assessing Task Completion, Delivery, and Language Use. Each student response
125	received both holistic and analytic trait/domain-specific scores ranging from 0 to 6 (Song &
126	Tang, 2025).
127	LLMs Trained for Automated Scoring
128	In alignment with the development of LLMs, ChatGPT 3.5 was first used to score all 120
129	essays and other AI engines were sequentially explored when new versions or new engines were
130	released. Data collection took approximately one and a half years. This study incorporated ten AI
131	raters: ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5,
132	Gemini 2.0, Gemini Advanced 1.5 Pro, DeepSeek V3, and DeepSeek R1. These LLMs are
133	selected based on their popularity and demonstrated expertise in processing text data and
134	reasoning capabilities. ChatGPT 3.5 is for general-purpose tasks, casual writing, and basic
135	coding. ChatGPT 4 is better at technical problem-solving and creative content. ChatGPT 4
136	generally outperforms ChatGPT 3.5 in language understanding, with ChatGPT 4 Turbo offering
137	enhanced context handling. ChatGPT 4o excels at conversations. OpenAI o1 specializes in
138	advanced STEM applications and debugging. Claude 3.5 Sonnet is competitive, often cited in
139	safety-focused evaluations, technical coding, and natural-sounding content. Gemini 1.5 and 1.5
140	Pro are good at long-context tasks. Gemini 2.0 was selected to reflect the latest advancements in
141	Google’s LLMs, which feature enhanced language understanding and improved reasoning for
142	research, education, and multimedia analysis. DeepSeek V3 and DeepSeek R1 are two distinct
143	models developed by DeepSeek, each designed for different purposes and with unique
144	capabilities. DeepSeek V3 uses the Mixture-of-Experts model, optimized for general-purpose
145	tasks, including natural language understanding, text generation, and conversational AI.
146	DeepSeek R1 excels in reasoning. It is specifically tailored for tasks that require deep reasoning,
147	complex problem-solving, and advanced analytical capabilities. DeepSeek was included due to
148	its rising prominence as an open-source LLM with demonstrated strengths in structured
149	reasoning, grammatical precision, and technical problem-solving. Given its strong performance
150	in formal writing tasks and its potential as a cost-effective alternative to proprietary models,
151	4
152	
153	incorporating DeepSeek into our analysis allows for a more comprehensive comparison of AI
154	raters’ capabilities across diverse linguistic and evaluative contexts (Gao et al., 2025).
155	Before scoring, human rater R1, a certified AP Chinese Language and Culture Exam
156	rater, trained 10 AI engines (ChatGPT 3.5, ChatGPT 4.0, ChatGPT 4o, Gemini 1.5, Claude 3.5
157	Sonnet, OpenAI O1, Gemini 2.0, Gemini Advanced 1.5 Pro, DeepSeek V3, and DeepSeek R1)
158	using AI training protocols designed for evaluating student samples (see Appendix A for an
159	example protocol). As Lee et al. (2024) emphasized, human expert ratings are essential for
160	generating benchmark data that align AI scoring with educational standards. To ensure valid AI
161	rater performance, human rater R1 not only provided training examples drawn from the College
162	Board website and previously scored samples but also offered guidance on applying a holistic
163	scoring approach. AI raters were instructed to prioritize three traits: Task Completion, followed
164	by Delivery and Language Use, in line with official rubrics. In total, 2 human raters and 10 AI
165	raters scored 120 essays across four writing tasks.
166	Analysis
167	Using the analytic and holistic scores for the essays, this study investigates scoring
168	accuracy, reliability, and rater effects. Quadratic Weighted Kappa (QWK; Cohen, 1960; 1968)
169	was computed to evaluate the scoring accuracy of AI raters against the gold standards of human
170	ratings. QWK was computed for each AI against each human rater. Further, AI raters’ QWK
171	were compared with the QWK measures from two human raters which were used as the baseline
172	for comparison. Multiple ensemble models were explored by removing the worst performing
173	LLMs from the ensemble. The first ensemble model took the average of the scores assigned by
174	each of the studied 10 AI raters and labeled as AI11 model. Another ensemble model, AI12, was
175	built upon AI11 model by removing model AI7, Gemini 2.0. Ensemble model, AI13, was built
176	upon AI12 model by further removing model AI9, Gemini 1.5 Pro. Ensemble model, AI14, was
177	built upon AI13 model by further removing model AI6, OpenAI o1. Ensemble model, AI15, was
178	built upon AI14 model by further removing model AI8, DeepSeek V3. Ensemble model, AI16,
179	was built upon AI15 model by further removing models AI2 and AI4, ChatGPT 4.0 and Gemini
180	1.5. In addition, Cronbach Alpha was computed for each AI and human ratings across the three
181	trait scores and holistic scores as a measure of intra-rater consistency.
182	Furthermore, the rater effects for both human and AI raters were examined using the
183	Many FACET Rasch model (Linacre, 1989; 1994; 2024). The FACET model for the rating scale
184	model (Andrich, 1978) is given in equation 1.
185	ln �
186	
187	𝑃𝑃𝑗𝑗𝑗𝑗(𝑥𝑥=𝑘𝑘)
188	
189	𝑃𝑃𝑗𝑗𝑗𝑗(𝑥𝑥=𝑘𝑘−1)
190	
191	� = 𝜃𝜃𝑗𝑗 − 𝜏𝜏𝑖𝑖 − 𝛿𝛿𝑛𝑛 −𝛽𝛽𝑘𝑘 .
192	
193	(1)
194	
195	where 𝜃𝜃𝑗𝑗 is student j’s latent ability estimate, 𝜏𝜏𝑖𝑖 is rater i’s rater effect estimate, 𝛿𝛿𝑛𝑛 is essay n’s
196	
197	difficulty level, 𝛽𝛽𝑘𝑘 is the threshold parameter for score category k, where the probability for a
198	rating in category k is equal to the probability for a rating in category k-1. Our study uses the
199	rating scale version of the FACET model (Eckes, 2015; Myford & Wolfe, 2003, 2004), assuming
200	the threshold parameters are the same across all items. A partial credit model version can be
201	explored by assuming that each item has its own threshold parameters. The facets investigated in
202	5
203	
204	this study include students (30), essays (4: SN1, ER1, SN2, ER2), raters including two human
205	raters (R1, R2) and ten LLM-based AI raters (A1 - ChatGPT 3.5, A2 - ChatGPT 4, A3 ChatGPT 4o, A4 - Gemini 1.5, A5 - Claude 3.5 Sonnet, A6 - OpenAI o1, A7 - Gemini 2.0, A8 DeepSeek V3, A9 - Gemini 1.5 Pro, A10 - DeepSeek R1).
206	Rater effects such as the leniency or severity were quantified by the rater parameter in the
207	FACET Rasch model. The Wright map were used to illustrate the relative difficulty of essay
208	traits, rater effects, and student ability on the common scale. Two fit indexes were examined
209	including the infit and outfit mean square. Infit mean square indicates the consistency a rater uses
210	the rating scale across students and criteria while outfit mean squares quantifies the outlier score
211	patterns. The expected values of the infit and outfit mean squares are 1. Values smaller than 1
212	show less variation than expected in assigned scores while values larger than 1 show more
213	variation than expected in assigned scores. Values ranging from 0.5 to 1.5 (Linacre, 2003; Eckes,
214	2009) usually indicates good fit. Usually values smaller than 0.5 indicates overfitting and raters
215	do not discriminate high performing and low performing essays while values larger than 1.5 may
216	distort the measurement. Overfitting suggests a central tendency (Engelhard, 2002; Myford &
217	Wolfe, 2004). Researchers also suggested more stringent criteria using 0.7 and 1.3 as the cut
218	values (Bond & Fox, 2007; Bond et al., 2021; McNamara, 1996; Muller, 2020; Wright &
219	Linacre, 1994). For high-stakes decision making, Myford and Wolfe (2003) even suggested that
220	more stringent cut values like 0.8 and 1.2 might be set. This study follows the stringent criteria of
221	0.7 and 1.3.
222	Results
223	Scoring Accuracy
224	The scoring accuracy of the studied AI raters was evaluated against each human rater in
225	terms of QWK. Table 1 summarizes the holistic score accuracy in terms of QWK of each AI
226	rater against each human rater. Two human raters’ QWK was used as the baseline for
227	comparison. The red-colored numbers indicate the highest QWK against each human rater while
228	the blue-colored numbers indicate the second highest QWK. In general, the two human raters’
229	QWK on essay ER2 met the criterion suggested by Williamson, Xi, and Breyer (2012); that is,
230	QWK should be equal to or larger than a cut score of 0.7. For SN1, ChatGPT 4o yielded the
231	highest QWK with rater 2 while Claude 3.5 yielded the highest QWK with rater 1. For SN2,
232	Gemini 1.5 Pro yielded the highest QWK with both human raters. For ER 1, ChatGPT 4o yielded
233	the highest QWK with rater 1 while Claude 3.5 yielded the highest QWK with rater 2. For ER2,
234	ChatGPT 4o yielded the highest QWK with both human raters. Only one ensemble model by
235	removing Gemini 2.0 yielded higher QWK for SN2 and ER1 with rater R1 only. In general, one
236	of the AI rater achieved higher QWK with one human rater than human-human QWK on every
237	item.
238	
239	6
240	
241	Table 1
242	Holistic Scoring Accuracy (QWK) for AI Raters against Each Human Rater
243	Essay
244	SN1
245	SN2
246	ER1
247	Rater
248	R1
249	R2
250	R1
251	R2
252	R1
253	R2
254	R1/R2
255	0.683
256	0.565
257	0.684
258	A1 – ChatGPT 3.5
259	0.549
260	0.409
261	0.610
262	0.538
263	0.442
264	0.516
265	A2 – ChatGPT 4
266	0.392
267	0.350
268	0.440
269	0.394
270	0.558
271	0.459
272	A3 – ChatGPT 4o
273	0.626
274	0.620
275	0.526
276	0.393
277	0.741
278	0.475
279	A4 - Gemini 1.5
280	0.333
281	0.181
282	0.388
283	0.276
284	0.610
285	0.558
286	A5 - Claude 3.5
287	0.708
288	0.576
289	0.657
290	0.570
291	0.672
292	0.726
293	A6 - OpenAI o1
294	0.422
295	0.302
296	0.557
297	0.369
298	0.543
299	0.304
300	A7 – Gemini 2.0
301	0.201
302	0.131
303	0.319
304	0.199
305	0.289
306	0.143
307	A8 – DeepSeek V3
308	0.378
309	0.233
310	0.610
311	0.439
312	0.619
313	0.448
314	A9 - Gemini 1.5 pro
315	0.267
316	0.169
317	0.698
318	0.576
319	0.631
320	0.640
321	A10 - DeepSeek R1
322	0.579
323	0.522
324	0.417
325	0.293
326	0.453
327	0.368
328	A11=Ensemble
329	0.606
330	0.426
331	0.605
332	0.476
333	0.776
334	0.614
335	A12=A11-A7
336	0.630
337	0.474
338	0.720
339	0.535
340	0.783
341	0.671
342	A13=A12-A9
343	0.689
344	0.502
345	0.630
346	0.516
347	0.751
348	0.669
349	A14=A13-A6
350	0.692
351	0.551
352	0.693
353	0.474
354	0.733
355	0.623
356	A15= A14-A8
357	0.665
358	0.513
359	0.630
360	0.516
361	0.681
362	0.685
363	A16= A15-A2-A4
364	0.688
365	0.588
366	0.675
367	0.563
368	0.647
369	0.675
370	
371	R1
372	
373	ER2
374	
375	R2
376	
377	0.874
378	0.632
379	0.560
380	0.827
381	0.834
382	0.865
383	0.898
384	0.435
385	0.463
386	0.804
387	0.896
388	0.656
389	0.584
390	0.716
391	0.619
392	0.664
393	0.667
394	0.590
395	0.537
396	0.727
397	0.703
398	0.779
399	0.745
400	0.805
401	0.764
402	0.767
403	0.753
404	0.837
405	0.809
406	0.815
407	0.790
408	0.812
409	0.790
410	
411	Table 2
412	Analytic (Task Completion) Scoring Accuracy (QWK) for AI Raters against Each Human Rater
413	Essay
414	SN1
415	SN2
416	ER1
417	ER2
418	Rater
419	R1
420	R2
421	R1
422	R2
423	R1
424	R2
425	R1
426	R2
427	R1/R2
428	0.715
429	0.808
430	0.776
431	0.915
432	A1 – ChatGPT 3.5
433	0.523
434	0.577
435	0.673
436	0.533
437	0.543
438	0.514
439	0.624
440	0.674
441	A2 – ChatGPT 4
442	0.305
443	0.422
444	0.600
445	0.451
446	0.512
447	0.525
448	0.832
449	0.825
450	A3 – ChatGPT 4o
451	0.593
452	0.645
453	0.685
454	0.551
455	0.607
456	0.716
457	0.893
458	0.892
459	A4 - Gemini 1.5
460	0.171
461	0.223
462	0.427
463	0.319
464	0.635
465	0.654
466	0.569
467	0.587
468	A5 - Claude 3.5
469	0.574
470	0.634
471	0.639
472	0.575
473	0.653
474	0.757
475	0.754
476	0.814
477	A6 - OpenAI o1
478	0.258
479	0.307
480	0.568
481	0.427
482	0.385
483	0.475
484	0.569
485	0.599
486	A7 – Gemini 2.0
487	0.341
488	0.226
489	0.444
490	0.407
491	0.287
492	0.328
493	0.631
494	0.717
495	A8 – DeepSeek V3
496	0.380
497	0.251
498	0.525
499	0.372
500	0.580
501	0.580
502	0.651
503	0.650
504	A9 - Gemini 1.5 pro
505	0.344
506	0.121
507	0.492
508	0.456
509	0.696
510	0.729
511	0.621
512	0.644
513	A10 - DeepSeek R1
514	0.324
515	0.477
516	0.459
517	0.387
518	0.576
519	0.620
520	0.722
521	0.786
522	A11=Ensemble
523	0.460
524	0.474
525	0.698
526	0.615
527	0.734
528	0.815
529	0.725
530	0.785
531	A12=A11-A7
532	0.490
533	0.521
534	0.756
535	0.683
536	0.702
537	0.782
538	0.730
539	0.791
540	A13=A12-A9
541	0.469
542	0.573
543	0.746
544	0.632
545	0.702
546	0.782
547	0.752
548	0.773
549	A14=A13-A6
550	0.533
551	0.671
552	0.756
553	0.683
554	0.695
555	0.748
556	0.765
557	0.788
558	A15= A14-A8
559	0.465
560	0.562
561	0.730
562	0.585
563	0.755
564	0.786
565	0.785
566	0.813
567	A16= A15-A2-A4
568	0.481
569	0.699
570	0.690
571	0.566
572	0.676
573	0.767
574	0.735
575	0.819
576	
577	7
578	
579	Tables 2 to 4 summarize the analytic score accuracy in terms of QWK of each AI rater
580	against each human rater on each trait: Task Completion, Delivery, and Language Use
581	respectively. For analytic scores on Task Completion (Table 2), the two human rater had higher
582	consistency compared with the holistic scoring, with QWK all above 0.7. For SN1, ChatGPT 4o
583	yielded the highest QWK with both human raters on SN1 and ER2 as well as on SN2 with R1.
584	Claude 3.5 yielded the highest QWK with R2 on both SN2 and ER1. For ER1, Gemini 1.5 Pro
585	yielded the highest QWK with R1. Multiple ensemble models improved scoring accuracy over
586	the standalone LLM for SN1, SN2, and ER1. Human-human QWK was consistently higher than
587	AI-human QWK on each of the analytic scores.
588	For analytic scores on Delivery (Table 3), the two human rater yielded QWK above 0.7
589	on ER essays only. ChatGPT 4o yielded the highest QWK with both human raters on ER2.
590	Claude 3.5 yielded the highest QWK with each of the two raters on both SN1 and ER1. For SN2,
591	Gemini 1.5 Pro yielded the highest QWK with both human raters. Only two ensemble models
592	improved scoring accuracy over the standalone LLMS for SN1 and ER1. Unlike analytic scores
593	for Task Completion, AI-human QWK was consistently higher than human-human QWK on SN
594	tasks and ER1 task except ER2.
595	For analytic scores on Language Use (Table 4), the two human rater yielded QWK above
596	0.7 on all tasks except SN2. ChatGPT 4.0 and 4o yielded the highest QWK with R1 and R2
597	respectively on ER2. Gemini 1.5 yielded the highest QWK with both raters on ER1. Claude 3.5
598	yielded the highest QWK with both raters on SN1. For SN2, Gemini 1.5 Pro yielded the highest
599	QWK with both human raters. Only two ensemble models improved scoring accuracy over the
600	standalone LLMS for ER1. AI-human QWK was higher than human-human QWK only on SN2.
601	Table 3
602	Analytic (Delivery) Scoring Accuracy (QWK) for AI Raters against Each Human Rater
603	Essay
604	SN1
605	SN2
606	ER1
607	ER2
608	Rater
609	R1
610	R2
611	R1
612	R2
613	R1
614	R2
615	R1
616	R2
617	R1/R2
618	0.685
619	0.588
620	0.763
621	0.950
622	A1 – ChatGPT 3.5
623	0.552
624	0.478
625	0.470
626	0.381
627	0.486
628	0.499
629	0.655
630	0.672
631	A2 – ChatGPT 4
632	0.438
633	0.405
634	0.508
635	0.437
636	0.420
637	0.422
638	0.791
639	0.766
640	A3 – ChatGPT 4o
641	0.607
642	0.552
643	0.534
644	0.442
645	0.537
646	0.460
647	0.907
648	0.890
649	A4 - Gemini 1.5
650	0.166
651	0.187
652	0.489
653	0.282
654	0.614
655	0.544
656	0.362
657	0.368
658	A5 - Claude 3.5
659	0.698
660	0.599
661	0.660
662	0.614
663	0.652
664	0.781
665	0.746
666	0.803
667	A6 - OpenAI o1
668	0.265
669	0.284
670	0.480
671	0.342
672	0.521
673	0.344
674	0.593
675	0.599
676	A7 – Gemini 2.0
677	0.174
678	0.117
679	0.219
680	0.173
681	0.237
682	0.197
683	0.468
684	0.500
685	A8 – DeepSeek V3
686	0.346
687	0.286
688	0.424
689	0.436
690	0.619
691	0.468
692	0.544
693	0.597
694	A9 - Gemini 1.5 pro
695	0.361
696	0.221
697	0.681
698	0.631
699	0.497
700	0.463
701	0.731
702	0.718
703	A10 - DeepSeek R1
704	0.532
705	0.522
706	0.194
707	0.244
708	0.526
709	0.471
710	0.577
711	0.632
712	A11=Ensemble
713	0.541
714	0.417
715	0.545
716	0.444
717	0.667
718	0.596
719	0.670
720	0.723
721	A12=A11-A7
722	0.548
723	0.438
724	0.622
725	0.499
726	0.720
727	0.597
728	0.692
729	0.745
730	A13=A12-A9
731	0.593
732	0.486
733	0.571
734	0.526
735	0.744
736	0.588
737	0.700
738	0.756
739	A14=A13-A6
740	0.609
741	0.561
742	0.570
743	0.526
744	0.695
745	0.647
746	0.739
747	0.802
748	A15= A14-A8
749	0.594
750	0.527
751	0.574
752	0.508
753	0.721
754	0.712
755	0.768
756	0.784
757	A16= A15-A2-A4
758	0.689
759	0.650
760	0.541
761	0.449
762	0.731
763	0.684
764	0.789
765	0.828
766	8
767	
768	Table 4
769	Analytic (Language Use) Scoring Accuracy (QWK) for AI Raters against Each Human Rater
770	Essay
771	SN1
772	SN2
773	ER1
774	ER2
775	Rater
776	R1
777	R2
778	R1
779	R2
780	R1
781	R2
782	R1
783	R2
784	R1/R2
785	0.832
786	0.488
787	0.783
788	0.939
789	A1 – ChatGPT 3.5
790	0.462
791	0.453
792	0.503
793	0.459
794	0.420
795	0.500
796	0.560
797	0.603
798	A2 – ChatGPT 4
799	0.409
800	0.433
801	0.424
802	0.337
803	0.446
804	0.422
805	0.852
806	0.829
807	A3 – ChatGPT 4o
808	0.366
809	0.348
810	0.275
811	0.213
812	0.376
813	0.375
814	0.705
815	0.846
816	A4 - Gemini 1.5
817	0.235
818	0.246
819	0.496
820	0.293
821	0.695
822	0.677
823	0.380
824	0.416
825	A5 - Claude 3.5
826	0.667
827	0.686
828	0.585
829	0.596
830	0.583
831	0.594
832	0.715
833	0.744
834	A6 - OpenAI o1
835	0.236
836	0.283
837	0.451
838	0.397
839	0.341
840	0.252
841	0.553
842	0.581
843	A7 – Gemini 2.0
844	0.140
845	0.124
846	0.017
847	0.104
848	0.221
849	0.139
850	0.495
851	0.528
852	A8 – DeepSeek V3
853	0.227
854	0.074
855	0.265
856	0.246
857	0.368
858	0.417
859	0.553
860	0.581
861	A9 - Gemini 1.5 pro
862	0.447
863	0.304
864	0.626
865	0.677
866	0.599
867	0.622
868	0.495
869	0.528
870	A10 - DeepSeek R1
871	0.432
872	0.382
873	0.216
874	0.246
875	0.455
876	0.459
877	0.665
878	0.743
879	A11=Ensemble
880	0.460
881	0.382
882	0.429
883	0.417
884	0.644
885	0.558
886	0.618
887	0.685
888	A12=A11-A7
889	0.460
890	0.382
891	0.560
892	0.455
893	0.672
894	0.709
895	0.652
896	0.716
897	A13=A12-A9
898	0.432
899	0.364
900	0.509
901	0.397
902	0.690
903	0.602
904	0.688
905	0.761
906	A14=A13-A6
907	0.462
908	0.389
909	0.536
910	0.421
911	0.594
912	0.641
913	0.701
914	0.773
915	A15= A14-A8
916	0.492
917	0.443
918	0.551
919	0.413
920	0.729
921	0.748
922	0.685
923	0.741
924	A16= A15-A2-A4
925	0.618
926	0.598
927	0.497
928	0.416
929	0.670
930	0.659
931	0.730
932	0.783
933	For scoring accuracy, no AI rater turned out to be always the best performer across all
934	tasks. In general, ChatGPT 4o, Claude 3.5, and Gemini 1.5 Pro yielded the highest performing
935	AI raters depending on the scoring tasks, holistic or analytic, as well as the specific trait scores.
936	Ensemble models were able to occasionally improve the scoring accuracy for a specific essay
937	compared with the standalone LLMs.
938	Intra-Rater Consistency
939	This study further examined the intra-rater consistency using the Cronbach Alpha as
940	reported in Table 5. The number of items used for computing intra-rater consistency is 4 items
941	for the holistic scores and analytic scores for each trait respectively, 12 items for analytic scores
942	across all traits, and 6 items for analytic scores for each type of essays: SN and ER. The intrarater consistency was higher when the number of items included for the analysis was higher.
943	Again, the top performing AI raters, either ChatGPT 4o or Claude 3.5, still yielded the highest
944	intra-rater consistency across different tasks, yielding slightly lower values on Language Use
945	trait. The intra-rater consistency for human rater R2 was consistently higher than that for human
946	rater R1. The intra-rater consistency for the best performing AI raters was about the same or
947	higher than R2 except for analytic scores of Language Use and ER essay.
948	
949	9
950	
951	Table 5
952	Intra-Rater Consistency
953	# of Items
954	R1
955	R2
956	A1 – ChatGPT 3.5
957	A2 – ChatGPT 4
958	A3 – ChatGPT 4o
959	A4 - Gemini 1.5
960	A5 - Claude 3.5
961	A6 - OpenAI o1
962	A7 – Gemini 2.0
963	A8 – DeepSeek V3
964	A9 - Gemini 1.5 pro
965	A10 - DeepSeek R1
966	
967	Trait-Task
968	TraitHolistic Completion Delivery
969	4
970	4
971	4
972	0.71
973	0.73
974	0.67
975	0.81
976	0.81
977	0.78
978	0.71
979	0.66
980	0.73
981	0.66
982	0.64
983	0.64
984	0.81
985	0.80
986	0.79
987	0.46
988	0.60
989	0.63
990	0.80
991	0.82
992	0.78
993	0.67
994	0.62
995	0.50
996	0.35
997	0.26
998	0.28
999	0.62
1000	0.69
1001	0.51
1002	0.61
1003	0.61
1004	0.60
1005	0.68
1006	0.72
1007	0.73
1008	
1009	TraitLanguage Use
1010	4
1011	0.58
1012	0.77
1013	0.72
1014	0.58
1015	0.58
1016	0.58
1017	0.74
1018	0.56
1019	0.30
1020	0.58
1021	0.41
1022	0.67
1023	
1024	Analytic
1025	12
1026	0.90
1027	0.94
1028	0.92
1029	0.89
1030	0.91
1031	0.88
1032	0.94
1033	0.87
1034	0.72
1035	0.87
1036	0.85
1037	0.91
1038	
1039	SN
1040	6
1041	0.89
1042	0.95
1043	0.91
1044	0.92
1045	0.90
1046	0.90
1047	0.95
1048	0.85
1049	0.67
1050	0.92
1051	0.86
1052	0.89
1053	
1054	ER
1055	6
1056	0.91
1057	0.93
1058	0.89
1059	0.79
1060	0.90
1061	0.86
1062	0.89
1063	0.79
1064	0.80
1065	0.82
1066	0.81
1067	0.89
1068	
1069	AI Rater Effects
1070	The mean scores of the holistic and analytic scores assigned by each rater are
1071	summarized in Tables 6. The standard deviation of the scores assigned are presented in Table
1072	B.1 in Appendix B. The red colored numbers indicate the AI rater who assigned scores with the
1073	highest mean score among all AI raters or a human rater with higher scores compared with the
1074	other human rater while the blue-colored numbers indicate the lowest mean scores assigned
1075	among AI raters. To some degree, this pattern reflects the patterns observed in the rater effects of
1076	severity vs leniency. Further, Table 7 presents the standard deviation of the scores assigned by
1077	each rater, which may help better understand the rater centrality effect. In general, human rater
1078	R2 assigned higher mean scores across all rating tasks compared with R1. Geimini 2.0 assigned
1079	the lowest means cores on majority of the rating tasks while ChatGPT 3.5 and ChatGPT 4
1080	produced the highest mean scores on majority of the rating tasks. The pattern in standard
1081	deviation of the scores is not clear.
1082	The Wright Maps from the FACET models are presented in Figures 1 and 2 for the
1083	holistic and the analytic scores across three traits. Figures 3 to 5 present the Wright Map for the
1084	analytic scores for each trait. These maps demonstrate the relative locations of examinees,
1085	essays, and raters’ parameters on the latent trait scale ranging from -3 to +3. For holistic scoring
1086	as shown in Figure 1, SN2 was the most difficult essay, while ER2 was the easiest essay. Gemini
1087	2.0 was the most stringent rater, which is consistent with the lowest mean scores assigned while
1088	R2 and ChatGPT 3.5 were more lenient raters as they assigned the highest or higher mean scores
1089	as presented in Table 6.
1090	Table 7 presents the rater parameter estimates and fit measures of each rater to the
1091	FACET model. Following equation 1, when the rater parameter is 0, the rater has no effect on
1092	scoring. A positive rater parameter means the likelihood of getting a score will be decreased due
1093	to a severe rater effect while a negative rater parameter means the likelihood of getting a score
1094	10
1095	
1096	will be increased due to a lenient rater effect. Human rater R2 was more lenient than R1, with a
1097	logit value difference of about 0.6 which can be considered as non-negligible difference if we
1098	follow the cut value of 0.3 logit (Miller, Rotou, & Twing, 2004) for parameter drift evaluation.
1099	Table 6
1100	Mean Holistic and Analytic Scores Assigned by Each Rater
1101	Scores
1102	R1 R2 A1 A2 A3 A4 A5
1103	SN1-Holistic 3.70 4.10 3.53 3.03 3.73 2.83 3.80
1104	ER1-Holistic 3.30 3.83 4.30 3.43 2.93 3.43 3.50
1105	SN2-Holistic 3.23 3.70 3.50 2.97 2.70 2.90 3.10
1106	ER2-Holistic 3.73 4.07 3.13 3.93 3.77 3.60 3.87
1107	Task_SN1
1108	4.20 4.03 3.70 3.30 4.23 2.83 3.80
1109	Task_SN2
1110	3.60 3.73 3.53 3.33 3.47 2.90 3.03
1111	Task_ER1
1112	3.93 3.70 4.17 3.87 3.30 3.40 3.57
1113	Task_ER2
1114	4.03 3.87 3.27 3.93 3.87 3.57 3.60
1115	Delivery_SN1 3.77 4.03 3.43 3.03 3.50 2.67 3.80
1116	Delivery_SN2 3.23 3.63 3.43 3.10 2.73 2.90 3.07
1117	Delivery_ER1 3.53 3.73 4.30 3.87 2.97 3.57 3.97
1118	Delivery_ER2 3.97 3.87 3.20 4.03 3.87 3.63 3.67
1119	LUSE_SN1
1120	3.83 3.97 3.47 3.03 2.97 2.77 3.80
1121	LUSE_SN2
1122	3.30 3.53 3.43 2.87 2.40 2.90 3.03
1123	LUSE_ER1
1124	3.43 3.60 4.33 3.37 2.67 3.40 3.23
1125	LUSE_ER2
1126	4.10 3.90 3.20 3.90 3.77 3.53 3.63
1127	
1128	A6
1129	3.17
1130	2.90
1131	2.87
1132	3.10
1133	3.23
1134	3.03
1135	3.17
1136	3.03
1137	2.90
1138	2.87
1139	2.97
1140	3.03
1141	3.10
1142	2.80
1143	2.63
1144	3.03
1145	
1146	A7
1147	2.60
1148	2.37
1149	2.00
1150	3.10
1151	3.57
1152	3.73
1153	2.57
1154	3.27
1155	2.70
1156	2.40
1157	2.43
1158	3.37
1159	2.40
1160	2.20
1161	2.37
1162	3.17
1163	
1164	A8
1165	3.67
1166	3.10
1167	3.47
1168	3.47
1169	4.30
1170	4.13
1171	3.30
1172	3.43
1173	3.60
1174	3.47
1175	3.40
1176	3.23
1177	3.10
1178	2.50
1179	2.80
1180	3.03
1181	
1182	A9
1183	3.33
1184	3.80
1185	3.47
1186	3.20
1187	3.70
1188	3.77
1189	4.00
1190	3.27
1191	3.33
1192	3.47
1193	4.27
1194	3.57
1195	3.27
1196	3.53
1197	3.97
1198	3.17
1199	
1200	A10 Average
1201	3.50
1202	3.42
1203	3.57
1204	3.37
1205	3.37
1206	3.11
1207	3.50
1208	3.54
1209	3.30
1210	3.68
1211	3.47
1212	3.48
1213	3.63
1214	3.55
1215	3.53
1216	3.56
1217	3.43
1218	3.35
1219	2.93
1220	3.10
1221	3.43
1222	3.54
1223	3.43
1224	3.57
1225	3.27
1226	3.25
1227	2.83
1228	2.94
1229	3.13
1230	3.24
1231	3.40
1232	3.49
1233	
1234	Note: A1 – ChatGPT 3.5, A2 – ChatGPT 4, A3 – ChatGPT 4o, A4 - Gemini 1.5, A5 - Claude 3.5
1235	Sonnet, A6 - OpenAI o1, A7 – Gemini 2.0, A8 – DeepSeek V3, A9 - Gemini 1.5 Pro, A10 DeepSeek R1.
1236	Consistent with patterns of the mean scores in Table 6 and what presented in Figure 1, Gemini
1237	2.0 was an extreme severe rater with a logit value of 1.25. ChatGPT 4 was the most neutral rater
1238	with a rater parameter estimate close to 0. If we follow the cut value of 0.3, all AI raters did not
1239	have severe rater effects except ChatGPT 3.5 (-0.37) at the lenient end, while OpenAI o1 (0.5) at
1240	the harsh end. The two human raters had the smallest infit and outfit mean squares (both smaller
1241	than the cut value of 0.7), indicating potential central tendency effect. DeepSeek R1, ChatGPT
1242	3.5, and Gemini 1.5 Pro had infit and outfit mean squares larger than 1.3, indicating potential
1243	misfit.
1244	
1245	11
1246	
1247	Figure 1. The Wright Map for the Holistic Scores
1248	For analytic scoring across all three traits as shown in Figure 2, SN2 was still the most
1249	difficult essay, while ER2 was the easiest essay. SN1 was the second difficult essay. Gemini 2.0
1250	was the most stringent rater, which is consistent with the lowest mean scores assigned while two
1251	human raters were the most lenient raters. Among the three traits, Language Use was the most
1252	difficult, while Task Completion was the easiest.
1253	Table 8 presents the rater parameter estimates for the analytic scores. Human rater R2
1254	was slightly more lenient than R1, but with a smaller difference of about 0.08. Consistent with
1255	what presented in Figure 2, Gemini 2.0 was a severe rater with a logit value of 0.76. DeepSeek
1256	V3 was the most neutral rater with a rater parameter estimate close to 0. All AI raters did not
1257	have severe rater effects except OpenAI o1 (0.5) at the harsh end. OpenAI o1 had the least infit
1258	
1259	12
1260	
1261	and outfit mean squares at the borderline (0.69). No infit and outfit mean squares were larger
1262	than 1.3 for any rater.
1263	Table 7
1264	Rater Parameter Estimates for Holistic Scoring
1265	
1266	Rater
1267	2 R2
1268	3 ChatGPT 3.5
1269	7 Claude 3.5 Sonnet
1270	1 R1
1271	12 DeepSeek R1
1272	11 Gemini 1.5 Pro
1273	10 DeepSeek V3
1274	4 ChatGPT 4
1275	5 ChatGPT 4o
1276	6 Gemini 1.5
1277	8 OpenAI o1
1278	9 Gemini 2.0
1279	
1280	Rater Par
1281	-0.81
1282	-0.37
1283	-0.30
1284	-0.20
1285	-0.18
1286	-0.14
1287	-0.10
1288	0.02
1289	0.10
1290	0.23
1291	0.50
1292	1.25
1293	
1294	SE
1295	0.11
1296	0.11
1297	0.11
1298	0.11
1299	0.11
1300	0.11
1301	0.11
1302	0.11
1303	0.11
1304	0.11
1305	0.11
1306	0.11
1307	
1308	Infit MS
1309	0.60
1310	1.36
1311	1.01
1312	0.58
1313	1.37
1314	1.41
1315	1.07
1316	0.91
1317	0.85
1318	0.85
1319	0.70
1320	1.22
1321	
1322	Table 8
1323	Rater Parameter Estimates for Analytic Scoring
1324	Rater
1325	Rater Par SE
1326	Infit MS
1327	2 R2
1328	-0.55
1329	0.06
1330	0.73
1331	1 R1
1332	-0.47
1333	0.06
1334	0.83
1335	3 ChatGPT 3.5
1336	-0.31
1337	0.06
1338	1.21
1339	11 Gemini 1.5 Pro
1340	-0.29
1341	0.06
1342	1.19
1343	7 Claude 3.5 Sonnet
1344	-0.17
1345	0.06
1346	0.97
1347	4 ChatGPT 4
1348	-0.10
1349	0.06
1350	0.88
1351	10 DeepSeek-v3
1352	0.05
1353	0.06
1354	1.18
1355	12 DeepSeek R1
1356	0.10
1357	0.06
1358	1.15
1359	5 ChatGPT 4o
1360	0.11
1361	0.06
1362	1.06
1363	6 Gemini 1.5
1364	0.30
1365	0.06
1366	0.84
1367	8 OpenAI o1
1368	0.57
1369	0.06
1370	0.69
1371	9 Gemini 2.0
1372	0.76
1373	0.06
1374	1.21
1375	
1376	Outfit MS
1377	0.60
1378	1.36
1379	1.01
1380	0.59
1381	1.41
1382	1.41
1383	1.08
1384	0.92
1385	0.84
1386	0.88
1387	0.69
1388	1.29
1389	
1390	Outfit MS
1391	0.73
1392	0.84
1393	1.20
1394	1.19
1395	0.97
1396	0.89
1397	1.18
1398	1.18
1399	1.05
1400	0.87
1401	0.69
1402	1.26
1403	
1404	13
1405	
1406	Figure 2. The Wright Map for the Analytic Scores
1407	Table 9 presents the rater parameter estimates for the analytic scores for Task
1408	Completion. Two human raters were most lenient with R1 slightly more lenient than R2. OpenAI
1409	o1 was the most severe rater with a logit value of 0.61. ChatGPT 4 and Claude 3.5 were more
1410	neutral rater with a rater parameter estimate smaller than an absolute value of 0.1. All AI raters
1411	did not have severe rater effects except OpenAI o1 (0.5) at the harsh end, followed by Gemini
1412	1.5 (0.53) and 2.0 (0.38). No infit and outfit mean squares were smaller than 0.7 or larger than
1413	1.3 for any rater.
1414	
1415	14
1416	
1417	Figures 3, 4, and 5 present the Wright Maps for the analytic scores assigned to each of
1418	the three traits. For the Task Completion trait (Figure 3), SN2 was still the most difficult essay
1419	while SN1 was the easiest essay. ER1 and ER2 had about the same difficulty. OpenAI o1 was
1420	the most stringent rater while two human raters were the most lenient raters. R1 was more lenient
1421	than R2 on Task Completion trait scoring.
1422	
1423	Figure 3. The Wright Map for the Analytic Scores-Task Completion
1424	For the Delivery trait (Figure 4), SN2 was still the most difficult essay while ER2 was the
1425	easiest essay. Gemini 2.0 was the most stringent rater while R2 was the most lenient raters. R1
1426	was the second most lenient rater like Claude 3.5 and Gemini 1.5 Pro on Delivery trait scoring.
1427	
1428	15
1429	
1430	Table 9
1431	Rater Parameter Estimates for Analytic Scoring-Task Completion
1432	Rater
1433	Rater Par
1434	SE
1435	Infit MS
1436	Outfit MS
1437	1 R1
1438	-0.51
1439	0.11
1440	0.97
1441	0.96
1442	2 R2
1443	-0.36
1444	0.11
1445	0.74
1446	0.73
1447	10 DeepSeek V3
1448	-0.30
1449	0.11
1450	1.24
1451	1.23
1452	5 ChatGPT 4o
1453	-0.20
1454	0.11
1455	0.97
1456	0.96
1457	11 Gemini 1.5 Pro
1458	-0.16
1459	0.11
1460	1.24
1461	1.23
1462	3 ChatGPT 3.5
1463	-0.13
1464	0.11
1465	1.16
1466	1.16
1467	4 ChatGPT 4
1468	-0.06
1469	0.11
1470	0.90
1471	0.88
1472	7 Claude 3.5 Sonnet
1473	0.09
1474	0.11
1475	0.96
1476	0.96
1477	12 DeepSeek R1
1478	0.11
1479	0.11
1480	1.15
1481	1.15
1482	9 Gemini 2.0
1483	0.38
1484	0.11
1485	1.04
1486	1.05
1487	6 Gemini 1.5
1488	0.53
1489	0.11
1490	0.85
1491	0.88
1492	8 OpenAI o1
1493	0.61
1494	0.11
1495	0.78
1496	0.78
1497	
1498	Figure 4. The Wright Map for the Analytic Scores-Delivery
1499	16
1500	
1501	Table 10
1502	Rater Parameter Estimates for Analytic Scoring-Delivery
1503	Rater
1504	Rater Par SE
1505	Infit MS Outfit MS
1506	2 R2
1507	-0.63
1508	0.11
1509	0.78
1510	0.80
1511	11 Gemini 1.5 Pro
1512	-0.40
1513	0.11
1514	1.13
1515	1.12
1516	1 R1
1517	-0.35
1518	0.11
1519	0.80
1520	0.81
1521	7 Claude 3.5 Sonnet
1522	-0.35
1523	0.11
1524	1.01
1525	1.01
1526	3 ChatGPT 3.5
1527	-0.30
1528	0.11
1529	1.23
1530	1.22
1531	4 ChatGPT 4
1532	-0.18
1533	0.11
1534	0.93
1535	0.95
1536	10 DeepSeek V3
1537	-0.06
1538	0.11
1539	1.09
1540	1.09
1541	12 DeepSeek R1
1542	0.11
1543	0.11
1544	1.29
1545	1.32
1546	5 ChatGPT 4o
1547	0.18
1548	0.11
1549	0.99
1550	0.99
1551	6 Gemini 1.5
1552	0.29
1553	0.11
1554	0.87
1555	0.90
1556	8 OpenAI o1
1557	0.68
1558	0.11
1559	0.70
1560	0.71
1561	9 Gemini 2.0
1562	1.03
1563	0.12
1564	1.07
1565	1.13
1566	Table 10 presents the rater parameter estimates for the analytic scores for Delivery.
1567	Human rater R2 was the most lenient. Gemini 2.0 was the most severe rater with a rater
1568	parameter of 1.03. DeepSeek V3 was the most neutral rater with a rater parameter estimate of 0.06. Using an absolute cut value of 0.3, OpenAI o1 was a harsh rater, while Claude 3.5 was
1569	slightly lenient. All other AI raters did not have severe rater effects. No infit and outfit mean
1570	squares were smaller than 0.7 or larger than 1.3 for any rater.
1571	Table 11
1572	Rater Parameter Estimates for Analytic Scoring-Language Use
1573	Rater
1574	Infit
1575	Outfit
1576	Rater
1577	Par
1578	SE
1579	MS
1580	MS
1581	2 R2
1582	-0.74
1583	0.11
1584	0.72
1585	0.74
1586	1 R1
1587	-0.63
1588	0.11
1589	0.78
1590	0.79
1591	3 ChatGPT 3.5
1592	-0.55
1593	0.11
1594	1.33
1595	1.33
1596	11 Gemini 1.5 Pro
1597	-0.37
1598	0.11
1599	1.23
1600	1.23
1601	7 Claude 3.5 Sonnet
1602	-0.29
1603	0.11
1604	0.96
1605	0.96
1606	4 ChatGPT 4
1607	-0.10
1608	0.11
1609	0.90
1610	0.92
1611	12 DeepSeek R1
1612	0.09
1613	0.11
1614	1.09
1615	1.14
1616	6 Gemini 1.5
1617	0.10
1618	0.11
1619	0.88
1620	0.92
1621	5 ChatGPT 4o
1622	0.40
1623	0.11
1624	1.10
1625	1.09
1626	8 OpenAI o1
1627	0.49
1628	0.11
1629	0.64
1630	0.63
1631	10 DeepSeek V3
1632	0.54
1633	0.11
1634	0.97
1635	0.96
1636	9 Gemini 2.0
1637	1.06
1638	0.12
1639	1.39
1640	1.42
1641	For the Language Use trait (Figure 5), SN2 was still the most difficult essay while ER2
1642	was the easiest essay. Gemini 2.0 was the most stringent rater while rater 2 was the most lenient
1643	raters. R1 was the second most lenient rater on Language Use trait scoring.
1644	
1645	17
1646	
1647	Table 11 presents the rater parameter estimates for the analytic scores for Language Use.
1648	Human rater R2 was the most lenient, R1 the second most lenient. Gemini 2.0 was the most
1649	severe rater with a rater parameter of 1.06. DeepSeek R1, ChatGPT 4 and Gemini 1.5 were more
1650	neutral with an absolute rater parameter estimate around 0.1. Using the absolute cut value of 0.3,
1651	DeepSeek V3, OpenAI o1, and ChatGPT 4o were slightly harsh raters while Gemini 1.5 Pro and
1652	ChatGPT 3.5 were slightly lenient. OpenAI o1 had infit and outfit mean squares smaller than 0.7,
1653	indicating slight central tendency, while ChatGPT 3.5 and Gemini 2.0 yielded infit and outfit
1654	mean squares larger than 1.3, indicating slight misfit.
1655	
1656	Figure 5. The Wright Map for the Analytic Scores-Language Use
1657	
1658	18
1659	
1660	Summary and Discussion
1661	This study aims to examine the rater effects of LLM-based AI raters in automated
1662	scoring. To illustrate the methods for exploring AI rater effects, this study investigated the use of
1663	LLMs for automated holistic and analytic scoring using a fully crossed rating design. Ten LLMs
1664	were compared including ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5
1665	Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3, and DeepSeek R1
1666	against two human expert raters in scoring two types of writing tasks for the AP Chinese exams.
1667	The holistic and analytic score accuracy of LLMs compared with human raters were evaluated in
1668	terms of QWK. Intra-rater consistency across essays was compared in terms of Cronbach Alpha.
1669	Rater effects of LLMs were evaluated and compared with human raters using the Many FACET
1670	Rasch model.
1671	For Research Question 1 related to the AI raters’ accuracy, for holistic scoring, ChatGPT
1672	4o, Claude 3.5, and Gemini 1.5 Pro yielded the highest scoring accuracy against either human
1673	rater. ChatGPT 4o performed the best on ER items, while Gemini 1.5 Pro excelled on SN items
1674	while Claude 3.5 showed strong performance on both SN and ER items. These three LLMs
1675	turned out to be the best performing models in analytic scoring as well. For Task Completion,
1676	ChatGPT 4o performed the best for SN and ER2 items while Claude 3.5 and Gemini 1.5 Pro
1677	performed the best on SN2 and ER1 essays. For Delivery, Claude 3.5 performed the best on
1678	SN1 and ER1 while ChatGPT4o and Gemini 1.5 Pro performed the best on ER2 and SN2
1679	respectively. For the Language Use trait, ChatGPT 4, 4o, and Gemini 1.5 were the top
1680	performers on ER essays while Claude 3.5 and Gemini 1.5 Pro were the best performers for SN
1681	essays. In general, QWKs for the best performing AI raters were higher than those between two
1682	human raters for holistic scoring. However, human-human QWK were higher on analytic scoring
1683	than AI QWKs. QWKs for analytic scores were higher than those for holistic scoring.
1684	For Research Question 2 related to the AI raters’ intra-rater consistency, ChatGPT 4o
1685	yielded the highest intra-rater consistency for the holistic scores, the analytic scores on the
1686	Delivery trait, and the ER items. On the other hand, Claude 3.5 yielded the highest consistency
1687	for the analytic scores, analytic scores on the Task Completion and Language Use traits as well
1688	as the SN items. Human rater R2 yielded higher scoring consistency compared with R1. The best
1689	performing AI raters’ intra-rater consistency were about the same as those for the best
1690	performing human rater except on ER essays and analytic scores on Language Use with slightly
1691	lower consistency.
1692	For Research Questions 3 on the rater effects, human raters in general were more lenient.
1693	Gemini 2.0 turned out to be a harsh rater on most scoring tasks. ChatGPT 3.5 turned out to be a
1694	lenient rater in 3 out of 5 scoring analyses with DeepSeek V3 and Gemini 1.5 Pro as the two
1695	other lenient raters. Whether an AI rater was more neutral raters depends on the task. There was
1696	no evident central tendency effects for the AI raters. However, the two human raters displayed
1697	some minor central tendency effect in holistic scoring. As Wolfe (2004) pointed out, the rater
1698	effects estimated in the FACET Rasch model was scaled to a mean of 0. If the number of raters
1699	included in the comparison differs, the estimated rater effect may be different.
1700	
1701	19
1702	
1703	The results in general support the use of ChatGPT 4o, Gemini 1.5 Pro, and Claude 3.5
1704	Sonnet with high scoring accuracy, better intra-rater consistency, and less rater effects. However,
1705	there were no AI raters which consistently performed the best. Some further explorations will be
1706	conducted to better understand the AI rater scoring logic. The findings of this study provide
1707	insights into the strengths and limitations of AI raters compared to human raters using the data in
1708	the study.
1709	The limitations of the study lies in the sample size, the content domain, the type and the
1710	number of essays. There were only 30 students who participated in this experiment. The FACET
1711	software manual states a sample size of 30 as a minimum sample size. However, as the FACET
1712	Rasch model is an item response theory based latent trait model, a larger sample size would be
1713	expected even though the standard error of the rater parameter estimates was relatively small in
1714	the current study. Further, the content of the tasks was related to the AP Chinese exam. Whether
1715	the findings from this study is generalizable to other content domains such as English writing,
1716	reading, science, and math constructed-response items awaits further exploration. In addition,
1717	only two items types: SN and ER were included in the experiments, with a total of only 4 items.
1718	Other task types and traits for analytic scoring should be examined in future studies. The last
1719	limitation is related to the prompting methods for automated scoring using LLMs. The current
1720	study used a few-shot methods. Other methods should be explored in future studies including
1721	Chain-of-Thought and other fine-tuning methods.
1722	In summary, this study assessed the scoring accuracy, intra-rater consistency of AI and
1723	human holistic and analytic ratings, and estimated the AI rater effects. It demonstrated the
1724	methods that can be used to examine AI rater performance, in particular, the use of the Many
1725	FACET Rasch model to evaluate rater severity/leniency and central tendency effects. This study
1726	provided empirical evidence to inform the adoption of LLM-based AI raters for automated
1727	holistic and analytic scoring. It is highlighted that when LLMs are used for automated scoring,
1728	the methods demonstrated in this study could be the starting point for such evaluation.
1729	
1730	20
1731	
1732	References
1733	AI Anthropic. (2024). The claude 3 model family: Opus, sonnet, haiku. Claude-3 Model Card, 1,
1734	2024.
1735	Andrich, D. A. (1978). A rating formulation for ordered response categories. Psychometrika, 43,
1736	561-573. doi:10.1007/BF02293814
1737	Bond, T. G., & Fox, C. M. (2007). Applying the Rasch model: Fundamental measurement in the
1738	human sciences (2nd ed.). Mahwah, NJ: Erlbaum
1739	Bond, T. G , Yan, Z., & Heene, M. (2021). Applying the Rasch model: Fundamental
1740	measurement in the human sciences (4th ed). Routledge
1741	Bui, N.M., & Barrot, J.S. (2024). ChatGPT as an automated essay scoring tool in the writing
1742	classrooms: how it compares with human scoring. Education and Information
1743	Technologies. https://doi.org/10.1007/s10639-024-12891-w
1744	Cohen, J. (1968). Weighted kappa: Nominal scale agreement provision for scaled disagreement
1745	or partial credit. Psychological bulletin, 70, 4 (1968), 213.
1746	Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological
1747	Measurement, 20(1), 37–46.
1748	Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep
1749	Bidirectional Transformers for Language Understanding. arXiv:1810.04805 [Cs].
1750	http://arxiv.org/abs/1810.04805
1751	Eckes T (2009) On common ground? How raters perceive scoring criteria in oral proficiency
1752	testing. In Brown A, Hill K (ed) Language testing and evaluation 13: Tasks and criteria
1753	in performance assessment (pp. 43–73). Peter Lang Publishing
1754	Eckes, T. (2015). Introduction to many-facet Rasch measurement: Analyzing and evaluating
1755	rater mediated assessments (2nd ed.). Frankfurt am Main, Germany: Peter Lang.
1756	Engelhard, G. (2002). Monitoring raters in performance assessments. In G. Tindal & T. M.
1757	Haladyna (Eds.), Large-scale assessment programs for all students: Validity, technical
1758	adequacy, and implementation (pp. 261–287). Mahwah, NJ: Erlbaum.
1759	Gao, T., Jin, J., Zheng, K,, & and Moryoussef, G. (2025). A Comparison of DeepSeek and Other
1760	LLMs." arXiv preprint arXiv:2502.03688 .
1761	
1762	Gemini Team Google. (2023, Dec.). Gemini: A family of highly capable multimodal models.
1763	arXiv preprint arXiv:2312.11805 .
1764	Gunduz, A., & Gierl, M. (2024). Automated essay scoring with ChatGPT 3.5 and 4.0.
1765	Presentation at the UBlberta Graduate Student Research in Education Conference.
1766	He, P., Liu, X., Gao, J., & Chen, W. (2021). DeBERTa: Decoding-enhanced BERT with
1767	disentangled attention. Preprint retrieved from https://arxiv.org/abs/2006.03654
1768	Joshi, S. (2025). A Comprehensive Review of DeepSeek: Performance, Architecture and
1769	Capabilities.
1770	Kim, S., & Jo, M. (2024, July). Is GPT-4 Alone Sufficient for Automated Essay Scoring?: A
1771	Comparative Judgment Approach Based on Rater Cognition. In Proceedings of the
1772	Eleventh ACM Conference on Learning@ Scale (pp. 315-319).
1773	Kortemeyer, G. (2024). Performance of the pre-trained large language model GPT-4 on
1774	automated short answer grading. Discover Artificial Intelligence, 4(1), 47.
1775	Kundu, A., & Barbosa, D. (2024). Are Large Language Models Good Essay Graders?. arXiv
1776	preprint arXiv:2409.13120.
1777	Kwako, A., & Hansen, M. (2023). Extracting additional information from constructed response
1778	21
1779	
1780	items using latent variable language modeling. Presentation at the virtual annual meeting
1781	of National Council on Measurement in Education.
1782	Latif, E., & Zhai, X. (2024). Fine-tuning ChatGPT for automatic scoring. Computers and
1783	Education: Artificial Intelligence, 6. https://doi.org/10.1016/j.caeai.2024.100210.
1784	Lee, G. G., Latif, E., Wu, X., Liu, N., & Zhai, X. (2024). Applying large language models and
1785	chain-of-thought for automatic scoring. Computers and Education: Artificial
1786	Intelligence, 6, 100213.
1787	Li, W., & Liu, H. (2024). Applying large language models for automated essay scoring for nonnative Japanese. Humanit Soc Sci Commun 11, 723. https://doi.org/10.1057/s41599-02403209-9
1788	Linacre, J. M. (1994). Many-Facet Rasch Measurement, (2nd ed). Chicago, IL: MESA
1789	Press.
1790	Linacre, J. M. (2003). Size vs. Significance: Infit and Outfit Mean-Square and Standardized ChiSquare Fit Statistic. Rasch Measurement Transactions, 17:918
1791	Linacre, J. M. (2024). FACET computer program for many-facet Rasch measurement (Version
1792	3.87.0). Beaverton, OR: Author.
1793	Ludwig, S., Mayer, C., Hansen, C., Eilers, K., & Brandt, S. (2021). Automated Essay Scoring
1794	Using Transformer Models. Psych, 3(4), 897–915. https://doi.org/10.3390/psych3040056
1795	Lumley, T., & McNamara, T. F. (1995). Rater characteristics and rater bias: Implications for
1796	training. Language Testing, 12(1), 54–71. https://doi.org/10.1177/026553229501200104
1797	McNamara, T. F. (1996). Measuring second language performance. New York: Longman
1798	Miller, G. E., Rotou, O., & Twing, J. S. (2004). Evaluation of the 0.3 logits screening criterion in
1799	common item equating. Journal of Applied Measurement, 5(2), 172–177.
1800	Mizumoto, A., & Eguchi, M. (2023). Exploring the potential of using an AI language model for
1801	automated essay scoring. Research Methods in Applied Linguistics. 2, 100050,
1802	https://doi.org/10.1016/j.rmal.2023.100050
1803	Müller, M. Item fit statistics for Rasch analysis: can we trust them?. J Stat Distrib App 7, 5 (2020).
1804	https://doi.org/10.1186/s40488-020-00108-7
1805	Myford, C. M., & Wolfe, E. W. (2003). Detecting and measuring rater effects using many-facet
1806	Rasch measurement: Part I. Journal of Applied Measurement, 4, 386-422.
1807	Myford, C. M., & Wolfe, E. W. (2004). Detecting and measuring rater effects using many-facet
1808	Rasch measurement: Part II. Journal of Applied Measurement, 5, 189-227.
1809	OpenAI (2023). ChatGPT: Optimizing language models for dialogue. Retrieved October 10, 2023,
1810	from https://openai.com/blog/chatgpt/
1811	OpenAI. (2023). GPT-4 Technical Report, March 2023. arXiv:2303.08774 [cs].
1812	Ormerod, C. M., Malhotra, A., & Jafari, A. (2021). Automated essay scoring using efficient
1813	transformer based language models. Preprint retrieved from
1814	https://arxiv.org/abs/2102.13136
1815	Pack, A., Barrett, A., & Escalante, J. (2024). Large language models and automated essay scoring
1816	of English language learner writing: Insights into validity and reliability. Computers and
1817	Education: Artificial Intelligence, 6(2024), 1-9.
1818	https://doi.org/10.1016/j.caeai.2024.100234
1819	Page, E. B. The imminence of grading essays by computer. Phi Delta Kappa. 47, 238–243 (1966).
1820	Parker, J. L., Becker, K., & Carroca, C. (2023). ChatGPT for automated writing evaluation in
1821	scholarly writing instruction. Journal of Nursing Education, 62(12), 721–727.
1822	Ramesh, D., & Sanampudi, S. K. (2022). An automated essay scoring systems: a systematic
1823	22
1824	
1825	literature review. Artificial Intelligence Review, 55, 2495-2527.
1826	https://doi.org/10.1007/s10462-021-10068-2
1827	Riedl, M. O. (2019). Human‐centered artificial intelligence and machine learning. Human
1828	Behavior and Emerging Technologies, 1(1), 33-36.
1829	Rodriguez, P. U., Jafari, A., & Ormerod, C. M. (2019). Language models and Automated Essay
1830	Scoring. Preprint retrieved from https://arxiv.org/abs/1909.09482
1831	Saal, F. E., Downey, R. G., & Lahey, M. A. (1980). Rating the ratings: Assessing the
1832	psychometric quality of rating data. Psychological Bulletin, 88, 413-428.
1833	Shermis, M. D. (2015). Contrasting state-of-the-art in the machine scoring of short-form
1834	constructed responses. Educational Assessment, 20(1), 46-65.
1835	Song, D., & Tang, A. F. (2025). Exploring AI-assistance in L2 Chinese writing with
1836	standardized assessment tasks. Language Learning & Technology, 29(2), 161–189.
1837	https://hdl.handle.net/10125/73615
1838	Tate, T. P., Steiss, J., Bailey, D., Graham, S., Moon, Y., Ritchie, D., ... & Warschauer, M.
1839	(2024). Can AI provide useful holistic essay scoring?. Computers and Education:
1840	Artificial Intelligence, 7, 100255. https://doi.org/10.1016/j.caeai.2024.100255.
1841	Wijekumar, K. K., McKeown, D., Zhang, S., Lei, P. W., Hruska, N., & Pirnay-Dummer, P.
1842	(2024). We write automated scoring: Using ChatGPT for scoring in large-scale writing
1843	research projects. In The Routledge International Handbook of Automated Essay
1844	Evaluation (pp. 178-194). Taylor and Francis. https://doi.org/10.4324/9781003397618-12
1845	Williamson, D. M., Xi, X., & Breyer, F. J. (2012). A framework for evaluation and use of
1846	automated scoring. Educational Measurement: Issues and Practices, 31, 2.
1847	Wind, S. A. (2019). Examining the impacts of rater effects in performance assessments. Applied
1848	Psychological Measurement, 43(2), 159–171.
1849	Wolfe, E. W. (2004). Identifying rater effects using latent trait models. Psychology Science, 46,
1850	35–51.
1851	Wright, B. D., & Linacre, J. M. (1994). Reasonable mean-square fit values. Rasch Measurement
1852	Transactions, 8, 370.
1853	Wright, B. D. & Masters, G. N. (1982). Rating scale analysis, Chicago, IL: MESA
1854	Press.
1855	Xiao, C., Ma, W., Xu, S. X., Zhang, K., Wang, Y., & Fu, Q. (2024). From Automation to
1856	Augmentation: Large Language Models Elevating Essay Scoring Landscape. arXiv
1857	preprint arXiv:2401.06431.
1858	Yancey, K. P., Laflair, G., Verardi, A., & Burstein, J. (2023). Rating short L2 essays on the
1859	CEFR scale with GPT-4. In E. Kochmar, J. Burstein, A. Horbach, R. Laarmann-Quante,
1860	N. Madnani, A. Tack, V. Yaneva, Z. Yuan, & T. Zesch (Eds.), Proceedings of the 18th
1861	Workshop on Innovative Use of NLP for Building Educational Applications (pp. 576–
1862	584). Retrieved November 19, 2023, from https://aclanthology.org/2023.bea-1.49
1863	Yang, J., Latif, E., Zhai, X. (2025, In press). Fine-tuning ChatGPT for Automatic Scoring of
1864	Written Scientific Explanations in Chinese. Journal of Science Education and
1865	Technology.
1866	Yoshida, L. (2024). The Impact of Example Selection in Few-Shot Prompting on Automated
1867	Essay Scoring Using GPT Models. In: Olney, A.M., Chounta, IA., Liu, Z., Santos, O.C.,
1868	Bittencourt, I.I. (eds) Artificial Intelligence in Education. Posters and Late Breaking
1869	Results, Workshops and Tutorials, Industry and Innovation Tracks, Practitioners,
1870	Doctoral Consortium and Blue Sky. AIED 2024. Communications in Computer and
1871	23
1872	
1873	Information Science, vol 2150. Springer, Cham. https://doi.org/10.1007/978-3-03164315-6_5
1874	
1875	24
1876	
1877	Appendix A
1878	AI Training Prompting for Grading SN1 Student Essays
1879	Based on this prompt, grading rubric, and student writing samples, grade student's writing
1880	sample.
1881	Prompt: In this task, you will be asked to write in Chinese for a specific purpose and to a specific
1882	person. You should write in as complete and culturally appropriate a manner as possible, taking
1883	into account the purpose and the person described. The four pictures present a story. Imagine you
1884	are writing the story to a friend. Narrate a complete story as suggested by the pictures. Give your
1885	story a beginning, a middle, and an end.
1886	The first picture: A teenage boy is lying on his bed. His room is messy, and his dad is asking
1887	him to clean it up. There are many things on the bed and on the floor, including a guitar,
1888	basketball, football, books, and more. He is listening to music.
1889	The second picture: The boy puts everything under his bed, covers it with a bedsheet, and
1890	pretends he has cleaned the room.
1891	The third picture: His dad removes the bedsheet, sees the mess, and is very surprised and
1892	angry.
1893	The fourth picture: His dad goes downstairs and tells his son what he saw. The boy is sitting on
1894	the floor, playing video games, eating French fries, and drinking cola.
1895	The task for you is to rate the student responses. Assess each response holistically based on three
1896	key criteria: task completion, delivery, and language use, with task completion being the most
1897	critical factor. Start by determining whether the student fully addresses all aspects of the four
1898	pictures. Then, evaluate delivery and language use before assigning an overall score.
1899	Additionally, please provide three analytic scores—one for each criterion—following the rubric's
1900	guidelines. When rating, refer to the sample responses for each score level as benchmarks. In
1901	total, provide four scores: one overall score and three analytic scores. Tips: Student responses
1902	will be graded based on task completion, delivery, and language use. However, it is important to
1903	apply a holistic grading approach. Among these criteria, task completion is the most important. If
1904	a student addresses only three pictures, they will receive 3 points, regardless of the quality of
1905	their language use and delivery. A student will receive 4 points if they discuss all four pictures.
1906	In this context, use grading rubrics 5 and 6 as references for evaluating language use and
1907	delivery. If a student addresses three pictures but demonstrates weak language use and delivery,
1908	they may receive 2 points. A student who addresses only one or two pictures but includes one or
1909	two sentences may also receive 2 points. If a student writes only isolated words related to the
1910	prompts (pictures), they may receive 1 point.
1911	Grading Rubric:
1912	
1913	25
1914	
1915	Score of 0: UNACCEPTABLE: 1) Contains nothing that earns credit 2) Completely irrelevant to
1916	the stimulus 3) Not in Chinese characters, NR (No Response), BLANK (no response)
1917	Samples:
1918	Score 0: 你好
1919	Score 0: I want to eat icecream.
1920	Score of 1: Very Weak: Demonstrates lack of competence in interpersonal writing. - TASK
1921	COMPLETION: 1) E-mail addresses stimulus only minimally 2) Lacks organization and
1922	coherence; very disjointed sentences or isolated words -DELIVERY: 1) Constant use of register
1923	inappropriate to situation -LANGUAGE USE: 1) Insufficient, inappropriate vocabulary, with
1924	frequent errors that significantly obscure meaning; constant interference from another language
1925	2) Little or no control of grammatical structures, with frequent errors that significantly obscure
1926	meaning
1927	Score 1: 莫玩篮球房间。爸爸说莫它的。莫怕篮球房间。爸爸不高心有莫。爸爸莫去房
1928	Score 1: 小明在床上。
1929	Score of 2: Weak: Suggests lack of competence in interpersonal writing - TASK
1930	COMPLETION: 1) E-mail addresses topic only marginally or addresses only some aspects of
1931	stimulus 2) Scattered information generally lacks organization and coherence; minimal or no use
1932	of transitional elements and cohesive devices; fragmented sentences -DELIVERY: 1) Frequent
1933	use of register inappropriate to situation -LANGUAGE USE: 1) Minimal appropriate
1934	vocabulary, with frequent errors that obscure meaning; repeated interference from another
1935	language 2) Limited grammatical structures, with frequent errors that obscure meaning
1936	Score 2: 小蔡在床上，爸爸来房间，爸爸回到房间看，儿子没有整理。
1937	Score 2: 今天爸爸来到我的房间，让我打扫，可是我不想打扫。
1938	Score of 3: Adequate Suggests competence in interpersonal writing -TASK COMPLETION: 1)
1939	E-mail addresses topic directly but may not address all aspects of stimulus 2) Portions may lack
1940	organization or coherence; infrequent use of transitional elements and cohesive devices;
1941	disconnected sentences -DELIVERY: 1) Use of register appropriate to situation is inconsistent or
1942	includes many errors -LANGUAGE USE: 1) Limited appropriate vocabulary and idioms, with
1943	frequent errors that sometimes obscure meaning; intermittent interference from another language
1944	2) Mostly simple grammatical structures, with frequent errors that sometimes obscure meaning
1945	Score 3: 一天在星期五一个人叫麦可，麦可的爸爸要告诉他如果你要玩在电视你要干净你
1946	的地上。然后麦可要干净你的地上，他的爸爸要去看还有看，他方他的篮球，衣服，皮扎
1947	在他的睡觉地方。他的爸爸很生气！他去给他讲话。爸爸说“我很生气在你，你不可以玩
1948	电视“！然后他说”去放你的篮球，衣服，和皮扎放起来“！
1949	26
1950	
1951	Score 3: 小李的房间太凌乱了。 小李爸爸进来他的房间，看到房间里的混乱。小李的爸爸
1952	告诉他 “收拾你的房间！不然我就要拿走你的手机了”。 所以小李床下面脏器了混乱。小
1953	李收拾完的 时候，他去看电影。他爸爸找到小李做的事，他生气了。他说小李得再收拾
1954	他的房间。
1955	Score of 4: Good Demonstrates competence in interpersonal writing -TASK COMPLETION: 1)
1956	E-mail addresses all aspects of stimulus but may lack detail or elaboration 2) Generally
1957	organized and coherent; use of transitional elements and cohesive devices may be inconsistent;
1958	discourse of paragraph length, although sentences may be loosely connected -DELIVERY: 1)
1959	May include several lapses in otherwise consistent use of register appropriate to situation LANGUAGE USE: 1) Mostly appropriate vocabulary and idioms, with errors that do not
1960	generally obscure meaning 2) Mostly appropriate grammatical structures, with errors that do not
1961	generally obscure meaning
1962	Score 4: 儿子正在床上放松，他的爸爸走进他的房间，责骂他的居住环境凌乱不堪。爸爸
1963	要求儿子立刻收拾房间。然而，儿子没有打扫房间，而是把一切都塞到了床底下。爸爸后
1964	来回来，得知儿子没有打扫房间，而是把一切都藏在了床底下。爸爸下楼并要求儿子返回
1965	并打扫他的房间。
1966	Score 4: 一个下午，小王在翻松看电视。可是，他爸爸走进了他的房间，告诉他“你的房间
1967	真乱啊！以前你可以看电视，你现在得打扫。“ 所以小王把他的东西都放在床底下了，下
1968	楼。可是他的爸爸又走进了他的房间， 看床底下看到所有的物品，他下楼告诉小王“你还
1969	得打扫！”
1970	Score of 5: Very good Suggests excellence in interpersonal writing -TASK COMPLETION: 1)
1971	E-mail addresses all aspects of stimulus 2) Well organized and coherent, with a progression of
1972	ideas that is generally clear; some use of transitional elements and cohesive devices; connected
1973	discourse of paragraph length -DELIVERY: 1) Consistent use of register appropriate to situation
1974	except for occasional lapses -LANGUAGE USE: 1) Appropriate vocabulary and idioms, with
1975	sporadic errors 2) Variety of grammatical structures, with sporadic errors
1976	Score 5: 有一天下午，天明在房间里面听手机上的音乐。突然，天明的爸爸走进他的房间
1977	里，发现了他的房间乱七八糟，就对天明说他需要先把房间收拾好，才能玩儿。爸爸走了
1978	以后，天明就偷偷的把房间里面的所有东西都放在床底下。过了几个小时以后，爸爸又来
1979	到天明的房间里检查收拾了怎么样。天有不测风云，爸爸发现了床底下的东西，很吃惊。
1980	那时候，天明在楼下玩游戏。爸爸赶快到楼下很生气的跟天明说他需要把东西收拾好。
1981	Score 5: 有一天，一个叫小明的男孩独自在房间里听音乐。他已经有几周还没有打扫了，
1982	房间很乱。当小明的爸爸进他的房间看到这个混乱时，他非常生气，立刻命令小明打扫。
1983	小明真的不想打扫房间，他宁愿看电视。爸爸离开的时候，他就制定计划。小明把所有的
1984	垃圾和脏衣服都收拾起来，然后藏在床底下。他以为这足以让他爸爸满意，赶快下到客厅
1985	看电视。起初，当小明的爸爸看到房间有多干净时，他感到自豪，但当他看床底下时，一
1986	切都改变了。他立刻下到客厅，告诉小明要真正打扫，不要只是把东西藏在床底下。
1987	27
1988	
1989	Score of 6: Excellent Demonstrates excellence in interpersonal writing -TASK COMPLETION:
1990	1) E-mail addresses all aspects of stimulus with thoroughness and detail 2) Well organized and
1991	coherent, with a clear progression of ideas; use of appropriate transitional elements and cohesive
1992	devices; well-connected discourse of paragraph length -DELIVERY: 1) Consistent use of
1993	register appropriate to situation -LANGUAGE USE: 1) Rich and appropriate vocabulary and
1994	idioms, with minimal errors 2) Wide range of grammatical structures, with minimal errors
1995	Score 6: 一个阳光明媚的下午，小明躺在床上，一边听音乐一边玩手机，悠闲得很。突
1996	然，爸爸推门而入，看到房间乱得不可收拾，顿时火冒三丈。地上散落着书本、袜子、鞋
1997	子、球类，甚至还有披萨盒。他厉声命令小明立刻整理房间。小明口头答应，可等爸爸一
1998	离开，他便把所有东西胡乱塞进床底，装作已经收拾好了。自以为聪明的小明满意地走下
1999	楼，准备看电影放松一下。爸爸起了疑心，觉得五分钟不可能彻底整理完，于是折返回来
2000	查看。房间表面看起来干净整齐，但他无意间发现床底露出一本书的角。他蹲下身，一掀
2001	床单，果然发现所有杂物都藏在下面。他无奈地摇头，大喊：“小明，回房间来！”正在客
2002	厅吃东西的小明听见爸爸的声音，吓得立刻冲回楼上。
2003	Score 6: 今天爸爸走进我的房间，看到地板上堆满了书本、衣服和零食包装袋，脸色立刻
2004	沉了下来。他盯着我，说：“你必须把房间打扫干净。”我心里虽然知道他是对的，但实在
2005	太懒了，就随便把所有东西都塞到了床底下，假装收拾过了。然后我慢悠悠地下楼，一边
2006	吃着薯片一边看电视，脑子有点恍惚，完全没把这件事放在心上。没过多久，爸爸上楼检
2007	查，果然发现床底藏着所有的“秘密”。我的床底堆满了东西。他又下楼来，脸色更难看
2008	了，对我说：“你必须重新认真整理房间。”我这才意识到，想蒙混过关是行不通的，我总
2009	好快速跑上楼去打扫。
2010	
2011	28
2012	
2013	Appendix B
2014	Table B.1
2015	Standard Deviation of the Holistic and Analytic Scores Assigned by Each Rater
2016	R1 R2 A1 A2 A3 A4 A5 A6 A7 A8
2017	SN1
2018	0.75 0.76 1.01 0.89 1.17 0.79 1.10 0.83 0.67 0.84
2019	ER1
2020	0.88 0.95 1.47 0.68 0.91 0.90 1.22 0.76 0.85 1.24
2021	SN2
2022	0.68 0.65 0.94 1.03 0.84 0.66 1.06 0.94 1.02 0.90
2023	ER2
2024	1.11 1.17 1.01 1.23 1.25 0.67 1.38 1.03 1.06 1.17
2025	Task_SN1
2026	1.03 0.85 0.79 0.79 1.25 0.79 1.10 0.90 0.68 1.15
2027	Task_SN2
2028	0.89 0.78 0.82 0.92 1.07 0.66 1.03 1.16 0.74 1.04
2029	Task_ER1
2030	1.20 1.06 1.53 0.82 1.18 1.13 1.30 0.83 0.86 1.09
2031	Task_ER2
2032	1.40 1.28 1.17 1.23 1.25 0.73 1.28 1.00 0.98 1.10
2033	Delivery_SN1 0.86 0.85 1.07 0.89 1.14 0.88 1.10 0.80 0.65 0.93
2034	Delivery_SN2 0.63 0.67 0.86 0.92 0.87 0.66 1.05 0.68 0.72 0.90
2035	Delivery_ER1 0.86 0.98 1.39 0.90 0.89 0.77 1.16 0.76 0.77 0.93
2036	Delivery_ER2 1.35 1.28 1.03 1.07 1.22 0.81 1.21 1.00 0.81 0.97
2037	LUSE_SN1
2038	0.87 0.93 1.04 0.89 1.03 0.97 1.10 0.76 0.77 1.12
2039	LUSE_SN2
2040	0.60 0.68 0.86 0.97 0.81 0.66 1.03 0.76 1.24 0.82
2041	LUSE_ER1
2042	0.77 0.89 1.40 0.72 1.03 0.93 1.01 0.56 0.89 0.89
2043	LUSE_ER2
2044	1.30 1.30 0.92 1.24 1.01 0.78 1.22 1.00 0.91 1.00
2045	
2046	A9
2047	0.92
2048	1.30
2049	0.86
2050	1.47
2051	1.02
2052	0.68
2053	1.31
2054	1.44
2055	0.92
2056	0.86
2057	1.20
2058	1.04
2059	0.98
2060	0.78
2061	1.16
2062	0.91
2063	
2064	A10
2065	1.17
2066	1.19
2067	1.19
2068	1.46
2069	0.84
2070	1.11
2071	1.40
2072	1.46
2073	1.17
2074	1.05
2075	1.17
2076	1.28
2077	1.01
2078	1.09
2079	1.01
2080	1.19
2081	
2082	Note: A1 – ChatGPT 3.5, A2 – ChatGPT 4, A3 – ChatGPT 4o, A4 - Gemini 1.5, A5 - Claude 3.5
2083	Sonnet, A6 - OpenAI o1, A7 – Gemini 2.0, A8 – DeepSeek V3, A9 - Gemini 1.5 Pro, A10 DeepSeek R1.
2084	
2085	29
2086	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46a4889f-ede9-4387-b9a9-80f34d97840e",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "aed1d3e555792ca7c",
  "type": "user",
  "uuid": "86c3122a-c098-4cbd-8924-e730127d10a9",
  "sourceToolAssistantUUID": "46a4889f-ede9-4387-b9a9-80f34d97840e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T16:41:53.636Z_

Here is the complete extracted text from arXiv:2505.18486.

---

## Paper: "Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model"

**Authors:** Hong Jiao (University of Maryland, College Park), Dan Song, Won-Chan Lee (University of Iowa)

---

### ABSTRACT

Large language models (LLMs) have been widely explored for automated scoring in low-stakes assessment to facilitate learning and instruction. Empirical evidence related to which LLM produces the most reliable scores and induces least rater effects needs to be collected before the use of LLMs for automated scoring in practice. This study compared ten LLMs (ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3, and DeepSeek R1) with human expert raters in scoring two types of writing tasks. The accuracy of the holistic and analytic scores from LLMs compared with human raters was evaluated in terms of Quadratic Weighted Kappa. Intra-rater consistency across prompts was compared in terms of Cronbach Alpha. Rater effects of LLMs were evaluated and compared with human raters using the Many-Facet Rasch model. The results in general supported the use of ChatGPT 4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet with high scoring accuracy, better rater reliability, and less rater effects.

---

### 1. INTRODUCTION (Complete text)

**Paragraph 1:**
Performance assessment tasks, including essays and other types of constructed-response (CR) items are commonly used for assessing high-order thinking skills such as synthesizing information from multiple sources, critical evaluations, and evidence-based reasoning. These assessment formats are commonly employed in formative classroom assessments to facilitate instruction and learning as well as in high-stakes summative assessments for accountability and admission decisions. While the score represents a key form of feedback, the scoring of such assessment tasks is often costly, time-consuming, and error prone due to the subjectivity of human raters.

**Paragraph 2:**
Automated scoring of performance items is an efficient and scientifically validated technology designed to complement and enhance human scoring (Shermis, 2015). For example, automating the scoring of the National Assessment of Educational Progress (NAEP) CR items could yield significant cost saving of 70% for reading and 40% for math (Justice & Palermo, 2020). As one of the most successful applications of AI technology in educational assessments, the progress in automated scoring is aligned closely with the advances in machine learning and natural language processing (NLP). Though research on automated scoring started with the pioneering work of Page (1966; 2003), recent advances in AI technology have made breakthrough in automated scoring.

**Paragraph 3:**
Automated scoring can be categorized into two main approaches: feature-based and deep learning-based (Haller et al., 2022), with the latter further classified into neural network, small language model (SLM), and large language model (LLM) based approaches. Feature-based approaches rely on the extracted length, prompt, readability, syntactic, semantic, lexical, and discourse features (Ke & Ng, 2019; Uto et al., 2020) and supervised machine learning models. Deep learning-based approaches use word embeddings (Word2Vec, GloVe) and context embeddings from small language models (SLMs) such as BERT, deBERTa based on transformer (Vaswani et al., 2017) and large language models (LLMs) such as GPT, Claude, and Gemini.

**Paragraph 4:**
Developing feature-based or SLM-based automated scoring systems often requires foundational skills in supervised machine learning, NLP, and deep learning. This dramatically reduces the accessibility of automated scoring to classroom learners, teachers, and assessment developers. However, with the swift emerging of more capable LLMs, automated scoring techniques are becoming increasingly accessible to non-technical users who can fully leverage the LLM technology to revamp their routine scoring practices, with enhanced efficiency and accuracy.

**Paragraph 5:**
With the advances in Generative AI or Chatbots, LLMs have been explored for automated scoring in education assessments. LLMs have demonstrated unprecedented potential in automated scoring of essays and CR items in educational assessments (Latif & Zhai, 2024; Lee et al., 2024; Yancey et al., 2023; Yang et al., 2025). In low-stakes assessment programs, three commonly used models are ChatGPT by OpenAI, Claude by Anthropic, and Google Gemini. Recent studies have explored the use of GPT models, such as GPT 3.5 (Bui & Barrot, 2024; Mizumoto & Eguchi, 2023; Parker et al., 2023; Wijekumar et al., 2024) and GPT 4 (Kortemeyer, 2024) in automated scoring. Furthermore, several studies have compared the performance of GPT 3.5 and GPT 4 (Kim & Jo, 2024; Tate et al., 2024) as well as GPT and Llama3 (Kundu & Barbosa, 2024). Pack et al. (2024) compared PaLM 2, Claude 2, and GPT 3.5 and GPT 4, concluding that GPT 4 outperformed the others. Almost all studies on using LLMs for automated scoring purely focused on scoring accuracy, little is known about the potential rater effects of these LLM scoring engines.

**Paragraph 6:**
Rater effects (Myford & Wolfe, 2003, 2004; Saal, Downey, & Lahey, 1980) refer to different types of inconsistencies in ratings when human raters assign scores to test-takers' constructed responses to performance tasks such as essays or CR items in educational assessments. Rater effects may occur due to raters' personal backgrounds, preferences, inaccurate interpretations of the scoring rubrics, inappropriate conceptualization of the target test-takers' population, and their idiosyncratic traits that may impact their accuracy and consistency in assigning scores to assessment items. Rater effects can be classified into different categories. Some common rater effects include rater severity/leniency and centrality. When a rater assigns scores to students' responses to a performance task consistently lower than other raters, this rater effect is noted as rater severity. When rater severity is present, students' true scores may be underestimated if such rater effect is ignored. On the other hand, when a rater assigns scores to students' responses consistently higher than other raters, this rater effect is noted as rater leniency. When rater leniency is present, students' true scores may be overestimated if such rater effect is not accounted for. Further, some raters may consistently assign scores in the middle of the score scale and not assign high scores or low scores regardless of the ability levels. This central tendency or centrality effect will introduce score errors for students whose true scores lie at the two ends of the score scale. Such rater effects are as severe as score accuracy as they may compromise the fairness, reliability, and validity of the assigned scores. Though in operational rating sessions, different strategies would be implemented to minimize rater effects such as standardized rubrics, comprehensive rater training and calibration, in-session and post-session quality control of ratings, or assigning multiple raters to each rating tasks, rater effects need to be tracked as a source of validity evidence.

**Paragraph 7 (Research Questions / Contribution Statement):**
Each LLM has its own strengths and features that may cater to different scoring needs and applications. Like human raters, AI raters may bear different degrees of rater effects. Thus, it is worthwhile to compare the ratings from different scoring engines and understand the potential AI rater effects of each LLM. Thus, this study aims to investigate the AI rater effects in addition to rating accuracy and consistency compared with human raters of essay scoring. The AI raters investigated in this study include ten commonly used LLMs from GPT, Gemini, and Claude families and some recent LLMs such as DeepSeek. The research questions for the study include:
1. How accurate are LLM raters compared with human raters?
2. How consistent or reliable are LLM raters compared with human raters?
3. What are the LLM rater effects compared with human raters?

---

### METHODS

**Overview:**
This study conducts a series of psychometric analyses to investigate the AI raters' scoring accuracy and consistency, as well as uses the Many-Facet Rasch measurement model (Linacre, 1989, 1994, 2024; Wright & Masters, 1982; Wright & Stone, 1979) to investigate and compare rater effects between AI raters and human raters in a large-scale writing assessment.

**Data:**
A dataset consists of 30 student essays on two types of writing tasks. Each essay was scored by two human raters and ten AI raters, including ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3 and DeepSeek R1. The 30 U.S. college students, enrolled in Mandarin Chinese language courses, included 18 third-year and 12 fourth-year students from a range of majors such as business, humanities, STEM, and diplomacy. Data collection took place over two consecutive days using constructed-response writing prompts from the 2021 and 2022 AP Chinese exams developed by the College Board. On the first day, students completed the 2021 prompts, which included one story narration (SN1) task and one email response (ER1) task. On the second day, they responded to the 2022 prompts, which featured the same two task types, each labeled as SN2, and ER2. Two certified human raters of the AP Chinese exam evaluated the writing samples using the College Board's scoring rubrics for both holistic and analytic scoring for three trait scores assessing Task Completion, Delivery, and Language Use. Each student response received both holistic and analytic trait/domain-specific scores ranging from 0 to 6 (Song & Tang, 2025).

**LLMs Trained for Automated Scoring:**
In alignment with the development of LLMs, ChatGPT 3.5 was first used to score all 120 essays and other AI engines were sequentially explored when new versions or new engines were released. Data collection took approximately one and a half years. This study incorporated ten AI raters: ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 2.0, Gemini Advanced 1.5 Pro, DeepSeek V3, and DeepSeek R1. These LLMs are selected based on their popularity and demonstrated expertise in processing text data and reasoning capabilities.

- ChatGPT 3.5: general-purpose tasks, casual writing, and basic coding.
- ChatGPT 4: better at technical problem-solving and creative content; generally outperforms ChatGPT 3.5 in language understanding, with ChatGPT 4 Turbo offering enhanced context handling.
- ChatGPT 4o: excels at conversations.
- OpenAI o1: specializes in advanced STEM applications and debugging.
- Claude 3.5 Sonnet: competitive, often cited in safety-focused evaluations, technical coding, and natural-sounding content.
- Gemini 1.5 and 1.5 Pro: good at long-context tasks.
- Gemini 2.0: selected to reflect the latest advancements in Google's LLMs, which feature enhanced language understanding and improved reasoning for research, education, and multimedia analysis.
- DeepSeek V3: uses the Mixture-of-Experts model, optimized for general-purpose tasks, including natural language understanding, text generation, and conversational AI.
- DeepSeek R1: excels in reasoning; specifically tailored for tasks that require deep reasoning, complex problem-solving, and advanced analytical capabilities.

Before scoring, human rater R1, a certified AP Chinese Language and Culture Exam rater, trained 10 AI engines using AI training protocols designed for evaluating student samples (see Appendix A for an example protocol). As Lee et al. (2024) emphasized, human expert ratings are essential for generating benchmark data that align AI scoring with educational standards. To ensure valid AI rater performance, human rater R1 not only provided training examples drawn from the College Board website and previously scored samples but also offered guidance on applying a holistic scoring approach. AI raters were instructed to prioritize three traits: Task Completion, followed by Delivery and Language Use, in line with official rubrics. In total, 2 human raters and 10 AI raters scored 120 essays across four writing tasks.

**Analysis:**
Using the analytic and holistic scores for the essays, this study investigates scoring accuracy, reliability, and rater effects.

- **Quadratic Weighted Kappa (QWK; Cohen, 1960; 1968)** was computed to evaluate the scoring accuracy of AI raters against the gold standards of human ratings. QWK was computed for each AI against each human rater. AI raters' QWK were compared with the QWK measures from two human raters which were used as the baseline for comparison.

- **Ensemble models:** Multiple ensemble models were explored by removing the worst performing LLMs from the ensemble.
  - AI11 = average of all 10 AI raters
  - AI12 = AI11 minus Gemini 2.0 (A7)
  - AI13 = AI12 minus Gemini 1.5 Pro (A9)
  - AI14 = AI13 minus OpenAI o1 (A6)
  - AI15 = AI14 minus DeepSeek V3 (A8)
  - AI16 = AI15 minus ChatGPT 4.0 (A2) and Gemini 1.5 (A4)

- **Cronbach Alpha** was computed for each AI and human ratings across the three trait scores and holistic scores as a measure of intra-rater consistency.

- **Many-Facet Rasch Model (FACETS):** The FACET model for the rating scale model (Andrich, 1978) is given in equation 1:

  ln(P_jn(x=k) / P_jn(x=k-1)) = θ_j − τ_i − δ_n − β_k

  where θ_j is student j's latent ability estimate, τ_i is rater i's rater effect estimate, δ_n is essay n's difficulty level, β_k is the threshold parameter for score category k. The rating scale version of the FACET model is used (Eckes, 2015; Myford & Wolfe, 2003, 2004), assuming the threshold parameters are the same across all items.

  Facets investigated:
  - Students: 30
  - Essays: 4 (SN1, ER1, SN2, ER2)
  - Raters: 2 human (R1, R2) + 10 AI raters (A1=ChatGPT 3.5, A2=ChatGPT 4, A3=ChatGPT 4o, A4=Gemini 1.5, A5=Claude 3.5 Sonnet, A6=OpenAI o1, A7=Gemini 2.0, A8=DeepSeek V3, A9=Gemini 1.5 Pro, A10=DeepSeek R1)

  Rater effects (severity/leniency) quantified by rater parameter τ_i. Wright maps used to illustrate relative difficulty of essay traits, rater effects, and student ability on the common scale.

  **Fit indices:** Infit mean square (consistency of rating scale use across students and criteria) and outfit mean square (outlier score patterns). Expected value = 1. Good fit range: 0.5–1.5 (Linacre, 2003; Eckes, 2009). Stringent criteria applied in this study: 0.7 and 1.3 (Bond & Fox, 2007; Bond et al., 2021; McNamara, 1996; Muller, 2020; Wright & Linacre, 1994).

---

### RESULTS

#### Scoring Accuracy

**Table 1 — Holistic Scoring Accuracy (QWK) for AI Raters against Each Human Rater:**

Human-human QWK baseline: SN1=0.683, SN2=0.565, ER1=0.684, ER2=0.874

| Rater | SN1-R1 | SN1-R2 | SN2-R1 | SN2-R2 | ER1-R1 | ER1-R2 | ER2-R1 | ER2-R2 |
|---|---|---|---|---|---|---|---|---|
| R1/R2 (human-human) | 0.683 | | 0.565 | | 0.684 | | 0.874 | |
| A1 ChatGPT 3.5 | 0.549 | 0.409 | 0.610 | 0.538 | 0.442 | 0.516 | 0.632 | 0.560 |
| A2 ChatGPT 4 | 0.392 | 0.350 | 0.440 | 0.394 | 0.558 | 0.459 | 0.827 | 0.834 |
| A3 ChatGPT 4o | 0.626 | 0.620 | 0.526 | 0.393 | 0.741 | 0.475 | 0.865 | 0.898 |
| A4 Gemini 1.5 | 0.333 | 0.181 | 0.388 | 0.276 | 0.610 | 0.558 | 0.435 | 0.463 |
| A5 Claude 3.5 | 0.708 | 0.576 | 0.657 | 0.570 | 0.672 | 0.726 | 0.804 | 0.896 |
| A6 OpenAI o1 | 0.422 | 0.302 | 0.557 | 0.369 | 0.543 | 0.304 | 0.656 | 0.584 |
| A7 Gemini 2.0 | 0.201 | 0.131 | 0.319 | 0.199 | 0.289 | 0.143 | 0.716 | 0.619 |
| A8 DeepSeek V3 | 0.378 | 0.233 | 0.610 | 0.439 | 0.619 | 0.448 | 0.664 | 0.667 |
| A9 Gemini 1.5 Pro | 0.267 | 0.169 | 0.698 | 0.576 | 0.631 | 0.640 | 0.590 | 0.537 |
| A10 DeepSeek R1 | 0.579 | 0.522 | 0.417 | 0.293 | 0.453 | 0.368 | 0.727 | 0.703 |
| A11 Ensemble (all 10) | 0.606 | 0.426 | 0.605 | 0.476 | 0.776 | 0.614 | 0.779 | 0.745 |
| A12 = A11 - A7 | 0.630 | 0.474 | 0.720 | 0.535 | 0.783 | 0.671 | 0.805 | 0.764 |
| A13 = A12 - A9 | 0.689 | 0.502 | 0.630 | 0.516 | 0.751 | 0.669 | 0.767 | 0.753 |
| A14 = A13 - A6 | 0.692 | 0.551 | 0.693 | 0.474 | 0.733 | 0.623 | 0.837 | 0.809 |
| A15 = A14 - A8 | 0.665 | 0.513 | 0.630 | 0.516 | 0.681 | 0.685 | 0.815 | 0.790 |
| A16 = A15 - A2 - A4 | 0.688 | 0.588 | 0.675 | 0.563 | 0.647 | 0.675 | 0.812 | 0.790 |

Key findings: For SN1, ChatGPT 4o yielded the highest QWK with R2; Claude 3.5 yielded the highest QWK with R1. For SN2, Gemini 1.5 Pro yielded the highest QWK with both human raters. For ER1, ChatGPT 4o yielded the highest QWK with R1; Claude 3.5 yielded the highest QWK with R2. For ER2, ChatGPT 4o yielded the highest QWK with both human raters. In general, one AI rater achieved higher QWK with one human rater than human-human QWK on every item.

**Table 2 — Analytic (Task Completion) Scoring Accuracy (QWK):** Human-human QWK: SN1=0.715, SN2=0.808, ER1=0.776, ER2=0.915. ChatGPT 4o yielded the highest QWK with both human raters on SN1 and ER2 as well as SN2 with R1. Claude 3.5 yielded the highest QWK with R2 on both SN2 and ER1. Human-human QWK was consistently higher than AI-human QWK on each of the analytic scores.

**Table 3 — Analytic (Delivery) Scoring Accuracy (QWK):** Human-human QWK: SN1=0.685, SN2=0.588, ER1=0.763, ER2=0.950. ChatGPT 4o yielded the highest QWK with both human raters on ER2. Claude 3.5 yielded the highest QWK with each of the two raters on both SN1 and ER1. For SN2, Gemini 1.5 Pro yielded the highest QWK with both human raters. AI-human QWK was consistently higher than human-human QWK on SN tasks and ER1 task except ER2.

**Table 4 — Analytic (Language Use) Scoring Accuracy (QWK):** Human-human QWK: SN1=0.832, SN2=0.488, ER1=0.783, ER2=0.939. ChatGPT 4.0 and 4o yielded the highest QWK with R1 and R2 respectively on ER2. Gemini 1.5 yielded the highest QWK with both raters on ER1. Claude 3.5 yielded the highest QWK with both raters on SN1. For SN2, Gemini 1.5 Pro yielded the highest QWK with both human raters.

**Summary:** No AI rater was always the best performer across all tasks. In general, ChatGPT 4o, Claude 3.5, and Gemini 1.5 Pro yielded the highest performing AI raters depending on the scoring tasks. Ensemble models were able to occasionally improve the scoring accuracy for a specific essay compared with the standalone LLMs.

#### Intra-Rater Consistency (Table 5)

Cronbach Alpha values:

| Rater | Holistic (4 items) | Task Completion (4) | Delivery (4) | Language Use (4) | Analytic (12) | SN (6) | ER (6) |
|---|---|---|---|---|---|---|---|
| R1 | 0.71 | 0.73 | 0.67 | 0.58 | 0.90 | 0.89 | 0.91 |
| R2 | 0.81 | 0.81 | 0.78 | 0.77 | 0.94 | 0.95 | 0.93 |
| A1 ChatGPT 3.5 | 0.71 | 0.66 | 0.73 | 0.72 | 0.92 | 0.91 | 0.89 |
| A2 ChatGPT 4 | 0.66 | 0.64 | 0.64 | 0.58 | 0.89 | 0.92 | 0.79 |
| A3 ChatGPT 4o | 0.81 | 0.80 | 0.79 | 0.58 | 0.91 | 0.90 | 0.90 |
| A4 Gemini 1.5 | 0.46 | 0.60 | 0.63 | 0.58 | 0.88 | 0.90 | 0.86 |
| A5 Claude 3.5 | 0.80 | 0.82 | 0.78 | 0.74 | 0.94 | 0.95 | 0.89 |
| A6 OpenAI o1 | 0.67 | 0.62 | 0.50 | 0.56 | 0.87 | 0.85 | 0.79 |
| A7 Gemini 2.0 | 0.35 | 0.26 | 0.28 | 0.30 | 0.72 | 0.67 | 0.80 |
| A8 DeepSeek V3 | 0.62 | 0.69 | 0.51 | 0.58 | 0.87 | 0.92 | 0.82 |
| A9 Gemini 1.5 Pro | 0.61 | 0.61 | 0.60 | 0.41 | 0.85 | 0.86 | 0.81 |
| A10 DeepSeek R1 | 0.68 | 0.72 | 0.73 | 0.67 | 0.91 | 0.89 | 0.89 |

The top performing AI raters, either ChatGPT 4o or Claude 3.5, still yielded the highest intra-rater consistency across different tasks. The intra-rater consistency for human rater R2 was consistently higher than that for human rater R1. The intra-rater consistency for the best performing AI raters was about the same or higher than R2 except for analytic scores of Language Use and ER essay.

#### AI Rater Effects

**Table 6 — Mean Holistic and Analytic Scores Assigned by Each Rater:**

Key patterns: Human rater R2 assigned higher mean scores across all rating tasks compared with R1. Gemini 2.0 assigned the lowest mean scores on majority of the rating tasks. ChatGPT 3.5 and ChatGPT 4 produced the highest mean scores on majority of the rating tasks.

Selected mean scores (Holistic):
- SN1: R1=3.70, R2=4.10, A1=3.53, A2=3.03, A3=3.73, A4=2.83, A5=3.80, A6=3.17, A7=2.60, A8=3.67, A9=3.33, A10=3.50
- ER1: R1=3.30, R2=3.83, A1=4.30, A2=3.43, A3=2.93, A4=3.43, A5=3.50, A6=2.90, A7=2.37, A8=3.10, A9=3.80, A10=3.57
- SN2: R1=3.23, R2=3.70, A1=3.50, A2=2.97, A3=2.70, A4=2.90, A5=3.10, A6=2.87, A7=2.00, A8=3.47, A9=3.47, A10=3.37
- ER2: R1=3.73, R2=4.07, A1=3.13, A2=3.93, A3=3.77, A4=3.60, A5=3.87, A6=3.10, A7=3.10, A8=3.47, A9=3.20, A10=3.50

**Wright Maps (Figures 1–5):**

- **Figure 1 caption:** "The Wright Map for the Holistic Scores" — For holistic scoring, SN2 was the most difficult essay, while ER2 was the easiest essay. Gemini 2.0 was the most stringent rater (consistent with lowest mean scores) while R2 and ChatGPT 3.5 were more lenient raters.

- **Figure 2 caption:** "The Wright Map for the Analytic Scores" — For analytic scoring across all three traits, SN2 was still the most difficult essay, ER2 was easiest, SN1 was second most difficult. Gemini 2.0 was the most stringent rater; two human raters were the most lenient. Among the three traits, Language Use was the most difficult, while Task Completion was the easiest.

- **Figure 3 caption:** "The Wright Map for the Analytic Scores-Task Completion" — SN2 was still the most difficult essay while SN1 was the easiest. ER1 and ER2 had about the same difficulty. OpenAI o1 was the most stringent rater while two human raters were the most lenient raters. R1 was more lenient than R2 on Task Completion trait scoring.

- **Figure 4 caption:** "The Wright Map for the Analytic Scores-Delivery" — SN2 was still the most difficult essay while ER2 was the easiest essay. Gemini 2.0 was the most stringent rater while R2 was the most lenient raters. R1 was the second most lenient rater like Claude 3.5 and Gemini 1.5 Pro on Delivery trait scoring.

- **Figure 5 caption:** "The Wright Map for the Analytic Scores-Language Use" — SN2 was still the most difficult essay while ER2 was the easiest essay. Gemini 2.0 was the most stringent rater while rater 2 was the most lenient raters. R1 was the second most lenient rater on Language Use trait scoring.

**Table 7 — Rater Parameter Estimates for Holistic Scoring:**

| Rater | Rater Par | SE | Infit MS | Outfit MS |
|---|---|---|---|---|
| R2 | -0.81 | 0.11 | 0.60 | 0.60 |
| ChatGPT 3.5 | -0.37 | 0.11 | 1.36 | 1.36 |
| Claude 3.5 Sonnet | -0.30 | 0.11 | 1.01 | 1.01 |
| R1 | -0.20 | 0.11 | 0.58 | 0.59 |
| DeepSeek R1 | -0.18 | 0.11 | 1.37 | 1.41 |
| Gemini 1.5 Pro | -0.14 | 0.11 | 1.41 | 1.41 |
| DeepSeek V3 | -0.10 | 0.11 | 1.07 | 1.08 |
| ChatGPT 4 | 0.02 | 0.11 | 0.91 | 0.92 |
| ChatGPT 4o | 0.10 | 0.11 | 0.85 | 0.84 |
| Gemini 1.5 | 0.23 | 0.11 | 0.85 | 0.88 |
| OpenAI o1 | 0.50 | 0.11 | 0.70 | 0.69 |
| Gemini 2.0 | 1.25 | 0.11 | 1.22 | 1.29 |

Key findings: Gemini 2.0 was an extreme severe rater (logit = 1.25). ChatGPT 4 was the most neutral rater (parameter ≈ 0). Using cut value of 0.3: all AI raters did not have severe rater effects except ChatGPT 3.5 (-0.37, lenient) and OpenAI o1 (0.5, harsh). The two human raters had the smallest infit and outfit mean squares (both < 0.7), indicating potential central tendency effect. DeepSeek R1, ChatGPT 3.5, and Gemini 1.5 Pro had infit and outfit mean squares > 1.3, indicating potential misfit.

**Table 8 — Rater Parameter Estimates for Analytic Scoring:**

| Rater | Rater Par | SE | Infit MS | Outfit MS |
|---|---|---|---|---|
| R2 | -0.55 | 0.06 | 0.73 | 0.73 |
| R1 | -0.47 | 0.06 | 0.83 | 0.84 |
| ChatGPT 3.5 | -0.31 | 0.06 | 1.21 | 1.20 |
| Gemini 1.5 Pro | -0.29 | 0.06 | 1.19 | 1.19 |
| Claude 3.5 Sonnet | -0.17 | 0.06 | 0.97 | 0.97 |
| ChatGPT 4 | -0.10 | 0.06 | 0.88 | 0.89 |
| DeepSeek V3 | 0.05 | 0.06 | 1.18 | 1.18 |
| DeepSeek R1 | 0.10 | 0.06 | 1.15 | 1.18 |
| ChatGPT 4o | 0.11 | 0.06 | 1.06 | 1.05 |
| Gemini 1.5 | 0.30 | 0.06 | 0.84 | 0.87 |
| OpenAI o1 | 0.57 | 0.06 | 0.69 | 0.69 |
| Gemini 2.0 | 0.76 | 0.06 | 1.21 | 1.26 |

Key findings: Gemini 2.0 was severe (logit = 0.76). DeepSeek V3 was the most neutral rater (parameter ≈ 0.05). All AI raters did not have severe rater effects except OpenAI o1 (0.5, harsh). OpenAI o1 had the least infit and outfit mean squares at the borderline (0.69). No infit and outfit mean squares were larger than 1.3 for any rater.

**Table 9 — Rater Parameter Estimates for Analytic Scoring — Task Completion:**
Two human raters were most lenient (R1: -0.51, R2: -0.36). OpenAI o1 was the most severe rater (logit = 0.61). ChatGPT 4 and Claude 3.5 were more neutral (absolute value < 0.1). All AI raters did not have severe rater effects except OpenAI o1 (0.5), Gemini 1.5 (0.53), and Gemini 2.0 (0.38). No infit or outfit mean squares were < 0.7 or > 1.3.

**Table 10 — Rater Parameter Estimates for Analytic Scoring — Delivery:**
Human rater R2 was most lenient (-0.63). Gemini 2.0 was most severe (rater parameter = 1.03). DeepSeek V3 was most neutral (-0.06). Using absolute cut value of 0.3, OpenAI o1 was a harsh rater (0.68), while Claude 3.5 was slightly lenient (-0.35). No infit and outfit mean squares were < 0.7 or > 1.3.

**Table 11 — Rater Parameter Estimates for Analytic Scoring — Language Use:**
Human rater R2 was most lenient (-0.74), R1 second most lenient (-0.63). Gemini 2.0 was most severe (1.06). DeepSeek R1, ChatGPT 4 and Gemini 1.5 were more neutral (absolute parameter ≈ 0.1). Using absolute cut value of 0.3: DeepSeek V3 (0.54), OpenAI o1 (0.49), and ChatGPT 4o (0.40) were slightly harsh raters; Gemini 1.5 Pro (-0.37) and ChatGPT 3.5 (-0.55) were slightly lenient. OpenAI o1 had infit and outfit mean squares < 0.7 (slight central tendency); ChatGPT 3.5 and Gemini 2.0 yielded infit and outfit mean squares > 1.3 (slight misfit).

---

### SUMMARY AND DISCUSSION (complete)

This study aims to examine the rater effects of LLM-based AI raters in automated scoring. To illustrate the methods for exploring AI rater effects, this study investigated the use of LLMs for automated holistic and analytic scoring using a fully crossed rating design. Ten LLMs were compared including ChatGPT 3.5, ChatGPT 4, ChatGPT 4o, OpenAI o1, Claude 3.5 Sonnet, Gemini 1.5, Gemini 1.5 Pro, Gemini 2.0, as well as DeepSeek V3, and DeepSeek R1 against two human expert raters in scoring two types of writing tasks for the AP Chinese exams. The holistic and analytic score accuracy of LLMs compared with human raters were evaluated in terms of QWK. Intra-rater consistency across essays was compared in terms of Cronbach Alpha. Rater effects of LLMs were evaluated and compared with human raters using the Many FACET Rasch model.

For Research Question 1 related to the AI raters' accuracy, for holistic scoring, ChatGPT 4o, Claude 3.5, and Gemini 1.5 Pro yielded the highest scoring accuracy against either human rater. ChatGPT 4o performed the best on ER items, while Gemini 1.5 Pro excelled on SN items while Claude 3.5 showed strong performance on both SN and ER items. These three LLMs turned out to be the best performing models in analytic scoring as well. For Task Completion, ChatGPT 4o performed the best for SN and ER2 items while Claude 3.5 and Gemini 1.5 Pro performed the best on SN2 and ER1 essays. For Delivery, Claude 3.5 performed the best on SN1 and ER1 while ChatGPT 4o and Gemini 1.5 Pro performed the best on ER2 and SN2 respectively. For the Language Use trait, ChatGPT 4, 4o, and Gemini 1.5 were the top performers on ER essays while Claude 3.5 and Gemini 1.5 Pro were the best performers for SN essays. In general, QWKs for the best performing AI raters were higher than those between two human raters for holistic scoring. However, human-human QWK were higher on analytic scoring than AI QWKs. QWKs for analytic scores were higher than those for holistic scoring.

For Research Question 2 related to the AI raters' intra-rater consistency, ChatGPT 4o yielded the highest intra-rater consistency for the holistic scores, the analytic scores on the Delivery trait, and the ER items. On the other hand, Claude 3.5 yielded the highest consistency for the analytic scores, analytic scores on the Task Completion and Language Use traits as well as the SN items. Human rater R2 yielded higher scoring consistency compared with R1. The best performing AI raters' intra-rater consistency were about the same as those for the best performing human rater except on ER essays and analytic scores on Language Use with slightly lower consistency.

For Research Questions 3 on the rater effects, human raters in general were more lenient. Gemini 2.0 turned out to be a harsh rater on most scoring tasks. ChatGPT 3.5 turned out to be a lenient rater in 3 out of 5 scoring analyses with DeepSeek V3 and Gemini 1.5 Pro as the two other lenient raters. Whether an AI rater was more neutral raters depends on the task. There was no evident central tendency effects for the AI raters. However, the two human raters displayed some minor central tendency effect in holistic scoring. As Wolfe (2004) pointed out, the rater effects estimated in the FACET Rasch model was scaled to a mean of 0. If the number of raters included in the comparison differs, the estimated rater effect may be different.

The results in general support the use of ChatGPT 4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet with high scoring accuracy, better intra-rater consistency, and less rater effects. However, there were no AI raters which consistently performed the best. Some further explorations will be conducted to better understand the AI rater scoring logic. The findings of this study provide insights into the strengths and limitations of AI raters compared to human raters using the data in the study.

---

### LIMITATIONS (complete)

The limitations of the study lies in the sample size, the content domain, the type and the number of essays. There were only 30 students who participated in this experiment. The FACET software manual states a sample size of 30 as a minimum sample size. However, as the FACET Rasch model is an item response theory based latent trait model, a larger sample size would be expected even though the standard error of the rater parameter estimates was relatively small in the current study. Further, the content of the tasks was related to the AP Chinese exam. Whether the findings from this study is generalizable to other content domains such as English writing, reading, science, and math constructed-response items awaits further exploration. In addition, only two items types: SN and ER were included in the experiments, with a total of only 4 items. Other task types and traits for analytic scoring should be examined in future studies. The last limitation is related to the prompting methods for automated scoring using LLMs. The current study used a few-shot methods. Other methods should be explored in future studies including Chain-of-Thought and other fine-tuning methods.

---

### CONCLUSION (final paragraph of Summary and Discussion)

In summary, this study assessed the scoring accuracy, intra-rater consistency of AI and human holistic and analytic ratings, and estimated the AI rater effects. It demonstrated the methods that can be used to examine AI rater performance, in particular, the use of the Many FACET Rasch model to evaluate rater severity/leniency and central tendency effects. This study provided empirical evidence to inform the adoption of LLM-based AI raters for automated holistic and analytic scoring. It is highlighted that when LLMs are used for automated scoring, the methods demonstrated in this study could be the starting point for such evaluation.

---

### ALL FIGURE CAPTIONS

- **Figure 1:** "The Wright Map for the Holistic Scores"
- **Figure 2:** "The Wright Map for the Analytic Scores"
- **Figure 3:** "The Wright Map for the Analytic Scores-Task Completion"
- **Figure 4:** "The Wright Map for the Analytic Scores-Delivery"
- **Figure 5:** "The Wright Map for the Analytic Scores-Language Use"

### ALL TABLE CAPTIONS

- **Table 1:** "Holistic Scoring Accuracy (QWK) for AI Raters against Each Human Rater"
- **Table 2:** "Analytic (Task Completion) Scoring Accuracy (QWK) for AI Raters against Each Human Rater"
- **Table 3:** "Analytic (Delivery) Scoring Accuracy (QWK) for AI Raters against Each Human Rater"
- **Table 4:** "Analytic (Language Use) Scoring Accuracy (QWK) for AI Raters against Each Human Rater"
- **Table 5:** "Intra-Rater Consistency"
- **Table 6:** "Mean Holistic and Analytic Scores Assigned by Each Rater"
- **Table 7:** "Rater Parameter Estimates for Holistic Scoring"
- **Table 8:** "Rater Parameter Estimates for Analytic Scoring"
- **Table 9:** "Rater Parameter Estimates for Analytic Scoring-Task Completion"
- **Table 10:** "Rater Parameter Estimates for Analytic Scoring-Delivery"
- **Table 11:** "Rater Parameter Estimates for Analytic Scoring-Language Use"
- **Table B.1 (Appendix B):** "Standard Deviation of the Holistic and Analytic Scores Assigned by Each Rater"

---

### KEY IMPLEMENTATION DETAILS

- **Prompting method:** Few-shot prompting with training examples. Human rater R1 (certified AP Chinese examiner) designed and executed AI training protocols (Appendix A shows example for SN1 essay type).
- **Scoring rubric:** College Board AP Chinese rubric, 0–6 scale, holistic plus 3 analytic traits (Task Completion, Delivery, Language Use).
- **Training design:** AI raters were given the task prompt, scoring rubric, and student writing samples at multiple score levels as examples before scoring.
- **Scoring design:** Fully crossed rating design — all 12 raters (2 human + 10 AI) scored all 120 essays (30 students × 4 tasks).
- **Analysis software:** FACET software (Linacre, 2024), Version 3.87.0.
- **No ablation studies** were conducted in the traditional ML sense; instead, ensemble models were constructed by progressively removing worst-performing LLMs.
- **Data collection period:** Approximately one and a half years (sequential addition of models as released).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86c3122a-c098-4cbd-8924-e730127d10a9",
  "isSidechain": true,
  "agentId": "aed1d3e555792ca7c",
  "requestId": "req_011CbG3SAcfyL8tyVCzL8oPW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64132a85-79ff-4bf9-9246-aaab9af03160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BeNp6Mm2t4EsaBLtoTdfBF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29610,
      "cache_read_input_tokens": 19542,
      "output_tokens": 11741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11741,
          "cache_read_input_tokens": 19542,
          "cache_creation_input_tokens": 29610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29610,
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
