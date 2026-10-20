# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-28 (UTC).** ## Y

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/a88bc0c5-6738-4cbd-8064-aa4dfb9f0568.jsonl`
- **Structured JSON:** [`a1896a44e30590773c45.json`](../../sessions/a1/a1896a44e30590773c45.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T11:27:23.066Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T11:27:23.066Z",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2026\nTrack: Machine Learning (ML) — Efficient Inference and Reasoning\n\nDirection: Per-instance adaptive co-optimization of generation and verification compute, where both the number of generated solutions (K) and the verification depth (none/ORM/PRM/GenRM) are jointly selected based on online difficulty estimation from early reasoning tokens. Extends static aggregate scaling laws (Singhi et al.) to instance-adaptive, multi-depth allocation with a practical online algorithm.\n\nSeed Papers:\n- Singhi et al., \"When To Solve, When To Verify\" (arXiv 2025) — establishes aggregate scaling laws for generation-verification tradeoff; our work must explicitly extend this to per-instance, multi-depth allocation\n- Setlur et al., \"Scaling TTC Without Verification is Suboptimal\" (arXiv Feb 2025) — proves verification is essential and the gap grows with compute; motivates why verification budget allocation matters\n- Chen et al., \"VG-Search: Rethinking Optimal Verification Granularity\" (arXiv May 2025) — shows verification granularity matters for efficiency; we extend from granularity to depth and per-instance adaptation\n- Wang et al., \"ST-BoN\" (NeurIPS 2025 Spotlight) — early pruning via sampling consistency; a strong baseline for lightweight verification allocation\n\nKnown Gaps:\n- No method selects verification depth (none/ORM/PRM/GenRM) per-instance based on estimated difficulty; all existing work uses a fixed verification strategy across problems\n- Singhi et al.'s scaling laws are static and aggregate (one ratio for all problems); no online algorithm adapts the generation-verification split per-instance during inference\n- No framework jointly optimizes K (number of solutions) and d (verification depth) as coupled decision variables under a shared compute budget\n\nTheoretical Anchor: The bilinear structure of the joint optimization — P(correct) depends on coverage (increasing in K) and selection precision (increasing in d), while cost is c_g*K + c_v(d)*K = K*(c_g + c_v(d)) — admits a clean decomposition: for fixed d, optimal K = B/(c_g + c_v(d)), reducing the problem to selecting d* that maximizes selection precision per unit verification cost. This decomposition enables tractable optimization with provable approximation guarantees under mild assumptions on verifier accuracy monotonicity.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must evaluate on ≥4 benchmarks across ≥2 domains (math, code, science)\n- Must compare against Singhi et al.'s aggregate-optimal baseline and fixed-depth baselines\n\nQuality Self-Checks:\n- [x] Core insight: The optimal verification depth varies dramatically per problem — easy problems need no verification while hard problems benefit from expensive generative verification — and this variance is predictable from early tokens.\n- [x] Why not obvious: Singhi et al. showed the aggregate optimal ratio, but the per-instance variance and multi-depth selection weren't explored because their framework only compared two verification strategies (GenRM vs SC), not a continuum of depths.\n- [ ] Baseline fear test: A simple heuristic (e.g., always use PRM for problems longer than X tokens) could capture much of the benefit — must demonstrate learned allocation significantly outperforms simple rules. This is a REAL RISK.\n- [x] Information exploited: Early-token difficulty signals (entropy trajectory, hesitation markers from Zhou et al.) that are available before verification decisions must be made.\n\nAvoid:\n- Framing as 'first to study generation-verification tradeoff' — Singhi et al. already did this; frame as extending to per-instance multi-depth allocation\n- Math-only evaluation — must include code and science benchmarks\n- Pure scaling law contribution — must provide a practical online algorithm, not just power-law fits\n- Ignoring the baseline fear: if a simple threshold on problem length achieves 80% of the adaptive allocation's gain, the paper is dead**\n\n## Paper to analyze\n\n{\n  \"title\": \"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling\",\n  \"authors\": \"Liu et al.\",\n  \"venue\": \"arXiv 2025\",\n  \"url\": \"https://arxiv.org/abs/2502.06703\",\n  \"why_important\": \"Systematic analysis showing compute-optimal TTS depends on policy model × PRM × difficulty interaction — directly supports your thesis that uniform allocation is suboptimal\",\n  \"one_line_summary\": \"Demonstrates that compute-optimal test-time scaling is highly dependent on the interaction of policy model, PRM quality, and problem difficulty, with a 1B model surpassing 405B under optimal allocation.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T11:27:23.069Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T11:27:23.069Z",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-28T11:27:23.081Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-28 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Target: AAAI 2026
Track: Machine Learning (ML) — Efficient Inference and Reasoning

Direction: Per-instance adaptive co-optimization of generation and verification compute, where both the number of generated solutions (K) and the verification depth (none/ORM/PRM/GenRM) are jointly selected based on online difficulty estimation from early reasoning tokens. Extends static aggregate scaling laws (Singhi et al.) to instance-adaptive, multi-depth allocation with a practical online algorithm.

Seed Papers:
- Singhi et al., "When To Solve, When To Verify" (arXiv 2025) — establishes aggregate scaling laws for generation-verification tradeoff; our work must explicitly extend this to per-instance, multi-depth allocation
- Setlur et al., "Scaling TTC Without Verification is Suboptimal" (arXiv Feb 2025) — proves verification is essential and the gap grows with compute; motivates why verification budget allocation matters
- Chen et al., "VG-Search: Rethinking Optimal Verification Granularity" (arXiv May 2025) — shows verification granularity matters for efficiency; we extend from granularity to depth and per-instance adaptation
- Wang et al., "ST-BoN" (NeurIPS 2025 Spotlight) — early pruning via sampling consistency; a strong baseline for lightweight verification allocation

Known Gaps:
- No method selects verification depth (none/ORM/PRM/GenRM) per-instance based on estimated difficulty; all existing work uses a fixed verification strategy across problems
- Singhi et al.'s scaling laws are static and aggregate (one ratio for all problems); no online algorithm adapts the generation-verification split per-instance during inference
- No framework jointly optimizes K (number of solutions) and d (verification depth) as coupled decision variables under a shared compute budget

Theoretical Anchor: The bilinear structure of the joint optimization — P(correct) depends on coverage (increasing in K) and selection precision (increasing in d), while cost is c_g*K + c_v(d)*K = K*(c_g + c_v(d)) — admits a clean decomposition: for fixed d, optimal K = B/(c_g + c_v(d)), reducing the problem to selecting d* that maximizes selection precision per unit verification cost. This decomposition enables tractable optimization with provable approximation guarantees under mild assumptions on verifier accuracy monotonicity.

Constraints:
- Compute: ≤200 H100-hours
- Must evaluate on ≥4 benchmarks across ≥2 domains (math, code, science)
- Must compare against Singhi et al.'s aggregate-optimal baseline and fixed-depth baselines

Quality Self-Checks:
- [x] Core insight: The optimal verification depth varies dramatically per problem — easy problems need no verification while hard problems benefit from expensive generative verification — and this variance is predictable from early tokens.
- [x] Why not obvious: Singhi et al. showed the aggregate optimal ratio, but the per-instance variance and multi-depth selection weren't explored because their framework only compared two verification strategies (GenRM vs SC), not a continuum of depths.
- [ ] Baseline fear test: A simple heuristic (e.g., always use PRM for problems longer than X tokens) could capture much of the benefit — must demonstrate learned allocation significantly outperforms simple rules. This is a REAL RISK.
- [x] Information exploited: Early-token difficulty signals (entropy trajectory, hesitation markers from Zhou et al.) that are available before verification decisions must be made.

Avoid:
- Framing as 'first to study generation-verification tradeoff' — Singhi et al. already did this; frame as extending to per-instance multi-depth allocation
- Math-only evaluation — must include code and science benchmarks
- Pure scaling law contribution — must provide a practical online algorithm, not just power-law fits
- Ignoring the baseline fear: if a simple threshold on problem length achieves 80% of the adaptive allocation's gain, the paper is dead**

## Paper to analyze

{
  "title": "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling",
  "authors": "Liu et al.",
  "venue": "arXiv 2025",
  "url": "https://arxiv.org/abs/2502.06703",
  "why_important": "Systematic analysis showing compute-optimal TTS depends on policy model × PRM × difficulty interaction — directly supports your thesis that uniform allocation is suboptimal",
  "one_line_summary": "Demonstrates that compute-optimal test-time scaling is highly dependent on the interaction of policy model, PRM quality, and problem difficulty, with a 1B model surpassing 405B under optimal allocation."
}

## Instructions

1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.

2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:
   - What gap did they identify and HOW did they find it?
   - What was the key insight that others missed?
   - How did they formulate the problem differently from prior work?
   - What existing technique did they adapt/combine/simplify?

3. **Learn from reviewers**: If you can find reviewer comments, extract:
   - What did reviewers praise most?
   - What concerns were raised and how were they addressed?
   - What would have made this paper even stronger?

## Output format

Output a single JSON object:
{
  "title": "Paper title",
  "venue": "Where published",
  "problem_identification": "What gap/problem did they identify? How did they find it? (2-3 sentences)",
  "key_insight": "The core intellectual contribution — the aha moment (1-2 sentences)",
  "innovation_type": "new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis",
  "method_summary": "Technical approach in 3-5 sentences — enough to understand the machinery",
  "what_makes_it_good": "Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)",
  "limitations_acknowledged": "What gaps did the authors themselves identify? (1-2 sentences)",
  "open_questions": "What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)",
  "building_blocks": ["List of methods/tools/datasets used that could be reused"],
  "reviewer_feedback_summary": "If found on OpenReview: key praise and concerns. Otherwise: null",
  "relevance_to_seed": "How does this paper relate to our research area? What can we learn from it? (1-2 sentences)"
}

Be analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "69ca1a40-1583-48e0-b778-6a85a0d2e8bd",
  "type": "user",
  "uuid": "c32dcd37-ebac-4b68-b886-ec43202d4cca",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T11:27:23.080Z_

```json
{
  "parentUuid": "c32dcd37-ebac-4b68-b886-ec43202d4cca",
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
  "uuid": "01c822bf-7e4d-4625-aff9-c0d2694f5cf7",
  "timestamp": "2026-05-28T11:27:23.080Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T11:27:23.080Z_

```json
{
  "parentUuid": "01c822bf-7e4d-4625-aff9-c0d2694f5cf7",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "f63b2ffc-49df-4491-b484-e52a176421ea",
  "timestamp": "2026-05-28T11:27:23.080Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-28T11:27:23.080Z_

```json
{
  "parentUuid": "f63b2ffc-49df-4491-b484-e52a176421ea",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "26b8f463-d80a-40f0-ae25-05b64faceeda",
  "timestamp": "2026-05-28T11:27:23.080Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Liu et al. compute-optimal test-time scaling paper",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568"
}
```

---

### Assistant

_source line 8 · 2026-05-28T11:27:26.803Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to deeply analyze a paper "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling" by Liu et al. (arXiv 2025, arxiv.org/abs/2502.06703). I need to fetch the paper content and analyze it thoroughly.

Let me start by fetching the paper from arXiv.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26b8f463-d80a-40f0-ae25-05b64faceeda",
  "isSidechain": false,
  "requestId": "req_011CbUtNyMBBq1dDdpdMqB8r",
  "type": "assistant",
  "uuid": "0891a092-98f1-4954-8963-cfb074e848a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yUWf3ogfuL3vyabKNoffA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3513,
      "cache_read_input_tokens": 10620,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 186,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 3513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3513
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

_source line 9 · 2026-05-28T11:27:27.170Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GHJeBPqNexRtygiTxUfJQv`</summary>

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
  "parentUuid": "0891a092-98f1-4954-8963-cfb074e848a1",
  "isSidechain": false,
  "requestId": "req_011CbUtNyMBBq1dDdpdMqB8r",
  "type": "assistant",
  "uuid": "d5eab6f0-411f-4c4e-a715-d5ce3e05ec44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yUWf3ogfuL3vyabKNoffA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3513,
      "cache_read_input_tokens": 10620,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 186,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 3513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3513
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

_source line 10 · 2026-05-28T11:27:27.178Z_

<details><summary>↩ Tool result · `toolu_01GHJeBPqNexRtygiTxUfJQv`</summary>

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
  "parentUuid": "d5eab6f0-411f-4c4e-a715-d5ce3e05ec44",
  "isSidechain": false,
  "promptId": "69ca1a40-1583-48e0-b778-6a85a0d2e8bd",
  "type": "user",
  "uuid": "a0f071a2-4d3b-4a26-bcab-e00bc36ff154",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "d5eab6f0-411f-4c4e-a715-d5ce3e05ec44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-28T11:27:31.150Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll make multiple requests to get different parts of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0f071a2-4d3b-4a26-bcab-e00bc36ff154",
  "isSidechain": false,
  "requestId": "req_011CbUtPGdjqkNDucsftw3jk",
  "type": "assistant",
  "uuid": "3450927a-d720-4bb4-85f7-39c5bc82bcf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFj7nQRk6Mx3L8EfchsFUw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 14133,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 14133,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 706
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

_source line 12 · 2026-05-28T11:27:31.742Z_

Let me fetch the paper from multiple sources to get comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3450927a-d720-4bb4-85f7-39c5bc82bcf2",
  "isSidechain": false,
  "requestId": "req_011CbUtPGdjqkNDucsftw3jk",
  "type": "assistant",
  "uuid": "a024a7f8-6fc1-46c6-ae64-db5efcf00f05",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFj7nQRk6Mx3L8EfchsFUw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 14133,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 14133,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 706
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

_source line 13 · 2026-05-28T11:27:33.195Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WNFXShApxDoXvLEa1xvwDx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06703",
  "prompt": "Extract the full abstract, author list, and any other metadata (submission date, categories) from this arXiv paper page. Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a024a7f8-6fc1-46c6-ae64-db5efcf00f05",
  "isSidechain": false,
  "requestId": "req_011CbUtPGdjqkNDucsftw3jk",
  "type": "assistant",
  "uuid": "b3d52e28-2fb4-4b60-b10b-ef380fc0de7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFj7nQRk6Mx3L8EfchsFUw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 14133,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 14133,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 706
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

_source line 14 · 2026-05-28T11:27:36.603Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FDo4p5rpB4fLA7989f19Vg`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.06703",
  "prompt": "Extract the FULL text of the following sections from this paper, preserving all detail, equations, and references:\n1. Introduction (complete)\n2. Method / Approach / Framework section (complete - whatever the main technical contribution section is called)\n3. Key findings, results, and analysis sections\n\nInclude all mathematical formulations, algorithm descriptions, and key experimental details. Do NOT summarize - return the full text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3d52e28-2fb4-4b60-b10b-ef380fc0de7d",
  "isSidechain": false,
  "requestId": "req_011CbUtPGdjqkNDucsftw3jk",
  "type": "assistant",
  "uuid": "5f8ba4af-afaf-490f-84cb-81642bad658d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFj7nQRk6Mx3L8EfchsFUw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 14133,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 706,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 14133,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 706
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

_source line 15 · 2026-05-28T11:27:37.736Z_

<details><summary>↩ Tool result · `toolu_01WNFXShApxDoXvLEa1xvwDx`</summary>

```text
# Paper Metadata Extraction

**Title:** "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"

**Authors:** Runze Liu, Junqi Gao, Jian Zhao, Kaiyan Zhang, Xiu Li, Biqing Qi, Wanli Ouyang, Bowen Zhou

**Submission Date:** February 10, 2025

**arXiv Identifier:** 2502.06703

**Category:** Computer Science - Computation and Language (cs.CL)

**Abstract Summary:**
The paper investigates test-time scaling for LLMs, examining how policy models, Process Reward Models, and problem difficulty affect performance. Key findings indicate that "a 1B LLM can exceed a 405B LLM on MATH-500" and "a 0.5B LLM outperforms GPT-4o." The research demonstrates that smaller models with optimized compute-scaling strategies can match or surpass substantially larger models on reasoning tasks, suggesting compute-optimal test-time scaling offers promising efficiency gains for enhancing LLM reasoning capabilities.

**DOI:** https://doi.org/10.48550/arXiv.2502.06703
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3d52e28-2fb4-4b60-b10b-ef380fc0de7d",
  "isSidechain": false,
  "promptId": "69ca1a40-1583-48e0-b778-6a85a0d2e8bd",
  "type": "user",
  "uuid": "0d7780b5-1a87-418d-9ab9-a965d83a22ac",
  "toolUseResult": {
    "bytes": 47351,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Metadata Extraction\n\n**Title:** \"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling\"\n\n**Authors:** Runze Liu, Junqi Gao, Jian Zhao, Kaiyan Zhang, Xiu Li, Biqing Qi, Wanli Ouyang, Bowen Zhou\n\n**Submission Date:** February 10, 2025\n\n**arXiv Identifier:** 2502.06703\n\n**Category:** Computer Science - Computation and Language (cs.CL)\n\n**Abstract Summary:**\nThe paper investigates test-time scaling for LLMs, examining how policy models, Process Reward Models, and problem difficulty affect performance. Key findings indicate that \"a 1B LLM can exceed a 405B LLM on MATH-500\" and \"a 0.5B LLM outperforms GPT-4o.\" The research demonstrates that smaller models with optimized compute-scaling strategies can match or surpass substantially larger models on reasoning tasks, suggesting compute-optimal test-time scaling offers promising efficiency gains for enhancing LLM reasoning capabilities.\n\n**DOI:** https://doi.org/10.48550/arXiv.2502.06703",
    "durationMs": 4537,
    "url": "https://arxiv.org/abs/2502.06703"
  },
  "sourceToolAssistantUUID": "b3d52e28-2fb4-4b60-b10b-ef380fc0de7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
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
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "0d7780b5-1a87-418d-9ab9-a965d83a22ac",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Liu et al. compute-optimal test-time scaling paper",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568"
}
```

---

### Tool result

_source line 18 · 2026-05-28T11:28:08.114Z_

<details><summary>↩ Tool result · `toolu_01FDo4p5rpB4fLA7989f19Vg`</summary>

```text
# Full Text Extraction: Key Sections

## 1. Introduction (Complete)

Large Language Models (LLMs) have shown significant improvements across a variety of domains (OpenAI, 2023; Hurst et al., 2024; Anthropic, 2023; OpenAI, 2024; DeepSeek-AI et al., 2025). Recently, OpenAI o1 has demonstrated that "Test-Time Scaling (TTS) can enhance the reasoning capabilities of LLMs by allocating additional computation at inference time" (OpenAI, 2024).

TTS approaches divide into two main categories: (1) Internal TTS, which trains LLMs to "think" slowly with long Chain-of-Thought (CoT), and (2) External TTS, which improves reasoning performance via sampling or search-based methods with fixed LLMs. The key challenge of external TTS involves scaling compute optimally—allocating optimal computation for each problem.

Current TTS methods guide generation and select final answers using Process Reward Models (PRMs). However, existing studies lack systematic analysis of how policy models, PRMs, and problem difficulty influence TTS strategies. This limitation prevents full understanding and development of insights for compute-optimal TTS.

The paper investigates two core questions: (1) What is the optimal approach to scale test-time computation across different policy models, PRMs, and problem difficulty levels? (2) To what extent can extended computation improve LLM performance on complex tasks, and can smaller language models outperform larger ones?

Through comprehensive experiments on MATH-500 and AIME24 tasks, the authors observe: (1) "The compute-optimal TTS strategy is highly dependent on the choice of policy model, PRM, and problem difficulty" (Liu et al., 2025). (2) Even smaller models can outperform larger models and state-of-the-art reasoning models through compute-optimal TTS.

**Key Contributions:**
- Comprehensive evaluation of different TTS methods using up-to-date policy models, multiple PRMs, diverse scaling methods, and challenging tasks
- Analysis highlighting necessity of considering reward influence in TTS, introducing reward-aware compute-optimal TTS
- Empirical results demonstrating smaller language models outperforming larger models through TTS

---

## 2. Method / Approach / Framework Section

### 2.1 Problem Formulation

The reasoning problem is formulated as a Markov Decision Process (MDP) defined by the tuple (𝒮,𝒜,𝒫,ℛ,γ), where:
- 𝒮 is the state space
- 𝒜 is the action space
- 𝒫:𝒮×𝒜→𝒮 is the transition function
- ℛ:𝒮×𝒜→ℝ is the reward function
- γ∈[0,1] is the discount factor

Given a prompt x∼𝒳, the policy with parameters θ generates initial action a₁∼πθ(⋅∣s₁), where s₁=x is the initial state. The process follows:

**Initial State:** s₁=x∼𝒳
**Action:** aₜ∼πθ(⋅∣sₜ)
**State Transition:** sₜ₊₁=𝒫(⋅∣sₜ,aₜ)=[sₜ,aₜ]
**Reward:** rₜ=ℛ(sₜ,aₜ)

A trajectory of length H is represented as τ={a₁,a₂,⋯,aₕ}. The process continues until episode termination via reaching maximum steps or generating EOS token.

### 2.2 Test-Time Scaling Methods

Three TTS methods are evaluated:

**Best-of-N (BoN):** The policy model generates N responses, after which scoring and voting methods select the final answer.

**Beam Search:** Given beam width N and beam size M, the policy model generates N steps. The verifier selects top N/M steps for subsequent search. In the next step, the policy samples M steps for each selected previous step. Process repeats until maximum depth or EOS token generation.

**Diverse Verifier Tree Search (DVTS):** Extends beam search by dividing the search process into N/M subtrees, each explored independently using beam search. DVTS increases diversity and proves more effective on easy and medium problems with large computational budgets.

### 2.3 Compute-Optimal Test-Time Scaling

The original compute-optimal scaling strategy aims to maximize performance for given test-time strategy. Given prompt x, let Target(θ,N,x) represent the output distribution over x produced by policy model with parameters θ and compute budget N:

θ*ₓ,ᵧ*(ₓ)(N) = arg max_θ (𝔼ᵧ∼Target(θ,N,x)[𝟙ᵧ=ᵧ*(ₓ)])

where y*(x) denotes ground-truth correct response for x.

### 3.1 Reward-Aware Compute-Optimal Scaling Strategy

The paper proposes that rewards should integrate into compute-optimal TTS strategy. The reward-aware compute-optimal TTS formulation:

θ*ₓ,ᵧ*(ₓ),ℛ(N) = arg max_θ (𝔼ᵧ∼Target(θ,N,x,ℛ)[𝟙ᵧ=ᵧ*(ₓ)])

where Target(θ,N,x,ℛ) represents the output distribution of policy model θ, adjusted by reward function ℛ, under compute budget N and prompt x. "For sampling-based scaling methods, Target(θ,N,x,ℛ)=Target(θ,N,x)" (Liu et al., 2025).

This reward-aware strategy ensures "compute-optimal scaling adapts to the policy model, prompt, and reward function" (Liu et al., 2025).

### 3.2 Absolute Problem Difficulty Criterion

Rather than using difficulty levels from MATH or oracle labels based on Pass@1 accuracy quantiles, the paper proposes absolute thresholds based on Pass@1 accuracy:
- Easy: 50%-100%
- Medium: 10%-50%
- Hard: 0%-10%

---

## 3. Key Findings, Results, and Analysis

### 4.2 How TTS Improves with Different Policy Models and PRMs (Q1)

**Key Finding:** "PRMs are hard to generalize across policy models and tasks" (Liu et al., 2025). Results show performance varies significantly depending on policy-PRM combinations. For Llama-3.1-8B-Instruct, search-based methods with Skywork and Qwen2.5-Math PRMs improve substantially with larger compute budgets, while Math-Shepherd and RLHFlow PRMs remain relatively poor.

**Additional Observation:** "The optimal TTS method depends on the PRM used" (Liu et al., 2025). BoN outperforms other strategies most often when using Math-Shepherd and RLHFlow PRMs, while search-based methods perform better with Skywork and Qwen2.5-Math PRMs.

**Relationship Finding:** TTS performance positively correlates with process supervision abilities of different PRMs, with fitted function: Y = 7.66 log(X) + 44.31

**Scaling with Model Size:** For small policy models, "search-based methods outperform BoN, while for large policy models, BoN is more effective" (Liu et al., 2025). This occurs because larger models have stronger reasoning capabilities and don't require step-by-step verification.

### 4.3 TTS Improvement Across Problem Difficulty Levels (Q2)

**Finding:** "The optimal TTS methods vary with different difficulty levels" (Liu et al., 2025). For small policy models (fewer than 7B parameters), BoN works better for easy problems while beam search performs better for harder problems. For models between 7B-32B parameters, DVTS performs well for easy and medium problems, with beam search preferable for hard problems. For 72B parameter models, BoN remains best for all difficulty levels.

### 4.4 PRM Characteristics Analysis (Q3)

**Length Bias:** Analysis of training data reveals that different PRMs exhibit bias toward specific response lengths. For example, "the number of inference tokens of scaling with RLHFlow-PRM-Deepseek-8B is consistently larger than that of RLHFlow-PRM-Mistral-8B, nearly 2×" (Liu et al., 2025).

**Voting Method Sensitivity:** Different PRMs show varying sensitivity to voting methods. Skywork-PRM-7B works better with PRM-Vote than PRM-Max, while Qwen2.5-Math-PRM-7B shows low sensitivity to voting methods.

### 5.1 Can Smaller Models Outperform Larger Models? (Q4)

**Major Finding:** A 1B LLM can exceed a 405B LLM on MATH-500, representing "487.0% improvement" compared to previous work. Specific results include:

- Llama-3.2-3B-Instruct with compute-optimal TTS: 78.2% on MATH-500, 65.0% on AIME24
- Llama-3.1-405B-Instruct (CoT): 71.4% on MATH-500, 23.3% on AIME24

Additional achievements:
- "Qwen2.5-0.5B-Instruct and Llama-3.2-3B-Instruct with the compute-optimal TTS strategy outperforms GPT-4o" (Liu et al., 2025)
- DeepSeek-R1-Distill-Qwen-1.5B outperforms o1-preview and o1-mini on both MATH-500 and AIME24
- DeepSeek-R1-Distill-Qwen-7B outperforms o1 and DeepSeek-R1 on both datasets

**FLOPS Efficiency:** Small policy models "surpass large ones with less inference FLOPS and reduce the total FLOPS by 100×∼1000×" (Liu et al., 2025).

### 5.2 Compute-Optimal TTS vs. CoT and Majority Voting (Q5)

Key comparative results show:
- Llama-3.2-1B-Instruct: 154.6% performance gain, >256× efficiency gain
- Llama-3.2-3B-Instruct: 88.9% performance gain, 14.1× efficiency gain
- Qwen2.5-7B-Instruct: 18.5% performance gain, 35.9× efficiency gain

"As the number of parameters in the policy model increases, the improvement of TTS gradually decreases" (Liu et al., 2025), suggesting TTS effectiveness directly relates to policy model reasoning ability.

### 5.3 TTS vs. Long-CoT-Based Methods (Q6)

Comparative evaluation with rStar-Math, Eurus-2, SimpleRL, Satori, and DeepSeek-R1-Distill-Qwen-7B shows:
- TTS with Qwen2.5-7B outperforms rStar-Math (78.4% → 88.0% on MATH-500), Eurus-2, SimpleRL, and Satori
- Performance drops significantly on AIME24 compared to DeepSeek-R1-Distill-Qwen-7B
- Conclusion: "TTS is more effective than methods applying direct RL or SFT on data generated via MCTS but less effective than distilling from strong reasoning models" (Liu et al., 2025)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f8ba4af-afaf-490f-84cb-81642bad658d",
  "isSidechain": false,
  "promptId": "69ca1a40-1583-48e0-b778-6a85a0d2e8bd",
  "type": "user",
  "uuid": "47d4e70a-9c34-4524-8700-db9323b566d9",
  "toolUseResult": {
    "bytes": 353517,
    "code": 200,
    "codeText": "OK",
    "result": "# Full Text Extraction: Key Sections\n\n## 1. Introduction (Complete)\n\nLarge Language Models (LLMs) have shown significant improvements across a variety of domains (OpenAI, 2023; Hurst et al., 2024; Anthropic, 2023; OpenAI, 2024; DeepSeek-AI et al., 2025). Recently, OpenAI o1 has demonstrated that \"Test-Time Scaling (TTS) can enhance the reasoning capabilities of LLMs by allocating additional computation at inference time\" (OpenAI, 2024).\n\nTTS approaches divide into two main categories: (1) Internal TTS, which trains LLMs to \"think\" slowly with long Chain-of-Thought (CoT), and (2) External TTS, which improves reasoning performance via sampling or search-based methods with fixed LLMs. The key challenge of external TTS involves scaling compute optimally—allocating optimal computation for each problem.\n\nCurrent TTS methods guide generation and select final answers using Process Reward Models (PRMs). However, existing studies lack systematic analysis of how policy models, PRMs, and problem difficulty influence TTS strategies. This limitation prevents full understanding and development of insights for compute-optimal TTS.\n\nThe paper investigates two core questions: (1) What is the optimal approach to scale test-time computation across different policy models, PRMs, and problem difficulty levels? (2) To what extent can extended computation improve LLM performance on complex tasks, and can smaller language models outperform larger ones?\n\nThrough comprehensive experiments on MATH-500 and AIME24 tasks, the authors observe: (1) \"The compute-optimal TTS strategy is highly dependent on the choice of policy model, PRM, and problem difficulty\" (Liu et al., 2025). (2) Even smaller models can outperform larger models and state-of-the-art reasoning models through compute-optimal TTS.\n\n**Key Contributions:**\n- Comprehensive evaluation of different TTS methods using up-to-date policy models, multiple PRMs, diverse scaling methods, and challenging tasks\n- Analysis highlighting necessity of considering reward influence in TTS, introducing reward-aware compute-optimal TTS\n- Empirical results demonstrating smaller language models outperforming larger models through TTS\n\n---\n\n## 2. Method / Approach / Framework Section\n\n### 2.1 Problem Formulation\n\nThe reasoning problem is formulated as a Markov Decision Process (MDP) defined by the tuple (𝒮,𝒜,𝒫,ℛ,γ), where:\n- 𝒮 is the state space\n- 𝒜 is the action space\n- 𝒫:𝒮×𝒜→𝒮 is the transition function\n- ℛ:𝒮×𝒜→ℝ is the reward function\n- γ∈[0,1] is the discount factor\n\nGiven a prompt x∼𝒳, the policy with parameters θ generates initial action a₁∼πθ(⋅∣s₁), where s₁=x is the initial state. The process follows:\n\n**Initial State:** s₁=x∼𝒳\n**Action:** aₜ∼πθ(⋅∣sₜ)\n**State Transition:** sₜ₊₁=𝒫(⋅∣sₜ,aₜ)=[sₜ,aₜ]\n**Reward:** rₜ=ℛ(sₜ,aₜ)\n\nA trajectory of length H is represented as τ={a₁,a₂,⋯,aₕ}. The process continues until episode termination via reaching maximum steps or generating EOS token.\n\n### 2.2 Test-Time Scaling Methods\n\nThree TTS methods are evaluated:\n\n**Best-of-N (BoN):** The policy model generates N responses, after which scoring and voting methods select the final answer.\n\n**Beam Search:** Given beam width N and beam size M, the policy model generates N steps. The verifier selects top N/M steps for subsequent search. In the next step, the policy samples M steps for each selected previous step. Process repeats until maximum depth or EOS token generation.\n\n**Diverse Verifier Tree Search (DVTS):** Extends beam search by dividing the search process into N/M subtrees, each explored independently using beam search. DVTS increases diversity and proves more effective on easy and medium problems with large computational budgets.\n\n### 2.3 Compute-Optimal Test-Time Scaling\n\nThe original compute-optimal scaling strategy aims to maximize performance for given test-time strategy. Given prompt x, let Target(θ,N,x) represent the output distribution over x produced by policy model with parameters θ and compute budget N:\n\nθ*ₓ,ᵧ*(ₓ)(N) = arg max_θ (𝔼ᵧ∼Target(θ,N,x)[𝟙ᵧ=ᵧ*(ₓ)])\n\nwhere y*(x) denotes ground-truth correct response for x.\n\n### 3.1 Reward-Aware Compute-Optimal Scaling Strategy\n\nThe paper proposes that rewards should integrate into compute-optimal TTS strategy. The reward-aware compute-optimal TTS formulation:\n\nθ*ₓ,ᵧ*(ₓ),ℛ(N) = arg max_θ (𝔼ᵧ∼Target(θ,N,x,ℛ)[𝟙ᵧ=ᵧ*(ₓ)])\n\nwhere Target(θ,N,x,ℛ) represents the output distribution of policy model θ, adjusted by reward function ℛ, under compute budget N and prompt x. \"For sampling-based scaling methods, Target(θ,N,x,ℛ)=Target(θ,N,x)\" (Liu et al., 2025).\n\nThis reward-aware strategy ensures \"compute-optimal scaling adapts to the policy model, prompt, and reward function\" (Liu et al., 2025).\n\n### 3.2 Absolute Problem Difficulty Criterion\n\nRather than using difficulty levels from MATH or oracle labels based on Pass@1 accuracy quantiles, the paper proposes absolute thresholds based on Pass@1 accuracy:\n- Easy: 50%-100%\n- Medium: 10%-50%\n- Hard: 0%-10%\n\n---\n\n## 3. Key Findings, Results, and Analysis\n\n### 4.2 How TTS Improves with Different Policy Models and PRMs (Q1)\n\n**Key Finding:** \"PRMs are hard to generalize across policy models and tasks\" (Liu et al., 2025). Results show performance varies significantly depending on policy-PRM combinations. For Llama-3.1-8B-Instruct, search-based methods with Skywork and Qwen2.5-Math PRMs improve substantially with larger compute budgets, while Math-Shepherd and RLHFlow PRMs remain relatively poor.\n\n**Additional Observation:** \"The optimal TTS method depends on the PRM used\" (Liu et al., 2025). BoN outperforms other strategies most often when using Math-Shepherd and RLHFlow PRMs, while search-based methods perform better with Skywork and Qwen2.5-Math PRMs.\n\n**Relationship Finding:** TTS performance positively correlates with process supervision abilities of different PRMs, with fitted function: Y = 7.66 log(X) + 44.31\n\n**Scaling with Model Size:** For small policy models, \"search-based methods outperform BoN, while for large policy models, BoN is more effective\" (Liu et al., 2025). This occurs because larger models have stronger reasoning capabilities and don't require step-by-step verification.\n\n### 4.3 TTS Improvement Across Problem Difficulty Levels (Q2)\n\n**Finding:** \"The optimal TTS methods vary with different difficulty levels\" (Liu et al., 2025). For small policy models (fewer than 7B parameters), BoN works better for easy problems while beam search performs better for harder problems. For models between 7B-32B parameters, DVTS performs well for easy and medium problems, with beam search preferable for hard problems. For 72B parameter models, BoN remains best for all difficulty levels.\n\n### 4.4 PRM Characteristics Analysis (Q3)\n\n**Length Bias:** Analysis of training data reveals that different PRMs exhibit bias toward specific response lengths. For example, \"the number of inference tokens of scaling with RLHFlow-PRM-Deepseek-8B is consistently larger than that of RLHFlow-PRM-Mistral-8B, nearly 2×\" (Liu et al., 2025).\n\n**Voting Method Sensitivity:** Different PRMs show varying sensitivity to voting methods. Skywork-PRM-7B works better with PRM-Vote than PRM-Max, while Qwen2.5-Math-PRM-7B shows low sensitivity to voting methods.\n\n### 5.1 Can Smaller Models Outperform Larger Models? (Q4)\n\n**Major Finding:** A 1B LLM can exceed a 405B LLM on MATH-500, representing \"487.0% improvement\" compared to previous work. Specific results include:\n\n- Llama-3.2-3B-Instruct with compute-optimal TTS: 78.2% on MATH-500, 65.0% on AIME24\n- Llama-3.1-405B-Instruct (CoT): 71.4% on MATH-500, 23.3% on AIME24\n\nAdditional achievements:\n- \"Qwen2.5-0.5B-Instruct and Llama-3.2-3B-Instruct with the compute-optimal TTS strategy outperforms GPT-4o\" (Liu et al., 2025)\n- DeepSeek-R1-Distill-Qwen-1.5B outperforms o1-preview and o1-mini on both MATH-500 and AIME24\n- DeepSeek-R1-Distill-Qwen-7B outperforms o1 and DeepSeek-R1 on both datasets\n\n**FLOPS Efficiency:** Small policy models \"surpass large ones with less inference FLOPS and reduce the total FLOPS by 100×∼1000×\" (Liu et al., 2025).\n\n### 5.2 Compute-Optimal TTS vs. CoT and Majority Voting (Q5)\n\nKey comparative results show:\n- Llama-3.2-1B-Instruct: 154.6% performance gain, >256× efficiency gain\n- Llama-3.2-3B-Instruct: 88.9% performance gain, 14.1× efficiency gain\n- Qwen2.5-7B-Instruct: 18.5% performance gain, 35.9× efficiency gain\n\n\"As the number of parameters in the policy model increases, the improvement of TTS gradually decreases\" (Liu et al., 2025), suggesting TTS effectiveness directly relates to policy model reasoning ability.\n\n### 5.3 TTS vs. Long-CoT-Based Methods (Q6)\n\nComparative evaluation with rStar-Math, Eurus-2, SimpleRL, Satori, and DeepSeek-R1-Distill-Qwen-7B shows:\n- TTS with Qwen2.5-7B outperforms rStar-Math (78.4% → 88.0% on MATH-500), Eurus-2, SimpleRL, and Satori\n- Performance drops significantly on AIME24 compared to DeepSeek-R1-Distill-Qwen-7B\n- Conclusion: \"TTS is more effective than methods applying direct RL or SFT on data generated via MCTS but less effective than distilling from strong reasoning models\" (Liu et al., 2025)",
    "durationMs": 31506,
    "url": "https://arxiv.org/html/2502.06703"
  },
  "sourceToolAssistantUUID": "5f8ba4af-afaf-490f-84cb-81642bad658d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-28T11:28:10.825Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have substantial content from the paper. Let me now fetch the conclusion, limitations, and any additional analysis sections. I should also check for any OpenReview page for reviewer comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d4e70a-9c34-4524-8700-db9323b566d9",
  "isSidechain": false,
  "requestId": "req_011CbUtSHMEbZYK3BgtSwZhv",
  "type": "assistant",
  "uuid": "7b2059bf-ccc0-4b8b-b7b8-d883b5461126",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYWDa4PpNnsnchHeArQWtY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3536,
      "cache_read_input_tokens": 14839,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3536,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 405,
          "cache_read_input_tokens": 14839,
          "cache_creation_input_tokens": 3536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3536
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

_source line 20 · 2026-05-28T11:28:11.332Z_

Now let me fetch the conclusion/limitations and check for reviewer comments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b2059bf-ccc0-4b8b-b7b8-d883b5461126",
  "isSidechain": false,
  "requestId": "req_011CbUtSHMEbZYK3BgtSwZhv",
  "type": "assistant",
  "uuid": "a4865fbd-7a3a-4d15-b3c7-9f5bd1b64b97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYWDa4PpNnsnchHeArQWtY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3536,
      "cache_read_input_tokens": 14839,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3536,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 405,
          "cache_read_input_tokens": 14839,
          "cache_creation_input_tokens": 3536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3536
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

_source line 21 · 2026-05-28T11:28:14.325Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WEsFQRZBRpKcHjf3p7zujg`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.06703",
  "prompt": "Extract the FULL text of the following sections from this paper:\n1. Conclusion section\n2. Limitations section (if present)\n3. Discussion section (if present)\n4. Any section about related work that discusses Singhi et al., Setlur et al., or verification-generation tradeoffs\n5. Any ablation studies or analysis of difficulty-aware allocation\n\nReturn complete text, not summaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4865fbd-7a3a-4d15-b3c7-9f5bd1b64b97",
  "isSidechain": false,
  "requestId": "req_011CbUtSHMEbZYK3BgtSwZhv",
  "type": "assistant",
  "uuid": "ecbc8051-dbf2-4078-8ad4-71d87a52b4d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYWDa4PpNnsnchHeArQWtY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3536,
      "cache_read_input_tokens": 14839,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3536,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 405,
          "cache_read_input_tokens": 14839,
          "cache_creation_input_tokens": 3536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3536
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

_source line 22 · 2026-05-28T11:28:16.848Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LNXteL4zDf7Sx5tAPazGcX`</summary>

```json
{
  "url": "https://openreview.net/search?term=Can+1B+LLM+Surpass+405B+LLM+Rethinking+Compute-Optimal+Test-Time+Scaling",
  "prompt": "Find any OpenReview submission for the paper \"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling\" by Liu et al. Return the submission URL, venue, reviewer scores, and any reviewer comments you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecbc8051-dbf2-4078-8ad4-71d87a52b4d5",
  "isSidechain": false,
  "requestId": "req_011CbUtSHMEbZYK3BgtSwZhv",
  "type": "assistant",
  "uuid": "1a4546fd-e690-428b-bf76-47aa5f007e28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYWDa4PpNnsnchHeArQWtY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3536,
      "cache_read_input_tokens": 14839,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3536,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 405,
          "cache_read_input_tokens": 14839,
          "cache_creation_input_tokens": 3536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3536
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

_source line 23 · 2026-05-28T11:28:19.135Z_

<details><summary>↩ Tool result · `toolu_01LNXteL4zDf7Sx5tAPazGcX`</summary>

```text
I cannot find the submission you're looking for based on the provided web page content. The page shown is only the OpenReview.net homepage footer and navigation elements, which does not contain any information about specific papers, submissions, venues, reviewer scores, or comments.

To locate this paper, you would need to:
- Visit OpenReview.net directly
- Use their search functionality to find "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"
- Navigate to the specific submission page to view venue details, reviewer assessments, and feedback
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a4546fd-e690-428b-bf76-47aa5f007e28",
  "isSidechain": false,
  "promptId": "69ca1a40-1583-48e0-b778-6a85a0d2e8bd",
  "type": "user",
  "uuid": "0e4dcc78-4fa6-4aba-a4e3-a3789c48731c",
  "toolUseResult": {
    "bytes": 62419,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find the submission you're looking for based on the provided web page content. The page shown is only the OpenReview.net homepage footer and navigation elements, which does not contain any information about specific papers, submissions, venues, reviewer scores, or comments.\n\nTo locate this paper, you would need to:\n- Visit OpenReview.net directly\n- Use their search functionality to find \"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling\"\n- Navigate to the specific submission page to view venue details, reviewer assessments, and feedback",
    "durationMs": 2285,
    "url": "https://openreview.net/search?term=Can+1B+LLM+Surpass+405B+LLM+Rethinking+Compute-Optimal+Test-Time+Scaling"
  },
  "sourceToolAssistantUUID": "1a4546fd-e690-428b-bf76-47aa5f007e28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T11:28:24.110Z_

<details><summary>↩ Tool result · `toolu_01WEsFQRZBRpKcHjf3p7zujg`</summary>

```text
# Extracted Sections from Paper

## 1. Conclusion Section

"In this paper, we present a thorough empirical analysis of compute-optimal test-time scaling from the perspectives of different policy models, PRMs, and more challenging evaluation tasks. Our findings demonstrate the dependency of compute-optimal TTS strategies on policy models, PRMs, and problem difficulty, validating that smaller language models can perform better than larger models when applying compute-optimal TTS. Our results show that a 1B model can achieve better performance than a 405B model through TTS. Additionally, we demonstrate that a 7B PRM can achieve strong TTS results by supervising a more capable 72B policy model, which suggests the importance of investigating a true "weak-to-strong" approach instead of the current "strong-to-weak" supervision for policy optimization. To achieve this goal, we need to develop more efficient supervision methods, as both PRM-based and RL-based approaches have limitations due to their dependence on high-quality supervision. Future work should focus on developing more adaptable and universal supervision mechanisms to boost the performance of small language models on complex tasks and provide new approaches for developing efficient reasoning strategies."

## 2. Limitations Section

"Although we provide a comprehensive evaluation of TTS on mathematical tasks, there are still some limitations and future directions to explore: (1) Extending TTS to more tasks such as coding and chemistry tasks. (2) Exploring more effective methods for compute-optimal TTS."

## 3. Discussion Section

No separate "Discussion" section exists as a standalone heading in this paper. The discussion content is integrated into the Conclusion section above.

## 4. Related Work Sections

The paper contains three Related Work subsections but does **not** discuss Singhi et al., Setlur et al., or verification-generation tradeoffs explicitly. However, Setlur et al. is cited:

**Process Reward Models subsection mentions:** "Recently, more advanced PRMs are explored from advantage modeling (Setlur et al., [2024b]), Q-value rankings (Li and Li, 2024), implicit rewards (Yuan et al., 2024), and entropy regularization (Zhang et al., 2024b) perspectives."

The complete Related Work section discusses LLM test-time scaling, improving mathematical reasoning, and process reward models but does not contain the specific authors or concepts you requested in a dedicated discussion.

## 5. Difficulty-Aware Allocation Analysis

Section **3.2 "Absolute Problem Difficulty Criterion is More Effective Than Quantiles"** addresses difficulty classification: "we use absolute thresholds instead of quantiles to measure problem difficulty. Specifically, we define three difficulty levels based on Pass@1 accuracy: easy (50%∼100%), medium (10%∼50%), and hard (0%∼10%)."

Section **4.3 "How does TTS improve for problems with different difficulty levels? (Q2)"** provides the detailed analysis of difficulty-aware performance across methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecbc8051-dbf2-4078-8ad4-71d87a52b4d5",
  "isSidechain": false,
  "promptId": "69ca1a40-1583-48e0-b778-6a85a0d2e8bd",
  "type": "user",
  "uuid": "7c5dad51-4bec-466d-be27-4c83e9dc0942",
  "toolUseResult": {
    "bytes": 353517,
    "code": 200,
    "codeText": "OK",
    "result": "# Extracted Sections from Paper\n\n## 1. Conclusion Section\n\n\"In this paper, we present a thorough empirical analysis of compute-optimal test-time scaling from the perspectives of different policy models, PRMs, and more challenging evaluation tasks. Our findings demonstrate the dependency of compute-optimal TTS strategies on policy models, PRMs, and problem difficulty, validating that smaller language models can perform better than larger models when applying compute-optimal TTS. Our results show that a 1B model can achieve better performance than a 405B model through TTS. Additionally, we demonstrate that a 7B PRM can achieve strong TTS results by supervising a more capable 72B policy model, which suggests the importance of investigating a true \"weak-to-strong\" approach instead of the current \"strong-to-weak\" supervision for policy optimization. To achieve this goal, we need to develop more efficient supervision methods, as both PRM-based and RL-based approaches have limitations due to their dependence on high-quality supervision. Future work should focus on developing more adaptable and universal supervision mechanisms to boost the performance of small language models on complex tasks and provide new approaches for developing efficient reasoning strategies.\"\n\n## 2. Limitations Section\n\n\"Although we provide a comprehensive evaluation of TTS on mathematical tasks, there are still some limitations and future directions to explore: (1) Extending TTS to more tasks such as coding and chemistry tasks. (2) Exploring more effective methods for compute-optimal TTS.\"\n\n## 3. Discussion Section\n\nNo separate \"Discussion\" section exists as a standalone heading in this paper. The discussion content is integrated into the Conclusion section above.\n\n## 4. Related Work Sections\n\nThe paper contains three Related Work subsections but does **not** discuss Singhi et al., Setlur et al., or verification-generation tradeoffs explicitly. However, Setlur et al. is cited:\n\n**Process Reward Models subsection mentions:** \"Recently, more advanced PRMs are explored from advantage modeling (Setlur et al., [2024b]), Q-value rankings (Li and Li, 2024), implicit rewards (Yuan et al., 2024), and entropy regularization (Zhang et al., 2024b) perspectives.\"\n\nThe complete Related Work section discusses LLM test-time scaling, improving mathematical reasoning, and process reward models but does not contain the specific authors or concepts you requested in a dedicated discussion.\n\n## 5. Difficulty-Aware Allocation Analysis\n\nSection **3.2 \"Absolute Problem Difficulty Criterion is More Effective Than Quantiles\"** addresses difficulty classification: \"we use absolute thresholds instead of quantiles to measure problem difficulty. Specifically, we define three difficulty levels based on Pass@1 accuracy: easy (50%∼100%), medium (10%∼50%), and hard (0%∼10%).\"\n\nSection **4.3 \"How does TTS improve for problems with different difficulty levels? (Q2)\"** provides the detailed analysis of difficulty-aware performance across methods.",
    "durationMs": 9781,
    "url": "https://arxiv.org/html/2502.06703"
  },
  "sourceToolAssistantUUID": "ecbc8051-dbf2-4078-8ad4-71d87a52b4d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "7c5dad51-4bec-466d-be27-4c83e9dc0942",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Liu et al. compute-optimal test-time scaling paper",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568"
}
```

---

### Assistant

_source line 27 · 2026-05-28T11:28:26.768Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try to find the paper on OpenReview with a direct search, and also get the detailed experimental setup and figures from the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c5dad51-4bec-466d-be27-4c83e9dc0942",
  "isSidechain": false,
  "requestId": "req_011CbUtTTjLtcotjTCsmEmNF",
  "type": "assistant",
  "uuid": "1a4c99c5-a7a7-4e2e-b3c2-5caada0550cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EZhd9xeMbVHAidTTc1yrD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 166,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 18375,
      "output_tokens": 422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 166,
          "output_tokens": 422,
          "cache_read_input_tokens": 18375,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1099
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

_source line 28 · 2026-05-28T11:28:27.279Z_

Let me try to find the paper on OpenReview and get more details on the experimental methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a4c99c5-a7a7-4e2e-b3c2-5caada0550cc",
  "isSidechain": false,
  "requestId": "req_011CbUtTTjLtcotjTCsmEmNF",
  "type": "assistant",
  "uuid": "b4258794-d09d-4aca-963c-420a65159a01",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EZhd9xeMbVHAidTTc1yrD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 166,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 18375,
      "output_tokens": 422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 166,
          "output_tokens": 422,
          "cache_read_input_tokens": 18375,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1099
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

_source line 29 · 2026-05-28T11:28:28.708Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NmHMXKqwPthwhvbK6UoVxB`</summary>

```json
{
  "url": "https://openreview.net/search?term=%22Can+1B+LLM+Surpass+405B%22&content=all",
  "prompt": "Find any submissions related to \"Can 1B LLM Surpass 405B LLM\" paper. Return submission URLs, venue, and any reviewer information available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4258794-d09d-4aca-963c-420a65159a01",
  "isSidechain": false,
  "requestId": "req_011CbUtTTjLtcotjTCsmEmNF",
  "type": "assistant",
  "uuid": "7fff25a3-7ed3-4736-9636-b0a2446602a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EZhd9xeMbVHAidTTc1yrD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 166,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 18375,
      "output_tokens": 422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 166,
          "output_tokens": 422,
          "cache_read_input_tokens": 18375,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1099
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

_source line 30 · 2026-05-28T11:28:33.474Z_

<details><summary>↩ Tool result · `toolu_01NmHMXKqwPthwhvbK6UoVxB`</summary>

```text
Based on the web page content provided, I cannot find any submissions related to "Can 1B LLM Surpass 405B LLM" or similar papers.

The content shown is limited to OpenReview's navigation menu and footer information, which includes links to general pages like "About OpenReview," "All Venues," and "FAQ," but does not contain search results or specific submission details.

To locate this paper, you would need to:
1. Visit [OpenReview.net](/venues) and use their search functionality
2. Browse relevant conference or workshop venues
3. Search by title, authors, or keywords in their submission database

The current page excerpt does not display actual submission records or reviewer information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fff25a3-7ed3-4736-9636-b0a2446602a4",
  "isSidechain": false,
  "promptId": "69ca1a40-1583-48e0-b778-6a85a0d2e8bd",
  "type": "user",
  "uuid": "370962e0-89d0-4c52-8865-dc33e5739cdb",
  "toolUseResult": {
    "bytes": 62354,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find any submissions related to \"Can 1B LLM Surpass 405B LLM\" or similar papers.\n\nThe content shown is limited to OpenReview's navigation menu and footer information, which includes links to general pages like \"About OpenReview,\" \"All Venues,\" and \"FAQ,\" but does not contain search results or specific submission details.\n\nTo locate this paper, you would need to:\n1. Visit [OpenReview.net](/venues) and use their search functionality\n2. Browse relevant conference or workshop venues\n3. Search by title, authors, or keywords in their submission database\n\nThe current page excerpt does not display actual submission records or reviewer information.",
    "durationMs": 4762,
    "url": "https://openreview.net/search?term=%22Can+1B+LLM+Surpass+405B%22&content=all"
  },
  "sourceToolAssistantUUID": "7fff25a3-7ed3-4736-9636-b0a2446602a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-28T11:28:33.692Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Uoi9gYxU9VDXii3j54A4Fr`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.06703",
  "prompt": "Extract the FULL experimental setup details from this paper:\n1. What policy models were used? (all sizes and model families)\n2. What PRMs were used? (all PRMs listed)\n3. What benchmarks were used?\n4. What specific TTS methods were compared?\n5. What was the compute budget / how was compute measured?\n6. Any tables showing the main results (reproduce the key numbers)\n7. The reward-aware compute-optimal scaling strategy details — how exactly does it work?\n8. How do they estimate problem difficulty? What signals do they use?\n9. Any analysis of how the optimal strategy changes per-instance or per-difficulty level\n\nReturn complete details, not summaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "370962e0-89d0-4c52-8865-dc33e5739cdb",
  "isSidechain": false,
  "requestId": "req_011CbUtTTjLtcotjTCsmEmNF",
  "type": "assistant",
  "uuid": "17c081c8-c160-4b4d-8223-300ed1f5d212",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EZhd9xeMbVHAidTTc1yrD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 166,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 18375,
      "output_tokens": 422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 166,
          "output_tokens": 422,
          "cache_read_input_tokens": 18375,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1099
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

_source line 32 · 2026-05-28T11:28:49.607Z_

<details><summary>↩ Tool result · `toolu_01Uoi9gYxU9VDXii3j54A4Fr`</summary>

```text
# Experimental Setup Details

## 1. Policy Models

**Llama 3 Family:**
- Llama-3.1-8B-Instruct
- Llama-3.1-70B-Instruct
- Llama-3.1-405B-Instruct
- Llama-3.2-1B-Instruct
- Llama-3.2-3B-Instruct

**Qwen2.5 Family:**
- Qwen2.5-0.5B-Instruct
- Qwen2.5-1.5B-Instruct
- Qwen2.5-3B-Instruct
- Qwen2.5-7B-Instruct
- Qwen2.5-14B-Instruct
- Qwen2.5-32B-Instruct
- Qwen2.5-72B-Instruct

**Distilled Reasoning Models:**
- DeepSeek-R1-Distill-Qwen-1.5B
- DeepSeek-R1-Distill-Qwen-7B

## 2. Process Reward Models (PRMs)

**Math-Shepherd Series:**
- Math-Shepherd-PRM-7B (trained on Mistral-7B)

**RLHFlow Series:**
- RLHFlow-PRM-Mistral-8B
- RLHFlow-PRM-Deepseek-8B

**Skywork Series:**
- Skywork-PRM-1.5B
- Skywork-PRM-7B

**Qwen2.5-Math Series:**
- Qwen2.5-Math-PRM-7B
- Qwen2.5-Math-PRM-72B

## 3. Benchmarks

- **MATH-500:** "500 representative problems from the test set of MATH"
- **AIME24:** "more challenging" competition-level mathematical dataset

## 4. Test-Time Scaling Methods

Three primary methods evaluated:

**Best-of-N (BoN):** Generate N responses; apply scoring/voting to select final answer

**Beam Search:** Initial N steps generated; verifier selects top N/M steps; recursive sampling of M additional steps per retained step; continues until maximum depth or EOS token

**Diverse Verifier Tree Search (DVTS):** Extends beam search by "dividing the search process into N/M subtrees, each of which is explored independently using beam search"

## 5. Compute Budget

Budgets used: {4, 16, 64, 256}

**Token limits:**
- CoT and BoN: maximum 8192 new tokens
- Search-based methods: 2048 tokens per step; 8192 total response tokens

**Temperature:** 0.0 for CoT; 0.7 for other methods

## 6. Key Results Tables

**Table 3 - Small Models vs. Large Models:**

| Model | MATH-500 | AIME24 |
|-------|----------|--------|
| Llama-3.2-3B (TTS) | 78.2 | 30.0 |
| Llama-3.1-405B (CoT) | 71.4 | 23.3 |
| Qwen2.5-0.5B (TTS) | 76.4 | 10.0 |
| DeepSeek-R1-Distill-7B (TTS) | 95.2 | 83.3 |
| DeepSeek-R1 (CoT) | 97.3 | 79.8 |

**Table 5 - Compute-Optimal Improvements:**

| Model | CoT | Majority | TTS | Gain |
|-------|-----|----------|-----|------|
| Llama-3.2-1B | 26.0 | 39.0 | 66.2 | 154.6% |
| Qwen2.5-0.5B | 31.6 | 47.2 | 76.4 | 141.8% |
| Qwen2.5-7B | 76.8 | 83.6 | 91.0 | 18.5% |

**Table 6 - TTS vs. Long-CoT Methods:**

| Method | MATH-500 | AIME24 |
|--------|----------|--------|
| Qwen2.5-7B w/ 72B PRM (TTS) | 91.0 | 36.7 |
| DeepSeek-R1-Distill-7B | 92.4 | 63.3 |

## 7. Reward-Aware Compute-Optimal Strategy

The paper proposes incorporating reward function into optimization:

$$\theta^*_{x,y^*(x),\mathcal{R}}(N) = \arg\max_\theta \mathbb{E}_{y \sim \text{Target}(\theta,N,x,\mathcal{R})}[\mathbbm{1}_{y=y^*(x)}]$$

This differs from previous formulations by: "ensuring that compute-optimal scaling adapts to the policy model, prompt, and reward function." For sampling methods, reward doesn't modify generation; for search methods, rewards guide step selection at each response stage.

## 8. Problem Difficulty Estimation

Rather than quantile-based grouping, the authors use **absolute Pass@1 accuracy thresholds:**

- **Easy:** 50%-100% Pass@1 accuracy
- **Medium:** 10%-50% Pass@1 accuracy  
- **Hard:** 0%-10% Pass@1 accuracy

Rationale: "different policy models have different reasoning capabilities," making fixed quantiles ineffective across models.

## 9. Per-Instance/Per-Difficulty Strategy Analysis

**By Model Size:** "For small policy models, search-based methods outperform BoN, while for large policy models, BoN is more effective"

**By Difficulty:** "For small policy models (fewer than 7B parameters), BoN is better for easy problems, while beam search works better for harder problems"

**By PRM Choice:** Performance "heavily depends on the specific PRMs used," with "Math-Shepherd and RLHFlow PRMs" showing poor search scaling versus "Skywork and Qwen2.5-Math PRMs" demonstrating strong budget scaling

**Scoring Methods:** Table 2 shows voting method sensitivity varies by PRM (Skywork-PRM-7B prefers PRM-Vote; Qwen2.5-Math-PRM-7B relatively insensitive)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17c081c8-c160-4b4d-8223-300ed1f5d212",
  "isSidechain": false,
  "promptId": "69ca1a40-1583-48e0-b778-6a85a0d2e8bd",
  "type": "user",
  "uuid": "51f6c648-1a02-4e14-95f7-32cf0c3e3d86",
  "toolUseResult": {
    "bytes": 353517,
    "code": 200,
    "codeText": "OK",
    "result": "# Experimental Setup Details\n\n## 1. Policy Models\n\n**Llama 3 Family:**\n- Llama-3.1-8B-Instruct\n- Llama-3.1-70B-Instruct\n- Llama-3.1-405B-Instruct\n- Llama-3.2-1B-Instruct\n- Llama-3.2-3B-Instruct\n\n**Qwen2.5 Family:**\n- Qwen2.5-0.5B-Instruct\n- Qwen2.5-1.5B-Instruct\n- Qwen2.5-3B-Instruct\n- Qwen2.5-7B-Instruct\n- Qwen2.5-14B-Instruct\n- Qwen2.5-32B-Instruct\n- Qwen2.5-72B-Instruct\n\n**Distilled Reasoning Models:**\n- DeepSeek-R1-Distill-Qwen-1.5B\n- DeepSeek-R1-Distill-Qwen-7B\n\n## 2. Process Reward Models (PRMs)\n\n**Math-Shepherd Series:**\n- Math-Shepherd-PRM-7B (trained on Mistral-7B)\n\n**RLHFlow Series:**\n- RLHFlow-PRM-Mistral-8B\n- RLHFlow-PRM-Deepseek-8B\n\n**Skywork Series:**\n- Skywork-PRM-1.5B\n- Skywork-PRM-7B\n\n**Qwen2.5-Math Series:**\n- Qwen2.5-Math-PRM-7B\n- Qwen2.5-Math-PRM-72B\n\n## 3. Benchmarks\n\n- **MATH-500:** \"500 representative problems from the test set of MATH\"\n- **AIME24:** \"more challenging\" competition-level mathematical dataset\n\n## 4. Test-Time Scaling Methods\n\nThree primary methods evaluated:\n\n**Best-of-N (BoN):** Generate N responses; apply scoring/voting to select final answer\n\n**Beam Search:** Initial N steps generated; verifier selects top N/M steps; recursive sampling of M additional steps per retained step; continues until maximum depth or EOS token\n\n**Diverse Verifier Tree Search (DVTS):** Extends beam search by \"dividing the search process into N/M subtrees, each of which is explored independently using beam search\"\n\n## 5. Compute Budget\n\nBudgets used: {4, 16, 64, 256}\n\n**Token limits:**\n- CoT and BoN: maximum 8192 new tokens\n- Search-based methods: 2048 tokens per step; 8192 total response tokens\n\n**Temperature:** 0.0 for CoT; 0.7 for other methods\n\n## 6. Key Results Tables\n\n**Table 3 - Small Models vs. Large Models:**\n\n| Model | MATH-500 | AIME24 |\n|-------|----------|--------|\n| Llama-3.2-3B (TTS) | 78.2 | 30.0 |\n| Llama-3.1-405B (CoT) | 71.4 | 23.3 |\n| Qwen2.5-0.5B (TTS) | 76.4 | 10.0 |\n| DeepSeek-R1-Distill-7B (TTS) | 95.2 | 83.3 |\n| DeepSeek-R1 (CoT) | 97.3 | 79.8 |\n\n**Table 5 - Compute-Optimal Improvements:**\n\n| Model | CoT | Majority | TTS | Gain |\n|-------|-----|----------|-----|------|\n| Llama-3.2-1B | 26.0 | 39.0 | 66.2 | 154.6% |\n| Qwen2.5-0.5B | 31.6 | 47.2 | 76.4 | 141.8% |\n| Qwen2.5-7B | 76.8 | 83.6 | 91.0 | 18.5% |\n\n**Table 6 - TTS vs. Long-CoT Methods:**\n\n| Method | MATH-500 | AIME24 |\n|--------|----------|--------|\n| Qwen2.5-7B w/ 72B PRM (TTS) | 91.0 | 36.7 |\n| DeepSeek-R1-Distill-7B | 92.4 | 63.3 |\n\n## 7. Reward-Aware Compute-Optimal Strategy\n\nThe paper proposes incorporating reward function into optimization:\n\n$$\\theta^*_{x,y^*(x),\\mathcal{R}}(N) = \\arg\\max_\\theta \\mathbb{E}_{y \\sim \\text{Target}(\\theta,N,x,\\mathcal{R})}[\\mathbbm{1}_{y=y^*(x)}]$$\n\nThis differs from previous formulations by: \"ensuring that compute-optimal scaling adapts to the policy model, prompt, and reward function.\" For sampling methods, reward doesn't modify generation; for search methods, rewards guide step selection at each response stage.\n\n## 8. Problem Difficulty Estimation\n\nRather than quantile-based grouping, the authors use **absolute Pass@1 accuracy thresholds:**\n\n- **Easy:** 50%-100% Pass@1 accuracy\n- **Medium:** 10%-50% Pass@1 accuracy  \n- **Hard:** 0%-10% Pass@1 accuracy\n\nRationale: \"different policy models have different reasoning capabilities,\" making fixed quantiles ineffective across models.\n\n## 9. Per-Instance/Per-Difficulty Strategy Analysis\n\n**By Model Size:** \"For small policy models, search-based methods outperform BoN, while for large policy models, BoN is more effective\"\n\n**By Difficulty:** \"For small policy models (fewer than 7B parameters), BoN is better for easy problems, while beam search works better for harder problems\"\n\n**By PRM Choice:** Performance \"heavily depends on the specific PRMs used,\" with \"Math-Shepherd and RLHFlow PRMs\" showing poor search scaling versus \"Skywork and Qwen2.5-Math PRMs\" demonstrating strong budget scaling\n\n**Scoring Methods:** Table 2 shows voting method sensitivity varies by PRM (Skywork-PRM-7B prefers PRM-Vote; Qwen2.5-Math-PRM-7B relatively insensitive)",
    "durationMs": 15912,
    "url": "https://arxiv.org/html/2502.06703"
  },
  "sourceToolAssistantUUID": "17c081c8-c160-4b4d-8223-300ed1f5d212",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-28T11:28:49.614Z_

```json
{
  "parentUuid": "51f6c648-1a02-4e14-95f7-32cf0c3e3d86",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "06232a1d-826b-45cc-a429-fc6466a9b1dc",
  "timestamp": "2026-05-28T11:28:49.614Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-28T11:28:52.510Z_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive information about the paper. Let me also check if this paper has been accepted at any venue by searching for it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06232a1d-826b-45cc-a429-fc6466a9b1dc",
  "isSidechain": false,
  "requestId": "req_011CbUtVLmx15EXC86oCUJaQ",
  "type": "assistant",
  "uuid": "a7afff48-8d94-429a-901c-7d52d3eb55e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJrNYvCNxidy36dZAATdrp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2507,
      "cache_read_input_tokens": 19474,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 19474,
          "cache_creation_input_tokens": 2507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2507
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

_source line 35 · 2026-05-28T11:28:53.470Z_

Let me try one more search for reviewer feedback and check the paper's related work section for references to the seed papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7afff48-8d94-429a-901c-7d52d3eb55e6",
  "isSidechain": false,
  "requestId": "req_011CbUtVLmx15EXC86oCUJaQ",
  "type": "assistant",
  "uuid": "564f1673-86d6-4079-8b22-c4455709c8fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJrNYvCNxidy36dZAATdrp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2507,
      "cache_read_input_tokens": 19474,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 19474,
          "cache_creation_input_tokens": 2507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2507
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

_source line 36 · 2026-05-28T11:29:00.317Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F7WzUV7Y8unAQ7N68KUwBU`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.06703",
  "prompt": "Extract ALL of the following from this paper:\n1. The full Related Work section text\n2. Any references to or citations of: Singhi et al., \"When To Solve When To Verify\", \"scaling laws for generation-verification\", \"verification granularity\", \"ST-BoN\", \"Best-of-N\", Setlur et al.\n3. What are the paper's specific findings about WHEN different verification/scoring strategies are optimal? (e.g., when is BoN better vs beam search vs DVTS — what exact conditions?)\n4. Any analysis of PRM quality vs. compute allocation tradeoff\n5. The \"weak-to-strong\" supervision finding details\n6. Tables or figures showing per-difficulty-level breakdown of optimal strategies\n\nReturn ALL details, exact numbers where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "564f1673-86d6-4079-8b22-c4455709c8fd",
  "isSidechain": false,
  "requestId": "req_011CbUtVLmx15EXC86oCUJaQ",
  "type": "assistant",
  "uuid": "d0e8f663-2fb0-4e9a-9124-e57580801919",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJrNYvCNxidy36dZAATdrp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2507,
      "cache_read_input_tokens": 19474,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 19474,
          "cache_creation_input_tokens": 2507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2507
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

_source line 37 · 2026-05-28T11:29:02.578Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017ZcD6BmDpfK2Gn23CCCS7g`</summary>

```json
{
  "url": "https://scholar.google.com/scholar?q=%22Can+1B+LLM+Surpass+405B+LLM%22+Liu",
  "prompt": "Find information about the paper \"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling\" - check if it has been accepted at any conference or venue. Return citation count, venue information, and any links to published versions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0e8f663-2fb0-4e9a-9124-e57580801919",
  "isSidechain": false,
  "requestId": "req_011CbUtVLmx15EXC86oCUJaQ",
  "type": "assistant",
  "uuid": "abcdaa58-578b-4904-bcf6-b41e5a3ca0bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJrNYvCNxidy36dZAATdrp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2507,
      "cache_read_input_tokens": 19474,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2507,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 19474,
          "cache_creation_input_tokens": 2507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2507
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

_source line 38 · 2026-05-28T11:29:03.225Z_

<details><summary>↩ Tool result · `toolu_017ZcD6BmDpfK2Gn23CCCS7g`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abcdaa58-578b-4904-bcf6-b41e5a3ca0bf",
  "isSidechain": false,
  "promptId": "69ca1a40-1583-48e0-b778-6a85a0d2e8bd",
  "type": "user",
  "uuid": "05ceba88-db70-47e7-966a-e5b841fd4bfd",
  "toolUseResult": {
    "bytes": 0,
    "code": 403,
    "codeText": "Forbidden",
    "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 644,
    "url": "https://scholar.google.com/scholar?q=%22Can+1B+LLM+Surpass+405B+LLM%22+Liu"
  },
  "sourceToolAssistantUUID": "abcdaa58-578b-4904-bcf6-b41e5a3ca0bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-28T11:29:10.045Z_

<details><summary>↩ Tool result · `toolu_01F7WzUV7Y8unAQ7N68KUwBU`</summary>

```text
# Analysis of Paper: "Can 1B LLM Surpass 405B LLM?"

## 1. Full Related Work Section

The Related Work section spans from section 6 and covers three main areas:

**LLM Test-Time Scaling:** Reviews majority voting, search-based methods, and refinement approaches. Notes that prior work "lacks evaluation with either strong verifiers or policies with different sizes/capabilities."

**Improving Mathematical Reasoning:** Discusses training-time methods (pre-training, supervised fine-tuning, self-training) and test-time methods (CoT variants, self-refinement, tool integration, self-verification).

**Process Reward Models:** Covers PRM development, data collection methods, and recent open-source PRMs from Math-Shepherd, RLHFlow, Skywork, and Qwen2.5-Math series.

## 2. References to Requested Citations

**NOT FOUND** in this paper:
- Singhi et al.
- "When To Solve When To Verify"
- "scaling laws for generation-verification"
- "verification granularity"
- "ST-BoN"
- Setlur et al. (referenced only regarding advantage modeling and RL from incorrect synthetic data, not verification strategies)

**Best-of-N** is discussed extensively as a comparison method.

## 3. Specific Findings: When Different Strategies Are Optimal

**Key findings by model size:**

- **Small models (<7B params):** "BoN is better for easy problems, while beam search works better for harder problems"
- **Medium models (7B-32B):** "DVTS performs well for easy and medium problems, and beam search is preferable for hard problems"
- **Large models (72B+):** "BoN is the best method for all difficulty levels"

**By PRM type:**
- Math-Shepherd and RLHFlow PRMs: BoN outperforms search methods
- Skywork and Qwen2.5-Math PRMs: Search-based methods scale better with budgets

## 4. PRM Quality vs. Compute Allocation Tradeoff

**Finding:** "TTS performance is positively correlated with the process supervision abilities of PRMs" with fitted function: Y=7.66log(X)+44.31, where Y=performance, X=PRM supervision ability.

**Key insight:** Stronger PRMs enable more effective compute scaling through search methods.

## 5. "Weak-to-Strong" Supervision Details

The paper proposes investigating "true weak-to-strong approach instead of current strong-to-weak supervision for policy optimization," suggesting that 7B PRMs can effectively supervise 72B policy models. This contrasts with typical practice of using strong models to train weaker ones.

## 6. Per-Difficulty-Level Breakdowns

**Figure 8 and 9 show:**

| Model Size | Easy (50-100% Pass@1) | Medium (10-50%) | Hard (0-10%) |
|---|---|---|---|
| <7B | BoN best | Beam search | Beam search |
| 7B-32B | DVTS | DVTS | Beam search |
| 72B | BoN | BoN | BoN |

**Improvement by difficulty:** Smaller models show greatest gains on hard problems; gains decrease with model capacity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0e8f663-2fb0-4e9a-9124-e57580801919",
  "isSidechain": false,
  "promptId": "69ca1a40-1583-48e0-b778-6a85a0d2e8bd",
  "type": "user",
  "uuid": "8b48d6fe-b544-4972-a8e5-113ee5c3f7d4",
  "toolUseResult": {
    "bytes": 353517,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of Paper: \"Can 1B LLM Surpass 405B LLM?\"\n\n## 1. Full Related Work Section\n\nThe Related Work section spans from section 6 and covers three main areas:\n\n**LLM Test-Time Scaling:** Reviews majority voting, search-based methods, and refinement approaches. Notes that prior work \"lacks evaluation with either strong verifiers or policies with different sizes/capabilities.\"\n\n**Improving Mathematical Reasoning:** Discusses training-time methods (pre-training, supervised fine-tuning, self-training) and test-time methods (CoT variants, self-refinement, tool integration, self-verification).\n\n**Process Reward Models:** Covers PRM development, data collection methods, and recent open-source PRMs from Math-Shepherd, RLHFlow, Skywork, and Qwen2.5-Math series.\n\n## 2. References to Requested Citations\n\n**NOT FOUND** in this paper:\n- Singhi et al.\n- \"When To Solve When To Verify\"\n- \"scaling laws for generation-verification\"\n- \"verification granularity\"\n- \"ST-BoN\"\n- Setlur et al. (referenced only regarding advantage modeling and RL from incorrect synthetic data, not verification strategies)\n\n**Best-of-N** is discussed extensively as a comparison method.\n\n## 3. Specific Findings: When Different Strategies Are Optimal\n\n**Key findings by model size:**\n\n- **Small models (<7B params):** \"BoN is better for easy problems, while beam search works better for harder problems\"\n- **Medium models (7B-32B):** \"DVTS performs well for easy and medium problems, and beam search is preferable for hard problems\"\n- **Large models (72B+):** \"BoN is the best method for all difficulty levels\"\n\n**By PRM type:**\n- Math-Shepherd and RLHFlow PRMs: BoN outperforms search methods\n- Skywork and Qwen2.5-Math PRMs: Search-based methods scale better with budgets\n\n## 4. PRM Quality vs. Compute Allocation Tradeoff\n\n**Finding:** \"TTS performance is positively correlated with the process supervision abilities of PRMs\" with fitted function: Y=7.66log(X)+44.31, where Y=performance, X=PRM supervision ability.\n\n**Key insight:** Stronger PRMs enable more effective compute scaling through search methods.\n\n## 5. \"Weak-to-Strong\" Supervision Details\n\nThe paper proposes investigating \"true weak-to-strong approach instead of current strong-to-weak supervision for policy optimization,\" suggesting that 7B PRMs can effectively supervise 72B policy models. This contrasts with typical practice of using strong models to train weaker ones.\n\n## 6. Per-Difficulty-Level Breakdowns\n\n**Figure 8 and 9 show:**\n\n| Model Size | Easy (50-100% Pass@1) | Medium (10-50%) | Hard (0-10%) |\n|---|---|---|---|\n| <7B | BoN best | Beam search | Beam search |\n| 7B-32B | DVTS | DVTS | Beam search |\n| 72B | BoN | BoN | BoN |\n\n**Improvement by difficulty:** Smaller models show greatest gains on hard problems; gains decrease with model capacity.",
    "durationMs": 9722,
    "url": "https://arxiv.org/html/2502.06703"
  },
  "sourceToolAssistantUUID": "d0e8f663-2fb0-4e9a-9124-e57580801919",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-28T11:29:32.730Z_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive information about the paper. Let me synthesize my analysis and produce the JSON output.

Key observations for my analysis:

1. **Problem Identification**: The authors identified that prior TTS work evaluated methods in isolation without systematically varying the three key factors: policy model, PRM quality, and problem difficulty. This created a gap where compute-optimal strategies were treated as universal rather than conditional.

2. **Key Insight**: The optimal TTS strategy is not a single method but a function of (policy model capability, PRM quality, problem difficulty). This three-way interaction was unexplored — prior work would pick one method and show it scales, without asking "when should I use which method?"
   
3. **Innovation Type**: Rather than proposing a new algorithm, this is fundamentally an empirical analysis paper that uncovers important interaction effects through systematic study. The reward-aware compute-optimal scaling formulation itself is straightforward, but the real value lies in what the experiments reveal about when different methods work best.

4. **What makes it compelling**: The attention-grabbing framing combined with a thorough experimental design across multiple models, PRMs, and difficulty levels yields a practical finding — that PRM quality is a critical factor that interacts significantly with model size and problem complexity.

5. **Key limitations**: The scope is restricted to math benchmarks, there's no adaptive system that responds to individual problem characteristics, and the compute-optimal strategies depend on knowing problem difficulty upfront, which requires oracle information. The theoretical foundation for the reward-aware formulation is also relatively thin.

6. **How it connects to our work**: This directly validates that uniform allocation strategies are suboptimal and demonstrates the three-way interaction between model size, PRM quality, and difficulty that we need to handle with adaptive depth selection. The empirical tables showing difficulty-dependent optimal strategies provide exactly the kind of evidence we need, though they rely on oracle labels rather than solving the online adaptation problem we're tackling.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b48d6fe-b544-4972-a8e5-113ee5c3f7d4",
  "isSidechain": false,
  "requestId": "req_011CbUtWr94XpEkRUtvGRPNg",
  "type": "assistant",
  "uuid": "fa71f347-a259-4861-9bc4-82570e6dd369",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWRxZ1WNUx931H6yxKzR1f",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 21981,
      "output_tokens": 2563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 2563,
          "cache_read_input_tokens": 21981,
          "cache_creation_input_tokens": 1288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1288
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

_source line 41 · 2026-05-28T11:30:18.499Z_

Now I have comprehensive information about the paper. Let me synthesize the full analysis.

```json
{
  "title": "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling",
  "venue": "arXiv 2025 (preprint, arXiv:2502.06703)",
  "problem_identification": "Prior test-time scaling (TTS) studies evaluated methods in isolation — picking one policy model, one PRM, and one benchmark — without systematically varying across these axes. The authors identified that this fragmented evaluation masked a critical three-way interaction: the compute-optimal TTS strategy depends jointly on the policy model's capability, the PRM's quality, AND the problem's difficulty. They found this gap by observing that different papers reached contradictory conclusions about which TTS method was best (BoN vs. beam search vs. DVTS), and hypothesized these contradictions arose because each study held different factors constant.",
  "key_insight": "The optimal test-time scaling strategy is not a universal choice but a conditional function of (policy model size, PRM quality, problem difficulty) — and these factors interact non-trivially: search-based methods dominate for small models on hard problems with strong PRMs, while Best-of-N dominates for large models regardless of difficulty. This means there is no single 'best TTS method,' and any compute-optimal framework must be reward-aware, incorporating the PRM as a first-class variable in the optimization.",
  "innovation_type": "analysis",
  "method_summary": "The authors conduct a massive grid experiment varying 14 policy models (0.5B–405B across Llama, Qwen, and DeepSeek families), 8 PRMs (Math-Shepherd, RLHFlow, Skywork, Qwen2.5-Math), 3 TTS methods (BoN, beam search, DVTS), and compute budgets {4, 16, 64, 256} on MATH-500 and AIME24. They propose a 'reward-aware compute-optimal' formulation that explicitly conditions the optimal strategy on the reward function ℛ in addition to the policy and prompt: θ* = argmax_θ E[1(y=y*)] where the target distribution depends on (θ, N, x, ℛ). They introduce an absolute difficulty criterion based on Pass@1 thresholds (easy: 50-100%, medium: 10-50%, hard: 0-10%) rather than quantile-based binning, arguing this provides consistency across models. The core analysis decomposes optimal strategy selection across the three axes, revealing systematic patterns: small models benefit from search on hard problems; large models prefer BoN universally; PRM quality correlates log-linearly with TTS performance (Y = 7.66 log(X) + 44.31).",
  "what_makes_it_good": "The paper succeeds through three craft elements: (1) a provocative, memorable framing ('1B beats 405B') that makes the contribution immediately legible and shareable; (2) exhaustive experimental coverage that turns what could be incremental findings into a definitive reference — the sheer scale of the grid (14 models × 8 PRMs × 3 methods × 4 budgets × 3 difficulty levels) makes the interaction effects convincing and hard to dismiss; (3) practical actionability — the difficulty × model-size strategy tables give practitioners a direct lookup for their setting. The 'weak-to-strong' observation (7B PRM supervising 72B policy) is a genuinely surprising finding that opens new research directions.",
  "limitations_acknowledged": "The authors explicitly acknowledge two major limitations: (1) evaluation is restricted to mathematical reasoning tasks (MATH-500 and AIME24 only) — they note the need to extend to coding and chemistry tasks; (2) the compute-optimal strategy selection itself is not automated — they don't provide an online algorithm that selects the optimal (method, PRM, budget) configuration per instance at inference time, leaving this as future work.",
  "open_questions": [
    "The difficulty-dependent strategy tables require oracle access to Pass@1 accuracy (which implies knowing the problem's difficulty in advance). How can difficulty be estimated online from early tokens or problem features to enable per-instance adaptive allocation — exactly the gap our proposed work fills?",
    "The paper treats verification depth as a discrete categorical choice (none/BoN/beam/DVTS) but doesn't explore intermediate granularities or continuous verification depth — is there a smooth verification-compute frontier, or are there phase transitions in when each method becomes optimal?",
    "The log-linear relationship between PRM quality and TTS performance (Y = 7.66 log(X) + 44.31) suggests diminishing returns from better PRMs. Does this relationship hold per-difficulty-level, or do hard problems show a steeper slope (i.e., benefit more from PRM quality improvements)?"
  ],
  "building_blocks": [
    "Absolute difficulty criterion based on Pass@1 thresholds (easy/medium/hard) — more stable than quantile-based binning across models",
    "Reward-aware compute-optimal formulation: Target(θ, N, x, ℛ) — making PRM a first-class optimization variable",
    "Strategy selection tables indexed by (model_size_bucket, difficulty_level, PRM_family) — could serve as initialization for a learned policy",
    "Log-linear PRM quality → TTS performance relationship as a predictive model for compute allocation",
    "DVTS (Diverse Verifier Tree Search) as a strong baseline for medium-difficulty problems with large budgets",
    "The 14-model × 8-PRM evaluation grid as a reusable benchmarking framework",
    "DeepSeek-R1-Distill models as strong baselines combining internal and external TTS"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "This paper is the strongest empirical motivation for our per-instance adaptive allocation thesis: it proves that the optimal verification strategy varies dramatically across the (model, PRM, difficulty) space but stops short of building an online algorithm to exploit this variance — exactly our proposed contribution. Their difficulty-dependent strategy tables (small model + hard problem → beam search; large model + any difficulty → BoN) provide the ground truth our difficulty estimator must learn to approximate, and their absolute difficulty criterion could be adopted as the target variable for our early-token difficulty classifier. Critically, their limitation of requiring oracle difficulty labels to select the optimal strategy is precisely the gap our online difficulty estimation from early reasoning tokens is designed to fill. Their finding that PRM quality interacts with optimal strategy choice also supports extending our framework from a 2D (K, d) optimization to a 3D (K, d, PRM) optimization, though this increases the search space and may require the bilinear decomposition from our theoretical anchor to remain tractable."
}
```

## Key Craft Lessons for Our Research

**What we can learn from HOW this paper innovates:**

1. **The "reconciliation" move**: The authors noticed that different TTS papers reached contradictory conclusions about which method was best. Instead of proposing yet another method, they asked *why* results contradicted — and discovered the answer was a missing interaction variable. This is a powerful research move: when the literature disagrees, the disagreement itself is a research opportunity.

2. **Scale as persuasion**: The 14×8×3×4×3 experimental grid is deliberately exhaustive. This is an analysis paper, so the contribution lives or dies on whether the findings are robust. The scale makes the interaction effects undeniable and positions the paper as a definitive reference rather than an incremental observation.

3. **The provocative framing works but carries risk**: "1B beats 405B" is memorable and attracts reads, but it's technically conditional (requires oracle strategy selection, strong PRM, specific benchmark). For our work, we should be similarly bold but transparent about conditions.

4. **The gap they left open is exactly our opportunity**: They demonstrate the variance in optimal strategy across difficulty levels but use *oracle* difficulty labels (Pass@1 accuracy). They cannot do per-instance adaptation at inference time. Our early-token difficulty estimation directly fills this gap. Their Tables 3 and 5 essentially provide the target policy our learned allocator must approximate.

5. **Baseline fear for us**: Their paper raises a real concern for our work — if the optimal strategy can be captured by a simple lookup table indexed by (model_size_bucket × difficulty_bucket), then our learned per-instance allocation needs to outperform this coarse-grained table lookup, not just fixed-strategy baselines. This sharpens our baseline fear test.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa71f347-a259-4861-9bc4-82570e6dd369",
  "isSidechain": false,
  "requestId": "req_011CbUtWr94XpEkRUtvGRPNg",
  "type": "assistant",
  "uuid": "d1960485-1035-4b2a-b579-7dd5d6e4e59e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWRxZ1WNUx931H6yxKzR1f",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 21981,
      "output_tokens": 2563,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1288,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 2563,
          "cache_read_input_tokens": 21981,
          "cache_creation_input_tokens": 1288,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1288
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "d1960485-1035-4b2a-b579-7dd5d6e4e59e",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Liu et al. compute-optimal test-time scaling paper",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "d1960485-1035-4b2a-b579-7dd5d6e4e59e",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Liu et al. compute-optimal test-time scaling paper",
  "sessionId": "a88bc0c5-6738-4cbd-8064-aa4dfb9f0568"
}
```

---
