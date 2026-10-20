# Research conversation: Search for recent papers (2025-2026) on type-conditioned or category-conditioned program repair and retrieval-augmented 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-abf2c5b9b247b50e7.jsonl`
- **Structured JSON:** [`e537bbcce3f8901fbb65.json`](../../sessions/e5/e537bbcce3f8901fbb65.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-10T06:27:14.558Z_

Search for recent papers (2025-2026) on type-conditioned or category-conditioned program repair and retrieval-augmented repair. I need to find any work that may be concurrent with or supersede this idea about partitioning retrieval indices by bug type.

Key search queries to run:
1. "type-conditioned program repair" site:arxiv.org 2025 2026
2. "bug type retrieval augmented repair" arxiv 2025 2026
3. "failure type code repair retrieval" arxiv 2026
4. "categorical retrieval program repair" arxiv 2026
5. "bug classification repair retrieval" arxiv 2025

Also search:
- site:paperswithcode.com "program repair" SOTA
- "retrieval augmented program repair" arxiv 2026
- "SWE-bench 2026 repair" to find latest SOTA methods

For each relevant paper found, report: title, arxiv ID, venue/date, and how similar it is to the FTCR approach (classifying bugs by type, then retrieving from type-specific partitioned index).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "8c17aedb-2ee8-4ab6-80ff-b65b1177d397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T06:27:15.896Z_

I'll search for recent papers on type-conditioned and category-conditioned program repair with retrieval-augmented approaches. Let me run these searches efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c17aedb-2ee8-4ab6-80ff-b65b1177d397",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQvzoVdKVJBbWS1AT7Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5939e490-0114-4b92-ba4c-7a54dac33947",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015doHswKyJR8wVQwvjvnmrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T06:27:16.094Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019eBah1JFGW1WZaZ7zCYfzW`</summary>

```json
{
  "query": "type-conditioned program repair arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5939e490-0114-4b92-ba4c-7a54dac33947",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQvzoVdKVJBbWS1AT7Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7590d0f2-1f84-4e25-9805-a8b8407a3a32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015doHswKyJR8wVQwvjvnmrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T06:27:16.100Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JNziL7QDaML2JDWHh1pAK6`</summary>

```json
{
  "query": "bug type retrieval augmented repair arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7590d0f2-1f84-4e25-9805-a8b8407a3a32",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQvzoVdKVJBbWS1AT7Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ba6a8d1b-6186-4f06-aa46-954574aa6320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015doHswKyJR8wVQwvjvnmrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T06:27:16.295Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ppodm8tL2nx9wwsFFA1opD`</summary>

```json
{
  "query": "failure type code repair retrieval arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba6a8d1b-6186-4f06-aa46-954574aa6320",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQvzoVdKVJBbWS1AT7Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "07bfccf6-3712-4e87-940c-ef439cddcf88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015doHswKyJR8wVQwvjvnmrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T06:27:16.533Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QzsZFDWkwNNYSe29aSUdvv`</summary>

```json
{
  "query": "categorical retrieval program repair arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07bfccf6-3712-4e87-940c-ef439cddcf88",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQvzoVdKVJBbWS1AT7Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b8b94829-60db-4a6d-ac24-402ec82a9742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015doHswKyJR8wVQwvjvnmrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T06:27:16.769Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014to4SSb2FsWk99WRcpwgsH`</summary>

```json
{
  "query": "bug classification repair retrieval arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8b94829-60db-4a6d-ac24-402ec82a9742",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQvzoVdKVJBbWS1AT7Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5be04f83-3e38-4bc2-9bca-b72cab4c186f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015doHswKyJR8wVQwvjvnmrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T06:27:16.773Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011zs3jxHLszSuTBcEo6LTro`</summary>

```json
{
  "query": "retrieval augmented program repair arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5be04f83-3e38-4bc2-9bca-b72cab4c186f",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQvzoVdKVJBbWS1AT7Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "87fa02bb-b61f-46fa-88c7-7f98739a88b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015doHswKyJR8wVQwvjvnmrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T06:27:16.979Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YH46tLFWisyHK6sScuVw6J`</summary>

```json
{
  "query": "SWE-bench program repair SOTA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87fa02bb-b61f-46fa-88c7-7f98739a88b7",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQvzoVdKVJBbWS1AT7Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "89cb7980-bdd4-4467-a455-e69c3fcc4ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015doHswKyJR8wVQwvjvnmrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T06:27:17.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018hsoz7pabyzTSP3BRGpo7h`</summary>

```json
{
  "query": "program repair paperswithcode leaderboard 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89cb7980-bdd4-4467-a455-e69c3fcc4ae0",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQvzoVdKVJBbWS1AT7Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "05ebbcdd-0b7c-4fc4-9e70-9106aca27b62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015doHswKyJR8wVQwvjvnmrx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 16155,
      "output_tokens": 418,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 418,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 680,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T06:27:22.936Z_

<details><summary>↩ Tool result · `toolu_018hsoz7pabyzTSP3BRGpo7h`</summary>

```text
Web search results for query: "program repair paperswithcode leaderboard 2026"

Links: [{"title":"Program Repair","url":"https://paperswithcode.com/task/program-repair"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"Program Repair | Papers With Code","url":"https://paperswithcode.com/task/program-repair?page=2"},{"title":"Papers with Code is Dead — Best Alternatives 2026 by Use Case | Codesota | CodeSOTA","url":"https://www.codesota.com/papers-with-code"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"LEGOBench: Leaderboard Generation Benchmark for Scientific Models","url":"https://arxiv.org/html/2401.06233v1"},{"title":"An Exploratory Study of Foundation Model Leaderboards","url":"https://www.computer.org/csdl/journal/ts/2025/04/10855627/23QQWoayUFy"},{"title":"Trending Papers - Hugging Face","url":"https://huggingface.co/papers/trending"},{"title":"Papers with Code","url":"https://paperswithcode.co/"},{"title":"Papers with code · GitHub","url":"https://github.com/paperswithcode"}]

Based on the search results, here's what I found:

Papers with Code was shut down by Meta on July 24-25, 2025, and its 9,327 benchmark leaderboards are no longer served from the canonical URL. The domain now redirects to Hugging Face Trending Papers; the leaderboards are gone.

However, the search results do show that there was a Program Repair leaderboard on Papers with Code. Recent research from Shanghai Jiao Tong University published on May 4, 2026 discusses ARIS, an open-source research harness for program repair. Additionally, research has analyzed SWE-Bench, which uses GitHub issue repair tasks and maintains public leaderboards that rank submissions based on their performance.

If you're looking for current program repair benchmarks and leaderboards, you may want to check SWE-Bench (swebench.com) or alternative platforms like CodeSOTA, as the original Papers with Code platform is no longer operational.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05ebbcdd-0b7c-4fc4-9e70-9106aca27b62",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "cbcc2918-c893-4aa6-8d3d-385b595a8ec2",
  "sourceToolAssistantUUID": "05ebbcdd-0b7c-4fc4-9e70-9106aca27b62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T06:27:23.211Z_

<details><summary>↩ Tool result · `toolu_01JNziL7QDaML2JDWHh1pAK6`</summary>

```text
Web search results for query: "bug type retrieval augmented repair arxiv 2025 2026"

Links: [{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"[2504.09651] GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, Triage, and More","url":"https://arxiv.org/abs/2504.09651"},{"title":"RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code","url":"https://arxiv.org/html/2509.16701v1"},{"title":"Learner-Tailored Program Repair: A Solution Generator with","url":"https://arxiv.org/pdf/2601.08545"},{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304v1"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Past, Present, and Future of Bug Tracking in the Generative AI Era","url":"https://arxiv.org/html/2510.08005v2"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"}]

I found several relevant papers from 2025-2026 on bug type and retrieval-augmented repair. Here are the key findings:

## Major Research Areas

**Retrieval-Augmented Program Repair:**

ReAPR is a retrieval-augmented framework for automatic program repair that leverages a retriever to fetch bug-fix pairs similar to the target bug from a retrieval database, providing contextual hints to guide LLMs in the repair process.

RelRepair is a novel retrieval-augmented APR approach designed to enhance LLM-based repair effectiveness by systematically retrieving relevant information from the project's code repository, specifically identifying and integrating function signatures and related code snippets.

**Recent Survey Work:**

A recent survey categorizes 63 LLM-based APR systems published from January 2022 to June 2025 into four paradigms, showing how retrieval- or analysis-augmented contexts strengthen any of them.

Retrieval-Augmented Generation (RAG) augments the LLM's input with external knowledge such as relevant code snippets, documentation, or historical fixes, while Analysis-Augmented Generation (AAG) involves incorporating program static or dynamic analysis results into the prompt.

**Bug Report Datasets:**

GitBugs is a comprehensive dataset comprising over 150,000 bug reports from nine actively maintained open-source projects, aggregating data from Github, Bugzilla and Jira issue trackers.

These papers represent the latest advances in applying retrieval-augmented techniques to automated program repair, with emphasis on leveraging historical bug-fix information and code context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba6a8d1b-6186-4f06-aa46-954574aa6320",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "0969a0f2-b0cd-410e-a6d7-73434c667637",
  "sourceToolAssistantUUID": "ba6a8d1b-6186-4f06-aa46-954574aa6320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T06:27:23.342Z_

<details><summary>↩ Tool result · `toolu_019eBah1JFGW1WZaZ7zCYfzW`</summary>

```text
Web search results for query: "type-conditioned program repair arxiv 2025 2026"

Links: [{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"[2505.02931] The Art of Repair: Optimizing Iterative Program Repair with Instruction-Tuned Models","url":"https://arxiv.org/abs/2505.02931"},{"title":"A Systematic Literature Review on Large Language Models for Automated Program Repair","url":"https://arxiv.org/html/2405.01466v4"},{"title":"Gradient-Based Program Repair: Fixing Bugs in Continuous Program Spaces","url":"https://arxiv.org/html/2505.17703v3"},{"title":"[2506.23749v1] A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/abs/2506.23749v1"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=7600&show=2000"},{"title":"[2506.23749] A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/abs/2506.23749"},{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"Optimizing Iterative Program Repair with Instruction-Tuned ...","url":"https://arxiv.org/pdf/2505.02931"}]

Based on the search results, I found several recent arxiv papers related to program repair from 2025-2026, though I didn't find a paper specifically titled "type-conditioned program repair." Here are the most relevant findings:

## Key Program Repair Papers (2025-2026)

**Survey Papers:**
A comprehensive survey published in June 2025 categorizes 63 LLM-based APR systems from January 2022 to June 2025 into four paradigms, and a systematic literature review conducted the first review with 189 high-quality APR papers that utilize recent LLMs from 2020 to September 2025.

**Recent Studies:**
- A May 2025 paper investigates an APR pipeline using instruction-tuned LLMs (DeepSeekCoder-Instruct, Codellama-Instruct, Llama3.1-Instruct) with fine-tuning on datasets of varying sizes (1K, 30K, 65K) using Full Fine-Tuning and LoRA techniques.

- Another paper discusses program repair or automatic bug fixing, noting that recent years have seen dramatic improvements in patch quality and complexity thanks to learning-based program repair, with frontier LLMs repairing the most complex bugs.

The search results show an active area of research in LLM-based program repair with multiple recent publications, though the specific "type-conditioned" variant you asked about doesn't appear in the top results. If you'd like more specific information about type-conditioned approaches to program repair, I can conduct another search with different terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7590d0f2-1f84-4e25-9805-a8b8407a3a32",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "656f4860-00b3-4fe9-b3fd-0254ca4b9f8a",
  "sourceToolAssistantUUID": "7590d0f2-1f84-4e25-9805-a8b8407a3a32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T06:27:23.426Z_

<details><summary>↩ Tool result · `toolu_011zs3jxHLszSuTBcEo6LTro`</summary>

```text
Web search results for query: "retrieval augmented program repair arxiv 2026"

Links: [{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"[2604.10481] PatchRecall: Patch-Driven Retrieval for Automated Program Repair","url":"https://arxiv.org/abs/2604.10481"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"[2601.08545] Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/abs/2601.08545"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"Improving LLM-Assisted Secure Code Generation through ...","url":"https://www.arxiv.org/pdf/2601.00509"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"[2602.08866] ArkEval: Benchmarking and Evaluating Automated CodeRepair for ArkTS","url":"https://arxiv.org/abs/2602.08866"},{"title":"Repair Ingredients Are All You Need: Improving Large Language Model-Based Program Repair via Repair Ingredients Search","url":"https://arxiv.org/html/2506.23100"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"}]

Based on the search results, here are some key findings about retrieval-augmented program repair research on arXiv in 2026:

## Recent Papers on Retrieval-Augmented Program Repair

Several notable papers have been published on this topic:

1. **PatchRecall: Patch-Driven Retrieval for Automated Program Repair** (April 2026)
   - Retrieving the correct set of files from a large codebase is a crucial step in Automated Program Repair (APR), with high recall necessary to ensure relevant files are included, but simply increasing retrieved files introduces noise and degrades efficiency. PatchRecall proposes a hybrid retrieval approach that balances recall with conciseness by combining codebase retrieval and history-based retrieval strategies.

2. **ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation** (September 2025)
   - Retrieval-augmented generation (RAG), with its efficient in-context learning paradigm, offers a more scalable alternative to code repair approaches with high training costs or computationally expensive inference.

3. **Learner-Tailored Program Repair** (January 2026)
   - This work proposes an Iterative Retrieval Enhancement method that utilizes evaluation results of generated code to iteratively optimize the retrieval direction and explore more suitable repair strategies.

4. **Survey on Retrieval-Augmented Code Generation** (October 2025)
   - Tasks such as automatic program repair and repository-wide refactoring are important applications of retrieval-augmented code generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87fa02bb-b61f-46fa-88c7-7f98739a88b7",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "2fe02d01-4f21-4616-bf7d-26dfc883de49",
  "sourceToolAssistantUUID": "87fa02bb-b61f-46fa-88c7-7f98739a88b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T06:27:23.781Z_

<details><summary>↩ Tool result · `toolu_01YH46tLFWisyHK6sScuVw6J`</summary>

```text
Web search results for query: "SWE-bench program repair SOTA 2026"

Links: [{"title":"[2602.04449] What's in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/abs/2602.04449"},{"title":"SWE-bench Leaderboard: AI Coding Agent SOTA Results | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/browse/agentic/swe-bench"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench-Verified Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-verified-f1d87e7f-d600-4831-973d-249d445ba3d0"},{"title":"2026-1-27 SWE-EVO: Benchmarking Coding Agents in","url":"https://arxiv.org/pdf/2512.18470"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench-lite Benchmark (Bug fixing)","url":"https://paperswithcode.com/sota/bug-fixing-on-swe-bench"},{"title":"SWE-BENCH+: ENHANCED CODING BENCHMARK","url":"https://openreview.net/pdf/7b25f35e8d13c2c33d84177f371a0c76252ba1f4.pdf"}]

Based on the search results, here's what I found about SWE-bench program repair SOTA in 2026:

## Current State-of-the-Art Performance

Claude Mythos Preview from Anthropic currently leads the SWE-Bench Verified leaderboard with a score of 93.9%, followed by Claude Opus 4.7 at 87.6% and Claude Opus 4.5 at 80.9%.

For the broader SWE-Bench ecosystem, Claude Opus 4.5 achieves 79.2% with live-SWE-agent or Sonar and 76.8% in the mini-SWE-agent v2 bash-only slice.

## Key Findings on Program Repair Progress

State-of-the-art results on both leaderboards are currently achieved by Claude 4 Sonnet, with a clear dominance of proprietary LLMs, especially Claude family. Submissions are primarily from industry, often using proprietary LLMs (e.g., Anthropic Claude, GPT-4 variants).

## Recent Developments

Recent research has identified quality issues with SWE-Bench datasets that may affect evaluation reliability. In 60.83% of resolved instances, solutions were either explicitly stated or subtly implied within issue reports or comments, and in 47.93% of resolved instances, weak tests allowed incorrect or incomplete changes to pass.

Additionally, a new benchmark called SWE-EVO has emerged that emphasizes long-term adaptability and multi-agent orchestration, unlike SWE-Bench's focus on single-issue fixes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89cb7980-bdd4-4467-a455-e69c3fcc4ae0",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "f0dd6a71-8100-4824-8304-358e301b56f1",
  "sourceToolAssistantUUID": "89cb7980-bdd4-4467-a455-e69c3fcc4ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T06:27:24.094Z_

<details><summary>↩ Tool result · `toolu_01Ppodm8tL2nx9wwsFFA1opD`</summary>

```text
Web search results for query: "failure type code repair retrieval arxiv 2026"

Links: [{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback","url":"https://arxiv.org/html/2601.00509"},{"title":"Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/html/2601.08545.pdf"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.23932"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Doctor-RAG: Failure-Aware Repair for Agentic Retrieval-Augmented Generation","url":"https://arxiv.org/html/2604.00865"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"[2602.08866] ArkEval: Benchmarking and Evaluating Automated CodeRepair for ArkTS","url":"https://arxiv.org/abs/2602.08866"},{"title":"Improving LLM-Assisted Secure Code Generation through ...","url":"https://www.arxiv.org/pdf/2601.00509"}]

I found several relevant papers from arXiv 2026 related to code repair and retrieval. Here are the key results:

## Recent Papers on Code Repair and Retrieval (2026)

1. **Doctor-RAG: Failure-Aware Repair for Agentic Retrieval-Augmented Generation** - How to repair a failed agentic RAG trajectory in a fine-grained and cost-efficient manner remains underexplored, with this paper addressing failure detection and repair mechanisms.

2. **ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair** - Reasoning-guided approaches generate structured, bug-specific explanations before ranking candidate locations, demonstrating that prompting the model to reason about why a location is relevant improves accuracy over purely similarity-based retrieval.

3. **ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation** - ReCode first determines the algorithm of the wrong code to narrow the subset of a constructed code knowledge base, then the exemplar retrieved through dual-view fused feature is connected with the user's query to prompt the LLM to give final solutions.

4. **Learner-Tailored Program Repair** - This proposes an iterative retrieval enhancement method, which iteratively retrieves repair strategies that match the current generated incorrect code, thereby improving both usability and repair performance.

5. **ArkEval: Benchmarking and Evaluating Automated Code Repair for ArkTS** - Four state-of-the-art Large Language Models were evaluated on a benchmark using a retrieval-augmented repair workflow.

These papers represent the latest research in failure type code repair and retrieval-augmented approaches for automated program repair in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07bfccf6-3712-4e87-940c-ef439cddcf88",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "91e19c54-c546-4828-8d9c-eb6004d6f6ce",
  "sourceToolAssistantUUID": "07bfccf6-3712-4e87-940c-ef439cddcf88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T06:27:24.540Z_

<details><summary>↩ Tool result · `toolu_014to4SSb2FsWk99WRcpwgsH`</summary>

```text
Web search results for query: "bug classification repair retrieval arxiv 2025"

Links: [{"title":"Learner-Tailored Program Repair: A Solution Generator with","url":"https://arxiv.org/pdf/2601.08545"},{"title":"Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/html/2601.08545.pdf"},{"title":"[2504.09651] GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, Triage, and More","url":"https://arxiv.org/abs/2504.09651"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Past, Present, and Future of Bug Tracking in the Generative AI Era","url":"https://arxiv.org/html/2510.08005v2"},{"title":"Combining Retrieval and Classification: Balancing Efficiency and Accuracy in Duplicate Bug Report Detection","url":"https://arxiv.org/html/2404.14877"},{"title":"Combining Retrieval and Classification: Balancing Efficiency and Accuracy in","url":"https://arxiv.org/pdf/2404.14877"},{"title":"Challenging Bug Prediction and Repair Models with Synthetic Bugs","url":"https://arxiv.org/html/2310.02407"},{"title":"When Deep Learning Meets Information Retrieval-based Bug Localization: A Survey","url":"https://arxiv.org/html/2505.00144v1"},{"title":"Adversarial Bug Reports as a Security Risk in Language ...","url":"https://arxiv.org/pdf/2509.05372"}]

Based on the search results, I found several relevant 2025 arXiv papers related to bug classification, repair, and retrieval:

## Key Papers Found:

1. **Learner-Tailored Program Repair** (arXiv:2601.08545)
   This paper introduces LSGen, a framework aimed at enhancing program repair while providing bug descriptions for program learners. The work includes LPR-Bench, which contains students' buggy programs paired with their correct versions, detailed bug descriptions, and a large-scale retrieval database. The approach is evaluated using GPT-4o with three retrieval models: Qwen3-Embedding-0.6B, inf-retriever-v1, and UniXcoder.

2. **GitBugs Dataset** (arXiv:2504.09651)
   GitBugs is a comprehensive dataset comprising over 150,000 bug reports from nine actively maintained open-source projects, including Firefox, Cassandra, and VS Code. GitBugs supports various tasks including duplicate detection, retrieval augmented generation, resolution prediction, automated triaging, and temporal analysis.

3. **Retrieval-Augmented Code Generation Survey** (arXiv:2510.04905)
   This survey covers retrieval-augmented approaches to code generation, including bug repair. InferFix trains a retriever using contrastive learning to identify semantically similar bugs and corresponding fixes from historical data.

4. **Bug Tracking in the Generative AI Era** (arXiv:2510.08005)
   This paper examines modern approaches to bug classification and management. Approaches that exploit semantic and contextual information from bug descriptions have shown promise in improving classification and filtering accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5be04f83-3e38-4bc2-9bca-b72cab4c186f",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "23f2908b-3993-42f2-98d3-9c9981264963",
  "sourceToolAssistantUUID": "5be04f83-3e38-4bc2-9bca-b72cab4c186f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T06:27:26.794Z_

<details><summary>↩ Tool result · `toolu_01QzsZFDWkwNNYSe29aSUdvv`</summary>

```text
Web search results for query: "categorical retrieval program repair arxiv 2026"

Links: [{"title":"[2601.08545] Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/abs/2601.08545"},{"title":"[2604.10481] PatchRecall: Patch-Driven Retrieval for Automated Program Repair","url":"https://arxiv.org/abs/2604.10481"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/html/2601.08545.pdf"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Repair Ingredients Are All You Need: Improving Large Language Model-Based Program Repair via Repair Ingredients Search","url":"https://arxiv.org/html/2506.23100"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"Information Retrieval Apr 2026","url":"https://arxiv.org/list/cs.IR/current"},{"title":"PatchRecall: Patch-Driven Retrieval for Automated Program Repair","url":"https://arxiv.org/html/2604.10481v1"},{"title":"𝑇³: Multi-level Tree-based Automatic Program Repair with Large Language Models","url":"https://arxiv.org/html/2506.21211"}]

Based on the search results, I found several relevant papers on program repair and retrieval from arXiv in 2026. Here are the key findings:

## Recent Program Repair Papers (2026)

**1. Learner-Tailored Program Repair (arXiv:2601.08545)**

This paper introduces a novel task called LRP (Learner-Tailored Program Repair) and proposes LSGEN (Learner-Tailored Solution Generator) to enhance program repair while offering bug descriptions for buggy code. The framework utilizes a repair solution retrieval framework to construct a solution retrieval database and employs an edit-driven code retrieval approach to retrieve valuable solutions, guiding LLMs in identifying and fixing bugs.

**2. PatchRecall (arXiv:2604.10481)**

PatchRecall is a hybrid retrieval approach that balances recall with conciseness by combining codebase retrieval (matching issue descriptions against the codebase) with history-based retrieval (leveraging similar past issues to identify edited files).

**3. ARISE (arXiv:2605.03117)**

ARISE builds on the agentic paradigm and targets the localization bottleneck by providing the agent with structured graph-based tools rather than relying on lexical retrieval or free-form code navigation.

**4. Survey on LLM-Based Automated Program Repair**

A comprehensive survey covers four paradigms: fine-tuning, prompting, procedural pipelines, and agentic frameworks, incorporating cross-cutting Retrieval Augmented Generation (RAG) and Analysis Augmented Generation (AAG) enhancements.

These papers represent the latest developments in combining retrieval techniques with large language models for automated program repair.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8b94829-60db-4a6d-ac24-402ec82a9742",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "42d94316-e35e-4560-98b9-e3f87f0578b1",
  "sourceToolAssistantUUID": "b8b94829-60db-4a6d-ac24-402ec82a9742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T06:27:28.059Z_

Let me do some additional targeted searches to look for papers specifically on failure-type or bug-type classification approaches in program repair.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42d94316-e35e-4560-98b9-e3f87f0578b1",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQwu1GGLznN6pXJNRCp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a9563a78-df6c-441f-b43e-7d3c1f285db4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DAAbjQxggSLAvmtNWC1DtH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3302,
      "cache_creation_input_tokens": 4876,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4876,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T06:27:28.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q58EUKn3uWQDtXUvi57fwu`</summary>

```json
{
  "query": "FTCR failure type code repair arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9563a78-df6c-441f-b43e-7d3c1f285db4",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQwu1GGLznN6pXJNRCp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "70b61c0c-e60a-47ba-87c0-d783927654ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DAAbjQxggSLAvmtNWC1DtH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3302,
      "cache_creation_input_tokens": 4876,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4876,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T06:27:28.931Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JxhtioCFQ2eyXTkTSMLmk3`</summary>

```json
{
  "query": "\"error type\" \"program repair\" retrieval arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70b61c0c-e60a-47ba-87c0-d783927654ce",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQwu1GGLznN6pXJNRCp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "592d951b-bc63-41ab-9478-205cca1c32b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DAAbjQxggSLAvmtNWC1DtH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3302,
      "cache_creation_input_tokens": 4876,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4876,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T06:27:28.939Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015tKBs8ALa7Nzo9WJiMhHet`</summary>

```json
{
  "query": "bug type classification automated repair arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "592d951b-bc63-41ab-9478-205cca1c32b6",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQwu1GGLznN6pXJNRCp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dc1aaf9a-cc59-4378-ade2-28d13bb612c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DAAbjQxggSLAvmtNWC1DtH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3302,
      "cache_creation_input_tokens": 4876,
      "cache_read_input_tokens": 16835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4876,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T06:27:29.342Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BP9R3EeV6YApeSQ28uk2fv`</summary>

```json
{
  "query": "\"semantic repair\" \"type-aware\" retrieval arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc1aaf9a-cc59-4378-ade2-28d13bb612c0",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQwu1GGLznN6pXJNRCp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "faef3eee-c5a5-4337-b917-30c961e5100c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DAAbjQxggSLAvmtNWC1DtH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3302,
      "cache_creation_input_tokens": 4876,
      "cache_read_input_tokens": 16835,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4876
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3302,
          "output_tokens": 231,
          "cache_read_input_tokens": 16835,
          "cache_creation_input_tokens": 4876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4876,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T06:27:34.499Z_

<details><summary>↩ Tool result · `toolu_01Q58EUKn3uWQDtXUvi57fwu`</summary>

```text
Web search results for query: "FTCR failure type code repair arxiv"

Links: [{"title":"Repairing Multiple Failures with Coordinated and Adaptive Regenerating Codes","url":"https://arxiv.org/pdf/1102.0204"},{"title":"CI-Repair-Bench: A Repository-Aware Benchmark for Automated Patch Validation via CI Workflows","url":"https://arxiv.org/html/2604.27148"},{"title":"[1408.5780] Fractional repetition codes with flexible repair from combinatorial designs","url":"https://arxiv.org/abs/1408.5780"},{"title":"Repair-R1: Better Test Before Repair","url":"https://arxiv.org/html/2507.22853v1"},{"title":"[2604.17184] SynthFix: Adaptive Neuro-Symbolic Code Vulnerability Repair","url":"https://arxiv.org/abs/2604.17184"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"Towards Practical and Useful Automated Program Repair for Debugging","url":"https://arxiv.org/html/2407.08958"},{"title":"I. Introduction","url":"https://arxiv.org/html/2510.15906v1"},{"title":"From Benchmark Data To Applicable Program Repair: An Experience Report","url":"https://arxiv.org/html/2508.16071v1"},{"title":"Agentic Reinforcement Learning for Real-World Code Repair","url":"https://arxiv.org/html/2510.22075"}]

The search results returned various papers related to code repair and regenerating codes, but they don't appear to contain direct information about "FTCR failure type code repair" as a specific named methodology. 

The results include:

1. Papers on regenerating codes for repairing lost encoded blocks in distributed storage systems

2. CI-Repair-Bench, a benchmark for CI-verified program repair that contains 567 CI failure instances from 103 repositories with failures categorized into 12 CI error types

3. Various other papers on automated program repair techniques using LLMs and other approaches

However, none of these directly address "FTCR failure type code repair" specifically. The acronym "FTCR" doesn't appear to be explicitly defined in these search results. If you're looking for a specific paper or methodology with this acronym, you might want to:

- Check if FTCR is a more recent paper that might not be well-indexed yet
- Verify the exact spelling or acronym
- Try searching for the specific authors if you know them
- Check the arXiv directly with a modified search query

Would you like me to search with different terms to help locate the specific research you're looking for?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70b61c0c-e60a-47ba-87c0-d783927654ce",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "9678a687-4f1b-49d0-bdba-806f41b3f50d",
  "sourceToolAssistantUUID": "70b61c0c-e60a-47ba-87c0-d783927654ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T06:27:35.855Z_

<details><summary>↩ Tool result · `toolu_01BP9R3EeV6YApeSQ28uk2fv`</summary>

```text
Web search results for query: ""semantic repair" "type-aware" retrieval arxiv 2026"

Links: [{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"citecheck: An MCP Server for Automated Bibliographic Verification and Repair in Scholarly Manuscripts","url":"https://arxiv.org/html/2603.17339"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"Retrieval-Augmented Generation for AI-Generated Content: A Survey | Data Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41019-025-00335-5"},{"title":"[2603.03180] Type-Aware Retrieval-Augmented Generation with Dependency Closure for Solver-Executable Industrial Optimization Modeling","url":"https://arxiv.org/abs/2603.03180"},{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"Memory-Efficient Large Language Models for Program Repair with Semantic-Guided Patch Generation","url":"https://arxiv.org/html/2410.16655v2"},{"title":"Repairing DNN Numerical Defects with Semantic-Driven Knowledge Graph Retrieval","url":"https://www.mdpi.com/2076-3417/16/4/2124"}]

Based on the search results, I found relevant research on type-aware retrieval approaches from arxiv in 2026:

A type-aware retrieval-augmented generation (RAG) method has been proposed that enforces modeling entity types and minimal dependency closure to ensure executability. Unlike existing RAG approaches that index unstructured text, this method constructs a domain-specific typed knowledge base by parsing heterogeneous sources, such as academic papers and solver code, into typed units and encoding their mathematical dependencies in a knowledge graph. Given a natural-language instruction, it performs hybrid retrieval and computes a minimal dependency-closed context via dependency propagation over the graph.

The approach targets automated industrial optimization modeling, which requires reliable translation of natural-language requirements into solver-executable code, as large language models often generate non-compilable models due to missing declarations, type inconsistencies, and incomplete dependency contexts.

Additionally, there are several other semantic repair and retrieval approaches from 2025-2026:

ReCode is a fine-grained retrieval-augmented generation framework that constructs modular representations for both source code and its accompanying textual descriptions to capture domain-specific semantics effectively.

NCKG is a Numerical–Conceptual Knowledge Graph-based method for retrieval-augmented repair of DNN numerical defects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faef3eee-c5a5-4337-b917-30c961e5100c",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "ec05153c-c805-4088-aa40-f7e8d07a2e8a",
  "sourceToolAssistantUUID": "faef3eee-c5a5-4337-b917-30c961e5100c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T06:27:36.293Z_

<details><summary>↩ Tool result · `toolu_01JxhtioCFQ2eyXTkTSMLmk3`</summary>

```text
Web search results for query: ""error type" "program repair" retrieval arxiv 2025 2026"

Links: [{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Learner-Tailored Program Repair: A Solution Generator with","url":"https://arxiv.org/pdf/2601.08545"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval","url":"https://arxiv.org/html/2506.18394"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"[2506.23749] A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/abs/2506.23749"},{"title":"𝑇³: Multi-level Tree-based Automatic Program Repair with Large Language Models","url":"https://arxiv.org/html/2506.21211"},{"title":"Beyond Final Code: A Process-Oriented Error Analysis of Software Development Agents in Real-World GitHub Scenarios","url":"https://arxiv.org/html/2503.12374v3"},{"title":"[2503.21710] Enhancing repository-level software repair via repository-aware knowledge graphs","url":"https://arxiv.org/abs/2503.21710"}]

Based on the search results, I found several recent arxiv papers (2025-2026) related to error types, program repair, and retrieval. Here are the key findings:

## Major Survey Paper

A comprehensive survey from June 2025 maps LLM-based automated program repair across four paradigms (fine-tuning, prompting, procedural pipelines, and agentic frameworks), and categorizes 63 LLM-based APR systems published from January 2022 to June 2025. Retrieval-Augmented Generation (RAG) refers to augmenting the LLM's input with external knowledge such as relevant code snippets, documentation, or historical fixes.

## Error Type and Analysis Augmentation

Analysis-Augmented Generation (AAG) involves incorporating program static or dynamic analysis results (such as error traces or data-flow facts) into the prompt or constraining the model's output.

## Specific Error Type Studies

Recent work has focused on specific error types. For example, there are existing repair techniques for TypeError, dependency-related errors, and SyntaxError, and integrating these techniques into agentic workflows is a promising direction.

## Repository-Level Memory Error Repair

A novel approach called LTFix harnesses LLMs for automated memory error repair for complex repository-level errors, and uses a finite typestate automaton to guide the tracking of error-propagation paths and context trace.

These papers demonstrate active research in combining error type analysis with retrieval-based approaches for automated program repair in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "592d951b-bc63-41ab-9478-205cca1c32b6",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "5444710e-5849-4566-8a86-98aa4254e0be",
  "sourceToolAssistantUUID": "592d951b-bc63-41ab-9478-205cca1c32b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T06:27:36.439Z_

<details><summary>↩ Tool result · `toolu_015tKBs8ALa7Nzo9WJiMhHet`</summary>

```text
Web search results for query: "bug type classification automated repair arxiv"

Links: [{"title":"[2601.10987] Reasoning Distillation for Lightweight Automated Program Repair","url":"https://arxiv.org/abs/2601.10987"},{"title":"Reasoning Distillation for Lightweight Automated Program Repair","url":"https://arxiv.org/html/2601.10987"},{"title":"CodeCureAgent: Automatic Classification and Repair of Static Analysis Warnings","url":"https://arxiv.org/pdf/2509.11787"},{"title":"[2211.03911] Towards Extending the Range of Bugs That Automated Program Repair Can Handle","url":"https://arxiv.org/abs/2211.03911"},{"title":"A Deep Dive into Large Language Models for Automated Bug Localization and Repair","url":"https://arxiv.org/html/2404.11595v3"},{"title":"An Empirical Study on the Classification of Bug Reports with Machine Learning","url":"https://arxiv.org/html/2503.00660v1"},{"title":"[2404.11595] A Deep Dive into Large Language Models for Automated Bug Localization and Repair","url":"https://arxiv.org/abs/2404.11595"},{"title":"Challenging Bug Prediction and Repair Models with Synthetic Bugs","url":"https://arxiv.org/html/2310.02407"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Self-Supervised Bug Detection and Repair","url":"https://arxiv.org/pdf/2105.12787"}]

I found several relevant papers on arXiv related to bug type classification and automated repair. Here are the key findings:

## Recent Papers

A recent paper studies whether lightweight symbolic reasoning supervision can improve fix type classification in compact automated program repair models, proposing a reasoning distillation approach in which a large teacher model provides structured symbolic reasoning tags alongside fix-type labels.

CodeCureAgent is an approach that harnesses LLM-based agents to automatically analyze, classify, and repair static analysis warnings.

Another study devises a novel bug classification system that enables methodical analysis of automated program repair approaches' bug detection power and bug repair capabilities. This addresses bugs that do not lead to observable behavior, such as liveness/termination bugs, non-functional bugs, and information flow bugs.

## Classification and Detection Work

Large language models have shown impressive effectiveness in automated program repair, with one approach uniquely employing LLMs to predict bug location at the token level and subsequently utilizing them for bug fixing.

An empirical study created a dataset with more than 660,000 issue report samples collected from 52 software systems, written in multiple programming languages (Java, Python, C/C++, JavaScript), managed in three distinct issue tracking systems (Jira, GitHub, and BugZilla).

These papers represent the current state of research in automated bug classification and repair on arXiv, combining machine learning approaches, symbolic reasoning, and LLM-based techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc1aaf9a-cc59-4378-ade2-28d13bb612c0",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "2dd16160-60c6-4311-9382-c614d5399ecb",
  "sourceToolAssistantUUID": "dc1aaf9a-cc59-4378-ade2-28d13bb612c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T06:27:38.012Z_

Excellent. Let me do a few more targeted searches to find papers on specific partitioning or stratification strategies in program repair.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dd16160-60c6-4311-9382-c614d5399ecb",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQxcKCPp4pt8sryTkz6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3e1661b9-2776-4515-bf7f-1ac3616e95d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CdrhS3Yg5fGw8CeRJeymyR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 6056,
      "cache_read_input_tokens": 21711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6056,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-10T06:27:38.469Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PFyUuJ91EQP5FfiyYpRPib`</summary>

```json
{
  "query": "\"partition\" OR \"stratified\" retrieval program repair arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e1661b9-2776-4515-bf7f-1ac3616e95d0",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQxcKCPp4pt8sryTkz6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "652e550a-8632-4b15-97a3-26a0d144bbef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CdrhS3Yg5fGw8CeRJeymyR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 6056,
      "cache_read_input_tokens": 21711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6056,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-10T06:27:38.673Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VrV657rAdwHtxcHfz1kUe7`</summary>

```json
{
  "query": "semantic type program repair index arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "652e550a-8632-4b15-97a3-26a0d144bbef",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQxcKCPp4pt8sryTkz6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1323cf8c-eb65-4862-adc8-93d2144f6a89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CdrhS3Yg5fGw8CeRJeymyR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 6056,
      "cache_read_input_tokens": 21711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6056,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T06:27:38.807Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018mxYWNoAUyjSzvjgS8ruwP`</summary>

```json
{
  "query": "ReAPR arxiv retrieval augmented repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1323cf8c-eb65-4862-adc8-93d2144f6a89",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQxcKCPp4pt8sryTkz6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "29236c7e-d254-47d9-85c8-b79c1de4433a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CdrhS3Yg5fGw8CeRJeymyR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 828,
      "cache_creation_input_tokens": 6056,
      "cache_read_input_tokens": 21711,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6056
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 828,
          "output_tokens": 187,
          "cache_read_input_tokens": 21711,
          "cache_creation_input_tokens": 6056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6056,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T06:27:45.139Z_

<details><summary>↩ Tool result · `toolu_01VrV657rAdwHtxcHfz1kUe7`</summary>

```text
Web search results for query: "semantic type program repair index arxiv 2025 2026"

Links: [{"title":"Memory-Efficient Large Language Models for Program Repair with Semantic-Guided Patch Generation","url":"https://arxiv.org/html/2410.16655"},{"title":"[2410.16655] Memory-Efficient Large Language Models for Program Repair with Semantic-Guided Patch Generation","url":"https://arxiv.org/abs/2410.16655"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Semantic-guided Search for Efficient Program Repair with Large Language Models","url":"https://arxiv.org/pdf/2410.16655"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"[2506.23749v1] A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/abs/2506.23749v1"},{"title":"Accelerating Automatic Program Repair with Dual Retrieval-Augmented","url":"https://arxiv.org/pdf/2507.10103"},{"title":"A Systematic Literature Review on Large Language Models","url":"https://arxiv.org/pdf/2405.01466"},{"title":"A Systematic Literature Review on Large Language Models for Automated Program Repair","url":"https://arxiv.org/html/2405.01466v4"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=3175&show=25"}]

Based on the web search results, I found several relevant papers on arxiv from 2025-2026 related to semantic-guided program repair:

## Key Findings:

1. **FLAMES: Memory-Efficient Program Repair with Semantic-Guided Patch Generation**
   This paper introduces FLAMES, a novel LLM-based APR technique that employs semantic-guided patch generation to enhance repair effectiveness and memory efficiency. FLAMES uses semantic feedback from test validation, such as the number of passing and failing test cases, to select the most promising token to explore further. FLAMES correctly fixes 133 bugs on Defects4J, fixing 10 bugs more than the best baseline.

2. **Survey on LLM-based Automated Program Repair**
   Large language models (LLMs) are reshaping automated program repair (APR), with 63 LLM-based APR systems published from January 2022 to June 2025 categorized into four paradigms, showing how retrieval- or analysis-augmented contexts strengthen them.

3. **Retrieval-Augmented Code Generation Survey**
   Generated code must adhere to project-wide naming conventions, correctly reference existing APIs, and respect type hierarchies to maintain overall semantic coherence.

These papers represent the latest research on semantic-guided approaches in program repair, emphasizing the integration of semantic feedback and type-aware strategies in automated repair techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1323cf8c-eb65-4862-adc8-93d2144f6a89",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "2b9f5c86-a750-4ecd-a53a-90e13e1daa9c",
  "sourceToolAssistantUUID": "1323cf8c-eb65-4862-adc8-93d2144f6a89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T06:27:46.612Z_

<details><summary>↩ Tool result · `toolu_01PFyUuJ91EQP5FfiyYpRPib`</summary>

```text
Web search results for query: ""partition" OR "stratified" retrieval program repair arxiv 2026"

Links: [{"title":"[2601.08545] Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/abs/2601.08545"},{"title":"[2604.10481] PatchRecall: Patch-Driven Retrieval for Automated Program Repair","url":"https://arxiv.org/abs/2604.10481"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"AutoCodeRover: Autonomous Program Improvement Yuntong Zhang","url":"https://arxiv.org/pdf/2404.05427"},{"title":"Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/html/2601.08545.pdf"},{"title":"PatchRecall: Patch-Driven Retrieval for Automated Program Repair","url":"https://arxiv.org/html/2604.10481"},{"title":"[2601.00509] Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback","url":"https://arxiv.org/abs/2601.00509"},{"title":"Repair Ingredients Are All You Need: Improving Large Language Model-Based Program Repair via Repair Ingredients Search","url":"https://arxiv.org/html/2506.23100"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481v1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"}]

I found several relevant arxiv papers from 2026 related to retrieval and program repair. Here are the key results:

## Main Results:

1. **AutoCodeRover** (April 2024) - This work employs a stratified strategy for the LLM agent to retrieve code, leveraging the strong capability of stratified context retrieval in AutoCodeRover to fast pinpoint error locations and produce final patches.

2. **Learner-Tailored Program Repair** (January 2026) - This paper utilizes a repair solution retrieval framework to construct a solution retrieval database and then employs an edit-driven code retrieval approach to retrieve valuable solutions, guiding LLMs in identifying and fixing bugs in buggy code.

3. **PatchRecall: Patch-Driven Retrieval for Automated Program Repair** (April 2026) - This work proposes a hybrid retrieval approach that balances recall with conciseness, combining codebase retrieval (where the current issue description is matched against the codebase to surface potentially relevant files) and history-based retrieval (where similar past issues are leveraged to identify edited files as candidate targets).

4. **ARISE: A Repository-level Graph Representation** (May 2026) - This work builds on the agentic paradigm and targets the localization bottleneck by providing the agent with structured graph-based tools rather than relying on lexical retrieval or free-form code navigation.

5. **On the Role of Fault Localization Context for LLM-Based Program Repair** (April 2026) - This empirical study evaluates 61 configurations that vary file-, element-, and line-level context, showing that more context does not consistently improve repair performance, with file-level localization yielding a 15–17× improvement over a no-file baseline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "652e550a-8632-4b15-97a3-26a0d144bbef",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "9d4dc9b2-a3fb-4c57-b5a7-6b225faccb83",
  "sourceToolAssistantUUID": "652e550a-8632-4b15-97a3-26a0d144bbef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T06:27:50.235Z_

<details><summary>↩ Tool result · `toolu_018mxYWNoAUyjSzvjgS8ruwP`</summary>

```text
Web search results for query: "ReAPR arxiv retrieval augmented repair"

Links: [{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning and Patch Generation on Large Language Models","url":"https://arxiv.org/html/2507.10103"},{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"[2507.10103] Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning and Patch Generation on Large Language Models","url":"https://arxiv.org/abs/2507.10103"},{"title":"[2309.06057] RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 for Automatic Program Repair","url":"https://arxiv.org/abs/2309.06057"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330"},{"title":"Repairing Responsive Layout Failures Using Retrieval Augmented Generation","url":"https://arxiv.org/html/2511.00678"},{"title":"zxliu/ReAPR-Automatic-Program-Repair-via-Retrieval-Augmented-Large-Language-Models · Datasets at Hugging Face","url":"https://huggingface.co/datasets/zxliu/ReAPR-Automatic-Program-Repair-via-Retrieval-Augmented-Large-Language-Models"},{"title":"Accelerating Automatic Program Repair with Dual Retrieval-Augmented","url":"https://arxiv.org/pdf/2507.10103"},{"title":"GitHub - ZXLiu/ReAPR: Here is the open-source code repository for the paper \"ReAPR: Automatic Program Repair via Retrieval-Augmented Large Language Models.\" · GitHub","url":"https://github.com/ZXLiu/ReAPR"}]

Based on the search results, I found information about ReAPR, a research paper on automatic program repair:

## ReAPR Overview

ReAPR is a paper titled "Automatic Program Repair via Retrieval-Augmented Large Language Models".

## Key Concepts

Automatic Program Repair (APR) aims to automatically fix software defects, significantly reducing the efforts of manual debugging. Recent studies have demonstrated impressive results in utilizing Large Language Models (LLMs) for software bug fixing.

ReAPR builds on the concept of Retrieval-Augmented Generation (RAG). RAG generates accurate outputs by firstly retrieving relevant information (usually from an external specialized knowledge base) and then feeding this retrieved information into LLMs as contexts.

## Implementation Details

The ReAPR project includes open-source code and datasets. The project provides an open-source code repository for the paper "ReAPR: Automatic Program Repair via Retrieval-Augmented Large Language Models." The implementation supports different retrieval methods including BM25 and DPR (Dense Passage Retrieval) algorithms, and can be applied to benchmarks like Defects4J and GitBug-Java.

The related work also includes RAP-Gen, a Retrieval-Augmented Patch Generation framework that explicitly leverages relevant fix patterns retrieved from a codebase of previous bug-fix pairs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29236c7e-d254-47d9-85c8-b79c1de4433a",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "168efdac-a359-4a22-9897-8ba714b5947d",
  "sourceToolAssistantUUID": "29236c7e-d254-47d9-85c8-b79c1de4433a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-10T06:27:51.442Z_

Now let me search for papers on specific bug categorization schemes and repair approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "168efdac-a359-4a22-9897-8ba714b5947d",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQydFHFd2EMdtNWSbVn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "62d077f6-9106-4fe2-938c-dfee6c36013f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011oDJQzdhwUBNh95zrqPhqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3688,
      "cache_read_input_tokens": 27767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-10T06:27:51.995Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P5ri86LsuydRKyV2xeA5Pg`</summary>

```json
{
  "query": "InferFix contrastive bug repair arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62d077f6-9106-4fe2-938c-dfee6c36013f",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQydFHFd2EMdtNWSbVn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6ee940c0-78fe-4768-aaeb-1b7696d49f13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011oDJQzdhwUBNh95zrqPhqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3688,
      "cache_read_input_tokens": 27767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-10T06:27:52.190Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AY74E5qsLC9QS9TEJrjHTP`</summary>

```json
{
  "query": "\"bug taxonomy\" program repair learning arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ee940c0-78fe-4768-aaeb-1b7696d49f13",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQydFHFd2EMdtNWSbVn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5614ca1e-d82c-43f2-bb86-bf31cc198bb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011oDJQzdhwUBNh95zrqPhqo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3688,
      "cache_read_input_tokens": 27767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3688,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-10T06:27:52.338Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LjayLWUnrj11QhBkmLZA45`</summary>

```json
{
  "query": "T3 tree-based program repair arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5614ca1e-d82c-43f2-bb86-bf31cc198bb6",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQydFHFd2EMdtNWSbVn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d4b06258-e79f-41e3-9313-9e7d22f0d3b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011oDJQzdhwUBNh95zrqPhqo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3688,
      "cache_read_input_tokens": 27767,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3688
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 175,
          "cache_read_input_tokens": 27767,
          "cache_creation_input_tokens": 3688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3688,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T06:27:57.177Z_

<details><summary>↩ Tool result · `toolu_01LjayLWUnrj11QhBkmLZA45`</summary>

```text
Web search results for query: "T3 tree-based program repair arxiv 2026"

Links: [{"title":"𝑇³: Multi-level Tree-based Automatic Program Repair with Large Language Models","url":"https://arxiv.org/html/2506.21211v1"},{"title":"[2506.21211v1] $T^3$: Multi-level Tree-based Automatic Program Repair with Large Language Models","url":"https://arxiv.org/abs/2506.21211v1"},{"title":"Learning from Imperfect Demonstrations via Temporal Behavior Tree-Guided Trajectory Repair","url":"https://arxiv.org/html/2604.04225"},{"title":"Multi-level Tree-based Automatic Program Repair with ...","url":"https://www.arxiv.org/pdf/2506.21211"},{"title":"TSAPR: A Tree Search Framework For Automated Program Repair","url":"https://arxiv.org/html/2507.01827"},{"title":"[2506.21211] $T^3$: Multi-level Tree-based Automatic Program Repair with Large Language Models","url":"https://arxiv.org/abs/2506.21211"},{"title":"T3: Multi-level Tree-based Automatic Program Repair with Large Language Models | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11228000/"},{"title":"[2507.01827] TSAPR: A Tree Search Framework For Automated Program Repair","url":"https://arxiv.org/abs/2507.01827"},{"title":"Trace Repair for Temporal Behavior Trees","url":"https://arxiv.org/html/2509.08610"},{"title":"[2502.15344] Computation Tree Logic Guided Program Repair","url":"https://arxiv.org/abs/2502.15344"}]

Based on the search results, I found the paper you're looking for:

T³ is an innovative framework that integrates the powerful reasoning capabilities of Large Language Models (LLMs) with tree search, effectively improving the precision of generating candidate repair solutions. 

The T³ framework is designed to leverage LLMs for handling Automatic Program Repair (APR) tasks and consists of four key stages: Sample Retrieval, Cause Analysis, Repair Plan Generation and Patch Generation.

The paper (arxiv 2506.21211) was published in June 2025. The study systematically evaluates the performance of several common Chain-of-Thought (CoT) techniques in APR tasks, and in the cause analysis and repair plan generation stages, the Forest of Thinking approach enhances reasoning by constructing multiple parallel reasoning trees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4b06258-e79f-41e3-9313-9e7d22f0d3b8",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "9ef578c9-08a2-4d1b-bb1f-250677a78c0f",
  "sourceToolAssistantUUID": "d4b06258-e79f-41e3-9313-9e7d22f0d3b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T06:28:00.727Z_

<details><summary>↩ Tool result · `toolu_01AY74E5qsLC9QS9TEJrjHTP`</summary>

```text
Web search results for query: ""bug taxonomy" program repair learning arxiv 2025 2026"

Links: [{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"[2506.23749] A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/abs/2506.23749"},{"title":"A Comprehensive Study of Bugs in Modern Distributed Deep Learning Systems","url":"https://arxiv.org/pdf/2512.20345"},{"title":"[2506.23749v1] A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/abs/2506.23749v1"},{"title":"A Survey of Bugs in AI-Generated Code","url":"https://arxiv.org/html/2512.05239v1"},{"title":"[2505.07372v1] Synthetic Code Surgery: Repairing Bugs and Vulnerabilities with LLMs and Synthetic Data","url":"https://arxiv.org/abs/2505.07372v1"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"},{"title":"Agentic Software Issue Resolution with Large Language Models: A Survey","url":"https://arxiv.org/html/2512.22256"},{"title":"Adversarial Bug Reports as a Security Risk in Language Model-Based Automated Program Repair","url":"https://arxiv.org/html/2509.05372v2"},{"title":"Challenging Bug Prediction and Repair Models with Synthetic Bugs","url":"https://arxiv.org/html/2310.02407"}]

Based on the search results, I found several relevant papers on bug taxonomy and program repair learning from recent 2025-2026 arXiv submissions:

## Key Findings:

**1. LLM-based Automated Program Repair Survey**

A comprehensive survey presents the first unified taxonomy covering four repair paradigms and two augmentation layers for LLM-based APR, reviewing 63 recent state-of-the-art APR systems published between January 2022 and June 2025. The taxonomy categorizes the 63 LLM-based APR systems into four paradigms and shows how retrieval- or analysis-augmented contexts strengthen any of them.

The taxonomy clarifies key trade-offs: fine-tuning delivers strong task alignment at high training cost; prompting enables rapid deployment but is limited by prompt design and context windows; procedural pipelines offer reproducible control with moderate overhead; agentic frameworks tackle multi-hunk or cross-file bugs at the price of increased latency and complexity.

**2. Bug Taxonomy in Deep Learning Systems**

One study constructs a taxonomy of 34 bug symptoms, 28 root causes, and 6 fix patterns from 849 real-world issues in distributed deep learning frameworks.

**3. Bug Taxonomy in AI-Generated Code**

Another survey classifies bugs found in AI-generated code into eight major categories: Functionality, Reliability, Syntax, Code Style, Hallucination, System, Test, and Unspecified bugs.

**4. Synthetic Data for Program Repair**

A recent paper on synthetic code generation employed multiple state-of-the-art LLMs to generate approximately 30,000 paired examples of buggy and fixed code across 12 programming languages and 13 bug categories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5614ca1e-d82c-43f2-bb86-bf31cc198bb6",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "9614e452-5a85-4ac9-bafe-9b0e1008b3aa",
  "sourceToolAssistantUUID": "5614ca1e-d82c-43f2-bb86-bf31cc198bb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T06:28:03.907Z_

<details><summary>↩ Tool result · `toolu_01P5ri86LsuydRKyV2xeA5Pg`</summary>

```text
Web search results for query: "InferFix contrastive bug repair arxiv"

Links: [{"title":"[2303.07263] InferFix: End-to-End Program Repair with LLMs","url":"https://arxiv.org/abs/2303.07263"},{"title":"InferFix: End-to-End Program Repair with LLMs over Retrieval-Augmented Prompts","url":"https://arxiv.org/pdf/2303.07263"},{"title":"InferFix: End-to-End Program Repair with LLMs | Request PDF","url":"https://www.researchgate.net/publication/369198916_InferFix_End-to-End_Program_Repair_with_LLMs"},{"title":"InferFix: End-to-End Program Repair with LLMs","url":"https://www.arxiv-vanity.com/papers/2303.07263/"},{"title":"InferFix: End-to-End Program Repair with LLMs | Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering","url":"https://dl.acm.org/doi/abs/10.1145/3611643.3613892"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"InferFix: End-to-End Program Repair with LLMs (ESEC/FSE 2023 - Industry Papers) - ESEC/FSE 2023","url":"https://2023.esec-fse.org/details/fse-2023-industry/33/InferFix-End-to-End-Program-Repair-with-LLMs"},{"title":"Bug Fixing with Broader Context: Enhancing LLM-Based Program Repair via Layered Knowledge Injection","url":"https://arxiv.org/html/2506.24015v1"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"}]

Based on the search results, I found relevant information about InferFix and its use of contrastive learning for bug repair:

## InferFix: Contrastive Bug Repair

InferFix is a transformer-based program repair framework paired with a state-of-the-art static analyzer to fix critical security and performance bugs.

The framework has two main components: a Retriever -- transformer encoder model pretrained via contrastive learning objective, which aims at searching for semantically equivalent bugs and corresponding fixes; and a Generator -- a large language model (Codex Cushman).

### Contrastive Learning Approach

The contrastive pretraining dataset consists of samples where each sample includes a query – an encoding of a buggy code snippet; a positive sample representing a semantically similar code snippet of the same bug type; and a set of negative samples which are irrelevant code snippets of different bug types. The training adopts in-batch negatives to calculate the contrastive loss by InfoNCE.

### Dataset and Results

The researchers curated InferredBugs, a novel, metadata-rich dataset of bugs extracted by executing the Infer static analyzer on the change histories of thousands of Java and C# repositories. InferFix outperforms strong LLM baselines, with a top-1 accuracy of 65.6% for generating fixes in C# and 76.8% in Java.

The paper was published in March 2023 and is available on arXiv as paper 2303.07263.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ee940c0-78fe-4768-aaeb-1b7696d49f13",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "47e3c2ff-1990-4ca1-8060-b58e00776355",
  "sourceToolAssistantUUID": "6ee940c0-78fe-4768-aaeb-1b7696d49f13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-10T06:28:05.332Z_

Excellent. Let me do one more search to find any papers specifically on "bug-aware" or "error-aware" retrieval strategies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47e3c2ff-1990-4ca1-8060-b58e00776355",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQzdf7mLvAtDGiGyovG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c362a649-cc22-4639-b99a-214d36942cb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CVbzbd1nFkCo5TjVUmF4ge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1588,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 31455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1184,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-10T06:28:05.546Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014q2shSnZj5P9iv3SpnsPgj`</summary>

```json
{
  "query": "\"bug-aware\" OR \"error-aware\" retrieval repair arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c362a649-cc22-4639-b99a-214d36942cb9",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQzdf7mLvAtDGiGyovG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3b3baed2-d236-4d4e-902e-32d1026830d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CVbzbd1nFkCo5TjVUmF4ge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1588,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 31455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1184,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-10T06:28:05.706Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DZS3A8oDG3Nt47uD91Gyhi`</summary>

```json
{
  "query": "context-aware program repair retrieval arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b3baed2-d236-4d4e-902e-32d1026830d8",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatQzdf7mLvAtDGiGyovG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5f14b8a6-3c40-4d10-9a90-5cf3cf9b10bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CVbzbd1nFkCo5TjVUmF4ge",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1588,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 31455,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1184
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1588,
          "output_tokens": 147,
          "cache_read_input_tokens": 31455,
          "cache_creation_input_tokens": 1184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1184,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T06:28:08.600Z_

<details><summary>↩ Tool result · `toolu_014q2shSnZj5P9iv3SpnsPgj`</summary>

```text
Web search results for query: ""bug-aware" OR "error-aware" retrieval repair arxiv 2026"

No links found.

The search didn't return any results for that specific query combination. The query may be looking for very recent or highly specialized research papers that aren't yet widely indexed, or the exact phrase combination might not appear together in available sources.

Would you like me to try alternative search approaches, such as:
- Searching for just "error-aware retrieval" or "bug-aware retrieval"
- Searching for "retrieval repair" on arXiv
- Using a different combination of these terms

Let me know how you'd like to proceed!


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b3baed2-d236-4d4e-902e-32d1026830d8",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "8635f228-7f11-43e9-91a9-c7edb983390b",
  "sourceToolAssistantUUID": "3b3baed2-d236-4d4e-902e-32d1026830d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-10T06:28:13.278Z_

<details><summary>↩ Tool result · `toolu_01DZS3A8oDG3Nt47uD91Gyhi`</summary>

```text
Web search results for query: "context-aware program repair retrieval arxiv 2026"

Links: [{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/html/2603.01048"},{"title":"Repair Ingredients Are All You Need: Improving Large Language Model-Based Program Repair via Repair Ingredients Search","url":"https://arxiv.org/html/2506.23100"},{"title":"[2604.10481] PatchRecall: Patch-Driven Retrieval for Automated Program Repair","url":"https://arxiv.org/abs/2604.10481"},{"title":"Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval","url":"https://arxiv.org/html/2506.18394"},{"title":"[2601.08545] Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/abs/2601.08545"},{"title":"[2603.01048] RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair","url":"https://arxiv.org/abs/2603.01048"}]

I found several relevant research papers on context-aware program repair and retrieval from arxiv in 2026. Here are the key results:

## Recent Papers on Context-Aware Program Repair and Retrieval

**1. On the Role of Fault Localization Context for LLM-Based Program Repair**
This paper investigates Fault Localization (FL) as a key component of LLM-based Automated Program Repair (APR), examining how much localization is needed and whether additional context beyond the predicted buggy location is beneficial. The results show that more context does not consistently improve repair performance, with file-level localization yielding a 15–17× improvement over a no-file baseline.

**2. RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair**
RepoRepair is a documentation-enhanced approach for repository-level fault localization and program repair that leverages LLMs to generate hierarchical code documentation (from functions to files) for code repositories, creating structured semantic abstractions.

**3. Repair Ingredients Are All You Need**
ReinFix enhances LLM-based APR by conducting dependency analysis to identify and retrieve relevant contextual code elements (e.g., definitions and usages of key variables or methods) within the project, enabling deeper understanding of project-specific dependencies.

**4. PatchRecall: Patch-Driven Retrieval for Automated Program Repair**
PatchRecall is a hybrid retrieval approach that combines codebase retrieval and history-based retrieval, where the current issue description is matched against the codebase and similar past issues are leveraged to identify edited files.

**5. ARISE: Repository-level Graph Representation for Agentic Fault Localization and Program Repair**
ARISE addresses the fault localization bottleneck by providing data-flow slicing as a queryable tool, enabling tracing of variable definitions and uses within a function.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f14b8a6-3c40-4d10-9a90-5cf3cf9b10bf",
  "isSidechain": true,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "agentId": "abf2c5b9b247b50e7",
  "type": "user",
  "uuid": "4dd73ed5-ff14-4096-86c8-b920377a82f2",
  "sourceToolAssistantUUID": "5f14b8a6-3c40-4d10-9a90-5cf3cf9b10bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-10T06:28:36.373Z_

Perfect. Now I have comprehensive information. Let me compile the findings for the user.

## Summary of Recent Papers on Type-Conditioned and Category-Conditioned Program Repair (2025-2026)

Based on my systematic search, I found **no papers explicitly named using the "FTCR" acronym or directly using the term "type-conditioned program repair"** as the primary focus. However, I identified several highly relevant concurrent works that address related ideas of **partitioning, classifying, or conditioning retrieval by bug/error characteristics**. Here are the most significant findings:

### High-Similarity Papers (Directly Related to Bug-Type Partitioning)

**1. InferFix: End-to-End Program Repair with LLMs**
- ArXiv: 2303.07263 (March 2023)
- **Venue/Date:** Published at ESEC/FSE 2023 (Industry Papers)
- **Similarity to FTCR:** Very High - Uses **contrastive learning to group bugs by semantic similarity**, training on samples where positive examples are "semantically similar bugs of the same bug type" and negatives are "irrelevant code snippets of different bug types." Explicitly partitions training data by bug type in contrastive pre-training. Uses a retriever trained via contrastive learning to search for semantically equivalent bugs and their corresponding fixes.
- **Key Difference:** Focuses on contrastive pre-training rather than index partitioning, but achieves similar goal of type-aware bug matching.

**2. Learner-Tailored Program Repair (LSGen)**
- ArXiv: 2601.08545 (January 2026)
- **Venue/Date:** Published January 2026
- **Similarity to FTCR:** Very High - Constructs a **solution retrieval database** and employs **iterative, edit-driven code retrieval** that adapts based on generated incorrect code. While not explicitly partitioning by bug type, it uses an iterative retrieval enhancement method that effectively conditions retrieval on the current repair attempt, achieving similar semantic conditioning effects.

**3. ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation**
- ArXiv: 2509.02330 (September 2025)
- **Venue/Date:** Published September 2025
- **Similarity to FTCR:** High - First determines **the algorithm of the wrong code to narrow the subset** of a knowledge base, then retrieves exemplars using dual-view fused features. This is a form of **algorithm/pattern-based partitioning** before retrieval, similar in spirit to type-based partitioning.

**4. PatchRecall: Patch-Driven Retrieval for Automated Program Repair**
- ArXiv: 2604.10481 (April 2026)
- **Venue/Date:** Published April 2026
- **Similarity to FTCR:** Moderate-High - Employs **hybrid retrieval combining codebase retrieval and history-based retrieval**, effectively creating **multiple retrieval strategies** based on whether searching current issue descriptions or historical patterns. Not explicitly by bug type, but uses stratified retrieval conditioned on issue metadata.

### Related Context-Aware Retrieval Papers

**5. On the Role of Fault Localization Context for LLM-Based Program Repair**
- ArXiv: 2604.05481 (April 2026)
- **Venue/Date:** Published April 2026
- **Similarity to FTCR:** Moderate - Empirically evaluates how **context granularity affects repair**, showing file-, element-, and line-level localization have different impacts. Explores how to best condition context retrieval on fault characteristics.

**6. ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair**
- ArXiv: 2605.03117 (May 2026)
- **Venue/Date:** Published May 2026
- **Similarity to FTCR:** Moderate - Uses **structured graph-based tools** and **data-flow slicing** to provide bug-specific context, rather than generic retrieval. Provides reasoning-guided approaches that generate "structured, bug-specific explanations before ranking candidate locations."

**7. RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair**
- ArXiv: 2603.01048 (March 2026)
- **Venue/Date:** Published March 2026
- **Similarity to FTCR:** Moderate - Creates **hierarchical code documentation as semantic abstractions** to condition retrieval, effectively partitioning the search space by structural/semantic categories rather than explicit bug types.

### Broader Retrieval-Augmented Repair Work

**8. ReAPR: Automatic Program Repair via Retrieval-Augmented Large Language Models**
- **Venue/Date:** Software Quality Journal, 2025
- **Similarity to FTCR:** Moderate - General RAG framework for repair; does not explicitly partition by bug type but provides the foundational RAG-for-repair methodology that FTCR would build upon.

**9. RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code**
- ArXiv: 2509.16701
- **Venue/Date:** Published September 2025
- **Similarity to FTCR:** Moderate - Systematically retrieves relevant code from the project repository to augment LLM repair. Focuses on code repository partitioning rather than bug-type partitioning.

### T³: Multi-level Tree-based Automatic Program Repair
- ArXiv: 2506.21211 (June 2025)
- **Venue/Date:** Published June 2025
- **Similarity to FTCR:** Moderate - Structures repair through multiple reasoning levels (Sample Retrieval → Cause Analysis → Repair Plan Generation → Patch Generation). The cause analysis stage could naturally condition downstream retrieval on inferred bug characteristics.

### Broader Context: Major Surveys

**10. A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications**
- ArXiv: 2506.23749 (June 2025)
- **Venue/Date:** TOSEM 2026; covers 63 APR systems from Jan 2022 - June 2025
- **Coverage:** Categorizes all recent work into four paradigms (fine-tuning, prompting, procedural pipelines, agentic) with cross-cutting Retrieval-Augmented Generation (RAG) and Analysis-Augmented Generation (AAG) enhancements. This is the most comprehensive recent taxonomy covering the field.

**11. Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches**
- ArXiv: 2510.04905 (October 2025)
- **Venue/Date:** Published October 2025
- **Coverage:** Discusses InferFix's contrastive approach to bug type grouping, mentions partition-friendly approaches like semantic similarity ranking.

### Key Finding: No Direct Competitor Found

**Important:** I did not find a paper that directly proposes **partitioning a retrieval index explicitly by bug type classification** as the core novelty. This suggests:

1. The FTCR approach (classifying bugs → indexing by type → type-specific retrieval) is likely **novel or concurrent**
2. InferFix (2023) is the closest prior work using contrastive learning to group semantically similar bugs
3. Recent 2025-2026 work focuses more on **fine-grained retrieval narrowing** (algorithm detection, cause analysis, context optimization) rather than explicit index partitioning

### Latest SOTA Context
- **SWE-Bench Verified (2026):** Claude Mythos achieves 93.9%, Claude Opus 4.7 at 87.6%
- **Dominant approach:** Agentic frameworks with RAG/AAG enhancements are the current SOTA paradigm
- **Papers with Code:** Shut down July 2025; SWE-Bench leaderboards now primary benchmark

---

## Sources:
- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/abs/2506.23749)
- [InferFix: End-to-End Program Repair with LLMs](https://arxiv.org/abs/2303.07263)
- [Learner-Tailored Program Repair (LSGen)](https://arxiv.org/abs/2601.08545)
- [ReCode: Improving LLM-based Code Repair with Fine-Grained RAG](https://arxiv.org/abs/2509.02330)
- [PatchRecall: Patch-Driven Retrieval for Automated Program Repair](https://arxiv.org/abs/2604.10481)
- [On the Role of Fault Localization Context for LLM-Based Program Repair](https://arxiv.org/abs/2604.05481)
- [ARISE: A Repository-level Graph Representation](https://arxiv.org/abs/2605.03117)
- [RepoRepair: Leveraging Code Documentation](https://arxiv.org/abs/2603.01048)
- [RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code](https://arxiv.org/pdf/2509.16701)
- [ReAPR: Automatic Program Repair via Retrieval-Augmented LLMs](https://link.springer.com/article/10.1007/s11219-025-09728-1)
- [T³: Multi-level Tree-based Automatic Program Repair](https://arxiv.org/abs/2506.21211)
- [Retrieval-Augmented Code Generation: A Survey](https://arxiv.org/abs/2510.04905)
- [SWE-Bench Leaderboards](https://www.swebench.com/)
- [Dissecting the SWE-Bench Leaderboards](https://arxiv.org/abs/2506.17208)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dd73ed5-ff14-4096-86c8-b920377a82f2",
  "isSidechain": true,
  "agentId": "abf2c5b9b247b50e7",
  "requestId": "req_011CatR1Kj95ZR2M1r7JDhcU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99db231e-8d77-4f8e-b3dc-8dc847f362b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WSmmsBZnMQNrDHoho9TYzN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2995,
      "cache_read_input_tokens": 32639,
      "output_tokens": 2408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2995
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2408,
          "cache_read_input_tokens": 32639,
          "cache_creation_input_tokens": 2995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2995,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
