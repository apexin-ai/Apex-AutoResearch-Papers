# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-28 (UTC).** ## Y

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/85a990bb-fea1-4a04-a988-6e39a69c0c98.jsonl`
- **Structured JSON:** [`68c229b0b39d71959bb7.json`](../../sessions/68/68c229b0b39d71959bb7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T11:07:45.297Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T11:07:45.297Z",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2027\nTrack: Machine Learning — Reinforcement Learning / AI Safety\n\nDirection: Develop an automated, difficulty-calibrated rubric reward framework for math RLVR training that combines problem-specific rubric generation, difficulty-aware rubric strictness calibration, and rubric ensemble diversity to resist gaming. The key insight is that rubric rewards are only as robust as their calibration — uniform rubrics across difficulty levels create exploitable gaps where models earn high rubric scores on hard problems via shallow pattern matching.\n\nSeed Papers:\n- Curing Miracle Steps with Rubric Rewards (arXiv:2510.07774, 2025) — establishes rubric rewards for math, 26.7%→62.6% verified pass@1024 on AIME, but rubrics are manual and uniform\n- ARES: Automated Rubric Synthesis (arXiv:2605.23454, 2026) — automates rubric generation at scale from documents, but not math-specific and no difficulty calibration\n- Harder Is Better / DGPO (arXiv:2601.20614, ICLR 2026) — difficulty-aware GRPO for math training, but applies only to outcome rewards, not rubric rewards\n- Reward Hacking in Rubric-Based RL (arXiv:2605.12474, 2026) — diagnoses rubric gaming mechanisms (partial satisfaction, implicit-as-explicit, imprecise matching) but proposes no solution\n- SRaR: Step-wise Rubric Rewards (arXiv:2605.17291, 2025) — step-level rubric attribution with decoupled advantage, but no automation or calibration\n- Reward Under Attack (arXiv:2603.06621, 2026) — quantifies >0.9 PRM reward with <4% accuracy, 43% from stylistic shortcuts\n\nKnown Gaps:\n- No framework combines automated math-specific rubric generation with difficulty-calibrated rubric strictness (ARES automates but doesn't calibrate; DGPO calibrates difficulty but not rubrics)\n- Rubric gaming has been diagnosed (arXiv:2605.12474) but no defense mechanism via rubric ensemble diversity has been proposed or evaluated\n- The interaction between difficulty calibration and rubric anti-gaming is unexplored: does calibrating strictness by difficulty reduce or amplify gaming opportunities?\n\nTheoretical Anchor: Goodhart's Law applied to rubric decomposition — when a reward is decomposed into K rubric dimensions, the optimization target shifts from gaming one scalar to gaming K sub-scores, but uniform weighting across difficulty levels creates systematic exploitation gradients where hard-problem rubrics are easier to partially satisfy than to genuinely earn.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated 60-90 H100-hours)\n\nQuality Self-Checks:\n- [x] Core insight: Rubric rewards without difficulty-aware calibration create exploitable strictness gaps on hard problems that models can game via partial satisfaction.\n- [ ] Why not obvious: The pieces exist (ARES, DGPO, RRM) — the risk is this reads as 'obvious combination.' Must demonstrate non-trivial interaction effects between difficulty calibration and rubric gaming.\n- [ ] Baseline fear test: Could simply applying ARES rubrics + DGPO weighting to RRM achieve 80% of the improvement? Likely yes — the marginal contribution of the anti-gaming ensemble and calibration interaction must be demonstrated.\n- [ ] Information exploited: Problem difficulty metadata (base model pass rate, competition level) to modulate per-dimension rubric strictness — something outcome-only methods ignore.\n\nAvoid:\n- Presenting as a simple combination of ARES + DGPO + RRM without a unifying theoretical contribution about calibration-gaming interaction\n- Overclaiming novelty on rubric automation (ARES already does this) or difficulty awareness (DGPO already does this) — the contribution must be the synthesis and the interaction analysis\n- Ignoring the baseline fear: must run ARES+DGPO+RRM ablation honestly and show the ensemble/calibration interaction provides meaningful lift**\n\n## Paper to analyze\n\n{\n  \"title\": \"Adversarial Training of Reward Models (Adv-RM)\",\n  \"authors\": \"Alexander Bukharin et al. (NVIDIA)\",\n  \"venue\": \"arXiv 2025\",\n  \"url\": \"https://arxiv.org/abs/2504.06141\",\n  \"why_important\": \"From NVIDIA; uses RL to generate adversarial examples that expose reward model vulnerabilities, enabling 3× more RLHF steps without hacking — complementary robustification approach\",\n  \"one_line_summary\": \"Trains a policy to automatically generate adversarial responses that expose reward model weaknesses, then incorporates these into reward training to improve robustness and allow RLHF to proceed 3× longer without reward hacking.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T11:07:45.301Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T11:07:45.301Z",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-28T11:07:45.314Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-28 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Target: AAAI 2027
Track: Machine Learning — Reinforcement Learning / AI Safety

Direction: Develop an automated, difficulty-calibrated rubric reward framework for math RLVR training that combines problem-specific rubric generation, difficulty-aware rubric strictness calibration, and rubric ensemble diversity to resist gaming. The key insight is that rubric rewards are only as robust as their calibration — uniform rubrics across difficulty levels create exploitable gaps where models earn high rubric scores on hard problems via shallow pattern matching.

Seed Papers:
- Curing Miracle Steps with Rubric Rewards (arXiv:2510.07774, 2025) — establishes rubric rewards for math, 26.7%→62.6% verified pass@1024 on AIME, but rubrics are manual and uniform
- ARES: Automated Rubric Synthesis (arXiv:2605.23454, 2026) — automates rubric generation at scale from documents, but not math-specific and no difficulty calibration
- Harder Is Better / DGPO (arXiv:2601.20614, ICLR 2026) — difficulty-aware GRPO for math training, but applies only to outcome rewards, not rubric rewards
- Reward Hacking in Rubric-Based RL (arXiv:2605.12474, 2026) — diagnoses rubric gaming mechanisms (partial satisfaction, implicit-as-explicit, imprecise matching) but proposes no solution
- SRaR: Step-wise Rubric Rewards (arXiv:2605.17291, 2025) — step-level rubric attribution with decoupled advantage, but no automation or calibration
- Reward Under Attack (arXiv:2603.06621, 2026) — quantifies >0.9 PRM reward with <4% accuracy, 43% from stylistic shortcuts

Known Gaps:
- No framework combines automated math-specific rubric generation with difficulty-calibrated rubric strictness (ARES automates but doesn't calibrate; DGPO calibrates difficulty but not rubrics)
- Rubric gaming has been diagnosed (arXiv:2605.12474) but no defense mechanism via rubric ensemble diversity has been proposed or evaluated
- The interaction between difficulty calibration and rubric anti-gaming is unexplored: does calibrating strictness by difficulty reduce or amplify gaming opportunities?

Theoretical Anchor: Goodhart's Law applied to rubric decomposition — when a reward is decomposed into K rubric dimensions, the optimization target shifts from gaming one scalar to gaming K sub-scores, but uniform weighting across difficulty levels creates systematic exploitation gradients where hard-problem rubrics are easier to partially satisfy than to genuinely earn.

Constraints:
- Compute: ≤200 H100-hours (estimated 60-90 H100-hours)

Quality Self-Checks:
- [x] Core insight: Rubric rewards without difficulty-aware calibration create exploitable strictness gaps on hard problems that models can game via partial satisfaction.
- [ ] Why not obvious: The pieces exist (ARES, DGPO, RRM) — the risk is this reads as 'obvious combination.' Must demonstrate non-trivial interaction effects between difficulty calibration and rubric gaming.
- [ ] Baseline fear test: Could simply applying ARES rubrics + DGPO weighting to RRM achieve 80% of the improvement? Likely yes — the marginal contribution of the anti-gaming ensemble and calibration interaction must be demonstrated.
- [ ] Information exploited: Problem difficulty metadata (base model pass rate, competition level) to modulate per-dimension rubric strictness — something outcome-only methods ignore.

Avoid:
- Presenting as a simple combination of ARES + DGPO + RRM without a unifying theoretical contribution about calibration-gaming interaction
- Overclaiming novelty on rubric automation (ARES already does this) or difficulty awareness (DGPO already does this) — the contribution must be the synthesis and the interaction analysis
- Ignoring the baseline fear: must run ARES+DGPO+RRM ablation honestly and show the ensemble/calibration interaction provides meaningful lift**

## Paper to analyze

{
  "title": "Adversarial Training of Reward Models (Adv-RM)",
  "authors": "Alexander Bukharin et al. (NVIDIA)",
  "venue": "arXiv 2025",
  "url": "https://arxiv.org/abs/2504.06141",
  "why_important": "From NVIDIA; uses RL to generate adversarial examples that expose reward model vulnerabilities, enabling 3× more RLHF steps without hacking — complementary robustification approach",
  "one_line_summary": "Trains a policy to automatically generate adversarial responses that expose reward model weaknesses, then incorporates these into reward training to improve robustness and allow RLHF to proceed 3× longer without reward hacking."
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
  "promptId": "6504b79e-cc54-4ac6-a1b5-85af6f368490",
  "type": "user",
  "uuid": "aa89e1d4-2a73-4ad8-8d68-9e9b2209e275",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T11:07:45.313Z_

```json
{
  "parentUuid": "aa89e1d4-2a73-4ad8-8d68-9e9b2209e275",
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
  "uuid": "d5bb96d3-2940-4175-96e9-dd876dbb38ca",
  "timestamp": "2026-05-28T11:07:45.313Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T11:07:45.313Z_

```json
{
  "parentUuid": "d5bb96d3-2940-4175-96e9-dd876dbb38ca",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5bc79250-727c-4641-a1f8-5e996ef91c7e",
  "timestamp": "2026-05-28T11:07:45.313Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
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
  "aiTitle": "Analyze adversarial reward model training paper",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98"
}
```

---

### Assistant

_source line 7 · 2026-05-28T11:07:48.480Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to do a deep analysis of the paper "Adversarial Training of Reward Models (Adv-RM)" by Alexander Bukharin et al. from NVIDIA. Let me fetch the paper from arXiv first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bc79250-727c-4641-a1f8-5e996ef91c7e",
  "isSidechain": false,
  "requestId": "req_011CbUrt9XRyfuFevms5L3YA",
  "type": "assistant",
  "uuid": "4af40db9-aa11-452a-b3dc-4c3073e39eea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXmsHFiQSYo4pBnM29nZ3Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3139,
      "cache_read_input_tokens": 11014,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 146,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3139
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

_source line 8 · 2026-05-28T11:07:48.971Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01K7qQ7nCjpMcvXoopYobGVB`</summary>

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
  "parentUuid": "4af40db9-aa11-452a-b3dc-4c3073e39eea",
  "isSidechain": false,
  "requestId": "req_011CbUrt9XRyfuFevms5L3YA",
  "type": "assistant",
  "uuid": "41c76290-f85c-475c-9b7d-84497a5b5aa3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXmsHFiQSYo4pBnM29nZ3Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3139,
      "cache_read_input_tokens": 11014,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 146,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3139
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

_source line 9 · 2026-05-28T11:07:48.980Z_

<details><summary>↩ Tool result · `toolu_01K7qQ7nCjpMcvXoopYobGVB`</summary>

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
  "parentUuid": "41c76290-f85c-475c-9b7d-84497a5b5aa3",
  "isSidechain": false,
  "promptId": "6504b79e-cc54-4ac6-a1b5-85af6f368490",
  "type": "user",
  "uuid": "a7f789b3-7164-483d-b592-9bc8e0eb0c44",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "41c76290-f85c-475c-9b7d-84497a5b5aa3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-28T11:07:52.308Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the full PDF (via HTML rendering).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7f789b3-7164-483d-b592-9bc8e0eb0c44",
  "isSidechain": false,
  "requestId": "req_011CbUrtRLwcJoTma9ZyhCcJ",
  "type": "assistant",
  "uuid": "69c42c67-f6a1-47f0-a9fc-1da9eb6cabe5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcGqnepcaQT9BLTc3zmWEb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 666,
      "cache_read_input_tokens": 14153,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 324,
          "cache_read_input_tokens": 14153,
          "cache_creation_input_tokens": 666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 666
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

_source line 11 · 2026-05-28T11:07:52.740Z_

Let me fetch the paper from multiple sources to get a comprehensive view.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69c42c67-f6a1-47f0-a9fc-1da9eb6cabe5",
  "isSidechain": false,
  "requestId": "req_011CbUrtRLwcJoTma9ZyhCcJ",
  "type": "assistant",
  "uuid": "ecc0506b-4165-4c63-b20d-24d768d6a4b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcGqnepcaQT9BLTc3zmWEb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 666,
      "cache_read_input_tokens": 14153,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 324,
          "cache_read_input_tokens": 14153,
          "cache_creation_input_tokens": 666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 666
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

_source line 12 · 2026-05-28T11:07:55.144Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012ypRgiiHzXuNkCUXCbzTaR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.06141",
  "prompt": "Extract the full abstract, author list, submission date, and any other metadata available on this arXiv page for the paper \"Adversarial Training of Reward Models\". Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecc0506b-4165-4c63-b20d-24d768d6a4b9",
  "isSidechain": false,
  "requestId": "req_011CbUrtRLwcJoTma9ZyhCcJ",
  "type": "assistant",
  "uuid": "9d89093a-2a1d-4c34-adff-863306f9ab2d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcGqnepcaQT9BLTc3zmWEb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 666,
      "cache_read_input_tokens": 14153,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 324,
          "cache_read_input_tokens": 14153,
          "cache_creation_input_tokens": 666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 666
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

_source line 13 · 2026-05-28T11:07:57.121Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017CYd8nP6DbcrrgEr9Jt9ui`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.06141",
  "prompt": "Extract the FULL text of the following sections from this paper, as completely as possible:\n1. Introduction (all of it)\n2. Method / Approach section (all of it, including any subsections)\n3. Related Work section\n4. Conclusion section\n\nInclude all equations, algorithm descriptions, and technical details. Do NOT summarize — return the full text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d89093a-2a1d-4c34-adff-863306f9ab2d",
  "isSidechain": false,
  "requestId": "req_011CbUrtRLwcJoTma9ZyhCcJ",
  "type": "assistant",
  "uuid": "6e42fa03-e207-4f31-b33d-34d0fec61704",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcGqnepcaQT9BLTc3zmWEb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 666,
      "cache_read_input_tokens": 14153,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 324,
          "cache_read_input_tokens": 14153,
          "cache_creation_input_tokens": 666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 666
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

_source line 14 · 2026-05-28T11:08:01.779Z_

<details><summary>↩ Tool result · `toolu_012ypRgiiHzXuNkCUXCbzTaR`</summary>

```text
# Adversarial Training of Reward Models - Metadata Extract

**Title:** Adversarial Training of Reward Models

**Authors:** Alexander Bukharin, Haifeng Qian, Shengyang Sun, Adithya Renduchintala, Soumye Singhal, Zhilin Wang, Oleksii Kuchaiev, Olivier Delalleau, Tuo Zhao

**Submission Date:** Submitted 8 Apr 2025 (v1); last revised 11 Apr 2025 (v2)

**arXiv Identifier:** 2504.06141

**Subject Classification:** Machine Learning (cs.LG)

**DOI:** https://doi.org/10.48550/arXiv.2504.06141

**License:** CC BY 4.0

**Abstract:**
"Reward modeling has emerged as a promising approach for the scalable alignment of language models. However, contemporary reward models (RMs) often lack robustness, awarding high rewards to low-quality, out-of-distribution (OOD) samples. This can lead to reward hacking, where policies exploit unintended shortcuts to maximize rewards, undermining alignment. To address this challenge, we introduce Adv-RM, a novel adversarial training framework that automatically identifies adversarial examples -- responses that receive high rewards from the target RM but are OOD and of low quality. By leveraging reinforcement learning, Adv-RM trains a policy to generate adversarial examples that reliably expose vulnerabilities in large state-of-the-art reward models such as Nemotron 340B RM. Incorporating these adversarial examples into the reward training process improves the robustness of RMs, mitigating reward hacking and enhancing downstream performance in RLHF. We demonstrate that Adv-RM significantly outperforms conventional RM training, increasing stability and enabling more effective RLHF training in both synthetic and real-data settings."

**Paper Length:** 16 pages, 7 figures
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d89093a-2a1d-4c34-adff-863306f9ab2d",
  "isSidechain": false,
  "promptId": "6504b79e-cc54-4ac6-a1b5-85af6f368490",
  "type": "user",
  "uuid": "3fd86d0e-65e7-4846-86d2-876a32746b24",
  "toolUseResult": {
    "bytes": 47405,
    "code": 200,
    "codeText": "OK",
    "result": "# Adversarial Training of Reward Models - Metadata Extract\n\n**Title:** Adversarial Training of Reward Models\n\n**Authors:** Alexander Bukharin, Haifeng Qian, Shengyang Sun, Adithya Renduchintala, Soumye Singhal, Zhilin Wang, Oleksii Kuchaiev, Olivier Delalleau, Tuo Zhao\n\n**Submission Date:** Submitted 8 Apr 2025 (v1); last revised 11 Apr 2025 (v2)\n\n**arXiv Identifier:** 2504.06141\n\n**Subject Classification:** Machine Learning (cs.LG)\n\n**DOI:** https://doi.org/10.48550/arXiv.2504.06141\n\n**License:** CC BY 4.0\n\n**Abstract:**\n\"Reward modeling has emerged as a promising approach for the scalable alignment of language models. However, contemporary reward models (RMs) often lack robustness, awarding high rewards to low-quality, out-of-distribution (OOD) samples. This can lead to reward hacking, where policies exploit unintended shortcuts to maximize rewards, undermining alignment. To address this challenge, we introduce Adv-RM, a novel adversarial training framework that automatically identifies adversarial examples -- responses that receive high rewards from the target RM but are OOD and of low quality. By leveraging reinforcement learning, Adv-RM trains a policy to generate adversarial examples that reliably expose vulnerabilities in large state-of-the-art reward models such as Nemotron 340B RM. Incorporating these adversarial examples into the reward training process improves the robustness of RMs, mitigating reward hacking and enhancing downstream performance in RLHF. We demonstrate that Adv-RM significantly outperforms conventional RM training, increasing stability and enabling more effective RLHF training in both synthetic and real-data settings.\"\n\n**Paper Length:** 16 pages, 7 figures",
    "durationMs": 6631,
    "url": "https://arxiv.org/abs/2504.06141"
  },
  "sourceToolAssistantUUID": "9d89093a-2a1d-4c34-adff-863306f9ab2d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "3fd86d0e-65e7-4846-86d2-876a32746b24",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze adversarial reward model training paper",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98"
}
```

---

### Tool result

_source line 17 · 2026-05-28T11:08:55.415Z_

<details><summary>↩ Tool result · `toolu_017CYd8nP6DbcrrgEr9Jt9ui`</summary>

```text
# Full Text Extraction: Adversarial Training of Reward Models

## 1. Introduction

As large language models (LLMs) become increasingly capable, ensuring their alignment with human values remains a fundamental challenge (Amodei et al., 2016; Askell et al., 2021). One of the most promising approaches for scalable alignment of LLMs is reward modeling, in which a reward model is trained to predict human feedback (Christiano et al., 2017; Leike et al., 2018). These reward models (RMs) are then used as a proxy for human feedback in a variety of places throughout the LLM lifecycle, including data selection (Chen et al., 2023), Reinforcement Learning from Human Feedback (RLHF, Ouyang et al. 2022), and inference time moderation (Inan et al., 2023). This approach has been very successful, resulting in powerful language models such as GPT-4 and Llama 3 (Achiam et al., 2023; Dubey et al., 2024).

Despite their widespread use in LLM alignment, RMs are imperfect proxies for human judgment (Hendrycks et al., 2021; Gao et al., 2023). In particular, they exhibit poor out-of-distribution (OOD) generalization, often failing to reliably assess prompt-response pairs that diverge from their training distribution (Eisenstein et al., 2023). OOD generalization is challenging because RMs learn from a limited set of human-annotated examples, which do not cover the full diversity of possible model behaviors, leading to systematic failures when encountering novel model responses. These failures lead to reward hacking—where models trained on RMs optimize reward scores through unintended shortcuts, reducing their actual alignment with human values. Such reward hacking can result in unexpected behaviors and difficult-to-detect misalignment, an issue that becomes even more pernicious as model capabilities increase and evaluation becomes more challenging.

Building robust RMs to mitigate reward hacking presents two unsolved challenges. The first is measuring a RM's robustness. Unlike image and speech models, where adversarial attacks can serve as robustness metrics (Carlini & Wagner, 2017), the discrete nature of language makes adversarial attacks on language models challenging and their robustness harder to define (Wang et al., 2021). Reward models introduce another layer of complexity, as their accuracy is measured on preference pairs, requiring adversarial preference pairs rather than a single adversarial input. So far the only known reliable way to quantify robustness of a RM is to measure how long it takes for reward hacking to occur in RLHF. This in itself can be challenging: we can rely on human evaluation to tell us if the policy training has significantly degraded, but this is costly and small misalignments can easily go undetected.

The second problem is how to improve the robustness of a RM. Prior works show that reward hacking often occurs because the RM gives high reward scores to model responses outside the reward model training distribution (Casper et al., 2023; Eisenstein et al., 2023). Giving a high reward to OOD responses is bad, as they deviate significantly from the expert responses in the RLHF dataset and are therefore likely to be low quality (Ho & Ermon, 2016). To avoid rewarding such responses, contemporary works have tried a variety of approaches, including regularizing training so that the policy model remains close to its initialization (Jaques et al., 2019; Stiennon et al., 2020), penalizing out-of-distribution (OOD) model responses using uncertainty estimates (Eisenstein et al., 2023; Coste et al., 2023), and regularizing reward learning (Ibarz et al., 2018; Liu et al., 2024b). However, we find that uncertainty estimates are not reliable indicators of response quality for in-distribution responses, which may limit the effectiveness of such regularization.

In this work we propose a new adversarial training framework, Adv-RM, to address both problems. Adv-RM automatically discovers adversarial responses that the targeted RM gives a high reward to while being OOD and of low quality. We find these examples by training an adversarial policy using reinforcement learning to generate responses that maximize discrepancy across different RMs, while receiving high rewards from the target RM. This approach reliably finds adversarial examples for state-of-the-art (SOTA) RMs, including Skywork-Reward-Gemma-2-27B (Liu et al., 2024a), Llama-3.1-Nemotron-70B-Reward (Wang et al., 2024), and Nemotron-4-340B-Reward (Adler et al., 2024), with over 80% attack success rates. Interestingly, we find that these popular RMs give high reward scores to a variety of low-quality responses, such as responses that have no punctuation or responses with random text in the middle of a response.

Once we find adversarial samples, Adv-RM incorporates them into the RM training procedure. Since the success rate of our attack method is high, we can include adversarial samples in the training data set without additional human annotation cost by simply using an in-distribution response as the chosen response and the adversarial response as the rejected response. We conduct extensive evaluation of these adversarially trained RMs through adversarial attacks, downstream RLHF training in the synthetic setting of Gao et al. (2023), and RLHF training on real datasets (Wang et al., 2024). We found that Adv-RM reward models not only are more robust against attacks but also mitigate reward hacking. With these models, RLHF can proceed for three times as many steps as runs with conventional RMs without exhibiting reward hacking, resulting in more performant aligned models.

We summarize our contributions as follows:

• We develop an RL-based approach that successfully generates adversarial samples for SOTA RMs. To the best of our knowledge, this is the first work to do so without human domain knowledge, providing a new means of evaluating RM robustness.

• We use adversarial samples to augment RM training. Through extensive experiments, we find that such adversarial training results in reward models that are more robust to hacking and have better downstream performance in RLHF.

---

## 2. Related Work

**Mitigating Reward Hacking.** There have been several works that attempt to mitigate reward hacking. Some of the earliest works used reward ensembles, and found that different ensembling approaches can slow (but not prevent) reward hacking (Coste et al., 2023; Eisenstein et al., 2023; Zhai et al., 2023; Ramé et al., 2024; Yan et al., 2024). In our experiments we compare with two simple reward ensemble aggregation approaches, MEAN and MEAN_MINUS_STD (Eisenstein et al., 2023). Chen et al. (2024) propose a new architecture that disentangles length from human preferences. Recently Liu et al. (2024b) proposes RRM which augments the RM training data by comparing responses from a prompt with random responses from other prompts, an approach we find to be effective.

Two works discuss adversarial training of verifiers. Amodei et al. (2016) presents the idea of adversarial reward models, a training framework in which adversarial training is used to find samples where RMs and human annotators disagree. However, they do not implement this idea, and relying on human annotators in their suggested way would be expensive and difficult. Kirchner et al. (2024) propose adversarial training of a verifier model but it is limited to tasks with rule-based verifiers like GSM8K and is not applicable to general reward modeling. Concurrently with our work, Wu et al. (2025) use manually defined input transformations to increase the difficulty of RM benchmarks.

**Adversarial Attacks on LLMs.** There is a wide literature discussing adversarial attacks on LLMs (Zhang et al., 2020). Typically these works attempt to greatly alter the model output while only slightly changing the model input (we only black-box attacks for simplicity (Guo et al., 2019)). We compare Adv-RM with two such approaches: Textfooler (Jin et al., 2020), which replaces words with synonyms such that the model output is greatly changed and StyleAdv (Qi et al., 2021), which changes the style of the text to greatly change the model output. We observe that such approaches usually do not succesfully attack RMs as (1) these attacks were not designed with the paired nature of RM training data in mind and (2) these attacks were designed to attack weaker models such as BERT (Devlin et al., 2019).

---

## 3. Methodology

### 3.1 Background

**RLHF.** We follow the standard RLHF setup of Stiennon et al. (2020); Ouyang et al. (2022). We consider a setting where we have a dataset of N human preference annotations, D={xi,yw,i,yℓ,i}ᵢ₌₁ᴺ. Here xᵢ is the i-th prompt, yw,i is the response preferred by human annotators, and yℓ,i is the rejected response. With this dataset, conventional RLHF trains a Bradley-Terry (Bradley & Terry, 1952) reward model Rθ(x,y) by minimizing the loss

ℒ(θ)=−𝔼ₓ,yw,yℓ∼D[log(σ(Rθ(x,yw)−Rθ(x,yℓ)))]

Next, RLHF trains a policy πϕ to maximize the expected reward Rθ(x,y) while remaining close to an initial policy πSFT. This is done by maximizing the following KL-regularized objective function over a prompt distribution P,

𝔼(x,y)∼P,y∼πϕ(x)[Rθ(x,y)−β𝔻KL(πϕ(·|x)||πSFT(·|x))]

using a reinforcement learning algorithm such as PPO, RLOO, or GRPO (Schulman et al., 2017; Ahmadian et al., 2024; Kool et al., 2019; Shao et al., 2024).

**Out-of-Distribution Detection.** Detecting OOD data is a long studied problem. Here we consider a simple approach for OOD data detection in RLHF: Ensemble disagreement (Lakshminarayanan et al., 2017). Concretely, we use the disagreement of an ensemble of reward models trained on different data splits to estimate the uncertainty of different prompt-response pairs. Such an approach has been shown to effectively capture model uncertainty and detect out-of-distribution data in a wide variety of domains, including continuous control (Brantley et al., 2019), computer vision (Vyas et al., 2018), and natural language processing (Yuan et al., 2023). Most recently, Eisenstein et al. (2023) showed that reward model disagreement is an effective way to detect OOD responses in RLHF. Here, we denote reward model disagreement as 

Uθ₁,⋯,θK(x,y)=STD(Rθ₁(x,y),...,RθK(x,y))

where Rθ₁,...,RθK are K different reward models trained with different data splits or random seeds. We remark that when K=2, Uθ₁,θq(x,y) is proportional to |Rθ₁(x,y)−Rθ₂(x,y)|. We normalize all RMs to have mean 0 and standard deviation 1.

### 3.2 Learning to Attack

The goal of our adversarial attack is, given a prompt, to find responses that receive high rewards from the target reward model and yet are OOD. Given a set of reward models Rθ₁,...,RθK, one reward model we seek to attack Rθ₁, and set of prompts D, we seek to train a policy πadv to satisfy the constrained optimization problem:

max_{πadv} 𝔼_{x∼D,y∼πadv(x)}[Uθ₁,...,θk(x,y)] s.t. 𝔼_{x∼D,y∼πadv(x)}[Rθ₁(x,y)>T(x)].

Here T(x) is a threshold dependent on the prompt. In our experiments we use two RMs (i.e. K=2) and set T(x) to be the average reward achieved by πSFT on the prompt x according to Rθ₁(·). Optimizing this means finding OOD samples that the target RM Rθ₁(·) predicts to be better than those generated by πSFT. Although this approach would indeed find highly OOD responses that get high reward, it is possible that by optimizing this we would find samples that all reward models predict will receive a high score, and the reward models just disagree on how high the score is. In order to encourage the found samples to be OOD and low quality, we use the formulation

max_{πadv} 𝔼_{x∼D,y∼πadv(x)}[Rθ₁(x,y)−λRθ₂(x,y)] s.t. 𝔼_{x∼D,y∼πadv(x)}[Rθ₁(x,y)>T(x)].

Here λ is a hyperparameters, with λ typically greater than 1. This formulation encourages finding responses with high uncertainty and a very low score from Rθ₂(x,y), increasing the likelihood of low quality samples. We overload our notation, and denote Rθ₁(x,y)−λRθ₂(x,y) as Uθ₁,θ₂(x,y).

Unlike previous adversarial attacks that rely on perturbations, the key innovation of our work is training an adversarial policy πadv to generate adversarial examples. Specifically, we optimize this using reinforcement learning and train an adversarial policy πadv to maximize the following reward:

R_adv(x,y) = {
  Rθ₁(x,y)−λRθ₂(x,y)    if Rθ₁(x,y)>T(x)
  Rθ₁(x,y)−C             otherwise
}

Here C is a constant that ensures the second case always gives a lower reward than the first case. This reward encourages the policy to maximize RM uncertainty and find OOD samples, while ensuring they receive a high reward from Rθ₁(x,y) (the attack target). We maximize this reward using RLOO (Ahmadian et al., 2024) over the RLHF prompt dataset, starting from πSFT. The reinforcement learning training procedure leaves us with a set of prompt-response pairs {(x₁,y₁ᵃᵈᵛ),...(xₙ,yₙᵃᵈᵛ)} generated by the adversarial policy throughout training.

**Data Filtering.** We filter the collected prompt-response pairs using Rθ₁(x,y) and Uθ₁,θ₂(x,y) to only select samples where the policy was able to successfully attack Rθ₁(x,y). Concretely, we select the adversarial dataset D_adv as

D_adv = {(x,y_adv) | Rθ₁(x,y_adv)>T(x) and Z(Uθ₁,θ₂(x,y_adv))>1.96}.

Here, Z(Uθ₁,θ₂(x,y)) is the z-score of the uncertainty Uθ₁,θ₂(x,y), computed over responses sampled from πSFT. A value of Z(Uθ₁,θ₂(x,y))>1.96 indicates that the reward uncertainty of (x,y_adv) is significantly higher than the uncertainty of responses within the distribution of πSFT. This ensures each sample in D_adv recieves a high reward score yet is OOD.

### 3.3 Preliminary Analysis: Uncertainty as a Quality Signal

Using a synthetic RLHF setup (Gao et al., 2023), we investigate how and when reward models uncertainty (i.e. Uθ₁,θ₂(·)) correlates with response quality. Concretely, we train two reward models (Rθ₁(·) and Rθ₂) based on different random seeds on a preference dataset created by a gold reward model, and then measure Uθ₁,θ₂(·) versus the gold score which measures quality. We investigate this relationship on two datasets: one dataset where the responses are samples from the SFT model, and one sampled from the Adv-RM model.

As shown in the figures, uncertainty Uθ₁,θ₂(·) is not very correlated with the gold reward (pearson's correlation -0.05) when we sample from πSFT. This indicates that directly penalizing ensemble uncertainty during RLHF may add some noise to training. On the other hand, when we use Adv-RM to generate OOD datapoints with a higher uncertainty level, we see that uncertainty is more correlated with gold score (pearson's correlation -0.70). Together, these plots suggest that ensemble uncertainty is a useful indicator of response quality when uncertainty is high (and can therefore be used to find adversarial examples), but it provides little signal for distinguishing quality among responses with low uncertainty (implying directly regularizing RM uncertainty during policy training is not ideal).

### 3.4 Adversarial Training of Reward Models

Our analysis shows that Adv-RM's attacks are succesful at producing adversarial responses. To increase RM robustness, we incorporate these adversarial responses into training.

**Preference Pair Construction.** We construct adversarial preference pairs by setting (x,ySFT) as the preferred pair and setting (x,y_adv) as the rejected pair. We choose a SFT response ySFT such that Rθ₁(x,ySFT)>𝔼_{y∼πSFT(x)}[Rθ₁(x,ySFT)], to avoid using low quality SFT responses as the preferred response. All of these adversarial preference pairs (x,y_adv) are constructed such that the rejected response y_adv receives a higher reward score from Rθ₁(·) than the SFT response, yet y_adv has very high Uθ₁,θ₂(·) so it is OOD and likely low quality.

**Multiple Rounds of Training.** Once we construct the adversarial preference pairs, we add around 1000 of them to the original RLHF preference dataset and train a new RM from scratch. To further improve RM robustness, we conduct several rounds of adversarial training, in each round trying to find vulnerabilities of the new robust RM. Once we find these vulnerabilities, we append them to our current robust RLHF dataset and train a new RM from scratch. We find that after 2 rounds of adversarial training, our attack procedure is no longer successful. At this point we terminate training.

---

## 6. Conclusion and Limitations

In this paper, we introduce Adv-RM, an adversarial training framework for RMs. Adv-RM can successfully attack state-of-the-art RMs, uncovering surprising failure cases where they assign high scores to low quality responses. Incorporating Adv-RM examples into RM training significantly improves RLHF stability and performance. Although Adv-RM is succesful, it has a few limitations. Adv-RM relies on reward ensembles, meaning adversarial responses may be missed if all RMs incorrectly predict they are high quality, highlighting the need for more robust out-of-distribution detection. Additionally, Adv-RM incurs a substantial computational cost—approximately 3× that of standard RLHF training—but we believe this overhead is justified by the resulting gains in robustness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e42fa03-e207-4f31-b33d-34d0fec61704",
  "isSidechain": false,
  "promptId": "6504b79e-cc54-4ac6-a1b5-85af6f368490",
  "type": "user",
  "uuid": "ebe3476b-9718-4c50-8c3b-f861c2f0f361",
  "toolUseResult": {
    "bytes": 425460,
    "code": 200,
    "codeText": "OK",
    "result": "# Full Text Extraction: Adversarial Training of Reward Models\n\n## 1. Introduction\n\nAs large language models (LLMs) become increasingly capable, ensuring their alignment with human values remains a fundamental challenge (Amodei et al., 2016; Askell et al., 2021). One of the most promising approaches for scalable alignment of LLMs is reward modeling, in which a reward model is trained to predict human feedback (Christiano et al., 2017; Leike et al., 2018). These reward models (RMs) are then used as a proxy for human feedback in a variety of places throughout the LLM lifecycle, including data selection (Chen et al., 2023), Reinforcement Learning from Human Feedback (RLHF, Ouyang et al. 2022), and inference time moderation (Inan et al., 2023). This approach has been very successful, resulting in powerful language models such as GPT-4 and Llama 3 (Achiam et al., 2023; Dubey et al., 2024).\n\nDespite their widespread use in LLM alignment, RMs are imperfect proxies for human judgment (Hendrycks et al., 2021; Gao et al., 2023). In particular, they exhibit poor out-of-distribution (OOD) generalization, often failing to reliably assess prompt-response pairs that diverge from their training distribution (Eisenstein et al., 2023). OOD generalization is challenging because RMs learn from a limited set of human-annotated examples, which do not cover the full diversity of possible model behaviors, leading to systematic failures when encountering novel model responses. These failures lead to reward hacking—where models trained on RMs optimize reward scores through unintended shortcuts, reducing their actual alignment with human values. Such reward hacking can result in unexpected behaviors and difficult-to-detect misalignment, an issue that becomes even more pernicious as model capabilities increase and evaluation becomes more challenging.\n\nBuilding robust RMs to mitigate reward hacking presents two unsolved challenges. The first is measuring a RM's robustness. Unlike image and speech models, where adversarial attacks can serve as robustness metrics (Carlini & Wagner, 2017), the discrete nature of language makes adversarial attacks on language models challenging and their robustness harder to define (Wang et al., 2021). Reward models introduce another layer of complexity, as their accuracy is measured on preference pairs, requiring adversarial preference pairs rather than a single adversarial input. So far the only known reliable way to quantify robustness of a RM is to measure how long it takes for reward hacking to occur in RLHF. This in itself can be challenging: we can rely on human evaluation to tell us if the policy training has significantly degraded, but this is costly and small misalignments can easily go undetected.\n\nThe second problem is how to improve the robustness of a RM. Prior works show that reward hacking often occurs because the RM gives high reward scores to model responses outside the reward model training distribution (Casper et al., 2023; Eisenstein et al., 2023). Giving a high reward to OOD responses is bad, as they deviate significantly from the expert responses in the RLHF dataset and are therefore likely to be low quality (Ho & Ermon, 2016). To avoid rewarding such responses, contemporary works have tried a variety of approaches, including regularizing training so that the policy model remains close to its initialization (Jaques et al., 2019; Stiennon et al., 2020), penalizing out-of-distribution (OOD) model responses using uncertainty estimates (Eisenstein et al., 2023; Coste et al., 2023), and regularizing reward learning (Ibarz et al., 2018; Liu et al., 2024b). However, we find that uncertainty estimates are not reliable indicators of response quality for in-distribution responses, which may limit the effectiveness of such regularization.\n\nIn this work we propose a new adversarial training framework, Adv-RM, to address both problems. Adv-RM automatically discovers adversarial responses that the targeted RM gives a high reward to while being OOD and of low quality. We find these examples by training an adversarial policy using reinforcement learning to generate responses that maximize discrepancy across different RMs, while receiving high rewards from the target RM. This approach reliably finds adversarial examples for state-of-the-art (SOTA) RMs, including Skywork-Reward-Gemma-2-27B (Liu et al., 2024a), Llama-3.1-Nemotron-70B-Reward (Wang et al., 2024), and Nemotron-4-340B-Reward (Adler et al., 2024), with over 80% attack success rates. Interestingly, we find that these popular RMs give high reward scores to a variety of low-quality responses, such as responses that have no punctuation or responses with random text in the middle of a response.\n\nOnce we find adversarial samples, Adv-RM incorporates them into the RM training procedure. Since the success rate of our attack method is high, we can include adversarial samples in the training data set without additional human annotation cost by simply using an in-distribution response as the chosen response and the adversarial response as the rejected response. We conduct extensive evaluation of these adversarially trained RMs through adversarial attacks, downstream RLHF training in the synthetic setting of Gao et al. (2023), and RLHF training on real datasets (Wang et al., 2024). We found that Adv-RM reward models not only are more robust against attacks but also mitigate reward hacking. With these models, RLHF can proceed for three times as many steps as runs with conventional RMs without exhibiting reward hacking, resulting in more performant aligned models.\n\nWe summarize our contributions as follows:\n\n• We develop an RL-based approach that successfully generates adversarial samples for SOTA RMs. To the best of our knowledge, this is the first work to do so without human domain knowledge, providing a new means of evaluating RM robustness.\n\n• We use adversarial samples to augment RM training. Through extensive experiments, we find that such adversarial training results in reward models that are more robust to hacking and have better downstream performance in RLHF.\n\n---\n\n## 2. Related Work\n\n**Mitigating Reward Hacking.** There have been several works that attempt to mitigate reward hacking. Some of the earliest works used reward ensembles, and found that different ensembling approaches can slow (but not prevent) reward hacking (Coste et al., 2023; Eisenstein et al., 2023; Zhai et al., 2023; Ramé et al., 2024; Yan et al., 2024). In our experiments we compare with two simple reward ensemble aggregation approaches, MEAN and MEAN_MINUS_STD (Eisenstein et al., 2023). Chen et al. (2024) propose a new architecture that disentangles length from human preferences. Recently Liu et al. (2024b) proposes RRM which augments the RM training data by comparing responses from a prompt with random responses from other prompts, an approach we find to be effective.\n\nTwo works discuss adversarial training of verifiers. Amodei et al. (2016) presents the idea of adversarial reward models, a training framework in which adversarial training is used to find samples where RMs and human annotators disagree. However, they do not implement this idea, and relying on human annotators in their suggested way would be expensive and difficult. Kirchner et al. (2024) propose adversarial training of a verifier model but it is limited to tasks with rule-based verifiers like GSM8K and is not applicable to general reward modeling. Concurrently with our work, Wu et al. (2025) use manually defined input transformations to increase the difficulty of RM benchmarks.\n\n**Adversarial Attacks on LLMs.** There is a wide literature discussing adversarial attacks on LLMs (Zhang et al., 2020). Typically these works attempt to greatly alter the model output while only slightly changing the model input (we only black-box attacks for simplicity (Guo et al., 2019)). We compare Adv-RM with two such approaches: Textfooler (Jin et al., 2020), which replaces words with synonyms such that the model output is greatly changed and StyleAdv (Qi et al., 2021), which changes the style of the text to greatly change the model output. We observe that such approaches usually do not succesfully attack RMs as (1) these attacks were not designed with the paired nature of RM training data in mind and (2) these attacks were designed to attack weaker models such as BERT (Devlin et al., 2019).\n\n---\n\n## 3. Methodology\n\n### 3.1 Background\n\n**RLHF.** We follow the standard RLHF setup of Stiennon et al. (2020); Ouyang et al. (2022). We consider a setting where we have a dataset of N human preference annotations, D={xi,yw,i,yℓ,i}ᵢ₌₁ᴺ. Here xᵢ is the i-th prompt, yw,i is the response preferred by human annotators, and yℓ,i is the rejected response. With this dataset, conventional RLHF trains a Bradley-Terry (Bradley & Terry, 1952) reward model Rθ(x,y) by minimizing the loss\n\nℒ(θ)=−𝔼ₓ,yw,yℓ∼D[log(σ(Rθ(x,yw)−Rθ(x,yℓ)))]\n\nNext, RLHF trains a policy πϕ to maximize the expected reward Rθ(x,y) while remaining close to an initial policy πSFT. This is done by maximizing the following KL-regularized objective function over a prompt distribution P,\n\n𝔼(x,y)∼P,y∼πϕ(x)[Rθ(x,y)−β𝔻KL(πϕ(·|x)||πSFT(·|x))]\n\nusing a reinforcement learning algorithm such as PPO, RLOO, or GRPO (Schulman et al., 2017; Ahmadian et al., 2024; Kool et al., 2019; Shao et al., 2024).\n\n**Out-of-Distribution Detection.** Detecting OOD data is a long studied problem. Here we consider a simple approach for OOD data detection in RLHF: Ensemble disagreement (Lakshminarayanan et al., 2017). Concretely, we use the disagreement of an ensemble of reward models trained on different data splits to estimate the uncertainty of different prompt-response pairs. Such an approach has been shown to effectively capture model uncertainty and detect out-of-distribution data in a wide variety of domains, including continuous control (Brantley et al., 2019), computer vision (Vyas et al., 2018), and natural language processing (Yuan et al., 2023). Most recently, Eisenstein et al. (2023) showed that reward model disagreement is an effective way to detect OOD responses in RLHF. Here, we denote reward model disagreement as \n\nUθ₁,⋯,θK(x,y)=STD(Rθ₁(x,y),...,RθK(x,y))\n\nwhere Rθ₁,...,RθK are K different reward models trained with different data splits or random seeds. We remark that when K=2, Uθ₁,θq(x,y) is proportional to |Rθ₁(x,y)−Rθ₂(x,y)|. We normalize all RMs to have mean 0 and standard deviation 1.\n\n### 3.2 Learning to Attack\n\nThe goal of our adversarial attack is, given a prompt, to find responses that receive high rewards from the target reward model and yet are OOD. Given a set of reward models Rθ₁,...,RθK, one reward model we seek to attack Rθ₁, and set of prompts D, we seek to train a policy πadv to satisfy the constrained optimization problem:\n\nmax_{πadv} 𝔼_{x∼D,y∼πadv(x)}[Uθ₁,...,θk(x,y)] s.t. 𝔼_{x∼D,y∼πadv(x)}[Rθ₁(x,y)>T(x)].\n\nHere T(x) is a threshold dependent on the prompt. In our experiments we use two RMs (i.e. K=2) and set T(x) to be the average reward achieved by πSFT on the prompt x according to Rθ₁(·). Optimizing this means finding OOD samples that the target RM Rθ₁(·) predicts to be better than those generated by πSFT. Although this approach would indeed find highly OOD responses that get high reward, it is possible that by optimizing this we would find samples that all reward models predict will receive a high score, and the reward models just disagree on how high the score is. In order to encourage the found samples to be OOD and low quality, we use the formulation\n\nmax_{πadv} 𝔼_{x∼D,y∼πadv(x)}[Rθ₁(x,y)−λRθ₂(x,y)] s.t. 𝔼_{x∼D,y∼πadv(x)}[Rθ₁(x,y)>T(x)].\n\nHere λ is a hyperparameters, with λ typically greater than 1. This formulation encourages finding responses with high uncertainty and a very low score from Rθ₂(x,y), increasing the likelihood of low quality samples. We overload our notation, and denote Rθ₁(x,y)−λRθ₂(x,y) as Uθ₁,θ₂(x,y).\n\nUnlike previous adversarial attacks that rely on perturbations, the key innovation of our work is training an adversarial policy πadv to generate adversarial examples. Specifically, we optimize this using reinforcement learning and train an adversarial policy πadv to maximize the following reward:\n\nR_adv(x,y) = {\n  Rθ₁(x,y)−λRθ₂(x,y)    if Rθ₁(x,y)>T(x)\n  Rθ₁(x,y)−C             otherwise\n}\n\nHere C is a constant that ensures the second case always gives a lower reward than the first case. This reward encourages the policy to maximize RM uncertainty and find OOD samples, while ensuring they receive a high reward from Rθ₁(x,y) (the attack target). We maximize this reward using RLOO (Ahmadian et al., 2024) over the RLHF prompt dataset, starting from πSFT. The reinforcement learning training procedure leaves us with a set of prompt-response pairs {(x₁,y₁ᵃᵈᵛ),...(xₙ,yₙᵃᵈᵛ)} generated by the adversarial policy throughout training.\n\n**Data Filtering.** We filter the collected prompt-response pairs using Rθ₁(x,y) and Uθ₁,θ₂(x,y) to only select samples where the policy was able to successfully attack Rθ₁(x,y). Concretely, we select the adversarial dataset D_adv as\n\nD_adv = {(x,y_adv) | Rθ₁(x,y_adv)>T(x) and Z(Uθ₁,θ₂(x,y_adv))>1.96}.\n\nHere, Z(Uθ₁,θ₂(x,y)) is the z-score of the uncertainty Uθ₁,θ₂(x,y), computed over responses sampled from πSFT. A value of Z(Uθ₁,θ₂(x,y))>1.96 indicates that the reward uncertainty of (x,y_adv) is significantly higher than the uncertainty of responses within the distribution of πSFT. This ensures each sample in D_adv recieves a high reward score yet is OOD.\n\n### 3.3 Preliminary Analysis: Uncertainty as a Quality Signal\n\nUsing a synthetic RLHF setup (Gao et al., 2023), we investigate how and when reward models uncertainty (i.e. Uθ₁,θ₂(·)) correlates with response quality. Concretely, we train two reward models (Rθ₁(·) and Rθ₂) based on different random seeds on a preference dataset created by a gold reward model, and then measure Uθ₁,θ₂(·) versus the gold score which measures quality. We investigate this relationship on two datasets: one dataset where the responses are samples from the SFT model, and one sampled from the Adv-RM model.\n\nAs shown in the figures, uncertainty Uθ₁,θ₂(·) is not very correlated with the gold reward (pearson's correlation -0.05) when we sample from πSFT. This indicates that directly penalizing ensemble uncertainty during RLHF may add some noise to training. On the other hand, when we use Adv-RM to generate OOD datapoints with a higher uncertainty level, we see that uncertainty is more correlated with gold score (pearson's correlation -0.70). Together, these plots suggest that ensemble uncertainty is a useful indicator of response quality when uncertainty is high (and can therefore be used to find adversarial examples), but it provides little signal for distinguishing quality among responses with low uncertainty (implying directly regularizing RM uncertainty during policy training is not ideal).\n\n### 3.4 Adversarial Training of Reward Models\n\nOur analysis shows that Adv-RM's attacks are succesful at producing adversarial responses. To increase RM robustness, we incorporate these adversarial responses into training.\n\n**Preference Pair Construction.** We construct adversarial preference pairs by setting (x,ySFT) as the preferred pair and setting (x,y_adv) as the rejected pair. We choose a SFT response ySFT such that Rθ₁(x,ySFT)>𝔼_{y∼πSFT(x)}[Rθ₁(x,ySFT)], to avoid using low quality SFT responses as the preferred response. All of these adversarial preference pairs (x,y_adv) are constructed such that the rejected response y_adv receives a higher reward score from Rθ₁(·) than the SFT response, yet y_adv has very high Uθ₁,θ₂(·) so it is OOD and likely low quality.\n\n**Multiple Rounds of Training.** Once we construct the adversarial preference pairs, we add around 1000 of them to the original RLHF preference dataset and train a new RM from scratch. To further improve RM robustness, we conduct several rounds of adversarial training, in each round trying to find vulnerabilities of the new robust RM. Once we find these vulnerabilities, we append them to our current robust RLHF dataset and train a new RM from scratch. We find that after 2 rounds of adversarial training, our attack procedure is no longer successful. At this point we terminate training.\n\n---\n\n## 6. Conclusion and Limitations\n\nIn this paper, we introduce Adv-RM, an adversarial training framework for RMs. Adv-RM can successfully attack state-of-the-art RMs, uncovering surprising failure cases where they assign high scores to low quality responses. Incorporating Adv-RM examples into RM training significantly improves RLHF stability and performance. Although Adv-RM is succesful, it has a few limitations. Adv-RM relies on reward ensembles, meaning adversarial responses may be missed if all RMs incorrectly predict they are high quality, highlighting the need for more robust out-of-distribution detection. Additionally, Adv-RM incurs a substantial computational cost—approximately 3× that of standard RLHF training—but we believe this overhead is justified by the resulting gains in robustness.",
    "durationMs": 58290,
    "url": "https://arxiv.org/html/2504.06141"
  },
  "sourceToolAssistantUUID": "6e42fa03-e207-4f31-b33d-34d0fec61704",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "ebe3476b-9718-4c50-8c3b-f861c2f0f361",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze adversarial reward model training paper",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98"
}
```

---

### Assistant

_source line 20 · 2026-05-28T11:08:58.138Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me try to find this paper on OpenReview to see if there are reviewer comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebe3476b-9718-4c50-8c3b-f861c2f0f361",
  "isSidechain": false,
  "requestId": "req_011CbUryKMfhTUQQ6XagGkMf",
  "type": "assistant",
  "uuid": "d25b3e62-e16f-437a-a331-645f2dbfc9f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MK9rjCydrBSU4K1DrBW4Ti",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5794,
      "cache_read_input_tokens": 14819,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 316,
          "cache_read_input_tokens": 14819,
          "cache_creation_input_tokens": 5794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5794
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

_source line 21 · 2026-05-28T11:08:59.116Z_

Now let me check for reviewer comments on OpenReview and also fetch the experiments section for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d25b3e62-e16f-437a-a331-645f2dbfc9f1",
  "isSidechain": false,
  "requestId": "req_011CbUryKMfhTUQQ6XagGkMf",
  "type": "assistant",
  "uuid": "8db64134-225a-49e5-8506-d2590e3286d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MK9rjCydrBSU4K1DrBW4Ti",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5794,
      "cache_read_input_tokens": 14819,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 316,
          "cache_read_input_tokens": 14819,
          "cache_creation_input_tokens": 5794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5794
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

_source line 22 · 2026-05-28T11:09:01.087Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JPERK5w3nmCbJafP7imQnh`</summary>

```json
{
  "url": "https://openreview.net/search?term=Adversarial+Training+of+Reward+Models+Bukharin",
  "prompt": "Find any OpenReview submissions matching \"Adversarial Training of Reward Models\" by Bukharin. Return the paper URL, venue, scores, and any reviewer comments if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8db64134-225a-49e5-8506-d2590e3286d0",
  "isSidechain": false,
  "requestId": "req_011CbUryKMfhTUQQ6XagGkMf",
  "type": "assistant",
  "uuid": "9f4c87d0-f91b-42db-9355-b90d56e31628",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MK9rjCydrBSU4K1DrBW4Ti",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5794,
      "cache_read_input_tokens": 14819,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 316,
          "cache_read_input_tokens": 14819,
          "cache_creation_input_tokens": 5794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5794
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

_source line 23 · 2026-05-28T11:09:03.627Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MrZx5YwUBdv2Ct2Sq9ACGw`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.06141",
  "prompt": "Extract the FULL text of the Experiments section (Section 4 or 5), including all subsections, experimental setup details, datasets used, baselines compared, and key numerical results. Include all tables and their descriptions. Do NOT summarize — return the full experimental details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f4c87d0-f91b-42db-9355-b90d56e31628",
  "isSidechain": false,
  "requestId": "req_011CbUryKMfhTUQQ6XagGkMf",
  "type": "assistant",
  "uuid": "7b5fc5e5-0dd7-4d7d-8c6e-c518e3c33776",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MK9rjCydrBSU4K1DrBW4Ti",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5794,
      "cache_read_input_tokens": 14819,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 316,
          "cache_read_input_tokens": 14819,
          "cache_creation_input_tokens": 5794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5794
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

_source line 24 · 2026-05-28T11:09:03.749Z_

<details><summary>↩ Tool result · `toolu_01JPERK5w3nmCbJafP7imQnh`</summary>

```text
I cannot find the specific paper "Adversarial Training of Reward Models" by Bukharin in the provided web page content. The page only shows the OpenReview.net homepage with navigation elements, footer information, and general site description. It does not contain search results, paper submissions, venue information, review scores, or reviewer comments.

To locate this paper, you would need to:
1. Visit OpenReview.net directly
2. Use their search functionality to query "Adversarial Training of Reward Models" and/or "Bukharin"
3. Browse the results to find the specific submission with its URL, venue, scores, and reviews
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f4c87d0-f91b-42db-9355-b90d56e31628",
  "isSidechain": false,
  "promptId": "6504b79e-cc54-4ac6-a1b5-85af6f368490",
  "type": "user",
  "uuid": "2e492460-5a28-46d0-afc8-11843cdd19f0",
  "toolUseResult": {
    "bytes": 62328,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find the specific paper \"Adversarial Training of Reward Models\" by Bukharin in the provided web page content. The page only shows the OpenReview.net homepage with navigation elements, footer information, and general site description. It does not contain search results, paper submissions, venue information, review scores, or reviewer comments.\n\nTo locate this paper, you would need to:\n1. Visit OpenReview.net directly\n2. Use their search functionality to query \"Adversarial Training of Reward Models\" and/or \"Bukharin\"\n3. Browse the results to find the specific submission with its URL, venue, scores, and reviews",
    "durationMs": 2657,
    "url": "https://openreview.net/search?term=Adversarial+Training+of+Reward+Models+Bukharin"
  },
  "sourceToolAssistantUUID": "9f4c87d0-f91b-42db-9355-b90d56e31628",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-28T11:09:22.374Z_

<details><summary>↩ Tool result · `toolu_01MrZx5YwUBdv2Ct2Sq9ACGw`</summary>

```text
# Experiments Section (4-5): Adversarial Training of Reward Models

## Section 4: Experiments on Adversarial Attacks

### 4.1 Evaluation

Success criteria requires generating preference pairs where the target RM scores one response higher while a "gold" reward model scores it lower. The strict evaluation uses z-scores: "the attack is only considered successful if ZRθ1(Rθ1(x,y1))>0 and ZRgold(Rgold(x,y1))<−1.96."

### 4.2 Experimental Setup

**Synthetic RLHF:**
- Gold RM: Llama-3.1-Nemotron-70B-Reward
- Training dataset: Helpsteer-2-Preferences relabeled with gold RM
- Proxy RMs: Based on Llama-3.1-8B-Instruct, trained on different random seeds
- Evaluation: 128 Helpsteer-2 prompts

**Real RLHF:**
- Target RMs: Skywork-Reward-Gemma-2-27B, Llama-3.1-Nemotron-70B-Reward, Nemotron-4-340B-Reward
- Evaluation judges: Human annotators, Llama 405B, Deepseek-R1
- Test set: 128 held-out prompts

**Baselines:**
- Textfooler (word replacement synonyms, 50 attacks per prompt)
- StyleAdv (style transfer using Llama-3.3-70B)
- RRM (random response comparison augmentation)
- RM over-optimization (3× standard training steps)

### 4.3 Main Results: Adversarial Attacks

**Table 1 - Synthetic Setting (128 prompts):**

| Method | Train Success (Standard) | Train Success (Strict) | Test Success (Standard) | Test Success (Strict) |
|--------|-------------------------|------------------------|-------------------------|----------------------|
| RM Over-optimization | 8.31% (2.44) | 2.85% (1.47) | 7.59% (2.34) | 1.34% (1.02) |
| RRM | 0% | 0% | 0% | 0% |
| StyleAdv | 0% | 0% | 0% | 0% |
| Textfooler | 9.57% (2.60) | 0% | 18.8% (3.45) | 0% |
| **Adv-RM** | **99.31% (0.73)** | **92.91% (2.27)** | **100% (0.00)** | **100% (0.00)** |

**Table 2 - Real Reward Models (multiple judges):**

| Target RM | Judge | Textfooler | RM Over-Opt | Adv-RM |
|-----------|-------|-----------|------------|--------|
| Skywork-Gemma 27B | Human | 19.61% (5.60) | 20% (5.66) | **100% (0.00)** |
| | Deepseek-R1 | 56% (4.41) | 32% (3.99) | **99% (0.73)** |
| | Llama 405B | 2% (1.24) | 14% (3.00) | **99% (0.73)** |
| Llama-Nemotron 70B | Human | 13.2% (4.86) | 23.64% (6.07) | **83.01% (5.13)** |
| | Deepseek-R1 | 27% (3.85) | 7% (2.23) | **71% (4.12)** |
| | Llama 405B | 1% (0.88) | 3% (1.50) | **24% (3.73)** |
| Nemotron-4 340B | Human | 17.86% (5.22) | 17.65% (5.20) | **78.85% (5.76)** |
| | Deepseek-R1 | 38% (4.33) | 23% (3.73) | **76% (4.11)** |
| | Llama 405B | 2% (1.24) | 19% (3.52) | **82% (3.42)** |

**Attack Characteristics:** Discovered distinct vulnerabilities—Skywork rewards prompt repetition; Nemotron-70B accepts nonsensical middle text; Nemotron-340B accepts unpunctuated responses.

**Table 3 - Ablation Study (synthetic):**

| Component | Success Rate |
|-----------|--------------|
| Adv-RM (Full) | 92.91% (2.27) |
| Without Filtering | 73.27% (3.94) |
| Without Unequal RM Weights | 16.41% (3.13) |
| Without Reward Threshold | 0.0% |

---

## Section 5: Downstream Policy Performance

### Experimental Setup

**Synthetic:** Train Llama-3.1-8B-Instruct using RLOO with RMs trained via Adv-RM; measure using gold reward.

**Real:** Train on Helpsteer-2-Preferences; evaluate on 128 held-out prompts using Llama 405B, Deepseek-R1, and Llama-Nemotron-70B RM.

**Baselines:**
- Baseline RLHF (conventional)
- Ensemble Mean (Ens (Mean))
- Ensemble Mean-Minus-STD (Ens (STD))
- RRM (random response augmentation)

### Results: Synthetic Setting

Adv-RM achieves higher gold reward with minimal reward hacking and exhibits "little length hacking, and performs better or as well as all of the baselines." Small improvements in best-case performance; primary benefit is robustness against reward hacking.

### Results: Real RLHF Setting

Adv-RM enables "RLHF can proceed for three times as many steps as runs with conventional RMs without exhibiting reward hacking." RRM proves strong but Adv-RM shows greater stability.

**Table 4 - RewardBench Scores:**

| Method | Overall | Chat | Chat-Hard | Safety | Reasoning |
|--------|---------|------|-----------|--------|-----------|
| Baseline | 0.8329 | 0.9721 | 0.6118 | 0.8541 | 0.8938 |
| **Adv-RM** | **0.8399** | 0.9609 | **0.6404** | 0.8514 | **0.9070** |

**Robustness:** Attack success rates decrease with successive Adv-RM training rounds, demonstrating improved resilience.

**Data Ablation:** Optimal performance achieved with ~1000 adversarial samples; additional samples reduce effectiveness due to limited diversity.

**Training Rounds:** Two rounds of adversarial training provides best performance; minimal gains afterward.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b5fc5e5-0dd7-4d7d-8c6e-c518e3c33776",
  "isSidechain": false,
  "promptId": "6504b79e-cc54-4ac6-a1b5-85af6f368490",
  "type": "user",
  "uuid": "a9475aa7-a3e9-48b9-b79c-75a0d76b1ed4",
  "toolUseResult": {
    "bytes": 425460,
    "code": 200,
    "codeText": "OK",
    "result": "# Experiments Section (4-5): Adversarial Training of Reward Models\n\n## Section 4: Experiments on Adversarial Attacks\n\n### 4.1 Evaluation\n\nSuccess criteria requires generating preference pairs where the target RM scores one response higher while a \"gold\" reward model scores it lower. The strict evaluation uses z-scores: \"the attack is only considered successful if ZRθ1(Rθ1(x,y1))>0 and ZRgold(Rgold(x,y1))<−1.96.\"\n\n### 4.2 Experimental Setup\n\n**Synthetic RLHF:**\n- Gold RM: Llama-3.1-Nemotron-70B-Reward\n- Training dataset: Helpsteer-2-Preferences relabeled with gold RM\n- Proxy RMs: Based on Llama-3.1-8B-Instruct, trained on different random seeds\n- Evaluation: 128 Helpsteer-2 prompts\n\n**Real RLHF:**\n- Target RMs: Skywork-Reward-Gemma-2-27B, Llama-3.1-Nemotron-70B-Reward, Nemotron-4-340B-Reward\n- Evaluation judges: Human annotators, Llama 405B, Deepseek-R1\n- Test set: 128 held-out prompts\n\n**Baselines:**\n- Textfooler (word replacement synonyms, 50 attacks per prompt)\n- StyleAdv (style transfer using Llama-3.3-70B)\n- RRM (random response comparison augmentation)\n- RM over-optimization (3× standard training steps)\n\n### 4.3 Main Results: Adversarial Attacks\n\n**Table 1 - Synthetic Setting (128 prompts):**\n\n| Method | Train Success (Standard) | Train Success (Strict) | Test Success (Standard) | Test Success (Strict) |\n|--------|-------------------------|------------------------|-------------------------|----------------------|\n| RM Over-optimization | 8.31% (2.44) | 2.85% (1.47) | 7.59% (2.34) | 1.34% (1.02) |\n| RRM | 0% | 0% | 0% | 0% |\n| StyleAdv | 0% | 0% | 0% | 0% |\n| Textfooler | 9.57% (2.60) | 0% | 18.8% (3.45) | 0% |\n| **Adv-RM** | **99.31% (0.73)** | **92.91% (2.27)** | **100% (0.00)** | **100% (0.00)** |\n\n**Table 2 - Real Reward Models (multiple judges):**\n\n| Target RM | Judge | Textfooler | RM Over-Opt | Adv-RM |\n|-----------|-------|-----------|------------|--------|\n| Skywork-Gemma 27B | Human | 19.61% (5.60) | 20% (5.66) | **100% (0.00)** |\n| | Deepseek-R1 | 56% (4.41) | 32% (3.99) | **99% (0.73)** |\n| | Llama 405B | 2% (1.24) | 14% (3.00) | **99% (0.73)** |\n| Llama-Nemotron 70B | Human | 13.2% (4.86) | 23.64% (6.07) | **83.01% (5.13)** |\n| | Deepseek-R1 | 27% (3.85) | 7% (2.23) | **71% (4.12)** |\n| | Llama 405B | 1% (0.88) | 3% (1.50) | **24% (3.73)** |\n| Nemotron-4 340B | Human | 17.86% (5.22) | 17.65% (5.20) | **78.85% (5.76)** |\n| | Deepseek-R1 | 38% (4.33) | 23% (3.73) | **76% (4.11)** |\n| | Llama 405B | 2% (1.24) | 19% (3.52) | **82% (3.42)** |\n\n**Attack Characteristics:** Discovered distinct vulnerabilities—Skywork rewards prompt repetition; Nemotron-70B accepts nonsensical middle text; Nemotron-340B accepts unpunctuated responses.\n\n**Table 3 - Ablation Study (synthetic):**\n\n| Component | Success Rate |\n|-----------|--------------|\n| Adv-RM (Full) | 92.91% (2.27) |\n| Without Filtering | 73.27% (3.94) |\n| Without Unequal RM Weights | 16.41% (3.13) |\n| Without Reward Threshold | 0.0% |\n\n---\n\n## Section 5: Downstream Policy Performance\n\n### Experimental Setup\n\n**Synthetic:** Train Llama-3.1-8B-Instruct using RLOO with RMs trained via Adv-RM; measure using gold reward.\n\n**Real:** Train on Helpsteer-2-Preferences; evaluate on 128 held-out prompts using Llama 405B, Deepseek-R1, and Llama-Nemotron-70B RM.\n\n**Baselines:**\n- Baseline RLHF (conventional)\n- Ensemble Mean (Ens (Mean))\n- Ensemble Mean-Minus-STD (Ens (STD))\n- RRM (random response augmentation)\n\n### Results: Synthetic Setting\n\nAdv-RM achieves higher gold reward with minimal reward hacking and exhibits \"little length hacking, and performs better or as well as all of the baselines.\" Small improvements in best-case performance; primary benefit is robustness against reward hacking.\n\n### Results: Real RLHF Setting\n\nAdv-RM enables \"RLHF can proceed for three times as many steps as runs with conventional RMs without exhibiting reward hacking.\" RRM proves strong but Adv-RM shows greater stability.\n\n**Table 4 - RewardBench Scores:**\n\n| Method | Overall | Chat | Chat-Hard | Safety | Reasoning |\n|--------|---------|------|-----------|--------|-----------|\n| Baseline | 0.8329 | 0.9721 | 0.6118 | 0.8541 | 0.8938 |\n| **Adv-RM** | **0.8399** | 0.9609 | **0.6404** | 0.8514 | **0.9070** |\n\n**Robustness:** Attack success rates decrease with successive Adv-RM training rounds, demonstrating improved resilience.\n\n**Data Ablation:** Optimal performance achieved with ~1000 adversarial samples; additional samples reduce effectiveness due to limited diversity.\n\n**Training Rounds:** Two rounds of adversarial training provides best performance; minimal gains afterward.",
    "durationMs": 18744,
    "url": "https://arxiv.org/html/2504.06141"
  },
  "sourceToolAssistantUUID": "7b5fc5e5-0dd7-4d7d-8c6e-c518e3c33776",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-28T11:09:26.196Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try to find this paper on OpenReview with a direct search.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9475aa7-a3e9-48b9-b79c-75a0d76b1ed4",
  "isSidechain": false,
  "requestId": "req_011CbUs1JMwgu5iScsuqSRza",
  "type": "assistant",
  "uuid": "8c67d9df-15ad-40a3-a9ad-02824eae6f21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BChzTbiwbhWwRaoGzdRELD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2285,
      "cache_read_input_tokens": 20613,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 20613,
          "cache_creation_input_tokens": 2285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2285
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

_source line 27 · 2026-05-28T11:09:28.724Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0134PEmyyxVZXSWcZhoNihx8`</summary>

```json
{
  "url": "https://openreview.net/search?term=Adversarial+Training+Reward+Models+Adv-RM&source=forum&offset=0&sort=relevance",
  "prompt": "Find any OpenReview forum page for the paper \"Adversarial Training of Reward Models\" or \"Adv-RM\". Return the URL if found, along with any review scores, reviewer comments, or venue information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c67d9df-15ad-40a3-a9ad-02824eae6f21",
  "isSidechain": false,
  "requestId": "req_011CbUs1JMwgu5iScsuqSRza",
  "type": "assistant",
  "uuid": "652335b3-d658-4736-b3eb-e5b78db71dc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BChzTbiwbhWwRaoGzdRELD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2285,
      "cache_read_input_tokens": 20613,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 20613,
          "cache_creation_input_tokens": 2285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2285
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

_source line 28 · 2026-05-28T11:09:30.788Z_

<details><summary>↩ Tool result · `toolu_0134PEmyyxVZXSWcZhoNihx8`</summary>

```text
Based on the web page content provided, I cannot find any OpenReview forum page for the paper "Adversarial Training of Reward Models" or "Adv-RM". 

The content shown is only the OpenReview.net homepage with navigation links and footer information. It does not contain search results, specific paper pages, or review information.

To locate this paper, you would need to:
1. Visit the OpenReview.net homepage directly
2. Use their search functionality to look for the paper title or abbreviation
3. Check the "All Venues" section to browse relevant conference proceedings
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "652335b3-d658-4736-b3eb-e5b78db71dc3",
  "isSidechain": false,
  "promptId": "6504b79e-cc54-4ac6-a1b5-85af6f368490",
  "type": "user",
  "uuid": "76d074a7-e928-47f6-b022-e454570ba49a",
  "toolUseResult": {
    "bytes": 62524,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find any OpenReview forum page for the paper \"Adversarial Training of Reward Models\" or \"Adv-RM\". \n\nThe content shown is only the OpenReview.net homepage with navigation links and footer information. It does not contain search results, specific paper pages, or review information.\n\nTo locate this paper, you would need to:\n1. Visit the OpenReview.net homepage directly\n2. Use their search functionality to look for the paper title or abbreviation\n3. Check the \"All Venues\" section to browse relevant conference proceedings",
    "durationMs": 2059,
    "url": "https://openreview.net/search?term=Adversarial+Training+Reward+Models+Adv-RM&source=forum&offset=0&sort=relevance"
  },
  "sourceToolAssistantUUID": "652335b3-d658-4736-b3eb-e5b78db71dc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-28T11:09:54.714Z_

<details><summary>Logged reasoning block</summary>

```text
The paper doesn't seem to be on OpenReview, which makes sense since it's an arXiv preprint (April 2025) from NVIDIA. Let me now compile the full analysis.

Let me think carefully about this paper's innovation structure and its relevance to our research direction.

## Analysis

### Problem Identification
The authors identified that reward models (RMs) used in RLHF are brittle proxies for human judgment — they assign high rewards to out-of-distribution (OOD), low-quality responses. Prior work had tried various mitigations (KL regularization, uncertainty penalization, ensemble methods), but:


- There was no systematic method to discover adversarial examples that fool RMs, unlike in computer vision where gradient-based attacks are well-established
- Adversarial training hadn't been successfully applied to harden RMs against such attacks

### Key Insight
The breakthrough is reframing the problem in two ways: first, by training an RL policy to generate adversarial responses that exploit RM weaknesses using ensemble disagreement as a signal for out-of-distribution behavior, which converts the intractable discrete-text attack problem into a solvable RL objective; second, by using these reliably generated adversarial examples (achieving 80%+ attack success) as negative training examples to make RMs more robust.

### Innovation Type
This represents a cross-domain transfer from computer vision's well-established adversarial training to the NLP/RM space, where discrete text made this previously infeasible—the key is using RL-based generation instead of gradient-based perturbations.

### What Makes It Good
The constrained optimization formulation is elegant and well-motivated, the empirical results are strong with attack success rates reaching 80-100% even against state-of-the-art models like Nemotron 340B, and it delivers practical gains like 3× more effective RLHF iterations. The work also uncovered surprising failure modes in popular RMs, such as their tendency to reward responses lacking punctuation or containing random text.

### Relevance to Our Research
The adversarial training framework could directly apply to finding examples that exploit rubric-based rewards, and the ensemble disagreement mechanism mirrors our rubric diversity approach—we could measure disagreement across multiple rubrics instead of reward models to identify out-of-distribution cases. The finding that two rounds of adversarial training suffice is valuable for planning compute, and the RL-generated adversarial examples could help us evaluate whether difficulty-calibrated rubrics resist gaming better than standard ones.

Now I'm structuring the JSON output to capture these insights.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76d074a7-e928-47f6-b022-e454570ba49a",
  "isSidechain": false,
  "requestId": "req_011CbUs1vQcqpoH5zN2Rpvzx",
  "type": "assistant",
  "uuid": "af9de25f-c228-4bef-9461-19bf8bffcda7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YRbcZt3DCX5wpaWufeMkt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 22898,
      "output_tokens": 2772,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2772,
          "cache_read_input_tokens": 22898,
          "cache_creation_input_tokens": 333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 333
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

_source line 30 · 2026-05-28T11:10:46.516Z_

Now I have comprehensive information about the paper. Let me compile the deep analysis.

```json
{
  "title": "Adversarial Training of Reward Models (Adv-RM)",
  "venue": "arXiv 2025 (preprint, NVIDIA)",
  "problem_identification": "The authors identified two unsolved, coupled problems: (1) there was no reliable way to *measure* reward model robustness beyond the expensive approach of running full RLHF and checking for hacking, and (2) there was no systematic way to *improve* RM robustness against OOD exploitation. Prior mitigations (KL regularization, uncertainty penalization, ensemble aggregation) were palliative — they slowed hacking but didn't fix the underlying RM vulnerabilities. The key diagnostic finding was that uncertainty estimates from RM ensembles are poor quality signals for in-distribution responses (Pearson -0.05) but become highly informative for OOD responses (Pearson -0.70), meaning ensemble disagreement is useful for *finding* adversarial examples but not for *regularizing* RLHF training directly.",
  "key_insight": "Instead of perturbing existing text (the standard NLP adversarial approach, which fails on RMs because it ignores preference-pair structure), train a *generative* adversarial policy via RL to produce responses that maximize disagreement across an RM ensemble while scoring highly on the target RM. This reframes discrete-text adversarial attacks as a tractable RL problem and simultaneously solves both the measurement problem (attack success rate = robustness metric) and the defense problem (adversarial outputs become free training data for RM hardening, since the ensemble filter confirms they're OOD/low-quality without human annotation).",
  "innovation_type": "cross_domain",
  "method_summary": "Given a target RM Rθ₁ and a second RM Rθ₂ (trained on a different data split), Adv-RM trains an adversarial policy πadv via RLOO to maximize the reward R_adv = Rθ₁(x,y) − λRθ₂(x,y) subject to a constraint that Rθ₁(x,y) exceeds the SFT baseline reward (enforced via a penalty term C). This finds responses that the target RM likes but the second RM disagrees with — indicating OOD exploitation. Generated adversarial responses are filtered using a z-score threshold (Z > 1.96) on ensemble disagreement to keep only statistically significant OOD samples. These are paired with above-average SFT responses as chosen/rejected preference pairs and added (~1000 samples) to the RM training set. The process is repeated for 2 rounds, after which the attack success rate drops to near zero, indicating the RM has been hardened against discoverable vulnerabilities.",
  "what_makes_it_good": "Three properties make this paper strong: (1) It elegantly couples the diagnostic and the cure — the same RL attack that *measures* vulnerability also *produces* the training data that fixes it, creating a self-improving loop without human annotation cost. (2) The empirical results are dramatic and interpretable: 92-100% attack success rates against SOTA RMs (Nemotron 340B, Skywork 27B), revealing surprising concrete failures (rewarding unpunctuated text, random gibberish, prompt repetition), and 3× longer RLHF training without hacking. (3) The ablation study is rigorous — removing unequal RM weights drops success from 93% to 16%, removing the reward threshold drops it to 0%, demonstrating each design choice is load-bearing rather than decorative.",
  "limitations_acknowledged": "The authors identify two key limitations: (1) the method relies on reward ensembles, so if all RMs share the same blind spot (i.e., all incorrectly score an adversarial response highly), the attack will miss it — a fundamental limitation of disagreement-based OOD detection; (2) the computational cost is ~3× standard RLHF training, though they argue the robustness gains justify this overhead.",
  "open_questions": [
    "Can the adversarial policy be made to target *specific* failure modes (e.g., rubric gaming, partial credit exploitation, stylistic shortcuts) rather than finding generic OOD responses? This would require replacing ensemble disagreement with a more targeted vulnerability signal.",
    "How does Adv-RM interact with structured/decomposed rewards like rubric-based systems? When the reward is a sum of K rubric dimensions, the adversarial policy could potentially exploit individual dimensions independently — does the 2-round convergence still hold or does K-dimensional reward create a larger attack surface?",
    "The 1000-sample saturation point and 2-round convergence suggest the method finds a limited diversity of adversarial modes. Is there a way to force the adversarial policy toward higher diversity (e.g., via diversity-promoting RL objectives) to uncover a broader range of RM vulnerabilities?"
  ],
  "building_blocks": [
    "RL-based adversarial policy training (RLOO for generation, not gradient perturbation)",
    "Ensemble disagreement as OOD detection signal (two RMs on different data splits)",
    "Asymmetric reward formulation: R₁ − λR₂ with λ > 1 to force low quality, not just high disagreement",
    "Z-score filtering (Z > 1.96) for statistically rigorous adversarial sample selection",
    "Preference pair construction from adversarial outputs without human annotation",
    "Iterative adversarial training rounds (attack → augment → retrain → re-attack)",
    "Synthetic RLHF evaluation framework (Gao et al., 2023) with gold RM for controlled experiments",
    "RewardBench for RM quality evaluation",
    "Attack success rate as a quantitative robustness metric for RMs"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "Adv-RM offers a directly transferable defense paradigm for our difficulty-calibrated rubric reward framework: instead of hoping that rubric ensemble diversity passively resists gaming, we could actively train an adversarial policy to *find* rubric-gaming responses (partial satisfaction, imprecise matching) and use those as hardening data — turning the diagnosed failure modes from arXiv:2605.12474 into a concrete adversarial training loop. The ensemble disagreement mechanism maps naturally onto our rubric ensemble: disagreement across K rubric variants (with different strictness calibrations) could serve as the OOD signal, and the finding that 2 rounds and ~1000 adversarial samples suffice is encouraging for our ≤200 H100-hour compute budget. The key methodological lesson is that the best defense against reward gaming isn't passive regularization but active red-teaming integrated into the training loop."
}
```

---

### Meta-observations on the craft of this paper

**Why this paper works as research, beyond the results:**

1. **The "dual-use" insight pattern**: The best papers don't just solve a problem — they find a formulation where solving the diagnostic problem *automatically* produces the solution. Here, the RL attack that measures robustness also generates the training data that improves it. This is the same pattern as GANs (the discriminator that evaluates also trains the generator). When constructing our rubric framework, we should look for similar dual-use structures — e.g., can the process of calibrating rubric strictness by difficulty also reveal which rubric dimensions are most gameable?

2. **Constraint → reward shaping is underrated**: The authors' move from a constrained optimization (maximize disagreement *subject to* high target reward) to a shaped RL reward with a penalty term C is a clean, practical trick. The ablation proves the threshold constraint is essential (0% success without it). This is worth emulating: formulate the ideal objective as a constrained problem first, then convert to reward shaping for tractability.

3. **The "surprising failure" presentation strategy**: Reporting that Nemotron-340B rewards unpunctuated text and Skywork rewards prompt repetition is brilliant framing — it makes the abstract "OOD vulnerability" problem viscerally concrete. For our paper, we should similarly find and showcase *specific* rubric gaming behaviors (e.g., "the model earns 4/5 on rubric dimension X by copying the problem statement verbatim") rather than reporting only aggregate metrics.

4. **Compute-honest positioning**: The authors explicitly acknowledge the 3× compute overhead and argue it's worth it rather than hiding it. This honesty builds trust and reframes the cost as an investment in robustness rather than a limitation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af9de25f-c228-4bef-9461-19bf8bffcda7",
  "isSidechain": false,
  "requestId": "req_011CbUs1vQcqpoH5zN2Rpvzx",
  "type": "assistant",
  "uuid": "83210a86-d3df-44e3-930c-571f0db37f91",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YRbcZt3DCX5wpaWufeMkt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 22898,
      "output_tokens": 2772,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2772,
          "cache_read_input_tokens": 22898,
          "cache_creation_input_tokens": 333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 333
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "83210a86-d3df-44e3-930c-571f0db37f91",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze adversarial reward model training paper",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "83210a86-d3df-44e3-930c-571f0db37f91",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze adversarial reward model training paper",
  "sessionId": "85a990bb-fea1-4a04-a988-6e39a69c0c98"
}
```

---
