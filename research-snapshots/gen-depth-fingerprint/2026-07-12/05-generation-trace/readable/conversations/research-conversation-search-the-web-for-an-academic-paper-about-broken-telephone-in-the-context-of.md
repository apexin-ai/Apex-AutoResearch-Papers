# Research conversation: Search the web for an academic paper about "Broken Telephone" in the context of LLM text generation, iterative paraphras

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a1393d2486eb6b8da.jsonl`
- **Structured JSON:** [`d800de91875ca74f3126.json`](../../sessions/d8/d800de91875ca74f3126.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-21T03:00:27.021Z_

Search the web for an academic paper about "Broken Telephone" in the context of LLM text generation, iterative paraphrasing, or model collapse. Possible titles include:
- "The Broken Telephone Effect"
- "Broken Telephone: Exploring the Limits of Iterative Paraphrasing"
- Something about "broken telephone" + LLM + paraphrase

Use WebSearch to find this paper. Try these queries:
1. "Broken Telephone" paraphrase LLM arxiv paper
2. "Broken Telephone Effect" iterative paraphrasing language model
3. "Broken Telephone" "model collapse" text generation

For the paper you find, extract these dimensions:
- **Full title and authors**
- **Chain type**: what type of chain (paraphrase chain / translation chain / continuation chain / summarization chain)
- **Feature space**: what features or metrics they use to analyze (perplexity / diversity / embedding distance / vocabulary / entropy / etc.)
- **Analysis target**: what problem they analyze (convergence / attractor identification / quality degradation / depth classification)
- **Generator scale**: which models they use and what parameter sizes
- **Number of chain steps**: maximum chain depth
- **Core insight**: one-sentence summary of the main finding
- **Methodology details**: how they set up their experiments

Report all findings with citations to specific sections/tables if possible. Be thorough — I need accurate details, not guesses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ee0e299e-1086-42d9-9535-2aa06a2ee3cc",
  "agentId": "a1393d2486eb6b8da",
  "type": "user",
  "uuid": "0ef5732a-22cd-4e9e-9fc5-bb8985622c4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T03:00:27.023Z_

```json
{
  "parentUuid": "0ef5732a-22cd-4e9e-9fc5-bb8985622c4d",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "43451bcb-9129-4c0b-910b-f0ed8a3ad7a4",
  "timestamp": "2026-05-21T03:00:27.023Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T03:00:29.559Z_



I'll search for this paper using multiple queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43451bcb-9129-4c0b-910b-f0ed8a3ad7a4",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy4TLRTd52VXusrQTYP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1a27a8f-f24b-4745-8dda-1832a62fd4a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUB4iuE8LXkH2mdtCXZoaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6953,
      "cache_read_input_tokens": 9196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6953,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 4 · 2026-05-21T03:00:29.871Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RviV8bwKheRtj4GeKaDmZn`</summary>

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
  "parentUuid": "f1a27a8f-f24b-4745-8dda-1832a62fd4a5",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy4TLRTd52VXusrQTYP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b3ec87a-8a07-4019-b99b-4c7c8b0b7b96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUB4iuE8LXkH2mdtCXZoaf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6953,
      "cache_read_input_tokens": 9196,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6953
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 9196,
          "cache_creation_input_tokens": 6953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6953,
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

_source line 5 · 2026-05-21T03:00:29.874Z_

<details><summary>↩ Tool result · `toolu_01RviV8bwKheRtj4GeKaDmZn`</summary>

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
  "parentUuid": "9b3ec87a-8a07-4019-b99b-4c7c8b0b7b96",
  "isSidechain": true,
  "promptId": "ee0e299e-1086-42d9-9535-2aa06a2ee3cc",
  "agentId": "a1393d2486eb6b8da",
  "type": "user",
  "uuid": "772f6f6b-3439-40bb-b305-58f1e971c51e",
  "sourceToolAssistantUUID": "9b3ec87a-8a07-4019-b99b-4c7c8b0b7b96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T03:00:32.483Z_



Let me run multiple search queries in parallel to find this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "772f6f6b-3439-40bb-b305-58f1e971c51e",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy4fqzTgBh9hGANYGrJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6621de76-2b2b-4812-a1f6-1dc309d869f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171A4dTW1Ty48uen1cTB4Jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 16149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 7 · 2026-05-21T03:00:32.989Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MSXqz2iBXNasaMGBEZ2USu`</summary>

```json
{
  "query": "\"Broken Telephone\" paraphrase LLM arxiv paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6621de76-2b2b-4812-a1f6-1dc309d869f2",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy4fqzTgBh9hGANYGrJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1247c582-4532-4319-9b6a-8f56f33dd04c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171A4dTW1Ty48uen1cTB4Jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 16149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 8 · 2026-05-21T03:00:33.399Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015tN9iUMxM25Kom35irrQb7`</summary>

```json
{
  "query": "\"Broken Telephone Effect\" iterative paraphrasing language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1247c582-4532-4319-9b6a-8f56f33dd04c",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy4fqzTgBh9hGANYGrJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cd32c80-5bb1-49c2-802a-78d06ad45025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171A4dTW1Ty48uen1cTB4Jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 16149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 9 · 2026-05-21T03:00:33.684Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A8K74EhoAvy8g4RtNXEzm8`</summary>

```json
{
  "query": "\"Broken Telephone\" \"model collapse\" text generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cd32c80-5bb1-49c2-802a-78d06ad45025",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy4fqzTgBh9hGANYGrJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8ed1cd0-f149-4437-837c-3f876279c664",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171A4dTW1Ty48uen1cTB4Jt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 16149,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 176,
          "cache_read_input_tokens": 16149,
          "cache_creation_input_tokens": 1451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1451,
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

_source line 10 · 2026-05-21T03:00:39.528Z_

<details><summary>↩ Tool result · `toolu_01A8K74EhoAvy8g4RtNXEzm8`</summary>

```text
Web search results for query: ""Broken Telephone" "model collapse" text generation"

Links: [{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/html/2502.20258v1"},{"title":"Paper page - LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://huggingface.co/papers/2502.20258"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.20258v1"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts ...","url":"https://aclanthology.org/2025.acl-long.371.pdf"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | Request PDF","url":"https://www.researchgate.net/publication/394300051_LLM_as_a_Broken_Telephone_Iterative_Generation_Distorts_Information"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/pdf/2502.20258"}]

I found relevant search results about this topic. Here's what the research shows:

A study inspired by the "broken telephone" effect in chained human communication investigates whether LLMs similarly distort information through iterative generation. Large Language Models exhibit a "broken telephone" effect, where iterative generation processes, such as multi-hop translation or rephrasing, consistently lead to significant information distortion and factual degradation.

The research findings include several key insights:

1. **Information accumulates distortion over time**: Distortion accumulates over time, influenced by language choice and chain complexity.

2. **Factors affecting distortion**: The degree of information distortion in translation chains depends on the choice of intermediate languages, influenced by their linguistic similarity to the source language and their prevalence in the model's pre-training and post-training corpora.

3. **Chain complexity amplifies degradation**: Greater chain complexity, whether by adding languages or models, often amplifies distortion, with longer chains introducing more degradation regardless of the type of iterative chain.

4. **Mitigation strategies**: Although distortion is unavoidable, it can be mitigated through temperature control and restricted prompting, which restrict the LLM from deviating significantly from the original text.

This research connects to broader concerns about model collapse, as the repeated processing of LLM-generated content could contribute to knowledge degradation in AI systems over time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8ed1cd0-f149-4437-837c-3f876279c664",
  "isSidechain": true,
  "promptId": "ee0e299e-1086-42d9-9535-2aa06a2ee3cc",
  "agentId": "a1393d2486eb6b8da",
  "type": "user",
  "uuid": "dc2acb84-24ba-4d63-969a-f64bf4f2f00f",
  "sourceToolAssistantUUID": "f8ed1cd0-f149-4437-837c-3f876279c664",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T03:00:40.365Z_

<details><summary>↩ Tool result · `toolu_015tN9iUMxM25Kom35irrQb7`</summary>

```text
Web search results for query: ""Broken Telephone Effect" iterative paraphrasing language model"

Links: [{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/pdf/2502.20258"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/html/2502.20258v1"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.20258v1"},{"title":"[2502.20258] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/abs/2502.20258"},{"title":"[Quick Review] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://liner.com/review/llm-as-broken-telephone-iterative-generation-distorts-information"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts ...","url":"https://aclanthology.org/2025.acl-long.371.pdf"},{"title":"Paper page - LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://huggingface.co/papers/2502.20258"},{"title":"[Literature Review] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://www.themoonlight.io/en/review/llm-as-a-broken-telephone-iterative-generation-distorts-information"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.371/"}]

I found comprehensive information about the "Broken Telephone Effect" in the context of language models. Here's what the research shows:

## Overview

The "broken telephone" effect in LLMs investigates whether large language models similarly distort information through iterative generation, inspired by the broken telephone effect in chained human communication. The effect occurs where information gradually distorts through successive generations, similar to the childhood game where a message becomes increasingly garbled as it passes from person to person.

## Key Findings

Through translation-based experiments, distortion accumulates over time, influenced by language choice and chain complexity. The broken telephone effect extended beyond translation to rephrasing tasks, confirming the phenomenon's generality across different generative tasks.

## Experimental Approach

The study simulates the LLMs' broken telephone game using translation tasks across three experimental setups, comparing back-translated English versions with initial English using textual relevance and factuality measures. One experiment, called 'Bilingual Self-loop,' assesses distortion accumulation with single models translating between English and various bridge languages, finding degradation is influenced by linguistic similarity.

## Mitigation

While degradation is inevitable, it can be mitigated through strategic prompting techniques. The research demonstrates that distortion can be mitigated through strategic prompting techniques and temperature control, limiting deviations from the original text.

This research was published as an ACL 2025 paper and has significant implications for the reliability of LLM-generated content in iterative workflows.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cd32c80-5bb1-49c2-802a-78d06ad45025",
  "isSidechain": true,
  "promptId": "ee0e299e-1086-42d9-9535-2aa06a2ee3cc",
  "agentId": "a1393d2486eb6b8da",
  "type": "user",
  "uuid": "8187d7bc-16ab-487d-835d-c2ed3d213641",
  "sourceToolAssistantUUID": "2cd32c80-5bb1-49c2-802a-78d06ad45025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T03:00:42.476Z_

<details><summary>↩ Tool result · `toolu_01MSXqz2iBXNasaMGBEZ2USu`</summary>

```text
Web search results for query: ""Broken Telephone" paraphrase LLM arxiv paper"

Links: [{"title":"Paper page - LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://huggingface.co/papers/2502.20258"},{"title":"[Quick Review] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://liner.com/review/llm-as-broken-telephone-iterative-generation-distorts-information"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.20258v1"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/html/2502.20258v1"},{"title":"[2502.20258] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/abs/2502.20258"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/pdf/2502.20258"},{"title":"GitHub - amr-mohamedd/LLM-as-a-Broken-Telephone: [ACL 2025] Code implementation for the \"LLM as a Broken Telephone: Iterative Generation Distorts Information\" paper.","url":"https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts ...","url":"https://aclanthology.org/2025.acl-long.371.pdf"}]

I found the paper you're looking for! Here are the key details:

## "LLM as a Broken Telephone: Iterative Generation Distorts Information"

**Paper Details:**
- **ArXiv ID:** 2502.20258
- **Authors:** Amr Mohamed, Mingmeng Geng, Michalis Vazirgiannis, and Guokan Shang
- **Venue:** ACL 2025 (63rd Annual Meeting of the Association for Computational Linguistics)
- **Published:** February 27, 2025

**Overview:**
Inspired by the "broken telephone" effect in chained human communication, this study investigates whether LLMs similarly distort information through iterative generation, finding that distortion accumulates over time, influenced by language choice and chain complexity.

**Methodology:**
The study explores whether LLMs act as a 'broken telephone' when content is continuously refined, paraphrased, or reprocessed across successive model iterations, simulating the game using translation tasks across three experimental setups.

**Key Findings:**
While degradation is inevitable, it can be mitigated through strategic prompting techniques, and these findings contribute to discussions on the long-term effects of AI-mediated information propagation.

**Resources:**
- ArXiv: https://arxiv.org/abs/2502.20258
- GitHub Code: https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone
- ACL Proceedings: https://aclanthology.org/2025.acl-long.371.pdf


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1247c582-4532-4319-9b6a-8f56f33dd04c",
  "isSidechain": true,
  "promptId": "ee0e299e-1086-42d9-9535-2aa06a2ee3cc",
  "agentId": "a1393d2486eb6b8da",
  "type": "user",
  "uuid": "5dc33f99-19e2-485b-b083-62c270d2c350",
  "sourceToolAssistantUUID": "1247c582-4532-4319-9b6a-8f56f33dd04c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-21T03:00:46.848Z_

The paper is identified: **"LLM as a Broken Telephone: Iterative Generation Distorts Information"** (arXiv:2502.20258, ACL 2025). Now let me read the full paper for detailed extraction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dc33f99-19e2-485b-b083-62c270d2c350",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy5bRruE2sZTEKtHg5C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6b7c04a-e22f-4e89-b7e7-cccebf9da544",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WNZYuU8xHv8ze75JUg4Hv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1498,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 17600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1033,
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

_source line 14 · 2026-05-21T03:00:47.139Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DXqrFJC7fSpJZdkp2sMkD6`</summary>

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
  "parentUuid": "e6b7c04a-e22f-4e89-b7e7-cccebf9da544",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy5bRruE2sZTEKtHg5C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0edc04be-4ed7-4a9f-a9a5-9d01e2d40944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WNZYuU8xHv8ze75JUg4Hv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1498,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 17600,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1033
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1498,
          "output_tokens": 132,
          "cache_read_input_tokens": 17600,
          "cache_creation_input_tokens": 1033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1033,
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

_source line 15 · 2026-05-21T03:00:47.142Z_

<details><summary>↩ Tool result · `toolu_01DXqrFJC7fSpJZdkp2sMkD6`</summary>

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
  "parentUuid": "0edc04be-4ed7-4a9f-a9a5-9d01e2d40944",
  "isSidechain": true,
  "promptId": "ee0e299e-1086-42d9-9535-2aa06a2ee3cc",
  "agentId": "a1393d2486eb6b8da",
  "type": "user",
  "uuid": "6e75dede-c602-4349-af83-6727db1b5bdf",
  "sourceToolAssistantUUID": "0edc04be-4ed7-4a9f-a9a5-9d01e2d40944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T03:00:55.945Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015gJ4xM9zwPhJkkFrYjCufp`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.20258v1",
  "prompt": "Extract ALL of the following details from this paper:\n\n1. Full title and complete author list with affiliations\n2. What types of iterative chains are studied (translation chains, paraphrase chains, etc.)? List all experimental setups.\n3. What features/metrics do they use to measure distortion? (e.g., BLEU, BERTScore, perplexity, embedding distance, factuality metrics, etc.) List ALL metrics.\n4. What is the analysis target — what problem are they studying? (convergence, quality degradation, attractor states, depth classification, etc.)\n5. Which LLM models do they use and what are their parameter sizes?\n6. What is the maximum chain depth (number of iterative steps)?\n7. What are the core findings/insights — summarize each main finding in one sentence.\n8. Detailed experimental setup: how many experiments, what languages, what datasets, what prompting strategies.\n9. Any connection to \"model collapse\" or \"generation depth\" concepts.\n10. Section structure — list all section and subsection titles.\n\nBe as specific and detailed as possible. Include numbers, model names, language names, metric values where available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e75dede-c602-4349-af83-6727db1b5bdf",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy5wdJLBGJC51xoevUd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d63346b-66e4-4d65-bf81-1d7a6ba8afb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qt5JtHdwa5BmeUPBcs4kjR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2148,
      "cache_read_input_tokens": 18633,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2148
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 18633,
          "cache_creation_input_tokens": 2148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2148,
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

_source line 17 · 2026-05-21T03:01:11.963Z_

<details><summary>↩ Tool result · `toolu_015gJ4xM9zwPhJkkFrYjCufp`</summary>

```text
# Detailed Paper Analysis: "LLM as a Broken Telephone"

## 1. Title and Authors
**Full Title:** "LLM as a Broken Telephone: Iterative Generation Distorts Information"

**Authors:** Amr Mohamed¹, Mingmeng Geng², Michalis Vazirgiannis¹,³, Guokan Shang¹
- ¹MBZUAI, ²SISSA, ³Ecole Polytechnique

---

## 2. Iterative Chain Types & Experimental Setups

**Three main experimental configurations:**

- **Experiment 1 (Bilingual Self-loop):** English ↔ bridge language ↔ English, single model performing 100 iterations
- **Experiment 2 (Bilingual Two-player):** Two different models collaborating in the same English-bridge language-English chain
- **Experiment 3 (Multilingual Multiplayer):** 
  - Setting 1: Three languages (EN, FR, TH) with two models
  - Setting 2: Same as Setting 1 plus Gemma model added
  - Setting 3: Five languages (EN, FR, TH, ZH, DE) with original two models

**Ablation Studies:**
- Rephrasing chains (standalone and collaborative)
- Temperature variation experiments
- Prompt constraint sensitivity analysis

---

## 3. Distortion Measurement Metrics

**Textual Relevance Metrics:**
- BLEU (incremental error detection)
- ROUGE-1 (word-level omissions)
- CHR-F (character-level deviations)
- METEOR (paraphrastic variations)
- BERTScore (contextual/semantic relationships)

**Factuality Preservation:**
- FActScore (atomic fact verification against original text; uses Claude 3.5 Sonnet as judge)

---

## 4. Analysis Target

The study investigates "whether LLMs similarly distort information through iterative generation," mimicking the telephone game effect. The focus is on **progressive quality degradation** across multiple iterative steps, examining how "small alterations accumulate, leading to progressive drift from the original source."

---

## 5. LLM Models & Parameter Sizes

- **Llama-3.1-8B-Instruct** (8 billion parameters) — primary model
- **Mistral-7B-Instruct-v0.2** (7 billion parameters) — primary model
- **Gemma-2-9B-it** (9 billion parameters) — used in Experiment 3

---

## 6. Maximum Chain Depth

**100 iterative steps** for translation chains and rephrasing experiments

---

## 7. Core Findings (One-Sentence Summaries)

1. Information distortion accumulates progressively, with degradation rates depending on linguistic similarity between languages involved.

2. Non-Latin script languages (particularly Thai) exhibit significantly faster factuality loss than Latin-script pairs.

3. Chain complexity amplifies distortion: longer language chains and multi-model collaboration generally introduce greater degradation.

4. Temperature control and constrained prompting substantially mitigate (though cannot eliminate) information loss across iterations.

5. Larger models show improved information retention in collaborative settings.

---

## 8. Detailed Experimental Setup

**Datasets (150 documents each, 100-200 words):**
- BookSum (book summaries)
- ScriptBase-alpha (movie scripts)
- BBC News2024 (news articles)

**Languages Tested:**
- Source: English
- Bridge languages: French, German, Dutch, Vietnamese, Chinese, Thai

**Gradient Analysis Results** (FActScore deterioration rate):
- EN↔FR: -0.004 to -0.007 per iteration (Llama/Mistral)
- EN↔TH: -0.015 to -0.040 per iteration
- Thai demonstrated "the highest rates of factual degradation"

**Temperature Study:** 1×10⁻⁶, 0.25, 0.5, 0.75, 1.0

**Prompt Variants:** Simple, base (main), constrained

---

## 9. Connection to Model Collapse & Generation Depth

The research directly addresses "model and knowledge collapse" — where "iterative training on synthetically generated data induces systematic erosion." The authors note their work "echoes the ongoing conversation about the long-term impact of the widespread use of LLM-generated content on models themselves, humans, and society."

Key distinction: While prior work examined model retraining on synthetic data, this study focuses on **inference-time iterative processing** without retraining.

---

## 10. Section Structure

1. Introduction
2. Related Work
3. Methodology (Notations, Experimental Settings, Evaluation Metrics)
4. Experiments (3 main experiments)
5. Ablation Studies (Rephrasing, Temperature, Prompt Sensitivity)
6. Discussion and Conclusion
7. Appendices (Additional Details, Visualizations, Prompts, Examples)

---

## Key Takeaway

The study demonstrates LLMs function as "broken telephones" during iterative processing, with "small alterations in phrasing, meaning, or factual details accumulating" to create substantial divergence from originals—a phenomenon especially pronounced in underrepresented languages and complex multi-step chains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d63346b-66e4-4d65-bf81-1d7a6ba8afb6",
  "isSidechain": true,
  "promptId": "ee0e299e-1086-42d9-9535-2aa06a2ee3cc",
  "agentId": "a1393d2486eb6b8da",
  "type": "user",
  "uuid": "0b9bcddd-5280-4d37-8715-201548c43b30",
  "sourceToolAssistantUUID": "3d63346b-66e4-4d65-bf81-1d7a6ba8afb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-21T03:01:14.895Z_

Let me also fetch the GitHub repo for any additional experimental details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b9bcddd-5280-4d37-8715-201548c43b30",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy7mWeAmqXyH1j6jqMk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "460a6fb9-1197-4d91-b228-f436b9170534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oHvLV1FCdPTDquAQk6BZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 20781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1624,
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

_source line 19 · 2026-05-21T03:01:15.917Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N2skgRbDYYXK3N9THHDT7h`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.20258",
  "prompt": "Extract the exact abstract text, the submission date, and the full author list. Also check if there is a v2 or later version of the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "460a6fb9-1197-4d91-b228-f436b9170534",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy7mWeAmqXyH1j6jqMk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eddfb7d8-a628-44e3-9672-dd3b18e81887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oHvLV1FCdPTDquAQk6BZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 20781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1624,
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

_source line 20 · 2026-05-21T03:01:17.545Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AekLQZWGmowrMFSSDd9TCE`</summary>

```json
{
  "url": "https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone",
  "prompt": "Extract all details about the experimental setup: what scripts are available, what models are used, what datasets, what chain configurations, what evaluation metrics are computed. List all files and their purposes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eddfb7d8-a628-44e3-9672-dd3b18e81887",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy7mWeAmqXyH1j6jqMk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4faf36f-cf80-44e2-97f3-a2b5c39c02f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oHvLV1FCdPTDquAQk6BZQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 20781,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 20781,
          "cache_creation_input_tokens": 1624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1624,
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

_source line 21 · 2026-05-21T03:01:20.613Z_

<details><summary>↩ Tool result · `toolu_01N2skgRbDYYXK3N9THHDT7h`</summary>

```text
# Paper Information Summary

**Exact Abstract:**
"As large language models are increasingly responsible for online content, concerns arise about the impact of repeatedly processing their own outputs. Inspired by the "broken telephone" effect in chained human communication, this study investigates whether LLMs similarly distort information through iterative generation. Through translation-based experiments, we find that distortion accumulates over time, influenced by language choice and chain complexity. While degradation is inevitable, it can be mitigated through strategic prompting techniques. These findings contribute to discussions on the long-term effects of AI-mediated information propagation, raising important questions about the reliability of LLM-generated content in iterative workflows."

**Submission Date:** February 27, 2025

**Full Author List:**
1. Amr Mohamed
2. Mingmeng Geng
3. Michalis Vazirgiannis
4. Guokan Shang

**Version Status:** Yes, a second version exists. The paper was initially submitted on February 27, 2025 (v1) and revised on September 15, 2025 (v2). The current page displays version 2. The paper has been accepted to ACL 2025 Main Conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eddfb7d8-a628-44e3-9672-dd3b18e81887",
  "isSidechain": true,
  "promptId": "ee0e299e-1086-42d9-9535-2aa06a2ee3cc",
  "agentId": "a1393d2486eb6b8da",
  "type": "user",
  "uuid": "ffab5e16-7870-4715-8ee9-1b9c335db4ae",
  "sourceToolAssistantUUID": "eddfb7d8-a628-44e3-9672-dd3b18e81887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T03:01:24.120Z_

<details><summary>↩ Tool result · `toolu_01AekLQZWGmowrMFSSDd9TCE`</summary>

````text
# Experimental Setup Summary

## Available Scripts
The repository contains Python scripts organized by experiment type in the `Scripts/` directory:
- **Bilingual Self-loop**: Single model translating between two languages iteratively
- **Bilingual Two-player**: Two different models alternating translations
- **Multilingual Multiplayer**: Three models translating across multiple languages
- **Ablations**: Additional configuration variants
- **Evaluation**: Metrics computation in `Scripts/Evaluation/full_eval/`
- **Visualization**: Plot generation in `Scripts/Visualization/`

## Models Used
Three instruction-tuned LLMs are employed:
- Llama-3.1-8B-Instruct (Meta)
- Mistral-7B-Instruct-v0.2 (MistralAI)
- Gemma-2-9B-it (Google)

## Datasets
The `Datasets/` directory contains `all_data.csv` with subsets used for different experiments, including:
- news2024
- booksum
- scriptbase

## Chain Configurations
Translation chains vary by complexity:
- **Self-loop**: Single model repeating same language pair (e.g., English→French→English)
- **Two-player**: Alternating models on same language pair
- **Multiplayer**: Three models with bridge languages (French, German, Thai, Chinese) shuffled between iterations

## Evaluation Metrics
The system computes textual similarity and factuality measures:
- BLEU, ROUGE, CHR-F, METEOR (standard MT metrics)
- BERTScore (semantic similarity)
- FActScore (factual accuracy assessment)

## File Structure
```
Datasets/       - Data and knowledge sources
Results/        - Outputs, inferences, visualizations
Scripts/        - Python implementation files
requirements.txt - Dependencies
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4faf36f-cf80-44e2-97f3-a2b5c39c02f9",
  "isSidechain": true,
  "promptId": "ee0e299e-1086-42d9-9535-2aa06a2ee3cc",
  "agentId": "a1393d2486eb6b8da",
  "type": "user",
  "uuid": "d5a1828c-001d-4a15-90fa-9b203e8c0b4e",
  "sourceToolAssistantUUID": "c4faf36f-cf80-44e2-97f3-a2b5c39c02f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T03:01:26.860Z_

Now let me get more specific details about the experimental methodology from the HTML version, focusing on sections I need more detail on.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5a1828c-001d-4a15-90fa-9b203e8c0b4e",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy8fTHjtubwwWngwvaZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1794f092-9708-4ede-99a0-3e722f824e81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVVxkCqhG88Sbmx874wLLT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 22405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1104,
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

_source line 24 · 2026-05-21T03:01:32.769Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JCJ1GqAiBMRFErFTTKGgzZ`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.20258v1",
  "prompt": "Focus on these specific details:\n\n1. In the METHODOLOGY section: What exact notations do they use? How do they define a \"chain\"? What is the formal setup?\n\n2. In EXPERIMENT 1 (Bilingual Self-loop): What exact bridge languages are tested? What are the specific FActScore degradation rates per language pair? Any tables with numbers?\n\n3. In EXPERIMENT 2 (Bilingual Two-player): Which model pairs are used? What are the results?\n\n4. In EXPERIMENT 3 (Multilingual Multiplayer): What are the exact settings? How many languages and models in each setting?\n\n5. In ABLATION - Rephrasing: How do they set up rephrasing chains vs translation chains? What are the results?\n\n6. What specific FActScore values or BLEU/BERTScore values are reported at key chain depths (e.g., step 1, step 10, step 50, step 100)?\n\n7. Do they discuss \"attractor states\" or \"convergence\" or \"fixed points\" in the chain?\n\n8. What are the exact prompt templates used?\n\nReport exact numbers from tables and figures wherever possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1794f092-9708-4ede-99a0-3e722f824e81",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEy8fTHjtubwwWngwvaZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34ab5948-009f-4cb6-9d0c-d8f7e5b90710",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVVxkCqhG88Sbmx874wLLT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 22405,
      "output_tokens": 374,
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
          "input_tokens": 1,
          "output_tokens": 374,
          "cache_read_input_tokens": 22405,
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

_source line 25 · 2026-05-21T03:01:48.026Z_

<details><summary>↩ Tool result · `toolu_01JCJ1GqAiBMRFErFTTKGgzZ`</summary>

```text
# Key Technical Details from "LLM as a Broken Telephone"

## 1. METHODOLOGY: Notations and Formal Setup

The paper defines a **translation chain** as N sequential iterations transforming a document. Core notation:
- **Document set**: 𝒟={dᵢ}ᵢ₌₁ᴵ
- **Language set**: ℒ={lⱼ}ⱼ₌₁ᴶ  
- **Model set**: ℳ={mₖ}ₖ₌₁ᴷ

At iteration t, a language sequence ℒ⁽ᵗ⁾=(l₁⁽ᵗ⁾, l₂⁽ᵗ⁾, ..., lⱼ⁽ᵗ⁾) is constructed where the final language returns to the source. The translation operator composes individual translation functions: "𝒯⁽ᵗ⁾=𝒯ₗⱼ←ₗⱼ₋₁ᵐʲ ∘...∘ 𝒯ₗ₁←ₛₒᵤᵣcₑᵐ¹"

## 2. EXPERIMENT 1: Bilingual Self-loop Results

**Bridge languages tested**: French (FR), German (DE), Dutch (NL), Vietnamese (VN), Chinese (ZH), Thai (TH)

**FActScore gradient values** (Table 2) per dataset, showing factuality loss rate:

| Language Pair | News2024 (Llama) | News2024 (Mistral) |
|---|---|---|
| EN↔FR | -0.004 (±0.003) | -0.007 (±0.004) |
| EN↔TH | -0.018 (±0.009) | -0.038 (±0.022) |
| EN↔VN | -0.008 (±0.005) | -0.027 (±0.015) |
| EN↔ZH | -0.011 (±0.006) | -0.024 (±0.012) |

**Key finding**: "Latin script languages...demonstrated superior preservation...compared to those employing non-Latin script."

## 3. EXPERIMENT 2: Bilingual Two-player

**Model pairs**: Llama and Mistral randomly assigned to each translation step

**Selected language pairs**: EN↔FR (lowest distortion) and EN↔TH (highest distortion)

**Results summary**: For French, collaborative chains showed gradient of -0.007 (±0.004), slightly worse than standalone models. For Thai, collaborative gradient was -0.035 (±0.019), better than Mistral alone (-0.038) but worse than Llama alone.

## 4. EXPERIMENT 3: Multilingual Multiplayer Settings

**Setting 1**: ℒ={EN, FR, TH}, ℳ={Llama, Mistral}, chain: EN→l₁→l₂→EN (3 steps per iteration)

**Setting 2**: Same as Setting 1, adds Gemma (total 3 models)

**Setting 3**: ℒ={EN, FR, TH, ZH, DE}, ℳ={Llama, Mistral}, chain: EN→l₁→l₂→l₃→EN (5 steps)

**FActScore gradients at iteration 100**:
- Setting 3: -0.038±0.02 (steepest decline)
- Setting 1: -0.036±0.02
- Setting 2: -0.034±0.02 (slowest—larger model helped)

## 5. Ablation—Rephrasing Chains

Setup: "model is instructed to rephrase a given document while preserving its full meaning." 30 documents sampled from News2024. Four configurations mirror Experiments 1, 2, and 3-Setting 2.

**Result**: "Textual relevance metrics reveal rapid degradation...Among individual models, Llama shows the slowest divergence...combining Llama, Mistral, and Gemma leads to the steepest decline."

## 6. Specific Metric Values at Key Depths

The paper reports FActScore **gradient** (slope) rather than absolute values at specific steps. However, qualitative description states: "By the 10ᵗʰ generation, Setting 3's factuality had dropped to 0.054, and by the 100ᵗʰ generation, it further declined to 0.04."

BLEU, ROUGE-1, and BERTScore are visualized in figures but specific numeric tables at iterations 1, 10, 50, 100 are not extracted in the text.

## 7. Convergence/Attractor States

The paper does **not** discuss fixed-point attractors or convergence to stable states. Instead, it documents "progressive drift from the original source" and continuous degradation. Temperature experiments (Figure 5) show stabilization only at extremely low temperatures (1×10⁻⁶), where "factuality drops slightly...but stabilizes thereafter."

## 8. Exact Prompt Templates

**Base translation prompt** (Figure 13):
"You are a translation expert. Given a passage, a source language, and a target language, translate the passage from the source language to the target language while preserving all the original meaning and without losing any context. Do not write an introduction or a summary. Return only the translated passage."

**Constrained prompt** (Figure 15) adds explicit guidelines: "Do not add, omit, or modify any details from the original paragraph."

**Rephrasing prompt** (Figure 16):
"Given a passage, rephrase it while preserving all the original meaning and without losing any context."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34ab5948-009f-4cb6-9d0c-d8f7e5b90710",
  "isSidechain": true,
  "promptId": "ee0e299e-1086-42d9-9535-2aa06a2ee3cc",
  "agentId": "a1393d2486eb6b8da",
  "type": "user",
  "uuid": "ff5b013e-cbc1-4cb4-84d7-f70fb7254c25",
  "sourceToolAssistantUUID": "34ab5948-009f-4cb6-9d0c-d8f7e5b90710",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-21T03:02:18.677Z_

I now have comprehensive details. Here is the complete extraction:

---

## Paper: "LLM as a Broken Telephone: Iterative Generation Distorts Information"

**ArXiv:** 2502.20258 (v1: Feb 27, 2025; v2: Sep 15, 2025)
**Venue:** ACL 2025 Main Conference

### Full Title and Authors

**Title:** "LLM as a Broken Telephone: Iterative Generation Distorts Information"

**Authors:**
1. Amr Mohamed (MBZUAI)
2. Mingmeng Geng (SISSA)
3. Michalis Vazirgiannis (MBZUAI & Ecole Polytechnique)
4. Guokan Shang (MBZUAI)

### Chain Type

Primarily **translation chains** (back-translation loops), with **rephrasing chains** as an ablation study.

Three experimental configurations:
- **Experiment 1 — Bilingual Self-loop:** Single model translates EN -> bridge language -> EN, repeated for 100 iterations. Bridge languages: French, German, Dutch, Vietnamese, Chinese, Thai.
- **Experiment 2 — Bilingual Two-player:** Two different models alternate translation steps in the same EN <-> bridge language loop. Tested on EN<->FR and EN<->TH.
- **Experiment 3 — Multilingual Multiplayer:** Multiple languages and models in each iteration cycle.
  - Setting 1: L={EN, FR, TH}, M={Llama, Mistral}; chain EN->l1->l2->EN (3 translation steps per iteration)
  - Setting 2: Same languages, M={Llama, Mistral, Gemma} (3 models)
  - Setting 3: L={EN, FR, TH, ZH, DE}, M={Llama, Mistral}; chain EN->l1->l2->l3->EN (5 steps per iteration)

**Ablation — Rephrasing chains:** Model rephrases the same document iteratively (no language switching), tested in standalone and collaborative settings with 30 documents from News2024.

### Feature Space (Metrics)

**Textual relevance metrics:**
- BLEU (incremental error detection)
- ROUGE-1 (word-level omissions)
- CHR-F (character-level deviations)
- METEOR (paraphrastic variations)
- BERTScore (contextual semantic similarity)

**Factuality metric:**
- FActScore (atomic fact verification against the original text; uses Claude 3.5 Sonnet as the judge model)

The primary quantitative analysis uses the **gradient (slope)** of FActScore over iterations to measure degradation rate.

### Analysis Target

**Progressive information distortion through iterative LLM generation** — specifically how factual accuracy and textual fidelity degrade over successive generation steps. They study: (1) degradation rate as a function of bridge language choice, (2) effect of chain complexity (more languages/models), (3) mitigation via prompting and temperature control.

They do NOT study convergence to attractor states or fixed points. The paper documents continuous drift/degradation rather than convergence.

### Generator Scale

- **Llama-3.1-8B-Instruct** (8B parameters) — Meta
- **Mistral-7B-Instruct-v0.2** (7B parameters) — MistralAI
- **Gemma-2-9B-it** (9B parameters) — Google

All are instruction-tuned models in the 7-9B parameter range. No larger models tested.

### Number of Chain Steps

**100 iterations** maximum for all experiments (both translation and rephrasing chains).

### Core Insight

Information distortion accumulates progressively through iterative LLM generation, with degradation rates strongly influenced by the linguistic similarity between source and bridge languages (Latin-script languages like French degrade slowly at -0.004/iteration; non-Latin like Thai degrade rapidly at -0.018 to -0.038/iteration), and while chain complexity and multi-model collaboration amplify distortion, strategic prompting and low temperature can partially mitigate but never eliminate the effect.

### Methodology Details

**Datasets** (150 documents each, 100-200 words per document):
- BookSum (book summaries)
- ScriptBase-alpha (movie scripts)
- BBC News2024 (news articles)

**Key quantitative results (FActScore gradients from Table 2):**

| Language Pair | Llama (News2024) | Mistral (News2024) |
|---|---|---|
| EN<->FR | -0.004 (±0.003) | -0.007 (±0.004) |
| EN<->TH | -0.018 (±0.009) | -0.038 (±0.022) |
| EN<->VN | -0.008 (±0.005) | -0.027 (±0.015) |
| EN<->ZH | -0.011 (±0.006) | -0.024 (±0.012) |

**Temperature ablation:** Tested at 1e-6, 0.25, 0.5, 0.75, 1.0. Near-zero temperature stabilizes factuality after a small initial drop; higher temperature accelerates degradation.

**Prompt variants:** Simple (minimal instruction), Base (detailed translation expert prompt), Constrained (explicitly forbids adding/omitting/modifying details). Constrained prompting reduces degradation rate.

**Connection to model collapse:** The authors explicitly connect their work to the model collapse literature, noting their study addresses the *inference-time* variant — distortion through iterative use of models without retraining — as opposed to the training-time collapse studied by Shumailov et al. They frame it as contributing to "discussions on the long-term effects of AI-mediated information propagation."

**Code:** [github.com/amr-mohamedd/LLM-as-a-Broken-Telephone](https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone)

### Sources
- [ArXiv abstract](https://arxiv.org/abs/2502.20258)
- [ArXiv HTML full text](https://arxiv.org/html/2502.20258v1)
- [ACL Anthology](https://aclanthology.org/2025.acl-long.371/)
- [HuggingFace paper page](https://huggingface.co/papers/2502.20258)
- [GitHub repository](https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff5b013e-cbc1-4cb4-84d7-f70fb7254c25",
  "isSidechain": true,
  "agentId": "a1393d2486eb6b8da",
  "requestId": "req_011CbEyARjbVCuFnVtiHB1S6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f29d47d-d29d-4b11-b2bd-fbbc651fc7ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "2b7c0382-9576-43ca-be40-b30cc0e4127c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHFKwnSGkpDe22cFFg2HVQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1805,
      "cache_read_input_tokens": 23509,
      "output_tokens": 1617,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1805
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1617,
          "cache_read_input_tokens": 23509,
          "cache_creation_input_tokens": 1805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1805,
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
