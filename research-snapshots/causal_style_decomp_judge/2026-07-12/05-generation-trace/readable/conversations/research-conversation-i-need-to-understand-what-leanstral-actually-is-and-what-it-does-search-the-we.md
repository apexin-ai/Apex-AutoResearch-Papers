# Research conversation: I need to understand what Leanstral actually is and what it does. Search the web for "Leanstral Mistral Lean 4" and rela

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a496200c6301f6ce4.jsonl`
- **Structured JSON:** [`3c9240374a43dc32ffbf.json`](../../sessions/3c/3c9240374a43dc32ffbf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-27T23:46:26.860Z_

I need to understand what Leanstral actually is and what it does. Search the web for "Leanstral Mistral Lean 4" and related queries. I need to know:
1. Is Leanstral a proof generation/tactic agent or can it do autoformalization (natural language to formal Lean)?
2. What models do M2F and Meta FAIR's autoformalization systems actually use?
3. What are the current best models for autoformalization (informal math → formal Lean 4) as of 2026?

Search for: "Leanstral mistral lean", "M2F autoformalization model GPT", "autoformalization LLM 2026 best model", "ProofBridge ICLR 2026 autoformalization vs proof generation"

Provide detailed findings with sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "ac0bc32d-e16f-431e-88fe-b0257a9aabb6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T23:46:26.864Z_

```json
{
  "parentUuid": "ac0bc32d-e16f-431e-88fe-b0257a9aabb6",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
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
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "fec723f2-01b1-4544-ad16-f9683fe02ec3",
  "timestamp": "2026-05-27T23:46:26.864Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T23:46:26.865Z_

```json
{
  "parentUuid": "fec723f2-01b1-4544-ad16-f9683fe02ec3",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "28843b01-7883-4848-8549-4642cc301694",
  "timestamp": "2026-05-27T23:46:26.865Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 4 · 2026-05-27T23:46:29.853Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014C2jA1vzwCzCKGdo9gfihN`</summary>

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
  "parentUuid": "28843b01-7883-4848-8549-4642cc301694",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxvpyVr3hYk3rNJvW8c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db814f83-7d9e-4679-b9fc-1995f188da6e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TkvCjS7oGyMVqj5pLDJTe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8932,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8932,
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

### Tool result

_source line 5 · 2026-05-27T23:46:29.858Z_

<details><summary>↩ Tool result · `toolu_014C2jA1vzwCzCKGdo9gfihN`</summary>

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
  "parentUuid": "db814f83-7d9e-4679-b9fc-1995f188da6e",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "7d491e0b-e2bf-4d53-80d7-28027f0f85df",
  "sourceToolAssistantUUID": "db814f83-7d9e-4679-b9fc-1995f188da6e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-27T23:46:33.680Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CJDrEErStRmhLzEZLCFrhS`</summary>

```json
{
  "query": "Leanstral Mistral Lean 4 proof generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d491e0b-e2bf-4d53-80d7-28027f0f85df",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxw3stDDX3FqntPDyLt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f7989d7-8b2f-4c4b-8322-e5af58d8cb33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6F4Q2jrqM8F8YPNe9ayKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 8932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 605,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 7 · 2026-05-27T23:46:34.214Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019RBJBUgmeqEn7qsS6L6p3m`</summary>

```json
{
  "query": "M2F autoformalization model GPT mathematics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f7989d7-8b2f-4c4b-8322-e5af58d8cb33",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxw3stDDX3FqntPDyLt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbaa220c-072f-4679-8be5-c030fa880838",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6F4Q2jrqM8F8YPNe9ayKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 8932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 605,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 8 · 2026-05-27T23:46:34.218Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ESu1Wk6P1xt2EhUrLEUgY1`</summary>

```json
{
  "query": "autoformalization LLM 2026 best model informal math formal Lean"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbaa220c-072f-4679-8be5-c030fa880838",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxw3stDDX3FqntPDyLt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b45831f6-f913-422d-9d4b-d393ad9f601d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6F4Q2jrqM8F8YPNe9ayKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 8932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 605,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 9 · 2026-05-27T23:46:34.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TSPWSnAFPHsFWvigwbquav`</summary>

```json
{
  "query": "ProofBridge ICLR 2026 autoformalization proof generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b45831f6-f913-422d-9d4b-d393ad9f601d",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxw3stDDX3FqntPDyLt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9900927-ecce-4a45-a4d0-a744a1876cd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T6F4Q2jrqM8F8YPNe9ayKk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 8932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 605,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 10 · 2026-05-27T23:46:40.944Z_

<details><summary>↩ Tool result · `toolu_01TSPWSnAFPHsFWvigwbquav`</summary>

```text
Web search results for query: "ProofBridge ICLR 2026 autoformalization proof generation"

Links: [{"title":"GitHub - PrithwishJana/ProofBridge: [ICLR-2026 main track] ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. · GitHub","url":"https://github.com/PrithwishJana/ProofBridge"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings [Quick Review]","url":"https://liner.com/review/proofbridge-autoformalization-of-natural-language-proofs-in-lean-via-joint"},{"title":"GitHub - shreyascasturi/proofbridge-nesy-2026: [ICLR-2026 main track] ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains. · GitHub","url":"https://github.com/shreyascasturi/proofbridge-nesy-2026"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=Njrkeo3DiJ"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings | OpenReview","url":"https://openreview.net/forum?id=U2jxHXuOX9"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/pdf/2510.15681"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.13888"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings | Request PDF","url":"https://www.researchgate.net/publication/396693100_ProofBridge_Auto-Formalization_of_Natural_Language_Proofs_in_Lean_via_Joint_Embeddings"}]

Based on the search results, here's information about ProofBridge and ICLR 2026:

## ProofBridge Overview

ProofBridge is a unified framework that translates natural language theorems and proofs into Lean 4 using joint embeddings, cross-modal retrieval-augmented fine-tuning, and iterative proof repair, achieving strong semantic and type correctness gains.

## Publication Details

The paper was published at ICLR-2026 (14th International Conference on Learning Representations), 23-27 April 2026, Rio de Janeiro, Brazil. The pre-print is available at arxiv.org/abs/2510.15681.

## Key Technical Approach

ProofBridge presents a unified framework for automatically translating entire natural language theorems and proofs into Lean 4. At its core is a joint embedding model that aligns NL and FL theorem+proof pairs in a shared semantic space, enabling cross-modal retrieval of semantically relevant FL examples to guide translation.

The framework includes an NL/FL joint embedding model that maps semantically equivalent NL and FL theorem+proof pairs to nearby points in a shared space, enabling cross-modal retrieval of related FL proofs. It fine-tunes the state-of-the-art LLM Kimina-Prover-RL-1.7B to perform NL-to-Lean 4 proof translation, conditioned on the retrieved FL proofs and their relevance scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9900927-ecce-4a45-a4d0-a744a1876cd3",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "cee4f3e4-fbe5-4305-8276-37a17cd3eae2",
  "sourceToolAssistantUUID": "e9900927-ecce-4a45-a4d0-a744a1876cd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-27T23:46:41.233Z_

<details><summary>↩ Tool result · `toolu_01CJDrEErStRmhLzEZLCFrhS`</summary>

```text
Web search results for query: "Leanstral Mistral Lean 4 proof generation"

Links: [{"title":"Leanstral: Mistral AI's Open-Source Agent for Formal Proofs | AIToolly","url":"https://aitoolly.com/ai-news/article/2026-03-17-leanstral-mistral-ais-open-source-agent-for-trustworthy-coding-and-formal-proof-engineering"},{"title":"Mistral Leanstral: AI That Proves Its Own Code | AI Automation Global","url":"https://aiautomationglobal.com/blog/mistral-leanstral-formal-code-verification-2026"},{"title":"Mistral AI's Leanstral Tackles Trust in Code Generation | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/artificial-intelligence/2026/mistral-ai-s-leanstral-tackles-trust-in-code-generation"},{"title":"Leanstral: the open-source agent for formal code proofs - Viral Methods","url":"https://metodoviral.com/en/news/leanstral-the-open-source-agent-for-formal-code-proofs/"},{"title":"Leanstral by Mistral AI: The AI That Proves Your Code Is Correct","url":"https://emelia.io/hub/leanstral-mistral-ai-formal-verification"},{"title":"Leanstral: Open-Source foundation for trustworthy vibe-coding | Mistral AI","url":"https://mistral.ai/news/leanstral"},{"title":"Leanstral download | SourceForge.net","url":"https://sourceforge.net/projects/leanstral.mirror/"},{"title":"Chats-llm","url":"https://chats-llm.com/en/blog/leanstral-release"},{"title":"Leanstral - Mistral AI | Mistral Docs","url":"https://docs.mistral.ai/models/leanstral-26-03"},{"title":"Leanstral Outperforms Claude Sonnet at Formal Code Proofs | Awesome Agents","url":"https://awesomeagents.ai/news/leanstral-mistral-lean4-proof-agent/"}]

Based on the search results, here's what I found about Leanstral, Mistral, Lean 4, and proof generation:

## Overview

Mistral AI has introduced Leanstral, the first open-source code agent specifically designed for the Lean 4 proof assistant. Leanstral was released on March 16, 2026.

## What is Lean 4?

Lean 4 is a proof assistant capable of expressing complex mathematical objects such as perfectoid spaces and software specifications like properties of Rust fragments.

## How Proof Generation Works

Leanstral generates both the code and a machine-checkable mathematical proof that the code is correct. If the proof compiles in Lean 4, the logic is verified — not just tested. The model does not "guess" proofs: it builds them in dialogue with the verifier.

## Technical Architecture

The model utilizes a total parameter count of 119 billion, with only 6.5 billion active parameters per token. This sparse activation strategy allows for faster inference times and lower memory footprint compared to dense models of similar size.

## Performance

Leanstral achieved a benchmark score of 26.3 on FLTEval at pass@2 — beating Claude Sonnet (23.7) at just $36 vs $549.

## Access

Leanstral is integrated directly into Mistral Vibe for immediate, zero-setup vibe coding and proving, and is also accessible via the free/near-free API endpoint labs-leanstral-2603.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f7989d7-8b2f-4c4b-8322-e5af58d8cb33",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "655f7f52-bad2-4c31-b2eb-8dbc3e4e00c2",
  "sourceToolAssistantUUID": "7f7989d7-8b2f-4c4b-8322-e5af58d8cb33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T23:46:42.348Z_

<details><summary>↩ Tool result · `toolu_019RBJBUgmeqEn7qsS6L6p3m`</summary>

```text
Web search results for query: "M2F autoformalization model GPT mathematics"

Links: [{"title":"M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/html/2602.17016v1"},{"title":"(PDF) M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://www.researchgate.net/publication/400970848_M2F_Automated_Formalization_of_Mathematical_Literature_at_Scale"},{"title":"M2F: Automated Formalization of Mathematical Literature at Scale | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.17016v1"},{"title":"M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/pdf/2602.17016"},{"title":"[2602.17016] M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/abs/2602.17016"},{"title":"[2602.17016v1] M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/abs/2602.17016v1"},{"title":"MMFormalizer: Multimodal Autoformalization in the Wild","url":"https://arxiv.org/html/2601.03017"},{"title":"Autoformalize Mathematical Statements by Symbolic Equivalence and   Semantic Consistency","url":"https://arxiv.org/pdf/2410.20936"}]

Based on the search results, here's what I found about the M2F autoformalization model:

## M2F: Automated Formalization of Mathematical Literature at Scale

M2F (Math-to-Formal) is the first agentic framework for end-to-end, project-scale autoformalization in Lean. The model addresses a significant gap in automated mathematics formalization.

### How It Works

The framework operates in two stages. The statement compilation stage splits the document into atomic blocks, orders them via inferred dependencies, and repairs declaration skeletons until the project compiles, allowing placeholders in proofs. The proof repair stage closes these holes under fixed signatures using goal-conditioned local edits.

### Performance

In approximately three weeks, M2F converts long-form mathematical sources into a project-scale Lean library of 153,853 lines from 479 pages textbooks on real analysis and convex analysis, representing textbook-scale formalization at a pace that would typically require months or years of expert effort.

Additionally, on FATE-H it solves 96% fully automatically and 97% with a 31-declaration natural-language lemma map.

### GPT Connection

Notably, M2F surfaced a FATE-H statement error missed by state-of-the-art LLM-based semantic checks (including GPT-5.2 Pro), underscoring the value of formal verification for evaluating and improving large-model mathematical reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbaa220c-072f-4679-8be5-c030fa880838",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "302d9bc5-1537-40df-9a58-e0594a73f260",
  "sourceToolAssistantUUID": "dbaa220c-072f-4679-8be5-c030fa880838",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T23:46:42.908Z_

<details><summary>↩ Tool result · `toolu_01ESu1Wk6P1xt2EhUrLEUgY1`</summary>

```text
Web search results for query: "autoformalization LLM 2026 best model informal math formal Lean"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.15940"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://www.arxiv.org/pdf/2508.04440"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Autoformalization Framework","url":"https://www.emergentmind.com/topics/autoformalization-framework"},{"title":"TOWARDS AUTOFORMALIZATION OF LLM-GENERATED OUTPUTS FOR REQUIREMENT VERIFICATION","url":"https://arxiv.org/pdf/2511.11829"},{"title":"Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM","url":"https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"Conjecturing: An Overlooked Step in Formal Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.11986"}]

Based on the web search results, here's what I found about autoformalization with LLMs in 2026:

## What is Autoformalization?

Autoformalization is the automated translation of informal mathematics into formal proof-assistant code, and has become a key strategy for addressing the scarcity of high-quality formal data.

## Leading Models and Systems (2026)

Systems such as DeepSeek-Prover, InternLM2.5-StepProver, and Goedel Prover series formalize vast Lean corpora for expert iteration. Additionally, StepFun-Formalizer combined with Kimina-Autoformalizer generates the largest dataset under the same computation cost, with models trained on it achieving the best performance.

## LLM-Based Approaches

LLM-based pipelines that translate at scale with few-shot prompting or fine-tuning have eclipsed early neural encoders for statement formalization. LLMs now can perform autoformalization without explicitly training on aligned informal-formal data.

## Lean as a Testbed

Lean, a language for writing formal proofs, has attracted both mathematicians and AI researchers, and since the task allows rigorous evaluation in Lean, it has become increasingly popular as a testbed for LLMs.

## Current Challenges

A central bottleneck is autoformalisation, and on undergraduate-level problems from the ProofNet benchmark, the current state-of-the-art performance is only 31.28%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b45831f6-f913-422d-9d4b-d393ad9f601d",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "9158641f-5c12-4728-9b71-82274fdf1f7c",
  "sourceToolAssistantUUID": "b45831f6-f913-422d-9d4b-d393ad9f601d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-27T23:46:47.256Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SrdXuw7G8eD3MhQhPTm1Dk`</summary>

```json
{
  "query": "Leanstral autoformalization natural language to Lean 4 capabilities"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9158641f-5c12-4728-9b71-82274fdf1f7c",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxx13FinvVkXqxcY5oL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0bd97015-8bae-4915-979a-09ab9f041796",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtcaRjGqSBYu6XTRR5kpvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 967,
      "cache_creation_input_tokens": 2655,
      "cache_read_input_tokens": 9537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2655,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 15 · 2026-05-27T23:46:47.732Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BKYhuKM1PyGvfdBUgKsJSe`</summary>

```json
{
  "query": "M2F autoformalization which LLM backbone GPT Claude model used"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bd97015-8bae-4915-979a-09ab9f041796",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxx13FinvVkXqxcY5oL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3861853b-7647-4878-a39f-844271b7492a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtcaRjGqSBYu6XTRR5kpvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 967,
      "cache_creation_input_tokens": 2655,
      "cache_read_input_tokens": 9537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2655,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 16 · 2026-05-27T23:46:48.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014WDK86X1D9Hu9yRN881s8N`</summary>

```json
{
  "query": "Meta FAIR autoformalization Lean 2025 2026 model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3861853b-7647-4878-a39f-844271b7492a",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxx13FinvVkXqxcY5oL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be4468f9-7684-4c47-bbed-f21da58736fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtcaRjGqSBYu6XTRR5kpvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 967,
      "cache_creation_input_tokens": 2655,
      "cache_read_input_tokens": 9537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2655,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 17 · 2026-05-27T23:46:53.904Z_

<details><summary>↩ Tool result · `toolu_01BKYhuKM1PyGvfdBUgKsJSe`</summary>

```text
Web search results for query: "M2F autoformalization which LLM backbone GPT Claude model used"

Links: [{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/pdf/2511.12784"},{"title":"Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/html/2604.25031"},{"title":"Autoformalization with Large Language Models | OpenReview","url":"https://openreview.net/forum?id=IUikebJ1Bf0"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Conjecturing: An Overlooked Step in Formal Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.11986"},{"title":"Autoformalization with Large Language Models","url":"https://arxiv.org/pdf/2205.12615"},{"title":"Autoformalize Mathematical Statements by Symbolic Equivalence and   Semantic Consistency","url":"https://arxiv.org/pdf/2410.20936"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"Best Coding LLMs 2026: Claude 3.5 vs. GPT-4o vs. DeepSeek | VERTU","url":"https://vertu.com/lifestyle/the-best-llms-for-coding-in-2025-a-comprehensive-guide-to-ai-powered-development"}]

Based on the search results, I found relevant information about autoformalization research that uses different LLM backbones:

Recent autoformalization research has used both GPT-4o-mini (OpenAI) and Claude-3.7-sonnet (Anthropic) as LLM backbones for evaluating autoformalization robustness.

Another study on faithful autoformalization evaluated their approach using Claude Opus 4.6 and GPT-5.2.

For autoformalization experiments, researchers have instantiated LLMs as ChatGPT (mostly 5.2) or Claude Sonnet (4.5).

Additional autoformalization research has tested state-of-the-art LLMs including GPT-3.5, GPT-4, and Gemini Pro.

So the main LLM backbones used in autoformalization research include:
- **GPT models**: GPT-3.5, GPT-4, GPT-4o, GPT-5.2
- **Claude models**: Claude Sonnet, Claude Opus
- **Other models**: Gemini Pro, DeepSeek


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3861853b-7647-4878-a39f-844271b7492a",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "f871d9c1-58e4-4ae1-b924-354a3f720ca6",
  "sourceToolAssistantUUID": "3861853b-7647-4878-a39f-844271b7492a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T23:46:54.676Z_

<details><summary>↩ Tool result · `toolu_01SrdXuw7G8eD3MhQhPTm1Dk`</summary>

```text
Web search results for query: "Leanstral autoformalization natural language to Lean 4 capabilities"

Links: [{"title":"Process-Driven Autoformalization in Lean 4","url":"https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4/fulltext/666038b385a4ee7261a6723b/Process-Driven-Autoformalization-in-Lean-4.pdf?origin=scientificContributions"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/html/2406.01940v1"},{"title":"FormaRL: RL-Driven Autoformalization for Lean 4","url":"https://www.emergentmind.com/topics/formarl"},{"title":"Work in progress PROCESS-DRIVEN AUTOFORMALIZATION IN LEAN 4","url":"https://arxiv.org/pdf/2406.01940"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"(PDF) Process-Driven Autoformalization in Lean 4","url":"https://www.researchgate.net/publication/381158622_Process-Driven_Autoformalization_in_Lean_4"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/pdf/2603.24372"},{"title":"[2406.01940] Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/abs/2406.01940"},{"title":"Translating Natural Language into Lean 4 through Multi- ...","url":"https://aclanthology.org/2025.emnlp-main.1586v1.pdf"}]

Based on the search results, I found information about autoformalization capabilities for translating natural language to Lean 4, though the specific "Leanstral" project wasn't prominently featured. Here's what the search revealed about current autoformalization approaches:

## Key Autoformalization Frameworks for Lean 4

Autoformalization is the conversion of natural language mathematics into formal languages, which offers significant potential for advancing mathematical reasoning.

### FormL4 Benchmark

FormL4 is a benchmark specifically designed to assess the autoformalization capabilities of LLMs in Lean 4, encompassing questions, answers, formal statements, and proofs. This comprehensive approach allows for a more accurate assessment of an LLM's ability to understand the syntax of Lean 4 and reason logically within the language's framework.

### FormaRL Framework

FormaRL is a reinforcement learning framework that autoformalizes natural language mathematics into Lean 4 code using a dual reward system, employing a hybrid reward mechanism combining Lean compiler checks and large language model comparisons to ensure both syntactic correctness and semantic fidelity.

### Challenges

The rapid evolution of Lean 4 presents a significant challenge for autoformalization, as keeping up with the evolving syntax, semantics, library, and other aspects of the language requires substantial expertise, and the lack of training data and benchmarks specific to Lean 4 hinders progress.

The search results did not return specific information about a project called "Leanstral" specifically. If you're looking for information about a particular Leanstral implementation, you may want to search for more specific details about that project.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bd97015-8bae-4915-979a-09ab9f041796",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "2ec6bcf4-30f7-4e49-94ac-e0ea300cb1a3",
  "sourceToolAssistantUUID": "0bd97015-8bae-4915-979a-09ab9f041796",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T23:46:55.809Z_

<details><summary>↩ Tool result · `toolu_014WDK86X1D9Hu9yRN881s8N`</summary>

```text
Web search results for query: "Meta FAIR autoformalization Lean 2025 2026 model"

Links: [{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/pdf/2603.24372"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/pdf/2510.06857"},{"title":"Process-Driven Autoformalization in Lean 4 | OpenReview","url":"https://openreview.net/forum?id=k8KsI84Ds7"},{"title":"Autoformalization Framework","url":"https://www.emergentmind.com/topics/autoformalization-framework"}]

Based on the search results, here's what I found about Meta FAIR's autoformalization work related to Lean in 2025-2026:

## Recent Breakthroughs in Autoformalization

In 2025, multiple independent systems achieved gold-medal equivalent performance with formally verified Lean 4 proofs. Systems producing Lean 4 proofs offer a crucial advantage: no human verification required.

## Key Developments

Several notable autoformalization approaches have emerged:

1. **ProofBridge**: A 2025 research effort involving Yong Lin, Shange Tang, and other researchers on auto-formalization of natural language proofs in Lean via joint embeddings.

2. **Tool-Based Approaches**: The Autoformalizer with Tool Feedback (ATF) approach incorporates syntactic and consistency information as tools into the formalization process by integrating Lean 4 compilers for syntax corrections and employing a multi-LLMs-as-judge approach for consistency validation.

3. **Process-Driven Methods**: FormL4, a large-scale dataset designed to comprehensively evaluate autoformalization capabilities, is paired with a Process-Driven Autoformalization framework that leverages precise feedback from Lean 4 compilers to enhance autoformalization.

The search results show significant progress in autoformalization for Lean 4 throughout 2025-2026, though they don't specify exclusive Meta FAIR work. Would you like more specific information about Meta FAIR's particular contributions?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be4468f9-7684-4c47-bbed-f21da58736fd",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "14fce727-4251-49f0-8edd-9c3c98fbe95c",
  "sourceToolAssistantUUID": "be4468f9-7684-4c47-bbed-f21da58736fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-27T23:46:59.774Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QfkwxDxdkoGLg21F28ZaAG`</summary>

```json
{
  "query": "Mistral Leanstral formal verification code proofs NOT autoformalization capabilities"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14fce727-4251-49f0-8edd-9c3c98fbe95c",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxxxCPHMzCUvyRkeWyS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fdc5f1c-48c7-4efc-8367-9819ebb51d6e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RpnJzdvbc7ZmEfUqprtR13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3428,
      "cache_read_input_tokens": 12192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3428,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 21 · 2026-05-27T23:47:00.708Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BR4JZW7MNPLAG9WkufkyYk`</summary>

```json
{
  "query": "M2F arxiv 2602.17016 LLM model backbone architecture details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fdc5f1c-48c7-4efc-8367-9819ebb51d6e",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxxxCPHMzCUvyRkeWyS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2483bda-ac52-4f34-be56-2cc4eb707c2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RpnJzdvbc7ZmEfUqprtR13",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3428,
      "cache_read_input_tokens": 12192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3428,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 22 · 2026-05-27T23:47:01.111Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013AsEQydroxNgVmjy37zQUT`</summary>

```json
{
  "query": "StepFun-Formalizer Kimina-Autoformalizer 2026 autoformalization best performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2483bda-ac52-4f34-be56-2cc4eb707c2f",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxxxCPHMzCUvyRkeWyS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24927e61-b901-4282-bb15-2be49aaa0434",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RpnJzdvbc7ZmEfUqprtR13",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3428,
      "cache_read_input_tokens": 12192,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3428
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 12192,
          "cache_creation_input_tokens": 3428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3428,
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

_source line 23 · 2026-05-27T23:47:06.470Z_

<details><summary>↩ Tool result · `toolu_01BR4JZW7MNPLAG9WkufkyYk`</summary>

```text
Web search results for query: "M2F arxiv 2602.17016 LLM model backbone architecture details"

Links: [{"title":"[2602.17016] M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/abs/2602.17016"},{"title":"A SURVEY OF RESOURCE-EFFICIENT LLM AND MULTIMODAL FOUNDATION MODELS","url":"https://arxiv.org/pdf/2401.08092"},{"title":"Hardware Co-Design Scaling Laws via Roofline Modelling for On-Device LLMs","url":"https://arxiv.org/html/2602.10377"},{"title":"Speed Always Wins: A Survey on Efficient Architectures for Large Language Models","url":"https://arxiv.org/pdf/2508.09834"},{"title":"A2-LLM: An End-to-end Conversational Audio Avatar Large Language Model","url":"https://arxiv.org/html/2602.04913"},{"title":"Fine-tuned large language models enhance influenza forecasting","url":"https://www.medrxiv.org/content/10.1101/2025.03.27.25324747.full.pdf"},{"title":"A Survey on Large Language Models with some Insights on their   Capabilities and Limitations","url":"https://arxiv.org/pdf/2501.04040"}]

Based on the search results, M2F (Math-to-Formal) is the first agentic framework for end-to-end, project-scale autoformalization in Lean. 

However, the search results from the arXiv abstract (2602.17016) do not contain specific details about the LLM model backbone architecture used in M2F. The abstract focuses on the framework's two-stage approach—the statement compilation stage that splits documents into atomic blocks and orders them via inferred dependencies, and the proof repair stage that closes proof holes under fixed signatures using goal-conditioned local edits—but doesn't provide information about which LLM backbone or its architectural specifications are employed.

To get detailed information about the specific LLM model backbone architecture used in M2F, you would need to access the full paper PDF directly from the arXiv link provided in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2483bda-ac52-4f34-be56-2cc4eb707c2f",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "b572424b-4c85-4f8d-8833-6bbd912a4d60",
  "sourceToolAssistantUUID": "f2483bda-ac52-4f34-be56-2cc4eb707c2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-27T23:47:07.586Z_

<details><summary>↩ Tool result · `toolu_01QfkwxDxdkoGLg21F28ZaAG`</summary>

```text
Web search results for query: "Mistral Leanstral formal verification code proofs NOT autoformalization capabilities"

Links: [{"title":"Mistral Leanstral: AI That Proves Its Own Code | AI Automation Global","url":"https://aiautomationglobal.com/blog/mistral-leanstral-formal-code-verification-2026"},{"title":"Leanstral Review: Mistral Just Shipped the AI That Proves Your Code Is Correct | SaaS Pilot — AI & SaaS Tool Reviews","url":"https://saaspilot.org/ai-coding-assistants/2026-03-20-radar-2-leanstral-review/"},{"title":"Leanstral: Mistral AI's Open-Source Agent for Formal Proofs | AIToolly","url":"https://aitoolly.com/ai-news/article/2026-03-17-leanstral-mistral-ais-open-source-agent-for-trustworthy-coding-and-formal-proof-engineering"},{"title":"Leanstral – the first open-source AI coding agent launched by Mistral AI | Alternative AI Tools","url":"https://altools.ai/15389.html"},{"title":"Leanstral: the open-source agent for formal code proofs - Viral Methods","url":"https://metodoviral.com/en/news/leanstral-the-open-source-agent-for-formal-code-proofs/"},{"title":"Leanstral by Mistral AI: The AI That Proves Your Code Is Correct","url":"https://emelia.io/hub/leanstral-mistral-ai-formal-verification"},{"title":"Mistral's new agent proofs your code on the cheap","url":"https://www.theregister.com/2026/03/17/mistral_leanstral_ai_code_verification_tool/"},{"title":"Chats-llm","url":"https://chats-llm.com/en/blog/leanstral-release"},{"title":"Mistral’s Leanstral wants to kill off human-in-the-loop code checks, but is it blowing in the wind? - The New Stack","url":"https://thenewstack.io/leanstral-formal-verification-code/"}]

Based on the search results, here's what I found about Mistral Leanstral's formal verification capabilities:

## Overview

Mistral released Leanstral, the first open-source AI agent that generates Lean 4 formal proofs — mathematically verifying code correctness for $36 vs $549 with Claude Sonnet.

## How It Works

Unlike standard AI coding tools that generate code you then have to test and hope works, Leanstral generates both the code and a machine-checkable mathematical proof that the code is correct. If the proof compiles in Lean 4, the logic is verified — not just tested.

Leanstral uses a process of formal verification to mathematically prove that any given piece of code is capable of performing exactly as specified, with zero subtle (or inconsequential) bugs hidden between the lines.

## Technical Architecture

The model adopts a sparse Mixture-of-Experts (MoE) architecture with 120B total parameters and 6B active parameters. Using a highly sparse architecture optimized for proof engineering tasks, Leanstral leverages parallel inference with Lean acting as a perfect verifier.

## Benchmark Performance

With a benchmark score of 26.3 on FLTEval at pass@2 — beating Claude Sonnet (23.7) at just $36 vs $549 — Leanstral is the most cost-effective formal verification AI available today.

## Release and Availability

Mistral Leanstral — released March 16, 2026 — is the first open-source AI agent specifically built for Lean 4, a formal proof assistant used in software verification and mathematics. Available under Apache 2.0 licensing with a free API endpoint.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fdc5f1c-48c7-4efc-8367-9819ebb51d6e",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "737004b4-7996-4358-bdf9-8b2ff325941a",
  "sourceToolAssistantUUID": "0fdc5f1c-48c7-4efc-8367-9819ebb51d6e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-27T23:47:08.555Z_

<details><summary>↩ Tool result · `toolu_013AsEQydroxNgVmjy37zQUT`</summary>

```text
Web search results for query: "StepFun-Formalizer Kimina-Autoformalizer 2026 autoformalization best performance"

Links: [{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://www.arxiv.org/pdf/2508.04440"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion","url":"https://arxiv.org/html/2508.04440v2"},{"title":"stepfun-ai/StepFun-Formalizer-32B · Hugging Face","url":"https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B"},{"title":"stepfun-ai/StepFun-Formalizer-7B · Hugging Face","url":"https://huggingface.co/stepfun-ai/StepFun-Formalizer-7B"},{"title":"GitHub - stepfun-ai/StepFun-Formalizer: StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion · GitHub","url":"https://github.com/stepfun-ai/StepFun-Formalizer"},{"title":"StepFun-Formalizer-32B: Autoformalization LLM","url":"https://www.emergentmind.com/topics/stepfun-formalizer-32b"},{"title":"arXiv preprint AUTOFORMALIZER WITH TOOL FEEDBACK","url":"https://arxiv.org/pdf/2510.06857"},{"title":"𝚐𝔪𝟾𝚡𝚡𝟾 on X: \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion ThinkingF pipeline - Formal knowledge distillation: 183K Lean4-aligned pairs via majority voting + BEq filtering - Template-guided reasoning: 5.8K trajectories (Claude 3.7) - https://t.co/9AEztEHWPv\" / X","url":"https://x.com/gm8xx8/status/1953483273985757559"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/html/2510.06857v1"}]

Based on the search results, here's what I found about StepFun-Formalizer and Kimina-Autoformalizer's performance on autoformalization:

## Overview

StepFun-Formalizer is a family of large language models designed to translate natural-language mathematical problems into formal statements in Lean 4. Through the fusion of formal knowledge and informal-to-formal reasoning capability, StepFun-Formalizer achieves strong performance on autoformalization tasks.

## Best Performance

Evaluated with BEq verification on mainstream benchmarks including FormalMATH-Lite, ProverBench, and CombiBench, StepFun-Formalizer matches or exceeds all prior general-purpose and specialized autoformalization models of comparable scale.

Specifically, the model achieves state-of-the-art single-shot formalization accuracies of 40.5% on FormalMATH-Lite and 26.7% on ProverBench benchmarks.

## Comparison with Kimina-Autoformalizer

StepFun-Formalizer improves autoformalization performance by combining these two capabilities of formal knowledge and reasoning. Even StepFun-Formalizer-7B surpasses every competing model on both benchmarks, offering a computational efficiency advantage: on FormalMATH-Lite it exceeds the previous best, Kimina-Autoformalizer-7B, which serves as its formal knowledge source.

## Technical Approach

The approach implements two key components: (1) large-scale distillation and selection of data with formal knowledge from specialized models, and (2) informal-to-formal reasoning trajectories synthesis guided by an expert-designed autoformalization template.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24927e61-b901-4282-bb15-2be49aaa0434",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "9c16583b-6118-4d56-b185-a4ce8c34ab46",
  "sourceToolAssistantUUID": "24927e61-b901-4282-bb15-2be49aaa0434",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-27T23:47:13.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HPpH8zPA4EPb2eCgvemgrE`</summary>

```json
{
  "query": "Leanstral mistral.ai blog \"autoformalization\" OR \"natural language\" OR \"informal math\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c16583b-6118-4d56-b185-a4ce8c34ab46",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxythKcjWpPmg2vLp6a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44d1ad5b-2a39-40dc-bcad-4522d132b843",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AzFpFnQPiBnfn4Pw6ytfMt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2795,
      "cache_read_input_tokens": 15620,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2795,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 27 · 2026-05-27T23:47:13.260Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F5CcsNQcKVKdM6zDEi2xt6`</summary>

```json
{
  "query": "M2F autoformalization paper \"GPT-4\" OR \"Claude\" OR \"DeepSeek\" OR \"Sonnet\" backbone agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44d1ad5b-2a39-40dc-bcad-4522d132b843",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxythKcjWpPmg2vLp6a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c23a1ff4-24cb-4f6b-af80-67f59bd0b8c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AzFpFnQPiBnfn4Pw6ytfMt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2795,
      "cache_read_input_tokens": 15620,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2795,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 28 · 2026-05-27T23:47:18.332Z_

<details><summary>↩ Tool result · `toolu_01F5CcsNQcKVKdM6zDEi2xt6`</summary>

```text
Web search results for query: "M2F autoformalization paper "GPT-4" OR "Claude" OR "DeepSeek" OR "Sonnet" backbone agent"

Links: [{"title":"Generative Agents for Multi-Agent Autoformalization of Interaction Scenarios","url":"https://arxiv.org/pdf/2412.08805"},{"title":"Generative Agents for Multi-Agent Autoformalization of Interaction Scenarios","url":"https://arxiv.org/html/2412.08805v3"},{"title":"Claude Opus 4.7 vs GPT-5.2 vs Gemini 3.1 Pro vs DeepSeek V4 (2026)","url":"https://www.getpassionfruit.com/blog/gpt-5-1-vs-claude-4-5-sonnet-vs-gemini-3-pro-vs-deepseek-v3-2-the-definitive-2025-ai-model-comparison"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"GlobalGPT","url":"https://www.glbgpt.com/"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/pdf/2508.04440"},{"title":"Best AI for Coding in 2026: Top 6 Models Ranked - Morph","url":"https://www.morphllm.com/best-ai-model-for-coding"}]

Based on the search results, I found a relevant paper on autoformalization:

**"Generative Agents for Multi-Agent Autoformalization of Interaction Scenarios" (GAMA)**

This paper demonstrates autoformalization of natural language descriptions of game-theoretic scenarios representing social interactions into executable logic programs defining game rules. 

In experiments with 110 natural language descriptions across five 2 × 2 simultaneous-move games, GAMA achieves 100% syntactic and 76.5% semantic correctness with Claude 3.5 Sonnet, and 99.82% syntactic and 77% semantic correctness with GPT-4o. This paper directly compares the performance of Claude 3.5 Sonnet and GPT-4o as backbone models for the autoformalization task.

The paper is available at: https://arxiv.org/pdf/2412.08805


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c23a1ff4-24cb-4f6b-af80-67f59bd0b8c6",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "d41a0b43-067a-4ebd-b980-ccfca3ba11fd",
  "sourceToolAssistantUUID": "c23a1ff4-24cb-4f6b-af80-67f59bd0b8c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-27T23:47:20.734Z_

<details><summary>↩ Tool result · `toolu_01HPpH8zPA4EPb2eCgvemgrE`</summary>

```text
Web search results for query: "Leanstral mistral.ai blog "autoformalization" OR "natural language" OR "informal math""

Links: [{"title":"Leanstral: Mistral's Open-Source AI for Trustworthy Coding - Webkul Blog","url":"https://webkul.com/blog/mistrals-leanstral/"},{"title":"Autoformalize Mathematical Statements by Symbolic Equivalence and   Semantic Consistency","url":"https://arxiv.org/pdf/2410.20936"},{"title":"Autoformalization: Bridging Informal and Formal Math","url":"https://www.emergentmind.com/topics/autoformalization"},{"title":"Mistral Leanstral: AI That Proves Its Own Code | AI Automation Global","url":"https://aiautomationglobal.com/blog/mistral-leanstral-formal-code-verification-2026"},{"title":"Exploring proof autoformalization with Mistral on Herald","url":"https://www.researchgate.net/publication/396318111_Exploring_proof_autoformalization_with_Mistral_on_Herald"},{"title":"Multilingual Mathematical Autoformalization","url":"https://arxiv.org/pdf/2311.03755"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/pdf/2505.23486"}]

I found search results related to Leanstral and autoformalization, though the results don't appear to be specifically from Mistral AI's blog. Here's what I found:

## Leanstral Overview

On March 16, 2026, Mistral AI released Leanstral, the first open-source code agent built for Lean 4. It is implemented to generate the code and formally prove the correctness of the code using Lean 4, a powerful proof assistant.

Leanstral is a Mixture-of-Experts AI model with 119B total parameters, but only 6.5B are used at a time, making the model very efficient while still giving strong results for proof and coding tasks.

## Autoformalization Context

The search results include relevant information about autoformalization in relation to Leanstral's capabilities:

Autoformalization is the automated process of translating from natural language expressions into a formal language. It is the task of automatically translating informal mathematical content—typically written in human natural language or LaTeX—into formal statements or proofs in a machine-verifiable proof assistant language.

The results show that large language models have shown promising performance in autoformalization, especially in formalizing mathematical statements.

Note: The search results do not appear to include content directly from Mistral AI's official blog, but rather from articles and academic papers discussing Leanstral and autoformalization concepts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44d1ad5b-2a39-40dc-bcad-4522d132b843",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "2c64e8e8-b361-4c56-9f70-5d83e8675046",
  "sourceToolAssistantUUID": "44d1ad5b-2a39-40dc-bcad-4522d132b843",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-27T23:47:24.735Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EM5VMgRbD14vPNEwr9zSm8`</summary>

```json
{
  "query": "Leanstral docs.mistral.ai capabilities tactic generation proof search"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c64e8e8-b361-4c56-9f70-5d83e8675046",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxznyoTwKHYaJ5f88V2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8104c62b-5bab-4a0d-bf8a-4c23e72b4827",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ypFuKTbVFyzmCbPaUtcUS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 657,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 18415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 853,
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

_source line 31 · 2026-05-27T23:47:25.537Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Nu437iDNuUWPcyPCYAx1L`</summary>

```json
{
  "query": "\"M2F\" \"Math-to-Formal\" framework LLM \"deepseek\" OR \"o1\" OR \"GPT-4o\" OR \"sonnet\" architecture 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8104c62b-5bab-4a0d-bf8a-4c23e72b4827",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTxznyoTwKHYaJ5f88V2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d59cd41b-c8e8-486a-80df-cba68aeabea2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ypFuKTbVFyzmCbPaUtcUS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 657,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 18415,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 853
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 657,
          "output_tokens": 146,
          "cache_read_input_tokens": 18415,
          "cache_creation_input_tokens": 853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 853,
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

_source line 32 · 2026-05-27T23:47:31.863Z_

<details><summary>↩ Tool result · `toolu_01EM5VMgRbD14vPNEwr9zSm8`</summary>

```text
Web search results for query: "Leanstral docs.mistral.ai capabilities tactic generation proof search"

Links: [{"title":"Mistral AI's Leanstral Tackles Trust in Code Generation | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/artificial-intelligence/2026/mistral-ai-s-leanstral-tackles-trust-in-code-generation"},{"title":"Leanstral: Mistral AI's Open-Source Agent for Formal Proofs | AIToolly","url":"https://aitoolly.com/ai-news/article/2026-03-17-leanstral-mistral-ais-open-source-agent-for-trustworthy-coding-and-formal-proof-engineering"},{"title":"Leanstral: Open-Source foundation for trustworthy vibe-coding | Mistral AI","url":"https://mistral.ai/news/leanstral"},{"title":"Leanstral: Mistral’s Open-Source Proof Agent for Lean 4","url":"https://rits.shanghai.nyu.edu/ai/leanstral-mistrals-open-source-proof-agent-for-lean-4/"},{"title":"Leanstral by Mistral AI: The AI That Proves Your Code Is Correct","url":"https://emelia.io/hub/leanstral-mistral-ai-formal-verification"},{"title":"Leanstral: How AI-Powered Formal Verification is Revolutionizing Trustworthy Code Generation | TechPlanet","url":"https://techplanet.today/post/leanstral-how-ai-powered-formal-verification-is-revolutionizing-trustworthy-code-generation"},{"title":"Leanstral - Mistral AI | Mistral Docs","url":"https://docs.mistral.ai/models/leanstral-26-03"},{"title":"Mistral's new agent proofs your code on the cheap","url":"https://www.theregister.com/2026/03/17/mistral_leanstral_ai_code_verification_tool/"},{"title":"Leanstral Review: Mistral Just Shipped the AI That Proves Your Code Is Correct | SaaS Pilot — AI & SaaS Tool Reviews","url":"https://saaspilot.org/ai-coding-assistants/2026-03-20-radar-2-leanstral-review/"}]

Based on the search results, here's what I found about Leanstral and its capabilities:

## Overview

Leanstral is an open-source code agent designed for Lean 4, built for formal proof engineering in realistic repositories. It has 119B parameters with 6.5B active.

## Key Capabilities

**Proof and Tactic Generation:**
Leanstral is designed to both carry out tasks and formally prove implementations against strict specifications. The model does not "guess" proofs: it builds them in dialogue with the verifier.

**Proof Search:**
Leanstral enables development teams to specify expected behavior in Lean 4, then automatically generate compliance proofs, which the compiler then verifies.

**Architecture:**
Rather than wrapping a generalist LLM around Lean's syntax, Mistral trained a specialized model to operate natively in realistic formal repositories, understanding Lean's type system, tactic language, and proof obligations from the ground up.

**Compiler Integration:**
The agent interacts directly with the Lean 4 compiler via the MCP (Model Context Protocol), and was specifically trained to achieve maximal performance with frequently used lean-lsp-mcp.

The tool represents a significant advancement in combining AI with formal verification to eliminate the need for manual human code review in high-stakes domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8104c62b-5bab-4a0d-bf8a-4c23e72b4827",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "a74c2781-ee03-4fe4-b117-e9922c0bb037",
  "sourceToolAssistantUUID": "8104c62b-5bab-4a0d-bf8a-4c23e72b4827",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-27T23:47:32.794Z_

<details><summary>↩ Tool result · `toolu_015Nu437iDNuUWPcyPCYAx1L`</summary>

```text
Web search results for query: ""M2F" "Math-to-Formal" framework LLM "deepseek" OR "o1" OR "GPT-4o" OR "sonnet" architecture 2025"

Links: [{"title":"The Ultimate Guide to DeepSeek Models","url":"https://www.inferless.com/learn/the-ultimate-guide-to-deepseek-models"},{"title":"2025: The year in LLMs","url":"https://simonwillison.net/2025/Dec/31/the-year-in-llms/"},{"title":"A comparison of DeepSeek and other LLMs","url":"https://arxiv.org/html/2502.03688v3"},{"title":"DeepSeek - Wikipedia","url":"https://en.wikipedia.org/wiki/DeepSeek"},{"title":"Analyzing LLM Architectural Advances: From GPT-1 to DeepSeek-R1 | by LM Po | Medium","url":"https://medium.com/@lmpo/analyzing-llm-architectural-advances-from-gpt-1-to-deepseek-v3-a33431910b3f"},{"title":"From Informal to Formal -- Incorporating and Evaluating LLMs on Natural Language Requirements to Verifiable Formal Proofs","url":"https://arxiv.org/pdf/2501.16207"},{"title":"DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models","url":"https://arxiv.org/html/2512.02556v1"},{"title":"Challenges and Applications of Large Language Models: A Comparison of GPT and DeepSeek family of models","url":"https://arxiv.org/pdf/2508.21377"},{"title":"DeepSeek is open-access and the next AI disrupter for radiology","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12363671/"}]

Based on my search results, I found information about recent LLM developments in 2025 involving the models you mentioned (DeepSeek, o1, GPT-4o, and Sonnet), but I did not find specific information about an "M2F" or "Math-to-Formal" framework in the search results.

However, here's what I found about the relevant models and their architectures in 2025:

**DeepSeek Models:**
DeepSeek-R1 was released on January 20, 2025, and rivals OpenAI's o1. DeepSeek-R1 is a flagship reasoning model that excels at solving math and reasoning problems.

**LLM Architecture Trends:**
Modern LLM architectures have evolved to include efficient attention mechanisms like Grouped-Query Attention (GQA) and Multi-Latent Attention (MLA), along with the adoption of sparse Mixture-of-Experts (MoE) architecture, which enables massive parameter increases without proportional rises in computational cost.

**Reasoning Models Development:**
OpenAI started the "reasoning" revolution in September 2024 with o1 and o1-mini, then expanded with o3, o3-mini and o4-mini in early 2025, with reasoning becoming a signature feature of models from nearly every major AI lab.

If you're looking for specific information about the "M2F" framework, you may need to provide additional context or search for more recent papers, as this specific framework name doesn't appear in the current search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d59cd41b-c8e8-486a-80df-cba68aeabea2",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "33035b83-05e2-40e9-96ca-c117c0b1f501",
  "sourceToolAssistantUUID": "d59cd41b-c8e8-486a-80df-cba68aeabea2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-27T23:47:37.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01StXJfk8uV1onKkmVoFDWcZ`</summary>

```json
{
  "query": "M2F autoformalization \"130k lines\" topology OR \"153k lines\" DeepSeek Claude model used"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33035b83-05e2-40e9-96ca-c117c0b1f501",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTy1gJzCRJoTxTbzeuA6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e8c4e84-c01e-458d-9da9-11b035c6e3d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNPYRZ1bAYnw5QWxRe5Bda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2616,
      "cache_read_input_tokens": 19268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2616,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
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

_source line 35 · 2026-05-27T23:47:38.324Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y9dhjqawjaGQ2N7xpgK7R4`</summary>

```json
{
  "query": "Leanstral \"autoformalization\" OR \"translate natural language\" OR \"informal to formal\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e8c4e84-c01e-458d-9da9-11b035c6e3d5",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTy1gJzCRJoTxTbzeuA6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edec3fde-ac5f-4aae-89bf-c40f445279c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JNPYRZ1bAYnw5QWxRe5Bda",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2616,
      "cache_read_input_tokens": 19268,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2616
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 19268,
          "cache_creation_input_tokens": 2616,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2616,
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

_source line 36 · 2026-05-27T23:47:44.860Z_

<details><summary>↩ Tool result · `toolu_01StXJfk8uV1onKkmVoFDWcZ`</summary>

```text
Web search results for query: "M2F autoformalization "130k lines" topology OR "153k lines" DeepSeek Claude model used"

Links: [{"title":"M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/pdf/2602.17016"},{"title":"[2601.03298] 130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/abs/2601.03298"},{"title":"130k Lines of Topology: LLM Autoformalization - YouTube","url":"https://www.youtube.com/watch?v=CpEftWkps9E"},{"title":"130k Lines: Rapid Autoformalization in Topology","url":"https://www.emergentmind.com/papers/2601.03298"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://www.researchgate.net/publication/399558972_130k_Lines_of_Formal_Topology_in_Two_Weeks_Simple_and_Cheap_Autoformalization_for_Everyone"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260103298U/abstract"},{"title":"130k Lines of Formal Topology: Simple and Cheap Autoformalization for Everyone? | Hacker News","url":"https://news.ycombinator.com/item?id=47240504"},{"title":"Munkres' General Topology Autoformalized in Isabelle/HOL","url":"https://arxiv.org/pdf/2604.07455"},{"title":"Automatic Textbook Formalization","url":"https://arxiv.org/pdf/2604.03071"},{"title":"Josef Urban","url":"https://www.catalyzex.com/author/Josef%20Urban"}]

I found relevant results for your search. Here are the key findings:

## 130k Lines of Formal Topology Project

This project autoformalized a large portion of the general topology from the Munkres textbook, with about 130k lines completed in two weeks (December 22 to January 4) for an LLM subscription cost of about $100. The LLM was instantiated as ChatGPT (mostly 5.2) or Claude Sonnet (4.5) run through the respective Codex or Claude Code command line interfaces.

## M2F Autoformalization Project

The M2F project converts long-form mathematical sources into a project-scale Lean library of 153,853 lines from 479 pages textbooks on real analysis and convex analysis, fully formalized as Lean declarations with accompanying proofs, completed in approximately three weeks.

## Claude 4.5 Opus Multi-Agent Formalization

A recent formalization comprised 130K lines of code and 5900 Lean declarations conducted within one week by a total of 30K Claude 4.5 Opus agents collaborating in parallel on a shared code base.

These projects demonstrate significant advances in autoformalization using different LLM models and approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e8c4e84-c01e-458d-9da9-11b035c6e3d5",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "be600801-3690-4f9a-9b9b-85dd9c3a3feb",
  "sourceToolAssistantUUID": "3e8c4e84-c01e-458d-9da9-11b035c6e3d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-27T23:47:46.010Z_

<details><summary>↩ Tool result · `toolu_01Y9dhjqawjaGQ2N7xpgK7R4`</summary>

```text
Web search results for query: "Leanstral "autoformalization" OR "translate natural language" OR "informal to formal""

Links: [{"title":"Autoformalization | Envisioning Vocab","url":"https://www.envisioning.com/vocab/autoformalization"},{"title":"Autoformalization: Bridging Informal and Formal Math","url":"https://www.emergentmind.com/topics/autoformalization"},{"title":"TOWARDS AUTOFORMALIZATION OF LLM-GENERATED OUTPUTS FOR REQUIREMENT VERIFICATION","url":"https://arxiv.org/pdf/2511.11829"},{"title":"Autoformalization with Backtranslation: Training an Automated Mathematician","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/JakobNordhagen.pdf"},{"title":"Towards a Common Framework for Autoformalization","url":"https://ojs.aaai.org/index.php/AAAI/article/download/42132/46093"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://arxiv.org/pdf/2507.08665"},{"title":"Autoformalization with Large Language Models","url":"https://www.emergentmind.com/topics/autoformalization-with-large-language-models"},{"title":"Autoformalization with Large Language Models","url":"https://arxiv.org/pdf/2205.12615"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/pdf/2603.24372"}]

Based on the web search results, here's what I found about autoformalization and related concepts:

## What is Autoformalization?

Autoformalization leverages natural language processing (NLP) and symbolic reasoning to interpret informal descriptions—such as those found in mathematical proofs or legal text—and translate them into rigorously formal statements. More specifically, autoformalization is the task of automatically translating informal mathematical content—typically written in human natural language or LaTeX—into formal statements or proofs in a machine-verifiable proof assistant language.

## Key Applications

This process aims to bridge the gap between human mathematical discourse and formal systems, undergirding advances in automated reasoning, formal verification, and large-scale mathematical knowledge management. The process underpins applications in automated theorem proving, formal verification, and the construction of reliable mathematical libraries.

## How It Works

This process typically involves mapping natural language semantics onto formal systems, such as predicate logic, type theory, or formal verification frameworks. Modern autoformalization systems are built as modular pipelines incorporating advanced neural models, rule-based systems, feedback-driven refinement, and formal verification stages.

## Challenges

A key challenge is the ambiguity and imprecision in natural language, which requires sophisticated models that can understand context, infer meaning, and correctly formalize assumptions and definitions.

**Note:** The search results did not contain specific information about a tool or system called "Leanstral" specifically. The results focus on autoformalization as a general field and mention tools like Lean4 as a formal language system used in autoformalization research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edec3fde-ac5f-4aae-89bf-c40f445279c9",
  "isSidechain": true,
  "promptId": "8d366d75-42a3-471e-a2e4-fe494eaf1bbb",
  "agentId": "a496200c6301f6ce4",
  "type": "user",
  "uuid": "d251d4ef-1522-4c1d-98c6-c9c4948d1751",
  "sourceToolAssistantUUID": "edec3fde-ac5f-4aae-89bf-c40f445279c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-27T23:48:33.050Z_

Based on my extensive research across multiple searches, here are the detailed findings:

---

## 1. Leanstral: Proof Generation/Tactic Agent, NOT Autoformalization

**Leanstral is a proof generation and formal verification agent, not an autoformalization system.** Released by Mistral AI on March 16, 2026, it is specifically designed to:

- Generate code AND machine-checkable mathematical proofs that the code is correct
- Operate natively in Lean 4 repositories, understanding Lean's type system, tactic language, and proof obligations
- Build proofs in dialogue with the Lean 4 compiler/verifier (via MCP - Model Context Protocol)
- Verify software correctness, not translate informal math into formal Lean

**Key technical details:**
- Sparse Mixture-of-Experts (MoE) architecture: 119-120B total parameters, ~6.5B active per token
- Benchmarked on FLTEval (Formal Logic Test Evaluation): 26.3 at pass@2, beating Claude Sonnet (23.7)
- Cost: ~$36 vs $549 for Claude Sonnet on the same task
- Apache 2.0 license, free API endpoint at `labs-leanstral-2603`
- Trained specifically for formal proof engineering in realistic repositories

**It does NOT do autoformalization** (translating natural language math into formal Lean). It takes specifications already expressed formally and generates proofs/verified code. No search results show Leanstral being used for informal-to-formal math translation.

---

## 2. M2F and the "130k Lines" Project: LLM Backbones Used

### M2F (Math-to-Formal) - arxiv 2602.17016
M2F is an agentic framework for end-to-end, project-scale autoformalization in Lean. It produced 153,853 lines of formalized Lean from 479 pages of textbooks on real analysis and convex analysis in ~3 weeks. On FATE-H benchmark: 96% solved fully automatically, 97% with a 31-declaration lemma map.

**The specific LLM backbone used by M2F was not clearly identified in the search results.** The paper's abstract focuses on the two-stage architecture (statement compilation + proof repair) rather than specifying the underlying model. However, it notably found errors that GPT-5.2 Pro missed, suggesting it may use a different or fine-tuned model.

### "130k Lines of Formal Topology" Project (arxiv 2601.03298)
A closely related project (often confused with M2F) autoformalized Munkres' general topology textbook into ~130k lines in two weeks for ~$100. This project explicitly used:
- **ChatGPT (mostly GPT-5.2)** 
- **Claude Sonnet (4.5)**
- Run through Codex CLI or Claude Code command line interfaces

### Meta FAIR
I did not find a specific 2025-2026 Meta FAIR autoformalization system in the search results. The major autoformalization systems identified are academic/startup efforts rather than Meta FAIR specifically.

---

## 3. Current Best Models for Autoformalization (informal math to formal Lean 4) as of 2026

### Specialized Autoformalization Models (Best Performance):

1. **StepFun-Formalizer-32B** - State-of-the-art single-shot formalization:
   - 40.5% on FormalMATH-Lite
   - 26.7% on ProverBench
   - Surpasses all prior general-purpose and specialized models at comparable scale
   - Uses knowledge-reasoning fusion: formal knowledge distillation (183K Lean4-aligned pairs) + template-guided reasoning trajectories (5.8K trajectories from Claude 3.7)

2. **Kimina-Autoformalizer-7B** - Previous best before StepFun-Formalizer; serves as formal knowledge source for StepFun

3. **ProofBridge** (ICLR 2026) - Translates NL theorems AND proofs into Lean 4:
   - Uses joint NL/FL embeddings for cross-modal retrieval
   - Fine-tunes Kimina-Prover-RL-1.7B for NL-to-Lean 4 translation
   - Iterative proof repair with Lean compiler feedback

### General-Purpose LLMs Used for Autoformalization:

4. **GPT-5.2** (via ChatGPT/Codex CLI) - Used in the 130k lines topology project
5. **Claude 4.5 Opus** - Used multi-agent (30K agents) to produce 130K lines / 5900 Lean declarations in one week
6. **Claude Sonnet 4.5** - Used alongside GPT-5.2 in the topology project
7. **DeepSeek-Prover series** - Used for formalizing Lean corpora for expert iteration

### Key Insight:
The current state-of-the-art on ProofNet benchmark (undergraduate-level problems) is only **31.28%**, showing autoformalization remains extremely challenging. The best specialized model (StepFun-Formalizer-32B) achieves 40.5% on FormalMATH-Lite. The field is still far from solved.

---

## Summary Table

| System | Type | Task | LLM Backbone |
|--------|------|------|--------------|
| Leanstral | Proof agent | Code verification + proof generation | Custom Mistral MoE (119B/6.5B active) |
| M2F | Agentic framework | Project-scale autoformalization | Not publicly specified |
| 130k Topology | Pipeline | Textbook autoformalization | GPT-5.2 + Claude Sonnet 4.5 |
| StepFun-Formalizer | Specialized model | Statement autoformalization | Custom 7B/32B (trained with Claude 3.7 trajectories) |
| ProofBridge | Framework | NL theorem+proof to Lean 4 | Kimina-Prover-RL-1.7B (fine-tuned) |

---

Sources:
- [Leanstral: Open-Source foundation for trustworthy vibe-coding | Mistral AI](https://mistral.ai/news/leanstral)
- [Leanstral - Mistral Docs](https://docs.mistral.ai/models/leanstral-26-03)
- [Leanstral Outperforms Claude Sonnet at Formal Code Proofs | Awesome Agents](https://awesomeagents.ai/news/leanstral-mistral-lean4-proof-agent/)
- [M2F: Automated Formalization of Mathematical Literature at Scale (arxiv 2602.17016)](https://arxiv.org/abs/2602.17016)
- [130k Lines of Formal Topology in Two Weeks (arxiv 2601.03298)](https://arxiv.org/abs/2601.03298)
- [StepFun-Formalizer: Unlocking the Autoformalization Potential (arxiv 2508.04440)](https://www.arxiv.org/pdf/2508.04440)
- [StepFun-Formalizer-32B on HuggingFace](https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B)
- [ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)](https://arxiv.org/pdf/2510.15681)
- [ProofBridge GitHub](https://github.com/PrithwishJana/ProofBridge)
- [Autoformalization in the Era of Large Language Models: A Survey](https://arxiv.org/html/2505.23486v1)
- [Formal Reasoning Meets LLMs - Communications of the ACM](https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/)
- [The Register: Mistral's new agent proofs your code on the cheap](https://www.theregister.com/2026/03/17/mistral_leanstral_ai_code_verification_tool/)
- [Mistral Leanstral: AI That Proves Its Own Code](https://aiautomationglobal.com/blog/mistral-leanstral-formal-code-verification-2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d251d4ef-1522-4c1d-98c6-c9c4948d1751",
  "isSidechain": true,
  "agentId": "a496200c6301f6ce4",
  "requestId": "req_011CbTy2eojRH7vRQHN11RGk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3673beca-c67b-419c-b00e-2c8b4b807dbd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1f70fc8-7847-473d-8939-9661ba1529dd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LYSYPJzHXRQyzudchpCvMc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1757,
      "cache_read_input_tokens": 21884,
      "output_tokens": 2079,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1757
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2079,
          "cache_read_input_tokens": 21884,
          "cache_creation_input_tokens": 1757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1757,
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
