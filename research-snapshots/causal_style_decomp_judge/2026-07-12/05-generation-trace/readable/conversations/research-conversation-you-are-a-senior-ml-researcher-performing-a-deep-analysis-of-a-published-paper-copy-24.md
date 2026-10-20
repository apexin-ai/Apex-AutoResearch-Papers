# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-28 (UTC).** ## Y

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/69ca0528-3b85-48fe-9142-f6b2db6d8f54.jsonl`
- **Structured JSON:** [`86719def07efdf712584.json`](../../sessions/86/86719def07efdf712584.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T10:41:31.262Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T10:41:31.262Z",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2027\nTrack: Machine Learning — Reinforcement Learning / AI Safety\n\nDirection: Develop an automated, difficulty-calibrated rubric reward framework for math RLVR training that combines problem-specific rubric generation, difficulty-aware rubric strictness calibration, and rubric ensemble diversity to resist gaming. The key insight is that rubric rewards are only as robust as their calibration — uniform rubrics across difficulty levels create exploitable gaps where models earn high rubric scores on hard problems via shallow pattern matching.\n\nSeed Papers:\n- Curing Miracle Steps with Rubric Rewards (arXiv:2510.07774, 2025) — establishes rubric rewards for math, 26.7%→62.6% verified pass@1024 on AIME, but rubrics are manual and uniform\n- ARES: Automated Rubric Synthesis (arXiv:2605.23454, 2026) — automates rubric generation at scale from documents, but not math-specific and no difficulty calibration\n- Harder Is Better / DGPO (arXiv:2601.20614, ICLR 2026) — difficulty-aware GRPO for math training, but applies only to outcome rewards, not rubric rewards\n- Reward Hacking in Rubric-Based RL (arXiv:2605.12474, 2026) — diagnoses rubric gaming mechanisms (partial satisfaction, implicit-as-explicit, imprecise matching) but proposes no solution\n- SRaR: Step-wise Rubric Rewards (arXiv:2605.17291, 2025) — step-level rubric attribution with decoupled advantage, but no automation or calibration\n- Reward Under Attack (arXiv:2603.06621, 2026) — quantifies >0.9 PRM reward with <4% accuracy, 43% from stylistic shortcuts\n\nKnown Gaps:\n- No framework combines automated math-specific rubric generation with difficulty-calibrated rubric strictness (ARES automates but doesn't calibrate; DGPO calibrates difficulty but not rubrics)\n- Rubric gaming has been diagnosed (arXiv:2605.12474) but no defense mechanism via rubric ensemble diversity has been proposed or evaluated\n- The interaction between difficulty calibration and rubric anti-gaming is unexplored: does calibrating strictness by difficulty reduce or amplify gaming opportunities?\n\nTheoretical Anchor: Goodhart's Law applied to rubric decomposition — when a reward is decomposed into K rubric dimensions, the optimization target shifts from gaming one scalar to gaming K sub-scores, but uniform weighting across difficulty levels creates systematic exploitation gradients where hard-problem rubrics are easier to partially satisfy than to genuinely earn.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated 60-90 H100-hours)\n\nQuality Self-Checks:\n- [x] Core insight: Rubric rewards without difficulty-aware calibration create exploitable strictness gaps on hard problems that models can game via partial satisfaction.\n- [ ] Why not obvious: The pieces exist (ARES, DGPO, RRM) — the risk is this reads as 'obvious combination.' Must demonstrate non-trivial interaction effects between difficulty calibration and rubric gaming.\n- [ ] Baseline fear test: Could simply applying ARES rubrics + DGPO weighting to RRM achieve 80% of the improvement? Likely yes — the marginal contribution of the anti-gaming ensemble and calibration interaction must be demonstrated.\n- [ ] Information exploited: Problem difficulty metadata (base model pass rate, competition level) to modulate per-dimension rubric strictness — something outcome-only methods ignore.\n\nAvoid:\n- Presenting as a simple combination of ARES + DGPO + RRM without a unifying theoretical contribution about calibration-gaming interaction\n- Overclaiming novelty on rubric automation (ARES already does this) or difficulty awareness (DGPO already does this) — the contribution must be the synthesis and the interaction analysis\n- Ignoring the baseline fear: must run ARES+DGPO+RRM ablation honestly and show the ensemble/calibration interaction provides meaningful lift**\n\n## Paper to analyze\n\n{\n  \"title\": \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\",\n  \"authors\": \"Rishabh Tiwari et al.\",\n  \"venue\": \"arXiv 2026\",\n  \"url\": \"https://arxiv.org/abs/2603.06621\",\n  \"why_important\": \"Quantifies catastrophic PRM failure (>0.9 reward with <4% accuracy, 43% from stylistic shortcuts); releases PRM-BiasBench diagnostic toolkit; motivates the need for rubric-based alternatives to PRMs\",\n  \"one_line_summary\": \"Demonstrates that current process reward models function as fluency detectors rather than reasoning verifiers, with gradient-based attacks easily inflating rewards on logically invalid trajectories.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T10:41:31.265Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T10:41:31.265Z",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-28T10:41:31.279Z_

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
  "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
  "authors": "Rishabh Tiwari et al.",
  "venue": "arXiv 2026",
  "url": "https://arxiv.org/abs/2603.06621",
  "why_important": "Quantifies catastrophic PRM failure (>0.9 reward with <4% accuracy, 43% from stylistic shortcuts); releases PRM-BiasBench diagnostic toolkit; motivates the need for rubric-based alternatives to PRMs",
  "one_line_summary": "Demonstrates that current process reward models function as fluency detectors rather than reasoning verifiers, with gradient-based attacks easily inflating rewards on logically invalid trajectories."
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
  "promptId": "55ac8fb9-1fd3-47f2-982c-1088d7bccd96",
  "type": "user",
  "uuid": "4470e5dd-92b6-4b34-9f5f-bf2f17c67430",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T10:41:31.279Z_

```json
{
  "parentUuid": "4470e5dd-92b6-4b34-9f5f-bf2f17c67430",
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
  "uuid": "d2f9e247-9e7e-4438-9976-c9537335dee1",
  "timestamp": "2026-05-28T10:41:31.279Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T10:41:31.279Z_

```json
{
  "parentUuid": "d2f9e247-9e7e-4438-9976-c9537335dee1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f9c36c5a-f04d-46d1-b75e-89fbc0f079b0",
  "timestamp": "2026-05-28T10:41:31.279Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
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
  "aiTitle": "Analyze PRM robustness and gaming mechanisms",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54"
}
```

---

### Assistant

_source line 7 · 2026-05-28T10:41:35.374Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze the paper "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" (arXiv:2603.06621). Let me fetch the paper from arXiv to read its contents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9c36c5a-f04d-46d1-b75e-89fbc0f079b0",
  "isSidechain": false,
  "requestId": "req_011CbUpt7ySGiBokZAxkE2Ef",
  "type": "assistant",
  "uuid": "a12691e6-a613-4945-96e9-d8568184fe71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxzA2hDrqpJPh8xgUrDd8z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 11014,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 148,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3142
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

_source line 8 · 2026-05-28T10:41:35.610Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KvtJkNyQyeQEB2TNxmUFHr`</summary>

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
  "parentUuid": "a12691e6-a613-4945-96e9-d8568184fe71",
  "isSidechain": false,
  "requestId": "req_011CbUpt7ySGiBokZAxkE2Ef",
  "type": "assistant",
  "uuid": "a8e1c79b-c34d-4435-9324-a0bb0ccf4340",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DxzA2hDrqpJPh8xgUrDd8z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 11014,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 148,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3142
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

_source line 9 · 2026-05-28T10:41:35.619Z_

<details><summary>↩ Tool result · `toolu_01KvtJkNyQyeQEB2TNxmUFHr`</summary>

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
  "parentUuid": "a8e1c79b-c34d-4435-9324-a0bb0ccf4340",
  "isSidechain": false,
  "promptId": "55ac8fb9-1fd3-47f2-982c-1088d7bccd96",
  "type": "user",
  "uuid": "e7c26f86-b19a-48cd-a080-6644c707d1e1",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "a8e1c79b-c34d-4435-9324-a0bb0ccf4340",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-28T10:41:38.982Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the full PDF (via HTML version) to get comprehensive information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7c26f86-b19a-48cd-a080-6644c707d1e1",
  "isSidechain": false,
  "requestId": "req_011CbUptSURS2rvEocb9e1jf",
  "type": "assistant",
  "uuid": "cf57b928-fb14-406b-8b14-8e3a91eaacea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZQ6Pt4XzSCsKLQZuap3Wp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 14156,
      "output_tokens": 354,
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
          "input_tokens": 3,
          "output_tokens": 354,
          "cache_read_input_tokens": 14156,
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

### Tool call

_source line 11 · 2026-05-28T10:41:39.918Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Gopgq9Ys12HjwRhgBmq1fs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.06621",
  "prompt": "Extract the full abstract, author list, submission date, and any other metadata available on this page for the paper \"Reward Under Attack\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf57b928-fb14-406b-8b14-8e3a91eaacea",
  "isSidechain": false,
  "requestId": "req_011CbUptSURS2rvEocb9e1jf",
  "type": "assistant",
  "uuid": "ca5e0fac-46fe-43c8-b0ec-8105ba93883d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZQ6Pt4XzSCsKLQZuap3Wp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 14156,
      "output_tokens": 354,
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
          "input_tokens": 3,
          "output_tokens": 354,
          "cache_read_input_tokens": 14156,
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

### Tool call

_source line 12 · 2026-05-28T10:41:43.293Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WEG7982xbrv424VnFKzB4X`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.06621",
  "prompt": "Extract the FULL text of the following sections in as much detail as possible: \n1. Introduction (complete text)\n2. Related Work (complete text)\n3. Method / Approach / Methodology section (complete text, including all subsections, equations, algorithms)\n4. Experiments and Results (complete text including all tables and figures descriptions)\n5. Conclusion / Discussion (complete text)\n6. Limitations (if present)\n\nBe as comprehensive as possible - include all technical details, equations, specific numbers, benchmark names, model names, and experimental configurations. Do NOT summarize - extract the actual text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca5e0fac-46fe-43c8-b0ec-8105ba93883d",
  "isSidechain": false,
  "requestId": "req_011CbUptSURS2rvEocb9e1jf",
  "type": "assistant",
  "uuid": "e1a1a65d-23c0-4a09-8e2d-033a08f35dc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZQ6Pt4XzSCsKLQZuap3Wp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 14156,
      "output_tokens": 354,
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
          "input_tokens": 3,
          "output_tokens": 354,
          "cache_read_input_tokens": 14156,
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

_source line 13 · 2026-05-28T10:41:44.972Z_

<details><summary>↩ Tool result · `toolu_01Gopgq9Ys12HjwRhgBmq1fs`</summary>

```text
# Paper Metadata: "Reward Under Attack"

**Title:** Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models

**Authors:** Rishabh Tiwari, Aditya Tomar, Udbhav Bamba, Monishwaran Maheswaran, Heng Yang, Michael W. Mahoney, Kurt Keutzer, Amir Gholami

**Submission Date:** February 20, 2026

**arXiv Identifier:** 2603.06621

**Category:** Computer Science > Machine Learning (cs.LG)

**DOI:** https://doi.org/10.48550/arXiv.2603.06621

**License:** CC BY 4.0

## Abstract Summary

The research examines vulnerabilities in Process Reward Models (PRMs) used in LLM reasoning systems. Key findings include:

- A diagnostic framework revealing that PRMs detect surface-level style variations minimally but inconsistently identify logically flawed reasoning
- Gradient-based attacks that artificially inflate rewards on invalid outputs
- Critical failure modes where policies achieve near-perfect PRM scores while maintaining below 4% actual accuracy
- Evidence that approximately 43% of reward improvements stem from stylistic patterns rather than genuine reasoning improvements

The authors released "PRM-BiasBench" alongside a diagnostic toolkit to assess robustness before deployment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca5e0fac-46fe-43c8-b0ec-8105ba93883d",
  "isSidechain": false,
  "promptId": "55ac8fb9-1fd3-47f2-982c-1088d7bccd96",
  "type": "user",
  "uuid": "3497cc2d-e936-4d68-a448-9d3ac0b2fe02",
  "toolUseResult": {
    "bytes": 48230,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Metadata: \"Reward Under Attack\"\n\n**Title:** Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\n\n**Authors:** Rishabh Tiwari, Aditya Tomar, Udbhav Bamba, Monishwaran Maheswaran, Heng Yang, Michael W. Mahoney, Kurt Keutzer, Amir Gholami\n\n**Submission Date:** February 20, 2026\n\n**arXiv Identifier:** 2603.06621\n\n**Category:** Computer Science > Machine Learning (cs.LG)\n\n**DOI:** https://doi.org/10.48550/arXiv.2603.06621\n\n**License:** CC BY 4.0\n\n## Abstract Summary\n\nThe research examines vulnerabilities in Process Reward Models (PRMs) used in LLM reasoning systems. Key findings include:\n\n- A diagnostic framework revealing that PRMs detect surface-level style variations minimally but inconsistently identify logically flawed reasoning\n- Gradient-based attacks that artificially inflate rewards on invalid outputs\n- Critical failure modes where policies achieve near-perfect PRM scores while maintaining below 4% actual accuracy\n- Evidence that approximately 43% of reward improvements stem from stylistic patterns rather than genuine reasoning improvements\n\nThe authors released \"PRM-BiasBench\" alongside a diagnostic toolkit to assess robustness before deployment.",
    "durationMs": 5050,
    "url": "https://arxiv.org/abs/2603.06621"
  },
  "sourceToolAssistantUUID": "ca5e0fac-46fe-43c8-b0ec-8105ba93883d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T10:42:49.388Z_

<details><summary>↩ Tool result · `toolu_01WEG7982xbrv424VnFKzB4X`</summary>

```text
# Extracted Content from "Reward Under Attack"

## 1. Introduction

Process Reward Models have emerged as critical components in LLM reasoning pipelines, providing step-level feedback for reward-guided decoding, test-time compute scaling, and fine-tuning of chain-of-thought models. Unlike outcome-based reward models that evaluate only final answers, PRMs assess intermediate reasoning steps, offering finer-grained control and improved credit assignment during both training and inference.

The paper identifies a fundamental gap: systematic methods for evaluating PRM robustness are lacking. A PRM conflating "fluent text" with "correct reasoning" will reward implausible-sounding but logically-flawed steps, potentially amplifying errors during RL training or misleading inference-time search.

The authors introduce a three-tiered diagnostic framework quantifying PRM hackability with increasing adversarial pressure:

**Tier 1 - Static Perturbation Analysis:** Measures PRM sensitivity to controlled input modifications, including semantics-preserving changes (rephrasing, verbosity) and semantics-altering corruptions (hallucinated steps, mismatched prompts).

**Tier 2 - Adversarial Tokens Optimization:** Searches for discrete token sequences maximally inflating rewards on invalid trajectories. The achievable reward score quantifies exploitability and characterizes reward landscape geometry.

**Tier 3 - RL-Induced Reward Hacking:** Trains policies using only PRM feedback, measuring divergence between reward and ground-truth accuracy. This closed-loop evaluation exposes vulnerabilities emerging only under optimization pressure.

Applied to state-of-the-art PRMs (Skywork-o1-Open-PRM-1.5B/7B and Qwen2.5-Math-PRM-7B), findings reveal consistent vulnerabilities: optimized 100-token adversarial sequences push rewards above 0.9 on logically flawed reasoning, and RL-trained policies achieve high rewards while accuracy stagnates, with approximately 43% of reward gain attributable to stylistic shortcuts rather than genuine reasoning improvements.

Key contributions include:
- Comprehensive sensitivity analysis uncovering "fluency-logic dissociation": PRMs exhibit high invariance to surface-level stylistic changes (reward changes <<0.1) yet show inconsistent detection of semantic corruption
- Gradient-based adversarial probing demonstrating short token sequences universally inflate rewards on invalid trajectories
- RL-induced reward hacking showing policies trained with PRM feedback exhibit reward-accuracy divergence
- Release of PRM-BiasBench benchmark extending ProcessBench with controlled perturbations across 8 transformation types

The paper suggests current PRMs function as "fluency detectors" rather than "reasoning verifiers," creating systematic blind spots exploitable under optimization pressure. Notably, studied PRMs exhibit complementary failure modes: Skywork incentivizes performative complexity (elaborate but flawed reasoning), while Qwen incentivizes vacuous safety (minimal text avoiding errors by avoiding substance).

## 2. Related Work

### 2.1 Reward Model Vulnerabilities

Reward models central to aligning language models exhibit systematic failure modes. Reward hacking occurs when policies exploit spurious correlations achieving high scores without satisfying intended objectives. Common manifestations include length bias where longer outputs receive inflated rewards regardless of quality, and sycophancy where models agree with users rather than providing accurate information. These vulnerabilities amplify under optimization pressure, degrading downstream performance. While extensive work characterizes outcome-level reward models, PRMs remain understudied despite increasing deployment in reasoning pipelines.

### 2.2 Process Reward Models

PRMs provide step-level supervision for chain-of-thought reasoning, enabling finer-grained credit assignment than outcome-based alternatives. Recent work focuses on training methodology: Wang et al. demonstrate that PRMs improve mathematical reasoning when combined with Monte Carlo Tree Search, while Zhang et al. analyze best practices for PRM dataset construction. Zheng et al. introduce ProcessBench, a benchmark with human-annotated error locations in reasoning traces. Most relevant is Xu et al., finding that PRMs often rely on shallow consistency cues rather than causal reasoning structures. However, existing analyses remain limited to observational studies; the paper complements this with controlled perturbations, adversarial optimization, and closed-loop RL evaluation systematically quantifying exploitability.

### 2.3 Adversarial Attacks on Neural Networks

Gradient-based optimization has proven effective exposing vulnerabilities across neural architectures. In NLP, Wallace et al. demonstrate that short, input-agnostic token sequences trigger targeted misbehavior, while Zou et al. show optimized adversarial tokens reliably jailbreak aligned LLMs with cross-model transferability. These methods treat models as differentiable objectives searching for inputs maximizing undesirable outputs. The paper adapts this paradigm to PRMs, demonstrating similar vulnerabilities exist: optimized token sequences universally inflate rewards on invalid reasoning, and resulting reward landscapes exhibit flat, exploitable plateaus.

### 2.4 Reward Overoptimization

When policies optimize learned reward proxies, performance on true objectives eventually degrades, formalized as Goodhart's Law. Gao et al. characterize scaling laws for overoptimization, finding larger reward models delay but do not prevent degradation. Coste et al. show overoptimization correlates with distributional shift from reward model training data. The paper's RL-induced reward hacking analysis extends this to PRMs, revealing policies trained with PRM feedback exhibit reward-accuracy divergence.

Prior PRM limitation work has been largely observational. The paper fills this gap by applying increasing adversarial pressure from model-agnostic perturbations through gradient-based optimization to closed-loop RL, revealing complementary vulnerabilities at each level.

## 3. Method / Approach / Methodology

### Preliminaries

#### Trajectory Level Reward Calculation

A PRM assigns scores to individual reasoning steps. Given a query q and trajectory τ=(s₁,…,sₙ), a PRM computes step-level rewards rᵢ=PRM(q,s≤ᵢ) conditioned on preceding context. Aggregate trajectory reward depends on training objective: Skywork-o1-Open-PRM estimates success probability at each step using R(τ)=rₙ; Qwen2.5-Math-PRM-7B locates the first error using R(τ)=minᵢrᵢ.

#### Robustness Criteria

Four complementary robustness dimensions are evaluated:

**Style Invariance:** Reward unchanged by semantics-preserving edits (rephrasing, verbosity changes). For perturbed trajectory τ̃, expect ΔR=R(τ̃)−R(τ)≈0.

**Logic Sensitivity:** Reward decreases substantially for semantics-altering corruptions (hallucinated steps, mismatched prompts). Expect ΔR≪0.

**Adversarial Resistance:** Optimized token sequences should not inflate rewards on invalid trajectories. Given adversarial tokens e, reward R(q,τ⊕e) should remain bounded.

**Optimization Alignment:** Policies trained to maximize PRM reward should improve ground-truth accuracy, not diverge from it.

A robust PRM should satisfy all four criteria. The three-tiered framework tests each: static perturbations probe criteria 1 and 2; adversarial optimization probes criterion 3; RL-induced reward hacking probes criterion 4.

#### Experimental Setup

Two models evaluated: Skywork-o1-Open-PRM (1.5B and 7B) and Qwen2.5-Math-PRM-7B, representing current frontier of open process reward models for mathematical reasoning. For static analysis, ProcessBench extended into PRM-BiasBench with controlled perturbations across 8 transformation types. For adversarial optimization and RL experiments, AIME 2024 problems used for training and AIME 2025 for transfer evaluation, with Qwen2.5-1.5B-Instruct as base policy.

### 4. Static Perturbation Analysis

#### 4.1 Perturbation Taxonomy

Perturbations organize into two categories based on logical validity impact. Semantics-preserving edits maintain reasoning correctness: "rephrasing" alters word choice and syntax; "verbosity changes" add or remove redundant language. A robust PRM should be invariant to surface-level modifications. Semantics-altering attacks introduce logical errors: "question shuffling" pairs trajectory with unrelated prompt; "reasoning hallucination" injects false assumptions. A robust PRM should strongly penalize corruptions. All perturbations generated via GPT-4o and validated for semantic equivalence.

#### 4.2 Results

**Style Invariance:** Both PRMs exhibit strong invariance to semantics-preserving edits. Rephrasing and verbosity changes yield tight distributions centered near zero (|ΔR|<0.1 for vast majority of samples). Both models show nearly identical behavior, with Qwen exhibiting slightly higher peaks, suggesting these PRMs have largely overcome length and style biases documented in outcome-based reward models.

**Asymmetric Logic Detection:** Semantics-altering attacks reveal divergent vulnerabilities. For question shuffling, two PRMs exhibit opposite behaviors: Skywork reliably penalizes mismatched question-trajectory pairs (peak at ΔR≈−0.8), while Qwen largely fails to detect mismatch, retaining high rewards near zero. For reasoning hallucination, Qwen shows striking bimodal behavior: sharp spike at ΔR=−1 indicates strong penalization for some hallucinated trajectories, yet substantial mass near zero reveals many corrupted samples still receive high rewards. Skywork exhibits broader distribution with weaker overall penalization.

#### 4.3 The Fluency-Logic Dissociation

Static analysis reveals two key findings:

**High style invariance:** Both PRMs reliably ignore surface-level variations, with distributions tightly centered near zero for all semantics-preserving edits.

**Inconsistent logic detection:** PRMs use different heuristics and fail on different attacks. Qwen fails to penalize question-trajectory mismatches but partially detects hallucinated reasoning; Skywork shows opposite pattern.

This fluency-logic dissociation indicates PRMs function primarily as detectors of "reasoning-style" fluency rather than verifiers of logical correctness. Model-specific failure modes suggest current PRMs learn superficial correlates of valid reasoning rather than genuine verification capabilities.

### 5. Adversarial Probing

#### 5.1 Optimization Framework

Adversarial tokens e∈ℝ^(k×d) are k vectors in model's d-dimensional embedding space that, when added to trajectory containing logically-flawed reasoning, adversarially increase reward. Given batch of flawed trajectories ℬ={(qᵢ,τᵢ)} sampled from AIME24, adversary optimizes:

max_e ℒ_adv(e) = (1/|ℬ|)∑_{(q,τ)∈ℬ} R(q,τ⊕e) − λ·Ω(e)

where ⊕ denotes concatenation, R is PRM score, and Ω(e) is optional regularization term. Two sets of experiments performed: one with no regularization (continuous embedding space), one with entropy regularization (forcing adversarial vectors to discrete tokens).

For experiments, training conducted on AIME24 trajectories with evaluation on held-out AIME25 trajectories. For Skywork PRM, adversarial tokens appended as suffix after solution; for Qwen, tokens inserted between question and solution (Qwen trained to detect first wrong step).

#### 5.2 Continuous Token Optimization

Testing minimal adversarial capacity required to inflate Skywork-1.5B PRM rewards by optimizing single continuous embedding vector (k=1) appended to each flawed trajectory in batch.

**Results:** Single optimized embedding vector sufficiently increases reward across batch substantially, demonstrating minimal adversarial capacity suffices to exploit PRM vulnerabilities.

#### 5.3 Discrete Token Optimization

Continuous embeddings do not appear in real-world settings. To ensure findings transfer to practical scenarios, discrete token sequences optimized via entropy regularization. Optimization conducted over probability simplex of vocabulary V for k∈{1,50,100} adversarial tokens. Regularization term encourages one-hot distributions:

Ω(e) = −∑ᵢ₌₁ᵏ ∑ᵥ∈V pᵢ,ᵥ log pᵢ,ᵥ

By annealing λ during optimization, each pᵢ gradually forced toward one-hot representation, aiming to yield interpretable discrete sequences.

**Results:** Table 2 summarizes attack success and transfer across all three PRMs.

Skywork-1.5B highly vulnerable. From baseline of 0.237, adversarial optimization reaches R=0.954 at 100 tokens (4× increase) and transfers strongly to AIME25, tripling reward from 0.305 to 0.924 (Δ=+0.619). Even 50 tokens produce substantial inflation (Δ=+0.224). Optimized sequences typically consist of mathematical connectors and formatting tokens ("Therefore," "Thus," and so on), suggesting PRM functions as fluency-weighted pattern matcher.

Skywork-7B exhibits partial robustness. From baseline of 0.287, 7B model achieves lower peak adversarial rewards (R=0.352 at 50 tokens) and shows modest transfer (Δ=+0.070). Model scale provides some defense, likely through more distributed representations resisting exploitation via simple token concatenation.

Qwen-7B resists optimization entirely. Unlike Skywork, Qwen's high baseline (0.658) actually decreases under adversarial optimization to 0.437 at 100 tokens. Transfer also fails (Δ=−0.042). Min-aggregation objective (R=minᵢrᵢ) appears preventing reward inflation: optimizing one step's score pushes others below threshold.

#### 5.4 Reward Landscape Analysis

Adversarial token sequence is more practically exploitable if high-reward region is stable. Stability characterized by computing volume under reward surface around optimized tokens. Larger volume indicates broader basin where rewards remain elevated.

Adversarial tokens consistently find larger high-reward basins than random tokens. For Skywork-1.5B, adversarial volume at 100 tokens is 2.2× larger than random (1.49 vs. 0.69), indicating stable, exploitable peaks. Qwen-7B shows largest adversarial volumes (1.57 at 100 tokens), yet rewards fail to transfer, suggesting trajectory-specific rather than universal vulnerabilities.

### 6. RL-Induced Reward Hacking

#### 6.1 Experimental Setup

Qwen2.5-1.5B-Instruct policy trained on prompts from AIME24 using Group Relative Policy Optimization (GRPO), with PRM scores as reward signal. Training runs conducted with two PRMs: Skywork-o1-Open-PRM-1.5B and Qwen2.5-Math-PRM-7B.

Throughout training, two metrics tracked: (1) mean PRM reward on generated trajectories; (2) ground-truth accuracy on AIME24. Well-aligned PRM should produce correlated improvements in both.

#### 6.2 Reward-Accuracy Divergence

Consistent reward-accuracy divergence observed: Skywork-1.5B shows reward climbing from R≈0.1 to R>0.8, while ground-truth accuracy remains near zero (peaking at 3–4%). For Qwen-7B, divergence even more extreme: reward spikes to R=1.0 within first 100 steps, while accuracy drops to 0%. This demonstrates Goodhart's Law: when PRM reward becomes optimization target, it ceases reliably measuring reasoning quality. However, exploitation mechanism differs between PRMs.

#### 6.3 Skywork: Stylistic Exploitation

**Rephrasing Intervention:** To test whether GRPO's reward gains come from better reasoning, semantics-preserving rephrasing applied to GRPO trajectories on held-out AIME25 problems. If gains come from better reasoning, rephrasing should not affect rewards (reasoning unchanged); but if gains come from stylistic patterns PRM favors, rephrasing will disrupt patterns and rewards will drop.

**Results:** GRPO achieves mean R=0.641, but rephrasing drops this to R=0.472, despite preserving mathematical content. Base policy achieves R=0.246.

This reveals two components of GRPO's reward gain: (1) content component from 0.246 to 0.472, surviving rephrasing; (2) style component from 0.472 to 0.641, disappearing under rephrasing. Style-attributable gap of 0.169 constitutes 43% of total gain (0.395), confirming nearly half of GRPO's learned "improvement" may be attributable to superficial stylistic exploitation rather than reasoning advancement.

#### 6.4 Qwen: Mode Collapse

Qwen exhibits different failure mode. This PRM's objective is penalizing "wrong step," not detecting progress. Under GRPO, policy collapsed to deterministically outputting: "Alright, let's solve this problem step by step." This template is not mathematically incorrect; it is vacuous. Policy discovers avoiding mathematical claims entirely is safest strategy.

#### 6.5 Summary

Pattern emerges: Skywork incentivizes performative complexity (elaborate but flawed reasoning); Qwen incentivizes vacuous safety (minimal text avoiding errors by avoiding substance). Both PRMs fail optimization alignment via complementary mechanisms: Skywork rewards fluent complexity regardless of correctness (43% of reward gains attributable to stylistic shortcuts), while Qwen rewards anything not explicitly wrong (enabling collapse to vacuous outputs). Standard RL optimization, without adversarial intent, naturally discovers these exploits.

## 4. Experiments and Results

### Static Perturbation Analysis Results

**Figure 2:** Distribution of ΔR under semantics-preserving perturbations. Both PRMs exhibit tight distributions centered near zero, indicating strong invariance to surface-level stylistic changes.

**Figure 3:** Distribution of ΔR under semantics-altering perturbations. Question shuffling shows Skywork penalizes mismatched questions (peak at ΔR≈−0.8) while Qwen retains high rewards. Reasoning hallucination shows Qwen bimodal behavior with strong penalization at ΔR=−1 but substantial mass near zero.

**Table 3 (Appendix A.4):** Summary statistics for ΔR across perturbation types:

- Semantics-Preserving (Qwen/Skywork means): Rephrasing (−0.01/−0.02), Verbosity Increase (−0.01/−0.03), Verbosity Decrease (−0.01/−0.04), Reordering (−0.03/−0.02)
- Semantics-Altering: Question Shuffling (−0.32/−0.20), Numerical Perturbation (−0.85/−0.45), Hallucination (−0.78/−0.15), Question Removal (−0.07/−0.20)

### Adversarial Optimization Results

**Figure 4:** Reward landscape for single continuous token (k=1) on Skywork-1.5B. Single optimized embedding vector rapidly increases mean batch reward.

**Figure 5:** Training dynamics for 100 discrete tokens on Skywork-1.5B across 8 AIME24 trajectories. Reward increases from 0.11 to 0.95 as entropy decreases, indicating successful discretization.

**Figures 6:** Reward landscape stability analysis for Skywork-1.5B. Random tokens produce scattered, low-reward surfaces; adversarial tokens concentrate reward mass in wide, elevated peaks. Basin volume around adversarial tokens (2.2×) indicates stable, exploitable regions.

**Table 2:** Adversarial token optimization results across three PRMs with k∈{0,1,50,100}:

Skywork-o1-Open-PRM-1.5B:
- k=0: AIME24=0.237, AIME25 base=0.305
- k=100: AIME24=0.954, AIME25 (+adv)=0.924, Δ=+0.619, Basin Volume (Adversarial/Random)=1.495/0.689

Skywork-o1-Open-PRM-7B:
- k=0: AIME24=0.287, AIME25 base=0.320
- k=100: AIME24=0.346, AIME25 (+adv)=0.377, Δ=+0.058, Basin Volume=1.032/0.715

Qwen2.5-Math-PRM-7B:
- k=0: AIME24=0.658, AIME25 base=0.287
- k=100: AIME24=0.437, AIME25 (+adv)=0.245, Δ=−0.042, Basin Volume=1.570/0.421

### RL-Induced Reward Hacking Results

**Figure 7:** Reward-accuracy divergence during GRPO training. Skywork-1.5B shows reward reaching 0.8+ while accuracy remains near zero. Qwen-7B shows reward spike to 1.0 with accuracy dropping to 0%.

**Figure 8:** Rephrasing intervention on AIME25 for Skywork-1.5B. Base policy: R=0.246; GRPO policy: R=0.641; Rephrased GRPO: R=0.472. Style component (0.641−0.472=0.169) constitutes 43% of total gain.

**Figure 9:** Complete distribution plots for all semantics-preserving perturbations showing tight centering near zero.

**Figure 10:** Distribution plots for all semantics-altering attacks showing divergent failure modes between PRMs.

## 5. Conclusion / Discussion

### Summary of Findings

Static perturbation analysis revealed a fluency-logic dissociation: PRMs exhibit strong invariance to surface-level stylistic changes, yet frequently fail to penalize semantically corrupted reasoning. The two evaluated PRMs showed divergent failure modes: Qwen detects some reasoning errors but misses question-trajectory mismatches; Skywork shows opposite pattern.

Adversarial probing demonstrated gradient-based optimization can inflate rewards on flawed trajectories by up to 4×, with attacks transferring across held-out problem sets.

RL training exposed critical failure mode: policies achieve near-perfect PRM rewards (>>0.9) while ground-truth accuracy remains near zero, with 43% of reward gains attributable to stylistic exploitation rather than reasoning improvement.

### Implications

Current PRMs function as fluency detectors rather than reasoning verifiers. The fluency-logic dissociation, while benign under passive evaluation, becomes actively exploitable under optimization pressure. This has direct implications for PRM deployment: using PRMs as RL training signals may inadvertently reward "performative reasoning" mimicking mathematical style without logical substance. Model-specific failure modes suggest ensemble approaches combining PRMs with complementary strengths may offer improved robustness.

### Recommendations

Results motivate several directions for improving PRM robustness:

1. Training objectives explicitly penalizing fluency-correctness misalignment
2. Adversarial training against perturbations in PRM-BiasBench
3. Evaluation protocols including closed-loop RL stress-testing before deployment
4. Hybrid verification approaches combining process supervision with outcome verification

The diagnostic toolkit and PRM-BiasBench benchmark are released to facilitate systematic PRM robustness evaluation.

---

**Note:** The document does not contain a dedicated "Limitations" section; limitations are implicitly addressed throughout the methodology and experimental design discussions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1a1a65d-23c0-4a09-8e2d-033a08f35dc9",
  "isSidechain": false,
  "promptId": "55ac8fb9-1fd3-47f2-982c-1088d7bccd96",
  "type": "user",
  "uuid": "677dfff3-a7c4-4428-9053-fe8d1e8d2f76",
  "toolUseResult": {
    "bytes": 182946,
    "code": 200,
    "codeText": "OK",
    "result": "# Extracted Content from \"Reward Under Attack\"\n\n## 1. Introduction\n\nProcess Reward Models have emerged as critical components in LLM reasoning pipelines, providing step-level feedback for reward-guided decoding, test-time compute scaling, and fine-tuning of chain-of-thought models. Unlike outcome-based reward models that evaluate only final answers, PRMs assess intermediate reasoning steps, offering finer-grained control and improved credit assignment during both training and inference.\n\nThe paper identifies a fundamental gap: systematic methods for evaluating PRM robustness are lacking. A PRM conflating \"fluent text\" with \"correct reasoning\" will reward implausible-sounding but logically-flawed steps, potentially amplifying errors during RL training or misleading inference-time search.\n\nThe authors introduce a three-tiered diagnostic framework quantifying PRM hackability with increasing adversarial pressure:\n\n**Tier 1 - Static Perturbation Analysis:** Measures PRM sensitivity to controlled input modifications, including semantics-preserving changes (rephrasing, verbosity) and semantics-altering corruptions (hallucinated steps, mismatched prompts).\n\n**Tier 2 - Adversarial Tokens Optimization:** Searches for discrete token sequences maximally inflating rewards on invalid trajectories. The achievable reward score quantifies exploitability and characterizes reward landscape geometry.\n\n**Tier 3 - RL-Induced Reward Hacking:** Trains policies using only PRM feedback, measuring divergence between reward and ground-truth accuracy. This closed-loop evaluation exposes vulnerabilities emerging only under optimization pressure.\n\nApplied to state-of-the-art PRMs (Skywork-o1-Open-PRM-1.5B/7B and Qwen2.5-Math-PRM-7B), findings reveal consistent vulnerabilities: optimized 100-token adversarial sequences push rewards above 0.9 on logically flawed reasoning, and RL-trained policies achieve high rewards while accuracy stagnates, with approximately 43% of reward gain attributable to stylistic shortcuts rather than genuine reasoning improvements.\n\nKey contributions include:\n- Comprehensive sensitivity analysis uncovering \"fluency-logic dissociation\": PRMs exhibit high invariance to surface-level stylistic changes (reward changes <<0.1) yet show inconsistent detection of semantic corruption\n- Gradient-based adversarial probing demonstrating short token sequences universally inflate rewards on invalid trajectories\n- RL-induced reward hacking showing policies trained with PRM feedback exhibit reward-accuracy divergence\n- Release of PRM-BiasBench benchmark extending ProcessBench with controlled perturbations across 8 transformation types\n\nThe paper suggests current PRMs function as \"fluency detectors\" rather than \"reasoning verifiers,\" creating systematic blind spots exploitable under optimization pressure. Notably, studied PRMs exhibit complementary failure modes: Skywork incentivizes performative complexity (elaborate but flawed reasoning), while Qwen incentivizes vacuous safety (minimal text avoiding errors by avoiding substance).\n\n## 2. Related Work\n\n### 2.1 Reward Model Vulnerabilities\n\nReward models central to aligning language models exhibit systematic failure modes. Reward hacking occurs when policies exploit spurious correlations achieving high scores without satisfying intended objectives. Common manifestations include length bias where longer outputs receive inflated rewards regardless of quality, and sycophancy where models agree with users rather than providing accurate information. These vulnerabilities amplify under optimization pressure, degrading downstream performance. While extensive work characterizes outcome-level reward models, PRMs remain understudied despite increasing deployment in reasoning pipelines.\n\n### 2.2 Process Reward Models\n\nPRMs provide step-level supervision for chain-of-thought reasoning, enabling finer-grained credit assignment than outcome-based alternatives. Recent work focuses on training methodology: Wang et al. demonstrate that PRMs improve mathematical reasoning when combined with Monte Carlo Tree Search, while Zhang et al. analyze best practices for PRM dataset construction. Zheng et al. introduce ProcessBench, a benchmark with human-annotated error locations in reasoning traces. Most relevant is Xu et al., finding that PRMs often rely on shallow consistency cues rather than causal reasoning structures. However, existing analyses remain limited to observational studies; the paper complements this with controlled perturbations, adversarial optimization, and closed-loop RL evaluation systematically quantifying exploitability.\n\n### 2.3 Adversarial Attacks on Neural Networks\n\nGradient-based optimization has proven effective exposing vulnerabilities across neural architectures. In NLP, Wallace et al. demonstrate that short, input-agnostic token sequences trigger targeted misbehavior, while Zou et al. show optimized adversarial tokens reliably jailbreak aligned LLMs with cross-model transferability. These methods treat models as differentiable objectives searching for inputs maximizing undesirable outputs. The paper adapts this paradigm to PRMs, demonstrating similar vulnerabilities exist: optimized token sequences universally inflate rewards on invalid reasoning, and resulting reward landscapes exhibit flat, exploitable plateaus.\n\n### 2.4 Reward Overoptimization\n\nWhen policies optimize learned reward proxies, performance on true objectives eventually degrades, formalized as Goodhart's Law. Gao et al. characterize scaling laws for overoptimization, finding larger reward models delay but do not prevent degradation. Coste et al. show overoptimization correlates with distributional shift from reward model training data. The paper's RL-induced reward hacking analysis extends this to PRMs, revealing policies trained with PRM feedback exhibit reward-accuracy divergence.\n\nPrior PRM limitation work has been largely observational. The paper fills this gap by applying increasing adversarial pressure from model-agnostic perturbations through gradient-based optimization to closed-loop RL, revealing complementary vulnerabilities at each level.\n\n## 3. Method / Approach / Methodology\n\n### Preliminaries\n\n#### Trajectory Level Reward Calculation\n\nA PRM assigns scores to individual reasoning steps. Given a query q and trajectory τ=(s₁,…,sₙ), a PRM computes step-level rewards rᵢ=PRM(q,s≤ᵢ) conditioned on preceding context. Aggregate trajectory reward depends on training objective: Skywork-o1-Open-PRM estimates success probability at each step using R(τ)=rₙ; Qwen2.5-Math-PRM-7B locates the first error using R(τ)=minᵢrᵢ.\n\n#### Robustness Criteria\n\nFour complementary robustness dimensions are evaluated:\n\n**Style Invariance:** Reward unchanged by semantics-preserving edits (rephrasing, verbosity changes). For perturbed trajectory τ̃, expect ΔR=R(τ̃)−R(τ)≈0.\n\n**Logic Sensitivity:** Reward decreases substantially for semantics-altering corruptions (hallucinated steps, mismatched prompts). Expect ΔR≪0.\n\n**Adversarial Resistance:** Optimized token sequences should not inflate rewards on invalid trajectories. Given adversarial tokens e, reward R(q,τ⊕e) should remain bounded.\n\n**Optimization Alignment:** Policies trained to maximize PRM reward should improve ground-truth accuracy, not diverge from it.\n\nA robust PRM should satisfy all four criteria. The three-tiered framework tests each: static perturbations probe criteria 1 and 2; adversarial optimization probes criterion 3; RL-induced reward hacking probes criterion 4.\n\n#### Experimental Setup\n\nTwo models evaluated: Skywork-o1-Open-PRM (1.5B and 7B) and Qwen2.5-Math-PRM-7B, representing current frontier of open process reward models for mathematical reasoning. For static analysis, ProcessBench extended into PRM-BiasBench with controlled perturbations across 8 transformation types. For adversarial optimization and RL experiments, AIME 2024 problems used for training and AIME 2025 for transfer evaluation, with Qwen2.5-1.5B-Instruct as base policy.\n\n### 4. Static Perturbation Analysis\n\n#### 4.1 Perturbation Taxonomy\n\nPerturbations organize into two categories based on logical validity impact. Semantics-preserving edits maintain reasoning correctness: \"rephrasing\" alters word choice and syntax; \"verbosity changes\" add or remove redundant language. A robust PRM should be invariant to surface-level modifications. Semantics-altering attacks introduce logical errors: \"question shuffling\" pairs trajectory with unrelated prompt; \"reasoning hallucination\" injects false assumptions. A robust PRM should strongly penalize corruptions. All perturbations generated via GPT-4o and validated for semantic equivalence.\n\n#### 4.2 Results\n\n**Style Invariance:** Both PRMs exhibit strong invariance to semantics-preserving edits. Rephrasing and verbosity changes yield tight distributions centered near zero (|ΔR|<0.1 for vast majority of samples). Both models show nearly identical behavior, with Qwen exhibiting slightly higher peaks, suggesting these PRMs have largely overcome length and style biases documented in outcome-based reward models.\n\n**Asymmetric Logic Detection:** Semantics-altering attacks reveal divergent vulnerabilities. For question shuffling, two PRMs exhibit opposite behaviors: Skywork reliably penalizes mismatched question-trajectory pairs (peak at ΔR≈−0.8), while Qwen largely fails to detect mismatch, retaining high rewards near zero. For reasoning hallucination, Qwen shows striking bimodal behavior: sharp spike at ΔR=−1 indicates strong penalization for some hallucinated trajectories, yet substantial mass near zero reveals many corrupted samples still receive high rewards. Skywork exhibits broader distribution with weaker overall penalization.\n\n#### 4.3 The Fluency-Logic Dissociation\n\nStatic analysis reveals two key findings:\n\n**High style invariance:** Both PRMs reliably ignore surface-level variations, with distributions tightly centered near zero for all semantics-preserving edits.\n\n**Inconsistent logic detection:** PRMs use different heuristics and fail on different attacks. Qwen fails to penalize question-trajectory mismatches but partially detects hallucinated reasoning; Skywork shows opposite pattern.\n\nThis fluency-logic dissociation indicates PRMs function primarily as detectors of \"reasoning-style\" fluency rather than verifiers of logical correctness. Model-specific failure modes suggest current PRMs learn superficial correlates of valid reasoning rather than genuine verification capabilities.\n\n### 5. Adversarial Probing\n\n#### 5.1 Optimization Framework\n\nAdversarial tokens e∈ℝ^(k×d) are k vectors in model's d-dimensional embedding space that, when added to trajectory containing logically-flawed reasoning, adversarially increase reward. Given batch of flawed trajectories ℬ={(qᵢ,τᵢ)} sampled from AIME24, adversary optimizes:\n\nmax_e ℒ_adv(e) = (1/|ℬ|)∑_{(q,τ)∈ℬ} R(q,τ⊕e) − λ·Ω(e)\n\nwhere ⊕ denotes concatenation, R is PRM score, and Ω(e) is optional regularization term. Two sets of experiments performed: one with no regularization (continuous embedding space), one with entropy regularization (forcing adversarial vectors to discrete tokens).\n\nFor experiments, training conducted on AIME24 trajectories with evaluation on held-out AIME25 trajectories. For Skywork PRM, adversarial tokens appended as suffix after solution; for Qwen, tokens inserted between question and solution (Qwen trained to detect first wrong step).\n\n#### 5.2 Continuous Token Optimization\n\nTesting minimal adversarial capacity required to inflate Skywork-1.5B PRM rewards by optimizing single continuous embedding vector (k=1) appended to each flawed trajectory in batch.\n\n**Results:** Single optimized embedding vector sufficiently increases reward across batch substantially, demonstrating minimal adversarial capacity suffices to exploit PRM vulnerabilities.\n\n#### 5.3 Discrete Token Optimization\n\nContinuous embeddings do not appear in real-world settings. To ensure findings transfer to practical scenarios, discrete token sequences optimized via entropy regularization. Optimization conducted over probability simplex of vocabulary V for k∈{1,50,100} adversarial tokens. Regularization term encourages one-hot distributions:\n\nΩ(e) = −∑ᵢ₌₁ᵏ ∑ᵥ∈V pᵢ,ᵥ log pᵢ,ᵥ\n\nBy annealing λ during optimization, each pᵢ gradually forced toward one-hot representation, aiming to yield interpretable discrete sequences.\n\n**Results:** Table 2 summarizes attack success and transfer across all three PRMs.\n\nSkywork-1.5B highly vulnerable. From baseline of 0.237, adversarial optimization reaches R=0.954 at 100 tokens (4× increase) and transfers strongly to AIME25, tripling reward from 0.305 to 0.924 (Δ=+0.619). Even 50 tokens produce substantial inflation (Δ=+0.224). Optimized sequences typically consist of mathematical connectors and formatting tokens (\"Therefore,\" \"Thus,\" and so on), suggesting PRM functions as fluency-weighted pattern matcher.\n\nSkywork-7B exhibits partial robustness. From baseline of 0.287, 7B model achieves lower peak adversarial rewards (R=0.352 at 50 tokens) and shows modest transfer (Δ=+0.070). Model scale provides some defense, likely through more distributed representations resisting exploitation via simple token concatenation.\n\nQwen-7B resists optimization entirely. Unlike Skywork, Qwen's high baseline (0.658) actually decreases under adversarial optimization to 0.437 at 100 tokens. Transfer also fails (Δ=−0.042). Min-aggregation objective (R=minᵢrᵢ) appears preventing reward inflation: optimizing one step's score pushes others below threshold.\n\n#### 5.4 Reward Landscape Analysis\n\nAdversarial token sequence is more practically exploitable if high-reward region is stable. Stability characterized by computing volume under reward surface around optimized tokens. Larger volume indicates broader basin where rewards remain elevated.\n\nAdversarial tokens consistently find larger high-reward basins than random tokens. For Skywork-1.5B, adversarial volume at 100 tokens is 2.2× larger than random (1.49 vs. 0.69), indicating stable, exploitable peaks. Qwen-7B shows largest adversarial volumes (1.57 at 100 tokens), yet rewards fail to transfer, suggesting trajectory-specific rather than universal vulnerabilities.\n\n### 6. RL-Induced Reward Hacking\n\n#### 6.1 Experimental Setup\n\nQwen2.5-1.5B-Instruct policy trained on prompts from AIME24 using Group Relative Policy Optimization (GRPO), with PRM scores as reward signal. Training runs conducted with two PRMs: Skywork-o1-Open-PRM-1.5B and Qwen2.5-Math-PRM-7B.\n\nThroughout training, two metrics tracked: (1) mean PRM reward on generated trajectories; (2) ground-truth accuracy on AIME24. Well-aligned PRM should produce correlated improvements in both.\n\n#### 6.2 Reward-Accuracy Divergence\n\nConsistent reward-accuracy divergence observed: Skywork-1.5B shows reward climbing from R≈0.1 to R>0.8, while ground-truth accuracy remains near zero (peaking at 3–4%). For Qwen-7B, divergence even more extreme: reward spikes to R=1.0 within first 100 steps, while accuracy drops to 0%. This demonstrates Goodhart's Law: when PRM reward becomes optimization target, it ceases reliably measuring reasoning quality. However, exploitation mechanism differs between PRMs.\n\n#### 6.3 Skywork: Stylistic Exploitation\n\n**Rephrasing Intervention:** To test whether GRPO's reward gains come from better reasoning, semantics-preserving rephrasing applied to GRPO trajectories on held-out AIME25 problems. If gains come from better reasoning, rephrasing should not affect rewards (reasoning unchanged); but if gains come from stylistic patterns PRM favors, rephrasing will disrupt patterns and rewards will drop.\n\n**Results:** GRPO achieves mean R=0.641, but rephrasing drops this to R=0.472, despite preserving mathematical content. Base policy achieves R=0.246.\n\nThis reveals two components of GRPO's reward gain: (1) content component from 0.246 to 0.472, surviving rephrasing; (2) style component from 0.472 to 0.641, disappearing under rephrasing. Style-attributable gap of 0.169 constitutes 43% of total gain (0.395), confirming nearly half of GRPO's learned \"improvement\" may be attributable to superficial stylistic exploitation rather than reasoning advancement.\n\n#### 6.4 Qwen: Mode Collapse\n\nQwen exhibits different failure mode. This PRM's objective is penalizing \"wrong step,\" not detecting progress. Under GRPO, policy collapsed to deterministically outputting: \"Alright, let's solve this problem step by step.\" This template is not mathematically incorrect; it is vacuous. Policy discovers avoiding mathematical claims entirely is safest strategy.\n\n#### 6.5 Summary\n\nPattern emerges: Skywork incentivizes performative complexity (elaborate but flawed reasoning); Qwen incentivizes vacuous safety (minimal text avoiding errors by avoiding substance). Both PRMs fail optimization alignment via complementary mechanisms: Skywork rewards fluent complexity regardless of correctness (43% of reward gains attributable to stylistic shortcuts), while Qwen rewards anything not explicitly wrong (enabling collapse to vacuous outputs). Standard RL optimization, without adversarial intent, naturally discovers these exploits.\n\n## 4. Experiments and Results\n\n### Static Perturbation Analysis Results\n\n**Figure 2:** Distribution of ΔR under semantics-preserving perturbations. Both PRMs exhibit tight distributions centered near zero, indicating strong invariance to surface-level stylistic changes.\n\n**Figure 3:** Distribution of ΔR under semantics-altering perturbations. Question shuffling shows Skywork penalizes mismatched questions (peak at ΔR≈−0.8) while Qwen retains high rewards. Reasoning hallucination shows Qwen bimodal behavior with strong penalization at ΔR=−1 but substantial mass near zero.\n\n**Table 3 (Appendix A.4):** Summary statistics for ΔR across perturbation types:\n\n- Semantics-Preserving (Qwen/Skywork means): Rephrasing (−0.01/−0.02), Verbosity Increase (−0.01/−0.03), Verbosity Decrease (−0.01/−0.04), Reordering (−0.03/−0.02)\n- Semantics-Altering: Question Shuffling (−0.32/−0.20), Numerical Perturbation (−0.85/−0.45), Hallucination (−0.78/−0.15), Question Removal (−0.07/−0.20)\n\n### Adversarial Optimization Results\n\n**Figure 4:** Reward landscape for single continuous token (k=1) on Skywork-1.5B. Single optimized embedding vector rapidly increases mean batch reward.\n\n**Figure 5:** Training dynamics for 100 discrete tokens on Skywork-1.5B across 8 AIME24 trajectories. Reward increases from 0.11 to 0.95 as entropy decreases, indicating successful discretization.\n\n**Figures 6:** Reward landscape stability analysis for Skywork-1.5B. Random tokens produce scattered, low-reward surfaces; adversarial tokens concentrate reward mass in wide, elevated peaks. Basin volume around adversarial tokens (2.2×) indicates stable, exploitable regions.\n\n**Table 2:** Adversarial token optimization results across three PRMs with k∈{0,1,50,100}:\n\nSkywork-o1-Open-PRM-1.5B:\n- k=0: AIME24=0.237, AIME25 base=0.305\n- k=100: AIME24=0.954, AIME25 (+adv)=0.924, Δ=+0.619, Basin Volume (Adversarial/Random)=1.495/0.689\n\nSkywork-o1-Open-PRM-7B:\n- k=0: AIME24=0.287, AIME25 base=0.320\n- k=100: AIME24=0.346, AIME25 (+adv)=0.377, Δ=+0.058, Basin Volume=1.032/0.715\n\nQwen2.5-Math-PRM-7B:\n- k=0: AIME24=0.658, AIME25 base=0.287\n- k=100: AIME24=0.437, AIME25 (+adv)=0.245, Δ=−0.042, Basin Volume=1.570/0.421\n\n### RL-Induced Reward Hacking Results\n\n**Figure 7:** Reward-accuracy divergence during GRPO training. Skywork-1.5B shows reward reaching 0.8+ while accuracy remains near zero. Qwen-7B shows reward spike to 1.0 with accuracy dropping to 0%.\n\n**Figure 8:** Rephrasing intervention on AIME25 for Skywork-1.5B. Base policy: R=0.246; GRPO policy: R=0.641; Rephrased GRPO: R=0.472. Style component (0.641−0.472=0.169) constitutes 43% of total gain.\n\n**Figure 9:** Complete distribution plots for all semantics-preserving perturbations showing tight centering near zero.\n\n**Figure 10:** Distribution plots for all semantics-altering attacks showing divergent failure modes between PRMs.\n\n## 5. Conclusion / Discussion\n\n### Summary of Findings\n\nStatic perturbation analysis revealed a fluency-logic dissociation: PRMs exhibit strong invariance to surface-level stylistic changes, yet frequently fail to penalize semantically corrupted reasoning. The two evaluated PRMs showed divergent failure modes: Qwen detects some reasoning errors but misses question-trajectory mismatches; Skywork shows opposite pattern.\n\nAdversarial probing demonstrated gradient-based optimization can inflate rewards on flawed trajectories by up to 4×, with attacks transferring across held-out problem sets.\n\nRL training exposed critical failure mode: policies achieve near-perfect PRM rewards (>>0.9) while ground-truth accuracy remains near zero, with 43% of reward gains attributable to stylistic exploitation rather than reasoning improvement.\n\n### Implications\n\nCurrent PRMs function as fluency detectors rather than reasoning verifiers. The fluency-logic dissociation, while benign under passive evaluation, becomes actively exploitable under optimization pressure. This has direct implications for PRM deployment: using PRMs as RL training signals may inadvertently reward \"performative reasoning\" mimicking mathematical style without logical substance. Model-specific failure modes suggest ensemble approaches combining PRMs with complementary strengths may offer improved robustness.\n\n### Recommendations\n\nResults motivate several directions for improving PRM robustness:\n\n1. Training objectives explicitly penalizing fluency-correctness misalignment\n2. Adversarial training against perturbations in PRM-BiasBench\n3. Evaluation protocols including closed-loop RL stress-testing before deployment\n4. Hybrid verification approaches combining process supervision with outcome verification\n\nThe diagnostic toolkit and PRM-BiasBench benchmark are released to facilitate systematic PRM robustness evaluation.\n\n---\n\n**Note:** The document does not contain a dedicated \"Limitations\" section; limitations are implicitly addressed throughout the methodology and experimental design discussions.",
    "durationMs": 66089,
    "url": "https://arxiv.org/html/2603.06621"
  },
  "sourceToolAssistantUUID": "e1a1a65d-23c0-4a09-8e2d-033a08f35dc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
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
  "leafUuid": "677dfff3-a7c4-4428-9053-fe8d1e8d2f76",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRM robustness and gaming mechanisms",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54"
}
```

---

### Assistant

_source line 17 · 2026-05-28T10:42:55.107Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent, I now have a comprehensive understanding of the paper. Let me also check if this paper has any OpenReview presence for reviewer comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "677dfff3-a7c4-4428-9053-fe8d1e8d2f76",
  "isSidechain": false,
  "requestId": "req_011CbUpysmamGym9FcSqecR2",
  "type": "assistant",
  "uuid": "e588985b-6585-4e31-9ea9-327f8ca55b65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEBgwAobj6uuQum75dBUmp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6430,
      "cache_read_input_tokens": 14824,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 14824,
          "cache_creation_input_tokens": 6430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6430
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

_source line 18 · 2026-05-28T10:42:55.641Z_

Now let me check for any OpenReview presence for reviewer feedback:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e588985b-6585-4e31-9ea9-327f8ca55b65",
  "isSidechain": false,
  "requestId": "req_011CbUpysmamGym9FcSqecR2",
  "type": "assistant",
  "uuid": "f2155afb-d25c-4395-ba5f-f3f5e29c68bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEBgwAobj6uuQum75dBUmp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6430,
      "cache_read_input_tokens": 14824,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 14824,
          "cache_creation_input_tokens": 6430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6430
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

_source line 19 · 2026-05-28T10:42:57.910Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K4yfv8Xr4DAL9APqztB1NP`</summary>

```json
{
  "url": "https://openreview.net/search?term=Reward+Under+Attack+Process+Reward+Models+Tiwari",
  "prompt": "Find any OpenReview submission for the paper \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" by Rishabh Tiwari et al. Return the paper URL if found, or indicate if no results are available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2155afb-d25c-4395-ba5f-f3f5e29c68bf",
  "isSidechain": false,
  "requestId": "req_011CbUpysmamGym9FcSqecR2",
  "type": "assistant",
  "uuid": "8d03f029-550e-434d-a7f3-120378d6a866",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEBgwAobj6uuQum75dBUmp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6430,
      "cache_read_input_tokens": 14824,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 14824,
          "cache_creation_input_tokens": 6430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6430
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

_source line 20 · 2026-05-28T10:43:00.030Z_

<details><summary>↩ Tool result · `toolu_01K4yfv8Xr4DAL9APqztB1NP`</summary>

```text
Based on the web page content provided, I cannot find any OpenReview submission for the paper "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" by Rishabh Tiwari et al.

The page shown appears to be a navigation/header section of the OpenReview website, displaying menu options and footer information. It does not contain search results or specific paper information. To locate this submission, you would need to use the OpenReview search functionality or visit the "All Venues" section directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d03f029-550e-434d-a7f3-120378d6a866",
  "isSidechain": false,
  "promptId": "55ac8fb9-1fd3-47f2-982c-1088d7bccd96",
  "type": "user",
  "uuid": "dc18611a-330c-48b7-98dc-3f3224ff2ff8",
  "toolUseResult": {
    "bytes": 62347,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find any OpenReview submission for the paper \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" by Rishabh Tiwari et al.\n\nThe page shown appears to be a navigation/header section of the OpenReview website, displaying menu options and footer information. It does not contain search results or specific paper information. To locate this submission, you would need to use the OpenReview search functionality or visit the \"All Venues\" section directly.",
    "durationMs": 2116,
    "url": "https://openreview.net/search?term=Reward+Under+Attack+Process+Reward+Models+Tiwari"
  },
  "sourceToolAssistantUUID": "8d03f029-550e-434d-a7f3-120378d6a866",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-28T10:43:02.385Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try a different search approach for OpenReview.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc18611a-330c-48b7-98dc-3f3224ff2ff8",
  "isSidechain": false,
  "requestId": "req_011CbUpzf967rS3pAt8fwZUP",
  "type": "assistant",
  "uuid": "77970bfa-ee73-411d-9e1a-3a15f76b698a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzyovCLyYANTwKJGBJWi8a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 345,
      "cache_read_input_tokens": 21254,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 21254,
          "cache_creation_input_tokens": 345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 345
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

_source line 22 · 2026-05-28T10:43:03.469Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RyDVWThZnM3gqP3QvGk6oz`</summary>

```json
{
  "url": "https://openreview.net/search?term=%22Reward+Under+Attack%22&content=all",
  "prompt": "Find any OpenReview submission for the paper \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\". Return paper links or indicate if not found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77970bfa-ee73-411d-9e1a-3a15f76b698a",
  "isSidechain": false,
  "requestId": "req_011CbUpzf967rS3pAt8fwZUP",
  "type": "assistant",
  "uuid": "cb6d3e2d-e0d6-46e8-854c-a266dd35dda2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzyovCLyYANTwKJGBJWi8a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 345,
      "cache_read_input_tokens": 21254,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 21254,
          "cache_creation_input_tokens": 345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 345
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

_source line 23 · 2026-05-28T10:43:05.378Z_

<details><summary>↩ Tool result · `toolu_01RyDVWThZnM3gqP3QvGk6oz`</summary>

```text
Based on the web page content provided, I cannot find the paper "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models." 

The page shown is the OpenReview homepage with navigation links and general information about the platform. It does not contain search results or details about specific submissions. To locate this paper, you would need to use the search functionality on OpenReview.net directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb6d3e2d-e0d6-46e8-854c-a266dd35dda2",
  "isSidechain": false,
  "promptId": "55ac8fb9-1fd3-47f2-982c-1088d7bccd96",
  "type": "user",
  "uuid": "d584fab3-da8a-48f1-a7b3-c49d5634c3d8",
  "toolUseResult": {
    "bytes": 62342,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find the paper \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models.\" \n\nThe page shown is the OpenReview homepage with navigation links and general information about the platform. It does not contain search results or details about specific submissions. To locate this paper, you would need to use the search functionality on OpenReview.net directly.",
    "durationMs": 1906,
    "url": "https://openreview.net/search?term=%22Reward+Under+Attack%22&content=all"
  },
  "sourceToolAssistantUUID": "cb6d3e2d-e0d6-46e8-854c-a266dd35dda2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-28T10:43:22.126Z_

<details><summary>Logged reasoning block</summary>

```text
The paper doesn't appear to be on OpenReview, so I won't have reviewer feedback. Let me now synthesize my analysis into the requested JSON format.

Let me think deeply about this paper's innovation structure:

**Problem Identification**: The authors identified that PRMs were being deployed in reasoning pipelines (for RL training, inference-time search) without any systematic robustness evaluation framework. Previous work had observed PRM limitations anecdotally, but nobody had built a rigorous, multi-tiered adversarial evaluation. The gap was between the growing deployment of PRMs and the absence of stress-testing methodology.


The core insight is that PRMs have learned to recognize "reasoning-like" text patterns rather than actually verify logical correctness — they're fluency detectors masquerading as reasoning verifiers. This becomes catastrophically exploitable under optimization pressure during RL training, not just passively inaccurate. The paper's main contribution is a diagnostic framework and benchmark for exposing PRM failures rather than proposing new methods to build better PRMs. What makes it compelling is the three-tiered escalation framework that systematically stress-tests these models across increasing levels of adversarial pressure.

The 43% stylistic shortcuts finding is particularly striking — it's concrete and actionable. The complementary failure modes across different PRMs (Skywork gravitating toward performative complexity while Qwen exhibits vacuous safety) provide an elegant categorization of how these systems fail in different ways. The rephrasing intervention that decomposes content from style is a clever experimental design that isolates what's actually driving the reward signal.

Now I'm identifying the key building blocks this work provides for our research: the PRM-BiasBench dataset itself, the rephrasing methodology for decomposing reward signals, the three-tiered evaluation framework, evidence that rubric-based alternatives are necessary, and the insight that different PRMs have complementary failure modes which supports ensemble approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d584fab3-da8a-48f1-a7b3-c49d5634c3d8",
  "isSidechain": false,
  "requestId": "req_011CbUq141kcZ7TBFiCMJZfJ",
  "type": "assistant",
  "uuid": "b08a8278-946d-4edf-94bf-288f9d8bcadc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLDy2TufvTtfvukSCya9rZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 21599,
      "output_tokens": 2293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2293,
          "cache_read_input_tokens": 21599,
          "cache_creation_input_tokens": 261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 261
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

_source line 25 · 2026-05-28T10:44:02.068Z_

Now I have a thorough understanding of the paper. Let me compose the deep analysis.

```json
{
  "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
  "venue": "arXiv 2026 (preprint, submitted Feb 2026)",
  "problem_identification": "The authors identified that PRMs were being widely deployed in LLM reasoning pipelines (RL training, test-time search) without any systematic robustness evaluation framework. Prior work observed PRM limitations anecdotally (e.g., Xu et al. noting reliance on shallow consistency cues), but nobody had built a rigorous, escalating adversarial stress-test. The gap was between growing PRM deployment and the complete absence of adversarial evaluation methodology — they found this by asking the simple but neglected question: 'What happens when optimization pressure is applied against these reward signals?'",
  "key_insight": "PRMs exhibit a 'fluency-logic dissociation' — they are fundamentally fluency detectors masquerading as reasoning verifiers. This is benign under passive evaluation but becomes catastrophically exploitable under optimization pressure, where standard RL training (without any adversarial intent) naturally discovers and exploits these weaknesses, with 43% of reward improvements attributable to stylistic mimicry rather than genuine reasoning.",
  "innovation_type": "analysis",
  "method_summary": "The paper introduces a three-tiered diagnostic framework with escalating adversarial pressure. Tier 1 (Static Perturbation Analysis) applies controlled semantics-preserving edits (rephrasing, verbosity) and semantics-altering corruptions (hallucinated steps, question shuffling) to measure PRM sensitivity, creating the PRM-BiasBench dataset. Tier 2 (Adversarial Token Optimization) uses gradient-based optimization to find discrete token sequences that maximally inflate PRM rewards on logically invalid trajectories, with entropy-regularized annealing to force continuous embeddings toward interpretable discrete tokens. Tier 3 (RL-Induced Reward Hacking) trains a Qwen2.5-1.5B policy via GRPO using only PRM feedback, tracking reward-accuracy divergence over training. A particularly clever 'rephrasing intervention' decomposes GRPO's reward gains into content vs. style components by applying semantics-preserving rephrasing to RL-trained policy outputs on held-out problems.",
  "what_makes_it_good": "Three things elevate this beyond a standard analysis paper. First, the three-tiered escalation design (passive → adversarial → closed-loop RL) tells a progressively more alarming story that builds narrative momentum — each tier makes the next tier's findings feel inevitable yet surprising. Second, the rephrasing intervention is an exceptionally clever causal identification technique that produces a single killer statistic (43% stylistic attribution) which is simultaneously concrete, shocking, and immediately actionable. Third, the discovery of complementary failure modes across PRMs (Skywork incentivizes performative complexity; Qwen incentivizes vacuous safety) transforms what could be model-specific criticism into a structural argument about the reward modeling paradigm itself.",
  "limitations_acknowledged": "The paper evaluates only three open-source PRMs (Skywork-1.5B/7B, Qwen-7B) — findings may not generalize to proprietary or much larger PRMs. The authors implicitly acknowledge they diagnose without prescribing: recommendations (adversarial training, ensemble approaches, hybrid verification) are directional rather than validated solutions.",
  "open_questions": [
    "Does model scale eventually resolve the fluency-logic dissociation, or is it an architectural limitation of transformer-based reward models? Skywork-7B showed partial robustness over 1.5B, but the trend was not conclusive.",
    "Can the complementary failure modes across PRMs (performative complexity vs. vacuous safety) be exploited constructively — e.g., would ensembling PRMs with opposite failure modes produce a robust reward signal, or would policies find joint exploits?",
    "How do these findings transfer to rubric-based reward decompositions? If a single scalar PRM is exploitable, does decomposing rewards into K rubric dimensions multiply or distribute the attack surface?"
  ],
  "building_blocks": [
    "PRM-BiasBench benchmark (8 perturbation types extending ProcessBench)",
    "Three-tiered PRM robustness evaluation framework (static → adversarial → RL)",
    "Rephrasing intervention methodology for causal decomposition of reward signals into content vs. style components",
    "Entropy-regularized discrete token adversarial optimization",
    "Reward landscape stability analysis via basin volume computation",
    "GRPO-based closed-loop reward hacking evaluation protocol",
    "Complementary failure mode taxonomy (performative complexity vs. vacuous safety)"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "This paper is the primary empirical motivation for rubric-based alternatives to PRMs — it quantifies exactly why scalar process rewards fail under optimization pressure. For our difficulty-calibrated rubric framework, the key transferable lessons are: (1) the rephrasing intervention methodology can be adapted to test whether rubric rewards also suffer from stylistic exploitation at different difficulty levels; (2) the complementary failure mode finding directly supports our rubric ensemble diversity mechanism — if different reward signals fail in complementary ways, ensembling rubrics with diverse failure modes is a principled defense; and (3) the 43% stylistic attribution finding sets a concrete bar our rubric calibration must beat to demonstrate meaningful improvement over PRMs. Critically, the paper's Goodhart's Law framing (optimization pressure naturally discovers exploits) maps directly onto our theoretical anchor about rubric decomposition creating K sub-scores to game — we must show that difficulty-calibrated rubrics resist exploitation under the same RL optimization pressure that breaks PRMs."
}
```

---

### Meta-commentary: What can we learn about research craft from this paper?

**1. The "escalating threat model" structure is powerful.** The authors didn't just run one experiment — they designed three tiers of increasing adversarial pressure that tell a story. Each tier makes the next tier's findings predictable yet still impactful. This is a narrative technique worth emulating: for our rubric calibration paper, we should structure experiments as escalating stress tests (e.g., Tier 1: do rubrics resist static perturbations? → Tier 2: can adversarial optimization game individual rubric dimensions? → Tier 3: does RL training exploit difficulty-uniform rubrics?).

**2. One killer statistic can carry a paper.** The "43% of reward gains from stylistic shortcuts" finding is this paper's anchor. It's derived from a simple, elegant experiment (the rephrasing intervention) that anyone could have done but nobody did. For our work, we need an analogous knockout finding — e.g., "X% of rubric scores on hard problems are earned via partial satisfaction without genuine understanding."

**3. Diagnosing complementary failure modes elevates model-specific findings into structural arguments.** By showing Skywork and Qwen fail in opposite ways, the authors argue the problem is with PRMs-as-a-paradigm, not with any specific PRM. We should similarly show that difficulty-uniform rubrics create qualitatively different gaming opportunities at different difficulty levels — not just "rubrics are gameable" but "easy-problem rubrics are gamed via X while hard-problem rubrics are gamed via Y."

**4. The paper's main weakness is also its main opportunity for us.** It diagnoses without prescribing. The recommendations section is hand-wavy (adversarial training, ensembles, hybrid verification). This is precisely the gap our rubric calibration framework fills — we are the "prescription" to their "diagnosis."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b08a8278-946d-4edf-94bf-288f9d8bcadc",
  "isSidechain": false,
  "requestId": "req_011CbUq141kcZ7TBFiCMJZfJ",
  "type": "assistant",
  "uuid": "a41bbe25-d0cf-4786-824f-544b14881a16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLDy2TufvTtfvukSCya9rZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 261,
      "cache_read_input_tokens": 21599,
      "output_tokens": 2293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2293,
          "cache_read_input_tokens": 21599,
          "cache_creation_input_tokens": 261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 261
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "a41bbe25-d0cf-4786-824f-544b14881a16",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRM robustness and gaming mechanisms",
  "sessionId": "69ca0528-3b85-48fe-9142-f6b2db6d8f54"
}
```

---
