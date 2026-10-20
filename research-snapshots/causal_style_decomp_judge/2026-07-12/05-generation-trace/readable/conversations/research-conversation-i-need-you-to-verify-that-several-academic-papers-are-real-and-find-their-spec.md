# Research conversation: I need you to verify that several academic papers are real and find their specific baseline numbers. Use WebSearch for e

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9a2f7dc93ea0cae4.jsonl`
- **Structured JSON:** [`978b25b13f82fe936846.json`](../../sessions/97/978b25b13f82fe936846.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

64 recorded events

### User

_source line 1 · 2026-05-27T12:18:00.797Z_

I need you to verify that several academic papers are real and find their specific baseline numbers. Use WebSearch for each.

Papers to verify:
1. "Pseudo-Formalization" by Barkallah et al., May 2026 — search for this paper, its venue, its key results on ArxivMathGradingBench (specifically the ~50% error detection claim)
2. "Safe" by Liu et al., ACL 2025 — search for this paper about step-level formal verification in Lean 4 with ~80% proof success
3. "Hard2Verify" or process reward models dropping from 78.3% to 37.3% — Zheng et al., 2025
4. "miniF2F-Lean Revisited" 2025 — about autoformalization accuracy
5. Bhatt et al., 2025 — uncertainty-guided selective verification with SMT
6. Mu et al., 2026 — adaptive verification allocation, 44% fewer verifier calls on MATH

For each paper, report:
- Whether you found it (with URL if possible)
- The actual venue and year
- Key quantitative results/numbers
- If NOT found, say so clearly

Also search for these specific baseline numbers that the approach would need to beat:
- Best PRM accuracy on research-level math proofs
- Safe's formal verification success rate and cost overhead
- State of the art on ArxivMathGradingBench
- autoformalization success rates (NL to Lean 4)

Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "2200ecd8-f2c5-4b2a-83bb-b6c35abdaed5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T12:18:00.799Z_

```json
{
  "parentUuid": "2200ecd8-f2c5-4b2a-83bb-b6c35abdaed5",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
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
  "uuid": "2cc51fdf-19bc-4268-88d9-cd5808cd2ef5",
  "timestamp": "2026-05-27T12:18:00.799Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T12:18:00.800Z_

```json
{
  "parentUuid": "2cc51fdf-19bc-4268-88d9-cd5808cd2ef5",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "aa935e14-6ffc-4742-80f9-991220009b76",
  "timestamp": "2026-05-27T12:18:00.800Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T12:18:03.616Z_



I'll search for all these papers and baseline numbers in parallel. Let me start by loading the WebSearch tool, then conduct all searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa935e14-6ffc-4742-80f9-991220009b76",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4RyFxjQz1iES6fNeCz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cb5fd55-1220-4692-8409-34de14df9707",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EshRRmvbcRNURgvvngrXKD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1666,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 5 · 2026-05-27T12:18:03.985Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LHyR9RTUVU34MzD1uL1YB1`</summary>

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
  "parentUuid": "8cb5fd55-1220-4692-8409-34de14df9707",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4RyFxjQz1iES6fNeCz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "835a0d8c-278b-47b2-878a-7e2cf44eb4aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EshRRmvbcRNURgvvngrXKD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 7411,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1666
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1666,
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

_source line 6 · 2026-05-27T12:18:03.991Z_

<details><summary>↩ Tool result · `toolu_01LHyR9RTUVU34MzD1uL1YB1`</summary>

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
  "parentUuid": "835a0d8c-278b-47b2-878a-7e2cf44eb4aa",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "a0b6b837-68ad-4d94-b700-74ba51c22199",
  "sourceToolAssistantUUID": "835a0d8c-278b-47b2-878a-7e2cf44eb4aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T12:18:06.370Z_



Now let me search for all the papers and baseline numbers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0b6b837-68ad-4d94-b700-74ba51c22199",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4SDBcerQ2XLw35M6k1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "330b55ce-fe90-4227-8bfa-166dc0aa4b37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cWx2MWLAYsTV4Ej5TM6jc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 9077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 635,
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

_source line 8 · 2026-05-27T12:18:06.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MbFM9u4wAwWe6Es1Zi74o6`</summary>

```json
{
  "query": "Barkallah \"Pseudo-Formalization\" ArxivMathGradingBench 2026 error detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "330b55ce-fe90-4227-8bfa-166dc0aa4b37",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4SDBcerQ2XLw35M6k1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70e4c9be-d241-4229-af43-269c836f81a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cWx2MWLAYsTV4Ej5TM6jc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 9077,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 635
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 9077,
          "cache_creation_input_tokens": 635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 635,
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

_source line 9 · 2026-05-27T12:18:18.083Z_

<details><summary>↩ Tool result · `toolu_01MbFM9u4wAwWe6Es1Zi74o6`</summary>

```text
Web search results for query: "Barkallah "Pseudo-Formalization" ArxivMathGradingBench 2026 error detection"

Links: [{"title":"From Euler to Today: Universal Mathematical Fallibility A Large-Scale Computational Analysis of Errors in ArXiv Papers","url":"https://arxiv.org/pdf/2511.10543"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal   Large Language Models Via Error Detection","url":"https://arxiv.org/pdf/2410.04509"},{"title":"NL2SQL-BUGs: A Benchmark for Detecting Semantic Errors in NL2SQL Translation","url":"https://arxiv.org/pdf/2503.11984"}]

The search didn't return specific results about Barkallah's "Pseudo-Formalization" work or ArxivMathGradingBench. Let me try a more targeted search:

Links: [{"title":"“I Wanted Them to Think That I Wrote That”: AI-Generated Self-Presentation on Dating Apps and Implications of Non-Disclosure on Informed Consent | Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3772318.3791593"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"Conjecturing: An Overlooked Step in Formal Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.11986"},{"title":"Aymen BARKALLAH - A2B structure | LinkedIn","url":"https://www.linkedin.com/in/aymen-barkallah-a43487177/"},{"title":"FMTea 2026","url":"https://fmtea.github.io/"},{"title":"Whole-Genome Sequence of Corynebacterium pseudotuberculosis Strain 226, Isolated from the Abscess of a Goat in California","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4767917/"}]

I found a reference to Manel Barkallah in the search results. Let me try a more specific search:

Links: [{"title":"From Euler to Today: Universal Mathematical Fallibility A Large-Scale Computational Analysis of Errors in ArXiv Papers","url":"https://arxiv.org/pdf/2511.10543"},{"title":"[2410.04509] ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection","url":"https://arxiv.org/abs/2410.04509"},{"title":"ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal Large Language Models Via Error Detection","url":"https://arxiv.org/html/2410.04509"},{"title":"ErrorRadar: Benchmarking Complex Mathematical Reasoning of Multimodal   Large Language Models Via Error Detection","url":"https://arxiv.org/pdf/2410.04509"},{"title":"UGMathBench: A Diverse and Dynamic Benchmark for Undergraduate-Level Mathematical Reasoning with Large Language Models","url":"https://arxiv.org/html/2501.13766v1"}]

Based on my web searches, I was unable to find specific information about Barkallah's "Pseudo-Formalization" work or a benchmark called "ArxivMathGradingBench" in relation to error detection from 2026.

The search results did return several related papers on mathematical error detection benchmarks:

- ErrorRadar, a benchmark designed to assess multimodal large language models' capabilities in error detection, which evaluates two sub-tasks: error step identification and error categorization

- A large-scale computational analysis system that detects mathematical errors and provides complete referee reports, having processed over 37,000 papers across multiple mathematical categories

However, I could not locate the specific paper or work you're asking about regarding Barkallah's "Pseudo-Formalization" and ArxivMathGradingBench. The search did identify a Manel Barkallah who works on formal methods education, but no connection to the specific work you mentioned. If you have more details about where this work was published or additional context, I'd be happy to search again.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70e4c9be-d241-4229-af43-269c836f81a1",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "7392fbd9-d79a-4068-90de-9f6dea68a38d",
  "sourceToolAssistantUUID": "70e4c9be-d241-4229-af43-269c836f81a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-27T12:18:20.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AhGrm588ZuDB7NSqttNjNe`</summary>

```json
{
  "query": "Liu et al \"Safe\" ACL 2025 step-level formal verification Lean 4 proof success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7392fbd9-d79a-4068-90de-9f6dea68a38d",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4TFAxFxTbBvxLDnte2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66375d0f-6b1f-4db6-b443-20ce85794378",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JteGciUvPtuxTn89kfPJmE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1294,
      "cache_read_input_tokens": 9712,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1294
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 9712,
          "cache_creation_input_tokens": 1294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1294,
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

_source line 11 · 2026-05-27T12:18:29.509Z_

<details><summary>↩ Tool result · `toolu_01AhGrm588ZuDB7NSqttNjNe`</summary>

```text
Web search results for query: "Liu et al "Safe" ACL 2025 step-level formal verification Lean 4 proof success"

Links: [{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.594/"},{"title":"GitHub - liuchengwucn/Safe: (ACL 2025 Main) Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - Official Implementation & Dataset","url":"https://github.com/liuchengwucn/Safe"},{"title":"arXiv:2506.04592v1 [cs.CL] 5 Jun 2025","url":"https://arxiv.org/pdf/2506.04592"},{"title":"[2506.04592] Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/abs/2506.04592"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification | Request PDF","url":"https://www.researchgate.net/publication/394301322_Safe_Enhancing_Mathematical_Reasoning_in_Large_Language_Models_via_Retrospective_Step-aware_Formal_Verification"},{"title":"Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4","url":"https://arxiv.org/html/2602.01291v1"},{"title":"Construction-Verification: A Benchmark for Applied Mathematics in Lean 4","url":"https://arxiv.org/pdf/2602.01291"}]

Based on the search results, I found the paper you're looking for:

"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification" by Liu, Chengwu and colleagues, published in ACL 2025.

Key aspects of this work:

**Core Contribution:** This work represents the first endeavor to utilize formal mathematical language Lean 4 for verifying content generated by LLMs.

**Methodology:** The framework incorporates a step verifier that performs auto-formalization using in-context learning, validates the formalized Lean 4 theorem using the Lean REPL, and attempts to prove the theorem using an LLM-based prover, followed by verification through the Lean REPL.

**Benchmark:** The authors propose FormalStep as a benchmark for step correctness theorem proving with 30,809 formal statements.

**Results:** The framework was evaluated across multiple language models and various mathematical datasets, demonstrating significant performance improvement while offering interpretable and verifiable evidence.

The official implementation and datasets are available on GitHub at [liuchengwucn/Safe](https://github.com/liuchengwucn/Safe), and the full paper is available on both the ACL Anthology and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66375d0f-6b1f-4db6-b443-20ce85794378",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "272ac5d5-67e5-4ec9-938e-25e44f4f5304",
  "sourceToolAssistantUUID": "66375d0f-6b1f-4db6-b443-20ce85794378",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-27T12:18:32.596Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RZ9PgKbp8bHzETBEwpbU4x`</summary>

```json
{
  "query": "Zheng et al \"Hard2Verify\" process reward models 78.3% 37.3% 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "272ac5d5-67e5-4ec9-938e-25e44f4f5304",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4U61pSt5XPhUZRnow4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86afb9fd-8211-45b9-8ffb-b7a64a0730fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tf2aS6E5UoCbaJr5EJj6Gr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 11006,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 813
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 11006,
          "cache_creation_input_tokens": 813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 813,
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

_source line 13 · 2026-05-27T12:18:39.120Z_

<details><summary>↩ Tool result · `toolu_01RZ9PgKbp8bHzETBEwpbU4x`</summary>

```text
Web search results for query: "Zheng et al "Hard2Verify" process reward models 78.3% 37.3% 2025"

Links: [{"title":"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math","url":"https://arxiv.org/html/2510.13744v1"},{"title":"Preprint | Salesforce AI Research HARD2VERIFY: A STEP-LEVEL VERIFICATION","url":"https://arxiv.org/pdf/2510.13744"},{"title":"(PDF) Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math","url":"https://www.researchgate.net/publication/396517985_Hard2Verify_A_Step-Level_Verification_Benchmark_for_Open-Ended_Frontier_Math"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/pdf/2603.06621"},{"title":"Rethinking Reward Models for Multi-Domain Test-Time Scaling","url":"https://arxiv.org/pdf/2510.00492"},{"title":"SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning","url":"https://arxiv.org/pdf/2512.03244"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"}]

Based on the search results, I found information about the Hard2Verify benchmark and the specific performance metrics you mentioned.

Hard2Verify is a step-level verification benchmark for open-ended frontier math, where Qwen2.5-Math-PRM-72B's performance drops from ProcessBench state-of-the-art at 78.3 to 37.3 on Hard2Verify for an error identification task.

The benchmark was created by researchers who also evaluated models on both ProcessBench (Zheng et al., 2024a) and the Hard2Verify benchmark. This significant performance drop demonstrates that past benchmarks do not sufficiently evaluate in the frontier-level math settings that Hard2Verify does.

The research was published in October 2025 as a preprint on arXiv (arXiv:2510.13744).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86afb9fd-8211-45b9-8ffb-b7a64a0730fa",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "13e559d3-508e-48f1-be06-6082f82ab1fa",
  "sourceToolAssistantUUID": "86afb9fd-8211-45b9-8ffb-b7a64a0730fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-27T12:18:42.059Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HCFwiR97fECahQQ8qRikjv`</summary>

```json
{
  "query": "\"miniF2F\" \"Lean\" \"Revisited\" autoformalization accuracy 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13e559d3-508e-48f1-be06-6082f82ab1fa",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4Uo6c8uiLufP6uuZ8p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "554e8358-4cd8-4c35-9dda-1acbc30068db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MvK8xsn42GATKrTRyC3Rk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 11819,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 11819,
          "cache_creation_input_tokens": 704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 704,
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

_source line 15 · 2026-05-27T12:18:48.000Z_

<details><summary>↩ Tool result · `toolu_01HCFwiR97fECahQQ8qRikjv`</summary>

```text
Web search results for query: ""miniF2F" "Lean" "Revisited" autoformalization accuracy 2025"

Links: [{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/html/2511.03108v1"},{"title":"[Quick Review] miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://liner.com/review/minif2flean-revisited-reviewing-limitations-and-charting-path-forward"},{"title":"(PDF) miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://www.researchgate.net/publication/397322220_miniF2F-Lean_Revisited_Reviewing_Limitations_and_Charting_a_Path_Forward"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://openreview.net/pdf?id=KtaHv0YUyh"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward | OpenReview","url":"https://openreview.net/forum?id=KtaHv0YUyh"},{"title":"Paper page - miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://huggingface.co/papers/2511.03108"},{"title":"[2511.03108] miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/abs/2511.03108"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/pdf/2511.03108"},{"title":"NeurIPS Poster miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://neurips.cc/virtual/2025/poster/118598"}]

Based on the search results, here are the key findings from the "miniF2F-Lean Revisited" paper about autoformalization accuracy in 2025:

## Key Accuracy Findings

While the accuracy of the best autoformalization model on miniF2F is reported to be about 97%, and the accuracy of Kimina Prover on miniF2F is 70.8%, the combined accuracy of these models leads to an accuracy of 34.8% after comparing the final proofs with the original problem statements in informal language.

## Critical Discovery About Reported Accuracies

The research reveals a significant discrepancy in how autoformalization accuracy is typically evaluated. Extensive human evaluation of autoformalization results, across five models, reveals that their autoformalization accuracy is not as high as the ones reported in the literature, because those reported accuracies are often evaluated by LLMs and not by a human familiar with the formal language. Specifically, when performing a human review of the outputs of Herald @128 that LLM has marked as 97% correct, the actual accuracy was found to be much lower at 66%.

## Improvements with miniF2F-v2

Evaluating the full theorem proving pipeline on miniF2F-v2 leads to the best accuracy of 70%, a significant improvement from the 40% on the original miniF2F, yet indicating considerable misalignment between the autoformalization models and theorem provers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "554e8358-4cd8-4c35-9dda-1acbc30068db",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "8a7f694e-0f29-4cbd-a705-949237136abe",
  "sourceToolAssistantUUID": "554e8358-4cd8-4c35-9dda-1acbc30068db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T12:18:51.349Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ad3Nq4tTxTKV9Ur6t8Ldvn`</summary>

```json
{
  "query": "Bhatt et al 2025 uncertainty-guided selective verification SMT math reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a7f694e-0f29-4cbd-a705-949237136abe",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4VT5NXUKt6edtn9KJu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21d54506-3b09-491e-9c65-3f21f54a6be1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011EkPepzqSkUskpMYQAbjgR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 942,
      "cache_read_input_tokens": 12523,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 12523,
          "cache_creation_input_tokens": 942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 942,
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

_source line 17 · 2026-05-27T12:19:03.226Z_

<details><summary>↩ Tool result · `toolu_01Ad3Nq4tTxTKV9Ur6t8Ldvn`</summary>

```text
Web search results for query: "Bhatt et al 2025 uncertainty-guided selective verification SMT math reasoning"

Links: [{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/html/2505.20047"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in ...","url":"https://arxiv.org/pdf/2505.20047"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/pdf/2602.03975"},{"title":"Uncertainty-aware Step-wise Verification with Generative Reward Models","url":"https://arxiv.org/pdf/2502.11250"},{"title":"Not All Votes Count! Programs as Verifiers Improve Self-Consistency of   Language Models for Math Reasoning","url":"https://arxiv.org/pdf/2410.12608"},{"title":"Step-by-Step Reasoning for Math Problems via Twisted Sequential Monte   Carlo","url":"https://arxiv.org/pdf/2410.01920"},{"title":"Scaling Flaws of Verifier-Guided Search in Mathematical Reasoning","url":"https://arxiv.org/pdf/2502.00271"}]

Based on the search results, I found a highly relevant paper that matches your query:

The paper "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks" addresses how probabilistic uncertainty in LLM outputs for formal reasoning tasks, particularly when generating SMT-LIB programs, can serve as valuable information for guiding verification.

The research evaluates five frontier LLMs and reveals that Satisfiability Modulo Theories (SMT) based autoformalization shows domain-specific impact on accuracy. The paper introduces a probabilistic context-free grammar (PCFG) framework to model LLM outputs, yielding a refined uncertainty taxonomy.

The findings show that uncertainty signals are task-dependent, and a lightweight fusion of these signals enables selective verification to cut error rates by 14-100%.

The paper was published on May 26, 2025, and is available on arXiv (arxiv.org/abs/2505.20047).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21d54506-3b09-491e-9c65-3f21f54a6be1",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "8a42e2c5-8e27-478d-9ad6-23057bb22845",
  "sourceToolAssistantUUID": "21d54506-3b09-491e-9c65-3f21f54a6be1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-27T12:19:06.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0126EWLjmm3dL7gwaJ2o7usa`</summary>

```json
{
  "query": "Mu et al 2026 adaptive verification allocation \"fewer verifier calls\" MATH dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a42e2c5-8e27-478d-9ad6-23057bb22845",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4WaAncL1zd77nNKPBS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26fe8043-7649-49dd-8e36-900e3ab6bcff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uyo3pvG5jzzTsfZHFB5jRZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 13465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 632,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 19 · 2026-05-27T12:19:12.806Z_

<details><summary>↩ Tool result · `toolu_0126EWLjmm3dL7gwaJ2o7usa`</summary>

```text
Web search results for query: "Mu et al 2026 adaptive verification allocation "fewer verifier calls" MATH dataset"

Links: [{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/html/2602.03975v1"},{"title":"What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/pdf/2602.01070"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/pdf/2602.03975"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"},{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via...","url":"https://arxiv.org/abs/2604.14853"},{"title":"Pessimistic Verification for Open Ended Math Questions","url":"https://arxiv.org/pdf/2511.21522"}]

I found a relevant research paper that matches your query. On the MATH benchmark, this approach achieves higher accuracy than best-of-N, majority voting, and beam search while using 44% fewer verifier calls.

The method allocates verification according to state-local uncertainty rather than a uniform or purely problem-level rule, using deterministic gating, ranking surviving candidates with a hybrid pre-verification score, and choosing a state-conditional verification budget so that ambiguous branching points receive more verification while clear decisions receive less.

The paper is titled "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure" and was published on arXiv on February 3, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26fe8043-7649-49dd-8e36-900e3ab6bcff",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "e8e36bd2-f08a-41c9-abf0-5122fe1739f4",
  "sourceToolAssistantUUID": "26fe8043-7649-49dd-8e36-900e3ab6bcff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-27T12:19:15.460Z_

Now let me search for the specific baseline numbers requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8e36bd2-f08a-41c9-abf0-5122fe1739f4",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4XH7dzuRyp7Wid9Jkb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73c1d25b-8848-4091-96fa-a8abe244ac58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J47PFcF8LzAVxhFijLHe8w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 14097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 525,
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

_source line 21 · 2026-05-27T12:19:16.372Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D3g8D8nzn62fRett3Xi5Eo`</summary>

```json
{
  "query": "best PRM accuracy research-level math proofs process reward model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73c1d25b-8848-4091-96fa-a8abe244ac58",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4XH7dzuRyp7Wid9Jkb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9159f8cb-06aa-4b17-8f5c-903c468cab73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J47PFcF8LzAVxhFijLHe8w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 14097,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 525
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 14097,
          "cache_creation_input_tokens": 525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 525,
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

_source line 22 · 2026-05-27T12:19:25.724Z_

<details><summary>↩ Tool result · `toolu_01D3g8D8nzn62fRett3Xi5Eo`</summary>

```text
Web search results for query: "best PRM accuracy research-level math proofs process reward model 2025 2026"

Links: [{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"Proof-RM: A Scalable and Generalizable Reward Model for Mathematics Proof Verification","url":"https://arxiv.org/html/2602.02377"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"[2503.21295] R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/abs/2503.21295"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://aclanthology.org/2025.emnlp-main.679.pdf"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://arxiv.org/pdf/2602.09305"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/pdf/2503.21295"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"}]

Based on the search results, here are the key findings on PRM accuracy for research-level math proofs in 2025-2026:

## Top Performing Models

R-PRM surpasses strong baselines by 11.9 and 8.5 points in F1 scores on ProcessBench and PRMBench, respectively, and achieves consistent accuracy improvements of over 8.5 points across six challenging datasets when applied to guide mathematical reasoning.

ThinkPRM beats baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search, with the PRM surpassing discriminative verifiers trained with the full PRM800K by 8% and 4.5% respectively on out-of-domain evaluations over GPQA-Diamond and LiveCodeBench subsets.

## Proof Verification Advancement

Costly expert checking is now the only way to accurately evaluate proofs at the research level, creating an increasingly urgent need for a model that can verify correctness of proofs. In top-competition-level and research-level math, problems are predominantly proof-based, such as in USAMO 2025 where 4 out of 6 problems are proof problems.

## Key Architectural Improvements

Error-aware architectures like PathFinder-PRM introduce a hierarchically decoupled structure classifying error types at each step, which has been empirically shown to improve both benchmark F1 and downstream guided search performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9159f8cb-06aa-4b17-8f5c-903c468cab73",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "58e5b7f8-5e6f-43ea-b8bb-bab5c9f9f20f",
  "sourceToolAssistantUUID": "9159f8cb-06aa-4b17-8f5c-903c468cab73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-27T12:19:28.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YPmNyU8ZPtZqjWBCXwRRxf`</summary>

```json
{
  "query": "Safe formal verification success rate cost overhead Lean 4 step verification ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58e5b7f8-5e6f-43ea-b8bb-bab5c9f9f20f",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4YEME4XyjtVW26cWoD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cf38da9-959a-4630-97ab-c3210b792a12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtEGKNf38irYfmPLRiCCd1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 862,
      "cache_read_input_tokens": 14622,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 862
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 14622,
          "cache_creation_input_tokens": 862,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 862,
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

_source line 24 · 2026-05-27T12:19:38.966Z_

<details><summary>↩ Tool result · `toolu_01YPmNyU8ZPtZqjWBCXwRRxf`</summary>

```text
Web search results for query: "Safe formal verification success rate cost overhead Lean 4 step verification ACL 2025"

Links: [{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.594/"},{"title":"GitHub - liuchengwucn/Safe: (ACL 2025 Main) Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - Official Implementation & Dataset","url":"https://github.com/liuchengwucn/Safe"},{"title":"Lean4: The Theorem Prover That's Becoming AI's Most Important Safety Net","url":"https://winsomemarketing.com/ai-in-marketing/lean4-the-theorem-prover-thats-becoming-ais-most-important-safety-net"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/pdf/2506.04592"},{"title":"[2506.04592] Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/abs/2506.04592"},{"title":"VeriBench: End-to-End Formal Verification Benchmark for ...","url":"https://openreview.net/pdf?id=rWkGFmnSNl"},{"title":"Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4","url":"https://arxiv.org/html/2602.01291"}]

Based on the search results, I found information about the Safe framework presented at ACL 2025. Here's what the research reveals:

## Safe Framework Overview

Safe is a retrospective, step-aware formal verification framework designed to enhance mathematical reasoning in large language models. The framework articulates mathematical claims in formal mathematical language Lean 4 at each reasoning step and provides formal proofs to identify hallucinations.

## Key Results

The framework demonstrates significant performance improvement while offering interpretable and verifiable evidence across multiple language models and various mathematical datasets.

## Benchmark and Dataset

The researchers proposed FormalStep as a benchmark for step correctness theorem proving with 30,809 formal statements.

## Innovation

This represents the first endeavor to utilize formal mathematical language Lean 4 for verifying natural language content generated by LLMs, aligning with the reason why formal mathematical languages were created in the first place: to provide a robust foundation for hallucination-prone human-written proofs.

However, the search results do not contain specific information about the success rate percentages or the detailed cost overhead metrics for this approach. For more detailed quantitative results, you may want to consult the full paper on the ACL Anthology or arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cf38da9-959a-4630-97ab-c3210b792a12",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "ba783e4d-2e6d-4f8c-b2af-c3c86c24a076",
  "sourceToolAssistantUUID": "0cf38da9-959a-4630-97ab-c3210b792a12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-27T12:19:42.226Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G6NAEBm6FENcgVV1FCAcQ1`</summary>

```json
{
  "query": "ArxivMathGradingBench benchmark state of the art results 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba783e4d-2e6d-4f8c-b2af-c3c86c24a076",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4ZCz9o5aEEmo5Udg9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2615e589-213f-4a4d-9fb8-9698c3e9c194",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAzDQ5P3G6MyBN6fdWgYjA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 15484,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 773
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 15484,
          "cache_creation_input_tokens": 773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 773,
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

_source line 26 · 2026-05-27T12:19:49.943Z_

<details><summary>↩ Tool result · `toolu_01G6NAEBm6FENcgVV1FCAcQ1`</summary>

```text
Web search results for query: "ArxivMathGradingBench benchmark state of the art results 2025 2026"

Links: [{"title":"LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics","url":"https://arxiv.org/pdf/2602.24173"},{"title":"IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation","url":"https://arxiv.org/html/2509.26076v1"},{"title":"Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad","url":"https://arxiv.org/pdf/2503.21934"},{"title":"Towards Robust Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.01846"},{"title":"Evaluating Large Reasoning Model Performance on Complex Medical Scenarios In The MMLU-Pro Benchmark","url":"https://www.medrxiv.org/content/10.1101/2025.04.07.25325385.full.pdf"},{"title":"State-of-the-Art: The Temporal Order of Benchmarking Culture","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12048445/"},{"title":"Escaping the Cognitive Well: Efficient Competition Math with Off-the-Shelf Models","url":"https://arxiv.org/pdf/2602.16793"}]

Based on the search results, I found information about related mathematical benchmarks from 2025-2026, though the exact "ArxivMathGradingBench" benchmark wasn't directly mentioned. However, I did find highly relevant information about related mathematical grading and proof evaluation benchmarks:

**IMO-GradingBench:**
An autograding benchmark with 1000 human gradings on proofs was constructed to enable further progress in automatic evaluation of long-form answers.

**IMO-ProofBench Results:**
Gemini Deep Think achieved 65.7% on the advanced IMO-ProofBench, surpassing the best non-Gemini models by 42.4%.

**Other Recent Mathematical Benchmarks (2025-2026):**

- **IMProofBench:** A private benchmark developed in collaboration with the mathematical research community to evaluate LLMs on research-level proof writing.

- **Proof Evaluation on USAMO:** Expert human annotators evaluated state-of-the-art reasoning models on 2025 USAMO problems, finding that only Gemini-2.5-Pro achieved a non-trivial score of 25%, while all other models achieved less than 5%.

The search results suggest that mathematical grading and proof evaluation benchmarks have become increasingly important in 2025-2026 for assessing LLM capabilities beyond just final answers. If you're looking for more specific information about ArxivMathGradingBench, you might want to check the latest arXiv submissions directly or provide additional context about this benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2615e589-213f-4a4d-9fb8-9698c3e9c194",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "c80bc868-bd6a-4002-9ea9-62864cff8439",
  "sourceToolAssistantUUID": "2615e589-213f-4a4d-9fb8-9698c3e9c194",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-27T12:19:53.083Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JmHZ5RoBFuAY8ZX4nZ28FA`</summary>

```json
{
  "query": "autoformalization success rate natural language to Lean 4 translation 2025 2026 state of art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c80bc868-bd6a-4002-9ea9-62864cff8439",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4a1z9A7XmpXZunQHqL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "953f7042-957d-4104-b72f-fa8deac493b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADkkLgwDb6cAGk9wcHLfE5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 16257,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 804
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 16257,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 804,
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

_source line 28 · 2026-05-27T12:20:02.029Z_

<details><summary>↩ Tool result · `toolu_01JmHZ5RoBFuAY8ZX4nZ28FA`</summary>

```text
Web search results for query: "autoformalization success rate natural language to Lean 4 translation 2025 2026 state of art"

Links: [{"title":"Autoformalization with Large Language Models","url":"https://www.emergentmind.com/topics/autoformalization-with-large-language-models"},{"title":"[2510.15681] ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/abs/2510.15681"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Translating Natural Language into Lean 4 through Multi- ...","url":"https://aclanthology.org/2025.emnlp-main.1586v1.pdf"},{"title":"MerLean: An Agentic Framework For Autoformalization in Quantum Computation","url":"https://arxiv.org/html/2602.16554v1"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/pdf/2510.15681"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.15940"}]

Based on the search results, here's what I found about the state-of-the-art in autoformalization with natural language to Lean 4 translation for 2025-2026:

## Success Rates and Key Achievements

One approach achieves 68.4% pass rate on benchmarks such as MiniF2F. Additionally, Xu and Odersky (2026) demonstrated agentic proof automation by mechanizing System Capless (14,000+ lines of Lean 4) with 87% task success rate across 189 annotated tasks.

## Recent Methodological Advances

On-the-fly and distilled backtranslation, as well as line-by-line proof state analysis, have demonstrated superior results for Lean4 formalization (Chan et al., 18 Feb 2025). Process-driven autoformalization (FormL4+PSV) uses stepwise compiler traces, labeling each tactic as correct/incorrect, with the Process-Supervised Verifier filtering and ranking candidate formalizations to improve accuracy and sample efficiency.

## Data and Infrastructure Development

Large-scale LLM was used to automatically translate natural language math problems into Lean 4 formal statements, generating the Goedel-Pset-v1 dataset containing 1.64M formulative statements. FineLeanCorpus (2025) provides 509k NL/Lean4 pairs with difficulty ratings and domain labels.

## Remaining Challenges

However, state-of-the-art LLMs still cannot solve math research problems, indicating that while significant progress has been made, substantial challenges remain in full autoformalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "953f7042-957d-4104-b72f-fa8deac493b9",
  "isSidechain": true,
  "promptId": "b20dcf5f-0e10-41c2-b184-a16c9743162a",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "3274e8dc-a08f-4583-b60c-4658cec55089",
  "sourceToolAssistantUUID": "953f7042-957d-4104-b72f-fa8deac493b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-27T12:20:05.497Z_

Let me get more specific numbers from the Safe paper and the Hard2Verify paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3274e8dc-a08f-4583-b60c-4658cec55089",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4aubwS583LhXSLXVRC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83d0fbd4-3f58-4b9c-a01f-0e954e351950",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GouxfXo35YRCvfmpHPMph2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 17061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 859,
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

_source line 30 · 2026-05-27T12:20:06.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JtTHFHm4SzAuTTEF4B6uRd`</summary>

```json
{
  "query": "Safe Liu ACL 2025 \"proof success rate\" OR \"verification accuracy\" OR \"80%\" formal step Lean results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83d0fbd4-3f58-4b9c-a01f-0e954e351950",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4aubwS583LhXSLXVRC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23e07bde-ba2c-41a4-801e-92440dc54633",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GouxfXo35YRCvfmpHPMph2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 17061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 859,
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

_source line 31 · 2026-05-27T12:20:14.826Z_

<details><summary>↩ Tool result · `toolu_01JtTHFHm4SzAuTTEF4B6uRd`</summary>

```text
Web search results for query: "Safe Liu ACL 2025 "proof success rate" OR "verification accuracy" OR "80%" formal step Lean results"

Links: [{"title":"GitHub - liuchengwucn/Safe: (ACL 2025 Main) Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - Official Implementation & Dataset","url":"https://github.com/liuchengwucn/Safe"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.594/"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification | Request PDF","url":"https://www.researchgate.net/publication/394301322_Safe_Enhancing_Mathematical_Reasoning_in_Large_Language_Models_via_Retrospective_Step-aware_Formal_Verification"},{"title":"Lean4: How the theorem prover works and why it's the new competitive edge in AI - NeurByte AI","url":"https://www.neurbyte.net/2025/11/25/lean4-how-the-theorem-prover-works-and-why-its-the-new-competitive-edge-in-ai/"},{"title":"Lean4: How the theorem prover works and why it's the new competitive edge in AI - NOVALOGIQ","url":"https://novalogiq.com/2025/11/23/lean4-how-the-theorem-prover-works-and-why-its-the-new-competitive-edge-in-ai/"},{"title":"ProofOptimizer: Training Language Models to Simplify Proofs without Human Demonstrations","url":"https://arxiv.org/pdf/2510.15700"},{"title":"LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction","url":"https://leandojo.org/leanprogress.html"}]

I found information about the Safe framework from ACL 2025. Safe is a retrospective, step-aware formal verification framework that articulates mathematical claims in formal mathematical language Lean 4 at each reasoning step and provides formal proofs to identify hallucinations. The work also proposes FormalStep as a benchmark for step correctness theorem proving with 30,809 formal statements.

However, the search results I retrieved don't contain specific quantitative results mentioning "proof success rate," "verification accuracy," or the "80%" figure you're looking for. The GitHub repository and ACL Anthology pages in the results focus on the framework description rather than detailed performance metrics. To find the specific numerical results you're interested in, you may want to:

1. Access the full paper directly at the ACL Anthology link (https://aclanthology.org/2025.acl-long.594/)
2. Check the GitHub repository's README or documentation (https://github.com/liuchengwucn/Safe)
3. Look for a preprint version on arXiv

Would you like me to search for more specific performance metrics or quantitative results from the Safe paper?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23e07bde-ba2c-41a4-801e-92440dc54633",
  "isSidechain": true,
  "promptId": "9b06605d-7e70-447b-9d1c-b9dfe27e0c9d",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "3598b31c-dcbb-4ca3-8e11-8778404635fa",
  "sourceToolAssistantUUID": "23e07bde-ba2c-41a4-801e-92440dc54633",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T12:20:20.754Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R5CokCudfVnR4gJqhvGMxQ`</summary>

```json
{
  "query": "Hard2Verify Zheng 2025 \"78.3\" \"37.3\" ProcessBench Qwen PRM benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3598b31c-dcbb-4ca3-8e11-8778404635fa",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4brL2NipAfJYov6AKD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6102a47-6479-4fef-a6c5-7f1d1896f4c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2xgBi5MubPZZwQ58iUZST",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 876,
      "cache_read_input_tokens": 17920,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 876
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 17920,
          "cache_creation_input_tokens": 876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 876,
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

_source line 33 · 2026-05-27T12:20:28.706Z_

<details><summary>↩ Tool result · `toolu_01R5CokCudfVnR4gJqhvGMxQ`</summary>

```text
Web search results for query: "Hard2Verify Zheng 2025 "78.3" "37.3" ProcessBench Qwen PRM benchmark results"

Links: [{"title":"Hard2Verify: A Step-Level Verification Benchmark for Open ...","url":"https://arxiv.org/pdf/2510.13744"},{"title":"(PDF) Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math","url":"https://www.researchgate.net/publication/396517985_Hard2Verify_A_Step-Level_Verification_Benchmark_for_Open-Ended_Frontier_Math"},{"title":"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math","url":"https://arxiv.org/html/2510.13744v1"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://www.researchgate.net/publication/394269497_ProcessBench_Identifying_Process_Errors_in_Mathematical_Reasoning"},{"title":"Towards Effective Process Supervision in Mathematical Reasoning | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-math-prm/"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"}]

Based on the search results, I found information about the benchmark results you're looking for:

On the same error identification task, Qwen2.5-Math-PRM-72B performance drops from ProcessBench state-of-the-art at 78.3 to 37.3 on Hard2Verify.

This comes from the paper "Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math" by researchers including Zheng (published in October 2025). The finding demonstrates a significant performance gap between the ProcessBench benchmark and the harder Hard2Verify benchmark for the Qwen2.5-Math-PRM-72B process reward model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6102a47-6479-4fef-a6c5-7f1d1896f4c0",
  "isSidechain": true,
  "promptId": "9b06605d-7e70-447b-9d1c-b9dfe27e0c9d",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "17d52d4d-faf9-4abf-a2e7-1a86c6ed1435",
  "sourceToolAssistantUUID": "b6102a47-6479-4fef-a6c5-7f1d1896f4c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-27T12:20:32.292Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MscCVh9cmwttT35rPucZ4k`</summary>

```json
{
  "query": "Mu et al \"Adaptive Test-Time Compute\" 2026 \"44%\" verifier calls categorical structure authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17d52d4d-faf9-4abf-a2e7-1a86c6ed1435",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4csevUxgCDKHSdTCYQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c7e15f1-4840-4e7b-8bff-ebc7dcffef23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137myokRwzwk9E24ZwbbGZs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 606,
      "cache_read_input_tokens": 18796,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 606
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 18796,
          "cache_creation_input_tokens": 606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 606,
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

_source line 35 · 2026-05-27T12:20:39.401Z_

<details><summary>↩ Tool result · `toolu_01MscCVh9cmwttT35rPucZ4k`</summary>

```text
Web search results for query: "Mu et al "Adaptive Test-Time Compute" 2026 "44%" verifier calls categorical structure authors"

Links: [{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/html/2602.03975"},{"title":"[2602.03975] Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/abs/2602.03975"},{"title":"[Literature Review] Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://www.themoonlight.io/en/review/adaptive-test-time-compute-allocation-via-learned-heuristics-over-categorical-structure"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over","url":"https://arxiv.org/pdf/2602.03975"},{"title":"What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/pdf/2602.01070"},{"title":"Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations","url":"https://arxiv.org/html/2604.21018"},{"title":"Adaptive Test-Time Compute Allocation","url":"https://www.emergentmind.com/topics/adaptive-test-time-compute-allocation"}]

I found the paper you're looking for! Here are the key details:

**Paper:** "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure"

**Author:** Shuhui Qu from Stanford University

**Year:** 2026 (published February 3, 2026)

**Key Results:** The approach achieves higher accuracy than best-of-N, majority voting, and beam search while using 44% fewer verifier calls. More specifically, the approach achieves 55.2% accuracy while using an average of 44.8 verifier calls.

**Main Contribution:** The paper proposes a state-level selective verification framework that combines deterministic feasibility gating over a structured move interface, pre-verification ranking using a hybrid of learned state-distance and residual scoring, and adaptive allocation of verifier calls based on local uncertainty.

**Benchmark:** The framework is evaluated on the MATH benchmark using Llama 3.2 1B as the backbone generator and a process reward model (PRM) as the verifier.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c7e15f1-4840-4e7b-8bff-ebc7dcffef23",
  "isSidechain": true,
  "promptId": "9b06605d-7e70-447b-9d1c-b9dfe27e0c9d",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "31558db5-a6e3-4094-9ecd-d55c30ce0999",
  "sourceToolAssistantUUID": "4c7e15f1-4840-4e7b-8bff-ebc7dcffef23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-27T12:20:43.925Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RbW1apxANNJPXNcZMZNP71`</summary>

```json
{
  "query": "Bhatt 2025 \"selective verification\" SMT uncertainty LLM mathematical reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31558db5-a6e3-4094-9ecd-d55c30ce0999",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4dfXgxgJdpYX6pEBoi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55d10bc6-8da1-4a4e-8c39-b386c4cd1a60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCwQTvZZ2gcgv93eRPJZfJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 19402,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 19402,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 694,
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

_source line 37 · 2026-05-27T12:20:52.363Z_

<details><summary>↩ Tool result · `toolu_01RbW1apxANNJPXNcZMZNP71`</summary>

```text
Web search results for query: "Bhatt 2025 "selective verification" SMT uncertainty LLM mathematical reasoning"

Links: [{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/html/2505.20047"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://openreview.net/attachment?id=QfKpJ00t2L&name=pdf"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in ...","url":"https://arxiv.org/pdf/2505.20047"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055v2"},{"title":"Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving","url":"https://arxiv.org/pdf/2505.20869"},{"title":"Techrxiv","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176538331.19733376/v1"},{"title":"Right Is Not Enough: The Pitfalls of Outcome Supervision in Training LLMs for Math Reasoning","url":"https://arxiv.org/pdf/2506.06877"}]

Based on the search results, I found a highly relevant paper that matches your query:

**"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks"**

This research addresses the intersection of all your keywords:

- **SMT & LLM Mathematical Reasoning**: The paper evaluates Satisfiability Modulo Theories (SMT) based autoformalization's domain-specific impact on accuracy, ranging from +34.8% on logical tasks to -44.5% on factual ones.

- **Uncertainty Quantification**: The authors introduce a probabilistic context-free grammar (PCFG) framework to model LLM outputs, yielding a refined uncertainty taxonomy.

- **Selective Verification**: A lightweight fusion of uncertainty signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention.

The paper's core contribution is demonstrating that formal reasoning uncertainty is task-dependent and introducing a model-agnostic fusion of varied uncertainty signals that outperforms individual metrics. The authors analyze ensembles of LLM-generated SMT-LIB programs rather than relying on single outputs, enabling more reliable formal verification for mathematical reasoning tasks.

The paper was published recently (arxiv: 2505.20047, dated May 26, 2025) and is associated with NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55d10bc6-8da1-4a4e-8c39-b386c4cd1a60",
  "isSidechain": true,
  "promptId": "6c3f38f9-fafd-47f3-9f71-5e57d73fa4b4",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "50594151-7cf7-4085-bf65-f851c9d97d2f",
  "sourceToolAssistantUUID": "55d10bc6-8da1-4a4e-8c39-b386c4cd1a60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-27T12:20:55.549Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ld3bxz7au786scquHL8y6m`</summary>

```json
{
  "query": "\"Pseudo-Formalization\" arxiv 2026 math error detection formalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50594151-7cf7-4085-bf65-f851c9d97d2f",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4ecp1NXv8h1o3svG7U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e239955c-689a-44f6-a4ba-9f774cbb08f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CaYRiyZHXraH19CLqMA2eZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 20096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 751,
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

### Tool result

_source line 39 · 2026-05-27T12:21:05.594Z_

<details><summary>↩ Tool result · `toolu_01Ld3bxz7au786scquHL8y6m`</summary>

```text
Web search results for query: ""Pseudo-Formalization" arxiv 2026 math error detection formalization"

Links: [{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"From Euler to Today: Universal Mathematical Fallibility A Large-Scale Computational Analysis of Errors in ArXiv Papers","url":"https://arxiv.org/pdf/2511.10543"},{"title":"arXiv:2506.10558v2 [cs.LO] 30 Jun 2025","url":"https://arxiv.org/pdf/2506.10558"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"}]

Based on the search results, I found a highly relevant paper on arXiv from 2026:

Pseudo-Formalization (PF) is a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language, where a Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language.

The verification process translates a regular natural language proof to Pseudo-Formal format and then verifies each module independently through an algorithm called Block Verification (BV), which pareto-dominates LLM-as-judge baselines on error-finding precision and recall when evaluated on olympiad and research-level mathematics benchmarks.

The researchers also released a research-level proof verification benchmark called ArxivMathGradingBench.

The paper was authored by Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, and Tengyu Ma, and was submitted to arXiv on May 19, 2026 (arXiv:2605.20531).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e239955c-689a-44f6-a4ba-9f774cbb08f6",
  "isSidechain": true,
  "promptId": "6c3f38f9-fafd-47f3-9f71-5e57d73fa4b4",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "233958dd-c65f-48e6-a2d8-0d6974b6f744",
  "sourceToolAssistantUUID": "e239955c-689a-44f6-a4ba-9f774cbb08f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-27T12:21:08.852Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011i68HuKKf5HV9VDUR8H8Mq`</summary>

```json
{
  "query": "arxiv 2605.20531 Barkallah \"Pseudo-Formalization\" \"50%\" error detection ArxivMathGradingBench results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "233958dd-c65f-48e6-a2d8-0d6974b6f744",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4fbLUqo3QRWEwKdmy2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57c27d51-2feb-48e7-a941-933a05cfe5bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vh72mf19ydWRpWDgxid3HL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 20847,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 579
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 20847,
          "cache_creation_input_tokens": 579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 579,
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

_source line 41 · 2026-05-27T12:21:27.117Z_

<details><summary>↩ Tool result · `toolu_011i68HuKKf5HV9VDUR8H8Mq`</summary>

```text
Web search results for query: "arxiv 2605.20531 Barkallah "Pseudo-Formalization" "50%" error detection ArxivMathGradingBench results"

Links: [{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"By Their Fruits You Will Know Them: Comparing Formalizations of Law by the Decisions They Encode","url":"https://arxiv.org/html/2605.25186"},{"title":"Conjecturing: An Overlooked Step in Formal Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.11986"},{"title":"Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal   Proofs","url":"https://arxiv.org/pdf/2210.12283"}]

Great! I found the paper. Now let me search for more specific information about the "50%" error detection results and ArxivMathGradingBench mentioned in your query.

Links: [{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"From Euler to Today: Universal Mathematical Fallibility A Large-Scale Computational Analysis of Errors in ArXiv Papers","url":"https://arxiv.org/pdf/2511.10543"},{"title":"Low-overhead error detection with spacetime codes","url":"https://arxiv.org/html/2504.15725v1"},{"title":"Codes for error detection, good or not good","url":"https://arxiv.org/pdf/cs/0508035"},{"title":"When Variable-Length Codes Meet the Field of Error Detection","url":"https://arxiv.org/pdf/2208.14681"}]

Perfect! I found the information about ArxivMathGradingBench. Now let me search for the specific 50% error detection results mentioned.

Links: [{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"Precision at 50% recall for various combination of sources for... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Precision-at-50-recall-for-various-combination-of-sources-for-commercial-queries_fig4_221654012"},{"title":"Unachievable Region in Precision-Recall Space and Its Effect on   Empirical Evaluation","url":"https://arxiv.org/pdf/1206.4667"},{"title":"Linking Trials to Publications: Enhancing Recall by Identifying Trial Registry Mentions in Full-Text","url":"https://www.medrxiv.org/content/10.1101/2025.06.09.25329285.full.pdf"},{"title":"The MCC approaches the geometric mean of precision and recall as true negatives approach infinity","url":"https://arxiv.org/pdf/2305.00594"},{"title":"Google Scholar as replacement for systematic literature searches: good relative recall and precision are not enough","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3840556/"}]

Based on my web search results, I've found comprehensive information about the paper you're asking about:

## Paper Overview

The paper is titled "Pseudo-Formalization for Automatic Proof Verification" by authors Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, and Tengyu Ma, submitted on May 19, 2026 (arXiv:2605.20531).

## Pseudo-Formalization Approach

The paper proposes Pseudo-Formalization (PF), a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language. A Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language.

## Verification Method and Results

To verify the correctness of a regular natural language proof, an LLM translates it to Pseudo-Formal and then verifies each module independently, an algorithm called Block Verification (BV). 

The results report precision vs recall on identifying the mistaken step/lemma on the Hard2Verify benchmark and real arXiv papers with known errors, with Pseudo-Formalization pareto-dominating LLM-as-judge in both settings, achieving higher precision at every recall level.

## ArxivMathGradingBench Benchmark

To support future work, the authors release their research-level proof verification benchmark ArxivMathGradingBench. The evaluation shows PF+BV pareto-dominates LLM-as-judge baselines on error-finding precision and recall on benchmarks spanning olympiad and research-level mathematics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57c27d51-2feb-48e7-a941-933a05cfe5bd",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "370426d6-b8e9-43e3-bb8c-11d42f4dc12c",
  "sourceToolAssistantUUID": "57c27d51-2feb-48e7-a941-933a05cfe5bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-27T12:21:30.106Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013A3aViinKi5qK2TzZUByHY`</summary>

```json
{
  "query": "Pseudo-Formalization Block Verification precision recall results olympiad research level error identification percentage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "370426d6-b8e9-43e3-bb8c-11d42f4dc12c",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4hBNtbNM2BeSCLzDXB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2650782c-dedb-4d77-a5e9-4bfda97e6f55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AE8Rjs9rfoN8yAzq2vQ75S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1358,
      "cache_read_input_tokens": 21426,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1358
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 21426,
          "cache_creation_input_tokens": 1358,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1358,
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

_source line 43 · 2026-05-27T12:21:40.927Z_

<details><summary>↩ Tool result · `toolu_013A3aViinKi5qK2TzZUByHY`</summary>

```text
Web search results for query: "Pseudo-Formalization Block Verification precision recall results olympiad research level error identification percentage"

Links: [{"title":"Ascribing ground truth performance to annotation blocks","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11176320"},{"title":"When AI Co-Scientists Fail: SPOT-a Benchmark for Automated Verification of Scientific Research","url":"https://arxiv.org/pdf/2505.11855"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"Bounding the Probability of Error for High Precision Recognition","url":"https://arxiv.org/pdf/0907.0418"},{"title":"Detecting Laterality Errors in Combined Radiographic Studies by Enhancing the Traditional Approach With GPT-4o: Algorithm Development and Multisite Internal Validation","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12612642/"},{"title":"BioCreAtIvE Task1A: entity identification with a stochastic tagger","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1869018/"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"}]

The search results don't contain specific information about "Pseudo-Formalization Block Verification" with the exact precision/recall metrics and error identification percentages you're looking for. 

However, the results do include some related research:

- ProcessBench covers competition- or Olympiad-level difficulty math problems, which relates to the olympiad research level mentioned in your query.

- Autoformalization involves converting natural language specifications and pseudo-code into formal logic or verifiable code contracts for rigorous checking, which is conceptually related to formalization and block verification.

The search results don't specifically contain the "Pseudo-Formalization Block Verification" benchmark or its precision/recall results. This appears to be a specialized research topic that may require a more targeted search or may be from a specific recent research paper not yet widely indexed. Would you like me to try a different search query, or do you have more specific details about where this research was published?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2650782c-dedb-4d77-a5e9-4bfda97e6f55",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "f05853a9-2b00-4c18-a343-27c6f3f5b0f2",
  "sourceToolAssistantUUID": "2650782c-dedb-4d77-a5e9-4bfda97e6f55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-27T12:21:43.756Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013ds75yJZCiiqkWvYvT2VWd`</summary>

```json
{
  "query": "arxiv.org 2605.20531 Pseudo-Formalization proof verification results table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f05853a9-2b00-4c18-a343-27c6f3f5b0f2",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4iCSAguQxoigFi7KDw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3640433e-4522-4b38-a07e-ec4580711440",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MbdbZM1LiUzxFW2C4T63J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 22784,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 652
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 22784,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 652,
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

_source line 45 · 2026-05-27T12:21:51.540Z_

<details><summary>↩ Tool result · `toolu_013ds75yJZCiiqkWvYvT2VWd`</summary>

```text
Web search results for query: "arxiv.org 2605.20531 Pseudo-Formalization proof verification results table"

Links: [{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"Verification of Configurable SRA Systems","url":"https://arxiv.org/html/2605.21385"},{"title":"stepproof: step-by-step verification of","url":"https://arxiv.org/pdf/2506.10558"},{"title":"Towards LLM-based Generation of Human-Readable Proofs in Polynomial Formal Verification","url":"https://arxiv.org/pdf/2505.23311"},{"title":"A benchmark for vericoding: formally verified program synthesis","url":"https://arxiv.org/pdf/2509.22908"}]

Based on the search results, I found information about the arXiv paper 2605.20531 titled "Pseudo-Formalization for Automatic Proof Verification." 

The paper proposes Pseudo-Formalization (PF), a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language. To verify the correctness of a regular natural language proof, an LLM translates it to Pseudo-Formal and then verifies each module independently, an algorithm called Block Verification (BV).

The paper evaluates PF+BV on two benchmarks spanning olympiad and research-level mathematics, where it pareto-dominates LLM-as-judge baselines on error-finding precision and recall. The authors release a research-level proof verification benchmark called ArxivMathGradingBench.

However, the search results do not contain the specific details of the results table you're looking for. To access the detailed results table, you would need to view the full paper directly on arXiv at https://arxiv.org/abs/2605.20531 or download the PDF.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3640433e-4522-4b38-a07e-ec4580711440",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "44f7521c-3aa1-4e22-a57b-88b4c1a04a77",
  "sourceToolAssistantUUID": "3640433e-4522-4b38-a07e-ec4580711440",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-27T12:21:55.218Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MSTmNVrGRXLkqtH8bGcUu2`</summary>

```json
{
  "query": "site:arxiv.org \"Safe\" Liu Chengwu \"FormalStep\" accuracy percentage step verification results GPT Claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44f7521c-3aa1-4e22-a57b-88b4c1a04a77",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4iyngRERimxKQRAThk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4eaaaac4-ad4f-44c9-bb2d-afdc06262f81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5d4mbPDZJBYziZpx1LTo4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 23436,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 604
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 23436,
          "cache_creation_input_tokens": 604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 604,
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

_source line 47 · 2026-05-27T12:22:01.581Z_

<details><summary>↩ Tool result · `toolu_01MSTmNVrGRXLkqtH8bGcUu2`</summary>

```text
Web search results for query: "site:arxiv.org "Safe" Liu Chengwu "FormalStep" accuracy percentage step verification results GPT Claude"

Links: [{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/html/2506.04592v1"},{"title":"[2506.04592] Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/abs/2506.04592"},{"title":"MTMCS-Bench: Evaluating Contextual Safety of Multimodal Large Language Models in Multi-Turn Dialogues","url":"https://arxiv.org/html/2601.06757v1"},{"title":"Supporting Software Formal Verification with Large Language Models: An Experimental Study","url":"https://arxiv.org/pdf/2507.04857"},{"title":"—­ -- 上海人工智能实验室 -:=-.==.. Shanghai Artificial Intelligence Laboratory","url":"https://arxiv.org/pdf/2507.18576"},{"title":"DafnyBench: A Benchmark for Formal Software Verification","url":"https://arxiv.org/pdf/2406.08467"},{"title":"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification","url":"https://arxiv.org/pdf/2601.22642"}]

I found the research paper you're looking for! The paper "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification" evaluates the Safe framework across multiple language models and various mathematical datasets, and proposes FormalStep as a benchmark for step correctness theorem proving with 30,809 formal statements.

The work represents the first endeavor to utilize formal mathematical language Lean 4 for verifying natural language content generated by LLMs.

The paper was authored by Chengwu Liu and colleagues from institutions including Peking University, Huawei Noah's Ark Lab, Hong Kong University of Science and Technology, and Hong Kong Polytechnic University. It was published on arXiv on June 5, 2025 (arxiv.org/abs/2506.04592).

However, the specific accuracy percentages and detailed step verification results comparing GPT and Claude models are not visible in the search results provided. To see those specific metrics, you would need to access the full paper on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eaaaac4-ad4f-44c9-bb2d-afdc06262f81",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "e0a3cdf9-7d0a-4cb6-95b0-06b530802c8d",
  "sourceToolAssistantUUID": "4eaaaac4-ad4f-44c9-bb2d-afdc06262f81",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-27T12:22:06.266Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CkV6NATgGPeFwanXnX1Gzf`</summary>

```json
{
  "query": "\"miniF2F-Lean Revisited\" NeurIPS 2025 autoformalization accuracy \"97%\" \"66%\" human evaluation Herald"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0a3cdf9-7d0a-4cb6-95b0-06b530802c8d",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4jj4STnVHh4QfyfYrB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "356ee1c3-d561-4d70-87e9-d78117f02ab5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDqKU1bUc9qhR9w8RhhMhh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 24040,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 698
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 24040,
          "cache_creation_input_tokens": 698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 698,
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

_source line 49 · 2026-05-27T12:22:13.755Z_

<details><summary>↩ Tool result · `toolu_01CkV6NATgGPeFwanXnX1Gzf`</summary>

```text
Web search results for query: ""miniF2F-Lean Revisited" NeurIPS 2025 autoformalization accuracy "97%" "66%" human evaluation Herald"

Links: [{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://openreview.net/pdf?id=KtaHv0YUyh"},{"title":"[Quick Review] miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://liner.com/review/minif2flean-revisited-reviewing-limitations-and-charting-path-forward"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/html/2511.03108v1"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward | OpenReview","url":"https://openreview.net/forum?id=KtaHv0YUyh"},{"title":"miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/pdf/2511.03108"},{"title":"Paper page - miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://huggingface.co/papers/2511.03108"},{"title":"[2511.03108] miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://arxiv.org/abs/2511.03108"},{"title":"(PDF) miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://www.researchgate.net/publication/397322220_miniF2F-Lean_Revisited_Reviewing_Limitations_and_Charting_a_Path_Forward"},{"title":"NeurIPS Poster miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward","url":"https://neurips.cc/virtual/2025/poster/118598"}]

Based on the search results, I found detailed information about the "miniF2F-Lean Revisited" paper presented at NeurIPS 2025:

## Key Findings

When performing human review of the outputs of Herald that LLM has marked as 97% correct, the actual accuracy is much lower at 66%. This discrepancy is a central finding of the paper.

The extensive human evaluation of autoformalization results across five models reveals that their autoformalization accuracy is not as high as reported in the literature, because those reported accuracies are often evaluated by LLMs and not by a human familiar with the formal language.

## End-to-End Pipeline Performance

While the accuracy of the best autoformalization model on miniF2F is reported to be about 97%, and the accuracy of Kimina Prover on miniF2F is 70.8%, the combined accuracy of these models leads to an accuracy of 34.8% after comparing the final proofs with the original problem statements in informal language.

## The Solution: miniF2F-v2

To address these issues, the authors corrected all errors, discrepancies and simplifications in formal and informal statements to present miniF2F-v2, and evaluating the full theorem proving pipeline on miniF2F-v2 leads to the best accuracy of 70%, a significant improvement from the 40% on the original miniF2F.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "356ee1c3-d561-4d70-87e9-d78117f02ab5",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "c8f12356-f636-4cda-9a64-2ab328f6a2c0",
  "sourceToolAssistantUUID": "356ee1c3-d561-4d70-87e9-d78117f02ab5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-27T12:22:17.239Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015zcq4eepuZbmc7MBAL8ayM`</summary>

```json
{
  "query": "Bhatt 2025 \"Grammars of Formal Uncertainty\" authors selective verification SMT error rate reduction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8f12356-f636-4cda-9a64-2ab328f6a2c0",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4kcmSbfbu6aqogqtvL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa1015c7-23f1-466e-a8cf-9a1b8fef6e34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQy5MiJqyMbBytdYfqSnrs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 24738,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 24738,
          "cache_creation_input_tokens": 956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 956,
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

_source line 51 · 2026-05-27T12:22:27.426Z_

<details><summary>↩ Tool result · `toolu_015zcq4eepuZbmc7MBAL8ayM`</summary>

```text
Web search results for query: "Bhatt 2025 "Grammars of Formal Uncertainty" authors selective verification SMT error rate reduction"

Links: [{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/html/2505.20047"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://openreview.net/pdf/1bd62aad3dbda001bef71c29125c2be51f974644.pdf"},{"title":"[2505.20047] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/abs/2505.20047"},{"title":"NeurIPS Poster Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://neurips.cc/virtual/2025/poster/118114"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/grammars-of-formal-uncertainty-when-to-trust-llms-in-automated-reasoning-tasks/"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in ...","url":"https://arxiv.org/pdf/2505.20047"},{"title":"GitHub - DebarghaG/grammars-formal-uncertainty: [NeurIPS 2025] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://github.com/DebarghaG/grammars-formal-uncertainty"}]

Based on the search results, I found the paper "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks" from 2025. Here are the key findings:

## Paper Overview

The paper addresses failure modes and uncertainty quantification (UQ) in LLM-generated formal artifacts. A systematic evaluation of five frontier LLMs reveals Satisfiability Modulo Theories (SMT) based autoformalization's domain-specific impact on accuracy (from +34.8% on logical tasks to -44.5% on factual ones), with known UQ techniques like the entropy of token probabilities failing to identify these errors.

## Key Contributions

The paper introduces a probabilistic context-free grammar (PCFG) framework to model LLM outputs, yielding a refined uncertainty taxonomy. The researchers developed and evaluated 25 uncertainty metrics, revealing a refined taxonomy (epistemic-knowledge, epistemic-procedural, recursive-complexity, capacity-limited).

## Error Rate Reduction via Selective Verification

A lightweight fusion of uncertainty signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention, transforming LLM-driven formalization into a reliable engineering discipline. Uncertainty signals are task-dependent (e.g., grammar entropy for logic, AUROC>0.93).

The paper was presented at NeurIPS 2025 and appears to be authored by researchers including Debargha Ganguly, based on the arXiv metadata.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa1015c7-23f1-466e-a8cf-9a1b8fef6e34",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "b3284ea6-dc07-4186-b8f5-b0ee53f22543",
  "sourceToolAssistantUUID": "fa1015c7-23f1-466e-a8cf-9a1b8fef6e34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-27T12:22:30.857Z_

Let me check if this paper's authors include "Bhatt" specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3284ea6-dc07-4186-b8f5-b0ee53f22543",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4mdDWQBVLCsf6MMKCC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "987f2215-8d26-4406-832e-a2173bfe97d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tbs9sPZv5YebdJ1RAYw1dj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 25694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 875,
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

_source line 53 · 2026-05-27T12:22:31.144Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V4voMgXhTDdmniNLksCJr9`</summary>

```json
{
  "query": "arxiv 2505.20047 \"Grammars of Formal Uncertainty\" full author list Bhatt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "987f2215-8d26-4406-832e-a2173bfe97d6",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4mdDWQBVLCsf6MMKCC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b4f703e-3bd4-47f6-983e-182d9aefee54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tbs9sPZv5YebdJ1RAYw1dj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 25694,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 25694,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 875,
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

_source line 54 · 2026-05-27T12:22:37.050Z_

<details><summary>↩ Tool result · `toolu_01V4voMgXhTDdmniNLksCJr9`</summary>

```text
Web search results for query: "arxiv 2505.20047 "Grammars of Formal Uncertainty" full author list Bhatt"

Links: [{"title":"[2505.20047] Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/abs/2505.20047"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in ...","url":"https://arxiv.org/pdf/2505.20047"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://arxiv.org/html/2505.20047"},{"title":"Paper page - Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://huggingface.co/papers/2505.20047"},{"title":"[2605.01537] The grip of grammar on meaning uncertainty: cross-linguistic evidence, neural correlates, and clinical relevance","url":"https://arxiv.org/abs/2605.01537"},{"title":"A Formal Framework for Uncertainty Analysis of Text Generation with Large Language Models","url":"https://arxiv.org/pdf/2603.26363"}]

Based on the search results, the full author list for arxiv paper 2505.20047 "Grammars of Formal Uncertainty" is: Debargha Ganguly, Vikash Singh, Sreehari Sankar, Biyao Zhang, Xuecen Zhang, Srinivasan Iyengar, Xiaotian Han, Amit Sharma, Shivkumar Kalyanaraman, and Vipin Chaudhary.

Note: The search did not return an author named "Bhatt" on this paper. If you were expecting Bhatt to be an author, you may want to verify the arxiv ID or paper title.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b4f703e-3bd4-47f6-983e-182d9aefee54",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "50718d43-db4f-4631-85d6-cc85d6d19f2d",
  "sourceToolAssistantUUID": "0b4f703e-3bd4-47f6-983e-182d9aefee54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-27T12:22:40.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018hgJMrzLzZtqXNzhnf6kSa`</summary>

```json
{
  "query": "Bhatt 2025 uncertainty guided selective verification SMT solver mathematical reasoning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50718d43-db4f-4631-85d6-cc85d6d19f2d",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4nLQ1RLewnz38ZFTVe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d939e3c5-7bab-4de8-bb7a-bb010b6548d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tNaXkLKm8pavGvRfZFoCW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 26569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 56 · 2026-05-27T12:22:47.133Z_

<details><summary>↩ Tool result · `toolu_018hgJMrzLzZtqXNzhnf6kSa`</summary>

```text
Web search results for query: "Bhatt 2025 uncertainty guided selective verification SMT solver mathematical reasoning LLM"

Links: [{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in ...","url":"https://arxiv.org/pdf/2505.20047"},{"title":"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks","url":"https://openreview.net/attachment?id=QfKpJ00t2L&name=pdf"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.20055v2"},{"title":"LLM-Guided Quantified SMT Solving over Uninterpreted Functions","url":"https://www.arxiv.org/pdf/2601.04675"},{"title":"LLM-Guided Quantified SMT Solving over Uninterpreted Functions","url":"https://arxiv.org/html/2601.04675v1"},{"title":"Uncertainty-Aware Step-wise Verification with Generative Reward Models","url":"https://arxiv.org/pdf/2502.11250"}]

Based on the search results, I found relevant research on this topic. The paper appears to be:

"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks," which was presented at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025) and involves modeling LLM-generated SMT-LIB program distributions with Probabilistic Context-Free Grammars (PCFGs).

The central thesis is that the inherent probabilistic uncertainty in LLM outputs for formal reasoning tasks, particularly when generating formal artifacts like SMT-LIB programs, is a valuable source of information for guiding verification.

A systematic evaluation of five frontier LLMs reveals that Satisfiability Modulo Theories (SMT) based autoformalization has domain-specific impact on accuracy, ranging from +34.8% on logical tasks to -44.5% on factual ones.

A lightweight fusion of uncertainty signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d939e3c5-7bab-4de8-bb7a-bb010b6548d9",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "481fa9f1-833a-4d4b-b622-785b4d8e57cc",
  "sourceToolAssistantUUID": "d939e3c5-7bab-4de8-bb7a-bb010b6548d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-27T12:22:50.486Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JKpXSRbAoS4ALkKpFvLMeo`</summary>

```json
{
  "query": "Bhatt 2025 uncertainty verification math SMT arxiv paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "481fa9f1-833a-4d4b-b622-785b4d8e57cc",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4o5VM5fy84shetrhxM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58814c42-a846-48be-9aa9-f81a27936ff4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LEsXhHecRvFA3mBFpxhDYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 27157,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 27157,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 628,
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

_source line 58 · 2026-05-27T12:22:55.608Z_

<details><summary>↩ Tool result · `toolu_01JKpXSRbAoS4ALkKpFvLMeo`</summary>

```text
Web search results for query: "Bhatt 2025 uncertainty verification math SMT arxiv paper"

Links: [{"title":"arXiv:2505.20047v1 [cs.CL] 26 May 2025","url":"https://arxiv.org/pdf/2505.20047"},{"title":"Conformance Checking with Uncertainty via SMT (Extended Version)","url":"https://arxiv.org/pdf/2206.07461"},{"title":"arXiv:2506.07635v2 [cs.LO] 19 Jun 2025","url":"https://arxiv.org/pdf/2506.07635"},{"title":"Uncertainty-Aware Step-wise Verification with Generative Reward Models","url":"https://arxiv.org/pdf/2502.11250"},{"title":"Efficient Volume Computation for SMT Formulas","url":"https://arxiv.org/pdf/2508.09934"}]

Based on the search results, I found a relevant paper that appears to match your query. The paper discusses how probabilistic uncertainty in LLM outputs for formal reasoning tasks, particularly when generating SMT-LIB programs, can be valuable for guiding verification, and demonstrates how to systematically capture and analyze this output uncertainty by modeling LLM-generated SMT-LIB program distributions with Probabilistic Context-Free Grammars (PCFGs).

The paper is available on arXiv (2505.20047) and appears to be a preprint under review. It addresses the use of uncertainty quantification in mathematical and formal verification workflows involving SMT solvers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58814c42-a846-48be-9aa9-f81a27936ff4",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "c49cb4d9-a0a2-4553-b69c-7fe924f47479",
  "sourceToolAssistantUUID": "58814c42-a846-48be-9aa9-f81a27936ff4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-27T12:22:59.415Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EQuATDajTW3LCFNE3VNNvc`</summary>

```json
{
  "query": "Shuhui Qu 2026 \"Adaptive Test-Time Compute\" \"44%\" MATH Llama verifier arxiv 2602.03975"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c49cb4d9-a0a2-4553-b69c-7fe924f47479",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4ohhh4uREy6TqCnZ1V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52a05798-e8e6-4031-8171-e65427a019a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQRyZm4w8RftzfXWrpCdvg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 27785,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 469
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 27785,
          "cache_creation_input_tokens": 469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 469,
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

_source line 60 · 2026-05-27T12:23:05.810Z_

<details><summary>↩ Tool result · `toolu_01EQuATDajTW3LCFNE3VNNvc`</summary>

```text
Web search results for query: "Shuhui Qu 2026 "Adaptive Test-Time Compute" "44%" MATH Llama verifier arxiv 2602.03975"

Links: [{"title":"[2602.03975] Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/abs/2602.03975"},{"title":"What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/pdf/2602.01070"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/html/2602.03975"},{"title":"Strategic Scaling of Test-Time Compute: A Bandit Learning Approach","url":"https://arxiv.org/pdf/2506.12721"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over","url":"https://arxiv.org/pdf/2602.03975"},{"title":"What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/html/2602.01070"}]

I found the paper you're looking for! Here's what I found:

arxiv:2602.03975 is titled "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure" by Shuhui Qu, submitted on February 3, 2026.

The paper proposes a state-level selective verification framework that combines deterministic feasibility gating over a structured move interface, pre-verification ranking using a hybrid of learned state-distance and residual scoring, and adaptive allocation of verifier calls based on local uncertainty.

The paper addresses the problem that test-time computation has become a primary driver of progress in large language model (LLM) reasoning, but is increasingly bottlenecked by expensive verification.

The paper focuses on verification-cost-limited reasoning and how to efficiently allocate verification effort across intermediate states in LLM reasoning tasks, including MATH benchmarks. However, the search results don't contain the specific "44%" performance metric you mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52a05798-e8e6-4031-8171-e65427a019a6",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "0d5e3448-cd0a-4be3-b8b6-d51d8bbb9fe1",
  "sourceToolAssistantUUID": "52a05798-e8e6-4031-8171-e65427a019a6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-27T12:23:12.288Z_

Now let me also check the authorship details for the "Mu et al" reference and the Hard2Verify authorship.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d5e3448-cd0a-4be3-b8b6-d51d8bbb9fe1",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4pVWk3mjezFcmNWgkE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2802930b-d88a-49d3-8e94-4785e70b60eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEjCygkUuN72q2KMLDocL1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 28254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 627,
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

_source line 62 · 2026-05-27T12:23:12.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N5JV5hoNSfXbd6yDNLqC6z`</summary>

```json
{
  "query": "Hard2Verify arxiv 2510.13744 authors full list Zheng Salesforce"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2802930b-d88a-49d3-8e94-4785e70b60eb",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4pVWk3mjezFcmNWgkE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6122f0a7-168f-4f51-8cb9-6bde453032ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEjCygkUuN72q2KMLDocL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 28254,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 627
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 101,
          "cache_read_input_tokens": 28254,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 627,
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

_source line 63 · 2026-05-27T12:23:22.671Z_

<details><summary>↩ Tool result · `toolu_01N5JV5hoNSfXbd6yDNLqC6z`</summary>

```text
Web search results for query: "Hard2Verify arxiv 2510.13744 authors full list Zheng Salesforce"

Links: [{"title":"(PDF) Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math","url":"https://www.researchgate.net/publication/396517985_Hard2Verify_A_Step-Level_Verification_Benchmark_for_Open-Ended_Frontier_Math"},{"title":"Preprint | Salesforce AI Research HARD2VERIFY: A STEP-LEVEL VERIFICATION","url":"https://arxiv.org/pdf/2510.13744"},{"title":"[2510.13744] Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math","url":"https://arxiv.org/abs/2510.13744"},{"title":"[2510.13744v1] Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math","url":"https://arxiv.org/abs/2510.13744v1"},{"title":"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13744v1"}]

Based on the search results, the authors of the Hard2Verify paper (arXiv:2510.13744) are: Shrey Pandit, Austin Xu, Xuan-Phi Nguyen, Yifei Ming, Caiming Xiong, and Shafiq Joty.

The paper was submitted on October 15, 2025 and is a human-annotated, step-level verification benchmark produced with over 500 hours of human labor.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6122f0a7-168f-4f51-8cb9-6bde453032ea",
  "isSidechain": true,
  "promptId": "28415887-e53e-4d69-9605-a560114deea1",
  "agentId": "a9a2f7dc93ea0cae4",
  "type": "user",
  "uuid": "ccd5157b-a010-4748-a78a-816048646e5f",
  "sourceToolAssistantUUID": "6122f0a7-168f-4f51-8cb9-6bde453032ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-27T12:24:25.122Z_

Now I have all the information needed. Here is my comprehensive report:

---

## Paper Verification Report

### 1. "Pseudo-Formalization" by Barkallah et al., May 2026

**FOUND.** The paper is titled "Pseudo-Formalization for Automatic Proof Verification" by Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, and Tengyu Ma. It was posted to arXiv on May 19, 2026 (arXiv:2605.20531). Note the first author's first name is **Slim**, not a different Barkallah.

- **Venue/Year:** arXiv preprint, May 2026 (no confirmed conference venue yet)
- **Key results:** Pseudo-Formalization (PF) is a proof format combining formal modularity with natural language flexibility. Block Verification (BV) verifies each module independently. PF+BV Pareto-dominates LLM-as-judge baselines on error-finding precision and recall across olympiad and research-level math benchmarks. The authors release **ArxivMathGradingBench**, a research-level proof verification benchmark.
- **On the ~50% error detection claim:** I could not confirm the specific "~50%" number from search results alone. The paper reports precision-recall curves where PF+BV dominates baselines, but the exact 50% figure would require reading the full paper tables.

Sources: [arXiv abs](https://arxiv.org/abs/2605.20531), [arXiv HTML](https://arxiv.org/html/2605.20531)

---

### 2. "Safe" by Liu et al., ACL 2025

**FOUND.** The paper is "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification" by Chengwu Liu et al. (Peking University, Huawei Noah's Ark Lab, HKUST, HK PolyU).

- **Venue/Year:** ACL 2025 Main Conference (published June 2025, arXiv:2506.04592)
- **Key results:** First work to use Lean 4 for verifying LLM-generated natural language reasoning step by step. Proposes **FormalStep** benchmark with 30,809 formal statements. The framework auto-formalizes each step, validates the Lean 4 theorem via Lean REPL, attempts proof with an LLM-based prover, then verifies. Demonstrates "significant performance improvement" across multiple LLMs and math datasets.
- **On the ~80% proof success claim:** The specific "~80%" figure was not confirmed from search snippets. The full paper's tables would need to be consulted for exact proof success rates on FormalStep.

Sources: [ACL Anthology](https://aclanthology.org/2025.acl-long.594/), [GitHub](https://github.com/liuchengwucn/Safe), [arXiv](https://arxiv.org/abs/2506.04592)

---

### 3. "Hard2Verify" -- Zheng et al., 2025

**FOUND, but authorship correction needed.** The paper is "Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math" (arXiv:2510.13744, October 2025). It is from **Salesforce AI Research** and authored by **Shrey Pandit, Austin Xu, Xuan-Phi Nguyen, Yifei Ming, Caiming Xiong, and Shafiq Joty** -- NOT "Zheng et al." The name "Zheng" may be confused with the ProcessBench paper (Zheng et al., 2024) which is cited by Hard2Verify.

- **Venue/Year:** arXiv preprint, October 2025 (500+ hours of human annotation)
- **Key results:** The specific numbers you cited are **confirmed**: Qwen2.5-Math-PRM-72B drops from **78.3** on ProcessBench to **37.3** on Hard2Verify for error identification. This demonstrates that existing PRMs trained on competition-level math fail dramatically on frontier/research-level math.

Sources: [arXiv abs](https://arxiv.org/abs/2510.13744), [arXiv HTML](https://arxiv.org/html/2510.13744v1), [ResearchGate](https://www.researchgate.net/publication/396517985_Hard2Verify_A_Step-Level_Verification_Benchmark_for_Open-Ended_Frontier_Math)

---

### 4. "miniF2F-Lean Revisited" 2025

**FOUND.** The paper is "miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward" (arXiv:2511.03108).

- **Venue/Year:** **NeurIPS 2025** (poster)
- **Key results (confirmed numbers):**
  - Herald autoformalization reports **97%** accuracy when evaluated by LLM, but human review reveals actual accuracy is only **66%** -- a 31-point gap
  - Kimina Prover achieves **70.8%** on miniF2F
  - Combined end-to-end pipeline accuracy drops to **34.8%** when comparing final proofs against original informal problem statements
  - On corrected **miniF2F-v2**, best accuracy improves to **70%** (up from 40% on original miniF2F)

Sources: [arXiv](https://arxiv.org/abs/2511.03108), [NeurIPS 2025 poster](https://neurips.cc/virtual/2025/poster/118598), [OpenReview](https://openreview.net/forum?id=KtaHv0YUyh)

---

### 5. Bhatt et al., 2025 -- Uncertainty-guided selective verification with SMT

**NOT CONFIRMED as "Bhatt et al."** The closest matching paper is "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks" (arXiv:2505.20047, May 2025), presented at **NeurIPS 2025**. However, the authors are **Debargha Ganguly, Vikash Singh, Sreehari Sankar, Biyao Zhang, Xuecen Zhang, Srinivasan Iyengar, Xiaotian Han, Amit Sharma, Shivkumar Kalyanaraman, and Vipin Chaudhary** -- no author named "Bhatt" appears.

- **Venue/Year:** NeurIPS 2025
- **Key results:** Evaluates 5 frontier LLMs on SMT-LIB autoformalization. SMT accuracy varies by domain: +34.8% on logical tasks, -44.5% on factual ones. Introduces PCFG framework with 25 uncertainty metrics. Lightweight fusion of uncertainty signals enables selective verification that cuts error rates by **14-100%** with minimal abstention. Grammar entropy achieves AUROC > 0.93 for logic tasks.
- **Assessment:** The topic matches exactly (uncertainty-guided selective verification with SMT), but the authorship "Bhatt et al." does not match. Either the attribution is incorrect, or there is a different paper by Bhatt that I could not find.

Sources: [arXiv](https://arxiv.org/abs/2505.20047), [NeurIPS poster](https://neurips.cc/virtual/2025/poster/118114), [Microsoft Research](https://www.microsoft.com/en-us/research/publication/grammars-of-formal-uncertainty-when-to-trust-llms-in-automated-reasoning-tasks/), [GitHub](https://github.com/DebarghaG/grammars-formal-uncertainty)

---

### 6. Mu et al., 2026 -- Adaptive verification allocation, 44% fewer verifier calls on MATH

**FOUND, but authorship correction needed.** The paper is "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure" (arXiv:2602.03975, February 2026). The author listed is **Shuhui Qu** (Stanford University) -- not "Mu et al."

- **Venue/Year:** arXiv preprint, February 2026
- **Key results:** Proposes state-level selective verification combining deterministic feasibility gating, hybrid pre-verification ranking, and adaptive verifier call allocation based on local uncertainty. Achieves higher accuracy than best-of-N, majority voting, and beam search while using **44% fewer verifier calls** on the MATH benchmark with Llama 3.2 1B as the generator and a PRM as verifier.
- **Assessment:** The "44% fewer verifier calls" claim is confirmed, but the authorship is "Qu" not "Mu."

Sources: [arXiv abs](https://arxiv.org/abs/2602.03975), [arXiv HTML](https://arxiv.org/html/2602.03975)

---

## Baseline Numbers

### Best PRM accuracy on research-level math proofs
- **ProcessBench SOTA:** Qwen2.5-Math-PRM-72B achieves **78.3** on ProcessBench (competition-level), but drops to **37.3** on Hard2Verify (frontier/research-level)
- **R-PRM** surpasses baselines by **11.9** and **8.5** F1 points on ProcessBench and PRMBench respectively
- **ThinkPRM** beats PRM800K-trained discriminative verifiers by **8%** and **4.5%** on GPQA-Diamond and LiveCodeBench
- Bottom line: No PRM achieves reliable accuracy on research-level proofs; the best models barely exceed 37% on frontier math

### Safe's formal verification success rate and cost overhead
- Exact success rate percentage (the "~80%" claim) was **not confirmed** from search results. The paper reports "significant performance improvement" but specific numbers require reading the full paper tables. The FormalStep benchmark contains 30,809 formal statements. Cost overhead details were not retrievable from web search.

### State of the art on ArxivMathGradingBench
- This benchmark was **just released** with the Pseudo-Formalization paper (May 2026). PF+BV Pareto-dominates LLM-as-judge baselines. No other published work appears to report results on it yet, making the Barkallah et al. results the current (and only) SOTA.

### Autoformalization success rates (NL to Lean 4)
- **LLM-judged autoformalization:** up to 97% (Herald on miniF2F) -- but this is **inflated**
- **Human-judged autoformalization:** only **66%** (same Herald outputs reviewed by humans)
- **End-to-end (autoformalize + prove + verify):** **34.8%** on original miniF2F
- **On corrected miniF2F-v2:** **70%** best accuracy
- **Other benchmarks:** 68.4% pass rate reported on miniF2F by other methods; 87% task success rate for agentic proof automation on System Capless (Xu & Odersky, 2026)

---

## Summary of Issues Found

Three of the six papers have **incorrect author attributions** in your list:
1. **Hard2Verify** is by Pandit, Xu, Nguyen et al. (Salesforce), not "Zheng et al." (Zheng wrote ProcessBench, which Hard2Verify cites)
2. **"Bhatt et al."** does not match any found paper. The closest match (Ganguly et al., "Grammars of Formal Uncertainty") has no author named Bhatt
3. **"Mu et al."** does not match -- the adaptive verification paper is by **Shuhui Qu** (Stanford), not "Mu"

All six papers' core claims and topics are real and verifiable, but the specific quantitative claims for Safe (~80%) and Pseudo-Formalization (~50%) could not be confirmed or denied from web search alone -- the full paper PDFs would need to be read.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccd5157b-a010-4748-a78a-816048646e5f",
  "isSidechain": true,
  "agentId": "a9a2f7dc93ea0cae4",
  "requestId": "req_011CbT4qhUrTosLLH825qTxf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67ce8e92-bfc0-47ec-8e76-307c6c14189e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d50cf128-39c2-46f2-abb0-ee1a4faf1620",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PkroVGvSBuQ5zZ1E9cL89",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 28881,
      "output_tokens": 2969,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 552
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2969,
          "cache_read_input_tokens": 28881,
          "cache_creation_input_tokens": 552,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 552,
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
