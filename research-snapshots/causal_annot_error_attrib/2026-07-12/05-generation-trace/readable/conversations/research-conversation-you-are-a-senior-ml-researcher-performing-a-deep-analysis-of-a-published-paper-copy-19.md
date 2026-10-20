# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-28 (UTC).** ## Y

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/59298a2e-5f56-4c60-bfbd-6be00ffe6059.jsonl`
- **Structured JSON:** [`cd171f9df7b0c1807ac7.json`](../../sessions/cd/cd171f9df7b0c1807ac7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T10:37:12.452Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T10:37:12.452Z",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2026\nTrack: AI Alignment / Main Technical Track — Robustness Evaluation\n\nDirection: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated \"genuine capability\" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.\n\nSeed Papers:\n- Zawalski et al. \"CoDeC\" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation\n- Li et al. \"ATLAS\" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity\n- Hou et al. \"MaSTer\" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination\n- Zheng et al. \"ReasoningMath-Plus\" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component\n- Chen et al. \"Reasoning Models Don't Always Say What They Think\" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination\n- Xu et al. \"DCR\" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis\n- Kocetkov et al. \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches\n\nKnown Gaps:\n- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)\n- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only\n- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing\n- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives\n\nTheoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)\n- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)\n- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth\n\nQuality Self-Checks:\n- [x] Core insight: \"Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level.\"\n- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.\n- [x] Baseline fear test: A simple baseline of \"run on variants and average\" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.\n- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.\n\nAvoid:\n- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)\n- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark\n- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)\n- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead**\n\n## Paper to analyze\n\n{\n  \"title\": \"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\",\n  \"authors\": \"Huang et al.\",\n  \"venue\": \"arXiv 2025 (Princeton / Google DeepMind)\",\n  \"url\": \"https://arxiv.org/abs/2502.06453\",\n  \"why_important\": \"Targets competition-level math (hardest MATH-500 tier); introduces dual simple/hard perturbation taxonomy; identifies memorization-driven mechanical technique application\",\n  \"one_line_summary\": \"Constructs structure-preserving and structure-breaking perturbations of the hardest MATH problems, showing o1-mini drops 16.5% and models mechanically apply memorized techniques.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T10:37:12.456Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T10:37:12.456Z",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-28T10:37:12.470Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-28 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Target: AAAI 2026
Track: AI Alignment / Main Technical Track — Robustness Evaluation

Direction: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated "genuine capability" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.

Seed Papers:
- Zawalski et al. "CoDeC" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation
- Li et al. "ATLAS" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity
- Hou et al. "MaSTer" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination
- Zheng et al. "ReasoningMath-Plus" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component
- Chen et al. "Reasoning Models Don't Always Say What They Think" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination
- Xu et al. "DCR" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis
- Kocetkov et al. "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches

Known Gaps:
- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)
- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only
- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing
- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives

Theoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.

Constraints:
- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)
- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)
- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth

Quality Self-Checks:
- [x] Core insight: "Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level."
- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.
- [x] Baseline fear test: A simple baseline of "run on variants and average" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.
- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.

Avoid:
- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)
- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark
- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)
- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead**

## Paper to analyze

{
  "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
  "authors": "Huang et al.",
  "venue": "arXiv 2025 (Princeton / Google DeepMind)",
  "url": "https://arxiv.org/abs/2502.06453",
  "why_important": "Targets competition-level math (hardest MATH-500 tier); introduces dual simple/hard perturbation taxonomy; identifies memorization-driven mechanical technique application",
  "one_line_summary": "Constructs structure-preserving and structure-breaking perturbations of the hardest MATH problems, showing o1-mini drops 16.5% and models mechanically apply memorized techniques."
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
  "promptId": "29ec9519-6318-48b4-b045-a45e06ac918e",
  "type": "user",
  "uuid": "0c2f396f-aeb3-4b17-b6c5-a1470d2dedc1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T10:37:12.469Z_

```json
{
  "parentUuid": "0c2f396f-aeb3-4b17-b6c5-a1470d2dedc1",
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
  "uuid": "c457b6d1-d133-44f2-bb98-3998f153bec4",
  "timestamp": "2026-05-28T10:37:12.469Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T10:37:12.469Z_

```json
{
  "parentUuid": "c457b6d1-d133-44f2-bb98-3998f153bec4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a3bbaad7-1fd4-4d08-8d69-71ff09b515b6",
  "timestamp": "2026-05-28T10:37:12.469Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
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
  "aiTitle": "Analyze MATH-Perturb paper for research methodology",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059"
}
```

---

### Assistant

_source line 7 · 2026-05-28T10:37:15.286Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze the paper "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations" by Huang et al. from arXiv 2025. Let me fetch the paper first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3bbaad7-1fd4-4d08-8d69-71ff09b515b6",
  "isSidechain": false,
  "requestId": "req_011CbUpZ3LrFrLm7JtuMLEgX",
  "type": "assistant",
  "uuid": "a7739679-6dcf-4055-9fba-dc5cf82b48fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJ6guWbrHgPQCwrKQ1sHGa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3421,
      "cache_read_input_tokens": 11014,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 150,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3421
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

_source line 8 · 2026-05-28T10:37:15.676Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012mkwXKqVCn8eLU1hTsUkqs`</summary>

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
  "parentUuid": "a7739679-6dcf-4055-9fba-dc5cf82b48fc",
  "isSidechain": false,
  "requestId": "req_011CbUpZ3LrFrLm7JtuMLEgX",
  "type": "assistant",
  "uuid": "646e5dd0-d4c4-4852-bc1d-4f49cba74e0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJ6guWbrHgPQCwrKQ1sHGa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3421,
      "cache_read_input_tokens": 11014,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 150,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3421
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

_source line 9 · 2026-05-28T10:37:15.686Z_

<details><summary>↩ Tool result · `toolu_012mkwXKqVCn8eLU1hTsUkqs`</summary>

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
  "parentUuid": "646e5dd0-d4c4-4852-bc1d-4f49cba74e0b",
  "isSidechain": false,
  "promptId": "29ec9519-6318-48b4-b045-a45e06ac918e",
  "type": "user",
  "uuid": "74fce539-4726-4cab-83a2-046f0d97d195",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "646e5dd0-d4c4-4852-bc1d-4f49cba74e0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-28T10:37:18.005Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the full paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74fce539-4726-4cab-83a2-046f0d97d195",
  "isSidechain": false,
  "requestId": "req_011CbUpZHCHi9V9qCXRAh8Lb",
  "type": "assistant",
  "uuid": "6ce5c1f9-f33c-4a5a-af19-963b4e145bda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UBrHvR2YwKxhXLvRdmsef",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 14435,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 377,
          "cache_read_input_tokens": 14435,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 670
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

_source line 11 · 2026-05-28T10:37:19.827Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NLhbCUv2n2wmGaP9bghbn1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06453",
  "prompt": "Extract the full abstract, author list, and any other metadata visible on this arXiv page for the paper \"MATH-Perturb\". Include the full abstract text verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ce5c1f9-f33c-4a5a-af19-963b4e145bda",
  "isSidechain": false,
  "requestId": "req_011CbUpZHCHi9V9qCXRAh8Lb",
  "type": "assistant",
  "uuid": "8c46377f-0f32-42c4-a881-d82274d5fa57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UBrHvR2YwKxhXLvRdmsef",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 14435,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 377,
          "cache_read_input_tokens": 14435,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 670
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

_source line 12 · 2026-05-28T10:37:24.594Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BQmr4oUWnt1JaSN72tbeYM`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.06453v1",
  "prompt": "Extract the FULL content of this paper, including:\n1. Complete Introduction section\n2. Complete Method/Approach section (how perturbations are constructed, taxonomy of perturbation types, any formal definitions)\n3. Complete Experimental Setup (which models tested, which benchmarks, metrics)\n4. Complete Results section (all quantitative findings, tables, key numbers)\n5. Complete Discussion/Analysis sections (any analysis of WHY models fail, memorization analysis, mechanical technique application)\n6. Complete Conclusion and Limitations sections\n7. Related Work section\n\nBe as comprehensive as possible — extract all technical details, all numbers, all findings. Do NOT summarize — give me the raw content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c46377f-0f32-42c4-a881-d82274d5fa57",
  "isSidechain": false,
  "requestId": "req_011CbUpZHCHi9V9qCXRAh8Lb",
  "type": "assistant",
  "uuid": "2d5cd27d-8b62-4360-8586-a413710a4208",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UBrHvR2YwKxhXLvRdmsef",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 14435,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 377,
          "cache_read_input_tokens": 14435,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 670
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

_source line 13 · 2026-05-28T10:37:25.830Z_

<details><summary>↩ Tool result · `toolu_01NLhbCUv2n2wmGaP9bghbn1`</summary>

```text
# MATH-Perturb Paper Metadata

**Title:** MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations

**arXiv ID:** 2502.06453

**Submission Date:** February 10, 2025 (v1); February 12, 2025 (v2)

**Category:** Computer Science - Machine Learning (cs.LG); also classified under cs.AI and cs.CL

**Authors (18 total):** Kaixuan Huang, Jiacheng Guo, Zihao Li, Xiang Ji, Jiawei Ge, Wenzhe Li, Yingqing Guo, Tianle Cai, Hui Yuan, Runzhe Wang, Yue Wu, Ming Yin, Shange Tang, Yangsibo Huang, Chi Jin, Xinyun Chen, Chiyuan Zhang, and Mengdi Wang

**Abstract:**

The researchers developed two benchmarks by modifying challenging math problems from the MATH dataset. They created datasets where "simple perturbations" preserve original solution approaches and "hard perturbations" fundamentally alter problem structures requiring new solution methods. Testing across models including o1-mini and gemini-2.0-flash-thinking revealed significant performance degradation on hard variants. The study highlights a concerning pattern: "models blindly apply learned problem-solving skills without assessing their applicability to modified contexts." This tendency intensifies when original problems serve as in-context examples. The authors advocate for developing more robust reasoning systems that better generalize beyond learned patterns.

**License:** CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c46377f-0f32-42c4-a881-d82274d5fa57",
  "isSidechain": false,
  "promptId": "29ec9519-6318-48b4-b045-a45e06ac918e",
  "type": "user",
  "uuid": "4ad16903-f443-427a-8236-54383be287bb",
  "toolUseResult": {
    "bytes": 50270,
    "code": 200,
    "codeText": "OK",
    "result": "# MATH-Perturb Paper Metadata\n\n**Title:** MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\n\n**arXiv ID:** 2502.06453\n\n**Submission Date:** February 10, 2025 (v1); February 12, 2025 (v2)\n\n**Category:** Computer Science - Machine Learning (cs.LG); also classified under cs.AI and cs.CL\n\n**Authors (18 total):** Kaixuan Huang, Jiacheng Guo, Zihao Li, Xiang Ji, Jiawei Ge, Wenzhe Li, Yingqing Guo, Tianle Cai, Hui Yuan, Runzhe Wang, Yue Wu, Ming Yin, Shange Tang, Yangsibo Huang, Chi Jin, Xinyun Chen, Chiyuan Zhang, and Mengdi Wang\n\n**Abstract:**\n\nThe researchers developed two benchmarks by modifying challenging math problems from the MATH dataset. They created datasets where \"simple perturbations\" preserve original solution approaches and \"hard perturbations\" fundamentally alter problem structures requiring new solution methods. Testing across models including o1-mini and gemini-2.0-flash-thinking revealed significant performance degradation on hard variants. The study highlights a concerning pattern: \"models blindly apply learned problem-solving skills without assessing their applicability to modified contexts.\" This tendency intensifies when original problems serve as in-context examples. The authors advocate for developing more robust reasoning systems that better generalize beyond learned patterns.\n\n**License:** CC BY 4.0",
    "durationMs": 5998,
    "url": "https://arxiv.org/abs/2502.06453"
  },
  "sourceToolAssistantUUID": "8c46377f-0f32-42c4-a881-d82274d5fa57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "4ad16903-f443-427a-8236-54383be287bb",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MATH-Perturb paper for research methodology",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059"
}
```

---

### Tool result

_source line 16 · 2026-05-28T10:37:57.295Z_

<details><summary>↩ Tool result · `toolu_01BQmr4oUWnt1JaSN72tbeYM`</summary>

```text
# MATH-Perturb: Comprehensive Paper Content Extraction

## 1. INTRODUCTION

The paper investigates whether large language models achieve high performance on mathematical reasoning tasks through genuine understanding or memorization. While prior work examined "simple perturbations" (modifications preserving original solution paths), this work introduces "hard perturbations" that fundamentally alter problem-solving approaches.

**Key distinction**: "Simple perturbations" modify non-essential parameters while "hard perturbations" change problem formulations so original solution methods no longer apply, requiring deeper mathematical understanding.

**Main contributions**:
- Construction of MATH-P-Simple (279 problems with simple perturbations) and MATH-P-Hard (279 problems with hard perturbations) from level-5 MATH dataset problems
- Benchmarking 18 LLMs showing 10-25% performance drops on MATH-P-Hard
- Identification of "a new form of memorization where the model memorizes problem-solving techniques from the training set and blindly applies them without judging whether the modified settings are still suitable"
- Analysis showing in-context learning with original examples may hurt performance on hard perturbations

## 2. DATASET CURATION

**Origin**: Level-5 (hardest) problems from the MATH benchmark, with 164 examples from train split and 115 from test split.

**Annotation criteria**:
- MATH-P-Simple: Non-essential modifications ensuring problems solvable using original methods
- MATH-P-Hard: Fundamental modifications requiring different problem-solving approaches
- Minimal edits requirement to test generalization
- Changed answers guarantee to prevent pattern recognition

**Quality control**: 12 PhD-level annotators with strong mathematical backgrounds performed double-checking and cross-validation. "All the annotators hold a bachelor's degree in mathematics, have done researches in theoretical machine learning, and/or competed in mathematical competitions during high school."

**Perturbation strategies**:
- MATH-P-Simple: Primarily numerical modifications; also includes asking for different quantities, adding/removing non-essential constraints
- MATH-P-Hard: Increasing complexity of mathematical objects, raising polynomial degrees, altering key numbers to make brute-force infeasible, relaxing constraints to cover general cases, changing essential conditions to eliminate simplifying properties

**Similarity metrics**: Mean Reciprocal Ranks of 0.995 (MATH-P-Simple) and 0.986 (MATH-P-Hard) indicate high semantic similarity to original problems via typical retrieval methods.

## 3. EXPERIMENTAL SETUP

**Models evaluated (18 total)**:
- Long-CoT models: o1-preview, o1-mini, Gemini 2.0 flash thinking
- Closed-source models: GPT-4o, GPT-4 Turbo, Gemini 1.5 Pro, Gemini 2.0 flash, Claude 3.5 Sonnet, Claude 3 Opus
- Open-source general: Llama 3.1-8B-Instruct, Gemma 2-9b-it, Phi-3.5-mini-instruct
- Math-specific: MetaMath, MAmmoTH2, Deepseek-Math, Qwen2.5-Math, NuminaMath, Mathstral

**Evaluation setting**: Zero-shot chain-of-thought prompting (no tool usage or code interpreter access). Answer equivalence checked via string normalization and sympy package for mathematical object verification.

**Metrics**: Accuracy percentages reported separately for all problems, train-split-origin problems, and test-split-origin problems.

## 4. RESULTS

### 4.1 Benchmarking Performance

**Key findings from Table 1**:
- **Gemini-2.0-flash-thinking-exp**: 92.47% (Original) → 91.04% (MATH-P-Simple) → 78.14% (MATH-P-Hard), representing 16.49% drop
- **o1-mini**: 94.27% → 94.98% → 78.49% (16.49% drop on hard perturbations)
- **Gemini-2.0-flash-exp**: 88.17% → 82.80% → 67.03% (20.30% drop)
- **Claude-3.5-Sonnet**: 64.52% → 58.42% → 38.71% (25.81% drop)
- **GPT-4o**: 67.03% → 62.01% → 39.43% (27.60% drop)

Train vs. test split analysis shows performance drops primarily from train split, suggesting "generalization errors still exist for the state-of-the-art models even when the test examples follow the exact same reasoning patterns as the training problems."

### 4.2 Failure Mode Analysis

**Identified memorization patterns** (beyond naive verbatim recitation):
1. **Assumption ignorance**: Models fail to recognize modified assumptions and presume original assumptions still hold (exemplified in Figure 5 with consecutive seat selection problem)
2. **Blind technique application**: Models apply learned problem-solving techniques without first determining suitability (Figure 1 example with GPT-4o)
3. **Answer memorization**: Models output desired outcomes from original problems rather than modified problems (Figure 6 with o1-mini, outputting "all integer values" instead of "smallest integer value")

**Memorization percentages** (via manual inspection of 20 error cases):
- o1-mini: 40% of errors
- Claude-3.5-Sonnet: 25% of errors

**Case categorization** (Table 4):
- Case I (at least one easier variant correct + hard variant correct): 75.99% (Gemini-2.0-flash-thinking-exp) to 2.15% (MetaMath-13B)
- Case II (both variants incorrect + hard variant incorrect): 1.79% to 72.04%
- Case III (both variants incorrect but hard variant correct): <10% across all models
- Case IV (at least one easier correct but hard variant incorrect): 20.07% to 47.67%

### 4.3 Mode Collapse Analysis

**Finding**: "Naive recitation of the training material is not the major reason for producing the same answers." 

Table 5 shows percentage of errors where final answer matches original problem answer:
- MATH-P-Hard nsame < 10% of total errors (except Gemini-2.0-flash-thinking-exp at 16.39%, o1-mini at 15.00%, Gemini-2.0-flash-exp at 14.13%)
- Only 1 case (gemma-2-9b-it) showed identical output collapse in superficial text form
- Responses instead collapse "in more subtle manners, e.g. ignoring or failing to understand the modified assumptions"

### 4.4 In-Context Learning Effects

**MATH-P-Simple results** (Table 6): "Using the original (problem, solution) pair as a one-shot in-context demonstration boosts the performance of nearly all the models"
- o1-mini: 94.98% (zero-shot) → 94.98% (with ICL)
- Claude-3.5-Sonnet: 58.42% → 83.15%
- GPT-4o: 62.01% → 77.06%

**MATH-P-Hard results**: Two competing effects identified:
1. **ICL effect**: Original solutions supply helpful mathematical knowledge
2. **Misleading effect**: Models fail to recognize subtle differences and get misled by demonstrations

**Effect magnitudes** (Table 7):
- n(correct→wrong) percentages: 7.23%-40% (higher for larger models)
- n(wrong→correct) percentages: 1.90%-33.77%
- Overall result: "only marginal improvements (less than 5%) on the MATH-P-Hard for most models"

**Examples of misleading**:
- o1-mini: 40% of problems shift from correct to wrong with ICL
- Claude-3.5-Sonnet: 19.15% shift from correct to wrong

**Ablation comparison** (Table 8): ICL with original problems consistently outperforms ICL with random examples across both MATH-P-Simple and MATH-P-Hard, except one case (MetaMath-13B-V1.0 on MATH-P-Hard: 3.58% vs 5.38%).

### 4.5 Inference-Time Scaling (Section C.5)

Pass@k evaluation with N=8 for o1-mini and N=64 for smaller models:
- **o1-mini on Original**: Pass@1 94.27% → Pass@8 97.49%
- **o1-mini on MATH-P-Hard**: Pass@1 78.49% → Pass@8 85.66%
- **Llama-3.1-8B on MATH-P-Hard**: Pass@1 10.04% → Pass@64 23.66%
- Self-consistency (majority voting) provides modest improvements but doesn't close performance gaps

## 5. DISCUSSION & ANALYSIS

**Robustness progress**: "We did not observe such huge gaps for the models we evaluate" compared to Srivastava et al.'s 58-80% drop between modified and original MATH benchmarks, suggesting "progress in the robustness of the newly developed models against simple perturbations."

**Memorization as bottleneck**: "As the capabilities of language models continue to advance and the average-case performance continue to improve, the generalization abilities against hard perturbations may soon become the primary bottleneck in their real-world usages."

**ICL implications**: "Any naive fine-tuning technique with a limited distribution of problem settings will hurt the generalization of the language models against hard perturbations."

## 6. RELATED WORK

**Perturbation benchmarks**: GSM-IC, GSM-Plus, GSM-Symbolic, Functional-MATH, Putnam-AXIOM all focus on simple perturbations. This work distinguishes itself by requiring different solving strategies.

**Memorization literature**: Prior work examined verbatim memorization; this work identifies "subtle forms of memorization beyond naive verbatim memorization" through counterfactual testing.

**Comparison with MATH2**: Shah et al. created MATH2 by combining random pairs of skills, but lacks natural "original problem" references for investigating memorization effects.

## 7. CONCLUSION

The paper calls for research addressing hard perturbation generalization as "critical for advancing the robustness and reliability of future LLMs." Main findings: all models show 10-25% performance degradation on MATH-P-Hard, errors trace to subtle memorization forms where models blindly apply learned techniques, and in-context learning with original examples exacerbates problems by creating misleading effects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d5cd27d-8b62-4360-8586-a413710a4208",
  "isSidechain": false,
  "promptId": "29ec9519-6318-48b4-b045-a45e06ac918e",
  "type": "user",
  "uuid": "ece0f9ce-df0c-4222-aa69-6fbeeb6011e3",
  "toolUseResult": {
    "bytes": 366995,
    "code": 200,
    "codeText": "OK",
    "result": "# MATH-Perturb: Comprehensive Paper Content Extraction\n\n## 1. INTRODUCTION\n\nThe paper investigates whether large language models achieve high performance on mathematical reasoning tasks through genuine understanding or memorization. While prior work examined \"simple perturbations\" (modifications preserving original solution paths), this work introduces \"hard perturbations\" that fundamentally alter problem-solving approaches.\n\n**Key distinction**: \"Simple perturbations\" modify non-essential parameters while \"hard perturbations\" change problem formulations so original solution methods no longer apply, requiring deeper mathematical understanding.\n\n**Main contributions**:\n- Construction of MATH-P-Simple (279 problems with simple perturbations) and MATH-P-Hard (279 problems with hard perturbations) from level-5 MATH dataset problems\n- Benchmarking 18 LLMs showing 10-25% performance drops on MATH-P-Hard\n- Identification of \"a new form of memorization where the model memorizes problem-solving techniques from the training set and blindly applies them without judging whether the modified settings are still suitable\"\n- Analysis showing in-context learning with original examples may hurt performance on hard perturbations\n\n## 2. DATASET CURATION\n\n**Origin**: Level-5 (hardest) problems from the MATH benchmark, with 164 examples from train split and 115 from test split.\n\n**Annotation criteria**:\n- MATH-P-Simple: Non-essential modifications ensuring problems solvable using original methods\n- MATH-P-Hard: Fundamental modifications requiring different problem-solving approaches\n- Minimal edits requirement to test generalization\n- Changed answers guarantee to prevent pattern recognition\n\n**Quality control**: 12 PhD-level annotators with strong mathematical backgrounds performed double-checking and cross-validation. \"All the annotators hold a bachelor's degree in mathematics, have done researches in theoretical machine learning, and/or competed in mathematical competitions during high school.\"\n\n**Perturbation strategies**:\n- MATH-P-Simple: Primarily numerical modifications; also includes asking for different quantities, adding/removing non-essential constraints\n- MATH-P-Hard: Increasing complexity of mathematical objects, raising polynomial degrees, altering key numbers to make brute-force infeasible, relaxing constraints to cover general cases, changing essential conditions to eliminate simplifying properties\n\n**Similarity metrics**: Mean Reciprocal Ranks of 0.995 (MATH-P-Simple) and 0.986 (MATH-P-Hard) indicate high semantic similarity to original problems via typical retrieval methods.\n\n## 3. EXPERIMENTAL SETUP\n\n**Models evaluated (18 total)**:\n- Long-CoT models: o1-preview, o1-mini, Gemini 2.0 flash thinking\n- Closed-source models: GPT-4o, GPT-4 Turbo, Gemini 1.5 Pro, Gemini 2.0 flash, Claude 3.5 Sonnet, Claude 3 Opus\n- Open-source general: Llama 3.1-8B-Instruct, Gemma 2-9b-it, Phi-3.5-mini-instruct\n- Math-specific: MetaMath, MAmmoTH2, Deepseek-Math, Qwen2.5-Math, NuminaMath, Mathstral\n\n**Evaluation setting**: Zero-shot chain-of-thought prompting (no tool usage or code interpreter access). Answer equivalence checked via string normalization and sympy package for mathematical object verification.\n\n**Metrics**: Accuracy percentages reported separately for all problems, train-split-origin problems, and test-split-origin problems.\n\n## 4. RESULTS\n\n### 4.1 Benchmarking Performance\n\n**Key findings from Table 1**:\n- **Gemini-2.0-flash-thinking-exp**: 92.47% (Original) → 91.04% (MATH-P-Simple) → 78.14% (MATH-P-Hard), representing 16.49% drop\n- **o1-mini**: 94.27% → 94.98% → 78.49% (16.49% drop on hard perturbations)\n- **Gemini-2.0-flash-exp**: 88.17% → 82.80% → 67.03% (20.30% drop)\n- **Claude-3.5-Sonnet**: 64.52% → 58.42% → 38.71% (25.81% drop)\n- **GPT-4o**: 67.03% → 62.01% → 39.43% (27.60% drop)\n\nTrain vs. test split analysis shows performance drops primarily from train split, suggesting \"generalization errors still exist for the state-of-the-art models even when the test examples follow the exact same reasoning patterns as the training problems.\"\n\n### 4.2 Failure Mode Analysis\n\n**Identified memorization patterns** (beyond naive verbatim recitation):\n1. **Assumption ignorance**: Models fail to recognize modified assumptions and presume original assumptions still hold (exemplified in Figure 5 with consecutive seat selection problem)\n2. **Blind technique application**: Models apply learned problem-solving techniques without first determining suitability (Figure 1 example with GPT-4o)\n3. **Answer memorization**: Models output desired outcomes from original problems rather than modified problems (Figure 6 with o1-mini, outputting \"all integer values\" instead of \"smallest integer value\")\n\n**Memorization percentages** (via manual inspection of 20 error cases):\n- o1-mini: 40% of errors\n- Claude-3.5-Sonnet: 25% of errors\n\n**Case categorization** (Table 4):\n- Case I (at least one easier variant correct + hard variant correct): 75.99% (Gemini-2.0-flash-thinking-exp) to 2.15% (MetaMath-13B)\n- Case II (both variants incorrect + hard variant incorrect): 1.79% to 72.04%\n- Case III (both variants incorrect but hard variant correct): <10% across all models\n- Case IV (at least one easier correct but hard variant incorrect): 20.07% to 47.67%\n\n### 4.3 Mode Collapse Analysis\n\n**Finding**: \"Naive recitation of the training material is not the major reason for producing the same answers.\" \n\nTable 5 shows percentage of errors where final answer matches original problem answer:\n- MATH-P-Hard nsame < 10% of total errors (except Gemini-2.0-flash-thinking-exp at 16.39%, o1-mini at 15.00%, Gemini-2.0-flash-exp at 14.13%)\n- Only 1 case (gemma-2-9b-it) showed identical output collapse in superficial text form\n- Responses instead collapse \"in more subtle manners, e.g. ignoring or failing to understand the modified assumptions\"\n\n### 4.4 In-Context Learning Effects\n\n**MATH-P-Simple results** (Table 6): \"Using the original (problem, solution) pair as a one-shot in-context demonstration boosts the performance of nearly all the models\"\n- o1-mini: 94.98% (zero-shot) → 94.98% (with ICL)\n- Claude-3.5-Sonnet: 58.42% → 83.15%\n- GPT-4o: 62.01% → 77.06%\n\n**MATH-P-Hard results**: Two competing effects identified:\n1. **ICL effect**: Original solutions supply helpful mathematical knowledge\n2. **Misleading effect**: Models fail to recognize subtle differences and get misled by demonstrations\n\n**Effect magnitudes** (Table 7):\n- n(correct→wrong) percentages: 7.23%-40% (higher for larger models)\n- n(wrong→correct) percentages: 1.90%-33.77%\n- Overall result: \"only marginal improvements (less than 5%) on the MATH-P-Hard for most models\"\n\n**Examples of misleading**:\n- o1-mini: 40% of problems shift from correct to wrong with ICL\n- Claude-3.5-Sonnet: 19.15% shift from correct to wrong\n\n**Ablation comparison** (Table 8): ICL with original problems consistently outperforms ICL with random examples across both MATH-P-Simple and MATH-P-Hard, except one case (MetaMath-13B-V1.0 on MATH-P-Hard: 3.58% vs 5.38%).\n\n### 4.5 Inference-Time Scaling (Section C.5)\n\nPass@k evaluation with N=8 for o1-mini and N=64 for smaller models:\n- **o1-mini on Original**: Pass@1 94.27% → Pass@8 97.49%\n- **o1-mini on MATH-P-Hard**: Pass@1 78.49% → Pass@8 85.66%\n- **Llama-3.1-8B on MATH-P-Hard**: Pass@1 10.04% → Pass@64 23.66%\n- Self-consistency (majority voting) provides modest improvements but doesn't close performance gaps\n\n## 5. DISCUSSION & ANALYSIS\n\n**Robustness progress**: \"We did not observe such huge gaps for the models we evaluate\" compared to Srivastava et al.'s 58-80% drop between modified and original MATH benchmarks, suggesting \"progress in the robustness of the newly developed models against simple perturbations.\"\n\n**Memorization as bottleneck**: \"As the capabilities of language models continue to advance and the average-case performance continue to improve, the generalization abilities against hard perturbations may soon become the primary bottleneck in their real-world usages.\"\n\n**ICL implications**: \"Any naive fine-tuning technique with a limited distribution of problem settings will hurt the generalization of the language models against hard perturbations.\"\n\n## 6. RELATED WORK\n\n**Perturbation benchmarks**: GSM-IC, GSM-Plus, GSM-Symbolic, Functional-MATH, Putnam-AXIOM all focus on simple perturbations. This work distinguishes itself by requiring different solving strategies.\n\n**Memorization literature**: Prior work examined verbatim memorization; this work identifies \"subtle forms of memorization beyond naive verbatim memorization\" through counterfactual testing.\n\n**Comparison with MATH2**: Shah et al. created MATH2 by combining random pairs of skills, but lacks natural \"original problem\" references for investigating memorization effects.\n\n## 7. CONCLUSION\n\nThe paper calls for research addressing hard perturbation generalization as \"critical for advancing the robustness and reliability of future LLMs.\" Main findings: all models show 10-25% performance degradation on MATH-P-Hard, errors trace to subtle memorization forms where models blindly apply learned techniques, and in-context learning with original examples exacerbates problems by creating misleading effects.",
    "durationMs": 32694,
    "url": "https://arxiv.org/html/2502.06453v1"
  },
  "sourceToolAssistantUUID": "2d5cd27d-8b62-4360-8586-a413710a4208",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-28T10:38:04.878Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me check if this paper is on OpenReview (it might have been submitted to a venue with OpenReview reviews). Let me also try to get more details about the methodology - specifically the perturbation taxonomy and formal definitions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ece0f9ce-df0c-4222-aa69-6fbeeb6011e3",
  "isSidechain": false,
  "requestId": "req_011CbUpcLqeUWKQhca62nH46",
  "type": "assistant",
  "uuid": "8267d6cd-d921-4bd9-8ca6-3bda4ca1893e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017UKsck6tKTEapov6KAixKU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 15105,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3376,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 485,
          "cache_read_input_tokens": 15105,
          "cache_creation_input_tokens": 3376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3376
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

_source line 18 · 2026-05-28T10:38:05.876Z_

Let me also check for any OpenReview submissions and get more details on the perturbation methodology:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8267d6cd-d921-4bd9-8ca6-3bda4ca1893e",
  "isSidechain": false,
  "requestId": "req_011CbUpcLqeUWKQhca62nH46",
  "type": "assistant",
  "uuid": "3691ddbe-c23e-463c-9134-8b979213f332",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017UKsck6tKTEapov6KAixKU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 15105,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3376,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 485,
          "cache_read_input_tokens": 15105,
          "cache_creation_input_tokens": 3376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3376
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

_source line 19 · 2026-05-28T10:38:08.706Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018Pf47McAASGzxV1BFmBRdR`</summary>

```json
{
  "url": "https://openreview.net/search?term=MATH-Perturb+Benchmarking+LLMs+Math+Reasoning+Hard+Perturbations",
  "prompt": "Find the OpenReview submission for \"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\" by Huang et al. Extract the submission URL, venue, reviewer scores, and any reviewer comments or author responses. If the paper is not found, say so."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3691ddbe-c23e-463c-9134-8b979213f332",
  "isSidechain": false,
  "requestId": "req_011CbUpcLqeUWKQhca62nH46",
  "type": "assistant",
  "uuid": "50a54385-25af-4a23-a3ad-69321229cd56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017UKsck6tKTEapov6KAixKU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 15105,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3376,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 485,
          "cache_read_input_tokens": 15105,
          "cache_creation_input_tokens": 3376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3376
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

_source line 20 · 2026-05-28T10:38:11.035Z_

<details><summary>↩ Tool result · `toolu_018Pf47McAASGzxV1BFmBRdR`</summary>

```text
I cannot find the OpenReview submission for "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations" by Huang et al. in the provided web page content.

The content shown is only the OpenReview.net homepage with navigation menus, footer information, and general site descriptions. It does not contain any specific paper submissions, URLs, venue information, reviewer scores, or comments related to the paper you're asking about.

To locate this paper, you would need to visit OpenReview.net directly and use their search functionality or browse the relevant venue/conference listings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50a54385-25af-4a23-a3ad-69321229cd56",
  "isSidechain": false,
  "promptId": "29ec9519-6318-48b4-b045-a45e06ac918e",
  "type": "user",
  "uuid": "46bbc79c-6d04-417d-8726-9ff999e8b83c",
  "toolUseResult": {
    "bytes": 62395,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find the OpenReview submission for \"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\" by Huang et al. in the provided web page content.\n\nThe content shown is only the OpenReview.net homepage with navigation menus, footer information, and general site descriptions. It does not contain any specific paper submissions, URLs, venue information, reviewer scores, or comments related to the paper you're asking about.\n\nTo locate this paper, you would need to visit OpenReview.net directly and use their search functionality or browse the relevant venue/conference listings.",
    "durationMs": 2324,
    "url": "https://openreview.net/search?term=MATH-Perturb+Benchmarking+LLMs+Math+Reasoning+Hard+Perturbations"
  },
  "sourceToolAssistantUUID": "50a54385-25af-4a23-a3ad-69321229cd56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T10:38:12.859Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013zoXpdeqCKENbBtYLJTpFf`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.06453v1",
  "prompt": "Focus specifically on extracting:\n1. The EXACT perturbation strategies for MATH-P-Hard — what are all the specific types of hard perturbations? Give examples.\n2. Any formal or mathematical definitions of what makes a perturbation \"hard\" vs \"simple\"\n3. The quality control / validation process — how did they verify correctness of perturbations?\n4. Any details about the symbolic/automated vs manual process of creating perturbations\n5. The limitations section — what did the authors acknowledge as weaknesses?\n6. Any details about how they measured or defined \"memorization\" vs \"genuine reasoning\"\n7. The MRR similarity analysis — exact numbers and what retrieval model was used"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46bbc79c-6d04-417d-8726-9ff999e8b83c",
  "isSidechain": false,
  "requestId": "req_011CbUpcLqeUWKQhca62nH46",
  "type": "assistant",
  "uuid": "c3c0afc4-2fc4-4177-acdc-3980b60da3fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017UKsck6tKTEapov6KAixKU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 15105,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3376,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 485,
          "cache_read_input_tokens": 15105,
          "cache_creation_input_tokens": 3376,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3376
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

_source line 22 · 2026-05-28T10:38:26.135Z_

<details><summary>↩ Tool result · `toolu_013zoXpdeqCKENbBtYLJTpFf`</summary>

```text
# MATH-Perturb: Key Extraction Summary

## 1. Hard Perturbation Strategies

The paper identifies several specific strategies for MATH-P-Hard modifications:

**Explicit strategies mentioned:**
- "Increasing the complexity of the mathematical objects involved. For example, raising the degrees of polynomials will make them harder to solve or factorize"
- "Altering key numbers to large values can make brute-force solutions infeasible"
- "Relaxing constraints to cover more general cases"
- "Changing essential conditions so the original simplifying properties (e.g. symmetry, reducibility, linearity) no longer hold"

The fundamental distinction: hard perturbations "change the problem formulations fundamentally so that the original solution paths are no longer applicable."

## 2. Formal Definition: Hard vs. Simple

**Simple Perturbation:** "Non-essential modifications to the problem, ensuring that the modified problem can be solved using the same method as the original problem"

**Hard Perturbation:** "Small but fundamental modifications to the problem so that the modified problem cannot be solved using the same method as the original problem. Instead, it requires deeper math understanding and harder problem-solving skills"

Both require "Minimal Edits" and "Changed Answers" to ensure modifications don't allow pattern recognition.

## 3. Quality Control Process

The validation involved:
- 12 PhD-level annotators with strong mathematics backgrounds
- All held bachelor's degrees in mathematics and had competition/research experience
- "All the annotators are required to double-check their annotations"
- "Each modified problem is also cross-validated by an independent annotator to make sure the answer is correct"
- "Manually went through all the problems where the o1-mini's answer and the annotated answer differ and confirmed that the annotated answers are correct"

## 4. Perturbation Creation: Manual vs. Automated

The process was entirely **manual**. The paper states annotators "make as minimal modifications as possible" with specific requirements, but provides no algorithmic framework—only human expert judgment guided by rubrics.

## 5. Acknowledged Limitations

The paper does not contain an explicit limitations section. However, potential weaknesses are implied:

- The dataset comprises only 279 problems from MATH's hardest tier (level-5)
- Perturbation quality depends on subjective expert judgment
- The "misalignment between the models' capabilities and the annotators' perception of the difficulties" exists (mentioned in Appendix C.1)
- Authors note they did not evaluate with tool access, which "many problems can be trivially solved by writing a brute-force search program"

## 6. Memorization Definition & Measurement

The authors identify "a novel form of memorization" distinct from verbatim recitation:

Models exhibit memorization when they "memorize the problem-solving techniques from the training set and blindly apply them without judging whether the modified settings are still suitable." Specific manifestations include:

- Ignoring modified assumptions and assuming original conditions still apply
- Blindly applying techniques without assessing applicability (Figure 1 example)
- Outputting the original problem's answer instead of solving the modified version

Measurement: Manual inspection of error cases. For example: "we estimate the percentages of errors caused by memorization to be 40% for o1-mini and 25% for Claude-3.5-Sonnet, via manual inspections of 20 error cases."

The authors distinguish this from "genuine reasoning" through case analysis: Case IV (solves original/simple but fails hard) represents memorization failures.

## 7. MRR Similarity Analysis

**Exact metrics:**
- MATH-P-Simple MRR: 0.995
- MATH-P-Hard MRR: 0.986

**Retrieval model:** "OpenAI's text-embedding-3-large embedding model" with "cosine similarities of embeddings being the ranking method"

**Interpretation:** These high MRRs indicate "the corresponding original problem and solution are likely to be retrieved using typical semantic-based retrieval methods," suggesting hard perturbations remain textually similar despite requiring different solution approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3c0afc4-2fc4-4177-acdc-3980b60da3fe",
  "isSidechain": false,
  "promptId": "29ec9519-6318-48b4-b045-a45e06ac918e",
  "type": "user",
  "uuid": "4cd14090-b8c4-4420-975f-66f41dd5735f",
  "toolUseResult": {
    "bytes": 366995,
    "code": 200,
    "codeText": "OK",
    "result": "# MATH-Perturb: Key Extraction Summary\n\n## 1. Hard Perturbation Strategies\n\nThe paper identifies several specific strategies for MATH-P-Hard modifications:\n\n**Explicit strategies mentioned:**\n- \"Increasing the complexity of the mathematical objects involved. For example, raising the degrees of polynomials will make them harder to solve or factorize\"\n- \"Altering key numbers to large values can make brute-force solutions infeasible\"\n- \"Relaxing constraints to cover more general cases\"\n- \"Changing essential conditions so the original simplifying properties (e.g. symmetry, reducibility, linearity) no longer hold\"\n\nThe fundamental distinction: hard perturbations \"change the problem formulations fundamentally so that the original solution paths are no longer applicable.\"\n\n## 2. Formal Definition: Hard vs. Simple\n\n**Simple Perturbation:** \"Non-essential modifications to the problem, ensuring that the modified problem can be solved using the same method as the original problem\"\n\n**Hard Perturbation:** \"Small but fundamental modifications to the problem so that the modified problem cannot be solved using the same method as the original problem. Instead, it requires deeper math understanding and harder problem-solving skills\"\n\nBoth require \"Minimal Edits\" and \"Changed Answers\" to ensure modifications don't allow pattern recognition.\n\n## 3. Quality Control Process\n\nThe validation involved:\n- 12 PhD-level annotators with strong mathematics backgrounds\n- All held bachelor's degrees in mathematics and had competition/research experience\n- \"All the annotators are required to double-check their annotations\"\n- \"Each modified problem is also cross-validated by an independent annotator to make sure the answer is correct\"\n- \"Manually went through all the problems where the o1-mini's answer and the annotated answer differ and confirmed that the annotated answers are correct\"\n\n## 4. Perturbation Creation: Manual vs. Automated\n\nThe process was entirely **manual**. The paper states annotators \"make as minimal modifications as possible\" with specific requirements, but provides no algorithmic framework—only human expert judgment guided by rubrics.\n\n## 5. Acknowledged Limitations\n\nThe paper does not contain an explicit limitations section. However, potential weaknesses are implied:\n\n- The dataset comprises only 279 problems from MATH's hardest tier (level-5)\n- Perturbation quality depends on subjective expert judgment\n- The \"misalignment between the models' capabilities and the annotators' perception of the difficulties\" exists (mentioned in Appendix C.1)\n- Authors note they did not evaluate with tool access, which \"many problems can be trivially solved by writing a brute-force search program\"\n\n## 6. Memorization Definition & Measurement\n\nThe authors identify \"a novel form of memorization\" distinct from verbatim recitation:\n\nModels exhibit memorization when they \"memorize the problem-solving techniques from the training set and blindly apply them without judging whether the modified settings are still suitable.\" Specific manifestations include:\n\n- Ignoring modified assumptions and assuming original conditions still apply\n- Blindly applying techniques without assessing applicability (Figure 1 example)\n- Outputting the original problem's answer instead of solving the modified version\n\nMeasurement: Manual inspection of error cases. For example: \"we estimate the percentages of errors caused by memorization to be 40% for o1-mini and 25% for Claude-3.5-Sonnet, via manual inspections of 20 error cases.\"\n\nThe authors distinguish this from \"genuine reasoning\" through case analysis: Case IV (solves original/simple but fails hard) represents memorization failures.\n\n## 7. MRR Similarity Analysis\n\n**Exact metrics:**\n- MATH-P-Simple MRR: 0.995\n- MATH-P-Hard MRR: 0.986\n\n**Retrieval model:** \"OpenAI's text-embedding-3-large embedding model\" with \"cosine similarities of embeddings being the ranking method\"\n\n**Interpretation:** These high MRRs indicate \"the corresponding original problem and solution are likely to be retrieved using typical semantic-based retrieval methods,\" suggesting hard perturbations remain textually similar despite requiring different solution approaches.",
    "durationMs": 13271,
    "url": "https://arxiv.org/html/2502.06453v1"
  },
  "sourceToolAssistantUUID": "c3c0afc4-2fc4-4177-acdc-3980b60da3fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "4cd14090-b8c4-4420-975f-66f41dd5735f",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MATH-Perturb paper for research methodology",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059"
}
```

---

### Assistant

_source line 25 · 2026-05-28T10:38:29.279Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper. Let me also check if it was submitted to any conference via OpenReview - maybe ICML 2025 or similar.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cd14090-b8c4-4420-975f-66f41dd5735f",
  "isSidechain": false,
  "requestId": "req_011CbUpeUBECwRYsBcYj4ou5",
  "type": "assistant",
  "uuid": "3faa7f93-b370-4a1e-9e7e-9aa2c65e2d1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q29NaEqCpoxKhTvedNe3L2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1622,
      "cache_read_input_tokens": 18481,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 18481,
          "cache_creation_input_tokens": 1622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1622
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

_source line 26 · 2026-05-28T10:38:31.281Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0135Rj8NEykFU6ijkYVkZx6y`</summary>

```json
{
  "url": "https://openreview.net/search?term=MATH-Perturb+Huang+perturbations",
  "prompt": "Search for the paper \"MATH-Perturb\" by Huang et al. Is there any OpenReview submission? If so, extract the URL, venue, reviewer scores, and reviewer comments. If not found, state that clearly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3faa7f93-b370-4a1e-9e7e-9aa2c65e2d1d",
  "isSidechain": false,
  "requestId": "req_011CbUpeUBECwRYsBcYj4ou5",
  "type": "assistant",
  "uuid": "b3b8ac8d-09df-447e-a603-51b694d9d2be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q29NaEqCpoxKhTvedNe3L2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1622,
      "cache_read_input_tokens": 18481,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 18481,
          "cache_creation_input_tokens": 1622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1622
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

_source line 27 · 2026-05-28T10:38:33.280Z_

<details><summary>↩ Tool result · `toolu_0135Rj8NEykFU6ijkYVkZx6y`</summary>

```text
Based on the web page content provided, I cannot find any information about a paper titled "MATH-Perturb" by Huang et al. or any OpenReview submission details.

The content shown is only the header, navigation menu, and footer of the OpenReview.net homepage. It does not contain search results, paper metadata, venue information, reviewer scores, or reviewer comments that would be necessary to answer your query.

To locate this paper, you would need to use OpenReview's search functionality directly on their website.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3b8ac8d-09df-447e-a603-51b694d9d2be",
  "isSidechain": false,
  "promptId": "29ec9519-6318-48b4-b045-a45e06ac918e",
  "type": "user",
  "uuid": "c4d45954-8edd-41a9-8608-e1d812aa2440",
  "toolUseResult": {
    "bytes": 62286,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find any information about a paper titled \"MATH-Perturb\" by Huang et al. or any OpenReview submission details.\n\nThe content shown is only the header, navigation menu, and footer of the OpenReview.net homepage. It does not contain search results, paper metadata, venue information, reviewer scores, or reviewer comments that would be necessary to answer your query.\n\nTo locate this paper, you would need to use OpenReview's search functionality directly on their website.",
    "durationMs": 1994,
    "url": "https://openreview.net/search?term=MATH-Perturb+Huang+perturbations"
  },
  "sourceToolAssistantUUID": "b3b8ac8d-09df-447e-a603-51b694d9d2be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-28T10:38:35.305Z_

<details><summary>Logged reasoning block</summary>

```text
The paper doesn't seem to be on OpenReview. Let me try a different search approach to see if it was accepted at any conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4d45954-8edd-41a9-8608-e1d812aa2440",
  "isSidechain": false,
  "requestId": "req_011CbUpezeYVYPUpJP1rAPnT",
  "type": "assistant",
  "uuid": "aa4bd355-ebd2-4ba6-9b7e-ae7c4b738bf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLNtwwf4jD5F2aztdWHS5j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 20103,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 20103,
          "cache_creation_input_tokens": 321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 321
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

_source line 29 · 2026-05-28T10:38:37.700Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NjdW8WKVBKfyhW1hTsN2Yb`</summary>

```json
{
  "url": "https://scholar.google.com/scholar?q=%22MATH-Perturb%22+Huang+perturbations+LLM+math+reasoning",
  "prompt": "Find information about the paper \"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\". Was it accepted at any conference (ICML, NeurIPS, ACL, AAAI, etc.)? How many citations does it have? What venue is it associated with?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa4bd355-ebd2-4ba6-9b7e-ae7c4b738bf2",
  "isSidechain": false,
  "requestId": "req_011CbUpezeYVYPUpJP1rAPnT",
  "type": "assistant",
  "uuid": "8d4fe76c-7a01-4503-9519-31f811722048",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLNtwwf4jD5F2aztdWHS5j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 20103,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 321,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 20103,
          "cache_creation_input_tokens": 321,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 321
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

_source line 30 · 2026-05-28T10:38:43.240Z_

<details><summary>↩ Tool result · `toolu_01NjdW8WKVBKfyhW1hTsN2Yb`</summary>

```text
# MATH-Perturb Paper Information

Based on the Google Scholar search results provided, here's what I can determine about "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations":

## Conference/Venue Status
The search results don't explicitly state the original publication venue for MATH-Perturb itself. However, the paper is frequently cited in recent research (2025-2026) across multiple venues including NeurIPS workshops, arXiv preprints, and OpenReview publications.

## Citation Count
The specific citation count for the original MATH-Perturb paper is not clearly displayed in these search results. However, related papers referencing it show citation counts (for example, "MathRobust-LV" has 1 citation), indicating the benchmark has scholarly impact.

## Related Work
The benchmark appears prominently in current research on large language model robustness, with multiple 2025-2026 papers building upon or comparing against MATH-Perturb methodology, including:
- Studies on linguistic variations in mathematical reasoning
- Difficulty-evolving perturbation frameworks
- Robustness evaluations across different problem formulations

The benchmark is clearly established as a reference point in evaluating how well language models handle variations of mathematical problems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d4fe76c-7a01-4503-9519-31f811722048",
  "isSidechain": false,
  "promptId": "29ec9519-6318-48b4-b045-a45e06ac918e",
  "type": "user",
  "uuid": "ad72ad45-c934-4cb6-8fbd-efa69978b7d5",
  "toolUseResult": {
    "bytes": 173511,
    "code": 200,
    "codeText": "OK",
    "result": "# MATH-Perturb Paper Information\n\nBased on the Google Scholar search results provided, here's what I can determine about \"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\":\n\n## Conference/Venue Status\nThe search results don't explicitly state the original publication venue for MATH-Perturb itself. However, the paper is frequently cited in recent research (2025-2026) across multiple venues including NeurIPS workshops, arXiv preprints, and OpenReview publications.\n\n## Citation Count\nThe specific citation count for the original MATH-Perturb paper is not clearly displayed in these search results. However, related papers referencing it show citation counts (for example, \"MathRobust-LV\" has 1 citation), indicating the benchmark has scholarly impact.\n\n## Related Work\nThe benchmark appears prominently in current research on large language model robustness, with multiple 2025-2026 papers building upon or comparing against MATH-Perturb methodology, including:\n- Studies on linguistic variations in mathematical reasoning\n- Difficulty-evolving perturbation frameworks\n- Robustness evaluations across different problem formulations\n\nThe benchmark is clearly established as a reference point in evaluating how well language models handle variations of mathematical problems.",
    "durationMs": 5536,
    "url": "https://scholar.google.com/scholar?q=%22MATH-Perturb%22+Huang+perturbations+LLM+math+reasoning"
  },
  "sourceToolAssistantUUID": "8d4fe76c-7a01-4503-9519-31f811722048",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-28T10:39:00.300Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to do a thorough analysis. Let me construct the JSON output.

Key observations for my analysis:

1. **Problem identification**: The authors identified that existing perturbation benchmarks (GSM-Plus, GSM-Symbolic, etc.) only did "simple" perturbations that preserved solution paths. Nobody was testing whether models could handle perturbations that fundamentally changed the solution approach. This is the gap.

2. **Key insight**: There's a novel form of memorization beyond verbatim recitation — models memorize *problem-solving techniques* and blindly apply them even when conditions change. 

This becomes apparent when hard perturbations break the original solution method.

3. **Innovation type**: This is primarily a new_benchmark with a significant analysis component. The dual simple/hard perturbation taxonomy is the methodological contribution.

4. **What makes it good**: 
   - Clean experimental design with matched pairs (original → simple → hard)
   - Strong annotator quality (12 PhD-level mathematicians)
   - The MRR analysis showing perturbations are textually similar but require different solutions
   - Novel finding about mechanical technique application
   - ICL analysis revealing competing effects

5. **Limitations**:
   - Entirely manual perturbation process (279 examples)
   - No formal definition of "hard" — relies on expert judgment
   - Only level-5 MATH problems
   - Small sample for memorization analysis (20 error cases)
   - No tool-use evaluation

6. **Relevance to CRADE**: The paper demonstrates the need for adversarial variants but does it entirely manually, whereas CRADE would automate this with SymPy. Their finding about mechanical technique application is exactly the kind of memorization signal that step-level analysis would catch. They observe memorization without quantifying contamination levels, and they only evaluate at the answer level rather than examining step-by-step reasoning.

Now I'm generating the JSON output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad72ad45-c934-4cb6-8fbd-efa69978b7d5",
  "isSidechain": false,
  "requestId": "req_011CbUpfjFMyBxz5hvP54cGz",
  "type": "assistant",
  "uuid": "7e6d75a2-1ca0-4754-83b4-e2cf3559ff7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4jeGaEYvKNb1nYQg6pnBM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 528,
      "cache_read_input_tokens": 20424,
      "output_tokens": 2426,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2426,
          "cache_read_input_tokens": 20424,
          "cache_creation_input_tokens": 528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 528
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

_source line 32 · 2026-05-28T10:39:53.260Z_

Now I have comprehensive information to produce the analysis. Here is the deep analysis:

```json
{
  "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
  "venue": "arXiv 2025 (Princeton / Google DeepMind); no confirmed peer-reviewed venue acceptance found",
  "problem_identification": "Prior perturbation benchmarks (GSM-Plus, GSM-Symbolic, Functional-MATH) only tested 'simple' perturbations that preserved the original solution path — essentially asking 'can the model re-execute the same algorithm with different numbers?' The authors identified that this never tests whether a model actually UNDERSTANDS the mathematical structure, because even a memorizer with the right technique template would pass. The gap was found by observing that competition-level math problems often have 'fragile' solution paths: a small structural change (e.g., raising polynomial degree, removing a symmetry) can invalidate an entire approach, and no benchmark tested this boundary.",
  "key_insight": "There exists a previously uncharacterized form of memorization — 'mechanical technique application' — where models memorize not the answers but the problem-solving strategies themselves, and blindly apply learned techniques without verifying their applicability to modified conditions. This is revealed only by perturbations that preserve surface similarity (MRR ≈ 0.986) while invalidating the solution method, creating a clean separation between textual recognition and mathematical understanding.",
  "innovation_type": "new_benchmark",
  "method_summary": "The authors manually constructed 279 matched problem triplets from MATH level-5 (hardest tier): original → MATH-P-Simple (surface modifications preserving solution path) → MATH-P-Hard (minimal structural edits that invalidate the original solution approach, e.g., raising polynomial degree, breaking symmetry, making brute-force infeasible). Twelve PhD-level annotators with competition math backgrounds created and cross-validated all perturbations. They evaluated 18 LLMs zero-shot with chain-of-thought, analyzed four outcome cases (original-correct × hard-correct), manually inspected error traces to categorize memorization types (assumption ignorance, blind technique application, answer memorization), and ran controlled ICL experiments showing that providing original problem-solution pairs as demonstrations creates competing 'helpful knowledge' vs 'misleading template' effects on hard variants.",
  "what_makes_it_good": "The paper's strength is its clean experimental design: the simple/hard taxonomy creates a controlled 'ablation on problem structure' that isolates technique-level memorization from surface-level memorization, something no prior perturbation study achieved. The MRR analysis (≈0.986) elegantly proves that embedding-based retrieval cannot distinguish hard variants from originals, meaning any RAG-assisted model would retrieve the wrong solution template — this transforms a measurement paper into an attack surface paper. The failure mode taxonomy (with concrete traced examples like o1-mini outputting 'all integers' when asked for 'smallest integer') makes the memorization claim falsifiable and vivid rather than statistical hand-waving.",
  "limitations_acknowledged": "The authors acknowledge: (1) the dataset is small (279 problems) and entirely manually constructed by expert annotators, making it inherently non-scalable; (2) evaluation excluded tool-use/code-interpreter modes where 'many problems can be trivially solved by brute-force search programs'; (3) the memorization percentage estimates (40% for o1-mini, 25% for Claude-3.5-Sonnet) come from manual inspection of only 20 error cases per model — a very small sample for quantitative claims; (4) there is an acknowledged 'misalignment between model capabilities and annotator perception of difficulty.'",
  "open_questions": [
    "Can hard perturbation generation be automated with formal verification (e.g., SymPy-backed symbolic transforms that provably invalidate specific solution techniques while preserving problem well-formedness)? The manual process doesn't scale and introduces annotator subjectivity about what constitutes a 'different solution method.'",
    "The paper diagnoses mechanical technique application but never connects it to contamination — is the blind technique application rate correlated with the degree of training-set exposure? Their train/test split analysis hints at this (larger drops on train-split problems) but they never formalize the relationship.",
    "Step-level analysis is entirely absent: the paper evaluates only final answers. WHERE in the chain-of-thought does the model commit to the wrong technique? Does it consider and reject the correct approach, or never generate it? Process-level tracing would transform this from a benchmark paper into a mechanistic understanding paper."
  ],
  "building_blocks": [
    "Simple/hard perturbation taxonomy as a principled difficulty axis for adversarial evaluation",
    "MRR-based similarity verification (using text-embedding-3-large) to confirm perturbations are retrieval-indistinguishable from originals",
    "Four-case outcome analysis framework (original×variant correctness) for categorizing model failure modes",
    "ICL competing-effects methodology: measuring correct→wrong and wrong→correct transition rates under demonstration",
    "Manual error trace categorization protocol: assumption ignorance, blind technique application, answer memorization",
    "MATH level-5 as a substrate for competition-level perturbation studies",
    "Pass@k / self-consistency analysis on perturbed variants to test inference-time scaling robustness"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "MATH-Perturb is directly adjacent to CRADE's MaSTer-like variant generation component but exposes three critical gaps that CRADE must fill: (1) perturbations are entirely manual — CRADE's SymPy-backed generation would automate and scale this with provable correctness; (2) evaluation is answer-level only — CRADE's step-level SPA metric would detect exactly WHERE mechanical technique application occurs in the reasoning chain; (3) the paper observes memorization-driven failures but never connects them to contamination detection or produces a calibrated score — CRADE's contamination-aware IRT model would formalize the relationship between training exposure, technique memorization, and the performance drop they measure, turning their descriptive finding ('40% of o1-mini errors are memorization') into a quantitative decomposition (G + C − R). Their MRR≈0.986 finding also validates CRADE's design assumption that adversarial variants must be semantically close to originals to probe genuine capability rather than domain shift."
}
```

## Key Research Craft Takeaways

**What made this paper work as research:**

1. **The taxonomy is the contribution, not the benchmark.** Dozens of papers perturb math benchmarks. What elevates this one is the *principled distinction* between simple and hard perturbations — it reframes the question from "are models robust to noise?" to "do models understand the *structural preconditions* of their own techniques?" That's a sharper, more falsifiable claim.

2. **Controlled comparison design.** By creating matched triplets (original → simple → hard), every problem is its own control. The simple perturbation serves as a sanity check — if a model fails on simple AND hard, it's just a weak model; if it passes simple but fails hard, that's the memorization signal. This within-problem design is what makes the 16.5% drop on o1-mini *meaningful* rather than just a number.

3. **The MRR analysis anticipates the counterargument.** A reviewer would immediately ask: "maybe hard perturbations are just harder problems, not evidence of memorization." The MRR ≈ 0.986 preempts this — the problems are nearly indistinguishable to embedding models, so the performance gap can't be attributed to domain shift or retrieval failure.

4. **For CRADE specifically:** This paper validates the *need* for our framework but highlights that the field is stuck at manual, answer-level, contamination-unaware evaluation. The mechanical technique application finding is precisely the phenomenon CRADE's step-perturbation alignment (SPA) metric would quantify automatically and at scale. Their observation that train-split problems show larger drops than test-split problems is an implicit contamination signal they never formalize — exactly the gap CRADE's joint IRT model fills.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e6d75a2-1ca0-4754-83b4-e2cf3559ff7a",
  "isSidechain": false,
  "requestId": "req_011CbUpfjFMyBxz5hvP54cGz",
  "type": "assistant",
  "uuid": "5d655f59-7db0-49c6-9c32-2d8c1ebff06c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4jeGaEYvKNb1nYQg6pnBM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 528,
      "cache_read_input_tokens": 20424,
      "output_tokens": 2426,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2426,
          "cache_read_input_tokens": 20424,
          "cache_creation_input_tokens": 528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 528
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "5d655f59-7db0-49c6-9c32-2d8c1ebff06c",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze MATH-Perturb paper for research methodology",
  "sessionId": "59298a2e-5f56-4c60-bfbd-6be00ffe6059"
}
```

---
