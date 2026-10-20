# Research conversation: Search for the open-source code availability of "UDA" (Unsupervised Debiasing Alignment), a method for debiasing LLM jud

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af7bbaae6de608256.jsonl`
- **Structured JSON:** [`3375d90c753601480ba2.json`](../../sessions/33/3375d90c753601480ba2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-21T20:52:58.025Z_

Search for the open-source code availability of "UDA" (Unsupervised Debiasing Alignment), a method for debiasing LLM judges.

Perform these web searches and report findings:
1. Search "UDA unsupervised debiasing alignment LLM judge github"
2. Search "UDA AAAI 2026 LLM judge"
3. Search "unsupervised debiasing alignment LLM evaluation code"

For each search, report the top results. I need to know:
- Is there an open-source repo? If so, what's the URL?
- What license does it use?
- How is the code quality (well-documented, clean, etc.)?
- How complex would it be to integrate into an evaluation pipeline?
- If no code exists, how complex would reimplementation be based on the paper?

Be thorough - check arxiv pages for code links too. Report all URLs you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "e602d58d-8dc9-4c74-ad72-68d8abb2e418",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T20:52:58.031Z_

```json
{
  "parentUuid": "e602d58d-8dc9-4c74-ad72-68d8abb2e418",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
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
      "mcp__agent-ml-research__append_idea",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f26d267e-5484-40c1-9594-2d01ad7f4117",
  "timestamp": "2026-05-21T20:52:58.031Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T20:53:01.164Z_



I'll perform all three web searches in parallel, plus check arXiv for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f26d267e-5484-40c1-9594-2d01ad7f4117",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNr3ZeWC8ZuVSJXYTMu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e064a8c-a34d-43d1-9800-9a2b3e87b77a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWBsacVyLFXhYsY9yWn6EP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6734,
      "cache_read_input_tokens": 7329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6734,
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

_source line 4 · 2026-05-21T20:53:01.838Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011JrToxTbtRKs1jTzoS8RYT`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e064a8c-a34d-43d1-9800-9a2b3e87b77a",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNr3ZeWC8ZuVSJXYTMu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa65365b-5047-41f7-8c02-6059608d1ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWBsacVyLFXhYsY9yWn6EP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6734,
      "cache_read_input_tokens": 7329,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6734
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 7329,
          "cache_creation_input_tokens": 6734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6734,
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

_source line 5 · 2026-05-21T20:53:01.840Z_

<details><summary>↩ Tool result · `toolu_011JrToxTbtRKs1jTzoS8RYT`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa65365b-5047-41f7-8c02-6059608d1ea2",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "827bc759-2503-490e-a687-bc858abd86a8",
  "sourceToolAssistantUUID": "aa65365b-5047-41f7-8c02-6059608d1ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T20:53:04.271Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "827bc759-2503-490e-a687-bc858abd86a8",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNrL5a5ZqmZMQ6R9KLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8698b1fd-bbf8-4c57-bbf2-8c48be22080e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRKjxB15kBt7bavFvHoV2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 7 · 2026-05-21T20:53:04.825Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XXHmijxP3qNmg1se6F97Rj`</summary>

```json
{
  "query": "UDA unsupervised debiasing alignment LLM judge github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8698b1fd-bbf8-4c57-bbf2-8c48be22080e",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNrL5a5ZqmZMQ6R9KLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b89b5209-a98e-43c0-9a98-5a34a51e7ca5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRKjxB15kBt7bavFvHoV2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 8 · 2026-05-21T20:53:05.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S71FiYSLgDELbk2ZBdQaUP`</summary>

```json
{
  "query": "UDA AAAI 2026 LLM judge debiasing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b89b5209-a98e-43c0-9a98-5a34a51e7ca5",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNrL5a5ZqmZMQ6R9KLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac6b9b04-0268-4b5c-b4f1-f8ca4fc14c17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRKjxB15kBt7bavFvHoV2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 9 · 2026-05-21T20:53:05.732Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C3n2JVqYpuqdhRGDb4UCSg`</summary>

```json
{
  "query": "unsupervised debiasing alignment LLM evaluation code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac6b9b04-0268-4b5c-b4f1-f8ca4fc14c17",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNrL5a5ZqmZMQ6R9KLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7b92905-7139-47ac-bf5d-2672f991d8e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRKjxB15kBt7bavFvHoV2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 10 · 2026-05-21T20:53:05.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0125GdhTox1U4bMSHEUSvthR`</summary>

```json
{
  "query": "arxiv \"unsupervised debiasing alignment\" LLM judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7b92905-7139-47ac-bf5d-2672f991d8e6",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNrL5a5ZqmZMQ6R9KLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a0fe7ec-2971-47a7-a967-c0c2a69e267d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRKjxB15kBt7bavFvHoV2Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 14063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
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

_source line 11 · 2026-05-21T20:53:10.638Z_

<details><summary>↩ Tool result · `toolu_01C3n2JVqYpuqdhRGDb4UCSg`</summary>

```text
Web search results for query: "unsupervised debiasing alignment LLM evaluation code"

Links: [{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"}]

Based on the search results, I found a highly relevant paper for your query:

## UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

This research addresses preference bias in pairwise LLM evaluation by proposing UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system.

**Key Features:**
- For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities, operating in a fully unsupervised manner guided solely by minimizing dispersion among the Elo trajectories of all judges.

**Results:**
- Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.
- UDA elevates the performance of poorly performing judges to achieve parity with high-quality ones, fostering a more robust and reliable evaluation ecosystem.

**Code Availability:**
Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4 (note: this appears to be an anonymous repository for review purposes).

The paper was published in the AAAI Conference on Artificial Intelligence in 2026 and represents recent work in addressing bias and alignment issues in LLM evaluation methodologies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7b92905-7139-47ac-bf5d-2672f991d8e6",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "e539947d-29a5-495f-bed7-ae0d629a5d9f",
  "sourceToolAssistantUUID": "d7b92905-7139-47ac-bf5d-2672f991d8e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T20:53:11.252Z_

<details><summary>↩ Tool result · `toolu_01S71FiYSLgDELbk2ZBdQaUP`</summary>

```text
Web search results for query: "UDA AAAI 2026 LLM judge debiasing"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724"},{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/html/2603.05485"}]

Based on the search results, here's what I found about UDA AAAI 2026 LLM judge debiasing:

UDA (Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge) is a paper published at AAAI 2026. Pairwise evaluation of LLMs is prone to preference bias, where judges systematically favor certain outputs, such as their own, leading to inconsistent and skewed rankings across different judges.

UDA reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where a compact neural network learns to adaptively set the K-factor and refine win probabilities for each pairwise comparison. UDA operates in a fully unsupervised manner, guided solely by minimizing the dispersion among Elo trajectories of all judges, forcing alignment towards a collective consensus for more stable evaluation.

The results are impressive: UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%. Notably, UDA elevates the performance of poorly performing judges to achieve parity with high-quality ones.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac6b9b04-0268-4b5c-b4f1-f8ca4fc14c17",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "1b0f426d-8bd1-46a8-b1ff-bc21df64408c",
  "sourceToolAssistantUUID": "ac6b9b04-0268-4b5c-b4f1-f8ca4fc14c17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T20:53:11.260Z_

<details><summary>↩ Tool result · `toolu_0125GdhTox1U4bMSHEUSvthR`</summary>

```text
Web search results for query: "arxiv "unsupervised debiasing alignment" LLM judge"

Links: [{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724v1"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"}]

Based on the search results, I found the paper you're looking for:

## UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

The paper addresses preference bias in pairwise evaluation of LLMs, where judges systematically favor certain outputs, such as their own. 

The authors propose UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities, and UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges.

Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%, while elevating the performance of poorly performing judges to achieve parity with high-quality ones.

The paper was posted on arXiv on August 13, 2025 (arxiv:2508.09724) and has since been accepted to the AAAI Conference on Artificial Intelligence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a0fe7ec-2971-47a7-a967-c0c2a69e267d",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "a935ab56-c4ce-436c-8dda-cce0a2f7d1d1",
  "sourceToolAssistantUUID": "6a0fe7ec-2971-47a7-a967-c0c2a69e267d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T20:53:11.505Z_

<details><summary>↩ Tool result · `toolu_01XXHmijxP3qNmg1se6F97Rj`</summary>

```text
Web search results for query: "UDA unsupervised debiasing alignment LLM judge github"

Links: [{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724"}]

Based on the search results, here's what I found about UDA:

UDA (Unsupervised Debiasing Alignment) is a framework that addresses preference bias in pairwise evaluation of Large Language Models, where judges systematically favor certain outputs. 

The framework reduces inter-judge disagreement by dynamically adjusting the Elo rating system, with a compact neural network learning to adaptively set the K-factor and refine win probabilities for each pairwise comparison.

UDA operates in a fully unsupervised manner, minimizing the dispersion among Elo trajectories of all judges to force alignment towards a collective consensus that serves as an unsupervised proxy for more stable evaluation.

**Results:** Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.

**Code Availability:** Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4.

The research was authored by Yang Zhang, Cunxiang Wang, and colleagues, and has been published in the AAAI Conference on Artificial Intelligence (2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b89b5209-a98e-43c0-9a98-5a34a51e7ca5",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "007d72bd-b5d3-46c7-ac01-2ba0a7cd635b",
  "sourceToolAssistantUUID": "b89b5209-a98e-43c0-9a98-5a34a51e7ca5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-21T20:53:15.197Z_

The paper is found. The only code link so far is an anonymous review repo. Let me now check if there's a public GitHub repo (non-anonymous), and also look at the arXiv page and the anonymous repo directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "007d72bd-b5d3-46c7-ac01-2ba0a7cd635b",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNs3ArfUqT1FW5KzhQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6aa57328-9b46-47cc-9d72-4db50c60d537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dRoNWD2bNfpS3VCKAsiGf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2093,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 15523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 891,
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

_source line 16 · 2026-05-21T20:53:18.987Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011fFHFkaYNhGMRoHbFYgxfB`</summary>

```json
{
  "query": "github.com UDA unsupervised debiasing alignment Yang Zhang Cunxiang Wang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aa57328-9b46-47cc-9d72-4db50c60d537",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNs3ArfUqT1FW5KzhQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14d813d0-16b5-42ea-b49d-0331a4c710c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dRoNWD2bNfpS3VCKAsiGf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2093,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 15523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 891,
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

_source line 17 · 2026-05-21T20:53:19.108Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Czyz1wRPfRug7DT7hazxoQ`</summary>

```json
{
  "query": "site:github.com \"unsupervised debiasing alignment\" OR \"UDA\" LLM judge pairwise elo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14d813d0-16b5-42ea-b49d-0331a4c710c0",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNs3ArfUqT1FW5KzhQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c4cacc7-9114-45b0-a086-0fb4b53c4d77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dRoNWD2bNfpS3VCKAsiGf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2093,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 15523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 891,
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

_source line 18 · 2026-05-21T20:53:19.197Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KgSarcHcB8yDBqsfdV3CYw`</summary>

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
  "parentUuid": "3c4cacc7-9114-45b0-a086-0fb4b53c4d77",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNs3ArfUqT1FW5KzhQe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0503c493-0fc8-4fab-9344-96f39e0647dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dRoNWD2bNfpS3VCKAsiGf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2093,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 15523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 891,
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

_source line 19 · 2026-05-21T20:53:19.199Z_

<details><summary>↩ Tool result · `toolu_01KgSarcHcB8yDBqsfdV3CYw`</summary>

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
  "parentUuid": "0503c493-0fc8-4fab-9344-96f39e0647dd",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "bf8402fe-9512-470f-82bc-d287c128b4e4",
  "sourceToolAssistantUUID": "0503c493-0fc8-4fab-9344-96f39e0647dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T20:53:25.761Z_

<details><summary>↩ Tool result · `toolu_011fFHFkaYNhGMRoHbFYgxfB`</summary>

```text
Web search results for query: "github.com UDA unsupervised debiasing alignment Yang Zhang Cunxiang Wang"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"Unsupervised Learning of Debiased Representations with Pseudo-Attributes","url":"https://arxiv.org/pdf/2108.02943"},{"title":"Unsupervised Domain Alignment to Mitigate Low Level Dataset Biases","url":"https://arxiv.org/pdf/1907.03644"},{"title":"ToAlign: Task-oriented Alignment for Unsupervised Domain Adaptation","url":"https://arxiv.org/pdf/2106.10812"}]

Based on the search results, I found information about the UDA (Unsupervised Debiasing Alignment) paper by Yang Zhang and Cunxiang Wang:

UDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities.

The paper was authored by Yang Zhang from ZhipuAI and Peking University, and Cunxiang Wang from ZhipuAI and Tsinghua University, along with other co-authors.

The research addresses a key problem: Pairwise evaluation of Large Language Models (LLMs) is prone to preference bias, where judges systematically favor certain outputs, such as their own, leading to inconsistent and skewed rankings across different judges.

The paper was published in the Proceedings of the AAAI Conference on Artificial Intelligence, 40(41), 34854–34861 in 2026.

However, the search results did not return a specific GitHub repository URL. The paper appears to be published in academic venues (AAAI and arXiv), but I wasn't able to locate a dedicated GitHub repository through this search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14d813d0-16b5-42ea-b49d-0331a4c710c0",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "286b4866-6360-46ae-adf2-e942e100a5a1",
  "sourceToolAssistantUUID": "14d813d0-16b5-42ea-b49d-0331a4c710c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T20:53:26.158Z_

<details><summary>↩ Tool result · `toolu_01Czyz1wRPfRug7DT7hazxoQ`</summary>

```text
Web search results for query: "site:github.com "unsupervised debiasing alignment" OR "UDA" LLM judge pairwise elo"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"Aligning with Human Judgement: The Role of Pairwise Preference in Large   Language Model Evaluators","url":"https://arxiv.org/pdf/2403.16950"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"Fairness or Fluency? An Investigation into Language Bias of Pairwise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2601.13649"},{"title":"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection   Bias in LLMs-as-Judges","url":"https://arxiv.org/pdf/2410.15393"},{"title":"Improving Preference Extraction In LLMs By Identifying Latent Knowledge   Through Classifying Probes","url":"https://arxiv.org/pdf/2503.17755"}]

Based on the search results, I found relevant information about UDA and pairwise LLM-as-a-Judge evaluation. Here are the key findings:

## Main Result: UDA Paper

UDA (Unsupervised Debiasing Alignment) addresses preference bias in pairwise evaluation of Large Language Models, where judges systematically favor certain outputs. The framework reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where a compact neural network learns to adaptively set the K-factor and refine win probabilities for each pairwise comparison.

UDA operates in a fully unsupervised manner, guided solely by minimizing the dispersion among the Elo trajectories of all judges, forcing alignment towards a collective consensus. Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.

## Related Work

The search also returned several other relevant papers on pairwise LLM-as-a-Judge evaluation, including work on:
- PAIRS (Pairwise-preference Search) for rank aggregation
- Selection bias mitigation in pairwise comparisons
- Language bias and other systematic biases in LLM judges
- Methods for extracting preferences from LLMs

The UDA code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4, according to the paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c4cacc7-9114-45b0-a086-0fb4b53c4d77",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "bd005157-15ee-414d-83f6-e2c32ec6d32a",
  "sourceToolAssistantUUID": "3c4cacc7-9114-45b0-a086-0fb4b53c4d77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-21T20:53:29.191Z_



Let me now fetch the arXiv page and the anonymous repo to check for code links and details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd005157-15ee-414d-83f6-e2c32ec6d32a",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNt7nwzV7sc2HUZUZx4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4ad810f-9ed4-4041-8775-3890a8a1e904",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKAS2izpxDJacVpurbY4r4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4326,
      "cache_read_input_tokens": 16414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4326,
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

_source line 23 · 2026-05-21T20:53:31.151Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013Bhfi6FFjnmNgGpUXpHjpC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.09724",
  "prompt": "Extract: 1) All author names and affiliations, 2) Any links to code/data/GitHub repos mentioned anywhere on the page, 3) The paper's abstract, 4) Any \"Code\" or \"Data\" badges/links on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4ad810f-9ed4-4041-8775-3890a8a1e904",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNt7nwzV7sc2HUZUZx4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "181389d2-ee23-43d6-92e7-a47959b7f562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKAS2izpxDJacVpurbY4r4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4326,
      "cache_read_input_tokens": 16414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4326,
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

_source line 24 · 2026-05-21T20:53:32.577Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WcyBE2LQdg3fAWnE266hZY`</summary>

```json
{
  "url": "https://anonymous.4open.science/r/62AB93CD-23B4",
  "prompt": "List all files and directories in this repository. What programming language is used? Is there a README? What license is specified? What are the main code files? Describe the structure and quality of the code."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "181389d2-ee23-43d6-92e7-a47959b7f562",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNt7nwzV7sc2HUZUZx4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d093b0c3-c0d2-4705-bca4-eda06ddd63c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKAS2izpxDJacVpurbY4r4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4326,
      "cache_read_input_tokens": 16414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4326,
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

_source line 25 · 2026-05-21T20:53:32.815Z_

<details><summary>↩ Tool result · reported error · `toolu_01WcyBE2LQdg3fAWnE266hZY`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d093b0c3-c0d2-4705-bca4-eda06ddd63c1",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "06e39e05-7c4b-4961-bce6-b1ab48d3c986",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "d093b0c3-c0d2-4705-bca4-eda06ddd63c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T20:53:33.801Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R6DqZExP8Tpva7Mi6uURoF`</summary>

```json
{
  "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788",
  "prompt": "Extract any links to code, supplementary material, or GitHub repositories. Also extract author names, DOI, and publication details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06e39e05-7c4b-4961-bce6-b1ab48d3c986",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNt7nwzV7sc2HUZUZx4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b29bafbd-c164-46e4-9c1a-c6d401d256b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKAS2izpxDJacVpurbY4r4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4326,
      "cache_read_input_tokens": 16414,
      "output_tokens": 374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4326
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 374,
          "cache_read_input_tokens": 16414,
          "cache_creation_input_tokens": 4326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4326,
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

_source line 27 · 2026-05-21T20:53:36.492Z_

<details><summary>↩ Tool result · `toolu_013Bhfi6FFjnmNgGpUXpHjpC`</summary>

```text
# Paper Information Extraction

## 1. Authors and Affiliations
The page lists seven authors:
- Yang Zhang
- Cunxiang Wang
- Lindong Wu
- Wenbo Yu
- Yidong Wang
- Guangsheng Bao
- Jie Tang

However, **no affiliations are provided** on this arXiv abstract page.

## 2. Code/Data Links
The abstract mentions: "Code and data are available at [this https URL](https://anonymous.4open.science/r/62AB93CD-23B4)"

However, the actual URL destination is not fully displayed on the page—only a placeholder reference appears.

## 3. Abstract
"Pairwise evaluation of Large Language Models (LLMs) is a common paradigm, but it is prone to preference bias, where judges systematically favor certain outputs, such as their own. This bias leads to inconsistent and skewed rankings across different judges. To address this, we first empirically demonstrate significant and heterogeneous biases in cross-model evaluations. We then propose UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system." [truncated at 125 characters]

## 4. Code/Data Badges
The page does **not display dedicated "Code" or "Data" badges**. The code/data availability is mentioned only in text within the abstract itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "181389d2-ee23-43d6-92e7-a47959b7f562",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "57b2dbb5-bb3d-4e95-a79a-e819140714f3",
  "sourceToolAssistantUUID": "181389d2-ee23-43d6-92e7-a47959b7f562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T20:53:39.475Z_

<details><summary>↩ Tool result · `toolu_01R6DqZExP8Tpva7Mi6uURoF`</summary>

```text
# UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge

## Publication Details
- **DOI:** https://doi.org/10.1609/aaai.v40i41.40788
- **Published:** March 14, 2026
- **Conference:** AAAI-26 Technical Tracks 41, Natural Language Processing VI
- **Pages:** 34854–34861

## Authors
- Yang Zhang (ZhipuAI, Peking University)
- Cunxiang Wang (ZhipuAI, Tsinghua University)
- Lindong Wu (ZhipuAI)
- Wenbo Yu (ZhipuAI)
- Yidong Wang (ZhipuAI, Peking University)
- Guangsheng Bao (Westlake University)
- Jie Tang (Tsinghua University)

## Available Materials
- **PDF:** Available for download
- **Poster:** Available for download

## Code/Repository Links
No links to code repositories or supplementary materials are provided on this webpage.

## Summary
The paper addresses preference bias in pairwise LLM evaluation through an unsupervised framework that "reduces inter-judge disagreement by dynamically adjusting the Elo rating system," achieving up to 63.4% reduction in rating variance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b29bafbd-c164-46e4-9c1a-c6d401d256b8",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "cdd5fbd0-406f-4871-a106-8ce03dca555c",
  "sourceToolAssistantUUID": "b29bafbd-c164-46e4-9c1a-c6d401d256b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T20:53:42.543Z_

The anonymous repo returned a 403. Let me try a few more searches to find if the authors have released a public GitHub repo post-publication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdd5fbd0-406f-4871-a106-8ce03dca555c",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNu6ijSGhJ9cztpKzjv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b16891a-575c-405c-829a-64edfd1d7dd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQA9teoE3CZPLsbDpQ55kj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 20740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
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

_source line 30 · 2026-05-21T20:53:43.019Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YS7Wo9bMA4NCK2NWautJCk`</summary>

```json
{
  "query": "\"Yang Zhang\" \"Cunxiang Wang\" ZhipuAI UDA code github debiasing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b16891a-575c-405c-829a-64edfd1d7dd7",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNu6ijSGhJ9cztpKzjv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3adf938-c435-4d96-818a-acdfadb2a68e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQA9teoE3CZPLsbDpQ55kj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 20740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
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

_source line 31 · 2026-05-21T20:53:43.920Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Gpx8aXbmpxVDt6i1ZpNPz`</summary>

```json
{
  "query": "github.com UDA-debiasing OR UDA-judge OR unsupervised-debiasing-alignment elo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3adf938-c435-4d96-818a-acdfadb2a68e",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNu6ijSGhJ9cztpKzjv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4f4b388-be1f-4b8f-930d-b79446f4f023",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQA9teoE3CZPLsbDpQ55kj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 20740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1120,
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

_source line 32 · 2026-05-21T20:53:46.360Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CF1Rn4eSqjVLBhSYRzuSGB`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724",
  "prompt": "Find ALL URLs and links mentioned in the paper text, especially: 1) GitHub or code repository links, 2) Links to data or benchmarks, 3) Any footnotes with URLs. Also extract: the method description (how the neural network works, what it takes as input, what it outputs), and the training/optimization details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4f4b388-be1f-4b8f-930d-b79446f4f023",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNu6ijSGhJ9cztpKzjv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e5a35df-92d6-42c9-96e9-63e2e803fb5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQA9teoE3CZPLsbDpQ55kj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1120,
      "cache_read_input_tokens": 20740,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1120
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 20740,
          "cache_creation_input_tokens": 1120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1120,
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

_source line 33 · 2026-05-21T20:53:48.818Z_

<details><summary>↩ Tool result · `toolu_01YS7Wo9bMA4NCK2NWautJCk`</summary>

```text
Web search results for query: ""Yang Zhang" "Cunxiang Wang" ZhipuAI UDA code github debiasing"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"Yang Zhang","url":"https://www.csauthors.net/yang-zhang/"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"UGID: Unified Graph Isomorphism for Debiasing Large Language Models","url":"https://arxiv.org/pdf/2603.19144"}]

Based on the search results, I found relevant information about the paper you're looking for:

Yang Zhang from ZhipuAI and Peking University, and Cunxiang Wang from ZhipuAI and Tsinghua University are authors on a paper titled "UDA: Unsupervised Debiasing Alignment," a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system.

The framework reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where for each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. UDA operates in a fully unsupervised manner, guided by minimizing dispersion among Elo trajectories of all judges, forcing alignment towards collective consensus.

Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4. The paper was published at the Proceedings of the AAAI Conference on Artificial Intelligence, and the paper is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3adf938-c435-4d96-818a-acdfadb2a68e",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "f08d03ee-1a74-4b64-8ee3-cf9b9cc41104",
  "sourceToolAssistantUUID": "d3adf938-c435-4d96-818a-acdfadb2a68e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T20:53:50.506Z_

<details><summary>↩ Tool result · `toolu_012Gpx8aXbmpxVDt6i1ZpNPz`</summary>

```text
Web search results for query: "github.com UDA-debiasing OR UDA-judge OR unsupervised-debiasing-alignment elo"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"}]

Based on the search results, I found information about the UDA (Unsupervised Debiasing Alignment) research project:

UDA is a framework that addresses preference bias in pairwise evaluation of Large Language Models by reducing inter-judge disagreement through dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities, operating in a fully unsupervised manner guided solely by minimizing dispersion among the Elo trajectories of all judges.

Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.

The paper is available on arXiv (2508.09724) and has been published in the Proceedings of the AAAI Conference on Artificial Intelligence. According to the paper, code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4.

However, the search results did not return specific GitHub repository links matching your exact query terms (UDA-debiasing, UDA-judge, or unsupervised-debiasing-alignment).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4f4b388-be1f-4b8f-930d-b79446f4f023",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "0813b94c-402d-409e-b5de-195af3cb1981",
  "sourceToolAssistantUUID": "b4f4b388-be1f-4b8f-930d-b79446f4f023",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T20:53:53.496Z_

<details><summary>↩ Tool result · `toolu_01CF1Rn4eSqjVLBhSYRzuSGB`</summary>

```text
# UDA Paper: URLs, Method Details, and Training Information

## URLs and Links

1. **Code and Data Repository**: https://anonymous.4open.science/r/62AB93CD-23B4
2. **ArenaHard Benchmark**: Referenced as a dataset source (no direct URL provided in text)
3. **LMSys Chatbot Arena**: Mentioned as related work (no URL in paper)

## Method Description

### Input Components
The adaptive debiasing network processes three embedding vectors:
- Answer embeddings (𝐞ᵢ, 𝐞ⱼ) from candidate responses
- Judge's own embedding (𝐞ₖ) from the judge model's generated response

### Feature Engineering
The system constructs a 6D+9-dimensional feature vector containing:
- **Six high-dimensional vectors**: element-wise differences and normalized products between answer pairs and judge's response
- **Nine scalar features**: cosine similarities and KL-divergence measurements between embeddings
- **Self-awareness components**: specifically capture similarity between each candidate and judge's own output

### Neural Network Architecture
A 3-layer multilayer perceptron (MLP) maps features to three outputs:
- Instance-level K-factor (Kᵢⱼ)
- Soft labels (sᵢ, sⱼ) replacing hard binary preferences

## Training and Optimization

### Objective Function
Three complementary loss components:

1. **Anchor alignment** via mean squared error to consensus
2. **Rank fidelity** via Pearson correlation preservation
3. **Collective consensus** enforcement across all judges

### Training Configuration
- Optimizer: AdamW with learning rate scheduler
- Batch structure: "judge-homogeneous batches" containing all pairwise comparisons from single judge
- Dataset scale: 450,000 pairwise judgments on ArenaHard
- Computational cost: "8 hours on a single 4090"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e5a35df-92d6-42c9-96e9-63e2e803fb5e",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "ba36ba25-129d-41ce-9512-f661d73402ff",
  "sourceToolAssistantUUID": "6e5a35df-92d6-42c9-96e9-63e2e803fb5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-21T20:53:56.863Z_

Now let me do one final check -- try to find the authors' GitHub profiles to see if they released the code there.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba36ba25-129d-41ce-9512-f661d73402ff",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNv8gLRVoDm46CpLzio",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79f2eaf2-f23e-43ac-bfa1-89cc4f47ee62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsgS8DKb79Azizse1zgGaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2028,
      "cache_read_input_tokens": 21860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2028,
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

_source line 37 · 2026-05-21T20:53:57.388Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C4Lp2fYNJjdLNLyvXiapvr`</summary>

```json
{
  "query": "Cunxiang Wang github ZhipuAI NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79f2eaf2-f23e-43ac-bfa1-89cc4f47ee62",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNv8gLRVoDm46CpLzio",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b73ad4f-f5b2-42b1-8fcf-83b0aafd336c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsgS8DKb79Azizse1zgGaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2028,
      "cache_read_input_tokens": 21860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2028,
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

_source line 38 · 2026-05-21T20:53:57.525Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A5SuMjfevRDxgpGECP5GWh`</summary>

```json
{
  "query": "Guangsheng Bao github Westlake NLP LLM judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b73ad4f-f5b2-42b1-8fcf-83b0aafd336c",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNv8gLRVoDm46CpLzio",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "260919d1-64e3-4410-8cdc-bcc56b21d119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsgS8DKb79Azizse1zgGaT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2028,
      "cache_read_input_tokens": 21860,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2028
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 21860,
          "cache_creation_input_tokens": 2028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2028,
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

_source line 39 · 2026-05-21T20:54:02.580Z_

<details><summary>↩ Tool result · `toolu_01C4Lp2fYNJjdLNLyvXiapvr`</summary>

```text
Web search results for query: "Cunxiang Wang github ZhipuAI NLP"

Links: [{"title":"Cunxiang Wang, Westlake University","url":"https://wangcunxiang.github.io/"},{"title":"Method and device for chinese concept embedding generation based on wikipedia link structure","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11244020"},{"title":"Natural Language Processing Techniques to Detect Delirium in Hospitalized Patients from Clinical Notes: A Systematic Review","url":"https://www.medrxiv.org/content/10.1101/2025.06.05.25329038.full.pdf"},{"title":"Early Detection of Cognitive Decline in Parkinson’s Disease Using Natural Language Processing of Clinical Notes: A Systematic Review and Meta-Analysis Protocol","url":"https://www.medrxiv.org/content/10.1101/2025.10.11.25337798.full.pdf"},{"title":"ZpWang-AI (Zhipang (William) Wang) · GitHub","url":"https://github.com/ZpWang-AI"},{"title":"Early Detection of Cognitive Decline in Parkinson’s Disease Using Natural Language Processing of Speech: Protocol for a Systematic Review and Meta-Analysis","url":"https://www.medrxiv.org/content/10.1101/2025.10.11.25337799.full.pdf"},{"title":"Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"}]

Based on the search results, here's what I found:

Cunxiang Wang is recruiting self-motivated interns and full-time employees to work at Tsinghua or ZhipuAI. His personal website (wangcunxiang.github.io) shows his academic background and research interests.

He was a Ph.D. candidate supervised by Yue Zhang at Zhejiang University from August 2019 to June 2024. He received his undergraduate degree from Northeastern University's Computer Science and Technology department (2015-2019) and interned at Northeastern NLP Lab from 2016-2019.

His research involves work on large language models and NLP. He has published work on factuality in large language models, including knowledge, retrieval and domain-specificity. The search results indicate he maintains GitHub repositories related to his work, though the specific GitHub profile details weren't fully displayed in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b73ad4f-f5b2-42b1-8fcf-83b0aafd336c",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "179b1528-1c92-4e42-9f35-0659971a2e9e",
  "sourceToolAssistantUUID": "1b73ad4f-f5b2-42b1-8fcf-83b0aafd336c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T20:54:04.521Z_

<details><summary>↩ Tool result · `toolu_01A5SuMjfevRDxgpGECP5GWh`</summary>

```text
Web search results for query: "Guangsheng Bao github Westlake NLP LLM judge"

Links: [{"title":"baoguangsheng (Guangsheng Bao) · GitHub","url":"https://github.com/baoguangsheng"},{"title":"Guangsheng BAO | PhD Student | Ph.D. Candidate | Westlake University, Hangzhou | Research profile","url":"https://www.researchgate.net/profile/Guangsheng-Bao-2"},{"title":"Guangsheng Bao","url":"https://baoguangsheng.github.io/"},{"title":"The Silent Judge: Unacknowledged Shortcut Bias in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2509.26072"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge","url":"https://arxiv.org/pdf/2411.16594"}]

Based on the search results, here's what I found:

Guangsheng Bao is currently a Ph.D. candidate at Westlake University and Zhejiang University, where he is advised by Prof. Yue Zhang. His primary research interests lie in trustworthy NLP, encompassing topics like model generalization, explainable and controllable NLP systems, safe application of LLMs, and understanding the reasoning capabilities of LLMs.

**GitHub Profile:**
His GitHub profile is at github.com/baoguangsheng and is affiliated with Westlake University & Zhejiang University.

**Research on LLM Judges:**
Bao has published work on pairwise evaluation of Large Language Models, addressing preference bias where judges systematically favor certain outputs. He proposed UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system, with a neural network that adaptively sets the K-factor and refine win probabilities in an unsupervised manner.

**Research Background:**
He has published at esteemed conferences including ACL, ICLR, EMNLP, TASLP, and AAAI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "260919d1-64e3-4410-8cdc-bcc56b21d119",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "a4b9486e-fd32-4e3c-bece-a4e039c1ee1d",
  "sourceToolAssistantUUID": "260919d1-64e3-4410-8cdc-bcc56b21d119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T20:54:09.108Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Hugo5wr2ZyMfhM6jWEQQEe`</summary>

```json
{
  "url": "https://github.com/baoguangsheng",
  "prompt": "List all repositories visible on this GitHub profile page. Is there any repository related to UDA, debiasing, LLM judge evaluation, or Elo rating? List all repo names and their descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4b9486e-fd32-4e3c-bece-a4e039c1ee1d",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNvx39iQEvUBaxQydt5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79fb212f-6611-4363-833f-6c39603de032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014n8YMPBDQh56o2k3DaGphi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 23888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
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

_source line 42 · 2026-05-21T20:54:10.276Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011yqpCWXh5hihxdaR2kBfDP`</summary>

```json
{
  "url": "https://wangcunxiang.github.io/",
  "prompt": "Find any links to code repositories, GitHub profiles, or project pages related to UDA or LLM judge debiasing. List all GitHub/code links on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79fb212f-6611-4363-833f-6c39603de032",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNvx39iQEvUBaxQydt5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "012db780-e3da-4105-b59c-54fba241e5cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014n8YMPBDQh56o2k3DaGphi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 23888,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1445
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 23888,
          "cache_creation_input_tokens": 1445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1445,
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

_source line 43 · 2026-05-21T20:54:12.644Z_

<details><summary>↩ Tool result · `toolu_01Hugo5wr2ZyMfhM6jWEQQEe`</summary>

```text
# GitHub Repositories for baoguangsheng

Based on the profile page, here are the visible repositories:

1. **fast-detect-gpt** - "Code base for ICLR 2024 'Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature'."

2. **glimpse** - "Code base for ICLR 2025 'Glimpse: Enabling White-Box Methods to Use Proprietary Models for Zero-Shot LLM-Generated Text Detection'"

3. **g-transformer** - "Code base for 'G-Transformer for Document-level Machine Translation'"

4. **ctx-rewriter-for-summ** - "Code base for 'Contextualized Rewriting for Text Summarization'"

5. **target-side-augmentation** - "Code base for 'Target-Side Augmentation for Document-Level Machine Translation'"

6. **bart-rewriters** - "Code base for 'A General Contextualized Rewriting Framework for Text Summarization'"

## Relevant to Your Query

**No repositories directly related to UDA, debiasing, LLM judge evaluation, or Elo rating** are listed on this profile page. The visible projects focus on machine-generated text detection, machine translation, and text summarization techniques.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79fb212f-6611-4363-833f-6c39603de032",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "4863e4a4-c3b4-429b-9a34-7365d71decdd",
  "sourceToolAssistantUUID": "79fb212f-6611-4363-833f-6c39603de032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T20:54:15.162Z_

<details><summary>↩ Tool result · `toolu_011yqpCWXh5hihxdaR2kBfDP`</summary>

```text
# GitHub and Code Repository Links

Based on the webpage content, here are all the GitHub/code links related to projects:

1. **NovelQA** - "Benchmarking Question Answering on Documents Exceeding 200K Tokens"
   https://github.com/NovelQA/novelqa.github.io

2. **LLM-Factuality-Survey** - "Survey on Factuality in Large Language Models"
   https://github.com/wangcunxiang/LLM-Factuality-Survey

3. **StepMathAgent** - "A Step-Wise Agent for Evaluating Mathematical Processes through Tree-of-Error"
   https://github.com/SHU-XUN/StepMathAgent

4. **QA-Eval** - "Evaluating Open-QA Evaluation"
   https://github.com/wangcunxiang/QA-Eval/

5. **Graph-aS-Tokens** - "Exploiting Abstract Meaning Representation for Open-Domain Question Answering"
   https://github.com/wangcunxiang/Graph-aS-Tokens

6. **RFiD** - "Towards Rational Fusion-in-Decoder for Open-Domain Question Answering"
   https://github.com/wangcunxiang/RFiD

7. **SemEval2020-Task4** - "Commonsense Validation and Explanation"
   https://github.com/wangcunxiang/SemEval2020-Task4-Commonsense-Validation-and-Explanation

8. **Sen-Making-and-Explanation** - "Does it Make Sense? And Why?"
   https://github.com/wangcunxiang/Sen-Making-and-Explanation

9. **Domain-Representation-for-Knowledge-Graph-Embedding**
   https://github.com/wangcunxiang/Domain-Representation-for-Knowledge-Graph-Embedding

10. **Can-PLM-Serve-as-KB-for-CBQA** - "Can Generative Pre-trained Language Models Serve as Knowledge Bases?"
    https://github.com/wangcunxiang/Can-PLM-Serve-as-KB-for-CBQA
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "012db780-e3da-4105-b59c-54fba241e5cd",
  "isSidechain": true,
  "promptId": "2562d93a-d61d-47fc-b38d-4b566667fe21",
  "agentId": "af7bbaae6de608256",
  "type": "user",
  "uuid": "ad16474a-07de-4652-becf-afde575a08b1",
  "sourceToolAssistantUUID": "012db780-e3da-4105-b59c-54fba241e5cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-21T20:54:43.748Z_

Now I have a comprehensive picture. Here is the full report.

---

## UDA (Unsupervised Debiasing Alignment) -- Code Availability Report

### Paper Details

- **Title**: UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge
- **Venue**: AAAI 2026 (Technical Track 41, NLP VI), pages 34854-34861
- **arXiv**: [2508.09724](https://arxiv.org/abs/2508.09724)
- **DOI**: https://doi.org/10.1609/aaai.v40i41.40788
- **Authors**: Yang Zhang (ZhipuAI, Peking University), Cunxiang Wang (ZhipuAI, Tsinghua University), Lindong Wu (ZhipuAI), Wenbo Yu (ZhipuAI), Yidong Wang (ZhipuAI, Peking University), Guangsheng Bao (Westlake University), Jie Tang (Tsinghua University)

### Code Availability: No Public Repo Found

The **only code link** mentioned in the paper is an anonymous review-stage repository:
- `https://anonymous.4open.science/r/62AB93CD-23B4`

This link currently returns **403 Forbidden** -- anonymous 4open.science repos are typically shut down after the review period ends, and this one appears to be inaccessible now.

I checked all plausible locations:
- **No GitHub repo** exists under any of the authors' profiles (checked [baoguangsheng](https://github.com/baoguangsheng) and [wangcunxiang](https://wangcunxiang.github.io/))
- **No public repo** found on GitHub via keyword searches (UDA-debiasing, UDA-judge, unsupervised-debiasing-alignment, etc.)
- The **AAAI proceedings page** has no code/supplementary link
- The **arXiv page** only references the dead anonymous repo

**Conclusion: There is no publicly accessible open-source implementation of UDA as of 2026-05-21.**

### Reimplementation Complexity Assessment

Based on the full paper details extracted from the HTML version, here is what reimplementation would require:

**Architecture** (moderate complexity):
- A 3-layer MLP that takes a (6D+9)-dimensional feature vector and outputs three values: an instance-level K-factor and two soft labels (replacing hard binary win/loss preferences)
- Input features are constructed from embeddings of the two candidate answers and the judge's own response: element-wise differences, normalized products, cosine similarities, and KL-divergences between these embeddings

**Training** (moderate-high complexity):
- Unsupervised objective with three loss components: (1) anchor alignment via MSE to consensus, (2) rank fidelity via Pearson correlation preservation, (3) collective consensus enforcement across all judges
- Uses "judge-homogeneous batches" (all pairwise comparisons from a single judge per batch)
- Optimizer: AdamW with learning rate scheduler
- Training data: ~450,000 pairwise judgments on ArenaHard
- Compute: ~8 hours on a single RTX 4090

**Key dependencies for reimplementation**:
1. Need to collect pairwise judgments from multiple LLM judges on the same dataset (the paper uses ArenaHard with ~500 prompts)
2. Need sentence/response embeddings for all answers and judge outputs
3. Need a standard Elo rating implementation as the backbone
4. The MLP itself is trivial; the complexity is in the loss function design and the data pipeline

**Estimated reimplementation effort**: 2-4 days for a competent ML engineer familiar with Elo systems and PyTorch. The method is conceptually clean (small MLP, well-defined loss), but getting the data pipeline right (collecting multi-judge pairwise evaluations, computing all embedding features) and reproducing the exact training regime would take the bulk of the time. The paper is detailed enough that reimplementation is feasible without the original code.

**Integration complexity**: Medium. UDA is a post-hoc method -- it sits on top of existing pairwise judgments and adjusts Elo updates. It does not modify the judge prompts or LLM inference. You would: (1) collect pairwise judgments as usual, (2) compute embeddings, (3) run the trained MLP to get adjusted K-factors and soft labels, (4) use those in Elo computation. The main integration burden is maintaining the embedding computation and the trained MLP weights.

### All URLs Found

- arXiv abstract: https://arxiv.org/abs/2508.09724
- arXiv PDF: https://arxiv.org/pdf/2508.09724
- arXiv HTML: https://arxiv.org/html/2508.09724
- AAAI proceedings: https://ojs.aaai.org/index.php/AAAI/article/view/40788
- ResearchGate: https://www.researchgate.net/publication/394472798
- Dead anonymous repo: https://anonymous.4open.science/r/62AB93CD-23B4 (403)
- Cunxiang Wang's homepage: https://wangcunxiang.github.io/
- Guangsheng Bao's GitHub: https://github.com/baoguangsheng
- Guangsheng Bao's homepage: https://baoguangsheng.github.io/

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad16474a-07de-4652-becf-afde575a08b1",
  "isSidechain": true,
  "agentId": "af7bbaae6de608256",
  "requestId": "req_011CbGNwjKhrddVmmj1e6ojQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5fd82ff-f557-4445-9dc9-2de96553f475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "4909b84a-fc3b-4b99-94f5-cd6cd3d00579",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVQjTZ6FBZst1wLpKg4FsP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 25333,
      "output_tokens": 1336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1142
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1336,
          "cache_read_input_tokens": 25333,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1142,
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
