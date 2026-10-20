# Research conversation: Search for whether ReliabilityRAG (NeurIPS 2025) has open-source code available. Search for "ReliabilityRAG code github"

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aeedb491257612572.jsonl`
- **Structured JSON:** [`088147edb5dcb16374ea.json`](../../sessions/08/088147edb5dcb16374ea.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-30T07:20:44.339Z_

Search for whether ReliabilityRAG (NeurIPS 2025) has open-source code available. Search for "ReliabilityRAG code github" and "ReliabilityRAG NeurIPS 2025 implementation". Also check what baselines ReliabilityRAG compared against in its paper. Report concisely in under 150 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c76aef35-f9e0-437d-8b89-5335014d3c7a",
  "agentId": "aeedb491257612572",
  "type": "user",
  "uuid": "1379ef28-2684-4914-99ec-ec0556b0baaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T07:20:44.344Z_

```json
{
  "parentUuid": "1379ef28-2684-4914-99ec-ec0556b0baaa",
  "isSidechain": true,
  "agentId": "aeedb491257612572",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c3cdcf2b-87a5-4d6f-8ee4-37d894bb6205",
  "timestamp": "2026-05-30T07:20:44.344Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-30T07:20:45.717Z_

I'll search for ReliabilityRAG's open-source code and baseline information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3cdcf2b-87a5-4d6f-8ee4-37d894bb6205",
  "isSidechain": true,
  "agentId": "aeedb491257612572",
  "requestId": "req_011CbYMBvuBYYU6mGuRfBJrV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6287ba27-2ad7-469c-ba27-125d88adb9ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JE7pkhkJR49heeVyhA8VCa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16733,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16733,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 4 · 2026-05-30T07:20:45.905Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K9uK7uPmf98HY9zBQUwiPQ`</summary>

```json
{
  "query": "ReliabilityRAG code github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6287ba27-2ad7-469c-ba27-125d88adb9ac",
  "isSidechain": true,
  "agentId": "aeedb491257612572",
  "requestId": "req_011CbYMBvuBYYU6mGuRfBJrV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2c7c61f-13c2-4f45-8dc1-7af270d6c9f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JE7pkhkJR49heeVyhA8VCa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16733,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16733,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 5 · 2026-05-30T07:20:46.142Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013F179f369vsvzmHDXfYYSz`</summary>

```json
{
  "query": "ReliabilityRAG NeurIPS 2025 implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2c7c61f-13c2-4f45-8dc1-7af270d6c9f1",
  "isSidechain": true,
  "agentId": "aeedb491257612572",
  "requestId": "req_011CbYMBvuBYYU6mGuRfBJrV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0dabc741-95f3-4bf9-847b-defe44ab5455",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JE7pkhkJR49heeVyhA8VCa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16733,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16733,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 6 · 2026-05-30T07:20:46.217Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DAjKBvioBn1nMtxBBeVoyy`</summary>

```json
{
  "query": "ReliabilityRAG NeurIPS 2025 baselines comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dabc741-95f3-4bf9-847b-defe44ab5455",
  "isSidechain": true,
  "agentId": "aeedb491257612572",
  "requestId": "req_011CbYMBvuBYYU6mGuRfBJrV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c0927932-ca56-48c9-a7bd-212e184d0f52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JE7pkhkJR49heeVyhA8VCa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16733,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16733,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 7 · 2026-05-30T07:20:52.576Z_

<details><summary>↩ Tool result · `toolu_01DAjKBvioBn1nMtxBBeVoyy`</summary>

```text
Web search results for query: "ReliabilityRAG NeurIPS 2025 baselines comparison"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/poster/119236"},{"title":"NeurIPS 2025 Recap | Amplify Partners","url":"https://www.amplifypartners.com/blog-posts/neurips-2025-recap"},{"title":"From bigger models to better intelligence: what NeurIPS 2025 tells us about progress","url":"https://lambda.ai/blog/neurips-2025-from-bigger-models-to-better-intelligence"},{"title":"Retrieval-Augmented Generation with Estimation of Source Reliability","url":"https://arxiv.org/pdf/2410.22954"},{"title":"Medical QA dialogue datasets in RAG systems performance evaluation and ChatGPT optimization","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12739145/"}]

Based on the search results, here's what I found about ReliabilityRAG and its baselines comparison at NeurIPS 2025:

## Overview

ReliabilityRAG was presented at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025), and it introduces a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents.

## Baselines Comparison

The paper compares reliability-aware methods against several baselines: Vanilla RAG, which concatenates all retrieved passages without any defense mechanism; RobustRAG (Keyword), which is designed for adversarial robustness; and AstuteRAG, a framework designed to handle misinformation.

## Results

ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.

The work addresses performance limitations in existing robust RAG frameworks that overlook valuable document rank or reliability information, and ReliabilityRAG tackles these issues directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0927932-ca56-48c9-a7bd-212e184d0f52",
  "isSidechain": true,
  "promptId": "c76aef35-f9e0-437d-8b89-5335014d3c7a",
  "agentId": "aeedb491257612572",
  "type": "user",
  "uuid": "81b544fb-64f6-40ab-9d57-077b9582344a",
  "sourceToolAssistantUUID": "c0927932-ca56-48c9-a7bd-212e184d0f52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-30T07:20:52.709Z_

<details><summary>↩ Tool result · `toolu_01K9uK7uPmf98HY9zBQUwiPQ`</summary>

```text
Web search results for query: "ReliabilityRAG code github"

Links: [{"title":"GitHub - zeyushen-yo/ReliabilityRAG","url":"https://github.com/zeyushen-yo/ReliabilityRAG"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"Retrieval-Augmented Generation with Estimation of Source Reliability","url":"https://arxiv.org/pdf/2410.22954"},{"title":"URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models","url":"https://arxiv.org/pdf/2603.19281"},{"title":"A Decentralized Retrieval Augmented Generation System with Source Reliabilities Secured on Blockchain","url":"https://arxiv.org/pdf/2511.07577"},{"title":"StackRAG Agent: Improving Developer Answers with Retrieval-Augmented   Generation","url":"https://arxiv.org/pdf/2406.13840"}]

Based on the search results, I found information about ReliabilityRAG:

The ReliabilityRAG code is available on GitHub at zeyushen-yo/ReliabilityRAG and can be run using the command `python main.py` with parameters like `--model_name` (supporting mistral7b, llama3b, gpt-4o-mini), `--dataset_name` (realtimeqa, realtimeqa-mc, open_nq, biogen), and various other options for attack and defense methods.

ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. The framework adopts a graph-theoretic perspective to identify a "consistent majority" among retrieved documents to filter out malicious ones using a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction.

You can access the repository directly at: https://github.com/zeyushen-yo/ReliabilityRAG


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2c7c61f-13c2-4f45-8dc1-7af270d6c9f1",
  "isSidechain": true,
  "promptId": "c76aef35-f9e0-437d-8b89-5335014d3c7a",
  "agentId": "aeedb491257612572",
  "type": "user",
  "uuid": "7efcb617-76f0-45a4-a933-2224f9dc3849",
  "sourceToolAssistantUUID": "f2c7c61f-13c2-4f45-8dc1-7af270d6c9f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-30T07:20:53.196Z_

<details><summary>↩ Tool result · `toolu_013F179f369vsvzmHDXfYYSz`</summary>

```text
Web search results for query: "ReliabilityRAG NeurIPS 2025 implementation"

Links: [{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/poster/119236"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"NeurIPS 2025 oral: Why does the multimodal RAG still answer nonsense? | by L.J. | Dec, 2025 | Medium","url":"https://medium.com/@zljdanceholic/neurips-2025-oral-why-does-the-multimodal-rag-still-answer-nonsense-72505164a34d"},{"title":"GitHub - LHRLAB/HyperGraphRAG: [NeurIPS 2025] Official resources of \"HyperGraphRAG: Retrieval-Augmented Generation via Hypergraph-Structured Knowledge Representation\". · GitHub","url":"https://github.com/LHRLAB/HyperGraphRAG"},{"title":"RMIT-ADM+S at the MMU-RAG NeurIPS 2025 Competition","url":"https://arxiv.org/pdf/2602.20735"}]

Based on the search results, here's what I found about ReliabilityRAG and NeurIPS 2025:

## ReliabilityRAG Overview

ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. RAG systems remain vulnerable to attacks on the retrieval corpus, such as prompt injection.

## Implementation Details

The algorithm is based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction. The MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees.

## Context and Motivation

RAG-based search presents a particularly interesting adversarial setting because it includes built-in reliability signals—such as document ranking—that are difficult for adversaries to circumvent. RAG-based search systems (e.g., Google's Search AI Overview) present an interesting setting for studying and protecting against such threats, as defense algorithms can benefit from built-in reliability signals—like document ranking.

The research was presented as a poster at NeurIPS 2025 on December 4, 2025, and additional resources including a project page, slides, and the paper on OpenReview are available through the official NeurIPS posting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dabc741-95f3-4bf9-847b-defe44ab5455",
  "isSidechain": true,
  "promptId": "c76aef35-f9e0-437d-8b89-5335014d3c7a",
  "agentId": "aeedb491257612572",
  "type": "user",
  "uuid": "531d12b3-5846-437c-b33a-095ffeb55b39",
  "sourceToolAssistantUUID": "0dabc741-95f3-4bf9-847b-defe44ab5455",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-30T07:20:56.750Z_

## Summary

**ReliabilityRAG Open-Source Code:** Yes, available at [GitHub - zeyushen-yo/ReliabilityRAG](https://github.com/zeyushen-yo/ReliabilityRAG). The code supports multiple models (Mistral-7B, Llama-3B, GPT-4o-mini) and datasets (RealtimeQA, Open-NQ, BioGen).

**Baselines Compared:** ReliabilityRAG compared against Vanilla RAG, RobustRAG (Keyword), and AstuteRAG. The framework uses a Maximum Independent Set algorithm on document contradiction graphs to filter adversarial passages while preserving reliability signals from document ranking.

**NeurIPS 2025 Presentation:** Presented as a poster on December 4, 2025, focusing on provably robust defense for RAG-based web search systems.

Sources:
- [GitHub - zeyushen-yo/ReliabilityRAG](https://github.com/zeyushen-yo/ReliabilityRAG)
- [ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search](https://arxiv.org/pdf/2509.23519)
- [NeurIPS Poster ReliabilityRAG](https://neurips.cc/virtual/2025/poster/119236)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "531d12b3-5846-437c-b33a-095ffeb55b39",
  "isSidechain": true,
  "agentId": "aeedb491257612572",
  "requestId": "req_011CbYMCZvtnYw4GAjCs7H3N",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "22eecd63-327b-4546-be8a-8f9d4c1b7ad2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "68ffa26f-3917-4bbd-8456-e29cec68656c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01658QYHyk5mRigAkRm297nh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 606,
      "cache_creation_input_tokens": 1399,
      "cache_read_input_tokens": 16733,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1399
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 606,
          "output_tokens": 329,
          "cache_read_input_tokens": 16733,
          "cache_creation_input_tokens": 1399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1399,
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
