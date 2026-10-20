# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-28 (UTC).** ## Y

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/a97a0a13-710e-4482-a7b3-a1528324cc9e.jsonl`
- **Structured JSON:** [`b39375944e90919dc536.json`](../../sessions/b3/b39375944e90919dc536.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T11:20:30.761Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T11:20:30.761Z",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2026\nTrack: Machine Learning (ML) — Efficient Inference and Reasoning\n\nDirection: Per-instance adaptive co-optimization of generation and verification compute, where both the number of generated solutions (K) and the verification depth (none/ORM/PRM/GenRM) are jointly selected based on online difficulty estimation from early reasoning tokens. Extends static aggregate scaling laws (Singhi et al.) to instance-adaptive, multi-depth allocation with a practical online algorithm.\n\nSeed Papers:\n- Singhi et al., \"When To Solve, When To Verify\" (arXiv 2025) — establishes aggregate scaling laws for generation-verification tradeoff; our work must explicitly extend this to per-instance, multi-depth allocation\n- Setlur et al., \"Scaling TTC Without Verification is Suboptimal\" (arXiv Feb 2025) — proves verification is essential and the gap grows with compute; motivates why verification budget allocation matters\n- Chen et al., \"VG-Search: Rethinking Optimal Verification Granularity\" (arXiv May 2025) — shows verification granularity matters for efficiency; we extend from granularity to depth and per-instance adaptation\n- Wang et al., \"ST-BoN\" (NeurIPS 2025 Spotlight) — early pruning via sampling consistency; a strong baseline for lightweight verification allocation\n\nKnown Gaps:\n- No method selects verification depth (none/ORM/PRM/GenRM) per-instance based on estimated difficulty; all existing work uses a fixed verification strategy across problems\n- Singhi et al.'s scaling laws are static and aggregate (one ratio for all problems); no online algorithm adapts the generation-verification split per-instance during inference\n- No framework jointly optimizes K (number of solutions) and d (verification depth) as coupled decision variables under a shared compute budget\n\nTheoretical Anchor: The bilinear structure of the joint optimization — P(correct) depends on coverage (increasing in K) and selection precision (increasing in d), while cost is c_g*K + c_v(d)*K = K*(c_g + c_v(d)) — admits a clean decomposition: for fixed d, optimal K = B/(c_g + c_v(d)), reducing the problem to selecting d* that maximizes selection precision per unit verification cost. This decomposition enables tractable optimization with provable approximation guarantees under mild assumptions on verifier accuracy monotonicity.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must evaluate on ≥4 benchmarks across ≥2 domains (math, code, science)\n- Must compare against Singhi et al.'s aggregate-optimal baseline and fixed-depth baselines\n\nQuality Self-Checks:\n- [x] Core insight: The optimal verification depth varies dramatically per problem — easy problems need no verification while hard problems benefit from expensive generative verification — and this variance is predictable from early tokens.\n- [x] Why not obvious: Singhi et al. showed the aggregate optimal ratio, but the per-instance variance and multi-depth selection weren't explored because their framework only compared two verification strategies (GenRM vs SC), not a continuum of depths.\n- [ ] Baseline fear test: A simple heuristic (e.g., always use PRM for problems longer than X tokens) could capture much of the benefit — must demonstrate learned allocation significantly outperforms simple rules. This is a REAL RISK.\n- [x] Information exploited: Early-token difficulty signals (entropy trajectory, hesitation markers from Zhou et al.) that are available before verification decisions must be made.\n\nAvoid:\n- Framing as 'first to study generation-verification tradeoff' — Singhi et al. already did this; frame as extending to per-instance multi-depth allocation\n- Math-only evaluation — must include code and science benchmarks\n- Pure scaling law contribution — must provide a practical online algorithm, not just power-law fits\n- Ignoring the baseline fear: if a simple threshold on problem length achieves 80% of the adaptive allocation's gain, the paper is dead**\n\n## Paper to analyze\n\n{\n  \"title\": \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\",\n  \"authors\": \"DeepSeek-AI (Guo et al.)\",\n  \"venue\": \"Nature 2025\",\n  \"url\": \"https://arxiv.org/abs/2501.12948\",\n  \"why_important\": \"Published in Nature; landmark reasoning model showing pure RL produces emergent self-verification — defines the reasoning model ecosystem your work operates in\",\n  \"one_line_summary\": \"Pure reinforcement learning without human-annotated reasoning traces produces emergent self-reflection and verification behaviors, achieving o1-level performance across math, code, and STEM.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T11:20:30.765Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T11:20:30.765Z",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

## Round 1

63 recorded events

### User

_source line 3 · 2026-05-28T11:20:30.776Z_

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
  "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
  "authors": "DeepSeek-AI (Guo et al.)",
  "venue": "Nature 2025",
  "url": "https://arxiv.org/abs/2501.12948",
  "why_important": "Published in Nature; landmark reasoning model showing pure RL produces emergent self-verification — defines the reasoning model ecosystem your work operates in",
  "one_line_summary": "Pure reinforcement learning without human-annotated reasoning traces produces emergent self-reflection and verification behaviors, achieving o1-level performance across math, code, and STEM."
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
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "6b7a3a6f-4654-420c-832c-55ea920371dc",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T11:20:30.775Z_

```json
{
  "parentUuid": "6b7a3a6f-4654-420c-832c-55ea920371dc",
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
  "uuid": "b7fae61a-2f09-4f6a-ad3f-d90a151b4adf",
  "timestamp": "2026-05-28T11:20:30.775Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T11:20:30.775Z_

```json
{
  "parentUuid": "b7fae61a-2f09-4f6a-ad3f-d90a151b4adf",
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
  "uuid": "796cc127-b36e-40f3-b764-96f7b0a0e808",
  "timestamp": "2026-05-28T11:20:30.775Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-28T11:20:30.775Z_

```json
{
  "parentUuid": "796cc127-b36e-40f3-b764-96f7b0a0e808",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7eabe793-2691-4469-ba47-04929d24b2fa",
  "timestamp": "2026-05-28T11:20:30.775Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
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
  "aiTitle": "Analyze DeepSeek-R1 reasoning innovation approach",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Assistant

_source line 8 · 2026-05-28T11:20:34.166Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze the DeepSeek-R1 paper in depth. Let me start by fetching the paper from arXiv to read its full content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eabe793-2691-4469-ba47-04929d24b2fa",
  "isSidechain": false,
  "requestId": "req_011CbUsra8qX9h2zRDsC7Rif",
  "type": "assistant",
  "uuid": "770c7d26-bfc2-4bdc-9489-041d4f0dbff4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJw73CKwApKvHxSXwUrzVA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 10620,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 3503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3503
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

_source line 9 · 2026-05-28T11:20:34.358Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QSxm2571aCFdY3DA5442dN`</summary>

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
  "parentUuid": "770c7d26-bfc2-4bdc-9489-041d4f0dbff4",
  "isSidechain": false,
  "requestId": "req_011CbUsra8qX9h2zRDsC7Rif",
  "type": "assistant",
  "uuid": "a1b3fbf9-287f-4587-8e4b-d373dac41e3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJw73CKwApKvHxSXwUrzVA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3503,
      "cache_read_input_tokens": 10620,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 10620,
          "cache_creation_input_tokens": 3503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3503
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

_source line 10 · 2026-05-28T11:20:34.366Z_

<details><summary>↩ Tool result · `toolu_01QSxm2571aCFdY3DA5442dN`</summary>

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
  "parentUuid": "a1b3fbf9-287f-4587-8e4b-d373dac41e3b",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "e57b724b-0791-46f8-80ad-837e1e71e4bc",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "a1b3fbf9-287f-4587-8e4b-d373dac41e3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-28T11:20:38.258Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the full paper HTML version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e57b724b-0791-46f8-80ad-837e1e71e4bc",
  "isSidechain": false,
  "requestId": "req_011CbUsrqq9hoYbiFCAGh2Jk",
  "type": "assistant",
  "uuid": "20e00863-c28a-48b9-9122-6297b44e2720",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cSms2W1bTHkVKzunoxVFn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 14123,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 14123,
          "cache_creation_input_tokens": 649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 649
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

_source line 12 · 2026-05-28T11:20:38.928Z_

Let me fetch the paper from multiple sources to get a comprehensive view.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20e00863-c28a-48b9-9122-6297b44e2720",
  "isSidechain": false,
  "requestId": "req_011CbUsrqq9hoYbiFCAGh2Jk",
  "type": "assistant",
  "uuid": "c967349f-cf0e-4931-a5bd-021efe3b11c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cSms2W1bTHkVKzunoxVFn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 14123,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 14123,
          "cache_creation_input_tokens": 649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 649
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

_source line 13 · 2026-05-28T11:20:40.349Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014pWqwrtHpZXMqeCzxH68oj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.12948",
  "prompt": "Extract the full abstract, author list, and any other metadata available on this arXiv page for the DeepSeek-R1 paper. Include the complete abstract text verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c967349f-cf0e-4931-a5bd-021efe3b11c6",
  "isSidechain": false,
  "requestId": "req_011CbUsrqq9hoYbiFCAGh2Jk",
  "type": "assistant",
  "uuid": "4eae8167-c987-482b-bf74-bfd5f95f380e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cSms2W1bTHkVKzunoxVFn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 14123,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 14123,
          "cache_creation_input_tokens": 649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 649
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

_source line 14 · 2026-05-28T11:20:43.182Z_

<details><summary>↩ Tool result · `toolu_01D5JvGm1hd8HWkuoqBbRfjx`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae703634-cfe6-4dc1-8367-0577043d3cf1",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "1a8a8994-a84f-42ee-bbcc-71f85a07b260",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 7,
    "url": "https://arxiv.org/html/2501.12948"
  },
  "sourceToolAssistantUUID": "ae703634-cfe6-4dc1-8367-0577043d3cf1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T11:20:43.173Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D5JvGm1hd8HWkuoqBbRfjx`</summary>

```json
{
  "url": "https://arxiv.org/html/2501.12948",
  "prompt": "Extract the FULL text of the following sections from this paper: 1) Introduction (complete), 2) Method/Approach sections (complete - including all subsections about RL training, cold start, distillation, etc.), 3) Any section discussing emergent behaviors like self-verification or reflection. Include all technical details, equations, training stages, reward design, and algorithmic choices. Be as complete as possible - do not summarize, extract the actual text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eae8167-c987-482b-bf74-bfd5f95f380e",
  "isSidechain": false,
  "requestId": "req_011CbUsrqq9hoYbiFCAGh2Jk",
  "type": "assistant",
  "uuid": "ae703634-cfe6-4dc1-8367-0577043d3cf1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cSms2W1bTHkVKzunoxVFn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 14123,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 14123,
          "cache_creation_input_tokens": 649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 649
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

_source line 16 · 2026-05-28T11:20:46.842Z_

<details><summary>↩ Tool result · `toolu_014pWqwrtHpZXMqeCzxH68oj`</summary>

```text
# DeepSeek-R1 Paper Metadata

## Title
DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

## Abstract
"General reasoning represents a long-standing and formidable challenge in artificial intelligence. Recent breakthroughs, exemplified by large language models (LLMs) and chain-of-thought prompting, have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent upon extensive human-annotated demonstrations, and models' capabilities are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions, and STEM fields, surpassing its counterparts trained via conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically harnessed to guide and enhance the reasoning capabilities of smaller models."

## Key Metadata
- **arXiv ID:** 2501.12948
- **Submitted:** January 22, 2025 (v1); January 4, 2026 (v2)
- **Subject Areas:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- **Journal Reference:** Nature, volume 645, pages 633-638 (2025)
- **DOI:** 10.48550/arXiv.2501.12948

## Lead Authors
Primary contributors include DeepSeek-AI team members Daya Guo, Dejian Yang, and approximately 200+ additional authors listed on the publication.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eae8167-c987-482b-bf74-bfd5f95f380e",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "39e158e8-647f-4c7c-8d50-64d215e5186d",
  "toolUseResult": {
    "bytes": 80029,
    "code": 200,
    "codeText": "OK",
    "result": "# DeepSeek-R1 Paper Metadata\n\n## Title\nDeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\n\n## Abstract\n\"General reasoning represents a long-standing and formidable challenge in artificial intelligence. Recent breakthroughs, exemplified by large language models (LLMs) and chain-of-thought prompting, have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent upon extensive human-annotated demonstrations, and models' capabilities are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions, and STEM fields, surpassing its counterparts trained via conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically harnessed to guide and enhance the reasoning capabilities of smaller models.\"\n\n## Key Metadata\n- **arXiv ID:** 2501.12948\n- **Submitted:** January 22, 2025 (v1); January 4, 2026 (v2)\n- **Subject Areas:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)\n- **Journal Reference:** Nature, volume 645, pages 633-638 (2025)\n- **DOI:** 10.48550/arXiv.2501.12948\n\n## Lead Authors\nPrimary contributors include DeepSeek-AI team members Daya Guo, Dejian Yang, and approximately 200+ additional authors listed on the publication.",
    "durationMs": 6490,
    "url": "https://arxiv.org/abs/2501.12948"
  },
  "sourceToolAssistantUUID": "4eae8167-c987-482b-bf74-bfd5f95f380e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "39e158e8-647f-4c7c-8d50-64d215e5186d",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze DeepSeek-R1 reasoning innovation approach",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Tool call

_source line 19 · 2026-05-28T11:20:51.746Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PrnbEUD8P1nvo7trtuacvf`</summary>

```json
{
  "url": "https://arxiv.org/html/2501.12948v2",
  "prompt": "Extract the FULL text of these sections: 1) Introduction (complete), 2) All Method/Approach sections (complete - including subsections on RL training, GRPO, cold start, reward design, distillation, pipeline stages), 3) Sections on emergent behaviors (self-verification, reflection, aha moments), 4) Experimental results summary, 5) Conclusion/Discussion. Include all technical details - training stages, reward functions, algorithmic choices, model sizes. Be maximally complete."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39e158e8-647f-4c7c-8d50-64d215e5186d",
  "isSidechain": false,
  "requestId": "req_011CbUsskjqr86vNnpA3W7Q5",
  "type": "assistant",
  "uuid": "8bb01fdc-921f-4bf7-8559-2c960d98286c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EY7T5tVjcLKWcMy9y8sKKE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 14772,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 298,
          "cache_read_input_tokens": 14772,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 800
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

_source line 20 · 2026-05-28T11:20:51.763Z_

<details><summary>↩ Tool result · `toolu_01PrnbEUD8P1nvo7trtuacvf`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bb01fdc-921f-4bf7-8559-2c960d98286c",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "7f3cf85e-9401-42c8-a72d-1b757363c623",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 12,
    "url": "https://arxiv.org/html/2501.12948v2"
  },
  "sourceToolAssistantUUID": "8bb01fdc-921f-4bf7-8559-2c960d98286c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T11:20:53.171Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QWfaJBSTkqKvr7Fgn1At6U`</summary>

```json
{
  "url": "https://huggingface.co/papers/2501.12948",
  "prompt": "Extract any discussion, community comments, or analysis about the DeepSeek-R1 paper. What do people highlight as the key contributions, limitations, or surprising findings?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f3cf85e-9401-42c8-a72d-1b757363c623",
  "isSidechain": false,
  "requestId": "req_011CbUsskjqr86vNnpA3W7Q5",
  "type": "assistant",
  "uuid": "50c768d0-2293-4c94-8c6a-d1aad469958e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EY7T5tVjcLKWcMy9y8sKKE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 14772,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 298,
          "cache_read_input_tokens": 14772,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 800
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

_source line 22 · 2026-05-28T11:20:53.820Z_

<details><summary>↩ Tool result · `toolu_01QWfaJBSTkqKvr7Fgn1At6U`</summary>

```text
&lt;persisted-output>
Output too large (85.5KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt

Preview (first 2KB):
# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

DeepSeek-AI

research@deepseek.com

## Abstract

General reasoning represents a long-standing and formidable challenge in artificial intelligence. Recent breakthroughs, exemplified by large language models (LLMs) (Brown et al., 2020; OpenAI, 2023) and chain-of-thought prompting (Wei et al., 2022b), have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent upon extensive human-annotated demonstrations, and models' capabilities are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions, and STEM fields, surpassing its counterparts trained via conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically harnessed to guide and enhance the reasoning capabilities of smaller models.

## 1. Introduction

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```````json
{
  "recorded_role": "user",
  "parentUuid": "50c768d0-2293-4c94-8c6a-d1aad469958e",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "e1c336dc-1a20-4087-bb91-7bf0e0cf339a",
  "toolUseResult": {
    "bytes": 87739,
    "code": 200,
    "codeText": "OK",
    "result": "# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\n\nDeepSeek-AI\n\nresearch@deepseek.com\n\n## Abstract\n\nGeneral reasoning represents a long-standing and formidable challenge in artificial intelligence. Recent breakthroughs, exemplified by large language models (LLMs) (Brown et al., 2020; OpenAI, 2023) and chain-of-thought prompting (Wei et al., 2022b), have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent upon extensive human-annotated demonstrations, and models' capabilities are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions, and STEM fields, surpassing its counterparts trained via conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically harnessed to guide and enhance the reasoning capabilities of smaller models.\n\n## 1. Introduction\n\nReasoning capability, the cornerstone of human intelligence, enables complex cognitive tasks ranging from mathematical problem-solving to logical deduction and programming. Recent advances in artificial intelligence have demonstrated that large language models (LLMs) can exhibit emergent behaviors, including reasoning abilities, when scaled to a sufficient size (Kaplan et al., 2020; Wei et al., 2022a). However, achieving such capabilities in pre-training typically demands substantial computational resources. In parallel, a complementary line of research has demonstrated that large language models can be effectively augmented through chain-of-thought (CoT) prompting. This technique, which involves either providing carefully designed few-shot examples or using minimalistic prompts such as \"Let's think step by step\" (Kojima et al., 2022; Wei et al., 2022b), enables models to produce intermediate reasoning steps, thereby substantially enhancing their performance on complex tasks. Similarly, further performance gains have been observed when models learn high-quality, multi-step reasoning trajectories during the post-training phase (Chung et al., 2024; OpenAI, 2023). Despite their effectiveness, these approaches exhibit notable limitations. Their dependence on human-annotated reasoning traces hinders scalability and introduces cognitive biases. Furthermore, by constraining models to replicate human thought processes, their performance is inherently capped by the human-provided exemplars, which prevents the exploration of superior, non-human-like reasoning pathways.\n\nTo tackle these issues, we aim to explore the potential of LLMs for developing reasoning abilities through self-evolution in an RL framework, with minimal reliance on human labeling efforts. Specifically, we build upon DeepSeek-V3-Base (DeepSeek-AI, 2024b) and employ Group Relative Policy Optimization (GRPO) (Shao et al., 2024) as our RL framework. The reward signal is solely based on the correctness of final predictions against ground-truth answers, without imposing constraints on the reasoning process itself. Notably, we bypass the conventional supervised fine-tuning (SFT) phase before RL training. This design choice stems from our hypothesis that human-defined reasoning patterns may limit model exploration, whereas unrestricted RL training can better incentivize the emergence of novel reasoning capabilities in LLMs. Through this process, detailed in Section 2, our model (referred to as DeepSeek-R1-Zero) naturally developed diverse and sophisticated reasoning behaviors. In solving reasoning problems, the model exhibits a tendency to generate longer responses, incorporating verification, reflection, and the exploration of alternative approaches within each response. Although we do not explicitly teach the model how to reason, it successfully learns improved reasoning strategies through reinforcement learning.\n\nAlthough DeepSeek-R1-Zero demonstrates excellent reasoning capabilities, it faces challenges such as poor readability and language mixing, occasionally combining English and Chinese within a single chain-of-thought response. Furthermore, the rule-based RL training stage of DeepSeek-R1-Zero is narrowly focused on reasoning tasks, resulting in limited performance in broader areas such as writing and open-domain question answering. To address these challenges, we introduce DeepSeek-R1, a model trained through a multi-stage learning framework that integrates rejection sampling, reinforcement learning, and supervised fine-tuning, detailed in Section 3. This training pipeline enables DeepSeek-R1 to inherit the reasoning capabilities of its predecessor, DeepSeek-R1-Zero, while aligning model behavior with human preferences through additional non-reasoning data.\n\nTo enable broader access to powerful AI at a lower energy cost, we have distilled several smaller models and made them publicly available. These distilled models exhibit strong reasoning capabilities, surpassing the performance of their original instruction-tuned counterparts. We believe that these instruction-tuned versions will also significantly contribute to the research community by providing a valuable resource for understanding the mechanisms underlying long chain-of-thought (CoT) reasoning models and for fostering the development of more powerful reasoning models. We release DeepSeek-R1 series models to the public at &lt;https://huggingface.co/deepseek-ai>.\n\n## 2. DeepSeek-R1-Zero\n\nWe begin by elaborating on the training of DeepSeek-R1-Zero, which relies exclusively on reinforcement learning without supervised fine-tuning. To facilitate large-scale RL efficiency, we adopt Group Relative Policy Optimization (GRPO) (Shao et al., 2024).\n\n### 2.1. Group Relative Policy Optimization\n\nGRPO (Shao et al., 2024) is the reinforcement learning algorithm that we adopt to train DeepSeek-R1-Zero and DeepSeek-R1. It was originally proposed to simplify the training process and reduce the resource consumption of Proximal Policy Optimization (PPO) (Schulman et al., 2017), which is widely used in the RL stage of LLMs (Ouyang et al., 2022).For each question  $q$ , GRPO samples a group of outputs  $\\{o_1, o_2, \\dots, o_G\\}$  from the old policy  $\\pi_{\\theta_{old}}$  and then optimizes the policy model  $\\pi_{\\theta}$  by maximizing the following objective:\n\n$$\\mathcal{J}_{GRPO}(\\theta) = \\mathbb{E}[q \\sim P(Q), \\{o_i\\}_{i=1}^G \\sim \\pi_{\\theta_{old}}(O|q)]$$\n\n$$\\frac{1}{G} \\sum_{i=1}^G \\left( \\min \\left( \\frac{\\pi_{\\theta}(o_i|q)}{\\pi_{\\theta_{old}}(o_i|q)} A_i, \\text{clip} \\left( \\frac{\\pi_{\\theta}(o_i|q)}{\\pi_{\\theta_{old}}(o_i|q)}, 1 - \\varepsilon, 1 + \\varepsilon \\right) A_i \\right) - \\beta \\mathbb{D}_{KL}(\\pi_{\\theta} || \\pi_{ref}) \\right), \\quad (1)$$\n\n$$\\mathbb{D}_{KL}(\\pi_{\\theta} || \\pi_{ref}) = \\frac{\\pi_{ref}(o_i|q)}{\\pi_{\\theta}(o_i|q)} - \\log \\frac{\\pi_{ref}(o_i|q)}{\\pi_{\\theta}(o_i|q)} - 1, \\quad (2)$$\n\nwhere  $\\pi_{ref}$  is a reference policy,  $\\varepsilon$  and  $\\beta$  are hyper-parameters, and  $A_i$  is the advantage, computed using a group of rewards  $\\{r_1, r_2, \\dots, r_G\\}$  corresponding to the outputs within each group:\n\n$$A_i = \\frac{r_i - \\text{mean}(\\{r_1, r_2, \\dots, r_G\\})}{\\text{std}(\\{r_1, r_2, \\dots, r_G\\})}. \\quad (3)$$\n\nWe give a comparison of GRPO and PPO in Supplementary A.3. To train DeepSeek-R1-Zero, we set the learning rate to 3e-6, the KL coefficient to 0.001, and the sampling temperature to 1 for rollout. For each question, we sample 16 outputs with a maximum length of 32,768 tokens before the 8.2k step and 65,536 tokens afterward. As a result, both the performance and response length of DeepSeek-R1-Zero exhibit a significant jump at the 8.2k step, with training continuing for a total of 10,400 steps, corresponding to 1.6 training epochs. Each training step consists of 32 unique questions, resulting in a training batch size of 512. Every 400 steps, we replace the reference model with the latest policy model. To accelerate training, each rollout generates 8,192 outputs, which are randomly split into 16 mini-batches and trained for only a single inner epoch.\n\nTable 1 | Template for DeepSeek-R1-Zero. **prompt** will be replaced with the specific reasoning question during training.\n\n---\n\nA conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user with the answer. The reasoning process and answer are enclosed within `&lt;think>...&lt;/think>` and `&lt;answer>...&lt;/answer>` tags, respectively, i.e., `&lt;think>` reasoning process here `&lt;/think>` `&lt;answer>` answer here `&lt;/answer>`. User: **prompt**. Assistant:\n\n---\n\nOur high-performance RL infrastructure is described in Supplementary B.1, ensuring scalable and efficient training.\n\n## 2.2. Reward Design\n\nThe reward is the source of the training signal, which decides the direction of RL optimization. For DeepSeek-R1-Zero, we employ rule-based rewards to deliver precise feedback for data in mathematical, coding, and logical reasoning domains. Our rule-based reward system mainly consists of two types of rewards: accuracy rewards and format rewards.\n\n**Accuracy rewards** evaluate whether the response is correct. For example, in the case of math problems with deterministic results, the model is required to provide the final answer in a specified format (e.g., within a box), enabling reliable rule-based verification of correctness. Similarly, for code competition prompts, a compiler can be utilized to evaluate the model'sFigure 1 | (a) AIME accuracy of DeepSeek-R1-Zero during training. AIME takes a mathematical problem as input and a number as output, illustrated in Table 32. Pass@1 and Cons@16 are described in Supplementary D.1. The baseline is the average score achieved by human participants in the AIME competition. (b) The average response length of DeepSeek-R1-Zero on the training set during the RL process. DeepSeek-R1-Zero naturally learns to solve reasoning tasks with more thinking time. Note that a training step refers to a single policy update operation.\n\nresponses against a suite of predefined test cases, thereby generating objective feedback on correctness.\n\n**Format rewards** complement the accuracy reward model by enforcing specific formatting requirements. In particular, the model is incentivized to encapsulate its reasoning process within designated tags, specifically ‘`&lt;think>`’ and ‘`&lt;/think>`’. This ensures that the model’s thought process is explicitly delineated, enhancing interpretability and facilitating subsequent analysis.\n\n$$Reward_{rule} = Reward_{acc} + Reward_{format} \\quad (4)$$\n\nThe accuracy, reward and format reward are combined with the same weight. Notably, we abstain from applying neural reward models—whether outcome-based or process-based—to reasoning tasks. This decision is predicated on our observation that neural reward models are susceptible to reward hacking during large-scale reinforcement learning. Moreover, retraining such models necessitates substantial computational resources and introduces additional complexity into the training pipeline, thereby complicating the overall optimization process.\n\n### 2.3. Incentivize Reasoning Capability in LLMs\n\nSpecifically, we apply the RL technique on the DeepSeek-V3 base to train DeepSeek-R1-Zero. During training, we design a straightforward template, to require DeepSeek-R1-Zero to first produce a reasoning process, followed by the final answer. We intentionally limit our constraints to this structural format, avoiding any content-specific biases to ensure that we can accurately observe the model’s natural progression during the RL process.\n\nFigure 1(a) depicts the performance trajectory of DeepSeek-R1-Zero on the AIME 2024 benchmark throughout the RL training process, where the average pass@1 score on AIME 2024 shows a significant increase, jumping from an initial 15.6% to 77.9%. In addition, by leveraging the self-consistency decoding (Wang et al., 2023c), the model’s performance can beTable 2 | An interesting “aha moment” of an intermediate version of DeepSeek-R1-Zero. The model learns to rethink using an anthropomorphic tone. This is also an aha moment for us, allowing us to witness the power and beauty of reinforcement learning.\n\n---\n\n&lt;table border=\"0\" style=\"width: 100%;\">\n&lt;tr>\n&lt;td style=\"width: 5%; vertical-align: top;\">\n&lt;p>Question: If &lt;math>a &gt; 1&lt;/math>, then the sum of the real solutions of &lt;math>\\sqrt{a - \\sqrt{a + x}} = x&lt;/math> is equal to&lt;/p>\n&lt;/td>\n&lt;td style=\"width: 95%; vertical-align: top;\">\n&lt;p>Response: &lt;think&gt;&lt;/p>\n&lt;p>To solve the equation &lt;math>\\sqrt{a - \\sqrt{a + x}} = x&lt;/math>, let’s start by squaring both ...&lt;/p>\n&lt;math display=\"block\">\\left(\\sqrt{a - \\sqrt{a + x}}\\right)^2 = x^2 \\implies a - \\sqrt{a + x} = x^2.&lt;/math>\n&lt;p>Rearrange to isolate the inner square root term:&lt;/p>\n&lt;math display=\"block\">(a - x^2)^2 = a + x \\implies a^2 - 2ax^2 + (x^2)^2 = a + x \\implies x^4 - 2ax^2 - x + (a^2 - a) = 0&lt;/math>\n&lt;p>...&lt;/p>\n&lt;p>&lt;b>Wait, wait. Wait. That’s an aha moment I can flag here.&lt;/b>&lt;/p>\n&lt;p>Let’s reevaluate this step-by-step to identify if the correct sum can be ...&lt;/p>\n&lt;p>We started with the equation:&lt;/p>\n&lt;math display=\"block\">\\sqrt{a - \\sqrt{a + x}} = x&lt;/math>\n&lt;p>First, let’s square both sides:&lt;/p>\n&lt;math display=\"block\">a - \\sqrt{a + x} = x^2 \\implies \\sqrt{a + x} = a - x^2&lt;/math>\n&lt;p>Next, I could square both sides again, treating the equation: ...&lt;/p>\n&lt;p>...&lt;/p>\n&lt;/td>\n&lt;/tr>\n&lt;/table>\n\n---\n\nfurther improved, achieving an accuracy of 86.7%. This performance significantly surpasses the average performance across all human competitors. Besides the math competitions, as shown in Figure 10, DeepSeek-R1-Zero also achieves remarkable performance in coding competitions and graduate-level biology, physics, and chemistry problems. These results underscore the effectiveness of RL in enhancing the reasoning capabilities of large language models.\n\nThe self-evolution of DeepSeek-R1-Zero exemplifies how RL can autonomously enhance a model’s reasoning capabilities.\n\nAs shown in Figure 1(b), DeepSeek-R1-Zero exhibits a steady increase in thinking time throughout training, driven solely by intrinsic adaptation rather than external modifications. Leveraging long CoT, the model progressively refines its reasoning, generating hundreds to thousands of tokens to explore and improve its problem-solving strategies.\n\nThe increase in thinking time fosters the autonomous development of sophisticated behaviors. Specifically, DeepSeek-R1-Zero increasingly exhibits advanced reasoning strategies such as reflective reasoning and systematic exploration of alternative solutions (see Figure 9(a) in Supplementary C.2 for details), significantly boosting its performance on verifiable tasks like math and coding. Notably, during training, DeepSeek-R1-Zero exhibits an “aha moment” (Table 2), characterized by a sudden increase in the use of the word “wait” during reflections (see Figure 9(b) in Supplementary C.2 for details). This moment marks a distinct change in reasoning patterns and clearly shows the self-evolution process of DeepSeek-R1-Zero.\n\nThe self-evolution of DeepSeek-R1-Zero underscores the power and beauty of RL: rather than explicitly teaching the model how to solve a problem, we simply provide it with the right incentives, and it autonomously develops advanced problem-solving strategies. This serves as a reminder of the potential of RL to unlock higher levels of capabilities in LLMs, paving the way for more autonomous and adaptive models in the future.Figure 2 | The multi-stage pipeline of DeepSeek-R1. A detailed background on DeepSeek-V3 Base and DeepSeek-V3 is provided in Supplementary A.1. The models DeepSeek-R1 Dev1, Dev2, and Dev3 represent intermediate checkpoints within this pipeline.\n\n### 3. DeepSeek-R1\n\nAlthough DeepSeek-R1-Zero exhibits strong reasoning capabilities, it faces several issues. DeepSeek-R1-Zero struggles with challenges like poor readability, and language mixing, as DeepSeek-V3-Base is trained on multiple languages, especially English and Chinese. To address these issues, we develop DeepSeek-R1, whose pipeline is illustrated in Figure 2.\n\nIn the initial stage, we collect thousands of cold-start data that exhibits a conversational, human-aligned thinking process. RL training is then applied to improve the model performance with the conversational thinking process and language consistency. Subsequently, we apply rejection sampling and SFT once more. This stage incorporates both reasoning and non-reasoning datasets into the SFT process, enabling the model to not only excel in reasoning tasks but also demonstrate advanced writing capabilities. To further align the model with human preferences, we implement a secondary RL stage designed to enhance the model’s helpfulness and harmlessness while simultaneously refining its reasoning capabilities.\n\nThe remainder of this section details the key components of this pipeline: Section 3.1 introduces the Reward Model utilized in our RL stages, and Section 3.2 elaborates on the specific training methodologies and implementation details. Data we used in this stage is detailed in Supplementary B.3.\n\n#### 3.1. Model-based Rewards\n\nFor general data, we resort to reward models to capture human preferences in complex and nuanced scenarios. We build upon the DeepSeek-V3 pipeline and adopt a similar distribution of preference pairs and training prompts. For helpfulness, we focus exclusively on the final summary, ensuring that the assessment emphasizes the utility and relevance of the response to the user while minimizing interference with the underlying reasoning process. For harmlessness, we evaluate the entire response of the model, including both the reasoning process and the summary, to identify and mitigate any potential risks, biases, or harmful content that may ariseduring the generation process.\n\n**Helpful Reward Model** Regarding helpful reward model training, we first generate preference pairs by prompting DeepSeek-V3 using the arena-hard prompt format, listed in Supplementary B.2, where each pair consists of a user query along with two candidate responses. For each preference pair, we query DeepSeek-V3 four times, randomly assigning the responses as either Response A or Response B to mitigate positional bias. The final preference score is determined by averaging the four independent judgments, retaining only those pairs where the score difference ( $\\Delta$ ) exceeds 1 to ensure meaningful distinctions. Additionally, to minimize length-related biases, we ensure that the chosen and rejected responses of the whole dataset have comparable lengths. In total, we curated 66,000 data pairs for training the reward model. The prompts used in this dataset are all non-reasoning questions and are sourced either from publicly available open-source datasets or from users who have explicitly consented to share their data for the purpose of model improvement. The architecture of our reward model is consistent with that of DeepSeek-R1, with the addition of a reward head designed to predict scalar preference scores.\n\n$$Reward_{\\text{helpful}} = RM_{\\text{helpful}}(Response_A, Response_B) \\quad (5)$$\n\nThe helpful reward models were trained with a batch size of 256, a learning rate of 6e-6, and for a single epoch over the training dataset. The maximum sequence length during training is set to 8192 tokens, whereas no explicit limit is imposed during reward model inference.\n\n**Safety Reward Model** To assess and improve model safety, we curated a dataset of 106,000 prompts with model-generated responses annotated as “safe” or “unsafe” according to predefined safety guidelines. Unlike the pairwise loss employed in the helpfulness reward model, the safety reward model was trained using a point-wise methodology to distinguish between safe and unsafe responses. The training hyperparameters are the same as the helpful reward model.\n\n$$Reward_{\\text{safety}} = RM_{\\text{safety}}(Response) \\quad (6)$$\n\nFor general queries, each instance is categorized as belonging to either the safety dataset or the helpfulness dataset. The general reward,  $Reward_{\\text{General}}$ , assigned to each query corresponds to the respective reward defined within the associated dataset.\n\n### 3.2. Training Details\n\n#### 3.2.1. Training Details of the First RL Stage\n\nIn the first stage of RL, we set the learning rate to 3e-6, the KL coefficient to 0.001, the GRPO clip ratio  $\\epsilon$  to 10, and the sampling temperature to 1 for rollout. For each question, we sample 16 outputs with a maximum length of 32,768. Each training step consists of 32 unique questions, resulting in a training batch size of 512 per step. Every 400 steps, we replace the reference model with the latest policy model. To accelerate training, each rollout generates 8,192 outputs, which are randomly split into 16 minibatches and trained for only a single inner epoch. However, to mitigate the issue of language mixing, we introduce a language consistency reward during RL training, which is calculated as the proportion of target language words in the CoT.\n\n$$Reward_{\\text{language}} = \\frac{\\text{Num}(\\text{Words}_{\\text{target}})}{\\text{Num}(\\text{Words})} \\quad (7)$$Although ablation experiments in Supplementary B.6 show that such alignment results in a slight degradation in the model’s performance, this reward aligns with human preferences, making it more readable. We apply the language consistency reward to both reasoning and non-reasoning data by directly adding it to the final reward.\n\nNote that the clip ratio plays a crucial role in training. A lower value can lead to the truncation of gradients for a significant number of tokens, thereby degrading the model’s performance, while a higher value may cause instability during training.\n\n### 3.2.2. Training Details of the Second RL Stage\n\nSpecifically, we train the model using a combination of reward signals and diverse prompt distributions. For reasoning data, we follow the methodology outlined in DeepSeek-R1-Zero, which employs rule-based rewards to guide learning in mathematical, coding, and logical reasoning domains. During the training process, we observe that CoT often exhibits language mixing, particularly when RL prompts involve multiple languages. For general data, we utilize reward models to guide training. Ultimately, the integration of reward signals with diverse data distributions enables us to develop a model that not only excels in reasoning but also prioritizes helpfulness and harmlessness. Given a batch of data, the reward can be formulated as\n\n$$Reward = Reward_{\\text{reasoning}} + Reward_{\\text{general}} + Reward_{\\text{language}} \\quad (8)$$\n\n$$\\text{where, } Reward_{\\text{reasoning}} = Reward_{\\text{rule}} \\quad (9)$$\n\n$$Reward_{\\text{general}} = Reward_{\\text{reward\\_model}} + Reward_{\\text{format}} \\quad (10)$$\n\nThe second stage of RL retains most of the parameters from the first stage, with the key difference being a reduced temperature of 0.7, as we find that higher temperatures in this stage lead to incoherent generation. The stage comprises a total of 1,700 training steps, during which general instruction data and preference-based rewards are incorporated exclusively in the final 400 steps. We find that more training steps with the model based preference reward signal may lead to reward hacking, which is documented in Supplementary B.5. The total training cost is listed in Supplementary B.4.4.\n\n## 4. Experiment\n\nWe evaluate our models on MMLU (Hendrycks et al., 2021), MMLU-Redux (Gema et al., 2025), MMLU-Pro (Wang et al., 2024), C-Eval (Huang et al., 2023), and CMMLU (Li et al., 2024), IFEval (Zhou et al., 2023b), FRAMES (Krishna et al., 2024), GPQA Diamond (Rein et al., 2023), SimpleQA (OpenAI, 2024a), C-SimpleQA (He et al., 2024), SWE-Bench Verified (OpenAI, 2024b), Aider (Gauthier, 2025), LiveCodeBench (Jain et al., 2024) (2024-08 – 2025-01), Codeforces (Mirzayanov, 2025), Chinese National High School Mathematics Olympiad (CNMO 2024) (CMS, 2024), and American Invitational Mathematics Examination 2024 (AIME 2024) (MAA, 2024). The details of these benchmarks are listed in Supplementary D.\n\nTable 3 summarizes the performance of DeepSeek-R1 across multiple developmental stages, as outlined in Figure 2. A comparison between DeepSeek-R1-Zero and DeepSeek-R1 Dev1 reveals substantial improvements in instruction-following, as evidenced by higher scores on the IF-Eval and ArenaHard benchmarks. However, due to the limited size of the cold-start dataset, Dev1 exhibits a partial degradation in reasoning performance compared to DeepSeek-R1-Zero, most notably on the AIME benchmark. In contrast, DeepSeek-R1 Dev2 demonstratesTable 3 | Experimental results at each stage of DeepSeek-R1. Numbers in bold denote the performance is statistically significant (t-test with  $p < 0.01$ ).\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th colspan=\"2\">Benchmark (Metric)&lt;/th>\n&lt;th>R1-Zero&lt;/th>\n&lt;th>R1-Dev1&lt;/th>\n&lt;th>R1-Dev2&lt;/th>\n&lt;th>R1-Dev3&lt;/th>\n&lt;th>R1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td rowspan=\"10\">English&lt;/td>\n&lt;td>MMLU (EM)&lt;/td>\n&lt;td>88.8&lt;/td>\n&lt;td>89.1&lt;/td>\n&lt;td>&lt;b>91.2&lt;/b>&lt;/td>\n&lt;td>91.0&lt;/td>\n&lt;td>90.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MMLU-Redux (EM)&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>93.0&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>92.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MMLU-Pro (EM)&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>74.1&lt;/td>\n&lt;td>83.8&lt;/td>\n&lt;td>83.1&lt;/td>\n&lt;td>&lt;b>84.0&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DROP (3-shot F1)&lt;/td>\n&lt;td>89.1&lt;/td>\n&lt;td>89.8&lt;/td>\n&lt;td>91.1&lt;/td>\n&lt;td>88.7&lt;/td>\n&lt;td>&lt;b>92.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>IF-Eval (Prompt Strict)&lt;/td>\n&lt;td>46.6&lt;/td>\n&lt;td>71.7&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>&lt;b>83.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPQA Diamond (Pass@1)&lt;/td>\n&lt;td>&lt;b>75.8&lt;/b>&lt;/td>\n&lt;td>66.1&lt;/td>\n&lt;td>70.7&lt;/td>\n&lt;td>71.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>SimpleQA (Correct)&lt;/td>\n&lt;td>30.3&lt;/td>\n&lt;td>17.8&lt;/td>\n&lt;td>28.2&lt;/td>\n&lt;td>24.9&lt;/td>\n&lt;td>30.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>FRAMES (Acc.)&lt;/td>\n&lt;td>82.3&lt;/td>\n&lt;td>78.5&lt;/td>\n&lt;td>81.8&lt;/td>\n&lt;td>81.9&lt;/td>\n&lt;td>&lt;b>82.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AlpacaEval2.0 (LC-winrate)&lt;/td>\n&lt;td>24.7&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;td>62.1&lt;/td>\n&lt;td>&lt;b>87.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>ArenaHard (GPT-4-1106)&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>77.0&lt;/td>\n&lt;td>73.2&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>&lt;b>92.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">Code&lt;/td>\n&lt;td>LiveCodeBench (Pass@1-COT)&lt;/td>\n&lt;td>50.0&lt;/td>\n&lt;td>57.5&lt;/td>\n&lt;td>63.5&lt;/td>\n&lt;td>64.6&lt;/td>\n&lt;td>&lt;b>65.9&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Codeforces (Percentile)&lt;/td>\n&lt;td>80.4&lt;/td>\n&lt;td>84.5&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>92.1&lt;/td>\n&lt;td>&lt;b>96.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Codeforces (Rating)&lt;/td>\n&lt;td>1444&lt;/td>\n&lt;td>1534&lt;/td>\n&lt;td>1687&lt;/td>\n&lt;td>1746&lt;/td>\n&lt;td>&lt;b>2029&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>SWE Verified (Resolved)&lt;/td>\n&lt;td>43.2&lt;/td>\n&lt;td>39.6&lt;/td>\n&lt;td>44.6&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;td>&lt;b>49.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Aider-Polyglot (Acc.)&lt;/td>\n&lt;td>12.2&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;td>25.6&lt;/td>\n&lt;td>44.8&lt;/td>\n&lt;td>&lt;b>53.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Math&lt;/td>\n&lt;td>AIME 2024 (Pass@1)&lt;/td>\n&lt;td>77.9&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>74.0&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>&lt;b>79.8&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MATH-500 (Pass@1)&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>94.2&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>95.4&lt;/td>\n&lt;td>&lt;b>97.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>CNMO 2024 (Pass@1)&lt;/td>\n&lt;td>&lt;b>88.1&lt;/b>&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;td>73.9&lt;/td>\n&lt;td>77.3&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Chinese&lt;/td>\n&lt;td>CLUEWSC (EM)&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>92.8&lt;/td>\n&lt;td>92.6&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>92.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>C-Eval (EM)&lt;/td>\n&lt;td>&lt;b>92.8&lt;/b>&lt;/td>\n&lt;td>85.7&lt;/td>\n&lt;td>91.9&lt;/td>\n&lt;td>86.4&lt;/td>\n&lt;td>91.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>C-SimpleQA (Correct)&lt;/td>\n&lt;td>66.4&lt;/td>\n&lt;td>58.8&lt;/td>\n&lt;td>64.2&lt;/td>\n&lt;td>66.9&lt;/td>\n&lt;td>63.7&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nmarked performance enhancements on benchmarks that require advanced reasoning skills, including those focused on code generation, mathematical problem solving, and STEM-related tasks. Benchmarks targeting general-purpose tasks, such as AlpacaEval 2.0, show marginal improvement. These results suggest that reasoning-oriented RL considerably enhances reasoning capabilities while exerting limited influence on user preference-oriented benchmarks.\n\nDeepSeek-R1 Dev3 integrates both reasoning and non-reasoning datasets into the SFT pipeline, thereby enhancing the model’s proficiency in both reasoning and general language generation tasks. Compared to Dev2, DeepSeek-R1 Dev3 achieves notable performance improvements on AlpacaEval 2.0 and Aider-Polyglot, attributable to the inclusion of large-scale non-reasoning corpora and code engineering datasets. Finally, comprehensive RL training on DeepSeek-R1 Dev3 using mixed reasoning-focused and general-purpose data produced the final DeepSeek-R1. Marginal improvements occurred in code and mathematics benchmarks, as substantial reasoning-specific RL was done in prior stages. The primary advancements in the final DeepSeek-R1 were in general instruction-following and user-preference benchmarks, with AlpacaEval 2.0 improving by 25% and ArenaHard by 17%.\n\nIn addition, we compare DeepSeek-R1 with other models in Supplementary D.2. Model safety evaluations are provided in Supplementary D.3. A comprehensive analysis is provided in Supplementary E, including a comparison with DeepSeek-V3, performance evaluations on both fresh test sets, a breakdown of mathematical capabilities by category, and an investigation of test-time scaling behavior. Supplementary F shows that the strong reasoning capability can be transferred to smaller models.## 5. Ethics and Safety Statement\n\nWith the advancement in the reasoning capabilities of DeepSeek-R1, we deeply recognize the potential ethical risks. For example, R1 can be subject to jailbreak attacks, leading to the generation of dangerous content such as explosive manufacturing plans, while the enhanced reasoning capabilities enable the model to provide plans with better operational feasibility and executability. Besides, a public model is also vulnerable to further fine-tuning that could compromise inherent safety protections.\n\nIn Supplementary D.3, we present a comprehensive safety report from multiple perspectives, including performance on open-source and in-house safety evaluation benchmarks, and safety levels across multiple languages and against jailbreak attacks. These comprehensive safety analyses conclude that the inherent safety level of the DeepSeek-R1 model, compared to other state-of-the-art models, is generally at a moderate level (comparable to GPT-4o (2024-05-13)). Besides, when coupled with the risk control system, the model’s safety level is elevated to a superior standard.\n\n## 6. Conclusion, Limitation, and Future Work\n\nWe present DeepSeek-R1-Zero and DeepSeek-R1, which rely on large-scale RL to incentivize model reasoning behaviors. Our results demonstrate that pre-trained checkpoints inherently possess substantial potential for complex reasoning tasks. We believe that the key to unlocking this potential lies not in large-scale human annotation but in the provision of hard reasoning questions, a reliable verifier, and sufficient computational resources for reinforcement learning. Sophisticated reasoning behaviors, such as self-verification and reflection, appeared to emerge organically during the reinforcement learning process.\n\nEven if DeepSeek-R1 achieves frontier results on reasoning benchmarks, it still faces several capability limitations, as outlined below:\n\n**Structure Output and Tool Use:** Currently, the structural output capabilities of DeepSeek-R1 remain suboptimal compared to existing models. Moreover, DeepSeek-R1 cannot leverage tools, such as search engines and calculators, to improve the performance of output. However, as it is not hard to build an RL environment for structure output and tool use, we believe the issue will be addressed in the next version.\n\n**Token efficiency:** Unlike conventional test-time computation scaling approaches, such as majority voting or Monte Carlo Tree Search (MCTS), DeepSeek-R1 dynamically allocates computational resources during inference according to the complexity of the problem at hand. Specifically, it uses fewer tokens to solve simple tasks, while generating more tokens for complex tasks. Nevertheless, there remains room for further optimization in terms of token efficiency, as instances of excessive reasoning—manifested as overthinking—are still observed in response to simpler questions.\n\n**Language Mixing:** DeepSeek-R1 is currently optimized for Chinese and English, which may result in language mixing issues when handling queries in other languages. For instance, DeepSeek-R1 might use English for reasoning and responses, even if the query is in a language other than English or Chinese. We aim to address this limitation in future updates. The limitation may be related to the base checkpoint, DeepSeek-V3-Base, mainly utilizes Chinese and English, so that it can achieve better results with the two languages in reasoning.\n\n**Prompting Engineering:** When evaluating DeepSeek-R1, we observe that it is sensitive toprompts. Few-shot prompting consistently degrades its performance. Therefore, we recommend users directly describe the problem and specify the output format using a zero-shot setting for optimal results.\n\n**Software Engineering Tasks:** Due to the long evaluation times, which impact the efficiency of the RL process, large-scale RL has not been applied extensively in software engineering tasks. As a result, DeepSeek-R1 has not demonstrated a huge improvement over DeepSeek-V3 on software engineering benchmarks. Future versions will address this by implementing rejection sampling on software engineering data or incorporating asynchronous evaluations during the RL process to improve efficiency.\n\nBeyond specific capability limitations, the pure RL methodology itself also presents inherent challenges:\n\n**Reward Hacking:** The success of pure RL depends on reliable reward signals. In this study, we ensure reward reliability through a reasoning-domain rule-based reward model (RM). However, such dependable RMs are difficult to construct for certain tasks, such as writing. If the reward signal is assigned by a model instead of predefined rules, it becomes more susceptible to exploitation as training progresses, which means the policy model may find shortcuts to hack the reward model. Consequently, for complex tasks that cannot be effectively evaluated by a reliable reward model, scaling up pure RL methods remains an open challenge.\n\nIn this work, for tasks that cannot obtain a reliable signal, DeepSeek-R1 uses human annotation to create supervised data, and only conduct RL for hundreds of steps. We hope in the future, a robust reward model can be obtained to address such issues.\n\nWith the advent of pure RL methods like DeepSeek-R1, the future holds immense potential for solving any task that can be effectively evaluated by a verifier, regardless of its complexity for humans. Machines equipped with such advanced RL techniques are poised to surpass human capabilities in these domains, driven by their ability to optimize performance iteratively through trial and error. However, challenges remain for tasks where constructing a reliable reward model is inherently difficult. In such cases, the lack of a robust feedback mechanism may hinder progress, suggesting that future research should focus on developing innovative approaches to define and refine reward structures for these complex, less verifiable problems.\n\nFurthermore, leveraging tools during the reasoning process holds significant promise. Whether it's utilizing tools like compilers or search engines to retrieve or compute necessary information, or employing external tools—such as biological or chemical reagents, to validate final results in the real world, this integration of tool-augmented reasoning could dramatically enhance the scope and accuracy of machine-driven solutions.\n\n## 7. Author List\n\nThe list of authors is organized by contribution role, with individuals listed alphabetically by their first name within each category. Authors marked with an asterisk (\\*) are no longer affiliated with our team.\n\n**Core Contributors:** Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang, Shirong Ma, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z.F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao,\n\n**Contributions of the Core Authors:** Peiyi Wang and Daya Guo jointly demonstrated that outcome-based RL induces the emergence of long Chain-of-Thought patterns in LLMs, achievingbreakthrough reasoning capabilities. They contributed equally to the creation of R1-Zero, and their work laid the foundation for R1. Daya Guo also contributed to the RL training stability of MOE models. Junxiao Song proposed the GRPO algorithm, implemented the initial version, and introduced rule-based rewards for math tasks. The GRPO algorithm was subsequently refined by Peiyi Wang and Runxin Xu. Zhibin Gou proposed a large PPO clipping strategy to enhance GRPO performance, demonstrating its significance alongside Zhihong Shao and Junxiao Song. Regarding data iteration, reward design, and evaluation, specific teams led efforts across different domains: Qihao Zhu, Z.F. Wu, and Dejian Yang focused on code tasks; Zhihong Shao, Zhibin Gou, and Junxiao Song focused on math tasks; and Peiyi Wang, Ruoyu Zhang, Runxin Xu, and Yu Wu led efforts for other reasoning and general tasks. Additionally, Qihao Zhu and Zhihong Shao contributed to the data selection strategy for RL training, while Zhuoshu Li and Yu Wu co-led the data labeling efforts for the entire project. On the system side, Xiao Bi, Xingkai Yu, Shirong Ma, Xiaokang Zhang, Haowei Zhang, and Ziyi Gao implemented the RL pipeline, optimizing system efficiency and addressing stability issues in large-scale training. Finally, Zhibin Gou, Daya Guo, and Ruoyu Zhang oversaw the final training phase and monitored the model training dynamics. Zhibin Gou led the development of the R1-distill series.\n\n**Contributors:** Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo\\*, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Hanwei Xu, Honghui Ding, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jingchang Chen, Jingyang Yuan, Jinhao Tu, Junjie Qiu, Junlong Li, J.L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu\\*, Kaichao You, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Mingxu Zhou, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R.J. Chen, R.L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S.S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu\\*, Wentao Zhang, W.L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X.Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y.K. Li, Y.Q. Wang, Y.X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma\\*, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y.X. Zhu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z.Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu\\*, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, Zhen Zhang,## Appendix\n\n### A. Background\n\n#### A.1. DeepSeek-V3\n\nDeepSeek V3 (DeepSeek-AI, 2024b) is an advanced open-source LLM developed by DeepSeek. Released in December 2024, DeepSeek V3 represents a significant leap forward in AI innovation, designed to rival leading models like OpenAI’s GPT-4 and Meta’s Llama 3.1, while maintaining remarkable cost efficiency and performance. Built on a Mixture-of-Experts (MoE) architecture, DeepSeek V3 has 671 billion total parameters, with 37 billion activated per token, optimizing both efficiency and capability. It was pre-trained on an expansive dataset of 14.8 trillion high-quality, diverse tokens, followed by supervised fine-tuning and reinforcement learning to enhance its abilities across various domains. The model incorporates innovative features like Multi-head Latent Attention (MLA) (DeepSeek-AI, 2024a) for efficient inference, an auxiliary-loss-free load-balancing strategy, and Multi-Token Prediction (MTP) (Gloeckle et al., 2024) to boost performance, particularly in tasks like mathematics and coding.\n\nFor the training data of DeepSeek-V3-Base, we exclusively use plain web pages and e-books, without incorporating any synthetic data. However, we have observed that some web pages contain a significant number of OpenAI-model-generated answers, which may lead the base model to acquire knowledge from other powerful models indirectly. However, we did not intentionally include synthetic data generated by OpenAI during the pre-training cooldown phase; all data used in this phase were naturally occurring and collected through web crawling. The pre-training dataset contains a substantial amount of mathematical and code-related content, indicating that DeepSeek-V3-Base has been exposed to a significant volume of reasoning trace data. This extensive exposure equips the model with the capability to generate plausible solution candidates, from which reinforcement learning can effectively identify and optimize high-quality outputs. We did the data contamination in pre-training as described in Appendix D.1. The training data of DeepSeek-V3 base are mostly Chinese and English, which might be the cause for DeepSeek-R1-Zero language mixing when the language consistent reward is absent.\n\nIn this paper, we use the notation DeepSeek-V3-Base as the base model, DeepSeek-V3 as the instructed model. Notably, DeepSeek-R1 and DeepSeek-R1-Zero are trained on top of DeepSeek-V3-Base and DeepSeek-R1 leverages non-reasoning data from DeepSeek-V3 SFT data. DeepSeek-R1-Dev1, DeepSeek-R1-Dev2, DeepSeek-R1-Dev3 are intermediate checkpoints of DeepSeek-R1.\n\n#### A.2. Conventional Post-Training Paradigm\n\nPost-training has emerged as an essential step in refining pre-trained LLMs to meet specific performance goals and align with human expectations. A widely adopted two-stage post-training framework is SFT followed by RL (Ouyang et al., 2022).\n\nSupervised Fine-Tuning refines a pre-trained LLM by training it on a curated dataset of input-output pairs tailored to specific tasks. The process employs a supervised learning objective, typically minimizing cross-entropy loss between the model’s predictions and labeled ground truth (Brown et al., 2020). For instance, in conversational applications, SFT might utilize dialogue datasets where desired responses are explicitly provided, enabling the model to adapt its outputs to predefined standards (Radford et al., 2019). SFT offers several compelling benefits. First, it achieves precise task alignment by leveraging high-quality examples, allowing the model toexcel in domains such as customer support or technical documentation (Radford et al., 2019). Second, its reliance on pre-trained weights ensures computational efficiency, requiring fewer resources than training from scratch. Finally, the use of explicit input-output mappings enhances interpretability, as the model’s learning process is directly tied to observable data, minimizing the risk of erratic behavior (Ouyang et al., 2022). Despite its strengths, the performance of SFT hinges on the quality and diversity of the training dataset; narrow or biased data can impair the model’s ability to generalize to novel contexts (Brown et al., 2020). Additionally, SFT’s static nature—optimizing for fixed outputs—may fail to capture evolving human preferences or nuanced objectives. The labor-intensive process of curating high-quality datasets further complicates its scalability, as errors or inconsistencies in the data can propagate into the model’s behavior (Ouyang et al., 2022).\n\nFollowing SFT, Reinforcement Learning further refines the LLM by optimizing its outputs against a reward signal. In this stage, the model interacts with an environment—often a reward model trained on human feedback—and adjusts its behavior to maximize cumulative rewards. A prominent instantiation of this approach is Reinforcement Learning from Human Feedback (RLHF), where the reward function encodes human preferences (Christiano et al., 2017). RL thus shifts the focus from static supervision to dynamic optimization. Notably, RL reduces the need for extensive annotated resources; while SFT demands a fully labeled dataset for every input-output pair, RL can operate with a smaller set of human evaluations or a trained reward model, even rule-based reward model, significantly lowering the annotation burden.\n\nThe sequential application of SFT and RL combines their complementary strengths. SFT establishes a robust, task-specific baseline by grounding the model in curated examples, while RL refines this foundation to align with broader, human-centric objectives (Ouyang et al., 2022). For example, SFT might ensure grammatical accuracy in a dialogue system, while RL optimizes for engagement and brevity, as demonstrated in the development of InstructGPT (Ouyang et al., 2022). This hybrid approach has proven effective in producing models that are both precise and adaptable.\n\nIn this study, we demonstrate that the SFT stage may impede a model’s ability to explore and develop effective reasoning strategies. This limitation arises because human-provided responses, which serve as targets during SFT, are not always optimal for model learning; they often omit critical reasoning components such as explicit reflection and verification steps. To address this, DeepSeek-R1-Zero enables direct exploration of reasoning patterns by the model itself, independent of human priors. The reasoning trajectories discovered through this self-exploration are subsequently distilled and used to train other models, thereby promoting the acquisition of more robust and generalizable reasoning capabilities.\n\n### A.3. A Comparison of GRPO and PPO\n\nGroup Relative Policy Optimization (GRPO) (Shao et al., 2024) is the reinforcement learning algorithm that we adopt to train DeepSeek-R1-Zero and DeepSeek-R1. It was originally proposed to simplify the training process and reduce the resource consumption of Proximal Policy Optimization (PPO) (Schulman et al., 2017), which is widely used in the RL stage of LLMs (Ouyang et al., 2022). For an overall comparison between GRPO and PPO, see Figure 3.\n\nFor each question  $q$ , GRPO samples a group of outputs  $\\{o_1, o_2, \\dots, o_G\\}$  from the old policyFigure 3 | Demonstration of PPO and our GRPO. GRPO foregoes the value model, instead estimating the advantages from group scores.\n\n$\\pi_{\\theta_{old}}$  and then optimizes the policy model  $\\pi_{\\theta}$  by maximizing the following objective:\n\n$$\\mathcal{J}_{GRPO}(\\theta) = \\mathbb{E}[q \\sim P(Q), \\{o_i\\}_{i=1}^G \\sim \\pi_{\\theta_{old}}(O|q)] \\frac{1}{G} \\sum_{i=1}^G \\left( \\min \\left( \\frac{\\pi_{\\theta}(o_i|q)}{\\pi_{\\theta_{old}}(o_i|q)} A_i, \\text{clip} \\left( \\frac{\\pi_{\\theta}(o_i|q)}{\\pi_{\\theta_{old}}(o_i|q)}, 1 - \\varepsilon, 1 + \\varepsilon \\right) A_i \\right) - \\beta \\mathbb{D}_{KL}(\\pi_{\\theta} || \\pi_{ref}) \\right), \\quad (11)$$\n\n$$\\mathbb{D}_{KL}(\\pi_{\\theta} || \\pi_{ref}) = \\frac{\\pi_{ref}(o_i|q)}{\\pi_{\\theta}(o_i|q)} - \\log \\frac{\\pi_{ref}(o_i|q)}{\\pi_{\\theta}(o_i|q)} - 1, \\quad (12)$$\n\nwhere  $\\pi_{ref}$  is a reference policy,  $\\varepsilon$  and  $\\beta$  are hyper-parameters, and  $A_i$  is the advantage, computed using a group of rewards  $\\{r_1, r_2, \\dots, r_G\\}$  corresponding to the outputs within each group:\n\n$$A_i = \\frac{r_i - \\text{mean}(\\{r_1, r_2, \\dots, r_G\\})}{\\text{std}(\\{r_1, r_2, \\dots, r_G\\})}. \\quad (13)$$\n\nIn contrast, in PPO, the advantage is typically computed by applying the Generalized Advantage Estimation (GAE) (Schulman et al., 2015), based not only on the rewards but also on a learned value model. Since the value model is usually of similar size as the policy model, it introduces a significant memory and computational overhead. Additionally, the training objective of the value model is to predict the expected cumulative reward from the current position onward, based on the tokens generated from the beginning up to the current position. This is inherently difficult, especially when only the final outcome reward is available. The challenge becomes even more pronounced when training long chain-of-thought reasoning models. As the output length increases, the model is more likely to engage in behaviors such as reflection and revision during generation, meaning that the content initially generated may later be revised or contradicted, which makes it even less feasible to predict the final reward based on a partial response.\n\nAnother key difference between GRPO and PPO is how Kullback–Leibler (KL) divergence between the trained policy and the reference policy is incorporated into the training process. In GRPO, an unbiased estimator of the KL divergence (Schulman, 2020) is directly added in the loss as in equation 11, while in PPO the per-token KL penalty is added as a dense reward at each token (Ouyang et al., 2022). Since the optimization goal of reinforcement learning is toFigure 4 | Performance of PPO and GRPO on the MATH task.\n\nmaximize cumulative rewards, PPO’s approach penalizes the cumulative KL divergence, which may implicitly penalize the length of the response and thereby prevent the model’s response length from increasing. In addition, as we may train thousands of steps in the scenario of training long chain-of-thought reasoning models, the trained policy can diverge significantly from the initial reference policy. In order to balance the scope that the training policy can explore and the stability of the training, we periodically update the reference policy to the latest policy during the actual training process.\n\nFigure 4 compares the performance of PPO and GRPO on the MATH task using DeepSeek-Coder-V2-Lite (16B MoE with 2.4B active parameters). Unlike GRPO, PPO requires additional hyperparameter tuning—particularly of the  $\\lambda$  coefficient in GAE—and is highly sensitive to this parameter. When  $\\lambda$  is set to 0.95 (the default value in most open-source PPO implementations), PPO performs considerably worse than GRPO. However, with careful tuning (setting  $\\lambda$  to 1.0), PPO’s performance improves substantially, nearing that of GRPO.\n\nWhile PPO can achieve comparable performance when appropriately tuned, it demands additional computational cost for hyperparameter optimization. Moreover, considering the memory and computational overhead associated with training an additional value model, GRPO presents a more practical alternative, especially when training large-scale models with constrained resources.Figure 5 | Overview of our RL framework.\n\n## B. Training Details\n\n### B.1. RL Infrastructure\n\nConducting RL training on large models places high demands on the infrastructure. Our RL framework is architected with a decoupled and extensible structure to facilitate seamless integration of diverse models and algorithms. Within this framework, we have incorporated both intra-modular and inter-modular optimization techniques, to ensure training efficiency and scalability.\n\nSpecifically, as depicted in Figure 5, the framework is partitioned into four distinct modules, each corresponding to a specific phase of the RL pipeline:\n\n- • **Rollout Module:** Prompts are loaded from training dataset and uniformly dispatched across multiple vLLM (Kwon et al., 2023) workers, each equipped with the actor model, to sample multiple responses. For DeepSeek-V3 MoE architecture, we implement an expert parallelism strategy across nodes to reduce memory access overhead, and deploy redundant copies of hotspot experts to balance computational loads among different experts. Multi-Token Prediction (MTP) component is also leveraged for self-speculative decoding, significantly accelerating the decoding speed and effectively minimizing the completion time for the longest samples.\n- • **Inference Module:** This module loads the reward model and reference to perform a forward pass on the samples generated during the rollout phase, thereby obtaining model-based rewards and other essential information.\n- • **Rule-based Reward Module:** This module computes rule-based rewards for the model-generated responses. A unified interface has been designed to accommodate diverse implementations (e.g., code executor, answer matcher, format checker, etc.). Although this module does not require loading models into GPU memory, its execution tends to be time-consuming. To tackle this issue, an asynchronous scheduling approach is employed to overlap its execution with the Rollout and Inference modules, effectively hiding theassociated latency.\n\n- • **Training Module:** This module loads the actor model and the critic model (if required), to compute loss and update model parameters. It provides flexible support for a variety of RL algorithms (e.g., PPO, GRPO, DPO, etc.). To minimize computational waste caused by sequence padding and balance the workload across devices, we design the following data packing strategy: first, all data in a global batch is sorted by length and distributed across processes within the data parallel group; subsequently, within each process, the Best-Fit strategy is applied to pack the data into fixed-length chunks with minimal padding; finally, the number of chunks is adjusted to be equal across all processes. Additionally, we have integrated the DualPipe algorithm, utilized in DeepSeek-V3 training, to achieve efficient pipeline parallelism.\n\nNotably, upon completion of each module (excluding the Rule-based Reward module), the model instances utilized in that phase are automatically offloaded from VRAM to either system memory or disk storage, thereby freeing up VRAM for the subsequent phase.\n\n## B.2. Reward Model Prompt\n\nPlease act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user prompt displayed below. You will be given assistant A's answer and assistant B's answer. Your job is to evaluate which assistant's answer is better. Begin your evaluation by generating your own answer to the prompt. You must provide your answers before judging any answers.\n\nWhen evaluating the assistants' answers, compare both assistants' answers with your answer. You must identify and correct any mistakes or inaccurate information.\n\nThen consider if the assistant's answers are helpful, relevant, and concise. Helpful means the answer correctly responds to the prompt or follows the instructions. Note when user prompt has any ambiguity or more than one interpretation, it is more helpful and appropriate to ask for clarifications or more information from the user than providing an answer based on assumptions. Relevant means all parts of the response closely connect or are appropriate to what is being asked. Concise means the response is clear and not verbose or excessive.\n\nThen consider the creativity and novelty of the assistant's answers when needed. Finally, identify any missing important information in the assistants' answers that would be beneficial to include when responding to the user prompt.\n\nAfter providing your explanation, you must output only one of the following choices as your final verdict with a label:\n\n1. 1. Assistant A is significantly better: [[A>>B]]\n2. 2. Assistant A is slightly better: [[A>B]]\n3. 3. Tie, relatively the same: [[A=B]]\n4. 4. Assistant B is slightly better: [[B>A]]\n5. 5. Assistant B is significantly better: [[B>>A]]\n\nExample output: My final verdict is tie: [[A=B]]:Table 4 | Description of RL Data and Tasks.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Data Type&lt;/th>\n&lt;th># Prompts&lt;/th>\n&lt;th>Question Type&lt;/th>\n&lt;th>Output Type&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Math&lt;/td>\n&lt;td>26K&lt;/td>\n&lt;td>Quantitative Reasoning&lt;/td>\n&lt;td>Number/Expression/Equation&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Code&lt;/td>\n&lt;td>17K&lt;/td>\n&lt;td>Algorithm and Bug Fixing&lt;/td>\n&lt;td>Code Solution&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>STEM&lt;/td>\n&lt;td>22K&lt;/td>\n&lt;td>Multi-Choice&lt;/td>\n&lt;td>Option&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Logic&lt;/td>\n&lt;td>15K&lt;/td>\n&lt;td>Choice/Quantitative Reasoning&lt;/td>\n&lt;td>Option/Number&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>General&lt;/td>\n&lt;td>66K&lt;/td>\n&lt;td>Helpfulness/Harmlessness&lt;/td>\n&lt;td>Ranked Responses&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n### B.3. Data Recipe\n\n#### B.3.1. RL Data\n\nReasoning RL data includes four categories: mathematics, coding, STEM, and logic problems. In addition, we also incorporate general RL data to improve the helpfulness and harmlessness of the model in the training of DeepSeek-R1. All questions are in Chinese or English. The description of the RL data can be found in Table 4, where we will describe the details of each data type one by one as follows:\n\n- • **Mathematics** dataset consists of 26k quantitative reasoning questions, including math exam questions and competition problems. The average number of prompt tokens is 122. The dataset covers various mathematical domains such as algebra, calculus, probability, and geometry. Problems range in difficulty from regional contests to international Olympiads. For each problem, the model is expected to produce a step-by-step reasoning process culminating in a final answer, which can be a numerical value (e.g., \"5\"), a mathematical expression (e.g., \" $x^2 + 3x - 2$ \"), or an equation (e.g., \" $y = 2x + 1$ \"). Mathematical proofs are excluded because it is difficult to determine their correctness. For reinforcement learning purposes, we calculate the reward of a reasoning process by matching the predicted answer with the reference answer. If the answer aligns with the reference, the reward is assigned a value of 1; otherwise, it is assigned a value of 0.\n- • **Coding** dataset includes 17k algorithm competition questions, along with 8k bug fixing problems. The algorithm competition questions are similar to problems found on platforms like Codeforces or LeetCode. Each problem typically includes a detailed problem description, constraints, and multiple input-output examples. The task is to write a complete function or program that can solve the problem correctly and efficiently, passing a comprehensive set of hidden test cases that assess both correctness and performance. These problems test algorithmic skills, including dynamic programming, graph theory, string manipulation, and data structure usage. The bug-fixing problems are extracted from real-world GitHub issues. Each task provides an issue description, a buggy version of the source code, and a set of unit tests that partially or completely fail. The goal is to understand the intent of the issue, locate and fix the defect in the code, and ensure that the corrected version passes all unit tests.\n- • **STEM** dataset comprises 22k choice questions that cover topics such as physics, chemistry, and biology. Each question in the STEM task presents a subject-specific problem accompanied by four to eight answer options. The model is required to select the most scientifically accurate answer based on the given context and domain knowledge. The average number of prompt tokens is 161. Specifically, the dataset includes 15.5% physics, 30.7% biology, 46.5% chemistry, and 7.3% other topics such as health and medicine. Since all STEM questions are multiple-choice, a binary reward is assigned based on whether thecorrect option is matched.\n\n- • **Logic** dataset contains 15k questions designed to evaluate a model’s reasoning capabilities across a broad spectrum of logical challenges. The dataset includes both real-world and synthetically generated problems. All problems support automatic evaluation, and the average prompt length is approximately 420 tokens. The real-world portion of the dataset comprises a diverse selection of problems sourced from the web, including brain teasers, classical logic puzzles, and knowledge-intensive questions. These questions are presented in a multiple-choice format to ensure objective and consistent assessment. The synthetic portion consists primarily of two categories: code-IO problems and puzzle tasks. Code-IO problems are generated using the data pipeline introduced by Li et al. (2025), which converts competitive coding problems and their corresponding input-output test cases into verifiable logical reasoning problems. The puzzle tasks include problems intended to assess specific reasoning competencies. For example, cryptography puzzles are designed to evaluate a model’s ability to identify and apply patterns in cipher schemes or perform string manipulations; logic puzzles focus on deductive reasoning over complex constraints, such as inferring valid conclusions from a fixed set of premises (e.g., the Zebra puzzle); and arithmetic puzzles test the model’s numerical reasoning (e.g. probability questions and 24 game).\n- • **General** dataset consists of 66k questions designed to assess helpfulness, spanning various categories such as creative writing, editing, factual question answering, and role-playing. Additionally, the dataset includes 12,000 questions focused on evaluating harmlessness. To ensure robust verification, two reward models are utilized, each trained on a curated dataset of ranked responses generated by models in relation to helpfulness and harmlessness, respectively. We trained the helpful reward model for a single epoch with a maximum sequence length of 8192 tokens during the training phase. However, when deploying the model to generate reward signals, we did not impose any explicit length constraints on the input sequences being evaluated.\n\n### **B.3.2. DeepSeek-R1 Cold Start**\n\nFor DeepSeek-R1, we construct and collect a small amount of long CoT data to fine-tune the model as the initial RL actor. The motivation is primarily product-driven, with a strong emphasis on enhancing user experience. Users tend to find responses more intuitive and engaging when the reasoning process aligns with first-person perspective thought patterns. For example, DeepSeek-R1-Zero is more likely to employ the pronoun ‘we’ or avoid first-person pronouns altogether during problem solving, whereas DeepSeek-R1 tends to use ‘I’ more frequently. Furthermore, we acknowledge that such patterns may elicit unwarranted trust from users. Here, we would like to emphasize that the observed vivid reasoning patterns primarily reflect DeepSeek-engineered heuristics, rather than indicating that the model has inherently acquired human-like intelligence or autonomous problem-solving capabilities.\n\nIn cold start data creation, we prefer the thinking process that begins with comprehending the problem, followed by detailed reasoning that incorporates reflection and verification. The language employed throughout the thinking process is presented in the first-person perspective. Additionally, maintaining language consistency is crucial for an optimal user experience. Without proper control, model responses may contain a mixture of different languages, regardless of the language used in the query. Such inconsistencies can disrupt comprehension and reduce user satisfaction. Therefore, careful refinement is essential to ensure that responses remain coherent and aligned with user intent. Nevertheless, we acknowledge that the raw Chain-of-Thought (CoT) reasoning produced by DeepSeek-R1-Zero may possess potential that extends beyond thelimitations of current human priors. Specifically, we first engage human annotators to convert the reasoning trace into a more natural, human conversational style. The modified data pairs are then used as examples to prompt an LLM to rewrite additional data in a similar style. All LLM-generated outputs subsequently undergo a second round of human verification to ensure quality and consistency.\n\nListing 1 | Prompt for producing a human-readable solution.\n\n```\n## Question\n{question}\n\n## Thought process\n{thought_process}\n\n---\nBased on the above thought process, provide a clear, easy-to-follow, and well-formatted solution to the question. Use the same language as the question.\n\nThe solution must strictly follow these requirements:\n- Stay faithful and consistent with the given thought process. Do not add new reasoning steps or conclusions not shown in the original.\n- Show key steps leading to final answer(s) in clear, well-formatted LaTeX.\n- Use \\boxed{} for final answer(s).\n- Be clean and concise. Avoid colloquial language. Do not use phrases like \"thought process\" in the solution.\n\nYour response should start with the solution right away, and do not include anything else. Your task is solely to write the solution based on the provided thought process. Do not try to solve the question yourself.\n```\n\nSpecifically, we begin by gathering thousands of high-quality, diverse reasoning prompts. For each prompt, we generate multiple reasoning trajectories using DeepSeek-R1-Zero with a relatively high temperature of 1.0. Next, we filter these generations to retain only those with correct final answers and a readable format. For mathematical outputs, we use sympy (&lt;https://www.sympy.org/>) for parsing and expression comparison; and for formatting, we apply rules such as repetition detection and language-mixing filtering. Finally, we prompt DeepSeek-V3 to refine both the reasoning and the summaries to ensure proper formatting and a human-friendly expression. In particular, to resolve language mixing, we instruct DeepSeek-V3 to “Translate the thinking process to the same language as the question.” Since DeepSeek-R1-Zero’s summary only provided the final answer, we use the summary prompt in Listing 1 to produce a concise, human-readable solution that outlines both the reasoning steps and the final result.\n\nFor code data, we collect a large set of competitive programming problems. In detail, We have compiled an extensive collection of competitive programming problems from multiple online judge (OJ) platforms, specifically 5151 problems from Codeforces and 2504 problems from AtCoder. Since the original test cases are not publicly available from these platforms, we developed a methodology to create reliable test cases for each problem.\n\nOur approach involves using DeepSeek-V2.5 to generate candidate test cases, followed by a rigorous validation process. Specifically, we prompted DeepSeek-V2.5 to write Python programs that generate test cases tailored to each problem’s requirements as shown in Listing 2.\n\nAfter obtaining numerous candidate test cases, we implemented a two-phase filtering procedure. First, we used correct submissions to eliminate invalid test cases that produced incorrect outputs. Then, we strategically selected subsets of test cases that successfully identifiedflaws in incorrect submissions. This process ensured our final test cases properly differentiated between correct and incorrect solutions for each problem.\n\n#### Listing 2 | Prompt for generating test cases for code problem.\n\n```\n&lt;USER>\nQuestion:\nYou are given a string word and an integer k.\n\nA substring s of word is complete if:\n\nEach character in s occurs exactly k times.\nThe difference between two adjacent characters is at most 2. That is, for any two\nadjacent characters c1 and c2 in s, the absolute difference in their positions in\nthe alphabet is at most 2.\nReturn the number of complete substrings of word.\n\nA substring is a non-empty contiguous sequence of characters in a string.\n\n**Input**\nThe first line contains a single integer t the number of test cases.\nThe first line of each test case contain one string word.\nThe second line of each test case contain one integer k.\nIt is guaranteed that word consists only of lowercase English letters, and the sum of |\nword| over all test cases does not exceed 10^5.\n\n**Output**\nFor each test case, print one integer the number of complete substrings of word.\n\n**Example**\nInput\n'''\n2\nigigee\n2\naaabbccc\n3\n'''\n\nOutput\n'''\n3\n6\n'''\n\nConstruct some random input generators to generate diverse and adversarial inputs,\nwhich are large enough to to make incorrect codes exceed the time limit.\n&lt;/USER>\n\n&lt;ASSISTANT>\nFirst construct a random input generator for large data with 10 testcases of the same\nlength.\n\n'''python\nimport random\nimport string\n\ndef generate_random_string(l_min, l_max):\n    length = random.randint(l_min, l_max)\n    seq = ''.join(random.choices(string.ascii_lowercase, k=length))\n    k = random.randint(1, length)\n``````\n\n    return f\"{{seq}}\\n{{k}}\"\n\nt = 10 # the number of test cases\ntestcase = [generate_random_string(10000, 10000) for _ in range(t)]\n\nprint(t)\nprint(\"\\n\".join(testcase))\n'''\n\nFirst construct a random input generator for large data with 10 testcases of different\nlength.\n\n'''python\nimport random\nimport string\n\ndef generate_random_string(l_min, l_max):\n    length = random.randint(l_min, l_max)\n    seq = ''.join(random.choices(string.ascii_lowercase, k=length))\n    k = random.randint(1, length)\n    return f\"{{seq}}\\n{{k}}\"\n\nt = 10 # the number of test cases\ntestcase = []\ncum_length = 0\nfor i in range(t):\n    # each test case should have length >= 1\n    cur_testcase, cur_length = generate_random_string(1, 100000 - cum_length - (t -\n        i))\n    testcase.append(cur_testcase)\n    cum_length += cur_length\n\nprint(t)\nprint(\"\\n\".join(testcase))\n'''\n\nConstruct a random input generator for large data with only one test case.\n\n'''python\nimport random\nimport string\n\ndef generate_random_string(l_min, l_max):\n    ...\n\nt = 1 # the number of test cases\ntestcase = [generate_random_string(90000, 100000) for _ in range(t)]\n\nprint(t)\nprint(\"\\n\".join(testcase))\n'''\n\nConstruct an input generator for large adversarial inputs of a string of a repeated\nsingle character.\n\n'''python\nimport random\nimport string\n\ndef generate_single_repeated_char(l_min, l_max):\n    length = random.randint(l_min, l_max)\n\n``````\nchar = random.choice(string.ascii_lowercase)\nseq = char * length\nk = random.randint(1, length)\nreturn f\"{{seq}}\\n{{k}}\"\n\nt = 1 # the number of test cases\ntestcase = [generate_single_repeated_char(90000, 100000) for _ in range(t)]\n\nprint(t)\nprint(\"\\n\".join(testcase))\n'''\n```\n\nConstruct an input generator for large adversarial inputs of a string of two alternating characters.\n\n```\n'''python\nimport random\nimport string\n\ndef generate_alternating_chars(l_min, l_max):\n    length = random.randint(l_min, l_max)\n    char1, char2 = random.sample(string.ascii_lowercase, 2)\n    seq = ''.join(char1 if i % 2 == 0 else char2 for i in range(length))\n    k = random.randint(1, length)\n    return f\"{{seq}}\\n{{k}}\"\n\nt = 1 # the number of test cases\ntestcase = [generate_alternating_chars(90000, 100000) for _ in range(t)]\n\nprint(t)\nprint(\"\\n\".join(testcase))\n'''\n```\n\nConstruct an input generator for large adversarial inputs of a string of sequential characters from alphabet.\n\n```\n'''python\n...\n'''\n```\n\n&lt;/ASSISTANT>\n\nQuestion:\n\nQuestion Description\n\nConstruct some random input generators to generate large, diverse and adversarial inputs, which are large enough to testing time complexity and to make incorrect codes exceed the time limit.\n\nUse the format used in the above example by returning several input generators in different code blocks. Each of these generators prints EXACTLY ONE input directly into stdout.\n\nIn addition, we employ few-shot prompting for DeepSeek-V3 to generate responses to simple math problems, such as \"1 + 1 = ?\", ensuring that the outputs remain concise and appropriately structured. We provide the prompt for a simple math problem in Listing 3.\n\nListing 3 | Prompt for generating chain-of-thought for simple math problem.\n\n```\n## Question\nHow much is 5+4?\n``````\n## Response\n&lt;think>\n```\n\nI need to add the numbers 5 and 4. Starting with 5, if I add 4 to it, the total will be 9. Therefore, the sum of 5 and 4 is 9.\n\n```\n&lt;/think>\n```\n\n```\n**Solution:**\n```\n\nWe are asked to calculate the sum of 5 and 4.\n\n```\n**Step 1:** Start with the number 5.\n```\n\n```\n**Step 2:** Add 4 to it.\n```\n\n```\n\\[\n5 + 4 = 9\n\\]\n```\n\n```\n**Final Answer:** \\(\\boxed{9}\\)\n```\n\n```\n---\n```\n\n```\n## Question\nwhat is 1 plus 2\n```\n\n```\n## Response\n&lt;think>\n```\n\nI need to determine the sum of 1 and 2.\n\nAdding these two numbers together, 1 plus 2 equals 3.\n\nTherefore, the answer is 3.\n\n```\n&lt;/think>\n```\n\nSure! Let's solve the problem step by step.\n\n```\n**Problem:** What is  $(1 + 2)$ ?\n```\n\n```\n**Solution:**\n```\n\nTo find the sum of 1 and 2, simply add the two numbers together:\n\n```\n\\[\n1 + 2 = 3\n\\]\n```\n\n```\n**Answer:**\n```\n\n```\n\\(\\boxed{3}\\)\n```\n\n```\n---\n```\n\n```\n## Question\n{question}\n```\n\n```\n## Response\n```#### Listing 4 | An example prompt of using DeepSeek-V3 as a judge.\n\n```\nAs an advanced reasoning problem evaluation assistant, your primary responsibility is to assess the accuracy of provided answers. You will be presented with a reasoning-related question, its corresponding reference answer, and an answer requiring evaluation.\n\n## Answer Quality Classification\nYou have to carefully analyze and classify the answer into one of the following two levels:\n1. correct: The answer fully aligns with the reference answer in both reasoning process and final conclusion, and address the question without any errors or omissions.\n2. incorrect: The answer contains major errors in key reasoning steps or the final conclusion, or completely deviates from the core of the question. This indicates a fundamental misunderstanding or error in comprehending the question.\n\n## Question\n{question}\n\n## Reference Answer\n{reference}\n\n## Answer to be Evaluated\n{answer}\n\n## Output Format\nYou need to combine the question and reference answer, first provide a detailed explanation of your analysis of the answer to be evaluated, then conclude with the final answer quality classification.\nOutput the following content in JSON format, including two key:\n1. 'analysis': analysis of the answer's correctness;\n2. 'correctness': correct/incorrect\n```\n\n### B.3.3. 800K Supervised Data\n\n**Reasoning Data** We curate a large set of reasoning prompts and generate reasoning trajectories by performing rejection sampling from the checkpoint of the first-stage RL training. In the previous stage, we only included data that could be evaluated using rule-based rewards. However, in this stage, we expand the dataset by incorporating additional data, some of which uses a generative reward model by feeding the ground-truth and model predictions into DeepSeek-V3 for judgment, an example prompt is provided in Listing 4. Additionally, because the model output is sometimes chaotic and difficult to read, we have filtered out chain-of-thought with mixed languages, long paragraphs, and code blocks. For each prompt, we sample multiple responses and retain only the correct ones. In total, we collect about 600k reasoning-related training samples.\n\n**Non-Reasoning Data** For non-reasoning data, such as writing, factual QA, self-cognition, and translation, we adopt the DeepSeek-V3 pipeline and reuse portions of the SFT dataset of DeepSeek-V3. We also incorporate software engineering-focused data, including program repair and front-end web development, to enhance the model's ability to solve real-world problems. For certain non-reasoning tasks, we call DeepSeek-V3 to generate a potential chain-of-thought before answering the question by prompting. However, for simpler queries, such as \"hello\" we do not provide a CoT in response. In the end, we collected a total of approximately 200k training samples that are unrelated to reasoning.When designing our thinking process style, we ask the model to follow key principles: First, keep each paragraph concise and digestible. Short paragraphs make ideas clearer and easier to follow. Second, adopt a conversational tone that feels natural and engaging. We avoid technical formatting like markdown to maintain a smooth reading experience. Third, and most importantly, the thinking process begins by understanding the complete user context. This means analyzing who our users are, what situations they’re dealing with, and what they truly need - including those unstated needs that may lie beneath the surface of their initial request.\n\nAfter eliciting these thinking processes from the model, human annotators meticulously verify the accuracy of the outputs. Our findings indicate that these artificial reasoning traces enhance the model’s precision in interpreting user queries. Specifically, they effectively highlight format constraints, clarify user intentions, and elucidate the requisite structure of outputs. This methodological approach facilitates more accurate and responsive interactions between the model and users.\n\nTable 5 | Data Statistics of SFT Data.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Domain&lt;/th>\n&lt;th>Num Samples&lt;/th>\n&lt;th>Avg Rounds&lt;/th>\n&lt;th>Avg Tokens&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Math&lt;/td>\n&lt;td>395285&lt;/td>\n&lt;td>1.0&lt;/td>\n&lt;td>6094.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Code&lt;/td>\n&lt;td>211129&lt;/td>\n&lt;td>1.1&lt;/td>\n&lt;td>7435.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>STEM&lt;/td>\n&lt;td>10124&lt;/td>\n&lt;td>1.0&lt;/td>\n&lt;td>4928.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Logic&lt;/td>\n&lt;td>10395&lt;/td>\n&lt;td>1.0&lt;/td>\n&lt;td>2739.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>General&lt;/td>\n&lt;td>177812&lt;/td>\n&lt;td>1.1&lt;/td>\n&lt;td>1419.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Total&lt;/td>\n&lt;td>804745&lt;/td>\n&lt;td>1.0&lt;/td>\n&lt;td>5355.3&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**SFT Data Statistics** Table 5 summarizes the data statistics across various domains, based on approximately 800,000 supervised samples. It is worth noting that the majority of the data consists of single-turn interactions, which may limit the multi-turn conversational capabilities of DeepSeek-R1. We leave the expansion to multi-turn dialogue data as future work. The math-related data are primarily in Chinese and English, spanning a wide range of topics and difficulty levels. These questions are verifiable, either through deterministic rules or by reference to specific ground-truth answers. The code dataset encompasses not only competitive programming problems but also debugging tasks and project-oriented coding queries. STEM and logic-related questions, although smaller in volume compared to mathematics and code, are sourced from publicly available textbooks and online repositories. The general-domain queries are diverse, predominantly in Chinese and English, and include tasks such as creative writing, open-ended question answering, role-playing scenarios, and more.\n\n**Examples of SFT Trajectories** We provide examples of SFT trajectories related to math, code, and non-reasoning in Listings 5, 6, and 7.\n\nListing 5 | An example SFT trajectory from reasoning data related to mathematics.\n\n```\n## Question\nFor positive integer  $n$ , define  $S_n$  to be the minimum value of the sum  $\\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2}$ , where  $a_1, a_2, \\dots, a_n$  are positive real numbers whose sum is 17. There is a unique positive integer  $n$  for which  $S_n$  is also an integer. Find this  $n$ .\n\n## Response\n```&lt;think>\n\nAlright, so I'm trying to solve this problem where I need to find a positive integer  $n$  such that  $S_n$ , the minimum value of the sum  $\\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2}$ , is an integer. Here,  $(a_1, a_2, \\dots, a_n)$  are positive real numbers that add up to 17.\n\nHmm, okay, let me break this down. I know that when you have a sum of square roots like this, it often relates to geometry, maybe minimizing distances. It reminds me of the problem where you have to break up a path into segments with certain slopes to minimize total distance. Maybe this is similar to finding the shortest path in a staircase.\n\nLet me visualize it. Each term  $\\sqrt{(2k-1)^2 + a_k^2}$  looks like the hypotenuse of a right-angled triangle with legs  $(2k-1)$  and  $a_k$ . So, if I imagine a grid where I move horizontally by  $a_k$  and vertically by  $(2k-1)$  for each step  $k$ , then  $S_n$  would be the total length of this path.\n\nNow, the sum of all  $a_k$  is 17, which would be the total horizontal distance. I need to figure out the vertical distances, which are fixed based on  $k$ . So the total vertical distance would be  $\\sum_{k=1}^n (2k-1)$ . Let me compute that:\n\nThe sum  $\\sum_{k=1}^n (2k-1)$  is equal to  $2 \\sum_{k=1}^n k - \\sum_{k=1}^n 1 = 2 \\cdot \\frac{n(n+1)}{2} - n = n(n+1) - n = n^2$ . So the total vertical distance is  $n^2$ .\n\nWait a second, so this entire setup is like moving from the origin to the point  $(17, n^2)$  with  $n$  segments. Each segment has a horizontal component  $a_k$  and a vertical component  $(2k-1)$ . But in reality, this entire path from  $(0, 0)$  to  $(17, n^2)$  can be considered as a single straight line if we could somehow combine all these segments.\n\nBut we can't change the number of segments  $n$ ; each segment's vertical component is fixed. However, the horizontal components  $a_k$  can be adjusted as long as their sum is 17. So, to find the minimal total distance, maybe we can think of it as if each segment is contributing to the total path optimally. If we scale each horizontal component  $a_k$  proportionally, maybe this also corresponds to scaling the vertical components.\n\nAlternatively, I can think of calculus optimization techniques. If I need to minimize the sum  $\\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2}$  subject to  $\\sum_{k=1}^n a_k = 17$ , I can use the method of Lagrange multipliers.\n\nLet me set up the Lagrangian. Let  $L = \\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2} + \\lambda (17 - \\sum_{k=1}^n a_k)$ .\n\nTaking the derivative of  $L$  with respect to each  $a_k$ :\n\n$$\\frac{\\partial L}{\\partial a_k} = \\frac{a_k}{\\sqrt{(2k-1)^2 + a_k^2}} - \\lambda = 0$$\n\nSo, for each  $k$ , we have  $\\frac{a_k}{\\sqrt{(2k-1)^2 + a_k^2}} = \\lambda$ . Let me solve for  $a_k$ :\n\nSquaring both sides gives  $\\frac{a_k^2}{(2k-1)^2 + a_k^2} = \\lambda^2$ .\n\nRearranging terms:  $a_k^2 = \\lambda^2 \\left( (2k-1)^2 + a_k^2 \\right)$ .\n\nDivide both sides by  $a_k^2$  (assuming  $a_k \\neq 0$ ):  $1 = \\lambda^2 \\left( \\frac{(2k-1)^2}{a_k^2} + 1 \\right)$ .Simplify:  $\\sqrt{1 - \\lambda^2} = \\lambda \\sqrt{\\frac{(2k-1)^2}{a_k^2}}$ .\n\nThen,  $\\sqrt{\\frac{(2k-1)^2}{a_k^2}} = \\sqrt{\\frac{1-\\lambda^2}{\\lambda^2}}$ .\n\nTherefore,  $\\sqrt{\\frac{2k-1}{a_k}} = \\sqrt{\\frac{1-\\lambda^2}{\\lambda^2}} = \\frac{\\sqrt{1-\\lambda^2}}{\\lambda}$ .\n\nLet me denote  $c = \\frac{\\sqrt{1-\\lambda^2}}{\\lambda}$ . Then,  $a_k = \\frac{2k-1}{c}$ .\n\nSo, each  $a_k$  is proportional to  $(2k-1)$ . That is,  $a_k = \\frac{2k-1}{c}$ .\n\nSince the sum of all  $a_k$  is 17, we can write:\n\n$\\sum_{k=1}^n a_k = \\sum_{k=1}^n \\frac{2k-1}{c} = \\frac{1}{c} \\sum_{k=1}^n (2k-1)$ .\n\nEarlier, I found that  $\\sum_{k=1}^n (2k-1) = n^2$ . Therefore,\n\n$\\frac{n^2}{c} = 17 \\Rightarrow c = \\frac{n^2}{17}$ .\n\nThus,  $a_k = \\frac{2k-1}{c} = \\frac{(2k-1) \\cdot 17}{n^2}$ .\n\nNow, going back to the original expression for  $S_n$ :\n\n$S_n = \\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2}$ .\n\nSubstituting  $a_k = \\frac{17(2k-1)}{n^2}$ , we get:\n\n$\\sqrt{(2k-1)^2 + \\left(\\frac{17(2k-1)}{n^2}\\right)^2} = (2k-1) \\sqrt{1 + \\left(\\frac{17}{n^2}\\right)^2}$ .\n\nSo, factor that square root out of the sum:\n\n$S_n = \\sqrt{1 + \\left(\\frac{17}{n^2}\\right)^2} \\cdot \\sum_{k=1}^n (2k-1)$ .\n\nWe already know that  $\\sum_{k=1}^n (2k-1) = n^2$ , so this simplifies to:\n\n$S_n = \\sqrt{1 + \\left(\\frac{17}{n^2}\\right)^2} \\cdot n^2 = \\sqrt{n^4 + 17^2} = \\sqrt{n^4 + 289}$ .\n\nWait, that seems too simplified. Let me check my steps:\n\n1. 1. I set up the Lagrangian correctly.\n2. 2. Took the derivative and found  $a_k = \\frac{2k-1}{c}$ .\n3. 3. Summed them up to get  $c = \\frac{n^2}{17}$ .\n4. 4. Plugged back into  $S_n$  and factored out  $(2k-1)$ , so each term becomes  $(2k-1) \\sqrt{1 + \\left(\\frac{17}{n^2}\\right)^2}$ .\n5. 5. Since  $\\sum (2k-1) = n^2$ , so total sum is  $n^2 \\sqrt{1 + \\left(\\frac{17}{n^2}\\right)^2} = \\sqrt{n^4 + 17^2}$ .\n\nYeah, that seems to check out. So,  $S_n = \\sqrt{n^4 + 289}$ . Wait,  $17^2$  is 289.\n\nTherefore,  $S_n = \\sqrt{n^4 + 289}$ . We need this to be an integer.\n\nSo, I need to find an integer  $n$  such that  $n^4 + 289$  is a perfect square.\n\nLet me denote  $S_n = m$ , where  $m$  is an integer, so:\n\n$n^4 + 289 = m^2$ .This implies  $(m^2 - n^4 = 289)$ .\n\nHmm, 289 is  $17^2$ . So,  $(m^2 - n^4 = 17^2)$ . That can be written as:\n\n$$(m^2 - n^4 = (17)^2)$$\n\nLooking at this equation, it's a difference of squares.\n\n$$(m^2 - n^4 = (m - n^2)(m + n^2) = 17^2 = 289)$$\n\nSo, we have  $(m - n^2)(m + n^2) = 289$ .\n\nSince  $(m)$  and  $(n)$  are positive integers, both  $(m - n^2)$  and  $(m + n^2)$  are positive integers and factors of 289. Also,  $(m + n^2 > m - n^2)$ .\n\nSo, since 289 is  $17^2$ , its positive factor pairs are (1, 289) and (17, 17).\n\nHence, the factor pairs are:\n\n1. 1.  $(m - n^2 = 1)$  and  $(m + n^2 = 289)$ .\n2. 2.  $(m - n^2 = 17)$  and  $(m + n^2 = 17)$ .\n\nBut the second case gives  $(m - n^2 = 17)$  and  $(m + n^2 = 17)$ .\n\nSubtracting the equations:  $(m + n^2) - (m - n^2) = 17 - 17 \\Rightarrow (2n^2 = 0) \\Rightarrow (n^2 = 0)$ . But  $(n)$  is a positive integer, so this case is invalid.\n\nSo, we only consider the first factor pair:  $(m - n^2 = 1)$  and  $(m + n^2 = 289)$ .\n\nAdding the two equations:  $(m - n^2) + (m + n^2) = 1 + 289 \\Rightarrow (2m = 290) \\Rightarrow (m = 145)$ .\n\nSubtracting the two equations:  $(m + n^2) - (m - n^2) = 289 - 1 \\Rightarrow (2n^2 = 288) \\Rightarrow (n^2 = 144) \\Rightarrow (n = 12)$  since  $(n)$  is positive.\n\nTherefore,  $(n = 12)$ .\n\nBefore I conclude, let me verify that  $(S_n = \\sqrt{12^4 + 17^2} = \\sqrt{20736 + 289} = \\sqrt{21025} = 145)$ , which is indeed an integer.\n\nIs this the only  $(n)$ ? The question says there's a unique positive integer  $(n)$ , so this must be the one.\n\n**\\*\\*Final Answer\\*\\***\n\nThe unique positive integer  $(n)$  is  $\\boxed{12}$ .  \n&lt;/think>\n\nTo solve the problem, we need to find a positive integer  $(n)$  such that  $(S_n)$ , the minimum value of the sum  $(\\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2})$ , is an integer. Here,  $(a_1, a_2, \\dots, a_n)$  are positive real numbers whose sum is 17.\n\nFirst, we recognize that each term  $(\\sqrt{(2k-1)^2 + a_k^2})$  represents the hypotenuse of a right-angled triangle with legs  $(2k-1)$  and  $(a_k)$ . The total vertical distance is the sum of the vertical components, which is  $(\\sum_{k=1}^n (2k-1) = n^2)$ . The total horizontal distance is the sum of  $(a_k)$ , which is 17.\n\nTo minimize the sum, we use the method of Lagrange multipliers. We find that each  $(a_k)$  is proportional to  $(2k-1)$ . Thus,  $(a_k = \\frac{17(2k-1)}{n^2})$ .\n",
    "durationMs": 643,
    "url": "https://huggingface.co/papers/2501.12948"
  },
  "sourceToolAssistantUUID": "50c768d0-2293-4c94-8c6a-d1aad469958e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```````

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "e1c336dc-1a20-4087-bb91-7bf0e0cf339a",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze DeepSeek-R1 reasoning innovation approach",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Tool call

_source line 25 · 2026-05-28T11:20:57.122Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NqUDtivhQnHq4Z56vQ13YS`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1c336dc-1a20-4087-bb91-7bf0e0cf339a",
  "isSidechain": false,
  "requestId": "req_011CbUstGYioqnshR49BipbT",
  "type": "assistant",
  "uuid": "c28aa088-a0f9-4c4c-9f0a-4e1898283153",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyzGdqaYDSbot2RxeDxjuT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 15572,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 15572,
          "cache_creation_input_tokens": 905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 905
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

_source line 26 · 2026-05-28T11:20:57.404Z_

<details><summary>↩ Tool result · `toolu_01NqUDtivhQnHq4Z56vQ13YS`</summary>

```text
1	# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
2	
3	DeepSeek-AI
4	
5	research@deepseek.com
6	
7	## Abstract
8	
9	General reasoning represents a long-standing and formidable challenge in artificial intelligence. Recent breakthroughs, exemplified by large language models (LLMs) (Brown et al., 2020; OpenAI, 2023) and chain-of-thought prompting (Wei et al., 2022b), have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent upon extensive human-annotated demonstrations, and models' capabilities are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions, and STEM fields, surpassing its counterparts trained via conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically harnessed to guide and enhance the reasoning capabilities of smaller models.
10	
11	## 1. Introduction
12	
13	Reasoning capability, the cornerstone of human intelligence, enables complex cognitive tasks ranging from mathematical problem-solving to logical deduction and programming. Recent advances in artificial intelligence have demonstrated that large language models (LLMs) can exhibit emergent behaviors, including reasoning abilities, when scaled to a sufficient size (Kaplan et al., 2020; Wei et al., 2022a). However, achieving such capabilities in pre-training typically demands substantial computational resources. In parallel, a complementary line of research has demonstrated that large language models can be effectively augmented through chain-of-thought (CoT) prompting. This technique, which involves either providing carefully designed few-shot examples or using minimalistic prompts such as "Let's think step by step" (Kojima et al., 2022; Wei et al., 2022b), enables models to produce intermediate reasoning steps, thereby substantially enhancing their performance on complex tasks. Similarly, further performance gains have been observed when models learn high-quality, multi-step reasoning trajectories during the post-training phase (Chung et al., 2024; OpenAI, 2023). Despite their effectiveness, these approaches exhibit notable limitations. Their dependence on human-annotated reasoning traces hinders scalability and introduces cognitive biases. Furthermore, by constraining models to replicate human thought processes, their performance is inherently capped by the human-provided exemplars, which prevents the exploration of superior, non-human-like reasoning pathways.
14	
15	To tackle these issues, we aim to explore the potential of LLMs for developing reasoning abilities through self-evolution in an RL framework, with minimal reliance on human labeling efforts. Specifically, we build upon DeepSeek-V3-Base (DeepSeek-AI, 2024b) and employ Group Relative Policy Optimization (GRPO) (Shao et al., 2024) as our RL framework. The reward signal is solely based on the correctness of final predictions against ground-truth answers, without imposing constraints on the reasoning process itself. Notably, we bypass the conventional supervised fine-tuning (SFT) phase before RL training. This design choice stems from our hypothesis that human-defined reasoning patterns may limit model exploration, whereas unrestricted RL training can better incentivize the emergence of novel reasoning capabilities in LLMs. Through this process, detailed in Section 2, our model (referred to as DeepSeek-R1-Zero) naturally developed diverse and sophisticated reasoning behaviors. In solving reasoning problems, the model exhibits a tendency to generate longer responses, incorporating verification, reflection, and the exploration of alternative approaches within each response. Although we do not explicitly teach the model how to reason, it successfully learns improved reasoning strategies through reinforcement learning.
16	
17	Although DeepSeek-R1-Zero demonstrates excellent reasoning capabilities, it faces challenges such as poor readability and language mixing, occasionally combining English and Chinese within a single chain-of-thought response. Furthermore, the rule-based RL training stage of DeepSeek-R1-Zero is narrowly focused on reasoning tasks, resulting in limited performance in broader areas such as writing and open-domain question answering. To address these challenges, we introduce DeepSeek-R1, a model trained through a multi-stage learning framework that integrates rejection sampling, reinforcement learning, and supervised fine-tuning, detailed in Section 3. This training pipeline enables DeepSeek-R1 to inherit the reasoning capabilities of its predecessor, DeepSeek-R1-Zero, while aligning model behavior with human preferences through additional non-reasoning data.
18	
19	To enable broader access to powerful AI at a lower energy cost, we have distilled several smaller models and made them publicly available. These distilled models exhibit strong reasoning capabilities, surpassing the performance of their original instruction-tuned counterparts. We believe that these instruction-tuned versions will also significantly contribute to the research community by providing a valuable resource for understanding the mechanisms underlying long chain-of-thought (CoT) reasoning models and for fostering the development of more powerful reasoning models. We release DeepSeek-R1 series models to the public at &lt;https://huggingface.co/deepseek-ai>.
20	
21	## 2. DeepSeek-R1-Zero
22	
23	We begin by elaborating on the training of DeepSeek-R1-Zero, which relies exclusively on reinforcement learning without supervised fine-tuning. To facilitate large-scale RL efficiency, we adopt Group Relative Policy Optimization (GRPO) (Shao et al., 2024).
24	
25	### 2.1. Group Relative Policy Optimization
26	
27	GRPO (Shao et al., 2024) is the reinforcement learning algorithm that we adopt to train DeepSeek-R1-Zero and DeepSeek-R1. It was originally proposed to simplify the training process and reduce the resource consumption of Proximal Policy Optimization (PPO) (Schulman et al., 2017), which is widely used in the RL stage of LLMs (Ouyang et al., 2022).For each question  $q$ , GRPO samples a group of outputs  $\{o_1, o_2, \dots, o_G\}$  from the old policy  $\pi_{\theta_{old}}$  and then optimizes the policy model  $\pi_{\theta}$  by maximizing the following objective:
28	
29	$$\mathcal{J}_{GRPO}(\theta) = \mathbb{E}[q \sim P(Q), \{o_i\}_{i=1}^G \sim \pi_{\theta_{old}}(O|q)]$$
30	
31	$$\frac{1}{G} \sum_{i=1}^G \left( \min \left( \frac{\pi_{\theta}(o_i|q)}{\pi_{\theta_{old}}(o_i|q)} A_i, \text{clip} \left( \frac{\pi_{\theta}(o_i|q)}{\pi_{\theta_{old}}(o_i|q)}, 1 - \varepsilon, 1 + \varepsilon \right) A_i \right) - \beta \mathbb{D}_{KL}(\pi_{\theta} || \pi_{ref}) \right), \quad (1)$$
32	
33	$$\mathbb{D}_{KL}(\pi_{\theta} || \pi_{ref}) = \frac{\pi_{ref}(o_i|q)}{\pi_{\theta}(o_i|q)} - \log \frac{\pi_{ref}(o_i|q)}{\pi_{\theta}(o_i|q)} - 1, \quad (2)$$
34	
35	where  $\pi_{ref}$  is a reference policy,  $\varepsilon$  and  $\beta$  are hyper-parameters, and  $A_i$  is the advantage, computed using a group of rewards  $\{r_1, r_2, \dots, r_G\}$  corresponding to the outputs within each group:
36	
37	$$A_i = \frac{r_i - \text{mean}(\{r_1, r_2, \dots, r_G\})}{\text{std}(\{r_1, r_2, \dots, r_G\})}. \quad (3)$$
38	
39	We give a comparison of GRPO and PPO in Supplementary A.3. To train DeepSeek-R1-Zero, we set the learning rate to 3e-6, the KL coefficient to 0.001, and the sampling temperature to 1 for rollout. For each question, we sample 16 outputs with a maximum length of 32,768 tokens before the 8.2k step and 65,536 tokens afterward. As a result, both the performance and response length of DeepSeek-R1-Zero exhibit a significant jump at the 8.2k step, with training continuing for a total of 10,400 steps, corresponding to 1.6 training epochs. Each training step consists of 32 unique questions, resulting in a training batch size of 512. Every 400 steps, we replace the reference model with the latest policy model. To accelerate training, each rollout generates 8,192 outputs, which are randomly split into 16 mini-batches and trained for only a single inner epoch.
40	
41	Table 1 | Template for DeepSeek-R1-Zero. **prompt** will be replaced with the specific reasoning question during training.
42	
43	---
44	
45	A conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user with the answer. The reasoning process and answer are enclosed within `&lt;think>...&lt;/think>` and `&lt;answer>...&lt;/answer>` tags, respectively, i.e., `&lt;think>` reasoning process here `&lt;/think>` `&lt;answer>` answer here `&lt;/answer>`. User: **prompt**. Assistant:
46	
47	---
48	
49	Our high-performance RL infrastructure is described in Supplementary B.1, ensuring scalable and efficient training.
50	
51	## 2.2. Reward Design
52	
53	The reward is the source of the training signal, which decides the direction of RL optimization. For DeepSeek-R1-Zero, we employ rule-based rewards to deliver precise feedback for data in mathematical, coding, and logical reasoning domains. Our rule-based reward system mainly consists of two types of rewards: accuracy rewards and format rewards.
54	
55	**Accuracy rewards** evaluate whether the response is correct. For example, in the case of math problems with deterministic results, the model is required to provide the final answer in a specified format (e.g., within a box), enabling reliable rule-based verification of correctness. Similarly, for code competition prompts, a compiler can be utilized to evaluate the model'sFigure 1 | (a) AIME accuracy of DeepSeek-R1-Zero during training. AIME takes a mathematical problem as input and a number as output, illustrated in Table 32. Pass@1 and Cons@16 are described in Supplementary D.1. The baseline is the average score achieved by human participants in the AIME competition. (b) The average response length of DeepSeek-R1-Zero on the training set during the RL process. DeepSeek-R1-Zero naturally learns to solve reasoning tasks with more thinking time. Note that a training step refers to a single policy update operation.
56	
57	responses against a suite of predefined test cases, thereby generating objective feedback on correctness.
58	
59	**Format rewards** complement the accuracy reward model by enforcing specific formatting requirements. In particular, the model is incentivized to encapsulate its reasoning process within designated tags, specifically ‘`&lt;think>`’ and ‘`&lt;/think>`’. This ensures that the model’s thought process is explicitly delineated, enhancing interpretability and facilitating subsequent analysis.
60	
61	$$Reward_{rule} = Reward_{acc} + Reward_{format} \quad (4)$$
62	
63	The accuracy, reward and format reward are combined with the same weight. Notably, we abstain from applying neural reward models—whether outcome-based or process-based—to reasoning tasks. This decision is predicated on our observation that neural reward models are susceptible to reward hacking during large-scale reinforcement learning. Moreover, retraining such models necessitates substantial computational resources and introduces additional complexity into the training pipeline, thereby complicating the overall optimization process.
64	
65	### 2.3. Incentivize Reasoning Capability in LLMs
66	
67	Specifically, we apply the RL technique on the DeepSeek-V3 base to train DeepSeek-R1-Zero. During training, we design a straightforward template, to require DeepSeek-R1-Zero to first produce a reasoning process, followed by the final answer. We intentionally limit our constraints to this structural format, avoiding any content-specific biases to ensure that we can accurately observe the model’s natural progression during the RL process.
68	
69	Figure 1(a) depicts the performance trajectory of DeepSeek-R1-Zero on the AIME 2024 benchmark throughout the RL training process, where the average pass@1 score on AIME 2024 shows a significant increase, jumping from an initial 15.6% to 77.9%. In addition, by leveraging the self-consistency decoding (Wang et al., 2023c), the model’s performance can beTable 2 | An interesting “aha moment” of an intermediate version of DeepSeek-R1-Zero. The model learns to rethink using an anthropomorphic tone. This is also an aha moment for us, allowing us to witness the power and beauty of reinforcement learning.
70	
71	---
72	
73	&lt;table border="0" style="width: 100%;">
74	&lt;tr>
75	&lt;td style="width: 5%; vertical-align: top;">
76	&lt;p>Question: If &lt;math>a &gt; 1&lt;/math>, then the sum of the real solutions of &lt;math>\sqrt{a - \sqrt{a + x}} = x&lt;/math> is equal to&lt;/p>
77	&lt;/td>
78	&lt;td style="width: 95%; vertical-align: top;">
79	&lt;p>Response: &lt;think&gt;&lt;/p>
80	&lt;p>To solve the equation &lt;math>\sqrt{a - \sqrt{a + x}} = x&lt;/math>, let’s start by squaring both ...&lt;/p>
81	&lt;math display="block">\left(\sqrt{a - \sqrt{a + x}}\right)^2 = x^2 \implies a - \sqrt{a + x} = x^2.&lt;/math>
82	&lt;p>Rearrange to isolate the inner square root term:&lt;/p>
83	&lt;math display="block">(a - x^2)^2 = a + x \implies a^2 - 2ax^2 + (x^2)^2 = a + x \implies x^4 - 2ax^2 - x + (a^2 - a) = 0&lt;/math>
84	&lt;p>...&lt;/p>
85	&lt;p>&lt;b>Wait, wait. Wait. That’s an aha moment I can flag here.&lt;/b>&lt;/p>
86	&lt;p>Let’s reevaluate this step-by-step to identify if the correct sum can be ...&lt;/p>
87	&lt;p>We started with the equation:&lt;/p>
88	&lt;math display="block">\sqrt{a - \sqrt{a + x}} = x&lt;/math>
89	&lt;p>First, let’s square both sides:&lt;/p>
90	&lt;math display="block">a - \sqrt{a + x} = x^2 \implies \sqrt{a + x} = a - x^2&lt;/math>
91	&lt;p>Next, I could square both sides again, treating the equation: ...&lt;/p>
92	&lt;p>...&lt;/p>
93	&lt;/td>
94	&lt;/tr>
95	&lt;/table>
96	
97	---
98	
99	further improved, achieving an accuracy of 86.7%. This performance significantly surpasses the average performance across all human competitors. Besides the math competitions, as shown in Figure 10, DeepSeek-R1-Zero also achieves remarkable performance in coding competitions and graduate-level biology, physics, and chemistry problems. These results underscore the effectiveness of RL in enhancing the reasoning capabilities of large language models.
100	
101	The self-evolution of DeepSeek-R1-Zero exemplifies how RL can autonomously enhance a model’s reasoning capabilities.
102	
103	As shown in Figure 1(b), DeepSeek-R1-Zero exhibits a steady increase in thinking time throughout training, driven solely by intrinsic adaptation rather than external modifications. Leveraging long CoT, the model progressively refines its reasoning, generating hundreds to thousands of tokens to explore and improve its problem-solving strategies.
104	
105	The increase in thinking time fosters the autonomous development of sophisticated behaviors. Specifically, DeepSeek-R1-Zero increasingly exhibits advanced reasoning strategies such as reflective reasoning and systematic exploration of alternative solutions (see Figure 9(a) in Supplementary C.2 for details), significantly boosting its performance on verifiable tasks like math and coding. Notably, during training, DeepSeek-R1-Zero exhibits an “aha moment” (Table 2), characterized by a sudden increase in the use of the word “wait” during reflections (see Figure 9(b) in Supplementary C.2 for details). This moment marks a distinct change in reasoning patterns and clearly shows the self-evolution process of DeepSeek-R1-Zero.
106	
107	The self-evolution of DeepSeek-R1-Zero underscores the power and beauty of RL: rather than explicitly teaching the model how to solve a problem, we simply provide it with the right incentives, and it autonomously develops advanced problem-solving strategies. This serves as a reminder of the potential of RL to unlock higher levels of capabilities in LLMs, paving the way for more autonomous and adaptive models in the future.Figure 2 | The multi-stage pipeline of DeepSeek-R1. A detailed background on DeepSeek-V3 Base and DeepSeek-V3 is provided in Supplementary A.1. The models DeepSeek-R1 Dev1, Dev2, and Dev3 represent intermediate checkpoints within this pipeline.
108	
109	### 3. DeepSeek-R1
110	
111	Although DeepSeek-R1-Zero exhibits strong reasoning capabilities, it faces several issues. DeepSeek-R1-Zero struggles with challenges like poor readability, and language mixing, as DeepSeek-V3-Base is trained on multiple languages, especially English and Chinese. To address these issues, we develop DeepSeek-R1, whose pipeline is illustrated in Figure 2.
112	
113	In the initial stage, we collect thousands of cold-start data that exhibits a conversational, human-aligned thinking process. RL training is then applied to improve the model performance with the conversational thinking process and language consistency. Subsequently, we apply rejection sampling and SFT once more. This stage incorporates both reasoning and non-reasoning datasets into the SFT process, enabling the model to not only excel in reasoning tasks but also demonstrate advanced writing capabilities. To further align the model with human preferences, we implement a secondary RL stage designed to enhance the model’s helpfulness and harmlessness while simultaneously refining its reasoning capabilities.
114	
115	The remainder of this section details the key components of this pipeline: Section 3.1 introduces the Reward Model utilized in our RL stages, and Section 3.2 elaborates on the specific training methodologies and implementation details. Data we used in this stage is detailed in Supplementary B.3.
116	
117	#### 3.1. Model-based Rewards
118	
119	For general data, we resort to reward models to capture human preferences in complex and nuanced scenarios. We build upon the DeepSeek-V3 pipeline and adopt a similar distribution of preference pairs and training prompts. For helpfulness, we focus exclusively on the final summary, ensuring that the assessment emphasizes the utility and relevance of the response to the user while minimizing interference with the underlying reasoning process. For harmlessness, we evaluate the entire response of the model, including both the reasoning process and the summary, to identify and mitigate any potential risks, biases, or harmful content that may ariseduring the generation process.
120	
121	**Helpful Reward Model** Regarding helpful reward model training, we first generate preference pairs by prompting DeepSeek-V3 using the arena-hard prompt format, listed in Supplementary B.2, where each pair consists of a user query along with two candidate responses. For each preference pair, we query DeepSeek-V3 four times, randomly assigning the responses as either Response A or Response B to mitigate positional bias. The final preference score is determined by averaging the four independent judgments, retaining only those pairs where the score difference ( $\Delta$ ) exceeds 1 to ensure meaningful distinctions. Additionally, to minimize length-related biases, we ensure that the chosen and rejected responses of the whole dataset have comparable lengths. In total, we curated 66,000 data pairs for training the reward model. The prompts used in this dataset are all non-reasoning questions and are sourced either from publicly available open-source datasets or from users who have explicitly consented to share their data for the purpose of model improvement. The architecture of our reward model is consistent with that of DeepSeek-R1, with the addition of a reward head designed to predict scalar preference scores.
122	
123	$$Reward_{\text{helpful}} = RM_{\text{helpful}}(Response_A, Response_B) \quad (5)$$
124	
125	The helpful reward models were trained with a batch size of 256, a learning rate of 6e-6, and for a single epoch over the training dataset. The maximum sequence length during training is set to 8192 tokens, whereas no explicit limit is imposed during reward model inference.
126	
127	**Safety Reward Model** To assess and improve model safety, we curated a dataset of 106,000 prompts with model-generated responses annotated as “safe” or “unsafe” according to predefined safety guidelines. Unlike the pairwise loss employed in the helpfulness reward model, the safety reward model was trained using a point-wise methodology to distinguish between safe and unsafe responses. The training hyperparameters are the same as the helpful reward model.
128	
129	$$Reward_{\text{safety}} = RM_{\text{safety}}(Response) \quad (6)$$
130	
131	For general queries, each instance is categorized as belonging to either the safety dataset or the helpfulness dataset. The general reward,  $Reward_{\text{General}}$ , assigned to each query corresponds to the respective reward defined within the associated dataset.
132	
133	### 3.2. Training Details
134	
135	#### 3.2.1. Training Details of the First RL Stage
136	
137	In the first stage of RL, we set the learning rate to 3e-6, the KL coefficient to 0.001, the GRPO clip ratio  $\epsilon$  to 10, and the sampling temperature to 1 for rollout. For each question, we sample 16 outputs with a maximum length of 32,768. Each training step consists of 32 unique questions, resulting in a training batch size of 512 per step. Every 400 steps, we replace the reference model with the latest policy model. To accelerate training, each rollout generates 8,192 outputs, which are randomly split into 16 minibatches and trained for only a single inner epoch. However, to mitigate the issue of language mixing, we introduce a language consistency reward during RL training, which is calculated as the proportion of target language words in the CoT.
138	
139	$$Reward_{\text{language}} = \frac{\text{Num}(\text{Words}_{\text{target}})}{\text{Num}(\text{Words})} \quad (7)$$Although ablation experiments in Supplementary B.6 show that such alignment results in a slight degradation in the model’s performance, this reward aligns with human preferences, making it more readable. We apply the language consistency reward to both reasoning and non-reasoning data by directly adding it to the final reward.
140	
141	Note that the clip ratio plays a crucial role in training. A lower value can lead to the truncation of gradients for a significant number of tokens, thereby degrading the model’s performance, while a higher value may cause instability during training.
142	
143	### 3.2.2. Training Details of the Second RL Stage
144	
145	Specifically, we train the model using a combination of reward signals and diverse prompt distributions. For reasoning data, we follow the methodology outlined in DeepSeek-R1-Zero, which employs rule-based rewards to guide learning in mathematical, coding, and logical reasoning domains. During the training process, we observe that CoT often exhibits language mixing, particularly when RL prompts involve multiple languages. For general data, we utilize reward models to guide training. Ultimately, the integration of reward signals with diverse data distributions enables us to develop a model that not only excels in reasoning but also prioritizes helpfulness and harmlessness. Given a batch of data, the reward can be formulated as
146	
147	$$Reward = Reward_{\text{reasoning}} + Reward_{\text{general}} + Reward_{\text{language}} \quad (8)$$
148	
149	$$\text{where, } Reward_{\text{reasoning}} = Reward_{\text{rule}} \quad (9)$$
150	
151	$$Reward_{\text{general}} = Reward_{\text{reward\_model}} + Reward_{\text{format}} \quad (10)$$
152	
153	The second stage of RL retains most of the parameters from the first stage, with the key difference being a reduced temperature of 0.7, as we find that higher temperatures in this stage lead to incoherent generation. The stage comprises a total of 1,700 training steps, during which general instruction data and preference-based rewards are incorporated exclusively in the final 400 steps. We find that more training steps with the model based preference reward signal may lead to reward hacking, which is documented in Supplementary B.5. The total training cost is listed in Supplementary B.4.4.
154	
155	## 4. Experiment
156	
157	We evaluate our models on MMLU (Hendrycks et al., 2021), MMLU-Redux (Gema et al., 2025), MMLU-Pro (Wang et al., 2024), C-Eval (Huang et al., 2023), and CMMLU (Li et al., 2024), IFEval (Zhou et al., 2023b), FRAMES (Krishna et al., 2024), GPQA Diamond (Rein et al., 2023), SimpleQA (OpenAI, 2024a), C-SimpleQA (He et al., 2024), SWE-Bench Verified (OpenAI, 2024b), Aider (Gauthier, 2025), LiveCodeBench (Jain et al., 2024) (2024-08 – 2025-01), Codeforces (Mirzayanov, 2025), Chinese National High School Mathematics Olympiad (CNMO 2024) (CMS, 2024), and American Invitational Mathematics Examination 2024 (AIME 2024) (MAA, 2024). The details of these benchmarks are listed in Supplementary D.
158	
159	Table 3 summarizes the performance of DeepSeek-R1 across multiple developmental stages, as outlined in Figure 2. A comparison between DeepSeek-R1-Zero and DeepSeek-R1 Dev1 reveals substantial improvements in instruction-following, as evidenced by higher scores on the IF-Eval and ArenaHard benchmarks. However, due to the limited size of the cold-start dataset, Dev1 exhibits a partial degradation in reasoning performance compared to DeepSeek-R1-Zero, most notably on the AIME benchmark. In contrast, DeepSeek-R1 Dev2 demonstratesTable 3 | Experimental results at each stage of DeepSeek-R1. Numbers in bold denote the performance is statistically significant (t-test with  $p < 0.01$ ).
160	
161	&lt;table border="1">
162	&lt;thead>
163	&lt;tr>
164	&lt;th colspan="2">Benchmark (Metric)&lt;/th>
165	&lt;th>R1-Zero&lt;/th>
166	&lt;th>R1-Dev1&lt;/th>
167	&lt;th>R1-Dev2&lt;/th>
168	&lt;th>R1-Dev3&lt;/th>
169	&lt;th>R1&lt;/th>
170	&lt;/tr>
171	&lt;/thead>
172	&lt;tbody>
173	&lt;tr>
174	&lt;td rowspan="10">English&lt;/td>
175	&lt;td>MMLU (EM)&lt;/td>
176	&lt;td>88.8&lt;/td>
177	&lt;td>89.1&lt;/td>
178	&lt;td>&lt;b>91.2&lt;/b>&lt;/td>
179	&lt;td>91.0&lt;/td>
180	&lt;td>90.8&lt;/td>
181	&lt;/tr>
182	&lt;tr>
183	&lt;td>MMLU-Redux (EM)&lt;/td>
184	&lt;td>85.6&lt;/td>
185	&lt;td>90.0&lt;/td>
186	&lt;td>93.0&lt;/td>
187	&lt;td>93.1&lt;/td>
188	&lt;td>92.9&lt;/td>
189	&lt;/tr>
190	&lt;tr>
191	&lt;td>MMLU-Pro (EM)&lt;/td>
192	&lt;td>68.9&lt;/td>
193	&lt;td>74.1&lt;/td>
194	&lt;td>83.8&lt;/td>
195	&lt;td>83.1&lt;/td>
196	&lt;td>&lt;b>84.0&lt;/b>&lt;/td>
197	&lt;/tr>
198	&lt;tr>
199	&lt;td>DROP (3-shot F1)&lt;/td>
200	&lt;td>89.1&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c28aa088-a0f9-4c4c-9f0a-4e1898283153",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "812d745d-4034-4aaa-aa44-c11d91a855b1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt",
      "content": "# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\n\nDeepSeek-AI\n\nresearch@deepseek.com\n\n## Abstract\n\nGeneral reasoning represents a long-standing and formidable challenge in artificial intelligence. Recent breakthroughs, exemplified by large language models (LLMs) (Brown et al., 2020; OpenAI, 2023) and chain-of-thought prompting (Wei et al., 2022b), have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent upon extensive human-annotated demonstrations, and models' capabilities are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions, and STEM fields, surpassing its counterparts trained via conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically harnessed to guide and enhance the reasoning capabilities of smaller models.\n\n## 1. Introduction\n\nReasoning capability, the cornerstone of human intelligence, enables complex cognitive tasks ranging from mathematical problem-solving to logical deduction and programming. Recent advances in artificial intelligence have demonstrated that large language models (LLMs) can exhibit emergent behaviors, including reasoning abilities, when scaled to a sufficient size (Kaplan et al., 2020; Wei et al., 2022a). However, achieving such capabilities in pre-training typically demands substantial computational resources. In parallel, a complementary line of research has demonstrated that large language models can be effectively augmented through chain-of-thought (CoT) prompting. This technique, which involves either providing carefully designed few-shot examples or using minimalistic prompts such as \"Let's think step by step\" (Kojima et al., 2022; Wei et al., 2022b), enables models to produce intermediate reasoning steps, thereby substantially enhancing their performance on complex tasks. Similarly, further performance gains have been observed when models learn high-quality, multi-step reasoning trajectories during the post-training phase (Chung et al., 2024; OpenAI, 2023). Despite their effectiveness, these approaches exhibit notable limitations. Their dependence on human-annotated reasoning traces hinders scalability and introduces cognitive biases. Furthermore, by constraining models to replicate human thought processes, their performance is inherently capped by the human-provided exemplars, which prevents the exploration of superior, non-human-like reasoning pathways.\n\nTo tackle these issues, we aim to explore the potential of LLMs for developing reasoning abilities through self-evolution in an RL framework, with minimal reliance on human labeling efforts. Specifically, we build upon DeepSeek-V3-Base (DeepSeek-AI, 2024b) and employ Group Relative Policy Optimization (GRPO) (Shao et al., 2024) as our RL framework. The reward signal is solely based on the correctness of final predictions against ground-truth answers, without imposing constraints on the reasoning process itself. Notably, we bypass the conventional supervised fine-tuning (SFT) phase before RL training. This design choice stems from our hypothesis that human-defined reasoning patterns may limit model exploration, whereas unrestricted RL training can better incentivize the emergence of novel reasoning capabilities in LLMs. Through this process, detailed in Section 2, our model (referred to as DeepSeek-R1-Zero) naturally developed diverse and sophisticated reasoning behaviors. In solving reasoning problems, the model exhibits a tendency to generate longer responses, incorporating verification, reflection, and the exploration of alternative approaches within each response. Although we do not explicitly teach the model how to reason, it successfully learns improved reasoning strategies through reinforcement learning.\n\nAlthough DeepSeek-R1-Zero demonstrates excellent reasoning capabilities, it faces challenges such as poor readability and language mixing, occasionally combining English and Chinese within a single chain-of-thought response. Furthermore, the rule-based RL training stage of DeepSeek-R1-Zero is narrowly focused on reasoning tasks, resulting in limited performance in broader areas such as writing and open-domain question answering. To address these challenges, we introduce DeepSeek-R1, a model trained through a multi-stage learning framework that integrates rejection sampling, reinforcement learning, and supervised fine-tuning, detailed in Section 3. This training pipeline enables DeepSeek-R1 to inherit the reasoning capabilities of its predecessor, DeepSeek-R1-Zero, while aligning model behavior with human preferences through additional non-reasoning data.\n\nTo enable broader access to powerful AI at a lower energy cost, we have distilled several smaller models and made them publicly available. These distilled models exhibit strong reasoning capabilities, surpassing the performance of their original instruction-tuned counterparts. We believe that these instruction-tuned versions will also significantly contribute to the research community by providing a valuable resource for understanding the mechanisms underlying long chain-of-thought (CoT) reasoning models and for fostering the development of more powerful reasoning models. We release DeepSeek-R1 series models to the public at &lt;https://huggingface.co/deepseek-ai>.\n\n## 2. DeepSeek-R1-Zero\n\nWe begin by elaborating on the training of DeepSeek-R1-Zero, which relies exclusively on reinforcement learning without supervised fine-tuning. To facilitate large-scale RL efficiency, we adopt Group Relative Policy Optimization (GRPO) (Shao et al., 2024).\n\n### 2.1. Group Relative Policy Optimization\n\nGRPO (Shao et al., 2024) is the reinforcement learning algorithm that we adopt to train DeepSeek-R1-Zero and DeepSeek-R1. It was originally proposed to simplify the training process and reduce the resource consumption of Proximal Policy Optimization (PPO) (Schulman et al., 2017), which is widely used in the RL stage of LLMs (Ouyang et al., 2022).For each question  $q$ , GRPO samples a group of outputs  $\\{o_1, o_2, \\dots, o_G\\}$  from the old policy  $\\pi_{\\theta_{old}}$  and then optimizes the policy model  $\\pi_{\\theta}$  by maximizing the following objective:\n\n$$\\mathcal{J}_{GRPO}(\\theta) = \\mathbb{E}[q \\sim P(Q), \\{o_i\\}_{i=1}^G \\sim \\pi_{\\theta_{old}}(O|q)]$$\n\n$$\\frac{1}{G} \\sum_{i=1}^G \\left( \\min \\left( \\frac{\\pi_{\\theta}(o_i|q)}{\\pi_{\\theta_{old}}(o_i|q)} A_i, \\text{clip} \\left( \\frac{\\pi_{\\theta}(o_i|q)}{\\pi_{\\theta_{old}}(o_i|q)}, 1 - \\varepsilon, 1 + \\varepsilon \\right) A_i \\right) - \\beta \\mathbb{D}_{KL}(\\pi_{\\theta} || \\pi_{ref}) \\right), \\quad (1)$$\n\n$$\\mathbb{D}_{KL}(\\pi_{\\theta} || \\pi_{ref}) = \\frac{\\pi_{ref}(o_i|q)}{\\pi_{\\theta}(o_i|q)} - \\log \\frac{\\pi_{ref}(o_i|q)}{\\pi_{\\theta}(o_i|q)} - 1, \\quad (2)$$\n\nwhere  $\\pi_{ref}$  is a reference policy,  $\\varepsilon$  and  $\\beta$  are hyper-parameters, and  $A_i$  is the advantage, computed using a group of rewards  $\\{r_1, r_2, \\dots, r_G\\}$  corresponding to the outputs within each group:\n\n$$A_i = \\frac{r_i - \\text{mean}(\\{r_1, r_2, \\dots, r_G\\})}{\\text{std}(\\{r_1, r_2, \\dots, r_G\\})}. \\quad (3)$$\n\nWe give a comparison of GRPO and PPO in Supplementary A.3. To train DeepSeek-R1-Zero, we set the learning rate to 3e-6, the KL coefficient to 0.001, and the sampling temperature to 1 for rollout. For each question, we sample 16 outputs with a maximum length of 32,768 tokens before the 8.2k step and 65,536 tokens afterward. As a result, both the performance and response length of DeepSeek-R1-Zero exhibit a significant jump at the 8.2k step, with training continuing for a total of 10,400 steps, corresponding to 1.6 training epochs. Each training step consists of 32 unique questions, resulting in a training batch size of 512. Every 400 steps, we replace the reference model with the latest policy model. To accelerate training, each rollout generates 8,192 outputs, which are randomly split into 16 mini-batches and trained for only a single inner epoch.\n\nTable 1 | Template for DeepSeek-R1-Zero. **prompt** will be replaced with the specific reasoning question during training.\n\n---\n\nA conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user with the answer. The reasoning process and answer are enclosed within `&lt;think>...&lt;/think>` and `&lt;answer>...&lt;/answer>` tags, respectively, i.e., `&lt;think>` reasoning process here `&lt;/think>` `&lt;answer>` answer here `&lt;/answer>`. User: **prompt**. Assistant:\n\n---\n\nOur high-performance RL infrastructure is described in Supplementary B.1, ensuring scalable and efficient training.\n\n## 2.2. Reward Design\n\nThe reward is the source of the training signal, which decides the direction of RL optimization. For DeepSeek-R1-Zero, we employ rule-based rewards to deliver precise feedback for data in mathematical, coding, and logical reasoning domains. Our rule-based reward system mainly consists of two types of rewards: accuracy rewards and format rewards.\n\n**Accuracy rewards** evaluate whether the response is correct. For example, in the case of math problems with deterministic results, the model is required to provide the final answer in a specified format (e.g., within a box), enabling reliable rule-based verification of correctness. Similarly, for code competition prompts, a compiler can be utilized to evaluate the model'sFigure 1 | (a) AIME accuracy of DeepSeek-R1-Zero during training. AIME takes a mathematical problem as input and a number as output, illustrated in Table 32. Pass@1 and Cons@16 are described in Supplementary D.1. The baseline is the average score achieved by human participants in the AIME competition. (b) The average response length of DeepSeek-R1-Zero on the training set during the RL process. DeepSeek-R1-Zero naturally learns to solve reasoning tasks with more thinking time. Note that a training step refers to a single policy update operation.\n\nresponses against a suite of predefined test cases, thereby generating objective feedback on correctness.\n\n**Format rewards** complement the accuracy reward model by enforcing specific formatting requirements. In particular, the model is incentivized to encapsulate its reasoning process within designated tags, specifically ‘`&lt;think>`’ and ‘`&lt;/think>`’. This ensures that the model’s thought process is explicitly delineated, enhancing interpretability and facilitating subsequent analysis.\n\n$$Reward_{rule} = Reward_{acc} + Reward_{format} \\quad (4)$$\n\nThe accuracy, reward and format reward are combined with the same weight. Notably, we abstain from applying neural reward models—whether outcome-based or process-based—to reasoning tasks. This decision is predicated on our observation that neural reward models are susceptible to reward hacking during large-scale reinforcement learning. Moreover, retraining such models necessitates substantial computational resources and introduces additional complexity into the training pipeline, thereby complicating the overall optimization process.\n\n### 2.3. Incentivize Reasoning Capability in LLMs\n\nSpecifically, we apply the RL technique on the DeepSeek-V3 base to train DeepSeek-R1-Zero. During training, we design a straightforward template, to require DeepSeek-R1-Zero to first produce a reasoning process, followed by the final answer. We intentionally limit our constraints to this structural format, avoiding any content-specific biases to ensure that we can accurately observe the model’s natural progression during the RL process.\n\nFigure 1(a) depicts the performance trajectory of DeepSeek-R1-Zero on the AIME 2024 benchmark throughout the RL training process, where the average pass@1 score on AIME 2024 shows a significant increase, jumping from an initial 15.6% to 77.9%. In addition, by leveraging the self-consistency decoding (Wang et al., 2023c), the model’s performance can beTable 2 | An interesting “aha moment” of an intermediate version of DeepSeek-R1-Zero. The model learns to rethink using an anthropomorphic tone. This is also an aha moment for us, allowing us to witness the power and beauty of reinforcement learning.\n\n---\n\n&lt;table border=\"0\" style=\"width: 100%;\">\n&lt;tr>\n&lt;td style=\"width: 5%; vertical-align: top;\">\n&lt;p>Question: If &lt;math>a &gt; 1&lt;/math>, then the sum of the real solutions of &lt;math>\\sqrt{a - \\sqrt{a + x}} = x&lt;/math> is equal to&lt;/p>\n&lt;/td>\n&lt;td style=\"width: 95%; vertical-align: top;\">\n&lt;p>Response: &lt;think&gt;&lt;/p>\n&lt;p>To solve the equation &lt;math>\\sqrt{a - \\sqrt{a + x}} = x&lt;/math>, let’s start by squaring both ...&lt;/p>\n&lt;math display=\"block\">\\left(\\sqrt{a - \\sqrt{a + x}}\\right)^2 = x^2 \\implies a - \\sqrt{a + x} = x^2.&lt;/math>\n&lt;p>Rearrange to isolate the inner square root term:&lt;/p>\n&lt;math display=\"block\">(a - x^2)^2 = a + x \\implies a^2 - 2ax^2 + (x^2)^2 = a + x \\implies x^4 - 2ax^2 - x + (a^2 - a) = 0&lt;/math>\n&lt;p>...&lt;/p>\n&lt;p>&lt;b>Wait, wait. Wait. That’s an aha moment I can flag here.&lt;/b>&lt;/p>\n&lt;p>Let’s reevaluate this step-by-step to identify if the correct sum can be ...&lt;/p>\n&lt;p>We started with the equation:&lt;/p>\n&lt;math display=\"block\">\\sqrt{a - \\sqrt{a + x}} = x&lt;/math>\n&lt;p>First, let’s square both sides:&lt;/p>\n&lt;math display=\"block\">a - \\sqrt{a + x} = x^2 \\implies \\sqrt{a + x} = a - x^2&lt;/math>\n&lt;p>Next, I could square both sides again, treating the equation: ...&lt;/p>\n&lt;p>...&lt;/p>\n&lt;/td>\n&lt;/tr>\n&lt;/table>\n\n---\n\nfurther improved, achieving an accuracy of 86.7%. This performance significantly surpasses the average performance across all human competitors. Besides the math competitions, as shown in Figure 10, DeepSeek-R1-Zero also achieves remarkable performance in coding competitions and graduate-level biology, physics, and chemistry problems. These results underscore the effectiveness of RL in enhancing the reasoning capabilities of large language models.\n\nThe self-evolution of DeepSeek-R1-Zero exemplifies how RL can autonomously enhance a model’s reasoning capabilities.\n\nAs shown in Figure 1(b), DeepSeek-R1-Zero exhibits a steady increase in thinking time throughout training, driven solely by intrinsic adaptation rather than external modifications. Leveraging long CoT, the model progressively refines its reasoning, generating hundreds to thousands of tokens to explore and improve its problem-solving strategies.\n\nThe increase in thinking time fosters the autonomous development of sophisticated behaviors. Specifically, DeepSeek-R1-Zero increasingly exhibits advanced reasoning strategies such as reflective reasoning and systematic exploration of alternative solutions (see Figure 9(a) in Supplementary C.2 for details), significantly boosting its performance on verifiable tasks like math and coding. Notably, during training, DeepSeek-R1-Zero exhibits an “aha moment” (Table 2), characterized by a sudden increase in the use of the word “wait” during reflections (see Figure 9(b) in Supplementary C.2 for details). This moment marks a distinct change in reasoning patterns and clearly shows the self-evolution process of DeepSeek-R1-Zero.\n\nThe self-evolution of DeepSeek-R1-Zero underscores the power and beauty of RL: rather than explicitly teaching the model how to solve a problem, we simply provide it with the right incentives, and it autonomously develops advanced problem-solving strategies. This serves as a reminder of the potential of RL to unlock higher levels of capabilities in LLMs, paving the way for more autonomous and adaptive models in the future.Figure 2 | The multi-stage pipeline of DeepSeek-R1. A detailed background on DeepSeek-V3 Base and DeepSeek-V3 is provided in Supplementary A.1. The models DeepSeek-R1 Dev1, Dev2, and Dev3 represent intermediate checkpoints within this pipeline.\n\n### 3. DeepSeek-R1\n\nAlthough DeepSeek-R1-Zero exhibits strong reasoning capabilities, it faces several issues. DeepSeek-R1-Zero struggles with challenges like poor readability, and language mixing, as DeepSeek-V3-Base is trained on multiple languages, especially English and Chinese. To address these issues, we develop DeepSeek-R1, whose pipeline is illustrated in Figure 2.\n\nIn the initial stage, we collect thousands of cold-start data that exhibits a conversational, human-aligned thinking process. RL training is then applied to improve the model performance with the conversational thinking process and language consistency. Subsequently, we apply rejection sampling and SFT once more. This stage incorporates both reasoning and non-reasoning datasets into the SFT process, enabling the model to not only excel in reasoning tasks but also demonstrate advanced writing capabilities. To further align the model with human preferences, we implement a secondary RL stage designed to enhance the model’s helpfulness and harmlessness while simultaneously refining its reasoning capabilities.\n\nThe remainder of this section details the key components of this pipeline: Section 3.1 introduces the Reward Model utilized in our RL stages, and Section 3.2 elaborates on the specific training methodologies and implementation details. Data we used in this stage is detailed in Supplementary B.3.\n\n#### 3.1. Model-based Rewards\n\nFor general data, we resort to reward models to capture human preferences in complex and nuanced scenarios. We build upon the DeepSeek-V3 pipeline and adopt a similar distribution of preference pairs and training prompts. For helpfulness, we focus exclusively on the final summary, ensuring that the assessment emphasizes the utility and relevance of the response to the user while minimizing interference with the underlying reasoning process. For harmlessness, we evaluate the entire response of the model, including both the reasoning process and the summary, to identify and mitigate any potential risks, biases, or harmful content that may ariseduring the generation process.\n\n**Helpful Reward Model** Regarding helpful reward model training, we first generate preference pairs by prompting DeepSeek-V3 using the arena-hard prompt format, listed in Supplementary B.2, where each pair consists of a user query along with two candidate responses. For each preference pair, we query DeepSeek-V3 four times, randomly assigning the responses as either Response A or Response B to mitigate positional bias. The final preference score is determined by averaging the four independent judgments, retaining only those pairs where the score difference ( $\\Delta$ ) exceeds 1 to ensure meaningful distinctions. Additionally, to minimize length-related biases, we ensure that the chosen and rejected responses of the whole dataset have comparable lengths. In total, we curated 66,000 data pairs for training the reward model. The prompts used in this dataset are all non-reasoning questions and are sourced either from publicly available open-source datasets or from users who have explicitly consented to share their data for the purpose of model improvement. The architecture of our reward model is consistent with that of DeepSeek-R1, with the addition of a reward head designed to predict scalar preference scores.\n\n$$Reward_{\\text{helpful}} = RM_{\\text{helpful}}(Response_A, Response_B) \\quad (5)$$\n\nThe helpful reward models were trained with a batch size of 256, a learning rate of 6e-6, and for a single epoch over the training dataset. The maximum sequence length during training is set to 8192 tokens, whereas no explicit limit is imposed during reward model inference.\n\n**Safety Reward Model** To assess and improve model safety, we curated a dataset of 106,000 prompts with model-generated responses annotated as “safe” or “unsafe” according to predefined safety guidelines. Unlike the pairwise loss employed in the helpfulness reward model, the safety reward model was trained using a point-wise methodology to distinguish between safe and unsafe responses. The training hyperparameters are the same as the helpful reward model.\n\n$$Reward_{\\text{safety}} = RM_{\\text{safety}}(Response) \\quad (6)$$\n\nFor general queries, each instance is categorized as belonging to either the safety dataset or the helpfulness dataset. The general reward,  $Reward_{\\text{General}}$ , assigned to each query corresponds to the respective reward defined within the associated dataset.\n\n### 3.2. Training Details\n\n#### 3.2.1. Training Details of the First RL Stage\n\nIn the first stage of RL, we set the learning rate to 3e-6, the KL coefficient to 0.001, the GRPO clip ratio  $\\epsilon$  to 10, and the sampling temperature to 1 for rollout. For each question, we sample 16 outputs with a maximum length of 32,768. Each training step consists of 32 unique questions, resulting in a training batch size of 512 per step. Every 400 steps, we replace the reference model with the latest policy model. To accelerate training, each rollout generates 8,192 outputs, which are randomly split into 16 minibatches and trained for only a single inner epoch. However, to mitigate the issue of language mixing, we introduce a language consistency reward during RL training, which is calculated as the proportion of target language words in the CoT.\n\n$$Reward_{\\text{language}} = \\frac{\\text{Num}(\\text{Words}_{\\text{target}})}{\\text{Num}(\\text{Words})} \\quad (7)$$Although ablation experiments in Supplementary B.6 show that such alignment results in a slight degradation in the model’s performance, this reward aligns with human preferences, making it more readable. We apply the language consistency reward to both reasoning and non-reasoning data by directly adding it to the final reward.\n\nNote that the clip ratio plays a crucial role in training. A lower value can lead to the truncation of gradients for a significant number of tokens, thereby degrading the model’s performance, while a higher value may cause instability during training.\n\n### 3.2.2. Training Details of the Second RL Stage\n\nSpecifically, we train the model using a combination of reward signals and diverse prompt distributions. For reasoning data, we follow the methodology outlined in DeepSeek-R1-Zero, which employs rule-based rewards to guide learning in mathematical, coding, and logical reasoning domains. During the training process, we observe that CoT often exhibits language mixing, particularly when RL prompts involve multiple languages. For general data, we utilize reward models to guide training. Ultimately, the integration of reward signals with diverse data distributions enables us to develop a model that not only excels in reasoning but also prioritizes helpfulness and harmlessness. Given a batch of data, the reward can be formulated as\n\n$$Reward = Reward_{\\text{reasoning}} + Reward_{\\text{general}} + Reward_{\\text{language}} \\quad (8)$$\n\n$$\\text{where, } Reward_{\\text{reasoning}} = Reward_{\\text{rule}} \\quad (9)$$\n\n$$Reward_{\\text{general}} = Reward_{\\text{reward\\_model}} + Reward_{\\text{format}} \\quad (10)$$\n\nThe second stage of RL retains most of the parameters from the first stage, with the key difference being a reduced temperature of 0.7, as we find that higher temperatures in this stage lead to incoherent generation. The stage comprises a total of 1,700 training steps, during which general instruction data and preference-based rewards are incorporated exclusively in the final 400 steps. We find that more training steps with the model based preference reward signal may lead to reward hacking, which is documented in Supplementary B.5. The total training cost is listed in Supplementary B.4.4.\n\n## 4. Experiment\n\nWe evaluate our models on MMLU (Hendrycks et al., 2021), MMLU-Redux (Gema et al., 2025), MMLU-Pro (Wang et al., 2024), C-Eval (Huang et al., 2023), and CMMLU (Li et al., 2024), IFEval (Zhou et al., 2023b), FRAMES (Krishna et al., 2024), GPQA Diamond (Rein et al., 2023), SimpleQA (OpenAI, 2024a), C-SimpleQA (He et al., 2024), SWE-Bench Verified (OpenAI, 2024b), Aider (Gauthier, 2025), LiveCodeBench (Jain et al., 2024) (2024-08 – 2025-01), Codeforces (Mirzayanov, 2025), Chinese National High School Mathematics Olympiad (CNMO 2024) (CMS, 2024), and American Invitational Mathematics Examination 2024 (AIME 2024) (MAA, 2024). The details of these benchmarks are listed in Supplementary D.\n\nTable 3 summarizes the performance of DeepSeek-R1 across multiple developmental stages, as outlined in Figure 2. A comparison between DeepSeek-R1-Zero and DeepSeek-R1 Dev1 reveals substantial improvements in instruction-following, as evidenced by higher scores on the IF-Eval and ArenaHard benchmarks. However, due to the limited size of the cold-start dataset, Dev1 exhibits a partial degradation in reasoning performance compared to DeepSeek-R1-Zero, most notably on the AIME benchmark. In contrast, DeepSeek-R1 Dev2 demonstratesTable 3 | Experimental results at each stage of DeepSeek-R1. Numbers in bold denote the performance is statistically significant (t-test with  $p < 0.01$ ).\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th colspan=\"2\">Benchmark (Metric)&lt;/th>\n&lt;th>R1-Zero&lt;/th>\n&lt;th>R1-Dev1&lt;/th>\n&lt;th>R1-Dev2&lt;/th>\n&lt;th>R1-Dev3&lt;/th>\n&lt;th>R1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td rowspan=\"10\">English&lt;/td>\n&lt;td>MMLU (EM)&lt;/td>\n&lt;td>88.8&lt;/td>\n&lt;td>89.1&lt;/td>\n&lt;td>&lt;b>91.2&lt;/b>&lt;/td>\n&lt;td>91.0&lt;/td>\n&lt;td>90.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MMLU-Redux (EM)&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>93.0&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>92.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MMLU-Pro (EM)&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>74.1&lt;/td>\n&lt;td>83.8&lt;/td>\n&lt;td>83.1&lt;/td>\n&lt;td>&lt;b>84.0&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DROP (3-shot F1)&lt;/td>\n&lt;td>89.1&lt;/td>",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 1074
    }
  },
  "sourceToolAssistantUUID": "c28aa088-a0f9-4c4c-9f0a-4e1898283153",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "812d745d-4034-4aaa-aa44-c11d91a855b1",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze DeepSeek-R1 reasoning innovation approach",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Tool call

_source line 29 · 2026-05-28T11:21:03.061Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SgwUEapFJ33yd58QanKhMp`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "812d745d-4034-4aaa-aa44-c11d91a855b1",
  "isSidechain": false,
  "requestId": "req_011CbUstXthuMN2CaDESkX8b",
  "type": "assistant",
  "uuid": "94a2a85b-247c-475b-ba14-208852a74a12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYWwYf4wYBiSDi9fRSENvp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7439,
      "cache_read_input_tokens": 16477,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7439,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 16477,
          "cache_creation_input_tokens": 7439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7439
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

_source line 30 · 2026-05-28T11:21:03.401Z_

<details><summary>↩ Tool result · `toolu_01SgwUEapFJ33yd58QanKhMp`</summary>

```text
200	&lt;td>89.1&lt;/td>
201	&lt;td>89.8&lt;/td>
202	&lt;td>91.1&lt;/td>
203	&lt;td>88.7&lt;/td>
204	&lt;td>&lt;b>92.2&lt;/b>&lt;/td>
205	&lt;/tr>
206	&lt;tr>
207	&lt;td>IF-Eval (Prompt Strict)&lt;/td>
208	&lt;td>46.6&lt;/td>
209	&lt;td>71.7&lt;/td>
210	&lt;td>72.0&lt;/td>
211	&lt;td>78.1&lt;/td>
212	&lt;td>&lt;b>83.3&lt;/b>&lt;/td>
213	&lt;/tr>
214	&lt;tr>
215	&lt;td>GPQA Diamond (Pass@1)&lt;/td>
216	&lt;td>&lt;b>75.8&lt;/b>&lt;/td>
217	&lt;td>66.1&lt;/td>
218	&lt;td>70.7&lt;/td>
219	&lt;td>71.2&lt;/td>
220	&lt;td>71.5&lt;/td>
221	&lt;/tr>
222	&lt;tr>
223	&lt;td>SimpleQA (Correct)&lt;/td>
224	&lt;td>30.3&lt;/td>
225	&lt;td>17.8&lt;/td>
226	&lt;td>28.2&lt;/td>
227	&lt;td>24.9&lt;/td>
228	&lt;td>30.1&lt;/td>
229	&lt;/tr>
230	&lt;tr>
231	&lt;td>FRAMES (Acc.)&lt;/td>
232	&lt;td>82.3&lt;/td>
233	&lt;td>78.5&lt;/td>
234	&lt;td>81.8&lt;/td>
235	&lt;td>81.9&lt;/td>
236	&lt;td>&lt;b>82.5&lt;/b>&lt;/td>
237	&lt;/tr>
238	&lt;tr>
239	&lt;td>AlpacaEval2.0 (LC-winrate)&lt;/td>
240	&lt;td>24.7&lt;/td>
241	&lt;td>50.1&lt;/td>
242	&lt;td>55.8&lt;/td>
243	&lt;td>62.1&lt;/td>
244	&lt;td>&lt;b>87.6&lt;/b>&lt;/td>
245	&lt;/tr>
246	&lt;tr>
247	&lt;td>ArenaHard (GPT-4-1106)&lt;/td>
248	&lt;td>53.6&lt;/td>
249	&lt;td>77.0&lt;/td>
250	&lt;td>73.2&lt;/td>
251	&lt;td>75.6&lt;/td>
252	&lt;td>&lt;b>92.3&lt;/b>&lt;/td>
253	&lt;/tr>
254	&lt;tr>
255	&lt;td rowspan="5">Code&lt;/td>
256	&lt;td>LiveCodeBench (Pass@1-COT)&lt;/td>
257	&lt;td>50.0&lt;/td>
258	&lt;td>57.5&lt;/td>
259	&lt;td>63.5&lt;/td>
260	&lt;td>64.6&lt;/td>
261	&lt;td>&lt;b>65.9&lt;/b>&lt;/td>
262	&lt;/tr>
263	&lt;tr>
264	&lt;td>Codeforces (Percentile)&lt;/td>
265	&lt;td>80.4&lt;/td>
266	&lt;td>84.5&lt;/td>
267	&lt;td>90.5&lt;/td>
268	&lt;td>92.1&lt;/td>
269	&lt;td>&lt;b>96.3&lt;/b>&lt;/td>
270	&lt;/tr>
271	&lt;tr>
272	&lt;td>Codeforces (Rating)&lt;/td>
273	&lt;td>1444&lt;/td>
274	&lt;td>1534&lt;/td>
275	&lt;td>1687&lt;/td>
276	&lt;td>1746&lt;/td>
277	&lt;td>&lt;b>2029&lt;/b>&lt;/td>
278	&lt;/tr>
279	&lt;tr>
280	&lt;td>SWE Verified (Resolved)&lt;/td>
281	&lt;td>43.2&lt;/td>
282	&lt;td>39.6&lt;/td>
283	&lt;td>44.6&lt;/td>
284	&lt;td>45.6&lt;/td>
285	&lt;td>&lt;b>49.2&lt;/b>&lt;/td>
286	&lt;/tr>
287	&lt;tr>
288	&lt;td>Aider-Polyglot (Acc.)&lt;/td>
289	&lt;td>12.2&lt;/td>
290	&lt;td>6.7&lt;/td>
291	&lt;td>25.6&lt;/td>
292	&lt;td>44.8&lt;/td>
293	&lt;td>&lt;b>53.3&lt;/b>&lt;/td>
294	&lt;/tr>
295	&lt;tr>
296	&lt;td rowspan="3">Math&lt;/td>
297	&lt;td>AIME 2024 (Pass@1)&lt;/td>
298	&lt;td>77.9&lt;/td>
299	&lt;td>59.0&lt;/td>
300	&lt;td>74.0&lt;/td>
301	&lt;td>78.1&lt;/td>
302	&lt;td>&lt;b>79.8&lt;/b>&lt;/td>
303	&lt;/tr>
304	&lt;tr>
305	&lt;td>MATH-500 (Pass@1)&lt;/td>
306	&lt;td>95.9&lt;/td>
307	&lt;td>94.2&lt;/td>
308	&lt;td>95.9&lt;/td>
309	&lt;td>95.4&lt;/td>
310	&lt;td>&lt;b>97.3&lt;/b>&lt;/td>
311	&lt;/tr>
312	&lt;tr>
313	&lt;td>CNMO 2024 (Pass@1)&lt;/td>
314	&lt;td>&lt;b>88.1&lt;/b>&lt;/td>
315	&lt;td>58.0&lt;/td>
316	&lt;td>73.9&lt;/td>
317	&lt;td>77.3&lt;/td>
318	&lt;td>78.8&lt;/td>
319	&lt;/tr>
320	&lt;tr>
321	&lt;td rowspan="3">Chinese&lt;/td>
322	&lt;td>CLUEWSC (EM)&lt;/td>
323	&lt;td>93.1&lt;/td>
324	&lt;td>92.8&lt;/td>
325	&lt;td>92.6&lt;/td>
326	&lt;td>91.6&lt;/td>
327	&lt;td>92.8&lt;/td>
328	&lt;/tr>
329	&lt;tr>
330	&lt;td>C-Eval (EM)&lt;/td>
331	&lt;td>&lt;b>92.8&lt;/b>&lt;/td>
332	&lt;td>85.7&lt;/td>
333	&lt;td>91.9&lt;/td>
334	&lt;td>86.4&lt;/td>
335	&lt;td>91.8&lt;/td>
336	&lt;/tr>
337	&lt;tr>
338	&lt;td>C-SimpleQA (Correct)&lt;/td>
339	&lt;td>66.4&lt;/td>
340	&lt;td>58.8&lt;/td>
341	&lt;td>64.2&lt;/td>
342	&lt;td>66.9&lt;/td>
343	&lt;td>63.7&lt;/td>
344	&lt;/tr>
345	&lt;/tbody>
346	&lt;/table>
347	
348	marked performance enhancements on benchmarks that require advanced reasoning skills, including those focused on code generation, mathematical problem solving, and STEM-related tasks. Benchmarks targeting general-purpose tasks, such as AlpacaEval 2.0, show marginal improvement. These results suggest that reasoning-oriented RL considerably enhances reasoning capabilities while exerting limited influence on user preference-oriented benchmarks.
349	
350	DeepSeek-R1 Dev3 integrates both reasoning and non-reasoning datasets into the SFT pipeline, thereby enhancing the model’s proficiency in both reasoning and general language generation tasks. Compared to Dev2, DeepSeek-R1 Dev3 achieves notable performance improvements on AlpacaEval 2.0 and Aider-Polyglot, attributable to the inclusion of large-scale non-reasoning corpora and code engineering datasets. Finally, comprehensive RL training on DeepSeek-R1 Dev3 using mixed reasoning-focused and general-purpose data produced the final DeepSeek-R1. Marginal improvements occurred in code and mathematics benchmarks, as substantial reasoning-specific RL was done in prior stages. The primary advancements in the final DeepSeek-R1 were in general instruction-following and user-preference benchmarks, with AlpacaEval 2.0 improving by 25% and ArenaHard by 17%.
351	
352	In addition, we compare DeepSeek-R1 with other models in Supplementary D.2. Model safety evaluations are provided in Supplementary D.3. A comprehensive analysis is provided in Supplementary E, including a comparison with DeepSeek-V3, performance evaluations on both fresh test sets, a breakdown of mathematical capabilities by category, and an investigation of test-time scaling behavior. Supplementary F shows that the strong reasoning capability can be transferred to smaller models.## 5. Ethics and Safety Statement
353	
354	With the advancement in the reasoning capabilities of DeepSeek-R1, we deeply recognize the potential ethical risks. For example, R1 can be subject to jailbreak attacks, leading to the generation of dangerous content such as explosive manufacturing plans, while the enhanced reasoning capabilities enable the model to provide plans with better operational feasibility and executability. Besides, a public model is also vulnerable to further fine-tuning that could compromise inherent safety protections.
355	
356	In Supplementary D.3, we present a comprehensive safety report from multiple perspectives, including performance on open-source and in-house safety evaluation benchmarks, and safety levels across multiple languages and against jailbreak attacks. These comprehensive safety analyses conclude that the inherent safety level of the DeepSeek-R1 model, compared to other state-of-the-art models, is generally at a moderate level (comparable to GPT-4o (2024-05-13)). Besides, when coupled with the risk control system, the model’s safety level is elevated to a superior standard.
357	
358	## 6. Conclusion, Limitation, and Future Work
359	
360	We present DeepSeek-R1-Zero and DeepSeek-R1, which rely on large-scale RL to incentivize model reasoning behaviors. Our results demonstrate that pre-trained checkpoints inherently possess substantial potential for complex reasoning tasks. We believe that the key to unlocking this potential lies not in large-scale human annotation but in the provision of hard reasoning questions, a reliable verifier, and sufficient computational resources for reinforcement learning. Sophisticated reasoning behaviors, such as self-verification and reflection, appeared to emerge organically during the reinforcement learning process.
361	
362	Even if DeepSeek-R1 achieves frontier results on reasoning benchmarks, it still faces several capability limitations, as outlined below:
363	
364	**Structure Output and Tool Use:** Currently, the structural output capabilities of DeepSeek-R1 remain suboptimal compared to existing models. Moreover, DeepSeek-R1 cannot leverage tools, such as search engines and calculators, to improve the performance of output. However, as it is not hard to build an RL environment for structure output and tool use, we believe the issue will be addressed in the next version.
365	
366	**Token efficiency:** Unlike conventional test-time computation scaling approaches, such as majority voting or Monte Carlo Tree Search (MCTS), DeepSeek-R1 dynamically allocates computational resources during inference according to the complexity of the problem at hand. Specifically, it uses fewer tokens to solve simple tasks, while generating more tokens for complex tasks. Nevertheless, there remains room for further optimization in terms of token efficiency, as instances of excessive reasoning—manifested as overthinking—are still observed in response to simpler questions.
367	
368	**Language Mixing:** DeepSeek-R1 is currently optimized for Chinese and English, which may result in language mixing issues when handling queries in other languages. For instance, DeepSeek-R1 might use English for reasoning and responses, even if the query is in a language other than English or Chinese. We aim to address this limitation in future updates. The limitation may be related to the base checkpoint, DeepSeek-V3-Base, mainly utilizes Chinese and English, so that it can achieve better results with the two languages in reasoning.
369	
370	**Prompting Engineering:** When evaluating DeepSeek-R1, we observe that it is sensitive toprompts. Few-shot prompting consistently degrades its performance. Therefore, we recommend users directly describe the problem and specify the output format using a zero-shot setting for optimal results.
371	
372	**Software Engineering Tasks:** Due to the long evaluation times, which impact the efficiency of the RL process, large-scale RL has not been applied extensively in software engineering tasks. As a result, DeepSeek-R1 has not demonstrated a huge improvement over DeepSeek-V3 on software engineering benchmarks. Future versions will address this by implementing rejection sampling on software engineering data or incorporating asynchronous evaluations during the RL process to improve efficiency.
373	
374	Beyond specific capability limitations, the pure RL methodology itself also presents inherent challenges:
375	
376	**Reward Hacking:** The success of pure RL depends on reliable reward signals. In this study, we ensure reward reliability through a reasoning-domain rule-based reward model (RM). However, such dependable RMs are difficult to construct for certain tasks, such as writing. If the reward signal is assigned by a model instead of predefined rules, it becomes more susceptible to exploitation as training progresses, which means the policy model may find shortcuts to hack the reward model. Consequently, for complex tasks that cannot be effectively evaluated by a reliable reward model, scaling up pure RL methods remains an open challenge.
377	
378	In this work, for tasks that cannot obtain a reliable signal, DeepSeek-R1 uses human annotation to create supervised data, and only conduct RL for hundreds of steps. We hope in the future, a robust reward model can be obtained to address such issues.
379	
380	With the advent of pure RL methods like DeepSeek-R1, the future holds immense potential for solving any task that can be effectively evaluated by a verifier, regardless of its complexity for humans. Machines equipped with such advanced RL techniques are poised to surpass human capabilities in these domains, driven by their ability to optimize performance iteratively through trial and error. However, challenges remain for tasks where constructing a reliable reward model is inherently difficult. In such cases, the lack of a robust feedback mechanism may hinder progress, suggesting that future research should focus on developing innovative approaches to define and refine reward structures for these complex, less verifiable problems.
381	
382	Furthermore, leveraging tools during the reasoning process holds significant promise. Whether it's utilizing tools like compilers or search engines to retrieve or compute necessary information, or employing external tools—such as biological or chemical reagents, to validate final results in the real world, this integration of tool-augmented reasoning could dramatically enhance the scope and accuracy of machine-driven solutions.
383	
384	## 7. Author List
385	
386	The list of authors is organized by contribution role, with individuals listed alphabetically by their first name within each category. Authors marked with an asterisk (\*) are no longer affiliated with our team.
387	
388	**Core Contributors:** Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang, Shirong Ma, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z.F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao,
389	
390	**Contributions of the Core Authors:** Peiyi Wang and Daya Guo jointly demonstrated that outcome-based RL induces the emergence of long Chain-of-Thought patterns in LLMs, achievingbreakthrough reasoning capabilities. They contributed equally to the creation of R1-Zero, and their work laid the foundation for R1. Daya Guo also contributed to the RL training stability of MOE models. Junxiao Song proposed the GRPO algorithm, implemented the initial version, and introduced rule-based rewards for math tasks. The GRPO algorithm was subsequently refined by Peiyi Wang and Runxin Xu. Zhibin Gou proposed a large PPO clipping strategy to enhance GRPO performance, demonstrating its significance alongside Zhihong Shao and Junxiao Song. Regarding data iteration, reward design, and evaluation, specific teams led efforts across different domains: Qihao Zhu, Z.F. Wu, and Dejian Yang focused on code tasks; Zhihong Shao, Zhibin Gou, and Junxiao Song focused on math tasks; and Peiyi Wang, Ruoyu Zhang, Runxin Xu, and Yu Wu led efforts for other reasoning and general tasks. Additionally, Qihao Zhu and Zhihong Shao contributed to the data selection strategy for RL training, while Zhuoshu Li and Yu Wu co-led the data labeling efforts for the entire project. On the system side, Xiao Bi, Xingkai Yu, Shirong Ma, Xiaokang Zhang, Haowei Zhang, and Ziyi Gao implemented the RL pipeline, optimizing system efficiency and addressing stability issues in large-scale training. Finally, Zhibin Gou, Daya Guo, and Ruoyu Zhang oversaw the final training phase and monitored the model training dynamics. Zhibin Gou led the development of the R1-distill series.
391	
392	**Contributors:** Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo\*, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Hanwei Xu, Honghui Ding, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jingchang Chen, Jingyang Yuan, Jinhao Tu, Junjie Qiu, Junlong Li, J.L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu\*, Kaichao You, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Mingxu Zhou, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R.J. Chen, R.L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S.S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu\*, Wentao Zhang, W.L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X.Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y.K. Li, Y.Q. Wang, Y.X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma\*, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y.X. Zhu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z.Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu\*, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, Zhen Zhang,## Appendix
393	
394	### A. Background
395	
396	#### A.1. DeepSeek-V3
397	
398	DeepSeek V3 (DeepSeek-AI, 2024b) is an advanced open-source LLM developed by DeepSeek. Released in December 2024, DeepSeek V3 represents a significant leap forward in AI innovation, designed to rival leading models like OpenAI’s GPT-4 and Meta’s Llama 3.1, while maintaining remarkable cost efficiency and performance. Built on a Mixture-of-Experts (MoE) architecture, DeepSeek V3 has 671 billion total parameters, with 37 billion activated per token, optimizing both efficiency and capability. It was pre-trained on an expansive dataset of 14.8 trillion high-quality, diverse tokens, followed by supervised fine-tuning and reinforcement learning to enhance its abilities across various domains. The model incorporates innovative features like Multi-head Latent Attention (MLA) (DeepSeek-AI, 2024a) for efficient inference, an auxiliary-loss-free load-balancing strategy, and Multi-Token Prediction (MTP) (Gloeckle et al., 2024) to boost performance, particularly in tasks like mathematics and coding.
399	
400	For the training data of DeepSeek-V3-Base, we exclusively use plain web pages and e-books, without incorporating any synthetic data. However, we have observed that some web pages contain a significant number of OpenAI-model-generated answers, which may lead the base model to acquire knowledge from other powerful models indirectly. However, we did not intentionally include synthetic data generated by OpenAI during the pre-training cooldown phase; all data used in this phase were naturally occurring and collected through web crawling. The pre-training dataset contains a substantial amount of mathematical and code-related content, indicating that DeepSeek-V3-Base has been exposed to a significant volume of reasoning trace data. This extensive exposure equips the model with the capability to generate plausible solution candidates, from which reinforcement learning can effectively identify and optimize high-quality outputs. We did the data contamination in pre-training as described in Appendix D.1. The training data of DeepSeek-V3 base are mostly Chinese and English, which might be the cause for DeepSeek-R1-Zero language mixing when the language consistent reward is absent.
401	
402	In this paper, we use the notation DeepSeek-V3-Base as the base model, DeepSeek-V3 as the instructed model. Notably, DeepSeek-R1 and DeepSeek-R1-Zero are trained on top of DeepSeek-V3-Base and DeepSeek-R1 leverages non-reasoning data from DeepSeek-V3 SFT data. DeepSeek-R1-Dev1, DeepSeek-R1-Dev2, DeepSeek-R1-Dev3 are intermediate checkpoints of DeepSeek-R1.
403	
404	#### A.2. Conventional Post-Training Paradigm
405	
406	Post-training has emerged as an essential step in refining pre-trained LLMs to meet specific performance goals and align with human expectations. A widely adopted two-stage post-training framework is SFT followed by RL (Ouyang et al., 2022).
407	
408	Supervised Fine-Tuning refines a pre-trained LLM by training it on a curated dataset of input-output pairs tailored to specific tasks. The process employs a supervised learning objective, typically minimizing cross-entropy loss between the model’s predictions and labeled ground truth (Brown et al., 2020). For instance, in conversational applications, SFT might utilize dialogue datasets where desired responses are explicitly provided, enabling the model to adapt its outputs to predefined standards (Radford et al., 2019). SFT offers several compelling benefits. First, it achieves precise task alignment by leveraging high-quality examples, allowing the model toexcel in domains such as customer support or technical documentation (Radford et al., 2019). Second, its reliance on pre-trained weights ensures computational efficiency, requiring fewer resources than training from scratch. Finally, the use of explicit input-output mappings enhances interpretability, as the model’s learning process is directly tied to observable data, minimizing the risk of erratic behavior (Ouyang et al., 2022). Despite its strengths, the performance of SFT hinges on the quality and diversity of the training dataset; narrow or biased data can impair the model’s ability to generalize to novel contexts (Brown et al., 2020). Additionally, SFT’s static nature—optimizing for fixed outputs—may fail to capture evolving human preferences or nuanced objectives. The labor-intensive process of curating high-quality datasets further complicates its scalability, as errors or inconsistencies in the data can propagate into the model’s behavior (Ouyang et al., 2022).
409	
410	Following SFT, Reinforcement Learning further refines the LLM by optimizing its outputs against a reward signal. In this stage, the model interacts with an environment—often a reward model trained on human feedback—and adjusts its behavior to maximize cumulative rewards. A prominent instantiation of this approach is Reinforcement Learning from Human Feedback (RLHF), where the reward function encodes human preferences (Christiano et al., 2017). RL thus shifts the focus from static supervision to dynamic optimization. Notably, RL reduces the need for extensive annotated resources; while SFT demands a fully labeled dataset for every input-output pair, RL can operate with a smaller set of human evaluations or a trained reward model, even rule-based reward model, significantly lowering the annotation burden.
411	
412	The sequential application of SFT and RL combines their complementary strengths. SFT establishes a robust, task-specific baseline by grounding the model in curated examples, while RL refines this foundation to align with broader, human-centric objectives (Ouyang et al., 2022). For example, SFT might ensure grammatical accuracy in a dialogue system, while RL optimizes for engagement and brevity, as demonstrated in the development of InstructGPT (Ouyang et al., 2022). This hybrid approach has proven effective in producing models that are both precise and adaptable.
413	
414	In this study, we demonstrate that the SFT stage may impede a model’s ability to explore and develop effective reasoning strategies. This limitation arises because human-provided responses, which serve as targets during SFT, are not always optimal for model learning; they often omit critical reasoning components such as explicit reflection and verification steps. To address this, DeepSeek-R1-Zero enables direct exploration of reasoning patterns by the model itself, independent of human priors. The reasoning trajectories discovered through this self-exploration are subsequently distilled and used to train other models, thereby promoting the acquisition of more robust and generalizable reasoning capabilities.
415	
416	### A.3. A Comparison of GRPO and PPO
417	
418	Group Relative Policy Optimization (GRPO) (Shao et al., 2024) is the reinforcement learning algorithm that we adopt to train DeepSeek-R1-Zero and DeepSeek-R1. It was originally proposed to simplify the training process and reduce the resource consumption of Proximal Policy Optimization (PPO) (Schulman et al., 2017), which is widely used in the RL stage of LLMs (Ouyang et al., 2022). For an overall comparison between GRPO and PPO, see Figure 3.
419	
420	For each question  $q$ , GRPO samples a group of outputs  $\{o_1, o_2, \dots, o_G\}$  from the old policyFigure 3 | Demonstration of PPO and our GRPO. GRPO foregoes the value model, instead estimating the advantages from group scores.
421	
422	$\pi_{\theta_{old}}$  and then optimizes the policy model  $\pi_{\theta}$  by maximizing the following objective:
423	
424	$$\mathcal{J}_{GRPO}(\theta) = \mathbb{E}[q \sim P(Q), \{o_i\}_{i=1}^G \sim \pi_{\theta_{old}}(O|q)] \frac{1}{G} \sum_{i=1}^G \left( \min \left( \frac{\pi_{\theta}(o_i|q)}{\pi_{\theta_{old}}(o_i|q)} A_i, \text{clip} \left( \frac{\pi_{\theta}(o_i|q)}{\pi_{\theta_{old}}(o_i|q)}, 1 - \varepsilon, 1 + \varepsilon \right) A_i \right) - \beta \mathbb{D}_{KL}(\pi_{\theta} || \pi_{ref}) \right), \quad (11)$$
425	
426	$$\mathbb{D}_{KL}(\pi_{\theta} || \pi_{ref}) = \frac{\pi_{ref}(o_i|q)}{\pi_{\theta}(o_i|q)} - \log \frac{\pi_{ref}(o_i|q)}{\pi_{\theta}(o_i|q)} - 1, \quad (12)$$
427	
428	where  $\pi_{ref}$  is a reference policy,  $\varepsilon$  and  $\beta$  are hyper-parameters, and  $A_i$  is the advantage, computed using a group of rewards  $\{r_1, r_2, \dots, r_G\}$  corresponding to the outputs within each group:
429	
430	$$A_i = \frac{r_i - \text{mean}(\{r_1, r_2, \dots, r_G\})}{\text{std}(\{r_1, r_2, \dots, r_G\})}. \quad (13)$$
431	
432	In contrast, in PPO, the advantage is typically computed by applying the Generalized Advantage Estimation (GAE) (Schulman et al., 2015), based not only on the rewards but also on a learned value model. Since the value model is usually of similar size as the policy model, it introduces a significant memory and computational overhead. Additionally, the training objective of the value model is to predict the expected cumulative reward from the current position onward, based on the tokens generated from the beginning up to the current position. This is inherently difficult, especially when only the final outcome reward is available. The challenge becomes even more pronounced when training long chain-of-thought reasoning models. As the output length increases, the model is more likely to engage in behaviors such as reflection and revision during generation, meaning that the content initially generated may later be revised or contradicted, which makes it even less feasible to predict the final reward based on a partial response.
433	
434	Another key difference between GRPO and PPO is how Kullback–Leibler (KL) divergence between the trained policy and the reference policy is incorporated into the training process. In GRPO, an unbiased estimator of the KL divergence (Schulman, 2020) is directly added in the loss as in equation 11, while in PPO the per-token KL penalty is added as a dense reward at each token (Ouyang et al., 2022). Since the optimization goal of reinforcement learning is toFigure 4 | Performance of PPO and GRPO on the MATH task.
435	
436	maximize cumulative rewards, PPO’s approach penalizes the cumulative KL divergence, which may implicitly penalize the length of the response and thereby prevent the model’s response length from increasing. In addition, as we may train thousands of steps in the scenario of training long chain-of-thought reasoning models, the trained policy can diverge significantly from the initial reference policy. In order to balance the scope that the training policy can explore and the stability of the training, we periodically update the reference policy to the latest policy during the actual training process.
437	
438	Figure 4 compares the performance of PPO and GRPO on the MATH task using DeepSeek-Coder-V2-Lite (16B MoE with 2.4B active parameters). Unlike GRPO, PPO requires additional hyperparameter tuning—particularly of the  $\lambda$  coefficient in GAE—and is highly sensitive to this parameter. When  $\lambda$  is set to 0.95 (the default value in most open-source PPO implementations), PPO performs considerably worse than GRPO. However, with careful tuning (setting  $\lambda$  to 1.0), PPO’s performance improves substantially, nearing that of GRPO.
439	
440	While PPO can achieve comparable performance when appropriately tuned, it demands additional computational cost for hyperparameter optimization. Moreover, considering the memory and computational overhead associated with training an additional value model, GRPO presents a more practical alternative, especially when training large-scale models with constrained resources.Figure 5 | Overview of our RL framework.
441	
442	## B. Training Details
443	
444	### B.1. RL Infrastructure
445	
446	Conducting RL training on large models places high demands on the infrastructure. Our RL framework is architected with a decoupled and extensible structure to facilitate seamless integration of diverse models and algorithms. Within this framework, we have incorporated both intra-modular and inter-modular optimization techniques, to ensure training efficiency and scalability.
447	
448	Specifically, as depicted in Figure 5, the framework is partitioned into four distinct modules, each corresponding to a specific phase of the RL pipeline:
449	
450	- • **Rollout Module:** Prompts are loaded from training dataset and uniformly dispatched across multiple vLLM (Kwon et al., 2023) workers, each equipped with the actor model, to sample multiple responses. For DeepSeek-V3 MoE architecture, we implement an expert parallelism strategy across nodes to reduce memory access overhead, and deploy redundant copies of hotspot experts to balance computational loads among different experts. Multi-Token Prediction (MTP) component is also leveraged for self-speculative decoding, significantly accelerating the decoding speed and effectively minimizing the completion time for the longest samples.
451	- • **Inference Module:** This module loads the reward model and reference to perform a forward pass on the samples generated during the rollout phase, thereby obtaining model-based rewards and other essential information.
452	- • **Rule-based Reward Module:** This module computes rule-based rewards for the model-generated responses. A unified interface has been designed to accommodate diverse implementations (e.g., code executor, answer matcher, format checker, etc.). Although this module does not require loading models into GPU memory, its execution tends to be time-consuming. To tackle this issue, an asynchronous scheduling approach is employed to overlap its execution with the Rollout and Inference modules, effectively hiding theassociated latency.
453	
454	- • **Training Module:** This module loads the actor model and the critic model (if required), to compute loss and update model parameters. It provides flexible support for a variety of RL algorithms (e.g., PPO, GRPO, DPO, etc.). To minimize computational waste caused by sequence padding and balance the workload across devices, we design the following data packing strategy: first, all data in a global batch is sorted by length and distributed across processes within the data parallel group; subsequently, within each process, the Best-Fit strategy is applied to pack the data into fixed-length chunks with minimal padding; finally, the number of chunks is adjusted to be equal across all processes. Additionally, we have integrated the DualPipe algorithm, utilized in DeepSeek-V3 training, to achieve efficient pipeline parallelism.
455	
456	Notably, upon completion of each module (excluding the Rule-based Reward module), the model instances utilized in that phase are automatically offloaded from VRAM to either system memory or disk storage, thereby freeing up VRAM for the subsequent phase.
457	
458	## B.2. Reward Model Prompt
459	
460	Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user prompt displayed below. You will be given assistant A's answer and assistant B's answer. Your job is to evaluate which assistant's answer is better. Begin your evaluation by generating your own answer to the prompt. You must provide your answers before judging any answers.
461	
462	When evaluating the assistants' answers, compare both assistants' answers with your answer. You must identify and correct any mistakes or inaccurate information.
463	
464	Then consider if the assistant's answers are helpful, relevant, and concise. Helpful means the answer correctly responds to the prompt or follows the instructions. Note when user prompt has any ambiguity or more than one interpretation, it is more helpful and appropriate to ask for clarifications or more information from the user than providing an answer based on assumptions. Relevant means all parts of the response closely connect or are appropriate to what is being asked. Concise means the response is clear and not verbose or excessive.
465	
466	Then consider the creativity and novelty of the assistant's answers when needed. Finally, identify any missing important information in the assistants' answers that would be beneficial to include when responding to the user prompt.
467	
468	After providing your explanation, you must output only one of the following choices as your final verdict with a label:
469	
470	1. 1. Assistant A is significantly better: [[A>>B]]
471	2. 2. Assistant A is slightly better: [[A>B]]
472	3. 3. Tie, relatively the same: [[A=B]]
473	4. 4. Assistant B is slightly better: [[B>A]]
474	5. 5. Assistant B is significantly better: [[B>>A]]
475	
476	Example output: My final verdict is tie: [[A=B]]:Table 4 | Description of RL Data and Tasks.
477	
478	&lt;table border="1">
479	&lt;thead>
480	&lt;tr>
481	&lt;th>Data Type&lt;/th>
482	&lt;th># Prompts&lt;/th>
483	&lt;th>Question Type&lt;/th>
484	&lt;th>Output Type&lt;/th>
485	&lt;/tr>
486	&lt;/thead>
487	&lt;tbody>
488	&lt;tr>
489	&lt;td>Math&lt;/td>
490	&lt;td>26K&lt;/td>
491	&lt;td>Quantitative Reasoning&lt;/td>
492	&lt;td>Number/Expression/Equation&lt;/td>
493	&lt;/tr>
494	&lt;tr>
495	&lt;td>Code&lt;/td>
496	&lt;td>17K&lt;/td>
497	&lt;td>Algorithm and Bug Fixing&lt;/td>
498	&lt;td>Code Solution&lt;/td>
499	&lt;/tr>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94a2a85b-247c-475b-ba14-208852a74a12",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "06344df4-ba11-4af9-b7bd-76292d04e387",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt",
      "content": "&lt;td>89.1&lt;/td>\n&lt;td>89.8&lt;/td>\n&lt;td>91.1&lt;/td>\n&lt;td>88.7&lt;/td>\n&lt;td>&lt;b>92.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>IF-Eval (Prompt Strict)&lt;/td>\n&lt;td>46.6&lt;/td>\n&lt;td>71.7&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>&lt;b>83.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPQA Diamond (Pass@1)&lt;/td>\n&lt;td>&lt;b>75.8&lt;/b>&lt;/td>\n&lt;td>66.1&lt;/td>\n&lt;td>70.7&lt;/td>\n&lt;td>71.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>SimpleQA (Correct)&lt;/td>\n&lt;td>30.3&lt;/td>\n&lt;td>17.8&lt;/td>\n&lt;td>28.2&lt;/td>\n&lt;td>24.9&lt;/td>\n&lt;td>30.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>FRAMES (Acc.)&lt;/td>\n&lt;td>82.3&lt;/td>\n&lt;td>78.5&lt;/td>\n&lt;td>81.8&lt;/td>\n&lt;td>81.9&lt;/td>\n&lt;td>&lt;b>82.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AlpacaEval2.0 (LC-winrate)&lt;/td>\n&lt;td>24.7&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;td>62.1&lt;/td>\n&lt;td>&lt;b>87.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>ArenaHard (GPT-4-1106)&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>77.0&lt;/td>\n&lt;td>73.2&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>&lt;b>92.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">Code&lt;/td>\n&lt;td>LiveCodeBench (Pass@1-COT)&lt;/td>\n&lt;td>50.0&lt;/td>\n&lt;td>57.5&lt;/td>\n&lt;td>63.5&lt;/td>\n&lt;td>64.6&lt;/td>\n&lt;td>&lt;b>65.9&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Codeforces (Percentile)&lt;/td>\n&lt;td>80.4&lt;/td>\n&lt;td>84.5&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>92.1&lt;/td>\n&lt;td>&lt;b>96.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Codeforces (Rating)&lt;/td>\n&lt;td>1444&lt;/td>\n&lt;td>1534&lt;/td>\n&lt;td>1687&lt;/td>\n&lt;td>1746&lt;/td>\n&lt;td>&lt;b>2029&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>SWE Verified (Resolved)&lt;/td>\n&lt;td>43.2&lt;/td>\n&lt;td>39.6&lt;/td>\n&lt;td>44.6&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;td>&lt;b>49.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Aider-Polyglot (Acc.)&lt;/td>\n&lt;td>12.2&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;td>25.6&lt;/td>\n&lt;td>44.8&lt;/td>\n&lt;td>&lt;b>53.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Math&lt;/td>\n&lt;td>AIME 2024 (Pass@1)&lt;/td>\n&lt;td>77.9&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>74.0&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>&lt;b>79.8&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MATH-500 (Pass@1)&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>94.2&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>95.4&lt;/td>\n&lt;td>&lt;b>97.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>CNMO 2024 (Pass@1)&lt;/td>\n&lt;td>&lt;b>88.1&lt;/b>&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;td>73.9&lt;/td>\n&lt;td>77.3&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Chinese&lt;/td>\n&lt;td>CLUEWSC (EM)&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>92.8&lt;/td>\n&lt;td>92.6&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>92.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>C-Eval (EM)&lt;/td>\n&lt;td>&lt;b>92.8&lt;/b>&lt;/td>\n&lt;td>85.7&lt;/td>\n&lt;td>91.9&lt;/td>\n&lt;td>86.4&lt;/td>\n&lt;td>91.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>C-SimpleQA (Correct)&lt;/td>\n&lt;td>66.4&lt;/td>\n&lt;td>58.8&lt;/td>\n&lt;td>64.2&lt;/td>\n&lt;td>66.9&lt;/td>\n&lt;td>63.7&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nmarked performance enhancements on benchmarks that require advanced reasoning skills, including those focused on code generation, mathematical problem solving, and STEM-related tasks. Benchmarks targeting general-purpose tasks, such as AlpacaEval 2.0, show marginal improvement. These results suggest that reasoning-oriented RL considerably enhances reasoning capabilities while exerting limited influence on user preference-oriented benchmarks.\n\nDeepSeek-R1 Dev3 integrates both reasoning and non-reasoning datasets into the SFT pipeline, thereby enhancing the model’s proficiency in both reasoning and general language generation tasks. Compared to Dev2, DeepSeek-R1 Dev3 achieves notable performance improvements on AlpacaEval 2.0 and Aider-Polyglot, attributable to the inclusion of large-scale non-reasoning corpora and code engineering datasets. Finally, comprehensive RL training on DeepSeek-R1 Dev3 using mixed reasoning-focused and general-purpose data produced the final DeepSeek-R1. Marginal improvements occurred in code and mathematics benchmarks, as substantial reasoning-specific RL was done in prior stages. The primary advancements in the final DeepSeek-R1 were in general instruction-following and user-preference benchmarks, with AlpacaEval 2.0 improving by 25% and ArenaHard by 17%.\n\nIn addition, we compare DeepSeek-R1 with other models in Supplementary D.2. Model safety evaluations are provided in Supplementary D.3. A comprehensive analysis is provided in Supplementary E, including a comparison with DeepSeek-V3, performance evaluations on both fresh test sets, a breakdown of mathematical capabilities by category, and an investigation of test-time scaling behavior. Supplementary F shows that the strong reasoning capability can be transferred to smaller models.## 5. Ethics and Safety Statement\n\nWith the advancement in the reasoning capabilities of DeepSeek-R1, we deeply recognize the potential ethical risks. For example, R1 can be subject to jailbreak attacks, leading to the generation of dangerous content such as explosive manufacturing plans, while the enhanced reasoning capabilities enable the model to provide plans with better operational feasibility and executability. Besides, a public model is also vulnerable to further fine-tuning that could compromise inherent safety protections.\n\nIn Supplementary D.3, we present a comprehensive safety report from multiple perspectives, including performance on open-source and in-house safety evaluation benchmarks, and safety levels across multiple languages and against jailbreak attacks. These comprehensive safety analyses conclude that the inherent safety level of the DeepSeek-R1 model, compared to other state-of-the-art models, is generally at a moderate level (comparable to GPT-4o (2024-05-13)). Besides, when coupled with the risk control system, the model’s safety level is elevated to a superior standard.\n\n## 6. Conclusion, Limitation, and Future Work\n\nWe present DeepSeek-R1-Zero and DeepSeek-R1, which rely on large-scale RL to incentivize model reasoning behaviors. Our results demonstrate that pre-trained checkpoints inherently possess substantial potential for complex reasoning tasks. We believe that the key to unlocking this potential lies not in large-scale human annotation but in the provision of hard reasoning questions, a reliable verifier, and sufficient computational resources for reinforcement learning. Sophisticated reasoning behaviors, such as self-verification and reflection, appeared to emerge organically during the reinforcement learning process.\n\nEven if DeepSeek-R1 achieves frontier results on reasoning benchmarks, it still faces several capability limitations, as outlined below:\n\n**Structure Output and Tool Use:** Currently, the structural output capabilities of DeepSeek-R1 remain suboptimal compared to existing models. Moreover, DeepSeek-R1 cannot leverage tools, such as search engines and calculators, to improve the performance of output. However, as it is not hard to build an RL environment for structure output and tool use, we believe the issue will be addressed in the next version.\n\n**Token efficiency:** Unlike conventional test-time computation scaling approaches, such as majority voting or Monte Carlo Tree Search (MCTS), DeepSeek-R1 dynamically allocates computational resources during inference according to the complexity of the problem at hand. Specifically, it uses fewer tokens to solve simple tasks, while generating more tokens for complex tasks. Nevertheless, there remains room for further optimization in terms of token efficiency, as instances of excessive reasoning—manifested as overthinking—are still observed in response to simpler questions.\n\n**Language Mixing:** DeepSeek-R1 is currently optimized for Chinese and English, which may result in language mixing issues when handling queries in other languages. For instance, DeepSeek-R1 might use English for reasoning and responses, even if the query is in a language other than English or Chinese. We aim to address this limitation in future updates. The limitation may be related to the base checkpoint, DeepSeek-V3-Base, mainly utilizes Chinese and English, so that it can achieve better results with the two languages in reasoning.\n\n**Prompting Engineering:** When evaluating DeepSeek-R1, we observe that it is sensitive toprompts. Few-shot prompting consistently degrades its performance. Therefore, we recommend users directly describe the problem and specify the output format using a zero-shot setting for optimal results.\n\n**Software Engineering Tasks:** Due to the long evaluation times, which impact the efficiency of the RL process, large-scale RL has not been applied extensively in software engineering tasks. As a result, DeepSeek-R1 has not demonstrated a huge improvement over DeepSeek-V3 on software engineering benchmarks. Future versions will address this by implementing rejection sampling on software engineering data or incorporating asynchronous evaluations during the RL process to improve efficiency.\n\nBeyond specific capability limitations, the pure RL methodology itself also presents inherent challenges:\n\n**Reward Hacking:** The success of pure RL depends on reliable reward signals. In this study, we ensure reward reliability through a reasoning-domain rule-based reward model (RM). However, such dependable RMs are difficult to construct for certain tasks, such as writing. If the reward signal is assigned by a model instead of predefined rules, it becomes more susceptible to exploitation as training progresses, which means the policy model may find shortcuts to hack the reward model. Consequently, for complex tasks that cannot be effectively evaluated by a reliable reward model, scaling up pure RL methods remains an open challenge.\n\nIn this work, for tasks that cannot obtain a reliable signal, DeepSeek-R1 uses human annotation to create supervised data, and only conduct RL for hundreds of steps. We hope in the future, a robust reward model can be obtained to address such issues.\n\nWith the advent of pure RL methods like DeepSeek-R1, the future holds immense potential for solving any task that can be effectively evaluated by a verifier, regardless of its complexity for humans. Machines equipped with such advanced RL techniques are poised to surpass human capabilities in these domains, driven by their ability to optimize performance iteratively through trial and error. However, challenges remain for tasks where constructing a reliable reward model is inherently difficult. In such cases, the lack of a robust feedback mechanism may hinder progress, suggesting that future research should focus on developing innovative approaches to define and refine reward structures for these complex, less verifiable problems.\n\nFurthermore, leveraging tools during the reasoning process holds significant promise. Whether it's utilizing tools like compilers or search engines to retrieve or compute necessary information, or employing external tools—such as biological or chemical reagents, to validate final results in the real world, this integration of tool-augmented reasoning could dramatically enhance the scope and accuracy of machine-driven solutions.\n\n## 7. Author List\n\nThe list of authors is organized by contribution role, with individuals listed alphabetically by their first name within each category. Authors marked with an asterisk (\\*) are no longer affiliated with our team.\n\n**Core Contributors:** Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang, Shirong Ma, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z.F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao,\n\n**Contributions of the Core Authors:** Peiyi Wang and Daya Guo jointly demonstrated that outcome-based RL induces the emergence of long Chain-of-Thought patterns in LLMs, achievingbreakthrough reasoning capabilities. They contributed equally to the creation of R1-Zero, and their work laid the foundation for R1. Daya Guo also contributed to the RL training stability of MOE models. Junxiao Song proposed the GRPO algorithm, implemented the initial version, and introduced rule-based rewards for math tasks. The GRPO algorithm was subsequently refined by Peiyi Wang and Runxin Xu. Zhibin Gou proposed a large PPO clipping strategy to enhance GRPO performance, demonstrating its significance alongside Zhihong Shao and Junxiao Song. Regarding data iteration, reward design, and evaluation, specific teams led efforts across different domains: Qihao Zhu, Z.F. Wu, and Dejian Yang focused on code tasks; Zhihong Shao, Zhibin Gou, and Junxiao Song focused on math tasks; and Peiyi Wang, Ruoyu Zhang, Runxin Xu, and Yu Wu led efforts for other reasoning and general tasks. Additionally, Qihao Zhu and Zhihong Shao contributed to the data selection strategy for RL training, while Zhuoshu Li and Yu Wu co-led the data labeling efforts for the entire project. On the system side, Xiao Bi, Xingkai Yu, Shirong Ma, Xiaokang Zhang, Haowei Zhang, and Ziyi Gao implemented the RL pipeline, optimizing system efficiency and addressing stability issues in large-scale training. Finally, Zhibin Gou, Daya Guo, and Ruoyu Zhang oversaw the final training phase and monitored the model training dynamics. Zhibin Gou led the development of the R1-distill series.\n\n**Contributors:** Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo\\*, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Hanwei Xu, Honghui Ding, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jingchang Chen, Jingyang Yuan, Jinhao Tu, Junjie Qiu, Junlong Li, J.L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu\\*, Kaichao You, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Mingxu Zhou, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R.J. Chen, R.L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S.S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu\\*, Wentao Zhang, W.L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X.Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y.K. Li, Y.Q. Wang, Y.X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma\\*, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y.X. Zhu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z.Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu\\*, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, Zhen Zhang,## Appendix\n\n### A. Background\n\n#### A.1. DeepSeek-V3\n\nDeepSeek V3 (DeepSeek-AI, 2024b) is an advanced open-source LLM developed by DeepSeek. Released in December 2024, DeepSeek V3 represents a significant leap forward in AI innovation, designed to rival leading models like OpenAI’s GPT-4 and Meta’s Llama 3.1, while maintaining remarkable cost efficiency and performance. Built on a Mixture-of-Experts (MoE) architecture, DeepSeek V3 has 671 billion total parameters, with 37 billion activated per token, optimizing both efficiency and capability. It was pre-trained on an expansive dataset of 14.8 trillion high-quality, diverse tokens, followed by supervised fine-tuning and reinforcement learning to enhance its abilities across various domains. The model incorporates innovative features like Multi-head Latent Attention (MLA) (DeepSeek-AI, 2024a) for efficient inference, an auxiliary-loss-free load-balancing strategy, and Multi-Token Prediction (MTP) (Gloeckle et al., 2024) to boost performance, particularly in tasks like mathematics and coding.\n\nFor the training data of DeepSeek-V3-Base, we exclusively use plain web pages and e-books, without incorporating any synthetic data. However, we have observed that some web pages contain a significant number of OpenAI-model-generated answers, which may lead the base model to acquire knowledge from other powerful models indirectly. However, we did not intentionally include synthetic data generated by OpenAI during the pre-training cooldown phase; all data used in this phase were naturally occurring and collected through web crawling. The pre-training dataset contains a substantial amount of mathematical and code-related content, indicating that DeepSeek-V3-Base has been exposed to a significant volume of reasoning trace data. This extensive exposure equips the model with the capability to generate plausible solution candidates, from which reinforcement learning can effectively identify and optimize high-quality outputs. We did the data contamination in pre-training as described in Appendix D.1. The training data of DeepSeek-V3 base are mostly Chinese and English, which might be the cause for DeepSeek-R1-Zero language mixing when the language consistent reward is absent.\n\nIn this paper, we use the notation DeepSeek-V3-Base as the base model, DeepSeek-V3 as the instructed model. Notably, DeepSeek-R1 and DeepSeek-R1-Zero are trained on top of DeepSeek-V3-Base and DeepSeek-R1 leverages non-reasoning data from DeepSeek-V3 SFT data. DeepSeek-R1-Dev1, DeepSeek-R1-Dev2, DeepSeek-R1-Dev3 are intermediate checkpoints of DeepSeek-R1.\n\n#### A.2. Conventional Post-Training Paradigm\n\nPost-training has emerged as an essential step in refining pre-trained LLMs to meet specific performance goals and align with human expectations. A widely adopted two-stage post-training framework is SFT followed by RL (Ouyang et al., 2022).\n\nSupervised Fine-Tuning refines a pre-trained LLM by training it on a curated dataset of input-output pairs tailored to specific tasks. The process employs a supervised learning objective, typically minimizing cross-entropy loss between the model’s predictions and labeled ground truth (Brown et al., 2020). For instance, in conversational applications, SFT might utilize dialogue datasets where desired responses are explicitly provided, enabling the model to adapt its outputs to predefined standards (Radford et al., 2019). SFT offers several compelling benefits. First, it achieves precise task alignment by leveraging high-quality examples, allowing the model toexcel in domains such as customer support or technical documentation (Radford et al., 2019). Second, its reliance on pre-trained weights ensures computational efficiency, requiring fewer resources than training from scratch. Finally, the use of explicit input-output mappings enhances interpretability, as the model’s learning process is directly tied to observable data, minimizing the risk of erratic behavior (Ouyang et al., 2022). Despite its strengths, the performance of SFT hinges on the quality and diversity of the training dataset; narrow or biased data can impair the model’s ability to generalize to novel contexts (Brown et al., 2020). Additionally, SFT’s static nature—optimizing for fixed outputs—may fail to capture evolving human preferences or nuanced objectives. The labor-intensive process of curating high-quality datasets further complicates its scalability, as errors or inconsistencies in the data can propagate into the model’s behavior (Ouyang et al., 2022).\n\nFollowing SFT, Reinforcement Learning further refines the LLM by optimizing its outputs against a reward signal. In this stage, the model interacts with an environment—often a reward model trained on human feedback—and adjusts its behavior to maximize cumulative rewards. A prominent instantiation of this approach is Reinforcement Learning from Human Feedback (RLHF), where the reward function encodes human preferences (Christiano et al., 2017). RL thus shifts the focus from static supervision to dynamic optimization. Notably, RL reduces the need for extensive annotated resources; while SFT demands a fully labeled dataset for every input-output pair, RL can operate with a smaller set of human evaluations or a trained reward model, even rule-based reward model, significantly lowering the annotation burden.\n\nThe sequential application of SFT and RL combines their complementary strengths. SFT establishes a robust, task-specific baseline by grounding the model in curated examples, while RL refines this foundation to align with broader, human-centric objectives (Ouyang et al., 2022). For example, SFT might ensure grammatical accuracy in a dialogue system, while RL optimizes for engagement and brevity, as demonstrated in the development of InstructGPT (Ouyang et al., 2022). This hybrid approach has proven effective in producing models that are both precise and adaptable.\n\nIn this study, we demonstrate that the SFT stage may impede a model’s ability to explore and develop effective reasoning strategies. This limitation arises because human-provided responses, which serve as targets during SFT, are not always optimal for model learning; they often omit critical reasoning components such as explicit reflection and verification steps. To address this, DeepSeek-R1-Zero enables direct exploration of reasoning patterns by the model itself, independent of human priors. The reasoning trajectories discovered through this self-exploration are subsequently distilled and used to train other models, thereby promoting the acquisition of more robust and generalizable reasoning capabilities.\n\n### A.3. A Comparison of GRPO and PPO\n\nGroup Relative Policy Optimization (GRPO) (Shao et al., 2024) is the reinforcement learning algorithm that we adopt to train DeepSeek-R1-Zero and DeepSeek-R1. It was originally proposed to simplify the training process and reduce the resource consumption of Proximal Policy Optimization (PPO) (Schulman et al., 2017), which is widely used in the RL stage of LLMs (Ouyang et al., 2022). For an overall comparison between GRPO and PPO, see Figure 3.\n\nFor each question  $q$ , GRPO samples a group of outputs  $\\{o_1, o_2, \\dots, o_G\\}$  from the old policyFigure 3 | Demonstration of PPO and our GRPO. GRPO foregoes the value model, instead estimating the advantages from group scores.\n\n$\\pi_{\\theta_{old}}$  and then optimizes the policy model  $\\pi_{\\theta}$  by maximizing the following objective:\n\n$$\\mathcal{J}_{GRPO}(\\theta) = \\mathbb{E}[q \\sim P(Q), \\{o_i\\}_{i=1}^G \\sim \\pi_{\\theta_{old}}(O|q)] \\frac{1}{G} \\sum_{i=1}^G \\left( \\min \\left( \\frac{\\pi_{\\theta}(o_i|q)}{\\pi_{\\theta_{old}}(o_i|q)} A_i, \\text{clip} \\left( \\frac{\\pi_{\\theta}(o_i|q)}{\\pi_{\\theta_{old}}(o_i|q)}, 1 - \\varepsilon, 1 + \\varepsilon \\right) A_i \\right) - \\beta \\mathbb{D}_{KL}(\\pi_{\\theta} || \\pi_{ref}) \\right), \\quad (11)$$\n\n$$\\mathbb{D}_{KL}(\\pi_{\\theta} || \\pi_{ref}) = \\frac{\\pi_{ref}(o_i|q)}{\\pi_{\\theta}(o_i|q)} - \\log \\frac{\\pi_{ref}(o_i|q)}{\\pi_{\\theta}(o_i|q)} - 1, \\quad (12)$$\n\nwhere  $\\pi_{ref}$  is a reference policy,  $\\varepsilon$  and  $\\beta$  are hyper-parameters, and  $A_i$  is the advantage, computed using a group of rewards  $\\{r_1, r_2, \\dots, r_G\\}$  corresponding to the outputs within each group:\n\n$$A_i = \\frac{r_i - \\text{mean}(\\{r_1, r_2, \\dots, r_G\\})}{\\text{std}(\\{r_1, r_2, \\dots, r_G\\})}. \\quad (13)$$\n\nIn contrast, in PPO, the advantage is typically computed by applying the Generalized Advantage Estimation (GAE) (Schulman et al., 2015), based not only on the rewards but also on a learned value model. Since the value model is usually of similar size as the policy model, it introduces a significant memory and computational overhead. Additionally, the training objective of the value model is to predict the expected cumulative reward from the current position onward, based on the tokens generated from the beginning up to the current position. This is inherently difficult, especially when only the final outcome reward is available. The challenge becomes even more pronounced when training long chain-of-thought reasoning models. As the output length increases, the model is more likely to engage in behaviors such as reflection and revision during generation, meaning that the content initially generated may later be revised or contradicted, which makes it even less feasible to predict the final reward based on a partial response.\n\nAnother key difference between GRPO and PPO is how Kullback–Leibler (KL) divergence between the trained policy and the reference policy is incorporated into the training process. In GRPO, an unbiased estimator of the KL divergence (Schulman, 2020) is directly added in the loss as in equation 11, while in PPO the per-token KL penalty is added as a dense reward at each token (Ouyang et al., 2022). Since the optimization goal of reinforcement learning is toFigure 4 | Performance of PPO and GRPO on the MATH task.\n\nmaximize cumulative rewards, PPO’s approach penalizes the cumulative KL divergence, which may implicitly penalize the length of the response and thereby prevent the model’s response length from increasing. In addition, as we may train thousands of steps in the scenario of training long chain-of-thought reasoning models, the trained policy can diverge significantly from the initial reference policy. In order to balance the scope that the training policy can explore and the stability of the training, we periodically update the reference policy to the latest policy during the actual training process.\n\nFigure 4 compares the performance of PPO and GRPO on the MATH task using DeepSeek-Coder-V2-Lite (16B MoE with 2.4B active parameters). Unlike GRPO, PPO requires additional hyperparameter tuning—particularly of the  $\\lambda$  coefficient in GAE—and is highly sensitive to this parameter. When  $\\lambda$  is set to 0.95 (the default value in most open-source PPO implementations), PPO performs considerably worse than GRPO. However, with careful tuning (setting  $\\lambda$  to 1.0), PPO’s performance improves substantially, nearing that of GRPO.\n\nWhile PPO can achieve comparable performance when appropriately tuned, it demands additional computational cost for hyperparameter optimization. Moreover, considering the memory and computational overhead associated with training an additional value model, GRPO presents a more practical alternative, especially when training large-scale models with constrained resources.Figure 5 | Overview of our RL framework.\n\n## B. Training Details\n\n### B.1. RL Infrastructure\n\nConducting RL training on large models places high demands on the infrastructure. Our RL framework is architected with a decoupled and extensible structure to facilitate seamless integration of diverse models and algorithms. Within this framework, we have incorporated both intra-modular and inter-modular optimization techniques, to ensure training efficiency and scalability.\n\nSpecifically, as depicted in Figure 5, the framework is partitioned into four distinct modules, each corresponding to a specific phase of the RL pipeline:\n\n- • **Rollout Module:** Prompts are loaded from training dataset and uniformly dispatched across multiple vLLM (Kwon et al., 2023) workers, each equipped with the actor model, to sample multiple responses. For DeepSeek-V3 MoE architecture, we implement an expert parallelism strategy across nodes to reduce memory access overhead, and deploy redundant copies of hotspot experts to balance computational loads among different experts. Multi-Token Prediction (MTP) component is also leveraged for self-speculative decoding, significantly accelerating the decoding speed and effectively minimizing the completion time for the longest samples.\n- • **Inference Module:** This module loads the reward model and reference to perform a forward pass on the samples generated during the rollout phase, thereby obtaining model-based rewards and other essential information.\n- • **Rule-based Reward Module:** This module computes rule-based rewards for the model-generated responses. A unified interface has been designed to accommodate diverse implementations (e.g., code executor, answer matcher, format checker, etc.). Although this module does not require loading models into GPU memory, its execution tends to be time-consuming. To tackle this issue, an asynchronous scheduling approach is employed to overlap its execution with the Rollout and Inference modules, effectively hiding theassociated latency.\n\n- • **Training Module:** This module loads the actor model and the critic model (if required), to compute loss and update model parameters. It provides flexible support for a variety of RL algorithms (e.g., PPO, GRPO, DPO, etc.). To minimize computational waste caused by sequence padding and balance the workload across devices, we design the following data packing strategy: first, all data in a global batch is sorted by length and distributed across processes within the data parallel group; subsequently, within each process, the Best-Fit strategy is applied to pack the data into fixed-length chunks with minimal padding; finally, the number of chunks is adjusted to be equal across all processes. Additionally, we have integrated the DualPipe algorithm, utilized in DeepSeek-V3 training, to achieve efficient pipeline parallelism.\n\nNotably, upon completion of each module (excluding the Rule-based Reward module), the model instances utilized in that phase are automatically offloaded from VRAM to either system memory or disk storage, thereby freeing up VRAM for the subsequent phase.\n\n## B.2. Reward Model Prompt\n\nPlease act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user prompt displayed below. You will be given assistant A's answer and assistant B's answer. Your job is to evaluate which assistant's answer is better. Begin your evaluation by generating your own answer to the prompt. You must provide your answers before judging any answers.\n\nWhen evaluating the assistants' answers, compare both assistants' answers with your answer. You must identify and correct any mistakes or inaccurate information.\n\nThen consider if the assistant's answers are helpful, relevant, and concise. Helpful means the answer correctly responds to the prompt or follows the instructions. Note when user prompt has any ambiguity or more than one interpretation, it is more helpful and appropriate to ask for clarifications or more information from the user than providing an answer based on assumptions. Relevant means all parts of the response closely connect or are appropriate to what is being asked. Concise means the response is clear and not verbose or excessive.\n\nThen consider the creativity and novelty of the assistant's answers when needed. Finally, identify any missing important information in the assistants' answers that would be beneficial to include when responding to the user prompt.\n\nAfter providing your explanation, you must output only one of the following choices as your final verdict with a label:\n\n1. 1. Assistant A is significantly better: [[A>>B]]\n2. 2. Assistant A is slightly better: [[A>B]]\n3. 3. Tie, relatively the same: [[A=B]]\n4. 4. Assistant B is slightly better: [[B>A]]\n5. 5. Assistant B is significantly better: [[B>>A]]\n\nExample output: My final verdict is tie: [[A=B]]:Table 4 | Description of RL Data and Tasks.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Data Type&lt;/th>\n&lt;th># Prompts&lt;/th>\n&lt;th>Question Type&lt;/th>\n&lt;th>Output Type&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Math&lt;/td>\n&lt;td>26K&lt;/td>\n&lt;td>Quantitative Reasoning&lt;/td>\n&lt;td>Number/Expression/Equation&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Code&lt;/td>\n&lt;td>17K&lt;/td>\n&lt;td>Algorithm and Bug Fixing&lt;/td>\n&lt;td>Code Solution&lt;/td>\n&lt;/tr>",
      "numLines": 300,
      "startLine": 200,
      "totalLines": 1074
    }
  },
  "sourceToolAssistantUUID": "94a2a85b-247c-475b-ba14-208852a74a12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "06344df4-ba11-4af9-b7bd-76292d04e387",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze DeepSeek-R1 reasoning innovation approach",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Tool call

_source line 33 · 2026-05-28T11:21:08.659Z_

<details open><summary>🔧 Tool call — Read · `toolu_019X1u4m2ATgisTSTJrK62ZU`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt",
  "offset": 500,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06344df4-ba11-4af9-b7bd-76292d04e387",
  "isSidechain": false,
  "requestId": "req_011CbUstyZJC867QNnq1CzRj",
  "type": "assistant",
  "uuid": "c7dc95ec-1476-4670-8288-2873ca09e0ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtVL4cM7buCD2wt3uYfmSu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9901,
      "cache_read_input_tokens": 23916,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 23916,
          "cache_creation_input_tokens": 9901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9901
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

_source line 34 · 2026-05-28T11:21:08.669Z_

<details><summary>↩ Tool result · `toolu_019X1u4m2ATgisTSTJrK62ZU`</summary>

```````text
500	&lt;tr>
501	&lt;td>STEM&lt;/td>
502	&lt;td>22K&lt;/td>
503	&lt;td>Multi-Choice&lt;/td>
504	&lt;td>Option&lt;/td>
505	&lt;/tr>
506	&lt;tr>
507	&lt;td>Logic&lt;/td>
508	&lt;td>15K&lt;/td>
509	&lt;td>Choice/Quantitative Reasoning&lt;/td>
510	&lt;td>Option/Number&lt;/td>
511	&lt;/tr>
512	&lt;tr>
513	&lt;td>General&lt;/td>
514	&lt;td>66K&lt;/td>
515	&lt;td>Helpfulness/Harmlessness&lt;/td>
516	&lt;td>Ranked Responses&lt;/td>
517	&lt;/tr>
518	&lt;/tbody>
519	&lt;/table>
520	
521	### B.3. Data Recipe
522	
523	#### B.3.1. RL Data
524	
525	Reasoning RL data includes four categories: mathematics, coding, STEM, and logic problems. In addition, we also incorporate general RL data to improve the helpfulness and harmlessness of the model in the training of DeepSeek-R1. All questions are in Chinese or English. The description of the RL data can be found in Table 4, where we will describe the details of each data type one by one as follows:
526	
527	- • **Mathematics** dataset consists of 26k quantitative reasoning questions, including math exam questions and competition problems. The average number of prompt tokens is 122. The dataset covers various mathematical domains such as algebra, calculus, probability, and geometry. Problems range in difficulty from regional contests to international Olympiads. For each problem, the model is expected to produce a step-by-step reasoning process culminating in a final answer, which can be a numerical value (e.g., "5"), a mathematical expression (e.g., " $x^2 + 3x - 2$ "), or an equation (e.g., " $y = 2x + 1$ "). Mathematical proofs are excluded because it is difficult to determine their correctness. For reinforcement learning purposes, we calculate the reward of a reasoning process by matching the predicted answer with the reference answer. If the answer aligns with the reference, the reward is assigned a value of 1; otherwise, it is assigned a value of 0.
528	- • **Coding** dataset includes 17k algorithm competition questions, along with 8k bug fixing problems. The algorithm competition questions are similar to problems found on platforms like Codeforces or LeetCode. Each problem typically includes a detailed problem description, constraints, and multiple input-output examples. The task is to write a complete function or program that can solve the problem correctly and efficiently, passing a comprehensive set of hidden test cases that assess both correctness and performance. These problems test algorithmic skills, including dynamic programming, graph theory, string manipulation, and data structure usage. The bug-fixing problems are extracted from real-world GitHub issues. Each task provides an issue description, a buggy version of the source code, and a set of unit tests that partially or completely fail. The goal is to understand the intent of the issue, locate and fix the defect in the code, and ensure that the corrected version passes all unit tests.
529	- • **STEM** dataset comprises 22k choice questions that cover topics such as physics, chemistry, and biology. Each question in the STEM task presents a subject-specific problem accompanied by four to eight answer options. The model is required to select the most scientifically accurate answer based on the given context and domain knowledge. The average number of prompt tokens is 161. Specifically, the dataset includes 15.5% physics, 30.7% biology, 46.5% chemistry, and 7.3% other topics such as health and medicine. Since all STEM questions are multiple-choice, a binary reward is assigned based on whether thecorrect option is matched.
530	
531	- • **Logic** dataset contains 15k questions designed to evaluate a model’s reasoning capabilities across a broad spectrum of logical challenges. The dataset includes both real-world and synthetically generated problems. All problems support automatic evaluation, and the average prompt length is approximately 420 tokens. The real-world portion of the dataset comprises a diverse selection of problems sourced from the web, including brain teasers, classical logic puzzles, and knowledge-intensive questions. These questions are presented in a multiple-choice format to ensure objective and consistent assessment. The synthetic portion consists primarily of two categories: code-IO problems and puzzle tasks. Code-IO problems are generated using the data pipeline introduced by Li et al. (2025), which converts competitive coding problems and their corresponding input-output test cases into verifiable logical reasoning problems. The puzzle tasks include problems intended to assess specific reasoning competencies. For example, cryptography puzzles are designed to evaluate a model’s ability to identify and apply patterns in cipher schemes or perform string manipulations; logic puzzles focus on deductive reasoning over complex constraints, such as inferring valid conclusions from a fixed set of premises (e.g., the Zebra puzzle); and arithmetic puzzles test the model’s numerical reasoning (e.g. probability questions and 24 game).
532	- • **General** dataset consists of 66k questions designed to assess helpfulness, spanning various categories such as creative writing, editing, factual question answering, and role-playing. Additionally, the dataset includes 12,000 questions focused on evaluating harmlessness. To ensure robust verification, two reward models are utilized, each trained on a curated dataset of ranked responses generated by models in relation to helpfulness and harmlessness, respectively. We trained the helpful reward model for a single epoch with a maximum sequence length of 8192 tokens during the training phase. However, when deploying the model to generate reward signals, we did not impose any explicit length constraints on the input sequences being evaluated.
533	
534	### **B.3.2. DeepSeek-R1 Cold Start**
535	
536	For DeepSeek-R1, we construct and collect a small amount of long CoT data to fine-tune the model as the initial RL actor. The motivation is primarily product-driven, with a strong emphasis on enhancing user experience. Users tend to find responses more intuitive and engaging when the reasoning process aligns with first-person perspective thought patterns. For example, DeepSeek-R1-Zero is more likely to employ the pronoun ‘we’ or avoid first-person pronouns altogether during problem solving, whereas DeepSeek-R1 tends to use ‘I’ more frequently. Furthermore, we acknowledge that such patterns may elicit unwarranted trust from users. Here, we would like to emphasize that the observed vivid reasoning patterns primarily reflect DeepSeek-engineered heuristics, rather than indicating that the model has inherently acquired human-like intelligence or autonomous problem-solving capabilities.
537	
538	In cold start data creation, we prefer the thinking process that begins with comprehending the problem, followed by detailed reasoning that incorporates reflection and verification. The language employed throughout the thinking process is presented in the first-person perspective. Additionally, maintaining language consistency is crucial for an optimal user experience. Without proper control, model responses may contain a mixture of different languages, regardless of the language used in the query. Such inconsistencies can disrupt comprehension and reduce user satisfaction. Therefore, careful refinement is essential to ensure that responses remain coherent and aligned with user intent. Nevertheless, we acknowledge that the raw Chain-of-Thought (CoT) reasoning produced by DeepSeek-R1-Zero may possess potential that extends beyond thelimitations of current human priors. Specifically, we first engage human annotators to convert the reasoning trace into a more natural, human conversational style. The modified data pairs are then used as examples to prompt an LLM to rewrite additional data in a similar style. All LLM-generated outputs subsequently undergo a second round of human verification to ensure quality and consistency.
539	
540	Listing 1 | Prompt for producing a human-readable solution.
541	
542	```
543	## Question
544	{question}
545	
546	## Thought process
547	{thought_process}
548	
549	---
550	Based on the above thought process, provide a clear, easy-to-follow, and well-formatted solution to the question. Use the same language as the question.
551	
552	The solution must strictly follow these requirements:
553	- Stay faithful and consistent with the given thought process. Do not add new reasoning steps or conclusions not shown in the original.
554	- Show key steps leading to final answer(s) in clear, well-formatted LaTeX.
555	- Use \boxed{} for final answer(s).
556	- Be clean and concise. Avoid colloquial language. Do not use phrases like "thought process" in the solution.
557	
558	Your response should start with the solution right away, and do not include anything else. Your task is solely to write the solution based on the provided thought process. Do not try to solve the question yourself.
559	```
560	
561	Specifically, we begin by gathering thousands of high-quality, diverse reasoning prompts. For each prompt, we generate multiple reasoning trajectories using DeepSeek-R1-Zero with a relatively high temperature of 1.0. Next, we filter these generations to retain only those with correct final answers and a readable format. For mathematical outputs, we use sympy (&lt;https://www.sympy.org/>) for parsing and expression comparison; and for formatting, we apply rules such as repetition detection and language-mixing filtering. Finally, we prompt DeepSeek-V3 to refine both the reasoning and the summaries to ensure proper formatting and a human-friendly expression. In particular, to resolve language mixing, we instruct DeepSeek-V3 to “Translate the thinking process to the same language as the question.” Since DeepSeek-R1-Zero’s summary only provided the final answer, we use the summary prompt in Listing 1 to produce a concise, human-readable solution that outlines both the reasoning steps and the final result.
562	
563	For code data, we collect a large set of competitive programming problems. In detail, We have compiled an extensive collection of competitive programming problems from multiple online judge (OJ) platforms, specifically 5151 problems from Codeforces and 2504 problems from AtCoder. Since the original test cases are not publicly available from these platforms, we developed a methodology to create reliable test cases for each problem.
564	
565	Our approach involves using DeepSeek-V2.5 to generate candidate test cases, followed by a rigorous validation process. Specifically, we prompted DeepSeek-V2.5 to write Python programs that generate test cases tailored to each problem’s requirements as shown in Listing 2.
566	
567	After obtaining numerous candidate test cases, we implemented a two-phase filtering procedure. First, we used correct submissions to eliminate invalid test cases that produced incorrect outputs. Then, we strategically selected subsets of test cases that successfully identifiedflaws in incorrect submissions. This process ensured our final test cases properly differentiated between correct and incorrect solutions for each problem.
568	
569	#### Listing 2 | Prompt for generating test cases for code problem.
570	
571	```
572	&lt;USER>
573	Question:
574	You are given a string word and an integer k.
575	
576	A substring s of word is complete if:
577	
578	Each character in s occurs exactly k times.
579	The difference between two adjacent characters is at most 2. That is, for any two
580	adjacent characters c1 and c2 in s, the absolute difference in their positions in
581	the alphabet is at most 2.
582	Return the number of complete substrings of word.
583	
584	A substring is a non-empty contiguous sequence of characters in a string.
585	
586	**Input**
587	The first line contains a single integer t the number of test cases.
588	The first line of each test case contain one string word.
589	The second line of each test case contain one integer k.
590	It is guaranteed that word consists only of lowercase English letters, and the sum of |
591	word| over all test cases does not exceed 10^5.
592	
593	**Output**
594	For each test case, print one integer the number of complete substrings of word.
595	
596	**Example**
597	Input
598	'''
599	2
600	igigee
601	2
602	aaabbccc
603	3
604	'''
605	
606	Output
607	'''
608	3
609	6
610	'''
611	
612	Construct some random input generators to generate diverse and adversarial inputs,
613	which are large enough to to make incorrect codes exceed the time limit.
614	&lt;/USER>
615	
616	&lt;ASSISTANT>
617	First construct a random input generator for large data with 10 testcases of the same
618	length.
619	
620	'''python
621	import random
622	import string
623	
624	def generate_random_string(l_min, l_max):
625	    length = random.randint(l_min, l_max)
626	    seq = ''.join(random.choices(string.ascii_lowercase, k=length))
627	    k = random.randint(1, length)
628	``````
629	
630	    return f"{{seq}}\n{{k}}"
631	
632	t = 10 # the number of test cases
633	testcase = [generate_random_string(10000, 10000) for _ in range(t)]
634	
635	print(t)
636	print("\n".join(testcase))
637	'''
638	
639	First construct a random input generator for large data with 10 testcases of different
640	length.
641	
642	'''python
643	import random
644	import string
645	
646	def generate_random_string(l_min, l_max):
647	    length = random.randint(l_min, l_max)
648	    seq = ''.join(random.choices(string.ascii_lowercase, k=length))
649	    k = random.randint(1, length)
650	    return f"{{seq}}\n{{k}}"
651	
652	t = 10 # the number of test cases
653	testcase = []
654	cum_length = 0
655	for i in range(t):
656	    # each test case should have length >= 1
657	    cur_testcase, cur_length = generate_random_string(1, 100000 - cum_length - (t -
658	        i))
659	    testcase.append(cur_testcase)
660	    cum_length += cur_length
661	
662	print(t)
663	print("\n".join(testcase))
664	'''
665	
666	Construct a random input generator for large data with only one test case.
667	
668	'''python
669	import random
670	import string
671	
672	def generate_random_string(l_min, l_max):
673	    ...
674	
675	t = 1 # the number of test cases
676	testcase = [generate_random_string(90000, 100000) for _ in range(t)]
677	
678	print(t)
679	print("\n".join(testcase))
680	'''
681	
682	Construct an input generator for large adversarial inputs of a string of a repeated
683	single character.
684	
685	'''python
686	import random
687	import string
688	
689	def generate_single_repeated_char(l_min, l_max):
690	    length = random.randint(l_min, l_max)
691	
692	``````
693	char = random.choice(string.ascii_lowercase)
694	seq = char * length
695	k = random.randint(1, length)
696	return f"{{seq}}\n{{k}}"
697	
698	t = 1 # the number of test cases
699	testcase = [generate_single_repeated_char(90000, 100000) for _ in range(t)]
700	
701	print(t)
702	print("\n".join(testcase))
703	'''
704	```
705	
706	Construct an input generator for large adversarial inputs of a string of two alternating characters.
707	
708	```
709	'''python
710	import random
711	import string
712	
713	def generate_alternating_chars(l_min, l_max):
714	    length = random.randint(l_min, l_max)
715	    char1, char2 = random.sample(string.ascii_lowercase, 2)
716	    seq = ''.join(char1 if i % 2 == 0 else char2 for i in range(length))
717	    k = random.randint(1, length)
718	    return f"{{seq}}\n{{k}}"
719	
720	t = 1 # the number of test cases
721	testcase = [generate_alternating_chars(90000, 100000) for _ in range(t)]
722	
723	print(t)
724	print("\n".join(testcase))
725	'''
726	```
727	
728	Construct an input generator for large adversarial inputs of a string of sequential characters from alphabet.
729	
730	```
731	'''python
732	...
733	'''
734	```
735	
736	&lt;/ASSISTANT>
737	
738	Question:
739	
740	Question Description
741	
742	Construct some random input generators to generate large, diverse and adversarial inputs, which are large enough to testing time complexity and to make incorrect codes exceed the time limit.
743	
744	Use the format used in the above example by returning several input generators in different code blocks. Each of these generators prints EXACTLY ONE input directly into stdout.
745	
746	In addition, we employ few-shot prompting for DeepSeek-V3 to generate responses to simple math problems, such as "1 + 1 = ?", ensuring that the outputs remain concise and appropriately structured. We provide the prompt for a simple math problem in Listing 3.
747	
748	Listing 3 | Prompt for generating chain-of-thought for simple math problem.
749	
750	```
751	## Question
752	How much is 5+4?
753	``````
754	## Response
755	&lt;think>
756	```
757	
758	I need to add the numbers 5 and 4. Starting with 5, if I add 4 to it, the total will be 9. Therefore, the sum of 5 and 4 is 9.
759	
760	```
761	&lt;/think>
762	```
763	
764	```
765	**Solution:**
766	```
767	
768	We are asked to calculate the sum of 5 and 4.
769	
770	```
771	**Step 1:** Start with the number 5.
772	```
773	
774	```
775	**Step 2:** Add 4 to it.
776	```
777	
778	```
779	\[
780	5 + 4 = 9
781	\]
782	```
783	
784	```
785	**Final Answer:** \(\boxed{9}\)
786	```
787	
788	```
789	---
790	```
791	
792	```
793	## Question
794	what is 1 plus 2
795	```
796	
797	```
798	## Response
799	&lt;think>
```````

</details>

<details><summary>Recorded metadata</summary>

```````json
{
  "recorded_role": "user",
  "parentUuid": "c7dc95ec-1476-4670-8288-2873ca09e0ac",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "1fdd16af-b14a-4049-9563-a15d4357b990",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt",
      "content": "&lt;tr>\n&lt;td>STEM&lt;/td>\n&lt;td>22K&lt;/td>\n&lt;td>Multi-Choice&lt;/td>\n&lt;td>Option&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Logic&lt;/td>\n&lt;td>15K&lt;/td>\n&lt;td>Choice/Quantitative Reasoning&lt;/td>\n&lt;td>Option/Number&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>General&lt;/td>\n&lt;td>66K&lt;/td>\n&lt;td>Helpfulness/Harmlessness&lt;/td>\n&lt;td>Ranked Responses&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n### B.3. Data Recipe\n\n#### B.3.1. RL Data\n\nReasoning RL data includes four categories: mathematics, coding, STEM, and logic problems. In addition, we also incorporate general RL data to improve the helpfulness and harmlessness of the model in the training of DeepSeek-R1. All questions are in Chinese or English. The description of the RL data can be found in Table 4, where we will describe the details of each data type one by one as follows:\n\n- • **Mathematics** dataset consists of 26k quantitative reasoning questions, including math exam questions and competition problems. The average number of prompt tokens is 122. The dataset covers various mathematical domains such as algebra, calculus, probability, and geometry. Problems range in difficulty from regional contests to international Olympiads. For each problem, the model is expected to produce a step-by-step reasoning process culminating in a final answer, which can be a numerical value (e.g., \"5\"), a mathematical expression (e.g., \" $x^2 + 3x - 2$ \"), or an equation (e.g., \" $y = 2x + 1$ \"). Mathematical proofs are excluded because it is difficult to determine their correctness. For reinforcement learning purposes, we calculate the reward of a reasoning process by matching the predicted answer with the reference answer. If the answer aligns with the reference, the reward is assigned a value of 1; otherwise, it is assigned a value of 0.\n- • **Coding** dataset includes 17k algorithm competition questions, along with 8k bug fixing problems. The algorithm competition questions are similar to problems found on platforms like Codeforces or LeetCode. Each problem typically includes a detailed problem description, constraints, and multiple input-output examples. The task is to write a complete function or program that can solve the problem correctly and efficiently, passing a comprehensive set of hidden test cases that assess both correctness and performance. These problems test algorithmic skills, including dynamic programming, graph theory, string manipulation, and data structure usage. The bug-fixing problems are extracted from real-world GitHub issues. Each task provides an issue description, a buggy version of the source code, and a set of unit tests that partially or completely fail. The goal is to understand the intent of the issue, locate and fix the defect in the code, and ensure that the corrected version passes all unit tests.\n- • **STEM** dataset comprises 22k choice questions that cover topics such as physics, chemistry, and biology. Each question in the STEM task presents a subject-specific problem accompanied by four to eight answer options. The model is required to select the most scientifically accurate answer based on the given context and domain knowledge. The average number of prompt tokens is 161. Specifically, the dataset includes 15.5% physics, 30.7% biology, 46.5% chemistry, and 7.3% other topics such as health and medicine. Since all STEM questions are multiple-choice, a binary reward is assigned based on whether thecorrect option is matched.\n\n- • **Logic** dataset contains 15k questions designed to evaluate a model’s reasoning capabilities across a broad spectrum of logical challenges. The dataset includes both real-world and synthetically generated problems. All problems support automatic evaluation, and the average prompt length is approximately 420 tokens. The real-world portion of the dataset comprises a diverse selection of problems sourced from the web, including brain teasers, classical logic puzzles, and knowledge-intensive questions. These questions are presented in a multiple-choice format to ensure objective and consistent assessment. The synthetic portion consists primarily of two categories: code-IO problems and puzzle tasks. Code-IO problems are generated using the data pipeline introduced by Li et al. (2025), which converts competitive coding problems and their corresponding input-output test cases into verifiable logical reasoning problems. The puzzle tasks include problems intended to assess specific reasoning competencies. For example, cryptography puzzles are designed to evaluate a model’s ability to identify and apply patterns in cipher schemes or perform string manipulations; logic puzzles focus on deductive reasoning over complex constraints, such as inferring valid conclusions from a fixed set of premises (e.g., the Zebra puzzle); and arithmetic puzzles test the model’s numerical reasoning (e.g. probability questions and 24 game).\n- • **General** dataset consists of 66k questions designed to assess helpfulness, spanning various categories such as creative writing, editing, factual question answering, and role-playing. Additionally, the dataset includes 12,000 questions focused on evaluating harmlessness. To ensure robust verification, two reward models are utilized, each trained on a curated dataset of ranked responses generated by models in relation to helpfulness and harmlessness, respectively. We trained the helpful reward model for a single epoch with a maximum sequence length of 8192 tokens during the training phase. However, when deploying the model to generate reward signals, we did not impose any explicit length constraints on the input sequences being evaluated.\n\n### **B.3.2. DeepSeek-R1 Cold Start**\n\nFor DeepSeek-R1, we construct and collect a small amount of long CoT data to fine-tune the model as the initial RL actor. The motivation is primarily product-driven, with a strong emphasis on enhancing user experience. Users tend to find responses more intuitive and engaging when the reasoning process aligns with first-person perspective thought patterns. For example, DeepSeek-R1-Zero is more likely to employ the pronoun ‘we’ or avoid first-person pronouns altogether during problem solving, whereas DeepSeek-R1 tends to use ‘I’ more frequently. Furthermore, we acknowledge that such patterns may elicit unwarranted trust from users. Here, we would like to emphasize that the observed vivid reasoning patterns primarily reflect DeepSeek-engineered heuristics, rather than indicating that the model has inherently acquired human-like intelligence or autonomous problem-solving capabilities.\n\nIn cold start data creation, we prefer the thinking process that begins with comprehending the problem, followed by detailed reasoning that incorporates reflection and verification. The language employed throughout the thinking process is presented in the first-person perspective. Additionally, maintaining language consistency is crucial for an optimal user experience. Without proper control, model responses may contain a mixture of different languages, regardless of the language used in the query. Such inconsistencies can disrupt comprehension and reduce user satisfaction. Therefore, careful refinement is essential to ensure that responses remain coherent and aligned with user intent. Nevertheless, we acknowledge that the raw Chain-of-Thought (CoT) reasoning produced by DeepSeek-R1-Zero may possess potential that extends beyond thelimitations of current human priors. Specifically, we first engage human annotators to convert the reasoning trace into a more natural, human conversational style. The modified data pairs are then used as examples to prompt an LLM to rewrite additional data in a similar style. All LLM-generated outputs subsequently undergo a second round of human verification to ensure quality and consistency.\n\nListing 1 | Prompt for producing a human-readable solution.\n\n```\n## Question\n{question}\n\n## Thought process\n{thought_process}\n\n---\nBased on the above thought process, provide a clear, easy-to-follow, and well-formatted solution to the question. Use the same language as the question.\n\nThe solution must strictly follow these requirements:\n- Stay faithful and consistent with the given thought process. Do not add new reasoning steps or conclusions not shown in the original.\n- Show key steps leading to final answer(s) in clear, well-formatted LaTeX.\n- Use \\boxed{} for final answer(s).\n- Be clean and concise. Avoid colloquial language. Do not use phrases like \"thought process\" in the solution.\n\nYour response should start with the solution right away, and do not include anything else. Your task is solely to write the solution based on the provided thought process. Do not try to solve the question yourself.\n```\n\nSpecifically, we begin by gathering thousands of high-quality, diverse reasoning prompts. For each prompt, we generate multiple reasoning trajectories using DeepSeek-R1-Zero with a relatively high temperature of 1.0. Next, we filter these generations to retain only those with correct final answers and a readable format. For mathematical outputs, we use sympy (&lt;https://www.sympy.org/>) for parsing and expression comparison; and for formatting, we apply rules such as repetition detection and language-mixing filtering. Finally, we prompt DeepSeek-V3 to refine both the reasoning and the summaries to ensure proper formatting and a human-friendly expression. In particular, to resolve language mixing, we instruct DeepSeek-V3 to “Translate the thinking process to the same language as the question.” Since DeepSeek-R1-Zero’s summary only provided the final answer, we use the summary prompt in Listing 1 to produce a concise, human-readable solution that outlines both the reasoning steps and the final result.\n\nFor code data, we collect a large set of competitive programming problems. In detail, We have compiled an extensive collection of competitive programming problems from multiple online judge (OJ) platforms, specifically 5151 problems from Codeforces and 2504 problems from AtCoder. Since the original test cases are not publicly available from these platforms, we developed a methodology to create reliable test cases for each problem.\n\nOur approach involves using DeepSeek-V2.5 to generate candidate test cases, followed by a rigorous validation process. Specifically, we prompted DeepSeek-V2.5 to write Python programs that generate test cases tailored to each problem’s requirements as shown in Listing 2.\n\nAfter obtaining numerous candidate test cases, we implemented a two-phase filtering procedure. First, we used correct submissions to eliminate invalid test cases that produced incorrect outputs. Then, we strategically selected subsets of test cases that successfully identifiedflaws in incorrect submissions. This process ensured our final test cases properly differentiated between correct and incorrect solutions for each problem.\n\n#### Listing 2 | Prompt for generating test cases for code problem.\n\n```\n&lt;USER>\nQuestion:\nYou are given a string word and an integer k.\n\nA substring s of word is complete if:\n\nEach character in s occurs exactly k times.\nThe difference between two adjacent characters is at most 2. That is, for any two\nadjacent characters c1 and c2 in s, the absolute difference in their positions in\nthe alphabet is at most 2.\nReturn the number of complete substrings of word.\n\nA substring is a non-empty contiguous sequence of characters in a string.\n\n**Input**\nThe first line contains a single integer t the number of test cases.\nThe first line of each test case contain one string word.\nThe second line of each test case contain one integer k.\nIt is guaranteed that word consists only of lowercase English letters, and the sum of |\nword| over all test cases does not exceed 10^5.\n\n**Output**\nFor each test case, print one integer the number of complete substrings of word.\n\n**Example**\nInput\n'''\n2\nigigee\n2\naaabbccc\n3\n'''\n\nOutput\n'''\n3\n6\n'''\n\nConstruct some random input generators to generate diverse and adversarial inputs,\nwhich are large enough to to make incorrect codes exceed the time limit.\n&lt;/USER>\n\n&lt;ASSISTANT>\nFirst construct a random input generator for large data with 10 testcases of the same\nlength.\n\n'''python\nimport random\nimport string\n\ndef generate_random_string(l_min, l_max):\n    length = random.randint(l_min, l_max)\n    seq = ''.join(random.choices(string.ascii_lowercase, k=length))\n    k = random.randint(1, length)\n``````\n\n    return f\"{{seq}}\\n{{k}}\"\n\nt = 10 # the number of test cases\ntestcase = [generate_random_string(10000, 10000) for _ in range(t)]\n\nprint(t)\nprint(\"\\n\".join(testcase))\n'''\n\nFirst construct a random input generator for large data with 10 testcases of different\nlength.\n\n'''python\nimport random\nimport string\n\ndef generate_random_string(l_min, l_max):\n    length = random.randint(l_min, l_max)\n    seq = ''.join(random.choices(string.ascii_lowercase, k=length))\n    k = random.randint(1, length)\n    return f\"{{seq}}\\n{{k}}\"\n\nt = 10 # the number of test cases\ntestcase = []\ncum_length = 0\nfor i in range(t):\n    # each test case should have length >= 1\n    cur_testcase, cur_length = generate_random_string(1, 100000 - cum_length - (t -\n        i))\n    testcase.append(cur_testcase)\n    cum_length += cur_length\n\nprint(t)\nprint(\"\\n\".join(testcase))\n'''\n\nConstruct a random input generator for large data with only one test case.\n\n'''python\nimport random\nimport string\n\ndef generate_random_string(l_min, l_max):\n    ...\n\nt = 1 # the number of test cases\ntestcase = [generate_random_string(90000, 100000) for _ in range(t)]\n\nprint(t)\nprint(\"\\n\".join(testcase))\n'''\n\nConstruct an input generator for large adversarial inputs of a string of a repeated\nsingle character.\n\n'''python\nimport random\nimport string\n\ndef generate_single_repeated_char(l_min, l_max):\n    length = random.randint(l_min, l_max)\n\n``````\nchar = random.choice(string.ascii_lowercase)\nseq = char * length\nk = random.randint(1, length)\nreturn f\"{{seq}}\\n{{k}}\"\n\nt = 1 # the number of test cases\ntestcase = [generate_single_repeated_char(90000, 100000) for _ in range(t)]\n\nprint(t)\nprint(\"\\n\".join(testcase))\n'''\n```\n\nConstruct an input generator for large adversarial inputs of a string of two alternating characters.\n\n```\n'''python\nimport random\nimport string\n\ndef generate_alternating_chars(l_min, l_max):\n    length = random.randint(l_min, l_max)\n    char1, char2 = random.sample(string.ascii_lowercase, 2)\n    seq = ''.join(char1 if i % 2 == 0 else char2 for i in range(length))\n    k = random.randint(1, length)\n    return f\"{{seq}}\\n{{k}}\"\n\nt = 1 # the number of test cases\ntestcase = [generate_alternating_chars(90000, 100000) for _ in range(t)]\n\nprint(t)\nprint(\"\\n\".join(testcase))\n'''\n```\n\nConstruct an input generator for large adversarial inputs of a string of sequential characters from alphabet.\n\n```\n'''python\n...\n'''\n```\n\n&lt;/ASSISTANT>\n\nQuestion:\n\nQuestion Description\n\nConstruct some random input generators to generate large, diverse and adversarial inputs, which are large enough to testing time complexity and to make incorrect codes exceed the time limit.\n\nUse the format used in the above example by returning several input generators in different code blocks. Each of these generators prints EXACTLY ONE input directly into stdout.\n\nIn addition, we employ few-shot prompting for DeepSeek-V3 to generate responses to simple math problems, such as \"1 + 1 = ?\", ensuring that the outputs remain concise and appropriately structured. We provide the prompt for a simple math problem in Listing 3.\n\nListing 3 | Prompt for generating chain-of-thought for simple math problem.\n\n```\n## Question\nHow much is 5+4?\n``````\n## Response\n&lt;think>\n```\n\nI need to add the numbers 5 and 4. Starting with 5, if I add 4 to it, the total will be 9. Therefore, the sum of 5 and 4 is 9.\n\n```\n&lt;/think>\n```\n\n```\n**Solution:**\n```\n\nWe are asked to calculate the sum of 5 and 4.\n\n```\n**Step 1:** Start with the number 5.\n```\n\n```\n**Step 2:** Add 4 to it.\n```\n\n```\n\\[\n5 + 4 = 9\n\\]\n```\n\n```\n**Final Answer:** \\(\\boxed{9}\\)\n```\n\n```\n---\n```\n\n```\n## Question\nwhat is 1 plus 2\n```\n\n```\n## Response\n&lt;think>",
      "numLines": 300,
      "startLine": 500,
      "totalLines": 1074
    }
  },
  "sourceToolAssistantUUID": "c7dc95ec-1476-4670-8288-2873ca09e0ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```````

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "1fdd16af-b14a-4049-9563-a15d4357b990",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze DeepSeek-R1 reasoning innovation approach",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Tool call

_source line 37 · 2026-05-28T11:21:14.207Z_

<details open><summary>🔧 Tool call — Read · `toolu_015q9DZYfGrKpW15pEy4KT7c`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt",
  "offset": 800,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fdd16af-b14a-4049-9563-a15d4357b990",
  "isSidechain": false,
  "requestId": "req_011CbUsuNPEs6rn92GopFWwY",
  "type": "assistant",
  "uuid": "8d171140-a3a2-45f5-a433-68428113926f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtyqYmWugnY5HTAGtqZeX6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 33817,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 33817,
          "cache_creation_input_tokens": 4814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4814
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

_source line 38 · 2026-05-28T11:21:14.212Z_

<details><summary>↩ Tool result · `toolu_015q9DZYfGrKpW15pEy4KT7c`</summary>

````text
800	```
801	
802	I need to determine the sum of 1 and 2.
803	
804	Adding these two numbers together, 1 plus 2 equals 3.
805	
806	Therefore, the answer is 3.
807	
808	```
809	&lt;/think>
810	```
811	
812	Sure! Let's solve the problem step by step.
813	
814	```
815	**Problem:** What is  $(1 + 2)$ ?
816	```
817	
818	```
819	**Solution:**
820	```
821	
822	To find the sum of 1 and 2, simply add the two numbers together:
823	
824	```
825	\[
826	1 + 2 = 3
827	\]
828	```
829	
830	```
831	**Answer:**
832	```
833	
834	```
835	\(\boxed{3}\)
836	```
837	
838	```
839	---
840	```
841	
842	```
843	## Question
844	{question}
845	```
846	
847	```
848	## Response
849	```#### Listing 4 | An example prompt of using DeepSeek-V3 as a judge.
850	
851	```
852	As an advanced reasoning problem evaluation assistant, your primary responsibility is to assess the accuracy of provided answers. You will be presented with a reasoning-related question, its corresponding reference answer, and an answer requiring evaluation.
853	
854	## Answer Quality Classification
855	You have to carefully analyze and classify the answer into one of the following two levels:
856	1. correct: The answer fully aligns with the reference answer in both reasoning process and final conclusion, and address the question without any errors or omissions.
857	2. incorrect: The answer contains major errors in key reasoning steps or the final conclusion, or completely deviates from the core of the question. This indicates a fundamental misunderstanding or error in comprehending the question.
858	
859	## Question
860	{question}
861	
862	## Reference Answer
863	{reference}
864	
865	## Answer to be Evaluated
866	{answer}
867	
868	## Output Format
869	You need to combine the question and reference answer, first provide a detailed explanation of your analysis of the answer to be evaluated, then conclude with the final answer quality classification.
870	Output the following content in JSON format, including two key:
871	1. 'analysis': analysis of the answer's correctness;
872	2. 'correctness': correct/incorrect
873	```
874	
875	### B.3.3. 800K Supervised Data
876	
877	**Reasoning Data** We curate a large set of reasoning prompts and generate reasoning trajectories by performing rejection sampling from the checkpoint of the first-stage RL training. In the previous stage, we only included data that could be evaluated using rule-based rewards. However, in this stage, we expand the dataset by incorporating additional data, some of which uses a generative reward model by feeding the ground-truth and model predictions into DeepSeek-V3 for judgment, an example prompt is provided in Listing 4. Additionally, because the model output is sometimes chaotic and difficult to read, we have filtered out chain-of-thought with mixed languages, long paragraphs, and code blocks. For each prompt, we sample multiple responses and retain only the correct ones. In total, we collect about 600k reasoning-related training samples.
878	
879	**Non-Reasoning Data** For non-reasoning data, such as writing, factual QA, self-cognition, and translation, we adopt the DeepSeek-V3 pipeline and reuse portions of the SFT dataset of DeepSeek-V3. We also incorporate software engineering-focused data, including program repair and front-end web development, to enhance the model's ability to solve real-world problems. For certain non-reasoning tasks, we call DeepSeek-V3 to generate a potential chain-of-thought before answering the question by prompting. However, for simpler queries, such as "hello" we do not provide a CoT in response. In the end, we collected a total of approximately 200k training samples that are unrelated to reasoning.When designing our thinking process style, we ask the model to follow key principles: First, keep each paragraph concise and digestible. Short paragraphs make ideas clearer and easier to follow. Second, adopt a conversational tone that feels natural and engaging. We avoid technical formatting like markdown to maintain a smooth reading experience. Third, and most importantly, the thinking process begins by understanding the complete user context. This means analyzing who our users are, what situations they’re dealing with, and what they truly need - including those unstated needs that may lie beneath the surface of their initial request.
880	
881	After eliciting these thinking processes from the model, human annotators meticulously verify the accuracy of the outputs. Our findings indicate that these artificial reasoning traces enhance the model’s precision in interpreting user queries. Specifically, they effectively highlight format constraints, clarify user intentions, and elucidate the requisite structure of outputs. This methodological approach facilitates more accurate and responsive interactions between the model and users.
882	
883	Table 5 | Data Statistics of SFT Data.
884	
885	&lt;table border="1">
886	&lt;thead>
887	&lt;tr>
888	&lt;th>Domain&lt;/th>
889	&lt;th>Num Samples&lt;/th>
890	&lt;th>Avg Rounds&lt;/th>
891	&lt;th>Avg Tokens&lt;/th>
892	&lt;/tr>
893	&lt;/thead>
894	&lt;tbody>
895	&lt;tr>
896	&lt;td>Math&lt;/td>
897	&lt;td>395285&lt;/td>
898	&lt;td>1.0&lt;/td>
899	&lt;td>6094.2&lt;/td>
900	&lt;/tr>
901	&lt;tr>
902	&lt;td>Code&lt;/td>
903	&lt;td>211129&lt;/td>
904	&lt;td>1.1&lt;/td>
905	&lt;td>7435.7&lt;/td>
906	&lt;/tr>
907	&lt;tr>
908	&lt;td>STEM&lt;/td>
909	&lt;td>10124&lt;/td>
910	&lt;td>1.0&lt;/td>
911	&lt;td>4928.8&lt;/td>
912	&lt;/tr>
913	&lt;tr>
914	&lt;td>Logic&lt;/td>
915	&lt;td>10395&lt;/td>
916	&lt;td>1.0&lt;/td>
917	&lt;td>2739.0&lt;/td>
918	&lt;/tr>
919	&lt;tr>
920	&lt;td>General&lt;/td>
921	&lt;td>177812&lt;/td>
922	&lt;td>1.1&lt;/td>
923	&lt;td>1419.8&lt;/td>
924	&lt;/tr>
925	&lt;tr>
926	&lt;td>Total&lt;/td>
927	&lt;td>804745&lt;/td>
928	&lt;td>1.0&lt;/td>
929	&lt;td>5355.3&lt;/td>
930	&lt;/tr>
931	&lt;/tbody>
932	&lt;/table>
933	
934	**SFT Data Statistics** Table 5 summarizes the data statistics across various domains, based on approximately 800,000 supervised samples. It is worth noting that the majority of the data consists of single-turn interactions, which may limit the multi-turn conversational capabilities of DeepSeek-R1. We leave the expansion to multi-turn dialogue data as future work. The math-related data are primarily in Chinese and English, spanning a wide range of topics and difficulty levels. These questions are verifiable, either through deterministic rules or by reference to specific ground-truth answers. The code dataset encompasses not only competitive programming problems but also debugging tasks and project-oriented coding queries. STEM and logic-related questions, although smaller in volume compared to mathematics and code, are sourced from publicly available textbooks and online repositories. The general-domain queries are diverse, predominantly in Chinese and English, and include tasks such as creative writing, open-ended question answering, role-playing scenarios, and more.
935	
936	**Examples of SFT Trajectories** We provide examples of SFT trajectories related to math, code, and non-reasoning in Listings 5, 6, and 7.
937	
938	Listing 5 | An example SFT trajectory from reasoning data related to mathematics.
939	
940	```
941	## Question
942	For positive integer  $n$ , define  $S_n$  to be the minimum value of the sum  $\sum_{k=1}^n \sqrt{(2k-1)^2 + a_k^2}$ , where  $a_1, a_2, \dots, a_n$  are positive real numbers whose sum is 17. There is a unique positive integer  $n$  for which  $S_n$  is also an integer. Find this  $n$ .
943	
944	## Response
945	```&lt;think>
946	
947	Alright, so I'm trying to solve this problem where I need to find a positive integer  $n$  such that  $S_n$ , the minimum value of the sum  $\sum_{k=1}^n \sqrt{(2k-1)^2 + a_k^2}$ , is an integer. Here,  $(a_1, a_2, \dots, a_n)$  are positive real numbers that add up to 17.
948	
949	Hmm, okay, let me break this down. I know that when you have a sum of square roots like this, it often relates to geometry, maybe minimizing distances. It reminds me of the problem where you have to break up a path into segments with certain slopes to minimize total distance. Maybe this is similar to finding the shortest path in a staircase.
950	
951	Let me visualize it. Each term  $\sqrt{(2k-1)^2 + a_k^2}$  looks like the hypotenuse of a right-angled triangle with legs  $(2k-1)$  and  $a_k$ . So, if I imagine a grid where I move horizontally by  $a_k$  and vertically by  $(2k-1)$  for each step  $k$ , then  $S_n$  would be the total length of this path.
952	
953	Now, the sum of all  $a_k$  is 17, which would be the total horizontal distance. I need to figure out the vertical distances, which are fixed based on  $k$ . So the total vertical distance would be  $\sum_{k=1}^n (2k-1)$ . Let me compute that:
954	
955	The sum  $\sum_{k=1}^n (2k-1)$  is equal to  $2 \sum_{k=1}^n k - \sum_{k=1}^n 1 = 2 \cdot \frac{n(n+1)}{2} - n = n(n+1) - n = n^2$ . So the total vertical distance is  $n^2$ .
956	
957	Wait a second, so this entire setup is like moving from the origin to the point  $(17, n^2)$  with  $n$  segments. Each segment has a horizontal component  $a_k$  and a vertical component  $(2k-1)$ . But in reality, this entire path from  $(0, 0)$  to  $(17, n^2)$  can be considered as a single straight line if we could somehow combine all these segments.
958	
959	But we can't change the number of segments  $n$ ; each segment's vertical component is fixed. However, the horizontal components  $a_k$  can be adjusted as long as their sum is 17. So, to find the minimal total distance, maybe we can think of it as if each segment is contributing to the total path optimally. If we scale each horizontal component  $a_k$  proportionally, maybe this also corresponds to scaling the vertical components.
960	
961	Alternatively, I can think of calculus optimization techniques. If I need to minimize the sum  $\sum_{k=1}^n \sqrt{(2k-1)^2 + a_k^2}$  subject to  $\sum_{k=1}^n a_k = 17$ , I can use the method of Lagrange multipliers.
962	
963	Let me set up the Lagrangian. Let  $L = \sum_{k=1}^n \sqrt{(2k-1)^2 + a_k^2} + \lambda (17 - \sum_{k=1}^n a_k)$ .
964	
965	Taking the derivative of  $L$  with respect to each  $a_k$ :
966	
967	$$\frac{\partial L}{\partial a_k} = \frac{a_k}{\sqrt{(2k-1)^2 + a_k^2}} - \lambda = 0$$
968	
969	So, for each  $k$ , we have  $\frac{a_k}{\sqrt{(2k-1)^2 + a_k^2}} = \lambda$ . Let me solve for  $a_k$ :
970	
971	Squaring both sides gives  $\frac{a_k^2}{(2k-1)^2 + a_k^2} = \lambda^2$ .
972	
973	Rearranging terms:  $a_k^2 = \lambda^2 \left( (2k-1)^2 + a_k^2 \right)$ .
974	
975	Divide both sides by  $a_k^2$  (assuming  $a_k \neq 0$ ):  $1 = \lambda^2 \left( \frac{(2k-1)^2}{a_k^2} + 1 \right)$ .Simplify:  $\sqrt{1 - \lambda^2} = \lambda \sqrt{\frac{(2k-1)^2}{a_k^2}}$ .
976	
977	Then,  $\sqrt{\frac{(2k-1)^2}{a_k^2}} = \sqrt{\frac{1-\lambda^2}{\lambda^2}}$ .
978	
979	Therefore,  $\sqrt{\frac{2k-1}{a_k}} = \sqrt{\frac{1-\lambda^2}{\lambda^2}} = \frac{\sqrt{1-\lambda^2}}{\lambda}$ .
980	
981	Let me denote  $c = \frac{\sqrt{1-\lambda^2}}{\lambda}$ . Then,  $a_k = \frac{2k-1}{c}$ .
982	
983	So, each  $a_k$  is proportional to  $(2k-1)$ . That is,  $a_k = \frac{2k-1}{c}$ .
984	
985	Since the sum of all  $a_k$  is 17, we can write:
986	
987	$\sum_{k=1}^n a_k = \sum_{k=1}^n \frac{2k-1}{c} = \frac{1}{c} \sum_{k=1}^n (2k-1)$ .
988	
989	Earlier, I found that  $\sum_{k=1}^n (2k-1) = n^2$ . Therefore,
990	
991	$\frac{n^2}{c} = 17 \Rightarrow c = \frac{n^2}{17}$ .
992	
993	Thus,  $a_k = \frac{2k-1}{c} = \frac{(2k-1) \cdot 17}{n^2}$ .
994	
995	Now, going back to the original expression for  $S_n$ :
996	
997	$S_n = \sum_{k=1}^n \sqrt{(2k-1)^2 + a_k^2}$ .
998	
999	Substituting  $a_k = \frac{17(2k-1)}{n^2}$ , we get:
1000	
1001	$\sqrt{(2k-1)^2 + \left(\frac{17(2k-1)}{n^2}\right)^2} = (2k-1) \sqrt{1 + \left(\frac{17}{n^2}\right)^2}$ .
1002	
1003	So, factor that square root out of the sum:
1004	
1005	$S_n = \sqrt{1 + \left(\frac{17}{n^2}\right)^2} \cdot \sum_{k=1}^n (2k-1)$ .
1006	
1007	We already know that  $\sum_{k=1}^n (2k-1) = n^2$ , so this simplifies to:
1008	
1009	$S_n = \sqrt{1 + \left(\frac{17}{n^2}\right)^2} \cdot n^2 = \sqrt{n^4 + 17^2} = \sqrt{n^4 + 289}$ .
1010	
1011	Wait, that seems too simplified. Let me check my steps:
1012	
1013	1. 1. I set up the Lagrangian correctly.
1014	2. 2. Took the derivative and found  $a_k = \frac{2k-1}{c}$ .
1015	3. 3. Summed them up to get  $c = \frac{n^2}{17}$ .
1016	4. 4. Plugged back into  $S_n$  and factored out  $(2k-1)$ , so each term becomes  $(2k-1) \sqrt{1 + \left(\frac{17}{n^2}\right)^2}$ .
1017	5. 5. Since  $\sum (2k-1) = n^2$ , so total sum is  $n^2 \sqrt{1 + \left(\frac{17}{n^2}\right)^2} = \sqrt{n^4 + 17^2}$ .
1018	
1019	Yeah, that seems to check out. So,  $S_n = \sqrt{n^4 + 289}$ . Wait,  $17^2$  is 289.
1020	
1021	Therefore,  $S_n = \sqrt{n^4 + 289}$ . We need this to be an integer.
1022	
1023	So, I need to find an integer  $n$  such that  $n^4 + 289$  is a perfect square.
1024	
1025	Let me denote  $S_n = m$ , where  $m$  is an integer, so:
1026	
1027	$n^4 + 289 = m^2$ .This implies  $(m^2 - n^4 = 289)$ .
1028	
1029	Hmm, 289 is  $17^2$ . So,  $(m^2 - n^4 = 17^2)$ . That can be written as:
1030	
1031	$$(m^2 - n^4 = (17)^2)$$
1032	
1033	Looking at this equation, it's a difference of squares.
1034	
1035	$$(m^2 - n^4 = (m - n^2)(m + n^2) = 17^2 = 289)$$
1036	
1037	So, we have  $(m - n^2)(m + n^2) = 289$ .
1038	
1039	Since  $(m)$  and  $(n)$  are positive integers, both  $(m - n^2)$  and  $(m + n^2)$  are positive integers and factors of 289. Also,  $(m + n^2 > m - n^2)$ .
1040	
1041	So, since 289 is  $17^2$ , its positive factor pairs are (1, 289) and (17, 17).
1042	
1043	Hence, the factor pairs are:
1044	
1045	1. 1.  $(m - n^2 = 1)$  and  $(m + n^2 = 289)$ .
1046	2. 2.  $(m - n^2 = 17)$  and  $(m + n^2 = 17)$ .
1047	
1048	But the second case gives  $(m - n^2 = 17)$  and  $(m + n^2 = 17)$ .
1049	
1050	Subtracting the equations:  $(m + n^2) - (m - n^2) = 17 - 17 \Rightarrow (2n^2 = 0) \Rightarrow (n^2 = 0)$ . But  $(n)$  is a positive integer, so this case is invalid.
1051	
1052	So, we only consider the first factor pair:  $(m - n^2 = 1)$  and  $(m + n^2 = 289)$ .
1053	
1054	Adding the two equations:  $(m - n^2) + (m + n^2) = 1 + 289 \Rightarrow (2m = 290) \Rightarrow (m = 145)$ .
1055	
1056	Subtracting the two equations:  $(m + n^2) - (m - n^2) = 289 - 1 \Rightarrow (2n^2 = 288) \Rightarrow (n^2 = 144) \Rightarrow (n = 12)$  since  $(n)$  is positive.
1057	
1058	Therefore,  $(n = 12)$ .
1059	
1060	Before I conclude, let me verify that  $(S_n = \sqrt{12^4 + 17^2} = \sqrt{20736 + 289} = \sqrt{21025} = 145)$ , which is indeed an integer.
1061	
1062	Is this the only  $(n)$ ? The question says there's a unique positive integer  $(n)$ , so this must be the one.
1063	
1064	**\*\*Final Answer\*\***
1065	
1066	The unique positive integer  $(n)$  is  $\boxed{12}$ .  
1067	&lt;/think>
1068	
1069	To solve the problem, we need to find a positive integer  $(n)$  such that  $(S_n)$ , the minimum value of the sum  $(\sum_{k=1}^n \sqrt{(2k-1)^2 + a_k^2})$ , is an integer. Here,  $(a_1, a_2, \dots, a_n)$  are positive real numbers whose sum is 17.
1070	
1071	First, we recognize that each term  $(\sqrt{(2k-1)^2 + a_k^2})$  represents the hypotenuse of a right-angled triangle with legs  $(2k-1)$  and  $(a_k)$ . The total vertical distance is the sum of the vertical components, which is  $(\sum_{k=1}^n (2k-1) = n^2)$ . The total horizontal distance is the sum of  $(a_k)$ , which is 17.
1072	
1073	To minimize the sum, we use the method of Lagrange multipliers. We find that each  $(a_k)$  is proportional to  $(2k-1)$ . Thus,  $(a_k = \frac{17(2k-1)}{n^2})$ .
1074	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "8d171140-a3a2-45f5-a433-68428113926f",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "9f9c8d3e-1c8a-4947-bc05-7164f47f2c36",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt",
      "content": "```\n\nI need to determine the sum of 1 and 2.\n\nAdding these two numbers together, 1 plus 2 equals 3.\n\nTherefore, the answer is 3.\n\n```\n&lt;/think>\n```\n\nSure! Let's solve the problem step by step.\n\n```\n**Problem:** What is  $(1 + 2)$ ?\n```\n\n```\n**Solution:**\n```\n\nTo find the sum of 1 and 2, simply add the two numbers together:\n\n```\n\\[\n1 + 2 = 3\n\\]\n```\n\n```\n**Answer:**\n```\n\n```\n\\(\\boxed{3}\\)\n```\n\n```\n---\n```\n\n```\n## Question\n{question}\n```\n\n```\n## Response\n```#### Listing 4 | An example prompt of using DeepSeek-V3 as a judge.\n\n```\nAs an advanced reasoning problem evaluation assistant, your primary responsibility is to assess the accuracy of provided answers. You will be presented with a reasoning-related question, its corresponding reference answer, and an answer requiring evaluation.\n\n## Answer Quality Classification\nYou have to carefully analyze and classify the answer into one of the following two levels:\n1. correct: The answer fully aligns with the reference answer in both reasoning process and final conclusion, and address the question without any errors or omissions.\n2. incorrect: The answer contains major errors in key reasoning steps or the final conclusion, or completely deviates from the core of the question. This indicates a fundamental misunderstanding or error in comprehending the question.\n\n## Question\n{question}\n\n## Reference Answer\n{reference}\n\n## Answer to be Evaluated\n{answer}\n\n## Output Format\nYou need to combine the question and reference answer, first provide a detailed explanation of your analysis of the answer to be evaluated, then conclude with the final answer quality classification.\nOutput the following content in JSON format, including two key:\n1. 'analysis': analysis of the answer's correctness;\n2. 'correctness': correct/incorrect\n```\n\n### B.3.3. 800K Supervised Data\n\n**Reasoning Data** We curate a large set of reasoning prompts and generate reasoning trajectories by performing rejection sampling from the checkpoint of the first-stage RL training. In the previous stage, we only included data that could be evaluated using rule-based rewards. However, in this stage, we expand the dataset by incorporating additional data, some of which uses a generative reward model by feeding the ground-truth and model predictions into DeepSeek-V3 for judgment, an example prompt is provided in Listing 4. Additionally, because the model output is sometimes chaotic and difficult to read, we have filtered out chain-of-thought with mixed languages, long paragraphs, and code blocks. For each prompt, we sample multiple responses and retain only the correct ones. In total, we collect about 600k reasoning-related training samples.\n\n**Non-Reasoning Data** For non-reasoning data, such as writing, factual QA, self-cognition, and translation, we adopt the DeepSeek-V3 pipeline and reuse portions of the SFT dataset of DeepSeek-V3. We also incorporate software engineering-focused data, including program repair and front-end web development, to enhance the model's ability to solve real-world problems. For certain non-reasoning tasks, we call DeepSeek-V3 to generate a potential chain-of-thought before answering the question by prompting. However, for simpler queries, such as \"hello\" we do not provide a CoT in response. In the end, we collected a total of approximately 200k training samples that are unrelated to reasoning.When designing our thinking process style, we ask the model to follow key principles: First, keep each paragraph concise and digestible. Short paragraphs make ideas clearer and easier to follow. Second, adopt a conversational tone that feels natural and engaging. We avoid technical formatting like markdown to maintain a smooth reading experience. Third, and most importantly, the thinking process begins by understanding the complete user context. This means analyzing who our users are, what situations they’re dealing with, and what they truly need - including those unstated needs that may lie beneath the surface of their initial request.\n\nAfter eliciting these thinking processes from the model, human annotators meticulously verify the accuracy of the outputs. Our findings indicate that these artificial reasoning traces enhance the model’s precision in interpreting user queries. Specifically, they effectively highlight format constraints, clarify user intentions, and elucidate the requisite structure of outputs. This methodological approach facilitates more accurate and responsive interactions between the model and users.\n\nTable 5 | Data Statistics of SFT Data.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Domain&lt;/th>\n&lt;th>Num Samples&lt;/th>\n&lt;th>Avg Rounds&lt;/th>\n&lt;th>Avg Tokens&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Math&lt;/td>\n&lt;td>395285&lt;/td>\n&lt;td>1.0&lt;/td>\n&lt;td>6094.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Code&lt;/td>\n&lt;td>211129&lt;/td>\n&lt;td>1.1&lt;/td>\n&lt;td>7435.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>STEM&lt;/td>\n&lt;td>10124&lt;/td>\n&lt;td>1.0&lt;/td>\n&lt;td>4928.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Logic&lt;/td>\n&lt;td>10395&lt;/td>\n&lt;td>1.0&lt;/td>\n&lt;td>2739.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>General&lt;/td>\n&lt;td>177812&lt;/td>\n&lt;td>1.1&lt;/td>\n&lt;td>1419.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Total&lt;/td>\n&lt;td>804745&lt;/td>\n&lt;td>1.0&lt;/td>\n&lt;td>5355.3&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**SFT Data Statistics** Table 5 summarizes the data statistics across various domains, based on approximately 800,000 supervised samples. It is worth noting that the majority of the data consists of single-turn interactions, which may limit the multi-turn conversational capabilities of DeepSeek-R1. We leave the expansion to multi-turn dialogue data as future work. The math-related data are primarily in Chinese and English, spanning a wide range of topics and difficulty levels. These questions are verifiable, either through deterministic rules or by reference to specific ground-truth answers. The code dataset encompasses not only competitive programming problems but also debugging tasks and project-oriented coding queries. STEM and logic-related questions, although smaller in volume compared to mathematics and code, are sourced from publicly available textbooks and online repositories. The general-domain queries are diverse, predominantly in Chinese and English, and include tasks such as creative writing, open-ended question answering, role-playing scenarios, and more.\n\n**Examples of SFT Trajectories** We provide examples of SFT trajectories related to math, code, and non-reasoning in Listings 5, 6, and 7.\n\nListing 5 | An example SFT trajectory from reasoning data related to mathematics.\n\n```\n## Question\nFor positive integer  $n$ , define  $S_n$  to be the minimum value of the sum  $\\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2}$ , where  $a_1, a_2, \\dots, a_n$  are positive real numbers whose sum is 17. There is a unique positive integer  $n$  for which  $S_n$  is also an integer. Find this  $n$ .\n\n## Response\n```&lt;think>\n\nAlright, so I'm trying to solve this problem where I need to find a positive integer  $n$  such that  $S_n$ , the minimum value of the sum  $\\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2}$ , is an integer. Here,  $(a_1, a_2, \\dots, a_n)$  are positive real numbers that add up to 17.\n\nHmm, okay, let me break this down. I know that when you have a sum of square roots like this, it often relates to geometry, maybe minimizing distances. It reminds me of the problem where you have to break up a path into segments with certain slopes to minimize total distance. Maybe this is similar to finding the shortest path in a staircase.\n\nLet me visualize it. Each term  $\\sqrt{(2k-1)^2 + a_k^2}$  looks like the hypotenuse of a right-angled triangle with legs  $(2k-1)$  and  $a_k$ . So, if I imagine a grid where I move horizontally by  $a_k$  and vertically by  $(2k-1)$  for each step  $k$ , then  $S_n$  would be the total length of this path.\n\nNow, the sum of all  $a_k$  is 17, which would be the total horizontal distance. I need to figure out the vertical distances, which are fixed based on  $k$ . So the total vertical distance would be  $\\sum_{k=1}^n (2k-1)$ . Let me compute that:\n\nThe sum  $\\sum_{k=1}^n (2k-1)$  is equal to  $2 \\sum_{k=1}^n k - \\sum_{k=1}^n 1 = 2 \\cdot \\frac{n(n+1)}{2} - n = n(n+1) - n = n^2$ . So the total vertical distance is  $n^2$ .\n\nWait a second, so this entire setup is like moving from the origin to the point  $(17, n^2)$  with  $n$  segments. Each segment has a horizontal component  $a_k$  and a vertical component  $(2k-1)$ . But in reality, this entire path from  $(0, 0)$  to  $(17, n^2)$  can be considered as a single straight line if we could somehow combine all these segments.\n\nBut we can't change the number of segments  $n$ ; each segment's vertical component is fixed. However, the horizontal components  $a_k$  can be adjusted as long as their sum is 17. So, to find the minimal total distance, maybe we can think of it as if each segment is contributing to the total path optimally. If we scale each horizontal component  $a_k$  proportionally, maybe this also corresponds to scaling the vertical components.\n\nAlternatively, I can think of calculus optimization techniques. If I need to minimize the sum  $\\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2}$  subject to  $\\sum_{k=1}^n a_k = 17$ , I can use the method of Lagrange multipliers.\n\nLet me set up the Lagrangian. Let  $L = \\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2} + \\lambda (17 - \\sum_{k=1}^n a_k)$ .\n\nTaking the derivative of  $L$  with respect to each  $a_k$ :\n\n$$\\frac{\\partial L}{\\partial a_k} = \\frac{a_k}{\\sqrt{(2k-1)^2 + a_k^2}} - \\lambda = 0$$\n\nSo, for each  $k$ , we have  $\\frac{a_k}{\\sqrt{(2k-1)^2 + a_k^2}} = \\lambda$ . Let me solve for  $a_k$ :\n\nSquaring both sides gives  $\\frac{a_k^2}{(2k-1)^2 + a_k^2} = \\lambda^2$ .\n\nRearranging terms:  $a_k^2 = \\lambda^2 \\left( (2k-1)^2 + a_k^2 \\right)$ .\n\nDivide both sides by  $a_k^2$  (assuming  $a_k \\neq 0$ ):  $1 = \\lambda^2 \\left( \\frac{(2k-1)^2}{a_k^2} + 1 \\right)$ .Simplify:  $\\sqrt{1 - \\lambda^2} = \\lambda \\sqrt{\\frac{(2k-1)^2}{a_k^2}}$ .\n\nThen,  $\\sqrt{\\frac{(2k-1)^2}{a_k^2}} = \\sqrt{\\frac{1-\\lambda^2}{\\lambda^2}}$ .\n\nTherefore,  $\\sqrt{\\frac{2k-1}{a_k}} = \\sqrt{\\frac{1-\\lambda^2}{\\lambda^2}} = \\frac{\\sqrt{1-\\lambda^2}}{\\lambda}$ .\n\nLet me denote  $c = \\frac{\\sqrt{1-\\lambda^2}}{\\lambda}$ . Then,  $a_k = \\frac{2k-1}{c}$ .\n\nSo, each  $a_k$  is proportional to  $(2k-1)$ . That is,  $a_k = \\frac{2k-1}{c}$ .\n\nSince the sum of all  $a_k$  is 17, we can write:\n\n$\\sum_{k=1}^n a_k = \\sum_{k=1}^n \\frac{2k-1}{c} = \\frac{1}{c} \\sum_{k=1}^n (2k-1)$ .\n\nEarlier, I found that  $\\sum_{k=1}^n (2k-1) = n^2$ . Therefore,\n\n$\\frac{n^2}{c} = 17 \\Rightarrow c = \\frac{n^2}{17}$ .\n\nThus,  $a_k = \\frac{2k-1}{c} = \\frac{(2k-1) \\cdot 17}{n^2}$ .\n\nNow, going back to the original expression for  $S_n$ :\n\n$S_n = \\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2}$ .\n\nSubstituting  $a_k = \\frac{17(2k-1)}{n^2}$ , we get:\n\n$\\sqrt{(2k-1)^2 + \\left(\\frac{17(2k-1)}{n^2}\\right)^2} = (2k-1) \\sqrt{1 + \\left(\\frac{17}{n^2}\\right)^2}$ .\n\nSo, factor that square root out of the sum:\n\n$S_n = \\sqrt{1 + \\left(\\frac{17}{n^2}\\right)^2} \\cdot \\sum_{k=1}^n (2k-1)$ .\n\nWe already know that  $\\sum_{k=1}^n (2k-1) = n^2$ , so this simplifies to:\n\n$S_n = \\sqrt{1 + \\left(\\frac{17}{n^2}\\right)^2} \\cdot n^2 = \\sqrt{n^4 + 17^2} = \\sqrt{n^4 + 289}$ .\n\nWait, that seems too simplified. Let me check my steps:\n\n1. 1. I set up the Lagrangian correctly.\n2. 2. Took the derivative and found  $a_k = \\frac{2k-1}{c}$ .\n3. 3. Summed them up to get  $c = \\frac{n^2}{17}$ .\n4. 4. Plugged back into  $S_n$  and factored out  $(2k-1)$ , so each term becomes  $(2k-1) \\sqrt{1 + \\left(\\frac{17}{n^2}\\right)^2}$ .\n5. 5. Since  $\\sum (2k-1) = n^2$ , so total sum is  $n^2 \\sqrt{1 + \\left(\\frac{17}{n^2}\\right)^2} = \\sqrt{n^4 + 17^2}$ .\n\nYeah, that seems to check out. So,  $S_n = \\sqrt{n^4 + 289}$ . Wait,  $17^2$  is 289.\n\nTherefore,  $S_n = \\sqrt{n^4 + 289}$ . We need this to be an integer.\n\nSo, I need to find an integer  $n$  such that  $n^4 + 289$  is a perfect square.\n\nLet me denote  $S_n = m$ , where  $m$  is an integer, so:\n\n$n^4 + 289 = m^2$ .This implies  $(m^2 - n^4 = 289)$ .\n\nHmm, 289 is  $17^2$ . So,  $(m^2 - n^4 = 17^2)$ . That can be written as:\n\n$$(m^2 - n^4 = (17)^2)$$\n\nLooking at this equation, it's a difference of squares.\n\n$$(m^2 - n^4 = (m - n^2)(m + n^2) = 17^2 = 289)$$\n\nSo, we have  $(m - n^2)(m + n^2) = 289$ .\n\nSince  $(m)$  and  $(n)$  are positive integers, both  $(m - n^2)$  and  $(m + n^2)$  are positive integers and factors of 289. Also,  $(m + n^2 > m - n^2)$ .\n\nSo, since 289 is  $17^2$ , its positive factor pairs are (1, 289) and (17, 17).\n\nHence, the factor pairs are:\n\n1. 1.  $(m - n^2 = 1)$  and  $(m + n^2 = 289)$ .\n2. 2.  $(m - n^2 = 17)$  and  $(m + n^2 = 17)$ .\n\nBut the second case gives  $(m - n^2 = 17)$  and  $(m + n^2 = 17)$ .\n\nSubtracting the equations:  $(m + n^2) - (m - n^2) = 17 - 17 \\Rightarrow (2n^2 = 0) \\Rightarrow (n^2 = 0)$ . But  $(n)$  is a positive integer, so this case is invalid.\n\nSo, we only consider the first factor pair:  $(m - n^2 = 1)$  and  $(m + n^2 = 289)$ .\n\nAdding the two equations:  $(m - n^2) + (m + n^2) = 1 + 289 \\Rightarrow (2m = 290) \\Rightarrow (m = 145)$ .\n\nSubtracting the two equations:  $(m + n^2) - (m - n^2) = 289 - 1 \\Rightarrow (2n^2 = 288) \\Rightarrow (n^2 = 144) \\Rightarrow (n = 12)$  since  $(n)$  is positive.\n\nTherefore,  $(n = 12)$ .\n\nBefore I conclude, let me verify that  $(S_n = \\sqrt{12^4 + 17^2} = \\sqrt{20736 + 289} = \\sqrt{21025} = 145)$ , which is indeed an integer.\n\nIs this the only  $(n)$ ? The question says there's a unique positive integer  $(n)$ , so this must be the one.\n\n**\\*\\*Final Answer\\*\\***\n\nThe unique positive integer  $(n)$  is  $\\boxed{12}$ .  \n&lt;/think>\n\nTo solve the problem, we need to find a positive integer  $(n)$  such that  $(S_n)$ , the minimum value of the sum  $(\\sum_{k=1}^n \\sqrt{(2k-1)^2 + a_k^2})$ , is an integer. Here,  $(a_1, a_2, \\dots, a_n)$  are positive real numbers whose sum is 17.\n\nFirst, we recognize that each term  $(\\sqrt{(2k-1)^2 + a_k^2})$  represents the hypotenuse of a right-angled triangle with legs  $(2k-1)$  and  $(a_k)$ . The total vertical distance is the sum of the vertical components, which is  $(\\sum_{k=1}^n (2k-1) = n^2)$ . The total horizontal distance is the sum of  $(a_k)$ , which is 17.\n\nTo minimize the sum, we use the method of Lagrange multipliers. We find that each  $(a_k)$  is proportional to  $(2k-1)$ . Thus,  $(a_k = \\frac{17(2k-1)}{n^2})$ .\n",
      "numLines": 275,
      "startLine": 800,
      "totalLines": 1074
    }
  },
  "sourceToolAssistantUUID": "8d171140-a3a2-45f5-a433-68428113926f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 39 · 2026-05-28T11:21:14.280Z_

```json
{
  "parentUuid": "9f9c8d3e-1c8a-4947-bc05-7164f47f2c36",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "389fe699-1e82-43cf-8e32-c09010f89822",
  "timestamp": "2026-05-28T11:21:14.280Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "389fe699-1e82-43cf-8e32-c09010f89822",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze DeepSeek-R1 reasoning innovation approach",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Tool call

_source line 42 · 2026-05-28T11:21:19.853Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KAnbCfXPEPAPGR8zm8KsSA`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt",
  "offset": 1074,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "389fe699-1e82-43cf-8e32-c09010f89822",
  "isSidechain": false,
  "requestId": "req_011CbUsun1oAU9YwDyAPjQxL",
  "type": "assistant",
  "uuid": "9e5d02a5-250b-4851-926b-c170834b5ff5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcJuSnwZyPavDHqhLzxqzs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6108,
      "cache_read_input_tokens": 38631,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6108,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 38631,
          "cache_creation_input_tokens": 6108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6108
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

_source line 43 · 2026-05-28T11:21:19.857Z_

<details><summary>↩ Tool result · `toolu_01KAnbCfXPEPAPGR8zm8KsSA`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1074). The file has 1074 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e5d02a5-250b-4851-926b-c170834b5ff5",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "0f00e794-a702-4ec2-bb39-1f9a8ac9ced0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu/a97a0a13-710e-4482-a7b3-a1528324cc9e/tool-results/toolu_01QWfaJBSTkqKvr7Fgn1At6U.txt",
      "content": "",
      "numLines": 1,
      "startLine": 1074,
      "totalLines": 1074
    }
  },
  "sourceToolAssistantUUID": "9e5d02a5-250b-4851-926b-c170834b5ff5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-28T11:21:55.340Z_

<details><summary>Logged reasoning block</summary>

```text
I've now read the full paper content. Let me also try to fetch the Nature publication page for any additional context, and check if there are reviewer comments anywhere (Nature papers don't typically have public reviewer comments like OpenReview, but let me check).

Let me also look for the distillation section and any other key parts I might have missed. The paper is quite long. Let me now synthesize what I've learned.

Key points from my reading:

**Problem Identification:**
- The paper identifies that existing LLM reasoning capabilities are constrained by human-annotated reasoning traces (SFT data). This creates a ceiling effect where models can only replicate human thought patterns.


- The core question becomes: can we develop reasoning capabilities through RL alone, without relying on human-labeled reasoning trajectories?

**Key Insight:**
- Pure RL with rule-based rewards (no neural reward models, no SFT) can incentivize emergent reasoning behaviors like self-verification, reflection, and dynamic strategy adaptation. The model discovers these behaviors autonomously through the reward signal alone.
- The "aha moment" - the model spontaneously develops self-correction behaviors (saying "Wait, let me reconsider...")

**Method:**
1. DeepSeek-R1-Zero: Pure RL (GRPO) on DeepSeek-V3-Base with only rule-based rewards...

implications for how we think about training reasoning systems. The simplification itself—removing SFT and neural reward models—is the innovation, showing that emergent reasoning emerges naturally from straightforward reward signals.

Looking at how this connects to our work: DeepSeek-R1 essentially defines the reasoning landscape we're operating in, and their finding about uncontrolled self-verification aligns perfectly with what we're trying to solve—deciding when to supplement or replace that internal reasoning with external verification signals. The distillation work also matters for us since it suggests we could estimate problem difficulty from early token patterns in smaller models.

The main gaps they acknowledge—token inefficiency on simple problems, language mixing, prompt sensitivity, and reward hacking—are exactly where adaptive verification could add value.

What makes this a landmark paper is the elegant simplicity of the result: pure RL just produces reasoning without explicit supervision, demonstrated at massive scale with broad evaluation coverage, plus the open-source release gives the whole field a new baseline to build on.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f00e794-a702-4ec2-bb39-1f9a8ac9ced0",
  "isSidechain": false,
  "requestId": "req_011CbUsvPj8Pm9qJ9WnSh9GM",
  "type": "assistant",
  "uuid": "7c1725b0-3e7e-4e0a-a65a-938ed86f2917",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177B3CiR5VFzUBzE1AvrFGM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 205,
      "cache_read_input_tokens": 44739,
      "output_tokens": 1014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1014,
          "cache_read_input_tokens": 44739,
          "cache_creation_input_tokens": 205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 205
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

_source line 45 · 2026-05-28T11:21:55.778Z_

Now I have the full paper content. Let me also check if there's a Nature review or discussion available:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c1725b0-3e7e-4e0a-a65a-938ed86f2917",
  "isSidechain": false,
  "requestId": "req_011CbUsvPj8Pm9qJ9WnSh9GM",
  "type": "assistant",
  "uuid": "2b30b718-c04e-4fde-ac3d-3e316b72d729",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177B3CiR5VFzUBzE1AvrFGM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 205,
      "cache_read_input_tokens": 44739,
      "output_tokens": 1014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1014,
          "cache_read_input_tokens": 44739,
          "cache_creation_input_tokens": 205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 205
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

_source line 46 · 2026-05-28T11:21:55.941Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NiRcp9fomnx6JB522FakmV`</summary>

```json
{
  "url": "https://www.nature.com/articles/s41586-025-08998-w",
  "prompt": "Extract any editorial commentary, peer review information, reviewer concerns, or supplementary discussion about the DeepSeek-R1 paper. Also extract any \"Reviewer Comments\" or \"Peer Review File\" links if available. Also extract the main conclusions and any editor's summary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b30b718-c04e-4fde-ac3d-3e316b72d729",
  "isSidechain": false,
  "requestId": "req_011CbUsvPj8Pm9qJ9WnSh9GM",
  "type": "assistant",
  "uuid": "33c9e9aa-4282-425e-b015-5be115c4b8ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177B3CiR5VFzUBzE1AvrFGM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 205,
      "cache_read_input_tokens": 44739,
      "output_tokens": 1014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1014,
          "cache_read_input_tokens": 44739,
          "cache_creation_input_tokens": 205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 205
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

_source line 47 · 2026-05-28T11:21:56.527Z_

<details><summary>↩ Tool result · `toolu_01NiRcp9fomnx6JB522FakmV`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://www.nature.com/articles/s41586-025-08998-w
Redirect URL: https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-025-08998-w
Status: 303 See Other

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-025-08998-w"
- prompt: "Extract any editorial commentary, peer review information, reviewer concerns, or supplementary discussion about the DeepSeek-R1 paper. Also extract any "Reviewer Comments" or "Peer Review File" links if available. Also extract the main conclusions and any editor's summary."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33c9e9aa-4282-425e-b015-5be115c4b8ff",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "433e69d4-2b35-458d-88e3-7659a36de28e",
  "toolUseResult": {
    "bytes": 869,
    "code": 303,
    "codeText": "See Other",
    "result": "REDIRECT DETECTED: The URL redirects to a different host.\n\nOriginal URL: https://www.nature.com/articles/s41586-025-08998-w\nRedirect URL: https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-025-08998-w\nStatus: 303 See Other\n\nTo complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:\n- url: \"https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-025-08998-w\"\n- prompt: \"Extract any editorial commentary, peer review information, reviewer concerns, or supplementary discussion about the DeepSeek-R1 paper. Also extract any \"Reviewer Comments\" or \"Peer Review File\" links if available. Also extract the main conclusions and any editor's summary.\"",
    "durationMs": 582,
    "url": "https://www.nature.com/articles/s41586-025-08998-w"
  },
  "sourceToolAssistantUUID": "33c9e9aa-4282-425e-b015-5be115c4b8ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-28T11:22:00.182Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WdX4UKnFNv9CoYtrpuEDDc`</summary>

```json
{
  "url": "https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-025-08998-w",
  "prompt": "Extract any editorial commentary, peer review information, reviewer concerns, or supplementary discussion about the DeepSeek-R1 paper. Also extract any Reviewer Comments or Peer Review File links. Extract the main conclusions and editor's summary if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "433e69d4-2b35-458d-88e3-7659a36de28e",
  "isSidechain": false,
  "requestId": "req_011CbUsxtihph4dTkfXqjtcD",
  "type": "assistant",
  "uuid": "dd0cc5d9-30ee-47b0-8376-1414f10a43c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYqRR73HqUu2mD33PfKwrc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1303,
      "cache_read_input_tokens": 44944,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1303,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 44944,
          "cache_creation_input_tokens": 1303,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1303
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

_source line 49 · 2026-05-28T11:22:00.932Z_

<details><summary>↩ Tool result · `toolu_01WdX4UKnFNv9CoYtrpuEDDc`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://idp.nature.com/transit?redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-025-08998-w&code=80bd7132-efb0-42d6-be52-09491653dab1
Redirect URL: https://www.nature.com/articles/s41586-025-08998-w?error=cookies_not_supported&code=80bd7132-efb0-42d6-be52-09491653dab1
Status: 302 Found

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://www.nature.com/articles/s41586-025-08998-w?error=cookies_not_supported&code=80bd7132-efb0-42d6-be52-09491653dab1"
- prompt: "Extract any editorial commentary, peer review information, reviewer concerns, or supplementary discussion about the DeepSeek-R1 paper. Also extract any Reviewer Comments or Peer Review File links. Extract the main conclusions and editor's summary if available."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd0cc5d9-30ee-47b0-8376-1414f10a43c4",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "e53d106c-fc80-47c2-b501-c6ac6fe6b877",
  "toolUseResult": {
    "bytes": 900,
    "code": 302,
    "codeText": "Found",
    "result": "REDIRECT DETECTED: The URL redirects to a different host.\n\nOriginal URL: https://idp.nature.com/transit?redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-025-08998-w&code=80bd7132-efb0-42d6-be52-09491653dab1\nRedirect URL: https://www.nature.com/articles/s41586-025-08998-w?error=cookies_not_supported&code=80bd7132-efb0-42d6-be52-09491653dab1\nStatus: 302 Found\n\nTo complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:\n- url: \"https://www.nature.com/articles/s41586-025-08998-w?error=cookies_not_supported&code=80bd7132-efb0-42d6-be52-09491653dab1\"\n- prompt: \"Extract any editorial commentary, peer review information, reviewer concerns, or supplementary discussion about the DeepSeek-R1 paper. Also extract any Reviewer Comments or Peer Review File links. Extract the main conclusions and editor's summary if available.\"",
    "durationMs": 745,
    "url": "https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-025-08998-w"
  },
  "sourceToolAssistantUUID": "dd0cc5d9-30ee-47b0-8376-1414f10a43c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-28T11:22:05.096Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YAhfKfrJ5daXjAGNn4AEAX`</summary>

```json
{
  "url": "https://www.nature.com/articles/s41586-025-08998-w?error=cookies_not_supported&code=80bd7132-efb0-42d6-be52-09491653dab1",
  "prompt": "Extract all available content about the DeepSeek-R1 paper including: abstract, any editor summary, peer review file links, reviewer comments, and any editorial notes. Also note if there's a \"Transparent Peer Review\" or \"Peer Review File\" link."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e53d106c-fc80-47c2-b501-c6ac6fe6b877",
  "isSidechain": false,
  "requestId": "req_011CbUsyDV4PczeEUM8m4tKJ",
  "type": "assistant",
  "uuid": "dcda3611-8d9a-4a21-a1de-39d72776ef29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NJFyoC7cpoBDJXD9aX99Fz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 499,
      "cache_read_input_tokens": 46247,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 499,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 46247,
          "cache_creation_input_tokens": 499,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 499
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

_source line 51 · 2026-05-28T11:22:09.466Z_

<details><summary>↩ Tool result · `toolu_01YAhfKfrJ5daXjAGNn4AEAX`</summary>

```text
# Response

The provided webpage content does not contain any information about a DeepSeek-R1 paper. The content is entirely focused on a Nature article published May 14, 2025, titled "Genome diversity and signatures of natural selection in mainland Southeast Asia" (article ID: s41586-025-08998-w).

The page includes:
- The article abstract describing a genome dataset of 3,023 individuals from Southeast Asian populations
- Author affiliations and contributor information
- References section
- Data availability statements
- Acknowledgements

There is no mention of DeepSeek-R1, peer review files, transparent peer review links, editor summaries, or reviewer comments visible in the provided text. To access peer review information for this Nature article, you would need to navigate to the full article page and look for a "Peer Review File" or "Transparent Peer Review" section, which does not appear in the content excerpt provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcda3611-8d9a-4a21-a1de-39d72776ef29",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "0cfbb214-e8d1-4811-847a-b568bf05c56a",
  "toolUseResult": {
    "bytes": 688496,
    "code": 200,
    "codeText": "OK",
    "result": "# Response\n\nThe provided webpage content does not contain any information about a DeepSeek-R1 paper. The content is entirely focused on a Nature article published May 14, 2025, titled \"Genome diversity and signatures of natural selection in mainland Southeast Asia\" (article ID: s41586-025-08998-w).\n\nThe page includes:\n- The article abstract describing a genome dataset of 3,023 individuals from Southeast Asian populations\n- Author affiliations and contributor information\n- References section\n- Data availability statements\n- Acknowledgements\n\nThere is no mention of DeepSeek-R1, peer review files, transparent peer review links, editor summaries, or reviewer comments visible in the provided text. To access peer review information for this Nature article, you would need to navigate to the full article page and look for a \"Peer Review File\" or \"Transparent Peer Review\" section, which does not appear in the content excerpt provided.",
    "durationMs": 4366,
    "url": "https://www.nature.com/articles/s41586-025-08998-w?error=cookies_not_supported&code=80bd7132-efb0-42d6-be52-09491653dab1"
  },
  "sourceToolAssistantUUID": "dcda3611-8d9a-4a21-a1de-39d72776ef29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-28T11:22:12.700Z_

<details><summary>Logged reasoning block</summary>

```text
That wasn't the right Nature article. Let me search for the correct DOI for the DeepSeek-R1 Nature paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cfbb214-e8d1-4811-847a-b568bf05c56a",
  "isSidechain": false,
  "requestId": "req_011CbUsyr3zLhwaQ3gWPQmA6",
  "type": "assistant",
  "uuid": "e56dc94a-7ec7-4930-bba7-0de3bc365a43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhCDNLvDZwTgB6h3N6tEKx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 393,
      "cache_read_input_tokens": 46746,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 393,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 46746,
          "cache_creation_input_tokens": 393,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 393
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

_source line 53 · 2026-05-28T11:22:14.272Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018bizisy6kuBboNWE6aPdz4`</summary>

```json
{
  "url": "https://scholar.google.com/scholar?q=DeepSeek-R1+Incentivizing+Reasoning+Capability+Nature+2025",
  "prompt": "Find the Nature DOI or URL for the DeepSeek-R1 paper \"Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\" published in Nature 2025. Extract any citation information and the correct Nature article URL."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e56dc94a-7ec7-4930-bba7-0de3bc365a43",
  "isSidechain": false,
  "requestId": "req_011CbUsyr3zLhwaQ3gWPQmA6",
  "type": "assistant",
  "uuid": "005d6f88-740f-4685-ad40-22641aa0e00a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhCDNLvDZwTgB6h3N6tEKx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 393,
      "cache_read_input_tokens": 46746,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 393,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 46746,
          "cache_creation_input_tokens": 393,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 393
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

_source line 54 · 2026-05-28T11:22:14.739Z_

<details><summary>↩ Tool result · `toolu_018bizisy6kuBboNWE6aPdz4`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "005d6f88-740f-4685-ad40-22641aa0e00a",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "8aaecbac-c884-4994-b6ab-b4849c3ee23c",
  "toolUseResult": {
    "bytes": 0,
    "code": 403,
    "codeText": "Forbidden",
    "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 463,
    "url": "https://scholar.google.com/scholar?q=DeepSeek-R1+Incentivizing+Reasoning+Capability+Nature+2025"
  },
  "sourceToolAssistantUUID": "005d6f88-740f-4685-ad40-22641aa0e00a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-28T11:22:18.360Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013au73E1DYvJFaiczKsUWzg`</summary>

```json
{
  "url": "https://api.semanticscholar.org/graph/v1/paper/arXiv:2501.12948?fields=title,venue,citationCount,influentialCitationCount,externalIds,publicationDate",
  "prompt": "Extract all the metadata about this paper including venue, citation count, DOI, and any other identifiers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aaecbac-c884-4994-b6ab-b4849c3ee23c",
  "isSidechain": false,
  "requestId": "req_011CbUszEXqmeUdXrSJbYrLh",
  "type": "assistant",
  "uuid": "f48001da-3451-408a-89a1-1e26ac85efdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QDXUvE16FoJQcTpGVqkQp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 266,
      "cache_read_input_tokens": 47139,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 47139,
          "cache_creation_input_tokens": 266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 266
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

_source line 56 · 2026-05-28T11:22:18.797Z_

<details><summary>↩ Tool result · `toolu_013au73E1DYvJFaiczKsUWzg`</summary>

```text
The server returned HTTP 429 Too Many Requests.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f48001da-3451-408a-89a1-1e26ac85efdf",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "05613aed-f8db-41ee-a4cb-dbdddb4e5008",
  "toolUseResult": {
    "bytes": 0,
    "code": 429,
    "codeText": "Too Many Requests",
    "result": "The server returned HTTP 429 Too Many Requests.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 434,
    "url": "https://api.semanticscholar.org/graph/v1/paper/arXiv:2501.12948?fields=title,venue,citationCount,influentialCitationCount,externalIds,publicationDate"
  },
  "sourceToolAssistantUUID": "f48001da-3451-408a-89a1-1e26ac85efdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-28T11:22:23.138Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try to find the correct Nature article for DeepSeek-R1. Based on the arXiv page, the DOI is 10.48550/arXiv.2501.12948 which is just the arXiv DOI. The Nature reference says volume 645, pages 633-638, 2025. Let me try to find the correct Nature DOI.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05613aed-f8db-41ee-a4cb-dbdddb4e5008",
  "isSidechain": false,
  "requestId": "req_011CbUszXt8PcA5RZpZHyqrA",
  "type": "assistant",
  "uuid": "b4d2aad9-df2d-43e5-8117-8fe1d7ca7b8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152kSrAc5QKYEMfy3wGTEv1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 208,
      "cache_read_input_tokens": 47405,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 208,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 47405,
          "cache_creation_input_tokens": 208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 208
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

_source line 58 · 2026-05-28T11:22:24.357Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RccQQPwsSSL936aHTFfYs1`</summary>

```json
{
  "url": "https://www.nature.com/nature/volumes/645",
  "prompt": "Find the DeepSeek-R1 paper in this volume listing. Look for any article about reasoning, reinforcement learning, or LLMs by DeepSeek-AI. Extract the article URL and DOI."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4d2aad9-df2d-43e5-8117-8fe1d7ca7b8c",
  "isSidechain": false,
  "requestId": "req_011CbUszXt8PcA5RZpZHyqrA",
  "type": "assistant",
  "uuid": "6c396049-f943-40a4-a426-c01d1661bcdc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152kSrAc5QKYEMfy3wGTEv1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 208,
      "cache_read_input_tokens": 47405,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 208,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 47405,
          "cache_creation_input_tokens": 208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 208
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

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "6c396049-f943-40a4-a426-c01d1661bcdc",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze DeepSeek-R1 reasoning innovation approach",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Tool result

_source line 61 · 2026-05-28T11:22:24.657Z_

<details><summary>↩ Tool result · `toolu_01RccQQPwsSSL936aHTFfYs1`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://www.nature.com/nature/volumes/645
Redirect URL: https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Fnature%2Fvolumes%2F645
Status: 303 See Other

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Fnature%2Fvolumes%2F645"
- prompt: "Find the DeepSeek-R1 paper in this volume listing. Look for any article about reasoning, reinforcement learning, or LLMs by DeepSeek-AI. Extract the article URL and DOI."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c396049-f943-40a4-a426-c01d1661bcdc",
  "isSidechain": false,
  "promptId": "159e0b22-16b3-4592-aae0-90eaf412ee5c",
  "type": "user",
  "uuid": "9cec8aa2-5f33-4baf-9821-dc5d3d9391a6",
  "toolUseResult": {
    "bytes": 742,
    "code": 303,
    "codeText": "See Other",
    "result": "REDIRECT DETECTED: The URL redirects to a different host.\n\nOriginal URL: https://www.nature.com/nature/volumes/645\nRedirect URL: https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Fnature%2Fvolumes%2F645\nStatus: 303 See Other\n\nTo complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:\n- url: \"https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Fnature%2Fvolumes%2F645\"\n- prompt: \"Find the DeepSeek-R1 paper in this volume listing. Look for any article about reasoning, reinforcement learning, or LLMs by DeepSeek-AI. Extract the article URL and DOI.\"",
    "durationMs": 298,
    "url": "https://www.nature.com/nature/volumes/645"
  },
  "sourceToolAssistantUUID": "6c396049-f943-40a4-a426-c01d1661bcdc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-28T11:22:28.174Z_

<details><summary>Logged reasoning block</summary>

```text
Nature is behind a paywall, so I can't access the reviewer comments. Nature papers typically don't have public review files anyway (unlike conferences). Let me move forward with my analysis based on what I have.

I've read the paper in detail. Let me now compose the final analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cec8aa2-5f33-4baf-9821-dc5d3d9391a6",
  "isSidechain": false,
  "requestId": "req_011CbUszxx18wZGL9WJ2jhSx",
  "type": "assistant",
  "uuid": "544931c6-eb4c-41bb-b6de-50a8345e3a6b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dx3bPTxxDsCb4VvRtVsE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 490,
      "cache_read_input_tokens": 47613,
      "output_tokens": 1752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 490,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1752,
          "cache_read_input_tokens": 47613,
          "cache_creation_input_tokens": 490,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 490
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

_source line 63 · 2026-05-28T11:23:10.857Z_

I now have comprehensive coverage of the paper. Nature papers don't publish reviewer comments publicly like OpenReview conferences. Let me now synthesize the deep analysis.

```json
{
  "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
  "venue": "Nature 2025 (Vol. 645, pp. 633-638)",
  "problem_identification": "The authors identified that LLM reasoning capabilities were bottlenecked by dependence on human-annotated reasoning traces (SFT data), which both limits scalability and constrains models to replicate human thought patterns — preventing discovery of superior non-human reasoning pathways. They found this gap by observing that the conventional SFT→RLHF pipeline treats SFT as mandatory, but hypothesized that SFT might actually suppress exploration by anchoring the model to human priors. The key empirical observation motivating the work was that neural reward models are susceptible to reward hacking at scale, suggesting a simpler reward design might be both more robust and more scalable.",
  "key_insight": "When you remove human-annotated reasoning traces entirely and apply pure RL with only rule-based correctness rewards to a sufficiently capable base model, sophisticated reasoning behaviors — self-verification, reflection, backtracking, dynamic strategy switching — emerge autonomously as instrumentally useful strategies the model discovers through optimization. The SFT stage that everyone assumed was necessary was actually constraining the model's reasoning potential.",
  "innovation_type": "simplification",
  "method_summary": "DeepSeek-R1-Zero applies GRPO (Group Relative Policy Optimization — PPO without a value model, using group-relative advantage normalization) directly to DeepSeek-V3-Base (671B MoE) with only two reward signals: accuracy (binary correctness via rule-based checking or compilers) and format (enforcing &lt;think>...&lt;/think> tags). No SFT, no neural reward models. The model is sampled 16 times per question with answers compared within-group for advantage estimation. This produces emergent long-chain-of-thought reasoning with self-verification but suffers from readability and language-mixing issues. DeepSeek-R1 then refines this through a 4-stage pipeline: (1) cold-start SFT on thousands of curated R1-Zero trajectories rewritten for readability, (2) first RL stage with language consistency reward added, (3) rejection sampling + SFT on ~800K samples (600K reasoning via R1 checkpoint + 200K non-reasoning from V3), (4) second RL stage with mixed rule-based and model-based rewards for reasoning + general helpfulness/safety. Finally, reasoning capabilities are distilled to smaller models (1.5B–70B) via SFT on R1-generated trajectories.",
  "what_makes_it_good": "Three things make this Nature-worthy. First, the core finding is genuinely surprising and has the simplicity of a great scientific result: remove the thing everyone thinks is necessary (SFT), add only a correctness signal, and complex cognitive-like behaviors emerge — this is a clean, falsifiable claim with dramatic implications. Second, the 'aha moment' narrative (where the model spontaneously generates 'Wait, wait. Wait.' during self-correction) is the kind of vivid, memorable evidence that makes a paper iconic — it transforms an engineering result into a scientific discovery about emergent behavior. Third, the practical impact is undeniable: open-source release of frontier reasoning models across 7 sizes, achieving o1-level performance, made this immediately the most impactful open-source reasoning system.",
  "limitations_acknowledged": "The authors are refreshingly candid: token efficiency remains poor (overthinking on easy problems), reward hacking prevents scaling pure RL to tasks without reliable rule-based verifiers (like writing), language mixing persists for non-English/Chinese queries, few-shot prompting degrades performance, and software engineering tasks see limited improvement due to slow RL evaluation cycles. They explicitly note that the pure RL approach only works for 'verifiable tasks' — the scaling law breaks down when you can't construct a reliable reward signal.",
  "open_questions": [
    "The 'emergence' claim is scale-dependent but under-characterized: at what model size does self-verification emerge? Does it require the 671B MoE architecture, or would a 70B dense model exhibit the same emergent behaviors under pure RL? The distilled models inherit these behaviors via SFT, not via RL emergence, so the minimum scale for autonomous emergence remains unknown.",
    "The overthinking problem (excess tokens on easy problems) is acknowledged but unsolved — this directly motivates per-instance adaptive compute allocation: the model itself cannot efficiently decide when to stop reasoning, suggesting external verification-budget control (like our proposed framework) could substantially improve token efficiency.",
    "Reward hacking with neural reward models forced the authors to use only rule-based rewards for reasoning tasks, but this restricts the approach to domains with automated verifiers. How to extend pure RL reasoning to open-ended tasks (creative writing, nuanced reasoning without ground truth) remains the central open challenge."
  ],
  "building_blocks": [
    "GRPO algorithm (PPO without value model, group-relative advantages) — efficient RL for LLMs",
    "Rule-based reward design (accuracy + format rewards, no neural reward models)",
    "Cold-start data curation pipeline (R1-Zero generation → filtering → V3 rewriting → human verification)",
    "Rejection sampling from RL checkpoints for SFT data generation",
    "Language consistency reward (proportion of target-language words)",
    "DeepSeek-V3-Base (671B MoE with MLA and MTP) as foundation",
    "Expert parallelism + redundant hotspot experts for MoE RL training",
    "vLLM-based rollout with MTP self-speculative decoding",
    "Multi-stage pipeline: cold-start SFT → RL → rejection sampling SFT → RL",
    "DeepSeek-V3 as generative judge for non-rule-verifiable data",
    "Distillation via SFT on teacher-generated reasoning trajectories"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "DeepSeek-R1 is foundational context for our adaptive verification allocation work in two critical ways. First, it demonstrates that reasoning models naturally develop internal self-verification (reflection, backtracking) but do so inefficiently — the paper explicitly acknowledges 'overthinking' on easy problems and inadequate verification on hard ones. This is precisely the problem our per-instance adaptive framework addresses: the model's internal verification is uncontrolled, so external verification (ORM/PRM/GenRM) allocation based on difficulty estimation can systematically correct this imbalance. Second, R1's emergent reasoning patterns (entropy spikes at 'wait' moments, increasing response length with difficulty) provide exactly the early-token difficulty signals our online algorithm would exploit — the paper demonstrates these signals exist and are predictable, validating our core assumption that difficulty can be estimated from initial reasoning tokens. Our work can be framed as the 'external verification allocation complement' to R1's internal verification emergence."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "544931c6-eb4c-41bb-b6de-50a8345e3a6b",
  "isSidechain": false,
  "requestId": "req_011CbUszxx18wZGL9WJ2jhSx",
  "type": "assistant",
  "uuid": "f4a11a09-2940-49ca-89c5-957c8ebf23a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4dx3bPTxxDsCb4VvRtVsE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 490,
      "cache_read_input_tokens": 47613,
      "output_tokens": 1752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 490,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1752,
          "cache_read_input_tokens": 47613,
          "cache_creation_input_tokens": 490,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 490
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

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "f4a11a09-2940-49ca-89c5-957c8ebf23a0",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze DeepSeek-R1 reasoning innovation approach",
  "sessionId": "a97a0a13-710e-4482-a7b3-a1528324cc9e"
}
```

---
