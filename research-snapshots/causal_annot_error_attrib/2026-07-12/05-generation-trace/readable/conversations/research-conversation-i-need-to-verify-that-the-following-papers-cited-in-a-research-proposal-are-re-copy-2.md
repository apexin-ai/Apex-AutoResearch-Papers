# Research conversation: I need to verify that the following papers cited in a research proposal are real and get their exact details. Use WebSea

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a48da4d30e1295305.jsonl`
- **Structured JSON:** [`2af8046f4046d5fab581.json`](../../sessions/2a/2af8046f4046d5fab581.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-19T18:25:05.047Z_

I need to verify that the following papers cited in a research proposal are real and get their exact details. Use WebSearch for each one.

Papers to verify:
1. "Ji et al. (EMNLP 2025)" — about verbal uncertainty being governed by a single linear direction in representation space. Search: "Ji EMNLP 2025 verbal uncertainty linear direction representation"
2. "Joshi et al. (EMNLP 2025) LACE" — about intermediate layers encoding better-calibrated signals, adaptive ensemble of intermediate layers. Search: "Joshi LACE EMNLP 2025 calibration intermediate layers"
3. "Zhou et al. (arXiv 2510.03136)" — confirmed 5x ECE gap across 100+ languages and 6 model families, LLaMA-3 showing 23.1% vs 4.6% ECE. Search: "arXiv 2510.03136 Zhou calibration multilingual" and also "Zhou multilingual calibration ECE gap 100 languages LLM"
4. "MKA (ICLR Workshop 2025)" — cross-lingual consensus for abstention. Search: "MKA ICLR 2025 cross-lingual consensus abstention multilingual"
5. "Middle-layer representation alignment (ACL 2025)" — strongest cross-lingual alignment at intermediate layers. Search: "ACL 2025 middle layer cross-lingual representation alignment multilingual"

For each paper, report:
- Whether it's verifiably real (found on the web)
- Exact title, authors, venue, year
- The key finding relevant to this research
- If NOT found, say so clearly

Also search for any additional highly relevant papers I should cite:
6. WebSearch: "representation engineering calibration LLM linear probe 2024 2025"
7. WebSearch: "multilingual LLM calibration survey benchmark 2025"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "a34e7094-7bba-4339-b39a-9d236e79138e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T18:25:05.052Z_

```json
{
  "parentUuid": "a34e7094-7bba-4339-b39a-9d236e79138e",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
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
  "uuid": "babf47cf-a186-41ad-9fad-d79a32fe2399",
  "timestamp": "2026-05-19T18:25:05.052Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T18:25:05.053Z_

```json
{
  "parentUuid": "babf47cf-a186-41ad-9fad-d79a32fe2399",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d0ea57b3-37cc-4f85-97e9-d99b600a0dae",
  "timestamp": "2026-05-19T18:25:05.053Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T18:25:07.533Z_



I'll search for all these papers in parallel to verify their existence and get exact details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0ea57b3-37cc-4f85-97e9-d99b600a0dae",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCPx9W6h9ybb31CJnnHt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4da115b3-c507-42c5-b0ed-5f6e978a2d12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmBFQyLxsJHhXZTgFpBdDj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1763,
      "cache_read_input_tokens": 7409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1763,
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

_source line 5 · 2026-05-19T18:25:08.024Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017ApDzpv5wdxowyHpNKWy6k`</summary>

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
  "parentUuid": "4da115b3-c507-42c5-b0ed-5f6e978a2d12",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCPx9W6h9ybb31CJnnHt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d588c49-e515-48e0-9660-fb41b9944e37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmBFQyLxsJHhXZTgFpBdDj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1763,
      "cache_read_input_tokens": 7409,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1763
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 7409,
          "cache_creation_input_tokens": 1763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1763,
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

_source line 6 · 2026-05-19T18:25:08.029Z_

<details><summary>↩ Tool result · `toolu_017ApDzpv5wdxowyHpNKWy6k`</summary>

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
  "parentUuid": "6d588c49-e515-48e0-9660-fb41b9944e37",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "f79d979a-e986-4476-beea-28134f59c3bc",
  "sourceToolAssistantUUID": "6d588c49-e515-48e0-9660-fb41b9944e37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T18:25:10.428Z_



Now I'll run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f79d979a-e986-4476-beea-28134f59c3bc",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCPxNTDcF2W4hXam5aLo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcc1270c-0bb4-4d4b-8986-f0d771ab904f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011X2Ja3WoC3rTuND5RL2kRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 9172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 625,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T18:25:10.597Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DehtnpunqLH6JEqinSzmqr`</summary>

```json
{
  "query": "Ji EMNLP 2025 verbal uncertainty linear direction representation space"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc1270c-0bb4-4d4b-8986-f0d771ab904f",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCPxNTDcF2W4hXam5aLo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a936fa5c-a91b-4799-9b85-61f8d75aca7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011X2Ja3WoC3rTuND5RL2kRR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 9172,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 625
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 79,
          "cache_read_input_tokens": 9172,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 625,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T18:25:20.327Z_

<details><summary>↩ Tool result · `toolu_01DehtnpunqLH6JEqinSzmqr`</summary>

```text
Web search results for query: "Ji EMNLP 2025 verbal uncertainty linear direction representation space"

Links: [{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce   Hallucinations","url":"https://arxiv.org/pdf/2503.14477"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"}]

Based on the search results, here's what I found about the paper:

The paper "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" by Ziwei Ji and colleagues was published at EMNLP 2025 in Suzhou, China.

**Key Findings:**

The research finds that "verbal uncertainty" is governed by a single linear feature in the representation space of LLMs, and shows that this has only moderate correlation with the actual "semantic uncertainty" of the model.

**Main Contributions:**

The researchers show that, similarly to refusal and other behaviors, the degree of uncertainty expressed by a model is mediated by a single direction, which they call the "Verbal Uncertainty Feature" (VUF). Specifically, they demonstrate that the hidden states of input questions answered with low and high verbal uncertainty can be linearly separated, which allows them to use contrastive pairs to identify a single difference-in-means direction that can be intervened upon to control model expression of uncertainty.

**Results:**

By intervening on verbal uncertainty at inference time, they reduce hallucinations on short-form answers, achieving an average relative reduction of 32%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a936fa5c-a91b-4799-9b85-61f8d75aca7d",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "d9280ef5-f201-436f-a527-e336489e5b49",
  "sourceToolAssistantUUID": "a936fa5c-a91b-4799-9b85-61f8d75aca7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T18:25:22.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018NBF9ZuDftv6dJQ3dsQ1be`</summary>

```json
{
  "query": "Joshi LACE EMNLP 2025 calibration intermediate layers ensemble"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9280ef5-f201-436f-a527-e336489e5b49",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCPyGqQQ1YL4uSmgEPHX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "246afc49-775f-4e09-a797-53edc9956f57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxoG7T8Ru6oymknDQJopUB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1384,
      "cache_read_input_tokens": 9172,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1384
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 9172,
          "cache_creation_input_tokens": 1384,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1384,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T18:25:29.538Z_

<details><summary>↩ Tool result · `toolu_018NBF9ZuDftv6dJQ3dsQ1be`</summary>

```text
Web search results for query: "Joshi LACE EMNLP 2025 calibration intermediate layers ensemble"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.742/"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=CUS9OTCGdt"},{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"Accepted Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/ind_papers/"}]

Based on the search results, I found information about work related to your query. Here are the relevant findings:

The paper "Calibration Across Layers: Understanding Calibration Evolution in LLMs" by Joshi et al. was presented at EMNLP 2025 in Suzhou, China. The findings suggest that calibration is a distributed phenomenon, shaped throughout the network's forward pass, not just in its final projection, providing new insights into how confidence-regulating mechanisms operate within LLMs.

Additionally, there appears to be related work on multilingual calibration: The first large-scale, systematic studies of multilingual calibration across six model families and over 100 languages reveal that non-English languages suffer from systematically worse calibration. The research introduces a suite of training-free methods, including Language-Aware Confidence Ensemble (LACE), which adaptively selects an optimal ensemble of layers for each specific language. The layer-wise analysis uncovers that late-intermediate layers consistently offer a more reliable and better-calibrated signal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "246afc49-775f-4e09-a797-53edc9956f57",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "e1cd3ab5-3f2c-4c4f-b70d-d646aaef6137",
  "sourceToolAssistantUUID": "246afc49-775f-4e09-a797-53edc9956f57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-19T18:25:31.621Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PVGRd62QvHMTyaUEDRVm5z`</summary>

```json
{
  "query": "arXiv 2510.03136 Zhou calibration multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1cd3ab5-3f2c-4c4f-b70d-d646aaef6137",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCPyxBmVraBkgygv61uY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9e3cb36-f10d-4980-9ab0-f5cd5749801b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4C7VwYc3K25NfjhtxLGXj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 10556,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 10556,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 762,
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

_source line 13 · 2026-05-19T18:25:37.769Z_

<details><summary>↩ Tool result · `toolu_01PVGRd62QvHMTyaUEDRVm5z`</summary>

```text
Web search results for query: "arXiv 2510.03136 Zhou calibration multilingual"

Links: [{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136"},{"title":"Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLMs","url":"https://arxiv.org/html/2601.18306v1"},{"title":"Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM","url":"https://arxiv.org/pdf/2601.18306"},{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/pdf/2311.08669"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/pdf/2601.01362"}]

Based on the search results, here's what I found about arXiv paper 2510.03136:

## Paper Overview

The paper is titled "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models" by Ej Zhou and colleagues from the Language Technology Lab at the University of Cambridge.

## Key Findings

The research conducts the first large-scale, systematic studies of multilingual calibration across six model families and over 100 languages, revealing that non-English languages suffer from systematically worse calibration.

## Main Contributions

The work investigates the model's internal representations and finds that the final layer, biased by English-centric training, provides a poor signal for multilingual confidence. In contrast, their layer-wise analysis uncovers a key insight that late-intermediate layers consistently offer a more reliable and better-calibrated signal.

The paper introduces a suite of training-free methods, including Language-Aware Confidence Ensemble (LACE), which adaptively selects an optimal ensemble of layers.

The paper was submitted on October 3, 2025, and addresses the previously under-explored area of confidence calibration in multilingual Large Language Models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9e3cb36-f10d-4980-9ab0-f5cd5749801b",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "7d679417-68ae-488a-92e7-f877a9fddcdb",
  "sourceToolAssistantUUID": "e9e3cb36-f10d-4980-9ab0-f5cd5749801b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T18:25:39.963Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QCmuFM5wmGKyXSHBXfoDz5`</summary>

```json
{
  "query": "MKA ICLR 2025 cross-lingual consensus abstention multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d679417-68ae-488a-92e7-f877a9fddcdb",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCPzZQLQPZ8U65CyoZfG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dc744f9-64b5-4701-bc2c-54244649b073",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zTqex6xtUQVveLzP2gh8Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 684,
      "cache_read_input_tokens": 11318,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 11318,
          "cache_creation_input_tokens": 684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 684,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T18:25:50.419Z_

<details><summary>↩ Tool result · `toolu_01QCmuFM5wmGKyXSHBXfoDz5`</summary>

```text
Web search results for query: "MKA ICLR 2025 cross-lingual consensus abstention multilingual"

Links: [{"title":"MKA: Leveraging Cross-Lingual Consensus for Model Abstention | OpenReview","url":"https://openreview.net/forum?id=7z49r7RhP2"},{"title":"MKA: Leveraging Cross-Lingual Consensus for Model Abstention Sharad Duwal","url":"https://arxiv.org/pdf/2503.23687"},{"title":"[2503.23687] MKA: Leveraging Cross-Lingual Consensus for Model Abstention","url":"https://arxiv.org/abs/2503.23687"},{"title":"[Literature Review] MKA: Leveraging Cross-Lingual Consensus for Model Abstention","url":"https://www.themoonlight.io/en/review/mka-leveraging-cross-lingual-consensus-for-model-abstention"},{"title":"MKA: LEVERAGING CROSS-LINGUAL CONSENSUS","url":"https://openreview.net/pdf?id=7z49r7RhP2"},{"title":"MKA: Leveraging Cross-Lingual Consensus for Model Abstention","url":"https://arxiv.org/html/2503.23687v1"},{"title":"Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation","url":"https://arxiv.org/html/2605.12515"}]

Based on the search results, here's what I found about MKA and ICLR 2025:

## MKA: Leveraging Cross-Lingual Consensus for Model Abstention

MKA (Multilingual Knowledge Abstention) is a pipeline that improves the reliability of Large Language Models (LLMs) by leveraging their multilingual knowledge to determine when to abstain from answering a question.

### How It Works

The MKA pipeline takes a question in a target language, translates it to related auxiliary languages, prompts a multilingual model to get responses in these languages, translates them back to the target language, and then uses semantic similarity of the responses to calibrate the model's confidence based on whether it should abstain.

The confidence score is calculated as the average cosine similarity between the sentence embedding of the selected answer and the sentence embeddings of the other answers.

### Results

The pipeline showed an accuracy improvement of 71.2% for Bengali over a baseline performance without the pipeline, and even a high-resource language like English sees a 15.5% improvement.

### Publication Status

The paper was published on March 5, 2025 (last modified March 31, 2025) as part of the ICLR 2025 Workshop BuildingTrust.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dc744f9-64b5-4701-bc2c-54244649b073",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "2d6f82f6-1bff-4f82-b1f4-60824a0d8ab6",
  "sourceToolAssistantUUID": "4dc744f9-64b5-4701-bc2c-54244649b073",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T18:25:52.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013daPqxfsDQtTas5YH9nX5T`</summary>

```json
{
  "query": "ACL 2025 middle layer cross-lingual representation alignment multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d6f82f6-1bff-4f82-b1f4-60824a0d8ab6",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ1VWCuTiG19nSXRoFQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07ba3913-fbdc-4277-9880-b69bc165d6d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ybg8jJUdNMTC3nqLqrAByP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 11318,
      "output_tokens": 67,
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
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 11318,
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
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T18:25:59.305Z_

<details><summary>↩ Tool result · `toolu_013daPqxfsDQtTas5YH9nX5T`</summary>

```text
Web search results for query: "ACL 2025 middle layer cross-lingual representation alignment multilingual"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.778/"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual ...","url":"https://aclanthology.org/2025.acl-long.778.pdf"},{"title":"Proceedings of the 5th Workshop on Multilingual Representation Learning (MRL 2025) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.mrl-main/"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"},{"title":"Cross-Lingual Representation Alignment Through Contrastive Image-Caption Tuning - ACL Anthology","url":"https://aclanthology.org/2025.acl-short.95/"},{"title":"[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/abs/2502.14830"},{"title":"AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.328/"}]

I found relevant research on this topic. Here are the key results:

## Primary ACL 2025 Paper

Through analysis of LLM internal representations from over 1,000+ language pairs, researchers discovered that middle layers exhibit the strongest potential for cross-lingual alignment. The paper "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs" by Liu and Niehues was published at the 63rd Annual Meeting of the Association for Computational Linguistics in 2025.

## Key Findings and Methods

The researchers proposed a middle-layer alignment objective integrated into task-specific training. Experiments on slot filling, machine translation, and structured text generation showed consistent improvements in cross-lingual transfer, especially to lower-resource languages.

The method is robust to the choice of alignment languages and generalizes to languages unseen during alignment, and separately trained alignment modules can be merged with existing task-specific modules, improving cross-lingual capabilities without full re-training.

## Technical Approach

Activations from the middle layer are extracted for parallel texts and mean-pooled over sequence. This approach directly targets the layer found to have the strongest cross-lingual alignment potential.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07ba3913-fbdc-4277-9880-b69bc165d6d7",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "cc8fc350-5c18-4afb-86cb-a4d01ade631e",
  "sourceToolAssistantUUID": "07ba3913-fbdc-4277-9880-b69bc165d6d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T18:26:01.629Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HDPm6o9dysmVgF6adAZhuZ`</summary>

```json
{
  "query": "representation engineering calibration LLM linear probe 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc8fc350-5c18-4afb-86cb-a4d01ade631e",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ29ViMAVF39Q4eSUfi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ceb0ee22-4ee0-4a25-852e-4eea51eb78f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118YCV3urQ6k3QEQJPzwYqH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 12769,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 818
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 12769,
          "cache_creation_input_tokens": 818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 818,
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

_source line 19 · 2026-05-19T18:26:11.686Z_

<details><summary>↩ Tool result · `toolu_01HDPm6o9dysmVgF6adAZhuZ`</summary>

```text
Web search results for query: "representation engineering calibration LLM linear probe 2024 2025"

Links: [{"title":"Representation Engineering for Large-Language Models: Survey and Research Challenges","url":"https://arxiv.org/html/2502.17601v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ca6980a3dba7fb3e4e66925656dba68b-Paper-Conference.pdf"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"},{"title":"Improving Preference Extraction In LLMs By Identifying Latent Knowledge   Through Classifying Probes","url":"https://arxiv.org/pdf/2503.17755"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"}]

I found several recent papers related to representation engineering, calibration, and linear probes in LLMs from 2024-2025:

1. **Representation Engineering Survey (February 2025)**: Probes have been applied to investigate various LLM representations including biases, jailbreak mechanisms, and linguistic properties, with probes shown to encode uncertainty, hierarchical linguistic structure, and model knowledge.

2. **Instruction-Following Representation Engineering (ICLR 2025)**: Linear probing is applied to analyze internal representations from success and failure cases to identify instruction-following dimensions, with probes tested on unseen tasks and instruction types, and representation engineering then used to shift failure cases.

3. **LLM Judge Calibration with Linear Probes (2025)**: The LLM-as-judge paradigm has become prevalent in modern AI development, with reasoning-capable models generating reasoning traces before verdicts for higher accuracy and transparency. The paper specifically focuses on using linear probes for fast and reliable uncertainty estimation in LLM judges.

4. **Preference Extraction via Probing (2025)**: Probing methods assess the extent to which language model representations encode specific knowledge, typically using a supervised classifier trained to extract information, with linear probing particularly valued for its efficiency and interpretability.

5. **Calibration Through Representation Stability (2025)**: Calibration in LLMs refers to when expressed confidence in a prediction aligns with the empirical likelihood of that prediction being correct.

These papers show active research momentum in using linear probes for understanding and calibrating LLM representations in 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceb0ee22-4ee0-4a25-852e-4eea51eb78f8",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "e478abb0-3e81-40a1-ac68-0b328f26f4f8",
  "sourceToolAssistantUUID": "ceb0ee22-4ee0-4a25-852e-4eea51eb78f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T18:26:14.868Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SHtycaNaK4QUpcCkBETM8z`</summary>

```json
{
  "query": "multilingual LLM calibration survey benchmark 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e478abb0-3e81-40a1-ac68-0b328f26f4f8",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ34Rtgw6QLrBqJ7K2k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "353a426b-27f5-483d-a600-d1c451450f53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQQSUvQWBNVeaptZkBCVSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 13587,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 13587,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 762,
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

_source line 21 · 2026-05-19T18:26:21.528Z_

<details><summary>↩ Tool result · `toolu_01SHtycaNaK4QUpcCkBETM8z`</summary>

```text
Web search results for query: "multilingual LLM calibration survey benchmark 2025"

Links: [{"title":"Multilingual LLM Evaluation","url":"https://www.emergentmind.com/topics/multilingual-evaluation-of-large-language-models"},{"title":"GitHub - CSHaitao/Awesome-LLMs-as-Judges: The official repo for paper, LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods. · GitHub","url":"https://github.com/CSHaitao/Awesome-LLMs-as-Judges"},{"title":"On the Calibration of Multilingual Question Answering LLMs","url":"https://arxiv.org/pdf/2311.08669"},{"title":"2025-4-23 The Bitter Lesson Learned from 2,000+ Multilingual Benchmarks","url":"https://arxiv.org/pdf/2504.15521"},{"title":"LLM evaluation benchmarks and safety datasets for 2025 | RAIL Score Knowledge Hub","url":"https://responsibleailabs.ai/knowledge-hub/articles/llm-evaluation-benchmarks-2025"},{"title":"Large Language Model Evaluation in 2025: Smarter Metrics That ...","url":"https://www.techrxiv.org/users/927947/articles/1304989/master/file/data/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust.pdf"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/pdf/2601.01362"}]

Based on the search results, here are the key findings related to multilingual LLM calibration surveys and benchmarks in 2025:

## Recent Multilingual Benchmarks

Large-scale benchmarks such as MuBench (Han et al., 24 Jun 2025), BenchMAX (Huang et al., 11 Feb 2025), and MMLU-ProX (Xuan et al., 13 Mar 2025) employ machine and LLM-assisted translation, with holistic frameworks providing broad coverage across tasks like natural language understanding, commonsense reasoning, machine translation, code generation, and instruction following.

## Calibration Research

While investigations into LLM calibration remain limited, recent studies have examined whether calibration solutions act on multiple languages simultaneously, particularly given LLMs' ability to be used on different languages that can vary in resource scarcity. A recent 2025 study titled "Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning" addresses this gap, finding that instruction-tuned models are less calibrated than their base counterparts across all languages.

## Benchmark Challenges

Effective multilingual benchmarks require several key characteristics to meaningfully evaluate LLM capabilities across diverse languages, with development presenting unique challenges beyond those faced in monolingual evaluation settings.

The search results show active research in this area with several 2025 publications advancing multilingual evaluation methodologies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "353a426b-27f5-483d-a600-d1c451450f53",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "3c4186d0-c766-47fe-97ac-5b94529c4103",
  "sourceToolAssistantUUID": "353a426b-27f5-483d-a600-d1c451450f53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-19T18:26:25.519Z_

Now let me get more details on some of the papers. Let me look up the exact authors for the arXiv 2510.03136 paper and the LACE connection, and also get more details on some of the additional papers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c4186d0-c766-47fe-97ac-5b94529c4103",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ3nWD9TxtrN1yjzdSF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0edb31e1-2aac-4e7e-a71b-fdfaf4162381",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014agz9cz8NjmUVuWtj6uGoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 14349,
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

_source line 23 · 2026-05-19T18:26:25.864Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JhLukrcfYgjffWaiLCvYZP`</summary>

```json
{
  "query": "arxiv 2510.03136 \"Beyond the Final Layer\" authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0edb31e1-2aac-4e7e-a71b-fdfaf4162381",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ3nWD9TxtrN1yjzdSF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "084d644b-7deb-44bb-9929-986d276bf441",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014agz9cz8NjmUVuWtj6uGoK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 14349,
      "output_tokens": 122,
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
          "output_tokens": 122,
          "cache_read_input_tokens": 14349,
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

_source line 24 · 2026-05-19T18:26:33.336Z_

<details><summary>↩ Tool result · `toolu_01JhLukrcfYgjffWaiLCvYZP`</summary>

```text
Web search results for query: "arxiv 2510.03136 "Beyond the Final Layer" authors full list"

Links: [{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136"},{"title":"[2601.09322] Beyond the final layer: Attentive multilayer fusion for vision transformers","url":"https://arxiv.org/abs/2601.09322"},{"title":"Beyond the Final Layer: Attentive Multi-Layer Fusion for Vision Transformers","url":"https://arxiv.org/html/2601.09322"},{"title":"[2502.04139] Beyond the Final Layer: Hierarchical Query Fusion Transformer with Agent-Interpolation Initialization for 3D Instance Segmentation","url":"https://arxiv.org/abs/2502.04139"},{"title":"Improving LLM Predictions via Inter-Layer Structural Encoders","url":"https://arxiv.org/pdf/2603.22665"},{"title":"Layer by Layer: Uncovering Hidden Representations in Language Models","url":"https://arxiv.org/pdf/2502.02013"},{"title":"On the emergence of simplex symmetry in the final and penultimate layers   of neural network classifiers","url":"https://arxiv.org/pdf/2012.05420"}]

The full list of authors for arxiv 2510.03136 "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models" is: Ej Zhou, Caiqi Zhang, Tiancheng Hu, Chengzu Li, Nigel Collier, Ivan Vulić, and Anna Korhonen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "084d644b-7deb-44bb-9929-986d276bf441",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "71672770-46dd-486b-b05e-4493f9b94706",
  "sourceToolAssistantUUID": "084d644b-7deb-44bb-9929-986d276bf441",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T18:26:36.095Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GyocXUYAcA9GpStexFW7mN`</summary>

```json
{
  "query": "\"Calibration Across Layers\" Joshi EMNLP 2025 authors LACE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71672770-46dd-486b-b05e-4493f9b94706",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ4ezJF5UfxWasXyKCy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20d146a3-2c24-4d3e-a8c9-a23ccbee6105",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D6qshukjRm3ewDxbY5dvPV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 15224,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 617
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 15224,
          "cache_creation_input_tokens": 617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 617,
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

_source line 26 · 2026-05-19T18:26:47.042Z_

<details><summary>↩ Tool result · `toolu_01GyocXUYAcA9GpStexFW7mN`</summary>

```text
Web search results for query: ""Calibration Across Layers" Joshi EMNLP 2025 authors LACE"

Links: [{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.742/"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=22850&show=2000"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/abs/2511.00280"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/pdf/2511.00280"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"}]

Based on the search results, I found information about the paper "Calibration Across Layers: Understanding Calibration Evolution in LLMs":

**Paper Details:**
The paper "Calibration Across Layers: Understanding Calibration Evolution in LLMs" was authored by Abhinav Joshi, Areeb Ahmad, and Ashutosh Modi and published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 14697–14725, Suzhou, China.

**Key Findings:**
The work investigates how calibration evolves throughout the network depth, and analyzing multiple open-weight models on the MMLU benchmark, uncovers a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached. Furthermore, the researchers identify a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.

**Main Insight:**
The findings suggest that calibration is a distributed phenomenon, shaped throughout the network's forward pass, not just in its final projection, providing new insights into how confidence-regulating mechanisms operate within LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20d146a3-2c24-4d3e-a8c9-a23ccbee6105",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "ed439567-07a5-4428-b9b5-d03a4a732264",
  "sourceToolAssistantUUID": "20d146a3-2c24-4d3e-a8c9-a23ccbee6105",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T18:26:49.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01775uG4jr6CCPWZq8odp6Uf`</summary>

```json
{
  "query": "\"Ji\" \"Calibrating Verbal Uncertainty\" EMNLP 2025 authors full"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed439567-07a5-4428-b9b5-d03a4a732264",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ5fbnoayCmfwHxJEfk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10e4012a-22a9-4355-a45e-4c3d1caf922e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AK1U2qkZrRkq3ZfqLsThFC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 15841,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 739
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 15841,
          "cache_creation_input_tokens": 739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 739,
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

_source line 28 · 2026-05-19T18:26:56.066Z_

<details><summary>↩ Tool result · `toolu_01775uG4jr6CCPWZq8odp6Uf`</summary>

```text
Web search results for query: ""Ji" "Calibrating Verbal Uncertainty" EMNLP 2025 authors full"

Links: [{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"Awards - EMNLP 2025","url":"https://2025.emnlp.org/program/awards/"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.187@ACL"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Verbal Uncertainty Estimation","url":"https://www.emergentmind.com/topics/verbal-uncertainty-estimation"},{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"dblp: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations.","url":"https://dblp.org/rec/journals/corr/abs-2503-14477.html"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"}]

Based on the search results, the authors of "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations" published at EMNLP 2025 are: Ji, Ziwei; Yu, Lei; Koishekenov, Yeskendir; Bang, Yejin; Hartshorn, Anthony; Schelten, Alan; Zhang, Cheng; Fung, Pascale; and Cancedda, Nicola.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10e4012a-22a9-4355-a45e-4c3d1caf922e",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "95c2a59c-a3fa-41b6-b062-186c4150ea52",
  "sourceToolAssistantUUID": "10e4012a-22a9-4355-a45e-4c3d1caf922e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T18:26:59.005Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HKW5ZJ7Hyxo44qshn4Wc3G`</summary>

```json
{
  "query": "MKA \"Leveraging Cross-Lingual Consensus\" authors Duwal ICLR 2025 workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95c2a59c-a3fa-41b6-b062-186c4150ea52",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ6LAma9Vn6Zh91reEc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cfcde69-9358-4ba9-89dc-fd8ecd7c6b96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4urj4Jeisc4hXYmdzZaF8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 16580,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 705
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 16580,
          "cache_creation_input_tokens": 705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 705,
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

_source line 30 · 2026-05-19T18:27:06.166Z_

<details><summary>↩ Tool result · `toolu_01HKW5ZJ7Hyxo44qshn4Wc3G`</summary>

```text
Web search results for query: "MKA "Leveraging Cross-Lingual Consensus" authors Duwal ICLR 2025 workshop"

Links: [{"title":"[Literature Review] MKA: Leveraging Cross-Lingual Consensus for Model Abstention","url":"https://www.themoonlight.io/en/review/mka-leveraging-cross-lingual-consensus-for-model-abstention"},{"title":"MKA: Leveraging Cross-Lingual Consensus for Model Abstention | OpenReview","url":"https://openreview.net/forum?id=7z49r7RhP2"},{"title":"MKA: Leveraging Cross-Lingual Consensus for Model Abstention Sharad Duwal","url":"https://arxiv.org/pdf/2503.23687"},{"title":"[2503.23687] MKA: Leveraging Cross-Lingual Consensus for Model Abstention","url":"https://arxiv.org/abs/2503.23687"},{"title":"MKA: LEVERAGING CROSS-LINGUAL CONSENSUS","url":"https://openreview.net/pdf?id=7z49r7RhP2"},{"title":"MKA: Leveraging Cross-Lingual Consensus for Model Abstention","url":"https://arxiv.org/html/2503.23687v1"},{"title":"ICLR 2025 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2025%2FConference"}]

Based on the search results, I found information about the paper "MKA: Leveraging Cross-Lingual Consensus for Model Abstention":

**Author:** Sharad Duwal

**Conference/Workshop:** ICLR 2025 Workshop BuildingTrust

**Publication Date:** Published: 05 Mar 2025

**Summary:** The work focuses on utilizing the multilingual knowledge of an LLM to inform its decision to abstain or answer when prompted, developing a multilingual pipeline to calibrate the model's confidence and let it abstain when uncertain.

**Key Results:** The accuracy improved by 71.2% for Bengali over a baseline performance without the pipeline.

The paper is available on both OpenReview and arXiv (2503.23687).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cfcde69-9358-4ba9-89dc-fd8ecd7c6b96",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "61694e75-506c-457f-99d3-d31c357f1c40",
  "sourceToolAssistantUUID": "1cfcde69-9358-4ba9-89dc-fd8ecd7c6b96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T18:27:08.800Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WYKVcrzSKuq9mhH71WkS1H`</summary>

```json
{
  "query": "\"Middle-Layer Representation Alignment\" Liu Niehues ACL 2025 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61694e75-506c-457f-99d3-d31c357f1c40",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ75LaMoshj1ePQr7zp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34ae1f53-e570-4a2f-af5b-e4d775afb4eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHqR2ixhcmymdckX7ZBNbK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 17285,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 665
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 17285,
          "cache_creation_input_tokens": 665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 665,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T18:27:13.706Z_

<details><summary>↩ Tool result · `toolu_01WYKVcrzSKuq9mhH71WkS1H`</summary>

```text
Web search results for query: ""Middle-Layer Representation Alignment" Liu Niehues ACL 2025 authors"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.778/"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/abs/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in","url":"https://openreview.net/pdf/165a4c42ede4fa7182ef5ba60ec0669f5606b9b8.pdf"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual ...","url":"https://aclanthology.org/2025.acl-long.778.pdf"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"},{"title":"[Literature Review] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://www.themoonlight.io/en/review/middle-layer-representation-alignment-for-cross-lingual-transfer-in-fine-tuned-llms"}]

Based on the search results, here's information about the paper "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs":

## Authors

The paper is authored by Danni Liu and Jan Niehues.

## Publication Details

The paper was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15979–15996, Vienna, Austria.

## Main Contribution

Through analysis of LLM internal representations from over 1,000+ language pairs, the authors discovered that middle layers exhibit the strongest potential for cross-lingual alignment, and they propose a middle-layer alignment objective integrated into task-specific training.

## Experimental Results

The experiments on slot filling, machine translation, and structured text generation show consistent improvements in cross-lingual transfer, especially to lower-resource languages, and the method is robust to the choice of alignment languages and generalizes to languages unseen during alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34ae1f53-e570-4a2f-af5b-e4d775afb4eb",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "e2433730-2c6d-4c65-a255-503d2b017031",
  "sourceToolAssistantUUID": "34ae1f53-e570-4a2f-af5b-e4d775afb4eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T18:27:16.786Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P1rw2GTejh258SRTy6GZx2`</summary>

```json
{
  "query": "arxiv 2510.03136 \"23.1\" ECE LLaMA-3 multilingual calibration gap"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2433730-2c6d-4c65-a255-503d2b017031",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ7db3sfFcWv8Ea9ctu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da756931-0c99-47dd-a070-b122cf7af1be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CWMZdnZRBU4FhrBFzfbUv8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1470,
      "cache_read_input_tokens": 17285,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1470
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 17285,
          "cache_creation_input_tokens": 1470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1470,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T18:27:24.525Z_

<details><summary>↩ Tool result · `toolu_01P1rw2GTejh258SRTy6GZx2`</summary>

```text
Web search results for query: "arxiv 2510.03136 "23.1" ECE LLaMA-3 multilingual calibration gap"

Links: [{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLM","url":"https://arxiv.org/pdf/2601.18306"},{"title":"Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/pdf/2601.01362"},{"title":"On the Calibration of Multilingual Question Answering LLMs Yahan Yang*","url":"https://arxiv.org/pdf/2311.08669"},{"title":"Calibrating Beyond English: Language Diversity for Better Quantized Multilingual LLMs","url":"https://arxiv.org/html/2601.18306"},{"title":"On the Calibration of Massively Multilingual Language Models","url":"https://arxiv.org/pdf/2210.12265"}]

Based on the search results, I found the paper you were looking for. Here's what the research reveals:

For LLaMA-3, the Expected Calibration Error (ECE) is nearly five times higher on average for non-English than for English (23.1% vs. 4.6%). This significant multilingual calibration gap is a key finding from the paper arxiv 2510.03136, titled "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models."

The analysis spans six major model families and over 100 languages, using high-quality, human-curated benchmarks (MMMLU and Belebele) with approximately 10^5 instances. 

The paper identifies that English-aligned models like LLaMA3 struggle to maintain calibration quality beyond English, whereas multilingual-first models like Aya are systematically over-confident across the board. To address this issue, late-intermediate layers consistently offer a more reliable and better-calibrated signal compared to relying solely on the final layer for confidence scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da756931-0c99-47dd-a070-b122cf7af1be",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "b3442f2d-529b-4985-b6e5-d791ed1d3d93",
  "sourceToolAssistantUUID": "da756931-0c99-47dd-a070-b122cf7af1be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T18:27:27.259Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013zKicBkNDXZyWCZXSJXr4S`</summary>

```json
{
  "query": "\"Calibrating LLM Confidence\" \"Probing Perturbed Representation Stability\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3442f2d-529b-4985-b6e5-d791ed1d3d93",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ8RqdxTqfiGz4XQ7yZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d112d4f7-8133-4274-b6c0-c39bc1d94ec3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhLLcLD5KcVQGuoync1tcr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 18755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 36 · 2026-05-19T18:27:33.553Z_

<details><summary>↩ Tool result · `toolu_013zKicBkNDXZyWCZXSJXr4S`</summary>

```text
Web search results for query: ""Calibrating LLM Confidence" "Probing Perturbed Representation Stability" 2025"

Links: [{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/calibrating-llm-confidence-by-probing-perturbed-representation"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF","url":"https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"}]

Based on the search results, here's what I found about "Calibrating LLM Confidence" "Probing Perturbed Representation Stability":

## Overview

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method analyzing internal representational stability in LLMs. The paper was published in the 2025 Conference on Empirical Methods in Natural Language Processing in Suzhou, China.

## How It Works

CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness. The premise is that if an LLM is truly confident, its internal decision-making process for a token should be stable against relevant adversarial nudges.

## Performance Results

Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points, all relative to the strongest prior method.

## Evaluation

CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d112d4f7-8133-4274-b6c0-c39bc1d94ec3",
  "isSidechain": true,
  "promptId": "a5e88450-0f80-497a-ac6c-b43ba33e8c1f",
  "agentId": "a48da4d30e1295305",
  "type": "user",
  "uuid": "ddab6938-13b7-4f6f-9a39-76775b36fec0",
  "sourceToolAssistantUUID": "d112d4f7-8133-4274-b6c0-c39bc1d94ec3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-19T18:28:10.420Z_

Now I have comprehensive information on all the papers. Here is my full report:

---

## Paper Verification Results

### Paper 1: Ji et al. (EMNLP 2025) -- VERIFIED REAL

- **Title:** "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations"
- **Authors:** Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, Nicola Cancedda
- **Venue:** EMNLP 2025 (Main Conference), Suzhou, China
- **arXiv:** [2503.14477](https://arxiv.org/abs/2503.14477)
- **ACL Anthology:** [2025.emnlp-main.187](https://aclanthology.org/2025.emnlp-main.187/)
- **Key finding:** Verbal uncertainty in LLMs is governed by a single linear direction in representation space (the "Verbal Uncertainty Feature" or VUF). Intervening on this direction at inference time reduces hallucinations by an average relative reduction of 32% on short-form answers. This VUF has only moderate correlation with actual semantic uncertainty.

### Paper 2: Joshi et al. (EMNLP 2025) -- VERIFIED REAL, but NOT called "LACE"

- **Title:** "Calibration Across Layers: Understanding Calibration Evolution in LLMs"
- **Authors:** Abhinav Joshi, Areeb Ahmad, Ashutosh Modi
- **Venue:** EMNLP 2025 (Main Conference), Suzhou, China, pages 14697-14725
- **arXiv:** [2511.00280](https://arxiv.org/abs/2511.00280)
- **ACL Anthology:** [2025.emnlp-main.742](https://aclanthology.org/2025.emnlp-main.742/)
- **Key finding:** Calibration is a distributed phenomenon shaped throughout the network's forward pass. The work identifies a "confidence correction phase" in upper/later layers and a low-dimensional calibration direction in the residual stream whose perturbation significantly improves ECE and MCE without harming accuracy.
- **IMPORTANT CORRECTION:** The proposal attributes "LACE" (Language-Aware Confidence Ensemble) to this paper, but LACE actually belongs to **Zhou et al. (arXiv 2510.03136)** -- see Paper 3 below. The Joshi et al. paper is about calibration evolution across layers, not LACE. The proposal appears to conflate these two separate papers.

### Paper 3: Zhou et al. (arXiv 2510.03136) -- VERIFIED REAL

- **Title:** "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models"
- **Authors:** Ej Zhou, Caiqi Zhang, Tiancheng Hu, Chengzu Li, Nigel Collier, Ivan Vulic, Anna Korhonen (University of Cambridge)
- **arXiv:** [2510.03136](https://arxiv.org/abs/2510.03136)
- **Key finding:** First large-scale study of multilingual calibration across 6 model families and 100+ languages. Confirmed a ~5x ECE gap: LLaMA-3 shows **23.1% ECE for non-English vs. 4.6% for English**. Late-intermediate layers offer more reliable, better-calibrated signals than the final layer. Introduces **LACE** (Language-Aware Confidence Ensemble), which adaptively selects an optimal ensemble of layers per language.
- **IMPORTANT NOTE:** This is the paper that introduces LACE and reports the 5x ECE gap and LLaMA-3 statistics. The proposal correctly attributes the ECE numbers to Zhou et al. but incorrectly attributes LACE to Joshi et al.

### Paper 4: MKA (ICLR Workshop 2025) -- VERIFIED REAL

- **Title:** "MKA: Leveraging Cross-Lingual Consensus for Model Abstention"
- **Authors:** Sharad Duwal
- **Venue:** ICLR 2025 Workshop on Building Trust (BuildingTrust)
- **arXiv:** [2503.23687](https://arxiv.org/abs/2503.23687)
- **OpenReview:** [7z49r7RhP2](https://openreview.net/forum?id=7z49r7RhP2)
- **Key finding:** Uses multilingual knowledge of LLMs to decide when to abstain. Translates a question to auxiliary languages, gets responses, measures cross-lingual semantic similarity as a confidence signal. Achieves 71.2% accuracy improvement for Bengali and 15.5% for English over baseline.

### Paper 5: Middle-Layer Representation Alignment (ACL 2025) -- VERIFIED REAL

- **Title:** "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs"
- **Authors:** Danni Liu, Jan Niehues
- **Venue:** ACL 2025 (63rd Annual Meeting, Long Papers), Vienna, Austria, pages 15979-15996
- **arXiv:** [2502.14830](https://arxiv.org/abs/2502.14830)
- **ACL Anthology:** [2025.acl-long.778](https://aclanthology.org/2025.acl-long.778/)
- **Key finding:** Analysis of 1,000+ language pairs shows middle layers exhibit the strongest cross-lingual alignment potential. Proposes a middle-layer alignment objective integrated into task-specific training. Consistent improvements in cross-lingual transfer, especially for lower-resource languages. Separately trained alignment modules can be merged with existing task-specific modules without full retraining.

---

## Additional Highly Relevant Papers to Consider Citing

### 6. CCPS (EMNLP 2025)
- **Title:** "Calibrating LLM Confidence by Probing Perturbed Representation Stability"
- **Venue:** EMNLP 2025, Suzhou, China
- **arXiv:** [2505.21772](https://arxiv.org/abs/2505.21772)
- **Relevance:** Directly applies adversarial perturbations to final hidden states and uses a lightweight classifier to predict answer correctness. Reduces ECE by ~55% and Brier score by 21%. Highly relevant if your proposal involves representation-level calibration probes.

### 7. Investigating Multilingual Calibration Effects of Instruction-Tuning (2025)
- **arXiv:** [2601.01362](https://arxiv.org/pdf/2601.01362)
- **Relevance:** Finds that instruction-tuned models are less calibrated than base models across all languages -- important context for multilingual calibration work.

### 8. Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation (2025)
- **arXiv:** [2512.22245](https://arxiv.org/pdf/2512.22245)
- **Relevance:** Uses linear probes on LLM representations for uncertainty estimation in LLM-as-judge settings.

---

## Key Correction Needed in the Proposal

The most significant issue found: **LACE is attributed to "Joshi et al. (EMNLP 2025)"** in the proposal, but LACE actually belongs to **Zhou et al. (arXiv 2510.03136)**. These are two different papers:
- **Joshi et al. (EMNLP 2025)** = "Calibration Across Layers" -- about calibration evolution across layers, finding a low-dimensional calibration direction
- **Zhou et al. (arXiv 2510.03136)** = "Beyond the Final Layer" -- about multilingual calibration, LACE method, 5x ECE gap

The proposal should be updated to correctly attribute LACE to Zhou et al. and the calibration direction finding to Joshi et al.

Sources:
- [Ji et al. - ACL Anthology](https://aclanthology.org/2025.emnlp-main.187/)
- [Ji et al. - arXiv](https://arxiv.org/abs/2503.14477)
- [Joshi et al. - ACL Anthology](https://aclanthology.org/2025.emnlp-main.742/)
- [Joshi et al. - arXiv](https://arxiv.org/abs/2511.00280)
- [Zhou et al. - arXiv](https://arxiv.org/abs/2510.03136)
- [MKA - OpenReview](https://openreview.net/forum?id=7z49r7RhP2)
- [MKA - arXiv](https://arxiv.org/abs/2503.23687)
- [Liu & Niehues - ACL Anthology](https://aclanthology.org/2025.acl-long.778/)
- [Liu & Niehues - arXiv](https://arxiv.org/abs/2502.14830)
- [CCPS - ACL Anthology](https://aclanthology.org/2025.emnlp-main.530/)
- [CCPS - arXiv](https://arxiv.org/abs/2505.21772)
- [Multilingual Calibration Instruction-Tuning - arXiv](https://arxiv.org/pdf/2601.01362)
- [LLM Judge Linear Probes - arXiv](https://arxiv.org/pdf/2512.22245)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddab6938-13b7-4f6f-9a39-76775b36fec0",
  "isSidechain": true,
  "agentId": "a48da4d30e1295305",
  "requestId": "req_011CbCQ96UqQpHHbKQj6DHR8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cf8cc03-9464-4fd8-b842-607f98c4089d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "ebd110c8-b862-40dd-ac5e-2488a176a1fa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01998G44RKAhpQTohS4T2UvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 19480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 866,
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
