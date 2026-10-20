# Research conversation: Search for "Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation" at Agents4Science 2025. I need to

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a0cddc46ccf143ae0.jsonl`
- **Structured JSON:** [`db2657633172b4cdcf95.json`](../../sessions/db/db2657633172b4cdcf95.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-12T01:59:28.778Z_

Search for "Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation" at Agents4Science 2025.

I need to verify:
1. Does this paper exist?
2. What venue — "Agents4Science 2025"?
3. Claims: GPT-4o HumanEval pass@1 from 87% to 92% (+5pp), Claude 3.7 from 92% to 94% (+2pp)
4. Does it really ONLY generate specs without execution verification?

Search queries:
- "Self-Spec Model-Authored Specifications LLM Code Generation"
- "Self-Spec Agents4Science 2025"
- "model authored specification code generation"

Use WebSearch. Report findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "efed0031-f70c-4519-bb4d-6065f690e70c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T01:59:28.779Z_

```json
{
  "parentUuid": "efed0031-f70c-4519-bb4d-6065f690e70c",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "760e7801-5642-49b6-b7f2-c9efa791c7fd",
  "timestamp": "2026-05-12T01:59:28.779Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T01:59:37.164Z_



I'll search for this paper using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "760e7801-5642-49b6-b7f2-c9efa791c7fd",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011Cawr8YxjoR2jQJxBXxR6Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a0026ac-71ec-4ba5-bc4f-16a27b1078a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKb9VNtEbKr96WV6WMfDYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 723,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T01:59:37.276Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MgrmYC3r4CEQkCkutbVxzp`</summary>

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
  "parentUuid": "1a0026ac-71ec-4ba5-bc4f-16a27b1078a5",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011Cawr8YxjoR2jQJxBXxR6Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e058c0e7-9f47-4e04-a30b-8eef1983f26a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKb9VNtEbKr96WV6WMfDYx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 8223,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 723
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 723,
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

_source line 5 · 2026-05-12T01:59:37.285Z_

<details><summary>↩ Tool result · `toolu_01MgrmYC3r4CEQkCkutbVxzp`</summary>

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
  "parentUuid": "e058c0e7-9f47-4e04-a30b-8eef1983f26a",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "216d1a88-56ed-4e90-8449-463bcf4746a9",
  "sourceToolAssistantUUID": "e058c0e7-9f47-4e04-a30b-8eef1983f26a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T01:59:41.444Z_



Now let me run all three search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "216d1a88-56ed-4e90-8449-463bcf4746a9",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011Cawr9BNzMT6wNefqW5eYD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c343977f-2b66-4eb3-ac8c-0d795337d6d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUVBca427YbKAXZGtx4Gwr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T01:59:42.434Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H34USkTjKMmG6ZD59bx1sa`</summary>

```json
{
  "query": "Self-Spec Model-Authored Specifications LLM Code Generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c343977f-2b66-4eb3-ac8c-0d795337d6d7",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011Cawr9BNzMT6wNefqW5eYD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fddad004-f3db-4c0e-9ef4-5cb8b34e7d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUVBca427YbKAXZGtx4Gwr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-12T01:59:42.943Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PnFHiUYrET4h9pGgVVu8Pj`</summary>

```json
{
  "query": "Self-Spec Agents4Science 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fddad004-f3db-4c0e-9ef4-5cb8b34e7d6f",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011Cawr9BNzMT6wNefqW5eYD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c973790-5b33-4ab8-8bff-623ef27a449b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUVBca427YbKAXZGtx4Gwr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T01:59:43.395Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CKQ1BxcLZuv7jD17dJhJ4r`</summary>

```json
{
  "query": "model authored specification code generation HumanEval pass@1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c973790-5b33-4ab8-8bff-623ef27a449b",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011Cawr9BNzMT6wNefqW5eYD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "271cdc5a-0879-4e12-90ec-014cfeb77de6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUVBca427YbKAXZGtx4Gwr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8946,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1406
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 8946,
          "cache_creation_input_tokens": 1406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1406,
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

_source line 10 · 2026-05-12T01:59:49.643Z_

<details><summary>↩ Tool result · `toolu_01PnFHiUYrET4h9pGgVVu8Pj`</summary>

```text
Web search results for query: "Self-Spec Agents4Science 2025"

Links: [{"title":"Open Conference of AI Agents for Science: 2025","url":"https://agents4science.stanford.edu/"},{"title":"Agents4Science 2025: Pioneering Autonomous Research","url":"https://www.emergentmind.com/topics/agents4science-2025"},{"title":"AI Agents for Science","url":"https://agents4science.github.io/"},{"title":"Accepted Papers - Open Conference of AI Agents for Science: 2025","url":"https://agents4science.stanford.edu/accepted-papers.html"},{"title":"Agents4Science 2025 Conference | OpenReview","url":"https://openreview.net/group?id=Agents4Science%2F2025%2FConference"},{"title":"Stanford-Initiated First Academic Conference for AI Authors: First Author Must Be an AI","url":"https://eu.36kr.com/en/p/3375685195848200"},{"title":"Call for Papers - Open Conference of AI Agents for Science 2025","url":"https://agents4science.stanford.edu/call-for-papers.html"},{"title":"They are organising the first scientific conference with AI systems as authors and reviewers","url":"https://sciencemediacentre.es/en/they-are-organising-first-scientific-conference-ai-systems-authors-and-reviewers"},{"title":"Paper Submissions - Open Conference of AI Agents for Science: 2025","url":"https://agents4science.stanford.edu/submissions.html"},{"title":"Meet the researcher hosting a scientific conference by and for AI | MIT Technology Review","url":"https://www.technologyreview.com/2025/08/22/1122304/ai-scientist-research-autonomous-agents/"}]

Based on the search results, here's what I found about Self-Spec Agents4Science 2025:

## Overview

The 1st Open Conference of AI Agents for Science ("Agents4Science") represents a new approach to research conferences, where AI serve as both primary authors and reviewers of research papers. This inaugural conference explores if and how AI can independently generate novel scientific insights, hypotheses, and methodologies while maintaining quality through AI-driven peer review.

## Key Requirements

The first author must be an AI. Submitted papers should have an AI system as the main creator, leading the process of hypothesis generation, experiments, and writing. The AI should be listed as the sole first author. Human researchers can participate as co-authors, playing a role in supporting or supervising related work.

## Conference Details

The conference took place on 22 October 2025. Agents4Science is a one-day online event that encompasses all areas of science, from physics to medicine. All of the work shared was researched, written, and reviewed primarily by AI.

## Results and Approach

Agents4Science 2025 foregrounded modular, multi-agent research architectures. A canonical end-to-end pipeline featured six LLM-agent modules, each mapped to distinct scientific workflow stages. The acceptance rate of ~16% (24 out of 300+) is comparable to many journals and lower than most conferences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c973790-5b33-4ab8-8bff-623ef27a449b",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "2b91fdbf-1c7f-4dda-aa0b-a234c62abf12",
  "sourceToolAssistantUUID": "8c973790-5b33-4ab8-8bff-623ef27a449b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T01:59:50.408Z_

<details><summary>↩ Tool result · `toolu_01H34USkTjKMmG6ZD59bx1sa`</summary>

```text
Web search results for query: "Self-Spec Model-Authored Specifications LLM Code Generation"

Links: [{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation | OpenReview","url":"https://openreview.net/forum?id=6pr7BUGkLp"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/html/2605.02455"},{"title":"SpecGen: Automated Generation of Formal Program Specifications via Large Language Models","url":"https://arxiv.org/html/2401.08807v1"},{"title":"Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants","url":"https://arxiv.org/html/2602.00180v1"},{"title":"GitHub - mosofsky/spec-then-code: LLM prompts for structured software development because quality takes more than just \"good vibes\". · GitHub","url":"https://github.com/mosofsky/spec-then-code"},{"title":"[2401.08807] SpecGen: Automated Generation of Formal Program Specifications via Large Language Models","url":"https://arxiv.org/abs/2401.08807"},{"title":"AddyOsmani.com - How to write a good spec for AI agents","url":"https://addyosmani.com/blog/good-spec/"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"},{"title":"The Spec-to-Code Workflow: Building Software Using Only LLMs | by Mattia D'Argenio | Medium","url":"https://medium.com/@mattia.darge/the-spec-to-code-workflow-building-software-using-only-llms-5e025cd28de0"}]

Here are the search results for "Self-Spec Model-Authored Specifications LLM Code Generation":

## Self-Spec Overview

Self-Spec investigates whether large language models (LLMs) code more reliably when they first author a task-specific specification language and then implement strictly from that spec. It's a lightweight, deterministic orchestration that prompts a model to design a compact spec schema it prefers, instantiate that schema from a problem's docstring and signature, resolve ambiguities via a minimal Q&A loop, and generate code only from the confirmed spec.

## How It Works

The intuition is distributional: a self-authored spec better aligns with a model's internal representational bias, reducing docstring drift and format/edge-case mistakes. Self-Spec keeps the intermediate model-authored and compact, aiming for confirmability under deterministic decoding while remaining on-distribution.

## Performance Results

On HumanEval (pass@1, single sample), Self-Spec improves over direct NL→code for stronger models: GPT-4o 87%→92% (+5) and Claude 3.7 92%→94% (+2); Claude 3.5 dips 90%→89% (-1). Overall, two out of three models saw an accuracy gain by using Self-Spec, highlighting the potential of the approach for state-of-the-art LLMs.

## Broader Context

An emerging approach involves "self-spec" methods where LLMs author their own specifications before generating code. The agent first produces a spec from a high-level prompt, which is then reviewed and refined by humans before the same or another agent implements against it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fddad004-f3db-4c0e-9ef4-5cb8b34e7d6f",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "b7fd5cb1-345e-49ba-a326-09741a49767f",
  "sourceToolAssistantUUID": "fddad004-f3db-4c0e-9ef4-5cb8b34e7d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T01:59:50.471Z_

<details><summary>↩ Tool result · `toolu_01CKQ1BxcLZuv7jD17dJhJ4r`</summary>

```text
Web search results for query: "model authored specification code generation HumanEval pass@1"

Links: [{"title":"HumanEval: A Benchmark for Evaluating LLM Code Generation Capabilities | DataCamp","url":"https://www.datacamp.com/tutorial/humaneval-benchmark-for-evaluating-llm-code-generation-capabilities"},{"title":"What Is HumanEval? | IBM","url":"https://www.ibm.com/think/topics/humaneval"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"GitHub - openai/human-eval: Code for the paper \"Evaluating Large Language Models Trained on Code\" · GitHub","url":"https://github.com/openai/human-eval"},{"title":"HumanEval: LLM Benchmark for Code Generation","url":"https://deepgram.com/learn/humaneval-llm-benchmark"},{"title":"HumanEval | DeepEval by Confident AI - The LLM Evaluation Framework","url":"https://deepeval.com/docs/benchmarks-human-eval"},{"title":"HumanEval Benchmark: Evaluating LLM Code Generation Capability","url":"https://metaschool.so/articles/humaneval-benchmark-for-llm-code-generation"},{"title":"HumanEval Benchmark — Klu","url":"https://klu.ai/glossary/humaneval-benchmark"},{"title":"HumanEval Benchmark (Code Generation)","url":"https://paperswithcode.com/sota/code-generation-on-humaneval"},{"title":"BigCodeBench: The Next Generation of HumanEval","url":"https://huggingface.co/blog/leaderboard-bigcodebench"}]

I found comprehensive information about model-authored specifications for code generation and HumanEval pass@1 metrics. Here's what the search results reveal:

## Self-Spec: Model-Authored Specifications

A research paper proposes whether a generative model can create its own task-specific specification language (a model-invented DSL) and then faithfully implement code from that contract, obtaining a middle path between direct natural language-to-code and fixed human-designed intermediate representations.

## Performance Results on HumanEval pass@1

The "Self-Spec" approach evaluated different models with the following results:

- GPT-4o and Claude 3.7 clearly benefit from Self-Spec, while Claude 3.5 shows a slight decrease in performance with Self-Spec (90% down to 89%)
- Overall, two out of three models saw an accuracy gain by using Self-Spec, highlighting the potential of the approach for state-of-the-art LLMs

## How HumanEval pass@1 Works

HumanEval measures functional correctness using the pass@k metric where for each problem, a model generates k code samples and if any of those samples pass the unit tests, then the problem is considered correctly solved with the pass@k metric estimating the probability that at least one of the k samples is functionally correct. The probability that the top (first) generated code sample is correct is indicated by pass@1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "271cdc5a-0879-4e12-90ec-014cfeb77de6",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "eecdbf38-9c77-4e54-88c1-f97721a04f27",
  "sourceToolAssistantUUID": "271cdc5a-0879-4e12-90ec-014cfeb77de6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-12T01:59:56.060Z_

Now let me search specifically for the paper on OpenReview to confirm the venue and check whether it uses execution verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eecdbf38-9c77-4e54-88c1-f97721a04f27",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrA9j3zz3Q4TqHfAZk9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63a1af84-12b1-4133-b31c-d00bb8e82199",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhScq8VCro4nDuYeHQYEqh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 10352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2763,
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

_source line 14 · 2026-05-12T01:59:57.134Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XxBP162gZYhgdAi8YcLid9`</summary>

```json
{
  "query": "site:openreview.net Self-Spec Model-Authored Specifications 6pr7BUGkLp Agents4Science"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63a1af84-12b1-4133-b31c-d00bb8e82199",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrA9j3zz3Q4TqHfAZk9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e29cecfb-8d94-421f-bdfa-1562125bba71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhScq8VCro4nDuYeHQYEqh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 10352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2763,
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

_source line 15 · 2026-05-12T01:59:57.634Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013nZrA981xp2HAoGZctBCJV`</summary>

```json
{
  "query": "Self-Spec specification code generation \"no execution\" OR \"without execution\" OR \"does not execute\" OR \"no test\" verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e29cecfb-8d94-421f-bdfa-1562125bba71",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrA9j3zz3Q4TqHfAZk9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57a592ab-816d-479f-8cd7-2d7c5688766e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhScq8VCro4nDuYeHQYEqh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2763,
      "cache_read_input_tokens": 10352,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2763
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 10352,
          "cache_creation_input_tokens": 2763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2763,
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

_source line 16 · 2026-05-12T02:00:06.973Z_

<details><summary>↩ Tool result · `toolu_01XxBP162gZYhgdAi8YcLid9`</summary>

```text
Web search results for query: "site:openreview.net Self-Spec Model-Authored Specifications 6pr7BUGkLp Agents4Science"

Links: [{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation | OpenReview","url":"https://openreview.net/forum?id=6pr7BUGkLp"},{"title":"Agents4Science 2025 Conference | OpenReview","url":"https://openreview.net/group?id=Agents4Science%2F2025%2FConference"},{"title":"SpecEval: Evaluating Model Adherence to Behavior Specifications | OpenReview","url":"https://openreview.net/forum?id=pabByp2986"},{"title":"Evaluating Model Adherence to Behavior Specifications","url":"https://openreview.net/pdf/d38f88609a1fb5d40480334cb3b71ffb2e06faf5.pdf"},{"title":"SYSMOBENCH: EVALUATING AI ON FORMALLY MODELING ...","url":"https://openreview.net/pdf/d0eed08e290649943f7c04b29587678285b323e4.pdf"},{"title":"Published as a workshop paper at ICLR 2025 SSI-FM A SELF-IMPROVING CODING AGENT","url":"https://openreview.net/pdf?id=rShJCyLsOr"},{"title":"Self-Adapting Language Models Adam Zweiger∗ Jyothish Pari∗† Han Guo Yoon Kim","url":"https://openreview.net/pdf/d876d7104cce0a8cf2d822ec4ac887af6ef71678.pdf"},{"title":"Under review as a conference paper at ICLR 2024 AUTOAGENTS: A FRAMEWORK","url":"https://openreview.net/pdf/3f85171f1e9abe70ff93bd49a78a2603f02b3b53.pdf"},{"title":"A Computational Framework to Identify Self-Aspects in Text | OpenReview","url":"https://openreview.net/forum?id=CaWKytvIea"}]

I found the research paper you were looking for! Here are the key details about the Self-Spec paper:

## Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation

The paper addresses the question: "Do large language models (LLMs) code more reliably when they first author a task-specific specification language and then implement strictly from that spec?" It introduces Self-Spec, a lightweight, deterministic (T=0) orchestration that prompts a model to (i) design a compact spec schema it prefers, (ii) instantiate that schema from a problem's docstring and signature, (iii) resolve ambiguities via a minimal Q&A loop, and (iv) generate code only from the confirmed spec.

### Key Results

On HumanEval (pass@1, single sample), Self-Spec improves over direct NL→code for stronger models: GPT-4o 87%→92% (+5) and Claude 3.7 92%→94% (+2); Claude 3.5 dips 90%→89% (-1).

### Why It Works

The intuition is distributional: a self-authored spec better aligns with a model's internal representational bias, reducing docstring drift and format/edge-case mistakes.

### Paper Characteristics

This is the first systematic study that lets an LLM design its own spec language for coding. The method is simple (no finetuning), model-agnostic (each model chooses its spec shape), and practical (assumptions are made explicit).

The paper was posted on OpenReview on September 17, 2025, and appears to be affiliated with the Agents4Science 2025 Conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e29cecfb-8d94-421f-bdfa-1562125bba71",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "ef65f931-38de-4715-92df-8777e92ceafd",
  "sourceToolAssistantUUID": "e29cecfb-8d94-421f-bdfa-1562125bba71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T02:00:07.685Z_

<details><summary>↩ Tool result · `toolu_013nZrA981xp2HAoGZctBCJV`</summary>

```text
Web search results for query: "Self-Spec specification code generation "no execution" OR "without execution" OR "does not execute" OR "no test" verification"

Links: [{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"What Is Spec-Driven Development? A Complete Guide | Augment Code","url":"https://www.augmentcode.com/guides/what-is-spec-driven-development"},{"title":"Spec-driven development with AI: Get started with a new open source toolkit - The GitHub Blog","url":"https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/"},{"title":"Automatic Generation and Checking of Program Speciﬁcations","url":"https://dspace.mit.edu/bitstream/handle/1721.1/149926/MIT-LCS-TR-823.pdf?sequence=1&isAllowed=y"},{"title":"Spec Driven Development: Fixing the AI Coding Pipeline with OpenSpec and Claude Code","url":"https://khaledea.substack.com/p/spec-driven-development-fixing-the"},{"title":"OpenSpec — A lightweight spec‑driven framework","url":"https://openspec.dev/"},{"title":"6 Best Spec-Driven Development Tools for AI Coding in 2026 | Augment Code","url":"https://www.augmentcode.com/tools/best-spec-driven-development-tools"},{"title":"OpenSpec (Spec-Driven Development) Failed My Experiment — Instructions.md Was Simpler and Faster - DEV Community","url":"https://dev.to/incomplete_developer/openspec-spec-driven-development-failed-my-experiment-instructionsmd-was-simpler-and-faster-3a5d"},{"title":"GitHub - w3c/spec-generator: Service to automatically generate specs from various source formats · GitHub","url":"https://github.com/w3c/spec-generator"},{"title":"Automatic Program Generation from Formal Specifications using APTS | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-1-4020-6585-9_10"}]

Based on the search results, I found relevant information about Self-Spec. Here's what the research reveals:

## Self-Spec: Model-Authored Specifications

Self-Spec is a lightweight, deterministic orchestration that prompts the model to author its own specification language and then implement strictly according to that specification.

### Key Characteristics:

**Specification-Based Code Generation**: The work addresses whether a generative model can create its own task-specific specification language—a model-invented DSL—and then faithfully implement code from that contract.

**Verification Approach**: Self-Spec improves baseline performance without needing full formal verification, but it does not preclude eventually incorporating formal checks for an extra layer of assurance.

**Implementation Strategy**: The SpecExecutor is conditioned solely on the confirmed WorkingSpec, producing final code and strictly following agreed contracts. Deterministic decoding is enforced (temperature = 0), and the implementation must use exactly the provided function signature.

**Practical Application**: The target use case is everyday natural language-to-code interaction ("vibe programming"), where direct prompting delivers convenience but hits reliability ceilings. In contrast, introducing a specification intermediate makes assumptions explicit, reduces drift, and materially improves outcomes.

The approach was evaluated on the HumanEval benchmark for Python code generation, where the model's responsibility to define and use a spec is hypothesized to engage it in a form of self-consistent planning that improves final accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57a592ab-816d-479f-8cd7-2d7c5688766e",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "0c431d5e-ad3b-4ac1-9da4-a40ef7f51efb",
  "sourceToolAssistantUUID": "57a592ab-816d-479f-8cd7-2d7c5688766e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-12T02:00:10.872Z_

Let me do one more targeted search to confirm the venue affiliation and whether the paper explicitly avoids execution-based verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c431d5e-ad3b-4ac1-9da4-a40ef7f51efb",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrBRA289DnoJpsFAcYW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7c73664-2902-4d2f-97dc-2ac99814a1e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHab6NAeoEngSEjbN6UUEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2130,
      "cache_read_input_tokens": 13115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2130,
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

_source line 19 · 2026-05-12T02:00:11.975Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016F6zUgVjHEXfieWoeYZdDB`</summary>

```json
{
  "query": "openreview.net \"6pr7BUGkLp\" Agents4Science 2025 accepted paper venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7c73664-2902-4d2f-97dc-2ac99814a1e2",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrBRA289DnoJpsFAcYW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baf3734a-aa1b-40c0-b9bb-15f1da3c0b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHab6NAeoEngSEjbN6UUEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2130,
      "cache_read_input_tokens": 13115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2130,
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

_source line 20 · 2026-05-12T02:00:12.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ds4cjRbe3jJ67G3xj1iFDT`</summary>

```json
{
  "query": "Self-Spec \"spec only\" OR \"purely specification\" OR \"no runtime\" OR \"static\" OR \"without running\" code generation deterministic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "baf3734a-aa1b-40c0-b9bb-15f1da3c0b4c",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrBRA289DnoJpsFAcYW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7b6b28d-412f-43a9-824e-d222b25a5fa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHab6NAeoEngSEjbN6UUEa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2130,
      "cache_read_input_tokens": 13115,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2130
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 13115,
          "cache_creation_input_tokens": 2130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2130,
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

_source line 21 · 2026-05-12T02:00:17.439Z_

<details><summary>↩ Tool result · `toolu_016F6zUgVjHEXfieWoeYZdDB`</summary>

```text
Web search results for query: "openreview.net "6pr7BUGkLp" Agents4Science 2025 accepted paper venue"

Links: [{"title":"Venues | OpenReview","url":"https://openreview.net/"},{"title":"Agents4Science 2025 Conference | OpenReview","url":"https://openreview.net/group?id=Agents4Science%2F2025%2FConference"},{"title":"Accepted Papers - Open Conference of AI Agents for Science: 2025","url":"https://agents4science.stanford.edu/accepted-papers.html"},{"title":"ICLR 2025 Conference Submissions","url":"https://openreview.net/submissions?venue=ICLR.cc/2025/Conference"},{"title":"NeurIPS 2025 Call for Papers","url":"https://neurips.cc/Conferences/2025/CallForPapers"},{"title":"2025 OpenReview Profile Instructions","url":"https://iccv.thecvf.com/Conferences/2025/CompleteYourORProfile"},{"title":"Venue Directory | OpenReview","url":"https://openreview.net/venues"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"},{"title":"ICLR 2025 | OpenReview","url":"https://openreview.net/group?id=ICLR.cc/2025"},{"title":"OpenReviewer: A Specialized Large Language Model for Generating Critical Scientific Paper Reviews","url":"https://arxiv.org/html/2412.11948v3"}]

The search results show that Agents4Science 2025 Conference has an OpenReview homepage, and there are accepted papers at Agents4Science 2025 - The 1st Open Conference of AI Agents for Science. However, the specific paper ID "6pr7BUGkLp" does not appear in these results. 

The search results indicate that the Agents4Science 2025 conference uses OpenReview as its submission platform, but to find the specific paper with that ID, you would need to:

1. Visit the OpenReview page directly: https://openreview.net/group?id=Agents4Science%2F2025%2FConference
2. Or visit the conference's accepted papers page: https://agents4science.stanford.edu/accepted-papers.html

These pages should contain the specific paper information you're looking for with that submission ID.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baf3734a-aa1b-40c0-b9bb-15f1da3c0b4c",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "f98ba03f-206a-4118-afd7-a27471c0439f",
  "sourceToolAssistantUUID": "baf3734a-aa1b-40c0-b9bb-15f1da3c0b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T02:00:22.412Z_

<details><summary>↩ Tool result · `toolu_01Ds4cjRbe3jJ67G3xj1iFDT`</summary>

```text
Web search results for query: "Self-Spec "spec only" OR "purely specification" OR "no runtime" OR "static" OR "without running" code generation deterministic"

Links: [{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"Haskell for all: A sufficiently detailed spec is code","url":"https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code"},{"title":"Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants","url":"https://arxiv.org/html/2602.00180v1"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation | OpenReview","url":"https://openreview.net/forum?id=6pr7BUGkLp"},{"title":"Spec Driven Development: When Architecture Becomes Executable - InfoQ","url":"https://www.infoq.com/articles/spec-driven-development/"},{"title":"GitHub - emmtrix/emx-onnx-cgen: Deterministic ONNX-to-C compiler for embedded and safety-critical systems, generating static, auditable C code with no dynamic memory or runtime dependencies. · GitHub","url":"https://github.com/emmtrix/emx-onnx-cgen"},{"title":"Spec-Driven Development with AI Agents: From Build to Runtime Diagnostics | by Dave Patten | Medium","url":"https://medium.com/@dave-patten/spec-driven-development-with-ai-agents-from-build-to-runtime-diagnostics-415025fb1d62"},{"title":"6 Best Spec-Driven Development Tools for AI Coding in 2026 | Augment Code","url":"https://www.augmentcode.com/tools/best-spec-driven-development-tools"},{"title":"Reading 7: Designing Specifications","url":"https://web.mit.edu/6.005/www/fa15/classes/07-designing-specs/"},{"title":"Spec-Driven Development: What It Really Is (and What It Isn’t) | by Silvana Trabalon | Feb, 2026 | Medium","url":"https://sil-trabalon.medium.com/spec-driven-development-what-it-really-is-and-what-it-isnt-a0e576c96c96"}]

Based on the search results, here's what I found about Self-Spec and related spec-driven development approaches:

## Self-Spec Overview

Self-Spec is a lightweight, deterministic (T=0) orchestration that prompts the model to author its own specification language and then implement strictly from that spec.

## Key Characteristics

Self-Spec prompts a model to (i) design a compact spec schema it prefers, (ii) instantiate that schema from a problem's docstring and signature, (iii) resolve ambiguities via a minimal Q&A loop, and (iv) generate code only from the confirmed spec.

The approach emphasizes determinism: The model uses deterministic decoding with temperature T = 0, which means the model will always produce the same output for a given prompt, and they sample a single solution per task (pass@1 setting).

## Performance Results

On HumanEval (pass@1, single sample), Self-Spec improves over direct NL→code for stronger models: GPT-4o 87%→92% (+5) and Claude 3.7 92%→94% (+2).

## Broader Spec-Driven Development Context

An emerging approach involves "self-spec" methods where LLMs author their own specifications before generating code, with the agent first producing a spec from a high-level prompt, which is then reviewed and refined by humans before the same or another agent implements against it.

The fundamental principle behind this approach is that a spec authored by the model is more likely to match patterns learned during pretraining (structured NL, pseudo-code, bulletized constraints, mini-APIs), reducing docstring drift, inconsistent assumptions, and formatting/edge-case issues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7b6b28d-412f-43a9-824e-d222b25a5fa1",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "97b5613f-8f1b-4f26-a488-538bfbc83d3f",
  "sourceToolAssistantUUID": "a7b6b28d-412f-43a9-824e-d222b25a5fa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T02:00:27.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LnH1HyaDqaeR74f39hnNX3`</summary>

```json
{
  "query": "agents4science.stanford.edu accepted papers \"Self-Spec\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97b5613f-8f1b-4f26-a488-538bfbc83d3f",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrCW6TP5H2HTRuuHcwo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c372bf8a-f0cd-4567-b64b-e67eb0f92bee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWBQXWdzkNcsxZ7whLTSxw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1850,
      "cache_read_input_tokens": 15245,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1850
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 15245,
          "cache_creation_input_tokens": 1850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1850,
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

_source line 24 · 2026-05-12T02:00:30.449Z_

<details><summary>↩ Tool result · `toolu_01LnH1HyaDqaeR74f39hnNX3`</summary>

```text
Web search results for query: "agents4science.stanford.edu accepted papers "Self-Spec""

No links found.

The search didn't return any results. This could mean that the specific combination of terms—the agents4science.stanford.edu domain, accepted papers, and "Self-Spec"—doesn't have indexed web results, or the information may not be publicly available online yet.

You might want to try:
1. Visiting agents4science.stanford.edu directly to browse their accepted papers
2. Searching for just "Self-Spec" or the authors' names if you know them
3. Searching for "Self-Spec agents for science" without the domain restriction

Would you like me to try a different search query?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c372bf8a-f0cd-4567-b64b-e67eb0f92bee",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "7632f6f5-091f-4de6-ab7a-7c0e205096a7",
  "sourceToolAssistantUUID": "c372bf8a-f0cd-4567-b64b-e67eb0f92bee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-12T02:00:35.049Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01D4PdaTgvimvnC45qkXyEkk`</summary>

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
  "parentUuid": "7632f6f5-091f-4de6-ab7a-7c0e205096a7",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrD6Rh9GiVJngAuj1VY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "039e933e-2afe-48cf-944b-0581d41abc83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018J7FmGPPn6NBHq37dTgfop",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 17095,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 262
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 17095,
          "cache_creation_input_tokens": 262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 262,
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

_source line 26 · 2026-05-12T02:00:35.053Z_

<details><summary>↩ Tool result · `toolu_01D4PdaTgvimvnC45qkXyEkk`</summary>

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
  "parentUuid": "039e933e-2afe-48cf-944b-0581d41abc83",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "6084748f-7b89-46fe-86a0-ef6d5fb992c2",
  "sourceToolAssistantUUID": "039e933e-2afe-48cf-944b-0581d41abc83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-12T02:00:38.997Z_



Let me fetch the OpenReview page and the accepted papers page directly to confirm the venue and check for execution verification details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6084748f-7b89-46fe-86a0-ef6d5fb992c2",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrDSMWVZYts4f9Mvgbf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4bce490-638b-4bdb-a147-1f5a6de48ba9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154Fz1UuJPcw79XciydYDHc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 17357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-12T02:00:41.761Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0188cQrXvscxF73vsWCTXHa3`</summary>

```json
{
  "url": "https://openreview.net/forum?id=6pr7BUGkLp",
  "prompt": "What is the venue/conference this paper was submitted to or published at? Is it Agents4Science 2025? List the venue, submission date, authors, and any acceptance/decision status. Also note any details about whether the method uses execution-based verification or test execution."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4bce490-638b-4bdb-a147-1f5a6de48ba9",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrDSMWVZYts4f9Mvgbf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cb7258b-508e-42b9-a6af-ed432f58496d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154Fz1UuJPcw79XciydYDHc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 17357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T02:00:43.525Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CHqaDP846eXRzcAYzq2RpQ`</summary>

```json
{
  "url": "https://agents4science.stanford.edu/accepted-papers.html",
  "prompt": "Search the list of accepted papers for anything called \"Self-Spec\" or \"Model-Authored Specifications\" or related to specification-driven code generation. List the title if found, or confirm it is not in the list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cb7258b-508e-42b9-a6af-ed432f58496d",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrDSMWVZYts4f9Mvgbf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "657ff7d0-e00a-4d46-913f-7909349fa41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154Fz1UuJPcw79XciydYDHc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 17357,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 595
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 286,
          "cache_read_input_tokens": 17357,
          "cache_creation_input_tokens": 595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 595,
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

_source line 30 · 2026-05-12T02:00:45.795Z_

<details><summary>↩ Tool result · `toolu_01CHqaDP846eXRzcAYzq2RpQ`</summary>

```text
I found the paper you're looking for in the accepted papers list:

**"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation"** by Zihao Xu, Xiao Cheng, Jingling Xue, and Yuekang Li

This work appears in the general accepted papers section and addresses specification-driven approaches to improve code generation reliability through language models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "657ff7d0-e00a-4d46-913f-7909349fa41e",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "3701fbe7-567a-4a8d-870f-aad84087fa5b",
  "sourceToolAssistantUUID": "657ff7d0-e00a-4d46-913f-7909349fa41e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-12T02:00:46.831Z_

<details><summary>↩ Tool result · `toolu_0188cQrXvscxF73vsWCTXHa3`</summary>

```text
# Paper Details

**Venue:** Agents4Science 2025 Conference

**Publication Date:** October 8, 2025 (Last Modified: October 18, 2025)

**Authors:** Zihao Xu, Xiao Cheng, Jingling Xue, Yuekang Li

**Submission Number:** 206

**Acceptance Status:** Published (no explicit rejection or conditional acceptance noted)

## Method Overview

The Self-Spec approach is described as a "lightweight, deterministic (T=0) orchestration" that guides models through four steps: designing a specification schema, instantiating it from problem documentation, resolving ambiguities via Q&A, and then generating code. The researchers note this method involves "no finetuning" and is "model-agnostic."

## Verification Approach

The paper does **not employ execution-based verification or test execution**. Instead, it focuses on specification-driven code generation where the model works from self-authored formal specifications rather than directly from natural language. Results are measured through pass@1 rates on HumanEval benchmark tasks, which implies standard test suite evaluation rather than a novel verification mechanism within the Self-Spec method itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cb7258b-508e-42b9-a6af-ed432f58496d",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "458c32c7-d4bd-429f-930f-62b0899312d2",
  "sourceToolAssistantUUID": "1cb7258b-508e-42b9-a6af-ed432f58496d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-12T02:00:50.419Z_

Now let me fetch the actual PDF to get precise details about the execution/verification methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "458c32c7-d4bd-429f-930f-62b0899312d2",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrEJWVrbqCiYtaErF5H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbdb6ce1-ac72-4b92-abb4-27c7ffa0c7f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsR969BYnUfQXpDeGmJJCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 122,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 17952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
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

_source line 33 · 2026-05-12T02:00:53.970Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HrgPLdejdzMCFcgoUHB6pK`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=6pr7BUGkLp",
  "prompt": "Focus on the methodology section. Does Self-Spec use any form of execution-based verification, test execution, code running, or runtime feedback? Or does it ONLY generate specifications and then generate code from those specs without ever executing or testing the code as part of its pipeline? Describe the exact pipeline steps. Also confirm the exact HumanEval pass@1 numbers for GPT-4o baseline vs Self-Spec, Claude 3.7 baseline vs Self-Spec, and Claude 3.5 baseline vs Self-Spec."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbdb6ce1-ac72-4b92-abb4-27c7ffa0c7f1",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrEJWVrbqCiYtaErF5H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28c812dc-3627-419f-8756-87b167bc4d57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsR969BYnUfQXpDeGmJJCT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 122,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 17952,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 588
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 122,
          "output_tokens": 225,
          "cache_read_input_tokens": 17952,
          "cache_creation_input_tokens": 588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 588,
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

_source line 34 · 2026-05-12T02:00:59.528Z_

<details><summary>↩ Tool result · `toolu_01HrgPLdejdzMCFcgoUHB6pK`</summary>

```text
# Self-Spec Methodology Analysis

## Execution-Based Verification

Self-Spec does **NOT** use execution-based verification or runtime feedback. The pipeline is specification-then-code generation only:

The methodology follows this sequence: "(1) Generate specification from problem description, (2) Generate code from specification" without any intermediate test execution or code running steps.

## Pipeline Steps

The exact process involves:
1. Taking a natural language problem description
2. Generating a formal specification document
3. Using that specification to generate implementation code
4. No execution or testing occurs between specification generation and code generation

This is a **pure generation pipeline** without runtime verification loops.

## HumanEval Results

Unfortunately, the provided document content does not contain the specific HumanEval pass@1 numerical comparisons requested. The PDF appears to be a technical paper, but the extracted text sections don't include the concrete baseline performance metrics for:
- GPT-4o baseline vs Self-Spec
- Claude 3.7 baseline vs Self-Spec  
- Claude 3.5 baseline vs Self-Spec

To obtain these specific numbers, you would need to review the results table or performance section of the full paper document.

[Binary content (application/pdf, 413.5KB) also saved to /home/ubuntu/.claude-account-3/projects/-/9dc8ea75-e85f-4dda-a834-b95c01def98c/tool-results/webfetch-1778551254867-f07ruc.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28c812dc-3627-419f-8756-87b167bc4d57",
  "isSidechain": true,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "agentId": "a0cddc46ccf143ae0",
  "type": "user",
  "uuid": "d357bb33-6f25-436a-9b63-7c23b234a924",
  "sourceToolAssistantUUID": "28c812dc-3627-419f-8756-87b167bc4d57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-12T02:01:18.292Z_

Here are my findings across all four questions:

---

**1. Does the paper exist?**

Yes. "Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation" is a real paper. It is hosted on OpenReview at submission ID `6pr7BUGkLp`. Authors are **Zihao Xu, Xiao Cheng, Jingling Xue, and Yuekang Li**. It was published on October 8, 2025, and last modified October 18, 2025.

**2. What venue -- "Agents4Science 2025"?**

Confirmed. The paper's OpenReview page lists the venue as **Agents4Science 2025 Conference** (the 1st Open Conference of AI Agents for Science, affiliated with Stanford). It also appears on the conference's official accepted papers page at `agents4science.stanford.edu/accepted-papers.html`. The conference took place on October 22, 2025, with an acceptance rate of approximately 16% (24 out of 300+ submissions).

**3. Claims: GPT-4o HumanEval pass@1 from 87% to 92% (+5pp), Claude 3.7 from 92% to 94% (+2pp)?**

Confirmed. Multiple search results corroborate the exact figures:
- **GPT-4o**: 87% -> 92% (+5 percentage points)
- **Claude 3.7**: 92% -> 94% (+2 percentage points)
- **Claude 3.5**: 90% -> 89% (-1 percentage point, a slight regression)

All measured on HumanEval pass@1 with a single sample under deterministic decoding (temperature = 0).

**4. Does it really ONLY generate specs without execution verification?**

Yes, confirmed. Self-Spec is a **pure generation pipeline** with no execution-based verification or runtime feedback. The four-step pipeline is:
1. The model designs a compact spec schema it prefers
2. It instantiates that schema from the problem's docstring and signature
3. It resolves ambiguities via a minimal Q&A loop (still purely generative, no code execution)
4. It generates code solely from the confirmed spec

There is no intermediate test execution, no code running, and no runtime verification loop within the method. The pass@1 evaluation uses the standard HumanEval test suite *after* generation, but that is the benchmark's evaluation protocol, not part of the Self-Spec method itself. The paper explicitly describes the approach as "lightweight" and requiring "no finetuning."

---

Sources:
- [Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation (OpenReview forum)](https://openreview.net/forum?id=6pr7BUGkLp)
- [Self-Spec PDF](https://openreview.net/pdf?id=6pr7BUGkLp)
- [Agents4Science 2025 Conference (OpenReview)](https://openreview.net/group?id=Agents4Science%2F2025%2FConference)
- [Agents4Science 2025 Accepted Papers](https://agents4science.stanford.edu/accepted-papers.html)
- [Agents4Science 2025 Main Site](https://agents4science.stanford.edu/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d357bb33-6f25-436a-9b63-7c23b234a924",
  "isSidechain": true,
  "agentId": "a0cddc46ccf143ae0",
  "requestId": "req_011CawrFEmYeZLLvJjWMVwsn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d903f14-6b6e-4b03-bea8-f4d3fd85014e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NjX35WJ97TLdYgbYoc58L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 18540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 704,
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
