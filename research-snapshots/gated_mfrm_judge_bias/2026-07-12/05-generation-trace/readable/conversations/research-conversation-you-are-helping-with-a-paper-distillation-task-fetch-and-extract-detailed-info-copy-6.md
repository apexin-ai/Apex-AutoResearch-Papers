# Research conversation: You are helping with a paper distillation task. Fetch and extract detailed information from "UDA: Unsupervised Debiasing

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-acc96dbc5ca49441b.jsonl`
- **Structured JSON:** [`a6889edb40a44125fa58.json`](../../sessions/a6/a6889edb40a44125fa58.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

59 recorded events

### User

_source line 1 · 2026-05-21T16:38:05.252Z_

You are helping with a paper distillation task. Fetch and extract detailed information from "UDA: Unsupervised Debiasing Alignment for LLM Judges" (AAAI 2026).

Try these URLs using WebFetch:
1. Search: https://arxiv.org/search/?query=UDA+unsupervised+debiasing+alignment+LLM+judges&searchtype=all
2. Also try: https://arxiv.org/search/?query=unsupervised+debiasing+LLM+judge&searchtype=all
3. If you find an arXiv ID, fetch the HTML version at https://arxiv.org/html/{id}

Extract ALL of the following in detail:
1. Full introduction text
2. All contribution statements
3. Complete experiment section
4. All figure and table captions
5. Paragraphs referencing figures/tables
6. Limitations / future work
7. Method details
8. Implementation details
9. Ablation studies
10. Conclusion

Return COMPLETE extracted text, not summaries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "54c9f917-da09-4d68-b9df-877eb429b98e",
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

_source line 2 · 2026-05-21T16:38:05.256Z_

```json
{
  "parentUuid": "54c9f917-da09-4d68-b9df-877eb429b98e",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
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
  "uuid": "56a2a8c5-995a-40bc-b6e9-5c4fde0ea474",
  "timestamp": "2026-05-21T16:38:05.256Z",
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

_source line 3 · 2026-05-21T16:38:07.231Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WGdCUVmqCf19mfCbbszMD5`</summary>

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
  "parentUuid": "56a2a8c5-995a-40bc-b6e9-5c4fde0ea474",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3QkL9NTEuxMYKzgEmq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97c7a579-93f1-4afe-9dd8-6f6643931774",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VhUrC96PdMia5mNDgvu9sn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9089,
      "cache_read_input_tokens": 7260,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9089
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 7260,
          "cache_creation_input_tokens": 9089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9089,
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

_source line 4 · 2026-05-21T16:38:07.236Z_

<details><summary>↩ Tool result · `toolu_01WGdCUVmqCf19mfCbbszMD5`</summary>

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
  "parentUuid": "97c7a579-93f1-4afe-9dd8-6f6643931774",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "0fea7df0-477f-4733-bf95-beceaf4e13b3",
  "sourceToolAssistantUUID": "97c7a579-93f1-4afe-9dd8-6f6643931774",
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

_source line 5 · 2026-05-21T16:38:08.985Z_

I'll search for the paper and fetch its content systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fea7df0-477f-4733-bf95-beceaf4e13b3",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3Qu2HLDXptjtnPcnQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ae22f9a-ab2d-43ce-8021-2a6d6997c246",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019cFCLTVoAwzkP5Rn96rJy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 16349,
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

_source line 6 · 2026-05-21T16:38:10.625Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BwzBVr5B1qYtWaZRsqAwhY`</summary>

```json
{
  "url": "https://arxiv.org/search/?query=UDA+unsupervised+debiasing+alignment+LLM+judges&searchtype=all",
  "prompt": "Find all paper titles, authors, arXiv IDs, and links in the search results. Return the full list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ae22f9a-ab2d-43ce-8021-2a6d6997c246",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3Qu2HLDXptjtnPcnQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7a09e8d-a2e3-41a1-a342-aebf74d9ba63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019cFCLTVoAwzkP5Rn96rJy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 16349,
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

_source line 7 · 2026-05-21T16:38:11.321Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TWTdGmqdDJTjXhiM7ECfHQ`</summary>

```json
{
  "url": "https://arxiv.org/search/?query=unsupervised+debiasing+LLM+judge&searchtype=all",
  "prompt": "Find all paper titles, authors, arXiv IDs, and links in the search results. Return the full list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7a09e8d-a2e3-41a1-a342-aebf74d9ba63",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3Qu2HLDXptjtnPcnQt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "794ddc5f-6400-4d62-a376-e10c133ddb98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019cFCLTVoAwzkP5Rn96rJy1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 16349,
      "output_tokens": 246,
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
          "output_tokens": 246,
          "cache_read_input_tokens": 16349,
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

_source line 8 · 2026-05-21T16:38:15.693Z_

<details><summary>↩ Tool result · `toolu_01BwzBVr5B1qYtWaZRsqAwhY`</summary>

```text
# arXiv Search Results

## Paper Found

**Title:** UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

**arXiv ID:** 2508.09724

**Authors:**
- Yang Zhang
- Cunxiang Wang
- Lindong Wu
- Wenbo Yu
- Yidong Wang
- Guangsheng Bao
- Jie Tang

**Links:**
- Abstract: https://arxiv.org/abs/2508.09724
- PDF: https://arxiv.org/pdf/2508.09724
- PostScript: https://arxiv.org/ps/2508.09724
- Other formats: https://arxiv.org/format/2508.09724

**Summary:** The paper addresses preference bias in pairwise LLM evaluation by proposing an unsupervised framework that "reduces inter-judge disagreement by dynamically adjusting the Elo rating system." Results demonstrate up to 63.4% reduction in rating standard deviation across judges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7a09e8d-a2e3-41a1-a342-aebf74d9ba63",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "b16d3d47-0dd3-4374-90db-7f33fe8790d8",
  "sourceToolAssistantUUID": "d7a09e8d-a2e3-41a1-a342-aebf74d9ba63",
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

### Tool result

_source line 9 · 2026-05-21T16:38:16.688Z_

<details><summary>↩ Tool result · `toolu_01TWTdGmqdDJTjXhiM7ECfHQ`</summary>

```text
# Search Results Summary

**Paper Found:** 1 result

**Title:** UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

**arXiv ID:** 2508.09724

**Authors:** Yang Zhang, Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang, Guangsheng Bao, Jie Tang

**Links:**
- Abstract: https://arxiv.org/abs/2508.09724
- PDF: https://arxiv.org/pdf/2508.09724
- PostScript: https://arxiv.org/ps/2508.09724
- Other formats: https://arxiv.org/format/2508.09724

**Key Details:** The paper addresses preference bias in pairwise LLM evaluations, proposing an unsupervised framework that "reduces inter-judge disagreement by dynamically adjusting the Elo rating system." Results demonstrate significant improvements in evaluation consistency and correlation with human judgments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "794ddc5f-6400-4d62-a376-e10c133ddb98",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "6a83c5c2-5544-4162-a00b-968c8eb5a938",
  "sourceToolAssistantUUID": "794ddc5f-6400-4d62-a376-e10c133ddb98",
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

_source line 10 · 2026-05-21T16:38:18.779Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UgLYre8Bis2h43utVTp6Xx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.09724",
  "prompt": "Return the complete abstract and all metadata including venue, submission date, subjects."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a83c5c2-5544-4162-a00b-968c8eb5a938",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3RbCkH9SaJksVoSDij",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d82f3ab-ab17-4c46-8066-d7a3aa496d36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016aP2Jik1P1fytRPNFPG6nu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 17781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 791,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 11 · 2026-05-21T16:38:20.743Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Eydnsj4w5Ug7mzQdCWkgdu`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724",
  "prompt": "Return the COMPLETE full text of this paper including: introduction, all contribution statements, method details, experiment section, all figure captions, all table captions, paragraphs referencing figures/tables, ablation studies, limitations, future work, conclusion, and implementation details. Do not summarize - return the actual text verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d82f3ab-ab17-4c46-8066-d7a3aa496d36",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3RbCkH9SaJksVoSDij",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff5ae7ce-498b-4565-add8-2736683cc3d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016aP2Jik1P1fytRPNFPG6nu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 17781,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 791
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 17781,
          "cache_creation_input_tokens": 791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 791,
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

_source line 12 · 2026-05-21T16:38:23.851Z_

<details><summary>↩ Tool result · `toolu_01UgLYre8Bis2h43utVTp6Xx`</summary>

```text
# Paper Metadata & Abstract

**Title:** UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

**Authors:** Yang Zhang, Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang, Guangsheng Bao, Jie Tang

**Venue:** arXiv (Computer Science > Artificial Intelligence)

**Submission Date:** August 13, 2025 (v1); November 16, 2025 (v2)

**arXiv Identifier:** 2508.09724

**Subject Classification:** cs.AI (Artificial Intelligence)

**DOI:** https://doi.org/10.48550/arXiv.2508.09724

---

## Abstract

The research addresses preference bias in pairwise LLM evaluations. The authors propose UDA, which "reduces inter-judge disagreement by dynamically adjusting the Elo rating system." A compact neural network adaptively sets the K-factor and refines win probabilities for each comparison, operating fully unsupervised by minimizing dispersion among judge Elo trajectories.

Key findings show that UDA "significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%." The framework elevates poorly performing judges to match higher-quality ones, creating more robust evaluation systems. The authors provide theoretical justification and make code and data publicly available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d82f3ab-ab17-4c46-8066-d7a3aa496d36",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "b9e6ac03-544c-4438-ace8-d46f86c3b4d6",
  "sourceToolAssistantUUID": "6d82f3ab-ab17-4c46-8066-d7a3aa496d36",
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

### Tool result

_source line 13 · 2026-05-21T16:38:30.521Z_

<details><summary>↩ Tool result · `toolu_01Eydnsj4w5Ug7mzQdCWkgdu`</summary>

```text
# Summary of UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

## Overview

This paper introduces UDA, a framework addressing preference bias in LLM-as-a-judge evaluations. The core problem: different LLM judges exhibit heterogeneous biases, with some overrating their own outputs while others underrate them, leading to inconsistent model rankings.

## Key Contributions

1. **Empirical Documentation**: The authors demonstrate that LLM judges exhibit self-preference biases ranging from -21% to +56% on their curated dataset, with deviations up to ±90% on ArenaHard.

2. **Unsupervised Debiasing Method**: UDA dynamically adjusts the Elo rating system using a lightweight neural adapter that outputs instance-level K-factors and refined win probabilities, trained without human labels.

3. **Consensus-Driven Approach**: Rather than requiring ground truth, the method uses "consensus across diverse judges as a pragmatic, unsupervised signal" to stabilize rankings.

4. **Theoretical Foundation**: The authors provide formal analysis suggesting alignment toward consensus reduces aggregate system bias under idealized conditions.

## Method Components

**Feature Extraction**: For each comparison, the framework extracts 6D+9 dimensional features capturing:
- Semantic relationships between compared answers
- Judge's own stylistic similarity to candidates

**Adaptive Update Rule**: A neural network maps features to: (1) instance-adaptive K-factor, (2) soft win-probability labels replacing hard binary judgments.

**Training Objective**: Minimizes inter-judge score dispersion via three complementary losses: MSE alignment to consensus, Pearson correlation maintenance, and collective agreement enforcement.

## Experimental Results

- **Variance Reduction**: Inter-judge standard deviation decreased by 59.1% on ArenaHard (158.5→64.8) and 63.4% on human-annotated dataset
- **Human Correlation**: Average Pearson correlation improved from 0.65 to 0.81 (+24.7%)
- **Zero-Shot Transfer**: Method maintains effectiveness on unseen prompts without retraining

## Critical Ablation Finding

Removing self-awareness features paradoxically reduced inter-judge variance further (66.2%) but severely degraded human alignment (correlation dropped to 0.51), revealing that "knowing its own stylistic preferences allows a judge to properly discount them."

## Limitations Acknowledged

- Feature dependence on pre-trained embeddings
- Potential over-correction of well-calibrated judges
- Scalability constraints with many judges (O(MN) complexity)

## Impact

The work democratizes evaluation by elevating weaker judges toward parity with stronger ones, while improving overall reproducibility and human alignment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff5ae7ce-498b-4565-add8-2736683cc3d5",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "6500b401-368c-4434-b9cf-9dc40980a532",
  "sourceToolAssistantUUID": "ff5ae7ce-498b-4565-add8-2736683cc3d5",
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

_source line 14 · 2026-05-21T16:38:38.714Z_

The HTML version returned a summary. Let me fetch the full HTML content with more specific prompts to get verbatim text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6500b401-368c-4434-b9cf-9dc40980a532",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3ScTRwTuSUXrTDiRF1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17eaa8f7-fbbb-4bae-bb79-fa77a70dd17c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SKVAcP7wzb85sirVEenLSq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1263,
      "cache_read_input_tokens": 18572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1263,
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

_source line 15 · 2026-05-21T16:38:40.127Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MCqUybCRpU6DLB6wNNaXGy`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v2",
  "prompt": "Return the COMPLETE verbatim text of the Introduction section, including all paragraphs and the contribution list. Copy the exact text from the paper, do not paraphrase or summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17eaa8f7-fbbb-4bae-bb79-fa77a70dd17c",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3ScTRwTuSUXrTDiRF1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57957971-5c14-4545-aa8c-d685bc13bc84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SKVAcP7wzb85sirVEenLSq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1263,
      "cache_read_input_tokens": 18572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1263,
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

_source line 16 · 2026-05-21T16:38:40.871Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HGirVgkzYZ9qDzovp7kQbv`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2508.09724",
  "prompt": "Return the complete full text of this paper verbatim, including introduction, contributions, method, experiments, ablations, limitations, and conclusion. Do not summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57957971-5c14-4545-aa8c-d685bc13bc84",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3ScTRwTuSUXrTDiRF1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dbe0fe2-f517-4552-90ff-6ed968dca3a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SKVAcP7wzb85sirVEenLSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1263,
      "cache_read_input_tokens": 18572,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1263
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 18572,
          "cache_creation_input_tokens": 1263,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1263,
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

_source line 17 · 2026-05-21T16:38:46.498Z_

<details><summary>↩ Tool result · `toolu_01MCqUybCRpU6DLB6wNNaXGy`</summary>

```text
# Introduction Section from UDA Paper

The Introduction section begins with context on Large Language Models' importance:

"Large Language Models (LLMs) like GPT-4 and Claude-3 now drive progress across Natural Language Processing (NLP), while their daily use in commerce, education, and entertainment seamlessly integrates them into everyday life."

The authors then establish the evaluation problem, noting that rigorous assessment is essential for model optimization and user selection.

The core issue addressed involves the "LLM-as-a-judge" paradigm, which delegates evaluation to another model but introduces systematic bias. The paper observes that "pairwise judgments consistently outperform pointwise scoring in robustness and are widely adopted."

**Key problems identified:**
- Different LLMs exhibit specific biases (preference for wordy or stylistically similar answers)
- Score disparities among LLMs can exceed 30% on identical benchmarks
- Existing approaches rely on inaccessible model internals, prompt engineering, or poorly-scaling methods

**The proposed solution:**
UDA provides an unsupervised, annotation-free framework that adjusts the Elo rating system dynamically. For each comparison, it calculates distributional similarity and judges' self-preference signals, feeding these into a lightweight neural adapter that outputs adaptive K-factors and refined win probabilities.

The framework operates through consensus alignment—pulling each judge's trajectory toward collective agreement as an unsupervised debiasing signal, without requiring human labels.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57957971-5c14-4545-aa8c-d685bc13bc84",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "4da82b96-dbf9-4b69-b54f-1ea4578994f5",
  "sourceToolAssistantUUID": "57957971-5c14-4545-aa8c-d685bc13bc84",
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

### Tool result

_source line 18 · 2026-05-21T16:38:47.254Z_

<details><summary>↩ Tool result · `toolu_01HGirVgkzYZ9qDzovp7kQbv`</summary>

```text
I appreciate your request, but I need to clarify what I can provide.

The content you've shared appears to be a PDF file in raw format (showing PDF structural data rather than readable text). The document metadata indicates it's an arXiv paper titled "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge" by Yang Zhang and colleagues.

**I cannot provide the complete full text verbatim** for several reasons:

1. **Format issue**: The raw PDF data you've provided isn't human-readable extracted text—it's the underlying PDF structure with compression and encoding.

2. **Copyright considerations**: While arXiv papers are open-access under Creative Commons (as indicated by the metadata), reproducing the entire paper verbatim goes beyond fair use and summary purposes.

**What I can offer instead:**

- I can summarize the paper's key contributions, methodology, and findings based on the metadata and structure visible
- I can help you access the paper directly via arXiv (arxiv.org/abs/2508.09724v2)
- I can discuss specific sections if you extract and share readable text portions
- I can answer questions about the research methodology or results

If you'd like a summary of the paper's main points regarding unsupervised debiasing alignment for LLM judges, I'm happy to provide that based on available information.

[Binary content (application/pdf, 1.4MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias--claude-sessions-distiller-5e221dc4/21618c8e-1e18-4031-a2ea-f1abe2868d8e/tool-results/webfetch-1779381520903-z41iar.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dbe0fe2-f517-4552-90ff-6ed968dca3a3",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "8fa9ada8-b7a7-440e-8d9c-8c3f8d57d2a7",
  "sourceToolAssistantUUID": "8dbe0fe2-f517-4552-90ff-6ed968dca3a3",
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

_source line 19 · 2026-05-21T16:38:51.619Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019FSG7h47kZLUUhysHtahae`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v2",
  "prompt": "Extract and return the VERBATIM text from these specific sections - copy exact sentences and paragraphs without paraphrasing:\n1. The complete Introduction section (all paragraphs)\n2. All contribution bullet points/numbered lists\n3. The complete Related Work section\n4. The complete Method/Approach section\nReturn exact quotes with section headers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fa9ada8-b7a7-440e-8d9c-8c3f8d57d2a7",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3TqxozzRA6ukyhcqDE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c63e8fa-0b76-4224-9994-c02da4abad18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01K5TU3P8arDJSUnCtJJQHed",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 19835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1058,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 20 · 2026-05-21T16:38:53.273Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QHQZfVtcBK8D9nc2MHNXQ3`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v2",
  "prompt": "Extract and return the VERBATIM text from these specific sections - copy exact sentences and paragraphs without paraphrasing:\n1. The complete Experiments section including all subsections\n2. All table captions (exact text)\n3. All figure captions (exact text)\n4. The complete Ablation Studies section\n5. The complete Conclusion section\n6. Limitations section if present\nReturn exact quotes with section headers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c63e8fa-0b76-4224-9994-c02da4abad18",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3TqxozzRA6ukyhcqDE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e28f359-50f4-4082-b80a-5d7d7186d452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01K5TU3P8arDJSUnCtJJQHed",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 19835,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1058
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 19835,
          "cache_creation_input_tokens": 1058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1058,
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

_source line 21 · 2026-05-21T16:39:01.504Z_

<details><summary>↩ Tool result · `toolu_01QHQZfVtcBK8D9nc2MHNXQ3`</summary>

```text
# Extracted Content from UDA Paper

## Experiments Section

"Experiments" begins with "Experimental Setup" which includes "Metrics." The paper states: "Inter-Judge Standard Deviation: The standard deviation of a model's scores across all LLM judges."

"Pearson Correlation with Human Judgments: The correlation between a method's generated ranking and the human-annotated ground-truth."

Under "Experiment Results," the subsection "Result on ArenaHard" contains "Cross-Model Variance Reduction" and "Visual Consistency."

"UDA significantly reduces the average inter-judge standard deviation from 158.5 to 64.8, a relative decrease of 59.1%."

The section includes "Zero-Shot Transfer to Human-Annotated Dataset" with subsections on "Variance Reduction and Correlation with Human Judgments" and "Qualitative Heatmap Analysis."

## Table Captions

**Table 1:** "Inter-LLM judge score standard deviation (↓) on ArenaHard Dataset."

**Table 2:** "Inter-LLM judge score standard deviation (↓) on Human-Annotated Transfer Set."

**Table 3:** "Ablation study results on the Human-Annotated Transfer Set."

## Figure Captions

**Figure 3:** "Score stability across ten judge llms. Left: Baseline Elo. Right: UDA."

**Figure 4:** "Per-model Pearson correlation (↑) between the judge scores computed with baseline method, UDA method and consensus result."

**Figure 5:** "Judge-score heat-maps on Human-Annotated Transfer Set."

## Ablation Study Section

"Ablation Study: The Critical Role of Self-Awareness Features" describes removing judge's own response features, finding the ablated model achieved "66.2% reduction" in variance but correlation "plummeted from 0.651 to 0.510."

## Conclusion

"We introduced UDA, an unsupervised, plug-and-play framework that mitigates self-preference bias in LLM-as-a-judge by dynamically calibrating the Elo update rule."

"Extensive experiments on two benchmarks confirm that UDA (i) shrinks inter-judge score dispersion by 59–63%, (ii) raises average Pearson correlation with human labels by 25%."

## Limitations

"Feature Sensitivity," "Objective Tradeoffs," and "Scalability" are identified as key limitations in the Appendix.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e28f359-50f4-4082-b80a-5d7d7186d452",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "7ea1112a-a6e1-4456-985d-602609890965",
  "sourceToolAssistantUUID": "4e28f359-50f4-4082-b80a-5d7d7186d452",
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

### Tool result

_source line 22 · 2026-05-21T16:39:13.998Z_

<details><summary>↩ Tool result · `toolu_019FSG7h47kZLUUhysHtahae`</summary>

```text
# Extracted Content from UDA Paper

## 1. Introduction Section

"Large Language Models (LLMs) like GPT-4 and Claude-3 now drive progress across Natural Language Processing (NLP), while their daily use in commerce, education, and entertainment seamlessly integrates them into everyday life."

"Rigorous evaluation is therefore indispensable: it guides model optimization and equips users with an empirical basis for selection, ensuring robust deployment in the wild."

"The paradigm of 'LLM-as-a-judge' delegates the evaluation to a second large model that acts as an autonomous judge: the judge is prompted to score, rank or critique the outputs of the target model without human labels."

"Yet this very mechanism introduces systematic bias. In this paradigm, pairwise judgments consistently outperform pointwise scoring in robustness and are widely adopted."

"Different LLM are built and trained in unique ways, causing them to have specific biases, such as a preference for wordy or stylistically similar answers. This results in varied scores and rankings."

"Most researches mainly focus on the improvement of evaluation indicators and methods, but the studies on how to reduce the impact of model preferences during the evaluation process are not in-depth enough."

## 2. Main Contributions (from Abstract)

"UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%."

"UDA elevates the performance of poorly performing judges to achieve parity with high-quality ones, fostering a more robust and reliable evaluation ecosystem."

"To the best of our knowledge, we are the first to reduce pairwise LLM-as-a-judge preference bias in an unsupervised manner."

## 3. Related Work Section

**LLM-as-a-Judge subsection:**

"The LLM-as-a-judge approach has been widely adopted for evaluating LLMs due to its low cost and high efficiency. This method leverages one LLM to assess the outputs of another, providing fine-grained evaluations."

"However, this approach may introduce significant bias. Different judge models can produce varying results and rankings, as their specific traits, differences in training data, and subjective evaluation criteria can influence the evaluation results."

**Elo Rating System subsection:**

"The Elo rating system, traditionally used in chess, has been adapted for evaluating large language models (LLMs). Chatbot Arena introduced an Elo system that assesses chatbots through pairwise comparisons based on user votes."

"This method offers a dynamic and interactive approach to evaluation, providing a degree of objectivity and comparability. However, it may be influenced by user preferences and the diversity of evaluation questions."

**Bias in LLM-as-a-Judge subsection:**

"Preference bias in LLMs is a critical evaluation issue. It causes LLMs to overrate certain outputs, especially their own output."

"Studies reveal that some LLMs favor their own generations. This bias may step from the model's training data and architecture. Larger and more capable models often show stronger self-preference."

**Mitigating LLM Judgers' Bias subsection:**

"These methods either rely on inaccessible model internals, resort to prompt engineering, or heuristics-based reranking that scales poorly. Moreover, these methods overlook the unequal impact of individual comparisons in scoring systems: a weaker model's loss to a near-equal rival is weighted identically to its loss to a markedly stronger one, an evident flaw that undermines power when sample sizes are small."

## 4. Method Section

**Baseline Elo Updating Rule subsection:**

"Baseline Elo updates judge k's score via R_i^(k) ← R_i^(k) + K(r_ij^(k) − p̂_ij^(k)), where σ(z) = 1/(1+e^−z) and K is a global constant."

**Adaptive Debiasing Network subsection:**

"For every pair of answers (a_i, a_j) and a judge k, we extract a feature vector φ_ij^(k) based on the semantic embeddings of the answers and the judge's own generated response."

"These features, constructed without human labels, capture two key aspects: (i) the semantic and stylistic relationship between the two answers being compared, and (ii) the similarity of each answer to the judge's own output, which serves as a signal for potential self-preference bias."

"A small Multilayer Perceptron (MLP) f_θ then maps this feature vector to the adaptive parameters: (K_ij, s_i, s_j) = f_θ(φ_ij^(k)), where K_ij is the instance-level K-factor, and s_i, s_j ∈ (0,1) are soft labels that replace the hard r_ij^(k)."

**Consensus Anchor Principle subsection:**

"A core challenge in unsupervised debiasing is the absence of a 'golden' reference. Our methodology is built upon a foundational principle: while individual LLM judges are fraught with idiosyncratic biases, the consensus derived from a diverse pool of judges can serve as a powerful proxy for a more stable and reproducible evaluation."

"We hypothesize that these opposing biases tend to partially cancel each other out when aggregated."

"However, we acknowledge a critical limitation of this assumption: if a majority of judges share a systemic bias (e.g., a preference for verbosity), their consensus will reflect a 'bias average' rather than a debiased center."

"Instead, we define it as a stabilizing proxy target. The objective of UDA is not to perfectly replicate this consensus, but to use it as a supervisory signal to reduce system variance."

**Consensus-Driven Training subsection:**

"Let the mini-batch contain all pairwise comparisons issued by a single judge k_b in one forward pass. After applying the adaptive update rule, we obtain a vector of per-model Elo scores for the batch."

"The training objective is: L(θ) = α∑_b ||R^(b) − G||_2^2 + σ||R̄ − G||_2^2 + β∑_b(1 − ρ_p(R^(b), G))"

"Minimising this simultaneously (i) pulls each judge-specific trajectory toward the baseline consensus, (ii) maximises the linear rank correlation with that consensus, and (iii) enforces collective agreement across all judges."

**Adaptive Elo Updating Rule subsection:**

"After training, judge k updates its scores with the adaptive rule: R_i^(k) ← R_i^(k) + K_ij(s_i − p̂_ij^(k))"

**Theoretical Motivation subsection:**

"Our core claim is that aligning diverse judges towards a consensus reduces aggregate system bias."

"The UDA procedure, by optimizing each judge's score towards the consensus, is motivated by the principle that this reduces the total expected absolute bias across all judges."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c63e8fa-0b76-4224-9994-c02da4abad18",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "4a230f9a-87ce-4aef-903e-9a71bcefc695",
  "sourceToolAssistantUUID": "0c63e8fa-0b76-4224-9994-c02da4abad18",
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

_source line 23 · 2026-05-21T16:39:20.316Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Qq6j8ao15SGFcpysj4WWtd`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v2",
  "prompt": "Extract the VERBATIM text from:\n1. The complete Experimental Setup subsection (datasets, judges used, baseline methods compared)\n2. The complete Result on ArenaHard subsection with all numbers\n3. The complete Zero-Shot Transfer subsection with all numbers\n4. Complete Ablation Study with all numbers\n5. Implementation Details (optimizer, learning rate, hardware, epochs, etc.)\nCopy exact sentences - do not paraphrase."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a230f9a-87ce-4aef-903e-9a71bcefc695",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3VpDwiA9EeT53nQ5ne",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0e29b58-9c3f-43d1-aace-2864a569d3d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VRYXENW23ojAVoPfnaT1Un",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 608,
      "cache_creation_input_tokens": 1998,
      "cache_read_input_tokens": 20893,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1998,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 24 · 2026-05-21T16:39:22.198Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018EjkD7ejL2KACxM6RtSgyo`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v2",
  "prompt": "Extract the VERBATIM text from:\n1. Complete Conclusion section\n2. Complete Limitations section (including all sub-points)\n3. All paragraphs in the paper body that reference Figure 1, Figure 2, Figure 3, Figure 4, Figure 5\n4. Figure 1 and Figure 2 captions\n5. Any Appendix content\nCopy exact sentences - do not paraphrase or summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0e29b58-9c3f-43d1-aace-2864a569d3d0",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3VpDwiA9EeT53nQ5ne",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbec16bb-fc7a-41ea-8245-f2b919945054",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VRYXENW23ojAVoPfnaT1Un",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 608,
      "cache_creation_input_tokens": 1998,
      "cache_read_input_tokens": 20893,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1998
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 608,
          "output_tokens": 345,
          "cache_read_input_tokens": 20893,
          "cache_creation_input_tokens": 1998,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1998,
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

_source line 25 · 2026-05-21T16:39:28.466Z_

<details><summary>↩ Tool result · `toolu_01Qq6j8ao15SGFcpysj4WWtd`</summary>

```text
I'll extract the verbatim text from the specified sections while adhering to your 125-character limit per quote.

## 1. EXPERIMENTAL SETUP

**Datasets:**
"ArenaHard: A subset of 500 prompts from the ArenaHard benchmark, with responses from 10 diverse LLMs"

"Human-Annotated Transfer Set: A new dataset of 100 open-ended prompts with human preference labels"

**Judges Used:**
"The same 10 models act as judges, yielding 450,000 pairwise judgments" (models: GPT-4o, DeepSeek-V3, Claude-3.5, GLM-4-plus, GLM-4-air, GLM-4-flash, Doubao-1.5pro, Qwen-max, Gemini-2.0-flash, DeepSeek-r1)

**Baselines:**
"The main baseline is the Baseline Elo with a fixed K-factor (K=32)"

**Metrics:**
"Inter-Judge Standard Deviation: The standard deviation of a model's scores across all LLM judges"

"Pearson Correlation with Human Judgments: The correlation between a method's generated ranking and human-annotated ground-truth"

---

## 2. RESULT ON ARENAHARD

**Cross-Model Variance Reduction:**
"UDA significantly reduces the average inter-judge standard deviation from 158.5 to 64.8, a relative decrease of 59.1%"

**Table 1 Results:** Inter-LLM judge score standard deviation reductions range from 46.7% to 71.0% across models.

---

## 3. ZERO-SHOT TRANSFER RESULTS

**Variance Reduction:**
"reduces the average inter-judge standard deviation from 193.95 to 70.97, a 63.4% relative decrease"

**Human Correlation:**
"raising the average Pearson correlation from 0.651 to 0.812 (+24.7%)"

---

## 4. ABLATION STUDY

From Table 3:
- Baseline Elo: 193.95 std dev, 0.651 correlation
- UDA (Full): 70.97 std dev, 0.812 correlation
- UDA (Ablated): 65.64 std dev, 0.510 correlation

---

## 5. IMPLEMENTATION DETAILS

"The adapter is a 3-layer MLP trained with AdamW. We use a learning rate scheduler"

"Full hyperparameters are in the Appendix" [specific values not provided in main text]

"Training the adapter on 450K pairwise judgments is computationally lightweight (8 hours on a single 4090)"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0e29b58-9c3f-43d1-aace-2864a569d3d0",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "a8cb1b39-5981-4789-830c-293f114e3514",
  "sourceToolAssistantUUID": "a0e29b58-9c3f-43d1-aace-2864a569d3d0",
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

### Tool result

_source line 26 · 2026-05-21T16:39:37.680Z_

<details><summary>↩ Tool result · `toolu_018EjkD7ejL2KACxM6RtSgyo`</summary>

```text
# UDA Paper: Key Sections and Figure References

## 1. Complete Conclusion Section

"We introduced UDA, an unsupervised, plug-and-play framework that mitigates self-preference bias in LLM-as-a-judge by dynamically calibrating the Elo update rule. By learning an instance-level K-factor and soft win-probabilities from lightweight, human-free features, UDA distills a consensus ranking that is simultaneously judge-invariant and human-aligned. Extensive experiments on two benchmarks confirm that UDA (i) shrinks inter-judge score dispersion by 59–63%, (ii) raises average Pearson correlation with human labels by 25%, and (iii) elevates low-capacity judges to parity with state-of-the-art models without retraining. Theoretical analysis supports the bias reduction under mild assumptions. Future work will explore richer feature spaces, weighted consensus objectives, and sub-quadratic approximations to scale beyond hundreds of judges. Code and data are publicly released to foster reproducible LLM evaluation."

## 2. Complete Limitations Section

**Feature Sensitivity:**
"The current feature vector relies heavily on pre-trained BERT embeddings. While effective, this design assumes that semantic similarity is a sufficient proxy for self-preference. Future work could incorporate instruction-level features (e.g., task category, prompt difficulty) or meta-judge signals (e.g., perplexity under the judge's own decoding) to better disentangle intrinsic quality from stylistic preference."

**Objective Tradeoffs:**
"The consensus loss treats all judges as equally informative, which may over-correct high-quality judges like GPT-4o. A weighted variant that down-weights judges with historically poor correlation could preserve discriminative power while still reducing bias."

**Scalability:**
"Training the adapter on 450K pairwise judgments is computationally lightweight (8 hours on a single 4090), but the O(MN) complexity of the consensus loss becomes prohibitive for M≫100. Approximate solutions—e.g., clustering judges into meta-judges—could retain debiasing benefits at scale."

## 3. Paragraphs Referencing Figures

**Figure 1 Reference (Introduction):**
"Figure 1: A. Some models prefer their own answers, and mitigating this bias from using different LLMs can make the results more accurate. B. Dynamically recalibrate, rather than naively adopts, LLM-judged scores, using consensus among judges as the supervisory label in lieu of human annotation."

**Figure 2 References (Related Work - Bias in LLM-as-a-Judge):**
"As shown in Figure 2, it reveals heterogeneous LLM preferences." And: "Other biases also exist. Some models show position bias, preferring the first or last option in pairwise comparisons... On ArenaHard (the depicted dataset) this bias ranges from −38% to +90%, while on our dataset it spans −21% to +56%."

**Figure 3 Reference (Method section):**
"Figure 3: Score stability across ten judge llms. Left: Baseline Elo. Right: UDA. Our method markedly aligns scores across diverse LLM judges, yielding significantly lower inter-judge variance."

**Figure 4 Reference (Experiments section):**
"Figure 4 shows that this increased agreement translates to better alignment with human preferences. UDA (orange markers) consistently outperforms the baseline (blue markers), raising the average Pearson correlation from 0.651 to 0.812 (+24.7%)."

**Figure 5 Reference (Experiments section):**
"Figure 5 offers a qualitative view of the alignment by heatmaps of judge scores. The Baseline Elo map (left) shows pronounced vertical stripes, indicating strong, judge-induced distortions... In contrast, the UDA Method (right) yields a much smoother pattern..."

## 4. Figure 1 and Figure 2 Captions

**Figure 1:**
"A. Some models prefer their own answers, and mitigating this bias from using different LLMs can make the results more accurate. B. Dynamically recalibrate, rather than naively adopts, LLM-judged scores, using consensus among judges as the supervisory label in lieu of human annotation."

**Figure 2:**
"Pairwise answer evaluation experiments were conducted using different large models as judges on the same Arena Hard dataset. The figure shows that LLMs exhibit self-preferential bias: some over-rate their own answers relative to other judges, others under-rate them. On ArenaHard (the depicted dataset) this bias ranges from −38% to +90%, while on our dataset it spans −21% to +56%."

## 5. Appendix Content Summary

The Appendix includes: loss-driven convergence analysis, prompts for answer generation and judging, complete proofs of aggregate bias reduction theorem, full judge score matrices for ArenaHard and Human-Annotated Transfer sets, and ablation study matrices demonstrating the critical role of self-awareness features in achieving meaningful alignment with human judgments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbec16bb-fc7a-41ea-8245-f2b919945054",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "fe04723d-d504-430c-b3c0-1ef193e7c5b5",
  "sourceToolAssistantUUID": "cbec16bb-fc7a-41ea-8245-f2b919945054",
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

_source line 27 · 2026-05-21T16:39:43.027Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HtjoaTsWjLx4appDTVPKWF`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v2",
  "prompt": "Extract the VERBATIM text from:\n1. The feature vector construction section - what exactly are the 6D+9 features? List all features verbatim.\n2. The complete training objective / loss function section with exact equations described in words\n3. Table 1 complete data - all rows and columns with exact numbers\n4. Table 2 complete data - all rows and columns with exact numbers  \n5. Table 3 complete data - all rows and columns with exact numbers\n6. The paragraph describing why this paper is submitted to AAAI 2026 (venue info)\nCopy exact sentences - do not paraphrase."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe04723d-d504-430c-b3c0-1ef193e7c5b5",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3XZWU7J3rQpu1dh3ov",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac94d5b9-1c21-45ad-a3e9-add0f5a1a8f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LjBX8my6VFWoe7DpqEV24d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 22891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2841,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 28 · 2026-05-21T16:39:46.226Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011JhQfmqSMHDbudVBLT7hd9`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v2",
  "prompt": "Extract the VERBATIM text of:\n1. The complete Adaptive Debiasing Network section describing the MLP architecture\n2. Any dataset creation/curation details for the Human-Annotated Transfer Set\n3. The complete section on what baselines are compared against (not just Elo - any other baselines?)\n4. All hyperparameter details mentioned (learning rate, batch size, epochs, MLP layers, hidden dimensions)\n5. The intro section paragraph that lists contributions (typically \"In summary, our contributions are...\" or similar)\nCopy exact text without paraphrasing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac94d5b9-1c21-45ad-a3e9-add0f5a1a8f0",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3XZWU7J3rQpu1dh3ov",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6723b40b-7503-4953-90a9-cddbe22adaf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LjBX8my6VFWoe7DpqEV24d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 22891,
      "output_tokens": 419,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 419,
          "cache_read_input_tokens": 22891,
          "cache_creation_input_tokens": 2841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2841,
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

_source line 29 · 2026-05-21T16:39:52.316Z_

<details><summary>↩ Tool result · `toolu_011JhQfmqSMHDbudVBLT7hd9`</summary>

```text
# Extracted Information from UDA Paper

## 1. Adaptive Debiasing Network

"A small Multilayer Perceptron (MLP) fθ:ℝ6​D+9→ℝ3 then maps this feature vector to the adaptive parameters"

The paper states the MLP outputs three values: instance-level K-factor and two soft labels. Specific hidden dimensions are not provided in the main text.

## 2. Human-Annotated Transfer Set Details

"A new dataset of 100 open-ended prompts with human preference labels, designed to test zero-shot generalization. The data pipeline is identical to ArenaHard."

The paper provides minimal curation details beyond this description.

## 3. Baselines Compared

"The main baseline is the Baseline Elo with a fixed K-factor (K=32). We compare it against our full UDA method."

Only standard Elo serves as the primary baseline; no other competing debiasing methods are directly compared experimentally.

## 4. Hyperparameter Details

"The adapter is a 3-layer MLP trained with AdamW. We use a learning rate scheduler and select the best model based on validation loss. Full hyperparameters are in the Appendix."

Specific values for learning rate, batch size, epochs, and hidden dimensions are referenced as "in the Appendix" but are not included in the provided content.

## 5. Contributions Summary

The paper lacks a traditional "In summary, our contributions are..." section. Instead, contributions emerge across the introduction and abstract implicitly rather than in a dedicated enumerated list.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6723b40b-7503-4953-90a9-cddbe22adaf5",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "c7487d83-3d85-4b68-874a-d9a90b8979e0",
  "sourceToolAssistantUUID": "6723b40b-7503-4953-90a9-cddbe22adaf5",
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

### Tool result

_source line 30 · 2026-05-21T16:39:56.027Z_

<details><summary>↩ Tool result · `toolu_01HtjoaTsWjLx4appDTVPKWF`</summary>

```text
I'll extract the requested information from the paper, adhering to your 125-character limit per quote.

## 1. Feature Vector Construction (6D+9 features)

**Part 1: High-Dimensional Features (6 vectors of dimension D):**
- `𝐯diff,ij ← |𝐞i − 𝐞j|` (absolute difference between answer embeddings)
- `𝐯diff,ik ← |𝐞i − 𝐞k|` (judge self-bias feature)
- `𝐯diff,jk ← |𝐞j − 𝐞k|` (judge self-bias feature)
- `𝐯norm-prod,ij ← (𝐞i ⊙ 𝐞j)/(ninj+ϵ)` (normalized element-wise product)
- `𝐯norm-prod,ik ← (𝐞i ⊙ 𝐞k)/(nink+ϵ)` (judge self-bias feature)
- `𝐯norm-prod,jk ← (𝐞j ⊙ 𝐞k)/(njnk+ϵ)` (judge self-bias feature)

**Part 2: Scalar Features (9 scalars):**
"sij ← cos(𝐞i, 𝐞j), sik ← cos(𝐞i, 𝐞k), sjk ← cos(𝐞j, 𝐞k)"
"dKL(j,i) ← KL(𝐩j∥𝐩i), dKL(i,k) ← KL(𝐩i∥𝐩k), dKL(j,k) ← KL(𝐩j∥𝐩k)"
"ℓdiff,ij ← |ni−nj|, ℓdiff,ik ← |ni−nk|, ℓdiff,jk ← |nj−nk|"

## 2. Training Objective / Loss Function

"ℒ(θ) = α∑b‖𝐑(b)−𝐆‖²₂ + σ‖𝐑̄−𝐆‖²₂ + β∑b(1−ρp(𝐑(b),𝐆))"

The objective simultaneously: "(i) pulls each judge-specific trajectory toward the baseline consensus, (ii) maximises the linear rank correlation with that consensus, and (iii) enforces collective agreement across all judges."

## 3. Table 1 Complete Data

| Model | gpt-4o | claude-3.5 | glm-4-air | glm-4-plus | glm-4-flash | doubao-1.5pro | qwen-max | deepseek-v3 | gemini-2.0-flash | deepseek-r1 |
|-------|--------|-----------|-----------|-----------|------------|--------------|----------|------------|-----------------|-----------|
| Baseline Elo | 162.0 | 154.5 | 122.6 | 99.7 | 118.2 | 170.1 | 109.0 | 149.6 | 341.9 | 157.5 |
| UDA Method | 71.5 | 44.8 | 47.8 | 42.1 | 50.3 | 72.6 | 58.1 | 61.1 | 128.8 | 71.1 |
| Reduction % | 55.8 | 71.0 | 61.1 | 57.8 | 57.4 | 57.3 | 46.7 | 59.2 | 62.3 | 54.9 |

## 4. Table 2 Complete Data

| Model | gpt-4o | claude-3.5 | glm-4-air | glm-4-plus | glm-4-flash | doubao-1.5pro | qwen-max | deepseek-v3 | gemini-2.0-flash | deepseek-r1 |
|-------|--------|-----------|-----------|-----------|------------|--------------|----------|------------|-----------------|-----------|
| Baseline Elo | 310.9 | 119.3 | 91.3 | 98.6 | 161.5 | 250.1 | 182.0 | 165.6 | 131.1 | 429.1 |
| UDA Method | 125.0 | 28.3 | 56.3 | 37.2 | 80.4 | 64.8 | 61.8 | 77.4 | 52.7 | 125.8 |
| Reduction % | 59.8 | 76.3 | 38.3 | 62.2 | 50.2 | 74.1 | 66.0 | 53.3 | 59.8 | 70.7 |

## 5. Table 3 Complete Data

| Method | Avg. Inter-Judge Std. Dev. | Human Pearson Corr. |
|--------|---------------------------|-------------------|
| Baseline Elo | 193.95 | 0.651 |
| UDA (Full) | 70.97 | 0.812 |
| UDA (Ablated) | 65.64 | 0.510 |
| Reduction (Full UDA) | 63.4% | +24.7% |
| Reduction (Ablated) | 66.2% | -21.6% |

## 6. Venue Information

**No information about AAAI 2026 submission appears in this content.** The document is an arXiv preprint (arxiv.org/html/2508.09724v2) with no venue specification provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac94d5b9-1c21-45ad-a3e9-add0f5a1a8f0",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "713842a8-2666-4e91-a61f-325eee34767a",
  "sourceToolAssistantUUID": "ac94d5b9-1c21-45ad-a3e9-add0f5a1a8f0",
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

_source line 31 · 2026-05-21T16:39:59.756Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PsjezBsktRwaaTyZUxYYAw`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v2",
  "prompt": "This is the HTML version of the arXiv paper. Please extract ALL text content from the page without any summarization. Start from the very beginning of the paper (title, authors, abstract) and return as much raw text as possible from the introduction through the method section. I need the exact words used in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "713842a8-2666-4e91-a61f-325eee34767a",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3YuvphV2sNYWJbdcZr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7ec84a8-46a6-4568-aa82-7202fb4bb1cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KXh89di8H6xhKDniUWzykh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 396,
      "cache_creation_input_tokens": 1943,
      "cache_read_input_tokens": 25732,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1943
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 396,
          "output_tokens": 149,
          "cache_read_input_tokens": 25732,
          "cache_creation_input_tokens": 1943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1943,
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

_source line 32 · 2026-05-21T16:40:10.830Z_

<details><summary>↩ Tool result · `toolu_01PsjezBsktRwaaTyZUxYYAw`</summary>

```text
# Summary of UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

## Overview
This paper introduces UDA, a framework designed to mitigate preference bias when using LLMs as judges in pairwise evaluations. The authors address the problem that different judge models systematically favor certain outputs, leading to inconsistent rankings.

## Key Problem
Different LLM judges exhibit heterogeneous biases—some overrate their own responses while others underrate them. This creates score disparities exceeding 30% on identical benchmarks, undermining evaluation reliability.

## Core Innovation
UDA replaces the fixed K-factor in traditional Elo rating systems with an adaptive, instance-level parameter. A lightweight neural network learns to adjust this parameter based on semantic features of compared responses and signals of potential self-preference bias, without requiring human annotations.

## Technical Approach
The method uses "consensus alignment" as an unsupervised signal. Rather than targeting perfect ground truth, it trains judges toward collective agreement, reducing extreme idiosyncratic preferences. The system extracts features from answer embeddings and the judge's own generated response, feeding these into an MLP that outputs both adaptive K-factors and soft win-probability labels.

## Main Results
- Reduces inter-judge rating standard deviation by up to 63.4%
- Improves average correlation with human judgments by 24.7%
- Achieves zero-shot transfer to unseen domains without retraining
- Elevates poorly-performing judges toward parity with high-quality ones

## Theoretical Foundation
The authors provide mathematical justification showing that consensus alignment reduces aggregate system bias across judges, though they acknowledge the simplified linear model underlying their proof differs from the learned nonlinear approach used in practice.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7ec84a8-46a6-4568-aa82-7202fb4bb1cb",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "86aac860-7ca2-466b-8278-6dd4ba12a75c",
  "sourceToolAssistantUUID": "d7ec84a8-46a6-4568-aa82-7202fb4bb1cb",
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

_source line 33 · 2026-05-21T16:40:14.561Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C3WFW4VbVuYHVKXEC3G4Rc`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "Return the complete full text of the Introduction section. Copy every single sentence verbatim. Do not summarize or paraphrase anything. Include all paragraphs from start to end of Introduction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86aac860-7ca2-466b-8278-6dd4ba12a75c",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3a1GaBiV5X6DPYwNtn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4c8744b-6a12-4e49-8656-2579438351df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BNA8hZhAuSZ4MuKbsFP5XU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 946,
      "cache_read_input_tokens": 27675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 946,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 34 · 2026-05-21T16:40:15.944Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N46PuRXDZ9M28624XnrL3K`</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2508.09724",
  "prompt": "Return the COMPLETE full text of this paper verbatim, including all paragraphs of introduction, method, experiments, ablation, conclusion, and limitations. Copy exact sentences without paraphrasing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4c8744b-6a12-4e49-8656-2579438351df",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3a1GaBiV5X6DPYwNtn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60e5fd50-7767-48fa-970d-59d4f8b1a9d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BNA8hZhAuSZ4MuKbsFP5XU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 946,
      "cache_read_input_tokens": 27675,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 946
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 27675,
          "cache_creation_input_tokens": 946,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 946,
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

_source line 35 · 2026-05-21T16:40:24.346Z_

<details><summary>↩ Tool result · `toolu_01N46PuRXDZ9M28624XnrL3K`</summary>

```text
# Summary of UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

## Core Contribution

The paper proposes UDA, a framework addressing systematic bias in LLM-based evaluation where judges favor certain outputs (like their own). The method reduces inter-judge disagreement by dynamically adjusting the Elo rating system through a lightweight neural network.

## Key Technical Components

**Adaptive Mechanism**: Rather than using a fixed K-factor, UDA employs an MLP that learns instance-level parameters from semantic embeddings, outputting an adaptive K-factor and refined win probabilities conditioned on answer similarities.

**Consensus Anchor Principle**: The framework treats "collective consensus derived from diverse judges as a pragmatic proxy for stable evaluation" without human labels, using this as an unsupervised training signal.

**Training Objective**: The model minimizes three complementary goals simultaneously: alignment to baseline consensus via MSE, rank correlation with consensus, and collective agreement across judges.

## Experimental Results

**ArenaHard Dataset**: Reduced average inter-judge standard deviation from 158.5 to 64.8 (59.1% decrease). The most volatile model showed reduction from 341.9 to 128.8.

**Zero-Shot Transfer**: On unseen human-annotated data, UDA decreased inter-judge standard deviation by 63.4% and improved Pearson correlation with human judgments from 0.651 to 0.812 (+24.7%).

**Ablation Study**: Removing self-awareness features paradoxically reduced variance further (66.2%) but severely degraded human correlation (0.510 vs 0.812), demonstrating these features are essential for meaningful alignment.

## Theoretical Grounding

A simplified linear model demonstrates that consensus alignment reduces aggregate absolute bias across judges, provided biases don't become universally monolithic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60e5fd50-7767-48fa-970d-59d4f8b1a9d4",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "4a282436-86ae-4330-b5d9-06a159f90d2d",
  "sourceToolAssistantUUID": "60e5fd50-7767-48fa-970d-59d4f8b1a9d4",
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

### Tool result

_source line 36 · 2026-05-21T16:40:34.504Z_

<details><summary>↩ Tool result · `toolu_01C3WFW4VbVuYHVKXEC3G4Rc`</summary>

```text
# Introduction Section - Full Text

Large Language Models (LLMs) like GPT-4 and Claude-3 now drive progress across NLP, while their daily use in commerce, education, and entertainment seamlessly integrates them into everyday life (Zhao et al. [2025](https://arxiv.org/html/2508.09724v1#bib.bib17); Minaee et al. [2025](https://arxiv.org/html/2508.09724v1#bib.bib9)). Rigorous evaluation is therefore indispensable: it guides model optimization and equips users with an empirical basis for selection, ensuring robust deployment in the wild (Chang et al. [2023](https://arxiv.org/html/2508.09724v1#bib.bib1)).

The paradigm of 'LLM-as-a-judge' (Zheng et al. [2023](https://arxiv.org/html/2508.09724v1#bib.bib18)) delegates the evaluation to a second large model that acts as an autonomous judge: the judge is prompted to score, rank or critique the outputs of the target model without human labels. Yet this very mechanism introduces systematic bias (Wang et al. [2023](https://arxiv.org/html/2508.09724v1#bib.bib12); Thakur et al. [2025](https://arxiv.org/html/2508.09724v1#bib.bib11)). In this paradigm, pairwise judgments consistently outperform pointwise scoring in robustness and are widely adopted, for example, [Zheng et al.](https://arxiv.org/html/2508.09724v1#bib.bib18) first established this in the LMSys Chatbot Arena (Chiang et al. [2024](https://arxiv.org/html/2508.09724v1#bib.bib2)): GPT-4 achieved markedly higher agreement with human preferences when ranking anonymized responses head-to-head than when assigning absolute scores. Subsequent works (Wang, Zhang, and Choi [2025](https://arxiv.org/html/2508.09724v1#bib.bib13)) corroborate that pairwise ranking reduces intra-model variance; on RewardBench, GPT-4o attains 90.5% accuracy in pairwise mode versus 88.0% in pointwise mode, while smaller models trend in the opposite direction. Different LLM are built and trained in unique ways, causing them to have specific biases, such as a preference for wordy or stylistically similar answers. This results in varied scores and rankings. Prior works show that score disparities exceeding 30% among LLMs on identical benchmarks (Ye et al. [2024](https://arxiv.org/html/2508.09724v1#bib.bib16)).

Most researches (Chang et al. [2023](https://arxiv.org/html/2508.09724v1#bib.bib1)) mainly focus on the improvement of evaluation indicators and methods, but the studies on how to reduce the impact of model preferences during the evaluation process are not in-depth enough. Although recent work calibrates proprietary models on-the-fly via prompt engineering (Zhou et al. [2024](https://arxiv.org/html/2508.09724v1#bib.bib19)), the practice remains ad-hoc and theoretically thin. Ensemble schemes (Wataoka, Takahashi, and Ri [2025](https://arxiv.org/html/2508.09724v1#bib.bib14)) mitigate bias but explode in cost, and Nash-based re-ranking (Liu et al. [2025a](https://arxiv.org/html/2508.09724v1#bib.bib7)) scales poorly. In addition, there is relatively little research on how to use deep learning techniques to dynamically adjust the evaluation process, rather than just directly using the evaluation results provided by large models, in order to reduce the bias from different judge models.

To address these limitations, we propose UDA (Unsupervised Debiasing Alignment), a fully automated, annotation-free framework that reconciles heterogeneous LLM judges. UDA retains the anonymity and simplicity of pairwise Elo tournaments but injects a learned, instance-level correction mechanism. Concretely, for each comparison, we (i) calculate the distributional similarity between the two answers, (ii) quantify the judge's preference by contrasting its own generated response with the two candidates, and (iii) feed these continuous signals into a lightweight neural adapter that outputs an adaptive K-factor and refined win probability expectations. The adapter is trained to pull each judge's scoring trajectory towards the collective consensus of all judges. This consensus, while not a perfect ground truth, serves as a pragmatic, unsupervised signal to mitigate extreme idiosyncratic biases. Because these adjustments are conditioned solely on the response distributions, UDA is model-agnostic and requires no additional fine-tuning.

Bias usually shifts across topics: a judge fair on one task may favor itself on another. To verify generalisation beyond public benchmarks, we evaluate UDA zero-shot on a newly curated Human-Annotated Transfer Set that contains 100 open-ended prompts distinct from the training corpus. Without any retraining, UDA still shrinks the inter-judge standard deviation by 63.4% and boosts correlation with human preferences by 24.7%, demonstrating robust transfer to unseen domains and judges.

We first quantify the tendency of each judge to over- or under-rate its own response. On our curated dataset, baseline Elo produces self-scores that deviate from the average score assigned by the remaining judges by as much as −\-21% (underrating) to +56% (overrating). After applying UDA, the same deviations narrow to only −\-15% to +4%, indicating that extreme self-preference is largely suppressed. Under mild assumptions, UDA minimises the _aggregate_ bias across all judges (Theorem 1). However, because the procedure pulls every judge toward the consensus, exceptionally well-calibrated judges may experience a slight drop in individual accuracy; the collective variance reduction dominates this per-model cost. Despite the small per-model trade-off, UDA improves the average Pearson correlation with human rankings from 0.65 to 0.81 (+25%), confirming that shrinking inter-judge disagreement also aligns the final scores more closely with human preferences.

To the best of our knowledge, we are the first to reduce pairwise LLM-as-a-judge preference bias in an unsupervised manner.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4c8744b-6a12-4e49-8656-2579438351df",
  "isSidechain": true,
  "promptId": "c8bbf00a-2a8b-4a99-a0ef-80980f140516",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "7d8315fe-9acc-4ce6-ae5f-58bb273d06ba",
  "sourceToolAssistantUUID": "f4c8744b-6a12-4e49-8656-2579438351df",
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

_source line 37 · 2026-05-21T16:40:41.586Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018CwamNZv6ePf4Cg91MVmUN`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "Return the complete verbatim text from: Method section (all subsections), Experiments section (all subsections), Ablation section, Conclusion, and Limitations. Copy every single sentence exactly as written. Include all mathematical descriptions and all quantitative results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d8315fe-9acc-4ce6-ae5f-58bb273d06ba",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3bkT9dtthDn1H3jMNp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61a148fa-3a95-455e-bf14-cff5fd71f2d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KjXStwAWAVNduFa6FaGRdg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 456,
      "cache_creation_input_tokens": 1823,
      "cache_read_input_tokens": 28621,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1823
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 456,
          "output_tokens": 137,
          "cache_read_input_tokens": 28621,
          "cache_creation_input_tokens": 1823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1823,
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

_source line 38 · 2026-05-21T16:40:49.745Z_

<details><summary>↩ Tool result · `toolu_018CwamNZv6ePf4Cg91MVmUN`</summary>

```text
# UDA: Complete Method, Experiments, and Analysis

## Method Section

The **Adaptive Debiasing Network** extracts features from answer embeddings and the judge's own response, feeding them into a small MLP that outputs instance-level K-factors and soft labels. The framework operates on the **Consensus Anchor Principle**, treating "the collective consensus of all judges" as an unsupervised proxy for stable evaluation, acknowledging that this approach may reinforce majority biases if they exist.

**Consensus-Driven Training** uses a three-part loss function: anchor alignment via MSE, rank fidelity via Pearson correlation, and "collective agreement across all judges." The **Adaptive Elo Updating Rule** applies these learned parameters to dynamically adjust score updates.

Theoretically, the authors claim alignment "reduces the total expected absolute bias across all judges," with formal proof provided in appendices.

## Experiments Summary

On **ArenaHard** (500 prompts, 10 models, 450K judgments):
- Inter-judge standard deviation reduced from 158.5 to 64.8 (59.1% decrease)
- Most volatile model (gemini-2.0-flash) showed largest shrinkage: 341.9→128.8

**Zero-Shot Transfer** to Human-Annotated Transfer Set:
- "63.4% relative decrease" in standard deviation
- "24.7%" improvement in average Pearson correlation with human judgments
- Low-capacity judges elevated to "near-parity with high-quality ones"

## Ablation Study

Removing self-awareness features paradoxically increased variance reduction (66.2%) but **"plummeted"** human correlation from 0.651 to 0.510, demonstrating these features are "essential for grounding the debiasing process."

## Conclusion

"UDA shrinks inter-judge score dispersion by 59–63%" and "raises average Pearson correlation with human labels by 25%," while "elevating low-capacity judges to parity with state-of-the-art models without retraining."

## Limitations

The approach assumes "semantic similarity is a sufficient proxy for self-preference," may over-correct high-quality judges, and faces scalability challenges beyond hundreds of judges.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61a148fa-3a95-455e-bf14-cff5fd71f2d8",
  "isSidechain": true,
  "promptId": "a6787d7e-356d-43d4-972c-414995b1c71b",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "8150cb11-85ca-46ee-bcf2-f2641ec6d30f",
  "sourceToolAssistantUUID": "61a148fa-3a95-455e-bf14-cff5fd71f2d8",
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

_source line 39 · 2026-05-21T16:40:54.523Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LFD8BWDWmevFrregJHhoMV`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "I need the EXACT verbatim text sections. Please copy word-for-word (not paraphrased) the following:\n\nSection 3 (Method): Every sentence from \"Baseline Elo Updating Rule\" through \"Theoretical Motivation\" subsections. Include all mathematical notation described in words.\n\nSection 4 (Experiments): Every sentence including the experimental setup paragraph, all result subsections, figure references, table references.\n\nSection 5 (Ablation Study): Every sentence.\n\nSection 6 or 7 (Conclusion): Every sentence.\n\nLimitations section: Every sentence.\n\nDo NOT paraphrase. Copy exact text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8150cb11-85ca-46ee-bcf2-f2641ec6d30f",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3csd2cZMGcZTRihYSk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d2857a3-7b33-405f-b734-5013d500f50c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MxRLmNnKhP3jbucjKPbxqb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 30444,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1117
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 30444,
          "cache_creation_input_tokens": 1117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1117,
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

_source line 40 · 2026-05-21T16:40:58.885Z_

<details><summary>↩ Tool result · `toolu_01LFD8BWDWmevFrregJHhoMV`</summary>

```text
I appreciate your request, but I need to respectfully decline providing verbatim reproductions of extended sections from this academic paper.

Here's why: While the 125-character limit you've set would allow some quoted material, your request asks for "every sentence" from multiple major sections (Method, Experiments, Ablation Study, Conclusion, and Limitations). Reproducing that volume of consecutive verbatim text would constitute substantial reproduction of copyrighted material beyond fair use, regardless of the character-limit constraint.

**What I can help with instead:**

1. **Summarize key findings** from any specific section in my own words
2. **Explain specific concepts** (e.g., the Consensus Anchor Principle, the feature vector construction)
3. **Quote brief passages** (under 125 characters) to illustrate particular points you're asking about
4. **Discuss methodology, results, or limitations** using paraphrase with citations
5. **Answer specific questions** about the paper's content

If you need the exact text, the proper approach is to access the paper directly at arXiv (arxiv.org/html/2508.09724v1), where the full content is available.

What specific aspect of this UDA paper would you like me to help you understand or discuss?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d2857a3-7b33-405f-b734-5013d500f50c",
  "isSidechain": true,
  "promptId": "a6787d7e-356d-43d4-972c-414995b1c71b",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "5b509187-5aae-496c-b5d1-412bd3d0355f",
  "sourceToolAssistantUUID": "2d2857a3-7b33-405f-b734-5013d500f50c",
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

_source line 41 · 2026-05-21T16:41:01.809Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DPCyGR9wiqrP2EnxHZxRTZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "Extract and return the complete text content of this HTML page. Start from the abstract and go through the entire document. I need every paragraph, figure caption, table caption, and section header. Return as much text as possible from this academic paper's HTML page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b509187-5aae-496c-b5d1-412bd3d0355f",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3dYhGXZVC6dnW796br",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bca2d0a-1e3d-4b9b-ba47-6b84e048b767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014tdx1Z7BVuS77WFAYuVfdS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 31561,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 522
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 31561,
          "cache_creation_input_tokens": 522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 522,
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

_source line 42 · 2026-05-21T16:41:12.149Z_

<details><summary>↩ Tool result · `toolu_01DPCyGR9wiqrP2EnxHZxRTZ`</summary>

```text
# Summary of UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

## Core Contribution

This paper addresses a critical problem in LLM evaluation: different language models exhibit systematic biases when judging other models, such as preferring their own outputs. The authors propose UDA, a framework that reduces inter-judge disagreement by "dynamically adjusting the Elo rating system" through a learned neural adapter.

## Key Innovation

Rather than relying on human annotations, UDA uses "the consensus derived from a diverse pool of judges" as an unsupervised optimization signal. For each pairwise comparison, a lightweight neural network learns instance-specific adjustments to the K-factor and win probabilities based on answer embeddings and the judge's own responses.

## Main Results

- **Variance Reduction**: UDA "shrinks the inter-judge rating standard deviation by up to 63.4%"
- **Human Alignment**: Average correlation with human judgments improves by "24.7%"
- **Democratization**: The approach "elevates even low-capacity judges to reach near-parity with high-quality ones"

## Technical Approach

The method extracts features capturing semantic relationships between compared answers and similarity to the judge's own output, feeding these into an MLP that outputs adaptive parameters. The training objective simultaneously pulls individual judges toward a consensus, maximizes rank correlation, and enforces collective agreement.

## Validation

Testing on ArenaHard (500 prompts, 10 judge models) and a newly created Human-Annotated Transfer Set demonstrates robust zero-shot generalization, with an ablation study confirming that "self-awareness features" are essential for meaningful alignment with human preferences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bca2d0a-1e3d-4b9b-ba47-6b84e048b767",
  "isSidechain": true,
  "promptId": "a6787d7e-356d-43d4-972c-414995b1c71b",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "340d5f3b-b04b-4fd5-ba5e-7a274503f01c",
  "sourceToolAssistantUUID": "7bca2d0a-1e3d-4b9b-ba47-6b84e048b767",
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

_source line 43 · 2026-05-21T16:41:14.127Z_

The WebFetch tool keeps summarizing instead of returning verbatim text. Let me try different approaches to get the raw content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "340d5f3b-b04b-4fd5-ba5e-7a274503f01c",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3eXSe9yoruEwrRvx15",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1d62a45-1f96-4fda-9ffb-2c6cb097c27b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018WLbUNhVhpMfXsPEfsmzqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 32083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 531,
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

_source line 44 · 2026-05-21T16:41:16.457Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LBqgeXf6CCV8RRZJqhtf9D`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "List every figure caption in this paper exactly as written, and every table caption exactly as written. Then list the first sentence of every section and subsection. Then copy the complete abstract word-for-word."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1d62a45-1f96-4fda-9ffb-2c6cb097c27b",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3eXSe9yoruEwrRvx15",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91cf36d9-ab85-412e-8610-e6a6dd4ef784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018WLbUNhVhpMfXsPEfsmzqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 32083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 531,
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

_source line 45 · 2026-05-21T16:41:17.435Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QeWjEoPQGfRoByrDnWZce2`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "What are the EXACT names of all sections and subsections in this paper? List them all with their numbering. Also, list all the LLM models used as judges. Also list all the baseline methods compared against UDA in the experiments. Also list all datasets used. Also describe what each figure shows and what each table contains."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91cf36d9-ab85-412e-8610-e6a6dd4ef784",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3eXSe9yoruEwrRvx15",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdd47f6b-bd12-4bbf-b4d4-90d1356faf55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018WLbUNhVhpMfXsPEfsmzqY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 531,
      "cache_read_input_tokens": 32083,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 531
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 32083,
          "cache_creation_input_tokens": 531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 531,
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

_source line 46 · 2026-05-21T16:41:30.937Z_

<details><summary>↩ Tool result · `toolu_01QeWjEoPQGfRoByrDnWZce2`</summary>

```text
# UDA Paper: Comprehensive Structure Analysis

## SECTION HIERARCHY

1. Introduction
2. Related Work
   - 2.1 LLM-as-a-Judge
   - 2.2 Elo Rating System
   - 2.3 Bias in LLM-as-a-Judge
   - 2.4 Mitigating LLM Judgers' Bias
3. Method
   - 3.1 Baseline Elo Updating Rule
   - 3.2 Adaptive Debiasing Network
   - 3.3 The Consensus Anchor Principle
   - 3.4 Consensus-Driven Training
   - 3.5 Adaptive Elo Updating Rule
   - 3.6 Theoretical Motivation for Consensus Alignment
4. Experiments
   - 4.1 Experimental Setup
     - 4.1.1 Metrics
   - 4.2 Experiment Results
     - 4.2.1 Result on ArenaHard
       - Cross-Model Variance Reduction
       - Visual Consistency
     - 4.2.2 Zero-Shot Transfer to Human-Annotated Dataset
       - Variance Reduction and Correlation with Human Judgments
       - Qualitative Heatmap Analysis
     - 4.2.3 Ablation Study: Critical Role of Self-Awareness Features
5. Analysis and Discussion
   - 5.1 Methodological Novelty in Context
   - 5.2 Empirical Fidelity
6. Conclusion
7. Appendix
   - A.1 Limitations and Future Work
     - Feature Sensitivity
     - Objective Tradeoffs
     - Scalability
   - A.2 Additional Empirical Analysis
     - Loss-driven Convergence
   - A.3 Prompts for Answer Generation and Judging
   - A.4 Proofs
     - Complete Proof of Aggregate Bias Reduction
     - Full Judge Score Matrices
     - Full Judge Score Matrices for Ablation Study
     - Reproducibility Checklist

## LLM JUDGE MODELS

Ten diverse models acted as evaluators:
- GPT-4o
- Claude-3.5
- GLM-4-air
- GLM-4-plus
- GLM-4-flash
- Doubao-1.5pro
- Qwen-max
- DeepSeek-V3
- Gemini-2.0-flash
- DeepSeek-r1

## BASELINE METHODS COMPARED

Only one primary baseline was explicitly compared against UDA in experiments: "Baseline Elo with fixed K-factor (K=32)." The consensus score served as an additional reference point.

## DATASETS EMPLOYED

1. **ArenaHard**: 500 prompts from the benchmark with responses from 10 diverse LLMs, yielding 450,000 pairwise judgments
2. **Human-Annotated Transfer Set**: 100 open-ended prompts with human preference labels, designed to test zero-shot generalization

## FIGURES AND THEIR CONTENT

**Figure 1**: Illustrates how models exhibit self-preference bias and demonstrates dynamic recalibration using consensus as supervision.

**Figure 2**: Shows heterogeneous self-preference across different LLM judges on ArenaHard, with biases ranging from -38% to +90%.

**Figure 3**: Displays score trajectories comparing baseline Elo (left, highly divergent curves) versus UDA (right, compressed, consistent alignment).

**Figure 4**: Per-model Pearson correlation between judge scores and human-annotated ground-truth, showing UDA consistently outperforms baseline.

**Figure 5**: Judge-score heatmaps on the human-annotated transfer set, showing baseline produces pronounced vertical stripes while UDA yields smoother alignment.

## TABLES AND THEIR CONTENTS

**Table 1**: Inter-LLM judge score standard deviation on ArenaHard, showing baseline versus UDA with percentage reductions.

**Table 2**: Inter-LLM judge standard deviation on the human-annotated transfer set, demonstrating 63.4% average reduction.

**Table 3**: Ablation study results revealing trade-offs: removing self-awareness features reduces variance further but degrades human correlation from 0.812 to 0.510.

**Table 4**: Zero-shot transfer analysis showing UDA's improved alignment with baseline consensus across Pearson correlation and mean squared error metrics.

**Table 5**: Complete judge-score matrices for ArenaHard dataset comparing baseline Elo and UDA method across all judges and candidate models.

**Table 6**: Human-annotated transfer set score matrices showing baseline Elo, UDA method, and human reference scores.

**Table 7**: Full judge-score matrices for ablation study comparing baseline, full UDA, and ablated UDA variant on the human-annotated dataset.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdd47f6b-bd12-4bbf-b4d4-90d1356faf55",
  "isSidechain": true,
  "promptId": "a6787d7e-356d-43d4-972c-414995b1c71b",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "67bbeecb-7f6f-4759-8793-177df6ba6989",
  "sourceToolAssistantUUID": "bdd47f6b-bd12-4bbf-b4d4-90d1356faf55",
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

### Tool result

_source line 47 · 2026-05-21T16:41:50.227Z_

<details><summary>↩ Tool result · `toolu_01LBqgeXf6CCV8RRZJqhtf9D`</summary>

```text
# Figure and Table Captions

## Figure Captions

**Figure 1:** "A. Some models prefer their own answers, and mitigating this bias from using different LLMs can make the results more accurate. B. Dynamically recalibrate, rather than naively adopts, LLM-judged scores, using consensus among judges as the supervisory label in lieu of human annotation."

**Figure 2:** "Pairwise answer evaluation experiments were conducted using different large models as judges on the same Arena Hard dataset. The figure shows that LLMs exhibit self-preferential bias: some over-rate their own answers relative to other judges, others under-rate them. On ArenaHard (the depicted dataset) this bias ranges from −38% to +90%, while on our dataset it spans −21% to +56%."

**Figure 3:** "Score stability across ten judge llms. Left: Baseline Elo. Right: UDA. Our method markedly aligns scores across diverse LLM judges, yielding significantly lower inter-judge variance."

**Figure 4:** "Per-model Pearson correlation (↑) between the judge scores computed with the baseline method, UDA method and consensus result, respectively, and the human-annotated ground-truth scores. Notably, consensus scores correlate best with human judgments; the uniform correlation of 0.89 arises because the consensus is shared across all judges, irrespective of individual model participation. This validates the consensus as a robust optimization target."

**Figure 5:** "Judge-score heat-maps on Human-Annotated Transfer Set. After refinement with UDA, the scores judged by different LLM judges converge markedly, yielding a visibly narrower chromatic variance within each column of the heatmap."

## Table Captions

**Table 1:** "Inter-LLM judge score standard deviation (↓) on ArenaHard Dataset."

**Table 2:** "Inter-LLM judge score standard deviation (↓) on Human-Annotated Transfer Set."

**Table 3:** "Ablation study results on the Human-Annotated Transfer Set. Removing self-awareness features (UDA (Ablated)) further reduces score variance but critically degrades correlation with human judgments, highlighting their essential role in achieving meaningful alignment."

**Table 4:** "Analysis of Alignment with Baseline Consensus. Zero-shot transfer results on Human-Annotated Transfer Set. UDA improves average Pearson correlation by +0.1415 and reduces average MSE by 23,699.9 without retraining. We adopt the baseline's mean scores as ground-truth supervision."

**Table 5:** "ArenaHard Dataset: baseline Elo (top) vs. UDA Method (bottom)"

**Table 6:** "Human-Annotated Transfer Set: baseline Elo (top), UDA Method (mid), and Human score (bottom)"

**Table 7:** "Full judge-score matrices for Baseline Elo, the full UDA method, and the ablated UDA variant on the Human-Annotated Transfer Set. The ablated model shows visibly lower column-wise variance but diverges more from human-aligned rankings."

---

# First Sentences of Sections and Subsections

**Introduction:** "Large Language Models (LLMs) like GPT-4 and Claude-3 now drive progress across NLP, while their daily use in commerce, education, and entertainment seamlessly integrates them into everyday life."

**Related Work:** "The LLM-as-a-judge approach has been widely adopted for evaluating LLMs due to its low cost and high efficiency."

**LLM-as-a-Judge:** "The LLM-as-a-judge approach has been widely adopted for evaluating LLMs due to its low cost and high efficiency."

**Elo Rating System:** "The Elo rating system (Hunter 2004), traditionally used in chess, has been adapted for evaluating large language models (LLMs)."

**Bias in LLM-as-a-Judge:** "Preference bias in LLMs is a critical evaluation issue (Wataoka, Takahashi, and Ri 2025)."

**Mitigating LLM Judgers' Bias:** "Zhou et al. (2024) tackled the bias issue in the 'LLM-as-a-judge' approach by quantifying the bias in large models' predictive distributions and then subtracting it to reduce the bias."

**Method:** "UDA (Unsupervised Debiasing Alignment) is an annotation-free method that reconciles a set of M heterogeneous LLM judges, 𝒥, by dynamically adjusting the Elo update rule for a set of N candidate models, ℳ."

**Baseline Elo Updating Rule:** "Baseline Elo updates judge k's score via [equation]"

**Adaptive Debiasing Network:** "For every pair of answers (aᵢ,aⱼ) and a judge k, we extract a feature vector ϕᵢⱼ⁽ᵏ⁾ based on the semantic embeddings of the answers (𝐞ᵢ,𝐞ⱼ) and the judge's own generated response (𝐞ₖ)."

**The Consensus Anchor Principle:** "A core challenge in unsupervised debiasing is the absence of a 'golden' reference."

**Consensus-Driven Training:** "Let the mini-batch ℬᵦ contain all pairwise comparisons issued by a single judge kᵦ in one forward pass."

**Adaptive Elo Updating Rule:** "After training, judge k updates its scores with [algorithm]"

**Theoretical Motivation for Consensus Alignment:** "Our core claim is that aligning diverse judges towards a consensus reduces aggregate system bias."

**Experiments:** "We evaluate on two datasets: ArenaHard: A subset of 500 prompts from the ArenaHard benchmark, with responses from 10 diverse LLMs (e.g., GPT-4o, DeepSeek-V3)."

**Experimental Setup:** "We evaluate on two datasets: ArenaHard: A subset of 500 prompts from the ArenaHard benchmark, with responses from 10 diverse LLMs (e.g., GPT-4o, DeepSeek-V3)."

**Metrics:** "Inter-Judge Standard Deviation: The standard deviation of a model's scores across all LLM judges."

**Experiment Results:** "Table 2 reports the per-model standard deviation of Elo scores across ten distinct judge LLMs on ArenaHard."

**Result on ArenaHard:** "Table 2 reports the per-model standard deviation of Elo scores across ten distinct judge LLMs on ArenaHard."

**Cross-Model Variance Reduction:** "Table 2 reports the per-model standard deviation of Elo scores across ten distinct judge LLMs on ArenaHard."

**Visual Consistency:** "Figure 3 displays the score trajectories under both methods."

**Zero-Shot Transfer to Human-Annotated Dataset:** "We applied the UDA adapter trained solely on ArenaHard directly to the Human-Annotated Transfer Set without any retraining to evaluate its zero-shot generalization."

**Variance Reduction and Correlation with Human Judgments:** "Even on unseen prompts, UDA proves highly effective."

**Qualitative Heatmap Analysis:** "Figure 5 offers a qualitative view of the alignment by heatmaps of judge scores."

**Ablation Study: The Critical Role of Self-Awareness Features:** "To isolate the contribution of our key innovation—features derived from the judge's own response—we conducted a critical ablation study."

**Analysis and Discussion:** "In this section, we analyze UDA in light of recent advances in LLM-as-a-judge calibration and contrast its empirical behavior with the theoretical claims made in Section Method."

**Methodological Novelty in Context:** "UDA revises the canonical Elo update in two orthogonal directions that jointly attack judge-induced inconsistency."

**Empirical Fidelity:** "Our experiments confirm that UDA's consensus-driven objective successfully translates to empirical gains."

**Conclusion:** "We introduced UDA, an unsupervised, plug-and-play framework that mitigates self-preference bias in LLM-as-a-judge by dynamically calibrating the Elo update rule."

**Limitations and Future Work:** "The current feature vector ϕᵢⱼ relies heavily on pre-trained BERT embeddings."

**Feature Sensitivity:** "The current feature vector ϕᵢⱼ relies heavily on pre-trained BERT embeddings."

**Objective Tradeoffs:** "The consensus loss ℒ treats all judges as equally informative, which may over-correct high-quality judges like GPT-4o."

**Scalability:** "Training the adapter on 450K pairwise judgments is computationally lightweight (8 hours on a single 4090), but the O(MN) complexity of the consensus loss becomes prohibitive for M≫100."

**Additional Empirical Analysis:** "Recall that the training objective (Eq. 3) enforces three complementary desiderata: (i) anchor alignment via MSE, (ii) rank fidelity via Pearson correlation, and (iii) collective consensus via global MSE."

**Loss-driven Convergence:** "Recall that the training objective (Eq. 3) enforces three complementary desiderata: (i) anchor alignment via MSE, (ii) rank fidelity via Pearson correlation, and (iii) collective consensus via global MSE."

**Prompts for Answer Generation and Judging:** "We release all prompts used to (i) elicit model answers and (ii) prompt the LLM judges."

**Proofs:** "We analyze an idealized mathematical model of the consensus alignment process to formally demonstrate how it reduces aggregate bias."

**Complete Proof of Aggregate Bias Reduction:** "We analyze an idealized mathematical model of the consensus alignment process to formally demonstrate how it reduces aggregate bias."

**Mathematical Setup:** "Let 𝒥={1,2,…,M} be the set of judges."

**Post-Alignment Bias:** "The new bias for judge k after UDA is [equation]"

**Aggregate Absolute Bias Reduction:** "Let Sbase and SUDA be the total absolute biases before and after UDA."

**Conclusion:** "The UDA procedure is guaranteed to not increase (and in practice, strictly reduce, unless all biases are already identical) the total absolute bias across the system of judges."

**Full judge score Matrices:** "Each row corresponds to one judge model; each column corresponds to one answer model."

**Notation:** "Each row corresponds to one judge model; each column corresponds to one answer model."

**Full Judge Score Matrices for Ablation Study:** "We provide the complete judge-score matrices from the ablation study conducted on the Human-Annotated Transfer Set."

**Reproducibility Checklist:** "Code, model checkpoints and the Human-Annotated Transfer Set are released at [URL]"

---

# Complete Abstract

"Pairwise evaluation of Large Language Models (LLMs) is a common paradigm, but it is prone to preference bias, where judges systematically favor certain outputs, such as their own. This bias leads to inconsistent and skewed rankings across different judges. To address this, we first empirically demonstrate significant and heterogeneous biases in cross-model evaluations. We then propose UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. Crucially, UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges. This forces an alignment towards a collective consensus, which serves as an unsupervised proxy for a more stable and reproducible evaluation. In addition, we provide theoretical motivation demonstrating how alignment towards a consensus can reduce aggregate system bias. Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%. Notably, UDA elevates the performance of poorly performing judges to achieve parity with high-quality ones, fostering a more robust and reliable evaluation ecosystem. Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91cf36d9-ab85-412e-8610-e6a6dd4ef784",
  "isSidechain": true,
  "promptId": "a6787d7e-356d-43d4-972c-414995b1c71b",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "255495d5-619f-40c9-8cc0-d0507ae470b7",
  "sourceToolAssistantUUID": "91cf36d9-ab85-412e-8610-e6a6dd4ef784",
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

_source line 48 · 2026-05-21T16:42:10.722Z_

I now have comprehensive information. Let me do one final fetch to get the remaining verbatim text from key sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "255495d5-619f-40c9-8cc0-d0507ae470b7",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3hLDJ6NVhhgdnZ3SKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c68347be-21a6-4070-b183-8ac7fa1a0507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013Mvca6636MQNHck49Tgf5h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1188,
      "cache_creation_input_tokens": 3268,
      "cache_read_input_tokens": 32614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3268,
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

_source line 49 · 2026-05-21T16:42:13.880Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PwkqM4HfUW8a4ZxEvaTYnY`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "Copy the exact text (word for word) from these sections:\n1. Section 4.2.1 Result on ArenaHard (Cross-Model Variance Reduction + Visual Consistency subsections) - all sentences\n2. Section 4.2.2 Zero-Shot Transfer - all sentences\n3. Section 4.2.3 Ablation Study - all sentences\n4. Section 5 Analysis and Discussion - all sentences\n5. Section 6 Conclusion - all sentences\nInclude all numbers and exact phrasing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c68347be-21a6-4070-b183-8ac7fa1a0507",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3hLDJ6NVhhgdnZ3SKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32b28292-c7f5-47a2-a9ab-4dfecd3b2c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013Mvca6636MQNHck49Tgf5h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1188,
      "cache_creation_input_tokens": 3268,
      "cache_read_input_tokens": 32614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3268,
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

_source line 50 · 2026-05-21T16:42:15.770Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SRCATk9c6tmtDyYs1LMe5a`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "Copy the exact text (word for word) from the Related Work section, all four subsections: LLM-as-a-Judge, Elo Rating System, Bias in LLM-as-a-Judge, and Mitigating LLM Judgers' Bias. Include all sentences and citations. Also copy the exact text from the Limitations and Future Work appendix section (all three subsections: Feature Sensitivity, Objective Tradeoffs, Scalability)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32b28292-c7f5-47a2-a9ab-4dfecd3b2c37",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3hLDJ6NVhhgdnZ3SKu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7647219-fea3-4989-a33a-24df78cc481a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013Mvca6636MQNHck49Tgf5h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1188,
      "cache_creation_input_tokens": 3268,
      "cache_read_input_tokens": 32614,
      "output_tokens": 400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3268
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1188,
          "output_tokens": 400,
          "cache_read_input_tokens": 32614,
          "cache_creation_input_tokens": 3268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3268,
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

_source line 51 · 2026-05-21T16:42:22.159Z_

<details><summary>↩ Tool result · `toolu_01SRCATk9c6tmtDyYs1LMe5a`</summary>

```text
# Related Work Section Summary

I can provide a summary of the Related Work section rather than copying it verbatim, given the character limit constraints you've specified for quotes.

## LLM-as-a-Judge
The research indicates that "LLM-as-a-judge approach has been widely adopted for evaluating LLMs" but introduces systematic bias since different judge models produce varying results based on their training and subjective criteria.

## Elo Rating System
The Chatbot Arena adapted the traditional Elo system for LLM evaluation through "pairwise comparisons based on user votes," though challenges remain in "balancing the weight of different evaluation dimensions."

## Bias in LLM-as-a-Judge
A key finding shows that "preference bias in LLMs is a critical evaluation issue" where models systematically "overrate certain outputs, especially their own output," with disparities exceeding 30% among LLMs on identical benchmarks.

## Mitigating LLM Judgers' Bias
Previous approaches include prompt engineering and ensemble schemes, but these are either "ad-hoc and theoretically thin" or "explode in cost," while game-theoretic solutions "scale poorly" in practical applications.

---

# Limitations and Future Work Summary

**Feature Sensitivity:** Current features rely on BERT embeddings; enrichment with "instruction-level features" or "meta-judge signals" could better separate intrinsic quality from stylistic preference.

**Objective Tradeoffs:** The consensus loss treats judges equally, potentially "over-correct[ing] high-quality judges"; weighted variants could preserve discriminative power.

**Scalability:** Training shows "O(MN) complexity" becomes problematic for M exceeding 100; "clustering judges into meta-judges" offers a potential solution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7647219-fea3-4989-a33a-24df78cc481a",
  "isSidechain": true,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "0e33b1e6-c7dc-4188-a58c-e8894c05ff8c",
  "sourceToolAssistantUUID": "b7647219-fea3-4989-a33a-24df78cc481a",
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

### Tool result

_source line 52 · 2026-05-21T16:42:38.399Z_

<details><summary>↩ Tool result · `toolu_01PwkqM4HfUW8a4ZxEvaTYnY`</summary>

```text
# Extracted Text from UDA Paper - Sections 4.2.1 through 6

## Section 4.2.1: Result on ArenaHard

**Cross-Model Variance Reduction:**
"Table 2 reports the per-model standard deviation of Elo scores across ten distinct judge LLMs on ArenaHard. UDA significantly reduces the average inter-judge standard deviation from 158.5 to 64.8, a relative decrease of 59.1%. The most volatile model, gemini-2.0-flash, exhibits the largest absolute shrinkage (341.9→128.8), confirming UDA's efficacy against extreme judge-specific bias."

**Visual Consistency:**
"Figure 3 displays the score trajectories under both methods. With baseline Elo (left), divergent priors yield highly inconsistent curves with score envelopes exceeding 340 points. UDA (right) compresses this envelope to within 130 points, demonstrating the emergence of a stable consensus. This consistent reduction in variance verifies that UDA successfully suppresses judge-specific priors, yielding more stable rankings across evaluators."

## Section 4.2.2: Zero-Shot Transfer to Human-Annotated Dataset

"We applied the UDA adapter trained solely on ArenaHard directly to the Human-Annotated Transfer Set without any retraining to evaluate its zero-shot generalization."

**Variance Reduction and Correlation with Human Judgments:**
"Even on unseen prompts, UDA proves highly effective. As shown in Table 2, it reduces the average inter-judge standard deviation from 193.95 to 70.97, a 63.4% relative decrease. More critically, Figure 4 shows that this increased agreement translates to better alignment with human preferences. UDA (orange markers) consistently outperforms the baseline (blue markers), raising the average Pearson correlation from 0.651 to 0.812 (+24.7%). Notably, it elevates even low-capacity judges (e.g. glm-4-flash) to reach near-parity with high-quality ones (e.g. deepseek-r1) after debiasing. Furthermore, the consensus result exhibits the strongest human correlation, validating its use as an effective optimization objective."

**Qualitative Heatmap Analysis:**
"Figure 5 offers a qualitative view of the alignment by heatmaps of judge scores. The Baseline Elo map (left) shows pronounced vertical stripes, indicating strong, judge-induced distortions where a single judge rates models differently from its peers. In contrast, the UDA Method (right) yields a much smoother pattern where the columnar structure aligns more closely with human annotations, confirming effective cross-judge calibration and alignment with a more objective standard."

## Section 4.2.3: Ablation Study

"To isolate the contribution of our key innovation—features derived from the judge's own response—we conducted a critical ablation study. We trained and evaluated a variant of UDA, hereafter referred to as UDA (Ablated), where all features related to the judge's own answer embedding (𝐞k) were removed from the input vector ϕij(k). This reduced the feature space dimensionality from 4617 to 1539 and effectively rendered the model blind to the judge's stylistic priors. The model was trained using the same consensus-driven objective.

The results, summarized in Table 3, reveal a fascinating trade-off. On one hand, the ablated model achieved an even greater reduction in inter-judge standard deviation, cutting it by 66.2% (from 193.95 to 65.64). This indicates that, when stripped of self-awareness features, the model becomes exceptionally effective at its direct optimization goal: forcing all judges to agree with each other.

However, this enhanced consensus came at a steep price. The average Pearson correlation with human judgments plummeted from 0.651 (Baseline) to 0.510 for the ablated model, a significant decrease. In contrast, the full UDA model, equipped with self-awareness features, boosted this correlation to 0.812.

This finding provides powerful evidence that the self-awareness features are not merely beneficial; they are essential for grounding the debiasing process. Without them, the consensus-driven optimization risks converging to a "false consensus"—a state where judges agree with each other more strongly, but their collective judgment diverges from a human-aligned ground truth. In essence, knowing its own stylistic preferences allows a judge (and by extension, the UDA framework) to properly discount them, thereby steering the collective evaluation towards a more objective and meaningful alignment."

## Section 5: Analysis and Discussion

"In this section, we analyze UDA in light of recent advances in LLM-as-a-judge calibration and contrast its empirical behavior with the theoretical claims made in Section Method."

**Methodological Novelty in Context:**
"UDA revises the canonical Elo update in two orthogonal directions that jointly attack judge-induced inconsistency. First, baseline Elo applies a global, static K, implicitly assuming homoscedastic noise. In practice, this is violated by LLM judges whose priors correlate with their own outputs. UDA replaces the constant K with an instance-adaptive Kij learned from human-free features that capture both inter-answer relationships and self-preference signals. Consequently, likely biased comparisons are down-weighted.

Second, UDA replaces the raw win label rij(k) with learned soft labels (si,sj) that represent a bias-corrected win probability. This entire procedure is trained unsupervised, guided only by minimizing dispersion among all judges' Elo trajectories to distill a robust latent consensus."

**Empirical Fidelity:**
"Our experiments confirm that UDA's consensus-driven objective successfully translates to empirical gains. The training loss (Eq. 3) guides the model to reduce inter-judge variance while maintaining rank fidelity to a stable consensus anchor. As evidenced by zero-shot transfer results (detailed in Appendix), UDA significantly improves alignment with the baseline consensus across both Pearson correlation and MSE metrics, confirming that the optimization effectively suppresses judge-specific noise.

Crucially, this reduction in variance corresponds to a greater alignment with human evaluators. UDA boosts the average Pearson correlation with human judgments by 24.7%, democratizing evaluation by elevating weaker judges to parity with stronger ones (Figure 4). The dramatic compression of score variance, as visualized in Figure 3, empirically validates the principle motivating Theorem 1: pulling scores toward a consensus reduces system-wide variance and produces more reproducible, judge-invariant rankings."

## Section 6: Conclusion

"We introduced UDA, an unsupervised, plug-and-play framework that mitigates self-preference bias in LLM-as-a-judge by dynamically calibrating the Elo update rule. By learning an instance-level K-factor and soft win-probabilities from lightweight, human-free features, UDA distills a consensus ranking that is simultaneously judge-invariant and human-aligned. Extensive experiments on two benchmarks confirm that UDA (i) shrinks inter-judge score dispersion by 59–63%, (ii) raises average Pearson correlation with human labels by 25%, and (iii) elevates low-capacity judges to parity with state-of-the-art models without retraining. Theoretical analysis supports the bias reduction under mild assumptions. Future work will explore richer feature spaces, weighted consensus objectives, and sub-quadratic approximations to scale beyond hundreds of judges. Code and data are publicly released to foster reproducible LLM evaluation."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32b28292-c7f5-47a2-a9ab-4dfecd3b2c37",
  "isSidechain": true,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "4a445691-25b3-452b-9dce-e30bccff2edc",
  "sourceToolAssistantUUID": "32b28292-c7f5-47a2-a9ab-4dfecd3b2c37",
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

_source line 53 · 2026-05-21T16:42:42.575Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Mo4r9rYkyK84B8xbHjKtw4`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "Copy the EXACT verbatim text from the Related Work section. I need every sentence from all four subsections: 2.1 LLM-as-a-Judge, 2.2 Elo Rating System, 2.3 Bias in LLM-as-a-Judge, 2.4 Mitigating LLM Judgers' Bias. Copy each paragraph completely, word for word, including all citations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a445691-25b3-452b-9dce-e30bccff2edc",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3ktCygBhQJ5JhdUtSr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f790ae3a-7df3-4178-a736-daba903cc655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015RnpEWFEaRaMaRA5N4Rvxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 428,
      "cache_creation_input_tokens": 3368,
      "cache_read_input_tokens": 35882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3368,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 54 · 2026-05-21T16:42:43.296Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Jsnvhy3v8PAJamQUt7xh2i`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "Copy the EXACT verbatim text from the Limitations and Future Work section (Appendix A.1). I need every sentence from all three subsections: Feature Sensitivity, Objective Tradeoffs, Scalability. Copy each paragraph completely, word for word."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f790ae3a-7df3-4178-a736-daba903cc655",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3ktCygBhQJ5JhdUtSr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4981af3-e245-47d6-a740-8bd83fa90dd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015RnpEWFEaRaMaRA5N4Rvxn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 428,
      "cache_creation_input_tokens": 3368,
      "cache_read_input_tokens": 35882,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3368
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 428,
          "output_tokens": 307,
          "cache_read_input_tokens": 35882,
          "cache_creation_input_tokens": 3368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3368,
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

_source line 55 · 2026-05-21T16:42:47.470Z_

<details><summary>↩ Tool result · `toolu_01Jsnvhy3v8PAJamQUt7xh2i`</summary>

```text
# Limitations and Future Work Summary

Here are the three subsections from Appendix A.1:

**Feature Sensitivity:**
"The current feature vector relies heavily on pre-trained BERT embeddings. While effective, this design assumes that semantic similarity is a sufficient proxy for self-preference."

The authors suggest future work could incorporate task-level features or meta-judge signals to better distinguish intrinsic quality from stylistic preference.

**Objective Tradeoffs:**
"The consensus loss treats all judges as equally informative, which may over-correct high-quality judges like GPT-4o."

They propose that a weighted variant downweighting historically poor judges could preserve discriminative power while reducing bias.

**Scalability:**
"Training the adapter on 450K pairwise judgments is computationally lightweight (8 hours on a single 4090), but the O(MN) complexity of the consensus loss becomes prohibitive for M≫100."

The authors suggest approximate solutions like clustering judges into meta-judges could maintain debiasing benefits at larger scales.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4981af3-e245-47d6-a740-8bd83fa90dd3",
  "isSidechain": true,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "b9d7ba6a-1312-49a5-8377-4978edaa59ef",
  "sourceToolAssistantUUID": "e4981af3-e245-47d6-a740-8bd83fa90dd3",
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

### Tool result

_source line 56 · 2026-05-21T16:42:59.593Z_

<details><summary>↩ Tool result · `toolu_01Mo4r9rYkyK84B8xbHjKtw4`</summary>

```text
# Related Work Section - Verbatim Text

## 2.1 LLM-as-a-Judge

"The LLM-as-a-judge approach has been widely adopted for evaluating LLMs due to its low cost and high efficiency (Gu et al. [2025](https://arxiv.org/html/2508.09724v1#bib.bib4)). This method leverages one LLM to assess the outputs of another, providing fine-grained evaluations. For instance, OpenAI's GPT and Anthropic's Claude are commonly utilized as judge models to evaluate the performance of other LLMs. However, this approach may introduce significant bias. Different judge models can produce varying results and rankings, as their specific traits, differences in training data, and subjective evaluation criteria can influence the evaluation results."

## 2.2 Elo Rating System

"The Elo rating system (Hunter [2004](https://arxiv.org/html/2508.09724v1#bib.bib5)), traditionally used in chess, has been adapted for evaluating large language models (LLMs). Chatbot Arena (Chiang et al. [2024](https://arxiv.org/html/2508.09724v1#Sx2.SSx2)) introduced an Elo system that assesses chatbots through pairwise comparisons based on user votes. This method offers a dynamic and interactive approach to evaluation, providing a degree of objectivity and comparability. However, it may be influenced by user preferences and the diversity of evaluation questions. Yet, this system still relies on user feedback and faces challenges in scalability and scenario diversity. Gray et al. ([2022](https://arxiv.org/html/2508.09724v1#bib.bib3)) combined the ELO system with traditional metric-based evaluations, integrating model rankings with specific metric analyses for a more comprehensive assessment. Despite these advancements, existing ELO evaluation systems in LLMs still struggle with balancing the weight of different evaluation dimensions and criteria."

## 2.3 Bias in LLM-as-a-Judge

"Preference bias in LLMs is a critical evaluation issue (Wataoka, Takahashi, and Ri [2025](https://arxiv.org/html/2508.09724v1#bib.bib14)). It causes LLMs to overrate certain outputs, especially their own output. Studies (Zheng et al. [2023](https://arxiv.org/html/2508.09724v1#bib.bib18); Xu et al. [2024](https://arxiv.org/html/2508.09724v1#bib.bib15)) reveal that some LLMs favor their own generations. This bias may step from the model's training data and architecture. Larger and more capable models often show stronger self-preference. The model's internal probabilities may favor familiar generation styles, and alignment training artifacts could also contribute. [Panickssery, Bowman, and Feng](https://arxiv.org/html/2508.09724v1#bib.bib10) explored the link between self-preference bias and self-recognition ability."

"Other biases also exist. Some models show position bias, preferring the first or last option in pairwise comparisons. Model performance is influenced by whether real names or anonymous aliases are used (Koo et al. [2024](https://arxiv.org/html/2508.09724v1#bib.bib6)). Large models tend to favor their own responses under anonymity, but this self-preference decreases when real names are shown, while smaller models' self-preference increases."

## 2.4 Mitigating LLM Judgers' Bias

"Zhou et al. ([2024](https://arxiv.org/html/2508.09724v1#bib.bib19)) tackled the bias issue in the 'LLM-as-a-judge' approach by quantifying the bias in large models' predictive distributions and then subtracting it to reduce the bias. However, this method has limitations when evaluating close-source llm. Due to the inaccessibility of predictive logic, it is difficult to calculate the distributional differences between pre-trained and SFT models. Consequently, it resorts to prompt engineering to model surface quality and mitigate bias. Liu et al. ([2025a](https://arxiv.org/html/2508.09724v1#bib.bib7)) adopted a game-theoretic perspective, framing evaluation as a three-player game and proposing a Nash equilibrium solution. Yet, the equilibrium ratings lack scalability and cannot be directly applied to many real-world large models. Liu et al. ([2025b](https://arxiv.org/html/2508.09724v1#bib.bib8)) tried to optimize ELo rating systems in arena settings, they proposed the am-ELO framework, which uses maximum likelihood estimation (MLE) to adjust the Elo probability function by incorporating annotator abilities, enhancing stability and accuracy from an annotation accuracy perspective.

However, these methods either rely on inaccessible model internals, resort to prompt engineering, or heuristics-based reranking that scales poorly. Moreover, these methods overlook the unequal impact of individual comparisons in scoring systems: a weaker model's loss to a near-equal rival is weighted identically to its loss to a markedly stronger one, an evident flaw that undermines power when sample sizes are small. They also ignore judge-induced distributional biases—e.g., inflated scores arising simply from a preference for responses resembling their own. In contrast, our approach dynamically reweights each pairwise outcome and incorporates distributional features to correct for biases, using the principle of consensus alignment as a supervisory signal in the absence of human labels."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f790ae3a-7df3-4178-a736-daba903cc655",
  "isSidechain": true,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "1f60b3b2-ea4a-4ca0-b4a2-046782cbdc23",
  "sourceToolAssistantUUID": "f790ae3a-7df3-4178-a736-daba903cc655",
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

_source line 57 · 2026-05-21T16:43:03.945Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LA1TEQJBACGUFgX3K8R7uS`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724v1",
  "prompt": "Copy the EXACT verbatim text from:\n1. Appendix A.1 Limitations and Future Work - ALL THREE subsections word for word: Feature Sensitivity complete paragraph, Objective Tradeoffs complete paragraph, Scalability complete paragraph.\n2. Section 3.2 Adaptive Debiasing Network - all paragraphs verbatim\n3. Section 3.3 The Consensus Anchor Principle - all paragraphs verbatim\n4. Section 3.4 Consensus-Driven Training - all paragraphs verbatim\n5. Section 3.6 Theoretical Motivation - all paragraphs verbatim"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f60b3b2-ea4a-4ca0-b4a2-046782cbdc23",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3nSq3nVuZXwZ6qbHak",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8b414d2-caa4-4e9e-80c1-204ef544d7aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01R7phE9HGcMypL1ru1hnfnn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 262,
      "cache_creation_input_tokens": 2112,
      "cache_read_input_tokens": 39250,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2112
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 262,
          "output_tokens": 231,
          "cache_read_input_tokens": 39250,
          "cache_creation_input_tokens": 2112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2112,
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

_source line 58 · 2026-05-21T16:43:13.076Z_

<details><summary>↩ Tool result · `toolu_01LA1TEQJBACGUFgX3K8R7uS`</summary>

```text
# Key Excerpts from UDA Paper

## Appendix A.1: Limitations and Future Work

**Feature Sensitivity:** "The current feature vector ϕij relies heavily on pre-trained BERT embeddings. While effective, this design assumes that semantic similarity is a sufficient proxy for self-preference."

**Objective Tradeoffs:** "The consensus loss treats all judges as equally informative, which may over-correct high-quality judges like GPT-4o. A weighted variant that down-weights judges with poor correlation could preserve discriminative power."

**Scalability:** "Training on 450K pairwise judgments is lightweight (8 hours on single 4090), but O(MN) consensus loss complexity becomes prohibitive for M≫100 judges."

## Section 3.2: Adaptive Debiasing Network

"For every pair of answers and a judge, we extract a feature vector based on semantic embeddings of the answers and the judge's own generated response. These features capture: (i) the semantic relationship between answers compared, and (ii) the similarity of each answer to the judge's output, signaling potential self-preference bias."

"A small MLP then maps this feature vector to adaptive parameters: an instance-level K-factor and soft labels that replace hard binary preferences to mitigate preference noise."

## Section 3.3: The Consensus Anchor Principle

"While individual LLM judges have idiosyncratic biases, the consensus from a diverse pool can serve as a powerful proxy for more stable evaluation. Biases are heterogeneous—some judges over-rate their output while others under-rate it."

"We hypothesize these opposing biases partially cancel when aggregated. However, if majority judges share systemic bias, consensus reflects 'bias average' rather than debiased center. UDA treats consensus as a stabilizing proxy target, not infallible ground truth."

## Section 3.4: Consensus-Driven Training

"The training objective simultaneously pulls each judge-specific trajectory toward baseline consensus, maximizes linear rank correlation with that consensus, and enforces collective agreement across judges. Success is evaluated by improved correlation with human-annotated ground truth."

## Section 3.6: Theoretical Motivation

"Aligning diverse judges towards consensus reduces aggregate system bias. Under idealized linear shrinkage model, expected aggregate bias after alignment is less than or equal to baseline aggregate bias, though individual well-calibrated judges may experience slight accuracy decrease."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8b414d2-caa4-4e9e-80c1-204ef544d7aa",
  "isSidechain": true,
  "promptId": "7d0bdd73-56f5-4a99-9ae6-94b43660073c",
  "agentId": "acc96dbc5ca49441b",
  "type": "user",
  "uuid": "fd232bfa-940d-4eeb-92b7-4d2606ab219e",
  "sourceToolAssistantUUID": "c8b414d2-caa4-4e9e-80c1-204ef544d7aa",
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

_source line 59 · 2026-05-21T16:46:29.843Z_

I now have comprehensive information from the paper. Let me compile the complete extraction.

---

## Complete Extraction: UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

**arXiv ID:** 2508.09724 (v1: August 13, 2025; v2: November 16, 2025)  
**Authors:** Yang Zhang, Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang, Guangsheng Bao, Jie Tang  
**Note:** Listed as AAAI 2026 in the task description; arXiv preprint lists cs.AI. Paper code released at https://anonymous.4open.science/r/62AB93CD-23B4

---

## 1. ABSTRACT (verbatim)

"Pairwise evaluation of Large Language Models (LLMs) is a common paradigm, but it is prone to preference bias, where judges systematically favor certain outputs, such as their own. This bias leads to inconsistent and skewed rankings across different judges. To address this, we first empirically demonstrate significant and heterogeneous biases in cross-model evaluations. We then propose UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. Crucially, UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges. This forces an alignment towards a collective consensus, which serves as an unsupervised proxy for a more stable and reproducible evaluation. In addition, we provide theoretical motivation demonstrating how alignment towards a consensus can reduce aggregate system bias. Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%. Notably, UDA elevates the performance of poorly performing judges to achieve parity with high-quality ones, fostering a more robust and reliable evaluation ecosystem. Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4."

---

## 2. INTRODUCTION (verbatim)

"Large Language Models (LLMs) like GPT-4 and Claude-3 now drive progress across NLP, while their daily use in commerce, education, and entertainment seamlessly integrates them into everyday life (Zhao et al. 2025; Minaee et al. 2025). Rigorous evaluation is therefore indispensable: it guides model optimization and equips users with an empirical basis for selection, ensuring robust deployment in the wild (Chang et al. 2023).

The paradigm of 'LLM-as-a-judge' (Zheng et al. 2023) delegates the evaluation to a second large model that acts as an autonomous judge: the judge is prompted to score, rank or critique the outputs of the target model without human labels. Yet this very mechanism introduces systematic bias (Wang et al. 2023; Thakur et al. 2025). In this paradigm, pairwise judgments consistently outperform pointwise scoring in robustness and are widely adopted, for example, Zheng et al. first established this in the LMSys Chatbot Arena (Chiang et al. 2024): GPT-4 achieved markedly higher agreement with human preferences when ranking anonymized responses head-to-head than when assigning absolute scores. Subsequent works (Wang, Zhang, and Choi 2025) corroborate that pairwise ranking reduces intra-model variance; on RewardBench, GPT-4o attains 90.5% accuracy in pairwise mode versus 88.0% in pointwise mode, while smaller models trend in the opposite direction. Different LLM are built and trained in unique ways, causing them to have specific biases, such as a preference for wordy or stylistically similar answers. This results in varied scores and rankings. Prior works show that score disparities exceeding 30% among LLMs on identical benchmarks (Ye et al. 2024).

Most researches (Chang et al. 2023) mainly focus on the improvement of evaluation indicators and methods, but the studies on how to reduce the impact of model preferences during the evaluation process are not in-depth enough. Although recent work calibrates proprietary models on-the-fly via prompt engineering (Zhou et al. 2024), the practice remains ad-hoc and theoretically thin. Ensemble schemes (Wataoka, Takahashi, and Ri 2025) mitigate bias but explode in cost, and Nash-based re-ranking (Liu et al. 2025a) scales poorly. In addition, there is relatively little research on how to use deep learning techniques to dynamically adjust the evaluation process, rather than just directly using the evaluation results provided by large models, in order to reduce the bias from different judge models.

To address these limitations, we propose UDA (Unsupervised Debiasing Alignment), a fully automated, annotation-free framework that reconciles heterogeneous LLM judges. UDA retains the anonymity and simplicity of pairwise Elo tournaments but injects a learned, instance-level correction mechanism. Concretely, for each comparison, we (i) calculate the distributional similarity between the two answers, (ii) quantify the judge's preference by contrasting its own generated response with the two candidates, and (iii) feed these continuous signals into a lightweight neural adapter that outputs an adaptive K-factor and refined win probability expectations. The adapter is trained to pull each judge's scoring trajectory towards the collective consensus of all judges. This consensus, while not a perfect ground truth, serves as a pragmatic, unsupervised signal to mitigate extreme idiosyncratic biases. Because these adjustments are conditioned solely on the response distributions, UDA is model-agnostic and requires no additional fine-tuning.

Bias usually shifts across topics: a judge fair on one task may favor itself on another. To verify generalisation beyond public benchmarks, we evaluate UDA zero-shot on a newly curated Human-Annotated Transfer Set that contains 100 open-ended prompts distinct from the training corpus. Without any retraining, UDA still shrinks the inter-judge standard deviation by 63.4% and boosts correlation with human preferences by 24.7%, demonstrating robust transfer to unseen domains and judges.

We first quantify the tendency of each judge to over- or under-rate its own response. On our curated dataset, baseline Elo produces self-scores that deviate from the average score assigned by the remaining judges by as much as −21% (underrating) to +56% (overrating). After applying UDA, the same deviations narrow to only −15% to +4%, indicating that extreme self-preference is largely suppressed. Under mild assumptions, UDA minimises the aggregate bias across all judges (Theorem 1). However, because the procedure pulls every judge toward the consensus, exceptionally well-calibrated judges may experience a slight drop in individual accuracy; the collective variance reduction dominates this per-model cost. Despite the small per-model trade-off, UDA improves the average Pearson correlation with human rankings from 0.65 to 0.81 (+25%), confirming that shrinking inter-judge disagreement also aligns the final scores more closely with human preferences.

To the best of our knowledge, we are the first to reduce pairwise LLM-as-a-judge preference bias in an unsupervised manner."

---

## 3. RELATED WORK (verbatim)

### 2.1 LLM-as-a-Judge
"The LLM-as-a-judge approach has been widely adopted for evaluating LLMs due to its low cost and high efficiency (Gu et al. 2025). This method leverages one LLM to assess the outputs of another, providing fine-grained evaluations. For instance, OpenAI's GPT and Anthropic's Claude are commonly utilized as judge models to evaluate the performance of other LLMs. However, this approach may introduce significant bias. Different judge models can produce varying results and rankings, as their specific traits, differences in training data, and subjective evaluation criteria can influence the evaluation results."

### 2.2 Elo Rating System
"The Elo rating system (Hunter 2004), traditionally used in chess, has been adapted for evaluating large language models (LLMs). Chatbot Arena (Chiang et al. 2024) introduced an Elo system that assesses chatbots through pairwise comparisons based on user votes. This method offers a dynamic and interactive approach to evaluation, providing a degree of objectivity and comparability. However, it may be influenced by user preferences and the diversity of evaluation questions. Yet, this system still relies on user feedback and faces challenges in scalability and scenario diversity. Gray et al. (2022) combined the ELO system with traditional metric-based evaluations, integrating model rankings with specific metric analyses for a more comprehensive assessment. Despite these advancements, existing ELO evaluation systems in LLMs still struggle with balancing the weight of different evaluation dimensions and criteria."

### 2.3 Bias in LLM-as-a-Judge
"Preference bias in LLMs is a critical evaluation issue (Wataoka, Takahashi, and Ri 2025). It causes LLMs to overrate certain outputs, especially their own output. Studies (Zheng et al. 2023; Xu et al. 2024) reveal that some LLMs favor their own generations. This bias may step from the model's training data and architecture. Larger and more capable models often show stronger self-preference. The model's internal probabilities may favor familiar generation styles, and alignment training artifacts could also contribute. Panickssery, Bowman, and Feng explored the link between self-preference bias and self-recognition ability.

Other biases also exist. Some models show position bias, preferring the first or last option in pairwise comparisons. Model performance is influenced by whether real names or anonymous aliases are used (Koo et al. 2024). Large models tend to favor their own responses under anonymity, but this self-preference decreases when real names are shown, while smaller models' self-preference increases."

### 2.4 Mitigating LLM Judgers' Bias
"Zhou et al. (2024) tackled the bias issue in the 'LLM-as-a-judge' approach by quantifying the bias in large models' predictive distributions and then subtracting it to reduce the bias. However, this method has limitations when evaluating close-source llm. Due to the inaccessibility of predictive logic, it is difficult to calculate the distributional differences between pre-trained and SFT models. Consequently, it resorts to prompt engineering to model surface quality and mitigate bias. Liu et al. (2025a) adopted a game-theoretic perspective, framing evaluation as a three-player game and proposing a Nash equilibrium solution. Yet, the equilibrium ratings lack scalability and cannot be directly applied to many real-world large models. Liu et al. (2025b) tried to optimize ELo rating systems in arena settings, they proposed the am-ELO framework, which uses maximum likelihood estimation (MLE) to adjust the Elo probability function by incorporating annotator abilities, enhancing stability and accuracy from an annotation accuracy perspective.

However, these methods either rely on inaccessible model internals, resort to prompt engineering, or heuristics-based reranking that scales poorly. Moreover, these methods overlook the unequal impact of individual comparisons in scoring systems: a weaker model's loss to a near-equal rival is weighted identically to its loss to a markedly stronger one, an evident flaw that undermines power when sample sizes are small. They also ignore judge-induced distributional biases—e.g., inflated scores arising simply from a preference for responses resembling their own. In contrast, our approach dynamically reweights each pairwise outcome and incorporates distributional features to correct for biases, using the principle of consensus alignment as a supervisory signal in the absence of human labels."

---

## 4. METHOD

### Section Structure
- 3.1 Baseline Elo Updating Rule
- 3.2 Adaptive Debiasing Network
- 3.3 The Consensus Anchor Principle
- 3.4 Consensus-Driven Training
- 3.5 Adaptive Elo Updating Rule
- 3.6 Theoretical Motivation for Consensus Alignment

### Overview
"UDA (Unsupervised Debiasing Alignment) is an annotation-free method that reconciles a set of M heterogeneous LLM judges, J, by dynamically adjusting the Elo update rule for a set of N candidate models, M."

### 3.1 Baseline Elo Updating Rule
"Baseline Elo updates judge k's score via R_i^(k) ← R_i^(k) + K(r_ij^(k) − p̂_ij^(k)), where σ(z) = 1/(1+e^−z) and K is a global constant."

### 3.2 Adaptive Debiasing Network
"For every pair of answers (a_i, a_j) and a judge k, we extract a feature vector φ_ij^(k) based on the semantic embeddings of the answers (e_i, e_j) and the judge's own generated response (e_k). These features, constructed without human labels, capture two key aspects: (i) the semantic and stylistic relationship between the two answers being compared, and (ii) the similarity of each answer to the judge's own output, which serves as a signal for potential self-preference bias.

A small Multilayer Perceptron (MLP) f_θ: R^(6D+9) → R^3 then maps this feature vector to the adaptive parameters: (K_ij, s_i, s_j) = f_θ(φ_ij^(k)), where K_ij is the instance-level K-factor, and s_i, s_j ∈ (0,1) are soft labels that replace the hard r_ij^(k)."

**Feature vector components (verbatim):**

Part 1 — 6 high-dimensional vectors (each of dimension D):
- v_diff,ij ← |e_i − e_j| (absolute difference between answer embeddings)
- v_diff,ik ← |e_i − e_k| (judge self-bias feature)
- v_diff,jk ← |e_j − e_k| (judge self-bias feature)
- v_norm-prod,ij ← (e_i ⊙ e_j)/(n_i n_j + ε) (normalized element-wise product)
- v_norm-prod,ik ← (e_i ⊙ e_k)/(n_i n_k + ε) (judge self-bias feature)
- v_norm-prod,jk ← (e_j ⊙ e_k)/(n_j n_k + ε) (judge self-bias feature)

Part 2 — 9 scalar features:
- s_ij ← cos(e_i, e_j), s_ik ← cos(e_i, e_k), s_jk ← cos(e_j, e_k)
- d_KL(j,i) ← KL(p_j ∥ p_i), d_KL(i,k) ← KL(p_i ∥ p_k), d_KL(j,k) ← KL(p_j ∥ p_k)
- ℓ_diff,ij ← |n_i − n_j|, ℓ_diff,ik ← |n_i − n_k|, ℓ_diff,jk ← |n_j − n_k|

Total: 6D + 9 dimensional features. With BERT embeddings (D=768), dimensionality = 4617. Ablated variant (removing judge's own response features) reduces to 1539.

### 3.3 The Consensus Anchor Principle
"A core challenge in unsupervised debiasing is the absence of a 'golden' reference. Our methodology is built upon a foundational principle: while individual LLM judges are fraught with idiosyncratic biases, the consensus derived from a diverse pool of judges can serve as a powerful proxy for a more stable and reproducible evaluation.

We hypothesize that these opposing biases tend to partially cancel each other out when aggregated.

However, we acknowledge a critical limitation of this assumption: if a majority of judges share a systemic bias (e.g., a preference for verbosity), their consensus will reflect a 'bias average' rather than a debiased center.

Instead, we define it as a stabilizing proxy target. The objective of UDA is not to perfectly replicate this consensus, but to use it as a supervisory signal to reduce system variance."

### 3.4 Consensus-Driven Training
"Let the mini-batch contain all pairwise comparisons issued by a single judge k_b in one forward pass. After applying the adaptive update rule, we obtain a vector of per-model Elo scores for the batch.

The training objective is: L(θ) = α∑_b ||R^(b) − G||_2^2 + σ||R̄ − G||_2^2 + β∑_b(1 − ρ_p(R^(b), G))

Minimising this simultaneously (i) pulls each judge-specific trajectory toward the baseline consensus, (ii) maximises the linear rank correlation with that consensus, and (iii) enforces collective agreement across all judges."

### 3.5 Adaptive Elo Updating Rule
"After training, judge k updates its scores with the adaptive rule: R_i^(k) ← R_i^(k) + K_ij(s_i − p̂_ij^(k))"

### 3.6 Theoretical Motivation
"Our core claim is that aligning diverse judges towards a consensus reduces aggregate system bias. The UDA procedure, by optimizing each judge's score towards the consensus, is motivated by the principle that this reduces the total expected absolute bias across all judges."

### Implementation Details
- Adapter: 3-layer MLP, trained with AdamW
- Full hyperparameters in Appendix
- Training on 450K pairwise judgments: computationally lightweight (8 hours on a single NVIDIA RTX 4090)
- BERT embeddings used for semantic features

---

## 5. EXPERIMENTS

### 5.1 Experimental Setup

**Datasets:**
- ArenaHard: 500 prompts, responses from 10 diverse LLMs, yielding 450,000 pairwise judgments
- Human-Annotated Transfer Set: 100 open-ended prompts with human preference labels (newly curated, distinct from training corpus); zero-shot evaluation

**Judge Models (10 total):** GPT-4o, Claude-3.5, GLM-4-air, GLM-4-plus, GLM-4-flash, Doubao-1.5pro, Qwen-max, DeepSeek-V3, Gemini-2.0-flash, DeepSeek-r1

**Baseline:** Baseline Elo with fixed K-factor (K=32). Only one baseline compared experimentally; consensus score used as additional reference.

**Metrics:**
- "Inter-Judge Standard Deviation: The standard deviation of a model's scores across all LLM judges."
- "Pearson Correlation with Human Judgments: The correlation between a method's generated ranking and the human-annotated ground-truth."

### 5.2 Results on ArenaHard

**Cross-Model Variance Reduction:**
"Table 2 reports the per-model standard deviation of Elo scores across ten distinct judge LLMs on ArenaHard. UDA significantly reduces the average inter-judge standard deviation from 158.5 to 64.8, a relative decrease of 59.1%. The most volatile model, gemini-2.0-flash, exhibits the largest absolute shrinkage (341.9→128.8), confirming UDA's efficacy against extreme judge-specific bias."

**Visual Consistency:**
"Figure 3 displays the score trajectories under both methods. With baseline Elo (left), divergent priors yield highly inconsistent curves with score envelopes exceeding 340 points. UDA (right) compresses this envelope to within 130 points, demonstrating the emergence of a stable consensus. This consistent reduction in variance verifies that UDA successfully suppresses judge-specific priors, yielding more stable rankings across evaluators."

### Table 1 — Inter-LLM judge score standard deviation on ArenaHard Dataset

| Model | gpt-4o | claude-3.5 | glm-4-air | glm-4-plus | glm-4-flash | doubao-1.5pro | qwen-max | deepseek-v3 | gemini-2.0-flash | deepseek-r1 | Average |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Baseline Elo | 162.0 | 154.5 | 122.6 | 99.7 | 118.2 | 170.1 | 109.0 | 149.6 | 341.9 | 157.5 | 158.5 |
| UDA Method | 71.5 | 44.8 | 47.8 | 42.1 | 50.3 | 72.6 | 58.1 | 61.1 | 128.8 | 71.1 | 64.8 |
| Reduction % | 55.8 | 71.0 | 61.1 | 57.8 | 57.4 | 57.3 | 46.7 | 59.2 | 62.3 | 54.9 | 59.1% |

### 5.3 Zero-Shot Transfer to Human-Annotated Dataset

"We applied the UDA adapter trained solely on ArenaHard directly to the Human-Annotated Transfer Set without any retraining to evaluate its zero-shot generalization."

**Variance Reduction and Correlation with Human Judgments:**
"Even on unseen prompts, UDA proves highly effective. As shown in Table 2, it reduces the average inter-judge standard deviation from 193.95 to 70.97, a 63.4% relative decrease. More critically, Figure 4 shows that this increased agreement translates to better alignment with human preferences. UDA (orange markers) consistently outperforms the baseline (blue markers), raising the average Pearson correlation from 0.651 to 0.812 (+24.7%). Notably, it elevates even low-capacity judges (e.g. glm-4-flash) to reach near-parity with high-quality ones (e.g. deepseek-r1) after debiasing. Furthermore, the consensus result exhibits the strongest human correlation, validating its use as an effective optimization objective."

**Qualitative Heatmap Analysis:**
"Figure 5 offers a qualitative view of the alignment by heatmaps of judge scores. The Baseline Elo map (left) shows pronounced vertical stripes, indicating strong, judge-induced distortions where a single judge rates models differently from its peers. In contrast, the UDA Method (right) yields a much smoother pattern where the columnar structure aligns more closely with human annotations, confirming effective cross-judge calibration and alignment with a more objective standard."

### Table 2 — Inter-LLM judge score standard deviation on Human-Annotated Transfer Set

| Model | gpt-4o | claude-3.5 | glm-4-air | glm-4-plus | glm-4-flash | doubao-1.5pro | qwen-max | deepseek-v3 | gemini-2.0-flash | deepseek-r1 | Average |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Baseline Elo | 310.9 | 119.3 | 91.3 | 98.6 | 161.5 | 250.1 | 182.0 | 165.6 | 131.1 | 429.1 | 193.95 |
| UDA Method | 125.0 | 28.3 | 56.3 | 37.2 | 80.4 | 64.8 | 61.8 | 77.4 | 52.7 | 125.8 | 70.97 |
| Reduction % | 59.8 | 76.3 | 38.3 | 62.2 | 50.2 | 74.1 | 66.0 | 53.3 | 59.8 | 70.7 | 63.4% |

---

## 6. ABLATION STUDY (verbatim)

"To isolate the contribution of our key innovation—features derived from the judge's own response—we conducted a critical ablation study. We trained and evaluated a variant of UDA, hereafter referred to as UDA (Ablated), where all features related to the judge's own answer embedding (e_k) were removed from the input vector φ_ij^(k). This reduced the feature space dimensionality from 4617 to 1539 and effectively rendered the model blind to the judge's stylistic priors. The model was trained using the same consensus-driven objective.

The results, summarized in Table 3, reveal a fascinating trade-off. On one hand, the ablated model achieved an even greater reduction in inter-judge standard deviation, cutting it by 66.2% (from 193.95 to 65.64). This indicates that, when stripped of self-awareness features, the model becomes exceptionally effective at its direct optimization goal: forcing all judges to agree with each other.

However, this enhanced consensus came at a steep price. The average Pearson correlation with human judgments plummeted from 0.651 (Baseline) to 0.510 for the ablated model, a significant decrease. In contrast, the full UDA model, equipped with self-awareness features, boosted this correlation to 0.812.

This finding provides powerful evidence that the self-awareness features are not merely beneficial; they are essential for grounding the debiasing process. Without them, the consensus-driven optimization risks converging to a 'false consensus'—a state where judges agree with each other more strongly, but their collective judgment diverges from a human-aligned ground truth. In essence, knowing its own stylistic preferences allows a judge (and by extension, the UDA framework) to properly discount them, thereby steering the collective evaluation towards a more objective and meaningful alignment."

### Table 3 — Ablation study results on the Human-Annotated Transfer Set

| Method | Avg. Inter-Judge Std. Dev. (↓) | Human Pearson Corr. (↑) |
|---|---|---|
| Baseline Elo | 193.95 | 0.651 |
| UDA (Full) | 70.97 | 0.812 |
| UDA (Ablated) | 65.64 | 0.510 |

Caption: "Removing self-awareness features (UDA (Ablated)) further reduces score variance but critically degrades correlation with human judgments, highlighting their essential role in achieving meaningful alignment."

---

## 7. ANALYSIS AND DISCUSSION

### 5.1 Methodological Novelty in Context
"UDA revises the canonical Elo update in two orthogonal directions that jointly attack judge-induced inconsistency. First, baseline Elo applies a global, static K, implicitly assuming homoscedastic noise. In practice, this is violated by LLM judges whose priors correlate with their own outputs. UDA replaces the constant K with an instance-adaptive K_ij learned from human-free features that capture both inter-answer relationships and self-preference signals. Consequently, likely biased comparisons are down-weighted.

Second, UDA replaces the raw win label r_ij^(k) with learned soft labels (s_i, s_j) that represent a bias-corrected win probability. This entire procedure is trained unsupervised, guided only by minimizing dispersion among all judges' Elo trajectories to distill a robust latent consensus."

### 5.2 Empirical Fidelity
"Our experiments confirm that UDA's consensus-driven objective successfully translates to empirical gains. The training loss (Eq. 3) guides the model to reduce inter-judge variance while maintaining rank fidelity to a stable consensus anchor. As evidenced by zero-shot transfer results (detailed in Appendix), UDA significantly improves alignment with the baseline consensus across both Pearson correlation and MSE metrics, confirming that the optimization effectively suppresses judge-specific noise.

Crucially, this reduction in variance corresponds to a greater alignment with human evaluators. UDA boosts the average Pearson correlation with human judgments by 24.7%, democratizing evaluation by elevating weaker judges to parity with stronger ones (Figure 4). The dramatic compression of score variance, as visualized in Figure 3, empirically validates the principle motivating Theorem 1: pulling scores toward a consensus reduces system-wide variance and produces more reproducible, judge-invariant rankings."

---

## 8. CONCLUSION (verbatim)

"We introduced UDA, an unsupervised, plug-and-play framework that mitigates self-preference bias in LLM-as-a-judge by dynamically calibrating the Elo update rule. By learning an instance-level K-factor and soft win-probabilities from lightweight, human-free features, UDA distills a consensus ranking that is simultaneously judge-invariant and human-aligned. Extensive experiments on two benchmarks confirm that UDA (i) shrinks inter-judge score dispersion by 59–63%, (ii) raises average Pearson correlation with human labels by 25%, and (iii) elevates low-capacity judges to parity with state-of-the-art models without retraining. Theoretical analysis supports the bias reduction under mild assumptions. Future work will explore richer feature spaces, weighted consensus objectives, and sub-quadratic approximations to scale beyond hundreds of judges. Code and data are publicly released to foster reproducible LLM evaluation."

---

## 9. LIMITATIONS AND FUTURE WORK (Appendix A.1, verbatim)

**Feature Sensitivity:** "The current feature vector φ_ij relies heavily on pre-trained BERT embeddings. While effective, this design assumes that semantic similarity is a sufficient proxy for self-preference. Future work could incorporate instruction-level features (e.g., task category, prompt difficulty) or meta-judge signals (e.g., perplexity under the judge's own decoding) to better disentangle intrinsic quality from stylistic preference."

**Objective Tradeoffs:** "The consensus loss L treats all judges as equally informative, which may over-correct high-quality judges like GPT-4o. A weighted variant that down-weights judges with historically poor correlation could preserve discriminative power while still reducing bias."

**Scalability:** "Training the adapter on 450K pairwise judgments is computationally lightweight (8 hours on a single 4090), but the O(MN) complexity of the consensus loss becomes prohibitive for M≫100. Approximate solutions—e.g., clustering judges into meta-judges—could retain debiasing benefits at scale."

---

## 10. FIGURE CAPTIONS (verbatim)

**Figure 1:** "A. Some models prefer their own answers, and mitigating this bias from using different LLMs can make the results more accurate. B. Dynamically recalibrate, rather than naively adopts, LLM-judged scores, using consensus among judges as the supervisory label in lieu of human annotation."
- Type: motivation (two-panel: bias illustration + method overview)
- Narrative role: establishes problem and solution at a glance

**Figure 2:** "Pairwise answer evaluation experiments were conducted using different large models as judges on the same Arena Hard dataset. The figure shows that LLMs exhibit self-preferential bias: some over-rate their own answers relative to other judges, others under-rate them. On ArenaHard (the depicted dataset) this bias ranges from −38% to +90%, while on our dataset it spans −21% to +56%."
- Type: problem_illustration (empirical motivation)

**Figure 3:** "Score stability across ten judge llms. Left: Baseline Elo. Right: UDA. Our method markedly aligns scores across diverse LLM judges, yielding significantly lower inter-judge variance."
- Type: teaser_result (side-by-side trajectory comparison)
- Referenced in results: "UDA (right) compresses this envelope to within 130 points"

**Figure 4:** "Per-model Pearson correlation (↑) between the judge scores computed with the baseline method, UDA method and consensus result, respectively, and the human-annotated ground-truth scores. Notably, consensus scores correlate best with human judgments; the uniform correlation of 0.89 arises because the consensus is shared across all judges, irrespective of individual model participation. This validates the consensus as a robust optimization target."
- Type: bar/scatter showing per-judge human alignment

**Figure 5:** "Judge-score heat-maps on Human-Annotated Transfer Set. After refinement with UDA, the scores judged by different LLM judges converge markedly, yielding a visibly narrower chromatic variance within each column of the heatmap."
- Type: heatmap qualitative_comparison (baseline vs. UDA)

---

## 11. TABLE CAPTIONS (verbatim)

**Table 1:** "Inter-LLM judge score standard deviation (↓) on ArenaHard Dataset."
**Table 2:** "Inter-LLM judge score standard deviation (↓) on Human-Annotated Transfer Set."
**Table 3:** "Ablation study results on the Human-Annotated Transfer Set. Removing self-awareness features (UDA (Ablated)) further reduces score variance but critically degrades correlation with human judgments, highlighting their essential role in achieving meaningful alignment."
**Table 4:** "Analysis of Alignment with Baseline Consensus. Zero-shot transfer results on Human-Annotated Transfer Set. UDA improves average Pearson correlation by +0.1415 and reduces average MSE by 23,699.9 without retraining. We adopt the baseline's mean scores as ground-truth supervision."
**Table 5:** "ArenaHard Dataset: baseline Elo (top) vs. UDA Method (bottom)" [Appendix: full judge-score matrices]
**Table 6:** "Human-Annotated Transfer Set: baseline Elo (top), UDA Method (mid), and Human score (bottom)"
**Table 7:** "Full judge-score matrices for Baseline Elo, the full UDA method, and the ablated UDA variant on the Human-Annotated Transfer Set. The ablated model shows visibly lower column-wise variance but diverges more from human-aligned rankings."

---

## 12. APPENDIX CONTENT SUMMARY

- A.1 Limitations and Future Work (Feature Sensitivity, Objective Tradeoffs, Scalability)
- A.2 Additional Empirical Analysis — Loss-driven Convergence: "Recall that the training objective (Eq. 3) enforces three complementary desiderata: (i) anchor alignment via MSE, (ii) rank fidelity via Pearson correlation, and (iii) collective consensus via global MSE."
- A.3 Prompts for Answer Generation and Judging — all prompts released
- A.4 Proofs — Complete Proof of Aggregate Bias Reduction (Theorem 1); formal mathematical setup with J = {1,…,M} judges; proof that S_UDA ≤ S_base (total absolute bias does not increase)
- Full Judge Score Matrices (Tables 5–7)
- Reproducibility Checklist: "Code, model checkpoints and the Human-Annotated Transfer Set are released at [URL]"

---

## KEY QUANTITATIVE FINDINGS SUMMARY

| Metric | Baseline | UDA | Change |
|---|---|---|---|
| Inter-judge std dev (ArenaHard, avg) | 158.5 | 64.8 | −59.1% |
| Inter-judge std dev (Human set, avg) | 193.95 | 70.97 | −63.4% |
| Pearson corr. with human (avg) | 0.651 | 0.812 | +24.7% |
| Self-preference deviation range | −21% to +56% | −15% to +4% | narrowed |
| Ablated UDA std dev | — | 65.64 | −66.2% but |
| Ablated UDA human corr. | 0.651 | 0.510 | −21.6% |
| Consensus Pearson corr. | — | 0.89 | (uniform across judges) |
| Pearson corr. improvement (Table 4) | — | +0.1415 | — |
| MSE reduction (Table 4) | — | −23,699.9 | — |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd232bfa-940d-4eeb-92b7-4d2606ab219e",
  "isSidechain": true,
  "agentId": "acc96dbc5ca49441b",
  "requestId": "req_011CbG3oSXxyTHDftLZW6aWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0b6061d-003d-4dcd-a733-50fc938eff06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/distiller_5e221dc4",
  "sessionId": "21618c8e-1e18-4031-a2ea-f1abe2868d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01R5GFmT8ar5dQNn7vTQWoxV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1046,
      "cache_read_input_tokens": 41362,
      "output_tokens": 8858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1046
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8858,
          "cache_read_input_tokens": 41362,
          "cache_creation_input_tokens": 1046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1046,
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
