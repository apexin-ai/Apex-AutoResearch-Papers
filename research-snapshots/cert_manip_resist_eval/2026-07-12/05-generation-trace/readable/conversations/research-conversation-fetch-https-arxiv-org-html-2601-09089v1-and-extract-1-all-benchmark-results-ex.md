# Research conversation: Fetch https://arxiv.org/html/2601.09089v1 and extract: 1) All benchmark results - exact accuracy numbers for each model 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a024d5d4d480abe2b.jsonl`
- **Structured JSON:** [`f2b5f410642ed5b093b7.json`](../../sessions/f2/f2b5f410642ed5b093b7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

9 recorded events

### User

_source line 1 · 2026-05-19T12:26:50.261Z_

Fetch https://arxiv.org/html/2601.09089v1 and extract: 1) All benchmark results - exact accuracy numbers for each model tested on SubTokenTest. 2) How many tasks and domains does SubTokenTest cover? 3) What is the accuracy range for current LLMs? 4) Any discussion of training methods to improve sub-token understanding? 5) Key findings about reasoning models vs non-reasoning models on sub-token tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f5feb0d2-4d04-47ba-8946-60ea46dd76ee",
  "agentId": "a024d5d4d480abe2b",
  "type": "user",
  "uuid": "862e6496-858b-4277-93b8-a60a83458e73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1274bca5-2b4e-4d40-af1e-6458f6406c2c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T12:26:50.264Z_

```json
{
  "parentUuid": "862e6496-858b-4277-93b8-a60a83458e73",
  "isSidechain": true,
  "agentId": "a024d5d4d480abe2b",
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
  "uuid": "23fb35ab-1d00-4cd0-b69c-41ff1a47ac75",
  "timestamp": "2026-05-19T12:26:50.264Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1274bca5-2b4e-4d40-af1e-6458f6406c2c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T12:26:50.265Z_

```json
{
  "parentUuid": "23fb35ab-1d00-4cd0-b69c-41ff1a47ac75",
  "isSidechain": true,
  "agentId": "a024d5d4d480abe2b",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1ca4f327-5c4d-4340-b19c-8537958f1272",
  "timestamp": "2026-05-19T12:26:50.265Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1274bca5-2b4e-4d40-af1e-6458f6406c2c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T12:26:53.115Z_



I'll fetch the paper and extract the requested information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ca4f327-5c4d-4340-b19c-8537958f1272",
  "isSidechain": true,
  "agentId": "a024d5d4d480abe2b",
  "requestId": "req_011CbBvdg7BMq5bz1ttsP3H8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15e2f9fd-7f75-43ce-8502-b79443cd522e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1274bca5-2b4e-4d40-af1e-6458f6406c2c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2SdtiRjAPek75G4Lk54L9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9206,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9206,
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

_source line 5 · 2026-05-19T12:26:53.636Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QZm7VCyWTvaoHKJ4npwwTJ`</summary>

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
  "parentUuid": "15e2f9fd-7f75-43ce-8502-b79443cd522e",
  "isSidechain": true,
  "agentId": "a024d5d4d480abe2b",
  "requestId": "req_011CbBvdg7BMq5bz1ttsP3H8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c56ae115-0dc9-484d-8c62-c1d7778491a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1274bca5-2b4e-4d40-af1e-6458f6406c2c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D2SdtiRjAPek75G4Lk54L9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9206,
      "cache_read_input_tokens": 0,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9206
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9206,
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

_source line 6 · 2026-05-19T12:26:53.640Z_

<details><summary>↩ Tool result · `toolu_01QZm7VCyWTvaoHKJ4npwwTJ`</summary>

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
  "parentUuid": "c56ae115-0dc9-484d-8c62-c1d7778491a9",
  "isSidechain": true,
  "promptId": "f5feb0d2-4d04-47ba-8946-60ea46dd76ee",
  "agentId": "a024d5d4d480abe2b",
  "type": "user",
  "uuid": "f38b8093-fc65-4588-a65a-1a2bcba515e1",
  "sourceToolAssistantUUID": "c56ae115-0dc9-484d-8c62-c1d7778491a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1274bca5-2b4e-4d40-af1e-6458f6406c2c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T12:27:05.559Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LGyjum1rVeJ5BYVPXHDt1W`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.09089v1",
  "prompt": "Extract ALL of the following information exhaustively from this paper:\n\n1) ALL benchmark results - every exact accuracy number for each model tested on SubTokenTest. Include model names and their scores on each task/category. Present as complete tables if possible.\n\n2) How many tasks and domains does SubTokenTest cover? List them all.\n\n3) What is the accuracy range for current LLMs on SubTokenTest?\n\n4) Any discussion of training methods, fine-tuning approaches, or techniques to improve sub-token understanding?\n\n5) Key findings about reasoning models vs non-reasoning models on sub-token tasks - any comparisons, performance gaps, or analysis.\n\nBe as thorough and exact as possible. Include every number, every model name, every task name mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f38b8093-fc65-4588-a65a-1a2bcba515e1",
  "isSidechain": true,
  "agentId": "a024d5d4d480abe2b",
  "requestId": "req_011CbBvdvnUUvpJWvWuXSZ92",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd47221d-25f6-4a3a-b822-e01a0cdf553b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1274bca5-2b4e-4d40-af1e-6458f6406c2c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcJUiKD1AhvbqW4P9Z4pYC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 611,
      "cache_read_input_tokens": 9206,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 611
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 247,
          "cache_read_input_tokens": 9206,
          "cache_creation_input_tokens": 611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 611,
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

_source line 8 · 2026-05-19T12:27:22.579Z_

<details><summary>↩ Tool result · `toolu_01LGyjum1rVeJ5BYVPXHDt1W`</summary>

```text
# SubTokenTest: Comprehensive Benchmark Analysis

## 1. Complete Benchmark Results

**Table 2 presents full evaluation results across 9 LLMs:**

| Task Category | Metric | DS-V3 | DS-R1 | GPT-4 | GPT-5 | o4-mini (low) | o4-mini (high) | Qwen-7B | DS-Qwen-7B | Qwen-32B | DS-Qwen-32B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Keystroke Encoding** | EM | 86% | 95% | 90% | 99% | 95% | 96% | 2% | 0% | 13% | 42% |
| **Keystroke Decoding** | EM | 0% | 94% | 0% | 100% | 95% | 98% | 0% | 0% | 0% | 0% |
| **Cipher & Decipher** | EM | 30% | 43% | 25% | 40% | 14% | 38% | 0% | 0% | 0% | 0% |
| **Cipher & Decipher** | Similarity | 0.56 | 0.96 | 0.50 | 0.96 | 0.84 | 0.88 | 0.07 | 0.08 | 0.09 | 0.12 |
| **Bio-sequence** | EM | 77% | 85% | 32% | 97% | 86% | 98% | 0% | 0% | 0% | 2% |
| **Bio-sequence** | Similarity | 0.86 | 0.94 | 0.74 | 0.99 | 0.76 | 0.99 | 0.13 | 0.17 | 0.29 | 0.37 |
| **OCR-noise** | EM | 70% | 77% | 79% | 91% | 20% | 47% | 0% | 0% | 12% | 1% |
| **OCR-noise** | Similarity | 0.92 | 0.93 | 0.95 | 0.99 | 0.94 | 0.97 | 0.57 | 0.17 | 0.94 | 0.88 |
| **Safety-mask** | EM | 54% | 96% | 59% | 98% | 86% | 88% | 0% | 0% | 8% | 2% |
| **Safety-mask** | F1 | 0.93 | 1.00 | 0.92 | 1.00 | 0.98 | 0.98 | 0.12 | 0.13 | 0.76 | 0.51 |
| **Table** | Content Score | 0.69 | 0.78 | 0.95 | 0.66 | 0.34 | 0.69 | 0.52 | 0.21 | 0.55 | 0.44 |
| **Table** | Alignment Rate | 41% | 23.9% | 21% | 36% | 34% | 59% | 0% | 57.1% | 6% | 1.2% |
| **Tree Structure** | EM | 78% | 95% | 43% | 96% | 83% | 95% | 14% | 11% | 25% | 32% |
| **Tree Path** | EM | 93% | 99% | 27% | 97% | 72% | 90% | 0% | 2% | 31% | 31% |
| **Map-Nav (Sokoban)** | EM | 79% | 99% | 48% | 98% | 74% | 89% | 29% | 11% | 37% | 69% |
| **Map-Nav (FrozenLake)** | EM | 93% | 99% | 59% | 99% | 79% | 87% | 33% | 18% | 47% | 80% |
| **Gomoku Linear** | EM | 53% | 93% | 36% | 97% | 77% | 97% | 32% | 30% | 43% | 41% |
| **Gomoku Diagonal** | EM | 30% | 81% | 34% | 94% | 42% | 97% | 30% | 16% | 35% | 27% |
| **RSA-diff** | F1 | 0.07 | 0.97 | 0.04 | 0.98 | 0.58 | 0.95 | 0.01 | 0.00 | 0.01 | 0.00 |

## 2. Benchmark Structure

**SubTokenTest covers 10 tasks across 4 domains:**

- **Sequence Transformation (3 tasks):** Keystroke-level text editing (encoding/decoding), Cipher & Decipher, Biological sequence manipulation
- **Text Canonicalization (2 tasks):** OCR-noise canonicalization, Safety-style masking
- **Structured Data (2 tasks):** Aligned tables, Tree understanding (structure/path queries)
- **2D Spatial Pattern Recognition (3 tasks):** Map navigation (Sokoban/FrozenLake), Gomoku state reading (linear/diagonal), RSA difference identification

## 3. Accuracy Range for Current LLMs

The performance spectrum is dramatic:

- **Large reasoning models (GPT-5, DS-R1):** 81-100% on most tasks; 0-1% on others
- **Large standard models (GPT-4, DS-V3):** 25-95% depending on task
- **Small models (7B-32B):** "0% to 97% depending on model and task"

The paper notes "a significant performance gap based on model scale: large-scale models consistently outperform smaller models by a wide margin."

## 4. Training/Fine-tuning Methods

**The paper explicitly does NOT propose solutions.** The authors state: "we do not propose solutions for the challenges identified" and their "goal is to evaluate the current state of LLMs' ability to handle sub-token information."

However, the paper reviews existing mitigation strategies including stochastic tokenization methods (BPE-Dropout, StochasTok) and divide-and-conquer prompting techniques, noting these approaches show promise but remain limited.

## 5. Reasoning vs. Non-Reasoning Models

**Critical findings:**

- Reasoning models "consistently outperform their non-reasoning counterparts"
- DeepSeek-R1 vs DeepSeek-V3: R1 shows substantial gains but "this performance gain comes at a significant computational cost" with "tens or even hundreds of times more tokens"
- "Sensitivity to reasoning budget": Reducing o4-mini from "high" to "low" causes "sharp accuracy drop"
- **Counterintuitive finding:** On smaller models (7B-32B), "reasoning models do not always outperform their non-reasoning counterparts"; DeepSeek-R1-Distill-Qwen-7B "consistently lags behind its non-reasoning base model"
- Test-time scaling reveals "inverted U-shaped" performance curve: peak at ~2048 tokens, then degradation from "overthinking"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd47221d-25f6-4a3a-b822-e01a0cdf553b",
  "isSidechain": true,
  "promptId": "f5feb0d2-4d04-47ba-8946-60ea46dd76ee",
  "agentId": "a024d5d4d480abe2b",
  "type": "user",
  "uuid": "4ca84965-a523-471d-b9b1-4bed1f3553a9",
  "sourceToolAssistantUUID": "cd47221d-25f6-4a3a-b822-e01a0cdf553b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1274bca5-2b4e-4d40-af1e-6458f6406c2c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-19T12:27:55.181Z_

Here is the comprehensive extraction from the paper at `https://arxiv.org/html/2601.09089v1`:

---

## 1. Benchmark Results (All Exact Accuracy Numbers)

The paper evaluates 10 models (DS-V3 = DeepSeek-V3, DS-R1 = DeepSeek-R1, GPT-4, GPT-5, o4-mini at low/high reasoning effort, Qwen-7B, DS-Qwen-7B = DeepSeek-R1-Distill-Qwen-7B, Qwen-32B, DS-Qwen-32B = DeepSeek-R1-Distill-Qwen-32B):

| Task | Metric | DS-V3 | DS-R1 | GPT-4 | GPT-5 | o4-mini (low) | o4-mini (high) | Qwen-7B | DS-Qwen-7B | Qwen-32B | DS-Qwen-32B |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Keystroke Encoding | EM | 86% | 95% | 90% | 99% | 95% | 96% | 2% | 0% | 13% | 42% |
| Keystroke Decoding | EM | 0% | 94% | 0% | 100% | 95% | 98% | 0% | 0% | 0% | 0% |
| Cipher & Decipher | EM | 30% | 43% | 25% | 40% | 14% | 38% | 0% | 0% | 0% | 0% |
| Cipher & Decipher | Similarity | 0.56 | 0.96 | 0.50 | 0.96 | 0.84 | 0.88 | 0.07 | 0.08 | 0.09 | 0.12 |
| Bio-sequence | EM | 77% | 85% | 32% | 97% | 86% | 98% | 0% | 0% | 0% | 2% |
| Bio-sequence | Similarity | 0.86 | 0.94 | 0.74 | 0.99 | 0.76 | 0.99 | 0.13 | 0.17 | 0.29 | 0.37 |
| OCR-noise | EM | 70% | 77% | 79% | 91% | 20% | 47% | 0% | 0% | 12% | 1% |
| OCR-noise | Similarity | 0.92 | 0.93 | 0.95 | 0.99 | 0.94 | 0.97 | 0.57 | 0.17 | 0.94 | 0.88 |
| Safety-mask | EM | 54% | 96% | 59% | 98% | 86% | 88% | 0% | 0% | 8% | 2% |
| Safety-mask | F1 | 0.93 | 1.00 | 0.92 | 1.00 | 0.98 | 0.98 | 0.12 | 0.13 | 0.76 | 0.51 |
| Table | Content Score | 0.69 | 0.78 | 0.95 | 0.66 | 0.34 | 0.69 | 0.52 | 0.21 | 0.55 | 0.44 |
| Table | Alignment Rate | 41% | 23.9% | 21% | 36% | 34% | 59% | 0% | 57.1% | 6% | 1.2% |
| Tree Structure | EM | 78% | 95% | 43% | 96% | 83% | 95% | 14% | 11% | 25% | 32% |
| Tree Path | EM | 93% | 99% | 27% | 97% | 72% | 90% | 0% | 2% | 31% | 31% |
| Map-Nav (Sokoban) | EM | 79% | 99% | 48% | 98% | 74% | 89% | 29% | 11% | 37% | 69% |
| Map-Nav (FrozenLake) | EM | 93% | 99% | 59% | 99% | 79% | 87% | 33% | 18% | 47% | 80% |
| Gomoku Linear | EM | 53% | 93% | 36% | 97% | 77% | 97% | 32% | 30% | 43% | 41% |
| Gomoku Diagonal | EM | 30% | 81% | 34% | 94% | 42% | 97% | 30% | 16% | 35% | 27% |
| RSA-diff | F1 | 0.07 | 0.97 | 0.04 | 0.98 | 0.58 | 0.95 | 0.01 | 0.00 | 0.01 | 0.00 |

---

## 2. Tasks and Domains

SubTokenTest covers **10 tasks** across **4 domains**:

- **Sequence Transformation (3 tasks):** Keystroke-level text editing (encoding/decoding), Cipher & Decipher, Biological sequence manipulation
- **Text Canonicalization (2 tasks):** OCR-noise canonicalization, Safety-style masking
- **Structured Data (2 tasks):** Aligned tables, Tree understanding (structure and path queries)
- **2D Spatial Pattern Recognition (3 tasks):** Map navigation (Sokoban / FrozenLake), Gomoku state reading (linear / diagonal), RSA difference identification

---

## 3. Accuracy Range for Current LLMs

The range is extremely wide, spanning from **0% to 100%** depending on model and task:

- **Best performers** (GPT-5, DeepSeek-R1): 81--100% on most tasks, with GPT-5 hitting 100% exact match on Keystroke Decoding
- **Large non-reasoning models** (GPT-4, DeepSeek-V3): 0--95% depending on the task, with notable failures (e.g., GPT-4 and DS-V3 both score 0% on Keystroke Decoding)
- **Small models** (7B and 32B scale): Mostly 0--2% on many tasks, with occasional outliers (e.g., DS-Qwen-32B reaches 80% on FrozenLake)
- There is a significant performance gap based on model scale, with large models consistently outperforming smaller ones by wide margins

---

## 4. Training Methods to Improve Sub-Token Understanding

The paper **explicitly does not propose solutions**. The authors state their goal is to evaluate the current state, not to fix it. However, they review existing mitigation strategies from prior work:

- **Stochastic tokenization methods:** BPE-Dropout and StochasTok, which expose models to varied sub-word segmentations during training
- **Divide-and-conquer prompting techniques:** Breaking sub-token tasks into smaller steps at inference time

The authors note these approaches show promise but remain limited in their effectiveness.

---

## 5. Reasoning Models vs. Non-Reasoning Models -- Key Findings

This is one of the paper's most nuanced contributions:

1. **At large scale, reasoning models consistently outperform non-reasoning counterparts.** DeepSeek-R1 substantially outperforms DeepSeek-V3 across nearly all tasks (e.g., Keystroke Decoding: 94% vs. 0%; RSA-diff F1: 0.97 vs. 0.07).

2. **The gain comes at enormous computational cost.** Reasoning models consume tens to hundreds of times more tokens than non-reasoning models to achieve their results.

3. **Reasoning budget sensitivity.** Reducing o4-mini's reasoning effort from "high" to "low" causes sharp accuracy drops on several tasks (e.g., OCR-noise EM drops from 47% to 20%; Gomoku Diagonal from 97% to 42%).

4. **At small scale, reasoning can actually hurt.** This is a counterintuitive finding: DeepSeek-R1-Distill-Qwen-7B consistently lags behind its non-reasoning base model (Qwen-7B) on multiple tasks. Distilled reasoning does not reliably transfer to sub-token tasks at small scale.

5. **Inverted U-shaped performance with test-time scaling.** Performance peaks at around 2048 reasoning tokens, then degrades due to "overthinking" -- the model starts second-guessing correct intermediate steps with additional computation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ca84965-a523-471d-b9b1-4bed1f3553a9",
  "isSidechain": true,
  "agentId": "a024d5d4d480abe2b",
  "requestId": "req_011CbBvg4Gjb8Awqc2PNNiPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f01fe30a-56d8-415f-82aa-6e776d6f5097",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1274bca5-2b4e-4d40-af1e-6458f6406c2c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9UFNW5Qwh4q2d2C8SG5X3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2130,
      "cache_read_input_tokens": 9817,
      "output_tokens": 2233,
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
          "output_tokens": 2233,
          "cache_read_input_tokens": 9817,
          "cache_creation_input_tokens": 2130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2130,
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
