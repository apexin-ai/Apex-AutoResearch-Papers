# Research conversation: You are helping with a bibliography expansion for an EMNLP 2026 paper on "Generation Depth Fingerprint." Search for **re

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9c20d8349f5ebb86.jsonl`
- **Structured JSON:** [`0660706a3ac89d490fbb.json`](../../sessions/06/0660706a3ac89d490fbb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-20T19:33:12.078Z_

You are helping with a bibliography expansion for an EMNLP 2026 paper on "Generation Depth Fingerprint."

Search for **recent AI text detection / machine-generated text detection surveys published in 2025 or 2026**.

ALREADY CITED surveys:
- Jawahar et al. survey
- Tang et al. survey

Use WebSearch to find 2-3 NEW comprehensive surveys on AI text detection from 2025-2026. These should be published or accepted at major venues, or be widely cited arXiv preprints.

For each paper found, verify it exists by searching for its arXiv ID or DOI. Do NOT fabricate any papers.

For each paper, provide:
- Title
- Authors
- Venue and year
- arXiv ID or DOI (verified)
- One-sentence relevance
- Suggested citation location
- BibTeX entry

Search queries to try:
1. "AI text detection survey 2025"
2. "machine-generated text detection survey 2025 2026"
3. "LLM generated text detection comprehensive survey"
4. "AI-generated content detection survey recent"

Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "2b1321a8-5f64-426a-b979-eb0b4d9f66e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T19:33:12.080Z_

```json
{
  "parentUuid": "2b1321a8-5f64-426a-b979-eb0b4d9f66e9",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
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
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
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
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "2d0a1385-30b4-47f0-90e4-b08d12ed315f",
  "timestamp": "2026-05-20T19:33:12.080Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 3 · 2026-05-20T19:33:14.125Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0164w7Zg9tqR3cn7G3Zc9aNb`</summary>

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
  "parentUuid": "2d0a1385-30b4-47f0-90e4-b08d12ed315f",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENxLRZsfgKJ3gaN5VBe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c05124d-a086-4c63-931d-87e0a2e40f45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01U1DD9E8pzDsKwcqCa4qtKx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7037,
      "cache_read_input_tokens": 9059,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 9059,
          "cache_creation_input_tokens": 7037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7037,
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

_source line 4 · 2026-05-20T19:33:14.127Z_

<details><summary>↩ Tool result · `toolu_0164w7Zg9tqR3cn7G3Zc9aNb`</summary>

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
  "parentUuid": "6c05124d-a086-4c63-931d-87e0a2e40f45",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "89ec318b-f33d-4885-b5a0-ec7f4c96bfd9",
  "sourceToolAssistantUUID": "6c05124d-a086-4c63-931d-87e0a2e40f45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T19:33:16.210Z_

I'll run all four search queries in parallel to find recent AI text detection surveys.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89ec318b-f33d-4885-b5a0-ec7f4c96bfd9",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENxVM6GbB34M9e8E3Fn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb125e85-2047-4eac-a025-be3e3dcf5fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01M55yPTvXNv1xPybMHQrMEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 16096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 6 · 2026-05-20T19:33:16.343Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MQ9Q2pA7gVcgMzqDDKwyHy`</summary>

```json
{
  "query": "AI text detection survey 2025 arXiv comprehensive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb125e85-2047-4eac-a025-be3e3dcf5fb6",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENxVM6GbB34M9e8E3Fn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34908551-e686-48ea-8ac6-06f7d65aef4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01M55yPTvXNv1xPybMHQrMEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 16096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 7 · 2026-05-20T19:33:16.594Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A8Q3bpYXEVLZNybS3NBwjj`</summary>

```json
{
  "query": "machine-generated text detection survey 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34908551-e686-48ea-8ac6-06f7d65aef4a",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENxVM6GbB34M9e8E3Fn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9462a6e1-abeb-4bac-adac-7dc35fc51408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01M55yPTvXNv1xPybMHQrMEY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 16096,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1439
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 16096,
          "cache_creation_input_tokens": 1439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1439,
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

_source line 8 · 2026-05-20T19:33:23.169Z_

<details><summary>↩ Tool result · `toolu_01A8Q3bpYXEVLZNybS3NBwjj`</summary>

```text
Web search results for query: "machine-generated text detection survey 2025 2026"

Links: [{"title":"A Comprehensive Survey of Machine-Generated Text Detection","url":"https://www.researchgate.net/publication/399324725_A_Comprehensive_Survey_of_Machine-Generated_Text_Detection"},{"title":"Machine-Generated Text: A Comprehensive Survey of Threat Models and Detection Methods | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10177704/similar"},{"title":"(PDF) Human or Machine? A Survey on Machine-Generated Text Detection","url":"https://www.researchgate.net/publication/401008191_Human_or_Machine_A_Survey_on_Machine-Generated_Text_Detection"},{"title":"Human or Machine? A Survey on Machine-Generated Text Detection - Penn State","url":"https://pure.psu.edu/en/publications/human-or-machine-a-survey-on-machine-generated-text-detection/"},{"title":"[2210.07321] Machine Generated Text: A Comprehensive Survey of Threat Models and Detection Methods","url":"https://arxiv.org/abs/2210.07321"},{"title":"Are AI Detectors Good Enough? A Survey on Quality of Datasets With   Machine-Generated Texts","url":"https://arxiv.org/pdf/2410.14677"},{"title":"AI-Generated Text Detection: A Comprehensive Review of Active and Passive Approaches - ScienceDirect","url":"https://www.sciencedirect.com/org/science/article/pii/S1546221826000482"},{"title":"Detection of Machine-Generated Text: Literature Survey","url":"https://arxiv.org/pdf/2402.01642"},{"title":"A Survey on AI-Generated Text Detection: Methods, Challenges, and Future Directions","url":"https://www.researchgate.net/publication/400099134_A_Survey_on_AI-Generated_Text_Detection_Methods_Challenges_and_Future_Directions"}]

I found several relevant surveys on machine-generated text detection from 2025-2026. Here are the key findings:

## Recent Survey Publications

A Comprehensive Survey of Machine-Generated Text Detection was published in January 2026.

Ahmad et al. published "Human or Machine? A Survey on Machine-Generated Text Detection" in IEEE Access, 2026, Vol. 14, pp. 34113-34136. This survey includes a linguistic analysis covering phonology, morphology, syntax, semantics, lexicon, and pragmatics that identifies robust MGT signatures such as lower perplexity and simpler morphology, and reviews 30 benchmark corpora totaling over 4 million text samples and 44 empirical studies.

Another survey published on January 12, 2026 reviews recent progress in detection methods, categorizing approaches into passive and active categories based on their reliance on intrinsic textual features or embedded signals.

Additionally, an IEEE survey provides an extensive analysis of threat models posed by contemporary NLG systems and the most complete review of machine-generated text detection methods.

A Survey on AI-Generated Text Detection: Methods, Challenges, and Future Directions was published on November 5, 2025.

These recent surveys collectively address the growing challenge of detecting machine-generated text as generative AI systems become more sophisticated and widely deployed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9462a6e1-abeb-4bac-adac-7dc35fc51408",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "c3fb3fd8-fba2-4300-bca3-ada4e1987d89",
  "sourceToolAssistantUUID": "9462a6e1-abeb-4bac-adac-7dc35fc51408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T19:33:24.246Z_

<details><summary>↩ Tool result · `toolu_01MQ9Q2pA7gVcgMzqDDKwyHy`</summary>

```text
Web search results for query: "AI text detection survey 2025 arXiv comprehensive"

Links: [{"title":"AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification","url":"https://arxiv.org/html/2505.11550v1"},{"title":"A Systematic Survey of AI-Generated Text Detection, Humanization, and Grammar Correction Techniques","url":"https://ijettjournal.org/archive/ijett-v74i3p104"},{"title":"The Imitation Game revisited: A comprehensive survey on recent advances in AI-generated text detection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425003161"},{"title":"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy","url":"https://arxiv.org/html/2603.23146v2"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"AI-Generated Text Detection: A Comprehensive Review of Active and Passive Approaches - ScienceDirect","url":"https://www.sciencedirect.com/org/science/article/pii/S1546221826000482"},{"title":"Detecting AI-Generated Text: Factors Influencing Detectability with   Current Methods","url":"https://arxiv.org/pdf/2406.15583"},{"title":"Towards Possibilities & Impossibilities of AI-generated Text Detection:   A Survey","url":"https://arxiv.org/pdf/2310.15264"}]

I found several relevant resources about AI text detection surveys. Here are the key findings:

## Recent Comprehensive Surveys

A 2025 comprehensive survey titled "The Imitation Game Revisited" by Yang et al. examines recent advances in AI-generated text detection and was published in Expert Systems with Applications.

Wu et al. published a survey on LLM-generated text detection in Computational Linguistics (2025), covering necessity, methods, and future directions.

Another recent survey categorizes detection approaches into passive and active categories based on their reliance on intrinsic textual features or embedded signals, with passive detection divided into surface linguistic feature-based and language model-based methods, while active detection encompasses watermarking-based and semantic retrieval-based approaches.

## Key Challenges Identified

Robustness to domain and generator shift has emerged as one of the most persistent challenges in AI-generated text detection, with multiple studies reporting substantial performance degradation when detectors trained on one dataset are applied to different domains or newly released models.

While previous surveys have provided insights into AI-generated text detection, most are limited to specific application areas like news generation and academic writing, failing to provide a coherent framework for understanding broader progress and trends.

The search results show there are multiple comprehensive surveys published in 2025 on this topic, with papers available on arXiv and in peer-reviewed journals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34908551-e686-48ea-8ac6-06f7d65aef4a",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "86d908aa-2111-43e4-8f1f-77530f312a4e",
  "sourceToolAssistantUUID": "34908551-e686-48ea-8ac6-06f7d65aef4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T19:33:26.353Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0143tp1GT88tDJU8AuaTqtNG`</summary>

```json
{
  "query": "LLM generated text detection comprehensive survey arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86d908aa-2111-43e4-8f1f-77530f312a4e",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENyESvpFJ2h81LDK2Rk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f6354bf-5038-4020-bea7-736c79ca863d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S6ZfZZjb6kwQyf6b8JgSSi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 868,
      "cache_read_input_tokens": 17535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 868,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 11 · 2026-05-20T19:33:26.481Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TJ16hD6eGfvsjvfkkAF36a`</summary>

```json
{
  "query": "\"AI-generated content detection\" survey 2025 arXiv preprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f6354bf-5038-4020-bea7-736c79ca863d",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENyESvpFJ2h81LDK2Rk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c92ba67c-88bc-46db-89af-ebadc1486d35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S6ZfZZjb6kwQyf6b8JgSSi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 868,
      "cache_read_input_tokens": 17535,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 868
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 827,
          "output_tokens": 116,
          "cache_read_input_tokens": 17535,
          "cache_creation_input_tokens": 868,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 868,
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

_source line 12 · 2026-05-20T19:33:33.902Z_

<details><summary>↩ Tool result · `toolu_01TJ16hD6eGfvsjvfkkAF36a`</summary>

```text
Web search results for query: ""AI-generated content detection" survey 2025 arXiv preprint"

Links: [{"title":"[2410.14677v1] Are AI Detectors Good Enough? A Survey on Quality of Datasets With Machine-Generated Texts","url":"https://arxiv.org/abs/2410.14677v1"},{"title":"[2410.14677] Are AI Detectors Good Enough? A Survey on Quality of Datasets With Machine-Generated Texts","url":"https://arxiv.org/abs/2410.14677"},{"title":"A Practical Synthesis of Detecting AI-Generated Textual, ...","url":"https://arxiv.org/pdf/2504.02898"},{"title":"A Comprehensive Dataset for Human vs. AI Generated Text Detection","url":"https://arxiv.org/html/2510.22874v1"},{"title":"[2402.00045] Detecting Multimedia Generated by Large AI Models: A Survey","url":"https://arxiv.org/abs/2402.00045"},{"title":"Detecting AI-Generated Text: Factors Influencing Detectability with   Current Methods","url":"https://arxiv.org/pdf/2406.15583"},{"title":"[2403.01152] A Survey of AI-generated Text Forensic Systems: Detection, Attribution, and Characterization","url":"https://arxiv.org/abs/2403.01152"},{"title":"Detecting AI-Generated Content in Academic Peer Reviews","url":"https://arxiv.org/pdf/2602.00319"},{"title":"AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification","url":"https://arxiv.org/html/2505.11550v1"}]

Based on the search results, I found several relevant 2025 arXiv preprints related to AI-generated content detection:

## Key 2025 arXiv Preprints on AI-Generated Content Detection

1. **"Detecting Multimedia Generated by Large AI Models: A Survey"** (arXiv:2402.00045)
   - This survey examines the rapid advancement of Large AI Models, particularly diffusion models and large language models, and their integration into various aspects of daily life. The paper was last revised in July 2025.

2. **"A Practical Synthesis of Detecting AI-Generated Textual..."** (arXiv:2504.02898)
   - This paper focuses on text-based detection strategies, visual detection methods for AI-generated images and videos, and synthetic audio detection, with a version updated in September 2025.

3. **"A Comprehensive Dataset for Human vs. AI Generated Text Detection"** (arXiv:2510.22874)
   - This work presents a comprehensive dataset comprising over 58,000 text samples that combine authentic New York Times articles with synthetic versions generated by multiple state-of-the-art LLMs.

4. **"Detecting AI-Generated Content in Academic Peer Reviews"** (arXiv:2602.00319)
   - This study observes minimal detection of AI-generated content before 2022, followed by a substantial increase through 2025, with approximately 20% of ICLR reviews and 12% of Nature Communications reviews classified as AI-generated in 2025.

5. **"AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification"** (arXiv:2505.11550)
   - This paper describes a submission to the AI-Generated Text Detection shared task at AAAI 2025 which includes binary and multiclass classification of generative AI content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c92ba67c-88bc-46db-89af-ebadc1486d35",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "1c4d3d46-48a5-4141-9ada-0e1540a1608b",
  "sourceToolAssistantUUID": "c92ba67c-88bc-46db-89af-ebadc1486d35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T19:33:34.246Z_

<details><summary>↩ Tool result · `toolu_0143tp1GT88tDJU8AuaTqtNG`</summary>

```text
Web search results for query: "LLM generated text detection comprehensive survey arXiv 2025"

Links: [{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"A Survey on Detection of LLMs-Generated Content","url":"https://arxiv.org/pdf/2310.15654"},{"title":"[2310.15654] A Survey on Detection of LLMs-Generated Content","url":"https://arxiv.org/abs/2310.15654"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/survey-llm-generated-text-detection-necessity-methods"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"Variation is the Key: A Variation-Based Framework for LLM-Generated Text Detection","url":"https://arxiv.org/pdf/2602.13226"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://arxiv.org/pdf/2310.14724"}]

Based on the search results, I found several relevant surveys on LLM-generated text detection. Here are the key findings:

## Main Survey Results

A comprehensive survey titled "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions" was published in 2025. This survey was authored by Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Lidia Sam Chao, and Derek Fai Wong in Computational Linguistics 2025.

## Survey Scope and Content

The survey consolidates recent research breakthroughs, reviews existing datasets and their limitations, and examines various LLM-generated text detection paradigms, shedding light on challenges like out-of-distribution problems, potential attacks, real-world data issues, and ineffective evaluation frameworks.

The paper comprehensively covers recent advancements in LLM-generated text detection techniques, including watermarking methods that embed unique patterns in generated text, statistics-based detectors that analyze linguistic features, neural-based detectors that use machine learning models to classify text, and human-assisted methods.

## Related Context

LLM-generated text detection aims to discern if a piece of text was produced by an LLM, which is essentially a binary classification task. The growing reliance on LLMs underscores the urgent need for effective detection mechanisms to identify LLM-generated text, critical to mitigating misuse and safeguarding domains like artistic expression and social networks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f6354bf-5038-4020-bea7-736c79ca863d",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "e64386d7-acde-4077-adc0-bdecf6506372",
  "sourceToolAssistantUUID": "9f6354bf-5038-4020-bea7-736c79ca863d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-20T19:33:36.783Z_

Now let me verify the most promising candidates — the Wu et al. Computational Linguistics survey, the "Imitation Game Revisited" paper, and the Ahmad et al. IEEE Access survey.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e64386d7-acde-4077-adc0-bdecf6506372",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENyyCvRofUHPn5BKMDk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2cddf80-be1d-4928-993d-dda725b1a04e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FzhuR3vQiGiredvsqKjAm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 1734,
      "cache_read_input_tokens": 18403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1734,
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

_source line 15 · 2026-05-20T19:33:37.774Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XBfQFmTftFBhRaLi4wqsrz`</summary>

```json
{
  "query": "Wu Yang Zhan \"Survey on LLM-Generated Text Detection\" Computational Linguistics 2025 arXiv 2310.14724"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2cddf80-be1d-4928-993d-dda725b1a04e",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENyyCvRofUHPn5BKMDk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6a8ea34-21dd-426a-96e5-e12da56e472f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FzhuR3vQiGiredvsqKjAm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 1734,
      "cache_read_input_tokens": 18403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1734,
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

_source line 16 · 2026-05-20T19:33:37.933Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GDU3mvHdBmu3ZQ9PTmaJ3i`</summary>

```json
{
  "query": "\"Imitation Game revisited\" AI-generated text detection survey 2025 Expert Systems Applications arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6a8ea34-21dd-426a-96e5-e12da56e472f",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENyyCvRofUHPn5BKMDk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57890640-95e8-424d-b1ef-2051a5cf5414",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FzhuR3vQiGiredvsqKjAm4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 1734,
      "cache_read_input_tokens": 18403,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1734
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 893,
          "output_tokens": 185,
          "cache_read_input_tokens": 18403,
          "cache_creation_input_tokens": 1734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1734,
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

_source line 17 · 2026-05-20T19:33:44.077Z_

<details><summary>↩ Tool result · `toolu_01GDU3mvHdBmu3ZQ9PTmaJ3i`</summary>

```text
Web search results for query: ""Imitation Game revisited" AI-generated text detection survey 2025 Expert Systems Applications arXiv"

Links: [{"title":"The Imitation Game revisited: A comprehensive survey on recent advances in AI-generated text detection","url":"https://ouci.dntb.gov.ua/en/works/4EGm3xLV/"},{"title":"The Imitation Game revisited: A comprehensive survey on recent advances in AI-generated text detection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425003161"},{"title":"GitHub - Nicozwy/AIGTD-Survey: The official GitHub page for the survey paper of AIGTD entitled \"The Imitation Game Revisited: A Comprehensive Survey on Recent Advances in AI-generated Text Detection.\" · GitHub","url":"https://github.com/Nicozwy/AIGTD-Survey"},{"title":"AIGTD-Survey/README.md at main · Nicozwy/AIGTD-Survey","url":"https://github.com/Nicozwy/AIGTD-Survey/blob/main/README.md"},{"title":"ai-generated-text-detection · GitHub Topics · GitHub","url":"https://github.com/topics/ai-generated-text-detection"},{"title":"The Imitation Game revisited: : A comprehensive survey on recent advances in AI-generated text detection: Expert Systems with Applications: An International Journal: Vol 272, No C","url":"https://dl.acm.org/doi/10.1016/j.eswa.2025.126694"},{"title":"The imitation game: Detecting human and AI-generated texts in the era of ChatGPT and BARD | Request PDF","url":"https://www.researchgate.net/publication/378222518_The_imitation_game_Detecting_human_and_AI-generated_texts_in_the_era_of_ChatGPT_and_BARD"},{"title":"(PDF) The Imitation Game: Detecting Human and AI-Generated Texts in the Era of Large Language Models","url":"https://www.researchgate.net/publication/372583505_The_Imitation_Game_Detecting_Human_and_AI-Generated_Texts_in_the_Era_of_Large_Language_Models"},{"title":"The Imitation Game: Detecting Human and AI-Generated Texts in the Era of   ChatGPT and BARD","url":"https://arxiv.org/pdf/2307.12166"},{"title":"Build software better, together","url":"https://github.com/topics/aigtd"}]

I found the paper you're looking for! Here are the search results:

## "The Imitation Game Revisited: A Comprehensive Survey on Recent Advances in AI-Generated Text Detection"

**Publication Details:**
The paper has been accepted to "Expert Systems with Applications" (ESWA, a top-tier SCI journal).

**Citation Information:**
The paper is authored by Zhiwei Yang, Zhengjie Feng, Rongxin Huo, Huiru Lin, Hanghan Zheng, Ruichi Nie, and Hongrui Chen, published in Expert Systems with Applications, Volume 272, pages 126694, in 2025 by Elsevier.

**Content Overview:**
The survey addresses AI-generated text detection (AIGTD), a topic that has attracted increasing attention in recent years with numerous novel methodologies being proposed.

**Resources:**
- An official GitHub page has been created for the survey paper, available at: https://github.com/Nicozwy/AIGTD-Survey
- The paper is also available through ScienceDirect: https://www.sciencedirect.com/science/article/abs/pii/S0957417425003161

The GitHub repository contains organized papers and resources related to the AIGTD survey and continues to be updated with refinements to the survey material.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57890640-95e8-424d-b1ef-2051a5cf5414",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "405a636f-7b90-482c-8234-770a1fd029b0",
  "sourceToolAssistantUUID": "57890640-95e8-424d-b1ef-2051a5cf5414",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T19:33:44.136Z_

<details><summary>↩ Tool result · `toolu_01XBfQFmTftFBhRaLi4wqsrz`</summary>

```text
Web search results for query: "Wu Yang Zhan "Survey on LLM-Generated Text Detection" Computational Linguistics 2025 arXiv 2310.14724"

Links: [{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"(PDF) A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://www.researchgate.net/publication/387905627_A_Survey_on_LLM-Generated_Text_Detection_Necessity_Methods_and_Future_Directions"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future   Directions","url":"https://arxiv.org/pdf/2310.14724"},{"title":"[PDF] A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-LLM-generated-Text-Detection:-Methods,-Wu-Yang/a09d3686285f609b60b18b5935da64b29a5cce0f"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/article/view/2687"},{"title":"A Survey on Detection of LLMs-Generated Content","url":"https://arxiv.org/pdf/2310.15654"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Junchao+Wu%2C+Shu+Yang%2C+Runzhe+Zhan%2C+Yulin+Yuan%2C+Lidia+Sam+Chao%2C+and+Derek+Fai+Wong.+2025.+A+survey+on+LLM-generated+text+detection%3A+Necessity%2C+methods%2C+and+future+directions.+Computational+Linguistics%282025%29%2C+1-65."},{"title":"PREPRINT 1 A Survey on LLM-generated Text Detection:","url":"https://scispace.com/pdf/a-survey-on-llm-generated-text-detection-necessity-methods-k9h782wm19.pdf"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://aclanthology.org/2025.cl-1.8.pdf"}]

I found the paper you're looking for! Here are the details:

The survey "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions" is authored by Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Lidia Sam Chao, and Derek Fai Wong, and was published in Computational Linguistics, 51(1):275–338 in 2025.

The paper is available on arXiv (2310.14724), and it addresses how large language models have rapidly integrated LLM-generated text into daily life, and emphasizes the urgent need for effective detection mechanisms to identify LLM-generated text.

The paper is available through multiple sources including:
- MIT Press (Computational Linguistics journal)
- ACL Anthology
- arXiv
- ResearchGate


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6a8ea34-21dd-426a-96e5-e12da56e472f",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "72b6ae33-3fcd-4913-a639-8c13dbaafc29",
  "sourceToolAssistantUUID": "e6a8ea34-21dd-426a-96e5-e12da56e472f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T19:33:46.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TJDttbFsSMcqMZmKr3oEhK`</summary>

```json
{
  "query": "Ahmad \"Human or Machine\" machine-generated text detection survey IEEE Access 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72b6ae33-3fcd-4913-a639-8c13dbaafc29",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENzhUuHEqvba3YuRgMo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e6f1c08-edc9-4305-a146-4f721512a011",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MzEsUi41y2yFPeMEUYaNSc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 20137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2037,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 20 · 2026-05-20T19:33:47.003Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ps7VC1y4y1nnwJTRH25JLt`</summary>

```json
{
  "query": "\"AI-Generated Text Detection\" \"active and passive\" survey ScienceDirect 2026 arXiv ID"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e6f1c08-edc9-4305-a146-4f721512a011",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbENzhUuHEqvba3YuRgMo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b09bd7dd-791d-4ee5-b60e-232e8b2fcb23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MzEsUi41y2yFPeMEUYaNSc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 992,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 20137,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 992,
          "output_tokens": 132,
          "cache_read_input_tokens": 20137,
          "cache_creation_input_tokens": 2037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2037,
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

_source line 21 · 2026-05-20T19:33:55.946Z_

<details><summary>↩ Tool result · `toolu_01TJDttbFsSMcqMZmKr3oEhK`</summary>

```text
Web search results for query: "Ahmad "Human or Machine" machine-generated text detection survey IEEE Access 2026 arXiv"

Links: [{"title":"Human or Machine? A Survey on Machine-Generated Text Detection - Penn State","url":"https://pure.psu.edu/en/publications/human-or-machine-a-survey-on-machine-generated-text-detection/"},{"title":"(PDF) Human or Machine? A Survey on Machine-Generated Text Detection","url":"https://www.researchgate.net/publication/401008191_Human_or_Machine_A_Survey_on_Machine-Generated_Text_Detection"},{"title":"Human or Machine? A Survey on Machine-Generated Text Detection | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11404135/"},{"title":"Unsupervised and Distributional Detection of Machine-Generated Text","url":"https://arxiv.org/pdf/2111.02878"},{"title":"[2111.02878] Unsupervised and Distributional Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2111.02878"},{"title":"On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/pdf/2304.04736"},{"title":"Human or Machine? Analyzing the Ability to Detect Artificially Generated Text | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-031-98290-3_29"},{"title":"Machine Generated Text: A Comprehensive Survey of Threat Models and   Detection Methods","url":"https://arxiv.org/pdf/2210.07321"}]

I found the publication you're looking for! 

"Human or Machine? A Survey on Machine-Generated Text Detection" by Ahmad Z, Torres-Ruiz M, Mahmood A, Quintero R, Ameer I, and Bölücü N was published in IEEE Access in 2026, volume 14, pages 34113-34136.

The survey addresses how generative AI raises questions about authenticity, ethics, and social impact. It includes a linguistic analysis covering phonology, morphology, syntax, semantics, lexicon, and pragmatics that uncovers machine-generated text signatures such as lower perplexity and simpler morphology. The survey reviews 30 benchmark corpora with over 4 million text samples and 44 empirical studies, including outcomes from six major shared tasks.

Detection approaches are grouped into five broad classes: classical machine learning, deep learning, transformer-based architectures, commercial AI detectors, and statistical tools. Transformer models achieve near-perfect accuracy (approximately 100%), while human evaluators peak at approximately 77% accuracy.

The article is available through IEEE Access under Creative Commons Attribution 4.0 License (DOI 10.1109/ACCESS.2026.3666781).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e6f1c08-edc9-4305-a146-4f721512a011",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "a9e4621b-cd4f-4b28-b34d-611b35c3689f",
  "sourceToolAssistantUUID": "3e6f1c08-edc9-4305-a146-4f721512a011",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T19:33:55.966Z_

<details><summary>↩ Tool result · `toolu_01Ps7VC1y4y1nnwJTRH25JLt`</summary>

```text
Web search results for query: ""AI-Generated Text Detection" "active and passive" survey ScienceDirect 2026 arXiv ID"

Links: [{"title":"AI-Generated Text Detection: A Comprehensive Review of Active and Passive Approaches - ScienceDirect","url":"https://www.sciencedirect.com/org/science/article/pii/S1546221826000482"},{"title":"AI-generated text detection: A comprehensive review of methods, datasets, and applications - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1574013725000693"},{"title":"CMC | Free Full-Text | AI-Generated Text Detection: A Comprehensive Review of Active and Passive Approaches","url":"https://www.techscience.com/cmc/v86n3/65497/html"},{"title":"Detecting AI-Generated Text: Factors Influencing Detectability with   Current Methods","url":"https://arxiv.org/pdf/2406.15583"},{"title":"The Imitation Game revisited: A comprehensive survey on recent advances in AI-generated text detection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425003161"},{"title":"(PDF) AI-Generated Text Detection: A Comprehensive Review of Active and Passive Approaches","url":"https://www.researchgate.net/publication/398443891_AI-Generated_Text_Detection_A_Comprehensive_Review_of_Active_and_Passive_Approaches"},{"title":"Towards Possibilities & Impossibilities of AI-generated Text Detection:   A Survey","url":"https://arxiv.org/pdf/2310.15264"},{"title":"AI Generated Text Detection Adilkhan Alikhanov Department of Computer Science","url":"https://arxiv.org/pdf/2601.03812"}]

Perfect! I found the paper you're looking for. Here are the details:

**Paper Title:** "AI-Generated Text Detection: A Comprehensive Review of Active and Passive Approaches"

**Published:** Volume 86, Issue 3, January 12, 2026

**Journal:** ScienceDirect (appears to be published through Tech Science Press/CMC - Computers, Materials & Continua)

**Authors:** Lingyun Xiang, Nian Li, Yuling Liu, and Jiayong Hu

**DOI:** https://doi.org/10.32604/cmc.2025.073347

The paper categorizes detection approaches into passive and active categories based on their reliance on intrinsic textual features or embedded signals, with passive detection divided into surface linguistic feature-based and language model-based methods, whereas active detection encompasses watermarking-based and semantic retrieval-based approaches.

However, based on the search results, I don't see an arXiv ID associated with this particular paper. The arXiv papers that appeared in the results (like arXiv:2310.15264 and arXiv:2601.03812) are different papers on AI-generated text detection. If you need the arXiv ID for this specific paper, it may not be available on arXiv, as it appears to be published directly through ScienceDirect/Tech Science Press.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b09bd7dd-791d-4ee5-b60e-232e8b2fcb23",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "f2cd2b21-6711-4eca-9226-7a1d100260c2",
  "sourceToolAssistantUUID": "b09bd7dd-791d-4ee5-b60e-232e8b2fcb23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T19:33:58.931Z_

Now let me verify the arXiv ID for Wu et al. and check the DOI for the Ahmad et al. IEEE Access paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2cd2b21-6711-4eca-9226-7a1d100260c2",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbEP1a6RW91Tr6jHNqDLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "316fffa6-17c0-43dc-9de1-3b517d650688",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PiWt8wCjMSp2DzjHrg9z8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2765,
      "cache_read_input_tokens": 22174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2765,
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

_source line 24 · 2026-05-20T19:33:59.361Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EmJZZvK6ipwHEHT7Ph6JSW`</summary>

```json
{
  "query": "arxiv.org 2310.14724 Wu Yang Zhan LLM text detection computational linguistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "316fffa6-17c0-43dc-9de1-3b517d650688",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbEP1a6RW91Tr6jHNqDLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95050a9c-2638-430f-a692-6131349b45b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PiWt8wCjMSp2DzjHrg9z8Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2765,
      "cache_read_input_tokens": 22174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2765,
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

_source line 25 · 2026-05-20T19:33:59.837Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QAy2o6cicFB1TNZxLsgXdT`</summary>

```json
{
  "query": "site:ieeexplore.ieee.org \"Human or Machine\" machine-generated text survey 2026 DOI 10.1109/ACCESS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95050a9c-2638-430f-a692-6131349b45b7",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbEP1a6RW91Tr6jHNqDLn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14a9f6c2-3dd2-46e5-b583-51037db603f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PiWt8wCjMSp2DzjHrg9z8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2765,
      "cache_read_input_tokens": 22174,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2765
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 22174,
          "cache_creation_input_tokens": 2765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2765,
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

_source line 26 · 2026-05-20T19:34:05.501Z_

<details><summary>↩ Tool result · `toolu_01QAy2o6cicFB1TNZxLsgXdT`</summary>

```text
Web search results for query: "site:ieeexplore.ieee.org "Human or Machine" machine-generated text survey 2026 DOI 10.1109/ACCESS"

Links: [{"title":"Human or Machine? A Survey on Machine-Generated Text Detection | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11404135/"},{"title":"Unsupervised and Distributional Detection of Machine-Generated Text","url":"https://arxiv.org/pdf/2111.02878"},{"title":"Beyond Turing: A Comparative Analysis of Approaches for Detecting   Machine-Generated Text","url":"https://arxiv.org/pdf/2311.12373"},{"title":"Detection of Machine-Generated Text: Literature Survey","url":"https://arxiv.org/pdf/2402.01642"},{"title":"Are AI Detectors Good Enough? A Survey on Quality of Datasets With   Machine-Generated Texts","url":"https://arxiv.org/pdf/2410.14677"},{"title":"Detecting Machine-Generated Texts: Not Just \"AI vs Humans\" and Explainability is Complicated","url":"https://arxiv.org/pdf/2406.18259"},{"title":"Machine Generated Text: A Comprehensive Survey of Threat Models and   Detection Methods","url":"https://arxiv.org/pdf/2210.07321"},{"title":"All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated   Text","url":"https://arxiv.org/pdf/2107.00061"}]

Perfect! I found the IEEE paper you were looking for. Here's what the search returned:

The first result is a survey on machine-generated text detection that addresses how generative AI advances across education, research, medicine, and journalism raise questions about authenticity, ethics, and social impact.

The paper conducted a linguistic analysis covering phonology, morphology, syntax, semantics, lexicon, and pragmatics, uncovering robust machine-generated text signatures such as lower perplexity and simpler morphology. The survey reviews 30 benchmark corpora totaling over 4 million text samples and 44 empirical studies, including outcomes from six major shared tasks.

Detection approaches are grouped into five broad classes: classical machine learning, deep learning, transformer-based architectures, commercial AI detectors, and statistical tools, with transformer models achieving near-perfect accuracy while human evaluators peak at approximately 77% accuracy.

The paper is available at: https://ieeexplore.ieee.org/document/11404135/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14a9f6c2-3dd2-46e5-b583-51037db603f9",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "7603d106-49a0-423b-9f00-66f8fe7d8615",
  "sourceToolAssistantUUID": "14a9f6c2-3dd2-46e5-b583-51037db603f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T19:34:07.137Z_

<details><summary>↩ Tool result · `toolu_01EmJZZvK6ipwHEHT7Ph6JSW`</summary>

```text
Web search results for query: "arxiv.org 2310.14724 Wu Yang Zhan LLM text detection computational linguistics"

Links: [{"title":"[2310.14724v2] A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724v2"},{"title":"[PDF] A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-LLM-generated-Text-Detection:-Methods,-Wu-Yang/a09d3686285f609b60b18b5935da64b29a5cce0f"},{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"[2310.14724v3] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724v3"},{"title":"LLM-generated-Text-Detection/README.md at main · NLP2CT/LLM-generated-Text-Detection","url":"https://github.com/NLP2CT/LLM-generated-Text-Detection/blob/main/README.md"},{"title":"LLM-Detector: Improving AI-Generated Chinese Text Detection with   Open-Source LLM Instruction Tuning","url":"https://arxiv.org/pdf/2402.01158"},{"title":"DPIC: Decoupling Prompt and Intrinsic Characteristics for LLM Generated   Text Detection","url":"https://arxiv.org/pdf/2305.12519"},{"title":"dblp: A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions.","url":"https://dblp.org/rec/journals/corr/abs-2310-14724.html"}]

Based on the search results, here's what I found:

The paper arxiv.org 2310.14724 is titled "A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions" and was authored by Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Derek F. Wong, and Lidia S. Chao.

The paper focuses on LLM-generated text detection, which aims to discern if a piece of text was produced by an LLM—essentially a binary classification task. The survey discusses detector techniques including watermarking techniques, zero-shot methods, fine-tuning LMs methods, adversarial learning methods, LLMs as detectors, and human-assisted methods.

The survey paper was accepted by the Computational Linguistics Journal, and it addresses the need to mitigate potential misuse of LLMs and safeguard realms like artistic expression and social networks from harmful influence of LLM-generated content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95050a9c-2638-430f-a692-6131349b45b7",
  "isSidechain": true,
  "promptId": "962427aa-d732-47f7-941b-01657c796c3a",
  "agentId": "a9c20d8349f5ebb86",
  "type": "user",
  "uuid": "c1789820-749a-4f7e-b698-eb31aff4ec64",
  "sourceToolAssistantUUID": "95050a9c-2638-430f-a692-6131349b45b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T19:34:40.313Z_

Now I have enough verified information. The three candidates are:

1. **Wu et al.** — arXiv:2310.14724, published in *Computational Linguistics* 51(1):275–338, 2025. Fully verified.
2. **Yang et al. "Imitation Game Revisited"** — *Expert Systems with Applications* Vol. 272, 2025, DOI: 10.1016/j.eswa.2025.126694. Fully verified.
3. **Ahmad et al. "Human or Machine?"** — *IEEE Access* Vol. 14, pp. 34113–34136, 2026, DOI: 10.1109/ACCESS.2026.3666781, IEEE Xplore doc 11404135. Verified.

Note: Wu et al. (arXiv:2310.14724) is likely the same as the "Tang et al." or "Jawahar et al." already-cited survey — need to confirm it isn't already cited. The already-cited surveys are Jawahar et al. and Tang et al., so Wu et al. (Computational Linguistics, 2025) is new.

---

Here are **3 verified new surveys** on AI text detection from 2025–2026:

---

## 1. Wu et al. (2025) — Computational Linguistics

**Title:** A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions

**Authors:** Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Derek F. Wong, Lidia S. Chao

**Venue:** *Computational Linguistics*, 51(1):275–338, 2025 (MIT Press / ACL Anthology: 2025.cl-1.8)

**arXiv ID:** [2310.14724](https://arxiv.org/abs/2310.14724) (v3 = journal version)

**Relevance:** The most authoritative peer-reviewed survey in an ACL-affiliated journal; covers watermarking, zero-shot, fine-tuning, and adversarial detection paradigms with a systematic taxonomy — directly contextualizes the detection landscape that generation-depth fingerprinting operates within.

**Suggested citation location:** Introduction or Related Work, when situating the paper among existing detection approaches and motivating why generation-depth is an underexplored axis.

**BibTeX:**
```bibtex
@article{wu-etal-2025-survey,
  title     = {A Survey on {LLM}-Generated Text Detection:
               Necessity, Methods, and Future Directions},
  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and
               Yuan, Yulin and Wong, Derek F. and Chao, Lidia S.},
  journal   = {Computational Linguistics},
  volume    = {51},
  number    = {1},
  pages     = {275--338},
  year      = {2025},
  publisher = {MIT Press},
  doi       = {10.1162/coli_a_00549},
  url       = {https://aclanthology.org/2025.cl-1.8}
}
```

---

## 2. Yang et al. (2025) — Expert Systems with Applications

**Title:** The Imitation Game Revisited: A Comprehensive Survey on Recent Advances in AI-Generated Text Detection

**Authors:** Zhiwei Yang, Zhengjie Feng, Rongxin Huo, Huiru Lin, Hanghan Zheng, Ruichi Nie, Hongrui Chen

**Venue:** *Expert Systems with Applications*, Vol. 272, Article 126694, 2025 (Elsevier)

**DOI:** [10.1016/j.eswa.2025.126694](https://doi.org/10.1016/j.eswa.2025.126694)

**GitHub:** https://github.com/Nicozwy/AIGTD-Survey

**Relevance:** Comprehensive taxonomy of recent AIGTD methods with an actively maintained paper list; useful as the broadest empirical backdrop citation when claiming that existing surveys do not characterize generation depth as a fingerprint dimension.

**Suggested citation location:** Introduction ("existing surveys have taxonomized detectors by feature type but not by generative depth") or a Related Work paragraph on passive detection.

**BibTeX:**
```bibtex
@article{yang2025imitation,
  title   = {The Imitation Game Revisited: A Comprehensive Survey on
             Recent Advances in {AI}-Generated Text Detection},
  author  = {Yang, Zhiwei and Feng, Zhengjie and Huo, Rongxin and
             Lin, Huiru and Zheng, Hanghan and Nie, Ruichi and Chen, Hongrui},
  journal = {Expert Systems with Applications},
  volume  = {272},
  pages   = {126694},
  year    = {2025},
  publisher = {Elsevier},
  doi     = {10.1016/j.eswa.2025.126694}
}
```

---

## 3. Ahmad et al. (2026) — IEEE Access

**Title:** Human or Machine? A Survey on Machine-Generated Text Detection

**Authors:** Z. Ahmad, M. Torres-Ruiz, A. Mahmood, R. Quintero, I. Ameer, N. Bölücü

**Venue:** *IEEE Access*, Vol. 14, pp. 34113–34136, 2026

**DOI:** [10.1109/ACCESS.2026.3666781](https://doi.org/10.1109/ACCESS.2026.3666781) | [IEEE Xplore 11404135](https://ieeexplore.ieee.org/document/11404135/)

**Relevance:** Most recent (2026) survey; reviews 30 benchmark corpora (>4 M samples) and 44 empirical studies across five detector classes; its linguistic analysis of MGT signatures (lower perplexity, simpler morphology) directly frames why deeper structural signals like generation depth may be more robust.

**Suggested citation location:** Introduction or §2 Related Work when citing the state-of-the-art detection landscape and motivating the need for complementary structural fingerprinting.

**BibTeX:**
```bibtex
@article{ahmad2026human,
  title   = {Human or Machine? {A} Survey on Machine-Generated Text Detection},
  author  = {Ahmad, Zeeshan and Torres-Ruiz, Marco and Mahmood, Adeel and
             Quintero, Rolando and Ameer, Iqra and B{\"{o}}l{\"{u}}c{\"{u}}, Nilufar},
  journal = {IEEE Access},
  volume  = {14},
  pages   = {34113--34136},
  year    = {2026},
  doi     = {10.1109/ACCESS.2026.3666781}
}
```

---

**Notes on verification:**
- Wu et al. arXiv:2310.14724 confirmed live on arxiv.org with v3 (journal version).
- Yang et al. DOI 10.1016/j.eswa.2025.126694 confirmed on ScienceDirect and ACM DL.
- Ahmad et al. DOI 10.1109/ACCESS.2026.3666781 confirmed on IEEE Xplore (doc 11404135), open-access CC-BY 4.0.
- All three are distinct from Jawahar et al. and Tang et al.

Sources:
- [arXiv:2310.14724](https://arxiv.org/abs/2310.14724)
- [ACL Anthology 2025.cl-1.8](https://aclanthology.org/2025.cl-1.8/)
- [Computational Linguistics (MIT Press)](https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity)
- [Expert Systems with Applications — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417425003161)
- [AIGTD-Survey GitHub](https://github.com/Nicozwy/AIGTD-Survey)
- [IEEE Xplore 11404135](https://ieeexplore.ieee.org/document/11404135/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1789820-749a-4f7e-b698-eb31aff4ec64",
  "isSidechain": true,
  "agentId": "a9c20d8349f5ebb86",
  "requestId": "req_011CbEP2Pqov8r9WiJgxjzBo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80428c5b-a3f0-4687-9b58-b5695f08677a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "45e35366-fb43-404b-90c5-d5a1f36ff8d5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VdGPFgBjEpvNCpKWKgTfRQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 644,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 24939,
      "output_tokens": 2056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 949
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 644,
          "output_tokens": 2056,
          "cache_read_input_tokens": 24939,
          "cache_creation_input_tokens": 949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 949,
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
