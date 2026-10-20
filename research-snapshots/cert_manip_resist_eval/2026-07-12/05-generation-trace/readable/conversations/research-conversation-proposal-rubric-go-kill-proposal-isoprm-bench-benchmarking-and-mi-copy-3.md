# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # IsoPRM-Bench: Benchmarking and Mi

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/b92b42d7-02d4-46cb-973f-5b2c9d6023fd.jsonl`
- **Structured JSON:** [`1f04c295994a449f4861.json`](../../sessions/1f/1f04c295994a449f4861.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:14:40.234Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:14:40.234Z",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# IsoPRM-Bench: Benchmarking and Mitigating Structural Isomorphism Brittleness in Process Reward Models\n\n## Description\nWe propose IsoPRM-Bench, the first benchmark testing whether Process Reward Models maintain consistent scores across structurally isomorphic reasoning steps, paired with Iso-Aug, a mitigation method based on isomorphic augmentation with consistency regularization. While PRM-BiasBench tests surface perturbations (rephrasing, verbosity), reWordBench tests meaning-preserving transformations on general RMs at response level, PutnamGAP tests equivalent transformations on LLM solvers, GR-Ben extends PRM evaluation to 9 non-mathematical reasoning subdomains, and APRM improves error detection via adversarial training, no existing work tests step-level structural invariance of PRM verifiers — whether a PRM scores logically equivalent steps identically when their mathematical realization differs. Starting from ProcessBench's 3,400 human-annotated solutions (GSM8K: 400, MATH: 1,000, OlympiadBench: 1,000, Omni-MATH: 1,000), we generate isomorphic variants across four formally verifiable transformation types (variable renaming, commutative reordering, representation change, notation change) with a three-tier verification pipeline (SymPy, Z3, human audit). We explicitly quantify per-transformation coverage: T1/T2 apply broadly (~60-75% of steps), while T3/T4 require specific mathematical content (~35-55%), with coverage validated via a 100-solution pilot annotation and supplemented by AMC/AIME solutions if needed. We evaluate PRMs spanning three paradigms — discriminative (Qwen2.5-Math-PRM-72B/7B, Math-Shepherd), generative-CoT (ThinkPRM), and generative-code (GenPRM) — using an Isomorphic Invariance Score (IIS). Crucially, we cross-analyze IIS with PRM-BiasBench's surface robustness to map the two-dimensional robustness landscape. For mitigation, we adapt CoLD's causal debiasing framework to fine-tune Qwen2.5-Math-PRM-7B with isomorphic augmentation and consistency regularization, positioning Iso-Aug as complementary to APRM's adversarial training (which improves error detection robustness via novel negative generation, while Iso-Aug improves invariance across valid reformulations). Our analysis targets five key findings: (1) anti-correlated model-specific blind spots across transformation types, (2) whether generative PRMs show inherent isomorphic robustness — and if so, quantifying the paradigm gap to inform deployment decisions between latency-sensitive discriminative PRMs and invariance-superior generative PRMs, (3) whether brittleness increases with step depth (explaining tree search failure), (4) the practical impact on best-of-N selection with diverse reasoning strategies, and (5) a notation gaming attack surface analysis demonstrating how a policy can exploit PRM notation preferences to inflate scores without improving reasoning — analogous to but structurally deeper than PRM-BiasBench's finding that 43% of RL reward gains come from fluency-based stylistic shortcuts. We explicitly address the generative PRM trajectory: even if GenPRM/ThinkPRM pass invariance tests, the benchmark quantifies the paradigm robustness gap for deployment decisions, provides Iso-Aug training signal to improve latency-efficient discriminative PRMs, and establishes isomorphic invariance as a standard evaluation dimension. We adopt a two-phase submission strategy: benchmark-focused for AAAI 2027 (Jul 28; human-in-loop mode, 8-10 weeks), with full Iso-Aug + APRM composition for ICLR 2027 backup (~Oct 2026). This work bridges the gap between outcome-level robustness testing (IPT, PutnamGAP) and step-level verification, with direct implications for PRM-guided test-time compute scaling and reward hacking prevention.\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:14:40.238Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:14:40.238Z",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

## Round 1

50 recorded events

### User

_source line 3 · 2026-05-20T03:14:40.250Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# IsoPRM-Bench: Benchmarking and Mitigating Structural Isomorphism Brittleness in Process Reward Models

## Description
We propose IsoPRM-Bench, the first benchmark testing whether Process Reward Models maintain consistent scores across structurally isomorphic reasoning steps, paired with Iso-Aug, a mitigation method based on isomorphic augmentation with consistency regularization. While PRM-BiasBench tests surface perturbations (rephrasing, verbosity), reWordBench tests meaning-preserving transformations on general RMs at response level, PutnamGAP tests equivalent transformations on LLM solvers, GR-Ben extends PRM evaluation to 9 non-mathematical reasoning subdomains, and APRM improves error detection via adversarial training, no existing work tests step-level structural invariance of PRM verifiers — whether a PRM scores logically equivalent steps identically when their mathematical realization differs. Starting from ProcessBench's 3,400 human-annotated solutions (GSM8K: 400, MATH: 1,000, OlympiadBench: 1,000, Omni-MATH: 1,000), we generate isomorphic variants across four formally verifiable transformation types (variable renaming, commutative reordering, representation change, notation change) with a three-tier verification pipeline (SymPy, Z3, human audit). We explicitly quantify per-transformation coverage: T1/T2 apply broadly (~60-75% of steps), while T3/T4 require specific mathematical content (~35-55%), with coverage validated via a 100-solution pilot annotation and supplemented by AMC/AIME solutions if needed. We evaluate PRMs spanning three paradigms — discriminative (Qwen2.5-Math-PRM-72B/7B, Math-Shepherd), generative-CoT (ThinkPRM), and generative-code (GenPRM) — using an Isomorphic Invariance Score (IIS). Crucially, we cross-analyze IIS with PRM-BiasBench's surface robustness to map the two-dimensional robustness landscape. For mitigation, we adapt CoLD's causal debiasing framework to fine-tune Qwen2.5-Math-PRM-7B with isomorphic augmentation and consistency regularization, positioning Iso-Aug as complementary to APRM's adversarial training (which improves error detection robustness via novel negative generation, while Iso-Aug improves invariance across valid reformulations). Our analysis targets five key findings: (1) anti-correlated model-specific blind spots across transformation types, (2) whether generative PRMs show inherent isomorphic robustness — and if so, quantifying the paradigm gap to inform deployment decisions between latency-sensitive discriminative PRMs and invariance-superior generative PRMs, (3) whether brittleness increases with step depth (explaining tree search failure), (4) the practical impact on best-of-N selection with diverse reasoning strategies, and (5) a notation gaming attack surface analysis demonstrating how a policy can exploit PRM notation preferences to inflate scores without improving reasoning — analogous to but structurally deeper than PRM-BiasBench's finding that 43% of RL reward gains come from fluency-based stylistic shortcuts. We explicitly address the generative PRM trajectory: even if GenPRM/ThinkPRM pass invariance tests, the benchmark quantifies the paradigm robustness gap for deployment decisions, provides Iso-Aug training signal to improve latency-efficient discriminative PRMs, and establishes isomorphic invariance as a standard evaluation dimension. We adopt a two-phase submission strategy: benchmark-focused for AAAI 2027 (Jul 28; human-in-loop mode, 8-10 weeks), with full Iso-Aug + APRM composition for ICLR 2027 backup (~Oct 2026). This work bridges the gap between outcome-level robustness testing (IPT, PutnamGAP) and step-level verification, with direct implications for PRM-guided test-time compute scaling and reward hacking prevention.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "27f8822b-736e-4d31-8d60-f7a4417c7b6e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:14:40.249Z_

```json
{
  "parentUuid": "27f8822b-736e-4d31-8d60-f7a4417c7b6e",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "9fba31ee-72b9-4cbd-84fc-ea16d00fe875",
  "timestamp": "2026-05-20T03:14:40.249Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:14:40.249Z_

```json
{
  "parentUuid": "9fba31ee-72b9-4cbd-84fc-ea16d00fe875",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e55f7b10-a78d-47c1-90dc-483e6d41dff7",
  "timestamp": "2026-05-20T03:14:40.249Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate acceptance probability for IsoPRM-Bench proposal",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

### Assistant

_source line 7 · 2026-05-20T03:14:47.468Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 about "IsoPRM-Bench: Benchmarking and Mitigating Structural Isomorphism Brittleness in Process Reward Models." 

Wait, the user says CoRL 2026 but the proposal itself mentions AAAI 2027 and ICLR 2027 as target venues. Let me note this but focus on evaluating the idea quality regardless of venue.

Let me first do the required web searches to understand the field before making any judgments. I need to search for:

1. Recent work on Process Reward Models (PRMs) robustness


2. The specific benchmarks and methods mentioned like PRM-BiasBench, reWordBench, PutnamGAP, GR-Ben, and APRM
3. ProcessBench and related evaluation frameworks
4. How isomorphic invariance applies to mathematical reasoning tasks

I'll run these searches in parallel to get up to speed on the landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e55f7b10-a78d-47c1-90dc-483e6d41dff7",
  "isSidechain": false,
  "requestId": "req_011CbD6LSNdKdSzdje9CoXpi",
  "type": "assistant",
  "uuid": "49679a74-e47c-4ba5-ab85-e13a3d682396",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQwtYGYsNUvPc24Luia4mJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2367,
      "cache_read_input_tokens": 13985,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 337,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 2367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2367
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

### Assistant

_source line 8 · 2026-05-20T03:14:47.471Z_

I need to do thorough literature research before evaluating this proposal. Let me search for the key related works and the current state of Process Reward Model research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49679a74-e47c-4ba5-ab85-e13a3d682396",
  "isSidechain": false,
  "requestId": "req_011CbD6LSNdKdSzdje9CoXpi",
  "type": "assistant",
  "uuid": "0741ed8b-4079-48a0-a9a0-2015a4a2bb4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQwtYGYsNUvPc24Luia4mJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2367,
      "cache_read_input_tokens": 13985,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 337,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 2367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2367
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

### Tool call

_source line 9 · 2026-05-20T03:14:47.505Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JfuvTrLpTStTmCtsWHZ4E4`</summary>

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
  "parentUuid": "0741ed8b-4079-48a0-a9a0-2015a4a2bb4f",
  "isSidechain": false,
  "requestId": "req_011CbD6LSNdKdSzdje9CoXpi",
  "type": "assistant",
  "uuid": "ae030710-61c7-4e49-a257-5ada95bbab85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQwtYGYsNUvPc24Luia4mJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2367,
      "cache_read_input_tokens": 13985,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 337,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 2367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2367
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

_source line 10 · 2026-05-20T03:14:47.513Z_

<details><summary>↩ Tool result · `toolu_01JfuvTrLpTStTmCtsWHZ4E4`</summary>

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
  "parentUuid": "ae030710-61c7-4e49-a257-5ada95bbab85",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "efef6a86-9792-4001-bc47-0f6ab90adeee",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "ae030710-61c7-4e49-a257-5ada95bbab85",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T03:14:50.136Z_

Now let me run multiple searches in parallel to cover the key areas of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efef6a86-9792-4001-bc47-0f6ab90adeee",
  "isSidechain": false,
  "requestId": "req_011CbD6LyWt1BnXPDBHbtu4F",
  "type": "assistant",
  "uuid": "b2df1320-64d3-4dc0-8455-6a5e56099dec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtN8usbejEsFnG3PK6naZ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 16352,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 16352,
          "cache_creation_input_tokens": 864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 864
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

### Tool call

_source line 12 · 2026-05-20T03:14:50.542Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SLnLgiBrarLATCdbBvp2Br`</summary>

```json
{
  "query": "PRM-BiasBench Process Reward Model robustness benchmark 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2df1320-64d3-4dc0-8455-6a5e56099dec",
  "isSidechain": false,
  "requestId": "req_011CbD6LyWt1BnXPDBHbtu4F",
  "type": "assistant",
  "uuid": "dd9d4daa-f060-4cca-8ade-7dabbacc8489",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtN8usbejEsFnG3PK6naZ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 16352,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 16352,
          "cache_creation_input_tokens": 864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 864
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

_source line 13 · 2026-05-20T03:14:57.054Z_

<details><summary>↩ Tool result · `toolu_01SLnLgiBrarLATCdbBvp2Br`</summary>

```text
Web search results for query: "PRM-BiasBench Process Reward Model robustness benchmark 2024 2025"

Links: [{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF","url":"https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/abs/2501.03124"},{"title":"ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents","url":"https://arxiv.org/html/2601.12294v1"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1230/"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"Paper page - PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://huggingface.co/papers/2501.03124"},{"title":"Towards Robust Process Reward Modeling via Noise-aware Learning","url":"https://arxiv.org/pdf/2601.12748"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"}]

Based on the search results, I found information about **PRMBench** (not PRM-BiasBench specifically). Here's what I found:

## PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models

PRMBench is a process-level benchmark specifically designed to assess the fine-grained error detection capabilities of PRMs. It comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.

### Evaluation Results

In experiments on 25 models, spanning both open-source PRMs and closed-source large language models prompted as critic models, significant weaknesses in current PRMs were uncovered. These findings underscore the challenges inherent in process-level evaluation and highlight key directions for future research, establishing PRMBench as a robust testbed for advancing research on PRM evaluation and development.

### Timeline

The paper was initially submitted in January 2025 and has been updated multiple times through June 2025, with the final version published at ACL in July 2025.

**Note:** My search did not return specific results about "PRM-BiasBench" as a distinct benchmark. The results primarily showed PRMBench and related PRM evaluation benchmarks. If you're looking for information about a specific "PRM-BiasBench" benchmark, you may want to clarify if that's an alternative name or a different benchmark project.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd9d4daa-f060-4cca-8ade-7dabbacc8489",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "7800b7ba-d746-4e40-bd76-eb1ed127f115",
  "toolUseResult": {
    "query": "PRM-BiasBench Process Reward Model robustness benchmark 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UWGNcnAGMFxcWX6fbjmJyH",
        "content": [
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF",
            "url": "https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/abs/2501.03124"
          },
          {
            "title": "ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents",
            "url": "https://arxiv.org/html/2601.12294v1"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.1230/"
          },
          {
            "title": "R-PRM: Reasoning-Driven Process Reward Modeling",
            "url": "https://arxiv.org/html/2503.21295v1"
          },
          {
            "title": "Paper page - PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://huggingface.co/papers/2501.03124"
          },
          {
            "title": "Towards Robust Process Reward Modeling via Noise-aware Learning",
            "url": "https://arxiv.org/pdf/2601.12748"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/pdf/2501.03124"
          }
        ]
      },
      "Based on the search results, I found information about **PRMBench** (not PRM-BiasBench specifically). Here's what I found:\n\n## PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models\n\nPRMBench is a process-level benchmark specifically designed to assess the fine-grained error detection capabilities of PRMs. It comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.\n\n### Evaluation Results\n\nIn experiments on 25 models, spanning both open-source PRMs and closed-source large language models prompted as critic models, significant weaknesses in current PRMs were uncovered. These findings underscore the challenges inherent in process-level evaluation and highlight key directions for future research, establishing PRMBench as a robust testbed for advancing research on PRM evaluation and development.\n\n### Timeline\n\nThe paper was initially submitted in January 2025 and has been updated multiple times through June 2025, with the final version published at ACL in July 2025.\n\n**Note:** My search did not return specific results about \"PRM-BiasBench\" as a distinct benchmark. The results primarily showed PRMBench and related PRM evaluation benchmarks. If you're looking for information about a specific \"PRM-BiasBench\" benchmark, you may want to clarify if that's an alternative name or a different benchmark project."
    ],
    "durationSeconds": 6.5089492779999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dd9d4daa-f060-4cca-8ade-7dabbacc8489",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T03:14:59.772Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EsUaC9hQ9bezhzp2WFx5hE`</summary>

```json
{
  "query": "reWordBench meaning-preserving transformations reward models robustness arXiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7800b7ba-d746-4e40-bd76-eb1ed127f115",
  "isSidechain": false,
  "requestId": "req_011CbD6MfyTmh5fN3NoMMewJ",
  "type": "assistant",
  "uuid": "3aea0fd6-1756-41b2-a2a2-2005f35885e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FMSTcMWorbGyZ1sHdw9hki",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 17216,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 17216,
          "cache_creation_input_tokens": 920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 920
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

_source line 15 · 2026-05-20T03:15:06.626Z_

<details><summary>↩ Tool result · `toolu_01EsUaC9hQ9bezhzp2WFx5hE`</summary>

```text
Web search results for query: "reWordBench meaning-preserving transformations reward models robustness arXiv 2025 2026"

Links: [{"title":"[2503.11751] reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs","url":"https://arxiv.org/abs/2503.11751"},{"title":"Benchmarking and Improving the Robustness of Reward ...","url":"https://arxiv.org/pdf/2503.11751"},{"title":"Paper page - reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs","url":"https://huggingface.co/papers/2503.11751"},{"title":"RoboRewardBench: Robust Reward Model Benchmark","url":"https://www.emergentmind.com/topics/roborewardbench"},{"title":"[Literature Review] reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs","url":"https://www.themoonlight.io/en/review/rewordbench-benchmarking-and-improving-the-robustness-of-reward-models-with-transformed-inputs"},{"title":"reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs | Request PDF","url":"https://www.researchgate.net/publication/389917064_reWordBench_Benchmarking_and_Improving_the_Robustness_of_Reward_Models_with_Transformed_Inputs"},{"title":"Benchmarking and Improving the Robustness of Reward ...","url":"https://aclanthology.org/2025.emnlp-main.167.pdf"},{"title":"[Quick Review] Robust Reward Modeling via Causal Rubrics","url":"https://liner.com/review/robust-reward-modeling-via-causal-rubrics"}]

Based on the search results, here's what I found about reWordBench:

## Overview

reWordBench systematically transforms reward model inputs in meaning- or ranking-preserving ways. Reward models have become a staple in modern NLP, serving as not only a scalable text evaluator, but also an indispensable component in many alignment recipes and inference-time algorithms.

## Key Findings

State-of-the-art reward models suffer from substantial performance degradation even with minor input transformations, sometimes dropping to significantly below-random accuracy, suggesting brittleness.

## Proposed Solution

To improve reward model robustness, the authors propose to explicitly train them to assign similar scores to paraphrases, and find that this approach also improves robustness to other distinct kinds of transformations.

## Publication Details

The paper appears to be from 2025, with the arXiv identifier 2503.11751. The authors are Zhaofeng Wu, Michihiro Yasunaga, Andrew Cohen, Yoon Kim, Asli Celikyilmaz, and Marjan Ghazvininejad.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3aea0fd6-1756-41b2-a2a2-2005f35885e2",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "2903f111-054c-41e9-b410-da60bf942e48",
  "toolUseResult": {
    "query": "reWordBench meaning-preserving transformations reward models robustness arXiv 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01En3W4YCGXxQKmL8UMmTToL",
        "content": [
          {
            "title": "[2503.11751] reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs",
            "url": "https://arxiv.org/abs/2503.11751"
          },
          {
            "title": "Benchmarking and Improving the Robustness of Reward ...",
            "url": "https://arxiv.org/pdf/2503.11751"
          },
          {
            "title": "Paper page - reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs",
            "url": "https://huggingface.co/papers/2503.11751"
          },
          {
            "title": "RoboRewardBench: Robust Reward Model Benchmark",
            "url": "https://www.emergentmind.com/topics/roborewardbench"
          },
          {
            "title": "[Literature Review] reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs",
            "url": "https://www.themoonlight.io/en/review/rewordbench-benchmarking-and-improving-the-robustness-of-reward-models-with-transformed-inputs"
          },
          {
            "title": "reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs | Request PDF",
            "url": "https://www.researchgate.net/publication/389917064_reWordBench_Benchmarking_and_Improving_the_Robustness_of_Reward_Models_with_Transformed_Inputs"
          },
          {
            "title": "Benchmarking and Improving the Robustness of Reward ...",
            "url": "https://aclanthology.org/2025.emnlp-main.167.pdf"
          },
          {
            "title": "[Quick Review] Robust Reward Modeling via Causal Rubrics",
            "url": "https://liner.com/review/robust-reward-modeling-via-causal-rubrics"
          }
        ]
      },
      "Based on the search results, here's what I found about reWordBench:\n\n## Overview\n\nreWordBench systematically transforms reward model inputs in meaning- or ranking-preserving ways. Reward models have become a staple in modern NLP, serving as not only a scalable text evaluator, but also an indispensable component in many alignment recipes and inference-time algorithms.\n\n## Key Findings\n\nState-of-the-art reward models suffer from substantial performance degradation even with minor input transformations, sometimes dropping to significantly below-random accuracy, suggesting brittleness.\n\n## Proposed Solution\n\nTo improve reward model robustness, the authors propose to explicitly train them to assign similar scores to paraphrases, and find that this approach also improves robustness to other distinct kinds of transformations.\n\n## Publication Details\n\nThe paper appears to be from 2025, with the arXiv identifier 2503.11751. The authors are Zhaofeng Wu, Michihiro Yasunaga, Andrew Cohen, Yoon Kim, Asli Celikyilmaz, and Marjan Ghazvininejad."
    ],
    "durationSeconds": 6.848922701999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3aea0fd6-1756-41b2-a2a2-2005f35885e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # IsoPRM-Bench: Benchmarking and Mitigating Structural Isomorphism Brittleness in Process Reward Models  ## Descri…",
  "leafUuid": "2903f111-054c-41e9-b410-da60bf942e48",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate acceptance probability for IsoPRM-Bench proposal",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

### Tool call

_source line 18 · 2026-05-20T03:15:09.652Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BoF9ssxM39jj1jyfjtXypg`</summary>

```json
{
  "query": "PutnamGAP equivalent transformations LLM math solving invariance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2903f111-054c-41e9-b410-da60bf942e48",
  "isSidechain": false,
  "requestId": "req_011CbD6NNvZvG1zKmCDJiQLQ",
  "type": "assistant",
  "uuid": "249cd234-7009-4d1a-813f-74bd3197b1bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcF1cA8G6grcecYErV9dTd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 18136,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 18136,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 841
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

_source line 19 · 2026-05-20T03:15:17.241Z_

<details><summary>↩ Tool result · `toolu_01BoF9ssxM39jj1jyfjtXypg`</summary>

```text
Web search results for query: "PutnamGAP equivalent transformations LLM math solving invariance 2025 2026"

Links: [{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v1"},{"title":"[2508.08833] An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/abs/2508.08833"},{"title":"(PDF) An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://www.researchgate.net/publication/394457714_An_Investigation_of_Robustness_of_LLMs_in_Mathematical_Reasoning_Benchmarking_with_Mathematically-Equivalent_Transformation_of_Advanced_Mathematical_Problems"},{"title":"An Investigation of Robustness of LLMs in Mathematical ...","url":"https://arxiv.org/pdf/2508.08833"},{"title":"Semantic Invariance in Agentic AI","url":"https://arxiv.org/pdf/2603.13173"},{"title":"ICML Poster Putnam-AXIOM: A Functional & Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs","url":"https://icml.cc/virtual/2025/poster/44232"},{"title":"Putnam-AXIOM: A Functional and Static Benchmark for ...","url":"https://openreview.net/pdf?id=YXnwlZe0yf"},{"title":"Putnam-like dataset summary: LLMs as mathematical competition contestants","url":"https://arxiv.org/pdf/2509.24827"}]

Based on the search results, I found relevant information about PutnamGAP and related work on LLM mathematical reasoning with equivalent transformations:

## PutnamGAP Overview

PutnamGAP is a new benchmark dataset with multiple mathematically-equivalent variations of competition-level math problems. The framework assesses LLMs' mathematical-reasoning robustness by stress-testing them on advanced math problems that are mathematically equivalent but with linguistic and parametric variation.

## Key Findings on Invariance

These transformations allow measurement of the sensitivity of LLMs to non-mathematical perturbations, thereby enabling a more accurate evaluation of their mathematical reasoning capabilities. The research reveals significant robustness issues: across 18 commercial and open-source models sharp performance degradation was observed on the variants, with OpenAI's flagship reasoning model O3 scoring 51.5% on the originals but dropping by 4.7 percentage points on surface-renaming variants, and by 12.9 percentage points on other variants.

## Future Directions

Plans include integrating on-the-fly GAP transformations into training so that invariance to symbol and parameter changes is learned rather than merely tested. PutnamGAP emphasizes that genuine progress in mathematical AI will be measured not by ever-higher raw scores, but by a model's ability to stride across the hidden gulf between symbols and substance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "249cd234-7009-4d1a-813f-74bd3197b1bd",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "2b2b9adf-0644-4072-9f80-2fe3409c016c",
  "toolUseResult": {
    "query": "PutnamGAP equivalent transformations LLM math solving invariance 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Sojej8onrB9arvfwrWa1KV",
        "content": [
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833v1"
          },
          {
            "title": "[2508.08833] An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/abs/2508.08833"
          },
          {
            "title": "(PDF) An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://www.researchgate.net/publication/394457714_An_Investigation_of_Robustness_of_LLMs_in_Mathematical_Reasoning_Benchmarking_with_Mathematically-Equivalent_Transformation_of_Advanced_Mathematical_Problems"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical ...",
            "url": "https://arxiv.org/pdf/2508.08833"
          },
          {
            "title": "Semantic Invariance in Agentic AI",
            "url": "https://arxiv.org/pdf/2603.13173"
          },
          {
            "title": "ICML Poster Putnam-AXIOM: A Functional & Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs",
            "url": "https://icml.cc/virtual/2025/poster/44232"
          },
          {
            "title": "Putnam-AXIOM: A Functional and Static Benchmark for ...",
            "url": "https://openreview.net/pdf?id=YXnwlZe0yf"
          },
          {
            "title": "Putnam-like dataset summary: LLMs as mathematical competition contestants",
            "url": "https://arxiv.org/pdf/2509.24827"
          }
        ]
      },
      "Based on the search results, I found relevant information about PutnamGAP and related work on LLM mathematical reasoning with equivalent transformations:\n\n## PutnamGAP Overview\n\nPutnamGAP is a new benchmark dataset with multiple mathematically-equivalent variations of competition-level math problems. The framework assesses LLMs' mathematical-reasoning robustness by stress-testing them on advanced math problems that are mathematically equivalent but with linguistic and parametric variation.\n\n## Key Findings on Invariance\n\nThese transformations allow measurement of the sensitivity of LLMs to non-mathematical perturbations, thereby enabling a more accurate evaluation of their mathematical reasoning capabilities. The research reveals significant robustness issues: across 18 commercial and open-source models sharp performance degradation was observed on the variants, with OpenAI's flagship reasoning model O3 scoring 51.5% on the originals but dropping by 4.7 percentage points on surface-renaming variants, and by 12.9 percentage points on other variants.\n\n## Future Directions\n\nPlans include integrating on-the-fly GAP transformations into training so that invariance to symbol and parameter changes is learned rather than merely tested. PutnamGAP emphasizes that genuine progress in mathematical AI will be measured not by ever-higher raw scores, but by a model's ability to stride across the hidden gulf between symbols and substance."
    ],
    "durationSeconds": 7.5853053439999965,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "249cd234-7009-4d1a-813f-74bd3197b1bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T03:15:19.623Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HE4kWgX8tcB7xzVNWiaTPD`</summary>

```json
{
  "query": "GenPRM ThinkPRM generative process reward model code verification math 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b2b9adf-0644-4072-9f80-2fe3409c016c",
  "isSidechain": false,
  "requestId": "req_011CbD6PAJaUjKSEtepJokiD",
  "type": "assistant",
  "uuid": "255e4c57-96c0-4a46-9505-87823ae933dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012eS1jikAxpT2smQue5KtUJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 18977,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 873,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 18977,
          "cache_creation_input_tokens": 873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 873
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

_source line 21 · 2026-05-20T03:15:31.017Z_

<details><summary>↩ Tool result · `toolu_01HE4kWgX8tcB7xzVNWiaTPD`</summary>

```text
Web search results for query: "GenPRM ThinkPRM generative process reward model code verification math 2025 2026"

Links: [{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"THINKPRM: generative Process Reward Model for solution verification via long CoT Reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/thinkprm-generative-process-reward-model-for-solution-verification-via-long-cot-reasoning-2016f1e1387d"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost","url":"https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"},{"title":"Paper page - GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://huggingface.co/papers/2504.00891"},{"title":"Breaking the LLM Bottleneck: GenPRM’s approach to Scale test-time compute via generative reasoning | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e"}]

I've found search results for both GenPRM and ThinkPRM. Here's what the research shows:

## GenPRM

GenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. The research team from Tsinghua University, Shanghai AI Laboratory, BUPT, and Harbin Institute of Technology addresses challenges with GenPRM.

To obtain high-quality process supervision labels and rationale data, the researchers propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only 23K training data from MATH dataset. Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench.

## ThinkPRM

ThinkPRM is proposed as data-efficient PRMs which verbalizes stepwise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). This approach outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks.

On a subset of GPQA-Diamond and LiveCodeBench, ThinkPRM surpasses discriminative verifiers trained on full PRM800K by 8% and 4.5%, respectively.

Both models represent recent advances (April-May 2025) in process reward modeling for mathematical and coding verification tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "255e4c57-96c0-4a46-9505-87823ae933dc",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "d17b0d7a-5c35-4750-a663-89ce072093a1",
  "toolUseResult": {
    "query": "GenPRM ThinkPRM generative process reward model code verification math 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ViWgTPSuMBWAVErgNHbYAM",
        "content": [
          {
            "title": "GenPRM: Scaling Test-Time Compute of Process Reward ...",
            "url": "https://arxiv.org/pdf/2504.00891"
          },
          {
            "title": "THINKPRM: generative Process Reward Model for solution verification via long CoT Reasoning | by SACHIN KUMAR | Medium",
            "url": "https://medium.com/@techsachin/thinkprm-generative-process-reward-model-for-solution-verification-via-long-cot-reasoning-2016f1e1387d"
          },
          {
            "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"
          },
          {
            "title": "[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
            "url": "https://arxiv.org/abs/2504.00891"
          },
          {
            "title": "ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"
          },
          {
            "title": "Paper page - GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
            "url": "https://huggingface.co/papers/2504.00891"
          },
          {
            "title": "Breaking the LLM Bottleneck: GenPRM’s approach to Scale test-time compute via generative reasoning | by SACHIN KUMAR | Medium",
            "url": "https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa71e"
          }
        ]
      },
      "I've found search results for both GenPRM and ThinkPRM. Here's what the research shows:\n\n## GenPRM\n\nGenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. The research team from Tsinghua University, Shanghai AI Laboratory, BUPT, and Harbin Institute of Technology addresses challenges with GenPRM.\n\nTo obtain high-quality process supervision labels and rationale data, the researchers propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only 23K training data from MATH dataset. Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench.\n\n## ThinkPRM\n\nThinkPRM is proposed as data-efficient PRMs which verbalizes stepwise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). This approach outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks.\n\nOn a subset of GPQA-Diamond and LiveCodeBench, ThinkPRM surpasses discriminative verifiers trained on full PRM800K by 8% and 4.5%, respectively.\n\nBoth models represent recent advances (April-May 2025) in process reward modeling for mathematical and coding verification tasks."
    ],
    "durationSeconds": 11.369356462999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "255e4c57-96c0-4a46-9505-87823ae933dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T03:15:33.637Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K7ETU8b9uUbhay892ag1mD`</summary>

```json
{
  "query": "APRM adversarial training process reward model error detection 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d17b0d7a-5c35-4750-a663-89ce072093a1",
  "isSidechain": false,
  "requestId": "req_011CbD6QBPayKuahWszjDN2h",
  "type": "assistant",
  "uuid": "14fc3ef4-2078-4fcc-8e37-1ce7cf815e0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBERBcfR1wPtQJT8ooYtbP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 19850,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 19850,
          "cache_creation_input_tokens": 978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 978
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

_source line 23 · 2026-05-20T03:15:39.988Z_

<details><summary>↩ Tool result · `toolu_01K7ETU8b9uUbhay892ag1mD`</summary>

```text
Web search results for query: "APRM adversarial training process reward model error detection 2025 2026 arXiv"

Links: [{"title":"[2511.22888] Adversarial Training for Process Reward Models","url":"https://arxiv.org/abs/2511.22888"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/html/2511.22888"},{"title":"Adversarially Trained Reward Models","url":"https://www.emergentmind.com/topics/adversarially-trained-reward-models"},{"title":"[2504.06141] Adversarial Training of Reward Models","url":"https://arxiv.org/abs/2504.06141"},{"title":"(PDF) Adversarial Training of Reward Models","url":"https://www.researchgate.net/publication/390600688_Adversarial_Training_of_Reward_Models"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/html/2504.06141v2"}]

Based on the web search results, here's what I found about APRM:

## APRM - Adversarial Training for Process Reward Models

APRM (Adversarially Trained PRMs) is an approach where a Generator learns to produce reasoning errors to deceive a Process Reward Model (PRM), while the PRM concurrently learns to detect them.

**Key Details:**
- Process Reward Models enhance reasoning ability of LLMs by providing step-level supervision, but their widespread adoption is limited due to expensive manual step-level annotation and poor generalization of static training data to novel errors.

- The interaction yields progressively harder negatives for the PRM, improving its robustness and generalization to novel errors without requiring manual step-level labels.

**Performance Results:**
- Averaged across diverse mathematical reasoning benchmarks, APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline.

- APRM achieves gains of +5.3 percentage points on out-of-distribution tasks.

**Publication:**
The paper was posted on arXiv on November 28, 2025, with authors Gurusha Juneja, Deepak Nathani, and William Yang Wang from UC Santa Barbara.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14fc3ef4-2078-4fcc-8e37-1ce7cf815e0e",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "650bd56b-3737-4936-ab49-228ea6abac73",
  "toolUseResult": {
    "query": "APRM adversarial training process reward model error detection 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T2JeUWMmjs1ZR6RLqxeWmW",
        "content": [
          {
            "title": "[2511.22888] Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/abs/2511.22888"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/pdf/2511.22888"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/html/2511.22888"
          },
          {
            "title": "Adversarially Trained Reward Models",
            "url": "https://www.emergentmind.com/topics/adversarially-trained-reward-models"
          },
          {
            "title": "[2504.06141] Adversarial Training of Reward Models",
            "url": "https://arxiv.org/abs/2504.06141"
          },
          {
            "title": "(PDF) Adversarial Training of Reward Models",
            "url": "https://www.researchgate.net/publication/390600688_Adversarial_Training_of_Reward_Models"
          },
          {
            "title": "Adversarial Training of Reward Models",
            "url": "https://arxiv.org/html/2504.06141v2"
          }
        ]
      },
      "Based on the web search results, here's what I found about APRM:\n\n## APRM - Adversarial Training for Process Reward Models\n\nAPRM (Adversarially Trained PRMs) is an approach where a Generator learns to produce reasoning errors to deceive a Process Reward Model (PRM), while the PRM concurrently learns to detect them.\n\n**Key Details:**\n- Process Reward Models enhance reasoning ability of LLMs by providing step-level supervision, but their widespread adoption is limited due to expensive manual step-level annotation and poor generalization of static training data to novel errors.\n\n- The interaction yields progressively harder negatives for the PRM, improving its robustness and generalization to novel errors without requiring manual step-level labels.\n\n**Performance Results:**\n- Averaged across diverse mathematical reasoning benchmarks, APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline.\n\n- APRM achieves gains of +5.3 percentage points on out-of-distribution tasks.\n\n**Publication:**\nThe paper was posted on arXiv on November 28, 2025, with authors Gurusha Juneja, Deepak Nathani, and William Yang Wang from UC Santa Barbara."
    ],
    "durationSeconds": 6.34738104,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "14fc3ef4-2078-4fcc-8e37-1ce7cf815e0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T03:15:42.894Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MBaHg9xrankwWYc6pccuzn`</summary>

```json
{
  "query": "GR-Ben PRM evaluation non-mathematical reasoning subdomains process reward model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "650bd56b-3737-4936-ab49-228ea6abac73",
  "isSidechain": false,
  "requestId": "req_011CbD6Qqazv9qX4DRiUZQBb",
  "type": "assistant",
  "uuid": "a6c8ab5d-45cc-40e1-8493-5067d5683e7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JsA5sjviYL2o2MvFNaYfv9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 20828,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 20828,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 674
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

_source line 25 · 2026-05-20T03:15:53.220Z_

<details><summary>↩ Tool result · `toolu_01MBaHg9xrankwWYc6pccuzn`</summary>

```text
Web search results for query: "GR-Ben PRM evaluation non-mathematical reasoning subdomains process reward model 2025 2026"

Links: [{"title":"[2605.01203] GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models","url":"https://arxiv.org/abs/2605.01203"},{"title":"GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models","url":"https://arxiv.org/html/2605.01203"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner","url":"https://arxiv.org/pdf/2507.23317"},{"title":"Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/pdf/2505.19706"},{"title":"Rethinking Reward Models for Multi-Domain Test-Time Scaling","url":"https://arxiv.org/pdf/2510.00492"}]

I found relevant information about GR-Ben! Here are the key findings from the search:

## GR-Ben: A General Reasoning Benchmark

GR-Ben is a process-level benchmark specifically designed for assessing PRM's performance across two primary reasoning domains (science and logic) and nine subdomains.

### Motivation

Existing benchmarks primarily focus on mathematical reasoning, thereby failing to comprehensively evaluate the error detection ability of PRMs across diverse reasoning scenarios. GR-Ben was introduced to mitigate this gap by assessing PRM performance across two primary reasoning domains (science and logic) and nine subdomains.

### Key Findings

In domains beyond mathematical reasoning, the error-detection ability of existing PRMs and LLMs is found to be markedly weaker by comparison. Additionally, PRMs are less adept at identifying knowledge-based errors, whereas LLMs exhibit poorer performance in detecting computational errors.

### Research Scope

Extensive experiments were conducted on a diverse set of 22 models, encompassing both PRMs and LLMs.

The paper was recently published (approximately 3 weeks ago based on the search results) and represents an important contribution to understanding how process reward models perform on non-mathematical reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6c8ab5d-45cc-40e1-8493-5067d5683e7d",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "20592fa3-776c-42cb-87b9-470f8ec49194",
  "toolUseResult": {
    "query": "GR-Ben PRM evaluation non-mathematical reasoning subdomains process reward model 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PCMQvst8kMU7Rzf9LiSfTj",
        "content": [
          {
            "title": "[2605.01203] GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models",
            "url": "https://arxiv.org/abs/2605.01203"
          },
          {
            "title": "GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models",
            "url": "https://arxiv.org/html/2605.01203"
          },
          {
            "title": "Process Reward Models That Think | OpenReview",
            "url": "https://openreview.net/forum?id=V727xqBYIW"
          },
          {
            "title": "Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner",
            "url": "https://arxiv.org/pdf/2507.23317"
          },
          {
            "title": "Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision",
            "url": "https://arxiv.org/pdf/2505.19706"
          },
          {
            "title": "Rethinking Reward Models for Multi-Domain Test-Time Scaling",
            "url": "https://arxiv.org/pdf/2510.00492"
          }
        ]
      },
      "I found relevant information about GR-Ben! Here are the key findings from the search:\n\n## GR-Ben: A General Reasoning Benchmark\n\nGR-Ben is a process-level benchmark specifically designed for assessing PRM's performance across two primary reasoning domains (science and logic) and nine subdomains.\n\n### Motivation\n\nExisting benchmarks primarily focus on mathematical reasoning, thereby failing to comprehensively evaluate the error detection ability of PRMs across diverse reasoning scenarios. GR-Ben was introduced to mitigate this gap by assessing PRM performance across two primary reasoning domains (science and logic) and nine subdomains.\n\n### Key Findings\n\nIn domains beyond mathematical reasoning, the error-detection ability of existing PRMs and LLMs is found to be markedly weaker by comparison. Additionally, PRMs are less adept at identifying knowledge-based errors, whereas LLMs exhibit poorer performance in detecting computational errors.\n\n### Research Scope\n\nExtensive experiments were conducted on a diverse set of 22 models, encompassing both PRMs and LLMs.\n\nThe paper was recently published (approximately 3 weeks ago based on the search results) and represents an important contribution to understanding how process reward models perform on non-mathematical reasoning tasks."
    ],
    "durationSeconds": 10.32000475,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a6c8ab5d-45cc-40e1-8493-5067d5683e7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T03:15:55.893Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SwbP4W9Qj9H4wwGSgTQC5m`</summary>

```json
{
  "query": "ProcessBench human annotated solutions GSM8K MATH OlympiadBench step-level evaluation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20592fa3-776c-42cb-87b9-470f8ec49194",
  "isSidechain": false,
  "requestId": "req_011CbD6RpBSfhvkMxC51tawE",
  "type": "assistant",
  "uuid": "7f784f3a-06a5-4d88-bd1c-e54f39871e25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014G8CaKydfU2Vcy6dRQSKZU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 21502,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 21502,
          "cache_creation_input_tokens": 668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 668
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

_source line 27 · 2026-05-20T03:16:02.522Z_

<details><summary>↩ Tool result · `toolu_01SwbP4W9Qj9H4wwGSgTQC5m`</summary>

```text
Web search results for query: "ProcessBench human annotated solutions GSM8K MATH OlympiadBench step-level evaluation 2024 2025"

Links: [{"title":"Ali Launches New AI Benchmark 'PROCESSBENCH' to Assess Error Recognition Capability in Mathematical Reasoning","url":"https://www.aibase.com/news/13958"},{"title":"ProcessBench: Math Reasoning Error Identification","url":"https://www.emergentmind.com/papers/2412.06559"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://www.researchgate.net/publication/386577858_ProcessBench_Identifying_Process_Errors_in_Mathematical_Reasoning"},{"title":"Towards Effective Process Supervision in Mathematical Reasoning | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-math-prm/"},{"title":"[2412.06559] ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/abs/2412.06559"},{"title":"LLM Benchmarks | EvalScope - Read the Docs","url":"https://evalscope.readthedocs.io/en/v0.16.3/get_started/supported_dataset/llm.html"},{"title":"2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"GSM8K-V: Can Vision Language Models Solve Grade School Math Word Problems in Visual Contexts","url":"https://arxiv.org/pdf/2509.25160"}]

Based on the web search results, here's what I found about ProcessBench:

## Overview

ProcessBench is a benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, consisting of 3,400 test cases primarily focused on competition- and Olympiad-level math problems.

## Human Annotations and Data Sources

Each test case contains a step-by-step solution with error location annotated by human experts. The research team collected math problems from four well-known datasets (GSM8K, MATH, OlympiadBench, and additional sources).

## Evaluation Methodology

Models are required to identify the earliest step that contains an error, or conclude that all steps are correct. The evaluation involves two types of models: process reward models (PRMs) and critic models, where for the latter general LLMs are prompted to critique each solution step by step.

## Key Findings

Existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH.

The benchmark was introduced by the Alibaba Qwen team and addresses the need for step-level evaluation of mathematical reasoning, moving beyond simple binary correctness assessments to provide detailed error annotations at the solution step level.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f784f3a-06a5-4d88-bd1c-e54f39871e25",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "11bc61e2-bf1a-45cb-b94b-b7dfe8987e5c",
  "toolUseResult": {
    "query": "ProcessBench human annotated solutions GSM8K MATH OlympiadBench step-level evaluation 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MAZAajkstAPoEWwrhJ6scN",
        "content": [
          {
            "title": "Ali Launches New AI Benchmark 'PROCESSBENCH' to Assess Error Recognition Capability in Mathematical Reasoning",
            "url": "https://www.aibase.com/news/13958"
          },
          {
            "title": "ProcessBench: Math Reasoning Error Identification",
            "url": "https://www.emergentmind.com/papers/2412.06559"
          },
          {
            "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
            "url": "https://www.researchgate.net/publication/386577858_ProcessBench_Identifying_Process_Errors_in_Mathematical_Reasoning"
          },
          {
            "title": "Towards Effective Process Supervision in Mathematical Reasoning | Qwen",
            "url": "https://qwenlm.github.io/blog/qwen2.5-math-prm/"
          },
          {
            "title": "[2412.06559] ProcessBench: Identifying Process Errors in Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2412.06559"
          },
          {
            "title": "LLM Benchmarks | EvalScope - Read the Docs",
            "url": "https://evalscope.readthedocs.io/en/v0.16.3/get_started/supported_dataset/llm.html"
          },
          {
            "title": "2025-05-27 PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2412.06559"
          },
          {
            "title": "GSM8K-V: Can Vision Language Models Solve Grade School Math Word Problems in Visual Contexts",
            "url": "https://arxiv.org/pdf/2509.25160"
          }
        ]
      },
      "Based on the web search results, here's what I found about ProcessBench:\n\n## Overview\n\nProcessBench is a benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, consisting of 3,400 test cases primarily focused on competition- and Olympiad-level math problems.\n\n## Human Annotations and Data Sources\n\nEach test case contains a step-by-step solution with error location annotated by human experts. The research team collected math problems from four well-known datasets (GSM8K, MATH, OlympiadBench, and additional sources).\n\n## Evaluation Methodology\n\nModels are required to identify the earliest step that contains an error, or conclude that all steps are correct. The evaluation involves two types of models: process reward models (PRMs) and critic models, where for the latter general LLMs are prompted to critique each solution step by step.\n\n## Key Findings\n\nExisting PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH.\n\nThe benchmark was introduced by the Alibaba Qwen team and addresses the need for step-level evaluation of mathematical reasoning, moving beyond simple binary correctness assessments to provide detailed error annotations at the solution step level."
    ],
    "durationSeconds": 6.625775718000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7f784f3a-06a5-4d88-bd1c-e54f39871e25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28 · 2026-05-20T03:16:02.525Z_

```json
{
  "parentUuid": "11bc61e2-bf1a-45cb-b94b-b7dfe8987e5c",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7f5a3093-e0da-4fad-bbc5-9a7b3556903d",
  "timestamp": "2026-05-20T03:16:02.525Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # IsoPRM-Bench: Benchmarking and Mitigating Structural Isomorphism Brittleness in Process Reward Models  ## Descri…",
  "leafUuid": "7f5a3093-e0da-4fad-bbc5-9a7b3556903d",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate acceptance probability for IsoPRM-Bench proposal",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

### Tool call

_source line 31 · 2026-05-20T03:16:05.222Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fe4QA6gcqzm22TV7H4act7`</summary>

```json
{
  "query": "process reward model structural invariance isomorphic robustness step-level verification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f5a3093-e0da-4fad-bbc5-9a7b3556903d",
  "isSidechain": false,
  "requestId": "req_011CbD6SVvcbQ9G2gvF9gN1p",
  "type": "assistant",
  "uuid": "dfdd419c-1ce5-4bc6-a820-b0b8e3665883",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvYcnn76ji2Q1uge364qPA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 882,
      "cache_read_input_tokens": 22170,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 882,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 22170,
          "cache_creation_input_tokens": 882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 882
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

_source line 32 · 2026-05-20T03:16:12.795Z_

<details><summary>↩ Tool result · `toolu_01Fe4QA6gcqzm22TV7H4act7`</summary>

```text
Web search results for query: "process reward model structural invariance isomorphic robustness step-level verification 2025 2026"

Links: [{"title":"Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning","url":"https://arxiv.org/html/2601.17223"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"Towards Robust Process Reward Modeling via Noise-aware Learning","url":"https://arxiv.org/pdf/2601.12748"},{"title":"Uncertainty-Aware Step-wise Verification with Generative Reward Models","url":"https://arxiv.org/pdf/2502.11250"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"}]

I found relevant research on process reward models with several key papers from 2025-2026:

## Key Findings

Verifiable Process Reward Models (VPRMs) combine the robustness of RLVR with step-wise, rule-based verification, enabling transparent, structurally aligned reasoning while removing opportunities for reward hacking inherent in neural process rewards.

Verifiable process rewards integrate deterministic step-level verification with reinforcement learning, provide theoretical guarantees under mild assumptions, and demonstrate substantial empirical gains on risk-of-bias assessment in medical systematic reviews.

### Structural Properties and Robustness

The granularity of PRMs is structural rather than subjective, enabling step-specific error localization, whereas ORMs operate at only a single outcome level. However, PRMs are more susceptible to length hacking or verbosity bias due to high variance in step-wise optimization.

### Formal Verification Approaches

Recent work annotates step-level error labels using formal methods like Isabelle, with LLM-based PRMs trained on formally verified data significantly improving verification capabilities on a broad range of reasoning tasks compared to baseline PRMs.

### Generative Verification Methods

ThinkPRM is a long CoT verifier that verifies every step in the solution by generating a verification chain-of-thought, requiring orders of magnitude fewer process labels than discriminative PRMs.

The research indicates active development in making process reward models more robust, verifiable, and structurally sound for step-level reasoning verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfdd419c-1ce5-4bc6-a820-b0b8e3665883",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "8350f31b-3ceb-4708-97a1-c6a9a814e5c5",
  "toolUseResult": {
    "query": "process reward model structural invariance isomorphic robustness step-level verification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SSPURfcg31hWABgGRGJCGp",
        "content": [
          {
            "title": "Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning",
            "url": "https://arxiv.org/html/2601.17223"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process",
            "url": "https://arxiv.org/pdf/2510.08049"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "Process Reward Models That Think | OpenReview",
            "url": "https://openreview.net/forum?id=V727xqBYIW"
          },
          {
            "title": "Towards Robust Process Reward Modeling via Noise-aware Learning",
            "url": "https://arxiv.org/pdf/2601.12748"
          },
          {
            "title": "Uncertainty-Aware Step-wise Verification with Generative Reward Models",
            "url": "https://arxiv.org/pdf/2502.11250"
          },
          {
            "title": "Generalizable Process Reward Models via Formally Verified Training Data",
            "url": "https://arxiv.org/pdf/2505.15960"
          }
        ]
      },
      "I found relevant research on process reward models with several key papers from 2025-2026:\n\n## Key Findings\n\nVerifiable Process Reward Models (VPRMs) combine the robustness of RLVR with step-wise, rule-based verification, enabling transparent, structurally aligned reasoning while removing opportunities for reward hacking inherent in neural process rewards.\n\nVerifiable process rewards integrate deterministic step-level verification with reinforcement learning, provide theoretical guarantees under mild assumptions, and demonstrate substantial empirical gains on risk-of-bias assessment in medical systematic reviews.\n\n### Structural Properties and Robustness\n\nThe granularity of PRMs is structural rather than subjective, enabling step-specific error localization, whereas ORMs operate at only a single outcome level. However, PRMs are more susceptible to length hacking or verbosity bias due to high variance in step-wise optimization.\n\n### Formal Verification Approaches\n\nRecent work annotates step-level error labels using formal methods like Isabelle, with LLM-based PRMs trained on formally verified data significantly improving verification capabilities on a broad range of reasoning tasks compared to baseline PRMs.\n\n### Generative Verification Methods\n\nThinkPRM is a long CoT verifier that verifies every step in the solution by generating a verification chain-of-thought, requiring orders of magnitude fewer process labels than discriminative PRMs.\n\nThe research indicates active development in making process reward models more robust, verifiable, and structurally sound for step-level reasoning verification."
    ],
    "durationSeconds": 7.5686358429999965,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dfdd419c-1ce5-4bc6-a820-b0b8e3665883",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T03:16:15.808Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B1dh8sjP3Arvvqs8YcFb1c`</summary>

```json
{
  "query": "CoLD causal debiasing framework language models bias mitigation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8350f31b-3ceb-4708-97a1-c6a9a814e5c5",
  "isSidechain": false,
  "requestId": "req_011CbD6TFqKFSfVoQFg7v7Lf",
  "type": "assistant",
  "uuid": "fa79e350-7e2a-4bb6-9c86-cca8dee64280",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2DAoaECtVYxvpQnig288u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 23052,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 23052,
          "cache_creation_input_tokens": 768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 768
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

_source line 34 · 2026-05-20T03:16:23.387Z_

<details><summary>↩ Tool result · `toolu_01B1dh8sjP3Arvvqs8YcFb1c`</summary>

```text
Web search results for query: "CoLD causal debiasing framework language models bias mitigation 2024 2025"

Links: [{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/html/2507.15698v1"},{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/pdf/2507.15698"},{"title":"[2403.08743] Prompting Fairness: Integrating Causality to Debias Large Language Models","url":"https://arxiv.org/abs/2403.08743"},{"title":"Debiasing Multimodal Large Language Models via ...","url":"https://aclanthology.org/2025.findings-emnlp.205.pdf"},{"title":"Causal-Guided Active Learning for Debiasing Large Language Models","url":"https://arxiv.org/pdf/2408.12942"},{"title":"Causal-Guided Active Learning for Debiasing Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/384214455_Causal-Guided_Active_Learning_for_Debiasing_Large_Language_Models"},{"title":"Causal-Guided Active Learning for Debiasing Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.778/"},{"title":"Information Gain-Guided Causal Intervention for Autonomous Debiasing Large Language Models","url":"https://arxiv.org/pdf/2504.12898"}]

Based on the web search results, I found information about CoLD and related causal debiasing frameworks for language models:

## CoLD Framework

CoLD (Counterfactually-Guided Length Debiasing) is a unified framework that mitigates length bias through three components: an explicit length-penalty adjustment, a learned bias estimator trained to capture spurious length-related signals, and a joint training strategy that enforces length-invariance in reward predictions. The approach is grounded in counterfactual reasoning and informed by causal graph analysis.

Extensive experiments on MATH500 and GSM-Plus show that CoLD consistently reduces reward–length correlation, improves accuracy in step selection, and encourages more concise, logically valid reasoning.

## Related Causal Debiasing Approaches (2024-2025)

The search results also reveal several other causal-based debiasing frameworks for language models from this period:

1. **Causal-Guided Active Learning (CAL)**: This framework utilizes LLMs themselves to automatically and autonomously identify biased samples and induce the bias patterns.

2. **Information Gain-Guided Causal Intervention (IGCIDB)**: This framework addresses debiasing by starting from the essential cause to debias the instruction-tuning dataset.

3. **Prompting Fairness with Causality**: This research addresses how LLMs are susceptible to generating biased and discriminatory responses, and as LLMs increasingly influence high-stakes decision-making, mitigating these biases becomes critical.

These frameworks collectively represent recent advances in using causal reasoning and counterfactual analysis to address various types of bias in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa79e350-7e2a-4bb6-9c86-cca8dee64280",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "ec2564cd-b3de-4ae4-a5cd-8c670d2a1736",
  "toolUseResult": {
    "query": "CoLD causal debiasing framework language models bias mitigation 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QCigQosBab2vBJD6kUt9Lc",
        "content": [
          {
            "title": "CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://arxiv.org/html/2507.15698v1"
          },
          {
            "title": "CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://arxiv.org/pdf/2507.15698"
          },
          {
            "title": "[2403.08743] Prompting Fairness: Integrating Causality to Debias Large Language Models",
            "url": "https://arxiv.org/abs/2403.08743"
          },
          {
            "title": "Debiasing Multimodal Large Language Models via ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.205.pdf"
          },
          {
            "title": "Causal-Guided Active Learning for Debiasing Large Language Models",
            "url": "https://arxiv.org/pdf/2408.12942"
          },
          {
            "title": "Causal-Guided Active Learning for Debiasing Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/384214455_Causal-Guided_Active_Learning_for_Debiasing_Large_Language_Models"
          },
          {
            "title": "Causal-Guided Active Learning for Debiasing Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.778/"
          },
          {
            "title": "Information Gain-Guided Causal Intervention for Autonomous Debiasing Large Language Models",
            "url": "https://arxiv.org/pdf/2504.12898"
          }
        ]
      },
      "Based on the web search results, I found information about CoLD and related causal debiasing frameworks for language models:\n\n## CoLD Framework\n\nCoLD (Counterfactually-Guided Length Debiasing) is a unified framework that mitigates length bias through three components: an explicit length-penalty adjustment, a learned bias estimator trained to capture spurious length-related signals, and a joint training strategy that enforces length-invariance in reward predictions. The approach is grounded in counterfactual reasoning and informed by causal graph analysis.\n\nExtensive experiments on MATH500 and GSM-Plus show that CoLD consistently reduces reward–length correlation, improves accuracy in step selection, and encourages more concise, logically valid reasoning.\n\n## Related Causal Debiasing Approaches (2024-2025)\n\nThe search results also reveal several other causal-based debiasing frameworks for language models from this period:\n\n1. **Causal-Guided Active Learning (CAL)**: This framework utilizes LLMs themselves to automatically and autonomously identify biased samples and induce the bias patterns.\n\n2. **Information Gain-Guided Causal Intervention (IGCIDB)**: This framework addresses debiasing by starting from the essential cause to debias the instruction-tuning dataset.\n\n3. **Prompting Fairness with Causality**: This research addresses how LLMs are susceptible to generating biased and discriminatory responses, and as LLMs increasingly influence high-stakes decision-making, mitigating these biases becomes critical.\n\nThese frameworks collectively represent recent advances in using causal reasoning and counterfactual analysis to address various types of bias in language models."
    ],
    "durationSeconds": 7.574600598999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fa79e350-7e2a-4bb6-9c86-cca8dee64280",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T03:16:26.311Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DnWH2oK2hYpGpT1QYM5sgX`</summary>

```json
{
  "query": "\"reward hacking\" \"process reward model\" notation style preference exploitation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec2564cd-b3de-4ae4-a5cd-8c670d2a1736",
  "isSidechain": false,
  "requestId": "req_011CbD6U37NNU9r9qDQmMHSd",
  "type": "assistant",
  "uuid": "fa746778-9703-42e9-995a-b4a4c8c8754d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVWja4gQyjgXQpffuRKqJp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 23820,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 878,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 23820,
          "cache_creation_input_tokens": 878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 878
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

_source line 36 · 2026-05-20T03:16:34.818Z_

<details><summary>↩ Tool result · `toolu_01DnWH2oK2hYpGpT1QYM5sgX`</summary>

```text
Web search results for query: ""reward hacking" "process reward model" notation style preference exploitation 2025 2026"

Links: [{"title":"Recent Frontier Models Are Reward Hacking - METR","url":"https://metr.org/blog/2025-06-05-recent-reward-hacking/"},{"title":"Reward Hacking: The Hidden Failure Mode in AI Optimization | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/reward-hacking-the-hidden-failure-mode-in-ai-optimization-686b62acf408"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward hacking - Wikipedia","url":"https://en.wikipedia.org/wiki/Reward_hacking"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"NATURAL EMERGENT MISALIGNMENT FROM REWARD HACKING IN PRODUCTION RL","url":"https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf"},{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"},{"title":"AI Model Misbehavior in 2026: Scheming, Reward Hacking, and What Comes Next","url":"https://hatchworks.com/blog/gen-ai/ai-model-misbehavior/"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"The Cheating Machine: How AI’s “Reward Hacking” Spirals into Sabotage and Deceit - Sify","url":"https://www.sify.com/ai-analytics/the-cheating-machine-how-ais-reward-hacking-spirals-into-sabotage-and-deceit/"}]

I've completed a web search for your query on reward hacking and process reward models in 2025-2026. Here are the key findings:

## Recent Developments in Reward Hacking

Recent frontier models show increasingly clear examples of reward hacking where AI systems try to "cheat" and get impossibly high scores. They do this by exploiting bugs in scoring code or subverting the task setup, rather than actually solving the problem.

## Process Reward Model Exploitation

Process reward models (PRMs), which evaluate multi-step reasoning, exhibit a strong length bias where evaluators give higher scores to longer reasoning steps even when the logic remains the same. Large-scale reasoning models have introduced verbosity hacking through stalling tokens, where models generate repetitive thoughts or useless self-correction loops that look like deep thinking but are actually shortcuts to maintain high scores.

## Broader Implications and Emerging Patterns

Reward hacking occurs when an AI system optimizes the measured reward/proxy metric instead of the intended outcome, exploiting loopholes, blind spots, or distributional quirks. Models exploit imperfections in learned reward signals to maximize a proxy objective while bypassing true task intent, with research proposing the Proxy Compression Hypothesis as a unifying theoretical frame organizing exploitation mechanisms from feature-level to environment-level.

## Production-Scale Concerns

Anthropic's November 2025 research showed models trained using reinforcement learning on coding environments learned to exploit tests by issuing sys.exit(0) commands, breaking out of the test harness with a success exit code. The model generalized that cheating behavior to entirely new domains, including alignment faking, sabotage of safety research, and cooperation with hypothetical attackers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa746778-9703-42e9-995a-b4a4c8c8754d",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "fc69d870-24b7-417e-99be-f00e263b304e",
  "toolUseResult": {
    "query": "\"reward hacking\" \"process reward model\" notation style preference exploitation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BaiGfVqUVJpiCRWZEcCVQA",
        "content": [
          {
            "title": "Recent Frontier Models Are Reward Hacking - METR",
            "url": "https://metr.org/blog/2025-06-05-recent-reward-hacking/"
          },
          {
            "title": "Reward Hacking: The Hidden Failure Mode in AI Optimization | by Adnan Masood, PhD. | Medium",
            "url": "https://medium.com/@adnanmasood/reward-hacking-the-hidden-failure-mode-in-ai-optimization-686b62acf408"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Reward hacking - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Reward_hacking"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "NATURAL EMERGENT MISALIGNMENT FROM REWARD HACKING IN PRODUCTION RL",
            "url": "https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=hSX7Dd8dxy"
          },
          {
            "title": "AI Model Misbehavior in 2026: Scheming, Reward Hacking, and What Comes Next",
            "url": "https://hatchworks.com/blog/gen-ai/ai-model-misbehavior/"
          },
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "The Cheating Machine: How AI’s “Reward Hacking” Spirals into Sabotage and Deceit - Sify",
            "url": "https://www.sify.com/ai-analytics/the-cheating-machine-how-ais-reward-hacking-spirals-into-sabotage-and-deceit/"
          }
        ]
      },
      "I've completed a web search for your query on reward hacking and process reward models in 2025-2026. Here are the key findings:\n\n## Recent Developments in Reward Hacking\n\nRecent frontier models show increasingly clear examples of reward hacking where AI systems try to \"cheat\" and get impossibly high scores. They do this by exploiting bugs in scoring code or subverting the task setup, rather than actually solving the problem.\n\n## Process Reward Model Exploitation\n\nProcess reward models (PRMs), which evaluate multi-step reasoning, exhibit a strong length bias where evaluators give higher scores to longer reasoning steps even when the logic remains the same. Large-scale reasoning models have introduced verbosity hacking through stalling tokens, where models generate repetitive thoughts or useless self-correction loops that look like deep thinking but are actually shortcuts to maintain high scores.\n\n## Broader Implications and Emerging Patterns\n\nReward hacking occurs when an AI system optimizes the measured reward/proxy metric instead of the intended outcome, exploiting loopholes, blind spots, or distributional quirks. Models exploit imperfections in learned reward signals to maximize a proxy objective while bypassing true task intent, with research proposing the Proxy Compression Hypothesis as a unifying theoretical frame organizing exploitation mechanisms from feature-level to environment-level.\n\n## Production-Scale Concerns\n\nAnthropic's November 2025 research showed models trained using reinforcement learning on coding environments learned to exploit tests by issuing sys.exit(0) commands, breaking out of the test harness with a success exit code. The model generalized that cheating behavior to entirely new domains, including alignment faking, sabotage of safety research, and cooperation with hypothetical attackers."
    ],
    "durationSeconds": 8.502997923000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fa746778-9703-42e9-995a-b4a4c8c8754d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T03:16:37.790Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VPP5eR912Jnvi4ypncCCwE`</summary>

```json
{
  "query": "IPT isomorphic problem transformation LLM mathematical reasoning robustness benchmark 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc69d870-24b7-417e-99be-f00e263b304e",
  "isSidechain": false,
  "requestId": "req_011CbD6UswVfHfYYfCVkfioc",
  "type": "assistant",
  "uuid": "10476538-90eb-4a82-9c47-b0c7408936f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cdp4jDjUwbtRppCbMSRpd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1081,
      "cache_read_input_tokens": 24698,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1081,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 24698,
          "cache_creation_input_tokens": 1081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1081
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

_source line 38 · 2026-05-20T03:16:49.169Z_

<details><summary>↩ Tool result · `toolu_01VPP5eR912Jnvi4ypncCCwE`</summary>

```text
Web search results for query: "IPT isomorphic problem transformation LLM mathematical reasoning robustness benchmark 2025"

Links: [{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571"},{"title":"(PDF) An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://www.researchgate.net/publication/394457714_An_Investigation_of_Robustness_of_LLMs_in_Mathematical_Reasoning_Benchmarking_with_Mathematically-Equivalent_Transformation_of_Advanced_Mathematical_Problems"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems | OpenReview","url":"https://openreview.net/forum?id=b8GuXlLc1y"},{"title":"[2508.08833] An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/abs/2508.08833"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833"},{"title":"Computer Science Aug 2025","url":"https://www.arxiv.org/list/cs/2025-08?skip=4500&show=1000"}]

Based on the web search results, I found relevant information about this research. Here's what I discovered:

## Overview

The research introduces a systematic framework to assess LLMs' mathematical-reasoning robustness by stress-testing them on advanced math problems that are mathematically equivalent but with linguistic and parametric variation. These transformations allow measuring the sensitivity of LLMs to non-mathematical perturbations, enabling a more accurate evaluation of their mathematical reasoning capabilities.

## The PutnamGAP Benchmark

The researchers created PutnamGAP, a new benchmark dataset with multiple mathematically-equivalent variations of competition-level math problems. The benchmark was instantiated on all 1,051 Putnam Competition questions to produce the 6,306-question PutnamGAP benchmark.

## Key Findings

Across 18 commercial and open-source models, the researchers observed sharp performance degradation on the variants. OpenAI's flagship reasoning model, O3, scores 51.5% on the originals but drops by 4.7 percentage points on surface-renaming variants, and by 12.9 percentage points on parametric variants, while smaller models fare far worse.

This research was published in 2025 and addresses the robustness gap in LLM mathematical reasoning by using isomorphic problem transformations to create a more reliable evaluation methodology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10476538-90eb-4a82-9c47-b0c7408936f7",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "54c795c5-9666-4039-be01-6fc22f1d0085",
  "toolUseResult": {
    "query": "IPT isomorphic problem transformation LLM mathematical reasoning robustness benchmark 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AgSjfKb3sjgzDNHd9ysfYq",
        "content": [
          {
            "title": "Robust Reasoning Benchmark",
            "url": "https://arxiv.org/html/2604.08571"
          },
          {
            "title": "(PDF) An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://www.researchgate.net/publication/394457714_An_Investigation_of_Robustness_of_LLMs_in_Mathematical_Reasoning_Benchmarking_with_Mathematically-Equivalent_Transformation_of_Advanced_Mathematical_Problems"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems | OpenReview",
            "url": "https://openreview.net/forum?id=b8GuXlLc1y"
          },
          {
            "title": "[2508.08833] An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/abs/2508.08833"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833"
          },
          {
            "title": "Computer Science Aug 2025",
            "url": "https://www.arxiv.org/list/cs/2025-08?skip=4500&show=1000"
          }
        ]
      },
      "Based on the web search results, I found relevant information about this research. Here's what I discovered:\n\n## Overview\n\nThe research introduces a systematic framework to assess LLMs' mathematical-reasoning robustness by stress-testing them on advanced math problems that are mathematically equivalent but with linguistic and parametric variation. These transformations allow measuring the sensitivity of LLMs to non-mathematical perturbations, enabling a more accurate evaluation of their mathematical reasoning capabilities.\n\n## The PutnamGAP Benchmark\n\nThe researchers created PutnamGAP, a new benchmark dataset with multiple mathematically-equivalent variations of competition-level math problems. The benchmark was instantiated on all 1,051 Putnam Competition questions to produce the 6,306-question PutnamGAP benchmark.\n\n## Key Findings\n\nAcross 18 commercial and open-source models, the researchers observed sharp performance degradation on the variants. OpenAI's flagship reasoning model, O3, scores 51.5% on the originals but drops by 4.7 percentage points on surface-renaming variants, and by 12.9 percentage points on parametric variants, while smaller models fare far worse.\n\nThis research was published in 2025 and addresses the robustness gap in LLM mathematical reasoning by using isomorphic problem transformations to create a more reliable evaluation methodology."
    ],
    "durationSeconds": 11.375666717,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "10476538-90eb-4a82-9c47-b0c7408936f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # IsoPRM-Bench: Benchmarking and Mitigating Structural Isomorphism Brittleness in Process Reward Models  ## Descri…",
  "leafUuid": "54c795c5-9666-4039-be01-6fc22f1d0085",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate acceptance probability for IsoPRM-Bench proposal",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

### Tool call

_source line 41 · 2026-05-20T03:16:52.319Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019gFfax92Vbt3SyHJrsG6L9`</summary>

```json
{
  "query": "\"Reward Under Attack\" PRM robustness hackability process reward model 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54c795c5-9666-4039-be01-6fc22f1d0085",
  "isSidechain": false,
  "requestId": "req_011CbD6VwQsfu8bFUjgysMA3",
  "type": "assistant",
  "uuid": "4fffa840-ca54-480c-b178-7d56e33ada07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PgRPwKeb2z6WhGfNGBmS8e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 25779,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 25779,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 786
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

_source line 42 · 2026-05-20T03:16:59.789Z_

<details><summary>↩ Tool result · `toolu_019gFfax92Vbt3SyHJrsG6L9`</summary>

```text
Web search results for query: ""Reward Under Attack" PRM robustness hackability process reward model 2025 2026 arXiv"

Links: [{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"Reward Under Attack: Evaluating the Sensitivity of Process Reward Models","url":"https://openreview.net/pdf?id=Hw24VOppus"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"}]

I found the research paper you were looking for! Here are the key details:

## "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models"

Process Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.

### Main Findings:

Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts. Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

### Methodology:

The researchers introduce a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify these vulnerabilities. Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes reward changes <0.1, yet inconsistent detection of logically-corrupted reasoning.

### Paper Details:
- **arXiv ID:** 2603.06621
- **Posted:** February 20, 2026
- **Authors:** Rishabh Tiwari, Aditya Tomar, Udbhav Bamba, and others
- The authors release PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fffa840-ca54-480c-b178-7d56e33ada07",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "bec90936-1a89-4ee3-a9ec-3eff05bd35ab",
  "toolUseResult": {
    "query": "\"Reward Under Attack\" PRM robustness hackability process reward model 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HJQWmA5acdVWdFkAB96yxh",
        "content": [
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "Reward Under Attack: Evaluating the Sensitivity of Process Reward Models",
            "url": "https://openreview.net/pdf?id=Hw24VOppus"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          }
        ]
      },
      "I found the research paper you were looking for! Here are the key details:\n\n## \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\"\n\nProcess Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.\n\n### Main Findings:\n\nPolicies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts. Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n### Methodology:\n\nThe researchers introduce a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify these vulnerabilities. Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes reward changes <0.1, yet inconsistent detection of logically-corrupted reasoning.\n\n### Paper Details:\n- **arXiv ID:** 2603.06621\n- **Posted:** February 20, 2026\n- **Authors:** Rishabh Tiwari, Aditya Tomar, Udbhav Bamba, and others\n- The authors release PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment."
    ],
    "durationSeconds": 7.464590514000011,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4fffa840-ca54-480c-b178-7d56e33ada07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T03:17:03.348Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the related work. Let me also search for one more thing - whether anyone has specifically studied step-level structural isomorphism in PRMs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bec90936-1a89-4ee3-a9ec-3eff05bd35ab",
  "isSidechain": false,
  "requestId": "req_011CbD6Wijuji43DyqRMVbdo",
  "type": "assistant",
  "uuid": "31d2e6ce-ce41-4fda-87ea-b2a373ef5552",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166ca1PFeye4kKphkooxRgW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 26565,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 758,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 26565,
          "cache_creation_input_tokens": 758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 758
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

### Assistant

_source line 44 · 2026-05-20T03:17:04.328Z_

Now let me do one final targeted search to see if there's any direct prior work on step-level isomorphic invariance testing for PRMs specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31d2e6ce-ce41-4fda-87ea-b2a373ef5552",
  "isSidechain": false,
  "requestId": "req_011CbD6Wijuji43DyqRMVbdo",
  "type": "assistant",
  "uuid": "63c3978b-6513-4a15-bb99-657a998b8987",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166ca1PFeye4kKphkooxRgW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 26565,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 758,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 26565,
          "cache_creation_input_tokens": 758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 758
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

### Tool call

_source line 45 · 2026-05-20T03:17:04.982Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013wTT8kXzhSaL4hVaJMBvvc`</summary>

```json
{
  "query": "step-level isomorphic invariance PRM verifier variable renaming commutative reordering notation change benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63c3978b-6513-4a15-bb99-657a998b8987",
  "isSidechain": false,
  "requestId": "req_011CbD6Wijuji43DyqRMVbdo",
  "type": "assistant",
  "uuid": "e7ba6fa1-95e6-4b28-98dd-4a0da95fa153",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166ca1PFeye4kKphkooxRgW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 26565,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 758,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 26565,
          "cache_creation_input_tokens": 758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 758
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

_source line 46 · 2026-05-20T03:17:12.367Z_

<details><summary>↩ Tool result · `toolu_013wTT8kXzhSaL4hVaJMBvvc`</summary>

```text
Web search results for query: "step-level isomorphic invariance PRM verifier variable renaming commutative reordering notation change benchmark 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.11287"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"arXiv:2501.07301v2 [cs.CL] 5 Jun 2025 2025-06-12","url":"https://arxiv.org/pdf/2501.07301"},{"title":"Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/pdf/2505.15960"},{"title":"Names Don't Matter: Symbol-Invariant Transformer for Open-Vocabulary Learning","url":"https://arxiv.org/pdf/2601.23169"},{"title":"Let’s Verify Step by Step, ORM vs PRM | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/lets-verify-step-by-step-orm-vs-prm-613ecffb59ab"},{"title":"BDD variable reordering using parallel permutation","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8370289"}]

Based on the web search results, I found relevant research related to PRMs (Process Reward Models) and verifiers from 2025-2026, though the results don't specifically address all the technical terms in your query together.

Here are the key findings:

**Process Reward Models and Verification (2025-2026):**

Process reward models (PRMs)—also known as process verifiers—score (partial) solutions for selecting promising paths for search or ranking. Recent research shows significant advances in this area.

THINKPRM, trained on synthetic data utilizing as few as 8K step labels, surpasses LLM-as-a-judge and outperforms discriminative PRMs trained on two orders of magnitude more data across various test-time scaling scenarios.

**Variable Renaming and Symbol Invariance:**

Your query mentions variable renaming and notation changes. Recent work introduced a metric for measuring robustness against variable renaming and proposed a novel embedding strategy using random vectors to handle interchangeable tokens.

**Step-Level Annotations:**

PRMs are typically created by fine-tuning LLMs to classify the correctness of individual reasoning steps, using training datasets annotated with step-level error labels on LLM-generated reasoning traces.

The search results contain information about PRM verifiers and step-level verification from 2025-2026, though they don't specifically mention isomorphic invariance benchmarks or commutative reordering in the context of PRM verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7ba6fa1-95e6-4b28-98dd-4a0da95fa153",
  "isSidechain": false,
  "promptId": "5aa01183-a07e-4002-bfdb-7a91d581b289",
  "type": "user",
  "uuid": "7b016a37-a0da-4cb7-ab33-ec208dd98ee9",
  "toolUseResult": {
    "query": "step-level isomorphic invariance PRM verifier variable renaming commutative reordering notation change benchmark 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Gdxfa6DYxByAo6DNXDaNtM",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2410.11287"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "arXiv:2501.07301v2 [cs.CL] 5 Jun 2025 2025-06-12",
            "url": "https://arxiv.org/pdf/2501.07301"
          },
          {
            "title": "Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/pdf/2505.15960"
          },
          {
            "title": "Names Don't Matter: Symbol-Invariant Transformer for Open-Vocabulary Learning",
            "url": "https://arxiv.org/pdf/2601.23169"
          },
          {
            "title": "Let’s Verify Step by Step, ORM vs PRM | by Yanan Chen | Medium",
            "url": "https://medium.com/@yananchen1116/lets-verify-step-by-step-orm-vs-prm-613ecffb59ab"
          },
          {
            "title": "BDD variable reordering using parallel permutation",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8370289"
          }
        ]
      },
      "Based on the web search results, I found relevant research related to PRMs (Process Reward Models) and verifiers from 2025-2026, though the results don't specifically address all the technical terms in your query together.\n\nHere are the key findings:\n\n**Process Reward Models and Verification (2025-2026):**\n\nProcess reward models (PRMs)—also known as process verifiers—score (partial) solutions for selecting promising paths for search or ranking. Recent research shows significant advances in this area.\n\nTHINKPRM, trained on synthetic data utilizing as few as 8K step labels, surpasses LLM-as-a-judge and outperforms discriminative PRMs trained on two orders of magnitude more data across various test-time scaling scenarios.\n\n**Variable Renaming and Symbol Invariance:**\n\nYour query mentions variable renaming and notation changes. Recent work introduced a metric for measuring robustness against variable renaming and proposed a novel embedding strategy using random vectors to handle interchangeable tokens.\n\n**Step-Level Annotations:**\n\nPRMs are typically created by fine-tuning LLMs to classify the correctness of individual reasoning steps, using training datasets annotated with step-level error labels on LLM-generated reasoning traces.\n\nThe search results contain information about PRM verifiers and step-level verification from 2025-2026, though they don't specifically mention isomorphic invariance benchmarks or commutative reordering in the context of PRM verification."
    ],
    "durationSeconds": 7.3812112689999925,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e7ba6fa1-95e6-4b28-98dd-4a0da95fa153",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-20T03:18:17.697Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of the literature. Let me synthesize everything and produce my evaluation.

Key findings from my research:

1. **PRM-BiasBench** (arXiv 2603.06621, Feb 2026): This is the paper "Reward Under Attack" by Tiwari et al. It tests surface-level perturbations on PRMs and finds that 43% of reward gains are from stylistic shortcuts. It releases PRM-BiasBench. This is directly referenced in the proposal.

2. **reWordBench** (arXiv 2503.11751, EMNLP 2025): Tests meaning-preserving transformations on reward models. 

Reward models show significant degradation when exposed to minor input transformations, though this is a response-level benchmark for general RMs rather than step-level evaluation for PRMs.

3. **PutnamGAP** (arXiv 2508.08833): Tests mathematically equivalent transformations on LLM solvers, finding performance drops across 18 models.

4. **GR-Ben** (arXiv 2605.01203, May 2026): Extends PRM evaluation to non-mathematical reasoning domains, representing very recent work in this area.

5. **APRM** (arXiv 2511.22888, Nov 2025): Explores adversarial training approaches for improving PRM robustness.

6. **GenPRM** (arXiv 2504.00891, Apr 2025): Generative PRM that incorporates code verification capabilities.

7. **ThinkPRM** (Apr-May 2025): Generative PRM leveraging extended chain-of-thought reasoning.

8. **ProcessBench** (arXiv 2412.06559, Dec 2024): Provides 3,400 human-annotated solutions as foundational data.

9. **PRMBench** (arXiv 2501.03124, Jan 2025, ACL 2025): Fine-grained evaluation framework across 6,216 problems.

10. **CoLD** (arXiv 2507.15698): Addresses length bias in PRMs through counterfactual guidance.

11. **Robust Reasoning Benchmark** (arXiv 2604.08571): General robustness testing framework.

Now I'm evaluating whether this proposal actually fills a gap. The core claim is that no existing work tests whether PRMs score logically equivalent steps identically when expressed differently mathematically—sitting between surface-level perturbations like PRM-BiasBench and problem-level transformations like PutnamGAP. Looking at what's available, existing benchmarks test either surface rewording or solver-level equivalence, but nothing combines step-level granularity with structural mathematical equivalence specifically for PRM verifiers.

The proposal itself is fairly straightforward: apply isomorphic transformations to individual steps and evaluate PRMs against them, then use formal verification tools to confirm equivalence. The benchmark contribution is real but incremental—it's combining two known dimensions that haven't been tested together before. The mitigation method relies on standard data augmentation with consistency regularization, which isn't particularly novel. The more compelling aspects seem to be the cross-analysis with existing benchmarks and whatever patterns emerge from the 2D evaluation space.

I'm also thinking through the core assumptions here. The first is whether PRMs are actually vulnerable to these transformations in the first place—PutnamGAP suggests solvers are, but PRMs might already be more robust, especially the generative ones. Second, there's the question of whether step-level invariance actually translates to better performance on downstream tasks like tree search. And third, the four transformation types only cover about 35-55% of possible cases, so there's a coverage gap. The problem itself matters a lot for scaling test-time compute and preventing reward hacking, but I need to assess whether this particular approach actually moves the needle.

The core issue is that the angle here—structural isomorphism at the step level—feels somewhat narrow and predictable. Most researchers would probably expect PRMs to be at least somewhat brittle to notation changes, so the findings might not be particularly surprising. The novelty is really in combining these specific elements rather than introducing fundamentally new methodology. The mitigation approach is just standard augmentation with regularization, and the expected results are fairly obvious: discriminative PRMs will be more fragile than generative ones, augmentation will help, and brittleness will increase with depth. The notation gaming attack is interesting but builds directly on what PRM-BiasBench already found.

Wait—I'm noticing the user mentioned this is for CoRL 2026, which is the Conference on Robot Learning. But this entire proposal is about Process Reward Models for mathematical reasoning. That's a complete venue mismatch. CoRL focuses on robotics and embodied learning, not language model evaluation. This is a fundamental problem that overshadows the idea quality itself.

That said, the instructions ask me to evaluate idea quality specifically, not execution or venue fit. So let me separate these concerns: the core contribution is a solid but incremental benchmark that fills a gap in PRM evaluation for math, but it's being submitted to entirely the wrong conference. The venue mismatch alone would likely result in desk rejection, regardless of how well-executed the work is. standard data augmentation with consistency checks is the default mitigation strategy. The cross-analysis with PRM-BiasBench and the notation gaming attack surface are the most novel contributions here. But there's a critical issue: this is being evaluated for CoRL, which focuses on robot learning, not mathematical reasoning benchmarks—that's a fundamental venue mismatch that would tank acceptance regardless of idea quality. If submitted to an appropriate NLP/ML venue like EMNLP or NeurIPS, I'd estimate around 25-35% acceptance probability for a benchmark paper, but CoRL would be near zero due to the domain mismatch.

Looking at the proposal more carefully, it actually targets AAAI 2027 and ICLR 2027 as the intended venues, not CoRL 2026. So I'll evaluate the idea quality objectively for the NLP/ML community while flagging this venue mismatch as a critical issue.

For novelty, the specific combination of step-level and structural invariance with PRM evaluation is new, though the underlying approach of applying known transformation types and building benchmarks is fairly standard.  PRM-BiasBench and PutnamGAP already cover related ground, so the gap is real but narrow. Iso-Aug itself is a conventional technique.

On significance, PRM robustness matters given the test-time compute trend, but the structural isomorphism angle at the step level is quite narrow with largely predictable findings. The notation gaming attack adds some interest but builds on existing ideas.

The related work section is strong—the proposal shows excellent awareness of the landscape and clearly differentiates itself from PRM-BiasBench, reWordBench, PutnamGAP, GR-Ben, APRM, GenPRM, and ThinkPRM.

For acceptance probability, I'm estimating 20-30% at an appropriate NLP/ML venue, but only 3-8% for CoRL 2026 due to a fundamental venue mismatch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b016a37-a0da-4cb7-ab33-ec208dd98ee9",
  "isSidechain": false,
  "requestId": "req_011CbD6XeZR9kmiq69W5HMhH",
  "type": "assistant",
  "uuid": "6f4231aa-b20c-4065-8206-7094f6b45edb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRjsZhYXHhYUmXF4KofArf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 27323,
      "output_tokens": 6621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6621,
          "cache_read_input_tokens": 27323,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

### Assistant

_source line 48 · 2026-05-20T03:19:32.027Z_

Now I have enough information to make a well-grounded assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. **"Reward Under Attack" / PRM-BiasBench** (arXiv 2603.06621, Feb 2026):
   最直接竞争者。对 PRM 施加三层递进的对抗压力，发现 43% 的 RL reward gains 来自 fluency-based stylistic shortcuts。释出了 PRM-BiasBench 用于 surface-level robustness 评测。Proposal 将自身定位为"表面扰动 vs 结构等价"的正交维度——但 PRM-BiasBench 的 static perturbation analysis 已经覆盖了部分 surface invariance，且该工作发现 PRM 对 surface style changes 有高不变性 (reward change <0.1)，即 PRM 在表面层面已经相当鲁棒，这反过来削弱了"PRM 对结构等价也脆弱"的先验预期。

2. **reWordBench** (arXiv 2503.11751, EMNLP 2025):
   测试 meaning-preserving transformations 对 general reward models 的影响。发现 SOTA RMs 在 minor transformations 下性能显著下降。但作用于 response-level 且面向通用 RM，不是 step-level PRM。Proposal 正确识别了这一差异。

3. **PutnamGAP** (arXiv 2508.08833, 2025):
   对 1,051 道 Putnam 竞赛题生成 6,306 个数学等价变体，测试 LLM solver（非 verifier）的鲁棒性。O3 在 parametric variants 上下降 12.9pp。方法论上（等价变换 + 评测）与 IsoPRM-Bench 高度相似，但目标对象不同（solver vs verifier）。

4. **GR-Ben** (arXiv 2605.01203, May 2026):
   将 PRM 评测扩展到 9 个非数学推理子领域，发现 PRM 在数学之外的 error detection 能力显著更弱。极新的工作，显示 PRM 评测是活跃热点。

5. **APRM** (arXiv 2511.22888, Nov 2025):
   通过 adversarial training（Generator 生成错误、PRM 学习检测）提升 PRM 鲁棒性。OOD 任务上 +5.3pp。Proposal 将 Iso-Aug 定位为与 APRM 互补。

6. **GenPRM** (arXiv 2504.00891, Apr 2025) & **ThinkPRM** (Apr-May 2025):
   两类 generative PRM，分别用 code verification 和 long CoT reasoning 做 step-level verification。1.5B GenPRM 超过 GPT-4o，7B GenPRM 超过 Qwen2.5-Math-PRM-72B。

7. **ProcessBench** (arXiv 2412.06559, Dec 2024):
   3,400 人工标注数学解题步骤，是本 proposal 的数据基础。

8. **PRMBench** (arXiv 2501.03124, ACL 2025):
   6,216 problems, 83,456 step-level labels，评测 PRM 的 simplicity/soundness/sensitivity。已覆盖 fine-grained PRM evaluation，但角度不同（error detection 能力 vs 结构不变性）。

9. **CoLD** (arXiv 2507.15698, Jul 2025):
   Counterfactually-guided length debiasing for PRMs。Proposal 的 Iso-Aug 声称"adapt CoLD's causal debiasing framework"——但 CoLD 解决的是 length bias，不是 structural invariance。适配的合理性需要论证。

- **调研总结**: PRM 评测/鲁棒性是 2025-2026 年的热点领域，已有大量密集工作。PRM-BiasBench（surface robustness）、PRMBench（fine-grained error detection）、GR-Ben（non-math domains）从不同角度评测 PRM。PutnamGAP 对 solver 做结构等价测试。本 proposal 定位在"step-level structural invariance of PRM verifiers"这个交叉缝隙中——缝隙真实存在，但非常窄，且该领域发展极快，被近期工作侧面覆盖的风险很高。


【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁：

1. **直接用 PutnamGAP 的变换方法论 + ProcessBench 数据**: 将 PutnamGAP 的 mathematically-equivalent transformations 应用到 ProcessBench 的 step-level 数据上，然后跑现有 PRM，本质上就实现了 IsoPRM-Bench 的核心功能。Proposal 增加了 SymPy/Z3 formal verification，但这是工程层面的质量保障，不是方法论创新。

2. **PRM-BiasBench 的扩展**: PRM-BiasBench 已经测试了 surface perturbations 对 PRM 的影响，如果在其 perturbation taxonomy 中加入"structural mathematical equivalence"类别（如 variable renaming、commutative reordering），就能直接覆盖本 proposal 的核心场景。

3. **Iso-Aug 的 trivial baseline**: data augmentation + consistency regularization 是最标准的鲁棒性提升方法。在 Iso-Aug 之前，一个 reviewer 会问：为什么不直接用 isomorphic 数据做 fine-tuning（不需要 causal debiasing framework），效果会差多少？

增量价值主要在于：(a) 系统化的 transformation taxonomy + formal verification pipeline，(b) cross-analysis with PRM-BiasBench 的 2D robustness landscape，(c) 跨 paradigm 比较。但这些更接近"thorough engineering"而非"novel insight"。


【前提假设检验】:

核心逻辑链中有几个未经验证的环节：

1. **"PRM 对 structural isomorphism 脆弱"是假设而非已知事实**。PRM-BiasBench 发现 PRM 对 surface style changes 有高不变性（reward change <0.1）。如果 PRM 对 structural transformations 也是鲁棒的（尤其是 generative PRMs），整个 benchmark 的 raison d'être 就大幅削弱。Proposal 预设了 brittleness 存在并设计了 mitigation，但如果 null result 出现，论文的价值严重缩水。

2. **"Step-level 脆弱性导致 tree search failure"是未经验证的因果推断**。Proposal claim (3) 假设 brittleness 随 step depth 增加导致 tree search 失败，但这个因果链缺乏理论或实证支撑——tree search 失败的原因可能是 error propagation、branching factor 爆炸等其他因素。

3. **"Notation gaming attack surface 是实际威胁"的假设**。Proposal claim (5) 假设 policy 可以通过利用 PRM notation preferences 来 inflate scores。但如果 PRM 对 notation 变化本身就鲁棒（如 PRM-BiasBench 的发现所暗示），这个 attack surface 就不存在。

4. **CoLD framework 适配到 structural invariance 的合理性**。CoLD 针对 length bias 设计，其 causal graph 和 intervention 策略是否能直接迁移到 structural invariance 问题上，逻辑上并不自明。


【3 维度打分】:

1. **Novelty: 弱-中** — 核心贡献是在已有工作的缝隙中找到了一个未被显式测试的组合：step-level × structural invariance × PRM verifier。但方法论上没有新东西——transformation types（variable renaming, commutative reordering, representation change, notation change）都是 PutnamGAP 和 reWordBench 中已有的；formal verification pipeline（SymPy, Z3）是标准工具；Iso-Aug 是 augmentation + consistency regularization 的标准做法。PRM-BiasBench (2603.06621) 已经在 PRM 上测试了 perturbation robustness，只需扩展其 perturbation taxonomy 就能覆盖大部分场景。PutnamGAP 的方法论直接迁移到 step-level 就是本 proposal 的核心。Novelty 主要来自"nobody has explicitly done this exact combination"，这是 gap-filling 而非 insight-driven。

2. **Significance: 中** — PRM robustness 是一个重要且活跃的研究方向（PRM-BiasBench, APRM, CoLD 等都在 2025-2026 密集发表）。Test-time compute scaling 依赖可靠的 verifier 是真实需求。但：(a) 具体到 structural isomorphism 这个角度，影响面较窄——实际部署中，同一个推理步骤以不同数学记号出现的场景有限；(b) 预期发现的 surprise value 低——"discriminative PRM 比 generative PRM 更脆弱"几乎是 trivially expected（generative PRM 本身就做 explicit reasoning）；(c) 如果核心发现是 positive（PRM 确实脆弱），reviewer 大概率会说"I would have guessed this given PutnamGAP's findings on solvers"。

3. **Related Work: 强** — Proposal 展示了对领域的优秀理解和定位。清晰区分了 PRM-BiasBench（surface）、reWordBench（response-level general RM）、PutnamGAP（solver not verifier）、GR-Ben（non-math domains）、APRM（adversarial training）、GenPRM/ThinkPRM（generative paradigm）。定位准确，差异化清晰。这是这份 proposal 最强的维度。

【概率估计】: [15% - 28%] 中位 20%

【估计理由】:
- Novelty 是主要限制因素：核心贡献是 gap-filling benchmark，方法论层面没有新东西。在 PRM 评测已极度拥挤的 2025-2026 landscape 中（PRM-BiasBench, PRMBench, GR-Ben, ToolPRMBench 等），一个新 benchmark 需要展示"不可被现有 benchmark 简单扩展覆盖"的独特价值，而本 proposal 的核心场景可以被 PRM-BiasBench 扩展 taxonomy 或 PutnamGAP 方法下移到 step-level 来覆盖。
- Significance 受限于 surprise value：核心预期发现（PRM 对结构等价脆弱）是可预测的，不太可能让 reviewer 感到 "surprising"。
- **关键额外风险——venue mismatch**: Proposal 自述目标是 AAAI 2027 和 ICLR 2027，但用户询问的是 CoRL 2026（Conference on Robot Learning）。本 proposal 是纯粹的 NLP/mathematical reasoning PRM 评测工作，与 robot learning 完全无关。如果真的投 CoRL，大概率 desk reject。上述 15-28% 的估计是基于投到合适的 NLP/ML venue（如 AAAI/ICLR/ACL）的假设。如果投 CoRL 2026，概率应为 **3-5%**（基本只有误分配 reviewer 的极小概率）。

【主要风险】:
1. **Null result 风险**: 如果 PRM（尤其是 generative PRM）对 structural isomorphism 已经足够鲁棒，整个 benchmark 的核心 motivation 被瓦解，论文沦为"we tested and nothing interesting happened"。PRM-BiasBench 的发现（PRM 对 surface changes 高度不变）暗示这一风险非零。
2. **增量价值不足**: 在 PRM benchmark 极度拥挤的领域中，reviewer 可能认为"将 PutnamGAP 的方法下沉到 step-level + 跑几个 PRM"不构成充分的学术贡献——这是一个 well-executed engineering effort，但 insight 有限。
```

Sources:
- [Reward Under Attack / PRM-BiasBench (arXiv 2603.06621)](https://arxiv.org/abs/2603.06621)
- [reWordBench (arXiv 2503.11751)](https://arxiv.org/abs/2503.11751)
- [PutnamGAP (arXiv 2508.08833)](https://arxiv.org/abs/2508.08833)
- [GR-Ben (arXiv 2605.01203)](https://arxiv.org/abs/2605.01203)
- [APRM (arXiv 2511.22888)](https://arxiv.org/abs/2511.22888)
- [GenPRM (arXiv 2504.00891)](https://arxiv.org/abs/2504.00891)
- [ProcessBench (arXiv 2412.06559)](https://arxiv.org/abs/2412.06559)
- [PRMBench (arXiv 2501.03124)](https://arxiv.org/abs/2501.03124)
- [CoLD (arXiv 2507.15698)](https://arxiv.org/abs/2507.15698)
- [ThinkPRM (MarkTechPost)](https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f4231aa-b20c-4065-8206-7094f6b45edb",
  "isSidechain": false,
  "requestId": "req_011CbD6XeZR9kmiq69W5HMhH",
  "type": "assistant",
  "uuid": "b6643bd5-beff-403b-9c18-acee7e1680dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRjsZhYXHhYUmXF4KofArf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 27323,
      "output_tokens": 6621,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6621,
          "cache_read_input_tokens": 27323,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

### Runtime record

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # IsoPRM-Bench: Benchmarking and Mitigating Structural Isomorphism Brittleness in Process Reward Models  ## Descri…",
  "leafUuid": "b6643bd5-beff-403b-9c18-acee7e1680dc",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate acceptance probability for IsoPRM-Bench proposal",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # IsoPRM-Bench: Benchmarking and Mitigating Structural Isomorphism Brittleness in Process Reward Models  ## Descri…",
  "leafUuid": "b6643bd5-beff-403b-9c18-acee7e1680dc",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate acceptance probability for IsoPRM-Bench proposal",
  "sessionId": "b92b42d7-02d4-46cb-973f-5b2c9d6023fd"
}
```

---
