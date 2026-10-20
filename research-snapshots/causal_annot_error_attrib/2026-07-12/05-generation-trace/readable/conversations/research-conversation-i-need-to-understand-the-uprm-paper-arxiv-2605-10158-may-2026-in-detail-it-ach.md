# Research conversation: I need to understand the uPRM paper (arXiv 2605.10158, May 2026) in detail. It achieves up to 15% improvement over LLM-a

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-abad40be346c30ee3.jsonl`
- **Structured JSON:** [`c212d167bfd3ddacf535.json`](../../sessions/c2/c212d167bfd3ddacf535.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-28T01:52:40.406Z_

I need to understand the uPRM paper (arXiv 2605.10158, May 2026) in detail. It achieves up to 15% improvement over LLM-as-Judge on ProcessBench without any supervision, challenging the need for MC-based annotation entirely.

Please search for and read this paper. I need:
1. Full title and authors
2. What is uPRM's method? How does it work without supervision?
3. Exact results on ProcessBench - what F1 scores does it achieve on which subsets?
4. How does it compare to supervised/MC-based PRMs?
5. What are its limitations?
6. Does it truly challenge the need for MC estimation, or are there caveats?

Try searches: "uPRM unsupervised process reward model 2026", "arXiv 2605.10158", "uPRM ProcessBench". Also try fetching https://arxiv.org/abs/2605.10158

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "abad40be346c30ee3",
  "type": "user",
  "uuid": "8345a4c0-2112-4721-b2b4-6785cb8b4826",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T01:52:40.411Z_

```json
{
  "parentUuid": "8345a4c0-2112-4721-b2b4-6785cb8b4826",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "c9d92d07-8a8e-4fc1-b5dc-d3b99aaa1b2c",
  "timestamp": "2026-05-28T01:52:40.411Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T01:52:40.413Z_

```json
{
  "parentUuid": "c9d92d07-8a8e-4fc1-b5dc-d3b99aaa1b2c",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c169bf19-ad22-44c9-994d-7cd06af890d6",
  "timestamp": "2026-05-28T01:52:40.413Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T01:52:42.994Z_



I'll search for this paper using multiple approaches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c169bf19-ad22-44c9-994d-7cd06af890d6",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8Z6dspqkCjDMyMmMe2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a27359ff-c4cc-49cf-bf0e-96bcb2247eca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGAzD9r5n6QzruC33fX1xD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1534,
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

_source line 5 · 2026-05-28T01:52:43.387Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NUDBgiVCNeUookqeCT5G27`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a27359ff-c4cc-49cf-bf0e-96bcb2247eca",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8Z6dspqkCjDMyMmMe2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be1d9790-d5d8-4621-8bde-75f394852ba9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGAzD9r5n6QzruC33fX1xD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 7411,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1534
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1534,
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

_source line 6 · 2026-05-28T01:52:43.390Z_

<details><summary>↩ Tool result · `toolu_01NUDBgiVCNeUookqeCT5G27`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parentUuid": "be1d9790-d5d8-4621-8bde-75f394852ba9",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "abad40be346c30ee3",
  "type": "user",
  "uuid": "e0bd62f9-b2c7-4faf-9522-c12078d2410d",
  "sourceToolAssistantUUID": "be1d9790-d5d8-4621-8bde-75f394852ba9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T01:52:47.321Z_



Now let me search for the paper and try to fetch it directly from arXiv in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0bd62f9-b2c7-4faf-9522-c12078d2410d",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8ZKbF3VnbN7g3oWnbT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55898811-7282-4fc0-be00-bd8ee49f5676",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qGNr5rEuRFbNTWGNq18bz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 8 · 2026-05-28T01:52:48.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TTMWLVGkTFPvT548sxBDXx`</summary>

```json
{
  "query": "uPRM unsupervised process reward model 2026 arXiv 2605.10158"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55898811-7282-4fc0-be00-bd8ee49f5676",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8ZKbF3VnbN7g3oWnbT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7165284f-bfb6-4a59-ae25-b257cc003cc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qGNr5rEuRFbNTWGNq18bz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 9 · 2026-05-28T01:52:49.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MedX8UWSMSpC5HAojopZyH`</summary>

```json
{
  "query": "uPRM ProcessBench unsupervised process reward model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7165284f-bfb6-4a59-ae25-b257cc003cc3",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8ZKbF3VnbN7g3oWnbT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a84ff5bb-5b58-4317-a5fa-0cae58244220",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qGNr5rEuRFbNTWGNq18bz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 10 · 2026-05-28T01:52:50.323Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011GSekeVGZjsaDcQuFZCbmZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.10158",
  "prompt": "Extract the full title, all authors, and the complete abstract of this paper. Also extract any key details about the method, results, and contributions mentioned on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a84ff5bb-5b58-4317-a5fa-0cae58244220",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8ZKbF3VnbN7g3oWnbT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48e2eecf-6728-4261-8103-c5d75bd69b30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qGNr5rEuRFbNTWGNq18bz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 8945,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 244,
          "cache_read_input_tokens": 8945,
          "cache_creation_input_tokens": 1115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1115,
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

_source line 11 · 2026-05-28T01:52:55.803Z_

<details><summary>↩ Tool result · `toolu_011GSekeVGZjsaDcQuFZCbmZ`</summary>

```text
# Paper Summary: Unsupervised Process Reward Models

**Full Title:** Unsupervised Process Reward Models

**Authors:**
- Artyom Gadetsky
- Maxim Kodryan
- Siba Smarak Panigrahi
- Hang Guo
- Maria Brbic

**Abstract:**
The researchers present a novel approach to training process reward models without human supervision. Their method "requires no human supervision, neither at the level of step-by-step annotations nor through ground-truth verification of final answers." The core innovation involves using a scoring function derived from language model token probabilities to evaluate candidate positions of erroneous steps across multiple reasoning trajectories.

## Key Findings & Contributions

**Performance Results:**
- Achieved up to 15% absolute accuracy improvements over LLM-as-a-Judge in identifying erroneous steps on ProcessBench
- Functioned comparably to supervised models when used as a test-time verifier
- Outperformed majority voting by up to 6.9%
- Enabled "more robust policy optimization throughout training" when used as a reinforcement learning reward signal

**Significance:**
The work addresses scalability challenges in reward modeling by eliminating the need for expensive expert annotations, opening pathways toward "scalable reward modeling for complex reasoning tasks."

**Submission Details:**
- arXiv ID: 2605.10158
- Category: Machine Learning (cs.LG)
- Submitted: May 11, 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48e2eecf-6728-4261-8103-c5d75bd69b30",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "abad40be346c30ee3",
  "type": "user",
  "uuid": "a6cb5f54-1c10-4920-888a-694bc2f21fff",
  "sourceToolAssistantUUID": "48e2eecf-6728-4261-8103-c5d75bd69b30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T01:52:56.350Z_

<details><summary>↩ Tool result · `toolu_01MedX8UWSMSpC5HAojopZyH`</summary>

```text
Web search results for query: "uPRM ProcessBench unsupervised process reward model 2026"

Links: [{"title":"[2605.10158v1] Unsupervised Process Reward Models","url":"https://arxiv.org/abs/2605.10158v1"},{"title":"[2605.10158] Unsupervised Process Reward Models","url":"https://arxiv.org/abs/2605.10158"},{"title":"Unsupervised Process Reward Models","url":"https://arxiv.org/html/2605.10158"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/pdf/2503.22233"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"Efficient Process Reward Model Training via Active Learning","url":"https://arxiv.org/pdf/2504.10559"},{"title":"Uncertainty-Based Methods for Automated Process Reward Data Construction and Output Aggregation in Mathematical Reasoning","url":"https://arxiv.org/pdf/2508.01773"}]

Based on the search results, I found relevant information about uPRM and ProcessBench:

## Summary of Findings

uPRM is a method for training unsupervised Process Reward Models that requires no human supervision, neither at the level of step-by-step annotations nor through ground-truth verification of final answers. The approach defines a scoring function derived from LLM next-token probabilities that jointly assesses candidate positions of first erroneous steps across a batch of reasoning trajectories.

### Performance Results

uPRM achieves up to 15% absolute accuracy improvements over the LLM-as-a-Judge in identifying first erroneous steps on the ProcessBench dataset, performs comparably to supervised PRMs as a verifier for test-time scaling while outperforming the majority voting baseline by up to 6.9%, and when used as a reward signal in reinforcement learning, enables more robust policy optimization throughout training compared to a supervised PRM trained using ground-truth labels.

The research paper appears to have been published recently (about 2 weeks ago from the search date) and addresses the key problem that PRMs require expert annotations for every reasoning step, making them costly and difficult to scale.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a84ff5bb-5b58-4317-a5fa-0cae58244220",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "abad40be346c30ee3",
  "type": "user",
  "uuid": "53c7a21e-fae6-4c63-a97e-60b8be80794d",
  "sourceToolAssistantUUID": "a84ff5bb-5b58-4317-a5fa-0cae58244220",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T01:52:56.948Z_

<details><summary>↩ Tool result · `toolu_01TTMWLVGkTFPvT548sxBDXx`</summary>

```text
Web search results for query: "uPRM unsupervised process reward model 2026 arXiv 2605.10158"

Links: [{"title":"[2605.10158v1] Unsupervised Process Reward Models","url":"https://arxiv.org/abs/2605.10158v1"},{"title":"[2605.10158] Unsupervised Process Reward Models","url":"https://arxiv.org/abs/2605.10158"},{"title":"Unsupervised Process Reward Models","url":"https://arxiv.org/html/2605.10158"},{"title":"More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/pdf/2503.22233"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Uncertainty-Based Methods for Automated Process Reward Data Construction and Output Aggregation in Mathematical Reasoning","url":"https://arxiv.org/pdf/2508.01773"},{"title":"Entropy-Regularized Process Reward Model","url":"https://arxiv.org/pdf/2412.11006"}]

Based on the search results, here's what I found about the uPRM (Unsupervised Process Reward Model) paper:

## Overview
Process Reward Models (PRMs) are a powerful mechanism for steering large language model reasoning by providing fine-grained, step-level supervision. However, this effectiveness comes at a significant cost: PRMs require expert annotations for every reasoning step, making them costly and difficult to scale.

## The uPRM Approach
The paper proposes a method for training unsupervised PRMs (uPRM) that requires no human supervision, neither at the level of step-by-step annotations nor through ground-truth verification of final answers. The key idea behind the approach is to define a scoring function, derived from LLM next-token probabilities, that jointly assesses candidate positions of first erroneous steps across a batch of reasoning trajectories.

## Results
The paper demonstrates effectiveness across diverse scenarios: (i) uPRM achieves up to 15% absolute accuracy improvements over the LLM-as-a-Judge in identifying first erroneous steps on the ProcessBench dataset; (ii) as a verifier for test-time scaling, uPRM performs comparably to supervised PRMs and outperforms the majority voting baseline by up to 6.9%, and (iii) when used as a reward signal in reinforcement learning, uPRM enables more robust policy optimization throughout training compared to a supervised PRM trained using ground-truth labels.

The paper was submitted to arXiv on May 11, 2026, by researchers from EPFL including Artyom Gadetsky, Maxim Kodryan, Siba Smarak Panigrahi, Hang Guo, and Maria Brbic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7165284f-bfb6-4a59-ae25-b257cc003cc3",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "abad40be346c30ee3",
  "type": "user",
  "uuid": "ef940890-a822-4b75-9276-ba173ce0b016",
  "sourceToolAssistantUUID": "7165284f-bfb6-4a59-ae25-b257cc003cc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-28T01:53:00.503Z_

Good, I have the basic details. Now let me fetch the full HTML version of the paper to get the detailed methodology, exact results tables, limitations, and deeper analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef940890-a822-4b75-9276-ba173ce0b016",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8aKJuNeTGgtmRFoBuX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66f98b15-33bf-4af5-b4dd-ccf0c3905ad9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgiTjt4sEStvScuD1wzeRk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1003,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 10060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 986,
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

_source line 15 · 2026-05-28T01:53:05.934Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UJjV8YCczwFMygSRsxQpQS`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.10158",
  "prompt": "Extract ALL of the following in full detail:\n\n1. The complete methodology section - how does the uPRM scoring function work? What is the mathematical formulation? How does it use next-token probabilities? What is the joint assessment across batches?\n\n2. ALL results tables, especially on ProcessBench - extract exact F1 scores or accuracy numbers for each subset (e.g., GSM8K, MATH, AIME, Olympiad). Include numbers for all baselines (LLM-as-Judge, supervised PRMs, MC-based methods, majority voting).\n\n3. The limitations section - what do the authors identify as limitations?\n\n4. Any discussion of how uPRM compares to Monte Carlo (MC) based annotation methods.\n\n5. Any ablation studies or analysis of when the method fails.\n\n6. The test-time scaling results and RL results with exact numbers.\n\nPlease be as detailed and precise as possible with all numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66f98b15-33bf-4af5-b4dd-ccf0c3905ad9",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8aKJuNeTGgtmRFoBuX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21f3236b-3d1f-48b8-a4b3-5fbcfc83db07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgiTjt4sEStvScuD1wzeRk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1003,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 10060,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 986
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1003,
          "output_tokens": 326,
          "cache_read_input_tokens": 10060,
          "cache_creation_input_tokens": 986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 986,
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

_source line 16 · 2026-05-28T01:53:32.737Z_

<details><summary>↩ Tool result · `toolu_01UJjV8YCczwFMygSRsxQpQS`</summary>

```text
# Comprehensive Summary of Unsupervised Process Reward Models

## 1. Methodology: uPRM Scoring Function

### Core Scoring Mechanism

The uPRM uses LLM next-token probabilities to assess error positions without human labels. For a trajectory τ=(x,y₁,...,yₜ) and candidate error position j, the method constructs sequences interleaving steps with correctness markers:

**Single trajectory scoring:** The approach marks steps y₁,...,yⱼ₋₁ as correct (+) and step yⱼ as incorrect (-), creating sequence s(τ,j)=[x, y₁, +, ..., yⱼ₋₁, +, yⱼ, -]. The scoring function extracts LLM probabilities:

𝒮(j;s) = 𝟙[j≤T]·log pⱼ⁻ + Σₜ<ⱼ log pₜ⁺

where pₜ⁺ and pₜ⁻ represent next-token probabilities for "+" and "-" labels.

**Joint multi-trajectory assessment:** Trajectories are concatenated sequentially, leveraging in-context learning. For N trajectories with positions j₁,...,jₙ:

𝒮(j₁:ₙ;s₁:ₙ) = (1/N)Σₙ₌₁ᴺ [𝟙[jₙ≤Tₙ]·log pₙ,ⱼₙ⁻ + Σₜ<ⱼₙ log pₙ,ₜ⁺]

This captures in-context learning effects, though the authors identify and correct a "degenerate solution" problem where all trajectories converge to identical labels (discussed in Appendix A).

### Training Objective

The PRM is trained via reinforcement learning to optimize the joint score with entropy regularization:

max θ 𝔼[𝔼ⱼₙ~pθ(·|τₙ)[𝒮(j₁:ₙ)] + (γ/N)Σₙℍ(pθ(·|τₙ))]

where γ controls exploration-exploitation tradeoff (set to 3 based on ablations). The architecture applies LoRA to Qwen2.5-14B-Instruct, with an MLP head extracting binary correctness logits from hidden states at special tokens inserted between reasoning steps.

---

## 2. Results Tables

### ProcessBench Results (Table 1: F1 Scores)

| Dataset | LLM-as-Judge | uPRM |
|---------|--------------|------|
| GSM8K | 49.8 | 58.3 |
| MATH | 42.8 | 52.6 |
| OlympiadBench | 29.4 | 42.7 |
| Omni-MATH | 26.6 | 39.8 |

uPRM achieves 13-15% absolute improvements, with largest gains on challenging datasets. The authors note that "strong downstream utility does not require perfect localization of erroneous steps."

### Test-Time Scaling: Best-of-8 Results (Table 2)

Comparison on Qwen2.5-Math-7B with 8 generations:

| Model | MATH-500 | Minerva | OlympiadBench | Average |
|-------|----------|---------|---------------|---------|
| pass@8 (upper bound) | 91.5±0.4 | 55.5±0.3 | 60.3±0.8 | 69.1 |
| Math-Shepherd-PRM-7B | 86.8±0.9 | 47.3±1.2 | 47.1±0.1 | 60.4 |
| Qwen2.5-Math-PRM-7B | 87.0±0.9 | 47.2±0.2 | 47.7±0.4 | 60.6 |
| sPRM (supervised) | 86.3±1.1 | 46.7±0.6 | 47.1±0.1 | 60.0 |
| uPRM (ours) | 86.5±0.5 | 46.7±2.2 | 47.1±0.4 | 60.1 |

uPRM matches supervised methods despite no human annotations. For smaller models with 256 generations, uPRM outperforms majority voting by 6.9% absolute (Llama-3.2-1B) and 4.4% (Qwen2.5-1.5B).

### Reinforcement Learning Results (Table 3)

Training on hard MATH problems (levels 3-5):

| Model | Reward | MATH-500 | Minerva | OlympiadBench |
|-------|--------|----------|---------|---------------|
| Qwen2.5-Math-7B | VR only | 80.1±0.8 | 35.9±0.4 | 41.8±0.4 |
| | uPRM | 82.9±0.4 | 37.9±1.0 | 42.1±1.3 |
| | uPRM + VR | 82.1±1.3 | 36.3±2.2 | 43.8±0.2 |
| Qwen2.5-Math-1.5B | VR only | 70.0±0.4 | 26.0±0.2 | 33.5±1.0 |
| | sPRM† | 74.7±0.3 | 27.8±0.6 | 35.0±1.0 |
| | uPRM | 73.5±1.2 | 31.8±0.8 | 36.6±0.6 |

uPRM achieves 4% improvement for Math-1.5B vs. verifiable outcome reward alone. Critically, "uPRM supports more robust policy optimization across training runs" compared to supervised PRMs, showing resistance to reward hacking despite conventional wisdom suggesting it's inevitable.

---

## 3. Limitations Section

The authors identify several constraints:

- **Base model requirements:** Joint scoring demands LLMs with sufficient context length to process concatenated trajectory batches and capability for meaningful correctness judgments. This "limits the choice of base models," though the authors propose decoupling scoring LLMs from PRM backbones as mitigation.

- **Open research question:** While observing superior robustness to reward hacking compared to supervised PRMs, "fully characterizing its precise origin is an important next step."

- **Incomplete proxy:** The authors acknowledge that "direct accuracy of a reward model is an incomplete proxy for downstream utility," citing recent work showing highly accurate models aren't necessarily effective teachers.

---

## 4. Comparison to Monte Carlo Methods

The paper addresses MC-based annotation in related work. Traditional approaches like Math-Shepherd use "brute-force Monte Carlo estimations" or "credit assignment from ground truth final answers," requiring computational resources "that limits their general applicability." 

The uPRM approach is positioned as fully unsupervised—requiring "neither step-level annotations nor ground-truth verification of final answers," distinguishing it from MC methods that "still rely heavily on the availability of ground truth answers in the data."

---

## 5. Ablation Studies and Failure Analysis

### Entropy Regularization (Figure D1)
Testing γ ∈ {1, 3, 9}:
- γ=1: Entropy collapses by iteration 400, suggesting overfitting
- γ=3: Gradual entropy decrease balancing exploration/exploitation
- γ=9: Entropy remains near-uniform, insufficient learning signal

### Degenerate Solutions (Appendix A)
The joint score exhibits pathological behavior where all trajectories converge to j=1 (first step erroneous) or j=Tₙ+1 (no errors). The authors introduce a correction term with budget parameter ρ=0.25, preventing degenerate collapse when >75% of predictions assign corner positions. Figure A1 shows correction robustness across ρ values.

### Reward Hacking Analysis (Section D.3.1)
Notably, supervised PRM with ground-truth labels shows "rapid reward hacking" (collapse <50 iterations for Qwen-7B), whereas uPRM "supports more robust policy optimization throughout training" with "no signs of reward hacking" observed during full training of Math models. The mechanism remains incompletely characterized—the authors hypothesize self-training properties provide regularization against spurious reward maximization patterns.

### Aggregation Strategy (Table C1)
Best-of-8 ablation comparing last vs. product scoring across models shows marginal differences, with last slightly preferred for uPRM.

---

## 6. Test-Time Scaling and RL Results (Summary)

**Scaling patterns:** Figure 1 demonstrates consistent improvements scaling from 1 to 256 generations. Smaller models (1B-1.5B) show strongest gains—Llama-3.2-1B improves 17.1 percentage points (14.6% → 31.7% average accuracy). Larger models show weaker improvements due to stronger majority voting baselines. DVTS outperforms Best-of-N for smaller models but underperforms for larger ones.

**RL robustness:** The critical finding is uPRM's apparent resistance to reward hacking. While Cheng et al. argue hacking is "inevitable when relying solely on PRM rewards," training with uPRM alone successfully completes without collapse, yielding superior final performance compared to outcome-only rewards (+4% for 1.5B model on average benchmarks).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21f3236b-3d1f-48b8-a4b3-5fbcfc83db07",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "abad40be346c30ee3",
  "type": "user",
  "uuid": "119977fa-2545-48a5-8d5a-e5ddc424e55b",
  "sourceToolAssistantUUID": "21f3236b-3d1f-48b8-a4b3-5fbcfc83db07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-28T01:53:36.315Z_

Excellent -- I now have comprehensive details. Let me also fetch the paper to check for any additional details on the comparison with MC-based PRMs and to verify the F1 score numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "119977fa-2545-48a5-8d5a-e5ddc424e55b",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8cxMujTFQnL1ToTYiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a14b351a-6dd6-4516-94ae-1a988fcb323c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C8ZMDR2zp5HC6b3Q2xCos",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3725,
      "cache_read_input_tokens": 11046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3725,
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

_source line 18 · 2026-05-28T01:53:42.348Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014EBUGkGyckRXsbJNxP9F3Z`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.10158",
  "prompt": "Focus on extracting:\n\n1. The exact ProcessBench F1 scores for ALL methods compared in Table 1, not just LLM-as-Judge and uPRM. Are there MC-based PRMs, supervised PRMs, or other baselines shown? What about Qwen2.5-Math-PRM, Math-Shepherd, or any other method?\n\n2. Is the 15% improvement referring to F1 or accuracy? On which specific subset?\n\n3. Any discussion about whether uPRM truly challenges or replaces MC-based annotation - does the paper make strong claims or hedged claims?\n\n4. The exact training setup - what LLM is used for scoring, what model is the PRM backbone, what datasets are used for training?\n\n5. Any comparison showing where MC-based PRMs are still better than uPRM?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a14b351a-6dd6-4516-94ae-1a988fcb323c",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8cxMujTFQnL1ToTYiw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f774ae3-b337-44ed-bab4-0a28b209ef74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016C8ZMDR2zp5HC6b3Q2xCos",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3725,
      "cache_read_input_tokens": 11046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3725,
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

_source line 19 · 2026-05-28T01:53:50.814Z_

<details><summary>↩ Tool result · `toolu_014EBUGkGyckRXsbJNxP9F3Z`</summary>

```text
# Key Findings from "Unsupervised Process Reward Models"

## 1. ProcessBench Results (Table 1)

The paper only compares **two methods** on ProcessBench:
- **LLM-as-a-Judge**: 49.8 (GSM8K), 42.8 (MATH), 29.4 (OlympiadBench), 26.6 (Omni-MATH)
- **uPRM**: 58.3, 52.6, 42.7, 39.8 (same datasets, F1 scores)

No other PRMs are benchmarked on ProcessBench. The complete table appears only in appendix Table D1, but the main text provides no comparison to MC-based or supervised alternatives on this benchmark.

## 2. The 15% Improvement Claim

The improvement is measured in **F1 score**, specifically: "uPRM achieves up to 15% absolute accuracy improvements over the LLM-as-a-Judge" occurs on "the most challenging datasets such as OlympiadBench...and Omni-Math." The 13% gains mentioned are the largest improvements demonstrated.

## 3. Claims About MC-Based Annotation

The paper makes **hedged claims**. It states: "our approach eliminates this requirement entirely, training PRMs without any supervision at either step-level annotations or outcome labels." However, regarding prior MC-based methods, the authors note they "still rely heavily on the availability of ground truth answers in the data or access to external verifiers, and are often highly computationally demanding." The framing suggests superiority through elimination of *all* supervision rather than direct empirical replacement claims.

## 4. Training Setup

- **Scoring LLM**: Qwen2.5-14B-Instruct
- **PRM Backbone**: Same Qwen2.5-14B-Instruct with LoRA adapters
- **Training Data**: PRM800K dataset (reasoning trajectories only, no labels used)
- **Key Detail**: "Qwen2.5-14B-Instruct's post-training didn't involve training on any step-level correctness labels"

## 5. Where MC-Based Methods Remain Superior

The paper provides **no direct comparison** against MC-based PRMs. The closest proxy appears in Table 2 (test-time scaling), where uPRM achieves 60.1 average accuracy versus supervised baselines around 60.0-60.8. The authors note their uPRM is "competitive with various supervised PRMs" but don't isolate MC-annotation-derived PRMs for head-to-head comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f774ae3-b337-44ed-bab4-0a28b209ef74",
  "isSidechain": true,
  "promptId": "bf18714b-0e92-4a91-be0e-dc43bfe729a9",
  "agentId": "abad40be346c30ee3",
  "type": "user",
  "uuid": "3a9a8bc5-9496-4b22-bc41-81d88cc8cc3f",
  "sourceToolAssistantUUID": "5f774ae3-b337-44ed-bab4-0a28b209ef74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-28T01:54:36.283Z_

Now I have a thorough understanding of the paper. Here is my detailed analysis:

---

## Paper: "Unsupervised Process Reward Models" (arXiv 2605.10158)

### 1. Full Title and Authors

**Title:** Unsupervised Process Reward Models

**Authors:** Artyom Gadetsky, Maxim Kodryan, Siba Smarak Panigrahi, Hang Guo, and Maria Brbic (all from EPFL)

**Submitted:** May 11, 2026

---

### 2. Method: How uPRM Works Without Supervision

The core idea is to define a scoring function based on LLM next-token probabilities that evaluates where the first error occurs in a reasoning trajectory, without any human labels.

**Step-level scoring:** Given a trajectory `τ = (x, y₁, ..., yₜ)` and a candidate error position `j`, the method constructs a sequence that marks steps `y₁, ..., y_{j-1}` as correct (with a "+" token) and step `y_j` as incorrect (with a "-" token). The score is:

```
S(j; s) = 1[j ≤ T] · log p_j⁻ + Σ_{t<j} log p_t⁺
```

where `p_t⁺` and `p_t⁻` are the LLM's next-token probabilities for the "+" and "-" tokens respectively. This leverages the LLM's internalized understanding of mathematical reasoning correctness.

**Joint multi-trajectory scoring:** Multiple trajectories are concatenated into a single context, enabling in-context learning effects. For N trajectories with candidate error positions `j₁, ..., j_N`, the joint score is the average of individual scores computed with the full concatenated context.

**Training the PRM:** A PRM (Qwen2.5-14B-Instruct with LoRA adapters and an MLP head) is trained via reinforcement learning to optimize this joint score, with entropy regularization (γ = 3) to prevent collapse. The training uses PRM800K trajectories but discards all labels.

**Degenerate solution fix:** The authors identified a pathological failure mode where all trajectories converge to `j = 1` (everything wrong) or `j = T+1` (everything right). They introduce a correction term with a budget parameter `ρ = 0.25` that penalizes predictions when more than 75% assign these corner positions.

**Scoring LLM:** Qwen2.5-14B-Instruct (whose post-training did not involve step-level correctness labels).

---

### 3. Exact Results on ProcessBench (F1 Scores)

| Dataset | LLM-as-Judge (F1) | uPRM (F1) | Improvement |
|---------|-------------------|-----------|-------------|
| GSM8K | 49.8 | 58.3 | +8.5 |
| MATH | 42.8 | 52.6 | +9.8 |
| OlympiadBench | 29.4 | 42.7 | +13.3 |
| Omni-MATH | 26.6 | 39.8 | +13.2 |

The "up to 15%" claim in the abstract refers to these F1 improvements, with the largest gains (~13 points) on the hardest subsets (OlympiadBench and Omni-MATH). Notably, the paper only compares against LLM-as-Judge on ProcessBench -- no supervised or MC-based PRMs are benchmarked on this task.

---

### 4. Comparison to Supervised/MC-Based PRMs

**Test-time scaling (Best-of-8, Table 2):**

| Method | MATH-500 | Minerva | OlympiadBench | Average |
|--------|----------|---------|---------------|---------|
| pass@8 (upper bound) | 91.5 | 55.5 | 60.3 | 69.1 |
| Math-Shepherd-PRM-7B | 86.8 | 47.3 | 47.1 | 60.4 |
| Qwen2.5-Math-PRM-7B | 87.0 | 47.2 | 47.7 | 60.6 |
| sPRM (supervised) | 86.3 | 46.7 | 47.1 | 60.0 |
| **uPRM (unsupervised)** | 86.5 | 46.7 | 47.1 | 60.1 |

uPRM is essentially on par with supervised PRMs in Best-of-8 verification. For smaller models with 256 generations, uPRM outperforms majority voting by up to 6.9% (Llama-3.2-1B).

**RL training (Table 3):** uPRM as a reward signal achieves +4% over verifiable-reward-only training for Qwen2.5-Math-1.5B. Critically, uPRM shows resistance to reward hacking, while the supervised PRM collapses in under 50 iterations for Qwen-7B.

---

### 5. Limitations (Identified by Authors)

1. **Base model requirements:** The joint scoring mechanism demands LLMs with sufficient context length to process concatenated trajectory batches and strong enough reasoning to make meaningful correctness judgments. This limits model choices.
2. **Reward hacking robustness is unexplained:** While uPRM empirically resists reward hacking better than supervised PRMs, the authors cannot fully characterize why. They call this "an important next step."
3. **Accuracy as incomplete proxy:** The authors acknowledge that direct accuracy of a reward model is an incomplete proxy for downstream utility -- highly accurate PRMs are not necessarily effective teachers.

---

### 6. Does It Truly Challenge the Need for MC Estimation? -- Critical Assessment

**The paper's claims are hedged, and there are significant caveats:**

1. **No direct comparison to MC-based PRMs on ProcessBench.** The headline "15% improvement" is only against LLM-as-Judge, not against MC-annotated PRMs like Math-Shepherd. This is the weakest part of the evaluation -- the paper never shows uPRM beating MC-based annotation on error detection.

2. **On test-time scaling, uPRM matches but does not exceed supervised PRMs.** The average scores are 60.1 (uPRM) vs. 60.0-60.6 (supervised baselines). This demonstrates parity, not superiority.

3. **The RL robustness finding is the strongest argument.** uPRM avoids reward hacking where supervised PRMs collapse. But the authors themselves cannot explain why, making it hard to know if this generalizes.

4. **Training still uses PRM800K trajectories.** While labels are discarded, the method still requires curated reasoning trajectories. It is "unsupervised" in the label sense, not in the data sense.

5. **The scoring LLM (Qwen2.5-14B-Instruct) embeds implicit supervision.** The entire method relies on a powerful instruction-tuned LLM having internalized notions of mathematical correctness through its own training. The supervision is displaced, not eliminated.

**Bottom line:** The paper demonstrates that you can build a competitive PRM without step-level labels or outcome verification, which is genuinely useful for reducing annotation costs. However, it does not provide evidence that uPRM is *better* than MC-based PRMs -- only that it is comparable while being cheaper. The "challenging the need for MC estimation" framing is somewhat oversold; more accurately, the paper shows MC estimation is not strictly *necessary* to achieve similar performance, but it may still be beneficial.

Sources:
- [Unsupervised Process Reward Models (arXiv abstract)](https://arxiv.org/abs/2605.10158)
- [Unsupervised Process Reward Models (HTML full paper)](https://arxiv.org/html/2605.10158)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a9a8bc5-9496-4b22-bc41-81d88cc8cc3f",
  "isSidechain": true,
  "agentId": "abad40be346c30ee3",
  "requestId": "req_011CbU8eHZ6sNrnm74e6knQH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b08ebc8-e892-4598-86f8-0f33ce605046",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7890bce-66e6-4b21-ad35-e826123dba2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161gHUmLKXhbBi2jawXUeQY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 928,
      "cache_read_input_tokens": 14771,
      "output_tokens": 1947,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 928
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1947,
          "cache_read_input_tokens": 14771,
          "cache_creation_input_tokens": 928,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 928,
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
